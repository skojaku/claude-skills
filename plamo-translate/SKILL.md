---
name: plamo-translate
description: Translate between Japanese and English (and 14 other languages) with the local PLaMo server (http://127.0.0.1:8824), and rewrite English by sending it through Japanese and back. Runs offline on the user's Mac at ~85 tok/s, and is the backup for when DeepL's monthly quota is used up. Use when asked to translate a passage, 「日本語を英語に」, to draft an English version of Japanese notes, or to loosen English prose that is stuck on its own phrasing.
---

# plamo-translate

`pfnet/plamo-2-translate` (9.5B, 4bit MLX) served locally. Two things it does:

- **translate** — Japanese ↔ English and 14 other languages, faithfully, sentence by
  sentence. It is a translator, not a writer: it renders what the input says and adds
  nothing.
- **roundtrip** — English → Japanese → English. The detour is the point. A translator has
  to decide what a sentence *means* before it can say it again, so the English that comes
  back is rebuilt from the meaning rather than edited from the words. Fixed phrases,
  borrowed rhythm, and sentences that were long because they grew that way do not survive
  the trip.

Everything runs on the user's machine. Nothing is sent anywhere.

## When to use it

- Japanese in, English out (or the reverse), when a faithful rendering is wanted.
- DeepL is out of quota and the Alfred `rw` workflow needs its second leg.
- English prose that will not come unstuck from its own wording.

**When not to use it.** This model translates; it does not write. For prose in the user's
own voice use `style-rewrite`; for what to say and how a document is organised use
`scientific-writing`. Do not run this over a document full of LaTeX and nested numbered
lists — see the limits below.

## Calling it

```bash
# Japanese -> English
jq -Rs '{text: .}' < notes.md \
  | curl -sS -X POST http://127.0.0.1:8824/translate -H 'Content-Type: application/json' -d @- \
  | jq -r '.text'

# English -> Japanese
jq -Rs '{text: ., source: "English", target: "Japanese"}' < draft.md \
  | curl -sS -X POST http://127.0.0.1:8824/translate -H 'Content-Type: application/json' -d @- \
  | jq -r '.text'

# English -> Japanese -> English (the rewrite)
jq -Rs '{text: .}' < draft.md \
  | curl -sS -X POST http://127.0.0.1:8824/roundtrip -H 'Content-Type: application/json' -d @- \
  | jq -r '.text'
```

`GET /health` reports whether the model is loaded and lists the languages it accepts —
anything outside that list produces nonsense rather than an error, so the server rejects it.

**Always read `.warnings`.** It is an array, empty when the run was clean. A non-empty entry
means that chunk hit the output ceiling, which is how a runaway shows up. The text still
comes back and still looks plausible; it is not usable.

```bash
... | jq -e '.warnings | length == 0' >/dev/null || echo "check the output"
```

## The limits, which are lower than the model claims

`config.json` advertises a 10,485,760-token context and a 32K sliding window. Both are
nominal. Measured on this build:

| input | what happens |
|---|---|
| ≤ 600 tokens | translated in full |
| ~1,000 tokens | runs away — generates to the ceiling, repeating and hallucinating |
| ≥ 2,600 tokens | translates only the last paragraph, then stops normally |
| ~6,000 tokens | leaves Japanese untranslated inside the English |

None of these raise an error. **Every failure returns plausible-looking text**, which is why
the server splits input into 400-token chunks by paragraph, then by sentence, and why you
should not raise that limit.

Two consequences worth stating to the user rather than discovering later:

- **Terminology is not consistent across chunks.** The model sees one chunk at a time and
  cannot know how it rendered a term three paragraphs ago. Over a long document, grep the
  keywords afterwards.
- **Length is not the only failure mode.** A 385-token chunk of numbered argument mixed with
  LaTeX ran away on a real document. Structured text is off-distribution for a translation
  model; prose is what it is for.

## Speed

~85 tok/s, first token in 0.1 s, so a paragraph is under a second. The 8-second model load
is paid once at server start, which is why this is a server and not a CLI.

## If it is not answering

```bash
curl -s http://127.0.0.1:8824/health
launchctl kickstart -k gui/$(id -u)/com.skojaku.plamo-translate   # restart
tail -20 ~/Library/Logs/plamo-translate.log
```
