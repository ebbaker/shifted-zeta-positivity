#!/usr/bin/env python3
"""Exact rank-three Jacobi, residue and flat-control identities; not a physical metric solver."""
import argparse
from fractions import Fraction as F
import json
from pathlib import Path


def mat(rows):
    return [[F(v) for v in row] for row in rows]


def mul(a,b):
    return [[sum((a[i][k]*b[k][j] for k in range(3)),F(0)) for j in range(3)] for i in range(3)]


def trans(a):
    return [list(row) for row in zip(*a)]


def add(*args):
    return [[sum((a[i][j] for a in args),F(0)) for j in range(3)] for i in range(3)]


def scale(a,s):
    return [[x*s for x in row] for row in a]


def det(a):
    return sum((a[0][j]*(a[1][(j+1)%3]*a[2][(j+2)%3]-a[1][(j+2)%3]*a[2][(j+1)%3]) for j in range(3)),F(0))


def inverse(a):
    rows=[row[:] + [F(i==j) for j in range(3)] for i,row in enumerate(a)]
    for i in range(3):
        k=next(k for k in range(i,3) if rows[k][i])
        rows[i],rows[k]=rows[k],rows[i]
        value=rows[i][i];rows[i]=[x/value for x in rows[i]]
        for k in range(3):
            if k!=i:
                value=rows[k][i]
                rows[k]=[x-value*y for x,y in zip(rows[k],rows[i])]
    return [row[3:] for row in rows]


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path);args=p.parse_args()
    eye=mat([[1,0,0],[0,1,0],[0,0,1]]);zero=scale(eye,0)
    r=mat([[0,0,0],[1,-1,0],[0,1,F(-4,3)]])
    v=mat([[0,0,0],[0,0,0],[1,F(-4,3),F(4,9)]])
    assert add(mul(r,r),r,scale(v,-1))==zero
    assert add(mul(r,v),scale(v,F(4,3)))==zero
    assert add(mul(v,v),scale(v,F(-4,9)))==zero
    cyclic=[[eye[i][0],r[i][0],mul(r,r)[i][0]] for i in range(3)]
    assert det(cyclic)==1
    evaluate=mat([[1,0,0],[1,-1,0],[1,F(-4,3),F(4,9)]])
    weights=mat([[16,0,0],[0,-64,0],[0,0,48]])
    eta=mul(mul(trans(evaluate),weights),evaluate)
    expected=mat([[0,0,F(64,3)],[0,F(64,3),F(-256,9)],[F(64,3),F(-256,9),F(256,27)]])
    assert eta==expected and det(eta)==-F(64,3)**3
    assert mul(eta,r)==mul(trans(r),eta)
    diagonal=mat([[0,0,0],[0,-1,0],[0,0,F(-4,3)]])
    assert mul(evaluate,r)==mul(diagonal,evaluate)
    higgs_u=scale(r,F(1,16))
    higgs_spectrum=mat([[0,0,0],[0,F(-1,16),0],[0,0,F(-1,12)]])
    assert mul(evaluate,higgs_u)==mul(higgs_spectrum,evaluate)
    positive=mat([[16,0,0],[0,64,0],[0,0,48]])
    gram=mul(mul(trans(evaluate),positive),evaluate)
    assert det(evaluate)!=0 and all(positive[i][i]>0 for i in range(3))
    assert mul(gram,r)==mul(trans(r),gram)
    reality=mul(inverse(eta),gram)
    assert mul(reality,reality)==eye and gram[0][0]==128
    record={'status':'passed','arithmetic':'exact rational matrices',
            'checks':['Jacobi relations and identity cyclicity','orbit residue and multiplication invariance','semisimple spectrum and canonical Higgs factor','positive flat metric-equation control and reality'],
            'higgs_c':'-R/(16*c^2)','higgs_inverse_coordinate':'R/16',
            'residue_orbit_weights':[16,-64,48],
            'flat_identity_norm':128,
            'limitation':'Checks finite algebra and an auxiliary metric-equation solution; does not identify that solution with the physical metric or establish Weil positivity.'}
    text=json.dumps(record,indent=2,sort_keys=True)+'\n'
    if args.output:
        with args.output.open('x') as f:f.write(text)
    print(text,end='')


if __name__=='__main__':main()
