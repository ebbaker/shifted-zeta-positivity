#!/usr/bin/env python3
"""Independent checks for the round-one cross-model review of Project 04.

Prepared for Edward Baker with LLM assistance. Model: Claude Opus 5.5
(configured identifier claude-opus-5-5), Claude Cowork, reasoning effort max,
17 October 2026. The serving model may differ from the configured identifier.
Support computations for
papers/investigations-3/04_sonin_mixed_prime_response/reviews/
01_ROUND_ONE_CROSS_MODEL_REVIEW_CLAUDE_20261017.md.

Standard library only. Nothing is imported from the round, which has no
programs of its own. The finite models below test the operator algebra of the
round's identities: they are exact identities in matrices, valid for any
commuting unitaries, any positive source operator and any projection, so they
check the algebra and its bookkeeping, not the actual Sonin projection, which
no finite model contains.

Sections
  A  SHA-256 digests of the reviewed round artifacts and inherited sources
  B  exact rational finite models: Note 01 (8), (10)-(13); Note 02 (4)-(7);
     the one-prime law (A3); the 3x3 coefficient matrix; a commuting-projection
     case where every return vanishes and the metric correction is exactly
     minus the signed Gram term; negative controls that must fail; the
     generic a priori bound on the mixed response
  C  the generic two-dimensional control of Note 01 Section 6: formula (23)
     exactly; the actual weights at t = pi/log 2; its vanishing second order
     for the balanced projection; second-order responses of either sign for a
     tilted projection
  D  the boundary resolvent identity and bound of Note 02 (21) / manuscript
     Proposition 7.1 on exact symmetric involutions
  E  the boundary-to-source kernel identity of Note 02 (17)-(18) / manuscript
     (3.4), by three routes, in exact Gaussian-rational polynomial arithmetic,
     with orientation and factor-two negative controls
  F  gamma-sector asymptotics (floating): the diagonal Gamma[F_tau]; the
     signed Gram gamma term of Note 02 (12) for p=2, q=3, L=6/5; the gamma part
     of the one-prime source transport B_S[J_2 F] - B_S[F]; an
     inaccessible-shift illustration. Box-spline bumps (C^4) stand in for the
     smooth bumps: the asymptotics use only moment bounds on |h^|^2
  G  constants: first-pair coefficients; inherited gap bounds and the
     amplification in the enclosure contract; a priori bounds; condition growth
     along the support-adapted place sets

Status: sections B-E exact rational arithmetic (Fractions), except the
operator-norm comparison in D, which is floating; sections F-G floating.
Floating results are diagnostics, not certificates. The program exits with
status 1 if any exact check fails or a negative control fails to fail.
"""
import argparse
import cmath
import hashlib
import json
import math
import platform
import sys
import time
from fractions import Fraction as Fr
from pathlib import Path

SCHEMA = "project04_round1_claude_review_checks_v1"
FAILURES = []


def check(name, ok):
    if not ok:
        FAILURES.append(name)
    return bool(ok)


def fstr(x):
    return str(x) if isinstance(x, Fr) else repr(x)


# --------------------------------------------------------------------------
# A. digests
# --------------------------------------------------------------------------
PROJECT = "papers/investigations-3/04_sonin_mixed_prime_response/"
ARTIFACTS = [
    PROJECT + "notes/round-1/01_EXACT_MIXED_RESPONSE_AND_FINITE_TRANSLATE_OBSTRUCTION_CODEX_20261017.md",
    PROJECT + "notes/round-1/02_CORRECTED_SIGNED_WEIL_GRAM_AND_MIXED_SOURCE_ESTIMATES_CODEX_20261017.md",
    PROJECT + "notes/round-1/README.md",
    PROJECT + "manuscript/sonin_mixed_prime_response.tex",
    PROJECT + "manuscript/README.md",
    PROJECT + "README.md",
    PROJECT + "DRAFT_HISTORY.md",
    PROJECT + "research-overview/01_INITIAL_RESEARCH_PROPOSAL_20261016.md",
]
INHERITED = [
    "papers/investigations/sonin-critical-boundary/notes/FINITE_EULER_BOUNDARY_IDENTITY_20261003.md",
    "papers/weil-positivity/susy-positivity/investigations/wilson-loewner/arithmetic-storage/notes/SONIN_CANONICAL_COMPARISON_AUDIT_20260929.md",
    "papers/weil-positivity/susy-positivity/investigations/wilson-loewner/arithmetic-storage/notes/SONIN_PLACE_ADDITION_AND_ERROR_CONTROL_20260929.md",
    "papers/investigations/sonin-critical-boundary/notes/CLOSED_SOURCE_RELATIVE_COMPARISON_20261003.md",
    "papers/investigations/sonin-critical-boundary/notes/COMPACT_CORRECTION_AND_REVISED_B_20261003.md",
    "papers/brainstorm/investigations-3/reviews/03_REPLY_TO_CODEX_RESPONSE_CLAUDE_20261016.md",
    "papers/investigations-3/reviews/01_PORTFOLIO_SETUP_REVIEW_CLAUDE_20261016.md",
]


def section_A(repo_root):
    out = {"reviewed": {}, "inherited": {}, "missing": []}
    if repo_root is None:
        out["note"] = "no --repo-root given; digests skipped"
        return out
    root = Path(repo_root)
    for key, group in (("reviewed", ARTIFACTS), ("inherited", INHERITED)):
        for rel in group:
            p = root / rel
            if p.is_file():
                out[key][rel] = hashlib.sha256(p.read_bytes()).hexdigest()
            else:
                out["missing"].append(rel)
    return out


# --------------------------------------------------------------------------
# exact matrix helpers (Fractions)
# --------------------------------------------------------------------------
def eye(n):
    return [[Fr(int(i == j)) for j in range(n)] for i in range(n)]


def zeros(n, m):
    return [[Fr(0)] * m for _ in range(n)]


def tp(A):
    return [list(r) for r in zip(*A)]


def mm(*Ms):
    R = Ms[0]
    for B in Ms[1:]:
        Bt = list(zip(*B))
        R = [[sum((a * b for a, b in zip(row, col)), Fr(0)) for col in Bt] for row in R]
    return R


def madd(A, B):
    return [[a + b for a, b in zip(ra, rb)] for ra, rb in zip(A, B)]


def msub(A, B):
    return [[a - b for a, b in zip(ra, rb)] for ra, rb in zip(A, B)]


def msc(c, A):
    return [[c * a for a in r] for r in A]


def mtr(A):
    return sum((A[i][i] for i in range(len(A))), Fr(0))


def minv(A):
    n = len(A)
    M = [list(r) + [Fr(int(i == j)) for j in range(n)] for i, r in enumerate(A)]
    for c in range(n):
        piv = next((r for r in range(c, n) if M[r][c] != 0), None)
        if piv is None:
            raise ZeroDivisionError("singular matrix")
        M[c], M[piv] = M[piv], M[c]
        pv = M[c][c]
        M[c] = [x / pv for x in M[c]]
        for r in range(n):
            if r != c and M[r][c] != 0:
                f = M[r][c]
                M[r] = [x - f * y for x, y in zip(M[r], M[c])]
    return [row[n:] for row in M]


def meq(A, B):
    return all(a == b for ra, rb in zip(A, B) for a, b in zip(ra, rb))


def blockdiag(blocks):
    n = sum(len(b) for b in blocks)
    R = zeros(n, n)
    o = 0
    for b in blocks:
        k = len(b)
        for i in range(k):
            for j in range(k):
                R[o + i][o + j] = Fr(b[i][j])
        o += k
    return R


def rot(c, s):
    # multiplication by the unit complex number c + i s, real 2x2 form
    return [[Fr(c), -Fr(s)], [Fr(s), Fr(c)]]


def cmul(x, y):
    # multiplication by x + i y; commutes with every rot block
    return [[Fr(x), -Fr(y)], [Fr(y), Fr(x)]]


def proj_onto(X):
    G = mm(tp(X), X)
    return mm(X, minv(G), tp(X)), G


# --------------------------------------------------------------------------
# B. exact finite models of the round's operator identities
# --------------------------------------------------------------------------
class Model:
    """Commuting real rotations U_p, U_q (block form of commuting unitaries),
    a source operator C_F commuting with them, a rational base projection P
    onto span(X), and rational weights r_p, r_q in (0,1)."""

    def __init__(self, Up_blocks, Uq_blocks, CF_blocks, X, rp, rq):
        self.Up = blockdiag([rot(*b) for b in Up_blocks])
        self.Uq = blockdiag([rot(*b) for b in Uq_blocks])
        self.CF = blockdiag([cmul(*b) for b in CF_blocks])
        self.n = len(self.Up)
        self.X = [[Fr(v) for v in row] for row in X]
        self.rp, self.rq = Fr(rp), Fr(rq)
        self.AF = mm(tp(self.CF), self.CF)
        self.P, self.G = proj_onto(self.X)
        self.Gi = minv(self.G)
        self.I = eye(self.n)
        self.k = len(self.X[0])
        self.Ik = eye(self.k)
        self.bp = 2 * self.rp / (1 + self.rp ** 2)
        self.bq = 2 * self.rq / (1 + self.rq ** 2)
        self.Ep = msc(-self.bp / 2, madd(self.Up, tp(self.Up)))
        self.Eq = msc(-self.bq / 2, madd(self.Uq, tp(self.Uq)))
        self.Q = msub(self.I, self.P)

    def br(self, O):
        # matrix of the compression P O P on Ran P, in the basis X
        return mm(self.Gi, tp(self.X), O, self.X)

    def direct_B(self, factors):
        # ||C_F Pi_A||_HS^2 with Pi_A the orthogonal projection onto D_A Ran P
        D = self.I
        for U, r in factors:
            D = mm(D, msub(self.I, msc(r, U)))
        Y = mm(D, self.X)
        Pi, _ = proj_onto(Y)
        return mtr(mm(Pi, self.AF))


def model_checks(m, label):
    out = {"label": label, "n": m.n, "rank_P": m.k,
           "r_p": fstr(m.rp), "r_q": fstr(m.rq),
           "beta_p": fstr(m.bp), "beta_q": fstr(m.bq)}
    I, Ik = m.I, m.Ik
    # direct traces at the four corners
    B_S = m.direct_B([])
    B_p = m.direct_B([(m.Up, m.rp)])
    B_q = m.direct_B([(m.Uq, m.rq)])
    B_pq = m.direct_B([(m.Up, m.rp), (m.Uq, m.rq)])
    mix_direct = B_pq - B_p - B_q + B_S
    out["B_S"], out["B_p"], out["B_q"], out["B_pq"] = map(fstr, (B_S, B_p, B_q, B_pq))
    out["mixed_direct"] = fstr(mix_direct)
    # Note 01 (6)-(8)
    a, b, c = m.br(m.Ep), m.br(m.Eq), m.br(mm(m.Ep, m.Eq))
    N0, Np = m.br(m.AF), m.br(mm(m.Ep, m.AF))
    Nq, Npq = m.br(mm(m.Eq, m.AF)), m.br(mm(m.Ep, m.Eq, m.AF))
    Mm = madd(madd(madd(Ik, a), b), c)
    Ia, Ib = madd(Ik, a), madd(Ik, b)
    f_S = mtr(N0)
    f_p = mtr(mm(minv(Ia), madd(N0, Np)))
    f_q = mtr(mm(minv(Ib), madd(N0, Nq)))
    f_pq = mtr(mm(minv(Mm), madd(madd(madd(N0, Np), Nq), Npq)))
    out["note01_eq8_four_traces"] = check(label + ":N01(8)",
                                          (f_S, f_p, f_q, f_pq) == (B_S, B_p, B_q, B_pq))
    # Note 01 (9)-(11)
    Lp, Lq, Lpq = msub(Np, mm(a, N0)), msub(Nq, mm(b, N0)), msub(Npq, mm(c, N0))
    inner = msub(msub(Lpq, mm(madd(b, c), minv(Ia), Lp)), mm(madd(a, c), minv(Ib), Lq))
    mix10 = mtr(mm(minv(Mm), inner))
    out["note01_eq10_mixed_formula"] = check(label + ":N01(10)", mix10 == mix_direct)
    out["note01_eq11_resolvent"] = check(label + ":N01(11)",
        meq(msub(minv(Mm), minv(Ia)), msc(-1, mm(minv(Mm), madd(b, c), minv(Ia)))))
    # Note 01 (12)-(13)
    out["note01_eq12_defects"] = check(label + ":N01(12)",
        meq(Lp, m.br(mm(m.Ep, m.Q, m.AF))) and meq(Lq, m.br(mm(m.Eq, m.Q, m.AF)))
        and meq(Lpq, m.br(mm(m.Ep, m.Eq, m.Q, m.AF))))
    ret = msub(c, mm(a, b))
    out["note01_eq13_return"] = check(label + ":N01(13)", meq(ret, m.br(mm(m.Ep, m.Q, m.Eq))))
    out["return_c_minus_ab_nonzero"] = any(x != 0 for r in ret for x in r)
    out["a_b_commute"] = meq(mm(a, b), mm(b, a))
    # Note 02 (3)-(4): normalized transport, B_{S u A} = B_S[J_A F] + Z_A
    GA = {"p": madd(I, m.Ep), "q": madd(I, m.Eq),
          "pq": mm(madd(I, m.Ep), madd(I, m.Eq))}
    Bdir = {"p": B_p, "q": B_q, "pq": B_pq}
    Z, BJ = {}, {}
    ok4 = True
    for key, Gm in GA.items():
        MA, NA = m.br(Gm), m.br(mm(Gm, m.AF))
        BJ[key] = mtr(NA)
        Z[key] = mtr(mm(msub(minv(MA), Ik), NA))
        ok4 = ok4 and (BJ[key] + Z[key] == Bdir[key])
    out["note02_eq4_transport"] = check(label + ":N02(4)", ok4)
    Rmet = Z["pq"] - Z["p"] - Z["q"]
    Gram_BS = mtr(m.br(mm(m.Ep, m.Eq, m.AF)))
    out["note02_eq7_gram_plus_metric"] = check(label + ":N02(7)", Gram_BS + Rmet == mix_direct)
    out["G_BS"], out["R_met"] = fstr(Gram_BS), fstr(Rmet)
    # Note 02 (5): four shifts +-log p +-log q, grouped into a_+ and a_-
    Upq, Upqt = mm(m.Up, m.Uq), mm(m.Up, tp(m.Uq))
    four = sum((mtr(m.br(mm(U, m.AF))) for U in
                (Upq, tp(Upq), Upqt, tp(Upqt))), Fr(0))
    grouped = mtr(m.br(mm(Upq, m.AF))) + mtr(m.br(mm(Upqt, m.AF)))
    out["note02_eq5_coefficient"] = check(label + ":N02(5)",
        Gram_BS == m.bp * m.bq / 4 * four and Gram_BS == m.bp * m.bq / 2 * grouped)
    # place-addition (A3): delta_p = -(r/(1+r^2)) Tr (I - beta T)^{-1} X
    Zp = madd(m.Up, tp(m.Up))
    Tm = m.br(msc(Fr(1, 2), Zp))
    Xop = m.br(mm(Zp, m.Q, m.AF))
    dA3 = -(m.rp / (1 + m.rp ** 2)) * mtr(mm(minv(msub(Ik, msc(m.bp, Tm))), Xop))
    out["A3_one_prime_law"] = check(label + ":A3", dA3 == B_p - B_S)
    # generic a priori bound from (10): |M| <= C beta_p beta_q B_S
    bp, bq = m.bp, m.bq
    C = 2 / ((1 - bp) * (1 - bq)) * (1 + (1 + bp) / (1 - bp) + (1 + bq) / (1 - bq))
    bound = C * bp * bq * B_S
    out["apriori_bound"] = fstr(bound)
    out["apriori_ratio_float"] = float(abs(mix_direct) / bound) if bound else None
    out["apriori_bound_holds"] = check(label + ":apriori", abs(mix_direct) <= bound)
    # negative controls: plausible wrong formulas must fail
    no_inverse_mix = (BJ["pq"] - BJ["p"] - BJ["q"] + B_S)   # transport the source, drop metric
    wrong_sign = mtr(mm(minv(Mm), madd(madd(Lpq, mm(madd(b, c), minv(Ia), Lp)),
                                     mm(madd(a, c), minv(Ib), Lq))))
    order_swapped = mtr(mm(minv(Mm), msub(msub(Lpq, mm(minv(Ia), madd(b, c), Lp)),
                                         mm(minv(Ib), madd(a, c), Lq))))
    neg = {
        "drop_inverse_metric_differs": no_inverse_mix != mix_direct,
        "sign_flip_in_(11)_differs": wrong_sign != mix_direct,
        "factor_order_swapped_differs": order_swapped != mix_direct,
    }
    out["negative_controls"] = neg
    # the factor-order variant can agree by accident when a commutes with b+c;
    # record it, but require only the first two to fail
    check(label + ":neg_drop_inverse", neg["drop_inverse_metric_differs"])
    check(label + ":neg_sign_flip", neg["sign_flip_in_(11)_differs"])
    return out


def section_B():
    res = {"models": []}
    # Pythagorean rotations: rational cosine and sine
    Up = [(Fr(3, 5), Fr(4, 5)), (Fr(5, 13), Fr(-12, 13)),
          (Fr(-8, 17), Fr(15, 17)), (Fr(7, 25), Fr(24, 25))]
    Uq =[(Fr(20, 29), Fr(21, 29)), (Fr(-12, 37), Fr(35, 37)),
          (Fr(9, 41), Fr(-40, 41)), (Fr(28, 53), Fr(45, 53))]
    CF1 = [(1, 2), (-3, 1), (2, -1), (Fr(1, 2), 1)]
    CF2 = [(2, 0), (Fr(1, 3), -1), (-1, 3), (1, 1)]
    X1 = [[1, 0, 2], [2, 1, 0], [0, 1, 1], [1, -1, 0],
          [0, 2, -1], [1, 0, 1], [-1, 1, 0], [0, 0, 1]]
    X2 = [[1, 2], [0, 1], [3, -1], [1, 1], [-2, 0], [0, 1], [1, 0], [2, -1]]
    cases = [
        (Up, Uq, CF1, X1, Fr(1, 2), Fr(2, 5), "rank3_CF1"),
        (Up, Uq, CF2, X1, Fr(1, 2), Fr(2, 5), "rank3_CF2"),
        (Up, Uq, CF1, X2, Fr(1, 3), Fr(3, 7), "rank2_CF1"),
        (Up, Uq, CF2, X2, Fr(5, 7), Fr(3, 5), "rank2_CF2_large_r"),
    ]
    for args in cases:
        res["models"].append(model_checks(Model(*args[:6]), args[6]))
    # a base projection that commutes with the translations: every return vanishes
    Xc = [[1, 0], [0, 1], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
    mc = Model(Up, Uq, CF1, Xc, Fr(1, 2), Fr(2, 5))
    Bs = mc.direct_B([])
    Bp = mc.direct_B([(mc.Up, mc.rp)])
    Bq = mc.direct_B([(mc.Uq, mc.rq)])
    Bpq = mc.direct_B([(mc.Up, mc.rp), (mc.Uq, mc.rq)])
    # in this case the space does not move, so the metric correction is exactly
    # minus the source-transport (signed Gram) term
    Ik = mc.Ik
    Zc = {}
    for key, Gm in (("p", madd(mc.I, mc.Ep)), ("q", madd(mc.I, mc.Eq)),
                    ("pq", mm(madd(mc.I, mc.Ep), madd(mc.I, mc.Eq)))):
        Zc[key] = mtr(mm(msub(minv(mc.br(Gm)), Ik), mc.br(mm(Gm, mc.AF))))
    G_c = mtr(mc.br(mm(mc.Ep, mc.Eq, mc.AF)))
    R_c = Zc["pq"] - Zc["p"] - Zc["q"]
    res["commuting_projection"] = {
        "increments": [fstr(Bp - Bs), fstr(Bq - Bs)],
        "mixed": fstr(Bpq - Bp - Bq + Bs),
        "all_zero": check("B:commuting_projection",
                          Bp == Bs and Bq == Bs and Bpq == Bs),
        "G_BS": fstr(G_c), "R_met": fstr(R_c),
        "R_met_equals_minus_G_BS": check("B:commuting_Rmet", G_c != 0 and R_c == -G_c),
    }
    # second-order coefficient of the mixed response for small weights:
    # M = beta_p beta_q mu_2 + O(beta^3), with e_j = -(U_j + U_j^T)/2 and Q = I - P,
    # mu_2 = Tr P e_q Q e_p Q A_F P - Tr (P e_p P)(P e_q Q A_F P)   (derived in the review)
    m0 = Model(Up, Uq, CF1, X1, Fr(1, 2), Fr(2, 5))
    ep = msc(Fr(-1, 2), madd(m0.Up, tp(m0.Up)))
    eq = msc(Fr(-1, 2), madd(m0.Uq, tp(m0.Uq)))
    mu2 = mtr(m0.br(mm(eq, m0.Q, ep, m0.Q, m0.AF))) - mtr(mm(m0.br(ep), m0.br(mm(eq, m0.Q, m0.AF))))
    mu2_swapped = mtr(m0.br(mm(ep, m0.Q, eq, m0.Q, m0.AF))) - mtr(mm(m0.br(eq), m0.br(mm(ep, m0.Q, m0.AF))))
    scan = []
    for e in (10, 100, 1000):
        me = Model(Up, Uq, CF1, X1, Fr(1, e), Fr(2, 3 * e))
        Bs = me.direct_B([])
        Bp = me.direct_B([(me.Up, me.rp)])
        Bq = me.direct_B([(me.Uq, me.rq)])
        Bpq = me.direct_B([(me.Up, me.rp), (me.Uq, me.rq)])
        ratio = (Bpq - Bp - Bq + Bs) / (me.bp * me.bq)
        scan.append({"r_p": fstr(me.rp), "ratio": float(ratio), "ratio_minus_mu2": float(ratio - mu2)})
    errs = [abs(s["ratio_minus_mu2"]) for s in scan]
    res["second_order_coefficient"] = {
        "mu2": float(mu2), "symmetric_in_p_q": check("B:mu2_symmetric", mu2 == mu2_swapped),
        "nonzero": mu2 != 0, "scan": scan,
        "converges": check("B:mu2_limit", errs[-1] < errs[0] / 50),
    }
    # the 3x3 Gram coefficient matrix of Note 02 (5): char poly l^3 - 2 w^2 l
    w = Fr(7, 13)
    W = [[0, w, w], [w, 0, 0], [w, 0, 0]]

    def det3(A):
        return (A[0][0] * (A[1][1] * A[2][2] - A[1][2] * A[2][1])
                - A[0][1] * (A[1][0] * A[2][2] - A[1][2] * A[2][0])
                + A[0][2] * (A[1][0] * A[2][1] - A[1][1] * A[2][0]))
    okW = True
    for lam in (Fr(0), Fr(1), Fr(-2), Fr(3, 7)):
        A = [[(lam if i == j else 0) - W[i][j] for j in range(3)] for i in range(3)]
        okW = okW and det3(A) == lam ** 3 - 2 * w ** 2 * lam
    res["gram_matrix_charpoly"] = check("B:gram_charpoly", okW)
    res["gram_matrix_note"] = ("det(lI-W)=l^3-2w^2 l, so eigenvalues 0, +-sqrt(2) w; "
                               "with w=beta_p beta_q/4 these are +-beta_p beta_q/(2 sqrt 2)")
    return res


# --------------------------------------------------------------------------
# C. the generic two-dimensional control
# --------------------------------------------------------------------------
def twod_mixed(v, cos_p, cos_q, rp, rq, k1, k2):
    """Exact mixed response for P = |v><v| on C^2 (real v), translations
    diag(1, e^{-i theta_j}), source energies diag(k1, k2).  Uses the transported
    projection directly: B_A = sum_i k_i |(D_A v)_i|^2 / ||D_A v||^2."""
    def h(r, cs):
        return ((1 - r) ** 2, 1 + r * r - 2 * r * cs)
    hp, hq = h(rp, cos_p), h(rq, cos_q)

    def B(ws):
        num = k1 * v[0] ** 2 * ws[0] + k2 * v[1] ** 2 * ws[1]
        den = v[0] ** 2 * ws[0] + v[1] ** 2 * ws[1]
        return num / den
    Bs = B((1, 1))
    Bp = B(hp)
    Bq = B(hq)
    Bpq = B((hp[0] * hq[0], hp[1] * hq[1]))
    return Bpq - Bp - Bq + Bs, (Bs, Bp, Bq, Bpq), hp, hq


def section_C():
    res = {}
    # C1: formula (23) exactly, with rational stand-ins
    rows, ok = [], True
    for (rp, rq, cp, cq) in ((Fr(1, 2), Fr(1, 3), Fr(-1), Fr(7, 25)),
                             (Fr(2, 3), Fr(1, 5), Fr(3, 5), Fr(-4, 5)),
                             (Fr(1, 7), Fr(5, 6), Fr(0), Fr(12, 13))):
        for (k1, k2) in ((Fr(1), Fr(0)), (Fr(0), Fr(1)), (Fr(2), Fr(5))):
            mix, Bs, hp, hq = twod_mixed((Fr(1), Fr(1)), cp, cq, rp, rq, k1, k2)
            zp = (hp[1] - hp[0]) / (hp[1] + hp[0])
            zq = (hq[1] - hq[0]) / (hq[1] + hq[0])
            d = (k2 - k1) / 2
            f23 = -d * zp * zq * (zp + zq) / (1 + zp * zq)
            bp, bq = 2 * rp / (1 + rp * rp), 2 * rq / (1 + rq * rq)
            ok = ok and mix == f23 and zp <= bp and zq <= bq
            ok = ok and abs(mix) <= abs(d) * bp * bq * (bp + bq)
            rows.append({"r": [fstr(rp), fstr(rq)], "cos": [fstr(cp), fstr(cq)],
                         "k": [fstr(k1), fstr(k2)], "mixed": fstr(mix)})
    res["C1_formula_23_exact"] = check("C:formula23", ok)
    res["C1_rows"] = rows
    res["C1_note"] = "z_j <= beta_j, hence |M| <= |d| beta_p beta_q (beta_p + beta_q): third order"
    # C2: actual weights r_j = j^{-1/2}, t = pi/log 2
    t = math.pi / math.log(2)
    r2, r3 = 2 ** -0.5, 3 ** -0.5
    c2, c3 = math.cos(t * math.log(2)), math.cos(t * math.log(3))

    def zf(r, cs):
        h1, h2 = (1 - r) ** 2, 1 + r * r - 2 * r * cs
        return (h2 - h1) / (h2 + h1)
    z2, z3 = zf(r2, c2), zf(r3, c3)
    g = z2 * z3 * (z2 + z3) / (1 + z2 * z3)
    res["C2_actual_weights"] = {
        "t": t, "cos_t_log2": c2, "cos_t_log3": c3, "z2": z2, "z3": z3,
        "mixed_for_k=(1,0)": g / 2, "mixed_for_k=(0,1)": -g / 2,
        "either_sign": check("C:actual_weights_sign", z2 > 0 and z3 > 0 and g > 0),
        "log3_over_log2": math.log(3) / math.log(2),
    }
    # C3: second order. Balanced v=(1,1): M/(beta_p beta_q) -> 0.
    # Tilted v=(3/5,4/5): M/(beta_p beta_q) -> mu_2 with
    # mu_2 = -c^2 s^2 (s^2-c^2) (1-cos_p)(1-cos_q)(k2-k1).
    cp, cq = Fr(-1), Fr(7, 25)
    scan = []
    okC3 = True
    for (v, cc, ss) in (((Fr(1), Fr(1)), Fr(1), Fr(1)), ((Fr(3, 5), Fr(4, 5)), Fr(3, 5), Fr(4, 5))):
        nv = v[0] ** 2 + v[1] ** 2
        for (k1, k2) in ((Fr(1), Fr(0)), (Fr(0), Fr(1))):
            mu2 = -(cc * cc * ss * ss / nv ** 2) * ((ss * ss - cc * cc) / nv) \
                * (1 - cp) * (1 - cq) * (k2 - k1)
            seq = []
            for e in (10, 100, 1000, 10000):
                rp, rq = Fr(1, e), Fr(2, 3 * e)
                bp, bq = 2 * rp / (1 + rp * rp), 2 * rq / (1 + rq * rq)
                mix, _, _, _ = twod_mixed(v, cp, cq, rp, rq, k1, k2)
                ratio = mix / (bp * bq)
                seq.append({"r_p": fstr(rp), "ratio": float(ratio),
                            "ratio_minus_mu2": float(ratio - mu2)})
            # error must shrink by about a factor 10 per decade (first order in r)
            errs = [abs(s["ratio_minus_mu2"]) for s in seq]
            okC3 = okC3 and errs[-1] < errs[0] / 500
            scan.append({"v": [fstr(v[0]), fstr(v[1])], "k": [fstr(k1), fstr(k2)],
                         "mu2": fstr(mu2), "mu2_float": float(mu2), "scan": seq})
    res["C3_second_order"] = scan
    res["C3_converges"] = check("C:second_order", okC3)
    res["C3_note"] = ("balanced projection: mu_2 = 0 (third order); tilted projection: "
                      "mu_2 = -(c s)^2 (s^2-c^2)(1-cos_p)(1-cos_q)(k2-k1) for unit v=(c,s)")
    return res


# --------------------------------------------------------------------------
# D. the boundary resolvent identity and bound
# --------------------------------------------------------------------------
def sym_eigs(A, tol=1e-14, sweeps=100):
    """Jacobi eigenvalues of a real symmetric matrix (floating)."""
    n = len(A)
    a = [[float(x) for x in r] for r in A]
    for _ in range(sweeps):
        off = sum(a[i][j] ** 2 for i in range(n) for j in range(n) if i != j)
        if off < tol ** 2:
            break
        for p in range(n):
            for q in range(p + 1, n):
                if abs(a[p][q]) < 1e-300:
                    continue
                th = (a[q][q] - a[p][p]) / (2 * a[p][q])
                t = (1 if th >= 0 else -1) / (abs(th) + math.sqrt(th * th + 1))
                c = 1 / math.sqrt(t * t + 1)
                s = t * c
                for k in range(n):
                    akp, akq = a[k][p], a[k][q]
                    a[k][p], a[k][q] = c * akp - s * akq, s * akp + c * akq
                for k in range(n):
                    apk, aqk = a[p][k], a[q][k]
                    a[p][k], a[q][k] = c * apk - s * aqk, s * apk + c * aqk
    return sorted(a[i][i] for i in range(n))


def opnorm(A):
    return math.sqrt(max(0.0, sym_eigs(mm(tp(A), A))[-1]))


def section_D():
    res = {"instances": []}
    insts = [
        ([[1, 0, 2], [0, 1, 1], [2, -1, 0], [1, 1, 1], [0, 2, -1], [-1, 0, 1]],
         [[Fr(1, 1000), 0, Fr(-1, 2000)], [0, Fr(-1, 1500), 0], [Fr(-1, 2000), 0, Fr(1, 3000)]]),
        ([[3, 1, 0], [1, 0, 2], [0, 2, 1], [2, -1, 1], [1, 1, -2], [0, 3, 1]],
         [[0, Fr(1, 700), 0], [Fr(1, 700), 0, Fr(1, 900)], [0, Fr(1, 900), Fr(-1, 800)]]),
        # small gap: chi-components of one column are small
        ([[Fr(1, 40), 0, 0], [0, 1, 0], [0, 0, 1], [1, 0, 0], [0, 1, 1], [0, 1, -1]],
         [[Fr(1, 100000), 0, 0], [0, Fr(1, 100000), 0], [0, 0, Fr(-1, 100000)]]),
    ]
    ok_all = True
    for X, Delta in insts:
        Xf = [[Fr(v) for v in r] for r in X]
        Q, _ = proj_onto(Xf)
        F = msub(eye(6), msc(Fr(2), Q))
        C = [r[:3] for r in F[:3]]
        T = [r[3:] for r in F[:3]]
        I3 = eye(3)
        inv_ok = meq(mm(F, F), eye(6)) and meq(F, tp(F))
        tt_ok = meq(madd(mm(C, C), mm(T, tp(T))), I3)
        A = msub(I3, mm(C, C))
        Ai = minv(A)
        Y = mm(C, Ai, T)
        CN = madd(C, [[Fr(x) for x in r] for r in Delta])
        AN = msub(I3, mm(CN, CN))
        YN = mm(CN, minv(AN), T)
        rhs = madd(mm(msub(C, CN), Ai, T),
                   mm(CN, minv(AN), msub(mm(C, C), mm(CN, CN)), Ai, T))
        id_ok = meq(msub(Y, YN), rhs)
        AiT = mm(Ai, T)
        gram_ok = meq(mm(AiT, tp(AiT)), Ai)
        eps = opnorm(msub(C, CN))
        c, cN = opnorm(C), opnorm(CN)
        g = sym_eigs(A)[0]
        lhs = opnorm(msub(Y, YN))
        bound = eps * (1 + c * cN) / ((1 - cN ** 2) * math.sqrt(g))
        ok = inv_ok and tt_ok and id_ok and gram_ok and lhs <= bound * (1 + 1e-9)
        ok_all = ok_all and ok
        res["instances"].append({
            "involution_symmetric": inv_ok, "C2_plus_TTt_is_I": tt_ok,
            "resolvent_identity_exact": id_ok, "AinvT_gram_equals_Ainv": gram_ok,
            "eps": eps, "c": c, "c_N": cN, "gap_g": g,
            "norm_Y_minus_YN": lhs, "bound_21": bound,
            "bound_over_actual": bound / lhs if lhs else None,
            "amplification_bound_over_eps": bound / eps,
        })
    res["all_ok"] = check("D:resolvent", ok_all)
    return res


# --------------------------------------------------------------------------
# E. boundary-to-source kernel identity in exact Gaussian-rational arithmetic
# --------------------------------------------------------------------------
class CQ:
    __slots__ = ("re", "im")

    def __init__(self, re=0, im=0):
        self.re, self.im = Fr(re), Fr(im)

    def __add__(self, o):
        return CQ(self.re + o.re, self.im + o.im)

    def __sub__(self, o):
        return CQ(self.re - o.re, self.im - o.im)

    def __mul__(self, o):
        if isinstance(o, CQ):
            return CQ(self.re * o.re - self.im * o.im, self.re * o.im + self.im * o.re)
        return CQ(self.re * o, self.im * o)

    def conj(self):
        return CQ(self.re, -self.im)

    def __eq__(self, o):
        return self.re == o.re and self.im == o.im

    def j(self):
        return [str(self.re), str(self.im)]


Z0 = CQ(0)


def padd(p, q):
    n = max(len(p), len(q))
    return [(p[i] if i < len(p) else Z0) + (q[i] if i < len(q) else Z0) for i in range(n)]


def pmul(p, q):
    r = [Z0] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            r[i + j] = r[i + j] + a * b
    return r


def pscale(p, c):
    return [a * c for a in p]


def ppow_lin(alpha, beta, n):
    # (alpha s + beta)^n as a polynomial in s (alpha, beta rational)
    return [CQ(Fr(math.comb(n, m)) * Fr(alpha) ** m * Fr(beta) ** (n - m)) for m in range(n + 1)]


def pint(p, a, b):
    # integral from a to b (rationals)
    s = Z0
    for k, c in enumerate(p):
        s = s + c * ((Fr(b) ** (k + 1) - Fr(a) ** (k + 1)) / (k + 1))
    return s


def preal(p):
    return [CQ(c.re) for c in p]


def kappa_pieces(f):
    """kappa_F(s)=int conj(F(x))F(x+s)dx for F=sum f_i x^i on (-1/2,1/2).
    Returns polynomials kp (valid for s in [0,1]) and km (valid for s in [-1,0])."""
    half = Fr(1, 2)
    kp, km = [Z0], [Z0]
    for i, fi in enumerate(f):
        for jj, fj in enumerate(f):
            coef = fi.conj() * fj
            for l in range(jj + 1):
                # conj f_i f_j C(j,l) x^{i+l} s^{j-l}
                n, m = i + l, jj - l
                c = coef * Fr(math.comb(jj, l))
                # s>=0: int_{-1/2}^{1/2-s} x^n dx
                up = ppow_lin(-1, half, n + 1)
                lo = [CQ((-half) ** (n + 1))]
                piece = pscale(padd(up, pscale(lo, CQ(-1))), CQ(Fr(1, n + 1)))
                kp = padd(kp, pscale([Z0] * m + piece, c))
                # s<=0: int_{-1/2-s}^{1/2} x^n dx
                up2 = [CQ(half ** (n + 1))]
                lo2 = ppow_lin(-1, -half, n + 1)
                piece2 = pscale(padd(up2, pscale(lo2, CQ(-1))), CQ(Fr(1, n + 1)))
                km = padd(km, pscale([Z0] * m + piece2, c))
    return kp, km


def biv_int_triangle(poly_x, poly_z, rho):
    """int_{x,z>0,x+z<1} poly_x(x) poly_z(z) rho(x+z) dx dz, rho real poly."""
    tot = Z0
    for a, ua in enumerate(poly_x):
        for b, vb in enumerate(poly_z):
            for m, rm in enumerate(rho):
                for l in range(m + 1):
                    val = Fr(math.comb(m, l)) * Fr(math.factorial(a + l) * math.factorial(b + m - l),
                                                   math.factorial(a + b + m + 2))
                    tot = tot + ua * vb * rm * val
    return tot


def conv_poly(u, v):
    # w(s) = int_0^s u(x) v(s-x) dx
    w = [Z0] * (len(u) + len(v) + 1)
    for a, ua in enumerate(u):
        for b, vb in enumerate(v):
            w[a + b + 1] = w[a + b + 1] + ua * vb * Fr(math.factorial(a) * math.factorial(b),
                                                       math.factorial(a + b + 1))
    return w


def source_form(f, rw):
    """<F, H F> = int int conj(F(x)) k(y-x) F(y) dy dx on (-1/2,1/2)^2 with
    k(u) = rw(|u|), rw a real polynomial."""
    half = Fr(1, 2)
    tot = Z0
    # region y > x: k = rw(y - x); region y < x: k = rw(x - y)
    for sign in (1, -1):
        # build bivariate coefficients of rw(sign*(y-x)) F(y): {(px, py): c}
        biv = {}
        for m, rm in enumerate(rw):
            for l in range(m + 1):
                # (sign(y-x))^m = sign^m sum_l C(m,l) y^l (-x)^{m-l}
                c0 = rm * (Fr(math.comb(m, l)) * Fr(sign) ** m * Fr(-1) ** (m - l))
                for bidx, fb in enumerate(f):
                    key = (m - l, l + bidx)
                    biv[key] = biv.get(key, Z0) + c0 * fb
        # integrate in y: sign=+1 over (x, 1/2); sign=-1 over (-1/2, x)
        inner = [Z0]
        for (px, py), c in biv.items():
            if sign == 1:
                pol = padd([CQ(half ** (py + 1))], pscale([Z0] * (py + 1) + [CQ(1)], CQ(-1)))
            else:
                pol = padd([Z0] * (py + 1) + [CQ(1)], [CQ(-((-half) ** (py + 1)))])
            pol = pscale(pol, CQ(Fr(1, py + 1)))
            inner = padd(inner, pscale([Z0] * px + pol, c))
        fbar = [c.conj() for c in f]
        tot = tot + pint(pmul(fbar, inner), -half, half)
    return tot


def section_E():
    res = {}
    f = [CQ(1, 1), CQ(2, -1), CQ(-3, 2), CQ(1, 0)]          # complex cubic source on (-1/2,1/2)
    u = [[CQ(1), CQ(2)], [CQ(0), CQ(0), CQ(0, 1)]]           # u_j on (0,1)
    v = [[CQ(3), CQ(-1), CQ(0, 1)], [CQ(1, -1), CQ(2)]]      # v_j(z) = v'_j(-z) on (0,1)
    kp, km = kappa_pieces(f)
    # independent consistency: kappa(-s) = conj(kappa(s))
    km_from_kp = [CQ(c.re * (-1) ** i, -c.im * (-1) ** i) for i, c in enumerate(kp)]
    L = max(len(km), len(km_from_kp))
    km_p = km + [Z0] * (L - len(km))
    km_q = km_from_kp + [Z0] * (L - len(km_from_kp))
    res["kappa_reflection_exact"] = check("E:kappa_reflection", all(a == b for a, b in zip(km_p, km_q)))
    rho = preal(kp)                                         # Re kappa on [0,1]
    tr = Z0
    for uj, vj in zip(u, v):
        tr = tr + biv_int_triangle([c.conj() for c in uj], vj, rho)
    lhs = CQ(2 * tr.re)                                     # 2 Re Tr(Y_N X_{F,e})
    w = [Z0]
    for uj, vj in zip(u, v):
        w = padd(w, conv_poly([c.conj() for c in uj], vj))
    rw = preal(w)                                           # k_N(s) = Re w_N(|s|)
    rhs1 = pint(pmul(kp, rw), 0, 1) + pint(pmul(km, [c * (Fr(-1) ** i) for i, c in enumerate(rw)]), -1, 0)
    rhs2 = source_form(f, rw)
    res["LHS_2ReTr"] = lhs.j()
    res["RHS_int_kappa_k"] = rhs1.j()
    res["RHS_source_operator"] = rhs2.j()
    res["identity_18_exact"] = check("E:identity18", lhs == rhs1 and rhs1 == rhs2 and rhs1.im == 0)
    # negative controls: no factor two; wrong orientation (no reflection of v)
    wrong_factor = CQ(tr.re)
    v_unreflected = [[c * (Fr(-1) ** i) for i, c in enumerate(vj)] for vj in v]
    tr2 = Z0
    for uj, vj in zip(u, v_unreflected):
        tr2 = tr2 + biv_int_triangle([c.conj() for c in uj], vj, rho)
    res["neg_missing_factor_two_differs"] = check("E:neg_factor", not (wrong_factor == rhs1))
    res["neg_unreflected_output_differs"] = check("E:neg_orientation", not (CQ(2 * tr2.re) == rhs1))
    res["float_value"] = float(lhs.re)
    return res


# --------------------------------------------------------------------------
# F. gamma-sector asymptotics (floating)
# --------------------------------------------------------------------------
_B2K = [Fr(1, 6), Fr(-1, 30), Fr(1, 42), Fr(-1, 30), Fr(5, 66), Fr(-691, 2730),
        Fr(7, 6), Fr(-3617, 510), Fr(43867, 798)]


def digamma(z):
    acc = 0j
    while abs(z) < 24:
        acc -= 1 / z
        z += 1
    s = cmath.log(z) - 1 / (2 * z)
    zz = z * z
    zp = zz
    for k, b in enumerate(_B2K, start=1):
        s -= float(b) / (2 * k * zp)
        zp *= zz
    return acc + s


def gamma_inf(t):
    return digamma(0.25 + 0.5j * t).real - math.log(math.pi)


def gauss_legendre(n):
    xs, ws = [], []
    for i in range(1, n + 1):
        z = math.cos(math.pi * (i - 0.25) / (n + 0.5))
        for _ in range(100):
            p1, p2 = 1.0, 0.0
            for j in range(1, n + 1):
                p3, p2 = p2, p1
                p1 = ((2 * j - 1) * z * p2 - (j - 1) * p3) / j
            pp = n * (z * p1 - p2) / (z * z - 1)
            z1, z = z, z - p1 / pp
            if abs(z - z1) < 1e-16:
                break
        xs.append(z)
        ws.append(2 / ((1 - z * z) * pp * pp))
    return xs, ws


def bspline_M(m, x):
    # cardinal B-spline of order m on [0, m] by the stable recursion
    if m == 1:
        return 1.0 if 0 <= x < 1 else 0.0
    if x <= 0 or x >= m:
        return 0.0
    return (x * bspline_M(m - 1, x) + (m - x) * bspline_M(m - 1, x - 1)) / (m - 1)


class Bump:
    """h = sum of copies of the centered order-n box spline of width n*w at the
    given centers. Fourier transform hhat(s) = (w sinc(sw/2))^n sum_c e^{-isc}."""

    def __init__(self, n, w, centers):
        self.n, self.w, self.centers = n, w, centers

    def hhat2(self, s):
        x = s * self.w / 2
        sinc = 1.0 if x == 0 else math.sin(x) / x
        base = (self.w * sinc) ** self.n
        re = sum(math.cos(s * c) for c in self.centers)
        im = -sum(math.sin(s * c) for c in self.centers)
        return base * base * (re * re + im * im)

    def kappa_single(self, a):
        m = 2 * self.n
        return self.w ** (m - 1) * bspline_M(m, a / self.w + self.n)

    def kappa(self, a):
        return sum(self.kappa_single(a - (c1 - c2)) for c1 in self.centers for c2 in self.centers)

    def diameter(self):
        return (max(self.centers) - min(self.centers)) + self.n * self.w


def gamma_forms(bump, tau, shifts, S, panel=1.0, order=16):
    """Re Gamma(F_tau, U_a F_tau) for the shifts, and ||F_tau||^2, with
    hat F_tau(t) = tau^{-2} (t^2+1/4) hhat(t - tau)."""
    xs, ws = gauss_legendre(order)
    npan = int(round(2 * S / panel))
    acc = [0.0] * len(shifts)
    norm = 0.0
    for k in range(npan):
        lo = -S + k * panel
        for x, wq in zip(xs, ws):
            s = lo + (x + 1) * panel / 2
            t = tau + s
            wgt = wq * panel / 2
            amp = bump.hhat2(s) * ((t * t + 0.25) / (tau * tau)) ** 2 / (2 * math.pi)
            norm += wgt * amp
            g = gamma_inf(t) * amp * wgt
            for i, a in enumerate(shifts):
                acc[i] += g * math.cos(t * a)
    return acc, norm


def tail_majorant(bump, tau, S):
    # crude majorant of the omitted |s|>S part: |hhat|^2 <= (2/|s|)^{2n} (#centers)^2,
    # |gamma_inf(t)| <= log(2+|t|) + 6 for all real t (gamma_inf(0) = -5.37...),
    # and |t| <= tau + |s| in both the polynomial and the logarithmic factor
    xs, ws = gauss_legendre(24)
    tot = 0.0
    lo, hi = math.log(S), math.log(S) + 40
    npan = 40
    for k in range(npan):
        a = lo + k * (hi - lo) / npan
        b = a + (hi - lo) / npan
        for x, wq in zip(xs, ws):
            u = a + (x + 1) * (b - a) / 2
            s = math.exp(u)
            t = tau + s
            val = (len(bump.centers) ** 2) * (2 / s) ** (2 * bump.n) * \
                ((t * t + 0.25) / tau ** 2) ** 2 * (math.log(2 + t) + 6) / (2 * math.pi)
            tot += wq * (b - a) / 2 * val * s
    return 2 * tot


def section_F(quick=False):
    res = {}
    a_minus, a_plus, log2 = math.log(1.5), math.log(6.0), math.log(2.0)
    b2, b3 = 2 * 2 ** -0.5 / 1.5, 2 * 3 ** -0.5 / (4 / 3)
    res["gamma_inf_0"] = gamma_inf(0.0)
    res["gamma_inf_0_closed_form"] = -0.5772156649015329 - math.pi / 2 - 3 * math.log(2) - math.log(math.pi)
    check("F:gamma0", abs(res["gamma_inf_0"] - res["gamma_inf_0_closed_form"]) < 1e-12)
    # two bumps at +-a_minus/2, each of width 1/2: diameter a_minus + 1/2 in (a_minus, min(L, a_plus))
    n, width = 6, 0.5
    bump = Bump(n, width / n, [-a_minus / 2, a_minus / 2])
    k0, km, kplus, k2 = bump.kappa(0.0), bump.kappa(a_minus), bump.kappa(a_plus), bump.kappa(log2)
    res["bump"] = {"order": n, "box": width / n, "centers": bump.centers,
                   "diameter": bump.diameter(), "L": 1.2,
                   "kappa0": k0, "kappa_a_minus": km, "kappa_a_plus": kplus, "kappa_log2": k2}
    check("F:bump_geometry", a_minus < bump.diameter() < min(1.2, a_plus) and kplus == 0.0
          and km > 0 and k2 > 0)
    ch = (b2 * b3 / 2) * km / k0            # normalized by ||h||^2
    res["c_h_over_norm"] = ch
    res["beta2_beta3_over_2"] = b2 * b3 / 2
    # quadrature check of kappa(a) = int |hhat|^2 cos(sa) ds/2pi
    xs, ws = gauss_legendre(16)
    qk = []
    for a in (0.0, a_minus, log2):
        S, panel = 3000.0, 1.0
        acc = 0.0
        for kk in range(int(2 * S / panel)):
            lo = -S + kk * panel
            for x, wq in zip(xs, ws):
                s = lo + (x + 1) * panel / 2
                acc += wq * panel / 2 * bump.hhat2(s) * math.cos(s * a) / (2 * math.pi)
        qk.append(acc)
    res["kappa_by_quadrature"] = qk
    res["kappa_by_spline"] = [k0, km, k2]
    check("F:kappa_quadrature", all(abs(p - q) < 1e-9 * k0 for p, q in zip(qk, (k0, km, k2))))
    targets = [1e3, 1e4, 1e5] if quick else [1e3, 3e3, 1e4, 3e4, 1e5]
    lt = lambda tau: math.log(tau) - math.log(2 * math.pi)
    rows = []
    for T in targets:
        nn = max(1, round(T * a_minus / (2 * math.pi)))
        for kind, tau in (("cos=+1", 2 * math.pi * nn / a_minus),
                          ("cos=-1", (2 * nn + 1) * math.pi / a_minus)):
            S = 3000.0
            (g0, g_plus, g_minus), nrm = gamma_forms(bump, tau, (0.0, a_plus, a_minus), S)
            G = (b2 * b3 / 2) * (g_plus + g_minus) / k0
            pred = ch * lt(tau) * math.cos(tau * a_minus)
            rows.append({
                "tau": tau, "kind": kind, "norm_ratio": nrm / k0,
                "Gamma_diag_minus_log": g0 / k0 - lt(tau),
                "G_Gamma": G, "predicted": pred, "difference": G - pred,
                "a_plus_part": (b2 * b3 / 2) * g_plus / k0,
                "tail_majorant": tail_majorant(bump, tau, S) / k0,
            })
    res["rows"] = rows
    diffs = [abs(r["difference"]) for r in rows]
    check("F:asymptotic_mixed", diffs[-1] < 1e-4 and diffs[-1] < diffs[0])
    check("F:diagonal_log", abs(rows[-1]["Gamma_diag_minus_log"]) < 1e-4)
    # one-prime analogue: bumps at +-log(2)/2 of width 0.4 (diameter log 2 + 0.4 < 6/5)
    bump1 = Bump(6, 0.4 / 6, [-log2 / 2, log2 / 2])
    q0, q2 = bump1.kappa(0.0), bump1.kappa(log2)
    res["bump_one_prime"] = {"centers": bump1.centers, "diameter": bump1.diameter(),
                             "kappa_log2_over_kappa0": q2 / q0}
    check("F:bump1_geometry", log2 < bump1.diameter() < 1.2)
    rows1 = []
    for T in targets:
        nn = max(1, round(T * log2 / (2 * math.pi)))
        for kind, tau in (("cos=+1", 2 * math.pi * nn / log2),
                          ("cos=-1", (2 * nn + 1) * math.pi / log2)):
            (g2,), _ = gamma_forms(bump1, tau, (log2,), 3000.0)
            src = -b2 * g2 / q0          # Gamma part of B_S[J_2 F] - B_S[F]
            pred1 = -b2 * (q2 / q0) * math.cos(tau * log2) * lt(tau)
            rows1.append({"tau": tau, "kind": kind, "source_transport_gamma_part": src,
                          "predicted": pred1, "difference": src - pred1})
    res["one_prime_rows"] = rows1
    d1 = [abs(r["difference"]) for r in rows1]
    check("F:asymptotic_one_prime", d1[-1] < 1e-4 and d1[-1] < d1[0])
    # inaccessible shifts: one bump of width 0.3 < a_minus
    small = Bump(6, 0.05, [0.0])
    srows = []
    for T in ([1e3, 1e5] if quick else [1e3, 1e4, 1e5]):
        nn = max(1, round(T * a_minus / (2 * math.pi)))
        tau = 2 * math.pi * nn / a_minus
        (gp, gm), nrm = gamma_forms(small, tau, (a_plus, a_minus), 6000.0)
        srows.append({"tau": tau, "G_Gamma": (b2 * b3 / 2) * (gp + gm) / small.kappa(0.0),
                      "kappa_a_minus": small.kappa(a_minus)})
    res["inaccessible"] = {"diameter": small.diameter(), "rows": srows}
    return res


# --------------------------------------------------------------------------
# G. constants
# --------------------------------------------------------------------------
def primes_upto(N):
    sieve = bytearray([1]) * (N + 1)
    sieve[0:2] = b"\x00\x00"
    for i in range(2, int(N ** 0.5) + 1):
        if sieve[i]:
            sieve[i * i::i] = bytearray(len(sieve[i * i::i]))
    return [i for i in range(N + 1) if sieve[i]]


def section_G():
    res = {}
    # exact first-pair coefficient: (beta2 beta3 / 2)^2 = 1/6, i.e. sqrt(6)/6
    b2sq, b3sq = Fr(8, 9), Fr(3, 4)          # beta_2 = 2 sqrt2 / 3, beta_3 = sqrt3 / 2
    res["(beta2*beta3/2)^2"] = fstr(b2sq * b3sq / 4)
    check("G:coef", b2sq * b3sq / 4 == Fr(1, 6))
    # eigenvalue of W at (2,3): beta2 beta3/(2 sqrt2); square = beta2^2 beta3^2 / 8 = 1/12
    res["eig_W_squared"] = fstr(b2sq * b3sq / 8)
    check("G:eig", b2sq * b3sq / 8 == Fr(1, 12))
    a_m, a_p, L = math.log(1.5), math.log(6), 1.2
    res["a_minus"], res["a_plus"] = a_m, a_p
    res["active_primes_at_L=6/5"] = [p for p in (2, 3, 5) if math.log(p) < L]
    check("G:window", a_m < L < a_p and res["active_primes_at_L=6/5"] == [2, 3])
    # inherited archimedean gap 1-||C_inf||^2 >= 57/10^6 (closed-source note, Section 2)
    gap0 = 57e-6
    sets = {"{}": [], "{2}": [2], "{3}": [3], "{2,3}": [2, 3]}
    corners = {}
    for name, A in sets.items():
        lu = 1.0
        for p in A:
            r = p ** -0.5
            lu *= ((1 - r) / (1 + r)) ** 2
        g = lu * gap0
        c = math.sqrt(1 - g)
        corners[name] = {"(l/u)^2": lu, "g": g, "c_over_sqrt_g": c / math.sqrt(g),
                         "amplification_21": (1 + c * c) / ((1 - c * c) * math.sqrt(g))}
    res["corners"] = corners
    res["closed_source_check_L1_S2"] = 1.0 * corners["{2}"]["c_over_sqrt_g"]
    check("G:closed_source_772", abs(corners["{2}"]["c_over_sqrt_g"] - 771.9933840785) < 1e-6)
    ymix = sum(v["c_over_sqrt_g"] for v in corners.values())
    res["Ymix_norm_bound"] = ymix
    res["apriori_16_at_L=6/5"] = L * ymix
    # generic a priori bound from (10), relative to B_S
    def Cb(p, q):
        bp, bq = 2 * p ** -0.5 / (1 + 1 / p), 2 * q ** -0.5 / (1 + 1 / q)
        C = 2 * bp * bq / ((1 - bp) * (1 - bq)) * (1 + (1 + bp) / (1 - bp) + (1 + bq) / (1 - bq))
        return C, 6 * bp * bq
    res["apriori_relative_bound"] = {f"{p},{q}": {"bound_over_B_S": Cb(p, q)[0],
                                                  "6_beta_p_beta_q": Cb(p, q)[1]}
                                     for p, q in ((2, 3), (101, 103), (10007, 10009))}
    # condition growth along S_L = {p <= e^L}: log(u/l) and (u/l)^2
    ps = primes_upto(int(math.exp(12)) + 1)
    growth = []
    for Lv in (1, 2, 4, 6, 8, 10, 12):
        lg = sum(math.log((1 + p ** -0.5) / (1 - p ** -0.5)) for p in ps if p <= math.exp(Lv))
        growth.append({"L": Lv, "num_primes": sum(1 for p in ps if p <= math.exp(Lv)),
                       "log_u_over_l": lg, "log10_condition_(u/l)^2": 2 * lg / math.log(10)})
    res["condition_growth"] = growth
    res["certified_Q_margin_L=6/5_quoted"] = "Q >= (3/2000)||F||^2 (result-summaries/07), not recomputed"
    return res


# --------------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--output", required=True)
    ap.add_argument("--repo-root", default=None)
    ap.add_argument("--sections", default="ABCDEFG")
    ap.add_argument("--quick", action="store_true", help="fewer tau values in section F")
    args = ap.parse_args()
    root = args.repo_root
    if root is None:
        cand = Path(__file__).resolve().parents[6]
        if (cand / PROJECT).is_dir():
            root = str(cand)
    t0 = time.time()
    rec = {
        "schema": SCHEMA, "date": "2026-10-17", "prepared_for": "Edward Baker",
        "model": "Claude Opus 5.5 (configured identifier claude-opus-5-5)",
        "reasoning_effort": "max",
        "status": "B-E exact rational (D norms floating); F-G floating diagnostics",
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "python": platform.python_version(),
    }
    fns = {"A": lambda: section_A(root), "B": section_B, "C": section_C, "D": section_D,
           "E": section_E, "F": lambda: section_F(args.quick), "G": section_G}
    for s in args.sections:
        rec[s] = fns[s]()
    rec["failures"] = FAILURES
    rec["all_checks_passed"] = not FAILURES
    rec["runtime_seconds"] = round(time.time() - t0, 1)
    Path(args.output).write_text(json.dumps(rec, indent=1, sort_keys=False) + "\n")
    print(json.dumps({"failures": FAILURES, "runtime_seconds": rec["runtime_seconds"]}))
    sys.exit(1 if FAILURES else 0)


if __name__ == "__main__":
    main()
