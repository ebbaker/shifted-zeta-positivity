#!/usr/bin/env python3
"""Leading-order benchmark arithmetic for the Dirichlet-family transfer contract
(papers/investigations-3/01_dirichlet_newman_families,
notes/01_NORMALIZATION_AND_TRANSFER_CONTRACT_CLAUDE_20261017.md, Section 4).

17 October 2026. Prepared for Edward Baker with LLM assistance. Model:
Claude Opus 5.5 (configured identifier claude-opus-5-5), Claude Cowork,
reasoning effort max. Standard library only; deterministic; prints one JSON
record to stdout (floats rounded to 12 significant figures; exact constants as
fractions or 40-digit decimals).

Everything below is planning arithmetic.  Sections A, C and D are exact or
elementary; Sections B, E and F rest on a stated scaling hypothesis (the
exterior first-term dominance condition depends on (t, y) through
(t L, y L) at leading order, L the effective log analytic conductor), with all
remainder terms of the effective approximation omitted.  No number here is a
bound on any de Bruijn-Newman constant.

Sections
  A. Platt's GRH verification budget (arXiv:1305.3087): t0(q) for every modulus
     q <= 400000 with primitive characters (q not 2 mod 4), the analytic
     conductor q t0 and the effective log conductor
     L = log(q/pi) + Re psi((1/2 + a + i t0)/2), both parities, against the
     Stirling form log(q t0/(2 pi)).
  B. The two published zeta rows (Polymath t0=y0=0.2, X=6e10+83952-1/2;
     Platt-Trudgian t0=0.186, y0=0.16733, X=5e12+194858), their (tL, yL), and
     their transfer to a family value L' in two variants: both t and y scaled
     by L/L' (dominance-invariant at leading order), or t scaled with y fixed.
     The unmollified leading-order components (A-tail, |gamma| = e^{-yL/2},
     B-part, and the triangle margin D) are printed for each, to show which
     variant preserves the dominance budget; D is negative throughout because
     the published criteria use mollifiers and sharper bounds.
  C. The conditional strip bounds (2B-1)^2/2 for the claimed zero-free
     half-planes B = 11/12, 7/8, 34999/40000 and B_new = (1507-2 sqrt 921)/1653.
  D. The time-zero zero-free abscissa of Polymath's Proposition 3.3(i) for a
     target lambda = t0 + y0^2/2: sigma* = 1/2 + sqrt(y0^2 + 2 t0)/2
     = 1/2 + sqrt(2 lambda)/2, independent of the split.
  E. Large-conductor planning: the L* at which the scaled Polymath row gives
     a target lambda, and the conductor q0(lambda, a) above which the height-zero
     effective log conductor log(q/pi) + psi((1 + y + 2a)/4) reaches L*.
  F. The verification height a per-character certificate would need below
     q0, T*(q) ~ 2 pi e^{L*}/q (Stirling form), against Platt's t0(q).
  G. Family sizes: primitive characters with conductor at most Q, real ones,
     and the number of distinct Lambda values to be certified (conjugate
     characters share Lambda).
  H. The strip comparison of Hakimoglu-Brown (arXiv:2610.12803, the paired-zero
     inequality Q' <= -2 - (4Q/p) S + 8Q/(p^2 - Q), p^2 >= 5Q) with the exact
     time-zero floor of S(x,p,0) = (1/2) Re(xi'/xi)((1+p+ix)/2) for primitive
     chi: S >= (1/4)(log(q/pi) + psi((1+p)/4 + a/2)) - (1/2)(-zeta'/zeta)((1+p)/2)
     at every height.  The comparison time from M(0) = 1 (unconditional) or
     9/16 (claimed 7/8 half-plane) is integrated exactly and minimized over p.
     Holding the time-zero floor over the comparison interval is the planning
     hypothesis.
"""
import json
import math
from decimal import Decimal, getcontext
from fractions import Fraction

PI = math.pi
getcontext().prec = 50


def sig(x, n=12):
    if x == 0 or not math.isfinite(x):
        return x
    return float(f"{x:.{n - 1}e}")


# ---------------------------------------------------------------------------
# digamma (real and complex) by recurrence and the asymptotic series
# ---------------------------------------------------------------------------

def bernoulli(m):
    B = [Fraction(0)] * (m + 1)
    B[0] = Fraction(1)
    for n in range(1, m + 1):
        s = Fraction(0)
        c = 1
        for k in range(n):
            s += c * B[k]
            c = c * (n + 1 - k) // (k + 1)
        B[n] = -s / (n + 1)
    return B


BERN = bernoulli(30)


def digamma(z):
    import cmath
    acc = 0j
    w = complex(z)
    while w.real < 20.0:
        acc -= 1.0 / w
        w += 1.0
    res = cmath.log(w) - 0.5 / w
    wp = w * w
    w2 = w * w
    for k in range(1, 12):
        res -= float(BERN[2 * k]) / (2 * k) / wp
        wp *= w2
    return res + acc


# ---------------------------------------------------------------------------
# A. Platt's budget
# ---------------------------------------------------------------------------

def platt_t0(q):
    if q % 2 == 0:
        return max(1e8 / q, 7.5e7 / q + 200.0)
    return max(1e8 / q, 3.75e7 / q + 200.0)


def L_exact(q, a, height):
    """2 Re alpha_chi at s = 1/2 + i*height: log(q/pi) + Re psi((s+a)/2)."""
    return math.log(q / PI) + digamma(complex(0.25 + 0.5 * a, 0.5 * height)).real


def section_A():
    rows = []
    stats = {}
    for parity_q in ("even_q", "odd_q"):
        stats[parity_q] = {"qt0_min": float("inf"), "qt0_max": 0.0,
                           "L_stirling_min": float("inf"), "L_stirling_max": 0.0}
    for q in range(3, 400001):
        if q % 4 == 2:
            continue
        t0 = platt_t0(q)
        key = "even_q" if q % 2 == 0 else "odd_q"
        st = stats[key]
        qt = q * t0
        Ls = math.log(qt / (2 * PI))
        st["qt0_min"] = min(st["qt0_min"], qt)
        st["qt0_max"] = max(st["qt0_max"], qt)
        st["L_stirling_min"] = min(st["L_stirling_min"], Ls)
        st["L_stirling_max"] = max(st["L_stirling_max"], Ls)
    for q in (3, 4, 5, 100, 1000, 10000, 125000, 125001, 312500, 312501, 399999, 400000):
        if q % 4 == 2:
            continue
        t0 = platt_t0(q)
        rows.append({
            "q": q, "t0": sig(t0), "q_t0": sig(q * t0),
            "L_stirling": sig(math.log(q * t0 / (2 * PI))),
            "L_exact_even_char": sig(L_exact(q, 0, t0)),
            "L_exact_odd_char": sig(L_exact(q, 1, t0)),
        })
    for k in stats:
        stats[k] = {kk: sig(v) for kk, v in stats[k].items()}
    return {"extremes_over_q": stats, "sample_moduli": rows,
            "formula": "t0 = max(1e8/q, 7.5e7/q + 200) for even q; max(1e8/q, 3.75e7/q + 200) for odd q (Platt, abstract)"}


# ---------------------------------------------------------------------------
# B. Zeta rows and their transfer
# ---------------------------------------------------------------------------

ROWS = {
    "Polymath_Lambda<=0.22": (0.2, 0.2, 6e10 + 83952 - 0.5),
    "Platt-Trudgian_Lambda<=0.2": (0.186, 0.16733, 5e12 + 194858),
}


def components(t, y, L, nmax=1000000):
    """Unmollified leading-order dominance components of Polymath's f_t with the
    exponents (1+y)/2 + tL/4 (A-sum) and (1-y)/2 + tL/4 (B-sum), |gamma| = e^{-yL/2},
    sums to N = min(e^{L/2}, nmax).  Planning diagnostic only."""
    N = min(int(math.exp(L / 2)), nmax)
    sA = 0.0
    sB = 0.0
    eA = (1 + y) / 2 + t * L / 4
    eB = (1 - y) / 2 + t * L / 4
    for n in range(2, N + 1):
        ln = math.log(n)
        b = math.exp(t / 4 * ln * ln)
        sA += b * math.exp(-eA * ln)
        sB += b * math.exp(-eB * ln)
    g = math.exp(-y * L / 2)
    return {"A_tail": sig(sA), "abs_gamma": sig(g), "B_part": sig(g * (1 + sB)),
            "triangle_margin_D": sig(1 - sA - g * (1 + sB)), "N": N}


def section_B(Lfam):
    out = {}
    for name, (t0, y0, X) in ROWS.items():
        L = math.log(X / (4 * PI))
        rec = {"t0": t0, "y0": y0, "X": sig(X), "L": sig(L), "tL": sig(t0 * L),
               "yL": sig(y0 * L), "Lambda_row": sig(t0 + y0 * y0 / 2),
               "components_at_row": components(t0, y0, L), "transfers": []}
        for Lp in Lfam:
            ts = t0 * L / Lp
            ys = y0 * L / Lp
            rec["transfers"].append({
                "L_family": sig(Lp),
                "scaled": {"t": sig(ts), "y": sig(ys), "Lambda": sig(ts + ys * ys / 2),
                           "components": components(ts, ys, Lp)},
                "y_fixed": {"t": sig(ts), "y": y0, "Lambda": sig(ts + y0 * y0 / 2),
                            "components": components(ts, y0, Lp)},
            })
        out[name] = rec
    return out


# ---------------------------------------------------------------------------
# C. Conditional strip constants
# ---------------------------------------------------------------------------

def section_C():
    res = {}
    for name, B in (("11/12 (audited 5 October chain)", Fraction(11, 12)),
                    ("7/8 (OpenAI 30 September preprint, Thm 1.1 as quoted by Liu)", Fraction(7, 8)),
                    ("34999/40000 (Liu, Thm 15.1)", Fraction(34999, 40000))):
        lam = (2 * B - 1) ** 2 / 2
        res[name] = {"B": str(B), "Delta=2B-1": str(2 * B - 1), "Lambda_bound": str(lam),
                     "decimal": sig(float(lam))}
    r = Decimal(921).sqrt()
    Bnew = (Decimal(1507) - 2 * r) / Decimal(1653)
    lam = (2 * Bnew - 1) ** 2 / 2
    exact = "(1867057 - 10888 sqrt(921))/5464818"
    check = (Decimal(1867057) - 10888 * r) / Decimal(5464818)
    res["B_new (Liu, Thm 21.1)"] = {"B": "(1507 - 2 sqrt 921)/1653", "B_decimal": f"{Bnew:.30f}",
                                    "Lambda_bound": exact, "decimal": f"{lam:.30f}",
                                    "closed_form_minus_direct": f"{(check - lam):.3e}"}
    return res


# ---------------------------------------------------------------------------
# D. sigma*(lambda)
# ---------------------------------------------------------------------------

def section_D():
    res = []
    for lam in (0.5, 25 / 72, 0.3046, 9 / 32, 0.25, 0.22, 0.2, 0.1787854):
        res.append({"lambda": sig(lam), "sigma_star": sig(0.5 + math.sqrt(2 * lam) / 2)})
    return {"identity": "y0^2 + 2 t0 = 2 (t0 + y0^2/2) = 2 lambda", "table": res}


# ---------------------------------------------------------------------------
# E. Large-conductor planning
# ---------------------------------------------------------------------------

def solve_L(lam, c1, c2):
    """Solve c1/L + c2^2/(2 L^2) = lam for L > 0."""
    # lam L^2 - c1 L - c2^2/2 = 0
    disc = c1 * c1 + 2 * lam * c2 * c2
    return (c1 + math.sqrt(disc)) / (2 * lam)


def section_E():
    t0, y0, X = ROWS["Polymath_Lambda<=0.22"]
    L = math.log(X / (4 * PI))
    c1, c2 = t0 * L, y0 * L
    res = []
    for lam in (0.45, 0.4, 0.35, 0.3046, 9 / 32, 0.25, 0.22, 0.2):
        Ls = solve_L(lam, c1, c2)
        ys = c2 / Ls
        row = {"lambda": sig(lam), "L_star": sig(Ls), "t": sig(c1 / Ls), "y": sig(ys)}
        for a in (0, 1):
            psi = digamma(complex((1 + ys + 2 * a) / 4, 0.0)).real
            q0 = PI * math.exp(Ls - psi)
            row[f"q0_parity_{a}"] = sig(q0)
            row[f"psi_shift_parity_{a}"] = sig(psi)
        row["A=2pi e^L*"] = sig(2 * PI * math.exp(Ls))
        res.append(row)
    return {"row_used": "Polymath, scaled transfer", "c1=tL": sig(c1), "c2=yL": sig(c2),
            "height_zero_L": "L_eff(q, a, y) = log(q/pi) + psi((1 + y + 2a)/4)", "table": res}


# ---------------------------------------------------------------------------
# F. Needed verification height below q0
# ---------------------------------------------------------------------------

def section_F():
    t0, y0, X = ROWS["Polymath_Lambda<=0.22"]
    L = math.log(X / (4 * PI))
    c1, c2 = t0 * L, y0 * L
    res = []
    for lam in (0.3046, 9 / 32, 0.25, 0.22):
        Ls = solve_L(lam, c1, c2)
        A = 2 * PI * math.exp(Ls)
        rows = []
        for q in (3, 4, 100, 10000, 400000):
            rows.append({"q": q, "T_star_stirling": sig(A / q), "Platt_t0": sig(platt_t0(q)),
                         "ratio": sig((A / q) / platt_t0(q))})
        res.append({"lambda": sig(lam), "L_star": sig(Ls), "A": sig(A), "moduli": rows})
    return res


# ---------------------------------------------------------------------------
# G. Family sizes
# ---------------------------------------------------------------------------

def section_G():
    """Number of primitive characters with conductor 3 <= q <= Q (multiplicative
    count p-2 at p, p^k (1-1/p)^2 at p^k, k >= 2), and of real ones (fundamental
    discriminants), so that the per-character work of a finite-set theorem is
    explicit; conjugate pairs share Lambda, so complex characters count once per pair."""
    Qs = (100, 1000, 10000, 100000)
    Qmax = max(Qs)
    spf = list(range(Qmax + 1))
    for i in range(2, int(Qmax ** 0.5) + 1):
        if spf[i] == i:
            for j in range(i * i, Qmax + 1, i):
                if spf[j] == j:
                    spf[j] = i

    def nprim(q):
        res = 1
        while q > 1:
            p = spf[q]
            k = 0
            while q % p == 0:
                q //= p
                k += 1
            if k == 1:
                res *= p - 2
            else:
                res *= p ** (k - 2) * (p - 1) ** 2
        return res

    def nreal(q):
        # real primitive characters mod q: 1 if q is |fundamental discriminant| (q > 1), counting
        # both signs when both +-q are fundamental (q = 8 has two: 8 and -8)
        cnt = 0
        for D in (q, -q):
            if is_fund(D):
                cnt += 1
        return cnt

    def squarefree(n):
        n = abs(n)
        while n > 1:
            p = spf[n]
            n //= p
            if n % p == 0:
                return False
        return True

    def is_fund(D):
        if D % 4 == 1:
            return squarefree(D)
        if D % 4 == 0:
            m = D // 4
            return (m % 4 in (2, 3)) and squarefree(m)
        return False

    out = []
    tot = 0
    totr = 0
    qprev = 2
    for Q in Qs:
        for q in range(qprev + 1, Q + 1):
            tot += nprim(q)
            totr += nreal(q)
        qprev = Q
        out.append({"Q": Q, "primitive_characters_3<=q<=Q": tot, "real_ones": totr,
                    "distinct_Lambda_classes(real + complex pairs)": totr + (tot - totr) // 2})
    return out


# ---------------------------------------------------------------------------
# H. The strip comparison of arXiv:2610.12803 transferred to the family
# ---------------------------------------------------------------------------

def zeta_real(s, N=40, M=14):
    """zeta(s) for complex s != 1 by Euler-Maclaurin (a = 1); used at real
    sigma and, with a 1e-20 imaginary step, for zeta'(sigma)."""
    import cmath
    total = 0j
    for k in range(1, N + 1):
        total += cmath.exp(-s * math.log(k))
    Na = N + 1.0
    lNa = math.log(Na)
    total += cmath.exp((1 - s) * lNa) / (s - 1)
    total += 0.5 * cmath.exp(-s * lNa)
    rising = s
    fact = 2.0
    for j in range(1, M + 1):
        total += float(BERN[2 * j]) / fact * rising * cmath.exp((-s - 2 * j + 1) * lNa)
        rising *= (s + 2 * j - 1) * (s + 2 * j)
        fact *= (2 * j + 1) * (2 * j + 2)
    return total


def log_deriv_zeta_neg(sigma):
    """-zeta'/zeta(sigma), by the complex-step derivative."""
    h = 1e-20
    z = zeta_real(complex(sigma, h))
    return -(z.imag / h) / z.real


def S_floor(logq_over_pi, a_par, p):
    """Exact time-zero lower bound for S(x,p,0) = (1/2) Re (xi'/xi)((1+p+ix)/2)
    over all real x: (1/4)(log(q/pi) + psi((1+p)/4 + a/2)) - (1/2)(-zeta'/zeta)((1+p)/2),
    using Re psi increasing in |Im| and |L'/L(s,chi)| <= -zeta'/zeta(Re s)."""
    return 0.25 * (logq_over_pi + digamma(complex((1 + p) / 4 + a_par / 2, 0.0)).real) \
        - 0.5 * log_deriv_zeta_neg((1 + p) / 2)


def comparison_time(C, p, a, b=0.0, m=4000):
    """Time for the comparison ODE Q' = -2 - (4C/p) Q + 8Q/(p^2 - Q) to bring Q from
    a to b (Simpson in Q); returns None if the right side is not negative throughout."""
    def rate(Qv):
        return 2 + (4 * C / p) * Qv - 8 * Qv / (p * p - Qv)
    for j in range(m + 1):
        if rate(b + (a - b) * j / m) <= 0:
            return None
    h = (a - b) / m
    tot = 1 / rate(b) + 1 / rate(a)
    for j in range(1, m):
        tot += (4 if j % 2 else 2) / rate(b + j * h)
    return tot * h / 3


def best_over_p(logq, a_par, a, b=0.0, Cshift=0.0):
    best = None
    pmin = math.sqrt(5 * a)
    for i in range(0, 801):
        p = pmin + 0.01 * i
        C = S_floor(logq, a_par, p) + Cshift
        if C <= 0:
            continue
        t = comparison_time(C, p, a, b)
        if t is None:
            continue
        lam = t + b / 2
        if best is None or lam < best[0]:
            best = (lam, p, C, t)
    return best


def section_H():
    """Planning values for the strip comparison in the large-conductor regime
    (no finite region: S bounded below at every height) and, for reference, in
    a Platt-type regime where the comparison must stop at b = 1/25 (the finite
    region of their Lemma 2) and S is evaluated at large heights (log conductor L)."""
    out = {"zeta_checks": {"-zeta'/zeta(2)": sig(log_deriv_zeta_neg(2.0)),
                           "zeta(2)-pi^2/6": sig(zeta_real(2.0).real - PI * PI / 6)}}
    # Calibration against the paper's one-step bound (18): C = 21/4, p = 4, a = 9/16, b = 1/25
    k = 21 / 4 - 8 / (16 - 9 / 16)
    one_step = 1 / 50 + (1 / k) * math.log((2 + k * 9 / 16) / (2 + k / 25))
    exact_ode = 1 / 50 + comparison_time(21 / 4, 4.0, 9 / 16, 1 / 25)
    out["calibration_paper_eq18"] = {"one_step_formula": sig(one_step),
                                     "paper_value": "0.1797275414...",
                                     "exact_ODE_same_constants": sig(exact_ode)}
    rows = []
    for q in (10 ** 3, 10 ** 4, 10 ** 5, 10 ** 6, 10 ** 8, 10 ** 10, 10 ** 12):
        lq = math.log(q / PI)
        for a_par in (0, 1):
            row = {"q": q, "parity": a_par}
            for label, a in (("unconditional_a=1", 1.0), ("half-plane_7/8_a=9/16", 9 / 16)):
                r = best_over_p(lq, a_par, a)
                row[label] = None if r is None else {"lambda": sig(r[0]), "p": sig(r[1]), "C": sig(r[2])}
            rows.append(row)
    out["large_conductor_all_heights"] = rows
    # Platt-type regime: S at large height x with log conductor L (psi ~ log), comparison to b=1/25
    plat = []
    for L in (16.58, 17.02, 22.2866, 26.7094):
        row = {"L": L}
        for label, a in (("unconditional_a=1", 1.0), ("half-plane_7/8_a=9/16", 9 / 16)):
            best = None
            for i in range(0, 801):
                p = math.sqrt(5 * a) + 0.01 * i
                C = 0.25 * L - 0.5 * log_deriv_zeta_neg((1 + p) / 2)
                t = comparison_time(C, p, a, 1 / 25)
                if t is None:
                    continue
                lam = t + 1 / 50
                if best is None or lam < best[0]:
                    best = (lam, p, C)
            row[label] = None if best is None else {"lambda": sig(best[0]), "p": sig(best[1]), "C": sig(best[2])}
        plat.append(row)
    out["finite_region_regime_b=1/25"] = plat
    out["note"] = ("S floors are exact time-zero lower bounds; holding them on the whole comparison "
                   "interval is the planning hypothesis (Lemma A_p would supply it); the finite-region "
                   "rows also need the per-character barrier of the paper's Lemma 2 over that interval")
    return out


def main():
    A = section_A()
    Lfam = [16.58, 17.02, 20.0, 22.2866, 26.7094]
    rec = {
        "script": "benchmark_family_contract_claude_20261017.py",
        "model": "Claude Opus 5.5 (claude-opus-5-5), Claude Cowork, effort max",
        "date": "2026-10-17",
        "status": "planning arithmetic under a stated scaling hypothesis; no bound is asserted",
        "A_platt_budget": A,
        "B_zeta_rows_and_transfer": section_B(Lfam),
        "C_conditional_strip": section_C(),
        "D_sigma_star": section_D(),
        "E_large_conductor_planning": section_E(),
        "F_needed_verification": section_F(),
        "G_family_sizes": section_G(),
        "H_strip_comparison_planning": section_H(),
    }
    print(json.dumps(rec, indent=1, sort_keys=True))


if __name__ == "__main__":
    main()
