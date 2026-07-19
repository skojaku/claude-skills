# Review: skim review, adversarial review

The review passes of workflow.md Phases 3–4, also invoked standalone on a review request. SKILL.md's reader model and structure rules are assumed. A review-only invocation reports findings and stops; do not apply fixes until asked.

## Skim review — does the busy reader get the argument?

- Mechanically extract the skim view: headings, first sentence of each paragraph (with one-sentence-per-line layout, the first line after each blank line or heading), figure captions, bold text.
- Give ONLY this extract to a fresh agent started from `agents/skim-critic.md` (per workflow.md's role separation).
- Compare the readback to the takeaway list. Every missed or distorted takeaway marks a first sentence not doing its job, a missing entry-point repetition, or a buried section. Fix at the skeleton level, not by adding text.

## Adversarial review — does the argument survive attack?

- For a section or larger, run with a fresh agent started from `agents/adversarial-critic.md`, given the full section text (not the skeleton).
- For less than a section, the coordinator applies the same checklist inline.
- Fold every confirmed objection into the takeaway list. Fix by conceding, qualifying, realigning evidence, or adding a forward-pointer.

## Reporting

Findings ranked by severity, each with the claim, the objection as a hostile reviewer would voice it, and the concrete fix. Separate one-line wording fixes from design decisions needing the user; state which findings you did not act on and why.
