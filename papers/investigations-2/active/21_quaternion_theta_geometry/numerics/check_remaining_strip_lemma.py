#!/usr/bin/env python3
"""Exact rational checks for the closed outer threshold 61/24.

Prepared for Edward Baker, 14 October 2026 (America/New_York), with
substantial LLM assistance. Recorded parent model: gpt-6-astra; effort:
ultra, verified by the parent from current turn metadata. This subagent's
separate runtime metadata was not independently inspected.

This finite audit checks exponent-pair identities, convex endpoint margins,
fixed perturbation budgets, and explicit limitations of the selected bounds.
It does not prove imported exponent-pair theorems, infinite analytic bounds,
or physical theta signs. No height sweep or numerical certificate is made.
The deterministic JSON receipt contains no wall-clock-dependent fields.
"""

import argparse
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path


def A(pair):
    k, ell = pair
    return k / (2 * k + 2), (k + ell + 1) / (2 * k + 2)


def exponent(pair, beta, theta):
    """Weighted exponent before eta, real-part, or endpoint perturbations."""
    k, ell = pair
    return k + (ell - k - F(1, 2)) * beta - theta * beta * (1 - beta) / 4


def canonical(value):
    if isinstance(value, F):
        return str(value)
    if isinstance(value, (tuple, list)):
        return [canonical(v) for v in value]
    if isinstance(value, dict):
        return {k: canonical(v) for k, v in value.items()}
    return value


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    checks = []

    def equal(name, value, expected):
        if value != expected:
            raise AssertionError((name, value, expected))
        checks.append({'name': name, 'kind': 'equality', 'value': canonical(value)})

    def positive(name, value):
        if value <= 0:
            raise AssertionError((name, value))
        checks.append({'name': name, 'kind': 'strict_positive', 'value': str(value)})

    def nonnegative(name, value):
        if value < 0:
            raise AssertionError((name, value))
        checks.append({'name': name, 'kind': 'nonnegative', 'value': str(value)})

    theta = F(61, 24)
    eta = delta = theta_loss = endpoint_allowance = F(1, 100000)
    final_decay = F(1, 20000)
    P = (F(13, 84), F(55, 84))
    AP = (F(13, 194), F(76, 97))
    AAP = (F(13, 414), F(359, 414))
    TY1 = (F(4742, 38463), F(35731, 51284))
    TY2 = (F(18, 199), F(593, 796))
    TY3 = (F(2779, 38033), F(58699, 76066))
    TY4 = (F(715, 10238), F(7955, 10238))
    equal('A(P) exact pair', A(P), AP)
    equal('A^2(P) exact pair', A(AP), AAP)

    # Starting with P+(eta,eta) yields transforms no larger componentwise
    # than AP+(eta,eta), AAP+(eta,eta). The source permits every eta>0.
    Peta = tuple(v + eta for v in P)
    for name, actual, target in [('AP', A(Peta), AP),
                                 ('AAP', A(A(Peta)), AAP)]:
        for coordinate in (0, 1):
            positive(name + ' eta allowance coordinate ' + str(coordinate),
                     target[coordinate] + eta - actual[coordinate])

    partitions = [
        ('AAP', AAP, F(1, 5), F(3, 10),
         (-F(43, 13800), -F(869, 662400))),
        ('AP', AP, F(3, 10), F(3, 8),
         (-F(459, 310400), -F(145, 198656))),
        ('TY2', TY2, F(3, 8), F(81, 200),
         (-F(215, 407552), -F(21807, 254720000))),
        ('TY1', TY1, F(81, 200), F(3, 7),
         (-F(4368359, 49232640000), -F(1, 1176))),
        ('P', P, F(3, 7), F(1, 2),
         (-F(1, 1176), -F(11, 2688))),
    ]
    margins = []
    for i, (name, pair, left, right, expected) in enumerate(partitions):
        positive(name + ' interval length', right - left)
        if i:
            equal(name + ' adjacent intervals meet', left, partitions[i - 1][3])
        positive(name + ' convex quadratic coefficient', theta / 4)
        for beta, value in zip((left, right), expected):
            actual = exponent(pair, beta, theta)
            equal(name + ' endpoint beta=' + str(beta), actual, value)
            positive(name + ' strict endpoint decay beta=' + str(beta), -actual)
            margins.append(-actual)
    base_margin = min(margins)
    equal('smallest principal endpoint margin', base_margin, F(21807, 254720000))
    equal('Bourgain endpoint theta=5/2 still has saving',
          exponent(P, F(1, 2), F(5, 2)), -F(1, 672))

    # Each base exponent is convex on its stated interval. Adding eta to
    # both pair coordinates costs eta exactly. The real-part error costs
    # <=delta/2; losing theta_loss costs <=theta_loss/16 on [1/5,1/2].
    equal('equal pair-coordinate perturbation costs eta',
          exponent(Peta, F(2, 5), theta) - exponent(P, F(2, 5), theta), eta)
    perturbation = eta + delta / 2 + theta_loss / 16 + endpoint_allowance
    equal('total allocated exponent perturbation', perturbation, F(41, 1600000))
    positive('reserve after perturbations and final decay',
             base_margin - perturbation - final_decay)

    # For the last pair, E(beta)=13/84-theta*beta*(1-beta)/4.
    # On 1/2 <= beta <= 1/2+1/100000, its increment is at most
    # theta*1e-10/4. This is far below the reserved endpoint allowance.
    beta_excess = F(1, 100000)
    equal('last-pair endpoint extension increment',
          exponent(P, F(1, 2) + beta_excess, theta)
          - exponent(P, F(1, 2), theta), theta * beta_excess ** 2 / 4)
    positive('endpoint extension allowance suffices',
             endpoint_allowance - theta * beta_excess ** 2 / 4 - delta * beta_excess)

    # sigma >= 1/2+theta_u/4-delta and theta_u >= theta-theta_loss.
    # For n<=exp(ell/5), the low heat discrepancy is absolutely dominated
    # with exponent 1/2+theta_u/5-delta.
    low_base = F(1, 2) + theta / 5
    equal('unperturbed low discrepancy exponent', low_base, F(121, 120))
    low_perturbed = low_base - theta_loss / 5 - delta
    positive('low discrepancy margin above 1+1/240',
             low_perturbed - 1 - F(1, 240))
    sigma = F(1, 2) + (theta - theta_loss) / 4 - delta
    positive('carrier real part exceeds 9/8', sigma - F(9, 8))
    equal('ordinary zeta tail decay at low cutoff',
          F(1, 5) * (F(9, 8) - 1), F(1, 40))
    positive('imported complete C error decays faster than u^-2/5',
             F(1, 4) + (theta - theta_loss) / 16 - F(2, 5))
    equal('imported complete AB-error exponent', F(1, 4) - 1, -F(3, 4))
    positive('theta boundary exceeds target lower boundary', theta - F(5, 2))
    positive('theta boundary improves preceding 8/3', F(8, 3) - theta)
    equal('width of unresolved lower interval', theta - F(5, 2), F(1, 24))

    # These are failures of selected upper bounds, not positive lower
    # bounds on actual sums and not a disproof of theta positivity.
    selected_pairs = {'P': P, 'AP': AP, 'AAP': AAP,
                      'TY1': TY1, 'TY2': TY2, 'TY3': TY3, 'TY4': TY4}
    witnesses = {}
    for name, pair in selected_pairs.items():
        e = exponent(pair, F(2, 5), F(5, 2))
        positive('theta=5/2 selected bound fails at beta=2/5: ' + name, e)
        witnesses[name] = e
    equal('best selected bound failure at theta=5/2 beta=2/5',
          min(witnesses.values()), F(9, 3980))

    # The two near-bottleneck source pairs cross at this exact beta.
    slope = lambda pair: pair[1] - pair[0] - F(1, 2)
    crossing = (TY1[0] - TY2[0]) / (slope(TY2) - slope(TY1))
    equal('TY1/TY2 principal crossover beta', crossing, F(62831, 155153))
    equal('TY1/TY2 crossover exponent identity',
          exponent(TY1, crossing, theta), exponent(TY2, crossing, theta))
    threshold = 4 * (TY2[0] + slope(TY2) * crossing) / (crossing * (1 - crossing))
    equal('threshold at this selected-pair crossover',
          threshold, F(4911678521, 1933561194))
    positive('61/24 clears selected-pair crossover', theta - threshold)
    positive('127/50 does not clear selected-pair crossover', threshold - F(127, 50))
    for name, pair in selected_pairs.items():
        positive('theta=127/50 selected bound fails at crossover: ' + name,
                 exponent(pair, crossing, F(127, 50)))

    # Conditional bridge: the new power-saving hypothesis is needed only
    # in a fixed overlapping middle window, not at every frequency scale.
    # No assertion that this middle-window hypothesis is proved is made.
    conditional_theta = F(5, 2)
    conditional_low = F(19, 100)
    conditional_window = (F(7, 25), F(47, 100))
    equal('conditional low discrepancy exponent at theta=5/2',
          F(1, 2) + conditional_theta * (1 - conditional_low) / 4,
          F(161, 160))
    positive('conditional low discrepancy margin above one', F(161, 160) - 1)
    conditional_endpoints = [
        ('AAP', AAP, F(19, 100), -F(3293, 3312000)),
        ('AAP', AAP, F(2, 7), -F(1, 4508)),
        ('P', P, F(23, 50), -F(41, 84000)),
        ('P', P, F(1, 2), -F(1, 672)),
    ]
    for name, pair, beta, expected in conditional_endpoints:
        actual = exponent(pair, beta, conditional_theta)
        equal('conditional outer window ' + name + ' beta=' + str(beta),
              actual, expected)
        positive('conditional outer window endpoint margin ' + name + ' beta=' + str(beta),
                 -actual)
    equal('conditional lower overlap width',
          F(2, 7) - conditional_window[0], F(1, 175))
    equal('conditional upper overlap width',
          conditional_window[1] - F(23, 50), F(1, 100))
    positive('conditional lower overlap is nonempty', F(1, 175))
    positive('conditional upper overlap is nonempty', F(1, 100))
    # Hypothesis exponent is beta/2+(5/8)beta(1-beta)-kappa.
    # Subtracting physical amplitude beta/2+(theta/4)beta(1-beta)
    # at theta=5/2 cancels both beta coefficients and leaves -kappa.
    equal('conditional middle beta coefficient cancels',
          F(1, 2) + F(5, 8) - F(1, 2) - conditional_theta / 4, F(0))
    equal('conditional middle beta^2 coefficient cancels',
          -F(5, 8) + conditional_theta / 4, F(0))

    # A coarse geometric jet margin suffices when normalized errors <=1/8.
    # Note 31's sharper retained-square estimate is not needed here.
    err = F(1, 8)
    equal('normalized Laguerre lower bound coarse form',
          1 - 4 * err - 2 * err ** 2, F(15, 32))
    positive('normalized Laguerre sign margin', 1 - 4 * err - 2 * err ** 2)
    equal('fourfold jet-scale coarse Laguerre lower bound',
          4 * (1 - 4 * err - 2 * err ** 2), F(15, 8))
    positive('3/2 is a strict upper bound for sqrt(2)', F(9, 4) - 2)
    positive('normalized energy exceeds 1/2 with omega>=1', 1 - 3 * err - F(1, 2))

    this = Path(__file__).resolve()
    inv = this.parent.parent
    inputs = [this, inv / 'notes/19_OSCILLATORY_BLOCKS_AND_PAIRED_LAGUERRE_FORMS_20261014.md',
              inv / 'notes/31_SIGNED_CUTOFF_LEMMA_AND_THRESHOLD_EIGHT_THIRDS_20261014.md']
    hashes = {str(p.relative_to(inv)): {'sha256': sha256(p.read_bytes()).hexdigest(),
                                       'bytes': p.stat().st_size} for p in inputs}
    payload = {
        'record_type': 'finite_exact_rational_audit_not_height_certificate',
        'prepared_for': 'Edward Baker',
        'date': '2026-10-14',
        'date_timezone': 'America/New_York',
        'llm_assistance': 'substantial',
        'recorded_parent_model': 'gpt-6-astra',
        'recorded_parent_reasoning_effort': 'ultra',
        'parent_metadata_verification': 'parent inspected current source turn metadata',
        'parent_turn_id': '01a13d9a-fea1-7af1-9ca6-51d8429ae89a',
        'separate_subagent_runtime_metadata': 'not independently inspected',
        'external_sources': [
            {'url': 'https://arxiv.org/pdf/1408.5794',
             'version': '1408.5794v2', 'result': 'Bourgain Theorem 6'},
            {'url': 'https://arxiv.org/pdf/2306.05599',
             'version': '2306.05599v3',
             'result': 'Trudgian-Yang definition (1.1)-(1.2), Lemma 1.1, A process (1.10)'}],
        'theta_closed_boundary': str(theta),
        'high_block_decay_after_perturbations': str(final_decay),
        'parameters': canonical({'eta': eta, 'delta_cap': delta,
                                 'theta_loss_cap': theta_loss,
                                 'endpoint_allowance': endpoint_allowance,
                                 'partitions': partitions}),
        'failed_selected_bound_witnesses_at_theta_5_over_2_beta_2_over_5': canonical(witnesses),
        'conditional_full_strip_bridge': {
            'status': 'conditional; middle-window power-saving hypothesis is not proved',
            'theta_closed_lower_boundary': '5/2',
            'beta_window': canonical(conditional_window),
            'required_hypothesis': 'sup_I |sum_{n in I} n^{-iT}| <= C T^{beta/2+(5/8)beta(1-beta)-kappa}, kappa>0',
            'beta_definition': 'log(M)/log(T)',
            'outside_window_endpoint_checks': canonical(conditional_endpoints),
        },
        'scope': [
            'Exact endpoint arithmetic plus convexity verifies the stated five-piece exponent bound.',
            'The external exponent-pair theorems and analytic transfer are not proved by this script.',
            'Positive exponents at theta=5/2 diagnose failure of selected upper estimates only.',
            'No mathematical impossibility claim is made about the unresolved lower strip.',
            'No quadrature, height sweep, zero search, or finite-height certificate is performed.'],
        'source_hashes': hashes,
        'check_count': len(checks),
        'all_checks_passed': True,
        'checks': checks,
    }
    encoded = json.dumps(payload, indent=2, sort_keys=True) + '\n'
    if args.output:
        args.output.write_text(encoded)
    else:
        print(encoded, end='')


if __name__ == '__main__':
    main()
