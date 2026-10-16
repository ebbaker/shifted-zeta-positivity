#!/usr/bin/env python3
"""Complete-theta boundary winding pilot (15 October 2026).

Prepared for Edward Baker with substantial LLM assistance. Model and effort
are not independently recorded in this delegated process and are not inferred.
Requires python-flint >=0.9.0. Source integrals, tails, Taylor remainder and
segment homotopies are validated by Arb; polygon winding uses exact Fractions.
No files other than the explicitly requested receipt are modified.
"""
from __future__ import annotations
import argparse,hashlib,json,math,platform,time
from fractions import Fraction as F
from pathlib import Path
import flint
from flint import arb,acb,ctx

def main():
 p=argparse.ArgumentParser(description=__doc__)
 p.add_argument('--output',type=Path); p.add_argument('--bits',type=int,default=160)
 a=p.parse_args(); ctx.prec=a.bits; start=time.monotonic(); checks=[]
 def check(label,v):
  if not v: raise AssertionError(label)
  checks.append(label)
 def A(x): return arb(x.numerator)/x.denominator if isinstance(x,F) else arb(x)
 def interval(lo,hi): return arb(A((lo+hi)/2),A((hi-lo)/2))
 def rec(v): return v.str(32,more=True)
 pi=arb.pi(); N=4; L=50; K=12; JMAX=L+2*K+1; MOMAX=JMAX+2
 tlo,thi,xlo,xhi=map(F,['0.01','0.20','25','45'])
 tc=(tlo+thi)/2; xc=(xlo+xhi)/2; T=A(thi); DT=A((thi-tlo)/2); DX=A((xhi-xlo)/2)
 check('positive_time_and_time_upper_bound',A(tlo)>0 and T<=arb(1)/4)
 # phi_n=(p_n''-p_n)/8, p_n=e^(u-a exp(4u)), a=pi*n^2.
 # Therefore int_0^infty phi_n <= beta_n/8, beta_n=(4a-1)e^-a.
 # On [0,1], e^(t u^2)u^j <= e^T. For n>=N+1, beta_n<=4pi n^2 e^-pi n^2,
 # and successive upper-bound terms have ratio <=4exp[-pi(2N+3)].
 mode_ratio=4*(-pi*(2*N+3)).exp()
 beta_tail=4*pi*(N+1)**2*(-pi*(N+1)**2).exp()/(1-mode_ratio)
 mode_tail=T.exp()*beta_tail/8
 # For u>=1 and j<=MOMAX, u^j<=exp[j(u-1)] and phi_n<=2a^2 exp(9u-ae^(4u)).
 # The logarithmic envelope g has g''=2T-16a e^(4u)<0, so its tangent at 1
 # gives integral <= 2a^2 exp[T+9-ae^4]/[4ae^4-9-j-2T].
 # For n>=1 these bounds have successive ratio <=16exp[-3pi e^4].
 e4=arb(4).exp(); source_ratio=16*(-3*pi*e4).exp()
 source_denom=4*pi*e4-9-MOMAX-2*T
 check('source_tail_tangent_is_decaying',source_denom>0 and 2*T<16*pi*e4)
 source_tail=2*pi*pi*(T+9-pi*e4).exp()/source_denom/(1-source_ratio)
 check('mode_and_source_geometric_ratios_below_one',mode_ratio<1 and source_ratio<1)
 jet_tail=mode_tail+source_tail
 betas=sum(((4*pi*n*n-1)*(-pi*n*n).exp() for n in range(1,N+1)),arb(0))
 M=T.exp()*(betas+beta_tail)/8+source_tail
 # First truncate the real x Taylor expansion at the actual t (trigonometric
 # remainder bound M DX^(L+1)/(L+1)!), then time-expand each retained derivative.
 # All required absolute moments, through MOMAX, are <=M by the preceding split.
 taylor_error=M*(DX**(L+1)/math.factorial(L+1)+DX.exp()*DT**(K+1)/math.factorial(K+1))
 integral_start=time.monotonic(); jets=[]
 for j in range(JMAX+1):
  def ff(u,analytic):
   q=(4*u).exp()
   phi=sum(((2*(pi*n*n)**2*q*q-3*pi*n*n*q)*(-pi*n*n*q).exp() for n in range(1,N+1)),acb(0))
   phase=A(xc)*u
   tr=(phase.cos(),-phase.sin(),-phase.cos(),phase.sin())[j%4]
   return (A(tc)*u*u+u).exp()*phi*u**j*tr
  z=acb.integral(ff,0,1,abs_tol=arb('1e-35'),rel_tol=arb('1e-28'),eval_limit=200000,depth_limit=30)
  check('finite_real_midpoint_integral_'+str(j),z.is_finite() and z.imag.contains(0))
  jets.append(z.real+arb(0,jet_tail))
 integral_elapsed=time.monotonic()-integral_start
 coeff_cache={}; evaluations=0
 def coefficients(t0,t1,j):
  key=(t0,t1,j)
  if key not in coeff_cache:
   dt=interval(t0,t1)-A(tc); c=[]
   for l in range(L+1):
    r=jets[l+2*K+j]/math.factorial(K)
    for k in range(K-1,-1,-1): r=-dt*r+jets[l+2*k+j]/math.factorial(k)
    c.append(r/math.factorial(l))
   coeff_cache[key]=c
  return coeff_cache[key]
 def enclose(t0,t1,x0,x1):
  nonlocal evaluations
  evaluations+=1; dx=interval(x0,x1)-A(xc); out=[]
  for j in [0,1]:
   if t0==t1:
    c=coefficients(t0,t1,j); r=c[-1]
    for z in reversed(c[:-1]): r=r*dx+z
   else:
    dt=interval(t0,t1)-A(tc); c=[]
    for k in range(K+1):
     z=jets[L+2*k+j]/math.factorial(L)
     for l in range(L-1,-1,-1): z=z*dx+jets[l+2*k+j]/math.factorial(l)
     c.append(z/math.factorial(k))
    r=c[-1]
    for z in reversed(c[:-1]): r=-dt*r+z
   out.append(r+arb(0,taylor_error))
  return out
 def separator(v):
  choices=[(z.abs_lower(),j,1 if z>0 else -1) for j,z in enumerate(v) if z>0 or z<0]
  return max(choices,key=lambda q:float(q[0])) if choices else None
 boundary=[]; rejected=0; max_depth=0
 def edge(q0,q1,depth=0):
  nonlocal rejected,max_depth
  max_depth=max(max_depth,depth)
  v=enclose(min(q0[0],q1[0]),max(q0[0],q1[0]),min(q0[1],q1[1]),max(q0[1],q1[1]))
  s=separator(v)
  if s:
   boundary.append((q0,q1,s)); return
  rejected+=1
  if depth>=30: raise RuntimeError('boundary refinement limit')
  qm=tuple((u+v)/2 for u,v in zip(q0,q1)); edge(q0,qm,depth+1); edge(qm,q1,depth+1)
 boundary_start=time.monotonic(); before=evaluations
 # Positive orientation for dt wedge dx: bottom x=xlo to the right in t,
 # then right t=thi upward in x, top back in t, left back in x.
 corners=[(tlo,xlo),(thi,xlo),(thi,xhi),(tlo,xhi),(tlo,xlo)]
 for q0,q1 in zip(corners,corners[1:]): edge(q0,q1)
 segment_evaluations=evaluations-before
 polygon=[]; endpoint_values=[]
 for q0,q1,s in boundary:
  v=enclose(q0[0],q0[0],q0[1],q0[1]); endpoint_values.append(v)
  polygon.append(tuple(F(float(z.mid())) for z in v))
 for i,(q0,q1,s) in enumerate(boundary):
  margin,j,sign=s
  check('polygon_and_true_edge_share_strict_halfplane_'+str(i),sign*polygon[i][j]>0 and sign*polygon[(i+1)%len(polygon)][j]>0)
 # Signed crossings of the positive H ray. Upward crossing contributes +1.
 winding=0; crossings=[]
 for i,(q,r) in enumerate(zip(polygon,polygon[1:]+polygon[:1])):
  x,y=q; X,Y=r; cross=x*Y-X*y
  if y<=0<Y and cross>0: winding+=1; crossings.append([i,1])
  elif Y<=0<y and cross<0: winding-=1; crossings.append([i,-1])
 check('zero_boundary_winding',winding==0)
 # Independent zero-count check of the same boundary degree: spatial walls
 # have H>0; on each face segment either H has fixed sign, or Hx does and
 # endpoint H signs determine whether the strictly monotone H crosses once.
 face_counts={str(tlo):0,str(thi):0}
 for i,(q0,q1,s) in enumerate(boundary):
  if q0[0]!=q1[0]:continue
  v0=endpoint_values[i][0]; v1=endpoint_values[(i+1)%len(polygon)][0]
  check('time_face_endpoint_H_nonzero_'+str(i),(v0>0 or v0<0) and (v1>0 or v1<0))
  opposite=(v0>0 and v1<0) or (v0<0 and v1>0)
  check('time_face_sign_change_requires_monotone_H_'+str(i),not opposite or s[1]==1)
  face_counts[str(q0[0])]+=int(opposite)
 wall_checks={}
 for x in [xlo,xhi]:
  v=enclose(tlo,thi,x,x)
  check('spatial_wall_H_strictly_positive_'+str(x),v[0]>0)
  wall_checks[str(x)]=rec(v[0])
 check('winding_agrees_with_half_face_zero_count',2*winding==face_counts[str(tlo)]-face_counts[str(thi)])
 boundary_elapsed=time.monotonic()-boundary_start
 sign_witnesses={}
 for j,name in enumerate(['H','Hx']):
  for sign,label in [(1,'positive'),(-1,'negative')]:
   found=next(((q0,v[j]) for (q0,_,_),v in zip(boundary,endpoint_values) if sign*v[j]>0),None)
   check(name+'_has_'+label+'_boundary_witness',found is not None)
   sign_witnesses[name+'_'+label]={'t':str(found[0][0]),'x':str(found[0][1]),'enclosure':rec(found[1])}
 # Interior baseline uses the same validated enclosure, keeping the full time
 # interval in every cell and subdividing x only. This avoids an artificially
 # expensive full 2D grid. Every accepted strip excludes a common jet zero.
 strips=[]; interior_rejected=0
 def interior(a0,b0,depth=0):
  nonlocal interior_rejected
  v=enclose(tlo,thi,a0,b0); s=separator(v)
  if s: strips.append((a0,b0,s)); return
  interior_rejected+=1
  if depth>=30: raise RuntimeError('interior strip refinement limit')
  m=(a0+b0)/2; interior(a0,m,depth+1); interior(m,b0,depth+1)
 interior_start=time.monotonic(); before=evaluations; interior(xlo,xhi)
 interior_evaluations=evaluations-before; interior_elapsed=time.monotonic()-interior_start
 check('interior_baseline_covers_entire_rectangle',strips[0][0]==xlo and strips[-1][1]==xhi and all(a[1]==b[0] for a,b in zip(strips,strips[1:])))
 def canonical(v):return json.dumps(v,sort_keys=True,separators=(',',':')).encode()
 edge_records=[{'from':[str(z) for z in q0],'to':[str(z) for z in q1],'component':['H','Hx'][s[1]],'sign':s[2],'margin_lower':rec(s[0])} for q0,q1,s in boundary]
 poly_records=[[[str(z.numerator),str(z.denominator)] for z in q] for q in polygon]
 output={
  'date':'2026-10-15','prepared_for':'Edward Baker','llm_assistance':'Substantial LLM assistance; Arb validation plus exact rational polygon crossing arithmetic.',
  'coordinating_model':'gpt-6-astra','coordinating_reasoning_effort':'ultra',
  'provenance':'Coordinating model and effort verified by root from current rollout; delegated runtime settings not independently recorded.',
  'checker':Path(__file__).name,'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
  'python_version':platform.python_version(),'python_flint_version':flint.__version__,'precision_bits':a.bits,
  'exact_box':{'t':[str(tlo),str(thi)],'x':[str(xlo),str(xhi)]},'exact_midpoint':[str(tc),str(xc)],
  'normalization':'H(t,x)=int_0^infty e^(t*u^2) sum_n (2*pi^2*n^4*e^(9u)-3*pi*n^2*e^(5u))*e^(-pi*n^2*e^(4u))*cos(xu) du',
  'finite_modes':N,'source_cutoff':1,'maximum_midpoint_jet_order':JMAX,'maximum_moment_order':MOMAX,
  'taylor_degrees':{'x':L,'t':K},'absolute_moment_upper_bound':rec(M),
  'omitted_mode_bound_on_u_0_1':rec(mode_tail),'complete_source_bound_on_u_ge_1':rec(source_tail),
  'full_jet_tail':rec(jet_tail),'uniform_taylor_error_each_component':rec(taylor_error),
  'midpoint_jet_enclosures':[rec(z) for z in jets],
  'boundary':{'orientation':'dt wedge dx','segments':len(boundary),'rejected_parent_segments':rejected,'maximum_bisection_depth':max_depth,
   'range_evaluations':segment_evaluations,'vertex_evaluations':len(polygon),'total_enclosure_evaluations':segment_evaluations+len(polygon),'minimum_halfplane_margin':rec(min(s[0] for _,_,s in boundary)),
   'polygon_winding_exact':winding,'positive_H_ray_crossings':crossings,'segments_sha256':hashlib.sha256(canonical(edge_records)).hexdigest(),
   'rational_polygon_sha256':hashlib.sha256(canonical(poly_records)).hexdigest(),'rational_polygon_vertices':poly_records,'segment_records':edge_records},
  'component_sign_change_witnesses':sign_witnesses,
  'boundary_degree_crosscheck':{'face_simple_zero_counts':face_counts,'spatial_wall_H_enclosures':wall_checks,'additional_wall_enclosure_evaluations':2},
  'interior_baseline':{'method':'Full-time strips with adaptive x subdivision; same rigorous first-jet coordinate enclosure.',
   'accepted_strips':len(strips),'rejected_parent_strips':interior_rejected,'range_evaluations':interior_evaluations,
   'minimum_halfplane_margin':rec(min(s[0] for _,_,s in strips))},
  'timing_seconds':{'shared_midpoint_integrals':integral_elapsed,'boundary_plus_polygon':boundary_elapsed,'interior_strip_baseline':interior_elapsed,'total':time.monotonic()-start},
  'cost_assessment':'Both methods share 76 complete midpoint jet enclosures and identical tails. Boundary cost includes all 234 polygon vertices and the optional two wall checks. The evaluator uses time-coefficient caching on fixed-time faces and the alternate Horner order on variable-time intervals. Counts and timings are implementation-specific. This is a coordinate-separation interior baseline, not a comparison with all possible stationary algorithms. No practical speed advantage is claimed.',
  'assertions_passed':len(checks),'checks':checks,
  'establishes':['The complete theta first jet is nonzero on every boundary segment, with neither H nor Hx of fixed sign on the boundary.',
   'A homotopic rational polygon has winding zero, so the same-sign spacetime index theorem excludes interior collisions.',
   'The independently covered full-time interior strips also directly exclude collisions on the whole closed rectangle.'],
  'does_not_establish':['A global theta phase estimate, RH, or a new local-index theorem.','A computational advantage over the recorded interior baseline or existing general stationary methods.','Formal proof verification or external refereeing.']}
 text=json.dumps(output,indent=2)+'\n'
 if a.output:a.output.write_text(text)
 else:print(text,end='')
 print('PASS',len(checks),'assertions;',len(boundary),'boundary segments;',len(strips),'interior strips; winding',winding,flush=True)
if __name__=='__main__':main()
