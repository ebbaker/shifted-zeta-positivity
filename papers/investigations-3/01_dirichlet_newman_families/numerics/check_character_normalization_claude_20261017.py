#!/usr/bin/env python3
"""Normalization checks for the primitive Dirichlet family under the heat flow
(papers/investigations-3/01_dirichlet_newman_families,
notes/01_NORMALIZATION_AND_TRANSFER_CONTRACT_CLAUDE_20261017.md, Section 1).

17 October 2026. Prepared for Edward Baker with LLM assistance. Model:
Claude Opus 5.5 (configured identifier claude-opus-5-5), Claude Cowork,
reasoning effort max. Standard library only; deterministic; prints one JSON
record to stdout. Floats are rounded to 12 significant figures (13 for zero
locations) so that the record is stable across platforms.

What is checked, for a fixed list of primitive characters chi mod q of both
parities, real and complex:

  A. Gauss sums and root numbers: eps(chi) = tau(chi)/(i^a sqrt q) has modulus
     one, eps = 1 for real chi, eps(conj chi) = conj eps(chi); comparison with
     the LMFDB signs quoted in the note (three digits).
  B. The kernel in Dobner's normalization,
        Phi_chi(u) = 4 alpha (pi/q)^(a/2) e^((1+2a)u) sum_n chi(n) n^a exp(-pi n^2 e^(4u)/q),
     alpha = eps^(-1/2): the Hermitian symmetry Phi(-u) = conj Phi(u), checked
     by evaluating the series directly at negative u.
  C. The transform H_chi(z) = int Phi_chi(u) e^(izu) du (trapezoid on the full
     line, using B for u < 0) against an independent evaluation of
        xi_chi(s) = alpha (q/pi)^(s/2) Gamma((s+a)/2) L(s,chi),  s = (1+iz)/2,
     with L(s,chi) = q^(-s) sum_a chi(a) zeta(s, a/q) (Hurwitz zeta by
     Euler-Maclaurin) and the complex Gamma function by Stirling's series.
     Real and complex z, |Re z| <= 40.
  D. Reality of H_chi on the real axis, the Hermitian functional equation
     xi(s) = conj xi(1 - conj s), and, for independently constructed conjugate
     pairs (separate tables, Gauss sums and kernels), eps(conj chi) = conj eps(chi)
     and H_{t,conj chi}(z) = c conj H_{t,chi}(-conj z), c = +-1 the branch of
     eps^(-1/2), at t = 0 and t = 0.2, with mirror-image real zeros.
  E. Real zeros of H_chi on [-50, 50] by sign changes and bisection, reported
     as gamma = x/2, against the LMFDB zeros quoted in the note (characters
     3.2, 5.2, 5.4, 7.2 in Conrey's labelling).
  F. The backward heat equation d_t H = -d_z^2 H by central differences at one
     complex point, and the displacement of the low zeros between t = 0 and
     t = 0.2 (a diagnostic of the real drift term for complex characters).

Nothing here is a certificate: floating point throughout, with quadrature and
series errors far below the reported discrepancies only by the estimates in
the docstrings. The real-zero locations are heights where GRH is long verified;
they test the normalization, not any statement about zeros.
"""
import cmath
import json
import math
from fractions import Fraction

PI = math.pi
I = 1j


def sig(x, n=12):
    if x == 0 or not math.isfinite(x):
        return x
    return float(f"{x:.{n - 1}e}")


def csig(z, n=12):
    return [sig(z.real, n), sig(z.imag, n)]


# ---------------------------------------------------------------------------
# Bernoulli numbers (exact), Stirling series, digamma, Hurwitz zeta
# ---------------------------------------------------------------------------

def bernoulli_even(kmax):
    """B_0..B_{2kmax} as Fractions via the standard recurrence."""
    m = 2 * kmax
    B = [Fraction(0)] * (m + 1)
    B[0] = Fraction(1)
    for n in range(1, m + 1):
        s = Fraction(0)
        binom = 1
        for k in range(n):
            # binom = C(n+1, k)
            s += binom * B[k]
            binom = binom * (n + 1 - k) // (k + 1)
        B[n] = -s / (n + 1)
    return B


BERN = bernoulli_even(30)


def cgamma(z):
    """Complex Gamma via Stirling's series after shifting Re z to >= 20."""
    shift = 0
    prod = 1.0 + 0j
    w = complex(z)
    while w.real < 20.0:
        prod *= w
        w += 1.0
        shift += 1
    logg = (w - 0.5) * cmath.log(w) - w + 0.5 * math.log(2 * PI)
    wpow = w
    w2 = w * w
    for k in range(1, 12):
        logg += float(BERN[2 * k]) / (2 * k * (2 * k - 1)) / wpow
        wpow *= w2
    return cmath.exp(logg) / prod


def digamma(z):
    """Complex digamma via the asymptotic series after shifting."""
    acc = 0j
    w = complex(z)
    while w.real < 20.0:
        acc -= 1.0 / w
        w += 1.0
    res = cmath.log(w) - 0.5 / w
    wpow = w * w
    w2 = w * w
    for k in range(1, 12):
        res -= float(BERN[2 * k]) / (2 * k) / wpow
        wpow *= w2
    return res + acc


def hurwitz_zeta(s, a, N=40, M=24):
    """zeta(s, a), 0 < a <= 1, s != 1, by Euler-Maclaurin with N terms and M
    Bernoulli corrections; the correction ratio is about |s|/(2 pi (N+a)),
    below 0.15 for |s| <= 35, so the truncation is far below 1e-15."""
    total = 0j
    for k in range(N):
        total += cmath.exp(-s * math.log(k + a))
    Na = N + a
    lNa = math.log(Na)
    total += cmath.exp((1 - s) * lNa) / (s - 1)
    total += 0.5 * cmath.exp(-s * lNa)
    rising = s  # (s)_{1}
    fact = 2.0  # (2j)! for j=1
    for j in range(1, M + 1):
        term = float(BERN[2 * j]) / fact * rising * cmath.exp((-s - 2 * j + 1) * lNa)
        total += term
        # update rising factorial (s)_{2j-1} -> (s)_{2j+1}
        rising *= (s + 2 * j - 1) * (s + 2 * j)
        fact *= (2 * j + 1) * (2 * j + 2)
    return total


# ---------------------------------------------------------------------------
# Characters
# ---------------------------------------------------------------------------

def prim_root(q):
    for g in range(2, q):
        seen = set()
        x = 1
        for _ in range(q - 1):
            x = x * g % q
            seen.add(x)
        if len(seen) == q - 1:
            return g
    raise ValueError(q)


def char_prime(q, j):
    """chi(g^k) = e(j k/(q-1)) for the smallest primitive root g (Conrey's
    character q.(g^j mod q))."""
    g = prim_root(q)
    vals = [0j] * q
    x = 1
    for k in range(q - 1):
        vals[x] = cmath.exp(2j * PI * j * k / (q - 1))
        x = x * g % q
    # clean exact values
    for a in range(q):
        z = vals[a]
        vals[a] = complex(round(z.real, 15), round(z.imag, 15))
    label = f"{q}.{pow(g, j, q)}"
    return vals, label


def char_table(q, table):
    vals = [0j] * q
    for a, v in table.items():
        vals[a % q] = complex(v)
    return vals


def parity(vals, q):
    v = vals[(q - 1) % q]
    return 0 if abs(v - 1) < 1e-12 else 1


def is_real(vals):
    return all(abs(v.imag) < 1e-12 for v in vals)


def conj_vals(vals):
    return [v.conjugate() for v in vals]


def gauss_sum(vals, q):
    return sum(vals[a] * cmath.exp(2j * PI * a / q) for a in range(1, q))


# ---------------------------------------------------------------------------
# Kernel, transform and independent xi
# ---------------------------------------------------------------------------

class Family:
    def __init__(self, vals, q, alpha=None, h=0.01, umax=2.6):
        self.vals = vals
        self.q = q
        self.a = parity(vals, q)
        tau = gauss_sum(vals, q)
        self.tau = tau
        self.eps = tau / ((I ** self.a) * math.sqrt(q))
        self.alpha = alpha if alpha is not None else 1.0 / cmath.sqrt(self.eps)
        self.h = h
        self.K = int(round(umax / h))
        self.phi_pos = [self.phi_direct(k * h) for k in range(self.K + 1)]

    def phi_direct(self, u):
        q, a = self.q, self.a
        x = math.exp(4 * u)
        nmax = int(math.sqrt(60.0 * q / (PI * x))) + 2
        s = 0j
        for n in range(1, nmax + 1):
            c = self.vals[n % q]
            if c == 0:
                continue
            s += c * (n ** a) * math.exp(-PI * n * n * x / q)
        return 4 * self.alpha * (PI / q) ** (a / 2) * math.exp((1 + 2 * a) * u) * s

    def H(self, z, t=0.0):
        """Full-line trapezoid of e^{t u^2} Phi(u) e^{izu}, Phi(-u) = conj Phi(u)."""
        h = self.h
        tot = self.phi_pos[0]
        for k in range(1, self.K + 1):
            u = k * h
            w = math.exp(t * u * u)
            ph = self.phi_pos[k]
            tot += w * (ph * cmath.exp(1j * z * u) + ph.conjugate() * cmath.exp(-1j * z * u))
        return h * tot

    def xi(self, s):
        q, a = self.q, self.a
        L = cmath.exp(-s * math.log(q)) * sum(
            self.vals[b % q] * hurwitz_zeta(s, b / q) for b in range(1, q + 1) if self.vals[b % q] != 0)
        return self.alpha * cmath.exp(0.5 * s * math.log(q / PI)) * cgamma(0.5 * (s + a)) * L


def real_zeros(fam, xmin, xmax, step=0.05, t=0.0):
    xs = []
    n = int(round((xmax - xmin) / step))
    prev_x = xmin
    prev_v = fam.H(xmin, t).real
    for k in range(1, n + 1):
        x = xmin + k * step
        v = fam.H(x, t).real
        if prev_v == 0:
            xs.append(prev_x)
        elif prev_v * v < 0:
            lo, hi, flo = prev_x, x, prev_v
            for _ in range(48):
                mid = 0.5 * (lo + hi)
                fm = fam.H(mid, t).real
                if flo * fm <= 0:
                    hi = mid
                else:
                    lo, flo = mid, fm
            xs.append(0.5 * (lo + hi))
        prev_x, prev_v = x, v
    return xs


# ---------------------------------------------------------------------------
# Test characters
# ---------------------------------------------------------------------------

def characters():
    out = []
    # q = 3, 5, 7, 11, 13 from the primitive-root construction (all primitive)
    for q, js in [(3, [1]), (5, [1, 2, 3]), (7, [1, 2, 3, 4, 5]), (11, [1, 9]), (13, [2, 10])]:
        for j in js:
            vals, label = char_prime(q, j)
            out.append((label, q, vals))
    out.append(("4.3", 4, char_table(4, {1: 1, 3: -1})))
    out.append(("8:(2/n)", 8, char_table(8, {1: 1, 3: -1, 5: -1, 7: 1})))   # even
    out.append(("8:(-2/n)", 8, char_table(8, {1: 1, 3: 1, 5: -1, 7: -1})))  # odd
    return out


# LMFDB values quoted in the note (fetched 17 October 2026); signs to 3 digits.
LMFDB = {
    "3.2": {"zeros": [8.03973715568146668171362321417, 11.24920620777293524970502567886,
                      15.70461917672162556516555088043], "sign": [1.0, 0.0]},
    "5.4": {"zeros": [6.64845334472771471612327845997, 9.831444432886669616348321347458,
                      11.95884562608351453026565868826], "sign": [1.0, 0.0]},
    "5.2": {"zeros": [-4.13290370521285159500191933156, 6.18357819545085391437751730970,
                      8.45722917442323072160535286274, 12.67494641701135578048229914508],
            "sign": [0.850, 0.525]},
    "7.2": {"zeros": [-6.20123004275588129466099054628, 4.35640162473628422727957479051,
                      8.78555471449907536558015746317, 10.73611998749339311587424153504],
            "sign": [0.895, -0.444]},
}


def main():
    rec = {
        "script": "check_character_normalization_claude_20261017.py",
        "model": "Claude Opus 5.5 (claude-opus-5-5), Claude Cowork, effort max",
        "date": "2026-10-17",
        "status": "floating-point diagnostics; no certificate",
        "normalization": {
            "xi": "xi_chi(s) = alpha (q/pi)^(s/2) Gamma((s+a)/2) L(s,chi), alpha = eps^(-1/2), eps = tau/(i^a sqrt q)",
            "kernel": "Phi_chi(u) = 4 alpha (pi/q)^(a/2) e^((1+2a)u) sum_n chi(n) n^a exp(-pi n^2 e^(4u)/q)",
            "transform": "H_{t,chi}(z) = int_R e^(t u^2) Phi_chi(u) e^(izu) du = xi_chi((1+iz)/2) at t = 0",
            "zero_map": "rho = beta + i gamma  <->  z = 2 gamma + i (1 - 2 beta)",
            "quadrature": "full-line trapezoid, h = 0.01, |u| <= 2.6",
        },
        "characters": [],
    }
    worst = {"symmetry": 0.0, "transform_vs_xi": 0.0, "reality": 0.0,
             "hermitian_fe": 0.0, "conjugate_relation": 0.0, "eps_modulus": 0.0}
    fams = {}
    zpts = [0.0, 3.0, 7.5, 12.0, 20.0, 30.0, 40.0, -9.0, -25.0]
    cpts = [5.0 + 0.3j, 11.0 - 0.5j, -17.0 + 0.9j, 26.0 + 0.6j]
    for label, q, vals in characters():
        zs_cache = []
        fam = Family(vals, q)
        fams[label] = (fam, zs_cache)
        entry = {"label": label, "q": q, "parity": fam.a, "real": is_real(vals),
                 "eps": csig(fam.eps), "abs_eps_minus_1": sig(abs(abs(fam.eps) - 1.0))}
        worst["eps_modulus"] = max(worst["eps_modulus"], abs(abs(fam.eps) - 1.0))
        if label in LMFDB:
            sgn = complex(*LMFDB[label]["sign"])
            entry["lmfdb_sign"] = LMFDB[label]["sign"]
            entry["eps_minus_lmfdb_sign"] = sig(abs(fam.eps - sgn))
        # B. symmetry at negative u by direct series
        sym = 0.0
        for u in (0.15, 0.3, 0.45, 0.6):
            d = abs(fam.phi_direct(-u) - fam.phi_direct(u).conjugate())
            sym = max(sym, d / abs(fam.phi_direct(u)))
        entry["phi_symmetry_rel_defect"] = sig(sym)
        worst["symmetry"] = max(worst["symmetry"], sym)
        # C. transform vs independent xi
        dev = 0.0
        samples = []
        for z in zpts + cpts:
            hz = fam.H(z)
            xz = fam.xi(0.5 * (1 + 1j * z))
            r = abs(hz - xz) / max(abs(xz), 1e-300)
            dev = max(dev, r)
            samples.append({"z": csig(complex(z)), "H": csig(hz), "rel_diff": sig(r)})
        entry["transform_vs_xi_max_rel"] = sig(dev)
        entry["transform_samples"] = samples
        worst["transform_vs_xi"] = max(worst["transform_vs_xi"], dev)
        # D. reality on R, Hermitian FE, conjugate relation
        real_def = max(abs(fam.H(x).imag) / max(abs(fam.H(x)), 1e-300) for x in (1.0, 6.5, 13.0, 21.0, -8.0))
        entry["imag_part_rel_on_R"] = sig(real_def)
        worst["reality"] = max(worst["reality"], real_def)
        fe = 0.0
        for s in (0.3 + 4.0j, 0.8 - 7.0j, 0.1 + 12.5j):
            lhs = fam.xi(s)
            rhs = fam.xi(1 - s.conjugate()).conjugate()
            fe = max(fe, abs(lhs - rhs) / abs(lhs))
        entry["hermitian_fe_rel"] = sig(fe)
        worst["hermitian_fe"] = max(worst["hermitian_fe"], fe)
        # E. real zeros
        zs = real_zeros(fam, -50.0, 50.0)
        gammas = [z / 2 for z in zs]
        pos = [g for g in gammas if g > 0][:4]
        neg = sorted([g for g in gammas if g < 0], reverse=True)[:3]
        entry["zeros_gamma_positive"] = [sig(g, 13) for g in pos]
        entry["zeros_gamma_negative"] = [sig(g, 13) for g in neg]
        entry["zero_count_|x|<=50"] = len(zs)
        if label in LMFDB:
            diffs = []
            for g in LMFDB[label]["zeros"]:
                near = min(gammas, key=lambda v: abs(v - g))
                diffs.append(sig(abs(near - g)))
            entry["lmfdb_zero_abs_diffs"] = diffs
        zs_cache.extend(zs)
        rec["characters"].append(entry)
    # D'. Independently constructed conjugate pairs chi_j, chi_{q-1-j} (separate
    # character tables, Gauss sums and kernels): eps(conj chi) = conj eps(chi),
    # H_{t,conj chi}(z) = c conj H_{t,chi}(-conj z) with c = alpha'/conj(alpha) = +-1,
    # and the real zeros of the pair are mirror images.
    pairs = []
    for la, lb in (("5.2", "5.3"), ("7.3", "7.5"), ("7.2", "7.4"), ("11.2", "11.6"), ("13.4", "13.10")):
        fa, za = fams[la]
        fb, zb = fams[lb]
        c = fb.alpha / fa.alpha.conjugate()
        cr = 0.0
        for t in (0.0, 0.2):
            for z in cpts:
                a1 = fb.H(z, t)
                a2 = c * fa.H(-z.conjugate(), t).conjugate()
                cr = max(cr, abs(a1 - a2) / abs(a1))
        mirror = max(abs(x + y) for x, y in zip(sorted(za), sorted(zb, reverse=True)))
        worst["conjugate_relation"] = max(worst["conjugate_relation"], cr)
        pairs.append({"pair": [la, lb], "eps_conj_defect": sig(abs(fb.eps - fa.eps.conjugate())),
                      "branch_sign_c": csig(c), "conjugate_relation_rel_t0_and_t0.2": sig(cr),
                      "zero_counts": [len(za), len(zb)], "mirror_zero_max_abs_defect_x": sig(mirror)})
    rec["conjugate_pairs"] = pairs
    # F. heat equation and drift, for one complex odd and one complex even character
    heat = []
    for label, q, vals in characters():
        if label not in ("5.2", "7.2"):
            continue
        fam = Family(vals, q)
        z0 = 9.0 + 0.4j
        t0 = 0.2
        dt = 1e-3
        dz = 1e-2
        dH_dt = (fam.H(z0, t0 + dt) - fam.H(z0, t0 - dt)) / (2 * dt)
        d2H = (fam.H(z0 + dz, t0) - 2 * fam.H(z0, t0) + fam.H(z0 - dz, t0)) / (dz * dz)
        z_t0 = real_zeros(fam, -20.0, 20.0)
        z_t1 = real_zeros(fam, -20.0, 20.0, t=0.2)
        heat.append({
            "label": label,
            "heat_equation_rel_defect": sig(abs(dH_dt + d2H) / abs(dH_dt)),
            "zeros_x_t0": [sig(v, 10) for v in z_t0],
            "zeros_x_t0.2": [sig(v, 10) for v in z_t1],
            "note": "real zeros of H_{0.2,chi} near the origin; counts and displacements are diagnostics only",
        })
    rec["heat_flow"] = heat
    rec["worst"] = {k: sig(v) for k, v in worst.items()}
    print(json.dumps(rec, indent=1, sort_keys=True))


if __name__ == "__main__":
    main()
