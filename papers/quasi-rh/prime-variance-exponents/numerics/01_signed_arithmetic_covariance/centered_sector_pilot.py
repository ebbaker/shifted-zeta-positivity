#!/usr/bin/env python3
"""Complete capped semiprime/smooth/prime-power diagnostic; no exponent fit.

Substantial LLM assistance, GPT-6 (Codex), inherited configuration.
Uses the established fixed probe and NumPy. Only small summaries are saved.
"""
import argparse
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import platform

import numpy as np
from numpy.polynomial.legendre import leggauss

PROBE = Path(__file__).resolve().parents[1] / "mobius_reduction_20261004/pilot.py"
spec = importlib.util.spec_from_file_location("probe", PROBE)
probe = importlib.util.module_from_spec(spec)
spec.loader.exec_module(probe)


def coefficients(X):
    N = math.floor(2 * probe.B * X)
    U = math.floor(X**(11 / 24))
    cap = N // (U + 1)
    assert cap < (U + 1)**2, "The large-prime support argument needs this cap."
    mu, lam = probe.sieve(N)
    prime = np.ones(N + 1, dtype=bool)
    prime[:2] = False
    for p in range(2, math.isqrt(N) + 1):
        if prime[p]:
            prime[p*p::p] = False
    primes = np.flatnonzero(prime)
    a = np.zeros(cap + 1, dtype=np.int64)
    for d in range(U + 1, cap + 1):
        a[d::d] += int(mu[d])
    smooth = np.ones(cap + 1, dtype=bool)
    for p in primes[(primes > U) & (primes <= cap)]:
        smooth[p::p] = False
    exceptional = [m for m in range(U + 1, cap + 1)
                   if not smooth[m] and a[m] != (-1 if prime[m] else 0)]
    assert not exceptional

    whole = np.zeros(N + 1)
    smooth_prime = np.zeros(N + 1)
    inner_power = np.zeros(N + 1)
    for n in np.flatnonzero(lam[U + 1:cap + 1]) + U + 1:
        ms = np.arange(U + 1, N // n + 1)
        terms = a[ms] * lam[n]
        whole[n * ms] += terms
        if prime[n]:
            chosen = smooth[ms]
            smooth_prime[n * ms[chosen]] += terms[chosen]
        else:
            inner_power[n * ms] += terms

    # Independently assemble semiprime coefficients from unordered prime pairs.
    semiprime = np.zeros(N + 1)
    ps = primes[(primes > U) & (primes <= cap)]
    for i, p in enumerate(ps):
        qs = ps[i:]
        qs = qs[qs <= N // p]
        if not len(qs):
            break
        semiprime[p * qs] -= math.log(int(p)) + np.log(qs)
        if qs[0] == p:
            semiprime[p * p] += math.log(int(p))
    error = float(np.max(np.abs(whole - semiprime - smooth_prime - inner_power)))
    assert error < 1e-10
    return U, cap, mu, lam, np.stack((semiprime, smooth_prime, inner_power)), error


def evaluate(X, nodes):
    U, cap, mu, lam, coeff, error = coefficients(X)
    n = np.arange(len(lam), dtype=float)
    z, wz = leggauss(nodes)
    xs, weights = X * (1.5 + z / 2), X * wz / 2
    tz, tw = leggauss(128)
    ts = (probe.A + probe.B) / 2 + (probe.B - probe.A) * tz / 2
    cw = float((probe.B - probe.A) / 2 * np.sum(tw * probe.weight(ts) * np.log(ts)))
    continuum = cw * float(np.sum(mu[1:U + 1] / n[1:U + 1]))
    values = np.zeros((nodes, 4))
    original = np.zeros(nodes)
    for i, x in enumerate(xs):
        w = probe.weight(n / x)
        values[i, :3] = coeff @ w
        values[i, 3] = continuum * x
        original[i] = lam @ w
    gram = values.T @ (weights[:, None] * values)
    xx = (7 / 3) * X**3
    slopes = values.T @ (weights * xs) / xx
    total = values.sum(axis=1)
    norm = lambda v: float(np.sum(weights * v * v))
    mismatch = float(slopes.sum())
    shape = norm(total - mismatch * xs)
    scalar = xx * mismatch**2
    predicted_semislope = -cw / ((1 - 11/24) * math.log(X))
    return {
        "X": X, "nodes": nodes, "U_equals_V": U, "max_outer_factor": cap,
        "large_prime_classification_failures": 0,
        "coefficient_decomposition_error": error,
        "sector_order": ["semiprime", "smooth_outer_prime_inner", "inner_higher_prime_power", "continuum"],
        "sector_slopes": slopes.tolist(),
        "sector_energy_over_X2": (np.diag(gram) / X**2).tolist(),
        "semiprime_smooth_cross_over_X2": float(2 * gram[0, 1] / X**2),
        "all_cross_terms_over_X2": float((gram.sum() - np.trace(gram)) / X**2),
        "continuum_coefficient": continuum,
        "predicted_leading_semiprime_slope": predicted_semislope,
        "semiprime_slope_to_leading_term": float(slopes[0] / predicted_semislope),
        "complete_centered_energy_over_X2": norm(total) / X**2,
        "projected_shape_over_X2": shape / X**2,
        "scalar_mismatch_energy_over_X2": scalar / X**2,
        "scalar_mismatch": mismatch,
        "original_variance_over_X2": norm(original) / X**2,
        "vaughan_remainder_energy_over_X2": norm(original - total) / X**2,
        "orthogonal_split_residual_over_X2": abs(norm(total) - shape - scalar) / X**2,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--scales", type=float, nargs="+", default=[10000.5, 100000.25])
    parser.add_argument("--nodes", type=int, nargs="+", default=[128, 256])
    args = parser.parse_args()
    assert min(args.scales) > 10 and min(args.nodes) >= 16
    rows = [evaluate(X, nodes) for X in args.scales for nodes in args.nodes]
    assert max(r["orthogonal_split_residual_over_X2"] for r in rows) < 1e-9
    record = {
        "date": "2026-10-04", "status": "FLOATING_DIAGNOSTIC_NOT_CERTIFICATE",
        "assistance": "Substantial LLM assistance; GPT-6 (Codex), inherited configuration; exact serving variant and effort not inferred.",
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "probe_sha256": hashlib.sha256(PROBE.read_bytes()).hexdigest(),
        "python": platform.python_version(), "numpy": np.__version__, "rows": rows,
        "limitations": ["No interval enclosure or asymptotic exponent fit.",
                        "Quadrature refinement is diagnostic, not a rigorous error bound.",
                        "All arrays discarded; only small summaries retained."]
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps({"runs": len(rows), "max_coefficient_error": max(r["coefficient_decomposition_error"] for r in rows),
                      "max_split_error_over_X2": max(r["orthogonal_split_residual_over_X2"] for r in rows)}))


if __name__ == "__main__":
    main()
