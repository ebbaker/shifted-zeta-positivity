#!/usr/bin/env python3
"""Independent epsilon normalization control through entire spherical Bessel integrals.

Prepared for Edward Baker, 2026-09-29, with GPT-6 (Codex) assistance.
Exact serving variant and configured reasoning effort are not exposed.
Defaults to sibling prolate/epsilon modules and records/ output.
"""
import argparse
import hashlib
import json
import math
import platform
import sys
from fractions import Fraction as Q
from pathlib import Path
import flint
from flint import arb,acb,ctx


def direct_value(rho,P):
    n=P.nrows()
    sqrts=[arb(4*i+1).sqrt() for i in range(n)]
    denom=[math.prod(range(1,4*i+2,2)) for i in range(n)]
    pcoeff=[[acb(P[i,j]) for j in range(n)] for i in range(n)]
    def integrand(u,analytic):
        x=u/rho
        # Even ordinary Legendre basis, evaluated by its independent recurrence.
        previous=acb(1);current=x
        evens=[previous]
        for degree in range(1,2*n-1):
            nxt=((2*degree+1)*x*current-degree*previous)/(degree+1)
            previous,current=current,nxt
            if (degree+1)%2==0:
                evens.append(nxt)
        outer=[sqrts[j]*evens[j] for j in range(n)]
        z=2*arb.pi()*u
        arg=-(z*z)/4
        total=acb(0)
        for i in range(n):
            # j_(2i)(z) = z^(2i)/(4i+1)!! * 0F1(2i+3/2; -z²/4).
            # This is entire, so the analytic callback is valid on all boxes.
            inner=sqrts[i]*(-1)**i*z**(2*i)/denom[i]*arg.hypgeom_0f1(arb(4*i+3)/2)
            dot=sum((pcoeff[i][j]*outer[j] for j in range(n)),acb(0))
            total+=inner*dot
        return 2/rho.sqrt()*total
    length=Q(str(rho.fmpq()))-1
    count=max(1,math.ceil(4*length))
    total=acb(0)
    for k in range(count):
        a=main.ab(1+length*k/count);b=main.ab(1+length*(k+1)/count)
        value=acb.integral(integrand,acb(a),acb(b),
                           rel_tol=arb(2)**-90,abs_tol=arb(2)**-90,
                           deg_limit=128,eval_limit=100000,depth_limit=30)
        if not value.is_finite() or not value.imag.contains(0):
            raise ArithmeticError(value)
        total+=value
    return total.real


def run(numerics,output):
    global prolate,main
    sys.path.insert(0,str(numerics.resolve()))
    import prolate_certificate as prolate
    import sonin_scalar_epsilon as main
    bits=384
    terms,error,_,pcert,_=main.exponential_model(prolate,80,bits,arb(5))
    p2,C,R=prolate.certify(rank=32,precision_bits=bits)
    main.require(pcert['dyadic_inverse_sha256']==p2['dyadic_inverse_sha256'],
                 'The two routes must use the same exact dyadic inverse')
    P=C*R
    rows=[]
    for rho_exact in ('3/2','2','4'):
        rho=main.ab(rho_exact)
        polynomial=sum((c*(main.ab(lam)*rho.log()).exp() for lam,c in terms),arb(0))
        # This lower working precision is independent of the scalar polynomial evaluation.
        ctx.prec=192
        direct=direct_value(rho,P)
        ctx.prec=bits
        difference=polynomial-direct
        main.require(abs(difference)<main.ab('9e-28'),
                     f'Selected-point comparison failed: {difference}')
        rows.append({'rho':rho_exact,'finite_exponential_model':main.pack(polynomial),
                     'finite_Bessel_integral':main.pack(direct),
                     'difference':main.pack(difference)})
        print(json.dumps({'rho':rho_exact,'polynomial':str(polynomial),
                          'bessel_integral':str(direct),'difference':str(difference)}),flush=True)
    result={'status':'PASSED_SELECTED_POINT_CONTROL',
            'date':'2026-09-29','prepared_for':'Edward Baker','model':'GPT-6 (Codex)',
            'serving_variant':'not exposed','reasoning_effort':'not exposed',
            'provenance':'Prepared with LLM assistance; internal same-model control, not independent human refereeing.',
            'scope':'Independent selected-point finite-kernel normalization control, not a new epsilon approximation theorem.',
            'polynomial_precision_bits':bits,'Bessel_quadrature_precision_bits':192,
            'rank':32,'cosine_terms':80,
            'comparison_abs_tolerance':'9e-28',
            'full_kernel_approximation_error':main.pack(error),
            'inverse_sha256':pcert['dyadic_inverse_sha256'],
            'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'script_hashes':{name:hashlib.sha256(path.read_bytes()).hexdigest() for name,path in
                [('epsilon_selected_point_review.py',Path(__file__)),
                 ('prolate_certificate.py',Path(prolate.__file__)),
                 ('sonin_scalar_epsilon.py',Path(main.__file__))]},
            'runtime':{'python':platform.python_version(),'python_flint':flint.__version__,
                       'flint':flint.__FLINT_VERSION__},
            'rows':rows}
    output.parent.mkdir(parents=True,exist_ok=True)
    output.write_text(json.dumps(result,indent=2)+'\n')
    return result


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--numerics',type=Path,default=Path(__file__).resolve().parent)
    parser.add_argument('--output',type=Path,default=Path(__file__).resolve().parent/'records/epsilon_selected_point_review.json')
    args=parser.parse_args()
    run(args.numerics,args.output)
