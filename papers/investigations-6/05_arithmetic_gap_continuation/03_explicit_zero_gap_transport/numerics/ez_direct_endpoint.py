"""Matched endpoint comparator for the first counted theta gap.

20 November 2026. Prepared for Edward Baker with OpenAI Codex assistance.
Execution provenance is recorded in the E03 receipt.
"""

from decimal import Decimal, ROUND_CEILING, ROUND_FLOOR, localcontext

from flint import acb, arb, ctx


def _decimal_bound(value, rounding):
    # Convert an exact dyadic to a decimal with directed rounding.
    mantissa, exponent = map(int, value.man_exp())
    with localcontext() as decimal_context:
        decimal_context.prec = 65
        decimal_context.rounding = rounding
        if exponent >= 0:
            return str(+Decimal(mantissa << exponent))
        return str(Decimal(mantissa) / Decimal(1 << -exponent))


def _bounds(value):
    return {
        "lower": _decimal_bound(value.lower(), ROUND_FLOOR),
        "upper": _decimal_bound(value.upper(), ROUND_CEILING),
    }


def _bisect_sign(value, left, right, positive_side):
    """Return the innermost abscissa with the requested strict sign."""
    for _ in range(ctx.prec):
        middle = ((left + right) / 2).mid()
        if middle == left or middle == right:
            break
        at_middle = value(middle)
        if positive_side:
            if at_middle > 0:
                left = middle
            else:
                right = middle
        elif at_middle < 0:
            right = middle
        else:
            left = middle
    return left if positive_side else right


def direct_endpoint(moments, s, r, roots_hint):
    """Certify the endpoint D from the 28 moments and the counted root tubes.

    `moments` are the anchor expectations of powers of P=U−671/500.
    The caller certifies that `roots_hint` contains the first and second
    positive phase levels at `s`, inside their common chart 0 <= x <= 4.
    """
    moments = tuple(map(arb, moments))
    s, r = arb(s), arb(r)
    if (len(moments) != 29 or not all(m.is_finite() for m in moments)
            or not moments[28] >= 0 or not s >= 0 or not r > 0):
        raise ArithmeticError("invalid anchor moments or endpoint Taylor parameters")
    if len(roots_hint) != 2:
        raise ArithmeticError("the first and second counted root tubes are required")

    b = arb(671) / 500
    x_cap = arb(4)
    cauchy_scale = (s * (b**2 + r**2)).exp() / r**28
    remainder_scale = moments[28] * cauchy_scale
    derivative_scale = r * cauchy_scale * (b * (moments[26] * moments[28]).sqrt() + moments[28])

    def coefficients(x):
        linear = acb(-2 * s * b, x)
        series = [acb(1), linear]
        for degree in range(2, 28):
            series.append((linear * series[-1] - 2 * s * series[-2]) / degree)
        return acb(0, x * b).exp(), series

    def field(x):
        phase, series = coefficients(x)
        polynomial = sum(c * m for c, m in zip(series, moments))
        error = (remainder_scale * (x.abs_upper() * r).exp()).upper()
        return (phase * polynomial).real + arb(0, error)

    def slope(x):
        phase, series = coefficients(x)
        # Taylor degree 26 leaves a remainder of order |P|^27 for F.
        # Multiplying by U=b+P costs at most b E|P|^27 + E[P^28].
        polynomial = sum(series[j] * (b * moments[j] + moments[j + 1])
                         for j in range(27))
        error = (derivative_scale * (x.abs_upper() * r).exp()).upper()
        return -(phase * polynomial).imag + arb(0, error)

    # The allowed padding avoids a sign test exactly on a tube endpoint.
    # A slope check on each padded tube certifies that the resulting sign
    # bracket identifies the root already counted there by the caller.
    initial = [hint + arb(0, "1e-12") for hint in roots_hint]
    if not 0 < initial[0] < initial[1] < x_cap:
        raise ArithmeticError("direct root tubes must be disjoint inside the counted chart")

    roots, signed_limits, sign_brackets = [], [], []
    for k, tube in enumerate(initial, start=1):
        orientation = (-1)**(k - 1)

        def value(x):
            return orientation * field(x)

        left, right = tube.lower(), tube.upper()
        oriented_slope = orientation * slope(tube)
        if not (oriented_slope < 0 and value(left) > 0 and value(right) < 0):
            raise ArithmeticError(f"failed direct endpoint slope or initial signs at root {k}")
        low = _bisect_sign(value, left, right, positive_side=True)
        high = _bisect_sign(value, left, right, positive_side=False)
        at_low, at_high = value(low), value(high)
        if not (low < high and at_low > 0 and at_high < 0):
            raise ArithmeticError(f"failed final direct endpoint signs at root {k}")
        roots.append(low.union(high))
        signed_limits.append((low, high))
        sign_brackets.append({
            "index": k,
            "orientation": orientation,
            "oriented_field_at_lower": _bounds(at_low),
            "oriented_field_at_upper": _bounds(at_high),
            "oriented_slope_on_tube": _bounds(oriented_slope),
        })

    (left_low, left_high), (right_low, right_high) = signed_limits
    gap_low = (right_low - left_high).lower()
    gap_high = (right_high - left_low).upper()
    if not gap_low > 0:
        raise ArithmeticError("direct endpoint gap lower bound failed")
    lower = ((gap_low / 2)**2).lower()
    upper = ((gap_high / 2)**2).upper()
    D = lower.union(upper)
    outward = _bounds(D)
    summary = {
        "root_brackets": [{"lower": _decimal_bound(low, ROUND_FLOOR),
                           "upper": _decimal_bound(high, ROUND_CEILING)}
                          for low, high in signed_limits],
        "sign_brackets": sign_brackets,
        "D_lower": outward["lower"],
        "D_upper": outward["upper"],
        "D_width_upper": _decimal_bound((D.upper() - D.lower()).upper(), ROUND_CEILING),
        "field_remainder_upper_on_chart": _decimal_bound(
            (remainder_scale * (x_cap * r).exp()).upper(), ROUND_CEILING),
    }
    return summary, D, roots
