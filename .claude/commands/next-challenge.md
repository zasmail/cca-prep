---
allowed-tools: Read, Write, Bash, Glob
---

# Next Challenge

Determine and advance to the next exercise tier. Follow these steps:

1. **Read progress**: `!cat progress.json`

2. **Find the current module and tier** (the first one with status "in_progress" or the first "not_started"):
   - Priority order: 01 → 02 → 03 → 04 → 05 → 06
   - Within each module: starter → intermediate → advanced

3. **Run tests for the current tier**:
   ```
   !uv run pytest modules/<module>/starter/tests/ -v --tb=short
   ```

4. **If tests PASS**:
   - Update progress.json: set current tier to "completed", next tier to "in_progress"
   - Congratulate with what exam pattern they just mastered
   - Read the next tier's skeleton and explain the new concepts it introduces
   - Give a concrete first TODO to work on

5. **If tests FAIL**:
   - Show which specific tests failed
   - Explain what exam pattern each failing test validates
   - Give a targeted hint (NOT the answer) about what to fix
   - Reference the anti-pattern number if relevant

6. **If all tiers in current module are complete**:
   - Mark module as complete
   - Advance to next module
   - Run `/start-module <next-number>` workflow

7. **If ALL modules complete**: Congratulate and suggest:
   - Run `/quiz-me` on weak areas
   - Review the Notion study guide for practice questions
   - Re-run `/check-work` for a final anti-pattern audit
