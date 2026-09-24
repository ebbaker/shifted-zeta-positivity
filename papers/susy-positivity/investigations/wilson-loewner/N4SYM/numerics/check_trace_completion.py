#!/usr/bin/env python3
"""Growing Loewner trace in N=4 SYM: scaling, completion and first equation.

Companion to N4SYM/notes/STRAIGHT_LINE_RESPONSE_AND_TRACE_COMPLETION_20260923.md.
Prepared for Edward Baker by Claude Opus 5.5 (Anthropic; model identifier
claude-opus-5-5 as reported by the runtime; reasoning effort not exposed).

Standard library only; prints one JSON object (or writes --output FILE).
Deterministic. No zeta function is evaluated. Floating cases are
diagnostics of analytic statements, not interval certificates; the
classical background below is a test connection, not a sample of the
quantum measure.

Groups
  T1  linear-driver tip: exact Gaussian-rational series and the implicit
      relation a q + 2 log(1 - a q/2) = a^2 t;
  T2  Loewner scaling q_a(T r) = sqrt(T) q_{a sqrt T}(r);
  T3  sliver geometry of trace + straight chord: width (s/6) y (2 - y),
      cusp opening s/3, with s = a sqrt(t);
  T4  one-loop Maldacena-Wilson trace-chord exchange: constant scalar
      direction grows like 1/s, flipped return direction is O(s);
  T5  exact first evolution equation for the chord-completed transport
      with constant or flipped return scalar, checked by finite
      differences of direct transports on a noncommuting SU(2)
      gauge+scalar background; a = 0 controls; gauge covariance;
      leading short-time behaviour of the classical transport.
"""
from fractions import Fraction as Fr
import argparse
import cmath
import json
import math

CASES = []


def case(name, group, kind, value, threshold, comparison='<=', note=''):
    value = float(value)
    passed = value <= threshold if comparison == '<=' else value >= threshold
    CASES.append(dict(name=name, group=group, kind=kind, value=value,
                      threshold=threshold, comparison=comparison,
                      passed=bool(passed), note=note))


# ------------------------------------------------------------- quadrature
def gauss_legendre(n):
    nodes, weights = [], []
    for i in range(1, n + 1):
        x = math.cos(math.pi * (i - 0.25) / (n + 0.5))
        for _ in range(100):
            p0, p1 = 1.0, x
            for k in range(2, n + 1):
                p0, p1 = p1, ((2 * k - 1) * x * p1 - (k - 1) * p0) / k
            dp = n * (x * p1 - p0) / (x * x - 1.0)
            dx = p1 / dp
            x -= dx
            if abs(dx) < 1e-16:
                break
        nodes.append(x)
        weights.append(2.0 / ((1.0 - x * x) * dp * dp))
    return nodes, weights


GL16 = gauss_legendre(16)


def integrate_edges(f, edges):
    nodes, weights = GL16
    total = 0.0
    for lo, hi in zip(edges[:-1], edges[1:]):
        h = hi - lo
        for x, w in zip(nodes, weights):
            total += 0.5 * h * w * f(lo + 0.5 * h * (x + 1))
    return total


# ------------------------------------------------------------- T1 tip
class CQ:
    """Gaussian rational re + i im with Fractions."""

    def __init__(self, re, im=0):
        self.re, self.im = Fr(re), Fr(im)

    def __add__(self, o):
        return CQ(self.re + o.re, self.im + o.im)

    def __sub__(self, o):
        return CQ(self.re - o.re, self.im - o.im)

    def __mul__(self, o):
        return CQ(self.re * o.re - self.im * o.im, self.re * o.im + self.im * o.re)

    def scale(self, f):
        return CQ(self.re * f, self.im * f)

    def inv(self):
        d = self.re ** 2 + self.im ** 2
        return CQ(self.re / d, -self.im / d)

    def eq(self, re, im):
        return self.re == Fr(re) and self.im == Fr(im)

    def c(self):
        return complex(float(self.re), float(self.im))


def tip_series(nterms=8):
    """q(t) = sum_n g_n a^(n-1) t^(n/2) from q q' = 2 a sigma q - 4 sigma, sigma = sqrt t.

    With q = sum c_n sigma^n (c_n = g_n a^(n-1)), the sigma^(m) coefficient of
    q q' is sum_{i+j=m+1} c_i j c_j; the right side gives 2 a c_{m-1} at
    order m >= 2 and -4 at order 1.  Take a = 1 (powers of a are fixed by
    the scaling a -> a sqrt(T)); the branch is c_1 = 2i.
    """
    c = {1: CQ(0, 2)}
    for m in range(2, nterms + 1):
        # coefficient of sigma^m on the left: sum_{i+j=m+1} i? use q q' = (1/2) d/dsigma (q^2)
        # (1/2) d(q^2)/dsigma at order sigma^m = (m+1)/2 * [q^2]_{m+1}
        # [q^2]_{m+1} = sum_{i+j=m+1} c_i c_j involves c_m through 2 c_1 c_m.
        known = CQ(0)
        for i in range(2, m):
            j = m + 1 - i
            if 1 <= j < m:
                known = known + c[i] * c[j]
        rhs = c[m - 1].scale(2)  # 2 a sigma q at order sigma^m
        # (m+1)/2 * (2 c_1 c_m + known) = rhs  (m >= 2)
        target = rhs.scale(Fr(2, m + 1)) - known
        c[m] = target * (c[1].scale(2)).inv()
    return c


_SERIES = tip_series(12)
_SERIES_C = {n: c.c() for n, c in _SERIES.items()}


def solve_tip(a, t):
    """Tip of the linear-driver trace. For s = |a| sqrt(t) < 0.05 the exact
    12-term series is used (truncation below 1e-19 relative); the implicit
    relation is ill-conditioned there because q + 2 log(1 - q a/2) cancels
    to O(q^2). Otherwise Newton's method from the series."""
    if t == 0:
        return 0j
    if a == 0:
        return 2j * math.sqrt(t)
    sq = math.sqrt(t)
    q = sum(_SERIES_C[n] * a ** (n - 1) * sq ** n for n in _SERIES_C)
    if abs(a) * sq < 0.05:
        return q
    for _ in range(60):
        F = a * q + 2 * cmath.log(1 - a * q / 2) - a * a * t
        dF = a - a / (1 - a * q / 2)
        dq = F / dF
        q -= dq
        if abs(dq) < 1e-16 * max(1.0, abs(q)):
            break
    return q


def t1_tip():
    ser = tip_series(8)
    want = {1: (0, 2), 2: (Fr(2, 3), 0), 3: (0, Fr(-1, 18)), 4: (Fr(1, 135), 0)}
    for n, (re, im) in want.items():
        case(f'T1 exact tip coefficient c_{n} (parent note eq. 16)', 'T1', 'exact',
             0.0 if ser[n].eq(re, im) else 1.0, 0.0)
    worst = 0.0
    for a in (1.0, -0.7, 2.5):
        for t in (1e-4, 1e-2, 0.04):
            q = solve_tip(a, t)
            worst = max(worst, abs(a * q + 2 * cmath.log(1 - a * q / 2) - a * a * t))
            case(f'T1 tip in upper half plane a={a:g}, t={t:g}', 'T1', 'floating', q.imag, 0.0, '>=')
    case('T1 implicit relation residual', 'T1', 'floating', worst, 1e-14)
    # Independent re-derivation agrees with the parent's recorded coefficients
    # (growing-trace-hierarchy-20260921.json, 'geometry_coefficients_sqrt_time').
    parent = {5: (0, Fr(1, 2160)), 6: (Fr(1, 8505), 0), 7: (0, Fr(139, 2721600)),
              8: (Fr(-1, 102060), 0), 9: (0, Fr(-571, 1175731200)), 10: (Fr(-281, 757795500), 0),
              11: (0, Fr(-163879, 1086375628800)), 12: (Fr(5221, 177324147000), 0)}
    ser12 = tip_series(12)
    mism = sum(0 if ser12[n].eq(re, im) else 1 for n, (re, im) in parent.items())
    case('T1 coefficients c_5..c_12 agree with the parent record', 'T1', 'exact', float(mism), 0.0)
    # Series versus Newton where the implicit relation is well conditioned.
    a, t = 1.0, 0.01
    sq = math.sqrt(t)
    qs = sum(ser12[n].c() * a ** (n - 1) * sq ** n for n in ser12)
    case('T1 twelve-term series agrees with Newton root at s = 0.1', 'T1', 'floating',
         abs(qs - solve_tip(a, t)) / abs(qs), 1e-13)


# ------------------------------------------------------------- T2 scaling
def t2_scaling():
    worst = 0.0
    for a in (0.8, -1.3):
        for T in (0.01, 0.2, 0.6):
            for r in (0.1, 0.5, 1.0):
                lhs = solve_tip(a, T * r)
                rhs = math.sqrt(T) * solve_tip(a * math.sqrt(T), r)
                worst = max(worst, abs(lhs - rhs) / abs(lhs))
    case('T2 Loewner scaling q_a(T r) = sqrt(T) q_{a sqrt T}(r)', 'T2', 'floating', worst, 1e-13)


# ------------------------------------------------------------- T3 sliver
def trace_point(s, u):
    """Rescaled trace (t = 1, slope s) at Loewner time u^2, with dq/du."""
    q = solve_tip(s, u * u)
    if u == 0:
        return 0j, 2j
    dq = 2 * u * (s - 2 / q)
    return q, dq


def t3_sliver():
    for s in (0.1, 0.05, 0.025):
        tip = solve_tip(s, 1.0)
        e = tip / abs(tip)
        best = 0.0
        for k in range(1, 400):
            q, _ = trace_point(s, k / 400)
            d = abs((q * e.conjugate()).imag)
            best = max(best, d)
        case(f'T3 max trace-chord width / (s/6) -> 1 at s={s:g}', 'T3', 'floating',
             abs(best / (s / 6) - 1), 1.5 * s)
        # cusp openings at base and tip
        base_angle = abs(cmath.phase(e) - math.pi / 2)
        _, dq = trace_point(s, 1.0)
        tip_angle = abs(cmath.phase(dq) - cmath.phase(e))
        case(f'T3 base cusp opening / (s/3) -> 1 at s={s:g}', 'T3', 'floating',
             abs(base_angle / (s / 3) - 1), 0.5 * s)
        case(f'T3 tip cusp opening / (s/3) -> 1 at s={s:g}', 'T3', 'floating',
             abs(tip_angle / (s / 3) - 1), 1.5 * s)


# ------------------------------------------------------------- T4 one loop
def exchange_integrals(s, eps):
    """J_const, J_flip: trace x chord part of int int (|x'||y'| n.n' - x'.y')/|x-y|^2.

    Both orderings are included (factor 2). Points within distance eps of the
    base or tip are excised on both legs. The chord integral is done in
    closed form; the trace integral by graded Gauss-Legendre in u.
    """
    tip = solve_tip(s, 1.0)
    L = abs(tip)
    e = tip / L

    def dist_base(u):
        return abs(trace_point(s, u)[0]) - eps

    def dist_tip(u):
        return abs(trace_point(s, u)[0] - tip) - eps

    def bisect(f, lo, hi):
        flo = f(lo)
        for _ in range(80):
            mid = 0.5 * (lo + hi)
            if (f(mid) > 0) == (flo > 0):
                lo, flo = mid, f(mid)
            else:
                hi = mid
        return 0.5 * (lo + hi)
    u_lo = bisect(dist_base, 1e-9, 0.5)
    u_hi = bisect(dist_tip, 0.5, 1.0)

    def integrand(u, kind):
        q, dq = trace_point(s, u)
        speed = abs(dq)
        T = dq / speed
        l0 = (q * e.conjugate()).real
        d = abs((q * e.conjugate()).imag)
        inner = (math.atan((L - eps - l0) / d) - math.atan((eps - l0) / d)) / d
        te = (T * e.conjugate()).real
        if kind == 'const':
            return 2 * speed * (1 + te) * inner
        return -2 * speed * (1 - te) * inner
    # geometric grading toward both excision points
    edges = [u_lo]
    width = u_hi - u_lo
    g = [0.0]
    x = s * eps * 1e-2
    while x < 0.5:
        g.append(x)
        x *= 1.6
    g.append(0.5)
    left = [u_lo + width * y for y in g]
    right = [u_hi - width * y for y in reversed(g)]
    edges = left + right[1:]
    return (integrate_edges(lambda u: integrand(u, 'const'), edges),
            integrate_edges(lambda u: integrand(u, 'flip'), edges))


def t4_one_loop():
    eps = 0.1
    Lg = math.log((2 - eps) / eps)
    pc = 24 * math.pi * Lg
    pf = -(2 * math.pi / 3) * (Lg - 2 * (1 - eps))
    rows = {}
    for s in (0.2, 0.1, 0.05, 0.025, 0.0125, 0.00625):
        jc, jf = exchange_integrals(s, eps)
        rows[s] = (s * jc, jf / s)
    for s, (a, b) in rows.items():
        case(f'T4 constant-n0 exchange: s J / (24 pi log((2-eps)/eps)) - 1 at s={s:g}', 'T4', 'floating',
             abs(a / pc - 1), 1.2 * s + 1e-3)
        case(f'T4 flipped-return exchange: (J/s) / prediction - 1 at s={s:g}', 'T4', 'floating',
             abs(b / pf - 1), 4.0 * s + 1e-3)
    # Linear extrapolation in s from successive pairs; the residual itself
    # halves with s (an s log s remainder), which is what identifies the limit.
    ext_c = [(2 * rows[s2][0] - rows[s1][0]) / pc - 1 for s1, s2 in ((0.025, 0.0125), (0.0125, 0.00625))]
    ext_f = [(2 * rows[s2][1] - rows[s1][1]) / pf - 1 for s1, s2 in ((0.025, 0.0125), (0.0125, 0.00625))]
    case('T4 constant-n0: extrapolated s J(s) at s -> 0 equals 24 pi log((2-eps)/eps)', 'T4', 'floating',
         abs(ext_c[1]), 1e-3)
    case('T4 flipped-return: extrapolated J(s)/s at s -> 0 equals -(2 pi/3)(log((2-eps)/eps) - 2(1-eps))',
         'T4', 'floating', abs(ext_f[1]), 1e-3)
    case('T4 constant-n0: extrapolation residual shrinks on halving s', 'T4', 'floating',
         abs(ext_c[1] / ext_c[0]), 0.6)
    case('T4 flipped-return: extrapolation residual shrinks on halving s', 'T4', 'floating',
         abs(ext_f[1] / ext_f[0]), 0.6)
    case('T4 flipped-return exchange is negative (repulsive scalar, gauge attraction cancelled)', 'T4',
         'floating', max(b for _, b in rows.values()), 0.0, '<=')
    return rows


# ------------------------------------------------------------- matrices
def mm(A, B):
    return [[A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]],
            [A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]]]


def madd(*Ms):
    return [[sum(M[i][j] for M in Ms) for j in range(2)] for i in range(2)]


def msc(c, A):
    return [[c * A[i][j] for j in range(2)] for i in range(2)]


def minv(A):
    det = A[0][0] * A[1][1] - A[0][1] * A[1][0]
    return [[A[1][1] / det, -A[0][1] / det], [-A[1][0] / det, A[0][0] / det]]


def comm(A, B):
    return madd(mm(A, B), msc(-1, mm(B, A)))


def tr(A):
    return A[0][0] + A[1][1]


def mnorm(A):
    return math.sqrt(sum(abs(A[i][j]) ** 2 for i in range(2) for j in range(2)))


I2 = [[1 + 0j, 0j], [0j, 1 + 0j]]
T1m = [[0j, 0.5 + 0j], [0.5 + 0j, 0j]]
T2m = [[0j, -0.5j], [0.5j, 0j]]
T3m = [[0.5 + 0j, 0j], [0j, -0.5 + 0j]]


# ------------------------------------------------------------- background
# A test connection in the (x1, x2) plane, Hermitian, noncommuting, with a
# scalar Phi = n0 . Phi. Exact derivatives are coded by hand.
def fields(x1, x2, gauge=False):
    A1 = madd(msc(0.7, T1m), msc(0.3 * x2, T3m), msc(0.2 * x1 * x2, T2m))
    A2 = madd(msc(0.5, T2m), msc(-0.4 * x1, T3m), msc(0.1 * x2 * x2, T1m))
    Ph = madd(msc(0.6, T3m), msc(0.5 * x1, T1m), msc(-0.3 * x2, T2m), msc(0.2 * x1 * x2, T3m))
    if gauge:
        # g = exp(i theta T3), theta = 0.3 x1 + 0.2 x2^2; A' = g A g^-1 + d(theta) T3
        th = 0.3 * x1 + 0.2 * x2 * x2
        g = [[cmath.exp(0.5j * th), 0j], [0j, cmath.exp(-0.5j * th)]]
        gi = [[cmath.exp(-0.5j * th), 0j], [0j, cmath.exp(0.5j * th)]]
        A1 = madd(mm(mm(g, A1), gi), msc(0.3, T3m))
        A2 = madd(mm(mm(g, A2), gi), msc(0.4 * x2, T3m))
        Ph = mm(mm(g, Ph), gi)
    return A1, A2, Ph


def derived(x1, x2):
    A1, A2, Ph = fields(x1, x2)
    d1A2 = msc(-0.4, T3m)
    d2A1 = madd(msc(0.3, T3m), msc(0.2 * x1, T2m))
    F12 = madd(d1A2, msc(-1, d2A1), msc(-1j, comm(A1, A2)))
    d1P = madd(msc(0.5, T1m), msc(0.2 * x2, T3m))
    d2P = madd(msc(-0.3, T2m), msc(0.2 * x1, T3m))
    D1P = madd(d1P, msc(-1j, comm(A1, Ph)))
    D2P = madd(d2P, msc(-1j, comm(A2, Ph)))
    return A1, A2, Ph, F12, D1P, D2P


# ------------------------------------------------------------- transports
def rk4(Mfun, n):
    """Solve dU/dv = M(v) U on [0,1], U(0) = I; return list of U at grid."""
    U = I2
    out = [U]
    h = 1.0 / n
    for k in range(n):
        v = k * h
        k1 = mm(Mfun(v), U)
        k2 = mm(Mfun(v + h / 2), madd(U, msc(h / 2, k1)))
        k3 = mm(Mfun(v + h / 2), madd(U, msc(h / 2, k2)))
        k4 = mm(Mfun(v + h), madd(U, msc(h, k3)))
        U = madd(U, msc(h / 6, madd(k1, msc(2, k2), msc(2, k3), k4)))
        out.append(U)
    return out


def trace_transport(a, t, n, gauge=False):
    """Prefix transport with connection i A.dq + |dq| Phi (scalar +n0)."""
    if t == 0:
        return I2

    def M(v):
        r = t * v * v
        if v == 0:
            q, dq = 0j, 2j * math.sqrt(t)
        else:
            q = solve_tip(a, r)
            dq = 2 * v * t * (a - 2 / q)
        A1, A2, Ph = fields(q.real, q.imag, gauge)
        return madd(msc(1j * dq.real, A1), msc(1j * dq.imag, A2), msc(abs(dq), Ph))
    return rk4(M, n)[-1]


def chord_direct(q, sign, n, gauge=False):
    """Chord traversed tip -> base with connection i A.dx + sign |dx| Phi."""
    def M(v):
        x = q * (1 - v)
        A1, A2, Ph = fields(x.real, x.imag, gauge)
        dx = -q
        return madd(msc(1j * dx.real, A1), msc(1j * dx.imag, A2), msc(sign * abs(dx), Ph))
    return rk4(M, n)[-1]


def loop(a, t, family, n, gauge=False):
    q = solve_tip(a, t)
    sign = -1.0 if family == 'flip' else 1.0
    return mm(chord_direct(q, sign, n, gauge), trace_transport(a, t, n, gauge))


def generator(a, t, family, n):
    """Insertion formula for Qdot Q^-1 (decomposed and raw forms)."""
    q = solve_tip(a, t)
    qd = a - 2 / q
    Lq = abs(q)
    k = q.real * qd.imag - q.imag * qd.real
    qqd = (q.real * qd.real + q.imag * qd.imag) / Lq
    nhat = complex(-q.imag, q.real) / Lq
    sgn = 1.0 if family == 'flip' else -1.0   # scalar sign in base->tip transport R

    def Nconn(r):
        A1, A2, Ph = fields(r * q.real, r * q.imag)
        return madd(msc(1j * q.real, A1), msc(1j * q.imag, A2), msc(sgn * Lq, Ph))
    Rs = rk4(Nconn, n)
    J = [[0j, 0j], [0j, 0j]]
    G = [[0j, 0j], [0j, 0j]]
    raw = [[0j, 0j], [0j, 0j]]
    h = 1.0 / n
    for idx, R in enumerate(Rs):
        r = idx * h
        w = h / 3 * (1 if idx in (0, n) else (4 if idx % 2 else 2))
        A1, A2, Ph, F12, D1P, D2P = derived(r * q.real, r * q.imag)
        Ri = minv(R)

        def hat(X):
            return mm(mm(Ri, X), R)
        J = madd(J, msc(w * r, hat(F12)))
        G = madd(G, msc(w * r, hat(madd(msc(nhat.real, D1P), msc(nhat.imag, D2P)))))
        # raw insertion: r iF_{nu mu} qd^nu q^mu + sgn(|q| r qd.D Phi + (q.qd/|q|) Phi)
        Fqq = msc(-k, F12)
        qdDP = madd(msc(qd.real, D1P), msc(qd.imag, D2P))
        ins = madd(msc(1j * r, Fqq), msc(sgn * Lq * r, qdDP), msc(sgn * qqd, Ph))
        raw = madd(raw, msc(w, hat(ins)))
    Ph1 = mm(mm(minv(Rs[-1]), fields(q.real, q.imag)[2]), Rs[-1])
    gam = abs(qd) - sgn * qqd
    X = madd(msc(1j * k, J), msc(-sgn * k, G), msc(gam, Ph1))
    Xraw = madd(msc(abs(qd), Ph1), msc(-1, raw))
    return X, Xraw, dict(k=k, gamma=gam, q=q)


def t5_first_equation():
    n = 400
    for family in ('flip', 'const'):
        for a in (1.3, -0.8):
            for t in (0.05, 0.3):
                X, Xraw, info = generator(a, t, family, n)
                case(f'T5 {family}: decomposed generator equals raw insertion form a={a:g} t={t:g}', 'T5',
                     'floating', mnorm(madd(X, msc(-1, Xraw))) / mnorm(X), 1e-9)
                dt = 1e-4 * t
                Qp, Qm, Q0 = loop(a, t + dt, family, n), loop(a, t - dt, family, n), loop(a, t, family, n)
                Qd = msc(1 / (2 * dt), madd(Qp, msc(-1, Qm)))
                err = mnorm(madd(Qd, msc(-1, mm(X, Q0)))) / mnorm(Qd)
                case(f'T5 {family}: finite-difference Qdot equals X Q, a={a:g} t={t:g}', 'T5',
                     'floating', err, 2e-6)
    # a = 0 controls
    for t in (0.05, 0.3):
        Qf = loop(0.0, t, 'flip', n)
        case(f'T5 flipped return, a = 0: Q = I (backtracking one-form) t={t:g}', 'T5', 'floating',
             mnorm(madd(Qf, msc(-1, I2))), 1e-10)
        Qc = loop(0.0, t, 'const', n)
        case(f'T5 constant n0, a = 0: Q differs from I t={t:g}', 'T5', 'floating',
             mnorm(madd(Qc, msc(-1, I2))), 0.05, '>=')
        X, Xraw, info = generator(0.0, t, 'const', n)
        case(f'T5 constant n0, a = 0: gamma = 2|qdot| = 2/sqrt(t) t={t:g}', 'T5', 'floating',
             abs(info['gamma'] - 2 / math.sqrt(t)) * math.sqrt(t), 1e-12)
        X, Xraw, info = generator(0.0, t, 'flip', n)
        case(f'T5 flipped, a = 0: generator vanishes t={t:g}', 'T5', 'floating', mnorm(X), 1e-10)
    # Gauge covariance of the closed transport trace.
    for family in ('flip', 'const'):
        Q = loop(1.1, 0.2, family, n)
        Qg = loop(1.1, 0.2, family, n, gauge=True)
        case(f'T5 {family}: tr Q gauge invariant', 'T5', 'floating', abs(tr(Q) - tr(Qg)), 1e-10)
    # Geometric coefficients for the linear driver, small s.
    for s in (0.02, 0.005):
        a, t = 1.0, s * s
        q = solve_tip(a, t)
        qd = a - 2 / q
        k = q.real * qd.imag - q.imag * qd.real
        gam = abs(qd) - (q.real * qd.real + q.imag * qd.imag) / abs(q)
        case(f'T5 k / (-(2a/3) sqrt t) -> 1 at s={s:g}', 'T5', 'floating',
             abs(k / (-(2 * a / 3) * math.sqrt(t)) - 1), 2 * s * s + 1e-9)
        case(f'T5 gamma_flip / (a^2 sqrt t / 18) -> 1 at s={s:g}', 'T5', 'floating',
             abs(gam / (a * a * math.sqrt(t) / 18) - 1), 3 * s + 1e-6)
    # Leading short-time behaviour of the classical closed transport.
    A1, A2, Ph, F12, D1P, D2P = derived(0.0, 0.0)
    for t in (1e-3, 2.5e-4):
        a = 1.0
        area = -(2 * a / 9) * t ** 1.5
        Xint = madd(msc(area, madd(msc(1j, F12), D1P)), msc(a * a * t ** 1.5 / 27, Ph))
        pred = 0.25 * tr(mm(Xint, Xint))          # (1/2N) tr X^2 with N = 2
        Qf = loop(a, t, 'flip', 800)
        got = 0.5 * tr(Qf) - 1
        case(f'T5 flipped: (1/N)tr Q - 1 matches (1/2N) tr(A (iF12 + D1 Phi) + (a^2 t^1.5/27) Phi)^2 at t={t:g}',
             'T5', 'floating', abs(got / pred - 1), 12 * math.sqrt(t))
        Qc = loop(a, t, 'const', 800)
        gotc = 0.5 * tr(Qc) - 1
        predc = 8 * t * 0.5 * tr(mm(Ph, Ph))
        case(f'T5 constant n0: (1/N)tr Q - 1 matches 8 t (1/N) tr Phi(0)^2 at t={t:g}', 'T5', 'floating',
             abs(gotc / predc - 1), 12 * math.sqrt(t))


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('--output')
    args = parser.parse_args()
    t1_tip()
    t2_scaling()
    t3_sliver()
    t4_one_loop()
    t5_first_equation()
    data = dict(
        program='check_trace_completion.py',
        prepared_by='Claude Opus 5.5 (Anthropic), model identifier claude-opus-5-5 as reported by the runtime; effort not exposed',
        prepared_for='Edward Baker',
        date='2026-09-23',
        parameters=dict(driver='u(t) = a t', excision_eps=0.1,
                        transport='RK4, 400 steps (800 for short-time), Simpson insertions',
                        background='SU(2) polynomial test connection and scalar, see fields()'),
        scope=('Geometric and smooth-field diagnostics: exact tip series, Loewner scaling, '
               'sliver geometry, one-loop trace-chord exchange with excised cusps, and the '
               'first evolution equation for two chord completions on a classical test '
               'background. Not a quantum expectation, renormalization or interval proof.'),
        case_count=len(CASES),
        all_pass=all(c['passed'] for c in CASES),
        cases=CASES)
    text = json.dumps(data, indent=1, sort_keys=True)
    if args.output:
        with open(args.output, 'w') as fh:
            fh.write(text + '\n')
    print(text)


if __name__ == '__main__':
    main()
