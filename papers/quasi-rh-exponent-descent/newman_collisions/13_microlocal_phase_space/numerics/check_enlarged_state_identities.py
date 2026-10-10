#!/usr/bin/env python3
"""Exact finite algebra controls; no theta sign or coverage certificate.

Prepared for Edward Baker with substantial LLM assistance, 2026-10-10.
Model family: GPT-6 (Codex). Serving variant and effort are unavailable.
Uses only Python's standard library and exact rational arithmetic.
"""

import argparse
from fractions import Fraction as F
from hashlib import sha256
from itertools import product
import json
from pathlib import Path


COUNTS = {}


def check(group, actual, expected):
    if actual != expected:
        raise AssertionError((group, actual, expected))
    COUNTS[group] = COUNTS.get(group, 0) + 1


def clean(poly):
    return {degree: value for degree, value in poly.items() if value}


def add(left, right):
    out = dict(left)
    for degree, value in right.items():
        out[degree] = out.get(degree, F(0)) + value
    return clean(out)


def scale(poly, value):
    return clean({degree: value * coefficient
                  for degree, coefficient in poly.items()})


def multiply(left, right):
    out = {}
    for a, value_a in left.items():
        for b, value_b in right.items():
            out[a + b] = out.get(a + b, F(0)) + value_a * value_b
    return clean(out)


def derivative(poly):
    return clean({degree - 1: degree * value
                  for degree, value in poly.items() if degree})


def gaussian_derivative(poly, alpha):
    """Derivative of poly(k) exp(-k^2/(4 alpha)), divided by exponential."""
    return add(derivative(poly),
               scale(multiply(poly, {1: F(1)}), -1 / (2 * alpha)))


def matvec(matrix, vector):
    return [sum(a * b for a, b in zip(row, vector)) for row in matrix]


def graph_controls():
    B = [[-2, 1, 0], [0, -3, 1]]
    q = [1, 2, 6]
    A = [[sum(B[r][i] * B[r][j] for r in range(2))
          + int(i == j == 0) for j in range(3)] for i in range(3)]
    check("graph", matvec(B, q), [0, 0])
    check("graph", A, [[5, -2, 0], [-2, 10, -3], [0, -3, 1]])
    check("graph", matvec(A, q), [1, 0, 0])
    check("graph", sum(a * b for a, b in zip(q, matvec(A, q))), 1)
    # Eliminating coordinates two and three: C^{-1} = [[1,3],[3,10]].
    C_inverse = [[1, 3], [3, 10]]
    coupling = [-2, 0]
    correction = sum(a * b for a, b in
                     zip(coupling, matvec(C_inverse, coupling)))
    check("graph", correction, 4)
    check("graph", A[0][0] - correction, 1)
    check("graph", matvec(C_inverse, [2, 0]), [2, 6])
    # Positive definiteness also follows from ||Bv||^2 + v_1^2.
    for vector in product(range(-2, 3), repeat=3):
        energy = sum(a * b for a, b in zip(vector, matvec(A, vector)))
        check("graph", energy,
              sum(value * value for value in matvec(B, vector)) + vector[0] ** 2)
        check("graph", energy > 0, any(vector))
    return {"B": B, "q": q, "A": A, "Aq": [1, 0, 0],
            "anchored_schur_complement": 1}


def gaussian_controls():
    # Fourier transform of u^4 exp(-alpha u^2) is the fourth derivative
    # of the Gaussian Fourier transform; its i-power is +1.
    for alpha in [F(1, 4), F(1, 2), F(3, 4), F(1), F(5, 4), F(2)]:
        p = {0: F(1)}
        for _ in range(4):
            p = gaussian_derivative(p, alpha)
        numerator = scale(add(scale(p, 16), {0: F(24)}), alpha ** 4)
        expected = {4: F(1), 2: -12 * alpha,
                    0: 12 * alpha ** 2 + 24 * alpha ** 4}
        check("gaussian", numerator, expected)
        discriminant = (-12 * alpha) ** 2 - 4 * expected[0]
        check("gaussian", discriminant, 96 * alpha ** 2 * (1 - alpha ** 2))
        check("gaussian", discriminant >= 0, alpha <= 1)
        check("gaussian", expected[0] > 0, True)
    # Exact polynomial identity in alpha, independent of sampled alpha.
    check("gaussian", add({2: F(144)}, scale({2: F(12), 4: F(24)}, -4)),
          {2: F(96), 4: F(-96)})
    threshold_poly = multiply({2: F(1), 0: F(-6)}, {2: F(1), 0: F(-6)})
    check("gaussian", threshold_poly, {4: F(1), 2: F(-12), 0: F(36)})
    # At k^2=6, P=P'=0 and P''=48: ordinary double zeros.
    second_poly = derivative(derivative(threshold_poly))
    check("gaussian", second_poly[2] * 6 + second_poly[0], 48)
    return {"control_t_star": "1/40", "alpha": "1 + t_star - t",
            "fourier_numerator": "k^4 - 12 alpha k^2 + 12 alpha^2 + 24 alpha^4",
            "discriminant_in_k_squared": "96 alpha^2 (1-alpha^2)",
            "threshold_factorization": "(k^2-6)^2",
            "second_polynomial_derivative_at_k_squared_6": 48}


def chord_controls():
    """Two-variable sparse polynomials: exponents are (k degree, ell degree)."""
    def sum2(left, right, right_scale=F(1)):
        out = dict(left)
        for degree, value in right.items():
            out[degree] = out.get(degree, F(0)) + right_scale * value
        return clean(out)

    def d2(poly, axis):
        out = {}
        for degree, value in poly.items():
            n = degree[axis]
            if n >= 2:
                target = list(degree)
                target[axis] -= 2
                out[tuple(target)] = value * n * (n - 1)
        return out

    def times_square(poly, axis):
        out = {}
        for degree, value in poly.items():
            target = list(degree)
            target[axis] += 2
            out[tuple(target)] = value / 4
        return out

    def H(poly):
        return sum2(d2(poly, 1), times_square(poly, 0))

    def L(poly):
        return sum2(times_square(poly, 1), d2(poly, 0), -1)

    for i, j in product(range(9), repeat=2):
        mono = {(i, j): F(1)}
        commutator = sum2(H(L(mono)), L(H(mono)), -1)
        check("chord", commutator, {(i, j): F(i + j + 1)})
        # If B=-HA and A_t=LA, then B_t=LB-[H,L]A.
        left = {degree: -value for degree, value in H(L(mono)).items()}
        right = sum2(L({degree: -value for degree, value in H(mono).items()}),
                     commutator, -1)
        check("chord", clean(left), right)
    return {"H": "partial_ell^2 + k^2/4",
            "L": "-partial_k^2 + ell^2/4",
            "commutator_H_L": "k partial_k + ell partial_ell + 1",
            "tested_monomial_degrees": "0 through 8 in each variable"}


def score_controls():
    beta_values = [F(1, 2), F(1), F(3, 2), F(2), F(7)]
    k_values = [F(1, 3), F(1), F(7, 4), F(-2)]
    jet_values = [F(-2), F(-1, 3), F(0), F(1, 2), F(3)]
    for beta, k, a2, a3, a4 in product(
            beta_values, k_values, jet_values, jet_values, jet_values):
        # Obtain D_j by differentiating its exact full-state operator,
        # then imposing only A_0=A_1=0 on the complete observed state.
        d0 = -beta ** 2 * a2
        d1 = -beta ** 2 * a3 - 2 * beta * k * a2
        d2 = -beta ** 2 * a4 - 2 * beta * k * a3 - (k ** 2 + 6 * beta) * a2
        check("score", -d0 / beta ** 2, a2)
        check("score", -d1 / beta ** 2 + 2 * k * d0 / beta ** 3, a3)
        check("score", -d2 / beta ** 2 + 2 * k * d1 / beta ** 3
              + (6 * beta - 3 * k ** 2) * d0 / beta ** 4, a4)
        for g in [F(0), 9 / k ** 2, F(-2, 3)]:
            left = beta ** 4 * (2 * a3 ** 2 - 3 * a2 * a4 - g * a2 ** 2)
            right = (2 * d1 ** 2 - 3 * d0 * d2 - 2 * k * d0 * d1 / beta
                     + (18 / beta - k ** 2 / beta ** 2 - g) * d0 ** 2)
            check("score", left, right)
    return {"full_state_D": "-beta^2 A_kk - 2 beta k A_k - (k^2+2 beta) A",
            "candidate_constraints": "A_0 = A_1 = 0",
            "quadratic": "2 D_1^2 - 3 D_0 D_2 - 2k D_0 D_1/beta + (18/beta-k^2/beta^2-g) D_0^2",
            "rational_jet_configurations": 2500}


def main():
    checks = {"graph": graph_controls(), "gaussian_control": gaussian_controls(),
              "chord_commutator": chord_controls(), "score_dictionary": score_controls()}
    source = Path(__file__).resolve()
    record = {
        "date": "2026-10-10", "prepared_for": "Edward Baker",
        "acknowledgment": "Prepared with substantial LLM assistance; internal algebra replay.",
        "model_family": "GPT-6 (Codex)", "serving_variant": "unavailable; not inferred",
        "reasoning_effort": "unavailable; not inferred", "arithmetic": "exact Fraction; stdlib only",
        "scope": "Finite algebra controls only. No actual-theta sign, outward interval certificate, collision exclusion, or global coverage.",
        "source_sha256": sha256(source.read_bytes()).hexdigest(),
        "checks": checks, "assertions_by_group": COUNTS,
        "total_assertions": sum(COUNTS.values()), "status": "passed",
    }
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", nargs="?", type=Path,
                        default=source.with_name("ENLARGED_STATE_IDENTITY_RECORD_20261010.json"),
                        help="Small JSON record; defaults to the script's directory.")
    destination = parser.parse_args().output
    destination.write_text(json.dumps(record, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"status": record["status"], "assertions": record["total_assertions"],
                      "record": str(destination), "source_sha256": record["source_sha256"]}))


if __name__ == "__main__":
    main()
