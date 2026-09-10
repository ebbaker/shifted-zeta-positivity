"""Arb polynomial moments involving an exterior logarithm.

All logarithms are real on the integration intervals. The exterior parameter
is c>1. Closed recurrences, not numerical quadrature, enclose every moment.
"""
import math
from flint import arb as A, arb_mat as AM

def plain(n,lo=A(0),hi=A(1)):
    return [(hi**(k+1)-lo**(k+1))/(k+1) for k in range(n)]

def left(n,lo=A(0),hi=A(1)):
    def end(x,k):
        return A(0) if x.is_zero() else x**(k+1)*(x.log()/(k+1)-A(1)/(k+1)**2)
    return [end(hi,k)-end(lo,k) for k in range(n)]

def minus(n,c,lo=A(0),hi=A(1)):
    """Integral x^k log(c-x), including the endpoint c=hi=1."""
    if c==1 and hi==1:
        harmonic=A(0);out=[]
        for k in range(n):
            harmonic+=A(1)/(k+1)
            out.append(-harmonic/(k+1))
        if not lo.is_zero():
            low=minus(n,c,A(0),lo)
            out=[x-y for x,y in zip(out,low)]
        return out
    assert hi<c
    integral=((c-lo)/(c-hi)).log()
    out=[]
    for k in range(n):
        integral=c*integral-(hi**(k+1)-lo**(k+1))/(k+1)
        boundary=hi**(k+1)*(c-hi).log()-lo**(k+1)*(c-lo).log()
        out.append((boundary+integral)/(k+1))
    return out

def exterior(n,c):
    """Moments of log(c-x), its square, and products with endpoint logs."""
    assert c>1
    r=c-1
    lc=minus(n,c)
    j=-(1/c).polylog(2)
    t=(c.log()**2-r.log()**2)/2
    ll=[];sq=[]
    for k in range(n):
        j=c*j+A(1)/(k+1)**2
        ll.append((j-lc[k])/(k+1))
        t=c*t-lc[k]
        sq.append((r.log()**2+2*t)/(k+1))
    # Reflect log(1-x)*log(c-x), using log(y)*log(r+y).
    jp=(-1/r).polylog(2)
    ip=(c/r).log()
    plus=[]
    for k in range(n):
        ip=A(1)/(k+1)-r*ip
        lp=(c.log()-ip)/(k+1)
        jp=-r*jp-A(1)/(k+1)**2
        plus.append(-(lp+jp)/(k+1))
    right=[sum(((-1)**j*math.comb(k,j)*plus[j] for j in range(k+1)),A(0)) for k in range(n)]
    return {'outer':lc,'left_outer':ll,'right_outer':right,'outer2':sq}

def hankel(vals,n,m):
    assert len(vals)>=n+m-1
    return AM([[vals[i+j] for j in range(m)] for i in range(n)])
