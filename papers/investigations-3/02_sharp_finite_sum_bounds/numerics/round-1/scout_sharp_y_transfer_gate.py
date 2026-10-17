#!/usr/bin/env python3
"""Bounded floating gate scout, not a certificate.
Prepared for Edward Baker with substantial LLM assistance, 17 October 2026.
Model gpt-6.1-sol (Codex), reasoning effort ultra.
"""
#!/usr/bin/env python3
import argparse, math, time, json, pathlib, hashlib
OUT=pathlib.Path(__file__).resolve().parent
ap=argparse.ArgumentParser(description=__doc__)
ap.add_argument("--output",type=pathlib.Path,required=True)
args=ap.parse_args()
START=time.monotonic(); LIMIT=120; CAP=200000
T=.157; y0=math.sqrt(.0350708); y1=math.sqrt(.686)
CASES=[(690988,[2,3,5,7,11]),(728999,[2,3,5,7,11]),(729000,[2,3,5,7]),(818999,[2,3,5,7]),(819000,[2,3,5]),(1027999,[2,3,5]),(1028000,[2,3]),(3840000,[2,3])]
YS=[y0+(y1-y0)*j/24 for j in range(25)]
count=0; worst=[]; allworst=[]; violations=0; near_ties=0; pattern_count=0; term_count=0; complete=True; why=None; case_counts=[]
def bound():
    if time.monotonic()-START>LIMIT: raise RuntimeError('wall cap')
    if count>=CAP: raise RuntimeError('term-y cap')
def subsets(ps):
    out=[(1,1,0.)]
    for p in ps:
        lp=math.log(p)
        out += [(d*p,-sgn,sq+lp*lp) for d,sgn,sq in out[:]]
    return sorted(out)
def selected(N,ps):
    global pattern_count
    D=math.prod(ps); ds=subsets(ps); answer=set()
    for G,_,_ in ds:
        div=[a for a in ds if G%a[0]==0]
        previous=0
        for d,_,_ in div:
            low=max(2,previous*N+1); high=d*N; previous=d
            kmin=(low+G-1)//G; kmax=high//G
            if kmin>kmax: continue
            active=[a for a in div if a[0]>=d]
            pattern_count+=1
            def snap(k):
                for h in range(50):
                    for v in ([k] if h==0 else [k-h,k+h]):
                        if kmin<=v<=kmax and math.gcd(v,D//G)==1:
                            answer.add(G*v); return
            lo=math.log(max(low,G*kmin)); hi=math.log(high)
            for j in range(5): snap(round(math.exp(lo+(hi-lo)*j/4)/G))
            snap(kmin); snap(kmax)
            def c0(L):
                return math.fsum(sgn*math.exp(T/4*(sq+math.log(d0)**2-2*L*math.log(d0))) for d0,sgn,sq in active)
            grid=[lo+(hi-lo)*j/32 for j in range(33)]
            for a,b in zip(grid,grid[1:]):
                fa=c0(a); fb=c0(b)
                if fa*fb<0:
                    for _ in range(60):
                        m=(a+b)/2; fm=c0(m)
                        if fa*fm<=0:b=m;fb=fm
                        else:a=m;fa=fm
                    root=round(math.exp((a+b)/2)/G)
                    for offset in [-2,-1,0,1,2]: snap(root+offset)
    return sorted(answer)
try:
 for N,ps in CASES:
    case_start=count; D=math.prod(ps); divs=subsets(ps); ns=selected(N,ps)
    q=N*N-T/16; x=4*math.pi*q; ell=.02-.5*math.log(q)
    for n in ns:
        L=math.log(n); G=math.gcd(n,D)
        active=[(d,sgn,sq) for d,sgn,sq in divs if n%d==0 and n//d<=N]
        terms=[(sgn*math.exp(T/4*(sq+math.log(d)**2-2*L*math.log(d))),math.log(d)) for d,sgn,sq in active]
        C0=math.fsum(r for r,ld in terms); bt=math.exp(T/4*L*L)
        for y in YS:
            bound(); count+=1
            Cy=math.fsum(r*math.exp(-y*ld) for r,ld in terms)
            Cyprime=math.fsum(-ld*r*math.exp(-y*ld) for r,ld in terms)
            gg=math.exp(ell*y); gp=ell*gg; gy=gg*math.exp(y*L)
            Aover=math.exp(y*L)*Cy; zprod=gy*Cy
            vp=gy*((L+ell)*Cy+Cyprime)
            us={e:abs(C0+e*zprod)/(1+e*gg) for e in [-1,1]}
            umax=max(us.values()); tie_tol=1e-13*max(umax,1e-300)
            sigma=(1+y)/2+T/4*math.log(q)-T/(2*x*x)*max(1-3*y+4*y*(1+y)/(x*x),0)
            F=1-3*y+4*y*(1+y)/(x*x)
            sigma_prime=.5-T/(2*x*x)*(-3+4*(1+2*y)/(x*x)) if F>=0 else .5
            for e in [-1,1]:
                if us[e]<umax-tie_tol: continue
                if abs(us[1]-us[-1])<=tie_tol:near_ties+=1
                z=C0+e*zprod; den=1+e*gg
                Dzw=math.copysign(1,z)*e*vp if z else abs(e*vp)
                gate=Dzw-(L/2+e*gp/den)*abs(z)
                actual_gate=Dzw-(sigma_prime*L+e*gp/den)*abs(z)
                scaled=bt*math.exp(-sigma*L)/den
                row=dict(N=N,n=n,G=G,P=ps,y=y,e=e,z_normalized=z,B=bt*C0,A=bt*Aover,A_prime=bt*math.exp(y*L)*(L*Cy+Cyprime),C0=C0,Cy=Cy,g=gg,ell=ell,active_divisors=[a[0] for a in active],gate_normalized=gate,actual_gate_normalized=actual_gate,derivative_actual=actual_gate*scaled,derivative_bound=gate*scaled,sigma=sigma,sigma_prime=sigma_prime,u_minus=us[-1],u_plus=us[1])
                allworst.append(row); allworst.sort(key=lambda r:r['gate_normalized'],reverse=True);del allworst[20:]
                if gate>0:
                    violations+=1;worst.append(row);worst.sort(key=lambda r:r['derivative_actual'],reverse=True);del worst[20:]
        term_count+=1
    case_counts.append(dict(N=N,terms=len(ns),term_y_count=count-case_start))
except RuntimeError as err:
 complete=False;why=str(err)
record=dict(date='2026-10-17',prepared_for='Edward Baker',model='gpt-6.1-sol',reasoning_effort='ultra',status='FLOAT_DIAGNOSTIC_ONLY',complete=complete,stop_reason=why,t=T,y0=y0,y1=y1,term_y_count=count,term_count=term_count,pattern_count=pattern_count,violation_branch_count=violations,near_tie_branch_count=near_ties,elapsed_seconds=time.monotonic()-START,case_counts=case_counts,worst_derivative_violations=worst,worst_normalized_gates=allworst,source_sha256=hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),plan_sha256=hashlib.sha256((OUT/'FLOAT_PLAN.md').read_bytes()).hexdigest())
args.output.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({k:v for k,v in record.items() if k not in ['worst_derivative_violations','worst_normalized_gates']},indent=2))
print('WORST_ACTUAL_DERIVATIVES',json.dumps(worst[:3],indent=2))
print('WORST_NORMALIZED_GATES',json.dumps(allworst[:3],indent=2))
