#!/usr/bin/env python3
"""Matched real-source replay of the bounded height-1000 signed consumer.
Prepared for Edward Baker, 18 October2026, with substantial LLM assistance.
Authoring modelgpt-6.1-sol, actualeffortultra. Internal same-model verification.
"""
from __future__ import annotations
import argparse,hashlib,json,math,platform,signal,time
from pathlib import Path
from fractions import Fraction as F
import flint
from flint import arb,acb,ctx
import high_height_consumer as base

class BudgetStop(RuntimeError):pass

def digest(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def integrate_real(bits, relative, limit, callback_limit):
 ctx.prec=bits;started=time.monotonic();counter=0
 pi=arb.pi();X=arb(1000);tc=arb(21)/200
 norm=(pi*X/8).exp()/X**(arb(7)/4);lams=[pi*n*n for n in range(1,12)]
 result={'bits':bits,'relative_tolerance':str(relative),'absolute_tolerance_norm':'1e-13','per_integral_eval_limit':200000,'depth_limit':30,'case_limit_seconds':limit,'callback_limit':callback_limit,'jets':[],'status':'started'}
 def alarm(s,f):raise BudgetStop('matched real setup time limit')
 old=signal.signal(signal.SIGALRM,alarm);signal.setitimer(signal.ITIMER_REAL,limit)
 try:
  for j in range(51):
   before=counter;tic=time.monotonic()
   def integrand(u,analytic):
    nonlocal counter
    counter+=1
    if counter>callback_limit:raise BudgetStop('matched real setup callback limit')
    q=(4*u).exp();total=acb(0)
    for lam in lams:total+=(2*lam*lam*q*q-3*lam*q)*(-lam*q).exp()
    phase=X*u;trig=(phase.cos,phase.sin,phase.cos,phase.sin)[j%4]()
    if j%4 in (1,2):trig=-trig
    return norm*(tc*u*u+u).exp()*total*u**j*trig
   value=acb.integral(integrand,0,2,abs_tol=arb('1e-13'),rel_tol=arb(relative),eval_limit=200000,depth_limit=30)
   base.check(value.is_finite() and value.imag.contains(0),'nonfinite/nonreal real midpoint integral')
   result['jets'].append({'j':j,'midpoint':base.s(value.real.mid()),'quadrature_radius':base.s(value.real.rad().upper()),'seconds':time.monotonic()-tic,'callbacks':counter-before})
  # This explicit gate rejects finite but useless enclosures. Relative goals
  # can permit large radii under severe oscillatory cancellation.
  result['largest_radius_norm']=base.s(max(arb(r['quadrature_radius']).upper()for r in result['jets']))
  result['radius_gate_passed']=all(arb(r['quadrature_radius'])<arb('1e-10')for r in result['jets'])
  result['status']='pass' if result['radius_gate_passed']else 'rejected_error_budget'
 except Exception as exc:
  result['status']='bounded_failure';result['failure']=str(exc)
 finally:
  signal.setitimer(signal.ITIMER_REAL,0);signal.signal(signal.SIGALRM,old)
 result['seconds']=time.monotonic()-started;result['callbacks']=counter
 return result

def real_tails(j,Y=0):
 pi=arb.pi();m=12;T=arb(1)/5;U=arb(2)
 norm=(pi*1000/8).exp()/arb(1000)**(arb(7)/4)
 B=4*pi*m*m-9-Y;r=(arb(m+1)/m)**4*(-pi*(2*m+1)).exp()
 base.check(B>0 and 8*pi*m*m>=T and r<1,'real omitted-mode contract')
 mode=norm*2*pi*pi*m**4*(-pi*m*m).exp()*math.factorial(j)/(B**(j+1)*(1-r))
 source=arb(0)
 for n in range(1,m):
  lam=pi*n*n;D=4*lam*(4*U).exp()-9-Y-2*T*U-arb(j)/U
  base.check(D>0 and 16*lam*(4*U).exp()>2*T,'real retained-source contract')
  source+=2*lam*lam*U**j*(T*U*U+(9+Y)*U-lam*(4*U).exp()).exp()/D
 return mode.upper(),(norm*source).upper()

def attach_real(setup,raw,bits):
 ev=base.load_setup(setup);ctx.prec=bits
 data=setup['setup']
 Hmoment=arb(data['full_H_common_moment_norm']).upper()
 low,high=real_tails(0),real_tails(52)
 ev.majorant=(Hmoment+low[0]+high[0]+high[1]).upper()
 tails=[real_tails(j)for j in range(3)]
 ev.uniform_tails=([t[0]for t in tails],[t[1]for t in tails])
 ev.values=[];ev.radii=[];ev.coeff_cache={};ev.calls=0
 for r in raw['jets']:
  v=arb(r['midpoint']);ev.values.append(v.mid());ev.radii.append((v.rad()+arb(r['quadrature_radius']).upper()).upper())
 return ev,Hmoment

def replay_cells(ev,certificate):
 rows=[]
 for r in certificate['repair_cells']:
  ta,tb=map(F,r['t']);xa,xb=map(F,r['x']);v,b=ev.enclose(ta,tb,xa,xb)
  E=base.square(v[0])+base.square(v[1]);excess=base.square(v[1])-v[0]*v[2]-E/100
  base.check(excess>0,'real-source signed replay failed')
  overlap=[v[j].overlaps(arb(r['jet'][j]))for j in range(3)]
  base.check(all(overlap),'real/shifted cell enclosures disjoint')
  rows.append({'t':r['t'],'x':r['x'],'jet':[base.s(x)for x in v],'excess_norm2':base.s(excess),'energy_norm2':base.s(E),'budgets':[{k:base.s(z)for k,z in q.items()}for q in b],'overlaps_shifted':overlap})
 return rows

def replay_wall(ev,certificate):
    started=time.monotonic();wall=base.prepare_wall(ev)
    T=arb(1)/5;Y=1;m=12;d=ev.d;c=ev.c;pi=ev.pi;U=ev.U;J=52
    B=4*c*pi*m*m-9-Y;P=4*ev.sin4d*pi*m*m-1000-2*T*d
    r=(arb(m+1)/m)**4*(-c*pi*(2*m+1)).exp()
    base.check(B>0 and P>0 and r<1 and 8*c*pi*m*m>=T,'high-order complete wall tail')
    S=(2*pi*pi*m**4+3*pi*m*m)*(-c*pi*m*m).exp()/(1-r)
    mode=[]
    for j in (0,J):
        Q=sum((math.comb(j,k)*d**(j-k)*math.factorial(k)/B**k for k in range(j+1)),arb(0))
        mode.append(ev.norm*2*S*Q/P)
    source=arb(0)
    for lam in ev.lams:
        D=4*c*lam*(4*U).exp()-9-Y-2*T*U-arb(J)/(U+d)
        base.check(D>0 and 16*c*lam*(4*U).exp()>2*T,'high-order complete wall source tail')
        source+=(2*lam*lam+3*lam)*(U+d)**J*(T*U*U+(9+Y)*U-c*lam*(4*U).exp()).exp()/D
    complete=(wall['M']+mode[0]+mode[1]+ev.norm*source).upper()
    r0,rJ=real_tails(0,1),real_tails(J,1)
    wall['M']=(complete+r0[0]+rJ[0]+rJ[1]).upper()
    low=[real_tails(j,1)for j in range(3)]
    wall['mode']=[r[0]for r in low];wall['source']=[r[1]for r in low]
    rows=[]
    for record in certificate['cells']:
        ta,tb=map(F,record['t']);ya,yb=map(F,record['y'])
        values,budgets=base.wall_enclose(ev,ta,tb,ya,yb,wall)
        margin=max(values[0].real.abs_lower(),values[0].imag.abs_lower())
        base.check(margin>arb('1e-3'),'real midpoint wall replay lost strict coordinate margin')
        overlap=[values[j].real.overlaps(arb(record['jet'][j]['real'])) and values[j].imag.overlaps(arb(record['jet'][j]['imag'])) for j in range(3)]
        base.check(all(overlap),'real and shifted wall jets disjoint')
        rows.append({'t':record['t'],'y':record['y'],'margin_norm':base.s(margin),'overlaps_shifted':overlap,'added_errors_norm':[base.s(b['total'])for b in budgets]})
    return {'cells':rows,'minimum_margin_norm':base.s(min(arb(r['margin_norm']).lower()for r in rows)),
            'complete_H_common_majorant_norm':base.s(complete),'real_cutoff_common_majorant_norm':base.s(wall['M']),
            'seconds':time.monotonic()-started,'status':'pass'}

def main():
 p=argparse.ArgumentParser();p.add_argument('--repo',type=Path,required=True);p.add_argument('--setup',type=Path,required=True);p.add_argument('--signed',type=Path,required=True);p.add_argument('--output',type=Path,required=True);p.add_argument('--wall',type=Path,required=True);p.add_argument('--execution-model',required=True);p.add_argument('--execution-effort',required=True);p.add_argument('--bits',type=int,default=768);a=p.parse_args()
 setup=json.loads(a.setup.read_text());certificate=json.loads(a.signed.read_text())
 base.validate_setup(setup,a.repo)
 base.check(certificate['source_sha256']==digest(base.__file__),'signed evaluator source mismatch')
 started=time.monotonic();first=integrate_real(a.bits,'1e-30',60,2000000);attempts=[first]
 if first['status']!='pass':
  # One predeclared tolerance repair, with all failed work charged.
  remaining=60-first['seconds'];remaining_callbacks=2000000-first['callbacks']
  base.check(remaining>0 and remaining_callbacks>0,'real setup budget exhausted')
  attempts.append(integrate_real(a.bits,'0',remaining,remaining_callbacks))
 raw=attempts[-1];base.check(raw['status']=='pass','real comparator failed after one tolerance repair')
 ev,Hmoment=attach_real(setup,raw,a.bits);rows=replay_cells(ev,certificate)
 shared_overhead=max(0,setup['setup']['seconds']-sum(setup['setup']['jet_seconds']))
 total=time.monotonic()-started+shared_overhead
 shifted_cost=certificate['total_seconds_including_setup']
 wall_certificate=json.loads(a.wall.read_text());base.check(wall_certificate['source_sha256']==digest(base.__file__),'wall evaluator source mismatch');wall_result=replay_wall(ev,wall_certificate)
 report={'date':'2026-10-18','timezone':'America/New_York','prepared_for':'Edward Baker','actual_model':a.execution_model,'actual_effort':a.execution_effort,'llm_assistance':'substantial; same-model internal matched comparison','python':platform.python_version(),'python_flint':flint.__version__,'script_sha256':digest(__file__),'evaluator_sha256':digest(base.__file__),'input_sha256':{'setup':digest(a.setup),'signed':digest(a.signed),'wall':digest(a.wall)},'declaration':{'bits':a.bits,'same_domain':True,'same_source_modes_and_cutoff':True,'same_signed_target':True,'same_accuracy_requirement_norm':'1e-8','same_polynomial_degrees':[24,12],'maximum_setup_seconds_inclusive_failed_attempt':60,'maximum_setup_callbacks_inclusive_failed_attempt':2000000,'one_repair':'relative tolerance1e-30 replaced by0; all failed costs charged','propagation':'Both evaluators may consume the same complete-H contour derivative majorant; real cutoff tails pay transfer to its finite integral'},'attempts':attempts,'common_H_moment_norm':base.s(Hmoment),'real_finite_integral_moment_norm':base.s(ev.majorant),'shared_precomputation_charge_seconds':shared_overhead,'cells':rows,'wall_replay':wall_result,'minimum_excess_norm2':base.s(min(arb(r['excess_norm2']).lower()for r in rows)),'maximum_added_error_norm':base.s(max(arb(q['total']).upper()for r in rows for q in r['budgets'])),'total_real_seconds':total,'shifted_total_seconds':shifted_cost,'real_over_shifted_cost_ratio':total/shifted_cost,'factor_two_shifted_gain_gate':bool(total>=2*shifted_cost),'status':'pass'}
 a.output.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({k:report[k]for k in ['status','total_real_seconds','shifted_total_seconds','real_over_shifted_cost_ratio','factor_two_shifted_gain_gate']}))
if __name__=='__main__':main()
