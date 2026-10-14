#!/usr/bin/env python3
"""Checks for direction 19 (Euler-factor controls), first note.

Prepared for Edward Baker with LLM assistance, 13 October 2026.
Model: Claude Opus 5.5 (configured identifier claude-opus-5-5), Claude Cowork,
reasoning effort max.

Standard library only.  Part E is exact rational arithmetic.  Part N is a
double-precision replay (contour-shifted trapezoid quadrature, Newton
iteration); it is numerical evidence, not an interval certificate.

Run:
    python3 -I check_euler_factor_controls_claude_20261013.py --output RECORD.json

Objects (see notes/1_EXACT_FLOW_WITNESSES_AND_ASYMPTOTICS_20261013.md):
    Phi_{c,p}(u) = Phi(u) + (c/2)[Phi(u+a) + Phi(u-a)],  a = (1/2) log p,
    H^{c,p}_t(x) = (1/2) int e^{t u^2 + i x u} Phi_{c,p}(u) du,
    exact flow:  H^{c,p}_t(x) = H_t(x) + (c/2) e^{t a^2}[e^{-iax} H_t(x+2ita) + e^{iax} H_t(x-2ita)],
    multiplier constant t_m = log(1/c)/a^2 = 4 log(1/c)/(log p)^2,
    off-line zeros at t=0:  |Im x| = delta = 2 arccosh(1/c)/log p,
    expansion:  Lambda_{c,p} = t_m - S2 t_m^2 + ...,  S2 = xi''(1/2)/(2 xi(1/2)).
"""

import argparse
import cmath
import hashlib
import json
import math
import platform
import random
import sys
from fractions import Fraction as Fr

PI = math.pi
RESULTS = {}
FAILURES = []


def record(section, name, value, ok=True):
    RESULTS.setdefault(section, {})[name] = value
    if not ok:
        FAILURES.append(f"{section}/{name}")


def sig(x, d=12):
    if isinstance(x, complex):
        return [sig(x.real, d), sig(x.imag, d)]
    if x == 0 or not math.isfinite(x):
        return x
    return float(f"{x:.{d}g}")


def err2(x):
    return float(f"{x:.2g}")


# ---------------------------------------------------------------------------
# Part E: exact algebra
# ---------------------------------------------------------------------------

def part_e():
    # E1: Q_p(X) = 1 + (2 sqrt p / c) X + p X^2.  With Y = sqrt(p) X: Y^2 + (2/c) Y + 1.
    # For Pythagorean c the roots are rational; neither has |Y| = 1, so neither root of Q_p
    # lies on |X| = p^{-1/2}, and the moduli are (1 +- sqrt(1-c^2))/(c sqrt p).
    rows = {}
    ok = True
    for c, s in ((Fr(3, 5), Fr(4, 5)), (Fr(5, 13), Fr(12, 13)), (Fr(8, 17), Fr(15, 17))):
        roots = [(-1 + s) / c, (-1 - s) / c]
        good = all(y * y + 2 / c * y + 1 == 0 for y in roots) and all(abs(y) != 1 for y in roots)
        good &= roots[0] * roots[1] == 1  # reciprocal pair: the Fricke symmetry of Q_p
        rows[str(c)] = [str(y) for y in roots]
        ok &= good
    record("E_exact", "E1_Qp_roots_off_critical_circle_and_reciprocal", rows, ok)

    # E2: Laguerre product rule L0(Hm) = m^2 L0(H) + H^2 L0(m), L0(f) = f'^2 - f f''.
    rng = random.Random(20261013)
    ok = True
    for _ in range(60):
        H, H1, H2, m, m1, m2 = (Fr(rng.randint(-60, 60), rng.randint(1, 9)) for _ in range(6))
        f, f1, f2 = H * m, H1 * m + H * m1, H2 * m + 2 * H1 * m1 + H * m2
        ok &= f1 * f1 - f * f2 == m * m * (H1 * H1 - H * H2) + H * H * (m1 * m1 - m * m2)
    record("E_exact", "E2_laguerre_product_rule", ok, ok)

    # E3: multiplier m_t = 1 + C cos(ax), C = c e^{t a^2}: L0(m_t) = C a^2 (C + cos ax).
    # Check with cos/sin replaced by a rational point (k, l) on the unit circle.
    ok = True
    for (k, l) in ((Fr(3, 5), Fr(4, 5)), (Fr(-5, 13), Fr(12, 13)), (Fr(-1), Fr(0)), (Fr(1), Fr(0))):
        for C in (Fr(1, 2), Fr(9, 10), Fr(1), Fr(7, 3)):
            for a in (Fr(1, 3), Fr(2)):
                m, m1, m2 = 1 + C * k, -C * a * l, -C * a * a * k
                ok &= m1 * m1 - m * m2 == C * a * a * (C + k)
    record("E_exact", "E3_multiplier_laguerre_negative_iff_cos_below_minus_C", ok, ok)

    # E4: algebra of the first-order expansion near x = 0.  With H(z)/H(0) = 1 + kappa z^2/2 + O(z^4),
    #   e^{-iax}(x+2ita)^2 + e^{iax}(x-2ita)^2 = 2(x^2 - 4t^2a^2) cos(ax) + 8 t a x sin(ax),
    # checked in Q(i) at rational points (k, l) = (cos, sin) of the unit circle.  At the leading
    # double zero (cos = -1, sin = 0, C = 1) the bracket R = xi^2 + C((xi^2 - 4 tau^2) cos + 4 tau xi sin)
    # equals 4 tau^2 for every xi, so every pair moves by the same first-order amount.
    ok = True
    for (k, l) in ((Fr(3, 5), Fr(4, 5)), (Fr(-5, 13), Fr(12, 13)), (Fr(-1), Fr(0)), (Fr(8, 17), Fr(-15, 17))):
        for x, t, a in ((Fr(2, 3), Fr(1, 7), Fr(5)), (Fr(-3), Fr(2, 9), Fr(1, 2))):
            def cm(u, v):
                return (u[0] * v[0] - u[1] * v[1], u[0] * v[1] + u[1] * v[0])
            em, ep = (k, -l), (k, l)            # e^{-iax}, e^{iax}
            zp, zm = (x, 2 * t * a), (x, -2 * t * a)  # x + 2ita, x - 2ita
            lhs = tuple(p_ + q_ for p_, q_ in zip(cm(em, cm(zp, zp)), cm(ep, cm(zm, zm))))
            rhs = (2 * (x * x - 4 * t * t * a * a) * k + 8 * t * a * x * l, Fr(0))
            ok &= lhs == rhs
    for xi2 in (Fr(1), Fr(9), Fr(225, 7)):
        for tau in (Fr(1, 3), Fr(7, 10), Fr(2)):
            ok &= xi2 + ((xi2 - 4 * tau * tau) * (-1) + 0) == 4 * tau * tau
    record("E_exact", "E4_first_order_expansion_algebra", ok, ok)


# ---------------------------------------------------------------------------
# Part N: numerics
# ---------------------------------------------------------------------------

def phi_series(z):
    e4, e5, e9 = cmath.exp(4 * z), cmath.exp(5 * z), cmath.exp(9 * z)
    s = 0j
    n = 1
    while True:
        t = (2 * PI * PI * n ** 4 * e9 - 3 * PI * n * n * e5) * cmath.exp(-PI * n * n * e4)
        s += t
        if abs(t) < 1e-32 and n >= 2:
            break
        n += 1
    return s


def phi(z):
    z = complex(z)
    return phi_series(-z if z.real < 0 else z)


class Source:
    """Trapezoid rule on Im u = theta for H^{(k)}(x) = (1/2) int (iu)^k e^{t u^2 + ixu} F(u) du."""

    def __init__(self, p=None, c=0.0, theta=0.25, per_unit=150):
        self.a = 0.5 * math.log(p) if p else 0.0
        U = max(3.2, self.a + 1.7)
        n = int(2 * U * per_unit)
        self.h = 2 * U / n
        self.us = [complex(-U + j * self.h, theta) for j in range(n + 1)]
        self.f = []
        for j, z in enumerate(self.us):
            w = 0.5 if j in (0, n) else 1.0
            val = phi(z)
            if c:
                val += 0.5 * c * (phi(z + self.a) + phi(z - self.a))
            self.f.append(w * val)
        self._t = None

    def derivs(self, t, x, kmax=3):
        if self._t != t:
            self.wt = [fj * cmath.exp(t * z * z) for fj, z in zip(self.f, self.us)]
            self._t = t
        out = [0j] * (kmax + 1)
        for wj, z in zip(self.wt, self.us):
            e = wj * cmath.exp(1j * x * z)
            iz = 1j * z
            pw = 1
            for k in range(kmax + 1):
                out[k] += pw * e
                pw *= iz
        return [0.5 * self.h * o for o in out]


def complex_zero(src, t, z, iters=80):
    for _ in range(iters):
        H = src.derivs(t, z, 1)
        dz = H[0] / H[1]
        z -= dz
        if abs(dz) < 1e-13 * max(1.0, abs(z)):
            break
    return z


def double_zero(src, t, x, iters=60):
    for _ in range(iters):
        H = src.derivs(t, x, 3)
        F0, F1 = H[0].real, H[1].real
        J00, J01, J10, J11 = -H[2].real, H[1].real, -H[3].real, H[2].real
        det = J00 * J11 - J01 * J10
        dt = (F0 * J11 - F1 * J01) / det
        dx = (J00 * F1 - J10 * F0) / det
        t -= dt
        x -= dx
        if abs(dt) < 1e-15 * max(1.0, abs(t)) and abs(dx) < 1e-13:
            break
    H = src.derivs(t, x, 2)
    return t, x, H[2].real


def track_pair(src, p, c, k):
    """Follow the k-th off-line zero (2k+1)pi/a + i delta from t = 0 to its collision."""
    a = 0.5 * math.log(p)
    delta = 2 * math.acosh(1 / c) / math.log(p)
    tm = math.log(1 / c) / (a * a)
    z0 = complex((2 * k + 1) * PI / a, delta)
    z = complex_zero(src, 0.0, z0)
    start_err = abs(z - z0)
    t, dt = 0.0, tm / 40
    while dt > 1e-7 * tm:
        zn = complex_zero(src, t + dt, z)
        if zn.imag < 1e-3 * delta or abs(zn - z) > 0.5 * delta:
            dt /= 2
            continue
        t, z = t + dt, zn
    lam, xs, hxx = double_zero(src, t + 0.5 * z.imag ** 2, z.real)
    return start_err, lam, xs, hxx


def part_n():
    # N0: S2 = xi''(1/2) / (2 xi(1/2)) = -2 H0''(0)/H0(0)
    theta_src = Source()
    H = theta_src.derivs(0.0, 0.0, 2)
    S2 = -2 * H[2].real / H[0].real
    record("N_float", "N0_curvature_S2", {"H0(0)": sig(H[0].real), "H0''(0)": sig(H[2].real), "S2": sig(S2),
                                         "xi(1/2)_from_H0": sig(8 * H[0].real)},
           abs(8 * H[0].real - 0.4971207781883141) < 1e-13)

    # N1: exact Newman-time flow of the controls (dilation lemma) versus direct quadrature
    rows = []
    worst = 0.0
    for p, c, t, x in ((2, 0.5, 1.0, 8.0), (101, 0.5, 0.1, 1.36), (3, 0.5, 0.5, complex(5.4, 0.3)), (10007, 0.9, 0.004, 0.7)):
        a = 0.5 * math.log(p)
        direct = Source(p, c).derivs(t, x, 0)[0]
        Hp = theta_src.derivs(t, x + 2j * t * a, 0)[0]
        Hm = theta_src.derivs(t, x - 2j * t * a, 0)[0]
        H0 = theta_src.derivs(t, x, 0)[0]
        flow = H0 + 0.5 * c * math.exp(t * a * a) * (cmath.exp(-1j * a * x) * Hp + cmath.exp(1j * a * x) * Hm)
        e = abs(direct - flow) / abs(direct)
        worst = max(worst, e)
        rows.append({"p": p, "c": c, "t": t, "x": sig(complex(x), 6), "direct": sig(direct, 10), "flow": sig(flow, 10), "rel_err": err2(e)})
    record("N_float", "N1_exact_flow_of_controls", {"rows": rows, "max_rel_err": err2(worst)}, worst < 1e-11)

    # N2: Lambda_{c,p} by tracking the three lowest off-line pairs and Newton on H = H_x = 0
    rows = []
    ok = True
    asym = []
    for p, c in ((2, 0.5), (3, 0.5), (5, 0.5), (11, 0.5), (41, 0.5), (43, 0.5), (101, 0.5), (1009, 0.5), (10007, 0.5),
                 (2, 0.9), (101, 0.9), (10007, 0.9)):
        src = Source(p, c)
        a = 0.5 * math.log(p)
        tm = math.log(1 / c) / (a * a)
        delta = 2 * math.acosh(1 / c) / math.log(p)
        pairs = []
        for k in (0, 1, 2):
            e0, lam, xs, hxx = track_pair(src, p, c, k)
            pairs.append((lam, xs))
            ok &= e0 < 1e-10 and abs(hxx) > 0
        lam0 = pairs[0][0]
        lowest_last = all(lam0 > pairs[k][0] for k in (1, 2))
        ok &= lowest_last and lam0 < tm < delta * delta / 2
        ratio_asym = (tm - lam0) / (S2 * tm * tm)
        asym.append(ratio_asym)
        rows.append({"p": p, "c": c, "delta": sig(delta, 8), "t_m": sig(tm, 10), "delta2_over_2": sig(delta * delta / 2, 8),
                     "Lambda": sig(lam0, 10), "x_star": sig(pairs[0][1], 8), "Lambda_over_t_m": sig(lam0 / tm, 8),
                     "t_m_minus_S2_t_m2": sig(tm - S2 * tm * tm, 10),
                     "(t_m-Lambda)/(S2 t_m^2)": sig(ratio_asym, 6),
                     "pair_collision_times_k0_k1_k2": [sig(v[0], 9) for v in pairs],
                     "lowest_pair_collides_last": lowest_last})
    # the asymptotic ratio should tend to 1 along p -> infinity at fixed c
    ok &= abs(asym[8] - 1) < 2e-3 and abs(asym[11] - 1) < 2e-3
    # threshold example used in the notes: Lambda_{1/2,41} > 0.2 > Lambda_{1/2,43}
    ok &= rows[4]["Lambda"] > 0.2 > rows[5]["Lambda"]
    record("N_float", "N2_lambda_table_and_expansion", {"rows": rows}, ok)

    # N3: Laguerre witnesses below Lambda, nonnegativity above
    rows = []
    ok = True
    for p, c in ((2, 0.5), (101, 0.5), (10007, 0.9)):
        src = Source(p, c)
        a = 0.5 * math.log(p)
        delta = 2 * math.acosh(1 / c) / math.log(p)
        _, lam, xs, _ = track_pair(src, p, c, 0)
        wit = []
        for frac in (0.0, 0.5, 0.9, 0.99):
            t = frac * lam
            z = complex(PI / a, delta)
            for j in range(0, 101):
                z = complex_zero(src, t * j / 100, z)
            H = src.derivs(t, z.real, 2)
            L0 = (H[1] ** 2 - H[0] * H[2]).real
            wit.append({"t_over_Lambda": frac, "x": sig(z.real, 8), "Im_zero": sig(z.imag, 6), "L0_over_H2": sig(L0 / H[0].real ** 2, 6)})
            ok &= L0 < 0
        X = 3 * xs + 10
        t = 1.01 * lam
        mn = None
        for i in range(1, 1201):
            x = X * i / 1200
            H = src.derivs(t, x, 2)
            val = (H[1] ** 2 - H[0] * H[2]).real
            scale = H[1].real ** 2 + abs(H[0].real * H[2].real)
            q = val / scale
            mn = q if mn is None or q < mn else mn
        ok &= mn > 0
        rows.append({"p": p, "c": c, "Lambda": sig(lam, 10), "witnesses": wit,
                     "t=1.01*Lambda_min_normalized_L0_on_grid": sig(mn, 6), "grid_x_max": sig(X, 6)})
    record("N_float", "N3_laguerre_witnesses", {"rows": rows}, ok)


    # N4: c = 1/2 over all primes p <= 47 (lowest pair only), and the witness at t = 0.2 for p = 41
    primes = [q for q in range(2, 48) if all(q % d for d in range(2, int(q ** 0.5) + 1))]
    lams = {}
    for q in primes:
        src = Source(q, 0.5)
        _, lam, xs, _ = track_pair(src, q, 0.5, 0)
        lams[q] = lam
    above = [q for q in primes if lams[q] > 0.2]
    monotone = all(lams[primes[i]] > lams[primes[i + 1]] for i in range(len(primes) - 1))
    src = Source(41, 0.5)
    a = 0.5 * math.log(41)
    delta = 2 * math.acosh(2) / math.log(41)
    z = complex(PI / a, delta)
    for j in range(0, 201):
        z = complex_zero(src, 0.2 * j / 200, z)
    H = src.derivs(0.2, z.real, 2)
    wit = (H[1] ** 2 - H[0] * H[2]).real / H[0].real ** 2
    ok = above == [q for q in primes if q <= 41] and monotone and wit < -1000
    record("N_float", "N4_half_strength_primes_up_to_47",
           {"Lambda_by_prime": {str(q): sig(lams[q], 9) for q in primes}, "primes_with_Lambda_above_0.2": above,
            "decreasing_in_p": monotone,
            "witness_p41_t0.2": {"x0": sig(z.real, 8), "Im_zero": sig(z.imag, 5), "L0_over_H2": sig(wit, 5)}}, ok)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", default=None)
    args = ap.parse_args()
    part_e()
    part_n()
    with open(__file__, "rb") as fh:
        digest = hashlib.sha256(fh.read()).hexdigest()
    rec = {
        "title": "Euler-factor controls: exact flow, Lambda table, expansion and Laguerre witnesses",
        "date": "2026-10-13",
        "prepared_for": "Edward Baker",
        "model": "Claude Opus 5.5 (claude-opus-5-5), Claude Cowork, effort max",
        "script_sha256": digest,
        "python": platform.python_version(),
        "status": "PASS" if not FAILURES else "FAIL",
        "failures": FAILURES,
        "results": RESULTS,
        "scope": "Part E exact rational; Part N double-precision numerics, not interval-certified.",
    }
    text = json.dumps(rec, indent=1, sort_keys=True)
    if args.output:
        with open(args.output, "w") as fh:
            fh.write(text + "\n")
    print(text)
    return 0 if not FAILURES else 1


if __name__ == "__main__":
    sys.exit(main())
