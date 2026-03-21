# Orchestrated Loop Skill

## Purpose

Set up a **lead-agent + subagent** orchestration loop for any multi-step, iterative task. The lead agent owns the task queue and delegates work; subagents pick one unit of work, execute it, and exit. Compatible with the Ralph Loop plugin (`/ralph-loop`) or standalone use.

---

## Core Pattern

```
Lead Agent (loop controller)
  ├─ Maintains: progress.txt, shared state files
  ├─ Spawns subagents via Task tool
  ├─ Waits for each subagent to complete
  └─ Repeats until all work is done or stop condition met

Subagent (spawned per work unit)
  ├─ Reads progress.txt → picks ONE unclaimed item
  ├─ Claims it (marks in-progress) immediately to prevent double-work
  ├─ Does the work, appends results to shared output files
  ├─ Marks item done in progress.txt
  └─ Exits
```

---

## When Invoked

Do NOT immediately generate files. Run the elicitation protocol below first.

### Step 1 — Elicit the task structure

Ask the user:

1. **What is the task?** Describe the overall goal in one sentence.
2. **What are the work units?** What is one "item" that a subagent processes? (e.g., one paper, one file, one ticket, one data point)
3. **How are work units discovered?** Are they files in a directory, lines in a file, API calls, user-provided list?
4. **What does a subagent produce?** What output does it write, and where?
5. **Is there cross-unit state?** Is there accumulated context (themes, running totals, learned patterns) that each subagent should read from and append to?
6. **What is the stop condition?** When is the loop done? (e.g., all items processed, N iterations, external signal)
7. **Are any phases parallelizable?** Can multiple subagents run concurrently on different items, or must they run sequentially?
8. **What subagent types are needed?** Is there one kind of subagent, or multiple specialized roles (e.g., extract → plan → process → synthesize)?

Push back if answers are vague. A "work unit" must be atomic and independently executable.

---

### Step 2 — Design the orchestration

Using the elicited answers, define:

#### Shared State Files

| File | Purpose | Access pattern |
|------|---------|----------------|
| `progress.txt` | One line per work unit; checkboxes track status | Lead reads; subagents claim + mark done |
| `<output>.md` or `<output>.txt` | Accumulated subagent output | Subagents append only; never read |
| `context.txt` (if cross-unit state needed) | Running insights/themes across units | Subagents read before work, append after |

**`progress.txt` format:**
```
[ ] item_a   — unclaimed
[~] item_b   — in-progress (claimed by a running subagent)
[x] item_c   — done: <one-line note>
```

#### Lead Agent Steps

1. **Init** (first run only): create state files from templates if they don't exist; populate `progress.txt` with all work units.
2. **Check stop condition**: if all items are `[x]` and any final synthesis is done → output `<promise>LOOP COMPLETE</promise>` and stop.
3. **Spawn subagents**: based on task design, either:
   - Spawn one sequential subagent for the next unclaimed item, wait, repeat.
   - Spawn N parallel subagents for unclaimed items (safe only if subagents don't read each other's output).
   - Spawn a specialized subagent for the current phase (e.g., synthesis after all items done).
4. **Handle failure**: if a subagent leaves an item stuck in `[~]` (in-progress but never completed), reset it to `[ ]` and retry or escalate to user.

#### Subagent Steps (per work unit)

1. Read `progress.txt` → find first `[ ]` item.
2. **Immediately** mark it `[~]` (in-progress) before doing any work.
3. Read `context.txt` if cross-unit state is needed.
4. Execute the work unit (call tools, process files, run commands, etc.).
5. Append results to the designated output file(s). **Append only — never overwrite shared files.**
6. Append to `context.txt` if new cross-unit insights were gained.
7. Mark item `[x]` in `progress.txt` with a one-line note.
8. Exit.

---

### Step 3 — Generate the orchestration spec

Produce a `PROMPT.md` (for use with `/ralph-loop`) or a standalone `SKILL.md` (for use as a skill) with the following sections filled in for the specific task:

```markdown
# <Task Name> Loop

## Shared Files
- `progress.txt` — <description of work units tracked>
- `<output file>` — <what is accumulated and how>
- `context.txt` — <cross-unit state, if any>

## Lead Agent (loop controller)

### Initialization (first run only)
- <How to discover/enumerate work units>
- <How to populate progress.txt>
- <Which template files to copy, if any>

### Loop Logic
1. Check stop condition: <specific condition>
2. Spawn <subagent type(s)>: <sequential or parallel, under what condition>
3. Wait. Repeat.
4. On completion: <final action, e.g., spawn synthesis subagent, write summary>
5. Output `<promise>LOOP COMPLETE</promise>` and stop.

### Failure Handling
- If item stuck in `[~]` for more than one iteration: reset to `[ ]` or escalate.

## Subagent: <Name> (spawned via Task tool, general/mode: subagent)

### Inputs
- Reads: `progress.txt`, `context.txt` (if applicable)

### Work
1. Claim next `[ ]` item → mark `[~]`
2. <Domain-specific steps>
3. Append results to `<output file>`
4. Update `context.txt` if applicable
5. Mark `[x]` in `progress.txt`

## Stop Conditions
- <Primary: all work units done>
- <Secondary: explicit user cancellation, repeated subagent failures>

## Output Writing Style
- <Specify tone, format, notation conventions for the task domain>
```

---

### Step 4 — Confirm and create files

Present the design to the user:
- The proposed shared files and their formats
- The lead agent loop logic
- Each subagent's role and access pattern
- The stop condition

Ask: *Does this capture the task correctly? Any edge cases (empty inputs, partial runs, retries)?*

After confirmation:
1. Create `progress.txt`, `context.txt`, and any template files if starting from scratch.
2. Write the `PROMPT.md` or `SKILL.md` for the specific task.
3. If using `/ralph-loop`, provide the exact invocation command.

---

## Anti-Patterns to Avoid

- **Subagents reading shared output files** — they should append only, never read what other subagents wrote (use `context.txt` for that).
- **No claim step** — without marking `[~]` immediately, parallel subagents may process the same item twice.
- **Lead agent doing domain work** — the lead only orchestrates; all domain-specific work belongs in subagents.
- **Unbounded loops** — always define a concrete stop condition tied to `progress.txt` state.
- **Monolithic subagents** — if a subagent's work can be split into phases (extract → analyze → write), consider separate subagent types.
- **Overwriting shared files** — all subagent writes must be appends; only the synthesis phase (if any) may overwrite a designated output file.

---

## Example Invocation (Ralph Loop)

```
/ralph-loop "Run the <task name> orchestration loop. Lead agent manages progress.txt and spawns subagents. Stop when all items are [x] and final output is written. Output <promise>LOOP COMPLETE</promise> when done." --completion-promise "LOOP COMPLETE" --max-iterations 50
```
