# Workflow: the drafting–review loop

Phased loop for drafting and rewriting, harness-agnostic. SKILL.md's reader model and structure rules are assumed; reviews follow review.md. Draft in explicit passes, not linearly with a polish at the end. For a multi-section document, run the loop per section, then once over the whole document.

## Roles

Separate deciding, writing, and attacking. Where the environment can delegate (subagents, spawned agents, parallel sessions), give each role its own fresh agent. Where it cannot, run each role as a separate bounded pass with only that role's inputs in view, and state in the report that reviews were self-run — a drafter grading its own text is a weaker guarantee than an independent reader.

- **Planner.** Owns takeaways, skeleton, attention-budget pass. Reads critic findings against the takeaways, decides which to act on, writes revision briefs (diagnosed faults, not rewritten sentences). Highest-judgment role; give it the strongest reasoning capacity available.
- **Editor.** Expands the skeleton into prose or rewrites diagnosed passages surgically, self-checks against the invoking skill's sentence-level rules, and is the only role that writes files. Executes plans it did not set. Lightest sufficient capacity.
- **Critics.** Spawn fresh each round; their value is uncontaminated judgment. Invoked in the `agents/` directory of this skill (or an invoking skill's own `agents/`). Input contract is self-described in each agent file — do not hand a critic anything beyond what its file specifies.

The coordinator (the session agent) owns user communication, sequencing, and the final commit; it does not draft prose or judge quality itself. Where continuing an agent's conversation is supported, send follow-ups there; otherwise include prior output in the new prompt.

## Phases

**0 — Takeaways (planner).** The 3–5 sentences the busy reader must retain, plus one per section. This list is the acceptance criteria for every review. If the user stated takeaways, use theirs; otherwise confirm the planner's list with the user before drafting at length.

**1 — Skeleton (planner).** Headings and the first sentence of every planned paragraph. Fix ordering, missing steps, and buried claims here, where a change costs one line. Do not proceed until the skeleton alone tells the story.

**2 — Expand (editor).** Grow each skeleton sentence into its paragraph, point first, in the invoking skill's voice, without demoting any skeleton sentence from first position. Coordinator checks the seams.

**3 — Skim review.** Run review.md's skim review.

**4 — Adversarial review.** Run review.md's adversarial review. If a companion skill defines a further audit on top (e.g. scientific-review's review-grant.md for grant documents), run it here too.

**5 — Deep review.** Fresh deep critic spot-checks touched sentences against the invoking skill's sentence-level self-check list.

**6 — Attention budget (planner).** Name each section's one thread in a sentence. Anything not serving it gets cut, demoted to a clause, or moved. Cut before adding.

**Loop.** Repeat 3–6 until the skim readback returns the takeaways undistorted, no unanswered objection remains, and the deep check is clean. Two rounds typical; one is suspicious. Then hand back to the invoking skill for finalization (commit rules live there).

## Rewriting existing text

The common invocation. Same phases, entered in diagnostic order, scaled to the passage.

- **Recover takeaways first.** From the user's request or comments addressed to the assistant in the source. Otherwise infer the intended takeaway, state it in one or two sentences, and confirm before rewriting at length. Polishing prose around the wrong takeaway is wasted work.
- **Extract the existing skeleton before touching prose.** Read headings and first sentences as the skimmer would. Diagnose at this level: buried points, first sentences carrying context instead of claims, sections braiding two threads. Reorder and promote before rewriting any sentence. Most weak passages fail here, not at the sentence level.
- **Rewrite surgically.** The revision brief lists diagnosed faults and the sentences that already comply and must survive. Every changed line traces to a structural fault or a sentence-rule violation, not to taste. Match the density and idiom of surrounding untouched text.
- **Scale roles to scope.** For a paragraph or a few sentences, the coordinator works alone: edit inline, apply the checklist in agents/adversarial-critic.md inline to load-bearing claims, run Phases 5–6 itself. For a section or more, use full role separation. For edits inside a larger document, check the seams: the rewritten passage must link backward from its first sentence and hand off cleanly.
