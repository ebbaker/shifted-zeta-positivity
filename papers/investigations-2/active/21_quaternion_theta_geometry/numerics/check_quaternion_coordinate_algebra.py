#!/usr/bin/env python3
"""Exact quaternion signs, complex-coordinate orientation, and heat identities.

14 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded model: gpt-6.1-sol (Codex); reasoning effort: ultra.
"""
import argparse
from fractions import Fraction as Q
from hashlib import sha256
import importlib.util
import json
from math import factorial
from pathlib import Path


def cadd(a, b):
    return a[0] + b[0], a[1] + b[1]


def cscale(a, coefficient):
    return a[0] * coefficient, a[1] * coefficient


def cmul(a, b):
    return a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0]


def cconj(a):
    return a[0], -a[1]


def cpow(a, exponent):
    result = (Q(1), Q(0))
    for _ in range(exponent):
        result = cmul(result, a)
    return result


def qmul(a, b):
    return (a[0]*b[0]-a[1]*b[1]-a[2]*b[2]-a[3]*b[3],
            a[0]*b[1]+a[1]*b[0]+a[2]*b[3]-a[3]*b[2],
            a[0]*b[2]-a[1]*b[3]+a[2]*b[0]+a[3]*b[1],
            a[0]*b[3]+a[1]*b[2]-a[2]*b[1]+a[3]*b[0])


def qconj(a):
    return a[0], -a[1], -a[2], -a[3]


def pair_to_quaternion(u, v):
    return u[0], u[1], v[0], -v[1]


def polynomial_value(poly, point):
    return sum((coefficient * product(point, powers)
                for powers, coefficient in poly.items()), Q(0))


def product(point, powers):
    result = Q(1)
    for coordinate, exponent in zip(point, powers):
        result *= coordinate ** exponent
    return result


def determinant(matrix):
    a = [list(row) for row in matrix]
    result = Q(1)
    for col in range(len(a)):
        pivot = next((row for row in range(col, len(a)) if a[row][col]), None)
        if pivot is None:
            return Q(0)
        if pivot != col:
            a[pivot], a[col] = a[col], a[pivot]
            result = -result
        value = a[col][col]
        result *= value
        for row in range(col + 1, len(a)):
            multiplier = a[row][col] / value
            for j in range(col + 1, len(a)):
                a[row][j] -= multiplier * a[col][j]
    return result


def complex_heat(degree, tau, z):
    if degree < 0:
        return Q(0), Q(0)
    result = Q(0), Q(0)
    for r in range(degree // 2 + 1):
        coefficient = Q((-1)**r * factorial(degree),
                        factorial(r) * factorial(degree - 2*r))
        result = cadd(result, cscale(cmul(cpow(tau, r), cpow(z, degree - 2*r)), coefficient))
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--polynomial-utilities", type=Path,
                        default=Path(__file__).with_name("check_fueter_boundary_identities.py"))
    args = parser.parse_args()
    spec = importlib.util.spec_from_file_location("exact_polynomial_utilities", args.polynomial_utilities)
    p = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(p)
    tests = {}
    complex_values = [(Q(2, 3), Q(-3, 5)), (Q(-7, 4), Q(5, 6)),
                      (Q(1, 8), Q(2, 7)), (Q(-4, 9), Q(-1, 11))]
    for shift in range(len(complex_values)):
        a, b, c, d = complex_values[shift:] + complex_values[:shift]
        pair_product = pair_to_quaternion(
            cadd(cmul(a, c), cscale(cmul(cconj(b), d), -1)),
            cadd(cmul(b, c), cmul(cconj(a), d)))
        tests["hamilton_pair_product_" + str(shift)] = (
            qmul(pair_to_quaternion(a, b), pair_to_quaternion(c, d)) == pair_product)
        tests["hamilton_pair_conjugate_" + str(shift)] = (
            qconj(pair_to_quaternion(a, b)) == pair_to_quaternion(cconj(a), cscale(b, -1)))

    # (a,b,c,e) are the standard oriented Hamilton coordinates; d=-e.
    points = ((Q(2, 3), Q(1, 4), Q(-1, 5), Q(2, 7)),
              (Q(-3, 8), Q(4, 9), Q(1, 6), Q(-5, 11)))
    time = Q(2, 7)
    records = []
    for degree, constant_term in ((2, 0), (3, 0), (4, 0), (6, 0), (2, 1)):
        label = "P" if constant_term else "H_" + str(degree)
        field = p.lift(degree, time, constant_term)
        dplus = p.fueter_residual(field)
        da = tuple(p.deriv(component, 0) for component in field)
        # Dminus = 2*d_a - Dplus, divided by 2 for normalized partial_q.
        conjugate_derivative = tuple(p.scale(p.add(p.scale(x, 2), p.scale(y, -1)), Q(1, 2))
                                     for x, y in zip(da, dplus))
        tests[label + "_fueter_polynomial"] = all(not component for component in dplus)
        tests[label + "_normalized_conjugate_derivative"] = conjugate_derivative == da
        second = tuple(p.deriv(component, 0) for component in da)
        external_time = tuple(p.deriv(component, 2) for component in field)
        tests[label + "_external_heat"] = all(not p.add(a, b) for a, b in zip(external_time, second))
        tests[label + "_derivative_regular"] = all(not component for component in p.fueter_residual(da))
        for index, point in enumerate(points):
            z = point[0], point[1]
            tau = time + point[2], point[3]
            h = []
            for derivative_order in range(4):
                coefficient = Q(factorial(degree), factorial(degree - derivative_order)) if derivative_order <= degree else Q(0)
                h.append(cscale(complex_heat(degree - derivative_order, tau, z), coefficient))
            h[0] = cadd(h[0], (Q(constant_term), Q(0)))
            actual_field = tuple(polynomial_value(component, point) for component in field)
            tests[label + "_complex_lift_" + str(index)] = actual_field == pair_to_quaternion(h[0], h[1])
            matrix = [[polynomial_value(p.deriv(component, axis), point) for axis in range(4)]
                      for component in field]
            laguerre_1 = cadd(cmul(h[2], h[2]), cscale(cmul(h[1], h[3]), -1))
            expected_det = -(laguerre_1[0]**2 + laguerre_1[1]**2)
            actual_det = determinant(matrix)
            tests[label + "_negative_real_jacobian_" + str(index)] = actual_det == expected_det
            jet1 = pair_to_quaternion(h[1], h[2])
            jet2 = pair_to_quaternion(h[2], h[3])
            signed_product = qmul(qconj(jet1), jet2)
            # -j*(L_real+i*L_imag) has j coefficient -L_real and k coefficient +L_imag.
            tests[label + "_complex_laguerre_orientation_" + str(index)] = (
                signed_product[2] == -laguerre_1[0] and signed_product[3] == laguerre_1[1])
            records.append({"case": label, "point_abce": list(map(str, point)),
                            "real_jacobian_determinant": str(actual_det),
                            "complex_L1": list(map(str, laguerre_1))})
    result = {"checker_source_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
              "polynomial_utilities_sha256": sha256(args.polynomial_utilities.read_bytes()).hexdigest(),
              "arithmetic": "fractions.Fraction (exact)",
              "date": "2026-10-14", "prepared_for": "Edward Baker",
              "model": "gpt-6.1-sol", "reasoning_effort": "ultra",
              "scope": "Exact rational polynomial and orientation checks; not a theta sign certificate",
              "coordinate_convention": "q=a+i*b+j*c+k*e; z0=a+i*b; z1=c-i*e; tau=t+c+i*e",
              "checks": tests, "all_pass": all(tests.values()), "complex_point_records": records}
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"all_pass": result["all_pass"], "check_count": len(tests),
                      "checker_source_sha256": result["checker_source_sha256"]}))
    if not result["all_pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
