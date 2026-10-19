#!/usr/bin/env python3
"""S05-T1 bounded source-consumer fit probe; no full evaluator setup.

Prepared for Edward Baker, 19 October 2026, with substantial LLM assistance.
Execution model/effort are explicit CLI metadata. Outward Arb/Acb arithmetic.
This compares finite retained modes on S01's actual shifted contour. It does
not transfer complete-source parity or an S05 infinite-tail allowance.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import platform
import time
import flint
from flint import arb, acb, ctx

INV = Path('papers/investigations-3/11_arithmetic_collision_rigidity')
S05 = INV/'symmetries/05_covariant_theta_jets'
METHODS = ('expanded', 'polynomial_factored', 'exponential_grouped')
SOURCE_PINS = {
 str(INV/'numerics/high_height_consumer/high_height_consumer.py'):'e96feb2b4c3e84de3025713b486fb8cf99fdd810f61366b79a0da188eb12535f',
 str(INV/'symmetries/01_modular_self_duality/numerics/S01_COMPLETE_CONSUMER_20261019.json'):'4e5b8336843da26294d721c2338e8b2bac5f8af67260aea7843205d1fb97806a',
 str(INV/'symmetries/01_modular_self_duality/numerics/integrate_paired_tail_consumer.py'):'f6b89d07cbf1f6fb7fbdbe0a491545a86c5ecabf9320bccf6285db53c7c1158f',
 str(S05/'numerics/check_covariant_source_enclosures.py'):'bc78419b4bd60b979c63728d37faced2c373e2240d1c0879586361ac5b0c91e6',
 str(S05/'notes/01_COMPLETE_SOURCE_JETS_AND_FIXED_POINT_ENCLOSURES_20261018.md'):'693817db663ba4170554b83cfbe756e0f771a9ff85c04fcf09a4fedb1c3eab4a',
}


def check(condition, message):
    if not condition:
        raise ArithmeticError(message)


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def s(value):
    return value.str(45, more=True)


def dyadic(value):
    check(value.is_finite() and value.is_exact(), 'exact finite dyadic required')
    mantissa, exponent = value.man_exp()
    return {'mantissa': str(mantissa), 'exponent': int(exponent)}


def coordinate_radius(value):
    candidates = [value.real.rad().upper(), value.imag.rad().upper()]
    check(all(x.is_exact() for x in candidates), 'radius upper endpoints must be exact')
    return max(candidates)


def source_polynomial_sum(v, lams, method):
    """Finite n=1..11 source sum. Expanded form matches the actual caller."""
    q = (4*v).exp()
    total = acb(0)
    for lam in lams:
        if method == 'expanded':
            total += (2*lam*lam*q*q-3*lam*q)*(-lam*q).exp()
        else:
            w = lam*q
            if method == 'polynomial_factored':
                total += w*(2*w-3)*(-w).exp()
            elif method == 'exponential_grouped':
                total += (v-w).exp()*w*(2*w-3)
            else:
                raise ValueError(method)
    return total


def retained_source(v, lams, method):
    total = source_polynomial_sum(v, lams, method)
    return total if method == 'exponential_grouped' else v.exp()*total


def probe(repo, bits, model, effort, output_dir):
    check(bits in (192,256),'a matched 192/256-bit historical budget is required')
    check(model.strip() and effort.strip(),'actual execution metadata required')
    for relative, expected in SOURCE_PINS.items():
        check(digest(repo/relative)==expected,'stale acquisition source: '+relative)
    ctx.prec = bits
    started = time.monotonic()
    pi = arb.pi()
    d = pi/8-4*arb(1000).log()/1000
    norm = arb(1000)**(arb(9)/4)
    tc, X, U, j = arb(21)/200, arb(1000), arb(2), 0
    lams = [pi*n*n for n in range(1,12)]
    check(0 < d < pi/8, 'actual source contour outside open strip')
    actual = repo/INV/'numerics/high_height_consumer/high_height_consumer.py'
    text = actual.read_text()
    check('total+=(2*lam*lam*q*q-3*lam*q)*(-lam*q).exp()' in text,
          'original retained-source expression changed')
    check("abs_tol=arb('1e-13'),rel_tol=arb('1e-30'),eval_limit=200000,depth_limit=30" in text,
          'original quadrature settings changed')
    quadratures, balls = [], {}
    for method in METHODS:
        count = 0
        def integrand(u, analytic):
            nonlocal count
            count += 1
            check(count <= 200000, 'bounded j=0 callback limit exceeded')
            v = u+acb(0,d)
            total = source_polynomial_sum(v, lams, method)
            if method == 'exponential_grouped':
                return norm*(tc*v*v+acb(0,X)*u).exp()*total*(acb(0,1)*v)**j
            # This expanded branch has exactly the original j=0 common factor.
            return norm*(tc*v*v+v+acb(0,X)*u).exp()*total*(acb(0,1)*v)**j
        begin = time.monotonic()
        value = acb.integral(integrand, 0, U, abs_tol=arb('1e-13'),
                             rel_tol=arb('1e-30'), eval_limit=200000, depth_limit=30)
        seconds = time.monotonic()-begin
        check(value.is_finite(), 'nonfinite j=0 quadrature')
        balls[method] = value
        quadratures.append({'method': method, 'callbacks': count,
             'seconds_diagnostic_only': seconds, 'real_value': s(value.real),
             'imaginary_value': s(value.imag), 'real_midpoint_dyadic': dyadic(value.real.mid()),
             'real_quadrature_radius_upper': s(value.real.rad().upper()),
             'real_quadrature_radius_upper_dyadic': dyadic(value.real.rad().upper()),
             'imaginary_quadrature_radius_upper': s(value.imag.rad().upper()),
             'finite': True})
    for method in METHODS[1:]:
        check(balls['expanded'].real.overlaps(balls[method].real),
              'algebraically equivalent j=0 real enclosures disjoint')
        check(balls['expanded'].imag.overlaps(balls[method].imag),
              'algebraically equivalent j=0 imaginary enclosures disjoint')
    cells, counters = [], {method: {'narrower':0, 'wider':0, 'equal':0} for method in METHODS[1:]}
    ratios = {method: [] for method in METHODS[1:]}
    for cell in range(128):
        lo, hi = F(cell,64), F(cell+1,64)
        u = arb(arb(2*cell+1)/128, arb(1)/128)
        v = acb(u,d)
        images = {method: retained_source(v,lams,method) for method in METHODS}
        radii = {method: coordinate_radius(value) for method,value in images.items()}
        row = {'u_cell':[str(lo),str(hi)], 'source_coordinate':'v=u+i*d',
               'coordinate_radius_upper': {method:s(value) for method,value in radii.items()}}
        for method in METHODS[1:]:
            check(images['expanded'].real.overlaps(images[method].real)
                  and images['expanded'].imag.overlaps(images[method].imag),
                  'same retained-source interval formulas disjoint')
            ratio = radii['expanded']/radii[method]
            ratios[method].append(ratio)
            verdict = ('narrower' if radii[method] < radii['expanded'] else
                       'wider' if radii[method] > radii['expanded'] else 'equal')
            counters[method][verdict] += 1
            row[method+'_direct_over_candidate_radius'] = s(ratio)
        cells.append(row)
    old_radius = balls['expanded'].real.rad().upper()
    factored_radius = balls['polynomial_factored'].real.rad().upper()
    delta = old_radius-factored_radius
    check(delta > 0, 'preliminary factored j=0 quadrature decrease not reproduced')
    check(balls['exponential_grouped'].real.rad().upper() > old_radius,
          'range-narrowing/quad-widening counterexample not reproduced')
    ledger_path = repo/INV/'symmetries/01_modular_self_duality/numerics/S01_COMPLETE_CONSUMER_20261019.json'
    ledger = json.loads(ledger_path.read_text())
    producer = repo/INV/'symmetries/01_modular_self_duality/numerics/integrate_paired_tail_consumer.py'
    check(ledger['script_sha256'] == digest(producer), 'S01 historical budget producer hash is stale')
    historical_pin_checks = {relative: digest(repo/relative) == expected
                            for relative,expected in ledger['source_sha256'].items()}
    check(all(historical_pin_checks.values()), 'S01 historical budget input pin is stale')
    check(ledger['status'] == 'pass', 'S01 historical budget did not pass')
    historical = next(row for row in ledger['replays'] if row['bits']==bits)
    old_complete = arb(historical['complete_error_ledger'][0]['paired_complete_added_error'])
    old_quad = arb(historical['complete_error_ledger'][0]['quadrature_with_internal_rounding'])
    report = {'schema':'s05-t1-shifted-source-fit-probe-v1', 'date':'2026-10-19',
        'timezone':'America/New_York', 'prepared_for':'Edward Baker',
        'actual_model':model, 'actual_effort':effort, 'llm_assistance':'substantial; internal same-model research',
        'python':platform.python_version(), 'python_flint':flint.__version__, 'precision_bits':bits,
        'script_sha256':digest(__file__),
        'source_sha256':SOURCE_PINS,
        'historical_S01_ledger_verification':{'producer_sha256_matches':True,
                'source_pin_checks':historical_pin_checks, 'status_pass':True},
        'selected_caller':'WholeCellEvaluator midpoint acquisition, S01 complete signed consumer on B',
        'scope':{'B_t':['1/100','1/5'], 'B_x':['999','1001'], 'midpoint':['21/200','1000'],
                 'j':0,'retained_modes':[1,11], 'U':'2', 'd':'pi/8-4*log(1000)/1000', 'd_enclosure':s(d),
                 'midpoint_integral_normalization':'1000^(9/4)',
                 'physical_output_units':'H/Gc, Gc=1000^(7/4)*exp(-125*pi)',
                 'quadrature_abs_tol':'1e-13','quadrature_rel_tol':'1e-30',
                 'eval_limit':200000,'depth_limit':30,'range_cells':128,
                 'range_cell_width':'1/64','range_domain':['0','2'],
                 'source_images':'finite retained source only; no full-source tail added'},
        'formulas':{'expanded':'exp(v)*sum((2*lam^2*q^2-3*lam*q)*exp(-lam*q))',
                    'polynomial_factored':'exp(v)*sum(w*(2*w-3)*exp(-w)), w=lam*q',
                    'exponential_grouped':'sum(exp(v-w)*w*(2*w-3)), w=lam*q'},
        'j0_quadratures':quadratures,
        'actual_shifted_retained_source_range_diagnostics':{'counts':counters,
             'direct_over_candidate_radius_bounds':{method:{
                 'minimum_lower_bound':s(min(value.lower() for value in values)),
                 'maximum_upper_bound':s(max(value.upper() for value in values))}
                  for method,values in ratios.items()},
             'cell_receipts':'Regenerated in memory by this script; only aggregate counts and extrema retained under LARGE_FILES.md.'},
        'hypothetical_complete_budget_if_only_r0_changes':{
             'interpretation':'Conditional feasibility scale, not a complete consumer replay. The other 50 coefficients/radii and other errors are held common; C0 midpoint and its radius may both change. The delta is measured against a fresh expanded integral and divided by the historical complete allowance for scale.',
             'delta_r0_equals_delta_Q0':s(delta), 'old_j0_radius':s(old_radius),
             'factored_j0_radius':s(factored_radius),
             'delta_over_j0_radius':s(delta/old_radius),
             'historical_paired_epsilon0':s(old_complete),
             'historical_Q0_over_epsilon0':s(old_quad/old_complete),
             'delta_over_historical_epsilon0':s(delta/old_complete),
             'Q0_weight_of_r0':'1', 'Q1_Q2_use_r0':False,
             'historical_complete_budget_source':'hash-pinned S01 record; not freshly reacquired'},
        'decision':'Select polynomial-factoring-only retained-mode acquisition as possible S05-T2 budget fit; park real fixed-point parity transfer for this caller.',
        'limitations':['Only j=0 acquired; no other 50 midpoint coefficients reacquired.',
          'No full physical consumer, complete new error, paid margin, coverage or speedup certified.',
          'Finite n=1..11 algebra applies without source parity. No full-source parity or tail is transferred.',
          'Real fixed-point parity Taylor is incompatible with this shifted contour.',
          'Narrower source cell ranges alone do not guarantee quadrature improvement: exponential grouping is a counterexample here.',
          'Acb quadrature may inspect complex neighborhoods; the 128 actual-line cell widths are diagnostic, not quadrature error proofs.',
          'Reported seconds are one-run diagnostics and not matched performance measurements.',
          'A future T2 must pay all coefficient acquisitions, unchanged mode/source tails, moment/Taylor work and whole-cell propagation.'],
        'seconds_total_diagnostic':time.monotonic()-started,'status':'pass'}
    output = output_dir/f'S05_T1_SHIFTED_SOURCE_FIT_{bits}_20261019.json'
    output.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({'bits':bits,'status':'pass','path':str(output),
          'quadratures':[{k:row[k] for k in ('method','callbacks','real_quadrature_radius_upper')} for row in quadratures],
          'delta_r0':s(delta),'delta_over_historical_epsilon0':s(delta/old_complete)}),flush=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--repo',type=Path,required=True)
    parser.add_argument('--output-dir',type=Path,required=True)
    parser.add_argument('--bits',type=int,nargs='+',choices=[192,256],default=[192,256])
    parser.add_argument('--execution-model',required=True)
    parser.add_argument('--execution-effort',required=True)
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True,exist_ok=True)
    for bits in args.bits:
        probe(args.repo.resolve(),bits,args.execution_model,args.execution_effort,args.output_dir)


if __name__=='__main__':
    main()
