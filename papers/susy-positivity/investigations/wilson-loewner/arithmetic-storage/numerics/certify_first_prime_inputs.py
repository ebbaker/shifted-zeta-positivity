#!/usr/bin/env python3
"""Rational certificates for first-prime local metrics and two obstructions.

Certifies local all-input floors, failure of the M=128 relative-energy proxy,
and a gamma/pole negative witness repaired by the exact prime on that witness.
Does NOT certify all-input first-prime positivity or cumulative coupling.
See FIRST_PRIME_CONTINUATION_ANALYSIS_20260924.md for the reductions and tails.
"""
import argparse
import hashlib
import importlib.util
import json
import math
import platform
from fractions import Fraction as F
from pathlib import Path


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--repository', type=Path)
    ap.add_argument('--digits', type=int, default=40)
    ap.add_argument('--output', type=Path, required=True)
    args = ap.parse_args()
    root = args.repository or Path(__file__).resolve().parents[6]
    inherited = root/'papers/susy-positivity/investigations/critical-path/numerics/certify_ema_original_anchor.py'
    spec = importlib.util.spec_from_file_location('anchor_intervals', inherited)
    a = importlib.util.module_from_spec(spec); spec.loader.exec_module(a)
    I = a.I; assert args.digits >= 40; I.scale = 10**args.digits
    pi = 16*a.atan_reciprocal(5)-4*a.atan_reciprocal(239)
    hn = I(sum((F(1,j) for j in range(1,1001)), F(0)))-a.log_interval(1000)
    gamma = I.raw((hn-F(1,2000)).lo, (hn-F(1,2002)).hi)
    w0 = -gamma-pi/2-3*a.log_interval(2)-a.log_interval(pi)
    wminus = F(-5372184,1000000); assert w0.lower() > wminus
    N, M, J = 32, 128, 1024
    fs, ms, ee = 10**20, 10**12, F(1,10**12)
    audit = {}

    def round_interval(v, scale, tolerance):
        mid = (v.lower()+v.upper())/2
        z = (mid.numerator*scale+mid.denominator//2)//mid.denominator
        assert max(abs(v.lower()-F(z,scale)),abs(v.upper()-F(z,scale))) <= tolerance
        return z

    def ldl(name, mat):
        piv = a.ldl_positive(mat)
        audit[name] = {'size':len(mat), 'minimum_pivot_lower':str(min(v.lower() for v in piv))}

    def fourth_tail(ell, start):
        return (2/I(ell))*(I(ell)/pi)**4/(3*(start-1)**3)

    def local(ell, name, head, high_floor, r2, eta, floor):
        rho = [(1/I(ell)).sqrt()]+[(2/I(ell)).sqrt()]*(J-1)
        k = [j*pi/ell for j in range(J)]
        ep = a.exp_interval(ell/4); sh=(ep-1/ep)/2; ch=(ep+1/ep)/2
        c=[sh*rho[j]/(F(1,4)+k[j]*k[j]) if j%2==0 else I(0) for j in range(J)]
        sn=[-ch*rho[j]/(F(1,4)+k[j]*k[j]) if j%2 else I(0) for j in range(J)]
        features=[[] for _ in range(J)]; diag=[I(wminus) for _ in range(N+1)]
        env=[I(0) for _ in range(N)]
        for n in range(M):
            rate=I(F(4*n+1,2)); ex=1/a.exp_interval(rate*ell)
            fac=[(2*rate*rate*(1-ex)).sqrt(),(2*rate*rate*(1+ex)).sqrt()]
            for j in range(J):
                v=fac[j%2]*rho[j]/(rate*rate+k[j]*k[j])
                assert v.abs().upper()<27
                features[j].append(round_interval(v,fs,F(1,fs)))
            for j in range(N+1):
                diag[j]+=2/rate*k[j]*k[j]/(rate*rate+k[j]*k[j])
            for j in range(N):
                env[j]+=2*rho[j]*rate*rate*(1+ex)/(rate*rate+k[j]*k[j])
        rank_error=M*(F(54,fs)+F(1,fs**2))
        mat=[]
        for i in range(N):
            row=[]
            for j in range(J):
                value=I(0)
                if (i-j)%2==0:
                    value=I(F(sum(x*y for x,y in zip(features[i],features[j])),fs**2))
                    value=I.raw((value-rank_error).lo,(value+rank_error).hi)
                    value+=2*c[i]*c[j]-2*sn[i]*sn[j]
                if i==j: value+=diag[i]
                row.append(round_interval(value,ms,ee))
            mat.append(row)
        A=[[I(F(mat[i][j],ms)-(N*ee if i==j else 0)) for j in range(N)] for i in range(N)]
        ldl(name+'_head',[[A[i][j]-(head if i==j else 0) for j in range(N)] for i in range(N)])
        high=diag[N]-2*ch*ch*fourth_tail(ell,N)
        assert high.lower()>high_floor
        for i in range(N): env[i]+=2*(c[i].abs()*sh+sn[i].abs()*ch)
        tail=fourth_tail(ell,J)*sum((v*v for v in env),I(0))
        B=[row[N:] for row in mat]
        gram=[[F(sum(x*y for x,y in zip(B[i],B[j])),ms**2) for j in range(N)] for i in range(N)]
        frob=I(sum((gram[i][i] for i in range(N)),F(0))).sqrt().upper()
        assert N*(J-N)<=256**2
        err=256*ee; guard=2*frob*err+err*err
        ldl(name+'_metric_cross',[[r2*A[i][j]-I(gram[i][j])-(tail+guard if i==j else 0)
                                  for j in range(N)] for i in range(N)])
        complement=high_floor-r2/eta
        assert (1-eta)*head>=floor and complement>=floor
        audit[name]={'length':str(ell),'head_floor':str(head),'raw_complement_floor':str(high_floor),
                     'relative_cross_squared_upper':str(r2),'eta':str(eta),
                     'paid_complement_floor':str(complement),'all_input_floor':str(floor),
                     'uncomputed_metric_columns_squared_upper':tail.record()}
        print(name+': all-input central metric certified',flush=True)

    local(F(11,20),'old',F(2,125),F(79,25),F(9,500),F(1,25),F(3,200))
    local(F(1,5),'new',F(9,20),F(359,100),F(1,1000),F(1,100),F(11,25))

    def trig(x):
        count=0
        while x.abs().upper()>F(1,2): x=x/2; count+=1
        sn=I(0); cs=I(0); st=x; ct=I(1)
        for j in range(24):
            sn+=st; cs+=ct
            st=-st*x*x/((2*j+2)*(2*j+3))
            ct=-ct*x*x/((2*j+1)*(2*j+2))
        se=I(F(1,2**48*math.factorial(48))); ce=I(F(1,2**47*math.factorial(47)))
        sn=I.raw((sn-se).lo,(sn+se).hi); cs=I.raw((cs-ce).lo,(cs+ce).hi)
        for _ in range(count): sn,cs=2*sn*cs,cs*cs-sn*sn
        return sn,cs

    def norm2(ell,coeff):
        return I(ell)*sum((b*b*(1 if j==0 else F(1,2)) for j,b in coeff.items()),F(0))

    def cosine_energy(ell,coeff,count):
        k2={j:(j*pi/ell)**2 for j in coeff}; norm=norm2(ell,coeff)
        val=w0*norm
        ex=1/a.exp_interval(ell/2); step=1/a.exp_interval(2*ell)
        for n in range(count):
            rate=F(4*n+1,2); den={j:rate*rate+k2[j] for j in coeff}
            val+=sum((2/rate*k2[j]/den[j]*ell*b*b*(1 if j==0 else F(1,2)) for j,b in coeff.items()),I(0))
            for parity in (0,1):
                v=sum((b/den[j] for j,b in coeff.items() if j%2==parity),I(0))
                val+=2*rate*rate*(1-(-1)**parity*ex)*v*v
            ex*=step
        ep=a.exp_interval(ell/4);sh=(ep-1/ep)/2;ch=(ep+1/ep)/2
        cv=sum((b/(F(1,4)+k2[j]) for j,b in coeff.items() if j%2==0),I(0))*sh
        sv=sum((b/(F(1,4)+k2[j]) for j,b in coeff.items() if j%2),I(0))*ch
        val+=2*cv*cv-2*sv*sv
        sup2=sum((abs(b) for b in coeff.values()),F(0))**2
        deriv=ell/2*sum((b*b*k2[j] for j,b in coeff.items()),I(0))
        rate=F(4*count+1,2)
        tail=2*sup2*(1/rate**2+1/(2*rate))+2*deriv*(1/rate**3+1/(4*rate**2))
        return val,tail

    def exponential_integral(ell,coeff,rate,ex):
        return sum((b*rate*(1-(-1)**j*ex)/(rate*rate+(j*pi/ell)**2) for j,b in coeff.items()),I(0))

    def mixed_arch(ell,h,fc,gc,count):
        ef=1/a.exp_interval(5*ell/2);eg=1/a.exp_interval(5*h/2)
        sf=1/a.exp_interval(2*ell);sg=1/a.exp_interval(2*h)
        ans=I(0)
        for n in range(1,count+1):
            rate=F(4*n+1,2)
            ans+=exponential_integral(ell,fc,rate,ef)*exponential_integral(h,gc,rate,eg)
            ef*=sf;eg*=sg
        ans-=exponential_integral(ell,fc,F(-1,2),a.exp_interval(ell/2))*exponential_integral(h,gc,F(-1,2),a.exp_interval(h/2))
        start=F(4*(count+1)+1,2)
        tail=sum((abs(b) for b in fc.values()),F(0))*sum((abs(b) for b in gc.values()),F(0))*(1/start**2+1/(2*start))
        return I.raw((ans-tail).lo,(ans+tail).hi)

    delay=a.log_interval(2);cp=delay/I(2).sqrt()

    def integrate_cos(freq,phase,left,right):
        if freq.lo==freq.hi==0: return (right-left)*trig(phase)[1]
        return (trig(freq*right+phase)[0]-trig(freq*left+phase)[0])/freq

    def prime_pair(ell,h,fc,gc):
        left=delay-ell; right=I(h); assert left.lower()>0 and right.lower()>left.upper()
        val=I(0)
        for i,b in gc.items():
            ki=i*pi/h
            for j,c in fc.items():
                kj=j*pi/ell
                # cos(ki*t) cos(kj*(a-t)); handle identical rational frequencies exactly.
                fm=I(0) if F(i,h)==F(j,ell) else ki-kj
                fp=ki+kj
                val+=b*c/2*(integrate_cos(fm,kj*delay,left,right)+integrate_cos(fp,-kj*delay,left,right))
        return cp*val

    fc={0:F(1061,1000),1:F(842,1000),2:F(-271,1000)}
    gc={0:F(809,1000),1:F(592,1000),2:F(14,1000)}
    ell,h=F(11,20),F(1,5)
    lf,_=cosine_energy(ell,fc,128);lg,_=cosine_energy(h,gc,128)
    ha=mixed_arch(ell,h,fc,gc,4096);hp=prime_pair(ell,h,fc,gc)
    proxy=lf+lg-2*(ha+hp)
    assert proxy.upper()<F(-33,10000)
    lf_full,tf=cosine_energy(ell,fc,4096);lg_full,tg=cosine_energy(h,gc,4096)
    full=lf_full+lg_full-2*(ha+hp)
    full=I.raw(full.lo,(full+tf+tg).hi)
    assert full.lower()>F(4,1000)
    audit['M128_proxy_witness']={'old_raw_cosines':{str(j):str(b) for j,b in fc.items()},
        'new_raw_cosines':{str(j):str(b) for j,b in gc.items()},'old_coordinate':'reflected r=L-y',
        'ordinary_norm_squared':norm2(ell,fc).__add__(norm2(h,gc)).record(),
        'arch_mixed_pairing':ha.record(),'prime_mixed_pairing':hp.record(),
        'proxy_form':proxy.record(),'complete_form_same_witness':full.record()}
    print('M128 proxy failure certified; same witness has positive complete form',flush=True)

    length=F(3,4);wc={1:F(1),3:F(-27,100),5:F(-1,10),7:F(-56,1000)}
    arch,tail=cosine_energy(length,wc,4096);arch=I.raw(arch.lo,(arch+tail).hi)
    # Correlation integral over 0<x<R-a: cos(ki*(x+a))*cos(kj*x).
    corr=I(0);width=length-delay
    for i,b in wc.items():
        for j,c in wc.items():
            ki=i*pi/length;kj=j*pi/length
            fm=I(0) if i==j else ki-kj
            corr+=b*c/2*(integrate_cos(fm,ki*delay,I(0),width)+integrate_cos(ki+kj,ki*delay,I(0),width))
    prime=-2*cp*corr;repaired=arch+prime
    assert arch.upper()<F(-6,10000) and repaired.lower()>F(1,1000)
    audit['arch_negative_witness']={'length':str(length),'raw_cosines':{str(j):str(b) for j,b in wc.items()},
        'ordinary_norm_squared':norm2(length,wc).record(),'complete_arch_form':arch.record(),
        'prime_correction':prime.record(),'complete_arithmetic_form':repaired.record(),
        'positive_omitted_gamma_upper':tail.record()}
    print('Gamma/pole negative witness and positive prime repair certified',flush=True)

    w=F(1,1000)
    for name,length,floor,defect_target in [('old',ell,F(3,200),F(2999,100000000)),('new',h,F(11,25),F(1759,2000000))]:
        cosh=(a.exp_interval(w*length)+1/a.exp_interval(w*length))/2
        perturb=w*w*cosh*(length*length/4+a.exp_interval(length/2)*length**3/3)
        rate=floor-perturb
        defect=1-1/a.exp_interval(2*w*rate)
        assert rate.lower()>0 and defect.lower()>defect_target
        audit[name]['uniform_shift_perturbation_upper']=perturb.record()
        audit[name]['cumulative_diagonal_defect_lower']=str(defect_target)
    R=ell+h;cw=(a.exp_interval(w*R)+1/a.exp_interval(w*R))/2
    mixed_perturb=w*w*R*R/2*cw*(pi/2+((a.exp_interval(ell)-1)*(a.exp_interval(h)-1)).sqrt())
    cwa=(a.exp_interval(w*delay)+1/a.exp_interval(w*delay))/2
    mixed_perturb+=cp*(cwa-1)
    audit['complete_mixed_shift_perturbation_upper']=mixed_perturb.record()
    result={'date':'2026-09-24','model':'GPT-6 (Codex; developer-provided identity)',
      'reasoning_effort':'Not exposed; not inferred','digits':args.digits,'python':platform.python_version(),
      'scope':'Local all-input metric floors and stated witness inequalities only; no all-input first-prime coupling certificate',
      'parameters':{'L':'11/20','h':'1/5','omega':'1/1000','metric_M':M,'metric_N':N,'metric_J':J,'witness_series_terms':4096},
      'checks':audit,'certificate_pass':True,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
      'inherited_source_sha256':{str(inherited.relative_to(root)):hashlib.sha256(inherited.read_bytes()).hexdigest()}}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'certificate_pass':True,'proxy_form':proxy.record()['decimal_display_only'],
      'same_witness_complete':full.record()['decimal_display_only'],'arch_witness':arch.record()['decimal_display_only'],
      'prime_repaired_witness':repaired.record()['decimal_display_only']},indent=2))


if __name__=='__main__':
    if not __debug__: raise SystemExit('Do not disable certificate assertions with python -O.')
    main()
