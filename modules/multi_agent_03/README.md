# Module 03: Multi-Agent Research System — Progression Guide

## Starter: Coordinator Pattern

Build the central coordinator that manages research subagents.

1. Complete `starter/coordinator.py` — implement delegate and synthesize tools
2. Run `starter/tests/test_coordinator.py` to validate coordination patterns

**Key exam concept**: The coordinator is the ONLY agent that sees the full picture.
Workers receive scoped context (subtopic + format) and return structured results.
Workers NEVER communicate with each other or see each other's outputs.

## Intermediate: Structured Error Propagation

Build the error handling layer that prevents silent failures.

1. Complete `intermediate/error_propagation.py` — implement ErrorCategory and SubagentResult
2. Run `intermediate/tests/test_errors.py` to validate error structure

**Key exam concept**: When a subagent fails, it MUST return a structured error
with category (TRANSIENT/VALIDATION/NOT_FOUND/PERMISSION), a human-readable message,
whether it's retryable, what was attempted, and alternative approaches.
NEVER return `{}` or `[]` as a failure response (AP7).

## Advanced: Claude Code Native Agents

Wire up real agent files that Claude Code can orchestrate.

1. Review `advanced/agents/research-lead.md` — the primary researcher agent
2. Review `advanced/agents/fact-checker.md` — the verification agent (runs on haiku)
3. Run `advanced/tests/test_subagents.py` to validate context isolation

**Key exam concept**: Agent files define tools, model, and maxTurns for subagents.
The research-lead uses a capable model (sonnet/opus) with more turns.
The fact-checker uses haiku (cheaper, faster) with fewer turns.
This is cost-efficient orchestration — use the right model for each task's complexity.
