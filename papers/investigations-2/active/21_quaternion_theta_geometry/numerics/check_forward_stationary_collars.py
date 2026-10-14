#!/usr/bin/env python3
"""Exact-rational checks and one guarded theta collar for Note 10.

Prepared for Edward Baker, 14 October 2026, with substantial LLM assistance.
Recorded inherited model: gpt-6.1-sol (Codex); reasoning effort: ultra.
Checks coefficientwise heat/implicit-branch identities on a polynomial
basis, a quartic control, and strict collar inequalities using the paid
dyadic enclosures in the hash-bound Note 8 certificate. This script does
not prove the analytic branch-covering theorem or any all-height claim.
"""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import hashlib
import json


SOURCE_NAME = "COMPENSATED_STATIONARY_THETA_CERTIFICATE_20261014.json"
SOURCE_SHA256 = "887e207c90fd3d6eeb2baa7c4e1bade7cc9490d401abd2153a43bc0d2408a5ce"


def add(*polynomials):
    result = {}
    for polynomial in polynomials:
        for degree, coefficient in polynomial.items():
            result[degree] = result.get(degree, F(0)) + coefficient
    return {degree: value for degree, value in result.items() if value}


def scale(polynomial, value):
    return {degree: coefficient * value for degree, coefficient in polynomial.items()
            if coefficient * value}


def multiply(p, q):
    result = {}
    for degree, coefficient in p.items():
        for other, value in q.items():
            power = tuple(a + b for a, b in zip(degree, other))
            result[power] = result.get(power, F(0)) + coefficient * value
    return {degree: value for degree, value in result.items() if value}


def derivative(polynomial, variable, order=1):
    for _ in range(order):
        result = {}
        for degree, coefficient in polynomial.items():
            if degree[variable]:
                power = list(degree)
                power[variable] -= 1
                result[tuple(power)] = coefficient * degree[variable]
        polynomial = result
    return polynomial


def at_y_zero(polynomial):
    return {degree: value for degree, value in polynomial.items() if degree[0] == 0}


def reduce_y_square(polynomial, multiplier):
    """Exact remainder modulo y^2 - multiplier * delta."""
    result = {}
    for (y, delta, amplitude), value in polynomial.items():
        quotient, remainder = divmod(y, 2)
        degree = (remainder, delta + quotient, amplitude)
        result[degree] = result.get(degree, F(0)) + value * multiplier ** quotient
    return {degree: value for degree, value in result.items() if value}


def dyadic_endpoint(ball, side):
    value = ball[f"{side}_dyadic"]
    return F(value["mantissa"]) * F(2) ** value["exponent"]


def genuine_interval(cell, order):
    retained = cell["compensated_aggregate_jets"][order]
    error = dyadic_endpoint(cell["complete_compensated_four_jet_errors"][order], "upper")
    return (dyadic_endpoint(retained, "lower") - error,
            dyadic_endpoint(retained, "upper") + error)


def distance_from_zero(interval):
    return max(F(0), interval[0], -interval[1])


def same_strict_sign(first, second):
    return first[0] > 0 and second[0] > 0 or first[1] < 0 and second[1] < 0


def ball_interval(ball):
    return dyadic_endpoint(ball, "lower"), dyadic_endpoint(ball, "upper")


def moment_upper(order):
    # Note 10: pi>25/8, pi<22/7, e>8/3, m>=1, tau<=1.
    q = F(3, 8) ** 3
    return 2 * factorial(order) * F(22, 7) ** 2 * F(2, 7) ** (order + 1) * q / (1 - q ** 3)


def main():
    checks = []

    def check(name, condition):
        if not condition:
            raise RuntimeError(f"Exact collar check failed: {name}")
        checks.append({"name": name, "passed": True})

    # Independently generate the finite heat evolution of every spatial
    # monomial through degree 14, then differentiate its coefficients.
    # Variables are (y, delta, amplitude_parameter).
    for degree in range(15):
        W = {(degree - 2 * p, p, 0):
             F((-1) ** p * factorial(degree), factorial(p) * factorial(degree - 2 * p))
             for p in range(degree // 2 + 1)}
        jets = [derivative(W, 0, k) for k in range(6)]
        check(f"heat basis degree {degree}", not add(derivative(W, 1), jets[2]))
        for j in (0, 1):
            f, C, D, E = jets[j + 1:j + 5]
            # Along a regular f=0 branch: velocity=D/C. Verify
            # quotient-free identities before imposing stationarity.
            amplitude_numerator = add(multiply(C, derivative(jets[j], 1)), multiply(D, f))
            check(f"amplitude ODE degree {degree} j={j}",
                  not add(amplitude_numerator, multiply(C, C), scale(multiply(D, f), -1)))
            curvature_numerator = add(multiply(C, derivative(C, 1)), multiply(D, derivative(C, 0)))
            check(f"curvature ODE degree {degree} j={j}",
                  not add(curvature_numerator, multiply(C, E), scale(multiply(D, D), -1)))
            check(f"implicit velocity degree {degree} j={j}",
                  not add(multiply(C, derivative(f, 1)), multiply(D, derivative(f, 0))))

    Q = {(4, 0, 0): F(1, 4), (2, 1, 0): F(-3),
         (0, 2, 0): F(3), (0, 0, 1): F(-1)}
    h = [derivative(Q, 0, k) for k in range(5)]
    L = [add(multiply(h[j + 1], h[j + 1]), scale(multiply(h[j], h[j + 2]), -1))
         for j in (0, 1)]
    check("quartic heat equation", not add(derivative(Q, 1), h[2]))
    check("quartic central first sign", at_y_zero(L[0]) == {(0, 3, 0): F(18), (0, 1, 1): F(-6)})
    check("quartic outer first signs", reduce_y_square(L[0], F(6)) ==
          {(0, 3, 0): F(72), (0, 1, 1): F(12)})
    check("quartic second stationary signs", reduce_y_square(L[1], F(2)) == {(0, 2, 0): F(48)})
    check("quartic central stationary derivative", not at_y_zero(h[1]))
    check("quartic triple stationary root at delta zero",
          {degree: value for degree, value in h[1].items() if degree[1] == 0} == {(3, 0, 0): F(1)})

    path = Path(__file__).resolve().parent / SOURCE_NAME
    source_bytes = path.read_bytes()
    check("hash-bound source certificate", hashlib.sha256(source_bytes).hexdigest() == SOURCE_SHA256)
    source = json.loads(source_bytes)
    check("source successful", source["status"] == "PASS")
    check("source closed domain", source["domain"]["t"] == ["1/200", "3/50"] and
          source["domain"]["x"] == ["7", "41"])
    check("source no unresolved cells", not source["unresolved_cells"] and
          not source["branch_isolation_unresolved_cells"])
    cells = source["cells"]
    check("34 source cells", len(cells) == 34)
    for index, cell in enumerate(cells):
        check(f"source cell {index} exact cover",
              dyadic_endpoint(cell["x_left"], "lower") == 7 + index and
              dyadic_endpoint(cell["x_right"], "upper") == 8 + index)

    moment_caps = {m: moment_upper(m) for m in range(2, 6)}
    step = F(1, 200000)
    data = []
    for j, d_floor, edge_floor, amplitude_floor, B_cap in [
            (0, F(1, 500000), F(1, 500000), F(9, 100000), F(9, 100)),
            (1, F(1, 1000000), F(1, 1000000), F(3, 200000), F(3, 25))]:
        cell_gaps = [max(distance_from_zero(genuine_interval(cell, j + 1)),
                        distance_from_zero(genuine_interval(cell, j + 2))) for cell in cells]
        check(f"j={j} complete derivative-pair slice floor", min(cell_gaps) > d_floor)
        edge_gap = min(distance_from_zero(genuine_interval(cells[index], j + 1)) for index in (0, -1))
        check(f"j={j} strict outer edge floor", edge_gap > edge_floor)
        branches = []
        for cell in cells:
            observation = next(item for item in cell["observations"] if item["j"] == j)
            if observation["classification"] == "stationarity_excluded":
                direct = distance_from_zero(genuine_interval(cell, j + 1)) > 0
                monotone = (observation.get("exclusion_method") ==
                            "uniform_endpoint_signs_and_strict_spatial_monotonicity" and
                            distance_from_zero(ball_interval(observation["genuine_next_derivative"])) > 0 and
                            same_strict_sign(ball_interval(observation["left_stationary_derivative"]),
                                             ball_interval(observation["right_stationary_derivative"])))
                check(f"j={j} exclusion at x={dyadic_endpoint(cell['x_left'], 'lower')}",
                      direct or monotone)
                continue
            check(f"j={j} regular branch classification", observation["classification"] == "stationary_signed_and_unique_branch")
            first, curvature = genuine_interval(cell, j), genuine_interval(cell, j + 2)
            check(f"j={j} opposite branch signs", first[1] < 0 < curvature[0] or curvature[1] < 0 < first[0])
            check(f"j={j} initial amplitude floor", distance_from_zero(first) > amplitude_floor)
            branches.append([str(dyadic_endpoint(cell["x_left"], "lower")), str(dyadic_endpoint(cell["x_right"], "upper"))])
        check(f"j={j} safe moment sum cap", moment_caps[j + 3] + moment_caps[j + 4] < B_cap)
        check(f"j={j} nondegeneration collar inequality", step * B_cap < d_floor)
        check(f"j={j} no edge entry collar inequality", step * moment_caps[j + 3] < edge_floor)
        data.append({"j": j, "derivative_pair_floor": str(d_floor), "edge_floor": str(edge_floor),
                     "amplitude_floor": str(amplitude_floor), "moment_sum_cap": str(B_cap),
                     "stationary_Laguerre_floor": str(amplitude_floor * (d_floor - step * B_cap)),
                     "stationary_energy_floor": str(amplitude_floor ** 2), "base_stationary_cells": branches})

    record = {
        "date": "2026-10-14", "prepared_for": "Edward Baker", "LLM_assistance": "substantial",
        "recorded_model": "gpt-6.1-sol (Codex)", "recorded_reasoning_effort": "ultra",
        "arithmetic": "Python standard-library exact Fraction polynomial and dyadic endpoint arithmetic",
        "status": "all exact checks passed", "checker": Path(__file__).name,
        "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "source_certificate": SOURCE_NAME, "source_certificate_sha256": SOURCE_SHA256,
        "time_base": "3/50", "time_step": str(step), "time_top": str(F(3, 50) + step),
        "spatial_interval": ["7", "41"], "moment_upper_bounds": {str(m): str(v) for m, v in moment_caps.items()},
        "collar_data": data, "checks": checks, "check_count": len(checks),
        "scope": "Conditional on Note 8 source certificate and Note 10 analytic theorem; no quadrature rerun or all-height claim."
    }
    output = Path(__file__).resolve().parent / "FORWARD_STATIONARY_COLLAR_CHECKS_20261014.json"
    output.write_text(json.dumps(record, indent=2, sort_keys=True) + "\n")
    print(f"{len(checks)} exact checks passed; wrote {output.name}")


if __name__ == "__main__":
    main()
