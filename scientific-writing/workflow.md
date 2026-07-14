# Workflow: the drafting–review loop

The phased loop for drafting and rewriting. The reader model and document-structure rules in SKILL.md are assumed. Prose is written in the voice of style.md, and the review phases are specified in critique.md. Draft and revise in explicit passes; do not draft linearly start-to-finish and then polish. For a multi-section document, run the loop per section, then once over the whole document.

## The phases

**Phase 0 — Takeaways.** Before writing, list the 3–5 sentences the busy reader must still hold after putting the document down, plus one sentence per section. Write these down (a scratch file is fine). These are the acceptance criteria for every later review pass. If the user has stated the takeaways, use theirs; otherwise propose the list and confirm before drafting at length.

**Phase 1 — Skeleton draft.** Write only the headings and the first sentence of every planned paragraph. Read this skeleton against the takeaway list. Fix ordering, missing steps, and buried claims here, where a change costs one line, not after paragraphs are built on top. Do not proceed until the skeleton alone tells the story.

**Phase 2 — Expand.** Grow each skeleton sentence into its paragraph, point first, in the voice of style.md. Expansion must not demote the skeleton sentence from first position.

**Phase 3 — Skim review.** Run the skim review of critique.md: extract the skim view, hand it to a fresh subagent, compare the readback to the Phase 0 takeaways, and fix misses at the skeleton level.

**Phase 4 — Adversarial review and risk–return audit.** Run the adversarial review of critique.md on the full text, then the risk–return audit on every element the attack landed on. Phase 3 tests whether the reader gets the argument; this tests whether the argument survives someone trying to break it. Fold every confirmed objection back into the Phase 0 takeaways as a claim the revision must now defend. When the audit says an element costs more criticism than it returns evidence, redirect its function instead of defending its prose, and flag redirects that change the design to the user before applying them.

**Phase 5 — Deep review.** For the reader who does descend, check every touched sentence against the self-check list in style.md.

**Phase 6 — Attention budget.** Per section, name its one thread in a sentence. Anything in the section that does not serve that thread gets cut, demoted to a clause, or moved. Cut before adding. Drop preliminary numbers that are not load-bearing.

**Loop.** Repeat Phases 3–6 until the skim readback returns the intended takeaways without distortion, the adversarial pass raises no unanswered objection, and the deep check is clean. Two rounds are typical; one is suspicious. Then commit and push per SKILL.md.

## Rewriting existing text

The common invocation is a rewrite, not a blank page. The same phases apply, entered in diagnostic order, and scaled to the size of the passage.

- **Recover the takeaways first (Phase 0).** Take them from the user's request or `#Claude` comments when given. Otherwise infer what the passage is trying to leave with the reader, state that inference in one or two sentences, and confirm it before rewriting at length. A rewrite that polishes prose around the wrong takeaway is wasted work.
- **Extract the existing skeleton before touching prose (Phase 1).** Read the headings and first sentences of the passage as the skimming reader would. Diagnose at this level: buried points, first sentences that carry context instead of claims, sections braiding two threads. Fix structure by reordering and promoting sentences before rewriting any of them. Most weak passages fail here, not at the sentence level.
- **Rewrite surgically (Phase 2).** Keep sentences that already comply. Every changed line should trace to a diagnosed structural fault or a sentence-rule violation, not to taste. Match the density and idiom of the surrounding text that is not being rewritten.
- **Scale the review to the scope.** For a paragraph or a few sentences, Phases 5–6 inline suffice, and the adversarial checks of critique.md apply to any claim the passage rests on; skip the subagents. For a section or more, run the full Phase 3 skim review and Phase 4 adversarial review with fresh subagents, feeding the skim reviewer the post-rewrite skeleton and the adversarial reviewer the full text. For edits inside a larger document, check the seams: the rewritten passage must still link backward from its first sentence and hand off cleanly to what follows.
