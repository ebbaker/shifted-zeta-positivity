#!/usr/bin/env python3
"""Height-p transport law for the heat-flowed completed L-functions, and the
explicit error budget of Lemma A_p (Project 03, note 01).

Prepared for Edward Baker with LLM assistance.  Model: Claude Opus 5.5
(configured identifier claude-opus-5-5), Claude Cowork, reasoning effort max,
17 October 2026.  Standard library only; prints one deterministic JSON record
(floats rounded to 12 significant figures).

Companion of papers/investigations-3/03_effective_outer_remainders/notes/round-1/
01_HEIGHT_P_TRANSPORT_AND_LEMMA_AP_CLAUDE_20261017.md.  Every number below is
a floating-point evaluation: either a direct numerical computation (sections B
and C) or the evaluation of the explicit majorants of the note's Proposition
4.5 (sections D-H), with the real-variable majorants interpolated from
logarithmic tables (relative error below 4e-5).  Nothing here is an
outward-rounded certificate.

Sections
  A  special-function self-checks
  B  identity check: kernel integral against the Gaussian average of xi
  C  transport law: S(x,p,t) against (1/2) Re (F'/F)(s_*) and the second-order term
  D  the explicit bound E against the measured deviation of section C
  E  E/2 against the floor gain on (ell, t) grids; the thresholds ell_1(p, a)
  F  Lemma A_p floors for the consumers (family at every height; zeta at x >= X)
  G  the strip comparison of note 01 of Project 01 rerun with the heat floor
  H  thresholds in ell and in the conductor, small-t limits, monotonicity of E in ell
"""
import cmath
import json
import math
from fractions import Fraction

PI = math.pi
SQRT2PI = math.sqrt(2 * PI)


def sig(x, n=12):
    if x is None:
        return None
    if isinstance(x, complex):
        return [sig(x.real, n), sig(x.imag, n)]
    if x == 0 or not math.isfinite(x):
        return x if math.isfinite(x) else str(x)
    return float(f"{x:.{n}g}")


# ---------------------------------------------------------------------------
# Bernoulli numbers
# ---------------------------------------------------------------------------

def bernoulli_list(m):
    B = [Fraction(0)] * (m + 1)
    B[0] = Fraction(1)
    for n in range(1, m + 1):
        s = Fraction(0)
        for k in range(n):
            s += math.comb(n + 1, k) * B[k]
        B[n] = -s / (n + 1)
    return B


BERN = bernoulli_list(60)
B2K = [float(BERN[2 * k]) for k in range(30)]


# ---------------------------------------------------------------------------
# zeta and its derivatives by Euler-Maclaurin (complex s, s != 1)
# ---------------------------------------------------------------------------

def zeta_derivs(s, jmax=3, N=None, M=16):
    """[zeta^{(j)}(s), j = 0..jmax]; zeta^{(j)}(s) = (-1)^j sum (log n)^j n^{-s}."""
    s = complex(s)
    if N is None:
        N = int(abs(s.imag)) + 25
    lnN = math.log(N)
    logs = [math.log(n) for n in range(2, N)]
    pw = [cmath.exp(-s * ln) for ln in logs]
    out = []
    for j in range(jmax + 1):
        tot = 0j
        if j == 0:
            for v in pw:
                tot += v
            tot += 1.0
        else:
            for ln, v in zip(logs, pw):
                tot += (ln ** j) * v
        Ns1 = cmath.exp((1 - s) * lnN)
        for i in range(j + 1):
            tot += math.factorial(j) / math.factorial(j - i) * lnN ** (j - i) * Ns1 / (s - 1) ** (i + 1)
        tot += lnN ** j * cmath.exp(-s * lnN) / 2
        P = [0j] * (j + 1)
        P[j] = 1 + 0j
        m = 0
        k = 1
        corr = 0j
        while k <= M:
            newP = [-(s + m) * c for c in P]
            for i in range(1, len(P)):
                newP[i - 1] += i * P[i]
            P = newP
            m += 1
            if m == 2 * k - 1:
                val = sum(P[i] * lnN ** i for i in range(len(P))) * cmath.exp(-(s + m) * lnN)
                corr += B2K[k] / math.factorial(2 * k) * val
                k += 1
        tot -= corr
        out.append(((-1) ** j) * tot)
    return out


def zeta_real_family(sg):
    """zeta, log zeta, kappa = -zeta'/zeta, K2 = -kappa', K3 = kappa'' at real sigma > 1."""
    z = zeta_derivs(complex(sg, 0.0), 3, N=25)
    z0, z1, z2, z3 = (c.real for c in z)
    kap = -z1 / z0
    K2 = (z2 * z0 - z1 * z1) / (z0 * z0)
    K3 = -(z3 / z0 - 3 * z2 * z1 / (z0 * z0) + 2 * (z1 / z0) ** 3)
    return z0, math.log(z0), kap, K2, K3


# ---------------------------------------------------------------------------
# digamma family (real and complex) and log Gamma (complex)
# ---------------------------------------------------------------------------

def psi_family_real(x):
    """(psi, psi', psi'') at real x > 0."""
    sh0 = sh1 = sh2 = 0.0
    while x < 15.0:
        sh0 -= 1.0 / x
        sh1 += 1.0 / (x * x)
        sh2 -= 2.0 / (x ** 3)
        x += 1.0
    p0 = math.log(x) - 1 / (2 * x)
    p1 = 1 / x + 1 / (2 * x * x)
    p2 = -1 / (x * x) - 1 / (x ** 3)
    for k in range(1, 12):
        b = B2K[k]
        p0 -= b / (2 * k * x ** (2 * k))
        p1 += b / x ** (2 * k + 1)
        p2 -= (2 * k + 1) * b / x ** (2 * k + 2)
    return p0 + sh0, p1 + sh1, p2 + sh2


def digamma_c(z):
    z = complex(z)
    sh = 0j
    while z.real < 15.0:
        sh -= 1 / z
        z += 1
    r = cmath.log(z) - 1 / (2 * z)
    for k in range(1, 12):
        r -= B2K[k] / (2 * k * z ** (2 * k))
    return r + sh


def trigamma_c(z):
    z = complex(z)
    sh = 0j
    while z.real < 15.0:
        sh += 1 / (z * z)
        z += 1
    r = 1 / z + 1 / (2 * z * z)
    for k in range(1, 12):
        r += B2K[k] / z ** (2 * k + 1)
    return r + sh


def tetragamma_c(z):
    z = complex(z)
    sh = 0j
    while z.real < 15.0:
        sh -= 2 / (z ** 3)
        z += 1
    r = -1 / (z * z) - 1 / (z ** 3)
    for k in range(1, 12):
        r -= (2 * k + 1) * B2K[k] / z ** (2 * k + 2)
    return r + sh


def loggamma_c(z):
    z = complex(z)
    sh = 0j
    while z.real < 15.0:
        sh -= cmath.log(z)
        z += 1
    r = (z - 0.5) * cmath.log(z) - z + 0.5 * math.log(2 * PI)
    for k in range(1, 12):
        r += B2K[k] / (2 * k * (2 * k - 1) * z ** (2 * k - 1))
    return r + sh


# ---------------------------------------------------------------------------
# Tables for the majorants (linear interpolation on logarithmic grids)
# ---------------------------------------------------------------------------

class Table:
    def __init__(self, f, lo, hi, n, shift):
        """f evaluated at shift + exp(u), u uniform on [log lo, log hi]."""
        self.u0 = math.log(lo)
        self.du = (math.log(hi) - self.u0) / (n - 1)
        self.shift = shift
        self.vals = [f(shift + math.exp(self.u0 + i * self.du)) for i in range(n)]
        self.n = n

    def __call__(self, x, col):
        u = (math.log(x - self.shift) - self.u0) / self.du
        i = int(u)
        if i < 0:
            i = 0
        if i >= self.n - 1:
            i = self.n - 2
        w = u - i
        a = self.vals[i][col]
        b = self.vals[i + 1][col]
        return a + (b - a) * w


ZT = Table(zeta_real_family, 1e-4, 120.0, 2600, 1.0)   # sigma = 1 + exp(u)


def zeta_r(s):
    return ZT(s, 0)


def logzeta_r(s):
    return ZT(s, 1)


def kappa_r(s):
    return ZT(s, 2)


def K2_r(s):
    return ZT(s, 3)


def K3_r(s):
    return ZT(s, 4)


def _psi_row(x):
    p0, p1, p2 = psi_family_real(x)
    return (p0, p1, p2, math.lgamma(x))


PT = Table(_psi_row, 0.05, 80.0, 2600, 0.0)


def psi_r(x):
    return PT(x, 0)


def psi1_r(x):
    return PT(x, 1)


def lgam_r(x):
    return PT(x, 3)


# ---------------------------------------------------------------------------
# Sections D-H machinery: the explicit bound of Proposition 4.5
# ---------------------------------------------------------------------------

def crude_L(sg, Q, mode, T=None):
    """Upper bound for |L(sigma+iT)|, 0 < sigma <= 1 (+eta), from partial summation.
    family:  1 + int_1^N u^-sigma du + Q N^-sigma/(2 sigma),   Q >= q|s|
    zeta:    1 + int_1^N u^-sigma du + N^(1-sigma)/T + N^-sigma/2 + Q N^-sigma/(2 sigma), Q >= |s|."""
    best = math.inf
    base = max(1, int(Q / 2))
    for N in (max(1, base - 1), base, base + 1, base + 2):
        if abs(sg - 1) < 1e-12:
            I = math.log(N)
        else:
            I = (N ** (1 - sg) - 1) / (1 - sg)
        val = 1 + I + Q * N ** (-sg) / (2 * sg)
        if mode == "zeta":
            val += N ** (1 - sg) / T + 0.5 * N ** (-sg)
        best = min(best, val)
    return best


def simpson(xs_fx):
    """Composite Simpson on an odd number of equally spaced samples [(x, f)]."""
    n = len(xs_fx) - 1
    h = xs_fx[1][0] - xs_fx[0][0]
    tot = xs_fx[0][1] + xs_fx[-1][1]
    for i in range(1, n):
        tot += (4 if i % 2 else 2) * xs_fx[i][1]
    return tot * h / 3


def E_bound(ell, tau, p, mode, a=0, T=None, eta=0.05, n_e=600, n_l=400, n_r=600, detail=False):
    """Explicit majorant E of |G'/G(w) - (F'/F)(s_*)| (Proposition 4.5), as a function of
    ell = ell_* = 2 Re alpha(s_*), tau = sqrt(t/2), p, and the case:
      mode 'family': primitive chi with parity a, Gamma bounds uniform in the height;
      mode 'zeta'  : zeta at height >= T (Gamma curvature 2/T, 3/T^2)."""
    s0 = (1 + p) / 2
    ss = s0 + tau * tau * ell / 2
    sig1 = 1 + eta
    V = ss - sig1
    if V <= 0:
        return math.inf, None
    ks = kappa_r(ss)
    zr = zeta_r(ss) / zeta_r(2 * ss)
    if mode == "family":
        k = K2_r(ss) + 0.25 * psi1_r((ss + a) / 2)
        xs = (ss + a) / 2
        c = 1 / (2 * xs) + 1 / (12 * xs * xs)
        lam_s = lgam_r((ss + a) / 2)
        dlam_s = 0.5 * psi_r((ss + a) / 2)
        Mfun_s = ks - 0.5 * psi_r((ss + a) / 2)

        def Mfun(sgm):
            return kappa_r(sgm) - 0.5 * psi_r((sgm + a) / 2)

        def theta(v):
            sgm = ss + v
            return lgam_r((sgm + a) / 2) - lam_s - v * dlam_s
    else:
        k = K2_r(ss) + 2.0 / T
        xs = ss / 2
        zabs = math.hypot(xs, T / 2)
        c = xs / (2 * zabs * zabs) + 1 / (12 * xs * zabs)
        Mfun_s = ks

        def Mfun(sgm):
            return kappa_r(sgm)

        def theta(v):
            return v * v / T
    if tau * tau * k >= 1:
        return math.inf, None
    Q = 2 * PI * math.exp(ell + c)
    lzs = logzeta_r(ss)
    tt = tau * tau

    def logphi(v):
        return -v * v / (2 * tt) - math.log(SQRT2PI * tau)

    # ---- Euler region v in [-V, 16 tau], split at 0 (Lemmas 4.1-4.2)
    def euler_terms(v):
        sgm = ss + v
        lz = logzeta_r(sgm) - lzs
        th = theta(v)
        if mode == "family":
            r = Mfun(sgm) - Mfun_s + v * k
        else:
            r = (kappa_r(sgm) - ks + v * K2_r(ss)) + 1.5 * v * v / (T * T)
        r = max(r, 0.0)
        logg = abs(lz) + th
        Dm = (lz + v * ks) + th
        lp = logphi(v)
        return r * math.exp(logg + lp), math.exp(ks * abs(v) + lp) * math.expm1(max(Dm, 0.0)), logg
    vlo = -min(V, 40 * tau)
    pts_l = [vlo + (0 - vlo) * i / n_e for i in range(n_e + 1)]
    pts_r = [16 * tau * i / n_e for i in range(n_e + 1)]
    A1 = [(v,) + euler_terms(v)[:2] for v in pts_l]
    A2 = [(v,) + euler_terms(v)[:2] for v in pts_r]
    Mrho = simpson([(x, f) for x, f, _ in A1]) + simpson([(x, f) for x, f, _ in A2])
    P1 = simpson([(x, g) for x, _, g in A1]) + simpson([(x, g) for x, _, g in A2])
    _, _, loggV = euler_terms(-V)
    BV = math.exp(loggV + logphi(V))
    # ---- left strip: sigma in [1/2, sig1)
    DL = NL = P2 = 0.0
    smin = max(0.5, ss - 40 * tau)
    if smin < sig1:
        pts = []
        for i in range(n_l + 1):
            sgm = smin + (sig1 - smin) * i / n_l
            v = sgm - ss
            if sgm > 1.0 + 2e-4:
                Lam = min(zeta_r(sgm), crude_L(sgm, Q, mode, T))
            else:
                Lam = crude_L(sgm, Q, mode, T)
            lg = math.log(zr * Lam) + theta(v) + logphi(v)
            gl = math.exp(lg)
            pts.append((sgm, gl, gl * (abs(v) / tt + ks), gl + math.exp(ks * abs(v) + logphi(v))))
        DL += simpson([(x, a1) for x, a1, _, _ in pts])
        NL += simpson([(x, a2) for x, _, a2, _ in pts])
        P2 += simpson([(x, a3) for x, _, _, a3 in pts])
    # ---- reflected region: sigma < 1/2, u = 1 - sigma in (1/2, umax]
    umax = ss + tt * ell + 30 * tau + 2.0
    pts = []
    for i in range(n_r + 1):
        u = 0.5 + 1e-9 + (umax - 0.5) * i / n_r
        sgm = 1 - u
        v = sgm - ss
        if u > 1.0 + 2e-4:
            Lam = zeta_r(u)
            if u <= ss:
                Lam = min(Lam, crude_L(u, Q, mode, T))
        else:
            Lam = crude_L(u, Q, mode, T)
        lg = math.log(zr * Lam) + (ell / 2) * (1 - 2 * sgm) + theta(u - ss) + logphi(v)
        gr = math.exp(lg) if lg > -700 else 0.0
        pts.append((u, gr, gr * (abs(v) / tt + ks), gr + math.exp(ks * abs(v) + logphi(v))))
    DL += simpson([(x, a1) for x, a1, _, _ in pts])
    NL += simpson([(x, a2) for x, _, a2, _ in pts])
    P2 += simpson([(x, a3) for x, _, _, a3 in pts])
    d0 = math.exp(-tt * ks * ks / 2) - P1 - P2
    if d0 <= 0:
        return math.inf, None
    main = tt * k * ks / (1 - tt * k)
    R = (Mrho + BV + tt * k * ks * DL + (1 + tt * k) * NL) / ((1 - tt * k) * d0)
    E = main + R
    info = None
    if detail:
        info = {"sigma_star": ss, "kappa_star": ks, "k": k, "main": main, "M_rho": Mrho, "B_V": BV,
                "D_L": DL, "N_L": NL, "P1": P1, "P2": P2, "d0": d0, "eta": eta}
    return E, info


ETAS = (0.03, 0.08)


def E_best(ell, tau, p, mode, a=0, T=None, etas=ETAS, detail=False):
    best = (math.inf, None)
    for eta in etas:
        E, info = E_bound(ell, tau, p, mode, a, T, eta, detail=detail)
        if E < best[0]:
            best = (E, info)
    return best


# ---------------------------------------------------------------------------
# Section A: self-checks
# ---------------------------------------------------------------------------

def section_A():
    z0, lz, kap, K2, K3 = zeta_real_family(2.0)
    p0, p1, p2 = psi_family_real(1.0)
    zc = zeta_derivs(0.5 + 14.134725141734693j, 1)
    return {
        "zeta(2)-pi^2/6": sig(z0 - PI * PI / 6),
        "kappa(2)": sig(kap),
        "K2(2)": sig(K2),
        "K3(2)": sig(K3),
        "psi(1)+gamma": sig(p0 + 0.5772156649015329),
        "psi'(1)-pi^2/6": sig(p1 - PI * PI / 6),
        "psi''(1)+2zeta(3)": sig(p2 + 2 * 1.2020569031595942),
        "|zeta(1/2+i gamma_1)|": sig(abs(zc[0])),
        "table_rel_err_kappa(1.618)": sig(kappa_r(1.618) / zeta_real_family(1.618)[2] - 1),
        "table_rel_err_K3(1.3)": sig(K3_r(1.3) / zeta_real_family(1.3)[4] - 1),
        "table_rel_err_psi1(0.809)": sig(psi1_r(0.809) / psi_family_real(0.809)[1] - 1),
        "max_beta_prime_on_grid(<=1/12)": sig(max(beta_prime(0.001 * i) for i in range(1, 40001))),
        "min_beta_prime_on_grid(>=0)": sig(min(beta_prime(0.001 * i) for i in range(1, 40001))),
        "stirling_check_min_slack": sig(min(stirling_slack(complex(xr, yi))
                                            for xr in (0.6, 0.81, 1.3, 2.5, 7.0)
                                            for yi in (0.0, 0.5, 3.0, 40.0, 2500.0))),
    }


def beta_prime(u):
    """beta'(u) for beta(u) = 1/(e^u - 1) - 1/u + 1/2 (Binet's integrand), = (1/4)(1/v^2 - 1/sinh(v)^2), v = u/2."""
    v = u / 2
    if v < 1e-3:
        return (1 / 3 - v * v / 15 + 2 * v ** 4 / 189) / 4
    return 0.25 * (1 / (v * v) - 1 / math.sinh(v) ** 2)


def stirling_slack(z):
    """Re psi(z) + x/(2|z|^2) + 1/(12 x |z|) - log|z|  (Lemma 4.3: must be >= 0)."""
    x = z.real
    return digamma_c(z).real + x / (2 * abs(z) ** 2) + 1 / (12 * x * abs(z)) - math.log(abs(z))


# ---------------------------------------------------------------------------
# zeta: xi, alpha, saddle, and the Gaussian average
# ---------------------------------------------------------------------------

def logxi(s):
    s = complex(s)
    if s.real < 0.5:
        s = 1 - s
    z = zeta_derivs(s, 0)[0]
    return cmath.log(s / 2) + cmath.log(s - 1) - (s / 2) * math.log(PI) + loggamma_c(s / 2) + cmath.log(z)


def alpha_zeta(s):
    return 1 / s + 1 / (s - 1) - 0.5 * math.log(PI) + 0.5 * digamma_c(s / 2)


def alpha1_zeta(s):
    return -1 / s ** 2 - 1 / (s - 1) ** 2 + 0.25 * trigamma_c(s / 2)


def alpha2_zeta(s):
    return 2 / s ** 3 + 2 / (s - 1) ** 3 + 0.125 * tetragamma_c(s / 2)


def saddle(w, tau, alpha):
    s = w
    for _ in range(200):
        sn = w + tau * tau * alpha(s)
        if abs(sn - s) < 1e-15:
            return sn
        s = sn
    return s


def gauss_logderiv_zeta(x, p, t):
    """(G'/G)(w), w = (1+p+ix)/2, by trapezoid in h of the Gaussian average of xi (Lemma 3.1)."""
    tau = math.sqrt(t / 2)
    w = complex((1 + p) / 2, x / 2)
    cshift = tau * tau * alpha_zeta(w).real
    hlo = -p - cshift - 12 * tau
    hhi = cshift + 14 * tau
    n = int((hhi - hlo) / (tau / 6)) + 1
    ref = logxi(w + cshift)
    num = 0j
    den = 0j
    for i in range(n + 1):
        h = hlo + (hhi - hlo) * i / n
        val = cmath.exp(logxi(w + h) - ref - h * h / (2 * tau * tau))
        num += h * val
        den += val
    return num / den / (tau * tau)


# ---------------------------------------------------------------------------
# characters: kernel integral
# ---------------------------------------------------------------------------

def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def primitive_root(q):
    phi = q - 1
    fac = []
    m = phi
    d = 2
    while d * d <= m:
        if m % d == 0:
            fac.append(d)
            while m % d == 0:
                m //= d
        d += 1
    if m > 1:
        fac.append(m)
    for g in range(2, q):
        if all(pow(g, phi // f, q) != 1 for f in fac):
            return g


class Character:
    """Character of order k (k | q-1) modulo a prime q: chi(g^e) = exp(2 pi i e/k)."""

    def __init__(self, q, k):
        self.q = q
        self.k = k
        if k == 2:
            def chi(n):
                n %= q
                if n == 0:
                    return 0.0
                return 1.0 if pow(n, (q - 1) // 2, q) == 1 else -1.0
            self.chi = chi
            self.a = 0 if q % 4 == 1 else 1
            self.eps = 1.0 + 0j
        else:
            g = primitive_root(q)
            dlog = [0] * q
            x = 1
            for e in range(q - 1):
                dlog[x] = e
                x = (x * g) % q
            om = [cmath.exp(2j * PI * j / k) for j in range(k)]

            def chi(n):
                n %= q
                if n == 0:
                    return 0j
                return om[dlog[n] % k]
            self.chi = chi
            m1 = chi(q - 1)
            self.a = 0 if abs(m1 - 1) < 1e-9 else 1
            tau_g = 0j
            for n in range(1, q):
                tau_g += chi(n) * cmath.exp(2j * PI * n / q)
            self.eps = tau_g / ((1j) ** self.a * math.sqrt(q))
        self.alpha = 1 / cmath.sqrt(self.eps)
        self._grid()

    def _grid(self, du=2e-3, extra=3.0):
        q, a = self.q, self.a
        U = 0.25 * math.log(q / PI) + extra
        J = int(U / du)
        nmax = int(math.sqrt(60 * q / PI)) + 2
        cn = [self.chi(n) * n ** a for n in range(1, nmax + 1)]
        sq = [n * n for n in range(1, nmax + 1)]
        pos = []
        for j in range(J + 1):
            u = j * du
            e4 = math.exp(4 * u)
            m = min(nmax, int(math.sqrt(60 * q / (PI * e4))) + 2)
            c = PI * e4 / q
            tot = 0j
            for i in range(m):
                tot += cn[i] * math.exp(-c * sq[i])
            pos.append(4 * self.alpha * (PI / q) ** (a / 2) * math.exp((1 + 2 * a) * u) * tot)
        self.du = du
        self.u = [-(J - j) * du for j in range(J)] + [j * du for j in range(J + 1)]
        self.Phi = [pos[J - j].conjugate() for j in range(J)] + pos

    def H01(self, z, t):
        h0 = 0j
        h1 = 0j
        n = len(self.u)
        for i in range(n):
            u = self.u[i]
            wgt = 0.5 if i in (0, n - 1) else 1.0
            val = wgt * math.exp(t * u * u) * self.Phi[i] * cmath.exp(1j * z * u)
            h0 += val
            h1 += 1j * u * val
        return h0 * self.du, h1 * self.du

    def S(self, x, p, t):
        h0, h1 = self.H01(complex(x, p), t)
        return -(h1 / h0).imag

    def alpha_g(self, s):
        return 0.5 * math.log(self.q / PI) + 0.5 * digamma_c((s + self.a) / 2)


# ---------------------------------------------------------------------------
# Section B: identity check
# ---------------------------------------------------------------------------

def zeta_kernel_H01(z, t, du=1e-3, U=1.6):
    """H_t and H_t' for zeta from the Polymath kernel (even), trapezoid on [-U, U]."""
    h0 = 0j
    h1 = 0j
    J = int(U / du)
    for j in range(-J, J + 1):
        u = j * du
        au = abs(u)
        ph = 0.0
        for n in range(1, 40):
            e = PI * n * n * math.exp(4 * au)
            if e > 800:
                break
            ph += (2 * PI * PI * n ** 4 * math.exp(9 * au) - 3 * PI * n * n * math.exp(5 * au)) * math.exp(-e)
        wgt = 0.5 if abs(j) == J else 1.0
        val = wgt * math.exp(t * u * u) * ph * cmath.exp(1j * z * u)
        h0 += val
        h1 += 1j * u * val
    return h0 * du, h1 * du


def section_B():
    rows = []
    for (x, p, t) in ((3.0, math.sqrt(5), 0.0), (10.0, math.sqrt(5), 0.1), (20.0, 3.0, 0.3), (25.0, math.sqrt(5), 0.5)):
        h0, h1 = zeta_kernel_H01(complex(x, p), t)
        S_kernel = -(h1 / h0).imag
        if t > 0:
            S_gauss = 0.5 * gauss_logderiv_zeta(x, p, t).real
        else:
            w = complex((1 + p) / 2, x / 2)
            zd = zeta_derivs(w, 1)
            S_gauss = 0.5 * (alpha_zeta(w) + zd[1] / zd[0]).real
        rows.append({"case": "zeta", "x": x, "p": sig(p), "t": t, "S_kernel": sig(S_kernel),
                     "S_gaussian_average": sig(S_gauss), "difference": sig(S_kernel - S_gauss)})
    return {"rows": rows, "note": "kernel integral (Polymath normalization) against the Gaussian "
            "average E[xi(w + tau N)] of Lemma 3.1; two independent routes to S(x,p,t)"}


# ---------------------------------------------------------------------------
# Section C: transport law
# ---------------------------------------------------------------------------

def section_C():
    out = {"zeta": [], "characters": []}
    for x in (1000.0, 10000.0):
        for p in (math.sqrt(5), 3.0):
            w = complex((1 + p) / 2, x / 2)
            for t in (0.02, 0.1, 0.3, 0.5):
                tau = math.sqrt(t / 2)
                R = gauss_logderiv_zeta(x, p, t)
                s = saddle(w, tau, alpha_zeta)
                zd = zeta_derivs(s, 3)
                c1 = zd[1] / zd[0]
                dc1 = zd[2] / zd[0] - c1 * c1
                d2c1 = zd[3] / zd[0] - 3 * zd[2] * zd[1] / zd[0] ** 2 + 2 * c1 ** 3
                al = alpha_zeta(s)
                g0 = al + c1
                D1 = alpha1_zeta(s) + dc1
                D2 = alpha2_zeta(s) + d2c1
                eps = R - g0
                eps2 = tau * tau * (D1 * c1 + D2 / 2)
                out["zeta"].append({
                    "x": x, "p": sig(p), "t": t, "s_star": sig(s), "ell_star": sig(2 * al.real),
                    "kappa_star": sig(kappa_r(s.real)),
                    "S_direct": sig(R.real / 2), "S_main": sig(g0.real / 2),
                    "abs_eps": sig(abs(eps)), "eps": sig(eps), "eps_second_order": sig(eps2),
                    "floor_t0_C": sig(0.25 * (2 * alpha_zeta(w).real) - 0.5 * kappa_r((1 + p) / 2)),
                })
    chars = [(10007, 2), (10009, 2), (10009, 3), (100003, 2), (1000003, 2)]
    q4 = 1000001
    while not (is_prime(q4) and q4 % 4 == 1):
        q4 += 2
    chars.append((q4, 2))
    for (q, kk) in chars:
        ch = Character(q, kk)
        for p in (math.sqrt(5), 3.0):
            for x in (0.0, 2.0, 10.0):
                w = complex((1 + p) / 2, x / 2)
                S0 = ch.S(x, p, 0.0)
                lw = 2 * ch.alpha_g(w).real
                C0 = 0.25 * lw - 0.5 * kappa_r((1 + p) / 2)
                for t in (0.05, 0.2, 0.5):
                    tau = math.sqrt(t / 2)
                    St = ch.S(x, p, t)
                    s = saddle(w, tau, ch.alpha_g)
                    Smain = ch.S(2 * s.imag, 2 * s.real - 1, 0.0)
                    out["characters"].append({
                        "q": q, "order": kk, "parity": ch.a, "x": x, "p": sig(p), "t": t,
                        "s_star": sig(s), "ell_star": sig(2 * ch.alpha_g(s).real),
                        "S_t0": sig(S0), "S_direct": sig(St), "S_main": sig(Smain),
                        "abs_Re_eps": sig(2 * abs(St - Smain)), "floor_at_x_t0": sig(C0),
                    })
    return out


# ---------------------------------------------------------------------------
# Section D: bound against measured deviation
# ---------------------------------------------------------------------------

def section_D(C):
    rows = []
    for r in C["zeta"]:
        tau = math.sqrt(r["t"] / 2)
        E, info = E_best(r["ell_star"], tau, r["p"], "zeta", T=r["x"] / 2 - 1, detail=True)
        rows.append({"case": "zeta", "x": r["x"], "p": r["p"], "t": r["t"], "ell_star": r["ell_star"],
                     "measured_abs_eps": r["abs_eps"], "E": sig(E),
                     "ok": (E == math.inf) or (r["abs_eps"] <= E)})
    for r in C["characters"]:
        tau = math.sqrt(r["t"] / 2)
        E, info = E_best(r["ell_star"], tau, r["p"], "family", a=r["parity"], detail=True)
        rows.append({"case": "chi", "q": r["q"], "order": r["order"], "x": r["x"], "p": r["p"], "t": r["t"],
                     "ell_star": r["ell_star"], "measured_abs_Re_eps": r["abs_Re_eps"], "E": sig(E),
                     "ok": (E == math.inf) or (r["abs_Re_eps"] <= E)})
    applicable = [r for r in rows if r["E"] != math.inf and r["E"] != "inf"]
    return {"rows": rows, "all_ok": all(r["ok"] for r in rows),
            "n_applicable": len(applicable), "n_rows": len(rows)}


# ---------------------------------------------------------------------------
# Sections E-G
# ---------------------------------------------------------------------------

TGRID = (0.002, 0.01, 0.02, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.4, 0.5)
TFINE = (0.001, 0.002, 0.005, 0.01, 0.02, 0.03, 0.05, 0.075, 0.1, 0.125, 0.15, 0.175, 0.2,
         0.225, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5)


def section_E():
    out = []
    for (mode, a) in (("family", 0), ("family", 1), ("zeta", 0)):
        for p in (math.sqrt(5), 3.0, 4.0):
            s0 = (1 + p) / 2
            rows = []
            for ell in (8.0, 10.0, 11.0, 12.0, 16.0, 22.3, 26.7):
                worst = None
                for t in TGRID:
                    tau = math.sqrt(t / 2)
                    E, _ = E_best(ell, tau, p, mode, a, T=1e9)
                    gain = 0.5 * (kappa_r(s0) - kappa_r(s0 + tau * tau * ell / 2))
                    marg = gain - E / 2
                    if worst is None or marg < worst[0]:
                        worst = (marg, t, E / 2, gain)
                rows.append({"ell": ell, "min_over_t_of_gain_minus_E/2": sig(worst[0]),
                             "at_t": worst[1], "E/2": sig(worst[2]), "gain": sig(worst[3])})
            out.append({"mode": mode, "parity": a, "p": sig(p), "rows": rows})
    return {"tables": out, "note": "zeta mode at height T = 1e9; gain = (kappa(sigma_0) - kappa(sigma_0 + tau^2 ell/2))/2 only; "
            "the family floor also gains (1/4)(psi((sigma_*+a)/2) - psi((sigma_0+a)/2)) at x = 0, "
            "not counted here"}


def ell_star0(q, a, p, t):
    """ell_* at x = 0 (the real Gamma saddle) for the family."""
    tau2 = t / 2
    s0 = (1 + p) / 2
    sgm = s0
    for _ in range(200):
        sn = s0 + tau2 * (0.5 * math.log(q / PI) + 0.5 * psi_r((sgm + a) / 2))
        if abs(sn - sgm) < 1e-14:
            break
        sgm = sn
    return math.log(q / PI) + psi_r((sgm + a) / 2), sgm


def heat_floor_family(q, a, p, t, extra=(0.0, 1.0, 3.0)):
    """H(t) = min over ell >= ell_*^{(0)} (sampled) of ell/4 - kappa(sigma_0+tau^2 ell/2)/2 - E(ell)/2."""
    if t == 0:
        return C_floor_family(q, a, p), None
    tau = math.sqrt(t / 2)
    l0, _ = ell_star0(q, a, p, t)
    s0 = (1 + p) / 2
    best = None
    for d in extra:
        ell = l0 + d
        E, _ = E_best(ell, tau, p, "family", a)
        val = ell / 4 - 0.5 * kappa_r(s0 + tau * tau * ell / 2) - E / 2
        if best is None or val < best[0]:
            best = (val, ell, E)
    return best[0], best


def C_floor_family(q, a, p):
    s0 = (1 + p) / 2
    return 0.25 * (math.log(q / PI) + psi_r((s0 + a) / 2)) - 0.5 * kappa_r(s0)


def section_F():
    fam = []
    for q in (10 ** 4, 10 ** 6, 10 ** 8, 10 ** 10, 10 ** 12):
        for a in (0, 1):
            for p in (math.sqrt(5), 3.0):
                C0 = C_floor_family(q, a, p)
                worst = None
                for t in TFINE:
                    H, _ = heat_floor_family(q, a, p, t)
                    if worst is None or H - C0 < worst[0]:
                        worst = (H - C0, t, H)
                last = H - C0
                fam.append({"q": q, "parity": a, "p": sig(p), "C_qa(p)": sig(C0),
                            "min_t(H(t)-C)": sig(worst[0]), "at_t": worst[1],
                            "H(0.5)-C": sig(last),
                            "delta_zero_holds_on_grid": worst[0] >= 0})
    zet = []
    for (label, X) in (("Polymath X", 6.0e10 * 1.0), ("Platt-Trudgian X", 5e12 + 194858)):
        T = X / 2 - 1
        for p in (math.sqrt(5), 3.0, 4.0, 5.0, 6.0):
            s0 = (1 + p) / 2
            ellX = math.log(T / (2 * PI)) - 1e-6
            C0 = ellX / 4 - 0.5 * kappa_r(s0)
            worst = None
            for t in TFINE:
                tau = math.sqrt(t / 2)
                vals = []
                for d in (0.0, 1.0, 3.0):
                    ell = ellX + d
                    E, _ = E_best(ell, tau, p, "zeta", T=T)
                    vals.append(ell / 4 - 0.5 * kappa_r(s0 + tau * tau * ell / 2) - E / 2)
                H = min(vals)
                if worst is None or H - C0 < worst[0]:
                    worst = (H - C0, t)
            zet.append({"regime": label, "X": X, "p": sig(p), "ell_X": sig(ellX), "C_X(p)": sig(C0),
                        "min_t(H(t)-C)": sig(worst[0]), "at_t": worst[1],
                        "delta_zero_holds_on_grid": worst[0] >= 0})
    return {"family_every_height": fam, "zeta_beyond_X": zet,
            "note": "H(t) sampled at ell_*^{(0)} + {0,1,3}; monotonicity in ell is checked "
                    "numerically in section E's tables, not proved"}


def comparison_time_const(C, p, a0, m=4000):
    def rate(Qv):
        return 2 + (4 * C / p) * Qv - 8 * Qv / (p * p - Qv)
    for j in range(m + 1):
        if rate(a0 * j / m) <= 0:
            return None
    h = a0 / m
    tot = 1 / rate(0.0) + 1 / rate(a0)
    for j in range(1, m):
        tot += (4 if j % 2 else 2) / rate(j * h)
    return tot * h / 3


def comparison_time_heat(Hfun, p, a0, dt=2e-4):
    """RK4 for Q' = -2 - (4 H(t)/p) Q + 8 Q/(p^2 - Q) from Q(0) = a0 to Q = 0."""
    def f(t, Q):
        return -2 - (4 * Hfun(t) / p) * Q + 8 * Q / (p * p - Q)
    t = 0.0
    Q = a0
    while Q > 0 and t < 1.0:
        k1 = f(t, Q)
        k2 = f(t + dt / 2, Q + dt * k1 / 2)
        k3 = f(t + dt / 2, Q + dt * k2 / 2)
        k4 = f(t + dt, Q + dt * k3)
        Qn = Q + dt * (k1 + 2 * k2 + 2 * k3 + k4) / 6
        if Qn <= 0:
            return t + dt * Q / (Q - Qn)
        Q = Qn
        t += dt
    return None


def section_G():
    rows = []
    tg = (0.0, 0.01, 0.05, 0.1, 0.15, 0.2, 0.3, 0.4, 0.5)
    for q in (10 ** 6, 10 ** 8, 10 ** 10, 10 ** 12):
        for a in (0, 1):
            for (lab, a0) in (("a=1", 1.0), ("a=9/16", 9 / 16)):
                pmin = math.sqrt(5 * a0)
                # constant floor (Project 01's planning hypothesis), p on a 0.01 grid
                bc = None
                for i in range(0, 401):
                    p = pmin + 0.01 * i
                    C = C_floor_family(q, a, p)
                    if C <= 0:
                        continue
                    tt = comparison_time_const(C, p, a0)
                    if tt is not None and (bc is None or tt < bc[0]):
                        bc = (tt, p)
                if bc is None:
                    rows.append({"q": q, "parity": a, "start": lab, "constant_floor": None})
                    continue
                # heat floor, p on a 0.1 grid around the constant optimum
                bh = None
                for j in range(-3, 4):
                    p = bc[1] + 0.15 * j
                    if p < pmin:
                        continue
                    Hs = [heat_floor_family(q, a, p, t, extra=(0.0,))[0] for t in tg]

                    def Hfun(t, Hs=Hs):
                        if t >= tg[-1]:
                            return Hs[-1]
                        for i in range(len(tg) - 1):
                            if tg[i] <= t <= tg[i + 1]:
                                w = (t - tg[i]) / (tg[i + 1] - tg[i])
                                return Hs[i] + (Hs[i + 1] - Hs[i]) * w
                        return Hs[0]
                    if min(Hs) <= 0:
                        continue
                    tt = comparison_time_heat(Hfun, p, a0)
                    if tt is not None and (bh is None or tt < bh[0]):
                        bh = (tt, p, min(h - C_floor_family(q, a, p) for h in Hs[1:]))
                rows.append({"q": q, "parity": a, "start": lab,
                             "constant_floor_lambda": sig(bc[0], 6), "constant_floor_p": sig(bc[1], 4),
                             "heat_floor_lambda": None if bh is None else sig(bh[0], 6),
                             "heat_floor_p": None if bh is None else sig(bh[1], 4),
                             "heat_floor_min_excess_over_C": None if bh is None else sig(bh[2], 6)})
    return {"rows": rows, "note": "planning values: conditional on H12 and on a written comparison "
            "theorem (Project 01, Section 3.5); the heat floor H(t) is the proved bound of the note "
            "evaluated in floating point; lambda = time for Q to reach 0 (b -> 0)"}


def margin_family_ell(ell, p, a, mode, T=1e4):
    """min over the t-grid of gain - E/2 at fixed ell (kappa gain only)."""
    s0 = (1 + p) / 2
    worst = math.inf
    for t in TFINE:
        tau = math.sqrt(t / 2)
        E, _ = E_best(ell, tau, p, mode, a, T=T)
        gain = 0.5 * (kappa_r(s0) - kappa_r(s0 + tau * tau * ell / 2))
        worst = min(worst, gain - E / 2)
    return worst


def family_margin_q(q, a, p):
    """min over the t-grid of H(t) - C_{q,a}(p)."""
    C0 = C_floor_family(q, a, p)
    worst = math.inf
    for t in TFINE:
        H, _ = heat_floor_family(q, a, p, t, extra=(0.0,))
        worst = min(worst, H - C0)
    return worst


def section_H():
    """Thresholds: smallest ell (bisection) with gain >= E/2 on the t-grid (zeta mode with
    the Gamma constants of height T = 1e4, valid at every height x >= 2e4); smallest q with
    H(t) >= C_{q,a}(p) on the t-grid; small-t limits of E/tau^2 and gain/tau^2."""
    ells = []
    for (mode, a) in (("family", 0), ("family", 1), ("zeta", 0)):
        for p in (math.sqrt(5), 2.5, 3.0, 4.0):
            lo, hi = 3.0, 30.0
            if margin_family_ell(hi, p, a, mode) < 0:
                ells.append({"mode": mode, "parity": a, "p": sig(p), "ell_1": None})
                continue
            for _ in range(10):
                mid = (lo + hi) / 2
                if margin_family_ell(mid, p, a, mode) >= 0:
                    hi = mid
                else:
                    lo = mid
            s0 = (1 + p) / 2
            if mode == "family":
                kk = K2_r(s0) + 0.25 * psi1_r((s0 + a) / 2)
                k2 = K3_r(s0) - 0.125 * psi_family_real((s0 + a) / 2)[2]
            else:
                kk = K2_r(s0)
                k2 = K3_r(s0)
            ka = kappa_r(s0)
            ells.append({"mode": mode, "parity": a, "p": sig(p), "ell_1": sig(hi, 5),
                         "small_t_E/tau^2": sig(kk * ka + k2 / 2, 6),
                         "small_t_kappa_gain/(tau^2 ell)": sig(K2_r(s0) / 4, 6),
                         "small_t_threshold_kappa_gain_only": sig(2 * (kk * ka + k2 / 2) / K2_r(s0), 5),
                         "small_t_threshold_family_x0_with_psi_gain": sig(2 * (kk * ka + k2 / 2) / kk, 5)})
    qs = []
    for a in (0, 1):
        for p in (math.sqrt(5), 3.0):
            lo, hi = 2.0, 8.0     # log10 q
            if family_margin_q(10 ** hi, a, p) < 0:
                qs.append({"parity": a, "p": sig(p), "q_1": None})
                continue
            if family_margin_q(10 ** lo, a, p) >= 0:
                qs.append({"parity": a, "p": sig(p), "q_1": "<= 100"})
                continue
            for _ in range(10):
                mid = (lo + hi) / 2
                if family_margin_q(10 ** mid, a, p) >= 0:
                    hi = mid
                else:
                    lo = mid
            qs.append({"parity": a, "p": sig(p), "log10_q_1": sig(hi, 4), "q_1": sig(10 ** hi, 4),
                       "ell_0_at_q_1": sig(math.log(10 ** hi / PI) + psi_r(((1 + p) / 2 + a) / 2), 5)})
    mono = []
    for (mode, a, p) in (("family", 0, math.sqrt(5)), ("family", 1, 3.0), ("zeta", 0, math.sqrt(5))):
        for t in (0.002, 0.05, 0.2, 0.5):
            tau = math.sqrt(t / 2)
            vals = [E_best(ell, tau, p, mode, a, T=1e9)[0] for ell in (10.0, 11.0, 12.0, 14.0, 16.0, 20.0, 25.0, 30.0, 40.0)]
            fin = [v for v in vals if math.isfinite(v)]
            mono.append({"mode": mode, "parity": a, "p": sig(p), "t": t,
                         "E_on_ell_10_to_40": [sig(v, 6) for v in vals],
                         "nonincreasing": all(fin[i + 1] <= fin[i] * (1 + 1e-9) for i in range(len(fin) - 1))})
    return {"ell_thresholds": ells, "family_q_thresholds": qs, "E_monotone_in_ell": mono,
            "note": "thresholds use the 20-point grid TFINE (0.001 <= t <= 0.5); below t = 0.001 the "
                    "margin is tau^2 times the small-t coefficient plus O(tau^3), the latter not bounded "
                    "here; the conductor thresholds sample ell at ell_*^(0) only (monotonicity in ell is "
                    "the separate check E_monotone_in_ell)"}


def main():
    A = section_A()
    B = section_B()
    C = section_C()
    D = section_D(C)
    E = section_E()
    F = section_F()
    G = section_G()
    Hs = section_H()
    rec = {"programme": "height_p_transport_claude_20261017.py",
           "model": "Claude Opus 5.5 (claude-opus-5-5), Claude Cowork, effort max",
           "date": "2026-10-17",
           "A_self_checks": A, "B_identity": B, "C_transport_law": C, "D_bound_vs_measured": D,
           "E_bound_vs_gain": E, "F_lemma_Ap_floors": F, "G_strip_comparison_heat_floor": G,
           "H_thresholds": Hs}
    print(json.dumps(rec, indent=1, sort_keys=False))


if __name__ == "__main__":
    main()
