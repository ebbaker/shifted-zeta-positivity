#!/usr/bin/env python3
"""Exact finite algebra supporting S07-T1; not an analytic/RH certificate.

Prepared for Edward Baker, 19 October 2026, with substantial LLM assistance.
Actual model gpt-6.1-sol (Codex), reasoning effort ultra.

Standard library only.  Hermite/Gaussian computations use Fraction.  The
checker verifies the explicitly stated identities and counterfixtures; the
associated note supplies domains, convergence, trace proofs, and scope.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path


def clean(p):
    p = [F(x) for x in p]
    while len(p) > 1 and not p[-1]:
        p.pop()
    return p or [F(0)]


def add(a, b):
    return clean([(a[j] if j < len(a) else 0) +
                  (b[j] if j < len(b) else 0)
                  for j in range(max(len(a), len(b)))])


def scale(a, c):
    return clean([c*x for x in a])


def mul(a, b):
    p = [F(0)]*(len(a)+len(b)-1)
    for j, x in enumerate(a):
        for k, y in enumerate(b):
            p[j+k] += x*y
    return clean(p)


def deriv(a):
    return clean([j*a[j] for j in range(1, len(a))])


def factorial(n):
    ans = 1
    for j in range(2, n+1):
        ans *= j
    return ans


def moment(k):
    """Normalized integral v^k exp(-2v^2) / integral exp(-2v^2)."""
    if k % 2:
        return F(0)
    ans = F(1)
    for j in range(1, k//2+1):
        ans *= F(2*j-1, 4)
    return ans


def mean(a):
    return sum((x*moment(j) for j, x in enumerate(a)), F(0))


def inner(a, b):
    return mean(mul(a, b))


def raise_p(a):
    return add(mul([0, 2], a), scale(deriv(a), F(-1, 2)))


def lower_p(a):
    return scale(deriv(a), F(1, 2))


def encode(a):
    return [str(x) for x in clean(a)]


# Sparse multivariable Laurent polynomials.  These checks involve only
# identities; no rational-function or transcendental evaluation is hidden.
VARS = ('n', 's', 'r', 'p', 'y', 'q', 'k', 'x0', 'x1', 'x2')
NZERO = (0,)*len(VARS)


def mc(c):
    return {} if not c else {NZERO: F(c)}


def mv(name):
    e = list(NZERO)
    e[VARS.index(name)] = 1
    return {tuple(e): F(1)}


def ma(*ps):
    out = {}
    for p in ps:
        for e, c in p.items():
            out[e] = out.get(e, F(0)) + c
    return {e: c for e, c in out.items() if c}


def ms(p, c):
    return {e: F(c)*a for e, a in p.items() if c*a}


def mm(*ps):
    out = mc(1)
    for p in ps:
        nxt = {}
        for a, x in out.items():
            for b, y in p.items():
                e = tuple(i+j for i, j in zip(a, b))
                nxt[e] = nxt.get(e, F(0)) + x*y
        out = {e: c for e, c in nxt.items() if c}
    return out


def mp(p, n):
    if n < 0:
        if len(p) != 1:
            raise ValueError('negative power requires one monomial')
        (e, c), = p.items()
        return {tuple(n*i for i in e): c**n}
    out = mc(1)
    for _ in range(n):
        out = mm(out, p)
    return out


def sub(p, mapping):
    out = {}
    for e, c in p.items():
        term = mc(c)
        for j, power in enumerate(e):
            if power:
                term = mm(term, mp(mapping.get(VARS[j], mv(VARS[j])), power))
        out = ma(out, term)
    return out


def check():
    P = [[F(1)]]
    for _ in range(6):
        P.append(raise_p(P[-1]))
    expected = [[1], [0, 2], [-1, 0, 4], [0, -6, 0, 8],
                [3, 0, -24, 0, 16], [0, 30, 0, -80, 0, 32],
                [-15, 0, 180, 0, -240, 0, 64]]
    assert P == [clean(x) for x in expected]
    gram = [[inner(a, b) for b in P] for a in P]
    for j in range(7):
        for k in range(7):
            assert gram[j][k] == (factorial(j) if j == k else 0)
    for j in range(7):
        want = scale(P[j-1], j) if j else [F(0)]
        assert lower_p(P[j]) == want
        if j < 6:
            assert raise_p(P[j]) == P[j+1]
        for k in range(7):
            assert inner(raise_p(P[j]), P[k]) == inner(P[j], lower_p(P[k]))
    Q = scale(add(P[4], [-3]), F(1, 16))
    assert Q == clean([0, 0, F(-3, 2), 0, 1])
    assert inner(Q, Q) == F(33, 256)
    assert lower_p(Q) == scale(P[3], F(1, 4))
    assert lower_p(Q) != [F(0)]
    B5Q = Q
    for _ in range(5):
        B5Q = lower_p(B5Q)
    assert B5Q == [F(0)]
    # Since A = i sqrt(c) R and B = i sqrt(c) L, the polynomial
    # raising/lowering identities imply B A^j theta = -j c A^(j-1) theta.
    # The displayed adjoint identity implies A* = -B.

    n, s, r, p, y, q, k, x0, x1, x2 = [mv(v) for v in VARS]
    phase = ma(mm(p, mp(n, 2)), ms(mm(n, ma(r, mm(p, s))), 2))
    # s -> s+1, followed by reindexing old n = new n-1.
    shifted = sub(phase, {'s': ma(s, mc(1)), 'n': ma(n, mc(-1))})
    wanted = ma(phase, ms(p, -1), ms(r, -2), ms(mm(p, s), -2))
    assert shifted == wanted
    # In units of i*pi, differentiating the W phase in p and adding
    # the unitary connection a_p/pi=s^2-p^2 leaves y^2-p^2.
    raw_p = ma(mp(n, 2), ms(mm(n, s), 2), mp(s, 2), ms(mp(p, 2), -1))
    assert raw_p == sub(ma(mp(y, 2), ms(mp(p, 2), -1)), {'y': ma(n, s)})
    # In units of 2*pi*i, covariant r differentiates by n+s.
    assert ma(n, s) == sub(y, {'y': ma(n, s)})
    # (partial_s-p partial_r) cancels W phase; its connection cancels too.
    assert ma(ms(mm(n, p), 2), ms(mm(p, n), -2)) == {}
    assert ma(ms(mm(p, s), 2), ms(mm(p, s), -2)) == {}

    # Formal theta Fourier seam: c_(n+1)=t^(2n+1)c_n.  At N=0,
    # c_0=1,c_1=0 gives -t, which is nonzero for t=exp(pi*i*tau).
    t0, t1, t = F(1), F(0), [F(0), F(1)]
    seam_defect = add([t1], scale(t, -t0))
    assert seam_defect == [0, -1] and seam_defect != [0]
    finite_indices = {0}
    assert {j+1 for j in finite_indices} != finite_indices

    # p transport includes y^2: level four creates level six.
    v2P4 = mul([0, 0, 1], P[4])
    assert v2P4 == scale(add(add(P[6], scale(P[4], 9)), scale(P[2], 12)), F(1, 4))
    assert len(v2P4)-1 == 6 and inner(v2P4, P[6]) == F(factorial(6), 4)
    # A multiplication fixture demonstrates that cutoff/multiplier
    # residuals need not be pure high levels: (1-(1+v^2))*Q.
    residual_fixture = scale(mul([0, 0, 1], Q), -1)
    assert len(residual_fixture)-1 == 6
    assert inner(residual_fixture, P[0]) == F(3, 64)
    assert inner(residual_fixture, P[6]) != 0

    # Optional profile Jacobi algebra, k=pi.  For a=exp(-k*q*y^2),
    # derivatives are represented by their polynomial ratios to a.
    ay = ms(mm(k, q, y), -2)
    ayy = ma(ms(mm(k, q), -2), ms(mm(mp(k, 2), mp(q, 2), mp(y, 2)), 4))
    aq = ms(mm(k, mp(y, 2)), -1)
    potential = ma(ms(mm(k, mp(q, -1)), F(1, 2)), ms(mm(mp(k, 2), mp(y, 2)), -1))
    Jgaussian = ma(ms(mm(k, aq), 2), ms(mm(ayy, mp(q, -2)), F(1, 4)),
                   ms(mm(k, y, ay, mp(q, -1)), -1), potential)
    assert Jgaussian == {}
    # Product rules for chi(y)*a; x_j denotes chi^(j), j=0,1,2.
    product_yy = ma(mm(x0, ayy), ms(mm(x1, ay), 2), x2)
    Jproduct = ma(ms(mm(k, x0, aq), 2), ms(mm(product_yy, mp(q, -2)), F(1, 4)),
                  ms(mm(k, y, ma(mm(x0, ay), x1), mp(q, -1)), -1), mm(potential, x0))
    commutator = ma(ms(mm(x2, mp(q, -2)), F(1, 4)),
                    ms(mm(ay, x1, mp(q, -2)), F(1, 2)),
                    ms(mm(k, y, x1, mp(q, -1)), -1))
    assert Jproduct == commutator and commutator != {}

    # Rational bookkeeping for a proof in the note, rather than numerical
    # tests of infinite-dimensional sampling/trace theorems.
    # 1+2 sum_(n>=1) 1/(1+n²) <=1+2 sum 1/n²
    # <=1+2*(1+integral_1^infty x^-2 dx)=5.
    lattice_weight_sum_upper = F(1)+2*(F(1)+F(1))
    assert lattice_weight_sum_upper == 5
    # Interval-center sampling: |g(a)| <= ||g||+||g'||/sqrt(12).
    # With weight 1+a^2 <= 2(1+y^2), 2*(13/12)=13/6 <4.
    sampling_weighted_upper = 2*F(13, 12)
    assert sampling_weighted_upper == F(13, 6) < 4
    assert 5*4 == 20
    # Base interval length 1/2: averaging plus derivative kernel gives
    # |a(0)|^2 <= 4||a||^2+(1/12)||a'||^2 <=4||a||^2+||a'||^2.
    length = F(1, 2)
    base_value_constant = 2/length
    base_derivative_constant = 2*length/F(12)
    assert base_value_constant == 4 and base_derivative_constant == F(1, 12) <= 1

    return {
        'status': 'pass: exact finite algebra and rational budget checks',
        'scope': 'No interval physical-sign certificate, optimized kernel bound, global trace theorem, or RH conclusion is supplied by this checker.',
        'hermite_polynomials_P0_to_P6': [encode(a) for a in P],
        'normalized_gaussian_gram_0_to_6': [[str(a) for a in row] for row in gram],
        'source_polynomial': encode(Q),
        'source_squared_norm_normalized_gaussian': '33/256',
        'fiber_dimension_at_degree_four': 5,
        'verified_algebra': [
            'P_(j+1)=2v P_j-P_j_prime/2; P_j_prime/2=j P_(j-1)',
            'Gaussian moment Gram is delta_jk j!; polynomial raising is adjoint to lowering',
            'source (P4-3)/16=v^4-3v^2/2; B source !=0; B^5 source=0',
            'W s-shift reindexing gives exp(-pi*i*p-2pi*i*(r+p*s))',
            'Dp profile=partial_p+i*pi*(y^2-p^2); Dr profile=2pi*i*y; (Ds-pDr) profile=partial_y',
            'Jacobi profile annihilates Gaussian and has displayed cutoff commutator',
        ],
        'adversarial_fixtures': {
            'zero_mode_only_theta_truncation_seam_defect': encode(seam_defect),
            'level_four_p_transport_level_six_coefficient': '1/4 before physical scalings',
            'multiplier_residual_low_level_zero_coefficient': '3/64',
            'multiplier_residual_level_six_pairing': str(inner(residual_fixture, P[6])),
            'fourth_order_source_holomorphic': False,
            'V4_closed_under_p_covariant_derivative': False,
            'arbitrary_multiplier_residual_is_pure_high_level': False,
        },
        'rational_proof_budget': {
            'lattice_weight_sum_upper': str(lattice_weight_sum_upper),
            'chosen_lattice_sum_constant': 5,
            'weighted_sampling_upper': str(sampling_weighted_upper),
            'chosen_weighted_sampling_constant': 4,
            'chosen_fiber_X_norm_evaluation_squared_constant': 20,
            'base_interval_length': str(length),
            'base_L2_constant': str(base_value_constant),
            'base_derivative_constant_before_relaxation': str(base_derivative_constant),
            'chosen_base_derivative_constant': 1,
        },
        'analytic_premises_not_certified_by_finite_algebra': [
            'Theta/Fourier series convergence and globally smooth bundle domains',
            'Degree-one holomorphic dimension and ker(B^5) characterization',
            'Weil-Brezin isometry and Sobolev sample/trace proofs',
            'Specific smooth cutoff derivative bounds and all tail integrations',
            'Physical normalization, base trace, exterior tails and consumer error comparison',
        ],
    }


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    if not __debug__:
        raise RuntimeError('Run without Python -O: exact assertions must be enabled.')
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    repo = args.repo.resolve()
    if not (repo/'AGENTS.md').is_file():
        parser.error('--repo must identify the research repository')
    record = check()
    record['date'] = '2026-10-19'
    record['prepared_for'] = 'Edward Baker'
    record['llm_assistance'] = {'model': 'gpt-6.1-sol (Codex)', 'reasoning_effort': 'ultra'}
    sources = [
        repo/'papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/research-overview/01_RESEARCH_OVERVIEW_GOALS_AND_TASKS_20261018.md',
        repo/'papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/research-overview/02_S07_MISSING_ESTIMATES_AND_ALTERNATIVE_APPROACHES_20261018.md',
    ]
    note_dir = repo/'papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/07_geometric_duality_and_quaternionic_symmetry/notes'
    sources.extend(sorted(note_dir.glob('0[123]_*.md')))
    record['source_sha256'] = {str(p.relative_to(repo)): sha(p) for p in sources if p.is_file()}
    record['checker_sha256'] = sha(Path(__file__).resolve())
    record['hash_scope'] = 'Hashes identify reviewed text/code; they do not prove mathematical claims.'
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(record, indent=2, sort_keys=True)+'\n', encoding='utf-8')
    print('S07-T1 exact algebra checks pass; record: '+str(args.output.resolve()))


if __name__ == '__main__':
    main()
