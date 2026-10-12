#!/usr/bin/env python3
"""Independent interval re-verification of the Dini y-transfer gate of the
pinned Gomila package, with an explicit margin.  Standard-library Python.

Audited package: judegomila/dbn-lambda-01787854-candidate-audit at commit
a74738deb6d5e0f76887cb36901da08b68dca705, theorem
provenance/TRIANGLE_Y_DINI_THEOREM.independent.md, verifier
verifiers/verify_triangle_y_dini_arb.c (logs/triangle_y_dini_{180,256}.log).

The theorem reduces monotonicity in y of the direct Triangle mass to the gate,
for every Euler prime set P of the finite legs, every gcd pattern G0 | D, every
ratio sector d_{j-1} < n/N <= d_j (active set S = {d | G0 : d >= d_j}), every
L = log n in the sector and every y in [y0, sqrt(1 - 2 t0)]:

    h <= 0   or   G h < (L/2) |C0|,                                     (gate)

    r_d(L) = exp((t/4)(sum_{p|d} log^2 p + log^2 d - 2 L log d)),  s_d = (-1)^omega(d),
    C0 = sum_S s_d r_d,   C = sum_S s_d r_d d^-y,   LC + C' = sum_S s_d (L - log d) r_d d^-y,
    h  = |LC + C'| + (g - L/2) |C|,     G = exp(y (L + g)),
    g  = 1/50 - (1/2) log q,  q = max(N_min^2, e^{2L}/d_j^2) - t/16  (a lower bound for q_N).

The package's C program certifies the gate on 297,490 + 52,239 + 9,290 + 237
rectangles and reports a largest certified ratio upper bound
0.99999860767275095 (P = {2,3,5,7,11}).  That number is the largest interval
upper bound among the leaves its bisection accepted, and the bisection stops
as soon as a leaf's bound drops below 1; it is therefore a property of the
stopping rule, not the supremum of the ratio.  This programme re-verifies the
same gate on the same (L, y) domain with a stricter acceptance threshold
THETA < 1, i.e. it certifies

    h <= 0   or   G h <= THETA (L/2) |C0|    everywhere on the covered domain,

so that sup (G h_+)/((L/2)|C0|) <= THETA (THETA = 0 demands h <= 0 everywhere).

Interval arithmetic: decimal at PREC digits with ROUND_FLOOR/ROUND_CEILING
for +,-,*,/ and correctly rounded exp/ln/sqrt (ROUND_HALF_EVEN, documented)
padded by a relative 10^-(PREC-2), i.e. 20 half-ulps.  Monotonicity gives
tight enclosures: each term s_d r_d(L) d^-y is decreasing in L and in y, so
its range on a rectangle is spanned by its values at two opposite corners;
g - L/2 is decreasing in L on both branches; L + g is increasing (low
branch) or decreasing (high branch).  The domain is the package's: L in
[log 2, log(N_max d_j)] for j = 0 and [log(N_min d_{j-1}), log(N_max d_j)]
for j > 0 (log endpoints rounded outward), split at log(N_min d_j) into the
two q-branches; it contains log n for every n active in the sector at some
N of the leg, and many unphysical L.

What this checks: the gate inequality on the covered domain.  It does not
re-derive the Dini reduction itself (reviewed separately in the audit notes),
nor the normalizer and kappa-correction monotonicity.

Prepared for Edward Baker with LLM assistance (Claude Opus 5.5,
claude-opus-5-5), 12 October 2026.  Internal check, not independent review.

Usage:
    python3 check_dini_gate_margin.py --theta 3/4,3/4,1/4,0 --negative-control --output rec.json
(the retained record was produced by exactly this command; about 5 minutes).
The per-leg thresholds are those of the retained record: sup <= 3/4 for
{2,3,5,7,11} and {2,3,5,7}, <= 1/4 for {2,3,5}, and h <= 0 everywhere for {2,3}.
"""
import argparse
import decimal
import hashlib
import itertools
import json
import math
import platform
import sys
import time
from decimal import Context, Decimal as Dc, ROUND_CEILING, ROUND_FLOOR, ROUND_HALF_EVEN
from fractions import Fraction

PREC = 30
CN = Context(prec=PREC, rounding=ROUND_HALF_EVEN)
CF = Context(prec=PREC, rounding=ROUND_FLOOR)
CC = Context(prec=PREC, rounding=ROUND_CEILING)
decimal.setcontext(Context(prec=PREC, rounding=ROUND_HALF_EVEN))
ETA = Dc(10) ** (-(PREC - 2))
T = Dc("0.16125")                 # t0 = 129/800
Y0SQ = Dc("0.0350708")            # 87677/2500000
YMAXSQ = Dc("0.6775")             # 1 - 2 t0 = 271/400
LEGS = [((2, 3, 5, 7, 11), 690988, 728999), ((2, 3, 5, 7), 729000, 818999),
        ((2, 3, 5), 819000, 1027999), ((2, 3), 1028000, 3840000)]
PACKAGE = {"repository": "https://github.com/judegomila/dbn-lambda-01787854-candidate-audit",
           "commit": "a74738deb6d5e0f76887cb36901da08b68dca705"}
PACKAGE_RATIO_UB = {"235711": "0.99999860767275095", "2357": "0.99997108988463879",
                    "235": "0.99999531405046582", "23": "0.99224052112549543"}


def exp_lo(x):
    return CF.multiply(CN.exp(x), CF.subtract(1, ETA))


def exp_hi(x):
    return CC.multiply(CN.exp(x), CC.add(1, ETA))


def ln_lo(x):
    v = CN.ln(x)
    return CF.subtract(v, CC.multiply(ETA, max(Dc(1), v.copy_abs())))


def ln_hi(x):
    v = CN.ln(x)
    return CC.add(v, CC.multiply(ETA, max(Dc(1), v.copy_abs())))


def sqrt_lo(x):
    return CF.multiply(CN.sqrt(x), CF.subtract(1, ETA))


def sqrt_hi(x):
    return CC.multiply(CN.sqrt(x), CC.add(1, ETA))


def imul(a, b):
    """Product of intervals a=(lo,hi), b=(lo,hi)."""
    ps = [(x, y) for x in a for y in b]
    return (min(CF.multiply(x, y) for x, y in ps), max(CC.multiply(x, y) for x, y in ps))


def iadd(a, b):
    return (CF.add(a[0], b[0]), CC.add(a[1], b[1]))


def imag(a):
    return max(a[0].copy_abs(), a[1].copy_abs())


def imig(a):
    if a[0] > 0:
        return a[0]
    if a[1] < 0:
        return a[1].copy_abs()
    return Dc(0)


class Leg:
    def __init__(self, P, nlo, nhi):
        self.P, self.nlo, self.nhi = P, nlo, nhi
        self.lnp = {p: (ln_lo(Dc(p)), ln_hi(Dc(p))) for p in P}
        # t/2 * log p enclosures and exp((t/4)(sum log^2 p + log^2 d)) for every divisor
        self.half_t_lnp = {p: (CF.multiply(CN.divide(T, 2), self.lnp[p][0]),
                               CC.multiply(CN.divide(T, 2), self.lnp[p][1])) for p in P}
        self.alpha = {}
        for r in range(len(P) + 1):
            for c in itertools.combinations(P, r):
                s2lo = s2hi = ldlo = ldhi = Dc(0)
                for p in c:
                    s2lo = CF.add(s2lo, CF.multiply(self.lnp[p][0], self.lnp[p][0]))
                    s2hi = CC.add(s2hi, CC.multiply(self.lnp[p][1], self.lnp[p][1]))
                    ldlo = CF.add(ldlo, self.lnp[p][0])
                    ldhi = CC.add(ldhi, self.lnp[p][1])
                alo = CF.multiply(CN.divide(T, 4), CF.add(s2lo, CF.multiply(ldlo, ldlo)))
                ahi = CC.multiply(CN.divide(T, 4), CC.add(s2hi, CC.multiply(ldhi, ldhi)))
                self.alpha[c] = ((exp_lo(alo), exp_hi(ahi)), (ldlo, ldhi))
        # N_min^2 - t/16 is exact at PREC digits (at most 22 significant digits)
        self.qlow = CN.subtract(Dc(nlo * nlo), CN.divide(T, 16))
        assert Fraction(self.qlow) == Fraction(nlo * nlo) - Fraction(129, 12800)
        self.glow = (CF.subtract(Dc("0.02"), CC.divide(ln_hi(self.qlow), 2)),
                     CC.subtract(Dc("0.02"), CF.divide(ln_lo(self.qlow), 2)))


def g_high(L, rmax, lo_side):
    """g = 1/50 - (1/2) log(e^{2L}/rmax^2 - t/16), an enclosure endpoint at the point L."""
    if lo_side:     # lower bound of g needs upper bound of q
        q = CC.subtract(CC.divide(exp_hi(CC.multiply(2, L)), rmax * rmax), CN.divide(T, 16))
        return CF.subtract(Dc("0.02"), CC.divide(ln_hi(q), 2))
    q = CF.subtract(CF.divide(exp_lo(CF.multiply(2, L)), rmax * rmax), CN.divide(T, 16))
    return CC.subtract(Dc("0.02"), CF.divide(ln_lo(q), 2))


def evaluate(leg, active, rmax, low_branch, L1, L2, y1, y2, theta):
    """Return ('h', None) if h <= 0 certified, ('r', ratio_ub) if G h <= theta (L/2)|C0|
    certified with ratio_ub = upper bound of G h/((L/2)|C0|), or ('u', None) if undecided."""
    C0, C, LCC = enclosures(leg, active, L1, L2, y1, y2)
    # g and g - L/2 (both decreasing in L on both branches)
    if low_branch:
        g = leg.glow
    else:
        g = (g_high(L2, rmax, True), g_high(L1, rmax, False))
    gmL_hi = CC.subtract(g[1], CF.divide(L1, 2))       # max of g - L/2
    gmL_lo = CF.subtract(g[0], CC.divide(L2, 2))       # min of g - L/2
    assert gmL_hi < 0
    h_hi = CC.add(imag(LCC), CC.multiply(gmL_hi, imig(C)))
    if h_hi <= 0:
        return "h", None
    # L + g: increasing in L on the low branch, decreasing on the high branch
    if low_branch:
        Lg = (CF.add(L1, g[0]), CC.add(L2, g[1]))
    else:
        Lg = (CF.add(L2, g_high(L2, rmax, True)), CC.add(L1, g_high(L1, rmax, False)))
    yLg = imul((y1, y2), Lg)
    G_hi = exp_hi(yLg[1])
    num = CC.multiply(G_hi, h_hi)
    den = CF.multiply(CF.divide(L1, 2), imig(C0))
    if theta > 0 and den > 0 and num <= CF.multiply(theta, den):
        return "r", CC.divide(num, den)
    return "u", None


def enclosures(leg, active, L1, L2, y1, y2):
    """Enclosures of C0, C and LC + C' on [L1, L2] x [y1, y2] (termwise monotone)."""
    fL = {}
    fy = {}
    for p in leg.P:
        a = leg.half_t_lnp[p]
        fL[p] = (exp_lo(CC.multiply(a[1], L2).copy_negate()), exp_hi(CF.multiply(a[0], L1).copy_negate()))
        b = leg.lnp[p]
        fy[p] = (exp_lo(CC.multiply(b[1], y2).copy_negate()), exp_hi(CF.multiply(b[0], y1).copy_negate()))
    C0 = (Dc(0), Dc(0))
    C = (Dc(0), Dc(0))
    LCC = (Dc(0), Dc(0))
    for c in active:
        (ealo, eahi), (ldlo, ldhi) = leg.alpha[c]
        rlo, rhi = ealo, eahi
        for p in c:
            rlo = CF.multiply(rlo, fL[p][0])
            rhi = CC.multiply(rhi, fL[p][1])
        tlo, thi = rlo, rhi
        for p in c:
            tlo = CF.multiply(tlo, fy[p][0])
            thi = CC.multiply(thi, fy[p][1])
        m = imul((CF.subtract(L1, ldhi), CC.subtract(L2, ldlo)), (tlo, thi))
        if len(c) % 2:
            C0 = (CF.subtract(C0[0], rhi), CC.subtract(C0[1], rlo))
            C = (CF.subtract(C[0], thi), CC.subtract(C[1], tlo))
            LCC = (CF.subtract(LCC[0], m[1]), CC.subtract(LCC[1], m[0]))
        else:
            C0 = (CF.add(C0[0], rlo), CC.add(C0[1], rhi))
            C = (CF.add(C[0], tlo), CC.add(C[1], thi))
            LCC = (CF.add(LCC[0], m[0]), CC.add(LCC[1], m[1]))
    return C0, C, LCC


def ratio_lower_bound(leg, G, j, L1, L2, y1, y2):
    """Certified lower bound, over [L1, L2] x [y1, y2], of the gate ratio
    G h_+/((L/2)|C0|) in sector j of gcd pattern G (a tuple of primes), with
    the q-bound of the gate (low branch when L2 <= log(N_min d_j))."""
    divs = sorted((math.prod(c), c) for rr in range(len(G) + 1) for c in itertools.combinations(G, rr))
    rmax = divs[j][0]
    active = [c for (_, c) in divs[j:]]
    if not L2 <= ln_lo(Dc(leg.nlo * rmax)):
        raise ValueError("ratio_lower_bound is implemented for the low q-branch only")
    C0, C, LCC = enclosures(leg, active, L1, L2, y1, y2)
    glo = leg.glow[0]
    h_lo = CF.add(imig(LCC), CF.multiply(CF.subtract(glo, CC.divide(L2, 2)), imag(C)))
    if h_lo <= 0:
        return Dc(0)
    G_lo = exp_lo(min(CF.multiply(y1, CF.add(L1, glo)), CF.multiply(y2, CF.add(L1, glo))))
    den_hi = CC.multiply(CC.divide(L2, 2), imag(C0))
    return CF.divide(CF.multiply(G_lo, h_lo), den_hi)


def certify_leg(P, nlo, nhi, theta, maxdepth=40):
    leg = Leg(P, nlo, nhi)
    y1 = sqrt_lo(Y0SQ)
    y2 = sqrt_hi(YMAXSQ)
    k = len(P)
    stats = dict(patterns=0, leaves=0, h_nonpositive=0, splits=0, max_ratio_ub=Dc(0), worst=None,
                 undecided=0)
    for r in range(k + 1):
        for G in itertools.combinations(P, r):
            divs = sorted((math.prod(c), c)
                          for rr in range(len(G) + 1) for c in itertools.combinations(G, rr))
            for j in range(len(divs)):
                stats["patterns"] += 1
                rmax = divs[j][0]
                rprev = divs[j - 1][0] if j else 0
                active = [c for (_, c) in divs[j:]]
                lmin = ln_lo(Dc(2)) if j == 0 else ln_lo(Dc(nlo * rprev))
                lmax = ln_hi(Dc(nhi * rmax))
                trans = (ln_lo(Dc(nlo * rmax)), ln_hi(Dc(nlo * rmax)))
                pieces = []
                if lmin <= trans[1]:
                    pieces.append((True, lmin, min(lmax, trans[1])))
                if trans[0] <= lmax:
                    pieces.append((False, max(lmin, trans[0]), lmax))
                for low, a, b in pieces:
                    if a > b:
                        continue
                    # initial chunks of width <= 1/4 in L
                    n0 = int(CC.divide(CC.subtract(b, a), Dc("0.25")).to_integral_value(rounding=ROUND_CEILING)) or 1
                    edges = [a] + [CN.add(a, CN.multiply(CN.divide(CN.subtract(b, a), n0), i)) for i in range(1, n0)] + [b]
                    stack = [(edges[i], edges[i + 1], y1, y2, 0) for i in range(n0)]
                    while stack:
                        L1, L2, ya, yb, dep = stack.pop()
                        kind, ratio = evaluate(leg, active, rmax, low, L1, L2, ya, yb, theta)
                        if kind == "h":
                            stats["leaves"] += 1
                            stats["h_nonpositive"] += 1
                            continue
                        if kind == "r":
                            stats["leaves"] += 1
                            if ratio > stats["max_ratio_ub"]:
                                stats["max_ratio_ub"] = ratio
                                stats["worst"] = dict(G0=G, sector=[rprev, rmax], L=[str(L1), str(L2)],
                                                      y=[str(ya), str(yb)], low_branch=low)
                            continue
                        if dep >= maxdepth:
                            # a leaf that cannot be decided at the depth limit fails the leg
                            stats["undecided"] += 1
                            stats["first_undecided"] = dict(G0=G, sector=[rprev, rmax], L=[str(L1), str(L2)],
                                                            y=[str(ya), str(yb)], low_branch=low)
                            stats["max_ratio_ub"] = str(stats["max_ratio_ub"])
                            stats["passed"] = False
                            return stats
                        stats["splits"] += 1
                        # bisect the side that is longer relative to (1/4, 1/16)
                        if CN.subtract(L2, L1) * 4 >= CN.subtract(yb, ya) * 16:
                            m = CN.divide(CN.add(L1, L2), 2)
                            stack.append((L1, m, ya, yb, dep + 1))
                            stack.append((m, L2, ya, yb, dep + 1))
                        else:
                            m = CN.divide(CN.add(ya, yb), 2)
                            stack.append((L1, L2, ya, m, dep + 1))
                            stack.append((L1, L2, m, yb, dep + 1))
    stats["max_ratio_ub"] = str(stats["max_ratio_ub"])
    stats["passed"] = stats["undecided"] == 0
    return stats


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--theta", default="3/4",
                    help="acceptance threshold; one value or four comma-separated values (one per leg)")
    ap.add_argument("--legs", default="0,1,2,3")
    ap.add_argument("--maxdepth", type=int, default=40,
                    help="bisection depth at which an undecided leaf fails its leg")
    ap.add_argument("--output", default=None)
    ap.add_argument("--negative-control", action="store_true",
                    help="also certify lower bounds of the gate ratio at the sampled maximizers, "
                         "showing the thresholds cannot be lowered past 0.70 ({2,3,5,7,11}, {2,3,5,7}) "
                         "or 0.18 ({2,3,5})")
    a = ap.parse_args()
    ths = [Fraction(x) for x in a.theta.split(",")]
    if len(ths) == 1:
        ths = ths * len(LEGS)
    thetas = [CF.divide(Dc(th.numerator), Dc(th.denominator)) for th in ths]
    rec = {"title": "Interval re-verification of the Dini y-transfer gate with margin",
           "date": "2026-10-12", "model": "Claude Opus 5.5 (claude-opus-5-5)",
           "source_package": PACKAGE, "theta": a.theta, "precision_digits": PREC,
           "package_reported_ratio_ub": PACKAGE_RATIO_UB, "legs": []}
    ok = True
    for i in [int(x) for x in a.legs.split(",")]:
        P, nlo, nhi = LEGS[i]
        t0 = time.time()
        st = certify_leg(P, nlo, nhi, thetas[i], maxdepth=a.maxdepth)
        st.update(P=list(P), N_range=[nlo, nhi], theta=str(ths[i]), seconds=round(time.time() - t0, 1))
        rec["legs"].append(st)
        ok = ok and st["passed"]
        print(json.dumps({k: st[k] for k in ("P", "patterns", "leaves", "h_nonpositive", "splits",
                                             "undecided", "max_ratio_ub", "seconds")}), file=sys.stderr)
    if a.negative_control:
        # certified LOWER bounds of the gate ratio near the float maximizers
        # (explore_dini_gate_landscape.py); the upper bounds above cannot be lowered past these.
        # Rectangles: L in [log 2, 0.6931471806] or [ln_lo(n), ln_hi(n)], y in the enclosure of y0.
        ylo, yhi = sqrt_lo(Y0SQ), sqrt_hi(Y0SQ)
        l2 = (ln_lo(Dc(2)), Dc("0.6931471806"))
        n_att = 6910020          # = 330 * 20940, gcd(n, 2310) = 330, n/690988 = 10.0002 in (10, 11]
        pts = [(0, (2, 5, 7), 0, l2, "0.70", "covered domain (L = log 2 is not attained by n = 70k)"),
               (0, (2, 3, 5, 11), 6, (ln_lo(Dc(n_att)), ln_hi(Dc(n_att))), "0.66",
                "attained: n = 6910020 at N = 690988, where the q-bound is exact"),
               (1, (2, 5, 7), 0, l2, "0.70", "covered domain"),
               (2, (2, 3, 5), 0, l2, "0.18", "covered domain")]
        neg = []
        for i, G, j, (L1, L2), claim, where in pts:
            P, nlo, nhi = LEGS[i]
            leg = Leg(P, nlo, nhi)
            lb = ratio_lower_bound(leg, G, j, L1, L2, ylo, yhi)
            divs = sorted(math.prod(c) for rr in range(len(G) + 1) for c in itertools.combinations(G, rr))
            neg.append(dict(P=list(P), G0=list(G), sector=[divs[j - 1] if j else 0, divs[j]],
                            L=[str(L1), str(L2)], y="y0", where=where, ratio_lower_bound=str(lb),
                            exceeds=claim, confirmed=bool(lb > Dc(claim))))
        rec["negative_control"] = neg
        ok = ok and all(x["confirmed"] for x in neg)
    rec["result"] = "PASS" if ok else "FAIL"
    rec["software"] = {"python": platform.python_version(), "implementation": platform.python_implementation()}
    with open(__file__, "rb") as fh:
        rec["checker_sha256"] = hashlib.sha256(fh.read()).hexdigest()
    out = json.dumps(rec, indent=1)
    if a.output:
        with open(a.output, "w") as fh:
            fh.write(out + "\n")
        print("wrote", a.output)
    else:
        print(out)
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
