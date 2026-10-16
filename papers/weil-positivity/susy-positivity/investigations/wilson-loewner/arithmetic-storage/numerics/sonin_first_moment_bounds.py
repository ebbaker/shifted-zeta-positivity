#!/usr/bin/env python3
"""Combine actual compressed-moment enclosures into positive-measure bounds.

Prepared for Edward Baker with GPT-6 (Codex), 2026-09-29.
Exact serving variant/reasoning effort not exposed. All numerical decisions
use outward Arb arithmetic. One moment does not determine the residual sign.
"""
import argparse
import hashlib
import json
from pathlib import Path
from fractions import Fraction
from flint import arb,ctx


def require(ok,message):
    if not ok:raise ArithmeticError(message)


def rational(s):
    q=Fraction(s)
    return arb(q.numerator)/q.denominator


def unpack(x):
    lo=rational(x['rational_lower'])
    hi=rational(x['rational_upper'])
    require(lo<=hi,'Inverted recorded endpoints')
    return arb((lo+hi)/2,((hi-lo)/2).abs_upper())


def interval(lo,hi):
    lo,hi=lo.lower(),hi.upper()
    require(lo<=hi,'Empty enclosure intersection')
    return arb((lo+hi)/2,((hi-lo)/2).abs_upper())


def pack(v):
    require(v.is_finite(),'Nonfinite result')
    return {'display':v.str(25),'rational_lower':str(v.lower().fmpq()),
            'rational_upper':str(v.upper().fmpq())}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(args):
    ctx.prec=256
    paths=[args.h2,args.correction,args.prime,args.numerics/'records/sonin_scalar_summary.json']
    second,corr,prime,scalar=[json.loads(p.read_text()) for p in paths]
    require(second['status']==corr['status']=='CERTIFIED','An input is not certified')
    require(prime['status']=='CERTIFIED_WITH_INHERITED_SOURCE_AND_GAMMA_RECORDS','Uncertified arithmetic control')
    require(second['script_sha256']==digest(args.new_numerics/'sonin_second_transport_scalar.py'),'Second scalar generator mismatch')
    require(prime['script_sha256']==digest(args.new_numerics/'arithmetic_prime_diagnostic.py'),'Prime generator mismatch')
    for name,sha in prime['input_sha256'].items():
        require(sha==digest(args.numerics/'records'/name),'Prime input mismatch: '+name)
    require(scalar['script_sha256']==digest(args.numerics/'sonin_scalar_summary.py'),'Scalar generator mismatch')
    for name,sha in scalar['input_sha256'].items():
        require(sha==digest(args.numerics/'records'/name),'Scalar input mismatch: '+name)
    for name,sha in second['dependency_sha256'].items():
        require(sha==digest(args.numerics/name),'Second scalar dependency mismatch: '+name)
    # The correction producer names every local and inherited dependency.
    for name,sha in corr['dependency_sha256'].items():
        base=args.numerics if name.startswith('inherited:') else args.new_numerics
        relative=name.split(':',1)[1] if ':' in name else name
        require(sha==digest(base/relative),'Correction dependency mismatch: '+name)
    require(corr['script_sha256']==digest(args.new_numerics/corr['generator']),'Correction generator mismatch')
    r=1/arb(2).sqrt()
    m=(1-r)*(1-r)
    M=(1+r)*(1+r)
    rows=[]
    for sid in range(2):
        s=second['sources'][sid];c=corr['sources'][sid]
        p=prime['sources'][sid];b=scalar['sources'][sid]
        require(all(x['source']==sid for x in [s,c,p,b]),'Source order mismatch')
        h0=unpack(b['h0_B_infinity_D2F'])
        require(h0>0,'Positive source mass unresolved')
        h2=unpack(s['h2_B_infinity_D2_squared_F'])
        correction=unpack(c['compact_correction'])
        rawmoment=h2-correction
        moment=interval(rawmoment.lower().max((m*h0).lower()),rawmoment.upper().min((M*h0).upper()))
        require(moment>0,'Positive actual moment unresolved')
        jensen=h0.lower()*h0.lower()/moment.upper()
        secant=((m+M)*h0.upper()-moment.lower())/(m*M)
        prior=unpack(b['B2_coercivity_and_residual_enclosure'])
        b2=interval(prior.lower().max(jensen.lower()),prior.upper().min(secant.upper()))
        q=unpack(p['direct_Q1'])
        residual=q-b2
        exact_mass_mean_J=h0*h0/moment
        exact_mass_mean_U=((m+M)*h0-moment)/(m*M)
        mass_mean_sign_insufficient=bool(exact_mass_mean_J.upper()<q.lower()
                                         and exact_mass_mean_U.lower()>q.upper())
        rows.append({'source':sid,'h0':pack(h0),'h2':pack(h2),
                     'compact_correction':pack(correction),'actual_compressed_first_moment':pack(moment),
                     'Jensen_lower':pack(jensen),'secant_upper':pack(secant),
                     'previous_B2':pack(prior),'B2_first_moment_enclosure':pack(b2),
                     'direct_Q1':pack(q),'complete_arithmetic_residual_enclosure':pack(residual),
                     'mass_mean_extremal_lower_range':pack(exact_mass_mean_J),
                     'mass_mean_extremal_upper_range':pack(exact_mass_mean_U),
                     'mass_and_first_moment_alone_cannot_decide_residual_sign':mass_mean_sign_insufficient,
                     'residual_contains_zero':bool(residual.contains(0)),
                     'residual_positive':bool(residual>0),'residual_negative':bool(residual<0)})
    return {'status':'CERTIFIED','date':'2026-09-29','model':'GPT-6 (Codex)',
            'serving_variant':'not exposed','reasoning_effort':'not exposed',
            'scope':'First actual compressed moment and source-specific Jensen/secant bounds; no all-source or all-support result.',
            'script_sha256':digest(Path(__file__)),
            'input_sha256':{p.name:digest(p) for p in paths},'sources':rows}


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--numerics',type=Path,default=Path(__file__).resolve().parent)
    p.add_argument('--new-numerics',type=Path,default=Path(__file__).resolve().parent)
    p.add_argument('--h2',type=Path,required=True)
    p.add_argument('--correction',type=Path,required=True)
    p.add_argument('--prime',type=Path,required=True)
    p.add_argument('--output',type=Path,required=True)
    args=p.parse_args()
    result=run(args)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    for row in result['sources']:
        print(json.dumps({'source':row['source'],**{k:row[k]['display'] for k in
          ['actual_compressed_first_moment','B2_first_moment_enclosure','complete_arithmetic_residual_enclosure']}}))
