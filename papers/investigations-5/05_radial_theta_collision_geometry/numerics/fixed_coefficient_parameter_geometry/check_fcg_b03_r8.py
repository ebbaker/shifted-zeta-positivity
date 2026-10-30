#!/usr/bin/env python3
"""Source-free R8 bookkeeping. Does not numerically test the degree theorem."""
import argparse
import hashlib
import json
from datetime import datetime, timezone
from fractions import Fraction as F
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, default=Path(__file__).resolve().parents[5])
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    repo = args.repo.resolve()
    base = repo / 'papers/investigations-5/05_radial_theta_collision_geometry'
    source = base / 'numerics/fixed_coefficient_parameter_geometry/fcg_e02_r7_taylor_subtracted_assessment_20261030.json'
    inherited = json.loads(source.read_text())
    evidence = []
    for item in inherited['inputs']:
        p = repo / item['path']
        digest = hashlib.sha256(p.read_bytes()).hexdigest()
        assert digest == item['sha256'], f"Changed inherited input: {item['path']}"
        evidence.append({'path': item['path'], 'sha256': digest})

    checks = []
    def check(name, condition):
        assert condition, name
        checks.append(name)

    tau, r, T0, delta = F(1, 4), F(1, 128), F(17, 64), F(511, 128)
    lam = delta-r
    beta_squared = lam*lam/r
    check('critical Gaussian slack equals inner radius', T0-tau-r == r)
    check('linear slack and original exponent', delta+r == 4)
    check('strict tail-monotonicity premise', delta > 2*r)
    check('lambda value', lam == F(255,64))
    check('sharp square-root exponent squared', beta_squared == F(65025,32))
    check('degree-rule premise beta > 4', beta_squared > 16)
    check('upper exponential simplification', delta/2-r/4+lam*lam/(4*r) == delta*delta/(4*r))
    check('upper exponent rational value', delta*delta/(4*r) == F(261121,512))
    check('lower exponent rational value', delta/2-r/4-1 == F(509,512))
    check('positive Bernoulli factor', 1-r/4 == F(511,512))
    check('primitive domination factor', F(64**2,72) == F(512,9))

    # One inherited N=4 polynomial identity, not a degree sweep.
    from math import comb, factorial
    n = 5
    c = r**n/F(factorial(n))
    pb = {n+j: 2*c*comb(n,j) for j in range(n+1)}
    for j in range(n):
        pb[n+j] += n*c*comb(n-1,j)
    ph = {n+1+j: c*comb(n,j) for j in range(n+1)}
    check('N4 pb matches frozen R7 coefficient list', [pb[n+j]/c for j in range(n+1)] == [7,30,50,40,15,2])
    check('N4 ph matches frozen R7 coefficient list', [ph[n+1+j]/c for j in range(n+1)] == [1,5,10,10,5,1])

    tail_cap, margin_floor, gain_cap = F('2.153e-23'), F('1.89988e-19'), F('0.00012')
    check('maximal relative margin gain below 0.012 percent', tail_cap/margin_floor < gain_cap)
    check('common X1 is a single 384-bit moment', inherited['common_moment']['moment_stage_bits'] == 384)
    check('same common moment reused in both stages', inherited['common_moment']['same_X1_reused_both_jet_stages'] is True)
    for stage in inherited['stages']:
        row = stage['row']
        bits = stage['bits']
        check(f'{bits}: inherited direct tail below quoted cap', F(row['TD']['upper']) < tail_cap)
        check(f'{bits}: inherited direct margin above quoted floor', F(row['dD']['lower']) > margin_floor)
        check(f'{bits}: inherited old C degree-four margin negative', F(stage['old_C']['d']['upper']) < 0)
        check(f'{bits}: inherited scalar H floor', F(stage['scalar']['floor_H']['lower']) > F('6.38928e-10'))
        check(f'{bits}: inherited scalar HA floor', F(stage['scalar']['floor_HA']['lower']) > F('4.17477e-10'))

    for rel in [
        'notes/fixed_coefficient_parameter_geometry/B03_R8_GAUSSIAN_SLACK_DEGREE_LAW_20261030.md',
        'notes/fixed_coefficient_parameter_geometry/B03_R8_CONTINUATION_AND_MODEL_HANDOFF_20261030.md',
        'reviews/fixed_coefficient_parameter_geometry/E02_R7_TAYLOR_SUBTRACTED_ASSESSMENT_20261030.md',
        'numerics/fixed_coefficient_parameter_geometry/fcg_e02_r7_taylor_subtracted_assessment_20261030.json',
    ]:
        p = base / rel
        evidence.append({'path': str(p.relative_to(repo)), 'sha256': hashlib.sha256(p.read_bytes()).hexdigest()})
    result = {
        'task': 'FCG-B03 R8 source-free bookkeeping',
        'date': '2026-10-30', 'prepared_for': 'Edward Baker',
        'model': 'gpt-6-astra', 'effort': 'max',
        'thread_id': '01a18e52-fa91-7b61-b31b-b311eee675f8', 'history_number': 50,
        'provenance': 'Same-assistant checks by proof author; inherited R7 data and premises; no independent assessment.',
        'inputs': evidence,
        'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'checks': checks,
        'constants': {'r': str(r), 'delta': str(delta), 'lambda': str(lam), 'beta_squared': str(beta_squared),
                      'upper_exponent': str(delta*delta/(4*r)), 'lower_exponent': str(delta/2-r/4-1)},
        'inherited_tail_cap': str(tail_cap), 'inherited_margin_floor': str(margin_floor),
        'relative_gain_cap': str(gain_cap),
        'new_source_evaluations': 0, 'new_quadrature_evaluations': 0,
        'degree_sweep': False, 'new_G_payment_evaluated': False,
        'scope': 'Exact rational constants, one inherited N4 polynomial identity, inherited source hashes and saved endpoint comparisons only. Infinite-degree claims are proved analytically in the note, not inferred from these checks.',
        'status': 'source_free_checks_passed_separate_R8_assessment_pending',
        'recorded_utc': datetime.now(timezone.utc).isoformat(),
    }
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'status': result['status'], 'checks': len(checks), 'output': str(args.output), 'new_source_evaluations': 0}))


if __name__ == '__main__':
    main()
