# claude-skills

Personal Claude Code skills.

## Skills

- **scientific-writing** — Draft papers/grants for busy readers who skim: reader model, skeleton-first drafting loop, and the user's voice
- **scientific-review** — Two-layer staged review: naive critics file findings as GitHub issues (Layer 1), a simplifier triages them cut-before-patch (Layer 2), coarse to fine with user decisions locked between stages
- **write-prd** — Guides through creating a detailed PRD via structured interview and submits as a GitHub issue
- **snakemake** — Snakemake style guide and utilities (`utils.smk`) for bioinformatics/data workflows
- **ralph-loop** — Reusable lead-agent + subagent orchestration loop pattern; elicits task structure and generates `PROMPT.md`/`SKILL.md` for any iterative multi-step task
- **officecli** — Create, analyze, and modify Office documents (.docx, .xlsx, .pptx) via the officecli CLI

## Installation

These skills are managed as a submodule in [dotfiles](https://github.com/skojaku/dotfiles) and symlinked to `~/.claude/skills/`.

To install manually:

```bash
ln -s /path/to/claude-skills ~/.claude/skills
```
