# Critique: skim review, adversarial review, risk–return audit

The review passes of workflow.md Phases 3–4, also invoked standalone on a review request. SKILL.md's reader model and structure rules are assumed. A review-only invocation reports findings and stops; do not apply fixes until asked.

## Skim review — does the busy reader get the argument?

- Mechanically extract the skim view: headings, first sentence of each paragraph (with one-sentence-per-line layout, the first line after each blank line or heading), figure captions, bold text.
- Give ONLY this extract to a fresh skim critic (per workflow.md's role separation) with a prompt like: "You are a busy reviewer who skimmed this document. State in your own words: what is being proposed, why it matters, what the evidence is, and what you remain unconvinced by. Do not guess charitably."
- Compare the readback to the takeaway list. Every missed or distorted takeaway marks a first sentence not doing its job, a missing entry-point repetition, or a buried section. Fix at the skeleton level, not by adding text.

## Adversarial review — does the argument survive attack?

Read the full passage as a hostile expert looking for a reason to decline. Interrogate every load-bearing claim:

- **Operationalization gap.** Concept defined one way, measured another ("traversability, a property of shared conceptual frameworks" later measured as "many researchers transition between the areas"). Name the confounds the measurement admits but the definition excludes (job markets, funding, geography); check the text concedes them and points to what rebuts them.
- **Claim–evidence alignment.** Every citation or number must support the specific claim, not merely share its topic. Trace each to the assertion it sits under; flag those that only relate.
- **Fabricated precision.** A suspiciously specific number with no traceable source. Check for a citation, a result reported elsewhere in the document, or an explicit "target:"/"stretch goal:" label. When none backs it, treat it as invented: cut to a qualitative claim, restore the real figure, or relabel explicitly as target or assumption.
- **Dropped qualifier across an inference.** Check every "therefore"/"thus"/"hence": does the conclusion carry a qualifier the premise never licensed? "Distant combinations have impact, therefore reachable unlinked pairs hide impact" swaps "distant" for "reachable". Restore the qualifier or cut the inference.
- **Causal overclaim from correlational support.** "X accelerates Y" where the evidence is an association. Downgrade to the association shown, or supply the mechanism licensing the causal verb.
- **Prescriptive use of a descriptive instrument.** A document declaring an instrument descriptive (map of realized transitions) yet pitching it prescriptively ("shows where you can go") must not patch the gap with statistical-adjustment language, which concedes a causal frame without earning it. Rephrase the pitch descriptively ("fields researchers have actually reached") so quoting pitch against declaration yields no contradiction, and rest the defense on evaluation that needs no causal reading (record-not-prescription framing, human final selection, outcome-based scoring). Avoid causal-identification vocabulary unless the document does identification.
- **Rhetorical inflation.** Superlatives and absolutes ("first", "only", "every", "regardless of", "any") are claims, not flourishes. Cut or qualify the ones that overreach. Check "only"/"first" against the rest of the document — a stronger instrument elsewhere silently falsifies them.
- **Product / SE register drift.** Flag prose reading like release notes, app architecture, or marketing rather than methods and measurements (bans and replacements in style.md's "NSF/scientific register"): ships/shipped, tool suite, backend, production pipeline, degrade gracefully, base/stretch layer, travelers-on-the-map, humans-in-control slogans, technology-transfer path, enables-openers, tagline stacks of the same instead-of contrast across summary/merit/impacts/body. Rewrite to the concrete mechanism, release channel, or contingency. Keep genuine technical nouns.
- **Invitation to refute.** A claim phrased as a verdict against an alternative ("X is not sufficient", "existing approaches cannot Z", headings most of all) reads as a dare and pulls the reviewer into hunting the one counterexample. Recast as the actual diff being drawn: "Why Existing Approaches Are Not Sufficient" -> "Relatedness Is Not Traversability".
- **Misplaced rebuttal.** The answer to the obvious objection often exists in a later section. Add a one-clause forward-pointer so the skeptic does not put the document down first.
- **Named claim without a metric.** When the text announces what is being tested ("navigation finds literature keyword search misses"), some evaluation paragraph must name the measurement scoring exactly that claim. Two fixes, a decision not a default: upgrade the metric to the claim, or demote the claim to the metric. For claims the document does not stand on, prefer demotion — promising a failable analysis for a non-core component is asymmetric risk.

For a section or larger, run with a fresh adversarial critic: full section text (not the skeleton) plus "You are a hostile reviewer whose job is to find the reason to decline this proposal. For each central claim, state the strongest objection and whether the text answers it. Do not be charitable." Fold confirmed objections into the takeaway list; fix by conceding, qualifying, realigning evidence, or adding the forward-pointer.

## Risk–return audit — is this element worth the attack it invites?

Some elements draw a stronger objection than the support they contribute; fixing their prose is the wrong move. Run on every load-bearing design element after the adversarial pass.

- **Estimate both sides.** What does the argument lose if this element is cut? How long is the hostile reviewer's paragraph about it? When the objection outweighs the contribution, the element costs more than it returns.
- **Recurring shapes.** An underpowered sample carrying a "test"/"validation" claim. An ethically sensitive population (students, patients, employees) validating a method when public or archival data could serve. A measurement confounded by design (syllabus-constrained behavior offered as evidence of free choice). A data-collection plan whose compliance surface dwarfs its evidential yield. An experiment on captive participants that could run offline against expert ratings.
- **Redirect, do not defend.** Move the evidential function to the strongest instrument the document already contains (public dataset, powered later-year test, existing expert-rubric evaluation); return the risky element to a low-claim role it genuinely fills (deployment, field feedback, teaching, dissemination). Example: learner trajectories (~90 students, syllabus-constrained, collected by their grading instructor) carried "the only direct test of whether the gravity law generalizes beyond careers". A Year-5 demonstration on public occupational-mobility data tests the same generalization with real power and no human subjects. Redirect: generalization test moved to the public-data demonstration; students became users of the research; classroom signal became field testing and feedback.

## Reporting

Findings ranked by severity, each with the claim, the objection as a hostile reviewer would voice it, and the concrete fix or redirect. Separate one-line wording fixes from design decisions needing the user; state which findings you did not act on and why. Report in Japanese per SKILL.md; the document's prose stays in its own language.
