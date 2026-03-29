# Module 02: Claude Code Configuration

## Exam Coverage
- **Primary Domain**: D3 Claude Code Configuration (~20% of exam)
- **Secondary Domain**: D5 Context Management (~15% of exam)
- **Combined**: 35% of exam weight — second highest-value module

## Learning Objectives
1. Master the CLAUDE.md hierarchy: user → project → directory → @import → rules
2. Write path-specific rules with `paths:` directive to scope enforcement to file globs
3. Build slash commands with `argument-hint:` for parameterized workflows
4. Create skills with `context: fork` for isolated subagent execution
5. Understand context scoping — skills run in forked context, NOT the parent session

## Key Patterns
- **CLAUDE.md Hierarchy**: user (~/.claude/CLAUDE.md) → project (repo root) → directory (subdir) → @import → .claude/rules/*.md
- **`paths:` directive**: Scopes a rule file to matching file globs (e.g., `paths: src/app/api/**/*.ts`)
- **`argument-hint:`**: Frontmatter in slash commands — provides placeholder text for $ARGUMENTS
- **`context: fork`**: Skills run as isolated subagents with their own context window — critical for avoiding AP9 (same-session review bias)
- **`allowed-tools:`**: Restricts which tools a slash command can use — principle of least privilege

## Anti-Patterns Tested
- **AP3**: Using prompt instructions to enforce critical rules instead of hooks/programmatic enforcement
- **AP8**: Giving an agent more than 5 tools (18+ tools degrades selection reliability)
- **AP9**: Same-session self-review — skills with `context: fork` solve this by creating isolated evaluation context

## Progression
- **Starter**: Build a CLAUDE.md for a fintech dashboard + write path-scoped rule files
- **Intermediate**: Create slash commands with argument-hint and allowed-tools
- **Advanced**: Build a security audit skill with context: fork (isolated subagent)
