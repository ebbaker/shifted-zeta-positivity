#!/usr/bin/env python3
"""Certify Q >= 9/100 ||F||^2 on the length-one three-moment source space.

Prepared for Edward Baker, 2026-10-03, with substantial LLM assistance.
Model: GPT-6 (Codex); exact serving variant and effort are not exposed.
See LOCAL_COERCIVITY_LOW_BAND_20261003.md for the analytic proof.
Only small certificate records are saved; all derived matrices are regenerated.
"""
import argparse, hashlib, json, platform, time
from pathlib import Path
import flint
from flint import arb, acb, arb_mat, ctx

def pack(x):
    if not x.is_finite():raise ArithmeticError('Non-finite enclosure')
    return {'lower':str(x.lower().fmpq()), 'upper':str(x.upper().fmpq())}

def ldl_positive(matrix):
    """Outward LDL pivots of a symmetric real ball matrix, no eigenvalue sampling."""
    n=matrix.nrows();L=arb_mat(n,n);ds=[]
    for j in range(n):
        dj=matrix[j,j]-sum((L[j,k]*L[j,k]*ds[k] for k in range(j)),arb(0))
        if not dj>0:raise ArithmeticError('Unproved positive LDL pivot')
        ds.append(dj);L[j,j]=1
        for i in range(j+1,n):
            L[i,j]=(matrix[i,j]-sum((L[i,k]*L[j,k]*ds[k] for k in range(j)),arb(0)))/dj
    return min(x.lower() for x in ds)

def plane_tail(rank,z):
    d=1
    for j in range(rank+1):d*=2*j+1
    ratio=z*z/((2*rank+1)*(2*rank+3))
    if not ratio<1:raise ArithmeticError('Tail ratio not below one')
    return ((2*rank+1)*z**(2*rank)/(d*d)/(1-ratio)).sqrt()

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--nodes',type=int,default=46000)
    p.add_argument('--rank',type=int,default=40)
    p.add_argument('--bits',type=int,default=192)
    p.add_argument('--output',type=Path,required=True)
    args=p.parse_args()
    if args.nodes<=0 or args.rank<4 or args.rank%2 or args.bits<64:
        p.error('Require positive nodes, even rank at least four, and at least 64 bits')
    ctx.prec=args.bits
    start=time.time();M=args.rank;n=args.nodes
    pi=arb.pi();a=arb(2).log();c=arb(2).sqrt()*a
    h=arb(46)/n
    mats=[arb_mat(M//2,M//2),arb_mat(M//2,M//2)]
    panels=[[],[]];wp=[];active=0;Wmid=arb(0)
    fac=[];us=[];uc=[];d=1
    sh=(arb(1)/4).sinh();ch=(arb(1)/4).cosh();mean=4*sh
    ns=(arb(1)/2).sinh()-arb(1)/2
    nc=(arb(1)/2).sinh()+arb(1)/2-mean*mean
    if not ns>0 or not nc>0:raise ArithmeticError('Constraint norms are not proved positive')
    for j in range(M):
        if j:d*=2*j+1
        fac.append(arb(2*j+1).sqrt()/d*((-1)**(j//2)))
        coeff=arb(2*j+1).sqrt()/d*(arb(1)/4)**j*(arb(1)/64).hypgeom_0f1(arb(j)+arb(3)/2)
        us.append(coeff/ns.sqrt() if j%2 else arb(0))
        uc.append(coeff/nc.sqrt() if j>0 and j%2==0 else arb(0))
    def flush():
        nonlocal panels,wp,mats
        if not wp:return
        for parity in [0,1]:
            L=arb_mat([[panels[parity][k][j]*wp[k] for k in range(len(wp))] for j in range(M//2)])
            R=arb_mat([[panels[parity][k][j] for k in range(len(wp))] for j in range(M//2)])
            mats[parity]+=L*R.transpose()
        panels=[[],[]];wp=[]
    for k in range(n):
        t=arb(46)*(2*k+1)/(2*n)
        gamma=acb(arb(1)/4,t/2).digamma().real-pi.log()
        z=1-gamma+c*(a*t).cos()
        if z.upper()<=0:continue
        if z.lower()<0:
            u=z.upper();z=arb(u/2,u/2)
        Wmid+=h*z
        w=h*z/pi
        v=t/2;q=-v*v/4
        sinc=v.sin()/v
        bs=2*(ch*v.sin()/2-t*sh*v.cos())/(arb(1)/4+t*t)
        bc=2*(sh*v.cos()/2+t*ch*v.sin())/(arb(1)/4+t*t)
        oddcoef=bs/ns.sqrt();evencoef=(bc-mean*sinc)/nc.sqrt()
        vals=[];power=arb(1)
        for j in range(M):
            raw=fac[j]*power*q.hypgeom_0f1(arb(j)+arb(3)/2)
            vals.append(raw-us[j]*oddcoef-uc[j]*evencoef if j else arb(0))
            power*=v
        panels[0].append(vals[::2]);panels[1].append(vals[1::2]);wp.append(w);active+=1
        if len(wp)>=256:flush()
        if k and k%5000==0:print(json.dumps({'node':k,'active':active,'seconds':time.time()-start}),flush=True)
    flush()
    # A matrix bound, not just computed floating eigenvalues.
    pivots=[]
    for mat in mats:
        test=arb_mat([[arb(9)/10*(i==j)-mat[i,j] for j in range(M//2)] for i in range(M//2)])
        pivots.append(ldl_positive(test))
    gamma0=acb(arb(1)/4).digamma().real-pi.log()
    gammaT=acb(arb(1)/4,arb(23)).digamma().real-pi.log()
    if not gammaT>1+c:raise ArithmeticError('Frequency tail cutoff unproved')
    V0=gammaT-gamma0+c*a*46
    Wbound=Wmid+h*V0/2
    quadrature=h/(2*pi)*(V0+Wbound/arb(3).sqrt())
    tail=plane_tail(M,arb(23))+(arb(1)/4).exp()*plane_tail(M,arb(1)/4)*(1/ns.sqrt()+1/nc.sqrt())
    truncation=2*tail*Wbound/pi
    error=quadrature+truncation
    if not error<arb(1)/100:raise ArithmeticError('Remainder budget exceeds 0.01')
    # The compact correction norm uses the separately inherited boundary gap.
    g=(17-12*arb(2).sqrt())*arb(57)/10**6
    k=((1-g)/g).sqrt()
    if not k<772:raise ArithmeticError('Correction norm bound exceeds 772')
    payload=[[[pack(mat[i,j]) for j in range(M//2)] for i in range(M//2)] for mat in mats]
    result={'status':'CERTIFIED_FIRST_PRIME_PREPARED_MEAN_ZERO_GAP','nodes':n,'rank':M,'bits':args.bits,'cutoff':'46','lambda':'1','constraints':['mean','exp(x/2)','exp(-x/2)'],'active_nodes':active,'seconds':time.time()-start,'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'matrix_enclosure_sha256':hashlib.sha256(json.dumps(payload,sort_keys=True,separators=(',',':')).encode()).hexdigest(),'matrix_upper_bound':'9/10','parity_LDL_min_pivots':[pack(x) for x in pivots],'weight_midpoint_integral':pack(Wmid),'weight_total_variation_bound':pack(V0),'weight_integral_upper_bound':pack(Wbound),'matrix_midpoint_error_bound':pack(quadrature),'projected_plane_tail_bound':pack(tail),'operator_truncation_error_bound':pack(truncation),'total_error_bound':pack(error),'Q_norm_gap':'9/100','inherited_boundary_gap':pack(g),'correction_norm_bound_evaluation':pack(k),'correction_norm_cap':'772','retained_B_fraction':'9/77209','relative_K_upper_fraction':'77200/77209','limitations':['Mean-zero and both pole-neutrality moments are required.','Only source support in (-1/2,1/2) and prime set {2}.','Correction norm and retained-B comparison depend on the inherited archimedean gap certificate.','Does not establish domination of the unweighted positive spectral part K_plus.']}
    result.update({'date':'2026-10-03','model':'GPT-6 (Codex)','serving_variant':'not exposed','reasoning_effort':'not exposed','runtime':{'python':platform.python_version(),'python_flint':flint.__version__,'flint':flint.__FLINT_VERSION__},'simple_retained_B_fraction':'1/9000','frequency_cutoff_margin':pack(gammaT-1-c)})
    args.output.write_text(json.dumps(result)+'\n')
    print(json.dumps({k:result[k] for k in ['status','nodes','rank','bits','seconds','Q_norm_gap','simple_retained_B_fraction']}),flush=True)

if __name__=='__main__':main()
