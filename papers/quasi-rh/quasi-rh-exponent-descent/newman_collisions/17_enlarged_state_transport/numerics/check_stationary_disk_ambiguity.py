#!/usr/bin/env python3
"""Certify two opposite stationary signs inside the coarse holomorphic error disk.

Uses the actual prescribed finite sum at one weak stationary-sweep point.
The alternative observations are not asserted to be the genuine theta flow.
Exact low jets are preserved under a normalized quadratic/cubic perturbation.
All arithmetic except timing uses directed Decimal intervals.
"""
import argparse
from decimal import Decimal
import hashlib
import json
from pathlib import Path
import platform
import sys
import time

PARSER = argparse.ArgumentParser(description=__doc__)
PARSER.add_argument('--record', type=Path)
PARSER.add_argument('--interval-source-dir', type=Path,
 default=Path(__file__).resolve().parents[2]/'13_microlocal_phase_space'/'numerics')
ARGS = PARSER.parse_args()
HASHES = {
 'check_block_current.py':'0cfca37632cfaaea522cce2a9514b81eaf9db0bf6213cd243de0f937679627a2',
 'check_complete_current_rectangle.py':'ac547ff45915d95369afc558f6ee3daa01fb6974ad1569e719dc3f0abcd4c522'}
for name, digest in HASHES.items():
 if hashlib.sha256((ARGS.interval_source_dir/name).read_bytes()).hexdigest()!=digest:
  raise RuntimeError('Retained source hash mismatch: '+name)
sys.path.insert(0, str(ARGS.interval_source_dir))
from check_complete_current_rectangle import (
 I, DOWN, UP, pi_interval, reduced_trig, factorial, absmax, add, rotate, real_data)

def pad(v, b): return v+I(b.copy_negate(), b)
def ia(v): return I(absmax(v))
def sym(v): return I(v.hi.copy_negate(), v.hi)
def hull(v): return I(min(x.lo for x in v), max(x.hi for x in v))
def contains_zero(v): return v.lo<=0<=v.hi

def derivative_envelopes(x, t, ell, ar, ai, U, V):
 alpha=ia(ar)+ia(ai); a1=ia(U)+ia(V)
 a2=2/x**2+24/x**3; a3=8/x**3+144/x**4
 gx=a1/4+t*(a1*a1+(alpha+ell)*a2)/8
 gxx=a2/8+t*(3*a1*a2+(alpha+ell)*a3)/16
 gxt=(a1*a1+(alpha+ell)*a2)/8
 gxxt=(3*a1*a2+(alpha+ell)*a3)/16
 return gx,gxx,gxt,gxxt,alpha,a1,a2,a3

def enclose():
 started=time.perf_counter()
 N,degree=22066,4
 pi=pi_interval(); logN=I(N).ln(); t0=1/(2*logN); x0=4*pi*N*N
 hbox=I('58.57'); middle=I('58.57'); dt=I(0)
 tb=t0+I(0,dt.hi); xb=x0+hbox; Lb=(xb/(4*pi)).ln()
 kappa=tb*Lb; natural=xb/(4*pi)+tb/16
 assert 0<tb.lo<=tb.hi<Decimal('.05')
 assert kappa.lo>=1 and kappa.hi<=Decimal('1.5')
 assert N*N<=natural.lo and natural.hi<(N+1)*(N+1)
 ar,ai,U,V,c,Omega,atanx,lc=real_data(x0,t0,pi)
 aN=I('.5')+t0*ar/2-t0*logN/2
 wN=(t0*logN*logN/4-(I('.5')+t0*ar/2)*logN).exp()
 T=(x0-t0*ai)/2
 carrier=pi*(N%2)-pi+atanx/4-x0*lc/8+t0*ai*(ar-logN)/2
 csine,ccosine=reduced_trig(carrier,pi)
 xhull=x0+I(0,hbox.hi)
 sar,sai,sU,sV,sc,sOmega,*_=real_data(xhull,t0,pi)
 bar,bai,bU,bV,bc,bOmega,*_=real_data(xb,tb,pi)
 moments=[[I(0),I(0)] for _ in range(degree)]
 moment12=I(0); spatial=[I(0) for _ in range(4)]
 budget=[I(0) for _ in range(4)]; max_residual=Decimal(0)
 for n in range(1,N+1):
  delta=(I(N)/n).ln(); ell=logN-delta; g0=delta/2
  amp=(aN*delta+t0*delta*delta/4).exp(); w0=wN*amp
  sine,cosine=reduced_trig(-T*delta-middle*delta/2,pi)
  mq=[amp*cosine,amp*sine]; power=I(1)
  for k in range(degree):
   moments[k]=add(moments[k],[power*mq[0],power*mq[1]])
   power*=g0
  moment12+=w0*power
  residual_imag=sOmega-sc*logN+(sc-I('.5'))*delta
  residual=ia(t0*sV*ell/4)+ia(residual_imag)
  max_residual=max(max_residual,residual.hi)
  growth=(I(hbox.hi)*residual).exp()
  exp_error=I(0,UP.subtract(growth.hi,Decimal(1)))
  sgx,sgxx,*_=derivative_envelopes(xhull,t0,ell,sar,sai,sU,sV)
  sgamma=g0+residual
  differences=[exp_error,
   g0*exp_error+residual*growth,
   g0*g0*exp_error+((2*g0+residual)*residual+sgx)*growth,
   g0**3*exp_error+((3*g0*g0+3*g0*residual+residual*residual)*residual
                    +3*sgamma*sgx+sgxx)*growth]
  for j in range(4): spatial[j]+=w0*differences[j]
  wb=(tb*ell*ell/4-(I('.5')+tb*bar/2)*ell).exp()
  chi=ia(ell*ell/4-bar*ell/2)+ia(bai*(bar-ell)/2)
  gamma=ia(tb*bV*ell/4)+ia(bOmega-bc*ell)
  gamma_t=ia(bV*ell/4)+ia((bU*(bar-ell)-bai*bV)/4)
  bgx,bgxx,bgxt,bgxxt,*_=derivative_envelopes(xb,tb,ell,bar,bai,bU,bV)
  terms=[chi, gamma_t+gamma*chi,
   2*gamma*gamma_t+bgxt+(gamma*gamma+bgx)*chi,
   3*gamma*gamma*gamma_t+3*gamma_t*bgx+3*gamma*bgxt+bgxxt
                    +(gamma**3+3*gamma*bgx+bgxx)*chi]
  for j in range(4): budget[j]+=wb*terms[j]
 jets=[]
 for k,moment in enumerate(moments):
  rotated=rotate(moment,csine,ccosine,wN)
  for _ in range(k%4): rotated=[rotated[1],-rotated[0]]
  jets.append(rotated)
 transport=[spatial[j]+dt*budget[j] for j in range(4)]
 lam=(bai*(1+tb*bU/2)+bar*tb*bV/2)/2
 *_,alpha,a1,a2,a3=derivative_envelopes(xb,tb,logN,bar,bai,bU,bV)
 lam1=sym((a1+tb*(a1*a1+alpha*a2)/2)/4)
 lam2=sym((a2+tb*(3*a1*a2+alpha*a3)/2)/8)
 nc=[I(1),lam,lam*lam+lam1,lam**3+3*lam*lam1+lam2]
 eta=5*(-tb*Lb*Lb/16-Lb/4).exp()
 cauchy=[eta*factorial(j)*Lb**j for j in range(4)]
 paid_error=[cauchy[0],cauchy[1]+ia(lam)*cauchy[0],
  cauchy[2]+2*ia(lam)*cauchy[1]+ia(nc[2])*cauchy[0],
  cauchy[3]+3*ia(lam)*cauchy[2]+3*ia(nc[2])*cauchy[1]+ia(nc[3])*cauchy[0]]
 def enclosed_jets(offset):
  f=[]
  for j in range(4):
   val=I(0)
   for k in range(j,degree): val+=jets[k][0]*offset**(k-j)/factorial(k-j)
   rem=moment12*ia(offset)**(degree-j)/factorial(degree-j)
   f.append(pad(2*val,(2*(rem+transport[j])).hi))
  K=[f[0],f[1]+lam*f[0],f[2]+2*lam*f[1]+nc[2]*f[0],
     f[3]+3*lam*f[2]+3*nc[2]*f[1]+nc[3]*f[0]]
  return [pad(K[j],paid_error[j].hi) for j in range(4)],K
 # Only the finite-sum transport intervals are used in the construction.
 # The independent Cauchy errors are reported to identify the coarse budget.
 Kpaid,K=enclosed_jets(I(0))
 a2=-K[2]/(2*eta*Lb**2)
 norm_bound=ia(a2)+I('.5')
 assert norm_bound.hi<Decimal(1)
 assert K[1].hi<0
 energy=K[0]**2+K[1]**2
 assert energy.lo>0
 half_cubic=3*eta*Lb**3
 variants=[]
 for sgn in (-1,1):
  k3=K[3]-3*lam*K[2]+sgn*half_cubic
  product=K[1]*k3
  if sgn<0:
   assert k3.hi<0 and product.lo>0
  else:
   assert k3.lo>0 and product.hi<0
  variants.append({'cubic_coefficient':str(Decimal(sgn)/2),
   'stationary_Hxx_over_A':'0 exactly by construction',
   'third_jet_over_A':k3.strings(),
   'stationary_product_over_A_squared':product.strings(),
   'stationary_product_over_first_jet_energy':(product/energy).strings(),
   'sign':'adverse' if sgn<0 else 'favorable'})
 return {
  'status':'PASS','date':'2026-10-10','prepared_for':'Edward Baker',
  'model_family':'GPT-6 (Codex)','reasoning_effort':'not exposed; not inferred',
  'acknowledgment':'Substantial LLM assistance; internal outward computation, not independent mathematical validation.',
  'scope':'Two analytic observations with identical value and slope, exact Hxx=0 and opposite Hx Hxxx signs, both strictly inside the printed normalized disk envelope around the actual finite approximant. No assertion identifies either observation with genuine theta.',
  'arithmetic':'60-digit directed Decimal; explicit trigonometric remainders; no binary float in enclosures or decisions',
  'N':N,'number_of_terms':N,
  'domain':{'definition':'t0=1/(2 log N); x=4 pi N^2+58.57; disk radius 1/L',
   'time':tb.strings(),'height':xb.strings(),'L':Lb.strings(),
   'kappa':kappa.strings(),'natural_cutoff_squared':natural.strings()},
  'normalizer':{'definition':'A=exp(Re m_t)>0; K_j=G^(j)/A for the complete finite reflected G',
   'lambda':lam.strings(),'lambda_prime':lam1.strings(),'lambda_second':lam2.strings()},
  'finite_physical_normalized_jets':[v.strings() for v in K],
  'independently_paid_theta_jet_boxes':[v.strings() for v in Kpaid],
  'payments':{'coarse_eta':eta.strings(),
   'Cauchy_physical_normalized_derivative_errors':[v.strings() for v in paid_error],
   'spatial_finite_transport_errors':[v.strings() for v in spatial],
   'total_finite_transport_errors':[v.strings() for v in transport],
   'max_spatial_residual':str(max_residual)},
  'perturbation':{'definition':'Hstar=G+A eta(a2 w^2 + d w^3), w=L(z-x), a2=-K2/(2 eta L^2), d=+/-1/2',
   'quadratic_coefficient':a2.strings(),
   'upper_bound_on_disk_norm_divided_by_eta':norm_bound.strings(),
   'first_jet_energy_over_A_squared':energy.strings(),
   'half_cubic_third_jet_change':half_cubic.strings(),
   'exact_preserved_jets':'Hstar/A=K0 and Hstar_x/A=K1 at the center',
   'variants':variants},
  'imported_sources':HASHES,
  'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
  'python_version':platform.python_version(),'runtime_seconds':str(time.perf_counter()-started),
  'limitations':['This certifies ambiguity of the coarse disk interface, not an adverse genuine theta stationary point.',
   'The two center first jets are nonzero, so neither constructed center is a collision.',
   'Jointly analytic local heat alternatives require the separate polynomial-approximation argument in the accompanying note; direct analytic backward evolution is not assumed.',
   'A sharper or theta-specific correlated remainder can distinguish the alternatives.',
   'No uniform relative bound, new genuine collision exclusion, or RH conclusion is obtained.']}

if __name__=='__main__':
 result=enclose()
 if ARGS.record: ARGS.record.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
 print(json.dumps({k:result[k] for k in ['status','finite_physical_normalized_jets','perturbation','runtime_seconds']},indent=2))
