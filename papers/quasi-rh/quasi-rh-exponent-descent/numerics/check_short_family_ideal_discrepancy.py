"""Exact algebra checks for the ideal/Hecke signed-discrepancy bridge.

Prepared for Edward Baker, 8 October 2026, with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured effort are not exposed and are not inferred.

This formal ideal monoid uses six distinct good prime-ideal symbols with
norms (7, 7, 13, 13, 25, 31). The lambda tests are arbitrary completely
multiplicative sixth-root phases, including deletion zeros; they are not a
verification of native sextic reciprocity or physical Hecke row labels.
All comparisons use exact integers/Fractions in Q[zeta_6][log rational
primes]. No analytic bound, prime theorem, or asymptotic moment is checked.
Run directly with Python 3; no external dependencies or output files.
"""

from fractions import Fraction as Q
from itertools import product
import json

NORMS = (7, 7, 13, 13, 25, 31)
CAP = 10000
IDEALS = []


def generate(i, n, exponents):
    if i == len(NORMS):
        IDEALS.append((tuple(exponents), n))
        return
    j = 0
    while n <= CAP:
        generate(i + 1, n, exponents + [j])
        n *= NORMS[i]
        j += 1


generate(0, 1, [])
IDEALS.sort(key=lambda item: (item[1], item[0]))


def divisors(e):
    return product(*(range(x + 1) for x in e))


def mu(e):
    return 0 if max(e, default=0) > 1 else (-1) ** sum(e)


def subtract(e, a):
    return tuple(x - y for x, y in zip(e, a))


def norm(e):
    n = 1
    for p, k in zip(NORMS, e):
        n *= p**k
    return n


# Cyclotomic coefficients are pairs a+b*zeta_6, zeta_6^2=zeta_6-1.
ZERO = (Q(0), Q(0))
ONE = (Q(1), Q(0))


def ca(a, b):
    return a[0] + b[0], a[1] + b[1]


def cm(a, b):
    return a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0] + a[1] * b[1]


def cs(a, k):
    return a[0] * k, a[1] * k


def phase(k):
    value = ONE
    for _ in range(k % 6):
        value = cm(value, (Q(0), Q(1)))
    return value


# Polynomials map sorted tuples of rational-prime logarithms to coefficients.
def pa(a, b):
    result = dict(a)
    for k, value in b.items():
        result[k] = ca(result.get(k, ZERO), value)
    return {k: value for k, value in result.items() if value != ZERO}


def ps(a, k):
    return {m: cs(v, k) for m, v in a.items() if cs(v, k) != ZERO}


def pc(a, c):
    return {m: cm(v, c) for m, v in a.items() if cm(v, c) != ZERO}


def pm(a, b):
    result = {}
    for ka, va in a.items():
        for kb, vb in b.items():
            key = tuple(sorted(ka + kb))
            result[key] = ca(result.get(key, ZERO), cm(va, vb))
    return {k: value for k, value in result.items() if value != ZERO}


def factor(n):
    result = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            result[p] = result.get(p, 0) + 1
            n //= p
        p += 1
    if n > 1:
        result[n] = result.get(n, 0) + 1
    return result


def lograt(value):
    value = Q(value)
    result = {}
    for p, j in factor(value.numerator).items():
        result[(p,)] = (Q(j), Q(0))
    for p, j in factor(value.denominator).items():
        key = (p,)
        result[key] = ca(result.get(key, ZERO), (-Q(j), Q(0)))
    return {k: value for k, value in result.items() if value != ZERO}


def constant(value):
    return {} if value == 0 else {(): (Q(value), Q(0))}


def check_convolution_and_truncation():
    convolution_checks = truncated_checks = 0
    for e, _ in IDEALS:
        # First keep a distinct formal logarithm for each prime ideal.
        convolution = [0] * len(NORMS)
        for a in divisors(e):
            b = subtract(e, a)
            support = [i for i, x in enumerate(b) if x]
            if len(support) == 1:
                convolution[support[0]] += mu(a)
        assert convolution == [-mu(e) * x for x in e]
        convolution_checks += 1
        for z in (7, 13, 31, 100):
            coefficient = 0
            prime_convolution = [0] * len(NORMS)
            for a in divisors(e):
                b = subtract(e, a)
                if norm(a) <= z and norm(b) <= z:
                    coefficient += mu(a) * mu(b)
                if norm(a) <= z and norm(b) <= z:
                    for aa in divisors(a):
                        bb = subtract(a, aa)
                        support = [i for i, x in enumerate(bb) if x]
                        if len(support) == 1:
                            prime_convolution[support[0]] += mu(aa) * mu(b)
            assert [coefficient * x for x in e] == [-2 * x for x in prime_convolution]
            truncated_checks += 1
    return convolution_checks, truncated_checks


def check_discrepancy(phase_vector, deleted, delta, r, u, v):
    def lam(e):
        if any(e[i] for i in deleted):
            return ZERO
        return phase(sum(x * y for x, y in zip(e, phase_vector)))

    fs, gs = [], []
    for e, n in IDEALS:
        if n > r:
            continue
        f = cs(lam(e), mu(e))
        if f != ZERO:
            fs.append((n, f))
        support = [i for i, x in enumerate(e) if x]
        if len(support) == 1 and lam(e) != ZERO:
            gs.append((n, pc(lograt(NORMS[support[0]]), lam(e))))

    high_high, density = {}, {}
    for a, fa in fs:
        if a <= u:
            continue
        for b, gb in gs:
            if b > v and a * b <= r:
                high_high = pa(high_high, pc(pm(gb, lograt(Q(r, a * b))), fa))
        if a * v <= r:
            bracket = pa(constant(Q(r, a) - v), ps(lograt(Q(r, a * v)), -v))
            density = pa(density, pc(ps(bracket, delta), fa))
    right = pa(high_high, ps(density, -1))

    # Both low/full edges minus their low/low overlap, versus mu*Lambda.
    closure = dict(high_high)
    for a, fa in fs:
        for b, gb in gs:
            if a * b > r:
                continue
            term = pc(pm(gb, lograt(Q(r, a * b))), fa)
            if a <= u:
                closure = pa(closure, term)
            if b <= v:
                closure = pa(closure, term)
            if a <= u and b <= v:
                closure = pa(closure, ps(term, -1))
    full = {}
    for n, fn in fs:
        full = pa(full, pc(pm(lograt(n), lograt(Q(r, n))), cs(fn, -1)))
    assert closure == full

    lower, upper = Q(u), Q(r, v)
    cuts = {lower, upper}
    cuts.update(Q(a) for a, _ in fs if lower < Q(a) < upper)
    cuts.update(Q(r, b) for b, _ in gs if lower < Q(r, b) < upper)
    cuts = sorted(cuts)
    left = {}
    for x, y in zip(cuts, cuts[1:]):
        midpoint = (x + y) / 2
        mf = ZERO
        for a, fa in fs:
            if u < a <= midpoint:
                mf = ca(mf, fa)
        eg = {}
        for b, gb in gs:
            if v < b <= Q(r) / midpoint:
                eg = pa(eg, gb)
        # Integral of [Psi(r/s)-Psi(v)-delta*(r/s-v)] ds/s.
        piece = pm(pa(eg, constant(delta * v)), lograt(y / x))
        piece = pa(piece, constant(delta * r * (1 / y - 1 / x)))
        left = pa(left, pc(piece, mf))
    assert left == right

    # Raw centered Stieltjes bridge with polynomial smooth weights.
    # Some cuts are precisely prime-power atoms; endpoints are right-continuous.
    raw_cases = [(Q(3, 2), 7, 1), (7, 13, 2), (13, 31, 3),
                 (25, 100, 1), (7, 7, 2), (31, 137, 2)]
    for lower, upper, power in raw_cases:
        lower, upper = Q(lower), Q(upper)
        direct, increment = {}, {}
        for b, gb in gs:
            if lower < b <= upper:
                direct = pa(direct, ps(gb, Q(b)**power))
                increment = pa(increment, gb)
        increment = pa(increment, constant(-delta * (upper - lower)))
        bridge = pa(constant(delta * (upper**(power + 1) - lower**(power + 1))
                             / (power + 1)), ps(increment, upper**power))
        subcuts = sorted({lower, upper} |
                         {Q(b) for b, _ in gs if lower < b < upper})
        for x, y in zip(subcuts, subcuts[1:]):
            midpoint = (x + y) / 2
            step = constant(delta * lower)
            for b, gb in gs:
                if lower < b <= midpoint:
                    step = pa(step, gb)
            integral = pa(ps(step, y**power - x**power),
                          constant(-delta * Q(power, power + 1)
                                   * (y**(power + 1) - x**(power + 1))))
            bridge = pa(bridge, ps(integral, -1))
        assert direct == bridge
    return len(cuts) - 1, len(raw_cases)


def main():
    convolution_checks, truncated_checks = check_convolution_and_truncation()
    interval_count = test_count = raw_count = 0
    cases = [
        ((0, 0, 0, 0, 0, 0), (), 1),
        ((0, 0, 0, 0, 0, 0), (0, 4), 1),
        ((1, 2, 3, 4, 5, 1), (), 0),
        ((1, 2, 3, 4, 5, 1), (1, 3), 0),
    ]
    for phases, deleted, delta in cases:
        for r, u, v in [(1400, 13, 7), (1500, 7, 13), (3000, 25, 7), (4096, 13, 25)]:
            intervals, raw = check_discrepancy(phases, deleted, delta, r, u, v)
            interval_count += intervals
            raw_count += raw
            test_count += 1
    print(json.dumps({
        "date": "2026-10-08",
        "author": "Prepared for Edward Baker with substantial LLM assistance",
        "model": "GPT-6 (Codex), inherited configuration; exact variant/effort not exposed",
        "named_equality_checks": convolution_checks + truncated_checks + 2 * test_count + raw_count,
        "ideal_count": len(IDEALS),
        "mu_lambda_convolution_checks": convolution_checks,
        "truncated_derivation_checks": truncated_checks,
        "exact_complex_discrepancy_integrals": test_count,
        "staircase_intervals_checked": interval_count,
        "complete_riesz_edge_closures": test_count,
        "raw_centered_stieltjes_checks": raw_count,
        "ring": "Q[zeta_6][log rational primes]; all comparisons exact",
        "scope": "formal ideal monoid; no analytic or reciprocity estimate",
    }, indent=2))


if __name__ == "__main__":
    main()
