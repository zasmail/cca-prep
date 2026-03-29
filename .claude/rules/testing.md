---
paths: "**/tests/**"
---

# Testing Rules

- Every implementation MUST have corresponding tests
- Test names MUST describe the exam pattern being validated:
  - `test_uses_stop_reason_not_text_parsing` (AP1)
  - `test_hook_enforces_kyc_before_refund` (AP3)
  - `test_error_includes_is_retryable_field` (AP6)
- Tests validate **architectural correctness**, not just "does it run"
- Use AAA pattern: Arrange (blank line) Act (blank line) Assert
- Mock external API calls (anthropic client) but NOT the architectural patterns
- Test both success AND failure paths
- Test anti-pattern violations explicitly — prove the guard works by testing what happens when violated
