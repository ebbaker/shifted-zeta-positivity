#!/usr/bin/env python3
"""
The Markov part is the Epstein scattering matrix of a rank-(d+1) lattice, and the lattice does
not continue.  Standard library only; prints JSON to stdout.  Nothing here is a positivity
certificate and nothing here is about the zeros.

WHAT IS SHOWN.  Two things, one positive and one negative.

A. THE INTEGER POINTS ARE ALL REALIZED, not just d = 1.  For a covolume-one lattice L of rank
   m in R^m write

       Z_L(s) = sum_{0 != v in L} |v|^(-2s) ,     Estar_L(s) = Z_L(s)/zeta(2s)

   for the Epstein zeta and its PRIMITIVE part (every nonzero vector is uniquely k times a
   primitive one, so the two differ by exactly zeta(2s)).  Poisson summation in dimension m,
   theta_L(1/x) = x^(m/2) theta_L(x) for L = L* unimodular, gives the Epstein functional
   equation, and dividing it by zeta gives

       xi(2s) Estar_L(s) = xi(m - 2s) Estar_{L*}(m/2 - s)  ,

   so that the RATIO is universal -- independent of the lattice, depending only on the rank:

       Estar_L(s) / Estar_{L*}(m/2 - s) = xi(m - 2s)/xi(2s) = xi(2s - d)/xi(2s),   d = m - 1.

   Under this investigation's dictionary -- d = 2 omega, u = 2s = p + b, b = (d+1)/2 -- the right
   side is exactly Ktilde_omega(p) = Lambda(s0 - omega)/Lambda(s0 + omega), the Markov part of
   the shifted Weil transfer.  So:

       for EVERY integer d >= 1, Ktilde_omega is the scattering matrix (the c-function of the
       degenerate maximal-parabolic Eisenstein series) of the space of unimodular lattices of
       RANK d + 1 = 2 omega + 1.

   The three dictionary entries are then simultaneously realized: the archimedean factor is the
   integral over the d-dimensional unipotent radical, the comb zeta(2s-d)/zeta(2s) = sum_n
   J_d(n) n^(-2s) is the sum over that radical mod n, and the residue |S^d|/(2 zeta(d+1)) is the
   residue of Estar at its rightmost pole s = m/2.  And the transfer's own reflection p -> -p IS
   the Epstein functional equation s -> m/2 - s, exactly; on Re p = 0 the two arguments are
   complex conjugates, which is why |Ktilde| = 1 there.

   This STRENGTHENS the investigation's previous position.  d = 1 was the only integer in the
   family's range (0,1], and was the only point known to be realized.  In fact d = 1, 2, 3, ...
   are all realized, as ranks 2, 3, 4, ...; they simply lie outside the range.  The family
   omega in (0,1/2] is m = d + 1 in (1,2]: it lives entirely in the FIRST GAP of the lattice
   sequence, between rank 1 and rank 2, with RH sitting at its right endpoint m = 2 = Z^2.

B. THE LATTICE DOES NOT CONTINUE INTO THAT GAP.  The point count of Z^m has a unique analytic
   interpolation in m, namely the coefficients of theta(tau)^m -- well defined for every real m
   because theta is nonvanishing on the upper half-plane -- and they are POLYNOMIALS in m:

       r_m(n) = sum_{j>=1} C(m,j) 2^j R_j(n),   R_j(n) = # ordered reps of n as j positive squares,

   agreeing with the representation numbers of Z^m at every integer m.  The first three are

       r_m(1) = 2m ,    r_m(2) = 2m(m-1) ,    r_m(3) = (4/3) m(m-1)(m-2) .

   With m = d + 1 the third reads r_{d+1}(3) = (4/3)(d+1) d (d-1), which is STRICTLY NEGATIVE
   for every d in (0,1) and vanishes exactly at the endpoints d = 0 and d = 1.  So on the whole
   open range of the family the interpolated lattice has a negative point count at n = 3 -- and
   since theta(i t)^m = sum_n r_m(n) e^(-pi n t) is a discrete Laplace expansion, uniqueness of
   Laplace transforms makes this the same statement as: theta(i t)^m is NOT completely monotone.
   There is no measure, hence no space.

   (The companion statement below rank 1 is r_m(2) = 2m(m-1) < 0 for m in (0,1).  A numerical
   scan, reported and not claimed as a theorem, finds a negative coefficient for every
   non-integer m < 4 in the grid and none for m >= 4 -- the Lagrange threshold.)

C. AND THE CAP omega <= 1/2 IS THE RANK-TWO WALL.  xi has simple poles at 0 and 1, so the
   numerator xi(u - d) = xi(m - u) of the Markov part has exactly two poles in p: at
   p = b = omega + 1/2, which is the one the Blaschke factor cancels, and at p = omega - 1/2,
   which lies in the closed left half-plane exactly when omega <= 1/2, that is when m <= 2.  In
   the lattice variable that second pole sits at s = (m-1)/2 = omega, where zeta(2s) has its
   pole precisely at omega = 1/2.  So the family's cap and the rank cap are one statement, and
   both are the pole of zeta at 1 reaching the boundary Re p = 0: rank two -- the lattice zeta
   itself comes from -- is the largest rank at which the transfer has a single cancelled pole.

WHAT THIS ANSWERS.  The investigation asked: is there anything of which J_d and zeta(d+1) are
the invariants when d is not an integer?  The answer here is that whatever it is, it is not a
point set.  J_d(n) > 0 and 1/zeta(d+1) in (0,1) for every real d > 0, and the scattering matrix
they build is unimodular on the critical line for every real d; what fails to continue is the
lattice whose primitive data they are.  The fractional object is a scattering matrix without a
space.

METHOD.  Everything is computed from one function, the completed Epstein integral

    Lambda_m(s) = 1/(s - m/2) - 1/s + int_1^inf (theta_m(x) - 1)(x^(s-1) + x^(m/2-s-1)) dx,
    theta_m(x) = (sum_{k in Z} e^(-pi x k^2))^m ,

which is Riemann's theta method in dimension m.  It is manifestly symmetric under
s <-> m/2 - s, so it is verified NON-TAUTOLOGICALLY against direct lattice summation in the
region of absolute convergence, and its only input, Poisson summation in dimension m, is
verified on its own.  At m = 1 it is 2 xi(2s), which supplies xi and zeta at real arguments.

Values of zeta are taken at REAL arguments only, including negative ones, by this convergent
integral.  The real segment of the critical strip is unavoidable here -- it is where a
scattering matrix lives -- but no value off the real axis is computed, no zero is located, and
nothing here bears on the zeros.

Author: Claude Opus 5 (Anthropic), model `claude-opus-5`.  18 September 2026.
"""

import json
import math
from fractions import Fraction as F

# ----------------------------------------------------------------------------------------------
# harness
# ----------------------------------------------------------------------------------------------


class Group(object):
    def __init__(self, name, note=None):
        self.name, self.note, self.checks, self.tables = name, note, [], {}

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


# ----------------------------------------------------------------------------------------------
# the theta machinery:  one quadrature grid, one cached theta, everything else from it
# ----------------------------------------------------------------------------------------------

_T_TOP = 14.0          # theta_m(x) - 1 ~ 2m e^(-pi x); at x = 14 that is under 1e-19
_PANELS = 16
_GL_ORDER = 40


def gauss_legendre(n):
    """Nodes and weights on [-1,1] by Newton on the Legendre polynomial."""
    xs, ws = [], []
    for i in range(1, n + 1):
        x = math.cos(math.pi * (i - 0.25) / (n + 0.5))
        dp = 1.0
        for _ in range(100):
            p0, p1 = 1.0, 0.0
            for j in range(1, n + 1):
                p2 = p1
                p1 = p0
                p0 = ((2 * j - 1) * x * p1 - (j - 1) * p2) / j
            dp = n * (x * p0 - p1) / (x * x - 1.0)
            dx = -p0 / dp
            x += dx
            if abs(dx) < 1e-15:
                break
        xs.append(x)
        ws.append(2.0 / ((1.0 - x * x) * dp * dp))
    return xs, ws


def vartheta(x, K=80):
    """sum_{k in Z} e^(-pi x k^2)."""
    return 1.0 + 2.0 * math.fsum(math.exp(-math.pi * x * k * k) for k in range(1, K + 1))


def _grid():
    gx, gw = gauss_legendre(_GL_ORDER)
    nodes, weights = [], []
    h = (_T_TOP - 1.0) / _PANELS
    for k in range(_PANELS):
        c = 1.0 + k * h + h / 2.0
        for x, w in zip(gx, gw):
            nodes.append(c + x * h / 2.0)
            weights.append(w * h / 2.0)
    return nodes, weights, [vartheta(t) for t in nodes]


_NODES, _WEIGHTS, _VT = _grid()


def Lambda_m(s, m):
    """pi^(-s) Gamma(s) Z_{Z^m}(s), by Riemann's theta method in dimension m."""
    tot = math.fsum(w * (v ** m - 1.0) * (t ** (s - 1.0) + t ** (m / 2.0 - s - 1.0))
                    for t, w, v in zip(_NODES, _WEIGHTS, _VT))
    return 1.0 / (s - m / 2.0) - 1.0 / s + tot


def xi(u):
    """The completed Riemann zeta; Lambda_1(u/2) = 2 xi(u)."""
    return Lambda_m(u / 2.0, 1) / 2.0


def zeta(u):
    return xi(u) * math.pi ** (u / 2.0) / math.gamma(u / 2.0)


def Z_lattice(s, m):
    """The Epstein zeta of Z^m."""
    return Lambda_m(s, m) * math.pi ** s / math.gamma(s)


def Estar(s, m):
    """The PRIMITIVE Epstein zeta of Z^m: sum over primitive vectors only."""
    return Z_lattice(s, m) / zeta(2.0 * s)


def sphere(m):
    """|S^(m-1)|, the unit sphere in R^m."""
    return 2.0 * math.pi ** (m / 2.0) / math.gamma(m / 2.0)


# ----------------------------------------------------------------------------------------------
# the interpolated point count
# ----------------------------------------------------------------------------------------------

_NMAX = 30


def R_table(nmax):
    """R[j][n] = number of ORDERED representations of n as a sum of j positive squares."""
    R = [[0] * (nmax + 1) for _ in range(nmax + 1)]
    R[0][0] = 1
    sq = [k * k for k in range(1, int(nmax ** 0.5) + 1)]
    for j in range(1, nmax + 1):
        for n in range(1, nmax + 1):
            R[j][n] = sum(R[j - 1][n - t] for t in sq if t <= n)
    return R


_R = R_table(_NMAX)


def binom(m, j):
    """C(m,j) for any m (Fraction or float)."""
    num = F(1) if isinstance(m, F) else 1.0
    for i in range(j):
        num = num * (m - i)
    return num / math.factorial(j)


def r_m(m, n):
    """[q^n] theta(tau)^m -- a polynomial in m, the representation numbers of Z^m at integer m."""
    terms = [binom(m, j) * (F(2) ** j if isinstance(m, F) else 2.0 ** j) * _R[j][n]
             for j in range(1, n + 1) if _R[j][n]]
    zero = F(0) if isinstance(m, F) else 0.0
    out = zero
    for t in terms:
        out = out + t
    return out


def brute_counts(m, nmax):
    """Representation numbers of Z^m by direct enumeration."""
    cnt = [0] * (nmax + 1)
    lim = int(nmax ** 0.5)

    def walk(k, acc):
        if k == m:
            if 1 <= acc <= nmax:
                cnt[acc] += 1
            return
        for v in range(-lim, lim + 1):
            a = acc + v * v
            if a <= nmax:
                walk(k + 1, a)

    walk(0, 0)
    return cnt


# power-series log/exp, for the scan only
def theta_pow_series(m, N, _cache={}):
    if N not in _cache:
        a = [0.0] * (N + 1)
        a[0] = 1.0
        k = 1
        while k * k <= N:
            a[k * k] = 2.0
            k += 1
        L = [0.0] * (N + 1)
        for n in range(1, N + 1):
            L[n] = (n * a[n] - math.fsum(j * L[j] * a[n - j] for j in range(1, n))) / n
        _cache[N] = L
    L = _cache[N]
    E = [0.0] * (N + 1)
    E[0] = 1.0
    for n in range(1, N + 1):
        E[n] = math.fsum(j * m * L[j] * E[n - j] for j in range(1, n + 1)) / n
    return E


# ----------------------------------------------------------------------------------------------
# groups
# ----------------------------------------------------------------------------------------------


def group_machinery():
    g = Group("A. the theta machinery, verified against things it does not assume",
              "Poisson summation in dimension m is the only input; the completed integral is "
              "then checked against direct lattice summation where that converges, and against "
              "closed-form zeta values")
    for m in (1, 2, 3, 5):
        for x in (0.3, 0.7, 1.3, 2.5):
            a = vartheta(1.0 / x) ** m
            b = x ** (m / 2.0) * vartheta(x) ** m
            g.add("Poisson: theta_%d(1/%g) = %g^(%d/2) theta_%d(%g)" % (m, x, x, m, m, x),
                  abs(a - b) / abs(b), 1e-13)
    for u, closed, name in ((2.0, math.pi ** 2 / 6.0, "pi^2/6"),
                            (4.0, math.pi ** 4 / 90.0, "pi^4/90"),
                            (6.0, math.pi ** 6 / 945.0, "pi^6/945"),
                            (-1.0, -1.0 / 12.0, "-1/12"),
                            (-3.0, 1.0 / 120.0, "1/120")):
        g.add("zeta(%g) against %s" % (u, name), abs(zeta(u) - closed) / abs(closed), 1e-11)
    # direct lattice sum, with the exact continuum tail, against the theta value
    rows = {}
    for m, s, L in ((2, 2.5, 220), (2, 3.0, 160), (3, 3.0, 45), (4, 4.0, 22)):
        norms = []

        def walk(k, acc):
            if k == m:
                if acc and acc <= L * L:
                    norms.append(acc)
                return
            for v in range(-L, L + 1):
                a = acc + v * v
                if a <= L * L:
                    walk(k + 1, a)

        walk(0, 0)
        direct = math.fsum(q ** (-s) for q in norms)
        tail = sphere(m) * L ** (m - 2.0 * s) / (2.0 * s - m)
        th = Z_lattice(s, m)
        rows["m=%d,s=%g" % (m, s)] = {"direct_plus_tail": direct + tail, "theta_method": th}
        g.add("Epstein Z_{Z^%d}(%g): direct lattice sum + continuum tail vs the theta method"
              % (m, s), abs(direct + tail - th) / abs(th), 3e-5)
    g.tables = {"lattice_sum_cross_check": rows}
    return g.out()


def group_scattering():
    g = Group("B. the scattering identity: the ratio is universal and depends only on the rank",
              "xi(2s) Estar(s) = Lambda_m(s), which is symmetric in s <-> m/2 - s; so the "
              "primitive Epstein zeta of ANY unimodular rank-m lattice has the same reflection "
              "ratio, xi(m-2s)/xi(2s)")
    for m in (2, 3, 4, 5, 6):
        for s in (1.6, 2.2, 3.1):
            lhs = xi(2.0 * s) * Estar(s, m)
            g.add("m=%d s=%g: xi(2s) Estar(s) = Lambda_m(s)" % (m, s),
                  abs(lhs - Lambda_m(s, m)) / abs(Lambda_m(s, m)), 1e-12)
            a = Estar(s, m) / Estar(m / 2.0 - s, m)
            b = xi(m - 2.0 * s) / xi(2.0 * s)
            g.add("m=%d s=%g: Estar(s)/Estar(m/2-s) = xi(m-2s)/xi(2s)" % (m, s),
                  abs(a - b) / abs(b), 1e-11)
    return g.out()


def group_dictionary():
    g = Group("C. the dictionary: at every integer d the Markov part IS that scattering matrix",
              "d = 2 omega, b = (d+1)/2, u = 1/2 + p + omega = 2s, m = d + 1; the arguments "
              "avoid the poles of xi at 0 and 1")
    rows = {}
    for d in (1, 2, 3, 4, 5):
        om = d / 2.0
        m = d + 1
        for p in (0.9, 1.3, 2.4, 3.7):
            u = 0.5 + p + om
            s = u / 2.0
            K_transfer = xi(0.5 + p - om) / xi(0.5 + p + om)     # the Markov part, as defined
            K_rank = xi(m - 2.0 * s) / xi(2.0 * s)               # the rank-m scattering matrix
            K_lat = Estar(s, m) / Estar(m / 2.0 - s, m)          # primitive Epstein ratio
            g.add("d=%d p=%g: Ktilde_omega(p) = xi(m-2s)/xi(2s)" % (d, p),
                  abs(K_transfer - K_rank) / abs(K_rank), 1e-11)
            g.add("d=%d p=%g: Ktilde_omega(p) = Estar(s)/Estar(m/2-s) of Z^%d" % (d, p, m),
                  abs(K_transfer - K_lat) / abs(K_lat), 1e-10)
            rows["d=%d,p=%g" % (d, p)] = K_transfer
    # the reflection p -> -p IS s -> m/2 - s, exactly, in rationals
    for d in (1, 2, 3, 4, 5):
        om = F(d, 2)
        m = F(d + 1)
        for p in (F(9, 10), F(13, 10), F(12, 5), F(37, 10)):
            s_plus = (F(1, 2) + p + om) / 2
            s_minus = (F(1, 2) - p + om) / 2
            g.assert_true("d=%d p=%s: s(-p) = m/2 - s(p) exactly" % (d, p),
                          s_minus == m / 2 - s_plus)
    g.tables = {"values_of_the_markov_part": rows,
                "corollary": "on Re p = 0 the two arguments are complex conjugates and the "
                             "coefficients are real, so |Ktilde_omega| = 1 there: the "
                             "all-pass property of the transfer is the Epstein functional "
                             "equation. Not computed here -- no value off the real axis is."}
    return g.out()


def group_residue():
    g = Group("D. the residue is the residue of the primitive Epstein zeta",
              "Lambda_m has residue 1 at s = m/2, so Estar has residue "
              "pi^(m/2)/(Gamma(m/2) zeta(m)) = |S^(m-1)|/(2 zeta(m)) there; with m = d+1 this "
              "is the |S^d|/(2 zeta(d+1)) of the previous programme")
    for m in (2, 3, 4, 5, 6):
        # Richardson on eps * Lambda_m(m/2 + eps) -> 1
        vals = []
        for eps in (1e-3, 5e-4):
            vals.append(eps * Lambda_m(m / 2.0 + eps, m))
        res_L = 2.0 * vals[1] - vals[0]
        g.add("m=%d: Res_{s=m/2} Lambda_m = 1" % m, abs(res_L - 1.0), 1e-6)
        pred = sphere(m) / (2.0 * zeta(float(m)))
        vals = []
        for eps in (1e-3, 5e-4):
            vals.append(eps * Estar(m / 2.0 + eps, m))
        res_E = 2.0 * vals[1] - vals[0]
        g.add("m=%d: Res_{s=m/2} Estar = |S^(m-1)|/(2 zeta(m))" % m,
              abs(res_E - pred) / pred, 1e-5)
        g.add("m=%d: |S^(m-1)|/(2 zeta(m)) equals pi^(m/2)/(Gamma(m/2) zeta(m))" % m,
              abs(pred - math.pi ** (m / 2.0) / (math.gamma(m / 2.0) * zeta(float(m)))) / pred,
              1e-13)
        # the two residues coincide: dp = 2 ds doubles a residue in s, and the other
        # factor Estar(m/2 - s) -> Estar(0) = Z(0)/zeta(0) = (-1)/(-1/2) = 2 halves it
        g.add("m=%d: Z_{Z^m}(0) = -1" % m, abs(Z_lattice(1e-6, m) + 1.0), 1e-4)
        g.add("m=%d: Estar(0) = 2" % m, abs(Estar(1e-6, m) - 2.0), 1e-4)
        vals = []
        for eps in (1e-3, 5e-4):
            om, b = (m - 1) / 2.0, m / 2.0
            pp = b + eps
            vals.append(eps * (xi(0.5 + pp - om) / xi(0.5 + pp + om)))
        g.add("m=%d: Res_{p=b} Ktilde_omega = Res_{s=m/2} Estar, the Jacobian cancelling "
              "against Estar(0) = 2" % m,
              abs((2.0 * vals[1] - vals[0]) - pred) / pred, 1e-5)
    return g.out()


def group_interpolation():
    g = Group("E. the point count has a unique interpolation, and it is polynomial in m",
              "r_m(n) = sum_j C(m,j) 2^j R_j(n) are the coefficients of theta(tau)^m, which is "
              "well defined for every real m because theta does not vanish on the upper "
              "half-plane; exact rational arithmetic throughout")
    for m in (1, 2, 3, 4, 5):
        b = brute_counts(m, 20)
        ok = all(r_m(F(m), n) == b[n] for n in range(1, 21))
        g.assert_true("m=%d: r_m(n) equals the representation numbers of Z^%d for n <= 20"
                      % (m, m), ok)
    # r_m(n) is a polynomial in m of degree <= n: the (n+1)-st finite difference vanishes
    for n in (1, 2, 3, 4, 5, 6, 7):
        deg = n + 1
        delta = sum((-1) ** (deg - k) * F(math.comb(deg, k)) * r_m(F(k), n)
                    for k in range(deg + 1))
        g.assert_true("n=%d: the %d-th finite difference of m -> r_m(%d) vanishes (degree <= %d)"
                      % (n, deg, n, n), delta == 0)
    # the three closed forms, at rational m
    for m in (F(1, 3), F(7, 10), F(3, 2), F(12, 5), F(7, 2)):
        g.assert_true("m=%s: r_m(1) = 2m" % m, r_m(m, 1) == 2 * m)
        g.assert_true("m=%s: r_m(2) = 2m(m-1)" % m, r_m(m, 2) == 2 * m * (m - 1))
        g.assert_true("m=%s: r_m(3) = (4/3)m(m-1)(m-2)" % m,
                      r_m(m, 3) == F(4, 3) * m * (m - 1) * (m - 2))
    return g.out()


def group_sign():
    g = Group("F. the interpolated lattice is negative on the whole open range of the family",
              "with m = d + 1, r_{d+1}(3) = (4/3)(d+1)d(d-1) < 0 for every d in (0,1) and "
              "vanishes exactly at d = 0 and d = 1; exact rational arithmetic")
    for num in range(1, 20):
        d = F(num, 20)
        val = r_m(d + 1, 3)
        g.assert_true("d=%s: r_{d+1}(3) < 0" % d, val < 0)
    for d in (F(0), F(1)):
        g.assert_true("d=%s: r_{d+1}(3) = 0 exactly" % d, r_m(d + 1, 3) == 0)
    # the shape of the arch: r_{d+1}(3) = (4/3)(d^3 - d) on [0,1]
    g.assert_true("r_{d+1}(3) = (4/3)(d^3 - d) as a polynomial identity",
                  all(r_m(F(k, 7) + 1, 3) == F(4, 3) * ((F(k, 7)) ** 3 - F(k, 7))
                      for k in range(0, 15)))
    g.add("the arch's minimum is at d = 1/sqrt(3)",
          abs(1.0 / math.sqrt(3.0) - min((r_m(1.0 + j / 20000.0, 3), j / 20000.0)
                                         for j in range(0, 20001))[1]), 1e-4)
    g.add("the arch's depth is -8/(9 sqrt 3)",
          abs(r_m(1.0 + 1.0 / math.sqrt(3.0), 3) + 8.0 / (9.0 * math.sqrt(3.0))), 1e-12)
    # the endpoint slopes, from the verified closed form: P(d) = (4/3)(d^3 - d),
    # P'(d) = (4/3)(3d^2 - 1); the exact central difference of a cubic is P' + (4/3)h^2
    for d, slope in ((F(0), F(-4, 3)), (F(1), F(8, 3))):
        h = F(1, 10 ** 6)
        num = (r_m(d + h + 1, 3) - r_m(d - h + 1, 3)) / (2 * h)
        g.assert_true("d=%s: P'(d) = (4/3)(3d^2 - 1) = %s" % (d, slope),
                      F(4, 3) * (3 * d * d - 1) == slope)
        g.assert_true("d=%s: the exact central difference is P'(d) + (4/3)h^2" % d,
                      num == slope + F(4, 3) * h * h)
    # the companion below rank one
    for num in range(1, 10):
        m = F(num, 10)
        g.assert_true("m=%s in (0,1): r_m(2) < 0" % m, r_m(m, 2) < 0)
    # and the scan, reported rather than claimed
    N = 160
    scan = {}
    mm = 1
    while mm <= 60:
        m = mm / 10.0
        c = theta_pow_series(m, N)
        first = None
        for n in range(1, N + 1):
            if c[n] < -1e-7:
                first = n
                break
        scan["%.1f" % m] = first
        mm += 1
    for m_str, first in scan.items():
        m = float(m_str)
        if abs(m - round(m)) < 1e-12:
            g.assert_true("m=%s (integer): no negative coefficient up to n=%d" % (m_str, N),
                          first is None)
        elif m < 4.0:
            g.assert_true("m=%s (non-integer, below the Lagrange threshold): a negative "
                          "coefficient appears" % m_str, first is not None)
    g.tables = {"first_n_with_a_negative_coefficient": scan,
                "scan_note": "an observation on a grid to n = %d, not a theorem: every "
                             "non-integer m below 4 has a negative coefficient (at n = 2, 3, 7 "
                             "on (0,1), (1,2), (2,3) respectively), and none was found at or "
                             "above m = 4, the Lagrange four-square threshold. Only the two "
                             "exact statements above are claimed." % N,
                "consequence": "theta(i t)^m = sum_n r_m(n) e^(-pi n t) is a discrete Laplace "
                               "expansion, so by uniqueness of Laplace transforms a negative "
                               "r_m(n) says exactly that theta(i t)^m is not completely "
                               "monotone: no positive measure, hence no point set."}
    return g.out()


def group_survivors():
    g = Group("G. what does continue: the cusp invariants, at every real d",
              "J_d and 1/zeta(d+1) are positive for every real d > 0, so the scattering matrix "
              "survives the loss of the lattice")
    def J(d, n):
        out = float(n) ** d
        k, p = n, 2
        seen = []
        while p * p <= k:
            if k % p == 0:
                seen.append(p)
                while k % p == 0:
                    k //= p
            p += 1
        if k > 1:
            seen.append(k)
        for q in seen:
            out *= (1.0 - float(q) ** (-d))
        return out
    for d in (0.05, 0.2, 0.5, 0.75, 0.999, 1.0):
        for n in (2, 3, 6, 12, 30, 97, 100):
            g.assert_true("d=%g n=%d: J_d(n) > 0" % (d, n), J(d, n) > 0.0)
        z = zeta(d + 1.0) if d + 1.0 != 1.0 else float("inf")
        g.assert_true("d=%g: 1/zeta(d+1) lies in (0,1)" % d, 0.0 < 1.0 / z < 1.0)
    return g.out()


def group_wall():
    g = Group("H. the wall at rank two: where the second pole crosses",
              "xi has simple poles at 0 and 1 (residues -1 and +1), so the numerator "
              "xi(u-d) = xi(m-u) of the Markov part has exactly two, at p = b = omega + 1/2 "
              "and at p = omega - 1/2. The first is what the Blaschke factor cancels; the "
              "second is in the closed left half-plane exactly when omega <= 1/2, that is "
              "when m = 2 omega + 1 <= 2")
    for e in (1e-3, 1e-4):
        g.add("xi has residue -1 at 0", abs(e * xi(e) + 1.0), 2e-3)
        g.add("xi has residue +1 at 1", abs(e * xi(1.0 + e) - 1.0), 2e-3)
    for om in (F(1, 4), F(1, 2), F(3, 4), F(1), F(3, 2), F(2)):
        d = 2 * om
        b = F(1, 2) + om
        m = d + 1
        p1 = m - b          # from xi(m-u) at m-u = 0, i.e. u = m
        p2 = m - 1 - b      # from xi(m-u) at m-u = 1, i.e. u = m - 1
        g.assert_true("omega=%s: the cancelled pole is at p = b" % om, p1 == b)
        g.assert_true("omega=%s: the other pole is at p = omega - 1/2" % om,
                      p2 == om - F(1, 2))
        g.assert_true("omega=%s: that pole is in the closed left half-plane iff m <= 2"
                      % om, (p2 <= 0) == (m <= 2))
        # in the lattice variable it sits at s = (m-1)/2 = omega, the pole of zeta(2s)
        g.assert_true("omega=%s: in s it is at (m-1)/2 = omega, where zeta(2s) has its pole "
                      "exactly at omega = 1/2" % om, F(m - 1, 2) == om)
    g.tables = {"reading": "the family's cap omega <= 1/2 and the rank cap m <= 2 are the same "
                           "statement, and both are the pole of zeta at 1 reaching the "
                           "boundary Re p = 0. Rank two -- the modular surface, the lattice "
                           "zeta itself comes from -- is the largest rank at which the "
                           "transfer has a single cancelled pole in the right half-plane."}
    return g.out()


def main():
    groups = [group_machinery(), group_scattering(), group_dictionary(), group_residue(),
              group_interpolation(), group_sign(), group_survivors(), group_wall()]
    out = {
        "programme": "check_epstein_scattering.py",
        "investigation": "fractional-dimension",
        "statement": "for every integer d >= 1 the Markov part of the shifted Weil transfer is "
                     "the primitive-Epstein scattering matrix of the space of unimodular "
                     "lattices of rank d + 1, with p -> -p the Epstein functional equation "
                     "s -> m/2 - s; and the point count of that lattice, whose unique analytic "
                     "interpolation is the coefficients of theta^(d+1), is strictly negative at "
                     "n = 3 for every d in the open range (0,1) of the family",
        "consequence": "the family lives in the gap between rank 1 and rank 2, with d = 1 (the "
                       "modular surface, and RH) at its right endpoint; strictly inside, there "
                       "is a scattering matrix but no space",
        "scope": "finite test cases; zeta is evaluated only at REAL arguments, by a convergent "
                 "theta integral; no value off the real axis is computed, no zero is located, "
                 "and nothing here is a positivity certificate",
        "groups": groups,
    }
    out["all_pass"] = all(g["pass"] for g in groups)
    out["total_checks"] = sum(g["cases"] for g in groups)
    print(json.dumps(out, indent=2, sort_keys=False))


if __name__ == "__main__":
    main()
