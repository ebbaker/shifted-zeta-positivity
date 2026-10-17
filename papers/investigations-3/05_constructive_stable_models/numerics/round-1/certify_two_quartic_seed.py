#!/usr/bin/env python3
"""Bounded same-model preparation; no theta-realization claim.

2026-10-17. Prepared for Edward Baker with substantial LLM assistance.
Recorded parent model: gpt-6.1-sol (Codex); reasoning effort: ultra.
The initial numerical scout preceded the declared retained-run contract.
The retained calculation below reruns the exact fixed domain and budget;
its contract is not represented as having preceded that initial scout.

For joint (X,Y) density proportional
exp[-x^4-y^4+(7/2)(x^2+y^2)+xy], the marginal density f(s) of
S=X+Y has potential V(s)=-log f(s).
The s^6 coefficient equals (9/2) kappa_3(W), W=U^2, where
U has density proportional exp[-2(U^2-3/2)^2].

Compute on [0,4] by Acb rigorous analytic integration; bound tails by
exp(-128)/32 for every integral of U^(2k), k=0,1,2,3.  For u>=4:
exp[-2(u^2-3/2)^2] <= exp(-u^4), u^(2k)<=exp(u^4/2),
and u^4/2>=32u.  Hence the tail bound.  Symmetry removes the
factor two from all ratios.
"""
import argparse
import hashlib
import json
import pathlib
import sys
import flint
from flint import acb, arb, ctx

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--output', type=pathlib.Path)
args = parser.parse_args()

# Retained-run contract, set before any evaluations.  Four integrals only.
# Each integral has relative and absolute goal 2^-130 and at most 100,000
# evaluations with depth limit 100.  Final kappa3 radius must be <2^-100.
ctx.prec = 160
contract = {
    'integral_count': 4,
    'integration_domain': [0, 4],
    'precision_bits': 160,
    'integration_tolerance_bits': 130,
    'eval_limit_per_integral': 100000,
    'depth_limit_per_integral': 100,
    'requested_final_kappa3_radius_bits': 100,
    'termination': 'fixed four calls; no precision or domain refinement',
}
tail = arb(-128).exp() / 32
vals = []
for k in range(4):
    value = acb.integral(
        lambda z, analytic: z**(2*k) * (-2*(z*z-arb(3)/2)**2).exp(),
        0, 4, rel_tol=arb(2)**-130, abs_tol=arb(2)**-130,
        eval_limit=100000, depth_limit=100)
    assert value.imag.contains(0)
    vals.append(value.real + arb(tail/2, tail/2))
mom = [v / vals[0] for v in vals]
kappa = mom[3] - 3*mom[2]*mom[1] + 2*mom[1]**3
v6 = arb(9)/2 * kappa
assert kappa < 0
assert kappa.rad() < arb(2)**-100
record = {
    'date': '2026-10-17',
    'prepared_for': 'Edward Baker',
    'llm_assistance': 'Substantial LLM assistance; same-model research preparation, not formal review.',
    'recorded_parent_model': 'gpt-6.1-sol (Codex)',
    'recorded_reasoning_effort': 'ultra',
    'scout_and_retained_run': 'Initial numerical scout preceded the declared retained-run contract; only this fixed-contract rerun is retained as the certificate. The contract is not claimed to have preceded the scout.',
    'status': 'rigorous interval calculation; same-model preparation',
    'contract': contract,
    'source_sha256': hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
    'source_filename': pathlib.Path(__file__).name,
    'python_version': sys.version.split()[0],
    'python_flint_version': flint.__version__,
    'flint_version': flint.__FLINT_VERSION__,
    'precision_bits': ctx.prec,
    'parameters': {'alpha': 1, 'beta': '-7/2', 'K': 1},
    'readout': 'S=X+Y, two quartic site laws coupled by +XY',
    'domain': 'four Acb integrations on [0,4], analytic entire integrands',
    'tail_bound_each': str(tail),
    'integrals_0_2_4_6': [str(v) for v in vals],
    'moments_of_W': [str(v) for v in mom],
    'kappa3_W': str(kappa),
    'potential_coefficient_s6': str(v6),
    'scope': 'Shows this explicit interacting stable marginal escapes nonnegative higher-potential-coefficient cone; no theta matching or limit.'
}
formatted = json.dumps(record, indent=2) + '\n'
if args.output:
    args.output.write_text(formatted)
else:
    print(formatted, end='')
