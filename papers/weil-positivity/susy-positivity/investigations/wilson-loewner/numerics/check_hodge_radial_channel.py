#!/usr/bin/env python3
"""Finite checks for the free Hodge projection and even spatial channel.

Exact rational/counting checks plus floating diagnostics, not a supersymmetry
proof checker or an arithmetic positivity certificate. Standard library only.
"""
from fractions import Fraction as F
import argparse
import hashlib
import json
import math
from pathlib import Path


def run():
    max_degree = 24
    states = [(a, b) for a in range(max_degree + 1)
              for b in range(max_degree + 1 - a)]
    degrees = []
    for degree in range(max_degree + 1):
        level = [(a, b) for a, b in states if a + b == degree]
        neutral = sum(a == b for a, b in level)
        charge_one = sum(a - b == 1 for a, b in level)
        selected = sum(a - b == 1 and b % 2 == 0 for a, b in level)
        assert len(level) == degree + 1
        assert neutral == int(degree % 2 == 0)
        assert charge_one == int(degree % 2 == 1)
        assert selected == int(degree % 4 == 1)
        degrees.append(dict(degree=degree, energy=str(F(degree, 2)),
                            multiplicity=len(level), neutral=neutral,
                            flavor_one=charge_one, flavor_one_even_b=selected))

    one_particle = []
    for angular_l in range(13):
        energy, r_weight = F(2 * angular_l + 1, 2), F(1, 2)
        gap = energy - r_weight
        assert gap == angular_l
        kept = gap == 0
        assert kept == (angular_l == 0)
        one_particle.append(dict(angular_l=angular_l, spatial_multiplicity=2 * angular_l + 1,
                                 energy=str(energy), hodge_gap=str(gap), retained=kept))

    channels = []
    for u in (0.02, 0.05, 0.1, 0.5, 1.0, 2.0):
        # Half the covariance at aligned and antipodal spatial directions.
        angular = (1 / math.sqrt(2 * (math.cosh(u) - 1))
                   + 1 / math.sqrt(2 * (math.cosh(u) + 1))) / 2
        complete = math.exp(-u / 2) / (-math.expm1(-2 * u))
        retained = math.exp(-u / 2)
        omitted = math.exp(-2.5 * u) / (-math.expm1(-2 * u))
        assert abs(angular / complete - 1) < 2e-12
        assert abs((retained + omitted) / complete - 1) < 1e-14
        assert abs(omitted / complete - math.exp(-2 * u)) < 1e-14
        # This is a channel/trace weight, not a fraction of Hilbert-space norm.
        channels.append(dict(u=u, even_axial_covariance=complete,
                             protected_one_particle=retained, omitted=omitted,
                             omitted_channel_fraction=omitted / complete,
                             u_times_omitted=u * omitted,
                             covariance_relative_error=abs(angular / complete - 1)))

    # Integral-test enclosure of the omitted positive arithmetic contribution.
    # Sum n=1..N of 2/(p+2n+1/2)^2; the analytic remainder is between the
    # integrals starting at N+1 and N. This excludes floating quadrature.
    p, terms = F(2), 256
    partial = sum((F(2) / (p + 2 * n + F(1, 2)) ** 2
                   for n in range(1, terms + 1)), F(0))
    lower = partial + 1 / (p + 2 * terms + F(5, 2))
    upper = partial + 1 / (p + 2 * terms + F(1, 2))
    assert F(1, 4) < lower < upper < F(3, 10)
    return dict(schema=1,
                model="OpenAI GPT-6 (Codex; developer-provided identity)",
                effort="not exposed in this session; not inferred",
                status="PASS: finite algebraic checks and floating diagnostics",
                scope="Free Hodge control only; no physical spatial-to-Mellin dictionary or arithmetic positivity claim",
                source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                one_particle=one_particle, protected_degree_counts=degrees,
                channels=channels,
                arithmetic_positive_derivative_at_p2=dict(
                    terms=terms, lower=float(lower), upper=float(upper),
                    coarse_exact_enclosure="1/4 < sum(n>=1) 2/(2+2*n+1/2)^2 < 3/10",
                    proof="Exact rational partial sum plus monotone integral-test bounds; see note",
                    rational_enclosure_sha256=hashlib.sha256(
                        (str(lower) + '\n' + str(upper)).encode()).hexdigest()))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    result = run()
    payload = json.dumps(result, indent=2, sort_keys=True) + '\n'
    if args.output:
        args.output.write_text(payload)
        print(json.dumps(dict(status="PASS", degree_levels=len(result['protected_degree_counts']),
                              one_particle_levels=len(result['one_particle']),
                              spatial_comparisons=len(result['channels']),
                              derivative_bounds=result['arithmetic_positive_derivative_at_p2'])))
    else:
        print(payload, end='')


if __name__ == '__main__':
    main()
