#!/usr/bin/env python3
"""Exact polynomial checks of the declared Fueter lift and S^3 moments."""
import argparse
from fractions import Fraction as Q
from hashlib import sha256
import json
from math import comb, factorial
from pathlib import Path

ZERO = (0, 0, 0, 0)


def const(value):
    return {ZERO: Q(value)} if value else {}


def var(index):
    powers = list(ZERO)
    powers[index] = 1
    return {tuple(powers): Q(1)}


def add(*polys):
    result = {}
    for poly in polys:
        for powers, value in poly.items():
            result[powers] = result.get(powers, Q(0)) + value
    return {powers: value for powers, value in result.items() if value}


def scale(poly, factor):
    return {powers: value * factor for powers, value in poly.items() if value * factor}


def mul(left, right):
    result = {}
    for p, a in left.items():
        for q, b in right.items():
            powers = tuple(x + y for x, y in zip(p, q))
            result[powers] = result.get(powers, Q(0)) + a * b
    return {powers: value for powers, value in result.items() if value}


def deriv(poly, index):
    result = {}
    for powers, value in poly.items():
        if powers[index]:
            new = list(powers)
            new[index] -= 1
            result[tuple(new)] = value * powers[index]
    return result


def cadd(left, right):
    return add(left[0], right[0]), add(left[1], right[1])


def cmul(left, right):
    return (add(mul(left[0], right[0]), scale(mul(left[1], right[1]), -1)),
            add(mul(left[0], right[1]), mul(left[1], right[0])))


def cpow(value, exponent):
    result = (const(1), {})
    for _ in range(exponent):
        result = cmul(result, value)
    return result


def heat_polynomial(degree, time):
    z = (var(0), var(1))
    tau = (add(const(time), var(2)), var(3))
    result = ({}, {})
    for r in range(degree // 2 + 1):
        term = cmul(cpow(tau, r), cpow(z, degree - 2 * r))
        coefficient = Q((-1) ** r * factorial(degree),
                        factorial(r) * factorial(degree - 2 * r))
        result = cadd(result, tuple(scale(component, coefficient) for component in term))
    return result


def lift(degree, time, constant_term=0):
    real, imag = heat_polynomial(degree, time)
    real = add(real, const(constant_term))
    # j(V_real + i V_imag) = j V_real - k V_imag.
    return real, imag, deriv(real, 0), scale(deriv(imag, 0), -1)


def fueter_residual(field):
    # D = d_a + i d_b + j d_c + k d_e; factor 1/2 is immaterial.
    derivatives = [tuple(deriv(component, axis) for component in field) for axis in range(4)]
    a, b, c, e = derivatives
    return (add(a[0], scale(b[1], -1), scale(c[2], -1), scale(e[3], -1)),
            add(a[1], b[0], c[3], scale(e[2], -1)),
            add(a[2], scale(b[3], -1), c[0], e[1]),
            add(a[3], b[2], scale(c[1], -1), e[0]))


def odd_double_factorial(k):
    result = 1
    for value in range(1, 2 * k, 2):
        result *= value
    return result


def sphere_moment(powers):
    if any(power % 2 for power in powers):
        return Q(0)
    half = tuple(power // 2 for power in powers)
    numerator = 1
    for k in half:
        numerator *= odd_double_factorial(k)
    denominator = 1
    for k in range(sum(half)):
        denominator *= 4 + 2 * k
    return Q(numerator, denominator)


def centered(poly, center, radius):
    # a = center + radius*w0; b,c,e = radius*w1,w2,w3.
    result = {}
    for powers, value in poly.items():
        for k in range(powers[0] + 1):
            new = (k,) + powers[1:]
            coefficient = value * comb(powers[0], k) * center ** (powers[0] - k)
            coefficient *= radius ** (k + sum(powers[1:]))
            result[new] = result.get(new, Q(0)) + coefficient
    return {powers: value for powers, value in result.items() if value}


def average(poly, additional_w0_power=0):
    result = Q(0)
    for powers, value in poly.items():
        weighted = (powers[0] + additional_w0_power,) + powers[1:]
        result += value * sphere_moment(weighted)
    return result


def at_center(poly, center):
    return sum((value * center ** powers[0]
                for powers, value in poly.items() if not any(powers[1:])), Q(0))


def quaternion_mul(left, right):
    a, b, c, d = left
    e, f, g, h = right
    return (a*e-b*f-c*g-d*h, a*f+b*e+c*h-d*g,
            a*g-b*h+c*e+d*f, a*h+b*g-c*f+d*e)


def signed_correlation(left, right):
    conjugate = (left[0], -left[1], -left[2], -left[3])
    return quaternion_mul((Q(0), Q(0), Q(1), Q(0)),
                          quaternion_mul(conjugate, right))[0]


def check_case(label, degree, time, center, radius, constant_term=0):
    field = lift(degree, time, constant_term)
    regular = all(not component for component in fueter_residual(field))
    boundary = tuple(centered(component, center, radius) for component in field)
    direct = [tuple(at_center(component, center) for component in field)]
    for order in (1, 2):
        derivative = field
        for _ in range(order):
            derivative = tuple(deriv(component, 0) for component in derivative)
        direct.append(tuple(at_center(component, center) for component in derivative))
    moments = [tuple(average(component) for component in boundary),
               tuple(4 * average(component, 1) / radius for component in boundary),
               tuple(6 * (4 * average(component, 2) - average(component)) / radius ** 2
                     for component in boundary)]
    equality = [actual == expected for actual, expected in zip(moments, direct)]
    h0, h1 = direct[0][0], direct[0][2]
    h2, h3 = direct[1][2], direct[2][2]
    scalar_forms = (h1*h1-h0*h2, h2*h2-h1*h3)
    boundary_forms = (signed_correlation(moments[0], moments[1]),
                      signed_correlation(moments[1], moments[2]))
    signed_forms_match = boundary_forms == scalar_forms
    control_forms_match = (scalar_forms == (2*center*center+4*time-2, Q(4))
                           if degree == 2 and constant_term == 1 else True)
    return {"case": label, "degree": degree, "t": str(time), "x": str(center),
            "R": str(radius), "fueter_regular": regular,
            "moment_orders_0_1_2": equality,
            "direct_quaternion_components": [[str(value) for value in row] for row in direct],
            "laguerre_forms": [str(value) for value in boundary_forms],
            "signed_boundary_forms_match_scalar": signed_forms_match,
            "polynomial_control_forms_match": control_forms_match,
            "pass": regular and all(equality) and signed_forms_match and control_forms_match}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    cases = []
    parameters = ((Q(1, 3), Q(2, 5), Q(3, 4)),
                  (Q(7, 6), Q(-1, 2), Q(2, 3)))
    for time, center, radius in parameters:
        for degree in (0, 1, 2, 3, 4, 6):
            cases.append(check_case("H_" + str(degree), degree, time, center, radius))
        cases.append(check_case("P=z^2-2tau+1", 2, time, center, radius, 1))
    # Independent elementary moment sanity checks.
    moment_sanity = {"one": sphere_moment((0, 0, 0, 0)) == 1,
                     "w0_squared": sphere_moment((2, 0, 0, 0)) == Q(1, 4),
                     "w0_fourth": sphere_moment((4, 0, 0, 0)) == Q(1, 8),
                     "w0_squared_w1_squared": sphere_moment((2, 2, 0, 0)) == Q(1, 24),
                     "odd": sphere_moment((1, 0, 0, 0)) == 0}
    collision = check_case("P physical collision", 2, Q(1, 2), Q(0), Q(1), 1)
    collision_zero = all(value == "0" for value in collision["direct_quaternion_components"][0])
    wrong_sign = check_case("P wrong stationary sign", 2, Q(0), Q(0), Q(1), 1)
    control_sanity = {"positive_time_joint_zero": collision_zero and collision["pass"],
                      "wrong_stationary_L0": wrong_sign["laguerre_forms"] == ["-2", "4"]
                      and wrong_sign["pass"]}
    result = {"checker_source_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
              "date": "2026-10-14",
              "prepared_for": "Edward Baker",
              "llm_assistance": "Substantial LLM assistance",
              "recorded_model": "gpt-6.1-sol (Codex)",
              "reasoning_effort": "ultra",
              "arithmetic": "fractions.Fraction (exact)",
              "quaternion_coordinate_convention": "q=a+i*b+j*c+k*e; z0=a+i*b; z1=c-i*e",
              "case_count": len(cases), "moment_sanity": moment_sanity,
              "control_sanity": control_sanity,
              "all_pass": all(case["pass"] for case in cases) and all(moment_sanity.values())
              and all(control_sanity.values()),
              "cases": cases}
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({key: result[key] for key in ("checker_source_sha256", "case_count", "all_pass")}))
    if not result["all_pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
