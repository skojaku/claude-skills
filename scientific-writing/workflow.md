# Workflow: the drafting–review loop

The phased loop for drafting and rewriting, run by an orchestrator that delegates to role subagents. The reader model and document-structure rules in SKILL.md are assumed. Prose is written in the voice of style.md, and the review phases are specified in critique.md. Draft and revise in explicit passes; do not draft linearly start-to-finish and then polish. For a multi-section document, run the loop per section, then once over the whole document.

## Role separation

The session agent is the **orchestrator**. It owns the takeaways, the skeleton, all file edits, seam checks, decisions, user communication, and the commit. It does not draft section-scale prose and it does not review its own text, because a drafter is blind to its own draft. Three roles run as fresh subagents, spawned with whatever delegation mechanism the host harness provides (in Claude Code the Agent tool with a general-purpose agent, elsewhere a fresh session or sub-process). Each role starts fresh so no role sees another role's deliberation, and a mid-tier strong model suffices for the roles when the harness allows a model choice:

- **Writer.** Receives SKILL.md, style.md, the approved skeleton, the takeaways, and the surrounding paragraphs for density matching. Expands the skeleton into prose (or rewrites a diagnosed passage surgically), self-checks against the style.md self-check list, and returns the text. The writer returns prose; it does not edit files.
- **Skim reader.** Receives ONLY the skim extract, no skill files, no context, per critique.md. Its value is naivety; giving it anything else destroys the measurement.
- **Critic.** Receives the full passage text and the adversarial checklist plus risk–return audit from critique.md, and nothing about how the text was drafted. Returns objections ranked by severity with the fix or redirect each one needs.

The orchestrator compares reviewer output against the takeaways, decides which findings to act on, sends the writer a revision brief (the diagnosed faults, not rewritten sentences), and applies the returned text to the file. Send follow-up rounds to the same writer conversation where the harness supports continuing a subagent, so the writer keeps its context. Where it does not, include the prior draft and the new brief in a fresh writer prompt. Spawn reviewers fresh every round so their judgment stays uncontaminated.

**No-subagent fallback.** When the host harness cannot spawn subagents at all, keep the role protocol and lose only the process isolation. Run each role as a separate, clearly bounded pass with only that role's inputs in view. For the skim pass, write the skim extract to a file and evaluate the extract alone, never the full text beside it. State in the report that the reviews were self-run, because a drafter reviewing its own text is a weaker guarantee than an independent reader.

## The phases

**Phase 0 — Takeaways (orchestrator).** Before writing, list the 3–5 sentences the busy reader must still hold after putting the document down, plus one sentence per section. Write these sentences down (a scratch file is fine). The takeaway list is the acceptance criteria for every later review pass. If the user has stated the takeaways, use theirs; otherwise propose the list and confirm before drafting at length.

**Phase 1 — Skeleton draft (orchestrator).** Write only the headings and the first sentence of every planned paragraph. Read this skeleton against the takeaway list. Fix ordering, missing steps, and buried claims here, where a change costs one line, not after paragraphs are built on top. Do not proceed until the skeleton alone tells the story.

**Phase 2 — Expand (writer).** Send the writer the skeleton, takeaways, and neighboring text. The writer grows each skeleton sentence into its paragraph, point first, in the voice of style.md, without demoting any skeleton sentence from first position. The orchestrator applies the returned prose and checks the seams.

**Phase 3 — Skim review (skim reader).** Run the skim review of critique.md: the orchestrator extracts the skim view, hands it to a fresh skim reader, compares the readback to the Phase 0 takeaways, and fixes misses at the skeleton level.

**Phase 4 — Adversarial review and risk–return audit (critic).** Run the adversarial review of critique.md through a fresh critic on the full text, then the risk–return audit on every element the attack landed on. Phase 3 tests whether the reader gets the argument; Phase 4 tests whether the argument survives someone trying to break it. The orchestrator folds every confirmed objection back into the Phase 0 takeaways as a claim the revision must now defend. When the audit says an element costs more criticism than it returns evidence, redirect its function instead of defending its prose, and flag redirects that change the design to the user before applying them.

**Phase 5 — Deep review (orchestrator).** The writer already self-checked; the orchestrator spot-checks every touched sentence against the self-check list in style.md, since the writer grading its own homework is a weaker guarantee than a second reader.

**Phase 6 — Attention budget (orchestrator).** Per section, name its one thread in a sentence. Anything in the section that does not serve that thread gets cut, demoted to a clause, or moved. Cut before adding. Drop preliminary numbers that are not load-bearing. Cuts go to the writer as a revision brief when they exceed clause-level surgery.

**Loop.** Repeat Phases 3–6 until the skim readback returns the intended takeaways without distortion, the adversarial pass raises no unanswered objection, and the deep check is clean. Two rounds are typical; one is suspicious. Then the orchestrator commits and pushes per SKILL.md.

## Rewriting existing text

The common invocation is a rewrite, not a blank page. The same phases apply, entered in diagnostic order, and scaled to the size of the passage.

- **Recover the takeaways first (orchestrator, Phase 0).** Take them from the user's request or `#Claude` comments when given. Otherwise infer what the passage is trying to leave with the reader, state that inference in one or two sentences, and confirm it before rewriting at length. A rewrite that polishes prose around the wrong takeaway is wasted work.
- **Extract the existing skeleton before touching prose (orchestrator, Phase 1).** Read the headings and first sentences of the passage as the skimming reader would. Diagnose at this level: buried points, first sentences that carry context instead of claims, sections braiding two threads. Fix structure by reordering and promoting sentences before rewriting any of them. Most weak passages fail here, not at the sentence level.
- **Rewrite surgically (writer, Phase 2).** The revision brief to the writer lists the diagnosed faults and the sentences that already comply and must survive. Every changed line should trace to a diagnosed structural fault or a sentence-rule violation, not to taste. Match the density and idiom of the surrounding text that is not being rewritten.
- **Scale the roles to the scope.** For a paragraph or a few sentences, the orchestrator works alone: it edits inline, applies the adversarial checks of critique.md to any claim the passage rests on, and runs Phases 5–6 itself, spawning no subagents. For a section or more, use the full role separation: writer for the rewrite, fresh skim reader on the post-rewrite skeleton, fresh critic on the full text. For edits inside a larger document, check the seams: the rewritten passage must still link backward from its first sentence and hand off cleanly to what follows.
