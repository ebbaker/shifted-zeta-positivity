#!/usr/bin/env python3
"""Outward fixed-cutoff physical calibration for a regular adjoint direction.

Uses retained standard-library interval operations, never floating point in
sign tests. Conditional on the project17 complete holomorphic disk interface.
The direction does not divide by either observed coordinate.
"""
import argparse, hashlib, json, platform, sys, time
from decimal import Decimal
from pathlib import Path
PARSER=argparse.ArgumentParser(description=__doc__)
PARSER.add_argument('output',nargs='?',type=Path,
 default=Path(__file__).with_name('REGULAR_ADJOINT_CELL_RECORD_20261010.json'))
PARSER.add_argument('--interval-source-dir',type=Path,
 default=Path(__file__).resolve().parents[2]/'13_microlocal_phase_space'/'numerics',
 help='Directory containing the retained outward interval sources; defaults to sibling program 13.')
ARGS=PARSER.parse_args()
BASE=ARGS.interval_source_dir
HASHES={
 'check_block_current.py':'0cfca37632cfaaea522cce2a9514b81eaf9db0bf6213cd243de0f937679627a2',
 'check_complete_current_rectangle.py':'ac547ff45915d95369afc558f6ee3daa01fb6974ad1569e719dc3f0abcd4c522'
}
for name,digest in HASHES.items():
 if hashlib.sha256((BASE/name).read_bytes()).hexdigest()!=digest:
  raise RuntimeError('Retained source hash mismatch: '+name)
sys.path.insert(0,str(BASE))
from check_complete_current_rectangle import (I,DOWN,UP,PRECISION,atan_small,
 pi_interval,reduced_trig,factorial,absmax,add,rotate,real_data)


def padded_real(value,error):
 return value+I(error.copy_negate(),error)


def enclose():
 started=time.perf_counter()
 M,degree=22066,12
 pi=pi_interval(); logM=I(M).ln(); t0=1/(2*logM); x0=4*pi*M*M
 hbox=I('.3','.7'); middle=I('.5'); dt=I('.000008')
 tbox=t0+I(0,dt.hi); xbox=x0+hbox
 Lbox=(xbox/(4*pi)).ln(); kappabox=tbox*Lbox
 natural=xbox/(4*pi)+tbox/16
 assert 0<tbox.lo<=tbox.hi<Decimal('.05')
 assert kappabox.lo>=1 and kappabox.hi<=Decimal('1.5')
 assert natural.lo>=M*M and natural.hi<(M+1)*(M+1)
 ar,ai,U,V,c,Omega,atanx,lc=real_data(x0,t0,pi)
 aN=I('.5')+t0*ar/2-t0*logM/2
 T=(x0-t0*ai)/2
 wN=(t0*logM*logM/4-(I('.5')+t0*ar/2)*logM).exp()
 carrier=pi*(M%2)-pi+atanx/4-x0*lc/8+t0*ai*(ar-logM)/2
 csine,ccosine=reduced_trig(carrier,pi)
 sar,sai,sU,sV,sc,sOmega,_,_=real_data(x0+I(0,hbox.hi),t0,pi)
 bar,bai,bU,bV,bc,bOmega,_,_=real_data(xbox,tbox,pi)
 moments=[[I(0),I(0)] for _ in range(degree)]
 absolute_last=I(0); spatial_error0=I(0); spatial_error1=I(0)
 time_budget0=I(0); time_budget1=I(0); max_residual=Decimal(0)
 for n in range(1,M+1):
  delta=(I(M)/n).ln(); ell=logM-delta
  amp=(aN*delta+t0*delta*delta/4).exp(); w0=wN*amp
  sine,cosine=reduced_trig(-T*delta-middle*delta/2,pi)
  mq=[amp*cosine,amp*sine]; power=I(1)
  for k in range(degree):
   moments[k]=add(moments[k],[power*mq[0],power*mq[1]])
   power*=delta/2
  absolute_last+=w0*power
  residual_imag=sOmega-sc*logM+(sc-I('.5'))*delta
  residual=I(absmax(t0*sV*ell/4))+I(absmax(residual_imag))
  max_residual=max(max_residual,residual.hi)
  growth=(I(hbox.hi)*residual).exp()
  exp_error=I(0,UP.subtract(growth.hi,Decimal(1)))
  spatial_error0+=w0*exp_error
  spatial_error1+=w0*((delta/2)*exp_error+residual*growth)
  wb=(tbox*ell*ell/4-(I('.5')+tbox*bar/2)*ell).exp()
  chi=I(absmax(ell*ell/4-bar*ell/2))+I(absmax(bai*(bar-ell)/2))
  gamma=I(absmax(tbox*bV*ell/4))+I(absmax(bOmega-bc*ell))
  gamma_t=I(absmax(bV*ell/4))+I(absmax((bU*(bar-ell)-bai*bV)/4))
  time_budget0+=wb*chi; time_budget1+=wb*(gamma_t+gamma*chi)
 jets=[]
 for k,moment in enumerate(moments):
  rotated=rotate(moment,csine,ccosine,wN)
  for _ in range(k%4):rotated=[rotated[1],-rotated[0]]
  jets.append(rotated)
 physical_error0=spatial_error0+dt*time_budget0
 physical_error1=spatial_error1+dt*time_budget1
 slope_factor=I('.15')
 def enclose_offset(offset):
  v=I(0); d=I(0); combined=I(0)
  for k,jet in enumerate(jets):
   factor=offset**k/factorial(k)
   v+=factor*jet[0]
   coeff=jet[0]
   if k<degree-1:
    d+=factor*jets[k+1][0]
    coeff+=slope_factor*jets[k+1][0]
   combined+=factor*coeff
  radius=I(absmax(offset))
  rem0=absolute_last*radius**degree/factorial(degree)
  rem1=absolute_last*radius**(degree-1)/factorial(degree-1)
  err0=(rem0+physical_error0).hi; err1=(rem1+physical_error1).hi
  errcombined=(I(err0)+slope_factor*I(err1)).hi
  return padded_real(v,err0),padded_real(d,err1),padded_real(combined,errcombined)
 allS=[]; allD=[]; allCombined=[]; subcells=[]
 for k in range(40):
  offset=I('-.2')+I(k,k+1)/100
  v,d,z=enclose_offset(offset)
  allS.append(v);allD.append(d);allCombined.append(z)
  subcells.append({'height_offset':(offset+middle).strings(),'Sreal':v.strings(),'Sprime_real':d.strings(),'directional_observation':z.strings()})
 def hull(entries):return I(min(e.lo for e in entries),max(e.hi for e in entries))
 S,D,Vobs=hull(allS),hull(allD),hull(allCombined)
 R=absmax(1-Vobs)
 eta=5*(-tbox*Lbox*Lbox/16-Lbox/4).exp()
 # Compare the joint global direction with paid scalar subdivision.
 def absmin(value):
  return Decimal(0) if value.lo<=0<=value.hi else min(value.lo.copy_abs(),value.hi.copy_abs())
 scalar_counts={'value':0,'derivative_only':0}
 for cell in subcells:
  value=I(*cell['Sreal']);derivative=I(*cell['Sprime_real'])
  if absmin(value)>(eta/2).hi:
   scalar_counts['value']+=1
  else:
   assert absmin(derivative)>(Lbox*eta/2).hi
   scalar_counts['derivative_only']+=1
 assert scalar_counts=={'value':38,'derivative_only':2}
 y2=slope_factor*Lbox; B=I(1); support=y2+B*B/(4*y2)
 assert y2.lo>Decimal('0.5')
 # sqrt is not needed: this conservative norm enclosure is sufficient.
 Y=1+y2
 directional_payment=eta*support/2
 margin=1-I(R)-directional_payment
 euclidean_margin=1-I(R)-eta*Y/2
 assert Vobs.lo>Decimal('0.5701248') and Vobs.hi<Decimal('1.3556811')
 assert R<Decimal('0.4298752') and eta.hi<Decimal('0.00964146')
 assert support.hi<Decimal('3.083857') and margin.lo>Decimal('0.5552583')
 assert S.lo<0<S.hi and D.lo<0<D.hi
 assert Vobs.lo>0 and R<1 and margin.lo>0 and euclidean_margin.lo>0
 leftv,leftd,_=enclose_offset(I('-.2'))
 rightv,rightd,_=enclose_offset(I('.2'))
 assert leftv.hi<0<rightv.lo and rightd.hi<0<leftd.lo
 Qleft=padded_real(2*leftv,eta.hi);Qright=padded_real(2*rightv,eta.hi)
 derivative_payment=(Lbox*eta).hi
 Qprimeleft=padded_real(2*leftd,derivative_payment)
 Qprimeright=padded_real(2*rightd,derivative_payment)
 assert Qleft.hi<0<Qright.lo and Qprimeright.hi<0<Qprimeleft.lo
 record={
 'status':'PASS','scope':'one bounded fixed-cutoff physical cell, conditional on complete disk approximation; regular directional calibration; no shrinking-family growth bound or global coverage',
 'date':'2026-10-10','prepared_for':'Edward Baker','acknowledgment':'Prepared with substantial LLM assistance; internal outward arithmetic replay, not independent mathematical validation.',
 'model_family':'GPT-6 (Codex)','reasoning_effort':'not exposed to this worker; not inferred',
 'arithmetic':'60-digit outward Decimal; explicit atan and trig Taylor remainder; repeated outward integer powers; no binary float in sign tests',
 'N':M,'number_of_terms':M,'Taylor_degree':degree-1,'subcell_count':40,
 'domain':{'definition':'t0=1/(2 log N), x0=4 pi N^2; t in [t0,t0+8e-6], x in [x0+0.3,x0+0.7]',
  'time':tbox.strings(),'height':xbox.strings(),'L':Lbox.strings(),'kappa':kappabox.strings(),'natural_cutoff_squared':natural.strings()},
 'direction':{'y1':'1','y2':'0.15 L','directional_readout':'y dot Cq = Re S + 0.15 Re Sprime','construction':'No division by value, slope, or a common-zero determinant; tree-adjoint telescoping may leave only r=(1-y dot Cq)b at the source and use the imaginary-source anchor.'},
 'separate_global_observations':{'Sreal':S.strings(),'Sprime_real':D.strings(),'both_intersect_zero':True,
  'left_endpoint_Sreal':leftv.strings(),'right_endpoint_Sreal':rightv.strings(),'left_endpoint_Sprime_real':leftd.strings(),'right_endpoint_Sprime_real':rightd.strings(),'both_actual_coordinates_change_sign':True,
  'paid_Q_left_endpoint':Qleft.strings(),'paid_Q_right_endpoint':Qright.strings(),
  'paid_Qprime_left_endpoint':Qprimeleft.strings(),'paid_Qprime_right_endpoint':Qprimeright.strings(),
  'genuine_normalized_value_and_slope_each_change_sign_under_disk_input':True},
 'certificate':{'directional_observation_enclosure':Vobs.strings(),'source_residual_cost_upper':str(R),'eta_upper_enclosure':eta.strings(),'directional_support_upper':str(support.hi),'multiplier_norm_conservative_upper':str(Y.hi),'paid_directional_margin':margin.strings(),'paid_euclidean_margin':euclidean_margin.strings()},
 'payments':{'last_absolute_frequency_moment':absolute_last.strings(),'max_physical_spatial_residual_upper':str(max_residual),'spatial_value_error_upper':str(spatial_error0.hi),'spatial_slope_error_upper':str(spatial_error1.hi),'physical_time_value_budget_upper':str(time_budget0.hi),'physical_time_slope_budget_upper':str(time_budget1.hi),'total_physical_value_error_upper':str(physical_error0.hi),'total_physical_slope_error_upper':str(physical_error1.hi)},
 'jets_at_frozen_midpoint':[{'real':j[0].strings(),'imaginary':j[1].strings()} for j in jets],
 'subcells':subcells,'paid_scalar_subdivision':scalar_counts,'imported_sources':HASHES,
 'python_version':platform.python_version(),'runtime_seconds':str(time.perf_counter()-started),
 'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'limitation':'The global separate value/slope hulls are inconclusive, but the same 40 subcells also exclude joint zeros by separate paid scalar tests (38 by value, 2 by derivative). This does not establish an advantage over subdivision, a useful asymptotic multiplier bound, or the imported disk interface.'}
 return record

if __name__=='__main__':
 out=ARGS.output
 result=enclose();out.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
 print(json.dumps({k:result[k] for k in ['status','N','certificate','runtime_seconds']}))
