---
name: slide-review
description: Review a Marp slide deck for quality issues. Use when the user asks to review, check, or QA a slide deck.
---

# Slide Review

Review a Marp slide deck against the quality rubric. See `SLIDE_RUBRIC.md` for criteria
and `REVIEW_PLAYBOOK.md` for the review-loop process, both bundled alongside this file in
`~/.claude/skills/slide-review/` — this skill defines the review protocol. The default
theme and QA CLI live in the sibling `slide-build` skill (`gatelib/` here is a symlink to
`~/.claude/skills/slide-build/gatelib/`), so a deck needs no external repo to review.

## Tiered review protocol

### Tier 0: Automated checks (zero tokens)

Run first, every round:

```sh
cd ~/.claude/skills/slide-build
python3 -m gatelib review <deck_dir>
```

This runs: auto-fix → render → source checks → render checks → image prep.
Exit code 0 = all automated checks pass. If exit code 1, fix reported issues first.

### Tier 1: Targeted LLM review (changed slides only)

After Tier 0 passes:

```sh
python3 -m gatelib prepare <deck_dir> --changed-only
```

This outputs: number of changed slides, token estimate, and paths to downscaled
review images in `<deck_dir>/review/small/`.

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
`<deck_dir>/review/.render_hashes.json`. On subsequent runs it reports which slides
changed. This is the correct Tier 1 scope — it catches figure edits that propagate to
slides whose markdown did not change.

## Review image preparation

`deckgate prepare` downscales rendered slides from 1280x720 to 640x360.
Each downscaled slide costs ~307 tokens instead of ~1,229 — a 75% saving.
Text at 30px body remains readable at half scale (for the bundled default theme).

For batches of ≤ 12 changed slides, use `--contact-sheet` to tile them into
one image and save tool-call round-trips.

## Common review findings (from past deck-build sessions)

The most frequent issues across many decks' reviews:

1. **Figure container mismatch** — figure drawn for a narrower box than it lands in
2. **KaTeX in HTML blocks** — renders as literal source
3. **Em dashes in captions** — renders as two hyphens
4. **Missing demo link on slide** — URL only in speaker notes
5. **Stagnation regression** — repeated narrative beats lose momentum
6. **Figure reuse with different captions** — same figure, different story

Tier 0 catches all of these except stagnation regression (#5).
