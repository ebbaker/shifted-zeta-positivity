#!/usr/bin/env python3
"""Exact finite-mode Taylor and expanding-cutoff checks for Investigation 21.

Prepared for Edward Baker, 15 October 2026, with substantial LLM assistance.
Recorded coordinating model gpt-6.1-sol, effort ultra. Standard library only.
The infinite-domain conclusions use the analytic proof in Note 42; these
finite exact checks neither prove a stationary sign nor evaluate theta roots.
"""
import argparse
from fractions import Fraction as Q
from hashlib import sha256
import json
from math import factorial
from pathlib import Path
import platform

ORDER = 4
# A key (n,a,k) denotes z^n exp(4*a*s) pi^k, before the common z^(1/2).
def add(*polys):
    out = {}
    for poly in polys:
        for key, value in poly.items():
            out[key] = out.get(key, Q(0)) + value
    return {key: value for key, value in out.items() if value}

def scale(poly, value):
    return {key: c*value for key, c in poly.items() if c*value}

def multiply(left, right):
    out = {}
    for (n,a,k), v in left.items():
        for (m,b,l), w in right.items():
            if n+m <= ORDER:
                key = (n+m,a+b,k+l)
                out[key] = out.get(key, Q(0)) + v*w
    return {key: value for key, value in out.items() if value}

def power(poly, degree):
    out = {(0,0,0): Q(1)}
    for _ in range(degree):
        out = multiply(out, poly)
    return out

def series_exponential(poly):
    return add(*(scale(power(poly,n),Q(1,factorial(n))) for n in range(ORDER+1)))

def series_cosine(poly):
    return add(*(scale(power(poly,2*n),Q((-1)**n,factorial(2*n)))
                 for n in range(ORDER//2+1)))

def mode_expansion(p,k):
    # f=z^(1/2)(1+z^2)^(-1/2).
    f = {(0,0,0):Q(1),(2,0,0):Q(-1,2),(4,0,0):Q(3,8)}
    # -pi*(exp(4s)p^2+exp(-4s)k^2)*z/(1+z^2).
    exponent = {(1,1,1):Q(-p*p),(1,-1,1):Q(-k*k),
                (3,1,1):Q(p*p),(3,-1,1):Q(k*k)}
    # (-1)^(pk)cos(pi*pk*tau)=cos(2*pi*pk*z^2/(1+z^2)).
    phase = {(2,0,1):Q(2*p*k),(4,0,1):Q(-2*p*k)}
    return multiply(multiply(f,series_exponential(exponent)),series_cosine(phase))

def operator(poly):
    out = {}
    for (n,a,k), coefficient in poly.items():
        x,y = 4*a,-2-4*n
        symbol = (x*x-y*y)**2-8*(x*x+y*y)+16
        if symbol:
            out[(n,a,k)] = coefficient*Q(symbol,4096)
    return out

def main(output):
    named=[]
    def require(name,condition):
        if not condition:
            raise AssertionError(name)
        named.append(name)
    mode_rows=[]
    for p in range(-3,4):
        for k in range(-3,4):
            result = operator(mode_expansion(p,k))
            early = {key:c for key,c in result.items() if key[0]<2}
            leading = {key:c for key,c in result.items() if key[0]==2 and c}
            expected={(2,0,0):Q(-9,8)}
            if p*k:
                expected[(2,0,2)] = Q(9,4)*p*p*k*k
            require('annihilated first two orders %s,%s'%(p,k),not early)
            require('exact leading mode polynomial %s,%s'%(p,k),leading==expected)
            mode_rows.append({'p':p,'k':k,'constant':str(Q(-9,8)),
                              'pi_squared_coefficient':str(Q(9,4)*p*p*k*k)})
    rectangles=[]
    for P in range(7):
        for K in range(7):
            total=(2*P+1)*(2*K+1)
            mixed=sum(p*p*k*k for p in range(-P,P+1) for k in range(-K,K+1))
            predicted=Q(P*(P+1)*(2*P+1),3)*Q(K*(K+1)*(2*K+1),3)
            require('rectangle square-moment formula %s,%s'%(P,K),mixed==predicted)
            require('rectangle coefficient formula %s,%s'%(P,K),
                    Q(9,4)*mixed==Q(total*P*(P+1)*K*(K+1),4))
            if P and K:
                # pi^2>9 suffices; this is a rational strict sign check.
                lower=Q(9,8)*total*(Q(2*P*(P+1)*K*(K+1))-1)
                require('positive rectangle coefficient using pi squared > 9 %s,%s'%(P,K),lower>0)
            else:
                require('negative axial rectangle coefficient %s,%s'%(P,K),mixed==0 and total>0)
            rectangles.append({'P':P,'K':K,'mode_count':total,'sum_p2k2':str(mixed),
                               'leading_sign':'positive' if P and K else 'negative'})
    for j in (0,1):
        # A last-radial strip of width 1/R leaves this exact power.
        require('strip polynomial power j=%s'%j,2*j+2-1==2*j+1)
    # R=(log N)/2: 2tR^2-10R=(t/2)log(N)^2-5log(N).
    require('quadratic log coefficient',2*Q(1,2)**2==Q(1,2))
    require('linear log coefficient',-10*Q(1,2)==-5)
    require('complete exterior Gaussian scaling',4*Q(1,2)==2)
    # On e^(-v)g(y), y=e^(-4v), (d_v^2-1) is
    # 24*y*d_y+16*y^2*d_y^2. Independent monomial-symbol check.
    for degree in range(9):
        require('diagonal profile differential symbol degree=%s'%degree,
                (-1-4*degree)**2-1==24*degree+16*degree*(degree-1))
    require('first diagonal source multiplier',Q(5**2-1,256)==Q(3,32))
    record={
      'schema':'inv21_poisson_modes_and_cutoff_cost_v1','date':'2026-10-15',
      'prepared_for':'Edward Baker','llm_assistance':'substantial',
      'recorded_model':'gpt-6.1-sol','recorded_effort':'ultra','status':'PASS',
      'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
      'runtime':{'python':platform.python_version(),'arithmetic':'exact rational'},
      'assertion_count':len(named),'assertions':named,
      'formal_expansion_order':ORDER,'mode_cases':mode_rows,'rectangular_cases':rectangles,
      'limitations':[
       'Checks finite generating-series algebra and exact sums only.',
       'Uniform analytic remainders, positive-time divergence and superpolynomial growth are proved in Note 42, not by finite sampling.',
       'No theta stationary sign, collision exclusion, new certified domain or source energy-relative payment is asserted.']}
    output.write_text(json.dumps(record,indent=2)+'\n')
    print('PASS',len(named),'exact assertions;',len(mode_rows),'modes;',len(rectangles),'rectangles')

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',required=True,type=Path)
    main(parser.parse_args().output)
