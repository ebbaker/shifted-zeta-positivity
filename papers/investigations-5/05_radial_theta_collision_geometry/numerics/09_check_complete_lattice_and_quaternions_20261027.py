#!/usr/bin/env python3
"""Finite exact and floating checks for RTC Note10, not interval certificates.

Prepared for Edward Baker, 2026-10-27; substantial LLM assistance.
Recorded model gpt-6-astra (Codex), effort max. Requires NumPy.
"""
import argparse
import hashlib
import itertools
import json
import math
import platform
from collections import Counter
from pathlib import Path

import numpy as np
from numpy.polynomial.legendre import leggauss


def coset(cutoff):
    b = math.isqrt(cutoff)
    return [(x, y, z) for x in range(-b, b+1) if x % 2
            for y in range(-b, b+1) if y % 2 == 0
            for z in range(-b, b+1) if z % 2 == 0
            if x*x+y*y+z*z <= cutoff]


def exact_checks():
    pts = coset(225)
    counts = Counter()
    for x, y, z in pts:
        counts[x*x+y*y+z*z] += (-1 if (z//2) % 2 else 1)
    for N in range(1, 226):
        n = math.isqrt(N)
        expected = 2*n*(-1 if ((n-1)//2) % 2 else 1) if n*n == N and n % 2 else 0
        assert counts[N] == expected, (N, counts[N], expected)
    nearest = [p for p in pts if sum(a*a for a in p) == 1]
    gap = min(sum(a*a for a in p) for p in pts if p not in nearest)
    assert sorted(nearest) == [(-1, 0, 0), (1, 0, 0)] and gap == 5

    # Doubled coordinates enumerate both Z^4 and (Z+1/2)^4 exactly.
    norm_max = 32
    b = math.isqrt(4*norm_max)
    hurwitz = Counter()
    hopf_shells = {n:Counter() for n in (1, 2, 3)}
    for parity in (0, 1):
        vals = [a for a in range(-b, b+1) if a % 2 == parity]
        for p in itertools.product(vals, repeat=4):
            ss = sum(a*a for a in p)
            if 0 < ss <= 4*norm_max and ss % 4 == 0:
                hurwitz[ss//4] += 1
                a, b0, c, d = p
                numer = (a*a+b0*b0-c*c-d*d, 2*(b0*c+a*d), 2*(b0*d-a*c))
                assert all(v % 4 == 0 for v in numer)
                hopf = tuple(v//4 for v in numer)
                assert sum(v*v for v in hopf) == (ss//4)**2
                if ss//4 in hopf_shells:
                    hopf_shells[ss//4][hopf] += 1
    for n in range(1, norm_max+1):
        assert hurwitz[n] == 24*sum(d for d in range(1, n+1, 2) if n % d == 0)
        inverse = sum(mobius(d)*d*hurwitz[n//d] for d in range(1,n+1,2) if n%d==0)
        assert inverse == 24
    assert len(hopf_shells[3]) == 24 and set(hopf_shells[3].values()) == {4}
    for ell in range(40):
        dim = math.comb(ell+3, 3) - (math.comb(ell+1, 3) if ell >= 2 else 0)
        assert dim == (ell+1)**2
        assert ell*(ell+2)+1 == (ell+1)**2
    return {"signed_shells_through_squared_radius":225,
            "nearest_points":nearest, "next_squared_radius":gap,
            "hurwitz_norms_through":norm_max,
            "hurwitz_first_eight_counts":[hurwitz[n] for n in range(1, 9)],
            "hopf_integrality_and_squared_norm_identity_checked":True,
            "mobius_shell_inverse_checked_through":norm_max,
            "norm_three_hopf_image_sites":len(hopf_shells[3]),
            "sphere_multiplicity_and_shift_through_degree":39,
            "all_passed":True}


def mobius(n):
    sign = 1
    p = 2
    while p*p <= n:
        if n % p == 0:
            n //= p
            sign = -sign
            if n % p == 0:
                return 0
        p += 1
    return -sign if n > 1 else sign


def sphere_grid(n_mu, n_phi):
    mu, wt = leggauss(n_mu)
    phi = 2*np.pi*np.arange(n_phi)/n_phi
    st = np.sqrt(1-mu**2)
    omega = np.stack([np.repeat(mu, n_phi),
                      (st[:, None]*np.cos(phi)).ravel(),
                      (st[:, None]*np.sin(phi)).ravel()], axis=1)
    weights = np.repeat(wt/(2*n_phi), n_phi)
    return omega, weights


def prepare(n_mu, n_phi, cutoff=81):
    q = np.array(coset(cutoff), dtype=float)
    sq = np.sum(q*q, axis=1)
    chi = np.where((q[:, 2].astype(int)//2) % 2, -1., 1.)
    omega, weights = sphere_grid(n_mu, n_phi)
    dot = q@omega.T
    cosine_mean = np.cos(np.pi*dot/2)@weights
    keep = sq > 1
    distances = np.maximum(0., sq[keep, None]+1-2*dot[keep])
    return sq, chi, weights, cosine_mean, keep, distances


def lattice_mean(r, data, direct_angles=True):
    sq, chi, weights, cosine_mean, keep, dist = data
    if direct_angles:
        first = np.sum(chi*np.exp(-np.pi*r*r*sq)*cosine_mean)
        second = np.sum(chi[keep]*(np.exp(-np.pi*r*r*dist/4)@weights))
    else:
        R = np.sqrt(sq)
        first = np.sum(chi*np.exp(-np.pi*r*r*sq)*np.sinc(R/2))
        R = R[keep]
        second = np.sum(chi[keep]*(np.exp(-np.pi*r*r*(R-1)**2/4)
                        -np.exp(-np.pi*r*r*(R+1)**2/4))/(np.pi*r*r*R))
    return np.pi*first/2 + np.pi*r*r*second/4 - np.exp(-np.pi*r*r)/2


def values(grid, cases):
    n_u, n_mu, n_phi = grid
    data = prepare(n_mu, n_phi)
    x, weights = leggauss(n_u)
    U = 1.6
    u, weights = (x+1)*U/2, weights*U/2
    r = np.exp(2*u)
    a_lattice = np.array([lattice_mean(v, data) for v in r])
    a_angular = np.array([lattice_mean(v, data, False) for v in r])
    n = np.arange(1., 13.)
    gauss = np.exp(-np.pi*r[:, None]**2*n[None, :]**2)
    a = np.sum(gauss, axis=1)
    ztrace = np.sum(n[None, :]**2*gauss, axis=1)
    phi = np.sum((2*np.pi**2*n[None, :]**4*np.exp(9*u[:, None])
                  -3*np.pi*n[None, :]**2*np.exp(5*u[:, None]))*gauss, axis=1)
    endpoint = np.pi/2*np.sum(n*n*np.exp(-np.pi*n*n))
    rows = []
    for t, z in cases:
        w = np.exp(t*u*u)*np.cos(z*u)
        w1 = np.exp(t*u*u)*((2*t*u-1)*np.cos(z*u)-z*np.sin(z*u))
        w2 = np.exp(t*u*u)*((2*t+4*t*t*u*u-z*z-1)*np.cos(z*u)
                            -4*t*u*z*np.sin(z*u))
        direct = np.sum(weights*w*phi)
        angular = 1/16+np.sum(weights*np.exp(u)*w2*a_angular)/8
        full3d = 1/16+np.sum(weights*np.exp(u)*w2*a_lattice)/8
        su2 = endpoint+np.pi/2*np.sum(weights*np.exp(5*u)*w1*ztrace)
        rows.append({"t":str(t), "z":str(z), "direct_H":str(complex(direct)),
                     "lattice_H":str(complex(full3d)),
                     "exact_angular_lattice_H":str(complex(angular)),
                     "unit_quaternion_trace_H":str(complex(su2)),
                     "lattice_absolute_error":float(abs(full3d-direct)),
                     "angular_absolute_error":float(abs(angular-direct)),
                     "unit_quaternion_absolute_error":float(abs(su2-direct))})
    sample = []
    for v in [1., 1.3, 2.]:
        direct = float(np.sum(np.exp(-np.pi*v*v*n*n)))
        val = float(lattice_mean(v, data))
        sample.append({"r":v, "A_direct":direct, "A_lattice":val, "absolute_error":abs(val-direct)})
    return {"grid_u_mu_phi":grid, "u_upper":U, "lattice_squared_radius_cutoff":81,
            "reference_n_max":12, "rows":rows, "profile_checks":sample,
            "max_sampled_angular_profile_error":float(np.max(np.abs(a_lattice-a_angular)))}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    cases = [(0.,0.), (0.1,5.), (-0.2,2.), (0.5,12.), (0.1+0.07j, 3.+0.2j)]
    results = [values((72, 24, 48), cases), values((96, 36, 72), cases)]
    errors = [row['lattice_absolute_error'] for row in results[-1]['rows']]
    assert max(errors) < 2e-12, errors
    xg, wg = leggauss(160)
    theta, wg = (xg+1)*np.pi/2, wg*np.pi/2
    ng = np.arange(1., 49.)
    characters = np.sin(theta[:,None]*ng[None,:])/np.sin(theta[:,None])
    green = (np.pi-theta)/(2*np.sin(theta))
    haar = 2/np.pi*np.sin(theta)**2
    green_rows = []
    for s in [0.25, 0.64, 1.]:
        damping = np.exp(-np.pi*s*ng*ng)
        kernel = characters@(ng*damping)
        green_error = float(abs(np.sum(wg*haar*green*kernel)-np.sum(damping)))
        mass_error = float(abs(np.sum(wg*haar*kernel)-np.exp(-np.pi*s)))
        assert green_error < 2e-13 and mass_error < 2e-13
        green_rows.append({'s':s, 'green_observation_error':green_error, 'shifted_heat_mass_error':mass_error})
    record = {"date":"2026-10-27", "prepared_for":"Edward Baker",
              "model":"gpt-6-astra", "effort":"max", "llm_assistance":"substantial",
              "status":"finite exact checks and floating normalization diagnostics only",
              "python":platform.python_version(), "numpy":np.__version__,
              "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "exact":exact_checks(), "floating":results,
              "floating_green_kernel_checks":green_rows,
              "limitations":"No interval rounding or certified quadrature/tail error. Infinite identities and convergence are proved analytically in Note10. No collision/sign test, independent review, or performance comparison."}
    args.output.write_text(json.dumps(record, indent=2)+'\n')
    print(json.dumps({"output":str(args.output), "exact_passed":True,
                      "max_fine_lattice_error":max(errors),
                      "max_fine_SU2_error":max(r['unit_quaternion_absolute_error'] for r in results[-1]['rows'])}))


if __name__ == '__main__':
    main()
