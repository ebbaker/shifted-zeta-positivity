#!/usr/bin/env python3
"""Floating sign/endpoint diagnostics for I4 Note 11; not certification.

23 October 2026. For Edward Baker, with substantial LLM assistance.
Model gpt-6-astra, effort max. Standard library only.
Run: python3 check_initial_cap_height_20261023.py --output RECORD.json
"""
import argparse
import cmath
import hashlib
import json
import math
from pathlib import Path


def simpson(f, a, b, n=16000):
    h = (b-a)/n
    return h/3*(f(a)+f(b)+sum((4 if j % 2 else 2)*f(a+j*h)
                              for j in range(1, n)))


def cap(jet, a, b):
    def density(x):
        f, d, dd = jet(x)
        return (d*d-f*dd)/(math.pi*(f*f+d*d))
    return simpson(density, a, b)


def phase(jet, a, b):
    def theta(x):
        f, d, _ = jet(x)
        assert f != 0
        return math.atan(d/f)
    return (theta(a)-theta(b))/math.pi


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    rows = []
    for label, jet, nlate, births, defect, entry, a, b in [
        ('delayed_double', lambda x: (x*x+0.5, 2*x, 2), 2, 2, 0, 0, -3, 3),
        ('delayed_triple', lambda x: (x**3+1.5*x, 3*x*x+1.5, 6*x),
         3, 2, 0, 0, -3, 3),
        ('right_wall_entry', lambda x: (x-1, 1, 0), 1, 0, 0, 1, -1, 0.5),
        ('left_wall_exit', lambda x: (x-1, 1, 0), 0, 0, 0, -1, 0.5, 3),
    ]:
        observed = cap(jet, a, b)
        expected = nlate-births-defect-entry+phase(jet, a, b)
        rows.append(dict(case=label, integral=observed, balance=expected,
                         absolute_error=abs(observed-expected)))
    for m in range(2, 9):
        r = 3.0
        # The spatially cancelled density is regular, including at x=0.
        observed = simpson(lambda x: m/(math.pi*(x*x+m*m)), -r, r)
        endpoint = -2*math.atan(m/r)/math.pi
        expected = m-(m-1)+endpoint
        rows.append(dict(case=f'initial_order_{m}', integral=observed,
                         balance=expected, defect=m-1,
                         absolute_error=abs(observed-expected)))
    for m in range(2, 7):
        roots = [complex(j+0.1*j*j, 0.2*(-1)**j) for j in range(m)]
        alpha, tau, beta = 0.07+0.11j, 0.2+0.15j, -0.03+0.02j
        lhs = 1+0j
        delta = 1+0j
        unit = 1+0j
        for i, zi in enumerate(roots):
            ui = cmath.exp(alpha*zi+beta*tau)
            unit *= ui
            derivative = ui
            for j, zj in enumerate(roots):
                if i != j:
                    derivative *= zi-zj
            lhs *= derivative
            for zj in roots[i+1:]:
                delta *= (zi-zj)**2
        rhs = (-1)**(m*(m-1)//2)*delta*unit
        rows.append(dict(case=f'root_derivative_product_{m}',
                         relative_error=abs(lhs-rhs)/abs(rhs)))
    # Check implicit barrier differentiation without differentiating roots.
    def g(x, t):
        v = math.log(x/(4*math.pi))
        return x/(4*math.pi)*(v-1)+11/8+t/16*v
    def wall(t, label):
        x = 10000.0
        for _ in range(12):
            v = math.log(x/(4*math.pi))
            x -= (g(x, t)-label)/(v/(4*math.pi)+t/(16*x))
        return x
    t = 0.3
    label = math.floor(g(10000, t))+0.5
    x = wall(t, label)
    v = math.log(x/(4*math.pi))
    exact_speed = -math.pi/4*v/(v+math.pi*t/(4*x))
    step = 0.01
    fd_speed = (wall(t+step, label)-wall(t-step, label))/(2*step)
    rows.append(dict(case='implicit_barrier_speed', analytic=exact_speed,
                     finite_difference=fd_speed,
                     absolute_error=abs(exact_speed-fd_speed)))
    errors = [r.get('absolute_error', r.get('relative_error', 0)) for r in rows]
    assert max(errors) < 1e-7, max(errors)
    record = dict(status='floating diagnostics passed; not interval-certified',
                  date='2026-10-23', model='gpt-6-astra', effort='max',
                  scope='Generic sign, multiplicity and product checks only; no theta numerics',
                  source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  checks=rows, maximum_reported_error=max(errors))
    Path(args.output).write_text(json.dumps(record, indent=2)+'\n')
    print(json.dumps({'checks': len(rows), 'maximum_reported_error': max(errors),
                      'record': args.output}))


if __name__ == '__main__':
    main()
