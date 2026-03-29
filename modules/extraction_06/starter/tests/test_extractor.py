"""Tests for Module 06 Starter — Invoice Extraction.

These tests validate forced tool_use extraction patterns,
nullable field handling, and schema correctness.
"""

import pytest


class TestInvoiceSchema:
    """INVOICE_SCHEMA must define correct extraction structure."""

    def test_schema_has_required_fields(self) -> None:
        """Schema must require all non-nullable invoice fields."""
        from modules.extraction_06.starter.extractor import INVOICE_SCHEMA

        schema = INVOICE_SCHEMA["input_schema"]
        required = set(schema["required"])
        expected_required = {
            "vendor_name",
            "invoice_number",
            "date",
            "line_items",
            "subtotal",
            "total",
            "currency",
        }

        assert expected_required == required, (
            f"Required fields mismatch. Expected: {expected_required}, Got: {required}. "
            "All non-nullable fields must be required."
        )

    def test_tax_field_is_nullable(self) -> None:
        """Tax must be nullable — prevents fabrication when no tax on invoice.

        EXAM INSIGHT: Nullable fields are the exam-correct way to handle
        missing data. Without nullable, the model may fabricate a tax amount.
        """
        from modules.extraction_06.starter.extractor import INVOICE_SCHEMA

        properties = INVOICE_SCHEMA["input_schema"]["properties"]
        tax_type = properties["tax"]["type"]

        # Nullable can be expressed as ["number", "null"] or {"anyOf": [...]}
        if isinstance(tax_type, list):
            assert "null" in tax_type, "tax field must allow null type"
        else:
            pytest.fail("tax field must be nullable (type should include 'null')")

    def test_confidence_notes_is_nullable(self) -> None:
        """confidence_notes must be nullable — null when extraction is clear."""
        from modules.extraction_06.starter.extractor import INVOICE_SCHEMA

        properties = INVOICE_SCHEMA["input_schema"]["properties"]
        notes_type = properties["confidence_notes"]["type"]

        if isinstance(notes_type, list):
            assert "null" in notes_type, "confidence_notes must allow null type"
        else:
            pytest.fail("confidence_notes must be nullable")

    def test_tax_is_not_required(self) -> None:
        """Tax must NOT be in the required list — it's nullable."""
        from modules.extraction_06.starter.extractor import INVOICE_SCHEMA

        required = INVOICE_SCHEMA["input_schema"]["required"]

        assert "tax" not in required, (
            "tax must NOT be required — it's nullable because not all invoices have tax"
        )

    def test_confidence_notes_is_not_required(self) -> None:
        """confidence_notes must NOT be in the required list."""
        from modules.extraction_06.starter.extractor import INVOICE_SCHEMA

        required = INVOICE_SCHEMA["input_schema"]["required"]

        assert "confidence_notes" not in required, (
            "confidence_notes must NOT be required — it's nullable"
        )

    def test_line_items_has_item_structure(self) -> None:
        """Line items must define per-item structure with required fields."""
        from modules.extraction_06.starter.extractor import INVOICE_SCHEMA

        line_items = INVOICE_SCHEMA["input_schema"]["properties"]["line_items"]
        assert line_items["type"] == "array", "line_items must be an array"

        item_schema = line_items["items"]
        required_item_fields = {"description", "quantity", "unit_price", "amount"}
        actual_item_fields = set(item_schema.get("properties", {}).keys())
        assert required_item_fields.issubset(actual_item_fields), (
            f"Line item missing fields: {required_item_fields - actual_item_fields}"
        )

    def test_date_field_describes_iso_format(self) -> None:
        """Date field description must specify ISO 8601 format."""
        from modules.extraction_06.starter.extractor import INVOICE_SCHEMA

        date_desc = INVOICE_SCHEMA["input_schema"]["properties"]["date"]["description"]

        assert "ISO 8601" in date_desc or "YYYY-MM-DD" in date_desc, (
            "Date field must specify ISO 8601 format in its description"
        )


class TestToolChoicePattern:
    """extract_invoice must use forced tool_choice for guaranteed structure."""

    def test_schema_defines_tool_name(self) -> None:
        """The schema must have a name field for tool_choice targeting."""
        from modules.extraction_06.starter.extractor import INVOICE_SCHEMA

        assert INVOICE_SCHEMA["name"] == "extract_invoice", (
            "Schema name must be 'extract_invoice' to match tool_choice target"
        )

    def test_extract_function_exists(self) -> None:
        """extract_invoice function must exist and accept document_text."""
        from modules.extraction_06.starter.extractor import extract_invoice

        import inspect
        sig = inspect.signature(extract_invoice)
        assert "document_text" in sig.parameters, (
            "extract_invoice must accept document_text parameter"
        )

    def test_schema_description_prevents_fabrication(self) -> None:
        """Tool description must instruct model NOT to fabricate values."""
        from modules.extraction_06.starter.extractor import INVOICE_SCHEMA

        desc = INVOICE_SCHEMA["description"].lower()

        assert "null" in desc or "fabricat" in desc or "guess" in desc, (
            "Tool description must instruct the model to return null for missing data, "
            "not fabricate values. This is the exam-correct pattern."
        )


class TestNullableFieldValidation:
    """validate_nullable_fields must identify null fields in extractions."""

    def test_identifies_null_tax(self) -> None:
        """Should report tax as null when missing from extraction."""
        from modules.extraction_06.starter.extractor import validate_nullable_fields

        try:
            extraction = {
                "vendor_name": "Test Corp",
                "invoice_number": "INV-001",
                "date": "2026-01-15",
                "line_items": [{"description": "Widget", "quantity": 1, "unit_price": 100, "amount": 100}],
                "subtotal": 100,
                "tax": None,
                "total": 100,
                "currency": "USD",
                "confidence_notes": None,
            }

            null_fields = validate_nullable_fields(extraction)

            assert "tax" in null_fields
            assert "confidence_notes" in null_fields
        except NotImplementedError:
            pytest.skip("validate_nullable_fields not yet implemented")

    def test_no_nulls_when_all_present(self) -> None:
        """Should return empty list when all fields have values."""
        from modules.extraction_06.starter.extractor import validate_nullable_fields

        try:
            extraction = {
                "vendor_name": "Test Corp",
                "invoice_number": "INV-001",
                "date": "2026-01-15",
                "line_items": [{"description": "Widget", "quantity": 1, "unit_price": 100, "amount": 100}],
                "subtotal": 100,
                "tax": 8.50,
                "total": 108.50,
                "currency": "USD",
                "confidence_notes": "Tax rate assumed from state",
            }

            null_fields = validate_nullable_fields(extraction)

            assert len(null_fields) == 0
        except NotImplementedError:
            pytest.skip("validate_nullable_fields not yet implemented")
