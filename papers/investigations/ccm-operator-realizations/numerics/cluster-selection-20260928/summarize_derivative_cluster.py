#!/usr/bin/env python3
"""Check retained precision, source hashes, and summarize the bounded cluster run.

GPT-6 (Codex), 2026-09-28; serving variant and effort not exposed.
Standard-library only. No new numerical operator calculation is performed.
"""
import argparse
from decimal import Decimal, localcontext
import hashlib
import json
from pathlib import Path


def differences(a, b, path=''):
    # Rounding error checks vary with working precision by design.
    if path.endswith('/checks') or path == '/digits':
        return []
    if type(a) is not type(b):
        return [path]
    if isinstance(a, dict):
        if a.keys() != b.keys():
            return [path + '/keys']
        return sum((differences(a[k], b[k], path + '/' + k) for k in a), [])
    if isinstance(a, list):
        if len(a) != len(b):
            return [path + '/length']
        return sum((differences(x, y, path + '/' + str(i))
                    for i, (x, y) in enumerate(zip(a, b))), [])
    return [] if a == b else [path]


def main():
    here = Path(__file__).resolve().parent
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--record-a', type=Path, default=here/'derivative-cluster-130.json')
    p.add_argument('--record-b', type=Path, default=here/'derivative-cluster-160.json')
    p.add_argument('--repo-numerics', type=Path, default=here)
    p.add_argument('--output', type=Path, default=here/'derivative-cluster-summary.json')
    args = p.parse_args()
    a, b = (json.loads(path.read_text()) for path in (args.record_a, args.record_b))
    diff = differences(a, b)
    verified = {}
    for name, expected in b['source_hashes'].items():
        source = here/name if name == 'check_derivative_cluster.py' else args.repo_numerics/name
        actual = hashlib.sha256(source.read_bytes()).hexdigest()
        verified[name] = dict(expected=expected, actual=actual, match=actual == expected)
    rows = []
    with localcontext() as ctx:
        ctx.prec = 100
        for case in b['cases']:
            theta = Decimal(case['harmonic_ritz_eigenvalues'][0])
            delta = Decimal(case['complement_min_eigenvalue'])
            eigen = Decimal(case['actual_even_ground'])
            lower = theta * delta / (delta + theta)
            rows.append(dict(N=case['N'], trial_dimension=case['trial_dimension'],
                harmonic_theta=str(theta), observed_delta=str(delta),
                conditional_eigenvalue_lower_bound=str(lower),
                actual_ground_in_conditional_interval=lower <= eigen <= theta,
                conditional_relative_bracket_width=str(theta/(delta+theta)),
                observed_relative_eigenvalue_error=str(theta/eigen-1),
                xi_distance=case['base_profile']['distance_true_ground'],
                plain_ritz_distance=case['trial_ritz_profile']['distance_true_ground'],
                best_projection_distance=case['best_ground_projection_distance'],
                ordinary_schur_lift_distance=case['schur_plain_lifted_profile']['distance_true_ground'],
                generalized_harmonic_lift_distance=case['harmonic_ritz_profile']['distance_true_ground'],
                cancellation_decimal_digits=case['cancellation_decimal_digits']))
    result = dict(date='2026-09-28', model='GPT-6 (Codex)',
        exact_serving_variant='not exposed', reasoning_effort='not exposed',
        status='multiprecision diagnostic comparison; not interval certification',
        compared_digits=[a['digits'], b['digits']],
        serializer_significant_digits=45,
        exact_match_except_precision_and_roundoff_checks=not diff,
        differing_paths=diff, source_hash_verification=verified,
        bound_scope='Algebraic bound assumes A is positive semidefinite and D >= delta I > 0. Here these hypotheses are only observed in finite floating calculations.',
        cases=rows)
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))
    if diff or not all(item['match'] for item in verified.values()):
        raise SystemExit('Precision comparison or source verification failed')


if __name__ == '__main__':
    main()
