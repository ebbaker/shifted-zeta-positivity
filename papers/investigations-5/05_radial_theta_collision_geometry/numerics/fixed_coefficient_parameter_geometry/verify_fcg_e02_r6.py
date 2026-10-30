#!/usr/bin/env python3
"""Frozen FCG-E02 R6 audit; exact saved intervals plus one optional panel replay.

30 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Actual assessment model gpt-6.1-sol, effort ultra, verified from this agent's
local turn_context. Different Sol agent from E01 R3; inherited premises and
complete-source inputs remain shared. No specialist or formal independence.

Only --output is written. --replay evaluates exactly the saved 256 panels at
256 and 384 bits, no refinement/cases/source acquisition, within 120 seconds.
"""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
from decimal import Decimal, localcontext
from fractions import Fraction as F
from hashlib import sha256
import json
from math import factorial
from pathlib import Path
import re
import signal
import sys
import time

BASE = 'papers/investigations-5/05_radial_theta_collision_geometry'
SUB = 'fixed_coefficient_parameter_geometry'
PACKET = BASE+'/research-progress/handoffs/'+SUB+'/FCG-E02_R6_PRIMITIVE_ABSOLUTE_PAYMENT_ASSESSMENT_20261030.md'
PACKET_SHA = 'c6d01412c5de5ccfd7c4875f712327bd4e3cf40e3458dc39b8d989c87aa1e52c'
R2 = BASE+'/numerics/'+SUB+'/fcg_e01_r2_adaptive_ibp_20261030.json'
R3 = BASE+'/numerics/'+SUB+'/fcg_e01_r3_primitive_absolute_payment_20261030.json'
SCRIPT3 = BASE+'/numerics/'+SUB+'/execute_fcg_e01_r3.py'
RADII = (F(1,64),F(1,128),F(1,256))
DEGREES = (1,2,4,8)
R = F(1,32)

class I:
    def __init__(self,a,b=None):
        if isinstance(a,I): self.lo,self.hi=a.lo,a.hi
        else: self.lo,self.hi=F(a),F(a if b is None else b)
        assert self.lo<=self.hi
    def __add__(self,b):
        b=I(b);return I(self.lo+b.lo,self.hi+b.hi)
    __radd__=__add__
    def __neg__(self):return I(-self.hi,-self.lo)
    def __sub__(self,b):return self+-I(b)
    def __rsub__(self,b):return I(b)+-self
    def __mul__(self,b):
        b=I(b);v=[x*y for x in (self.lo,self.hi) for y in (b.lo,b.hi)]
        return I(min(v),max(v))
    __rmul__=__mul__
    def __truediv__(self,b):
        b=I(b);assert not b.lo<=0<=b.hi
        return self*I(1/b.hi,1/b.lo)
    def __pow__(self,n):
        assert n>=0 and isinstance(n,int)
        if not n:return I(1)
        if n==2:
            a=self.absolute();return I(a.lo*a.lo,a.hi*a.hi)
        return (self**2)**(n//2) if not n%2 else self*(self**(n-1))
    def absolute(self):
        return I(0 if self.lo<=0<=self.hi else min(abs(self.lo),abs(self.hi)),max(abs(self.lo),abs(self.hi)))
    def contains(self,b):
        b=I(b);return self.lo<=b.lo and b.hi<=self.hi
    def overlaps(self,b):return self.lo<=b.hi and b.lo<=self.hi
    def exact(self):return {'lower_exact':str(self.lo),'upper_exact':str(self.hi)}

def dyadic(x):
    m,e=int(x[0]),int(x[1]);return F(m)*F(2)**e
def binary(d):
    m,r=dyadic(d['mid_binary']),dyadic(d['rad_binary']);assert r>=0
    return I(m-r,m+r)
def textball(s):
    s=s.strip()
    if not s.startswith('['):return I(F(s))
    m,r=[F(x.strip()) for x in s[1:-1].split('+/-')];return I(m-r,m+r)
def dec(q):
    with localcontext() as c:
        c.prec=36;return str(Decimal(q.numerator)/Decimal(q.denominator))
def tail(q,n):return q**(n+1)*((n+2)-(n+1)*q)/(1-q)**2
def mg(h1,b,u3,u4):
    e0=(R**3/6+R**2)*u3+R**2*u4/2
    e1=(R+R**2/2)*u3
    return 2*b.absolute()*e0+(h1.absolute()+R*b.absolute())*e1
def polyd(p):return {k-1:k*v for k,v in p.items() if k}
def plus(p,q):
    out=dict(p)
    for k,v in q.items():out[k]=out.get(k,F(0))+v
    return {k:v for k,v in out.items() if v}
def times(p,c):return {k:v*c for k,v in p.items() if v*c}
def logder(p):return plus(polyd(p),{k+1:v/2 for k,v in p.items()})

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--repo',type=Path,required=True)
    ap.add_argument('--output',type=Path,required=True)
    ap.add_argument('--replay',action='store_true')
    ap.add_argument('--record-prior-replay-export-failure',action='store_true',
                    help='Record the observed prior replay assertions/export failure, without inventing lost numerical outputs or repeating evaluations.')
    a=ap.parse_args();root=a.repo.resolve()
    assert not (a.replay and a.record_prior_replay_export_failure),'do not repeat the prior bounded replay'
    assert not a.output.exists(),'preserve earlier assessment record'
    checks=[]
    def check(ok,label):
        if not ok:raise AssertionError(label)
        checks.append(label)
    packet=(root/PACKET).read_bytes()
    check(sha256(packet).hexdigest()==PACKET_SHA,'assessment packet identity')
    frozen=re.findall(r'\| `([^`]+)` \| `([0-9a-f]{64})` \|',packet.decode())
    check(len(frozen)==10,'ten frozen inputs')
    hashes=[]
    for p,h in frozen:
        data=(root/p).read_bytes();got=sha256(data).hexdigest()
        check(got==h,'frozen identity '+p)
        check(len(data)<1048576,'frozen file below 1 MiB '+p)
        hashes.append({'path':p,'sha256':got,'bytes':len(data)})
    d2=json.loads((root/R2).read_text());d3=json.loads((root/R3).read_text())
    check(d3['script_sha256']==sha256((root/SCRIPT3).read_bytes()).hexdigest(),'execution script record identity')
    check(d3['terminal_status']=='certified_domination_of_specified_class','R3 terminal result')
    check(d3['model']=='gpt-6.1-sol' and d3['effort']=='ultra','R3 recorded model and effort')
    check(d3['fixed']['tau']=='1/4' and d3['fixed']['a']=='64' and d3['fixed']['R']=='1/32','frozen physical center and outer radius')
    check(d3['fixed']['I']==['1/32','1/4'],'frozen witness interval')
    check(d3['fixed']['radii']==[str(x) for x in RADII] and d3['fixed']['degrees']==list(DEGREES),'frozen consumer cases')
    check([s['bits'] for s in d2['stages']]==[256,384] and [s['bits'] for s in d3['stages']]==[256,384],'two fixed binary precision stages')

    # Independent rational derivation of (d^2/du^2-1)[u^3 exp(u^2/4) sin64u].
    p={3:F(1)};dp=logder(p);ddp=logder(dp)
    sinpoly=plus(ddp,times(p,-4097));cospoly=times(dp,128)
    check(sinpoly=={1:F(6),3:-F(8187,2),5:F(1,4)},'exact Q sine polynomial')
    check(cospoly=={2:F(384),4:F(64)},'exact Q cosine polynomial')
    atan=lambda z,n:sum(((-1)**k*z**(2*k+1)/F(2*k+1) for k in range(n+1)),F(0))
    piL=4*(atan(F(1,2),3)+atan(F(1,3),3))
    piU=4*(atan(F(1,2),4)+atan(F(1,3),4))
    check(piL>F(157,50) and piU<F(22,7),'alternating arctangent pi bounds')
    check(F(3,2)*F(22,7)<5 and 6<2*F(157,50),'[5,6] inside fourth trig quadrant')
    check(5-F(3,2)*F(22,7)==F(2,7) and 5-F(3,2)*F(157,50)<F(1,2),'cos5 small argument bounds')
    check(2*F(157,50)-6==F(7,25) and 2*F(22,7)-6==F(2,7),'minus sin6 argument bounds')
    check(F(2,7)-F(1,48)==F(89,336)>F(1,4),'cos5 lower polynomial')
    check(F(7,25)-F(4,1029)>F(1,4),'minus sin6 lower polynomial')
    lo,hi=F(5,64),F(3,32)
    derivative_lower=F(24561,2)*lo**2-6-F(5,4)*hi**4
    check(derivative_lower>0,'A monotonicity on rational interval')
    Aval=F(8187,2)*lo**3-6*lo-lo**5/4
    check(Aval==F(6370218955,4294967296)>F(7,5),'A exact rational endpoint')
    check(384*lo**2==F(75,32)>F(23,10),'B endpoint lower value')
    check((F(7,5)+F(23,10))/4==F(37,40),'Q lower value')
    x=F(3,8);e38=1+x+x*x/(2*(1-x/3))
    check(e38==F(163,112),'positive exponential Taylor tail at 3/8')
    eexpo=F(22,7)*e38-lo
    check(eexpo==F(14099,3136)<F(9,2),'primitive negative exponent lower payment')
    eup=1+1+F(1,2)+F(1,6)+F(1,24)/(1-F(1,5))
    check(eup==F(87,32)<F(11,4)<F(25,9),'positive exponential Taylor tail at one')
    check(F(11,4)**4*F(5,3)==F(73205,768)<100,'exp(9/2) upper bound below100')
    jrat=F(37,256000)
    check(hi-lo==F(1,64) and (hi-lo)*F(1,100)*F(37,40)==jrat,'interval length and rational integral lower bound')
    hfloor=F('4.18e-10');mceil=F('2.17e-16')
    lrat=R*hfloor*jrat/8
    check(lrat==F(7733,32768000000000000000)>mceil,'final rational witness value and strict baseline gap')
    elementary={'pi_lower_exact':str(piL),'pi_upper_exact':str(piU),'A_derivative_lower_exact':str(derivative_lower),'A_endpoint_exact':str(Aval),'J_lower_strict_exact':str(jrat),'h1_lower_strict_exact':str(hfloor),'M_upper_strict_exact':str(mceil),'payment_lower_strict_exact':str(lrat),'payment_lower_decimal':dec(lrat)}

    stage_results=[]
    evaluations=0
    for s2,s3 in zip(d2['stages'],d3['stages']):
        bits=s3['bits'];bl=s3['baseline'];f=s3['final'];label=str(bits)
        jets={v['j']:v['complete'] for v in s2['integrals'] if v['kind']=='jet'}
        selected={v['j']:v['selected_min'] for v in s2['panel_acquisitions']}
        names=[('h1',jets[1]),('b',jets[2]),('U3',selected[3]),('U4',selected[4])]
        decoded={}
        for name,original in names:
            key=name+'_complete_saved'
            check(bl[key]==original,label+' original binary '+name+' preserved')
            decoded[name]=binary(bl[name+'_decoded'])
            check(decoded[name].contains(binary(original)),label+' decoded '+name+' encloses all saved bits')
        h1,b,u3,u4=[decoded[k] for k in ['h1','b','U3','U4']]
        check(h1.hi<0 and b.hi<0 and u3.lo>0 and u4.lo>0,label+' source signs')
        check(h1.absolute().lo>hfloor,label+' rational-witness complete h1 endpoint')
        M=binary(bl['M_G_IBP']);exactM=mg(h1,b,u3,u4)
        check(M.contains(exactM),label+' serialized M contains exact reconstructed formula')
        check(M.hi<mceil,label+' rational-witness reconstructed M endpoint')
        rows=[r for p in s2['passes'] for r in p['rows'] if r['rule']=='C']
        check(len(rows)==12 and {(r['r'],r['N']) for r in rows}=={(str(r),n) for r in RADII for n in DEGREES},label+' all twelve rule C cases')
        # Saved rows contain displayed values only. They enclose the reconstructed binary baseline.
        for row in rows:
            tag=label+' C '+row['r']+' '+str(row['N'])
            check(row['outer']=='1/32' and textball(row['M_G']).contains(M),tag+' text baseline encloses binary reconstruction')
            r,n=F(row['r']),row['N'];tf=tail(r/R,n)
            check(textball(row['tail_factor']).contains(I(tf)),tag+' exact tail factor')
            h={j:binary(v) for j,v in jets.items()}
            D=(h[1]**2-2*h[2]*h[0]).absolute();tp=2*h[2]**2*r
            def q(m,k):
                if (m,k) in ((0,0),(0,1),(0,2),(1,0)):return I(0)
                return (-1)**m*h[2*m+k]/(factorial(m)*factorial(k))
            finite=I(0)
            for degree in range(1,n+1):
                for m in range(degree+1):
                    k=degree-m
                    finite+=(h[2]*(k-2)*q(m,k)+h[1]*(k+1)*q(m,k+1)).absolute()*r**degree
            for name,v in [('D',D),('time',tp),('finite_sum',finite)]:
                check(textball(row[name]).contains(v),tag+' unchanged '+name)
        check(len(s3['attempts'])==1,label+' no refinement')
        attempt=s3['attempts'][0];panels=attempt['panel_contributions']
        check(attempt['panel_count']==attempt['range_evaluations']==256,label+' exactly256 panels')
        width=F(attempt['width_exact'])
        check(width==F(7,8192) and F(1,32)+256*width==F(1,4),label+' exact complete panel coverage')
        check([p['index'] for p in panels]==list(range(256)),label+' panel indices contiguous and unique')
        checksum=sha256(json.dumps(panels,sort_keys=True,separators=(',',':')).encode()).hexdigest()
        check(checksum==attempt['panel_contributions_sha256'],label+' actual panel payload identity')
        aggregate=sum((binary(p['contribution']) for p in panels),I(0))
        J=binary(attempt['J_I'])
        check(J.contains(aggregate),label+' serialized aggregate contains exact sum of all panel intervals')
        check(attempt['J_I']==f['J_I'] and attempt['comparison']==f,label+' final equals accepted attempt')
        L=binary(f['L_I']);difference=binary(f['difference']);gap=binary(f['endpoint_gap'])
        check(L.contains(R*h1.absolute()*J/8),label+' L contains exact complete h1 times panel integral')
        check(difference.contains(L-M),label+' difference exact interval containment')
        exactgap=L.lo-M.hi
        check(gap.contains(I(exactgap)) and gap.lo>0,label+' strict endpoint cost gap')
        check(L.lo>F('8.98e-15') and M.hi<F('2.17e-16'),label+' conservative stated L and M bounds')
        ratio=L.lo/M.hi
        check(ratio>F('41.46'),label+' exact endpoint ratio strictly above41.46')
        check(binary(f['ratio']).contains(L/M),label+' divided ratio enclosure only')
        check(f['L_lower_strictly_above_M_upper'] and f['accepted_M_positive'] and M.lo>0,label+' reported comparison flags')
        consumers=s3['consumer_cost_lower_bounds']
        check(len(consumers)==12 and {(v['r'],v['N']) for v in consumers}=={(str(r),n) for r in RADII for n in DEGREES},label+' all twelve matched consumer differences')
        for c in consumers:
            tag=label+' cost '+c['r']+' '+str(c['N'])
            q=F(c['r'])/R;tf=tail(q,c['N'])
            check(F(c['q'])==q and F(c['tail_factor_exact'])==tf and tf>0,tag+' exact T_N')
            product=binary(c['cost_gap_product_enclosure']);lower=binary(c['certified_lower_bound'])
            # lower() rounds the dyadic gap downward, possibly by less than one ulp.
            check(product.overlaps(I(gap.lo*tf)),tag+' product reconciles saved gap lower endpoint')
            check(lower.lo>0 and lower.hi<=exactgap*tf,tag+' serialized lower bound is positive and valid')
            check(lower.lo<=product.lo and lower.hi<=product.hi,tag+' lower extraction is conservative')
        check(0<=attempt['Q_zero_crossing_panels']<=256,label+' zero-crossing count in range')
        check(0<=attempt['seconds']<=s3['arithmetic_seconds']<=120,label+' measured local stage time in cap')
        evaluations+=attempt['range_evaluations']
        stage_results.append({'bits':bits,'h1_absolute':h1.absolute().exact(),'M_IBP':M.exact(),'J_I':J.exact(),'L_I':L.exact(),'L_lower_decimal':dec(L.lo),'M_upper_decimal':dec(M.hi),'endpoint_ratio_lower_exact':str(ratio),'endpoint_ratio_lower_decimal':dec(ratio),'endpoint_gap_exact':str(exactgap),'original_C_rows_checked':len(rows),'consumer_cost_rows_checked':len(consumers),'panels_checked':len(panels),'zero_crossings_recorded':attempt['Q_zero_crossing_panels'],'panel_aggregate_contains_exact_sum':True})
    for key,fn in [('J_I',lambda s:binary(s['final']['J_I'])),('L_I',lambda s:binary(s['final']['L_I'])),('M_G_IBP',lambda s:binary(s['baseline']['M_G_IBP'])),('h1',lambda s:binary(s['baseline']['h1_decoded'])),('b',lambda s:binary(s['baseline']['b_decoded']))]:
        check(fn(d3['stages'][0]).overlaps(fn(d3['stages'][1])) and d3['cross_precision_overlaps'][key],'exact cross-precision overlap '+key)
    check(evaluations==512==d3['cost']['range_evaluations'],'512 recorded ranges and no refinement')
    check(d3['limits']['total_range_evaluations']==3584 and d3['limits']['total_arithmetic_seconds']==120,'issued execution work caps')
    check(sum(s['arithmetic_seconds'] for s in d3['stages'])<=d3['cost']['arithmetic_seconds']<120,'recorded total local arithmetic time')
    for item in d3['inputs']:
        p,h=item['path'],item['sha256']
        check(sha256((root/p).read_bytes()).hexdigest()==h,'R3 own input hash '+p)

    replay={'performed':False,'new_range_evaluations':0,'new_source_acquisition':False}
    if a.replay:
        import flint
        from flint import arb,ctx
        start=time.monotonic();count=0;replayed=[]
        def alarm(signum,frame):raise TimeoutError('bounded replay exceeded120 seconds')
        signal.signal(signal.SIGALRM,alarm);signal.setitimer(signal.ITIMER_REAL,120)
        def ar(q):return arb(q.numerator)/q.denominator
        def ai(v):return arb((int(v['mid_binary'][0]),int(v['mid_binary'][1])),(int(v['rad_binary'][0]),int(v['rad_binary'][1])))
        def encode(v):
            m,e=v.mid().man_exp();r,re=v.rad().man_exp()
            return {'mid_binary':[str(m),int(e)],'rad_binary':[str(r),int(re)]}
        try:
            for s in d3['stages']:
                ctx.prec=s['bits'];attempt=s['attempts'][0];width=F(7,8192);total=arb(0);cross=0
                for k,panel in enumerate(attempt['panel_contributions']):
                    check(count<512 and time.monotonic()-start<120,'independent replay finite limit '+str(count))
                    left=F(1,32)+k*width;u=arb(ar(left+width/2),ar(width/2));u2=u*u
                    # Independently grouped Horner expression for the already-combined Q.
                    q=u*((6+u2*(-ar(F(8187,2))+u2/4))*(64*u).sin()+u*(384+64*u2)*(64*u).cos())
                    cross+=int(q.contains(0))
                    ab=abs(q)
                    value=(u+u2/4-arb.pi()*(4*u).exp()).exp()*ab*ar(width)
                    check(binary(encode(value)).overlaps(binary(panel['contribution'])),str(s['bits'])+' replay panel overlaps stored enclosure '+str(k))
                    total+=value;count+=1
                check(total.overlaps(ai(attempt['J_I'])),str(s['bits'])+' independent full panel aggregate overlap')
                check(cross==attempt['Q_zero_crossing_panels'],str(s['bits'])+' independent zero-crossing count')
                bl=s['baseline'];h,b,u,v=[ai(bl[k+'_complete_saved']) for k in ['h1','b','U3','U4']]
                z=ar(R);e0=(z**3/6+z*z)*u+z*z*v/2;e1=(z+z*z/2)*u
                M=2*abs(b)*e0+(abs(h)+z*abs(b))*e1
                check(encode(M)=={k:bl['M_G_IBP'][k] for k in ['mid_binary','rad_binary']},str(s['bits'])+' baseline binary reconstruction reproduces execution')
                check(all(M.str(65,more=True)==r['M_G'] for p in d2['stages'][0 if s['bits']==256 else 1]['passes'] for r in p['rows'] if r['rule']=='C'),str(s['bits'])+' binary baseline reproduces twelve printed C rows')
                replayed.append({'bits':s['bits'],'panels':256,'Q_zero_crossing_panels':cross,'J_I':encode(total),'J_I_display':total.str(50,more=True),'aggregate_overlaps_saved':True,'all_panel_enclosures_overlap_saved':True,'baseline_reproduced_binary_identically':True})
        finally:signal.setitimer(signal.ITIMER_REAL,0)
        check(count==512,'independent replay exactly512 range evaluations')
        replay={'performed':True,'new_range_evaluations':count,'seconds':time.monotonic()-start,'precisions':[256,384],'panels_per_precision':256,'refinement':False,'new_source_acquisition':False,'formula':'independent Horner grouping of complete Q, real interval ranges; same I and exact widths','python_flint':flint.__version__,'flint':getattr(flint,'__FLINT_VERSION__','unavailable'),'stages':replayed}
    if a.record_prior_replay_export_failure:
        replay={'performed':True,'new_range_evaluations':512,'precisions':[256,384],
                'panels_per_precision':256,'refinement':False,'new_source_acquisition':False,
                'fresh_range_evaluations_during_record_repair':0,
                'formula':'independent Horner grouping of complete Q, real interval ranges at exactly the original panels',
                'observed_assertions_status':'All replay panel overlaps, aggregate overlaps, zero-crossing counts, binary baseline reproductions, exact512 count, and ending frozen-input identities passed before final report serialization failed.',
                'export_status':'failed_after_assertions',
                'reporting_error':'TypeError: Object of type fmpz is not JSON serializable, at final json.dumps',
                'pre_reporting_fix_verifier_sha256':'2ff8feebf19812d21f619763edb7a9dfdfdc6acc9025563e8cc1ed975f46fbc7',
                'numeric_outputs_retained':False,'replay_aggregate_intervals':None,'measured_replay_seconds':None,
                'limitation':'Observed execution/control-flow evidence only; no machine-readable replay-range receipt or lost numerical values are inferred. Main acceptance rests on the exact saved-input audit and analytic proof. Replay was not repeated.',
                'reporting_repair':'Convert binary exponents to ordinary Python int before JSON serialization; no source/proof/input correction.'}
    for p,h in frozen:check(sha256((root/p).read_bytes()).hexdigest()==h,'end-of-assessment frozen identity '+p)
    result={'task':'FCG-E02 R6','date':'2026-10-30','prepared_for':'Edward Baker','llm_assistance':'Substantial; internal shared-premise different-agent Sol review of Astra proof and Sol implementation, no specialist or formal independence','model':'gpt-6.1-sol','effort':'ultra','model_provenance':'Own local turn_context model/effort; thread01a18dc5-e74e-7da3-9dee-77608c86007b, turn01a18dcc-4e1b-7863-8f90-7cfe431806c7','separate_chat_registration':False,'assessment_packet_sha256':PACKET_SHA,'verifier_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),'input_identities':hashes,'rational_witness':elementary,'stages':stage_results,'optional_independent_formula_replay':replay,'exact_assertions_passed':len(checks),'check_labels':checks,'dispositions':[{'obligation':i,'decision':'accept_without_mathematical_correction'} for i in range(1,9)],'terminal_status':'accepted_absolute_payment_route_inactive_in_stated_class','scope':'One actual-theta center(1/4,64), R1/32, U>=1 or infinity; modulus before source integration and full finite boundary/exterior payment; no signed panel/cross-piece/Taylor-subtracted/smaller-cutoff conclusion','continuation':'B03 R7 conceptual question only: subtract known total-degree<=4 kernel terms, compare remaining primitive tail at r1/128,N4 with accepted IBP and identical-information direct source remainder; B04 remains gated; not initiated','recorded_utc':datetime.now(timezone.utc).isoformat()}
    payload=json.dumps(result,indent=2)+'\n'
    assert len(payload.encode())<1048576,'assessment record below1 MiB'
    a.output.write_text(payload)
    print(json.dumps({'status':result['terminal_status'],'assertions':len(checks),'replay_ranges':replay['new_range_evaluations'],'record_bytes':len(payload.encode()),'ratios':[s['endpoint_ratio_lower_decimal'] for s in stage_results]}))

if __name__=='__main__':main()
