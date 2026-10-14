#!/usr/bin/env python3
"""Independent exact endpoint/coverage audit of the height-100--104 pilot.

Prepared for Edward Baker, 2026-10-14, with substantial LLM assistance.
Parent-verified model gpt-6-astra, reasoning effort ultra.
Uses only the Python standard library. This checks stored dyadic claims,
exact closed-cell coverage and source-file hashes. It does not recompute
quadrature, validate Arb itself, or prove the analytic tail lemmas.

Default source files are adjacent to the supplied certificate. Optional
source-path arguments support reviewing a staged certificate. A comparison
record can be supplied to verify a separate full numerical replay, with
only elapsed_seconds ignored.
"""
import argparse
from collections import Counter
from fractions import Fraction as Q
from functools import lru_cache
from hashlib import sha256
import json
from pathlib import Path
import platform


class Audit:
    def __init__(self):
        self.counts = Counter()
        self.classifications = Counter()

    def check(self, group, name, condition):
        self.counts[group] += 1
        if not condition:
            raise ValueError(name)


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def dyadic(pair):
    if not isinstance(pair, list) or len(pair) != 2:
        raise ValueError('Invalid dyadic endpoint')
    mantissa, exponent = pair
    if not isinstance(exponent, int) or abs(exponent) > 100000:
        raise ValueError('Invalid or excessive dyadic exponent')
    return Q(int(mantissa)) * Q(2) ** exponent


def interval(encoded):
    if not isinstance(encoded, list) or len(encoded) != 2:
        raise ValueError('Invalid interval')
    lo, hi = map(dyadic, encoded)
    if lo > hi:
        raise ValueError('Reversed interval')
    return lo, hi


def mul(a, b):
    products = [x*y for x in a for y in b]
    return min(products), max(products)


def add(a, b):
    return a[0]+b[0], a[1]+b[1]


def distance(a):
    return a[0] if a[0] > 0 else (-a[1] if a[1] < 0 else Q(0))


def squared_max(a):
    return max(abs(a[0]), abs(a[1])) ** 2


@lru_cache(maxsize=None)
def negative_exponential_lower(z):
    """Rational lower bound for exp(-z), z >= 0, by a positive Taylor tail.

    exp(z/128) is bounded above by its degree-32 Taylor polynomial plus
    the geometric bound starting at degree 33. Taking the 128th power
    preserves that upper bound; reciprocation gives the required lower.
    """
    s = z/128
    if z < 0 or s >= 1:
        raise ValueError('Unexpected exponential argument')
    total = term = Q(1)
    for k in range(1, 33):
        term *= s/k
        total += term
    first_omitted = term*s/33
    upper = total + first_omitted/(1-s/34)
    return 1/(upper**128)


def run(args, audit):
    record = json.loads(args.record.read_text())
    check = audit.check
    check('metadata', 'certificate schema', record['schema'] ==
          'inv21_phase_centered_complete_source_pilot_v1')
    check('metadata', 'status PASS', record['status'] == 'PASS')
    check('metadata', 'no failed cells', record['failed_cells'] == [])
    check('metadata', 'fixed claimed domain', record['domain'] ==
          {'x': ['100', '104'], 't': ['0', '1/2']})
    check('metadata', 'declared cone is 1/9', Q(record['B_squared_claim']) == Q(1, 9))
    check('metadata', 'exact partition parameters', record['width'] == '1'
          and record['time_slabs'] == 8)
    check('metadata', 'declared truncation parameters', record['N'] == 8
          and Q(record['U']) == Q(3, 2) and record['space_order'] == 12
          and record['time_order'] == 8)
    check('source_binding', 'expected imported source name',
          record['imported_source_name'] == 'check_shifted_contour_payments.py')
    driver = args.driver or args.record.parent / 'certify_phase_centered_residual.py'
    contour = args.contour_source or args.record.parent / record['imported_source_name']
    check('source_binding', 'driver source hash', digest(driver) == record['script_sha256'])
    check('source_binding', 'contour source hash', digest(contour) == record['imported_source_sha256'])
    cells = record['cells']
    check('coverage', 'exactly 32 cells', len(cells) == record['cell_count'] == 32)
    expected = {((str(x), str(x+1)), (str(Q(j, 16)), str(Q(j+1, 16))))
                for x in range(100, 104) for j in range(8)}
    actual = [(tuple(row['x']), tuple(row['t'])) for row in cells]
    check('coverage', 'complete exact rational Cartesian closed-cell cover',
          len(set(actual)) == 32 and set(actual) == expected)

    for i, row in enumerate(cells):
        energy = interval(row['energy_lower'])
        residual2 = interval(row['C2_upper'])
        mu = interval(row['Lambda'])
        slack = interval(row['residual_cone_margin'])
        jets = list(map(interval, row['whole_cell_jets']))
        residuals = list(map(interval, row['whole_cell_C']))
        check('cell_shape', f'cell {i} four jets and two residuals',
              len(jets) == 4 and len(residuals) == 2)
        check('cell_shape', f'cell {i} center jets through order 28',
              len(row['center_jets']) == 29)
        check('cone', f'cell {i} positive endpoint energy',
              energy[0] > 0 and energy[0] == energy[1])
        check('cone', f'cell {i} energy floor from jet endpoints',
              energy[1] <= distance(jets[0])**2 + distance(jets[1])**2)
        check('cone', f'cell {i} residual upper bound from endpoints',
              residual2[0] == residual2[1] and
              residual2[0] >= squared_max(residuals[0])+squared_max(residuals[1]))
        check('cone', f'cell {i} exact positive cone slack',
              slack[0] > 0 and slack[0] <= energy[0]/9-residual2[0] <= slack[1])
        check('cone', f'cell {i} squared residual ratio below 0.073',
              residual2[0] < Q(73, 1000)*energy[0])
        check('cone', f'cell {i} mu at least two fifths', mu[0] >= Q(2, 5))
        check('cone', f'cell {i} positive explicit center b', interval(row['b'])[0] > 0)
        xc = (Q(row['x'][0])+Q(row['x'][1]))/2
        dx = (Q(row['x'][1])-Q(row['x'][0]))/2
        # Classical rigorous pi < 22/7. The deliberately wider rational
        # bounds still suffice for both advertised global floors.
        physical_lower = energy[0]*negative_exponential_lower(Q(22, 7)*xc/4)
        normalized_lower = energy[0]*negative_exponential_lower(Q(22, 7)*dx/4)
        check('global_norm_floors', f'cell {i} physical norm greater than 4e-16',
              physical_lower > Q(4, 10**16)**2)
        check('global_norm_floors', f'cell {i} normalized squared norm greater than 2700',
              normalized_lower > 2700)
        check('metadata_consistency', f'cell {i} recorded flags',
              row['norm_positive'] is True and row['residual_inequality_pass'] is True
              and row['mu_at_least_two_fifths'] is True)
        check('cell_shape', f'cell {i} two stationary observations',
              len(row['stationary_classification']) == 2 and
              len(row['stationary_signed_form_enclosures']) == 2)
        for j, classification in enumerate(row['stationary_classification']):
            audit.classifications[f'{j}:{classification}'] += 1
            excluded = jets[j+1][0] > 0 or jets[j+1][1] < 0
            if classification == 'stationarity_excluded':
                check('stationarity', f'cell {i}, j={j}: actual exclusion', excluded)
            else:
                check('stationarity', f'cell {i}, j={j}: known classification',
                      classification == 'stationary_sign_certified_by_centered_identity')
                check('stationarity', f'cell {i}, j={j}: stationary condition retained', not excluded)
                signed = add(mul(mu, mul(jets[j], jets[j])), mul(jets[j], residuals[j]))
                check('stationarity', f'cell {i}, j={j}: independently computed rational margin',
                      signed[0] > 0)
                check('stationarity', f'cell {i}, j={j}: recorded positive margin',
                      interval(row['stationary_signed_form_enclosures'][j])[0] > 0)
    check('metadata_consistency', 'all observations resolved',
          record['all_stationary_observations_resolved'] is True)
    for key in ('complete_unscaled_index_payments', 'complete_unscaled_integration_payments',
                'complete_unscaled_moment_majorants'):
        check('cell_shape', f'{key}: orders zero through 29', len(record[key]) == 30)
        check('cell_shape', f'{key}: positive bounds',
              all(interval(value)[0] > 0 for value in record[key]))
    if args.compare_record is not None:
        comparison = json.loads(args.compare_record.read_text())
        original = dict(record)
        original.pop('elapsed_seconds', None)
        comparison.pop('elapsed_seconds', None)
        check('replay_comparison', 'independent results match except elapsed time', original == comparison)
    return {'driver_source_sha256': record['script_sha256'],
            'contour_source_sha256': record['imported_source_sha256']}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--record', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--driver', type=Path)
    parser.add_argument('--contour-source', type=Path)
    parser.add_argument('--compare-record', type=Path)
    args = parser.parse_args()
    audit = Audit()
    result = {
        'schema': 'inv21_theta_centered_residual_exact_record_audit_v1',
        'date': '2026-10-14', 'prepared_for': 'Edward Baker',
        'llm_assistance': 'Substantial', 'recorded_model': 'gpt-6-astra',
        'recorded_effort': 'ultra', 'python': platform.python_version(),
        'audit_source_name': Path(__file__).name,
        'audit_source_sha256': digest(Path(__file__)),
        'record_name': args.record.name, 'status': 'FAIL',
        'arithmetic': 'exact fractions.Fraction endpoint and interval comparisons',
        'scope': 'Record and source-hash audit; quadrature and analytic tail lemmas are not independently formalized.',
    }
    try:
        result['record_sha256'] = digest(args.record)
        result.update(run(args, audit))
        if args.compare_record is not None:
            result['compared_record_sha256'] = digest(args.compare_record)
            result['comparison_ignored_fields'] = ['elapsed_seconds']
        result['status'] = 'PASS'
    except Exception as exc:
        result['error'] = {'type': type(exc).__name__, 'message': str(exc)}
    result['checks_total'] = sum(audit.counts.values())
    result['checks_by_group'] = dict(sorted(audit.counts.items()))
    result['classification_counts'] = dict(sorted(audit.classifications.items()))
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))
    return 0 if result['status'] == 'PASS' else 1


if __name__ == '__main__':
    raise SystemExit(main())
