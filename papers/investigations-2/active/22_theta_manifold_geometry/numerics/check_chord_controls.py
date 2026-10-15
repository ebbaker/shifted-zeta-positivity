#!/usr/bin/env python3
"""Exact collision chord replay. Prepared for Edward Baker, 2026-10-15.
Substantial LLM assistance; coordinating model gpt-6-astra, effort ultra.
Root isolation and all bounds use rational arithmetic. No theta certificate.
"""
from fractions import Fraction as Q
from math import factorial as fac
from pathlib import Path
import argparse, hashlib, json, platform

checks=[]
def check(ok,label):
    if not ok: raise AssertionError(label)
    checks.append(label)

class I:
    def __init__(self,a,b=None): self.a,self.b=Q(a),Q(a if b is None else b)
    def __add__(self,v):
        v=v if isinstance(v,I) else I(v)
        return I(self.a+v.a,self.b+v.b)
    __radd__=__add__
    def __neg__(self): return I(-self.b,-self.a)
    def __sub__(self,v): return self+(-v if isinstance(v,I) else -Q(v))
    def __mul__(self,v):
        v=v if isinstance(v,I) else I(v)
        p=[self.a*v.a,self.a*v.b,self.b*v.a,self.b*v.b]
        return I(min(p),max(p))
    __rmul__=__mul__
    def __truediv__(self,v):
        v=v if isinstance(v,I) else I(v)
        if v.a<=0<=v.b: raise ZeroDivisionError()
        return self*I(1/v.b,1/v.a)
    def pow(self,n):
        if not n: return I(1)
        if n%2: return I(self.a**n,self.b**n)
        return I(0 if self.a<=0<=self.b else min(self.a**n,self.b**n),max(self.a**n,self.b**n))
    def absmax(self): return max(abs(self.a),abs(self.b))

def poly(m,b,s,sign,d):
    p={}
    for n,c in ((m,Q(sign)),(m+1,sign*b)):
        for k in range(n//2+1):
            e=n-2*k-d
            if e>=0: p[e]=p.get(e,Q(0))+c*Q(fac(n),fac(k)*fac(e))*s**k
    return {e:c for e,c in p.items() if c}

def val(p,x): return sum((c*x**e for e,c in p.items()),Q(0))
def enc(p,x): return sum((c*x.pow(e) for e,c in p.items()),I(0))
def ceilq(q,bits=30):
    d=2**bits; return Q(-((-q.numerator*d)//q.denominator),d)
def floorq(q,bits=30):
    d=2**bits; return Q((q.numerator*d)//q.denominator,d)
def bounds(i): return [str(floorq(i.a,40)),str(ceilq(i.b,40))]
def Fprime(r,c): return sum((Q(fac(r),fac(r-l)*fac(2*l-1))*c**(2*l-1) for l in range(1,r+1)),Q(0))

roots=[]; witnesses=[]; worst=[Q(0),Q(0),Q(0)]
inner=parabolic=negative=positive=fixed_endpoint=0
fixed_worst=Q(0)
fixed_negative=fixed_positive=fixed_undecided=0
for m in (2,3,4,5):
    j=m%2; r=(m-j)//2; n=2*r
    for b in (Q(0),Q(1,3),Q(-2,5)):
        lam=b if j==0 else b*Q(m+1,m)
        for sign in (1,-1):
            for exponent in (4,8,12,16,20,24):
                s=Q(1,2**exponent); root=I(-2*s,2*s)
                p=[poly(m,b,s,sign,d) for d in range(4)]
                label=f'm={m},b={b},sign={sign},s={s}'
                check(sign*val(p[j+1],root.a)<0,'root left '+label)
                check(sign*val(p[j+1],root.b)>0,'root right '+label)
                check(1-abs(lam)*(n+1)*2*s>0,'root monotonicity '+label)
                for _ in range(64):
                    mid=(root.a+root.b)/2; v=sign*val(p[j+1],mid)
                    if v==0: root=I(mid); break
                    root=I(mid,root.b) if v<0 else I(root.a,mid)
                check(root.b-root.a<=4*s/Q(2**64),'root width '+label)
                H,Hx=enc(p[0],root),enc(p[1],root)
                W0=enc(p[j],root)
                E=H.pow(2) if j==0 else H.pow(2)+Hx.pow(2)
                check(E.a>0,'central physical E '+label)
                roots.append({'m':m,'j':j,'b':str(b),'sign':sign,'s':str(s),'root':[str(root.a),str(root.b)]})
                for C in (Q(1,2),Q(1),Q(2),Q(4)):
                    ell=C*s/r; y=root+ell; R=2*s+ell
                    check(1-abs(lam)*(n+1)*R>0,'zero-free inner '+label+f',C={C}')
                    W,V=enc(p[j],y),enc(p[j+1],y)
                    check(W.a>0 if sign>0 else W.b<0,'endpoint sign '+label+f',C={C}')
                    slope=V/W; chord=W0*(W-V)/E
                    qe=(slope-C).absmax(); ce=(chord-(1-C)).absmax()
                    worst[0]=max(worst[0],qe/s); worst[1]=max(worst[1],ce/s)
                    check(qe<=128*s,'slope error '+label+f',C={C}')
                    check(ce<=128*s,'chord error '+label+f',C={C}')
                    if C>1:
                        check(chord.b<0,'negative chord '+label+f',C={C}'); negative+=1
                    if C<1:
                        check(chord.a>0,'positive chord '+label+f',C={C}'); positive+=1
                    inner+=1
                    if exponent==24 and sign==1 and b==Q(1,3) and C==2:
                        witnesses.append({'kind':'inner','m':m,'s':str(s),'C':str(C),'slope':bounds(slope),'chord_over_central_E':bounds(chord),'angle_error_upper':str(ceilq(qe,50))})
                for c in (Q(1,2),Q(1)):
                    sqrt_s=Q(1,2**(exponent//2)); y=root+c*sqrt_s; R=2*s+c*sqrt_s
                    check(1-abs(lam)*(n+1)*R>0,'zero-free parabolic '+label+f',c={c}')
                    W,V=enc(p[j],y),enc(p[j+1],y)
                    chord=W0*(W-V)/E; fp=Fprime(r,c)
                    error=(sqrt_s*chord+fp).absmax()
                    worst[2]=max(worst[2],error/sqrt_s)
                    check(error<=128*sqrt_s,'parabolic error '+label+f',c={c}')
                    if exponent>=12: check(chord.b<0,'negative parabolic '+label+f',c={c}')
                    parabolic+=1
                    if exponent==24 and sign==1 and b==Q(1,3) and c==1:
                        witnesses.append({'kind':'parabolic','m':m,'s':str(s),'c':str(c),'sqrt_s_times_chord_over_central_E':bounds(sqrt_s*chord),'limit':str(-fp)})


                for delta in (Q(1,8),Q(1,4)):
                    check(root.b<delta,'fixed endpoint to right '+label+f',delta={delta}')
                    R=max(2*s,delta)
                    check(1-abs(lam)*(n+1)*R>0,'zero-free fixed interval '+label+f',delta={delta}')
                    end=sign*(val(p[j],delta)-val(p[j+1],delta))
                    limit=sign*(val(poly(m,b,Q(0),sign,j),delta)-val(poly(m,b,Q(0),sign,j+1),delta))
                    check(limit<0,'fixed endpoint limit sign '+label+f',delta={delta}')
                    if j==0:
                        factor=I(1)
                    else:
                        # sqrt(1+u)<=1+u/2, u>=0, gives rational bounds.
                        u=(H/W0).absmax()**2
                        factor=I(1/(1+u/2),1)
                    scaled=end*factor
                    if exponent>=8: check(scaled.b<0,'fixed chord over sqrt E sign '+label+f',delta={delta}')
                    if scaled.b<0: fixed_negative+=1
                    elif scaled.a>0: fixed_positive+=1
                    else: fixed_undecided+=1
                    error=(scaled-limit).absmax()
                    check(error<=128*s,'fixed endpoint error '+label+f',delta={delta}')
                    fixed_worst=max(fixed_worst,error/s)
                    fixed_endpoint+=1
                    if (exponent==24 and sign==1 and b==Q(1,3)) or scaled.a>0:
                        witnesses.append({'kind':'fixed_endpoint','m':m,'b':str(b),'sign':sign,'s':str(s),'delta':str(delta),'chord_over_sqrt_central_E':bounds(scaled),'strictly_negative_limit':str(limit)})

parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--output',type=Path); args=parser.parse_args()
record={'schema':'theta22-chord-controls-v1','status':'PASS','event_time':'1/4','date':'2026-10-15','timezone':'America/New_York','prepared_for':'Edward Baker','llm_assistance':'Substantial LLM assistance; exact rational internal replay, not external refereeing.','model':'gpt-6-astra','reasoning_effort':'ultra','script':Path(__file__).name,'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'python_version':platform.python_version(),'exact_assertions':len(checks),'germs':24,'certified_full_stationary_roots':len(roots),'inner_windows':inner,'parabolic_windows':parabolic,'fixed_endpoint_windows':fixed_endpoint,'fixed_endpoint_signs':{'negative':fixed_negative,'positive':fixed_positive,'undecided':fixed_undecided,'negative_assertion_range':'s<=1/256; earlier observations retained'},'strictly_negative_inner_chords_C_gt_1':negative,'strictly_positive_inner_chords_C_lt_1':positive,'max_error_ratio_upper':{'slope_error_over_s':str(ceilq(worst[0])),'central_E_chord_error_over_s':str(ceilq(worst[1])),'parabolic_scaled_error_over_sqrt_s':str(ceilq(worst[2])),'fixed_endpoint_error_over_s':str(ceilq(fixed_worst))},'angle_certificate':'|angle-atan(C)| <= |Wx/W-C| <= 128*s; no floating-point atan assertion.','zero_free_certificate':'|P_(2r+1)| <= (2r+1)|x|P_(2r); 1-|lambda|(2r+1)R>0 on every whole window.','scope':'Exact heat polynomials. Rational root endpoint signs plus analytic strict derivative sign certify a unique full stationary root; exact bisection encloses it. No theta sign, all-N source family or unbounded-domain estimate is certified.','witnesses':witnesses,'root_enclosures':roots}
if args.output: args.output.write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in record.items() if k not in ('root_enclosures','witnesses')},indent=2))
