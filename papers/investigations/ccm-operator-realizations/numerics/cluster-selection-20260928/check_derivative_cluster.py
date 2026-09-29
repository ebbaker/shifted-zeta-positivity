#!/usr/bin/env python3
"""Xi-derivative trial spaces and finite Schur correction at X=13.

GPT-6 (Codex); exact serving variant and effort not exposed. 2026-09-28.
Floating diagnostics only. The initial trial basis uses no eigenvector.
All dense matrices remain in memory, and no zero list is evaluated.
"""
import argparse
from functools import lru_cache
import hashlib
import json
import platform
from pathlib import Path
import sys
import time

sys.dont_write_bytecode=True
bootstrap=argparse.ArgumentParser(add_help=False)
bootstrap.add_argument('--repo-numerics',type=Path,default=Path(__file__).resolve().parent)
NUM=bootstrap.parse_known_args()[0].repo_numerics.resolve()
sys.path.insert(0,str(NUM))
import mpmath as mp
from check_odd_blocks import coefficients,blocks
from check_mass_stiffness import strings,weil_matrix,scaled_error


def polynomial(order):
    # d/dx[t^(5/4) exp(-t) P(t)] = same*( (5/2-2t)P+2tP' ).
    p=[-mp.mpf('1.5'),mp.mpf(1)]
    for _ in range(order):
        q=[mp.mpf(0)]*(len(p)+1)
        for j,c in enumerate(p):
            q[j]+=(2*j+mp.mpf('2.5'))*c
            q[j+1]-=2*c
        p=q
    return tuple(p)


@lru_cache(maxsize=None)
def kernel(x,order=0):
    x=mp.mpf(x)
    sign=-1 if x<0 and order%2 else 1
    u=mp.exp(abs(x))
    nmax=int(mp.ceil(mp.sqrt((mp.mp.dps+35)*mp.log(10)/mp.pi)/u))+2
    p=polynomial(order)
    def term(n):
        base=mp.pi*n*n
        t=base*u*u
        return base**(-mp.mpf('.25'))*t**mp.mpf('1.25')*mp.exp(-t)*mp.polyval(p[::-1],t)
    return sign*mp.fsum(term(n) for n in range(1,nmax+1))


def trial_coefficients(length,nmax):
    b=length/2
    points=[b*j/8 for j in range(9)]
    integral=lambda f:2*mp.quad(f,points,method='gauss-legendre')
    norm=mp.sqrt(integral(lambda x:kernel(x)**2))
    c0=mp.matrix(nmax+1,1)
    for n in range(nmax+1):
        d=2*mp.pi*n/length
        scale=mp.sqrt((1 if n==0 else 2)/length)
        c0[n]=scale*(-1)**n*integral(lambda x:kernel(x)*mp.cos(d*x))/norm
    first,third=kernel(b,1)/norm,kernel(b,3)/norm
    c2,c4=mp.zeros(nmax+1,1),mp.zeros(nmax+1,1)
    for n in range(nmax+1):
        d=2*mp.pi*n/length
        scale=mp.sqrt((1 if n==0 else 2)/length)
        c2[n]=-d*d*c0[n]+2*scale*first
        c4[n]=d**4*c0[n]-2*scale*d*d*first+2*scale*third
    checks={}
    for order,coeff in ((2,c2),(4,c4)):
        for n in (0,1,3):
            d=2*mp.pi*n/length
            scale=mp.sqrt((1 if n==0 else 2)/length)
            direct=scale*(-1)**n*integral(lambda x:kernel(x,order)*mp.cos(d*x))/norm
            checks[f'derivative_{order}_mode_{n}_integration_by_parts']=abs(direct-coeff[n])/max(1,abs(direct))
    # Direct differentiation provides a separate polynomial recurrence check.
    for order in (1,2,3,4):
        x=mp.mpf('.4')
        direct=mp.diff(lambda y:uncached_base(y),x,order)
        checks[f'analytic_derivative_{order}']=abs(direct-kernel(x,order))/max(1,abs(direct))
    return (c0,c2,c4),dict(normalization=norm,k_at_endpoint=kernel(b),
        first_derivative_at_endpoint=kernel(b,1),third_derivative_at_endpoint=kernel(b,3),checks=checks)


def uncached_base(x):
    # Used only for differentiation controls; avoids cached low-precision nodes.
    u=mp.exp(x)
    nmax=int(mp.ceil(mp.sqrt((mp.mp.dps+35)*mp.log(10)/mp.pi)/u))+2
    return mp.sqrt(u)*mp.fsum(mp.pi/2*(n*u)**2*(2*mp.pi*(n*u)**2-3)*
         mp.exp(-mp.pi*(n*u)**2) for n in range(1,nmax+1))


def align(v,ref):
    v=v/mp.norm(v)
    if (v.T*ref)[0]<0:v=-v
    return v


def profile(v,ground,base,length):
    v=align(v,ground)
    mean=mp.sqrt(length)*v[0]
    moment=length**2/24+mp.sqrt(2)/v[0]*mp.fsum(v[n]/(2*mp.pi*n/length)**2 for n in range(1,v.rows))
    return dict(overlap_true_ground=(v.T*ground)[0],distance_true_ground=mp.norm(v-ground),
        overlap_xi_proxy=abs((v.T*base)[0]),signed_half_second_moment=moment,mean=mean)


def trial_case(A,ground,eigen,n,dimension,columns,length):
    raw=mp.matrix(n+1,dimension)
    for j in range(dimension):
        v=columns[j][:n+1,:]
        raw[:,j]=v/mp.norm(v)
    orth,R=mp.qr(raw,mode='full')
    S,T=orth[:,:dimension],orth[:,dimension:]
    if (S[:,0].T*raw[:,0])[0]<0:S[:,0]=-S[:,0]
    H=S.T*A*S
    C=T.T*A*S
    D=T.T*A*T
    H=(H+H.T)/2
    D=(D+D.T)/2
    he,hv=mp.eigsy(H)
    de=mp.eigsy(D,eigvals_only=True)
    base=raw[:,0]
    ptrue=S.T*ground
    capture=mp.norm(ptrue)
    ptrue/=capture
    ritz=S*hv[:,0]
    out=dict(N=n,trial_dimension=dimension,trial_derivatives=[2*j for j in range(dimension)],
        actual_even_ground=eigen[0],actual_second_even=eigen[1],
        base_profile=profile(base,ground,base,length),
        trial_gram=raw.T*raw,trial_H=H,trial_ritz_eigenvalues=list(he),
        trial_ritz_profile=profile(ritz,ground,base,length),
        best_ground_projection_norm=capture,best_ground_projection_distance=mp.sqrt(max(0,2-2*capture)),
        trial_ritz_projected_orientation_overlap=abs((hv[:,0].T*ptrue)[0]),
        complement_min_eigenvalue=de[0],complement_first_three_eigenvalues=list(de[:3]),
        complement_positive_observed=bool(de[0]>0),coupling_frobenius_norm=mp.norm(C),
        H_frobenius_norm=mp.norm(H),actual_ground_over_complement_min=abs(eigen[0])/de[0],
        checks=dict(orthonormality=mp.norm(orth.T*orth-mp.eye(n+1)),
            decomposition=scaled_error(A,orth*mp.matrix([[0]])*orth.T) if False else
             scaled_error(A,S*H*S.T+S*C.T*T.T+T*C*S.T+T*D*T.T)))
    if de[0]<=0:
        out['schur_status']='not computed: D positivity not observed'
        return out
    Z=mp.matrix(D.rows,dimension)
    for j in range(dimension):Z[:,j]=mp.lu_solve(D,C[:,j])
    correction=C.T*Z
    correction=(correction+correction.T)/2
    F=H-correction
    fe,fv=mp.eigsy(F)
    lifted=S-T*Z
    metric=mp.eye(dimension)+Z.T*Z
    lower=mp.cholesky(metric)
    inverse=lower**-1
    effective=inverse*F*inverse.T
    effective=(effective+effective.T)/2
    ge,gv=mp.eigsy(effective)
    gp=(lower.T**-1)*gv[:,0]
    plainp=fv[:,0]
    plainlift=lifted*plainp
    harmonic=lifted*gp
    harmonic=align(harmonic,ground)
    hray=(harmonic.T*A*harmonic)[0]
    out.update(schur_status='E=0 calculated after positive finite D observed',
        schur_correction=correction,schur_F=F,schur_eigenvalues=list(fe),
        correction_frobenius_norm=mp.norm(correction),F_frobenius_norm=mp.norm(F),
        F_over_H_norm=mp.norm(F)/mp.norm(H),
        cancellation_decimal_digits=mp.log10(mp.norm(H)/mp.norm(F)),
        schur_plain_head_profile=profile(S*plainp,ground,base,length),
        schur_plain_lifted_profile=profile(plainlift,ground,base,length),
        schur_plain_projected_orientation_overlap=abs((plainp.T*ptrue)[0]),
        lift_metric=metric,harmonic_ritz_eigenvalues=list(ge),
        harmonic_ritz_profile=profile(harmonic,ground,base,length),
        harmonic_ritz_rayleigh=hray,
        harmonic_ritz_full_residual=mp.norm(A*harmonic-hray*harmonic),
        harmonic_ritz_energy_over_true_ground=ge[0]/eigen[0],
        harmonic_ritz_projected_orientation_overlap=abs((gp.T*ptrue)[0])/mp.norm(gp),
        harmonic_lift_norm=mp.norm(Z))
    out['checks'].update(solve_scaled=scaled_error(D*Z,C),
        solve_relative_to_C=mp.norm(D*Z-C)/mp.norm(C),
        energy_congruence=mp.norm(lifted.T*A*lifted-F)/max(mp.norm(F),mp.mpf('1e-200')),
        mass_congruence=scaled_error(lifted.T*lifted,metric),
        generalized_rayleigh_relative=abs(hray-ge[0])/max(abs(ge[0]),mp.mpf('1e-200')))
    return out


def run(digits,cutoffs,output):
    mp.mp.dps=digits
    kernel.cache_clear()
    length=mp.log(13)
    started=time.monotonic()
    data=coefficients(max(cutoffs))
    columns,candidate_checks=trial_coefficients(length,max(cutoffs))
    report=dict(date='2026-09-28',model='GPT-6 (Codex)',exact_serving_variant='not exposed',
        reasoning_effort='not exposed',status='multiprecision diagnostics; not interval certified',
        digits=digits,X=13,L=length,python=platform.python_version(),mpmath=mp.__version__,
        zero_data_used=False,initial_trial_space_uses_eigenvectors=False,
        basis='Orthonormal QR of separately normalized projections of k,k second derivative,k fourth derivative; integration-by-parts endpoint corrections included.',
        schur_scope='E=0 on finite Fourier complement. Harmonic lift is A-dependent and has its own induced mass metric. No infinite-tail bound.',
        source_hashes={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in
            (Path(__file__),NUM/'check_odd_blocks.py',NUM/'check_mass_stiffness.py')},
        candidate_controls=candidate_checks,cases=[])
    for n in cutoffs:
        A,_=blocks(n,*data)
        eigen,vec=mp.eigsy(A)
        ground=align(vec[:,0],columns[0][:n+1,:])
        for dimension in (2,3):
            row=trial_case(A,ground,eigen,n,dimension,columns,length)
            report['cases'].append(row)
            output.write_text(json.dumps(strings(report),indent=2)+'\n')
            print(json.dumps(strings(dict(N=n,dim=dimension,D_min=row['complement_min_eigenvalue'],
                ritz_distance=row['trial_ritz_profile']['distance_true_ground'],
                best_distance=row['best_ground_projection_distance'],
                harmonic_distance=row.get('harmonic_ritz_profile',{}).get('distance_true_ground'),
                cancellation_digits=row.get('cancellation_decimal_digits'),
                H_min=row['trial_ritz_eigenvalues'][0],F_min=row.get('schur_eigenvalues',[None])[0],
                elapsed=time.monotonic()-started))),flush=True)
    return report


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--repo-numerics',type=Path,default=Path(__file__).resolve().parent)
    p.add_argument('--digits',type=int,default=130)
    p.add_argument('--cutoffs',nargs='+',type=int,default=[32,64])
    p.add_argument('--output',type=Path,required=True)
    args=p.parse_args()
    if args.digits<90 or any(n<4 for n in args.cutoffs):p.error('Use >=90 digits and cutoff>=4')
    args.output.parent.mkdir(parents=True,exist_ok=True)
    report=run(args.digits,sorted(set(args.cutoffs)),args.output)
    args.output.write_text(json.dumps(strings(report),indent=2)+'\n')
