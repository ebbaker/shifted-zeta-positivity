#!/usr/bin/env python3
"""Small structural memory replay; floating point, not a theta certificate."""
import json
import math


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def add(a, b):
    return [x + y for x, y in zip(a, b)]


def scale(c, a):
    return [c * x for x in a]


def theta(u):
    r = abs(u)
    return sum((2 * math.pi**2 * n**4 * math.exp(9*r)
                - 3 * math.pi * n**2 * math.exp(5*r))
               * math.exp(-math.pi * n*n * math.exp(4*r))
               for n in range(1, 9))


U, xstar, size = 2.0, 1.25, 25
nodes = [-U + 2*U*i/(size-1) for i in range(size)]
weights = [2*U/(size-1)] * size
weights[0] /= 2
weights[-1] /= 2
roots = [math.sqrt(w) for w in weights]
rows = [[roots[k] * u**j * math.cos(xstar*u+j*math.pi/2)
         for k, u in enumerate(nodes)] for j in range(5)]
basis = []
for row in rows:
    q = row[:]
    # Reorthogonalize to make the algebra check insensitive to conditioning.
    for _ in range(2):
        for e in basis:
            q = add(q, scale(-dot(q, e), e))
    qnorm = math.sqrt(dot(q, q))
    assert qnorm > 1e-6
    basis.append(scale(1/qnorm, q))


def P(v):
    out = [0.0] * size
    for e in basis:
        out = add(out, scale(dot(e, v), e))
    return out


def R(v):
    return add(v, scale(-1, P(v)))


def L(v):
    return [u*u*z for u, z in zip(nodes, v)]


def D(v):
    return R(L(R(v)))


def expD(t, v):
    out, term = v[:], v[:]
    for n in range(1, 25):
        term = scale(t/n, D(term))
        out = add(out, term)
    return out


f0 = [root * theta(u) for root, u in zip(roots, nodes)]
b0 = R(f0)
t = 0.12
ft = [math.exp(t*u*u) * v for u, v in zip(nodes, f0)]
at = P(ft)
direct = P(L(ft))
rhs = add(P(L(at)), P(L(expD(t, b0))))
panels = 128
integral = [0.0] * size
for i in range(panels+1):
    s = t*i/panels
    fs = [math.exp(s*u*u)*v for u, v in zip(nodes, f0)]
    cs = R(L(P(fs)))
    term = P(L(expD(t-s, cs)))
    coefficient = 1 if i in (0, panels) else (4 if i % 2 else 2)
    integral = add(integral, scale(coefficient*t/(3*panels), term))
rhs = add(rhs, integral)
residual = max(abs(a-b) for a, b in zip(direct, rhs))
assert residual < 2e-10, residual

hidden_first_rows = [math.sqrt(dot(R(L(r)), R(L(r)))) for r in rows[:3]]
assert max(hidden_first_rows) < 2e-12
closure_defect = math.sqrt(dot(R(L(rows[4])), R(L(rows[4]))))
assert closure_defect > 1e-4
memory_forms = []
for k in range(6):
    v = P([math.sin((k+1)*u)+math.cos((k+2)*u) for u in nodes])
    cv = R(L(v))
    form = dot(cv, expD(t, cv))
    square = dot(expD(t/2, cv), expD(t/2, cv))
    assert form >= -1e-12
    assert abs(form-square) < 2e-11
    memory_forms.append(form)

print(json.dumps({
    "status": "PASS",
    "scope": "finite quadrature structural replay, floating point; not a certified theta inequality",
    "nodes": size, "U": U, "height": xstar, "time": t,
    "memory_equation_max_residual": residual,
    "first_three_hidden_row_norms": hidden_first_rows,
    "fourth_derivative_closure_defect": closure_defect,
    "memory_quadratic_forms": memory_forms,
}, indent=2))
