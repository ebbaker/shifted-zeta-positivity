#!/usr/bin/env python3
"""RGD-E02 r1: two-case rigorous acquisition and exact record verification.

Prepared for Edward Baker, 4 November 2026, with substantial LLM assistance.
Actual gpt-6.1-sol (Codex), effort ultra, research chat0003.
Exact polynomial helpers below are copied unchanged from the frozen E03
script; the acquired source and comparison remain unchanged.
Run with python-flint to acquire; --verify needs only Python's standard library.
"""
import time
START = time.perf_counter()
import argparse
from collections import Counter, defaultdict
from fractions import Fraction as F
import hashlib
from itertools import permutations, product
import json
from math import comb, factorial
from pathlib import Path
import platform
import signal
import sys

ACTIVE_BUDGET = False
EVALUATIONS = 0
LIMIT_SECONDS = 180
LIMIT_EVALUATIONS = 200000

class CapExceeded(RuntimeError):
    pass

def check_budget():
    if ACTIVE_BUDGET and time.perf_counter()-START >= LIMIT_SECONDS:
        raise CapExceeded('180-second total computation cap')

def timed_out(*_):
    raise CapExceeded('180-second total computation cap')

def term(out, e, a):
    if a:
        out[e] = out.get(e, 0) + a
        if not out[e]:
            del out[e]


def const(a, n):
    return {(0,)*n: a} if a else {}


def var(i, n):
    e = [0]*n
    e[i] = 1
    return {tuple(e): 1}


def add(*ps):
    out = {}
    for p in ps:
        for e, a in p.items():
            term(out, e, a)
    return out


def scale(p, a):
    return {e: c*a for e, c in p.items() if c*a}


def mul(*ps):
    n = len(next(iter(next(p for p in ps if p)))) if any(ps) else 8
    out = const(1, n)
    for p in ps:
        nxt = {}
        for e, a in out.items():
            for f, b in p.items():
                term(nxt, tuple(x+y for x, y in zip(e, f)), a*b)
        out = nxt
    return out


def power(p, n):
    dim = len(next(iter(p))) if p else 8
    return mul(const(1, dim), *([p]*n))


def det_by_permutations(r, k, c, n=8):
    out = {}
    for perm in permutations(range(r)):
        sign = (-1)**sum(perm[i] > perm[j] for i in range(r) for j in range(i+1, r))
        factors = [c(k+perm[i]-i) for i in range(r)]
        out = add(out, scale(mul(const(1, n), *factors), sign))
    return out


def f3(l, c):
    return add(power(c(l), 3), scale(mul(c(l-1), c(l), c(l+1)), -2),
               mul(c(l-2), power(c(l+1), 2)),
               mul(power(c(l-1), 2), c(l+2)),
               scale(mul(c(l-2), c(l), c(l+2)), -1))


def joint(k, c):
    return add(power(f3(k, c), 2), scale(mul(f3(k-1, c), f3(k+1, c)), -1))


def poly_hash(p):
    data = [[list(e), str(a)] for e, a in sorted(p.items())]
    return hashlib.sha256(json.dumps(data, separators=(',', ':')).encode()).hexdigest()


def exact_assembly():
    c = lambda j: var(j, 8) if j >= 0 else {}
    formal = {k: joint(k, c) for k in (1, 4)}
    A, B, C, D, H = [c(j) for j in range(5)]
    p1 = add(power(B, 6), scale(mul(A, power(B, 4), C), -4),
             scale(mul(power(A, 2), power(B, 2), power(C, 2)), 4),
             scale(mul(power(A, 2), power(B, 3), D), 2),
             scale(mul(power(A, 3), B, C, D), -2),
             scale(mul(power(A, 3), power(C, 3)), -1),
             scale(mul(power(A, 3), power(B, 2), H), -1),
             mul(power(A, 4), C, H))
    factored = mul(add(power(B, 2), scale(mul(A, C), -1)),
                   add(power(B, 4), scale(mul(A, power(B, 2), C), -3),
                       mul(power(A, 2), power(C, 2)),
                       scale(mul(power(A, 2), B, D), 2),
                       scale(mul(power(A, 3), H), -1)))
    assert formal[1] == p1 == factored
    assert len(p1) == 8
    assert all(e[0] == 0 for e in formal[4])
    for k in (1, 4):
        assert formal[k] == mul(det_by_permutations(4, k, c), det_by_permutations(2, k, c))
        for l in (k-1, k, k+1):
            assert f3(l, c) == det_by_permutations(3, l, c)
    reference = {}
    plans = {}
    details = {}
    for k in (1, 4):
        n = k+4  # five/eight primitive variables; b=1/16 exact
        def entry(j):
            if j < 0:
                return {}
            return add(const(F(1, 16) if j == 0 else 0, n),
                       var(j-1, n) if j else {}, scale(var(j, n), -1))
        reference[k] = joint(k, entry)
        plan = defaultdict(dict)
        for beta, a in reference[k].items():
            for alpha in product(*(range(v+1) for v in beta)):
                gamma = tuple(v-w for v, w in zip(beta, alpha))
                coeff = a
                for v, w in zip(beta, alpha):
                    coeff *= comb(v, w)
                term(plan[alpha], gamma, coeff)
        plan = {a: p for a, p in plan.items() if p}
        zero = (0,)*n
        assert plan[zero] == reference[k]
        assert len(plan) <= (462 if k == 1 else 3003)
        assert max(map(sum, plan)) == 6
        # Verify the complete exact translation at rational, non-theta data.
        xrat = [F(j+1, 17) for j in range(n)]
        zrat = [F(j+2, 29) for j in range(n)]
        def ev(p, values):
            return sum(a*product_value(values, e) for e, a in p.items())
        assert ev(reference[k], [a+b for a, b in zip(xrat, zrat)]) == sum(
            ev(p, xrat)*product_value(zrat, alpha) for alpha, p in plan.items())
        plans[k] = plan
        details[str(k)] = {
            'formal_c_terms': len(formal[k]), 'reference_x_terms': len(reference[k]),
            'translation_monomials_including_constant': len(plan),
            'translation_terms_by_degree': dict(sorted(Counter(map(sum, plan)).items())),
            'formal_c_polynomial_sha256': poly_hash(formal[k]),
            'reference_polynomial_sha256': poly_hash(reference[k]),
            'D4_times_D2_permutation_identity': True,
            'F3_formula_permutation_identity': True,
            'exact_rational_translation_check': True,
            'b_independent': k == 4,
        }
        check_budget()
    return reference, plans, details


def product_value(values, exponents):
    value = 1
    for x, e in zip(values, exponents):
        if e:
            value *= x**e
    return value


def pair_fraction(pair):
    m, e = int(pair[0]), int(pair[1])
    return F(m*2**e) if e >= 0 else F(m, 2**(-e))


def fraction_pair(x):
    assert x.denominator & (x.denominator-1) == 0
    return [str(x.numerator), -(x.denominator.bit_length()-1)]


def bounds(data):
    m, r = pair_fraction(data['mid']), pair_fraction(data['rad'])
    assert r >= 0
    return m-r, m+r


def pack(x):
    assert x.is_finite(), 'nonfinite real ball'
    return {'mid': [str(v) if i == 0 else int(v) for i,v in enumerate(x.mid().man_exp())],
            'rad': [str(v) if i == 0 else int(v) for i,v in enumerate(x.rad().man_exp())],
            'display': x.str(22)}


def fraction_text(x, digits=18):
    from decimal import Decimal, localcontext
    with localcontext() as c:
        c.prec = digits
        return format(Decimal(x.numerator)/Decimal(x.denominator), '.12E')


def rational_propagation(item, polys, plans):
    """Exact interval propagation from saved inputs; no transcendental calls.

    Positive moment intervals allow endpoint powers/products. Every signed
    coefficient polynomial is collected before its absolute-value bound.
    """
    X = [bounds(v['ball']) for v in item['moments']]
    assert len(X) == 8 and all(0 < lo <= hi for lo,hi in X)
    grid = 2**384
    T = []
    for row in item['tail_allowances']:
        elo,ehi = bounds(row['E'])
        blo,bhi = bounds(row['B'])
        assert elo > 0 and blo > 0
        exact_upper = ehi+bhi
        scaled = exact_upper*grid
        upward = F(-((-scaled.numerator)//scaled.denominator), grid)
        assert upward >= exact_upper
        T.append(upward)
    result = {}
    for k in (1,4):
        n = k+4
        xp = [[(F(1),F(1))]+[(lo**h,hi**h) for h in range(1,7)] for lo,hi in X[:n]]
        tp = [[F(1)]+[t**h for h in range(1,7)] for t in T[:n]]
        def evaluate(p):
            lo,hi = F(0),F(0)
            for e,a in p.items():
                ml,mh = F(1),F(1)
                for j,h in enumerate(e):
                    ml *= xp[j][h][0]
                    mh *= xp[j][h][1]
                if a >= 0:
                    lo += a*ml; hi += a*mh
                else:
                    lo += a*mh; hi += a*ml
            return lo,hi
        qlo,qhi = evaluate(polys[k])
        R = F(0)
        for alpha,p in plans[k].items():
            if not sum(alpha):
                continue
            lo,hi = evaluate(p)
            amplitude = max(abs(lo),abs(hi))
            for j,h in enumerate(alpha):
                amplitude *= tp[j][h]
            R += amplitude
        ell = qlo-R
        witness = F(7,10**23) if k == 1 else F(1,10**74)
        result[str(k)] = {'q_lower':fraction_pair(qlo), 'q_upper':fraction_pair(qhi),
                          'residual_upper':fraction_pair(R), 'lower_allowance':fraction_pair(ell),
                          'lower_allowance_display':fraction_text(ell),
                          'positive':ell > 0,
                          'weaker_rational_witness':str(witness), 'witness_verified':ell > witness}
        check_budget()
    return result


def verify_record(path, base, polys=None, plans=None):
    d = json.loads(path.read_text())
    assert hashlib.sha256(Path(__file__).read_bytes()).hexdigest() == d['code_sha256']
    for name,h in d['input_sha256'].items():
        assert hashlib.sha256((base/name).read_bytes()).hexdigest() == h, name
    assert d['task'] == 'RGD-E02' and d['request_revision'] == 'r1'
    assert d['status'] == 'certified two-case lower bounds'
    assert d['breakpoints'] == ['0','1/8','1/4','1/2','1','2']
    if polys is None:
        polys,plans,_ = exact_assembly()
    item = d['passes'][-1]
    assert [moment['j'] for moment in item['moments']] == list(range(8))
    for moment in item['moments']:
        lo,hi = F(0),F(0)
        assert len(moment['segments']) == 5
        assert [row['index'] for row in moment['segments']] == list(range(5))
        for row in moment['segments']:
            left,right = bounds(row['real'])
            lo += left; hi += right
            imlo,imhi = bounds(row['imag'])
            assert imlo <= 0 <= imhi
        xlo,xhi = bounds(moment['ball'])
        assert xlo <= lo <= hi <= xhi
    rational = rational_propagation(item,polys,plans)
    for k in ('1','4'):
        saved = item['cases'][k]
        qlo,_ = bounds(saved['q_lower'])
        _,rhi = bounds(saved['residual_upper'])
        ell,_ = bounds(saved['lower_allowance'])
        assert ell > 0 and ell <= qlo-rhi
        assert rational[k] == item['rational_verification'][k]
        assert rational[k]['positive']
    assert d['total_callback_evaluations'] <= LIMIT_EVALUATIONS
    assert sum(v['callback_evaluations'] for p in d['passes'] for m in p['moments']
               for v in m['segments']) == d['total_callback_evaluations']
    assert d['total_computation_seconds'] <= LIMIT_SECONDS
    return {'status':'exact serialized-record checks passed',
            'scope':'hashes, cover sums, positive dyadic bounds and rational propagation; trusts identified Arb acquisition',
            'record_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
            'cases':{k:{'positive':v['positive'],'witness_verified':v['witness_verified']}
                     for k,v in rational.items()}}


def main():
    global ACTIVE_BUDGET,EVALUATIONS
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--output',type=Path)
    group.add_argument('--verify',type=Path)
    args = parser.parse_args()
    base = Path(__file__).resolve().parent.parent
    if args.verify:
        result = verify_record(args.verify,base)
        result['verification_seconds'] = time.perf_counter()-START
        print(json.dumps(result))
        return
    ACTIVE_BUDGET = True
    signal.signal(signal.SIGALRM,timed_out)
    signal.setitimer(signal.ITIMER_REAL,max(.001,LIMIT_SECONDS-(time.perf_counter()-START)))
    inputs = ['notes/01_BOUNDARY_PRESERVING_FIRST_MODE_COMPARISON_20261104.md',
              'reviews/01_RGD_E04_R1_BOUNDARY_PRESERVING_COMPARISON_ASSESSMENT_20261104.md',
              'notes/02_RGD_E03_R1_TWO_CASE_FIRST_MODE_DIAGNOSTIC_RETURN_20261104.md',
              'numerics/rgd_e03_firstmode_diagnostic.py',
              'numerics/RGD_E03_R1_FIRSTMODE_DIAGNOSTIC_20261104.json',
              'research-progress/handoffs/04_RGD_E02_R1_RIGOROUS_TWO_CASE_ACQUISITION_20261104.md']
    record = {'date':'2026-11-04','timezone':'America/New_York','prepared_for':'Edward Baker',
              'llm_assistance':True,'model':'gpt-6.1-sol','reasoning_effort':'ultra',
              'thread_id':'01a1a77f-2607-7832-9902-29399c58b442',
              'turn_id':'01a1a789-4831-75e3-ac1d-91bbab495d0d',
              'task':'RGD-E02','request_revision':'r1','status':'started',
              'python_version':platform.python_version(),'python_executable':sys.executable,
              'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'input_sha256':{p:hashlib.sha256((base/p).read_bytes()).hexdigest() for p in inputs},
              'limits':{'seconds':180,'callback_evaluations':200000,'precision_bits':[384,512],
                        'tolerance_bits':[320,448],'degree_per_call':128,'depth_per_call':20,
                        'evaluations_per_call':5000,'use_heap':True},
              'breakpoints':['0','1/8','1/4','1/2','1','2'],
              'enclosure_contract':'entire acb integration; outward Arb constants/tails and joint polynomial propagation; exact dyadic serialization',
              'passes':[],'failures':[]}
    try:
        import flint
        from flint import arb,acb,ctx
        record['python_flint_version'] = flint.__version__
        record['FLINT_version'] = flint.__FLINT_VERSION__
        polys,plans,details = exact_assembly()
        prior = json.loads((base/inputs[4]).read_text())
        for k in ('1','4'):
            assert json.loads(json.dumps(details[k])) == prior['algebra']['cases'][k]
        record['algebra'] = {'status':'passed, identical polynomial data to E03', 'cases':details,
                             'elapsed_seconds':time.perf_counter()-START}
        for bits,tol_bits in [(384,320),(512,448)]:
            ctx.prec = bits
            ctx.threads = 1
            pass_start = time.perf_counter()
            item = {'precision_bits':bits,'tolerance_bits':tol_bits,'moments':[],
                    'tail_allowances':[],'cases':{},'complete':False}
            record['passes'].append(item)
            pi = arb.pi()
            exp8 = arb(8).exp()
            a = 16*pi-1
            denom_geom = 1-(-5*pi).exp()
            aU = 4*pi*exp8-1
            assert pi > 0 and a > 0 and denom_geom > 0 and aU > 0
            item['constants'] = {name:pack(value) for name,value in
                                 [('pi',pi),('exp8',exp8),('a',a),('denom_geom',denom_geom),('aU',aU)]}
            X = []
            finite = True
            endpoints = [arb(0),arb(1)/8,arb(1)/4,arb(1)/2,arb(1),arb(2)]
            tolerance = arb(2)**(-tol_bits)
            for j in range(8):
                total = acb(0)
                moment = {'j':j,'segments':[]}
                item['moments'].append(moment)
                for index,(left,right) in enumerate(zip(endpoints,endpoints[1:])):
                    before = EVALUATIONS
                    denominator = 8*factorial(2*j)
                    def integrand(z,analytic):
                        global EVALUATIONS
                        check_budget()
                        if EVALUATIONS >= LIMIT_EVALUATIONS:
                            raise CapExceeded('200000 callback evaluation cap')
                        EVALUATIONS += 1
                        # Entire: integer power, multiplication and nested exp.
                        return z**(2*j)*(z-acb(pi)*(4*z).exp()).exp()/denominator
                    integral = acb.integral(integrand,left,right,rel_tol=tolerance,
                                            abs_tol=tolerance,deg_limit=128,eval_limit=5000,
                                            depth_limit=20,use_heap=True)
                    if integral.is_finite() and not integral.imag.contains(0):
                        raise ArithmeticError(f'finite integral excludes reality at j={j}, segment={index}')
                    if not integral.is_finite():
                        finite = False
                        item['failure'] = f'nonfinite enclosure at j={j}, segment={index}'
                        moment['segments'].append({'index':index,
                                                  'callback_evaluations':EVALUATIONS-before,
                                                  'failure':item['failure']})
                        break
                    moment['segments'].append({'index':index,'real':pack(integral.real),
                                                'imag':pack(integral.imag),
                                                'callback_evaluations':EVALUATIONS-before})
                    total += integral
                    check_budget()
                if not finite:
                    break
                assert total.imag.contains(0)
                X.append(total.real)
                moment['ball'] = pack(total.real)
            if not finite:
                item['elapsed_seconds'] = time.perf_counter()-pass_start
                item['refinement_reason'] = item['failure']
                continue
            E,B,V = [],[],[]
            for j in range(8):
                e = (-4*pi).exp()/(8*denom_geom*a**(2*j+1))
                b = (arb(2)-pi*exp8).exp()/(8*factorial(2*j))*sum(
                    (arb(comb(2*j,h)*2**(2*j-h)*factorial(h))/aU**(h+1)
                     for h in range(2*j+1)),arb(0))
                v = e+b
                assert e > 0 and b > 0 and v > 0
                E.append(e);B.append(b);V.append(v)
                item['tail_allowances'].append({'j':j,'E':pack(e),'B':pack(b),'E_plus_B':pack(v),
                                                'same_midpoint_as_E':v.mid()==e.mid(),
                                                'B_paid_outward':True})
            for k in (1,4):
                n = k+4
                xp = [[arb(1)]+[X[j]**h for h in range(1,7)] for j in range(n)]
                tp = [[arb(1)]+[V[j].upper()**h for h in range(1,7)] for j in range(n)]
                def evaluate(p):
                    value = arb(0)
                    for exponent,coefficient in sorted(p.items()):
                        value += (arb(coefficient.numerator)/coefficient.denominator
                                  if isinstance(coefficient,F) else arb(coefficient))*product_value(
                                      [xp[j][h] for j,h in enumerate(exponent)],(1,)*n)
                    return value
                q = evaluate(polys[k])
                majorant = arb(0)
                degrees = defaultdict(lambda:arb(0))
                for alpha,p in sorted(plans[k].items()):
                    if not sum(alpha):
                        continue
                    coefficient_bound = evaluate(p).abs_upper()
                    value = coefficient_bound
                    for j,h in enumerate(alpha):
                        value *= tp[j][h]
                    majorant += value
                    degrees[sum(alpha)] += value
                qlower = q.lower()
                Rupper = majorant.upper()
                ell = (qlower-Rupper).lower()
                assert all(v.is_finite() for v in [q,majorant,qlower,Rupper,ell])
                item['cases'][str(k)] = {'q_ball':pack(q),'majorant_ball':pack(majorant),
                                         'q_lower':pack(qlower),'residual_upper':pack(Rupper),
                                         'lower_allowance':pack(ell),'positive':bool(ell>0),
                                         'q_lower_div_R_upper':pack(qlower/Rupper),
                                         'majorant_by_degree':{str(degree):pack(v) for degree,v in sorted(degrees.items())}}
                check_budget()
            item['rational_verification'] = rational_propagation(item,polys,plans)
            item['complete'] = True
            item['elapsed_seconds'] = time.perf_counter()-pass_start
            passed = all(v['positive'] for v in item['cases'].values()) and all(
                v['positive'] for v in item['rational_verification'].values())
            print(json.dumps({'precision_bits':bits,'certified':passed,'seconds':time.perf_counter()-START,
                              'callbacks':EVALUATIONS,'lower_allowances':{k:v['lower_allowance']['display']
                              for k,v in item['cases'].items()}}),flush=True)
            if passed:
                record['status'] = 'certified two-case lower bounds'
                break
            item['refinement_reason'] = 'final lower enclosure not strictly positive or independent rational witness unresolved'
        if record['status'] == 'started':
            record['status'] = 'inconclusive within frozen two-pass contract'
    except (CapExceeded,AssertionError,ArithmeticError,RuntimeError,ValueError,ImportError) as exc:
        record['status'] = 'capped' if isinstance(exc,CapExceeded) else 'failed'
        record['failures'].append({'type':type(exc).__name__,'message':str(exc)})
    finally:
        record['total_computation_seconds'] = time.perf_counter()-START
        record['total_callback_evaluations'] = EVALUATIONS
        signal.setitimer(signal.ITIMER_REAL,0)
        ACTIVE_BUDGET = False
        args.output.write_text(json.dumps(record,indent=2)+'\n')
        print(json.dumps({name:record.get(name) for name in ['status','failures','total_computation_seconds','total_callback_evaluations']}))


if __name__ == '__main__':
    main()


