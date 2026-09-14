"""Complete polynomial-input outputs on a partition into spatial intervals.

The smooth gamma profile is truncated; endpoint/exterior logarithms and
arithmetic translations are integrated exactly with Arb enclosures.
"""
from dataclasses import dataclass
from fractions import Fraction
import math
from common import *
import log_moments as lm

@dataclass
class Output:
    poly: AM
    logs: dict
    translations: list

class Geometry:
    def __init__(self,lengths,modes,degree):
        assert len(lengths)==len(modes) and all(n>0 for n in modes)
        self.lengths,self.modes,self.degree=lengths,modes,degree
        self.starts=[ZERO]
        for length in lengths:self.starts.append(self.starts[-1]+length)
        self.L=self.starts[-1]
        assert self.L.value()<3
        self.g=c.profile(degree)
        self.phis=[legendre(n) for n in modes]
        self.active=active_powers(self.L)
        self.outputs={}
        self.values={}
        self.moments={}

    def pos(self,target,point):
        key=(target,point)
        if key not in self.values:
            if point==self.starts[target]:v=A(0)
            elif point==self.starts[target+1]:v=A(1)
            else:v=(point-self.starts[target]).value()/self.lengths[target].value()
            self.values[key]=v
        return self.values[key]

    def intersection(self,a,b,d,e):
        lo=max(a,d);hi=min(b,e)
        return (lo,hi) if lo<hi else None

    def output(self,target,source):
        key=(target,source)
        if key in self.outputs:return self.outputs[key]
        a,b=self.starts[target],self.starts[source]
        lo,li=self.lengths[target].value(),self.lengths[source].value()
        phi=self.phis[source];n=len(phi);M=self.degree
        logs={}
        if target==source:
            poly,log=residual.gamma_output(n,li,M,self.g)
            logs={a:log,self.starts[target+1]:log}
        else:
            right=target>source;sign=1 if right else -1
            ratio=lo/li;z=AP([(a-b).value()/li,ratio])
            continuation=[p(z) for p in phi]
            divided=[]
            for i,p in enumerate(phi):
                q=AP([sum((p[k]/(k-j) for k in range(j+1,i+1)),A(0)) for j in range(i)])
                divided.append(q(z)*(sign*ratio.sqrt()/2))
            logs[b]=matrix([-p*(sign*ratio.sqrt()/2) for p in continuation])
            logs[self.starts[source+1]]=matrix([p*(sign*ratio.sqrt()/2) for p in continuation])
            gap=(a-self.starts[source+1] if right else b-self.starts[target+1]).value()
            shifted=AP([rat(v) for v in self.g[1:]])(AP([gap,1]))
            moments=AM(n,M)
            for i in range(n):
                value=Fraction(math.factorial(i)**2,math.factorial(2*i+1))
                for k in range(i,M):
                    if k>i:value*=Fraction(k*k,(k-i)*(k+i+1))
                    moments[i,k]=rat(value)*A(2*i+1).sqrt()*((-1)**i if right else 1)
            kernel=AM(M,M)
            ip=[li**k for k in range(M)];op=[lo**k for k in range(M)]
            for k in range(M):
                for j in range(M-k):
                    kernel[k,j]=-shifted[k+j]*math.comb(k+j,k)*ip[k]*op[j]/2
            smooth=rows((li*lo).sqrt()*moments*kernel)
            if not right:smooth=[p(AP([1,-1])) for p in smooth]
            poly=matrix([x+y for x,y in zip(divided,smooth)])
        translations=[]
        for number,prime,_ in self.active:
            for direction in [-1,1]:
                delay=direction*logn(number)
                window=self.intersection(a,self.starts[target+1],b-delay,self.starts[source+1]-delay)
                if window:
                    z=AP([(a+delay-b).value()/li,lo/li])
                    alpha=-A(prime).log()/A(number).sqrt()*(lo/li).sqrt()
                    translations.append((*window,matrix([alpha*p(z) for p in phi])))
        # Merge identical supports before any products are formed. In
        # particular all full-window translates belong in the polynomial
        # part; keeping them separate needlessly expands one Gram into many.
        merged={}
        for left,right,term in translations:
            if left==a and right==self.starts[target+1]:
                width=max(poly.ncols(),term.ncols())
                poly=residual.pad(poly,width)+residual.pad(term,width)
            else:
                window=(left,right)
                if window in merged:
                    prev=merged[window];width=max(prev.ncols(),term.ncols())
                    term=residual.pad(prev,width)+residual.pad(term,width)
                merged[window]=term
        translations=[(*window,term) for window,term in merged.items()]
        out=Output(poly,logs,translations)
        self.outputs[key]=out
        return out

    def moment(self,target,n,m,centres=(),window=None):
        lo,hi=window or (self.starts[target],self.starts[target+1])
        centres=tuple(sorted(centres))
        key=(target,centres,lo,hi)
        needed=n+m-1
        if key not in self.moments or len(self.moments[key])<needed:
            ll,hh=self.pos(target,lo),self.pos(target,hi)
            if not centres:vals=lm.plain(needed,ll,hh)
            elif len(centres)==1:vals=lm.single(needed,self.pos(target,centres[0]),ll,hh)
            else:
                assert len(centres)==2 and ll==0 and hh==1
                vals=lm.pair(needed,*[self.pos(target,x) for x in centres])
            self.moments[key]=vals
        return lm.hankel(self.moments[key],n,m)

    def inner(self,target,x,y,centres=(),window=None):
        return x*self.moment(target,x.ncols(),y.ncols(),centres,window)*y.transpose()

    def gram_block(self,target,left,right):
        x,y=self.output(target,left),self.output(target,right)
        xt=[((),x.poly)]+[((p,),v) for p,v in x.logs.items()]
        yt=[((),y.poly)]+[((p,),v) for p,v in y.logs.items()]
        out=AM(self.modes[left],self.modes[right])
        for xc,xv in xt:
            for yc,yv in yt:out+=self.inner(target,xv,yv,xc+yc)
        for lo,hi,v in x.translations:
            for centres,yv in yt:out+=self.inner(target,v,yv,centres,(lo,hi))
        for lo,hi,v in y.translations:
            for centres,xv in xt:out+=self.inner(target,xv,v,centres,(lo,hi))
        for lo,hi,xv in x.translations:
            for l2,h2,yv in y.translations:
                window=self.intersection(lo,hi,l2,h2)
                if window:out+=self.inner(target,xv,yv,(),window)
        return c.sym(out) if left==right else out

    def head_block(self,target,source):
        out=self.output(target,source);phi=matrix(self.phis[target])
        head=self.inner(target,phi,out.poly)
        for centre,v in out.logs.items():head+=self.inner(target,phi,v,(centre,))
        for lo,hi,v in out.translations:head+=self.inner(target,phi,v,(),(lo,hi))
        return head
