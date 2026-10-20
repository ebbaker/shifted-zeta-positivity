#!/usr/bin/env python3
"""Exact algebra fixtures; no theta source acquisition or sign certificate."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import argparse
import hashlib
import json


def mul(a, b, n=5):
    out = [F(0)] * n
    for i in range(min(n, len(a))):
        for j in range(min(n - i, len(b))):
            out[i + j] += a[i] * b[j]
    return out


def inv(a, n=5):
    assert a[0]
    out = [1 / a[0]] + [F(0)] * (n - 1)
    for i in range(1, n):
        out[i] = -sum(a[j] * out[i - j]
                      for j in range(1, min(i + 1, len(a)))) / a[0]
    return out


def mobius(a, h):
    wh = [F(0)] + h[:4]
    return mul([a] + wh[1:], inv([F(1)] + [a * q for q in wh[1:]]))


def nested(parameters):
    u, v, c, d, e = parameters
    coeff = [e] + [F(0)] * 4
    for a in (d, c, v, u):
        coeff = mobius(a, coeff)
    return coeff


def formula(parameters):
    u, v, c, d, e = parameters
    s, t = 1 - u * u, 1 - v * v
    return [
        u,
        s * v,
        s * (t * c - u * v * v),
        s * (t * ((1 - c * c) * d - v * c * c)
             - 2 * u * v * t * c + u * u * v**3),
        s * (t * (1 - c * c)
             * ((1 - d * d) * e - c * d * d - 2 * v * (c + u) * d)
             + t * v * v * c**3 + 2 * u * v * v * t * c * c
             - u * t * t * c * c + 3 * u * u * v * v * t * c
             - u**3 * v**4),
    ]


def data(u, v, c, p, eta, radius):
    s, t = 1 - u*u, 1 - v*v
    x = p[0] + 2*eta*s/radius**2*(t*c-u*v*v)
    y = p[1] + 6*eta*s/radius**3*(-t*v*c*c-2*u*v*t*c+u*u*v**3)
    b = 6*eta*s*t*(1-c*c)/radius**3
    z = p[2] + 24*eta*s/radius**4*(
        t*v*v*c**3+2*u*v*v*t*c*c-u*t*t*c*c+3*u*u*v*v*t*c-u**3*v**4)
    e = 24*eta*s*t*(1-c*c)/radius**4
    return x, y, b, z, e


def quadratic(u, v, c, p, eta, radius, kappa):
    x, y, b, z, e = data(u, v, c, p, eta, radius)
    constant = 2*y*y-3*x*z+3*abs(x)*e-18*kappa*x*x
    linear = 4*y*b+6*x*e*v*(c+u)
    square = 2*b*b+3*e*(x*c-abs(x))
    return constant, linear, square


def qvalue(parameters, p, eta, radius, kappa):
    bj = formula(parameters)
    f2 = p[0] + 2*eta*bj[2]/radius**2
    f3 = p[1] + 6*eta*bj[3]/radius**3
    f4 = p[2] + 24*eta*bj[4]/radius**4
    return 2*f3*f3-3*f2*f4-18*kappa*f2*f2


def quadratic_max(j, d):
    if j < 0 and abs(d) <= -2*j:
        return -d*d/(4*j), -d/(2*j)
    point = F(1) if d >= 0 else F(-1)
    return j+abs(d), point


def box_max(intervals, kappa):
    (lo, hi), (l3, u3), (l4, u4) = intervals
    candidates = []
    for a, b, v in ((max(lo, F(0)), hi, l4), (lo, min(hi, F(0)), u4)):
        if a > b:
            continue
        pts = [a, b]
        if kappa > 0:
            vertex = -v/(12*kappa)
            if a <= vertex <= b:
                pts.append(vertex)
        candidates.extend(-18*kappa*x*x-3*v*x for x in pts)
    return 2*max(l3*l3, u3*u3)+max(candidates)


def run():
    values = [F(-1), F(-1, 2), F(0), F(1, 2), F(1)]
    coefficient_count = 0
    for params in product(values, repeat=5):
        assert nested(params) == formula(params)
        coefficient_count += 1

    endpoint_count = 0
    p, eta, radius, kappa = (F(2, 7), F(-3, 11), F(5, 13)), F(7, 5), F(3, 2), F(1, 17)
    for u, v, c, d in product(values, repeat=4):
        x = data(u, v, c, p, eta, radius)[0]
        e = F(-1) if x >= 0 else F(1)
        bound = qvalue((u, v, c, d, e), p, eta, radius, kappa)
        constant, linear, square = quadratic(u, v, c, p, eta, radius, kappa)
        assert bound == constant+linear*d+square*d*d
        for ee in values:
            assert qvalue((u, v, c, d, ee), p, eta, radius, kappa) <= bound
        endpoint_count += 1

    quadratic_count = 0
    for j, d in product([F(-5), F(-1), F(-1, 4), F(0), F(1, 3), F(7)], repeat=2):
        maximum, point = quadratic_max(j, d)
        assert -1 <= point <= 1
        assert maximum == j*point*point+d*point
        for z in [F(k, 16) for k in range(-16, 17)]:
            assert j*z*z+d*z <= maximum
        quadratic_count += 1

    # A concave interior optimum that an endpoint-only algorithm misses.
    maximum, point = quadratic_max(F(-3), F(1))
    assert point == F(1, 6) and maximum == F(1, 12)
    assert maximum > max(F(-3)+F(1), F(-3)-F(1))

    synthetic_count = 0
    for c in [F(k, 20) for k in range(-20, 21)]:
        for ll in (F(1, 100), F(1, 2), F(1), F(2), F(17)):
            cc, dd, jj = quadratic(0, 0, c, (0, 0, 0), F(1), F(1), ll)
            assert dd == 0 and jj == 72*(1-c*c)*(1-abs(c))**2
            maximum, _ = quadratic_max(jj, dd)
            assert cc+maximum == 72*(1-c**4)-72*ll*c*c <= 72
            synthetic_count += 1
    for ll in (F(1, 100), F(1, 2), F(1), F(2), F(17)):
        result = box_max(((F(-2), F(2)), (F(-6), F(6)), (F(-24), F(24))), ll)
        exact = 72+(144-72*ll if ll <= 1 else 72/ll)
        assert result == exact > 72

    # Event feasibility and boundary Möbius functions, as rational identities.
    feasibility_count = 0
    for u, v in product(values, repeat=2):
        p0 = -eta*u
        p1 = -eta*(1-u*u)*v/radius
        assert p0*p0+eta*radius*abs(p1) <= eta*eta
        if abs(u) == 1:
            assert p1 == 0 and formula((u, v, F(1, 3), F(1, 5), F(-1, 7)))[1:] == [0]*4
        if abs(v) == 1:
            assert formula((u, v, F(1, 3), F(1, 5), F(-1, 7)))[1:] == [
                (1-u*u)*(-u)**(j-1)*v**j for j in range(1, 5)]
        feasibility_count += 1
    return {
        "status": "passed exact rational algebra fixtures",
        "classification": "independent finite algebra implementation; not a theta certificate",
        "prepared_for": "Edward Baker",
        "date": "2026-10-20",
        "model": "gpt-6-astra",
        "reasoning_effort": "ultra",
        "checks": {
            "nested_mobius_coefficient_tuples": coefficient_count,
            "endpoint_and_quadratic_reductions": endpoint_count,
            "quadratic_endpoint_vertex_fixtures": quadratic_count,
            "synthetic_closed_form_fixtures": synthetic_count,
            "synthetic_box_comparators": 5,
            "event_feasibility_and_boundary_fixtures": feasibility_count,
            "strict_interior_vertex_fixture": True,
        },
        "synthetic_fixture": {
            "P": "0", "eta": "1", "R": "1", "A": "1",
            "L_domain": "L>0", "U_Schur": "72",
            "U_box_L_le_1": "216-72L", "U_box_L_ge_1": "72+72/L",
            "arithmetic_theta_claim": False,
        },
        "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = run()
    rendered = json.dumps(result, indent=2)+"\n"
    if args.output:
        args.output.write_text(rendered)
    print(rendered)
