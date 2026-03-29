"""MCP Integration — Advanced Tier.

CCA-F Exam Domains: D2 Tool Design (~18%), D3 Claude Code Configuration (~20%)

This exercise teaches how to wrap an external MCP server (fintech-mock)
as custom tools available to Claude Code. MCP tools appear as regular tools
to the model — the integration is transparent.

Key concepts tested:
- MCP servers provide tools with the same schema as built-in tools
- Tool definitions follow the same input_schema format as API tools
- Connection lifecycle: initialize -> list tools -> call tool -> shutdown
- .mcp.json configures server connections for Claude Code
- MCP tools count toward the AP8 tool limit (5 per agent guideline)
"""

from __future__ import annotations


import json
from typing import Any


# ---------------------------------------------------------------------------
# MCP Server Configuration
#
# In Claude Code, this lives in .mcp.json at the project root.
# Format: {"mcpServers": {"server-name": {"command": "...", "args": [...]}}}
#
# EXAM INSIGHT: Know that .mcp.json is the configuration file for MCP servers
# in Claude Code. The exam may ask where MCP servers are configured.
# ---------------------------------------------------------------------------

MCP_CONFIG: dict[str, Any] = {
    "mcpServers": {
        "fintech-mock": {
            "command": "uv",
            "args": [
                "--directory",
                "shared/mcp-servers/fintech-mock",
                "run",
                "server.py",
            ],
        },
    },
}


# ---------------------------------------------------------------------------
# Fintech Tool Definitions
#
# These mirror what the fintech-mock MCP server provides.
# In practice, tools are discovered via MCP's tools/list method.
# Here we define them explicitly for the exercise.
#
# TODO: Add the remaining fintech tools:
# - check_fraud_score (input: transaction_id) -> risk assessment
# - get_account_balance (input: account_id) -> balance info
# - list_transactions (input: account_id, date_range) -> transaction list
# ---------------------------------------------------------------------------

FINTECH_TOOLS: list[dict[str, Any]] = [
    {
        "name": "verify_kyc",
        "description": (
            "Verify a customer's KYC (Know Your Customer) status. "
            "Returns verification level (basic, enhanced, none) and any "
            "pending requirements. Must be checked before high-value operations."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "customer_id": {
                    "type": "string",
                    "pattern": "^CUST-\\d{3}$",
                    "description": "Customer ID in format CUST-xxx",
                },
            },
            "required": ["customer_id"],
        },
    },
    {
        "name": "process_payment",
        "description": (
            "Process a payment between accounts. Validates sufficient balance, "
            "KYC status, and fraud score before executing. "
            "Returns transaction_id and status."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "from_account": {
                    "type": "string",
                    "pattern": "^ACC-\\d{3}$",
                    "description": "Source account ID",
                },
                "to_account": {
                    "type": "string",
                    "pattern": "^ACC-\\d{3}$",
                    "description": "Destination account ID",
                },
                "amount": {
                    "type": "number",
                    "minimum": 0.01,
                    "description": "Payment amount in USD",
                },
                "currency": {
                    "type": "string",
                    "enum": ["USD", "EUR", "GBP"],
                    "default": "USD",
                },
            },
            "required": ["from_account", "to_account", "amount"],
        },
    },
    # TODO: Add check_fraud_score tool definition
    # TODO: Add get_account_balance tool definition
    # TODO: Add list_transactions tool definition
]


class MCPClientWrapper:
    """Wrapper for communicating with an MCP server.

    This class abstracts the MCP protocol for use in Claude Code tool execution.
    In production, Claude Code handles this automatically via .mcp.json.
    This exercise teaches the underlying mechanics.

    TODO: Implement the MCP client lifecycle methods.

    MCP Protocol Flow:
    1. Initialize: Send initialize request, receive server capabilities
    2. List Tools: Send tools/list request, receive available tools
    3. Call Tool: Send tools/call with name + arguments, receive result
    4. Shutdown: Send shutdown notification, close connection

    EXAM INSIGHT: You don't need to implement MCP from scratch on the exam,
    but you DO need to understand the lifecycle and how tools are discovered.
    """

    def __init__(self, server_name: str, config: dict[str, Any]) -> None:
        """Initialize the MCP client wrapper.

        Args:
            server_name: Name of the MCP server (key in .mcp.json).
            config: Server configuration (command, args, env).
        """
        self.server_name = server_name
        self.config = config
        self._connected = False
        self._tools: list[dict[str, Any]] = []

    async def connect(self) -> None:
        """Connect to the MCP server and perform initialization handshake.

        TODO: Implement connection logic.

        Steps:
        1. Start the server process using config["command"] and config["args"]
        2. Send the initialize request with client capabilities
        3. Receive and store server capabilities
        4. Set _connected = True
        """
        # TODO: Implement MCP connection
        raise NotImplementedError("Implement connect — MCP initialization handshake")

    async def list_tools(self) -> list[dict[str, Any]]:
        """Discover available tools from the MCP server.

        TODO: Implement tool discovery.

        Steps:
        1. Send tools/list request to the server
        2. Parse the response to extract tool definitions
        3. Store in self._tools for later reference
        4. Return the list of tool definitions

        EXAM INSIGHT: Tool discovery is dynamic — the server declares its tools
        at runtime, not at configuration time. This is why .mcp.json only has
        the command to start the server, not the tool definitions.
        """
        # TODO: Implement tool listing
        raise NotImplementedError("Implement list_tools — MCP tool discovery")

    async def call_tool(self, tool_name: str, arguments: dict[str, Any]) -> str:
        """Call a tool on the MCP server.

        TODO: Implement tool calling.

        Steps:
        1. Validate tool_name exists in self._tools
        2. Send tools/call request with name and arguments
        3. Parse the response (can be text, image, or resource content)
        4. Return the result as a JSON string

        Error handling:
        - If tool not found, return structured error with isError=True
        - If server returns error, propagate with error details
        - NEVER silently suppress errors (AP7)

        Args:
            tool_name: Name of the tool to call.
            arguments: Tool input arguments.

        Returns:
            JSON string with the tool result.
        """
        # TODO: Implement tool calling
        raise NotImplementedError("Implement call_tool — MCP tool execution")

    async def disconnect(self) -> None:
        """Gracefully disconnect from the MCP server.

        TODO: Implement disconnection.

        Steps:
        1. Send shutdown notification
        2. Close the connection
        3. Terminate the server process
        4. Set _connected = False
        """
        # TODO: Implement disconnection
        raise NotImplementedError("Implement disconnect — MCP graceful shutdown")


def build_agent_with_mcp_tools(
    mcp_tools: list[dict[str, Any]],
    max_tools_per_agent: int = 5,
) -> list[dict[str, Any]]:
    """Select the most relevant MCP tools for an agent, respecting AP8 limits.

    AP8: More than 5 tools per agent degrades selection reliability.
    When an MCP server provides many tools, you must select a subset.

    TODO: Implement tool selection for agent configuration.

    Strategy:
    1. If len(mcp_tools) <= max_tools_per_agent, use all of them
    2. If more, select the most relevant based on the agent's purpose
    3. Consider splitting into multiple specialized agents (orchestrator pattern)

    Args:
        mcp_tools: All available tools from MCP server(s).
        max_tools_per_agent: Maximum tools per agent (default 5, per AP8).

    Returns:
        Selected subset of tools for this agent.
    """
    # TODO: Implement tool selection with AP8 enforcement
    raise NotImplementedError("Implement build_agent_with_mcp_tools — AP8 tool selection")
