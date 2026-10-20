#!/usr/bin/env python3
"""Exact controls and rational coefficient enclosures for BW-08 Note 03.

Prepared for Edward Baker, 19 October 2026, with substantial LLM assistance.
Recorded model: gpt-6-astra; reasoning effort: max.
No theta jets or threshold locations are computed. Standard library only.
"""

import argparse
from datetime import datetime, timezone
from fractions import Fraction as F
import hashlib
import json
from math import factorial
from pathlib import Path
import subprocess


ATAN_TERMS = 48
LOG_TERMS = 64
BASE = Path("papers/investigations-3/13_contradiction_analysis/04_boundary_winding")
ROUTE = BASE / "threshold_routes/08_deflated_jet_hierarchy"


def decimal_endpoint(x, digits, upper=False):
    scale = 10**digits
    n = (x.numerator * scale) // x.denominator
    if upper and F(n, scale) != x:
        n += 1
    sign = "-" if n < 0 else ""
    n = abs(n)
    return f"{sign}{n // scale}.{n % scale:0{digits}d}"


def show_interval(bounds, digits=15):
    lo, hi = bounds
    assert lo <= hi
    return [decimal_endpoint(lo, digits), decimal_endpoint(hi, digits, True)]


def atan_bounds(x):
    assert 0 < x < 1
    total = sum(((-1)**j * x**(2*j+1) / (2*j+1)
                 for j in range(ATAN_TERMS)), F(0))
    adjacent = total + (-1)**ATAN_TERMS * x**(2*ATAN_TERMS+1) / (2*ATAN_TERMS+1)
    return min(total, adjacent), max(total, adjacent)


def pi_bounds():
    a, b = atan_bounds(F(1, 5)), atan_bounds(F(1, 239))
    exact = (16*a[0]-4*b[1], 16*a[1]-4*b[0])
    # Rational outward decimal endpoints shorten subsequent denominators.
    return tuple(F(s) for s in show_interval(exact, 40))


def log_unit_bounds(x):
    assert 1 <= x <= 2
    q = (x-1)/(x+1)
    total = 2*sum((q**(2*j+1)/(2*j+1) for j in range(LOG_TERMS)), F(0))
    remainder = 2*q**(2*LOG_TERMS+1)/((2*LOG_TERMS+1)*(1-q*q))
    return total, total+remainder


def log_bounds(x):
    assert x > 0
    k = 0
    while x >= 2:
        x /= 2
        k += 1
    while x < 1:
        x *= 2
        k -= 1
    lo, hi = log_unit_bounds(x)
    l2, u2 = log_unit_bounds(F(2))
    return (lo+k*l2, hi+k*u2) if k >= 0 else (lo+k*u2, hi+k*l2)


def coefficient_bounds(a, pi):
    a = F(a)
    log_lo = log_bounds((a+1)/(4*pi[1]))[0]
    log_hi = log_bounds((a+1)/(4*pi[0]))[1]
    ell = (log_lo/(4*a)-F(3, 2)/(a*a), log_hi/(4*a)-F(3, 2)/(a*a))
    mirror = 1/(2*a*a)
    assert ell[0] > mirror
    return ell, (log_lo/4, log_hi/4), {
        "hypothetical_a": int(a),
        "mirror_bound_exact": str(mirror),
        "new_ell_outward": show_interval(ell),
        "ratio_to_mirror_outward": show_interval(tuple(v/mirror for v in ell), 8),
        "D_floor_outward": show_interval((log_lo/4, log_hi/4)),
        "six_ell_outward": show_interval(tuple(6*v for v in ell)),
    }


def mul(p, q, limit=None):
    result = [F(0)] * (len(p)+len(q)-1)
    for i, v in enumerate(p):
        for j, w in enumerate(q):
            result[i+j] += v*w
    return result if limit is None else (result+[F(0)]*limit)[:limit]


def derivative(p, order):
    return [p[j]*F(factorial(j), factorial(j-order)) for j in range(order, len(p))]


def evaluate(p, x):
    result = F(0)
    for coefficient in reversed(p):
        result = result*x+coefficient
    return result


def heat_critical_series(jets):
    """Substitute the critical curve to order two in the finite heat flow.

    H(s,a+y)=sum (-s)^k h_(j+2k) y^j/(k! j!). Terms through s^3
    depend only on c1,c2, because Hx(0,a)=0.
    """
    h2, h3, h4, h5 = jets[2:6]
    c1 = h3/h2
    c2 = (h4*c1-h3*c1*c1/2-h5/2)/h2
    curve = [F(0), c1, c2, F(0)]
    result = [F(0)]*4
    power = [F(1), F(0), F(0), F(0)]
    for j in range(4):
        for k in range(4):
            if j+2*k >= len(jets):
                continue
            coefficient = F((-1)**k, factorial(k)*factorial(j))*jets[j+2*k]
            for n in range(4-k):
                result[n+k] += coefficient*power[n]
        power = mul(power, curve, 4)
    return result


def polynomial_control(name, a, pairs, scale, floor=None):
    a = F(a)
    p = [F(scale)]
    for root, multiplicity in pairs:
        for _ in range(multiplicity):
            p = mul(p, [-F(root)**2, F(0), F(1)])
    jets = [evaluate(derivative(p, j), a) for j in range(max(7, len(p)))]
    assert jets[0] == jets[1] == 0 and jets[2] != 0
    h2, h3, h4, h5, h6 = jets[2:7]
    jet_s = h3*h3/(9*h2*h2)-h4/(6*h2)
    root_s = F(1, 2)/(a*a)
    for root, multiplicity in pairs:
        root = F(root)
        if root != a:
            root_s += multiplicity*(1/(a-root)**2+1/(a+root)**2)
    assert jet_s == root_s
    imaginary_poly = [v*((-1)**(j//2)) if j % 2 == 0 else F(0)
                      for j, v in enumerate(p)]
    d_from_coefficients = evaluate(derivative(imaginary_poly, 1), a)/evaluate(imaginary_poly, a)
    d_from_roots = sum((2*a*m/(F(r)**2+a*a) for r, m in pairs), F(0))
    assert d_from_coefficients == d_from_roots
    gap = jet_s-(d_from_coefficients/a-F(3, 2)/(a*a))
    assert gap >= 0
    second = h4-h3*h3/h2
    third = -h6+3*h3*h5/h2-3*h3*h3*h4/(h2*h2)+h3**4/h2**3
    series = heat_critical_series(jets)
    assert series[0] == 0 and series[1] == -h2
    assert 2*series[2] == second and 6*series[3] == third
    assert second/h2 == -(h3/h2)**2/3-6*jet_s
    floor_status = "outside a>=20 range"
    if floor is not None:
        floor_status = ("passes scalar D floor" if d_from_coefficients > floor[1]
                        else "fails scalar D floor" if d_from_coefficients < floor[0]
                        else "inconclusive")
    return {
        "name": name, "a": str(a), "degree": len(p)-1, "source": "own finite polynomial",
        "h2_h3_h4_h5_h6": [str(v) for v in jets[2:7]],
        "deflated_S_exact": str(jet_s), "D_at_a_exact": str(d_from_coefficients),
        "paired_root_inequality_gap_exact": str(gap),
        "critical_second_over_h2_exact": str(second/h2),
        "critical_third_over_h2_exact": str(third/h2),
        "scalar_floor_screen": floor_status,
        "heat_series_and_root_sum_checks": "passed",
        "theta_identity_assigned": False,
        "collision_excluded": False,
    }


def quartic_finite_transfer():
    rho, delta, h2 = F(1, 8), F(1, 256), F(8)
    b2, b3, b4, b5, b6 = h2/2, F(27), F(24), F(0), F(0)
    assert b3*rho+b4*delta <= h2/2
    assert b3*delta < b2*rho
    c = F(6)  # Own-source mirror S=1/2 and h3/h2=3.
    k = (b6+3*b3*b5/b2+3*b3*b3*b4/b2**2+b3**4/b2**3)/h2
    assert delta <= 3*c/(2*k)
    # Exact critical value: P(T+s,sqrt(1+6s))/8 = -s-3s^2.
    exact_pair = -6*delta*delta
    paid_upper = -c*delta*delta+k*delta**3/3
    target = -c*delta*delta/2
    assert exact_pair <= paid_upper <= target < 0
    return {
        "source": "a=1 quartic, own derivative bounds; theta height bound not used",
        "T": "1/4", "rho": str(rho), "delta": str(delta),
        "B3_B4_B5_B6": [str(v) for v in (b3,b4,b5,b6)],
        "b2": str(b2), "C": str(c), "K": str(k),
        "curvature_radius_3C_over_2K": str(3*c/(2*k)),
        "exact_pair_at_delta": str(exact_pair),
        "paid_pair_upper_at_delta": str(paid_upper),
        "target_upper_at_delta": str(target),
        "all_scale_transfer_at_0<s<=delta": "passed",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--result-note", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    pi = pi_bounds()
    assert pi[1] < F(22, 7)
    # Uniform a>=20 improvement follows analytically from monotonicity.
    x = F(147, 88)  # 21/(4*(22/7))
    assert 20*2*(x-1)/(x+1) > 8
    tables = [coefficient_bounds(a, pi) for a in (20, 100, 1000, 10000)]
    floor20 = tables[0][1]
    controls = [
        polynomial_control("quartic_a1", 1, [(1,2)], 1),
        polynomial_control("quartic_a20", 20, [(20,2)], 1, floor20),
        polynomial_control("negative_quartic_a20", 20, [(20,2)], -1, floor20),
        polynomial_control("degree8_extra_pairs", 20, [(20,2),(21,1),(22,1)], 1, floor20),
    ]
    assert controls[1]["scalar_floor_screen"] == "fails scalar D floor"
    assert controls[2]["scalar_floor_screen"] == "fails scalar D floor"
    assert controls[3]["scalar_floor_screen"] == "passes scalar D floor"
    paths = [
        ROUTE / "notes/02_IMAGINARY_AXIS_CONTRACT_20261019.md",
        BASE / "threshold_routes/01_local_double_winding/notes/03_PAIRED_FACE_REMAINDER_OBSTRUCTION_20261019.md",
        Path("papers/quasi-rh/quasi-rh-exponent-descent/newman_collisions/newman_collision_reductions.tex"),
    ]
    if args.result_note:
        paths.append(args.result_note)
    hashes = {str(path): hashlib.sha256((args.repo/path).read_bytes()).hexdigest() for path in paths}
    hashes[str(ROUTE / "numerics/check_imaginary_axis_bound.py")] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    record = {
        "status": "exact controls and outward coefficient enclosures passed",
        "prepared_for": "Edward Baker", "llm_assistance": "substantial",
        "model": "gpt-6-astra", "reasoning_effort": "max",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "git_parent": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=args.repo, text=True).strip(),
        "source_sha256": hashes,
        "arithmetic": "fractions.Fraction; no floating sign decisions",
        "pi_method": "16 atan(1/5)-4 atan(1/239), alternating remainder, then outward 40-place rationals",
        "atan_terms_each": ATAN_TERMS, "log_terms_each": LOG_TERMS,
        "log_method": "power-of-two reduction and 2*atanh series with geometric remainder",
        "pi_outward": show_interval(pi, 40),
        "table": [t[2] for t in tables], "polynomial_controls": controls,
        "finite_transfer_control": quartic_finite_transfer(),
        "theta_jet_acquisition": "not performed",
        "theta_event_location": "not supplied",
        "theta_exclusion_margin": None,
        "winding_certificate": None,
        "independent_review": False,
    }
    rendered = json.dumps(record, indent=2)+"\n"
    if args.output:
        args.output.write_text(rendered)
        print(json.dumps({"status": record["status"], "output": str(args.output),
                          "bytes": len(rendered.encode()), "table": record["table"]}, indent=2))
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
