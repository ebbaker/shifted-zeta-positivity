#!/usr/bin/env python3
"""Independent numerical checks of the EMA anchor's analytic reduction.

The certificate itself needs only the standard library. These diagnostics use
NumPy to integrate causal responses directly; they do not establish positivity.
"""
import argparse
from fractions import Fraction as F
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import numpy as np


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--certificate-source', type=Path,
                    default=Path(__file__).with_name('certify_ema_original_anchor.py'))
    ap.add_argument('--output', type=Path, required=True)
    args = ap.parse_args()
    spec = importlib.util.spec_from_file_location('anchor', args.certificate_source)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    I = module.I
    checks = 0
    values = [F(-7, 3), F(-1, 7), F(0), F(2, 9), F(13, 5)]
    for x in values:
        for y in values:
            for got, expected in [(I(x)+I(y), x+y), (I(x)-I(y), x-y), (I(x)*I(y), x*y)]:
                assert got.lower() <= expected <= got.upper()
                checks += 1
            if y:
                got = I(x)/I(y)
                assert got.lower() <= x/y <= got.upper()
                checks += 1
    for x in [F(0), F(2), F(7, 11)]:
        q = I(x).sqrt()
        assert q.lower()**2 <= x <= q.upper()**2
        checks += 1
    # Non-point operands: verify every corner using exact Fraction arithmetic.
    for aa, bb in [((F(-3), F(2)), (F(1, 3), F(5))),
                   ((F(-7), F(-2)), (F(-3), F(-1, 5)))]:
        a = I.raw(I(aa[0]).lo, I(aa[1]).hi)
        b = I.raw(I(bb[0]).lo, I(bb[1]).hi)
        for op, fn in [(a+b, lambda x,y: x+y), (a-b, lambda x,y: x-y),
                       (a*b, lambda x,y: x*y), (a/b, lambda x,y: x/y)]:
            for x in aa:
                for y in bb:
                    assert op.lower() <= fn(x,y) <= op.upper()
                    checks += 1
    L, M, N = .5, 32, 16
    w0 = -.5772156649015329-math.pi/2-3*math.log(2)-math.log(math.pi)
    j = np.arange(N)
    k = j*math.pi/L
    phi = np.full(N, math.sqrt(2/L)); phi[0] = 1/math.sqrt(L)
    a = 2*np.arange(M)+.5
    den = a[:,None]**2+k[None,:]**2
    diag = w0+np.sum((2/a)[:,None]*k[None,:]**2/den, axis=0)
    v = phi[None,:]/den
    matrix = np.diag(diag)
    for parity in (0,1):
        vv = v*(j % 2 == parity)[None,:]
        coef = 2*a*a*(1-(-1)**parity*np.exp(-a*L))
        matrix += vv.T@(coef[:,None]*vv)
    b = .5
    c = 2*b*math.sinh(b*L/2)*phi/(b*b+k*k)*(j % 2 == 0)
    s = -2*b*math.cosh(b*L/2)*phi/(b*b+k*k)*(j % 2 == 1)
    matrix += 2*np.outer(c,c)-2*np.outer(s,s)
    errors = []
    for order in (96, 160):
        z, wz = np.polynomial.legendre.leggauss(order)
        x, weight = L*(z+1)/2, L*wz/2
        sn, cs = np.sin(x[:,None]*k), np.cos(x[:,None]*k)
        f = phi*cs
        def resolvent(rate):
            return phi*(rate*cs+k*sn-rate*np.exp(-rate*x[:,None]))/(rate*rate+k*k)
        response = w0*f
        for rate in a:
            response += (2/rate)*(f-rate*resolvent(rate))
        response += 2*(resolvent(b)+resolvent(-b))
        direct = f.T@(weight[:,None]*response)
        direct = (direct+direct.T)/2
        errors.append(float(np.max(np.abs(direct-matrix))))
    assert max(errors) < 2e-11
    # LDL must refuse an explicit negative direction, even with positive diagonal.
    rejected = False
    try:
        module.ldl_positive([[I(1), I(2)], [I(2), I(1)]])
    except AssertionError:
        rejected = True
    assert rejected
    record = {'date': '2026-09-20', 'model': 'OpenAI GPT-6 (Codex)',
              'reasoning_effort': 'Not exposed in this session',
              'scope': 'Independent direct-response quadrature and interval-arithmetic controls; diagnostics, not a positivity certificate',
              'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'certificate_source_sha256': hashlib.sha256(args.certificate_source.read_bytes()).hexdigest(),
              'exact_fraction_arithmetic_cases': checks,
              'direct_response_matrix_max_errors': errors,
              'indefinite_matrix_rejected': rejected, 'checks_pass': True}
    args.output.write_text(json.dumps(record, indent=2, sort_keys=True)+'\n')
    print(json.dumps(record, indent=2, sort_keys=True))


if __name__ == '__main__':
    if not __debug__:
        raise SystemExit('Verification requires assertions; do not use python -O.')
    main()
