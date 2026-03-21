---
name: ralph-loop
description: Set up an orchestrated lead-agent + subagent loop for any iterative multi-step task. Use this skill whenever the user wants to process a collection of items one at a time (papers, files, tickets, data points), build up accumulated results across iterations, or run a multi-phase pipeline with a controlling agent and worker subagents. Also trigger on "ralph loop", "lead agent loop", "orchestration loop", "subagent delegation", processing a list of things automatically, or iterating over a batch of inputs. Trigger even when the user just describes the task without naming the pattern—if it sounds like "do X for each Y and accumulate results", this skill applies.
---

# Orchestrated Loop Skill

Help the user set up a **lead-agent + subagent** orchestration loop, then produce a ready-to-run `PROMPT.md`.

The lead agent owns the task queue and coordinates; subagents claim one unit of work, do it, and exit. This pattern works for any batch task: literature review, code refactoring, data extraction, ticket triage, etc.

---

## Step 1 — Understand the task

Ask the user these questions (conversationally — don't dump them all at once, probe where answers are vague):

1. What is the overall goal in one sentence?
2. What is one **work unit** — the smallest thing a subagent processes? (e.g., one paper, one file, one row)
3. How are work units **discovered**? (files in a dir, lines in a file, API response, user-provided list?)
4. What does a subagent **produce**? Where does it write output?
5. Is there **cross-unit context** that accumulates? (running themes, totals, learned patterns that each subagent should read before starting)
6. Are any phases **parallelizable**, or must units be processed in order?
7. Are there **multiple subagent roles** (e.g., extract → plan → process → synthesize), or just one kind?
8. What is the **stop condition**? (all items done, N iterations, explicit signal)

A work unit must be atomic — a subagent should be able to claim and finish it without needing to know about other units.

---

## Step 2 — Design the orchestration

Using the answers, design:

### Shared state files

Three files cover most cases:

- **`progress.txt`** — one line per work unit, tracks claim status. Lead reads; subagents claim and mark done.
- **`output.<ext>`** — accumulated subagent results. Subagents **append only**; never read.
- **`context.txt`** — cross-unit insights (if needed). Subagents read before working, append after.

`progress.txt` format:
```
[ ] item_a
[~] item_b      ← claimed, in-progress
[x] item_c — done: one-line note
```

The `[~]` claim step is critical: a subagent must mark an item in-progress *before* doing any work, not after. Without this, parallel subagents double-process the same item.

### Lead agent logic

1. **Init** (first run only): enumerate work units, write `progress.txt`, copy any templates.
2. **Check stop**: if all `[x]` and any final phase is done → output `<promise>LOOP COMPLETE</promise>` and stop.
3. **Spawn subagent(s)**: sequential (one next unclaimed item) or parallel (N unclaimed items), depending on whether units are independent.
4. **Wait**. Repeat from step 2.
5. **Failure recovery**: if an item is stuck in `[~]` across iterations, reset to `[ ]` or escalate to user.

The lead agent does **no domain work** — all domain logic belongs in subagents.

### Subagent logic (per work unit)

1. Read `progress.txt` → find first `[ ]` item.
2. Mark it `[~]` immediately.
3. Read `context.txt` if cross-unit state is needed.
4. Do the work (call tools, process files, run commands).
5. Append results to output file(s). **Append only — never overwrite shared files.**
6. Append to `context.txt` if new cross-unit insights gained.
7. Mark `[x]` with a one-line note in `progress.txt`.
8. Exit.

---

## Step 3 — Generate the PROMPT.md

Confirm the design with the user, then write `PROMPT.md` for their specific task. Read `references/prompt-template.md` for the exact format to use — fill in every placeholder from the user's answers.

Keep the generated file concrete: real filenames, real subagent names, real stop conditions. No placeholders in the output.

---

## Step 4 — Create initial state files

After writing `PROMPT.md`:
1. Create `progress.txt` with all work units listed as `[ ]`.
2. Create empty `context.txt` if cross-unit state is needed.
3. Copy any template files the subagents will reference.

Provide the exact `/ralph-loop` invocation command:
```
/ralph-loop "<task description>. Output <promise>LOOP COMPLETE</promise> when done." --completion-promise "LOOP COMPLETE" --max-iterations <N>
```

---

## Anti-patterns to avoid

- **No `[~]` claim step** — parallel subagents will race and double-process items.
- **Subagents reading shared output** — they should append only; route cross-unit state through `context.txt`.
- **Lead agent doing domain work** — it orchestrates; subagents work.
- **No concrete stop condition** — always tie the stop to `progress.txt` state.
- **Monolithic subagents** — if work has distinct phases (extract / analyze / synthesize), use separate subagent roles.
