#!/usr/bin/env python3
"""AGC E12 r2 fixed corrected-reference certificate for Edward Baker.

2026-11-19; OpenAI Codex LLM assistance. Dispatch gpt-6.1-sol/ultra;
actual backend model/effort attestation unavailable. One frozen geometry.
"""
import argparse
import hashlib
import importlib.util
import json
import platform
from pathlib import Path
from time import perf_counter

import flint
from flint import arb, acb, fmpq, ctx

BASE = Path(__file__).resolve().parents[1]
BASE_CODE = BASE/'numerics/agc_fixed_cell_comparison.py'
PRIOR_RECORD = BASE/'numerics/03_AGC_FIXED_CELL_COMPARISON_20261119.json'
BASE_SHA = '9c6b6fd6f19cd716582f1569cea0d38ba0da3c7a3a2a4847bac78242d3160cda'
PRIOR_SHA = '6f97ba677fd59382dae07ef185e6ab51352a1aae952c761c230a918b3628fb05'
OUT = BASE/'numerics/05_AGC_CORRECTED_REFERENCE_COMPARISON_20261119.json'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


if sha(BASE_CODE) != BASE_SHA or sha(PRIOR_RECORD) != PRIOR_SHA:
    raise RuntimeError('frozen r1 implementation/record hash mismatch')
spec = importlib.util.spec_from_file_location('agc_frozen_r1', BASE_CODE)
old = importlib.util.module_from_spec(spec)
spec.loader.exec_module(old)
ctx.prec = 192
PI, X, RAD = old.PI, old.X, old.RAD
K = PI/8
NT, M = 64, 512
I = acb(0, 1)


def correction(t, z):
    w = z/2+K*t
    p = 2*old.N+1-2*(w/(2*PI)).sqrt()
    if not (p.real > arb(fmpq(9, 50)) and p.real < arb(fmpq(6, 25))
            and abs(p.imag) < arb(fmpq(1, 400))):
        raise RuntimeError('accepted local correction patch not enclosed')
    den = 2*(PI*p).cos()
    if not den.abs_lower() > arb(fmpq(7, 5)):
        raise RuntimeError('correction denominator clearance failed')
    theta = PI*(p*p/2+arb(fmpq(3, 8)))
    cs = (PI*p/2).cos()
    cp = ((I*theta).exp()-I*arb(2).sqrt()*cs)/den
    cm = ((-I*theta).exp()+I*arb(2).sqrt()*cs)/den
    an = w.sqrt()*((w+I)*cp+(w-I)*cm)/2
    js = ((-1)**(old.N+1)*PI.sqrt()/4
          *(K*(acb(X)-z)-K*K*t).exp())
    return js*an, js, p


def fields(t, z, source=True):
    """Return Q_scaled, conservative |R_Q,scaled| bound, and full V_Q."""
    pp, rp, _ = old.fields(t, z, False)
    cc, js, _ = correction(t, z)
    qq = pp-cc
    defect = abs(rp).upper()+350*abs(js).upper()
    terms, retained, mismatch = arb(0), arb(0), arb(0)
    if source:
        T = z.real/2
        for s in ((1+I*z)/2, (1-I*z)/2):
            al = old.alpha(s)
            common = old.l0(s)+old.SCALELOG
            for ln in old.LOGS:
                an = al-ln
                pn = (common-s*ln+t*an*an/4).exp()
                eps = ((t*t*abs(an)**2/8+t/4+arb(fmpq(1, 6)))
                       /(T-arb('3.33'))).expm1()
                terms += abs(pn)*eps
        eta = abs(z.imag)
        tp = T+K*t
        ars = (tp/(2*PI)).sqrt()
        delta = arb(0)
        for sigma in ((1-eta)/2, (1+eta)/2):
            delta += ((arb('0.397')*(sigma*arb(9).log()).exp()
                       /(ars-arb('0.865'))+5/(3*(T-6)))
                      *(arb('3.49')/(T-4)).exp())
        leading = (t*PI*PI/64+old.l0(acb(0, tp)).real+old.SCALELOG).exp()
        retained = leading*delta
        mismatch = 12000*abs(js)*eta
    return qq, defect.upper(), (terms+retained+mismatch).upper(), {
        'term': terms.upper(), 'retained': retained.upper(),
        'mismatch': mismatch.upper(), 'correction': abs(cc).upper(),
        'J': abs(js).upper()}


def moments(t, minlog, maxlog):
    vals = []
    for j in range(M):
        w = RAD*old.unit(j, M)
        qq, _, _, _ = fields(t, acb(X)+w, False)
        ff = qq/(w*w)
        if not ff.real > 0:
            raise RuntimeError('principal Q logarithm not cleared at moment node')
        vals.append(ff.log())
    inner, outer = arb(fmpq(4, 5)), arb(1)
    ao, ai = (RAD/outer)**M, (inner/RAD)**M
    coeffs, aliases = [], []
    for k in (1, 2):
        cc = RAD**k*sum((vals[j]*old.unit(k*j, M) for j in range(M)), acb(0))/M
        alias = (maxlog*outer**k*ao/(1-ao)+minlog*inner**k*ai/(1-ai)).upper()
        coeffs.append(cc+acb(arb(0, alias), arb(0, alias)))
        aliases.append(alias)
    center = -coeffs[0]/2
    disc = -coeffs[1]-coeffs[0]*coeffs[0]/4
    return center, disc, aliases


def extrema(rows, key, is_min=False):
    val = rows[0][key]
    for row in rows[1:]:
        val = val.min(row[key]) if is_min else val.max(row[key])
    return val


def public(row):
    return {key: str(value) if isinstance(value, (arb, acb)) else value
            for key, value in row.items() if not key.startswith('_')}


def main(output=None):
    started = perf_counter()
    output = Path(output) if output else OUT
    reviews = sorted((BASE/'reviews').glob('05_*.md'))
    if len(reviews) != 1:
        raise RuntimeError('expected one saved accepted Review05 before source pinning')
    sources = [Path(__file__), BASE_CODE, PRIOR_RECORD,
               BASE/'notes/04_AGC_E10_CONTOUR_ENDPOINT_20261119.md',
               BASE/'notes/06_AGC_E11_SOURCE_ALLOWANCE_20261119.md',
               BASE/'notes/08_AGC_E13_LOG_DISK_ALLOWANCE_20261119.md',
               BASE/'notes/10_AGC_E13_R2_HOLOMORPHIC_CORRECTION_20261119.md',
               reviews[0], BASE/'research-progress/handoffs/AGC-E12-r2-request.md',
               BASE/'brainstorm/notes/05_AGC_B02_R2_RETAINED_CORRECTION_CONTRACT_20261119.md']
    hashes = {str(p.relative_to(BASE)): sha(p) for p in sources}
    prior = json.loads(PRIOR_RECORD.read_text())
    prior_rows = prior['attempts'][-1]['rows']
    if prior['attempts'][-1]['time_cells'] != NT or prior['attempts'][-1]['contour_arcs'] != M:
        raise RuntimeError('prior geometry changed')
    low = (X-old.A)/(4*PI)+old.TMIN/16
    high = (X+old.A)/(4*PI)+old.TMAX/16
    if not (low >= old.N**2 and high < (old.N+1)**2):
        raise RuntimeError('natural-cutoff gate failed')
    result = {'date': '2026-11-19', 'prepared_for': 'Edward Baker',
              'LLM_assistance': 'OpenAI Codex', 'dispatch': 'gpt-6.1-sol/ultra',
              'actual_backend_model': None, 'actual_effort': None,
              'python': platform.python_version(), 'python_flint': flint.__version__,
              'precision_bits': ctx.prec, 'time_cells': NT, 'closed_arcs': M,
              'parameters': prior['parameters'], 'radii': ['4/5', '9/10', '1'],
              'scale': 'exp(pi X/8), positive constant independent of t,z',
              'reference': 'Q33=P33-C_hol from accepted Note10',
              'source_allowance': 'both term errors + full retained delta remainder + 12000 |J_scaled| |y|',
              'defect_scope': 'conservative bound |R_Q,scaled| <= |R_P,scaled|+350|J_scaled|; not exact complex R_Q',
              'derivative_constants': {'A_prime_upper': 24000, 'A_second_upper': 1400},
              'known_coverage': 'same already-covered fixed cell; no new coverage or Newman bound',
              'cutoff': {'passed': True, 'lower': str(low), 'upper': str(high)},
              'source_sha256_at_start': hashes, 'rows': []}
    rows = []
    print('fixed Q run: 192 bits,64 time cells,512 closed arcs', flush=True)
    for it in range(NT):
        lo = old.TMIN+(old.TMAX-old.TMIN)*arb(fmpq(it, NT))
        hi = old.TMIN+(old.TMAX-old.TMIN)*arb(fmpq(it+1, NT))
        t = old.box(lo, hi)
        logs, positive = {}, {}
        mlow = None
        vtotal, qlocal, rbound = arb(0), arb(0), arb(0)
        components = {key: arb(0) for key in ('term', 'retained', 'mismatch', 'correction', 'J')}
        for ir, radius in enumerate((arb(fmpq(4, 5)), RAD, arb(1))):
            refloor, logmax = None, arb(0)
            for j in range(M):
                w = radius*old.unit(j, M, True)
                qq, rr, vv, cc = fields(t, acb(X)+w, ir == 1)
                ff = qq/(w*w)
                refloor = ff.real.lower() if refloor is None else refloor.min(ff.real.lower())
                logmax = logmax.max(abs(ff.log()).upper()) if ff.real > 0 else arb('inf')
                if ir == 1:
                    denom = qq.abs_lower()
                    mlow = denom if mlow is None else mlow.min(denom)
                    vtotal = vtotal.max(vv)
                    qlocal = qlocal.max((vv/denom).upper()) if denom > 0 else arb('inf')
                    rbound = rbound.max(rr)
                    for key in components:
                        components[key] = components[key].max(cc[key])
            logs[ir], positive[ir] = logmax, bool(refloor > 0)
            if ir == 1:
                qrefloor = refloor
        row = {'time_index': it, 't_cell': t, 'm_Q_scaled_lower': mlow,
               'V_Q_scaled_upper': vtotal, 'q_Q_local_upper': qlocal,
               'q_Q_global_sup_over_inf_upper': (vtotal/mlow).upper() if mlow > 0 else arb('inf'),
               'Re_Q_over_w2_lower': qrefloor, 'count_Q_two': positive[1],
               'annulus_boundary_positive': all(positive.values()),
               'log_inner_upper': logs[0], 'log_outer_upper': logs[2],
               'conservative_Q_defect_scaled_upper_on_Gamma': rbound,
               **{f'{key}_scaled_upper_on_Gamma': value for key, value in components.items()},
               'prior_P_refined_complete_D_H_lower': arb(prior_rows[it]['refined_complete_D_H_lower'])}
        if all(positive.values()) and qlocal < 1:
            center, disc, aliases = moments(t, logs[0], logs[2])
            d = abs(center).upper()/RAD
            lam = -(1-qlocal).log()
            eta = ((1+qlocal)/(1-qlocal)).log()/2
            e10 = RAD*RAD*(lam*(1+d*d).sqrt()+lam*lam/4)
            ec = RAD*RAD*(eta*(1+d*d).sqrt()+eta*eta/4)
            ep = RAD*RAD*(eta+eta*d*d/(2-eta)) if eta < 2 else ec
            refined = ec.min(ep)
            newlower = (disc.real-refined).lower()
            row.update({'center_Q_offset': center, 'center_Q_abs_upper': abs(center).upper(),
                        'D_Q_real': disc.real, 'D_Q_imag_inclusion': disc.imag,
                        'D_Q_lower': disc.real.lower(), 'D_Q_upper': disc.real.upper(),
                        'alias_a_minus1_upper': aliases[0], 'alias_a_minus2_upper': aliases[1],
                        'lambda_Q_upper': lam.upper(), 'eta_Q_upper': eta.upper(),
                        'E10_Q_allowance_upper': e10.upper(),
                        'refined_Q_Cauchy_upper': ec.upper(), 'refined_Q_parabolic_upper': ep.upper(),
                        'refined_Q_allowance_upper': refined.upper(),
                        'E10_Q_complete_D_H_lower': (disc.real-e10).lower(),
                        'refined_Q_complete_D_H_lower': newlower,
                        'refined_Q_positive': bool(newlower > 0),
                        'refined_Q_strictly_smaller_than_E10_Q': bool(refined < e10),
                        'Q_lower_strictly_exceeds_prior_P_lower': bool(newlower > row['prior_P_refined_complete_D_H_lower'])})
        rows.append(row)
        result['rows'] = [public(r) for r in rows]
        result['completed_time_cells'] = len(rows)
        result['elapsed_seconds'] = perf_counter()-started
        output.write_text(json.dumps(result, indent=2)+'\n')
        print(f'cell {it+1}/64: count={positive[1]},q<1={bool(qlocal<1)},positive={row.get("refined_Q_positive",False)}', flush=True)
        if perf_counter()-started > 900:
            raise RuntimeError('15-minute program-runtime cap reached; partial record preserved')
    result['all_time_count_Q_two'] = all(r['count_Q_two'] for r in rows)
    result['all_time_annulus_positive'] = all(r['annulus_boundary_positive'] for r in rows)
    result['all_time_q_below_one'] = all(r['q_Q_local_upper'] < 1 for r in rows)
    result['all_time_refined_positive'] = all(r.get('refined_Q_positive', False) for r in rows)
    result['all_time_Q_lower_exceeds_prior_P_lower'] = all(r.get('Q_lower_strictly_exceeds_prior_P_lower', False) for r in rows)
    names = {'m_Q_scaled_lower': True, 'V_Q_scaled_upper': False, 'q_Q_local_upper': False,
             'conservative_Q_defect_scaled_upper_on_Gamma': False, 'D_Q_lower': True,
             'center_Q_abs_upper': False, 'E10_Q_allowance_upper': False,
             'refined_Q_allowance_upper': False, 'E10_Q_complete_D_H_lower': True,
             'refined_Q_complete_D_H_lower': True}
    result['uniform_summary'] = {key: str(extrema(rows, key, mn)) for key, mn in names.items()
                                 if all(key in row for row in rows)}
    result['prior_P_uniform_refined_lower'] = str(extrema(rows, 'prior_P_refined_complete_D_H_lower', True))
    result['source_hashes_unchanged_during_run'] = all(sha(BASE/p) == digest for p, digest in hashes.items())
    result['r1_scientific_files_still_pinned'] = sha(BASE_CODE) == BASE_SHA and sha(PRIOR_RECORD) == PRIOR_SHA
    result['elapsed_seconds'] = perf_counter()-started
    output.write_text(json.dumps(result, indent=2)+'\n')
    print('saved',output,'runtime_seconds',result['elapsed_seconds'],flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, help='scratch replay destination; mathematical inputs stay fixed')
    main(parser.parse_args().output)
