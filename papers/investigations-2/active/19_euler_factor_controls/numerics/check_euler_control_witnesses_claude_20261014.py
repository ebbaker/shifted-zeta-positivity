#!/usr/bin/env python3
"""Certified Laguerre witnesses for the Euler-factor controls.

14 October 2026. Prepared for Edward Baker with LLM assistance.
Model: Claude Opus 5.5 (configured identifier claude-opus-5-5; the serving
model may differ), Claude Cowork, reasoning effort max.  Internal
certificate, not independent validation.

For c > 0 and a prime p put a = (1/2) log p and

    Phi_{c,p}(u) = Phi(u) + (c/2) [Phi(u + a) + Phi(u - a)],
    H_t(x) = int_0^infty exp(t u^2) Phi_{c,p}(u) cos(x u) du,

with Phi the Riemann theta kernel.  For each listed (c, p, t, x0) the
program encloses H, H', H'' at x0 and proves

    L0 = H'(x0)^2 - H(x0) H''(x0) < 0,

which shows that H_t has a non-real zero, hence Lambda_{c,p} > t.

Method (Part A).  The integrands are even and analytic in the strip
|Im u| < pi/8.  The trapezoid rule on the real line with step h has
error at most 2M/(exp(2 pi b/h) - 1) for any b < pi/8, where M bounds
int |F(u + iv)| du for |v| <= b (Trefethen and Weideman, SIAM Review 56
(2014), Theorem 5.1).  M is bounded by an interval Riemann upper sum of
an explicit majorant on [0, U] and an analytic tail beyond U.  The sum is
truncated at U with an analytic tail bound.  All arithmetic is outward
rounded Decimal interval arithmetic at 60 digits; pi, sin and cos use
Taylor series with explicit remainders; exp and ln use Decimal's
correctly rounded functions widened by one unit in the last place;
square roots of integers are verified by squaring.  Negation uses
copy_negate (exact).  The default Decimal context traps Inexact and
Rounded, so any operation outside the directed-rounding contexts must be
exact or the program stops.

Part B encloses the moments used by the asymptotic theorem of the
manuscript: m_k(t) = int_0^infty exp(t u^2) Phi(u) u^k du for k = 0, 2, 4
and the cosh-weighted fourth moment
mu_4(t, r) = int_0^infty exp(t u^2) Phi(u) u^4 cosh(r u) du,
by the same method, with Phi in place of Phi_{c,p}.

Regression checks (not part of the proof): the pi enclosure is compared
with 70 known digits, and the enclosure of m_0(0) = H_0(0) = xi(1/2)/8 with
an independent 40-digit value of xi(1/2).

Standard library only.  No floating-point number enters a certificate.
Revision of 14 October 2026: after an internal review found that unary
minus on Decimal rounded in the default 28-digit context, negation was made
exact and the default context was set to trap inexact operations.
"""
import argparse
import decimal
import hashlib
import json
import platform
import sys
import time
from decimal import (Context, Decimal, DivisionByZero, Inexact,
                     InvalidOperation, Overflow, ROUND_CEILING, ROUND_FLOOR,
                     ROUND_HALF_EVEN, Rounded)
from fractions import Fraction
from pathlib import Path

PRECISION = 60
_E = dict(Emin=-10**7, Emax=10**7,
          traps=[DivisionByZero, InvalidOperation, Overflow])
DOWN = Context(prec=PRECISION, rounding=ROUND_FLOOR, **_E)
UP = Context(prec=PRECISION, rounding=ROUND_CEILING, **_E)
NEAR = Context(prec=PRECISION, rounding=ROUND_HALF_EVEN, **_E)
TINY = Decimal('1e-40000')   # exp(x) < TINY whenever x < -10**5

# Every rounding in a certificate goes through DOWN, UP or NEAR.  Arithmetic
# in the default context (28 digits, round-half-even) is allowed only when
# it is exact; these traps turn any inexact default-context operation into
# an exception instead of a silent rounding.
decimal.getcontext().traps[Inexact] = True
decimal.getcontext().traps[Rounded] = True


class Iv:
    """Closed interval [lo, hi] of Decimals, rounded outward at every step."""
    __slots__ = ('lo', 'hi')

    def __init__(self, lo, hi=None):
        self.lo = Decimal(lo)
        self.hi = self.lo if hi is None else Decimal(hi)
        if not self.lo <= self.hi:
            raise ValueError('empty interval')

    @staticmethod
    def of(v):
        return v if isinstance(v, Iv) else Iv(v)

    @staticmethod
    def frac(q):
        q = Fraction(q)
        n, d = Decimal(q.numerator), Decimal(q.denominator)
        return Iv(DOWN.divide(n, d), UP.divide(n, d))

    def __add__(self, o):
        o = Iv.of(o)
        return Iv(DOWN.add(self.lo, o.lo), UP.add(self.hi, o.hi))
    __radd__ = __add__

    def __neg__(self):
        return Iv(self.hi.copy_negate(), self.lo.copy_negate())

    def __sub__(self, o):
        return self + (-Iv.of(o))

    def __rsub__(self, o):
        return Iv.of(o) + (-self)

    def __mul__(self, o):
        o = Iv.of(o)
        xs = (self.lo, self.hi)
        ys = (o.lo, o.hi)
        return Iv(min(DOWN.multiply(x, y) for x in xs for y in ys),
                  max(UP.multiply(x, y) for x in xs for y in ys))
    __rmul__ = __mul__

    def recip(self):
        if self.lo <= 0 <= self.hi:
            raise ZeroDivisionError('interval contains zero')
        return Iv(DOWN.divide(Decimal(1), self.hi), UP.divide(Decimal(1), self.lo))

    def __truediv__(self, o):
        return self * Iv.of(o).recip()

    def __rtruediv__(self, o):
        return Iv.of(o) * self.recip()

    def sq(self):
        if self.lo >= 0:
            return Iv(DOWN.multiply(self.lo, self.lo), UP.multiply(self.hi, self.hi))
        if self.hi <= 0:
            return Iv(DOWN.multiply(self.hi, self.hi), UP.multiply(self.lo, self.lo))
        m = max(self.lo.copy_negate(), self.hi)
        return Iv(Decimal(0), UP.multiply(m, m))

    def __pow__(self, n):
        assert isinstance(n, int) and n >= 1
        out = self
        for _ in range(n - 1):
            out = out * self
        return out

    def pad(self, e):
        e = Decimal(e)
        assert e >= 0
        return Iv(DOWN.subtract(self.lo, e), UP.add(self.hi, e))

    def absmax(self):
        return max(self.lo.copy_negate(), self.hi)

    def contains_zero(self):
        return self.lo <= 0 <= self.hi

    def mid(self):
        return NEAR.divide(NEAR.add(self.lo, self.hi), Decimal(2))

    def width(self):
        return UP.subtract(self.hi, self.lo)

    def s(self):
        return [str(self.lo), str(self.hi)]


def exp_iv(x):
    x = Iv.of(x)
    if x.hi < -100000:
        return Iv(0, TINY)
    lo = Decimal(0) if x.lo < -100000 else NEAR.exp(x.lo).next_minus(NEAR)
    hi = NEAR.exp(x.hi).next_plus(NEAR)
    return Iv(max(lo, Decimal(0)), hi)


def ln_iv(x):
    x = Iv.of(x)
    assert x.lo > 0
    return Iv(NEAR.ln(x.lo).next_minus(NEAR), NEAR.ln(x.hi).next_plus(NEAR))


def sqrt_int(n):
    """Verified enclosure of sqrt(n) for a positive integer n."""
    n = Decimal(n)
    s = NEAR.sqrt(n)
    lo, hi = s.next_minus(NEAR), s.next_plus(NEAR)
    assert UP.multiply(lo, lo) <= n <= DOWN.multiply(hi, hi)
    return Iv(lo, hi)


def sqrt_iv(x):
    """Verified enclosure of sqrt of a nonnegative interval."""
    x = Iv.of(x)
    assert x.lo >= 0
    lo = NEAR.sqrt(x.lo).next_minus(NEAR) if x.lo > 0 else Decimal(0)
    hi = NEAR.sqrt(x.hi).next_plus(NEAR)
    lo = max(lo, Decimal(0))
    assert UP.multiply(lo, lo) <= x.lo and DOWN.multiply(hi, hi) >= x.hi
    return Iv(lo, hi)


def atan_small(x, terms=100):
    """Alternating Taylor enclosure of arctan on 0 <= x < 1."""
    x = Iv.of(x)
    assert 0 <= x.lo and x.hi < 1
    total, term, x2 = Iv(0), x, x.sq()
    for k in range(terms):
        total = total + (term if k % 2 == 0 else -term) / (2 * k + 1)
        term = term * x2
    return total.pad((term / (2 * terms + 1)).hi)


def pi_iv():
    # Machin: pi/4 = 4 arctan(1/5) - arctan(1/239), checked exactly.
    z = Fraction(1, 5)
    two = 2 * z / (1 - z * z)
    four = 2 * two / (1 - two * two)
    assert (four - Fraction(1, 239)) / (1 + four / 239) == 1
    return 16 * atan_small(Iv.frac(Fraction(1, 5))) - 4 * atan_small(Iv.frac(Fraction(1, 239)))


PI = pi_iv()
TWO_PI = 2 * PI

# Regression check, not part of the proof: 70 known decimals of pi, so that
# PI_REF < pi < PI_REF + 1e-70.
PI_REF = Decimal('3.1415926535897932384626433832795028841971693993751058209749445923078164')
assert PI.lo <= UP.add(PI_REF, Decimal('1e-70')) and PI.hi >= PI_REF
assert PI.width() < Decimal('1e-55')
# Independent value of xi(1/2) (mpmath, 60 digits, rounded to 40 significant
# digits); m_0(0) = H_0(0) = xi(1/2)/8 is checked against it in main().
XI_HALF = Decimal('0.4971207781883141099127737396853977198073')


def sincos(theta, terms=48):
    """Enclosures of (sin, cos) of an interval theta, after reduction by 2 pi."""
    theta = Iv.of(theta)
    m = int(NEAR.divide(theta.mid(), TWO_PI.mid()).to_integral_value())
    r = theta - TWO_PI * m
    assert r.absmax() <= Decimal('3.2')
    r2 = r.sq()
    s_tot, c_tot = Iv(0), Iv(0)
    s_term, c_term = r, Iv(1)
    for k in range(terms):
        if k % 2 == 0:
            s_tot, c_tot = s_tot + s_term, c_tot + c_term
        else:
            s_tot, c_tot = s_tot - s_term, c_tot - c_term
        s_term = s_term * r2 / ((2 * k + 2) * (2 * k + 3))
        c_term = c_term * r2 / ((2 * k + 1) * (2 * k + 2))
    # Lagrange remainders: |r|^(2N+1)/(2N+1)! and |r|^(2N)/(2N)!.
    bound = max(s_term.absmax(), c_term.absmax())
    s_tot, c_tot = s_tot.pad(bound), c_tot.pad(bound)
    clip = lambda v: Iv(max(v.lo, Decimal(-1)), min(v.hi, Decimal(1)))
    return clip(s_tot), clip(c_tot)


# ---------------------------------------------------------------------------
# The theta kernel.  For r >= 0 write E_k = exp(k r).  Then
#   Phi(r) = sum_n (2 pi^2 n^4 E9 - 3 pi n^2 E5) exp(-pi n^2 E4).
# The strip majorant replaces the bracket by its absolute value and E4 by
# kappa*E4 with kappa = cos(4b) <= cos(4 Im w), see the manuscript.
NTERMS = 8
C_NT = 2 * PI.sq() + 3 * PI          # 2 pi^2 + 3 pi


def _tail(E4, E9, kappa):
    """Bound for sum over n > NTERMS of (2 pi^2 n^4 E9 + 3 pi n^2 E5) e^{-pi kappa n^2 E4}.

    Uses E5 <= E9 (r >= 0), n^2 <= n^4, and the ratio bound
    ((n+1)/n)^4 exp(-pi kappa (2n+1) E4) <= (10/9)^4 exp(-19 pi kappa E4) for n >= 9.
    """
    first = C_NT * 9 ** 4 * E9 * exp_iv(-81 * PI * kappa * E4)
    ratio = Iv.frac(Fraction(10, 9) ** 4) * exp_iv(-19 * PI * kappa * E4)
    assert ratio.hi < 1
    return (first / (1 - ratio)).hi


def phi_value(E4, E5, E9):
    total = Iv(0)
    for n in range(1, NTERMS + 1):
        c = PI * (n * n)
        total = total + (2 * c.sq() * E9 - 3 * c * E5) * exp_iv(-c * E4)
    return total.pad(_tail(E4, E9, Iv(1)))


def phi_majorant(E4, E5, E9, kappa):
    total = Iv(0)
    for n in range(1, NTERMS + 1):
        c = PI * (n * n)
        total = total + (2 * c.sq() * E9 + 3 * c * E5) * exp_iv(-c * kappa * E4)
    return Iv(total.lo, (total + _tail(E4, E9, kappa)).hi)


def e_powers(r):
    """(E4, E5, E9) = (e^{4r}, e^{5r}, e^{9r}) for an interval r >= 0."""
    r = Iv.of(r)
    assert r.lo >= 0
    return exp_iv(4 * r), exp_iv(5 * r), exp_iv(9 * r)


class Control:
    """Exact-shift evaluation of Phi_{c,p} at grid points u >= 0.

    Phi(u + a) uses e^{4(u+a)} = p^2 e^{4u}, e^{5(u+a)} = p^{5/2} e^{5u},
    e^{9(u+a)} = p^{9/2} e^{9u}; Phi(u - a) = Phi(|u - a|) similarly.
    """

    def __init__(self, c, p):
        self.c = Iv.frac(c)
        self.p = p
        self.sp = sqrt_int(p)
        self.p2 = Iv(p * p)
        self.p52 = self.p2 * self.sp
        self.p92 = Iv(p ** 4) * self.sp
        self.a = ln_iv(Iv(p)) / 2

    def value(self, u):
        E4, E5, E9 = e_powers(u)
        base = phi_value(E4, E5, E9)
        plus = phi_value(E4 * self.p2, E5 * self.p52, E9 * self.p92)
        e2 = exp_iv(2 * Iv(u))
        if e2.lo > self.p:            # u > a
            minus = phi_value(E4 / self.p2, E5 / self.p52, E9 / self.p92)
        elif e2.hi < self.p:          # u < a
            minus = phi_value(self.p2 / E4, self.p52 / E5, self.p92 / E9)
        else:
            raise ArithmeticError('grid point too close to a')
        return base + self.c / 2 * (plus + minus)

    def majorant(self, cell, kappa):
        """Upper bound on |Phi_{c,p}(w)| for Re w in cell (cell >= 0), |Im w| <= b."""
        u = Iv.of(cell)
        base = phi_majorant(*e_powers(u), kappa)
        plus = phi_majorant(*e_powers(u + self.a), kappa)
        lo = max(Decimal(0), DOWN.subtract(u.lo, self.a.hi), DOWN.subtract(self.a.lo, u.hi))
        hi = max(UP.subtract(u.hi, self.a.lo), UP.subtract(self.a.hi, u.lo))
        minus = phi_majorant(*e_powers(Iv(lo, hi)), kappa)
        return (base + self.c / 2 * (plus + minus)).hi


class Theta:
    """Phi itself (c = 0), with the same interface."""

    def __init__(self):
        self.c = Iv(0)
        self.a = Iv(0)

    def value(self, u):
        return phi_value(*e_powers(u))

    def majorant(self, cell, kappa):
        return phi_majorant(*e_powers(Iv.of(cell)), kappa).hi


B_STRIP = Decimal('0.3')              # strip half-width b < pi/8
CELL = Decimal(1) / 16                # Riemann cells for the strip majorant


def analytic_tail(a_hi, c, cosh_xb, weight_exp, prefactor=Decimal(1)):
    """Bound for int_U^infty of the strip majorant, U = a + 2.

    For u >= U every argument r of Phi satisfies r >= u - a >= 2.  There
    sum_n n^4 exp(-pi kappa (n^2 - 1) e^{4r}) <= 2, so each Phi-majorant is
    at most 2 (2 pi^2 + 3 pi) exp(9 s' - pi kappa e^{4 s'}), s' = u - a,
    a decreasing function for s' >= 2.  The polynomial, Gaussian and
    cosh weights are at most exp(weight_exp * u^2) with weight_exp <= 2,
    u^2 <= 2 s^2 + 2 (a + 2)^2 for s = u - a - 2, and
    e^{4s'} >= e^8 (1 + 4 s + 8 s^2).  With A = pi kappa e^8 the integrand
    is at most K exp(-(4A - 9) s), K as below.  A weight that is only
    bounded by prefactor * exp(2 u^2) is handled by the prefactor.
    """
    kappa = KAPPA.lo
    A = PI * kappa * exp_iv(8)
    assert weight_exp <= 2
    K = (Iv(prefactor) * Iv(cosh_xb) * (1 + Iv(c)) * 2 * C_NT
         * exp_iv(4 * (Iv(a_hi) + 2).sq() + 18 - A))
    return (K / (4 * A - 9)).hi


KAPPA = sincos(4 * B_STRIP)[1]        # cos(4b) for b = 0.3
assert KAPPA.lo > Decimal('0.36')


def strip_majorant(source, weight, U, cosh_xb, c_iv, prefactor=Decimal(1)):
    """Upper bound for int_R sup_{|v|<=b} |F(u+iv)| du with |F| <= weight(u) |Phi_{c,p}|.

    weight(cell) returns an interval upper bound of the polynomial/Gaussian
    factor on the cell.  Riemann upper sum on [0, U] with cells of width
    1/16, doubled by evenness, plus the analytic tail.
    """
    total = Iv(0)
    n_cells = int((U / CELL).to_integral_value(rounding=ROUND_CEILING))
    for i in range(n_cells):
        cell = Iv(CELL * i, CELL * (i + 1))
        total = total + CELL * weight(cell) * source.majorant(cell, KAPPA.lo) * cosh_xb
    tail = analytic_tail(source.a.hi, c_iv.hi, cosh_xb, 2, prefactor)
    return (2 * (total + tail)).hi


def trapezoid_jets(source, t, x, h, U):
    """Half-line trapezoid sums for H, H', H'' and their rigorous errors."""
    t, x, h = Decimal(t), Decimal(x), Decimal(h)
    K = int((U / h).to_integral_value(rounding=ROUND_CEILING))
    U_grid = h * K                     # exact: h = 1/64 or 1/32
    tI, xI = Iv(t), Iv(x)
    sums = [Iv(0), Iv(0), Iv(0)]
    for k in range(K + 1):
        u = h * k                      # exact grid point
        uI = Iv(u)
        w = exp_iv(tI * uI.sq()) * source.value(u)
        s, c = sincos(xI * uI)
        wt = h / 2 if k == 0 else h
        sums[0] = sums[0] + wt * w * c
        sums[1] = sums[1] - wt * (uI * w * s)
        sums[2] = sums[2] - wt * (uI.sq() * w * c)
    b = B_STRIP
    xb = xI * b
    cosh_xb = (exp_iv(xb) + exp_iv(-xb)) / 2
    gauss = lambda cell: exp_iv(t * cell.sq())
    weights = [lambda cell: gauss(cell),
               lambda cell: gauss(cell) * (cell + b),
               lambda cell: gauss(cell) * (cell.sq() + b * b)]
    discretization = []
    tails = []
    denom = exp_iv(2 * PI * b / h) - 1
    for j in range(3):
        M = strip_majorant(source, weights[j], U_grid, cosh_xb.hi, source.c)
        discretization.append((Iv(M) / denom).hi)
        tails.append(analytic_tail(source.a.hi, source.c.hi, cosh_xb.hi, 2))
    jets = [sums[j].pad(UP.add(discretization[j], tails[j])) for j in range(3)]
    return jets, {'grid_points': K + 1, 'U': str(U_grid), 'h': str(h),
                  'discretization_bounds': [str(v) for v in discretization],
                  'truncation_bounds': [str(v) for v in tails]}


# Witness table: (c, p, t, x0).  x0 is a point near the real part of the
# lowest off-line pair; any point with L0 < 0 suffices.
WITNESSES = [
    ('1/2', 2, '0.2', '9.0194'),
    ('1/2', 3, '0.2', '5.6906'),
    ('1/2', 5, '0.2', '3.8844'),
    ('1/2', 7, '0.2', '3.2128'),
    ('1/2', 11, '0.2', '2.6072'),
    ('1/2', 13, '0.2', '2.4374'),
    ('1/2', 17, '0.2', '2.2066'),
    ('1/2', 19, '0.2', '2.1232'),
    ('1/2', 23, '0.2', '1.9939'),
    ('1/2', 29, '0.2', '1.8566'),
    ('1/2', 31, '0.2', '1.8206'),
    ('1/2', 37, '0.2', '1.7314'),
    ('1/2', 41, '0.2', '1.6835'),
    ('1/2', 43, '0.1787854', '1.6622'),
    ('1/2', 47, '0.1787854', '1.6238'),
]


def certify(c, p, t, x0, h, cross_h=None):
    source = Control(Fraction(c), p)
    # U = smallest multiple of 1/64 strictly above an upper bound for a + 2.
    n = UP.multiply(UP.add(source.a.hi, Decimal(2)), Decimal(64))
    U = Decimal(int(n.to_integral_value(rounding=ROUND_FLOOR)) + 1) / 64
    assert U > UP.add(source.a.hi, Decimal(2))
    start = time.perf_counter()
    jets, info = trapezoid_jets(source, t, x0, h, U)
    H, H1, H2 = jets
    L0 = H1.sq() - H * H2
    out = {
        'c': c, 'p': p, 't': t, 'x0': x0,
        'a_enclosure': source.a.s(),
        'H': H.s(), 'H_x': H1.s(), 'H_xx': H2.s(),
        'L0': L0.s(),
        'L0_upper_bound': str(L0.hi),
        'certified_L0_negative': L0.hi < 0,
        'quadrature': info,
    }
    if not H.contains_zero():
        out['L0_over_H2'] = (L0 / H.sq()).s()
    if cross_h is not None:
        jets2, info2 = trapezoid_jets(source, t, x0, cross_h, U)
        overlap = all(max(A.lo, B.lo) <= min(A.hi, B.hi) for A, B in zip(jets, jets2))
        out['cross_check'] = {'h': str(cross_h), 'enclosures_overlap': overlap,
                              'H': jets2[0].s()}
        assert overlap
    out['seconds'] = round(time.perf_counter() - start, 3)
    return out


# ---------------------------------------------------------------------------
# Part B: moments of the theta kernel for the asymptotic theorem.

def theta_moments(t, r, h=Decimal(1) / 64):
    """Enclose m_0, m_2, m_4 at time t and mu_4(t, r) (cosh weight)."""
    source = Theta()
    t, r = Decimal(t), Decimal(r)
    U = Decimal(3)
    K = int((U / h).to_integral_value(rounding=ROUND_CEILING))
    sums = [Iv(0), Iv(0), Iv(0), Iv(0)]
    tI, rI = Iv(t), Iv(r)
    for k in range(K + 1):
        u = h * k                      # exact grid point
        uI = Iv(u)
        u2 = uI.sq()
        w = exp_iv(tI * u2) * source.value(u)
        wt = h / 2 if k == 0 else h
        ru = rI * uI
        ch = (exp_iv(ru) + exp_iv(-ru)) / 2
        sums[0] = sums[0] + wt * w
        sums[1] = sums[1] + wt * u2 * w
        sums[2] = sums[2] + wt * u2.sq() * w
        sums[3] = sums[3] + wt * u2.sq() * ch * w
    b = B_STRIP
    gauss = lambda cell: exp_iv(t * cell.sq())
    weights = [gauss,
               lambda cell: gauss(cell) * (cell.sq() + b * b),
               lambda cell: gauss(cell) * (cell.sq() + b * b).sq(),
               lambda cell: gauss(cell) * (cell.sq() + b * b).sq() * exp_iv(r * cell)]
    denom = exp_iv(2 * PI * b / h) - 1
    out = []
    # Weights: (u^2+b^2)^2 <= e^{u^2}, e^{t u^2} <= e^{u^2/4} (t <= 1/4) and
    # e^{r u} <= e^{u^2/2 + r^2/2}; so every weight is <= e^{r^2/2} e^{2 u^2}.
    assert t <= Decimal('0.25') and r <= 3
    pref = exp_iv(rI.sq() / 2).hi
    for j in range(4):
        M = strip_majorant(source, weights[j], U, Decimal(1), source.c, pref)
        err = UP.add((Iv(M) / denom).hi,
                     analytic_tail(Decimal(0), Decimal(0), Decimal(1), 2, pref))
        out.append(sums[j].pad(err))
    return out


# ---------------------------------------------------------------------------
# Part C: the explicit inequality (W') of the asymptotic theorem.
#
# With k0 = m2(0)/m0(0) = S2/2, kbar >= m2(t)/m0(t), dbar >= m4(t)/m0(t) and
# mubar >= mu4(t, R)/m0(t) for 0 <= t <= 1/4 and R <= 3, the manuscript shows
# that L0(H^{c,p}_t; pi/a) < 0 at t = t_m - S2 t_m^2 - Q/a^6 whenever
#   Q > s^2/2 + kbar pi^2 s/2 + 2 dbar tau0^3 + mubar (pi^4 + P^2)/24 + D1^2/F2,
# s = 2 k0 tau0^2 + Q eps, eps = 1/a^2, P = pi^2 + 4 tau0^2,
# D1 = kbar pi (1 + 2 tau0) + mubar (pi^3/6 + P^2/24 + P^{3/2}/6) eps,
# D2 = pi^2/2 + P^2/24 + P^{3/2}/3 + P/2,
# F2 = exp(-eps s) - kbar eps (1 + pi^2/2) - mubar D2 eps^2 > 0.
# Every term on the right increases with tau0 and eps, so checking the
# largest tau0 and eps of a regime proves the whole regime.

STATED = {'kbar': '0.0116463', 'dbar': '0.000378', 'mubar': '0.00046792'}

REGIMES = [
    {'name': 'c in [1/2, 1), p >= 29', 'tau0_max': 'ln2', 'p_min': 29, 'Q': Fraction(1, 50)},
    {'name': 'c in [exp(-2), 1), p >= 293', 'tau0_max': '2', 'p_min': 293, 'Q': Fraction(1, 10)},
]


def check_regimes(m_t0, m_tq):
    m0, m2, _, _ = m_t0
    _, m2q, m4q, mu4q = m_tq
    k0 = m2 / m0
    kbar_cert = Iv(m2q.hi) / Iv(m0.lo)
    dbar_cert = Iv(m4q.hi) / Iv(m0.lo)
    mubar_cert = Iv(mu4q.hi) / Iv(m0.lo)
    # The manuscript states rounded-up constants; check that they dominate
    # the certified ratios, and use the stated values in (W').
    kbar, dbar, mubar = Iv(STATED['kbar']), Iv(STATED['dbar']), Iv(STATED['mubar'])
    assert kbar_cert.hi <= kbar.lo and dbar_cert.hi <= dbar.lo and mubar_cert.hi <= mubar.lo
    widths = {name: str(v.width()) for name, v in (('m0(0)', m0), ('m2(0)', m2), ('m2(1/4)', m2q),
                                                     ('m4(1/4)', m4q), ('mu4(1/4,3)', mu4q))}
    out = {'k0': k0.s(), 'S2': (2 * k0).s(), 'kbar_certified_upper': str(kbar_cert.hi),
           'dbar_certified_upper': str(dbar_cert.hi), 'mubar_certified_upper': str(mubar_cert.hi),
           'stated_constants': dict(STATED), 'moment_enclosure_widths': widths, 'regimes': []}
    for reg in REGIMES:
        tau0 = ln_iv(Iv(2)) if reg['tau0_max'] == 'ln2' else Iv(reg['tau0_max'])
        tau0 = Iv(tau0.hi)
        eps = Iv(4) / ln_iv(Iv(reg['p_min'])).sq()
        eps = Iv(eps.hi)
        Q = Iv.frac(reg['Q'])
        tmax = tau0 * eps
        P = PI.sq() + 4 * tau0.sq()
        R2 = P * eps
        assert tmax.hi <= Decimal('0.25') and R2.hi <= 9
        sP = sqrt_iv(P)
        P32 = P * sP
        s = 2 * Iv(k0.hi) * tau0.sq() + Q * eps
        D1 = kbar * PI * (1 + 2 * tau0) + mubar * (PI ** 3 / 6 + P.sq() / 24 + P32 / 6) * eps
        D2 = PI.sq() / 2 + P.sq() / 24 + P32 / 3 + P / 2
        F2 = exp_iv(-(eps * s)) - kbar * eps * (1 + PI.sq() / 2) - mubar * D2 * eps.sq()
        assert F2.lo > 0
        rhs = (s.sq() / 2 + kbar * PI.sq() * s / 2 + 2 * dbar * tau0 ** 3
               + mubar * (PI ** 4 + P.sq()) / 24 + D1.sq() / F2)
        ok = Q.lo > rhs.hi
        out['regimes'].append({'name': reg['name'], 'tau0_max': str(tau0.hi), 'p_min': reg['p_min'],
                               'eps_max': str(eps.hi), 't_max': str(tmax.hi), 'R_max_squared': str(R2.hi),
                               'Q': str(reg['Q']), 'right_side_upper': str(rhs.hi),
                               'F2_lower': str(F2.lo), 'inequality_holds': ok})
        assert ok, reg['name']
    return out


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('--output', type=Path)
    parser.add_argument('--quick', action='store_true', help='only p = 41, no cross-check')
    args = parser.parse_args()
    start = time.perf_counter()
    h = Decimal(1) / 64
    cases = [w for w in WITNESSES if not args.quick or w[1] == 41]
    results = []
    for c, p, t, x0 in cases:
        res = certify(c, p, t, x0, h, None if args.quick else Decimal(1) / 32)
        results.append(res)
        print(f"c={c} p={p:>2} t={t:<9} x0={x0:<7} L0<= {float(res['L0_upper_bound']):.4e}"
              f"  certified={res['certified_L0_negative']}  ({res['seconds']} s)", flush=True)
    ok = all(r['certified_L0_negative'] for r in results)
    record = {
        'title': 'Certified Laguerre witnesses for Euler-factor controls',
        'date': '2026-10-14',
        'prepared_for': 'Edward Baker',
        'model': 'Claude Opus 5.5 (claude-opus-5-5; serving model may differ), Claude Cowork, reasoning effort max',
        'status': 'PASS' if ok else 'FAIL',
        'statement': 'For each case, L0(H^{c,p}_t; x0) < 0, hence H^{c,p}_t has a non-real zero and Lambda_{c,p} > t.',
        'arithmetic': {'decimal_digits': PRECISION,
                       'rounding': 'outward (floor/ceiling); exp/ln widened by one ulp; negation exact '
                                   '(copy_negate); default context traps Inexact and Rounded',
                       'pi_enclosure': PI.s(), 'strip_halfwidth_b': str(B_STRIP),
                       'cos4b_enclosure': KAPPA.s(), 'theta_terms_explicit': NTERMS,
                       'riemann_cell_width': str(CELL)},
        'quadrature': 'Half-line trapezoid sums of even integrands with strip error bound M/(exp(2 pi b/h)-1) '
                      'and analytic truncation tail; h = 1/64, cross-check h = 1/32',
        'cases': results,
        'python_version': platform.python_version(),
        'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'runtime_seconds': round(time.perf_counter() - start, 1),
    }
    if not args.quick:
        moments, computed = {}, {}
        for t, r in (('0', '0'), ('0.25', '3')):
            computed[(t, r)] = theta_moments(t, r)
            m0, m2, m4, mu4 = computed[(t, r)]
            moments[f't={t},r={r}'] = {'m0': m0.s(), 'm2': m2.s(), 'm4': m4.s(), 'mu4': mu4.s()}
        record['theta_moments'] = moments
        m0 = computed[('0', '0')][0]
        xi8 = Iv(XI_HALF).pad(Decimal('1e-40')) / 8
        xi_ok = max(m0.lo, xi8.lo) <= min(m0.hi, xi8.hi)
        record['regression_checks'] = {
            'pi_matches_70_known_decimals': True,
            'm0(0)_consistent_with_xi(1/2)/8': xi_ok,
            'xi(1/2)_reference': str(XI_HALF)}
        assert xi_ok
        record['asymptotic_theorem_check'] = check_regimes(computed[('0', '0')], computed[('0.25', '3')])
        print(json.dumps({r['name']: [r['Q'], r['right_side_upper'][:12]]
                          for r in record['asymptotic_theorem_check']['regimes']}))
    text = json.dumps(record, indent=1, sort_keys=True) + '\n'
    if args.output:
        args.output.write_text(text)
    print(json.dumps({'status': record['status'], 'cases': len(results),
                      'runtime_seconds': record['runtime_seconds']}))
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
