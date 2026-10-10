#!/usr/bin/env python3
"""Floating controls for the character-channel note (26 September 2026).

Prepared for Edward Baker by Claude (Anthropic). Model line: claude-fable-5-1
(Fable 5.1) per the runtime environment, session configured as claude-opus-5-5;
the serving model may differ. Reasoning effort not exposed.

Floating diagnostics only.  Nothing here proves GRH, a limiting theorem, or
positivity.  NumPy is required; Part C also needs mpmath (Dirichlet L-functions
and their zeros).

Setting (from the YM manuscript, papers/susy-positivity/investigations/wilson-loewner/YM):
class sector with basis chi_n, Gram <chi_n, chi_m> = t_{n-m} - t_{n+m} where t_k are the
Fourier coefficients of the plaquette marginal rho; winding V_a chi_n = chi_{an}; Mellin
packets sum_n n^{-1/2} f(log(n/N)) chi_n.  The note defines, for a primitive Dirichlet
character chi mod q, the multiplicative packet

    M^chi_R f = sqrt(q / (phi(q) rhobar_q)) sum_n n^{-1/2} chi(n) f(log(n/N)) chi_n,
    rhobar_q  = (1/phi(q)) sum_{j in (Z/q)^*} rho(2 pi j / q),

and proves the limits (N = e^R -> infinity)

    <M^chi f, M^chi' g>      ->  c_{chi chi'} G_{chi chi'} <f, g>,
    <M^chi f, V_a M^chi' g>  ->  a^{-1/2} conj(chi'(a)) c_{chi chi'} G_{chi chi'} <f, U_{log a} g>,
    G_{chi chi'} = (1/q) sum_j chi(j) conj(chi'(j)) rho(2 pi j/q),  c = tau(chibar)/tau(chibar') * normalizations,

so that for chi = chi' the state enters only through rhobar_q, and for chi != chi' the
sectors mix unless rho is constant on the primitive q-th roots of unity (Galois symmetry).

Part A  checks these limits in the class sector for q = 5 (real character and a complex
        character of order 4) with the Haar marginal and with a five-harmonic marginal.
Part B  checks that the manuscript's compensated archimedean insertion
        C = log D + B^* M_{log(theta/2pi)} B (Haar picture) applied to a character packet
        diverges as R ||.||^2 with finite part
            <f, x f>/||f||^2 + (1/phi(q)) sum_j log(min(j, q-j)/q),
        i.e. it does not produce the archimedean factor of L(s, chi).
Part C  verifies the normalization of the family Weil form Q_chi (explicit formula for
        L(s, chi)) on the detecting probe f_* of the manuscript's Section 10 against the
        zeros of L(s, chi) for the six real primitive characters of conductor 3, 4, 5, 7, 8
        (two of conductor 8): C_chi(t) = Q_chi(f_*, U_t f_*) from the definition versus
        sum_gamma 2 |fhat_*(gamma)|^2 cos(gamma t) over zeros up to height T.
        Zeros are located as sign changes of the real completed function
        Lambda(1/2 + it, chi) = (q/pi)^{s/2} Gamma((s+kappa)/2) L(s, chi) and refined with
        the secant method; they are cached in records/dirichlet-zeros-T320.json.
"""
import argparse
import hashlib
import json
import math
import platform
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
ZERO_CACHE = HERE / "records" / "dirichlet-zeros-T320.json"
EULER = 0.57721566490153286060


# ------------------------------------------------------------------ digamma, probe
def digamma_complex(z):
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
    series = inv2 * (1/12 - inv2 * (1/120 - inv2 * (1/252 - inv2 * (1/240 - inv2 * (1/132 - inv2 * (691/32760 - inv2/12))))))
    return np.log(z) - 0.5 * inv - series - shift


def m_chi(tau, q, kappa):
    """archimedean multiplier of L(s, chi): Re psi(1/4 + kappa/2 + i tau/2) + log(q/pi)."""
    return digamma_complex(0.25 + 0.5 * kappa + 0.5j * np.asarray(tau, dtype=float)).real + math.log(q / math.pi)


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


def fhat_probe(tau):
    z = -1j * np.asarray(tau, dtype=float)
    return (0.25 - z * z) * B_transform(1.0 + z) / B_ONE


def envelope_weight(gamma):
    """rigorous upper bound for |fhat_*(gamma)|^2 on the critical line (see the YM control)."""
    gamma = abs(float(gamma))
    out = 1.0
    for a in AJ:
        c = math.sinh(a) / a
        b = math.cosh(a) / (a * gamma) if gamma > 0 else float("inf")
        out *= min(c, b)
    return (0.25 + gamma ** 2) ** 2 * out ** 2 / B_ONE ** 2


# ------------------------------------------------------------------ characters
def characters(q):
    """primitive characters mod q used here, as (name, values on 0..q-1, parity kappa)."""
    if q == 3:
        return [("chi_-3", [0, 1, -1], 1)]
    if q == 4:
        return [("chi_-4", [0, 1, 0, -1], 1)]
    if q == 5:
        return [("chi_5", [0, 1, -1, -1, 1], 0), ("chi_5^(i)", [0, 1, 1j, -1j, -1], 1)]   # order 4, chi(2)=i, odd
    if q == 7:
        w = np.exp(2j * np.pi / 3)
        return [("chi_-7", [0, 1, 1, -1, 1, -1, -1], 1),
                ("chi_7^(w)", [0, 1, w**2, w, w, w**2, 1], 0),      # cubic character, chi(3) = w, even
                ("chi_7^(w^2)", [0, 1, w, w**2, w**2, w, 1], 0)]   # its conjugate, even
    if q == 8:
        return [("chi_8", [0, 1, 0, -1, 0, -1, 0, 1], 0), ("chi_-8", [0, 1, 0, 1, 0, -1, 0, -1], 1)]
    raise ValueError(q)


def chi_of(values, n):
    return np.asarray(values, dtype=complex)[np.asarray(n) % len(values)]


def gauss_sum(values):
    q = len(values)
    return sum(complex(values[r]) * np.exp(2j * math.pi * r / q) for r in range(q))


def phi_euler(q):
    return 1 if q == 1 else sum(1 for j in range(1, q) if math.gcd(j, q) == 1)


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


# ------------------------------------------------------------------ tests, marginals
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


def inner_shift(f1, f2, s):
    return np.trapezoid(np.conj(f1(XG)) * f2(XG - s), XG)


class Marginal:
    """rho(theta) = sum_k t_k e^{ik theta}; Haar is t_k = delta_{k0}."""

    def __init__(self, half=None):
        if half is None:
            half = {0: 1.0}
        c = 1.0 / (half.get(0, 0.0) - half.get(2, 0.0))
        self.t = {}
        for k, v in half.items():
            self.t[k] = c * v
            self.t[-k] = c * v
        self.K = max(abs(k) for k in self.t)

    def tk(self, k):
        return self.t.get(int(k), 0.0)

    def rho(self, theta):
        return sum(self.tk(k) * math.cos(k * theta) for k in range(-self.K, self.K + 1))

    def rhobar(self, q):
        if q == 1:
            return self.rho(0.0)
        units = [j for j in range(1, q) if math.gcd(j, q) == 1]
        return sum(self.rho(2 * math.pi * j / q) for j in units) / len(units)

    def G(self, chi, chip, q):
        return sum(complex(chi[j]) * np.conj(complex(chip[j])) * self.rho(2 * math.pi * j / q)
                   for j in range(1, q) if math.gcd(j, q) == 1) / q

    def pair(self, cn, n_idx, dm, m_idx):
        pos = {int(m): i for i, m in enumerate(m_idx)}
        tot = 0.0 + 0.0j
        for i, nn in enumerate(n_idx):
            for k in range(-self.K, self.K + 1):
                if nn - k in pos:
                    tot += np.conj(cn[i]) * dm[pos[nn - k]] * self.tk(k)
                if k - nn in pos:
                    tot -= np.conj(cn[i]) * dm[pos[k - nn]] * self.tk(k)
        return tot


def packet(fun, N, chi_values, marg, q):
    """multiplicative packet coefficients on labels n in [N/e, N e]."""
    n = np.arange(max(1, int(N * math.exp(-1)) - 2), int(N * math.exp(1)) + 3)
    norm = math.sqrt(q / (phi_euler(q) * marg.rhobar(q)))
    return n, norm * fun(np.log(n / N)) / np.sqrt(n) * chi_of(chi_values, n)


# ------------------------------------------------------------------ Part A
def part_A(check):
    out = []
    cases = [(5, 0, 1), (7, 1, 2)]     # (q, index of chi, index of chi') : opposite parity mod 5, same parity mod 7
    for mname, marg, tol in (("Haar", Marginal(), {1024: 1e-10, 4096: 1e-12}),
                             ("five-harmonic", Marginal({0: 1.0, 1: 0.15, 2: 0.125, 3: 0.05, 5: -0.025}), {1024: 4e-5, 4096: 1e-5})):
        for q, i1, i2 in cases:
            chars = characters(q)
            rb = marg.rhobar(q)
            for N in (1024, 4096):
                packs = {}
                for idx in (i1, i2):
                    nm, vals, _ = chars[idx]
                    n, cf = packet(f_test, N, vals, marg, q)
                    _, cg = packet(g_test, N, vals, marg, q)
                    packs[idx] = (nm, vals, cf, cg)
                for ia, ib in ((i1, i1), (i2, i2), (i1, i2)):
                    na, ca, cf, _ = packs[ia]
                    nb, cb, _, cg = packs[ib]
                    pref = (gauss_sum(np.conj(ca)) / gauss_sum(np.conj(cb))) * marg.G(ca, cb, q) * (q / (phi_euler(q) * rb))
                    val = marg.pair(cf, n, cg, n)
                    tgt = pref * inner_shift(f_test, g_test, 0.0)
                    check(f"A {mname} q={q} N={N} <{na},{nb}> norm limit", abs(val - tgt), tol[N],
                          value=[val.real, val.imag], target=[tgt.real, tgt.imag], G=[marg.G(ca, cb, q).real, marg.G(ca, cb, q).imag])
                    for a in (2, 3, 4, 5, 6, 7):
                        val = marg.pair(cf, n, cg, a * n)
                        tgt = a ** -0.5 * np.conj(complex(cb[a % q])) * pref * inner_shift(f_test, g_test, math.log(a))
                        check(f"A {mname} q={q} N={N} <{na}, V_{a} {nb}>", abs(val - tgt), tol[N],
                              value=[val.real, val.imag], target=[tgt.real, tgt.imag])
                out.append({"marginal": mname, "q": q, "N": N, "rhobar_q": rb,
                            "G": {f"{chars[a][0]},{chars[b][0]}": [marg.G(chars[a][1], chars[b][1], q).real, marg.G(chars[a][1], chars[b][1], q).imag]
                                  for a in (i1, i2) for b in (i1, i2)}})
    return out


# ------------------------------------------------------------------ Part B
def gl_nodes(npanels, upper):
    x, w = np.polynomial.legendre.leggauss(16)
    edges = np.linspace(0.0, upper, npanels + 1)
    u = np.concatenate([0.5 * (b - a) * x + 0.5 * (b + a) for a, b in zip(edges[:-1], edges[1:])])
    wt = np.concatenate([0.5 * (b - a) * w for a, b in zip(edges[:-1], edges[1:])])
    return u, wt


def log_angle_moments(kmax):
    """J_k = int_0^pi log(theta/2pi) cos(k theta) dtheta = -Si(k pi)/k (k >= 1), J_0 = pi (log(1/2) - 1)."""
    from scipy.special import sici
    k = np.arange(1, kmax + 1)
    J = np.empty(kmax + 1)
    J[0] = math.pi * (math.log(0.5) - 1.0)
    J[1:] = -sici(k * math.pi)[0] / k
    return J


def angle_term(c, n):
    """int_0^pi log(theta/2pi) |sqrt(2/pi) sum_n c_n cos(n theta)|^2 dtheta, exactly, via J_k."""
    J = log_angle_moments(int(2 * n[-1]) + 2)
    tot = 0.0
    for i0 in range(0, len(n), 2048):
        rows = n[i0:i0 + 2048]
        K = J[np.abs(rows[:, None] - n[None, :])] + J[rows[:, None] + n[None, :]]
        tot += float(np.real(np.conj(c[i0:i0 + 2048]) @ (K @ c)))
    return tot / math.pi


def part_B(check):
    """The class-sector insertion C = log D + B^* M_{log q} B on character packets (Haar picture)."""
    out = []
    marg = Marginal()
    for q in (3, 5):
        name, values, kappa = characters(q)[0]
        units = [j for j in range(1, q) if math.gcd(j, q) == 1]
        predicted_const = sum(math.log(min(j, q - j) / q) for j in units) / len(units)
        xf = inner_shift(f_test, lambda x: np.asarray(x) * f_test(x), 0.0).real / inner_shift(f_test, f_test, 0.0).real
        rows = []
        for N in (256, 1024, 4096):
            R = math.log(N)
            n, c = packet(f_test, N, values, marg, q)
            norm2 = float(np.sum(np.abs(c) ** 2))
            electric = float(np.sum(np.abs(c) ** 2 * np.log(n)))
            angle = angle_term(c, n)
            finite = (electric + angle) / norm2 - R
            rows.append({"N": N, "finite_part": finite, "norm2": norm2, "electric_over_norm": electric / norm2, "angle_over_norm": angle / norm2})
        predicted = xf + predicted_const
        err = abs(rows[-1]["finite_part"] - predicted)
        check(f"B {name}: (<M,CM>/||M||^2 - R) -> <f,xf>/||f||^2 + (1/phi) sum log(min(j,q-j)/q)", err, 1e-6,
              finite_parts=[r["finite_part"] for r in rows], predicted=predicted, x_moment=xf, conductor_constant=predicted_const)
        out.append({"q": q, "character": name, "rows": rows, "predicted": predicted, "x_moment": xf, "constant": predicted_const,
                    "minus_log_q": -math.log(q)})
    # control: the identity packet (q = 1) with the same code must give the finite archimedean limit of Theorem 5.2
    n, c = packet(f_test, 1024, [1], marg, 1)
    val = (float(np.sum(np.abs(c) ** 2 * np.log(n))) + angle_term(c, n))
    tau = np.arange(-400.0, 400.0, 0.02)
    fh = np.array([np.trapezoid(f_test(XG) * np.exp(-1j * t * XG), XG) for t in tau])
    target = float(np.trapezoid(m_chi(tau, 1, 0) * np.abs(fh) ** 2, tau) / (2 * math.pi))
    check("B control: identity packet, exact J_k angle term reproduces Theorem 5.2 at N=1024", val - target, 1e-9, value=val, target=target)
    return out


# ------------------------------------------------------------------ Part C
def dirichlet_zeros(T, refresh=False):
    if ZERO_CACHE.exists() and not refresh:
        return json.load(open(ZERO_CACHE))
    import mpmath as mp
    mp.mp.dps = 15
    result = {"T": T, "method": "sign changes of Lambda(1/2+it,chi) on a grid of step 0.04, refined by mp.findroot (secant)", "zeros": {}}
    for q in (3, 4, 5, 7, 8):
        for name, values, kappa in characters(q):
            if any(isinstance(v, complex) for v in values):
                continue
            chi = [int(v) for v in values]

            def Lam(t):
                s = mp.mpf('0.5') + 1j * t
                return ((q / mp.pi) ** (s / 2) * mp.gamma((s + kappa) / 2) * mp.dirichlet(s, chi)).real
            grid = np.arange(0.02, T, 0.04)
            vals = [Lam(mp.mpf(t)) for t in grid]
            zs = []
            for i in range(len(grid) - 1):
                if vals[i] * vals[i + 1] < 0:
                    z = mp.findroot(Lam, (mp.mpf(grid[i]), mp.mpf(grid[i + 1])), solver="secant", tol=1e-24)
                    zs.append(float(z))
            expected = T / (2 * math.pi) * math.log(q * T / (2 * math.pi * math.e))
            result["zeros"][name] = {"q": q, "kappa": kappa, "count": len(zs), "count_main_term": expected, "ordinates": zs}
            print(f"  zeros of L(s,{name}) up to {T}: {len(zs)} (main term {expected:.1f})", flush=True)
    ZERO_CACHE.parent.mkdir(exist_ok=True)
    json.dump(result, open(ZERO_CACHE, "w"))
    return result


def part_C(check, refresh):
    zeros = dirichlet_zeros(320.0, refresh)
    tgrid = np.arange(0.0, 1500.0, 0.005)
    W = np.abs(fhat_probe(tgrid)) ** 2
    labels, lam = von_mangoldt(int(math.exp(5.0 + 2.0)) + 2)
    out = []
    for name, rec in zeros["zeros"].items():
        q, kappa = rec["q"], rec["kappa"]
        values = [v for nm, v, k in characters(q) if nm == name][0]
        gam = np.array(rec["ordinates"])
        wz = 2.0 * np.abs(fhat_probe(gam)) ** 2
        Mp = m_chi(tgrid, q, kappa)
        # tail estimate beyond T (floating): envelope times a generous zero density
        T = zeros["T"]
        dens = math.log(q * (T + 1) / (2 * math.pi)) / (2 * math.pi) + 3.0
        tail = sum(2 * dens * envelope_weight(T + k) for k in range(0, 400))
        rows = []
        for t in (0.0, 0.5, 1.0, 2.0, 3.0, 5.0):
            arch = np.trapezoid(W * Mp * np.cos(tgrid * t), tgrid) / math.pi
            prime = 0.0
            for n, la in zip(labels, lam):
                cn = float(np.real(chi_of(values, n)))
                if cn == 0.0:
                    continue
                ln = math.log(n)
                for s in (t + ln, t - ln):
                    if abs(s) < 2.0:
                        prime += la * cn / math.sqrt(n) * np.trapezoid(W * np.cos(tgrid * s), tgrid) / math.pi
            direct = arch - prime
            via = float(np.sum(wz * np.cos(gam * t)))
            rows.append({"t": t, "definition": direct, "zeros": via, "archimedean": arch, "prime": prime})
            check(f"C L(s,{name}) q={q} kappa={kappa}: C_chi({t}) definition vs zeros", direct - via, 1e-8, definition=direct, zeros=via)
        out.append({"character": name, "q": q, "kappa": kappa, "zero_count": rec["count"], "first_zeros": rec["ordinates"][:4],
                    "tail_estimate_floating": tail, "rows": rows})
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--part", default="all", choices=["A", "B", "C", "all"])
    ap.add_argument("--output", type=Path)
    ap.add_argument("--refresh-zeros", action="store_true")
    args = ap.parse_args()
    checks = []

    def check(name, error, tol, **extra):
        rec = {"name": name, "error": float(abs(error)), "tolerance": float(tol), "passed": bool(abs(error) <= tol)}
        rec.update({k: (v if not isinstance(v, np.floating) else float(v)) for k, v in extra.items()})
        checks.append(rec)

    result = {
        "status": "floating diagnostics only; not proof of GRH, any limiting theorem, or positivity",
        "prepared_for": "Edward Baker",
        "assistant": "Claude (Anthropic); model line claude-fable-5-1 (Fable 5.1), session configured as claude-opus-5-5; serving model may differ",
        "python": platform.python_version(), "numpy": np.__version__,
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    if args.part in ("A", "all"):
        result["part_A"] = part_A(check)
    if args.part in ("B", "all"):
        result["part_B"] = part_B(check)
    if args.part in ("C", "all"):
        result["part_C"] = part_C(check, args.refresh_zeros)
        result["zero_cache_sha256"] = hashlib.sha256(ZERO_CACHE.read_bytes()).hexdigest()
    result["checks"] = checks
    result["check_count"] = len(checks)
    result["all_passed"] = all(c["passed"] for c in checks)
    result["failed"] = [c["name"] for c in checks if not c["passed"]]
    text = json.dumps(result, indent=2, default=float)
    print(text)
    if args.output:
        args.output.write_text(text)


if __name__ == "__main__":
    main()
