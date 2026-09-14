"""Enclosed polynomial moments of real endpoint/exterior logarithms.

All log centres lie outside the open output interval. Mixed logarithms use
integration by parts and the real part of a dilogarithm, including both
endpoint limits. No numerical quadrature enters the matrix construction.
"""
from flint import arb as A, arb_mat as AM

def plain(n,lo,hi):
    return [(hi**(k+1)-lo**(k+1))/(k+1) for k in range(n)]

def single(n,centre,lo,hi):
    """Integral v^k log|v-centre|; exact zero endpoint distances permitted."""
    p=[A(1)]
    for k in range(n):p.append(p[-1]*centre)
    def primitive(x):
        xp=[A(1)]
        for k in range(n):xp.append(xp[-1]*x)
        distance=abs(x-centre)
        singular=distance.is_zero()
        if not singular:assert distance>0
        log=A(0) if singular else distance.log()
        out=[]
        # Integral of v^(k+1)/(v-c) after polynomial division.
        accum=A(0)
        for k in range(n):
            accum=centre*accum+xp[k+1]/(k+1)
            boundary=A(0) if singular else (xp[k+1]-p[k+1])*log
            out.append((boundary-accum)/(k+1))
        return out
    a,b=primitive(lo),primitive(hi)
    return [y-x for x,y in zip(a,b)]

def ratlog(centre,other):
    """Integral_0^1 log|v-other|/(v-centre), when finite."""
    if centre is other or centre==other:
        assert centre<0 or centre>1
        left,right=abs(centre).log(),abs(1-centre).log()
        # Multiplication encloses squares even when a logarithm's ball
        # straddles zero. The general power operation may return nan there.
        return (right*right-left*left)/2
    gap=other-centre
    assert abs(gap)>0
    lg=abs(gap).log()
    def end(x):
        delta=x-centre
        if delta.is_zero():
            assert lg.is_zero(), 'Nonintegrable rational-log endpoint'
            first=A(0)
        else:first=lg*abs(delta).log()
        # Preserve exact endpoint identities before interval division.
        u=A(1) if x==other else delta/gap
        if u==0:dilog=A(0)
        elif u==1:dilog=A.pi()**2/6
        elif u<1:dilog=u.polylog(2)
        else:
            assert u>1, 'Unresolved dilogarithm branch'
            dilog=A.pi()**2/6-u.log()*(u-1).log()-(1-u).polylog(2)
        assert dilog.is_finite()
        return first-dilog
    return end(A(1))-end(A(0))

def pair(n,centre,other):
    """Integral_0^1 v^k log|v-c|log|v-d|."""
    c,d=centre,other
    assert c<=0 or c>=1
    assert d<=0 or d>=1
    lc=single(n,c,A(0),A(1));ld=single(n,d,A(0),A(1))
    chi=A(1) if c==1 or d==1 else A(0)
    boundary=A(0) if chi==1 else abs(1-c).log()*abs(1-d).log()
    # Coefficients of any divergent rational-log term vanish identically.
    icd=None if (c==0 and chi==0) or (c==1 and chi==1) else ratlog(c,d)
    idc=None if (d==0 and chi==0) or (d==1 and chi==1) else ratlog(d,c)
    cs,ds=A(0),A(0);cp,dp=A(1),A(1);out=[]
    for k in range(n):
        cs=c*cs+ld[k];ds=d*ds+lc[k]
        cp*=c;dp*=d
        extra=(cp-chi)*icd if icd is not None else A(0)
        extra+=(dp-chi)*idc if idc is not None else A(0)
        out.append((boundary-cs-ds-extra)/(k+1))
    return out

def hankel(values,n,m):
    assert len(values)>=n+m-1
    return AM([[values[i+j] for j in range(m)] for i in range(n)])
