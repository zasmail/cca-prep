---
name: quiz-me
description: Generates 5 exam-style multiple-choice questions on a given CCA-F topic (agentic-loops, hooks, mcp, tools, cicd, extraction, caching, batch-api, model-selection, context-management), presented one at a time with full explanations after each answer. Trigger on "quiz me on X", "test me on X", or "practice questions about X".
argument-hint: <topic: agentic-loops | hooks | mcp | tools | cicd | extraction | caching | batch-api | model-selection | context-management>
allowed-tools: Read
---

# Quiz Me: $ARGUMENTS

Generate 5 exam-style multiple choice questions for the CCA-F exam on the topic: **$ARGUMENTS**

## Topic Mapping
- **agentic-loops**: D1 — stop_reason checking, loop lifecycle, tool_result formatting, max_iterations as safety net
- **hooks**: D1, D3 — PreToolUse/PostToolUse, programmatic enforcement vs prompts, compliance gates
- **mcp**: D2 — MCP server architecture, tool design, .mcp.json config, FastMCP patterns
- **tools**: D2 — tool_choice options, tool descriptions encoding business rules, focused-tool-selection heuristic (few tools per agent; Tool Search / Programmatic Tool Calling is the scaling answer, not a hard cap)
- **cicd**: D3 — -p flag, --output-format json, session isolation, --permission-mode plan
- **extraction**: D4 — forced tool_use, nullable fields, validation-retry, citations (incompatible with Structured Outputs, NOT with tool_use)
- **caching**: D4, D5 — prompt caching (10% hit, 5min/1hr TTL, model-dependent minimum 512–4,096 tokens, 4 breakpoints, prefix order)
- **batch-api**: D4 — 100,000 requests or 256 MB max, 50% discount, 24h window, no SLA/streaming (multi-turn + tool use ARE supported), .jsonl 29 days
- **model-selection**: D5 — Opus/Sonnet/Haiku capabilities, pricing, context windows, extended thinking
- **context-management**: D5 — CLAUDE.md hierarchy, @import, .claude/rules/, context isolation

## Question Format
For each of the 5 questions:

1. Present a **realistic scenario** (3-5 sentences describing an architecture decision)
2. Give **4 options (A-D)** — each should be plausible, not obviously wrong. The real exam is **multiple-choice AND multiple-response**: make at least 1 of the 5 questions a multi-select ("select TWO that apply" — say so explicitly in the question)
3. **Wait for the learner's answer** before revealing the correct one
4. After they answer, explain:
   - Why the correct answer is right (reference specific exam concept)
   - Why EACH wrong answer is wrong (reference specific anti-pattern number if applicable)
   - Which exam domain this tests

## Key Principles
- Focus on **architectural JUDGMENT**, not trivia
- At least 2 questions should test anti-pattern recognition
- At least 1 question should have a "trap" answer that sounds right but violates an anti-pattern
- Reference the technical reference card values from CLAUDE.md when relevant
- If the learner gets something wrong, reference the Notion study guide for deeper review:
  https://www.notion.so/3302367dc5ff8015bd89e00af01a69c3

Present questions ONE AT A TIME. Wait for the answer before moving to the next.
