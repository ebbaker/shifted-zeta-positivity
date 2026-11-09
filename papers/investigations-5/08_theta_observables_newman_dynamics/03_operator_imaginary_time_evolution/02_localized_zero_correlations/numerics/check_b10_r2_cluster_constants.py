#!/usr/bin/env python3
"""Exact bookkeeping for B10 r2; no canonical zeros or values are evaluated.

9 November 2026. Prepared for Edward Baker with substantial OpenAI Codex
assistance. Recorded current thread gpt-6-astra/max; per-turn backend
configuration unavailable. Standard-library rational arithmetic only.
The analytic inequalities and conditional theorem are proved in Note20.
"""
from fractions import Fraction as Q
import json

def main():
    N, T, a = 1024, 1000, 2015
    r, sigma = Q(1, 2**12), Q(1, 2**24)
    source_majorant = 5 * Q(12, 11)**3
    source_anchor = Q(1, 7290)
    assert source_majorant < 7
    assert source_anchor > Q(1, 10000)
    assert 7 * 10000 < 2**20  # log(M/H0(0)) < 20 follows from e > 2.
    q = Q(1, 2**12)
    geometric = (1 + q) / (1 - q)**3
    tail_bound = 32 * a*a * geometric / 2**72
    assert geometric < 2
    assert tail_bound < Q(1, 2**44)
    omitted_pair = 2 * (N + Q(1, 2**44)) * Q(1, 2**44)
    assert omitted_pair < Q(1, 2**32)
    cluster = Q(18*N*N + 5*N, T) * r*r
    centroid = Q(18*N*N + 4*N, T) * sigma
    analytic = cluster + centroid + Q(1, 2**32)
    arithmetic = Q(1, 400)
    assert analytic < Q(1, 400)
    assert analytic + arithmetic < Q(1, 200) < Q(1, 100)
    first_order = Q(18*N*N + 4*N, T) * r
    assert first_order == Q(4609, 1000)
    print(json.dumps({
        "task": "TND-OC-B10 r2",
        "date_local": "2026-11-09",
        "prepared_for": "Edward Baker",
        "llm_assistance": "substantial OpenAI Codex",
        "recorded_current_thread_model": "gpt-6-astra",
        "recorded_current_thread_effort": "max",
        "per_turn_backend_configuration": None,
        "arithmetic": "Python fractions.Fraction",
        "scope": "Exact constants for the conditional clustered evaluator; no canonical computation",
        "majorant_upper_rational": str(source_majorant),
        "anchor_lower_rational": str(source_anchor),
        "gaussian_tail_upper_rational": str(tail_bound),
        "uniform_tail_target": "2^-44",
        "cluster_error_upper_rational": str(cluster),
        "centroid_error_upper_rational": str(centroid),
        "analytic_error_upper_rational": str(analytic),
        "arithmetic_radius_gate": str(arithmetic),
        "total_upper_rational": str(analytic + arithmetic),
        "total_strictly_below": "1/200",
        "count_only_first_order_allowance": str(first_order),
        "status": "exact_bookkeeping_passed_not_a_theta_certificate"
    }, indent=2))

if __name__ == "__main__":
    main()

