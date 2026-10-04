#!/usr/bin/env python3
"""Exact common-shell source covariance; no Sonin/Weil loss certificate.

Prepared for Edward Baker, 2026-10-03, with substantial LLM assistance.
Model: GPT-6 (Codex); exact serving variant and effort are not exposed.
Uses Python standard-library rational arithmetic only.
"""
from fractions import Fraction as Q
from math import comb
from decimal import Decimal, localcontext
from pathlib import Path
from itertools import combinations
from hashlib import sha256
import json
import platform


def trim(p):
    p = list(p)
    while len(p) > 1 and not p[-1]:
        p.pop()
    return p


def derivative(p):
    return trim([Q(i)*p[i] for i in range(1, len(p))] or [Q(0)])


def multiply(p, q):
    out = [Q(0)]*(len(p)+len(q)-1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i+j] += a*b
    return trim(out)


def evaluate(p, x):
    out = Q(0)
    for c in reversed(p):
        out = out*x+c
    return out


def integrate(p, a, b):
    return sum((c*(b**(i+1)-a**(i+1))/Q(i+1)
                for i, c in enumerate(p)), Q(0))


def affine(p, a, b):
    # Coefficients of p(a+b*x), avoiding any floating arithmetic.
    out = [Q(0)]*len(p)
    for i, c in enumerate(p):
        for j in range(i+1):
            out[j] += c*comb(i, j)*a**(i-j)*b**j
    return trim(out)


def raw_profile():
    # Exact method adapted from the existing translated-probe certificate:
    # integral_-a^(a-u) g0(x)g0(x+u)dx on 0<=u<=2a.
    a = Q(1, 4)
    h = [Q(0)]*17
    for j in range(9):
        h[2*j] = Q(comb(8,j)*(-16)**j)
    first = derivative(h)
    third = derivative(derivative(first))
    g0 = [c/4 for c in first]
    for j, c in enumerate(third):
        g0[j] -= c
    g0 = trim(g0)
    raw = [Q(0)]*(2*len(g0))
    for i, gi in enumerate(g0):
        if not gi:
            continue
        for j, gj in enumerate(g0):
            if not gj:
                continue
            for k in range(j+1):
                power = i+k+1
                c = gi*gj*comb(j,k)/power
                for v in range(power+1):
                    raw[j-k+v] += c*comb(power,v)*a**(power-v)*(-1)**v
                raw[j-k] -= c*(-a)**power
    raw = trim(raw)
    norm = raw[0]
    assert norm == Q(146640624550936576,37921101075)
    assert integrate(multiply(g0,g0),-a,a) == norm
    assert evaluate(raw,Q(1,2)) == 0
    assert raw[1] == 0
    assert integrate(raw,0,Q(1,2)) == 0
    return h, g0, raw, norm


def determinant(matrix):
    work = [row[:] for row in matrix]
    out = Q(1)
    for col in range(len(work)):
        pivot = next((j for j in range(col,len(work)) if work[j][col]), None)
        if pivot is None:
            return Q(0)
        if pivot != col:
            work[col],work[pivot] = work[pivot],work[col]
            out = -out
        p = work[col][col]
        out *= p
        for j in range(col+1,len(work)):
            ratio = work[j][col]/p
            for k in range(col+1,len(work)):
                work[j][k] -= ratio*work[col][k]
    return out


def dec(q):
    return Decimal(q.numerator)/Decimal(q.denominator)


def main():
    folder = Path(__file__).resolve().parent
    h,g0,raw,norm = raw_profile()
    ell = Q(1,2)
    reflected = affine(raw,ell,-1)
    zero = [Q(0)]
    # y=norm*sqrt(2)*z on each half shell, u in [0,ell].
    pieces = [([norm],raw,reflected,zero),
              ([norm],zero,raw,reflected)]
    Xi = [[Q(0)]*4 for _ in range(4)]
    for y in pieces:
        for i in range(4):
            for j in range(4):
                Xi[i][j] += integrate(multiply(y[i],y[j]),0,ell)/(2*norm**2)
    J = integrate(multiply(raw,raw),0,ell)/norm**2
    K = integrate(multiply(raw,reflected),0,ell)/norm**2
    structured = [[Q(1,2),0,0,0],
                  [0,J/2,K/2,0],
                  [0,K/2,J,K/2],
                  [0,0,K/2,J/2]]
    assert Xi == structured
    assert J > 0 and J > abs(K)
    minors = []
    for size in range(1,5):
        for indices in combinations(range(4),size):
            value = determinant([[Xi[i][j] for j in indices] for i in indices])
            assert value > 0
            minors.append({'indices_zero_based':list(indices),'determinant':str(value)})
    shifted = [[Xi[i][j]-(Q(1,32) if i == j else 0)
                for j in range(4)] for i in range(4)]
    lower_minors = []
    for size in range(1,5):
        for indices in combinations(range(4),size):
            value = determinant([[shifted[i][j] for j in indices] for i in indices])
            assert value > 0
            lower_minors.append({'indices_zero_based':list(indices),'determinant':str(value)})
    # Gershgorin on the independent moving block certifies Xi<=I/2;
    # the stationary coordinate attains the upper eigenvalue exactly.
    assert J+abs(K) < Q(1,2)
    trace = sum(Xi[i][i] for i in range(4))
    assert trace == Q(1,2)+2*J and trace < 1
    # Plus directions are normalized (g+tau_s g)/sqrt2 in the orthonormal W.
    plus = {str(s):(Xi[0][0]+2*Xi[0][i]+Xi[i][i])/2
            for i,s in enumerate([0,Q(2),Q(5,2),Q(3)]) if i}
    with localcontext() as ctx:
        ctx.prec = 50
        radical = (dec(J*J+8*K*K)).sqrt()
        eigenvalues = sorted([Decimal('0.5'),dec(J)/2,
                              (3*dec(J)-radical)/4,(3*dec(J)+radical)/4])
        decimal_matrix = [[str(dec(q)) for q in row] for row in Xi]
        decimal_J,decimal_K = str(dec(J)),str(dec(K))
        decimal_trace = str(dec(trace))
        decimal_eigenvalues = [str(q) for q in eigenvalues]
    record = {
        'status':'EXACT_RATIONAL_COVARIANCE_AND_ALL_15_PRINCIPAL_MINORS_PASS',
        'date':'2026-10-03','model':'GPT-6 (Codex)',
        'serving_variant':'not exposed','reasoning_effort':'not exposed',
        'python_version':platform.python_version(),
        'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
        'shell':['2','3'],'translations':['0','2','5/2','3'],
        'source_support':['-1/4','1/4'],'autocorrelation_support':['-1/2','1/2'],
        'g0_coefficients':list(map(str,g0)),
        'norm_squared_g0':str(norm),
        'raw_autocorrelation_coefficients_nonnegative_u':list(map(str,raw)),
        'normalized_autocorrelation_coefficients_nonnegative_u':list(map(str,[c/norm for c in raw])),
        'raw_autocorrelation_degree':len(raw)-1,
        'J_integral_phi_squared':str(J),'K_integral_phi_times_reflection':str(K),
        'J_decimal_diagnostic':decimal_J,'K_decimal_diagnostic':decimal_K,
        'matrix_rational':[[str(q) for q in row] for row in Xi],
        'matrix_decimal_diagnostic':decimal_matrix,
        'all_principal_minors':minors,'rank':4,
        'strict_lower_shift':'1/32',
        'all_principal_minors_after_lower_shift':lower_minors,
        'upper_operator_bound':'1/2',
        'uniform_over_integer_shells':'Same Xi for every j>=2 with translations [0,j,j+1/2,j+1].',
        'eigenvalues_exact':['1/2','J/2','(3*J-sqrt(J^2+8*K^2))/4','(3*J+sqrt(J^2+8*K^2))/4'],
        'eigenvalues_decimal_diagnostic':decimal_eigenvalues,
        'plus_direction_integrals_rational':{s:str(q) for s,q in plus.items()},
        'trace_rational':str(trace),'trace_decimal_diagnostic':decimal_trace,
        'integrated_projection_residual_norm_squared':str(1-trace),
        'checks':['Independent direct g0 squared norm integral matches raw phi(0).',
                  'Integral phi on [0,1/2] is exactly zero.',
                  'Piecewise full 4x4 integration agrees with the J,K structured matrix.',
                  'All 15 rational principal minors are strictly positive.',
                  'All 15 rational principal minors of Xi-I/32 are strictly positive.',
                  'J+abs(K)<1/2 proves the upper operator bound by the moving block row sums.',
                  'Template W is L2 orthonormal: translates have disjoint interiors.',
                  'Trace is below one, as required by the projection Gram identity.'],
        'limitations':['Only continuous source-covariance geometry is calibrated.',
                       'No Sonin metric, K comparison, Weil positivity or growing-window loss is computed.',
                       'Decimal eigenvalues are diagnostics; exact minors certify positive definiteness.']
    }
    (folder/'result.json').write_text(json.dumps(record,indent=2)+'\n')
    lines = [
        '# Exact common-shell source covariance, 2<=r<=3',
        '',
        '3 October 2026. Prepared for Edward Baker with substantial LLM assistance.',
        'Model: GPT-6 (Codex); exact serving variant and configured effort not exposed.',
        'Python standard-library rational arithmetic; no Sonin loss or Weil positivity claim.',
        '',
        'Use g0=-h\'\'\'+h\'/4, h=(1-16x^2)^8 on |x|<1/4, and g=g0/||g0||.',
        'Its norm squared is '+str(norm)+'. The autocorrelation is even, supported',
        'on [-1/2,1/2], and its nonnegative branch is an exact degree-31 rational',
        'polynomial regenerated by the script. All coefficients are in result.json.',
        '',
        'For W=[g,tau_2 g,tau_(5/2) g,tau_3 g] and F_r=(g+tau_r g)/sqrt2,',
        'z=W*F_r has two exact branches. With u in [0,1/2], they are',
        '(1,phi(u),phi(1/2-u),0)/sqrt2 and',
        '(1,0,phi(u),phi(1/2-u))/sqrt2.',
        '',
        'Write J=integral_0^(1/2)phi(u)^2 du and',
        'K=integral_0^(1/2)phi(u)phi(1/2-u)du. Then',
        '',
        '    Xi = [[1/2,0,0,0],',
        '          [0,J/2,K/2,0],',
        '          [0,K/2,J,K/2],',
        '          [0,0,K/2,J/2]].',
        '',
        'The exact fractions are:',
        '',
        '    J = '+str(J),
        '    K = '+str(K),
        '',
        'Diagnostic decimals: J='+decimal_J+', K='+decimal_K+'.',
        'J>|K| was checked exactly; all 15 rational principal minors are positive.',
        'Rank is four. Exact eigenvalues are 1/2, J/2, and',
        '(3J plus/minus sqrt(J^2+8K^2))/4.',
        'Their diagnostic ascending decimals are '+', '.join(decimal_eigenvalues)+'.',
        '',
        'The off-diagonal entries involving the stationary g vanish exactly:',
        'they are multiples of integral_0^(1/2)phi=0. Adjacent moving templates',
        'have small but nonzero signed covariance K/2; the two endpoints have',
        'zero covariance because their moving overlap profiles have disjoint interiors.',
        '',
        'For the normalized plus templates (g+tau_s g)/sqrt2:',
        '',
    ]
    for s,q in plus.items():
        lines.append('    s='+s+': integral_2^3 |<plus_s,F_r>|^2 dr = '+str(q))
    lines += ['',
              'W is orthonormal. The total captured average source energy is',
              'Tr Xi=1/2+2J='+str(trace)+' (diagnostic '+decimal_trace+').',
        'The integrated orthogonal residual norm squared is 1/2-2J='+str(1-trace)+'.',
              '',
              'The same covariance holds on every integer shell [j,j+1], j>=2,',
              'with W_j=[g,tau_j g,tau_(j+1/2) g,tau_(j+1) g]. Exactly',
              'Xi>(1/32)I and Xi<=(1/2)I: the first is certified by all 15 rational',
              'principal minors after subtracting I/32; the second follows from',
              'J+|K|<1/2 and the independent stationary eigenvalue 1/2.',
              'For any positive four-template coefficient matrix Lambda_j,',
              '',
              '    (1/32)Tr Lambda_j < Tr(Lambda_j Xi) <= (1/2)Tr Lambda_j',
              '',
              'when Lambda_j is nonzero. Also ||z(r)||^2<=1 by orthonormality, so',
              'the pointwise template loss z(r)*Lambda_j z(r) is at most',
              'Tr Lambda_j < 32 Tr(Lambda_j Xi). Thus a polynomial shell average',
              'within this fixed template family also implies a polynomial pointwise',
              'bound. Averaging here does not conceal arbitrarily narrow large peaks.',
              '',
              'Reproduce with python3 calculate.py. The script and result are standalone;',
              'all derived files are small. These source overlaps do not certify relative',
              'Schur tail positivity, source-weighted correction loss, or polynomial growth.',
              'The source energy metric B and its inverse have not been computed.']
    (folder/'RESULT.md').write_text('\n'.join(lines)+'\n')
    print(json.dumps({'status':record['status'],'J':decimal_J,'K':decimal_K,
                      'rank':4,'trace':decimal_trace,'eigenvalues':decimal_eigenvalues,
                      'result_json_bytes':(folder/'result.json').stat().st_size,
                      'result_note_bytes':(folder/'RESULT.md').stat().st_size}))


if __name__ == '__main__':
    main()
