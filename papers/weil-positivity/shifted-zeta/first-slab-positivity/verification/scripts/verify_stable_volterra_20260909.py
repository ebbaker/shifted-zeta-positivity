#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Edward B. Baker III
"""Stable numerical diagnostics for the first-slab impulse and finite sections.

Repairs the singular-kernel sampling and float-overflow failures in the A4
portion of verify_preprint_checks_20260905.py. The historical file is retained.
This script is ordinary numerical verification, not an interval certificate
or a proof of infinite-dimensional contractivity. It does not replace the
historical A1--A3 checks or its exploratory Suzuki-normalization comparisons.

The normalized piecewise-constant Galerkin matrix uses exact triangular
overlap weights. Gauss--Jacobi quadrature handles the t**(omega-1) endpoint
singularity. H and V use separate sum/difference index rules with shared
scalar integrals, so their algebra checks test coordinate consistency, not
independent reconstruction of the kernel. A two-resolution compression check
and a doubled-quadrature check test the integration separately.

Run: python3 verify_stable_volterra_20260909.py
Dependencies: mpmath, numpy, scipy (see requirements_stable_checks.txt).
"""

from __future__ import annotations

import argparse
from functools import lru_cache
import math

import mpmath as mp
import numpy as np
from scipy.special import beta, betainc, gamma, roots_jacobi, roots_legendre


def impulse_float(t: np.ndarray, omega: float) -> np.ndarray:
    """Evaluate at strictly positive quadrature nodes inside [0, log 2]."""
    if np.any(t <= 0):
        raise ValueError("The impulse is singular at zero: integrate it instead.")
    alpha = 0.5 - omega
    q = -np.expm1(-2 * t)
    first = 2 * np.exp(-alpha * t) * q ** (omega - 1) / gamma(omega)
    # Avoid beta(omega, 0) at the endpoint: its entire coefficient is zero.
    second = np.zeros_like(t)
    if alpha != 0:
        incomplete = beta(omega, alpha) * betainc(omega, alpha, q)
        second = 4 * alpha * omega * np.exp(alpha * t) * incomplete / gamma(omega)
    third = (
        4 * (0.5 + omega) * omega * np.exp(-alpha * t)
        * q ** omega / gamma(omega + 1)
    )
    return math.pi ** omega * (first - second - third)


@lru_cache(maxsize=None)
def scalar_overlap(d: int, n: int, omega: float, order: int) -> float:
    """Integral of kappa(t) * max(0, 1-|t/h-d|), restricted to t>=0."""
    if d < 0:
        return 0.0
    h = math.log(2) / n
    result = 0.0
    for lo, hi in ((max(0, d - 1) * h, d * h), (d * h, (d + 1) * h)):
        if hi <= lo:
            continue
        if lo == 0:
            nodes, weights = roots_jacobi(order, 0.0, omega - 1)
            t = hi * (nodes + 1) / 2
            overlap = np.maximum(0, 1 - np.abs(t / h - d))
            regular_part = impulse_float(t, omega) * t ** (1 - omega)
            result += (hi / 2) ** omega * float(weights @ (regular_part * overlap))
        else:
            nodes, weights = roots_legendre(order)
            t = (lo + hi) / 2 + (hi - lo) * nodes / 2
            overlap = np.maximum(0, 1 - np.abs(t / h - d))
            result += (hi - lo) / 2 * float(weights @ (impulse_float(t, omega) * overlap))
    return result


def galerkin(n: int, omega: float, order: int) -> tuple[np.ndarray, np.ndarray]:
    # Indices, not floating comparisons at x+y=L, decide causality.
    v = np.array([[scalar_overlap(i-j, n, omega, order) for j in range(n)] for i in range(n)])
    h = np.array([[scalar_overlap(i+j+1-n, n, omega, order) for j in range(n)] for i in range(n)])
    return v, h


def damped_impulse(t: mp.mpf, omega: mp.mpf, p: mp.mpf) -> mp.mpf:
    """e**(-p*t) * kappa(t), combining exponents before evaluation."""
    alpha = mp.mpf("0.5") - omega
    q = -mp.expm1(-2 * t)
    first = 2 * mp.exp(-(p+alpha)*t) * q ** (omega-1) / mp.gamma(omega)
    second = mp.mpf(0)
    if alpha:
        second = (
            4 * alpha * omega * mp.exp(-(p-alpha)*t)
            * mp.betainc(omega, alpha, 0, q) / mp.gamma(omega)
        )
    third = (
        4 * (mp.mpf("0.5")+omega) * omega * mp.exp(-(p+alpha)*t)
        * q ** omega / mp.gamma(omega+1)
    )
    return mp.pi ** omega * (first-second-third)


def laplace_impulse(omega: mp.mpf, p: mp.mpf) -> mp.mpf:
    if p <= abs(mp.mpf("0.5")-omega):
        raise ValueError("p must lie to the right of the impulse's growth rate")

    def transformed(u: mp.mpf) -> mp.mpf:
        # t=u**(1/omega): remove the singularity, with its exact endpoint limit.
        if not u:
            return (2*mp.pi) ** omega / mp.gamma(omega+1)
        t = u ** (1/omega)
        return damped_impulse(t, omega, p) * t / (omega*u)

    return mp.quad(transformed, [0, mp.mpf("0.25"), 1]) + mp.quad(
        lambda t: damped_impulse(t, omega, p), [1, 3, 8, mp.inf]
    )


def completed_gamma(s: mp.mpf) -> mp.mpf:
    return s * (s-1) * mp.pi ** (-s/2) * mp.gamma(s/2) / 2


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dps", type=int, default=50)
    args = parser.parse_args()
    if args.dps < 40:
        parser.error("--dps must be at least 40 for the stated Laplace tolerances")
    mp.mp.dps = args.dps
    outcomes: list[bool] = []

    def check(label: str, condition: bool, detail: str = "") -> None:
        ok = bool(condition)
        outcomes.append(ok)
        print(f"{'PASS' if ok else 'FAIL'} {label}" + (f": {detail}" if detail else ""), flush=True)

    for omega in (0.3, 0.5):
        v, h = galerkin(16, omega, 48)
        v_hi, h_hi = galerkin(16, omega, 96)
        v_fine, _ = galerkin(32, omega, 96)
        check(f"finite Galerkin entries, omega={omega}",
              np.isfinite(v).all() and np.isfinite(h).all())
        r = np.fliplr(np.eye(16))
        identity_error = max(
            np.max(np.abs(h-v@r)), np.max(np.abs(h-r@v.T)),
            np.max(np.abs(r@v@r-v.T)), np.max(np.abs(h@h-v@v.T)),
            np.max(np.abs(h-h.T)),
        )
        check(f"finite-section Volterra/reflection algebra, omega={omega}",
              identity_error < 1e-12, f"maximum discrepancy {identity_error:.3e}")
        error = max(np.max(np.abs(v-v_hi)), np.max(np.abs(h-h_hi)))
        check(f"48/96-node convergence, omega={omega}", error < 2e-11,
              f"maximum entry discrepancy {error:.3e}")
        injection = np.zeros((32, 16))
        for j in range(16):
            injection[2*j:2*j+2, j] = 1/math.sqrt(2)
        error = np.max(np.abs(v_hi-injection.T@v_fine@injection))
        check(f"16/32-cell compression consistency, omega={omega}", error < 2e-11,
              f"maximum entry discrepancy {error:.3e}")
        nv = float(np.linalg.svd(v_hi, compute_uv=False)[0])
        nh = float(np.max(np.abs(np.linalg.eigvalsh(h_hi))))
        check(f"sampled finite-section norm agreement, omega={omega}", abs(nv-nh) < 1e-12,
              f"||V_16||={nv:.12f}, ||H_16||={nh:.12f}")
        check(f"sampled finite-section norm below one, omega={omega}", nv < 1,
              "a diagnostic for this finite matrix only")

    for omega_s in ("0.3", "0.5"):
        for p_s in ("1.7", "2.3"):
            omega, p = mp.mpf(omega_s), mp.mpf(p_s)
            observed = laplace_impulse(omega, p)
            target = completed_gamma(mp.mpf("0.5")+p-omega) / completed_gamma(mp.mpf("0.5")+p+omega)
            error = abs(observed-target)
            check(f"Laplace impulse = gamma transfer, omega={omega_s}, p={p_s}",
                  mp.isfinite(observed) and error < mp.mpf("1e-25"),
                  f"absolute discrepancy {mp.nstr(error, 8)}")

    print(f"{sum(outcomes)}/{len(outcomes)} checks passed. Numerical diagnostics only.", flush=True)
    return 0 if all(outcomes) else 1


if __name__ == "__main__":
    raise SystemExit(main())
