---
name: slide-build
description: Build a slide deck for one module of the network science course. Use when the user asks to create, update, or fix a lecture deck (m07+, or fixes to existing decks).
---

# Slide Build

Build or fix a Marp slide deck for the adv-net-sci course. See
`/Users/skojaku/Documents/teaching/adv-net-sci/docs/slide/new/DECK_BUILD_GUIDE.md`
for the full process. This skill is the short version.

Course repo root: `/Users/skojaku/Documents/teaching/adv-net-sci`

## Automated pipeline

All checks run through `deckgate` (the gatelib CLI), bundled directly with this
skill at `gatelib/` (real files — this is the canonical source; the project's
`docs/slide/new/gatelib` is a symlink back to this directory). Run from
`docs/slide/new/` in the course repo:

```sh
cd /Users/skojaku/Documents/teaching/adv-net-sci/docs/slide/new

python3 -m gatelib review <module_dir>      # full pipeline: fix → render → check → prepare
python3 -m gatelib check <module_dir>       # all checks (source + render)
python3 -m gatelib fix <module_dir>         # auto-fix mechanical issues
python3 -m gatelib fix <module_dir> --dry-run  # preview fixes
python3 -m gatelib prepare <module_dir> --changed-only  # downscaled review images
python3 -m gatelib render <module_dir>      # render + check
```

`deckgate review` runs the full Tier 0 pipeline: auto-fix → marp render → source checks → render checks → prepare downscaled review images. Exit code 0 = all pass.

Editing gatelib: edit the files here (`~/.claude/skills/slide-build/gatelib/`),
not through the project symlink. `slide-review`'s `gatelib/` is a relative
symlink to this same directory, so both skills stay in sync automatically.

## What automation handles (Tier 0)

These are checked and/or fixed automatically. Do NOT spend LLM tokens on them:

| Check | Auto-fix | Tool |
|-------|----------|------|
| Fragment syntax mixing | ✅ | `deckgate fix` |
| KaTeX in HTML blocks | ✅ | `deckgate fix` |
| Demo links in speaker notes | ✅ | `deckgate fix` |
| Trailing whitespace | ✅ | `deckgate fix` |
| Node disc sizes | ❌ | `deckgate check-render` |
| Text size (x-height) | ❌ | `deckgate check-render` |
| Content overflow | ❌ | `deckgate check-render` |
| Container mismatch | ❌ | `deckgate check-render` |
| Figure reuse w/ diff captions | ❌ | `deckgate check-deck` |
| Answer leak (text) | ❌ | `deckgate check-deck` |
| Bold overuse | ❌ | `deckgate check-deck` |
| Stale render | ❌ | `deckgate check-deck` |
| Em dashes | ❌ | `deckgate check-render` |
| Caption colours | ❌ | `deckgate check-render` |

## What needs LLM judgment (Tier 1)

Only review these on changed slides (use render hash from `deckgate check-deck`):

- P1 (one point per slide)
- F1 (unexplained encodings)
- F4 (figure carries the point)
- N1–N4 (narrative, conversational tone, question-before-answer)
- S1–S5 (four-act structure, milestone demos)

## Review agent model

- Anthropic models → use `sonnet` for review subagent
- Non-Anthropic models → use `grok-4.5` for review subagent

## Agent architecture

Three agents maximum:

1. **Lead** (strong model) — reads guides once, reviews, writes FIXES_Rn.md
2. **deck-fixer** (cheap model) — applies markdown fixes from FIXES_Rn.md
3. **figure-fixer** (cheap model) — applies figure script fixes from FIXES_Rn.md

Briefs include relevant guide sections inline (injected by lead). Workers never read guides.

## Checkpointing

After each gate pass, `git commit` the current state. Write `CHECKPOINT.md` with:
- Current round number and phase
- Last gate results (pass/fail per criterion)
- Which slides have been LLM-reviewed this round

On session resume, read CHECKPOINT.md to restore state.
