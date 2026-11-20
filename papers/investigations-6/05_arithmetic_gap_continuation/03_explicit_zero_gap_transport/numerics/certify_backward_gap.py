"""Transport the first theta gap from t=1000 to t=999 using anchor moments.

20 November 2026. For Edward Baker with OpenAI Codex assistance,
recorded gpt-6.2-astra/max. Run with Python 3 and python-flint 0.9.0.
"""
from hashlib import sha256
import importlib.util
import json
from math import comb, factorial
from pathlib import Path

import flint
from flint import arb, ctx

SIBLING = Path(__file__).resolve().parents[2] / "01_jacobi_integer_hierarchy" / "numerics"
CELLS = 16


def require(condition, message):
    if not condition:
        raise ArithmeticError(message)


def pinned(name, digest):
    path = SIBLING / name
    require(sha256(path.read_bytes()).hexdigest() == digest, "changed input: " + name)
    return path


def anchor_inputs():
    path = pinned("check_large_time_resummation.py",
                  "24a95d13a7d7d178f9d14eb591b3c909af27552552595d8d37bb276955e447a8")
    spec = importlib.util.spec_from_file_location("founding_theta_source", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    receipt = pinned("08_LARGE_TIME_LOOP_RESUMMATION_20261120.json",
                     "52c5c2818ff4958ea654499557282098bb41569d81dddbab102fde73f03d7a4f")
    rows = json.loads(receipt.read_text())["examples"]
    require([row["k"] for row in rows] == [1, 2], "anchor indices")
    return module.ThetaAt1000(), [arb(row["root_bracket_ball"]) for row in rows]


class AnchorTilt:
    def __init__(self, source):
        self.b = arb(671) / 500
        b = self.b
        # Degrees through 28 fit the verified envelope (u+2)^7 exp(16(u+2)).
        moments = [arb(1)] + [source.expect(lambda u: (u - b)**n) for n in range(1, 29)]

        def mixed(j, m):
            # U^2-b^2 = (U-b)(2b+U-b).
            return sum(comb(m, h) * (2 * b)**(m - h) * moments[j + m + h]
                       for h in range(m + 1))

        self.rows = [[(-1)**m * mixed(j, m) / factorial(m) for m in range(4)]
                     for j in range(7)]
        self.errors = []
        for j in range(7):
            square = mixed(2 * j, 8)
            require(square > 0, "squared Taylor remainder")
            self.errors.append((b * b).exp() * square.sqrt() / 24)

    def at(self, s):
        raw = []
        for coefficients, error in zip(self.rows, self.errors):
            poly = arb(0)
            for coefficient in reversed(coefficients):
                poly = poly * s + coefficient
            raw.append(poly + arb(0, (s**4 * error).abs_upper()))
        require(raw[0] > 0, "tilted mass")
        return [arb(1)] + [z / raw[0] for z in raw[1:]]


def drift_bounds(moments, b):
    X = arb(4)
    mu = b + moments[1]
    variance = moments[2] - moments[1]**2
    require(variance > 0, "source variance")

    def difference_moment(p):
        return sum((-1)**i * comb(p, i) * moments[i]
                   * (b * moments[p - i] + moments[p - i + 1])
                   for i in range(p + 1)) / mu

    w, fourth = difference_moment(2), difference_moment(4)
    floor = 1 - X**2 * w / 2
    low = w - X**2 * fourth / 2
    require(floor > 0 and low > 0 and fourth > 0, "positive current and signed curvature")
    high = w / floor + (X * w / floor)**2
    phase_error = X**2 * variance / 2
    require(phase_error < 1 and mu * X - phase_error.asin() > 3 * arb.pi() / 2,
            "counted first two positive phase levels")
    return low, high, floor, mu, phase_error.asin()


def matched_root(k, b, moments):
    q = (2 * k - 1) * arb.pi() / 2
    mu = b + moments[1]
    center = (q / mu).mid()
    left, right = (center - arb("0.04")).lower(), (center + arb("0.04")).upper()
    require(left > 0 and right < 4 and abs(mu * left - q) < 1 and abs(mu * right - q) < 1,
            "marked endpoint bracket")

    def value(x):
        partial = sum(moments[j] * x**j * (x * b + j * arb.pi() / 2).cos() / factorial(j)
                      for j in range(6))
        return (-1)**(k - 1) * (partial + arb(0, (x**6 * moments[6] / 720).abs_upper()))

    require(value(left) > 0 and value(right) < 0, "matched endpoint signs")
    # Keep only certified outer ends when the midpoint sign is inconclusive.
    a, z = left, right
    for _ in range(64):
        mid = ((a + z) / 2).mid()
        if value(mid) > 0:
            a = mid
        else:
            z = mid
    lower = a
    a, z = left, right
    for _ in range(64):
        mid = ((a + z) / 2).mid()
        if value(mid) < 0:
            z = mid
        else:
            a = mid
    return lower.union(z)


def full_endpoint_root(k, source, b, mu):
    q = (2 * k - 1) * arb.pi() / 2
    x = (q / mu).mid()

    def field(point, derivative=False):
        def test(u):
            tilt = (b**2 - u**2).exp()
            return -u * tilt * (point * u).sin() if derivative else tilt * (point * u).cos()
        return source.expect(test)

    for _ in range(4):
        slope = field(x, True)
        require(not slope.contains(0), "endpoint Newton slope")
        x = (x - field(x) / slope).mid()
    left, right = (x - arb("1e-41")).lower(), (x + arb("1e-41")).upper()
    require(field(left) * field(right) < 0 and abs(mu * x - q) < arb(1) / 2
            and 0 < left and right < 4, "direct endpoint bracket or index")
    return left.union(right)


def endpoints(ball):
    return {"lower": ball.lower().str(25), "upper": ball.upper().str(25)}


def main():
    ctx.prec = 224
    source, anchors = anchor_inputs()
    tilt = AnchorTilt(source)
    g0 = anchors[1] - anchors[0]
    D0 = (g0 / 2)**2
    log_growth_lower, log_growth_upper = arb(0), arb(0)
    floors, rates_low, rates_high = [], [], []
    for cell in range(CELLS):
        s = (arb(cell) / CELLS).union(arb(cell + 1) / CELLS)
        low, high, floor, _, _ = drift_bounds(tilt.at(s), tilt.b)
        log_growth_lower += low.lower() / CELLS
        log_growth_upper += high.upper() / CELLS
        floors.append(floor.lower())
        rates_low.append(low.lower())
        rates_high.append(high.upper())

    moments = tilt.at(arb(1))
    _, _, _, mu, _ = drift_bounds(moments, tilt.b)
    lower = (D0 * (2 * log_growth_lower).exp()).lower()
    upper = (D0 * (2 * log_growth_upper).exp()).upper()
    matched = [matched_root(k, tilt.b, moments) for k in (1, 2)]
    full = [full_endpoint_root(k, source, tilt.b, mu) for k in (1, 2)]
    D_matched = ((matched[1] - matched[0]) / 2)**2
    D_full = ((full[1] - full[0]) / 2)**2
    require(lower > D0 and lower < D_full and D_full < upper, "transport versus direct endpoint")
    require(D_matched.contains(D_full), "matched bracket versus direct endpoint")
    return {
        "date": "2026-11-20", "prepared_for": "Edward Baker",
        "assistance": "OpenAI Codex, recorded gpt-6.2-astra/max",
        "time": [999, 1000], "positive_zero_indices": [1, 2], "spatial_cap": 4,
        "precision_bits": ctx.prec, "python_flint": flint.__version__, "time_cells": CELLS,
        "anchor_center": "671/500", "anchor_polynomial_moments_through": 28,
        "current_floor_lower": min(floors).str(19), "minus_log_gap_drift_lower": min(rates_low).str(19),
        "minus_log_gap_drift_upper": max(rates_high).str(19), "anchor_D": D0.str(30),
        "transport_D_lower": lower.str(25), "transport_D_upper": upper.str(25),
        "transport_width": (upper - lower).str(14),
        "matched_endpoint_D": endpoints(D_matched), "matched_width": (2 * D_matched.rad()).str(14),
        "full_endpoint_D": D_full.str(36), "scope": "One anchor, one counted edge and one closed time slab."
    }


if __name__ == "__main__":
    print(json.dumps(main(), indent=2))
