#!/usr/bin/env python3
"""Exact covariance controls for BW12 Note 15.

Prepared for Edward Baker, 21 October 2026, with substantial LLM assistance.
Recorded model: gpt-6-astra (Codex); reasoning effort: ultra.
Generic continuous-law-plus-atom controls, not theta-source certificates.
"""
from fractions import Fraction as Q
import argparse
import hashlib
import json
from pathlib import Path
from ftsr_exact_controls import add, scale, deriv, value, response

def polynomial_l1(p):
    return sum(abs(v) for v in p)


def integrate_unit(p):
    return sum(Q(v, k+1) for k, v in enumerate(p))


def vector_value(v, x, n=0):
    """v[j](x) is the coefficient of z^j in V(x,z)."""
    return [value(deriv(p, n), x) for p in v]


def vector_derivative_bound(v, n):
    return sum(polynomial_l1(deriv(p, n)) for p in v)


def linear_double(v):
    return -4 * (v[0] if v else Q(0))


def bilinear_double(v, w):
    vv = list(v) + [Q(0)] * max(0, 3-len(v))
    ww = list(w) + [Q(0)] * max(0, 3-len(w))
    return vv[1]*ww[1] + 2*(vv[0]*ww[2]+vv[2]*ww[0])


def signed_double(v):
    return linear_double(v) + bilinear_double(v, v)


def covariance_case(v, eta, j):
    """Exact eta atom at 0 plus (1-eta) uniform density on (0,1]."""
    w, h = 1-eta, Q(1, j)
    exact = [eta*value(p, Q(0)) + w*integrate_unit(p) for p in v]
    bar = scale(vector_value(v, Q(0)), eta)
    correction = [Q(0)]
    cell_mass = w*h
    cell_variance = w*h**3/12
    cell_abs_third = w*h**4/32
    for i in range(j):
        center = (Q(i)+Q(1, 2))*h
        bar = add(bar, scale(vector_value(v, center), cell_mass))
        correction = add(correction, scale(vector_value(v, center, 2), cell_variance/2))
    error = add(exact, scale(bar, -1))
    residual = add(error, scale(correction, -1))
    m = vector_derivative_bound(v, 0)
    m2, m3 = vector_derivative_bound(v, 2), vector_derivative_bound(v, 3)
    eps2 = m2*j*cell_variance/2
    eps3 = m3*j*cell_abs_third/6
    # F=z^2, R=1, r=1/2, delta=1 gives Note 11 C_L=6,C_B=4.
    cl, cb = Q(6), Q(4)
    center = signed_double(bar) + linear_double(correction) + 2*bilinear_double(bar, correction)
    radius = (cl+2*cb*m)*eps3 + cb*eps2**2
    actual = signed_double(exact)
    mixed = 2*bilinear_double(bar, correction)
    remainder_identity = linear_double(residual) + 2*bilinear_double(bar, residual) + bilinear_double(error, error)
    assert actual-center == remainder_identity
    assert polynomial_l1(error) <= eps2
    assert polynomial_l1(residual) <= eps3
    assert abs(actual-center) <= radius
    assert j*cell_variance <= w*h*h/4
    assert j*cell_abs_third <= h*j*cell_variance <= w*h**3/4
    assert tuple(response([0, 0, 1], (Q(0), Q(0)), exact)) == (
        linear_double(exact), bilinear_double(exact, exact))
    return {"actual": actual, "center": center, "radius": radius,
            "mixed": mixed, "quadratic": bilinear_double(exact, exact),
            "eps2": eps2, "eps3": eps3, "atom_value": vector_value(v, Q(0))}


def run_covariance():
    counts = {"covariance_coupled_identity_and_bound": 0,
              "nonzero_mixed_quadratic_responses": 0,
              "strict_exact_cell_range_containment": 0,
              "exact_range_slack_constant": 0,
              "dropped_mixed_term_rejected": 0}
    response_signs, quadratic_signs, mixed_signs = set(), set(), set()
    # Nonzero atom contribution; degree-five V gives nonzero beyond-covariance residual.
    for s0 in (-1, 1):
        for s1 in (-1, 1):
            for s2 in (-1, 1):
                v = [scale([1, 1, 0, 0, 1], Q(s0, 20)),
                     scale([2, 0, 1, 1], Q(s1, 30)),
                     scale([1, 1, 0, 1, 0, 1], Q(s2, 20))]
                for eta in (Q(1, 4), Q(2, 5)):
                    for j in (1, 2, 3, 4, 8, 16):
                        r = covariance_case(v, eta, j)
                        counts["covariance_coupled_identity_and_bound"] += 1
                        if r["mixed"]:
                            counts["nonzero_mixed_quadratic_responses"] += 1
                        for value_, target in ((r["actual"], response_signs),
                                                (r["quadratic"], quadratic_signs),
                                                (r["mixed"], mixed_signs)):
                            target.add(1 if value_ > 0 else -1 if value_ < 0 else 0)
                        assert r["eps3"] > 0
                        assert any(r["atom_value"])
    assert {-1, 1}.issubset(response_signs)
    assert {-1, 1}.issubset(quadratic_signs)
    assert {-1, 1}.issubset(mixed_signs)

    examples = []
    # V=x^2*z: G=x^2*y^2, increasing in each coordinate, Q nonzero.
    # V=x^2: G=-2(x^2+y^2), decreasing, signed linear response negative.
    for name, v, g in (
        ("positive_quadratic", [[0], [0, 0, 1], [0]], Q(1, 32)),
        ("negative_linear", [[0, 0, 1], [0], [0]], Q(1))):
        eta, w = Q(1, 4), Q(3, 4)
        for j in (8, 16, 32):
            h = Q(1, j)
            result = covariance_case(v, eta, j)
            lo_m2 = sum(w*h*(i*h)**2 for i in range(j))
            hi_m2 = sum(w*h*((i+1)*h)**2 for i in range(j))
            if name == "positive_quadratic":
                lower, upper = lo_m2**2, hi_m2**2
                assert result["actual"] == w*w/9
                assert result["actual"]-result["center"] == (w*h*h/12)**2
                # An intentionally omitted mixed term violates the proved payment.
                assert abs(result["actual"]-(result["center"]-result["mixed"])) > result["radius"]
                counts["dropped_mixed_term_rejected"] += 1
            else:
                # Atom at x=0 has nonzero atom-continuous G contributions;
                # these are included by total law mass one in this formula.
                lower, upper = -4*hi_m2, -4*lo_m2
                assert result["actual"] == -4*w/3
            # Rectangle X=Y=[1/4,3/4] has lengths 1/2; q0=w.
            c_star = g*w*w*Q(1, 2)*Q(1, 2)/8
            assert h <= Q(1, 8)
            assert result["actual"]-lower >= c_star*h
            assert upper-result["actual"] >= c_star*h
            counts["exact_range_slack_constant"] += 1
            assert 2*result["radius"] < c_star*h
            assert lower < result["center"]-result["radius"]
            assert result["center"]+result["radius"] < upper
            counts["strict_exact_cell_range_containment"] += 1
            if j == 8:
                examples.append({"case": name, "J": j, "eta": str(eta),
                    "actual_response": str(result["actual"]),
                    "covariance_center": str(result["center"]),
                    "covariance_radius": str(result["radius"]),
                    "exact_cell_range_lower": str(lower),
                    "exact_cell_range_upper": str(upper),
                    "proved_slack_floor_c_times_h": str(c_star*h)})
    return counts, examples


def run():
    counts, examples = run_covariance()
    return {
        "status": "all exact covariance controls passed",
        "date": "2026-10-21", "author": "Prepared for Edward Baker",
        "llm_assistance": "Substantial; gpt-6-astra (Codex), effort ultra",
        "checks": counts, "covariance_examples": examples,
        "arithmetic": "Python standard-library fractions.Fraction",
        "scope": "Exact continuous-uniform-law-plus-atom polynomial controls, including both signs, retained mixed quadratic terms, strict exact-range containment, and rejected dropped-mixed-term estimates. Not theta acquisition, a canonical-source certificate, finite-time advantage, or endpoint exclusion.",
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "helper_sha256": hashlib.sha256(Path(__file__).with_name("ftsr_exact_controls.py").read_bytes()).hexdigest(),
    }


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    record = run()
    output = json.dumps(record, indent=2, sort_keys=True) + '\n'
    if args.output:
        args.output.write_text(output)
    print(output, end='')
