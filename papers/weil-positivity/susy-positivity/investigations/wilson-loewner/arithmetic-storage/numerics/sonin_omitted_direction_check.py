#!/usr/bin/env python3
"""Check the omitted actual-Sonin direction against two generated trial records.

Prepared for Edward Baker, 2026-09-29, with GPT-6 (Codex) assistance.
Serving variant and reasoning effort are not exposed. Hashes bind provenance;
replaying the generating programs, not a hash alone, verifies their arithmetic.
"""
import argparse
import hashlib
import json
from pathlib import Path
from flint import arb,ctx
import prolate_certificate as prolate
import source_norm_enclosures as source


def require(value,message):
    if not value:raise ArithmeticError(message)


def unpack(x):
    d=x['ball']
    return arb((int(d[0][0]),d[0][1]),(int(d[1][0]),d[1][1]))


def bound(x):
    return {'lower_exact':str(x.lower().fmpq()),'upper_exact':str(x.upper().fmpq()),
            'display':x.str(24)}


def check(directory):
    ctx.prec=256
    files=['sonin_trial_enclosure.json','sonin_omitted_direction.json','source_norm_enclosures.json']
    base,larger,src=[json.loads((directory/'records'/p).read_text()) for p in files]
    for rec in (base,larger):
        for name,digest in rec['script_hashes'].items():
            require(hashlib.sha256((directory/name).read_bytes()).hexdigest()==digest,
                    'Generator changed; regenerate '+name)
        require(rec['source_record_sha256']==hashlib.sha256((directory/'records'/files[2]).read_bytes()).hexdigest(),
                'Source record changed')
    require(base['seed_degrees']==[20,24] and larger['seed_degrees']==[20,24,21],
            'Expected the specified nested trial spaces')
    for key in ('N','precision_bits','smooth_cutoff_width','dyadic_coefficient_bits','gamma_exact'):
        require(base[key]==larger[key],'Mismatched experiment parameter '+key)
    pc,_,_=prolate.certify(rank=32,precision_bits=256)
    tau=unpack(pc['bounds']['cosine_trace_norm_bound'])
    ell2=(1-1/arb(2).sqrt())*(1-1/arb(2).sqrt())
    checks=[]
    for j,(small,large,source_row) in enumerate(zip(base['sources'],larger['sources'],src['sources'])):
        require(small['source']==large['source']==source_row['source']==j,'Source mismatch')
        difference=unpack(large['B_N'])-unpack(small['B_N'])
        floor=arb('0.00373' if j==0 else '0.00712')
        require(difference>floor,'Omitted direction was not resolved')
        source_l1=source.record_ball(source_row['normalized_L1'])
        Binfupper=source.record_ball(source_row['gamma_upper_bound_F'])+tau*source_l1*source_l1
        require(Binfupper<arb('4.2'),'Expected fixed-source upper cap failed')
        relative_floor=difference/Binfupper
        require(relative_floor>arb('0.0009' if j==0 else '0.0017'),
                'Relative accuracy obstruction failed')
        checks.append({'source':j,'B_N':bound(unpack(small['B_N'])),
                       'B_augmented':bound(unpack(large['B_N'])),
                       'B_augmented_minus_B_N':bound(difference),
                       'full_trace_error_lower_strict':('373/100000' if j==0 else '89/12500'),
                       'full_HS_residual_squared_lower':bound(ell2*difference),
                       'B_infinity_upper_majorant':bound(Binfupper),
                       'trace_error_relative_to_B_infinity_lower':bound(relative_floor)})
    return {'date':'2026-09-29','model':'GPT-6 (Codex)','serving_variant':'not exposed',
            'reasoning_effort':'not exposed','status':'CERTIFIED_SCOPED_ACCURACY_OBSTRUCTION',
            'scope':'The actual-Sonin trial space with seed degrees20,24 misses the stated positive trace amounts. This does not give an arithmetic residual sign or exclude other trial spaces or trace methods.',
            'proof':'Nested Galerkin monotonicity: B_S-B_N >= B_augmented-B_N. Also ||R_N||_HS^2 >= ell_2^2 (B_S-B_N).',
            'input_hashes':{name:hashlib.sha256((directory/'records'/name).read_bytes()).hexdigest() for name in files},
            'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'checks':checks}


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--directory',type=Path,default=Path(__file__).resolve().parent)
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    result=check(args.directory)
    target=args.output or args.directory/'records'/'sonin_omitted_direction_check.json'
    target.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':result['status'],'checks':result['checks']},indent=2))
