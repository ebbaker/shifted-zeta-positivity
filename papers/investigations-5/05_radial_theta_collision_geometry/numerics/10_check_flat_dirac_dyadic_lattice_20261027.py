#!/usr/bin/env python3
"""Note12 normalization checks; exact finite shells and floating quadrature.

27 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded model gpt-6-astra, effort max. Requires NumPy; no interval claims.
"""
import argparse
from collections import defaultdict
from fractions import Fraction
import itertools
import json
import math
from pathlib import Path

import numpy as np


def sites(radius):
    """Disjoint union 2**j ((1,0,0)+2 Z**3), inside a complete ball."""
    bound = math.floor(radius)
    out = []
    for m in itertools.product(range(-bound, bound + 1), repeat=3):
        norm2 = sum(x*x for x in m)
        if not 0 < norm2 <= radius*radius:
            continue
        v = m
        j = 0
        while all(x % 2 == 0 for x in v):
            v = tuple(x // 2 for x in v)
            j += 1
        if v[0] % 2 != 1 or v[1] % 2 or v[2] % 2:
            continue
        sign = 1 if (v[2] // 2) % 2 == 0 else -1
        out.append((m, v, j, sign, norm2))
    return out


def exact_shells():
    data = sites(15)
    shells = defaultdict(int)
    for m, v, j, sign, norm2 in data:
        shells[j, norm2] += sign
    checked = 0
    for j in range(4):
        for norm2 in range(1, 226):
            n = math.isqrt(norm2)
            h = n // (2**j)
            expected = 0
            if n*n == norm2 and n % (2**j) == 0 and h % 2:
                expected = 2*h*(-1)**((h-1)//2)
            assert shells[j, norm2] == expected, (j, norm2)
            checked += 1
    for n in range(1, 16):
        j = (n & -n).bit_length()-1
        h = n // (2**j)
        recovered = Fraction(shells[j, n*n]*(-1)**((h-1)//2), 2*h)
        assert recovered == 1
    # The first nonaxial contribution is essential, including its dilation.
    assert shells[0, 9] == -6 and shells[1, 36] == -6
    return {"complete_squared_radius": 225, "sites": len(data),
            "checked_scale_shell_pairs": checked, "recovered_square_weights": 15,
            "signed_shell_9": shells[0, 9], "dilated_signed_shell_36": shells[1, 36]}


def qmul(a, b):
    a0, av = a[0], np.array(a[1:], dtype=int)
    b0, bv = b[0], np.array(b[1:], dtype=int)
    return np.r_[a0*b0-np.dot(av, bv), a0*bv+b0*av+np.cross(av,bv)]


def exact_dirac():
    units = [np.eye(4, dtype=int)[j] for j in range(1, 4)]
    for i in range(3):
        for j in range(3):
            expected = np.array([-2 if i == j else 0, 0, 0, 0])
            assert np.array_equal(qmul(units[i],units[j])+qmul(units[j],units[i]), expected)
    # At a real quaternion q=t, (partial_t + D) exp(q) = (1-3)exp(t).
    return {"anticommutator_pairs": 9, "D_squared_coefficient": -1,
            "Fueter_exponential_real_axis_multiplier": 1-3,
            "note": "Algebra fixes D^2=-Delta; the Fueter calculation is only for ordinary exp(q)."}


def sphere_grid(nmu, nphi):
    mu, weights = np.polynomial.legendre.leggauss(nmu)
    phi = 2*np.pi*np.arange(nphi)/nphi
    radial = np.sqrt(1-mu*mu)[:,None]
    xyz = np.stack([np.broadcast_to(radial*np.cos(phi),(nmu,nphi)),
                    np.broadcast_to(radial*np.sin(phi),(nmu,nphi)),
                    np.broadcast_to(mu[:,None],(nmu,nphi))],axis=-1).reshape(-1,3)
    w = np.broadcast_to(weights[:,None]/(2*nphi),(nmu,nphi)).reshape(-1)
    return xyz,w


def packed(z):
    return [float(np.real(z)), float(np.imag(z))]


def floating(nu, nmu, nphi):
    data = sites(6)
    v = np.array([row[1] for row in data], dtype=float)
    signs = np.array([row[3] for row in data])
    norm2 = np.array([row[4] for row in data])
    b = np.pi*v/2
    xyz, sw = sphere_grid(nmu,nphi)
    h = xyz@b.T
    cs = np.cos(h)
    sphere_cos = sw@cs
    # Integral of the full angular Laplacian, not just its expected value zero.
    sphere_lap = sw@(-(np.sum(b*b,axis=1)-h*h)*cs+2*h*np.sin(h))
    x, w = np.polynomial.legendre.leggauss(nu)
    umax = 1.2
    u = (x+1)*umax/2
    uw = w*umax/2
    r = np.exp(2*u)
    gauss = np.exp(-np.pi*r[:,None]**2*norm2)
    avg_kernel = gauss@(signs*sphere_cos)
    a = np.pi*norm2
    avg_laplacian = np.sum(gauss*signs*(
        (4*a*a*r[:,None]**2-6*a)*sphere_cos+sphere_lap/r[:,None]**2),axis=1)
    n = np.arange(1,13)
    ng = np.exp(-np.pi*r[:,None]**2*n*n)
    phi = np.sum((2*np.pi**2*n**4*np.exp(9*u[:,None])
                  -3*np.pi*n*n*np.exp(5*u[:,None]))*ng,axis=1)
    pairs = [(0,0),(0.2,4),(-0.5,10),(0.1+0.2j,1+0.3j),(1,20)]
    rows = []
    errors = []
    for t,z in pairs:
        g = np.exp(t*u*u)
        cosine, sine = np.cos(z*u), np.sin(z*u)
        B0 = 2*t-1+4*t*t*u*u-z*z
        B1 = 4*t*u*z
        canonical = np.sum(uw*g*phi*cosine)
        # Note12 sphere formula, using its actually quadrature-averaged lattice field.
        completed = 1/16+np.pi/32*np.sum(uw*np.exp(u)*g*(B0*cosine-B1*sine)*avg_kernel)
        # Note12 D^2 formula, including the angular Laplacian before averaging.
        dirac = np.pi/8*np.sum(uw*r**2.5*g*cosine*avg_laplacian)
        error = max(abs(completed-canonical),abs(dirac-canonical))
        errors.append(float(error))
        rows.append({"t":packed(t),"z":packed(z),"canonical_H":packed(canonical),
                     "completed_lattice_H":packed(completed),"Dirac_lattice_H":packed(dirac),
                     "maximum_absolute_difference":float(error)})
    assert max(errors)<5e-12
    return {"u_nodes":nu,"sphere_nodes":[nmu,nphi],"u_max":umax,
            "lattice_ball_radius":6,"lattice_sites":len(data),
            "largest_angular_laplacian_mean_residual":float(max(abs(sphere_lap))),
            "largest_theta_mean_difference":float(max(abs(avg_kernel-4/np.pi*np.sum(ng,axis=1)))),
            "largest_H_difference":max(errors),"cases":rows}


def quaternion_exponential():
    data=sites(6)
    v=np.array([row[1] for row in data],dtype=float)
    signs=np.array([row[3] for row in data])
    norm2=np.array([row[4] for row in data])
    R=np.sqrt(np.sum(v*v,axis=1))
    cases=[]
    for r,t,z in [(1,0,0),(1.3,0.2,4),(1.1,0.1+0.2j,1+0.3j)]:
        u=math.log(r)/2
        phase=np.pi*R/2+z*u
        factor=signs*np.exp(-np.pi*r*r*norm2+t*u*u)/2
        scalar=np.sum(factor*np.sin(phase)/R)
        vector=-np.sum((factor*np.cos(phase)/(R*R))[:,None]*v,axis=0)
        n=np.arange(1,13)
        target=np.exp(t*u*u)*np.cos(z*u)*np.sum(np.exp(-np.pi*r*r*n*n))
        err=float(max(abs(scalar-target),max(abs(vector))))
        assert err<5e-14
        cases.append({"r":r,"t":packed(t),"z":packed(z),"scalar_error":float(abs(scalar-target)),
                      "vector_norm":float(np.linalg.norm(vector))})
    return cases


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    record={"date":"2026-10-27","prepared_for":"Edward Baker","llm_assistance":"substantial",
            "model":"gpt-6-astra","effort":"max","numpy_version":np.__version__,
            "scope":"Finite exact identities and floating normalization diagnostics; not interval or collision certificates.",
            "exact_shells":exact_shells(),"exact_quaternion_algebra":exact_dirac(),
            "quaternion_exponential":quaternion_exponential(),
            "quadrature":[floating(96,18,36),floating(144,26,52)]}
    output=json.dumps(record,indent=2)+'\n'
    if args.output: args.output.write_text(output)
    print(output)


if __name__=='__main__': main()
