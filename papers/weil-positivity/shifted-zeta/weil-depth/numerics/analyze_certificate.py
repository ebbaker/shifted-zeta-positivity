#!/usr/bin/env python3
"""Recheck saved balls, derive continuation, and diagnose relative coupling.

All asserted continuation inequalities use Arb/exact rational arithmetic.
The final eigenvalues after high-precision congruence are diagnostics only.
"""
from pathlib import Path
import argparse, gzip, hashlib, json, sys
from fractions import Fraction as F
import numpy as np
from flint import arb as A, arb_mat as AM, ctx
import certify_arb as c


def relative_diagnostic(q,e):
    n=q.nrows();low=AM(n,n);piv=[]
    # Numerical congruence for the chosen midpoint matrices. The eigenvalues
    # subsequently computed in double precision are not used for certification.
    q,e=q.mid(),e.mid()
    for i in range(n):
        v=q[i,i]-sum((low[i,k]**2*piv[k] for k in range(i)),A(0))
        assert v>0
        piv.append(v);low[i,i]=1
        for j in range(i+1,n):
            low[j,i]=(q[j,i]-sum((low[j,k]*low[i,k]*piv[k] for k in range(i)),A(0)))/v
    inv=low.inv()
    for i in range(n):
        for j in range(n):inv[i,j]/=piv[i].sqrt()
    z=inv*e*inv.transpose()
    arr=np.array([[float(z[i,j].mid()) for j in range(n)] for i in range(n)])
    vals=np.linalg.eigvalsh((arr+arr.T)/2)
    return {'minimum':float(vals[0]),'maximum':float(vals[-1]),
            'status':'Floating-point spectral diagnostic after Arb congruence; not a certificate'}


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('folder')
    ap.add_argument('--legacy')
    ap.add_argument('--shift',help='Positive rational upper shift; defaults to a certified dyadic value')
    ap.add_argument('--decay',help='Positive rational decay coefficient; defaults to half the central floor')
    ap.add_argument('--generator-bound',help='Rational upper bound for C_L; defaults to a checked integer')
    args=ap.parse_args();folder=Path(args.folder)
    archive=c.locate(folder/'central_matrices.json.gz')
    with gzip.open(archive,'rt') as f:data=json.load(f)
    ctx.prec=data['precision_bits']
    cert=json.loads((folder/'central_certificate.json').read_text())
    digest=hashlib.sha256(archive.read_bytes()).hexdigest()
    if digest != cert['matrix_archive_sha256']:
        raise ValueError('Certificate hash does not match the matrix archive')
    if 'matrices_content_sha256' in cert and c.content_sha256(data) != cert['matrices_content_sha256']:
        raise ValueError('Certificate content hash does not match the matrices in the archive')
    for key in ('N','M','precision_bits','horizon','log_horizon'):
        if cert[key] != data[key]:
            raise ValueError('Certificate/archive metadata mismatch: '+key)
    # A PASS string alone is not evidence: rerun the ball tests before using m.
    replay=c.validate(data,cert['central_coercivity'])
    if replay['status']!='PASS' or cert['status']!='PASS':
        raise ValueError('No valid central certificate; continuation is unavailable')
    mats={k:AM([[c.unpack(x) for x in row] for row in mat]) for k,mat in data['matrices'].items()}
    out={'matrix_archive_sha256':digest,'central_replay':'PASS','relative_coupling':[]}
    b={k:c.unpack(v) for k,v in data['bounds'].items()}
    # Horizon-specific display checks are supplementary, not universal inputs.
    L=A(data['log_horizon']).log() if data['log_horizon'] is not None else c.rat(data['horizon'])
    fresh=c.analytic(L,c.profile(data['M']),data['N'],c.prime_powers(L,data['log_horizon']),data['log_horizon'])
    b=fresh
    if data['log_horizon'] is None and F(data['horizon'])==F(9,5) and data['N']==128 and data['M']==180:
        assert b['tail_floor']>c.rat('0.69124708426711')
        assert b['smooth_variation']<c.rat('5.482684')
        assert b['profile_remainder']<c.rat('2.477e-40')
        assert b['generator_change_constant']<c.rat('10.298615')
        out['original_1p8_display_bounds']='PASS'
    out['analytic_bounds']={k:c.show(v) for k,v in b.items()}
    for parity in [0,1]:
        ids=list(range(parity,data['N'],2))
        q,e=c.block(mats['Q'],ids),c.block(mats['E_central'],ids)
        diag=relative_diagnostic(q,e)
        diag['parity']=parity
        diag['ratio_to_available_tail']=diag['maximum']/float(c.unpack(data['bounds']['tail_floor']).mid())
        out['relative_coupling'].append(diag)
    m=F(cert['central_coercivity'])
    decay=F(args.decay) if args.decay is not None else m/2
    if not 0<decay<m:
        raise ValueError('Require 0 < decay < central floor')
    change=b['generator_change_constant']
    if args.generator_bound is None:
        rounded=F(1)
        while not change<c.rat(rounded):
            rounded+=1
    else:
        rounded=F(args.generator_bound)
    if not rounded>0 or not change<c.rat(rounded):
        raise ValueError('The chosen generator constant is not a positive strict upper bound')
    if args.shift is None:
        h=F(1,2)
        while m-rounded*h*h/3<decay:
            h/=2
    else:
        h=F(args.shift)
    if not (0<h<=F(1,2) and m-rounded*h*h/3>=decay):
        raise ValueError('The requested shift/decay does not satisfy the continuation inequality')
    out['continuation']={'status':'PASS','central_floor':str(m),'rounded_generator_constant':str(rounded),
        'shift_maximum':str(h),'decay_coefficient':str(decay),
        'norm_bound':'exp(-('+str(decay)+') * omega)',
        'storage_lower_bound':'1-exp(-2 * ('+str(decay)+') * omega)',
        'rational_exponent_margin':str(m-rounded*h*h/3-decay)}
    if args.legacy:
        old=json.loads(Path(args.legacy).read_text());N=old['N'];differences={}
        for newkey,oldkey in [('Q','Q'),('Gram_causal','Gram'),('ReflectedGram_causal','ReflectedGram')]:
            diff=A(0)
            for i in range(N):
                for j in range(N):
                    sign=(-1)**(i+j) if oldkey!='Q' else 1
                    d=(mats[newkey][i,j]-c.rat(old['matrices'][oldkey][i][j])*sign).abs_upper()
                    diff=diff.max(d)
            assert diff<A('1e-45')
            differences[newkey]=c.show(diff)
        out['legacy_comparison']={'status':'PASS','source':args.legacy,
            'absolute_differences_upper':differences,
            'scope':'Independent arithmetic implementation agrees with prior 96-mode point entries within 1e-45; legacy entries are diagnostic comparison inputs only.'}
    (folder/'analysis.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
