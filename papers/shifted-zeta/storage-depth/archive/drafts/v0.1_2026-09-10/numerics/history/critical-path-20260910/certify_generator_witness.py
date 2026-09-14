#!/usr/bin/env python3
"""Ball Rayleigh witness for a negative shifted GENERATOR, not a norm defect.

The generator's gamma profile is G_w(t)=cosh(w*t)G_0(t); on |t|=3
its modulus is <256*cosh(3*|w|). This gives the explicit operator remainder
used below. All sign decisions use Arb and this remainder. mpmath only
proposes a rational test vector. The adopted normalization is the v0.3 one.
"""
import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import platform
import mpmath as mp
import flint
from flint import arb as A, arb_mat as AM, ctx
import explore_path as e

def certify(args):
    if not __debug__:
        raise RuntimeError('Assertions must be enabled')
    ctx.prec, mp.mp.dps = args.bits, args.digits
    c = e.load_source(e.DEFAULT_SOURCE)
    ids = list(range(0,args.n,2))
    Q0 = e.head(c,args.horizon,args.n,args.degree,return_balls=True)
    if args.vector_record:
        prior = json.loads(Path(args.vector_record).read_text())
        assert prior['basis_degrees'] == ids
        coefficients = prior['rational_vector_decimal_coefficients']
    else:
        q0 = mp.matrix([[e.midpoint(Q0[i,j]) for j in ids] for i in ids])
        _,vec = mp.eigsy(q0)
        coefficients = [mp.nstr(vec[i,0],80) for i in range(len(ids))]
    v = AM([[c.rat(Fraction(t))] for t in coefficients])
    q0ball = c.block(Q0,ids)
    Qw = e.head(c,args.horizon,args.n,args.degree,args.shift,return_balls=True)
    qwball = c.block(Qw,ids)
    norm = (v.transpose()*v)[0,0]
    assert norm > 0
    central = (v.transpose()*q0ball*v)[0,0]/norm
    shifted = (v.transpose()*qwball*v)[0,0]/norm
    L,w = A(args.horizon).log(),c.rat(Fraction(args.shift))
    assert 0 < L < 3 and 0 < w <= c.rat(Fraction(1,2))
    assert A(3).sin() > c.rat(Fraction(1,8))
    assert c.rat(Fraction(3,2)).exp() < 5
    assert 5*(24+12) < 256
    eta0 = 256*(L/3)**(args.degree+1)/((args.degree+1)*(1-L/3))
    eta = (3*w).cosh()*eta0
    upper = (shifted+eta.upper()).upper()
    lower = (shifted-eta.upper()).lower()
    assert upper < 0, 'No negative witness certified'
    # The central even vector multiplied by centered x has only odd degrees
    # through n-1, so its full polynomial output is retained without projection.
    full_v = AM(args.n,1)
    for i,j in enumerate(ids):
        full_v[j,0] = v[i,0]
    X = AM(args.n,args.n)
    for j in range(args.n-1):
        X[j,j+1] = X[j+1,j] = L*(j+1)/(2*A((2*j+1)*(2*j+3)).sqrt())
    y = X*full_v
    ynorm = (y.transpose()*y)[0,0]
    xenergy = (y.transpose()*Q0*y)[0,0]
    assert central-eta0.upper() > 0
    assert xenergy-eta0.upper()*ynorm > 0
    ratio_lower = ((xenergy-eta0.upper()*ynorm)/(norm*(central+eta0.upper()))).lower()
    kappa_lower = ratio_lower.sqrt().lower()
    # Exact rounded scalar, not a full-norm upper bound or a safe shift claim.
    rounded_kappa = c.rat('2.32e11')
    kappa_lower_pass = bool(kappa_lower > rounded_kappa) if args.horizon == 7 and args.n == 128 else None
    if kappa_lower_pass is not None:
        assert kappa_lower_pass
    data = {
        'result':'PASS: negative shifted-generator Rayleigh quotient, with analytic infinite-profile remainder',
        'scope':'No assertion about noncontractivity of V, negativity of central Q0, or RH.',
        'normalization':'finite-horizon Weil v0.3 at a566944dc1be2899e37fce3d0e857516ced33d8f',
        'log_horizon':args.horizon,'shift_rational':args.shift,
        'retained_modes':args.n,'profile_degree':args.degree,'precision_bits':args.bits,
        'basis':'sqrt((2n+1)/L) P_n(2x/L-1), even n only',
        'basis_degrees':ids,'rational_vector_decimal_coefficients':coefficients,
        'central_model_rayleigh':central.str(45),
        'central_profile_remainder_upper':eta0.upper().str(45),
        'shifted_model_rayleigh':shifted.str(45),
        'shifted_profile_remainder_upper':eta.upper().str(45),
        'exact_shifted_rayleigh_lower':lower.str(45),
        'exact_shifted_rayleigh_upper':upper.str(45),
        'negative_upper_bound_pass':bool(upper < 0),
        'central_coordinate_energy_ratio_lower':ratio_lower.str(45),
        'central_coordinate_energy_norm_lower':kappa_lower.str(45),
        'kappa_exceeds_2p32e11_pass':kappa_lower_pass,
        'versions':{'python':platform.python_version(),'python_flint':flint.__version__,
                    'flint':flint.__FLINT_VERSION__,'mpmath':mp.__version__},
        'source_sha256':{name:hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest()
                         for name in ['reference_certify_arb.py','explore_path.py','certify_generator_witness.py']}}
    Path(args.output).write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps({k:v for k,v in data.items() if k not in ['basis_degrees','rational_vector_decimal_coefficients','source_sha256']},indent=2),flush=True)

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--horizon',type=int,default=7)
    p.add_argument('--shift',default='1e-11')
    p.add_argument('--n',type=int,default=128)
    p.add_argument('--degree',type=int,default=220)
    p.add_argument('--bits',type=int,default=1792)
    p.add_argument('--digits',type=int,default=100)
    p.add_argument('--output',required=True)
    p.add_argument('--vector-record',help='Replay using the exact rational vector in a prior result')
    certify(p.parse_args())
