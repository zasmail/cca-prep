"""Metrics aggregation for CCA-F evaluation results.

Computes accuracy, pass/fail counts, and latency statistics
from a list of EvalResult objects.
"""

from __future__ import annotations


from dataclasses import dataclass

from shared.eval.runner import EvalResult


@dataclass
class AggregateMetrics:
    """Aggregated metrics across an evaluation suite."""

    total: int
    passed: int
    failed: int
    accuracy: float  # 0.0 to 1.0
    avg_score: float
    avg_latency_ms: float
    total_cost_usd: float


def aggregate_results(results: list[EvalResult]) -> AggregateMetrics:
    """Compute aggregate metrics from a list of evaluation results.

    Args:
        results: List of EvalResult from run_eval_suite().

    Returns:
        AggregateMetrics with accuracy, pass/fail counts, and averages.
    """
    if not results:
        return AggregateMetrics(
            total=0,
            passed=0,
            failed=0,
            accuracy=0.0,
            avg_score=0.0,
            avg_latency_ms=0.0,
            total_cost_usd=0.0,
        )

    total = len(results)
    passed = sum(1 for r in results if r.passed)
    failed = total - passed

    return AggregateMetrics(
        total=total,
        passed=passed,
        failed=failed,
        accuracy=passed / total,
        avg_score=sum(r.score for r in results) / total,
        avg_latency_ms=sum(r.latency_ms for r in results) / total,
        total_cost_usd=sum(r.cost_usd for r in results),
    )
