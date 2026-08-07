# gatelib — slide deck QA pipeline

Single CLI entry point (`deckgate`) for all automated slide checks, fixes, and
review image preparation. Replaces per-module copy-and-edit scripts.

## Quick start

```sh
cd docs/slide/new

# Full pipeline: auto-fix → render → check → prepare review images
python3 -m gatelib review m01

# Individual commands
python3 -m gatelib check m01              # all checks
python3 -m gatelib check-deck m01         # source-level only
python3 -m gatelib check-render m01       # pixel-level only
python3 -m gatelib fix m01                # auto-fix mechanical issues
python3 -m gatelib fix m01 --dry-run      # preview fixes
python3 -m gatelib prepare m01 --changed-only  # downscaled review images
python3 -m gatelib render m01             # render + check
```

## What it automates

| Check | Auto-fix | Command |
|-------|----------|---------|
| Fragment syntax mixing | ✅ | `fix` |
| KaTeX in HTML blocks | ✅ | `fix` |
| Demo links in speaker notes | ✅ | `fix` |
| Trailing whitespace | ✅ | `fix` |
| Node disc sizes | ❌ | `check-render` |
| Text size (x-height) | ❌ | `check-render` |
| Content overflow | ❌ | `check-render` |
| Container mismatch | ❌ | `check-render` |
| Figure reuse w/ diff captions | ❌ | `check-deck` |
| Answer leak (text) | ❌ | `check-deck` |
| Bold overuse | ❌ | `check-deck` |
| Stale render | ❌ | `check-deck` |
| Em dashes | ❌ | `check-render` |
| Caption colours | ❌ | `check-render` |

## Architecture

```
gatelib/
  __main__.py       # python3 -m gatelib entry
  cli.py            # CLI argument parsing + subcommands
  check_deck.py     # source-level checks (markdown)
  check_render.py   # pixel-level checks (rendered PNGs)
  fix_deck.py       # auto-fixers for mechanical issues
  review_images.py  # downscale/contact-sheet for LLM review
```

Each module (`m01`–`m06`) keeps a thin `check_render.py` wrapper that carries
only its constants (deck filename, NODE_FILLS palette, FIG_H modifiers, exempt
figures). All logic lives in gatelib.

## Render hash change detection

`check-deck` saves SHA-256 hashes of rendered slide PNGs to
`review/.render_hashes.json`. Changed slides are the Tier 1 LLM review scope.
A figure edit propagates to every slide that uses it — the hash catches this.

## Token-efficient review images

`prepare` downscales 1280x720 slides to 640x360 (~307 tokens each vs ~1,229).
With `--changed-only`, only changed slides are prepared. Typical savings:
75% per slide, 95% when combined with changed-only filtering.

## Recovered checks

Checks that were lost in the per-module copy pattern:

| Check | Written for | Lost in | Recovered |
|-------|------------|---------|-----------|
| `caption_colours` | m02 | m03+ | gatelib |
| `em_dashes` | m03 | m04+ | gatelib |
| `_flood_from_border` | m02 | m03 | gatelib |

## Adding a new check

Add it to `check_render.py` or `check_deck.py` in gatelib. Every module
inherits it on the next run. No per-module copies to update.
