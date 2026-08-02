---
title: Claude Code Best Practices
speaker: Anthropic (Claude Code docs)
source: https://code.claude.com/docs/en/best-practices
retrieved: 2026-07-16
themes:
  - context-engineering
  - tool-design-mcp
  - skills
  - claude-code-workflows
  - enforcement-reliability
  - memory
---

## Core Claims

1. Context window management is the single most important resource to manage in a Claude Code session; context degrades performance as it fills.
2. Without a pass/fail verification signal, "looks done" becomes the only signal and humans become the verification loop.
3. Hooks are deterministic and guaranteed; prompt-based guidance can always be ignored.
4. A Stop hook blocks turn-end but Claude Code overrides it after 8 consecutive blocks—a hard-coded safety escape hatch.
5. CLAUDE.md must be ruthlessly pruned; bloated versions cause Claude to ignore parts of it.
6. Explore → Plan → Implement → Commit is the four-phase workflow; skip planning only for small, clearly-scoped changes.
7. Fresh-context reviewers avoid self-review bias better than same-session review.
8. After 2 failed corrections on the same issue, `/clear` and rewrite beats continued patching.
9. Kitchen-sink sessions (mixing unrelated tasks) and unscoped investigation are recurring failure modes.
10. Headless mode (`claude -p`) with `--allowedTools` scoping enables unattended batch runs.

## Patterns & Frameworks

- **Explore → Plan → Implement → Commit**: Four-phase workflow; plan mode reads without changes, gates on quality, scales to multi-file/unfamiliar code.
- **Context compaction**: Auto-preservation of key code/decisions; guided via `/compact <instructions>`; CLAUDE.md can specify what to always preserve.
- **Checkpoint/rewind**: Every prompt creates a snapshot; `/rewind` restores conversation-only, code-only, or both to any prior point.
- **Fresh-context reviewer**: Parallel session reviews code it didn't write—Writer/Reviewer pattern avoids confirmation bias.
- **Verification gates**: Tests, build exit code, linter, diff fixture, or screenshot comparison; ask Claude to show evidence, not assert success.
- **Environment setup layers**: CLAUDE.md (hierarchical: global, project, directory), hooks (deterministic), skills (reusable workflows), subagents (isolated context).

## Numbers & Specifics

- **8 consecutive blocks**: Stop hook override threshold (safety escape hatch)
- **2 failed corrections**: Threshold to `/clear` and rewrite instead of continued patching
- **Context burn rate**: One debugging session can burn tens of thousands of tokens
- **Three approval-fatigue reduction mechanisms**: auto mode (classifier gates risky actions), permission allowlists, OS-level sandboxing
- **Skip planning for**: typo fix, log line, variable rename (overhead only worth it for multi-file/uncertain/unfamiliar)
- **CLAUDE.md scope**: Non-obvious bash commands, code style, testing preferences, repo etiquette, architecture decisions, gotchas; exclude: inferable content, defaults, long docs, fast-changing info

## Quotes

> "Context fills fast... and performance degrades as it fills — Claude can start 'forgetting' earlier instructions."

> "Without a pass/fail signal, 'looks done' is the only signal, and the human becomes the verification loop."

> "Hooks are scripts that run automatically at defined points — deterministic (guaranteed), unlike advisory CLAUDE.md instructions."

> "The 'would removing this line cause a mistake?' test" (pruning heuristic for CLAUDE.md)

> "A clean session with a sharper prompt usually beats a long polluted one."

## Applied AI Relevance

- **Enforcement requires code, not prompts**: Critical business rules need hooks or schema validation, not CLAUDE.md guidance. Ties directly to CCA-F D3 (programmatic enforcement vs. prompt-based) and exam anti-pattern #3.
- **Context is the hardest constraint**: Manage aggressively via `/clear` (reset between tasks), `/compact` (guided compression), subagents (exploration in isolation), and checkpoints (fast recovery). Directly relevant to D5 (context management).
- **Verification gates are non-negotiable**: Tests, build exit code, screenshot comparison—not assertions. Escalates to `Esc` interrupt, rewind, `/clear`, and fresh-context review. Prevents shipping unverified work.
- **Parallel + fresh-context scales unattended runs**: Writer/Reviewer pattern, headless mode with `--allowedTools` scoping, and adversarial review step eliminate self-review bias and enable batch automation. Core pattern for D3 CI/CD scenarios.

---

*Distilled: 574 words. Direct source for D3 (Claude Code Configuration) exam domain.*
