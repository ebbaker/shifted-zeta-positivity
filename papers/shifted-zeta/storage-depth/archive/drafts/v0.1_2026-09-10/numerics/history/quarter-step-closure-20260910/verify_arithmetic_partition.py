"""Replay the Schur weight on every interval where any shifted weight changes."""
from fractions import Fraction as F
import hashlib
import json
import math
from pathlib import Path
from flint import arb as A,ctx
import arithmetic_bound as base

def run():
    ctx.prec=256
    here=Path(__file__).resolve().parent
    source=here/'arithmetic_512.json'
    record=json.loads(source.read_text());n=record['cells']
    w=[base.c.rat(x) for x in record['weights']]
    primes=[2,3,5,7];logs=[A(p).log() for p in primes]
    # L_q=(3/4)log(14). Exact prime-exponent vectors identify equal cuts.
    grid=[(F(3*j,4*n),F(0),F(0),F(3*j,4*n)) for j in range(n+1)]
    zero=grid[0];end=grid[-1]
    active=[(2,2,1),(3,3,1),(4,2,2),(5,5,1),(7,7,1)]
    shifts=[]
    for number,powerbase,power in active:
        for sign in [-1,1]:
            exponents=[F(0)]*4;exponents[primes.index(powerbase)]=F(sign*power)
            shifts.append((tuple(exponents),A(powerbase).log()/A(number).sqrt()))
    def value(key):return sum((base.c.rat(e)*l for e,l in zip(key,logs)),A(0))
    L=value(end)
    keys=set(grid)
    for point in grid:
        for delta,_ in shifts:
            key=tuple(x-y for x,y in zip(point,delta))
            x=value(key)
            if key==zero or key==end or 0<x<L:keys.add(key)
            else:assert x<0 or x>L
    cuts=sorted([(key,value(key)) for key in keys],key=lambda kv:float(kv[1].mid()))
    def cell(x):
        scaled=x*n/L;j=math.floor(float(scaled.mid()))
        assert 0<=j<n and j<scaled<j+1
        return j
    ratios=[]
    for (_,lo),(_,hi) in zip(cuts,cuts[1:]):
        assert lo<hi
        x=(lo+hi)/2;i=cell(x);row=A(0)
        for delta,alpha in shifts:
            y=x+value(delta)
            if 0<y<L:row+=alpha*w[cell(y)]
            else:assert y<0 or y>L
        ratios.append((row/w[i]).upper())
    upper=max(ratios)
    assert upper<A('1.95')
    assert upper<=A(record['norm_upper']).upper()
    output={'scope':'Independent interval-partition verification of the saved positive arithmetic Schur weight.',
            'all_checks_pass':True,'intervals':len(ratios),'norm_upper':upper.str(40),
            'weight_record_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    (here/'arithmetic_partition_check.json').write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps(output,indent=2))

if __name__=='__main__':run()
