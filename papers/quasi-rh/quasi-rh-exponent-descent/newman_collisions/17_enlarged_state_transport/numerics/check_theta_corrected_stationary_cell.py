#!/usr/bin/env python3
"""Certify a genuine theta stationary branch with the retained leading correction.

Polymath Corollary 6.4 and Proposition 6.6 supply the complete A+B-C
remainder. A real-amplitude comparison replaces its nonholomorphic C
by a holomorphic exponential at each center. The normalized analytic
residual is paid through three physical derivatives, including the
normalizer derivatives. Binary floats are used only for elapsed time.
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
from check_block_current import atan_small
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

def sqrt_i(v): return (v.ln()/2).exp()

def correction_ledger(xb,tb,pi,N):
 r=I('.05'); xm=xb-r; xp=xb+r
 qm=xm/(4*pi); qp=xp/(4*pi); V=xm/2
 S=sqrt_i(xp*xp+(1+r)**2)/2
 amin=qm.ln()/2-1/(V*V)
 astar=3/(2*V)+sqrt_i((S/(2*pi)).ln()**2+pi*pi/4)/2
 dstar=3/(2*V*V)+1/(2*V)
 kcost=(r*astar*(1+tb*dstar/2)/2).exp()
 tiny_k=tb*r/(2*(xm-6))
 nab=(tiny_k*I(N).ln()).exp()
 ab=I(0)
 for n in range(1,N+1):
  ln=I(n).ln(); d=ln*ln/4-amin*ln/2
  wn=(-ln/2+tb*d).exp()
  ell=hull([ia(qm.ln()-2*ln),ia(qp.ln()-2*ln)])
  # A single enclosing maximum suffices; its lower endpoint is irrelevant.
  ell=I(0,ell.hi)
  un=((tb*tb*ell*ell/16+I('.626'))/(xm-I('6.66'))).exp()-1
  ab+=(1+nab*(r*ln).exp())*wn*un
 z=(-qm.ln()/4-tb*qm.ln()**2/16+
    (3*sqrt_i(qp.ln()**2+pi*pi/4)+I('3.58'))/(xm-I('8.52'))).exp()
 bc=I('1.24')*((r*I(3).ln()).exp()+(-r*I(3).ln()).exp())/(I(N)-I('.125'))+I('6.92')/(xm-12)
 tau_m=xm/2+pi*tb/8; tau_p=xp/2+pi*tb/8
 a_m=sqrt_i(tau_m/(2*pi)); a_p=sqrt_i(tau_p/(2*pi))
 assert N<=a_m.lo and a_p.hi<N+1
 p_disk=1-2*(hull([a_m,a_p])-N)
 assert Decimal('.99')<=p_disk.lo<=p_disk.hi<=Decimal('1.01')
 J=3/(4*tau_m)*(1+2/tau_m)+(4+6/tau_m)/(4*pi*a_m)+1/(tau_m*tau_m)
 # Enclose (tau_+/tau_-)^(3/2) with an outward log/exponential.
 geometry=2*r*((tau_p/tau_m).ln()*I('1.5')).exp()*J
 eta=kcost*(ab+z*(bc+geometry))
 # Stable real formula for C(t,x)/A(t,x), avoiding exp(-pi*x/8).
 ar,ai,*_=real_data(xb,tb,pi)
 tau=xb/2+pi*tb/8; a=sqrt_i(tau/(2*pi)); p=1-2*(a-N)
 sn,cs=reduced_trig(pi*(p*p/2+I('.375')),pi)
 _,cp=reduced_trig(pi*p,pi)
 _,ch=reduced_trig(pi*p/2,pi)
 u=cs/(2*cp); v=(sn-sqrt_i(I(2))*ch)/(2*cp)
 atanrec=atan_small(1/xb,6)
 logpref=pi.ln()/4+3*I(2).ln()+I('1.5')*tau.ln()-I('1.75')*xb.ln()-I('.875')*(1+1/(xb*xb)).ln()-xb*atanrec/4+I('.25')-tb*pi*pi/64-tb*(ar*ar-ai*ai)/4
 correction=((-1)**(N+1))*logpref.exp()*(u-v/tau)
 return correction,eta,r,{
  'disk_radius':r.strings(),'normalizer_cost_K':kcost.strings(),
  'AB_error_before_normalizer':ab.strings(),'Z':z.strings(),
  'C_source_relative_error_B':bc.strings(),
  'C_real_amplitude_slope_bound_J':J.strings(),
  'C_holomorphic_comparison_cost':geometry.strings(),
  'normalized_holomorphic_remainder_eta':eta.strings(),
  'disk_p_range':p_disk.strings(),'real_p_range':p.strings(),
  'real_correction_C_over_A':correction.strings(),
  'u':u.strings(),'v':v.strings(),'log_prefactor_over_A':logpref.strings()}


def enclose():
 started=time.perf_counter()
 N,degree=22066,12
 pi=pi_interval(); logN=I(N).ln(); t0=1/(2*logN); x0=4*pi*N*N
 hbox=I('58.567','58.571'); middle=I('58.569'); dt=I('.00000001')
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
 coarse_eta=5*(-tb*Lb*Lb/16-Lb/4).exp()
 correction,eta,disk_r,ledger=correction_ledger(xb,tb,pi,N)
 cauchy=[eta*factorial(j)/(disk_r**j) for j in range(4)]
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
  return [pad(K[j]-correction*((-pi/8)**j),paid_error[j].hi) for j in range(4)],K
 subcells=[]; allK=[[] for _ in range(4)]; candidates=[]
 eliminated=[]; decay=-pi/8
 for k in range(8):
  h=I('58.567')+I(k,k+1)/2000
  K,Kfinite=enclosed_jets(h-middle)
  for j in range(4): allK[j].append(K[j])
  candidate=contains_zero(K[2])
  if candidate:
   candidates.append((h,K))
   corr1=pad(Kfinite[1]-Kfinite[2]/decay,(paid_error[1]+paid_error[2]/(-decay)).hi)
   corr3=pad(Kfinite[3]-decay*Kfinite[2],(paid_error[3]+ia(decay)*paid_error[2]).hi)
   assert corr1.hi<0 and corr3.lo>0
   eliminated.append({'height_offset':h.strings(),'conditional_Hx_over_A':corr1.strings(),'conditional_Hxxx_over_A':corr3.strings(),'conditional_product_over_A_squared':(corr1*corr3).strings()})
  assert K[1].hi<0 and K[3].lo>0
  assert (K[1]*K[3]).hi<0
  subcells.append({'height_offset':h.strings(),
   'physical_normalized_H_jets':[v.strings() for v in K],
   'finite_physical_normalized_jets':[v.strings() for v in Kfinite],
   'Hxx_stationary_candidate':candidate,
   'S1_product_Hx_Hxxx_over_A_squared':(K[1]*K[3]).strings()})
 whole=[hull(v) for v in allK]
 left=enclosed_jets(I('-.002'))[0]; right=enclosed_jets(I('.002'))[0]
 assert left[2].hi<0<right[2].lo
 assert candidates
 candidate_band=hull([c[0] for c in candidates])
 product=hull([K[1]*K[3] for h,K in candidates])
 # Division is used only after the paid slope separation is proved.
 stiffness=hull([-K[3]/K[1] for h,K in candidates])
 return {
 'status':'PASS','date':'2026-10-11','prepared_for':'Edward Baker',
 'model_family':'GPT-6 (Codex)','reasoning_effort':'not exposed to this worker; not inferred',
 'acknowledgment':'Prepared with substantial LLM assistance; internal outward arithmetic replay, not independent mathematical validation.',
 'scope':'One nonempty genuine theta Hxx stationary branch using Polymath A+B-C source bounds and the explicitly derived holomorphic exponential comparison. Every time in the rectangle has exactly one Hxx zero and strict Hx Hxxx<0 there.',
 'arithmetic':'60-digit outward Decimal with explicit atan/trig remainders and outward integer powers; no binary float in signs',
 'N':N,'number_of_terms':N,'Taylor_degree':degree-1,'subcell_count':8,
 'domain':{'definition':'t0=1/(2 log N), x0=4 pi N^2; t in [t0,t0+1e-8], x in x0+[58.567,58.571]',
  'time':tb.strings(),'height':xb.strings(),'L':Lb.strings(),'kappa':kappa.strings(),
  'natural_cutoff_squared':natural.strings()},
 'normalizer':{'definition':'A=exp(Re m_t)>0, observed K_j=H_j/A',
  'lambda':lam.strings(),'lambda_prime':lam1.strings(),'lambda_second':lam2.strings()},
 'theta_correction_ledger':ledger,
 'payments':{'coarse_eta':coarse_eta.strings(),'eta':eta.strings(),'normalized_corrected_remainder_derivative_errors':[v.strings() for v in cauchy],
  'physical_remainder_derivative_errors_over_A':[v.strings() for v in paid_error],
  'spatial_transport_errors':[v.strings() for v in spatial],
  'physical_time_derivative_budgets':[v.strings() for v in budget],
  'total_finite_transport_errors':[v.strings() for v in transport],
  'absolute_twelfth_frequency_moment':moment12.strings(),'max_spatial_residual':str(max_residual)},
 'stationary_certificate':{'whole_cell_physical_normalized_jets':[v.strings() for v in whole],
  'left_Hxx_over_A':left[2].strings(),'right_Hxx_over_A':right[2].strings(),
  'Hxx_candidate_subcells':len(candidates),'Hxx_stationary_offset_band':candidate_band.strings(),
  'Hx_Hxxx_over_A_squared_on_candidate_band':product.strings(),
  'stationary_effective_stiffness_minus_Hxxx_over_Hx':stiffness.strings(),
  'one_unique_Hxx_zero_for_every_time':True,'S1_certified_strictly_and_nonvacuously':True,
  'Hxxx_positive_throughout':True,'Hx_negative_throughout':True},
 'jets_at_frozen_midpoint':[{'real':j[0].strings(),'imaginary':j[1].strings()} for j in jets],
 'subcells':subcells,'leading_amplitude_eliminated_on_Hxx_zero':eliminated,
 'imported_sources':HASHES,
 'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'analytic_inputs':{'Polymath':'https://arxiv.org/html/1904.12438v2#S6.SS3','source_results':'Corollary 6.4 and Proposition 6.6; parent fixed-cutoff symmetric normalization; companion Note20 holomorphic exponential comparison'},
 'python_version':platform.python_version(),'runtime_seconds':str(time.perf_counter()-started),
 'limitations':['Imports the published Polymath A+B-C bounds; the source theorem itself is not formally verified by this script.',
  'The correlated leading correction is proved on a fixed-cutoff patch with |p-1|<=0.01; no uniform relative or Holder stationary-loss theorem is established.',
  'The old coarse interface already separates the first derivative here; this improves stationary-sign resolution, not collision coverage.',
  'No earlier-time predecessor buffer outside the stated rectangle is supplied.',
  'The region was selected by floating-point diagnostics; all reported signs are independently recomputed with outward interval arithmetic.']}

if __name__=='__main__':
 result=enclose()
 if ARGS.record: ARGS.record.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
 print(json.dumps({k:result[k] for k in ['status','stationary_certificate','runtime_seconds']},indent=2))
