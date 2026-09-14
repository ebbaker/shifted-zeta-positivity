"""A positive piecewise-constant Schur weight for all arithmetic delays."""
import argparse
import hashlib
import json
import math
from pathlib import Path
import sys
from flint import arb as A, ctx

ROOT=Path(__file__).resolve().parent.parent
sys.path.insert(0,str(ROOT/'critical-path-20260910'))
import reference_certify_arb as c

def build(cells=512,iterations=500):
    ctx.prec=256
    L=A(7).log()+(A(8).log()-A(7).log())/4
    active=c.prime_powers(L)
    edges=[]
    for n,p,_ in active:
        delta=A(n).log()*cells/L
        for signed in [-delta,delta]:
            k=math.floor(float(signed.mid()))
            assert k<signed<k+1
            edges.append((A(p).log()/A(n).sqrt(),k))
    # Each translated cell meets at most these two cells. Taking the larger
    # weight separately for each delay is an upper bound on the whole row.
    neighbors=[[(float(alpha.mid()),[j for j in [i+k,i+k+1] if 0<=j<cells]) for alpha,k in edges] for i in range(cells)]
    weights=[1.]*cells
    for _ in range(iterations):
        tw=[sum(alpha*max((weights[j] for j in js),default=0.) for alpha,js in row) for row in neighbors]
        scale=max(tw)+3
        weights=[(x+3*y)/scale for x,y in zip(tw,weights)]
    strings=[format(x,'.16g') for x in weights]
    w=[c.rat(s) for s in strings]
    assert all(x>0 for x in w)
    ratios=[]
    for i in range(cells):
        row=A(0)
        for alpha,k in edges:
            vals=[w[j] for j in [i+k,i+k+1] if 0<=j<cells]
            if vals:row+=alpha*max(v.upper() for v in vals)
        ratios.append((row/w[i]).upper())
    upper=max(ratios)
    return {'scope':'Full arithmetic operator norm via a certified positive Schur weight.','cells':cells,'iterations':iterations,'norm_upper':upper.str(40),'weights':strings,'all_checks_pass':True,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--cells',type=int,default=512);p.add_argument('--output',required=True)
    args=p.parse_args();data=build(args.cells)
    Path(args.output).write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps({k:v for k,v in data.items() if k!='weights'},indent=2))
