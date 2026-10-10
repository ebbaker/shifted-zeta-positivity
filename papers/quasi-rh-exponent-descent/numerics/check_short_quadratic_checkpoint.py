#!/usr/bin/env python3
"""Exact finite algebra for the 2026-10-09 short/quadratic checkpoints.

No floating prime asymptotic, imported sieve theorem, or target moment is
tested. Finite rational substitutes verify identities valid for all positive
row weights and complex coefficients. Inherited model configuration.
"""
from fractions import Fraction as F
from itertools import product
from math import comb
from pathlib import Path
import json

from check_integer_quadratic_lift import factors, jacobi


ASSERTIONS = 0


def check(condition):
    global ASSERTIONS
    assert condition
    ASSERTIONS += 1


def add(z, w):
    return z[0] + w[0], z[1] + w[1]


def sub(z, w):
    return z[0] - w[0], z[1] - w[1]


def scale(t, z):
    return t*z[0], t*z[1]


def norm(z):
    return z[0]**2 + z[1]**2


def real_inner(z, w):
    return z[0]*w[0] + z[1]*w[1]


def sum_z(items):
    value = F(0), F(0)
    for z in items:
        value = add(value, z)
    return value


def coherent_covariance_checks():
    cases = 0
    for size in range(1, 9):
        weights = [F(i+1, i+2) for i in range(size)]
        mass = sum(weights)
        for seed in range(1, 29):
            block = F(seed % 5 - 2, seed % 3 + 1), F(seed % 7 - 3, 4)
            residual = [(F((seed+3*i) % 11 - 5, i+2),
                         F((2*seed+i) % 9 - 4, i+3)) for i in range(size)]
            mean = scale(1/mass, sum_z(scale(w, r) for w, r in zip(weights, residual)))
            variance = sum(w*norm(sub(r, mean)) for w, r in zip(weights, residual))
            A = mass*norm(block)
            C = sum(w*norm(r) for w, r in zip(weights, residual))
            cross = sum(w*real_inner(block, r) for w, r in zip(weights, residual))
            energy = sum(w*norm(add(block, r)) for w, r in zip(weights, residual))
            check(energy == mass*norm(add(block, mean)) + variance)
            check(C == mass*norm(mean) + variance)
            check(cross == mass*real_inner(block, mean))
            check(energy == A+C+2*cross)
            check(cross**2 <= A*C)
            check(variance >= 0)
            check(mass*norm(add(block, mean)) <= energy)
            if A > 0 and C > 0:
                # The algebra underlying the angle identity, without sqrt floats.
                check(energy/A == 1+C/A+2*cross/A)
            cases += 1
    # Exact cancellation of the mean alone leaves a nonzero variance.
    block = F(1), F(2)
    residual = [(F(-2), F(-2)), (F(0), F(-2))]
    mean = scale(F(1, 2), sum_z(residual))
    check(mean == scale(-1, block))
    check(sum(norm(add(block, r)) for r in residual) == 2)
    return cases


def finite_span_checks():
    # Two distinct allowed prime-ideal symbols can have the same norm 7.
    # Powers of 7 let log labels be represented exactly as multiples of log(7).
    blocks = [(), ("p",), ("q",), ("p", "q")]
    cases, nonzero_cases, norm_zero_cases = 0, 0, 0
    first_orders = {}
    scalar_tuples = list(product((-2, -1, 0, 1, 2), repeat=4))
    # Tuned complete-block coefficients cancel one or two leading moments.
    # The second gives normalized grouped weights (1,-2,1).
    scalar_tuples += [(F(-6, 7), F(1), F(0), F(0)), (36, -84, 0, 49)]
    for scalar_tuple in scalar_tuples:
        if scalar_tuple == (0, 0, 0, 0):
            continue
        measure = {}
        for ideal, scalar in zip(blocks, scalar_tuple):
            for flags in product((0, 1), repeat=len(ideal)):
                degree = sum(flags)
                measure[degree] = measure.get(degree, F(0)) + F(scalar)*(-1)**degree/F(7**degree)
        measure = {degree: coefficient for degree, coefficient in measure.items() if coefficient}
        if not measure:
            norm_zero_cases += 1
            check(scalar_tuple[0] == 0 and scalar_tuple[3] == 0
                  and scalar_tuple[1] == -scalar_tuple[2])
            cases += 1
            continue
        nonzero_cases += 1
        support = sorted(measure)
        log_moments = [sum(c*degree**j for degree, c in measure.items())
                       for j in range(len(support)+6)]
        first = next(j for j, moment in enumerate(log_moments) if moment)
        check(first <= len(support)-1)
        first_orders[first] = first_orders.get(first, 0) + 1
        for k0 in (1, 2, 3, 4):
            moments = [F(0)]*k0 + [F(5, 7)] + [F(j+2, j+3) for j in range(10)]
            K = k0 + first
            for k in range(K+1):
                convolution = sum(F(comb(k, j))*moments[j]*log_moments[k-j]
                                  for j in range(k+1))
                translated = sum(c*sum(F(comb(k, j))*moments[j]*degree**(k-j)
                                       for j in range(k+1))
                                 for degree, c in measure.items())
                check(convolution == translated)
                if k < K:
                    check(convolution == 0)
                else:
                    check(convolution == comb(K, k0)*moments[k0]*log_moments[first] != 0)
        cases += 1
    # B_p - (1-1/q) B_1: leading measure moment zero, next one nonzero.
    q = 7
    c_unit, c_prime = F(1, q), F(-1)
    check(c_unit + c_prime/q == 0)
    check(c_prime/q == F(-1, 7))  # coefficient of log(7) in L_1
    for k0 in range(1, 9):
        K = k0+1
        alpha = sum(F(1, 2**(K-j)*j) for j in range(1, K+1))
        check(alpha > 0)
        check(comb(K, k0)*F(5, 7)*F(-1, 7) != 0)
    check(first_orders[1] > 0 and first_orders[2] > 0)
    return {"cases": cases, "nonzero_grouped_measures": nonzero_cases,
            "exact_norm_group_cancellations": norm_zero_cases,
            "first_logarithmic_orders": first_orders,
            "labels": "two distinct norm-7 prime symbols; log labels in units of log(7)"}


def squarefree(n):
    return all(e == 1 for e in factors(n).values())


def prime_power(n):
    fac = factors(n)
    return next(iter(fac)) if len(fac) == 1 else None


def signed_quadratic_checks():
    cases, masks, cross_nonzero, near_nonzero, far_nonzero = 0, 0, 0, 0, 0
    for Q in (9, 21, 35):
        rows = [a for a in range(1, Q+1, 2) if squarefree(a)]
        weights = {a: F(1, a) for a in rows}
        for low, high in ((2, 80), (13, 121), (Q+1, Q+130)):
            numbers = [n for n in range(low, high+1) if prime_power(n)]
            primes = [n for n in numbers if factors(n) == {n: 1} and n % 2]
            powers = [n for n in numbers if n not in primes]
            # Rational signed profile weights replace only transcendental values.
            # All powers of 2 and the prime 2 are part of R.
            coeff = {n: F((n % 13 - 6)*(prime_power(n) % 7 + 1), n % 5 + 1)
                     for n in numbers}
            S = {a: sum(coeff[n]*jacobi(n, a) for n in numbers) for a in rows}
            P = {a: sum(coeff[p]*jacobi(p, a) for p in primes) for a in rows}
            R = {a: sum(coeff[n]*jacobi(n, a) for n in powers) for a in rows}
            ES = sum(weights[a]*S[a]**2 for a in rows)
            EP = sum(weights[a]*P[a]**2 for a in rows)
            ER = sum(weights[a]*R[a]**2 for a in rows)
            cross = sum(weights[a]*P[a]*R[a] for a in rows)
            check(ES == EP+ER+2*cross)
            check(cross**2 <= EP*ER)
            cross_nonzero += cross != 0
            for a in rows:
                check(S[a] == P[a]+R[a])
            kernel = {(p, q): sum(weights[a]*jacobi(p*q, a) for a in rows)
                      for p in primes for q in primes}
            diagonal = sum(coeff[p]**2*kernel[p, p] for p in primes)
            for p in primes:
                check(kernel[p, p] == sum(weights[a] for a in rows if a % p))
                if p <= Q:
                    check(kernel[p, p] <= sum(weights.values()))
                    masks += 1
            for Delta in (2, 4, 10, 30):
                near_pairs = [(p, q) for p in primes for q in primes
                              if p != q and abs(p-q) <= Delta]
                far_pairs = [(p, q) for p in primes for q in primes if abs(p-q) > Delta]
                near = sum((coeff[p]*coeff[q]*kernel[p, q] for p, q in near_pairs), F(0))
                far = sum((coeff[p]*coeff[q]*kernel[p, q] for p, q in far_pairs), F(0))
                check(EP == diagonal+near+far)
                check(ES == far+near+diagonal+ER+2*cross)
                check(len(near_pairs)+len(far_pairs) == len(primes)*(len(primes)-1))
                check(len(near_pairs) <= len(primes)*2*Delta)
                if primes:
                    pair_bound = len(near_pairs)*max(abs(coeff[p]) for p in primes)**2*sum(weights.values())
                    check(abs(near) <= pair_bound)
                near_nonzero += near != 0
                far_nonzero += far != 0
                # The integer threshold is assigned to near, strictly > to far.
                for p, q in near_pairs:
                    check(abs(p-q) <= Delta)
                for p, q in far_pairs:
                    check(abs(p-q) > Delta)
                cases += 1
    check(masks > 0 and cross_nonzero > 0 and near_nonzero > 0 and far_nonzero > 0)
    return {"cases": cases, "small_scale_diagonal_masks": masks,
            "nonzero_prime_power_cross_cases": cross_nonzero,
            "nonzero_near_pair_cases": near_nonzero, "nonzero_far_pair_cases": far_nonzero,
            "weights": "arbitrary positive rational row weights 1/a, finite rational signed columns"}


def budget_checks():
    cases = []
    for h in (F(6, 5), F(4, 3), F(7, 5), F(3, 2), F(7, 4), F(19, 10)):
        T = 1+h/2
        cross = 2-h/4
        check(T-cross == 3*h/4-1)
        check((T-cross > 0) == (h > F(4, 3)))
        diagonal = 2-h/2
        check(T-diagonal == h-1)
        for delta in (F(1, 100), F(1, 40), F(1, 10)):
            if delta >= h-1:
                continue
            d = h-1-delta
            near = 2-h/2+d
            check(near == T-delta)
            check(2-near > 0)  # Removed absolute sector is o(X^2).
            rho = min(h-1, 3*h/4-1, delta)
            if h > F(4, 3):
                check(rho > 0)
                check(max(diagonal, cross, near) == T-rho)
            cases.append({"h": str(h), "delta": str(delta), "gap_power": str(d),
                          "target_power": str(T), "additive_reserve": str(rho)})
    h, delta = F(7, 5), F(1, 40)
    check(2-h == F(3, 5))
    check(h-1-delta == F(3, 8))
    check(2-h/4 == F(33, 20))
    check(2-h/2 == F(13, 10))
    check(1+h/2-delta == F(67, 40))
    check((1+h/2)/2 == F(17, 20))
    # Short coherent count, block energy and required covariance accuracy.
    mass_power, block_response_power, target = F(-14, 15), F(1), F(4, 5)
    block_energy = mass_power + 2*block_response_power
    check(block_energy == F(16, 15))
    check(target-block_energy == F(-4, 15))
    check((target-block_energy)/2 == F(-2, 15))
    check((target-mass_power)/2 == F(13, 15))
    return cases


def main():
    coherent = coherent_covariance_checks()
    span = finite_span_checks()
    quadratic = signed_quadratic_checks()
    budgets = budget_checks()
    result = {
        "date": "2026-10-09", "arithmetic": "exact integer and rational; complex values as rational pairs",
        "assertions": ASSERTIONS, "coherent_covariance_cases": coherent,
        "fixed_signed_cofactor_span": span, "quadratic_signed_partitions": quadratic,
        "rational_budget_checks": budgets,
        "example": {"h": "7/5", "Q_power": "3/5", "strict_far_gap_power": "3/8",
                    "target_power": "17/10", "comparison_error_power": "67/40", "reserve": "1/40",
                    "prime_power_cross_power": "33/20", "short_mean_relative_power": "-2/15",
                    "short_angle_defect_power": "-4/15"},
        "scope": "Finite covariance, signed cofactor moment, signed prime/power pair identities and budgets; no target moment or new strip.",
    }
    output = Path(__file__).with_name("short_quadratic_checkpoint_record_20261009.json")
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(f"PASS: {ASSERTIONS} exact assertions; {coherent} covariance cases; "
          f"{span['cases']} finite signed spans; {quadratic['cases']} signed pair partitions")


if __name__ == "__main__":
    main()
