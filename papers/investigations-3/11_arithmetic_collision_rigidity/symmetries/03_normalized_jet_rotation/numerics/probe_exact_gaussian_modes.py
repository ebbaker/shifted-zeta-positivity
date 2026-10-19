#!/usr/bin/env python3
"""G3 exact finite gamma-Gaussian arithmetic jets: bounded point decomposition.

Prepared for Edward Baker, 19 October 2026, with substantial LLM assistance.
gpt-6.1-sol, actual effort ultra. Same-model internal arithmetic checks.
Point decompositions, not a uniform complete residual theorem.
"""
import argparse, hashlib, importlib.util, json, math, platform, sys
sys.dont_write_bytecode = True
from fractions import Fraction as F
from pathlib import Path
import flint
from flint import arb, acb, acb_series, ctx
INV=Path('papers/investigations-3/11_arithmetic_collision_rigidity')
LANE=INV/'symmetries/03_normalized_jet_rotation'
def A(v):return arb(v.numerator)/v.denominator if isinstance(v,F) else arb(v)
def out(v):return v.str(38,more=True)
def check(ok,msg):
 if not ok:raise ArithmeticError(msg)
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(p,name):
 s=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
def box(a,b):
 a,b=A(a),A(b);return arb((a+b)/2,((b-a)/2).upper())

def run(repo,setup,bits):
 hh=load(repo/INV/'numerics/high_height_consumer/high_height_consumer.py','g3_hh'+str(bits));hh.validate_setup(setup,repo)
 ev=hh.load_setup(setup);ctx.prec=bits;ctx.cap=8
 js=load(repo/INV/'symmetries/02_cutoff_reflection/numerics/evaluate_complete_frozen_jets.py','g3_jets'+str(bits))
 e=js.ClosedJetEvaluator(repo,bits);o=e.old;pi=arb.pi();ii=acb(0,1);lg=e.logGc
 rows=[]
 for xx,tt in [(1000,F(21,200)),(999,F(21,200)),(1001,F(21,200)),(1000,F(1,100)),(1000,F(1,5))]:
  ctx.prec=bits
  x,t=A(xx),A(tt);s=acb(A(F(1,2)),-x/2);rt=t.sqrt();V=A(10);calls=0
  # Uniform physical-x disk radius1 bound for the omitted Gaussian tails.
  # Im(s) stays below -499; the m0' Lipschitz/Stirling bounds hold for all
  # real Gaussian shifts, so the tails below are not point samples.
  sr=acb(box(0,1),box(-F(xx+1,2),-F(xx-1,2)))
  Tlo=A(F(xx-1,2));c=1-t/(4*(Tlo-3));total_tail=A(0)
  tail_rows=[]
  for n in range(1,9):
   ell=A(n).log();beta=(rt*(o.alpha(sr)-ell).real.abs_upper()).upper()
   check(c>0 and c*V-beta/2>0,'Gaussian tail admissibility')
   pref=((o.m0(sr)-sr*ell-lg).real+1/(6*(Tlo-A('.66')))).exp().upper()
   bound=(pref*(-c*V*V+beta*V).exp()/(pi.sqrt()*(c*V-beta/2))).upper()
   total_tail+=2*bound;tail_rows.append({'n':n,'physical_value_tail_over_Gstar_upper':out(2*bound)})
  total_tail=total_tail.upper()
  tails=[(math.factorial(j)*total_tail).upper() for j in range(3)]
  # Cauchy with physical-x radius1 pays differentiated infinite tails.
  values=[];quadrature=[]
  for j in range(3):
   def integrand(v,analytic):
    nonlocal calls
    calls+=1;sv=s+rt*v
    lm=sv.log()+(sv-1).log()-sv*pi.log()/2+(sv/2).lgamma()-A(16).log()-lg
    rho=1/sv+1/(sv-1)-pi.log()/2+(sv/2).digamma()/2
    rhop=-1/(sv*sv)-1/((sv-1)*(sv-1))+(sv/2).polygamma(1)/4
    result=acb(0)
    for n in range(1,9):
     ell=A(n).log();mode=(lm-sv*ell).exp()
     factor=[acb(1),-ii*(rho-ell)/2,-((rho-ell)**2+rhop)/4][j]
     result+=mode*factor
    return result*(-v*v).exp()/pi.sqrt()
   value=acb.integral(integrand,-V,V,abs_tol=A('1e-24'),rel_tol=A('1e-25'),eval_limit=100000,depth_limit=25)
   check(value.is_finite(),'finite gamma-Gaussian quadrature')
   quadrature.append((2*value.real.rad()).upper())
   values.append(2*value.real+arb(0,tails[j]))
  data=e.jets(x,t);w,wp,b,bp,C=[data[k] for k in ['omega','omega_x','b','b_x','chi']]
  def qjets(v):return [C*v[0],C*(v[1]-b*v[0]),C*(v[2]-2*b*v[1]+(b*b-bp)*v[0])]
  def R(v):return v[0]+v[2]/(w*w)-wp*v[1]/(w**3)
  source,_=ev.enclose(tt,tt,xx,xx)
  ctx.prec=bits  # The historical source evaluator restores its own 192-bit precision.
  z=acb_series([acb(x),acb(1)],3);N=o.normalizer(z,t);ss=(1-ii*z)/2
  G=sum((o.mode(z,t,n) for n in range(1,9)),acb_series([0]))/lg.exp()
  Gjet=[math.factorial(j)*G[j].real for j in range(3)]
  sourceQ=qjets(source);exactQ=qjets(values);GQ=qjets(Gjet)
  residual=[sourceQ[j]-data['full'][j] for j in range(3)]
  exact_delta=[exactQ[j]-GQ[j] for j in range(3)]
  exact_edge=[residual[j]-exact_delta[j] for j in range(3)]
  pred=acb_series([0]);n1=acb_series([0])
  for n in range(1,9):
   ell=A(n).log();pn=acb_series([0])
   for sv in (ss,1-ss):
    a=o.alpha(sv)-ell;g=(o.m0(sv)-sv*ell+t*a*a/4).exp()
    kappa=1/(6*sv)+o.alphap(sv)*(t/4+t*t*a*a/8)
    pn+=g*kappa
   pred+=pn/N
   if n==1:n1=pn/N
  pj=[math.factorial(j)*pred[j].real for j in range(3)]
  n1j=[math.factorial(j)*n1[j].real for j in range(3)]
  diff=[exact_delta[j]-pj[j] for j in range(3)]
  rows.append({'t':str(tt),'x':xx,'gaussian_cutoff':'10','callbacks':calls,
   'tail_derivation':'Bound on physical-x disk radius1; unshifted real Gaussian tails and Cauchy derivative factors1,1,2.',
   'physical_gaussian_tails_over_Gstar_upper':[out(v) for v in tails],
   'quadrature_radii_over_Gstar':[out(v) for v in quadrature],
   'complete_residual_Q_jets':[out(v) for v in residual],'complete_residual_R':out(R(residual)),
   'exact_finite_mode_delta_Q_jets':[out(v) for v in exact_delta],'exact_finite_mode_delta_R':out(R(exact_delta)),
   'first_arithmetic_correction_Q_jets':[out(v) for v in pj],'first_arithmetic_correction_R':out(R(pj)),
   'finite_mode_first_correction_error_Q_jets':[out(v) for v in diff],'finite_mode_first_correction_error_R':out(R(diff)),
   'exact_edge_discrepancy_Q_jets':[out(v) for v in exact_edge],'exact_edge_discrepancy_R':out(R(exact_edge)),
   'n1_first_correction_Q_jets':[out(v) for v in n1j],'n1_first_correction_R':out(R(n1j))})
 return {'bits':bits,'points':rows}
def main():
 p=argparse.ArgumentParser();p.add_argument('--repo',type=Path,required=True);p.add_argument('--setup',type=Path,required=True)
 p.add_argument('--output',type=Path,required=True);p.add_argument('--bits',type=int,nargs='+',default=[192,256])
 p.add_argument('--execution-model',required=True);p.add_argument('--execution-effort',required=True);a=p.parse_args()
 setup=json.loads(a.setup.read_text());pins=[INV/'numerics/high_height_consumer/high_height_consumer.py',
 INV/'symmetries/02_cutoff_reflection/numerics/evaluate_complete_frozen_jets.py',INV/'symmetries/02_cutoff_reflection/numerics/check_cutoff_reflection.py']
 data={'date':'2026-10-19','prepared_for':'Edward Baker','actual_model':a.execution_model,'actual_effort':a.execution_effort,
  'llm_assistance':'substantial; same-model research and separate internal review',
  'python':platform.python_version(),'python_flint':flint.__version__,'script_sha256':sha(__file__),
  'source_sha256':{str(v):sha(a.repo/v) for v in pins},'source_setup_sha256':sha(a.setup),
  'status':'Certified five-point finite gamma-Gaussian/complete-source decomposition; not a uniform full arithmetic remainder theorem.',
  'runs':[run(a.repo,setup,b) for b in a.bits]}
 a.output.write_text(json.dumps(data,indent=2)+'\n')
 print(json.dumps({'output':str(a.output),'center':[r['points'][0] for r in data['runs']]}))
if __name__=='__main__':main()
