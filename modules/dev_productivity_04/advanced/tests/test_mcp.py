"""Tests for Module 04 Advanced — MCP Integration.

These tests validate MCP integration patterns and AP8 tool limits.
"""

import pytest


class TestMCPConfig:
    """MCP configuration must follow Claude Code conventions."""

    def test_mcp_config_has_server_definition(self) -> None:
        """MCP_CONFIG must define at least one server with command and args."""
        from modules.dev_productivity_04.advanced.mcp_integration import MCP_CONFIG

        assert "mcpServers" in MCP_CONFIG, (
            "MCP config must have 'mcpServers' key — this is the .mcp.json format"
        )

        servers = MCP_CONFIG["mcpServers"]
        assert len(servers) > 0, "Must define at least one MCP server"

        for name, config in servers.items():
            assert "command" in config, f"Server '{name}' must have 'command'"
            assert "args" in config, f"Server '{name}' must have 'args'"

    def test_fintech_mock_server_configured(self) -> None:
        """The fintech-mock MCP server must be configured."""
        from modules.dev_productivity_04.advanced.mcp_integration import MCP_CONFIG

        assert "fintech-mock" in MCP_CONFIG["mcpServers"], (
            "fintech-mock server must be configured in MCP_CONFIG"
        )


class TestFintechTools:
    """Fintech tool definitions must follow API schema conventions."""

    def test_tools_have_valid_schema(self) -> None:
        """Each tool must have name, description, and input_schema."""
        from modules.dev_productivity_04.advanced.mcp_integration import FINTECH_TOOLS

        for tool in FINTECH_TOOLS:
            assert "name" in tool, "Tool must have 'name'"
            assert "description" in tool, "Tool must have 'description'"
            assert "input_schema" in tool, "Tool must have 'input_schema'"

            schema = tool["input_schema"]
            assert schema["type"] == "object", "input_schema type must be 'object'"
            assert "properties" in schema, "input_schema must have 'properties'"
            assert "required" in schema, "input_schema must have 'required'"

    def test_tools_encode_business_rules_in_descriptions(self) -> None:
        """Tool descriptions must encode business rules (exam-tested concept).

        The exam tests whether business rules are in tool descriptions
        vs only in the system prompt. Descriptions are more reliable.
        """
        from modules.dev_productivity_04.advanced.mcp_integration import FINTECH_TOOLS

        kyc_tool = next((t for t in FINTECH_TOOLS if t["name"] == "verify_kyc"), None)
        assert kyc_tool is not None, "verify_kyc tool must exist"
        assert "before" in kyc_tool["description"].lower() or \
               "must" in kyc_tool["description"].lower(), (
            "verify_kyc description should encode when it MUST be called"
        )

    def test_tool_count_within_ap8_limit(self) -> None:
        """FINTECH_TOOLS should demonstrate awareness of AP8 tool limits."""
        from modules.dev_productivity_04.advanced.mcp_integration import FINTECH_TOOLS

        # The defined tools should be within the recommended limit
        # (even if TODOs add more, the initial set should be reasonable)
        assert len(FINTECH_TOOLS) <= 10, (
            f"FINTECH_TOOLS has {len(FINTECH_TOOLS)} tools. "
            "AP8: More than 5 per agent degrades selection. "
            "Consider splitting across multiple agents."
        )


class TestMCPClientWrapper:
    """MCPClientWrapper must implement the correct lifecycle."""

    def test_client_initializes_with_config(self) -> None:
        """Client must accept server name and configuration."""
        from modules.dev_productivity_04.advanced.mcp_integration import (
            MCP_CONFIG,
            MCPClientWrapper,
        )

        config = MCP_CONFIG["mcpServers"]["fintech-mock"]

        client = MCPClientWrapper("fintech-mock", config)

        assert client.server_name == "fintech-mock"
        assert client._connected is False

    def test_client_has_lifecycle_methods(self) -> None:
        """Client must expose connect, list_tools, call_tool, disconnect."""
        from modules.dev_productivity_04.advanced.mcp_integration import MCPClientWrapper

        assert hasattr(MCPClientWrapper, "connect")
        assert hasattr(MCPClientWrapper, "list_tools")
        assert hasattr(MCPClientWrapper, "call_tool")
        assert hasattr(MCPClientWrapper, "disconnect")


class TestBuildAgentWithMCPTools:
    """build_agent_with_mcp_tools must enforce AP8 limits."""

    def test_respects_max_tools_limit(self) -> None:
        """Must not return more tools than max_tools_per_agent."""
        from modules.dev_productivity_04.advanced.mcp_integration import (
            build_agent_with_mcp_tools,
        )

        many_tools = [{"name": f"tool_{i}"} for i in range(15)]

        try:
            result = build_agent_with_mcp_tools(many_tools, max_tools_per_agent=5)
            assert len(result) <= 5, (
                f"Returned {len(result)} tools but limit is 5. AP8 violated."
            )
        except NotImplementedError:
            pytest.skip("build_agent_with_mcp_tools not yet implemented")

    def test_returns_all_when_under_limit(self) -> None:
        """When tools are within limit, return all of them."""
        from modules.dev_productivity_04.advanced.mcp_integration import (
            build_agent_with_mcp_tools,
        )

        few_tools = [{"name": f"tool_{i}"} for i in range(3)]

        try:
            result = build_agent_with_mcp_tools(few_tools, max_tools_per_agent=5)
            assert len(result) == 3, "Should return all tools when under limit"
        except NotImplementedError:
            pytest.skip("build_agent_with_mcp_tools not yet implemented")
