#!/usr/bin/env python3
"""Read-only, floating audit of two calculations in Claude's brainstorm.

16 October 2026. Prepared for Edward Baker with LLM assistance.
Coordinating model gpt-6-astra (Codex), reasoning effort ultra.

Print JSON to stdout. No file writes. Requires NumPy and the existing source
checker, located relative to --repo. This is not an interval certificate.
"""
import argparse
import hashlib
import json
import math
import platform
from pathlib import Path
import runpy
import sys

import numpy as np

DEPENDENCY = "papers/brainstorm/investigations-3/numerics/check_brainstorm_modifications_claude_20261016.py"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, required=True)
    args = parser.parse_args()
    path = args.repo / DEPENDENCY
    expected = "b7249c105ba42bc6e13c9397b837fdf60dab8c130f7c762debbae60683c5cfbc"
    if hashlib.sha256(path.read_bytes()).hexdigest() != expected:
        raise SystemExit("Source checker differs from the reviewed dependency")
    m = runpy.run_path(str(path))
    term = m["term_transform"]
    rows = []
    for t, x in ((0.25, 44.1303), (0.0, 60.0)):
        matrix = np.array([[term(n, t, x, deriv=j) for n in range(1, 7)]
                           for j in (0, 1)])
        field = matrix.sum(axis=1)
        solves = []
        for n in (2, 3, 6):
            a = matrix[:, :n]
            delta, _, rank, singular = np.linalg.lstsq(a, -field, rcond=None)
            solves.append({
                "N": n, "distance": float(np.linalg.norm(delta)),
                "perturbed_weights": (1.0 + delta).tolist(),
                "singular_values": singular.tolist(), "numerical_rank": int(rank),
                "condition_number": float(singular[0] / singular[-1]),
                "linear_residual": (a @ delta + field).tolist(),
                "positive_weights": bool(np.all(1.0 + delta >= 0.0)),
            })
        rows.append({"t": t, "x": x, "columns_first_six": matrix.tolist(),
                     "theta_jet_truncated_at_six": field.tolist(), "solves": solves})

    t_height = 3e12
    log_height = math.log(t_height / (2.0 * math.pi))
    s_bound = m["trudgian_S_bound"](t_height)
    original_pull = m["pull_lower_bound"]
    original_b1 = m["best_pull_coefficient"](log_height, s_bound, 1.0)
    # N counts individual zeros; each displayed lower bound applies to two.
    # This mutation changes only this transient module dictionary in memory.
    m["best_pull_coefficient"].__globals__["pull_lower_bound"] = (
        lambda b, L, S, D: original_pull(b, L, S, D) / 2.0)
    corrected_b1 = m["best_pull_coefficient"](log_height, s_bound, 1.0)
    collision_times = {str(steps): m["collision_time"](1.0, log_height, s_bound, steps)
                       for steps in (500, 1000)}
    result = {
        "status": "Floating diagnostic, not certified. No new zero-free domain or theorem about zeta.",
        "prepared_for": "Edward Baker",
        "author_assistance": "OpenAI Codex, coordinating model gpt-6-astra, reasoning effort ultra, verified from coordinating session metadata",
        "date": "2026-10-16 America/New_York",
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "dependency": {"repo_relative_path": DEPENDENCY,
                       "sha256": hashlib.sha256(path.read_bytes()).hexdigest()},
        "environment": {"python": sys.version, "numpy": np.__version__,
                        "platform": platform.platform()},
        "quadrature": {"method": "Dependency composite Simpson rule",
                       "panels": m["PANELS"], "upper_endpoint": m["U_MAX"],
                       "theta_nmax": 6,
                       "limitations": "Floating and truncated; no quadrature/tail error enclosure. Printed residuals only measure the computed linear system."},
        "coefficient_distance": rows,
        "attraction": {
            "T": t_height, "L": log_height, "S_bound": s_bound,
            "D_grid": {"min": 0.5, "max": 60.0, "step": 0.05},
            "b0": 1.0,
            "original_b1_pull_and_window": original_b1,
            "corrected_b1_pull_and_window": corrected_b1,
            "corrected_time_midpoint_steps": collision_times,
            "remaining_hypotheses": "Uses a time-zero count at positive time without justification, and freezes location/count parameters; not an upper bound on the Newman constant.",
            "exact_pair_inequality_proof": {
                "variables": "u=d^2, B=b^2, C=c^2, b>0, 0<=c<=b; nonzero denominators",
                "g": "g(y)=2y/(u+y^2)",
                "difference": "g(b-c)+g(b+c)-4b/(u+4B) = 4b(B-C)(3u+3B+C)/[((u+B+C)^2-4BC)(u+4B)] >= 0",
                "counting": "A conjugate pair uses two counted zeros. A real zero is half a c=0 pair. Thus N individual zeros give aggregate pull at least 2b*N/(D^2+4b^2), not 4b*N/(D^2+4b^2).",
            },
        },
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
