#!/usr/bin/env python3
"""Reproducible Hubbard-dimer heat trial benchmark; no external dependencies.
Prepared for Edward Baker, 2026-10-14, with substantial LLM assistance.
Recorded model: gpt-6.1-sol; reasoning effort: ultra.
All certificates use rational outward intervals, not floating-point scans.
"""
from fractions import Fraction as F
from math import sqrt, isqrt
from decimal import Decimal, localcontext, ROUND_FLOOR, ROUND_CEILING
from pathlib import Path
import argparse, hashlib, json, platform

DATE='2026-10-14'
DIM=4
T=F(6); SHIFT=F(3); U=F(4); BETA=F(1)
RATES=[F(1),F(3),F(5)]
H0=[[F(v) for v in row] for row in [[0,-1,-1,0],[-1,0,0,-1],[-1,0,0,-1],[0,-1,-1,0]]]
V=[[U if i==j and i in [0,3] else F(0) for j in range(DIM)] for i in range(DIM)]
H=[[H0[i][j]+V[i][j] for j in range(DIM)] for i in range(DIM)]
B=[[H0[i][j]+(SHIFT if i==j else 0) for j in range(DIM)] for i in range(DIM)]
A=[[H[i][j]+(SHIFT if i==j else 0) for j in range(DIM)] for i in range(DIM)]
ID=[[F(i==j) for j in range(DIM)] for i in range(DIM)]

def mm(a,b):
 return [[sum(a[i][k]*b[k][j] for k in range(DIM)) for j in range(DIM)] for i in range(DIM)]

def spectral_projector(l):
 p=ID
 for k in RATES:
  if k!=l:
   p=mm(p,[[(B[i][j]-k*ID[i][j])/(l-k) for j in range(DIM)] for i in range(DIM)])
 return p
PROJECTORS=[spectral_projector(l) for l in RATES]

class I:
 """Closed interval with exact rational endpoints."""
 def __init__(self,lo,hi=None):
  if isinstance(lo,I): self.lo,self.hi=lo.lo,lo.hi; return
  self.lo=F(lo); self.hi=self.lo if hi is None else F(hi)
  assert self.lo<=self.hi
 def __add__(self,x):
  x=I(x); return I(self.lo+x.lo,self.hi+x.hi)
 __radd__=__add__
 def __neg__(self):return I(-self.hi,-self.lo)
 def __sub__(self,x):return self+-I(x)
 def __rsub__(self,x):return I(x)+-self
 def __mul__(self,x):
  x=I(x); p=[self.lo*x.lo,self.lo*x.hi,self.hi*x.lo,self.hi*x.hi]; return I(min(p),max(p))
 __rmul__=__mul__
 def __truediv__(self,x):
  x=I(x); assert not x.lo<=0<=x.hi; return self*I(1/x.hi,1/x.lo)
 def __rtruediv__(self,x):return I(x)/self
 def __pow__(self,n):
  assert isinstance(n,int) and n>=0
  if n==0:return I(1)
  if n%2 and n==1:return self
  if self.lo>=0:return I(self.lo**n,self.hi**n)
  if self.hi<=0:
   return I(self.lo**n,self.hi**n) if n%2 else I(self.hi**n,self.lo**n)
  return I(min(self.lo**n,self.hi**n),max(self.lo**n,self.hi**n)) if n%2 else I(0,max(self.lo**n,self.hi**n))
 def sqrt(self,bits=160):
  assert self.lo>=0, float(self.lo)
  den=1<<bits
  lo=F(isqrt((self.lo.numerator<<(2*bits))//self.lo.denominator),den)
  hi=F(isqrt((self.hi.numerator<<(2*bits))//self.hi.denominator)+1,den)
  return I(lo,hi)
 def string(self):
  def dec(x,rounding):
   with localcontext() as c:
    c.prec=29; c.rounding=rounding
    return str(Decimal(x.numerator)/Decimal(x.denominator))
  return {'lo':dec(self.lo,ROUND_FLOOR),'hi':dec(self.hi,ROUND_CEILING)}

# Alternating series through degrees 31 and 32 encloses e^-1.
s=F(1); term=F(1); lower=None
for k in range(1,33):
 term*=-F(1,k);s+=term
 if k==31:lower=s
EXP_MINUS_ONE=I(lower,s)

def exp_minus_integer(x):
 assert F(x).denominator==1 and x>=0
 return EXP_MINUS_ONE**int(x)

EXP_T=[exp_minus_integer(l*T) for l in RATES]
EXP_2T=[exp_minus_integer(2*l*T) for l in RATES]
F_T=[(1-e)/l for l,e in zip(RATES,EXP_T)]
J0=[(1-e)/(2*l) for l,e in zip(RATES,EXP_2T)]
J1=[(1-e*(1+2*l*T))/(4*l*l) for l,e in zip(RATES,EXP_2T)]

def midpoint(x):return float((x.lo+x.hi)/2)

class Work:
 def __init__(self):
  self.d={k:0 for k in ['multiplications','additions','dot_products','H_actions','V_actions','A_actions','projector_actions','linear_combinations','square_roots']}
 def inc(self,k,n=1):self.d[k]+=n
 def units(self):return self.d['multiplications']+self.d['additions']

def matvec(M,v,w=None,kind=None):
 out=[]
 if w and kind:w.inc(kind)
 for row in M:
  terms=[a*b for a,b in zip(row,v) if a!=0]
  if w:w.inc('multiplications',len(terms));w.inc('additions',max(0,len(terms)-1))
  out.append(sum(terms))
 return out

def dot(v,z,w=None):
 if w:w.inc('dot_products');w.inc('multiplications',DIM);w.inc('additions',DIM-1)
 return sum(a*b for a,b in zip(v,z))

def combine(c,vs,w=None):
 if w:w.inc('linear_combinations');w.inc('multiplications',DIM*len(c));w.inc('additions',DIM*(len(c)-1))
 return [sum(a*v[i] for a,v in zip(c,vs)) for i in range(DIM)]

def rho_of(p,q):
 aa=[F(1),p] if p is not None else [F(0),F(1)]
 bb=[F(1),q] if q is not None else [F(0),F(1)]
 return [a*b for a in aa for b in bb]

def prepare(p,q,w=None):
 rho=rho_of(p,q)
 return rho,[matvec(P,rho,w,'projector_actions') for P in PROJECTORS]

# Numerical functions share exactly the same spectral-mode representation.
FTf=list(map(midpoint,F_T)); ETf=list(map(midpoint,EXP_T)); J0f=list(map(midpoint,J0)); J1f=list(map(midpoint,J1))
Hf=[[float(x) for x in r] for r in H]; Vf=[[float(x) for x in r] for r in V]
Pf=[[[float(x) for x in r] for r in P] for P in PROJECTORS]

def num_prepare(p,q,w):
 rho=list(map(float,rho_of(p,q)))
 w.inc('multiplications',4)  # initial tensor product construction
 return rho,[matvec(P,rho,w,'projector_actions') for P in Pf]

def diagonals(v,w):
 ns=[dot(x,x,w) for x in v]
 w.inc('multiplications',6);w.inc('additions',4)
 return sum(a*b for a,b in zip(J0f,ns)),sum(a*b for a,b in zip(J1f,ns))

def num_uncorrected(p,q,w):
 rho,v=num_prepare(p,q,w); q0,q1=diagonals(v,w)
 return 2*q0/(4*q1)-3

def num_direct(p,q,w):
 rho,v=num_prepare(p,q,w);psi=combine(FTf,v,w); hp=matvec(Hf,psi,w,'H_actions')
 return dot(psi,hp,w)/dot(psi,psi,w)

def num_residual(p,q,w):
 rho,v=num_prepare(p,q,w);q0,q1=diagonals(v,w)
 terminal=combine(ETf,v,w); rn=[matvec(Vf,x,w,'V_actions') for x in v]; R=combine(FTf,rn,w)
 w.inc('square_roots',2)
 nlow=(sqrt(4*q1)-sqrt(dot(terminal,terminal,w)))**2
 return (2*q0+dot(R,R,w)/4)/nlow-3

def moments(z,k):
 if z==0:return I(T if k==0 else T*T/2)
 e=exp_minus_integer(z*T)
 return (1-e)/z if k==0 else (1-e*(1+z*T))/(z*z)

def norm_integral(v,rs,k):
 total=I(0)
 for i in range(len(v)):
  for j in range(i,len(v)):
   total+=(1 if i==j else 2)*dot(v[i],v[j])*moments(rs[i]+rs[j],k)
 return total

def cross_integral(v,vr,z,zr,k=0):
 return sum(dot(a,b)*moments(ra+rb,k) for a,ra in zip(v,vr) for b,rb in zip(z,zr))

def certify(p,q):
 rho,v=prepare(p,q);ns=[dot(x,x) for x in v]
 q0=sum(a*b for a,b in zip(J0,ns));q1=sum(a*b for a,b in zip(J1,ns))
 psi=combine(F_T,v);terminal=combine(EXP_T,v)
 norm=dot(psi,psi);energy=dot(psi,matvec(H,psi)); rayleigh=energy/norm
 R=combine(F_T,[matvec(V,x) for x in v]);rnorm2=dot(R,R)
 nroot=(4*q1).sqrt()-dot(terminal,terminal).sqrt()/BETA
 assert nroot.lo>0
 nlow=nroot**2
 upper=(2*q0+rnorm2/U)/nlow-SHIFT
 # Exact residual identity confirms A Psi = rho + R - u(T).
 relation=[x-y-z+t for x,y,z,t in zip(matvec(A,psi),rho,R,terminal)]
 assert all(x.lo<=0<=x.hi for x in relation)
 eb=sum(l*f*f*n for l,f,n in zip(RATES,F_T,ns))
 projector_energy=(eb+rnorm2/U)/norm-SHIFT
 # Generic CS (3) from the seed note, evaluated with the same path and T.
 uconst=combine([-e/l for e,l in zip(EXP_T,RATES)],v)
 uc=[uconst]+[[x/l for x in vv] for l,vv in zip(RATES,v)]
 dc=[matvec(A,uconst)]+[[x/l-y for x,y in zip(matvec(A,vv),vv)] for l,vv in zip(RATES,v)]
 rs=[F(0)]+RATES
 d0=norm_integral(dc,rs,0);d1=norm_integral(dc,rs,1);v0=norm_integral(uc,rs,0)
 assert d0.lo>0 and d1.lo>0 and v0.lo>0
 de=2*(q0*d0).sqrt();dn=4*(q1*d1).sqrt()+2*(v0*d0).sqrt();generic_den=4*q1-dn
 corrected_e=2*q0+2*cross_integral(v,RATES,dc,rs)
 corrected_n=4*q1+4*cross_integral(v,RATES,dc,rs,1)-2*cross_integral(uc,rs,dc,rs)
 diff_e=corrected_e-(energy+SHIFT*norm);diff_n=corrected_n-norm
 assert diff_e.lo<=0<=diff_e.hi and diff_n.lo<=0<=diff_n.hi
 assert max(rayleigh.lo,projector_energy.lo)<=min(rayleigh.hi,projector_energy.hi)
 out={
  'finite_time_seed_energy_and_norm_identity_interval_checks':True,
  'parameters':{'p':'infinity' if p is None else str(p),'q':'infinity' if q is None else str(q)},
  'uncorrected_energy':(2*q0/(4*q1)-SHIFT).string(),
  'integrated_trial_rayleigh':rayleigh.string(),
  'endpoint_projector_residual_upper':upper.string(),
  'exact_projector_residual_rayleigh':projector_energy.string(),
  'N':norm.string(),'N_lower':nlow.string(),'Q0':q0.string(),'Q1':q1.string(),
  'integrated_residual_norm_squared':rnorm2.string(),
  'generic_Cauchy_denominator':generic_den.string(),
  'generic_delta_E':de.string(),'generic_delta_N':dn.string(),
  'beats_single_product_Slater_global_lower_minus_half':upper.hi < -F(1,2),
  'rayleigh_interval_width_below_1e_minus_25':rayleigh.hi-rayleigh.lo<F(1,10**25),
  'upper_interval_width_below_1e_minus_25':upper.hi-upper.lo<F(1,10**25),
  'uncorrected_violates_ground_bound':(2*q0/(4*q1)-SHIFT).hi < (I(2)-2*I(2).sqrt()).lo,
 }
 assert out['rayleigh_interval_width_below_1e_minus_25'] and out['upper_interval_width_below_1e_minus_25']
 return out

GRID=[F(0),F(1,8),F(1,4),F(3,8),F(1,2),F(3,4),F(1),F(4,3),F(2),F(8,3),F(4),F(8),None]

def num_generic_den(p,q):
 # Float diagnostic only: selected certificates establish failure rigorously.
 rho,v=prepare(p,q);v=[list(map(float,x)) for x in v]
 q0=sum(a*dot(x,x) for a,x in zip(J0f,v));q1=sum(a*dot(x,x) for a,x in zip(J1f,v))
 uconst=combine([-e/float(l) for e,l in zip(ETf,RATES)],v)
 uc=[uconst]+[[x/float(l) for x in vv] for l,vv in zip(RATES,v)]
 Af=[[float(x) for x in r] for r in A]
 dc=[matvec(Af,uconst)]+[[x/float(l)-y for x,y in zip(matvec(Af,vv),vv)] for l,vv in zip(RATES,v)]
 rs=[F(0)]+RATES
 def ni(v,k):
  return sum((1 if i==j else 2)*dot(v[i],v[j])*midpoint(moments(rs[i]+rs[j],k)) for i in range(4) for j in range(i,4))
 d0=ni(dc,0);d1=ni(dc,1);v0=ni(uc,0)
 return (4*q1-4*sqrt(q1*d1)-2*sqrt(v0*d0))/dot(rho,rho)

def main():
 parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path,default=Path(__file__).with_name('HUBBARD_HEAT_BENCHMARK_20261014.json'));args=parser.parse_args()
 methods={'uncorrected':num_uncorrected,'integrated_trial_direct_variational':num_direct,'endpoint_projector_residual':num_residual}
 results={};work={};best={}
 for name,fn in methods.items():
  w=Work();rows=[]
  for p in GRID:
   for q in GRID:rows.append((fn(p,q,w),p,q))
  row=min(rows,key=lambda r:r[0]);best[name]=(row[1],row[2]);results[name]={'evaluated_candidates':len(rows),'minimum_numeric':row[0],'p':'infinity' if row[1] is None else str(row[1]),'q':'infinity' if row[2] is None else str(row[2])};work[name]={**w.d,'multiply_add_work_units':w.units()}
 # Use direct Rayleigh on the identical continuous rational Slater family at
 # the residual scan's multiplication-plus-addition budget. Repeated shared
 # candidates are intentionally charged, so no caching advantage is hidden.
 budget=work['endpoint_projector_residual']['multiply_add_work_units'];wd=Work();dense=[F(i,16) for i in range(65)]+[None]
 candidates=[(p,q) for p in GRID for q in GRID]+[(p,q) for p in dense for q in dense if (p,q) not in {(x,y) for x in GRID for y in GRID}]
 matched=[]
 direct_cost=work['integrated_trial_direct_variational']['multiply_add_work_units']//169
 assert direct_cost*169==work['integrated_trial_direct_variational']['multiply_add_work_units']
 for p,q in candidates:
  # The evaluator's operation count is state independent. Check the fixed
  # cost before executing, so a rejected final evaluation is never hidden.
  if wd.units()+direct_cost>budget:break
  local_work=Work(); value=num_direct(p,q,local_work)
  assert local_work.units()==direct_cost
  for k,v in local_work.d.items():wd.d[k]+=v
  matched.append((value,p,q))
 row=min(matched,key=lambda r:r[0])
 csdens=[num_generic_den(p,q) for p in GRID for q in GRID]
 certs={name:certify(*params) for name,params in best.items()}
 # Duplicate tied minima may have opposite-site conventions, both certified.
 record={
  'date':DATE,'prepared_for':'Edward Baker','LLM_assistance':'substantial','model':'gpt-6.1-sol','reasoning_effort':'ultra',
  'status':'rigorous selected-state enclosures; grid optimization evidence is numerical',
  'Hamiltonian':{'sector':'N_up=N_down=1, hence N=2','basis':['L_up L_down','L_up R_down','R_up L_down','R_up R_down'],'hopping':1,'repulsion':4,'shift':3,'surrogate':'B=H_hop+3I','beta':1,'time':6,'H':[[str(x) for x in r] for r in H]},
  'state_family':'rho=(1,p)_up tensor (1,q)_down, including localized endpoints; Psi=int_0^T exp(-tB)rho dt',
  'grid':[str(x) if x is not None else 'infinity' for x in GRID],
  'integration':{'method':'closed exponential moments, common analytic integration for every method; no time-node quadrature','rigorous_arithmetic':'Fraction endpoints; alternating e^-1 series through 31/32, integer powers; integer-isqrt outward square roots','enclosure_width_target':'1e-25'},
  'ground_energy':(I(2)-2*I(2).sqrt()).string(),
  'single_product_Slater_global_minimum':{'exact':'-1/2','proof':'E >= 2-s-sqrt(5-4s^2) >= -1/2, 0<=s<=1; equality at s=1/2'},
  'same_169_candidates':results,'actual_counted_work_for_same_169_candidates':work,
  'direct_variational_at_residual_arithmetic_budget':{'work_metric':'instrumented vector/mode multiplications plus additions, including initial tensor product; scalar exponentials precomputed for all methods; scalar final quotient/sqrt operations not priced, sqrt counts shown separately','budget':budget,'fixed_per_candidate_work':direct_cost,'rejected_evaluations_performed':0,'used_work':wd.units(),'candidate_count':len(matched),'minimum_numeric':row[0],'p':'infinity' if row[1] is None else str(row[1]),'q':'infinity' if row[2] is None else str(row[2]),'work_counts':wd.d},
  'generic_Cauchy_grid_diagnostic':{'certified':False,'positive_denominator_candidate_count':sum(x>0 for x in csdens),'largest_denominator_divided_by_initial_norm_squared':max(csdens),'rigorous_failure_at_selected_states':'see rational interval certificates'},
  'selected_state_rational_interval_certificates':certs,
  'limitations':['The four-dimensional state representation makes direct Rayleigh evaluation cheaper than residual accumulation.','The interaction-gap estimate applies to repulsive Hubbard V, not to arbitrary signed interactions or gapless continuum potentials.','No floating grid minimum is claimed globally optimal.','This small benchmark demonstrates a certified correlated trial bound, not scalable many-body computational advantage or literature novelty.'],
  'reproducibility':{'python_version':platform.python_version(),'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()},
 }
 args.output.write_text(json.dumps(record,indent=2)+'\n')
 print(json.dumps({'output':str(args.output),'grid_minima':results,'work':work,'matched_budget_direct':record['direct_variational_at_residual_arithmetic_budget'],'certified_Neel_upper':certs['endpoint_projector_residual']['endpoint_projector_residual_upper']},indent=2))

if __name__=='__main__':main()
