---
name: scientific-review
description: Hierarchical review of scientific documents (papers, grant proposals) without editing them. Layer 1 spawns naive skim and adversarial critics that file findings as GitHub issues; Layer 2 triages each finding simplification-first (cut before patch). Runs coarse to fine — document skeleton, sections, paragraphs — locking user decisions between stages, then a sentence-level style check. Use for any review or critique request on paper or proposal prose. For writing, rewriting, or wording edits, use the scientific-writing skill instead.
---

# Scientific Review

Two-layer staged review. Layer 1 finds problems; Layer 2 picks the cheapest sound fix, cutting logic over adding it. Findings live in GitHub issues, not chat. This skill decides what to change; edits run under scientific-writing.

- `workflow.md` — stages, layers, issue conventions, decision points. Read first on any review request.
- `agents/skim-critic.md` — L1: naive busy reader, reads back the skim extract.
- `agents/adversarial-critic.md` — L1: hostile expert, attacks claims and evidence at the stage's scope.
- `agents/simplifier.md` — L2: triages issues (patch/cut/reject), owns the risk–return audit.
- `agents/style-critic.md` — final pass: sentences vs scientific-writing's `style.md`.

Each agent file fully defines one subagent: role, inputs, output. Spawn with the file's content + only the inputs it names.

## Principles

- **Critics are naive.** Only the manuscript (skim critic: only the extract) + repo/labels for filing. No history, no skill files, no takeaway list. Naivety is the measurement instrument.
- **Simple beats complex.** A reader who cannot follow a braided defense rejects. If a patch adds a qualifier chain or a new thread, cut the element and move its function to a stronger instrument already in the document.
- **Findings are issues.** Agents return issue numbers + one-liners only; coordinator triages from `gh issue list`, opens bodies selectively.
- **Decisions lock.** User rulings recorded on the issue; later stages never reopen them.

## Models

Critics + simplifier: Opus. Style critic: Haiku. Post-review edits (scientific-writing): Sonnet, Haiku for wording.

## Reporting

Japanese. Per stage: findings by severity with L2's recommendation; `needs-decision` issues as explicit questions. Never translate the document's own prose.
