#!/usr/bin/env python3
"""Outward genuine-theta stationary-set calibration on the retained N=22066 cell.

Conditional on the complete holomorphic disk input. Physical derivatives of H
include all derivatives of A, where H=AQ. No stationary condition on Q or F
is substituted for stationarity of H. No binary floats enter sign tests.
"""
import argparse
from decimal import Decimal
import hashlib
import importlib.util
import json
from pathlib import Path
import platform
import sys
import time

PARSER=argparse.ArgumentParser(description=__doc__)
PARSER.add_argument('--record',type=Path,help='Write a record only when this explicit path is supplied.')
PARSER.add_argument('--project17-numerics',type=Path,default=Path(__file__).resolve().parent)
PARSER.add_argument('--interval-source-dir',type=Path,default=Path(__file__).resolve().parents[2]/'13_microlocal_phase_space'/'numerics')
ARGS=PARSER.parse_args()
HASHES={
 'check_regular_adjoint_cell.py':'4668bd61defe09d2cac15b210160152c1dd9e81d43906c4a899260d2449d5156',
 'check_block_current.py':'0cfca37632cfaaea522cce2a9514b81eaf9db0bf6213cd243de0f937679627a2',
 'check_complete_current_rectangle.py':'ac547ff45915d95369afc558f6ee3daa01fb6974ad1569e719dc3f0abcd4c522'}
for name,digest in HASHES.items():
 base=ARGS.project17_numerics if name=='check_regular_adjoint_cell.py' else ARGS.interval_source_dir
 if hashlib.sha256((base/name).read_bytes()).hexdigest()!=digest:raise RuntimeError('Retained source hash mismatch: '+name)
# Regenerate, rather than merely trust, the retained outward midpoint jets.
saved_argv=sys.argv
sys.argv=['check_regular_adjoint_cell.py','unused_regular_record.json','--interval-source-dir',str(ARGS.interval_source_dir)]
spec=importlib.util.spec_from_file_location('retained_regular_adjoint',ARGS.project17_numerics/'check_regular_adjoint_cell.py')
regular=importlib.util.module_from_spec(spec)
spec.loader.exec_module(regular)
sys.argv=saved_argv
I,DOWN,UP,absmax=regular.I,regular.DOWN,regular.UP,regular.absmax
factorial,pi_interval,real_data=regular.factorial,regular.pi_interval,regular.real_data


def pad(value,bound):return value+I(bound.copy_negate(),bound)
def interval_abs(value):return I(absmax(value))
def hull(values):return I(min(v.lo for v in values),max(v.hi for v in values))
def symmetric(bound):return I(bound.hi.copy_negate(),bound.hi)
def includes_zero(value):return value.lo<=0<=value.hi

def derivative_envelopes(x,t,ell,ar,ai,U,V):
 # Explicit rational alpha-derivative envelopes, valid since |s|,|s-1|>=x/2.
 alpha=interval_abs(ar)+interval_abs(ai)
 a1=interval_abs(U)+interval_abs(V)
 a2=2/(x*x)+24/(x*x*x)
 a3=8/(x*x*x)+144/(x*x*x*x)
 gx=a1/4+t*(a1*a1+(alpha+ell)*a2)/8
 gxx=a2/8+t*(3*a1*a2+(alpha+ell)*a3)/16
 gxt=(a1*a1+(alpha+ell)*a2)/8
 gxxt=(3*a1*a2+(alpha+ell)*a3)/16
 return gx,gxx,gxt,gxxt,alpha,a1,a2,a3


def enclose():
 start=time.perf_counter()
 calibration=regular.enclose()
 M=22066; degree=12; pi=pi_interval();logM=I(M).ln();t0=1/(2*logM);x0=4*pi*M*M
 tb=I(*calibration['domain']['time']);xb=I(*calibration['domain']['height']);Lb=I(*calibration['domain']['L']);dt=I('.000008')
 hbox=I('.3','.7');middle=I('.5')
 bar,bai,bU,bV,bc,bOmega,*_=real_data(xb,tb,pi)
 # A=exp(Re m_t), so lambda=(log A)_x=Im(alpha*(1+t alpha'/2))/2.
 lam=(bai*(1+tb*bU/2)+bar*tb*bV/2)/2
 gx,gxx,gxt,gxxt,alpha,a1,a2,a3=derivative_envelopes(xb,tb,logM,bar,bai,bU,bV)
 lam1bound=(a1+tb*(a1*a1+alpha*a2)/2)/4
 lam2bound=(a2+tb*(3*a1*a2+alpha*a3)/2)/8
 lam1,lam2=symmetric(lam1bound),symmetric(lam2bound)
 # Model spatial transport is frozen at t0,x0 but its carrier is centered .5.
 ar,ai,U,V,c,Omega,*_=real_data(x0,t0,pi)
 aN=I('.5')+t0*ar/2-t0*logM/2
 wN=(t0*logM*logM/4-(I('.5')+t0*ar/2)*logM).exp()
 xhull=x0+I(0,hbox.hi)
 sar,sai,sU,sV,sc,sOmega,*_=real_data(xhull,t0,pi)
 spatial=[I(0) for _ in range(4)];budget=[I(0) for _ in range(4)]
 maximum_gamma_x=Decimal(0);maximum_gamma_xx=Decimal(0)
 for n in range(1,M+1):
  delta=(I(M)/n).ln();ell=logM-delta;g0=delta/2
  amp=(aN*delta+t0*delta*delta/4).exp();w0=wN*amp
  residual_imag=sOmega-sc*logM+(sc-I('.5'))*delta
  residual=interval_abs(t0*sV*ell/4)+interval_abs(residual_imag)
  growth=(I(hbox.hi)*residual).exp();exp_error=I(0,UP.subtract(growth.hi,Decimal(1)))
  sgx,sgxx,*_=derivative_envelopes(xhull,t0,ell,sar,sai,sU,sV)
  sgamma=g0+residual
  differences=[exp_error,
   g0*exp_error+residual*growth,
   g0*g0*exp_error+((2*g0+residual)*residual+sgx)*growth,
   g0**3*exp_error+((3*g0*g0+3*g0*residual+residual*residual)*residual+3*sgamma*sgx+sgxx)*growth]
  for j in range(4):spatial[j]+=w0*differences[j]
  wb=(tb*ell*ell/4-(I('.5')+tb*bar/2)*ell).exp()
  chi=interval_abs(ell*ell/4-bar*ell/2)+interval_abs(bai*(bar-ell)/2)
  gamma=interval_abs(tb*bV*ell/4)+interval_abs(bOmega-bc*ell)
  gamma_t=interval_abs(bV*ell/4)+interval_abs((bU*(bar-ell)-bai*bV)/4)
  bgx,bgxx,bgxt,bgxxt,*_=derivative_envelopes(xb,tb,ell,bar,bai,bU,bV)
  terms=[chi,
   gamma_t+gamma*chi,
   2*gamma*gamma_t+bgxt+(gamma*gamma+bgx)*chi,
   3*gamma*gamma*gamma_t+3*gamma_t*bgx+3*gamma*bgxt+bgxxt+(gamma**3+3*gamma*bgx+bgxx)*chi]
  for j in range(4):budget[j]+=wb*terms[j]
  maximum_gamma_x=max(maximum_gamma_x,bgx.hi);maximum_gamma_xx=max(maximum_gamma_xx,bgxx.hi)
 transport=[spatial[j]+dt*budget[j] for j in range(4)]
 jets=[I(*j['real']) for j in calibration['jets_at_frozen_midpoint']]
 moment12=I(*calibration['payments']['last_absolute_frequency_moment'])
 eta=5*(-tb*Lb*Lb/16-Lb/4).exp()
 cauchy=[eta*factorial(j)*Lb**j for j in range(4)]
 # H_j/A physical jets, exact triangular normalization dictionary.
 normalizer_coeff=[I(1),lam,lam*lam+lam1,lam**3+3*lam*lam1+lam2]
 physical_error=[cauchy[0],
   cauchy[1]+interval_abs(lam)*cauchy[0],
   cauchy[2]+2*interval_abs(lam)*cauchy[1]+interval_abs(normalizer_coeff[2])*cauchy[0],
   cauchy[3]+3*interval_abs(lam)*cauchy[2]+3*interval_abs(normalizer_coeff[2])*cauchy[1]+interval_abs(normalizer_coeff[3])*cauchy[0]]
 def enclosed_jets(offset):
  f=[];model=[];remainders=[]
  radius=interval_abs(offset)
  for j in range(4):
   value=I(0)
   for k in range(j,degree):value+=jets[k]*offset**(k-j)/factorial(k-j)
   remainder=moment12*radius**(degree-j)/factorial(degree-j)
   remainders.append(remainder)
   model.append(2*value)
   f.append(pad(2*value,(2*(remainder+transport[j])).hi))
  K=[f[0],f[1]+lam*f[0],
     f[2]+2*lam*f[1]+normalizer_coeff[2]*f[0],
     f[3]+3*lam*f[2]+3*normalizer_coeff[2]*f[1]+normalizer_coeff[3]*f[0]]
  Kpaid=[pad(K[j],physical_error[j].hi) for j in range(4)]
  return Kpaid,K,model,remainders
 subcells=[];allK=[[] for _ in range(4)];stationaryHx=[];stationaryHxx=[]
 for k in range(80):
  h=I('.3')+I(k,k+1)/200
  K,Kfinite,model,rems=enclosed_jets(h-middle)
  for j in range(4):allK[j].append(K[j])
  cand1=includes_zero(K[1]);cand2=includes_zero(K[2])
  if cand1:
   stationaryHx.append((h,K));assert K[0].lo>0 and K[2].hi<0 and (K[0]*K[2]).hi<0
  if cand2:
   stationaryHxx.append((h,K));assert (K[1]*K[3]).hi<=0
  subcells.append({'height_offset':h.strings(),'physical_normalized_H_jets':[v.strings() for v in K],
    'Hx_stationary_candidate':cand1,'Hxx_stationary_candidate':cand2,
    'S0_normalized_product':(K[0]*K[2]).strings() if cand1 else None,
    'S1_normalized_product':(K[1]*K[3]).strings() if cand2 else None})
 whole=[hull(values) for values in allK]
 left=enclosed_jets(I('-.2'))[0];right=enclosed_jets(I('.2'))[0]
 assert whole[2].hi<0
 assert left[1].lo>0 and right[1].hi<0
 assert stationaryHx and not stationaryHxx
 critical_band=hull([entry[0] for entry in stationaryHx])
 critical_values=hull([entry[1][0] for entry in stationaryHx])
 critical_curvatures=hull([entry[1][2] for entry in stationaryHx])
 critical_products=hull([entry[1][0]*entry[1][2] for entry in stationaryHx])
 assert critical_values.lo>0 and critical_curvatures.hi<0 and critical_products.hi<0
 return {
 'status':'PASS','date':'2026-10-10','prepared_for':'Edward Baker',
 'model_family':'GPT-6 (Codex)','reasoning_effort':'not exposed to this worker; not inferred',
 'acknowledgment':'Prepared with substantial LLM assistance; internal outward arithmetic replay, not independent mathematical validation.',
 'scope':'Complete stationary-set enclosure on one closed physical rectangle, conditional on imported complete disk input. S0 holds strictly on its nonempty genuine Hx stationary set; S1 is vacuous because genuine Hxx is strictly negative throughout.',
 'arithmetic':'Retained 60-digit outward Decimal; explicit trig/atan remainder; repeated outward integer powers; no binary float in signs',
 'N':M,'number_of_terms':M,'subcell_count':80,'Taylor_degree':11,
 'domain':calibration['domain'],
 'normalizer':{'definition':'H=AQ, A=exp(Re m_t)>0; all observed physical jets are H_j/A',
  'lambda_exact_dictionary':'lambda=Im[alpha*(1+t*alpha_prime/2)]/2',
  'lambda':lam.strings(),'lambda_prime_symmetric_enclosure':lam1.strings(),'lambda_second_symmetric_enclosure':lam2.strings(),
  'physical_jet_dictionary':'K0=Q; K1=Qprime+lambda*Q; K2=Qsecond+2lambda*Qprime+(lambda²+lambda_prime)Q; K3=Qthird+3lambda*Qsecond+3(lambda²+lambda_prime)Qprime+(lambda³+3lambda lambda_prime+lambda_second)Q'},
 'payments':{'eta':eta.strings(),'Cauchy_Q_derivative_errors':[e.strings() for e in cauchy],
  'Cauchy_physical_normalized_derivative_errors':[e.strings() for e in physical_error],
  'spatial_transport_errors':[e.strings() for e in spatial],'physical_time_derivative_budgets':[e.strings() for e in budget],
  'total_finite_transport_errors':[e.strings() for e in transport],
  'absolute_twelfth_frequency_moment':moment12.strings(),
  'maximum_gamma_x_upper':str(maximum_gamma_x),'maximum_gamma_xx_upper':str(maximum_gamma_xx)},
 'complete_stationary_sets':{
  'whole_cell_physical_normalized_jets':[v.strings() for v in whole],
  'left_Hx_over_A':left[1].strings(),'right_Hx_over_A':right[1].strings(),
  'Hx_candidate_subcells':len(stationaryHx),'Hx_stationary_height_band':critical_band.strings(),
  'H_over_A_on_Hx_candidate_band':critical_values.strings(),
  'Hxx_over_A_on_Hx_candidate_band':critical_curvatures.strings(),
  'HHxx_over_A_squared_on_Hx_candidate_band':critical_products.strings(),
  'one_unique_genuine_Hx_zero_for_every_time':True,
  'Hxx_candidate_subcells':len(stationaryHxx),'Hxx_strictly_negative_throughout':True,
  'S0_certified_strictly':True,'S1_certified_vacuously':True},
 'subcells':subcells,
 'imported_sources':HASHES,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'python_version':platform.python_version(),'runtime_seconds':str(time.perf_counter()-start),
 'limitations':[
  'The imported complete holomorphic disk approximation is assumed, not newly proved.',
  'Signs are proved on this rectangle itself; using the stationary-sign criterion to exclude a closed target requires a proved predecessor neighborhood. No earlier-time buffer at the lower time boundary is supplied.',
  'The Hxx stationary set is empty here. This example does not certify a nonvacuous S1 sign, whose third-derivative Cauchy cost is explicitly retained.',
  'This cell was already excluded from joint zeros by earlier paid first-jet methods. No improvement over that coverage or global RH conclusion follows.']}

if __name__=='__main__':
 result=enclose()
 if ARGS.record:ARGS.record.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
 print(json.dumps({'status':result['status'],'stationary_sets':result['complete_stationary_sets'],'runtime_seconds':result['runtime_seconds']},indent=2))
