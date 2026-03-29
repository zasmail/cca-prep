"""Tool Selection Decision Matrix — Starter Tier.

CCA-F Exam Domains: D2 Tool Design (~18%), D3 Claude Code Configuration (~20%)

This exercise teaches the correct built-in tool for each task type.
The exam WILL present scenarios where Bash "works" but the dedicated tool is correct.
Selecting the wrong tool is one of the most common exam mistakes.

Key concepts tested:
- Each task type maps to exactly ONE correct tool
- Bash is a fallback, not a default — use dedicated tools first
- Using Write for small edits is an anti-pattern (overwrites entire file)
- Using Edit for new files is wrong (Edit requires existing content to match)
- MultiEdit exists for multiple changes to the same file
- AP8: More than 5 tools per agent degrades selection by ~40%
"""

from __future__ import annotations


from typing import Any


# ---------------------------------------------------------------------------
# Tool Matrix — maps task types to the CORRECT tool.
#
# EXAM INSIGHT: The exam tests whether you know these mappings.
# The "wrong" tool often works but is the anti-pattern answer.
#
# TODO: Complete this matrix with all correct mappings.
# Each entry: task_type -> {"correct": tool_name, "anti_pattern": wrong_tool, "why": reason}
# ---------------------------------------------------------------------------

TOOL_MATRIX: dict[str, dict[str, str]] = {
    "read_file": {
        "correct": "Read",
        "anti_pattern": "Bash('cat')",
        "why": (
            "Read is purpose-built for file reading with line numbers, "
            "image support, and PDF page ranges. Bash('cat') bypasses these features "
            "and provides a worse experience."
        ),
    },
    "modify_few_lines": {
        "correct": "Edit",
        "anti_pattern": "Write",
        "why": (
            "Edit sends only the diff — safer and more efficient for small changes. "
            "Write overwrites the entire file, risking data loss if you miss content. "
            "Edit also requires reading the file first, which forces verification."
        ),
    },
    "find_by_name": {
        "correct": "Glob",
        "anti_pattern": "Bash('find')",
        "why": (
            "Glob is optimized for filename pattern matching and returns results "
            "sorted by modification time. Bash('find') is slower on large codebases "
            "and lacks the built-in sorting."
        ),
    },
    "search_contents": {
        "correct": "Grep",
        "anti_pattern": "Bash('grep')",
        "why": (
            "Grep is built on ripgrep with optimized permissions and access. "
            "Supports output modes (content, files_with_matches, count), "
            "context lines, and file type filtering. Bash('grep') misses these."
        ),
    },
    "create_new_file": {
        "correct": "Write",
        "anti_pattern": "Edit",
        "why": (
            "Write creates files from scratch. Edit requires matching existing content "
            "with old_string — it CANNOT create new files since there is nothing to match on."
        ),
    },
    "multiple_edits_same_file": {
        "correct": "MultiEdit",
        "anti_pattern": "sequential Edit",
        "why": (
            "MultiEdit applies all changes atomically in a single operation. "
            "Sequential Edit calls can fail if an earlier edit shifts line numbers "
            "or changes content that a later edit expects to match."
        ),
    },
    "run_tests": {
        "correct": "Bash",
        "anti_pattern": None,
        "why": (
            "Running tests requires shell execution — there is no dedicated test tool. "
            "Bash is the CORRECT choice here. This is an exam trap: not every task "
            "has a dedicated tool, and Bash is right when execution is needed."
        ),
    },
    # TODO: Add these additional task types:
    # - "search_files_by_type" -> Grep with type parameter
    # - "read_specific_lines" -> Read with offset/limit
    # - "read_pdf_pages" -> Read with pages parameter
    # - "run_build" -> Bash (correct — build needs shell execution)
    # - "install_dependencies" -> Bash (correct — npm/pip needs shell)
    # - "check_git_status" -> Bash (correct — git needs shell)
}


def select_correct_tool(task_description: str) -> str:
    """Given a task description, return the name of the correct tool to use.

    This function implements the decision matrix that the CCA-F exam tests.
    The key insight: dedicated tools ALWAYS beat Bash for their specific purpose.

    TODO: Implement this function.

    Strategy:
    1. Normalize the task description (lowercase, strip whitespace)
    2. Match against known task patterns using keyword detection
    3. Return the correct tool name from TOOL_MATRIX
    4. If no specific match, return "Bash" as the general-purpose fallback

    EXAM INSIGHT: The exam presents task descriptions and asks which tool
    to use. The wrong answers are always tools that "work" but are anti-patterns.

    Args:
        task_description: Natural language description of the task.

    Returns:
        The name of the correct tool (e.g., "Read", "Edit", "Glob", "Grep",
        "Write", "MultiEdit", "Bash").
    """
    # TODO: Implement tool selection logic
    raise NotImplementedError("Implement select_correct_tool — the tool decision matrix")


def validate_tool_count(tools: list[dict[str, Any]]) -> tuple[bool, str]:
    """Validate that an agent's tool list follows AP8 guidelines.

    AP8: More than 5 tools per agent degrades selection reliability.
    At 18+ tools, selection accuracy drops by ~40%.

    TODO: Implement this function.

    Rules:
    - 1-5 tools: OK (optimal range)
    - 6-10 tools: WARNING (selection may degrade)
    - 11-17 tools: ERROR (significant degradation)
    - 18+ tools: CRITICAL (selection reliability drops ~40%)

    Args:
        tools: List of tool definition dicts.

    Returns:
        Tuple of (is_valid, message) where is_valid is True if <= 5 tools.
    """
    # TODO: Implement tool count validation
    raise NotImplementedError("Implement validate_tool_count — AP8 enforcement")


def explain_tool_choice(task_type: str) -> str:
    """Return a detailed explanation of why a specific tool is correct for a task.

    Useful for studying: given a task type from TOOL_MATRIX, returns the
    correct tool, the anti-pattern alternative, and the reasoning.

    TODO: Implement this function.

    Args:
        task_type: Key from TOOL_MATRIX (e.g., "read_file", "modify_few_lines").

    Returns:
        Formatted explanation string.

    Raises:
        KeyError: If task_type is not in TOOL_MATRIX.
    """
    # TODO: Implement explanation generator
    raise NotImplementedError("Implement explain_tool_choice — study aid for tool selection")
