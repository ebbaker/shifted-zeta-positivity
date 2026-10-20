#!/usr/bin/env python3
"""Frozen one-cell Gaussian cap comparison; source acquisition is inherited."""
from __future__ import annotations
import argparse, hashlib, importlib.util, json, math, platform, signal, sys, time
from fractions import Fraction as F
from pathlib import Path
sys.dont_write_bytecode=True
from flint import arb, ctx
import flint
T0,T1=F(109999,10**6),F(110001,10**6)
X0,X1=F(4005,4),F(2003,2)
S,L=F(1,10**6),F(1,10)
XC,TC=F(1000),F(21,200)
ROUTE=Path('papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/09_expanding_contour_later_collision')
def check(c,m):
 if not c: raise ArithmeticError(m)
def digest(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(p,name):
 spec=importlib.util.spec_from_file_location(name,p); mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod); return mod

def validate(t0,t1,x0,x1,s,L,have_tails=True,global_bounds=(1,1),orders=51):
 check(s>0 and L>0,'positive fixed scale and cutoff required')
 check(t0<=t1 and x0<=x1,'ordered closed parameters required')
 check(F(1,100)<=t0 and t1+s<=F(1,5),'initial/cap time leaves complete domain')
 check(x0-L>=999 and x1+L<=1002,'cap leaves physical source-tail domain')
 check(have_tails and all(v>0 for v in global_bounds),'complete spatial tails and positive global bounds required')
 check(orders>=50,'cached midpoint derivatives through order49 required')

def evaluate_cap(bw,base,setup,bits):
 started=time.monotonic(); ctx.prec=bits; validate(T0,T1,X0,X1,S,L)
 A,rec,interval,poly=bw.A,bw.rec,bw.interval,bw.poly
 cache=setup['setup']; rows=cache['midpoint_jets']
 moments=[base.undyadic(r['midpoint_dyadic']) for r in rows]
 radii=[base.undyadic(r['quadrature_radius_dyadic']) for r in rows]
 check(len(moments)==51 and all(r['j']==j for j,r in enumerate(rows)),'cache derivative orders mismatch')
 M=base.undyadic(cache['common_moment_dyadic'])
 modes,sources,admissibility=bw.tail_bounds(bits)
 dt=interval(T0+S,T1+S)-A(TC); dx=interval(X0-L,X1+L)-A(XC)
 Delta=A(max(abs(T0+S-TC),abs(T1+S-TC)))
 R=A(max(abs(X0-L-XC),abs(X1+L-XC)))
 fac=[math.factorial(j) for j in range(53)]
 rem=(M*(R**25/fac[25]+R.exp()*Delta**13/fac[13])).upper()
 P=[]; errors=[]; payments=[]; physical=[]
 for j in (0,1):
  cs=[poly([(-1)**k*moments[j+l+2*k]/fac[k] for k in range(13)],dt)/fac[l] for l in range(25)]
  image=poly(cs,dx)
  quad=sum((R**l*Delta**k*radii[j+l+2*k]/(fac[l]*fac[k]) for l in range(25) for k in range(13)),arb(0)).upper()
  err=(rem+quad+modes[j]+sources[j]).upper()
  check(err<arb('1e-6'),'predeclared component allowance failed')
  P.append(image); errors.append(err); physical.append(image+arb(0,err))
  payments.append({'j':j,'polynomial_image':rec(image),'taylor_remainder':rec(rem),'propagated_quadrature':rec(quad),'omitted_modes':rec(modes[j]),'retained_source_tail':rec(sources[j]),'total_error':rec(err),'complete_cap_component':rec(physical[-1])})
 acquisition_consumer_seconds=time.monotonic()-started
 consumer_started=time.monotonic()
 z=A(L)/(2*A(S).sqrt()); mass=z.erf(); p=z.erfc()
 norm=arb(1000)**(arb(7)/4)*(-125*arb.pi()).exp()
 check(norm>0 and p>0 and mass>0,'Gaussian mass or normalization not positive')
 raw=(A(S)*base.square(P[1])-base.square(P[0]))*mass
 product_terms=[(2*P[j].abs_upper()*errors[j]+errors[j]**2).upper() for j in (0,1)]
 product=(mass*(product_terms[0]+A(S)*product_terms[1])).upper()
 finite=raw+arb(0,product)
 tail_low=(-p/norm**2).lower(); tail_up=(A(S)*p/norm**2).upper()
 spatial=arb((tail_low+tail_up)/2,(tail_up-tail_low)/2)
 full=finite+spatial
 # Arb uses a compact outward radius. Record any additional endpoint
 # widening when product and asymmetric spatial payments are combined.
 rounding_upper=max(arb(0),(full.upper()-raw.upper()-product-tail_up).upper())
 rounding_lower=max(arb(0),(raw.lower()-product+tail_low-full.lower()).upper())
 U=full.upper(); LD=max(arb(0),-U)
 # Gaussian moments are exact complete-field conservation identities. Entire
 # cap components already include their complete physical source errors.
 moment_tail=(p/norm).upper()
 gm=[v*mass+arb(0,moment_tail) for v in physical]
 Lgm=(gm[0].abs_lower()**2+A(S)*gm[1].abs_lower()**2).lower()
 deficit_seconds=time.monotonic()-consumer_started
 return {'arithmetic_precision_bits':bits,'source_acquisition_precision_bits':setup['actual_precision_bits'],
  'full_cap_time':[str(T0+S),str(T1+S)],'full_cap_space':[str(X0-L),str(X1+L)],
  'R':rec(R),'Delta':rec(Delta),'retained_derivative_majorant':rec(M),'admissibility':admissibility,
  'components':payments,'gaussian_cutoff_z':rec(z),'retained_mass':rec(mass),'omitted_mass':rec(p),'Gstar':rec(norm),
  'raw_finite_cap_deficit_interval':rec(raw),'product_error_terms_unweighted':list(map(rec,product_terms)),
  'total_product_error':rec(product),'finite_cap_with_product_error':rec(finite),
  'spatial_tail_interval':rec(spatial),'spatial_tail_lower':rec(tail_low),'spatial_tail_upper':rec(tail_up),
  'additional_interval_rounding_allowance':{'lower':rec(rounding_lower),'upper':rec(rounding_upper),'scope':'Additional endpoint widening when combining raw finite-cap interval, product payment and true asymmetric spatial-tail endpoints. Arithmetic rounding within each earlier interval is already included there.'},
  'complete_deficit_interval':rec(full),'U_D':rec(U),'L_D':rec(LD),'delta_D':rec(-U),
  'strict_negative_deficit_certified':bool(U<0),
  'structural_interval_loss':{'value_polynomial_image_contains_zero':bool(P[0].contains(0)),'explanation':'The independent whole-cap squared value range has lower endpoint zero. Consequently its raw upper deficit is nonnegative even with all product/source/spatial errors set to zero; eliminating numerical errors alone cannot make this retained interval information certify negativity.'},
  'gaussian_moment_component_intervals':list(map(rec,gm)),'gaussian_moment_tail_each':rec(moment_tail),
  'L_gaussian_moments':rec(Lgm),'energy_minus_gaussian_moment_lower_bound':rec(LD-Lgm),
  'cap_component_consumer_seconds':acquisition_consumer_seconds,'gaussian_consumers_seconds':deficit_seconds,
  'total_seconds':time.monotonic()-started,'new_quadrature_calls':0,'cell_count':1}

def poly_mul(p,q):
 r=[F(0)]*(len(p)+len(q)-1)
 for i,a in enumerate(p):
  for j,b in enumerate(q): r[i+j]+=a*b
 return r

def gaussian_integral(p,s):
 return sum((c*F(math.factorial(n),math.factorial(n//2))*s**(n//2) for n,c in enumerate(p) if n%2==0),F(0))

def controls(bw):
 # Construct the cap by the exact finite heat series from initial jets.
 defs={'quadratic':[0,0,2],'cubic':[0,0,2,6],'multiplicity_four':[0,0,0,0,24],'two_event_quartic_first_event':[0,0,12,0,24]}
 out=[]
 for name,rawjets in defs.items():
  for sign in (-1,1):
   jets=[F(sign*j) for j in rawjets]
   for s in (S,F(1,4),F(1)):
    p=[sum(((-s)**k*jets[l+2*k]/(math.factorial(k)*math.factorial(l)) for k in range((len(jets)-l+1)//2)),F(0)) for l in range(len(jets))]
    dp=[(i+1)*p[i+1] for i in range(len(p)-1)]
    direct=s*gaussian_integral(poly_mul(dp,dp),s)-gaussian_integral(poly_mul(p,p),s)
    expected=sum((F(n-2,2)*(2*s)**n*jets[n]**2/math.factorial(n) for n in range(3,len(jets))),F(0))
    check(direct==expected and direct>=0,'own-polynomial event falsely excluded')
    check(gaussian_integral(p,s)==0 and gaussian_integral(dp,s)==0,'control Gaussian event moment failed')
    out.append({'field':name,'sign':sign,'s':str(s),'direct_exact_D':str(direct),'spectral_exact_D':str(expected),'initial_h2':str(jets[2]),'strict_event_exclusion_refused':True,'ordinary_contour_eligible':bool(jets[2]),'source_error':'0; own exact polynomial data'})
 atom=[]
 for bits in (192,256):
  ctx.prec=bits
  for s in (S,F(1,4),F(1)):
   x=bw.A(s); D=1+x*(2*x).sinh()-(2*x).cosh()
   check(D>0,'bounded positive atomic event not strictly positive')
   atom.append({'bits':bits,'s':str(s),'D':bw.rec(D),'strict_event_exclusion_refused':True,'source':'own exact positive atoms at frequencies zero and one'})
 refusals=[]
 params={'t0':T0,'t1':T1,'x0':X0,'x1':X1,'s':S,'L':L}
 for label,changes in [('missing_tails',{'have_tails':False}),('missing_global_bounds',{'global_bounds':(0,1)}),('zero_scale',{'s':F(0)}),('zero_cutoff',{'L':F(0)}),('outside_time',{'t1':F(1,5)}),('outside_source_tail_domain',{'x1':F(1002)}),('reversed_interval',{'t0':T1+1}),('missing_derivatives',{'orders':49})]:
  args=params|changes
  try: validate(**args)
  except ArithmeticError as e: refusals.append({'case':label,'refused':True,'reason':str(e)})
  else: raise ArithmeticError('required refusal not triggered: '+label)
 return {'exact_polynomial_cases':out,'atomic_cases':atom,'required_refusals':refusals,'multiplicity_four_contour_refused_but_gaussian_applies':True,'screen_scope':'No theta errors assigned to controls; two-event first event is not its all-real threshold.'}

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--repo',type=Path,required=True); ap.add_argument('--output',type=Path,required=True); ap.add_argument('--baseline',type=Path); ap.add_argument('--baseline-wrapper',type=Path,default=Path(__file__).with_name('check_hfce_baseline.py')); ap.add_argument('--contract',type=Path,required=True); a=ap.parse_args()
 started=time.monotonic(); signal.signal(signal.SIGALRM,lambda *args: (_ for _ in ()).throw(TimeoutError('frozen 300 second budget'))); signal.setitimer(signal.ITIMER_REAL,300)
 r={'date':'2026-10-20','timezone':'America/New_York','prepared_for':'Edward Baker','llm_assistance':'substantial; same-model delegated computation','model':'gpt-6-astra','reasoning_effort':'ultra','model_metadata_provenance':'verified by root agent from parent turn metadata','python':platform.python_version(),'flint':flint.__version__,'wrapper_sha256':digest(__file__),'contract_sha256':digest(a.contract),'contract_text':a.contract.read_text(),'global_bound_input':'Parent analytic proof gives w_t(u)<=20 sum_{n>=1} n^4 exp(-3n^2) exp(-3u)<=exp(-3u) for 0<=t<=1/5, by ratio<=16 exp(-9) and 20 exp(-3)+16 exp(-9)<1. Thus M0<=1/3,M1<=1/9. The frozen consumer uses conservative M0=M1=1.'}
 try:
  bwpath=a.repo/ROUTE/'numerics/check_bounded_first_jet_extension.py'; bw=load(bwpath,'bw09_extension')
  r['imported_wrapper']={'path':str(bwpath.relative_to(a.repo)),'sha256':digest(bwpath)}
  base,setup,pins=bw.pin_sources(a.repo); r['source_pins']=pins
  r['source_acquisition_seconds']=setup['setup'].get('seconds'); r['source_acquisition_precision_bits']=setup['actual_precision_bits']; r['source_acquisition_callbacks']=setup['setup'].get('callbacks')
  r['controls']=controls(bw)
  r['arithmetic_replays']=[evaluate_cap(bw,base,setup,bits) for bits in (192,256)]
  if a.baseline:
   check(a.baseline_wrapper is not None,'baseline wrapper path required for source pin')
   br=json.loads(a.baseline.read_text())
   check(br['wrapper_sha256']==digest(a.baseline_wrapper),'baseline wrapper changed since receipt')
   check(br['source_pins']['setup']==pins['setup'],'baseline source cache does not match cap source cache')
   r['baseline_receipt']={'path':str(a.baseline),'sha256':digest(a.baseline),'wrapper_sha256':br['wrapper_sha256'],'source_cache_match':True}
   for z in r['arithmetic_replays']:
    ctx.prec=z['arithmetic_precision_bits']; match=[v for v in br['replays'] if v['bits']==ctx.prec]
    check(len(match)==1,'matching direct baseline precision absent')
    b=match[0]; direct=base.undyadic(b['strongest_complete_lower_F']['lower_dyadic'])
    gm=base.undyadic(z['L_gaussian_moments']['lower_dyadic']); energy=base.undyadic(z['L_D']['lower_dyadic'])
    strongest=max(direct,gm)
    z['same_cache_correlated_direct_lower_F']=bw.rec(direct)
    z['L_direct_strongest']=bw.rec(strongest)
    z['G_E']=bw.rec(energy-strongest)
    z['direct_baseline_consumer']=b['selected_F_consumer']
    z['direct_baseline_already_excludes_box']=bool(direct>0)
    z['new_energy_coverage']=False
   r['comparison_class']='Separately frozen same-data cost comparison; initial direct baseline already excludes the box.'
  r['status']='strict_deficit_on_declared_box' if all(x['strict_negative_deficit_certified'] for x in r['arithmetic_replays']) else 'bounded_failure_no_adaptation'
 except Exception as e: r.update(status='bounded_failure',failure_type=type(e).__name__,failure_message=str(e))
 finally: signal.setitimer(signal.ITIMER_REAL,0)
 r['elapsed_seconds']=time.monotonic()-started; a.output.write_text(json.dumps(r,indent=2)+'\n')
 print(json.dumps({'status':r['status'],'failure':r.get('failure_message'),'seconds':r['elapsed_seconds'],'replays':[{'bits':z['arithmetic_precision_bits'],'D':z['complete_deficit_interval']['display'],'L_D':z['L_D']['display'],'L_GM':z['L_gaussian_moments']['display']} for z in r.get('arithmetic_replays',[])]},indent=2))
 return 0 if r['status']=='strict_deficit_on_declared_box' else 1
if __name__=='__main__': raise SystemExit(main())
