#!/usr/bin/env python3
"""Exact algebra supporting the complex-field book, 24 October 2026.

Prepared for Edward Baker with substantial LLM assistance.
Model gpt-6-astra (Codex), actual reasoning effort max.
These checks supplement analytic proofs; they do not establish global
integrability, Picard's theorem, or a theta-specific estimate.
"""
import argparse
import json
import platform
from pathlib import Path
import sympy as s


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    indices = [(i, j) for i in range(5) for j in range(5-i)]
    a = {(i, j): s.Symbol(f'a{i}{j}') for i, j in indices}
    b = {(i, j): s.Symbol(f'b{i}{j}') for i, j in indices}
    v = {(i, j): s.Symbol(f'v{i}{j}', real=True) for i, j in indices}
    h = {(i, j): s.Symbol(f'h{i}{j}', real=True) for i, j in indices}
    maps = [a, b, v, h]

    def diff(q, direction):
        di, dj = direction
        return sum(s.diff(q, m[i, j])*m[i+di, j+dj]
                   for m in maps for i, j in indices
                   if (i+di, j+dj) in m)

    def dx(q): return diff(q, (1, 0))
    def dy(q): return diff(q, (0, 1))

    A, B, V, H = a[0, 0], b[0, 0], v[0, 0], h[0, 0]
    At = s.I*(a[1, 1]-V*A)
    Bt = -s.I*(b[1, 1]-V*B)
    rho = A*B
    rhot = At*B+A*Bt
    px = (B*a[1, 0]-A*b[1, 0])/(2*s.I)
    py = (B*a[0, 1]-A*b[0, 1])/(2*s.I)
    residuals = {'continuity': rhot+dx(py)+dy(px)}
    for name, d, ij in [('x', dx, (1, 0)), ('y', dy, (0, 1))]:
        Ai, Bi = a[ij], b[ij]
        pit = (Bt*Ai+B*d(At)-At*Bi-A*d(Bt))/(2*s.I)
        stress_x = (B*dy(Ai)+A*dy(Bi))/2
        stress_y = (b[1, 0]*Ai+a[1, 0]*Bi)/2
        residuals['momentum_'+name] = pit-dx(stress_x)+dy(stress_y)+rho*d(V)
    residuals['window_continuity'] = (
        H**2*rhot+dx(H**2*py)+dy(H**2*px)
        -2*H*(dx(H)*py+dy(H)*px))
    Z, Zt = s.symbols('Z Zt', positive=True)
    psi = H*A/s.sqrt(Z)
    psit = H*At/s.sqrt(Z)-Zt*psi/(2*Z)
    correction = (dx(dy(H))*A+dx(H)*dy(A)+dy(H)*dx(A))/s.sqrt(Z)
    residuals['normalized_state'] = (
        s.I*psit+dx(dy(psi))-V*psi-correction+s.I*Zt*psi/(2*Z))
    r, rb = s.symbols('residual conjugate_residual')
    source_rhot = (At-s.I*r)*B+A*(Bt+s.I*rb)
    residuals['residual_source'] = (
        source_rhot+dx(py)+dy(px)-(B*r-A*rb)/s.I)
    kx, ky = s.symbols('kx ky', real=True)
    multiplier = -8*s.pi*kx*ky/(kx*kx+ky*ky)
    residuals['degree_zero_multiplier'] = (
        kx*s.diff(multiplier,kx)+ky*s.diff(multiplier,ky))
    residuals = {k: s.simplify(s.factor(x)) for k, x in residuals.items()}
    assert all(x == 0 for x in residuals.values()), residuals

    z, t, w = s.symbols('z t w')
    polynomial_checks = []
    for n in range(2, 8):
        coeff = s.symbols('c0:'+str(n))
        initial = z**n + sum(coeff[j]*z**j for j in range(n))
        heat = sum((-t)**j/s.factorial(j)*s.diff(initial,z,2*j)
                   for j in range(n//2+1))
        assert s.expand(s.diff(heat,t)+s.diff(heat,z,2)) == 0
        poly = s.Poly(heat-w,z)
        S1 = -poly.coeff_monomial(z**(n-1))
        S2 = S1**2-2*poly.coeff_monomial(z**(n-2))
        assert s.diff(S1,t) == 0
        assert s.diff(S2,t) == 2*n*(n-1)
        if n > 2: assert not S2.has(w)
        else: assert s.diff(S2,w) == 2
        polynomial_checks.append({'degree':n,'first_moment_derivative':0,
                                  'second_moment_derivative':2*n*(n-1),
                                  'angular_moment':n*(n-1)})
    radius, scale = s.symbols('radius scale', positive=True)
    gradient_size = radius/(4*scale)*s.exp(-radius**2/(8*scale))
    assert s.simplify(s.diff(gradient_size,radius).subs(radius,2*s.sqrt(scale))) == 0
    assert s.simplify(gradient_size.subs(radius,2*s.sqrt(scale))
                      -s.exp(-s.Rational(1,2))/(2*s.sqrt(scale))) == 0
    record = {'date':'2026-10-24','prepared_for':'Edward Baker',
              'model':'gpt-6-astra (Codex)','reasoning_effort':'max',
              'llm_assistance':'Substantial; same-assistant analytic derivation and algebra checks',
              'python':platform.python_version(),'sympy':s.__version__,
              'local_residuals':{k:str(v) for k,v in residuals.items()},
              'polynomial_newton_checks':polynomial_checks,
              'gaussian_lipschitz_constant':'exp(-1/2)/(2*sqrt(s))',
              'scope':'Exact local identities, multiplier homogeneity and finite-degree coefficient checks. Global conservation, mass classification, zero-energy polynomial conclusion and measure limits rely on the manuscript proofs and their hypotheses. No theta bound or independent review.'}
    if args.output: args.output.write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps({'all_residuals_zero':True,'identities':len(residuals),
                      'polynomial_degrees':[x['degree'] for x in polynomial_checks],
                      'gaussian_constant':'checked'}))


if __name__ == '__main__':
    main()
