#!/usr/bin/env python3
"""Certified A17 source integrals: Arb interior quadrature and analytic endpoint tails.

Prepared for Edward Baker, 2026-09-29, with GPT-6 (Codex) assistance.
Exact serving variant/reasoning effort are not exposed. Requires python-flint.
No ordinary floating-point computation is used in any enclosure.
"""
import argparse
import hashlib
import json
import flint
from fractions import Fraction as Q
from pathlib import Path
from flint import acb, arb, ctx

ctx.prec = 192
B = Q(9, 20)
Y_END = Q(255, 256)
V_END = 1 / (1 - Y_END**2)


def ball(q):
    if isinstance(q, Q):
        return arb(q.numerator) / q.denominator
    return arb(q)


def trim(p):
    while len(p) > 1 and not p[-1]:
        p.pop()
    return p


def add(p, q):
    out = [Q(0)] * max(len(p), len(q))
    for i, x in enumerate(p):
        out[i] += x
    for i, x in enumerate(q):
        out[i] += x
    return trim(out)


def scale(p, c):
    return trim([c*x for x in p])


def mul(p, q):
    out = [Q(0)] * (len(p) + len(q) - 1)
    for i, x in enumerate(p):
        for j, y in enumerate(q):
            out[i+j] += x*y
    return trim(out)


def deriv(p):
    return trim([i*p[i] for i in range(1, len(p))] or [Q(0)])


def source_derivative(parity, p):
    """d/dx of exp(-v) y^parity p(v), y=x/b, v=(1-y²)^(-1)."""
    difference = add(deriv(p), scale(p, -1))
    if parity == 0:
        return 1, scale(mul([0, 0, 2], difference), 1/B)
    return 0, scale(add(p, mul([0, -2, 2], difference)), 1/B)


def polyval(p, v):
    result = v*0
    for c in reversed(p):
        result = result*v + ball(c)
    return result


def integrand(parity, p, square):
    def value(y, analytic):
        denominator = 1 - y*y
        if denominator.contains(0):
            return acb("nan")
        v = 1 / denominator
        z = polyval(p, v)
        if parity:
            z *= y
        if square:
            return (-2*v).exp()*z*z
        return (-v).exp()*z
    return value


def integral_core(parity, p, square, end=Y_END):
    # Endpoints are rational/dyadic. The integrand is holomorphic away from ±1.
    breaks = [Q(0), Q(1, 2), Q(3, 4), Q(7, 8), Q(15, 16),
              Q(31, 32), Q(63, 64), Q(127, 128), Y_END]
    breaks = [x for x in breaks if x < end] + [end]
    total = acb(0)
    for a, b in zip(breaks, breaks[1:]):
        piece = acb.integral(
            integrand(parity, p, square), acb(ball(a)), acb(ball(b)),
            rel_tol=arb(2)**-110, abs_tol=arb(2)**-110,
            deg_limit=128, eval_limit=100000, depth_limit=40,
        )
        assert piece.is_finite(), (parity, square, a, b, piece)
        assert piece.imag.contains(0), piece
        total += piece
    assert total.is_finite() and total.imag.contains(0)
    return total.real


def endpoint_tail(p, square):
    """Bounds BOTH endpoint tails in dx, with y^parity discarded above by ≤1."""
    coeffs = [abs(c) for c in p]
    if square:
        coeffs = mul(coeffs, coeffs)
    decay = 2 if square else 1
    v = ball(V_END)
    exponential = (-decay*v).exp()
    moment = exponential / decay
    total = ball(coeffs[0])*moment
    for n in range(1, len(coeffs)):
        moment = exponential*v**n/decay + ball(n)*moment/decay
        total += ball(coeffs[n])*moment
    return ball(B / (Y_END*V_END**2))*total


def norm_square(parity, p):
    interior = 2*ball(B)*integral_core(parity, p, True)
    tail = endpoint_tail(p, True)
    upper = tail.upper()
    total = interior + arb(upper/2, upper/2)  # Adds [0, upper].
    assert total > 0
    return total, tail


def rational_polyval(p, x):
    result = Q(0)
    for c in reversed(p):
        result = result*x + c
    return result


def one_positive_root(p):
    # For the two undifferentiated A17 polynomials, the note proves exactly
    # one root in v≥1 and it lies in (2,3).
    lo, hi = Q(2), Q(3)
    assert rational_polyval(p, lo) > 0 > rational_polyval(p, hi)
    for _ in range(160):
        mid = (lo+hi)/2
        if rational_polyval(p, mid) > 0:
            lo = mid
        else:
            hi = mid
    ylo = (1 - 1/ball(lo)).sqrt().lower()
    yhi = (1 - 1/ball(hi)).sqrt().upper()
    return Q(str(ylo.fmpq())), Q(str(yhi.fmpq())), lo, hi


def l1_norm(parity, p):
    ylo, yhi, vlo, vhi = one_positive_root(p)
    positive = integral_core(parity, p, False, ylo)
    total_signed = integral_core(parity, p, False)
    # Correct the integration split from ylo to the true root.
    ybox = ball(ylo) + arb(ball((yhi-ylo)/2), ball((yhi-ylo)/2))
    vbox = 1/(1-ybox*ybox)
    qbox = (-vbox).exp()*polyval(p, vbox)
    if parity:
        qbox *= ybox
    split_error = 4*ball(B)*ball(yhi-ylo)*abs(qbox).upper()
    endpoint = endpoint_tail(p, False)
    value = 2*ball(B)*(2*positive-total_signed)
    value += arb(0, split_error.upper()+endpoint.upper())
    assert value > 0
    return value, endpoint, {"v_lower":str(vlo), "v_upper":str(vhi)}


def enclosure(value):
    assert value.is_finite()
    return {
        "ball": value.str(36),
        "rational_lower": str(value.lower().fmpq()),
        "rational_upper": str(value.upper().fmpq()),
    }


def initial_polynomial(source_id):
    if source_id == 0:
        return 0, [Q(1,4), 0, -6/B**2, 12/B**2, -4/B**2]
    if source_id == 1:
        return 1, [B/4, 0, -2/B, 12/B, -4/B]
    raise ValueError("Only the two A17 sources are defined")


def record_ball(data):
    lo = Q(data["rational_lower"])
    hi = Q(data["rational_upper"])
    return arb(ball((lo+hi)/2), ball((hi-lo)/2))


def source_value(source_id, x, derivative_order=0, normalizer=None):
    """Rigorous real Arb value at a ball wholly inside or outside the support.

    Boundary-straddling balls are rejected; do not silently evaluate them as zero.
    Pass a loaded normalizer to avoid reading the small record repeatedly.
    """
    x = arb(x)
    b = ball(B)
    if abs(x) >= b:
        return arb(0)
    if not abs(x) < b:
        raise ValueError("Input interval meets a support endpoint")
    if normalizer is None:
        record = json.loads((Path(__file__).resolve().parent / "records" / "source_norm_enclosures.json").read_text())
        normalizer = record_ball(record["sources"][source_id]["normalizer"])
    parity, p = initial_polynomial(source_id)
    for _ in range(derivative_order):
        parity, p = source_derivative(parity,p)
    y = x/b
    v = 1/(1-y*y)
    result = (-v).exp()*polyval(p,v)/normalizer
    return y*result if parity else result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path(__file__).resolve().parent / "records" / "source_norm_enclosures.json")
    args = parser.parse_args()
    # p2(y) = 6v²−12v³+4v⁴. Each q is exp(-v)y^parity P(v).
    q0 = [Q(1,4), 0, -6/B**2, 12/B**2, -4/B**2]
    q1 = [B/4, 0, -2/B, 12/B, -4/B]
    rows = []
    for source_id, initial in enumerate([(0,q0),(1,q1)]):
        parity, p = initial
        norms = []
        for order in range(5):
            squared, tail = norm_square(parity, p)
            norms.append(squared)
            rows.append({"source":source_id,"derivative_order":order,
                         "raw_derivative_norm_square":enclosure(squared),
                         "analytic_endpoint_tail_upper":enclosure(tail),
                         "parity":parity,
                         "polynomial_coefficients":[str(c) for c in p]})
            parity, p = source_derivative(parity,p)
        raw_l1, l1_tail, root = l1_norm(*initial)
        normalizer = norms[0].sqrt()
        normalized_l1 = raw_l1/normalizer
        normalized = [x/norms[0] for x in norms]
        r = 1/arb(2).sqrt()
        scale2 = (1+r)**2
        # m(t) ≤ (1/2)log(1+4t²/25); Jensen is proved in the findings.
        gamma_upper_f = (1+arb(4)*normalized[1]/25).log()/2
        gamma_upper_d2f = scale2*gamma_upper_f
        fourier_tails = []
        for cutoff in (1000,10000):
            for order in range(1,5):
                power = 2*order-1
                coefficient = scale2*2*ball(B)*normalized[order]
                bound = coefficient/arb.pi()*arb(cutoff)**(-power)/power*(
                    6+(arb(29)/25).log()/2+arb(cutoff).log()+arb(1)/power)
                fourier_tails.append({"cutoff":cutoff,"derivative_order":order,
                                      "absolute_gamma_D2F_tail_bound":enclosure(bound)})
        source_row = {
            "source":source_id,
            "normalizer":enclosure(normalizer),
            "normalized_L1":enclosure(normalized_l1),
            "normalized_derivative_norm_squares":[enclosure(x) for x in normalized],
            "normalized_derivative_norms":[enclosure(x.sqrt()) for x in normalized],
            "normalized_derivative_L1_cauchy_bounds":[enclosure((2*ball(B)*x).sqrt()) for x in normalized],
            "gamma_upper_bound_F":enclosure(gamma_upper_f),
            "gamma_upper_bound_D2F":enclosure(gamma_upper_d2f),
            "B_infinity_D2F_epsilon_supnorm_coefficient":enclosure(scale2*normalized_l1**2),
            "positive_half_source_root_v_bracket":root,
            "raw_L1_endpoint_tail_bound":enclosure(l1_tail),
            "fourier_tail_bounds":fourier_tails,
        }
        print(json.dumps({"progress":source_id,"normalizer":str(normalizer),
                          "L1":str(normalized_l1),"derivative_L2":[str(x.sqrt()) for x in normalized]}),flush=True)
        if source_id == 0:
            sources = [source_row]
        else:
            sources.append(source_row)
    output = {
        "date":"2026-09-29","model":"GPT-6 (Codex)",
        "serving_variant":"not exposed","reasoning_effort":"not exposed",
        "scope":"Certified source integrals and analytic bounds only; no actual Sonin trace or Weil sign.",
        "arithmetic":"python-flint Arb/Acb at 192 bits; exact rational coefficients; no binary float inputs",
        "python_flint_version":flint.__version__,
        "interior_integration_y_endpoint":str(Y_END),"endpoint_v":str(V_END),
        "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "sources":sources,"raw_integrals":rows,
    }
    offset = arb(4)/5+(arb(5)/4).log()-arb.pi().log()
    gamma_minimum = (arb(1)/4).digamma()-arb.pi().log()
    assert offset < 0 and gamma_minimum > -6
    output["gamma_scalar_checks"] = {
        "upper_bound_discarded_negative_constant":enclosure(offset),
        "gamma_multiplier_minimum":enclosure(gamma_minimum),
    }
    target = args.output
    target.write_text(json.dumps(output,indent=2)+"\n")
    print(str(target),flush=True)


if __name__ == "__main__":
    main()
