#!/usr/bin/env python3
"""Exact finite heat-polynomial controls for the spacetime jet winding.

Only Python's standard library is used. All sign, root-count, and identity
checks use integers/Fraction; no floating-point sampling enters a check.
This is a finite control calculation, not a theta certificate or a proof
of the all-multiplicity local index theorem.

Prepared for Edward Baker, 15 October 2026, with substantial LLM assistance.
Recorded coordinating model: gpt-6-astra; reasoning effort: ultra.

Run: python3 check_spacetime_topology.py --output /tmp/spacetime_topology_checks.json
"""

import argparse
import datetime
from fractions import Fraction as F
import hashlib
import json
import math
from pathlib import Path


ASSERTIONS = 0


def check(condition, message):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def trim(p):
    p = list(p)
    while p and p[-1] == 0:
        p.pop()
    return p


def poly_eval(p, x):
    value = F(0)
    for coefficient in reversed(p):
        value = value * x + coefficient
    return value


def poly_derivative(p):
    return trim([i * p[i] for i in range(1, len(p))])


def poly_divmod(a, b):
    a, b = trim(a), trim(b)
    if not b:
        raise ZeroDivisionError("zero polynomial divisor")
    quotient = [F(0)] * max(0, len(a) - len(b) + 1)
    while a and len(a) >= len(b):
        shift = len(a) - len(b)
        coefficient = a[-1] / b[-1]
        quotient[shift] += coefficient
        for i, value in enumerate(b):
            a[i + shift] -= coefficient * value
        a = trim(a)
    return trim(quotient), a


def positive_normalize(p):
    """Remove positive scalar factors without changing Sturm signs."""
    p = trim(p)
    if not p:
        return p
    common_denominator = math.lcm(*(value.denominator for value in p))
    integers = [value.numerator * (common_denominator // value.denominator)
                for value in p]
    common_numerator = math.gcd(*(abs(value) for value in integers))
    return [F(value // common_numerator) for value in integers]


def sturm_sequence(p):
    p = positive_normalize(p)
    if not p:
        raise ValueError("identically zero polynomial has no finite root count")
    sequence = [p]
    derivative = positive_normalize(poly_derivative(p))
    if not derivative:
        return sequence
    sequence.append(derivative)
    while True:
        _, remainder = poly_divmod(sequence[-2], sequence[-1])
        if not remainder:
            break
        sequence.append(positive_normalize([-value for value in remainder]))
    return sequence


def sign(value):
    return (value > 0) - (value < 0)


def variations(sequence, x):
    signs = [sign(poly_eval(p, x)) for p in sequence]
    signs = [value for value in signs if value]
    return sum(left != right for left, right in zip(signs, signs[1:]))


def root_count(sequence, left, right):
    if left >= right:
        raise ValueError("root interval must have positive length")
    if poly_eval(sequence[0], left) == 0 or poly_eval(sequence[0], right) == 0:
        raise ValueError("Sturm endpoints must not be roots")
    return variations(sequence, left) - variations(sequence, right)


def total_real_roots(sequence):
    def at_infinity(direction):
        signs = [sign(p[-1]) * direction ** (len(p) - 1) for p in sequence]
        return sum(a != b for a, b in zip(signs, signs[1:]))
    return at_infinity(-1) - at_infinity(1)


def simple_roots(p, sequence):
    # The final nonzero Euclidean remainder is gcd(p,p'); constant means
    # every complex root, hence every real root in the box, is simple.
    return len(p) <= 1 or len(sequence[-1]) == 1


def isolate_simple_roots(p, sequence, left, right):
    """Disjoint rational intervals, each containing exactly one real root."""
    count = root_count(sequence, left, right)
    if count == 0:
        return []
    if count == 1:
        if poly_eval(p, left) * poly_eval(p, right) >= 0:
            raise AssertionError("a simple isolated root must change sign")
        return [(left, right)]
    midpoint = (left + right) / 2
    exponent = 3
    while poly_eval(p, midpoint) == 0:
        midpoint = (left + right) / 2 + (right - left) / (2 ** exponent)
        exponent += 1
    return (isolate_simple_roots(p, sequence, left, midpoint)
            + isolate_simple_roots(p, sequence, midpoint, right))


def clean2(p):
    return {power: F(value) for power, value in p.items() if value}


def add2(*polynomials):
    result = {}
    for p in polynomials:
        for power, value in p.items():
            result[power] = result.get(power, F(0)) + value
    return clean2(result)


def scale2(p, coefficient):
    return clean2({power: value * coefficient for power, value in p.items()})


def derivative2(p, coordinate):
    result = {}
    for power, value in p.items():
        if power[coordinate]:
            new_power = list(power)
            new_power[coordinate] -= 1
            result[tuple(new_power)] = value * power[coordinate]
    return clean2(result)


def multiply_variable(p, coordinate):
    result = {}
    for power, value in p.items():
        new_power = list(power)
        new_power[coordinate] += 1
        result[tuple(new_power)] = value
    return result


def heat_polynomial(m):
    return {(k, m - 2 * k): F(math.factorial(m) * (-1) ** k,
                            math.factorial(k) * math.factorial(m - 2 * k))
            for k in range(m // 2 + 1)}


def restrict(p, coordinate, value):
    """Fix one coordinate; return a univariate polynomial in the other."""
    other = 1 - coordinate
    result = [F(0)] * (1 + max(power[other] for power in p))
    for power, coefficient in p.items():
        result[power[other]] += coefficient * value ** power[coordinate]
    return trim(result)


def rational(value):
    return str(value.numerator) if value.denominator == 1 else str(value)


def crossing_record(p, sequence, left, right):
    intervals = isolate_simple_roots(p, sequence, left, right)
    records = []
    for a, b in intervals:
        left_sign, right_sign = sign(poly_eval(p, a)), sign(poly_eval(p, b))
        check(left_sign * right_sign == -1, "root isolation sign crossing")
        records.append({
            "interval": [rational(a), rational(b)],
            "endpoint_signs": [left_sign, right_sign],
            "sign_Hx_at_root": right_sign,
        })
    return records


def rectangle_check(name, p, m, time_radius, space_radius):
    """Count winding by oriented crossings of the positive imaginary ray.

    The rectangle has orientation dt wedge dx. Its t=+delta edge runs
    from x=-rho to +rho, and t=-delta runs in the reverse direction.
    At H=0 and Hx>0, dH/dx=Hx>0, so the forward-x jet curve crosses
    the positive imaginary ray clockwise, with contribution -1.
    Spatial walls have no H zeros and contribute no crossings. This
    computes the winding from actual root crossings, separately from
    the zero-count-difference expression checked afterwards.
    """
    pt = derivative2(p, 0)
    pxx = derivative2(derivative2(p, 1), 1)
    check(not add2(pt, pxx), name + ": backward heat PDE")
    wall_records = []
    for wall_x in (-space_radius, space_radius):
        wall = restrict(p, 1, wall_x)
        sequence = sturm_sequence(wall)
        endpoint_values = [poly_eval(wall, -time_radius),
                           poly_eval(wall, time_radius)]
        check(all(endpoint_values), name + ": no corner zero")
        roots = root_count(sequence, -time_radius, time_radius)
        check(roots == 0, name + ": no H zero on spatial wall")
        wall_records.append({"x": rational(wall_x), "H_root_count": roots,
                             "endpoint_signs": [sign(v) for v in endpoint_values]})

    slices = []
    for t, expected in ((-time_radius, m % 2), (time_radius, m)):
        slice_p = restrict(p, 0, t)
        sequence = sturm_sequence(slice_p)
        check(simple_roots(slice_p, sequence), name + ": square-free endpoint slice")
        count = root_count(sequence, -space_radius, space_radius)
        check(count == expected, name + ": endpoint Sturm root count")
        total_count = total_real_roots(sequence)
        additional_roots = 2 if name.startswith("asymmetric_") else 0
        check(total_count == expected + additional_roots,
              name + ": total real-root count including roots outside box")
        crossings = crossing_record(slice_p, sequence, -space_radius, space_radius)
        check(len(crossings) == count, name + ": complete root isolation")
        positive = sum(record["sign_Hx_at_root"] == 1 for record in crossings)
        slices.append({"t": rational(t), "real_root_count": count,
                       "total_real_root_count": total_count,
                       "simple_endpoint_slice": True,
                       "positive_imaginary_ray_crossings_forward_x": positive,
                       "roots": crossings})

    winding = (slices[0]["positive_imaginary_ray_crossings_forward_x"]
               - slices[1]["positive_imaginary_ray_crossings_forward_x"])
    count_formula = F(slices[0]["real_root_count"] - slices[1]["real_root_count"], 2)
    check(F(winding) == count_formula, name + ": winding versus zero-count difference")
    check(winding == -(m // 2), name + ": multiplicity winding")
    return {"name": name, "multiplicity_at_origin": m,
            "rectangle": {"time": [rational(-time_radius), rational(time_radius)],
                          "space": [rational(-space_radius), rational(space_radius)],
                          "orientation": "dt wedge dx"},
            "walls": wall_records, "endpoint_slices": slices,
            "boundary_J_nonzero": True,
            "winding_from_oriented_ray_crossings": winding,
            "half_zero_count_difference": rational(count_formula)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--max-degree", type=int, default=16)
    args = parser.parse_args()
    if not 2 <= args.max_degree <= 24:
        parser.error("--max-degree must be between 2 and 24")

    max_degree = args.max_degree
    # This margin contains the Hermite roots in the requested finite range.
    # Root containment is verified by exact counts, not assumed from a bound.
    wall_scale = F(2 * max_degree)
    epsilon = F(1, 1024)
    models = {m: heat_polynomial(m) for m in range(2, max_degree + 3)}
    identities = []
    records = []
    for m in range(2, max_degree + 1):
        p = models[m]
        px = derivative2(p, 1)
        pxx = derivative2(px, 1)
        check(not add2(derivative2(p, 0), pxx), "p_m backward heat PDE")
        hermite = add2(scale2(multiply_variable(pxx, 0), F(2)),
                       scale2(multiply_variable(px, 1), F(-1)),
                       scale2(p, F(m)))
        check(not hermite, "scaled Hermite ODE")
        at_zero_time = restrict(p, 0, F(0))
        check(at_zero_time == [F(0)] * m + [F(1)], "exact spatial multiplicity")
        identities.append({"m": m, "heat_PDE": "p_t+p_xx=0",
                           "Hermite_ODE": "2t p_xx-x p_x+m p=0",
                           "initial_slice": "x^m"})
        asymmetric = add2(p, scale2(models[m + 1], F(1, 3)),
                          scale2(models[m + 2], F(-1, 7)))
        check(restrict(asymmetric, 0, F(0))[:m] == [F(0)] * m,
              "asymmetric model has order at least m")
        check(restrict(asymmetric, 0, F(0))[m] == 1,
              "asymmetric model has exact order m")
        for multiplier, suffix in ((F(1), ""), (F(-1), "_sign_reversed")):
            records.append(rectangle_check(
                "p_%d%s" % (m, suffix), scale2(p, multiplier), m,
                F(1), wall_scale))
            records.append(rectangle_check(
                "asymmetric_%d%s" % (m, suffix), scale2(asymmetric, multiplier), m,
                epsilon ** 2, wall_scale * epsilon))

    # An exact global sign reversal rotates J by pi, hence preserves degree.
    by_name = {record["name"]: record for record in records}
    for m in range(2, max_degree + 1):
        for prefix in ("p_", "asymmetric_"):
            name = prefix + str(m)
            check(by_name[name]["winding_from_oriented_ray_crossings"]
                  == by_name[name + "_sign_reversed"]["winding_from_oriented_ray_crossings"],
                  "sign reversal preserves winding")

    receipt = {
        "status": "PASS",
        "prepared_for": "Edward Baker",
        "llm_assistance": "Substantial; internal research checks",
        "coordinating_model": "gpt-6-astra",
        "reasoning_effort": "ultra",
        "scope": "Finite exact polynomial controls only; no theta integration, RH certificate, or all-multiplicity proof.",
        "arithmetic": "Python standard-library Fraction, exact polynomial division, Sturm sequences, rational root isolation",
        "created_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "degree_range": [2, max_degree], "assertions": ASSERTIONS,
        "rectangle_cases": len(records),
        "asymmetric_model": "p_m+(1/3)p_(m+1)-(1/7)p_(m+2)",
        "asymmetric_epsilon": rational(epsilon),
        "boundary_winding_method": "Oriented positive-imaginary-ray crossings of J=(H,H_x); exact Sturm isolation classifies each crossing; H is nonzero on both spatial walls.",
        "identities": identities, "cases": records,
    }
    output = json.dumps(receipt, indent=2, sort_keys=True) + "\n"
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(output, encoding="utf-8")
    print(json.dumps({"status": "PASS", "assertions": ASSERTIONS,
                      "rectangle_cases": len(records), "output": str(args.output),
                      "bytes": len(output.encode("utf-8"))}, sort_keys=True))


if __name__ == "__main__":
    main()
