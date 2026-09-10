"""Recheck delivered archives, all common entries, and independent Schur tests."""
import gzip
import hashlib
import json
from pathlib import Path
from flint import arb, arb_mat, ctx
import certify_arb as c
import independent_arb as ind

def check_pair(original, independent):
    left=c.locate(original/'central_matrices.json.gz')
    right=c.locate(independent/'independent_matrices.json.gz')
    data=json.load(gzip.open(left,'rt'))
    other=json.load(gzip.open(right,'rt'))
    cert=json.loads((original/'central_certificate.json').read_text())
    icert=json.loads((independent/'certificate.json').read_text())
    if hashlib.sha256(left.read_bytes()).hexdigest()!=cert['matrix_archive_sha256']:
        raise ValueError('Original hash mismatch')
    if hashlib.sha256(right.read_bytes()).hexdigest()!=icert['matrix_sha256']:
        raise ValueError('Independent hash mismatch')
    ctx.prec=max(data['precision_bits'],other['parameters']['bits'])
    if data['N']!=other['parameters']['N'] or data['M']!=other['parameters']['M']:
        raise ValueError('Model-size mismatch')
    if data['log_horizon']!=other['parameters']['log_horizon']:
        raise ValueError('Horizon mismatch')
    if data['log_horizon'] is None and not c.rat(data['horizon']).overlaps(c.rat(other['parameters']['horizon'])):
        raise ValueError('Rational horizon mismatch')
    if not c.rat(cert['central_coercivity']).overlaps(c.rat(other['parameters']['floor'])):
        raise ValueError('Target-floor mismatch')
    if c.validate(data,cert['central_coercivity'])['status']!='PASS':
        raise ValueError('Original replay failed')
    N=data['N'];result={'original_sha256':hashlib.sha256(left.read_bytes()).hexdigest(),
                       'independent_sha256':hashlib.sha256(right.read_bytes()).hexdigest()}
    for a,b in [('Q','q'),('Gram_causal','F'),('ReflectedGram_causal','C')]:
        maximum=arb(0);count=0
        for i in range(N):
            for j in range(N):
                x=c.unpack(data['matrices'][a][i][j]);y=ind.decode(other['matrices'][b][i][j])
                if not x.overlaps(y):raise ArithmeticError(f'Disjoint {a}[{i},{j}]')
                count+=1;maximum=max(maximum,(x-y).abs_upper())
        result[a]={'overlapping_entries':count,'total':N*N,'difference_upper':maximum.str(35)}
    mats={name:arb_mat([[ind.decode(x) for x in row] for row in values])
          for name,values in other['matrices'].items()}
    par=other['parameters']
    L=arb(par['log_horizon']).log() if par['log_horizon'] is not None else arb(par['horizon'])
    indices=[(n,ind.prime_base(n)) for n in range(2,30)
             if ind.prime_base(n) and ind.active(n,L,par['log_horizon'])]
    bounds=ind.bounds(L,N,par['M'],ind.profile(par['M']),indices,par['log_horizon'])
    a=bounds['a'].lower();eta=bounds['eta'].upper();m=arb(par['floor'])
    if not a>m>0:raise ValueError('Invalid independent target')
    if not sum(mats['F'][i,i] for i in range(N))<10**7:raise ValueError('Gram trace')
    eps=((abs(a-m)+40000)*eta+2*eta**2).upper()
    for r,label in [(1,'even'),(-1,'odd')]:
        ids=list(range(0 if r==1 else 1,N,2))
        q,F,C=(ind.block(mats[name],ids) for name in ['q','F','C'])
        E=(F+r*C)/2-q*q
        eye=c.ident(len(ids))
        test=ind.sym((a-m)*(q-m*eye)-E-eps*eye)
        saved=arb_mat([[ind.decode(x) for x in row] for row in other['tests'][label]])
        if not test.overlaps(saved):raise ValueError('Independent Schur reconstruction mismatch')
        if not ind.ldl(test)['passed'] or not ind.ldl(saved)['passed']:
            raise ValueError('Independent replay failed')
        result['independent_replay_'+label]=True
    return result

PAIRS=[('log2','log2_N128','independent_log2'),('log3','log3_N128','independent_log3'),
       ('log4','log4_N128','independent_log4'),('log5','log5_N128','independent_log5'),
       ('log6','log6_N128','independent_log6'),('1p8','length_1p8_N128','independent_1p8'),
       ('log7','log7_N128','independent_log7')]

if __name__=='__main__':
    root=Path(__file__).resolve().parent
    for label,original,independent in PAIRS:
        try:
            c.locate(root/'output'/independent/'independent_matrices.json.gz')
            c.locate(root/'output'/original/'central_matrices.json.gz')
        except FileNotFoundError as err:
            print(label,'SKIPPED:',str(err).split('.')[0])
            continue
        result=check_pair(root/'output'/original,root/'output'/independent)
        (root/'review'/('crosscheck_'+label+'.json')).write_text(json.dumps(result,indent=2)+'\n')
        print(label,'PASS',json.dumps(result)[:160])
