#!/usr/bin/env python3
"""Finite-input diagnostics for the first-prime generator coupling.

Full local form coefficients use inherited translation-correlation quadrature.
The mixed kernel uses physical-delay cross sections, independently of the
certificate's exponential series. Floating norms are NOT all-input bounds.
"""
import argparse
import hashlib
import importlib.util
import json
import math
import platform
from fractions import Fraction
from pathlib import Path
import numpy as np


def load(path):
    spec=importlib.util.spec_from_file_location('append_diagnostic',path)
    mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
    return mod


def mixed(d,L,h,n,order,inner):
    z,w=np.polynomial.legendre.leggauss(order)
    q,wq=np.polynomial.legendre.leggauss(inner);q=(q+1)/2;wq=wq/2
    out=np.zeros((n,n))
    edges=[0,min(h,L),max(h,L),L+h]
    for left,right in zip(edges[:-1],edges[1:]):
        for u,wt in zip(left+(right-left)*(z+1)/2,(right-left)*w/2):
            lo=max(0,u-L);hi=min(h,u);t=lo+(hi-lo)*q
            kernel=math.exp(-2.5*u)/(-math.expm1(-2*u))-math.exp(u/2)
            out+=wt*(hi-lo)*kernel*d.gram(d.basis(t,h,n),wq,d.basis(u-t,L,n))
    a=math.log(2);lo=max(0,a-L);hi=min(h,a);r=np.zeros_like(out)
    if hi>lo:
        t=lo+(hi-lo)*(z+1)/2
        r=d.gram(d.basis(t,h,n),(hi-lo)*w/2,d.basis(a-t,L,n))
    return out,math.log(2)/math.sqrt(2)*r


def tower(ell,n,M):
    rho=np.full(n,math.sqrt(2/ell));rho[0]=1/math.sqrt(ell)
    k=np.arange(n)*math.pi/ell;rates=2*np.arange(M)+.5
    den=rates[:,None]**2+k[None,:]**2
    w0=-.5772156649015329-math.pi/2-3*math.log(2)-math.log(math.pi)
    diag=w0+np.sum((2/rates)[:,None]*k[None,:]**2/den,axis=0)
    feat=np.sqrt(2*rates[:,None]**2*(1-(-1.)**np.arange(n)[None,:]*np.exp(-rates[:,None]*ell)))*rho[None,:]/den
    q=np.diag(diag)
    for parity in (0,1):q[parity::2,parity::2]+=feat[:,parity::2].T@feat[:,parity::2]
    c=math.sinh(ell/4)*rho/(.25+k*k);s=-math.cosh(ell/4)*rho/(.25+k*k)
    c[1::2]=0;s[::2]=0
    return q+2*np.outer(c,c)-2*np.outer(s,s)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--repository',type=Path)
    ap.add_argument('--certificate',type=Path,required=True)
    ap.add_argument('--output',type=Path,required=True)
    args=ap.parse_args()
    root=args.repository or Path(__file__).resolve().parents[6]
    source=root/'papers/susy-positivity/investigations/critical-path/numerics/diagnose_cumulative_append.py'
    d=load(source);cert=json.loads(args.certificate.read_text())
    assert cert['certificate_pass']
    cert_source=Path(__file__).with_name('certify_first_prime_inputs.py')
    assert cert['source_sha256']==hashlib.sha256(cert_source.read_bytes()).hexdigest()
    L,h=.55,.2;runs=[]
    for n,order,inner in [(16,192,96),(32,256,128),(64,384,192),(96,512,256),(64,512,256)]:
        ql=d.central(L,n,order);qh=d.central(h,n,order)
        il=d.inverse_sqrt(ql);ih=d.inverse_sqrt(qh)
        ha,hp=mixed(d,L,h,n,order,inner)
        kappas={name:d.norm(ih@mat@il) for name,mat in [('arch',ha),('prime',hp),('complete',ha+hp)]}
        full=np.block([[ql,-(ha+hp).T],[-(ha+hp),qh]])
        row={'cosines_per_window':n,'delay_order':order,'cross_section_order':inner,
             'old_local_minimum_eigenvalue':float(np.linalg.eigvalsh(ql)[0]),
             'new_local_minimum_eigenvalue':float(np.linalg.eigvalsh(qh)[0]),
             'relative_coupling_quotients':kappas,
             'complete_form_compression_minimum_eigenvalue':float(np.linalg.eigvalsh(full)[0])}
        runs.append(row);print(json.dumps(row),flush=True)
    assert abs(runs[2]['relative_coupling_quotients']['complete']-runs[4]['relative_coupling_quotients']['complete'])<1e-8
    ha,hp=mixed(d,L,h,32,256,128)
    tower_runs=[]
    for M in (128,256,512,1024,2048):
        ql=tower(L,32,M);qh=tower(h,32,M)
        tower_runs.append({'M':M,'relative_coupling_quotient':d.norm(d.inverse_sqrt(qh)@(ha+hp)@d.inverse_sqrt(ql))})

    controls=[]
    def interval_control(name,value,record):
        lo,hi=float(Fraction(record['lower'])),float(Fraction(record['upper']))
        assert lo-1e-10 <= value <= hi+1e-10,(name,value,lo,hi)
        controls.append({'name':name,'floating_value':value,'within_rational_enclosure':True})
    wc=cert['checks']['M128_proxy_witness']
    rawf=np.array([float(Fraction(wc['old_raw_cosines'][str(j)])) for j in range(3)])
    rawg=np.array([float(Fraction(wc['new_raw_cosines'][str(j)])) for j in range(3)])
    rf=np.array([1/math.sqrt(L),math.sqrt(2/L),math.sqrt(2/L)])
    rg=np.array([1/math.sqrt(h),math.sqrt(2/h),math.sqrt(2/h)])
    f,g=rawf/rf,rawg/rg
    ha,hp=mixed(d,L,h,3,256,128)
    interval_control('arch mixed witness',float(g@ha@f),wc['arch_mixed_pairing'])
    interval_control('prime mixed witness',float(g@hp@f),wc['prime_mixed_pairing'])
    proxy=float(f@tower(L,3,128)@f+g@tower(h,3,128)@g-2*g@(ha+hp)@f)
    whole=float(f@d.central(L,3,256)@f+g@d.central(h,3,256)@g-2*g@(ha+hp)@f)
    interval_control('M128 proxy witness',proxy,wc['proxy_form'])
    interval_control('complete same witness',whole,wc['complete_form_same_witness'])
    ac=cert['checks']['arch_negative_witness'];length=.75
    raw=np.zeros(8)
    for j,b in ac['raw_cosines'].items():raw[int(j)]=float(Fraction(b))
    v=raw*math.sqrt(length/2);arch=float(v@d.central(length,8,256)@v)
    z,w=np.polynomial.legendre.leggauss(128);a=math.log(2);x=(length-a)*(z+1)/2
    fun=lambda t:sum(raw[j]*np.cos(j*math.pi*t/length) for j in range(8))
    prime=float(-math.sqrt(2)*a*np.sum((length-a)*w/2*fun(x+a)*fun(x)))
    interval_control('negative arch witness',arch,ac['complete_arch_form'])
    interval_control('prime repair',prime,ac['prime_correction'])
    interval_control('repaired complete witness',arch+prime,ac['complete_arithmetic_form'])
    controls.append({'name':'repeated n=64 quadrature agrees to 1e-8','check_pass':True})
    result={'date':'2026-09-24','model':'GPT-6 (Codex; developer-provided identity)',
        'reasoning_effort':'Not exposed; not inferred','status':'Floating finite-input diagnostics; NOT an all-input upper bound',
        'python':platform.python_version(),'numpy':np.__version__,'parameters':{'L':L,'h':h,'shift_for_continuation':.001},
        'central_full_form_runs':runs,'lower_tower_runs':tower_runs,'reduction_controls':controls,
        'check_pass':True,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'inherited_source_sha256':{str(source.relative_to(root)):hashlib.sha256(source.read_bytes()).hexdigest()},
        'certificate_sha256':hashlib.sha256(args.certificate.read_bytes()).hexdigest()}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')


if __name__=='__main__':
    if not __debug__:raise SystemExit('Do not disable diagnostic assertions with python -O.')
    main()
