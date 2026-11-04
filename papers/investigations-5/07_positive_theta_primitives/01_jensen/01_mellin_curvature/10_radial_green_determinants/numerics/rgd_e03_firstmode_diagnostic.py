#!/usr/bin/env python3
"""RGD-E03 r1: fixed k=1,4 floating feasibility, not certification.

Prepared for Edward Baker, 4 Nov 2026, with substantial LLM assistance.
Actual model gpt-6.1-sol (Codex), effort ultra; research chat0003.
Run with Python containing mpmath; no SymPy or downloads required.
All exact assembly and numerical attempts share one 180-second budget.
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

LIMIT_SECONDS = 180
LIMIT_EVALUATIONS = 250_000
EVALUATIONS = 0


class CapExceeded(RuntimeError):
    pass


def check_budget():
    if time.perf_counter() - START >= LIMIT_SECONDS:
        raise CapExceeded('180-second total computation cap')


def timed_out(*_):
    raise CapExceeded('180-second total computation cap')


signal.signal(signal.SIGALRM, timed_out)
signal.setitimer(signal.ITIMER_REAL, max(.001, LIMIT_SECONDS-(time.perf_counter()-START)))


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


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    base = Path(__file__).resolve().parent.parent
    inputs = [base/'notes/01_BOUNDARY_PRESERVING_FIRST_MODE_COMPARISON_20261104.md',
              base/'research-progress/handoffs/01_RGD_E04_R1_AND_E03_R1_BOUNDARY_PRESERVING_COMPARISON_20261104.md',
              base/'reviews/01_RGD_E04_R1_BOUNDARY_PRESERVING_COMPARISON_ASSESSMENT_20261104.md']
    record = {
        'date': '2026-11-04', 'timezone': 'America/New_York', 'prepared_for': 'Edward Baker',
        'llm_assistance': True, 'model': 'gpt-6.1-sol', 'reasoning_effort': 'ultra',
        'thread_id': '01a1a77f-2607-7832-9902-29399c58b442',
        'task': 'RGD-E03', 'request_revision': 'r1',
        'evidence': 'floating feasibility diagnostic and exact rational algebra; not certified',
        'python_version': platform.python_version(), 'python_executable': sys.executable,
        'code_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'input_sha256': {str(p.relative_to(base)): hashlib.sha256(p.read_bytes()).hexdigest() for p in inputs},
        'limits': {'seconds': 180, 'integrand_evaluations': 250000, 'maxdegree': 10,
                   'initial_decimal_digits': [80, 120], 'conditional_decimal_digits': 160},
        'method': 'mpmath tanh-sinh; breakpoints [0,1/8,1/4,1/2,1,2]; same moments 0..7',
        'tails': 'Note01 E_j (6) and B_j(2) (18), complete n>=2 and u>2; no numerical enclosure',
        'passes': [], 'status': 'started', 'failures': [],
        'attempts': 1,
    }
    try:
        import mpmath as mp
        record['mpmath_version'] = mp.__version__
        polys, plans, details = exact_assembly()
        record['algebra'] = {'status': 'all exact checks passed', 'k1_eight_terms_and_factorization': True,
                             'k4_c0_and_b_absent': True, 'cases': details,
                             'elapsed_seconds': time.perf_counter()-START}
        raw_passes = []
        def fmt(v):
            return mp.nstr(v, mp.mp.dps, min_fixed=0, max_fixed=0)
        def acquire(dps):
            global EVALUATIONS
            mp.mp.dps = dps
            pass_start = time.perf_counter()
            item = {'decimal_digits': dps, 'moments': [], 'cases': {}, 'complete': False}
            record['passes'].append(item)
            xs = []
            for j in range(8):
                before = EVALUATIONS
                denominator = 8*factorial(2*j)
                def integrand(u):
                    global EVALUATIONS
                    check_budget()
                    if EVALUATIONS >= LIMIT_EVALUATIONS:
                        raise CapExceeded('250000 total integrand evaluation cap')
                    EVALUATIONS += 1
                    return u**(2*j)*mp.exp(u-mp.pi*mp.exp(4*u))/denominator
                x, err = mp.quad(integrand, [0, mp.mpf(1)/8, mp.mpf(1)/4, mp.mpf(1)/2, 1, 2],
                                 method='tanh-sinh', error=True, maxdegree=10)
                xs.append(x)
                item['moments'].append({'j': j, 'x': fmt(x), 'quadrature_error_estimate': fmt(err),
                                        'integrand_evaluations': EVALUATIONS-before})
                check_budget()
            E = [mp.exp(-4*mp.pi)/(8*(-mp.expm1(-5*mp.pi))*(16*mp.pi-1)**(2*j+1)) for j in range(8)]
            aU = 4*mp.pi*mp.exp(8)-1
            Btail = [mp.exp(2-mp.pi*mp.exp(8))/(8*factorial(2*j))*mp.fsum(
                mp.mpf(comb(2*j, h)*2**(2*j-h)*factorial(h))/aU**(h+1) for h in range(2*j+1)) for j in range(8)]
            payment = [e+b for e,b in zip(E, Btail)]
            item['tail_allowances'] = [{'j': j, 'E': fmt(E[j]), 'B': fmt(Btail[j]),
                                        'E_plus_B': fmt(payment[j]), 'addition_rounded_to_E': payment[j] == E[j]}
                                       for j in range(8)]
            raw = {'xs': xs, 'cases': {}}
            for k in (1, 4):
                n = k+4
                xp = [[mp.mpf(1)]+[xs[j]**h for h in range(1,7)] for j in range(n)]
                vp = [[mp.mpf(1)]+[payment[j]**h for h in range(1,7)] for j in range(n)]
                def eval_poly(p):
                    return mp.fsum((mp.mpf(a.numerator)/a.denominator if isinstance(a,F) else mp.mpf(a))
                                   * mp.fprod(xp[j][h] for j,h in enumerate(e) if h)
                                   for e,a in sorted(p.items()))
                q = eval_poly(polys[k])
                paid = []
                by_degree = defaultdict(list)
                counts = Counter()
                for alpha,p in sorted(plans[k].items()):
                    degree = sum(alpha)
                    if not degree:
                        continue
                    coefficient = eval_poly(p)
                    contribution = abs(coefficient)*mp.fprod(vp[j][h] for j,h in enumerate(alpha) if h)
                    paid.append(contribution)
                    by_degree[degree].append(contribution)
                    counts[degree] += 1
                R = mp.fsum(paid)
                if R <= 0 or not all(mp.isfinite(v) for v in [q,R]):
                    raise ArithmeticError(f'k={k}: nonpositive residual or nonfinite result')
                L, S = q-R, q/R
                norm = L/(abs(q)+R)
                raw['cases'][k] = {'q':q,'R':R,'L':L,'S':S,'normalized_margin':norm}
                item['cases'][str(k)] = {name:fmt(value) for name,value in raw['cases'][k].items()}
                item['cases'][str(k)]['residual_by_degree'] = {str(d):fmt(mp.fsum(v)) for d,v in sorted(by_degree.items())}
                item['cases'][str(k)]['taylor_coefficients_by_degree'] = dict(sorted(counts.items()))
                check_budget()
            item['complete'] = True
            item['elapsed_seconds'] = time.perf_counter()-pass_start
            item['integrand_evaluations_total'] = EVALUATIONS
            raw_passes.append(raw)
            print(json.dumps({'completed_digits': dps, 'elapsed_seconds': time.perf_counter()-START,
                              'evaluations': EVALUATIONS,
                              'ratios': {str(k):mp.nstr(raw['cases'][k]['S'],12) for k in (1,4)}}), flush=True)
        acquire(80)
        acquire(120)
        def compare():
            old,new = raw_passes[-2:]
            discrepancy = lambda v,w: abs(v-w)/max(abs(v),abs(w),mp.mpf('1e-500'))
            dx = [discrepancy(v,w) for v,w in zip(old['xs'],new['xs'])]
            dc = {k:{name:discrepancy(old['cases'][k][name],new['cases'][k][name])
                     for name in ('q','R','S')} for k in (1,4)}
            return dx,dc
        dx,dc = compare()
        def category(v):
            if v > 1+mp.mpf('1e-20'): return 'favorable diagnostic'
            if v < 1-mp.mpf('1e-20'): return 'adverse for this payment'
            return 'inconclusive'
        trigger = []
        if max(dx+[v for d in dc.values() for v in d.values()]) > mp.mpf('1e-30'):
            trigger.append('relative discrepancy exceeds 1e-30')
        for k in (1,4):
            if category(raw_passes[-1]['cases'][k]['S']) != category(raw_passes[-2]['cases'][k]['S']):
                trigger.append(f'k={k} classification changed')
            if abs(raw_passes[-1]['cases'][k]['S']-1) <= mp.mpf('1e-20'):
                trigger.append(f'k={k} ratio within 1e-20 of 1')
        record['conditional_160_digit_trigger'] = trigger
        if trigger:
            acquire(160)
            dx,dc = compare()
        record['last_two_pass_comparison'] = {
            'decimal_digits': [p['decimal_digits'] for p in record['passes'][-2:]],
            'moment_symmetric_relative_discrepancies': [fmt(v) for v in dx],
            'case_symmetric_relative_discrepancies': {str(k):{n:fmt(v) for n,v in d.items()} for k,d in dc.items()},
            'definition': '|v-w|/max(|v|,|w|,1e-500); estimates, not guaranteed errors',
        }
        record['dispositions'] = {}
        for k in (1,4):
            # k=1 uses x0..x4; k=4 uses all eight acquired moments.
            consistent = max(dx[:k+4]+list(dc[k].values())) <= mp.mpf('1e-30')
            disposition = category(raw_passes[-1]['cases'][k]['S']) if consistent else 'inconclusive'
            record['dispositions'][str(k)] = {'classification':disposition,'precision_consistent':consistent}
        record['status'] = 'completed bounded diagnostic'
    except (CapExceeded, ArithmeticError, AssertionError, ImportError) as exc:
        record['status'] = 'capped' if isinstance(exc,CapExceeded) else 'failed'
        record['failures'].append({'type':type(exc).__name__, 'message':str(exc)})
    finally:
        record['total_computation_seconds'] = time.perf_counter()-START
        signal.setitimer(signal.ITIMER_REAL, 0)
        record['total_integrand_evaluations'] = EVALUATIONS
        record['budget_exceeded'] = record['total_computation_seconds']>180 or EVALUATIONS>250000
        args.output.write_text(json.dumps(record,indent=2)+'\n')
        print(json.dumps({k:record.get(k) for k in ['status','dispositions','failures','total_computation_seconds','total_integrand_evaluations']}))


if __name__ == '__main__':
    main()
