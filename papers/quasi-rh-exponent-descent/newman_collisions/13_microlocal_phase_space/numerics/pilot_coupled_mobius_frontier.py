#!/usr/bin/env python3
"""All-coefficient numerical Möbius frontier, without an ordered-pair expansion.

The source-bound sibling supplies actual complete phases and physical data.
All q with nonzero c_J(q) are retained; q>N/2 has exactly zero singleton
Jdagger by its polynomial identity. Fraction controls verify that identity
and the direct pair/gcd interpretation at small formal sample sizes.
"""
import argparse
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import math
import platform
import sys
import time
import numpy as np

BASE=Path(__file__).with_name('pilot_complete_centered_jets.py')
EXPECTED='4534bae2445bb3e0c6b0a5086194abd9bec2acbb559c3f5576557f7ec19dd9b3'
if hashlib.sha256(BASE.read_bytes()).hexdigest()!=EXPECTED:
    raise RuntimeError('Source-bound sibling pilot mismatch; restore the retained source.')
import pilot_complete_centered_jets as base


def mobius(N):
    least=[0]*(N+1);primes=[];mu=np.zeros(N+1,dtype=np.int64);mu[1]=1
    for n in range(2,N+1):
        if not least[n]:least[n]=n;primes.append(n);mu[n]=-1
        for p in primes:
            if p*n>N:break
            least[p*n]=p
            if n%p==0:mu[p*n]=0;break
            mu[p*n]=-mu[n]
    return mu


def coefficients(N,J):
    mu=mobius(N);cj=np.zeros(N+1,dtype=np.int64)
    for j in range(1,J+1):cj[j::j]+=mu[1:N//j+1]
    assert cj[1]==1 and np.all(cj[2:J+1]==0)
    assert np.all(cj[J+1:min(N,2*J)+1]==-1)
    total=np.zeros(N+1,dtype=np.int64)
    for q in range(1,N+1):
        if cj[q]:total[q::q]+=cj[q]
    target=np.zeros(N+1,dtype=np.int64);target[1:J+1]=1
    assert np.array_equal(total,target)
    return cj


def exact_J(m,epsilon):
    x=[z[0] for z in m];y=[z[1] for z in m]
    return [2*y[3]**2+3*x[2]*x[4]-3*x[0]*x[6]
             +2*epsilon*x[0]*y[6]-2*(y[1]+epsilon*x[1])*y[5],
            -x[2]**2+x[0]*x[4]]


def exact_controls():
    checks=0
    for N in range(1,13):
        eps=F(1,7)
        terms=[]
        for n in range(1,N+1):
            rho=F(n-N,N)
            r,i=F(n+1,n+3),F(2*n-3,n+5)
            terms.append([[r*rho**k,i*rho**k] for k in range(7)])
            assert exact_J(terms[-1],eps)==[0,0];checks+=1
        def summed(indices):
            return [[sum((terms[n][k][j] for n in indices),F(0)) for j in range(2)] for k in range(7)]
        for J in range(1,N+1):
            cj=coefficients(N,J)
            direct=[F(0),F(0)]
            for n in range(1,N+1):
                for m in range(1,N+1):
                    if math.gcd(n,m)>J:continue
                    combined=[[terms[n-1][k][j]+terms[m-1][k][j] for j in range(2)] for k in range(7)]
                    kernel=exact_J(combined,eps)
                    for k in range(2):direct[k]+=kernel[k]/2
            coupled=[F(0),F(0)]
            for q in range(1,N+1):
                block=exact_J(summed(range(q-1,N,q)),eps)
                for k in range(2):coupled[k]+=int(cj[q])*block[k]
            assert direct==coupled;checks+=2
    return checks


def channels(m,eps):
    """Difference and reflected-product coefficients, each affine in Gamma."""
    m0,m1,m2,m3,m4,m5,m6=m
    difference=[abs(m3)**2+1.5*(m2*m4.conjugate()).real
        -1.5*(m0*m6.conjugate()).real-eps*(m0*m6.conjugate()).imag
        -((1+1j*eps)*m1*m5.conjugate()).real,
        -.5*abs(m2)**2+.5*(m0*m4.conjugate()).real]
    product=[-(m3*m3).real+1.5*(m2*m4).real-1.5*(m0*m6).real
        +eps*(m0*m6).imag+((1+1j*eps)*m1*m5).real,
        -.5*(m2*m2).real+.5*(m0*m4).real]
    return np.array(difference),np.array(product)


def cross_J(b,c,eps):
    zB,zC=b[1].imag+eps*b[1].real,c[1].imag+eps*c[1].real
    return np.array([4*b[3].imag*c[3].imag
       +3*(b[2].real*c[4].real+c[2].real*b[4].real)
       -3*(b[0].real*c[6].real+c[0].real*b[6].real)
       +2*eps*(b[0].real*c[6].imag+c[0].real*b[6].imag)
       -2*(zB*c[5].imag+zC*b[5].imag),
       -2*b[2].real*c[2].real+b[0].real*c[4].real+c[0].real*b[4].real])


def exact_cutoff_power(N):
    J=math.ceil(N**.4)
    while (J-1)**5>=N*N:J-=1
    while J**5<N*N:J+=1
    assert (J-1)**5<N*N<=J**5
    return J


def calculate(q0,logs,N,h,cj,J):
    data=base.physical_data(N,h);eps=data['epsilon']
    q=base.transported_q(q0,logs,data);rho=logs-data['mu']
    powers=[np.ones(N)]
    for _ in range(6):powers.append(powers[-1]*rho)
    weighted=[q*p for p in powers]
    bands={k:[] for k in ('q1','first_active_band','all_q_above_2J')}
    maxima={'channels':0.,'BB_CC_BC':0.}
    q1=None
    singleton_coeff_nonzero=0
    for step in range(1,N+1):
        coeff=int(cj[step])
        if not coeff:continue
        if step>N//2:
            singleton_coeff_nonzero+=1
            # Exact degree-six diagonal-annihilation identity, checked over
            # Fractions below, makes all complete/same-block terms zero.
            continue
        m=[complex(np.sum(z[step-1::step])) for z in weighted]
        k=(N//2)//step
        mb=[complex(np.sum(z[(k+1)*step-1::step])) for z in weighted]
        mc=[complex(np.sum(z[step-1:k*step:step])) for z in weighted]
        full=np.array(base.affine_J(m,eps));bb=np.array(base.affine_J(mb,eps))
        cc=np.array(base.affine_J(mc,eps));bc=cross_J(mb,mc,eps)
        diff,prod=channels(m,eps)
        maxima['channels']=max(maxima['channels'],float(np.max(np.abs(full-diff-prod))))
        maxima['BB_CC_BC']=max(maxima['BB_CC_BC'],float(np.max(np.abs(full-bb-cc-bc))))
        if step==1:q1={'moments_0_to_6':[[z.real,z.imag] for z in m],
              'Jdagger_affine':full.tolist(),'difference_affine':diff.tolist(),'product_affine':prod.tolist()}
        name='q1' if step==1 else ('first_active_band' if step<=2*J else 'all_q_above_2J')
        bands[name].append(coeff*np.concatenate((full,diff,prod,bb,cc,bc)))
    summed={name:[math.fsum(float(a[k]) for a in values) for k in range(12)]
            for name,values in bands.items()}
    total=[math.fsum(summed[name][k] for name in summed) for k in range(12)]
    def unpack(v):
        return {name:v[k:k+2] for name,k in (('Jdagger_affine',0),('difference_affine',2),
           ('product_affine',4),('BB_affine',6),('CC_affine',8),('BC_affine',10))}
    scale=max(1,*[abs(v) for v in total])
    assert max(maxima.values())<1e-10*scale
    affine=total[:2]
    endpoints=[data['Gamma0'],data['Gamma0']+data['density']]
    return {'N':N,'height_offset':h,'J':J,
       'frontier':'all ordered pairs with gcd(n,m)<=J, represented by every exact c_J(q)',
       'Gamma0':data['Gamma0'],'density_coefficient':data['density'],
       'Gamma_formula':'Gamma0+density_coefficient/(4*C_count+1)^2; no count constant chosen',
       'bands':{name:unpack(v) for name,v in summed.items()},'complete_frontier':unpack(total),
       'frontier_Jdagger_at_Gamma_range_endpoints':[base.eval_affine(affine,g) for g in endpoints],
       'q1_complete_state':q1,'identity_maximum_absolute_errors':maxima,
       'singleton_sublattices_with_nonzero_cJ_optimized_exactly':singleton_coeff_nonzero,
       'scope':'Numerical signed frontier, not a candidate-conditioned sign or threshold theorem.'}


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--N',type=int,default=100000)
    parser.add_argument('--output',required=True);args=parser.parse_args()
    start=time.time();checks=exact_controls();N=args.N;J=exact_cutoff_power(N)
    cj=coefficients(N,J)
    q0,logs=base.decimal_complete(N,0,55,return_array=True)
    samples=[calculate(q0,logs,N,h,cj,J) for h in (0,.35)]
    out={'date':'2026-10-10','status':'PASS',
       'scope':'Bounded numerical coupled Möbius frontier; exact rational controls are formal identities, not actual heat-sign certificates.',
       'model':'GPT-6 (Codex); exact serving variant and effort unavailable, not inferred',
       'N':N,'J':J,'complexity':'O(N logN) summed sublattice terms; no N squared ordered-pair expansion',
       'exact_fraction_assertions':checks,'full_integer_divisor_identity_checked_through':N,
       'cJ_nonzero_count':int(np.count_nonzero(cj)),
       'cJ_minimum':int(np.min(cj[1:])),'cJ_maximum':int(np.max(cj[1:])),
       'cJ_histogram':{str(int(k)):int(v) for k,v in zip(*np.unique(cj[1:],return_counts=True))},
       'first_active_band_count':min(N,2*J)-J,'first_active_band_all_coefficients_minus_one':True,
       'all_q_above_2J_retained':'Every nonzero coefficient retained, with exact zero singleton optimization for q>N/2.',
       'samples':samples,'elapsed_seconds':time.time()-start,'python_executable':sys.executable,
       'python_version':platform.python_version(),'numpy_version':np.__version__,
       'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
       'dependency_sha256':EXPECTED,'dependency_hash_checked_before_import':True,
       'source_interface':'09_prime_phase_torus/notes/9_COUPLED_MOBIUS_PRIMITIVE_FRONTIER_AND_RESONANT_SUBLATTICES_20261010.md equations5-8; degree-six Jdagger from prime-torus manuscript',
       'limitations':['No candidate constraint is applied to individual sublattices.',
          'No constant in the zero count is assigned; no all-real or finite-height count range is checked.',
          'The actual numerical signs are not interval enclosures.',
          'Formal rational controls verify exact kernels and grouping, not huge-height arithmetic signs.']}
    Path(args.output).write_text(json.dumps(out,indent=2,allow_nan=False)+'\n')
    print(json.dumps({'status':'PASS','output':args.output,'elapsed_seconds':out['elapsed_seconds'],
                     'exact_fraction_assertions':checks}),flush=True)


if __name__=='__main__':main()
