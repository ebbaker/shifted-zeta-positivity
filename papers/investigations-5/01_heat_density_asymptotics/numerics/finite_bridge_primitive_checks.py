#!/usr/bin/env python3
"""Floating check of Note 20's finite Gaussian primitives, not a bridge solve.

24 October 2026. Prepared for Edward Baker with substantial LLM assistance.
gpt-6-astra (Codex), actual effort max. NumPy, no interval arithmetic.
"""
import argparse
import cmath
import hashlib
import json
import math
from pathlib import Path
import numpy as np
from numpy.polynomial.legendre import leggauss


def erf_series(z):
    # Restricted to the small arguments in this control; not a general evaluator.
    term=z; value=z
    for n in range(1,160):
        term *= -z*z/n
        value += term/(2*n+1)
    return 2/math.sqrt(math.pi)*value


def primitive(t,z,u):
    if t==0:
        if z==0:return complex(u),complex(u*u/2)
        a=1j*z
        return (cmath.exp(a*u)-1)/a,(cmath.exp(a*u)*(a*u-1)+1)/(a*a)
    a=cmath.sqrt(-t+0j)
    v=-1j*z/(2*a)
    i0=math.sqrt(math.pi)/(2*a)*cmath.exp(z*z/(4*t))*(erf_series(a*u+v)-erf_series(v))
    i1=(cmath.exp(t*u*u+1j*z*u)-1-1j*z*i0)/(2*t)
    return i0,i1


def main():
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True)
    args=p.parse_args();rows=[]
    for t in [-2.,0.,1.]:
        for z in [0j,.3+.2j,2+.4j]:
            u=.7
            plus=primitive(t,z,u);minus=primitive(t,-z,u)
            actual=np.array([(a+b)/2 for a,b in zip(plus,minus)])
            refs=[]
            for order in [64,96]:
                x,w=leggauss(order);x=(x+1)*u/2;w=w*u/2
                v=w*np.exp(t*x*x)*np.cos(z*x)
                refs.append(np.array([sum(v),sum(v*x)]))
            err=float(max(abs(actual-refs[-1])))
            assert err<1e-12,(t,z,err)
            rows.append({'t':t,'z':[z.real,z.imag],'upper_u':u,
                         'max_primitive_error':err,
                         'quadrature_refinement':float(max(abs(refs[-1]-refs[0])))})
    record={'date':'2026-10-24','prepared_for':'Edward Baker','model':'gpt-6-astra',
            'reasoning_effort':'max','status':'Floating primitive checks only; no finite-time bridge or interval certificate.',
            'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'numpy':np.__version__,'rows':rows,
            'limitations':['Small-argument error-function series is a control implementation only.',
                'No theta nodal mesh, density/current/covariance evaluation, or full-transition budget selected.',
                'Heat identities and source-to-jet/covariance inequalities are proved in Note 20, not certified by these samples.']}
    args.output.write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps({'cases':len(rows),'max_primitive_error':max(r['max_primitive_error'] for r in rows)}))


if __name__=='__main__':main()
