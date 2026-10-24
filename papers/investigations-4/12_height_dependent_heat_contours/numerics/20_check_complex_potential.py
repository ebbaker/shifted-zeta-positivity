#!/usr/bin/env python3
"""Exact normalization checks for HDC Note 20; requires SymPy.

Generic holomorphic and antiholomorphic jets impose only H_t=-H_zz.
No theta estimate or collision exclusion is tested or claimed.
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
    f, g = s.symbols('f0:5'), s.symbols('g0:5')
    epsilon = s.symbols('epsilon', positive=True)

    def dz(q):
        return sum(s.diff(q, f[k])*f[k+1] for k in range(4))

    def db(q):
        return sum(s.diff(q, g[k])*g[k+1] for k in range(4))

    def dx(q):
        return dz(q)+db(q)

    def dy(q):
        return s.I*(dz(q)-db(q))

    def dt(q):
        return -sum(s.diff(q, f[k])*f[k+2]+s.diff(q, g[k])*g[k+2]
                    for k in range(3))

    D = f[0]*g[0]+epsilon**2
    S = s.log(D)
    # a omits the constant epsilon/sqrt(pi); rho and currents include it.
    a, b = f[1]/D, g[1]/D
    c2 = epsilon**2/s.pi
    rho = c2*a*b
    W, Wb = 2*dz(dz(S)), 2*db(db(S))
    V = -2*dx(dy(S))
    j, jb = c2*f[2]*g[1]/D**2, c2*g[2]*f[1]/D**2
    residuals = {
        'density': dz(db(S))-s.pi*rho,
        'real_potential': V+s.I*(W-Wb),
        'complex_constraint': db(W)-2*s.pi*dz(rho),
        'complex_evolution': dt(a)-db(db(a))+dz(dz(a))-(Wb-W)*a,
        'original_SP_evolution': s.I*dt(a)+dx(dy(a))-V*a,
        'original_SP_poisson': 4*dz(db(V))+8*s.pi*dx(dy(rho)),
        'complex_current': c2*(b*dz(a)-a*dz(b))-j,
        'continuity': dt(rho)+dz(j)+db(jb),
        'amplitude_antiholomorphic_derivative': db(a)+db(S)*a,
        'potential_heat_identity': dt(S)+dz(dz(S))+db(db(S))+dz(S)**2+db(S)**2,
        'potential_amplitude_identity': dz(S)*dz(a)-dz(dz(S))*a,
    }
    # Independent amplitude jets check the cutoff and residual conventions.
    z, zb, time = s.symbols('z zb time')
    aa = s.Function('a')(time,z,zb)
    ab = s.Function('a_bar')(time,z,zb)
    hh = s.Function('h')(z,zb)
    ww, wb = s.symbols('W W_bar')
    kinetic = lambda q: s.diff(q,zb,2)-s.diff(q,z,2)
    correction = (s.diff(hh,z,2)-s.diff(hh,zb,2))*aa + 2*(
        s.diff(hh,z)*s.diff(aa,z)-s.diff(hh,zb)*s.diff(aa,zb))
    residuals['localization_commutator'] = hh*kinetic(aa)-kinetic(hh*aa)-correction
    current = ab*s.diff(aa,z)-aa*s.diff(ab,z)
    current_bar = aa*s.diff(ab,zb)-ab*s.diff(aa,zb)
    rr = s.diff(aa,time)-kinetic(aa)+(ww-wb)*aa
    rr_bar = s.diff(ab,time)+kinetic(ab)+(wb-ww)*ab
    residuals['general_evolution_residual'] = (
        s.diff(aa*ab,time)+s.diff(current,z)+s.diff(current_bar,zb)
        -ab*rr-aa*rr_bar)
    kx, ky = s.symbols('kx ky', real=True)
    multiplier = 2*s.pi*(kx-s.I*ky)/(kx+s.I*ky)
    residuals['Fourier_real_potential'] = (
        2*s.im(multiplier)+8*s.pi*kx*ky/(kx**2+ky**2))
    checked = {key: str(s.cancel(s.expand_complex(value))
                        if key == 'Fourier_real_potential' else s.cancel(value))
               for key, value in residuals.items()}
    if any(value != '0' for value in checked.values()):
        raise AssertionError(checked)
    record = {
        'date': '2026-10-24',
        'prepared_for': 'Edward Baker',
        'llm_assistance': 'Substantial; same-assistant derivation and algebra checks',
        'model': 'gpt-6-astra (Codex)',
        'reasoning_effort': 'max',
        'python': platform.python_version(),
        'sympy': s.__version__,
        'residuals': checked,
        'scope': 'Exact coordinate and potential reformulation; no new estimate. '
                 'Generic jets permit critical and multiple points; epsilon is positive.'
    }
    output = json.dumps(record, indent=2)+'\n'
    if args.output:
        args.output.write_text(output)
    print(output, end='')


if __name__ == '__main__':
    main()
