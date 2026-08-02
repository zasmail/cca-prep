---
title: "Claude Code best practices"
speaker: Anthropic (Claude Code docs)
source: https://code.claude.com/docs/en/best-practices
retrieved: 2026-07-16
method: webfetch
note: >
  Copyright limits prevent saving a full verbatim copy of this docs page (the raw
  fetch returned most prose paragraphs, tables, and code blocks essentially
  word-for-word). Below is a condensed, independently-written study-note summary
  (substantially shorter than, and restructured from, the source), keeping only
  short functional command/code examples verbatim since those are factual usage
  syntax rather than expressive prose. Refer to the source URL for the original text.
---

# Claude Code best practices — study notes

## Central constraint: context window
- Context fills fast (one debugging session can burn tens of thousands of tokens) and performance degrades as it fills — Claude can start "forgetting" earlier instructions.
- Managing context is described as the single most important resource to manage in a session.

## Give Claude a way to verify its own work
- Without a pass/fail signal, "looks done" is the only signal, and the human becomes the verification loop.
- Provide something Claude can check: tests, build exit code, linter, diff against a fixture, or a screenshot comparison.
- Escalating ways to gate on the check: ask Claude to run+iterate in one prompt → set a `/goal` condition re-checked every turn → a Stop hook that blocks turn-end deterministically until the check passes (Claude Code overrides the hook after 8 consecutive blocks) → a separate verification subagent/fresh-context reviewer.
- Ask Claude to show evidence (test output, command run, screenshot) rather than just asserting success.

## Explore → Plan → Implement → Commit
- Four-phase workflow: (1) plan mode to explore/read without changes, (2) ask for a detailed implementation plan (can open plan in an editor via Ctrl+G), (3) exit plan mode and implement + test, (4) commit with a descriptive message / open a PR.
- Skip planning for small, clearly-scoped changes (typo fix, log line, variable rename) — plan mode adds overhead that's worth it mainly for multi-file changes, uncertain approach, or unfamiliar code.

## Provide specific context in prompts
- Scope the task (file, scenario, testing preference), point to sources (e.g., "check git history"), reference existing code patterns to follow, describe symptom + likely location + definition of "fixed" — all reduce back-and-forth vs. vague asks.
- Rich content options: `@file` references, pasted/dragged images, URLs (allowlist frequent domains via `/permissions`), piping data (`cat error.log | claude`), or letting Claude fetch what it needs itself via Bash/MCP.
- Vague prompts ("what would you improve here?") are still useful when you can afford to course-correct and want Claude to surface things you hadn't thought to ask.

## Environment setup
- **CLAUDE.md**: special file read at the start of every session; `/init` generates a starter version from the codebase. Keep it short — the "would removing this line cause a mistake?" test. Include: non-obvious bash commands, non-default code style rules, testing preferences, repo etiquette, project-specific architecture decisions, environment quirks, and non-obvious gotchas. Exclude: things Claude can infer from code, default language conventions, long docs (link instead), fast-changing info, file-by-file descriptions. Supports `@path/to/file` imports and multiple locations (`~/.claude/CLAUDE.md` global, project root shared via git, `CLAUDE.local.md` personal/gitignored, parent/child directories for monorepos). Bloated CLAUDE.md causes Claude to ignore parts of it — prune like code.
- **Permissions**: three ways to reduce approval fatigue — auto mode (a classifier model blocks only risky actions), permission allowlists for known-safe commands, and OS-level sandboxing.
- **CLI tools**: install things like `gh` so Claude can use them directly instead of hitting rate-limited unauthenticated APIs; Claude can also learn unfamiliar CLI tools via `--help`.
- **MCP servers**: connect external tools (Notion, Figma, databases) via `claude mcp add`.
- **Hooks**: scripts that run automatically at defined points — deterministic (guaranteed), unlike advisory CLAUDE.md instructions. Claude can write hooks for you (e.g., "run eslint after every edit").
- **Skills**: `.claude/skills/<name>/SKILL.md` with YAML frontmatter (`name`, `description`); can define reusable workflows invoked via `/skill-name`; `disable-model-invocation: true` for side-effecting workflows that should only run when explicitly called.
- **Subagents**: `.claude/agents/<name>.md` defines a specialized assistant with its own context and allowed tool list — good for isolated/investigative tasks; invoke explicitly ("use a subagent to...").
- **Plugins**: bundle skills/hooks/subagents/MCP into one installable unit via `/plugin` marketplace.

## Communication patterns
- Ask Claude Code questions the way you'd ask a senior engineer about an unfamiliar codebase — no special prompting needed.
- For larger features, have Claude interview you first (using the AskUserQuestion tool) covering implementation, UI/UX, edge cases, and tradeoffs, then write a SPEC.md; start a fresh session to implement against the finished spec.

## Managing a session
- **Course-correct early**: `Esc` stops mid-action (context preserved); `Esc+Esc` / `/rewind` opens a menu to restore conversation/code/both to a prior checkpoint; "undo that" reverts changes; `/clear` resets context between unrelated tasks.
- Rule of thumb: after 2 failed corrections on the same issue, `/clear` and write a better initial prompt rather than continuing to patch — a clean session with a sharper prompt usually beats a long polluted one.
- **Context management**: auto-compaction preserves key code/decisions near context limits; `/compact <instructions>` for guided compaction; `Esc+Esc`/`/rewind` can summarize just part of the conversation; CLAUDE.md can specify what to always preserve during compaction; `/btw` asks a quick question that never enters conversation history.
- **Subagents for investigation**: delegate research ("use subagents to investigate X") so exploration reads files in a separate context instead of bloating the main conversation; also usable for post-implementation review.
- **Checkpoints**: every prompt creates a checkpoint (file snapshots); `/rewind` can restore conversation-only, code-only, or both. Checkpoints only capture changes made through Claude's own file-editing tools, not Bash/external-process changes — not a replacement for git.
- **Resuming**: `claude --continue` resumes the latest session; `claude --resume` picks from a list; `/rename` names sessions for easy return (e.g., "oauth-migration").

## Automate and scale
- **Non-interactive/headless mode**: `claude -p "prompt"` for CI/pre-commit/scripts; still creates a resumable session unless `--no-session-persistence`; `--output-format json` / `stream-json --verbose` for programmatic parsing.
- **Parallel sessions**: worktrees (isolated git checkouts), the desktop app (visual multi-session management), Claude Code on the web (cloud VMs), or agent teams (coordinated multi-session with shared tasks/messaging/team lead). Useful for a Writer/Reviewer pattern — a fresh-context session reviews code it didn't write, avoiding self-review bias.
- **Fan-out across files**: generate a task list, loop `claude -p` over it with `--allowedTools` scoping permissions for unattended batch runs, test on a few files before scaling to the full set.
- **Auto mode for autonomy**: `claude --permission-mode auto -p "..."` lets a classifier gate risky actions without a human in the loop; in headless (`-p`) mode, auto mode aborts if the classifier repeatedly blocks actions since there's no human fallback.
- **Adversarial review step**: before calling a long unattended run "done," have a fresh-context subagent review the diff against stated criteria — bundled `/code-review` skill does a correctness pass; a custom prompt can check a diff against a PLAN.md. Caveat: a reviewer asked to find gaps usually finds some even when work is sound — instruct it to flag only correctness/requirement gaps, not style, to avoid over-engineering churn.

## Common failure patterns to recognize
- **Kitchen-sink session** (unrelated tasks mixed in one context) → fix: `/clear` between tasks.
- **Repeated correcting** on the same issue → fix: `/clear` after 2 failed attempts, write a sharper prompt.
- **Over-specified CLAUDE.md** (too long, rules get lost) → fix: prune ruthlessly; convert enforceable rules to hooks.
- **Trust-then-verify gap** (plausible-looking code that misses edge cases) → fix: always provide a verification method; don't ship unverified work.
- **Unscoped "investigate X"** → fix: scope narrowly or delegate to a subagent so exploration doesn't consume main context.

## Exam-relevant takeaways
- This page is the direct source for D3 (Claude Code Configuration) content: CLAUDE.md hierarchy/pruning rules, hooks vs. prompt-based guidance (hooks = deterministic, ties to the "programmatic enforcement" exam theme), skills vs. subagents vs. MCP vs. plugins decision surface, and headless/`-p` mode + `--allowedTools` for CI/batch scenarios (D3/D5 crossover).
- Stop-hook detail worth remembering: Claude Code overrides a blocking Stop hook after **8 consecutive blocks** — a hard-coded safety escape hatch.
