#!/usr/bin/env python3
"""Finite source-value obstructions for two specified stable-seed classes.

Prepared for Edward Baker, 17 October 2026, with substantial LLM assistance.
Parent-recorded serving configuration: gpt-6.1-sol, reasoning effort ultra.
Full-history subagents inherit that configuration by the collaboration API.

Declared after floating-point scouts and before this interval replay:
160 bits; n=1,...,8 for each theta sum; 4 potential-test nodes and
5 Bessel-ratio nodes; total wall limit 30 seconds; no precision escalation
or subdivision; required enclosure width < 1e-7 for each finite difference.
Every input is rational or an Arb elementary-function enclosure.
"""

import hashlib
import json
import platform
import signal
import time
from pathlib import Path

import flint
from flint import arb, ctx

BITS = 160
N = 8
MAX_SECONDS = 30
MAX_WIDTH = '1e-7'


def timeout(signum, frame):
    raise TimeoutError('predeclared 30-second budget exceeded')


def theta_phi(u):
    """Actual theta source, with a complete signed tail enclosure.

    For u>=0 all summands are positive. Discarding the negative term gives
    T_N(u)<=2*pi^2*exp(9u)*sum_{n>N} n^4*exp(-pi*n^2), since exp(4u)>=1.
    Successive majorant-term ratios are bounded by
    q=16*exp(-pi*(2N+3))<1 for n>=N+1. Geometric summation gives tail_upper.
    A symmetric radius enclosing [0,tail_upper] is conservative.
    """
    pi = arb.pi()
    e4u, e5u, e9u = (4*u).exp(), (5*u).exp(), (9*u).exp()
    assert u >= 0
    partial = arb(0)
    for n in range(1, N+1):
        partial += (2*pi*pi*n**4*e9u - 3*pi*n*n*e5u) * (-pi*n*n*e4u).exp()
    q = 16*(-pi*(2*N+3)).exp()
    assert q < 1
    tail_upper = 2*pi*pi*e9u*(N+1)**4*(-pi*(N+1)**2).exp()/(1-q)
    assert tail_upper > 0
    result = partial + arb(0, tail_upper.upper())
    assert result > 0
    return result, tail_upper


def serialize(x):
    return x.str(65, more=True)


def sample(k, denominator, bessel_ratio=False):
    x = arb(k)/denominator
    u = x.sqrt()
    phi, tail = theta_phi(u)
    value = phi*(2*arb.pi()*(4*u).cosh()).exp() if bessel_ratio else -phi.log()
    return value, {'x_exact': f'{k}/{denominator}', 'u': serialize(u),
                   'phi': serialize(phi), 'source_tail_upper': serialize(tail),
                   'value': serialize(value)}


def main():
    started = time.monotonic()
    signal.signal(signal.SIGALRM, timeout)
    signal.alarm(MAX_SECONDS)
    ctx.prec = BITS
    potential_values, potential_rows = [], []
    for k in range(4):
        value, row = sample(k, 100)
        potential_values.append(value)
        potential_rows.append(row)
    potential_weights = [-1, 3, -3, 1]
    potential_diff = sum(w*v for w, v in zip(potential_weights, potential_values))
    assert 2*potential_diff.rad() < arb(MAX_WIDTH)
    assert potential_diff > arb('-0.000434999')
    assert potential_diff < arb('-0.000434997')

    ratio_values, ratio_rows = [], []
    for k in range(5):
        value, row = sample(k, 1000, bessel_ratio=True)
        ratio_values.append(value)
        ratio_rows.append(row)
    ratio_weights = [1, -4, 6, -4, 1]
    ratio_diff = sum(w*v for w, v in zip(ratio_weights, ratio_values))
    assert 2*ratio_diff.rad() < arb(MAX_WIDTH)
    assert ratio_diff > arb('-5.232e-7')
    assert ratio_diff < arb('-5.230e-7')
    signal.alarm(0)
    output = {
        'schema': 'constructive_stable_source_obstructions_v1',
        'date': '2026-10-17', 'prepared_for': 'Edward Baker',
        'model': 'gpt-6.1-sol',
        'reasoning_effort': 'ultra',
        'configuration_provenance': 'Parent-recorded turn_context; full-history subagent inherits parent configuration.',
        'llm_assistance': 'Substantial LLM assistance.',
        'python_version': platform.python_version(),
        'python_flint_version': flint.__version__,
        'underlying_flint_version': flint.__FLINT_VERSION__,
        'budget': {'precision_bits': BITS, 'theta_terms_per_node': N,
                   'nodes': 9, 'wall_clock_seconds': MAX_SECONDS,
                   'precision_escalation': False, 'subdivision': False},
        'replay_contract': {'declared_after_floating_point_scout': True,
                            'finite_difference_width_at_most': MAX_WIDTH},
        'formula': 'Phi(u)=sum_{n>=1}(2*pi^2*n^4*exp(9u)-3*pi*n^2*exp(5u))*exp(-pi*n^2*exp(4u))',
        'tail_proof': 'For u>=0, 0<T_N<=2*pi^2*exp(9u)*(N+1)^4*exp(-pi*(N+1)^2)/(1-16*exp(-pi*(2N+3))).',
        'potential_test': {
            'function': 'V(x)=-log(Phi(sqrt(x)))',
            'step_exact': '1/100', 'weights': potential_weights,
            'rows': potential_rows,
            'finite_difference': serialize(potential_diff),
            'rational_outer_interval': ['-0.000434999', '-0.000434997'],
            'strict_sign': -1,
            'scope': 'Excludes pointwise convergence at these four nodes from positive sources whose negative log has nonnegative u^(2k) coefficients for k>=3; constants and quadratic or quartic terms cancel.'},
        'bessel_multiplier_test': {
            'function': 'U(x)=Phi(sqrt(x))*exp(2*pi*cosh(4*sqrt(x)))',
            'step_exact': '1/1000', 'weights': ratio_weights,
            'rows': ratio_rows,
            'finite_difference': serialize(ratio_diff),
            'rational_outer_interval': ['-5.232e-7', '-5.230e-7'],
            'strict_sign': -1,
            'scope': 'Excludes pointwise convergence at these five nodes of sources exp(-2*pi*cosh(4u))*U_n(u), where each U_n has nonnegative even Taylor coefficients. Includes positive normalized even universal factors.'},
        'elapsed_seconds': time.monotonic()-started,
        'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'references': [
            'https://repository.tudelft.nl/file/File_524a4d3c-0858-4c55-b425-8c8ce1fb89da',
            'https://arxiv.org/pdf/0801.2996',
            'https://python-flint.readthedocs.io/en/latest/arb.html'],
        'claims_not_made': ['No exclusion of every stable seed or varying Bessel base.',
                             'No RH assertion.', 'No formal round review.']}
    output_path = Path(__file__).with_name('SOURCE_ALTERNATIVE_OBSTRUCTIONS.json')
    output_path.write_text(json.dumps(output, indent=2)+'\n')
    print(json.dumps({'path': str(output_path),
                      'potential_finite_difference': serialize(potential_diff),
                      'bessel_ratio_finite_difference': serialize(ratio_diff),
                      'elapsed_seconds': output['elapsed_seconds']}, indent=2))


if __name__ == '__main__':
    main()
