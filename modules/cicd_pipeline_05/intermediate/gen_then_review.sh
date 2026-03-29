#!/usr/bin/env bash
# ---------------------------------------------------------------------------
# Generate-Then-Review Pipeline — Intermediate Tier
#
# CCA-F Exam Domains: D3 Claude Code Configuration (~20%), D4 Prompt Engineering (~20%)
#
# This script demonstrates the CRITICAL exam pattern: session isolation (AP9).
# Generation and review MUST use SEPARATE sessions to prevent confirmation bias.
#
# Key concepts tested:
# - AP9: Same-session self-review is an anti-pattern (confirmation bias)
# - Separate --session-id values ensure independent context
# - Generation session: write-capable tools (Write, Edit, Bash)
# - Review session: read-only tools (Read, Grep, Glob) + --permission-mode plan
# - Each session gets a unique UUID via $(uuidgen)
#
# WHY SEPARATE SESSIONS?
# When Claude reviews its own output in the SAME session, it has access to
# its own reasoning for why it made those choices. This creates confirmation
# bias — it's predisposed to approve its own work. A separate session starts
# fresh with no memory of the generation rationale.
# ---------------------------------------------------------------------------

set -euo pipefail

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

# TODO: Define the task for generation
GENERATION_TASK="Create a Python function that validates credit card numbers using the Luhn algorithm. Include type hints, docstring, and handle edge cases (empty string, non-numeric, wrong length)."

# TODO: Set the output directory for generated code
OUTPUT_DIR="${1:-./generated}"
mkdir -p "${OUTPUT_DIR}"

# ---------------------------------------------------------------------------
# Session A: GENERATION
#
# This session has WRITE capabilities — it creates new code.
# Uses a unique session ID so its context is isolated.
#
# Tools allowed: Write, Edit, Bash (for running tests)
# ---------------------------------------------------------------------------

# TODO: Generate a unique session ID for the generation session
# EXAM INSIGHT: Each session MUST have its own unique ID.
# Using the same ID for gen and review defeats the purpose of isolation.
GEN_SESSION_ID="$(uuidgen)"

echo "=== SESSION A: GENERATION ==="
echo "Session ID: ${GEN_SESSION_ID}"
echo "Task: ${GENERATION_TASK}"
echo "---"

# TODO: Uncomment and complete this command once claude CLI is available
# claude -p "${GENERATION_TASK}

# Write the implementation to ${OUTPUT_DIR}/luhn_validator.py
# Write tests to ${OUTPUT_DIR}/test_luhn_validator.py
# Run the tests with pytest to verify they pass." \
#   --session-id "${GEN_SESSION_ID}" \
#   --output-format json \
#   --max-turns 10 \
#   --max-budget-usd 2.00 \
#   --allowedTools "Write" "Edit" "Bash"

echo "Generation session complete."
echo ""

# ---------------------------------------------------------------------------
# Session B: REVIEW
#
# This session is READ-ONLY — it reviews what Session A produced.
# Uses a DIFFERENT session ID so it has NO memory of generation rationale.
#
# Tools allowed: Read, Grep, Glob (read-only)
# Permission mode: plan (restricts to read-only operations)
#
# EXAM INSIGHT: --permission-mode plan ensures the review session
# CANNOT modify the code it's reviewing. This is defense-in-depth:
# both --allowedTools AND --permission-mode restrict access.
# ---------------------------------------------------------------------------

# TODO: Generate a SEPARATE unique session ID for the review session
# CRITICAL: This MUST be different from GEN_SESSION_ID
REVIEW_SESSION_ID="$(uuidgen)"

echo "=== SESSION B: REVIEW ==="
echo "Session ID: ${REVIEW_SESSION_ID}"
echo "Reviewing output from Session A..."
echo "---"

# TODO: Define the review schema (same structure as starter tier)
REVIEW_SCHEMA='{
  "type": "object",
  "required": ["summary", "issues", "approved"],
  "properties": {
    "summary": { "type": "string" },
    "issues": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["file", "line", "severity", "description", "suggestion"],
        "properties": {
          "file": { "type": "string" },
          "line": { "type": "integer" },
          "severity": { "type": "string", "enum": ["critical", "warning", "info"] },
          "description": { "type": "string" },
          "suggestion": { "type": "string" }
        }
      }
    },
    "approved": { "type": "boolean" }
  }
}'

# TODO: Uncomment and complete this command once claude CLI is available
# claude -p "Review the code in ${OUTPUT_DIR}/ for:
# 1. Correctness: Does the Luhn algorithm implementation handle all edge cases?
# 2. Security: Any input validation gaps?
# 3. Quality: Type hints, docstrings, test coverage?
#
# You are reviewing code written by a DIFFERENT session. Approach with fresh eyes.
# Mark approved=true only if there are zero critical issues." \
#   --session-id "${REVIEW_SESSION_ID}" \
#   --output-format json \
#   --json-schema "${REVIEW_SCHEMA}" \
#   --max-turns 5 \
#   --max-budget-usd 1.00 \
#   --allowedTools "Read" "Grep" "Glob" \
#   --permission-mode plan

echo "Review session complete."
echo ""

# ---------------------------------------------------------------------------
# Verify Session Isolation
# ---------------------------------------------------------------------------

# TODO: Confirm the two sessions used different IDs
echo "=== SESSION ISOLATION CHECK ==="
echo "Generation Session: ${GEN_SESSION_ID}"
echo "Review Session:     ${REVIEW_SESSION_ID}"

if [ "${GEN_SESSION_ID}" = "${REVIEW_SESSION_ID}" ]; then
    echo "ERROR: Sessions used the SAME ID — AP9 violated!"
    echo "Generation and review MUST use separate sessions."
    exit 1
else
    echo "OK: Sessions are properly isolated (different IDs)."
fi

echo ""
echo "TODO: Pipeline not yet connected to claude CLI."
echo "Session isolation pattern and flags are defined — implement the execution blocks above."
