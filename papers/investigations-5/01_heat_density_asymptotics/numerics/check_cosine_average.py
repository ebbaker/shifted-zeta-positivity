#!/usr/bin/env python3
"""Floating checks of the opening brainstorm's cosine mean-density formula.

Prepared for Edward Baker with substantial LLM assistance:
gpt-6-astra (Codex), recorded effort max, 2026-10-24.
Uses the Python standard library. This is not a theta error certificate.
"""
import argparse
import json
import math
import platform
from pathlib import Path


def simpson(function, left, right, panels=8192):
    assert panels % 2 == 0
    step = (right - left) / panels
    odd = math.fsum(function(left + j * step) for j in range(1, panels, 2))
    even = math.fsum(function(left + j * step) for j in range(2, panels, 2))
    return step * (function(left) + function(right) + 4 * odd + 2 * even) / 3


def period_mean(eta, y):
    a = math.sinh(y) ** 2 + eta**2
    numerator = 2 * a * (a + 1) + 1 - eta**2 * (2 * a + 1)
    return eta**2 * numerator / (2 * math.pi * (a * (a + 1)) ** 1.5)


def direct_mean(eta, y):
    b = math.sinh(y) ** 2
    def density(x):
        return eta**2 * (math.sin(x)**2 + b) / (
            math.pi * (math.cos(x)**2 + b + eta**2)**2
        )
    return simpson(density, 0, math.pi) / math.pi


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    cases = []
    masses = []
    for eta in (0.1, 0.5, 1.0, 2.3):
        for y in (0.0, 0.3, 1.0, 2.0):
            closed = period_mean(eta, y)
            direct = direct_mean(eta, y)
            error = abs(closed - direct)
            assert error < 1e-10, (eta, y, error)
            cases.append(dict(eta=eta, Y=y, closed_form=closed,
                              direct_quadrature=direct, absolute_error=error))
        mass = simpson(lambda y: period_mean(eta, y), -16, 16)
        error = abs(mass - 1 / math.pi)
        assert error < 1e-8, (eta, mass, error)
        masses.append(dict(eta=eta, transverse_range=[-16, 16],
                           integral=mass, target=1 / math.pi, absolute_error=error))
    record = dict(
        date="2026-10-24", timezone="America/New_York",
        prepared_for="Edward Baker", model="gpt-6-astra",
        reasoning_effort="max", python=platform.python_version(),
        status="floating model checks passed",
        scope="L=1 cosine slice; no theta approximation or interval certificate",
        method="Composite Simpson quadrature, 8192 panels; finite transverse truncation",
        period_average_cases=cases, transverse_mass_cases=masses,
    )
    encoded = json.dumps(record, indent=2) + "\n"
    if args.output:
        args.output.write_text(encoded)
    print(json.dumps(dict(
        status=record["status"], period_cases=len(cases), mass_cases=len(masses),
        max_period_error=max(row["absolute_error"] for row in cases),
        max_mass_error=max(row["absolute_error"] for row in masses),
    )))


if __name__ == "__main__":
    main()
