#!/usr/bin/env python3
"""MC11-E04 r1: separate exact reconstruction; no imports from execution scripts.

Prepared for Edward Baker, 4 November 2026, with substantial LLM assistance.
Actual gpt-6.1-sol, effort ultra. Trusts identified acquired integral balls.
"""
import argparse
from fractions import Fraction as Q
import hashlib
import json
from math import comb,factorial
from pathlib import Path
import platform
import time

BASE=Path('papers/investigations-5/07_positive_theta_primitives/01_jensen/01_mellin_curvature')
MC=BASE/'11_energy_filtered_theta_overlaps'
RG=BASE/'10_radial_green_determinants'
VERSIONS=MC/'research-progress/handoffs/03_MC11_E04_R1_INPUT_VERSIONS_20261104.json'


def plus(*ps):
    out={}
    for p in ps:
        for m,c in p.items():out[m]=out.get(m,Q(0))+c
    return {m:c for m,c in out.items() if c}


def times(a,b):
    out={}
    for m,c in a.items():
        for n,d in b.items():
            key=tuple(sorted(m+n));out[key]=out.get(key,Q(0))+c*d
    return {m:c for m,c in out.items() if c}


def coeff(p,a):return {m:c*a for m,c in p.items() if c*a}


def v(j):return {(j,):Q(1)}


def replace(p,images):
    out={}
    for m,c in p.items():
        term={():c}
        for j in m:term=times(term,images[j])
        out=plus(out,term)
    return out


def from_terms(rows):
    out={}
    for row in rows:
        m=tuple(j+1 for j,k in enumerate(row['powers']) for _ in range(k))
        out[m]=Q(row['coefficient'])
    return out


def multiply_iv(a,b):
    values=[x*y for x in a for y in b]
    return min(values),max(values)


def add_iv(a,b):return a[0]+b[0],a[1]+b[1]


def divide_positive(a,b):
    assert b[0]>0
    return multiply_iv(a,(1/b[1],1/b[0]))


def evaluate(p,boxes):
    out=(Q(0),Q(0))
    for monomial,c in p.items():
        term=(c,c)
        for j in monomial:term=multiply_iv(term,boxes[j-1])
        out=add_iv(out,term)
    return out


def pair(x):return Q(int(x[0]))*Q(2)**int(x[1])


def saved_ball(x):
    m,r=pair(x['mid']),pair(x['rad'])
    assert r>=0
    return m-r,m+r


def saved_iv(x):return Q(x['lower']),Q(x['upper'])


def grid_ceil(x,bits):
    a=x*2**bits
    return Q(-(-a.numerator//a.denominator),2**bits)


def contains(outer,inner):return outer[0]<=inner[0]<=inner[1]<=outer[1]


def packed(x):return {'lower':str(x[0]),'upper':str(x[1])}


def normalized(weights,kappa):
    return (weights[0][0]+weights[1][0]/kappa**2+weights[3][0]/kappa**6,
            weights[0][1]+weights[2][1]/kappa**4+weights[4][1]/kappa**8)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo',required=True,type=Path)
    parser.add_argument('--output',required=True,type=Path)
    args=parser.parse_args()
    if args.output.exists():raise SystemExit('Refusing to overwrite an assessment record')
    start=time.perf_counter();checks=[]
    def check(name,condition):
        checks.append({'check':name,'passed':bool(condition)})
        if not condition:raise AssertionError(name)
    manifest=json.loads((args.repo/VERSIONS).read_text())
    for path,sha in manifest['input_sha256_relative_to_repository'].items():
        check('frozen SHA-256 '+path,hashlib.sha256((args.repo/path).read_bytes()).hexdigest()==sha)
    old=json.loads((args.repo/MC/'numerics/MC11_E02_R1_SPECTRAL_SPLIT_20261104.json').read_text())
    acquired=json.loads((args.repo/MC/'numerics/MC11_E03_R1_FIRST_EXCITED_ACQUISITION_20261104.json').read_text())
    rg=json.loads((args.repo/RG/'numerics/RGD_E02_R2_NEXT_ORDER_EXISTING_DATA_20261104.json').read_text())
    X=[saved_ball(x) for x in rg['compact_moment_dyadics']]
    C=[(Q(1,16)-X[0][1],Q(1,16)-X[0][0])]
    C += [(X[j-1][0]-X[j][1],X[j-1][1]-X[j][0]) for j in range(1,6)]
    B=[]
    for j,row in enumerate(rg['tail_allowances']):
        b=saved_ball({'mid':row['B_mid'],'rad':row['B_rad']})
        check('positive inherited ground spatial bound '+str(j),b[0]>0)
        B.append(grid_ceil(b[1],384))
    b=[(C[j][0]-B[j],C[j][1]+B[j-1]) for j in range(1,6)]
    check('ground boxes rebuilt from primitive dyadics',b==[saved_iv(x) for x in old['ground_coefficient_boxes']])
    p=acquired['passes'][0]
    cover=['0','1/8','1/4','1/2','1','2']
    check('one completed acquisition no refinement',len(acquired['passes'])==1 and p['complete'])
    check('fixed cover',p['cover']==cover)
    check('fixed precision tolerance software',acquired['precision_bits']==384 and acquired['tolerance_bits']==320
          and acquired['python_flint_version']=='0.9.0' and acquired['FLINT_version']=='3.6.0')
    check('five moment indices only',[m['j'] for m in p['moments']]==list(range(1,6)))
    check('resource limits and no acquisition failure',not acquired['failures'] and acquired['acquisition_seconds']<180
          and acquired['total_callback_evaluations']==1991 and acquired['total_callback_evaluations']<200000)
    check('callback count matches segment records',sum(s['callback_evaluations'] for m in p['moments'] for s in m['segments'])==1991)
    const={k:saved_ball(x) for k,x in acquired['constants'].items()}
    check('coarse pi and energy brackets',3<const['pi'][0]<=const['pi'][1]<Q(13,4)
          and 12<const['E'][0]<=const['E'][1]<13)
    check('E encloses four pi',contains(const['E'],(4*const['pi'][0],4*const['pi'][1])))
    check('XU encloses E exp8',contains(const['XU'],multiply_iv(const['E'],const['exp8'])))
    check('rate encloses 4 XU minus 9',contains(const['source_tail_rate'],(4*const['XU'][0]-9,4*const['XU'][1]-9)))
    check('coarse exterior proof constants',const['exp8'][0]>256 and const['source_tail_rate'][0]>1
          and 2*13**2<2**9 and 18-12*256==-3054 and 11*2**10<2**14)
    check('independent analytic grid payment',Q(2)**(-3031)<Q(2)**(-384))
    A=[]
    goals=[Q(x) for x in ['8.8483e-15','3.6456e-18','1.5020e-21','6.1887e-25','2.5498e-28']]
    for j,m in enumerate(p['moments'],1):
        check('five ordered segments '+str(j),[s['index'] for s in m['segments']]==list(range(5)))
        total=(Q(0),Q(0))
        for k,s in enumerate(m['segments']):
            total=add_iv(total,saved_ball(s['real']))
            im=saved_ball(s['imag'])
            check('imaginary enclosure contains reality '+str((j,k)),im[0]<=0<=im[1])
        compact=saved_ball(m['compact_ball'])
        check('compact sum contains serialized cover '+str(j),contains(compact,total))
        bound=saved_ball(m['tail_majorant_ball'])
        rate=const['source_tail_rate'];pref=const['source_tail_prefactor']
        # Exact monotone evaluation of the saved positive bound expression.
        lower=sum(Q(comb(2*j,k)*2**(2*j-k)*factorial(k),factorial(2*j))/rate[1]**(k+1) for k in range(2*j+1))*pref[0]
        upper=sum(Q(comb(2*j,k)*2**(2*j-k)*factorial(k),factorial(2*j))/rate[0]**(k+1) for k in range(2*j+1))*pref[1]
        check('serialized source tail encloses bound expression '+str(j),contains(bound,(lower,upper)))
        payment=Q(m['tail_upper_grid384'])
        check('positive bound and exact upward grid '+str(j),bound[0]>0 and payment==grid_ceil(bound[1],384)==Q(2)**(-384))
        full=(compact[0],compact[1]+payment)
        check('full moment uses zero to upper tail '+str(j),full==saved_iv(m['full_box']))
        check('full half-width meets goal '+str(j),0<full[0] and (full[1]-full[0])/2==Q(m['half_width'])<goals[j-1])
        A.append(full)

    # Fresh cofactor construction: monomials are sorted variable labels, not power vectors.
    matrix=[[v(3+j-i) for j in range(3)] for i in range(3)]
    cofactor=[]
    for i in range(3):
        row=[]
        for j in range(3):
            minor=[[matrix[a][z] for z in range(3) if z!=j] for a in range(3) if a!=i]
            d=plus(times(minor[0][0],minor[1][1]),coeff(times(minor[0][1],minor[1][0]),-1))
            row.append(coeff(d,(-1)**(i+j)))
        cofactor.append(row)
    D=plus(*(times(matrix[0][j],cofactor[0][j]) for j in range(3)))
    G=[{} for _ in range(5)]
    for i in range(3):
        for j in range(3):G[3+j-i-1]=plus(G[3+j-i-1],cofactor[i][j])
    check('D3 from first-row cofactor expansion',D==from_terms(old['D3_polynomial']))
    check('G1 to G5 from all nine cofactors',G==[from_terms(x) for x in old['G_polynomials']])
    def Bij(i,j):
        return plus(times(v(i),v(j)),coeff(times(v(i),v(j+5)),Q(1,2)),
                    coeff(times(v(i+5),v(j)),Q(1,2)),coeff(times(v(i+5),v(j+5)),Q(1,3)))
    K=[]
    for g in G:
        total={}
        for m,c in g.items():
            assert len(m)==2
            total=plus(total,coeff(Bij(*m),c))
        K.append(total)
    check('K from exact integrated product formula',K==[from_terms(x) for x in old['K_polynomials_in_b1_to_b5_h1_to_h5']])
    mapping={j:plus(v(j),v(j+5)) for j in range(1,6)}
    mapping0={j:v(j) for j in range(1,6)}
    endpoint=plus(replace(D,mapping),coeff(replace(D,mapping0),-1))
    response=plus(*(times(v(j+6),K[j]) for j in range(5)))
    check('response equals collected cubic endpoint',endpoint==response)
    # Reverse only the determinant leg's true exchange term -2 c2 c3 c4.
    mutated_D=plus(D,{(2,3,4):Q(4)})
    mutated_endpoint=plus(replace(mutated_D,mapping),coeff(replace(mutated_D,mapping0),-1))
    defect=plus(mutated_endpoint,coeff(response,-1))
    expected_defect=coeff(plus(replace({(2,3,4):Q(1)},mapping),coeff({(2,3,4):Q(1)},-1)),4)
    check('true determinant exchange sign mutation rejected',bool(defect) and defect==expected_defect and len(defect)==7)

    U=[Q(x) for x in old['moment_upper_n2']]
    V=[Q(x) for x in old['moment_upper_n_ge3']]
    pi=saved_iv(old['constants']['pi'])
    e4,e7,e9=[saved_iv(old['constants'][k]) for k in ['exp_minus_4pi','exp_minus_7pi','exp_minus_9pi']]
    check('n2 primitive-majorant formula',U==[e4[1]/(8*(16*pi[0]-1)**(2*j-1)) for j in range(1,6)])
    check('full n>=3 geometric-majorant formula',V==[e9[1]/(8*(1-e7[1])*(36*pi[0]-1)**(2*j-1)) for j in range(1,6)])
    kap2,kap3=[Q(x) for x in old['constants']['source_slopes_lower']]
    slope=lambda E:4*E-9-Q(12)/(2*E-3)
    check('source slope constants',kap2==slope(4*pi[0]) and kap3==slope(9*pi[0]) and kap3>100)
    old_h=[(Q(0),u+w) for u,w in zip(U,V)]
    old_K=[evaluate(k,b+old_h) for k in K]
    old_G=[evaluate(g,[(x[0],x[1]+y[1]) for x,y in zip(b,old_h)]) for g in G]
    check('E02 integrated K boxes independently reconstructed',old_K==[saved_iv(x) for x in old['integrated_K_boxes']])
    check('E02 whole-path G boxes independently reconstructed',old_G==[saved_iv(x) for x in old['whole_path_G_boxes']])
    check('every n>=3 level positive for every s',normalized(old_G,kap3)[0]>0)
    def independent(group):
        return (sum(min(Q(0),iv[0])*u for iv,u in zip(old_K,group)),
                sum(max(Q(0),iv[1])*u for iv,u in zip(old_K,group)))
    raw2=independent(U);raw3=independent(V)
    norm2,norm3=normalized(old_K,kap2),normalized(old_K,kap3)
    old_L2=(max(raw2[0],min(Q(0),norm2[0])*U[0]),
            min(raw2[1],max(Q(0),norm2[1])*U[0]))
    old_tail=(Q(0),min(raw3[1],norm3[1]*V[0]))
    check('E02 retained inconclusive n2 interval',old_L2==saved_iv(old['final_bounds']['L2']) and old_L2[0]<0<old_L2[1])
    check('E02 complete positive-group allowance',old_tail==saved_iv(old['final_bounds']['Lge3']) and norm3[0]>0)
    h=[(a[0],a[1]+w) for a,w in zip(A,V)]
    new_K=[evaluate(k,b+h) for k in K]
    recorded=acquired['exact_propagation']
    check('E03 refined common K boxes',new_K==[saved_iv(x) for x in recorded['integrated_K_boxes']])
    L2=(Q(0),Q(0))
    for a,k in zip(A,new_K):L2=add_iv(L2,multiply_iv(a,k))
    norm=normalized(new_K,kap3)
    check('strict positive higher-group normalized margin',norm[0]>0)
    tail=(Q(0),min(old_tail[1],norm[1]*V[0]))
    delta_split=add_iv(L2,tail)
    delta_endpoint=evaluate(endpoint,b+h)
    delta=(max(delta_split[0],delta_endpoint[0]),min(delta_split[1],delta_endpoint[1]))
    d0=evaluate(D,b)
    ratio=divide_positive(delta,d0)
    current_G=[evaluate(g,[(x[0],x[1]+y[1]) for x,y in zip(b,h)]) for g in G]
    point=(Q(0),Q(0))
    for a,g in zip(A,current_G):point=add_iv(point,multiply_iv(a,g))
    final={'L2':L2,'Lge3':tail,'Delta3_from_split':delta_split,
           'Delta3_from_collected_endpoint':delta_endpoint,'Delta3':delta,
           'D3_ground':d0,'Delta3_over_D3_ground':ratio,'pointwise_n2_all_s':point}
    for name,iv in final.items():
        check('E03 exact output reproduced '+name,iv==saved_iv(recorded['final_bounds'][name]))
    check('positive integrated first excited net and reference',L2[0]>0 and delta[0]>0 and d0[0]>0)
    check('first excited pointwise sign for all s',point[0]>0)
    for name,lo,hi in [('L2','2.22665020868e-33','2.22665020869e-33'),
                       ('Delta3','2.22665020e-33','2.22665075e-33'),
                       ('D3_ground','1.66142398817e-28','1.66142398818e-28'),
                       ('Delta3_over_D3_ground','1.34020588635e-5','1.34020621148e-5'),
                       ('pointwise_n2_all_s','2.2266193e-33','2.2266811e-33')]:
        check('outward reported decimal bounds '+name,Q(lo)<final[name][0]<=final[name][1]<Q(hi))
    check('outward full higher-group bound',tail[1]<Q('5.402e-40'))
    check('spectral fraction and percent dominance',tail[1]/delta[0]<Q('2.427e-7')
          and 100*(1-Q('2.427e-7'))==Q('99.99997573'))
    result={
        'task':'MC11-E04','request_revision':'r1','date':'2026-11-04','timezone':'America/New_York',
        'prepared_for':'Edward Baker','llm_assistance':True,'actual_model':'gpt-6.1-sol','reasoning_effort':'ultra',
        'thread_id':'01a1a8e5-1cb3-74b3-80a9-e4b99f6f4fab','turn_id':'01a1a9d5-044d-7ee1-a1e3-7a415581b884',
        'input_manifest_sha256':hashlib.sha256((args.repo/VERSIONS).read_bytes()).hexdigest(),
        'input_sha256':manifest['input_sha256_relative_to_repository'],
        'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'python_version':platform.python_version(),'arithmetic':'standard-library Fraction only; no execution-script helpers imported',
        'integrand_evaluations':0,'new_moments':0,'local_corrections':0,
        'coarse_source_tail_proof':{'prefactor_strict_upper':'2^-3045','polynomial_sum_strict_upper':'2^14',
                                   'actual_source_tail_strict_upper':'2^-3031','retained_grid_payment':'2^-384'},
        'exchange_mutation_defect':[{'variables':list(m),'coefficient':str(c)} for m,c in sorted(defect.items())],
        'exact_final_bounds':{k:packed(iv) for k,iv in final.items()},
        'tail_fraction_strict_upper':str(tail[1]/delta[0]),
        'checks':checks,'status':'all fixed E04 exact reconstruction checks passed',
        'trust_limits':'Shared identified Arb integration/constant balls; same-model internal assessment, no specialist independence',
        'execution_seconds':time.perf_counter()-start,
    }
    with args.output.open('x') as f:json.dump(result,f,indent=2);f.write('\n')
    print(json.dumps({'status':result['status'],'checks':len(checks),'seconds':result['execution_seconds'],
                      'local_corrections':0,'new_integrand_evaluations':0,
                      'exchange_mutation_defect_terms':len(defect)}))


if __name__=='__main__':
    main()
