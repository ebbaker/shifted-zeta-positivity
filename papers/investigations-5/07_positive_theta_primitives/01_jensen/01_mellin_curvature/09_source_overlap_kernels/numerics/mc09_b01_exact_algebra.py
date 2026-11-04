#!/usr/bin/env python3
"""Exact polynomial checks for MC09-B01; no theta numerical evaluation.

Uses sparse multivariate integer polynomials and Leibniz determinants.
The theorem's analytic and Gram-completion arguments require written review.
Run from any directory; by default print the small JSON record to stdout.
"""
import argparse
import hashlib
import itertools
import json
from datetime import datetime, timezone
from pathlib import Path

NAMES = ("a0", "a1", "a2", "a3", "a4", "beta", "chi", "lam", "x", "y")
ZERO = (0,) * len(NAMES)


def const(n):
    return {ZERO: n} if n else {}


def variable(name):
    powers = list(ZERO)
    powers[NAMES.index(name)] = 1
    return {tuple(powers): 1}


def add(*terms):
    result = {}
    for term in terms:
        for powers, coefficient in term.items():
            result[powers] = result.get(powers, 0) + coefficient
    return {p: c for p, c in result.items() if c}


def scale(term, scalar):
    return {p: scalar * c for p, c in term.items() if scalar * c}


def mul(*terms):
    result = const(1)
    for term in terms:
        next_result = {}
        for a, x in result.items():
            for b, y in term.items():
                powers = tuple(i + j for i, j in zip(a, b))
                next_result[powers] = next_result.get(powers, 0) + x * y
        result = {p: c for p, c in next_result.items() if c}
    return result


def determinant(matrix):
    n = len(matrix)
    result = {}
    for perm in itertools.permutations(range(n)):
        inversions = sum(perm[i] > perm[j] for i in range(n) for j in range(i + 1, n))
        term = mul(*(matrix[i][perm[i]] for i in range(n)))
        result = add(result, scale(term, (-1) ** inversions))
    return result


def format_polynomial(poly):
    terms = []
    for powers, coefficient in sorted(poly.items()):
        factors = [name if exponent == 1 else f"{name}^{exponent}"
                   for name, exponent in zip(NAMES, powers) if exponent]
        terms.append({"coefficient": coefficient, "monomial": "*".join(factors) or "1"})
    return terms


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    a0, a1, a2, a3, a4, beta, chi, lam, x, y = [variable(name) for name in NAMES]
    matrix = [[a0, a1, a2, a3, a4],
              [{}, lam, {}, mul(lam, beta), mul(lam, chi)],
              [{}, {}, lam, {}, {}]]
    expected = [mul(lam, lam, a0),
                mul(lam, lam, add(a3, scale(mul(a1, beta), -1))),
                mul(lam, lam, add(mul(a3, chi), scale(mul(a4, beta), -1)))]
    checks = []
    for start, wanted in enumerate(expected):
        actual = determinant([row[start:start + 3] for row in matrix])
        if actual != wanted:
            raise AssertionError(f"Consecutive minor {start} does not match")
        checks.append({"identity": f"consecutive_minor_{start}",
                       "result": format_polynomial(actual), "passed": True})
    difference = add(x, scale(y, -1))
    lhs = add(mul(x, x), mul(y, y), scale(mul(x, y), -2))
    if lhs != mul(difference, difference):
        raise AssertionError("Two-copy polynomial identity does not match")
    checks.append({"identity": "two_copy_squared_difference", "passed": True})
    script = Path(__file__).resolve()
    note = script.parent.parent / "notes/01_KERNEL_MECHANISM_SELECTION_20261103.md"
    record = {
        "task": "MC09-B01", "request_revision": "plan r1",
        "prepared_for": "Edward Baker", "llm_assistance": True,
        "actual_model": "gpt-6-astra", "actual_reasoning_effort": "max",
        "thread_id": "01a1a43c-e3ab-7f73-9373-d130d40c1068",
        "turn_id": "01a1a447-c6e4-7d40-9b2c-8b5eb421cd46",
        "recorded_at_utc": datetime.now(timezone.utc).isoformat(),
        "arithmetic": "exact sparse multivariate integer polynomials; Python standard library",
        "scope": "Three 3x3 formal minors and the two-copy polynomial factorization only",
        "not_tested": ["theta coefficients", "Gram eigenvalues", "contour quadrature",
                       "analytic existence and endpoint proofs", "any original theta ratio"],
        "script_sha256": hashlib.sha256(script.read_bytes()).hexdigest(),
        "note_sha256": hashlib.sha256(note.read_bytes()).hexdigest() if note.exists() else None,
        "checks": checks, "status": "passed",
        "evidence_limit": "Proof-author algebra support; not separate mathematical review or a theta certificate"
    }
    rendered = json.dumps(record, indent=2) + "\n"
    if args.output:
        args.output.write_text(rendered)
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
