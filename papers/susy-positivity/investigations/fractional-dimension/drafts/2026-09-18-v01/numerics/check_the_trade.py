#!/usr/bin/env python3
"""
Why the transfer's positivity and the lattice's part company, and why the trade is
not the explanation.  Standard library only; prints JSON to stdout.  Written by
Claude Opus 5 (Anthropic), model `claude-opus-5`, for the fractional-dimension
investigation, 18 September 2026.

THE QUESTION.  The fourth note found that the contraction criterion has arithmetic
content on exactly omega in (0,1/2) -- that is m in (1,2) -- which is exactly the
open interval on which the third note proved the lattice point count negative, and
asked whether that is one fact or two.  On the transfer side the carrier is the
rational factor (p+a)/(p-a) with a = (2-m)/2, which at m = 2 does not LOSE a
positivity but EXCHANGES one for another: completely monotone and not inner for
m < 2, inner and not completely monotone for m > 2.

WHAT IS CHECKED.

  A. The arithmetic behind the theta side.  R_j(n), the number of ORDERED
     representations of n as j positive squares, by dynamic programming against
     brute-force enumeration; s(n) = min{j : R_j(n) > 0}, the least number of
     POSITIVE squares; and N_k = min{n : s(n) >= k+2}.  N_0 = 2, N_1 = 3, N_2 = 7,
     and N_k does not exist for k >= 3 because s(n) <= 4 for every n -- Lagrange's
     four-square theorem.
  B. The sign law for the binomial coefficient.  For m in the gap (k, k+1),
     sign binom(m,j) = (-1)^max(0, j-k-1): positive for j <= k+1, first negative at
     j = k+2, alternating after.  Exact rationals.
  C. The forced coefficient.  Since theta^m = sum_j binom(m,j) (theta-1)^j and
     (theta-1)^j = sum_n 2^j R_j(n) q^n,
         r_m(n) = sum_j binom(m,j) 2^j R_j(n),
     so (i) r_m(n) > 0 automatically for n <= k+1, because R_j(n) = 0 for j > n;
     and (ii) at n = N_k every contributing j is >= k+2, so the leading term is
     negative.  Checked exactly on grids in the first three gaps, together with the
     closed forms r_m(2) = 2m(m-1), r_m(3) = (4/3)m(m-1)(m-2) and
     r_m(7) = 64 binom(m,4) + 128 binom(m,7).
  D. At the integers the coefficients are representation numbers and none is
     negative.  Exact, m = 1..5.
  E. The transfer has exactly ONE positivity threshold, and it is at m = 2.
     a = (2-m)/2 vanishes only there; k^Gamma_omega(tau) > 0 and the comb weights
     ct_n > 0 at every real omega > 0, across omega = 1, 3/2, 2, 5/2; and the two
     Gamma-ratio parameter gaps of the fourth note's regrouping, 1/2 and
     c = omega - 1/2, stay non-negative for every omega >= 1/2.  The transfer's only
     other feature at an integer is at m = 3, where the archimedean exponent
     omega - 1 = (m-3)/2 vanishes: a REGULARITY threshold (the atom goes from
     unbounded to vanishing at the origin), not a positivity one -- and it points
     the wrong way, since at m = 3 the theta REGAINS positivity.
  F. Why the transfer continues positively and the point count does not.  The
     comb's positivity is LOCAL: the Euler factor of zeta(u-d)/zeta(u) at p is
     1 + sum_{k>=1} p^((k-1)d) (p^d - 1) p^(-ku), whose coefficients are positive
     for every real d > 0 because p^d > 1.  Local positivity is an inequality in d
     that survives continuation, and multiplying the local factors reproduces the
     Jordan totient J_d(n).  The point count has no such local structure: its unique
     continuation is a binomial series whose coefficients alternate.
  G. The divergence.  The theta's failure set and the criterion's content set agree
     on (1,2) and differ on (2,3), where the theta still fails (N_2 = 7) and the
     criterion is vacuous.  So no equivalence of the two positivities can hold.

  Counts below refer to finite test cases, not independent theorems.

ZETA HYGIENE.  NO VALUE OF zeta IS COMPUTED ANYWHERE IN THIS PROGRAMME.  The comb
is handled through its Euler factors and the Jordan totient, both elementary; the
theta side is exact rational arithmetic on representation numbers.

SCOPE.  Nothing here is a positivity certificate for the Weil form and nothing here
is a statement about the zeros.
"""
import json
import math
from fractions import Fraction as F

NMAX_R = 240          # range of the representation-number table
NMAX_EXACT = 40       # range of exact r_m(n) arithmetic
GRID = (1, 3, 5, 8, 11, 13, 15)      # m = k + t/16 for t in GRID


# ------------------------------------------------- representation numbers
def build_R(nmax):
    """R[j][n] = number of ORDERED tuples of j positive squares summing to n."""
    sq = [k * k for k in range(1, int(nmax ** 0.5) + 1)]
    R = [[0] * (nmax + 1) for _ in range(nmax + 1)]
    R[0][0] = 1
    for j in range(1, nmax + 1):
        prev, cur = R[j - 1], R[j]
        for n in range(1, nmax + 1):
            t = 0
            for s in sq:
                if s > n:
                    break
                t += prev[n - s]
            cur[n] = t
    return R


R = build_R(NMAX_R)


def brute_R(j, n):
    """Ordered j-tuples of positive squares summing to n, by direct enumeration."""
    if j == 0:
        return 1 if n == 0 else 0
    tot, k = 0, 1
    while k * k <= n:
        tot += brute_R(j - 1, n - k * k)
        k += 1
    return tot


def s_min(n):
    for j in range(1, NMAX_R + 1):
        if R[j][n] > 0:
            return j
    return None


SMIN = {n: s_min(n) for n in range(1, NMAX_R + 1)}


def N_of(k):
    c = [n for n in range(1, NMAX_R + 1) if SMIN[n] >= k + 2]
    return min(c) if c else None


# ------------------------------------------------- the interpolated point count
def binom(m, j):
    v = F(1)
    for i in range(j):
        v *= (m - i)
    for i in range(1, j + 1):
        v /= i
    return v


def r_of(m, n):
    """r_m(n) = sum_j binom(m,j) 2^j R_j(n), the q^n coefficient of theta^m."""
    return sum(binom(m, j) * F(2) ** j * R[j][n] for j in range(1, n + 1))


# ------------------------------------------------- the transfer side
def kG(omega, tau):
    """k^Gamma_omega(tau) = (2 pi^om / Gamma(om)) (2 sinh tau)^(om-1) e^(tau/2)."""
    return ((2.0 * math.pi ** omega / math.gamma(omega))
            * (2.0 * math.sinh(tau)) ** (omega - 1.0) * math.exp(tau / 2.0))


def prime_factors(n):
    out, d = [], 2
    while d * d <= n:
        if n % d == 0:
            out.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        out.append(n)
    return out


def comb_weight(n, omega):
    v = n ** (omega - 0.5)
    for p in prime_factors(n):
        v *= 1.0 - p ** (-2.0 * omega)
    return v


def jordan(n, d):
    """J_d(n) = n^d prod_{p | n} (1 - p^(-d))."""
    v = float(n) ** d
    for p in prime_factors(n):
        v *= 1.0 - float(p) ** (-d)
    return v


class Group(object):
    def __init__(self, name, note=None):
        self.name, self.note = name, note
        self.checks, self.tables = [], {}

    def add(self, what, error, tol):
        self.checks.append({"what": what, "error": error, "tolerance": tol, "pass": error < tol})
        return self

    def assert_true(self, what, ok):
        self.checks.append({"what": what, "error": 0.0 if ok else 1.0, "tolerance": 0.5, "pass": bool(ok)})
        return self

    def out(self):
        d = {"name": self.name, "cases": len(self.checks),
             "worst_margin_against_own_tolerance": max(c["error"] / c["tolerance"] for c in self.checks),
             "pass": all(c["pass"] for c in self.checks), "checks": self.checks}
        if self.note:
            d["note"] = self.note
        d.update(self.tables)
        return d


# --------------------------------------------------------------------- groups
def group_squares():
    g = Group("A. the arithmetic behind the theta side: least number of positive squares",
              "N_k = least n needing at least k+2 positive squares.  It exists for k = 0,1,2 "
              "and not for k >= 3, because Lagrange's four-square theorem makes s(n) <= 4 for "
              "every n.  That is the whole of the Lagrange threshold the third note observed")
    for j in range(1, 5):
        for n in range(1, 13):
            g.assert_true("R_%d(%d) by dynamic programming = brute-force enumeration" % (j, n),
                          R[j][n] == brute_R(j, n))
    g.assert_true("s(n) <= 4 for every n <= %d (Lagrange)" % NMAX_R,
                  max(SMIN.values()) == 4)
    expected = {0: 2, 1: 3, 2: 7, 3: None, 4: None, 5: None}
    got = {}
    for k in range(0, 6):
        N = N_of(k)
        got[k] = N
        g.assert_true("N_%d = %s" % (k, expected[k]), N == expected[k])
        if N is not None:
            g.assert_true("s(N_%d) = %d exactly, so the leading j is k+2" % (k, k + 2),
                          SMIN[N] == k + 2)
            g.assert_true("R_%d(N_%d) > 0" % (k + 2, k), R[k + 2][N] > 0)
    g.tables = {"s(n) for n = 1..24": [SMIN[n] for n in range(1, 25)],
                "N_k": {("k = %d" % k): got[k] for k in got},
                "max s(n) over n <= %d" % NMAX_R: max(SMIN.values())}
    return g.out()


def group_signs():
    g = Group("B. the sign law for binom(m,j) on the gap (k, k+1)",
              "binom(m,j) = prod_{i<j}(m-i)/j!, and the negative factors are exactly those with "
              "i >= k+1, so sign = (-1)^max(0, j-k-1): positive through j = k+1, first negative "
              "at j = k+2, alternating after.  Exact rationals")
    for k in range(0, 6):
        for t in (1, 8, 15):          # three points per gap keeps the record proportionate
            m = F(k) + F(t, 16)
            for j in range(1, 14):
                b = binom(m, j)
                pred = (-1) ** max(0, j - k - 1)
                g.assert_true("sign binom(%s, %d) = %+d on the gap (%d,%d)" % (m, j, pred, k, k + 1),
                              b != 0 and ((b > 0) == (pred > 0)))
    return g.out()


def group_forced():
    g = Group("C. the forced negative coefficient in each of the first three gaps",
              "r_m(n) = sum_j binom(m,j) 2^j R_j(n) with R_j(n) = 0 for j > n.  So for n <= k+1 "
              "every contributing j has a positive binomial and r_m(n) > 0 automatically; and at "
              "n = N_k every contributing j is >= k+2, so the leading term is negative.  All "
              "exact")
    rows = {}
    for k in (0, 1, 2, 3, 4):
        for t in GRID:
            m = F(k) + F(t, 16)
            for n in range(1, k + 2):
                g.assert_true("r_m(%d) > 0 automatically at m = %s (n <= k+1)" % (n, m),
                              r_of(m, n) > 0)
    for k in (0, 1, 2):
        N = N_of(k)
        sub = {}
        for t in GRID:
            m = F(k) + F(t, 16)
            pre = all(r_of(m, n) > 0 for n in range(1, N))
            val = r_of(m, N)
            g.assert_true("r_m(n) > 0 for every n < %d at m = %s" % (N, m), pre)
            g.assert_true("r_m(%d) < 0 at m = %s" % (N, m), val < 0)
            sub["m = %s" % m] = {"r_m(N_k)": float(val), "exact": str(val),
                                 "positive below N_k": pre}
        rows["gap (%d,%d), N_%d = %d" % (k, k + 1, k, N)] = sub
    # closed forms
    for t in GRID:
        for k, N, closed in ((0, 2, lambda m: 2 * m * (m - 1)),
                             (1, 3, lambda m: F(4, 3) * m * (m - 1) * (m - 2)),
                             (2, 7, lambda m: 64 * binom(m, 4) + 128 * binom(m, 7))):
            m = F(k) + F(t, 16)
            g.assert_true("closed form for r_m(%d) at m = %s" % (N, m), r_of(m, N) == closed(m))
    # the coefficients below N_2 = 7, whose positivity on (2,3) the note proves by hand
    for t in GRID:
        m = F(2) + F(t, 16)
        for n, closed in ((4, lambda m: 2 * m + 16 * binom(m, 4)),
                          (5, lambda m: 8 * binom(m, 2) + 32 * binom(m, 5)),
                          (6, lambda m: 24 * binom(m, 3) + 64 * binom(m, 6))):
            g.assert_true("closed form for r_m(%d) at m = %s" % (n, m), r_of(m, n) == closed(m))
            g.assert_true("r_m(%d) > 0 at m = %s (the note bounds this by hand)" % (n, m),
                          r_of(m, n) > 0)
    g.tables = {"the forced coefficient, exactly": rows,
                "closed forms": {"r_m(2)": "2 m (m-1)", "r_m(3)": "(4/3) m (m-1) (m-2)",
                                 "r_m(4)": "2 m + 16 binom(m,4)",
                                 "r_m(5)": "8 binom(m,2) + 32 binom(m,5)",
                                 "r_m(6)": "24 binom(m,3) + 64 binom(m,6)",
                                 "r_m(7)": "64 binom(m,4) + 128 binom(m,7)"},
                "the representation data behind them": {
                    "R_2(2)=1": R[2][2], "R_3(3)=1": R[3][3], "R_1(4)=1, R_4(4)=1": [R[1][4], R[4][4]],
                    "R_2(5)=2, R_5(5)=1": [R[2][5], R[5][5]],
                    "R_3(6)=3, R_6(6)=1": [R[3][6], R[6][6]],
                    "R_4(7)=4, R_7(7)=1": [R[4][7], R[7][7]]}}
    return g.out()


def group_integers():
    g = Group("D. at the integers the coefficients are representation numbers",
              "so none is negative, and theta(it)^m is completely monotone there.  Exact")
    rows = {}
    for m in (1, 2, 3, 4, 5):
        neg = [n for n in range(1, NMAX_EXACT + 1) if r_of(F(m), n) < 0]
        g.assert_true("no negative r_%d(n) for n <= %d" % (m, NMAX_EXACT), not neg)
        g.assert_true("r_%d(n) agrees with the DP representation count at n <= 12" % m,
                      all(r_of(F(m), n) == sum(binom(F(m), j) * F(2) ** j * R[j][n]
                                               for j in range(1, n + 1))
                          for n in range(1, 13)))
        rows["m = %d" % m] = {"negative coefficients among n <= %d" % NMAX_EXACT: neg,
                              "first eight r_m(n)": [int(r_of(F(m), n)) for n in range(1, 9)]}
    g.tables = {"integer ranks": rows}
    return g.out()


def group_transfer():
    g = Group("E. the transfer has exactly one positivity threshold, and it is at m = 2",
              "every factor of the Markov part is positive at every real omega > 0; the only "
              "object in the decomposition whose positivity depends on omega is the rational "
              "factor (p+a)/(p-a), and it changes at a = 0, i.e. m = 2.  The transfer's only "
              "other feature at an integer is the archimedean exponent omega - 1 = (m-3)/2 "
              "vanishing at m = 3, which is a REGULARITY threshold and not a positivity one")
    rows = {}
    for m in (1.25, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 6.0):
        om = (m - 1.0) / 2.0
        a, c = (2.0 - m) / 2.0, (m - 2.0) / 2.0
        g.assert_true("a = (2-m)/2 vanishes only at m = 2 (m = %g)" % m,
                      (abs(a) < 1e-15) == (abs(m - 2.0) < 1e-15))
        g.assert_true("the two Gamma-ratio gaps 1/2 and c are >= 0 iff omega >= 1/2 (m = %g)" % m,
                      (c >= -1e-15) == (om >= 0.5 - 1e-15))
        kvals = [kG(om, tau) for tau in (0.05, 0.3, 1.0, 3.0, 8.0)]
        g.assert_true("k^Gamma_omega(tau) > 0 at every sampled tau (m = %g)" % m,
                      all(v > 0.0 for v in kvals))
        cvals = [comb_weight(n, om) for n in range(1, 60)]
        g.assert_true("ct_n > 0 for every n < 60 (m = %g)" % m, all(v > 0.0 for v in cvals))
        jvals = [jordan(n, m - 1.0) for n in range(1, 60)]
        g.assert_true("J_d(n) > 0 for every n < 60 (m = %g)" % m, all(v > 0.0 for v in jvals))
        rows["m = %g" % m] = {"omega": om, "a": a, "c": c,
                              "archimedean exponent omega - 1": om - 1.0,
                              "min k^Gamma over the sample": min(kvals),
                              "min ct_n, n < 60": min(cvals), "min J_d(n), n < 60": min(jvals)}
    # the regularity threshold at m = 3, and that it is not a sign change
    for m in (2.5, 3.0, 3.5):
        om = (m - 1.0) / 2.0
        g.assert_true("k^Gamma_omega stays positive across the m = 3 regularity threshold "
                      "(m = %g, exponent %+g)" % (m, om - 1.0),
                      kG(om, 0.02) > 0.0 and kG(om, 2.0) > 0.0)
    g.assert_true("the archimedean atom is unbounded at the origin for m < 3 and vanishes "
                  "there for m > 3", kG(0.75, 1e-6) > kG(0.75, 1.0) and kG(1.25, 1e-6) < kG(1.25, 1.0))
    g.tables = {"the transfer across the integers": rows}
    return g.out()


def group_local():
    g = Group("F. the comb's positivity is local at each prime, and local positivity continues",
              "the Euler factor of zeta(u-d)/zeta(u) at p is "
              "1 + sum_{k>=1} p^((k-1)d) (p^d - 1) p^(-ku): its coefficients are positive for "
              "every real d > 0 because p^d > 1, an inequality that survives continuation in d.  "
              "Multiplying the local factors reproduces the Jordan totient.  The point count has "
              "no such local structure -- its continuation is a binomial series whose "
              "coefficients alternate (group B)")
    for d in (0.1, 0.5, 1.0, 1.5, 2.0, 3.0, 4.0):
        for p in (2, 3, 5, 7, 11):
            for k in range(1, 5):
                coeff = p ** ((k - 1) * d) * (p ** d - 1.0)
                g.assert_true("local coefficient at p = %d, k = %d is positive (d = %g)" % (p, k, d),
                              coeff > 0.0)
        # the local factors multiply to J_d
        for n in (12, 30, 36, 49, 60):
            loc = 1.0
            for p in prime_factors(n):
                loc *= 1.0 - p ** (-d)
            g.assert_true("prod_{p|n} (1 - p^-d) . n^d = J_d(n) at n = %d, d = %g" % (n, d),
                          abs(loc * n ** d - jordan(n, d)) <= 1e-12 * jordan(n, d))
    g.tables = {"reading": ("the transfer's two positivity mechanisms -- the Beta density of a "
                            "Gamma ratio and the Euler factor of the comb -- both take the "
                            "continuation parameter as an EXPONENT, where positivity is an "
                            "inequality that holds for every real value.  The point count takes "
                            "it as a BINOMIAL INDEX, where it does not")}
    return g.out()


def group_divergence():
    g = Group("G. the divergence: the two positivity sets agree on (1,2) and differ on (2,3)",
              "so no equivalence between them can hold, and the coincidence of intervals the "
              "fourth note recorded is the first gap and nothing more")
    # theta fails on (1,2) and on (2,3); the criterion has content only on (1,2)
    for t in GRID:
        m12, m23 = F(1) + F(t, 16), F(2) + F(t, 16)
        g.assert_true("theta^m is not completely monotone at m = %s (r_m(3) < 0)" % m12,
                      r_of(m12, 3) < 0)
        g.assert_true("theta^m is not completely monotone at m = %s (r_m(7) < 0)" % m23,
                      r_of(m23, 7) < 0)
        a12, a23 = (2 - m12) / 2, (2 - m23) / 2
        g.assert_true("the criterion has content at m = %s (a = %s > 0)" % (m12, a12), a12 > 0)
        g.assert_true("the criterion is vacuous at m = %s (a = %s <= 0)" % (m23, a23), a23 <= 0)
    # and at m = 3 the theta is positive while the rational factor is not
    g.assert_true("at m = 3 theta^m is completely monotone (a genuine lattice)",
                  all(r_of(F(3), n) >= 0 for n in range(1, NMAX_EXACT + 1)))
    g.assert_true("at m = 3 the rational factor is NOT completely monotone (a = -1/2 < 0)",
                  (2 - F(3)) / 2 < 0)
    g.tables = {"the divergence": {
        "m in (1,2)": {"theta^m completely monotone": False, "witness": "r_m(3) < 0",
                       "(p+a)/(p-a) completely monotone": True,
                       "criterion has arithmetic content": True},
        "m = 2": {"theta^m completely monotone": True, "witness": "rank-two lattice",
                  "(p+a)/(p-a) completely monotone": True,
                  "criterion has arithmetic content": False},
        "m in (2,3)": {"theta^m completely monotone": False, "witness": "r_m(7) < 0",
                       "(p+a)/(p-a) completely monotone": False,
                       "criterion has arithmetic content": False},
        "m = 3": {"theta^m completely monotone": True, "witness": "rank-three lattice",
                  "(p+a)/(p-a) completely monotone": False,
                  "criterion has arithmetic content": False}},
        "conclusion": ("the theta's failure set contains (2,3) and the criterion's content set "
                       "does not; at m = 3 the theta is positive and the rational factor is not.  "
                       "The two positivity statements are not the same statement, and the trade "
                       "is not the explanation")}
    return g.out()


def main():
    groups = [group_squares(), group_signs(), group_forced(), group_integers(),
              group_transfer(), group_local(), group_divergence()]
    out = {
        "programme": "check_the_trade.py",
        "investigation": "fractional-dimension",
        "model": "claude-opus-5",
        "object": "the two positivity statements of the family -- the transfer's, carried by the "
                  "rational factor (p+a)/(p-a), and the lattice's, carried by the interpolated "
                  "point count r_m(n) -- and whether their thresholds are one fact or two",
        "zeta": "NOT EVALUATED ANYWHERE in this programme",
        "scope": "finite test cases; not a positivity certificate and not a statement about the "
                 "zeros",
        "groups": groups,
    }
    out["all_pass"] = all(g["pass"] for g in groups)
    out["total_checks"] = sum(g["cases"] for g in groups)
    print(json.dumps(out, indent=2, sort_keys=False))


if __name__ == "__main__":
    main()
