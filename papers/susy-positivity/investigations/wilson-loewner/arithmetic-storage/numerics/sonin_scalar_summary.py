#!/usr/bin/env python3
"""Combine certified scalar components and update fixed-space trace diagnostics.

Prepared for Edward Baker with GPT-6 (Codex), 29 September 2026.
Serving variant and reasoning effort are not exposed. Uses python-flint.
"""
import argparse, hashlib, json
from pathlib import Path
from fractions import Fraction
from flint import arb, ctx


def require(condition,message):
    if not condition:raise ArithmeticError(message)


def rational(s):
    q=Fraction(s);return arb(q.numerator)/q.denominator


def unpack(item):
    if 'rational_lower' in item:
        lo,hi=rational(item['rational_lower']),rational(item['rational_upper'])
    elif 'lower' in item:
        lo,hi=rational(item['lower']),rational(item['upper'])
    else:
        m,r=item['ball'];return arb((int(m[0]),m[1]),(int(r[0]),r[1]))
    return arb((lo+hi)/2,((hi-lo)/2).abs_upper())


def interval(lo,hi):
    lo,hi=lo.lower(),hi.upper()
    require(lo<=hi,'Empty interval intersection')
    return arb((lo+hi)/2,((hi-lo)/2).abs_upper())


def pack(v):
    return {'display':v.str(24),'rational_lower':str(v.lower().fmpq()),
            'rational_upper':str(v.upper().fmpq())}


def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()


def run(directory,previous):
    ctx.prec=256
    paths=[directory/'records'/n for n in ('gamma_scalar_certificate.json','sonin_scalar_epsilon.json')]
    gamma,epsilon=[json.loads(p.read_text()) for p in paths]
    trialpath=previous/'records/sonin_trial_enclosure.json'
    trial=json.loads(trialpath.read_text())
    require(gamma['status']==epsilon['status']=='CERTIFIED','Uncertified scalar component')
    require(gamma['script_sha256']==digest(directory/'gamma_scalar_certificate.py'),'Gamma script hash mismatch')
    for name,sha in epsilon['script_hashes'].items():
        parent=directory if name=='sonin_scalar_epsilon.py' else previous
        require(sha==digest(parent/name),'Epsilon dependency hash mismatch: '+name)
    require(gamma['source_script_sha256']==digest(previous/'source_norm_enclosures.py'),'Gamma source mismatch')
    sourcehash=digest(previous/'records/source_norm_enclosures.json')
    require(sourcehash==gamma['source_record_sha256']==epsilon['source_record_sha256']==trial['source_record_sha256'],'Source record mismatch')
    for name,sha in trial['script_hashes'].items():
        require(sha==digest(previous/name),'Trial dependency hash mismatch: '+name)
    r=1/arb(2).sqrt();ell2=(1-r)**2;upper=(1+r)**2
    rows=[]
    for sid in range(2):
        grow={x['kernel']:unpack(x['gamma']) for x in gamma['results'] if x['source']==sid}
        erow=epsilon['sources'][sid];trow=trial['sources'][sid]
        require(erow['source']==trow['source']==sid,'Source order mismatch')
        bf=grow['F']+unpack(erow['E_F'])
        h0=grow['D2F']+unpack(erow['E_D2F'])
        require(bf>0 and h0>0,'Positive trace sign not resolved')
        require(2*bf.rad()<rational('1e-5') and 2*h0.rad()<rational('1e-5'),'Scalar accuracy target unmet')
        bn=unpack(trow['B_N'])
        residual=h0+unpack(trow['finite_residual_correction'])
        require(residual>0,'Fixed-space residual lower bound not positive')
        omitted=interval((residual/upper).lower(),(residual/ell2).upper())
        b2_from_residual=bn+omitted
        b2_from_h0=interval((h0/upper).lower(),(h0/ell2).upper())
        b2=interval(b2_from_residual.lower().max(b2_from_h0.lower()),
                    b2_from_residual.upper().min(b2_from_h0.upper()))
        require(b2>bn,'Fixed-space trace separation unresolved')
        rows.append({'source':sid,'Gamma_F':pack(grow['F']),'Gamma_D2F':pack(grow['D2F']),
                     'E_F':erow['E_F'],'E_D2F':erow['E_D2F'],
                     'B_infinity_F':pack(bf),'h0_B_infinity_D2F':pack(h0),
                     'previous_B_N':trow['B_N'],
                     'fixed_space_HS_residual_squared':pack(residual),
                     'fixed_space_missed_positive_trace':pack(omitted),
                     'B2_coercivity_and_residual_enclosure':pack(b2),
                     'fixed_space_captured_fraction_upper':pack(bn.upper()/b2.lower())})
    return {'status':'CERTIFIED','date':'2026-09-29','model':'GPT-6 (Codex)',
            'serving_variant':'not exposed','reasoning_effort':'not exposed',
            'scope':'Accurate real-place smoothed traces; first-prime trace only bounded, not evaluated. No complete arithmetic residual sign.',
            'script_sha256':digest(Path(__file__)),
            'input_sha256':{p.name:digest(p) for p in paths+[trialpath]},
            'sources':rows}


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--numerics',type=Path,default=Path(__file__).resolve().parent)
    p.add_argument('--previous-numerics',type=Path)
    p.add_argument('--output',type=Path)
    a=p.parse_args()
    result=run(a.numerics,a.previous_numerics or a.numerics)
    (a.output or a.numerics/'records/sonin_scalar_summary.json').write_text(json.dumps(result,indent=2)+'\n')
    for row in result['sources']:
        print(json.dumps({'source':row['source'],**{k:row[k]['display'] for k in
            ('B_infinity_F','h0_B_infinity_D2F','fixed_space_HS_residual_squared',
             'fixed_space_missed_positive_trace','B2_coercivity_and_residual_enclosure','fixed_space_captured_fraction_upper')}}))
