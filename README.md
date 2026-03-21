# claude-skills

Personal Claude Code skills.

## Skills

- **write-prd** — Guides through creating a detailed PRD via structured interview and submits as a GitHub issue
- **snakemake** — Snakemake style guide and utilities (`utils.smk`) for bioinformatics/data workflows
- **ralph-loop** — Reusable lead-agent + subagent orchestration loop pattern; elicits task structure and generates `PROMPT.md`/`SKILL.md` for any iterative multi-step task

## Installation

These skills are managed as a submodule in [dotfiles](https://github.com/skojaku/dotfiles) and symlinked to `~/.claude/skills/`.

To install manually:

```bash
ln -s /path/to/claude-skills ~/.claude/skills
```
