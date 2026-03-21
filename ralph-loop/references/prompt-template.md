# PROMPT.md Template

Use this template when generating a `PROMPT.md` for the user's specific task. Replace every `<placeholder>` with concrete values — no placeholders in the final output.

---

```markdown
# <Task Name> Loop

## Shared Files
- `progress.txt` — one line per <work unit type>; `[ ]` unclaimed, `[~]` in-progress, `[x]` done
- `<output file>` — <what accumulates here, e.g., "paper summaries, append only">
- `context.txt` — <cross-unit state, e.g., "running themes and gaps across papers"> [omit if not needed]

## Lead Agent (loop controller — no domain work)

### First run only
1. <How to discover work units, e.g., "list all .pdf files in ./papers/">
2. Write `progress.txt` with one `[ ]` entry per unit.
3. <Copy any template files, e.g., "copy templates/research_note.md to ./"> [omit if not needed]

### Every run
1. Read `progress.txt`.
2. If all entries are `[x]` and <final condition, e.g., "synthesis.md exists"> → output `<promise>LOOP COMPLETE</promise>` and stop.
3. <Spawn logic — choose one:>
   - Sequential: spawn one subagent for the next `[ ]` item. Wait. Repeat.
   - Parallel: spawn subagents for all `[ ]` items simultaneously. Wait. Repeat.
   - Phased: if <condition>, spawn <Phase A subagent>; else spawn <Phase B subagent>.
4. If any item stuck in `[~]` from a previous run: reset to `[ ]` and retry.

## Subagent: <Name>
*(spawned via Task tool, general / mode: subagent)*

1. Read `progress.txt` → find first `[ ]` item.
2. Mark it `[~]` immediately before doing any other work.
3. <Read context.txt for accumulated <themes/state>.> [omit if not needed]
4. <Domain-specific step 1, e.g., "run uv run python tools/extract_pdf.py <file>">
5. <Domain-specific step 2>
6. Append result to `<output file>`. Do not read it.
7. <Append new insights to context.txt. Note contradictions; avoid restating existing themes.> [omit if not needed]
8. Mark `[x] <item> — <one-line note>` in `progress.txt`.

## <Optional: Additional Subagent Role, e.g., Synthesis>
*(spawned once after all items are [x])*

1. Read `<output file>` and `context.txt`.
2. <Write final output, e.g., "overwrite synthesis.md with: Synthesis, Contradictions, Open Questions">

## Stop Conditions
- All `progress.txt` entries are `[x]` <and final output exists>.
- Subagent fails repeatedly on the same item → escalate to user.
- User cancels.

## Output Style
- <Tone and format conventions for this task domain>
```

---

## Example: Literature Review

```markdown
# Literature Review Loop

## Shared Files
- `progress.txt` — one line per PDF; `[ ]` unread, `[~]` being read, `[x]` done
- `research_note.md` — paper summaries and themes, append only
- `context.txt` — running cross-paper insights, gaps, contradictions

## Lead Agent

### First run only
1. List all .pdf files in ./papers/.
2. Write `progress.txt` with one `[ ]` entry per PDF.
3. Copy templates/research_note.md and templates/context.txt to ./.

### Every run
1. Read `progress.txt`.
2. If all `[x]` and synthesis.md exists → output `<promise>LOOP COMPLETE</promise>` and stop.
3. If any papers are `[ ]`: spawn one Reading subagent for the next unclaimed paper. Wait.
4. If all papers are `[x]` and synthesis.md does not exist: spawn Synthesis subagent. Wait.
5. Reset any `[~]` items stuck from a previous run to `[ ]`.

## Subagent: Reading
*(spawned via Task tool, general / mode: subagent)*

1. Read `progress.txt` → find first `[ ]` paper.
2. Mark it `[~]` immediately.
3. Read `context.txt` for accumulated themes and gaps.
4. Run `uv run python tools/extract_pdf.py <paper.pdf>`.
5. Append a new entry to `research_note.md` (use template format). Do not read it.
6. Append new insights to `context.txt`. Note contradictions; avoid restating existing themes.
7. Mark `[x] paper.pdf — one-line summary` in `progress.txt`.

## Subagent: Synthesis
*(spawned once, after all papers are [x])*

1. Read `research_note.md` and `context.txt`.
2. Overwrite `synthesis.md` with: Synthesis, Contradictions, Open Questions.

## Stop Conditions
- All papers `[x]` and `synthesis.md` exists.
- Reading subagent fails 3× on same paper → escalate to user.
- User cancels.

## Output Style
- Concise; sacrifice grammar but not clarity
- LaTeX for equations
- Paragraph narrative, no bullets
```
