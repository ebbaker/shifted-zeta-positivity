#!/usr/bin/env python3
"""Small exact-rational controls; no theta acquisition or endpoint certificate.
Prepared for Edward Baker with LLM assistance, gpt-6-astra, effort ultra,
22 October 2026. Written proofs remain in Notes 03 and 04.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json


def run():
    # Independent evaluations of generic phase-current and source formulas.
    phase_checks = 0
    for h, hx, hxx, hxxx in [(2, 3, -5, 7), (-3, 2, 4, -9), (5, 0, -2, 1), (1, -4, 6, 3)]:
        h, hx, hxx, hxxx = map(F, (h, hx, hxx, hxxx))
        p = hx / h
        Q = hx * hx - h * hxx
        Qx = hx * hxx - h * hxxx
        E = h * h + hx * hx
        qx = Qx / (h * h) - 2 * Q * hx / (h ** 3)
        c0, s1, c2, s3 = h, -hx, -hxx, hxxx
        source = (2*s1**3 + 3*c0*s1*c2 - c0**2*s3)/(c0*(c0**2+s1**2))
        assert (Qx - 2*p*Q)/E == qx/(1+p*p) == source
        assert Qx/Q - 2*p == qx/(Q/h**2)
        phase_checks += 1
    # Quadratic invariant C^2=x(t-x^2/10)^2: derivative along x'=4x/(x^2-2t).
    for t, x in [(F(1), F(1,2)), (F(2), F(3,2)), (F(1,2), F(1,3))]:
        v = 4*x/(x*x-2*t)
        z = t-x*x/10
        partial_t = 2*x*z
        partial_x = z*z - F(2,5)*x*x*z
        assert partial_t + v*partial_x == 0
        q = 2*(x*x+2*t)/(x*x-2*t)**2
        assert q >= 1/t
    # T=1/2, epsilon=s^2/2 removes radicals from the survivor polynomial.
    rows = []
    T = F(1,2)
    for s in [F(1,2), F(1,4), F(1,8), F(1,16)]:
        rhs = F(4,25)*s**5
        def f(r):
            return r*(T-r*r/10)**2-rhs
        lo, hi = F(0), F(1)
        for _ in range(100):
            mid = (lo+hi)/2
            if f(mid) < 0:
                lo = mid
            else:
                hi = mid
        leading = F(16,25)*s**5
        assert f(lo) <= 0 <= f(hi)
        assert lo >= leading
        assert hi <= s**5  # bound (8), with L=K=0
        rows.append({"s": str(s), "epsilon": str(s*s/2),
                     "r_lower": str(lo), "r_upper": str(hi),
                     "r_over_leading_display": float((lo+hi)/(2*leading))})
    return {"date": "2026-10-22", "author": "Prepared for Edward Baker",
            "llm_assistance": True, "model": "gpt-6-astra", "effort": "ultra",
            "scope": "Exact rational control checks and quadratic root brackets only; not theta data, a general proof, or independent review.",
            "phase_identity_spot_checks": phase_checks,
            "quadratic_invariant_spot_checks": 3,
            "quadratic_survivor_brackets": rows,
            "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "status": "passed"}


if __name__ == "__main__":
    out = Path(__file__).with_name('ICW_ANALYTIC_CHECKS_20261022.json')
    out.write_text(json.dumps(run(), indent=2) + '\n')
    print(json.dumps({"status": "passed", "receipt": str(out)}))
