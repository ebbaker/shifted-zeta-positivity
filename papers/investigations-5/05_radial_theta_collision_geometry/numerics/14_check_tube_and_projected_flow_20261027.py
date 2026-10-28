#!/usr/bin/env python3
"""Exact control algebra; floating tube geometry and additive-response checks.

For Edward Baker, 27 October 2026 (America/New_York).
LLM assistance: gpt-6-astra, recorded effort max, investigation05 chat0008.
Requires Python 3 and NumPy. No theta sampling, interval certificate, or
simulation of the infinite-dimensional projected flow is performed.
"""
import argparse
import hashlib
import json
import math
import platform
from pathlib import Path

import numpy as np
from numpy.polynomial.legendre import leggauss


def trim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def add(p, q):
    out = [0] * max(len(p), len(q))
    for i, v in enumerate(p):
        out[i] += v
    for i, v in enumerate(q):
        out[i] += v
    return trim(out)


def scale(p, a):
    return trim([a * v for v in p])


def mul(p, q):
    out = [0] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i + j] += a * b
    return trim(out)


def gaussian_derivative(p, exponent=1):
    deriv = [i * p[i] for i in range(1, len(p))] or [0]
    return add(deriv, [0] + scale(p, -2 * exponent))


def exact_control():
    y, z, g = [4, 0, 4], [-1], [24, 0, 0, 0, 16]
    dy, dz = gaussian_derivative(y), gaussian_derivative(z)
    w = add(mul(y, dz), scale(mul(dy, z), -1))
    k = add(mul(y, y), mul(g, z))
    checks = {
        'Y_forcing': add(add(gaussian_derivative(dy), scale(y, 6)), scale(g, -1)) == [0],
        'Z_fixed_source_derivative': add(add(gaussian_derivative(dz), scale(z, 6)), y) == [0],
        'W_polynomial': w == [0, 8],
        'K_polynomial': k == [-8, 0, 32],
        'Wronskian_derivative': add(gaussian_derivative(w, 2), k) == [0],
        'double_boundary_data': dy[0] == dz[0] == 0,
    }
    assert all(checks.values())
    return checks


S, B, LAM = 1.7, 0.7, 6.0
ASTAR = 2 * math.sqrt(LAM)


def axis(r):
    u = math.log(r) / 2
    co, si = math.cos(ASTAR * u), math.sin(ASTAR * u)
    v = np.array([co, -B * u * si, 0.0])
    dv = np.array([-ASTAR * si, -B * si - B * ASTAR * u * co, 0.0])
    ddv = np.array([-ASTAR**2 * co, -2 * B * ASTAR * co + B * ASTAR**2 * u * si, 0.0])
    m = np.linalg.norm(v)
    n = v / m
    dm = np.dot(n, dv)
    nu = (dv - n * dm) / m
    ddm = np.dot(nu, dv) + np.dot(n, ddv)
    nuu = (ddv - n * ddm - 2 * dm * nu) / m
    nr = nu / (2 * r)
    nrr = (nuu - 2 * nu) / (4 * r**2)
    return n, nr, nrr


def profile(q):
    return S * np.exp(S * q) / math.sinh(S)


def radial(r):
    x = math.log(r)
    e = math.exp(-x * x)
    y, z, g = (4 * x * x + 4) * e, -e, (16 * x**4 + 24) * e
    yp, zp = -8 * x**3 * e, 2 * x * e
    psi, zeta = y / math.sqrt(r), z / math.sqrt(r)
    psir, zetar = (yp - y / 2) / r**1.5, (zp - z / 2) / r**1.5
    return psi, zeta, psir, zetar, g / r**2.5


def wk(r):
    x = np.log(r)
    return 8 * x * np.exp(-2 * x * x), 8 * (4 * x * x - 1) * np.exp(-2 * x * x)


def grad_lap(fun, X, step):
    f0 = fun(X)
    grad = np.empty(3)
    lap = 0.0
    for i in range(3):
        e = np.zeros(3)
        e[i] = step
        fm2, fm1, fp1, fp2 = fun(X - 2*e), fun(X-e), fun(X+e), fun(X+2*e)
        grad[i] = (fm2 - 8*fm1 + 8*fp1 - fp2) / (12*step)
        lap += (-fp2 + 16*fp1 - 30*f0 + 16*fm1 - fm2) / (12*step*step)
    return grad, lap


def points():
    return [math.exp(x) * np.array(w) / np.linalg.norm(w)
            for x, w in [(0.3, [1., 2., 3.]), (0.7, [-2., 1., .8]), (1., [.3, -1., .4])]]


def gauge_diagnostic(step_scale):
    errors = []
    for X in points():
        r = np.linalg.norm(X)
        omega = X / r
        n, nr, nrr = axis(r)
        q = np.dot(n, omega)
        gradell = S * (np.dot(nr, omega) * omega + (n - q*omega)/r)
        lapell = S * (np.dot(nrr + 2*nr/r, omega) - 2*q/r**2)
        potential = (LAM+.25)/r**2 + np.dot(gradell, gradell) - lapell

        def f_at(Y, component):
            ry = np.linalg.norm(Y)
            ny = axis(ry)[0]
            return profile(np.dot(ny, Y/ry)) * radial(ry)[component]

        psi, zeta, _, _, Q = radial(r)
        f = profile(q)*psi
        for component, target in [(0, profile(q)*Q), (1, -f/r**2)]:
            fun = lambda Y: f_at(Y, component)
            gradient, laplacian = grad_lap(fun, X, step_scale*r)
            residual = laplacian - 2*np.dot(gradell, gradient) + potential*fun(X) - target
            errors.append(abs(residual)/(1+abs(target)))
    return max(errors)


def quadrature(a, b, order):
    nodes, weights = leggauss(order)
    return (a+b)/2+(b-a)*nodes/2, (b-a)*weights/2


def cap(c):
    return S * (math.exp(2*S)-math.exp(2*S*c)) / (4*math.sinh(S)**2)


def tube_diagnostic(order, variable=False):
    r0, r1 = math.exp(.18), math.exp(1.15)
    slope = .18 if variable else 0.0
    cfun = lambda r: .35 + slope * math.log(r)
    rs, wrs = quadrature(r0, r1, order)
    signed_side = unsigned_side = predicted_side = predicted_unsigned = body = 0.0
    phis, wphis = [], []
    for i in range(4):
        ps, ws = quadrature(i*math.pi/2, (i+1)*math.pi/2, order)
        phis.extend(ps)
        wphis.extend(ws)
    phis, wphis = np.array(phis), np.array(wphis)
    for r, wr in zip(rs, wrs):
        n, nr, _ = axis(r)
        e1, e1r, e2 = np.array([-n[1], n[0], 0.]), np.array([-nr[1], nr[0], 0.]), np.array([0., 0., 1.])
        c, cp = cfun(r), slope/r
        d = math.sqrt(1-c*c)
        dp = -c*cp/d
        tangent = np.cos(phis)[:,None]*e1 + np.sin(phis)[:,None]*e2
        tangentr = np.cos(phis)[:,None]*e1r
        omega = c*n+d*tangent
        omegar = cp*n+c*nr+dp*tangent+d*tangentr
        Xr = omega+r*omegar
        Xphi = r*d*(-np.sin(phis)[:,None]*e1 + np.cos(phis)[:,None]*e2)
        outward_area = -np.cross(Xr, Xphi)
        W, K = wk(r)
        currents = profile(c)**2 * W/r**2 * omega
        fluxes = np.sum(currents*outward_area, axis=1)
        signed_side += wr*np.dot(wphis, fluxes)/(4*math.pi)
        unsigned_side += wr*np.dot(wphis, np.abs(fluxes))/(4*math.pi)
        predicted_side += wr*.5*profile(c)**2*W*cp
        predicted_unsigned += wr*profile(c)**2*d/math.pi*abs(W)*np.linalg.norm(nr)
        qs, wqs = quadrature(c, 1., order)
        angular_bulk = np.dot(wqs, profile(qs)**2)/2
        body -= wr*angular_bulk*K/r
    faces = cap(cfun(r1))*wk(r1)[0]-cap(cfun(r0))*wk(r0)[0]
    residual = body-faces-signed_side
    out = dict(variable_width=variable, order=order, body=float(body), radial_faces=float(faces),
               signed_lateral=float(signed_side), predicted_lateral=float(predicted_side),
               balance_residual=float(residual), lateral_formula_error=float(abs(signed_side-predicted_side)),
               unsigned_lateral=float(unsigned_side))
    if not variable:
        out['unsigned_formula_error'] = float(abs(unsigned_side-predicted_unsigned))
    return out


MU, R0, R1 = .8, 1.1, 3.5


def additive_fields(X):
    r = np.linalg.norm(X)
    omega = X/r
    psi, zeta, psir, zetar, Q = radial(r)
    p = (r-R0)**4 * (R1-r)**4
    logp = 4/(r-R0)-4/(R1-r)
    pr = p*logp
    prr = p*(logp**2-4/(r-R0)**2-4/(R1-r)**2)
    q = omega[2]
    U = p*q
    gradU = pr*q*omega+p/r*(np.array([0.,0.,1.])-q*omega)
    G = (prr+2*pr/r-2*p/r**2-MU**2*p)*q
    j = (psi+U)*zetar*omega-zeta*(psir*omega+gradU)
    V = (LAM+.25)/r**2
    sigma = psi/r**2+(V+MU**2)*zeta
    density = psi*psi/r**2+Q*zeta+sigma*U+zeta*G
    omitted = (V+MU**2)*zeta*U
    return j, density, omitted


def additive_diagnostic(step_scale):
    errors, omission_errors = [], []
    for X in points():
        step = step_scale*np.linalg.norm(X)
        div = 0.0
        for i in range(3):
            e = np.zeros(3)
            e[i] = step
            fm2, fm1, fp1, fp2 = [additive_fields(Y)[0][i] for Y in [X-2*e,X-e,X+e,X+2*e]]
            div += (fm2-8*fm1+8*fp1-fp2)/(12*step)
        _, density, omitted = additive_fields(X)
        errors.append(abs(div+density)/(1+abs(density)))
        omission_errors.append(abs(omitted)/(1+abs(density)))
    return dict(max_relative_residual=max(errors), omitted_projected_potential_effect=max(omission_errors))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--output', required=True)
    args = ap.parse_args()
    tubes = [tube_diagnostic(n, variable) for n in (32,64) for variable in (False,True)]
    gauges = {str(h):gauge_diagnostic(h) for h in (1e-3,5e-4)}
    additives = {str(h):additive_diagnostic(h) for h in (1e-3,5e-4)}
    assert max(gauges.values()) < 2e-7
    assert all(abs(t['balance_residual']) < 2e-10 and t['lateral_formula_error'] < 2e-10 for t in tubes)
    assert all(t.get('unsigned_formula_error', 0) < 2e-10 for t in tubes)
    assert all(abs(t['signed_lateral']) > 1e-3 for t in tubes if t['variable_width'])
    assert max(v['max_relative_residual'] for v in additives.values()) < 2e-7
    assert min(v['omitted_projected_potential_effect'] for v in additives.values()) > 1e-3
    record = dict(date='2026-10-27', timezone='America/New_York', prepared_for='Edward Baker',
                  llm_assistance='substantial', model='gpt-6-astra', effort='max', chat='0008',
                  status='Exact polynomial checks plus floating diagnostics; no interval certification',
                  exact_control=exact_control(), parameters=dict(s=S,b=B,lambda_value=LAM,a_star=ASTAR,mu=MU),
                  conjugated_operator=gauges, tube_geometry=tubes, additive_response=additives,
                  scope='No theta data sampled. No collision exclusion. The projected flow theorem is analytical, not simulated.',
                  python=platform.python_version(), numpy=np.__version__,
                  script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    Path(args.output).write_text(json.dumps(record,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'status':'passed','gauge_max':max(gauges.values()),
                      'tube_balance_max':max(abs(t['balance_residual']) for t in tubes),
                      'additive_max':max(v['max_relative_residual'] for v in additives.values())}))


if __name__ == '__main__':
    main()
