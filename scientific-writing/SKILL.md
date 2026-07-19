---
name: scientific-writing
description: Draft and revise multi-page scientific documents (papers, grant proposals) in the user's style. Structures documents for busy readers who skim, using a skeleton-first drafting loop with skim-reader and adversarial claim-and-evidence review passes. Also enforces the user's sentence-level voice (terse first-person description over persuasive, blog-like phrasing). Use whenever writing, rewriting, or reviewing paper or proposal prose, even for a single paragraph.
---

# Scientific Writing

This skill overlays the user's personal voice and grant-specific review on top of the writing-for-busy-readers skill, which supplies the reader model, document structure rules, and the drafting/review workflow.

- **`style.md`** — voice, sentence rules, layout, examples. Read before writing or editing ANY prose, down to one sentence.
- **`review-grant.md`** — risk–return audit for grant/proposal design elements. Read after the adversarial review pass.

## Routing

- Any prose edit, however short -> read `style.md` first.
- Drafting or rewriting a paragraph or more -> load the writing-for-busy-readers skill (invoke it by name through the environment's skill mechanism where available; otherwise read `../writing-for-busy-readers/SKILL.md` — the two skills are installed side by side) and follow its workflow.
- A review request -> run writing-for-busy-readers' `review.md`, then this skill's `review-grant.md`. Start the adversarial critic from writing-for-busy-readers' `agents/adversarial-critic.md`. Start the style deep-check from this skill's `agents/style-critic.md`.

## After editing

After editing a document file: `git add`, commit, push. End commit messages with the project's `Co-Authored-By` trailer.

## Reporting to the user

Report to the user in Japanese after any edit or review-only pass: what you diagnosed, what changed (or was found) and why, and what you deliberately left alone. Do not translate the document's own prose.
