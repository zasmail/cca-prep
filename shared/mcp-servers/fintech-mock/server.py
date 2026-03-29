"""Fintech Mock MCP Server for CCA-F exam prep exercises.

Provides simulated banking/fintech tools: customer lookup, order management,
refunds, KYC checks, payments, and fraud risk assessment.
"""

from __future__ import annotations


import json
from datetime import datetime, timezone

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("fintech-mock")

# ---------------------------------------------------------------------------
# In-memory data stores
# ---------------------------------------------------------------------------

ACCOUNTS: dict[str, dict] = {
    "ACC-001": {
        "account_id": "ACC-001",
        "name": "Alice Johnson",
        "email": "alice@example.com",
        "balance": 15420.50,
        "status": "active",
        "type": "checking",
        "kyc_status": "verified",
        "kyc_level": "full",
        "created_at": "2024-01-15T10:00:00Z",
    },
    "ACC-002": {
        "account_id": "ACC-002",
        "name": "Bob Smith",
        "email": "bob@example.com",
        "balance": 82310.00,
        "status": "active",
        "type": "savings",
        "kyc_status": "verified",
        "kyc_level": "full",
        "created_at": "2024-02-20T14:30:00Z",
    },
    "ACC-003": {
        "account_id": "ACC-003",
        "name": "Carol Davis",
        "email": "carol@example.com",
        "balance": 500.00,
        "status": "frozen",
        "type": "checking",
        "kyc_status": "pending",
        "kyc_level": "basic",
        "created_at": "2024-03-10T09:15:00Z",
    },
}

CUSTOMERS: dict[str, dict] = {
    "CUST-001": {
        "customer_id": "CUST-001",
        "name": "Alice Johnson",
        "email": "alice@example.com",
        "account_id": "ACC-001",
        "status": "active",
        "kyc_verified": True,
        "created_at": "2024-01-15T10:00:00Z",
    },
    "CUST-002": {
        "customer_id": "CUST-002",
        "name": "Bob Smith",
        "email": "bob@example.com",
        "account_id": "ACC-002",
        "status": "active",
        "kyc_verified": True,
        "created_at": "2024-02-20T14:30:00Z",
    },
    "CUST-003": {
        "customer_id": "CUST-003",
        "name": "Carol Davis",
        "email": "carol@example.com",
        "account_id": "ACC-003",
        "status": "suspended",
        "kyc_verified": False,
        "created_at": "2024-03-10T09:15:00Z",
    },
}

ORDERS: dict[str, dict] = {
    "ORD-1001": {
        "order_id": "ORD-1001",
        "customer_id": "CUST-001",
        "total": 149.99,
        "status": "delivered",
        "items": [{"name": "USB-C Hub", "quantity": 1, "price": 149.99}],
        "created_at": "2024-11-01T08:00:00Z",
        "refund_eligible": True,
    },
    "ORD-1002": {
        "order_id": "ORD-1002",
        "customer_id": "CUST-002",
        "total": 899.00,
        "status": "shipped",
        "items": [{"name": "Standing Desk", "quantity": 1, "price": 899.00}],
        "created_at": "2024-11-15T12:00:00Z",
        "refund_eligible": True,
    },
    "ORD-1003": {
        "order_id": "ORD-1003",
        "customer_id": "CUST-001",
        "total": 2499.99,
        "status": "delivered",
        "items": [
            {"name": "MacBook Air M3", "quantity": 1, "price": 2499.99},
        ],
        "created_at": "2024-10-05T16:30:00Z",
        "refund_eligible": True,
    },
}

# Email lookup index
_EMAIL_TO_CUSTOMER: dict[str, str] = {c["email"]: cid for cid, c in CUSTOMERS.items()}

VALID_ESCALATION_REASONS = {"customer_request", "policy_gap", "capability_limit"}


def _error(message: str, code: str, *, is_retryable: bool = False) -> str:
    """Return a structured error response — exam anti-pattern #6 compliance."""
    return json.dumps({
        "error": message,
        "code": code,
        "isError": True,
        "isRetryable": is_retryable,
    })


# ---------------------------------------------------------------------------
# MCP Tools
# ---------------------------------------------------------------------------


@mcp.tool()
async def get_customer(customer_id: str) -> str:
    """Look up a customer by ID (CUST-xxx) or email address.

    MUST be called before any order lookup or refund to verify identity.
    Returns customer profile with kyc_verified flag.
    """
    # Try direct ID lookup
    if customer_id in CUSTOMERS:
        return json.dumps({"customer": CUSTOMERS[customer_id], "verified": True})

    # Try email lookup
    if customer_id in _EMAIL_TO_CUSTOMER:
        cid = _EMAIL_TO_CUSTOMER[customer_id]
        return json.dumps({"customer": CUSTOMERS[cid], "verified": True})

    return _error(
        f"Customer not found: {customer_id}",
        "CUSTOMER_NOT_FOUND",
    )


@mcp.tool()
async def lookup_order(order_id: str) -> str:
    """Look up an order by ID (ORD-xxxx). Returns order details including
    status, total, items, and refund eligibility.

    Requires prior customer verification via get_customer.
    """
    if order_id not in ORDERS:
        return _error(f"Order not found: {order_id}", "ORDER_NOT_FOUND")

    return json.dumps({"order": ORDERS[order_id]})


@mcp.tool()
async def process_refund(order_id: str, amount: float, reason: str) -> str:
    """Process a refund for an order.

    Validates:
    - Order exists
    - Amount > 0
    - Amount <= order total
    - Returns requires_approval: true if amount > $500

    Requires prior customer verification via get_customer.
    """
    if order_id not in ORDERS:
        return _error(f"Order not found: {order_id}", "ORDER_NOT_FOUND")

    order = ORDERS[order_id]

    if amount <= 0:
        return _error(
            "Refund amount must be greater than 0",
            "INVALID_AMOUNT",
        )

    if amount > order["total"]:
        return _error(
            f"Refund amount ${amount:.2f} exceeds order total ${order['total']:.2f}",
            "AMOUNT_EXCEEDS_TOTAL",
        )

    requires_approval = amount > 500
    refund_id = f"REF-{order_id.split('-')[1]}-{int(datetime.now(timezone.utc).timestamp())}"

    return json.dumps({
        "refund_id": refund_id,
        "order_id": order_id,
        "amount": amount,
        "reason": reason,
        "status": "pending_approval" if requires_approval else "processed",
        "requires_approval": requires_approval,
        "processed_at": datetime.now(timezone.utc).isoformat(),
    })


@mcp.tool()
async def escalate_to_human(
    case_summary: str,
    customer_id: str,
    reason: str,
    priority: str = "normal",
) -> str:
    """Escalate a case to a human agent.

    Valid reasons (exam-tested — only these 3 are correct):
    - customer_request: Customer explicitly asked for a human
    - policy_gap: No policy covers this situation
    - capability_limit: AI cannot perform the required action

    INVALID reasons (exam traps):
    - Sentiment-based ("customer sounds angry") — NEVER valid
    - Confidence-based ("I'm only 60% sure") — NEVER valid

    Priority: low, normal, high, urgent
    """
    if reason not in VALID_ESCALATION_REASONS:
        return _error(
            f"Invalid escalation reason: '{reason}'. "
            f"Valid reasons: {', '.join(sorted(VALID_ESCALATION_REASONS))}",
            "INVALID_ESCALATION_REASON",
        )

    if priority not in {"low", "normal", "high", "urgent"}:
        return _error(
            f"Invalid priority: '{priority}'. Valid: low, normal, high, urgent",
            "INVALID_PRIORITY",
        )

    if customer_id not in CUSTOMERS:
        return _error(f"Customer not found: {customer_id}", "CUSTOMER_NOT_FOUND")

    case_id = f"CASE-{int(datetime.now(timezone.utc).timestamp())}"

    return json.dumps({
        "case_id": case_id,
        "customer_id": customer_id,
        "reason": reason,
        "priority": priority,
        "summary": case_summary,
        "status": "escalated",
        "created_at": datetime.now(timezone.utc).isoformat(),
    })


@mcp.tool()
async def check_kyc_status(account_id: str) -> str:
    """Check KYC (Know Your Customer) verification status for an account.

    Returns kyc_status (verified/pending/failed) and verification level
    (basic/full/enhanced).
    """
    if account_id not in ACCOUNTS:
        return _error(f"Account not found: {account_id}", "ACCOUNT_NOT_FOUND")

    account = ACCOUNTS[account_id]
    return json.dumps({
        "account_id": account_id,
        "kyc_status": account["kyc_status"],
        "kyc_level": account["kyc_level"],
        "name": account["name"],
    })


@mcp.tool()
async def transfer_payment(
    from_account: str,
    to_account: str,
    amount: float,
    currency: str = "USD",
) -> str:
    """Transfer funds between accounts.

    Validates:
    - Both accounts exist
    - Neither account is frozen
    - Sufficient balance in source account
    - Amount > 0

    Updates balances in-memory on success.
    """
    if from_account not in ACCOUNTS:
        return _error(f"Source account not found: {from_account}", "ACCOUNT_NOT_FOUND")
    if to_account not in ACCOUNTS:
        return _error(f"Destination account not found: {to_account}", "ACCOUNT_NOT_FOUND")

    source = ACCOUNTS[from_account]
    dest = ACCOUNTS[to_account]

    if source["status"] == "frozen":
        return _error(
            f"Source account {from_account} is frozen",
            "ACCOUNT_FROZEN",
        )
    if dest["status"] == "frozen":
        return _error(
            f"Destination account {to_account} is frozen",
            "ACCOUNT_FROZEN",
        )

    if amount <= 0:
        return _error("Transfer amount must be greater than 0", "INVALID_AMOUNT")

    if source["balance"] < amount:
        return _error(
            f"Insufficient balance: ${source['balance']:.2f} < ${amount:.2f}",
            "INSUFFICIENT_BALANCE",
        )

    # Update balances
    source["balance"] -= amount
    dest["balance"] += amount

    txn_id = f"TXN-{int(datetime.now(timezone.utc).timestamp())}"

    return json.dumps({
        "transaction_id": txn_id,
        "from_account": from_account,
        "to_account": to_account,
        "amount": amount,
        "currency": currency,
        "status": "completed",
        "from_new_balance": source["balance"],
        "to_new_balance": dest["balance"],
        "processed_at": datetime.now(timezone.utc).isoformat(),
    })


@mcp.tool()
async def check_fraud_risk(
    account_id: str,
    amount: float,
    recipient_country: str = "US",
) -> str:
    """Assess fraud risk for a transaction.

    Returns risk_score (0-100), risk_level (low/medium/high), and flags:
    - HIGH_VALUE: amount > $10,000
    - INTERNATIONAL: recipient_country != "US"
    - FROZEN_ACCOUNT: source account is frozen
    """
    if account_id not in ACCOUNTS:
        return _error(f"Account not found: {account_id}", "ACCOUNT_NOT_FOUND")

    account = ACCOUNTS[account_id]
    flags: list[str] = []
    risk_score = 10  # Base score

    if amount > 10000:
        flags.append("HIGH_VALUE")
        risk_score += 30

    if recipient_country != "US":
        flags.append("INTERNATIONAL")
        risk_score += 25

    if account["status"] == "frozen":
        flags.append("FROZEN_ACCOUNT")
        risk_score += 40

    if account["kyc_status"] != "verified":
        flags.append("KYC_INCOMPLETE")
        risk_score += 20

    # Cap at 100
    risk_score = min(risk_score, 100)

    if risk_score >= 70:
        risk_level = "high"
    elif risk_score >= 40:
        risk_level = "medium"
    else:
        risk_level = "low"

    return json.dumps({
        "account_id": account_id,
        "amount": amount,
        "recipient_country": recipient_country,
        "risk_score": risk_score,
        "risk_level": risk_level,
        "flags": flags,
        "recommendation": "block" if risk_level == "high" else "allow",
        "assessed_at": datetime.now(timezone.utc).isoformat(),
    })


if __name__ == "__main__":
    mcp.run(transport="stdio")
