# Workflow: two layers, coarse to fine

Coordinator (session agent) runs this top to bottom: spawns agents, triages issues, talks to the user. Critique itself stays with the agents. Separate file so orchestration can change without touching agent roles.

## Prerequisites

- `gh repo view` succeeds; else stop and tell the user — findings are GitHub issues, no fallback.
- Labels exist (`gh label create` if missing): `review`, `stage:skeleton`, `stage:section`, `stage:paragraph`, `needs-decision`, `locked`.

## Layers

**L1 — find.** Naive critics file every problem as an issue: logic holes, weak support, claim–evidence mismatch, undelivered takeaways. Each gets its agent file + the input it names + repo/labels.

**L2 — resolve.** One simplifier per stage reads the stage's open issues; per issue: patch / cut / reject, cut preferred when a patch complicates the argument. Merges duplicates, closes issues its cuts dissolve, appends recommendations, labels `needs-decision` where the user must rule.

## Stages

Coarsest first. Don't descend while `needs-decision` issues are open.

1. **Skeleton** — does the document-level argument stand? Extract the skim view (headings, first sentence per paragraph, captions, bold). In parallel: skim critic (extract only) + adversarial critic (full manuscript; scope: main claims, support chain, ordering, missing steps). Diff the readback against intended takeaways (user's, or confirm now); file an issue per missed or distorted takeaway. Simplifier → decision point.
2. **Sections** — does each section's logic hold? One adversarial critic per section in parallel (input: section + abstract; scope: its internal argument). Simplifier → decision point.
3. **Paragraphs** — one point per paragraph, point first, inferences hold? Adversarial critics per section at paragraph scope. Simplifier → decision point.
4. **Sentences** — no layers, no issues. Style critic (Haiku) on touched sentences + path to `../scientific-writing/style.md`; fix violations via scientific-writing.

## Decision point (each stage)

1. Triage `gh issue list --label "stage:<X>" --state open`; open bodies only where titles are not enough.
2. Report per SKILL.md; ask the `needs-decision` questions.
3. Record rulings as issue comments; label `locked`, close resolved.
4. Apply agreed fixes (scientific-writing) before the next stage. Review-only request: stop here, ask before editing.
5. Later critic re-raises a locked ruling → close as duplicate pointing at it. No re-litigating.

## Issue conventions

- Title `[skeleton|section|paragraph] <one-line finding>`. Body: where, claim, objection as a hostile reviewer would voice it, bearing evidence. Labels: `review` + stage.
- Simplifier appends `## Recommendation` — patch/cut/reject + the concrete move.
- Agents return numbers + one-liners; full text stays on the issues.
