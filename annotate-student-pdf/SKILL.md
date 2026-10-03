---
name: annotate-student-pdf
description: Put the user's own feedback on a student's PDF (assignment, project proposal, report) into the file as highlight-linked popup comments, rewriting blunt feedback into motivating wording without dropping the critique, then running every comment through the Alfred round-trip translation (EN→JA→EN) and surgically repairing what the trip broke. Use when the user is reviewing student work and gives feedback to be annotated onto a PDF, e.g. "学生の課題をレビュー", "PDFにアノテーション", "フィードバックをPDFに入れて", or pastes comments for a named student. Also covers suggesting references to add to those comments. Not for generating a critique of a paper yourself (scientific-review), uploading feedback or grades to Brightspace (brightspace), or general PDF edits (pdf).
---

# Annotate Student PDFs

The user writes feedback in English (often dictated, in speaking order, sometimes without page numbers). You place each point as a highlight with a popup comment in a **copy** of the student's PDF, in a tone that motivates, after the English has been through a round trip.

## Workflow

1. **Find the file.** Brightspace downloads are one folder per student (`<id> - <Last, First> - <date>/<file>`) plus an `index.html` listing submissions. Some students submit more than once, submit several files, or are a team (the names are in `index.html` comments); flag this and take the latest unless told otherwise. A `.docx` needs a PDF first: check `which soffice`, else ask the user to export it.
2. **Read the text with page markers** (PyMuPDF `page.get_text()`), then map each point of the feedback to the most specific sentence it is about. Spoken feedback can retract itself ("oh okay, I got it"): drop the retracted point, but a realisation the user reached can still sharpen another comment.
3. **Rewrite the tone** (below) and write `comments.json`.
4. **Round trip** (below): `roundtrip.py run`, review, `roundtrip.py apply`. Skip only if the user says so.
5. **Annotate**: `uv run --script ~/.claude/skills/annotate-student-pdf/annotate.py comments.final.json`. It needs no setup (dependencies are inline). Fix every NOT FOUND / AMBIGUOUS quote; never place by guess.
6. **Verify.** All comments placed; render a page or two to PNG and look at them; `qpdf --check` the output; the original must still have no annotations and be unchanged.
7. **Report in Japanese, and show the comments in the chat.** Print every final comment in full, in English as the student will read it, each under a heading with its page and a short excerpt of the highlighted text. Never replace them with a summary, a count, or only the output path: popup comments cannot be read without opening the PDF in a viewer, and the user needs to read the exact wording to veto it. Then give: the output path; what the round trip got wrong and how it was fixed; judgment calls (anchor choices, dropped points, any wording added beyond the user's own); what was verified and what was not (popup display in the user's viewer, PDF Expert, cannot be checked from here).

## Tone rule

The user knows their comments come out harsh. Keep every point and its substance; change only how it lands.

- Say what to do next ("tie each question to something you will do with the data") rather than only what is missing.
- A sharp question can stay a question, introduced as "the key place to strengthen".
- Never invent praise. Positive framing comes only from observable facts or the user's own words ("interesting", "small enough to draw").
- Anything added beyond the user's words must be a direct consequence of their point, hedged ("may"), and flagged in the report.
- No overall sticky note unless the user gives an overall comment. Offer one instead, with strengths you actually saw in the document, for the user to confirm.
- Comment text is English (the student reads it); the report to the user is Japanese. Never translate the student's prose.

## Round trip

Every comment goes through the user's Alfred "Round Trip" workflow: Gemini writes the Japanese, DeepL says it back in English, a checker compares with the original. The detour rebuilds the English from its meaning. It also introduces mistranslations, so each result is read against its draft and repaired surgically.

```
S=~/.claude/skills/annotate-student-pdf
uv run --script $S/roundtrip.py run comments.json [--show-ja]     # -> comments.rt.json
# read draft vs "rt" for each comment, write edits.json
uv run --script $S/roundtrip.py apply comments.rt.json edits.json -o comments.final.json
```

`run` prints per comment the route, the checker's verdict, and `LOST` tokens (numbers, names, quoted phrases, mid-sentence capitalised words of the draft that are missing from the result). Use `--show-ja` to see which leg dropped something.

**What counts as a mistranslation (fix it):**
- a changed word: "gap" → "point of difference", "as the threshold varies" → "fluctuations", "meaningful" → "validity";
- changed strength or modality: advice turned into obligation ("would help" → "it is necessary"), "may" dropped, praise weakened ("very good" → "reasonable");
- changed agency: advice to the student turned into "we introduce…" or an impersonal passive, "If it were up to me" added;
- a qualifier that moved: a parenthetical now attached to the wrong word, "to each other" dropped;
- a term taken from the student's document altered ("charging locations" → "charging stations");
- any change to a suggested-reading citation: compare those paragraphs with the draft character by character;
- a comment that came back harsher or more impersonal than the draft.

Leave alone: formality, word choice and rhythm that mean the same thing.

**Surgical means:** in `edits.json` map the comment index (string) to `[[old, new], ...]`, where `old` is a span of the round-trip text that occurs exactly once and `new` restores the draft's meaning. `apply` refuses anything else and prints how many words each comment changed. Do not rewrite a comment wholesale; if a result is beyond repair, use `"draft"` in place of the list to keep the draft. A comment with no entry is taken as returned.

**Constraints:**
- Needs the network and an OpenRouter key (DeepL key optional) in the macOS Keychain. The workflow is found under `~/dotfiles/alfred/Alfred.alfredpreferences/workflows/*/roundtrip.sh`; set `ROUNDTRIP_SH` to override. It exits 0 even on failure and prints the error as text, so `run` reports a missing success footer as FAILED. If the round trip cannot run, tell the user; do not silently skip.
- The route in the footer should read `DeepL`. If it names only Gemini, DeepL failed and Gemini took the way back; say so in the report.
- Only the comment text is sent (to OpenRouter and DeepL). The `quote` field is not sent. Do not put the student's name or their prose inside a comment.
- The workflow writes its result to the clipboard. `run` backs the clipboard up and restores it afterwards (plain text only, so RTF/HTML formatting is lost), refuses to run if an image or file is on it unless `--force`, silences the workflow's sounds, and runs one comment at a time. macOS may still show notification banners. Mention the clipboard in the report.
- Cost is under 1¢ per comment. The workflow's default tone is "terse" (`RW_TONE`); in use it kept praise that carried meaning, but check that encouragement survived.

## Reference suggestions (only when asked)

Delegate to a general-purpose sub-agent. Have it read the user's paper "Constructing networks by filtering correlation matrices: A null model approach" (Kojaku & Masuda, arXiv:1903.10805) in full and choose **only from its bibliography**, never from memory. State the requested split (e.g. one graphical lasso, two on correlation matrices, one modularity for correlation matrices, at most five total), list what the student already cites so it is excluded, and ask for full citations cross-checked against the web, plus why each fits this student. Show the user the candidates and where you would attach each; edit the PDF only after they agree. Attach each as "suggested reading", phrased as an invitation, after a blank line at the end of the closest existing comment (or a new comment on the relevant term). The round trip applies to these comments too, and the citation paragraph must come back unchanged.

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
