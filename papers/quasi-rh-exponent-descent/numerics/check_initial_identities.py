#!/usr/bin/env python3
"""Exact finite checks for the initial descent investigation.

Prepared for Edward Baker, 2026-10-08, with substantial LLM assistance.
Model: GPT-6 (Codex); serving variant and effort are not exposed.
Uses Python 3 standard library only. No zeta zeros or prime data are fitted.
"""

from fractions import Fraction as Q
import json
from pathlib import Path


def trim(a):
    a = list(map(Q, a))
    while len(a) > 1 and not a[-1]:
        a.pop()
    return a


def add(a, b):
    return trim([(a[i] if i < len(a) else 0) +
                 (b[i] if i < len(b) else 0)
                 for i in range(max(len(a), len(b)))])


def scale(a, c):
    return trim([Q(c) * v for v in a])


def mul(a, b):
    out = [Q(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return trim(out)


def diff(a):
    return trim([i * a[i] for i in range(1, len(a))] or [0])


def derivative_times_phi(a, b):
    # d/du[(A(c)+s B(c))*exp(-c)], c=cosh(u), s=sinh(u).
    even = add(mul([0, 1], b), mul([-1, 0, 1], add(diff(b), scale(b, -1))))
    odd = add(diff(a), scale(a, -1))
    return even, odd


def kernel_check():
    a, b = [Q(1)], [Q(0)]
    for _ in range(4):
        a, b = derivative_times_phi(a, b)
    assert a == list(map(Q, [-3, 5, 5, -6, 1]))
    assert b == [0]
    positive_kernel = add(a, [324])
    square_term = scale(mul(mul([-9, 2], [-9, 2]), [27, 12, 4]), Q(1, 16))
    certificate = add(add(add(square_term, [-5, 0, 5]), [-5, 5]), [Q(3109, 16)])
    assert positive_kernel == certificate
    monotonic_poly = add(positive_kernel, scale(diff(positive_kernel), -1))
    assert monotonic_poly == list(map(Q, [316, -5, 23, -10, 1]))
    monotonic_certificate = add(mul([0, 0, 1], mul([-5, 1], [-5, 1])), [316, -5, -2])
    assert monotonic_poly == monotonic_certificate
    # z=3+3i gives z^2=18i and z^4=-324, using integer pairs.
    z2_real, z2_imag = 3 * 3 - 3 * 3, 2 * 3 * 3
    assert z2_real * z2_real - z2_imag * z2_imag == -324
    assert 2 * z2_real * z2_imag == 0
    return {
        "fourth_derivative_coefficients_ascending": [int(x) for x in a],
        "positive_kernel_coefficients_ascending": [int(x) for x in positive_kernel],
        "positive_lower_bound_for_c_ge_1": "3109/16",
        "positive_certificate_identity": True,
        "monotonicity_polynomial_identity": True,
        "quartic_zero_at_3_plus_3i": True,
    }


def recurrence_check():
    records = []
    for q, eta in [(Q(1, 4), 1), (Q(1, 2), 2), (Q(1, 2), 1)]:
        energy = Q(1)
        for n in range(1, 33):
            energy = q * energy + Q(1, 2 ** (eta * n))
            formula = q ** n + Q(1, 2 ** (eta * n)) * sum(
                (q * 2 ** eta) ** j for j in range(n))
            assert energy == formula
        records.append({"q": str(q), "b": 2, "eta": eta,
                        "steps_checked": 32, "identity": True,
                        "final_energy": str(energy)})
    # For a=1/2, r=2, q=1/4, log-scale y=2^n:
    # E(exp(y))=y^-2=q E(exp(y/2)), exactly.
    for n in range(1, 33):
        y = Q(2 ** n)
        assert y ** -2 == Q(1, 4) * (y / 2) ** -2
    return {"fixed_scale_geometric_iteration": records,
            "factor_scale_logarithmic_counterexample": True}


def main():
    cutoff = Q(11, 24)
    exponents = [7 * cutoff - 7, 14 * cutoff - 7, 8 * (2 * cutoff - 1)]
    assert exponents == [Q(-91, 24), Q(-7, 12), Q(-2, 3)]
    assert Q(1, 2) - Q(5, 12) == Q(1, 12)
    result = {
        "date": "2026-10-08",
        "arithmetic": "exact rational and integer operations",
        "kernel": kernel_check(),
        "recurrences": recurrence_check(),
        "scalar_remainder_exponents": [str(v) for v in exponents],
        "minimum_normalized_remainder_power": "1/12",
        "scope": "Finite algebra checks only; no RH, zero-strip, or arithmetic contraction proof.",
    }
    out = Path(__file__).with_name("initial_identity_record_20261008.json")
    out.write_text(json.dumps(result, indent=2) + "\n")
    print("All exact identities passed; wrote " + out.name)


if __name__ == "__main__":
    main()
