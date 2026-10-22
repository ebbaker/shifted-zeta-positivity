"""Certified finite geometry for RHE-09 actual fiber acquisition.
Full canonical H0 by exact xi identity, python-flint outward balls.
2026-10-22. For Edward Baker. Substantial LLM assistance.
Actual recorded model gpt-6.1-sol, effort ultra. Requires python-flint0.9.
"""
from fractions import Fraction as Q
from flint import arb, acb, acb_series, ctx
import time
I=acb(0,1)

def A(q):
    q=Q(q)
    return arb(q.numerator)/q.denominator

def h0(z):
    s=(1+I*z)/2
    return s*(s-1)/16*(-s*arb.pi().log()/2).exp()*(s/2).gamma()*s.zeta()

def certify_count(H=h0, N=8192):
    """Exactly two H zeros in |z-35|<8.

    Each full angular cell is evaluated as an acb rectangle. The H rectangle
    is convex and excludes zero, so its curve and endpoint chord are
    homotopic avoiding zero. Sum the argument increments of all exact ball
    endpoints and isolate the resulting integer.
    """
    st=time.monotonic()
    floor=arb('1e100'); total=arb(0); previous=H(acb(43)); maxrad=arb(0)
    for k in range(N):
        th=2*arb.pi()*arb(2*k+1,1)/(2*N)
        v=H(35+8*acb(0,th).exp())
        low=abs(v).lower()
        if not low>0: raise ArithmeticError('zero in boundary image enclosure '+str(k))
        floor=min(floor,low)
        nxt=H(35+8*acb(0,2*arb.pi()*(k+1)/N).exp())
        ratio=nxt/previous
        if not ratio.real>0: raise ArithmeticError('unresolved phase increment '+str(k))
        total+=ratio.arg(); previous=nxt
    winding=total/(2*arb.pi())
    if not (winding.contains(2) and winding>A('3/2') and winding<A('5/2')):
        raise ArithmeticError('winding does not isolate 2')
    return {'N':N,'count':2,'winding':str(winding),
            'boundary_floor_lower':str(floor),'seconds':time.monotonic()-st,
            'canonical_xi_calls':2*N+1}

def acquire_roots(steps=80):
    """Real sign brackets plus local nonzero derivative (and Rouche replay).

    The two real brackets together with the boundary count2 prove the only
    two complex roots are real/simple. The independent local Rouche test
    also certifies one root per tiny disk, without using the global count.
    """
    rows=[]; roots=[]
    for lo,hi in [(Q('28.26945'),Q('28.26946')),(Q('42.04407'),Q('42.04409'))]:
        sl=h0(acb(A(lo))).real
        sr=h0(acb(A(hi))).real
        if not (sl*sr<0): raise ArithmeticError('initial root sign bracket')
        sign=1 if sl>0 else -1
        for k in range(steps):
            mid=(lo+hi)/2; v=h0(acb(A(mid)))
            if not v.imag.contains(0): raise ArithmeticError('reality consistency')
            if v.real>0: sm=1
            elif v.real<0: sm=-1
            else: raise ArithmeticError('bisection sign unresolved')
            if sm==sign:lo=mid
            else:hi=mid
        c=A((lo+hi)/2); r=A(hi-lo) # strict disk larger than bracket halfwidth
        ctx.cap=3
        center=h0(acb_series([acb(c),1]))
        local=h0(acb_series([acb(arb(c,r),arb(0,r)),1]))
        second_upper=2*abs(local[2]).upper()
        margin=abs(center[1]).lower()*r-abs(center[0]).upper()-second_upper*r*r/2
        if not margin>0:raise ArithmeticError('local Rouche margin')
        derivative_floor=abs(center[1]).lower()-r*second_upper
        if not derivative_floor>0:raise ArithmeticError('simple root derivative floor')
        root=arb(c,r)
        roots.append(root)
        rows.append({'real_bracket_lo_exact':str(lo),'real_bracket_hi_exact':str(hi),
                    'root':str(root),'center':str(c),'disk_radius':str(r),
                    'local_second_derivative_upper':str(second_upper),
                    'rouche_margin_lower':str(margin.lower()),
                    'derivative_floor_lower':str(derivative_floor.lower()),
                    'bisection_steps':steps})
    return roots,rows

if __name__=='__main__':
    import json
    ctx.prec=160
    roots,rows=acquire_roots()
    print(json.dumps({'roots':rows,'count':certify_count()},indent=2))
