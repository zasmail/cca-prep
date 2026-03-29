---
argument-hint: <feature-description>
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
---

# TDD Cycle: RED → GREEN → REFACTOR

CCA-F Exam Domain: D3 Claude Code Configuration (~20%)

This slash command drives a full TDD cycle for the given feature.
Run as: `/tdd-cycle add transfer validation to the payments API`

Key exam concepts demonstrated:
- `argument-hint:` — shows placeholder text, value accessible via $ARGUMENTS
- `allowed-tools:` — restricts available tools (principle of least privilege, AP8)
- Structured workflow phases with clear gates between them

---

## Phase 1: RED — Write Failing Tests First

Analyze the feature request: $ARGUMENTS

1. **Read** existing test files in the relevant module to understand conventions
2. **Grep** for related test patterns to avoid duplication
3. **Write** new test file(s) that describe the expected behavior:
   - Use descriptive test names: `test_<behavior>_when_<condition>_then_<expected>`
   - Follow AAA pattern: Arrange → Act → Assert
   - Include both happy path and edge cases
   - Include at least one anti-pattern guard test

4. **Run tests** to confirm they FAIL:
   ```bash
   uv run pytest <test_file> -v
   ```

GATE: All new tests must FAIL before proceeding. If any pass, the test isn't
testing new behavior — rewrite it.

## Phase 2: GREEN — Minimal Implementation

Write the MINIMUM code to make all failing tests pass:

1. **Read** the failing test output carefully
2. **Write** or **Edit** source files with the simplest implementation that satisfies tests
3. Do NOT over-engineer — write just enough to pass
4. **Run tests** to confirm they PASS:
   ```bash
   uv run pytest <test_file> -v
   ```

GATE: ALL tests (new and existing) must PASS before proceeding.
If existing tests broke, your implementation has a regression — fix it.

## Phase 3: REFACTOR — Clean Up While Green

Improve code quality without changing behavior:

1. **Read** through the implementation looking for:
   - Duplicated logic that can be extracted
   - Magic numbers/strings that need constants
   - Missing type hints
   - Unclear variable names
2. **Edit** files to refactor
3. **Run tests** after EVERY refactor step to ensure nothing broke:
   ```bash
   uv run pytest <test_file> -v
   ```

GATE: Tests must stay GREEN throughout refactoring. If any test fails,
your refactor changed behavior — revert and try again.

## Summary

After completing all three phases, provide:
- List of files created/modified
- Test count: X passing, 0 failing
- Brief description of what was implemented for: $ARGUMENTS
