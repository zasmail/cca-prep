# Module 06: Structured Data Extraction

## Exam Coverage
- **Primary Domains**: D4 Prompt Engineering (~20%), D5 Context Management (~15%)
- **Combined weight**: ~35% of exam touches these domains

## Learning Objectives
1. Use forced `tool_choice` for guaranteed structured extraction
2. Design nullable fields to PREVENT fabrication (model returns null instead of guessing)
3. Implement validation-retry with SPECIFIC error feedback (not generic "try again")
4. Apply the two-pass pattern (citations-enabled free text for attribution, then forced tool_use for structure) — and know WHY it's two passes
5. Recognize that `tool_use` guarantees STRUCTURE but not SEMANTICS

## Key Patterns
- **Forced tool_use**: `tool_choice={"type": "tool", "name": "extract_invoice"}` guarantees structured output
- **Nullable fields**: Fields like `tax: nullable` prevent the model from fabricating values when data is missing
- **Validation-retry**: Extract -> validate -> if errors, send tool_result with `is_error=True` and SPECIFIC feedback
- **Two-pass pattern**: Pass 1 extracts with citations (free text — attribution), Pass 2 forces the result into schema (tool_use — structure)
- **Key insight**: Citations API IS compatible with tool_use (no API error). The real incompatibility is Citations + Structured Outputs (`output_config.format`) — that combination returns a 400 error. The two-pass ordering here exists because forced tool_choice suppresses text output (citations need text to attach to), not because of a documented citations/tool_use conflict.

## Anti-Patterns Tested
- AP6: Generic error messages ("try again") instead of specific feedback ("subtotal X but items sum to Y")
- AP10: Aggregate accuracy metrics only — must track per-document-type AND per-field metrics
- Fabricating values for missing fields (use nullable instead)
- Assuming citations are incompatible with tool_use (they aren't) — the real conflict is Structured Outputs
- Stating an unsourced "~15% better recall" figure for citations (no official percentage exists)

## Progression
- **Starter**: Invoice extraction with forced tool_use and nullable fields
- **Intermediate**: Validation-retry loop with specific error feedback
- **Advanced**: Two-pass pattern — citations-based extraction (free text), then forced tool_use structuring; correcting the citations/tool_use compatibility myth
