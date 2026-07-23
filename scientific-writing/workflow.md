# Workflow: the drafting–review loop

Phased loop, harness-agnostic. SKILL.md's reader model and structure rules assumed; critics come from `../scientific-review/agents/`. Draft in explicit passes, not linearly with a polish at the end. Multi-section document: loop per section, then once over the whole document.

## Roles

Separate deciding, writing, attacking. Fresh subagent per role where the environment allows; else run each role as a bounded pass seeing only that role's inputs, and disclose in the report that reviews were self-run.

- **Planner** (Opus-tier). Owns takeaways, skeleton, attention budget. Reads critic findings against the takeaways, decides which to act on, writes revision briefs — diagnosed faults, not rewritten sentences.
- **Editor** (Sonnet-tier; Haiku for pure wording). Expands skeleton into prose or rewrites diagnosed passages surgically, self-checks against `style.md`, only role that writes files. Executes plans it did not set.
- **Critics.** Fresh each round — their value is uncontaminated judgment. Each agent file self-describes its inputs; hand a critic its own file + those inputs, nothing else.

Coordinator (session agent) owns user communication, sequencing, final commit. Above paragraph scope it neither drafts nor judges; at paragraph scope or less it collapses all roles (see Rewriting).

## Phases

**0 — Takeaways (planner).** The 3–5 sentences the reader must retain + one per section. Acceptance criteria for every review. Use the user's if stated; else confirm the planner's list before drafting at length.

**1 — Skeleton (planner).** Headings + first sentence of every planned paragraph. Fix ordering, missing steps, buried claims here, where a change costs one line. Don't proceed until the skeleton alone tells the story.

**2 — Expand (editor).** Grow each skeleton sentence into its paragraph, point first, `style.md` voice, never demoting a skeleton sentence from first position. Coordinator checks the seams.

**3 — Skim review.** Mechanically extract the skim view: headings, first sentence per paragraph (with one-sentence-per-line layout: the first line after each blank line or heading), captions, bold. Fresh agent from `agents/skim-critic.md`, given ONLY the extract. Compare readback to takeaways — each miss or distortion marks a failing first sentence, a missing entry-point repetition, or a buried section. Fix at skeleton level, not by adding text.

**4 — Adversarial review.** Section or larger: fresh agent from `agents/adversarial-critic.md`, full text + scope. Smaller: coordinator applies its checklist inline. Fold confirmed objections into the takeaway list; fix by conceding, qualifying, realigning evidence, or a forward-pointer — prefer cutting a vulnerable element over patching (scientific-review's simplification principle).

**5 — Deep review.** Fresh agent from `agents/style-critic.md` + path to `style.md`, over touched sentences.

**6 — Attention budget (planner).** Name each section's one thread in a sentence; whatever does not serve it gets cut, demoted to a clause, or moved. Cut before adding.

**Loop 3–6** until the skim readback returns the takeaways undistorted, no unanswered objection, deep check clean. Two rounds typical; one is suspicious. Then finalize per SKILL.md.

## Rewriting existing text

The common invocation. Same phases in diagnostic order, scaled to the passage.

- **Recover takeaways first** — from the request or comments in the source. Else infer, state in 1–2 sentences, confirm before rewriting at length. Polishing prose around the wrong takeaway is wasted work.
- **Extract the existing skeleton before touching prose.** Diagnose there: buried points, first sentences carrying context instead of claims, sections braiding two threads. Reorder and promote before rewriting any sentence — most weak passages fail here, not at sentence level.
- **Rewrite surgically.** The brief lists diagnosed faults + the sentences that comply and must survive. Every changed line traces to a structural fault or a sentence-rule violation, not taste. Match surrounding density and idiom.
- **Scale roles to scope.** Paragraph or less: coordinator alone — edit inline, apply the adversarial checklist inline to load-bearing claims, run 5–6 itself. Section or more: full role separation. Edits inside a larger document: check the seams — link backward from the first sentence, hand off cleanly.
