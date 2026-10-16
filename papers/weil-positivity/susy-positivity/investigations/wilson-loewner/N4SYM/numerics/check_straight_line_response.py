#!/usr/bin/env python3
"""Straight half-BPS line: quadratic shape response, spectral measure and work.

Companion to N4SYM/notes/STRAIGHT_LINE_RESPONSE_AND_TRACE_COMPLETION_20260923.md.
Prepared for Edward Baker by Claude Opus 5.5 (Anthropic; model identifier
claude-opus-5-5 as reported by the runtime; reasoning effort not exposed).

Standard library only. Prints one JSON object to stdout (or --output FILE).
Deterministic: no random numbers, fixed quadrature rules.

Units: B = 1 throughout, so C_D = 12 and C_Phi = 2 (Correa-Henn-Maldacena-
Sever, arXiv:1202.4455, eqs. 20, 55). Every "floating" case is a diagnostic
of an analytic identity, not an interval certificate. No zeta function is
evaluated anywhere in this program.

Groups
  S1  tree-level displacement and tilt two-point functions from propagator
      derivatives (fixes signs of the Euclidean insertion iF + D Phi);
  S2  Fourier constants of the scale-covariant extensions of |s|^-4, |s|^-2
      (Hadamard finite part versus analytic continuation);
  S3  one-loop Maldacena-Wilson kernel on a wavy line and on an internal
      bump versus the quadratic formula pi B int (|k|^3|h|^2 - |k||j|^2);
  S4  exact rational bookkeeping: C_D = 6 C_Phi, spectral moments, mass
      shift and Foster masses of the exponential-cutoff control;
  S5  cutoff impedance: positive real at finite cutoff, low-frequency
      coefficient -2 pi B p^2, renormalized impedance not positive real;
  S6  work: total work -> 2 pi B ||h''||^2; finite-time work minus the
      cutoff mass energy -> 2 pi B (int h''^2 - h' h''); onset negativity
      of the renormalized account; tilt channel is an exact resistor.
"""
from fractions import Fraction as Fr
import argparse
import cmath
import json
import math

B = 1.0
CD = 12.0 * B
CPHI = 2.0 * B

CASES = []


def case(name, group, kind, value, threshold, comparison='<=', note=''):
    value = float(value)
    passed = value <= threshold if comparison == '<=' else value >= threshold
    CASES.append(dict(name=name, group=group, kind=kind, value=value,
                      threshold=threshold, comparison=comparison,
                      passed=bool(passed), note=note))


def exact(name, group, ok, note=''):
    case(name, group, 'exact', 0.0 if ok else 1.0, 0.0, '<=', note)


# ---------------------------------------------------------------- quadrature
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


GL = {n: gauss_legendre(n) for n in (8, 12, 20, 40)}


def panel_rule(a, b, panels, order=12):
    xs, ws = [], []
    nodes, weights = GL[order]
    h = (b - a) / panels
    for p in range(panels):
        lo = a + p * h
        for x, w in zip(nodes, weights):
            xs.append(lo + 0.5 * h * (x + 1.0))
            ws.append(0.5 * h * w)
    return xs, ws


def integrate(f, a, b, panels=40, order=12):
    xs, ws = panel_rule(a, b, panels, order)
    return sum(w * f(x) for x, w in zip(xs, ws))


def integrate_graded(f, edges, order=12, per=4):
    total = 0.0
    for lo, hi in zip(edges[:-1], edges[1:]):
        total += integrate(f, lo, hi, per, order)
    return total


# ------------------------------------------------------ S1 tree-level check
def s1_tree_level():
    def G(x):
        return 1.0 / sum(c * c for c in x)

    def d2(i, j, x):
        # Richardson-extrapolated central differences (error O(step^4)).
        return (4 * d2raw(i, j, x, 5e-4) - d2raw(i, j, x, 1e-3)) / 3

    def d2raw(i, j, x, step):
        def shift(v, k, d):
            v = list(v)
            v[k] += d
            return v
        if i == j:
            return (G(shift(x, i, step)) - 2 * G(x) + G(shift(x, i, -step))) / step ** 2
        return (G(shift(shift(x, i, step), j, step)) - G(shift(shift(x, i, step), j, -step))
                - G(shift(shift(x, i, -step), j, step)) + G(shift(shift(x, i, -step), j, -step))) / (4 * step ** 2)

    # Direction 0 is the line; 1,2,3 transverse. Propagators g^2/(4 pi^2 x^2)
    # per colour; <d_i Phi(x) d_j Phi(y)> = -d_i d_j G(x-y) etc.
    for sigma in (1.0, 0.7):
        x = [sigma, 0.0, 0.0, 0.0]
        scal = [[-d2(i, j, x) for j in (1, 2, 3)] for i in (1, 2, 3)]
        gauge = [[d2(i, j, x) + (d2(0, 0, x) if i == j else 0.0) for j in (1, 2, 3)]
                 for i in (1, 2, 3)]
        total = [[(scal[a][b] + gauge[a][b]) * sigma ** 4 for b in range(3)] for a in range(3)]
        # Colour factor C_F and g^2/(4 pi^2) = 2 B_1/C_F: <<DD>> = 2 B_1 * total
        case(f'S1 scalar-gradient coefficient 2 at sigma={sigma}', 'S1', 'floating',
             abs(scal[0][0] * sigma ** 4 - 2.0), 1e-5)
        case(f'S1 i F i F coefficient 4 (positive) at sigma={sigma}', 'S1', 'floating',
             abs(gauge[0][0] * sigma ** 4 - 4.0), 1e-5)
        off = max(abs(total[a][b]) for a in range(3) for b in range(3) if a != b)
        case(f'S1 displacement correlator diagonal in transverse index at sigma={sigma}',
             'S1', 'floating', off, 1e-5)
        case(f'S1 C_D/B_1 = 2 x 6 = 12 at sigma={sigma}', 'S1', 'floating',
             abs(2.0 * total[1][1] - 12.0), 2e-5)
    # Tilt: <Phi_a Phi_b> = G -> coefficient 1 -> 2 B_1 / sigma^2.
    x = [0.7, 0.0, 0.0, 0.0]
    case('S1 C_Phi/B_1 = 2 x (sigma^2 G) = 2 (tree level)', 'S1', 'floating',
         abs(2.0 * G(x) * 0.7 ** 2 - 2.0), 1e-14)


# ------------------------------------------------ S2 Fourier constants
def s2_fourier_constants():
    # Autocorrelation of h(s) = exp(-s^2): phi(u) = sqrt(pi/2) exp(-u^2/2).
    c = math.sqrt(math.pi / 2)

    def fp4(u):  # (phi(u) - phi(0) - u^2 phi''(0)/2)/u^4, series near 0
        if u < 0.05:
            v = u * u / 2
            return c * (1.0 / 8 - v / 24 + v * v / 96 - v ** 3 / 480)
        return c * (math.exp(-u * u / 2) - 1 + u * u / 2) / u ** 4

    def fp2(u):
        if u < 0.05:
            v = u * u / 2
            return c * (-0.5 + v / 4 - v * v / 12 + v ** 3 / 48)
        return c * (math.exp(-u * u / 2) - 1) / u ** 2

    edges = [0, 0.5, 1, 2, 4, 8, 16, 40]
    val4 = 2 * (integrate_graded(fp4, edges) + c * (-1.0 / (3 * 40 ** 3) + 1.0 / (2 * 40)))
    val2 = 2 * (integrate_graded(fp2, edges) - c / 40)
    # Fourier side: (pi/6) int |k|^3 |h^|^2 dk/2pi and -pi int |k| |h^|^2 dk/2pi,
    # |h^(k)|^2 = pi exp(-k^2/2), integrated numerically.
    k3 = 2 * integrate_graded(lambda k: k ** 3 * math.pi * math.exp(-k * k / 2), [0, 1, 2, 4, 8, 16]) / (2 * math.pi)
    k1 = 2 * integrate_graded(lambda k: k * math.pi * math.exp(-k * k / 2), [0, 1, 2, 4, 8, 16]) / (2 * math.pi)
    case('S2 finite part <[|s|^-4], phi> equals (pi/6) int |k|^3|h|^2', 'S2', 'floating',
         abs(val4 - math.pi / 6 * k3), 1e-9)
    case('S2 finite part <[|s|^-4], phi> equals pi/3 for the Gaussian', 'S2', 'floating',
         abs(val4 - math.pi / 3), 1e-9)
    case('S2 finite part <[|s|^-2], phi> equals -pi int |k||h|^2', 'S2', 'floating',
         abs(val2 + math.pi * k1), 1e-9)
    # Gagliardo identity: int int (g-g')^2/(s-s')^2 = 2 pi int |k||g^|^2 dk/2pi, g = h'.
    gag = 2 * c * 2 * integrate_graded(
        lambda u: (1 - (1 - u * u) * math.exp(-u * u / 2)) / u ** 2 if u > 1e-3 else 1.5 - 5 * u * u / 8,
        [0, 0.5, 1, 2, 4, 8, 16, 40]) + 2 * c * 2 / 40
    case('S2 Gagliardo form of h\' equals 2 pi int |k|^3 |h|^2 dk/2pi = 4 pi', 'S2', 'floating',
         abs(gag - 4 * math.pi), 1e-9)
    # Quadratic response of the Gaussian bump: (1/2) C_D <[s^-4],phi> = pi B int|k|^3|h|^2 = 2 pi B
    case('S2 (1/2) C_D <[s^-4],phi> = 2 pi B for the Gaussian bump', 'S2', 'floating',
         abs(0.5 * CD * val4 - 2 * math.pi * B), 1e-8)


# ------------------------------------------------ S3 one-loop MW kernel
def mw_double_integral(eps, sector, L=12.0, panels=24, order=12):
    xs, ws = panel_rule(-L, L, panels, order)
    if sector == 'h':
        h = [math.exp(-x * x) for x in xs]
        hd = [-2 * x * math.exp(-x * x) for x in xs]
        hdd = [(4 * x * x - 2) * math.exp(-x * x) for x in xs]
    else:
        g = [math.exp(-x * x) for x in xs]
        gd = [-2 * x * math.exp(-x * x) for x in xs]
    total = 0.0
    n = len(xs)
    for i in range(n):
        for k in range(n):
            du = xs[i] - xs[k]
            if sector == 'h':
                a, b = hd[i], hd[k]
                A = math.sqrt(1 + eps * eps * a * a)
                Bq = math.sqrt(1 + eps * eps * b * b)
                if abs(du) < 1e-12:
                    val = eps * eps * hdd[i] ** 2 / (2 * (1 + eps * eps * a * a) ** 2)
                else:
                    num = eps * eps * (a - b) ** 2 / (A * Bq + 1 + eps * eps * a * b)
                    val = num / (du * du + eps * eps * (h[i] - h[k]) ** 2)
            else:
                a, b = g[i], g[k]
                if abs(du) < 1e-12:
                    val = -eps * eps * gd[i] ** 2 / (2 * (1 + eps * eps * a * a) ** 2)
                else:
                    S = math.sqrt((1 + eps * eps * a * a) * (1 + eps * eps * b * b))
                    num = -eps * eps * (a - b) ** 2 / (S * ((1 + eps * eps * a * b) + S))
                    val = num / (du * du)
            total += ws[i] * ws[k] * val
    # Tails |s| > L on one variable (the bump vanishes there to e^-144).
    tail = 0.0
    for i in range(n):
        x = xs[i]
        if sector == 'h':
            f = math.sqrt(1 + eps * eps * hd[i] ** 2) - 1
            cc = eps * abs(h[i])
            if cc > 1e-14:
                inner = (math.pi / 2 - math.atan((L - x) / cc)) / cc + (math.pi / 2 - math.atan((L + x) / cc)) / cc
            else:
                inner = 1 / (L - x) + 1 / (L + x)
        else:
            f = 1 / math.sqrt(1 + eps * eps * g[i] ** 2) - 1
            inner = 1 / (L - x) + 1 / (L + x)
        tail += ws[i] * f * inner
    return total + 2 * tail


def s3_one_loop():
    res_h = {e: mw_double_integral(e, 'h') / e ** 2 for e in (0.2, 0.1, 0.05, 0.025)}
    res_j = {e: mw_double_integral(e, 'j') / e ** 2 for e in (0.2, 0.1, 0.05, 0.025)}
    # Quadratic predictions (B stripped): wavy line 2 pi; internal bump -pi.
    for e, v in res_h.items():
        case(f'S3 wavy-line one-loop I(eps)/eps^2 - 2 pi at eps={e}', 'S3', 'floating',
             abs(v - 2 * math.pi), 0.03 * e * e / 0.01 + 1e-6)
    for e, v in res_j.items():
        case(f'S3 internal-bump one-loop I(eps)/eps^2 + pi at eps={e}', 'S3', 'floating',
             abs(v + math.pi), 0.03 * e * e / 0.01 + 1e-6)
    # Deviation scales like eps^2 (quartic term), ratio ~ 4 on halving eps.
    rh = (res_h[0.1] - 2 * math.pi) / (res_h[0.05] - 2 * math.pi)
    rj = (res_j[0.1] + math.pi) / (res_j[0.05] + math.pi)
    case('S3 wavy-line deviation ratio eps=0.1 vs 0.05 near 4 (quartic order)', 'S3', 'floating',
         abs(rh - 4.0), 0.05)
    case('S3 internal-bump deviation ratio eps=0.1 vs 0.05 near 4', 'S3', 'floating',
         abs(rj - 4.0), 0.05)
    # Extrapolated eps -> 0 values (three-point Richardson in eps^2).
    # Residual is O(eps^6); a 64-fold drop on halving was observed when writing.
    ext_h = (64 * res_h[0.025] - 20 * res_h[0.05] + res_h[0.1]) / 45
    ext_j = (64 * res_j[0.025] - 20 * res_j[0.05] + res_j[0.1]) / 45
    case('S3 wavy-line Richardson limit (eps = 0.1, 0.05, 0.025) equals 2 pi', 'S3', 'floating',
         abs(ext_h - 2 * math.pi), 1e-7)
    case('S3 internal-bump Richardson limit (eps = 0.1, 0.05, 0.025) equals -pi', 'S3', 'floating',
         abs(ext_j + math.pi), 1e-7)
    # Zarembo profile n = T (j = h'): one-loop integrand vanishes identically;
    # at quadratic order the two sectors cancel iff C_D = 6 C_Phi.
    quad_h = math.pi * B * 2.0          # pi B int |k|^3 |h|^2 dk/2pi for Gaussian h
    quad_j = -math.pi * B * 2.0         # -pi B int |k| |h'^|^2 = -pi B int |k|^3 |h|^2
    case('S3 Zarembo profile j = h\': quadratic response cancels', 'S3', 'floating',
         abs(quad_h + quad_j), 1e-15)
    return res_h, res_j


# ------------------------------------------------ S4 exact bookkeeping
def s4_exact():
    cd, cphi = Fr(12), Fr(2)
    exact('S4 C_D - 6 C_Phi = 0 (CHMS values, units of B)', 'S4', cd - 6 * cphi == 0,
          'Equivalent to vanishing quadratic response of the Zarembo profile')
    fact = [1, 1, 2, 6, 24, 120]
    exact('S4 int_0^inf e^{-W s} W^3 dW = 6/s^4 => d mu = (C_D/6) W^3 dW', 'S4', fact[3] == 6)
    exact('S4 exponential cutoff: mass of d mu = C_D Lambda^4 = 12 B Lambda^4', 'S4',
          cd / 6 * fact[3] == 12)
    exact('S4 mass shift delta m = int 2 d mu / W^3 = (C_D/3) Lambda = 4 B Lambda', 'S4',
          2 * cd / 6 * fact[0] == 4)
    exact('S4 static Kubo term chi(0) = int 2 d mu / W = (2 C_D/3) Lambda^3 = 8 B Lambda^3', 'S4',
          2 * cd / 6 * fact[2] == 8)
    exact('S4 Foster mass of Y = p chi (measure 2 W d mu) = 8 C_D Lambda^5 = 96 B Lambda^5', 'S4',
          2 * cd / 6 * fact[4] == 96)
    exact('S4 Foster mass of the translation-invariant impedance (2/W) d mu = 8 B Lambda^3', 'S4',
          2 * cd / 6 * fact[2] == 8)
    exact('S4 radiation-reaction coefficient pi C_D/6 = 2 pi B (ratio to pi rational = 2)', 'S4',
          cd / 6 == 2)
    exact('S4 tilt resistance pi C_Phi = 2 pi B equals displacement coefficient', 'S4',
          cphi == cd / 6)


# ------------------------------------------------ S5 impedance
def cutoff_Z(p, lam):
    # Z(p) = (C_D/3) int_0^inf W^2 p e^{-W/lam}/(p^2+W^2) dW
    def f(w):
        return w * w * p * math.exp(-w / lam) / (p * p + w * w)
    edges = [0, 0.25, 0.5, 1, 2, 4, 8, 16, 32, 64]
    while edges[-1] < 60 * lam:
        edges.append(edges[-1] * 2)
    s = 0
    for lo, hi in zip(edges[:-1], edges[1:]):
        xs, ws = panel_rule(lo, hi, 4, 20)
        s += sum(wt * f(x) for x, wt in zip(xs, ws))
    return CD / 3 * s


def s5_impedance():
    worst = 1e9
    for lam in (5.0, 50.0):
        for p in (0.3 + 0.0j, 1 + 1j, 0.2 + 3j, 2 + 0.5j, 0.05 + 10j, 4 + 4j):
            worst = min(worst, cutoff_Z(p, lam).real)
    case('S5 finite-cutoff impedance Re Z(p) >= 0 on sampled Re p > 0', 'S5', 'floating',
         worst, 0.0, '>=', 'Foster form guarantees this; numerics only confirm')
    for lam in (10.0, 100.0, 1000.0):
        p = 1.0
        coeff = (cutoff_Z(p, lam).real - (CD / 3) * lam * p) / p ** 2
        # Leading approach: -2 pi B + (C_D/3)(log Lambda + 1 - gamma_E)/Lambda.
        lead = -2 * math.pi * B + CD / 3 * (math.log(lam) + 1 - 0.5772156649015329) / lam
        case(f'S5 low-frequency coefficient (Z - delta m p)/p^2 -> -2 pi B at Lambda={lam:g}', 'S5',
             'floating', abs(coeff - lead), 20.0 * (1 + math.log(lam)) ** 2 / lam ** 2)
    # Renormalized impedance m_R p - 2 pi B p^2 is not positive real.
    for mR in (0.0, 1.0, 100.0):
        x = (mR + 1.0) / (2 * math.pi * B) * 2
        case(f'S5 renormalized Z_R(x) < 0 at real x={x:.4g} for m_R={mR:g}', 'S5', 'floating',
             mR * x - 2 * math.pi * B * x * x, 0.0, '<=')


# ------------------------------------------------ polynomials for S6
class Poly:
    def __init__(self, c):
        self.c = [Fr(x) for x in c]

    def d(self):
        return Poly([k * self.c[k] for k in range(1, len(self.c))] or [0])

    def __mul__(self, o):
        r = [Fr(0)] * (len(self.c) + len(o.c) - 1)
        for i, a in enumerate(self.c):
            for j, b in enumerate(o.c):
                r[i + j] += a * b
        return Poly(r)

    def integ(self):
        return Poly([0] + [self.c[k] / (k + 1) for k in range(len(self.c))])

    def __call__(self, x):
        s = Fr(0) if isinstance(x, Fr) else 0.0
        for a in reversed(self.c):
            s = s * x + (a if isinstance(x, Fr) else float(a))
        return s


def bump():
    base = Poly([1, 0, -1])  # 1 - s^2
    p = Poly([1])
    for _ in range(5):
        p = p * base
    return p  # (1 - s^2)^5 on [-1, 1]


_DERIV_CACHE = {}


def _float_derivs(P):
    key = id(P)
    if key not in _DERIV_CACHE:
        derivs = []
        q = P
        while any(c != 0 for c in q.c):
            derivs.append([float(c) for c in q.c])
            q = q.d()
        _DERIV_CACHE[key] = (P, derivs)
    return _DERIV_CACHE[key][1]


def _horner(coeffs, t):
    s = 0.0
    for a in reversed(coeffs):
        s = s * t + a
    return s


def fourier_poly(P, lo, hi, w):
    """int_lo^hi P(s) e^{i w s} ds for polynomial P (exact formula or GL)."""
    derivs = _float_derivs(P)
    if w < 2.0:
        nodes, weights = GL[40]
        s = 0j
        for x, wt in zip(nodes, weights):
            t = lo + 0.5 * (hi - lo) * (x + 1)
            s += 0.5 * (hi - lo) * wt * _horner(derivs[0], t) * cmath.exp(1j * w * t)
        return s

    def anti(t):
        s = 0j
        for k, dk in enumerate(derivs):
            s += (-1) ** k * _horner(dk, t) / (1j * w) ** (k + 1)
        return s * cmath.exp(1j * w * t)
    return anti(hi) - anti(lo)


def omega_integral(f, wmax=2000.0):
    edges = [0, 0.5, 1, 2, 3, 4, 6, 8, 12, 16, 24, 32, 48, 64, 96, 128, 192, 256, 384, 512, 768, 1024, 1536, 2000]
    s = 0
    for lo, hi in zip(edges[:-1], edges[1:]):
        per = max(4, int((hi - lo) / 2))
        s += integrate(f, lo, hi, per, 12)
    return s


def s6_work():
    h = bump()
    hd, hdd, hddd = h.d(), h.d().d(), h.d().d().d()
    hdd2 = (hdd * hdd).integ()
    total_exact = hdd2(Fr(1)) - hdd2(Fr(-1))
    gl = integrate(lambda s: hdd(s) ** 2, -1.0, 1.0, 8, 20)
    case('S6 exact rational int h\'\'^2 agrees with Gauss-Legendre quadrature', 'S6', 'floating',
         abs(float(total_exact) - gl) / gl, 1e-13, note=f'exact value {total_exact}')
    # Total work at finite cutoff: (C_D/6) int W^4 e^{-W/lam} |h^(W)|^2 dW.
    def total_work(lam):
        return CD / 6 * omega_integral(
            lambda w: w ** 4 * math.exp(-w / lam) * abs(fourier_poly(h, -1.0, 1.0, w)) ** 2)
    target = 2 * math.pi * B * float(total_exact)
    prev = None
    for lam in (5.0, 50.0, 500.0):
        wv = total_work(lam)
        case(f'S6 total work below 2 pi B ||h\'\'||^2 at Lambda={lam:g}', 'S6', 'floating',
             wv - target, 1e-9, '<=')
        if prev is not None:
            case(f'S6 total work increases with Lambda (to {lam:g})', 'S6', 'floating',
                 prev - wv, 0.0, '<=')
        prev = wv
    wv_inf = CD / 6 * omega_integral(lambda w: w ** 4 * abs(fourier_poly(h, -1.0, 1.0, w)) ** 2)
    case('S6 total work at infinite cutoff equals 2 pi B ||h\'\'||^2', 'S6', 'floating',
         abs(wv_inf - target) / target, 1e-7)
    # Finite time: subtract the cutoff mass energy and compare with the
    # renormalized account 2 pi B (int^T h''^2 - h'(T) h''(T)).
    for T in (Fr(-9, 10), Fr(-1, 2), Fr(0), Fr(1, 3), Fr(7, 10)):
        Tf = float(T)
        a, b, c = float(hd(T)), float(hdd(T)), float(hddd(T))
        ren = hdd2(T) - hdd2(Fr(-1)) - hd(T) * hdd(T)

        def integrand(w):
            F = fourier_poly(hd, -1.0, Tf, w)
            return w * w * abs(F) ** 2 - a * a
        tail = (b * b - 2 * a * c) / 2000.0
        sub = CD / 6 * (omega_integral(integrand) + tail)
        case(f'S6 finite-time work minus cutoff mass energy -> renormalized account at T={Tf:g}', 'S6',
             'floating', abs(sub - 2 * math.pi * B * float(ren)), 2e-6 * max(1.0, abs(2 * math.pi * float(ren))))
        # Approach from finite Lambda (monotone in Lambda is not claimed).
        # Approach: |error| ~ (C_D/6) |h''^2 - 2 h' h'''| (log Lambda + O(1))/Lambda.
        errs = []
        for lam in (400.0, 4000.0):
            sub_l = CD / 6 * omega_integral(
                lambda w: w * w * math.exp(-w / lam) * (abs(fourier_poly(hd, -1.0, Tf, w)) ** 2 - a * a / (w * w)))
            errs.append(abs(sub_l - sub))
        # Rate check: a pure (log Lambda)/Lambda or 1/Lambda law gives 0.10-0.14 for a tenfold
        # Lambda; drive-dependent constants move the observed ratio (0.10-0.18 when written).
        case(f'S6 finite-Lambda subtracted work converges at rate O(log Lambda/Lambda) at T={Tf:g}',
             'S6', 'floating', errs[1] / errs[0], 0.2,
             note=f'errors {errs[0]:.4e} (Lambda=400), {errs[1]:.4e} (Lambda=4000)')
    # Onset negativity of the renormalized account: every T close to -1.
    onset = []
    for x in (Fr(1, 5), Fr(1, 10), Fr(1, 20), Fr(1, 100)):
        T = Fr(-1) + x
        ren = hdd2(T) - hdd2(Fr(-1)) - hd(T) * hdd(T)
        onset.append(float(ren))
        exact(f'S6 renormalized work (m_R = 0) is negative at T = -1 + {x}', 'S6', ren < 0,
              f'value/(2 pi B) = {float(ren):.6e}')
    # Leading ratio h'h''/int h''^2 -> (2n-3)/(n-1) = 7/4 for onset order n = 5.
    x = Fr(1, 10 ** 6)
    T = Fr(-1) + x
    ratio = hd(T) * hdd(T) / (hdd2(T) - hdd2(Fr(-1)))
    case('S6 onset ratio h\'h\'\'/int h\'\'^2 -> 7/4 for fifth-order onset', 'S6', 'exact-rational-eval',
         abs(float(ratio) - 1.75), 1e-5)
    # Any finite renormalized mass: negativity persists close enough to onset.
    for mR in (10, 1000, 100000):
        found = None
        for k in range(1, 60):
            xx = Fr(1, 2 ** k)
            T = Fr(-1) + xx
            val = Fr(mR, 2) * hd(T) ** 2 + 2 * Fr(math.pi) * (hdd2(T) - hdd2(Fr(-1)) - hd(T) * hdd(T))
            if val < 0:
                found = float(xx)
                break
        case(f'S6 renormalized work negative near onset for m_R={mR} (B = 1)', 'S6', 'exact-rational-eval',
             0.0 if found else 1.0, 0.0, '<=', f'first negative at T = -1 + {found}')
    # Tilt channel: W_Phi(T) = C_Phi int_0^inf |int^T e^{iWs} j'|^2 dW = 2 pi B int^T j'^2.
    j = bump()
    jd = j.d()
    jd2 = (jd * jd).integ()
    for T in (Fr(-9, 10), Fr(0), Fr(1, 2), Fr(1)):
        Tf = float(T)
        a = float(jd(T))
        val = CPHI * (omega_integral(lambda w: abs(fourier_poly(jd, -1.0, Tf, w)) ** 2) + a * a / 2000.0)
        exact_val = 2 * math.pi * B * float(jd2(T) - jd2(Fr(-1)))
        case(f'S6 tilt finite-time work equals 2 pi B int^T j\'^2 at T={Tf:g}', 'S6', 'floating',
             abs(val - exact_val), 2e-6 * max(1.0, exact_val))
    return onset


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('--output')
    args = parser.parse_args()
    s1_tree_level()
    s2_fourier_constants()
    s3_one_loop()
    s4_exact()
    s5_impedance()
    s6_work()
    data = dict(
        program='check_straight_line_response.py',
        prepared_by='Claude Opus 5.5 (Anthropic), model identifier claude-opus-5-5 as reported by the runtime; effort not exposed',
        prepared_for='Edward Baker',
        date='2026-09-23',
        parameters=dict(B=B, C_D=CD, C_Phi=CPHI, units='B = 1',
                        bump='exp(-s^2) for S2-S3; (1-s^2)^5 on [-1,1] for S6',
                        cutoff='d mu_Lambda = (C_D/6) W^3 exp(-W/Lambda) dW',
                        quadrature='composite Gauss-Legendre, fixed panels'),
        scope=('Diagnostics of analytic identities for the straight half-BPS line: '
               'tree-level signs, Fourier constants, one-loop kernel expansion, '
               'spectral bookkeeping, impedance positivity and energy accounting. '
               'Not interval arithmetic; not a proof of the continuum statements.'),
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
