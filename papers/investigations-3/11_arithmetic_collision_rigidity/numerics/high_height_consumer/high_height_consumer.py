#!/usr/bin/env python3
"""Reproducible bounded height-1000 signed and complex-wall consumers.

Prepared for Edward Baker,18October2026,with substantial LLM assistance.
The actual execution model and effort are required CLI metadata. Internal
verification only; no global Newman-constant or RH conclusion is asserted.

Fresh execution:
  python high_height_consumer.py --repo /path/to/shifted-zeta-positivity \
    --output-dir /path/to/records --execution-model MODEL \
    --execution-effort EFFORT [--bits160]

Importable API: WholeCellEvaluator, load_setup, run_signed_consumer,
prepare_wall, wall_enclose, run_wall_consumer, s, square, check.

The complete reflected contour identity precedes finite square-mode
truncation. Physical derivatives freeze d,m,U and the fixed G0(1000).
The Note11 nonstationary mode tail is consumed at physical orders0..2.
"""
from __future__ import annotations
import argparse,hashlib,json,math,platform,signal,time
from fractions import Fraction as F
from pathlib import Path
from flint import arb,acb,ctx
import flint

class BudgetStop(RuntimeError):pass

def A(v):return arb(v.numerator)/v.denominator if isinstance(v,F) else arb(v)
def s(v):return v.str(35,more=True)
def check(c,msg):
 if not c:raise ArithmeticError(msg)
def box(a,b):
 a,b=F(a),F(b)
 return arb(A((a+b)/2),A((b-a)/2))
def square(v):
 lo=(v.abs_lower()*v.abs_lower()).lower();hi=(v.abs_upper()*v.abs_upper()).upper()
 return arb((lo+hi)/2,((hi-lo)/2).upper())
def poly(cs,x):
 r=cs[-1]
 for c in reversed(cs[:-1]):r=r*x+c
 return r

class WholeCellEvaluator:
 def __init__(self,bits=160):
  ctx.prec=bits;self.bits=bits;self.tlo=F(1,100);self.thi=F(1,5);self.tc=F(21,200)
  self.xlo=F(999);self.xhi=F(1001);self.xc=F(1000);self.U=arb(2);self.m=12
  self.L=24;self.K=12;self.J=2;self.maxmid=50;self.maxrem=52
  self.pi=arb.pi();self.d=self.pi/8-4*A(self.xc).log()/A(self.xc);self.c=(4*self.d).cos();self.sin4d=(4*self.d).sin()
  self.norm=A(self.xc)**(arb(9)/4);self.lams=[self.pi*n*n for n in range(1,self.m)]
  self.callbacks=0;self.jet_callbacks=[];self.jet_seconds=[];self.values=[];self.radii=[]
  self.fact=[math.factorial(j) for j in range(self.maxrem+1)];self.coeff_cache={};self.calls=0
  self.start=time.monotonic();self.diagnostic={}
  self.uniform_tails=self.tails(self.xlo,self.xhi)
  self.high_order_tails=self.tails(self.xlo,self.xhi,self.maxrem)
  self.full_H_moment=None
  self.majorant=self.moment_bound()
  R=arb(1);dt=A((self.thi-self.tlo)/2)
  self.full_H_moment=(self.majorant+max(self.high_order_tails[0])+max(self.high_order_tails[1])).upper()
  self.whole_box_taylor=(self.majorant*(R**(self.L+1)/self.fact[self.L+1]+R.exp()*dt**(self.K+1)/self.fact[self.K+1])).upper()
  check(self.whole_box_taylor<arb('1e-9'),'predeclared Taylor subbudget failed')
  for j in range(self.maxmid+1):
   begin=time.monotonic();before=self.callbacks
   def integrand(u,analytic):
    self.tick();v=u+acb(0,self.d);q=(4*v).exp();total=acb(0)
    for lam in self.lams:total+=(2*lam*lam*q*q-3*lam*q)*(-lam*q).exp()
    return self.norm*(A(self.tc)*v*v+v+acb(0,A(self.xc))*u).exp()*total*(acb(0,1)*v)**j
   val=acb.integral(integrand,0,self.U,abs_tol=arb('1e-13'),rel_tol=arb('1e-30'),eval_limit=200000,depth_limit=30)
   check(val.is_finite(),'nonfinite midpoint jet '+str(j))
   self.values.append(val.real.mid());self.radii.append(val.real.rad().upper())
   self.jet_callbacks.append(self.callbacks-before);self.jet_seconds.append(time.monotonic()-begin)
  self.setup_seconds=time.monotonic()-self.start
 def tick(self):
  self.callbacks+=1
  if self.callbacks>2000000:raise BudgetStop('2 million total setup callbacks')
  if time.monotonic()-self.start>60:raise BudgetStop('60 second setup deadline')
 def moment_bound(self):
  T=A(self.thi);J=self.maxrem
  def integrand(u,analytic):
   self.tick();total=acb(0)
   for lam in self.lams:total+=(2*lam*lam+3*lam)*(T*u*u+9*u-self.c*lam*(4*u).exp()).exp()
   return total*(1+(u+self.d)**J)
  v=acb.integral(integrand,0,self.U,abs_tol=arb('1e-22'),rel_tol=arb('1e-25'),eval_limit=200000,depth_limit=30)
  check(v.is_finite() and v.imag.contains(0),'moment majorant quadrature failed')
  normleft=self.norm*(self.d*(A(self.xc)-A(self.xlo))).exp()
  return (normleft*v.real).upper()
 def tails(self,xleft,xright,maximum_order=2):
  T=A(self.thi);m=self.m;d=self.d;c=self.c;pi=self.pi;U=self.U
  B=4*c*pi*m*m-9;P=4*self.sin4d*pi*m*m-A(xright)-2*T*d
  ratio=(arb(m+1)/m)**4*(-c*pi*(2*m+1)).exp()
  check(d>0 and d<pi/8 and B>0 and P>0 and 8*c*pi*m*m>=T and ratio<1,'nonstationary mode admissibility')
  S=(2*pi*pi*m**4+3*pi*m*m)*(-c*pi*m*m).exp()/(1-ratio)
  normleft=self.norm*(d*(A(self.xc)-A(xleft))).exp();mode=[];source=[]
  sourceD=[];sourceC=[]
  for j in range(maximum_order+1):
   Q=sum((math.comb(j,k)*d**(j-k)*math.factorial(k)/B**k for k in range(j+1)),arb(0))
   mode.append((normleft*2*S*Q/P).upper());src=arb(0)
   for lam in self.lams:
    D=4*c*lam*(4*U).exp()-9-2*T*U-arb(j)/(U+d);C=16*c*lam*(4*U).exp()-2*T
    check(D>0 and C>0,'retained-source tangent admissibility')
    sourceD.append(D.lower());sourceC.append(C.lower())
    src+=(2*lam*lam+3*lam)*(U+d)**j*(T*U*U+9*U-c*lam*(4*U).exp()).exp()/D
   source.append((normleft*src).upper())
  self.diagnostic={'B':s(B),'P':s(P),'ratio':s(ratio),'eight_q_minus_T':s(8*c*pi*m*m-T),
  'minimum_source_D':s(min(sourceD)),'minimum_source_concavity':s(min(sourceC))}
  return mode,source
 def enclose(self,t0,t1,x0,x1):
  t0,t1,x0,x1=map(F,(t0,t1,x0,x1));check(self.tlo<=t0<=t1<=self.thi and self.xlo<=x0<=x1<=self.xhi,'domain')
  self.calls+=1;dt=box(t0,t1)-A(self.tc);dx=box(x0,x1)-A(self.xc)
  R=A(max(abs(x0-self.xc),abs(x1-self.xc)));delta=A(max(abs(t0-self.tc),abs(t1-self.tc)))
  tw=[delta**k/self.fact[k] for k in range(self.K+1)];sw=[R**l/self.fact[l] for l in range(self.L+1)]
  remainder=(self.majorant*(R**(self.L+1)/self.fact[self.L+1]+R.exp()*delta**(self.K+1)/self.fact[self.K+1])).upper()
  # Keep the already-checked uniform physical tail on all consumer cells.
  mode,source=self.uniform_tails;vals=[];budgets=[]
  for j in range(3):
   key=(t0,t1,j)
   if key not in self.coeff_cache:
    self.coeff_cache[key]=[poly([(-1)**k*self.values[j+l+2*k]/self.fact[k] for k in range(self.K+1)],dt)/self.fact[l] for l in range(self.L+1)]
   image=poly(self.coeff_cache[key],dx)
   quad=sum((sw[l]*tw[k]*self.radii[j+l+2*k] for l in range(self.L+1) for k in range(self.K+1)),arb(0)).upper()
   total=(quad+remainder+mode[j]+source[j]).upper()
   check(total<arb('1e-8'),'consumer added error exceeds target')
   vals.append(image+arb(0,total));budgets.append({'quadrature':quad,'taylor':remainder,'mode':mode[j],'source':source[j],'total':total})
  return vals,budgets

SCHEMA='acr-high-height-consumer-v1'
INVESTIGATION=Path('papers/investigations-3/11_arithmetic_collision_rigidity')
NOTE11=INVESTIGATION/'notes/02_updated_research_plan/11_EFFECTIVE_NONSTATIONARY_ARITHMETIC_TAIL_20261018.md'
MANUSCRIPT=INVESTIGATION/'manuscript/positive_arithmetic_packets'

def digest(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def dyadic(value):
 check(value.is_finite() and value.is_exact(),'exact finite dyadic required')
 man,exp=value.man_exp();return {'mantissa':str(man),'exponent':int(exp)}
def undyadic(data):
 value=arb((int(data['mantissa']),int(data['exponent'])))
 check(value.is_finite() and value.is_exact(),'dyadic cache did not load exactly')
 return value

def source_pins(repo):
 repo=Path(repo).resolve();note=repo/NOTE11;main=repo/MANUSCRIPT/'main.tex'
 check(note.is_file() and main.is_file(),'repository source pins missing')
 files=sorted((repo/MANUSCRIPT).rglob('*.tex'))
 entries=[{'path':str(path.relative_to(repo)),'sha256':digest(path)}for path in files]
 aggregate=hashlib.sha256(json.dumps(entries,sort_keys=True,separators=(',',':')).encode()).hexdigest()
 return {'note11':{'path':str(NOTE11),'sha256':digest(note)},'manuscript_main':{'path':str(MANUSCRIPT/'main.tex'),'sha256':digest(main)},
 'manuscript_tex_manifest':entries,'manuscript_tex_manifest_sha256':aggregate}

def provenance(repo,model,effort,bits):
 return {'schema':SCHEMA,'date':'2026-10-18','timezone':'America/New_York','prepared_for':'Edward Baker',
 'actual_model':model,'actual_effort':effort,'llm_assistance':'substantial; internal verification',
 'python':platform.python_version(),'python_flint':flint.__version__,'actual_precision_bits':bits,
 'source_sha256':digest(__file__),'source_pins':source_pins(repo)}

def setup_record(ev,meta):
 jets=[{'j':j,'midpoint':s(v),'midpoint_dyadic':dyadic(v),'quadrature_radius':s(ev.radii[j]),
 'quadrature_radius_dyadic':dyadic(ev.radii[j]),'seconds':ev.jet_seconds[j],'callbacks':ev.jet_callbacks[j]}for j,v in enumerate(ev.values)]
 setup={'seconds':ev.setup_seconds,'callbacks':ev.callbacks,'jet_seconds':ev.jet_seconds,'jet_callbacks':ev.jet_callbacks,
 'common_moment_norm':s(ev.majorant),'common_moment_dyadic':dyadic(ev.majorant),
 'full_H_common_moment_norm':s(ev.full_H_moment),'full_H_common_moment_dyadic':dyadic(ev.full_H_moment),
 'all_order_mode_tail_max':s(max(ev.high_order_tails[0])),'all_order_source_tail_max':s(max(ev.high_order_tails[1])),
 'all_order_mode_tail_dyadics':[dyadic(v)for v in ev.high_order_tails[0]],
 'all_order_source_tail_dyadics':[dyadic(v)for v in ev.high_order_tails[1]],
 'whole_box_Taylor_norm':s(ev.whole_box_taylor),
 'uniform_mode_tail_norm':[s(v)for v in ev.uniform_tails[0]],'uniform_source_tail_norm':[s(v)for v in ev.uniform_tails[1]],
 'uniform_mode_tail_dyadics':[dyadic(v)for v in ev.uniform_tails[0]],
 'uniform_source_tail_dyadics':[dyadic(v)for v in ev.uniform_tails[1]],'admissibility':ev.diagnostic,'midpoint_jets':jets}
 return dict(meta,kind='shifted_setup',status='pass',bits=ev.bits,
 normalization='fixed G0(1000)=1000^(7/4)*exp(-125*pi); never differentiated',
 domain={'t':['1/100','1/5'],'x':[999,1001]},
 frozen_parameters={'midpoint':['21/200','1000'],'d':'pi/8-4*log(1000)/1000','first_omitted_mode':12,'retained_modes':[1,11],'U':2,'bits':ev.bits},
 predeclared={'spatial_degree':24,'time_degree':12,'midpoint_orders':[0,50],'common_moment_order':52,
 'setup_seconds_limit':60,'setup_callback_limit':2000000,'per_integral_eval_limit':200000,'depth_limit':30,
 'midpoint_abs_tol_norm':'1e-13','midpoint_rel_tol':'1e-30','maximum_added_component_error_norm':'1e-8',
 'whole_box_Taylor_subbudget_norm':'1e-9','consumer_calls_limit':512},
 source_contract='Complete reflected contour precedes truncation; retained paired finite-cutoff integral solves the heat equation; no reflection or evenness assumed for truncated source.',
 cache_contract='Every midpoint and outward upper radius is serialized as its exact binary mantissa/exponent. Decimal strings are readable redundant enclosures.',setup=setup)

def validate_setup(data,repo=None):
 check(data.get('schema')==SCHEMA and data.get('kind')=='shifted_setup' and data.get('status')=='pass','invalid setup schema or status')
 check(data.get('source_sha256')==digest(__file__),'setup code hash mismatch')
 bits=data.get('actual_precision_bits')
 check(isinstance(bits,int) and bits>=128 and data.get('bits')==bits,'setup precision mismatch')
 check(data.get('domain')=={'t':['1/100','1/5'],'x':[999,1001]},'setup domain mismatch')
 expected={'midpoint':['21/200','1000'],'d':'pi/8-4*log(1000)/1000','first_omitted_mode':12,'retained_modes':[1,11],'U':2,'bits':bits}
 check(data.get('frozen_parameters')==expected,'setup frozen parameters mismatch')
 declared=data.get('predeclared',{})
 for key,value in [('spatial_degree',24),('time_degree',12),('midpoint_orders',[0,50]),('common_moment_order',52)]:
  check(declared.get(key)==value,'setup Taylor contract mismatch')
 if repo is not None:check(data.get('source_pins')==source_pins(repo),'setup analytic source mismatch')


def load_setup(data):
 """Restore cached finite-integral midpoint dyadics and rigorous bounds.

 No integration is performed. Exact dyadics prevent decimal cache drift.
 The fallback supports the earlier bounded pilot records conservatively.
 """
 validate_setup(data)
 bits=int(data.get('actual_precision_bits',data.get('bits',data.get('frozen_parameters',{}).get('bits',160))))
 ctx.prec=bits;record=data['setup'];ev=WholeCellEvaluator.__new__(WholeCellEvaluator)
 ev.bits=bits;ev.tlo=F(1,100);ev.thi=F(1,5);ev.tc=F(21,200);ev.xlo=F(999);ev.xhi=F(1001);ev.xc=F(1000)
 ev.U=arb(2);ev.m=12;ev.L=24;ev.K=12;ev.J=2;ev.maxmid=50;ev.maxrem=52
 ev.pi=arb.pi();ev.d=ev.pi/8-4*arb(1000).log()/1000;ev.c=(4*ev.d).cos();ev.sin4d=(4*ev.d).sin()
 ev.norm=arb(1000)**(arb(9)/4);ev.lams=[ev.pi*n*n for n in range(1,12)]
 ev.fact=[math.factorial(j)for j in range(53)];ev.coeff_cache={};ev.calls=0;ev.start=time.monotonic()
 ev.values=[];ev.radii=[];ev.jet_seconds=record['jet_seconds'];ev.jet_callbacks=record.get('jet_callbacks',[])
 for j,row in enumerate(record['midpoint_jets']):
  check(row['j']==j,'misordered midpoint cache')
  if 'midpoint_dyadic'in row:
   value=undyadic(row['midpoint_dyadic']);radius=undyadic(row['quadrature_radius_dyadic'])
  else:
   text=arb(row['midpoint']);value=text.mid();radius=(text.rad()+arb(row['quadrature_radius']).upper()).upper()
  check(radius.is_finite() and radius>=0,'nonfinite or negative quadrature radius');ev.values.append(value);ev.radii.append(radius)
 check(len(ev.values)==51,'incomplete midpoint cache')
 ev.majorant=undyadic(record['common_moment_dyadic'])if 'common_moment_dyadic'in record else arb(record['common_moment_norm']).upper()
 ev.full_H_moment=undyadic(record['full_H_common_moment_dyadic'])if 'full_H_common_moment_dyadic'in record else arb(record['full_H_common_moment_norm']).upper()
 if 'uniform_mode_tail_dyadics'in record:
  ev.uniform_tails=([undyadic(v)for v in record['uniform_mode_tail_dyadics']],[undyadic(v)for v in record['uniform_source_tail_dyadics']])
 else:ev.uniform_tails=ev.tails(ev.xlo,ev.xhi)
 if 'all_order_mode_tail_dyadics'in record:
  ev.high_order_tails=([undyadic(v)for v in record['all_order_mode_tail_dyadics']],[undyadic(v)for v in record['all_order_source_tail_dyadics']])
 else:ev.high_order_tails=ev.tails(ev.xlo,ev.xhi,52)
 check(ev.majorant.is_finite() and ev.majorant>0 and ev.full_H_moment.is_finite() and ev.full_H_moment>=ev.majorant,'invalid cached derivative majorant')
 ev.callbacks=int(record['callbacks']);ev.setup_seconds=record['seconds'];ev.diagnostic=record['admissibility']
 delta=A(F(19,200));ev.whole_box_taylor=(ev.majorant*(arb(1)/ev.fact[25]+arb(1).exp()*delta**13/ev.fact[13])).upper()
 return ev

def signed_cell(ev,t0,t1,x0,x1,depth):
 values,budgets=ev.enclose(t0,t1,x0,x1)
 E=square(values[0])+square(values[1]);L0=square(values[1])-values[0]*values[2];excess=L0-E/100
 return excess,{'t':[str(t0),str(t1)],'x':[str(x0),str(x1)],'depth':depth,'jet':[s(v)for v in values],
 'energy_norm2':s(E),'L0_norm2':s(L0),'excess_norm2':s(excess),
 'budgets':[{k:s(v)for k,v in b.items()}for b in budgets]}

def run_signed_consumer(ev):
 """Whole-time attempt, then the single predeclared four-slab repair."""
 started=time.monotonic();ev.calls=0;ev.coeff_cache={}
 report={'kind':'signed_consumer','status':'started','domain':{'t':['1/100','1/5'],'x':[999,1001]},
 'normalization':'fixed G0(1000); L0 and E divided by fixedG0^2',
 'predeclared':{'target':'Hx^2-H*Hxx>(H^2+Hx^2)/100','component_added_error_norm':'1e-8',
 'maximum_total_consumer_calls':512,'maximum_spatial_depth':9,
 'initial_attempt':'whole-time closed spatial strips','one_geometry_repair':'four equal closed time slabs with adaptive closed spatial strips; no new quadrature'},
 'initial_attempt_cells':[],'repair_cells':[],'repair_choices':[]}
 initial_started=time.monotonic();pending=[(F(999),F(1001),0)];initial_failure=None
 try:
  while pending:
   check(ev.calls<512,'signed consumer call budget')
   x0,x1,depth=pending.pop();excess,row=signed_cell(ev,ev.tlo,ev.thi,x0,x1,depth)
   if excess>0:row['status']='accepted'
   elif depth>=9:row['status']='depth_failure';initial_failure='maximum dyadic strip depth9'
   else:
    row['status']='split';mid=(x0+x1)/2;pending.extend([(mid,x1,depth+1),(x0,mid,depth+1)])
   report['initial_attempt_cells'].append(row)
   if initial_failure:break
  initial_calls=ev.calls
  report['initial_attempt']={'status':'bounded_failure'if initial_failure else'pass','failure':initial_failure,
   'consumer_calls':initial_calls,'seconds':time.monotonic()-initial_started}
  if initial_failure:
   dt=(ev.thi-ev.tlo)/4;times=[ev.tlo+k*dt for k in range(5)]
   pending=[(times[k],times[k+1],ev.xlo,ev.xhi,0)for k in reversed(range(4))]
   while pending:
    check(ev.calls<512,'signed consumer call budget inclusive initial attempt')
    t0,t1,x0,x1,depth=pending.pop();excess,row=signed_cell(ev,t0,t1,x0,x1,depth)
    if excess>0:row['status']='accepted';report['repair_cells'].append(row)
    elif depth>=9:
     row['status']='depth_failure';report['repair_choices'].append(row);raise BudgetStop('four-slab geometry repair failed atdepth9')
    else:
     row['status']='split';report['repair_choices'].append(row);mid=(x0+x1)/2
     pending.extend([(t0,t1,mid,x1,depth+1),(t0,t1,x0,mid,depth+1)])
  else:
   times=[ev.tlo,ev.thi];report['repair_cells']=[r for r in report['initial_attempt_cells']if r['status']=='accepted']
  for ta,tb in zip(times,times[1:]):
   slab=sorted([r for r in report['repair_cells']if r['t']==[str(ta),str(tb)]],key=lambda r:F(r['x'][0]))
   check(slab and F(slab[0]['x'][0])==ev.xlo and F(slab[-1]['x'][1])==ev.xhi,'signed endpoint coverage')
   check(all(F(a['x'][1])==F(b['x'][0])for a,b in zip(slab,slab[1:])),'signed contiguous closed coverage')
  minimum=min(arb(r['excess_norm2']).lower()for r in report['repair_cells'])
  maximum=max(arb(b['total']).upper()for r in report['repair_cells']for b in r['budgets'])
  check(minimum>0 and maximum<arb('1e-8'),'serialized signed consumer replay')
  report['summary']={'accepted_cells':len(report['repair_cells']),'repair_split_choices':len(report['repair_choices']),
   'initial_consumer_calls':initial_calls,'repair_consumer_calls':ev.calls-initial_calls,'total_consumer_calls':ev.calls,
   'coverage_verified':True,'maximum_added_component_error_norm':s(maximum),'minimum_signed_excess_norm2':s(minimum),
   'minimum_energy_lower_norm2':s(min(arb(r['energy_norm2']).lower()for r in report['repair_cells']))}
  report['status']='pass'
 except Exception as exc:report.update(status='bounded_failure',failure_type=type(exc).__name__,failure_message=str(exc))
 report['consumer_seconds']=time.monotonic()-started;report['total_seconds_including_setup']=ev.setup_seconds+report['consumer_seconds']
 return report

def prepare_wall(ev):
 """One positive-majorant integral; no new midpoint integration."""
 started=time.monotonic();T=arb(1)/5;Y=arb(1);counter=[0]
 def integrand(u,analytic):
  counter[0]+=1
  if counter[0]>200000:raise BudgetStop('wall positive-majorant callback budget')
  total=acb(0)
  for lam in ev.lams:total+=(2*lam*lam+3*lam)*(T*u*u+(9+Y)*u-ev.c*lam*(4*u).exp()).exp()
  return total*(1+(u+ev.d)**52)
 moment=acb.integral(integrand,0,ev.U,abs_tol=arb('1e-22'),rel_tol=arb('1e-25'),eval_limit=200000,depth_limit=30)
 check(moment.is_finite() and moment.imag.contains(0),'wall positive majorant integration')
 M=(ev.norm*moment.real).upper();B=4*ev.c*ev.pi*ev.m*ev.m-9-Y
 P=4*ev.sin4d*ev.pi*ev.m*ev.m-arb(1000)-2*T*ev.d
 ratio=(arb(ev.m+1)/ev.m)**4*(-ev.c*ev.pi*(2*ev.m+1)).exp()
 check(B>0 and P>0 and 8*ev.c*ev.pi*ev.m*ev.m>=T and ratio<1,'wall mode tail admissibility')
 S=(2*ev.pi*ev.pi*ev.m**4+3*ev.pi*ev.m*ev.m)*(-ev.c*ev.pi*ev.m*ev.m).exp()/(1-ratio)
 mode=[];source=[];minD=None;minC=None
 for j in range(3):
  Q=sum((math.comb(j,k)*ev.d**(j-k)*math.factorial(k)/B**k for k in range(j+1)),arb(0))
  mode.append((ev.norm*2*S*Q/P).upper());src=arb(0)
  for lam in ev.lams:
   D=4*ev.c*lam*(4*ev.U).exp()-9-Y-2*T*ev.U-arb(j)/(ev.U+ev.d);C=16*ev.c*lam*(4*ev.U).exp()-2*T
   check(D>0 and C>0,'wall source tangent admissibility')
   minD=D.lower()if minD is None else min(minD,D.lower());minC=C.lower()if minC is None else min(minC,C.lower())
   src+=(2*lam*lam+3*lam)*(ev.U+ev.d)**j*(T*ev.U*ev.U+(9+Y)*ev.U-ev.c*lam*(4*ev.U).exp()).exp()/D
  source.append((ev.norm*src).upper())
 wall={'M':M,'mode':mode,'source':source,'calls':0,'coeff_cache':{},
 'setup':{'common_derivative_majorant_norm':s(M),'majorant_dyadic':dyadic(M),
 'whole_wall_Taylor_norm':s((M*(arb(1)/ev.fact[25]+arb(1).exp()*A(F(21,200))**13/ev.fact[13])).upper()),
 'majorant_integral':s(moment.real),'majorant_callbacks':counter[0],'majorant_seconds':time.monotonic()-started,
 'mode_tail_norm':[s(v)for v in mode],'source_tail_norm':[s(v)for v in source],
 'admissibility':{'B':s(B),'P':s(P),'ratio':s(ratio),'eight_q_minus_T':s(8*ev.c*ev.pi*ev.m*ev.m-T),
 'minimum_source_D':s(minD),'minimum_source_concavity':s(minC)}}}
 ev.wall_context=wall;return wall

def wall_enclose(ev,t0,t1,y0,y1,wall=None):
 """Enclose H,Hx,Hxx on one closed wall cell; all errors are paid."""
 t0,t1,y0,y1=map(F,(t0,t1,y0,y1));check(F(0)<=t0<=t1<=F(1,5) and F(0)<=y0<=y1<=F(1),'wall domain')
 if wall is None:
  check(hasattr(ev,'wall_context'),'call prepare_wall once before wall_enclose');wall=ev.wall_context
 wall['calls']+=1;dt=box(t0,t1)-A(ev.tc);dx=acb(0,box(y0,y1));R=A(y1);Delta=A(max(abs(t0-ev.tc),abs(t1-ev.tc)))
 tw=[Delta**k/ev.fact[k]for k in range(ev.K+1)];sw=[R**l/ev.fact[l]for l in range(ev.L+1)]
 rem=(wall['M']*(R**25/ev.fact[25]+R.exp()*Delta**13/ev.fact[13])).upper();values=[];budgets=[]
 for j in range(3):
  key=(t0,t1,j)
  if key not in wall['coeff_cache']:
   wall['coeff_cache'][key]=[poly([(-1)**k*ev.values[j+l+2*k]/ev.fact[k]for k in range(ev.K+1)],dt)/ev.fact[l]for l in range(ev.L+1)]
  image=poly(wall['coeff_cache'][key],dx)
  quad=sum((sw[l]*tw[k]*ev.radii[j+l+2*k]for l in range(ev.L+1)for k in range(ev.K+1)),arb(0)).upper()
  total=(quad+rem+wall['mode'][j]+wall['source'][j]).upper();check(total<arb('1e-8'),'wall added coordinate error')
  values.append(image+acb(arb(0,total),arb(0,total)))
  budgets.append({'quadrature':quad,'taylor':rem,'mode':wall['mode'][j],'source':wall['source'][j],'total':total})
 return values,budgets

def run_wall_consumer(ev):
 started=time.monotonic();report={'kind':'vertical_wall','status':'started',
 'predeclared':{'domain':{'t':['0','1/5'],'real_z':1000,'imag_z':['0','1']},
 'normalization':'fixed G0(1000); never differentiated','strict_coordinate_margin_norm':'1e-3',
 'maximum_added_error_norm_per_coordinate':'1e-8','maximum_consumer_calls':512,'runtime_seconds':30,
 'new_midpoint_quadratures':0,'new_positive_majorant_quadratures':1,
 'subdivision':'four equal closed time slabs, then dyadic imaginary-height cells; no parameter repair'},
 'cells':[],'split_choices':[]}
 try:
  wall=prepare_wall(ev);report['setup']=wall['setup'];times=[F(k,20)for k in range(5)]
  pending=[(times[k],times[k+1],F(0),F(1),0)for k in reversed(range(4))]
  while pending:
   check(wall['calls']<512,'wall consumer call budget')
   if time.monotonic()-started>30:raise BudgetStop('30second wall budget')
   t0,t1,y0,y1,depth=pending.pop();values,budgets=wall_enclose(ev,t0,t1,y0,y1,wall)
   margin,coordinate=max([(values[0].real.abs_lower(),'real'),(values[0].imag.abs_lower(),'imag')],key=lambda a:float(a[0]))
   row={'t':[str(t0),str(t1)],'y':[str(y0),str(y1)],'depth':depth,'jet':[{'real':s(v.real),'imag':s(v.imag)}for v in values],
   'budgets':[{k:s(v)for k,v in b.items()}for b in budgets],'selected_coordinate':coordinate,'selected_margin_norm':s(margin)}
   if margin>arb('1e-3'):row['status']='accepted';report['cells'].append(row)
   else:
    row['status']='split';report['split_choices'].append(row);mid=(y0+y1)/2
    pending.extend([(t0,t1,mid,y1,depth+1),(t0,t1,y0,mid,depth+1)])
  for ta,tb in zip(times,times[1:]):
   slab=sorted([r for r in report['cells']if r['t']==[str(ta),str(tb)]],key=lambda r:F(r['y'][0]))
   check(slab and F(slab[0]['y'][0])==0 and F(slab[-1]['y'][1])==1,'wall endpoint coverage')
   check(all(F(a['y'][1])==F(b['y'][0])for a,b in zip(slab,slab[1:])),'wall contiguous closed coverage')
  minimum=min(arb(r['selected_margin_norm']).lower()for r in report['cells'])
  maximum=max(arb(b['total']).upper()for r in report['cells']for b in r['budgets'])
  check(minimum>arb('1e-3') and maximum<arb('1e-8'),'serialized wall consumer replay')
  report['summary']={'accepted_cells':len(report['cells']),'split_choices':len(report['split_choices']),'consumer_calls':wall['calls'],
   'minimum_selected_coordinate_margin_norm':s(minimum),'maximum_added_coordinate_error_norm':s(maximum),
   'closed_wall_coverage_verified':True,'negative_imaginary_height_by_real_conjugacy':True,'new_midpoint_quadratures':0}
  report['status']='pass'
 except Exception as exc:report.update(status='bounded_failure',failure_type=type(exc).__name__,failure_message=str(exc))
 report['seconds']=time.monotonic()-started;return report

def bounded(function,seconds):
 def alarm(signum,frame):raise BudgetStop(str(seconds)+'second bounded execution')
 old=signal.signal(signal.SIGALRM,alarm);signal.setitimer(signal.ITIMER_REAL,seconds)
 try:return function()
 finally:signal.setitimer(signal.ITIMER_REAL,0);signal.signal(signal.SIGALRM,old)

def write_record(path,data):
 path.write_text(json.dumps(data,indent=2)+'\n')

def main():
 parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--output-dir',type=Path,required=True)
 parser.add_argument('--repo',type=Path,required=True);parser.add_argument('--execution-model',required=True)
 parser.add_argument('--execution-effort',required=True);parser.add_argument('--bits',type=int,default=160)
 args=parser.parse_args();check(args.bits>=128,'at least128bits required');args.output_dir.mkdir(parents=True,exist_ok=True)
 meta=provenance(args.repo,args.execution_model,args.execution_effort,args.bits)
 # Construct once; every subsequent signed/wall consumer uses these same
 # exact midpoint dyadics. Outer alarms also bound positive-majorant calls.
 started=time.monotonic()
 try:ev=bounded(lambda:WholeCellEvaluator(args.bits),60)
 except Exception as exc:
  record=dict(meta,kind='shifted_setup',status='bounded_failure',failure_type=type(exc).__name__,failure_message=str(exc),seconds=time.monotonic()-started)
  write_record(args.output_dir/'SETUP.json',record);print(json.dumps(record));return 1
 setup=setup_record(ev,meta);write_record(args.output_dir/'SETUP.json',setup)
 # Exercise the exact JSON cache lane for the two actual consumers.
 ev=load_setup(json.loads((args.output_dir/'SETUP.json').read_text()))
 signed=dict(meta,**run_signed_consumer(ev));write_record(args.output_dir/'SIGNED_CONSUMER.json',signed)
 try:wall=dict(meta,**bounded(lambda:run_wall_consumer(ev),30))
 except Exception as exc:wall=dict(meta,kind='vertical_wall',status='bounded_failure',failure_type=type(exc).__name__,failure_message=str(exc))
 write_record(args.output_dir/'VERTICAL_WALL.json',wall)
 summary={'source_sha256':meta['source_sha256'],'output_dir':str(args.output_dir),'setup_seconds':setup['setup']['seconds'],
 'signed_status':signed['status'],'signed_summary':signed.get('summary'),'wall_status':wall['status'],'wall_summary':wall.get('summary'),
 'whole_execution_seconds':time.monotonic()-started}
 print(json.dumps(summary));return 0 if signed['status']==wall['status']=='pass'else 1
if __name__=='__main__':raise SystemExit(main())
