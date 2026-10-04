#!/usr/bin/env python3
"""Small complete-cap diagnostics; no interval certificate or exponent fit.

Reuses the established fixed probe and sieve, but assembles block coefficients
and projected Gram matrices here. Run from any working directory.
"""
import argparse
import hashlib
import importlib.util
import json
import math
import platform
from pathlib import Path

import numpy as np
from numpy.polynomial.legendre import leggauss

BASE = Path(__file__).resolve().parents[1]
PROBE_SOURCE = BASE / "mobius_reduction_20261004/pilot.py"
spec = importlib.util.spec_from_file_location("established_probe", PROBE_SOURCE)
probe = importlib.util.module_from_spec(spec)
spec.loader.exec_module(probe)


def blocks(top):
    """Disjoint integer blocks, including the final partial block."""
    lo = 1
    while lo <= top:
        hi = min(2 * lo - 1, top)
        yield lo, hi
        lo *= 2


def evaluate(X, nodes):
    N = math.floor(2 * probe.B * X)
    n = np.arange(N + 1, dtype=float)
    mu, lam = probe.sieve(N)
    logs = np.log(np.maximum(n, 1))
    D = math.floor(X**0.9)
    K = N // (D + 1)
    spans = list(blocks(K))
    cofactor = np.zeros((len(spans), N + 1))
    for j, (lo, hi) in enumerate(spans):
        for k in range(lo, hi + 1):
            ds = np.arange(D + 1, N // k + 1)
            cofactor[j, k * ds] -= mu[ds] * logs[ds]
    low = np.zeros(N + 1)
    for d in range(2, D + 1):
        low[d::d] -= mu[d] * logs[d]

    U = math.floor(X**(11 / 24))
    a = np.zeros(N + 1, dtype=np.int64)
    for d in range(U + 1, N + 1):
        if mu[d]:
            a[d::d] += int(mu[d])
    mspans = [(lo, hi) for lo, hi in blocks(N // (U + 1)) if hi > U]
    vaughan = np.zeros((len(mspans), N + 1))
    for j, (lo, hi) in enumerate(mspans):
        for m in range(max(lo, U + 1), hi + 1):
            if a[m]:
                ns = np.arange(U + 1, N // m + 1)
                vaughan[j, m * ns] += a[m] * lam[ns]

    z, wz = leggauss(nodes)
    xs, qw = X * (1.5 + z / 2), X * wz / 2
    W = np.array([probe.weight(n / x) for x in xs])
    prime_response = W @ lam
    cofactor_response = W @ cofactor.T
    vaughan_response = W @ vaughan.T
    tz, tw = leggauss(128)
    ts = (probe.A + probe.B) / 2 + (probe.B - probe.A) * tz / 2
    cw = float((probe.B - probe.A) / 2 * np.sum(tw * probe.weight(ts) * np.log(ts)))
    c = cw * float(np.sum(mu[1:U + 1] / n[1:U + 1]))

    def energy(v):
        return float(np.sum(qw * v * v))

    def gram_record(response, continuum):
        gram = response.T @ (qw[:, None] * response)
        xx = (7 / 3) * X**3
        slopes = response.T @ (qw * xs) / xx
        residual = response - xs[:, None] * slopes[None, :]
        projected = residual.T @ (qw[:, None] * residual)
        total = np.sum(response, axis=1) + continuum * xs
        shape = float(np.sum(projected))
        scalar = xx * (float(np.sum(slopes)) + continuum)**2
        return {
            "gram_trace_over_X2": float(np.trace(gram)) / X**2,
            "gram_offdiagonal_sum_over_X2": float(np.sum(gram) - np.trace(gram)) / X**2,
            "projected_trace_over_X2": float(np.trace(projected)) / X**2,
            "projected_offdiagonal_sum_over_X2": float(np.sum(projected) - np.trace(projected)) / X**2,
            "block_slopes": slopes.tolist(),
            "continuum_coefficient": continuum,
            "shape_over_X2": shape / X**2,
            "scalar_over_X2": scalar / X**2,
            "whole_energy_over_X2": energy(total) / X**2,
            "split_residual_over_X2": abs(energy(total) - shape - scalar) / X**2,
            "rank_one_matrix_residual_over_X2": float(np.max(np.abs(
                gram - projected - xx * np.outer(slopes, slopes)))) / X**2,
        }

    # Local Euler-place identity, tested on coefficient arrays, not quadrature.
    euler_errors = {}
    for p in (2, 3):
        lhs = np.zeros(N + 1)
        rhs = np.zeros(N + 1)
        for d in range(D + 1, N + 1):
            lhs[d] = mu[d] * logs[d]
            if d % p:
                rhs[d] += mu[d] * logs[d]
        for e in range(math.floor(D / p) + 1, N // p + 1):
            if e % p:
                rhs[p * e] -= mu[e] * (logs[e] + math.log(p))
        euler_errors[str(p)] = float(np.max(np.abs(lhs - rhs)))

    out = {
        "X": X, "nodes": nodes, "D": D, "K": K, "U_equals_V": U,
        "cofactor_blocks_inclusive": spans, "vaughan_m_blocks_inclusive": mspans,
        "coefficient_identity_max_error": float(np.max(np.abs(lam - low - cofactor.sum(axis=0)))),
        "euler_place_coefficient_errors": euler_errors,
        "variance_over_X2": energy(prime_response) / X**2,
        "cofactor_remainder_over_X2": energy(prime_response - cofactor_response.sum(axis=1)) / X**2,
        "vaughan_remainder_over_X2": energy(prime_response - vaughan_response.sum(axis=1) - c * xs) / X**2,
        "cofactor": gram_record(cofactor_response, 0.0),
        "vaughan": gram_record(vaughan_response, c),
    }
    assert out["coefficient_identity_max_error"] < 1e-10
    assert max(euler_errors.values()) < 1e-10
    for name in ("cofactor", "vaughan"):
        assert out[name]["split_residual_over_X2"] < 1e-8
        assert out[name]["rank_one_matrix_residual_over_X2"] < 1e-8
    return out


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--scales", type=float, nargs="+", default=[1000.25, 10000.5])
    parser.add_argument("--nodes", type=int, nargs="+", default=[128, 256])
    args = parser.parse_args()
    assert min(args.scales) > 10 and min(args.nodes) >= 16
    rows = [evaluate(X, nodes) for X in args.scales for nodes in args.nodes]
    record = {
        "date": "2026-10-04", "status": "FLOATING_DIAGNOSTIC_NOT_CERTIFICATE",
        "assistance": "Substantial LLM assistance; GPT-6 (Codex), inherited configuration; exact serving variant and effort not inferred.",
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "probe_source_sha256": hashlib.sha256(PROBE_SOURCE.read_bytes()).hexdigest(),
        "python": platform.python_version(), "numpy": np.__version__, "rows": rows,
        "limitations": ["Finite quadrature is not outward certification.",
                        "No fitted exponent or global saving.",
                        "Only small diagnostic summaries retained; matrices and sieves are not stored."]
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps({"rows": len(rows), "max_identity_error": max(r["coefficient_identity_max_error"] for r in rows),
                      "max_split_error_over_X2": max(r[k]["split_residual_over_X2"] for r in rows for k in ("cofactor", "vaughan"))}))


if __name__ == "__main__":
    main()
