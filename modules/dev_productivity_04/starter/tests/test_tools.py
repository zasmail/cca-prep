"""Tests for Module 04 Starter — Tool Selection Decision Matrix.

These tests validate EXAM-CORRECT tool selection patterns.
Each test name describes the specific CCA-F pattern being validated.
"""

import pytest


class TestToolMatrix:
    """TOOL_MATRIX must contain correct mappings for all task types."""

    def test_matrix_has_all_core_task_types(self) -> None:
        """The tool matrix must cover all 7 core task types tested on the exam."""
        from modules.dev_productivity_04.starter.tool_selection import TOOL_MATRIX

        required_types = {
            "read_file",
            "modify_few_lines",
            "find_by_name",
            "search_contents",
            "create_new_file",
            "multiple_edits_same_file",
            "run_tests",
        }

        assert required_types.issubset(set(TOOL_MATRIX.keys())), (
            f"Missing task types: {required_types - set(TOOL_MATRIX.keys())}. "
            "All 7 core task types must be in the TOOL_MATRIX."
        )

    def test_each_entry_has_required_fields(self) -> None:
        """Each matrix entry must have correct, anti_pattern, and why fields."""
        from modules.dev_productivity_04.starter.tool_selection import TOOL_MATRIX

        for task_type, entry in TOOL_MATRIX.items():
            assert "correct" in entry, f"{task_type} missing 'correct' field"
            assert "anti_pattern" in entry, f"{task_type} missing 'anti_pattern' field"
            assert "why" in entry, f"{task_type} missing 'why' field"

    def test_read_file_uses_read_not_bash_cat(self) -> None:
        """Reading files must use Read tool, not Bash('cat').

        Read provides line numbers, image support, and PDF page ranges.
        Bash('cat') bypasses all of these and is the anti-pattern answer.
        """
        from modules.dev_productivity_04.starter.tool_selection import TOOL_MATRIX

        entry = TOOL_MATRIX["read_file"]

        assert entry["correct"] == "Read"
        assert "cat" in entry["anti_pattern"].lower() or "Bash" in entry["anti_pattern"]

    def test_modify_few_lines_uses_edit_not_write(self) -> None:
        """Modifying a few lines must use Edit, not Write.

        Edit sends only the diff. Write overwrites the entire file.
        """
        from modules.dev_productivity_04.starter.tool_selection import TOOL_MATRIX

        entry = TOOL_MATRIX["modify_few_lines"]

        assert entry["correct"] == "Edit"
        assert "Write" in entry["anti_pattern"]

    def test_find_by_name_uses_glob_not_bash_find(self) -> None:
        """Finding files by name must use Glob, not Bash('find')."""
        from modules.dev_productivity_04.starter.tool_selection import TOOL_MATRIX

        entry = TOOL_MATRIX["find_by_name"]

        assert entry["correct"] == "Glob"
        assert "find" in entry["anti_pattern"].lower() or "Bash" in entry["anti_pattern"]

    def test_search_contents_uses_grep_not_bash_grep(self) -> None:
        """Searching file contents must use Grep, not Bash('grep')."""
        from modules.dev_productivity_04.starter.tool_selection import TOOL_MATRIX

        entry = TOOL_MATRIX["search_contents"]

        assert entry["correct"] == "Grep"
        assert "grep" in entry["anti_pattern"].lower() or "Bash" in entry["anti_pattern"]

    def test_create_new_file_uses_write_not_edit(self) -> None:
        """Creating new files must use Write, not Edit.

        Edit requires existing content to match — cannot create files from scratch.
        """
        from modules.dev_productivity_04.starter.tool_selection import TOOL_MATRIX

        entry = TOOL_MATRIX["create_new_file"]

        assert entry["correct"] == "Write"
        assert "Edit" in entry["anti_pattern"]

    def test_multiple_edits_uses_multiedit(self) -> None:
        """Multiple edits to the same file must use MultiEdit for atomicity."""
        from modules.dev_productivity_04.starter.tool_selection import TOOL_MATRIX

        entry = TOOL_MATRIX["multiple_edits_same_file"]

        assert entry["correct"] == "MultiEdit"

    def test_run_tests_correctly_uses_bash(self) -> None:
        """Running tests is one case where Bash IS the correct tool.

        Exam trap: not every task has a dedicated tool.
        """
        from modules.dev_productivity_04.starter.tool_selection import TOOL_MATRIX

        entry = TOOL_MATRIX["run_tests"]

        assert entry["correct"] == "Bash"
        assert entry["anti_pattern"] is None


class TestSelectCorrectTool:
    """select_correct_tool must return the right tool for task descriptions."""

    def test_read_file_task(self) -> None:
        """'Read the contents of config.py' -> Read."""
        from modules.dev_productivity_04.starter.tool_selection import select_correct_tool

        try:
            result = select_correct_tool("Read the contents of config.py")
            assert result == "Read"
        except NotImplementedError:
            pytest.skip("select_correct_tool not yet implemented")

    def test_modify_lines_task(self) -> None:
        """'Change the import on line 3' -> Edit."""
        from modules.dev_productivity_04.starter.tool_selection import select_correct_tool

        try:
            result = select_correct_tool("Change the import on line 3")
            assert result == "Edit"
        except NotImplementedError:
            pytest.skip("select_correct_tool not yet implemented")

    def test_find_file_task(self) -> None:
        """'Find all Python test files' -> Glob."""
        from modules.dev_productivity_04.starter.tool_selection import select_correct_tool

        try:
            result = select_correct_tool("Find all Python test files named test_*.py")
            assert result == "Glob"
        except NotImplementedError:
            pytest.skip("select_correct_tool not yet implemented")

    def test_search_content_task(self) -> None:
        """'Search for all usages of process_refund' -> Grep."""
        from modules.dev_productivity_04.starter.tool_selection import select_correct_tool

        try:
            result = select_correct_tool("Search for all usages of process_refund")
            assert result == "Grep"
        except NotImplementedError:
            pytest.skip("select_correct_tool not yet implemented")

    def test_create_file_task(self) -> None:
        """'Create a new file called helpers.py' -> Write."""
        from modules.dev_productivity_04.starter.tool_selection import select_correct_tool

        try:
            result = select_correct_tool("Create a new file called helpers.py")
            assert result == "Write"
        except NotImplementedError:
            pytest.skip("select_correct_tool not yet implemented")

    def test_run_tests_task(self) -> None:
        """'Run the test suite with pytest' -> Bash."""
        from modules.dev_productivity_04.starter.tool_selection import select_correct_tool

        try:
            result = select_correct_tool("Run the test suite with pytest")
            assert result == "Bash"
        except NotImplementedError:
            pytest.skip("select_correct_tool not yet implemented")


class TestToolCountValidation:
    """AP8: More than 5 tools per agent degrades selection reliability."""

    def test_five_or_fewer_tools_is_valid(self) -> None:
        """5 or fewer tools should pass validation."""
        from modules.dev_productivity_04.starter.tool_selection import validate_tool_count

        try:
            tools = [{"name": f"tool_{i}"} for i in range(5)]

            is_valid, message = validate_tool_count(tools)

            assert is_valid is True
        except NotImplementedError:
            pytest.skip("validate_tool_count not yet implemented")

    def test_more_than_five_tools_is_invalid(self) -> None:
        """More than 5 tools should fail validation (AP8)."""
        from modules.dev_productivity_04.starter.tool_selection import validate_tool_count

        try:
            tools = [{"name": f"tool_{i}"} for i in range(10)]

            is_valid, message = validate_tool_count(tools)

            assert is_valid is False
            assert "degrade" in message.lower() or "warning" in message.lower()
        except NotImplementedError:
            pytest.skip("validate_tool_count not yet implemented")

    def test_eighteen_plus_tools_is_critical(self) -> None:
        """18+ tools should report critical degradation (~40% drop)."""
        from modules.dev_productivity_04.starter.tool_selection import validate_tool_count

        try:
            tools = [{"name": f"tool_{i}"} for i in range(20)]

            is_valid, message = validate_tool_count(tools)

            assert is_valid is False
            assert "40%" in message or "critical" in message.lower()
        except NotImplementedError:
            pytest.skip("validate_tool_count not yet implemented")
