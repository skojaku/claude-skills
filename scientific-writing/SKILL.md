---
name: scientific-writing
description: Draft and revise multi-page scientific documents (papers, grant proposals) in the user's style. Structures documents for busy readers who skim — skeleton-first drafting loop, claim-carrying headings — and enforces the user's sentence-level voice (terse first-person description over persuasive, blog-like phrasing). Use whenever writing, rewriting, or editing paper or proposal prose, even for a single sentence. For a review or critique request without editing, use the scientific-review skill instead.
---

# Scientific Writing

How the user's scientific documents get written: a reader model and structure rules for busy readers who skim, a phased drafting loop, and the user's sentence-level voice. Reviewing is not this skill's job — the scientific-review skill owns the critics and the review workflow; this skill's drafting loop calls into its `agents/` at the review checkpoints.

- **`style.md`** — the user's voice: sentence rules, register, layout, examples. Read before writing or editing ANY prose, down to one sentence.
- **`workflow.md`** — the drafting–review loop and rewrite entry path. Read when drafting or rewriting more than a paragraph.

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

## Routing

- A wording or sentence-level edit -> read `style.md`, make the edit, run its self-check list. No review passes.
- Drafting from a skeleton, or a rewrite larger than a paragraph -> `style.md` + `workflow.md`.
- A review request without editing -> switch to the scientific-review skill and follow its `workflow.md`.

## Delegation

Where the environment can delegate (subagents, spawned agents, parallel sessions), give each workflow role its own fresh agent. Critics live in the scientific-review skill's `agents/` directory (side-by-side install: `../scientific-review/agents/`); hand a critic only its own agent file plus the exact input that file specifies — never the rest of this skill. Where delegation is unavailable, run each role as a bounded pass that sees only that role's inputs, and disclose in the report that the review was self-run rather than independent.

## After editing

After editing a document file: `git add`, commit, push. End commit messages with the project's `Co-Authored-By` trailer.

## Reporting

Report to the user in Japanese after any edit: what you diagnosed, what changed and why, and what you deliberately left alone. Do not translate the document's own prose.
