#!/usr/bin/env python3
"""Recheck saved balls, derive continuation, and diagnose relative coupling.

All asserted continuation inequalities use Arb/exact rational arithmetic.
The final eigenvalues after high-precision congruence are diagnostics only.
"""
from pathlib import Path
import argparse, gzip, json
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
    ap.add_argument('--shift',default='3e-14')
    ap.add_argument('--decay',default='5e-27')
    args=ap.parse_args();folder=Path(args.folder)
    with gzip.open(folder/'central_matrices.json.gz','rt') as f:data=json.load(f)
    ctx.prec=data['precision_bits']
    cert=json.loads((folder/'central_certificate.json').read_text())
    mats={k:AM([[c.unpack(x) for x in row] for row in mat]) for k,mat in data['matrices'].items()}
    out={'relative_coupling':[]}
    b={k:c.unpack(v) for k,v in data['bounds'].items()}
    # Outward rational bounds displayed in the research report.
    assert b['tail_floor']>c.rat('0.69124708426711')
    assert b['smooth_variation']<c.rat('5.482684')
    assert b['profile_remainder']<c.rat('2.477e-40')
    assert b['generator_change_constant']<c.rat('10.298615')
    a,eta,m=b['tail_floor'].lower(),b['profile_remainder'].upper(),c.rat(cert['central_coercivity'])
    assert ((a-m).abs_upper()+40000)*eta+2*eta**2<c.rat('9.908e-36')
    out['displayed_outward_bounds']='PASS'
    for parity in [0,1]:
        ids=list(range(parity,data['N'],2))
        q,e=c.block(mats['Q'],ids),c.block(mats['E_central'],ids)
        diag=relative_diagnostic(q,e)
        diag['parity']=parity
        diag['ratio_to_available_tail']=diag['maximum']/float(c.unpack(data['bounds']['tail_floor']).mid())
        out['relative_coupling'].append(diag)
    if cert['status']=='PASS':
        m,h,decay=F(cert['central_coercivity']),F(args.shift),F(args.decay)
        change=c.unpack(data['bounds']['generator_change_constant'])
        assert change<11 and m-F(11)*h*h/3>=decay>0 and h<=F(1,2)
        out['continuation']={'status':'PASS','central_floor':str(m),'rounded_generator_constant':11,
            'shift_maximum':args.shift,'decay_coefficient':args.decay,
            'norm_bound':'exp(-'+args.decay+' * omega)',
            'storage_lower_bound':'1-exp(-2 * '+args.decay+' * omega)',
            'rational_exponent_margin':str(m-F(11)*h*h/3-decay)}
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
