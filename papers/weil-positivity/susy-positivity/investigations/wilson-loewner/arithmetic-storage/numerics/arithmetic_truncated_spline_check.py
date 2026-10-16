#!/usr/bin/env python3
"""Independent Acb cellwise controls for the exact truncated spline helper.

Prepared for Edward Baker with GPT-6 (Codex), 29 September 2026.
Serving variant and configured effort not exposed. No repository paths used.
"""
import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from flint import arb, acb, ctx
import arithmetic_truncated_spline as helper_module
from arithmetic_truncated_spline import TruncatedCorrelation


def require(ok, message):
    if not ok:
        raise ArithmeticError(message)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def overlap(a, b):
    alo,ahi = Fraction(str(a.lower().fmpq())),Fraction(str(a.upper().fmpq()))
    blo,bhi = Fraction(str(b.lower().fmpq())),Fraction(str(b.upper().fmpq()))
    return max(alo,blo)<=min(ahi,bhi)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--bits', type=int, default=512)
    args = parser.parse_args()
    require(args.bits>=256, 'At least 256 bits required')
    ctx.prec = args.bits
    coefficients = [3,-2,5,7,-11,13,-1,9,2]
    N,scale = 5,3
    h = arb(2).log()/N
    helper = TruncatedCorrelation(coefficients,h,N,scale)

    def direct_integral(lam, end):
        q = lam*h
        total = acb(0)
        for j in range(end):
            def value(s, analytic):
                z = s*0
                for m in range(j-1,j+3):
                    if abs(m)>=len(coefficients):
                        continue
                    v = s-m
                    midpoint = Fraction(2*j+1,2)-m
                    sign = 1 if midpoint>0 else -1
                    if abs(midpoint)<1:
                        beta = acb(2)/3-v*v+sign*v*v*v/2
                    else:
                        beta = (2-sign*v)**3/6
                    z += coefficients[abs(m)]*beta
                return z*(q*s).exp()
            piece = acb.integral(value,j,j+1,abs_tol=arb(2)**-180,
                                 rel_tol=arb(2)**-180,eval_limit=100000)
            require(piece.is_finite() and piece.imag.contains(0), 'Acb cell integration failure')
            total += piece
        return h*h/scale**2*total.real

    rows = []
    for exponent in ['0','0.5','-0.5','239.5','-239.5','0.00001','-0.00001']:
        lam = arb(exponent)
        full,before = helper.evaluate(lam)
        actual_before = direct_integral(lam,N)
        actual_full = direct_integral(lam,len(coefficients)+1)
        row = {'lambda':exponent, 'before_overlap':overlap(before,actual_before),
               'full_overlap':overlap(full,actual_full),
               'before_display':before.str(16), 'full_display':full.str(16)}
        require(row['before_overlap'] and row['full_overlap'], 'Independent integral mismatch: '+exponent)
        rows.append(row)
    result = {'status':'PASS', 'date':'2026-09-29', 'model':'GPT-6 (Codex)',
              'serving_variant':'not exposed', 'reasoning_effort':'not exposed',
              'scope':'Independent Acb piecewise polynomial integration checks; not a source interpolation proof',
              'bits':args.bits, 'module_sha256':digest(Path(helper_module.__file__)),
              'script_sha256':digest(Path(__file__)),
              'coefficients':coefficients, 'N':N, 'scale':scale,
              'spacing':'log(2)/5', 'rows':rows}
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'PASS', 'exponents':len(rows),
                      'before_checks':sum(r['before_overlap'] for r in rows),
                      'full_checks':sum(r['full_overlap'] for r in rows)}))


if __name__ == '__main__':
    main()
