#!/usr/bin/env python3
"""Finite controls for the WZW collar and primary arithmetic-readout test.

Requires Python 3 and NumPy. These are floating diagnostics and exact rational
controls, not interval certificates, a full sewing construction, or an RH test.
"""
import argparse
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path
import platform

import numpy as np

H = 3.0 / 16.0
ALPHA = 2 * H
EULER = 0.577215664901532860606512090082402431
CASES = []


def check(name, value, threshold, comparison='<=', kind='floating'):
    value = float(value)
    passed = math.isfinite(value) and (
        value <= threshold if comparison == '<=' else value >= threshold)
    CASES.append(dict(name=name, value=value, threshold=threshold,
                      comparison=comparison, passed=passed, kind=kind))


def exact(name, value):
    check(name, 0 if value else 1, 0, kind='exact rational')


def quadrature(n):
    x, w = np.polynomial.legendre.leggauss(n)
    return (x + 1) / 2, w / 2


def primary(u, omega=0.0):
    u = np.asarray(u)
    return np.sinh(u) ** (-ALPHA) * np.cosh(omega * u)


def susceptibility(p):
    # Integral of exp(-p*u) * sinh(u)^(-2h), h=3/16.
    a = p / 2 + H
    return 2 ** (ALPHA - 1) * math.exp(
        math.lgamma(a) + math.lgamma(1 - ALPHA)
        - math.lgamma(a + 1 - ALPHA))


def susceptibility_quad(p, n):
    # y=1-exp(-2u), followed by y=r^(1/(1-alpha)), removes the
    # integrable collision singularity before numerical quadrature.
    r, w = quadrature(n)
    return (2 ** (ALPHA - 1) / (1 - ALPHA)
            * np.dot(w, (1 - r ** (1 / (1 - ALPHA))) ** (p / 2 + H - 1)))


def digamma(x):
    shift = 0.0
    while x < 24:
        shift -= 1 / x
        x += 1
    z = 1 / (x * x)
    return (shift + math.log(x) - .5 / x
            - z / 12 + z**2 / 120 - z**3 / 252
            + z**4 / 240 - z**5 / 132 + 691 * z**6 / 32760)


def target_a0(p):
    return digamma(1.25 + p / 2) - math.log(math.pi) + 2 / (p - .5)


def target_logk(p, omega):
    return (omega * math.log(math.pi)
            + math.lgamma((p + 2.5 - omega) / 2)
            - math.lgamma((p + 2.5 + omega) / 2)
            + math.log((p - .5 - omega) / (p - .5 + omega)))


def target_kernel(u, omega, n=80):
    # Prime-free gamma/rational kernel. In the Volterra integral use
    # v=u*z^(1/omega), which removes v^(omega-1) at v=0.
    u = np.asarray(u)
    z, w = quadrature(n)
    v = u[..., None] * z ** (1 / omega)
    ratio_v = -np.expm1(-2 * v) / (2 * v)
    integral = np.sum(w * np.exp(-(3 - 2 * omega) * v) * ratio_v ** (omega - 1), axis=-1)
    ratio_u = -np.expm1(-2 * u) / (2 * u)
    a = (2 * math.pi) ** omega / math.gamma(omega)
    return a * u ** (omega - 1) * (
        np.exp(-(2.5 - omega) * u) * ratio_u ** (omega - 1)
        - 2 * u * np.exp((.5 - omega) * u) * integral)


def cross_cell(omega, order):
    z, w = quadrature(order)
    # Unit L2 indicators on A=(0,.02), B=(.03,.05).
    x = .02 * z
    y = .03 + .02 * z
    kernel = target_kernel(y[:, None] - x[None, :], omega)
    return .02 * float(w @ kernel @ w)


def run():
    alpha = Fraction(3, 8)
    coefficients = [Fraction(1)]
    for n in range(1, 9):
        coefficients.append(coefficients[-1] * (alpha + n - 1) / n)
    exact('primary first four spectral weights', coefficients[:4] == [
        Fraction(1), Fraction(3, 8), Fraction(33, 128), Fraction(209, 1024)])
    # Obtain descendant norms using the sl(2) lowering/raising relation,
    # then compare with the binomial coefficients from the conformal map.
    norm = Fraction(1)
    for n in range(1, 9):
        norm *= n * (alpha + n - 1)
        exact(f'global descendant norm at level {n}',
              norm / math.factorial(n)**2 == coefficients[n])
    exact('uniform gamma weights disagree at level one', coefficients[1] != 1)
    exact('spin-half gap at spacing two is 3/8', 2 * Fraction(3, 16) == Fraction(3, 8))
    exact('spin-one unit weights have wrong gamma gap',
          2 * Fraction(1, 2) != Fraction(1, 2))

    for u in [.05, .2, .7, 1.2]:
        mapped = (4 * math.exp(2 * u) / math.expm1(2 * u)**2) ** H
        check(f'plane-to-cylinder covariance u={u}', abs(mapped / primary(u) - 1), 2e-14)
        q = math.exp(-2 * u)
        coefficient = 1.0
        terms = [1.0]
        cutoff = 64
        for n in range(1, cutoff + 1):
            coefficient *= (ALPHA + n - 1) / n
            terms.append(coefficient * q**n)
        prefactor = 2**ALPHA * math.exp(-2 * H * u)
        approximation = prefactor * math.fsum(terms)
        # For 0<alpha<1 all d_n<=1; this gives an analytic truncation
        # bound. The additional allowance is explicitly floating roundoff.
        tail = prefactor * q**(cutoff + 1) / (1 - q)
        check(f'spectral sum with analytic tail u={u}',
              abs(float(primary(u)) - approximation), tail + 2e-13)

    for p in [4.0, 8.0, 16.0]:
        closed = susceptibility(p)
        fine = susceptibility_quad(p, 256)
        coarse = susceptibility_quad(p, 128)
        check(f'primary beta susceptibility p={p}', abs(fine / closed - 1), 2e-9)
        check(f'primary quadrature refinement p={p}', abs(fine - coarse), 2e-8)

    for u in [.2, .7, 1.2]:
        omega = .25
        pair = .5 * float(primary(u)) * (math.exp(omega * u) + math.exp(-omega * u))
        check(f'opposite-charge cosh factor u={u}', abs(pair - primary(u, omega)), 2e-14)

    levels = np.arange(16)
    f = (1 + 1j * ((levels % 3) - 1)) / (levels + 1)**2
    f = f / np.linalg.norm(f)
    for s in [.01, .2, .7]:
        evolved = np.exp(-s * levels) * f
        z, w = quadrature(80)
        loss_integral = s * float(np.dot(w, [
            2 * np.sum(levels * abs(f)**2 * np.exp(-2 * s * v * levels)) for v in z]))
        check(f'collar norm balance s={s}',
              abs(np.linalg.norm(evolved)**2 + loss_integral - 1), 2e-14)
        check(f'collar contraction s={s}', np.linalg.norm(evolved), 1 + 2e-14)
    check('collar two-stage composition', np.linalg.norm(
        np.exp(-.2 * levels) * np.exp(-.3 * levels) * f - np.exp(-.5 * levels) * f), 2e-15)

    for p in [2.0, 4.0, 9.0]:
        delta = 2e-5
        derivative = -(target_logk(p, delta) - target_logk(p, -delta)) / (2 * delta)
        check(f'complete prime-free shift derivative p={p}', abs(derivative - target_a0(p)), 2e-9)
    w0 = -EULER - math.pi / 2 - 3 * math.log(2) - math.log(math.pi)
    check('fixed local constant from digamma', abs(w0 - (digamma(.25) - math.log(math.pi))), 2e-14)
    for epsilon in [1e-3, 1e-4]:
        v = math.exp(-epsilon / 2)
        tail = math.log((1 + v) / (1 - v)) + 2 * math.atan(v)
        contact = -w0 - tail
        check(f'hard-cutoff contact asymptotic epsilon={epsilon}',
              abs(contact - math.log(epsilon) - EULER - math.log(2 * math.pi)), 2 * epsilon)

    for omega in [.1, .25, .5]:
        u = 1e-6
        leading = (2 * math.pi)**omega / math.gamma(omega)
        ratio = float(target_kernel(u, omega)) * u**(1 - omega) / leading
        check(f'arithmetic collision order omega={omega}', abs(ratio - 1), 4e-6)

    cross = cross_cell(.25, 32)
    check('arithmetic forward disjoint-cell response nonzero', cross, .01, '>=')
    check('disjoint-cell quadrature refinement', abs(cross - cross_cell(.25, 48)), 2e-12)
    # The reversed cell response is exactly zero by causal support, not
    # an approximate numerical cancellation.
    exact('reversed disjoint-cell response vanishes by support', Fraction(1, 50) < Fraction(3, 100))

    ell = math.log(2)
    delay_samples = []
    for omega in [0.0, .25]:
        coefficient = -math.sqrt(2) * ell * math.cosh(omega * ell)
        z, w = quadrature(48)
        epsilon = 1e-4
        mass = 2 * epsilon * float(np.dot(w, primary(ell - epsilon + 2 * epsilon * z, omega)))
        check(f'primary smooth near-delay mass omega={omega}',
              abs(mass / (2 * epsilon) - primary(ell, omega)), 2e-8)
        check(f'prime atom absent from primary readout omega={omega}', abs(coefficient) - mass, .9, '>=')
        delay_samples.append(dict(omega=omega, required_generator_atom=coefficient,
                                 primary_mass_on_width_0_0002=mass))
    for omega in [.1, .25, .5]:
        c2 = (2**omega - 2**(-omega)) / math.sqrt(2)
        check(f'first transfer-delay coefficient omega={omega}',
              abs(c2 - math.sqrt(2) * math.sinh(omega * ell)), 2e-15)
        delta = 1e-5
        derivative = (math.sqrt(2) * math.sinh((omega + delta) * ell)
                      - math.sqrt(2) * math.sinh((omega - delta) * ell)) / (2 * delta)
        check(f'transfer-delay coefficient derivative omega={omega}',
              abs(derivative - math.sqrt(2) * ell * math.cosh(omega * ell)), 1e-10)

    p = 1e5
    check('primary susceptibility decays at high p',
          abs(susceptibility(p) * p**(1 - ALPHA) / math.gamma(1 - ALPHA) - 1), 1e-5)
    check('arithmetic generator logarithmic high-p growth',
          abs(target_a0(p) - math.log(p) + math.log(2 * math.pi)), 1e-4)

    return dict(schema_version=1, date='2026-09-23',
                model='GPT-6 (Codex; developer-provided identity)',
                effort='not exposed; not inferred',
                status='Exact finite algebra and floating diagnostics; no interval certification or physical realization',
                parameters=dict(h=H, alpha=ALPHA, cylinder_scale=2,
                                spectral_cutoff=64, collar_levels=16),
                environment=dict(python=platform.python_version(), numpy=np.__version__),
                program_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                case_count=len(CASES),
                exact_rational_cases=sum(c['kind'] == 'exact rational' for c in CASES),
                all_pass=all(c['passed'] for c in CASES), cases=CASES,
                samples=dict(primary_spectral_weights=[str(c) for c in coefficients[:4]],
                             forward_cell_response=cross, reverse_cell_response=0,
                             local_constant=w0, first_delay=delay_samples,
                             source_high_p=dict(p=p, primary_susceptibility=susceptibility(p),
                                                arithmetic_generator=target_a0(p))))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    record = run()
    text = json.dumps(record, indent=2, sort_keys=True) + '\n'
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text)
        print(json.dumps({k: record[k] for k in ['case_count', 'exact_rational_cases', 'all_pass']}))
    else:
        print(text, end='')
    raise SystemExit(0 if record['all_pass'] else 1)
