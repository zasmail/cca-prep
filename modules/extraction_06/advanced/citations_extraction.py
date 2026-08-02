"""Citations + Structured Extraction — Advanced Tier.

CCA-F Exam Domains: D4 Prompt Engineering (~20%), D5 Context Management (~15%)

This exercise teaches how to combine the Citations API with structured extraction.

The critical insight: Citations are COMPATIBLE with tool_use. There is no API-level
block on using `citations.enabled=true` on a document in the same request where you
also force a tool call. The real, documented incompatibility is Citations +
**Structured Outputs** (`output_config.format`, or the deprecated `output_format`):
enabling citations on any document while also setting that parameter returns a
400 error.

So why does this module still use two passes? Not because of an API restriction —
because of a mechanical one: when `tool_choice` forces a specific tool, the API
prefills the assistant turn so the model emits ONLY the tool_use block, with no
natural-language text. Citation markers attach to text content, so a forced-tool
call gives you nowhere for citations to land even though nothing errors. The fix
is ordering, not separation-for-its-own-sake: gather cited evidence FIRST (a
free-text pass where the model can talk and cite), THEN force that evidence into
your schema (a second pass where structure, not attribution, is the goal).

Key concepts tested:
- Citations API provides source attribution for extracted data
- Citations + tool_use (forced tool_choice) are COMPATIBLE — no API error
- Citations + Structured Outputs (`output_config.format`) are INCOMPATIBLE (400 error)
- cited_text is NOT counted as output tokens
- Enable citations on ALL or NONE documents (no selective enabling)
- Anthropic's own evaluations describe citations as "significantly more likely" to
  cite the most relevant quotes than prompt-only approaches — no official percentage
  is published, so don't repeat a specific number as fact
- Two-pass pattern here: Pass 1 (citations, free text) -> Pass 2 (forced tool_use,
  structure) — useful because forced tool_choice suppresses text output, not
  because citations and tool_use can't share a request

EXAM INSIGHT: The exam WILL ask about citations compatibility. The trap is
assuming tool_use is the blocked feature. It isn't — Structured Outputs is.
"""

from __future__ import annotations


import json
from typing import Any

import anthropic

from modules.extraction_06.starter.extractor import INVOICE_SCHEMA


# ---------------------------------------------------------------------------
# Two-Pass Architecture
#
# Pass 1: EXTRACT WITH CITATIONS (free text, tool_choice="auto" or no tools)
#   - Enables citations={"enabled": True} on the source document
#   - Asks the model to state each field's value AND cite the supporting text
#   - Gets VALUE + SOURCE ATTRIBUTION, in prose (not yet schema-shaped)
#
# Pass 2: STRUCTURE (forced tool_use)
#   - Takes Pass 1's cited findings and forces them into INVOICE_SCHEMA
#   - Uses: tool_choice={"type": "tool", "name": "extract_invoice"}
#   - Gets GUARANTEED STRUCTURE — but the assistant turn is tool_use-only,
#     so this pass produces no new citations (there's no room for them)
#
# WHY TWO PASSES?
# - Citations need text output to attach to; forced tool_choice eliminates
#   text output. That's a mechanical conflict, not a documented API error.
# - Doing structure first and citations second would just throw away the
#   citations, so citations has to come first.
# - If you don't need forced-schema guarantees, you can skip Pass 2 entirely
#   and just enable citations alongside tools with tool_choice="auto" —
#   citations + tool_use coexist fine there.
# - The one combination that DOES error is citations + Structured Outputs
#   (`output_config.format`) — see demonstrate_citations_compatibility().
# ---------------------------------------------------------------------------


def pass_1_extract_with_citations(
    document_text: str,
    *,
    model: str = "claude-sonnet-4-6",
) -> dict[str, Any]:
    """Pass 1: Extract field values with source citations (free text, no forced tool).

    TODO: Implement this function.

    This pass does NOT force tool_choice. Citations require the model to produce
    text content with citation markers, so tool_choice must stay "auto" (or be
    omitted) here — a forced tool call would leave no text for citations to
    attach to.

    Steps:
    1. Build a prompt asking the model to state each invoice field's value and
       point to the exact text that supports it (see build_citation_prompt).
    2. Call the API with the document as a citable source:
       messages = [{"role": "user", "content": [
           {
               "type": "document",
               "source": {"type": "text", "media_type": "text/plain", "data": document_text},
               "title": "Invoice Document",
               "citations": {"enabled": True},  # Enable citations on this document
           },
           {"type": "text", "text": citation_prompt},
       ]}]
       Do NOT set tool_choice to a forced tool here.
    3. Parse the response's text + citation blocks into a per-field dict.

    Args:
        document_text: The raw text of the invoice document.
        model: Claude model to use.

    Returns:
        Dict mapping field names to their cited evidence, e.g.:
        {
            "vendor_name": {"value": "Acme Corp", "cited_text": "Acme Corp\\n123 Main St"},
            "tax": {"value": None, "cited_text": None},  # null is correct when absent
            ...
        }
    """
    # TODO: Implement Pass 1 — citations-enabled, text-based extraction
    raise NotImplementedError(
        "Implement pass_1_extract_with_citations — citations-enabled free-text extraction"
    )


def pass_2_structure(
    cited_extraction: dict[str, Any],
    *,
    model: str = "claude-sonnet-4-6",
) -> dict[str, Any]:
    """Pass 2: Force Pass 1's cited findings into the strict INVOICE_SCHEMA.

    TODO: Implement this function.

    This is a forced tool_use call (`tool_choice={"type": "tool", "name": "extract_invoice"}`)
    that turns Pass 1's prose + citations into schema-valid structured data. No
    new citations come out of this pass — the assistant turn is tool_use-only,
    so there's no text for citation markers to attach to. That's expected and
    fine: attribution already happened in Pass 1.

    EXAM INSIGHT: This pass would NOT error if you also set
    `citations={"enabled": True}` on a document here — citations and tool_use
    are compatible. It just wouldn't do anything useful, since forced
    tool_choice suppresses the text output citations need.

    Args:
        cited_extraction: The field -> {value, cited_text} dict from Pass 1.
        model: Claude model to use.

    Returns:
        Dict with extracted invoice fields matching INVOICE_SCHEMA.
    """
    # TODO: Implement Pass 2 — forced tool_use structuring
    raise NotImplementedError("Implement pass_2_structure — forced tool_use structuring")


def build_citation_prompt(document_text: str) -> str:
    """Build a prompt asking the model to state and cite each invoice field.

    TODO: Implement this function.

    The prompt should:
    1. List the invoice fields we need (vendor_name, invoice_number, date,
       line_items, subtotal, tax, total, currency).
    2. Ask the model to state each field's value and quote the exact
       supporting text (citations will attach to this response automatically
       when citations are enabled on the document).
    3. Instruct the model to say a field is absent rather than guessing —
       same nullable-field discipline as the starter tier.

    Args:
        document_text: The raw text of the invoice document (for context only —
            the actual citable source is passed separately as a document block).

    Returns:
        Citation prompt string.
    """
    # TODO: Implement citation prompt builder
    raise NotImplementedError("Implement build_citation_prompt — field-by-field citation prompt")


def two_pass_extract_and_structure(
    document_text: str,
    *,
    model: str = "claude-sonnet-4-6",
) -> dict[str, Any]:
    """Full two-pass pipeline: cited extraction, then forced structuring.

    TODO: Implement the end-to-end two-pass pattern.

    Steps:
    1. Pass 1: Extract with citations (free text) -> cited_extraction
    2. Pass 2: Structure the cited findings (forced tool_use) -> structured data
    3. Merge results: structured data + the citation evidence from Pass 1
    4. Flag any fields Pass 1 could not find supporting text for

    EXAM INSIGHT: This pattern exists because forced tool_choice suppresses
    text output (mechanical reason), not because citations and tool_use are
    documented as incompatible (they aren't). Contrast with Structured Outputs
    (`output_config.format`), which citations genuinely cannot share a request
    with — see demonstrate_citations_compatibility().

    Args:
        document_text: The raw text of the invoice document.
        model: Claude model to use.

    Returns:
        Dict with:
        - "structured": the schema-valid data from Pass 2
        - "citations": the per-field cited evidence from Pass 1
        - "unverified_fields": list of fields with no supporting citation
    """
    # TODO: Implement two-pass pipeline
    raise NotImplementedError(
        "Implement two_pass_extract_and_structure — cited extraction then structuring"
    )


def demonstrate_citations_compatibility() -> str:
    """Document what citations ARE and ARE NOT compatible with.

    This is a study aid — returns an explanation of the real compatibility
    rules, correcting a common exam trap.

    EXAM INSIGHT: This is a direct exam question, and the naive answer
    ("citations are incompatible with tool_use") is WRONG. The correct
    answer:
    - Citations + tool_use: COMPATIBLE. No API error combining them.
    - Citations + Structured Outputs (`output_config.format`): INCOMPATIBLE.
      The API returns a 400 error if you enable citations on any document
      and also set `output_config.format` (or the deprecated `output_format`).

    Returns:
        Explanation string.
    """
    return (
        "Citations API and tool_use are COMPATIBLE in the same API call — "
        "there is no documented restriction, and no 400 error.\n\n"
        "The real incompatibility: Citations and Structured Outputs "
        "(`output_config.format`, or the deprecated `output_format`) CANNOT be "
        "combined. Enabling citations on any document while also setting "
        "`output_config.format` returns a 400 error.\n\n"
        "Why this module still uses two passes: forced tool_choice prefills the "
        "assistant turn so the model emits only a tool_use block, with no "
        "natural-language text for citation markers to attach to. That's a "
        "mechanical limitation of forced tool_choice, not a citations/tool_use "
        "API incompatibility. The fix is ordering: gather cited evidence in a "
        "free-text pass, then force that evidence into schema in a second pass.\n\n"
        "Citation cost note: cited_text is NOT counted as output tokens.\n"
        "Citation recall: Anthropic's evaluations describe citations as "
        "'significantly more likely' to cite the most relevant quotes than "
        "prompt-only approaches — no official percentage is published, so "
        "don't cite one.\n"
        "Citation scope: must enable on ALL or NONE documents."
    )
