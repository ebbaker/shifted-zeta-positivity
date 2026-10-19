#!/usr/bin/env python3
"""Correlated complete-source arithmetic residual on the bounded S03 box.
Prepared for Edward Baker, 18 October 2026, with substantial LLM assistance.
Actual authoring model/effort: gpt-6.1-sol / ultra, same-model internal work.
"""
from __future__ import annotations
import argparse,hashlib,importlib.util,json,math,platform,time
from fractions import Fraction as F
from pathlib import Path
import flint
from flint import arb,acb,acb_series,ctx

def A(v):return arb(v.numerator)/v.denominator if isinstance(v,F) else arb(v)
def out(v):return v.str(38,more=True)
def interval(a,b):
 a,b=A(a),A(b);return arb((a+b)/2,((b-a)/2).upper())
def check(c,msg):
 if not c:raise ArithmeticError(msg)
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def poly(cs,x):
 r=cs[-1]
 for c in reversed(cs[:-1]):r=r*x+c
 return r
def prefix_step(prefix,image,width):
 partial=prefix+interval(0,width)*image
 return prefix+width*image,abs(partial).upper()
def import_path(name,path):
 s=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m

def main():
 p=argparse.ArgumentParser();p.add_argument('--repo',required=True,type=Path);p.add_argument('--setup',required=True,type=Path)
 p.add_argument('--output',required=True,type=Path);p.add_argument('--bits',default=192,type=int)
 p.add_argument('--execution-model',required=True);p.add_argument('--execution-effort',required=True);args=p.parse_args()
 started=time.monotonic();ctx.prec=args.bits;ctx.cap=64
 base=args.repo/'papers/investigations-3/11_arithmetic_collision_rigidity'
 hhpath=base/'numerics/high_height_consumer/high_height_consumer.py'
 s02path=base/'symmetries/02_cutoff_reflection/numerics/check_cutoff_reflection.py'
 setup=json.loads(args.setup.read_text())
 check(setup['source_sha256']==sha(hhpath),'complete evaluator source pin')
 hh=import_path('complete_source',hhpath);hh.validate_setup(setup,args.repo);ev=hh.load_setup(setup)
 ctx.prec=args.bits
 s02record=s02path.with_name('S02_CUTOFF_REFLECTION_192_20261018.json');s02data=json.loads(s02record.read_text())
 check(s02data['script_sha256']==sha(s02path),'S02 retained script hash')
 for rel,pin in s02data['source_sha256'].items():check(sha(args.repo/rel)==pin,'S02 retained analytic source hash '+rel)
 old=import_path('s02_arithmetic',s02path)
 opening_path=base/'symmetries/03_normalized_jet_rotation/numerics/S03_ROTATION_192_20261018.json'
 opening_script=opening_path.with_name('check_normalized_rotation.py');opening=json.loads(opening_path.read_text())
 check(opening['script_sha256']==sha(opening_script),'opening S03 script hash')
 check(opening['inherited_S02_contract']['record_sha256']==sha(s02record),'opening S03 inherited record hash')
 check(opening['inherited_S02_contract']['script_sha256']==sha(s02path),'opening S03 inherited script hash')
 check(opening['closed_cover']['t_cells']==32 and opening['closed_cover']['x_cells']==128 and len(opening['slabs'])==32,'opening S03 matched geometry')
 L=26;K=12;nt=32;nx=128;Rx=A(8);Rt=A(2);tc=A(F(21,200));xc=A(1000);delta=A(F(19,200));pi=arb.pi();ii=acb(0,1)
 lg=A(F(7,4))*xc.log()-pi*xc/8
 def phase(x,t):
  ss=(1-ii*acb(x))/2
  mp=lambda v:old.alpha(v)*(1+t*old.alphap(v)/2)
  mpp=lambda v:old.alphap(v)*(1+t*old.alphap(v)/2)+t*old.alpha(v)*old.alphapp(v)/2
  th=((old.mt(ss,t)-old.mt(1-ss,t))/(2*ii)).real
  w=(-(mp(ss)+mp(1-ss))/4).real
  wp=(ii*(mpp(ss)-mpp(1-ss))/8).real
  a=(-ii*(mp(ss)-mp(1-ss))/4).real
  ax=(-(mpp(ss)+mpp(1-ss))/8).real
  loga=((old.mt(ss,t)+old.mt(1-ss,t))/2).real
  return th,w,wp,a,ax,(lg-loga).exp()
 def stable_J(z,t):
  v=z/2+pi*t/8
  root=(v.log()/2).exp();aa=((v/(2*pi)).log()/2).exp();pp=17-2*aa
  den=2*(pi*pp).cos();check(not (den[0]if isinstance(den,acb_series)else den).contains(0),'complex correction denominator')
  DD,EE,_,_=old.profile(pp)
  return root*(v*DD-EE)
 def hhat(z,t):
  ss=(1-ii*z)/2;total=acb(0)
  for n in range(1,9):
   ell=A(n).log()
   for v in (ss,1-ss):total+=(old.m0(v)-v*ell+t*(old.alpha(v)-ell)**2/4-lg).exp()
  corr=-pi.sqrt()/4*(-pi*z/8-pi*pi*t/64-lg).exp()*stable_J(z,t)
  return total-corr
 # A declared closed rectangular cover contains the entire complex polydisk.
 # Both holomorphic channels are retained on complex cells.
 majorant=A(0);polydisk_cells=0
 for xr in range(4):
  for xi in range(4):
   z=acb(interval(F(992)+4*xr,F(992)+4*(xr+1)),interval(-8+4*xi,-8+4*(xi+1)))
   for tr in range(4):
    for ti in range(4):
     t=acb(interval(F(21,200)-2+tr,F(21,200)-2+tr+1),interval(-2+ti,-2+ti+1))
     vv=hhat(z,t);check(vv.is_finite(),'finite polydisk majorant')
     majorant=max(majorant,abs(vv).upper());polydisk_cells+=1
 # Mixed coefficients of the physical arithmetic expression, divided by G*.
 zs=acb_series([acb(xc),acb(1)],L+K+1);ss=(1-ii*zs)/2
 hhat_cs=[[acb(0)for _ in range(K+1)]for _ in range(L+1)]
 for n in range(1,9):
  ell=A(n).log()
  for v in (ss,1-ss):
   cn=(old.alpha(v)-ell)**2/4
   g=(old.m0(v)-v*ell+tc*cn-lg).exp();power=acb_series([1])
   for k in range(K+1):
    vv=g*power/math.factorial(k)
    for l in range(L+1):hhat_cs[l][k]+=vv[l]
    power*=cn
 corr=-pi.sqrt()/4*(-pi*zs/8-pi*pi*tc/64-lg).exp()*old.J(zs,tc,8)[0]
 for l in range(L+1):
  for k in range(K+1):
   ck=sum((math.comb(k,j)*(pi/4)**j*(pi*pi/64)**(k-j)*math.factorial(l+j)/math.factorial(l)*corr[l+j] for j in range(k+1)),acb(0))/math.factorial(k)
   hhat_cs[l][k]-=ck
 coeff=[];hhat_real=[];quadmax=A(0)
 for l in range(L+1):
  row=[];hrow=[]
  for k in range(K+1):
   check(hhat_cs[l][k].imag.contains(0),'physical arithmetic mixed coefficient real')
   j=l+2*k
   hv=arb(ev.values[j],ev.radii[j])*(-1)**k/(math.factorial(l)*math.factorial(k))
   row.append(hv-hhat_cs[l][k].real);hrow.append(hhat_cs[l][k].real)
  coeff.append(row);hhat_real.append(hrow)
 # Complete-source real derivative remainder for the SAME differentiated P26,12.
 source_taylor=[];source_mode=[];source_tail=[];arithmetic_tail=[]
 q=1/Rx;v=delta/Rt;n=L+1
 S=[q**n/(1-q),q**(n-1)*(n/(1-q)+q/(1-q)**2),
    q**(n-2)*(n*(n-1)/(1-q)+2*n*q/(1-q)**2+2*q*q/(1-q)**3)]
 for j in range(3):
  source_taylor.append((ev.majorant*(A(1)/math.factorial(L+1-j)+A(1).exp()*delta**(K+1)/math.factorial(K+1))).upper())
  source_mode.append(ev.uniform_tails[0][j]);source_tail.append(ev.uniform_tails[1][j])
  arithmetic_tail.append((majorant/Rx**j/(1-v)*(S[j]+v**(K+1)*math.factorial(j)/(1-q)**(j+1))).upper())
 errors=[(source_taylor[j]+source_mode[j]+source_tail[j]+arithmetic_tail[j]).upper()for j in range(3)]
 # Physical quadrature is already in the shared coefficient balls. Print a
 # redundant independent supremum to disclose its scale, without adding twice.
 quad=[]
 for j in range(3):
  quad.append(sum((ev.radii[l+2*k]*delta**k/math.factorial(k)/math.factorial(l-j)for l in range(j,L+1)for k in range(K+1)),A(0)).upper())
 # Select exact nominal coefficient midpoints and combine the anchor
 # powers using Fraction, so exponent gaps cannot round away a term.
 def exact_fraction(value):
  check(value.is_exact(),'nominal dyadic coefficient must be exact')
  man,exponent=value.man_exp();man,exponent=int(man),int(exponent)
  return F(man*(1<<exponent),1)if exponent>=0 else F(man,1<<(-exponent))
 def exact_dyadic(value):
  numerator,denominator=value.numerator,value.denominator
  check(denominator>0 and denominator&(denominator-1)==0,'nominal coefficient is not dyadic')
  if numerator==0:return {'mantissa':'0','exponent':0}
  trailing=(abs(numerator)&-abs(numerator)).bit_length()-1
  return {'mantissa':str(numerator>>trailing),'exponent':trailing-(denominator.bit_length()-1)}
 nominal_anchor_value=[];nominal_anchor_dx=[]
 for k in range(K+1):
  value=sum(((-1)**l*exact_fraction(coeff[l][k].mid())for l in range(L+1)),F(0))
  dxvalue=sum((l*(-1)**(l-1)*exact_fraction(coeff[l][k].mid())for l in range(1,L+1)),F(0))
  nominal_anchor_value.append(exact_dyadic(value));nominal_anchor_dx.append(exact_dyadic(dxvalue))
 def coeff_at(table,dt):return [poly(row,dt)for row in table]
 def images(cs,x):
  return [poly(cs,x),poly([(l+1)*cs[l+1]for l in range(L)],x),poly([(l+2)*(l+1)*cs[l+2]for l in range(L-1)],x)]
 def residual(cs,x,t):
  th,w,wp,a,ax,C=phase(x,t);check(w<0,'decreasing prescribed phase')
  dx=x-xc;d0=1+(a*a-ax)/(w*w)+wp*a/(w**3);d1=-2*a/(w*w)-wp/(w**3);d2=1/(w*w)
  rrcoeff=[d0*cs[l]+(d1*(l+1)*cs[l+1]if l<L else 0)+(d2*(l+2)*(l+1)*cs[l+2]if l<L-1 else 0)for l in range(L+1)]
  R=C*poly(rrcoeff,dx)
  Re=(C.upper()*(abs(d0).upper()*errors[0]+abs(d1).upper()*errors[1]+abs(d2).upper()*errors[2])).upper()
  vals=images(cs,dx);rv=C*vals[0];rx=C*(vals[1]-a*vals[0])
  e0=C.upper()*errors[0];e1=C.upper()*(errors[1]+abs(a).upper()*errors[0])
  eps=(abs(acb(rv,-rx/w)).upper()+(e0*e0+(e1/abs(w).lower())**2).sqrt()).upper()
  return th,w,wp,a,ax,C,R,Re,rv,rx,eps
 coefficient_uncertainty=[sum((c.rad().upper()*delta**k for k,c in enumerate(row)),A(0)).upper()for row in coeff]
 nominal_anchor_error0=sum(coefficient_uncertainty,A(0))+errors[0]
 nominal_anchor_error1=sum((l*coefficient_uncertainty[l]for l in range(1,L+1)),A(0))+errors[1]
 max_nominal_anchor_error=A(0)
 max_I=A(0);max_poly_I=A(0);max_l1=A(0);max_poly_l1=A(0);max_R=A(0);max_Re=A(0)
 max_eps=A(0);matched=A(0);min_direct=A(100);anchor_physical=A(100);slabs=[]
 transport_min=A(100);independent_transport_min=A(100)
 for it in range(nt):
  ta=F(1,100)+F(19,100)*it/nt;tb=F(1,100)+F(19,100)*(it+1)/nt;t=interval(ta,tb);dt=t-tc
  cs=coeff_at(coeff,dt);fs=coeff_at(hhat_real,dt)
  anchor=residual(cs,A(999),t);epsa=anchor[-1]
  th,w,wp,a,ax,C,*_=anchor
  nominal_anchor_error=(C.upper()*(nominal_anchor_error0**2+((nominal_anchor_error1+abs(a).upper()*nominal_anchor_error0)/abs(w).lower())**2).sqrt()).upper()
  max_nominal_anchor_error=max(max_nominal_anchor_error,nominal_anchor_error)
  fva=images(fs,-A(1));Wfa=acb(C*fva[0],-C*(fva[1]-a*fva[0])/w)
  efhat=(C.upper()**2*(arithmetic_tail[0]**2+((arithmetic_tail[1]+abs(a).upper()*arithmetic_tail[0])/abs(w).lower())**2)).sqrt()
  anchor_lower=(abs(Wfa).lower()-efhat-epsa).lower();anchor_physical=min(anchor_physical,anchor_lower)
  prefix=acb(0);poly_prefix=acb(0);l1=A(0);poly_l1=A(0);slab_I=A(0);slab_poly_I=A(0);slab_eps=A(0);slab_direct=A(100)
  for ix in range(nx):
   xa=F(999)+F(2)*ix/nx;xb=F(999)+F(2)*(ix+1)/nx;x=interval(xa,xb);h=A(xb-xa)
   th,w,wp,a,ax,C,R,Re,rv,rx,eps=residual(cs,x,t)
   completeR=R+arb(0,Re);factor=(-ii*th).exp()*w
   f=factor*completeR;fp=factor*R
   prefix,bound=prefix_step(prefix,f,h);poly_prefix,poly_bound=prefix_step(poly_prefix,fp,h)
   slab_I=max(slab_I,bound);slab_poly_I=max(slab_poly_I,poly_bound)
   l1+=h*abs(f).upper();poly_l1+=h*abs(fp).upper()
   slab_eps=max(slab_eps,eps);max_R=max(max_R,abs(completeR).upper());max_Re=max(max_Re,Re)
   fv=images(fs,x-xc);Wf=acb(C*fv[0],-C*(fv[1]-a*fv[0])/w)
   fe=(C.upper()**2*(arithmetic_tail[0]**2+((arithmetic_tail[1]+abs(a).upper()*arithmetic_tail[0])/abs(w).lower())**2)).sqrt()
   slab_direct=min(slab_direct,(abs(Wf).lower()-fe-eps).lower())
  max_I=max(max_I,slab_I);max_poly_I=max(max_poly_I,slab_poly_I)
  max_l1=max(max_l1,l1.upper());max_poly_l1=max(max_poly_l1,poly_l1.upper());max_eps=max(max_eps,slab_eps)
  matched=max(matched,(epsa+slab_eps).upper());min_direct=min(min_direct,slab_direct)
  oldslab=opening['slabs'][it];check(oldslab['t_index']==it,'opening time slab order')
  gap=A(oldslab['anchor_minus_signed_integral_lower']).lower()
  transport_margin=(gap-epsa-slab_I).lower()
  independent_transport_margin=(gap-2*epsa-slab_eps).lower()
  transport_min=min(transport_min,transport_margin);independent_transport_min=min(independent_transport_min,independent_transport_margin)
  slabs.append({'t':[str(ta),str(tb)],'anchor_residual_jet_radius_upper':out(epsa),
   'full_box_residual_jet_radius_upper':out(slab_eps),'matched_independent_endpoint_integral_upper':out(epsa+slab_eps),
   'correlated_signed_prefix_integral_upper':out(slab_I),'polynomial_signed_prefix_integral_upper':out(slab_poly_I),
   'correlated_L1_integral_upper':out(l1.upper()),'direct_complete_first_jet_radius_lower':out(slab_direct),
   'complete_source_anchor_radius_lower':out(anchor_lower),'nominal_oscillator_anchor_uncertainty_upper':out(nominal_anchor_error),
   'correlated_transport_radius_lower':out(transport_margin),'same_source_independent_transport_radius_lower':out(independent_transport_margin)})
 check(max_I<matched,'correlated increment fails fair matched independent-endpoint gate')
 check(max_I<A('.01'),'predeclared increment .01 gate')
 check(min_direct>0,'fair direct comparison lost')
 check(transport_min>0 and independent_transport_min>0,'matched paid transport consumer')
 # Exact-point complete residual and defect consistency, including every tail.
 cs0=coeff_at(coeff,A(0));r0=residual(cs0,xc,tc)
 e0=r0[5].upper()*errors[0];e1=r0[5].upper()*(errors[1]+abs(r0[3]).upper()*errors[0])
 exactpoint={'r_polynomial':out(r0[8]),'r_x_polynomial':out(r0[9]),
  'r_complete':out(r0[8]+arb(0,e0)),'r_x_complete':out(r0[9]+arb(0,e1)),
  'R_polynomial':out(r0[6]),'R_error_upper':out(r0[7]),'R_complete':out(r0[6]+arb(0,r0[7])),
  'residual_jet_radius_upper':out(r0[-1])}
 # Check physical coefficient identities against the original exact S02 jet.
 zz=acb(xc);norm=(lg).exp();Fhat=old.series_approximation(zz,tc,True)
 fs0=coeff_at(hhat_real,A(0));th,w,wp,a,ax,C=phase(xc,tc)
 fq=[C*fs0[0],C*(fs0[1]-a*fs0[0]),C*(2*fs0[2]-2*a*fs0[1]+(a*a-ax)*fs0[0])]
 cross=[]
 for j in range(3):
  diff=fq[j]-math.factorial(j)*Fhat[j].real;check(diff.contains(0),'complete arithmetic mixed coefficient order '+str(j))
  cross.append({'j':j,'difference':out(diff),'contains_zero':True})
 # An off-center check exercises all mixed time coefficients and their
 # independent polydisk remainder, unlike the k=0 midpoint normalization.
 off_t=A(F(1,5));off_x=A(1001)
 exact_off=hhat(acb_series([acb(off_x),acb(1)],3),off_t)
 off_image=images(coeff_at(hhat_real,off_t-tc),off_x-xc);off_cross=[]
 for j in range(3):
  discrepancy=off_image[j]-math.factorial(j)*exact_off[j].real
  check(abs(discrepancy)<arithmetic_tail[j],'off-center mixed arithmetic polynomial order '+str(j))
  off_cross.append({'j':j,'discrepancy':out(discrepancy),'paid_remainder':out(arithmetic_tail[j]),'passes':True})
 # Changed consumers must use the same interval-prefix routine and fail
 # strict preservation on a genuine collision; theta-specific tails do not
 # enter these exact controls.
 controls={}
 pref=acb(0);control_bound=A(0)
 for j in range(32):
  x=interval(F(-1)+F(j,32),F(-1)+F(j+1,32));image=(-ii*x).exp()*(x*x+2)
  pref,bound=prefix_step(pref,image,A(F(1,32)));control_bound=max(control_bound,bound)
 check(control_bound>=A(5).sqrt(),'polynomial collision control hidden by prefix routine')
 controls['heat_polynomial_collision']={'H':'x^2-2(t-t_c)','time':'t_c','f':'2cos(x)','theta':'x','anchor_x':'-1','event_x':'0',
  'residual_defect':'x^2+2','exact_integral_modulus_at_event':out(A(5).sqrt()),
  'interval_prefix_bound':out(control_bound),'strict_anchor_preservation_margin_upper':out(A(5).sqrt()-control_bound),
  'strict_preservation_fails':True}
 pref=acb(0);osc_bound=A(0)
 for j in range(32):pref,bound=prefix_step(pref,acb(0),A(F(1,32)));osc_bound=max(osc_bound,bound)
 check(osc_bound==0,'oscillator residual exact zero defect')
 controls['oscillator_residual']={'r':'c cos(theta)','defect':'0 exactly','interval_prefix_bound':out(osc_bound)}
 pref=acb(0);constant_bound=A(0)
 for j in range(32):
  x=interval(pi*j/32,pi*(j+1)/32);pref,bound=prefix_step(pref,(-ii*x).exp(),pi/32);constant_bound=max(constant_bound,bound)
 check(constant_bound>=2,'constant residual increment control')
 controls['constant_residual']={'r':'1','theta':'x','phase_interval':['0','pi'],'exact_integral_modulus':'2','interval_prefix_bound':out(constant_bound)}
 result={'date' :'2026-10-18','timezone':'America/New_York','prepared_for':'Edward Baker','actual_model':args.execution_model,'actual_effort':args.execution_effort,
  'llm_assistance':'substantial; same-model parallel derivation and numerical internal review',
  'python':platform.python_version(),'python_flint':flint.__version__,'precision_bits':args.bits,
  'domain':{'t':['1/100','1/5'],'x':['999','1001'],'anchor_x':'999'},
  'shared_model':{'physical_center':['21/200','1000'],'normalization':'G*=1000^(7/4) exp(-125 pi), fixed before differentiation',
   'spatial_degree':L,'time_degree':K,'retained_source_midpoint_orders':[0,50],'moment_order':52,
   'residual_coefficients':'delta_lk=(-1)^k midpoint_H^(l+2k)/(l! k!)-corrected_arithmetic_physical_mixed_coefficient',
   'quadrature_handling':'nominal signed coefficients are combined before bounds; midpoint-radius uncertainty is enclosed conservatively in coefficient balls; repeated Arb objects do not retain exact covariance; independent displayed quadrature envelope is diagnostic and not added twice',
   'correction_time_identity':'C_t=(pi/4) C_x+(pi^2/64)C',
   'complete_residual_defect':'C*[d0 delta+d1 delta_x+d2 delta_xx], combined at coefficient level before interval evaluation'},
  'closed_cover':{'time_cells':nt,'space_cells':nx,'total_real_cells':nt*nx,'quadrature':'signed complex interval range integral, including all prefixes and partial last cells'},
  'arithmetic_polydisk':{'Rx':'8','Rt':'2','center':['1000','21/200'],'closed_rectangular_cells':polydisk_cells,
   'Hhat_over_Gstar_majorant_upper':out(majorant),'both_holomorphic_channels_retained':True,'correction_denominator_excludes_zero_on_cover':True},
  'physical_error_ledger':{'complete_source_Taylor_remainder_orders_0_2':[out(v)for v in source_taylor],
   'complete_source_omitted_modes_orders_0_2':[out(v)for v in source_mode],
   'complete_source_retained_U_tails_orders_0_2':[out(v)for v in source_tail],
   'shared_coefficient_quadrature_sup_diagnostic_orders_0_2':[out(v)for v in quad],
   'arithmetic_rectangular_Taylor_tail_orders_0_2':[out(v)for v in arithmetic_tail],
   'total_extra_physical_residual_error_orders_0_2':[out(v)for v in errors],
   'normalized_defect_added_error_upper':out(max_Re)},
  'comparison':{'old_S02_independent_joint_endpoint_budget':'0.82746927949148930148645416822069171438',
   'matched_source_informed_independent_endpoint_budget_upper':out(matched),'source_informed_residual_jet_radius_upper':out(max_eps),
   'correlated_complete_signed_prefix_integral_upper':out(max_I),'correlated_polynomial_only_signed_prefix_integral_upper':out(max_poly_I),
   'correlated_complete_L1_integral_upper':out(max_l1),'correlated_polynomial_only_L1_integral_upper':out(max_poly_l1),
   'complete_residual_defect_abs_upper':out(max_R),'correlated_over_matched_independent':out(max_I/matched),
   'complete_source_anchor_radius_lower':out(anchor_physical),'fair_direct_complete_jet_radius_lower':out(min_direct),
   'correlated_paid_transport_radius_lower':out(transport_min),
   'same_source_independent_paid_transport_radius_lower':out(independent_transport_min),
   'old_joint_disk_transport_radius_lower':opening['transport']['joint_disk_endpoint_budget_lower_bound'],
   'paid_transport_passes':True,'same_source_independent_paid_transport_passes':True,
   'direct_radius_exceeds_correlated_transport_radius':bool(min_direct>transport_min),
   'strict_smaller_than_matched_independent_endpoints':True,'strict_increment_below_0_01':True},
  'calibrated_oscillator':{'nominal_physical_anchor_time_coefficients':{'time_center':'21/200','anchor_x':'999','powers':'ascending powers of t-21/200',
   'physical_delta_over_Gstar':nominal_anchor_value,'physical_delta_x_over_Gstar':nominal_anchor_dx,
   'construction':'select exact midpoints of every shared physical residual coefficient, then sum the x=-1 powers with exact rational arithmetic',
   'normalization':'r_nom=C*P_nom, r_x_nom=C*(P_x_nom-a*P_nom), with C=Gstar/A and a=partial_x log A'},
   'nominal_anchor':'real midpoint coefficient polynomial delta_mid(t,999), normalized by exact C(t,999); derivative normalized by prescribed omega(999)',
   'definition':'g=r_nominal_anchor*cos(theta-theta_anchor)+(r_x_nominal_anchor/omega_anchor)*sin(theta-theta_anchor)',
   'anchor_jet_uncertainty_upper':out(max_nominal_anchor_error),
   'uniform_phase_scaled_jet_error_for_H_over_A_minus_Fhat_minus_g_upper':out(max_nominal_anchor_error+max_I),
   'scope':'finite box only; anchor calibration is computed from the same validated complete-source reference'},
  'controls':controls,
  'midpoint_residual':exactpoint,'arithmetic_mixed_coefficient_crosschecks':cross,'off_center_arithmetic_crosscheck':{'t':'1/5','x':'1001','orders':off_cross},'slabs':slabs,
  'source_pins':{'complete_setup':{'path':str(args.setup),'sha256':sha(args.setup),'precision_bits':setup['bits'],'setup_seconds':setup['setup']['seconds'],'setup_callbacks':setup['setup']['callbacks']},
   'complete_source_code':{'path':str(hhpath.relative_to(args.repo)),'sha256':sha(hhpath)},
   'arithmetic_source_code':{'path':str(s02path.relative_to(args.repo)),'sha256':sha(s02path),'retained_record_sha256':sha(s02record),'retained_source_pins_validated':True},
   'complete_setup_analytic_pins':setup['source_pins'],'setup_validated_against_current_repository':True,
   'opening_S03_192_record':{'path':str(opening_path.relative_to(args.repo)),'sha256':sha(opening_path),'script_sha256':sha(opening_script),'inherited_S02_pins_validated':True}},
  'script_sha256':sha(__file__),'seconds':time.monotonic()-started,
  'status':'PASS: finite correlated residual increment is strictly smaller than matched source-informed independent endpoints',
  'limitations':['Fixed real box only; no new region or global arithmetic bound.',
   'The complete-source cache is an external input and must pass current source validation; regenerate it if unavailable or stale.',
   'This estimates the complete arithmetic residual defect by its signed shared coefficients; the L1 alternative diagnoses whether integration cancellation adds a gain.',
   'Same-model internal evidence, no independent human review or performance claim.']}
 args.output.write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps({'status':result['status'],'majorant':out(majorant),'signed_integral':out(max_I),'L1':out(max_l1),'matched_independent':out(matched),'direct_lower':out(min_direct),'seconds':result['seconds']}))
if __name__=='__main__':main()
