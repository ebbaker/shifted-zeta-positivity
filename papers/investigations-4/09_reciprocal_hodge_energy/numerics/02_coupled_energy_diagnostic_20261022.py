#!/usr/bin/env python3
"""Floating polynomial check of RHE Note03; not a certificate or theta data.

Prepared for Edward Baker with LLM assistance, gpt-6.1-sol, effort ultra.
2026-10-22. Standard-library quadrature of complete smooth-cover geometry.
"""

import cmath
import hashlib
import json
import math
from pathlib import Path
import platform

EPSILON = 0.1
RADIUS = 5 / 12
M2, M3, M4 = 2.6, 0.6, 0.0
BOUNDARY_CELLS, ANGLE_CELLS, RADIAL_CELLS = 8192, 512, 512


def midpoint(function, left, right, cells):
    step = (right - left) / cells
    return step * math.fsum(function(left + (j + 0.5) * step) for j in range(cells))


def bisect(function, left, right):
    fl = function(left)
    assert fl * function(right) < 0
    for _ in range(70):
        center = (left + right) / 2
        fc = function(center)
        if (fl > 0) == (fc > 0):
            left, fl = center, fc
        else:
            right = center
    return (left + right) / 2


def constants():
    nu = 0.75  # |A|=1
    ell = M3 / (12 * nu ** 1.5)
    kay = M3 * M3 / (48 * nu ** 2.5) + M4 / (24 * nu ** 1.5)
    oscillation = 8 * math.pi * RADIUS * ell / math.sqrt(nu) + 8 * math.pi * RADIUS**2 * ell**2
    jay = 14 * M3**2 / 27 + 23 * M4 / 36
    sigma = min(1, 3 * RADIUS**2 / (8 * M2), RADIUS / (4 * M3))
    dee = 2 * RADIUS * math.sqrt(5 / 6)
    kcmp = max(0, 3 * oscillation / (2 * math.pi) + 7 * (math.log(2) + 0.25) - 16)
    sstar = min(sigma, dee**2, nu / (6 * jay), dee**2 * math.exp(-2 * (kcmp + 1)))
    return dict(nu=nu, L=ell, K=kay, Cosc=oscillation, J=jay, sigma=sigma, D=dee, sstar=sstar)


def diagnostic(tau, params):
    def field(x):
        return x*x + EPSILON*x**3 - 2*tau - 6*EPSILON*tau*x

    alpha = bisect(field, -RADIUS, 0)
    beta = bisect(field, 0, RADIUS)
    center, half_gap = (alpha + beta) / 2, (beta - alpha) / 2

    def unit(x):
        return 1 + EPSILON * (x + alpha + beta)

    def boundary(theta):
        x = RADIUS * cmath.exp(1j * theta)
        shifted = x - center
        y0 = shifted * cmath.sqrt(1 - (half_gap / shifted)**2)
        return 1j * x / (cmath.sqrt(unit(x)) * y0)

    step = 2 * math.pi / BOUNDARY_CELLS
    trace = [boundary(j * step) for j in range(BOUNDARY_CELLS + 1)]
    core = step * sum(trace[:-1])
    rotation = 1j * core.conjugate() / abs(core)
    v = [0.0]
    complex_increment = [0j]
    for j in range(BOUNDARY_CELLS):
        v.append(v[-1] + (rotation * (trace[j] + trace[j + 1])).real * step / 2)
        complex_increment.append(complex_increment[-1] + (trace[j] + trace[j + 1]) * step / 2)
    flux = [(rotation * value).imag for value in trace]
    exterior = 2 * step * math.fsum((v[j] * flux[j] + v[j + 1] * flux[j + 1]) / 2 for j in range(BOUNDARY_CELLS))
    u_marked = math.acosh((RADIUS - center) / half_gap)
    transverse = -2 * midpoint(lambda s: 1 / math.sqrt(unit(center + half_gap * math.cosh(s))), 0, u_marked, RADIAL_CELLS * 4)
    scalar_center = (core.conjugate() * transverse).imag
    full_primitive = [-transverse / 2 + value for value in complex_increment]
    # Odd primitives differ from one coherent cut-domain choice by a core
    # constant on the other boundary. This changes only the imaginary
    # subtotal, so the following is the full real physical payment.
    physical_payment = (1j * step * sum(
        (full_primitive[j] * trace[j].conjugate() + full_primitive[j + 1] * trace[j + 1].conjugate()) / 2
        for j in range(BOUNDARY_CELLS))).real
    cut_payment = scalar_center / 2

    def extent(theta):
        sine = math.sin(theta)
        cmax = (-center * math.cos(theta) + math.sqrt(RADIUS**2 - (center**2 - half_gap**2) * sine*sine)) / half_gap
        return math.acosh(cmax)

    def angular_energy(theta):
        cap = extent(theta)

        def integrand(s):
            x = center + half_gap * cmath.cosh(complex(s, theta))
            return 1 / abs(unit(x))

        return midpoint(integrand, -cap, cap, RADIAL_CELLS)

    energy = midpoint(angular_energy, 0, 2 * math.pi, ANGLE_CELLS)
    model_energy = 2 * midpoint(extent, 0, 2 * math.pi, ANGLE_CELLS)
    coefficient = core / (2j * math.pi)
    model_transverse = -2 * u_marked
    ce = params['Cosc'] + 8 * math.pi * params['K'] * RADIUS**2 / math.sqrt(params['nu'])
    cp = 4 * params['L'] * RADIUS + 2 * params['K'] * RADIUS**2
    sharp_upper = 4 * math.pi * (1 + params['J'] * tau / params['nu']) * math.asinh(params['D'] / math.sqrt(tau)) + params['Cosc']
    coarse_upper = (8 / 3) * (4 * math.pi + 2 * math.pi * math.log(params['D'] / math.sqrt(tau)))
    identity_defect = abs(energy - scalar_center - exterior)
    energy_remainder = abs(energy - abs(coefficient)**2 * model_energy)
    period_remainder = abs(transverse - coefficient * model_transverse)
    cut_remainder = abs(cut_payment + math.pi * abs(coefficient)**2 * model_transverse)
    physical_remainder = abs(physical_payment - abs(coefficient)**2 * (model_energy + math.pi * model_transverse))
    assert identity_defect < 2e-5
    assert abs(energy - cut_payment - physical_payment) < 2e-5
    assert energy_remainder <= ce
    assert period_remainder <= cp
    assert cut_remainder <= math.pi * abs(coefficient) * cp
    assert physical_remainder <= ce + math.pi * abs(coefficient) * cp
    assert energy <= sharp_upper < coarse_upper
    assert coarse_upper - sharp_upper >= 2 * math.pi / 3
    return dict(tau=tau, alpha=alpha, beta=beta, midpoint=center, half_gap=half_gap,
                energy=energy, model_energy=model_energy, core=[core.real, core.imag],
                transverse=transverse, scalar_center=scalar_center, exterior_correction=exterior,
                cut_payment=cut_payment, physical_boundary_payment=physical_payment,
                full_cut_boundary_identity_defect=abs(energy - cut_payment - physical_payment),
                cut_model_remainder=cut_remainder, physical_boundary_model_remainder=physical_remainder,
                real_primitive_identity_defect=identity_defect, periodic_real_primitive_defect=abs(v[-1]),
                energy_model_remainder=energy_remainder, energy_remainder_bound=ce,
                relative_period_remainder=period_remainder, relative_period_bound=cp,
                sharper_upper=sharp_upper, coarse_upper=coarse_upper)


if __name__ == '__main__':
    params = constants()
    print(json.dumps(dict(date='2026-10-22', prepared_for='Edward Baker', model='gpt-6.1-sol',
                         reasoning_effort='ultra', status='floating diagnostic; not a certificate or theta acquisition',
                         python=platform.python_version(), script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                         polynomial_epsilon=EPSILON, radius=RADIUS, A=1, M2=M2, M3=M3, M4=M4,
                         boundary_cells=BOUNDARY_CELLS, angle_cells=ANGLE_CELLS, radial_cells=RADIAL_CELLS,
                         constants=params, rows=[diagnostic(params['sstar']/factor, params) for factor in (2, 4, 8)]), indent=2))
