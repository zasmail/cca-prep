# Module 06: Structured Data Extraction

## Exam Coverage
- **Primary Domains**: D4 Prompt Engineering (~20%), D5 Context Management (~15%)
- **Combined weight**: ~35% of exam touches these domains

## Learning Objectives
1. Use forced `tool_choice` for guaranteed structured extraction
2. Design nullable fields to PREVENT fabrication (model returns null instead of guessing)
3. Implement validation-retry with SPECIFIC error feedback (not generic "try again")
4. Apply the two-pass citations pattern (tool_use for structure, citations API for attribution)
5. Recognize that `tool_use` guarantees STRUCTURE but not SEMANTICS

## Key Patterns
- **Forced tool_use**: `tool_choice={"type": "tool", "name": "extract_invoice"}` guarantees structured output
- **Nullable fields**: Fields like `tax: nullable` prevent the model from fabricating values when data is missing
- **Validation-retry**: Extract -> validate -> if errors, send tool_result with `is_error=True` and SPECIFIC feedback
- **Two-pass citations**: Pass 1 extracts structure (tool_use), Pass 2 verifies attribution (citations API)
- **Key insight**: Citations API is INCOMPATIBLE with tool_use — must be separate passes

## Anti-Patterns Tested
- AP6: Generic error messages ("try again") instead of specific feedback ("subtotal X but items sum to Y")
- AP10: Aggregate accuracy metrics only — must track per-document-type AND per-field metrics
- Fabricating values for missing fields (use nullable instead)
- Combining tool_use and citations in a single pass (incompatible)

## Progression
- **Starter**: Invoice extraction with forced tool_use and nullable fields
- **Intermediate**: Validation-retry loop with specific error feedback
- **Advanced**: Two-pass pattern — tool_use extraction + citations verification
