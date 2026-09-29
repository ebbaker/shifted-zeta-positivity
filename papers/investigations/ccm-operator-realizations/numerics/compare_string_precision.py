#!/usr/bin/env python3
"""Compare compact string records and fail closed on stale source hashes.

This compares saved observables, not error estimates or rigorous enclosures.
It uses only the Python standard library.
"""
import argparse
from decimal import Decimal, InvalidOperation, localcontext
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def checked_record(path):
    if not path.is_file():
        raise FileNotFoundError(f'{path}: regenerate using check_string_realization.py; see numerics/README.md')
    value = json.loads(path.read_text())
    for name in ('check_string_realization.py', 'check_mass_stiffness.py'):
        if value['sources_sha256'].get(name) != digest(HERE/name):
            raise ValueError(f'{path}: stale source hash for {name}; regenerate the record.')
    return value


def compare(a, b, path, differences, counts):
    if isinstance(a, dict):
        if set(a) != set(b):
            raise ValueError(f'Key mismatch at {path}')
        for key in a:
            if key not in ('checks', 'positive_one_mass_string_checks'):
                compare(a[key], b[key], f'{path}/{key}', differences, counts)
    elif isinstance(a, list):
        if len(a) != len(b):
            raise ValueError(f'Length mismatch at {path}')
        for i, (x, y) in enumerate(zip(a, b)):
            compare(x, y, f'{path}/{i}', differences, counts)
    elif isinstance(a, str):
        try:
            x, y = Decimal(a), Decimal(b)
        except InvalidOperation:
            if a != b:
                raise ValueError(f'Label mismatch at {path}')
            return
        if not x.is_finite() or not y.is_finite():
            raise ValueError(f'Nonfinite observation at {path}')
        counts['numeric_observables'] += 1
        error = abs(x-y)/max(Decimal(1), abs(x), abs(y))
        counts['maximum_scaled_difference'] = max(counts['maximum_scaled_difference'], error)
        if a != b:
            differences.append(dict(path=path, low=a, high=b, scaled_difference=str(error)))
    elif a != b:
        raise ValueError(f'Discrete observation mismatch at {path}')


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--low', type=Path, default=HERE/'records'/'string_realization_120_20260926.json')
    p.add_argument('--high', type=Path, default=HERE/'records'/'string_realization_160_20260926.json')
    p.add_argument('--output', type=Path, default=HERE/'records'/'string_precision_comparison_20260926.json')
    args = p.parse_args()
    low, high = checked_record(args.low), checked_record(args.high)
    counts = dict(numeric_observables=0, maximum_scaled_difference=Decimal(0))
    differences = []
    with localcontext() as ctx:
        ctx.prec = 80
        for key in ('cases','cutoff_comparisons','controls'):
            compare(low[key], high[key], key, differences, counts)
    if counts['maximum_scaled_difference'] > Decimal('1e-43'):
        raise ArithmeticError('Saved observables fail the 1e-43 scaled comparison.')
    report = dict(date='2026-09-26', status='precision comparison, not an interval certificate',
                  comparison_source_sha256=digest(Path(__file__)),
                  input_sha256={args.low.name:digest(args.low), args.high.name:digest(args.high)},
                  generator_hashes_verified=True,
                  low_decimal_digits=low['decimal_digits'], high_decimal_digits=high['decimal_digits'],
                  numeric_observables=counts['numeric_observables'],
                  identical_at_all_45_saved_significant_digits=not differences,
                  maximum_scaled_difference=str(counts['maximum_scaled_difference']),
                  maximum_scaled_residual_low=low['maximum_scaled_residual'],
                  maximum_scaled_residual_high=high['maximum_scaled_residual'],
                  differing_saved_observables=differences)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
