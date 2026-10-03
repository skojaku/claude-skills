# /// script
# requires-python = ">=3.9"
# dependencies = ["pymupdf"]
# ///
"""Annotate a PDF with highlight-linked popup comments.

Usage: uv run --script annotate.py comments.json

comments.json:
{
  "src": "path/to/original.pdf",
  "dst": "path/to/annotated/copy.pdf",
  "author": "S. Kojaku",
  "overall": "optional sticky note on page 1",
  "comments": [
    {"page": 2, "quote": "text to highlight", "text": "comment shown in popup"}
  ]
}

"page" is 1-based (the PDF's page index, not printed page labels) and optional.
A quote that is not found, or that occurs more than once on its page, is reported
and skipped: it is never placed by guess. Exit status is 1 if any quote was skipped.
"""
import json
import re
import sys
from pathlib import Path

import pymupdf

HIGHLIGHT = (1.0, 0.93, 0.35)  # soft yellow


def norm(s):
    return re.sub(r"\s+", " ", s).strip()


def popup_rect(page, anchor, text="", w=290):
    """Popup window just below the highlight, kept inside the page.

    Height grows with the comment so longer comments are readable without scrolling.
    """
    h = min(300, max(110, 45 + 0.55 * len(text)))
    r = page.rect
    x0 = min(max(anchor.x0, r.x0 + 10), r.x1 - w - 10)
    y0 = min(anchor.y1 + 4, r.y1 - h - 10)
    return pymupdf.Rect(x0, y0, x0 + w, y0 + h)


def locate(doc, quote, page_no=None):
    """Find quote. Returns (page, quads, status); status is 'ok', 'missing' or 'ambiguous'.

    A wrong page hint falls back to a whole-document search, but only an
    unambiguous single match is accepted.
    """
    q = norm(quote)
    pages = [doc[page_no - 1]] if page_no else list(doc)
    found = []
    for page in pages:
        n = norm(page.get_text()).count(q)
        if n > 1:
            return page, None, "ambiguous"
        if n == 1:
            found.append(page)
    if not found and page_no:
        return locate(doc, quote, None)
    if len(found) != 1:
        return None, None, ("ambiguous" if found else "missing")
    page = found[0]
    # quads=True keeps a multi-line match as one quad per line
    quads = page.search_for(q, quads=True)
    return (page, quads, "ok") if quads else (None, None, "missing")


def main(cfg_path):
    cfg = json.loads(Path(cfg_path).read_text())
    src, dst = Path(cfg["src"]), Path(cfg["dst"])
    if src.resolve() == dst.resolve():
        sys.exit("refusing to overwrite the original: dst must differ from src")
    author = cfg.get("author", "Reviewer")
    doc = pymupdf.open(src)
    skipped, placed = [], []

    for c in cfg.get("comments", []):
        page, quads, status = locate(doc, c["quote"], c.get("page"))
        if status != "ok":
            skipped.append((status, c))
            continue
        annot = page.add_highlight_annot(quads=quads)
        annot.set_colors(stroke=HIGHLIGHT)
        annot.set_info(content=c["text"], title=author)
        annot.update()
        # Explicit Popup object so every viewer has a window to show; closed by default.
        annot.set_popup(popup_rect(page, annot.rect, c["text"]))
        annot.set_open(False)
        placed.append((page.number + 1, c.get("page"), c["quote"]))

    if cfg.get("overall"):
        p0 = doc[0]
        note = p0.add_text_annot(
            pymupdf.Point(p0.rect.width - 40, 20), cfg["overall"], icon="Note"
        )
        note.set_info(title=author)
        note.set_colors(stroke=(1.0, 0.8, 0.2))
        note.set_open(False)
        note.update()

    dst.parent.mkdir(parents=True, exist_ok=True)
    doc.save(dst, garbage=3, deflate=True)
    print(f"saved: {dst}")
    for pg, hint, q in placed:
        moved = f"  (hint p.{hint} was wrong)" if hint and hint != pg else ""
        print(f"  placed p.{pg}: {q[:70]!r}{moved}")
    for status, c in skipped:
        why = "NOT FOUND" if status == "missing" else "AMBIGUOUS (occurs more than once; quote more context)"
        print(f"  {why} (p.{c.get('page')}): {c['quote'][:70]!r}")
    return 1 if skipped else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
