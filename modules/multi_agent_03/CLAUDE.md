# Module 03: Multi-Agent Research System

## Exam Coverage
- **Primary Domain**: D1 Agentic Architecture (~27% of exam)
- **Secondary Domains**: D2 Tool Design (~18%), D5 Context Management (~15%)
- **Combined**: 60% of exam weight — this is a high-value module

## Learning Objectives
1. Implement the orchestrator-worker pattern (Anthropic Pattern #4)
2. Scope subagent context — workers get ONLY task-relevant information, never full conversation history
3. Build structured error propagation with categories, retryability, and partial results
4. Use Claude Code native subagents (agent files) for research coordination
5. Annotate conflicting findings with source attribution

## Key Patterns
- **Coordinator manages ALL inter-agent communication**: Workers never talk to each other directly. The coordinator dispatches tasks, collects results, resolves conflicts, and synthesizes.
- **Scoped context for subagents**: Each worker receives ONLY the subtopic and output format — NOT the full conversation history or other workers' results. This prevents context pollution and reduces token cost.
- **Conflict annotation with attribution**: When workers return contradictory findings, the coordinator annotates both with source attribution rather than silently picking one.
- **Structured error propagation**: Failures return `SubagentResult.failure()` with category, message, isRetryable, and alternatives — NEVER empty dicts or silent failures.

## Anti-Patterns Tested
- **AP6**: Generic error messages — errors MUST include category, message, isRetryable, and what was attempted
- **AP7**: Silent error suppression — returning `{}` or `[]` on failure instead of structured error
- **AP8**: Too many tools per agent — a few focused tools scoped to its task is a good heuristic for worker design (not a hard cap enforced by the platform). For agents that genuinely need many tools, Anthropic's Nov 2025 Tool Search Tool (keeps tool defs out of context until requested) and Programmatic Tool Calling (Claude writes code to call multiple tools in one round-trip) are the current scaling answer — reach for those before assuming a tool-count ceiling
- **AP9**: Same-session self-review — use separate context (context: fork) for evaluation

## Progression
- **Starter**: Build coordinator skeleton with delegate and synthesize tool definitions
- **Intermediate**: Implement structured error propagation with SubagentResult
- **Advanced**: Wire up Claude Code native agent files for research-lead and fact-checker
