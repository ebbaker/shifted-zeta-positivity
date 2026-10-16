#!/usr/bin/env python3
"""Floating diagnostics for exact Mobius/cofactor and Vaughan reductions.

No interval certification or asymptotic exponent inference. NumPy only.
Run from any directory; output is a small JSON record, with no saved sieve.
"""
import argparse
import hashlib
import json
import math
import platform
from pathlib import Path

import numpy as np
from numpy.polynomial.legendre import leggauss

A, B = math.exp(-0.25), math.exp(0.25)
NU = 146640624550936576 / 37921101075


def weight(t):
    out = np.zeros_like(t, dtype=float)
    active = (t > A) & (t < B)
    v = -np.log(t[active])
    q = 1 - 16 * v * v
    g0 = -64 * v * q**5 * (2688 * (1 - 80 * v * v) + q * q)
    out[active] = g0 / np.sqrt(NU * t[active])
    return out


def sieve(limit):
    prime = np.ones(limit + 1, dtype=bool)
    prime[:2] = False
    for p in range(2, math.isqrt(limit) + 1):
        if prime[p]:
            prime[p * p::p] = False
    primes = np.flatnonzero(prime)
    mu = np.ones(limit + 1, dtype=np.int8)
    mu[0] = 0
    lam = np.zeros(limit + 1)
    for p in primes:
        p = int(p)
        mu[p::p] *= -1
        if p * p <= limit:
            mu[p * p::p * p] = 0
        power = p
        while power <= limit:
            lam[power] = math.log(p)
            power *= p
    return mu, lam


def evaluate(X, nodes, cutoff_factor, mu_all, lam_all, logmoment):
    N = math.floor(2 * B * X)
    n = np.arange(N + 1, dtype=float)
    mu, lam = mu_all[:N + 1], lam_all[:N + 1]
    logs = np.log(np.maximum(1, n))
    mobius_log = -mu * logs
    cutoff = cutoff_factor * X**(11 / 12) / math.log(X)**(1 / 6)
    D = math.floor(cutoff)
    K = N // (D + 1)
    low = np.zeros(N + 1)
    for d in range(2, D + 1):
        if mu[d]:
            low[d::d] += mobius_log[d]
    high = np.zeros(N + 1)
    for k in range(1, K + 1):
        high[k * (D + 1)::k] += mobius_log[D + 1:N // k + 1]
    convolution_error = float(np.max(np.abs(low + high - lam)))

    U = math.floor(X**(11 / 24))
    a = np.zeros(N + 1, dtype=np.int32)
    for d in range(1, U + 1):
        if mu[d]:
            a[d::d] -= int(mu[d])
    a[:U + 1] = 0
    bilinear = np.zeros(N + 1)
    for ell in np.flatnonzero(lam[U + 1:N // (U + 1) + 1]) + U + 1:
        ell = int(ell)
        bilinear[ell * (U + 1)::ell] += lam[ell] * a[U + 1:N // ell + 1]
    reciprocal_mu = float(np.sum(mu[1:U + 1] / n[1:U + 1]))
    continuum_coefficient = logmoment * reciprocal_mu

    z, wz = leggauss(nodes)
    xs = X * (1.5 + z / 2)
    quadrature_weights = X * wz / 2
    components = np.zeros((nodes, K))
    exact_v, low_v, type2_v = (np.zeros(nodes) for _ in range(3))
    for i, x in enumerate(xs):
        values = weight(n / x)
        exact_v[i] = np.sum(lam * values)
        low_v[i] = np.sum(low * values)
        type2_v[i] = np.sum(bilinear * values)
        for k in range(1, K + 1):
            components[i, k - 1] = np.sum(
                mobius_log[D + 1:N // k + 1] * values[k * (D + 1)::k])

    def energy(v):
        return float(np.sum(quadrature_weights * v * v))

    high_v = np.sum(components, axis=1)
    gram = components.T @ (quadrature_weights[:, None] * components)
    gram_diag = float(np.trace(gram))
    high_energy = energy(high_v)
    xx = (7 / 3) * X**3
    projection = float(np.sum(quadrature_weights * type2_v * xs) / xx)
    shape = energy(type2_v - projection * xs)
    mismatch = projection + continuum_coefficient
    centered = type2_v + continuum_coefficient * xs
    centered_energy = energy(centered)
    rank_split_error = abs(centered_energy - shape - xx * mismatch * mismatch)
    return {
        "X": X, "nodes": nodes, "cutoff_factor": cutoff_factor,
        "D": D, "K": K, "U_equals_V": U,
        "coefficient_identity_max_absolute_error": convolution_error,
        "response_identity_max_absolute_error": float(np.max(np.abs(exact_v - low_v - high_v))),
        "variance_over_X2": energy(exact_v) / X**2,
        "low_divisor_energy_over_X2": energy(low_v) / X**2,
        "cofactor_energy_over_X2": high_energy / X**2,
        "cofactor_diagonal_over_X2": gram_diag / X**2,
        "cofactor_offdiagonal_over_X2": (high_energy - gram_diag) / X**2,
        "cofactor_signed_to_diagonal_ratio": high_energy / gram_diag,
        "cofactor_component_energies_over_X2": (np.diag(gram) / X**2).tolist(),
        "vaughan_remainder_energy_over_X2": energy(exact_v - centered) / X**2,
        "centered_type2_energy_over_X2": centered_energy / X**2,
        "type2_shape_energy_over_X2": shape / X**2,
        "type2_scalar_mismatch_energy_over_X2": xx * mismatch**2 / X**2,
        "type2_rank_one_split_absolute_error": rank_split_error,
        "mu_reciprocal_sum": reciprocal_mu,
        "type2_fitted_linear_coefficient": projection,
        "type1_continuum_coefficient": continuum_coefficient,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--scales", nargs="+", type=float,
                        default=[1000.25, 3000.5, 10000.25, 30000.5, 100000.25, 300000.5])
    parser.add_argument("--nodes", nargs="+", type=int, default=[128, 256])
    parser.add_argument("--cutoff-factor", type=float, default=0.25)
    args = parser.parse_args()
    assert min(args.scales) > math.e and 0 < args.cutoff_factor <= 1
    mu, lam = sieve(math.floor(2 * B * max(args.scales)))
    z, wz = leggauss(128)
    t = (A + B) / 2 + (B - A) * z / 2
    logmoment = float((B - A) / 2 * np.sum(wz * weight(t) * np.log(t)))
    results = []
    for X in args.scales:
        for nodes in args.nodes:
            row = evaluate(X, nodes, args.cutoff_factor, mu, lam, logmoment)
            results.append(row)
            print(f"X={X:g}, nodes={nodes}: variance/X2={row['variance_over_X2']:.10g}, "
                  f"K={row['K']}, signed/diagonal={row['cofactor_signed_to_diagonal_ratio']:.6g}", flush=True)
    out = {
        "date": "2026-10-04", "status": "FLOATING_DIAGNOSTIC_NOT_CERTIFICATE",
        "model": "GPT-6 (Codex), inherited configuration; serving variant and effort not exposed",
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "python": platform.python_version(), "numpy": np.__version__,
        "weight_log_moment": logmoment, "rows": results,
        "limitations": [
            "Finite floating quadrature, not outward interval certification.",
            "No global exponent or asymptotic slope inferred.",
            "Quadrature node refinement checks discretization, not a rigorous error bound.",
            "Gram entries retain signs; diagonal-only estimates do not bound their sum.",
        ],
    }
    args.output.write_text(json.dumps(out, indent=2) + "\n")


if __name__ == "__main__":
    main()
