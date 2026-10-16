#!/usr/bin/env python3
"""Exact finite algebra for the nonsquarefree adaptive-tail projection.

8 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; the exact serving variant and
configured reasoning effort are not exposed and are not inferred.

Standard library only. Ideals are exponent vectors on three DISTINCT prime
symbols with norms 7, 7, and 13. Thus norm ties cannot substitute for ideal
equality or divisibility. Phases are exact sixth roots in Z[omega], including
original zero extensions. Prints deterministic JSON and writes no files.

This is finite verification, not a certificate of reciprocity, completion,
large-sieve bounds, ideal asymptotics, or the missing full tail moment.
"""

import bisect
import itertools
import json
from fractions import Fraction
from functools import lru_cache


PRIME_NORMS = (7, 7, 13)
DIMENSION = len(PRIME_NORMS)
UNIT = (0,) * DIMENSION
ZERO = (0, 0)
ONE = (1, 0)
# zeta_6=1+omega and omega^2+omega+1=0.
ROOTS = ((1, 0), (1, 1), (0, 1), (-1, 0), (-1, -1), (0, -1))
assertions = 0


def check(condition, detail=""):
    global assertions
    assertions += 1
    if not condition:
        raise AssertionError(detail or "exact assertion failed")


def zmul(x, y):
    a, b = x
    c, d = y
    return (a * c - b * d, a * d + b * c - b * d)


def zadd(x, y):
    return (x[0] + y[0], x[1] + y[1])


def zscale(k, x):
    return (k * x[0], k * x[1])


def zsum(values):
    value = ZERO
    for item in values:
        value = zadd(value, item)
    return value


def znorm(x):
    return x[0] ** 2 - x[0] * x[1] + x[1] ** 2


def zpower(x, exponent):
    value = ONE
    for _ in range(exponent):
        value = zmul(value, x)
    return value


@lru_cache(None)
def norm(n):
    value = 1
    for p, exponent in zip(PRIME_NORMS, n):
        value *= p ** exponent
    return value


def multiply(n, m):
    return tuple(x + y for x, y in zip(n, m))


def power(n, exponent):
    return tuple(exponent * x for x in n)


def divides(d, n):
    return all(x <= y for x, y in zip(d, n))


def quotient(n, d):
    assert divides(d, n)
    return tuple(x - y for x, y in zip(n, d))


def gcd(n, m):
    return tuple(min(x, y) for x, y in zip(n, m))


@lru_cache(None)
def divisors(n):
    return tuple(itertools.product(*(range(x + 1) for x in n)))


@lru_cache(None)
def square_divisors(n):
    # Includes nonsquarefree k, whose Mobius coefficient must vanish.
    return tuple(itertools.product(*(range(x // 2 + 1) for x in n)))


def mobius(n):
    if any(x >= 2 for x in n):
        return 0
    return (-1) ** sum(n)


def nonsquarefree(n):
    return int(any(x >= 2 for x in n))


def phase(n, prime_values):
    value = ONE
    for exponent, prime_value in zip(n, prime_values):
        value = zmul(value, zpower(prime_value, exponent))
    return value


def join_phase_values(first, second):
    return tuple(zmul(x, y) for x, y in zip(first, second))


def j_ideal(d, k):
    square = power(k, 2)
    return quotient(square, gcd(square, d))


def sixth_decomposition(n):
    ell = tuple(x // 6 for x in n)
    n0 = tuple(x % 6 for x in n)
    return ell, n0


def integer_model_ideals(maximum_exponent):
    return tuple(itertools.product(range(maximum_exponent + 1),
                                   repeat=DIMENSION))


def profile_weight(n):
    # A fixed complex finite profile. No smooth-profile theorem is inferred.
    return ROOTS[(sum(n) + n[0] + 2 * n[2]) % 6]


NU_VALUES = (ROOTS[1], ROOTS[2], ROOTS[5])
ROW_VALUES = (
    (ROOTS[1], ROOTS[2], ROOTS[3]),
    (ROOTS[2], ZERO, ROOTS[1]),
    (ZERO, ROOTS[5], ROOTS[2]),
    (ROOTS[3], ROOTS[1], ZERO),
)
LAM_VALUES = tuple(join_phase_values(NU_VALUES, row) for row in ROW_VALUES)

# Distinct equal-norm prime ideals must not be identified.
p = (1, 0, 0)
q = (0, 1, 0)
r = (0, 0, 1)
check(p != q and norm(p) == norm(q) == 7)
check(not divides(p, q))
check(gcd(p, q) == UNIT)
check(not divides(power(q, 2), power(p, 2)))
check(j_ideal(power(p, 2), q) == power(q, 2))

# Exact sixth-root phases, multiplication, and deletion zeros.
for root in ROOTS:
    check(zpower(root, 6) == ONE)
    check(znorm(root) == 1)
for n in integer_model_ideals(2):
    for m in integer_model_ideals(2):
        for values in LAM_VALUES:
            check(phase(multiply(n, m), values)
                  == zmul(phase(n, values), phase(m, values)))

# Nonsquarefree indicator identity, with nonsquarefree auxiliary k retained.
indicator_cases = integer_model_ideals(8)
for n in indicator_cases:
    auxiliary_sum = sum(mobius(k) for k in square_divisors(n) if k != UNIT)
    check(nonsquarefree(n) == -auxiliary_sum)

# Overlap reduction k^2|dm iff j|m. This includes arbitrary higher powers
# in d,m,k and cases where k is nonsquarefree and hence has zero weight.
overlap_ideals = integer_model_ideals(3)
auxiliary_ideals = integer_model_ideals(2)
for d in overlap_ideals:
    for m in overlap_ideals:
        dm = multiply(d, m)
        for k in auxiliary_ideals:
            j = j_ideal(d, k)
            check(divides(power(k, 2), dm) == divides(j, m))
            check(norm(j) <= norm(k) ** 2)
            if divides(j, m):
                mprime = quotient(m, j)
                check(multiply(d, multiply(j, mprime)) == dm)

# Sixth-power reduction. Only squarefree k contributes to the Mobius sum.
# Check k' squared divides n0 and Nk' >= Nk/Nell with genuine ideal gcds.
sixth_cases = integer_model_ideals(12)
sixth_witnesses = 0
for n in sixth_cases:
    ell, n0 = sixth_decomposition(n)
    check(multiply(power(ell, 6), n0) == n)
    check(all(x < 6 for x in n0))
    for k in square_divisors(n):
        if mobius(k) == 0:
            continue
        kprime = quotient(k, gcd(k, ell))
        check(divides(power(kprime, 2), n0))
        check(gcd(kprime, ell) == UNIT)
        check(norm(kprime) * norm(ell) >= norm(k))
        for threshold in (Fraction(1), Fraction(7), Fraction(49, 2),
                          Fraction(49), Fraction(100)):
            if norm(k) > threshold:
                check(norm(kprime) > threshold / norm(ell))
        sixth_witnesses += 1

Z = 4096
Z2 = Z * Z
PROFILE = tuple(sorted(
    (n for n in integer_model_ideals(8) if Z < norm(n) <= Z2),
    key=lambda n: (norm(n), n)))


@lru_cache(None)
def c_z(d):
    return sum(mobius(a) * mobius(quotient(d, a))
               for a in divisors(d)
               if norm(a) <= Z and norm(quotient(d, a)) <= Z)


CUTOFFS = (Fraction(0), Fraction(1), Fraction(7), Fraction(49),
           Fraction(343), Fraction(Z), Fraction(2 * Z + 1, 2),
           Fraction(Z2))
R_CUTOFFS = (Fraction(1), Fraction(7), Fraction(15, 2),
             Fraction(13), Fraction(49), Fraction(100), Fraction(Z))

# Full truncated inverse, exact projected I, T_nsq=-I_nsq, and k split.
# Work coefficientwise before summing any complex physical profile.
aggregate_tests = 0
for n in PROFILE:
    all_coefficient = -sum(c_z(d) for d in divisors(n))
    check(all_coefficient == mobius(n))
    for cutoff in CUTOFFS:
        dsmall = tuple(d for d in divisors(n) if norm(d) <= cutoff)
        dtail = tuple(d for d in divisors(n) if norm(d) > cutoff)
        i_coefficient = -nonsquarefree(n) * sum(c_z(d) for d in dsmall)
        t_coefficient = -nonsquarefree(n) * sum(c_z(d) for d in dtail)
        check(t_coefficient == -i_coefficient)
        projected = sum(c_z(d) * mobius(k)
                        for d in dsmall
                        for k in square_divisors(n) if k != UNIT)
        check(projected == i_coefficient)
        for radius in R_CUTOFFS:
            low = sum(c_z(d) * mobius(k)
                      for d in dsmall for k in square_divisors(n)
                      if k != UNIT and norm(k) <= radius)
            high = sum(c_z(d) * mobius(k)
                       for d in dsmall for k in square_divisors(n)
                       if k != UNIT and norm(k) > radius)
            check(projected == low + high)
        for values in LAM_VALUES:
            # Expanded j formula for projected I has a PLUS sign.
            weighted_projected = ZERO
            for d in dsmall:
                m = quotient(n, d)
                for k in square_divisors(n):
                    if k == UNIT:
                        continue
                    j = j_ideal(d, k)
                    check(divides(j, m))
                    mprime = quotient(m, j)
                    factor_phase = zmul(phase(d, values),
                                        zmul(phase(j, values),
                                             phase(mprime, values)))
                    check(factor_phase == phase(n, values))
                    weighted_projected = zadd(
                        weighted_projected,
                        zscale(c_z(d) * mobius(k),
                               zmul(factor_phase, profile_weight(n))))
            expected = zscale(i_coefficient,
                              zmul(phase(n, values), profile_weight(n)))
            check(weighted_projected == expected)
            aggregate_tests += 1

# At norm cutoff 7, both distinct norm-seven primes are included.
check(norm(p) <= Fraction(7) and norm(q) <= Fraction(7))
check(not norm(p) <= Fraction(13, 2))
check(not norm(q) <= Fraction(13, 2))
# Strict large-k endpoint: Nk=7 is small at R=7, large at R=13/2.
check(not norm(p) > Fraction(7))
check(norm(p) > Fraction(13, 2))


def w_large(n, radius):
    return -sum(mobius(k) for k in square_divisors(n)
                if k != UNIT and norm(k) > radius)


# Logical sparse support, including after sixth-power removal.
for n in PROFILE:
    ell, n0 = sixth_decomposition(n)
    for radius in R_CUTOFFS:
        weight = w_large(n, radius)
        if weight == 0:
            continue
        witnesses = [k for k in square_divisors(n)
                     if k != UNIT and norm(k) > radius and mobius(k) != 0]
        check(bool(witnesses))
        for k in witnesses:
            kprime = quotient(k, gcd(k, ell))
            check(divides(power(kprime, 2), n0))
            check(norm(kprime) > radius / norm(ell))

# Fixed norm order with stable ideal tie-breaking for adaptive prefixes.
D_COLUMNS = tuple(sorted(
    {d for n in PROFILE for d in divisors(n)},
    key=lambda d: (norm(d), d)))
D_NORMS = [norm(d) for d in D_COLUMNS]
D_INDEX = {d: index for index, d in enumerate(D_COLUMNS)}
PAD = 1
while PAD < len(D_COLUMNS):
    PAD *= 2
LEVELS = PAD.bit_length()


def intervals_at_level(level):
    size = PAD >> level
    return tuple((start, start + size)
                 for start in range(0, PAD, size))


def prefix_intervals(length):
    result = []

    def visit(start, stop, level):
        if start >= length:
            return
        if stop <= length:
            result.append((level, start, stop))
            return
        middle = (start + stop) // 2
        visit(start, middle, level + 1)
        visit(middle, stop, level + 1)

    if length:
        visit(0, PAD, 0)
    return tuple(result)


for length in range(len(D_COLUMNS) + 1):
    intervals = prefix_intervals(length)
    covered = [index for _, start, stop in intervals
               for index in range(start, stop)]
    check(covered == list(range(length)))
    check(len(intervals) <= LEVELS)
    check(len({level for level, _, _ in intervals}) == len(intervals))
    for level, start, stop in intervals:
        check((start, stop) in intervals_at_level(level))

# Build all interval coefficient vectors BEFORE choosing row cutoffs.
# Every vector is on sixth-power-free n0 columns, even though n is arbitrary.
radius = Fraction(13)
ELL_GROUPS = {}
for n in PROFILE:
    ell, n0 = sixth_decomposition(n)
    ELL_GROUPS.setdefault(ell, []).append((n, n0))
fixed_vectors = {}
level_bounds = 0
for ell, pairs in sorted(ELL_GROUPS.items()):
    for level in range(LEVELS):
        intervals = intervals_at_level(level)
        vectors = {}
        for start, stop in intervals:
            vector = {}
            for n, n0 in pairs:
                coefficient = sum(c_z(d) for d in divisors(n)
                                  if start <= D_INDEX[d] < stop)
                base = zscale(w_large(n, radius),
                              zmul(phase(n, NU_VALUES), profile_weight(n)))
                vector[n0] = zscale(coefficient, base)
                check(all(x < 6 for x in n0))
            vectors[(start, stop)] = vector
            fixed_vectors[(ell, level, start, stop)] = vector
        lhs = sum(znorm(value)
                  for vector in vectors.values() for value in vector.values())
        rhs = 0
        for n, n0 in pairs:
            base = zscale(w_large(n, radius),
                          zmul(phase(n, NU_VALUES), profile_weight(n)))
            rhs += znorm(base) * sum(abs(c_z(d)) for d in divisors(n)) ** 2
        check(lhs <= rhs)
        level_bounds += 1

# Test an adaptive cutoff separately for every finite row. No fixed vector
# above depends on those choices. Its interval decomposition is exact, and
# finite Cauchy controls the sum with the actual number of intervals.
adaptive_cutoffs = (Fraction(7), Fraction(49), Fraction(687, 2), Fraction(Z))
adaptive_checks = 0
for row_number, row_values in enumerate(ROW_VALUES):
    cutoff = adaptive_cutoffs[row_number]
    length = bisect.bisect_right(D_NORMS, cutoff)
    intervals = prefix_intervals(length)
    for ell, pairs in sorted(ELL_GROUPS.items()):
        direct = ZERO
        for n, n0 in pairs:
            coefficient = sum(c_z(d) for d in divisors(n)
                              if norm(d) <= cutoff)
            base = zscale(w_large(n, radius),
                          zmul(phase(n, NU_VALUES), profile_weight(n)))
            direct = zadd(direct,
                          zscale(coefficient,
                                 zmul(base, phase(n0, row_values))))
        responses = []
        for level, start, stop in intervals:
            vector = fixed_vectors[(ell, level, start, stop)]
            response = zsum(zmul(value, phase(n0, row_values))
                            for n0, value in vector.items())
            responses.append(response)
        check(zsum(responses) == direct)
        check(znorm(direct)
              <= len(responses) * sum(znorm(x) for x in responses))
        mask = phase(power(ell, 6), row_values)
        check(znorm(mask) <= 1)
        check(znorm(zmul(mask, direct)) <= znorm(direct))
        original = ZERO
        for n, n0 in pairs:
            coefficient = sum(c_z(d) for d in divisors(n)
                              if norm(d) <= cutoff)
            base = zscale(w_large(n, radius),
                          zmul(phase(n, NU_VALUES), profile_weight(n)))
            original = zadd(original,
                            zscale(coefficient,
                                   zmul(base, phase(n, row_values))))
        check(original == zmul(mask, direct))
        adaptive_checks += 1

# Exact rational budgets. Endpoint notation is interpreted by rho<theta/2.
h = a = Fraction(2, 5)
theta1 = Fraction(11, 20)
theta2 = Fraction(13, 20)
target = h + a
generic_powers = (h, 1 + h / 6, 5 * h / 6 + Fraction(1, 3),
                  h / 3 + Fraction(5, 6))
check(generic_powers == (Fraction(2, 5), Fraction(16, 15),
                         Fraction(2, 3), Fraction(29, 30)))
check(max(generic_powers) == Fraction(16, 15))
check(Fraction(16, 15) - theta1 / 2 == Fraction(19, 24))
check(target - Fraction(19, 24) == Fraction(1, 120))
check(h + 1 - theta1 == Fraction(17, 20))
check(h + 1 - theta2 == Fraction(3, 4))
check(Fraction(16, 15) - theta2 / 2 == Fraction(89, 120))
check(Fraction(16, 15) - Fraction(1, 40) / 2 == Fraction(253, 240))
rho_checks = []
for theta in (theta1, theta2):
    rho = theta / 2 - Fraction(1, 1000)
    check(0 < 2 * rho < theta)
    sparse = Fraction(16, 15) - rho
    check(sparse < target)
    rho_checks.append({
        "theta": str(theta), "rho": str(rho),
        "completion_gap": str(theta - 2 * rho),
        "sparse_power_before_epsilon": str(sparse),
        "margin_below_target": str(target - sparse)
    })

# Grouped generic diagnostic on a finite rational x grid.
for x in (Fraction(j, 20) for j in range(1, 21)):
    grouped = (1 + h - x, 1 + h / 6,
               1 + 5 * h / 6 - 2 * x / 3,
               1 + h / 3 - x / 6)
    check(grouped[1] == Fraction(16, 15))

print(json.dumps({
    "status": "passed",
    "assertions": assertions,
    "finite_model": {
        "distinct_prime_symbols": DIMENSION,
        "prime_norms": list(PRIME_NORMS),
        "equal_norm_distinct_primes": True,
        "phase_ring": "Z[omega], omega^2+omega+1=0",
        "nonreal_phases_and_zero_extensions": True,
        "z": Z,
        "profile_products": len(PROFILE),
        "coefficient_columns": len(D_COLUMNS),
        "binary_partition_levels": LEVELS
    },
    "checks": {
        "nonsquarefree_indicator_cases": len(indicator_cases),
        "sixth_power_cases": len(sixth_cases),
        "squarefree_auxiliary_witnesses": sixth_witnesses,
        "weighted_projected_identity_cases": aggregate_tests,
        "binary_level_energy_cases": level_bounds,
        "adaptive_row_prefix_cases": adaptive_checks
    },
    "rational_budgets": {
        "h": str(h), "a": str(a), "target": str(target),
        "generic_powers": [str(x) for x in generic_powers],
        "theta_11_over_20_sparse_endpoint": "19/24",
        "theta_11_over_20_sparse_margin": "1/120",
        "theta_11_over_20_elementary_endpoint": "17/20",
        "theta_13_over_20_elementary_endpoint": "3/4",
        "theta_13_over_20_sparse_endpoint": "89/120",
        "strict_rho_examples": rho_checks
    },
    "covered": [
        "ideal equality and divisibility despite equal norms",
        "arbitrary nonsquarefree total ideals and overlaps",
        "correct projected-I sign",
        "T_nonsquarefree=-I_nonsquarefree on the truncated-inverse profile",
        "j=k^2/gcd(k^2,d) divisibility and complete phases",
        "exact small/large auxiliary-divisor split and endpoints",
        "sixth-power decomposition and improved squarefree-k threshold",
        "fixed binary interval vectors and per-level coefficient energy",
        "row-dependent prefixes chosen after fixed vectors",
        "common sixth-power row mask and positivity",
        "rational analytic budgets with strict completion margins"
    ],
    "not_verified": [
        "physical sextic reciprocity or primitive conductor structure",
        "Poisson completion and radical-weighted row mass",
        "ideal counting or any asymptotic sparse-support bound",
        "the imported sextic large sieve",
        "Schwartz tails on an infinite row family",
        "an unbounded nonsquarefree projection estimate",
        "the remaining squarefree tail moment or any new zero-free region"
    ]
}, indent=2, sort_keys=True))
