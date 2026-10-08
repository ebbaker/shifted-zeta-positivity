#!/usr/bin/env python3
"""Exploratory theta-cutoff checks; floating point, not interval certificates.

Run from any working directory. Small JSON goes to stdout. The analytical
truncation and collision-certificate theorems are in
../newman_collisions/notes/2_ZETA_COLLISION_ARITHMETIC_20261008.md. No large output is generated.
"""
import json
import math


def phi_term(n, u):
    a = math.pi * n * n
    return (2*a*a*math.exp(9*u)-3*a*math.exp(5*u))*math.exp(-a*math.exp(4*u))


def moments(t, x, nmax, panels):
    """Composite Simpson quadrature on [0,1] for H, H', H''."""
    assert panels % 2 == 0
    h = 1.0 / panels
    terms = [[], [], []]
    for j in range(panels+1):
        u = j*h
        weight = 1 if j in (0, panels) else (4 if j % 2 else 2)
        kernel = math.exp(t*u*u)*math.fsum(phi_term(n, u) for n in range(1, nmax+1))
        trig = (math.cos(x*u), -u*math.sin(x*u), -u*u*math.cos(x*u))
        for k in range(3):
            terms[k].append(weight*kernel*trig[k])
    return [h*math.fsum(a)/3 for a in terms]


def odd_jet(nmax):
    # The tail is used to avoid subtracting nearly equal endpoint jets.
    # Ten further terms suffice for these exploratory double-precision rows;
    # the exact positive infinite series is proved in the note.
    values = []
    for n in range(nmax+1, nmax+11):
        a = math.pi*n*n
        values.append(a*(8*a*a-30*a+15)*math.exp(-a))
    return math.fsum(values)


def error_bound(k, nmax, tau=0.5, upper=1.0):
    """Analytic bounds evaluated in float: these are NOT directed enclosures."""
    m = nmax+1
    b = math.exp(-math.pi*m*m)*(m**4+m**3/(2*math.pi)+3*m/(4*math.pi**2)+3/(8*math.pi**3*m))
    lattice = 2*math.pi**2*math.exp(tau*upper**2+9*upper)*upper**(k+1)*b/(k+1)
    denominator = 4*math.pi*math.exp(4*upper)-2*tau*upper-9-k/upper
    assert denominator > 0
    spatial = 4*math.pi**2*upper**k*math.exp(tau*upper**2+9*upper-math.pi*math.exp(4*upper))/denominator
    return dict(lattice=lattice, spatial=spatial, total=lattice+spatial)


def main():
    rows = []
    for nmax, x, t in [(6, 28., .25), (6, 30., .25), (6, 40., .25),
                        (1, 80., .25), (1, 160., .25), (2, 240., .25)]:
        coarse = moments(t, x, nmax, 8192)
        fine = moments(t, x, nmax, 16384)
        wronskian = fine[1]**2-fine[0]*fine[2]
        a = odd_jet(nmax)
        rows.append(dict(nmax=nmax, x=x, t=t, H_derivatives=fine,
                         panel_doubling_change=[abs(v-w) for v, w in zip(coarse, fine)],
                         wronskian=wronskian, endpoint_odd_jet=a,
                         wronskian_leading_asymptotic=-2*a*a/x**6))
    print(json.dumps(dict(
        status="exploratory floating point; no interval quadrature or rectangle coverage; not an RH certificate",
        panels=[8192, 16384], integration_interval=[0, 1],
        theta_cutoff_6_analytic_errors_float=[error_bound(k, 6) for k in range(4)],
        rows=rows), indent=2))


if __name__ == '__main__':
    main()
