#!/usr/bin/env python3
"""Exact finite coefficient-transport controls; no theta acquisition.
Prepared for Edward Baker with LLM assistance, gpt-6-astra, effort ultra.
23 October 2026, America/New_York. Standard-library rational arithmetic.
Default output is JSON on stdout; file writing requires --output.
"""
from fractions import Fraction as F
from itertools import combinations
from math import factorial, comb
import argparse
import json


def trim(p):
    p=list(map(F,p))
    while len(p)>1 and p[-1]==0:
        p.pop()
    return p


def add(p,q):
    out=[F(0)]*max(len(p),len(q))
    for i,x in enumerate(p): out[i]+=x
    for i,x in enumerate(q): out[i]+=x
    return trim(out)


def scale(p,c): return trim([F(c)*x for x in p])


def multiply(p,q):
    out=[F(0)]*(len(p)+len(q)-1)
    for i,x in enumerate(p):
        for j,y in enumerate(q): out[i+j]+=x*y
    return trim(out)


def derivative(p,k=1):
    p=list(p)
    for _ in range(k):
        p=[i*p[i] for i in range(1,len(p))] or [F(0)]
    return trim(p)


def evaluate(p,x): return sum(c*x**i for i,c in enumerate(p))


def divrem(p,q):
    p=trim(p);q=trim(q)
    if q==[0]: raise ZeroDivisionError
    quotient=[F(0)]*max(1,len(p)-len(q)+1)
    while p!=[0] and len(p)>=len(q):
        k=len(p)-len(q); c=p[-1]/q[-1]
        quotient[k]+=c
        p=add(p,[F(0)]*k+scale(q,-c))
    return trim(quotient),trim(p)


def from_roots(roots):
    p=[F(1)]
    for r in roots:p=multiply(p,[-F(r),F(1)])
    return p


def heat(p,h):
    out=[F(0)]
    for j in range((len(p)-1)//2+1):
        out=add(out,scale(derivative(p,2*j),h**j/F(factorial(j))))
    return out


def heat_matrix(n,h):
    return [[F(factorial(k),factorial(j)*factorial((k-j)//2))*h**((k-j)//2)
             if k>=j and (k-j)%2==0 else F(0)
             for k in range(n+1)] for j in range(n+1)]


def matmul(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def matvec(a,p):
    p=list(p)+[F(0)]*(len(a)-len(p))
    return trim([sum(x*y for x,y in zip(row,p)) for row in a])


def norm(p,R):return sum(abs(c)*R**j for j,c in enumerate(p))


def C(n,x):
    return sum(F(factorial(n),factorial(k)*factorial(n-2*k))*x**k
               for k in range(n//2+1))


def integral_C(n,h,R):
    return sum(F(factorial(n),factorial(k)*factorial(n-2*k))*h**(k+1)
               /(F(k+1)*R**(2*k)) for k in range(n//2+1))


def time_eval(powers,t):
    out=[F(0)]
    for k,p in enumerate(powers):out=add(out,scale(p,t**k))
    return out


def drift_heat_time_series(p,c):
    powers=[]; current=p
    for k in range(len(p)):
        powers.append(scale(current,F((-1)**k,factorial(k))))
        current=add(derivative(current,2),scale(derivative(current),2*c))
    return powers


def integrate_heat_forcing(time_powers,t0,T):
    """Exact integral from t0 to T of exp((s-t0)D²)R(s) ds."""
    out=[F(0)]
    for k,p in enumerate(time_powers):
        for j in range((len(p)-1)//2+1):
            factor=F(0)
            for r in range(j+1):
                factor+=F(comb(j,r),factorial(j))*(-t0)**(j-r)*(
                    T**(k+r+1)-t0**(k+r+1))/F(k+r+1)
            out=add(out,scale(derivative(p,2*j),factor))
    return out


def source_moment_series(series,c,N):
    # Reciprocal Laurent series in v=1/z, independently of the shift operator.
    def z_coefficient(time_series,i):
        return trim([p[i] if 0<=i<len(p) else F(0) for p in time_series])
    denominator=[z_coefficient(series,N-j) for j in range(N+1)]
    inverse_series=[[F(1)]]
    for j in range(1,N+1):
        out=[F(0)]
        for r in range(1,j+1):
            out=add(out,multiply(denominator[r],inverse_series[j-r]))
        inverse_series.append(scale(out,-1))
    numerator_series=[add(derivative(p,2),scale(derivative(p),2*c)) for p in series]
    numerator=[z_coefficient(numerator_series,N-j) for j in range(N+1)]
    moments=[]
    for k in range(N):
        out=[F(0)]
        for r in range(k+2):
            out=add(out,multiply(numerator[r],inverse_series[k+1-r]))
        moments.append(out)
    return moments


def integrate_time(p,t0,T):
    return sum(c*(T**(k+1)-t0**(k+1))/F(k+1) for k,c in enumerate(p))


def shift_operator(p,moments):
    out=[F(0)]
    for j,c in enumerate(moments,1):
        out=add(out,scale(p[j:] or [F(0)],c))
    return out


def shift_exponential(p,moments):
    out=list(p);current=list(p)
    for k in range(1,len(p)):
        current=shift_operator(current,moments)
        out=add(out,scale(current,F(1,factorial(k))))
    return out


def exp_coefficients(moments,n):
    generator=[F(0)]+list(moments)
    current=[F(1)];out=[F(1)]
    for k in range(1,n+1):
        current=trim(multiply(current,generator)[:n+1])
        out=add(out,scale(current,F(1,factorial(k))))
    return out+[F(0)]*(n+1-len(out))


def run():
    count=0
    def expect(condition,label):
        nonlocal count
        count+=1
        if not condition:raise AssertionError(label)
    remainder_rows=[]
    root_sets=[[-1,1],[-1,0,2],[-2,-1,1,3],[0,0],[0,0,2],
               [-1,-1,1,1],[0,0,0],[0,0,0,2]]
    for roots in root_sets:
        roots=list(map(F,roots)); P=from_roots(roots)
        for b in [[F(2,3)],[F(1),F(-2),F(0),F(3,5)]]:
            product=multiply(b,derivative(P))
            quotient,remainder=divrem(product,P)
            residue=[F(0)]
            for r in sorted(set(roots)):
                factor,zero=divrem(P,[-r,F(1)])
                expect(zero==[0],'exact root division')
                residue=add(residue,scale(factor,roots.count(r)*evaluate(b,r)))
            expect(remainder==residue,'wall residue remainder with multiplicity')
            expect(add(multiply(quotient,P),remainder)==product,'division recovery')
            remainder_rows.append({'roots':[str(r) for r in roots],
                                   'b':[str(x) for x in b],
                                   'remainder':[str(x) for x in remainder]})

    matrix_rows=[]
    h,k,R=F(4,7),F(3,5),F(3,2)
    for N in range(2,9):
        # Full polynomials have degree N; monic differences degree at most N-1.
        E=heat_matrix(N,h)
        expect(matmul(E,heat_matrix(N,k))==heat_matrix(N,h+k),'finite heat semigroup')
        expect(matmul(E,heat_matrix(N,-h))==heat_matrix(N,F(0)),'finite heat inverse')
        p=[F((-1)**j,j+1) for j in range(N+1)]
        expect(matvec(E,p)==heat(p,h),'matrix versus derivative polynomial')
        n=N-1; M=heat_matrix(n,h)
        column_norms=[sum(abs(M[i][j])*R**i/R**j for i in range(n+1))
                      for j in range(n+1)]
        exact=C(n,h/R**2)
        expect(max(column_norms)==column_norms[-1]==exact,'sharp induced weighted norm')
        eT=[F(0)]*n+[1/R**n]
        expect(norm(heat(eT,h),R)==exact,'attaining terminal monomial')
        beta=F(2,5)
        integrated=integrate_heat_forcing([eT],F(0),h)
        total=add(heat(eT,h),scale(integrated,beta))
        bound=exact+beta*integral_C(n,h,R)
        expect(norm(total,R)==bound,'attaining joint Duhamel norm bound')
        expect(heat(heat(p,-h),h)==trim(p),'unforced backward polynomial recovery')
        matrix_rows.append({'N':N,'error_degree':n,'h':str(h),'R':str(R),
                            'sharp_norm':str(exact),'sharp_forced_bound':str(bound)})

    duhamel_rows=[]
    for N in range(2,6):
        P0=from_roots([F(j-2,2) for j in range(N)])
        for c in [F(-2,3),F(1,5)]:
            series=drift_heat_time_series(P0,c)
            t0,T=F(1,7),F(4,5)
            P_t0=time_eval(series,t0);P_T=time_eval(series,T)
            Rseries=[scale(derivative(p),c) for p in series]
            recovered=add(heat(P_T,T-t0),scale(integrate_heat_forcing(Rseries,t0,T),2))
            expect(recovered==P_t0,'complete backward forced Duhamel sign')
            expect(heat(P_T,T-t0)!=P_t0,'dropping forcing gives a wrong polynomial')
            Pt=[scale(series[j],j) for j in range(1,len(series))]
            residual=add(time_eval(Pt,t0),add(derivative(P_t0,2),scale(derivative(P_t0),2*c)))
            expect(residual==[0],'drift heat differential equation')
            duhamel_rows.append({'N':N,'constant_b':str(c),'t0':str(t0),'T':str(T),
                                 'recovered':True,'forcing_required':True})

    # Complete shifted-sine/cosine pair ±1: true exterior values agree modulo P
    # with b_rep=-z/2. Thus Rem_P(bP')=-1 exactly, irrespective of pi.
    P=[F(-1),F(0),F(1)];b=[F(0),F(-1,2)]
    _,rem=divrem(multiply(b,derivative(P)),P)
    expect(rem==[F(-1)],'stationary cosine full exterior remainder')
    expect(add(scale(derivative(P,2),-1),scale(rem,-2))==[0],
           'stationary cosine cancellation')
    recovered=add(heat(P,h),scale(integrate_heat_forcing([rem],0,h),2))
    expect(recovered==P,'stationary cosine backward recovery')
    expect(heat(P,h)!=P,'unforced sine pair prediction fails')

    precision_rows=[]
    for t in [F(1,7),F(1,100),F(1,10000)]:
        eta=F(1,5);epsilon=eta*t
        a=4*t;p=-2*t+epsilon
        Q=2*a/(-4*p+2*a)
        expect(Q==F(2)/(4-eta),'quadratic scaled coefficient error persists')
        expect(Q-F(1,2)==eta/(2*(4-eta)),'quadratic filter precision constant')
        expect(heat([epsilon],h)==[epsilon],'constant coefficient error has no amplification')
        precision_rows.append({'t':str(t),'epsilon_over_t':str(eta),'q':str(Q)})
    for rt in [F(1,3),F(1,10),F(1,100)]:
        t=rt*rt;eta=F(1,2);p=-6*t;d=eta*rt**3;a=4*t;B=-3*p
        delta=-4*p**3-27*d*d
        Q=(2*a*B*B+12*a*a*B)/(delta+2*a*B*B+6*a*a*B)
        expect(Q==F(6048)/(5184-27*eta*eta),'cubic scaled coefficient error persists')
        expect(heat([d],h)==[d],'cubic constant coefficient error has no amplification')

    source_rows=[]
    for N in range(2,9):
        P0=from_roots([F(j-2,2) for j in range(N)])
        for c in [F(0),F(-2,3),F(1,5)]:
            series=drift_heat_time_series(P0,c)
            moments=source_moment_series(series,c,N)
            t0,T=F(1,7),F(4,5)
            P_early=time_eval(series,t0);P_late=time_eval(series,T)
            integrated=[integrate_time(m,t0,T) for m in moments]
            recovered=shift_exponential(P_late,integrated)
            expect(recovered==P_early,'complete-source integrated moment propagator')
            instantaneous=[evaluate(m,t0) for m in moments]
            expected=add(derivative(P_early,2),scale(derivative(P_early),2*c))
            expect(shift_operator(P_early,instantaneous)==expected,
                   'source Laurent residues give actual coefficient equation')
            expect(evaluate(moments[0],t0)==2*c*N,'complete exterior zeroth source moment')
            source_rows.append({'N':N,'b':str(c),'exact_recovery':True})

    shift_norm_rows=[]
    for N in range(2,9):
        n=N-1; R=F(3,2)
        J=[F((-1)**j*(j+2),j+3) for j in range(1,n+1)]
        K=[F(2*j-1,2*j+3) for j in range(1,n+1)]
        p=[F(j+1,j+2) for j in range(n+1)]
        expect(shift_operator(shift_operator(p,J),K)==shift_operator(shift_operator(p,K),J),
               'all complete-source shift operators commute')
        expect(shift_exponential(shift_exponential(p,J),K)==
               shift_exponential(p,[a+b for a,b in zip(J,K)]),
               'finite exponential composition')
        coeff=exp_coefficients(J,n)
        matrix=[[coeff[j-i] if j>=i else F(0) for j in range(n+1)] for i in range(n+1)]
        expect(matvec(matrix,p)==shift_exponential(p,J),
               'scalar truncated exponential versus direct operator exponential')
        exact=sum(abs(coeff[j])/R**j for j in range(n+1))
        columns=[sum(abs(matrix[i][j])*R**i/R**j for i in range(n+1))
                 for j in range(n+1)]
        expect(max(columns)==columns[-1]==exact,'exact source propagator weighted norm')
        shift_norm_rows.append({'N':N,'sharp_norm':str(exact)})
    cubic_error=[F(0),F(0),F(1)]
    expect(shift_exponential(cubic_error,[0,6*h])==[6*h,0,1],
           'cubic fixed-source error amplification')
    expect(heat(cubic_error,h)==[2*h,0,1],
           'unforced coefficient error uses a different generator')
    expect(shift_exponential(P,[0,0])==P,'stationary cosine source moments vanish')

    return {'date':'2026-10-23','timezone':'America/New_York',
        'prepared_for':'Edward Baker','llm_assistance':True,
        'model':'gpt-6-astra','reasoning_effort':'ultra',
        'arithmetic':'Python standard-library fractions.Fraction; exact rationals',
        'status':'PASS','assertions':count,
        'scope':'Finite coefficient, remainder and forcing controls; no theta estimate or independent acquisition of the nonlinear source residual.',
        'remainder_controls':remainder_rows,'semigroup_and_norm_controls':matrix_rows,
        'complete_source_moment_controls':source_rows,'source_shift_norm_controls':shift_norm_rows,
        'forced_duhamel_controls':duhamel_rows,'precision_controls':precision_rows,
        'stationary_cosine':{'population_polynomial':'z^2-1',
                            'exterior_remainder':'-1','forcing_required':True}}


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',help='Optional explicit output file; default is stdout only.')
    args=parser.parse_args()
    result=run();serialized=json.dumps(result,indent=2,sort_keys=True)
    if args.output:
        with open(args.output,'w') as f:f.write(serialized+'\n')
    print(serialized)
