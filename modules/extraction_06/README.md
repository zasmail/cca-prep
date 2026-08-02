# Module 06: Structured Data Extraction

## Overview
This module teaches structured data extraction patterns — a high-frequency exam topic.
The critical insight: `tool_use` guarantees STRUCTURE (valid JSON matching your schema)
but NOT SEMANTICS (the values could still be wrong). Validation and citations close that gap.

## Domains Covered
| Domain | Weight | Focus |
|--------|--------|-------|
| D4 Prompt Engineering | ~20% | tool_choice, nullable fields, validation prompts |
| D5 Context Management | ~15% | Citations API, document handling, two-pass patterns |

## Tier Breakdown

### Starter: Invoice Extraction
**File**: `starter/extractor.py`

Forced extraction using tool_use with:
- `tool_choice={"type": "tool", "name": "extract_invoice"}` for guaranteed structure
- Nullable fields (`tax`, `confidence_notes`) to prevent fabrication
- ISO 8601 date format
- Line items array with per-item structure

### Intermediate: Validation-Retry Loop
**File**: `intermediate/validation_retry.py`

Extract-validate-retry pattern:
- Extract using forced tool_use
- Validate extracted data (totals match, required fields present)
- On error: send `tool_result` with `is_error=True` and SPECIFIC feedback
- Key: Error messages must be specific ("subtotal $X but items sum to $Y")
- NEVER use generic "try again" messages (AP6)
- Max retries with exponential backoff

### Advanced: Two-Pass Citations + Structuring
**File**: `advanced/citations_extraction.py`

Two-pass extraction pattern:
- Pass 1: Extract with citations enabled (free text) — gets source attribution
- Pass 2: Force the cited findings into schema via tool_use — gets guaranteed structure
- Key: Citations API IS compatible with tool_use (no API error). The real incompatibility
  is Citations + Structured Outputs (`output_config.format`) — that combination returns a
  400 error. The two-pass order exists because forced `tool_choice` suppresses text output,
  leaving citations nowhere to attach — not because citations and tool_use conflict.
- Citations `cited_text` is NOT counted as output tokens

## Running Tests
```bash
uv run pytest modules/extraction_06/ -v
```

## Key Exam Insights
- `tool_choice: {"type": "tool", ...}` is INCOMPATIBLE with extended thinking
- Nullable fields are the exam-correct way to handle missing data
- Validation-retry uses the same conversation (append tool_result with is_error)
- Citations are "significantly more likely" to cite the most relevant quotes than prompt-only approaches (Anthropic's own evaluations) — no official percentage is published, so don't repeat a specific number as fact
- Citations must be enabled on ALL or NONE documents (no selective enabling)
- Per-field accuracy metrics are required — aggregate-only is AP10
