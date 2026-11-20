#!/usr/bin/env python3
"""Fixed AGC E12 interval pilot for Edward Baker, 2026-11-19.

Codex LLM assistance; requested helper dispatch gpt-6.1-sol/ultra.
Actual backend/effort attestation unavailable. No parameter search.
"""
import hashlib
import json
import platform
import sys
from pathlib import Path
from time import perf_counter

import flint
from flint import arb, acb, fmpq, ctx

BASE = Path(__file__).resolve().parents[1]
OUT = BASE / 'numerics/03_AGC_FIXED_CELL_COMPARISON_20261119.json'
SCHEDULE = ((16, 128), (32, 256), (64, 512))
ctx.prec = 192
PI = arb.pi()
X = arb(fmpq(140101, 10))
A, H, RAD = arb(2), arb(1), arb(fmpq(9, 10))
TMIN, TMAX, U = arb(fmpq(9, 100)), arb(fmpq(1, 10)), arb(fmpq(1, 100))
N = 33
LOGS = [arb(n).log() for n in range(1, N+1)]
SCALELOG = PI*X/8
started = perf_counter()


def enc(v):
    return str(v)


def box(lo, hi):
    return arb((lo+hi)/2, ((hi-lo)/2).upper())


def upper(v):
    return v.upper()


def l0(s):
    return (s.log()+(s-1).log()-s*PI.log()/2
            +(2*PI).sqrt().log()-arb(16).log()
            +(s/2-arb(fmpq(1, 2)))*(s/2).log()-s/2)


def alpha(s):
    return 1/(2*s)+1/(s-1)+(s/(2*PI)).log()/2


def fields(t, z, source=True):
    """Natural interval inclusion over all t,z in the input boxes."""
    P, R, V = acb(0), acb(0), arb(0)
    T = z.real/2
    for s in ((1+acb(0, 1)*z)/2, (1-acb(0, 1)*z)/2):
        al = alpha(s)
        b = -1/(2*s*s)-1/((s-1)**2)+1/(2*s)
        c = 1/(s**3)+2/((s-1)**3)-1/(2*s*s)
        common = l0(s)+SCALELOG
        for ln in LOGS:
            an = al-ln
            p = (common-s*ln+t*an*an/4).exp()
            P += p
            F = b+t*an*an*b+t*(b*b+an*c)/2+t*t*an*an*b*b/4
            R -= p*F/4
            if source:
                eps = ((t*t*abs(an)**2/8+t/4+arb(fmpq(1, 6)))
                       /(T-arb('3.33'))).expm1()
                V += abs(p)*eps
    if source:
        eta = abs(z.imag)
        tp = T+PI*t/8
        ars = (tp/(2*PI)).sqrt()
        common_delta = 5/(3*(T-6))
        delta_factor = (arb('3.49')/(T-4)).exp()
        ds = []
        for sigma in ((1-eta)/2, (1+eta)/2):
            ds.append((arb('0.397')*(sigma*arb(9).log()).exp()
                       /(ars-arb('0.865'))+common_delta)*delta_factor)
        rem = (t*PI*PI/64+l0(acb(0, tp)).real+SCALELOG).exp()
        V += rem*(1+ds[0]+ds[1])
    return P, R, V


def unit(j, m, arc=False):
    angle = 2*PI*arb(fmpq(j, m))
    if arc:
        angle += box(arb(0), 2*PI/m)
    return acb(angle.cos(), angle.sin())


def defect_uniform():
    """E11 (4), scaled by the fixed positive physical scale."""
    d = X-A
    t0, ss = d/2, (1+H)/2
    q = (1-H)/2
    t1 = 2*PI*(N+1)**2
    qq = (t1*t1+ss*ss).sqrt()
    b = 1/(2*t0)+3/(2*t0*t0)
    c = 1/(2*t0*t0)+3/(t0**3)
    k0 = ((2*PI).sqrt()/16*(t0*t0+ss*ss)
          *(SCALELOG-PI*t0/4).exp())
    total = arb(0)
    for n, ln in enumerate(LOGS, 1):
        ll = abs((t0/(2*PI*n*n)).log()).max(abs((qq/(2*PI*n*n)).log()))
        an = 3/(2*t0)+(ll*ll+PI*PI/4).sqrt()/2
        gg = b+TMAX*an*an*b+TMAX*(b*b+an*c)/2+TMAX*TMAX*an*an*b*b/4
        total += (-q*ln+TMAX*an*an/4).exp()*gg
    return upper(k0*total/2)


def moments(t, m, min_log_bound, max_log_bound):
    """Laurent moments, with t-cell variation and rigorous two-sided aliases."""
    vals = []
    for j in range(m):
        w = RAD*unit(j, m)
        p, _, _ = fields(t, acb(X)+w, False)
        f = p/(w*w)
        if not f.real > 0:
            return None
        vals.append(f.log())
    aa = []
    inner, outer = arb(fmpq(4, 5)), arb(1)
    ao, ai = (RAD/outer)**m, (inner/RAD)**m
    aliases = []
    for k in (1, 2):
        coeff = RAD**k*sum((vals[j]*unit(k*j, m) for j in range(m)), acb(0))/m
        alias = (max_log_bound*outer**k*ao/(1-ao)
                 +min_log_bound*inner**k*ai/(1-ai)).upper()
        coeff += acb(arb(0, alias), arb(0, alias))
        aa.append(coeff)
        aliases.append(alias)
    center = -aa[0]/2
    disc = -aa[1]-aa[0]*aa[0]/4
    return {'center_offset': enc(center), 'center_abs_upper': enc(abs(center).upper()),
            'D_P_real': enc(disc.real), 'D_P_imag_inclusion': enc(disc.imag),
            'D_P_lower': enc(disc.real.lower()),
            'alias_a_minus1_upper': enc(aliases[0]),
            'alias_a_minus2_upper': enc(aliases[1]),
            '_center': abs(center).upper(), '_D': disc.real}


def attempt(nt, m):
    print(f'run geometry {nt} time cells, {m} closed arcs', flush=True)
    rows = []
    total_count = True
    for it in range(nt):
        lo = TMIN+(TMAX-TMIN)*arb(fmpq(it, nt))
        hi = TMIN+(TMAX-TMIN)*arb(fmpq(it+1, nt))
        t = box(lo, hi)
        m_floor, re_floor = None, None
        vmax, rmax, qlocal = arb(0), arb(0), arb(0)
        log_bounds = {}
        counts = {}
        for ir, radius in enumerate((arb(fmpq(4, 5)), RAD, arb(1))):
            f_re, lmax = None, arb(0)
            for j in range(m):
                w = radius*unit(j, m, True)
                p, rr, v = fields(t, acb(X)+w, ir == 1)
                f = p/(w*w)
                this_re = f.real.lower()
                f_re = this_re if f_re is None else f_re.min(this_re)
                if f.real > 0:
                    lmax = lmax.max(abs(f.log()).upper())
                else:
                    lmax = arb('inf')
                if ir == 1:
                    pp = p.abs_lower()
                    m_floor = pp if m_floor is None else m_floor.min(pp)
                    vmax = vmax.max(v.upper())
                    rmax = rmax.max(abs(rr).upper())
                    local_ratio = (v.upper()/pp).upper() if pp > 0 else arb('inf')
                    qlocal = qlocal.max(local_ratio)
            key = str(radius.mid())
            counts[key] = bool(f_re > 0)
            log_bounds[key] = lmax
            if ir == 1:
                re_floor = f_re
        main_count = bool(re_floor > 0)
        total_count = total_count and main_count
        qglobal = (vmax/m_floor).upper() if m_floor > 0 else arb('inf')
        q = qlocal.upper()
        row = {'time_index': it, 't_cell': enc(t), 'm_P_scaled_lower': enc(m_floor),
               'raw_error_scaled_upper': enc(vmax), 'q_raw_upper': enc(q),
               'q_global_sup_over_inf_upper': enc(qglobal),
               'q_definition': 'maximum of paid local source/denominator ratios on the same arcs',
               'reference_defect_scaled_upper_on_Gamma': enc(rmax),
               'Re_P_over_w2_lower': enc(re_floor), 'reference_count_two': main_count,
               'annulus_boundary_positive': all(counts.values()),
               'annulus_log_bounds': {k: enc(v) for k, v in log_bounds.items()},
               '_q': q, '_v': vmax, '_m': m_floor, '_t': t}
        if all(counts.values()) and q < 1:
            moment = moments(t, m, log_bounds[str(arb(fmpq(4, 5)).mid())],
                             log_bounds[str(arb(1).mid())])
            if moment:
                row.update(moment)
                lam = -(1-q).log()
                d = moment['_center']/RAD
                sep = RAD*RAD*((1+d)*lam+lam*lam/4)
                old = RAD*RAD*(lam*(1+d*d).sqrt()+lam*lam/4)
                eta = ((1+q)/(1-q)).log()/2
                refined_c = RAD*RAD*(eta*(1+d*d).sqrt()+eta*eta/4)
                refined_p = RAD*RAD*(eta+eta*d*d/(2-eta)) if eta < 2 else refined_c
                refined = refined_c.min(refined_p)
                row['raw_log_lambda_upper'] = enc(lam.upper())
                row['centered_log_eta_upper'] = enc(eta.upper())
                row['independent_moment_gap_allowance_upper'] = enc(sep.upper())
                row['raw_gap_allowance_upper'] = enc(old.upper())
                row['raw_complete_D_H_lower'] = enc((moment['_D']-old).lower())
                row['refined_Cauchy_gap_allowance_upper'] = enc(refined_c.upper())
                row['refined_parabolic_gap_allowance_upper'] = enc(refined_p.upper())
                row['refined_gap_allowance_upper'] = enc(refined.upper())
                row['refined_complete_D_H_lower'] = enc((moment['_D']-refined).lower())
                row['refined_strictly_smaller_than_strong_E10'] = bool(refined < old)
                row['refined_protects_time_cell'] = bool(moment['_D']-refined > 0)
        rows.append(row)
        print(f'cell {it+1}/{nt}: count={main_count}, q<1={bool(q<1)}', flush=True)
    return rows, total_count


def clean(obj):
    if isinstance(obj, dict):
        return {k: clean(v) for k, v in obj.items() if not k.startswith('_')}
    if isinstance(obj, list):
        return [clean(v) for v in obj]
    return obj


def main():
    cutlow = (X-A)/(4*PI)+TMIN/16
    cuthi = (X+A)/(4*PI)+TMAX/16
    cutoff = bool(cutlow >= N*N and cuthi < (N+1)**2)
    result = {'date': '2026-11-19', 'prepared_for': 'Edward Baker',
              'LLM_assistance': 'OpenAI Codex',
              'dispatch_metadata': 'gpt-6.1-sol / ultra requested in packet',
              'actual_backend_model': None, 'actual_effort': None,
              'python': platform.python_version(), 'python_flint': flint.__version__,
              'precision_bits': ctx.prec, 'scale': 'exp(pi X/8), positive constant',
              'parameters': {'X': '140101/10', 'A': '2', 'h': '1', 'r': '9/10',
                             't_min': '9/100', 't_max': '1/10', 'N': N},
              'cutoff': {'passed': cutoff, 'lower': enc(cutlow), 'upper': enc(cuthi)},
              'known_coverage': 'pilot inside earlier canonical coverage; no new coverage claim',
              'quadrature': 'M-point Laurent trapezoid with two annulus alias payments; t interval included',
              'interval_cover': 'closed rational time cells and closed angle arcs; Arb outward rounding',
              'attempts': []}
    if not cutoff:
        raise RuntimeError('frozen cutoff failed')
    rows = []
    for nt, m in SCHEDULE:
        rows, count = attempt(nt, m)
        result['attempts'].append({'time_cells': nt, 'contour_arcs': m,
                                   'count_gate': count, 'all_q_below_one': all(r['_q']<1 for r in rows),
                                   'rows': clean(rows), 'elapsed_seconds': perf_counter()-started})
        OUT.write_text(json.dumps(result, indent=2)+'\n')
        # Parent authorized the last scheduled refinement to reduce geometric wrapping.
        if perf_counter()-started > 12*60:
            break
    # Complete, conservative bounded-heat data acquired on the full horizontal rectangle.
    initial_z = acb(box(X-A, X+A), box(arb(0), RAD))
    _, _, init = fields(TMAX, initial_z)
    eps0 = init.upper()
    mb = arb(0)
    for side in (X-A, X+A):
        _, _, vv = fields(box(TMIN, TMAX), acb(side, box(arb(0), RAD)))
        mb = mb.max(vv.upper())
    rho = defect_uniform()
    beta = (((-(A-RAD)/(2*U.sqrt())).erf()+1)
            +((-(A+RAD)/(2*U.sqrt())).erf()+1)).min(arb(1))
    heat = eps0+(mb-eps0)*beta+U*rho if mb >= eps0 else eps0+U*rho
    raw_uniform = arb(0)
    for row in rows:
        raw_uniform = raw_uniform.max(row['_v'])
    result['heat_conservative'] = {'initial_scaled_upper': enc(eps0),
        'full_time_both_lateral_scaled_upper': enc(mb), 'full_rectangle_defect_scaled_upper': enc(rho),
        'beta_Gamma_at_U_upper': enc(beta.upper()), 'uniform_heat_scaled_upper': enc(heat.upper()),
        'retained_survival_note': 'exact initial mass accounted; if Mb<eps0 used safe eps0+U*rho',
        'raw_Gamma_scaled_upper': enc(raw_uniform),
        'heat_strictly_improves_raw_uniform': bool(heat < raw_uniform)}
    src = [Path(__file__), BASE/'notes/04_AGC_E10_CONTOUR_ENDPOINT_20261119.md',
           BASE/'notes/05_AGC_E10_BOUNDED_HEAT_20261119.md', BASE/'notes/06_AGC_E11_SOURCE_ALLOWANCE_20261119.md',
           BASE/'brainstorm/notes/04_AGC_B01_FIXED_PILOT_ADDENDUM_20261119.md',
           BASE/'notes/08_AGC_E13_LOG_DISK_ALLOWANCE_20261119.md']
    result['source_sha256'] = {str(p.relative_to(BASE)): hashlib.sha256(p.read_bytes()).hexdigest() for p in src}
    result['elapsed_seconds'] = perf_counter()-started
    result['certificate_scope'] = 'Every reported ball is an outward interval inclusion. Gates are explicit; failed gates do not certify a gap.'
    result['refined_all_time_positive_margin'] = all(r.get('refined_protects_time_cell', False) for r in rows)
    result['refined_all_time_strictly_smaller'] = all(r.get('refined_strictly_smaller_than_strong_E10', False) for r in rows)
    OUT.write_text(json.dumps(result, indent=2)+'\n')
    print('saved', OUT, 'elapsed', result['elapsed_seconds'], flush=True)


if __name__ == '__main__':
    main()
