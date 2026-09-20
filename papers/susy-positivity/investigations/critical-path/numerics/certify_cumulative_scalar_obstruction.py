#!/usr/bin/env python3
"""Exact rational comparisons for the scalar-anchor append obstruction.

The accompanying note proves the kernel, Carleman, and gamma inequalities.
This is NOT a certificate of the actual defect-normalized coupling.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path


def calculate():
    def atan_bounds(q, n=32):
        s=sum(((-1)**j*F(1,(2*j+1)*q**(2*j+1)) for j in range(n)), F(0))
        t=(-1)**n*F(1,(2*n+1)*q**(2*n+1))
        return min(s,s+t),max(s,s+t)
    a,b=atan_bounds(5); c,d=atan_bounds(239)
    assert 16*a-4*d > F(157,50) and 16*b-4*c < F(22,7)
    def exp_partial(x,n):
        term,total=F(1),F(1)
        for j in range(1,n+1):
            term*=F(x,j); total+=term
        return total
    assert exp_partial(10,24)>10000 and exp_partial(2,8)>7
    w, delta = F(1, 1000), F(24999, 500000000)
    eps, T = F(1, 10000), F(50)
    # u<=2 eps: e^(-5u/2)-2u e^(u/2) >= bracket.
    bracket = 1-5*eps-4*eps/(1-eps)
    # u>=2 eps e^-T; log(1/eps)<10; u^w >= 1-w(T+10).
    power_lower = 1-w*(T+10)
    # Unit log-flat Carleman test: expectation >= pi-8/T.
    carleman_lower = F(157, 50)-8/T
    lower = w*power_lower*bracket*carleman_lower
    # Gamma(1+w)>=1-w and (2pi)^w<=1/(1-2w).
    coefficient_upper = w/((1-w)*(1-2*w))
    # |k(u)| <= coefficient_upper * (1/u+2 e^(R/2)), R=11/20.
    # Carleman norm <=pi<22/7 and sqrt(Lh)<4/25.
    upper = coefficient_upper*(F(22, 7)+2*F(40, 29)*F(4, 25))
    assert bracket > 0 and power_lower > 0
    assert lower > 55*delta
    assert upper < 72*delta
    # Both omitted cosine spaces, indices j>=32. Unit log-flat tests have
    # ||P_N f||^2 <= (2N-1)/length * 4 epsilon/T.
    old_projection, new_projection = F(4,125),F(101,1000)
    assert old_projection**2 >= F(63,F(1,2))*4*eps/T
    assert new_projection**2 >= F(63,F(1,20))*4*eps/T
    complement_lower=lower-upper*(old_projection+new_projection)
    assert complement_lower>46*delta
    def record(x):
        return {'exact_rational': str(x), 'decimal_display_only': float(x)}
    return {
        'date': '2026-09-20',
        'model': 'OpenAI GPT-6 (Codex; developer-provided identity)',
        'reasoning_effort': 'Not exposed in this session; not inferred',
        'parameters': {'L': '1/2', 'h': '1/20', 'omega': str(w),
                       'delta': str(delta), 'epsilon': str(eps), 'log_width': str(T)},
        'kernel_bracket_lower': record(bracket),
        'fractional_power_lower': record(power_lower),
        'carleman_test_lower': record(carleman_lower),
        'mixed_operator_norm_lower': record(lower),
        'mixed_operator_norm_upper': record(upper),
        'scalar_route_best_bound_lower': record(lower/delta),
        'scalar_route_best_bound_upper': record(upper/delta),
        'both_cosine_complements_N32_norm_lower': record(complement_lower),
        'both_cosine_complements_N32_div_delta_lower': record(complement_lower/delta),
        'projection_norm_upper': {'old':str(old_projection),'new':str(new_projection)},
        'claims': ['55 < ||Y||/delta < 72',
                   'The scalar-anchor sufficient condition cannot close, even with exact ||Y||'],
        'not_claimed': ['A lower bound above one for the actual normalized coupling',
                        'An all-input certificate of ||C||<1'],
        'certificate_pass': True,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--output', type=Path, required=True)
    args = ap.parse_args()
    out = calculate()
    out['source_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(out, indent=2, sort_keys=True)+'\n')
    print(json.dumps({k: out[k] for k in ('certificate_pass',
          'scalar_route_best_bound_lower', 'scalar_route_best_bound_upper')}, indent=2))


if __name__ == '__main__':
    if not __debug__:
        raise SystemExit('Do not disable certificate assertions with python -O.')
    main()
