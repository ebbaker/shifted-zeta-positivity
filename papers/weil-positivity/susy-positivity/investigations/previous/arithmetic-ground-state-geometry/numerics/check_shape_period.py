#!/usr/bin/env python3
"""Check the shape-period ODE with exact algebra and independent Gaussian moments."""
import argparse
from fractions import Fraction as Q
import json
import math
from pathlib import Path


def add(*terms):
    out = {}
    for term in terms:
        for k, v in term.items():
            out[k] = out.get(k, Q(0)) + v
    return {k:v for k,v in out.items() if v}


def scale(term, coefficient=1, power=0):
    return {(p+power,n): Q(coefficient)*v for (p,n),v in term.items() if coefficient*v}


def derivative(term):
    out = {}
    for (p,n),v in term.items():
        if p:
            out = add(out, {(p-1,n):p*v})
        out = add(out, {(p,n+1):v})
    return out


def normal_moment(n):
    if n % 2:
        return 0
    return math.prod(range(1,n,2))


def gaussian_jet(k):
    moment = 0
    for a in range(k+1):
        for b in range(k-a+1):
            d = k-a-b
            coefficient = math.factorial(k)//(math.factorial(a)*math.factorial(b)*math.factorial(d))
            moment += coefficient*normal_moment(4*a+2*d)*normal_moment(4*b+2*d)
    return Q((-1)**k*moment,4**k)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output',type=Path)
    args = p.parse_args()
    mass_jets = [{(0,0):Q(1)}]
    for n in range(3):
        mass_jets.append(add(scale(mass_jets[-1],-(n+1)),scale(derivative(mass_jets[-1]),-2,1)))
    expected_third = {(0,0):Q(-6),(1,1):Q(-54),(2,2):Q(-48),(3,3):Q(-8)}
    assert mass_jets[3] == expected_third
    mass_equation = add(scale(mass_jets[3],6,2),scale(mass_jets[2],-7,1),
                        scale(mass_jets[1],2),scale(mass_jets[1],-7,1),scale(mass_jets[0],2))
    shape_equation = {(4,3):Q(48),(3,2):Q(288),(2,2):Q(28),
                      (2,1):Q(324),(1,1):Q(56),(0,1):Q(4),(1,0):Q(36),(0,0):Q(7)}
    assert mass_equation == scale(shape_equation,-1,1)
    jets = [gaussian_jet(k) for k in range(10)]
    for n in range(9):
        coefficient = Q(0)
        for (power,deriv),v in shape_equation.items():
            if n >= power:
                coefficient += v*jets[n-power+deriv]/math.factorial(n-power)
        assert coefficient == 0, (n,coefficient)
    record = {'status':'passed','arithmetic':'exact rational differential algebra and independent Gaussian moments',
              'checks':['homogeneity derivative hierarchy','mass-to-shape differential equation','nine coefficients from Gaussian moment jets'],
              'shape_equation':"48*c^4*C''' + (288*c^3+28*c^2)*C'' + (324*c^2+56*c+4)*C' + (36*c+7)*C = 0",
              'right_derivatives_at_zero':[str(v) for v in jets[:4]],
              'limitation':'Algebra after analytic cycle and differentiation assumptions; jets are asymptotic, not a convergent Taylor expansion; no physical norm or Weil positivity checked.'}
    output = json.dumps(record,indent=2,sort_keys=True)+'\n'
    if args.output:
        with args.output.open('x') as f:
            f.write(output)
    print(output,end='')


if __name__ == '__main__':
    main()
