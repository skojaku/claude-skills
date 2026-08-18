#!/usr/bin/env python3
"""Process- and generator-hygiene checks — the automatable lessons from REVIEW_PLAYBOOK.md.

Each check here replaces a shell incantation the playbook used to ask reviewers
to run by hand:

  - writer processes alive   (was: ps -ax | grep make_figures|pdflatex)
  - private drawing helpers  (was: grep 'def _rect|_fill|_disc...' figures/*.py)
  - guards defined, never called (was: grep every assert_*/check_* for call sites)
  - PNG deleted before regen (was: os.remove(out) before writing)
  - generator collects all failures (was: try/except per figure, exit at end)

Run standalone:  python3 -m gatelib hygiene <module_dir>
Exit 0 = clean, 1 = hygiene failure found.
"""
import glob
import os
import re
import subprocess
import sys

WRITER_PATTERNS = ("make_figures", "make_animations", "pdflatex", "marp ")


def check_writer_processes():
    """Any figure/render writer process alive right now? Fail before rendering.

    A green render is only meaningful if nothing else can still write into the
    directory. Silence from your own agents does not prove this — look.
    """
    try:
        out = subprocess.run(
            ["ps", "-o", "pid=,command=", "-ax"],
            capture_output=True, text=True,
        ).stdout
    except Exception as e:
        print(f"  WARN writer-process check could not run ps: {e}")
        return []
    hits = []
    for line in out.splitlines():
        if "grep" in line:
            continue
        if any(p in line for p in WRITER_PATTERNS):
            hits.append(line.strip())
    return hits


def _figure_sources(module_dir):
    return sorted(glob.glob(os.path.join(module_dir, "figures", "*.py")))


def check_private_helpers(module_dir):
    """Private drawing helpers bypass the shared primitive = hole in every gate."""
    pat = re.compile(r"^\s*def\s+_(rect|fill|disc|node|edge|polygon|arrow|label)\b")
    hits = []
    for src in _figure_sources(module_dir):
        with open(src) as fh:
            for i, line in enumerate(fh, 1):
                if pat.match(line):
                    hits.append(f"{os.path.basename(src)}:{i}: {line.strip()}")
    return hits


def check_uncalled_guards(module_dir):
    """An assertion that is never called is not a check.

    Find `def assert_*` / `def check_*` in figures/*.py and verify each name
    appears at least once more (a call site) somewhere in the figure sources.
    """
    defpat = re.compile(r"^\s*def\s+((?:assert|check)_[A-Za-z0-9_]+)\s*\(")
    defined = {}   # name -> "file:line"
    bodies = {}    # src -> text
    for src in _figure_sources(module_dir):
        with open(src) as fh:
            text = fh.read()
        bodies[src] = text
        for i, line in enumerate(text.splitlines(), 1):
            m = defpat.match(line)
            if m:
                defined[m.group(1)] = f"{os.path.basename(src)}:{i}"
    uncalled = []
    for name, loc in defined.items():
        calls = sum(len(re.findall(rf"\b{name}\s*\(", text)) for text in bodies.values())
        if calls <= 1:  # the definition itself
            uncalled.append(f"{loc}: def {name}() — never called")
    return uncalled


def check_delete_before_regen(module_dir):
    """Figure writers should delete the PNG before writing, so a green build
    cannot report success for bytes written by another process."""
    warnings = []
    for src in _figure_sources(module_dir):
        with open(src) as fh:
            text = fh.read()
        writes = ("savefig" in text) or (".write(" in text and ".png" in text)
        deletes = ("os.remove(" in text) or ("os.unlink(" in text) or (".unlink(" in text)
        if writes and not deletes:
            warnings.append(
                f"{os.path.basename(src)}: writes PNGs but never deletes first"
            )
    return warnings


def check_collect_all_failures(module_dir):
    """A generator that stops at the first failed assertion hides the rest.
    Heuristic: a generator containing multiple figures should catch
    AssertionError per figure and exit at the end."""
    warnings = []
    for src in _figure_sources(module_dir):
        with open(src) as fh:
            text = fh.read()
        n_fig = len(re.findall(r"^\s*def\s+(?:fig|figure|make)_", text, re.M))
        if n_fig >= 5 and "except AssertionError" not in text:
            warnings.append(
                f"{os.path.basename(src)}: {n_fig} figures, no per-figure "
                "AssertionError collection (stops at first failure)"
            )
    return warnings


def run(module_dir):
    """Run all hygiene checks. Returns exit code (0 clean, 1 failures)."""
    failures = 0

    print("── hygiene: writer processes ──")
    hits = check_writer_processes()
    if hits:
        failures += len(hits)
        print("  FAIL writer process(es) alive — hold them before rendering:")
        for h in hits:
            print(f"    {h}")
    else:
        print("  ok — no figure/render writers running")

    if os.path.isdir(os.path.join(module_dir, "figures")):
        print("── hygiene: figure generators ──")
        hits = check_private_helpers(module_dir)
        if hits:
            failures += len(hits)
            print("  FAIL private drawing helpers bypass shared primitives:")
            for h in hits:
                print(f"    {h}")
        hits = check_uncalled_guards(module_dir)
        if hits:
            failures += len(hits)
            print("  FAIL guards defined but never called:")
            for h in hits:
                print(f"    {h}")
        for w in check_delete_before_regen(module_dir):
            print(f"  WARN {w}")
        for w in check_collect_all_failures(module_dir):
            print(f"  WARN {w}")
        if failures == 0:
            print("  ok")
    else:
        print("(no figures/ directory — generator checks skipped)")

    if failures:
        print(f"\nhygiene: {failures} failure(s)")
        return 1
    print("\nhygiene: clean")
    return 0


if __name__ == "__main__":
    sys.exit(run(sys.argv[1] if len(sys.argv) > 1 else "."))
