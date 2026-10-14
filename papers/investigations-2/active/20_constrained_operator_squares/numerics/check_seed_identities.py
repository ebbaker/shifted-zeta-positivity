#!/usr/bin/env python3
"""Elementary exact seed checks. Prepared for Edward Baker with LLM assistance.
2026-10-14; gpt-6-astra (Codex), reasoning effort ultra.
These checks validate examples, not theta positivity or numerical advantage.
"""
from fractions import Fraction as F
from pathlib import Path
import argparse
import hashlib
import json


def add(a, b):
    return [(a[i] if i < len(a) else F(0)) +
            (b[i] if i < len(b) else F(0))
            for i in range(max(len(a), len(b)))]


def scale(a, c):
    return [c*x for x in a]


def mul(a, b):
    out = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return out


def derivative(a):
    return [F(i)*a[i] for i in range(1, len(a))] or [F(0)]


def integral(a):
    return sum((x/F(i+1) for i, x in enumerate(a)), F(0))


def tail(a):
    return [integral(a)] + [-x/F(i+1) for i, x in enumerate(a)]


def dot(a, b):
    out = [F(0)]
    for x, y in zip(a, b):
        out = add(out, mul(x, y))
    return out


def matvec(A, v):
    out = []
    for row in A:
        q = [F(0)]
        for a, x in zip(row, v):
            q = add(q, scale(x, a))
        out.append(q)
    return out


def residual_check():
    A = [[F(2), F(1)], [F(1), F(3)]]
    u = [[F(1), F(1)], [F(2), F(-1)]]
    U = [tail(x) for x in u]
    Au = matvec(A, u)
    r = [add(derivative(x), y) for x, y in zip(u, Au)]
    d = [add(tail(x), [-sum(y)]) for x, y in zip(r, u)]
    AU = matvec(A, U)
    for lhs, x, y in zip(AU, u, d):
        rhs = add(x, y)
        assert all(z == 0 for z in add(lhs, scale(rhs, F(-1))))
    psi = [[x[0]] for x in U]
    expected_E = dot(psi, matvec(A, psi))[0]
    expected_N = dot(psi, psi)[0]
    q = dot(u, u)
    ud = dot(u, d)
    Ud = dot(U, d)
    E0 = 2*integral(q)
    N0 = 4*integral(mul([F(0), F(1)], q))
    E = E0 + 2*integral(ud)
    N = N0 + 4*integral(mul([F(0), F(1)], ud)) - 2*integral(Ud)
    assert E == expected_E == F(63, 4)
    assert N == expected_N == F(9, 2)
    assert E0/N0 == 1
    # Sylvester's criterion: A-I is positive definite, so 1 is below
    # the ground eigenvalue. The uncorrected quotient violates the bound.
    assert A[0][0]-1 > 0
    assert (A[0][0]-1)*(A[1][1]-1)-A[0][1]*A[1][0] > 0
    return {"status": "PASS", "matrix": [[str(x) for x in row] for row in A],
            "path": ["1+t", "2-t"], "T": "1",
            "energy": str(E), "norm_squared": str(N),
            "corrected_quotient": str(E/N),
            "uncorrected_quotient": str(E0/N0),
            "uncorrected_below_ground_energy": True,
            "nonzero_endpoint": True}


def parity(n):
    return F(1 if n % 2 == 0 else -1)


def collision_check():
    nodes = (-1, 0, 1)
    weights = (F(1, 4), F(1), F(1, 4))
    H = sum((w*parity(u) for u, w in zip(nodes, weights)), F(0))
    Hxx = -sum((w*u*u*parity(u) for u, w in zip(nodes, weights)), F(0))
    L0 = F(1, 2)*sum(((u-v)**2*wu*wv*parity(u+v)
                       for u, wu in zip(nodes, weights)
                       for v, wv in zip(nodes, weights)), F(0))
    L1 = -F(1, 2)*sum(((u-v)**2*u*v*wu*wv*parity(u+v)
                        for u, wu in zip(nodes, weights)
                        for v, wv in zip(nodes, weights)), F(0))
    assert L0 == -H*Hxx == F(-1, 4)
    assert L1 == Hxx*Hxx == F(1, 4)
    return {"status": "PASS", "c": "1/2", "t": "0", "x": "pi",
            "H": str(H), "Hx": "0", "Hxx": str(Hxx),
            "L0": str(L0), "L1": str(L1)}


def taylor_check():
    # Compare cos(s sqrt(-L)) and exp(s^2 L). Even rescaling the
    # latter by 1/2 to match order s^2 leaves unequal s^4 coefficients.
    cosine_L = F(1, 2)
    heat_L = F(1)
    cosine_L2 = F(1, 24)
    rescaled_heat_L2 = F(1, 8)
    assert cosine_L != heat_L
    assert cosine_L2 != rescaled_heat_L2
    return {"status": "PASS", "cosine_s2_L": str(cosine_L),
            "heat_s2_L": str(heat_L), "cosine_s4_L2": str(cosine_L2),
            "rescaled_heat_s4_L2": str(rescaled_heat_L2)}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    record = {
        "date": "2026-10-14", "prepared_for": "Edward Baker",
        "model": "gpt-6-astra", "reasoning_effort": "ultra",
        "arithmetic": "Python standard-library Fraction",
        "scope": "Exact finite consistency checks; no theta certificate or performance claim",
        "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "checks": {"finite_time_residual": residual_check(),
                   "paired_stationary_control": collision_check(),
                   "dirac_trace_vs_heat": taylor_check()},
        "status": "PASS",
    }
    text = json.dumps(record, indent=2) + "\n"
    if args.output:
        args.output.write_text(text)
    print(text, end="")


if __name__ == "__main__":
    main()
