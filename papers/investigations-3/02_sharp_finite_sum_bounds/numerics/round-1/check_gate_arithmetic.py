#!/usr/bin/env python3
"""Same-model arithmetic spot checks of the bounded sharp transfer engine.
Prepared for Edward Baker with substantial LLM assistance, 17 October 2026.
Recorded model gpt-6.1-sol (Codex), reasoning effort ultra.
This is a sample/implementation check, not an independent formal review.
"""
import argparse,importlib.util,sys,math,json,time,hashlib,traceback
from decimal import Decimal as D, Context, ROUND_HALF_EVEN, localcontext
from pathlib import Path
HC=Context(prec=110,rounding=ROUND_HALF_EVEN)
logs={}
def log(n):
    if n not in logs:logs[n]=HC.ln(D(n))
    return logs[n]
def direct(leg,p,N,n,y):
    with localcontext(HC):
        L=log(n);ell=D('.02')-HC.ln(D(N*N)-D('.157')/16)/2
        g=HC.exp(y*ell);c=D(0);Q=D(0);Tv=D(0)
        for d,s,ld,alpha in p.active:
            a=log(d)
            sum2=sum((log(prime)**2 for prime in leg.P if d%prime==0),D(0))
            r=HC.exp(D('.157')/4*(sum2+a*a-2*L*a))
            term=HC.exp(y*(L-a+ell))*r
            c+=s*r;Q+=s*term;Tv+=s*term*(L-a+ell)
        def dint(z,w):return w if z>0 else -w if z<0 else abs(w)
        ub={e:abs(c+e*Q)/(1+e*g) for e in (-1,1)};um=max(ub.values())
        active=[e for e in (-1,1) if ub[e]==um]
        gates={e:(1+e*g)*dint(c+e*Q,e*Tv)-(L/2*(1+e*g)+e*ell*g)*abs(c+e*Q) for e in (-1,1)}
        R=c-g*Q;S=Q-g*c;Rp=-g*(ell*Q+Tv);Sp=Tv-ell*g*c
        alt=dint(R,Rp)+dint(S,Sp)-(L/2-2*g*g*ell/(1-g*g))*(abs(R)+abs(S))
        return gates,active,alt,(g*c-Q)*(c-g*Q),c,Q
EXPECTED_ENGINE_SHA256='aa6c73e0aa6672b5e6706f704b0a8dda42f1a572d9cd2a3766c91a61bebf6792'

def run_checks(m,src):
    results={};defects=[];count=0
    started=time.monotonic()
    for idx in range(4):
        leg=m.Leg(idx)
        for p in leg.patterns:
            for mode in range(3):
                N=(leg.nlo,leg.nhi,(leg.nlo+leg.nhi)//2)[mode]
                lower=2 if p.previous==0 else p.previous*N+1
                upper=p.top*N
                candidates=[max(lower,p.nmin),upper,(lower+upper)//2]
                raw=candidates[mode]
                k=max(1,(raw+p.G-1)//p.G)
                while math.gcd(k,leg.D//p.G)!=1:k+=1
                n=p.G*k
                if n>upper:
                    k=upper//p.G
                    while math.gcd(k,leg.D//p.G)!=1:k-=1
                    n=p.G*k
                assert lower<=n<=upper and n>=p.nmin and math.gcd(n,leg.D)==p.G
                y=(D('.1873'),D('.51'),D('.828'))[mode]
                H=m.ln(m.I(N));V=m.ln(m.I(n)/N);Y=m.I(y)
                kind,detail=m.evaluate(leg,p,H,V,Y)
                gates,active,alt,activity,c,Q=direct(leg,p,N,n,y)
                count+=1;results[kind]=results.get(kind,0)+1
                if kind=='empty':defects.append(('false_empty',idx,p.label(),N,n))
                if kind in ('singleton','prime_zero') and max(gates[e] for e in active)>D('1e-85'):
                    defects.append(('false_shortcut',idx,p.label(),N,n,str(max(gates[e] for e in active))))
                if kind in ('active','unresolved'):
                    for e in active:
                        if e not in detail['branches']:defects.append(('missed_branch',idx,N,n,e))
                    for e,bnd in detail['bounds'].items():
                        if not D(bnd[0])<=gates[int(e)]<=D(bnd[1]):
                            defects.append(('bad_enclosure',idx,N,n,e,bnd,str(gates[int(e)])))
                if kind=='absolute_sum' and not D(detail['bound'][0])<=alt<=D(detail['bound'][1]):
                    defects.append(('bad_alt_enclosure',idx,N,n,detail,str(alt)))
                if kind=='unresolved' and not D(detail['absolute_sum'][0])<=alt<=D(detail['absolute_sum'][1]):
                    defects.append(('bad_unresolved_alt',idx,N,n,detail,str(alt)))
                if kind not in ('empty','unresolved') and max(gates[e] for e in active)>D('1e-85'):
                    defects.append(('false_pass',idx,N,n,kind,str(max(gates[e] for e in active))))
    rec={'code_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'samples':count,'precision':110,'kinds':results,'defects':defects,'seconds':time.monotonic()-started}

    # Deliberately adverse exact control with both branches tied.
    a=m.ln(m.I(2));c=m.I(1);Q=m.I('.5');Tv=-3*a;g=m.I('.5');ell=-2*a;L=4*a
    activity=(g*c-Q)*(c-g*Q)
    branches=(-1,) if activity.lo>0 else ((1,) if activity.hi<0 else (-1,1))
    bounds={}
    for e in branches:
        z=c+e*Q;d=1+e*g
        bounds[e]=d*m.dint(z,e*Tv)-((L/2)*d+e*ell*g)*z.abs()
    R=c-g*Q;S=Q-g*c;Rp=-g*(ell*Q+Tv);Sp=Tv-ell*g*c
    alt=m.dint(R,Rp)+m.dint(S,Sp)-(L/2-2*g*g*ell/(1-g*g))*(R.abs()+S.abs())
    assert branches==(-1,1) and bounds[-1].lo>0 and bounds[1].hi<0 and alt.hi>0
    with localcontext(HC):
        ln2=HC.ln(D(2))
        assert bounds[-1].lo<=ln2/2<=bounds[-1].hi
        assert bounds[1].lo<=-D('7.5')*ln2<=bounds[1].hi
        assert alt.lo<=D('1.5')*ln2<=alt.hi
    rec['adverse_tied_control']={'activity':activity.data(),'branches':list(branches),'bounds':{str(k):v.data() for k,v in bounds.items()},'absolute_sum':alt.data(),'correctly_rejected':True}

    # A zero numerator can be inactive.  Its adverse right derivative is then irrelevant;
    # test both branch selection and the interval upper-right derivative helper.
    c=m.I(1);Q=m.I(1);Tv=m.I(10);g=m.I('.5');ell=m.I(-2);L=m.I(4)
    activity=(g*c-Q)*(c-g*Q)
    branches=(-1,) if activity.lo>0 else ((1,) if activity.hi<0 else (-1,1))
    assert branches==(1,)
    zero_derivative=m.dint(c-Q,-Tv)
    assert zero_derivative.lo<=10<=zero_derivative.hi
    for z in (m.I('-1e-45','1e-45'),m.I(0)):
        for w in (m.I(-7),m.I(3),m.I(-7,3)):
            v=m.dint(z,w)
            assert v.lo<=max(abs(w.lo),abs(w.hi))<=v.hi
    rec['synthetic_kinks']={'inactive_zero_keeps_only_plus_branch':True,'zero_right_derivative_enclosed':True}

    # Exhaustively exercise trimming itself, including narrow point boxes and a
    # sequence of bisected root boxes enclosing every feasible small integer pair.
    trim_points=0;trim_cells=0
    for idx in (3,2):
        leg=m.Leg(idx);leg.nlo=7;leg.nhi=9;leg.h=m.I(m.ln(m.I(7)).lo,m.ln(m.I(9)).hi)
        for N in range(7,10):
            for n in range(2,leg.D*N+1):
                G=math.gcd(n,leg.D)
                if n>G*N:continue
                p=next(p for p in leg.patterns if p.G==G and (not p.previous or p.previous*N<n) and n<=p.top*N)
                H=m.ln(m.I(N));V=m.ln(m.I(n)/N)
                tr=m.trim(leg,p,H,V)
                assert tr is not None
                Li,cand=tr
                with localcontext(HC):
                    assert Li.lo<=log(n)<=Li.hi and (cand is None or n in cand)
                trim_points+=1
                cell=leg.root(p)
                with localcontext(HC):hh=log(N);vv=log(n)-log(N);yy=D('.5')
                for depth in range(13):
                    H,V,Y,_=cell
                    tr=m.trim(leg,p,H,V)
                    assert tr is not None,('false pruned cell',idx,N,n,depth)
                    Li,cand=tr
                    with localcontext(HC):assert Li.lo<=log(n)<=Li.hi and (cand is None or n in cand)
                    trim_cells+=1
                    kids=m.split(*cell)
                    if kids is None:break
                    eligible=[kid for kid in kids if kid[0].lo<=hh<=kid[0].hi and kid[1].lo<=vv<=kid[1].hi and kid[2].lo<=yy<=kid[2].hi]
                    assert eligible
                    cell=eligible[0]
    rec['integer_trimming']={'feasible_integer_points':trim_points,'containing_bisected_cells':trim_cells,'false_prunes':0}
    rec['seconds']=time.monotonic()-started
    rec['tested_code_unchanged']=rec['code_sha256']==hashlib.sha256(src.read_bytes()).hexdigest()
    return rec

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--engine',type=Path,default=Path(__file__).with_name('check_sharp_y_transfer_gate.py'))
    ap.add_argument('--output',type=Path,required=True)
    args=ap.parse_args()
    rec=dict(date='2026-10-17',prepared_for='Edward Baker',model='gpt-6.1-sol',reasoning_effort='ultra',
        scope='Same-model arithmetic sample check; not an independent formal review or a uniform certificate',
        checker_source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        expected_engine_sha256=EXPECTED_ENGINE_SHA256,passed=False)
    try:
        if not __debug__:
            raise RuntimeError('Assertions must remain enabled for this arithmetic checker')
        engine_hash=hashlib.sha256(args.engine.read_bytes()).hexdigest()
        rec['engine_sha256']=engine_hash
        if engine_hash!=EXPECTED_ENGINE_SHA256:
            raise ValueError('Engine SHA-256 does not match the pinned tested source')
        spec=importlib.util.spec_from_file_location('gate',args.engine)
        m=importlib.util.module_from_spec(spec)
        sys.modules['gate']=m
        spec.loader.exec_module(m)
        rec.update(run_checks(m,args.engine))
        rec['passed']=not rec['defects'] and rec['tested_code_unchanged']
        if not rec['passed']:
            rec['error']='Arithmetic defects or source change detected'
    except Exception as exc:
        rec['passed']=False
        rec['error']=dict(type=type(exc).__name__,message=str(exc),
            location=traceback.extract_tb(exc.__traceback__)[-1].lineno)
    args.output.write_text(json.dumps(rec,indent=2)+'\n')
    print(json.dumps(dict(output=str(args.output),passed=rec['passed'],samples=rec.get('samples'),
        error=rec.get('error'))))
    return 0 if rec['passed'] else 1

if __name__=='__main__':
    sys.exit(main())
