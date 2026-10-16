#!/usr/bin/env python3
"""Outward complete theta correction bound across a natural cutoff change.

Imports the published Polymath A+B-C source estimate. A direct logarithmic
comparison bounds the difference between the entering finite term and the
leading correction jump on a complex rectangle. The frozen-cutoff analytic
remainder then has a full-disk bound even when the natural cutoff changes.
No binary floating point is used in bounds or mathematical decisions.
"""
import argparse,hashlib,json,platform,sys,time
from pathlib import Path
from decimal import Decimal
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--record',type=Path)
parser.add_argument('--interval-source-dir',type=Path,
 default=Path(__file__).resolve().parents[2]/'13_microlocal_phase_space'/'numerics')
args=parser.parse_args()
SOURCE=args.interval_source_dir
HASHES={'check_block_current.py':'0cfca37632cfaaea522cce2a9514b81eaf9db0bf6213cd243de0f937679627a2','check_complete_current_rectangle.py':'ac547ff45915d95369afc558f6ee3daa01fb6974ad1569e719dc3f0abcd4c522'}
for n,h in HASHES.items():
 if hashlib.sha256((SOURCE/n).read_bytes()).hexdigest()!=h:
  raise RuntimeError('Retained interval source hash mismatch: '+n)
sys.path.insert(0,str(SOURCE))
from check_block_current import atan_small
from check_complete_current_rectangle import I,pi_interval,absmax,reduced_trig,real_data,factorial

def sqrt(x):return (x.ln()/2).exp()
def imax(x,y):return I(max(x.lo,y.lo),max(x.hi,y.hi))
started=time.perf_counter()
m=22066; pi=pi_interval(); lm=I(m).ln(); t0=1/(2*lm)
center=4*pi*m*m+I('-.1','.1'); r=I('.05')
eps=I(t0.lo); tm=I((t0+I('.00000001')).hi)
xlo=I(center.lo)-r; xhi=I(center.hi)+r; qlo=xlo/(4*pi); qhi=xhi/(4*pi)
assert xlo.lo>=200 and 0<eps.lo<=tm.hi<=Decimal('.5')
assert 0<r.lo<=r.hi<=1
natural_lo=qlo+eps/16; natural_hi=qhi+tm/16
assert (m-1)**2<=natural_lo.lo<m*m<natural_hi.hi<(m+1)**2
Tlo=xlo/2; taulo=Tlo+pi*eps/8; tauhi=xhi/2+pi*tm/8
alo=sqrt(taulo/(2*pi)); ahi=sqrt(tauhi/(2*pi)); arange=I(alo.lo,ahi.hi)
dmax=I(absmax(arange-m)); etamax=I(absmax((arange/m).ln()))
amin=I(min(alo.lo,Decimal(m)))
sigmamax=(1+r)/2
Ddelta=sqrt(sigmamax*sigmamax+(pi*tm/8)**2)
D0=3/(2*taulo); D1=1/(2*Tlo)+3/(2*Tlo*Tlo); Ds=D0+Ddelta*D1
Em=Ddelta*D0+Ddelta*Ddelta*D1/2+tm*(2*(etamax+pi/4)*Ds+Ds*Ds)/4
phase=2*pi*dmax**3/(3*amin)
Lambda=sigmamax*etamax+tm*etamax*etamax/4+phase+Em
relative=(Lambda.exp()-1)*2
# Complete error ledger for reference cutoff m; source natural cutoff may be m-1.
V=xlo/2; S=sqrt(xhi*xhi+(1+r)**2)/2
alpha_minus=qlo.ln()/2-1/(V*V)
Astar=3/(2*V)+sqrt((S/(2*pi)).ln()**2+pi*pi/4)/2
Dstar=3/(2*V*V)+1/(2*V); Lstar=Astar*(1+tm*Dstar/2)
K=(r*Lstar/2).exp(); ks=tm*r/(2*(xlo-6)); EAB=I(0)
for n in range(1,m+1):
 ln=I(n).ln(); d=ln*ln/4-alpha_minus*ln/2
 vn=(-ln/2+imax(eps*d,tm*d)).exp()
 ell=I(max(absmax((qlo/(n*n)).ln()),absmax((qhi/(n*n)).ln())))
 un=((tm*tm*ell*ell/16+I('.626'))/(xlo-I('6.66'))).exp()-1
 EAB+=(1+(ks*lm+r*ln).exp())*vn*un
Z=(-qlo.ln()/4-eps*qlo.ln()**2/16+(3*sqrt(qhi.ln()**2+pi*pi/4)+I('3.58'))/(xlo-I('8.52'))).exp()
BC=I('1.24')*((r*I(3).ln()).exp()+(-r*I(3).ln()).exp())/(I(m-1)-I('.125'))+I('6.92')/(xlo-12)
J=3/(4*taulo)+1/(2*taulo*taulo)+(4+6/taulo)/(4*pi*alo)
W=((tauhi/taulo).ln()*I('1.5')).exp()
match=K*Z*relative; source=K*(EAB+Z*BC); holo=2*K*Z*r*W*J
eta=source+match+holo
p_ref=1-2*(arange-m)
assert Decimal('.99')<p_ref.lo<p_ref.hi<Decimal('1.01')
assert Lambda.hi<Decimal('0.000000001')
assert eta.hi<Decimal('0.0000004')
edge_offsets=-pi*I(eps.lo,tm.hi)/4
assert Decimal('-.1')<edge_offsets.lo<=edge_offsets.hi<Decimal('.1')
# Constant real-center normalization permits physical Cauchy payments directly.
physical_errors=[factorial(j)*eta/(r**j) for j in range(4)]
annihilator_error=eta*(1/r+pi/8)
# Independent direct real-edge evaluation, avoiding huge phase subtraction.
xe=4*pi*m*m-pi*t0/4; taue=2*pi*m*m
ar,ai,_,_,_,_,atanx,lc=real_data(xe,t0,pi)
ratio_log=(1-t0/(16*m*m)).ln()
edge_phase=pi*(m%2)-pi-pi*t0/16+atanx/4-xe*ratio_log/4-xe*lc/8+t0*ai*(ar-lm)/2
_,edge_cos=reduced_trig(edge_phase,pi)
edge_weight=(t0*lm*lm/4-(I('.5')+t0*ar/2)*lm).exp()
edge_wave=2*edge_weight*edge_cos
stable_log=pi.ln()/4+3*I(2).ln()+I('.25')+I('1.5')*taue.ln()-I('1.75')*xe.ln()-I('.875')*lc-xe*atan_small(1/xe,6)/4-t0*pi*pi/64-t0*(ar*ar-ai*ai)/4
ss,cc=reduced_trig(pi/8,pi)
correction_jump=((-1)**(m+1))*stable_log.exp()*(cc+ss/taue)
direct_mismatch=edge_wave-correction_jump
assert absmax(direct_mismatch)<match.hi
record={
 'date':'2026-10-11','status':'PASS','prepared_for':'Edward Baker',
 'model_family':'GPT-6 (Codex)','reasoning_effort':'not exposed; not inferred',
 'acknowledgment':'Substantial LLM assistance; internal analytic and outward arithmetic checks, not independent mathematical validation.',
 'scope':'Complete corrected disk source bound across the natural cutoff 22065 to 22066, with a fixed reference cutoff 22066 and a direct complex logarithmic comparison of the entering finite term with the leading correction jump.',
 'arithmetic':'60-digit directed Decimal; explicit trigonometric remainders; only elapsed time uses binary floating point',
 'analytic_input':{'source':'https://arxiv.org/html/1904.12438v2#S6.SS3','results':'Polymath Corollary 6.4 and Proposition 6.6; companion Note22 direct matching and holomorphic remainder theorem'},
 'normalization':'The analytic error is divided by the constant positive A_t(X) at the real center. Physical derivative payments therefore need no normalizer convolution.',
 'region':{'m':m,'center_definition':'X in 4*pi*m^2+[-0.1,0.1]',
  'center_offsets':['-.1','.1'],'centers':center.strings(),'radius':r.strings(),
  'time':[str(eps.lo),str(tm.hi)],'time_definition':'t in [t0,t0+1e-8], t0=1/(2*log m)',
  'x_enclosing_rectangle':[str(xlo.lo),str(xhi.hi)],
  'a_range':arange.strings(),'p_reference_range':p_ref.strings(),
  'natural_cutoff_possibilities':[m-1,m],
  'cutoff_squared_enclosure':[str(natural_lo.lo),str(natural_hi.hi)],
  'moving_edge_offset_from_4pi_m_squared':edge_offsets.strings(),
  'moving_edge_inside_center_interval_for_every_time':True},
 'bounds':{k:v.strings() for k,v in {
  'd_max':dmax,'eta_log_max':etamax,'delta_max':Ddelta,'D0':D0,'D1':D1,'Ds':Ds,
  'carrier_log_error':Em,'phase_error':phase,'Lambda':Lambda,
  'relative_edge_match_2expm1':relative,'K':K,'E_AB':EAB,'Z':Z,'B_C':BC,
  'source_error':source,'edge_matching_error':match,
  'holomorphic_surrogate_error':holo,'total_corrected_disk_error':eta,
  'annihilator_first_error':annihilator_error}.items()},
 'physical_derivative_errors_over_Acenter':[v.strings() for v in physical_errors],
 'real_edge_crosscheck':{'time':'t0','location':'4*pi*m^2-pi*t0/4',
  'entering_wave_over_A':edge_wave.strings(),
  'correction_jump_over_A':correction_jump.strings(),
  'difference_over_A':direct_mismatch.strings(),
  'enclosed_by_complex_rectangle_matching_bound':True,
  'scope':'Independent finite-term evaluation at one exact edge; the full-disk theorem uses analytic bounds, not this point check.'},
 'limitations':[
  'The published source theorem is imported, not formally verified by this script.',
  'This record verifies the explicit error ledger on one rectangle; the broader cutoff-uniform theorem is proved in the accompanying note.',
  'No positive lower bound for a genuine first jet or stationary product is evaluated here.',
  'The remaining error is absolute; uniform bounded or Holder stationary loss near a vanishing joint first jet remains open.'],
 'dependencies':HASHES,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'python_version':platform.python_version(),'runtime_seconds':str(time.perf_counter()-started)}
if args.record: args.record.write_text(json.dumps(record,indent=2,sort_keys=True)+'\n')
print(json.dumps({k:record[k] for k in ['status','bounds','physical_derivative_errors_over_Acenter','real_edge_crosscheck','runtime_seconds']},indent=2,sort_keys=True))
