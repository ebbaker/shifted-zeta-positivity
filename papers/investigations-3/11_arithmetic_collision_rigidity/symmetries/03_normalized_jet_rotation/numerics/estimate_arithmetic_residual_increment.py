#!/usr/bin/env python3
"""Complete independent arithmetic residual increment on the fixed G3 pilot.

Prepared for Edward Baker, 19 October 2026, substantial LLM assistance.
Execution model/effort supplied by CLI. No physical-source Taylor data are used.
The companion proof pays the coherent RS8/Gaussian polynomial edge and finite
heat-Stirling mode remainder. This evaluates their signed endpoint primitive.
"""
from pathlib import Path
import sys, math, importlib.util, time, argparse, hashlib, json, platform
from fractions import Fraction as F
sys.dont_write_bytecode=True
import flint
from flint import arb, acb, acb_series, ctx
INV=Path('papers/investigations-3/11_arithmetic_collision_rigidity')
LANE=INV/'symmetries/03_normalized_jet_rotation'
COHERENT=INV/'symmetries/02_cutoff_reflection/numerics/check_cutoff_reflection.py'
HIERARCHY=LANE/'numerics/check_rs_edge_hierarchy.py'
FINITE=LANE/'numerics/check_heat_stirling_remainder.py'
BOUND=LANE/'numerics/bound_complete_rs_edge.py'
def load(p,n):
 spec=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(spec)
 sys.modules[n]=m;spec.loader.exec_module(m);return m
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def out(v):return v.str(38,more=True)
def check(v,msg):
 if not v:raise ArithmeticError(msg)
def A(v):return arb(v.numerator)/v.denominator if isinstance(v,F)else arb(v)
def box(a,b):
 a,b=A(a),A(b);return arb((a+b)/2,((b-a)/2).upper())
def fder(p,n):
 h=p-p0;v=acb(0)
 # multiplication/division is performed in ball arithmetic, not floats.
 v=acb(0)
 for k in reversed(range(n,121)):v=v*h+fc[k]*(math.factorial(k)//math.factorial(k-n))
 return v

def ds_poly(K):
 d={(0,0):[F(1)]};get=lambda n,k:d.get((n,k),[])
 for n in range(1,K+1):
  for k in range(3*n//2+1):
   m=3*n-2*k
   if m:d[n,k]=rr.add(rr.scale(get(n-1,k),F(1,4*m)),rr.mul([F(1,2*m),F(-1,m)],get(n-1,k-1)),rr.scale(get(n-1,k-2),-m-1))
   else:d[n,k]=rr.add(*(rr.scale(get(n,j),-(-1)**(k-j)*F(math.factorial(2*k-2*j),math.factorial(k-j)))for j in range(k)))
 return d
def g_series(tau,L=12,J=24):
 b=ii*tau;u=acb_series([acb(A(F(1,2))),acb(1)],L+1)
 eta=acb_series([0],L+1);eb=acb_series([0],L+1);ebb=acb_series([0],L+1)
 def term(uc,c,k,den):
  nonlocal eta,eb,ebb
  eta+=uc*c*den**(-k);eb+=uc*(-k*c)*den**(-k-1);ebb+=uc*(k*(k+1)*c)*den**(-k-2)
 term(u+u*u,A(F(1,2)),1,b)
 for k in range(2,J+1):
  c=A(F((-1)**(k+1),2*k));term(u**k,c,k-1,b);term(u**k*(1+u),c,k,b)
 for k in range(1,J+1):term(u**k,A(F((-1)**(k+1),k)),k,b-1)
 for k,c in [(1,F(1,6)),(3,F(-1,45)),(5,F(8,315))]:term(acb_series([1],L+1),A(c),k,b+u)
 g=eta.exp();gx=g*ii*eb/2;gxx=-g*(eb*eb+ebb)/4
 return [g,gx,gxx]

def edge(x,t,K=8,L=12):
 tau=x/2+pi*t/8;a=(tau/(2*pi)).sqrt();p=17-2*a;gamma_x=1/(4*tau);gamma_xx=-1/(8*tau*tau);px=-1/(4*pi*a);pxx=-px*gamma_x
 fd=[fder(p,j)for j in range(3*K+3)]
 P=L+K+1;u=acb_series([acb(A(F(1,2))),acb(1)],P)
 poly=[acb_series([0],P)for _ in range(3)]
 for k in range(K+1):
  for j in range(3*k//2+1):
   coeff=DS[k,j];dp=acb_series([0],P)
   for c in reversed(coeff):dp=dp*u+A(c)
   m=3*k-2*j;factor=(pi/(2*ii))**j/pi**(2*k)/a**k
   row=[fd[m],fd[m+1]*px-k*gamma_x*fd[m],fd[m+2]*px*px+fd[m+1]*(pxx-2*k*gamma_x*px)+fd[m]*(k*k*gamma_x*gamma_x-k*gamma_xx)]
   for n in range(3):poly[n]+=dp*factor*row[n]
 gg=[acb_series([v[j]for j in range(L+1)]+[acb(0)]*K,P)for v in g_series(tau,L)]
 products=[gg[0]*poly[0],gg[1]*poly[0]+gg[0]*poly[1],gg[2]*poly[0]+2*gg[1]*poly[1]+gg[0]*poly[2]]
 means=[]
 for v in products:
  means.append(sum((v[2*j]*(t/2)**j*math.prod(range(1,2*j,2))for j in range((L+K)//2+1)),acb(0)))
 # Subtract the retained Chat profile, with coherent spatial derivatives.
 means[0]-=fd[0];means[1]-=fd[1]*px;means[2]-=fd[2]*px*px+fd[1]*pxx
 ps=acb_series([means[0],means[1],means[2]/2],3)
 z=acb_series([acb(x),acb(1)],3);ts=z/2+pi*t/8
 ds=acb_series([v.real for v in ps],3);es=acb_series([v.imag for v in ps],3)
 q=o.W_real(z,t)*ts.sqrt()*(ts*ds-es)
 return [q[0].real,q[1].real,2*q[2].real]

def finite_jets(x,t):
 z=acb_series([acb(x),acb(1)],3);s=(1-ii*z)/2;hh=acb_series([0],3)
 for n in range(1,9):
  ell=A(n).log();aa=o.alpha(s)-ell
  p=(-s*ell+t*(ell*ell-2*o.alpha(s)*ell)/4).exp()
  kap=1/(6*s)+o.alphap(s)*(t/4+t*t*aa*aa/8);hh+=p*kap
 th,w,wp=phase(x,t);H=acb_series([hh[j]for j in range(3)],3)
 ths=acb_series([acb(th),acb(w),acb(wp/2)],3)
 q=(ii*ths).exp()*H
 return [2*q[0].real,2*q[1].real,4*q[2].real]
def rotating_finite(x,t):
 z=acb_series([acb(x),acb(1)],2);s=(1-ii*z)/2;hh=acb_series([0],2)
 for n in range(1,9):
  ell=A(n).log();aa=o.alpha(s)-ell
  p=(-s*ell+t*(ell*ell-2*o.alpha(s)*ell)/4).exp()
  kap=1/(6*s)+o.alphap(s)*(t/4+t*t*aa*aa/8);hh+=p*kap
 th,w,_=phase(x,t)
 return 2*hh[0]-ii/w*(hh[1]+(-2*ii*th).exp()*hh[1].conjugate())
def rotating_model(x,t):
 qe=edge(x,t);th,w,_=phase(x,t)
 return rotating_finite(x,t)+(-ii*th).exp()*(qe[0]-ii*qe[1]/w)
def phase(x,t):
 z=acb_series([acb(x),acb(1)],3);s=(1-ii*z)/2
 th=(o.mt(s,t)-o.mt(1-s,t))/(2*ii)
 return th[0].real,th[1].real,2*th[2].real

def initialize(repo,bits):
 global o,rr,pi,ii,p0,fc,DS
 ctx.prec=bits+512;ctx.cap=130
 o=load(repo/COHERENT,'g3_complete_modes_'+str(bits))
 rr=load(repo/HIERARCHY,'g3_complete_coeff_'+str(bits))
 pi=arb.pi();ii=acb(0,1);p0=acb(-A(21)/25)
 pw=acb_series([p0,acb(1)],121)
 profile=((ii*pi*(pw*pw/2+A(F(3,8)))).exp()-ii*A(2).sqrt()*(pi*pw/2).cos())/(2*(pi*pw).cos())
 fc=[profile[j]for j in range(121)];DS=ds_poly(8)

def run(repo,bits,bound_record):
 initialize(repo,bits);started=time.monotonic()
 finite=load(repo/FINITE,'g3_complete_finite_'+str(bits)).finite_mode_ledger(repo,bits)
 ctx.prec=bits+512
 e0=arb(finite['totals']['normalized_value'])+A('6e-8')
 e1=arb(finite['totals']['normalized_x'])+A('6e-8')
 e2=arb(finite['totals']['normalized_xx'])+A('1.2e-7')
 omega=arb(finite['normalizer']['omega']);wlo=omega.abs_lower()
 check(omega<0 and wlo>0,'oriented nonzero omega')
 endpoint_error=(e0*e0+(e1/wlo)**2).sqrt().upper()
 prefix_error=(2*endpoint_error).upper()
 # A closed, declared 8x32 cover. No subdivision optimization is performed.
 nt,nx=8,32;largest=A(0);slabs=[];cells=[];worst=None
 for it in range(nt):
  tl=F(1,100)+F(19,100)*it/nt;tu=F(1,100)+F(19,100)*(it+1)/nt
  t=box(tl,tu);anchor=rotating_model(A(999),t);slabmax=A(0)
  for ix in range(nx):
   xl=F(999)+F(2)*ix/nx;xu=F(999)+F(2)*(ix+1)/nx;x=box(xl,xu)
   nominal=rotating_model(x,t)-anchor;payment=abs(nominal).upper()
   check(payment.is_finite(),'finite complete prefix model')
   cells.append({'it':it,'ix':ix,'nominal':str(nominal),'upper':str(payment)})
   if payment>slabmax:slabmax=payment
   if payment>largest:
    largest=payment;worst={'t':[str(tl),str(tu)],'x':[str(xl),str(xu)],'nominal':out(nominal),'upper':out(payment)}
  slabs.append({'t':[str(tl),str(tu)],'nominal_prefix_upper':out(slabmax)})
 total=(largest+prefix_error).upper()
 check(total<A('.000854'),'complete independent arithmetic allowance ceiling')
 check(total<A('.812260'),'improvement on complete analytic-only allowance')
 # Independent algebra/formula checks at the pilot center.
 x,t=A(1000),A(F(21,200));ef=edge(x,t);ff=finite_jets(x,t)
 theta,w,wp=phase(x,t);q=[a+b for a,b in zip(ef,ff)]
 direct=(-ii*theta).exp()*(q[0]-ii*q[1]/w)
 retained=rotating_model(x,t)
 check(direct.overlaps(retained),'rotating-finite product identity')
 point={'t':'21/200','x':1000,'edge_model_jets':[out(v)for v in ef],
        'finite_kappa_jets':[out(v)for v in ff],
        'model_rotation_defect':out(q[0]+q[2]/w**2-wp*q[1]/w**3),
        'rotating_model':out(retained),'direct_rotating_formula':out(direct)}
 # A tiny extra budget for nonfinite-control validation is not inferred here:
 # this is an error certificate, not a new event-acceptance interface.
 return {'requested_bits':bits,'working_bits':bits+512,'domain':{'t':['1/100','1/5'],'x':['999','1001']},
  'fixed_cutoff':8,'edge_RS_order':8,'gaussian_Taylor_degree':12,'log_series_degree':24,'profile_Taylor_degree':120,
  'cover':{'time_slabs':nt,'spatial_cells':nx,'closed_cells':nt*nx,'anchor_x':999},
  'complete_edge_value_error_input':'6e-8','complete_edge_x_error_input':'6e-8','complete_edge_xx_error_input':'1.2e-7',
  'finite_remainder_ledger':finite,'complete_normalized_residual_errors':[out(v.upper())for v in (e0,e1,e2)],
  'omega_abs_lower':out(wlo),'endpoint_jet_error':out(endpoint_error),'two_endpoint_error_payment':out(prefix_error),
  'nominal_prefix_upper':out(largest),'complete_arithmetic_increment_upper':out(total),
  'reported_ceiling':'0.000854','old_analytic_only_allowance':'0.812260','source_informed_comparator':'0.000266448',
  'old_analytic_allowance_over_new':out(A('.812260')/total),
  'source_comparator_beaten':bool(total<A('.000266448')),'worst_model_cell':worst,'slabs':slabs,
  'cells_math_sha256':hashlib.sha256(json.dumps(cells,sort_keys=True,separators=(',',':')).encode()).hexdigest(),
  'center_formula_check':point,'observed_seconds':time.monotonic()-started,
  'scope':'Uniform complete arithmetic residual increment on B, independent of source Taylor data. No new consumer comparison, source-informed improvement, coverage, or height-uniform theorem.'}

def main():
 p=argparse.ArgumentParser();p.add_argument('--repo',type=Path,required=True)
 p.add_argument('--edge-record',type=Path,required=True);p.add_argument('--output',type=Path,required=True)
 p.add_argument('--bits',type=int,nargs='+',choices=[192,256],default=[192,256])
 p.add_argument('--execution-model',required=True);p.add_argument('--execution-effort',required=True)
 a=p.parse_args();repo=a.repo.resolve();edge_record=json.loads(a.edge_record.read_text())
 check(edge_record['script_sha256']==sha(repo/BOUND),'complete edge producer pin')
 check(edge_record['retained_model']['sha256']==sha(__file__),'edge polynomial model pin')
 for path,digest in edge_record['source_sha256'].items():check(sha(repo/path)==digest,'complete edge source pin: '+path)
 check(edge_record['runs'] and all(v['normalized_value_cap']=='6e-8' and v['physical_disk_radius']=='1' and v['normalized_first_x_cap']=='6e-8' and v['normalized_second_x_cap']=='1.2e-7' for v in edge_record['runs']),'complete edge cap')
 check(set(a.bits)<=set(v['requested_bits']for v in edge_record['runs']),'edge precision coverage')
 sources=[COHERENT,HIERARCHY,FINITE,BOUND,LANE/'notes/06_ARITHMETIC_GAMMA_AND_EDGE_CORRECTIONS_20261019.md']
 result={'date':'2026-10-19','prepared_for':'Edward Baker','actual_model':a.execution_model,'actual_effort':a.execution_effort,
  'llm_assistance':'substantial; separate same-model arithmetic and proof review; no specialist review',
  'python':platform.python_version(),'python_flint':flint.__version__,'script_sha256':sha(__file__),
  'source_sha256':{str(v):sha(repo/v)for v in sources},'complete_edge_record_sha256':sha(a.edge_record),
  'source_theta_taylor_data_used':False,'source_quadrature_used':False,
  'runs':[run(repo,b,edge_record)for b in a.bits]}
 a.output.write_text(json.dumps(result,indent=2)+chr(10))
 print(json.dumps({'output':str(a.output),'bounds':[v['complete_arithmetic_increment_upper']for v in result['runs']]}))
if __name__=='__main__':main()
