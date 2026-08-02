"""Validation-Retry Extraction — Intermediate Tier.

CCA-F Exam Domains: D4 Prompt Engineering (~20%), D5 Context Management (~15%)

This exercise teaches the extract-validate-retry pattern.
The key insight: tool_use guarantees STRUCTURE but not SEMANTICS.
Validation catches semantic errors; retry with SPECIFIC feedback fixes them.

Key concepts tested:
- Extract -> validate -> if errors, send tool_result with is_error=True
- Error messages MUST be SPECIFIC: "subtotal $150 but items sum to $130"
- NEVER generic "try again" or "please fix the errors" (AP6)
- Retry uses the SAME conversation (append tool_result, not new conversation)
- max_retries prevents infinite loops (safety net, like max_iterations in agentic loops)
"""

from __future__ import annotations


import json
from typing import Any

import anthropic

from modules.extraction_06.starter.extractor import INVOICE_SCHEMA


# ---------------------------------------------------------------------------
# Validation Rules
#
# These rules check SEMANTIC correctness — things tool_use schema can't enforce.
# Schema enforces structure (types, required fields).
# Validation enforces meaning (totals match, dates are valid, etc.).
# ---------------------------------------------------------------------------

def validate_extraction(extraction: dict[str, Any]) -> list[str]:
    """Validate extracted invoice data for semantic correctness.

    TODO: Implement these validation rules.

    Rules to check:
    1. Line item amounts: each item's amount should equal quantity * unit_price
    2. Subtotal: should equal sum of all line item amounts
    3. Total: should equal subtotal + tax (or subtotal if tax is null)
    4. Date format: must be valid ISO 8601 (YYYY-MM-DD)
    5. Currency: must be a valid 3-letter code
    6. Line items: must have at least one item

    EXAM INSIGHT: Each error message must be SPECIFIC with actual values.
    AP6: Generic error messages like "totals don't match" are an anti-pattern.
    Correct: "subtotal is $150 but line items sum to $130 (Widget: $100, Service: $30)"

    Args:
        extraction: The extracted invoice data dict.

    Returns:
        List of specific error messages. Empty list means validation passed.
    """
    errors: list[str] = []

    # TODO: Rule 1 — Validate each line item amount = quantity * unit_price
    # Example error: "Line item 'Widget' amount is $150 but quantity(2) * unit_price($100) = $200"

    # TODO: Rule 2 — Validate subtotal = sum of line item amounts
    # Example error: "subtotal is $150 but line items sum to $130 (Widget: $100, Service: $30)"

    # TODO: Rule 3 — Validate total = subtotal + tax
    # Example error: "total is $165 but subtotal($150) + tax($10) = $160"

    # TODO: Rule 4 — Validate ISO 8601 date format
    # Example error: "date '01/15/2026' is not ISO 8601 format (expected YYYY-MM-DD)"

    # TODO: Rule 5 — Validate currency is 3 uppercase letters
    # Example error: "currency 'dollars' is not a valid 3-letter code (expected e.g., USD)"

    # TODO: Rule 6 — Validate at least one line item
    # Example error: "line_items is empty — invoice must have at least one item"

    raise NotImplementedError("Implement validate_extraction — semantic validation rules")


def format_error_feedback(errors: list[str]) -> str:
    """Format validation errors as SPECIFIC feedback for retry.

    TODO: Implement this function.

    The error feedback is sent back as a tool_result with is_error=True.
    It must be specific enough for the model to correct the exact issue.

    AP6 VIOLATION (WRONG):
        "There are errors in your extraction. Please try again."

    CORRECT:
        "Validation failed with 2 errors:
        1. subtotal is $150 but line items sum to $130 (Widget: $100, Service: $30)
        2. date '01/15/2026' is not ISO 8601 format (expected YYYY-MM-DD)

        Please re-extract with corrected values."

    Args:
        errors: List of specific error messages from validate_extraction().

    Returns:
        Formatted error string to send as tool_result content.
    """
    # TODO: Implement specific error formatting
    raise NotImplementedError("Implement format_error_feedback — AP6-compliant error messages")


def extract_with_validation(
    document_text: str,
    *,
    max_retries: int = 3,
    model: str = "claude-sonnet-4-6",
) -> dict[str, Any]:
    """Extract invoice data with validation-retry loop.

    TODO: Implement the full extract-validate-retry pattern.

    Algorithm:
    1. Initialize conversation with the document
    2. Call extract (forced tool_use) to get initial extraction
    3. Validate the extraction with validate_extraction()
    4. If validation passes (no errors), return the extraction
    5. If validation fails:
       a. Build a tool_result with is_error=True and SPECIFIC error feedback
       b. Append the assistant message (with tool_use) to conversation
       c. Append the error tool_result as a user message
       d. Call the API again — model sees the errors and retries
    6. Repeat up to max_retries times
    7. If max_retries exceeded, return last extraction with errors noted

    Message structure for retry:
    ```
    messages = [
        {"role": "user", "content": document_text},
        {"role": "assistant", "content": [tool_use_block]},  # Model's extraction
        {"role": "user", "content": [{                        # Our error feedback
            "type": "tool_result",
            "tool_use_id": tool_use_block.id,
            "content": format_error_feedback(errors),
            "is_error": True,                                 # CRITICAL: marks as error
        }]},
    ]
    ```

    EXAM INSIGHT: is_error=True in the tool_result tells the model its
    previous extraction had problems. Combined with specific error messages,
    this gives the model enough information to correct the exact issues.

    EXAM INSIGHT: The retry happens in the SAME conversation — we append
    to the existing messages list. Starting a new conversation would lose
    the context of what went wrong.

    Args:
        document_text: The raw text of the invoice document.
        max_retries: Maximum number of validation-retry attempts.
        model: Claude model to use.

    Returns:
        Dict with the validated extraction, plus a "_validation" key
        containing {"passed": bool, "attempts": int, "errors": list}.
    """
    # TODO: Implement the validation-retry loop
    raise NotImplementedError(
        "Implement extract_with_validation — the extract-validate-retry pattern"
    )


def track_per_field_accuracy(
    extractions: list[dict[str, Any]],
    ground_truth: list[dict[str, Any]],
) -> dict[str, float]:
    """Track extraction accuracy per field, not just aggregate.

    TODO: Implement per-field accuracy tracking.

    AP10: Aggregate accuracy metrics only is an anti-pattern.
    You MUST track per-document-type AND per-field metrics.

    Example output:
    {
        "vendor_name": 0.95,      # 95% correct across all extractions
        "invoice_number": 0.90,
        "date": 0.85,             # Dates are harder — track separately
        "subtotal": 0.92,
        "tax": 0.70,              # Tax often missing — lower accuracy expected
        "total": 0.93,
        "line_items_count": 0.88, # Number of items correctly identified
    }

    EXAM INSIGHT: If you only report aggregate accuracy (e.g., "92% overall"),
    you miss that tax extraction is only 70% accurate. Per-field metrics
    reveal which fields need improvement.

    Args:
        extractions: List of extracted invoice dicts.
        ground_truth: List of ground truth invoice dicts (same order).

    Returns:
        Dict mapping field names to accuracy scores (0.0 to 1.0).
    """
    # TODO: Implement per-field accuracy tracking (AP10 compliance)
    raise NotImplementedError(
        "Implement track_per_field_accuracy — AP10 requires per-field metrics"
    )
