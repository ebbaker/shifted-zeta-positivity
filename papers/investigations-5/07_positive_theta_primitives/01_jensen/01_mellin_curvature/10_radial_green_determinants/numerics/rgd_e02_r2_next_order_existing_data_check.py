#!/usr/bin/env python3
"""RGD-E02 r2: exact existing-data verification; no new integration.

Prepared for Edward Baker, 4 Nov 2026, with substantial LLM assistance.
Actual gpt-6.1-sol (Codex), effort ultra, research chat0003.
Python standard library only. No prior checker is imported or executed.
"""
import time
START = time.perf_counter()
import argparse
from fractions import Fraction as F
import hashlib
from itertools import permutations
import json
from math import comb
from pathlib import Path
import platform
import signal

LOCKS = {
    'notes/05_RGD_B03_PREPARATORY_ORDER_DEPENDENCE_20261104.md': '93ac9495bf685a4464ca7751ae89b7218364f635b522aa80dbc4f554f6007a2b',
    'numerics/RGD_E02_R1_TWO_CASE_CERTIFICATE_20261104.json': '6db6276d65ea11706286cffa0aef899d1097f8e4bac76cbdd70f0ef40d692298',
    'numerics/rgd_e02_two_case_certificate.py': 'b4863a6840cd4d68b10fe993f3f4cdc5e66dd8b3d44903445b306a50c8879db4',
    'reviews/03_RGD_E04_R2_TWO_CASE_CERTIFICATE_ASSESSMENT_20261104.md': '4c1d9e07f620e49f6d2fcaad538f176549316e19e8f11d9010cc52f4856b3807',
    'notes/01_BOUNDARY_PRESERVING_FIRST_MODE_COMPARISON_20261104.md': '556a97aa60f7a3448acbd00cf8bfa4c3e2916e428f67d03dbb97889077bc9847',
    'research-progress/handoffs/08_RGD_E02_R2_EXISTING_DATA_NEXT_ORDER_AND_MODEL_CHANGE_20261104.md': 'c58c87ce3af0b4ca67c320b883929bdc6dc4b366d11f21dace57b683024d3d6c',
}


class FixedCheckFailure(Exception):
    pass


class RuntimeCap(Exception):
    pass


def alarm(*_):
    raise RuntimeCap('60-second cumulative execution cap')


def pair_value(v):
    m,e = int(v[0]),int(v[1])
    return F(m*2**e) if e >= 0 else F(m,2**(-e))


def endpoints(ball):
    m,r = pair_value(ball['mid']),pair_value(ball['rad'])
    if r < 0:
        raise FixedCheckFailure('negative serialized radius')
    return m-r,m+r


def rational(v):
    return str(v)


def reading(v):
    from decimal import Decimal,localcontext
    with localcontext() as ctx:
        ctx.prec = 18
        return format(Decimal(v.numerator)/Decimal(v.denominator),'.12E')


def poly_constant(v,n):
    return {(0,)*n:v} if v else {}


def variable(j,n):
    e = [0]*n
    e[j] = 1
    return {tuple(e):1}


def add(*ps):
    out = {}
    for p in ps:
        for e,a in p.items():
            out[e] = out.get(e,0)+a
            if not out[e]:
                del out[e]
    return out


def scale(p,a):
    return {e:a*c for e,c in p.items() if a*c}


def multiply(p,q):
    out = {}
    for e,a in p.items():
        for f,b in q.items():
            g = tuple(x+y for x,y in zip(e,f))
            out[g] = out.get(g,0)+a*b
            if not out[g]:
                del out[g]
    return out


def determinant(n,k):
    """Direct permutation expansion in formal c0,...,c5."""
    out = {}
    for p in permutations(range(n)):
        indices = [k+p[i]-i for i in range(n)]
        if min(indices) < 0:
            continue
        e = [0]*6
        for j in indices:
            e[j] += 1
        sign = (-1)**sum(p[i]>p[j] for i in range(n) for j in range(i+1,n))
        out = add(out,{tuple(e):sign})
    return out


def value(p,point):
    total = F(0)
    for e,a in p.items():
        term = F(a)
        for x,h in zip(point,e):
            term *= x**h
        total += term
    return total


def derivative(p,j):
    out = {}
    for e,a in p.items():
        if e[j]:
            g = list(e)
            g[j] -= 1
            out[tuple(g)] = a*e[j]
    return out


def interval_value(p,box):
    lo,hi = F(0),F(0)
    for e,a in p.items():
        ml,mh = F(1),F(1)
        for (l,u),h in zip(box,e):
            ml *= l**h
            mh *= u**h
        if a >= 0:
            lo += a*ml;hi += a*mh
        else:
            lo += a*mh;hi += a*ml
    return lo,hi


def polynomial_record(p):
    return [{'powers':list(e),'coefficient':str(a)} for e,a in sorted(p.items())]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--prior-record',type=Path,
                        help='Preserved first-run implementation failure, only for the one permitted correction')
    args = parser.parse_args()
    if args.output.exists():
        raise SystemExit('Refusing to overwrite an execution record; use a fresh output path.')
    base = Path(__file__).resolve().parent.parent
    previous_seconds = 0
    previous = None
    attempt = 1
    if args.prior_record:
        old = json.loads(args.prior_record.read_text())
        if old['task'] != 'RGD-E02' or old['request_revision'] != 'r2' or old['attempt'] != 1:
            raise SystemExit('Invalid prior run for the two-run contract.')
        if old['status'] != 'implementation failure' or old['input_sha256'] != LOCKS:
            raise SystemExit('Only one implementation correction with unchanged locked inputs is permitted.')
        attempt = 2
        previous_seconds = old['cumulative_execution_seconds']
        previous = {'record_sha256':hashlib.sha256(args.prior_record.read_bytes()).hexdigest(),
                    'code_sha256':old['code_sha256'],'execution_seconds':old['execution_seconds'],
                    'status':old['status'],'failure':old['failure']}
    record = {
        'date':'2026-11-04','timezone':'America/New_York','prepared_for':'Edward Baker',
        'llm_assistance':True,'model':'gpt-6.1-sol','reasoning_effort':'ultra',
        'thread_id':'01a1a77f-2607-7832-9902-29399c58b442',
        'turn_id':'01a1a7ac-1448-7770-b86d-3264bc4b53e2',
        'task':'RGD-E02','request_revision':'r2','attempt':attempt,'prior_attempt':previous,
        'input_sha256':LOCKS,'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'python_version':platform.python_version(),'arithmetic':'standard-library Fraction and integers only',
        'evidence':'exact rational post-processing of an accepted Arb/FLINT acquisition; no new integration',
        'new_application':{'r':4,'k':1},'matched_analytical_comparison':{'r':3,'k':1},
        'moment_indices_used':list(range(6)),'tail_indices_used':list(range(6)),
        'integrand_evaluations':0,'new_moments':0,
        'limits':{'cumulative_seconds':60,'runs':2,'record_bytes':102400},
        'checks':[],'status':'started','failure':None,
    }
    def check(condition,name,detail=None):
        record['checks'].append({'check':name,'passed':bool(condition),'detail':detail})
        if not condition:
            raise FixedCheckFailure(name)
    signal.signal(signal.SIGALRM,alarm)
    signal.setitimer(signal.ITIMER_REAL,max(.001,60-previous_seconds-(time.perf_counter()-START)))
    try:
        for name,expected in LOCKS.items():
            check(hashlib.sha256((base/name).read_bytes()).hexdigest()==expected,'locked input '+name)
        old = json.loads((base/'numerics/RGD_E02_R1_TWO_CASE_CERTIFICATE_20261104.json').read_text())
        check(old['status']=='certified two-case lower bounds' and len(old['passes'])==1,
              'accepted single acquisition pass')
        saved = old['passes'][0]
        check(saved['complete'] and saved['precision_bits']==384,'accepted pass identity')
        X = []
        raw = []
        for j in range(6):
            row = saved['moments'][j]
            check(row['j']==j,'moment identity '+str(j))
            box = endpoints(row['ball'])
            check(0<box[0]<=box[1],'positive compact moment '+str(j))
            X.append(box)
            raw.append({'j':j,'mid':row['ball']['mid'],'rad':row['ball']['rad']})
        C = [(F(1,16)-X[0][1],F(1,16)-X[0][0])]
        C.extend((X[j-1][0]-X[j][1],X[j-1][1]-X[j][0]) for j in range(1,6))
        for j,(lo,hi) in enumerate(C):
            check(lo>0,'positive reference C'+str(j))
        check(C[1][0]>F(1,3000),'C1 lower > 1/3000')
        record['compact_moment_dyadics'] = raw
        record['reference_boxes'] = [{'j':j,'lower':rational(lo),'upper':rational(hi),
                                       'lower_reading':reading(lo),'upper_reading':reading(hi)}
                                      for j,(lo,hi) in enumerate(C)]
        box = [(F(465,1000),F(466,1000)),(F(135,1000),F(137,1000)),
               (F(28,1000),F(29,1000)),(F(4,1000),F(5,1000))]
        ratios = []
        for j,(wantlo,wanthi) in zip(range(2,6),box):
            lo = C[0][0]**(j-1)*C[j][0]/C[1][1]**j
            hi = C[0][1]**(j-1)*C[j][1]/C[1][0]**j
            check(wantlo<=lo<=hi<=wanthi,'normalized ratio t'+str(j)+' in fixed box')
            ratios.append({'j':j,'lower':rational(lo),'upper':rational(hi),
                           'lower_reading':reading(lo),'upper_reading':reading(hi),
                           'required_lower':rational(wantlo),'required_upper':rational(wanthi)})
        record['normalized_ratios'] = ratios
        T = []
        tails = []
        for j in range(6):
            row = saved['tail_allowances'][j]
            check(row['j']==j,'tail identity '+str(j))
            el,eu = endpoints(row['E']);bl,bu = endpoints(row['B'])
            check(el>0 and bl>0,'positive E and nonzero B '+str(j))
            total = eu+bu
            scaled = total*2**384
            rounded = F(-((-scaled.numerator)//scaled.denominator),2**384)
            check(rounded>=total,'upward tail sum containment '+str(j))
            T.append(rounded)
            tails.append({'j':j,'E_mid':row['E']['mid'],'E_rad':row['E']['rad'],
                          'B_mid':row['B']['mid'],'B_rad':row['B']['rad'],
                          'upper_grid384':rational(rounded),'B_included':True})
        eps = F(1,40000)
        rel = [T[0]/C[0][0]]+[(T[j-1]+T[j])/C[j][0] for j in range(1,6)]
        for j,v in enumerate(rel):
            check(v<=eps,'entry-relative allowance <= 1/40000 at j='+str(j))
        record['tail_allowances'] = tails
        record['entry_relative_upper_bounds'] = [{'j':j,'exact':rational(v),'reading':reading(v)}
                                                 for j,v in enumerate(rel)]

        # Exact recurrence and independent permutation algebra in formal c.
        c = [variable(j,6) for j in range(6)]
        D = {0:poly_constant(1,6)}
        fpolys = {}
        for n in range(1,6):
            recurrence = {}
            for j in range(1,n+1):
                c0power = {(j-1,0,0,0,0,0):1}
                recurrence = add(recurrence,scale(multiply(multiply(c0power,c[j]),D[n-j]),(-1)**(j-1)))
            direct = determinant(n,1)
            check(recurrence==direct,'Hessenberg recurrence equals permutation expansion n='+str(n))
            D[n] = recurrence
            normalized = {}
            for e,a in recurrence.items():
                check(sum(e)==n and sum(j*e[j] for j in range(6))==n,
                      'determinant homogeneity n='+str(n)+' powers='+str(e))
                alpha = e[2:6]
                check(e[0]==sum((j-1)*e[j] for j in range(2,6)) and
                      e[1]==n-sum(j*e[j] for j in range(2,6)),
                      'normalization powers n='+str(n)+' powers='+str(e))
                normalized[alpha] = normalized.get(alpha,0)+a
            fpolys[n] = normalized
        expected = {
            2:{(0,0,0,0):1,(1,0,0,0):-1},
            3:{(0,0,0,0):1,(1,0,0,0):-2,(0,1,0,0):1},
            4:{(0,0,0,0):1,(1,0,0,0):-3,(2,0,0,0):1,(0,1,0,0):2,(0,0,1,0):-1},
            5:{(0,0,0,0):1,(1,0,0,0):-4,(2,0,0,0):3,(0,1,0,0):3,
               (1,1,0,0):-2,(0,0,1,0):-2,(0,0,0,1):1},
        }
        Spolys = {n:{e:abs(a) for e,a in p.items()} for n,p in expected.items()}
        for n in range(2,6):
            check(fpolys[n]==expected[n],'displayed f'+str(n)+' polynomial')
        joint = add(multiply(D[4],D[4]),scale(multiply(determinant(4,0),determinant(4,2)),-1))
        check(joint==multiply(D[5],D[3]),'degree-eight joint identity D4,1^2-D4,0*D4,2=D5,1*D3,1')
        check(all(sum(e)==8 for e in joint),'joint degree eight')
        record['exact_algebra'] = {'determinant_polynomials':{str(n):polynomial_record(D[n]) for n in range(2,6)},
                                   'normalized_f':{str(n):polynomial_record(p) for n,p in expected.items()},
                                   'absolute_coefficient_S':{str(n):polynomial_record(p) for n,p in Spolys.items()},
                                   'joint_terms':len(joint),'joint_identity':True}

        # Signs of each derivative throughout the entire coarse rational box.
        signs = {2:{0:-1},3:{0:-1,1:1},4:{0:-1,1:1,2:-1},5:{0:-1,1:1,2:-1,3:1}}
        exact_intervals = {2:(F('0.534'),F('0.535')),3:(F('0.203'),F('0.207')),
                           4:(F('0.060156'),F('0.067225')),5:(F('0.012648'),F('0.021265'))}
        convenient = {2:(F(1,2),F(3,5)),3:(F(1,5),F(1,4)),
                      4:(F(3,50),F(7,100)),5:(F(1,80),F(1,40))}
        Sup = {2:F(3,2),3:F(21,10),4:F(3),5:F(21,5)}
        margin_data = {}
        for n in range(2,6):
            derivatives = {}
            for j,sign in signs[n].items():
                dlo,dhi = interval_value(derivative(expected[n],j),box)
                check(dlo>0 if sign>0 else dhi<0,'derivative sign f'+str(n)+' t'+str(j+2))
                derivatives[str(j+2)] = {'lower':rational(dlo),'upper':rational(dhi),'sign':sign}
            minpoint = [lo if signs[n].get(j,0)>=0 else hi for j,(lo,hi) in enumerate(box)]
            maxpoint = [hi if signs[n].get(j,0)>=0 else lo for j,(lo,hi) in enumerate(box)]
            fmin,fmax = value(expected[n],minpoint),value(expected[n],maxpoint)
            check((fmin,fmax)==exact_intervals[n],'exact f'+str(n)+' endpoint values')
            flo,fhi = convenient[n]
            check(flo<fmin<=fmax<fhi,'convenient strict f'+str(n)+' bounds')
            smax = value(Spolys[n],[hi for lo,hi in box])
            check(smax<Sup[n],'S'+str(n)+' majorant bound')
            higher_sum = sum(comb(n,j) for j in range(2,n+1))
            check(higher_sum<=26 and 26*eps**2<eps,'higher-binomial-term bound n='+str(n))
            h = (1+eps)**n-1
            check(h<(n+1)*eps,'h_n < (n+1)/40000 n='+str(n))
            margin_data[str(n)] = {'derivatives':derivatives,'f_min':rational(fmin),'f_max':rational(fmax),
                                    'strict_floor':rational(flo),'strict_ceiling':rational(fhi),
                                    'S_max':rational(smax),'S_strict_upper':rational(Sup[n]),
                                    'h_exact':rational(h),'h_strict_upper':rational((n+1)*eps)}
        record['rational_box_lemma'] = margin_data
        bn = {n:(n+1)*eps*Sup[n] for n in range(2,6)}
        expected_bn = {2:F(9,80000),3:F(21,100000),4:F(3,8000),5:F(63,100000)}
        check(bn==expected_bn,'four determinant remainder bounds b_n')
        error3 = convenient[4][1]*bn[2]+convenient[2][1]*bn[4]+bn[2]*bn[4]
        error4 = convenient[5][1]*bn[3]+convenient[3][1]*bn[5]+bn[3]*bn[5]
        check(error3==F(149067,640000000) and error3<F(1,4000),'matched r=3 error sum (16)')
        check(error4==F(1628823,10**10) and error4<F(1,6000),'next-order r=4 error sum (17)')
        margin3 = convenient[4][0]*convenient[2][0]
        margin4 = convenient[5][0]*convenient[3][0]
        check(margin3==F(3,100) and margin4==F(1,400),'reference margin products')
        check(error3/margin3<F(1,120) and error4/margin4<F(1,15),'matched relative error bounds')
        check(F(1,4000)/margin3==F(1,120) and F(1,6000)/margin4==F(1,15),
              'stated conservative relative-budget table')
        floor = F(1,400)-F(1,6000)
        check(floor==F(7,3000),'lower allowance coefficient 7/3000')
        rational_floor = F(7,3000**9)
        target = F(3,10**31)
        check(floor*F(1,3000)**8==rational_floor and rational_floor>target,
              'final exact lower consequence > 3/10^31')
        record['closure'] = {'epsilon':str(eps),'b_n':{str(n):str(v) for n,v in bn.items()},
                             'r3_error_strict_upper':str(error3),'r4_error_strict_upper':str(error4),
                             'r3_margin_strict_lower':str(margin3),'r4_margin_strict_lower':str(margin4),
                             'r3_relative_strict_upper':'1/120','r4_relative_strict_upper':'1/15',
                             'r4_complete_error_strict_upper':'1/6000',
                             'r4_lower_coefficient':str(floor),'rational_lower_floor':str(rational_floor),
                             'rational_lower_floor_reading':reading(rational_floor),
                             'target_strict_lower':str(target),'target_verified':True,
                             'product_remainder_included':True,'degrees_paid':list(range(1,9))}
        record['scoped_growth_lemma'] = {
            'status':'analytically checked; no new moment acquisition or infinite-case numerical test',
            'domain':'j>=2, U=2, fixed compact first-mode reference and original E vector',
            'pointwise_ratio_upper':'4/[(2j)(2j-1)] <= 1/3',
            'coefficient_upper':'a0*4^(j-1)/(2j-2)!',
            'relative_lower':'K/(a*a0) * (2j-2)!/(4*a^2)^(j-1)',
            'successive_factor_ratio':'(2j)(2j-1)/(4*a^2) -> infinity',
            'conclusion':'no fixed uniformly small entry-relative epsilon at all indices',
            'does_not_exclude':['exact joint payment','canonical determinant positivity','all first-mode/Green estimates'],
        }
        record['status'] = 'passed fixed existing-data next-order verification'
    except FixedCheckFailure as exc:
        record['status'] = 'failed fixed premise'
        record['failure'] = str(exc)
    except RuntimeCap as exc:
        record['status'] = 'capped'
        record['failure'] = str(exc)
    except Exception as exc:
        record['status'] = 'implementation failure'
        record['failure'] = type(exc).__name__+': '+str(exc)
    finally:
        record['execution_seconds'] = time.perf_counter()-START
        record['cumulative_execution_seconds'] = previous_seconds+record['execution_seconds']
        signal.setitimer(signal.ITIMER_REAL,0)
        data = json.dumps(record,indent=2)+'\n'
        if len(data.encode())>=102400:
            raise SystemExit('Record exceeds fixed 100 KiB limit; acquisition inputs unchanged.')
        args.output.write_text(data)
        print(json.dumps({k:record.get(k) for k in ['status','failure','attempt','execution_seconds',
                                                    'cumulative_execution_seconds','integrand_evaluations']}))


if __name__ == '__main__':
    main()
