#!/usr/bin/env python3
"""Exact finite algebra for dressed Schur returns; no Weil positivity claim."""

from fractions import Fraction as F
import json


def product(values):
    answer = F(1)
    for value in values:
        answer *= value
    return answer


def u_minus(q, state):
    result = {}
    for (magnetic, electric), coefficient in state.items():
        for key, value in (
            ((magnetic - 1, electric), q**(-electric)*coefficient),
            ((magnetic - 1, electric + 1),
             q**(-electric - magnetic)*coefficient),
        ):
            result[key] = result.get(key, F(0)) + value
    return {key: value for key, value in result.items() if value}


def multiply_by_linear(poly, coefficient):
    result = [F(0)] * (len(poly) + 1)
    for n, value in enumerate(poly):
        result[n] += value
        result[n + 1] += coefficient*value
    return result


def evaluate(poly, argument):
    result = F(0)
    for value in reversed(poly):
        result = result*argument + value
    return result


def main():
    counts = {}
    count = 0
    for q in (F(1, 2), F(2, 3), F(4, 5)):
        for r in (F(1, 3), F(1, 2), F(3, 4)):
            a = q*r
            for maximum in (3, 6, 9):
                state = {(0, n): (-a)**n for n in range(maximum + 1)}
                actual = u_minus(q, state)
                expected = {(-1, 0): F(1)}
                for n in range(1, maximum + 1):
                    expected[-1, n] = (1-r)*(-r)**(n-1)
                # The shifted final coefficient is part of the finite vector.
                expected[-1, maximum+1] = (-r)**maximum
                assert actual == expected
                norm = sum(value*value for value in actual.values())
                assert norm == F(2)/(1+r) + 2*r**(2*maximum+1)/(1+r)
                count += 2
    counts['magnetic_action_and_finite_vector_norm'] = count

    count = 0
    for r in (F(1, 5), F(1, 3), F(1, 2), F(2, 3), F(4, 5)):
        for d in (F(1, 3), F(1), F(7, 4)):
            amplitude_squared = d*r*(1+r)/(1-r)
            contact = 2*d*r/(1-r)
            # Sum products of filter coefficients, retaining exact geometric tails.
            mean = amplitude_squared*(1+(1-r)**2/(1-r*r))
            assert mean == contact
            count += 1
            for m in range(1, 10):
                coefficient = amplitude_squared*(
                    -(1-r)*r**(m-1) + (1-r)**2*r**m/(1-r*r)
                )
                assert coefficient == -d*r**m
                count += 1
            for cosine in (F(-1), F(-3, 5), F(0), F(3, 5), F(1)):
                denominator = 1-2*r*cosine+r*r
                direct = amplitude_squared*(2-2*cosine)/denominator
                geometric = contact-2*d*(r*cosine-r*r)/denominator
                assert direct == geometric
                assert direct >= 0
                if cosine == 1:
                    assert direct == 0
                count += 1
    counts['full_prime_multiplier_and_all_coefficient_formula'] = count

    count = 0
    for q in (F(1, 2), F(2, 3), F(4, 5)):
        for a in (F(1, 5), F(2, 5), q, q**3, q**5):
            maximum = 11
            state = {(0, n): (-a)**n for n in range(maximum + 1)}
            for k in range(1, 6):
                state = u_minus(q, state)
                poly = [F(1)]
                for j in range(k):
                    poly = multiply_by_linear(poly, q**(k-1-2*j))
                pole_value = evaluate(poly, -q**k/a)
                assert pole_value == product(
                    1-q**(2*j+1)/a for j in range(k)
                )
                # Only interior coefficients of the truncated input are compared.
                for n in range(k, maximum + 1):
                    assert state.get((-k, n), F(0)) == (
                        (-a*q**(-k))**n * pole_value
                    )
                count += 1
                for j in range(k):
                    cancelling_a = q**(2*j+1)
                    assert evaluate(poly, -q**k/cancelling_a) == 0
                    count += 1
    counts['higher_magnetic_action_and_pole_cancellation'] = count

    count = 0
    # A state with one allowed insertion but a forbidden third insertion.
    q, a = F(2, 3), F(1, 3)
    assert a < q*q and a > q**3
    witness = product(1-q**(2*j+1)/a for j in range(3))
    assert witness != 0 and a/q**3 > 1
    count += 1
    for r in (F(1, 3), F(1, 2), F(3, 4)):
        for s in (F(1, 4), F(2, 3)):
            # This is the coefficient of z_2^{-1} z_3 in conjugate(A_2) A_3.
            cross_coefficient = (1-r)*(1-s)
            assert cross_coefficient > 0
            count += 1
    matches = [(n, m) for n in range(1, 13) for m in range(1, 13)
               if F(3**m, 2**n) == F(3, 2)]
    assert matches == [(1, 1)]
    count += 1
    counts['domain_witness_and_first_mixed_return'] = count

    print(json.dumps({
        'status': 'passed',
        'date': '2026-09-14',
        'arithmetic': 'exact rational',
        'checks': counts,
        'total_checks': sum(counts.values()),
        'scope': (
            'Finite coefficient checks of the written dressed-state identities. '
            'Finite magnetic vectors retain their shifted boundary coefficient. '
            'Infinite geometric sums are evaluated by the stated closed formulas; '
            'the program does not prove analytic domains or QFT construction. '
            'The mixed-return uniqueness sample is not a replacement for the '
            'unique-factorization proof. No full Weil positivity or RH claim.'
        ),
    }, indent=2))


if __name__ == '__main__':
    main()
