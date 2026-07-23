---
name: scientific-writing
description: Draft and revise multi-page scientific documents (papers, grant proposals) in the user's style. Structures documents for busy readers who skim, using a skeleton-first drafting loop, and enforces the user's sentence-level voice (terse first-person description over persuasive, blog-like phrasing). Use whenever writing, rewriting, or editing paper or proposal prose, even for a single sentence. For a review or critique request without editing, use the scientific-review skill instead.
---

# Scientific Writing

This skill overlays the user's personal voice on top of the writing-for-busy-readers skill, which supplies the reader model, document structure rules, and the drafting workflow. Reviewing is not this skill's job — the scientific-review skill owns the review pipeline.

- **`style.md`** — voice, sentence rules, layout, examples. Read before writing or editing ANY prose, down to one sentence.

## Routing

- A wording or sentence-level edit -> read `style.md`, make the edit, run its self-check list. No review passes.
- Drafting or rewriting a paragraph or more -> load the writing-for-busy-readers skill (invoke it by name through the environment's skill mechanism where available; otherwise read `../writing-for-busy-readers/SKILL.md` — the skills are installed side by side) and follow its workflow. Its review phases start their critics from the scientific-review skill's `agents/`; this skill's deep critic is scientific-review's `agents/style-critic.md`, handed the path to `style.md`.
- A review request without editing -> switch to the scientific-review skill and follow its `workflow.md`.

## After editing

After editing a document file: `git add`, commit, push. End commit messages with the project's `Co-Authored-By` trailer.

## Reporting to the user

Report to the user in Japanese after any edit: what you diagnosed, what changed and why, and what you deliberately left alone. Do not translate the document's own prose.
