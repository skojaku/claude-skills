---
name: slide-build
description: Build a Marp slide deck for a lecture, technical talk, or workshop. Use when the user asks to create, update, or fix a slide deck (a new deck from scratch, or fixes to an existing one).
---

# Slide Build

Build or fix a Marp slide deck. See `DECK_BUILD_GUIDE.md` and `FIGURE_GUIDE.md`, bundled
alongside this file in `~/.claude/skills/slide-build/`, for the full process — this skill
is the short version. The default theme (`theme.css`) and the QA pipeline (`gatelib/`) are
also bundled here, so a deck needs no external repo to build against.

## Which deck directory

If the user names a path, use it. Otherwise: if the current working directory already
looks like a deck directory (a `.md` file with `marp: true` front matter), use it.
Otherwise ask which directory, or offer to scaffold a new one from
`~/.claude/skills/slide-build/template/` (copy `deck.md`, `check_render.py`, and
`README.md` into a new directory and adjust the filename and constants).

## Automated pipeline

All checks run through `deckgate` (the gatelib CLI), bundled with this skill at
`gatelib/`. Run it from the skill directory, passing the deck's directory (absolute or
relative — it does not need to live under `~/.claude/skills/`):

```sh
cd ~/.claude/skills/slide-build

python3 -m gatelib review <deck_dir>      # full pipeline: fix → render → check → prepare
python3 -m gatelib check <deck_dir>       # all checks (source + render)
python3 -m gatelib fix <deck_dir>         # auto-fix mechanical issues
python3 -m gatelib fix <deck_dir> --dry-run  # preview fixes
python3 -m gatelib prepare <deck_dir> --changed-only  # downscaled review images
python3 -m gatelib render <deck_dir>      # render + check
```

`deckgate review` runs the full Tier 0 pipeline: auto-fix → marp render → source checks →
render checks → prepare downscaled review images. Exit code 0 = all pass.

Each deck needs its own thin `check_render.py` (copied from `template/`) that imports
gatelib and declares that deck's constants — see the template for what to set. `slide-review`'s
`gatelib/` is a symlink to this same directory, so a fix made here reaches both skills.

If `python3 -m gatelib ...` fails with `ModuleNotFoundError: No module named 'numpy'` (or
`PIL`), your active `python3` is a virtualenv without them — call an interpreter that has
`numpy`+`Pillow` installed explicitly (e.g. `/opt/homebrew/bin/python3` on a Homebrew Mac).

## What automation handles (Tier 0)

These are checked and/or fixed automatically. Do NOT spend LLM tokens on them:

| Check | Auto-fix | Tool |
|-------|----------|------|
| Fragment syntax mixing | ✅ | `deckgate fix` |
| KaTeX in HTML blocks | ✅ | `deckgate fix` |
| Demo links in speaker notes | ✅ | `deckgate fix` |
| Trailing whitespace | ✅ | `deckgate fix` |
| Node disc sizes (opt-in, network/graph diagrams) | ❌ | `deckgate check-render` |
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

After each gate pass, `git commit` the current state (if the deck directory is a git
repo). Write `review/CHECKPOINT.md` with:
- Current round number and phase
- Last gate results (pass/fail per criterion)
- Which slides have been LLM-reviewed this round

On session resume, read CHECKPOINT.md to restore state.
