#!/usr/bin/env python3
"""Frozen finite algebra support for HMC Notes 19 and 20.

Prepared for Edward Baker, 2026-10-21, with gpt-6-astra / max assistance.
Question: do finite heat models recover the paired velocities, exterior
interaction, moving deflation, root-block constant and covariance signs?
Domain: the exact rational fixtures below and heat degrees 2 through 8.
Arithmetic: Python standard-library Fraction; no tolerance or sampling.
Stopping rule: any failed identity exits nonzero. No adaptive extension.
Exclusions: this does not certify theta roots, infinite tails, the saddle
asymptotic, a shrinkage onset, or a simplicity criterion. Analytic tail
theorems are not premises of these purely finite tests.
"""

import argparse
import datetime
from fractions import Fraction as F
import hashlib
import json
from math import factorial
from pathlib import Path
import platform


def trim(p):
    p = [F(x) for x in p]
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def add(p, q):
    return trim([(p[i] if i < len(p) else 0) +
                 (q[i] if i < len(q) else 0)
                 for i in range(max(len(p), len(q)))])


def scale(p, a):
    return trim([a * x for x in p])


def mul(p, q):
    out = [F(0)] * (len(p) + len(q) - 1)
    for i, x in enumerate(p):
        for j, y in enumerate(q):
            out[i + j] += x * y
    return trim(out)


def derivative(p):
    return trim([i * p[i] for i in range(1, len(p))] or [0])


def value(p, x):
    out = F(0)
    for a in reversed(p):
        out = out * x + a
    return out


def divide_exact(p, q):
    p, q = trim(p), trim(q)
    out = [F(0)] * max(1, len(p) - len(q) + 1)
    while p != [0] and len(p) >= len(q):
        shift = len(p) - len(q)
        coeff = p[-1] / q[-1]
        out[shift] += coeff
        p = add(p, [0] * shift + scale(q, -coeff))
    assert p == [0], ("nonzero polynomial remainder", p)
    return trim(out)


def root_polynomial(roots):
    p = [F(1)]
    for r in roots:
        p = mul(p, [-r, 1])
    return p


def check_slice(roots, pair):
    roots = list(map(F, roots))
    a, b = map(F, pair)
    p = root_polynomial(roots)
    p1, p2 = derivative(p), derivative(derivative(p))
    speeds = {r: value(p2, r) / value(p1, r) for r in roots}
    for r in roots:
        assert speeds[r] == 2 * sum((1 / (r - s) for s in roots if s != r), F(0))
    g, c = b - a, (a + b) / 2
    exterior = [r for r in roots if r not in (a, b)]
    interaction = sum((1 / ((b-r)*(a-r)) for r in exterior), F(0))
    gp, cp = speeds[b] - speeds[a], (speeds[a] + speeds[b]) / 2
    assert gp == 4/g - 2*g*interaction
    assert cp == sum((1/(a-r) + 1/(b-r) for r in exterior), F(0))
    factor = [a*b, -(a+b), F(1)]
    deflated = divide_exact(p, factor)
    factor_t = [speeds[a]*b + speeds[b]*a, -speeds[a]-speeds[b]]
    deflated_t = divide_exact(add(scale(p2, -1), scale(mul(factor_t, deflated), -1)), factor)
    residual = add(mul(factor, add(deflated_t, derivative(derivative(deflated)))),
                   add(scale(mul(derivative(factor), derivative(deflated)), 2),
                       mul(add(factor_t, [2]), deflated)))
    assert residual == [0]
    assert add(factor_t, [2]) == trim([2*cp*c + g*g*interaction, -2*cp])
    for endpoint, mutual in ((a, -2/g), (b, 2/g)):
        assert speeds[endpoint] == mutual + 2*value(derivative(deflated), endpoint)/value(deflated, endpoint)
    return {"roots": list(map(str, roots)), "pair": [str(a), str(b)],
            "gap_velocity": str(gp), "center_velocity": str(cp),
            "exterior_interaction": str(interaction)}


def check_even_block(positives):
    positives = list(map(F, positives))
    roots = sorted(positives + [-r for r in positives])
    speeds = {r: 2*sum((1/(r-s) for s in roots if s != r), F(0)) for r in roots}
    for k in range(1, len(positives)+1):
        actual = sum((2*r*speeds[r] for r in positives[:k]), F(0))
        exterior = sum((r*r/(s*s-r*r) for r in positives[:k] for s in positives[k:]), F(0))
        assert actual == 2*k*(2*k-1) - 8*exterior
    return {"positive_roots": list(map(str, positives)), "all_prefixes": "pass"}


def check_heat_polynomial(m, t):
    p, pt = [F(0)]*(m+1), [F(0)]*(m+1)
    for j in range(m//2+1):
        coeff = F(factorial(m), factorial(j)*factorial(m-2*j)) * (-1)**j
        p[m-2*j] = coeff*t**j
        if j:
            pt[m-2*j] = coeff*j*t**(j-1)
    assert add(pt, derivative(derivative(p))) == [0]
    # Newton's second power sum; odd first coefficient vanishes.
    assert -2*p[m-2] == 2*m*(m-1)*t
    if m % 2 == 0:
        k = m//2
        assert -p[m-2]/t == 2*k*(2*k-1)


def check_atomic_series():
    # x represents alpha^2. cos(alpha)/(sin(alpha)/alpha).
    cosine = [F(1), F(-1, 2), F(1, 24), F(-1, 720)]
    sinc = [F(1), F(-1, 6), F(1, 120), F(-1, 5040)]
    ratio = [F(0)] * 4
    for i in range(4):
        ratio[i] = cosine[i] - sum((sinc[j]*ratio[i-j] for j in range(1, i+1)), F(0))
    assert ratio == [F(1), F(-1, 3), F(-1, 45), F(-2, 945)]
    assert -ratio[1]/2 == F(1, 6)  # S_ext at the double endpoint.
    h = [F(0), F(2), F(-2, 3)]  # alpha^2 = 2t - 2t^2/3 + ...
    time_series = add(scale(h, F(1, 2)), scale(mul(h, h), F(1, 12)))
    assert time_series[:3] == [F(0), F(1), F(0)]
    assert 4*h[2] == -16*F(1, 6)
    # Exact instantaneous gap identity, treating alpha and cot(alpha)
    # as symbolic inputs to rational operations.
    for alpha, cotangent in ((F(1, 3), F(5, 2)), (F(2, 3), F(3, 4))):
        s = 1/(2*alpha*alpha)-cotangent/(2*alpha)
        assert 4/(2*alpha)-2*(2*alpha)*s == 2*cotangent
    return {"S_at_birth": "1/6", "gap_squared_t2_coefficient": "-8/3"}


def check_covariance():
    nodes, weights, center = [F(1), F(2), F(4)], [F(1, 4), F(1, 2), F(1, 4)], F(5, 2)
    ev = lambda values: sum((w*x for w, x in zip(weights, values)), F(0))
    v = [u-center for u in nodes]
    mean, second, third = ev(v), ev([x*x for x in v]), ev([x**3 for x in v])
    cov = ev([u*u*x for u, x in zip(nodes, v)])-ev([u*u for u in nodes])*mean
    assert cov == 2*center*(second-mean*mean)+third-second*mean
    for kappa in (F(8), F(32), F(100)):
        lp = 2*center/kappa
        assert -2/kappa + lp/center == 0
    return {"covariance_decomposition": "pass", "leading_rescaling_cancellation": "pass"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    slices = [check_slice([-1, 1], [-1, 1]),
              check_slice([-1, 0, 1], [-1, 0]),
              check_slice([-7, -4, -2, -1, 1, 2, 4, 7], [1, 2]),
              check_slice([-7, -4, -2, -1, 1, 2, 4, 7], [2, 4])]
    blocks = [check_even_block([1, 2, 4, 7]), check_even_block([F(1, 3), F(2, 3), F(5, 3)])]
    for degree in range(2, 9):
        for t in (F(1, 8), F(1), F(2)):
            check_heat_polynomial(degree, t)
    result = {
        "status": "pass", "date": "2026-10-21", "prepared_for": "Edward Baker",
        "model": "gpt-6-astra", "reasoning_effort": "max",
        "review_scope": "same-assistant finite exact algebra, not independent review",
        "captured_at_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "python": platform.python_version(),
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "arithmetic": "fractions.Fraction; exact equalities",
        "finite_slices": slices, "even_root_blocks": blocks,
        "heat_polynomials": {"degrees": [2, 3, 4, 5, 6, 7, 8], "times": ["1/8", "1", "2"], "status": "pass"},
        "atomic_series": check_atomic_series(), "covariance": check_covariance(),
        "does_not_establish": ["infinite zero tail", "theta root enclosure", "saddle asymptotic", "numerical onset time", "simplicity"]
    }
    rendered = json.dumps(result, indent=2) + "\n"
    if args.output:
        args.output.write_text(rendered)
    print(rendered)


if __name__ == "__main__":
    main()
