#!/usr/bin/env python3
"""Source-free exact Fraction audit of fixed FCG-E02 R5 evidence.

30 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Actual model gpt-6.1-sol, effort ultra, Investigation05 chat0047.
Reads frozen records only; never imports or evaluates the source integrator.
"""
from fractions import Fraction as F
from hashlib import sha256
from math import factorial, isqrt
from pathlib import Path
import argparse
import json
import re

BASE = "papers/investigations-5/05_radial_theta_collision_geometry"
PACKET = BASE + "/research-progress/handoffs/fixed_coefficient_parameter_geometry/FCG-E02_R5_ADAPTIVE_RADIUS_IBP_ASSESSMENT_20261030.md"
PACKET_SHA = "b1c695e9cd0a2cf57b7efe0e0110213604a284f79de82ff6461cd8bb30249a4b"
SOURCE = BASE + "/numerics/fixed_coefficient_parameter_geometry/fcg_e01_r2_adaptive_ibp_20261030.json"
RADII = (F(1,64), F(1,128), F(1,256))
DEGREES = (1,2,4,8)
R = F(1,32)

class I:
    def __init__(self, lo, hi=None):
        if isinstance(lo,I): self.lo,self.hi=lo.lo,lo.hi
        else: self.lo,self.hi=F(lo),F(lo if hi is None else hi)
        assert self.lo<=self.hi
    def __add__(self,y):
        y=I(y); return I(self.lo+y.lo,self.hi+y.hi)
    __radd__=__add__
    def __neg__(self): return I(-self.hi,-self.lo)
    def __sub__(self,y): return self+-I(y)
    def __rsub__(self,y): return I(y)+-self
    def __mul__(self,y):
        y=I(y); z=[a*b for a in (self.lo,self.hi) for b in (y.lo,y.hi)]
        return I(min(z),max(z))
    __rmul__=__mul__
    def __truediv__(self,y):
        y=I(y); assert not y.lo<=0<=y.hi
        return self*I(1/y.hi,1/y.lo)
    def __rtruediv__(self,y): return I(y)/self
    def __pow__(self,n):
        assert isinstance(n,int) and n>=0
        if n==0:return I(1)
        if n==2:return self.square()
        return self.square()**(n//2) if n%2==0 else self*(self**(n-1))
    def absolute(self):
        return I(0 if self.lo<=0<=self.hi else min(abs(self.lo),abs(self.hi)),max(abs(self.lo),abs(self.hi)))
    def square(self):
        a=self.absolute(); return I(a.lo*a.lo,a.hi*a.hi)
    def sqrt(self):
        assert self.lo>=0
        scale=2**512
        def down(x): return F(isqrt(x.numerator*scale*scale//x.denominator),scale)
        a,b=down(self.lo),down(self.hi)
        if b*b<self.hi:b+=F(1,scale)
        return I(a,b)
    def contains(self,y):
        y=I(y); return self.lo<=y.lo and y.hi<=self.hi
    def overlaps(self,y): return self.lo<=y.hi and y.lo<=self.hi
    def nonnegative(self): return I(max(F(0),self.lo),max(F(0),self.hi))

def p2(pair):
    m,e=int(pair[0]),int(pair[1]); return F(m*2**e) if e>=0 else F(m,2**(-e))
def binary(obj):
    m,r=p2(obj['mid_binary']),p2(obj['rad_binary']); assert r>=0
    return I(m-r,m+r)
def decimal(s):
    s=s.strip()
    if not s.startswith('['):return I(F(s))
    m,r=(F(x.strip()) for x in s[1:-1].split('+/-')); return I(m-r,m+r)
def imin(xs): return I(min(x.lo for x in xs),min(x.hi for x in xs))
def tail(r,n,outer):
    q=r/outer; return q**(n+1)*((n+2)-(n+1)*q)/(1-q)**2
def mg(h,z,U):
    u,v=U;b,h1=h[2],h[1]
    return 2*b.absolute()*((z**3/6+z*z)*u+z*z*v/2)+(h1.absolute()+z*b.absolute())*(z+z*z/2)*u
def case(h,r,n,outer,U):
    b,h1=h[2],h[1]
    def q(m,k):
        if (m,k) in ((0,0),(0,1),(0,2),(1,0)):return I(0)
        return (-1)**m*h[2*m+k]/(factorial(m)*factorial(k))
    finite=I(0)
    for k in range(1,n+1):
        for m in range(k+1):
            v=k-m;g=b*(v-2)*q(m,v)+h1*(v+1)*q(m,v+1)
            finite+=g.absolute()*r**k
    D=(h1.square()-2*b*h[0]).absolute();payment=2*b.square()*r
    M=mg(h,outer,U);tf=tail(r,n,outer);t=M*tf;G=finite+t;d=D-payment-G
    c=d/(1+h[0].square()+h1.square()+b.square())
    K=(4*b.square()+(h1.absolute()+r*b.absolute()).square()).sqrt()
    mu=d/K if d.lo>0 else I(0)
    sh=h[0].absolute()-r*h1.absolute()-b.absolute()*(r+r*r/2)-(r**3/6+r*r)*U[0]-r*r*U[1]/2
    sa=h1.absolute()-r*b.absolute()-(r+r*r/2)*U[0]
    return dict(D=D,time=payment,finite_sum=finite,M_G=M,tail_factor=I(tf),tail=t,Gamma=G,d=d,c=c,K=K,mu=mu,scalar_H_floor=sh,scalar_HA_floor=sa)
def radius(h,U):
    D=(h[1].square()-2*h[2]*h[0]).absolute()
    L0=2*h[2].square()+(h[1]*h[3]).absolute();M=mg(h,R,U)
    return imin([I(R/2),I(F(1,8)),D/(L0+(L0.square()+16*M*D/R**2).sqrt())])

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--repo',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);a=ap.parse_args()
    assert not a.output.exists(),'preserve earlier record'
    root=a.repo.resolve();checks=0
    def check(ok,label):
        nonlocal checks
        assert ok,label
        checks+=1
    check(sha256((root/PACKET).read_bytes()).hexdigest()==PACKET_SHA,'packet bytes')
    frozen=re.findall(r'\| `([^`]+)` \| `([0-9a-f]{64})` \|',(root/PACKET).read_text())
    check(len(frozen)==20,'twenty frozen inputs');hashes=[]
    for path,expected in frozen:
        actual=sha256((root/path).read_bytes()).hexdigest();check(actual==expected,path)
        hashes.append(dict(path=path,sha256=actual))
    source=json.loads((root/SOURCE).read_text())
    check(source['terminal_status']=='completed_fixed_comparison' and source['refinement'] is None,'completed without refinement')
    check(source['limits']==dict(seconds=1200,eval_limit=200000,depth_limit=30,panel_counts=[1024,2048],precisions=[256,384]),'fixed work limits')
    check(source['fixed']==dict(tau='1/4',a='64',R='1/32',radii=['1/64','1/128','1/256'],degrees=[1,2,4,8],modes=8,analytic_cutoff=1,U3='41*pi/128',U4='21*pi/64'),'fixed inputs')
    check(source['script_sha256']==sha256((root/BASE/'numerics/fixed_coefficient_parameter_geometry/execute_fcg_e01_r2.py').read_bytes()).hexdigest(),'execution script bytes')
    def guards(g):
        check(g['guards_pass'],'tail guard flag')
        check(decimal(g['beta']).lo>0 and decimal(g['ratio']).hi<1 and decimal(g['time_guard']).lo>=0,'actual mode guards')
        check(len(g['source_denominators'])==8 and all(decimal(x).lo>0 for x in g['source_denominators']),'actual exterior denominators')
        check(decimal(g['minimum_concavity']).lo>0,'actual concavity')
    stages=[];all_integrals=[];panels=[];stage_data=[]
    for s in source['stages']:
        bits=s['bits'];at,rt=(180,140) if bits==256 else (280,240)
        check(s['abs_tolerance']==f'2^-{at}' and s['rel_tolerance']==f'2^-{rt}','prescribed tolerances')
        ints=s['integrals'];all_integrals+=ints
        check(len(ints)==(24 if bits==256 else 28),'analytic call count per precision')
        for x in ints:
            f,c=binary(x['finite']),binary(x['complete'])
            mode,ext=decimal(x['mode_upper']),decimal(x['source_upper'])
            check(mode.lo>=0 and ext.lo>=0,'nonnegative complements')
            e=mode.hi+ext.hi
            check(c.contains(f+(I(-e,e) if x['kind']=='jet' else I(0,e))),'complete analytic input includes both tails')
            check(decimal(x['quad_radius_upper']).hi>=p2(x['finite']['rad_binary']),'quadrature radius')
            check(x['callbacks']<=200000,'callback limit');guards(x['tail'])
        check([(x['j'],x['T'],x['Y']) for x in ints[:6]]==[(j,str(F(1,4)+rho),str(rho)) for rho in (R,F(1,64),F(1,128)) for j in (3,4)],'six shared positive moments')
        jets=ints[6:24]
        check([(x['kind'],x['j'],x['T'],x['Y']) for x in jets]==[('jet',j,'1/4','0') for j in range(18)],'signed jets through seventeen')
        h=[binary(x['complete']) for x in jets]
        moments={rho:[binary(x['complete']) for x in ints[k:k+2]] for rho,k in ((R,0),(F(1,64),2),(F(1,128),4))}
        env=[]
        check(len(s['panel_acquisitions'])==2,'two panel acquisitions')
        for j,p in zip((3,4),s['panel_acquisitions']):
            panels.append(p);check(p['j']==j and p['count']==1024,'issued derivative and panel count')
            check(0<=p['inside_zero_crossing_panels']<=1024,'zero-crossing panel count')
            check(len(p['panel_contribution_sha256'])==64,'panel digest retained')
            for g in p['B_tail_components']:guards(g)
            guards(p['phase_exterior_tail'])
            check(len(p['B_tail_components'])==5,'complete derivative tail components')
            check(decimal(p['endpoint_ratio']).hi<1 and decimal(p['endpoint_mode_upper']).lo>=0,'paid endpoint guard')
            bm=decimal(p['core_mode_symmetric_upper']).hi
            bs=decimal(p['whole_retained_exterior_upper']).hi
            extra=decimal(p['whole_additional_mode_upper'])
            check(extra.overlaps(decimal(p['core_mode_symmetric_upper'])),'intentional duplicate I mode payment')
            expectedI=((binary(p['finite_core_whole'])+I(-bm,bm)).nonnegative()+I(0,bs+extra.hi))/(64-R)
            expectedW=(binary(p['boundary'])+(binary(p['finite_core_phase'])+I(-bm,bm)).nonnegative())/(64-R)+I(0,decimal(p['phase_retained_exterior_upper']).hi+decimal(p['phase_exterior_mode_upper']).hi)
            check(binary(p['I']).contains(expectedI),'whole envelope core plus full complements')
            check(binary(p['W']).contains(expectedW),'phase envelope boundary core and exterior')
            M,ii,w=(binary(p[k]) for k in ('M','I','W'))
            check(M.overlaps(moments[R][j-3]),'same moment information')
            check(w.hi<ii.lo and ii.hi<M.lo,'strict W < I < M')
            check(binary(p['selected_min']).contains(imin([M,ii,w])),'endpoint interval minimum')
            check(w.hi/M.lo<F('0.134' if j==3 else '0.140'),'published envelope reduction')
            env.append(binary(p['selected_min']))
        check(len(s['passes'])==1 and len(s['passes'][0]['rows'])==36,'one full thirty-six-case pass')
        rows=s['passes'][0]['rows'];values={};status_rows=[]
        check(len({(x['r'],x['N'],x['rule']) for x in rows})==36,'distinct case keys')
        for row in rows:
            r,n,rule=F(row['r']),row['N'],row['rule']
            check(r in RADII and n in DEGREES and rule in ('A','B','C'),'fixed case key')
            outer=2*r if rule=='A' else R;U=moments[outer] if rule!='C' else env
            check(F(row['outer'])==outer,'outer rule')
            v=case(h,r,n,outer,U);values[r,n,rule]=v
            for key,value in v.items():check(decimal(row[key]).contains(value),'row arithmetic '+str((bits,r,n,rule,key)))
            st='positive' if v['d'].lo>0 else ('nonpositive' if v['d'].hi<=0 else 'unresolved')
            check(st==row['status'] and st!='unresolved','endpoint status')
            if rule=='C' and st=='positive':
                check((v['scalar_H_floor'].hi<0 if r==F(1,128) else v['scalar_H_floor'].lo>0) and v['scalar_HA_floor'].hi<0,'matched scalar consumers')
            status_rows.append(dict(r=str(r),N=n,rule=rule,status=st))
        minima=[]
        for r in RADII:
            minimum={rule:next((n for n in DEGREES if values[r,n,rule]['d'].lo>0),None) for rule in ('A','B','C')}
            expected={'A':None,'B':None if r==F(1,64) else 8,'C':None if r==F(1,64) else (8 if r==F(1,128) else 4)}
            check(minimum==expected,'least passing issued degree');minima.append(dict(r=str(r),**minimum))
        for row in s['passes'][0]['differences']:
            r,n=F(row['r']),row['N'];gap=(mg(h,R,moments[R])-mg(h,R,env))*tail(r,n,R)
            check(gap.lo>0 and decimal(row['Gamma_B_minus_C']).contains(gap),'strict shared B minus C difference')
        rad=next(x for x in source['sharp_radius'] if x['bits']==bits)
        for key,U in (('B',moments[R]),('C',env)):
            check(binary(rad[key]).contains(radius(h,U)),'stable quadratic radius '+key)
        check(binary(rad['C']).lo>binary(rad['B']).hi*F('2.7'),'strict radius separation')
        stage_data.append(dict(h=h,moments=moments,env=env,values=values))
        stages.append(dict(bits=bits,rows=status_rows,minimum_degrees=minima,strict_W_I_M=True,all_twelve_B_minus_C_positive=True))
    x,y=stage_data
    for rho in x['moments']:
        for u,v in zip(x['moments'][rho],y['moments'][rho]):check(u.overlaps(v),'moment precision overlap')
    for u,v in zip(x['h'],y['h']):check(u.overlaps(v),'jet precision overlap')
    for u,v in zip(x['env'],y['env']):check(u.overlaps(v),'envelope precision overlap')
    for key in x['values']:
        for name in ('Gamma','d','c'):check(x['values'][key][name].overlaps(y['values'][key][name]),'margin precision overlap')
    derived=source['derived_ball'];r=F(derived['radius'])
    rc=binary(source['sharp_radius'][1]['C'])
    check(r==F(1,8192) and r<=rc.lo<2*r and derived['power_of_two']==-13,'explicit power-of-two rounding')
    v=case(y['h'],r,1,R,y['env'])
    for name,z in v.items():check(decimal(derived['case'][name]).contains(z),'derived '+name)
    check(v['d'].lo>F('1.80e-19') and (v['d']-v['D']/2).lo>0,'derived margin and half-D guarantee')
    check(v['scalar_H_floor'].lo>0 and v['scalar_HA_floor'].hi<0,'derived scalar consumers')
    rep=source['representative'];check((rep['r'],rep['N'])==('1/128',8),'prescribed representative')
    v=y['values'][F(1,128),8,'C']
    for name in ('c','mu'):check(binary(rep[name]).contains(v[name]),'representative '+name)
    cl,ml=binary(rep['c']).lo,binary(rep['mu']).lo
    check(cl>F('1.78e-19') and ml>F('4.25e-10'),'representative lower bounds')
    b2=y['h'][2].absolute()+F(1,128)*sum(y['env'],I(0))
    check(binary(rep['B2']).contains(b2),'same-input C01 derivative envelope')
    check(1+binary(rep['B2']).hi/ml<361 and rep['C01_integer']==361,'valid C01 integer')
    carrier=source['stages'][1]['integrals'][24:]
    check([(z['j'],z['T'],z['Y']) for z in carrier]==[(0,'17/64','0'),(1,'17/64','0'),(0,'17/64','4'),(1,'17/64','4')],'four carrier inputs at chosen representative')
    L=sum((binary(z['complete']) for z in carrier[:2]),I(0));RR=sum((binary(z['complete']) for z in carrier[2:]),I(0))
    check(binary(rep['L']).contains(L) and binary(rep['R2']).contains(RR),'complete carrier sums')
    Lhi,Rhi=binary(rep['L']).hi,binary(rep['R2']).hi
    check(Lhi<F('.068') and Rhi<F('.101'),'carrier reporting bounds')
    N=max(Rhi+6*Lhi,3*Lhi/cl)
    check(decimal(rep['Nbar_upper']).hi>=N and N<F('1.14e18'),'full preparation and second-moment ceiling')
    delta2=9*F('4.25e-10')**7/(2048*F(22,7)**2*F('1.14e18')**3)
    check(delta2>F('2.7e-62')**2,'conservative exact-coefficient all-time energy floor')
    cost=source['cost'];keys={(z['kind'],z['j'],z['T'],z['Y']) for z in all_integrals}
    check(len(keys)==28 and len(all_integrals)==52 and sum(z['callbacks'] for z in all_integrals)==31700,'analytic acquisition counts')
    check(len(panels)==4 and sum(z['count'] for z in panels)==4096,'actual panel work')
    check(cost['distinct_analytic_integrands']==28 and cost['analytic_calls']==52 and cost['analytic_callbacks']==31700,'stored analytic counts')
    check(cost['panel_acquisitions']==4 and cost['panel_range_evaluations']==4096,'stored panel counts')
    check(cost['analytic_seconds']==sum(z['seconds'] for z in all_integrals) and cost['incremental_ibp_panel_seconds']==sum(z['seconds'] for z in panels),'timing sums')
    check(source['elapsed_seconds']<1200 and max(z['callbacks'] for z in all_integrals)==732,'time and maximum callbacks')
    check(all(tail(F(1,2),n,F(1))==F(n+3,2**n) for n in DEGREES),'general total-degree tail normalization')
    check(F(64)*F(41,128)+F(3,2)==22 and F(64)*F(21,64)+2==23,'exact endpoint phases')
    result=dict(task='FCG-E02 R5',date='2026-10-30',prepared_for='Edward Baker',llm_assistance='Substantial; internal same-assistant numerical assessment, shared premises',model='gpt-6.1-sol',effort='ultra',chat='0047',thread_id='01a18d3a-0de3-7781-b7e1-79a42cf0a6fd',packet=dict(path=PACKET,sha256=PACKET_SHA),inputs=hashes,script_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),method='Exact Fraction arithmetic on binary midpoint/radius inputs; decimal output containment; 512-bit rational square-root enclosures. Source integrator never imported or run.',checks_passed=checks,stages=stages,cost=cost,acquisition_replayed=False,manuscript_writes=False,reporting_bounds=dict(c_gt='1.78e-19',mu_gt='4.25e-10',Nbar_lt='1.14e18',energy_gt='2.7e-62',C01_integer=361,derived_radius='1/8192'),limits='Arithmetic reconciliation and code/proof inspection do not independently revalidate Acb quadrature or recompute panel ranges. No specialist/formal/implementation independence.')
    a.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(status='passed',checks=checks,rows=72,frozen_inputs=20,acquisition_replayed=False)))

if __name__=='__main__':main()
