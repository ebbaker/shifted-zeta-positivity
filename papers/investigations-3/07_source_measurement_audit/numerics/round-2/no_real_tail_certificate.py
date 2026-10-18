#!/usr/bin/env python3
"""One analytic tail-dominance certificate, with no physical-height grid.

17 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded model gpt-6.1-sol, reasoning effort ultra.
Requires python-flint. Recomputes the fixed round-one directional budget.
"""
import argparse
import hashlib
import json
from pathlib import Path
import platform
import resource
import subprocess
import sys
import tempfile
import time

from flint import arb, ctx, __version__ as flint_version


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(output, producer):
    started = time.monotonic()
    with tempfile.TemporaryDirectory(prefix='source-audit-tail-') as directory:
        budget_path = Path(directory) / 'budget.json'
        subprocess.run([sys.executable, str(producer), '--output', str(budget_path)],
                       check=True, stdout=subprocess.DEVNULL, timeout=120)
        budget = json.loads(budget_path.read_text())
        assert budget['checker_sha256'] == digest(producer)
        budget_stored_sha = digest(budget_path)

    ctx.prec = 320
    a = abs(arb(budget['leading']['a']))
    error = arb(budget['remainder_constants']['E_A'])
    direction = [arb(v) for v in budget['A']]
    # d_k = delta_{k-1} - 2 delta_k + delta_{k+1}, with zero outside 1..N.
    padded = [arb(0), *direction, arb(0), arb(0)]
    rows = [padded[k-1]-2*padded[k]+padded[k+1] for k in range(1, 5)]
    measurement_norm = sum((v*v for v in rows), arb(0)).sqrt()
    kappa = arb.pi()/16
    envelope = arb(6)/5
    cases = []
    for units, eps, height in [
            ('coefficient multiplier', arb('1e-16'), 264),
            ('raw recurrence Euclidean norm', arb('1e-16')/measurement_norm, 269)]:
        x = arb(height)
        lower = a/x**2-error/x**4
        theta_upper = envelope*(-kappa*x).exp()
        dominance = eps*lower/theta_upper
        log_derivative_lower = kappa-2/x
        assert lower > 0 and dominance > 1 and log_derivative_lower > 0
        assert eps < arb('1e-15') and eps*max(abs(v).upper() for v in direction) < 1
        cases.append({
            'error_units': units, 'tolerance': '1e-16', 'X': height,
            'abs_epsilon': eps.str(80, more=True),
            'directional_transform_abs_lower_at_X': lower.str(80, more=True),
            'complete_theta_abs_upper_at_X': theta_upper.str(80, more=True),
            'dominance_ratio_at_X': dominance.str(80, more=True),
            'ratio_log_derivative_lower_for_x_ge_X': log_derivative_lower.str(80, more=True),
            'both_signs_of_epsilon': True,
            'for_all_x_ge_X_and_t_in_0_quarter': True,
            'coefficient_positivity': '1 - abs(epsilon)*max(abs(A_n)) > 0',
        })
    mathematical = {
        'heat_interval': ['0', '1/4'], 'direction': budget['A'],
        'direction_formula': 'A=e2-(beta2/beta1)e1; theta tail; no anchor',
        'a_abs': a.str(80, more=True), 'E_A': error.str(80, more=True),
        'recurrence_norm_A': measurement_norm.str(80, more=True),
        'complete_theta_envelope': '(6/5)*exp(-pi*x/16)',
        'tail_lower': 'abs(epsilon)*(abs(a)/x^2-E_A/x^4)',
        'monotonicity_proof': 'd_x log(exp(k*x)*(a/x^2-E/x^4)) = k-2/x+2*E/(x^3*(a-E/x^2)) > k-2/X > 0',
        'cases': cases,
    }
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if platform.system() == 'Linux':
        rss *= 1024
    record = {
        'schema': 'source_measurement_no_real_tail_v1',
        'date': '2026-10-17', 'prepared_for': 'Edward Baker',
        'recorded_model': 'gpt-6.1-sol', 'recorded_reasoning_effort': 'ultra',
        'llm_assistance': 'Substantial; routine same-model verification, no specialist review',
        'status': 'Arb certificate of uniform analytic tail domination; no physical integrals',
        'contract': {'fixed_heights': [264, 269], 'height_grid': False,
                     'support_sweep': False, 'max_seconds': 180, 'memory_MiB': 512},
        'mathematical_content': mathematical,
        'mathematical_content_sha256': hashlib.sha256(json.dumps(mathematical, sort_keys=True, separators=(',', ':')).encode()).hexdigest(),
        'provenance': {'producer_sha256': digest(producer),
                       'fresh_budget_stored_sha256': budget_stored_sha,
                       'checker_sha256': digest(Path(__file__)),
                       'python': platform.python_version(), 'python_flint': flint_version,
                       'arb_precision_bits': ctx.prec},
        'elapsed_seconds': time.monotonic()-started, 'peak_resident_bytes': rss,
        'scope': 'No real zeros at or above X for each specified fixed nonzero perturbation, both signs, 0<=t<=1/4. Sufficient bounds; no claim about first loss height or eta at x=140.',
    }
    assert record['elapsed_seconds'] < 180 and rss < 512*1024**2
    output.write_text(json.dumps(record, indent=2)+'\n')
    print(json.dumps({'content_sha256': record['mathematical_content_sha256'],
                      'cases': cases}, indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--budget-producer', type=Path,
                        default=Path(__file__).resolve().parents[1]/'round-1'/'concrete_onset_budget.py')
    args = parser.parse_args()
    run(args.output, args.budget_producer)
