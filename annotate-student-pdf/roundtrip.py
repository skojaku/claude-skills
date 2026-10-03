#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = []
# ///
"""Round-trip (EN -> JA -> EN) the comments of a comments.json through the Alfred
"Round Trip" workflow, then apply surgical fixes to what the trip got wrong.

  roundtrip.py run   comments.json [--show-ja] [--force]   -> comments.rt.json
  roundtrip.py apply comments.rt.json edits.json -o comments.final.json

run    Sends each comment's "text" through the workflow's roundtrip.sh, one at a time
       (the workflow writes its result to the clipboard, so parallel runs would collide).
       Adds to each comment: "draft" (your original text), "rt" (the English that came
       back), "rt_info" (route and checker note), "rt_lost" (numbers, names, quoted
       phrases and mid-sentence capitalised words of the draft that are missing from
       the result) and "rt_warn". "text" is left as the draft until `apply`.
       The clipboard is backed up first and restored afterwards (text only).

apply  edits.json maps a comment index (as a string) to either a list of
       [old, new] pairs or the string "draft". Each `old` must occur exactly once in
       that comment's round-trip text, and is replaced by `new`: nothing else changes.
       "draft" puts the unedited draft back. Writes a comments.json for annotate.py.

The comment text, never the student's name or quoted prose, is what leaves the
machine: roundtrip.sh sends it to OpenRouter and DeepL.
"""
import argparse
import difflib
import glob
import json
import os
import re
import subprocess
import sys
from pathlib import Path

FOOTER = re.compile(r"^— (\d+) → (\d+) words.*$", re.M)
JA_MARK = "\n--- 日本語 ---\n"
# `clipboard info` reports AppleScript class names, e.g. "picture" for an image.
# Only text flavours can be backed up with pbpaste, so anything else blocks the run.
TEXT_CLIPBOARD = {"string", "Unicode text", "text", "styled text", "styled Unicode text",
                  "«class utf8»", "«class ut16»", "«class RTF »", "«class HTML»"}
RICH_CLIPBOARD = {"«class RTF »", "«class HTML»"}


def find_script():
    env = os.environ.get("ROUNDTRIP_SH")
    if env:
        return env
    hits = glob.glob(os.path.expanduser(
        "~/dotfiles/alfred/Alfred.alfredpreferences/workflows/*/roundtrip.sh"))
    if len(hits) != 1:
        sys.exit(f"cannot find a single roundtrip.sh ({len(hits)} found); set ROUNDTRIP_SH")
    return hits[0]


def parse_output(raw):
    """Split roundtrip.sh stdout into (english, footer, japanese, warnings).

    The script exits 0 even on failure and prints the error as text, so success
    is recognised by the footer line only. Returns english=None on failure.
    """
    warn = re.findall(r"^⚠ .*$", raw, re.M)
    head, _, ja = raw.partition(JA_MARK)
    m = FOOTER.search(head)
    if not m:
        return None, None, None, [raw.strip()]
    en = head[:m.start()].strip()
    ja = "\n".join(l for l in ja.splitlines() if not l.startswith("⚠ ")).strip()
    return en, m.group(0), ja, warn


def protected_tokens(text):
    """Things a translation trip must not lose: numbers, names, quoted phrases."""
    toks = set(re.findall(r"\d+(?:[.,:]\d+)*", text))
    toks |= set(re.findall(r"\b[A-Za-z]*[a-z][A-Z][A-Za-z]*\b|\b[A-Z]{2,}\b", text))
    toks |= set(re.findall(r'"([^"]+)"', text))
    for sent in re.split(r"(?<=[.!?])\s+|\n+", text):
        words = re.findall(r"[A-Za-z][\w'-]*", sent)[1:]  # first word is capitalised anyway
        toks |= {w for w in words if len(w) > 1 and w[0].isupper()}
    return toks


def missing_tokens(draft, en):
    out = []
    for t in sorted(protected_tokens(draft)):
        pat = re.escape(t) if not t[0].isalnum() or not t[-1].isalnum() else r"\b" + re.escape(t) + r"\b"
        if not re.search(pat, en):
            out.append(t)
    return out


def clipboard_types():
    """Type names on the clipboard, from `clipboard info` ("«class HTML», 563, string, 14, ...")."""
    r = subprocess.run(["osascript", "-e", "clipboard info"], capture_output=True, text=True)
    parts = [p.strip() for p in r.stdout.strip().split(",") if p.strip()]
    return set(parts[0::2])


def pbpaste():
    return subprocess.run(["pbpaste"], capture_output=True,
                          env={**os.environ, "LC_CTYPE": "UTF-8"}).stdout


def pbcopy(data):
    subprocess.run(["pbcopy"], input=data, env={**os.environ, "LC_CTYPE": "UTF-8"})


def cmd_run(args):
    cfg = json.loads(Path(args.comments).read_text())
    script = find_script()
    types = clipboard_types()
    other = sorted(types - TEXT_CLIPBOARD)
    if other and not args.force:
        sys.exit(f"clipboard holds non-text data {other} that cannot be restored; "
                 "copy something else first, or pass --force to overwrite it")
    if types & RICH_CLIPBOARD:
        print("note: clipboard formatting (RTF/HTML) is not restored, only its plain text")
    backup = pbpaste()
    env = {**os.environ, "RW_DONE_SOUND": "/nonexistent", "RW_FAIL_SOUND": "/nonexistent",
           "RW_SHOW_JA": "1" if args.show_ja else "0"}
    failed = 0
    try:
        for i, c in enumerate(cfg["comments"]):
            r = subprocess.run([script, c["text"]], capture_output=True, text=True,
                               env=env, timeout=300)
            en, footer, ja, warn = parse_output(r.stdout)
            c["draft"] = c["text"]
            if en is None:
                failed += 1
                c["rt"], c["rt_info"], c["rt_warn"] = None, None, warn
                print(f"[{i}] FAILED: {warn[0][:200]}")
                continue
            c["rt"], c["rt_info"], c["rt_warn"] = en, footer, warn
            c["rt_lost"] = missing_tokens(c["draft"], en)
            if args.show_ja:
                c["ja"] = ja
            print(f"[{i}] {footer}" + (f" | LOST: {c['rt_lost']}" if c["rt_lost"] else "")
                  + (f" | WARN: {warn}" if warn else ""))
    finally:
        pbcopy(backup)
    out = Path(args.comments).with_suffix(".rt.json")
    out.write_text(json.dumps(cfg, ensure_ascii=False, indent=2))
    print(f"wrote {out}")
    return 1 if failed else 0


def cmd_apply(args):
    cfg = json.loads(Path(args.rt).read_text())
    edits = json.loads(Path(args.edits).read_text())
    unknown = set(edits) - {str(i) for i in range(len(cfg["comments"]))}
    if unknown:
        sys.exit(f"edits refer to missing comment indexes: {sorted(unknown)}")
    for i, c in enumerate(cfg["comments"]):
        e = edits.get(str(i), [])
        if e == "draft" or c.get("rt") is None:
            if c.get("rt") is None and e != "draft":
                print(f"[{i}] no round-trip text; keeping the draft")
            c["text"] = c["draft"]
            print(f"[{i}] draft kept")
        else:
            t = c["rt"]
            for old, new in e:
                n = t.count(old)
                if n != 1:
                    sys.exit(f"[{i}] `old` occurs {n} times, need exactly 1: {old[:60]!r}")
                t = t.replace(old, new)
            a, b = c["rt"].split(), t.split()
            changed = sum(max(i2 - i1, j2 - j1) for tag, i1, i2, j1, j2 in
                          difflib.SequenceMatcher(None, a, b).get_opcodes() if tag != "equal")
            c["text"] = t
            print(f"[{i}] round-trip {len(a)} words -> final {len(b)} | edited {changed} words "
                  f"| {len(e)} edit(s)")
        for k in ("draft", "rt", "rt_info", "rt_lost", "rt_warn", "ja"):
            c.pop(k, None)
    Path(args.out).write_text(json.dumps(cfg, ensure_ascii=False, indent=2))
    print(f"wrote {args.out}")
    return 0


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawTextHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("run")
    r.add_argument("comments")
    r.add_argument("--show-ja", action="store_true")
    r.add_argument("--force", action="store_true", help="run even if the clipboard holds an image/file")
    a = sub.add_parser("apply")
    a.add_argument("rt")
    a.add_argument("edits")
    a.add_argument("-o", "--out", required=True)
    args = ap.parse_args()
    return cmd_run(args) if args.cmd == "run" else cmd_apply(args)


if __name__ == "__main__":
    sys.exit(main())
