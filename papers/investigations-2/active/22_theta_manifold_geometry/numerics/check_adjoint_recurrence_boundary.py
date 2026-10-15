#!/usr/bin/env python3
"""Exact finite checks for the adjoint recurrence experiment.

15 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded model: gpt-6-astra; reasoning effort: ultra.
Standard-library rational algebra only. These checks do not certify a theta
sign, analytic convergence, or a Riemann Hypothesis implication.
"""

from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime, timezone
from fractions import Fraction as Q
import hashlib
import json
from math import comb
from pathlib import Path


COUNTS: Counter[str] = Counter()


def check(name, condition):
    if not condition:
        raise AssertionError(name)
    COUNTS[name] += 1


def clean(values):
    return {n: Q(v) for n, v in values.items() if n >= 1 and v}


def add(a, b, scale=Q(1)):
    return clean({n: a.get(n, 0) + scale * b.get(n, 0) for n in a.keys() | b.keys()})


def step(values):
    """Distribution update; mass going from 1 to 0 is absorbed."""
    result = {}
    for m, value in values.items():
        for n in (m - 1, m + 1):
            if n >= 1:
                result[n] = result.get(n, 0) + value / 2
    return clean(result)


def laplacian(values, zero=Q(0)):
    last = max(values, default=0)
    return clean({n: (zero if n == 1 else values.get(n - 1, 0))
                  - 2 * values.get(n, 0) + values.get(n + 1, 0)
                  for n in range(1, last + 2)})


def moment(values):
    return sum((n * v for n, v in values.items()), Q(0))


def total(values):
    return sum(values.values(), Q(0))


def survival(depth, start):
    """Reflection-principle formula, independent of distribution updates."""
    numerator = 0
    for k in range(1 - start, start + 1):
        if (depth + k) % 2 == 0:
            index = (depth + k) // 2
            if 0 <= index <= depth:
                numerator += comb(depth, index)
    return Q(numerator, 2 ** depth)


def residual(values, depth):
    return sum((survival(depth, n) * v for n, v in values.items()), Q(0))


def current(values, depth):
    result = {}
    moving = values
    for _ in range(depth):
        result = add(result, moving, -Q(1, 2))
        moving = step(moving)
    return result, moving


def green(values, n):
    return sum(((m - n) * v for m, v in values.items() if m > n), Q(0))


def run():
    COUNTS.clear()
    # Dynamic random-walk distributions versus a binomial reflection formula.
    for start in range(1, 13):
        moving = {start: Q(1)}
        for depth in range(25):
            p = Q(comb(depth, depth // 2), 2 ** depth)
            check("reflection_vs_walk", total(moving) == survival(depth, start))
            check("survival_bound", 0 <= survival(depth, start) <= min(1, start * p))
            check("central_binomial_bound", p * p <= Q(2, depth + 1))
            check("walk_first_moment", moment(moving) == start)
            if start > depth:
                check("finite_absorption_support", survival(depth, start) == 1)
            moving = step(moving)

    families = []
    for length in range(1, 10):
        families.extend([
            {length: Q(1)},
            {1: Q(-2), length + 1: Q(3, 7)},
            {k: Q((-1) ** k * (k + length), k + 2) for k in range(1, length + 1)},
        ])
    for values in families:
        for depth in range(1, 21):
            flux, moving = current(values, depth)
            p = Q(comb(depth, depth // 2), 2 ** depth)
            boundary = -flux.get(1, 0)
            check("current_equation", laplacian(flux) == add(values, moving, -1))
            check("summed_current", total(values) == boundary + total(moving))
            check("residual_reflection", total(moving) == residual(values, depth))
            check("boundary_hitting_weights", boundary == total(values) - residual(values, depth))
            check("signed_remainder_bound", abs(total(moving)) <= p * sum(n * abs(v) for n, v in values.items()))
            check("signed_first_moment", moment(moving) == moment(values))

        # Decaying Green inverse: its two lower traces detect the zeroth and first moments.
        g = {n: green(values, n) for n in range(1, max(values) + 1)}
        check("green_equation", laplacian(clean(g), green(values, 0)) == clean(values))
        check("green_trace", green(values, 0) - green(values, 1) == total(values))
        check("weighted_telescope", moment(laplacian(clean(g), green(values, 0))) == green(values, 0))

    # Rational surrogate beta, normalized to total 1/2; not actual theta data.
    beta = {1: Q(1, 3), 2: Q(1, 9), 3: Q(1, 27), 4: Q(1, 54)}
    check("surrogate_normalization", total(beta) == Q(1, 2))
    examples = []
    for values in families:
        for depth in range(1, 17):
            beta_tail = residual(beta, depth)
            boundary = total(values) - residual(values, depth)
            check("positive_beta_residual", beta_tail > 0)
            eta = -boundary / beta_tail
            check("cancelled_boundary", boundary + eta * beta_tail == 0)
            corrected = add(values, beta, -eta)
            check("cancellation_returns_unknown", residual(corrected, depth) == total(values))
            check("normalized_decomposition", boundary + eta * beta_tail + residual(corrected, depth) == total(values))
            if values == {1: Q(1)} and depth in (1, 4, 16):
                examples.append({"depth": depth, "eta": str(eta), "remaining_residual": str(residual(corrected, depth))})

    # Defect identity: polynomial coefficient sequences, finite test observables.
    for degree in range(1, 5):
        def a(n):
            return Q(1) + sum((Q((-1) ** k * n ** k, 2 * k + 1) for k in range(1, degree + 1)), Q(0))
        for size in range(3, 11):
            b = {n: Q(1, 3 ** n) for n in range(1, size + 1)}
            z = 2 * total(b)
            b = {n: v / z for n, v in b.items()}
            f = {n: v * Q((-1) ** n * n, size) for n, v in b.items()}
            eta = moment(f) / moment(b)
            d = {k: a(k - 1) - 2 * a(k) + a(k + 1) for k in range(1, size + 1)}
            dual = {k: green(f, k) - eta * green(b, k) for k in range(size + 2)}
            e = sum(b[n] * a(n) for n in b) - Q(1, 2)
            lhs = sum(f[n] * a(n) for n in f) - total(f)
            check("defect_observation_identity", lhs == eta * e + sum(dual[k] * d[k] for k in d))
            check("dual_zero_trace", dual[0] == 0)
            check("dual_one_trace", dual[1] == -total(f) + eta / 2)
            for k in range(1, size + 1):
                check("dual_equation", dual[k - 1] - 2 * dual[k] + dual[k + 1] == f[k] - eta * b[k])

    # Finite hierarchy ramp + remote spike, and fixed-slope improvement.
    size = 30
    b = {n: Q(1, 4 ** n) for n in range(1, size + 1)}
    z = 2 * total(b)
    b = {n: v / z for n, v in b.items()}
    for cutoff in range(2, 15):
        tail = sum(v for n, v in b.items() if n > cutoff)
        prefix_moment = sum(n * v for n, v in b.items() if n <= cutoff)
        for anchored in (False, True):
            a_values = {0: Q(1)}
            a_values.update({n: (Q(1) if anchored and n <= cutoff else
                                  max(Q(0), 1 - Q(n, cutoff)) if not anchored else Q(0))
                             for n in range(1, size + 2)})
            missing = Q(1, 2) - sum(b[n] * a_values[n] for n in b)
            a_values[size] += missing / b[size]
            check("hierarchy_positive", all(v >= 0 for v in a_values.values()))
            check("hierarchy_normalized", sum(b[n] * a_values[n] for n in b) == Q(1, 2))
            for k in range(1, cutoff):
                check("hierarchy_prefix_recurrence", a_values[k - 1] - 2 * a_values[k] + a_values[k + 1] == 0)
            distance = sum(b[n] * abs(a_values[n] - 1) for n in b)
            bound = 2 * tail if anchored else 2 * tail + 2 * prefix_moment / cutoff
            check("hierarchy_distance_bound", distance <= bound)

    return {"status": "pass", "assertions": sum(COUNTS.values()),
            "checks": dict(sorted(COUNTS.items())), "cancellation_examples": examples}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    record = {"date": "2026-10-15", "prepared_for": "Edward Baker",
              "llm_assistance": "substantial", "model": "gpt-6-astra", "reasoning_effort": "ultra",
              "verified_at_utc": datetime.now(timezone.utc).isoformat(),
              "arithmetic": "fractions.Fraction; no floating-point sign tests",
              "scope": "Finite algebra checks only; beta surrogates are rational test data. Analytic proofs and actual theta weights are in the companion note. No signed endpoint estimate is certified.",
              "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              **run()}
    rendered = json.dumps(record, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(rendered)
    print(rendered, end="")


if __name__ == "__main__":
    main()
