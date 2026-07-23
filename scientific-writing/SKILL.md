---
name: scientific-writing
description: Draft and revise multi-page scientific documents (papers, grant proposals) in the user's style. Structures documents for busy readers who skim — skeleton-first drafting loop, claim-carrying headings — and enforces the user's sentence-level voice (terse first-person description over persuasive, blog-like phrasing). Use whenever writing, rewriting, or editing paper or proposal prose, even for a single sentence. For a review or critique request without editing, use the scientific-review skill instead.
---

# Scientific Writing

How the user's scientific documents get written: reader model + structure rules (this file), a phased drafting loop (`workflow.md`), the user's voice (`style.md`). Reviewing belongs to the scientific-review skill; the drafting loop calls its `agents/` at review checkpoints.

- `style.md` — voice, sentence rules, layout, examples. Read before writing or editing ANY prose, down to one sentence.
- `workflow.md` — drafting–review loop, rewrite entry path, role/model assignments. Read when drafting or rewriting more than a paragraph.

## Reader model

Busy experts:

1. skim headings, first sentences, figures, bold; descend only where the skim raised interest or doubt;
2. satisfice — a paragraph's first sentence is often the only sentence read;
3. remember gist, not text — a 15-page document leaves ~5 sentences; the writer chooses them;
4. hold one thread; a section braiding three ideas encodes as a blur;
5. read position: sentence opening links back (old), end carries the news (stress position);
6. read out of order — any section can be the entry point.

## Document structure

- **Skeleton stands alone.** Headings + first sentence per paragraph + figures deliver the complete argument.
- **Headings carry claims** ("Mobility embeddings recover field structure", not "Preliminary results"); else a bold lead-in or first sentence.
- **Context, content, conclusion at every scale** — document, section, paragraph.
- **One point per paragraph, point first.** Two point sentences = two paragraphs. No throat-clearing openers.
- **Repeat the core claim at every entry point** (summary, intro, home section), words adapted per scale.
- **Re-anchor at section boundaries** with a one-clause referent restatement ("The mobility embedding from Thrust 1...").
- **Front-load by primacy**, not chronology or work order.
- **Figures read independently.** Caption states what it shows and what it means, without the body text. Per-cell annotations neutral, descriptive.

## Routing

- Wording or sentence-level edit → `style.md`, edit, run its self-check. No review passes.
- Drafting from a skeleton, or rewrite larger than a paragraph → `style.md` + `workflow.md`.
- Review request without editing → scientific-review skill, its `workflow.md`.

## After editing

`git add`, commit (Co-Authored-By trailer), push. Report in Japanese: diagnosis, what changed and why, what was deliberately left alone. Never translate the document's own prose.
