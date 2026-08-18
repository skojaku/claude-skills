---
name: style-rewrite
description: Rewrite a passage into the user's own writing style by calling the local style-server API (http://127.0.0.1:8823). English or Japanese goes in, English prose in the user's voice comes out, checked by a reviewer you can give instructions to, with every LaTeX expression preserved byte for byte. Use when asked to put text "in my style" / 「自分のスタイルで」, to turn Japanese notes or bullets into English prose, or to restyle an existing draft. It changes voice only — structure and argument belong to the scientific-writing skill.
---

# style-rewrite

A local server that runs the user's fine-tuned style model, in three stages:

1. **Outline** — the input is broken into a Japanese outline (`deepseek-v4-flash:cloud`), with
   display equations pulled out;
2. **Style** — the outline goes to the user's fine-tuned model (`my-style-model`, thinking
   off), which writes English prose;
3. **Review** — `deepseek-v4-flash:cloud` reads the source and the styled draft together and
   repairs the draft. This is the stage you can give instructions to.

Roughly 20-35 s for a paragraph with review on, 5 s with it off. Everything runs on the
user's machine except stages 1 and 3.

## When to use it

- The user asks for text in their style, their voice, or their wording.
- The user hands you Japanese notes and wants English prose.
- You have written a draft paragraph for the user and it needs to sound like them.

Do not use it to decide *what* to say or how a document is organised — that is the
`scientific-writing` skill. Run that first, this last.

## Calling it

```bash
# any text file in, styled prose out
python3 -c 'import json,sys; print(json.dumps({"text": sys.stdin.read()}))' < draft.md \
  | curl -sS -X POST http://127.0.0.1:8823/rewrite -H 'Content-Type: application/json' -d @- \
  | python3 -c 'import json,sys; r=json.load(sys.stdin); print(r["styled"]);
print("WARNINGS:", r["warnings"], file=sys.stderr) if r["warnings"] else None'
```

Response fields: `styled` (the final prose), `draft` (stage 2, before the reviewer touched
it — diff the two to see what was repaired), `review` (`{verdict, issues, model}`),
`attempts`, `outline` (the intermediate Japanese bullets), `warnings`, `timing`.

`review.verdict` is `pass` (draft needed nothing), `repaired` (the reviewer fixed it and
`issues` says what was wrong), `reject` (too broken to repair — stage 2 was re-run), or
`unparsed` (the reviewer's JSON was unreadable; the draft shipped unchecked).

Endpoints: `POST /rewrite`, `POST /outline` (stage 1 only), `POST /review` (stage 3 only, to
re-check an existing draft under new instructions without regenerating it),
`POST /rewrite/stream` (SSE — the deltas are the *draft*; the reviewed text arrives in
`done`), `GET /health`.

## Steering it with `instructions`

`instructions` is a free-text field that goes to the **reviewer**, not to the style model:

```json
{"text": "...",
 "instructions": "This is one bullet in a topic list. Return one line, at most one sentence. Do not define the concept or list applications. Address the reader as 'you'."}
```

The style model is a LoRA trained on one exact prompt. Adding instructions to it costs the
voice you are calling it for, so the pipeline never does. Everything you want enforced —
person, length, register, vocabulary you must keep, house terminology — goes in
`instructions`, and the reviewer applies it to the draft afterwards.

The reviewer checks six things by default, in order: faithfulness (no invented claims,
numbers, or citations), agency (who does what — it catches "we"/"I" displacing "you"),
terminology (no paraphrasing a term of art), scale (a one-line item stays one line), sense
(no truncated sentences or word salad), and notation. Your instructions win where they
conflict.

Two repairs are rejected in code, not by the model: one that drops notation the draft had
right, and one that hands the source back instead of editing the draft. Both fall back to the
draft, and the second re-runs stage 2.

Other body fields: `review` (default `true` — set `false` to skip stage 3), `max_attempts`
(default 2), `style_temperature` (default 0.7 — lower it for a literal rewrite),
`outline_temperature` and `review_temperature` (default 0.2), `style_model`, `outline_model`,
`review_model`.

## The contract fields, which are what actually hold

`instructions` steers a language model, so it holds most of the time. These four fields are
checked in **code** after stage 3, and a failure buys another repair pass:

```json
{"text": "...",
 "mode": "imperative",
 "max_sentences": 2,
 "protect_regex": ["`[^`\\n]+`", "https?://\\S+"],
 "glossary": [{"term": "Königsberg"}, {"term": "node", "instead_of": ["vertex"]}]}
```

- **`mode`** — `prose` (default) | `bullet` | `imperative` | `question` | `caption` |
  `fragment`. Sets a default sentence ceiling (prose ∞, bullet/imperative 2, caption 3,
  question/fragment 1), tells the reviewer what shape it is looking at, and turns on the
  matching check. **Use it on every list item and every question** — untagged, they come back
  as "We will…" or with the answer appended.
- **`max_sentences`** — a hard ceiling, overriding the mode's default. Overflow that survives
  the repair pass is cut at a sentence boundary, with the dropped text quoted back in
  `contract.violations`.
- **`protect` / `protect_regex`** — literals and regex matches swapped for markers before
  stage 1 and restored after stage 3, the way display math already is. Anything you cannot
  afford to lose and is not math goes here: code spans, URLs, Quarto shortcodes, citation
  keys. Losing one is a blocking violation, so it can no longer ship silently.
- **`glossary`** — `{"term": ..., "instead_of": [...], "required": bool}`, or a bare string
  for just the term. The spelling check folds case and diacritics, so it catches
  `Königsberg` → `Konigsberg`; `instead_of` catches a near-synonym the source never used.

The response gains a `contract` object: `{mode, max_sentences, sentences, protected, repairs,
violations, satisfied}`. **Read `satisfied` before `review.verdict`** — the reviewer's verdict
is noisy, and `reject` with `satisfied: true` is usually fine.

Two violations are fixed mechanically when the repair pass fails: overflow is truncated, and
`imperative` narration is de-narrated ("We will store…" → "Store…"). Both are recorded in
`violations` with what was changed — nothing is edited silently — so read them and check the
result rather than trusting the flag.

`POST /check` runs the whole contract with no model in the loop. Use it to test a rule, or to
re-check text you edited by hand.

## Mathematics

- **Display math** (`$$ $$`, `\[ \]`, `align` / `equation` / `gather` / `subequations` …)
  never reaches any model. It is swapped for a marker and substituted back verbatim, so
  it is guaranteed byte-identical. It splits the outline rather than being summarised into it.
- **Inline math** (`$ $`, `\( \)`) rides along inside the bullets and does pass through the
  style and review models. The server checks afterwards that every expression survived and
  reports any loss in `warnings`.

**If `warnings` is non-empty, do not ship the output as is.** Re-run, or patch the missing
notation back by hand against the source.

## Lists, headings and tables

The pipeline outputs prose. Feed it a bulleted list and stage 1 flattens the bullets into
outline items, and stage 2 writes them out as one paragraph — the list is gone. Feed it a
table and it will be prose too.

So:

- **Send prose to the server; keep structure out of it.** Tables, headings and citation
  strings should never be in the payload. Anything that must survive byte-for-byte and is not
  math — Quarto shortcodes like `{{< var x >}}`, URLs, code spans, reference lists — goes in
  `protect` or `protect_regex`, not into a placeholder you invent yourself. A placeholder the
  server does not know about gets flattened into prose ("[[CODE_1]]" comes back as "Code 1")
  and nothing warns you.
- **Send list items one at a time** if the output must stay a list. One call per bullet
  returns one line per bullet. Set `mode` to `bullet` or `imperative` as well — a bare
  fragment invites the style model to expand it into a paragraph or to narrate it, and the
  mode is what stops both.
- Feed long documents one section at a time. The server splits at 6000 characters, but
  section-sized inputs read better.

## Controlling sentence shape

Stage 1 normalises the input into plain Japanese statements, so anything carried by the
*shape* of the source — a verbless opening, a deliberately clipped fragment — is gone before
the style model sees it. Turning the temperature up does not bring it back; it only shuffles
vocabulary.

If you need control over the sentence shape, write the Japanese outline yourself and post it
as `text`. Stage 1 will pass your bullets through nearly unchanged, and stage 2 will follow
their rhythm. `POST /outline` shows you what the automatic version looks like first.

## Reviewing the output

The reviewer is a checker, not a guarantee. You still own the result:

- diff `draft` against `styled` and `styled` against the source, and read `review.issues`;
- if the model invents a transition or a claim the reviewer missed, delete it rather than
  arguing with the model.

**If you reject the model's wording and keep your own, say so.** The failure mode of this
skill is quietly restoring your own sentences, changing a word or two, and reporting it as a
rewrite in the user's voice. The user asked for their model's output, not yours. When you
override it, name the lines you overrode and why — a wrong fact, a lost term, a broken
structure — and let them judge.

## If the server is not answering

```bash
curl -s http://127.0.0.1:8823/health                          # models present?
launchctl kickstart -k "gui/$UID/com.skojaku.style-server"    # restart it
tail -50 ~/Library/Logs/style-server.log                      # why it died
```

It runs as a launchd agent and starts at login. It needs Ollama running (Ollama.app must be
set to launch at login). Source and setup: `~/models/finetuning/kojaku-style-12b-v5-portable`.
Prompts are in `style-server/prompts.py`; the reviewer's default checks live in
`REVIEW_SYSTEM` there.
