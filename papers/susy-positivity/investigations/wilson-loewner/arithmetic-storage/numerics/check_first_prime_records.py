#!/usr/bin/env python3
"""Check nested certificates, source bindings, and a conditional shift bound."""
import argparse
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--records',type=Path,default=Path(__file__).with_name('records'))
    ap.add_argument('--output',type=Path,required=True)
    args=ap.parse_args()
    names=['first-prime-inputs-40digits-20260924.json','first-prime-inputs-60digits-20260924.json',
           'first-prime-coupling-diagnostics-20260924.json']
    paths=[args.records/name for name in names]
    a,b,d=[json.loads(p.read_text()) for p in paths]
    cert=Path(__file__).with_name('certify_first_prime_inputs.py')
    diag=Path(__file__).with_name('diagnose_first_prime_coupling.py')
    assert a['certificate_pass'] and b['certificate_pass'] and d['check_pass']
    assert a['source_sha256']==b['source_sha256']==hashlib.sha256(cert.read_bytes()).hexdigest()
    assert d['source_sha256']==hashlib.sha256(diag.read_bytes()).hexdigest()
    assert d['certificate_sha256']==hashlib.sha256(paths[0].read_bytes()).hexdigest()
    count=0
    def check(x,y):
        nonlocal count
        if isinstance(x,dict):
            if 'lower' in x and 'upper' in x:
                assert F(x['lower'])<=F(y['lower'])<=F(y['upper'])<=F(x['upper'])
                count+=1
            else:
                for k,v in x.items():check(v,y[k])
        elif isinstance(x,list):
            assert len(x)==len(y)
            for v,w in zip(x,y):check(v,w)
    check(a['checks'],b['checks'])
    c=a['checks']
    assert F(c['old']['uniform_shift_perturbation_upper']['upper'])<F(15,10**8)
    assert F(c['new']['uniform_shift_perturbation_upper']['upper'])<F(13,10**9)
    assert F(c['complete_mixed_shift_perturbation_upper']['upper'])<F(7,10**7)
    assert F(812,10000)**2<F(3,200)*F(11,25)
    bound=(F(999,1000)+F(7,10**7)/F(812,10000))/(1-F(1,100000)-F(3,10**8))
    assert bound<F(49951,50000)
    out={'date':'2026-09-24','model':'GPT-6 (Codex; developer-provided identity)',
        'reasoning_effort':'Not exposed; not inferred','nested_interval_records':count,
        'floating_reduction_controls':len(d['reduction_controls']),
        'conditional_shift_transfer':{'UNPROVED_HYPOTHESIS':'Complete all-input central relative coupling <= 999/1000',
            'upper_under_hypothesis':str(bound),'outward_conclusion':'49951/50000',
            'hypothesis_certified':False},'check_pass':True,
        'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'records_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps(out,indent=2,sort_keys=True))


if __name__=='__main__':
    if not __debug__:raise SystemExit('Do not disable assertions with python -O.')
    main()
