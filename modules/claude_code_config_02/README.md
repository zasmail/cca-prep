# Module 02: Claude Code Configuration — Progression Guide

## Starter: CLAUDE.md + Rules

Build the foundational configuration layer for a Next.js fintech dashboard project.

1. Complete `starter/fintech_dashboard_claude.md` — fill in all TODO sections
2. Review `starter/rules/api-routes.md` — understand path-scoped rules
3. Run `starter/tests/test_config.py` to validate your work

**Key exam concept**: CLAUDE.md hierarchy determines instruction precedence.
Directory-level CLAUDE.md overrides project-level for files in that directory.

## Intermediate: Slash Commands

Build parameterized slash commands that drive structured workflows.

1. Study `intermediate/commands/tdd-cycle.md` — RED/GREEN/REFACTOR with $ARGUMENTS
2. Study `intermediate/commands/plan-then-build.md` — plan mode to auto-accept pattern
3. Run `intermediate/tests/test_commands.py` to validate frontmatter syntax

**Key exam concept**: `argument-hint` provides the placeholder shown to the user.
`allowed-tools` restricts which tools the command can invoke (least privilege).

## Advanced: Skills with Context Isolation

Build a security audit skill that runs as an isolated subagent.

1. Complete `advanced/skills/security-audit/SKILL.md`
2. Run `advanced/tests/test_skills.py` to validate frontmatter and isolation concepts

**Key exam concept**: `context: fork` creates a NEW context window for the skill.
The subagent does NOT see the parent conversation — this prevents AP9 (same-session review bias).
The subagent gets ONLY the skill instructions + any files it reads itself.
