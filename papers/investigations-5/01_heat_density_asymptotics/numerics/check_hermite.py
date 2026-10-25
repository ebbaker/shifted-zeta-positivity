#!/usr/bin/env python3
"""Eight exact-rational polynomial controls for HDA-17-AN03.

Prepared for Edward Baker with substantial LLM assistance, gpt-6.1-sol,
actual reasoning effort ultra inherited from parent metadata. Standard
library only; these controls do not certify theta or floating arithmetic.
"""
from fractions import Fraction as Q
from math import comb, factorial
from pathlib import Path
import hashlib
import json
import platform
import sys
import time

def trim(p):
    p=list(map(Q,p))
    while len(p)>1 and p[-1]==0: p.pop()
    return p
def add(p,q):
    r=[Q(0)]*max(len(p),len(q))
    for k,v in enumerate(p): r[k]+=v
    for k,v in enumerate(q): r[k]+=v
    return trim(r)
def scale(p,c): return trim([Q(c)*v for v in p])
def sub(p,q): return add(p,scale(q,-1))
def mul(p,q):
    r=[Q(0)]*(len(p)+len(q)-1)
    for i,u in enumerate(p):
        for j,v in enumerate(q): r[i+j]+=u*v
    return trim(r)
def power(p,n):
    r=[Q(1)]
    for _ in range(n): r=mul(r,p)
    return r
def deriv(p,n=1):
    for _ in range(n): p=[k*p[k] for k in range(1,len(p))] or [Q(0)]
    return trim(p)
def value(p,x):
    r=Q(0)
    for c in reversed(p): r=r*x+c
    return r
def integ(p,a=Q(0),b=Q(1)):
    return sum((v*(b**(k+1)-a**(k+1))/Q(k+1) for k,v in enumerate(p)),Q(0))
def compose(p,q):
    r=[Q(0)]
    for c in reversed(p): r=add(mul(r,q),[c])
    return r
def same(p,q): return trim(p)==trim(q)
def bezier(beta):
    n=len(beta)-1; r=[Q(0)]
    for k,b in enumerate(beta):
        r=add(r,scale(mul(power([0,1],k),power([1,-1],n-k)),comb(n,k)*b))
    return r

S=[Q(0),Q(1)]
H00=[Q(1),Q(0),Q(-3),Q(2)]
H01=[Q(0),Q(0),Q(3),Q(-2)]
H10=[Q(0),Q(1),Q(-2),Q(1)]
H11=[Q(0),Q(0),Q(-1),Q(1)]
ABS_H11=scale(H11,-1)
R4=scale(mul(power(S,2),power([1,-1],2)),Q(1,24))

def hermite(va,vb,da,db,h):
    return add(add(scale(H00,va),scale(H01,vb)),add(scale(H10,h*da),scale(H11,h*db)))

def main():
    begin=time.perf_counter(); cases=[]
    def keep(name,detail): cases.append({'name':name,'status':'passed','details':detail})
    # 1. Complete source derivative polynomial recurrence, independently exact.
    polys=[[-3,2]]
    for _ in range(4):
        p=polys[-1]
        polys.append(add(mul([5,-4],p),mul([0,4],deriv(p))))
    expected=[-1875,30930,-68096,41408,-8448,512]
    assert polys[4]==list(map(Q,expected))
    assert polys[1]==list(map(Q,[-15,30,-8]))
    keep('complete_Phi4_recurrence',{'P0_through_P4':[[str(v) for v in p] for p in polys]})
    # 2. A nontrivial cubic is reproduced as a polynomial on a rational cell.
    a=Q(1,3); b=Q(5,4); h=b-a
    p=[Q(2,7),Q(-5,3),Q(4,5),Q(-7,11)]
    hs=hermite(value(p,a),value(p,b),value(deriv(p),a),value(deriv(p),b),h)
    assert same(hs,compose(p,[a,h]))
    keep('cubic_reproduction',{'cell':[str(a),str(b)],'cubic_power_coefficients':list(map(str,p)),'difference_power_coefficients':['0']})
    # 3. f(u)=u^4 has f4=24. The remainder has exactly the sign/factor 1/24.
    p4=[Q(0),Q(0),Q(0),Q(0),Q(1)]
    h4=hermite(a**4,b**4,4*a**3,4*b**3,h)
    remainder=sub(compose(p4,[a,h]),h4)
    target=scale(R4,24*h**4)
    assert same(remainder,target)
    assert value(remainder,Q(1,2))==h**4/Q(16)
    assert integ(scale(R4,h**5))==h**5/Q(720)
    keep('quartic_remainder_sign_and_1_over_24',{'remainder_power_coefficients':list(map(str,remainder)),'midpoint_remainder':str(value(remainder,Q(1,2))),'integrated_unit_Phi4_remainder':str(h**5/Q(720))})
    # 4. Exact endpoint value perturbations retain H00/H01 independently.
    dva=Q(2,7); dvb=Q(-3,5)
    perturbed=hermite(value(p,a)+dva,value(p,b)+dvb,value(deriv(p),a),value(deriv(p),b),h)
    value_error=sub(perturbed,hs)
    assert same(value_error,add(scale(H00,dva),scale(H01,dvb)))
    for s in [Q(0),Q(1,4),Q(1,2),Q(3,4),Q(1)]:
        assert abs(value(value_error,s))<=abs(dva)*value(H00,s)+abs(dvb)*value(H01,s)
    keep('endpoint_value_perturbations',{'endpoint_errors':[str(dva),str(dvb)],'exact_error_power_coefficients':list(map(str,value_error))})
    # 5. H11 is negative: a positive right derivative perturbation subtracts.
    dda=Q(2,7); ddb=Q(3,5)
    perturbed=hermite(value(p,a),value(p,b),value(deriv(p),a)+dda,value(deriv(p),b)+ddb,h)
    derivative_error=sub(perturbed,hs)
    assert same(derivative_error,add(scale(H10,h*dda),scale(H11,h*ddb)))
    assert value(H11,Q(1,2))==Q(-1,8)
    for s in [Q(0),Q(1,4),Q(1,2),Q(3,4),Q(1)]:
        assert abs(value(derivative_error,s))<=h*(abs(dda)*value(H10,s)+abs(ddb)*value(ABS_H11,s))
    keep('endpoint_derivative_perturbations_and_sign',{'endpoint_derivative_errors':[str(dda),str(ddb)],'right_derivative_cardinal_at_half':'-1/8','exact_error_power_coefficients':list(map(str,derivative_error))})
    # 6. All absolute cardinal integrals and complete-cell chord moments.
    zeroth=[integ(p) for p in [H00,H01,H10,ABS_H11,R4]]
    first=[integ(mul(S,p)) for p in [H00,H01,H10,ABS_H11,R4]]
    assert zeroth==list(map(Q,[Q(1,2),Q(1,2),Q(1,12),Q(1,12),Q(1,720)]))
    assert first==list(map(Q,[Q(3,20),Q(7,20),Q(1,30),Q(1,20),Q(1,1440)]))
    for k in range(4):
        bk=scale(mul(power(S,k),power([1,-1],3-k)),comb(3,k))
        assert integ(bk)==Q(1,4)
        assert integ(mul(S,bk))==Q(k+1,20)
    keep('absolute_cardinal_and_Bernstein_integrals',{'zeroth_moments':list(map(str,zeroth)),'first_moments':list(map(str,first)),'Bernstein_integrals':'1/4 each; first moments (k+1)/20'})
    # 7. Positive endpoint data can produce a negative cubic; fallback stays positive.
    bad_beta=[Q(1),Q(-3),Q(-3),Q(1)]
    assert same(bezier(bad_beta),hermite(1,1,-12,12,1))
    assert value(bezier(bad_beta),Q(1,2))==Q(-2)
    fallback=[Q(1)] # exact line with endpoints 1 and 1
    assert all(value(fallback,s)>=0 for s in [Q(0),Q(1,4),Q(1,2),Q(3,4),Q(1)])
    good_beta=[Q(1),Q(2),Q(3),Q(2)]
    assert same(bezier(good_beta),hermite(1,2,3,-3,1))
    assert min(good_beta)>=0
    keep('Bernstein_positive_branch_and_linear_fallback',{'failed_Bernstein_coefficients':list(map(str,bad_beta)),'failed_cubic_midpoint':'-2','positive_fallback':'1','positive_cubic_Bernstein_coefficients':list(map(str,good_beta))})
    # 8. Dyadic stored coefficients define an exactly nonnegative finite source,
    # while their deviation from ideal coefficients remains a separate ledger.
    va=Q(5,8); vb=Q(9,8); da=Q(1,3); db=Q(-2,5); hh=Q(7,8)
    ideal=[va,va+hh*da/3,vb-hh*db/3,vb]
    stored=[va,Q(23,32),Q(5,4),vb]
    assert min(stored)>=0
    delta=[stored[k]-ideal[k] for k in range(4)]
    assert same(sub(bezier(stored),bezier(ideal)),bezier(delta))
    for s in [Q(0),Q(1,4),Q(1,2),Q(3,4),Q(1)]:
        assert value(bezier(stored),s)>=0
        assert abs(value(bezier(delta),s))<=value(bezier([abs(v) for v in delta]),s)
    assert same(bezier([1,1,1,1]),[1])
    keep('stored_dyadic_coefficients_and_separate_construction_ledger',{'ideal_coefficients':list(map(str,ideal)),'stored_coefficients':list(map(str,stored)),'construction_error_coefficients':list(map(str,delta))})
    elapsed=time.perf_counter()-begin
    record={'prepared_for':'Edward Baker','model':'gpt-6.1-sol','actual_reasoning_effort':'ultra','status':'eight exact-rational polynomial control families passed; no theta or floating arithmetic certification','case_count':len(cases),'runtime_seconds':elapsed,'environment':{'python':sys.version,'platform':platform.platform(),'arithmetic':'Python fractions.Fraction; exact polynomial identities and selected rational inequality substitutions'},'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'controls':cases}
    Path(__file__).with_name('HERMITE_CONTROLS.json').write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps({k:record[k] for k in ['status','case_count','runtime_seconds','script_sha256']},indent=2))
if __name__=='__main__': main()
