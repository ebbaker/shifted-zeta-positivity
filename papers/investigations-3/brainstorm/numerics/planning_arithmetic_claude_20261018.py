#!/usr/bin/env python3
"""Planning arithmetic for the investigations-3 direction review.

Prepared for Edward Baker with LLM assistance. Model: Claude Fable 5.1
(claude-fable-5-1), Claude Cowork, 18 October 2026 (session configured as
claude-opus-5-5; the serving model may differ from the configured identifier).

Standard-library floating point only. Nothing here is a certificate: the
script evaluates the closed-form consequences of the repository's own
statements (the conductor-rate note's T(q), Hakimoglu-Brown's kernel
constant k = 4C/p - 8/(p^2 - q) with q <= 1, and the restart time
log(1 + k Q_0 / 2) / k) under stated planning assumptions, so that the
review's judgments about what is worth optimizing rest on numbers rather
than impressions. Every assumption is recorded in the output.

Sections of the record:
  A  T(q) from the conductor-rate note at a ladder of conductors, with the
     asymptotic form 3(log log q - log 6)/log q for comparison.
  B  Sensitivity of T(10^12) to the transport remainder E (the quantity the
     correlated-Gaussian pilot of brainstorm note 03 would improve).
  C  Dependence on the comparison height p in [sqrt 5, 4] at q = 10^12,
     with the time-zero Euler floor kappa((1+p)/2) and an assumed remainder
     E_p in {0.2, 0.4} (E_p is certified only at p = 3).
  D  Dependence on the initial squared strip Q_0 (1 unconditionally; 9/16 if
     a zero-free half-plane Re s > 7/8 held for the character).
  E  Crossover between T(q) and a hypothetical O(1/log q) bound c/ell for
     several c, to locate where an improved asymptotic rate would matter.
  F  The smallest conductor at which the restart mechanism is nonvacuous
     (C(q) > 3/4) and T(q) < 1/2, if the transport envelope E < 1/5 were
     extended below q = 10^12 (it is not certified there).

kappa(sigma) = -zeta'/zeta(sigma) is computed as sum_{n <= N} Lambda(n) n^{-sigma}
plus an upper bound for the tail, so the floor is slightly understated and
the resulting times slightly overstated (safe direction for planning).
"""
import json
import math
import sys

GAMMA = 0.5772156649015329
PI = math.pi


def von_mangoldt_table(N):
    """Return a list lam with lam[n] = Lambda(n) for 0 <= n <= N."""
    lam = [0.0] * (N + 1)
    is_comp = bytearray(N + 1)
    for p in range(2, N + 1):
        if is_comp[p]:
            continue
        lp = math.log(p)
        m = p
        while m <= N:
            lam[m] = lp
            m *= p
        for k in range(p * p, N + 1, p):
            is_comp[k] = 1
    return lam


LAM = von_mangoldt_table(200000)


def kappa(sigma):
    """-zeta'/zeta(sigma) for sigma > 1.3: finite sum plus tail upper bound.

    Tail: sum_{n > N} Lambda(n) n^{-sigma} <= sum_{n > N} log(n) n^{-sigma}
          <= int_N^inf log(u) u^{-sigma} du
           = N^{1-sigma} (log N/(sigma-1) + 1/(sigma-1)^2).
    """
    N = len(LAM) - 1
    s = 0.0
    for n in range(2, N + 1):
        if LAM[n]:
            s += LAM[n] * n ** (-sigma)
    tail = N ** (1 - sigma) * (math.log(N) / (sigma - 1) + 1 / (sigma - 1) ** 2)
    return s, s + tail


def L_of_log10q(e):
    """L(q) = log(q/pi) - gamma for q = 10^e, computed in log space."""
    return e * math.log(10) - math.log(PI) - GAMMA


def C_of_L(L, floor_loss=77 / 200):
    return L / 4 - floor_loss


def restart_time(k, Q0=1.0):
    """Time for Q' = -2 - kQ to reach zero from Q0 (k > 0)."""
    return math.log(1 + k * Q0 / 2) / k


def T_rate(e, floor_loss=77 / 200, p=3.0, Q0=1.0):
    """Restart time at q = 10^e with Hakimoglu-Brown's k = 4C/p - 8/(p^2 - 1) (worst Q <= 1)."""
    C = C_of_L(L_of_log10q(e), floor_loss)
    k = 4 * C / p - 8 / (p * p - 1)
    if k <= 0:
        return None, C, k
    return restart_time(k, Q0), C, k


record = {
    "title": "Planning arithmetic for the investigations-3 direction review",
    "model": "Claude Fable 5.1 (claude-fable-5-1), Claude Cowork, effort max; "
             "session configured as claude-opus-5-5",
    "date": "2026-10-18",
    "status": "floating-point planning arithmetic; not a certificate",
    "environment": "standard-library Python 3; the record carries no version string so that "
                   "identical arithmetic gives an identical file on any machine",
    "conventions": {
        "L(q)": "log(q/pi) - gamma  (the conductor-rate note's main term, even parity)",
        "C(q)": "L(q)/4 - 77/200, i.e. kappa(2)/2 < 57/200 and E/2 < 1/10 subtracted",
        "k": "4C/p - 8/(p^2 - 1), Hakimoglu-Brown's constant at worst strip Q = 1 (p = 3 gives 4C/3 - 1)",
        "T": "log(1 + k Q_0/2)/k, the restart time from squared strip Q_0",
        "kappa": "-zeta'/zeta(sigma): finite sum to 200000 plus integral tail bound (upper value used)",
    },
}

# ---- A: ladder of conductors -------------------------------------------------
A = []
for e in [12, 13, 14, 15, 18, 20, 25, 30, 40, 50, 75, 100, 200, 500]:
    T, C, k = T_rate(e)
    lq = e * math.log(10)
    asym = 3 * (math.log(lq) - math.log(6)) / lq
    A.append({"q": f"1e{e}", "L": round(L_of_log10q(e), 4), "C": round(C, 4), "k": round(k, 4),
              "T": round(T, 6), "asymptotic_3loglog_over_log": round(asym, 6)})
record["A_conductor_ladder"] = A

# ---- B: sensitivity to E at q = 1e12 -----------------------------------------
q12 = 12
B = []
for E in [0.2, 0.15, 0.1, 0.05, 0.0]:
    loss = 57 / 200 + E / 2
    T, C, k = T_rate(q12, floor_loss=loss)
    B.append({"E": E, "C": round(C, 5), "k": round(k, 5), "T": round(T, 6)})
T_base = B[0]["T"]
record["B_sensitivity_to_E_at_1e12"] = {
    "rows": B,
    "relative_gain_if_E_were_zero": round((T_base - B[-1]["T"]) / T_base, 4),
    "note": "the repository's certified E < 1/5 enters T only through 77/200; "
            "removing it entirely changes T by about one percent",
}

# ---- C: dependence on the comparison height p at q = 1e12 ---------------------
C_rows = []
for p in [math.sqrt(5), 2.4, 2.6, 2.8, 3.0, 3.5, 4.0]:
    sigma0 = (1 + p) / 2
    kap_lo, kap_hi = kappa(sigma0)
    row = {"p": round(p, 4), "sigma0": round(sigma0, 4), "kappa_sigma0_upper": round(kap_hi, 5)}
    for Ep in [0.2, 0.4]:
        loss = kap_hi / 2 + Ep / 2
        T, Cq, k = T_rate(q12, floor_loss=loss, p=p)
        row[f"T_if_E={Ep}"] = None if T is None else round(T, 6)
        row[f"k_if_E={Ep}"] = round(k, 5)
    C_rows.append(row)
record["C_height_p_dependence_at_1e12"] = {
    "rows": C_rows,
    "note": "p^2 >= 5 Q_0 requires p >= sqrt 5 for Q_0 = 1; E_p is certified only at p = 3 "
            "(E < 0.192767); the two E columns bracket what a lower height might cost",
}

# ---- D: dependence on the initial strip ---------------------------------------
D = []
for Q0, label in [(1.0, "unconditional strip |Im z| <= 1"),
                  (9 / 16, "if Re s > 7/8 were zero-free for the character"),
                  (1 / 4, "if Re s > 3/4 were zero-free for the character")]:
    T, Cq, k = T_rate(q12, Q0=Q0)
    D.append({"Q0": round(Q0, 4), "assumption": label, "T_at_1e12": round(T, 6),
              "de_Bruijn_alone": round(Q0 / 2, 4)})
record["D_initial_strip_dependence_at_1e12"] = D

# ---- E: crossover with a hypothetical c/ell bound -------------------------------
E_rows = []
for c in [5.0, 7.0, 9.0, 12.0]:
    # find smallest ell (= L) with c/ell < T(ell)
    found = None
    ell = 26.0
    while ell < 5000:
        C = ell / 4 - 77 / 200
        k = 4 * C / 3 - 1
        T = restart_time(k)
        if c / ell < T:
            found = ell
            break
        ell += 0.5
    q_cross = None if found is None else math.exp(found + GAMMA) * PI
    E_rows.append({"c": c, "crossover_L": found,
                   "crossover_q_log10": None if q_cross is None else round(math.log10(q_cross), 1)})
record["E_crossover_with_c_over_log_q"] = {
    "rows": E_rows,
    "note": "T(q) wins below the crossover; an O(1/log q) bound with constant c only "
            "matters for conductors above 10^(crossover_q_log10)",
}

# ---- F: smallest conductor where the mechanism is nonvacuous ------------------
F = {}
# C(q) > 3/4  <=>  L(q) > 4.54
L_min = 4 * (3 / 4 + 77 / 200)
F["L_for_C_above_3_over_4"] = round(L_min, 4)
F["q_for_C_above_3_over_4"] = round(PI * math.exp(L_min + GAMMA), 1)
rows = []
for e in [3, 4, 5, 6, 8, 10]:
    T, C, k = T_rate(e)
    rows.append({"q": f"1e{e}", "L": round(L_of_log10q(e), 4), "C": round(C, 4), "k": round(k, 4),
                 "T_if_E_lt_1_over_5_held": None if T is None else round(T, 6)})
F["ladder_below_1e12"] = rows
F["note"] = ("E < 1/5 is certified only for ell >= 129/5 (q >= 10^12); these rows show what the "
             "same restart would give if the envelope were extended, and where the conclusion "
             "becomes numerically testable on actual characters")
record["F_small_conductor_feasibility"] = F

# ---- G: the two gates of the conductor-rate note, recomputed ----------------
T12, C12, k12 = T_rate(q12)
record["G_checks_against_the_conductor_rate_note"] = {
    "L(1e12)": round(L_of_log10q(q12), 9),
    "note_states_L_gt": 25.909075565,
    "C(1e12)": round(C12, 6),
    "k(1e12)": round(k12, 6),
    "T(1e12)": round(T12, 10),
    "note_states_T_approx": 0.2130631631,
    "log(9/2)/7": round(math.log(4.5) / 7, 9),
    "43/200": 0.215,
    "restart_note_k_2623_over_375": round(2623 / 375, 6),
    "restart_note_terminal_gate_exp(kT)_vs_1+k/2": [round(math.exp(2623 / 375 * 43 / 200), 6), round(1 + 2623 / 750, 6)],
}

json.dump(record, sys.stdout, indent=1)
sys.stdout.write("\n")
