#!/usr/bin/env python3
"""Exact finite parabolic contour controls; Python standard library only.

Prepared for Edward Baker with substantial LLM assistance, 2026-10-20.
Authoring model: gpt-6-astra (Codex), ultra; verified by parent metadata.
No theta estimate or source-acquisition claim.
"""
from fractions import Fraction as Q
from math import comb
from hashlib import sha256
from pathlib import Path
import argparse
import json


def clean(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def add(p, q):
    r = [Q(0)] * max(len(p), len(q))
    for i, c in enumerate(p):
        r[i] += c
    for i, c in enumerate(q):
        r[i] += c
    return clean(r)


def scale(p, c):
    return clean([c*x for x in p])


def mul(p, q):
    r = [Q(0)] * (len(p)+len(q)-1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            r[i+j] += a*b
    return clean(r)


def power(p, n):
    r = [Q(1)]
    for _ in range(n):
        r = mul(r, p)
    return r


def peval(p, x):
    r = Q(0)
    for c in reversed(p):
        r = r*x+c
    return r


def deriv_biv(h, component):
    d = {}
    for (i, j), c in h.items():
        n = (i, j)[component]
        if n:
            ij = (i-1, j) if component == 0 else (i, j-1)
            d[ij] = n*c
    return d


def heat_identity(h):
    d = deriv_biv(h, 0)
    for ij, c in deriv_biv(deriv_biv(h, 1), 1).items():
        d[ij] = d.get(ij, Q(0))+c
    return all(c == 0 for c in d.values())


def on_path(h, time_poly):
    p = [Q(0)]
    for (i, j), c in h.items():
        p = add(p, scale(mul(power(time_poly, i),
                                  [Q(0)]*j+[Q(1)]), c))
    return p


def bernstein(p, a, b):
    """Exact Bernstein coefficients of p(a+(b-a)s), 0<=s<=1."""
    n = len(p)-1
    local = [Q(0)]*(n+1)
    for i, c in enumerate(p):
        for j in range(i+1):
            local[j] += c*comb(i, j)*a**(i-j)*(b-a)**j
    return [sum((local[j]*Q(comb(k, j), comb(n, j))
                 for j in range(k+1)), Q(0)) for k in range(n+1)]


def halfplane_certificate(re, im, a, b):
    for name, p in (("Re", re), ("Im", im)):
        bs = bernstein(p, a, b)
        if min(bs) > 0:
            return name, 1, min(bs)
        if max(bs) < 0:
            return name, -1, -max(bs)
    return None


class Refusal(Exception):
    pass


def certify_arc(re, im, a, b, arc, depth=0):
    for x in (a, b):
        if peval(re, x) == peval(im, x) == 0:
            raise Refusal("physical jet vanishes on boundary endpoint")
    hp = halfplane_certificate(re, im, a, b)
    if hp is not None:
        axis, sign, margin = hp
        return [{
            "arc": arc, "from": str(a), "to": str(b),
            "halfplane": axis, "sign": sign, "margin": str(margin),
            "p": [str(peval(re, a)), str(peval(im, a))],
            "q": [str(peval(re, b)), str(peval(im, b))],
        }]
    if depth >= 24:
        raise Refusal("whole-cell strict half-plane proof unavailable")
    m = (a+b)/2
    return (certify_arc(re, im, a, m, arc, depth+1)
            + certify_arc(re, im, m, b, arc, depth+1))


def winding(cells):
    """SL(2,Q) shear avoids all cut vertices; signed rational ray count."""
    verts = [tuple(map(Q, c["p"])) for c in cells]
    for c, nxt in zip(cells, cells[1:]+cells[:1]):
        assert c["q"] == nxt["p"], "boundary partition is not closed"
    candidates = [0]
    for k in range(1, len(verts)+2):
        candidates += [k, -k]
    shear = next(k for k in candidates
                 if all(y-k*x != 0 for x, y in verts))
    value, crossings = 0, []
    for i, cell in enumerate(cells):
        ax, ay = map(Q, cell["p"])
        bx, by = map(Q, cell["q"])
        ay -= shear*ax
        by -= shear*bx
        if ay*by < 0:
            intercept = (ax*by-bx*ay)/(by-ay)
            assert intercept != 0, "certified chord cannot contain origin"
            if intercept > 0:
                inc = 1 if by > ay else -1
                value += inc
                crossings.append({"cell": i, "sign": inc,
                                  "ray_coordinate": str(intercept)})
    return value, shear, crossings


def make_case(name, h, k, e, B, expected, bottom=None,
              apex_radius_l1=None, apex_error=None):
    assert heat_identity(h)
    R = B*B/k-e
    hx = deriv_biv(h, 1)
    if bottom is not None:
        h2 = deriv_biv(hx, 1).get((0, 0), Q(0))
        if h2 == 0:
            raise Refusal("h2=0; ordinary-double quotient contract fails")
    paths = [("cap", [R], -B, B)]
    if bottom is None:
        paths += [("parabola", [-e, Q(0), 1/k], B, -B)]
    else:
        assert e == 0
        eta = bottom*bottom/k
        paths += [("right_arm", [Q(0), Q(0), 1/k], B, bottom),
                  ("apex_chord", [eta], bottom, -bottom),
                  ("left_arm", [Q(0), Q(0), 1/k], -bottom, -B)]
    cells = []
    for label, time_poly, a, b in paths:
        re, im = on_path(h, time_poly), on_path(hx, time_poly)
        cells += certify_arc(re, im, a, b, label)
    degree, shear, crossings = winding(cells)
    assert degree == expected, (name, degree, expected)
    result = {
        "case": name, "k": str(k), "epsilon_squared": str(e),
        "cap_halfwidth": str(B), "R": str(R),
        "heat_identity_exact": True,
        "boundary_cell_count": len(cells),
        "physical_jet_boundary_modulus_lower_bound": str(
            min(Q(c["margin"]) for c in cells)),
        "winding": degree, "expected_winding": expected,
        "ray_shear": shear, "ray_crossings": crossings,
        "cells": cells,
    }
    if bottom is not None:
        assert apex_error is not None and apex_error < 1
        result.update({
            "target": "regularized forward field J/L",
            "bottom_halfwidth": str(bottom), "eta": str(eta),
            "apex_radius_l1_bound": str(apex_radius_l1),
            "apex_relative_error_upper_bound": str(apex_error),
            "apex_real_part_lower_bound": str(1-apex_error),
            "reference_degree_on_truncated_domain": 0,
            "regularized_degree": degree,
        })
    else:
        result["target"] = "physical jet J"
    return result


def sign_poly(h, sign):
    return {ij: sign*c for ij, c in h.items()}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path,
                        default=Path(__file__).with_name(
                            "EXPANDING_CONTOUR_CONTROLS_20261020.json"))
    args = parser.parse_args()
    quadratic = {(0, 2): Q(1), (1, 0): Q(-2)}
    fourth = {(0, 4): Q(1), (1, 2): Q(-12), (2, 0): Q(12)}
    # F(t,y)=y^4-12ty^2+12t^2-3, translated t=tau-1/2.
    two_event = {(0, 4): Q(1), (0, 2): Q(6), (1, 2): Q(-12),
                 (2, 0): Q(12), (1, 0): Q(-12)}
    B, e, b = Q(2), Q(1, 4), Q(1, 32)
    cases = []
    for k, label in ((Q(1), "narrow"), (Q(2), "borderline"),
                     (Q(4), "wide")):
        for sign in (1, -1):
            h = sign_poly(quadratic, sign)
            cases.append(make_case(
                f"quadratic_physical_{label}_{sign:+}", h,
                k, e, B, -1))
            # rho<=eta+b on the whole removed apex piece; |J-L|<=rho^2,
            # |L|=2rho. This is an analytic premise checked algebraically.
            radius = b*b/k+b
            cases.append(make_case(
                f"quadratic_regularized_{label}_{sign:+}", h,
                k, Q(0), B, 0, b, radius, radius/2))
    for sign in (1, -1):
        cases.append(make_case(
            f"fourth_physical_{sign:+}", sign_poly(fourth, sign),
            Q(4), e, B, -2))
        cases.append(make_case(
            f"two_event_physical_{sign:+}", sign_poly(two_event, sign),
            Q(2), e, B, -2))
        # At first event, L=-12tau+12iy. On rho<=1,
        # |J-L|<=(42+16rho+rho^2)rho^2<=59rho^2.
        radius = b*b/2+b
        assert radius < Q(1, 16)
        cases.append(make_case(
            f"two_event_regularized_{sign:+}", sign_poly(two_event, sign),
            Q(2), Q(0), B, -1, b, radius, Q(59, 12)*radius))
    rejections = []
    # First event is at the lower vertex when e=0.
    try:
        make_case("physical_apex_touch", quadratic, Q(2), Q(0), B, -1)
    except Refusal as exc:
        rejections.append({"case": "physical_apex_touch", "refused": str(exc)})
    else:
        raise AssertionError("boundary collision accepted")
    # Cap at tau=1 meets the later ordinary double of the translated quartic.
    try:
        make_case("later_collision_on_cap", two_event, Q(2), Q(1), B, -2)
    except Refusal as exc:
        rejections.append({"case": "later_collision_on_cap", "refused": str(exc)})
    else:
        raise AssertionError("cap collision accepted")
    try:
        make_case("fourth_double_quotient", fourth, Q(4), Q(0), B, -1,
                  b, Q(1, 16), Q(1, 2))
    except Refusal as exc:
        rejections.append({"case": "fourth_double_quotient", "refused": str(exc)})
    else:
        raise AssertionError("fourth event accepted by double quotient contract")
    artifact = {
        "date": "2026-10-20", "prepared_for": "Edward Baker",
        "model": "gpt-6-astra (Codex)",
        "effort": "ultra; verified from recorded metadata by parent execution",
        "arithmetic": "Python fractions.Fraction only; no floating values",
        "orientation": "dt wedge dx: cap left-to-right; lower boundary right-to-left",
        "method": "exact Bernstein half-planes, chord homotopy, rational ray count",
        "scope": "finite polynomial controls; not theta or a new sign estimate",
        "script_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "cases": cases, "contract_refusals": rejections,
    }
    args.output.write_text(json.dumps(artifact, indent=2)+"\n")
    print(json.dumps({
        "output": str(args.output), "bytes": args.output.stat().st_size,
        "case_count": len(cases), "rejections": len(rejections),
        "max_cells": max(c["boundary_cell_count"] for c in cases),
        "degrees": {c["case"]: c["winding"] for c in cases},
    }, indent=2))


if __name__ == "__main__":
    main()
