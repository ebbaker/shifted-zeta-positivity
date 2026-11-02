#!/usr/bin/env python3
"""J-E02 r1 compact certificate, 1 November 2026.

Prepared for Edward Baker with substantial LLM assistance.
Recorded model gpt-6.1-sol (Codex), effort ultra.
Requires python-flint 0.9.0 (Arb/FLINT). All sign decisions use ball arithmetic.
24 terms, degree 63, P70, 128/256 bits, prescribed leaf/depth/time caps.
"""
import argparse
from collections import deque
from fractions import Fraction
from hashlib import sha256
import json
from math import comb, factorial
from pathlib import Path
import time
import flint
from flint import arb, arb_series, ctx

DEGREE, TERMS, RHO = 63, 24, Fraction(1, 8)
START = None
PRIOR = 0.0
LIVE = {}


def clock_check():
    if START is not None and PRIOR+time.monotonic()-START >= 1800:
        raise TimeoutError('30-minute arithmetic cap')


def ball(q):
    if isinstance(q, Fraction):
        return arb(q.numerator)/q.denominator
    return arb(q)


def two(e):
    return arb((1, e))


def dyad(a):
    m, e = a.man_exp()
    return [str(m), int(e)]


def enclosure(a):
    return dict(mid=dyad(a.mid()), radius=dyad(a.rad()),
                lower=dyad(a.lower()), upper=dyad(a.upper()), display=a.str(18))


def det(a,b,c,d,e,f,g,h,i):
    return a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)


def numerators(q):
    a=q[0]*q[3]-q[1]*q[2]
    b=q[0]*q[4]-q[2]*q[2]
    w=det(q[0],q[1],q[2],q[2],q[3],q[4],q[4],q[5],q[6])
    w1=det(q[0],q[1],q[3],q[2],q[3],q[5],q[4],q[5],q[7])
    return a,q[0]*a*w1-3*(q[0]*b-q[1]*a)*w


def make_P():
    p=[[0,-3,2]]
    for j in range(70):
        old=p[-1];new=[0]*(len(old)+1)
        for k,c in enumerate(old):
            new[k]+=(1+4*k)*c
            new[k+1]-=4*c
        p.append(new)
    return p


def horner(p,x):
    s=arb(0)
    for a in reversed(p):
        s=s*x+a
    return s


def bernstein_bound(coefficients,left,right):
    """Exact power-to-Bernstein formula, all operations rounded out by Arb."""
    n=len(coefficients)-1
    l,w=ball(left),ball(right-left)
    lp=[arb(1)];wp=[arb(1)]
    for j in range(n):
        lp.append(lp[-1]*l);wp.append(wp[-1]*w)
    shifted=[]
    for j in range(n+1):
        shifted.append(wp[j]*sum((coefficients[i]*comb(i,j)*lp[i-j]
                                  for i in range(j,n+1)),arb(0)))
    beta=[sum((shifted[j]*comb(k,j)/comb(n,j) for j in range(k+1)),arb(0))
          for k in range(n+1)]
    return min(b.lower() for b in beta)


def origin_coefficients(P,bits):
    ctx.prec=bits;ctx.cap=64
    pi=arb.pi();xs=[pi*n*n for n in range(1,25)]
    exps=[(-x).exp() for x in xs]
    source=[]
    for j in range(71):
        clock_check()
        a=sum((horner(P[j],x)*e for x,e in zip(xs,exps)),arb(0))/factorial(j)
        a+=arb(0,(1,-146+2*j))
        if j%2:
            assert a.contains(0), ('odd full-source coefficient enclosure',j)
            a=arb(0)
        source.append(a)
    jets=[]
    for j in range(8):
        jets.append(arb_series([source[j+k]*factorial(j+k)/factorial(k)
                                for k in range(64)],64))
    A,N=numerators(jets)
    for j in range(64):
        if j%2==0 or j<1:
            assert A[j].contains(0),('A parity',j)
        if j%2==0 or j<5:
            assert N[j].contains(0),('N exact cancellation',j)
    U=[A[2*k+1] for k in range(32)]
    V=[N[2*k+5] for k in range(30)]
    # Independent endpoint formulas use the same 24 retained exponentials.
    theta=1+2*sum(exps,arb(0))+arb(0,(1,-146))
    z=pi*pi*theta**8/4;p0=z-arb(3)/2
    previous=json.loads((ARGS.repo/ROUTE/'numerics/J_E01_R2_EXACT_RECORD_20261101.json').read_text())
    AP=[630,-4620,1062,-104,200]
    Mp=[int(Fraction(c)) for c in previous['origin']['M']]
    rp=horner(AP,z)/(2*p0*p0)
    J=arb(768)*horner(Mp,z)/(5*p0**6)
    expectedU=2*source[0]**2*rp
    expectedV=32*source[0]**6*J
    assert U[0].overlaps(expectedU) and V[0].overlaps(expectedV)
    assert U[0]>0 and V[0]>0 and z>arb(47)/10
    acquisition=dict(precision=bits, source_coefficients=[enclosure(a) for a in source],
                     U_coefficients=[enclosure(a) for a in U],
                     V_coefficients=[enclosure(a) for a in V],
                     endpoint_U=enclosure(U[0]),endpoint_V=enclosure(V[0]),
                     inherited_U=enclosure(expectedU),inherited_V=enclosure(expectedV),
                     endpoint_formulas_overlap=True)
    return U,V,acquisition


def origin_run(P):
    attempts=[]
    LIVE['origin_progress']=dict(attempts=attempts)
    for bits in (128,256):
        U,V,acq=origin_coefficients(P,bits)
        queue=deque([(Fraction(0),Fraction(1,4096),0)]);accepted=[];failed=[]
        while queue:
            clock_check();left,right,depth=queue.popleft()
            lbU=bernstein_bound(U,left,right)-two(-150)
            lbV=bernstein_bound(V,left,right)-two(-16)
            row=dict(left=str(left),right=str(right),depth=depth,precision=bits,
                     U_lower=enclosure(lbU),V_lower=enclosure(lbV))
            if lbU>0 and lbV>0:
                row['status']='certified';accepted.append(row)
            elif bits==128:
                row['status']='unresolved_at_128';failed.append(row)
            elif depth<6 and len(accepted)+len(queue)+len(failed)+2<=64:
                mid=(left+right)/2
                queue.append((left,mid,depth+1));queue.append((mid,right,depth+1))
            else:
                row['status']='unresolved';failed.append(row)
        attempts.append(dict(acquisition=acq,cells=accepted+failed))
        if not failed:
            return dict(status='certified',attempts=attempts,cells=accepted)
    return dict(status='unresolved',attempts=attempts,cells=accepted+failed)


def normalized_series(center,P,bits):
    ctx.prec=bits;ctx.cap=64
    tc=arb.pi()*(4*ball(center)).exp()
    ts=tc*arb_series([0,4],64).exp()
    inverse_powers=[arb_series([1],64)]
    for k in range(1,10):
        inverse_powers.append(arb_series([0,-4*k],64).exp()/tc**k)
    nu=[arb_series([],64) for _ in range(8)]
    for n in range(1,25):
        clock_check()
        amplitude=arb_series([1],64) if n==1 else (-(n*n-1)*ts).exp()
        n2=n*n
        for j in range(8):
            inner=arb_series([],64)
            for ell,c in enumerate(P[j]):
                if c:
                    inner+=inverse_powers[j+2-ell]*(c*n2**ell)
            nu[j]+=amplitude*inner/(64**j)
    return numerators(nu)


def middle_cell(left,right,depth,P,bits):
    A,N=normalized_series((left+right)/2,P,bits)
    h=(right-left)/2;r=ball(h/RHO)
    errorA=two(53)*r**64/(1-r)+two(-502)
    errorN=two(163)*r**64/(1-r)+two(-391)
    lbA=bernstein_bound([A[k] for k in range(64)],-h,h)-errorA
    lbN=bernstein_bound([N[k] for k in range(64)],-h,h)-errorN
    row=dict(left=str(left),right=str(right),depth=depth,precision=bits,
             A_lower=enclosure(lbA),N_lower=enclosure(lbN),
             A_error=enclosure(errorA),N_error=enclosure(errorN))
    if lbA>0 and lbN>0:
        row['status']='certified'
    elif A[0]+two(-502)<0 or N[0]+two(-391)<0:
        row.update(status='certified_negative_center',center=str((left+right)/2),
                   A_center=enclosure(A[0]+arb(0,(1,-502))),
                   N_center=enclosure(N[0]+arb(0,(1,-391))))
    else:
        row['status']='unresolved'
    return row


def middle_run(P):
    queue=deque([(Fraction(m,128),Fraction(m+1,128),0,128) for m in range(2,128)])
    accepted=[];failed=[];attempts=[];negative=[]
    LIVE['middle_progress']=dict(accepted=accepted,failed=failed,attempts=attempts,negative=negative)
    while queue:
        LIVE['middle_progress']['pending']=[dict(left=str(a),right=str(b),depth=d,precision=p)
                                            for a,b,d,p in queue]
        clock_check();left,right,depth,bits=queue.popleft()
        row=middle_cell(left,right,depth,P,bits);attempts.append(row)
        if row['status']=='certified':
            accepted.append(row)
        elif row['status']=='certified_negative_center':
            negative.append(row);break
        elif bits==128:
            queue.appendleft((left,right,depth,256))
        elif depth<8 and len(accepted)+len(failed)+len(queue)+2<=4096:
            mid=(left+right)/2
            queue.appendleft((mid,right,depth+1,256));queue.appendleft((left,mid,depth+1,256))
        else:
            failed.append(row)
        if len(attempts)%8==0:
            print(json.dumps(dict(progress='middle',accepted=len(accepted),failed=len(failed),
                                  queued=len(queue),elapsed_seconds=time.monotonic()-START)),flush=True)
    remaining=[dict(left=str(a),right=str(b),depth=d,precision=bits,status='not_executed_after_counterpoint')
               for a,b,d,bits in queue]
    status='certified_negative' if negative else ('unresolved' if failed else 'certified')
    return dict(status=status,cells=accepted+failed+negative+remaining,attempts=attempts)


def coverage(cells,left,right):
    intervals=sorted((Fraction(c['left']),Fraction(c['right'])) for c in cells)
    assert intervals and intervals[0][0]==left and intervals[-1][1]==right
    assert all(intervals[j][1]==intervals[j+1][0] for j in range(len(intervals)-1))


def main():
    global ARGS,ROUTE,START,PRIOR,LIVE
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo',type=Path,required=True)
    parser.add_argument('--record',type=Path,required=True)
    parser.add_argument('--prior-seconds',type=float,default=0.0)
    ARGS=parser.parse_args();ARGS.repo=ARGS.repo.resolve()
    ROUTE=Path('papers/investigations-5/07_positive_theta_primitives/jensen')
    PRIOR=ARGS.prior_seconds;START=time.monotonic();P=make_P()
    record=dict(date='2026-11-01',prepared_for='Edward Baker',llm_assistance='substantial',
                model='gpt-6.1-sol',effort='ultra',task='J-E02',revision='r1',
                arithmetic=dict(library='python-flint',version=flint.__version__,FLINT=flint.__FLINT_VERSION__),
                code_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),
                caps=dict(retained_terms=24,Taylor_degree=63,P_order=70,precisions=[128,256],
                          origin_max_leaves=64,origin_max_depth=6,middle_max_leaves=4096,
                          middle_max_depth=8,arithmetic_seconds=1800),
                error_policy='Note09 (14)-(16),(21)-(22), exact full-source parity and low coefficients',
                audited_tail=dict(domain='u>=1',t_cutoff=128,Rprime_lower='63*t^2',K_lower='2^30*t^7'))
    LIVE=record
    names=['notes/05_J_B01_SIGNED_AVERAGING_DECISION_20261101.md',
           'notes/07_J_E01_R2_SIGNED_AVERAGING_AND_Q10_P7_RETURN_20261101.md',
           'notes/08_CONTINUATION_FOR_ASTRA_GLOBAL_SIGNED_AVERAGING_20261101.md',
           'notes/09_J_B02_GLOBAL_TAIL_AND_COMPACT_CERTIFICATE_20261101.md',
           'notes/10_CONTINUATION_FOR_SOL_GLOBAL_SIGN_CERTIFICATE_20261101.md',
           'numerics/j_e01_r2_audit.py','numerics/J_E01_R2_EXACT_RECORD_20261101.json']
    record['input_sha256']={n:sha256((ARGS.repo/ROUTE/n).read_bytes()).hexdigest() for n in names}
    try:
        record['origin']=origin_run(P)
        print(json.dumps(dict(progress='origin',status=record['origin']['status'],elapsed_seconds=time.monotonic()-START)),flush=True)
        record['middle']=middle_run(P)
        coverage(record['origin']['cells'],Fraction(0),Fraction(1,4096))
        coverage(record['middle']['cells'],Fraction(1,64),Fraction(1))
        record['status']='certified' if record['origin']['status']==record['middle']['status']=='certified' else 'bounded_incomplete'
    except TimeoutError as e:
        record.update(status='time_cap_unresolved',error=str(e))
    finally:
        record['arithmetic_elapsed_seconds']=time.monotonic()-START
        record['prior_arithmetic_seconds']=PRIOR
        record['total_arithmetic_seconds']=PRIOR+record['arithmetic_elapsed_seconds']
        if record.get('status')=='certified':
            record.pop('origin_progress',None);record.pop('middle_progress',None)
        ARGS.record.parent.mkdir(parents=True,exist_ok=True)
        ARGS.record.write_text(json.dumps(record,indent=2,ensure_ascii=False)+'\n')
        print(json.dumps(dict(status=record.get('status','implementation_error'),record=str(ARGS.record),
                              elapsed_seconds=record['arithmetic_elapsed_seconds'])),flush=True)


if __name__=='__main__':
    main()
