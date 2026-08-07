---
name: slide-review
description: Review a slide deck for quality issues. Use when the user asks to review, check, or QA a lecture deck.
---

# Slide Review

Review a Marp slide deck against the quality rubric for the adv-net-sci course.
See `/Users/skojaku/Documents/teaching/adv-net-sci/docs/slide/new/SLIDE_RUBRIC.md`
for criteria. This skill defines the review protocol.

Course repo root: `/Users/skojaku/Documents/teaching/adv-net-sci`

## Tiered review protocol

### Tier 0: Automated checks (zero tokens)

Run first, every round. The CLI is bundled with the `slide-build` skill at
`gatelib/` (this skill's `gatelib/` is a symlink to
`~/.claude/skills/slide-build/gatelib/`, so both stay in sync):

```sh
cd /Users/skojaku/Documents/teaching/adv-net-sci/docs/slide/new
python3 -m gatelib review <module_dir>
```

This runs: auto-fix → render → source checks → render checks → image prep.
Exit code 0 = all automated checks pass. If exit code 1, fix reported issues first.

### Tier 1: Targeted LLM review (changed slides only)

After Tier 0 passes:

```sh
python3 -m gatelib prepare <module_dir> --changed-only
```

This outputs: number of changed slides, token estimate, and paths to downscaled
review images in `review/small/`.

Review ONLY the changed slides, ONLY these judgment criteria:

- P1 (one point per slide)
- F1 (unexplained encodings)
- F4 (figure carries the point)
- N1–N4 (narrative, conversational tone, question-before-answer)
- S1–S5 (four-act structure, milestone demos)

Skip criteria that Tier 0 handles: layout sizes, colors, overflow, tables, code
blocks, fragment syntax, KaTeX issues, demo links, figure reuse, bold usage.

**Review agent model**: Anthropic → `sonnet`, non-Anthropic → `grok-4.5`.

### Tier 2: Full-deck review (once, before shipping)

After Tier 1 passes, review the ENTIRE deck once:

- All criteria (including those Tier 0 checks, as a sanity check)
- All slides, including unchanged ones
- Focus on deck-level narrative flow and coherence

## Render hash change detection

`deckgate check-deck` saves SHA-256 hashes of every rendered slide PNG to
`review/.render_hashes.json`. On subsequent runs it reports which slides changed.
This is the correct Tier 1 scope — it catches figure edits that propagate to
slides whose markdown did not change.

## Review image preparation

`deckgate prepare` downscales rendered slides from 1280x720 to 640x360.
Each downscaled slide costs ~307 tokens instead of ~1,229 — a 75% saving.
Text at 30px body remains readable at half scale.

For batches of ≤ 12 changed slides, use `--contact-sheet` to tile them into
one image and save tool-call round-trips.

## Common review findings (from past sessions)

The most frequent issues across 6 modules of reviews:

1. **Figure container mismatch** — figure drawn for a narrower box than it lands in
2. **KaTeX in HTML blocks** — renders as literal source
3. **Em dashes in captions** — renders as two hyphens
4. **Missing demo link on slide** — URL only in speaker notes
5. **Stagnation regression** — repeated narrative beats lose momentum
6. **Figure figure reuse with different captions** — same figure, different story

Tier 0 catches all of these except stagnation regression (#5).
