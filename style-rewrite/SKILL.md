---
name: style-rewrite
description: Rewrite a passage into the user's own writing style by calling the local style-server API (http://127.0.0.1:8823). English or Japanese goes in, English prose in the user's voice comes out, with every LaTeX expression preserved byte for byte. Use when asked to put text "in my style" / 「自分のスタイルで」, to turn Japanese notes or bullets into English prose, or to restyle an existing draft. It changes voice only — structure and argument belong to the scientific-writing skill.
---

# style-rewrite

A local server that runs the user's fine-tuned style model. It always works in two stages:

1. the input is broken into a Japanese outline (`deepseek-v4-flash:cloud`), with display equations pulled out;
2. the outline goes to the user's fine-tuned model (`my-style-model`, thinking off), which writes English prose.

Roughly 5 s for a paragraph. Everything runs on the user's machine except stage 1.

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

Response fields: `styled` (the prose), `outline` (the intermediate Japanese bullets),
`warnings`, `timing`. Other endpoints: `POST /outline` (stage 1 only, when you want to
inspect or hand-edit the bullets), `POST /rewrite/stream` (SSE), `GET /health`.

Optional body fields: `style_temperature` (default 0.7 — lower it for a literal rewrite),
`outline_temperature` (default 0.2), `style_model`, `outline_model`.

## Mathematics

- **Display math** (`$$ $$`, `\[ \]`, `align` / `equation` / `gather` / `subequations` …)
  never reaches either model. It is swapped for a marker and substituted back verbatim, so
  it is guaranteed byte-identical. It splits the outline rather than being summarised into it.
- **Inline math** (`$ $`, `\( \)`) rides along inside the bullets and does pass through the
  style model. The server checks afterwards that every expression survived and reports any
  loss in `warnings`.

**If `warnings` is non-empty, do not ship the output as is.** Re-run, or patch the missing
notation back by hand against the source.

## Reviewing the output

The style model is a 12B local model. Treat its output as a draft:

- diff it against the source and restore any claim, number, citation, or hedge it dropped;
- feed long documents one section at a time — the server splits at 6000 characters, but
  section-sized inputs read better;
- if it invents a transition or a claim, delete it rather than arguing with the model.

## If the server is not answering

```bash
curl -s http://127.0.0.1:8823/health                          # models present?
launchctl kickstart -k "gui/$UID/com.skojaku.style-server"    # restart it
tail -50 ~/Library/Logs/style-server.log                      # why it died
```

It runs as a launchd agent and starts at login. It needs Ollama running (Ollama.app must be
set to launch at login). Source and setup: `~/models/finetuning/kojaku-style-12b-v5-portable`.
