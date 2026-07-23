---
name: writing-for-busy-readers
description: Structure and draft long-form text (reports, docs, papers, proposals) for busy readers who skim. Skeleton-first drafting loop with review checkpoints; the critics those checkpoints call live in the scientific-review skill. Usable standalone or as the foundation other skills (e.g. scientific-writing) build domain-specific voice on top of. For a review-only request, use scientific-review directly.
---

# Writing for Busy Readers

Shared foundation. Task rules live in companion files; read the ones the task needs before producing anything. Never draft from this file alone. Reviewing is not this skill's job — the scientific-review skill owns the critics and the review workflow; this skill's drafting loop calls into its `agents/` at the review checkpoints.

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

- Drafting from a skeleton, or a rewrite larger than a paragraph -> `workflow.md`.
- A review request without editing -> the scientific-review skill.
- Starting a critic (workflow.md Phases 3–5): critics live in the scientific-review skill's `agents/` directory (side-by-side install: `../scientific-review/agents/`). Hand a critic only its own agent file plus the exact input the file specifies. Do not hand a critic the rest of this skill.

## Delegation

Where the environment can delegate (subagents, spawned agents, parallel sessions), give each role its own fresh agent, passing it only the relevant `agents/*.md` file's content plus the target text as its instructions. Where it cannot, run that role as a bounded pass that sees only that role's inputs, and disclose in the report that the review was self-run rather than independent.
