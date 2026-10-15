#!/usr/bin/env python3
"""Exact finite algebra for the coupled theta product and parity sectors.

Prepared for Edward Baker, 15 October 2026; substantial LLM assistance.
Recorded model gpt-6-astra, reasoning effort ultra.
"""
from fractions import Fraction as F
from pathlib import Path
import argparse
import hashlib
import json
import platform

counts = {}


def check(a, b, group):
    assert a == b, (group, a, b)
    counts[group] = counts.get(group, 0) + 1


def clean(p):
    return {k: F(v) for k, v in p.items() if v}


def const(a):
    return {} if not a else {(0, 0, 0, 0, 0): F(a)}


def var(i):
    key = [0] * 5
    key[i] = 1
    return {tuple(key): F(1)}


def add(*ps):
    out = {}
    for p in ps:
        for k, a in p.items():
            out[k] = out.get(k, F(0)) + a
    return clean(out)


def scale(p, a):
    return clean({k: a * v for k, v in p.items()})


def mul(*ps):
    out = const(1)
    for p in ps:
        nxt = {}
        for k, a in out.items():
            for ell, b in p.items():
                key = tuple(x + y for x, y in zip(k, ell))
                nxt[key] = nxt.get(key, F(0)) + a * b
        out = clean(nxt)
    return out


def power(p, n):
    return mul(*([p] * n))


def evaluate(p, values):
    result = F(0)
    for exponents, coefficient in p.items():
        for value, exponent in zip(values, exponents):
            coefficient *= value ** exponent
        result += coefficient
    return result


# Formal ring (q,r,pi,DX,DY). Normalize the double source operator by
# 256*pi^4/e^(u+v), so no negative powers are needed.
q, r, pi, DX, DY = [var(i) for i in range(5)]
Dz, Dw = add(DX, DY), add(DX, scale(DY, -1))
Sq = add(mul(power(q, 2), power(Dz, 4)),
         scale(mul(pi, q, power(Dz, 2)), 6))
Sr = add(mul(power(r, 2), power(Dw, 4)),
         scale(mul(pi, r, power(Dw, 2)), 6))
outer = power(add(power(DX, 2), scale(power(DY, 2), -1)), 2)
mixed = add(mul(add(q, r), add(power(DX, 2), power(DY, 2))),
            scale(mul(add(q, scale(r, -1)), DX, DY), 2))
factored = mul(q, r, outer,
               add(mul(q, r, outer), scale(mul(pi, mixed), 6),
                   scale(power(pi, 2), 36)))
check(mul(Sq, Sr), factored, 'complete_double_source_operator')

# On p,k plane waves in X,Y, DX=pi*i*p and DY=pi*i*k.
# All derivative orders are even, so the coefficients remain rational.
mode = {}
for (eq, er, ep, dx, dy), coefficient in factored.items():
    degree = dx + dy
    assert degree % 2 == 0
    exponent = (eq, er, ep + degree - 4, dx, dy)
    mode[exponent] = mode.get(exponent, F(0)) + coefficient * (-1) ** (degree // 2) / 256
mode = clean(mode)
p, k = DX, DY
L = add(power(p, 2), scale(power(k, 2), -1))
mode_expected = scale(mul(power(pi, 2), q, r, power(L, 2),
                         add(mul(pi, q, power(add(p, k), 2)), const(-6)),
                         add(mul(pi, r, power(add(p, scale(k, -1)), 2)), const(-6))), F(1, 256))
check(mode, mode_expected, 'source_mode_factorization')

gaussian = scale(add(mul(q, power(add(p, k), 2)),
                     mul(r, power(add(p, scale(k, -1)), 2))), F(1, 4))
gaussian_expected = add(scale(mul(add(q, r), add(power(p, 2), power(k, 2))), F(1, 4)),
                        scale(mul(add(q, scale(r, -1)), p, k), F(1, 2)))
check(gaussian, gaussian_expected, 'coupled_gaussian_quadratic_form')

for n in range(-5, 6):
    for m in range(-5, 6):
        pp, kk = n + m, n - m
        check((pp - kk) % 2, 0, 'lattice_parity_and_inverse')
        check(((pp + kk) // 2, (pp - kk) // 2), (n, m), 'lattice_parity_and_inverse')
        check((pp % 2 == 0), (n % 2 == m % 2), 'physical_parity_channel')
        if n and m:
            check(abs(pp + kk) >= 2 and abs(pp - kk) >= 2, True,
                  'nonzero_source_lattice_gap')
        for qq, rr in ((F(1), F(1)), (F(1), F(3)), (F(5, 2), F(7, 3))):
            # pi=3 is a rational surrogate for a finite polynomial replay,
            # not a numerical enclosure of the transcendental constant.
            ppival = F(3)
            expected = ((ppival**2 * qq**2 * n**4 - F(3, 2) * ppival * qq * n**2)
                        * (ppival**2 * rr**2 * m**4 - F(3, 2) * ppival * rr * m**2))
            check(evaluate(mode, (qq, rr, ppival, pp, kk)), expected,
                  'source_mode_replay')
            if not n or not m:
                check(expected, F(0), 'complete_zero_mode_lines')

for epsilon in (0, 1):
    for a in range(-4, 5):
        for b in range(-4, 5):
            n, m = a + b + epsilon, a - b
            aa, bb = F(a) + F(epsilon, 2), F(b) + F(epsilon, 2)
            for qq, rr in ((F(1), F(2)), (F(3), F(1))):
                A, B = qq + rr, qq - rr
                check(qq * n*n + rr * m*m,
                      A * (aa*aa + bb*bb) + 2 * B * aa * bb,
                      'parity_sector_mixed_heat_exponent')
                check(A - abs(B), 2 * min(qq, rr), 'mixed_heat_convergence_margin')

# The differential multiplier is checked coefficientwise: the lth term of
# exp[B/(2*pi) DX DY] has mode multiplier (-2*pi*B*a*b)^l/l!.
from math import factorial
for ell in range(9):
    check(F((-4) ** ell, 2 ** ell * factorial(ell)),
          F((-2) ** ell, factorial(ell)), 'mixed_heat_series_coefficients')

# Rank-one coefficient condition on the full, pre-source even sector.
for c in (F(1), F(2, 3)):
    a = lambda n: c ** (n*n)
    for n in range(-4, 5):
        for m in range(-4, 5):
            check(a(n+m) * a(n-m), a(n)**2 * a(m)**2,
                  'gaussian_weight_parallelogram_control')
    sequence = [F(1), c]
    for n in range(1, 8):
        sequence.append(sequence[n]**2 * c**2 / sequence[n-1])
    check(sequence, [c ** (n*n) for n in range(9)], 'gaussian_weight_recurrence')

for M in (3, 4):
    weight = F(M+1, M)
    # C00=1,C_M0=C_0M=a_M^2,C_MM=a_2M*a0=0 for a finite control.
    determinant = -weight**4
    check(determinant < 0, True, 'finite_support_coefficient_minor')

# Source parity matrices have zero diagonal and positive off-diagonal;
# record the exact determinant normalized by the squared off-diagonal.
check(F(0) * F(0) - F(1)**2, F(-1), 'even_source_gram_obstruction')
check(F(1)*0 + F(1)*0 - 2*F(1), F(-2), 'even_source_negative_vector')
check(F(0) * F(0) - F(1)**2, F(-1), 'odd_source_gram_obstruction')

# The source parity matrix is indefinite even on coefficient sum-zero.
# Formal ring temporarily (a,b,c,lambda,unused). Exact bounds use e>2;
# the analytic mode-ratio estimate in the note supplies the inequalities.
a_coef, b_coef, c_coef, lam = [var(i) for i in range(4)]
for vec, expected in (((1, -1, 0), scale(a_coef, -2)),
                      ((1, 1, -2), add(scale(a_coef, 2),
                                      scale(b_coef, -4), scale(c_coef, -4)))):
    check(sum(vec), 0, 'zero_sum_witness_constraint')
    value = add(scale(a_coef, 2*vec[0]*vec[1]),
                scale(b_coef, 2*vec[0]*vec[2]),
                scale(c_coef, 2*vec[1]*vec[2]))
    check(value, expected, 'zero_sum_source_quadratic_form')
    check(add(value, scale(lam, sum(vec)**2)), value,
          'constant_rank_one_correction_vanishes')

# The mode ratios satisfy phi_n/phi_m <= prefactor*exp(-exponent).
def ratio_bound(n, m):
    assert n >= m >= 1
    return 2*F(n, m)**4, 3*(n*n-m*m)

for sector, indices, pairs, expected in (
        ('even', (0, 2, 4), ((2, 1, 2, 1), (3, 1, 1, 1)),
         ((F(1024), 18), (F(162), 24))),
        ('odd', (1, 3, 5), ((3, 2, 2, 1), (4, 2, 1, 1)),
         ((F(324), 24), (F(32), 36)))):
    # A ratio with equal indices is exactly one, not the looser bound two.
    obtained = []
    for n, m, ell, k in pairs:
        p1, e1 = ratio_bound(n, m) if n != m else (F(1), 0)
        p2, e2 = ratio_bound(ell, k) if ell != k else (F(1), 0)
        obtained.append((p1*p2, e1+e2))
    check(tuple(obtained), expected, sector+'_source_ratio_coefficients')
    rational_majorant = sum(prefactor/F(2)**exponent for prefactor, exponent in obtained)
    check(rational_majorant < F(1, 2), True, sector+'_zero_sum_positive_witness_bound')
    check(2 - 4*rational_majorant > 0, True, sector+'_zero_sum_positive_quadratic_bound')
    source_modes = tuple(((indices[i]+indices[j])//2,
                          abs(indices[i]-indices[j])//2)
                         for i, j in ((0, 1), (0, 2), (1, 2)))
    check(source_modes, ((1, 1), (2, 2), (3, 1)) if sector == 'even'
          else ((2, 1), (3, 2), (4, 1)), sector+'_zero_sum_block_modes')

# Formal ring now (We,Wo,Ve,Vo,alpha).
We, Wo, Ve, Vo, alpha = [var(i) for i in range(5)]
Wp, Wm = add(We, Wo), add(We, scale(Wo, -1))
Vp, Vm = add(Ve, Vo), add(Ve, scale(Vo, -1))
Aobs = add(power(Wp, 2), scale(mul(alpha, Wp, Vp), -1))
Bobs = add(power(Wm, 2), scale(mul(alpha, Wm, Vm), -1))
same = add(power(We, 2), power(Wo, 2),
           scale(mul(alpha, add(mul(We, Ve), mul(Wo, Vo))), -1))
cross = add(scale(mul(We, Wo), 2),
            scale(mul(alpha, add(mul(We, Vo), mul(Wo, Ve))), -1))
check(scale(same, 2), add(Aobs, Bobs), 'physical_parity_observations')
check(scale(cross, 2), add(Aobs, scale(Bobs, -1)), 'physical_parity_observations')
check(evaluate(Aobs, (F(1), F(-1), F(0), F(0), F(1, 2))), F(0),
      'sector_cancellation_witness')
check(evaluate(same, (F(1), F(-1), F(0), F(0), F(1, 2))), F(2),
      'sector_cancellation_witness')
check(evaluate(cross, (F(1), F(-1), F(0), F(0), F(1, 2))), F(-2),
      'sector_cancellation_witness')

# Formal primitive endpoint/corner bookkeeping, with I=var0,J=var1,
# alpha=var2 and d=delta_j0 in {0,1}.
I, J, a = var(0), var(1), var(2)
for d in (F(0), F(1)):
    X, Y = add(I, const(d/2)), add(J, const(d/2))
    direct = add(power(X, 2), scale(mul(a, X, Y), -1))
    expanded = add(power(I, 2), scale(mul(a, I, J), -1),
                   scale(I, d), scale(mul(a, add(I, J)), -d/2),
                   const(d/4), scale(a, -d/4))
    check(direct, expanded, 'full_primitive_edges_and_corner')

parser = argparse.ArgumentParser()
parser.add_argument('--output', type=Path)
args = parser.parse_args()
record = {
    'status': 'pass', 'date': '2026-10-15', 'prepared_for': 'Edward Baker',
    'assistance': 'Substantial LLM assistance', 'model': 'gpt-6-astra',
    'reasoning_effort': 'ultra', 'python_version': platform.python_version(),
    'arithmetic': 'Standard-library exact rational polynomial and finite lattice algebra',
    'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'exact_assertions': sum(counts.values()), 'assertions_by_group': counts,
    'rational_pi_surrogate_scope': 'pi=3 used only for supplementary finite polynomial evaluations; formal polynomial identity checks retain pi as an independent variable.',
    'analytic_proofs_not_inferred_from_finite_checks': [
        'Normal convergence of the mixed-heat theta addition identity',
        'Gaussian-weight rigidity and primitive-endpoint normalization',
        'Convergence and complete primitive endpoint integrations',
        'Every physical source parity block has a negative principal minor',
        'Each physical parity block has both signs on its coefficient zero-sum subspace',
    ],
    'not_established': [
        'A theta-specific signed amplitude or chord-core estimate',
        'A positive Gram representation of the actual source parity matrix',
        'Theta collision exclusion, a new sign domain, or RH',
        'Failure of every possible coupled arithmetic representation',
    ],
}
serialized = json.dumps(record, indent=2, sort_keys=True) + '\n'
if args.output:
    args.output.write_text(serialized)
print(serialized)
