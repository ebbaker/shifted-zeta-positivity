"""Exact rational checks for Note01's Gaussian forcing control.
Prepared for Edward Baker with substantial LLM assistance.
gpt-6-astra (Codex), recorded effort max; 27 October 2026.
This checks finite polynomial algebra, not a theta exclusion theorem.
"""
from fractions import Fraction as F
from pathlib import Path
import json


def clean(p):
    return {k: F(v) for k, v in p.items() if v}


def add(p, q):
    out = dict(p)
    for k, v in q.items():
        out[k] = out.get(k, F(0)) + v
    return clean(out)


def scale(p, a):
    return clean({k: a*v for k, v in p.items()})


def mul(p, q):
    out = {}
    for i, a in p.items():
        for j, b in q.items():
            out[i+j] = out.get(i+j, F(0)) + a*b
    return clean(out)


def derivative_gaussian(p):
    # d/dx [p(x) exp(-x^2)] = [p'(x)-2x p(x)] exp(-x^2).
    dp = {k-1: k*v for k, v in p.items() if k}
    return add(dp, {k+1: -2*v for k, v in p.items()})


def helmholtz(p):
    return add(derivative_gaussian(derivative_gaussian(p)), scale(p, 6))


def integral_ratio(p):
    # Integral p exp(-2x^2) over [0,infinity), divided by I0.
    total = F(0)
    for degree, coefficient in p.items():
        assert degree % 2 == 0
        moment = F(1)
        for j in range(1, degree//2+1):
            moment *= F(2*j-1, 4)
        total += coefficient*moment
    return total


h = {0: F(1)}
y = helmholtz(h)
g = helmholtz(y)
y_lambda = scale(h, -1)
assert y == {0: F(4), 2: F(4)}
assert g == {0: F(24), 4: F(16)}
assert helmholtz(y_lambda) == scale(y, -1)
assert derivative_gaussian(y).get(0, 0) == 0
assert derivative_gaussian(y_lambda).get(0, 0) == 0
assert all(v > 0 for v in y.values()) and all(v > 0 for v in g.values())
positive_norm = integral_ratio(mul(y, y))
forcing_pairing = integral_ratio(mul(g, y_lambda))
assert positive_norm == 27
assert forcing_pairing == -27
assert positive_norm + forcing_pairing == 0
record = {
    "date": "2026-10-27", "timezone": "America/New_York",
    "prepared_for": "Edward Baker", "llm_assistance": "substantial",
    "model": "gpt-6-astra", "effort": "max", "status": "passed",
    "scope": "Exact rational Gaussian-polynomial control algebra; no theta evaluation or global threshold test",
    "lambda": 6, "Y_polynomial": {str(k): str(v) for k, v in y.items()},
    "g_polynomial": {str(k): str(v) for k, v in g.items()},
    "I0": "sqrt(pi)/(2*sqrt(2))",
    "positive_norm_over_I0": str(positive_norm),
    "forcing_pairing_over_I0": str(forcing_pairing),
    "wronskian_sum_over_I0": str(positive_norm+forcing_pairing),
    "review_scope": "same-assistant algebra check, not independent review"
}
output = Path(__file__).with_name("01_FORCED_WRONSKIAN_CONTROL_CHECKS_20261027.json")
output.write_text(json.dumps(record, indent=2)+"\n")
print(json.dumps({"status": record["status"], "positive_norm_over_I0": str(positive_norm), "forcing_pairing_over_I0": str(forcing_pairing), "record": str(output)}))
