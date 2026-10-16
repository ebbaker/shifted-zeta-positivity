#!/usr/bin/env python3
"""Seeded Gaussian pair interface: exact algebra and independent finite diagnostics.

Standard library only. The note derives the infinite-dimensional result.
This program is neither a supersymmetry checker nor an arithmetic certificate.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
import math
from pathlib import Path


def response(q, u):
    return (1 - q) ** 2 * math.exp(-u / 2) / (1 - q * math.exp(-u)) ** 2


def selected(q, u):
    # Additional comparison-only projection: even b occupation, excluding b=0.
    x = q * q * math.exp(-2 * u)
    return ((1 - q) ** 2 * math.exp(-u / 2)
            * x * (3 - x) / (1 - x) ** 2)


def omitted(u):
    return math.exp(-2.5 * u) / (-math.expm1(-2 * u))


def singular_selected(u):
    x = math.exp(-2 * u)
    return math.exp(-2.5 * u) * (3 - x) / (-math.expm1(-2 * u)) ** 2


def tail(z, n):
    """Exact sum of (k+1) z**k for k>=n; valid for 0<=z<1."""
    return z ** n * ((n + 1) - n * z) / (1 - z) ** 2


def squeeze_ode(r, levels, steps):
    """RK4 for dc/dr=(a^dagger b^dagger-ab)c in the F=1 sector.

    Initial |1,0>; no closed-form amplitudes used by the integrator.
    Truncation and RK errors are diagnostics, not interval enclosures.
    """
    links = [math.sqrt((k + 1) * (k + 2)) for k in range(levels - 1)]

    def rhs(c):
        return [(links[k - 1] * c[k - 1] if k else 0.0)
                - (links[k] * c[k + 1] if k + 1 < levels else 0.0)
                for k in range(levels)]

    c = [1.0] + [0.0] * (levels - 1)
    h = r / steps
    for _ in range(steps):
        k1 = rhs(c)
        k2 = rhs([v + h * d / 2 for v, d in zip(c, k1)])
        k3 = rhs([v + h * d / 2 for v, d in zip(c, k2)])
        k4 = rhs([v + h * d for v, d in zip(c, k3)])
        c = [v + h * (d1 + 2 * d2 + 2 * d3 + d4) / 6
             for v, d1, d2, d3, d4 in zip(c, k1, k2, k3, k4)]
    return c


def run():
    exact = []
    for lam in (F(0), F(1, 5), F(1, 2), F(4, 5)):
        q = lam * lam
        g = lam / (1 + q)
        gap = (1 - q) / (2 * (1 + q))
        assert gap * gap == F(1, 4) - g * g
        # H_g ground recurrence after dividing out c_k, k>=1.
        for k in range(1, 17):
            if lam:
                assert F(2 * k + 1, 2) - g * (k / lam + (k + 1) * lam) == gap
        assert F(1, 2) - g * lam == gap
        n = 40
        partial = sum(((k + 1) * q ** k for k in range(n)), F(0))
        assert (1 - q) ** 2 * (partial + tail(q, n)) == 1
        for v in (F(1), F(3, 4), F(1, 4)):
            z = q * v
            finite = sum(((k + 1) * z ** k for k in range(n)), F(0))
            assert finite + tail(z, n) == 1 / (1 - z) ** 2
            x = z * z
            even = (1 / (1 - z) ** 2 + 1 / (1 + z) ** 2) / 2
            assert even - 1 == x * (3 - x) / (1 - x) ** 2
        exact.append(dict(lambda_value=str(lam), q=str(q), coupling=str(g),
                          gap=str(gap), normalized_tail_after_40=str((1-q)**2*tail(q,n))))

    wick = []
    for k in range(25):
        # Exponential coefficient 1/k!, Wick norms (k+1)! k!.
        weight = F(math.factorial(k + 1) * math.factorial(k), math.factorial(k) ** 2)
        assert weight == k + 1
        wick.append(dict(k=k, energy=str(F(2*k+1, 2)), weight_over_geometric=str(weight)))
    # Even-sector equal weights at n=1,2 require q^2=3/5;
    # equal weights at n=2,3 instead require q^2=5/7.
    assert F(3, 5) != F(5, 7)

    ode = []
    for q in (0.04, 0.25, 0.64):
        r = math.atanh(math.sqrt(q))
        levels = 120
        expected = [(1-q) * math.sqrt(k+1) * q ** (k/2) for k in range(levels)]
        coarse = squeeze_ode(r, levels, 512)
        fine = squeeze_ode(r, levels, 1024)
        coarse_error = max(abs(a-b) for a,b in zip(coarse, expected))
        fine_error = max(abs(a-b) for a,b in zip(fine, expected))
        assert fine_error < 2e-10
        norm_error = abs(sum(c*c for c in fine) - 1)
        assert norm_error < 2e-10
        u = 0.37
        numerical_response = sum(c*c * math.exp(-(k+0.5)*u) for k,c in enumerate(fine))
        response_error = abs(numerical_response-response(q,u))
        assert response_error < 2e-10
        ode.append(dict(q=q, levels=levels, steps=[512,1024],
                        max_amplitude_errors=[coarse_error,fine_error],
                        norm_error=norm_error, u=u, response_error=response_error,
                        analytic_norm_tail=(1-q)**2*tail(q,levels)))

    comparisons = []
    for q in (0.0, 0.25, 0.64, 0.99):
        assert abs(response(q,0)-1) < 1e-14
        for u in (0.02, 0.1, 0.5, 1.0, 2.0):
            n = 2000
            direct = sum((1-q)**2 * (k+1) * q**k * math.exp(-(k+0.5)*u)
                         for k in range(n))
            error = abs(direct-response(q,u))
            assert error < 2e-12
            even = sum((1-q)**2 * (2*j+1) * q**(2*j) * math.exp(-(2*j+0.5)*u)
                       for j in range(1,n//2))
            assert abs(even-selected(q,u)) < 2e-12
            comparisons.append(dict(q=q,u=u,response=response(q,u),
                                     comparison_only_selected=selected(q,u),
                                     target=omitted(u),series_error=error))

    short_distance = []
    for u in (1e-2, 1e-3, 1e-4, 1e-5):
        full = math.exp(-u/2) / (-math.expm1(-u))**2
        ss = singular_selected(u)
        short_distance.append(dict(u=u,u_times_target=u*omitted(u),
                                   u_squared_times_singular_full=u*u*full,
                                   u_squared_times_singular_selected=u*u*ss))
    last = short_distance[-1]
    assert abs(last['u_times_target']-0.5) < 1e-5
    assert abs(last['u_squared_times_singular_full']-1) < 1e-5
    assert abs(last['u_squared_times_singular_selected']-0.5) < 1e-5

    regulator = []
    for eps in (0.2,0.05,0.01):
        q = math.exp(-2*eps)
        for u in (0.1,0.5,1.0):
            # exp(-eps D)|chi> versus the unnormalized squeeze family.
            left = math.exp(-eps)*response(q,u)/(1-q)**2
            right = math.exp(-(u+2*eps)/2) / (-math.expm1(-(u+2*eps)))**2
            assert abs(left/right-1) < 2e-14
            regulator.append(dict(epsilon=eps,u=u,relative_error=abs(left/right-1)))

    return dict(schema=1, status='PASS',
                model='OpenAI GPT-6 (Codex; developer-provided identity)',
                effort='unavailable; not exposed in this session',
                scope='Specified Gaussian mode interface only; no local supersymmetric interface, physical arithmetic transfer, or arithmetic positivity certificate',
                source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                exact_algebra=exact, wick_weights=wick,
                exact_mismatch={'q_squared_from_first_pair':'3/5',
                                'q_squared_from_second_pair':'5/7',
                                'equal_weight_conditions_incompatible':True},
                independent_squeeze_ode=ode, comparisons=comparisons,
                short_distance_diagnostics=short_distance, heat_regulator=regulator,
                analytic_scope='Infinite identities, domains, and limits proved in the note; finite checks here are not their proof',
                certificates='Only the displayed finite rational identities are exact; no physical or arithmetic certificate')


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    result=run()
    payload=json.dumps(result,indent=2,sort_keys=True)+'\n'
    if args.output:
        args.output.write_text(payload)
        print(json.dumps(dict(status=result['status'],exact_couplings=len(result['exact_algebra']),
                              wick_levels=len(result['wick_weights']),ode_runs=len(result['independent_squeeze_ode']),
                              comparisons=len(result['comparisons']),regulator_checks=len(result['heat_regulator']))))
    else:
        print(payload,end='')


if __name__=='__main__':
    main()
