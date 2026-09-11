#!/usr/bin/env python3
"""Independent all-input check using the existing v0.3 certificate method.

The rational ceiling 1.98 contains the requested quarter-step. This uses
the existing method, not the proposed cumulative continuation recursion.
"""
import argparse
import hashlib
import json
from pathlib import Path
from types import SimpleNamespace
from flint import arb as A,ctx
import central_residual as r

def run(args):
    ctx.prec=args.bits
    horizon='99/50'
    quarter=A(7).log()+(A(8).log()-A(7).log())/4
    assert quarter<r.c.rat(horizon)
    source=SimpleNamespace(N=args.n,M=args.degree,horizon=horizon,log_horizon=None)
    data=r.c.build(source)
    result=r.c.validate(data,args.floor)
    result['quarter_step_contained']=True
    result['method']='Existing v0.3 central full-operator head/tail method at rational ceiling 1.98'
    result['source_sha256']={str(p.relative_to(r.ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in [Path(__file__).resolve(),Path(r.c.__file__)]}
    Path(args.output).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ['checks','source_sha256']},indent=2),flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--n',type=int,default=256)
    p.add_argument('--degree',type=int,default=260)
    p.add_argument('--bits',type=int,default=3072)
    p.add_argument('--floor',default='1e-31')
    p.add_argument('--output',required=True)
    run(p.parse_args())
