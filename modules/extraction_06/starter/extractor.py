"""Structured Invoice Extraction — Starter Tier.

CCA-F Exam Domains: D4 Prompt Engineering (~20%), D5 Context Management (~15%)

This exercise teaches forced tool_use extraction with nullable fields.
The key insight: tool_use guarantees STRUCTURE (valid JSON matching schema)
but NOT SEMANTICS (values could still be wrong — validation comes in intermediate tier).

Key concepts tested:
- tool_choice={"type": "tool", "name": "extract_invoice"} forces structured output
- Nullable fields PREVENT fabrication — model returns null instead of guessing
- tool_choice type="tool" is INCOMPATIBLE with extended thinking
- tool_choice type="any" is also INCOMPATIBLE with extended thinking
- ISO 8601 date format for consistency
- confidence_notes (nullable) lets the model flag uncertainty without fabricating
"""

from __future__ import annotations


from typing import Any

import anthropic


# ---------------------------------------------------------------------------
# Invoice Extraction Tool Definition
#
# This tool schema defines the structure of extracted invoice data.
# By forcing the model to use this tool (via tool_choice), we guarantee
# the output matches this schema.
#
# EXAM INSIGHT: Nullable fields are the exam-correct way to handle missing data.
# Without them, the model may fabricate values to fill required fields.
# With them, the model can return null and explain in confidence_notes.
# ---------------------------------------------------------------------------

INVOICE_SCHEMA: dict[str, Any] = {
    "name": "extract_invoice",
    "description": (
        "Extract structured data from an invoice document. "
        "Return null for any field where the data is not clearly present "
        "in the document. Do NOT fabricate or guess values. "
        "Use confidence_notes to flag any uncertainty."
    ),
    "input_schema": {
        "type": "object",
        "required": [
            "vendor_name",
            "invoice_number",
            "date",
            "line_items",
            "subtotal",
            "total",
            "currency",
        ],
        "properties": {
            "vendor_name": {
                "type": "string",
                "description": "Name of the vendor/supplier on the invoice",
            },
            "invoice_number": {
                "type": "string",
                "description": "Invoice number or reference ID",
            },
            "date": {
                "type": "string",
                "description": "Invoice date in ISO 8601 format (YYYY-MM-DD)",
            },
            "line_items": {
                "type": "array",
                "description": "Individual items or services on the invoice",
                "items": {
                    "type": "object",
                    "required": ["description", "quantity", "unit_price", "amount"],
                    "properties": {
                        "description": {
                            "type": "string",
                            "description": "Item or service description",
                        },
                        "quantity": {
                            "type": "number",
                            "description": "Number of units",
                        },
                        "unit_price": {
                            "type": "number",
                            "description": "Price per unit in invoice currency",
                        },
                        "amount": {
                            "type": "number",
                            "description": "Line total (quantity * unit_price)",
                        },
                    },
                },
            },
            "subtotal": {
                "type": "number",
                "description": "Sum of all line item amounts before tax",
            },
            "tax": {
                "type": ["number", "null"],
                "description": (
                    "Tax amount. MUST be null if no tax is shown on the invoice. "
                    "Do NOT assume or calculate a tax amount."
                ),
            },
            "total": {
                "type": "number",
                "description": "Final total amount due",
            },
            "currency": {
                "type": "string",
                "description": "Three-letter currency code (e.g., USD, EUR, GBP)",
            },
            "confidence_notes": {
                "type": ["string", "null"],
                "description": (
                    "Any notes about uncertain extractions or ambiguous data. "
                    "Null if all fields were clearly extractable. "
                    "Example: 'Tax field shows TBD — set to null'"
                ),
            },
        },
    },
}


def extract_invoice(
    document_text: str,
    *,
    model: str = "claude-sonnet-4-6-20250514",
) -> dict[str, Any]:
    """Extract structured invoice data from a document using forced tool_use.

    TODO: Implement this function.

    Steps:
    1. Initialize the Anthropic client
    2. Call client.messages.create() with:
       - model: the specified model
       - max_tokens: 4096 (sufficient for invoice extraction)
       - tools: [INVOICE_SCHEMA]
       - tool_choice: {"type": "tool", "name": "extract_invoice"}
       - messages: [{"role": "user", "content": document_text}]
    3. Extract the tool_use block from the response
    4. Return the tool input (the structured invoice data)

    EXAM INSIGHT: tool_choice forces the model to use extract_invoice.
    This guarantees the response is valid JSON matching our schema.
    However, it does NOT guarantee the VALUES are correct — that requires
    validation (intermediate tier) and citations (advanced tier).

    EXAM INSIGHT: tool_choice type="tool" and type="any" are both
    INCOMPATIBLE with extended thinking. If you need extended thinking,
    use tool_choice="auto" and handle the case where the model doesn't
    use the tool.

    Args:
        document_text: The raw text of the invoice document.
        model: Claude model to use.

    Returns:
        Dict with extracted invoice fields matching INVOICE_SCHEMA.
    """
    # TODO: Implement forced extraction
    raise NotImplementedError("Implement extract_invoice — forced tool_use extraction")


def validate_nullable_fields(extraction: dict[str, Any]) -> list[str]:
    """Check which nullable fields are null (data was missing from document).

    This is a study aid — in practice, null values are expected and correct
    when the source document doesn't contain that data.

    TODO: Implement this function.

    Nullable fields in INVOICE_SCHEMA:
    - tax: null when no tax shown on invoice
    - confidence_notes: null when all fields were clearly extractable

    EXAM INSIGHT: A null value in a nullable field is CORRECT behavior —
    it means the model recognized the data was missing and didn't fabricate.
    A non-null fabricated value would be WORSE than null.

    Args:
        extraction: The extracted invoice data dict.

    Returns:
        List of field names that are null in this extraction.
    """
    # TODO: Implement nullable field validation
    raise NotImplementedError("Implement validate_nullable_fields — check for null fields")


def extract_with_system_context(
    document_text: str,
    document_type: str = "invoice",
    *,
    model: str = "claude-sonnet-4-6-20250514",
) -> dict[str, Any]:
    """Extract with additional system context about the document type.

    TODO: Implement this function.

    Adding a system prompt with context about the expected document type
    improves extraction accuracy. The system prompt should:
    1. Specify the document type (invoice, receipt, PO, etc.)
    2. Define date format expectations (ISO 8601)
    3. Emphasize: return null for missing fields, never fabricate
    4. Specify currency handling rules

    EXAM INSIGHT: System prompts improve extraction but don't GUARANTEE
    correctness. Only validation-retry (intermediate) catches errors.

    Args:
        document_text: The raw text of the invoice document.
        document_type: Type of document being processed.
        model: Claude model to use.

    Returns:
        Dict with extracted invoice fields.
    """
    # TODO: Implement extraction with system context
    raise NotImplementedError(
        "Implement extract_with_system_context — system prompt improves accuracy"
    )
