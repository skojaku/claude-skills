---
name: scientific-review
description: Hierarchical review of scientific documents (papers, grant proposals) without editing them. Layer 1 spawns naive skim and adversarial critics that file findings as GitHub issues; Layer 2 triages each finding simplification-first (cut before patch). Runs coarse to fine — document skeleton, sections, paragraphs — locking user decisions between stages, then a sentence-level style check. Use for any review or critique request on paper or proposal prose. For writing, rewriting, or wording edits, use the scientific-writing skill instead.
---

# Scientific Review

Two-layer, staged review pipeline for the user's scientific documents. Layer 1 finds problems; Layer 2 decides the cheapest sound response to each, preferring to cut logic rather than add it. Findings live in GitHub issues, not in chat. This skill decides what to change but never edits the manuscript — edits happen afterwards under the scientific-writing skill.

- **`workflow.md`** — the orchestration: stages, layers, issue conventions, decision points. Read first on any review request.
- **`agents/skim-critic.md`** — Layer 1. A naive busy reader; reads back what the skim extract alone conveys.
- **`agents/adversarial-critic.md`** — Layer 1. A hostile expert; attacks claims and evidence at the stage's granularity.
- **`agents/simplifier.md`** — Layer 2. Triages the filed issues: patch, cut, or reject; owns the risk–return audit.
- **`agents/style-critic.md`** — final pass. Sentence-level check against scientific-writing's `style.md`.

Each `agents/*.md` file fully describes one subagent: its role, its exact inputs, its output contract. To spawn one, pass it the file's content plus only the inputs the file names — nothing else.

## Principles

- **Critics are naive.** A Layer 1 critic sees only the manuscript (the skim critic: only the skim extract). No conversation history, no skill files, no takeaway list. Naivety is the measurement instrument.
- **Simple beats complex.** A clear argument outperforms a precise but braided one that does the same work; a reader who cannot follow the defense rejects, they do not suspend judgment. When a patch would add a qualifier chain or a new argumentative thread, cut the vulnerable element instead and move its function to a stronger instrument the document already has.
- **Findings are issues.** Critics file GitHub issues and return only issue numbers; the coordinator triages from `gh issue list` and opens bodies selectively, keeping full critiques out of its context.
- **Decisions lock.** Once the user rules on a finding, the ruling is recorded on the issue and later stages do not reopen it.

## Models

Layer 1 critics and the simplifier run on Opus-tier agents. The style critic runs on Haiku. Post-review edits (under scientific-writing) use Sonnet-tier editors, Haiku for pure wording fixes.

## Reporting

Report to the user in Japanese: per stage, findings ranked by severity with Layer 2's recommendation on each, and the `needs-decision` issues as explicit questions. Do not translate the document's own prose.
