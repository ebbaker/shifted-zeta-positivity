#!/usr/bin/env python3
"""Exact finite algebra for the derivative-core and threshold-jet continuation.

Prepared for Edward Baker with substantial LLM assistance, 9 October 2026.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.

These checks concern polynomial identities, scalar exponent reserves, and
finite real-root polynomial models. No actual heat function, physical phase,
large cutoff, analytic limit, Hilbert inequality, or RH assertion is checked.
Stdout is deterministic JSON; --output optionally saves the same bytes.
"""
import argparse
from fractions import Fraction as F
import hashlib
import itertools
import json
from pathlib import Path

COUNTS = {}


def check(group, assertion):
    if not assertion:
        raise AssertionError(group)
    COUNTS[group] = COUNTS.get(group, 0) + 1


# Sparse exact polynomials; every monomial is an exponent tuple.
def add(*polys):
    result = {}
    for poly in polys:
        for key, value in poly.items():
            result[key] = result.get(key, F(0)) + value
    return {key: value for key, value in result.items() if value}


def scale(poly, value):
    return {key: value * coeff for key, coeff in poly.items() if value * coeff}


def mul(left, right):
    result = {}
    for a, x in left.items():
        for b, y in right.items():
            key = tuple(i + j for i, j in zip(a, b))
            result[key] = result.get(key, F(0)) + x * y
    return {key: value for key, value in result.items() if value}


def variable(index, dimensions):
    key = tuple(1 if i == index else 0 for i in range(dimensions))
    return {key: F(1)}


def constant(value, dimensions):
    return {(0,) * dimensions: F(value)} if value else {}


def derivative(poly, index, order=1):
    for _ in range(order):
        result = {}
        for key, value in poly.items():
            if key[index]:
                new = list(key)
                new[index] -= 1
                result[tuple(new)] = value * key[index]
        poly = result
    return poly


def evaluate(poly, values):
    return sum((coeff * product(value ** degree for value, degree in zip(values, key))
                for key, coeff in poly.items()), F(0))


def product(values):
    result = F(1)
    for value in values:
        result *= value
    return result


def jet_polynomial(q2, q3, q4, gamma):
    return 2 * q3 * q3 - 3 * q2 * q4 - gamma * q2 * q2


def normalization_and_heat_identities():
    # Variables q2,q3,q4,b,b_x,mu where mu=9/x^2.
    q2, q3, q4, b, bx, mu = (variable(i, 6) for i in range(6))
    h2 = q2
    h3 = add(q3, scale(mul(b, q2), 3))
    h4 = add(q4, scale(mul(b, q3), 4),
             scale(mul(add(mul(b, b), bx), q2), 6))
    lhs = add(scale(mul(h3, h3), 2), scale(mul(h2, h4), -3),
              scale(mul(mu, mul(h2, h2)), -1))
    rhs = add(scale(mul(q3, q3), 2), scale(mul(q2, q4), -3),
              scale(mul(add(scale(bx, 18), mu), mul(q2, q2)), -1))
    check('symbolic_normalization', lhs == rhs)
    # Deflation g=H/(z-x)^2: 72(g'^2-gg'') = 2h3^2-3h2h4.
    check('symbolic_normalization', F(72, 36) == 2)
    check('symbolic_normalization', F(72, 24) == 3)
    check('symbolic_normalization', F(72, 8) == 9)

    # Exact backward heat model in variables z,delta,a^2.
    z, delta, a2 = (variable(i, 3) for i in range(3))
    z2 = mul(z, z)
    model = add(mul(z2, z2),
                scale(mul(add(scale(a2, 2), scale(delta, 12)), z2), -1),
                mul(a2, a2), scale(mul(a2, delta), 4), scale(mul(delta, delta), 12))
    check('symbolic_heat_model', add(derivative(model, 1), derivative(model, 0, 2)) == {})
    h = [evaluate(derivative(model, 0, j), (F(3), F(0), F(9))) for j in range(5)]
    check('symbolic_heat_model', h[0] == h[1] == 0)
    check('symbolic_heat_model', h[2:] == [F(72), F(72), F(24)])
    check('symbolic_heat_model', 2 * h[3]**2 - 3 * h[2] * h[4] == 9 * h[2]**2 / 9)
    # Discriminant in z^2: (2a^2+12delta)^2 - 4C =32delta(a^2+3delta).
    total = add(scale(a2, 2), scale(delta, 12))
    cterm = add(mul(a2, a2), scale(mul(a2, delta), 4), scale(mul(delta, delta), 12))
    disc = add(mul(total, total), scale(cterm, -4))
    check('symbolic_heat_model', disc == scale(mul(delta, add(a2, scale(delta, 3))), 32))


def scalar_and_exponent_checks():
    k = variable(0, 1)
    a = add(scale(k, F(1, 4)), scale(mul(k, k), F(-1, 16)))
    b = add(scale(k, F(1, 4)), scale(mul(k, k), F(1, 16)))
    check('continuous_exponents', add(a, scale(b, -1)) == scale(mul(k, k), F(-1, 8)))
    check('continuous_exponents', add(scale(a, 2), scale(k, F(-1, 2))) ==
          scale(mul(k, k), F(-1, 8)))
    check('continuous_exponents', add(scale(a, 5), scale(k, -1), constant(F(1, 16), 1)) ==
          scale(mul(add(k, constant(-1, 1)), add(scale(k, 5), constant(1, 1))), F(-1, 16)))
    check('continuous_exponents', F(3) * F(3, 16) == F(9, 16))
    check('continuous_exponents', F(8) / F(2)**2 == 2)
    check('continuous_exponents', F(8) / F(1)**2 == 8)

    beta, s_min = F(7, 8), F(5, 8)
    powers = (3 * beta / 4, beta - F(1, 6), beta / 4 + F(1, 4))
    check('derivative_edge', max(powers) == F(17, 24))
    for j, expected in [(1, F(-1, 24)), (2, F(-1, 6)),
                        (3, F(-7, 24)), (4, F(-5, 12))]:
        check('derivative_edge', max(powers) - s_min + j * (beta - 1) == expected)
    check('derivative_edge', F(7, 8) < F(43, 48))
    check('derivative_edge', F(3, 4) < F(7, 8))
    check('derivative_edge', F(6) < F(8, 5)**4)
    check('derivative_edge', 36 * 11**6 < 20**6)
    check('derivative_edge', 11 * F(8, 5) < 20)
    check('derivative_edge', 11 < 20)
    check('derivative_edge', F(201, 100) / F(7, 10)**3 < 6)
    check('derivative_edge', 20 * 40 == 800)

    # Original edge pays a quadratic jet; the deeper derivative edge does not
    # automatically pay it by the absolute e^(a/t) jet budget.
    beta, pmax = F(3, 4), F(7, 12)
    for j, expected in [(2, F(-13, 24)), (3, F(-19, 24)), (4, F(-25, 24))]:
        check('quadratic_jet_edge', pmax - s_min + j * (beta - 1) == expected)
    check('quadratic_jet_edge', F(-13, 24) + F(3, 8) == F(-1, 6))
    check('quadratic_jet_edge', F(-19, 24) + F(3, 8) == F(-5, 12))
    check('quadratic_jet_edge', F(-25, 24) + F(3, 8) == F(-2, 3))
    check('quadratic_jet_edge', F(-1, 6) + F(3, 8) == F(5, 24) > 0)

    # For d>=4, Arias's first raw value exponent alone caps beta<=5/7,
    # whereas d=3 permits the uniform strict threshold19/24.
    check('derivative_order_limit', F(5, 8) / F(7, 8) == F(5, 7))
    check('derivative_order_limit', F(5, 7) < F(19, 24))
    check('derivative_order_limit', F(19, 24) < 1)
    j, s = (variable(i, 2) for i in range(2))
    js = add(j, s)
    # Cross-multiply the d3 middle threshold against the d>=4 first cap.
    cross = add(mul(add(js, constant(F(1, 6), 2)), add(j, constant(F(7, 8), 2))),
                scale(mul(js, add(j, constant(1, 2))), -1))
    check('derivative_order_limit', cross == add(scale(j, F(1, 24)),
          scale(s, F(-1, 8)), constant(F(7, 48), 2)))
    check('derivative_order_limit', F(7, 48) - F(3, 4) / 8 > 0)
    check('hilbert_scalar_reserves', 3 * 4 == 12)
    check('hilbert_scalar_reserves', F(1, 2) - F(1, 8) == F(3, 8))
    check('hilbert_scalar_reserves', F(1, 8) - F(1, 16) == F(1, 16))
    check('hilbert_scalar_reserves', F(4, 3) == 4 * F(1, 3))
    for n in (2, 3, 4, 16, 256, 22000):
        check('hilbert_scalar_reserves', F(n - 1, n) >= F(1, 2))


def paid_jet_checks():
    cases = 0
    for f2, f3, f4, gamma in itertools.product((F(-2), F(0), F(3)), repeat=4):
        errors = (F(1, 7), F(1, 11), F(1, 13))
        e2, e3, e4 = errors
        bound = (4 * abs(f3) * e3 + 2 * e3**2 + 3 * abs(f2) * e4
                 + 3 * abs(f4) * e2 + 3 * e2 * e4
                 + abs(gamma) * (2 * abs(f2) * e2 + e2**2))
        for shifts in itertools.product((-1, 0, 1), repeat=3):
            q2, q3, q4 = (f + sign * error
                          for f, sign, error in zip((f2, f3, f4), shifts, errors))
            difference = abs(jet_polynomial(q2, q3, q4, gamma)
                             - jet_polynomial(f2, f3, f4, gamma))
            check('paid_jet_model', difference <= bound)
            cases += 1
    check('paid_jet_model', cases == 2187)


def real_root_deflation_models():
    for x in (F(1), F(2), F(3), F(5, 2)):
        for multiplicity in (2, 3, 4, 5):
            for extra_count in (0, 1, 2):
                z = variable(0, 1)
                own = add(z, constant(-x, 1))
                mirror = add(z, constant(x, 1))
                g = constant(1, 1)
                for _ in range(multiplicity - 2):
                    g = mul(g, own)
                for _ in range(multiplicity):
                    g = mul(g, mirror)
                for index in range(extra_count):
                    root = x + index + 1
                    g = mul(g, add(mul(z, z), constant(-root * root, 1)))
                h = mul(mul(own, own), g)
                derivatives = [evaluate(derivative(h, 0, j), (x,)) for j in range(5)]
                h2, h3, h4 = derivatives[2:]
                check('real_root_models', derivatives[0] == derivatives[1] == 0)
                check('real_root_models', 2 * h3**2 - 3 * h2 * h4 >= 9 * h2**2 / x**2)
                g0 = evaluate(g, (x,))
                g1 = evaluate(derivative(g, 0), (x,))
                g2 = evaluate(derivative(g, 0, 2), (x,))
                check('real_root_models', 72 * (g1**2 - g0 * g2) == 2 * h3**2 - 3 * h2 * h4)
                if multiplicity == 2 and extra_count == 0:
                    check('real_root_models', 2 * h3**2 - 3 * h2 * h4 == 9 * h2**2 / x**2)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    normalization_and_heat_identities()
    scalar_and_exponent_checks()
    paid_jet_checks()
    real_root_deflation_models()
    record = {
        'date': '2026-10-09',
        'investigation': 'local heat jet and asymmetric derivative input',
        'model': 'GPT-6 (Codex), inherited configuration; exact serving variant not exposed',
        'reasoning_effort': 'not exposed; not inferred',
        'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'assertions': sum(COUNTS.values()),
        'assertions_by_category': dict(sorted(COUNTS.items())),
        'arithmetic': 'exact integers, fractions, and sparse polynomials',
        'result': 'pass',
        'scope': ['symbolic normalized jet and backward-heat identities',
                  'finite scalar reserves and paid perturbation models',
                  'finite real-root polynomial deflation and mirror-bound models'],
        'not_certified': ['actual heat functions, genuine phases, large cutoffs or numerical zeros',
                          'imported Hilbert or derivative theorems, analytic limits, or canonical products',
                          'the missing signed jet implication, pointwise collision exclusion, RH or novelty'],
    }
    output = json.dumps(record, indent=2, sort_keys=True) + '\n'
    if args.output:
        args.output.write_text(output, encoding='utf-8')
    print(output, end='')


if __name__ == '__main__':
    main()
