#!/usr/bin/env python3
"""Exact algebra checks for HDC brainstorm Note 22; requires SymPy 1.14.

Checks identities for independent holomorphic and antiholomorphic jets with
the heat equation imposed. These are algebra checks, not theta estimates.
"""
import argparse
import json
import platform
from pathlib import Path

import sympy as s


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    f = s.symbols('f0:5')
    g = s.symbols('g0:5')
    epsilon = s.symbols('epsilon', positive=True)

    def dx(q):
        return sum(s.diff(q, f[k])*f[k+1] + s.diff(q, g[k])*g[k+1]
                   for k in range(4))

    def dy(q):
        return s.I * sum(s.diff(q, f[k])*f[k+1] - s.diff(q, g[k])*g[k+1]
                         for k in range(4))

    def dt(q):
        return -sum(s.diff(q, f[k])*f[k+2] + s.diff(q, g[k])*g[k+2]
                    for k in range(3))

    def laplacian(q):
        return dx(dx(q)) + dy(dy(q))

    denominator = f[0]*g[0] + epsilon**2
    # A below omits the spatially/time-constant epsilon/sqrt(pi).
    amplitude = f[1]/denominator
    conjugate_amplitude = g[1]/denominator
    potential = -2*dx(dy(s.log(denominator)))
    density = epsilon**2*f[1]*g[1]/(s.pi*denominator**2)
    velocity = f[2]/f[1]
    conjugate_velocity = g[2]/g[1]
    ux = (velocity + conjugate_velocity)/2
    uy = (velocity - conjugate_velocity)/(2*s.I)
    jx = epsilon**2*(f[2]*g[1] + g[2]*f[1])/(2*s.pi*denominator**2)
    jy = epsilon**2*(f[2]*g[1] - g[2]*f[1])/(2*s.pi*s.I*denominator**2)
    phase_x, phase_y = uy, ux
    phase_t = (-f[3]/f[1] + g[3]/g[1])/(2*s.I)

    residuals = {
        'schrodinger_equation': s.I*dt(amplitude) + dx(dy(amplitude))
                               - potential*amplitude,
        'continuity': dt(density) + dx(jx) + dy(jy),
        'density_from_laplacian': laplacian(s.log(denominator)) - 4*s.pi*density,
        'current_x_from_amplitude': epsilon**2/s.pi * (
            conjugate_amplitude*dy(amplitude) - amplitude*dy(conjugate_amplitude)
        )/(2*s.I) - jx,
        'current_y_from_amplitude': epsilon**2/s.pi * (
            conjugate_amplitude*dx(amplitude) - amplitude*dx(conjugate_amplitude)
        )/(2*s.I) - jy,
        'material_amplitude': dt(amplitude) + ux*dx(amplitude) + uy*dy(amplitude)
                              + (f[3]/f[1] - velocity**2)*amplitude,
        'potential_density_coupling': laplacian(potential) + 8*s.pi*dx(dy(density)),
        'phase_evolution': phase_t + dx(phase_x) + 2*phase_x*phase_y,
    }
    residuals = {name: s.simplify(s.factor(value)) for name, value in residuals.items()}
    assert all(value == 0 for value in residuals.values()), residuals

    radius, coefficient, scale = s.symbols('radius coefficient scale', positive=True)
    monomial_checks = []
    for m in range(1, 7):
        mass = m*coefficient**2*radius**(2*m)/(coefficient**2*radius**(2*m) + epsilon**2)
        radial_density = (2*epsilon**2*m*m*coefficient**2*radius**(2*m-1)
                          /(coefficient**2*radius**(2*m) + epsilon**2)**2)
        assert s.factor(s.diff(mass, radius)-radial_density) == 0
        assert s.limit(mass, radius, 0, dir='+') == 0
        assert s.limit(mass, radius, s.oo) == m
        monomial_checks.append({'multiplicity': m, 'total_amplitude_mass': m,
                                'coincident_ordered_pair_excess': m*(m-1)})

    separation = s.symbols('separation', positive=True)
    close_pair_excess = 2*s.exp(-separation**2/(8*scale))
    assert s.limit(close_pair_excess, scale, 0, dir='+') == 0
    assert close_pair_excess.subs(separation, 0) == 2

    record = {
        'date': '2026-10-24',
        'prepared_for': 'Edward Baker',
        'llm_assistance': 'Substantial; same-assistant derivation and algebra check',
        'model': 'gpt-6-astra (Codex)',
        'reasoning_effort': 'max',
        'python': platform.python_version(),
        'sympy': s.__version__,
        'generic_heat_jet_residuals': {name: str(value) for name, value in residuals.items()},
        'monomial_controls': monomial_checks,
        'distinct_pair_excess': str(close_pair_excess),
        'scope': 'Exact generic identities and finite multiplicity controls; no canonical theta estimate, numerical root campaign, global finite-mass claim for theta, or novelty claim.',
    }
    if args.output:
        args.output.write_text(json.dumps(record, indent=2) + '\n')
    print(json.dumps({'generic_identities': len(residuals), 'all_residuals_zero': True,
                      'monomial_controls': len(monomial_checks),
                      'distinct_pair_limit': 0, 'double_pair_excess': 2}))


if __name__ == '__main__':
    main()
