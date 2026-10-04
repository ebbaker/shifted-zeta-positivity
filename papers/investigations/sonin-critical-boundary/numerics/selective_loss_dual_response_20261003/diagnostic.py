#!/usr/bin/env python3
"""Small floating diagnostic of the actual finite arithmetic response.

No source/Sonin inverse is computed. No outward rounding or certificate.
NumPy must already be available; this script never installs dependencies.
"""

import hashlib
import json
import math
from pathlib import Path
import platform
import time

import numpy as np


ROOT = Path(__file__).resolve().parent
RS = (2, 3, 4, 5, 6)
ORDERS = (16, 24, 32)
NORM_NUM = 146640624550936576
NORM_DEN = 37921101075
G0_NORM_SQ = NORM_NUM / NORM_DEN
G0_NORM = math.sqrt(G0_NORM_SQ)


def g(x):
    """Normalized factored polynomial; caller supplies points in support."""
    xx = x * x
    return (-64 * x * (1 - 16 * xx) ** 5
            * (2689 - 215072 * xx + 256 * xx * xx)) / G0_NORM


def active_prime_powers(L):
    cutoff = math.exp(L)
    N = int(cutoff)
    sieve = [True] * (N + 1)
    sieve[:2] = [False, False]
    for p in range(2, math.isqrt(N) + 1):
        if sieve[p]:
            for n in range(p * p, N + 1, p):
                sieve[n] = False
    out = []
    for p in range(2, N + 1):
        if not sieve[p]:
            continue
        n, m = p, 1
        while n < cutoff:
            out.append({"n": n, "p": p, "m": m,
                        "log_n": math.log(n),
                        "coefficient": math.log(p) / math.sqrt(2 * n)})
            n *= p
            m += 1
    return sorted(out, key=lambda row: row["n"])


def packets_and_breakpoints(r):
    L = r + 0.5
    half = L / 2
    pp = active_prime_powers(L)
    packets = []
    points = {-half, half}
    for row in pp:
        a = row["log_n"] - r / 2
        for center in (a, -a):
            packets.append((center, row["coefficient"]))
            for endpoint in (center - 0.25, center + 0.25):
                points.add(max(-half, min(half, endpoint)))
    return L, pp, packets, np.array(sorted(points), dtype=float)


def arithmetic_response(x, packets):
    out = np.zeros_like(x)
    for center, coefficient in packets:
        shifted = x - center
        inside = np.abs(shifted) < 0.25
        out[inside] += coefficient * g(shifted[inside])
    return out


def integrate_order(order, L, packets, points):
    nodes, weights = np.polynomial.legendre.leggauss(order)
    mid = (points[:-1] + points[1:]) / 2
    radius = (points[1:] - points[:-1]) / 2
    x = mid[:, None] + radius[:, None] * nodes[None, :]
    wf = arithmetic_response(x, packets)
    quadrature_weights = radius[:, None] * weights[None, :]
    raw = float(np.sum(quadrature_weights * wf * wf))
    sinh_moment = float(np.sum(quadrature_weights * np.sinh(x / 2) * wf))
    denominator = math.sinh(L / 2) - L / 2
    subtraction = sinh_moment * sinh_moment / denominator
    projected = raw - subtraction
    return {
        "order": order,
        "raw_norm_sq": raw,
        "sinh_moment": sinh_moment,
        "projection_denominator": denominator,
        "subtracted_norm_sq": subtraction,
        "projected_norm_sq": projected,
        "retained_fraction": projected / raw,
        "mean_moment_diagnostic": float(np.sum(quadrature_weights * wf)),
        "cosh_moment_diagnostic": float(np.sum(
            quadrature_weights * np.cosh(x / 2) * wf)),
    }


def difference(a, b, key):
    absolute = abs(a[key] - b[key])
    return {"absolute": absolute,
            "relative": absolute / max(abs(b[key]), np.finfo(float).tiny)}


def run():
    started = time.perf_counter()
    source_hash = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    rows = []
    preflight = []
    for r in RS:
        L, pp, packets, points = packets_and_breakpoints(r)
        preflight.append({"r": r, "prime_power_count": len(pp),
                          "piece_count": len(points) - 1,
                          "largest_active_n": max(row["n"] for row in pp),
                          "quadrature_evaluations":
                          (len(points) - 1) * sum(ORDERS)})
        orders = [integrate_order(n, L, packets, points) for n in ORDERS]
        q16, q24, q32 = orders
        primary = q16["raw_norm_sq"] - q32["subtracted_norm_sq"]
        rows.append({
            "r": r, "L": L,
            "prime_power_count": len(pp),
            "piece_count": len(points) - 1,
            "raw_norm_sq_16": q16["raw_norm_sq"],
            "sinh_moment_32": q32["sinh_moment"],
            "projected_norm_sq_raw16_moment32": primary,
            "raw_norm_16": math.sqrt(q16["raw_norm_sq"]),
            "projected_norm_raw16_moment32": math.sqrt(primary),
            "retained_fraction_raw16_moment32": primary / q16["raw_norm_sq"],
            "projected_norm_sq_over_r2": primary / (r * r),
            "orders": orders,
            "order_comparison": {
                "raw16_vs24": difference(q16, q24, "raw_norm_sq"),
                "raw24_vs32": difference(q24, q32, "raw_norm_sq"),
                "moment24_vs32": difference(q24, q32, "sinh_moment"),
                "projected24_vs32": difference(q24, q32, "projected_norm_sq"),
                "primary_vs_all32": {
                    "absolute": abs(primary - q32["projected_norm_sq"]),
                    "relative": abs(primary - q32["projected_norm_sq"])
                    / q32["projected_norm_sq"],
                },
            },
        })
    for i, row in enumerate(rows):
        row["successive_projected_ratio"] = (
            None if i == 0 else row["projected_norm_sq_raw16_moment32"]
            / rows[i - 1]["projected_norm_sq_raw16_moment32"])
    gn, gw = np.polynomial.legendre.leggauss(16)
    normalized_probe_sq_check = float(np.sum(gw * g(gn / 4) ** 2) / 4)
    record = {
        "date": "2026-10-03",
        "prepared_for": "Edward Baker",
        "model": "GPT-6 (Codex)",
        "serving_variant": "not exposed; not inferred",
        "reasoning_effort": "not exposed; not inferred",
        "llm_acknowledgement": "Prepared with substantial LLM assistance.",
        "status": "FLOATING DIAGNOSTIC ONLY; no outward certificate",
        "scope": "Actual finite arithmetic W_L response, projected to the three-moment source space. No B inverse, Sonin correction, or A inverse computed.",
        "formula": "WF=sum_(n=p^m,log n<L) log(p)/sqrt(2n) [g(x+r/2-log n)+g(x-r/2+log n)]",
        "centered_interval": "[-L/2,L/2], L=r+1/2",
        "g0_norm_sq_exact": f"{NORM_NUM}/{NORM_DEN}",
        "normalization_quad16_diagnostic": normalized_probe_sq_check,
        "raw_integrand_degree_per_piece": 30,
        "raw_gauss16": "Exact for degree <=31 in ideal real arithmetic; finite floating evaluation is not an enclosure.",
        "moment_orders": [24, 32],
        "all_polynomial_breakpoints_used": True,
        "script_sha256": source_hash,
        "python_version": platform.python_version(),
        "numpy_version": np.__version__,
        "preflight": preflight,
        "runtime_seconds": time.perf_counter() - started,
        "results": rows,
    }
    (ROOT / "record.json").write_text(json.dumps(record, indent=2) + "\n")
    print("r  pp  pieces  raw_norm_sq  projected_norm_sq  retained_fraction  projected/r^2")
    for row in rows:
        print(f'{row["r"]}  {row["prime_power_count"]}  {row["piece_count"]}  '
              f'{row["raw_norm_sq_16"]:.12g}  '
              f'{row["projected_norm_sq_raw16_moment32"]:.12g}  '
              f'{row["retained_fraction_raw16_moment32"]:.12g}  '
              f'{row["projected_norm_sq_over_r2"]:.12g}')
    print(f'Runtime: {record["runtime_seconds"]:.3f} seconds')
    print(f'Probe norm-squared check: {normalized_probe_sq_check:.17g}')


if __name__ == "__main__":
    run()
