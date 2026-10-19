#!/usr/bin/env python3
"""Exact contract checks and source pins; no theta estimate or consumer.

Prepared for Edward Baker with LLM assistance, 19 October 2026.
Execution model and effort are supplied explicitly in the receipt.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path

INV = Path('papers/investigations-3/11_arithmetic_collision_rigidity')
SYM = INV / 'symmetries'
NOTE = SYM / 'notes/07_UAR01_CORRECTED_RESIDUAL_AND_TRANSITION_CONTRACT_20261019.md'
SCRIPT = SYM / 'numerics/check_uar01_contract.py'
SOURCES = [NOTE, SCRIPT,
    SYM/'research-overview/03_UNIFORM_ARITHMETIC_RESIDUAL_RESEARCH_PROGRAM_20261019.md',
    SYM/'03_normalized_jet_rotation/notes/03_FILTERED_COMPLETE_RESIDUAL_AND_SPLIT_PREFIX_OBSTRUCTION_20261019.md',
    SYM/'03_normalized_jet_rotation/notes/06_ARITHMETIC_GAMMA_AND_EDGE_CORRECTIONS_20261019.md',
    SYM/'03_normalized_jet_rotation/notes/07_COMPLETE_ARITHMETIC_EDGE_AND_RESIDUAL_INCREMENT_20261019.md',
    SYM/'04_time_height_scaling/notes/01_PHASE_RETAINING_FULL_CUTOFF_SCALING_20261018.md',
    SYM/'04_time_height_scaling/notes/03_UNIFORM_LOCAL_RESIDUAL_TRANSFER_AND_CUTOFF_PAYMENT_OBSTRUCTION_20261019.md',
    SYM/'02_cutoff_reflection/notes/01_ANALYTIC_CUTOFF_CORRECTION_AND_COMPLETE_JET_ERRORS_20261018.md',
    Path('papers/quasi-rh/quasi-rh-exponent-descent/newman_collisions/17_enlarged_state_transport/notes/22_THETA_CUTOFF_MATCHING_AND_UNIFORM_PHYSICAL_JETS_20261011.md'),
    Path('result-summaries/12_collision_controls_and_screening.md')]

def check(ok, message):
    if not ok:
        raise ArithmeticError(message)

def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def validate_pins(repo, pins):
    check(set(pins) == {str(p) for p in SOURCES}, 'missing or extra source pin')
    for name, expected in pins.items():
        p = repo/name
        check(p.is_file() and not p.is_symlink(), 'missing/linked source: '+name)
        check(digest(p) == expected, 'stale source: '+name)

def domain(t, kappa):
    check(isinstance(t, F) and isinstance(kappa, F), 'use exact rational parameters')
    check(0 < t <= F(1, 20) and 1 <= kappa <= 2, 'outside sector')
    return t/kappa

def reject(call):
    try:
        call()
    except (ArithmeticError, FileNotFoundError):
        return True
    raise ArithmeticError('invalid fixture accepted')

# Small exact bivariate polynomial algebra, keys (x degree, t degree).
def add(*polys):
    out = {}
    for p in polys:
        for k, v in p.items():
            out[k] = out.get(k, F(0))+v
    return {k:v for k,v in out.items() if v}

def scale(p, v):
    return {k:a*v for k,a in p.items() if a*v}

def mul(p, q):
    out = {}
    for (a,b),v in p.items():
        for (c,d),w in q.items():
            k = (a+c,b+d)
            out[k] = out.get(k,F(0))+v*w
    return {k:v for k,v in out.items() if v}

def diff(p, axis):
    out = {}
    for k,v in p.items():
        if k[axis]:
            j = list(k); j[axis] -= 1
            out[tuple(j)] = v*k[axis]
    return out

def exact_checks():
    # (1+q^2)/(q+q^-1)=q after multiplying through.
    check({0:F(1),2:F(1)} == {k+1:v for k,v in {-1:F(1),1:F(1)}.items()},
          'profile shift Laurent identity')
    # p=-1-2d gives p^2/2+p+3/8 = 2d^2-1/8.
    p = {(0,0):F(-1),(1,0):F(-2)}
    phase = add(scale(mul(p,p),F(1,2)),p,{(0,0):F(3,8)})
    check(phase == {(2,0):F(2),(0,0):F(-1,8)}, 'jump phase identity')
    parity = []
    for n in [3,4,8,9,22066]:
        check((-1)**(n+1) == -(-1)**n, 'adjacent parity')
        parity.append(n)
    # S=I/i. Use arbitrary endpoint jet coordinates, chartwise r=Q-f.
    Q = [F(2),F(-3),F(5),F(7)]
    f = [[F(1),F(8)],[F(-2),F(4)],[F(6),F(-1)]]
    sewn = []
    for count in range(1,4):
        local = sum((Q[j+1]-f[j][1])-(Q[j]-f[j][0]) for j in range(count))
        jumps = sum(f[j][0]-f[j-1][1] for j in range(1,count))
        endpoint = (Q[count]-f[count-1][1])-(Q[0]-f[0][0])
        check(local == endpoint+jumps, 'residual sewing sign')
        check(Q[count]-Q[0] == f[count-1][1]-f[0][0]-jumps+local,
              'physical propagation sign')
        if count > 1:
            check(local != endpoint-jumps, 'wrong-sign mutation not detected')
        sewn.append(str(local))
    check(abs(F(5)+F(-5)) == 0 and abs(F(5))+abs(F(-5)) == 10,
          'signed transition counterexample')
    A = {(0,0):F(2),(2,0):F(1),(0,1):F(3)}
    q = {(0,0):F(1),(1,0):F(2),(2,1):F(-1)}
    H = mul(A,q)
    lhs = add(diff(H,1),diff(diff(H,0),0))
    rhs = add(mul(A,add(diff(q,1),diff(diff(q,0),0))),
              scale(mul(diff(A,0),diff(q,0)),F(2)),
              mul(add(diff(A,1),diff(diff(A,0),0)),q))
    check(lhs == rhs, 'normalized heat product rule')
    check(lhs != add(rhs,scale(mul(diff(A,1),q),F(-1))), 'missing time forcing mutation')
    check(lhs != add(rhs,scale(mul(diff(diff(A,0),0),q),F(-1))),
          'missing normalizer curvature mutation')
    # H=x^2+2(1-t), A=1, f=Q=H: r=0 at an actual polynomial heat event.
    eventH = {(2,0):F(1),(0,0):F(2),(0,1):F(-2)}
    check(add(diff(eventH,1),diff(diff(eventH,0),0)) == {}, 'control heat equation')
    check(eventH[(0,0)]+eventH[(0,1)] == 0, 'event value at t=1,x=0')
    check(all(a != 1 or b != 0 for a,b in eventH), 'event first derivative at x=0')
    for t,k in [(F(1,20),F(1)),(F(1,20),F(2)),(F(1,100),F(3,2))]:
        check(0 < domain(t,k) <= F(1,20), 'chart radius')
    invalid = [(F(0),F(1)),(F(-1),F(1)),(F(1,19),F(1)),
               (F(1,20),F(1,2)),(F(1,20),F(3)),(0.05,F(1))]
    for t,k in invalid:
        reject(lambda t=t,k=k:domain(t,k))
    return {'profile_shift':'exact Laurent identity; analytic removable extension proved in note',
        'jump_phase':'exact rational polynomial identity','parity_fixtures':parity,
        'sewing_prefix_values_I_over_i':sewn,'wrong_transition_sign_rejected':True,
        'opposing_transition_fixture':'signed sum 0, independent radii sum 10',
        'normalized_heat_product_rule':True,'forcing_omission_mutations_rejected':True,
        'own_source_polynomial_event':'zero residual with zero physical first jet; no exclusion inferred',
        'invalid_domain_fixtures_rejected':len(invalid)}

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--repo',type=Path,required=True)
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument('--write-record',type=Path)
    g.add_argument('--verify',type=Path)
    p.add_argument('--model')
    p.add_argument('--effort')
    args = p.parse_args(); repo=args.repo.resolve()
    checks=exact_checks()
    if args.verify:
        record=json.loads(args.verify.read_text())
        check(record['status']=='contract_only_no_new_estimate','wrong record scope')
        validate_pins(repo,record['source_sha256'])
        check(record['checks']==checks,'algebra replay mismatch')
        print(json.dumps({'status':'verified','source_pins':len(SOURCES),'scope':record['status']}))
        return
    check(bool(args.model) and bool(args.effort),'actual execution metadata required')
    pins={str(path):digest(repo/path) for path in SOURCES}
    validate_pins(repo,pins)
    reject(lambda:validate_pins(repo,{}))
    stale=dict(pins); stale[str(NOTE)]='0'*64
    reject(lambda:validate_pins(repo,stale))
    reject(lambda:validate_pins(repo/'nonexistent_contract_fixture',pins))
    record={'date':'2026-10-19','prepared_for':'Edward Baker','model':args.model,
        'effort':args.effort,'LLM_assistance':True,'status':'contract_only_no_new_estimate',
        'arithmetic':'Python standard-library exact rational polynomial/linear fixtures',
        'source_sha256':pins,'checks':checks,
        'source_guards':{'missing_pins_rejected':True,'stale_pin_rejected':True,'missing_files_rejected':True},
        'limitations':['Algebra fixtures do not prove imported analytic theorems.',
            'No theta quadrature, uniform residual constant, anchor, physical acceptance or coverage certificate.',
            'Separate same-model LLM review is not implementation-independent or specialist human review.']}
    args.write_record.write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps({'status':'record_written','path':str(args.write_record),'source_pins':len(SOURCES)}))

if __name__=='__main__':
    main()
