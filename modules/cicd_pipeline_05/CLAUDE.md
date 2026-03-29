# Module 05: CI/CD Pipeline Integration

## Exam Coverage
- **Primary Domains**: D3 Claude Code Configuration (~20%), D4 Prompt Engineering (~20%)
- **Combined weight**: ~40% of exam touches these domains

## Learning Objectives
1. Use `claude -p` for non-interactive (headless) pipeline execution
2. Enforce session isolation between generation and review (AP9)
3. Apply `--output-format json` with `--json-schema` for structured pipeline output
4. Configure resource limits: `--max-turns`, `--max-budget-usd`
5. Restrict tool access with `--allowedTools` for least-privilege execution
6. Use the Batch API for cost-efficient bulk operations (50% cheaper, 24h window)

## Key Patterns
- **Non-interactive mode**: `claude -p "prompt"` runs without human interaction — required for CI/CD
- **Session isolation**: Separate `--session-id` for generation vs review prevents confirmation bias
- **Structured output**: `--json-schema` forces output into a validated schema
- **Permission mode**: `--permission-mode plan` restricts to read-only tools (review sessions)
- **Batch API**: 50% cheaper for non-urgent bulk operations, 24h processing window

## Anti-Patterns Tested
- AP9: Same-session self-review (generation and review in ONE session = confirmation bias)
- Running `claude` interactively in CI/CD (requires `-p` flag)
- No resource limits in pipelines (runaway costs without `--max-budget-usd`)
- Allowing write tools in review sessions (review should be read-only)

## Progression
- **Starter**: Code review pipeline with `claude -p` and structured JSON output
- **Intermediate**: Two-session gen-then-review with session isolation
- **Advanced**: Batch API for bulk file review at 50% cost reduction
