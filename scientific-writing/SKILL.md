---
name: scientific-writing
description: Draft and revise multi-page scientific documents (papers, grant proposals) in the user's style. Structures documents for busy readers who skim, using a skeleton-first drafting loop with skim-reader and adversarial claim-and-evidence review passes. Also enforces the user's sentence-level voice (terse first-person description over persuasive, blog-like phrasing). Use whenever writing, rewriting, or reviewing paper or proposal prose, even for a single paragraph.
---

# Scientific Writing for Busy Readers

Shared foundation. Task rules live in three companion files; read the ones the task needs before producing anything. Never draft from this file alone.

- **`style.md`** — voice, sentence rules, layout, examples. Read before writing or editing ANY prose, down to one sentence.
- **`workflow.md`** — the drafting–review loop and rewrite entry path. Read when drafting or rewriting more than a paragraph.
- **`critique.md`** — skim review, adversarial review, risk–return audit. Read for review phases and any review-only request.

## Reader model

Every rule derives from how busy experts read:

1. Readers skim: headings, first sentences, figures, bold text; they descend only where the skim raised interest or doubt.
2. Skimming is satisficing — the first sentence of a paragraph is often the only sentence read.
3. Readers remember gist, not text. A 15-page document leaves about five sentences; the writer's job is to choose them.
4. Working memory holds one thread; a section braiding three ideas encodes as a blur.
5. Sentence position assigns meaning: opening links back (old information), end carries the news (stress position).
6. Long documents are read out of order; any section can be the entry point.

## Document structure

- **The skeleton stands alone.** Headings + first sentence of every paragraph + figures must deliver the complete argument.
- **Headings carry claims** where the format allows ("Mobility embeddings recover field structure", not "Preliminary results"); else push the claim into a bold lead-in or first sentence.
- **Context, content, conclusion at every scale** — document, section, paragraph.
- **One point per paragraph, point first.** Two point sentences means two paragraphs. Never open with throat-clearing context.
- **Repeat the core claim at every entry point** (summary, introduction, the section where the work lives), in words adapted to each scale.
- **Re-anchor at section boundaries** with a one-clause restatement of the referent ("The mobility embedding from Thrust 1...").
- **Front-load by primacy**, not chronology or work order.
- **Figures read independently.** Each caption states what the figure shows and what it means, without requiring the body text. Per-cell annotations stay neutral and descriptive.

## After editing

After editing a document file: `git add`, commit, push. End commit messages with the project's `Co-Authored-By` trailer.

## Reporting to the user

Report to the user in Japanese after any edit or review-only pass: what you diagnosed, what changed (or was found) and why, and what you deliberately left alone. Do not translate the document's own prose.
