#!/usr/bin/env python3
"""Exact finite checks for the hybrid exponent-pair cutoff lemma.

Prepared for Edward Baker, 14 October 2026 (America/New_York), with
substantial LLM assistance. Recorded parent model: gpt-6-astra; effort:
ultra, verified by the parent from the current turn metadata.

This checks rational identities and margins. It does not prove the imported
derivative tests, infinite sums, uniform analytic estimates, or theta signs.
No numerical sweep, quadrature, finite-height certification, or zero search
is performed. The JSON receipt has no wall-clock-dependent fields.
"""

import argparse
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    checks = []

    def equal(name, left, right):
        if left != right:
            raise AssertionError((name, left, right))
        checks.append({'name': name, 'kind': 'equality', 'value': str(left)})

    def positive(name, value):
        if value <= 0:
            raise AssertionError((name, value))
        checks.append({'name': name, 'kind': 'strict_positive', 'value': str(value)})

    theta = F(27, 10)
    lo, switch, hi = F(1, 4), F(4, 9), F(1, 2)

    # Coefficients are in ascending powers of beta, with delta=0.
    polys = {
        'fourth_first': (F(1, 14), F(3, 14) - theta / 4, theta / 4),
        'fourth_second': (-F(1, 14), F(15, 28) - theta / 4, theta / 4),
        'third_first': (F(1, 6), -theta / 4, theta / 4),
        'third_second': (-F(1, 6), F(1, 2) - theta / 4, theta / 4),
    }

    def value(poly, beta):
        return sum(c * beta ** i for i, c in enumerate(poly))

    endpoints = {
        'fourth_first': ((lo, -F(1, 640)), (switch, F(0))),
        'fourth_second': ((lo, -F(41, 640)), (switch, F(0))),
        'third_first': ((switch, F(0)), (hi, -F(1, 480))),
        'third_second': ((switch, -F(1, 9)), (hi, -F(41, 480))),
    }
    for name, poly in polys.items():
        equal(name + ' convexity coefficient', poly[2], F(27, 40))
        positive(name + ' strict convexity', poly[2])
        for beta, expected in endpoints[name]:
            equal(name + ' at beta=' + str(beta), value(poly, beta), expected)

    # Exact derivative-test powers for lambda_k comparable to T/M^k.
    equal('fourth first M power', 1 - F(4, 14), F(5, 7))
    equal('fourth second M power', F(3, 4) + F(4, 14), F(29, 28))
    equal('third first M power', 1 - F(3, 6), F(1, 2))
    equal('third second M power', F(1, 2) + F(3, 6), F(1))

    difference4 = tuple(a - b for a, b in zip(polys['fourth_second'],
                                               polys['fourth_first']))
    equal('fourth secondary minus first factorization', difference4,
          (-F(9, 28) * switch, F(9, 28), F(0)))
    equal('fourth secondary equals first at switch', value(difference4, switch), F(0))
    positive('fourth first dominates secondary at low endpoint',
             -value(difference4, lo))
    crossover = tuple(a - b for a, b in zip(polys['fourth_first'],
                                            polys['third_first']))
    equal('two principal estimates crossover factorization', crossover,
          (-F(3, 14) * switch, F(3, 14), F(0)))
    difference3 = tuple(a - b for a, b in zip(polys['third_second'],
                                               polys['third_first']))
    equal('third secondary minus first factorization', difference3,
          (-F(1, 3), F(1, 2), F(0)))
    equal('third secondary deficit at high endpoint', value(difference3, hi), -F(1, 12))

    # beta(1-beta) is increasing on [1/4,1/2], verified by its derivative.
    equal('frequency product low endpoint', lo * (1 - lo), F(3, 16))
    equal('frequency product high endpoint', hi * (1 - hi), F(1, 4))
    equal('frequency product derivative at high endpoint', 1 - 2 * hi, F(0))
    positive('frequency product derivative at low endpoint', 1 - 2 * lo)
    epsilon_decrease = F(1, 2) * F(3, 16) / 4
    delta_increase = F(1, 100) * F(1, 2)
    equal('theta increment decreases exponent per epsilon', epsilon_decrease, F(3, 128))
    equal('delta perturbation increases exponent per epsilon', delta_increase, F(1, 200))
    equal('net high-block margin per epsilon', epsilon_decrease - delta_increase,
          F(59, 3200))
    positive('reserve for extension beyond beta=1/2',
             epsilon_decrease - delta_increase - F(1, 100))

    delta_cap = F(1, 640)
    low_exponent = F(1, 2) + F(3, 16) * theta - delta_cap
    equal('low discrepancy base exponent', low_exponent, F(643, 640))
    positive('low discrepancy margin above 1+1/320', low_exponent - 1 - F(1, 320))
    sigma = F(1, 2) + theta / 4 - delta_cap
    equal('sigma lower-bound base value', sigma, F(751, 640))
    positive('sigma margin above 7/6', sigma - F(7, 6))
    equal('ordinary zeta tail exponent using beta=1/4',
          lo * (F(7, 6) - 1), F(1, 24))
    equal('complete imported C-error decay exponent', F(1, 4) + theta / 16,
          F(67, 160))
    equal('complete imported AB-error power', F(1, 4) - 1, -F(3, 4))

    # Main 8/3 improvement: retain the derivative-only 27/10 audit above,
    # then use the exact A/B chain allowed by Robert, Section 5.2.
    def A(pair):
        k, ell = pair
        return (k / (2 * k + 2), (k + ell + 1) / (2 * k + 2))

    def B(pair):
        k, ell = pair
        return (ell - F(1, 2), k + F(1, 2))

    pair = (F(0), F(1))
    chain = [
        ('B', (F(1, 2), F(1, 2))),
        ('A', (F(1, 6), F(2, 3))),
        ('A', (F(1, 14), F(11, 14))),
        ('B', (F(2, 7), F(4, 7))),
        ('A', (F(1, 9), F(13, 18))),
    ]
    for index, (operation, expected) in enumerate(chain, 1):
        pair = A(pair) if operation == 'A' else B(pair)
        equal('A/B exponent-pair chain step ' + str(index) + ' ' + operation,
              pair, expected)
        k, ell = pair
        if not (0 <= k <= F(1, 2) <= ell <= 1):
            raise AssertionError(('inadmissible pair coordinate range', pair))
        checks.append({'name': 'pair coordinate ranges step ' + str(index),
                       'kind': 'non_strict_bounds', 'value': str(pair)})

    main_theta = F(8, 3)
    main_switch = F(5, 13)
    main_polys = {
        'main_fourth_first': (F(1, 14), F(3, 14) - main_theta / 4, main_theta / 4),
        'main_fourth_second': (-F(1, 14), F(15, 28) - main_theta / 4, main_theta / 4),
        'main_new_pair': (F(1, 9), F(1, 9) - main_theta / 4, main_theta / 4),
        'main_pair_error': (-F(1), F(1, 2) - main_theta / 4, main_theta / 4),
    }
    main_endpoints = {
        'main_fourth_first': ((lo, F(0)), (main_switch, -F(2, 507))),
        'main_fourth_second': ((lo, -F(1, 16)), (main_switch, -F(47, 2028))),
        'main_new_pair': ((main_switch, -F(2, 507)), (hi, F(0))),
        'main_pair_error': ((main_switch, -F(979, 1014)), (hi, -F(11, 12))),
    }
    for name, poly in main_polys.items():
        equal(name + ' convexity coefficient', poly[2], F(2, 3))
        positive(name + ' strict convexity', poly[2])
        for beta, expected in main_endpoints[name]:
            equal(name + ' at beta=' + str(beta), value(poly, beta), expected)

    equal('new pair unweighted M power', pair[1] - pair[0], F(11, 18))
    equal('new pair weighted beta linear coefficient',
          pair[1] - pair[0] - F(1, 2), F(1, 9))
    main_crossover = tuple(a - b for a, b in zip(main_polys['main_fourth_first'],
                                                 main_polys['main_new_pair']))
    equal('main crossover factorization', main_crossover,
          (-F(5, 126), F(13, 126), F(0)))
    equal('main crossover at beta=5/13', value(main_crossover, main_switch), F(0))
    positive('main switch below fourth-secondary crossover', switch - main_switch)
    equal('fourth-secondary deficit at main switch',
          value(difference4, main_switch), -F(1, 52))
    equal('main low discrepancy threshold exponent',
          F(1, 2) + F(3, 16) * main_theta, F(1))
    equal('main low discrepancy margin per epsilon with delta<=epsilon/100',
          F(3, 32) - F(1, 100), F(67, 800))
    positive('main low discrepancy reserve above epsilon/16',
             F(3, 32) - F(1, 100) - F(1, 16))
    equal('main sigma threshold value', F(1, 2) + main_theta / 4, F(7, 6))
    positive('main sigma epsilon margin', F(1, 8) - F(1, 100))
    equal('main imported C-error decay exponent', F(1, 4) + main_theta / 16,
          F(5, 12))
    positive('new pair complete error below coarse -3/4 at both endpoints',
             -F(3, 4) - max(value(main_polys['main_pair_error'], main_switch),
                             value(main_polys['main_pair_error'], hi)))

    # Coarse rational consequences once a four-jet bound eta<=1/8 is proved.
    # For each Laguerre form, |linear perturbation|<=4 eta and
    # |quadratic perturbation|<=2 eta^2 using |sin|,|cos|<=1.
    eta = F(1, 8)
    equal('coarse Laguerre lower bound at eta=1/8', 1 - 4 * eta - 2 * eta ** 2,
          F(15, 32))
    positive('strict coarse Laguerre positivity', 1 - 4 * eta - 2 * eta ** 2)
    equal('coarse first-pair norm lower bound', 1 - 4 * eta, F(1, 2))
    equal('physical E lower coefficient in |Q| squared when omega>=1',
          4 * (1 - 4 * eta), F(2))

    root = Path(__file__).resolve().parents[1]
    source_names = [
        'numerics/check_hybrid_cutoff_lemma.py',
        'notes/19_OSCILLATORY_BLOCKS_AND_PAIRED_LAGUERRE_FORMS_20261014.md',
        'notes/30_THETA_SIGNED_CUTOFFS_AND_ANALYTIC_LOG_LOSS_20261014.md',
        'manuscript/quaternion_theta_geometry.tex',
    ]
    source_hashes = {name: sha256((root / name).read_bytes()).hexdigest()
                     for name in source_names}
    receipt = {
        'date': '2026-10-14',
        'date_timezone': 'America/New_York',
        'prepared_for': 'Edward Baker',
        'llm_assistance': 'Substantial',
        'recorded_parent_model': 'gpt-6-astra',
        'recorded_parent_reasoning_effort': 'ultra',
        'configuration_provenance': 'Parent verified current turn metadata; supplied to inherited subagent.',
        'status': 'PASS',
        'check_count': len(checks),
        'checks': checks,
        'source_sha256': source_hashes,
        'external_source': {
            'author': 'Olivier Robert',
            'title': "On van der Corput's k-th derivative test for exponential sums",
            'location': 'Theorems 2 and 3, printed p.8; exponent-pair definition and A/B closure, Section 5.2, printed pp.12-13',
            'url': 'https://perso.univ-st-etienne.fr/rool6510/robert-2015-indag.pdf',
            'verification': 'Read through the web tool on the dated research turn; no external PDF committed.',
        },
        'scope': 'Exact rational algebra and endpoint/margin checks only.',
        'limitations': [
            'Does not prove the imported third/fourth derivative tests or A/B exponent-pair closure.',
            'Does not certify infinite sums, analytic uniformity, or the four-jet approximation.',
            'Does not establish the full every-cutoff stationary relative-loss inequality.',
            'Does not evaluate an effective height or extend finite-height coverage.',
            'No numerical sweep, quadrature, or zero search was run.',
        ],
    }
    output = json.dumps(receipt, indent=2, sort_keys=True) + '\n'
    if args.output:
        args.output.write_text(output)
    print(json.dumps({'status': receipt['status'], 'check_count': len(checks),
                      'output': str(args.output) if args.output else None}, sort_keys=True))


if __name__ == '__main__':
    main()
