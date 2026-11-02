#!/usr/bin/env python3
"""J-E01 r2 exact Q10/P7 audit, 1 November 2026.

Prepared for Edward Baker with substantial LLM assistance.
Actual recorded model gpt-6.1-sol (Codex), reasoning effort ultra.
Standard library only; reuses immutable r1 routines after checking their hash.
No source grid, theta numerical acquisition, minors or quadrature.
Run with --repo /path/to/checkout; stdout is the small deterministic record.
"""
import argparse
from fractions import Fraction as F
from hashlib import sha256
import importlib.util
import json
from math import factorial
from pathlib import Path
import sys


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, required=True)
    repo = parser.parse_args().repo.resolve()
    base = Path('papers/investigations-5/07_positive_theta_primitives')
    route = base/'jensen'
    helper = repo/route/'numerics/j_e01_audit.py'
    helper_hash = sha256(helper.read_bytes()).hexdigest()
    assert helper_hash == '5905598d1aba38d7e366df0b0fabf0b53a34f4ace21b4056a1a644e89d4f73e5'
    sys.dont_write_bytecode = True
    spec = importlib.util.spec_from_file_location('j_e01_r1_helpers', helper)
    old = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(old)
    add, scale, mul, der = old.add, old.scale, old.mul, old.der
    product, det, serial, coeffs = old.product, old.determinant3, old.serial, old.coeffs

    def power(p, n):
        one = {(0,)*len(next(iter(p))): F(1)}
        return product(one, *([p]*n))

    # Same canonical Jacobi field; generate only Q0..Q10.
    a, z, chi = ({e: F(1)} for e in [(1, 0, 0), (0, 1, 0), (0, 0, 1)])
    one = {(0, 0, 0): F(1)}
    field = [scale(add(z, mul(a, a), scale(one, -1)), F(1, 2)),
             scale(mul(z, add(a, chi)), 2), add(mul(a, chi), scale(z, -1))]

    def D(p):
        return add(*(mul(field[j], der(p, j)) for j in range(3)))

    Q = [add(z, scale(add(mul(a, a), scale(one, -1)), F(3, 2)))]
    for j in range(10):
        Q.append(add(D(Q[-1]), scale(mul(a, Q[-1]), F(1, 4))))
    previous_path = repo/route/'numerics/J_E01_R1_EXACT_RECORD_20261101.json'
    assert sha256(previous_path.read_bytes()).hexdigest() == '923b67d799a4c87af4efdabd7a23c4f02a428473886da0b23b9ace4f89ce41bb'
    previous = json.loads(previous_path.read_text())
    assert [serial(q) for q in Q[:9]] == previous['Q']
    p = [{(e[1],): c*4**j for e, c in q.items() if e[0] == e[2] == 0}
         for j, q in enumerate(Q)]
    assert all(not p[j] for j in [1, 3, 5, 7, 9])
    p0 = p[0]

    # Quotient x-series via denominator*quotient=numerator, through x^3.
    # term[j] is the numerator over p0^(j+1), before multiplying j!.
    den = [scale(p[2*j], F(1, factorial(2*j))) for j in range(4)]

    def quotient(offset):
        num = [scale(p[2*j+offset], F(1, factorial(2*j))) for j in range(4)]
        terms = []
        for j in range(4):
            terms.append(add(mul(num[j], power(p0, j)),
                             *(scale(product(den[i], terms[j-i], power(p0, i-1)), -1)
                               for i in range(1, j+1))))
        for j in range(4):
            assert add(terms[j], *(product(den[i], terms[j-i], power(p0, i-1))
                                    for i in range(1, j+1))) == mul(num[j], power(p0, j))
        return [scale(v, factorial(j)) for j, v in enumerate(terms)]

    r, t = quotient(2), quotient(4)
    Hnum = add(mul(r[1], t[2]), scale(mul(t[1], r[2]), -1))
    Hpnum = add(mul(r[1], t[3]), scale(mul(t[1], r[3]), -1))
    Jraw = add(mul(r[1], Hpnum), scale(mul(Hnum, r[2]), -3))
    # Jraw/p0^8; cancellation leaves M/p0^6 with positive prefactor 768/5.
    A0 = add(mul(p0, p[4]), scale(mul(p[2], p[2]), -1))
    N0 = det([[p[0], p[2], p[4]], [p[2], p[4], p[6]], [p[4], p[6], p[8]]])
    assert r[1] == scale(A0, F(1, 2))
    assert Hnum == scale(mul(N0, power(p0, 2)), F(1, 24))
    m_expected = [0, 5157219375, 197546060250, -400881899250,
                  -2617975845450, 1837905778800, -5088891988890,
                  1978703613270, 1297491608430, -950010914439,
                  237333481512, -35580583380, -1384014396,
                  1983548600, -458690000, 112500000]
    M = {(j,): F(c) for j, c in enumerate(m_expected) if c}
    assert Jraw == scale(mul(M, power(p0, 2)), F(768, 5))
    shifted = old.translate(M, F(47, 10))
    assert len(shifted) == 16 and all(c > 0 for c in shifted.values())
    assert all(c > 0 for c in old.translate(A0, F(47, 10)).values())
    assert all(c < 0 for c in old.translate(N0, F(47, 10)).values())
    z_lower = F(previous['origin']['analytic_U_lower_bound'])
    assert z_lower > F(47, 10)

    # Check K in the canonical differential algebra through Q7 only.
    A = add(mul(Q[0], Q[3]), scale(mul(Q[1], Q[2]), -1))
    Dr = add(product(Q[0], Q[0], Q[4]),
             scale(product(Q[0], Q[2], Q[2]), -1),
             scale(product(Q[0], Q[1], Q[3]), -2),
             scale(product(Q[1], Q[1], Q[2]), 2))
    N = det([[Q[0], Q[1], Q[2]], [Q[2], Q[3], Q[4]], [Q[4], Q[5], Q[6]]])
    Cprime = add(mul(Q[0], D(N)), scale(mul(N, D(Q[0])), -3))
    Knum = add(mul(A, Cprime), scale(mul(N, Dr), -3))

    # First-summand tail: exactly P0..P7.
    y, one1 = {(1,): F(1)}, {(0,): F(1)}
    P = [add(scale(mul(y, y), 2), scale(y, -3))]
    for j in range(7):
        P.append(add(scale(mul(y, der(P[-1], 0)), 4),
                     mul(add(one1, scale(y, -4)), P[-1])))
    assert [coeffs(q) for q in P[:7]] == previous['tail']['P']
    d = add(scale(y, 2), scale(one1, -3))
    at = {(e[0]-1,): c for e, c in P[2].items()}
    bt = {(e[0]-1,): c for e, c in P[4].items()}
    rt = add(mul(der(at, 0), d), scale(at, -2))
    st = add(mul(der(bt, 0), d), scale(bt, -2))
    w = add(mul(rt, der(st, 0)), scale(mul(st, der(rt, 0)), -1))
    kt = add(mul(d, add(mul(rt, der(w, 0)), scale(mul(w, der(rt, 0)), -3))),
             scale(mul(rt, w), 4))
    kp = [-654885, 3056130, -6180300, 7280280, -5589360,
          2917728, -1034304, 239232, -32768, 2048]
    reduced_tail = {(j,): F(c) for j, c in enumerate(kp)}
    assert kt == scale(reduced_tail, 3*2**16)
    assert kt.get((10,), 0) == 0
    assert F(1024)*kt[(9,)]/2**7 == 3*2**30

    # Gaussian equality: normalized phi^(j) through j=4, in (a,u).
    ga, gu, gu1 = {(1, 0): F(1)}, {(0, 1): F(1)}, {(0, 0): F(1)}
    jets = [gu1]
    for j in range(4):
        jets.append(add(der(jets[-1], 1), scale(product(ga, gu, jets[-1]), -2)))
    gaussian_relation = add(mul(jets[2], jets[2]), scale(mul(ga, jets[2]), -8),
                            scale(mul(ga, ga), -8))
    assert jets[4] == gaussian_relation
    simplex_area, gaussian_gsecond = F(1, 2), F(2)
    assert simplex_area*gaussian_gsecond == 1

    # Pairwise lattice identity, no evaluation grid.
    vs = [{tuple(int(i == j) for i in range(4)): F(1)} for j in range(4)]
    aa, bb, cc, dd = vs
    diff = add(product(add(dd, scale(aa, -1)), add(bb, scale(cc, -1))),
               scale(product(add(bb, scale(aa, -1)), add(dd, scale(cc, -1))), -1))
    assert diff == product(add(cc, scale(aa, -1)), add(bb, scale(dd, -1)))

    paths = [Path('AGENTS.md'), Path('GPT_RESEARCH_MODEL_WORKFLOW.md'), Path('LARGE_FILES.md'),
             Path('tools/CHAT_HISTORY.md'),
             route/'notes/01_J_B01_COEFFICIENT_REPRESENTATION_DECISION_20261101.md',
             route/'notes/03_J_E01_R1_REPRESENTATION_AND_ENDPOINT_TAIL_RETURN_20261101.md',
             route/'notes/04_CONTINUATION_AFTER_J_E01_ORIGIN_OBSTRUCTION_20261101.md',
             route/'notes/05_J_B01_SIGNED_AVERAGING_DECISION_20261101.md',
             route/'notes/06_CONTINUATION_FOR_SOL_SIGNED_AVERAGING_AUDIT_20261101.md',
             route/'numerics/j_e01_audit.py', route/'numerics/J_E01_R1_EXACT_RECORD_20261101.json',
             base/'notes/02_CNV_DETERMINANT_TRANSFER_AND_THETA_DIFFERENTIAL_CLOSURE_20261101.md',
             base/'references/05_SIGNED_AVERAGING_SOURCES_20261101.md']
    record = dict(date='2026-11-01', prepared_for='Edward Baker', llm_assistance='substantial',
                  model='gpt-6.1-sol', effort='ultra', task='J-E01', request_revision='r2',
                  arithmetic='exact rational polynomial arithmetic; Python standard library',
                  code_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),
                  input_sha256={str(p): sha256((repo/p).read_bytes()).hexdigest() for p in paths},
                  limits=dict(max_Q=10, max_P=7, optional_theta_numerical_acquisition=False,
                              source_grid=False, coefficient_minors=False, quadrature=False),
                  Q_variables=['a', 'U', 'chi'], Q=[serial(q) for q in Q],
                  interior_K=dict(formula='K=4^13*Knum/Q0^6', numerator=serial(Knum)),
                  origin=dict(p_even={str(j): coeffs(p[j]) for j in [0, 2, 4, 6, 8, 10]},
                              Rhat_derivative_numerators=[coeffs(v) for v in r],
                              That_derivative_numerators=[coeffs(v) for v in t],
                              quotient_denominator='derivative j has denominator p0^(j+1)',
                              J0_formula='(768/5)*M(z)/(z-3/2)^6', M=coeffs(M),
                              translate='z=s+47/10', translated_M=coeffs(shifted),
                              U_lower_bound=str(z_lower), J0_sign='strictly positive',
                              inherited_signs=dict(Rhat_prime='positive', H0='negative')),
                  tail=dict(P=[coeffs(q) for q in P], r=coeffs(rt), s=coeffs(st), w=coeffs(w),
                            unreduced_K_numerator=coeffs(kt), reduced_K_polynomial=coeffs(reduced_tail),
                            K1_formula='3*2^26*t^5*polynomial/(2*t-3)^7',
                            degree_10_cancellation=True, K_leading_coefficient=str(3*2**30),
                            K_leading_power=7, K_remainder='O(t^6)+O(t^11*exp(-3*t))',
                            differentiated_theta_order=7, K_sign='eventually strictly positive',
                            Rprime_sign='eventually strictly positive', effective_cutoff=False),
                  gaussian=dict(g_second='2', simplex_area='1/2', divided_difference='1', A_k='1'),
                  checks=dict(r1_Q_and_P_preserved=True, quotient_series=True,
                              J_complete_mixed_numerator=True, shifted_M_positive=True,
                              inherited_origin_signs=True, no_numeric_theta_acquisition=True,
                              tail_K_exact=True, leading_cancellation=True,
                              Gaussian_relation=True, pair_lattice_identity=True),
                  disposition='Complete bounded supportive return; next [B] J-B02 — Astra for global Rprime>0 and K>=0')
    print(json.dumps(record, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    main()
