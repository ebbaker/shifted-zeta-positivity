#!/usr/bin/env python3
"""One fixed analytic interval budget, without evaluating physical integrals.

Prepared for Edward Baker with substantial LLM assistance, 2026-10-17.
Actual recorded model gpt-6.1-sol; reasoning effort ultra.
The selected height is determined by the determinant formula before the
coefficient positivity bound is evaluated. No height or support search.
"""
import argparse
import hashlib
import json
import math
from pathlib import Path
import platform
import resource
import time

# On this macOS host, lowering RLIMIT_AS or RLIMIT_DATA is unsupported.
# The finite polynomial calculation reports observed peak resident memory.
from flint import arb, ctx, __version__ as flint_version

ctx.prec = 320
START = time.monotonic()
T = arb(1) / 4
P0 = {(0, 2, 0): 2, (0, 1, 0): -3}


def advance(poly):
    """P' = d_u P + 4q d_q P + (2tu+1-4q)P, exactly over Z."""
    result = {}
    def add(key, val):
        result[key] = result.get(key, 0) + val
    for (j, k, ell), coeff in poly.items():
        if j:
            add((j-1, k, ell), j*coeff)
        add((j, k, ell), (4*k+1)*coeff)
        add((j+1, k, ell+1), 2*coeff)
        add((j, k+1, ell), -4*coeff)
    return {key: val for key, val in result.items() if val}


def derivatives(initial, count):
    result = [initial]
    for _ in range(count):
        result.append(advance(result[-1]))
    return result


GP = derivatives(P0, 7)
UGP = derivatives({(j+1, k, ell): c for (j,k,ell), c in P0.items()}, 7)
Q = [arb.pi()*n*n for n in (1,2,3)]
BETA = [(4*q-1)*(-q).exp() for q in Q]
V2 = [-BETA[1]/BETA[0], arb(1), arb(0)]
V3 = [-BETA[2]/BETA[0], arb(0), arb(1)]


def endpoint_coefficients(direction, order):
    result = {}
    for d, q in zip(direction, Q):
        for (j, k, ell), coeff in GP[order].items():
            if j == 0:
                result[ell] = result.get(ell, arb(0)) + d*(-q).exp()*coeff*q**k
    return result


def endpoint(direction, order):
    return endpoint_coefficients(direction, order).get(0, arb(0))


ELL_A = endpoint(V2, 1)
ELL_V3 = endpoint(V3, 1)
assert not ELL_A.contains(0)
RHO = ELL_V3 / ELL_A
A = V2
B = [v3-RHO*v2 for v2,v3 in zip(V2,V3)]
a = -endpoint(A, 1)
b = endpoint(B, 3)
assert not b.contains(0)


def endpoint_sup(direction, order):
    """Triangle polynomial majorant, after summing the node contributions."""
    terms = endpoint_coefficients(direction, order)
    return sum((abs(c)*T**ell for ell,c in terms.items()), arb(0)).upper()


GAMMA_CACHE = {}
def monomial_integral_majorant(node, j, k):
    """Note02 Eq(6), with exact integer powers and Arb incomplete gamma."""
    key = node,j,k
    if key not in GAMMA_CACHE:
        q = Q[node]
        c = 1-T/(8*q)
        s = arb(k)+arb(1)/2
        GAMMA_CACHE[key] = (math.factorial(j)/(4*q.sqrt())
                                 * c**(-s) * (c*q).gamma_upper(s))
    return GAMMA_CACHE[key]


def derivative_l1_majorant(direction, poly):
    total = arb(0)
    for node,d in enumerate(direction):
        for (j,k,ell), coeff in poly.items():
            total += abs(d)*abs(coeff)*T**ell*monomial_integral_majorant(node,j,k)
    return total.upper()


def bounds(direction, p):
    endpoint_bound = endpoint_sup(direction, p+1)
    gnorm = derivative_l1_majorant(direction, GP[p+2])
    ugnorm = derivative_l1_majorant(direction, UGP[p+3])
    E = (endpoint_bound+gnorm).upper()
    F = ((p+2)*endpoint_bound+ugnorm).upper()
    return E,F,endpoint_bound,gnorm,ugnorm


EA,FA,endA,normA,unormA = bounds(A,2)
EB,FB,endB,normB,unormB = bounds(B,4)
AA = abs(a).upper()
BB = abs(b).upper()
L = (2*abs(a)*abs(b)).lower()
assert L > 0
K2 = (AA*FB+4*BB*EA+BB*FA+2*AA*EB).upper()
K4 = (EA*FB+EB*FA).upper()
XD = ((K2+(K2*K2+2*L*K4).sqrt())/L).sqrt().upper()
KD = ((AA+EA)**2+(2*AA+FA)**2+(BB+EB)**2+(4*BB+FB)**2).sqrt().upper()
row_norms = [(da*da+db*db).sqrt().upper() for da,db in zip(A,B)]
PNORM = max(row_norms)
PREFACTOR = (12*KD*PNORM/(5*L)).upper()

# This formula selects the sole test height before coefficient evaluation.
X = max(1,int(XD.ceil().unique_fmpz()))+1
X_RULE = 'X = max(1, ceil(upper(X_D))) + 1; no height search'
X_ARB = arb(X)
MONOTONIC_ONSET = (80/arb.pi()).upper()
assert X_ARB > MONOTONIC_ONSET
DET_RELATIVE_REMAINDER = (K2/(L*X_ARB**2)+K4/(L*X_ARB**4)).upper()
assert DET_RELATIVE_REMAINDER < arb(1)/2
LOG_DELTA_BOUND = (PREFACTOR.log()+5*X_ARB.log()-arb.pi()*X_ARB/16).upper()
DELTA_BOUND = (PREFACTOR*X_ARB**5*(-arb.pi()*X_ARB/16).exp()).upper()
assert DELTA_BOUND < arb(1)/2
assert DELTA_BOUND < arb('4e-307')

# The two pre-existing measurement designs, restricted to the three free
# nodes. These are coefficient-to-measurement norm bounds, not new heights.
REC_MEASUREMENT_NORM = arb(35).sqrt().upper()
reflection_sum = arb(0)
def phi(q, u):
    z=q*(4*u).exp()
    return (u-z).exp()*(2*z*z-3*z)
for j in range(1,13):
    u=arb(j)/20
    row=sum((abs(phi(q,u)-phi(q,-u)) for q in Q),arb(0))
    reflection_sum += row*row
REF_MEASUREMENT_NORM = reflection_sum.sqrt().upper()
assert REC_MEASUREMENT_NORM<arb('5.917') and REF_MEASUREMENT_NORM<arb('1.916')

# Short outward decimal constants make the final inequalities independently
# readable without relying on equality comparisons between printed balls.
DEC_L=arb('5.47332689e-5')
DEC_K2=arb('418.436649');DEC_K4=arb('10985380.865')
DEC_KD=arb('59364.960794');DEC_P=arb('1.000000000003')
assert L>DEC_L and K2<DEC_K2 and K4<DEC_K4 and KD<DEC_KD and PNORM<DEC_P
DEC_REM=DEC_K2/(DEC_L*X_ARB**2)+DEC_K4/(DEC_L*X_ARB**4)
DEC_DELTA=12*DEC_KD*DEC_P/(5*DEC_L)*X_ARB**5*(-arb.pi()*X_ARB/16).exp()
assert DEC_REM<arb(1)/2 and DEC_DELTA<arb('4e-307')
assert 12*DEC_KD*DEC_P/(5*DEC_L)<arb('2.603095134e9')


def bs(value):
    return value.str(80,more=True)


record = {
    'status': 'Arb interval evaluation of one fixed analytic sufficient bound; no physical integrals',
    'prepared_for': 'Edward Baker',
    'LLM_assistance': 'substantial',
    'recorded_model': 'gpt-6.1-sol',
    'recorded_reasoning_effort': 'ultra',
    'date': '2026-10-17',
    'python_flint_version': flint_version,
    'python_version': platform.python_version(),
    'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'arb_precision_bits': ctx.prec,
    'contract': {'N':3,'T':'1/4','tail':'theta','normalization':'beta.delta = 0',
                 'anchor':False,'p':2,'r':4,
                 'directions':'A=v2; B=v3-rho*v2; vj=ej-(beta_j/beta_1)e1; rho=f_v3_prime(0)/f_v2_prime(0)',
                 'height_selection':X_RULE,
                 'limits':{'wall_seconds':120,'memory_MiB':512},
                 'height_grid':False,'support_sweep':False,'physical_integrals':False},
    'beta':list(map(bs,BETA)),
    'A':list(map(bs,A)), 'B':list(map(bs,B)), 'rho':bs(RHO),
    'leading':{'a':bs(a),'b':bs(b),'A_f_prime':bs(ELL_A),
               'B_f_prime_interval_check':bs(endpoint(B,1)),
               'B_f_prime_exact_reason':'zero identically by rho definition; interval encloses 0'},
    'remainder_components':{
        'A_endpoint_order3_sup':bs(endA),'A_g_order4_L1_majorant':bs(normA),
        'A_ug_order5_L1_majorant':bs(unormA),
        'B_endpoint_order5_sup':bs(endB),'B_g_order6_L1_majorant':bs(normB),
        'B_ug_order7_L1_majorant':bs(unormB)},
    'remainder_constants':{'E_A':bs(EA),'F_A':bs(FA),'E_B':bs(EB),'F_B':bs(FB)},
    'determinant':{'L_lower':bs(L),'K2_upper':bs(K2),'K4_upper':bs(K4),
                   'X_D_upper':bs(XD),'X':X,
                   'relative_remainder_at_X_upper':bs(DET_RELATIVE_REMAINDER)},
    'positivity':{'K_D_upper':bs(KD),'P_2_to_infinity_upper':bs(PNORM),
                  'prefactor_upper':bs(PREFACTOR),'monotonic_onset_upper':bs(MONOTONIC_ONSET),
                  'delta_sup_at_X_upper':bs(DELTA_BOUND),
                  'natural_log_delta_sup_upper':bs(LOG_DELTA_BOUND),
                  'for_every_x_ge_X':True,'for_every_t_in_0_quarter':True,
                  'coefficient_lower_bound':'1 - delta_sup_at_X_upper > 1/2'},
    'absolute_measurement_bounds':{
        'units':'original raw Euclidean row norms; same two declared designs',
        'recurrence_inf_to_2_bound':bs(REC_MEASUREMENT_NORM),
        'reflection_inf_to_2_bound':bs(REF_MEASUREMENT_NORM),
        'recurrence_at_X_upper':bs((REC_MEASUREMENT_NORM*DELTA_BOUND).upper()),
        'reflection_at_X_upper':bs((REF_MEASUREMENT_NORM*DELTA_BOUND).upper()),
        'uniform_for_x_ge_X':True},
    'short_outward_certificate':{
        'L_lower':'5.47332689e-5','K2_upper':'418.436649','K4_upper':'10985380.865',
        'K_D_upper':'59364.960794','P_norm_upper':'1.000000000003',
        'relative_determinant_error_at_3915':bs(DEC_REM),
        'coefficient_change_bound_at_3915':bs(DEC_DELTA),
        'strict_checks':'all outward rounded constants bound the computed expressions; determinant error<1/2, coefficient bound<4e-307'},
    'proof_inputs':{'derivative_recurrence':'P_{k+1}=d_uP_k+4q d_qP_k+(2tu+1-4q)P_k',
                    'monomial_majorant':'j!/(4sqrt(a_n))*c_n^(-k-1/2)*Gamma(k+1/2,c_n*a_n); c_n=1-T/(8*a_n)',
                    'complete_theta_twojet_bound':'(6/5)*exp(-pi*x/16)',
                    'determinant_onset':'X_D^2=(K2+sqrt(K2^2+2*L*K4))/L',
                    'delta_sup_bound':'(12*K_D*||P||_2toinf/(5*L))*x^5*exp(-pi*x/16)'},
    'scope':'Fixed normalized unanchored N=3 theta-tail perturbations; nearby exact double jets. No height-optimality or nondegeneracy is asserted.',
    'elapsed_seconds':time.monotonic()-START,
    'peak_resident_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss*(1024 if platform.system()=='Linux' else 1),
}
assert record['peak_resident_bytes'] < 512*1024**2
assert record['elapsed_seconds'] < 120
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--output',type=Path,required=True)
output=parser.parse_args().output
output.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({key:record[key] for key in ('leading','remainder_constants','determinant','positivity','elapsed_seconds')},indent=2))
