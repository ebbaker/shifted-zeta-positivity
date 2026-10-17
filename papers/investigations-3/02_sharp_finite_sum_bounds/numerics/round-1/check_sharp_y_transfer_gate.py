#!/usr/bin/env python3
"""Bounded outward implementation of the sharp active-branch y-transfer gate.
Prepared for Edward Baker with substantial LLM assistance, 17 October 2026.
Recorded model gpt-6.1-sol (Codex), reasoning effort ultra.
No complete Newman certificate. Standard-library Python only.
"""
import argparse, decimal, hashlib, itertools, json, math, platform, resource, time
from dataclasses import dataclass
from decimal import Decimal as D, Context, ROUND_FLOOR, ROUND_CEILING, ROUND_HALF_EVEN
from fractions import Fraction as F
from pathlib import Path

PREC=40
CF=Context(prec=PREC,rounding=ROUND_FLOOR)
CC=Context(prec=PREC,rounding=ROUND_CEILING)
CN=Context(prec=PREC,rounding=ROUND_HALF_EVEN)
decimal.setcontext(CN.copy())
ETA=D('1e-38')
T=D('.157')
LEGS=[((2,3,5,7,11),690988,728999),((2,3,5,7),729000,818999),
      ((2,3,5),819000,1027999),((2,3),1028000,3840000)]

class I:
    __slots__=('lo','hi')
    def __init__(self,lo,hi=None):
        self.lo=D(lo);self.hi=self.lo if hi is None else D(hi)
        if self.lo>self.hi:raise ValueError('empty interval')
    @staticmethod
    def of(a):return a if isinstance(a,I) else I(a)
    def __add__(a,b):
        b=I.of(b);return I(CF.add(a.lo,b.lo),CC.add(a.hi,b.hi))
    __radd__=__add__
    def __neg__(a):return I(a.hi.copy_negate(),a.lo.copy_negate())
    def __sub__(a,b):return a+-I.of(b)
    def __rsub__(a,b):return I.of(b)+-a
    def __mul__(a,b):
        b=I.of(b);p=[(x,y) for x in (a.lo,a.hi) for y in (b.lo,b.hi)]
        return I(min(CF.multiply(x,y) for x,y in p),max(CC.multiply(x,y) for x,y in p))
    __rmul__=__mul__
    def __truediv__(a,b):
        b=I.of(b)
        if b.lo<=0<=b.hi:raise ZeroDivisionError('interval contains zero')
        p=[(x,y) for x in (a.lo,a.hi) for y in (b.lo,b.hi)]
        return I(min(CF.divide(x,y) for x,y in p),max(CC.divide(x,y) for x,y in p))
    def __rtruediv__(a,b):return I.of(b)/a
    def abs(a):
        return I(0 if a.lo<=0<=a.hi else min(abs(a.lo),abs(a.hi)),max(abs(a.lo),abs(a.hi)))
    def width(a):return CC.subtract(a.hi,a.lo)
    def data(a):return [str(a.lo),str(a.hi)]

def ex(a):
    a=I.of(a)
    return I(CF.multiply(CN.exp(a.lo),CF.subtract(1,ETA)),CC.multiply(CN.exp(a.hi),CC.add(1,ETA)))
def ln(a):
    a=I.of(a)
    if a.lo<=0:raise ValueError('ln nonpositive')
    x,y=CN.ln(a.lo),CN.ln(a.hi)
    return I(CF.subtract(x,CC.multiply(ETA,max(D(1),abs(x)))),CC.add(y,CC.multiply(ETA,max(D(1),abs(y)))))
def sqroot(a):
    a=I.of(a)
    return I(CF.multiply(CN.sqrt(a.lo),CF.subtract(1,ETA)),CC.multiply(CN.sqrt(a.hi),CC.add(1,ETA)))
def meet(a,b):
    lo,hi=max(a.lo,b.lo),min(a.hi,b.hi)
    return None if lo>hi else I(lo,hi)
def dint(z,w):
    if z.lo>0:return w
    if z.hi<0:return -w
    # Covers either sign and the upper right derivative |w| at z=0.
    a=w.abs().hi;return I(-a,a)
def subsets(P):
    out=[(1,1,D(0))]
    for p in P:
        lp=ln(I(p));out += [(d*p,-s,sq+lp*lp) for d,s,sq in out[:]]
    return sorted(out,key=lambda x:x[0])
def ceiling(a):return int(a.to_integral_value(rounding=ROUND_CEILING))
def floor(a):return int(a.to_integral_value(rounding=ROUND_FLOOR))
def cdiv(a,b):return -(-a//b)

@dataclass
class Pattern:
    G:int
    previous:int
    top:int
    active:tuple
    nmin:int
    def label(self):return dict(G=self.G,sector=[self.previous,self.top],active=[d for d,_,_,_ in self.active])

class Leg:
    def __init__(self,idx):
        self.idx=idx;self.P,self.nlo,self.nhi=LEGS[idx];self.D=math.prod(self.P)
        self.h=I(ln(I(self.nlo)).lo,ln(I(self.nhi)).hi)
        self.patterns=[]
        ds=subsets(self.P)
        for G,_,_ in ds:
            divs=[q for q in ds if G%q[0]==0]
            nmin=G
            if G==1:
                nmin=2
                while math.gcd(nmin,self.D)!=1:nmin+=1
            for j,(top,_,_) in enumerate(divs):
                prev=divs[j-1][0] if j else 0
                active=[]
                for d,sign,sp2 in divs[j:]:
                    ld=ln(I(d))
                    alpha=(T/4)*(sp2+ld*ld)
                    active.append((d,sign,ld,alpha))
                self.patterns.append(Pattern(G,prev,top,tuple(active),nmin))
        assert len(self.patterns)==3**len(self.P)

    def root(self,p):
        v=I(ln(I(p.nmin)/self.nhi).lo,0) if not p.previous else I(ln(I(p.previous)).lo,ln(I(p.top)).hi)
        return (self.h,v,I(sqroot(I('.0350708')).lo,sqroot(I('.686')).hi),0)

def trim(leg,p,H,V):
    """Only discard a box after a necessary integer feasibility condition fails."""
    en=ex(H)
    nl=max(leg.nlo,ceiling(en.lo));nh=min(leg.nhi,floor(en.hi))
    if nl>nh:return None
    L=meet(H+V,I(ln(I(p.nmin)).lo,ln(I(p.G*nh)).hi))
    if L is None:return None
    er=ex(L)
    nlo=max(p.nmin,ceiling(er.lo),p.previous*nl+1 if p.previous else 2)
    nhi=min(floor(er.hi),p.top*nh)
    kl,kh=cdiv(nlo,p.G),nhi//p.G
    if kl>kh:return None
    candidates=None
    if kh-kl<=32:
        candidates=[];rr=ex(V)
        for k in range(kl,kh+1):
            if math.gcd(k,leg.D//p.G)!=1:continue
            n=p.G*k
            low=max(nl,cdiv(n,p.top),ceiling(CF.divide(D(n),rr.hi)))
            high=min(nh,floor(CC.divide(D(n),rr.lo)))
            if p.previous:high=min(high,(n-1)//p.previous)
            if low<=high:candidates.append(n)
        if not candidates:return None
        L=meet(L,I(ln(I(min(candidates))).lo,ln(I(max(candidates))).hi))
        assert L is not None
    return L,candidates

def evaluate(leg,p,H,V,Y):
    tr=trim(leg,p,H,V)
    if tr is None:return 'empty',None
    L,candidates=tr
    if len(p.active)==1:return 'singleton',None
    if p.previous==0 and p.G in leg.P and candidates==[p.G]:return 'prime_zero',None
    # Keep h and v as dependent coordinates through the exact delta(h).
    delta=-ln(1-(T/16)*ex(-2*H))/2
    ell=I('.02')-H+delta
    g=ex(Y*ell)
    assert 0<g.lo<=g.hi<1
    Fv=ex(Y*(V+I('.02')+delta))
    c=I(0);cy=I(0);ts=I(0)
    for d,sign,ld,alpha in p.active:
        r=I(1) if d==1 else ex(alpha-(T/2)*L*ld)
        term=r if d==1 else r*ex(-Y*ld)
        c+=sign*r;cy+=sign*term
        ts+=sign*term*(V+I('.02')+delta-ld)
    Q=Fv*cy;Tv=Fv*ts
    activity=(g*c-Q)*(c-g*Q)
    branches=(-1,) if activity.lo>0 else ((1,) if activity.hi<0 else (-1,1))
    bounds={}
    for e in branches:
        z=c+e*Q;d=1+e*g
        # Multiply the bracket in (2) by its positive denominator d.
        gate=d*dint(z,e*Tv)-((L/2)*d+e*ell*g)*z.abs()
        bounds[str(e)]=gate
    if all(v.hi<=0 for v in bounds.values()):
        return 'active',dict(branches=list(branches),bounds={k:v.data() for k,v in bounds.items()})
    # Equivalent absolute-sum formula automatically retains both kinds of kink.
    R=c-g*Q;S=Q-g*c
    Rp=-g*(ell*Q+Tv);Sp=Tv-ell*g*c
    gg=g*g
    alt=dint(R,Rp)+dint(S,Sp)-(L/2-2*gg*ell/(1-gg))*(R.abs()+S.abs())
    if alt.hi<=0:return 'absolute_sum',dict(bound=alt.data())
    return 'unresolved',dict(branches=list(branches),bounds={k:v.data() for k,v in bounds.items()},
        absolute_sum=alt.data(),activity=activity.data(),L=L.data(),g=g.data())

def split(H,V,Y,depth):
    ivs=(H,V,Y);scales=(D('.05'),D('.25'),D('.025'))
    axis=max(range(3),key=lambda j:CN.divide(ivs[j].width(),scales[j]))
    a=ivs[axis];mid=CN.divide(CN.add(a.lo,a.hi),2)
    if not a.lo<mid<a.hi:return None
    out=[]
    for b in (I(a.lo,mid),I(mid,a.hi)):
        child=list(ivs);child[axis]=b;out.append(tuple(child)+(depth+1,))
    return out

def box_data(H,V,Y,depth):return dict(h=H.data(),v=V.data(),y=Y.data(),depth=depth)

def certify_leg(idx,seconds,maxcells,maxdepth):
    leg=Leg(idx);start=time.monotonic();hh=hashlib.sha256()
    stats=dict(leg=idx,N=[leg.nlo,leg.nhi],primes=list(leg.P),patterns=len(leg.patterns),
        evaluated=0,accepted={},completed_patterns=[],unresolved_leaf_count=0,
        unresolved_examples=[],pending=[],stop_reason=None,accepted_leaf_sha256=None)
    stop=False
    for pi,p in enumerate(leg.patterns):
        stack=[leg.root(p)]
        while stack:
            if stats['evaluated']>=maxcells or time.monotonic()-start>=seconds:
                stats['stop_reason']='box_budget' if stats['evaluated']>=maxcells else 'wall_budget'
                stats['pending'].append(dict(pattern_index=pi,pattern=p.label(),subtrees=len(stack),
                    example=box_data(*stack[-1])))
                stats['unopened_pattern_indices']=list(range(pi+1,len(leg.patterns)))
                stop=True;break
            H,V,Y,depth=stack.pop();stats['evaluated']+=1
            kind,detail=evaluate(leg,p,H,V,Y)
            if kind!='unresolved':
                stats['accepted'][kind]=stats['accepted'].get(kind,0)+1
                hh.update(json.dumps(dict(pattern=pi,box=box_data(H,V,Y,depth),kind=kind,detail=detail),sort_keys=True).encode()+b'\n')
                continue
            children=split(H,V,Y,depth) if depth<maxdepth else None
            if children is not None:
                stack.extend(reversed(children));continue
            stats['unresolved_leaf_count']+=1
            if len(stats['unresolved_examples'])<12:
                stats['unresolved_examples'].append(dict(pattern_index=pi,pattern=p.label(),box=box_data(H,V,Y,depth),detail=detail))
        if stop:break
        stats['completed_patterns'].append(pi)
    stats['accepted_leaf_sha256']=hh.hexdigest()
    stats['seconds']=time.monotonic()-start
    stats['all_patterns_completed']=len(stats['completed_patterns'])==len(leg.patterns)
    stats['passed']=stats['all_patterns_completed'] and stats['unresolved_leaf_count']==0 and not stats['pending']
    return stats

def selftest():
    # Decimal transcendental endpoint padding checked against higher precision.
    high=Context(prec=100,rounding=ROUND_HALF_EVEN);ntrans=0
    for k in range(-50,51):
        x=D(k)/7
        assert ex(I(x)).lo<=high.exp(x)<=ex(I(x)).hi
        z=D(k+51)/11
        assert ln(I(z)).lo<=high.ln(z)<=ln(I(z)).hi
        assert sqroot(I(z)).lo<=high.sqrt(z)<=sqroot(I(z)).hi
        ntrans+=3
    # Exact one-sided derivative identity, including branch ties and numerator zeros.
    def da(z,w):return (1 if z>0 else -1)*w if z else abs(w)
    count=0
    for b,a,ap,g in itertools.product(range(-3,4),range(-3,4),range(-2,3),(F(1,4),F(1,2),F(3,4))):
        b,a,ap=F(b),F(a),F(ap);gp=-3*g;ell=gp/g;L=F(2)
        Q=g*a;Tv=gp*a+g*ap
        ub={e:abs(b+e*Q)/(1+e*g) for e in (-1,1)};um=max(ub.values())
        deriv=max(da(b+e*Q,e*Tv)/(1+e*g)-e*gp*abs(b+e*Q)/(1+e*g)**2-L/2*ub[e]
                  for e in (-1,1) if ub[e]==um)
        R=b-g*Q;S=Q-g*b;Rp=-g*(ell*Q+Tv);Sp=Tv-ell*g*b
        alt=(da(R,Rp)+da(S,Sp)-(L/2-2*g*g*ell/(1-g*g))*(abs(R)+abs(S)))/(1-g*g)
        assert deriv==alt,(b,a,ap,g,deriv,alt)
        count+=1
    # Exhaustive integer membership for small toy legs; counts all active nonleading terms.
    membership=0
    for P in ((2,3),(2,3,5)):
        Dv=math.prod(P)
        for N in (7,8,9):
            for n in range(2,Dv*N+1):
                G=math.gcd(n,Dv);divs=[d for d in range(1,G+1) if G%d==0]
                active=[d for d in divs if n<=d*N]
                if not active:
                    assert n>G*N;continue
                j=divs.index(active[0]);previous=divs[j-1] if j else 0
                assert (previous==0 or n>previous*N) and n<=divs[j]*N
                assert math.gcd(n//G,Dv//G)==1
                membership+=1
    # Singleton proof requires q_N/N > exp(.04), uniformly since N-t/(16N) increases.
    margin=I(690988)-I(T)/(16*690988)-ex(I('.04'))
    assert margin.lo>0
    prime_rate=F(52,100)-13+F(3,2)+F(1000,187)
    assert prime_rate<0
    return dict(transcendental_endpoint_checks=ntrans,exact_derivative_identities=count,
                toy_integer_memberships=membership,singleton_global_margin=margin.data(),
                prime_zero_log_rate_upper=str(prime_rate),passed=True)

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--legs',default='3,2,1,0')
    ap.add_argument('--seconds-per-leg',type=float,default=45)
    ap.add_argument('--maxcells',type=int,default=30000)
    ap.add_argument('--maxdepth',type=int,default=36)
    ap.add_argument('--selftest-only',action='store_true')
    ap.add_argument('--plan',type=Path,default=Path(__file__).with_name('GATE_RUN_PLAN_20261017.md'))
    ap.add_argument('--output',type=Path,required=True)
    a=ap.parse_args();indices=[int(v) for v in a.legs.split(',')]
    if any(i not in range(4) for i in indices) or len(set(indices))!=len(indices):raise ValueError('invalid leg list')
    rec=dict(date='2026-10-17',prepared_for='Edward Baker',model='gpt-6.1-sol',reasoning_effort='ultra',
        status='bounded outward gate implementation; not a complete Newman certificate',
        python=platform.python_version(),decimal_precision=PREC,t='157/1000',
        y_squared=['87677/2500000','343/500'],coordinates=['log N','log(n/N)','y'],
        code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        plan_sha256=hashlib.sha256(a.plan.read_bytes()).hexdigest(),
        limits=dict(seconds_per_leg=a.seconds_per_leg,maxcells_per_leg=a.maxcells,maxdepth=a.maxdepth),
        selftest=selftest(),legs=[])
    if not a.selftest_only:
        for idx in indices:
            r=certify_leg(idx,a.seconds_per_leg,a.maxcells,a.maxdepth);rec['legs'].append(r)
            print(json.dumps({k:r[k] for k in ('leg','evaluated','accepted','unresolved_leaf_count','stop_reason','seconds','passed')}),flush=True)
    rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    import sys
    rec['peak_resident_bytes']=rss if sys.platform=='darwin' else rss*1024
    rec['memory_budget_pass']=rec['peak_resident_bytes']<512*1024**2
    rec['all_requested_legs_passed']=not a.selftest_only and rec['memory_budget_pass'] and all(r['passed'] for r in rec['legs'])
    rec['full_four_leg_transfer_certified']=rec['all_requested_legs_passed'] and set(indices)==set(range(4))
    a.output.write_text(json.dumps(rec,indent=2)+'\n')
    print(json.dumps(dict(output=str(a.output),full_four_leg_transfer_certified=rec['full_four_leg_transfer_certified'],peak_resident_bytes=rec['peak_resident_bytes'])))

if __name__=='__main__':main()
