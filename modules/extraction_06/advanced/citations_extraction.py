"""Two-Pass Citations Extraction — Advanced Tier.

CCA-F Exam Domains: D4 Prompt Engineering (~20%), D5 Context Management (~15%)

This exercise teaches the two-pass extraction + verification pattern.
The critical insight: Citations API is INCOMPATIBLE with tool_use.
You MUST use separate passes — one for structure, one for attribution.

Key concepts tested:
- Citations API provides source attribution for extracted data
- Citations are INCOMPATIBLE with tool_use — separate passes required
- Citations are INCOMPATIBLE with Structured Outputs (JSON mode)
- cited_text is NOT counted as output tokens
- Enable citations on ALL or NONE documents (no selective enabling)
- ~15% better recall when citations are enabled
- Two-pass: Pass 1 (tool_use) for structure, Pass 2 (citations) for verification

EXAM INSIGHT: The exam WILL ask about citations + tool_use compatibility.
The answer is ALWAYS "incompatible — use separate passes."
"""

from __future__ import annotations


import json
from typing import Any

import anthropic

from modules.extraction_06.starter.extractor import INVOICE_SCHEMA


# ---------------------------------------------------------------------------
# Two-Pass Architecture
#
# Pass 1: EXTRACTION (tool_use)
#   - Forces structured output via tool_choice
#   - Gets the DATA but not the SOURCE ATTRIBUTION
#   - Uses: tool_choice={"type": "tool", "name": "extract_invoice"}
#
# Pass 2: VERIFICATION (citations)
#   - Verifies each extracted field against the source document
#   - Gets SOURCE ATTRIBUTION for each field
#   - Uses: citations={"enabled": True} on the document
#   - CANNOT use tool_use in this pass
#
# WHY TWO PASSES?
# - tool_use gives us guaranteed structure (valid JSON matching schema)
# - Citations give us guaranteed attribution (which text backs each field)
# - They're incompatible in the same API call
# - The two passes together give us structure + trust
# ---------------------------------------------------------------------------


def pass_1_extract(
    document_text: str,
    *,
    model: str = "claude-sonnet-4-6-20250514",
) -> dict[str, Any]:
    """Pass 1: Extract structured data using forced tool_use.

    TODO: Implement this function.

    This is identical to the starter tier extraction — forced tool_use
    for guaranteed structured output. The key difference is that this
    extraction will be VERIFIED by Pass 2.

    Steps:
    1. Call API with tool_choice forced to extract_invoice
    2. Extract the tool_use block from response
    3. Return the structured data

    Args:
        document_text: The raw text of the invoice document.
        model: Claude model to use.

    Returns:
        Dict with extracted invoice fields.
    """
    # TODO: Implement Pass 1 extraction (same as starter tier)
    raise NotImplementedError("Implement pass_1_extract — forced tool_use extraction")


def pass_2_verify_with_citations(
    document_text: str,
    extraction: dict[str, Any],
    *,
    model: str = "claude-sonnet-4-6-20250514",
) -> dict[str, Any]:
    """Pass 2: Verify extracted fields using the Citations API.

    TODO: Implement this function.

    This pass asks the model to verify each extracted field and cite
    the specific text in the document that supports each value.

    Steps:
    1. Build a verification prompt that lists each extracted field
    2. Include the document as a citable source:
       messages = [{"role": "user", "content": [
           {
               "type": "document",
               "source": {"type": "text", "media_type": "text/plain", "data": document_text},
               "title": "Invoice Document",
               "citations": {"enabled": True},  # Enable citations on this document
           },
           {
               "type": "text",
               "text": verification_prompt,
           },
       ]}]
    3. Parse the response for citation blocks
    4. Map citations back to extracted fields

    EXAM INSIGHT: Citations must be enabled on ALL or NONE documents.
    You cannot selectively enable citations on some documents.

    EXAM INSIGHT: cited_text is NOT counted as output tokens — it's
    "free" from a cost perspective.

    EXAM INSIGHT: Citations give ~15% better recall when enabled.

    CRITICAL: Do NOT use tool_choice in this pass. Citations are
    INCOMPATIBLE with tool_use. Use a text-based verification prompt instead.

    Args:
        document_text: The original invoice document text.
        extraction: The structured extraction from Pass 1.
        model: Claude model to use.

    Returns:
        Dict mapping field names to their citation evidence:
        {
            "vendor_name": {"value": "Acme Corp", "cited_text": "Acme Corp\n123 Main St", "verified": True},
            "tax": {"value": None, "cited_text": None, "verified": True},  # null is correct
            ...
        }
    """
    # TODO: Implement Pass 2 citation verification
    raise NotImplementedError(
        "Implement pass_2_verify_with_citations — citations API for attribution"
    )


def build_verification_prompt(extraction: dict[str, Any]) -> str:
    """Build a prompt asking the model to verify each extracted field.

    TODO: Implement this function.

    The prompt should:
    1. List each field and its extracted value
    2. Ask the model to cite the specific text supporting each value
    3. Ask the model to flag any fields that cannot be verified
    4. Handle nullable fields: null values should be verified as
       "no evidence of this field in the document" (which is correct)

    Args:
        extraction: The structured extraction from Pass 1.

    Returns:
        Verification prompt string.
    """
    # TODO: Implement verification prompt builder
    raise NotImplementedError("Implement build_verification_prompt — field-by-field verification")


def two_pass_extract_and_verify(
    document_text: str,
    *,
    model: str = "claude-sonnet-4-6-20250514",
) -> dict[str, Any]:
    """Full two-pass extraction + verification pipeline.

    TODO: Implement the end-to-end two-pass pattern.

    Steps:
    1. Pass 1: Extract structured data (tool_use)
    2. Pass 2: Verify with citations (citations API)
    3. Merge results: extraction + citation evidence
    4. Flag any unverified fields

    EXAM INSIGHT: This pattern gives you BOTH structure guarantees
    (from tool_use) AND source attribution (from citations).
    Neither pass alone provides both.

    Args:
        document_text: The raw text of the invoice document.
        model: Claude model to use.

    Returns:
        Dict with:
        - "extraction": the structured data from Pass 1
        - "verification": citation evidence from Pass 2
        - "unverified_fields": list of fields that couldn't be verified
        - "confidence": overall confidence based on verification coverage
    """
    # TODO: Implement two-pass pipeline
    raise NotImplementedError(
        "Implement two_pass_extract_and_verify — complete two-pass pattern"
    )


def demonstrate_incompatibility() -> str:
    """Document WHY citations and tool_use are incompatible.

    This is a study aid — returns explanation of the incompatibility.

    EXAM INSIGHT: This is a direct exam question. The answer:
    - tool_use forces the model to output a tool_use content block
    - Citations require the model to output text with citation markers
    - These are mutually exclusive output modes
    - Solution: use two separate API calls (passes)

    Also incompatible with citations:
    - Structured Outputs (JSON mode) — same reason (forced output format)

    Returns:
        Explanation string.
    """
    return (
        "Citations API and tool_use are INCOMPATIBLE in the same API call.\n\n"
        "Reason: tool_use forces the model to output a tool_use content block "
        "(structured JSON). Citations require the model to output text content "
        "with citation markers referencing source documents. These are mutually "
        "exclusive output modes — the model can't do both simultaneously.\n\n"
        "Solution: Use two separate API calls (passes):\n"
        "  Pass 1: tool_use with tool_choice for structured extraction\n"
        "  Pass 2: citations API for source attribution and verification\n\n"
        "Also incompatible with citations:\n"
        "  - Structured Outputs (JSON mode) — also forces output format\n\n"
        "Citation cost note: cited_text is NOT counted as output tokens.\n"
        "Citation recall: ~15% better recall when enabled.\n"
        "Citation scope: must enable on ALL or NONE documents."
    )
