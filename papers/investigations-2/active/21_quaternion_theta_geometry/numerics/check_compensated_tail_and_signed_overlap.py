#!/usr/bin/env python3
"""Rational-only replay of Note 8's all-index and signed overlap payments.

Prepared for Edward Baker, 14 October 2026, with substantial LLM assistance.
Recorded model: gpt-6.1-sol (Codex); reasoning effort: ultra.
This does not decide sampled stationary signs or certify the rest of R+.
"""
from fractions import Fraction as F
from math import comb, factorial
from pathlib import Path
import hashlib
import json


def add(*polynomials):
    result = {}
    for polynomial in polynomials:
        for degree, coefficient in polynomial.items():
            result[degree] = result.get(degree, F(0)) + coefficient
    return {degree: coefficient for degree, coefficient in result.items() if coefficient}


def mul(p, q):
    result = {}
    for (a, b), coefficient in p.items():
        for (c, d), other in q.items():
            degree = (a + c, b + d)
            result[degree] = result.get(degree, F(0)) + coefficient * other
    return result


def derivative(p, variable):
    result = {}
    for (a, b), coefficient in p.items():
        degree = (a, b)[variable]
        if degree:
            result[a - (variable == 0), b - (variable == 1)] = coefficient * degree
    return result


def gaussian_derivative(p):
    result = {}
    for degree, coefficient in p.items():
        if degree:
            result[degree - 1] = result.get(degree - 1, F(0)) + degree * coefficient
        result[degree + 1] = result.get(degree + 1, F(0)) - 2 * coefficient
    return {degree: coefficient for degree, coefficient in result.items() if coefficient}


def gaussian_moment_upper(degree):
    if degree % 2:
        return F(factorial(degree // 2), 2)
    return F(factorial(degree), 4 ** (degree // 2) * factorial(degree // 2)) * F(9, 10)


def exp_bounds(x, order):
    """Strict rational bounds from the Taylor sum and geometric tail."""
    if not 0 <= x < order + 2:
        raise RuntimeError("Taylor exponential bound has invalid parameters")
    lower = sum((x ** k / factorial(k) for k in range(order + 1)), F(0))
    tail = x ** (order + 1) / factorial(order + 1) / (1 - x / (order + 2))
    return lower, lower + tail


def serialized(value):
    if isinstance(value, F):
        return str(value)
    if isinstance(value, dict):
        return {str(key): serialized(item) for key, item in value.items()}
    if isinstance(value, (tuple, list)):
        return [serialized(item) for item in value]
    return value


def main():
    checks = []

    def check(name, condition):
        if not condition:
            raise RuntimeError(f"Failed rational certificate check: {name}")
        checks.append({"name": name, "passed": True})

    check("e > 8/3", exp_bounds(F(1), 3)[0] == F(8, 3))
    check("e < 11/4", exp_bounds(F(1), 8)[1] < F(11, 4))
    for x, target in [(F(2, 5), F(3, 2)), (F(3, 5), F(11, 6)),
                      (F(4, 5), F(9, 4)), (F(1, 5), F(5, 4))]:
        check(f"exp({x}) < {target}", exp_bounds(x, 8)[1] < target)
    check("exp(6/5) > 83/25", exp_bounds(F(6, 5), 8)[0] > F(83, 25))
    check("exp(23/3) > 2000", exp_bounds(F(23, 3), 12)[0] > 2000)
    check("exp(38/5) > 1960", exp_bounds(F(38, 5), 14)[0] > 1960)
    atan_fifth_lower = sum(((-1) ** k * F(1, 5) ** (2 * k + 1) / (2 * k + 1)
                            for k in range(4)), F(0))
    machin_lower = 16 * atan_fifth_lower - 4 * F(1, 239)
    check("Machin alternating lower bound > 333/106", machin_lower > F(333, 106))
    tangent_four_fifths = F(120, 119)
    check("Machin tangent identity", (tangent_four_fifths - F(1, 239))
          / (1 + tangent_four_fifths * F(1, 239)) == 1)
    check("sqrt(pi) < 9/5 from pi < 22/7", F(22, 7) < F(9, 5) ** 2)
    check("N=3 K=2 threshold", 16 * F(25, 8) > 25)

    Q = [{(0, 1): F(2), (0, 0): F(3)}]
    multiplier = {(1, 0): F(2), (0, 0): F(5), (0, 1): F(4)}
    for _ in range(4):
        Q.append(add(mul(multiplier, Q[-1]), derivative(Q[-1], 0),
                     mul({(0, 1): F(4)}, derivative(Q[-1], 1))))
    check("first endpoint majorant", {b: c for (a, b), c in Q[1].items() if a == 0}
          == {0: F(15), 1: F(30), 2: F(8)})
    check("third endpoint majorant", {b: c for (a, b), c in Q[3].items() if a == 0}
          == {0: F(465), 1: F(3450), 2: F(4280), 3: F(1440), 4: F(128)})
    betas = [{1: F(1), 3: F(1)}, {3: F(1, 6)}]
    for k, beta in enumerate(betas):
        third = F(6) * (beta.get(3, F(0)) - beta.get(1, F(0)))
        check(f"beta{k} Kronecker jets", (beta.get(1, F(0)), third)
              == ((F(1), F(0)) if k == 0 else (F(0), F(1))))

    def tail(s):
        alpha_power = F(352, 7) ** s if s >= 0 else F(50) ** s
        return alpha_power * F(3, 8) ** 50 / (1 - F(3, 8) ** 15)

    expected_B = [(F(316), F(67)), (F(702), F(747, 5)),
                  (F(1566), F(328)), (F(18819, 5), F(1539, 2))]
    C = []
    B = []
    for j in range(4):
        W = {}
        for ell in range(min(j, 4) + 1):
            coefficient = F(comb(4, ell) * factorial(j), factorial(j - ell))
            W = add(W, {(a + j - ell, b): coefficient * c
                        for (a, b), c in Q[4 - ell].items()})
        result = sum((c * F(factorial(a), 3 ** (a + 1)) * tail(b - a)
                      for (a, b), c in W.items()), F(0))
        gaussian_bounds = []
        for k, beta in enumerate(betas):
            p = {degree + j: c for degree, c in beta.items()}
            for _ in range(4):
                p = gaussian_derivative(p)
            bound = sum((abs(c) * gaussian_moment_upper(degree)
                         for degree, c in p.items()), F(0))
            gaussian_bounds.append(bound)
            result += bound * sum((c * tail(b + 1) for (a, b), c in Q[2 * k + 1].items()
                                   if a == 0), F(0))
        check(f"Gaussian majorants j={j}", tuple(gaussian_bounds) == expected_B[j])
        check(f"x^4 tail majorant j={j}", result < F((2, 4, 9, 20)[j], 10 ** 9))
        check(f"uniform x>=7 tail j={j}", result / 7 ** 4 < F((1, 2, 4, 9)[j], 10 ** 12))
        B.append(gaussian_bounds)
        C.append(result)

    check("extra source core 3/25", F(54) * F(4, 11) ** 6 > F(3, 25))
    check("extra source core 1/20", F(2052, 25) * F(4, 11) ** 7 * F(4, 5) > F(1, 20))
    check("core q upper at 3/20", F(22, 7) * F(11, 6) < 6)
    check("core q upper at 1/5", F(22, 7) * F(9, 4) < F(36, 5))
    check("tail exponent at b=3/10", F(27, 10) + F(27, 5000) - F(83, 8) < -F(23, 3))
    check("tail slope at b=3/10", F(9) + F(9, 250) - F(83, 2) < -32)
    b, c = F(3, 10), F(32, 3)
    primitive = lambda u: u ** 5 / 5 - c * u ** 7 / 7
    P = (F(6, 25) * primitive(F(1, 10))
         + F(3, 25) * (primitive(F(3, 20)) - primitive(F(1, 10)))
         + F(1, 20) * (primitive(F(1, 5)) - primitive(F(3, 20))))
    I = sum(((comb(6, ell) * b ** (6 - ell)
               - (b ** 2 * comb(4, ell) * b ** (4 - ell) if ell <= 4 else 0))
              * F(factorial(ell), 32 ** (ell + 1)) for ell in range(7)), F(0))
    check("positive core exact integral", P == F(111799, 33600000000))
    check("negative complete tail exact integral", I == F(85837761, 6710886400000))
    gap = P - F(16, 75) * I
    check("signed moment exact gap", gap == F(659107997, 1101004800000000))
    check("signed moment gap > 1/2000000", gap > F(1, 2000000))
    check("uniform t<=1 tail exponent", F(279, 100) - F(333, 106) * F(83, 25) < -F(38, 5))
    check("uniform t<=1 tail slope", F(48, 5) - 4 * F(333, 106) * F(83, 25) < -32)
    uniform_gap = P - F(32, 147) * I
    check("uniform t<=1 signed moment exact gap", uniform_gap == F(2092283587, 3853516800000000))
    check("uniform t<=1 signed moment gap > 1/2000000", uniform_gap > F(1, 2000000))

    eps = [F(k, 10 ** 12) for k in (1, 2, 4, 9)]
    p1, p2, p3 = F(1, 8) + eps[1], F(1, 12) + eps[2], F(1, 12) + eps[3]
    E1 = eps[2] ** 2 + p1 * eps[3] + p3 * eps[1] + eps[1] * eps[3]
    Eall = E1 + 2 * p2 * eps[2]
    check("stationary cross-term error < 13e-13", E1 < F(13, 10 ** 13))
    check("general Laguerre error < 2e-12", Eall < F(2, 10 ** 12))
    mu = F(49, 240000000000)
    check("all-band cross-term surplus > 1e-10", mu - Eall - E1 > F(1, 10 ** 10))

    record = {
        "date": "2026-10-14", "intended_author": "Edward Baker",
        "llm_assistance": "Substantial derivation and implementation assistance",
        "recorded_model": "gpt-6.1-sol (Codex)", "recorded_reasoning_effort": "ultra",
        "arithmetic": "Python fractions.Fraction; exact rational arithmetic",
        "scope": "K=2 N=3 omitted-index payments on R+ and analytic signed L1/cross-term estimate on B only",
        "rectangle_R_plus": {"t": ["1/200", "3/50"], "x": ["7", "41"]},
        "signed_band_B": {"t": ["1/200", "3/50"], "x": ["7", "8"]},
        "gaussian_majorants": B, "x4_jet_tail_majorants": C,
        "uniform_jet_error_upper": eps,
        "moment_gap_lower": gap, "stationary_error_upper": E1,
        "uniform_t_zero_to_one_moment_gap_lower": uniform_gap,
        "general_laguerre_error_upper": Eall, "signed_laguerre_lower": mu,
        "signed_cross_term_surplus_lower": F(1, 10 ** 10),
        "checks": checks, "check_count": len(checks), "all_passed": True,
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "limitations": ["Retained-channel quadrature is not performed by this replay.",
                        "R+ outside B and every all-height extension remain outside this record.",
                        "The analytic proof, not this source hash, applies these payments to the complete theta source."]
    }
    destination = Path(__file__).with_name("COMPENSATED_TAIL_AND_SIGNED_OVERLAP_20261014.json")
    destination.write_text(json.dumps(serialized(record), indent=2) + "\n")
    print(f"{len(checks)} exact rational checks passed; wrote {destination.name}")


if __name__ == "__main__":
    main()
