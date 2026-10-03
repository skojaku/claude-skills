---
name: annotate-student-pdf
description: Put the user's own feedback on a student's PDF (assignment, project proposal, report) into the file as highlight-linked popup comments, rewriting blunt feedback into motivating wording without dropping the critique. Use when the user is reviewing student work and gives feedback to be annotated onto a PDF, e.g. "学生の課題をレビュー", "PDFにアノテーション", "フィードバックをPDFに入れて", or pastes comments for a named student. Also covers suggesting references to add to those comments. Not for generating a critique of a paper yourself (scientific-review), uploading feedback or grades to Brightspace (brightspace), or general PDF edits (pdf).
---

# Annotate Student PDFs

The user writes feedback in English (often dictated, in speaking order, sometimes without page numbers). You place each point as a highlight with a popup comment in a **copy** of the student's PDF, in a tone that motivates.

## Workflow

1. **Find the file.** Brightspace downloads are one folder per student (`<id> - <Last, First> - <date>/<file>`) plus an `index.html` listing submissions. Some students submit more than once, submit several files, or are a team (the names are in `index.html` comments); flag this and take the latest unless told otherwise. A `.docx` needs a PDF first: check `which soffice`, else ask the user to export it.
2. **Read the text with page markers** (PyMuPDF `page.get_text()`), then map each point of the feedback to the most specific sentence it is about. Spoken feedback can retract itself ("oh okay, I got it"): drop the retracted point, but a realisation the user reached can still sharpen another comment.
3. **Rewrite the tone** (below) and write `comments.json`.
4. **Run** `uv run --script ~/.claude/skills/annotate-student-pdf/annotate.py comments.json`. It needs no setup (dependencies are inline). Fix every NOT FOUND / AMBIGUOUS quote; never place by guess.
5. **Verify.** All comments placed; render a page or two to PNG and look at them; `qpdf --check` the output; the original must still have no annotations and be unchanged.
6. **Report in Japanese**: output path; each comment as written (English); judgment calls (anchor choices, dropped points, any wording added beyond the user's own); what was verified and what was not (popup display in the user's viewer, PDF Expert, cannot be checked from here).

## Tone rule

The user knows their comments come out harsh. Keep every point and its substance; change only how it lands.

- Say what to do next ("tie each question to something you will do with the data") rather than only what is missing.
- A sharp question can stay a question, introduced as "the key place to strengthen".
- Never invent praise. Positive framing comes only from observable facts or the user's own words ("interesting", "small enough to draw").
- Anything added beyond the user's words must be a direct consequence of their point, hedged ("may"), and flagged in the report.
- No overall sticky note unless the user gives an overall comment. Offer one instead, with strengths you actually saw in the document, for the user to confirm.
- Comment text is English (the student reads it); the report to the user is Japanese. Never translate the student's prose.

## Reference suggestions (only when asked)

Delegate to a general-purpose sub-agent. Have it read the user's paper "Constructing networks by filtering correlation matrices: A null model approach" (Kojaku & Masuda, arXiv:1903.10805) in full and choose **only from its bibliography**, never from memory. State the requested split (e.g. one graphical lasso, two on correlation matrices, one modularity for correlation matrices, at most five total), list what the student already cites so it is excluded, and ask for full citations cross-checked against the web, plus why each fits this student. Show the user the candidates and where you would attach each; edit the PDF only after they agree. Attach each as "suggested reading", phrased as an invitation, after a blank line at the end of the closest existing comment (or a new comment on the relevant term).

## comments.json

```json
{
  "src": "<download root>/<student folder>/file.pdf",
  "dst": "<download root>/annotated/<student folder>/file.pdf",
  "author": "S. Kojaku",
  "overall": "optional sticky note on page 1",
  "comments": [
    {"page": 2, "quote": "exact sentence from the PDF", "text": "popup comment"}
  ]
}
```

- Outputs go to `annotated/<student folder>/<same filename>` under the download root. Never write over an original (the script refuses). Re-running overwrites only the annotated copy.
- The download root is usually not a git repo, so the "commit and push after editing" rule cannot apply there; say so.

## Gotchas

- Quote matching ignores whitespace but not hyphenation: a word broken across lines in the PDF ("differ-ent") will not match, so quote a segment that avoids it. Math symbols and ligatures may not match either.
- A quote must occur exactly once on its page. If it is AMBIGUOUS, quote more context. A wrong `page` hint is tolerated if the quote is unique in the document.
- `page` is the 1-based PDF page index, not the printed page number.
- Long comments get a taller popup (capped); viewers differ in how they draw it, so ask the user to check the first output.
