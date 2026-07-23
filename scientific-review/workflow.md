# Workflow: two layers, coarse to fine

The coordinator (session agent) runs this file top to bottom. It spawns subagents, triages issues, talks to the user, and never judges the manuscript itself. Kept separate from SKILL.md so the orchestration can be redesigned without touching the agent roles.

## Prerequisites

- The manuscript's repository has a GitHub remote (`gh repo view` succeeds). Without one, stop and tell the user — this workflow stores findings as GitHub issues and has no fallback.
- Ensure labels exist (`gh label create` for any missing): `review`, `stage:skeleton`, `stage:section`, `stage:paragraph`, `needs-decision`, `locked`.

## The two layers

**Layer 1 — find.** Naive critics attack the manuscript and file every problem as a GitHub issue: logic holes, weak support, claim–evidence mismatches, takeaways the skim does not deliver. Each critic gets its `agents/*.md` file, the input that file names, and the repo + labels for filing. It returns issue numbers with one-line summaries, nothing more.

**Layer 2 — resolve.** One simplifier (`agents/simplifier.md`) per stage reads the stage's open issues and chooses, per issue: patch, cut, or reject — cut preferred whenever the patch would complicate the argument. It merges duplicates, closes issues its cuts dissolve, appends a recommendation to each survivor, and labels the ones needing the user `needs-decision`.

## Stages

Run both layers at each granularity, coarsest first. Do not descend while the current stage has open `needs-decision` issues.

**Stage 1 — skeleton.** Does the document-level argument stand on its own?

1. Extract the skim view mechanically: headings, first sentence of each paragraph, figure captions, bold text.
2. In parallel: skim critic (the extract only) and adversarial critic (full manuscript; scope: the document-level argument — main claims, their support chain, ordering, missing steps).
3. Compare the skim readback against the intended takeaways (the user's, or confirm them now); file an issue for every missed or distorted takeaway.
4. Simplifier, then the decision point.

**Stage 2 — sections.** Does each section's internal logic hold? One adversarial critic per section in parallel (scope: that section's argument; input: the section plus the abstract for anchoring). Then simplifier, decision point.

**Stage 3 — paragraphs.** Does each paragraph make one point, point first, and do the inferences between sentences hold? Adversarial critics per section (scope: paragraph granularity). Then simplifier, decision point.

**Final pass — sentences.** No layers, no issues. Style critic (`agents/style-critic.md`, Haiku) over touched sentences, handed the path to `../scientific-writing/style.md`; hand violations to a scientific-writing edit.

## Decision point — end of every stage

1. Triage from `gh issue list --label "stage:<X>" --state open`; open bodies only where the title is not enough.
2. Report to the user in Japanese: findings by severity, the simplifier's recommendation on each, `needs-decision` issues as explicit questions.
3. Record each user ruling as a comment on its issue; label ruled issues `locked`, close the resolved ones.
4. Apply the agreed fixes under the scientific-writing skill before the next stage, so finer critics review corrected text. If the user asked for review only, stop here and ask before editing anything.
5. A later critic re-raising a locked ruling: close as duplicate with a pointer to the locked issue. Do not re-litigate.

## Issue conventions

- Title: `[skeleton|section|paragraph] <one-line finding>`. Body: where (section/paragraph), the claim, the objection as a hostile reviewer would voice it, and what evidence bears on it.
- Labels on creation: `review` plus the stage label.
- The simplifier appends `## Recommendation` — patch / cut / reject, with the concrete move.
- Critics and the simplifier return numbers and one-liners only; full text stays on the issues.
