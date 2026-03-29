---
argument-hint: <module-number 1-6>
allowed-tools: Read, Write, Bash, Glob
---

# Start Module $ARGUMENTS

You are launching a CCA-F exam prep module. Follow these steps:

1. **Validate input**: Module number must be 1-6. Map to directory:
   - 1 → modules/support_agent_01 (D1 Agentic Architecture ~27%)
   - 2 → modules/claude_code_config_02 (D3 Claude Code Config ~20%)
   - 3 → modules/multi_agent_03 (D1, D2, D5 ~18%)
   - 4 → modules/dev_productivity_04 (D2, D3 ~18%)
   - 5 → modules/cicd_pipeline_05 (D3, D4 ~20%)
   - 6 → modules/extraction_06 (D4, D5 ~15%)

2. **Read the module CLAUDE.md**: `!cat modules/<module-dir>/CLAUDE.md`

3. **Show the learner**:
   - Module name and which exam domains it covers
   - Domain weight (how much of the exam this represents)
   - Learning objectives from the CLAUDE.md
   - The 3 tiers: starter → intermediate → advanced
   - Which anti-patterns this module specifically tests

4. **Check progress**: Read `progress.json` to see if any tiers are already completed.

5. **Scaffold exercise files** if they don't exist yet:
   - Read the starter skeleton files
   - Explain what each TODO requires
   - Suggest starting with the starter tier

6. **Give a concrete first task**: Tell the learner exactly what to implement first,
   with a hint about which exam pattern it tests.

Remember: This learner learns by DOING. Don't explain theory — point them at code to write.
