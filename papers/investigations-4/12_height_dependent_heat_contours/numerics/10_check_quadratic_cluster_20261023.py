#!/usr/bin/env python3
"""Exact finite-polynomial diagnostic for the quadratic exterior comparison.

Prepared for Edward Baker, 23 October 2026 (America/New_York).
LLM assistance: gpt-6-astra (Codex), recorded reasoning effort ultra.
This is an information-class control, not a computation of theta zeros.
"""
from decimal import Decimal, localcontext
from fractions import Fraction
import json
from pathlib import Path


def exact_ratio(m, n, s, radius_squared):
    # E[u^(m+2j)] / E[u^m] = (2s)^j product_{h=1}^j(m+2h-1).
    term = Fraction(1)
    total = term
    for j in range(1, n + 1):
        term *= -Fraction(n - j + 1, j) * 2 * s * (m + 2*j - 1) / radius_squared
        total += term
    return total


def dec(x):
    return Decimal(x.numerator) / Decimal(x.denominator)


def main():
    rows = []
    with localcontext() as ctx:
        ctx.prec = 90
        for ell in (16, 32, 64, 128, 256):
            m = n = ell
            s = Fraction(1, ell*ell)
            radius_squared = Fraction(4)
            full = exact_ratio(m, n, s, radius_squared)
            d = 1 + 4*s*n/radius_squared
            quadratic_squared = d ** (-m-1)
            quadratic = dec(quadratic_squared).sqrt()
            full_decimal = dec(full)
            # Exact positivity check for this finite control; not a uniform theorem.
            assert 0 < full < 1
            rows.append({
                "L": ell, "m": m, "n": n, "s": str(s), "R": 2,
                "exact_full_over_linear": str(full),
                "exact_quadratic_ratio_squared": str(quadratic_squared),
                "full_over_linear_decimal": str(full_decimal),
                "quadratic_over_linear_decimal": str(quadratic),
                "relative_quadratic_error_decimal": str(abs(full_decimal/quadratic-1)),
                "linear_error_decimal": str(abs(full_decimal-1)),
            })
        limit = str(Decimal('-0.5').exp())
    record = {
        "date": "2026-10-23", "timezone": "America/New_York",
        "prepared_for": "Edward Baker", "model": "gpt-6-astra (Codex)",
        "reasoning_effort": "ultra",
        "purpose": "Check the finite real-rooted polynomial control showing an order-one linear-exterior omission error.",
        "family": "F_L(v)=v^L(1-v^2/4)^L, L even, s=L^-2; evaluate the exact heat polynomial at v=0.",
        "arithmetic": "Full/linear and squared quadratic/linear ratios are exact rational numbers. Displayed square roots and exp(-1/2) are 90-digit Decimal approximations, not interval certificates.",
        "scope": "Not theta data, a simplicity statistic, a high-height certificate, or evidence for RH. The asymptotic claim is proved analytically in Note 19.",
        "predicted_limit_decimal": limit, "rows": rows,
    }
    target = Path(__file__).with_name('10_QUADRATIC_CLUSTER_DIAGNOSTIC_20261023.json')
    target.write_text(json.dumps(record, indent=2) + '\n')
    print(json.dumps({"record": str(target), "rows": len(rows),
        "last_full_over_linear": rows[-1]["full_over_linear_decimal"],
        "last_relative_quadratic_error": rows[-1]["relative_quadratic_error_decimal"]}, indent=2))


if __name__ == '__main__':
    main()
