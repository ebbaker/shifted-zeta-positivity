#!/usr/bin/env python3
"""Hash-check and compare energy-port records, using only the standard library."""
import argparse
from decimal import Decimal, InvalidOperation, localcontext
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCES = ('check_energy_ports.py','check_mass_stiffness.py','check_string_realization.py')


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_record(path):
    if not path.is_file():
        raise FileNotFoundError(f'{path}: regenerate with check_energy_ports.py; see numerics/README.md.')
    data = json.loads(path.read_text())
    if set(data['sources_sha256']) != set(SOURCES):
        raise ValueError('Unexpected generator source manifest.')
    for name in SOURCES:
        if data['sources_sha256'][name] != digest(HERE/name):
            raise ValueError(f'{path}: stale source hash for {name}; regenerate.')
    return data


def compare(a, b, path, counts, differences):
    if type(a) is not type(b):
        raise ValueError(f'Type mismatch at {path}')
    if isinstance(a, dict):
        if set(a) != set(b):
            raise ValueError(f'Keys differ at {path}')
        for key in a:
            if key == 'checks' or key.endswith('_checks'):
                continue
            compare(a[key],b[key],path+'/'+key,counts,differences)
    elif isinstance(a, list):
        if len(a) != len(b):
            raise ValueError(f'Lengths differ at {path}')
        for j,(x,y) in enumerate(zip(a,b)):
            compare(x,y,path+'/'+str(j),counts,differences)
    elif isinstance(a, str):
        try:
            x,y = Decimal(a),Decimal(b)
        except InvalidOperation:
            if a != b:
                raise ValueError(f'Labels differ at {path}')
            return
        if not x.is_finite() or not y.is_finite():
            raise ValueError(f'Nonfinite observable at {path}')
        counts['numeric_observables'] += 1
        error = abs(x-y)/max(Decimal(1),abs(x),abs(y))
        counts['maximum_scaled_difference'] = max(counts['maximum_scaled_difference'],error)
        if a != b:
            differences.append(dict(path=path,low=a,high=b,scaled_difference=str(error)))
    elif a != b:
        raise ValueError(f'Discrete observable differs at {path}')


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--low',type=Path,default=HERE/'records'/'energy_ports_120_20260926.json')
    parser.add_argument('--high',type=Path,default=HERE/'records'/'energy_ports_160_20260926.json')
    parser.add_argument('--output',type=Path,default=HERE/'records'/'energy_port_precision_comparison_20260926.json')
    args=parser.parse_args()
    low,high=load_record(args.low),load_record(args.high)
    counts=dict(numeric_observables=0,maximum_scaled_difference=Decimal(0))
    differences=[]
    with localcontext() as ctx:
        ctx.prec=100
        for key in ('X','normalization','smooth_profile','zero_data_used','cases','controls'):
            compare(low[key],high[key],key,counts,differences)
    if counts['maximum_scaled_difference']>Decimal('1e-43'):
        raise ArithmeticError('Precision comparison fails the 1e-43 scaled tolerance.')
    report=dict(date='2026-09-26',status='precision comparison; not interval certification',
        comparison_source_sha256=digest(Path(__file__)),
        input_sha256={args.low.name:digest(args.low),args.high.name:digest(args.high)},
        generator_hashes_verified=True,low_decimal_digits=low['decimal_digits'],
        high_decimal_digits=high['decimal_digits'],numeric_observables=counts['numeric_observables'],
        identical_at_all_45_saved_significant_digits=not differences,
        maximum_scaled_difference=str(counts['maximum_scaled_difference']),
        maximum_scaled_residual_low=low['maximum_scaled_residual'],
        maximum_scaled_residual_high=high['maximum_scaled_residual'],
        differing_saved_observables=differences)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__=='__main__':
    main()
