#!/usr/bin/env python3
"""Check constants and finite identities for the positive arithmetic packets.

Prepared for Edward Baker, 18 October 2026, with substantial LLM assistance.
Recorded model gpt-6-astra (Codex), effort max. Requires python-flint.
The all-height inequalities are proved analytically in Note 04. This script
certifies their numerical constants and checks finite integration identities;
it does not infer a universal sign from samples or certify a theta collision.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import math
import platform
import resource
import signal
import time
from pathlib import Path
import flint
from flint import acb, arb, ctx

BITS = 384
MAX_SECONDS = 60


def bs(x):
    return x.str(65, more=True)


def maximum(a, b):
    assert not (a-b).contains(0), 'Comparison not separated at this precision'
    return a if a > b else b


def budgets(m, kappa):
    a = arb.pi()*m*m
    r4 = (arb(m+1)/m)**4*(-arb.pi()*(2*m+1)).exp()
    r6 = (arb(m+1)/m)**6*(-arb.pi()*(2*m+1)).exp()
    assert r4 < 1 and r6 < 1 and 8*a > arb(1)/2
    s0 = 2*a*a*(-a).exp()/(1-r4)
    q0 = 8*a**3*(-a).exp()/(1-r6)
    eps = [s0*math.factorial(j)/(4*a-9)**(j+1) for j in range(3)]
    rho = (4096*eps[0]+2*q0)/kappa
    eta1 = maximum(8192*eps[1], q0/8+2*s0)/kappa
    eta2 = maximum(8192*eps[2], 3*q0/512+s0/8+4*eps[0])/kappa
    return {'m': m, 'S': s0, 'Q': q0, 'eps': eps,
            'rho': rho, 'eta1': eta1, 'eta2': eta2}


def q_endpoint(n):
    a = arb.pi()*n*n
    return (8*a**3-30*a*a+15*a)*(-a).exp()


def source_jet(u, n, t):
    a = arb.pi()*n*n*(4*u).exp()
    p0 = 2*a*a-3*a
    p1 = -8*a**3+30*a*a-15*a
    p2 = 32*a**4-224*a**3+330*a*a-75*a
    pref = (t*u*u+u-a).exp()
    return (pref*p0, pref*(2*t*u*p0+p1),
            pref*((4*t*t*u*u+2*t)*p0+4*t*u*p1+p2))


def integrate(f, upper):
    out = acb.integral(f, 0, upper, rel_tol=arb('1e-95'),
                       abs_tol=arb('1e-105'), eval_limit=100000, depth_limit=30)
    assert out.is_finite()
    return out


def finite_boundary_checks():
    rows = []
    upper = arb(1)/8
    for n in (2, 5):
        for t in (arb(0), arb(1)/2):
            for x in (arb(32), arb(128)):
                direct = integrate(lambda u, analytic:
                    source_jet(u,n,t)[0]*(x*u).cos(), upper)
                positive = integrate(lambda u, analytic:
                    source_jet(u,n,t)[2]*(1-(x*u).cos())/x**2, upper)
                gu, gpu, _ = source_jet(acb(upper),n,t)
                boundary = gpu*((x*upper).cos()-1)/x**2+gu*(x*upper).sin()/x
                residual = direct-positive-boundary
                assert residual.real.contains(0) and residual.imag.contains(0)
                assert abs(residual) < arb('1e-90')
                assert positive.real > 0
                # This intentionally incorrect formula omits the upper boundary.
                omitted = direct-positive
                assert not omitted.real.contains(0)
                rows.append({'n': n, 't': bs(t), 'x': bs(x), 'upper': bs(upper),
                    'direct_finite_integral': bs(direct.real),
                    'positive_finite_integral': bs(positive.real),
                    'upper_boundary': bs(boundary.real),
                    'identity_residual': bs(residual.real),
                    'omitted_boundary_rejected': True})
    return rows


def main(output):
    started = time.monotonic()
    ctx.prec = BITS
    def timeout(signum, frame):
        raise TimeoutError('60-second bounded check exceeded')
    signal.signal(signal.SIGALRM, timeout)
    signal.setitimer(signal.ITIMER_REAL, MAX_SECONDS)
    a2 = 4*arb.pi()
    phi2 = (2*a2*a2-3*a2)*(-a2).exp()
    kappa = arb(7)/8*phi2
    b = {m: budgets(m,kappa) for m in (2,3,5,9)}
    B1, B2 = b[2]['eta1'], b[2]['eta2']
    C0 = B2+B1*B1
    assert B1 < arb('10.75') and B2 < arb('0.671') and C0 < 117
    for m, limits in [(3, ('0.000263','0.002843','0.06129')),
                      (5, ('7.3e-25','7.9e-24','1.7e-22'))]:
        row = b[m]
        row['r1_bound'] = row['eta1']+B1*row['rho']
        row['r2_bound'] = row['eta2']+2*B1*row['eta1']+(2*B1*B1+B2)*row['rho']
        for key, limit in zip(('rho','r1_bound','r2_bound'),limits):
            assert row[key] < arb(limit)
    # Full modular reflection proves this identity. The finite sum below,
    # together with an infinite endpoint tail, only checks its normalization.
    btheta = -q_endpoint(1)
    qsum = sum((q_endpoint(n) for n in range(2,9)),arb(0))
    reflection_check = btheta-qsum+arb(0,b[9]['Q'].abs_upper())
    assert btheta > 0 and reflection_check.contains(0)
    qA = sum((q_endpoint(n) for n in range(2,9) if n%2==0 or n%3==0),arb(0))
    qR = sum((q_endpoint(n) for n in range(2,9) if n%2 and n%3),arb(0))
    qA += arb(0,b[9]['Q'].abs_upper())
    qR += arb(0,b[9]['Q'].abs_upper())
    assert qA > 0 and qR > 0
    constants = {'kappa': bs(kappa), 'B1': bs(B1), 'B2': bs(B2), 'C0': bs(C0)}
    for m in (2,3,5):
        constants[str(m)] = {key: [bs(v) for v in val] if isinstance(val,list)
                             else val if key=='m' else bs(val)
                             for key,val in b[m].items()}
    record = {'schema': 'inv11_positive_packets_v1', 'date': '2026-10-18',
        'prepared_for': 'Edward Baker', 'model': 'gpt-6-astra', 'effort': 'max',
        'llm_assistance': 'Substantial LLM assistance; self-checks by the authoring assistant.',
        'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'python': platform.python_version(), 'python_flint': flint.__version__,
        'precision_bits': BITS, 'max_seconds': MAX_SECONDS,
        'scope': 'Certified constants in analytically proved real-axis bounds, an endpoint normalization check, and finite-interval integration identities. No theta sign or zero certificate.',
        'analytic_domain': {'t': '[0,1/2]', 'x': 'all real', 'packets': '{2} and {2,3}'},
        'constants': constants,
        'modular_endpoint_check': {'b': bs(btheta), 'residual': bs(reflection_check),
                                   'qA': bs(qA), 'qR': bs(qR), 'qR_over_qA': bs(qR/qA)},
        'finite_boundary_checks': finite_boundary_checks()}
    record['elapsed_seconds'] = time.monotonic()-started
    raw = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    record['peak_rss_bytes'] = int(raw if platform.system()=='Darwin' else 1024*raw)
    record['status'] = 'passed'
    output.write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps({'status':record['status'],'seconds':record['elapsed_seconds'],
                      'constants':{k:constants[k] for k in ('kappa','B1','B2','C0')},
                      'two_prime_limits':{k:constants['5'][k] for k in ('rho','r1_bound','r2_bound')}}))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    main(parser.parse_args().output)
