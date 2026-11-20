"""Direct implicit velocities on the counted AGC-EZ-E03 edge.

20 November 2026. Prepared for Edward Baker with OpenAI Codex assistance.
The execution assignment is recorded in the E03 request.
"""

from math import factorial

from flint import arb


def _projected_velocity(x, moments, b):
    """Enclose Hxx/Hx at an actual root inside x."""
    cosine, sine = [], []
    powers = [x**n / factorial(n) for n in range(11)]
    for p in range(3):
        degree = 9 - p
        c = sum((-1)**(n // 2) * powers[n] * moments[p + n]
                for n in range(0, degree + 1, 2))
        s = sum((-1)**(n // 2) * powers[n] * moments[p + n]
                for n in range(1, degree + 1, 2))
        # The real Taylor remainder is bounded by |P|^10 after weighting.
        radius = (powers[degree + 1] * moments[10]).abs_upper()
        cosine.append(c + arb(0, radius))
        sine.append(s + arb(0, radius))

    c0, c1, c2 = cosine
    s0, s1, s2 = sine
    if not c0 > 0:
        raise ArithmeticError(f"centered cosine C0 has no positive floor ({c0})")

    # H=0 gives cot(bx)=S0/C0 and permits U²-b² in the Hxx integral.
    # Cancel the same trigonometric factor in both parts of the quotient.
    numerator = (2 * b * c1 + c2) * s0 - (2 * b * s1 + s2) * c0
    denominator = (b * c0 + c1) * c0 + (b * s0 + s1) * s0
    if not denominator > 0:
        raise ArithmeticError(f"projected Hx has no positive floor ({denominator})")
    return numerator / denominator, denominator.lower()


def _counted_floor(moments, b, cap):
    mean = b + moments[1]
    variance = moments[2] - moments[1]**2
    if not mean > 0:
        raise ArithmeticError(f"source mean has no positive floor ({mean})")
    w = (2 * b * variance + moments[3] - moments[1] * moments[2]) / mean
    current_floor = 1 - cap**2 * w / 2
    phase_radius = (cap**2 * variance / 2).abs_upper()
    if not current_floor > 0:
        raise ArithmeticError(f"current has no positive floor ({current_floor})")
    if not phase_radius < 1 or not mean * cap - phase_radius.asin() > 3 * arb.pi() / 2:
        raise ArithmeticError(f"phase count misses the second positive level ({phase_radius})")
    return current_floor.lower()


def direct_path(records):
    """Compare velocities for cells (s, x1, x2, d) of the frozen slab.

    Each x tube encloses the corresponding counted first or second root on
    the entire cell. The caller supplies the complete closed-cell cover and
    normalized moments d[p] = E[(U-b)^p] on each cell.
    """
    b, cap = arb(671) / 500, arb(4)
    lower, upper, floors, denominators = [], [], [], []
    first_fail = None
    complete = True
    for cell, (s, x1, x2, moments) in enumerate(records):
        try:
            if not 0 < x1 < x2 < cap:
                raise ArithmeticError(f"root tubes are unordered or outside the phase chart ({x1}, {x2})")
            floor = _counted_floor(moments, b, cap)
            v1, denominator1 = _projected_velocity(x1, moments, b)
            v2, denominator2 = _projected_velocity(x2, moments, b)
            minus_drift = (v1 - v2) / (x2 - x1)
        except ArithmeticError as error:
            first_fail = {"cell": cell, "s": s.str(18), "gate": str(error)}
            complete = False
            break

        lower.append(minus_drift.lower())
        upper.append(minus_drift.upper())
        floors.append(floor)
        denominators.append(min(denominator1, denominator2))
        if first_fail is None and not minus_drift > 0:
            first_fail = {"cell": cell, "s": s.str(18), "gate": "strict physical widening",
                          "minus_log_gap_drift": minus_drift.str(25),
                          "left_velocity": v1.str(25), "right_velocity": v2.str(25)}

    complete = complete and bool(lower)
    return {
        "minus_log_gap_drift_lower": min(lower).str(25) if complete else None,
        "minus_log_gap_drift_upper": max(upper).str(25) if complete else None,
        "strict": complete and first_fail is None,
        "cells_evaluated": len(lower),
        "first_fail": first_fail,
        "counted_current_floor_lower": min(floors).str(25) if complete else None,
        "projected_denominator_lower": min(denominators).str(25) if complete else None,
    }
