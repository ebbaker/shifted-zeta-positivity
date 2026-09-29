#!/usr/bin/env python3
"""Hash-bound comparison of the 80- and 120-digit geometry diagnostics."""
import argparse
from decimal import Decimal, localcontext, InvalidOperation
import hashlib
import json
from pathlib import Path


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    base = Path(__file__).resolve().parent
    parser.add_argument('--low', type=Path, default=base/'records'/'prime_jump_geometry_80_20260926.json')
    parser.add_argument('--high', type=Path, default=base/'records'/'prime_jump_geometry_120_20260926.json')
    parser.add_argument('--operator-numerics', type=Path,
                        default=base.parent.parent/'ccm-operator-realizations'/'numerics')
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    for path in (args.low, args.high):
        if not path.is_file():
            parser.error(f'Missing {path}. Regenerate with check_prime_jump_geometry.py; see README.md.')
    low, high = json.loads(args.low.read_text()), json.loads(args.high.read_text())
    sources = {'check_prime_jump_geometry.py':digest(base/'check_prime_jump_geometry.py'),
               'check_mass_stiffness.py':digest(args.operator_numerics/'check_mass_stiffness.py')}
    if low['sources_sha256'] != sources or high['sources_sha256'] != sources:
        parser.error('Generator source hash mismatch. Preserve historical files and regenerate both records with current sources.')
    if [low['decimal_digits'], high['decimal_digits']] != [80,120]:
        parser.error('Expected independent 80- and 120-digit records.')
    ignored = {'checks','controls','maximum_control_residual','selected_direct_weil_entry_error'}
    diagnostics = []
    discrete_count = 0

    def compare(a, b, path):
        nonlocal discrete_count
        if isinstance(a, dict):
            if a.keys() != b.keys():
                raise AssertionError(f'Structure mismatch at {path}')
            for key in a:
                if key not in ignored:
                    compare(a[key], b[key], f'{path}.{key}')
        elif isinstance(a, list):
            assert len(a) == len(b), path
            for j, (x,y) in enumerate(zip(a,b)):
                compare(x,y,f'{path}[{j}]')
        else:
            try:
                if not isinstance(a, str):
                    raise InvalidOperation
                x, y = Decimal(a), Decimal(b)
            except InvalidOperation:
                assert a == b, path
                discrete_count += 1
                return
            with localcontext() as ctx:
                ctx.prec = 80
                error = abs(x-y)/max(abs(x),abs(y)) if x or y else Decimal(0)
                diagnostics.append((error, path))
                assert error < Decimal('1e-25'), (path, error)

    for key in ('X','L','prime_power_terms','cases','cutoff_comparisons',
                'harmonic_composition_relative_defect','folding_witness','zero_data_used'):
        compare(low[key], high[key], key)
    worst = max(diagnostics)
    result = dict(schema=1,date='2026-09-26',
                  status='Relative agreement at 25 decimal digits; not interval certification',
                  comparator_sha256=digest(Path(__file__)), sources_sha256=sources,
                  input_sha256={args.low.name:digest(args.low),args.high.name:digest(args.high)},
                  decimal_digits=[80,120],relative_tolerance='1e-25',
                  numerical_observables=len(diagnostics),discrete_observables=discrete_count,
                  maximum_relative_difference=str(worst[0]),worst_observable=worst[1],
                  all_checks_passed=True)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__ == '__main__':
    main()
