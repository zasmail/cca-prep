---
allowed-tools: Read, Bash, Glob, Grep
---

# Check Work

Review the learner's progress across all modules. Follow these steps:

1. **Read progress**: `!cat progress.json`

2. **Find and run tests**: `!cd modules && find . -name "test_*.py" -type f`
   Then run: `!cd /path/to/cca-prep && uv run pytest --tb=short -q`

3. **Review code against the 10 anti-patterns**:
   For each module with code written, check for:
   1. Text parsing instead of stop_reason checking
   2. Arbitrary iteration caps as PRIMARY loop control
   3. Prompt-based enforcement where hooks are needed
   4. Self-reported confidence scores for escalation
   5. Sentiment-based escalation triggers
   6. Generic error messages (missing isError/errorCategory/isRetryable)
   7. Silently suppressing errors / empty results as success
   8. More than 5 tools per agent
   9. Same-session self-review (needs separate sessions)
   10. Aggregate-only accuracy metrics

4. **Score each module tier**:
   - 🟢 **Pass** — Tests pass AND no anti-pattern violations
   - 🟡 **Needs work** — Tests pass but anti-pattern violations found
   - 🔴 **Critical** — Tests failing or major architectural issues

5. **Update progress.json** with current test counts and status.

6. **Recommend next action**: Which module/tier to work on next based on:
   - Exam domain weights (D1+D3 = 47%, prioritize these)
   - Current completion status
   - Dependencies between modules
