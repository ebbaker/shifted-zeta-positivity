#!/usr/bin/env python3
"""Exact operator audit and paid finite Poisson identity comparisons.

Prepared for Edward Baker, 15 October 2026, with substantial LLM assistance.
Recorded parent model gpt-6-astra, reasoning effort ultra.
Finite checks supplement the analytic proof; they certify no theta sign.
"""
import argparse
from fractions import Fraction as Q
from hashlib import sha256
import json
from pathlib import Path
import platform
import flint
from flint import arb, ctx


def poly_add(a, b):
    c = dict(a)
    for k, v in b.items(): c[k] = c.get(k, Q(0)) + v
    return {k: v for k, v in c.items() if v}


def poly_scale(a, v): return {k: c*v for k, c in a.items() if c*v}


def poly_mul(a, b):
    c = {}
    for k, v in a.items():
        for ell, w in b.items(): c[k+ell] = c.get(k+ell, Q(0)) + v*w
    return {k: v for k, v in c.items() if v}


def derivative_with_f(p):
    # z=tanh(4r), f=(2cosh(4r))^(-1/2): (f*p)'/f.
    dp = {k-1: k*v for k,v in p.items() if k}
    return poly_add(poly_mul({0:Q(4),2:Q(-4)},dp),poly_mul({1:Q(-2)},p))


def enc(v):
    def dy(x):
        m,e=x.man_exp(); return [str(m),int(e)]
    if not v.is_finite(): raise AssertionError('nonfinite ball')
    return {'lower':dy(v.lower()),'upper':dy(v.upper()),'display':v.str(16)}


def sym(v): return arb(0,v.upper())


def theta_part(y,n): return 1+2*sum((-arb.pi()*y*k*k).exp() for k in range(1,n+1))


def theta_tail(y,n):
    ratio=(-arb.pi()*y*(2*n+3)).exp()
    assert ratio<1
    return 2*(-arb.pi()*y*(n+1)**2).exp()/(1-ratio)


def run(args):
    ctx.prec=args.bits
    assert args.bits>=192
    checks=[]
    def check(name,actual,expected):
        assert actual==expected,(name,actual,expected)
        checks.append(name)
    p={0:Q(1)}; deriv=[p]
    for _ in range(4): p=derivative_with_f(p); deriv.append(p)
    check('f second derivative polynomial',deriv[2],{0:Q(-8),2:Q(12)})
    Df=poly_add(poly_add(deriv[4],poly_scale(deriv[2],-8)),{0:Q(16)})
    q={0:Q(1),2:Q(-1)}
    expected=poly_scale(poly_mul(q,poly_add({0:Q(24)},poly_scale(q,-35))),-48)
    check('D f equals -48 f q (24-35q)',Df,expected)
    check('axis asymptotic leading coefficient',Q(48*4*24,4096),Q(9,8))
    # For e^(a*s+b*r), D has this polynomial; direct chain rule has /256.
    for a,b in [(0,0),(2,0),(-2,0),(0,2),(0,-2),(3,7),(7,3),(-5,11)]:
        lhs=(Q((a+b)**2,4)-1)*(Q((a-b)**2,4)-1)/256
        rhs=Q((a*a-b*b)**2-8*(a*a+b*b)+16,4096)
        check('chain rule symbol %s,%s'%(a,b),lhs,rhs)
    # Correct parity lattice parametrization and its completed square.
    for m,n in [(0,0),(1,0),(1,2),(-2,3),(4,-1)]:
        p,q=m+n,m-n
        check('parity inverse %s,%s'%(m,n),(p+q,p-q),(2*m,2*n))
        assert (p-q)%2==0
        for y,z in [(Q(1),Q(2)),(Q(3,2),Q(7,3))]:
            A=y+z; T=(y-z)/A
            check('completed square %s,%s,%s,%s'%(m,n,y,z),m*m*y+n*n*z,
                  A*(q+T*p)**2/4+y*z*p*p/A)
    # Two independent Gaussian series with proven absolute tails.
    rows=[]; N=32
    for ss in [Q(-1,4),Q(0),Q(1,4)]:
      for rr in [Q(0),Q(1,8),Q(1,4),Q(1,2)]:
        s=arb(ss.numerator)/ss.denominator;r=arb(rr.numerator)/rr.denominator
        C=2*(4*r).cosh(); tau=(4*r).tanh(); f=1/C.sqrt()
        a=(4*s).exp()/C;b=(-4*s).exp()/C
        direct=arb(1)
        for v in [s+r,s-r]:
            y=(4*v).exp()
            direct*=v.exp()*(theta_part(y,N)+sym(theta_tail(y,N)))
        vals={}
        for parity in [True,False]:
            val=arb(0)
            for p in range(N+1):
              for k in range(N+1):
                sign=(-1 if (parity and p*k%2) else 1)
                multiplicity=(1 if p==0 else 2)*(1 if k==0 else 2)
                val+=sign*multiplicity*(-arb.pi()*(a*p*p+b*k*k)).exp()*(arb.pi()*p*k*tau).cos()
            tail=f*(theta_tail(a,N)*(theta_part(b,N)+theta_tail(b,N))+theta_part(a,N)*theta_tail(b,N))
            vals[parity]=f*val+sym(tail)
        assert direct.overlaps(vals[True]),(ss,rr,direct,vals[True])
        assert max(direct.rad(),vals[True].rad())<arb(10)**-25
        # A diagnostic sensitivity check: omitting parity changes the identity.
        if ss==0 and rr==0:
            assert not direct.overlaps(vals[False])
            checks.append('omitting parity factor fails at origin')
        rows.append({'s':str(ss),'r':str(rr),'direct_primitive':enc(direct),
                     'poisson_primitive':enc(vals[True]),'transformed_tail_bound':enc(tail),
                     'overlap':True})
    record={'schema':'inv21_poisson_parity_heat_obstruction_v1','date':'2026-10-15',
      'prepared_for':'Edward Baker','llm_assistance':'Substantial',
      'recorded_model':'gpt-6-astra','recorded_effort':'ultra','status':'PASS',
      'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
      'runtime':{'python':platform.python_version(),'python_flint':flint.__version__,'bits':args.bits},
      'exact_and_sensitivity_assertions':checks,'paid_identity_comparisons':rows,'source_and_transformed_cutoff':N,
      'scope':'Exact finite operator/parity algebra and independent ball comparisons with Gaussian tails. The positive-time nonintegrability conclusion is analytic, proved in Note 38; no new stationary or global sign claim.'}
    args.output.write_text(json.dumps(record,indent=2)+'\n')
    print('PASS',len(checks),'exact/sensitivity assertions;',len(rows),'paid identity comparisons')


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--bits',type=int,default=256)
    p.add_argument('--output',type=Path,required=True)
    run(p.parse_args())
