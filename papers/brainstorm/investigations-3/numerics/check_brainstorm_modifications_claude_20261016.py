#!/usr/bin/env python3
"""Labelled numerical computations behind the Claude brainstorm note
notes/03_MODIFICATIONS_AND_ALTERNATIVE_DIRECTIONS_CLAUDE_20261016.md
(papers/brainstorm/investigations-3).

16 October 2026. Prepared for Edward Baker with LLM assistance. Model:
Claude Fable 5.1 (configured identifier claude-fable-5-1), Claude Cowork.
Standard library only; deterministic; prints one JSON record to stdout.

Everything here is a floating-point computation that supports a remark in
the note. Nothing is certified, and nothing here is a theorem about zeta.

Sections
  A. Scale of the physical theta field against the size of the second
     square term of its source (Direction 1 remark: sup-norm closeness of
     sources is not the relevant measure).
  B. Minimal coefficient perturbation of the first three square weights
     that creates a collision at a given (t, x): the coefficient-space
     "collision distance" proposed as the first test of Direction 1.
  C. The attraction law for a complex zero of the heat flow, with the
     surrounding zero count bounded below by the Riemann-von Mangoldt
     formula and Trudgian's explicit bound on S(T) (Direction 4 remark).
     Includes a grid check of the elementary inequality used for the pull
     of a lower zero and its conjugate.
"""
import json
import math

PI = math.pi


# ---------------------------------------------------------------------------
# Source terms and quadrature
# ---------------------------------------------------------------------------

def phi_term(n, u):
    """n-th square term of the Polya source on u >= 0."""
    q = PI * n * n * math.exp(4.0 * u)
    if q > 700.0:
        return 0.0
    return (2.0 * q * q - 3.0 * q) * math.exp(u - q)


def simpson(f, a, b, m):
    """Composite Simpson rule with m (even) panels."""
    if m % 2:
        m += 1
    h = (b - a) / m
    s = f(a) + f(b)
    for k in range(1, m):
        s += (4.0 if k % 2 else 2.0) * f(a + k * h)
    return s * h / 3.0


U_MAX = 1.8      # phi_n(u) is below 1e-300 well before this point
PANELS = 36000


def term_transform(n, t, x, deriv=0):
    """H_n(t,x) = int_0^inf e^{tu^2} phi_n(u) cos(xu) du, or its x-derivative."""
    if deriv == 0:
        f = lambda u: math.exp(t * u * u) * phi_term(n, u) * math.cos(x * u)
    else:
        f = lambda u: -u * math.exp(t * u * u) * phi_term(n, u) * math.sin(x * u)
    return simpson(f, 0.0, U_MAX, PANELS)


def field(t, x, nmax=6, deriv=0):
    return sum(term_transform(n, t, x, deriv) for n in range(1, nmax + 1))


# ---------------------------------------------------------------------------
# A. field scale against source scale
# ---------------------------------------------------------------------------

def section_a():
    out = {}
    x = 44.1303          # near the three-square control's collision abscissa
    for t in (0.0, 0.25):
        H = field(t, x)
        Hx = field(t, x, deriv=1)
        H2 = term_transform(2, t, x)
        out["t=%g" % t] = {
            "x": x,
            "H(t,x)": H,
            "H_x(t,x)": Hx,
            "second_term_transform_H_2(t,x)": H2,
            "ratio_|H_2|/|H|": abs(H2) / abs(H) if H else None,
        }
    # size of the second square term in the source itself
    grid = [k * 0.005 for k in range(0, 400)]
    sup2 = max(abs(phi_term(2, u)) for u in grid)
    sup1 = max(abs(phi_term(1, u)) for u in grid)
    out["sup_u>=0 |phi_2|"] = sup2
    out["sup_u>=0 |phi_1|"] = sup1
    out["phi_2(0)"] = phi_term(2, 0.0)
    out["phi_3(0)"] = phi_term(3, 0.0)
    out["exp(-pi*x/8)"] = math.exp(-PI * x / 8.0)
    out["comment"] = ("The second square term is of order 1e-3 in the source "
                      "while the physical field at this height is of order "
                      "1e-6 to 1e-7; the term's own transform is of the same "
                      "order as the whole field, so coefficient perturbations "
                      "act at relative order one on the field although they "
                      "are small in the source's sup norm.")
    return out


# ---------------------------------------------------------------------------
# B. coefficient-space collision distance for the first three square weights
# ---------------------------------------------------------------------------

def min_norm_solution(rows, rhs):
    """Minimal Euclidean-norm solution of the 2 x k system rows . d = rhs
    (rows: two lists of length k), via the normal equations A A^T y = rhs."""
    a, b = rows
    g11 = sum(v * v for v in a)
    g12 = sum(v * w for v, w in zip(a, b))
    g22 = sum(w * w for w in b)
    det = g11 * g22 - g12 * g12
    if det == 0.0:
        return None, None
    y1 = (g22 * rhs[0] - g12 * rhs[1]) / det
    y2 = (-g12 * rhs[0] + g11 * rhs[1]) / det
    d = [y1 * v + y2 * w for v, w in zip(a, b)]
    return d, math.sqrt(sum(v * v for v in d))


def dphi_term(n, u, h=1e-5):
    return (phi_term(n, u + h) - phi_term(n, u - h)) / (2.0 * h)


def section_b():
    """Endpoint tails of the half-line square terms, and what the first
    reflection endpoint must be held to for the physical field to survive.
    The even extension of a single half-line term has a corner at u=0, so
    its cosine transform has the algebraic tail -phi_n'(0)/x^2 + ...; the
    tails cancel in the complete source because Phi'(0)=0 (reflection)."""
    out = {}
    dp = {n: dphi_term(n, 0.0) for n in range(1, 7)}
    out["phi_n'(0)"] = dp
    out["sum_{n<=6} phi_n'(0)"] = sum(dp.values())
    tails = {}
    for x in (30.0, 44.1303, 60.0):
        H = field(0.0, x)
        Hn = {n: term_transform(n, 0.0, x) for n in (1, 2, 3)}
        tails["x=%g" % x] = {
            "H(0,x)": H,
            "H_n(0,x)": Hn,
            "x^2 H_n(0,x) vs -phi_n'(0)": {n: [x * x * Hn[n], -dp[n]] for n in (1, 2)},
            "|H|/|H_1|": abs(H) / abs(Hn[1]),
            "tolerance_on_first_endpoint_|delta Phi'(0)| = |H| x^2": abs(H) * x * x,
            "same_as_relative_perturbation_of_a_1": abs(H) * x * x / abs(dp[1]),
        }
    out["tails"] = tails
    # the three-square control of 22 Note 05/01 (raw weights, interval midpoints)
    a2, a3 = 0.879175, 57742.5
    grid = [k * 0.005 for k in range(0, 400)]
    dist = max(abs((a2 - 1.0) * phi_term(2, u) + (a3 - 1.0) * phi_term(3, u)
                   - sum(phi_term(n, u) for n in range(4, 7))) for u in grid)
    t, x = 0.25, 44.1303
    H = field(t, x)
    Hx = field(t, x, deriv=1)
    out["three_square_control"] = {
        "raw_weights_used": {"a_1": 1.0, "a_2": a2, "a_3": a3},
        "source": "22 Note 05/01, Section 5 table (interval midpoints)",
        "sup_norm_distance_of_half-line_sources": dist,
        "theta_field_at_(1/4,44.1303)": {"H": H, "H_x": Hx, "E": H * H + Hx * Hx},
        "ratio_source_distance/|H|": dist / abs(H),
        "comment": ("the control's half-line source is within about 1e-4 of "
                    "theta's in sup norm and collides where theta's own field "
                    "is of order 1e-6; closeness of sources on the half-line "
                    "is not the measure in which collisions are decided"),
    }
    out["comment"] = ("For the even extension of a half-line comb, a defect "
                      "delta in the first reflection endpoint produces a "
                      "field tail -delta/x^2 that swamps the physical field "
                      "once |delta| exceeds |H(x)| x^2, which decreases like "
                      "x^2 exp(-pi x/8): the tolerance is exponentially small "
                      "in the height.")
    return out


# ---------------------------------------------------------------------------
# C. attraction law numbers
# ---------------------------------------------------------------------------

def trudgian_S_bound(T):
    """|S(T)| <= 0.111 log T + 0.275 log log T + 2.450 for T >= e
    (Trudgian, arXiv:1208.5846, Theorem 1)."""
    return 0.111 * math.log(T) + 0.275 * math.log(math.log(T)) + 2.450


def pull_lower_bound(b, L, S_max, D):
    """Lower bound for the downward pull on the topmost complex zero at
    imaginary part b from the zeros within horizontal distance D (x-units),
    counting all zeros at or below it: count >= (D/(2 pi)) L - 2 S_max - 2
    (the pair itself removed), each contributing at least 4b/(D^2+4b^2)."""
    count = (D / (2.0 * PI)) * L - 2.0 * S_max - 2.0
    if count <= 0.0:
        return 0.0
    return count * 4.0 * b / (D * D + 4.0 * b * b)


def best_pull_coefficient(L, S_max, b):
    best = 0.0
    bestD = None
    D = 0.5
    while D <= 60.0:
        p = pull_lower_bound(b, L, S_max, D)
        if p > best:
            best, bestD = p, D
        D += 0.05
    return best, bestD


def collision_time(b0, L, S_max, steps=4000):
    """Time for the topmost imaginary part to fall from b0 to 0 under
    db/dt <= -1/b - pull(b), integrating the bound (upper bound on time)."""
    total = 0.0
    h = b0 / steps
    for k in range(steps):
        b = (k + 0.5) * h
        p, _ = best_pull_coefficient(L, S_max, b)
        total += h / (1.0 / b + p)
    return total


def section_c():
    out = {}
    # grid check of the elementary inequality
    worst = float("inf")
    for d in [0.05 * k for k in range(0, 101)]:
        for b in [0.05 * k for k in range(1, 41)]:
            for c in [b * j / 40.0 for j in range(0, 41)]:
                g = lambda y: 2.0 * y / (d * d + y * y) if (d * d + y * y) > 0 else 0.0
                lhs = g(b - c) + g(b + c)
                rhs = 4.0 * b / (d * d + 4.0 * b * b)
                if rhs > 0:
                    worst = min(worst, lhs / rhs)
    out["inequality_check"] = {
        "statement": "g(b-c)+g(b+c) >= 4b/(d^2+4b^2) for 0<=c<=b, g(y)=2y/(d^2+y^2)",
        "min_ratio_lhs_over_rhs_on_grid": worst,
        "grid": "d in [0,5] step 0.05, b in (0,2] step 0.05, c in [0,b] 41 points",
    }
    # Riemann-von Mangoldt count near the current verification height
    T = 3.0e12
    L = math.log(2.0 * T / (4.0 * PI))
    S_max = trudgian_S_bound(T)
    rows = []
    for b in (1.0, 0.5, 0.25):
        p, D = best_pull_coefficient(L, S_max, b)
        rows.append({"b": b, "pull_lower_bound": p, "best_window_D": D,
                     "universal_term_1/b": 1.0 / b})
    out["at_T=3e12"] = {
        "L=log(x/4pi)": L, "S_max": S_max, "pulls": rows,
        "collision_time_bound_from_b0=1": collision_time(1.0, L, S_max),
        "de_Bruijn_time_b0^2/2": 0.5,
        "Polymath/Platt-Trudgian_published": 0.2,
    }
    # heuristic full-density case (as if every zero in the window were real
    # and counted exactly): pull = L/2 per unit b, no S(T) loss
    cfull = L / 2.0
    out["heuristic_full_density"] = {
        "pull_coefficient_L/2": cfull,
        "collision_time_from_b0=1": (1.0 / cfull) * (1.0 - math.log(1.0 + cfull) / cfull),
        "comment": "requires the local zero count at the scale of a few spacings, "
                   "i.e. RH-verification-strength information at that height",
    }
    # growth with height
    asym = []
    for T in (1e15, 1e20, 1e30, 1e50):
        L = math.log(2.0 * T / (4.0 * PI))
        S_max = trudgian_S_bound(T)
        asym.append({"T": T, "L": L,
                     "collision_time_bound_from_b0=1": collision_time(1.0, L, S_max, steps=800),
                     "first_term_dominance_4.5/L": 4.5 / L})
    out["growth_with_height"] = asym
    return out


def rounded(obj, digits=12):
    """Round every float to `digits` significant figures so that the record
    is byte-identical across platforms (libm differences appear in the last
    one or two bits of the quadratures)."""
    if isinstance(obj, float):
        if obj == 0.0 or math.isnan(obj) or math.isinf(obj):
            return obj
        return float("%.*e" % (digits - 1, obj))
    if isinstance(obj, dict):
        return {k: rounded(v, digits) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [rounded(v, digits) for v in obj]
    return obj


def main():
    record = {
        "note": "03_MODIFICATIONS_AND_ALTERNATIVE_DIRECTIONS_CLAUDE_20261016.md",
        "model": "Claude Fable 5.1 (claude-fable-5-1), Claude Cowork",
        "date": "2026-10-16",
        "status": "floating-point support computations; not certified; "
                  "floats rounded to 12 significant figures for cross-platform "
                  "byte identity",
        "A_field_scale_vs_source_scale": section_a(),
        "B_coefficient_space_collision_distance": section_b(),
        "C_attraction_law": section_c(),
    }
    print(json.dumps(rounded(record), indent=1, sort_keys=False))


if __name__ == "__main__":
    main()
