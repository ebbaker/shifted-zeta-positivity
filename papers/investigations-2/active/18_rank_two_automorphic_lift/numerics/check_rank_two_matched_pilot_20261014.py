#!/usr/bin/env python3
"""Bounded matched direction-18 pilot, 14 October 2026.
Prepared for Edward Baker with substantial LLM assistance.
Model gpt-6-astra (Codex), reasoning effort ultra.
Requires python-flint; all proof bounds use Arb at <=256 bits.
"""
import argparse,hashlib,json,os,platform,time
import flint
from pathlib import Path
from flint import arb,acb,ctx,fmpq
from fractions import Fraction
ctx.prec=256
PI=arb.pi(); T=arb(1)/20; TH=arb('1.3'); B=2*PI*TH.cos()
R=arb('1.5'); V=arb(6)
A0=4*PI**4+12*PI**3+9*PI**2
BASELINE_SHA256="e98a91f7c3abe8e8e9302ca3cf4c372329ec84d8668a5777eaf68bf86e0a0e47"
BASELINE_RELATIVE=Path("brainstorm/numerics/MATCHED_STATIONARY_BASELINE_RECORD_20261014.json")

def show(z): return z.str(40,more=True)
def gauss(k,q,half=False):
    if k not in (0,2,4): raise ValueError("Unsupported Gaussian moment")
    a=PI.sqrt()/q.sqrt()
    if k>=2:a/=2*q
    if k>=4:a*=3/(2*q)
    return a/2 if half else a

def packet(n,split=False):
    # After completing linear envelopes: e^(18r)<=e^(Ar r²/2+162/Ar),
    # cosh(v)<=e^|v|<=e^(Av v²/2+1/(2Av)).
    ar=(4 if split else 8)*B*n-2*T
    av=B*n/(4 if split else 2)-T/4
    if not (ar>0 and av>0): raise ValueError("Gaussian decay is not certified positive")
    c=(162/ar+1/(2*av)).exp()
    r2,r4=gauss(2,ar/2,True),gauss(4,ar/2,True)
    v0,v2=gauss(0,av/2),gauss(2,av/2)
    m0=r2*v0
    m1=r4*v0+r2*v2/8+r2*v0*((arb(n).log())**2/8+TH**2/16)
    return c,[m0,m1]

def mode_tail(N,X,j):
    n=N+1; logn=arb(n).log()
    c,m=packet(n)
    k=5+2*j
    ratio=(1+arb(1)/n)**k*(-B+T*logn/(2*n)).exp()
    if not ratio<1: raise ValueError("Omitted-mode geometric ratio is not certified below one")
    # d(n)<=n, A_n<=A0 n^4; for j1, log(n)^2 grows at most like n².
    return (-(arb(X)*TH)/2).exp()/2*A0*arb(n)**5*(-B*n+T*logn**2/4).exp()*c*m[j]/(1-ratio)

def divisor_count(n):return sum(n%d==0 for d in range(1,n+1))
def mode_bound(n,X,j,cut=None):
    c,m=packet(n,split=cut is not None)
    if cut=='r':decay=-B*n*((4*R).exp()+1)/2
    elif cut=='v':decay=-B*n*(V.cosh()+1)/2
    else:decay=-B*n
    a=4*PI**4*n**4+12*PI**3*n**3+9*PI**2*n**2
    return (-(arb(X)*TH)/2).exp()/2*divisor_count(n)*a*(decay+T*arb(n).log()**2/4).exp()*c*m[j]

def bounds(N,X,j):
    return {'mode_tail':mode_tail(N,X,j),
            'r_tail':sum((mode_bound(n,X,j,'r') for n in range(1,N+1)),arb(0)),
            'v_tail':sum((mode_bound(n,X,j,'v') for n in range(1,N+1)),arb(0)),
            'complete_absolute':sum((mode_bound(n,X,j) for n in range(1,N+1)),arb(0))+mode_tail(N,X,j)}

def cubature(N,X,j,limit,seconds):
    count={'mode_kernel':0,'spectral_divisor':0,'inner_callbacks':0,'outer_callbacks':0,'cache_hits':0}
    started=time.perf_counter();cache={};stop_reason=[None]
    ln=[[arb(a).log()-arb(n//a).log() for a in range(1,n+1) if n%a==0] for n in range(1,N+1)]
    X=arb(X)
    def check(extra=0):
        if stop_reason[0]:return False
        if count['mode_kernel']+count['spectral_divisor']+extra>limit:
            stop_reason[0]='primitive_evaluation_budget';return False
        if time.perf_counter()-started>seconds:
            stop_reason[0]='wall_time_budget';return False
        return True
    def spectral(v):
        key=v.repr()
        if key in cache:
            count['cache_hits']+=1;return cache[key]
        z=v+acb(0,TH); ch=z.cosh();sums=[]
        for ls in ln:
            h0=acb(0);h2=acb(0)
            for ell in ls:
                if not check(1):return None
                w=z-ell
                term=(T*w*w/8+acb(0,X)*w/2).exp()
                h0+=term
                if j:h2+=w*w/16*term
                count['spectral_divisor']+=1
            sums.append((h0,h2))
        if not check():return None
        value=(ch,sums)
        if len(cache)<20000:cache[key]=value
        return value
    def outer(r,analytic):
        count['outer_callbacks']+=1
        if not check():return acb('nan')
        zbase=PI*(4*r).exp()
        pref=r*r*(2*r+2*T*r*r).exp()/2
        def inner(v,analytic):
            count['inner_callbacks']+=1
            if not check():return acb('nan')
            data=spectral(v)
            if data is None:return acb('nan')
            ch,sums=data; total=acb(0)
            for n,(h0,h2) in enumerate(sums,1):
                if not check(1):return acb('nan')
                z=zbase*n
                poly=4*z**4-12*z**3*ch+9*z*z
                total+=poly*(-2*z*ch).exp()*((r*r*h0-h2) if j else h0)
                count['mode_kernel']+=1
            return pref*total
        # Entire integrands: no branch-cut decisions. Parameter balls r are
        # retained by all inner evaluations, enclosing the analytic integral.
        value=acb(0)
        for va,vb in [(-6,-3),(-3,0),(0,3),(3,6)]:
            value+=acb.integral(inner,va,vb,rel_tol=arb('1e-14'),abs_tol=arb('1e-78'),
                                eval_limit=12000,deg_limit=96,depth_limit=20)
            if stop_reason[0]:return acb('nan')
        return value
    result=acb(0);stop='completed'
    for ra,rb in [('0','.25'),('.25','.5'),('.5','.75'),('.75','1'),('1','1.5')]:
        result+=acb.integral(outer,arb(ra),arb(rb),rel_tol=arb('1e-12'),abs_tol=arb('1e-76'),
                            eval_limit=12000,deg_limit=96,depth_limit=12)
        if stop_reason[0]:
            stop=stop_reason[0];result=None;break
        if not result.is_finite():stop='nonfinite_validated_cubature';break
    return result,dict(count,elapsed_seconds=time.perf_counter()-started,stop=stop,cache_entries=len(cache))


def main():
    p=argparse.ArgumentParser();p.add_argument('--record',type=Path);p.add_argument('--tail-only',action='store_true')
    p.add_argument('--cell',choices=['j0','j1','both'],default='both');p.add_argument('--mode-cutoff',type=int,default=32)
    p.add_argument('--baseline',type=Path)
    p.add_argument('--primitive-limit',type=int,default=1000000);p.add_argument('--seconds',type=float,default=60)
    args=p.parse_args();rows=[]
    if args.mode_cutoff<2:
        p.error('--mode-cutoff must be at least 2 for the proved decreasing log(n)/n envelope')
    if not 0<args.primitive_limit<=1000000 or not 0<args.seconds<=60:
        p.error('The matched pilot permits at most 1000000 primitives and 60 seconds per cell')
    if args.baseline is None:
        normal=(Path(__file__).resolve().parent/'../../..'/BASELINE_RELATIVE).resolve()
        args.baseline=normal
        archive=os.environ.get('MATCHED_STATIONARY_ARCHIVES')
        if not normal.exists() and archive:
            args.baseline=Path(archive)/BASELINE_RELATIVE
    if not args.baseline.is_file():
        p.error('Missing matched baseline. Regenerate with brainstorm/numerics/check_matched_stationary_baseline.py and use --baseline PATH; supply the hash-bound committed record for this matched pilot.')
    baseline_bytes=args.baseline.read_bytes()
    baseline_sha=hashlib.sha256(baseline_bytes).hexdigest()
    if baseline_sha!=BASELINE_SHA256:
        p.error('Matched baseline SHA-256 mismatch; refusing unbound stationary brackets')
    baseline=json.loads(baseline_bytes)
    for j,x,cell in [(0,'204.088',['204.087','204.089']),(1,'205.557',['205.556','205.558'])]:
        if args.cell not in ['both','j'+str(j)]:continue
        b=bounds(args.mode_cutoff,cell[0],j)
        print('BOUNDS',j,{k:show(v) for k,v in b.items()},flush=True)
        row={'j':j,'x_cell':cell,'center':x,'bounds_uniform_on_cell':{k:show(v) for k,v in b.items()}}
        if not args.tail_only:
            target=arb(x)
            if baseline:
                br=baseline['cells'][j]['stationary_root_bracket']
                lo,hi=map(Fraction,br);md=(lo+hi)/2;rd=(hi-lo)/2
                target=arb(arb(fmpq(md.numerator,md.denominator)),arb(fmpq(rd.numerator,rd.denominator)))
                row['stationary_root_bracket_from_baseline']=br
            result,cost=cubature(args.mode_cutoff,target,j,args.primitive_limit,args.seconds)
            row['cubature']=cost
            if result is not None and result.is_finite():
                row['retained_integral_on_target']={'real':show(result.real),'imaginary':show(result.imag)}
                tail=b['mode_tail']+b['r_tail']+b['v_tail']
                value=result.real+arb(0,tail.upper())
                row['complete_integral_on_target']=show(value)
                row['positive_on_target']=bool(value>0)
                row['numerical_radius_goal_met']=bool(result.real.rad()<arb('5e-73'))
            else:
                row['complete_integral_uniform_fallback']=show(arb(0,b['complete_absolute'].upper()))
                row['positive_on_target']=False;row['numerical_radius_goal_met']=False
            print('RESULT',j,row.get('cubature'),flush=True)
        rows.append(row)
    record={'date':'2026-10-14','prepared_for':'Edward Baker','model':'gpt-6-astra','reasoning_effort':'ultra',
            'acknowledgment':'Substantial LLM assistance; internal arithmetic review, not independent validation.',
            'status':'TAIL_BOUNDS_ONLY' if args.tail_only else 'BOUNDED_COMPARISON',
            'arithmetic':{'library':'python-flint','precision_bits':ctx.prec,'python':platform.python_version(),'python_flint':flint.__version__},
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'parameters':{'t':'1/20','theta':'1.3','r_radius':'1.5','v_radius':'6','mode_cutoff':args.mode_cutoff,
                          'primitive_limit_per_cell':args.primitive_limit,'wall_seconds_per_cell':args.seconds,
                          'primitive_definition':'one mode polynomial/exponential evaluation, or one divisor phase/heat evaluation'},
            'baseline_sha256':baseline_sha,'rows':rows,'limitations':['No root existence or stationary constraint is inferred from midpoint quadrature.',
             'If cubature exhausts the budget, only the displayed analytic complete absolute envelope is certified.',
             'No favorable sample or finite cutoff establishes a global sign or an RH implication.']}
    if args.record:args.record.write_text(json.dumps(record,indent=2)+'\n')
if __name__=='__main__':main()
