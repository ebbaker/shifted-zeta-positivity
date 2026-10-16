#!/usr/bin/env python3
"""Flipped-return completion of the growing Loewner trace in N=4 SYM.

Companion to N4SYM/notes/FLIPPED_RETURN_TRACE_ANALYSIS_20260924.md.
Prepared for Edward Baker by Claude Opus 5.5 (Anthropic; model identifier
claude-opus-5-5 as reported by the runtime; reasoning effort not exposed).

Standard library only; imports geometry, transport and background helpers
from check_trace_completion.py in the same directory. Prints one JSON object
(or writes --output FILE). Deterministic. No zeta function is evaluated.
Floating cases are diagnostics of analytic statements, not certificates.

Units: rescaled trace (Loewner time 1, driver slope s = a sqrt t); the flow
time is tau_hat = tau/t. B_1 = lambda (1 - 1/N^2)/(16 pi^2) is stripped:
the programs compute I with log W^(1) = B_1 I.

Groups
  F1  continuum one loop, vertex-excision scheme: exact cusp coefficient,
      finite part F(s), F(s)/s -> 4 pi/3;
  F2  one loop with the free gradient-flow propagator
      (1 - exp(-r^2/8 tau))/(4 pi^2 r^2): three regimes
        I   tau >> t      : I -> -s^2/(1296 tau_hat^2) + s^4/(5832 tau_hat)
        II  s^2 t << tau << t : sliver erf law
        III tau << s^2 t  : I -> -(2 pi s/3)[log(8 kappa) + gamma_E/2 - 2]
      with kappa = s/(6 sqrt(8 tau_hat));
  F3  second evolution equation: transported-derivative rule and the
      explicit d/dt of the generator, checked by finite differences.
"""
import argparse
import cmath
import json
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import check_trace_completion as tc  # noqa: E402

CASES = []
GAMMA_E = 0.5772156649015329


def case(name, group, kind, value, threshold, comparison='<=', note=''):
    value = float(value)
    passed = value <= threshold if comparison == '<=' else value >= threshold
    CASES.append(dict(name=name, group=group, kind=kind, value=value,
                      threshold=threshold, comparison=comparison,
                      passed=bool(passed), note=note))


GL = {n: tc.gauss_legendre(n) for n in (12, 16, 24)}


def integrate_edges(f, edges, order=16):
    nodes, weights = GL[order]
    total = 0.0
    for lo, hi in zip(edges[:-1], edges[1:]):
        h = hi - lo
        for x, w in zip(nodes, weights):
            total += 0.5 * h * w * f(lo + 0.5 * h * (x + 1))
    return total


def graded_one(a, b, h0, ratio=1.6):
    """Edges on [a, b] refined geometrically toward a (a < b)."""
    edges = [a]
    x = h0
    while a + x < b:
        edges.append(a + x)
        x *= ratio
    edges.append(b)
    return edges


def graded(lo, hi, h0, ratio=1.5):
    """Edges on [lo, hi] refined geometrically toward both ends."""
    mid = 0.5 * (lo + hi)
    left = graded_one(lo, mid, h0, ratio)
    right = [hi - (x - lo) for x in reversed(graded_one(lo, mid, h0, ratio))]
    return left + right[1:]


def bisect(f, lo, hi):
    flo = f(lo)
    for _ in range(90):
        mid = 0.5 * (lo + hi)
        fm = f(mid)
        if (fm > 0) == (flo > 0):
            lo, flo = mid, fm
        else:
            hi = mid
    return 0.5 * (lo + hi)


# ------------------------------------------------------------- geometry
def cusp_angles(s):
    tip = tc.solve_tip(s, 1.0)
    e = tip / abs(tip)
    alpha_b = abs(cmath.phase(e / 1j))
    _, dq = tc.trace_point(s, 1.0)
    alpha_t = abs(cmath.phase(dq / e))
    return alpha_b, alpha_t


def gamma1_over_b1(alpha, theta):
    """One-loop cusp Gamma/B_1 at deflection phi = pi - alpha, internal theta."""
    phi = math.pi - alpha
    return 2 * (phi / math.sin(phi)) * (math.cos(phi) - math.cos(theta))


# ------------------------------------------------------------- F1 excision
def trace_trace(s, u_lo, u_hi, kernel, order=16, panels=24):
    """int int over the excised trace of (|x'||y'| - x'.y') K(|x-y|) (both orders).

    kernel(r2) returns K as a function of r^2; kernel=None means 1/r^2 with
    the diagonal limit theta_u^2/2 used for coincident nodes.
    """
    nodes, weights = GL[order]
    xs, ws = [], []
    h = (u_hi - u_lo) / panels
    for p in range(panels):
        lo = u_lo + p * h
        for x, w in zip(nodes, weights):
            xs.append(lo + 0.5 * h * (x + 1))
            ws.append(0.5 * h * w)
    pts = [tc.trace_point(s, u) for u in xs]
    total = 0.0
    n = len(xs)
    for i in range(n):
        qi, di = pts[i]
        for j in range(n):
            qj, dj = pts[j]
            num = abs(di) * abs(dj) - (di * dj.conjugate()).real
            r2 = abs(qi - qj) ** 2
            if kernel is None:
                if i == j:
                    # theta_u^2/2 with theta_u = Im(q''/q')
                    u = xs[i]
                    q = qi
                    d2 = 2 * (s - 2 / q) + 2 * u * (2 / q ** 2) * di
                    th = (d2 / di).imag
                    val = th * th / 2
                else:
                    val = num / r2
            else:
                val = num * kernel(r2)
            total += ws[i] * ws[j] * val
    return total


def excision_one_loop(s, eps):
    tip = tc.solve_tip(s, 1.0)
    u_lo = bisect(lambda u: abs(tc.trace_point(s, u)[0]) - eps, 1e-9, 0.5)
    u_hi = bisect(lambda u: abs(tc.trace_point(s, u)[0] - tip) - eps, 0.5, 1.0)
    _, jf = tc.exchange_integrals(s, eps)
    tt = trace_trace(s, u_lo, u_hi, None)
    return jf + tt, jf, tt, abs(tip)


def f1_excision():
    res = {}
    for s in (0.2, 0.1, 0.05, 0.025, 0.0125):
        ab, at = cusp_angles(s)
        A = gamma1_over_b1(ab, math.pi) + gamma1_over_b1(at, math.pi)
        G, tt_last = {}, None
        for eps in (0.02, 0.01, 0.005, 0.0025):
            I, jf, tt, L = excision_one_loop(s, eps)
            G[eps] = I + A * math.log(L / eps)
            tt_last = tt
        d1, d2, d3 = G[0.01] - G[0.02], G[0.005] - G[0.01], G[0.0025] - G[0.005]
        # With the exact cusp coefficient the remainder is linear in eps, so
        # successive differences halve; a wrong coefficient would leave a
        # constant (error x log 2) instead.
        case(f'F1 exact cusp coefficient A(s): eps-differences halve at s={s:g}', 'F1', 'floating',
             abs(d3 / d2 - 0.5), 0.02, note=f'A = {A:.8e}; ratios {d2 / d1:.4f}, {d3 / d2:.4f}')
        case(f'F1 trace-trace term -> (2/9) s^2 (1 - eps)^2 at s={s:g}', 'F1', 'floating',
             abs(tt_last / (2 * s * s / 9 * (1 - 0.0025) ** 2) - 1), 0.1 * s + 1e-3)
        res[s] = 2 * G[0.0025] - G[0.005]
    # F(s)/s = f1 + s (c log(1/s) + c'): solve on the three smallest s.
    ss = (0.05, 0.025, 0.0125)
    rows = [(1.0, s * math.log(1 / s), s, res[s] / s) for s in ss]

    def det3(M):
        return (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1])
                - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
                + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]))
    M = [[r[0], r[1], r[2]] for r in rows]
    y = [r[3] for r in rows]
    D = det3(M)
    f1 = det3([[y[i], M[i][1], M[i][2]] for i in range(3)]) / D
    c = det3([[M[i][0], y[i], M[i][2]] for i in range(3)]) / D
    case('F1 finite part: F(s)/s -> 4 pi/3 (fit f1 + s(c log(1/s) + c\') on s = 0.05, 0.025, 0.0125)',
         'F1', 'floating', abs(f1 - 4 * math.pi / 3), 2e-3,
         note=f'f1 = {f1:.6f}, c = {c:.4f}; 4 pi/3 = {4 * math.pi / 3:.6f}')
    for s in (0.2, 0.1, 0.05, 0.025, 0.0125):
        case(f'F1 F(s)/s - 4 pi/3 is positive and below s log(1/s) at s={s:g}', 'F1', 'floating',
             (res[s] / s - 4 * math.pi / 3) / (s * math.log(1 / s)), 1.0,
             note=f'F(s) = {res[s]:.8e}')
    A2 = [(gamma1_over_b1(*[x for x in (cusp_angles(s)[0], math.pi)])
           + gamma1_over_b1(cusp_angles(s)[1], math.pi) - 2 * math.pi * s / 3) / s ** 2
          for s in (0.05, 0.025)]
    return res, dict(f1=f1, c_log=c, A2=A2[1])


# ------------------------------------------------------------- F2 flow
def flow_kernel(tau):
    def K(r2):
        x = r2 / (8 * tau)
        if x < 1e-4:
            return (1 - x / 2 + x * x / 6 - x ** 3 / 24) / (8 * tau)
        return -math.expm1(-x) / r2
    return K


def chord_integral_flow(l0, d, L, tau):
    """int_0^L K_tau(sqrt((l - l0)^2 + d^2)) dl, graded toward l0 from both sides."""
    K = flow_kernel(tau)
    scale = max(min(max(d, math.sqrt(tau)), L / 8), 1e-12)
    c = min(max(l0, 0.0), L)
    edges = []
    if c > 0:
        edges = [c - x for x in reversed(graded_one(0.0, c, min(scale, c / 2), 1.6))]
    else:
        edges = [0.0]
    if c < L:
        right = [c + x for x in graded_one(0.0, L - c, min(scale, (L - c) / 2), 1.6)]
        edges = edges + right[1:]
    return integrate_edges(lambda l: K((l - l0) ** 2 + d * d), edges, 12)


def flow_one_loop(s, tau_hat, trace_panels=24):
    tip = tc.solve_tip(s, 1.0)
    L = abs(tip)
    e = tip / L
    tau = tau_hat

    def cross(u):
        q, dq = tc.trace_point(s, u)
        speed = abs(dq)
        T = dq / speed
        l0 = (q * e.conjugate()).real
        d = abs((q * e.conjugate()).imag)
        te = (T * e.conjugate()).real
        return -2 * speed * (1 - te) * chord_integral_flow(l0, d, L, tau)
    h0 = min(0.01, 0.2 * math.sqrt(tau) / max(s, 1e-3))
    edges = graded(1e-12, 1.0, max(h0 * 1e-2, 1e-9), 1.5)
    jc = integrate_edges(cross, edges, 12)
    tt = trace_trace(s, 1e-9, 1.0, flow_kernel(tau), order=16, panels=trace_panels)
    return jc + tt


def regime_I_prediction(s, tau_hat):
    return -s ** 2 / (1296 * tau_hat ** 2) + s ** 4 / (5832 * tau_hat)


def regime_III_prediction(s, tau_hat):
    kappa = s / (6 * math.sqrt(8 * tau_hat))
    return -(2 * math.pi * s / 3) * (math.log(8 * kappa) + GAMMA_E / 2 - 2)


def sliver_erf(s, tau_hat):
    """Leading-order sliver law valid for sqrt(tau) << 1 (regimes II and III)."""
    nu = math.sqrt(8 * tau_hat)

    def f(y):
        z = y * (2 - y)
        return (1 / z - 1) * math.erf(s * z / (6 * nu))
    edges = graded(0.0, 2.0, 1e-8, 1.4)
    return -(2 * math.pi * s / 3) * integrate_edges(f, edges, 16)


def moments(s, powers=(0, 2, 4), order=24, panels=24):
    """M_n = int int_{loop x loop} N(x,y) |x-y|^n for the flipped loop (both orders)."""
    tip = tc.solve_tip(s, 1.0)
    L = abs(tip)
    e = tip / L
    nodes, weights = GL[order]
    us, uw = [], []
    h = 1.0 / panels
    for p in range(panels):
        for x, w in zip(nodes, weights):
            us.append(p * h + 0.5 * h * (x + 1))
            uw.append(0.5 * h * w)
    pts = [tc.trace_point(s, u) for u in us]
    ls = [L * u for u in us]
    lw = [L * w for w in uw]
    out = {n: 0.0 for n in powers}
    for (qi, di), wi in zip(pts, uw):
        for (qj, dj), wj in zip(pts, uw):
            num = abs(di) * abs(dj) - (di * dj.conjugate()).real
            r2 = abs(qi - qj) ** 2
            for n in powers:
                out[n] += wi * wj * num * r2 ** (n // 2)
        T = di / abs(di)
        te = (T * e.conjugate()).real
        for l, wl in zip(ls, lw):
            r2 = abs(qi - l * e) ** 2
            num = -abs(di) * (1 - te)
            for n in powers:
                out[n] += 2 * wi * wl * num * r2 ** (n // 2)
    return out


def trace_length(s):
    return integrate_edges(lambda u: abs(tc.trace_point(s, u)[1]), [i / 16 for i in range(17)], 24)


def f2_flow():
    out = {}
    # Regime I (tau >> t): expand K = 1/(8 tau) - r^2/(128 tau^2) + r^4/(3072 tau^3) - ...
    errs = []
    for s in (0.3, 0.15, 0.075):
        M = moments(s)
        L_ch = abs(tc.solve_tip(s, 1.0))
        dl = trace_length(s) - L_ch
        # M_0 is a cancellation of O(1) pieces down to (s^2/27)^2: tolerance set by that floor.
        case(f'F2 regime I: M_0 equals (L_trace - L_chord)^2 at s={s:g}', 'F2', 'floating',
             abs(M[0] / dl ** 2 - 1), 1e-14 / dl ** 2)
        case(f'F2 regime I: (L_trace - L_chord) -> s^2/27 at s={s:g}', 'F2', 'floating',
             abs(dl / (s * s / 27) - 1), 0.2 * s * s)
        c2 = -M[2] / 128
        err = abs(c2 / (-s * s / 1296) - 1)
        errs.append(err)
        case(f'F2 regime I: -M_2/128 -> -s^2/1296 (the 2 a^2 t^3 (C^Phi - C)/81 term) at s={s:g}', 'F2',
             'floating', err, 0.5 * s * s)
        for tau_hat in (200.0, 2000.0):
            full = flow_one_loop(s, tau_hat)
            series = M[0] / (8 * tau_hat) - M[2] / (128 * tau_hat ** 2) + M[4] / (3072 * tau_hat ** 3)
            # Absolute comparison on the scale of the individual (cancelling) pieces,
            # about (2/9) s^2/(8 tau): the two leading terms cancel near s^2 = 4.5/tau_hat.
            piece = 2 * s * s / (72 * tau_hat)
            case(f'F2 regime I: flowed one loop equals moment series at s={s:g}, tau/t={tau_hat:g}', 'F2',
                 'floating', abs(full - series) / piece, 1e-6,
                 note=f'full {full:.8e}, series {series:.8e}, smooth-field {regime_I_prediction(s, tau_hat):.8e}')
            out[('I', s, tau_hat)] = (full, series, regime_I_prediction(s, tau_hat))
    case('F2 regime I: relative error of -s^2/1296 falls like s^2 (ratio on halving s near 1/4)', 'F2',
         'floating', abs(errs[2] / errs[1] - 0.25), 0.05)
    # The erf sliver integral reproduces the regime-III asymptotic constant.
    for s, tau_hat in ((0.1, 1e-8), (0.1, 1e-10)):
        a, b = sliver_erf(s, tau_hat), regime_III_prediction(s, tau_hat)
        kappa = s / (6 * math.sqrt(8 * tau_hat))
        case(f'F2 sliver erf law -> -(2 pi s/3)[log(8 kappa) + gamma/2 - 2] at kappa={kappa:.3g}', 'F2',
             'floating', abs(a - b) / abs(b), 1.0 / kappa)
    # Regimes II-III: full flowed one loop = sliver law + s^2 D(tau_hat).
    D = {}
    for tau_hat in (1e-3, 1e-5, 1e-7):
        for s in (0.1, 0.05):
            got = flow_one_loop(s, tau_hat)
            sl = sliver_erf(s, tau_hat)
            D[(s, tau_hat)] = (got - sl) / s ** 2
            out[('II-III', s, tau_hat)] = (got, sl, regime_III_prediction(s, tau_hat))
        case(f'F2 regimes II-III: (flowed - sliver)/s^2 independent of s at tau/t={tau_hat:g}', 'F2',
             'floating', abs(D[(0.1, tau_hat)] / D[(0.05, tau_hat)] - 1), 0.03,
             note=f'D = {D[(0.1, tau_hat)]:.5f} (s=0.1), {D[(0.05, tau_hat)]:.5f} (s=0.05)')
    return out, D


# ------------------------------------------------------------- F3 second equation
def derived2(x1, x2):
    """Fields, first and second covariant derivatives for the tc background."""
    A1, A2, Ph, F12, D1P, D2P = tc.derived(x1, x2)
    mm, madd, msc, comm = tc.mm, tc.madd, tc.msc, tc.comm
    T1m, T2m, T3m = tc.T1m, tc.T2m, tc.T3m
    d1A1 = msc(0.2 * x2, T2m)
    d2A1 = madd(msc(0.3, T3m), msc(0.2 * x1, T2m))
    d1A2 = msc(-0.4, T3m)
    d2A2 = msc(0.2 * x2, T1m)
    # d_mu F12 = d_mu d1 A2 - d_mu d2 A1 - i([d_mu A1, A2] + [A1, d_mu A2])
    d1F = madd(msc(-1, msc(0.2, T2m)), msc(-1j, madd(comm(d1A1, A2), comm(A1, d1A2))))
    d2F = msc(-1j, madd(comm(d2A1, A2), comm(A1, d2A2)))
    DF = [madd(d1F, msc(-1j, comm(A1, F12))), madd(d2F, msc(-1j, comm(A2, F12)))]
    d1P = madd(msc(0.5, T1m), msc(0.2 * x2, T3m))
    d2P = madd(msc(-0.3, T2m), msc(0.2 * x1, T3m))
    ddP = [[[[0j, 0j], [0j, 0j]], msc(0.2, T3m)], [msc(0.2, T3m), [[0j, 0j], [0j, 0j]]]]
    dA = [[d1A1, d1A2], [d2A1, d2A2]]      # dA[mu][nu] = d_mu A_nu
    A = [A1, A2]
    dP = [d1P, d2P]
    DP = [D1P, D2P]
    DDP = [[None, None], [None, None]]
    for mu in range(2):
        for nu in range(2):
            d_mu_DnuP = madd(ddP[mu][nu], msc(-1j, madd(comm(dA[mu][nu], Ph), comm(A[nu], dP[mu]))))
            DDP[mu][nu] = madd(d_mu_DnuP, msc(-1j, comm(A[mu], DP[nu])))
    return A1, A2, Ph, F12, DP, DF, DDP


def generator_and_derivative(a, t, n):
    mm, madd, msc, comm, minv = tc.mm, tc.madd, tc.msc, tc.comm, tc.minv
    q = tc.solve_tip(a, t)
    qd = a - 2 / q
    qdd = 2 * qd / q ** 2
    Lq = abs(q)
    k = q.real * qd.imag - q.imag * qd.real
    kd = q.real * qdd.imag - q.imag * qdd.real
    rho_d = (q.conjugate() * qd).real / Lq
    rho_dd = (abs(qd) ** 2 + (q.conjugate() * qdd).real) / Lq - rho_d ** 2 / Lq
    speed_d = (qd.conjugate() * qdd).real / abs(qd)
    gam = abs(qd) - rho_d
    gam_d = speed_d - rho_dd
    qhat = q / Lq
    nhat = 1j * qhat
    nhat_d = -(k / Lq ** 2) * qhat

    def Nconn(r):
        A1, A2, Ph = tc.fields(r * q.real, r * q.imag)
        return madd(msc(1j * q.real, A1), msc(1j * q.imag, A2), msc(Lq, Ph))
    Rs = tc.rk4(Nconn, n)
    h = 1.0 / n
    Fh, Gh, Ph_h, DqF, DDnq, DPnd = [], [], [], [], [], []
    for idx, R in enumerate(Rs):
        r = idx * h
        A1, A2, Ph, F12, DP, DF, DDP = derived2(r * q.real, r * q.imag)
        Ri = minv(R)

        def hat(X):
            return mm(mm(Ri, X), R)
        Fh.append(hat(F12))
        Gh.append(hat(madd(msc(nhat.real, DP[0]), msc(nhat.imag, DP[1]))))
        Ph_h.append(hat(Ph))
        DqF.append(hat(madd(msc(qd.real, DF[0]), msc(qd.imag, DF[1]))))
        qv, nv = (qd.real, qd.imag), (nhat.real, nhat.imag)
        acc = [[0j, 0j], [0j, 0j]]
        for mu in range(2):
            for nu in range(2):
                acc = madd(acc, msc(qv[mu] * nv[nu], DDP[mu][nu]))
        DDnq.append(hat(acc))
        DPnd.append(hat(madd(msc(nhat_d.real, DP[0]), msc(nhat_d.imag, DP[1]))))
    # cumulative Simpson on even nodes (spacing 2h)
    Jc, Gc = {0: [[0j, 0j], [0j, 0j]]}, {0: [[0j, 0j], [0j, 0j]]}
    for m in range(2, n + 1, 2):
        def simp(arr, weightfun):
            return madd(msc(h / 3 * weightfun(m - 2), arr[m - 2]), msc(4 * h / 3 * weightfun(m - 1), arr[m - 1]),
                        msc(h / 3 * weightfun(m), arr[m]))
        Jc[m] = madd(Jc[m - 2], simp(Fh, lambda i: i * h))
        Gc[m] = madd(Gc[m - 2], simp(Gh, lambda i: i * h))
    Kc = {m: madd(msc(-1j * k, Jc[m]), msc(k, Gc[m]), msc(rho_d * m * h, Ph_h[m])) for m in Jc}
    J, G, P1 = Jc[n], Gc[n], Ph_h[n]
    X = madd(msc(1j * k, J), msc(-k, G), msc(gam, P1))
    # outer integrals on the even subgrid with Simpson (spacing 2h)
    H = 2 * h
    evens = list(range(0, n + 1, 2))
    Jdot = [[0j, 0j], [0j, 0j]]
    Gdot = [[0j, 0j], [0j, 0j]]
    for pos, m in enumerate(evens):
        w = H / 3 * (1 if pos in (0, len(evens) - 1) else (4 if pos % 2 else 2))
        r = m * h
        Jdot = madd(Jdot, msc(w * r, madd(msc(r, DqF[m]), comm(Fh[m], Kc[m]))))
        Gdot = madd(Gdot, msc(w * r, madd(msc(r, DDnq[m]), DPnd[m], comm(Gh[m], Kc[m]))))
    A1, A2, Ph, F12, DP, DF, DDP = derived2(q.real, q.imag)
    Ri, R = minv(Rs[-1]), Rs[-1]
    tipgrad = mm(mm(Ri, madd(msc(qd.real, DP[0]), msc(qd.imag, DP[1]))), R)
    P1dot = madd(tipgrad, comm(P1, Kc[n]))
    Xdot = madd(msc(1j * kd, J), msc(-kd, G), msc(gam_d, P1),
                msc(1j * k, Jdot), msc(-k, Gdot), msc(gam, P1dot))
    return X, Xdot


def f3_second_equation():
    mm, madd, msc = tc.mm, tc.madd, tc.msc
    n = 800
    for a in (1.3, -0.8):
        for t in (0.05, 0.3):
            X, Xdot = generator_and_derivative(a, t, n)
            dt = 1e-4 * t
            Xp, _ = generator_and_derivative(a, t + dt, n)
            Xm, _ = generator_and_derivative(a, t - dt, n)
            fd = msc(1 / (2 * dt), madd(Xp, msc(-1, Xm)))
            err = tc.mnorm(madd(fd, msc(-1, Xdot))) / tc.mnorm(Xdot)
            case(f'F3 dX/dt from the transported-derivative rule equals finite difference a={a:g} t={t:g}',
                 'F3', 'floating', err, 1e-6)
            # Second equation: d^2/dt^2 tr Q = tr((Xdot + X^2) Q)
            Q0 = tc.loop(a, t, 'flip', 400)

            def d2(hh):
                Qp, Qm = tc.loop(a, t + hh, 'flip', 400), tc.loop(a, t - hh, 'flip', 400)
                return (tc.tr(Qp) - 2 * tc.tr(Q0) + tc.tr(Qm)) / hh ** 2
            # A large step with Richardson: small steps are roundoff-limited because
            # tr Q is O(1) while its second derivative is O(1e-3) here.
            hh = 0.1 * t
            fd2 = (4 * d2(hh / 2) - d2(hh)) / 3   # error O(hh^4)
            pred = tc.tr(mm(madd(Xdot, mm(X, X)), Q0))
            case(f'F3 second equation: d^2 trQ/dt^2 = tr((Xdot + X^2) Q) a={a:g} t={t:g}', 'F3', 'floating',
                 abs(fd2 - pred) / max(abs(pred), 1e-3), 2e-5)
    # a = 0: X and Xdot vanish identically for the flipped family.
    X, Xdot = generator_and_derivative(0.0, 0.2, 400)
    case('F3 a = 0: generator and its derivative vanish', 'F3', 'floating',
         tc.mnorm(X) + tc.mnorm(Xdot), 1e-12)


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('--output')
    args = parser.parse_args()
    res, fit = f1_excision()
    flow, D = f2_flow()
    slope = (D[(0.05, 1e-7)] - D[(0.05, 1e-5)]) / math.log(100.0)
    case('F2 regime III: log(1/tau) slope of the s^2 term equals -A_2/2 (O(s^2) part of the cusp sum)', 'F2',
         'floating', abs(slope / (-fit['A2'] / 2) - 1), 0.1,
         note=f'slope {slope:.5f}; -A_2/2 = {-fit["A2"] / 2:.5f}')
    f3_second_equation()
    data = dict(
        program='check_flipped_return.py',
        prepared_by='Claude Opus 5.5 (Anthropic), model identifier claude-opus-5-5 as reported by the runtime; effort not exposed',
        prepared_for='Edward Baker',
        date='2026-09-24',
        parameters=dict(driver='u(t) = a t', units='rescaled t = 1; tau_hat = tau/t; B_1 stripped',
                        excision='Euclidean distance eps from base and tip on both legs',
                        flow_kernel='(1 - exp(-r^2/(8 tau)))/r^2 for gauge and scalar alike'),
        derived=dict(finite_part_excision={f'{s:g}': v for s, v in res.items()},
                     finite_part_fit=fit,
                     flow_s2_coefficient={f'{k[0]:g},{k[1]:g}': v for k, v in D.items()}),
        scope=('One-loop Maldacena-Wilson integrals for the flipped-return loop in two schemes, '
               'and the second smooth-field evolution equation on a classical test background. '
               'Not a nonperturbative statement, not interval arithmetic.'),
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
