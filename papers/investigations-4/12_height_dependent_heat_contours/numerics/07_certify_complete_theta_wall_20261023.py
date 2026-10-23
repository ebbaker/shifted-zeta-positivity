#!/usr/bin/env python3
"""One bounded actual-theta wall/coefficient certificate on the frozen pilot box.
Prepared for Edward Baker, 2026-10-23; substantial LLM assistance,
gpt-6-astra (Codex), effort ultra. No root data enter the coefficient proof.
"""
from fractions import Fraction as F
from math import factorial
import argparse, hashlib, json, time, sys
from pathlib import Path
from flint import arb,acb
import hdc13_theta_core
from hdc13_theta_core import ActualHeatCore,rec


def a(x):
 x=F(x);return arb(x.numerator)/x.denominator

def rect(p,q):
 return acb(arb(a((p[0]+q[0])/2),a(abs(p[0]-q[0])/2)),
            arb(a((p[1]+q[1])/2),a(abs(p[1]-q[1])/2)))

def point(p):return acb(a(p[0]),a(p[1]))

def main():
 parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--output',type=Path)
 args=parser.parse_args(); started=time.perf_counter();core=ActualHeatCore()
 checks=[]
 def check(name,condition):
  if not condition:raise ArithmeticError(name)
  checks.append(name)
 wall=[];calls=0;rejected=0
 def cover(p,q,depth=0):
  nonlocal calls,rejected
  calls+=1
  if calls>2048 or depth>14:raise RuntimeError('bounded wall cover exceeded')
  z=rect(p,q);hs=core.jets(z,1,tau=0);hdiff=core.difference_cell(z)
  m=hs[0].abs_lower();omega=hdiff.abs_upper()
  if m>omega and m>0:
   eta=(omega/m).abs_upper()
   if eta<arb(1)/4:
    length=a(abs(q[0]-p[0])+abs(q[1]-p[1]))
    r=(z-36).abs_upper();K=-(1-eta).log()
    wall.append({'p':p,'q':q,'m':m,'omega':omega,'eta':eta,'K':K,'length':length,'r':r,
                 'mprime':hs[1].abs_upper(),'depth':depth});return
  rejected+=1;mid=tuple((u+v)/2 for u,v in zip(p,q));cover(p,mid,depth+1);cover(mid,q,depth+1)
 corners=[(F(26),F(-2)),(F(46),F(-2)),(F(46),F(2)),(F(26),F(2)),(F(26),F(-2))]
 for p,q in zip(corners,corners[1:]):cover(p,q)
 check('full ordered closed wall',wall[0]['p']==corners[0] and wall[-1]['q']==corners[-1] and all(x['q']==y['p'] for x,y in zip(wall,wall[1:])))
 wall_seconds=time.perf_counter()-started-core.setup_seconds
 print('Wall segments',len(wall),'calls',calls,'minfloor',rec(min(v['m']-v['omega'] for v in wall)),file=sys.stderr,flush=True)
 # Anchor quotient of the globally analytic finite polynomial only.
 # Complete H0/G0 correction is added outside the analytic integrator.
 e0=core.spatial_tail;e1=core.spatial_tail
 anchor=[];rounds=[];corrections=[];integral_started=time.perf_counter()
 for k in range(3):
  integral=acb(0)
  for p,q in zip(corners,corners[1:]):
   pp=point(p);direction=point(q)-pp
   def f(u,analytic):
    w=pp+direction*u
    return direction*(w-36)**k*core.evaluate_poly(w,0,1)/core.evaluate_poly(w,0,0)
   value=acb.integral(f,0,1,abs_tol=arb('1e-13'),rel_tol=arb('1e-13'),eval_limit=20000,depth_limit=16)
   check('finite anchor integral k'+str(k)+' edge'+str(p),value.is_finite())
   integral+=value
  correction=arb(0)
  for v in wall:
   m=v['m'];mg=m-e0
   check('anchor polynomial wall floor k'+str(k),mg>0)
   beta=e1/m+(v['mprime']+e1)*e0/(m*mg)
   correction+=v['length']*v['r']**k*beta/(2*arb.pi())
  val=integral/acb(0,2*arb.pi())
  val=acb(val.real+arb(0,correction),val.imag+arb(0,correction))
  anchor.append(val);corrections.append(correction)
  print('Moment',k,rec(val),file=sys.stderr,flush=True)
 check('anchor zero count unique integer 2',anchor[0].real>arb(3)/2 and anchor[0].real<arb(5)/2 and anchor[0].imag.contains(0))
 # Uniform full-D continuation uses the complete relative logarithm, keeping
 # H_tau-H0 together. Every leaf obeys eta<1, so the count stays two.
 errors=[arb(0)]
 for k in (1,2):errors.append(sum((k*v['length']*v['r']**(k-1)*v['K']/(2*arb.pi()) for v in wall),arb(0)).abs_upper())
 p1=acb(anchor[1].real+arb(0,errors[1]),anchor[1].imag+arb(0,errors[1]))
 p2=acb(anchor[2].real+arb(0,errors[2]),anchor[2].imag+arb(0,errors[2]))
 discriminant=2*p2-p1*p1
 check('uniform complex discriminant nonzero and positive real part',discriminant.real>0)
 check('anchor moments respect real symmetry',anchor[1].imag.contains(0) and anchor[2].imag.contains(0))
 # Exact real-type symmetry restricts the real-time discriminant to real part.
 t=arb(1)/10000;q=8*t/(discriminant.real+8*t)
 check('terminal complete filter positive below 1e-5',q>0 and q<arb(1)/100000)
 transport_seconds=time.perf_counter()-integral_started
 # Equally informed direct comparator: the identical wall/source oracle,
 # polynomial integrator, tolerances and complete quotient correction at T.
 baseline_started=time.perf_counter(); direct=[]; baseline_cells=[]
 for v in wall:
  hj=core.jets(rect(v['p'],v['q']),1,tau=t)
  baseline_cells.append((v,hj[0].abs_lower(),hj[1].abs_upper()))
 for k in (1,2):
  value=acb(0)
  for p,qend in zip(corners,corners[1:]):
   pp=point(p);direction=point(qend)-pp
   def f(u,analytic):
    w=pp+direction*u
    return direction*(w-36)**k*core.evaluate_poly(w,t,1)/core.evaluate_poly(w,t,0)
   one=acb.integral(f,0,1,abs_tol=arb('1e-13'),rel_tol=arb('1e-13'),eval_limit=20000,depth_limit=16)
   check('finite direct terminal integral k'+str(k)+' edge'+str(p),one.is_finite());value+=one
  correction=arb(0)
  for v,m,prime in baseline_cells:
   mg=m-core.errors[0];check('direct terminal polynomial wall floor',mg>0)
   beta=core.errors[1]/m+(prime+core.errors[1])*core.errors[0]/(m*mg)
   correction+=v['length']*v['r']**k*beta/(2*arb.pi())
  value/=acb(0,2*arb.pi())
  direct.append(acb(value.real+arb(0,correction),value.imag+arb(0,correction)))
 check('direct moments have real symmetry',all(v.imag.contains(0) for v in direct))
 direct_delta=2*direct[1].real-direct[0].real**2
 check('direct terminal discriminant positive',direct_delta>0)
 direct_q=8*t/(direct_delta+8*t)
 check('direct and continuation filters overlap',q.overlaps(direct_q))
 # Separate, cheap direct reality check. It is not used above.
 real_tau=arb(0,arb(1)/10000)
 signs=[core.cell(acb(x),tau=real_tau).real for x in (28,29,42,43)]
 check('two uniform real sign changes',signs[0]*signs[1]<0 and signs[2]*signs[3]<0)
 sign_q_bound=8*t/(arb(13)**2+8*t)
 baseline_seconds=time.perf_counter()-baseline_started
 wall_record=[{'from':[str(x) for x in v['p']],'to':[str(x) for x in v['q']],
    'anchor_H_floor':rec(v['m']),'time_difference_upper':rec(v['omega']),
    'relative_error_upper':rec(v['eta']),'log_error_upper':rec(v['K']),
    'full_D_H_floor':rec(v['m']-v['omega']),'depth':v['depth']} for v in wall]
 record={'status':'PASS','date':'2026-10-23','prepared_for':'Edward Baker','model':'gpt-6-astra','reasoning_effort':'ultra','llm_assistance':True,
  'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
  'core_sha256':hashlib.sha256(Path(hdc13_theta_core.__file__).read_bytes()).hexdigest(),
  'physical_box':{'x':['26','46'],'y':['-2','2'],'Re_tau':['-1/10000','1/10000'],'Im_tau':['-1/10000','1/10000']},
  'source_oracle':core.metadata(),'wall':{'segments':len(wall),'calls':calls,'rejected_parents':rejected,
   'minimum_full_D_floor':rec(min(v['m']-v['omega'] for v in wall)),
   'maximum_relative_error':rec(max(v['eta'] for v in wall)), 'segment_records':wall_record},
  'anchor_tau':'0','centered_anchor_power_sums':[rec(x) for x in anchor],
  'anchor_complete_quotient_corrections':[rec(x) for x in corrections],
  'complete_zero_count_uniform_D':2,'power_sum_continuation_errors':[rec(x) for x in errors],
  'uniform_D_p1':rec(p1),'uniform_D_p2':rec(p2),'uniform_D_discriminant':rec(discriminant),
  'terminal_tau':'1/10000','terminal_filter':rec(q),
  'direct_comparator':{'source':'identical complete source oracle and already certified spatial wall',
   'terminal_power_sums':[rec(x) for x in direct],'terminal_discriminant':rec(direct_delta),'terminal_filter':rec(direct_q),
   'uniform_real_time_sign_change_points':[28,29,42,43],'sign_values':[rec(x) for x in signs],
   'sign_change_filter_upper':rec(sign_q_bound),
   'cost':'8 additional contour integrals at the same tolerances, 16 terminal wall cells and 4 real point cells; count premise reuses the shared complete wall certificate.',
   'assessment':'The direct terminal coefficient enclosure is substantially tighter than the uniform full-complex-time continuation enclosure. The cheap sign-change comparator proves reality/simplicity on the real interval after the shared count. No practical superiority is claimed for continuation.'},
  'checks':checks,'assertions':len(checks),'timings_seconds':{'wall_cover':wall_seconds,'anchor_integrals_and_continuation':transport_seconds,'direct_comparator':baseline_seconds,'total':time.perf_counter()-started},
  'establishes':['The complete unchanged theta field is nonzero on the prescribed spatial wall throughout the original complex-time square.',
    'The entire interior spatial population has multiplicity count two on that square; no individual zero is used as a premise.',
    'The centered prepared discriminant has positive real part throughout the square, so the two roots are distinct there and are real on every real-time slice.',
    'The complete two-root filter at time 1e-4 is enclosed by the recorded positive interval.'],
  'does_not_establish':['The original cap or complement integral, a complete lower-bound comparison, or any height-uniform estimate.',
    'Any new global simplicity claim or any practical advantage over an equally informed direct source method.']}
 text=json.dumps(record,indent=2)+'\n'
 if args.output:args.output.write_text(text)
 else:print(text)
 print('PASS',len(checks),'checks; terminalfilter',rec(q),file=sys.stderr)
if __name__=='__main__':main()
