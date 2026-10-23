#!/usr/bin/env python3
"""Bounded complete-cap range quadrature on the frozen original theta box.
Prepared for Edward Baker, 2026-10-23, substantial LLM assistance,
gpt-6-astra (Codex), effort ultra. Whole faces; no root disks or omissions.
"""
import argparse,hashlib,heapq,json,time
from fractions import Fraction as F
from math import factorial
from pathlib import Path
from flint import arb,acb
import hdc13_theta_core as source_module
from hdc13_theta_core import ActualHeatCore,rec


def A(x):
 x=F(x);return arb(x.numerator)/x.denominator

def cell(b):
 x0,x1,y0,y1=b
 return acb(arb(A((x0+x1)/2),A((x1-x0)/2)),arb(A((y0+y1)/2),A((y1-y0)/2)))

def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--floor',type=Path,required=True);ap.add_argument('--output',type=Path);ap.add_argument('--leaves',type=int,default=512)
 a=ap.parse_args()
 if not 32<=a.leaves<=512:raise ValueError('fixed bounded pilot permits32..512 leaves')
 start=time.perf_counter();core=ActualHeatCore();checks=[]
 def check(name,v):
  if not v:raise ArithmeticError(name)
  checks.append(name)
 data=json.loads(a.floor.read_text());initial=[tuple(F(x) for x in r['spatial_bounds']) for r in data['leaf_records']]
 check('initial spatial area exactly80',sum(((b[1]-b[0])*(b[3]-b[2]) for b in initial),F(0))==80)
 check('initial cells contained in original rectangle',all(F(26)<=b[0]<b[1]<=46 and F(-2)<=b[2]<b[3]<=2 for b in initial))
 check('initial spatial cells disjoint',all(not(max(b[0],c[0])<min(b[1],c[1]) and max(b[2],c[2])<min(b[3],c[3])) for i,b in enumerate(initial) for c in initial[:i]))
 floors=[]
 for b in initial:
  j=core.jets(cell(b),1);floors.append(sum((v.abs_lower()**2 for v in j),arb(0)).abs_lower())
 floor=min(floors);check('replayed full-volume E floor exceeds1e-13',floor>arb(1)/10**13)
 eps=arb(1)/10000;Y=eps;sig=arb(0,Y);tt=arb(-eps/2,eps/2)
 tau0=acb(0,sig);tauleft=acb(-eps,sig);taum=acb(tt,-Y);taup=acb(tt,Y)
 tauall=acb(tt,sig);const=2*arb.pi()**2
 def positive(E):
  lo=max(E.lower(),floor);hi=E.upper()
  check('density E upper respects acquired floor',hi>=lo)
  return arb((lo+hi)/2,(hi-lo)/2)
 def inverse_E(E):
  lo=max(E.lower(),floor);hi=E.upper()
  low=1/hi;high=1/lo
  return arb((low+high)/2,(high-low)/2)
 def forms(j):
  h,h1,h2,h3=j
  E=positive(abs(h)**2+abs(h1)**2)
  L=h1*h1-h*h2;N=h2*h2-h1*h3;M=h1*h2-h*h3
  return E,L,N,M
 def densities(j):
  E,L,N,M=forms(j);inv=inverse_E(E)**2/const
  ln=L*N.conjugate();mn=M*N.conjugate()
  return [ln.real*inv,ln.imag*inv,mn.real*inv,mn.imag*inv]
 # Difference H(t+iY)-H(t-iY), retaining factor2iY before interval arithmetic.
 weights=[acb(0)]+[((-1)**k)*acb(0,2*Y)*sum((taup**i*taum**(k-1-i) for i in range(k)),acb(0))/factorial(k) for k in range(1,core.A)]
 def delta_jets(z):
  mid=acb(z.real.mid(),z.imag.mid());dz=z-mid;rho=dz.abs_upper();order=3+core.J-1
  v=core._normalized_poly_jets(mid-core.center,order+2*(core.A-1))
  pv=[sum((weights[k]*factorial(j+2*k)*v[j+2*k] for k in range(1,core.A)),acb(0)) for j in range(order+1)]
  out=[]
  for j in range(4):
   val=sum((pv[j+l]*dz**l/factorial(l) for l in range(core.J)),acb(0))
   bound=sum((weights[k].abs_upper()*core.bounds[j+core.J+2*k] for k in range(1,core.A)),arb(0))
   err=(rho**core.J*bound/factorial(core.J)+2*core.errors[j]).abs_upper()
   out.append(acb(val.real+arb(0,err),val.imag+arb(0,err)))
  return out
 def paired_p(z):
  j=core.jets(z,3,tau=taum);d=delta_jets(z);E,L,N,M=forms(j)
  h,h1,h2,h3=j;dh,d1,d2,d3=d
  dE=2*(h*dh.conjugate()+h1*d1.conjugate()).real+abs(dh)**2+abs(d1)**2
  dL=2*h1*d1+d1*d1-h*d2-dh*h2-dh*d2
  dN=2*h2*d2+d2*d2-h1*d3-d1*h3-d1*d3
  numerator=(L*N.conjugate()).imag
  dn=(dL*N.conjugate()+L*dN.conjugate()+dL*dN.conjugate()).imag
  Ep=positive(E+dE);dE2=dE*(2*E+dE)
  return (dn*E**2-numerator*dE2)*inverse_E(Ep)**2*inverse_E(E)**2/const
 serial=0;evaluations=0;active={};queue=[]
 def evaluate(b):
  nonlocal serial,evaluations
  evaluations+=1;z=cell(b);area=A((b[1]-b[0])*(b[3]-b[2]))
  direct=densities(core.jets(z,3,tau=tau0))[0]*area*(2*Y)
  left=densities(core.jets(z,3,tau=tauleft))[0]*area*(2*Y)
  ps=paired_p(z)*area*eps
  values=(direct,left,ps);serial+=1
  # Float only chooses refinement order; every mathematical bound is an Arb ball.
  score=sum(float(v.rad()) for v in values)
  active[serial]=(b,values);heapq.heappush(queue,(-score,serial));return serial
 for b in initial:evaluate(b)
 while len(active)<a.leaves:
  _,idx=heapq.heappop(queue)
  if idx not in active:continue
  b,_=active.pop(idx);x0,x1,y0,y1=b
  if x1-x0>=y1-y0:
   mid=(x0+x1)/2;children=[(x0,mid,y0,y1),(mid,x1,y0,y1)]
  else:
   mid=(y0+y1)/2;children=[(x0,x1,y0,mid),(x0,x1,mid,y1)]
  for c in children:evaluate(c)
 cap_sums=[sum((v[1][j] for v in active.values()),arb(0)) for j in range(3)]
 spatial_seconds=time.perf_counter()-start
 # Every remaining wall face, paired at its actual opposite physical faces.
 sides=32;rx=arb(0);sy=arb(0)
 for i in range(sides):
  y0=F(-2)+F(4*i,sides);y1=F(-2)+F(4*(i+1),sides)
  va=densities(core.jets(cell((F(26),F(26),y0,y1)),3,tau=tauall))[2]
  vb=densities(core.jets(cell((F(46),F(46),y0,y1)),3,tau=tauall))[2]
  rx+=(vb-va)*A(y1-y0)*eps*(2*Y)
  x0=F(26)+F(20*i,sides);x1=F(26)+F(20*(i+1),sides)
  bot=densities(core.jets(cell((x0,x1,F(-2),F(-2))),3,tau=tauall))[3]
  top=densities(core.jets(cell((x0,x1,F(2),F(2))),3,tau=tauall))[3]
  sy+=(top-bot)*A(x1-x0)*eps*(2*Y)
 I0,Im,Ssigma=cap_sums;S=Ssigma+rx+sy;B=Im-S
 check('complete cap direct and deformed intervals overlap',I0.overlaps(B))
 check('final spatial leaf area exactly80',sum(((b[1]-b[0])*(b[3]-b[2]) for b,_ in active.values()),F(0))==80)
 check('all numerical intervals finite',all(v.is_finite() for v in (I0,Im,Ssigma,rx,sy,S,B)))
 # Repeated denominator checks are summarized to keep the record small.
 repeated=checks.count('density E upper respects acquired floor')
 checks=[v for v in checks if v!='density E upper respects acquired floor']
 leaves=[{'bounds':[str(x) for x in b],'I0':rec(v[0]),'I_minus':rec(v[1]),'sigma_pair':rec(v[2])} for b,v in active.values()]
 result={'status':'PASS_BOUNDED_ENCLOSURE','date':'2026-10-23','prepared_for':'Edward Baker','model':'gpt-6-astra','reasoning_effort':'ultra','llm_assistance':True,
  'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'core_sha256':hashlib.sha256(Path(source_module.__file__).read_bytes()).hexdigest(),
  'input_floor_sha256':hashlib.sha256(a.floor.read_bytes()).hexdigest(),'source_oracle':core.metadata(),
  'box':{'x':['26','46'],'y':['-2','2'],'epsilon':'1/10000','Y':'1/10000'},
  'replayed_full_volume_E_floor':rec(floor),'shared_floor_cells':len(initial),'cap_spatial_leaves':len(active),'cap_parent_and_leaf_evaluations':evaluations,
  'side_segments_per_coordinate':sides,'raw_I0':rec(I0),'raw_I_minus_epsilon':rec(Im),'raw_S_sigma':rec(Ssigma),'raw_S_x':rec(rx),'raw_S_y':rec(sy),'raw_S_total':rec(S),'raw_B':rec(B),
  'direct_positive_lower_bound':bool(I0>0),'deformed_positive_lower_bound':bool(B>0),
  'direct_width':rec(2*I0.rad()),'deformed_width':rec(2*B.rad()),
  'denominator_consistency_checks':repeated,'checks':checks,
  'comparison_cost':{'shared_source_and_floor':'one source setup and31 rechecked complete first-jet cells',
    'direct':'one full jet0..3 range per tested cap spatial cell on common mesh',
    'deformed':'one left-cap jet range plus one sigma-face reference range and one coupled heat-polynomial difference range per tested spatial cell, plus128 side jet ranges',
    'interpretation':'Matched fixed geometry and common adaptive mesh. No claim of globally optimal quadrature or asymptotic computational complexity.'},
  'timing_seconds':{'cap_phase_including_shared_floor':spatial_seconds,'total':time.perf_counter()-start},
  'spatial_leaf_records':leaves,
  'establishes':['A finite rigorous range-quadrature enclosure for the entire original I0 cap and for every face of B_epsilon; no root chart or complementary region is omitted.',
    'The complete first jet is nonzero throughout the physical box, hence the exact geometric identity is B_epsilon=I0 with Q_minus=0.'],
  'does_not_establish':['A sharp quadrature, global simplicity estimate, or universal advantage or obstruction for curved contours.',
    'Any small positive lower bound unless the corresponding recorded positivity flag is true.']}
 text=json.dumps(result,indent=2)+'\n'
 if a.output:a.output.write_text(text)
 else:print(text,end='')
 print('I0',rec(I0),'B',rec(B),'S',rec(S),'leaves',len(active),file=__import__('sys').stderr)
if __name__=='__main__':main()
