# Module 01: Customer Support Agent

## Exam Coverage
- **Primary Domain**: D1 Agentic Architecture (~27% of exam)
- **This is the highest-value module** — master this first

## Learning Objectives
1. Implement the agentic loop lifecycle (the #1 exam pattern)
2. Use `stop_reason` for loop control (NOT text parsing — anti-pattern #1)
3. Format tool_result content blocks correctly (role="user", tool_use_id matching)
4. Build compliance hooks with PreToolUse/PostToolUse (programmatic enforcement)
5. Implement the 3 valid escalation triggers (customer_request, policy_gap, capability_limit)
6. Structure error responses with isError + errorCategory + isRetryable

## Key Patterns
- **Agentic loop**: send message → check stop_reason → if "tool_use", execute tool → append result → loop
- **Tool result format**: `{"type": "tool_result", "tool_use_id": "<id>", "content": "<json>"}`
- **Hook enforcement**: PreToolUse blocks unauthorized tool calls BEFORE they execute
- **max_iterations**: Safety net ONLY — never the primary loop termination condition

## Anti-Patterns Tested
- AP1: Text parsing for loop termination
- AP2: Iteration caps as primary control
- AP3: Prompt enforcement instead of hooks
- AP4: Confidence-based escalation
- AP5: Sentiment-based escalation
- AP6: Generic error responses
- AP7: Silent error suppression

## Progression
- **Starter**: Raw Messages API agentic loop — learn the core lifecycle
- **Intermediate**: Agent SDK with hooks — learn programmatic enforcement
- **Advanced**: Production-grade with case-fact extraction and structured errors
