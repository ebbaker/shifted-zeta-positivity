#!/usr/bin/env python3
"""S06-T2 same-ball twice-centered-current comparison.

19 October2026; prepared for Edward Baker with substantial LLM assistance.
Actual execution model/effort are CLI metadata. Internal verification only.
The finite source is unchanged; j3 has its own complete error payments.
"""
from __future__ import annotations
import argparse, hashlib, importlib.util, json, math, platform, time
from fractions import Fraction as F
from pathlib import Path
import flint
from flint import arb, acb, ctx

REL=Path('papers/investigations-3/11_arithmetic_collision_rigidity')
BASE=REL/'numerics/high_height_consumer/high_height_consumer.py'
CONTRACT='04_S06_T2_BOUNDED_CURRENT_COMPARISON_CONTRACT_20261019.md'
SCHEMA='s06-t2-bounded-completed-current-v1'
EXPECTED_CONTRACT_SHA256='9c2c36808de7167cb29c64b8ac8bba023ec126c6b17f97b5af656cdb1de5d73e'
EXPECTED_BASE_SHA256='e96feb2b4c3e84de3025713b486fb8cf99fdd810f61366b79a0da188eb12535f'

def digest(path): return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def load_base(repo):
 if digest(Path(repo)/BASE)!=EXPECTED_BASE_SHA256:raise ArithmeticError('base source hash mismatch')
 spec=importlib.util.spec_from_file_location('s06_t2_base',Path(repo)/BASE)
 mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);return mod

def exact(v):
 if not v.is_finite() or not v.is_exact():raise ArithmeticError('finite exact dyadic required')
 m,e=v.man_exp();return {'mantissa':str(m),'exponent':int(e)}
def unexact(v):
 r=arb((int(v['mantissa']),int(v['exponent'])))
 if not r.is_exact() or not r.is_finite():raise ArithmeticError('invalid dyadic')
 return r

def ball(v):return {'interval':v.str(35,more=True),'midpoint':exact(v.mid()),'radius':exact(v.rad())}
def unball(v):return arb(unexact(v['midpoint']),unexact(v['radius']))
def endpoint(v):return {'value':v.str(35,more=True),'dyadic':exact(v)}

def evaluator_class(base):
 class FourJetEvaluator(base.WholeCellEvaluator):
  def __init__(self,bits):
   ctx.prec=bits;self.bits=bits;self.tlo=F(1,100);self.thi=F(1,5);self.tc=F(21,200)
   self.xlo=F(999);self.xhi=F(1001);self.xc=F(1000);self.U=arb(2);self.m=12
   self.L=24;self.K=12;self.J=3;self.maxmid=51;self.maxrem=53
   self.pi=arb.pi();self.d=self.pi/8-4*base.A(self.xc).log()/base.A(self.xc)
   self.c=(4*self.d).cos();self.sin4d=(4*self.d).sin();self.norm=base.A(self.xc)**(arb(9)/4)
   self.lams=[self.pi*n*n for n in range(1,self.m)];self.callbacks=0
   self.jet_callbacks=[];self.jet_seconds=[];self.values=[];self.radii=[]
   self.fact=[math.factorial(j)for j in range(self.maxrem+1)];self.coeff_cache={};self.calls=0
   self.start=time.monotonic();self.diagnostic={}
   self.uniform_tails=self.tails(self.xlo,self.xhi,3)
   self.physical_tail_admissibility=dict(self.diagnostic)
   self.high_order_tails=self.tails(self.xlo,self.xhi,self.maxrem)
   self.high_order_tail_admissibility=dict(self.diagnostic)
   self.majorant=self.moment_bound()
   self.full_H_moment=(self.majorant+max(self.high_order_tails[0])+max(self.high_order_tails[1])).upper()
   dt=base.A((self.thi-self.tlo)/2)
   self.whole_box_taylor=(self.majorant*(arb(1)/self.fact[self.L+1]+arb(1).exp()*dt**(self.K+1)/self.fact[self.K+1])).upper()
   base.check(self.whole_box_taylor<arb('1e-9'),'predeclared Taylor subbudget failed')
   for j in range(self.maxmid+1):
    begin=time.monotonic();before=self.callbacks
    def integrand(u,analytic):
     self.tick();v=u+acb(0,self.d);q=(4*v).exp();total=acb(0)
     for lam in self.lams:total+=(2*lam*lam*q*q-3*lam*q)*(-lam*q).exp()
     return self.norm*(base.A(self.tc)*v*v+v+acb(0,base.A(self.xc))*u).exp()*total*(acb(0,1)*v)**j
    val=acb.integral(integrand,0,self.U,abs_tol=arb('1e-13'),rel_tol=arb('1e-30'),eval_limit=200000,depth_limit=30)
    base.check(val.is_finite(),'nonfinite midpoint jet '+str(j))
    self.values.append(val.real.mid());self.radii.append(val.real.rad().upper())
    self.jet_callbacks.append(self.callbacks-before);self.jet_seconds.append(time.monotonic()-begin)
   self.setup_seconds=time.monotonic()-self.start
  def enclose(self,t0,t1,x0,x1):
   t0,t1,x0,x1=map(F,(t0,t1,x0,x1))
   base.check(self.tlo<=t0<=t1<=self.thi and self.xlo<=x0<=x1<=self.xhi,'domain')
   self.calls+=1;dt=base.box(t0,t1)-base.A(self.tc);dx=base.box(x0,x1)-base.A(self.xc)
   R=base.A(max(abs(x0-self.xc),abs(x1-self.xc)));delta=base.A(max(abs(t0-self.tc),abs(t1-self.tc)))
   tw=[delta**k/self.fact[k]for k in range(self.K+1)];sw=[R**l/self.fact[l]for l in range(self.L+1)]
   rem=(self.majorant*(R**25/self.fact[25]+R.exp()*delta**13/self.fact[13])).upper()
   mode,source=self.uniform_tails;vals=[];budgets=[]
   for j in range(4):
    key=(t0,t1,j)
    if key not in self.coeff_cache:
     self.coeff_cache[key]=[base.poly([(-1)**k*self.values[j+l+2*k]/self.fact[k]for k in range(self.K+1)],dt)/self.fact[l]for l in range(self.L+1)]
    image=base.poly(self.coeff_cache[key],dx)
    quad=sum((sw[l]*tw[k]*self.radii[j+l+2*k]for l in range(self.L+1)for k in range(self.K+1)),arb(0)).upper()
    total=(quad+rem+mode[j]+source[j]).upper();base.check(total<arb('1e-8'),'component error exceeds limit')
    vals.append(image+arb(0,total));budgets.append({'quadrature':quad,'taylor':rem,'mode':mode[j],'source':source[j],'total':total,'polynomial_image':image})
   return vals,budgets
 return FourJetEvaluator

def measure(base,vals,t0,t1,x0,x1,budgets=None):
 base.check(len(vals)==4 and all(v.is_finite()for v in vals),'four finite complete jets required')
 t0,t1,x0,x1=map(F,(t0,t1,x0,x1))
 base.check(F(1,100)<=t0<=t1<=F(1,5)and F(999)<=x0<=x1<=F(1001),'measurement domain')
 if budgets is not None:
  base.check(len(budgets)==4,'four error ledgers required')
  for ledger in budgets:
   base.check(ledger['polynomial_image'].is_finite(),'nonfinite nominal polynomial image')
   base.check(all(ledger[k].is_finite()and ledger[k]>=0 for k in ('quadrature','taylor','mode','source','total')),'finite nonnegative component errors required')
 h0,h1,h2,h3=vals;t=base.box(t0,t1);x=base.box(x0,x1)
 beta=2*t*x/(165+4*t+base.square(x));a=-h2+beta*h3;b=h1-beta*h2
 # Factored residual keeps its exact signed derivative identity while paying dependence.
 r=h0*a+h1*b;den=(base.square(a)+base.square(b)).sqrt().upper()
 distances=[h0.abs_lower(),h1.abs_lower()];direct=(distances[0]**2+distances[1]**2).sqrt()
 positive=bool(r>0)
 if positive:base.check(den>0,'positive residual with zero denominator')
 C=arb(0)if not positive else r.lower()/den
 nogain=not positive or bool(C.upper()<direct.lower())
 approximation={}
 if budgets is not None:
  ms=[b['polynomial_image']for b in budgets];es=[b['total']for b in budgets]
  def B(i,j):return (ms[i].abs_upper()*es[j]+ms[j].abs_upper()*es[i]+es[i]*es[j]).upper()
  er=(B(1,1)+B(0,2)+beta.abs_upper()*(B(1,2)+B(0,3))).upper()
  nominal=ms[1]*ms[1]-ms[0]*ms[2]-beta*(ms[1]*ms[2]-ms[0]*ms[3])
  approximation={'residual_added_approximation_error_upper':endpoint(er),'nominal_residual':ball(nominal),
   'error_formula':'B11+B02+abs(beta)*(B12+B03); Bij=abs(mi)*ej+abs(mj)*ei+ei*ej'}
 return {'beta':ball(beta),'coefficient_a':ball(a),'coefficient_b':ball(b),'residual':ball(r),
  'residual_lower':endpoint(r.lower()),'denominator_upper':endpoint(den),
  'independently_signed':positive,'current_radius':ball(C),'direct_radius':ball(direct),
  'distances_to_zero':[endpoint(d)for d in distances],
  'strict_current_below_direct':nogain if positive else None,
  'no_gain':nogain,**approximation},C,direct

def contract_settings(bits):
 return {'domain':{'t':['1/100','1/5'],'x':['999','1001']},'midpoint':['21/200','1000'],
 'normalization':'fixed Gc=1000^(7/4)exp(-125*pi); never differentiated',
 'frozen':{'d':'pi/8-4*log(1000)/1000','U':2,'first_omitted_mode':12,'retained_modes':[1,11],
 'spatial_degree':24,'time_degree':12,'midpoint_orders':[0,51],'common_moment_order':53},
 'cell_cover':{'time_cuts':['1/100','23/400','21/200','61/400','1/5'],
 'x_cuts':[str(F(999)+F(k,8))for k in range(17)],'closed':True,'cells':64},
 'predeclared':{'bits':bits,'setup_seconds_limit':60,'setup_callback_limit':2000000,
 'per_integral_eval_limit':200000,'depth_limit':30,'midpoint_abs_tol_norm':'1e-13',
 'midpoint_rel_tol':'1e-30','maximum_added_component_error_norm':'1e-8',
 'whole_box_Taylor_subbudget_norm':'1e-9','consumer_calls':64,'refinement':False},
 'current':'r=L0-beta*L0_x=h0*(-h2+beta*h3)+h1*(h1-beta*h2); beta=2tx/(165+4t+x^2)',
 'primary_metric':'uniform physical sqrt(H^2+Hx^2)/fixed Gc',
 'comparator':'exact minimum first-jet norm over the same Cartesian h0,h1 projection'}

def setup_record(ev):
 return {'seconds':ev.setup_seconds,'callbacks':ev.callbacks,
 'jet_seconds':ev.jet_seconds,'jet_callbacks':ev.jet_callbacks,
 'common_moment':endpoint(ev.majorant),'whole_box_taylor':endpoint(ev.whole_box_taylor),
 'physical_tail_admissibility':ev.physical_tail_admissibility,
 'high_order_tail_admissibility':ev.high_order_tail_admissibility,
 'uniform_mode_tails':[endpoint(v)for v in ev.uniform_tails[0]],
 'uniform_source_tails':[endpoint(v)for v in ev.uniform_tails[1]],
 'all_order_mode_tails':[endpoint(v)for v in ev.high_order_tails[0]],
 'all_order_source_tails':[endpoint(v)for v in ev.high_order_tails[1]],
 'midpoint_jets':[{'j':j,'midpoint':exact(v),'quadrature_radius':exact(ev.radii[j])}for j,v in enumerate(ev.values)]}

def run(repo,bits,model,effort,contract):
 base=load_base(repo)
 base.check(bits in (192,256),'comparison precision must be192or256')
 base.check(isinstance(model,str)and model.strip()and isinstance(effort,str)and effort.strip(),'actual model and effort required')
 base.check(Path(contract).name==CONTRACT and digest(contract)==EXPECTED_CONTRACT_SHA256,'comparison contract mismatch')
 ctx.prec=bits;start=time.monotonic()
 record={'schema':SCHEMA,'date':'2026-10-19','timezone':'America/New_York','prepared_for':'Edward Baker',
 'actual_model':model,'actual_effort':effort,'llm_assistance':'substantial; internal verification; no specialist human review',
 'python':platform.python_version(),'python_flint':flint.__version__,'actual_precision_bits':bits,
 'producer_sha256':digest(__file__),'base_sha256':digest(Path(repo)/BASE),
 'contract_file':Path(contract).name,'contract_sha256':digest(contract),'source_pins':base.source_pins(repo),
 'settings':contract_settings(bits),'status':'started'}
 try:
  ev=base.bounded(lambda:evaluator_class(base)(bits),60);record['setup']=setup_record(ev)
  cells=[];currents=[];directs=[];maximum=arb(0);consumer_start=time.monotonic()
  times=[F(1,100)+F(19*k,400)for k in range(5)];xs=[F(999)+F(k,8)for k in range(17)]
  for ti in range(4):
   for xi in range(16):
    t0,t1=times[ti:ti+2];x0,x1=xs[xi:xi+2];vals,budgets=ev.enclose(t0,t1,x0,x1)
    metrics,C,D=measure(base,vals,t0,t1,x0,x1,budgets)
    cells.append({'index':[ti,xi],'t':[str(t0),str(t1)],'x':[str(x0),str(x1)],
     'jets':[ball(v)for v in vals],'budgets':[{k:ball(v)if k=='polynomial_image'else endpoint(v)for k,v in b.items()}for b in budgets],**metrics})
    currents.append(C);directs.append(D);maximum=max(maximum,max(b['total']for b in budgets))
  signed=sum(r['independently_signed']for r in cells)
  record.update(status='pass',cells=cells,consumer_seconds=time.monotonic()-consumer_start,
   summary={'cells':64,'coverage_verified':True,'independently_signed_cells':signed,'failed_current_cells':64-signed,
    'all_cells_no_current_radius_gain':all(r['no_gain']for r in cells),
    'strictly_smaller_current_radius_cells':sum(r['strict_current_below_direct']is True for r in cells),
    'minimum_current_radius':endpoint(min(C.lower()for C in currents)),
    'minimum_direct_radius':endpoint(min(D.lower()for D in directs)),
    'maximum_added_component_error_norm':endpoint(maximum),'consumer_calls':ev.calls,
    'midpoint_quadratures':52,'additional_h3_midpoint_quadratures_vs_old_setup':1,
    'decision':'stop this same-ball completed-current comparison; no gain'if all(r['no_gain']for r in cells)else'review unresolved comparison',
    'scope':'fixed B, fixed64closed cells, raw same-ball Cartesian first-jet norm; no global/exterior/sign/coverage/speed gain'})
 except Exception as exc:record.update(status='bounded_failure',failure_type=type(exc).__name__,failure_message=str(exc))
 record['total_seconds']=time.monotonic()-start;return record

def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--repo',type=Path,required=True)
 p.add_argument('--output',type=Path,required=True);p.add_argument('--contract',type=Path,required=True)
 p.add_argument('--bits',type=int,choices=[192,256],required=True);p.add_argument('--execution-model',required=True)
 p.add_argument('--execution-effort',required=True);a=p.parse_args()
 if not a.execution_model.strip()or not a.execution_effort.strip():p.error('actual model and effort required')
 if a.contract.name!=CONTRACT or not a.contract.is_file():p.error('predeclared contract missing or wrong filename')
 if digest(a.contract)!=EXPECTED_CONTRACT_SHA256:p.error('comparison contract hash mismatch')
 record=run(a.repo,a.bits,a.execution_model,a.execution_effort,a.contract)
 a.output.write_text(json.dumps(record,indent=2)+'\n')
 print(json.dumps({'output':str(a.output),'status':record['status'],'summary':record.get('summary'),
 'failure':record.get('failure_message'),'setup_callbacks':record.get('setup',{}).get('callbacks'),
 'setup_seconds':record.get('setup',{}).get('seconds'),'bytes':a.output.stat().st_size}))
 return 0 if record['status']=='pass'else 1
if __name__=='__main__':raise SystemExit(main())
