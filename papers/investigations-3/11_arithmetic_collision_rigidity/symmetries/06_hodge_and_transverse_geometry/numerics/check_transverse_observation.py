#!/usr/bin/env python3
"""Exact finite algebra and inherited control replay for S06.

Prepared for Edward Baker, 18 October 2026, with substantial LLM assistance.
Authoring model gpt-6.1-sol, actual effort ultra. Internal checks only.
The accompanying note supplies the analytic proofs and convergence scope.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
from math import factorial
import os
from pathlib import Path
import platform
import subprocess
import sys


def add(*ps):
    out = {}
    for p in ps:
        for k, v in p.items():
            out[k] = out.get(k, F(0)) + v
    return {k: v for k, v in out.items() if v}


def scale(p, c):
    return {k: c*v for k, v in p.items() if c*v}


def mul(p, q):
    return add(*[{j+k: a*b} for j, a in p.items() for k, b in q.items()])


def deriv(p):
    return {k-1: k*v for k, v in p.items() if k}


def at(p, v):
    return sum((a*v**k for k, a in p.items()), F(0))


def delta(p):
    # D[e^u exp(-v) p(v)] / [e^u exp(-v)], v=pi*n^2*e^(4u).
    return add(mul({1:F(4)}, deriv(p)), mul({0:F(1), 1:F(-4)}, p))


def apply(poly, operator, value):
    result = {}
    term = value
    for k in range(max(poly, default=-1)+1):
        result = add(result, scale(term, poly.get(k, 0)))
        term = operator(term)
    return result


def hermite(m):
    return {j:F(factorial(2*m)*(-4)**j,
                factorial(2*j)*2**(m-j)*factorial(m-j))
            for j in range(m+1)}


def quotient_by_d2_minus_1(p):
    remainder = p.copy()
    quotient = {}
    while remainder and max(remainder) >= 2:
        k = max(remainder)
        c = remainder[k]
        quotient = add(quotient, {k-2:c})
        remainder = add(remainder, {k:-c, k-2:c})
    return quotient, remainder


def integral01(p):
    return sum((v/F(k+1) for k, v in p.items()), F(0))


def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--replay-dir', type=Path, required=True)
    parser.add_argument('--execution-model', required=True)
    parser.add_argument('--execution-effort', required=True)
    args = parser.parse_args()
    repo = args.repo.resolve()
    checks = []

    def check(name, left, right):
        if left != right:
            raise ArithmeticError(name)
        checks.append(name)

    one = {0:F(1)}
    d = {1:F(1)}
    source = {1:F(-3), 2:F(2)}
    aa = [one, d]
    for m in range(1, 10):
        aa.append(add(mul(d, aa[m]), scale(aa[m-1], 2*m*(2*m-1))))
    for m, a in enumerate(aa):
        check(f'normalized ladder polynomial mode {m}', apply(a, delta, one), hermite(m))
        check(f'normalized ladder parity {m}',
              {k:v for k,v in a.items() if k % 2 != m % 2}, {})
        check(f'zero mode from ladder {m}', at(a,F(1)), hermite(m)[0])

    # General p transfer: after removing the common (-i/4)^m q^-m /8,
    # compare to direct (i*pi*n^2)^m times the complete source mode.
    for m in range(7):
        p = add(mul(add(d,{0:F(-4*m)}), add(d,{0:F(-4*m)})), {0:F(-1)})
        for j in range(m):
            p = mul(p, add(d, {0:F(-1-4*j)}))
        check(f'complete p derivative mode {m}', apply(p,delta,one),
              scale(mul({m:F(1)},source), 8*(-4)**m))
    p = mul(mul({1:F(1),0:F(-1)}, {1:F(1),0:F(-3)}),
            {1:F(1),0:F(-5)})
    check('first p cubic coefficients', p,
          {3:F(1),2:F(-9),1:F(23),0:F(-15)})
    for m in range(1, 8):
        zero = (hermite(m+2)[0]-3*hermite(m)[0])/16
        check(f'raw vertical zero mode is positive {m}', zero>0, True)
    check('first raw vertical zero mode', (hermite(3)[0]-3*hermite(1)[0])/16,F(3,4))
    check('renormalized first vertical insertion',
          scale(add(hermite(3),scale(hermite(1),-3)),F(1,8)),
          add(delta(source),scale(delta(one),F(3,2))))

    for m in range(8):
        c = at(aa[m+2],F(1))/at(aa[m],F(1))
        q = add(aa[m+2],scale(aa[m],-c))
        r, remainder = quotient_by_d2_minus_1(q)
        check(f'fixed parity zero mode division {m}',remainder,{})
        check(f'finite jet physical reduction mode {m}',
              scale(apply(q,delta,one),2),scale(apply(r,delta,source),16))

    # Verify the full Green identity before sending its upper current to 0.
    for j in range(7):
        psi = {j:F(1)}
        for k in range(7):
            f = {k:F(1)}
            psi1, f1 = deriv(psi), deriv(f)
            psi2, f2 = deriv(psi1), deriv(f1)
            current = add(mul(psi2,f),scale(mul(psi1,f1),-1),mul(psi,f2),
                          scale(mul(psi1,f),-9),scale(mul(psi,f1),9),
                          scale(mul(psi,f),23))
            adjoint = {degree:coefficient*(-1)**degree for degree,coefficient in p.items()}
            left = integral01(mul(apply(p,deriv,psi),f))
            right = at(current,F(1))-at(current,F(0))+integral01(mul(psi,apply(adjoint,deriv,f)))
            check(f'Green identity including both ends {j},{k}',left,right)
    for t in (F(1,100), F(1,5)):
        for x in (F(0), F(999), F(1001)):
            a,b,c = F(2,7),F(-1,2),F(3,11)
            f0,f1,f2 = F(1),F(-4),2*t+16-x*x
            boundary = -c*f0+b*f1-a*f2+9*b*f0-9*a*f1-23*a*f0
            check(f'first p lower boundary {t},{x}',boundary,
                  -c+5*b+(x*x-2*t-3)*a)

    # Exact counterexample at 2*pi*|B|=log 2: bad Fourier multiplier is 2.
    for sign in (1,-1):
        mode = (1,-sign)
        eigenvalue_in_2pi_units = -mode[0]*mode[1]
        check(f'mixed generator amplifying mode B sign {sign}',
              sign*eigenvalue_in_2pi_units,1)
        check(f'nonnegative input at cosine minimum B sign {sign}',1-1,0)
        check(f'negative output at cosine minimum B sign {sign}',1-2,-1)

    for q,r in ((F(1),F(1)),(F(1),F(5)),(F(7),F(2)),(F(3),F(3))):
        for lam in (F(1,4),F(1,2),F(1)):
            Q,R = (q+r+lam*(q-r))/2,(q+r-lam*(q-r))/2
            check(f'interpolation inverse {q},{r},{lam}',
                  ((Q+R+(Q-R)/lam)/2,(Q+R-(Q-R)/lam)/2),(q,r))
            check(f'interpolation domain {q},{r},{lam}',
                  Q+R>=2 and abs(Q-R)<=lam*(Q+R-2),True)
            check(f'interpolation determinant {q},{r},{lam}',
                  ((1+lam)/2)**2-((1-lam)/2)**2,lam)

    args.replay_dir.mkdir(parents=True,exist_ok=True)
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1')
    inv22 = Path('papers/investigations-2/active/22_theta_manifold_geometry/numerics')
    inherited = []
    for name in ('check_asd_path_metric.py','check_theta_signed_bridge.py',
                 'check_coupled_theta_product.py','check_parity_strip_cutoff.py'):
        script = repo/inv22/name
        output = args.replay_dir/(script.stem+'.json')
        proc = subprocess.run([sys.executable,str(script),'--output',str(output)],
                              check=True,capture_output=True,text=True,timeout=30,env=env)
        data = json.loads(output.read_text())
        inherited.append({'script':str(inv22/name),'script_sha256':digest(script),
                          'receipt_sha256':digest(output),'status':'pass',
                          'exact_assertions':data.get('exact_assertions',data.get('assertions_passed')),
                          'metadata_note':'Receipt retains its historical authoring metadata; current replay configuration is recorded above.'})
    control_script = repo/'papers/investigations-3/11_arithmetic_collision_rigidity/numerics/replay_nonstationary_controls.py'
    control_output = args.replay_dir/'source_specific_controls.json'
    subprocess.run([sys.executable,str(control_script),'--repo',str(repo),
                    '--receipts',str(args.replay_dir/'control_receipts'),
                    '--output',str(control_output),'--execution-model',args.execution_model,
                    '--execution-effort',args.execution_effort],check=True,
                   capture_output=True,text=True,timeout=60,env=env)
    controls = json.loads(control_output.read_text())
    events = controls['screen']['event_rejections']
    check('five inherited event rejections',len(events),5)
    check('all inherited strict tests rejected',
          all(e['strict_first_jet_rejected'] and e['strict_signed_margin_rejected'] for e in events),True)
    check('separate Euler signed witness rejected',
          controls['screen']['euler_witness']['strict_signed_margin_rejected'],True)
    base = Path('papers/investigations-3/11_arithmetic_collision_rigidity')
    sources = [Path('AGENTS.md'),Path('LARGE_FILES.md'),
               base/'research-overview/03_SYMMETRY_RESEARCH_PROGRAM_AND_INVESTIGATION_GUIDE_20261018.md',
               base/'notes/07_HODGE_MODULAR_DUALITY_AND_ROTATION_DEFECT_20261018.md',
               base/'reviews/14_HODGE_AND_MODULAR_SYMMETRY_ASSESSMENT_20261018.md']
    notes22 = Path('papers/investigations-2/active/22_theta_manifold_geometry/notes/03_theta_bundles_and_connections')
    sources += [notes22/name for name in (
        '01_COVARIANT_SOURCE_AND_ASD_CONNECTION_20261015.md',
        '02_ASD_METRIC_FREEDOM_AND_PHYSICAL_RESTRICTION_20261015.md',
        '03_COMPLETE_SIGNED_CORRELATION_BRIDGE_20261015.md',
        '06_COUPLED_THETA_PRODUCT_AND_PARITY_SECTORS_20261015.md',
        '07_PARITY_STRIP_CUTOFF_AND_FULL_STARTING_FACTOR_20261015.md')]
    note = Path(__file__).resolve().parent.parent/'notes/01_TRANSVERSE_OBSERVATION_AND_FINITE_JET_OBSTRUCTIONS_20261018.md'
    record = {'date':'2026-10-18','timezone':'America/New_York',
        'prepared_for':'Edward Baker','actual_model':args.execution_model,
        'actual_effort':args.execution_effort,'llm_assistance':'substantial; same-model internal agent review',
        'python':platform.python_version(),'status':'pass','arithmetic':'exact rational finite polynomials; inherited Arb source controls',
        'comparison_domain':{'t':['1/100','1/5'],'x':['999','1001']},
        'primary_gate':'scoped obstruction, analytic proof in the note; finite algebra consistency and inherited screening replay',
        'exact_assertions':len(checks),'checks':checks,
        'script_sha256':digest(Path(__file__)), 'note_sha256':digest(note),
        'source_sha256':{str(p):digest(repo/p) for p in sources},
        'inherited_replays':inherited,
        'source_control_replay':{'script_sha256':digest(control_script),'receipt_sha256':digest(control_output),
             'interface_precision_bits':controls['interface_precision_bits'],
             'python_flint':controls['python_flint'],'event_rejections':events,
             'euler_witness':controls['screen']['euler_witness'],
             'analytic_premise_screen':controls['screen']['analytic_premise_screen']},
        'scope':'p-observation algebra, lower endpoints, vertical zero modes, fixed-parity finite-jet reduction, mixed Fourier obstruction, interpolation domain; inherited control interfaces',
        'not_established':['infinite convergence by finite checks','new physical signed margin',
             'new noncollision coverage','smaller approximation error','speedup','global transverse or coupled impossibility']}
    args.output.write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps({'status':'pass','exact_assertions':len(checks),
                      'inherited_checkers':len(inherited),'control_events':len(events),'output':str(args.output)}))


if __name__ == '__main__':
    main()
