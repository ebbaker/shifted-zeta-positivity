#!/usr/bin/env python3
"""Finite exact edge-packet checks. Standard library; deterministic stdout only.

Model: GPT-6 (Codex), inherited variant/effort not exposed. Prepared for
Edward Baker, 8 October 2026, with substantial LLM assistance. This is finite
algebra verification, not independent specialist or analytic validation.
"""
from fractions import Fraction
from itertools import product
from math import factorial, isqrt, prod
import json


def prime_one_mod_three_at_least(n):
    while True:
        if n % 3 == 1 and all(n % d for d in range(2, isqrt(n) + 1)):
            return n
        n += 1


def divisors(n):
    return product(*(range(e + 1) for e in n))


def sub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def norm(n, norms):
    return prod(p ** e for p, e in zip(norms, n))


def mu(n):
    return 0 if any(e > 1 for e in n) else (-1) ** sum(n)


def add_to(a, b):
    for i, v in enumerate(b):
        a[i] += v


def vector_scaled(n, c):
    return [c * e for e in n]


def character(n, phases, deleted):
    return None if any(n[i] for i in deleted) else sum(e * p for e, p in zip(n, phases)) % 6


def character_product(values):
    return None if None in values else sum(values) % 6


def packet_case(b_exp, norms, z, y, u, v):
    size = len(norms)
    q_index, r_index = size - 2, size - 1
    b = tuple(b_exp) + (0, 0)
    n = tuple(b_exp) + (1, 1)
    b_norm = norm(b, norms)
    q_norm, r_norm = norms[-2:]
    assert b_norm > 1
    assert q_norm <= z and r_norm <= z and b_norm * q_norm <= z
    assert r_norm * min(p for p, e in zip(norms, b) if e) > z
    assert max(b_norm * q_norm, b_norm * r_norm) <= y < q_norm * r_norm
    assert b_norm <= min(u, v) and min(q_norm, r_norm) > max(u, v)
    assert y > z
    phases = tuple((2 * i + 1) % 6 for i in range(size))
    masks = ((), (0,), (q_index,), (r_index,))
    counters = {"tail_divisors": 0, "triple_terms": 0, "phase_checks": 0}
    total_original = 0
    for d in divisors(n):
        if norm(d, norms) <= y:
            continue
        counters["tail_divisors"] += 1
        assert d[q_index] == d[r_index] == 1
        e = d[:-2] + (0, 0)
        mu_e = mu(e)
        numerators = {edge: [0] * size for edge in ("LH", "HL", "HH", "LL")}
        c_z = sum(mu(a) * mu(sub(d, a)) for a in divisors(d)
                  if norm(a, norms) <= z and norm(sub(d, a), norms) <= z)
        assert c_z == 2 * mu_e
        total_original -= c_z
        for p_index, exponent in enumerate(d):
            for j in range(1, exponent + 1):
                ell = tuple(j if i == p_index else 0 for i in range(size))
                remainder = sub(d, ell)
                for a in divisors(remainder):
                    c = sub(remainder, a)
                    if norm(a, norms) * norm(ell, norms) > z or norm(c, norms) > z:
                        continue
                    counters["triple_terms"] += 1
                    edge = ("L" if norm(a, norms) <= u else "H") + ("L" if norm(ell, norms) <= v else "H")
                    numerators[edge][p_index] += 2 * mu(a) * mu(c)
                    free = sub(n, d)
                    for mask in masks:
                        values = [character(x, phases, mask) for x in (a, ell, c, free)]
                        assert character_product(values) == character(n, phases, mask)
                        counters["phase_checks"] += 1
        expected_lh = [0] * size
        expected_lh[q_index] = expected_lh[r_index] = -2 * mu_e
        expected_hl = vector_scaled(e, -2 * mu_e)
        assert numerators["LH"] == expected_lh
        assert numerators["HL"] == expected_hl
        assert numerators["HH"] == numerators["LL"] == [0] * size
        combined = numerators["LH"][:]
        add_to(combined, numerators["HL"])
        assert combined == vector_scaled(d, -2 * mu_e)
    assert total_original == 0
    assert counters["tail_divisors"] == prod(e + 1 for e in b_exp)
    return counters


def rational_log_checks():
    count = 0
    for weights in ((1,), (2,), (1, 3), (2, 2), (1, 2, 4), (2, 3, 5, 7)):
        k = len(weights)
        for L in (Fraction(1, 2), Fraction(3), Fraction(17), Fraction(100)):
            terms = [(Fraction((-1) ** sum(e)), sum(w * j for w, j in zip(weights, e)))
                     for e in product((0, 1), repeat=k)]
            J = sum(sign / (L + log_e) for sign, log_e in terms)
            lower = Fraction(factorial(k) * prod(weights), 1) / (L + sum(weights)) ** (k + 1)
            upper = Fraction(factorial(k) * prod(weights), 1) / L ** (k + 1)
            assert 0 < lower <= J <= upper
            LH = sum(-2 * sign * L / (L + log_e) for sign, log_e in terms)
            HL = sum(-2 * sign * log_e / (L + log_e) for sign, log_e in terms)
            assert LH == -2 * L * J and HL == 2 * L * J and LH + HL == 0
            for j in range(k):
                assert sum(sign * log_e ** j for sign, log_e in terms) == 0
            assert sum(sign * log_e ** k for sign, log_e in terms) == (-1) ** k * factorial(k) * prod(weights)
            count += 1
    return count


def main():
    r = prime_one_mod_three_at_least(500000)
    cases = [
        ((1,), (7, 13, 241), 256, 2000, 10, 10),
        # All weak endpoints matter: B=U=V, B*q=z, and B*r=Y.
        ((1,), (7, 37, 241), 259, 1687, 7, 7),
        ((1, 1), (7, 13, 109, 4999), 10000, 500000, 100, 100),
        ((2,), (7, 109, 4999), 10000, 300000, 100, 100),
        ((2, 1), (7, 13, 1009, r), 700000, 400000000, 1000, 1000),
    ]
    totals = {"tail_divisors": 0, "triple_terms": 0, "phase_checks": 0}
    for case in cases:
        result = packet_case(*case)
        for name, value in result.items():
            totals[name] += value
    assert mu((0,)) == 1
    L = Fraction(23)
    assert -2 * L * (1 / L) == -2
    assert 2 * L * (1 / L) - 2 == 0
    print(json.dumps({
        "status": "passed", "packet_cases": len(cases),
        **totals, "rational_log_cases": rational_log_checks(),
        "unit_cofactor_exception": "checked",
        "formal_logarithms": "exact integer vectors; Lambda(p^j)=log Np",
        "limitations": "finite algebra only; no analytic full-tail estimate",
    }, sort_keys=True))


if __name__ == "__main__":
    main()
