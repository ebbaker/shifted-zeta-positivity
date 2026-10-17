#!/usr/bin/env python3
"""Bounded Acb enclosure of a theta zero bracket and its triple.

Prepared for Edward Baker, 17 October 2026.
Substantial LLM assistance; recorded model gpt-6.1-sol, effort ultra.
Uses H_0(x)=xi((1+i*x)/2)/8, xi(s)=s(s-1)pi^(-s/2)Gamma(s/2)zeta(s)/2.
This is a finite sign certificate, not an RH or zero-simplicity assertion.

Predeclared budget: 160 bits; three evaluations; wall-clock limit 30 seconds;
no adaptive precision increase or subdivision. Input decimals are exact
rationals enclosed via Arb, not binary Python float literals.

Retained quantitative replay contract (declared after a sign scout): every
real/imaginary output radius <= 1e-15; signed margins exceed the exact
rational delta=36/10^14. This final replay checks that new approximation
floor. The radius and delta were not predeclared for the initial scout.
"""
import hashlib
import json
import platform
import signal
import time
from pathlib import Path
import flint
from flint import acb, arb, ctx

BITS = 160
MAX_SECONDS = 30
MAX_RADIUS = '1e-15'
DELTA_NUMERATOR = 36
DELTA_DENOMINATOR = 10**14
CASES = [('lower_endpoint', '28.26945'),
         ('upper_endpoint', '28.26946'),
         ('tripled_interval', '84.808365 +/- 0.000015')]


def enclosure(x):
    s = acb(arb(1)/2, x/2)
    return s*(s-1)/16*(-s*arb.pi().log()/2).exp()*(s/2).gamma()*s.zeta()


def fail_timeout(signum, frame):
    raise TimeoutError('predeclared 30-second wall-clock budget exceeded')


def main():
    started = time.monotonic()
    signal.signal(signal.SIGALRM, fail_timeout)
    signal.alarm(MAX_SECONDS)
    ctx.prec = BITS
    rows = []
    values = []
    for label, input_ball in CASES:
        x = arb(input_ball)
        z = enclosure(x)
        assert z.is_finite() and z.imag.contains(0)
        assert z.real.rad() <= arb(MAX_RADIUS)
        assert z.imag.rad() <= arb(MAX_RADIUS)
        sign = 1 if z.real > 0 else (-1 if z.real < 0 else 0)
        rows.append({'label': label, 'input': input_ball,
                     'real': z.real.str(65, more=True),
                     'imag': z.imag.str(65, more=True),
                     'strict_sign': sign})
        values.append(z.real)
    assert rows[0]['strict_sign'] == 1
    assert rows[1]['strict_sign'] == -1
    assert rows[2]['strict_sign'] != 0
    # Simple rational outer bounds make the finite certificate easy to quote.
    outer_strings = [('2e-11', '3e-11'), ('-9e-10', '-8e-10'),
                     ('-3.68e-13', '-3.67e-13')]
    outer = [(arb(a), arb(b)) for a, b in outer_strings]
    for row, value, bounds in zip(rows, values, outer):
        row['outer_bounds_check'] = bool(value > bounds[0] and value < bounds[1])
        assert row['outer_bounds_check']
    for row, bounds in zip(rows, outer_strings):
        row['rational_outer_interval'] = list(bounds)
    triple = arb(CASES[2][1])
    assert triple.contains(3*arb(CASES[0][1]))
    assert triple.contains(3*arb(CASES[1][1]))
    delta = arb(DELTA_NUMERATOR)/DELTA_DENOMINATOR
    assert values[0] > delta
    assert values[1] < -delta
    assert values[2] < -delta
    signal.alarm(0)
    output = {'schema': 'constructive_stable_harmonic_signs_v1',
              'date': '2026-10-17', 'prepared_for': 'Edward Baker',
              'model': 'gpt-6.1-sol', 'reasoning_effort': 'ultra',
              'llm_assistance': 'Substantial LLM assistance.',
              'python_version': platform.python_version(),
              'python_flint_version': flint.__version__,
              'underlying_flint_version': flint.__FLINT_VERSION__,
              'budget': {'precision_bits': BITS, 'evaluations': len(CASES),
                         'wall_clock_seconds': MAX_SECONDS,
                         'precision_escalation': False, 'subdivision': False},
              'retained_replay_contract': {
                  'declared_after_initial_sign_scout': True,
                  'requested_output_radius_at_most': MAX_RADIUS,
                  'strict_signed_margin': '36/100000000000000',
                  'replay_reason': 'Verify newly added quantitative approximation floor and finalize artifacts'},
              'formula': 's=(1+i*x)/2; H0=s(s-1)pi^(-s/2)Gamma(s/2)zeta(s)/16',
              'rows': rows, 'elapsed_seconds': time.monotonic()-started,
              'uniform_approximation_obstruction': {
                  'delta_exact': '36/100000000000000',
                  'delta_decimal': '3.6e-13',
                  'domain': '[28.26945,28.26946] union [84.80835,84.80838]',
                  'endpoint_and_triple_margins_strictly_exceed_delta': True,
                  'class': 'Finite products of cos(a_j*x) times a continuous nonvanishing real multiplier',
                  'conclusion': 'No member has uniform error strictly less than delta on this domain.'},
              'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'references': ['https://python-flint.readthedocs.io/en/latest/general.html#inexact-numbers-and-numerical-evaluation',
                             'https://python-flint.readthedocs.io/en/latest/acb.html#flint.acb.zeta'],
              'scope': 'Finite validated signs; continuity yields at least one zero in (28.26945,28.26946), and H0 has fixed nonzero sign on [84.80835,84.80838].'}
    path = Path(__file__).with_name('HARMONIC_SIGN_CERTIFICATE.json')
    path.write_text(json.dumps(output, indent=2)+'\n')
    print(json.dumps(output, indent=2))


if __name__ == '__main__':
    main()
