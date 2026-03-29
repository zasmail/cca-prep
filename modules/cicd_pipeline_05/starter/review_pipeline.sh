#!/usr/bin/env bash
# ---------------------------------------------------------------------------
# Code Review Pipeline — Starter Tier
#
# CCA-F Exam Domains: D3 Claude Code Configuration (~20%), D4 Prompt Engineering (~20%)
#
# This script runs Claude in NON-INTERACTIVE mode (-p flag) to review code
# and produce structured JSON output conforming to a review schema.
#
# Key concepts tested:
# - `claude -p` is REQUIRED for CI/CD — interactive mode blocks pipelines
# - `--output-format json` makes output machine-parseable
# - `--json-schema` enforces output structure (review format)
# - `--max-turns` limits tool call rounds (resource control)
# - `--max-budget-usd` caps API spend per invocation
# - `--allowedTools` restricts to read-only tools (least privilege)
# ---------------------------------------------------------------------------

set -euo pipefail

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

# TODO: Set the target path from command-line argument or default
TARGET_PATH="${1:-.}"

# TODO: Define the JSON schema for structured review output.
#
# EXAM INSIGHT: --json-schema forces Claude to return output matching this
# schema. This is different from tool_use forced extraction — json-schema
# works with `claude -p` in CLI mode, while tool_choice works with the API.
#
# Schema fields:
#   summary (string)      — Brief overall assessment
#   issues (array)        — List of issues found
#     file (string)       — File path where issue was found
#     line (integer)      — Line number (approximate)
#     severity (string)   — "critical" | "warning" | "info"
#     description (string)— What the issue is
#     suggestion (string) — How to fix it
#   approved (boolean)    — Whether the code passes review

REVIEW_SCHEMA='{
  "type": "object",
  "required": ["summary", "issues", "approved"],
  "properties": {
    "summary": {
      "type": "string",
      "description": "Brief overall assessment of the code quality"
    },
    "issues": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["file", "line", "severity", "description", "suggestion"],
        "properties": {
          "file": {
            "type": "string",
            "description": "File path where the issue was found"
          },
          "line": {
            "type": "integer",
            "description": "Approximate line number"
          },
          "severity": {
            "type": "string",
            "enum": ["critical", "warning", "info"],
            "description": "Issue severity level"
          },
          "description": {
            "type": "string",
            "description": "Description of the issue"
          },
          "suggestion": {
            "type": "string",
            "description": "Suggested fix or improvement"
          }
        }
      }
    },
    "approved": {
      "type": "boolean",
      "description": "Whether the code passes review (no critical issues)"
    }
  }
}'

# ---------------------------------------------------------------------------
# Review Prompt
# ---------------------------------------------------------------------------

# TODO: Craft the review prompt.
#
# EXAM INSIGHT: The prompt should be specific about what to review.
# Generic prompts like "review this code" produce vague results.
# Include: what to check, severity criteria, when to approve vs reject.

REVIEW_PROMPT="Review the code in ${TARGET_PATH} for:
1. Security vulnerabilities (critical: hardcoded secrets, SQL injection, XSS)
2. Error handling gaps (warning: missing try/catch, unhandled promises)
3. Code quality issues (info: naming, complexity, missing types)

Mark as approved=true ONLY if there are zero critical issues.
For each issue found, identify the specific file, line, severity, and suggestion."

# ---------------------------------------------------------------------------
# Execute Review
# ---------------------------------------------------------------------------

# TODO: Run claude -p with all required flags.
#
# Flag breakdown:
#   -p                    — Non-interactive mode (REQUIRED for CI/CD)
#   --output-format json  — Machine-readable JSON output
#   --json-schema         — Enforce output structure
#   --max-turns 5         — Limit tool call rounds (prevent runaway)
#   --max-budget-usd 1.00 — Cap API spend per invocation
#   --allowedTools        — Restrict to read-only tools (least privilege)
#
# EXAM INSIGHT: --allowedTools is how you enforce least privilege in pipelines.
# A review session should NEVER have Write, Edit, or Bash tools.

echo "Running code review on: ${TARGET_PATH}"
echo "---"

# TODO: Uncomment and complete this command once claude CLI is available
# claude -p "${REVIEW_PROMPT}" \
#   --output-format json \
#   --json-schema "${REVIEW_SCHEMA}" \
#   --max-turns 5 \
#   --max-budget-usd 1.00 \
#   --allowedTools "Read" "Grep" "Glob"

# TODO: Capture the exit code and output
# REVIEW_RESULT=$?
# if [ $REVIEW_RESULT -ne 0 ]; then
#     echo "ERROR: Review pipeline failed with exit code ${REVIEW_RESULT}"
#     exit 1
# fi

# TODO: Parse the JSON output to determine pass/fail
# APPROVED=$(echo "${OUTPUT}" | jq -r '.approved')
# if [ "${APPROVED}" = "true" ]; then
#     echo "PASS: Code review approved"
#     exit 0
# else
#     echo "FAIL: Code review found issues"
#     echo "${OUTPUT}" | jq '.issues[] | select(.severity == "critical")'
#     exit 1
# fi

echo "TODO: Pipeline not yet connected to claude CLI"
echo "Review schema and flags are defined — implement the execution block above."
