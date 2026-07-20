---
name: scientific-review
description: Review scientific documents (papers, grant proposals) without editing them. Runs a skim readback, an adversarial claim-and-evidence attack, a grant-specific risk–return audit, and a sentence-level style deep-check, then reports findings. Use for any review or critique request on paper or proposal prose. For writing, rewriting, or wording edits, use the scientific-writing skill instead.
---

# Scientific Review

Review pipeline for the user's scientific documents. It layers grant-specific review on top of the writing-for-busy-readers skill's review passes and checks sentences against the scientific-writing skill's `style.md`. A review-only invocation reports findings and stops; do not edit the document until asked. When the user then asks for fixes, apply them under the scientific-writing skill.

- **`review-grant.md`** — risk–return audit for grant/proposal design elements. Read after the adversarial review pass.
- **`agents/style-critic.md`** — deep line-edit check of touched sentences against `style.md`.

## Pipeline

1. Run writing-for-busy-readers' `review.md` (skim review, then adversarial review). Load that skill by name through the environment's skill mechanism where available; otherwise read `../writing-for-busy-readers/review.md` — the skills are installed side by side. Start the adversarial critic from its `agents/adversarial-critic.md`.
2. On a grant or proposal document, run this skill's `review-grant.md`.
3. Start the style deep-check from this skill's `agents/style-critic.md`, handing it the target passage and the path to `../scientific-writing/style.md`.

## Reporting to the user

Report in Japanese, following review.md's reporting format: findings ranked by severity, the concrete fix each needs, and which findings need a decision from the user. Do not translate the document's own prose.
