#!/usr/bin/env python3
"""Check two fixed replay outputs against unchanged historical certificates.

17 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded model gpt-6.1-sol, reasoning effort ultra. No arithmetic is rerun
here: this checks serialized identities and stored-byte provenance only.
"""
import argparse
import hashlib
import json
import platform
from pathlib import Path
import sys


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read(path):
    return json.loads(path.read_text())


def main(args):
    sys.path.insert(0, str(args.code_dir))
    from replay_record_hygiene import CONTENT_HASH_POLICY, mathematical_content_digest
    names = ['CERTIFIED_EVALUATION.json', 'CERTIFIED_MEASUREMENTS.json',
             'CERTIFIED_FEASIBILITY.json', 'ANALYTIC_BOUND_CHECKS.json',
             'FEASIBILITY_WITNESSES.json']
    run_dirs = [args.first_run, args.second_run]
    summaries = [read(path / 'REPLAY_SUMMARY.json') for path in run_dirs]
    rows = []
    for name in names:
        paths = [args.historical_dir / name] + [path / name for path in run_dirs]
        stored = [digest(path) for path in paths]
        content = [mathematical_content_digest(read(path)) for path in paths]
        assert len(set(content)) == 1, ('content changed', name)
        for i, summary in enumerate(summaries):
            assert summary['record_sha256'][name] == stored[i + 1], ('stored binding', name, i)
            assert summary['record_content_sha256'][name] == content[i + 1], ('content binding', name, i)
        rows.append({'record': name,
                     'stored_sha256': dict(zip(['historical', 'first_run', 'second_run'], stored)),
                     'mathematical_content_sha256': content[0],
                     'historical_and_both_runs_content_agree': True,
                     'both_runs_stored_bytes_agree': stored[1] == stored[2]})
    for run_dir, summary in zip(run_dirs, summaries):
        assert summary['content_hash_policy'] == CONTENT_HASH_POLICY
        assert summary['mathematical_content_sha256'] == mathematical_content_digest(summary)
        assert summary['all_feasibility_precision_classifications_agree']
        assert summary['no_threshold_or_support_sweep']
        assert summary['fixed_case_counts'] == {'observations': 6, 'conditioning_combinations': 24,
                                               'feasibility_combinations': 32}
        assert summary['elapsed_seconds'] < summary['replay_budget_seconds']
        assert summary['largest_child_peak_rss_bytes'] < summary['memory_budget_bytes']
        for name, expected in summary['code_sha256'].items():
            assert digest(args.code_dir / name) == expected, ('code binding', name)
        for record_name in ['CERTIFIED_MEASUREMENTS.json', 'CERTIFIED_FEASIBILITY.json',
                            'ANALYTIC_BOUND_CHECKS.json']:
            record = read(run_dir / record_name)
            assert record['evaluation_sha256'] == digest(run_dir / 'CERTIFIED_EVALUATION.json')
        assert read(run_dir / 'CERTIFIED_FEASIBILITY.json')['floating_witnesses_sha256'] == digest(run_dir / 'FEASIBILITY_WITNESSES.json')
    assert summaries[0]['mathematical_content_sha256'] == summaries[1]['mathematical_content_sha256']
    result = {
        'schema': 'source_measurement_replay_hygiene_check_v1',
        'date': '2026-10-17', 'prepared_for': 'Edward Baker',
        'model': 'gpt-6.1-sol', 'reasoning_effort': 'ultra',
        'llm_assistance': 'Substantial LLM assistance; same-model implementation and verification.',
        'status': 'Two fixed bounded replays; canonical identity and provenance checks pass.',
        'meaning': 'Serialized mathematical data agree with the unchanged historical records '
                   'in this environment. Hashes do not establish mathematical validity '
                   'or arithmetic portability.',
        'python_version': platform.python_version(), 'platform_system': platform.system(),
        'checker_sha256': digest(Path(__file__)),
        'content_hash_policy': CONTENT_HASH_POLICY,
        'retained_records': rows,
        'summary_mathematical_content_sha256': summaries[0]['mathematical_content_sha256'],
        'both_summary_content_hashes_agree': True,
        'stored_input_and_code_provenance_bindings_pass': True,
        'historical_mathematical_records_replaced': False,
        'fixed_case_counts': summaries[0]['fixed_case_counts'],
        'certificate_totals': summaries[0]['certificate_totals'],
        'replay_summaries': [
            {'label': label, 'stored_sha256': digest(path / 'REPLAY_SUMMARY.json'),
             'elapsed_seconds': summary['elapsed_seconds'],
             'largest_child_peak_rss_bytes': summary['largest_child_peak_rss_bytes'],
             'code_sha256': summary['code_sha256']}
            for label, path, summary in zip(['first_run', 'second_run'], run_dirs, summaries)],
    }
    args.output.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({'output': str(args.output),
                      'retained_record_content_agreement': len(rows),
                      'both_summary_content_hashes_agree': True,
                      'certificate_totals': result['certificate_totals'],
                      'replay_resources': [{key: row[key] for key in ['label', 'elapsed_seconds',
                                                                      'largest_child_peak_rss_bytes']}
                                           for row in result['replay_summaries']]}, indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ['code-dir', 'historical-dir', 'first-run', 'second-run', 'output']:
        parser.add_argument('--' + name, type=Path, required=True)
    main(parser.parse_args())
