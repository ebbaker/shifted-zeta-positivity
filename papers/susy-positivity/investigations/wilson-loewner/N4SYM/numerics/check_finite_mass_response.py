#!/usr/bin/env python3
"""Finite-mass heavy source in N=4 SYM at strong coupling: linearized
string-endpoint response, energy account, and the boundary 'tail' kernel.

Model: prepared with Claude Fable 5.1 (Anthropic; session configuration
``claude-fable-5-1``, the serving model can differ), 24 September 2026, for
Edward Baker.  Accompanies
``N4SYM/notes/FINITE_MASS_MEMORY_AND_QUARTIC_RESPONSE_20260924.md``.

Standard library only.  Deterministic.  Prints one JSON object (or writes it
with ``--output FILE``).  No zeta function is evaluated anywhere.

Units: AdS radius R = 1, string tension sqrt(lambda)/(2 pi).  The endpoint is
at z = z_m, the mass is m = sqrt(lambda)/(2 pi z_m).  One transverse
direction, linearized.  The retarded solution is
    x(t, z) = Xt(t - z) + z Xt'(t - z),
with Y(t) := Xt(t - z_m) the retarded auxiliary trajectory, so that
    F = m Y'',   X = Y + z_m Y',   m X'' = F + z_m F'.

Case groups
  A  wave equation, boundary condition, exact endpoint relations
  B  memory kernel, transfer function, pole, low-frequency expansion
  C  energy identity, string energy integral, flux
  D  point limit: Schott term as the cross term of a positive square;
     finite-time passivity where the renormalized point account fails
  E  nonrelativistic limits of the transcribed CGG equations (28) and (35)
  F  front test: integer exponents, universal collapse in omega z_m
  G  boundary tail kernel of the dilaton-coupled operator: g_4 polynomial,
     static-dipole sum rule, continuum of delays, integer high-frequency
     exponent, far-field polynomial, time-domain spread

Every case is a floating diagnostic of an analytic statement, not an
interval certificate.
"""
import argparse
import cmath
import json
import math
import sys

SQRT_LAMBDA = 20.0          # sqrt(lambda); the coefficient sqrt(lambda)/(2 pi) is 'Mikhailov'
MIK = SQRT_LAMBDA / (2 * math.pi)

CASES = []


def record(group, name, value, target, tol, note=""):
    if isinstance(value, complex) or isinstance(target, complex):
        err = abs(value - target)
    else:
        err = abs(value - target)
    ok = err <= tol
    CASES.append({
        "group": group, "name": name,
        "value": _ser(value), "target": _ser(target),
        "error": err, "tol": tol, "pass": bool(ok), "note": note,
    })
    return ok


def record_bool(group, name, ok, note=""):
    CASES.append({"group": group, "name": name, "value": bool(ok),
                  "target": True, "error": 0.0 if ok else 1.0, "tol": 0.0,
                  "pass": bool(ok), "note": note})
    return ok


def _ser(v):
    if isinstance(v, complex):
        return [v.real, v.imag]
    return v


# ----------------------------------------------------------------------------
# Drives.  Xt(u) is the boundary (auxiliary) trajectory; derivatives analytic.
# ----------------------------------------------------------------------------

class Gauss:
    """A e^{-(u-u0)^2/(2 w^2)} with analytic derivatives up to order 5."""

    def __init__(self, A=1.0, u0=0.0, w=1.0):
        self.A, self.u0, self.w = A, u0, w

    def d(self, u, n=0):
        s = (u - self.u0) / self.w
        g = self.A * math.exp(-0.5 * s * s)
        # Hermite-type coefficients for d^n/du^n e^{-s^2/2}
        h = [1.0, -s, s * s - 1.0, -s ** 3 + 3 * s, s ** 4 - 6 * s * s + 3,
             -s ** 5 + 10 * s ** 3 - 15 * s]
        return g * h[n] / self.w ** n


def gl_nodes(n):
    """Gauss-Legendre nodes/weights on [-1,1] by Newton iteration (deterministic)."""
    xs, ws = [], []
    for i in range(1, n + 1):
        x = math.cos(math.pi * (i - 0.25) / (n + 0.5))
        for _ in range(100):
            p0, p1 = 1.0, x
            for k in range(2, n + 1):
                p0, p1 = p1, ((2 * k - 1) * x * p1 - (k - 1) * p0) / k
            dp = n * (x * p1 - p0) / (x * x - 1.0)
            dx = p1 / dp
            x -= dx
            if abs(dx) < 1e-15:
                break
        p0, p1 = 1.0, x
        for k in range(2, n + 1):
            p0, p1 = p1, ((2 * k - 1) * x * p1 - (k - 1) * p0) / k
        dp = n * (x * p1 - p0) / (x * x - 1.0)
        xs.append(x)
        ws.append(2.0 / ((1 - x * x) * dp * dp))
    return xs, ws


GL_X, GL_W = gl_nodes(24)


def quad(f, a, b, panels=40):
    """Composite Gauss-Legendre on [a,b] (real or complex-valued f)."""
    h = (b - a) / panels
    total = 0.0
    for p in range(panels):
        c = a + (p + 0.5) * h
        for x, w in zip(GL_X, GL_W):
            total += w * f(c + 0.5 * h * x)
    return total * 0.5 * h


# ----------------------------------------------------------------------------
# Group A: wave equation, boundary condition, exact endpoint relations
# ----------------------------------------------------------------------------

def group_a():
    zm = 0.3
    m = MIK / zm
    Xt = Gauss(A=0.7, u0=1.5, w=0.8)

    def x(t, z):
        u = t - z
        return Xt.d(u, 0) + z * Xt.d(u, 1)

    # bulk equation  x_tt - x_zz + (2/z) x_z = 0 by central differences, Richardson
    def resid(t, z, h):
        xtt = (x(t + h, z) - 2 * x(t, z) + x(t - h, z)) / h / h
        xzz = (x(t, z + h) - 2 * x(t, z) + x(t, z - h)) / h / h
        xz = (x(t, z + h) - x(t, z - h)) / (2 * h)
        return xtt - xzz + 2.0 / z * xz

    for (t, z) in [(1.0, 0.5), (2.5, 1.2), (3.0, 2.0)]:
        r1, r2 = resid(t, z, 1e-2), resid(t, z, 5e-3)
        rich = (4 * r2 - r1) / 3
        record("A", "bulk_wave_eq_t%.1f_z%.1f" % (t, z), rich, 0.0, 2e-7,
               "Richardson-extrapolated residual of x_tt - x_zz + (2/z)x_z on the retarded solution")

    # exact relations: x'(t,z) = -z Xt''(t-z); F = m Y''; X = Y + z_m Y'
    for t in [0.5, 1.5, 2.5]:
        h = 1e-4
        xz = (x(t, zm + h) - x(t, zm - h)) / (2 * h)
        record("A", "x_z_at_endpoint_t%.1f" % t, xz, -zm * Xt.d(t - zm, 2), 1e-8,
               "x_z(t,z_m) = -z_m Xt''(t - z_m)")
        F = -(m / zm) * xz                    # boundary condition Pi^z = F
        record("A", "force_equals_m_Yddot_t%.1f" % t, F, m * Xt.d(t - zm, 2), 1e-6,
               "F(t) = m Y''(t) with Y(t) = Xt(t - z_m)")
        X = x(t, zm)
        record("A", "X_equals_Y_plus_zm_Ydot_t%.1f" % t, X,
               Xt.d(t - zm, 0) + zm * Xt.d(t - zm, 1), 1e-12)
        # m X'' = F + z_m F'
        Xdd = Xt.d(t - zm, 2) + zm * Xt.d(t - zm, 3)
        Fd = m * Xt.d(t - zm, 3)
        record("A", "mXdd_equals_F_plus_zmFd_t%.1f" % t, m * Xdd, F + zm * Fd, 1e-6,
               "linearized CGG equation, exact")


# ----------------------------------------------------------------------------
# Group B: memory kernel and transfer function
# ----------------------------------------------------------------------------

def group_b():
    zm = 0.25
    m = MIK / zm
    X = Gauss(A=1.0, u0=0.0, w=0.6)

    # Y(t) = (1/z_m) int_{-inf}^t e^{-(t-t')/z_m} X(t') dt'   satisfies Y + z_m Y' = X
    def Y(t):
        return quad(lambda tp: math.exp(-(t - tp) / zm) * X.d(tp, 0), t - 40 * zm - 6, t, panels=400) / zm

    for t in [-0.5, 0.3, 1.1]:
        h = 1e-3
        Yd = (Y(t + h) - Y(t - h)) / (2 * h)
        record("B", "memory_kernel_inverts_t%.1f" % t, Y(t) + zm * Yd, X.d(t, 0), 3e-6,
               "causal exponential kernel is the inverse of 1 + z_m d/dt")

    # transfer function chi_m(w) = -m w^2/(1 - i w z_m) from the mode solution
    for w in [0.3, 1.0, 3.0]:
        # mode x = (1 - i w z) e^{i w z} e^{-i w t};  F = -(m/z_m) x_z(z_m);  X = x(z_m)
        f = (1 - 1j * w * zm) * cmath.exp(1j * w * zm)
        fz = w * w * zm * cmath.exp(1j * w * zm)
        chi = (-(m / zm) * fz) / f
        record("B", "transfer_function_w%.1f" % w, chi, -m * w * w / (1 - 1j * w * zm), 1e-9,
               "chi_m(omega) = F^/X^ = -m omega^2/(1 - i omega z_m)")

    # pole in the lower half plane at omega = -i/z_m
    w0 = -1j / zm
    record("B", "pole_location", 1 - 1j * w0 * zm, 0.0, 1e-15, "1 - i omega z_m = 0 at omega = -i/z_m")
    record_bool("B", "pole_lower_half_plane", w0.imag < 0, "causal with e^{-i omega t}")

    # expansion coefficients: -m w^2 - i MIK w^3 + MIK z_m w^4 + i MIK z_m^2 w^5
    w = 0.02
    chi = -m * w * w / (1 - 1j * w * zm)
    series = -m * w ** 2 - 1j * MIK * w ** 3 + MIK * zm * w ** 4 + 1j * MIK * zm ** 2 * w ** 5
    record("B", "low_frequency_expansion", chi, series, MIK * zm ** 3 * w ** 6 * 1.01,
           "first two terms: mass and Abraham-Lorentz/Mikhailov with coefficient sqrt(lambda)/(2 pi)")
    record("B", "abraham_lorentz_coefficient", MIK, m * zm, 1e-12, "m z_m = sqrt(lambda)/(2 pi)")


# ----------------------------------------------------------------------------
# Group C: energy identity and string energy
# ----------------------------------------------------------------------------

def group_c():
    zm = 0.4
    m = MIK / zm
    Xt = Gauss(A=0.5, u0=2.0, w=0.7)

    def Yd(t, n=1):
        return Xt.d(t - zm, n)

    def F(t):
        return m * Yd(t, 2)

    def Xd(t):
        return Yd(t, 1) + zm * Yd(t, 2)

    for T in [1.0, 2.0, 2.6, 4.0, 8.0]:
        W = quad(lambda t: F(t) * Xd(t), -6.0, T, panels=200)
        rhs = 0.5 * m * Yd(T, 1) ** 2 + MIK * quad(lambda t: Yd(t, 2) ** 2, -6.0, T, panels=200)
        record("C", "work_identity_T%.1f" % T, W, rhs, 1e-9,
               "W(T) = (m/2) Y'(T)^2 + (sqrt(lambda)/2pi) int^T Y''^2")
        record_bool("C", "work_nonnegative_T%.1f" % T, W >= -1e-12)
        # radiated power = (z_m/m) F^2
        record("C", "radiated_power_T%.1f" % T, MIK * Yd(T, 2) ** 2, zm / m * F(T) ** 2, 1e-12,
               "(sqrt(lambda)/2pi) Y''^2 = (z_m/m) F^2 = (sqrt(lambda)/(2 pi m^2)) F^2")

    # string energy integral equals W(T); flux at large z equals radiated power
    def x_t(t, z):
        u = t - z
        return Xt.d(u, 1) + z * Xt.d(u, 2)

    def x_z(t, z):
        return -z * Xt.d(t - z, 2)

    for T in [2.6, 4.0]:
        E = quad(lambda z: (MIK / 2) / z / z * (x_t(T, z) ** 2 + x_z(T, z) ** 2), zm, T + 6.0, panels=300)
        W = quad(lambda t: F(t) * Xd(t), -6.0, T, panels=200)
        record("C", "string_energy_equals_work_T%.1f" % T, E, W, 1e-8,
               "int_{z_m}^inf H dz = W(T) on the retarded solution")
        zfar = 30.0
        Sz = -MIK / zfar / zfar * x_t(T + zfar, zfar) * x_z(T + zfar, zfar)
        record("C", "flux_at_depth_T%.1f" % T, Sz, MIK * Xt.d(T, 2) ** 2 * (1 + 0), MIK * abs(Xt.d(T, 1) * Xt.d(T, 2)) / zfar * 1.01 + 1e-14,
               "S_z -> (sqrt(lambda)/2pi) Xt''^2 up to the 1/z term")
        Sz_end = -MIK / zm / zm * x_t(T, zm) * x_z(T, zm)
        record("C", "flux_at_endpoint_equals_FXdot_T%.1f" % T, Sz_end, F(T) * Xd(T), 1e-10)


# ----------------------------------------------------------------------------
# Group D: point limit and passivity
# ----------------------------------------------------------------------------

def group_d():
    # X prescribed; Y from the memory kernel expansion (X smooth, z_m small)
    X = Gauss(A=1.0, u0=0.0, w=1.0)
    t = 0.4
    devs = []
    for zm in [0.05, 0.025, 0.0125]:
        m = MIK / zm
        # Y' = X' - z_m X'' + z_m^2 X''' - z_m^3 X'''' + ... (asymptotic)
        Yd = sum((-zm) ** k * X.d(t, k + 1) for k in range(0, 5))
        lhs = 0.5 * m * Yd ** 2 - (0.5 * m * X.d(t, 1) ** 2 - MIK * X.d(t, 1) * X.d(t, 2))
        pred = MIK / 2 * zm * (X.d(t, 2) ** 2 + 2 * X.d(t, 1) * X.d(t, 3))
        devs.append(lhs / pred - 1.0)
        record("D", "schott_cross_term_zm%.4f" % zm, lhs / pred, 1.0, 20 * zm,
               "(m/2)Y'^2 - [(m/2)X'^2 - (sqrt(lambda)/2pi) X'X''] = (sqrt(lambda)/4pi) z_m (X''^2 + 2X'X''') + O(sqrt(lambda) z_m^2)")
    record("D", "schott_remainder_is_linear_in_zm", devs[0] / devs[1], 2.0, 0.15,
           "the deviation from the O(z_m) prediction halves with z_m")
    record("D", "schott_remainder_is_linear_in_zm_2", devs[1] / devs[2], 2.0, 0.1)

    # the (1-s^2)^5 drive of the first note: renormalized point account negative just after onset,
    # finite-mass account nonnegative.
    def h(s, n=0):
        if abs(s) >= 1:
            return 0.0
        # (1-s^2)^5 derivatives via finite polynomial
        c = [1, 0, -5, 0, 10, 0, -10, 0, 5, 0, -1]  # coefficients of (1-s^2)^5 in powers of s
        val = 0.0
        for k, ck in enumerate(c):
            if ck == 0 or k < n:
                continue
            coef = ck
            for j in range(n):
                coef *= (k - j)
            val += coef * s ** (k - n)
        return val

    zm = 0.1
    m = MIK / zm
    # Y' solves z_m Y'' = X' - Y' (RK4 on a fine grid, from rest at the onset s = -1)
    N = 20000
    dt = 1.0 / N          # grid on [-1, 0]
    Yd_grid = [0.0]
    yd = 0.0
    for i in range(N):
        s = -1.0 + i * dt
        k1 = (h(s, 1) - yd) / zm
        k2 = (h(s + 0.5 * dt, 1) - (yd + 0.5 * dt * k1)) / zm
        k3 = (h(s + 0.5 * dt, 1) - (yd + 0.5 * dt * k2)) / zm
        k4 = (h(s + dt, 1) - (yd + dt * k3)) / zm
        yd += dt * (k1 + 2 * k2 + 2 * k3 + k4) / 6
        Yd_grid.append(yd)

    def Ydd(i):
        return (h(-1.0 + i * dt, 1) - Yd_grid[i]) / zm

    for T in [-0.98, -0.95, -0.9]:
        Xdd_int = quad(lambda s: h(s, 2) ** 2, -1.0, T, panels=100)
        point = 0.5 * m * h(T, 1) ** 2 + MIK * (Xdd_int - h(T, 1) * h(T, 2))
        record_bool("D", "point_account_negative_T%.2f" % T, point < 0,
                    "renormalized Lorentz-Dirac account with m_R = m is negative just after onset")
        iT = int(round((T + 1.0) / dt))
        W = 0.5 * m * Yd_grid[iT] ** 2
        rad = 0.0
        direct = 0.0
        for i in range(iT):          # trapezoid
            a, b = Ydd(i) ** 2, Ydd(i + 1) ** 2
            rad += 0.5 * dt * (a + b)
            direct += 0.5 * dt * (m * Ydd(i) * h(-1.0 + i * dt, 1) + m * Ydd(i + 1) * h(-1.0 + (i + 1) * dt, 1))
        W += MIK * rad
        record("D", "finite_mass_work_identity_T%.2f" % T, W, direct, 1e-5 * max(1e-12, abs(W)),
               "W(T) = int F X' equals the positive split (m/2)Y'^2 + (sqrt(lambda)/2pi) int Y''^2")
        record_bool("D", "finite_mass_account_nonnegative_T%.2f" % T, W >= 0.0,
                    "finite-time passivity restored by the finite mass; compare the negative point account")


# ----------------------------------------------------------------------------
# Group E: nonrelativistic limits of the transcribed CGG equations
# ----------------------------------------------------------------------------

def group_e():
    """Transcribed (fetch summary, arXiv:0906.1592 eqs. 28 and 35), one spatial direction,
    nonrelativistic with F^0 = F v.  Residual of  m v' = F + z_m F'  must be O(eps^3)."""
    zm = 0.3
    m = MIK / zm
    F = Gauss(A=1.0, u0=0.0, w=1.0)

    def lhs_rhs(eps, t):
        # v from the linearized equation to O(eps): m v' = eps(F + z_m F')  -> v = eps (int F + z_m F)/m
        Fi = quad(lambda s: F.d(s, 0), -8.0, t, panels=100)
        v = eps * (Fi + zm * F.d(t, 0)) / m
        vd = eps * (F.d(t, 0) + zm * F.d(t, 1)) / m
        Ft, Fd = eps * F.d(t, 0), eps * F.d(t, 1)
        F0 = Ft * v                     # F^0 = F.v
        F0d = Fd * v + Ft * vd
        Fsq = -F0 * F0 + Ft * Ft        # F^mu F_mu (mostly plus)
        den = math.sqrt(1 - zm * zm / m / m * Fsq)
        # d/dt of [m v - z_m F]/den  (spatial component), ignoring dtau/dt = 1 + O(eps^2)
        num = m * v - zm * Ft
        numd = m * vd - zm * Fd
        Fsqd = 2 * Ft * Fd - 2 * F0 * F0d
        dend = -0.5 * (zm * zm / m / m) * Fsqd / den
        lhs = (numd * den - num * dend) / den / den
        rhs = (Ft - (zm / m) * Fsq * v) / (den * den)
        return lhs - rhs, Ft, v

    t = 0.5
    res = []
    for eps in [0.2, 0.1, 0.05]:
        r, Ft, v = lhs_rhs(eps, t)
        res.append(abs(r))
    record("E", "cgg_eq28_residual_scaling_1", res[0] / res[1], 8.0, 1.5,
           "residual of eq. (28) against m v' = F + z_m F' scales as eps^3")
    record("E", "cgg_eq28_residual_scaling_2", res[1] / res[2], 8.0, 1.5)
    # radiation rate eq. (35), mu = 0 component
    eps = 0.05
    r, Ft, v = lhs_rhs(eps, t)
    F0 = Ft * v
    Fsq = Ft * Ft - F0 * F0
    dE = (MIK * Fsq / m / m) * (1.0 - (zm / m) * F0) / (1 - zm * zm / m / m * Fsq)
    record("E", "cgg_eq35_nonrelativistic", dE, (zm / m) * Ft * Ft, 1e-3 * (zm / m) * Ft * Ft,
           "dE/dt -> (sqrt(lambda)/(2 pi m^2)) F^2 = (z_m/m) F^2")
    record("E", "cgg_mass_relation", math.sqrt(SQRT_LAMBDA ** 2) / (2 * math.pi * m), zm, 1e-12,
           "z_m = sqrt(lambda)/(2 pi m)")


# ----------------------------------------------------------------------------
# Group F: front test on the endpoint channel
# ----------------------------------------------------------------------------

def group_f():
    def chi(w, zm):
        m = MIK / zm
        return -m * w * w / (1 - 1j * w * zm)

    zm = 0.2
    # low-frequency exponent 2, high-frequency exponent 1 (log-log slopes)
    lo = math.log(abs(chi(2e-3, zm)) / abs(chi(1e-3, zm))) / math.log(2)
    hi = math.log(abs(chi(2e4, zm)) / abs(chi(1e4, zm))) / math.log(2)
    record("F", "low_frequency_exponent", lo, 2.0, 1e-6)
    record("F", "high_frequency_exponent", hi, 1.0, 1e-6, "resistor-like at omega z_m >> 1: F ~ (m/z_m) X'")
    record("F", "high_frequency_coefficient", abs(chi(1e5, zm)) / 1e5, MIK / zm / zm, 1e-8 * MIK / zm / zm,
           "|chi| -> (m/z_m) omega = (2 pi m^2/sqrt(lambda)) omega")
    # universal collapse: chi(w; z_m) z_m^3/sqrt(lambda) = -(w z_m)^2/(1 - i w z_m) is a function of w z_m only
    for (z1, z2) in [(0.1, 0.4), (0.05, 1.0)]:
        v1 = chi(1.7 / z1, z1) * z1 ** 3 / MIK
        v2 = chi(1.7 / z2, z2) * z2 ** 3 / MIK
        record("F", "universal_collapse_%.2f_%.2f" % (z1, z2), v1, v2, 1e-12,
               "one scale: the shape of the kernel does not depend on m or lambda separately")
    record("F", "universal_form", chi(1.7 / 0.1, 0.1) * 0.1 ** 3 / MIK, -(1.7 ** 2) / (1 - 1.7j), 1e-12)
    # rational function: no branch cut. chi(w) - chi(-w)* vanishes for real w only via the pole term
    w = 1.3
    record("F", "reality_condition", chi(w, zm).conjugate(), chi(-w, zm), 1e-12,
           "chi(-omega) = conj chi(omega): real time-domain kernel")


# ----------------------------------------------------------------------------
# Group G: boundary tail kernel of the dilaton-coupled operator
# ----------------------------------------------------------------------------

def g4(rho, w):
    """d^4/ds^4 [e^{i w sqrt s}/(2 sqrt s)] at s = rho^2 (sympy-derived polynomial)."""
    y = w * rho
    return cmath.exp(1j * y) * (y ** 4 + 10j * y ** 3 - 45 * y * y - 105j * y + 105) / (32 * rho ** 9)


def g4_fd(rho, w):
    """Finite-difference check of g4 via the 4th derivative of e^{i w sqrt s}/(2 sqrt s)."""
    s0 = rho * rho
    h = 0.004 * s0

    def g(s):
        return cmath.exp(1j * w * math.sqrt(s)) / (2 * math.sqrt(s))

    def d4(h):
        return (g(s0 + 2 * h) - 4 * g(s0 + h) + 6 * g(s0) - 4 * g(s0 - h) + g(s0 - 2 * h)) / h ** 4
    a, b = d4(h), d4(h / 2)
    return (16 * b - a) / 15


def d4s_analytic(f, rho):
    """d^4/ds^4 at s = rho^2 of a function given through its rho-derivatives f(n), n = 0..4."""
    return (f(4) / (16 * rho ** 4) - 6 * f(3) / (16 * rho ** 5)
            + 15 * f(2) / (16 * rho ** 6) - 15 * f(1) / (16 * rho ** 7))


def tail_transfer(w, r, zm, theta=0.6, L=None, panels=200):
    """T(omega; r, z_m) = int_{z_m}^inf dz z^2 (1 - i w z) e^{i w (z - z_m)} g4(sqrt(z^2+r^2), w)
    on the rotated contour z = z_m + t e^{i theta}, which makes the integrand decay."""
    if L is None:
        L = 40.0 / max(w, 0.05) + 20.0
    e = cmath.exp(1j * theta)

    def f(t):
        z = zm + t * e
        rho = cmath.sqrt(z * z + r * r)
        y = w * rho
        g = cmath.exp(1j * y) * (y ** 4 + 10j * y ** 3 - 45 * y * y - 105j * y + 105) / (32 * rho ** 9)
        return z * z * (1 - 1j * w * z) * cmath.exp(1j * w * (z - zm)) * g * e
    return quad(f, 0.0, L, panels=panels)


def tail_polynomial(w, r, zm):
    """Closed form: T(omega; r, z_m) = e^{i omega r_m} P(omega), r_m = sqrt(r^2 + z_m^2).
    P is a quartic polynomial in omega (sympy-derived antiderivative, verified in G1)."""
    p = math.sqrt(r * r + zm * zm)
    z = zm
    S4 = 8 * p ** 4 + 24 * p ** 3 * z + 48 * p * p * z * z + 45 * p * z ** 3 + 15 * z ** 4
    c4 = z ** 3 / (32 * p ** 4 * (p + z))
    c3 = 1j * z * z * (2 * p + 3 * z) / (16 * p ** 5 * (p + z))
    c2 = -z * (8 * p ** 3 + 24 * p * p * z + 33 * p * z * z + 15 * z ** 3) / (32 * p ** 6 * (p + z) ** 2)
    c1 = -1j * S4 / (32 * p ** 7 * (p + z) ** 2)
    c0 = S4 / (32 * p ** 7 * (p + z) ** 3)
    return [c0, c1, c2, c3, c4], cmath.exp(1j * w * p) * (c0 + c1 * w + c2 * w ** 2 + c3 * w ** 3 + c4 * w ** 4)


def antiderivative(z, r, w):
    """G(z) with dG/dz = z^2 (1 - i w z) e^{i w z} g4(sqrt(z^2 + r^2), w)  (no e^{-i w z_m} factor)."""
    p = math.sqrt(z * z + r * r)
    N = (w ** 4 * p ** 3 * z ** 3 * (p + z) ** 2
         + 2j * w ** 3 * p * p * z * z * (p + z) ** 2 * (2 * p + 3 * z)
         - w * w * p * z * (p + z) * (8 * p ** 3 + 24 * p * p * z + 33 * p * z * z + 15 * z ** 3)
         - 1j * w * (p + z) * (8 * p ** 4 + 24 * p ** 3 * z + 48 * p * p * z * z + 45 * p * z ** 3 + 15 * z ** 4)
         + (8 * p ** 4 + 24 * p ** 3 * z + 48 * p * p * z * z + 45 * p * z ** 3 + 15 * z ** 4))
    return -cmath.exp(1j * w * (z + p)) * N / (32 * p ** 7 * (p + z) ** 3)


def group_g():
    # G1: g4 polynomial against finite differences; chain-rule operator
    for (rho, w) in [(1.0, 0.7), (2.0, 3.0)]:
        record("G", "g4_polynomial_rho%.1f_w%.1f" % (rho, w), g4(rho, w), g4_fd(rho, w), 3e-5 * abs(g4(rho, w)),
               "fourth s-derivative of e^{i omega sqrt s}/(2 sqrt s)")
    record("G", "g4_static_value", g4(1.3, 0.0), 105 / 32 / 1.3 ** 9, 1e-14)
    for (rho, w) in [(1.0, 0.7), (2.0, 3.0)]:
        def fr(n, rho=rho, w=w):
            tot = 0
            for k in range(n + 1):
                tot += math.comb(n, k) * (1j * w) ** k * cmath.exp(1j * w * rho) * ((-1) ** (n - k) * math.factorial(n - k) / (2 * rho ** (n - k + 1)))
            return tot
        record("G", "chain_rule_D4_rho%.1f_w%.1f" % (rho, w), d4s_analytic(fr, rho), g4(rho, w), 1e-12 * abs(g4(rho, w)))

    # G1b: the integrand is an exact z-derivative: dG/dz = integrand (central differences)
    r = 1.0
    for (z, w) in [(0.4, 0.9), (1.3, 2.5), (3.0, 0.3)]:
        h = 1e-4
        dG = (antiderivative(z + h, r, w) - antiderivative(z - h, r, w)) / (2 * h)
        integrand = z * z * (1 - 1j * w * z) * cmath.exp(1j * w * z) * g4(math.sqrt(z * z + r * r), w)
        record("G", "total_derivative_z%.1f_w%.1f" % (z, w), dG, integrand, 1e-6 * abs(integrand),
               "the depth integrand is a total derivative: the boundary response localizes at the endpoint")
    record("G", "antiderivative_vanishes_at_depth", abs(antiderivative(1e4, r, 1.0)), 0.0, 1e-8,
           "G -> 0 as z -> infinity (like omega^4/(64 z^2))")

    # G2: static dipole sum rule and the closed form
    for zm in [0.5, 0.1]:
        T0 = tail_transfer(0.0, r, zm, theta=0.0, L=400.0, panels=800)
        stat = 105 / 32 * quad(lambda z: z * z * (z * z + r * r) ** -4.5, zm, 400.0, panels=800)
        record("G", "static_dipole_sum_rule_zm%.1f" % zm, T0, stat, 1e-7,
               "omega -> 0 limit equals the gradient of the static profile (35 pi/16 convention check)")
        record("G", "static_closed_form_zm%.1f" % zm, tail_polynomial(0.0, r, zm)[1], stat, 1e-7,
               "S4/(32 r_m^7 (r_m + z_m)^3) = (105/32) int_{z_m}^inf z^2 (z^2 + r^2)^{-9/2} dz")
    # rotated contour agrees with the real-axis integral at moderate frequency
    Tr = tail_transfer(1.0, r, 0.5)
    Treal = quad(lambda z: z * z * (1 - 1j * z) * cmath.exp(1j * (z - 0.5)) * g4(math.sqrt(z * z + r * r), 1.0), 0.5, 3000.0, panels=60000)
    record("G", "contour_rotation_check", Tr, Treal, 2e-4 * abs(Tr), "real-axis oscillatory integral, truncated at z = 3000")

    # G3: the transfer function is EXACTLY e^{i omega r_m} times a quartic polynomial
    for (w, zm, rr) in [(0.7, 0.5, 1.0), (3.0, 0.5, 1.0), (11.0, 0.3, 1.0), (2.0, 0.2, 2.5), (40.0, 0.05, 1.0)]:
        T = tail_transfer(w, rr, zm, panels=400)
        _, P = tail_polynomial(w, rr, zm)
        record("G", "exact_locality_w%.1f_zm%.2f_r%.1f" % (w, zm, rr), T, P, 1e-8 * max(1.0, abs(P)),
               "T(omega) = e^{i omega r_m} P_4(omega): local in the retarded time, one fixed delay")
    # delays u(z) form a continuum, yet only the endpoint contributes (total derivative)
    zm = 0.3
    us = [z - zm + math.sqrt(z * z + r * r) for z in [zm + 0.1 * k for k in range(50)]]
    record_bool("G", "delay_monotone", all(b > a for a, b in zip(us, us[1:])),
                "u(z) = z - z_m + sqrt(z^2 + r^2) increases; the continuum of delays cancels exactly")
    record("G", "earliest_delay", us[0], math.sqrt(r * r + zm * zm), 1e-12)

    # G4: exponents and coefficients of the polynomial
    rm = math.sqrt(r * r + zm * zm)
    up = 1 + zm / rm
    cs, _ = tail_polynomial(0.0, r, zm)
    record("G", "quartic_coefficient", cs[4], zm ** 3 / (32 * rm ** 5 * up), 1e-15,
           "omega^4 coefficient = z_m^3/(32 r_m^5 u'(z_m)): endpoint stationary-phase-free asymptotics")
    slope = math.log(abs(tail_transfer(400.0, r, zm, panels=400)) / abs(tail_transfer(200.0, r, zm, panels=400))) / math.log(2)
    record("G", "high_frequency_exponent_zm0.3", slope, 4.0, 0.05, "integer exponent 4 for omega z_m >> 1")
    zm0 = 1e-6
    slope0 = math.log(abs(tail_transfer(400.0, r, zm0, panels=400)) / abs(tail_transfer(200.0, r, zm0, panels=400))) / math.log(2)
    record("G", "high_frequency_exponent_zm0", slope0, 1.0, 0.05, "massless limit: |T| ~ omega (one time derivative)")
    cs0, P0 = tail_polynomial(1.0, r, 0.0)
    record("G", "massless_closed_form", P0, cmath.exp(1j * r) * (1 - 1j * r) / (4 * r ** 6), 1e-15,
           "z_m -> 0: T = e^{i omega r}(1 - i omega r)/(4 r^6): Y and Y' at the retarded time only")

    # G5: far field: leading 1/r^5 coefficients [z_m^3, 4 i z_m^2, -8 z_m, -8 i]/32 for the omega^4..omega^1 terms
    zm = 0.3
    r_far = 4000.0
    cs, _ = tail_polynomial(0.0, r_far, zm)
    for k, target in [(4, zm ** 3 / 32), (3, 4j * zm ** 2 / 32), (2, -8 * zm / 32), (1, -8j / 32)]:
        record("G", "far_field_coefficient_omega%d" % k, cs[k] * r_far ** 5, target, 5e-4 * abs(target),
               "leading far-field polynomial, local in t - r")

    # G6: time domain: response to a short pulse equals the differential operator on Y at t - r_m
    zm = 0.3
    r = 1.0
    rm = math.sqrt(r * r + zm * zm)
    Yp = Gauss(A=1.0, u0=0.0, w=0.05)

    def xk(tp, z, k):
        u = tp - z + zm
        return Yp.d(u, k) + z * Yp.d(u, k + 1)

    def O(t):
        def integrand(z):
            rho = math.sqrt(z * z + r * r)

            def f(n):
                tot = 0.0
                for k in range(n + 1):
                    tot += (math.comb(n, k) * (-1) ** k * xk(t - rho, z, k)
                            * (-1) ** (n - k) * math.factorial(n - k) / (2 * rho ** (n - k + 1)))
                return tot
            return z * z * d4s_analytic(f, rho)
        return quad(integrand, zm, zm + 6.0, panels=120)

    cs, _ = tail_polynomial(0.0, r, zm)
    # omega^k e^{-i omega t'} = (i d/dt')^k e^{-i omega t'}  ->  O(t) = sum_k c_k i^k Y^{(k)}(t - r_m)
    def O_local(t):
        return sum((cs[k] * (1j) ** k).real * Yp.d(t - rm, k) for k in range(5))
    for dt in [-0.08, 0.0, 0.05, 0.12]:
        t = rm + dt
        record("G", "time_domain_locality_dt%+.2f" % dt, O(t), O_local(t), 1e-6 * abs(O_local(rm)),
               "direct depth integral equals the local fourth-order operator on Y at t - r_m")
    late = max(abs(O(rm + s)) for s in [0.8, 1.4, 2.2])
    record_bool("G", "no_tail_after_arrival", late < 1e-9 * abs(O_local(rm)),
                "no continuum of delays: the response vanishes once the pulse has passed")
    record_bool("G", "no_signal_before_arrival", abs(O(rm - 0.4)) < 1e-9 * abs(O_local(rm)), "causality")
    record_bool("G", "polynomial_coefficients_real_imaginary_alternate",
                all(abs((cs[k] * (1j) ** k).imag) < 1e-15 for k in range(5)),
                "c_k i^k real: the time-domain operator is real")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output")
    args = ap.parse_args()
    for g in (group_a, group_b, group_c, group_d, group_e, group_f, group_g):
        g()
    n_pass = sum(1 for c in CASES if c["pass"])
    out = {
        "program": "check_finite_mass_response.py",
        "model": "Claude Fable 5.1 (Anthropic), session configuration claude-fable-5-1",
        "date": "2026-09-24",
        "sqrt_lambda": SQRT_LAMBDA,
        "cases": len(CASES),
        "passed": n_pass,
        "all_pass": n_pass == len(CASES),
        "results": CASES,
    }
    text = json.dumps(out, indent=1, sort_keys=False)
    if args.output:
        with open(args.output, "w") as fh:
            fh.write(text + "\n")
    else:
        sys.stdout.write(text + "\n")
    return 0 if out["all_pass"] else 1


if __name__ == "__main__":
    sys.exit(main())
