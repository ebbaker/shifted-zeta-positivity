#!/usr/bin/env python3
"""Fresh S01 source-specific controls through the unchanged signed consumer.

Prepared for Edward Baker, 19 October 2026, with substantial LLM assistance.
Authoring model gpt-6.1-sol, actual effort ultra. Same-model internal replay.
Requires python-flint 0.9.0. All replay receipts remain in --work-dir;
--output is a small summary with source identities and arithmetic outcomes.
"""
from fractions import Fraction as F
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import platform
import subprocess
import sys
import time

import flint
from flint import arb, ctx

INV = Path('papers/investigations-3/11_arithmetic_collision_rigidity')


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


class SourceEventJetEvaluator:
    """Pass source-specific balls directly to the unchanged acceptance code."""
    def __init__(self, jets):
        self.jets = jets

    def enclose(self, *args):
        return self.jets, []


def challenge(base, name, jets, domain, event):
    base.check(len(jets) == 3 and all(v.is_finite() for v in jets),
               'nonfinite source-specific event ball')
    if event:
        base.check(jets[0].contains(0) and jets[1].contains(0),
                   'source-specific event is not enclosed')
    excess, _ = base.signed_cell(SourceEventJetEvaluator(jets),
                                 F(0), F(0), F(0), F(0), 0)
    regrouped = ((arb(99)/100)*base.square(jets[1])-jets[0]*jets[2]
                 -(arb(1)/100)*base.square(jets[0]))
    base.check(not(excess > 0) and not(regrouped > 0),
               'source-specific control passed actual acceptance')
    if not event:
        base.check(excess < 0 and regrouped < 0,
                   'Euler witness is not strictly negative')
    return {'control': name, 'source_domain': domain,
            'source_specific_jet_balls': [base.s(v) for v in jets],
            'unchanged_signed_cell_excess': base.s(excess),
            'regrouped_99_over_100_excess': base.s(regrouped),
            'strict_signed_cell_acceptance': bool(excess > 0),
            'strict_regrouped_acceptance': bool(regrouped > 0),
            'event_H_and_Hx_enclose_zero':
                bool(jets[0].contains(0) and jets[1].contains(0)) if event else None,
            'theta_tail_or_quadrature_constants_used': False,
            'strictly_negative_excess': bool(excess < 0)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, required=True)
    parser.add_argument('--work-dir', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--execution-model', required=True)
    parser.add_argument('--execution-effort', required=True)
    args = parser.parse_args()
    started = time.monotonic()
    repo = args.repo.resolve()
    work = args.work_dir.resolve()
    work.mkdir(parents=True, exist_ok=True)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    receipts = work/'receipts'
    source_record = work/'SOURCE_SPECIFIC_REPLAY.json'
    replay_path = repo/INV/'numerics/replay_nonstationary_controls.py'
    subprocess.run([sys.executable, str(replay_path), '--repo', str(repo),
                    '--receipts', str(receipts), '--output', str(source_record),
                    '--execution-model', args.execution_model,
                    '--execution-effort', args.execution_effort],
                   check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                   timeout=150)
    base_path = repo/INV/'numerics/high_height_consumer/high_height_consumer.py'
    paired_path = repo/INV/'symmetries/01_modular_self_duality/numerics/check_paired_modular_tail.py'
    base = load('s01_control_base', base_path)
    paired = load('s01_control_paired', paired_path)
    ctx.prec = 192
    source = json.loads(source_record.read_text())
    base.check(source['interface_precision_bits'] == 192,
               'fresh replay precision')
    base.check(source['checker_sha256'] == digest(repo/INV/'numerics/run_plan02_pilot.py'),
               'fresh replay checker mismatch')
    base.check(source['script_sha256'] == digest(replay_path),
               'fresh replay source mismatch')
    outcomes = []
    for event in source['screen']['event_rejections']:
        outcomes.append(challenge(base, event['control'],
            [arb(v) for v in event['event_jet_enclosures']], event['event_domain'], True))
    base.check(len(outcomes) == 5, 'fresh source-specific event count mismatch')
    euler_file = receipts/'EULER_FACTOR_REPLAY.json'
    euler = json.loads(euler_file.read_text())
    outcomes.append(challenge(base, 'Euler-factor p=41 negative-Laguerre witness',
        [arb(row['full_jet']['display']) for row in euler['jets']], euler['parameters'], False))
    negative_cases = paired.negative_cases()
    vertical_fixture = paired.vertical_fixture()
    receipt_ids = {}
    for key, row in source['screen']['receipt_identities'].items():
        base.check(digest(receipts/row['file']) == row['sha256'],
                   'fresh source receipt identity mismatch')
        receipt_ids[key] = row
    sources = [base_path, paired_path, repo/INV/'numerics/run_plan02_pilot.py',
        replay_path, repo/INV/'numerics/certify_shifted_theta_jet.py',
        repo/'papers/investigations-2/active/22_theta_manifold_geometry/numerics/certify_square_support_endpoint_collision.py',
        repo/'papers/investigations-2/active/22_theta_manifold_geometry/numerics/check_theta_two_endpoint_control.py',
        repo/'papers/investigations-2/active/22_theta_manifold_geometry/numerics/check_theta_center_separation.py',
        repo/'papers/investigations-2/active/19_euler_factor_controls/numerics/certify_euler_factor_witness.py']
    record = {'schema': 's01-consumer-controls-v1', 'date': '2026-10-19',
        'timezone': 'America/New_York', 'prepared_for': 'Edward Baker',
        'actual_model': args.execution_model, 'actual_effort': args.execution_effort,
        'llm_assistance': 'substantial; same-model internal replay',
        'python': platform.python_version(), 'python_flint': flint.__version__,
        'precision_bits': ctx.prec, 'status': 'pass',
        'acceptance_expression': 'square(v1)-v0*v2-(square(v0)+square(v1))/100 > 0, using unchanged high_height_consumer.signed_cell',
        'regrouped_expression': '(99/100)*square(v1)-v0*v2-(1/100)*square(v0) > 0',
        'scope': 'Acceptance-expression challenge on fresh source-specific event jet balls and Euler witness; five paired-tail admissibility failures and non-even vertical-boundary fixture. No theta constants substituted; no new tail theorem, source event certificate, region coverage or global sign claim.',
        'ball_transport': 'Fresh replay and source receipt display strings conservatively re-enclosed as Arb balls; no assertion of exact dyadic identity. The stub returns these balls directly and does not evaluate the theta source.',
        'fresh_replay': {'external_work_dir': str(work),
                         'filename': source_record.name, 'sha256': digest(source_record)},
        'source_pins': [{'path': str(path.relative_to(repo)), 'sha256': digest(path)}
                        for path in sources],
        'fresh_receipt_identities': receipt_ids, 'downstream_outcomes': outcomes,
        'paired_tail_invalid_parameter_rejections': negative_cases,
        'non_even_source_vertical_boundary_fixture': vertical_fixture,
        'analytic_premise_screen': source['screen']['analytic_premise_screen'],
        'review_script_sha256': digest(__file__), 'seconds': time.monotonic()-started}
    args.output.write_text(json.dumps(record, indent=2)+'\n')
    print(json.dumps({'output': str(args.output), 'sha256': digest(args.output),
        'event_boxes_rejected': len(outcomes)-1,
        'Euler_witness_strictly_negative': outcomes[-1]['strictly_negative_excess'],
        'invalid_parameter_rejections': len(negative_cases),
        'vertical_derivatives': len(vertical_fixture),
        'bytes': args.output.stat().st_size, 'seconds': record['seconds']}))


if __name__ == '__main__':
    main()
