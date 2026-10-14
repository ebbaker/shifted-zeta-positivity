#!/usr/bin/env python3
"""Complete angular correction: exact anchor constants and outward transfer test.

13 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded parent model gpt-6-astra (Codex), reasoning effort ultra.
The explicitly marked floating Volterra/transform diagnostics are not certificates.
"""
import argparse
import cmath
from decimal import Decimal
from fractions import Fraction as Q
import hashlib
import json
import math
from pathlib import Path
import platform
import sys
import time

HASHES = {
    'check_block_current.py': '0cfca37632cfaaea522cce2a9514b81eaf9db0bf6213cd243de0f937679627a2',
    'check_complete_current_rectangle.py': 'ac547ff45915d95369afc558f6ee3daa01fb6974ad1569e719dc3f0abcd4c522',
}


def derivative_polynomial(poly):
    result = [0]*(len(poly)+1)
    for k, value in enumerate(poly):
        result[k] += (1+4*k)*value
        result[k+1] -= 4*value
    return result


def exact_anchor_checks():
    # R_n'+5R_n=(6-4z)R_n, while -4pi e^-4u Phi_n/R_n=-2(2z²-3z)/z.
    assert [0, 6, -4] == [0, -2*(-3), -2*2]
    assert derivative_polynomial([1]) == [1, -4]
    assert derivative_polynomial([1, -4]) == [1, -24, 16]
    delta, m = Q(1, 10), Q(5)
    exp_two_fifths_upper = 1+Q(2, 5)+(Q(2, 5)**2/2)/(1-Q(2, 15))
    assert exp_two_fifths_upper == Q(97, 65) < Q(3, 2)
    assert Q(22, 7)*Q(3, 2) == Q(33, 7) < 5
    # pi>3 gives 2pi²[(4pi-1)²-16pi]>18*73.
    # exp(pi exp(.4))<exp(5)<3^5, since exp(1)<3.
    curvature_lower = Q(18*73, 3**5)
    assert curvature_lower == Q(146, 27) > m
    low_frequency_lower = 2*m*delta**3/(3*10)  # pi²<10
    assert low_frequency_lower == Q(1, 3000)
    high_frequency_coefficient = m*delta/2
    assert high_frequency_coefficient == Q(1, 4) > low_frequency_lower
    return {
        'status': 'PASS', 'arithmetic': 'exact rational polynomial and constant checks',
        'source_ODE': "R'(u)+5R(u)=-4*pi*exp(-4u)*Phi(u)",
        'derivative_polynomials_for_exp_u_minus_z': [[1], [1, -4], [1, -24, 16]],
        'delta': str(delta), 'exp_two_fifths_upper': str(exp_two_fifths_upper),
        'uniform_curvature_lower': str(curvature_lower), 'retained_simple_curvature_lower': str(m),
        'low_frequency_constant': str(low_frequency_lower),
        'high_frequency_inverse_square_coefficient': str(high_frequency_coefficient),
        'analytic_claim_checked_constants': 'P_t(x)>1/[3000*(1+x^2)] for every real x and 0<=t<=1',
        'proof_dependencies': [
            'For E=exp(4u), 1+2tu<=E on u>=0,0<=t<=1.',
            "r_n''/r_n=(1+2tu-4*pi*n^2*E)^2+2t-16*pi*n^2*E is strictly positive.",
            "On [0,1/10], r_t'' >= r_1,t'' >146/27>5.",
            "P_t(x)=x^-2 integral_0^infinity r_t''(u)(1-cos(xu))du, with the continuous x=0 limit.",
            'Use 1-cos(y)>=2*y^2/pi^2 for |y|<=pi, on |x|<=20; use integral_0^delta(1-cos(xu))du>=delta-1/|x| on |x|>=20.',
        ],
        'scope': 'The global analytic proof is in the accompanying note; these assertions replay its algebra and elementary numerical constants.'}


def floating_identities():
    def sources(u):
        phi, correction = 0.0, 0.0
        for n in range(1, 5):
            z = math.pi*n*n*math.exp(4*u)
            basic = math.exp(u-z)
            phi += basic*(2*z*z-3*z)
            correction += 2*math.pi**2*n*n*basic
        return phi, correction
    def integrate(f, lower=0.0, upper=1.0, panels=8192):
        step = (upper-lower)/panels
        return step/3*sum((1 if i in (0, panels) else (4 if i % 2 else 2))*f(lower+i*step)
                          for i in range(panels+1))
    volterra = []
    for u in (0.0, .2, .5):
        direct = sources(u)[1]
        integral = 4*math.pi*math.exp(-5*u)*integrate(lambda v: math.exp(v)*sources(v)[0], u)
        assert abs(direct-integral) < 2e-12*max(1, abs(direct))
        volterra.append({'u': u, 'direct_R': direct, 'Volterra_R': integral, 'absolute_residual': abs(direct-integral)})
    transform = []
    x = 32.0
    for t in (0.0, .05):
        S = integrate(lambda u: cmath.exp(t*u*u+1j*x*u)*sources(u)[1])
        Sx = integrate(lambda u: 1j*u*cmath.exp(t*u*u+1j*x*u)*sources(u)[1])
        shifted = integrate(lambda u: cmath.exp(t*u*u+(1j*x-4)*u)*sources(u)[0])
        residual = (5-1j*x)*S+2j*t*Sx-sources(0)[1]+4*math.pi*shifted
        assert abs(residual) < 2e-11
        transform.append({'t': t, 'x': x, 'absolute_ODE_residual': abs(residual)})
    return {'status': 'PASS_DIAGNOSTIC_ONLY', 'arithmetic': 'binary64 finite n<=4 and source window [0,1]; no certified tails',
            'Simpson_subintervals': 8192,
            'Volterra_samples': volterra, 'Fourier_ODE_samples': transform}


def certificate(cells, interval_dir):
    for name, digest in HASHES.items():
        if hashlib.sha256((interval_dir/name).read_bytes()).hexdigest() != digest:
            raise RuntimeError('Retained interval source mismatch: '+name)
    sys.path.insert(0, str(interval_dir))
    from check_complete_current_rectangle import I, pi_interval, reduced_trig, absmax, PRECISION
    pi = pi_interval(); x = I(32); radius = I(1); width = radius/cells
    polys = [[[0, -3, 2]], [[1]]]
    for channel in (0, 1):
        for _ in range(4):
            polys[channel].append(derivative_polynomial(polys[channel][-1]))
    def evaluate(poly, z):
        value = I(0)
        for coefficient in reversed(poly):
            value = value*z+coefficient
        return value
    def source_jets(u):
        out = [[I(0) for _ in range(5)] for _ in range(2)]
        E, e1 = (4*u).exp(), u.exp()
        for n in (1, 2, 3):
            z = pi*n*n*E; basic = e1*(-z).exp()
            for j in range(5):
                out[0][j] += basic*evaluate(polys[0][j], z)
                out[1][j] += 2*pi**2*n*n*basic*evaluate(polys[1][j], z)
        return out
    def integrands(u):
        source = source_jets(u)
        _, cosine = reduced_trig(x*u, pi)
        return [cosine*source[k][0] for k in (0, 1)]
    totals, errors = [I(0), I(0)], [I(0), I(0)]
    left_values = integrands(I(0))
    for cell in range(cells):
        left, right = width*cell, width*(cell+1)
        box = I(left.lo, right.hi)
        middle_values, right_values = integrands((left+right)/2), integrands(right)
        source = source_jets(box)
        for channel in (0, 1):
            totals[channel] += width*(left_values[channel]+4*middle_values[channel]+right_values[channel])/6
            fourth = sum((math.comb(4, k)*x**(4-k)*I(absmax(source[channel][k])) for k in range(5)), I(0))
            errors[channel] += width**5*fourth/2880
        left_values = right_values
    theta_tails, u_tails = [], []
    for power, source_exponent in ((4, 9), (2, 1)):
        ratio = (I(5)/4)**power*(-9*pi).exp()
        assert ratio.hi < 1
        theta_tails.append(2*pi**2*4**power*(-16*pi).exp()/((1-ratio)*(64*pi-source_exponent)))
        assert ((I(2)**power)*(-3*pi).exp()).hi < Decimal('.5')
        kappa = 4*pi*(4*radius).exp()-source_exponent
        u_tails.append(4*pi**2*(source_exponent*radius-pi*(4*radius).exp()).exp()/kappa)
    paid = []
    for channel in (0, 1):
        error = errors[channel]+theta_tails[channel]+u_tails[channel]
        paid.append(totals[channel]+I(error.hi.copy_negate(), error.hi))
    H, P = paid; auxiliary = H-P
    assert H.hi < 0 < P.lo
    assert auxiliary.hi < 0
    ratio = -auxiliary/P
    assert ratio.lo > 1
    delta = I('.1')
    m_bound = 2*pi**2*((4*pi-1)**2-16*pi)*(-pi*(4*delta).exp()).exp()
    assert m_bound.lo > 5
    return {
        'status': 'PASS', 'arithmetic': str(PRECISION)+'-digit outward Decimal with trigonometric Taylor remainders',
        'time': ['0', '0'], 'physical_frequency_x': x.strings(), 'half_source_window': radius.strings(),
        'Simpson_panels': cells, 'theta_terms': [1, 2, 3],
        'retained_finite_H_P': [v.strings() for v in totals],
        'Simpson_fourth_derivative_error_bounds': [v.strings() for v in errors],
        'complete_omitted_theta_tail_bounds': [v.strings() for v in theta_tails],
        'complete_source_u_tail_bounds': [v.strings() for v in u_tails],
        'complete_H_P': [v.strings() for v in paid], 'complete_auxiliary_A_equals_H_minus_P': auxiliary.strings(),
        'absolute_A_over_P': ratio.strings(),
        'global_anchor_curvature_bound_on_zero_to_one_tenth': m_bound.strings(),
        'scope': 'At t=0,x=32 the genuine H is negative and the complete correction P is positive, so |A|>P. This disproves global transfer through |A|<=P or |A|<=(1-delta)P. It is not a stationary sign test.',
        'limitations': ['The witness is one point chosen by a floating diagnostic.',
                        'Positive correction P alone gives no lower bound on |H| or on the physical value-slope pair.',
                        'No RH conclusion or complete paired-kernel factorization is established.']}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--record', type=Path, default=Path(__file__).with_name('COMPLETE_ANGULAR_CHANNELS_RECORD_20261013.json'))
    parser.add_argument('--cells', type=int, default=512)
    parser.add_argument('--interval-source-dir', type=Path,
                        default=Path(__file__).resolve().parents[4]/'quasi-rh-exponent-descent'/'newman_collisions'/'13_microlocal_phase_space'/'numerics')
    args = parser.parse_args(); assert args.cells > 0
    started = time.perf_counter()
    result = {'date': '2026-10-13', 'prepared_for': 'Edward Baker', 'model': 'gpt-6-astra (Codex)',
              'reasoning_effort': 'ultra; inherited from recorded parent session',
              'acknowledgment': 'Substantial LLM assistance; internal algebra and outward arithmetic, not independent validation.',
              'exact_anchor_checks': exact_anchor_checks(), 'floating_diagnostics': floating_identities(),
              'outward_certificate': certificate(args.cells, args.interval_source_dir),
              'imported_sources': HASHES, 'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'python_version': platform.python_version(), 'runtime_seconds': str(time.perf_counter()-started)}
    args.record.write_text(json.dumps(result, indent=2, sort_keys=True)+'\n')
    print(json.dumps({'exact_anchor_checks': result['exact_anchor_checks']['status'],
                      'floating_diagnostics': result['floating_diagnostics']['status'],
                      'outward_certificate': result['outward_certificate']['status'],
                      'complete_H_P': result['outward_certificate']['complete_H_P'],
                      'absolute_A_over_P': result['outward_certificate']['absolute_A_over_P'],
                      'runtime_seconds': result['runtime_seconds']}, indent=2))


if __name__ == '__main__':
    main()
