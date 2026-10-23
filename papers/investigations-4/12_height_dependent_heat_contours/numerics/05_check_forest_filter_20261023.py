#!/usr/bin/env python3
"""Exact rational controls for HDC11. No theta source or numerical acquisition.
Prepared for Edward Baker with LLM assistance, gpt-6-astra, effort ultra.
23 October 2026, America/New_York. Uses Python standard library only.
"""
from fractions import Fraction as F
from itertools import combinations
from math import factorial, prod
import argparse
import json


def determinant(matrix):
    a = [list(map(F, row)) for row in matrix]
    n = len(a)
    result = F(1)
    for i in range(n):
        pivot = next((j for j in range(i,n) if a[j][i]), None)
        if pivot is None:
            return F(0)
        if pivot != i:
            a[i], a[pivot] = a[pivot], a[i]
            result = -result
        p = a[i][i]
        result *= p
        for j in range(i+1,n):
            ratio = a[j][i]/p
            for k in range(i+1,n):
                a[j][k] -= ratio*a[i][k]
            a[j][i] = 0
    return result


def inverse(matrix):
    n = len(matrix)
    a = [[F(x) for x in row] + [F(i==j) for j in range(n)]
         for i,row in enumerate(matrix)]
    for i in range(n):
        pivot = next(j for j in range(i,n) if a[j][i])
        a[i], a[pivot] = a[pivot], a[i]
        p = a[i][i]
        a[i] = [v/p for v in a[i]]
        for j in range(n):
            if j != i:
                r = a[j][i]
                a[j] = [v-r*w for v,w in zip(a[j],a[i])]
    return [row[n:] for row in a]


def forests(n):
    edges = list(combinations(range(n),2))
    rows = []
    for mask in range(1<<len(edges)):
        parent = list(range(n))
        sizes = [1]*n
        def root(i):
            while parent[i] != i:
                i = parent[i]
            return i
        selected = []
        for e,(i,j) in enumerate(edges):
            if mask>>e & 1:
                ri,rj = root(i),root(j)
                if ri == rj:
                    break
                parent[ri] = rj
                sizes[rj] += sizes[ri]
                selected.append(e)
        else:
            factor = prod(sizes[i] for i in range(n) if root(i)==i)
            rows.append((tuple(selected), factor))
    return edges, rows


def forest_polynomial(points, table):
    edges, rows = table
    d = [(points[i]-points[j])**2 for i,j in edges]
    coefficients = [F(0)]*len(points)
    for selected, factor in rows:
        selected = set(selected)
        coefficients[len(selected)] += factor*prod(
            d[e] for e in range(len(edges)) if e not in selected)
    return coefficients


def poly_eval(coefficients, x):
    return sum(c*x**k for k,c in enumerate(coefficients))


def laplacian(points):
    n = len(points)
    out = [[F(0) for _ in points] for _ in points]
    for i,j in combinations(range(n),2):
        w = 1/(points[i]-points[j])**2
        out[i][i] += w
        out[j][j] += w
        out[i][j] -= w
        out[j][i] -= w
    return out


def monic_coefficients(points):
    c = [F(1)]
    for x in points:
        d = [F(0)]*(len(c)+1)
        for k,v in enumerate(c):
            d[k] -= x*v
            d[k+1] += v
        c = d
    return list(reversed(c))


def resultant(p, q):
    """Descending coefficients; Sylvester determinant."""
    m,n = len(p)-1,len(q)-1
    rows = []
    for shift in range(n):
        rows.append([F(0)]*shift+list(map(F,p))+[F(0)]*(n-1-shift))
    for shift in range(m):
        rows.append([F(0)]*shift+list(map(F,q))+[F(0)]*(m-1-shift))
    return determinant(rows)


def heat_polynomial(m,t):
    asc = [F(0)]*(m+1)
    for j in range(m//2+1):
        asc[m-2*j] = (-t)**j*F(factorial(m), factorial(j)*factorial(m-2*j))
    return list(reversed(asc))


def checks():
    count = 0
    def expect(condition, label):
        nonlocal count
        count += 1
        if not condition:
            raise AssertionError(label)
    tables = {n:forests(n) for n in range(2,6)}
    configurations = 0
    matrix_evaluations = 0
    for n,table in tables.items():
        configurations_list = [list(map(F,range(n))),
            [F(i*i+2*i-3,3) for i in range(n)],
            [F(i//2)+F(i%2,1000) for i in range(n)]]
        for points in configurations_list:
            configurations += 1
            coeff = forest_polynomial(points,table)
            delta = prod((points[i]-points[j])**2 for i,j in table[0])
            expect(coeff[0]==delta, 'constant coefficient is discriminant')
            expect(coeff==forest_polynomial(list(reversed(points)),table),
                   'root permutation invariance')
            L = laplacian(points)
            for a in [F(1,7),F(1),F(13,4)]:
                matrix_evaluations += 1
                matrix = [[F(i==j)+a*L[i][j] for j in range(n)] for i in range(n)]
                D = poly_eval(coeff,a)
                expect(D==delta*determinant(matrix),'forest determinant identity')
                qa = sum(k*c*a**k for k,c in enumerate(coeff))/D
                inv = inverse(matrix)
                qtrace = n-sum(inv[i][i] for i in range(n))
                expect(qa==qtrace,'log derivative filter identity')
                if n==2:
                    _,b,c = monic_coefficients(points)
                    disc = b*b-4*c
                    expect(D==disc+2*a,'quadratic formula')
                if n==3:
                    _,b,c,d = monic_coefficients(points)
                    B = b*b-3*c
                    disc = b*b*c*c-4*c**3-4*b**3*d-27*d*d+18*b*c*d
                    expect(delta==disc,'cubic coefficient discriminant')
                    expect(D==disc+2*a*B*B+6*a*a*B,'cubic forest formula')
                    expect(qa==(2*a*B*B+12*a*a*B)/D,'cubic filter formula')

    collision_rows = []
    for points in [[0,0],[0,0,1],[0,0,1,1],[0,0,1,1,2],
                   [0,0,0],[0,0,0,1],[0,0,0,1,2],[0,0,0,1,1]]:
        points = list(map(F,points))
        c = forest_polynomial(points,tables[len(points)])
        D = poly_eval(c,F(2,3))
        largest = max(points.count(x) for x in points)
        expect((D>0)==(largest<=2),'collision multiplicity nonvanishing control')
        collision_rows.append({'points':[str(x) for x in points], 'D':str(D)})

    for b in [F(1,3),F(2)]:
        points=[-b,-b,b,b]
        c=forest_polynomial(points,tables[4])
        for a in [F(1,7),F(1)]:
            expected=4*a*a*(2*b)**8+16*a**3*(2*b)**6
            expect(poly_eval(c,a)==expected,'simultaneous doubles explicit formula')
    for t in [F(1,7),F(1,3)]:
        a=4*t
        B=18*t
        delta=864*t**3
        D=delta+2*a*B*B+6*a*a*B
        G=2*a*B*B+12*a*a*B
        expect(D==5184*t**3 and G==6048*t**3,'cubic physical D and numerator')

    for a in [F(1,7),F(1),F(4)]:
        radius = a/8
        expect(2*a-4*radius==3*a/2,'complex coefficient disk denominator')
        expect(4*radius/(2*a-4*radius)==F(1,3),'complex coefficient disk quotient error')
        expect(2*a/(2*a+4*radius)==F(4,5),'real coefficient interval lower bound')
        for k in range(9):
            p = -radius*F(k,8)
            Q = 2*a/(2*a-4*p)
            expect(F(4,5)<=Q<=1,'real double interval samples')

    discriminant_checks = []
    for m in range(2,8):
        for t in [F(1,3),F(2,5)]:
            p = heat_polynomial(m,t)
            derivative = [(m-k)*p[k] for k in range(m)]
            disc = (-1)**(m*(m-1)//2)*resultant(p,derivative)
            J=m*(m-1)//2
            expected = (2*t)**J*prod(j**j for j in range(1,m+1))
            expect(disc==expected,'heat Hermite discriminant scaling')
            discriminant_checks.append({'m':m,'t':str(t),'discriminant':str(disc)})

    hermite_rows = []
    for m,t,points in [(2,F(1,2),[F(-1),F(1)]),
                       (3,F(1,6),[F(-1),F(0),F(1)])]:
        coeff = forest_polynomial(points,tables[m])
        for a in [F(1,5),F(2),4*t]:
            J=m*(m-1)//2
            expectedD = 2**J*prod(j**j for j in range(1,m+1))*t**((m-1)*(m-2)//2)*prod(t+a*F(k,4) for k in range(1,m))
            D = poly_eval(coeff,a)
            expect(D==expectedD,'Hermite forest scaling at exact rational roots')
            Q = sum(k*c*a**k for k,c in enumerate(coeff))/D
            expectedQ = sum(a*k/(4*t+a*k) for k in range(1,m))
            expect(Q==expectedQ,'Hermite complete filter spectrum')
            if a==4*t:
                expect(Q==m-sum(F(1,k) for k in range(1,m+1)),
                       'physical Hermite harmonic signature')
            hermite_rows.append({'m':m,'t':str(t),'a':str(a),'D':str(D),'Q':str(Q)})

    for rt in [F(1,2),F(1,3)]:
        t=rt*rt
        a=4*t
        for eta in [F(0),F(1),F(5)]:
            p=-6*t
            constant=eta*rt**3
            B=-3*p
            delta=-4*p**3-27*constant**2
            D=delta+2*a*B*B+6*a*a*B
            G=2*a*B*B+12*a*a*B
            expect(G/D==F(6048)/(5184-27*eta*eta),
                   'heat-scale cubic shape perturbation')

    # Algebraic cubic controls do not require complex algebraic root extraction.
    for r in [F(1,3),F(1,7),F(1,100)]:
        B=F(0); delta=-27*r**6; a=F(2,3)
        D=delta+2*a*B*B+6*a*a*B
        Q=(2*a*B*B+12*a*a*B)/D
        expect(D==delta and Q==0,'complex equilateral triple path')
    k=F(1,10)
    expect((2*k+12)/(F(4,27)*k*k+2*k+6)==F(8235,4186),
           'restricted real triple explicit lower endpoint')

    return {'date':'2026-10-23','timezone':'America/New_York',
        'prepared_for':'Edward Baker','llm_assistance':True,
        'model':'gpt-6-astra','reasoning_effort':'ultra',
        'arithmetic':'Python standard-library fractions.Fraction; exact rationals',
        'status':'PASS','assertions':count,
        'scope':'Finite algebra controls only; no theta acquisition, root-count certificate, or simplicity evidence.',
        'forest_counts':{str(n):len(table[1]) for n,table in tables.items()},
        'distinct_configurations':configurations,'matrix_evaluations':matrix_evaluations,
        'collision_controls':collision_rows,
        'hermite_discriminants':discriminant_checks,
        'hermite_matrix_controls':hermite_rows}


if __name__ == '__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',help='Optional explicit output file; default is stdout only.')
    args=parser.parse_args()
    record=checks()
    serialized=json.dumps(record,indent=2,sort_keys=True)
    if args.output:
        with open(args.output,'w') as f:
            f.write(serialized+'\n')
    print(serialized)
