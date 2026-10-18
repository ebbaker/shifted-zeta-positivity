#!/usr/bin/env python3
"""Bounded complete-source near-boundary evaluator; point evaluation for overview 02.
Prepared for Edward Baker, 2026-10-18, with LLM assistance.
Actual authoring: GPT-6.1 Sol, effort ultra. No field lower bound.
"""
from __future__ import annotations
import argparse, hashlib, json, math, platform, signal, time
from pathlib import Path
import flint
from flint import arb, acb, ctx

class BudgetStop(RuntimeError): pass

def s(v): return v.str(40, more=True)
def check(cond, msg):
    if not cond: raise ArithmeticError(msg)

def evaluate(x, offset, bits, limit):
    ctx.prec=bits
    tic=time.monotonic()
    counter=[0]
    m_exact=math.isqrt(x//4)
    if 4*m_exact*m_exact<x: m_exact+=1
    rec={'x':x,'time':'1/10','first_omitted_mode':m_exact,
         'b_star':'1/4','a_star':4,'offset_over_x':offset,'bits':bits,
         'cutoff_U':'2','quadrature_abs_tol':'1e-12','quadrature_rel_tol':'1e-20',
         'eval_limit':200000,'case_callback_limit':200000,'depth_limit':30,'runtime_limit_seconds':limit,
         'target_normalized_total_error':'1e-8','status':'started','derivatives':[]}
    def alarm(signum, frame): raise BudgetStop('30 second per-case runtime budget')
    old=signal.signal(signal.SIGALRM,alarm)
    signal.setitimer(signal.ITIMER_REAL,limit)
    try:
        pi=arb.pi(); X=arb(x); T=arb(1)/10; U=arb(2)
        d=pi/8-4*X.log()/X-arb(offset)/X
        c=(4*d).cos(); m=rec['first_omitted_mode']
        norm=X**(arb(9)/4)*arb(offset).exp()
        check(d>0 and d<pi/8,'invalid frozen shift')
        b=4*c*pi*m*m-9
        ratio=(arb(m+1)/m)**4*(-c*pi*(2*m+1)).exp()
        check(b>0 and 8*c*pi*m*m>=T and ratio<1,'mode tail admissibility')
        S=(2*pi*pi*m**4+3*pi*m*m)*(-c*pi*m*m).exp()/(1-ratio)
        lams=[pi*n*n for n in range(1,m)]
        rec['d']=s(d);rec['cos4d']=s(c);rec['normalized_spectral_factor']=s(norm)
        rec['admissibility']={'b':s(b),'eight_q_minus_T':s(8*c*pi*m*m-T),'ratio':s(ratio)}
        mode=[]; source=[]; source_D=[]; source_concavity=[]
        p_phase=4*(4*d).sin()*pi*m*m-X-2*T*d
        rec['unconsumed_IBP_diagnostic']={'p':s(p_phase), 'status':'Note 11 nonstationary bound; original manuscript mode bound consumed by enclosure', 'tail_norm':[]}
        for j in range(3):
            mode.append((norm*S*sum((math.comb(j,k)*d**(j-k)*math.factorial(k)/b**(k+1) for k in range(j+1)),arb(0))).upper())
            Q=sum((math.comb(j,k)*d**(j-k)*math.factorial(k)/b**k for k in range(j+1)),arb(0))
            rec['unconsumed_IBP_diagnostic']['tail_norm'].append(s((2*norm*S*Q/p_phase).upper()) if p_phase>0 else None)
            src=arb(0)
            for lam in lams:
                D=4*c*lam*(4*U).exp()-9-2*T*U-arb(j)/(U+d)
                check(D>0 and 16*c*lam*(4*U).exp()>2*T,'source concavity/tangent failure')
                source_D.append(D.lower());source_concavity.append((16*c*lam*(4*U).exp()-2*T).lower())
                src+=(2*lam*lam+3*lam)*(U+d)**j*(T*U*U+9*U-c*lam*(4*U).exp()).exp()/D
            source.append((norm*src).upper())
            check(mode[-1]+source[-1]<arb('1e-10'),'tails exceed predeclared budget')
        rec['admissibility']['minimum_retained_source_D']=s(min(source_D));rec['admissibility']['minimum_retained_source_concavity_margin']=s(min(source_concavity))
        rec['mode_tail_norm']=[s(v) for v in mode];rec['retained_U_tail_norm']=[s(v) for v in source]
        rec['setup_seconds']=time.monotonic()-tic
        for j in range(3):
            jtic=time.monotonic(); cb=counter[0]
            def integrand(u, analytic):
                counter[0]+=1
                if counter[0]>200000: raise BudgetStop('global callback cap')
                v=u+acb(0,d); q=(4*v).exp()
                total=acb(0)
                for lam in lams:
                    total+=(2*lam*lam*q*q-3*lam*q)*(-lam*q).exp()
                return norm*(T*v*v+v+acb(0,X)*u).exp()*total*(acb(0,1)*v)**j
            integral=acb.integral(integrand,0,U,abs_tol=arb('1e-12'),rel_tol=arb('1e-20'),eval_limit=200000,depth_limit=30)
            check(integral.is_finite(),'nonfinite quadrature')
            quadrature=integral.real.rad().upper()
            error=(quadrature+mode[j]+source[j]).upper()
            full=arb(integral.real.mid(),error)
            item={'j':j,'integral_real_norm':s(integral.real),'integral_imag_norm':s(integral.imag),
                  'quadrature_radius_norm':s(quadrature),'mode_tail_norm':s(mode[j]),
                  'source_tail_norm':s(source[j]),'total_added_error_norm':s(error),
                  'full_H_derivative_norm_enclosure':s(full),'callbacks':counter[0]-cb,
                  'seconds':time.monotonic()-jtic,'passes_budget':bool(error<arb('1e-8'))}
            rec['derivatives'].append(item)
            check(item['passes_budget'],'quadrature exceeds predeclared budget')
        rec['status']='pass'
    except Exception as exc:
        rec['status']='bounded_failure'; rec['failure_type']=type(exc).__name__;rec['failure_message']=str(exc)
    finally:
        signal.setitimer(signal.ITIMER_REAL,0);signal.signal(signal.SIGALRM,old)
    rec['callbacks']=counter[0];rec['seconds']=time.monotonic()-tic
    return rec

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output',required=True);parser.add_argument('--repo',type=Path,required=True);parser.add_argument('--bits',type=int,default=160)
    parser.add_argument('--execution-model',required=True);parser.add_argument('--execution-effort',required=True)
    args=parser.parse_args()
    inv=args.repo/'papers/investigations-3/11_arithmetic_collision_rigidity'
    pins=['manuscript/positive_arithmetic_packets/sections/07_shifted_approximation.tex',
          'notes/02_updated_research_plan/07_SHIFTED_EVALUATOR_AND_COMPLETE_ERROR_BUDGET_20261018.md']
    report={'actual_model':args.execution_model,'actual_effort':args.execution_effort,
            'analytic_source_sha256':{p:hashlib.sha256((inv/p).read_bytes()).hexdigest() for p in pins},
            'date':'2026-10-18','prepared_for':'Edward Baker','llm_assistance':True,
            'purpose':'Source-specific normalized point jet evaluator, no nonvanishing or global claim',
            'flint_version':flint.__version__,'python':platform.python_version(),
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'predeclared_x':[1000,10000], 'predeclared_first_omitted_mode':'ceil(sqrt(x/4))',
            'normalization':'G0=x^(7/4)*exp(-pi*x/8); factor e^(-d*x)/G0=x^(9/4)*exp(offset)',
            'error_contract':'H^(j)/G0 lies within exact real midpoint plus quadrature radius + full omitted mode tail + retained-source U tail; derivatives freeze m,d,U',
            'source_contract':'Manuscript complete reflected source precedes square-mode truncation; real t,x allow exact conjugate pairing; no evenness assumed for truncated source',
            'records':[]}
    # Each complete case is bounded at 30 s. A failure at the initial height
    # stops the height progression; the separately frozen contour still replays.
    first=evaluate(1000,0,args.bits,30);report['records'].append(first)
    Path(args.output).write_text(json.dumps(report,indent=2)+'\n')
    second=evaluate(1000,1,args.bits,30);report['records'].append(second)
    if first['status']=='pass' and second['status']=='pass':
        overlaps=[]
        for aa,bb in zip(first['derivatives'],second['derivatives']):
            overlaps.append({'j':aa['j'],'overlap':bool(arb(aa['full_H_derivative_norm_enclosure']).overlaps(arb(bb['full_H_derivative_norm_enclosure'])))})
        report['frozen_contour_replay']=overlaps
        # Expensive is predeclared as >=20 s at the first height.
        if first['seconds']<20:
            report['records'].append(evaluate(10000,0,args.bits,30))
        else: report['x10000_status']='skipped: initial x1000 cost >=20 seconds'
    else: report['x10000_status']='skipped: initial/replay x1000 failed'
    Path(args.output).write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({'output':args.output,'records':[{'x':r['x'],'offset':r['offset_over_x'],'status':r['status'],'seconds':r['seconds'],'callbacks':r['callbacks'],'failure':r.get('failure_message')} for r in report['records']]}))
if __name__=='__main__': main()
