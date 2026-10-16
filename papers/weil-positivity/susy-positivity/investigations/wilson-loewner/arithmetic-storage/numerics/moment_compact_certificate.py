#!/usr/bin/env python3
"""Certified compact correction for the actual Sonin first trace moment.

Prepared for Edward Baker with GPT-6 (Codex), 2026-09-29.
Exact serving variant and reasoning effort not exposed. No quadrature or
spatial tails are omitted: compact polynomial integrals reduce to exact
exponential spline moments, with operator/cosine/source errors enclosed.
"""
import argparse
from fractions import Fraction as Q
import hashlib
import json
import math
from pathlib import Path
import sys
import time
from flint import arb, ctx, fmpz_poly
from moment_kernel_polynomial import build,ab
from arithmetic_truncated_spline import TruncatedCorrelation


def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()


def run(NUM,N=131072,K=120,bits=1024):
    sys.path.insert(0,str(NUM))
    import source_norm_enclosures as source
    from sonin_scalar_epsilon import quantize,pack,add_error,require
    here=Path(__file__).resolve().parent
    src_path=NUM/'records/source_norm_enclosures.json'
    sr=json.loads(src_path.read_text())
    require(sr['script_sha256']==sha(NUM/'source_norm_enclosures.py'),'Source input hash mismatch')
    model=build(K,bits)
    ctx.prec=bits
    h=arb(2).log()/N;r=1/arb(2).sqrt();c=ab('3/2')
    radius=math.ceil(float(source.B)/float(h))+1
    require(radius*h>source.ball(source.B),'Source grid does not cover the exact support')
    support=(2*radius+2)*h
    require(support<model['L_upper'],'Spline support exceeds kernel model bound')
    scale=2**80
    rows=[]
    print(json.dumps({'stage':'model','operator_error':str(model['operator_error']),
                      'cosine_error':str(model['cosine_error']),'source_nodes':2*radius+1}),flush=True)
    for sid,row in enumerate(sr['sources']):
        started=time.time()
        norm=source.record_ball(row['normalizer'])
        second=source.record_ball(row['normalized_derivative_norm_squares'][2]).sqrt()
        values=[];qerr=arb(0)
        for j in range(-radius,radius+1):
            z,e=quantize(source.source_value(sid,j*h,normalizer=norm),scale)
            values.append(z);qerr=qerr.max(e)
        require(values[0]==values[-1]==0,'Nonzero source endpoints')
        eta=h*h/(arb.pi()**2)*second+support.sqrt()*qerr
        fp=fmpz_poly(values)
        con=(fp*fmpz_poly(list(reversed(values)))).coeffs()
        mid=len(values)-1
        aa=[int(con[mid+j]) if mid+j<len(con) else 0 for j in range(mid+1)]
        def at(j):return aa[abs(j)] if abs(j)<len(aa) else 0
        transported=[c*at(j)-r*(at(j-N)+at(j+N)) for j in range(len(aa)+N)]
        moments=TruncatedCorrelation(transported,h,N,scale)
        contact=h/(scale*scale)*(transported[N-1]+4*transported[N]+transported[N+1])/6
        finite=model['contact']*contact
        for j,lam in enumerate(model['whole']):
            wh,be=moments.evaluate(ab(lam))
            finite+=model['whole'][lam]*wh+model['before'][lam]*be
            if j%40==39:
                print(json.dumps({'stage':'moments','source':sid,'done':j+1,
                                  'elapsed_seconds':time.time()-started}),flush=True)
        gamma=ab('57/1000000')
        Xdiff=model['G_max']*model['z_upper']*eta*(2+eta)
        source_error=4*r/gamma*Xdiff
        operator_error=model['operator_error']*(1+eta)**2
        cosine_error=model['cosine_error']*(1+eta)**2
        total=add_error(finite,source_error+operator_error+cosine_error)
        require(total.is_finite(),'Nonfinite final correction')
        require(total.rad()<ab('1/200'),'Correction width did not resolve 0.01')
        out={'source':sid,'compact_correction':pack(total),
             'finite_interpolant_correction':pack(finite),
             'source_L2_error':pack(eta),'source_replacement_error':pack(source_error),
             'operator_replacement_error':pack(operator_error),'cosine_replacement_error':pack(cosine_error),
             'nodal_coefficients_sha256':hashlib.sha256(json.dumps(values,separators=(',',':')).encode()).hexdigest(),
             'elapsed_seconds':time.time()-started}
        rows.append(out)
        print(json.dumps({'stage':'result','source':sid,'compact_correction':total.str(20),
                          'finite_interpolant':finite.str(20),'source_error':source_error.str(10)}),flush=True)
    dep={name:sha(here/name) for name in ['moment_kernel_polynomial.py','arithmetic_truncated_spline.py']}
    dep.update({'inherited:'+name:sha(NUM/name) for name in
                ['prolate_certificate.py','source_norm_enclosures.py','sonin_scalar_epsilon.py',
                 'records/source_norm_enclosures.json']})
    return {'status':'CERTIFIED','generator':'moment_compact_certificate.py','date':'2026-09-29','model':'GPT-6 (Codex)',
            'serving_variant':'not exposed','reasoning_effort':'not exposed',
            'scope':'Compact correction C with m1=B_infinity[D2^2F]−C. No B2 or arithmetic residual sign is established by this record alone.',
            'script_sha256':sha(Path(__file__)),'dependency_sha256':dep,
            'grid_N':N,'precision_bits':bits,'cosine_terms':K,
            'source_spline_support_diameter':pack(support),'sources':rows}


if __name__=='__main__':
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--numerics',type=Path,default=Path(__file__).resolve().parent)
    ap.add_argument('--grid',type=int,default=131072)
    ap.add_argument('--cosine-terms',type=int,default=120)
    ap.add_argument('--bits',type=int,default=1024)
    ap.add_argument('--output',type=Path,default=Path(__file__).with_suffix('.json'))
    args=ap.parse_args()
    record=run(args.numerics,args.grid,args.cosine_terms,args.bits)
    args.output.write_text(json.dumps(record,indent=2)+'\n')
