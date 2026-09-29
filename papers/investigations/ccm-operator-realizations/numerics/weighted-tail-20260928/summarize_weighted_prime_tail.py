#!/usr/bin/env python3
"""Verify the bounded weighted-tail records; standard-library only.

GPT-6 (Codex), 2026-09-28; serving variant and effort not exposed.
"""
import argparse
from decimal import Decimal
import hashlib
import json
from pathlib import Path


def differences(a, b, path=''):
    if path.endswith('/checks') or path == '/digits':
        return []
    if type(a) is not type(b):
        return [path]
    if isinstance(a, dict):
        if a.keys() != b.keys():
            return [path+'/keys']
        return sum((differences(a[k], b[k], path+'/'+k) for k in a), [])
    if isinstance(a, list):
        if len(a) != len(b):
            return [path+'/length']
        return sum((differences(x, y, path+'/'+str(i))
                    for i, (x, y) in enumerate(zip(a, b))), [])
    return [] if a == b else [path]


if __name__ == '__main__':
    here = Path(__file__).resolve().parent
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--record-a', type=Path, default=here/'weighted-prime-tail-80.json')
    p.add_argument('--record-b', type=Path, default=here/'weighted-prime-tail-110.json')
    p.add_argument('--output', type=Path, default=here/'weighted-prime-tail-summary.json')
    args = p.parse_args()
    for path in (args.record_a, args.record_b):
        if not path.is_file():
            raise SystemExit(f'Missing record {path}; regenerate with check_weighted_prime_tail.py --digits 80 or 110 --output PATH (see README.md).')
    source_hash = hashlib.sha256((here/'check_weighted_prime_tail.py').read_bytes()).hexdigest()
    a, b = (json.loads(path.read_text()) for path in (args.record_a, args.record_b))
    if not source_hash == a.get('source_sha256') == b.get('source_sha256'):
        raise SystemExit('Generator source hash mismatch; regenerate both records with the current check_weighted_prime_tail.py (see README.md).')
    diff = differences(a, b)
    maxima = {str(record['digits']): {key: str(max(Decimal(case['checks'][key])
              for case in record['cases'])) for key in record['cases'][0]['checks']}
              for record in (a, b)}
    result = dict(date='2026-09-28', model='GPT-6 (Codex)',
        exact_serving_variant='not exposed', reasoning_effort='not exposed',
        status='Floating diagnostic verification; not interval certification',
        compared_digits=[a['digits'], b['digits']], serializer_significant_digits=45,
        exact_observable_match_excluding_precision_and_roundoff_checks=not diff,
        differing_paths=diff, source_sha256=source_hash,
        source_hash_matches_both_runs=source_hash == a['source_sha256'] == b['source_sha256'],
        all_observed_errors_below_floating_envelope_bound=all(
            row['observed_error_within_floating_bound'] for row in b['cases']),
        largest_consistency_errors=maxima,
        core_windows=b['core_windows'],
        cases=[{key: row[key] for key in ('X', 'T', 'prime_power_count',
            'complete_prime_power_rate', 'continuum_rate', 'prime_rate_minus_continuum',
            'finite_interval_relative_PNT_envelope', 'conditional_error_bound',
            'bound_over_observed_absolute_error', 'lower_rate_from_finite_envelope')}
            for row in b['cases']])
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))
    if diff or not result['source_hash_matches_both_runs'] or not result['all_observed_errors_below_floating_envelope_bound']:
        raise SystemExit('Precision comparison or source verification failed')
