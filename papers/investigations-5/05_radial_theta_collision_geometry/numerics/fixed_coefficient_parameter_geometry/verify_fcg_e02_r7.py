#!/usr/bin/env python3
"""FCG-E02 R7: exact saved-input assessment; no source evaluation.

Prepared for Edward Baker with substantial LLM assistance, 30 October 2026.
Actual assessment model gpt-6.1-sol, reasoning effort ultra, from local turn
metadata. Internal LLM assessment with inherited premises; no specialist or
formal independence. Uses only standard-library Fraction/int arithmetic.
Optional --output /private/tmp/NAME.json directs all output outside the repo.
"""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
from decimal import Decimal, localcontext, ROUND_FLOOR, ROUND_CEILING
from fractions import Fraction as F
from hashlib import sha256
from math import factorial, isqrt
from pathlib import Path
import json
import platform
import re
import signal
import sys
import time

BASE=Path('papers/investigations-5/05_radial_theta_collision_geometry')
SUB='fixed_coefficient_parameter_geometry'
PACKET=BASE/'research-progress/handoffs'/SUB/'FCG-E02_R7_TAYLOR_SUBTRACTED_ASSESSMENT_20261030.md'
PACKET_SHA='844bff883958ea276a897b74500b1ad30ae6de047dce0548e6dd4d4fc30260f6'
SOURCE=BASE/'numerics'/SUB/'fcg_e01_r2_adaptive_ibp_20261030.json'
OUT=BASE/'numerics'/SUB/'fcg_e02_r7_taylor_subtracted_assessment_20261030.json'
TAU=F(1,4); A=F(64); R=F(1,32); r=F(1,128); DELTA=F(511,128); T0=F(17,64)
CHECKS=[]
def check(ok,name):
    if not ok: raise ArithmeticError(name)
    CHECKS.append(name)

def frac(x): return x if isinstance(x,F) else F(x)
class I:
    def __init__(self,lo,hi=None):
        self.lo,self.hi=frac(lo),frac(lo if hi is None else hi)
        if self.lo>self.hi: raise ArithmeticError('reversed exact interval')
    def __add__(self,o):
        o=iv(o);return I(self.lo+o.lo,self.hi+o.hi)
    __radd__=__add__
    def __neg__(self):return I(-self.hi,-self.lo)
    def __sub__(self,o):return self+-iv(o)
    def __rsub__(self,o):return iv(o)+-self
    def __mul__(self,o):
        o=iv(o);v=[self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi];return I(min(v),max(v))
    __rmul__=__mul__
    def __truediv__(self,o):
        o=iv(o)
        if o.lo<=0<=o.hi:raise ArithmeticError('interval division through zero')
        return self*I(1/o.hi,1/o.lo)
    def __rtruediv__(self,o):return iv(o)/self
    def __pow__(self,n):
        if n==0:return I(1)
        if n==2:return self.square()
        z=I(1)
        for _ in range(n):z=z*self
        return z
    def square(self):
        if self.lo>=0:return I(self.lo*self.lo,self.hi*self.hi)
        if self.hi<=0:return I(self.hi*self.hi,self.lo*self.lo)
        return I(0,max(self.lo*self.lo,self.hi*self.hi))
    def absolute(self):
        if self.lo>=0:return self
        if self.hi<=0:return -self
        return I(0,max(-self.lo,self.hi))
    def contains(self,o):
        o=iv(o);return self.lo<=o.lo and self.hi>=o.hi
    def overlaps(self,o):
        o=iv(o);return max(self.lo,o.lo)<=min(self.hi,o.hi)

def iv(x):return x if isinstance(x,I) else I(x)
def dyad(z):return F(int(z[0]))*F(2)**int(z[1])
def dec(x):
    m,rad=dyad(x['mid_binary']),dyad(x['rad_binary']);return I(m-rad,m+rad)
def display(x):
    def val(q,mode):
        with localcontext() as c:
            c.prec=18;c.rounding=mode
            return str(Decimal(q.numerator)/Decimal(q.denominator))
    x=iv(x);return '['+val(x.lo,ROUND_FLOOR)+', '+val(x.hi,ROUND_CEILING)+']'
def rec(x):
    x=iv(x);return {'lower':str(x.lo),'upper':str(x.hi),'outward_decimal':display(x)}
def printed(s):
    if s.startswith('['):
        m,rad=s[1:-1].split(' +/- ');return I(F(m)-F(rad),F(m)+F(rad))
    return I(F(s))
def sqrt_bound(q,up=False):
    check(q>=0,'sqrt argument nonnegative')
    grid=10**80;z=isqrt(q.numerator*grid*grid//q.denominator)
    lo=F(z,grid)
    check(lo*lo<=q,'sqrt lower square')
    hi=lo if lo*lo==q else F(z+1,grid)
    check(hi*hi>=q,'sqrt upper square')
    return hi if up else lo
def sqrt_iv(x):return I(sqrt_bound(x.lo),sqrt_bound(x.hi,True))

def poly(p):return {k:frac(v) for k,v in p.items() if v}
def add(p,q):
    z=dict(p)
    for k,v in q.items():z[k]=z.get(k,F(0))+v
    return poly(z)
def scale(p,c):return poly({k:v*c for k,v in p.items()})
def mul(p,q):
    z={}
    for k,v in p.items():
        for j,w in q.items():z[k+j]=z.get(k+j,F(0))+v*w
    return poly(z)
def power(p,n):
    z={0:F(1)}
    for _ in range(n):z=mul(z,p)
    return z
def deriv(p):return poly({k-1:k*v for k,v in p.items() if k})
def Lp(p):
    D={0:r,1:2*(TAU+r)};Da=add(D,{0:A})
    return add(add(deriv(deriv(p)),scale(mul(Da,deriv(p)),2)),
               mul(add(mul(Da,Da),{0:2*r+abs(2*TAU-1)}),p))
def C(p):
    check(p.get(0,F(0))==0,'C polynomial zero constant')
    check(all(k>=1 and v>=0 for k,v in p.items()),'C positive polynomial')
    return sum((v*F(factorial(k-1))/DELTA**(k-1) for k,v in p.items()),F(0))
def prec(p):return {str(k):str(v) for k,v in sorted(p.items())}

def constants():
    w={1:r,2:r}
    pb=add(scale(power(w,5),F(2,120)),scale(mul({1:r},power(w,4)),F(1,24)))
    ph=scale(mul({1:F(1)},power(w,5)),F(1,120))
    ps=scale(power(w,5),F(1,120))
    polys={'pb':pb,'ph':ph,'Lp_pb':Lp(pb),'Lp_ph':Lp(ph),'pS':ps}
    expected={'pb':F(1989705625478911,217205108433542126803400320),
              'ph':F(881126540079433,173424703764906291869589943),
              'Lp_pb':F(247535379492981804236892593407,5575489793485205047839689437222010880),
              'Lp_ph':F(183125734587832495414844581961,7419466886643072342307503391719915520),
              'pS':F(532944860489673,217205108433542126803400320)}
    caps=dict(zip(polys,map(F,('9.161e-12','5.081e-12','4.440e-8','2.469e-8','2.454e-12'))))
    vals={k:C(p) for k,p in polys.items()}
    for k in vals:
        check(vals[k]==expected[k],'exact constant '+k)
        check(vals[k]<caps[k],'strict constant cap '+k)
    check(min(pb)==5 and max(pb)==10 and min(ph)==6 and max(ph)==11,'direct degrees/vanishing')
    check(min(polys['Lp_pb'])==3 and max(polys['Lp_pb'])==12,'Lp_pb degree/vanishing')
    check(min(polys['Lp_ph'])==4 and max(polys['Lp_ph'])==13,'Lp_ph degree/vanishing')
    # This is rebuilt from w rather than the printed coefficient lists.
    cb=r**5/120
    check(pb=={j+5:cb*v for j,v in enumerate((7,30,50,40,15,2))},'pb printed list independently matches')
    check(ph=={j+6:cb*v for j,v in enumerate((1,5,10,10,5,1))},'ph printed list independently matches')
    for name in ('pb','ph'):
        diff=add(polys['Lp_'+name],scale(polys[name],-A*A))
        check(all(v>=0 for v in diff.values()),'coefficientwise Lp-a2 '+name)
    bc,hc,xc=F('1.18e-11'),F('4.20e-10'),F('0.0096')
    td=xc*(bc*caps['pb']+hc*caps['ph'])
    tp=xc*(bc*caps['Lp_pb']+hc*caps['Lp_ph'])/72
    ts=xc*caps['pS'];ta=xc*caps['ph']
    check(td<F('2.153e-23'),'coarse direct tail cap')
    check(tp<F('1.453e-21'),'coarse primitive tail cap')
    check(ts<F('2.356e-14') and ta<F('4.878e-14'),'coarse scalar tail caps')
    coarseD=F('1.905e-19')-F('2.141e-24')-F('5.722e-22')-F('2.153e-23')
    coarseP=F('1.905e-19')-F('2.141e-24')-F('5.722e-22')-F('1.453e-21')
    check(coarseD>F('1.899e-19') and coarseP>F('1.884e-19'),'coarse final margins (14)')
    return vals,{'polynomials':{k:prec(p) for k,p in polys.items()},
        'exact_constants':{k:str(v) for k,v in vals.items()},
        'strict_caps':{k:str(v) for k,v in caps.items()},
        'coarse_cap_payments':{'TD':str(td),'TP':str(tp),'H_tail':str(ts),'HA_tail':str(ta),
                               'dD_from_coarse_caps':str(coarseD),'dP_from_coarse_caps':str(coarseP)}}

def moment(source,j,T,Y):
    matches=[z for z in source['stages'][1]['integrals'] if z['kind']=='moment'
             and z['j']==j and z['T']==T and z['Y']==Y]
    check(len(matches)==1,'unique common moment '+str((j,T,Y)))
    z=matches[0];check(z['tail']['guards_pass'],'inherited moment tail guards '+str((j,T,Y)))
    check(dec(z['complete']).lo>0,'positive complete moment '+str((j,T,Y)))
    return dec(z['complete']),z


def stage(s,cs,x1,L,R2):
    h={z['j']:dec(z['complete']) for z in s['integrals'] if z['kind']=='jet' and z['j']<=9}
    check(set(h)==set(range(10)),'full h0..h9 '+str(s['bits']))
    b=h[2];B=b.absolute();eta=h[1].absolute()
    coeffs={}
    def f(m,n):return (-1)**m*h[2*m+n]/(factorial(m)*factorial(n))
    def fa(m,n):return (-1)**m*h[2*m+n+1]/(factorial(m)*factorial(n))
    def q(m,n):return I(0) if (m,n) in ((0,0),(0,1),(0,2),(1,0)) else f(m,n)
    def g(m,n):return b*(n-2)*q(m,n)+h[1]*(n+1)*q(m,n+1)
    finite=I(0);sf=I(0);sfa=I(0)
    for total in range(5):
        for m in range(total+1):
            n=total-m; gg=g(m,n);ff=f(m,n);aa=fa(m,n)
            coeffs[f'{m},{n}']={'f':rec(ff),'fA':rec(aa),'q':rec(q(m,n)),
                 'q_m_nplus1':rec(q(m,n+1)),'g':rec(gg)}
            if total:
                finite+=gg.absolute()*r**total
                sf+=ff.absolute()*r**total
                sfa+=aa.absolute()*r**total
    check(g(0,0).lo==g(0,0).hi==0 and g(0,1).lo==g(0,1).hi==0,'exact cancelled g00 g01')
    D0=h[1].square()-2*b*h[0];D=D0.absolute();timepay=2*b.square()*r
    normalizer=1+h[0].square()+h[1].square()+b.square()
    K2=4*b.square()+(eta+r*B).square();K=sqrt_iv(K2)
    TD=x1*(B*cs['pb']+eta*cs['ph'])
    TP=x1*(B*cs['Lp_pb']+eta*cs['Lp_ph'])/72
    gammaD=finite+TD;gammaP=finite+TP
    dD=D-timepay-gammaD;dP=D-timepay-gammaP
    cD=dD/normalizer;cP=dP/normalizer
    check(B.hi<F('1.18e-11') and eta.hi<F('4.20e-10') and x1.hi<F('0.0096'),'source B eta X1 caps (13)')
    check(D.lo>F('1.905e-19') and finite.hi<F('5.722e-22') and timepay.hi<F('2.141e-24'),'D F4 time caps (13)')
    check(TD.hi<F('2.153e-23') and TP.hi<F('1.453e-21'),'actual paid tail caps')
    check(dD.lo>F('1.899e-19') and dP.lo>F('1.884e-19'),'actual margin caps (14)')
    check(TP.lo>TD.hi,'strict primitive/direct tail order')
    # Formula (11) is a pointwise comparison of the exact same B,eta,X1,
    # not an interval comparison requiring independent endpoint separation.
    tdiff=x1*(B*(cs['Lp_pb']/72-F(512,9)*cs['pb'])+
               eta*(cs['Lp_ph']/72-F(512,9)*cs['ph']))
    check(tdiff.lo>=0,'hatted ratio at least 512/9')
    envelopes={z['j']:dec(z['selected_min']) for z in s['panel_acquisitions']}
    u3,u4=envelopes[3],envelopes[4]
    e0=(R**3/6+R*R)*u3+R*R*u4/2;e1=(R+R*R/2)*u3
    MC=2*B*e0+(eta+R*B)*e1
    factor=F(19,2304);oldtail=MC*factor;oldgamma=finite+oldtail;oldd=D-timepay-oldgamma
    rows=[z for p in s['passes'] for z in p['rows'] if z['rule']=='C']
    check(len(rows)==12 and len({z['M_G'] for z in rows})==1,'twelve common C rows')
    check(all(z['outer']=='1/32' and printed(z['M_G']).contains(MC) for z in rows),'all C rows reconcile M_C')
    oldrow=next(z for z in rows if z['r']=='1/128' and z['N']==4)
    check(printed(oldrow['tail_factor']).contains(factor),'old exact tail factor 19/2304')
    for k,v in (('finite_sum',finite),('time',timepay),('D',D),('tail',oldtail),('Gamma',oldgamma),('d',oldd)):
        check(printed(oldrow[k]).contains(v),'old row reconciliation '+k)
    check(oldd.hi<0 and oldrow['status']=='nonpositive','old N4 negative')
    old8=next(z for z in rows if z['r']=='1/128' and z['N']==8)
    check(printed(old8['d']).lo>0 and old8['status']=='positive','historical stored N8 positive')
    check(TD.hi<oldtail.lo and TP.hi<oldtail.lo,'both new tails below old C')
    htail=x1*cs['pS'];hatail=x1*cs['ph']
    floorH=h[0].absolute()-sf-htail
    floorHA=eta-sfa-hatail
    check(htail.hi<F('2.356e-14') and hatail.hi<F('4.878e-14'),'actual scalar tails')
    check(floorH.lo>0 and floorHA.lo>0,'both same-information scalar floors positive')
    box2=I(floorH.lo**2+floorHA.lo**2)
    boxlower=sqrt_bound(box2.lo)
    mu=dD/K
    check(mu.lo>0 and cD.lo>0,'exact-defined cD and mu positive')
    check(boxlower>mu.hi,'direct scalar component box stronger than row mu')
    Nbar=max(R2.hi+6*L.hi,3*L.hi/cD.lo)
    check(Nbar>0,'positive carrier Nbar upper')
    # pi<22/7; z^(3/2)>= z*sqrt_lower(z), all exact rational.
    piupper=F(22,7)
    z=mu.lo/(2*Nbar)
    energy=3*mu.lo**2/(16*piupper)*z*sqrt_bound(z)
    B2=B+r*(u3+u4)
    c01upper=1+B2.hi/mu.lo
    c01ceil=-(-c01upper.numerator//c01upper.denominator)
    check(c01ceil>=c01upper and c01ceil-1<c01upper,'C01 exact ceiling')
    check(energy>0,'exact c all-time energy lower positive')
    return {'bits':s['bits'],'h0_h9_complete_binary':{str(z['j']):z['complete'] for z in s['integrals'] if z['kind']=='jet' and z['j']<=9},
        'h0_h9_exact_intervals':{str(k):rec(v) for k,v in h.items()},
        'U3_U4_complete_binary':{str(z['j']):z['selected_min'] for z in s['panel_acquisitions']},
        'coefficients_total_degree_le4':coeffs,
        'row':{k:rec(v) for k,v in {'D0':D0,'D':D,'F4':finite,'time':timepay,'normalizer':normalizer,
              'K_squared':K2,'K':K,'TD':TD,'TP':TP,'GammaD':gammaD,'GammaP':gammaP,
              'dD':dD,'dP':dP,'cD':cD,'cP':cP,'TP_minus_512over9_TD':tdiff}.items()},
        'old_C':{'M_C':rec(MC),'tail_factor_exact':str(factor),'tail':rec(oldtail),
                 'Gamma':rec(oldgamma),'d':rec(oldd),'original_N4_row':oldrow,
                 'historical_N8_row':old8,'N8_policy':'stored positive only; no new N8 calculation or minimum-degree claim',
                 'Gamma_C_minus_D':rec(oldgamma-gammaD),'Gamma_C_minus_P':rec(oldgamma-gammaP)},
        'scalar':{'finite_H':rec(sf),'finite_HA':rec(sfa),'tail_H':rec(htail),'tail_HA':rec(hatail),
                  'floor_H':rec(floorH),'floor_HA':rec(floorHA),'box_norm_lower':str(boxlower),
                  'box_norm_lower_outward':display(boxlower),
                  'no_simple_zero_crossing_exercised':True,'box_lower_exceeds_row_mu_upper':True},
        'flow':{'c_exact_definition':'dD/(1+h0^2+h1^2+b^2), not a rounded replacement',
                'cD':rec(cD),'mu_row':rec(mu),'Nbar_upper':str(Nbar),
                'Nbar_upper_outward':display(Nbar),'energy_lower':str(energy),
                'energy_lower_outward':display(energy),'B2':rec(B2),
                'C01_one_plus_B2_over_mu_lower_upper':str(c01upper),'C01_integer':c01ceil,
                'C01_start':'eventual compact-uniform derivative convergence; no acquired start time',
                'all_time_spatial_start':0,'pi_upper_rational':'22/7'},
        'checks':'all source caps, both degree4 margins, baseline, scalar, flow and C01 accepted'}


def main():
    pa=argparse.ArgumentParser(description=__doc__)
    pa.add_argument('--root',type=Path)
    pa.add_argument('--output',type=Path)
    args=pa.parse_args();root=(args.root or Path(__file__).resolve().parents[5]).resolve();output=args.output or root/OUT
    started=time.monotonic()
    def alarm(sig,frame):raise TimeoutError('120-second exact verifier cap')
    signal.signal(signal.SIGALRM,alarm);signal.setitimer(signal.ITIMER_REAL,120)
    packet=root/PACKET
    check(sha256(packet.read_bytes()).hexdigest()==PACKET_SHA,'frozen E02 R7 packet')
    rows=re.findall(r'\| `([^`]+)` \| `([0-9a-f]{64})` \|',packet.read_text())
    check(len(rows)==9,'nine frozen input hashes')
    inputs=[{'path':str(PACKET),'sha256':PACKET_SHA}]
    for p,h in rows:
        check(sha256((root/p).read_bytes()).hexdigest()==h,'frozen '+p)
        inputs.append({'path':p,'sha256':h})
    source=json.loads((root/SOURCE).read_text())
    check([s['bits'] for s in source['stages']]==[256,384],'original jet/envelope stages')
    check(TAU+r<T0 and DELTA+r==4 and DELTA==F(511,128),'moment exponent arithmetic')
    cs,cr=constants()
    x1,x1source=moment(source,1,'17/64','4')
    l0,l0s=moment(source,0,'17/64','0');l1,l1s=moment(source,1,'17/64','0')
    r0,r0s=moment(source,0,'17/64','4')
    L=l0+l1;R2=r0+x1
    check(dec(source['representative']['L']).contains(L),'inherited complete L reconciles')
    check(dec(source['representative']['R2']).contains(R2),'inherited complete R2 reconciles')
    stages=[stage(s,cs,x1,L,R2) for s in source['stages']]
    for name in ('dD','dP','TD','TP','GammaD','GammaP','cD'):
        def back(z):return I(F(z['lower']),F(z['upper']))
        check(back(stages[0]['row'][name]).overlaps(back(stages[1]['row'][name])), 'two-stage overlap '+name)
    for k in ('floor_H','floor_HA'):
        check(back(stages[0]['scalar'][k]).overlaps(back(stages[1]['scalar'][k])), 'two-stage scalar overlap '+k)
    for x in inputs:check(sha256((root/x['path']).read_bytes()).hexdigest()==x['sha256'],'unchanged at end '+x['path'])
    data={'task':'FCG-E02 R7','date':'2026-10-30','prepared_for':'Edward Baker',
          'model':'gpt-6.1-sol','effort':'ultra','model_provenance':'local implementing agent turn_context model/effort',
          'assessment_agent_thread':'01a18dc8-dee6-7423-a420-5efce432e84c',
          'provenance':'Internal same-Sol/different-agent saved-input assessment; not proof author; shared inherited inputs, no specialist/formal independence.',
          'inputs':inputs,'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
          'fixed':{'tau':str(TAU),'a':str(A),'R':str(R),'r':str(r),'N':4},
          'arithmetic':'Python standard-library Fraction/int only; exact binary dyadics; directed Decimal only for printed summaries',
          'new_source_evaluations':0,'new_quadrature_evaluations':0,
          'common_moment':{'X1':rec(x1),'X1_source_record':x1source,'L':rec(L),'R2':rec(R2),
              'moment_stage_bits':384,'same_X1_reused_both_jet_stages':True,
              'tails':'Complete saved moments include all modes and whole exterior; not two independent acquisitions.'},
          'constants':cr,'stages':stages,
          'obligations':[
              {'number':1,'disposition':'accept','scope':'kernel E4/E3, signed coefficients, complete primitive identity and boundary/uniformity checked analytically'},
              {'number':2,'disposition':'accept','scope':'H0 derivatives, coefficientwise Lp, distinct exact-integral and common-moment comparisons'},
              {'number':3,'disposition':'accept','scope':'all required zero constants, positive complete common X1, no unpaid mode/exterior'},
              {'number':4,'disposition':'accept','scope':'five exact rational constants and all strict coarse caps rebuilt'},
              {'number':5,'disposition':'accept','scope':'new degree4 direct/primitive positive, old degree4 C negative, historical N8 retained'},
              {'number':6,'disposition':'accept with editorial scope clarification','scope':'both scalar Taylor floors positive and scalar-box lower bound exceeds row mu; strongest-consumer optimality is unproved'},
              {'number':7,'disposition':'accept','scope':'exact-c row-mu/C01/all-time carrier bounds from old complete moments'},
              {'number':8,'disposition':'accept','scope':'fixed-degree common-moment limitation and original control/event qualifications'},
              {'number':9,'disposition':'accept','scope':'C04 R4 finite degree reduction, scalar separation, no new acquisition, B04 gated'}],
          'corrections':[{'type':'editorial_scope_clarification','issued_wording':'The strongest matched scalar consumers supplied by these inputs','supported_wording':'Matched scalar Taylor consumers','reason':'No optimality among all consumers from the same inputs has been proved; no displayed formula changes.'}],'terminal_status':'all_nine_obligations_accepted_with_scope_clarification',
          'check_count':len(CHECKS),'checks':CHECKS,
          'scope':'one existing ball only; new C04 R4 direct rule; no minimum degree, new physical region, simple zero, high-frequency schedule, global cover or RH/Newman consequence',
          'runtime':{'python':sys.version,'platform':platform.platform(),'seconds':time.monotonic()-started,'cap_seconds':120},
          'recorded_utc':datetime.now(timezone.utc).isoformat()}
    text=json.dumps(data,indent=2)+'\n'
    if len(text.encode())>=1048576: raise ArithmeticError('JSON exceeds 1 MiB')
    output.write_text(text)
    signal.setitimer(signal.ITIMER_REAL,0)
    print('accepted',len(CHECKS),'checks, seconds',data['runtime']['seconds'],'bytes',len(text.encode()))
    for s in stages:
        print('bits',s['bits'])
        for k in ('TD','TP','GammaD','GammaP','dD','dP','cD'):print(k,s['row'][k]['outward_decimal'])
        print('old d',s['old_C']['d']['outward_decimal'])
        for k in ('floor_H','floor_HA','box_norm_lower_outward'):print(k,s['scalar'][k]['outward_decimal'] if isinstance(s['scalar'][k],dict) else s['scalar'][k])
        print('mu',s['flow']['mu_row']['outward_decimal'],'Nbar',s['flow']['Nbar_upper_outward'],'energy',s['flow']['energy_lower_outward'],'C01',s['flow']['C01_integer'])

if __name__=='__main__':main()
