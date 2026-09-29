#!/usr/bin/env python3
"""Multiprecision checks of closed CCM blocks and structured tail coupling.

The analytic certificate is separate, in certify_odd_tail.py. These eigenvalue
and coupling diagnostics are not interval certificates; no zeta zeros are used.
"""
import argparse
from decimal import Decimal,InvalidOperation,localcontext
from fractions import Fraction
import hashlib
import json
import platform
from pathlib import Path

import mpmath as mp

from check_mass_stiffness import weil_matrix,scaled_error,strings

HERE=Path(__file__).resolve().parent
SOURCES=('check_odd_blocks.py','check_mass_stiffness.py','certify_odd_tail.py')
POWERS=((2,2),(3,3),(4,2),(5,5),(7,7),(8,2),(9,3),(11,11))


def coefficients(nmax):
    """Closed digamma/trigamma formulas, independently checked by quadrature."""
    length=mp.log(13)
    count=int(mp.ceil((mp.mp.dps+20)*mp.log(10)/mp.log(169)))
    exp_terms=[mp.power(13,-mp.mpf('.5'))/mp.power(169,k) for k in range(count)]
    b={};odd={}
    sinh2=mp.sinh(length/4)**2
    for n in range(1,nmax+1):
        d=2*mp.pi*n/length;z=mp.mpf('.25')+1j*d/2
        psi=mp.digamma(z);trigamma=mp.polygamma(1,z)
        pole_sin=-2*d*(mp.cosh(length/2)-1)/(d*d+mp.mpf('.25'))
        sine_arch=mp.im(psi)/2-mp.fsum(
            d*e/((2*k+mp.mpf('.5'))**2+d*d) for k,e in enumerate(exp_terms))
        sine_prime=mp.fsum(mp.log(p)/mp.sqrt(q)*mp.sin(d*mp.log(q)) for q,p in POWERS)
        b[n]=(sine_arch+sine_prime-pole_sin)/mp.pi
        arch=mp.re(psi)-mp.log(mp.pi)-mp.im(psi)/(length*d)+mp.re(trigamma)/(2*length)
        arch+=4*d*d/length*mp.fsum(
            e/((2*k+mp.mpf('.5'))**2+d*d)**2 for k,e in enumerate(exp_terms))
        pole=-16*sinh2*d*d/(length*(d*d+mp.mpf('.25'))**2)
        prime=mp.fsum(mp.log(p)/mp.sqrt(q)*(2*(1-mp.log(q)/length)*mp.cos(d*mp.log(q))
                     +2*mp.sin(d*mp.log(q))/(length*d)) for q,p in POWERS)
        odd[n]=arch+pole-prime
    constant_arch=mp.digamma(mp.mpf('.25'))-mp.log(mp.pi)+mp.polygamma(1,mp.mpf('.25'))/(2*length)
    constant_arch-=2/length*mp.fsum(e/(2*k+mp.mpf('.5'))**2 for k,e in enumerate(exp_terms))
    constant=constant_arch+32*sinh2/length-mp.fsum(
        2*mp.log(p)/mp.sqrt(q)*(1-mp.log(q)/length) for q,p in POWERS)
    return b,odd,constant


def blocks(n,b,odd,constant):
    wm=mp.zeros(n);wp=mp.zeros(n+1)
    wp[0,0]=constant
    for i in range(1,n+1):
        wm[i-1,i-1]=odd[i]
        wp[i,i]=odd[i]+2*b[i]/i
        wp[0,i]=wp[i,0]=mp.sqrt(2)*b[i]/i
        for j in range(1,i):
            wm[i-1,j-1]=wm[j-1,i-1]=2*(j*b[i]-i*b[j])/(i*i-j*j)
            wp[i,j]=wp[j,i]=2*(i*b[i]-j*b[j])/(i*i-j*j)
    return wp,wm


def coupling(m,n,b):
    return 2*(m*b[n]-n*b[m])/(n*n-m*m)


def finite_rank(m,n,b,q):
    return mp.fsum(-2*b[m]*mp.mpf(m)**(2*j)/mp.mpf(n)**(2*j+1)
                   +2*b[n]*mp.mpf(m)**(2*j+1)/mp.mpf(n)**(2*j+2)
                   for j in range(q))


def general_error_bound(r,K,q):
    # Proved uniform |b_n|<2; this weakened HS bound has no hidden finite cutoff.
    ratio=mp.mpf(r)/K;rho=mp.mpf(r)/(K+1)
    return 4/(1-rho*rho)*ratio**(2*q)*(1+ratio)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(digits,nvalues):
    mp.mp.dps=digits
    maxmode=max(2*max(nvalues),32)
    b,odd,constant=coefficients(maxmode)
    w,direct_error=weil_matrix(13,4)
    even,odd_basis=mp.zeros(9,5),mp.zeros(9,4)
    even[4,0]=1
    for j in range(1,5):
        even[4+j,j]=even[4-j,j]=1/mp.sqrt(2)
        odd_basis[4+j,j-1]=1/mp.sqrt(2)
        odd_basis[4-j,j-1]=-1/mp.sqrt(2)
    plus,minus=blocks(4,b,odd,constant)
    checks=dict(closed_even_vs_quadrature=scaled_error(plus,even.T*w*even),
                closed_odd_vs_quadrature=scaled_error(minus,odd_basis.T*w*odd_basis),
                selected_direct_entry=direct_error)
    # Check the rational enclosure witnesses against a different arithmetic path.
    from certify_odd_tail import certificate
    cert=certificate()
    def enclosed(value,box):
        bounds=[mp.mpf(str(Fraction(box[key]).numerator))/Fraction(box[key]).denominator
                for key in ('lower_rational','upper_rational')]
        return bounds[0]<=value<=bounds[1]
    bhigh,_,_=coefficients_sparse((4096,4097))
    cross=coupling(4096,4097,bhigh)
    if not enclosed(cross,cert['boundary_cross_entry']) or not enclosed(odd[1],cert['odd_first_diagonal']):
        raise ArithmeticError('Multiprecision value outside rational witness enclosure.')
    report=dict(date='2026-09-26',model='GPT-6 (Codex); exact variant and reasoning effort not exposed',
        status='multiprecision diagnostics, not interval eigenvalue enclosures',
        decimal_digits=digits,python=platform.python_version(),mpmath=mp.__version__,zero_data_used=False,
        sources_sha256={name:digest(HERE/name) for name in SOURCES},
        checks=checks,certificate_witnesses_enclose=True,cases=[],structured_tests=[])
    for n in nvalues:
        plus,minus=blocks(n,b,odd,constant)
        ep=mp.eigsy(plus,eigvals_only=True)
        em,vm=mp.eigsy(minus)
        v=vm[:,0]
        if em[0]<=ep[0]:
            raise ArithmeticError('Observed simple-even ordering failed.')
        crossblock=mp.matrix([[coupling(m,k,b) for m in range(1,n+1)] for k in range(n+1,2*n+1)])
        residual=crossblock*v
        s0=mp.fsum(b[m]*v[m-1] for m in range(1,n+1))
        t0=mp.fsum(m*v[m-1] for m in range(1,n+1))
        row=dict(N=n,least_even_ritz=ep[0],least_odd_ritz=em[0],finite_odd_gap=em[0]-ep[0],
            second_odd_ritz=em[1],cross_block_frobenius=mp.norm(crossblock),
            low_odd_mode_coupling_squared=mp.norm(residual)**2,
            low_odd_mode_relative_coupling=mp.norm(residual)**2/(em[0]-ep[0]),
            boundary_moment_abs=abs(s0),derivative_moment_abs=abs(t0),
            checks=dict(eigenpair_residual=mp.norm(minus*v-em[0]*v)))
        report['cases'].append(row)
        print(json.dumps(dict(N=n,odd_gap=mp.nstr(row['finite_odd_gap'],12),
            cross_norm=mp.nstr(row['cross_block_frobenius'],8),
            mode_coupling_squared=mp.nstr(row['low_odd_mode_coupling_squared'],8))),flush=True)
    for r,K in ((8,16),(16,32),(32,64)):
        for q in (0,2,4,8):
            values=[];identity_errors=[]
            for m in range(1,r+1):
                for n in range(K+1,2*K+1):
                    exact=coupling(m,n,b)
                    error=exact-finite_rank(m,n,b,q)
                    predicted=exact*(mp.mpf(m)/n)**(2*q)
                    values.append(abs(error)**2)
                    identity_errors.append(abs(error-predicted))
            measured=mp.sqrt(mp.fsum(values));bound=general_error_bound(r,K,q)
            if measured>bound:
                raise ArithmeticError('Structured remainder exceeds analytic bound.')
            report['structured_tests'].append(dict(retained=r,far_after=K,terms=q,rank_bound=2*q,
                finite_window_frobenius_error=measured,infinite_tail_operator_error_bound=bound,
                checks=dict(exact_remainder_identity=max(identity_errors))))
    residuals=list(checks.values())+[x['checks']['eigenpair_residual'] for x in report['cases']]
    residuals+=[x['checks']['exact_remainder_identity'] for x in report['structured_tests']]
    report['maximum_identity_residual']=max(residuals)
    if max(residuals)>mp.mpf('1e-80'):
        raise ArithmeticError('Reconstruction identity residual exceeds 1e-80.')
    return report


def coefficients_sparse(indices):
    """Only two distant b-coefficients; do not build a 4097-square matrix."""
    length=mp.log(13);out={}
    count=int(mp.ceil((mp.mp.dps+20)*mp.log(10)/mp.log(169)))
    for n in indices:
        d=2*mp.pi*n/length
        arch=mp.im(mp.digamma(mp.mpf('.25')+1j*d/2))/2-mp.fsum(
            d*mp.power(13,-2*k-mp.mpf('.5'))/((2*k+mp.mpf('.5'))**2+d*d) for k in range(count))
        pole=-2*d*(mp.cosh(length/2)-1)/(d*d+mp.mpf('.25'))
        prime=mp.fsum(mp.log(p)/mp.sqrt(q)*mp.sin(d*mp.log(q)) for q,p in POWERS)
        out[n]=(arch+prime-pole)/mp.pi
    return out,None,None


def comparison(paths):
    low,high=[json.loads(p.read_text()) for p in paths]
    for p,data in zip(paths,(low,high)):
        if set(data['sources_sha256'])!=set(SOURCES):
            raise ValueError('Unexpected source manifest.')
        for name in SOURCES:
            if data['sources_sha256'][name]!=digest(HERE/name):
                raise ValueError(f'{p}: stale source {name}; regenerate.')
    count=0;differences=[];maximum=Decimal(0)
    def compare(a,b,path):
        nonlocal count,maximum
        if type(a)!=type(b):raise ValueError('Type mismatch: '+path)
        if isinstance(a,dict):
            if set(a)!=set(b):raise ValueError('Key mismatch: '+path)
            for key in a:
                if key!='checks':compare(a[key],b[key],path+'/'+key)
        elif isinstance(a,list):
            if len(a)!=len(b):raise ValueError('Length mismatch: '+path)
            for j,(x,y) in enumerate(zip(a,b)):compare(x,y,path+'/'+str(j))
        elif isinstance(a,str):
            try:x,y=Decimal(a),Decimal(b)
            except InvalidOperation:
                if a!=b:raise ValueError('Label mismatch: '+path)
                return
            if not x.is_finite() or not y.is_finite():raise ValueError('Nonfinite observation')
            count+=1;error=abs(x-y)/max(Decimal(1),abs(x),abs(y));maximum=max(maximum,error)
            if a!=b:differences.append(dict(path=path,low=a,high=b,scaled_difference=str(error)))
        elif a!=b:raise ValueError('Discrete mismatch: '+path)
    with localcontext() as ctx:
        ctx.prec=100
        for key in ('cases','structured_tests','certificate_witnesses_enclose','zero_data_used'):
            compare(low[key],high[key],key)
    if maximum>Decimal('1e-43'):
        raise ArithmeticError('Precision agreement failed at 1e-43 scaled tolerance.')
    return dict(date='2026-09-26',status='precision comparison; not interval certification',
        source_sha256=digest(Path(__file__)),input_sha256={p.name:digest(p) for p in paths},
        generator_hashes_verified=True,numeric_observables=count,
        identical_at_all_45_saved_significant_digits=not differences,
        maximum_scaled_difference=str(maximum),differing_observables=differences,
        low_digits=low['decimal_digits'],high_digits=high['decimal_digits'],
        maximum_identity_residual_low=low['maximum_identity_residual'],
        maximum_identity_residual_high=high['maximum_identity_residual'])


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--digits',type=int,default=120)
    p.add_argument('--cutoffs',type=int,nargs='+',default=[8,16,32,64])
    p.add_argument('--compare',type=Path,nargs=2)
    p.add_argument('--output',type=Path,required=True)
    args=p.parse_args()
    if args.compare:
        data=comparison(args.compare)
    else:
        if args.digits<100 or min(args.cutoffs)<2 or max(args.cutoffs)<64:
            p.error('Use digits >= 100 and cutoffs >= 2, including a largest cutoff >= 64.')
        data=strings(run(args.digits,sorted(set(args.cutoffs))))
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(data,indent=2)+'\n')
    print('Record saved: '+str(args.output),flush=True)


if __name__=='__main__':
    main()
