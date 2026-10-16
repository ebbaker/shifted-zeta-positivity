#!/usr/bin/env python3
"""Bounded binary64 diagnostic of a complete reciprocal chirp block.

13 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded model: gpt-6-astra (Codex); reasoning effort ultra, inherited from
parent session. This script is NOT interval arithmetic or a certificate.
Requires Python 3 and NumPy. No generated arrays are saved.
"""
from __future__ import annotations

import argparse
import cmath
import hashlib
import json
import math
import platform
from pathlib import Path

import numpy as np
from numpy.polynomial.legendre import leggauss


def physical(n: int, t: float, x: float | None = None) -> dict:
    at_center = x is None
    if at_center:
        x = 4 * math.pi * n * n - t * math.pi / 4
        for _ in range(6):
            ai = 3 * x / (1 + x * x) - math.atan(x) / 2
            u = (7 * x * x - 5) / (1 + x * x) ** 2
            x -= (x - t * ai - 4 * math.pi * n * n) / (1 + t * u / 2)
    ell = math.log(x / (4 * math.pi))
    ar = ell / 2 + math.log1p(x ** -2) / 4 - 1 / (1 + x * x)
    ai = 3 * x / (1 + x * x) - math.atan(x) / 2
    u = (7 * x * x - 5) / (1 + x * x) ** 2
    v = x * (x * x + 5) / (1 + x * x) ** 2
    frequency = 2 * math.pi * n * n if at_center else (x - t * ai) / 2
    p = n * n if at_center else frequency / (2 * math.pi)
    sigma = 0.5 + t * ar / 2
    c = 0.5 + t * u / 4
    d = t * v / 4
    omega = (ar * (1 + t * u / 2) - ai * t * v / 2) / 2
    theta = (-math.pi + math.atan(x) / 4 + x * (1 - ell) / 4
             - x * math.log1p(x ** -2) / 8 + t * ar * ai / 2)
    delta_sigma = sigma - (0.5 + t * math.log(p) / 4)
    delta_sigma_x = d - t * c / (4 * frequency)
    delta_t = -t * ai / 2
    z, w = leggauss(24)
    vv = (z + 1) / 2
    # Stable formula for full Theta + 2*pi; the exponential is unchanged.
    theta_reflection = (math.atan(x) / 2 - math.pi / 4
        - x * math.log1p(x ** -2) / 4 + t * ai * (ar - ell / 2)
        + delta_t ** 2 * np.dot(w / 2, (1 - vv) / (x / 2 + vv * delta_t)))
    theta_reflection_x = -2 * omega + c * math.log(p)
    return dict(n=n, t=t, x=x, ell=ell, frequency=frequency, p=p,
        sigma=sigma, c=c, d=d, omega=omega, theta=theta,
        delta_sigma=delta_sigma, delta_sigma_x=delta_sigma_x,
        theta_reflection=theta_reflection,
        theta_reflection_x=theta_reflection_x,
        center_root_residual=x-t*ai-4*math.pi*n*n,
        kappa_diagnostic=t*ell,
        natural_cutoff=int(math.floor(math.sqrt(x/(4*math.pi)+t/16))))


def amplitude(u, data: dict, exterior: bool, jet: int):
    """Amplitude and two INDEX derivatives, retaining physical first jet."""
    t = data['t']
    sigma = data['sigma'] - (2 * data['delta_sigma'] if exterior else 0)
    factor = math.exp(-data['delta_sigma'] * math.log(data['p'])) if exterior else 1
    ell = np.log(u)
    weight = factor * np.exp(-sigma * ell + t * ell * ell / 4)
    power = -sigma + t * ell / 2
    aa = -1j * data['omega']
    bb = -data['d'] + 1j * data['c']
    if exterior:
        aa += (-data['delta_sigma_x'] * math.log(data['p'])
               - data['delta_sigma'] * data['c'] / data['frequency']
               - 1j * data['theta_reflection_x'])
        bb += 2 * data['delta_sigma_x']
    if jet == 0:
        aa, bb = 1, 0
    multiplier = aa + bb * ell
    return (weight * multiplier,
        weight / u * (power * multiplier + bb),
        weight / u ** 2 * ((power * power - power + t / 2) * multiplier
                           + (2 * power - 1) * bb))


def literal_sum(data: dict, lo: int, hi: int, exterior: bool, jet: int):
    u = np.arange(lo, hi + 1, dtype=float)
    halves = np.ones(len(u))
    halves[[0, -1]] = 0.5
    phase = np.exp(1j * (data['theta'] + data['frequency'] * np.log(u)))
    return np.sum(halves * amplitude(u, data, exterior, jet)[0] * phase)


def block(data: dict, lo: int, hi: int, exterior: bool, jet: int, degree: int):
    n, frequency = data['n'], data['frequency']
    ceiling = 4 * n
    z, w = leggauss(degree)
    panels = (hi - lo) * ceiling
    u = lo + (np.arange(panels)[:, None] + (z + 1)[None, :] / 2) / ceiling
    phase = lambda v: np.exp(1j * (data['theta'] + frequency * np.log(v)))
    # Sum all retained Fourier integrals as the exact Dirichlet kernel.
    # Reduction modulo 1 avoids spurious loss near removable integer values.
    fraction = u - np.rint(u)
    dirichlet = ((2 * ceiling + 1) * np.sinc((2 * ceiling + 1) * fraction)
                 / np.sinc(fraction))
    finite = np.sum(amplitude(u, data, exterior, jet)[0] * phase(u)
                    * dirichlet * w[None, :] / (2 * ceiling))

    def endpoint(v):
        omega = int(data['p'] // v)  # At these exact mathematical centers, integral.
        harmonic2 = lambda m: sum(k ** -2 for k in range(1, m + 1))
        s1 = -sum(1 / k for k in range(ceiling - omega + 1, ceiling + omega + 1))
        s2 = math.pi ** 2 / 3 - harmonic2(ceiling - omega) - harmonic2(ceiling + omega)
        s3 = -sum(1 / k ** 3 for k in range(ceiling - omega + 1, ceiling + omega + 1))
        a, ap, _ = amplitude(float(v), data, exterior, jet)
        return phase(float(v)) * (a * s1 / (2j * math.pi)
            + ap * s2 / (2 * math.pi) ** 2
            + frequency * a * s3 / (v * v * (2 * math.pi) ** 3))

    e_lo, e_hi = endpoint(lo), endpoint(hi)
    total = literal_sum(data, lo, hi, exterior, jet)
    tail = total - finite - e_hi + e_lo
    smooth_u = lo + (z + 1) * (hi - lo) / 2
    a, ap, app = amplitude(smooth_u, data, exterior, jet)
    # This is a FLOATING POINT EVALUATION of an analytic majorant, not an
    # outward enclosure of that majorant or of the residual.
    envelope = 2 / (math.pi ** 2 * ceiling) * np.dot(w * (hi - lo) / 2,
        np.abs(app) + 3 * np.abs(ap) / smooth_u + 5 * np.abs(a) / smooth_u ** 2)
    return dict(sum=total, finite_modes=finite, endpoint_lo=e_lo,
                endpoint_hi=e_hi, tail=tail, absolute_envelope_estimate=envelope)


def comparison(data: dict, degree: int, jet: int):
    n = data['n']
    interior = block(data, n // 2, n, False, jet, degree)
    exterior = block(data, n, 2 * n, True, jet, degree)
    turn = cmath.exp(1j * data['theta_reflection'])
    paired_tail = interior['tail'] - turn * exterior['tail'].conjugate()
    denominator = abs(interior['tail']) + abs(exterior['tail'])
    return dict(jet=jet, quadrature_degree=degree,
        panels_per_unit=4*n, fourier_ceiling=4*n,
        interior=interior, exterior=exterior, paired_tail=paired_tail,
        signed_real_pair=2 * paired_tail.real,
        paired_absolute_envelope_estimate=(interior['absolute_envelope_estimate']
            + exterior['absolute_envelope_estimate']),
        cancellation_ratio=abs(paired_tail)/denominator,
        cancellation_ratio_denominator=denominator,
        shared_endpoint=interior['endpoint_hi'] + turn*exterior['endpoint_lo'].conjugate(),
        complete_reflection_defect=interior['sum'] - turn*exterior['sum'].conjugate())


def encode(item):
    if isinstance(item, (complex, np.complexfloating)):
        return dict(real=float(item.real), imag=float(item.imag))
    if isinstance(item, dict):
        return {k: encode(v) for k, v in item.items()}
    if isinstance(item, (list, tuple)):
        return [encode(v) for v in item]
    if isinstance(item, np.floating):
        return float(item)
    return item


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--record', type=Path, required=True)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[5]
    inputs = [
        'papers/investigations-2/brainstorm/reviews/ACTIVE_DIRECTIONS_REVIEW_CODEX_20261013.md',
        'papers/investigations-2/active/01_complete_cutoff_reflection/notes/INITIAL_RESEARCH_PROGRAM_20261013.md',
        'papers/quasi-rh/quasi-rh-exponent-descent/newman_collisions/notes/22_SIGNED_PAIR_TRANSFORMS_AND_STATIONARY_REFLECTION_20261010.md',
        'papers/quasi-rh/quasi-rh-exponent-descent/newman_collisions/notes/24_CURVATURE_CONES_SHARP_NULL_PAYMENTS_AND_LOCALIZED_POISSON_20261010.md',
        'papers/quasi-rh/quasi-rh-exponent-descent/newman_collisions/09_prime_phase_torus/notes/8_OSCILLATION_PRESERVING_PRODUCT_POISSON_TRANSFORM_20261010.md',
        'papers/quasi-rh/quasi-rh-exponent-descent/newman_collisions/17_enlarged_state_transport/notes/22_THETA_CUTOFF_MATCHING_AND_UNIFORM_PHYSICAL_JETS_20261011.md']
    cases = []
    for n in [8, 12, 16, 32]:
        data = physical(n, 0.05)
        runs = [comparison(data, degree, jet) for jet in [0, 1] for degree in [16, 24]]
        checks = []
        for jet in [0, 1]:
            low, high = runs[2*jet:2*jet+2]
            gap = abs(low['paired_tail']-high['paired_tail'])
            assert gap < 1e-9, (n, jet, gap)
            checks.append(dict(jet=jet, paired_tail_degree_difference=gap))
        # Direct finite difference checks the PHYSICAL derivative with integer
        # ranges frozen; no Fourier endpoint differentiation is assumed.
        derivative = runs[3]['complete_reflection_defect']
        for step in [1e-3, 5e-4]:
            values = []
            for sign in [-1, 1]:
                moved = physical(n, 0.05, data['x'] + sign*step)
                values.append(literal_sum(moved,n//2,n,False,0)
                    - cmath.exp(1j*moved['theta_reflection'])
                    * literal_sum(moved,n,2*n,True,0).conjugate())
            diff = (values[1]-values[0])/(2*step)
            error = abs(diff-derivative)
            assert error < 1e-6, (n, step, error)
            checks.append(dict(check='physical first jet finite difference',
                               step=step, absolute_difference=error))
        w_n = float(amplitude(float(n),data,False,0)[0])
        analytic_factor = (math.sin(math.pi/8)/math.pi*math.log((5*n+1)/(3*n+1))
            - 34/(225*math.pi**2*n*n))
        cases.append(dict(physical=data, weight_at_cutoff=w_n,
            analytic_shared_endpoint_lower_factor_estimate=analytic_factor,
            checks=checks, runs=runs))
    record = dict(date='2026-10-13', prepared_for='Edward Baker',
        assistance='Substantial LLM assistance; internal work, not independent validation',
        model='gpt-6-astra', reasoning_effort='ultra',
        model_provenance='Inherited parent session; actual recorded configuration verified by parent',
        status='binary64 diagnostic, not interval certificate',
        python=platform.python_version(), numpy=np.__version__,
        source_hashes={name:hashlib.sha256((root/name).read_bytes()).hexdigest() for name in inputs},
        checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        primary_references=['https://dlmf.nist.gov/1.8','https://dlmf.nist.gov/4.22.E3'],
        limitations=['No outward rounding or certified quadrature errors.',
            'No genuine H evaluation or physical multiple-zero exclusion.',
            'Small N has kappa=t log(x/(4 pi)) below the asymptotic target [1,3/2].',
            'Reflected exterior is a real-index chirp continuation sampled at integers.',
            'Both endpoint half-weights and every finite Fourier mode are retained.',
            'Natural-cutoff source residual is not estimated by these chirp diagnostics.'],
        cases=cases)
    args.record.write_text(json.dumps(encode(record), indent=2)+'\n')
    print(json.dumps({'record':str(args.record),'cases':len(cases),
                      'status':'diagnostics passed, no certification'},indent=2))


if __name__ == '__main__':
    main()
