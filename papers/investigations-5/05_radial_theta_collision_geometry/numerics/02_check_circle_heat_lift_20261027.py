"""Exact operator checks for RTC-03 Note03; no numerical theta evaluation.

Prepared for Edward Baker with substantial LLM assistance.
gpt-6-astra (Codex), actual recorded effort max; 27 October 2026.

Polynomial coefficients are rational in x,p,t,lambda, with p'=2p.
After conjugating by exp(t*x*x/4+x/2-p), P becomes delta=d_x+2p*d_p.
Normal-form operator multiplication below checks identities as operators,
not merely on a finite selection of trial functions.
"""

from fractions import Fraction as Q
from math import comb
from pathlib import Path
import json


def clean(a):
    return {k: Q(v) for k, v in a.items() if v}


def const(v):
    return clean({(0, 0, 0, 0): Q(v)})


def var(j):
    k = [0] * 4
    k[j] = 1
    return {tuple(k): Q(1)}


def add(a, b):
    out = dict(a)
    for k, v in b.items():
        out[k] = out.get(k, Q(0)) + v
    return clean(out)


def scale(a, v):
    return clean({k: Q(v) * c for k, c in a.items()})


def sub(a, b):
    return add(a, scale(b, -1))


def mul(a, b):
    out = {}
    for ka, va in a.items():
        for kb, vb in b.items():
            k = tuple(i+j for i, j in zip(ka, kb))
            out[k] = out.get(k, Q(0)) + va*vb
    return clean(out)


def partial(a, j):
    out = {}
    for k, v in a.items():
        if k[j]:
            kk = list(k)
            kk[j] -= 1
            out[tuple(kk)] = v*k[j]
    return clean(out)


def delta(a):
    return add(partial(a, 0), scale(mul(p, partial(a, 1)), 2))


def at_x_zero(a):
    return clean({k: v for k, v in a.items() if k[0] == 0})


def op_clean(a):
    return {j: clean(v) for j, v in a.items() if clean(v)}


def op_add(a, b):
    out = dict(a)
    for j, v in b.items():
        out[j] = add(out.get(j, {}), v)
    return op_clean(out)


def op_scale(a, v):
    return op_clean({j: scale(c, v) for j, c in a.items()})


def op_sub(a, b):
    return op_add(a, op_scale(b, -1))


def compose(a, b):
    # (a_i delta^i)(b_j delta^j), using the full Leibniz rule.
    out = {}
    for i, ai in a.items():
        for j, bj in b.items():
            db = bj
            for k in range(i+1):
                order = i-k+j
                term = scale(mul(ai, db), comb(i, k))
                out[order] = add(out.get(order, {}), term)
                db = delta(db)
    return op_clean(out)


def apply(a, f):
    out = {}
    for j, aj in a.items():
        df = f
        for _ in range(j):
            df = delta(df)
        out = add(out, mul(aj, df))
    return out


def commute(a, b):
    return op_sub(compose(a, b), compose(b, a))


one = const(1)
x, p, t, lam = [var(j) for j in range(4)]
h = add(scale(mul(t, x), Q(1, 2)), const(Q(1, 2)))
f = sub(h, scale(p, 2))
P = {1: one}
D = {1: one, 0: f}
A = op_add(compose(D, D), {0: lam})
u = scale(p, -2)
v = scale(mul(p, p), 4)
g = add(scale(u, 3), v)
source_D = op_sub(D, {0: h})
assert apply(op_add(compose(source_D, source_D), source_D), one) == g
assert apply(P, one) == {}
assert apply(P, u) == scale(u, 2)
assert apply(P, v) == scale(v, 4)
assert apply(P, g) == add(scale(u, 6), scale(v, 4))
S = compose(op_sub(P, {0: const(2)}), op_sub(P, {0: const(4)}))
assert apply(S, g) == {}

C = op_sub(compose({0: sub(t, scale(p, 8))}, D), {0: scale(p, 8)})
assert commute(P, A) == C
assert commute(S, A) == op_sub(
    op_add(compose(P, C), compose(C, P)), op_scale(C, 6)
)
assert partial(h, 2) == partial(scale(mul(x, x), Q(1, 4)), 0)

endpoint = at_x_zero(apply(D, g))
expected_endpoint = add(
    add(scale(mul(mul(p, p), p), -8), scale(mul(p, p), 30)),
    scale(p, -15),
)
assert endpoint == expected_endpoint

# D(PY)=Y''+(2p-h)Y'+delta(2p-h)Y in physical, ungauged form.
boundary_b = at_x_zero(sub(scale(p, 2), h))
boundary_y = at_x_zero(sub(delta(sub(scale(p, 2), h)), lam))
assert boundary_b == sub(scale(p, 2), const(Q(1, 2)))
assert boundary_y == sub(sub(scale(p, 4), lam), scale(t, Q(1, 2)))

# Inversion-prefactor algebra: z'= -2z, b=-1+2z, b'=-4z.
z = p
b = add(const(-1), scale(z, 2))
db = scale(mul(z, partial(b, 1)), -2)
assert add(scale(b, 2), one) == add(const(-1), scale(z, 4))
assert add(add(mul(b, b), b), db) == sub(scale(mul(z, z), 4), scale(z, 6))

# Recheck the independent, inherited Gaussian-polynomial cancellation
# using exact even moments of exp(-2x^2), without modifying its old record.
def gaussian_d(a):
    da = {j-1: Q(j)*v for j, v in a.items() if j}
    for j, v in a.items():
        da[j+1] = da.get(j+1, Q(0)) - 2*v
    return {j: v for j, v in da.items() if v}


def gaussian_a(a):
    out = gaussian_d(gaussian_d(a))
    for j, v in a.items():
        out[j] = out.get(j, Q(0)) + 6*v
    return {j: v for j, v in out.items() if v}


def pmul(a, b):
    out = {}
    for i, u0 in a.items():
        for j, v0 in b.items():
            out[i+j] = out.get(i+j, Q(0)) + u0*v0
    return out


def moment(a):
    total = Q(0)
    for j, v0 in a.items():
        assert j % 2 == 0
        mj = Q(1)
        for k in range(1, j//2+1):
            mj *= Q(2*k-1, 4)
        total += v0*mj
    return total


gy = gaussian_a({0: Q(1)})
gg = gaussian_a(gy)
gyl = {0: Q(-1)}
assert gy == {0: Q(4), 2: Q(4)}
assert gg == {0: Q(24), 4: Q(16)}
assert gaussian_a(gyl) == {j: -v0 for j, v0 in gy.items()}
assert gaussian_d(gy).get(0, Q(0)) == 0
assert gaussian_d(gyl).get(0, Q(0)) == 0
assert moment(pmul(gy, gy)) == 27
assert moment(pmul(gg, gyl)) == -27

record = {
    "date": "2026-10-27", "timezone": "America/New_York",
    "prepared_for": "Edward Baker", "llm_assistance": "substantial",
    "model": "gpt-6-astra", "effort": "max", "status": "passed",
    "scope": "Exact rational normal-form differential-operator algebra and inherited Gaussian control; no theta sampling",
    "variables": "x,p,t,lambda; delta=partial_x+2p partial_p; p=pi*n^2*exp(2x)",
    "verified": {
        "source_polynomial": "4p^2-6p",
        "source_channels": "P U=2U; P V=4V; (P-2)(P-4)G=0",
        "time_compatibility": "partial_t h = partial_x(x^2/4)",
        "commutator": "[P,A]=(t-8p)D-8p on each mode",
        "higher_commutator": "[P^2-6P+8,A]=P C+C P-6C",
        "source_endpoint_derivative": "-8p^3+30p^2-15p",
        "response_boundary_y_coefficient": "4p-lambda-t/2",
        "response_boundary_beta_coefficient": "2p-1/2",
        "inversion_prefactor_coefficients": ["-1+4z", "4z^2-6z"],
        "gaussian_control": {"lambda": 6, "N_over_I0": "27", "C_over_I0": "-27", "sum": "0"}
    },
    "not_computationally_verified": [
        "Infinite-series convergence and all justified limit interchanges: proved in Note03",
        "Large-lattice-index boundary limit and nonzero residual: proved in Note03",
        "Finite invariant transverse-space obstruction: proved in Note03",
        "No collision exclusion, physical-height onset, or numerical certificate is claimed"
    ],
    "review_scope": "same-assistant exact algebra check, not independent review"
}
output = Path(__file__).with_name("02_CIRCLE_HEAT_LIFT_CHECKS_20261027.json")
output.write_text(json.dumps(record, indent=2)+"\n")
print(json.dumps({"status": "passed", "record": str(output), "theta_sampling": False}))
