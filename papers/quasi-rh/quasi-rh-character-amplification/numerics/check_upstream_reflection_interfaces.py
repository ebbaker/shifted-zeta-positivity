#!/usr/bin/env python3
"""Exact finite audit of source Proposition 5.1 and primitive Poisson interfaces.

Prepared for Edward Baker with substantial LLM assistance, 2026-10-09.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.
Same-model internal checks, not independent specialist or formal validation.

No numerical complex arithmetic is used. Local additive and multiplicative
roots are represented in Q(zeta_6,zeta_p). Cusp congruences are checked in the
actual Eisenstein integer ring. Finite cases do not prove unbounded analytic
estimates, automorphy, reciprocity, a large sieve, or the family baseline.
"""

import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path

COUNTS = {}


def check(condition, label):
    assert condition, label
    COUNTS[label.split(':')[0]] = COUNTS.get(label.split(':')[0], 0) + 1


# O = Z[omega], omega^2 + omega + 1 = 0. Rational pairs are also allowed.
ONE, ZERO, LAM = (1, 0), (0, 0), (1, 2)
UNITS = [(1, 0), (0, 1), (-1, -1), (-1, 0), (0, -1), (1, 1)]


def add(a, b):
    return a[0] + b[0], a[1] + b[1]


def neg(a):
    return -a[0], -a[1]


def sub(a, b):
    return add(a, neg(b))


def mul(a, b):
    return a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0] - a[1] * b[1]


def norm(a):
    return a[0] ** 2 - a[0] * a[1] + a[1] ** 2


def powe(a, k):
    r = ONE
    while k:
        if k & 1:
            r = mul(r, a)
        a = mul(a, a)
        k //= 2
    return r


def quot(a, b):
    n = norm(b)
    t = mul(a, (b[0] - b[1], -b[1]))
    return Fraction(t[0], n), Fraction(t[1], n)


def exactdiv(a, b):
    q = quot(a, b)
    assert all(x.denominator == 1 for x in q), (a, b, q)
    return tuple(int(x) for x in q)


def divrem(a, b):
    q = quot(a, b)
    # The nearest of this finite lattice neighborhood is a Euclidean quotient.
    aa, bb = q[0].numerator // q[0].denominator, q[1].numerator // q[1].denominator
    choices = [(aa + i, bb + j) for i in (-1, 0, 1, 2) for j in (-1, 0, 1, 2)]
    q0 = min(choices, key=lambda t: norm(sub(a, mul(t, b))))
    r = sub(a, mul(q0, b))
    assert norm(r) < norm(b)
    return q0, r


def egcd(a, b):
    x0, x1, y0, y1 = ONE, ZERO, ZERO, ONE
    while b != ZERO:
        q, r = divrem(a, b)
        a, b = b, r
        x0, x1 = x1, sub(x0, mul(q, x1))
        y0, y1 = y1, sub(y0, mul(q, y1))
    return a, x0, y0


def mod(a, m):
    return divrem(a, m)[1]


def inv(a, m):
    if norm(m) == 1:
        return ZERO
    g, x, _ = egcd(a, m)
    assert norm(g) == 1, (a, m, g)
    return mod(mul(x, exactdiv(ONE, g)), m)


def crt(a, m, b, n):
    return mod(add(a, mul(m, mod(mul(sub(b, a), inv(m, n)), n))), mul(m, n))


def divides(a, b):
    return all(x.denominator == 1 for x in quot(b, a))


def val(a, p):
    k = 0
    while divides(p, a):
        a = exactdiv(a, p)
        k += 1
    return k


def primary(a):
    return a[0] % 3 == 1 and a[1] % 3 == 0


class ResidueField:
    """Actual split O/(a+b omega), or inert O/(-p), with sextic embedding."""

    def __init__(self, element, p, inert=False):
        self.element, self.p, self.inert = element, p, inert
        self.q = p * p if inert else p
        self.values = [(a, b) for a in range(p) for b in range(p)] if inert else list(range(p))
        self.zero, self.one = ((0, 0), (1, 0)) if inert else (0, 1)
        self.root6 = (1, 1) if inert else (1 - element[0] * pow(element[1], -1, p)) % p
        root_values = [self.power(self.root6, j) for j in range(6)]
        assert len(set(root_values)) == 6
        self.chars = {x: None if x == self.zero else root_values.index(self.power(x, (self.q - 1) // 6)) for x in self.values}
        self.inverses = {x: self.power(x, self.q - 2) for x in self.values if x != self.zero}

    def product(self, a, b):
        if self.inert:
            t = mul(a, b)
            return t[0] % self.p, t[1] % self.p
        return a * b % self.p

    def power(self, a, k):
        r = self.one
        while k:
            if k & 1:
                r = self.product(r, a)
            a = self.product(a, a)
            k //= 2
        return r

    def additive(self, x):
        # e(a+b omega)=exp(2 pi i b). Inert denominator is the primary -p.
        return (-x[1] if self.inert else -self.element[1] * x) % self.p


class Cyclotomic:
    """Q(zeta_6,zeta_p), basis 1,zeta_6 and 1,...,zeta_p^(p-2)."""

    ROOTS = [(1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1)]

    def __init__(self, p):
        self.p = p
        self.zero = (0,) * (2 * p)
        self.one = self.term(0, 0)

    def canon(self, a):
        a = list(a)
        for r in (0, 1):
            s = a[r * self.p + self.p - 1]
            for k in range(self.p):
                a[r * self.p + k] -= s
        return tuple(a)

    def term(self, j, k, coefficient=1):
        a = [0] * (2 * self.p)
        r = self.ROOTS[j % 6]
        a[k % self.p], a[self.p + k % self.p] = coefficient * r[0], coefficient * r[1]
        return self.canon(a)

    def plus(self, a, b):
        return tuple(x + y for x, y in zip(a, b))

    def times_integer(self, a, k):
        return tuple(x * k for x in a)

    def shift(self, a, j=0, k=0):
        r0, r1 = self.ROOTS[j % 6]
        out = [0] * (2 * self.p)
        for e in range(self.p):
            u, v = a[e], a[self.p + e]
            d = (e + k) % self.p
            out[d] += u * r0 - v * r1
            out[self.p + d] += u * r1 + v * r0 + v * r1
        return self.canon(out)

    def product(self, a, b):
        out = self.zero
        for r in (0, 1):
            for k in range(self.p - 1):
                v = b[r * self.p + k]
                if v:
                    out = self.plus(out, self.times_integer(self.shift(a, r, k), v))
        return out

    def conjugate(self, a):
        out = self.zero
        for r in (0, 1):
            for k in range(self.p - 1):
                v = a[r * self.p + k]
                if v:
                    out = self.plus(out, self.term(-r, -k, v))
        return out


def check_local_fourier():
    descriptions = [((-2, -3), 7, False), ((1, -3), 13, False), ((-2, 3), 19, False),
                    ((1, 6), 31, False), ((7, 3), 37, False), ((7, 6), 43, False),
                    ((-5, 0), 5, True), ((-11, 0), 11, True)]
    reports = []
    for element, p, inert in descriptions:
        f, c = ResidueField(element, p, inert), Cyclotomic(p)
        G = {}
        for j in range(6):
            for sign in (-1, 1):
                total = c.zero
                for x in f.values:
                    if x != f.zero:
                        total = c.plus(total, c.term(j * f.chars[x], sign * f.additive(x)))
                G[j, sign] = total
            if j:
                check(c.product(G[j, 1], c.conjugate(G[j, 1])) == c.times_integer(c.one, f.q), 'gauss_norm: q')
            else:
                check(G[j, 1] == c.times_integer(c.one, -1), 'gauss_norm: principal_unit_mask')
        F = {}
        for j in range(6):
            for h in f.values:
                total = c.zero
                for x in f.values:
                    if x != f.zero:
                        total = c.plus(total, c.term(j * f.chars[x], -f.additive(f.product(h, x))))
                F[j, h] = total
                if j == 0:
                    expected = c.times_integer(c.one, f.q - 1 if h == f.zero else -1)
                elif h == f.zero:
                    expected = c.zero
                else:
                    expected = c.shift(G[j, -1], -j * f.chars[h])
                check(total == expected, 'finite_fourier: (5.11)')
        for j in range(1, 6):
            for h in f.values:
                # Positive finite transform in (17.8) must use conjugate psi(h).
                positive = c.conjugate(F[-j % 6, h])
                expected_positive = c.zero if h == f.zero else c.shift(G[j, 1], -j * f.chars[h])
                check(positive == expected_positive, 'primitive_orientation: (17.8)')
        epsilons = list(dict.fromkeys([f.one, f.root6, f.power(f.root6, 3)]))
        for epsilon in epsilons:
            for x in f.values:
                for j in range(6):
                    total = c.zero
                    for h in f.values:
                        if h != f.zero:
                            phase = f.additive(f.product(f.product(epsilon, f.inverses[h]), x))
                            total = c.plus(total, c.shift(F[j, h], -2 * f.chars[h], phase))
                    if j == 4:
                        expected = c.times_integer(G[4, -1], f.q - 1 if x == f.zero else -1)
                    elif x == f.zero:
                        expected = c.zero
                    else:
                        exponent = -(j + 2) * f.chars[f.product(epsilon, x)]
                        if j == 0:
                            expected = c.times_integer(c.shift(G[2, 1], exponent), -1)
                        else:
                            expected = c.shift(c.product(G[j, -1], G[(j + 2) % 6, 1]), exponent)
                    check(total == expected, 'local_reflection: B_j including collisions')
        # The principal unit mask is not a primitive character mod p.
        check(F[0, f.zero] != c.zero, 'countercheck: masked_principal_not_primitive')
        reports.append({'primary_prime': list(element), 'residue_order': f.q,
                        'additive_order': p, 'type': 'inert' if inert else 'split',
                        'all_exponents': list(range(6)), 'all_frequencies_and_columns': True,
                        'epsilon_count': len(epsilons)})
    return reports


def check_cubic_prime_two():
    # The theta coefficients may contain the primary prime -2 of norm four.
    # It has a cubic character, but there is no nontrivial sextic character
    # of order six on F_4^*. This suite deliberately uses cubic exponents.
    c = Cyclotomic(2)
    values = [(a, b) for a in range(2) for b in range(2)]
    roots = [ONE, (0, 1), (1, 1)]
    def fieldmul(a, b):
        t = mul(a, b)
        return t[0] % 2, t[1] % 2
    def gauss(t):
        total = c.zero
        for x in values:
            if x != ZERO:
                total = c.plus(total, c.term(2 * roots.index(x), fieldmul(t, x)[1]))
        return total
    G = gauss(ONE)
    check(c.product(G, c.conjugate(G)) == c.times_integer(c.one, 4), 'cubic_prime_two: gauss_norm')
    for t in values:
        expected = c.zero if t == ZERO else c.shift(G, -2 * roots.index(t))
        check(gauss(t) == expected, 'cubic_prime_two: supplementary_twists')
    return {'primary_prime': [-2, 0], 'residue_order': 4,
            'character_order': 3, 'sextic_character_used': False,
            'all_four_additive_twists': True}


def check_cusps():
    # L=18 has the required prime support {2,lambda}; every h0 mod L is read,
    # including nonunits and zero. This is one fixed arithmetic presentation.
    L = (18, 0)
    M = mul(powe(LAM, 12), powe(L, 4))
    M2 = mul(M, M)
    primes = [(-2, -3), (1, -3), (-5, 0)]
    sets = [[], [primes[0]], primes[:2], [primes[0], primes[2]], primes]
    cases, classes = 0, set()
    h0_nonunit = 0
    for hh in [(a, b) for a in range(18) for b in range(18)]:
        if norm(egcd(hh, L)[0]) > 1:
            h0_nonunit += 1
        g = egcd(mul(powe(LAM, 2), hh), L)[0]
        aF, cF = exactdiv(mul(powe(LAM, 2), hh), g), exactdiv(L, g)
        target = aF if divides(LAM, cF) else cF
        unit = next(u for u in UNITS if primary(mul(u, target)))
        aF, cF = mul(unit, aF), mul(unit, cF)
        check(norm(egcd(aF, cF)[0]) == 1, 'cusp_reduced: fixed_denominator')
        for active in sets:
            r = ONE
            for p in active:
                r = mul(r, p)
            cden = mul(cF, r)
            residues = []
            for seed in (1, 2, 3):
                h = {p: mul(M2, mod(mul((seed, 0), inv(M2, p)), p)) for p in active}
                a = mul(aF, r)
                for p in active:
                    a = add(a, mul(mul(powe(LAM, 2), cF), mul(exactdiv(r, p), h[p])))
                check(norm(egcd(a, cden)[0]) == 1, 'cusp_reduced: all_active_frequencies')
                check(divides(mul(M, cF), sub(a, mul(aF, r))), 'fixed_sector: a_mod_M_cF')
                mod_cf, mod_other = ONE, ONE
                for p in ((2, 0), LAM):
                    if divides(p, cF):
                        mod_cf = mul(mod_cf, powe(p, val(M, p) + val(cF, p)))
                    else:
                        mod_other = mul(mod_other, powe(p, val(M, p)))
                delta0 = crt(inv(a, mod_cf), mod_cf, ZERO, mod_other)
                fixed_modulus = mul(mod_cf, mod_other)
                delta = crt(delta0, fixed_modulus, inv(a, r), r)
                b = exactdiv(sub(mul(a, delta), ONE), cden)
                check(sub(mul(a, delta), mul(b, cden)) == ONE, 'cusp_matrix: determinant_one')
                vlam = val(cden, LAM)
                if vlam >= 2:
                    Gmatrix = [a, b, cden, delta]
                    branch = '3_divides_c'
                elif vlam == 1:
                    u0 = next(u for u in (LAM, neg(LAM)) if divides((3, 0), sub(cden, u)))
                    Gmatrix = [sub(a, mul(u0, b)), b, sub(cden, mul(u0, delta)), delta]
                    branch = 'lambda_exactly_once'
                else:
                    u0 = (a[0] % 3, a[1] % 3)
                    Gmatrix = [neg(b), add(a, mul(b, u0)), neg(delta), add(cden, mul(delta, u0))]
                    branch = 'lambda_unit'
                check(all(divides((3, 0), sub(t, z)) for t, z in zip(Gmatrix, [ONE, ZERO, ZERO, ONE])), 'cusp_matrix: Gamma_1_3')
                classes.add(branch)
                DF = mul(powe(LAM, 3), cF)
                deltaF = mod(delta, DF)
                theta_numerator = neg(mul(deltaF, inv(r, DF)))
                eps = {}
                for p in active:
                    sigma = mul(powe(LAM, 2), exactdiv(cden, p))
                    eps[p] = neg(inv(mul(mul(powe(LAM, 3), exactdiv(cden, p)), sigma), p))
                    check(divides(p, sub(a, mul(sigma, h[p]))), 'local_orientation: a_sigma_h')
                    check(divides(p, sub(delta, inv(mul(sigma, h[p]), p))), 'local_orientation: delta_inverse')
                for x in [(1, 0), (0, 1), (1, 1), (-2, 3), (7, -4)]:
                    left = quot(neg(mul(delta, x)), mul(DF, r))[1]
                    right = quot(mul(theta_numerator, x), DF)[1]
                    for p in active:
                        right += quot(mul(mul(eps[p], inv(h[p], p)), x), p)[1]
                    check((left - right).denominator == 1, 'additive_crt: (5.16) signs_lambda_powers')
                residues.append([mod(a, mul(M, cF)), mod(b, M), mod(cden, M), mod(delta, DF)])
                cases += 1
            check(all(t == residues[0] for t in residues), 'fixed_sector: cusp_data_independent_of_h')
    return {'fixed_L': list(L), 'fixed_frequency_count': 324,
            'nonunit_fixed_frequencies': h0_nonunit, 'active_prime_sets': [[list(p) for p in s] for s in sets],
            'frequency_choices_per_set': 3, 'cusp_cases': cases, 'all_three_cusp_branches': sorted(classes),
            'column_tests_per_cusp': 5}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path(__file__).with_name('upstream_reflection_interfaces_record_20261009.json'))
    args = parser.parse_args()
    local, prime_two, cusps = check_local_fourier(), check_cubic_prime_two(), check_cusps()
    record = {'date': '2026-10-09', 'prepared_for': 'Edward Baker',
              'model': 'GPT-6 (Codex), inherited configuration',
              'serving_variant_and_reasoning_effort': 'not exposed; not inferred',
              'llm_use': 'Substantial LLM assistance; same-model internal validation only.',
              'source_pdf_sha256': '8fe93046f8cf5ef1ba5969c89addc02d76311adc4ee907509ff9cd96f7ec99e7',
              'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'arithmetic': 'Exact integer and rational arithmetic; Q(zeta_6,zeta_p) quotient basis; actual Z[omega] cusp congruences.',
              'checks': dict(sorted(COUNTS.items())), 'assertions': sum(COUNTS.values()),
              'local_fields': local, 'cubic_prime_two': prime_two, 'cusps': cusps, 'passed': True,
              'scope_limits': ['Finite split/inert residue fields and one fixed L=18 cusp presentation.',
                               'No proof of theta automorphy, global reciprocity, cusp coefficient theorem, sieve inequality, or family baseline.',
                               'No validation of all primitive prime-power characters or every arithmetic presentation.',
                               'No numerical approximation, asymptotic estimate, or new zero-free theorem.']}
    args.output.write_text(json.dumps(record, indent=2, sort_keys=True) + '\n')
    print(json.dumps({'passed': True, 'assertions': record['assertions'], 'checks': record['checks'], 'record': str(args.output)}))


if __name__ == '__main__':
    main()
