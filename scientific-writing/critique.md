# Critique: skim review, adversarial review, risk–return audit

The review passes of the drafting–review loop (workflow.md Phases 3–4), also invoked standalone when the user asks for a review of existing text. The reader model and document-structure rules in SKILL.md are assumed. A review-only invocation reports findings and stops; do not apply fixes until asked.

## Skim review (does the busy reader get the argument?)

Reconstruct what the satisficing reader sees, and check it against the takeaways.

- Mechanically extract the skim view: headings, the first sentence of each paragraph (with one-sentence-per-line source layout this is the first line after each blank line or heading), figure captions, and bold text.
- Give ONLY this extract to a fresh subagent (Agent tool, general-purpose, no other context) with a prompt like: "You are a busy reviewer who skimmed this document. State in your own words: what is being proposed, why it matters, what the evidence is, and what you remain unconvinced by. Do not guess charitably." The drafter cannot simulate naivety about its own draft; a context-free agent can.
- Compare the subagent's readback to the takeaway list. Every takeaway the readback misses or distorts marks a paragraph whose first sentence is not doing its job, a missing entry-point repetition, or a buried section. Fix at the skeleton level, not by adding text.

## Adversarial review (does the argument survive attack?)

Attack the argument the way a reviewer looking for a reason to decline would, and check that the text answers each attack. Skim review reads the skeleton as a naive reader; this reads the full passage as a hostile expert. Interrogate every load-bearing claim along these lines:

- **Operationalization gap.** A quantity defined one way and measured another. When the text defines a concept ("traversability, a property of shared conceptual frameworks") and later operationalizes it differently ("many researchers transition between the areas"), name the confounds the measurement admits but the definition excludes (job markets, funding, geography), and check the text concedes them and points to what rebuts them.
- **Claim–evidence alignment.** Every cited number or result must support the specific claim, not merely share its topic. A statistic about redundant trials does not evidence a gap in tooling. Trace each citation to the exact assertion it sits under, and flag the ones that only relate to it.
- **Dropped qualifier across an inference.** Check every "therefore", "thus", "so", "hence": does the conclusion carry a qualifier the premise never licensed? "Distant combinations have impact, therefore reachable unlinked pairs hide impact" silently swaps "distant" for "reachable". Restore the missing qualifier or cut the inference.
- **Causal overclaim from correlational support.** "X accelerates Y" asserted as fact where the evidence is an association ("X-users show more Y"). Downgrade to the association actually shown, or supply the mechanism that licenses the causal verb.
- **Rhetorical inflation.** Superlatives and absolutes ("first", "oldest", "only", "every", "regardless of", "any") are claims, not flourishes. Check each against what is shown, and cut or qualify the ones that overreach. Check "only" and "first" against the rest of the document too, because a stronger instrument elsewhere (a later demonstration, a bigger dataset) silently falsifies them.
- **Misplaced rebuttal.** The answer to the obvious objection often already exists in a later section. When a claim invites an attack where it is made, add a one-clause forward-pointer to where the objection is met, so the skeptic does not put the document down first.
- **Named claim without a metric.** When the text announces what is being tested ("the claim under test is that navigation finds literature keyword search misses"), check that some evaluation paragraph names the measurement that scores exactly that claim. A falsifiable claim followed by metrics that measure something else (completion rates, satisfaction) reads worse than no claim, because it shows the writer knew what the test was and did not run it.

For a section or larger, run this with a fresh subagent: give it the full section text (not the skeleton) and the prompt "You are a hostile reviewer whose job is to find the reason to decline this proposal. For each central claim, state the strongest objection and whether the text answers it. Do not be charitable." Fold every confirmed objection back into the takeaway list as a claim the revision must now defend, then fix by conceding, qualifying, realigning evidence, or adding the forward-pointer.

## Risk–return audit (is this element worth the attack it invites?)

Some elements draw a stronger objection than the support they contribute. Fixing their prose is the wrong move; the element itself is the fault. Run this audit on every load-bearing design element and claim, after the adversarial pass has surfaced the objections.

- **Estimate both sides.** For each element ask two questions. What does the argument lose if this element is cut? How long is the hostile reviewer's paragraph about it? When the objection paragraph outweighs the contribution, the element costs more than it returns.
- **The recurring shapes.** An underpowered sample carrying a "test" or "validation" claim. An ethically sensitive population (students, patients, employees) used to validate a method when public or archival data could serve. A measurement confounded by design (behavior constrained by a syllabus offered as evidence of free choice). A data-collection plan whose compliance surface (IRB, consent, power dynamics between the collector and the collected) dwarfs the evidential yield. An experiment run on captive participants that could run offline against expert ratings.
- **Redirect, do not defend.** The fix is rarely better justification. Move the evidential function to the strongest instrument the document already contains (a public dataset, a powered test in a later year, an existing expert-rubric evaluation), and return the risky element to a low-claim role it genuinely fills (deployment, field feedback, teaching, dissemination). The claim gets stronger and the attack surface disappears at the same time.
- **Worked example.** Learner trajectories (~90 students, syllabus-constrained moves, collected by the instructor who grades them) carried the claim "the only direct test of whether the gravity law generalizes beyond scientific careers". The audit: cutting it loses little, since a Year-5 demonstration on public occupational-mobility data tests the same generalization with real power and no human subjects. The objection paragraph writes itself, with consent under a grading power dynamic, an unvalidated tool steering real students, and a confounded corpus. The redirect: the generalization test moved to the public-data demonstration, the students returned to being users of the research, and the classroom's return signal became field testing and feedback.

## Reporting

Present findings ranked by severity, each with the claim, the objection as a hostile reviewer would voice it, and the concrete fix or redirect. Separate what is a one-line wording fix from what needs a design decision by the user, and say which findings you did not act on and why.
