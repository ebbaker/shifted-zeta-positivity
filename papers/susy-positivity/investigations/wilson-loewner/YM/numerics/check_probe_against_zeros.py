#!/usr/bin/env python3
"""Independent floating controls for the consolidated YM manuscript (25 Sept 2026).

Prepared for Edward Baker by Claude (Anthropic). Model line: claude-fable-5-1
(Fable 5.1) per the runtime environment, session configured as claude-opus-5-5;
the serving model may differ. Reasoning effort not exposed.

These controls were written from the manuscript's displayed formulas only, not
from the other programs in this directory, and they use different discretizations.
They add one control the existing suite lacks: the complete Weil form Q of
Section 1, evaluated on the manuscript's own detecting probe f_* (Section 10),
is compared with the sum over the first 700 nontrivial zeta zeros.  This tests
the normalization of Q (digamma multiplier, contact constant, the factor
-2 Lambda(a)/sqrt(a), and the Fourier convention) against arithmetic that the
manuscript never uses.  Floating diagnostics only: nothing here proves RH, a
limiting theorem, positivity, or the occurrence of a YM source.

Only NumPy is required.  The 700 zero ordinates are read from
records/zeta-zeros-700.json (computed once with mpmath.zetazero; pass
--regenerate-zeros to recompute them, which needs mpmath and about two minutes).

Controls:
  1  m_+(0) = psi(1/4) - log pi = -gamma - pi/2 - 3 log 2 - log pi
  2  Theorem 5.4 (complete archimedean limit): <F_R f, C_rho F_R g>, computed by
     direct theta-quadrature of the log-angle term, converges to
     (1/2pi) int m_+ conj(fhat) ghat for a complex pair f != g.
  3  Theorem 4.2 with a NON-Haar marginal rho having five harmonics: the prime
     mixed limit a^{-1/2} <f, U_{log a} g> (a = 2, 3, 5), the wound norms
     rho_a(0)/rho(0) ||f||^2 (a = 2, 3), and the gcd formula for (a,b) = (2,4), (2,3).
  4  Section 10: C_*(t) from the definition (archimedean integral plus von
     Mangoldt sum) equals sum_gamma 2 |fhat_*(gamma)|^2 cos(gamma t) over the
     first 700 zeros, at twelve values of t in [0, 7].
  5  The closed archimedean tail C_{*,inf}(t) = -sum_j e^{-(2j+1/2)t} F(2j+1/2)F(-2j-1/2).
  6  Corollary 10.5: the empirical mean square of C_* on [0, 200] equals the
     almost-periodic prediction sum 2|w_gamma|^2 within one percent, and
     Q[f_*] = C_*(0) > 0.
"""
import argparse
import hashlib
import json
import math
import platform
from pathlib import Path

import numpy as np

EULER = 0.57721566490153286060
HERE = Path(__file__).resolve().parent
ZERO_FILE = HERE / "records" / "zeta-zeros-700.json"


# ----------------------------------------------------------------- digamma
def digamma_complex(z):
    """psi(z) for complex arrays: recurrence to Re z >= 24, then the asymptotic series."""
    z = np.asarray(z, dtype=complex).copy()
    shift = np.zeros_like(z)
    for _ in range(30):
        mask = z.real < 24
        if not mask.any():
            break
        shift[mask] += 1.0 / z[mask]
        z[mask] += 1.0
    inv = 1.0 / z
    inv2 = inv * inv
    # Bernoulli coefficients B_{2k}/(2k): 1/12, -1/120, 1/252, -1/240, 1/132, -691/32760, 1/12
    series = inv2 * (1/12 - inv2 * (1/120 - inv2 * (1/252 - inv2 * (1/240 - inv2 * (1/132 - inv2 * (691/32760 - inv2/12))))))
    return np.log(z) - 0.5 * inv - series - shift


def m_plus(tau):
    return digamma_complex(0.25 + 0.5j * np.asarray(tau, dtype=float)).real - math.log(math.pi)


# ----------------------------------------------------------------- probe
AJ = 2.0 ** -np.arange(1, 49)


def B_transform(z):
    z = np.asarray(z, dtype=complex)
    out = np.ones_like(z)
    for a in AJ:
        w = a * z
        small = np.abs(w) < 1e-4
        safe = np.where(small, 1.0, w)
        out = out * np.where(small, 1.0 + w * w / 6.0, np.sinh(safe) / safe)
    return out


B_ONE = B_transform(1.0).real


def F_detect(z):
    return (0.25 - np.asarray(z, dtype=complex) ** 2) * B_transform(1.0 + np.asarray(z, dtype=complex)) / B_ONE


def fhat_probe(tau):
    return F_detect(-1j * np.asarray(tau, dtype=float))


def von_mangoldt(limit):
    prime = np.ones(limit + 1, dtype=bool)
    prime[:2] = False
    for p in range(2, int(limit ** 0.5) + 1):
        if prime[p]:
            prime[p * p::p] = False
    weights = np.zeros(limit + 1)
    for p in np.flatnonzero(prime):
        n = int(p)
        while n <= limit:
            weights[n] = math.log(float(p))
            n *= int(p)
    labels = np.flatnonzero(weights)
    return labels, weights[labels]


# ----------------------------------------------------------------- tests
def bump(x):
    x = np.asarray(x, dtype=float)
    out = np.zeros_like(x)
    m = np.abs(x) < 1.0
    out[m] = np.exp(-1.0 / (1.0 - x[m] ** 2))
    return out


def f_test(x):
    return bump(x) * (1.0 + 0.5 * np.asarray(x)) * np.exp(0.8j * np.asarray(x))


def g_test(x):
    return bump(x) * (1.0 - 0.3 * np.asarray(x) ** 2) * np.exp(-0.45j * np.asarray(x))


XG = np.linspace(-3.0, 3.0, 60001)


def fourier(fun, tau):
    fx = fun(XG)
    return np.array([np.trapezoid(fx * np.exp(-1j * t * XG), XG) for t in tau])


def inner_shift(f1, f2, s):
    return np.trapezoid(np.conj(f1(XG)) * f2(XG - s), XG)


def gl_nodes(npanels, upper):
    x, w = np.polynomial.legendre.leggauss(16)
    edges = np.linspace(0.0, upper, npanels + 1)
    u = np.concatenate([0.5 * (b - a) * x + 0.5 * (b + a) for a, b in zip(edges[:-1], edges[1:])])
    wt = np.concatenate([0.5 * (b - a) * w for a, b in zip(edges[:-1], edges[1:])])
    return u, wt


def control_archimedean(target, N):
    """Theorem 5.4 by direct quadrature: electric sum + log-angle integral on (0, pi)."""
    n = np.arange(max(1, int(N * math.exp(-1)) - 2), int(N * math.exp(1)) + 3)
    cf = f_test(np.log(n / N)) / np.sqrt(n)
    cg = g_test(np.log(n / N)) / np.sqrt(n)
    electric = np.sum(np.conj(cf) * cg * np.log(n))
    u, wu = gl_nodes(6 * N + 400, 42.0)
    theta = math.pi * np.exp(-u)
    weight = wu * theta * np.log(theta / (2 * math.pi))
    angle = 0.0 + 0.0j
    for i0 in range(0, len(theta), 4096):
        cosm = np.cos(np.outer(theta[i0:i0 + 4096], n))
        Gf = math.sqrt(2 / math.pi) * cosm @ cf
        Gg = math.sqrt(2 / math.pi) * cosm @ cg
        angle += np.sum(weight[i0:i0 + 4096] * np.conj(Gf) * Gg)
    value = electric + angle
    return {"N": int(N), "electric": [electric.real, electric.imag], "angle": [angle.real, angle.imag],
            "value": [value.real, value.imag], "absolute_error": float(abs(value - target))}


class Marginal:
    """rho(theta) = c (1 + 0.3 cos th + 0.25 cos 2th + 0.1 cos 3th - 0.05 cos 5th), t_0 - t_2 = 1."""

    def __init__(self):
        half = {0: 1.0, 1: 0.15, 2: 0.125, 3: 0.05, 5: -0.025}
        c = 1.0 / (half[0] - half[2])
        self.t = {}
        for k, v in half.items():
            self.t[k] = c * v
            self.t[-k] = c * v

    def tk(self, k):
        return self.t.get(int(k), 0.0)

    def rho(self, theta):
        return sum(self.tk(k) * math.cos(k * theta) for k in range(-5, 6))

    def rho_a0(self, a):
        return sum(self.rho(2 * math.pi * j / a) for j in range(a)) / a

    def pair(self, cn, n_idx, dm, m_idx):
        """<sum c_n chi_n, sum d_m chi_m>_nu = sum conj(c_n) d_m (t_{n-m} - t_{n+m})."""
        pos = {int(m): i for i, m in enumerate(m_idx)}
        tot = 0.0 + 0.0j
        for i, nn in enumerate(n_idx):
            for k in range(-5, 6):
                if nn - k in pos:
                    tot += np.conj(cn[i]) * dm[pos[nn - k]] * self.tk(k)
                if k - nn in pos:
                    tot -= np.conj(cn[i]) * dm[pos[k - nn]] * self.tk(k)
        return tot


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    parser.add_argument("--regenerate-zeros", action="store_true")
    parser.add_argument("--extended", action="store_true", help="also test t = 10 (slower)")
    args = parser.parse_args()

    checks = []

    def check(name, error, tol, **extra):
        rec = {"name": name, "error": float(error), "tolerance": float(tol), "passed": bool(abs(error) <= tol)}
        rec.update(extra)
        checks.append(rec)

    # 1. contact constant
    m0 = float(m_plus(0.0))
    closed = -EULER - math.pi / 2 - 3 * math.log(2) - math.log(math.pi)
    check("m_plus(0) closed form", m0 - closed, 1e-12, value=m0, closed=closed)
    check("m_plus asymptotic at tau=1000", float(m_plus(1000.0)) - math.log(1000 / (2 * math.pi)), 1e-6)

    # 2. Theorem 5.4
    tau = np.arange(-400.0, 400.0, 0.02)
    fh, gh = fourier(f_test, tau), fourier(g_test, tau)
    target = np.trapezoid(m_plus(tau) * np.conj(fh) * gh, tau) / (2 * math.pi)
    arch = []
    for N in (256, 1024):
        r = control_archimedean(target, N)
        arch.append(r)
        check(f"Theorem 5.4 packet limit at N={N}", r["absolute_error"], 1e-10)

    # 3. Theorem 4.2 with a non-Haar marginal
    marg = Marginal()
    N = 4096
    n = np.arange(max(1, int(N * math.exp(-1)) - 2), int(N * math.exp(1)) + 3)
    r0 = marg.rho(0.0)
    cf = f_test(np.log(n / N)) / np.sqrt(n) / math.sqrt(r0)
    cg = g_test(np.log(n / N)) / np.sqrt(n) / math.sqrt(r0)
    packets = {"rho_0": r0, "rho_2(0)/rho(0)": marg.rho_a0(2) / r0, "rho_3(0)/rho(0)": marg.rho_a0(3) / r0}
    for a in (2, 3, 5):
        val = marg.pair(cf, n, cg, a * n)
        tgt = inner_shift(f_test, g_test, math.log(a)) / math.sqrt(a)
        check(f"prime mixed limit a={a}", abs(val - tgt), 1e-8, value=[val.real, val.imag], target=[tgt.real, tgt.imag])
    for a in (2, 3):
        val = marg.pair(cf, a * n, cf, a * n).real
        tgt = marg.rho_a0(a) / r0 * inner_shift(f_test, f_test, 0.0).real
        check(f"wound norm a={a}", abs(val - tgt), 1e-8, value=val, target=tgt, haar_value=tgt * (1 / a) / (marg.rho_a0(a) / r0))
    val = marg.pair(cf, 2 * n, cg, 4 * n)
    tgt = 2 * marg.rho_a0(2) / (math.sqrt(8) * r0) * inner_shift(f_test, g_test, math.log(2))
    check("gcd formula (2,4)", abs(val - tgt), 1e-8, value=[val.real, val.imag], target=[tgt.real, tgt.imag])
    val = marg.pair(cf, 2 * n, cg, 3 * n)
    tgt = inner_shift(f_test, g_test, math.log(1.5)) / math.sqrt(6)
    check("gcd formula (2,3)", abs(val - tgt), 1e-8, value=[val.real, val.imag], target=[tgt.real, tgt.imag])

    # 4. C_*(t): definition versus zeros
    if args.regenerate_zeros or not ZERO_FILE.exists():
        import mpmath as mp
        mp.mp.dps = 20
        zeros = [float(mp.zetazero(k).imag) for k in range(1, 701)]
        ZERO_FILE.parent.mkdir(exist_ok=True)
        json.dump({"source": "mpmath.zetazero(k), k = 1..700, dps = 20", "ordinates": zeros}, open(ZERO_FILE, "w"))
    zeros = np.array(json.load(open(ZERO_FILE))["ordinates"])
    tgrid = np.arange(0.0, 2000.0, 0.005)
    W = np.abs(fhat_probe(tgrid)) ** 2
    Mp = m_plus(tgrid)
    wz = 2.0 * np.abs(fhat_probe(zeros)) ** 2

    def k_corr(s):
        return np.trapezoid(W * np.cos(tgrid * s), tgrid) / math.pi

    def c_arch(t):
        return np.trapezoid(W * Mp * np.cos(tgrid * t), tgrid) / math.pi

    tvals = [0.0, 0.3, 0.7, 1.0, 1.5, 2.0, 2.5, 3.0, 4.0, 5.0, 6.0, 7.0] + ([10.0] if args.extended else [])
    labels, lam = von_mangoldt(int(math.exp(max(tvals) + 2.0)) + 2)
    probe_rows = []
    for t in tvals:
        arch_part = c_arch(t)
        prime_part = 0.0
        for a, la in zip(labels, lam):
            loga = math.log(a)
            for s in (t + loga, t - loga):
                if abs(s) < 2.0:
                    prime_part += la / math.sqrt(a) * k_corr(s)
        direct = arch_part - prime_part
        via_zeros = float(np.sum(wz * np.cos(zeros * t)))
        probe_rows.append({"t": t, "definition": direct, "zeros": via_zeros, "archimedean": arch_part, "prime": prime_part})
        check(f"C_*({t}) definition vs zeros", direct - via_zeros, 1e-9, definition=direct, zeros=via_zeros)

    # 5. archimedean tail
    tail_rows = []
    for t in (2.5, 3.0, 4.0, 6.0):
        s = 0.0
        for j in range(1, 40):
            e = 2 * j + 0.5
            s -= math.exp(-e * t) * (F_detect(e) * F_detect(-e)).real
        tail_rows.append({"t": t, "integral": c_arch(t), "closed": s})
        check(f"archimedean tail closed form t={t}", c_arch(t) - s, 1e-12)

    # 6. almost periodicity
    tt = np.linspace(0.0, 200.0, 4001)
    Ct = np.array([float(np.sum(wz * np.cos(zeros * t))) for t in tt])
    mean_square = float(np.mean(Ct ** 2))
    predicted = float(np.sum(wz ** 2 / 2.0))
    check("mean square of C_* on [0,200] vs sum 2|w|^2", (mean_square - predicted) / predicted, 1e-2,
          mean_square=mean_square, predicted=predicted, max_abs=float(np.abs(Ct).max()))
    q_probe = probe_rows[0]["definition"]
    check("Q[f_*] > 0", 0.0 if q_probe > 0 else 1.0, 0.5, value=q_probe)

    result = {
        "status": "floating diagnostics only; not proof of RH, any limiting theorem, positivity, or source occurrence",
        "prepared_for": "Edward Baker",
        "assistant": "Claude (Anthropic); model line claude-fable-5-1 (Fable 5.1), session configured as claude-opus-5-5; serving model may differ; reasoning effort not exposed",
        "python": platform.python_version(),
        "numpy": np.__version__,
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "zeros": {"count": int(len(zeros)), "last_ordinate": float(zeros[-1]),
                  "tail_weight_at_last_ordinate": float(np.abs(fhat_probe(zeros[-1])) ** 2),
                  "first_weights": [float(w) for w in wz[:5]]},
        "probe": {"B_one": B_ONE, "F_half": [float(abs(F_detect(0.5))), float(abs(F_detect(-0.5)))],
                  "min_abs_fhat_on_grid": float(np.sqrt(W).min()), "l2_norm_squared": float(np.trapezoid(W, tgrid) / math.pi)},
        "archimedean_target": [target.real, target.imag],
        "archimedean_convergence": arch,
        "marginal": packets,
        "probe_response": probe_rows,
        "archimedean_tail": tail_rows,
        "checks": checks,
        "check_count": len(checks),
        "all_passed": all(c["passed"] for c in checks),
        "failed": [c["name"] for c in checks if not c["passed"]],
    }
    text = json.dumps(result, indent=2)
    print(text)
    if args.output:
        args.output.write_text(text)


if __name__ == "__main__":
    main()
