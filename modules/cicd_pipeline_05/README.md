# Module 05: CI/CD Pipeline Integration

## Overview
This module teaches how to integrate Claude into CI/CD pipelines — a key exam topic
covering non-interactive execution, session isolation, and batch processing.
The critical insight: generation and review MUST use separate sessions (AP9).

## Domains Covered
| Domain | Weight | Focus |
|--------|--------|-------|
| D3 Claude Code Configuration | ~20% | Non-interactive mode, flags, permissions |
| D4 Prompt Engineering | ~20% | Structured output schemas, review prompts |

## Tier Breakdown

### Starter: Code Review Pipeline
**File**: `starter/review_pipeline.sh`

A single-session review pipeline using:
- `claude -p` for non-interactive execution
- `--output-format json` for machine-readable output
- `--json-schema` to enforce review structure
- `--max-turns 5` and `--max-budget-usd 1.00` for resource limits
- `--allowedTools` to restrict to read-only tools

### Intermediate: Generate-Then-Review
**File**: `intermediate/gen_then_review.sh`

Two SEPARATE sessions demonstrating AP9 compliance:
- Session A (generation): Write/Edit/Bash tools, generates code
- Session B (review): Read/Grep/Glob tools only, reviews Session A output
- Key: Different `--session-id` values prevent confirmation bias

### Advanced: Batch Review
**File**: `advanced/batch_review.py`

Bulk file review using the Anthropic Batch API:
- 50% cheaper than real-time API calls
- 24-hour processing window (no SLA)
- No streaming, no multi-turn tool calling
- Results as .jsonl, available for 29 days

## Running
```bash
# Starter — run the review pipeline
chmod +x modules/cicd_pipeline_05/starter/review_pipeline.sh
./modules/cicd_pipeline_05/starter/review_pipeline.sh path/to/code

# Intermediate — run gen-then-review
chmod +x modules/cicd_pipeline_05/intermediate/gen_then_review.sh
./modules/cicd_pipeline_05/intermediate/gen_then_review.sh

# Advanced — run batch review
uv run python modules/cicd_pipeline_05/advanced/batch_review.py
```

## Running Tests
```bash
uv run pytest modules/cicd_pipeline_05/ -v
```

## Key Exam Insights
- `claude -p` is REQUIRED for CI/CD — interactive mode blocks pipelines
- Session isolation (AP9) is one of the most commonly tested anti-patterns
- `--permission-mode plan` makes a session read-only (no writes, no executions)
- Batch API has NO SLA and NO streaming — only use for non-urgent work
- `--json-schema` gives you structured output without tool_use tricks
