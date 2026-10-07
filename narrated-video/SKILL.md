---
name: narrated-video
description: "Make or change the narrated video of a Remotion deck, for any module or new topic: a small figure lying down types short English notes as terminal lines with mechanical-keyboard sound, the slides' own sentences moved into the chat, a few reactions (worry, shrug). Covers starting from a topic with no deck, porting the video code to another deck, writing the narration, the figure and its Gemini-drawn frames, the typing sound, rendering and checking. Use when the lecturer asks for narration, a video of a deck or a topic, the typing sound or the character."
---

# Narrated video

The substance is in plain markdown in the course repo, so that any agent can follow it; this skill only dispatches.
Repo: `/Users/skojaku/Documents/teaching/adv-net-sci`. Read `slides/NARRATED_VIDEO_GUIDE.md` there and do what it says. Deck authoring and the Remotion pitfalls: `slides/REMOTION_DECK_GUIDE.md`.
This skill may be invoked from any directory: `cd` into the deck's project before running its commands (`slides/m05/remotion` is the source of the shared code).

## Where to start

Look first for a Remotion deck of the topic: `slides/*/remotion*/src/slides/index.ts`. Existing videos: Module 05 (`slides/m05/remotion`, id `M05`), modularity / Louvain / Leiden (`slides/m05/remotion-modularity`, id `M05MOD`).

- **No deck yet (a new topic)**: the deck is most of the work. The guide's section "Starting a new topic": the story as a table of slides and stages (`DECK_SPEC.md`), shown to the lecturer, with the narrative questions asked before anything is drawn; then **one command** from `slides/m05/remotion`: `node scripts/new_deck.mjs ../remotion-<topic> --name=<topic> --ids=a,b,c --video-id=<ID>` (shared parts, stub slides, index, the video code); numbers in `scripts/make_data.py` and an independent `scripts/verify_numbers.py`; slides (parallel agents by slide range); then the video.
- **A deck exists, no video**: "Making the video of another deck": `node scripts/port_video.mjs <project> --id=M06 --skip=<slides to leave out>` copies the video code, writes the four stubs and lists what the deck lacks; then `npm run video:prose`, `npm run video:skeleton -- --out=src/video/narration.ts`, the introduction (`narration[0][0]` plus `intro` in `video.config.json`), the lines, `moods.ts`.
- **Change a video** (a line, the layout, the introduction, a reaction, the pauses, the sound): the matching section of the guide; the knobs are listed in "Making the video of another deck".

## Always

- Decide on stills (`node scripts/render_video.mjs --still=...`) and a clip (`--frames=a-b --out=out/clip.mp4`), not on a full render; render in the background (about 11 minutes) once the lecturer says so; check the mp4 itself (ffprobe, frames, the sound of a stretch); say what an agent cannot judge (it cannot hear the sound).
- Run `npm run video:prose` and `npm run video:audio` again after any change to a slide's sentences, marks, the narration or the pauses.
- Count the lines before writing: a line costs about 7.5 seconds. The lecturer wants one straight line per step, no scattered slide, no closing recap, examples whose values differ clearly.
- The slides of an existing deck are never edited for the video. Commit only the deck's project directory; `git status` may list unrelated changes.

Commands (in the deck's project): `npm run video:prose | video:skeleton | video:lengths | video:audio | video | video:sampler`; deck: `npm run review`, `node scripts/review.mjs --only=1-8`, `python3 scripts/check_bottom.py`. Code: `src/video/` and `scripts/` (`new_deck.mjs`, `port_video.mjs`, `make_typing_audio.mjs`, `render_video.mjs`, `collect_prose.mjs`, `narration_skeleton.mjs`, `line_lengths.mjs`, `extract_mechvibes.mjs`, `gen_character.py`, `prep_character.py`).
