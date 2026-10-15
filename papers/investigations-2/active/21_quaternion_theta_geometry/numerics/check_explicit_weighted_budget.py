#!/usr/bin/env python3
"""Exact arithmetic audit of explicit PR01 elementary budgets.

Prepared for Edward Baker with substantial LLM assistance. Recorded
coordinating model: gpt-6.1-sol; recorded reasoning effort: ultra, verified
by the coordinating conversation.

This checks finite rational arithmetic, not exponent-pair theorems, global
transcendental inequalities, or a numerical all-height sign threshold.
"""
from fractions import Fraction as F
from pathlib import Path
import argparse
import hashlib
import json

checks = []
def record(name, result):
    assert result, name
    checks.append(name)

def textq(q):
    return str(q.numerator) if q.denominator == 1 else f"{q.numerator}/{q.denominator}"

rho = eta = F(1, 100000)
theta = F(61, 24)
theta0 = theta - rho / 100
mu = F(21807, 254720000)
lam = mu - F(63, 50) * rho
L0, ell0, U0 = 100002, 100001, 10**12
record('explicit disc delta at lower L and u bounds', F(1,2*L0) + F(3,4*U0) < rho/2)
record('explicit theta displacement', F(1,2*L0*U0) < rho/100)
record('shrinking disc loses less than one log-height unit', F(1,L0*U0) < 1)
record('elementary x lower bound via exponential sixth term', F(L0**6,60) - F(1,L0) > U0)
record('real-part zeta half-plane', F(1,2) + theta0/4 - rho/2 > F(9,8))
record('low-index exponent at least one plus one over 121', F(1,2) + theta0/5 - rho/2 > 1 + F(1,121))
record('regular-block perturbation inside reserved loss', 1 + F(1,4) + F(1,1600) < F(63,50))
record('improved saving exceeds one over 14000', lam > F(1,14000))
record('improved saving exceeds previous exact margin', lam > F(76399,1273600000))
record('exceptional final block remains strictly paid', F(11,2688) - rho*(1+F(1,1600)+F(33,128)) - F(1,32768) > F(1,300))
record('exceptional final saving exceeds regular saving', F(1,300) > lam)
record('final extension shorter than a half-log-two grid spacing', F(1,64) < F(1,2))
record('carrier path logarithmic derivative norm budget', (F(L0,4)+F(3,4))*(1+F(1,2*U0)) < F(L0,3))
record('carrier alpha-prime rational bound', F(1,U0)+F(6,U0**2) <= F(2,U0))
record('carrier alpha norm residual bound using pi less than 22 over 7', F(11,14)+F(3,U0)+F(1,U0**2) < 1)
record('EP scaling exponent below one sixth', F(13,84)+eta < F(1,6))
record('EP scaling conversion fourth power bound', 4*F(22,7) < 64)
record('EP phase range from T greater than u over 3', F(U0**2,9) > F(22,7)*U0 + F(22,7)**2/8)
record('T lies between u over 3 and u', F(22,7)/16 + F(3,4*U0) < F(U0,6))
record('weighted monotonicity r-zero', -F(1,2)+rho/2+F(1,256) < 0)

pairs = [
    (F(13,414), F(359,414), F(1,5), F(3,10)),
    (F(13,194), F(76,97), F(3,10), F(3,8)),
    (F(18,199), F(593,796), F(3,8), F(81,200)),
    (F(4742,38463), F(35731,51284), F(81,200), F(3,7)),
    (F(13,84), F(55,84), F(3,7), F(1,2)),
]
widths = []
for j, (k,l,a,b) in enumerate(pairs):
    widths.append(b-a)
    for endpoint, label in ((a,'left'),(b,'right')):
        exponent = k + (l-k-F(1,2))*endpoint-theta*endpoint*(1-endpoint)/4
        record(f'fixed assigned pair {j} {label} endpoint margin', exponent <= -mu)
    c = theta*(b-a)/8
    record(f'fixed assigned interval {j} curvature coefficient', c == F(61,192)*(b-a))
G = F(962773,671)
record('geometric rational multiplier arithmetic', 11+F(768,61)*sum(1/d for d in widths) == G)
record('geometric multiplier below 1435', G < 1435)
D1, D2 = 121**2+1, 2*121**3+4
A0 = (theta*D2+2*D1)/4
record('low-index r-zero coefficient', A0 == F(36138917,16))
record('low-index uniform theta factor uses 5 over e below 2', 1+1+F(1,2)+F(1,6) > F(5,2))
record('RS per-index multiplier numerator', F(ell0**2,64)+F(313,500) < ell0**2)
record('RS per-index exponent below one via sixth exponential term', F(120,ell0**4) < 1)
record('RS extra gamma exponent below one tenth', F(1,50*L0)+F(1,2*(U0-6))+F(1,64*L0) < F(1,10))
record('RS positive weight exponential below one half', F(3,4)*F(60,ell0**5) < F(1,2))
record('RS C-error correction below one via Taylor bounds', F(480,ell0**3)+F(720,ell0**5) < 1)
record('RS C-error exponent exceeds two fifths', F(1,4)+theta0/16 > F(2,5))
record('RS C-error second numerator', 3*F(22,7)/2+F(261,25) < ell0)
record('RS C-error first correction coefficient', F(31,25)*4*2 < 10)
record('analytic elementary error norm coefficients', 2*2 == 4 and 2*8 == 16 and 2*3 == 6)
record('third normalized Cauchy multiplier', F(6*4**3,2)*9 == 1728)
record('RS polynomial-exponential term decreasing on log domain', ell0 > F(8,3))

payload = {
    'schema': 'inv21-explicit-weighted-budget-v1',
    'date': '2026-10-15',
    'prepared_for': 'Edward Baker',
    'llm_assistance': 'substantial LLM assistance',
    'recorded_model': 'gpt-6.1-sol',
    'recorded_effort': 'ultra',
    'metadata_provenance': 'Verified by the coordinating conversation.',
    'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'assertion_count': len(checks),
    'assertions': checks,
    'constants': {'rho': textq(rho), 'eta': textq(eta), 'theta_star': textq(theta),
                  'L_min': L0, 'ell_min': ell0, 'u_min_sufficient': U0,
                  'lambda': textq(lam), 'lambda_decimal_diagnostic': float(lam),
                  'G_rational_upper_bound': textq(G), 'A0': textq(A0),
                  'C_EP': 'unevaluated; never replaced by one'},
    'scope': 'Finite exact rational bookkeeping only. Infinite-sum, analytic-disc, Abel, and primary-theorem arguments are in the note. No numerical starting height, middle saving, sign-domain extension, or RH result.'
}
parser = argparse.ArgumentParser()
parser.add_argument('--output', required=True)
args = parser.parse_args()
Path(args.output).write_text(json.dumps(payload, indent=2, sort_keys=True)+'\n')
print(f'{len(checks)} exact rational assertions passed')
