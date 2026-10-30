#!/usr/bin/env python3
"""Frozen FCG-E01 R3 real-panel lower-cost witness; no source jets or scan.

30 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Actual implementation/execution model gpt-6.1-sol; reasoning effort ultra,
verified in the implementing agent's local turn_context metadata. This is
internal LLM implementation, not independent specialist or formal review.

Run with /private/tmp/hcb-endpoint-venv/bin/python execute_fcg_e01_r3.py
from any working directory. The script writes only the packet's JSON and
return note beside the research files. All inputs are read-only/hash-bound.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from fractions import Fraction
from hashlib import sha256
import json
import os
from pathlib import Path
import platform
import signal
import sys
import time

import flint
from flint import arb, ctx

BASE = Path('papers/investigations-5/05_radial_theta_collision_geometry')
SUB = 'fixed_coefficient_parameter_geometry'
PACKET = BASE / 'research-progress/handoffs' / SUB / 'FCG-E01_R3_PRIMITIVE_ABSOLUTE_PAYMENT_20261030.md'
INPUT = BASE / 'numerics' / SUB / 'fcg_e01_r2_adaptive_ibp_20261030.json'
OUTPUT = BASE / 'numerics' / SUB / 'fcg_e01_r3_primitive_absolute_payment_20261030.json'
NOTE = BASE / 'notes' / SUB / 'E01_R3_PRIMITIVE_ABSOLUTE_PAYMENT_RETURN_20261030.md'
FROZEN = {
    str(PACKET): 'b2fdb03f7585139ac56d16e88f712bb615f5d8d91b7779e2a0135fbaaeacec31',
    str(BASE / 'notes' / SUB / 'B03_R6_PRIMITIVE_ABSOLUTE_PAYMENT_OBSTRUCTION_20261030.md'): 'bbe0230b0e07c8a70f9f56af4fbda1985555aa6b14f0676d95c48488e0120a1e',
    str(BASE / 'notes' / SUB / '26_ADAPTIVE_RADIUS_AND_PHASE_ALIGNED_IBP_B03_R5_20261030.md'): 'd450a8ccb05ce40e8e567a9585002d047406698775140f18606def71b31fa56b',
    str(BASE / 'notes' / SUB / '28_SHARP_QUADRATIC_RADIUS_PAYMENT_B03_R5_20261030.md'): '054f7663c9d9fcb49168ded71fc0813495c3d9927df41b462ca15206ade30aca',
    str(INPUT): '557c57e420534e4db949e3d019d5d40077a1df8f055f6634bd2f657c4f87392c',
    str(BASE / 'reviews' / SUB / 'E02_R5_ADAPTIVE_RADIUS_IBP_ASSESSMENT_20261030.md'): 'e7cc379644196226aa4c45af959fe182ee8da8995d32470fa411655514ff8af3',
}
BITS = (256, 384)
COUNTS = (256, 512, 1024)
RADII = (Fraction(1, 64), Fraction(1, 128), Fraction(1, 256))
DEGREES = (1, 2, 4, 8)
R = Fraction(1, 32)
CAP_SECONDS = 120
CAP_EVALUATIONS = 3584


def check(ok, why):
    if not ok:
        raise ArithmeticError(why)


def A(q):
    return arb(q.numerator) / q.denominator if isinstance(q, Fraction) else arb(q)


def enc(x):
    check(x.is_finite(), 'nonfinite interval')
    m, me = x.mid().man_exp()
    r, re = x.rad().man_exp()
    return {'ball': x.str(65, more=True), 'mid_binary': [str(m), int(me)],
            'rad_binary': [str(r), int(re)]}


def decode(x):
    """Decode every saved bit; Arb may widen a radius outward on conversion."""
    return arb((int(x['mid_binary'][0]), int(x['mid_binary'][1])),
               (int(x['rad_binary'][0]), int(x['rad_binary'][1])))


def absolute(x):
    # The complete signed Q has already been evaluated when this is called.
    if x >= 0:
        return x
    if x <= 0:
        return -x
    # This encloses [0,max|x|], with only outward radius conversion error.
    hi = x.abs_upper()
    return arb(hi / 2, hi / 2)


def load_baseline(s):
    jets = {i['j']: i['complete'] for i in s['integrals'] if i['kind'] == 'jet'}
    check(1 in jets and 2 in jets, 'missing complete saved jet')
    h1, b = decode(jets[1]), decode(jets[2])
    check(h1 < 0 and b < 0, 'saved jet sign not decided')
    selected = {p['j']: p['selected_min'] for p in s['panel_acquisitions']}
    check(set(selected) == {3, 4}, 'unexpected saved selected envelopes')
    u3, u4 = decode(selected[3]), decode(selected[4])
    z = A(R)
    e0 = (z**3 / 6 + z*z) * u3 + z*z*u4 / 2
    e1 = (z + z*z / 2) * u3
    mg = 2*absolute(b)*e0 + (absolute(h1) + z*absolute(b))*e1
    rows = [r for p in s['passes'] for r in p['rows'] if r['rule'] == 'C']
    check(len(rows) == 12, 'expected exactly twelve rule-C rows')
    expected_cases = {(str(r), n) for r in RADII for n in DEGREES}
    check({(r['r'], r['N']) for r in rows} == expected_cases, 'rule-C case set')
    check(all(r['outer'] == '1/32' for r in rows), 'rule-C outer radius changed')
    check(all(r['M_G'] == rows[0]['M_G'] for r in rows), 'rule-C M_G not common')
    # R2 saved binary source/envelope inputs, but printed M_G in its rows.
    # Rebuild the identical formula at the identical precision, using all bits.
    check(all(mg.str(65, more=True) == r['M_G'] for r in rows),
          'binary-reconstructed M_G does not reproduce every rule-C row')
    check(all(arb(r['M_G']).contains(mg) for r in rows),
          'binary-reconstructed M_G not enclosed by printed saved rows')
    return h1, b, mg, {
        'h1_complete_saved': jets[1], 'b_complete_saved': jets[2],
        'h1_decoded': enc(h1), 'b_decoded': enc(b),
        'U3_complete_saved': selected[3], 'U4_complete_saved': selected[4],
        'U3_decoded': enc(u3), 'U4_decoded': enc(u4),
        'M_G_IBP': enc(mg), 'rule_C_rows_checked': len(rows),
        'all_C_rows_same_outer_and_M_G': True,
        'reconstructed_M_G_display_matches_every_saved_C_row': True,
        'printed_rows_contain_reconstruction': True,
        'M_G_reconstruction': 'Note26 (13) in the identical arithmetic order as R2 MG(), from complete saved binary h1,b,U3,U4; no new integration.'}


class Witness:
    def __init__(self):
        self.start = time.monotonic()
        self.deadline = self.start + CAP_SECONDS
        self.evaluations = 0

    def cap(self):
        if time.monotonic() >= self.deadline:
            raise TimeoutError('120-second total arithmetic cap reached')
        if self.evaluations >= CAP_EVALUATIONS:
            raise TimeoutError('3584 range-evaluation cap reached')

    def panels(self, count):
        started = time.monotonic()
        a, b = Fraction(1, 32), Fraction(1, 4)
        width = (b-a) / count
        total = arb(0)
        pi = arb.pi()
        saved = []
        zero_crossings = 0
        for k in range(count):
            self.cap()
            lo, hi = a + k*width, a + (k+1)*width
            u = arb(A((lo+hi)/2), A(width/2))
            # Whole signed polynomial/trigonometric sum is formed before abs.
            q = (6*u - arb(8187)*u**3/2 + u**5/4)*(64*u).sin() \
                + (384*u**2 + 64*u**4)*(64*u).cos()
            expo = (u + u*u/4 - pi*(4*u).exp()).exp()
            check(expo > 0, 'positive exponent interval unresolved')
            zero_crossings += int(q.contains(0))
            contribution = expo*absolute(q)*A(width)
            total += contribution
            self.evaluations += 1
            # Binary contributions expose the actual finite range enclosure;
            # exact interval boundaries follow from a,b,count and this index.
            saved.append({'index': k, 'contribution': enc(contribution)})
        if time.monotonic() >= self.deadline:
            raise TimeoutError('120-second total arithmetic cap reached')
        return total, {
            'panel_count': count, 'range_evaluations': count,
            'width_exact': str(width), 'seconds': time.monotonic()-started,
            'Q_zero_crossing_panels': zero_crossings, 'J_I': enc(total),
            'panel_contributions': saved,
            'panel_contributions_sha256': sha256(json.dumps(saved, sort_keys=True,
                separators=(',', ':')).encode()).hexdigest()}


def lower_costs(gap):
    out = []
    for r in RADII:
        q = r/R
        for n in DEGREES:
            t = q**(n+1)*((n+2)-(n+1)*q)/(1-q)**2
            product = gap*A(t)
            lower = product.lower()
            check(lower > 0, 'nonpositive finite consumer cost-gap bound')
            out.append({'r': str(r), 'N': n, 'q': str(q),
                        'tail_factor_exact': str(t),
                        'cost_gap_product_enclosure': enc(product),
                        'certified_lower_bound': enc(lower)})
    return out


def make_note(data):
    good = data['terminal_status'] == 'certified_domination_of_specified_class'
    lines = [
        '# E01 R3 return: primitive absolute-payment lower-cost witness', '',
        '30 October 2026. Prepared for **Edward Baker** with substantial LLM assistance. '
        'Actual implementation/execution model **gpt-6.1-sol**, reasoning effort **ultra**, '
        'verified from local turn metadata. Internal LLM implementation; no independent '
        'specialist or formal review is claimed. Parent B03 R6; frozen E01 R3 only. '
        'The parent is the sole shared-status/history writer.', '',
        ('**Certified domination of the specified absolute-payment class.** Both '
         'precisions certify $L_{I,\\mathrm{lower}}>M^{\\mathrm{IBP}}_{G,\\mathrm{upper}}$. '
         'The matched direct/C01 consumers retain the accepted R5 bound.' if good else
         '**Unresolved for this fixed witness.** No benefit of the absolute payment '
         'is inferred, and no interval or parameter search is authorized.'), '',
        'The fixed data are $(\\tau,a,R)=(1/4,64,1/32)$ and $I=[1/32,1/4]$. '
        'At every uniform real Arb panel the complete signed $Q$ in B03 R6 (5) '
        'was formed before its absolute-value enclosure; it was multiplied by '
        '$\\exp(u+u^2/4-\\pi e^{4u})$ and the exact width. Arb encloses $\\pi$. '
        'This is a real interval range integral with outward rounding, including '
        'its complete panel discretization enclosure; sampling and holomorphic '
        'quadrature through an absolute value were not used.', '',
        '| Bits | Panels used | $J_I$ enclosure | $L_I$ enclosure | Accepted $M_G^{IBP}$ enclosure |',
        '| --- | --- | --- | --- | --- |']
    for s in data['stages']:
        final = s.get('final')
        if final:
            lines.append(f"| {s['bits']} | {','.join(str(a['panel_count']) for a in s['attempts'])} | `{final['J_I']['ball']}` | `{final['L_I']['ball']}` | `{s['baseline']['M_G_IBP']['ball']}` |")
    lines += ['', 'All displayed decimals are summaries; the JSON preserves binary '
              'midpoints/radii for the complete saved inputs, decoded inputs, all '
              'panel contributions, final enclosures and consumer comparisons. '
              'Binary R2 $h_1,b,\\mathcal U_3,\\mathcal U_4$ were decoded at the '
              'matching precision. R2 stores row $M_G$ as text, so its full interval '
              'was reconstructed using Note26 (13) in the original arithmetic '
              'order. This reproduces the displayed common $M_G$ in every one '
              'of the twelve rule-C rows at each precision; each printed saved '
              'row encloses the reconstruction. No new jets were acquired.', '']
    for s in data['stages']:
        if 'final' not in s:
            continue
        f = s['final']
        lines += [f"At {s['bits']} bits, $L_I-M_G^{{IBP}}$ is `{f['difference']['ball']}`; "
                  f"the strict endpoint gap is `{f['endpoint_gap']['ball']}` and "
                  f"$L_I/M_G^{{IBP}}$ is `{f['ratio']['ball']}`. "
                  f"Panel arithmetic used {sum(x['range_evaluations'] for x in s['attempts'])} "
                  f"range evaluations in {s['arithmetic_seconds']:.6f} seconds.", '']
    if good:
        lines += ['The final $J_I$ and $L_I$ enclosures overlap across 256/384 bits; '
                  'the baseline intervals also overlap. The fixed finite consumer '
                  'cost differences below are lower bounds for '
                  '$(L_{I,\\mathrm{lower}}-M_{G,\\mathrm{upper}}^{IBP})T_N(r/R)$. '
                  'They are **margin-cost comparisons**, not newly acquired physical margins.', '',
                  '| $r$ | $N$ | 256-bit lower bound | 384-bit lower bound |',
                  '| --- | --- | --- | --- |']
        first, second = data['stages']
        for x,y in zip(first['consumer_cost_lower_bounds'], second['consumer_cost_lower_bounds']):
            lines.append(f"| {x['r']} | {x['N']} | `{x['certified_lower_bound']['ball']}` | `{y['certified_lower_bound']['ball']}` |")
        lines += ['', 'By B03 R6 (4)/(8), every bound paying the full joint primitive '
                  'integrand by absolute value before source integration, with its '
                  'stated finite-$U\\ge1$ boundary/exterior or whole-line payment, '
                  'costs more than the accepted IBP envelope at this center and '
                  'outer radius. It cannot improve the same-radius, same-degree '
                  'consumer margin or minimum passing degree. This invokes the '
                  'issued proof; E02 R6 still owns its assessment.', '']
    lines += ['Only the first positive primitive mode and $I$ enter this **lower** '
              'bound. Omitted primitive modes and the source complement contribute '
              'nonnegatively to B03 R6 (4), so no omitted-tail **upper** payment is '
              'needed for this witness. The saved $h_1$ remains the complete signed '
              'theta jet. This neither truncates the physical source nor encloses '
              'its complete primitive payment from above.', '',
              'The result is restricted to the issued absolute-payment class, center, '
              'outer radius and unchanged matched consumers. Signed source-panel '
              'integration, cross-piece cancellation, other references and $U<1$ '
              'are outside that class. No global covering, physical collision, '
              'theta-zero exclusion, RH statement or new spatial floor follows.', '',
              f"Total arithmetic: {data['cost']['range_evaluations']} range evaluations, "
              f"{data['cost']['arithmetic_seconds']:.6f} seconds; caps 3584 and 120 seconds. "
              f"python-flint {data['runtime']['python_flint']}; FLINT {data['runtime']['flint']}. "
              'The record includes exact frozen-input and script hashes. All inputs '
              'were unchanged. Only this note, the permitted script and JSON were written.', '',
              'Runnable evidence: [script](../../numerics/fixed_coefficient_parameter_geometry/execute_fcg_e01_r3.py), '
              '[JSON](../../numerics/fixed_coefficient_parameter_geometry/fcg_e01_r3_primitive_absolute_payment_20261030.json), '
              '[issued packet](../../research-progress/handoffs/fixed_coefficient_parameter_geometry/FCG-E01_R3_PRIMITIVE_ABSOLUTE_PAYMENT_20261030.md), '
              '[parent proof](B03_R6_PRIMITIVE_ABSOLUTE_PAYMENT_OBSTRUCTION_20261030.md). '
              'Interpretation follows the [result index](../../../../../result-summaries/README.md), '
              '[theta bookkeeping](../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md), '
              '[avoid index](../../../../../avoid/README.md), especially '
              '[separate absolute bounds](../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md) and '
              '[scoped exclusions](../../../../../avoid/07_scoped_exclusions_read_as_universal.md).', '']
    if data.get('error'):
        lines += ['Error/cap return: `' + data['error'] + '`.', '']
    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[5])
    args = parser.parse_args()
    root = args.root.resolve()
    for p,h in FROZEN.items():
        check(sha256((root/p).read_bytes()).hexdigest() == h, 'frozen input hash mismatch: '+p)
    source = json.loads((root/INPUT).read_text())
    check([s['bits'] for s in source['stages']] == list(BITS), 'saved precision set')
    check(source['fixed']['tau'] == '1/4' and source['fixed']['a'] == '64'
          and source['fixed']['R'] == '1/32', 'saved center/outer radius')
    data = {
        'task': 'FCG-E01 R3', 'date': '2026-10-30', 'prepared_for': 'Edward Baker',
        'llm_assistance': 'Substantial; internal implementation/execution, not specialist independence',
        'model': 'gpt-6.1-sol', 'effort': 'ultra',
        'model_provenance': 'Implementing agent local turn_context model/effort fields',
        'implementing_thread_id': '01a18dc8-dee6-7423-a420-5efce432e84c',
        'parent_thread_id': '01a18dc4-d540-7f43-8874-81dafca23151',
        'separate_chat_registration': False,
        'fixed': {'tau':'1/4','a':'64','R':'1/32','I':['1/32','1/4'],
                  'radii':[str(r) for r in RADII], 'degrees':list(DEGREES),
                  'integrand':'exp(u+u^2/4-pi*exp(4u))*abs((6u-8187u^3/2+u^5/4)*sin(64u)+(384u^2+64u^4)*cos(64u))'},
        'limits': {'precisions':list(BITS), 'uniform_panel_counts':list(COUNTS),
                   'total_arithmetic_seconds':CAP_SECONDS,'total_range_evaluations':CAP_EVALUATIONS},
        'runtime': {'python':sys.version,'executable':sys.executable,
                    'python_flint':flint.__version__,
                    'flint':getattr(flint,'__FLINT_VERSION__','unavailable'),
                    'platform':platform.platform()},
        'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
        'inputs':[{'path':p,'sha256':h} for p,h in FROZEN.items()],
        'stages':[], 'terminal_status':'in_progress'}
    run = Witness()
    signal.signal(signal.SIGALRM, lambda sig, frame: (_ for _ in ()).throw(TimeoutError('120-second arithmetic alarm')))
    signal.setitimer(signal.ITIMER_REAL, CAP_SECONDS)
    final_values = []
    try:
        for saved_stage in source['stages']:
            stage_start = time.monotonic()
            ctx.prec = saved_stage['bits']
            h1,b,mg,baseline = load_baseline(saved_stage)
            stage = {'bits':ctx.prec, 'baseline':baseline, 'attempts':[]}
            data['stages'].append(stage)
            for count in COUNTS:
                j, acquisition = run.panels(count)
                li = A(R)*absolute(h1)*j/8
                difference = li-mg
                gap = li.lower()-mg.upper()
                ratio = li/mg if mg > 0 else None
                final = {'J_I':enc(j),'L_I':enc(li),'difference':enc(difference),
                         'endpoint_gap':enc(gap),'ratio':enc(ratio) if ratio is not None else None,
                         'L_lower_strictly_above_M_upper':bool(gap > 0),
                         'accepted_M_positive':bool(mg > 0)}
                acquisition['comparison'] = final
                stage['attempts'].append(acquisition)
                stage['final'] = final
                if gap > 0:
                    stage['consumer_cost_lower_bounds'] = lower_costs(gap.lower())
                    break
            stage['arithmetic_seconds'] = time.monotonic()-stage_start
            final_values.append((j,li,mg,h1,b))
            print('bits',ctx.prec,'panels',[x['panel_count'] for x in stage['attempts']],
                  'J',j.str(15,more=True),'L',li.str(15,more=True),
                  'M',mg.str(15,more=True),'strict',gap>0,flush=True)
        ctx.prec = 384
        overlap = {key: bool(final_values[0][i].overlaps(final_values[1][i]))
                   for i,key in enumerate(('J_I','L_I','M_G_IBP','h1','b'))}
        check(all(overlap.values()), 'cross-precision disjoint enclosure: '+str(overlap))
        data['cross_precision_overlaps'] = overlap
        data['terminal_status'] = ('certified_domination_of_specified_class' if
            all(s['final']['L_lower_strictly_above_M_upper'] for s in data['stages'])
            else 'unresolved_for_fixed_witness')
    except TimeoutError as e:
        data['terminal_status'] = 'unresolved_for_fixed_witness'
        data['error'] = str(e)
    except Exception as e:
        data['terminal_status'] = 'implementation_failure'
        data['error'] = type(e).__name__+': '+str(e)
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
    data['cost'] = {'range_evaluations':run.evaluations,
                    'arithmetic_seconds':time.monotonic()-run.start}
    data['recorded_utc'] = datetime.now(timezone.utc).isoformat()
    data['scope'] = ('Necessary cost of the issued absolute-payment class at one fixed center '
                     'and outer radius, compared at unchanged R5 consumers; no global or zero claim.')
    # Recheck frozen inputs before creating either permitted output.
    for p,h in FROZEN.items():
        check(sha256((root/p).read_bytes()).hexdigest() == h, 'input changed during execution: '+p)
    payload = json.dumps(data, indent=2)+'\n'
    check(len(payload.encode()) < 1048576, 'record exceeds 1 MiB')
    (root/OUTPUT).write_text(payload)
    (root/NOTE).write_text(make_note(data))
    print(data['terminal_status'],data['cost'], 'JSON bytes',len(payload.encode()),flush=True)
    if data['terminal_status'] == 'implementation_failure':
        raise SystemExit(2)


if __name__ == '__main__':
    main()
