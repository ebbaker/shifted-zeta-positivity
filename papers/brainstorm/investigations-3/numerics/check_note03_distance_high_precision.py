#!/usr/bin/env python3
"""Independent mpmath quadrature spot-check. JSON stdout; no file writes.

16 October 2026. Prepared for Edward Baker with LLM assistance.
Coordinating model gpt-6-astra (Codex), reasoning effort ultra.

Requires mpmath. All results are high-precision floating, not certificates.
"""
import hashlib
from pathlib import Path
import json
import platform
import sys
import mpmath as mp

mp.mp.dps = 60
BREAKS = [mp.mpf(x) for x in ("0", ".1", ".3", ".5", ".8", "1", "1.2", "1.5", "1.8")]


def transform(n, t, x, deriv):
    def integrand(u):
        q = mp.pi * n**2 * mp.exp(4*u)
        source = (2*q*q-3*q)*mp.exp(u-q)
        oscillation = mp.cos(x*u) if deriv == 0 else -u*mp.sin(x*u)
        return mp.exp(t*u*u)*source*oscillation
    return mp.quad(integrand, BREAKS)


def fmt(x):
    return mp.nstr(x, 48)


rows = []
for ts, xs in ((".25", "44.1303"), ("0", "60")):
    t, x = mp.mpf(ts), mp.mpf(xs)
    matrix = mp.matrix([[transform(n, t, x, j) for n in range(1, 7)] for j in (0, 1)])
    a = matrix[:, :2]
    tail = mp.matrix([sum(matrix[j, n] for n in range(2, 6)) for j in (0, 1)])
    weights = mp.lu_solve(a, -tail)
    h = mp.matrix([sum(matrix[j, n] for n in range(6)) for j in (0, 1)])
    row = {"t": ts, "x": xs, "N": 2,
           "columns_first_six": [[fmt(matrix[j, n]) for n in range(6)] for j in (0, 1)],
           "theta_jet_truncated_at_six": [fmt(v) for v in h],
           "perturbed_weights": [fmt(v) for v in weights],
           "distance": fmt(mp.sqrt(sum((v-1)**2 for v in weights))),
           "linear_residual": [fmt(v) for v in a*weights+tail]}
    if t == 0:
        s = mp.mpf('.5')+1j*x/2
        zeta_value = s*(s-1)*mp.power(mp.pi, -s/2)*mp.gamma(s/2)*mp.zeta(s)/16
        row["xi_over_eight_real"] = fmt(mp.re(zeta_value))
        row["theta_transform_minus_xi_over_eight"] = fmt(h[0]-mp.re(zeta_value))
    rows.append(row)

print(json.dumps({
    "status": "60-decimal mpmath floating quadrature check; not interval-certified",
    "date": "2026-10-16 America/New_York",
    "prepared_for": "Edward Baker",
    "coordinating_model": "gpt-6-astra (Codex)",
    "reasoning_effort": "ultra",
    "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "environment": {"python": sys.version, "mpmath": mp.__version__, "platform": platform.platform()},
    "params": {"decimal_precision": 60, "nmax": 6, "integration_breaks": [str(v) for v in BREAKS],
               "method": "mpmath tanh-sinh quadrature, independent elementary source implementation"},
    "limits": "Source is cut at n=6 and u=1.8 without interval tail certification. No theorem is inferred from the displayed digits.",
    "rows": rows,
}, indent=2))
