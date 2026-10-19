#!/usr/bin/env python3
"""Portable S02 matched-correction mechanism guards; no coverage claim.

Prepared for Edward Baker, 19 October 2026, with substantial LLM assistance.
Authoring model gpt-6.1-sol, actual effort ultra. Same-model internal audit.
Requires python-flint 0.9.0. Independent source controls are recorded separately.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import platform
import sys

import flint
from flint import arb, acb, acb_series, ctx


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, required=True)
    parser.add_argument('--comparison-script', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--execution-model', required=True)
    parser.add_argument('--execution-effort', required=True)
    args = parser.parse_args()
    repo = args.repo.resolve()
    mainpath = args.comparison_script.resolve()
    comparison = load('s02_main_guard_audit', mainpath)
    opening_path = repo/comparison.S02/'numerics/check_cutoff_reflection.py'
    s = load('s02_opening_guard_audit', opening_path)
    ctx.prec = 256
    checks = comparison.algebra_checks(s)
    cases = []
    for X in [arb(1000), arb(1018)]:
        t = arb(21)/200
        k = arb.pi()/8
        z = acb_series([acb(X), acb(1)], 3)
        a = s.normalizer(z, t)
        b, bp = comparison.logA_jets(s, X, t)
        b_ref = a[1]/a[0]
        bp_ref = 2*a[2]/a[0]-b_ref*b_ref
        comparison.check((b_ref-b).contains(0),
                         'b versus analytic normalizer derivative')
        comparison.check((bp_ref-bp).contains(0),
                         'bp versus analytic normalizer derivative')
        C = s.correction(acb(X), t, 8)
        f = C*(-k*(z-X)).exp()/a
        c = C/a[0]
        omitted_b_rejected = not (f[1]+k*c).contains(0)
        omitted_b_and_bp_rejected = not (2*f[2]-k*k*c).contains(0)
        comparison.check(omitted_b_rejected and omitted_b_and_bp_rejected,
                         'normalizer-omission mutation not detected')
        # An arbitrary analytic Q residual independently tests physical return.
        r = acb_series([acb(2), acb(3), acb(5)], 3)
        physical = a*r
        e0 = physical[0]/a[0]
        e1 = physical[1]/a[0]
        e2 = 2*physical[2]/a[0]
        comparison.check((e1-r[1]-b*r[0]).contains(0),
                         'physical first return')
        comparison.check((e2-2*r[2]-2*b*r[1]-(b*b+bp)*r[0]).contains(0),
                         'physical second return')
        comparison.check((e1+k*e0-r[1]-(b+k)*r[0]).contains(0),
                         'demodulated first return')
        comparison.check((e2+2*k*e1+k*k*e0-2*r[2]-2*(b+k)*r[1]
                          -((b+k)**2+bp)*r[0]).contains(0),
                         'demodulated second return')
        cases.append({'center': str(X), 'b': str(b), 'bp': str(bp),
                      'abs_b_plus_k': str(abs(b+k)),
                      'normalizer_log_derivatives_verified': True,
                      'omitted_normalizer_first_rejected': omitted_b_rejected,
                      'omitted_normalizer_second_rejected': omitted_b_and_bp_rejected,
                      'physical_and_demodulated_chain_rule_verified': True})
    rejected = []
    fixtures = [
        ('changed_domain', lambda: comparison.compare(s, 999, 1002, 4, 24, 8, False)),
        ('changed_grid', lambda: comparison.compare(s, 999, 1001, 4, 25, 8, False)),
        ('changed_crossing_flag', lambda: comparison.compare(s, 999, 1001, 4, 24, 8, True)),
        ('changed_radius', lambda: comparison.edge_payment(
            s, 1017, 1019, arb(2), arb(1), arb(1), comparison.F(1))),
        ('non_crossing_edge_domain', lambda: comparison.edge_payment(
            s, 999, 1001, arb(2), arb(1), arb(1))),
    ]
    for name, fixture in fixtures:
        try:
            fixture()
        except ArithmeticError as exc:
            rejected.append({'case': name, 'rejected': True, 'reason': str(exc)})
        else:
            raise ArithmeticError('failed mutation rejection: '+name)
    report = {
        'schema': 's02-correction-mechanism-guards-v1',
        'date': '2026-10-19', 'timezone': 'America/New_York',
        'prepared_for': 'Edward Baker',
        'llm_assistance': 'substantial; same-model internal audit',
        'actual_model': args.execution_model,
        'actual_effort': args.execution_effort,
        'python': platform.python_version(), 'python_flint': flint.__version__,
        'precision_bits': ctx.prec, 'status': 'pass',
        'scope': 'Actual new comparison import/algebra/guard fixtures and independent analytic normalizer-chain-rule checks; no new physical acceptance interface.',
        'comparison_script_sha256': digest(mainpath),
        'opening_script_sha256': digest(opening_path),
        'audit_script_sha256': digest(__file__),
        'main_algebra_checks': checks,
        'independent_normalizer_checks': cases,
        'guard_mutations': rejected,
        'limitations': [
            'No new collision coverage or global sign claim.',
            'No duplicate full-grid comparison; decisive envelope replays are separate.',
            'The fixed-domain early guards are challenged before profile evaluation; phase and denominator bounds are exercised by the full comparison records.',
        ],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps({'output': str(args.output), 'sha256': digest(args.output),
                      'bytes': args.output.stat().st_size,
                      'guard_mutations': len(rejected), 'normalizer_fixtures': len(cases)}))


if __name__ == '__main__':
    main()
