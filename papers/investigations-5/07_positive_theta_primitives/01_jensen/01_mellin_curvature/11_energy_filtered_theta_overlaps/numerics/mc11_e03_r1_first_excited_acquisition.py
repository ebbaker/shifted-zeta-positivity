#!/usr/bin/env python3
"""MC11-E03 r1: five n=2 source moments at 384 bits and common-path replay.

Prepared for Edward Baker, 4 November 2026, with substantial LLM assistance.
Actual model gpt-6.1-sol, effort ultra. Acquisition needs python-flint;
--verify uses only the Python standard library and trusts identified balls.
"""
import argparse
from fractions import Fraction as F
import hashlib
import importlib.util
import json
from math import comb, factorial
from pathlib import Path
import platform
import signal
import sys
import time

PARENT=Path('papers/investigations-5/07_positive_theta_primitives/01_jensen/01_mellin_curvature')
MC11=PARENT/'11_energy_filtered_theta_overlaps'
RGD=PARENT/'10_radial_green_determinants'
LOCKS={
    str(MC11/'numerics/MC11_E02_R1_SPECTRAL_SPLIT_20261104.json'):'2e33a57d09ae986343c3735fbad97c3a49c26a909b2f2b11f5b964c07de86d20',
    str(MC11/'numerics/mc11_e02_r1_spectral_split.py'):'4d0eff7733071967fe8af896889b75000522aefb5210501725ff8760166cb0da',
    str(MC11/'research-progress/handoffs/02_MC11_E02_RETURN_AND_E03_MODEL_CONTINUATION_20261104.md'):'f9f35d523e9f46372faf2b8203ed19c9e4bd5369370003f06dffab06bf757bc9',
    str(RGD/'numerics/rgd_e02_two_case_certificate.py'):'b4863a6840cd4d68b10fe993f3f4cdc5e66dd8b3d44903445b306a50c8879db4',
}
GOALS=[F(x) for x in ['8.8483e-15','3.6456e-18','1.5020e-21','6.1887e-25','2.5498e-28']]
BASE_COVER=[F(0),F(1,8),F(1,4),F(1,2),F(1),F(2)]
SECONDS=180
MAX_EVALUATIONS=200000
EVALUATIONS=0
ACQUISITION_START=0


class CapExceeded(RuntimeError):
    pass


def check_budget():
    if time.perf_counter()-ACQUISITION_START>=SECONDS:
        raise CapExceeded('180-second acquisition cap')
    if EVALUATIONS>=MAX_EVALUATIONS:
        raise CapExceeded('200000 callback cap')


def alarm(*_):
    raise CapExceeded('180-second acquisition cap')


def dyadic(pair):
    return F(int(pair[0]))*F(2)**int(pair[1])


def ball(row):
    m,r=dyadic(row['mid']),dyadic(row['rad'])
    assert r>=0
    return m-r,m+r


def pack(value):
    assert value.is_finite()
    return {'mid':[str(value.mid().man_exp()[0]),int(value.mid().man_exp()[1])],
            'rad':[str(value.rad().man_exp()[0]),int(value.rad().man_exp()[1])],
            'display':value.str(24)}


def ceil_grid384(value):
    scaled=value*2**384
    return F(-(-scaled.numerator//scaled.denominator),2**384)


def parse_iv(row):
    return F(row['lower']),F(row['upper'])


def load_inputs(repo):
    hashes={}
    for path,expected in LOCKS.items():
        h=hashlib.sha256((repo/path).read_bytes()).hexdigest()
        assert h==expected,('frozen input changed',path)
        hashes[path]=h
    old=json.loads((repo/MC11/'numerics/MC11_E02_R1_SPECTRAL_SPLIT_20261104.json').read_text())
    for path,expected in old['input_sha256'].items():
        h=hashlib.sha256((repo/path).read_bytes()).hexdigest()
        assert h==expected,('inherited input changed',path)
        hashes[path]=h
    sys.dont_write_bytecode=True
    spec=importlib.util.spec_from_file_location('mc11_frozen_e02',repo/MC11/'numerics/mc11_e02_r1_spectral_split.py')
    e02=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(e02)
    return old,e02,hashes


def parse_poly(rows):
    return {tuple(row['powers']):F(row['coefficient']) for row in rows}


def rational_replay(record,old,e02):
    checks=[]
    def check(name,condition):
        checks.append({'check':name,'passed':bool(condition)})
        if not condition:raise AssertionError(name)
    check('fixed 384-bit precision',record['precision_bits']==384)
    check('one acquisition and at most one subdivision refinement',1<=len(record['passes'])<=2)
    check('evaluation cap',record['total_callback_evaluations']<=MAX_EVALUATIONS)
    check('time cap',record['acquisition_seconds']<=SECONDS)
    complete=[p for p in record['passes'] if p.get('complete')]
    check('at least one complete five-moment enclosure',bool(complete))
    chosen=complete[-1]
    check('five moments only',len(chosen['moments'])==5)
    A=[]
    count=0
    for attempt,p in enumerate(record['passes']):
        expected_cover=BASE_COVER
        if attempt:
            expected_cover=sorted(set(BASE_COVER+[(a+b)/2 for a,b in zip(BASE_COVER,BASE_COVER[1:])]))
        check('fixed cover attempt '+str(attempt),p['cover']==[str(x) for x in expected_cover])
        count+=sum(s['callback_evaluations'] for m in p['moments'] for s in m['segments'])
    check('callback bookkeeping',count==record['total_callback_evaluations'])
    for j,m in enumerate(chosen['moments'],1):
        check('source moment index '+str(j),m['j']==j)
        check('complete segment cover '+str(j),len(m['segments'])==len(chosen['cover'])-1)
        lo,hi=F(0),F(0)
        for k,s in enumerate(m['segments']):
            check('segment order '+str((j,k)),s['index']==k)
            il,iu=ball(s['imag'])
            check('imaginary interval contains zero '+str((j,k)),il<=0<=iu)
            x,y=ball(s['real']);lo+=x;hi+=y
        compact=ball(m['compact_ball'])
        check('compact sum enclosure '+str(j),compact[0]<=lo<=hi<=compact[1])
        tail=ball(m['tail_majorant_ball'])
        payment=F(m['tail_upper_grid384'])
        check('nonzero spatial-tail bound '+str(j),tail[0]>0)
        check('upward grid spatial-tail payment '+str(j),payment==ceil_grid384(tail[1]) and payment>=tail[1])
        full=(compact[0],compact[1]+payment)
        check('full moment is compact plus [0,tail upper] '+str(j),full==parse_iv(m['full_box']))
        check('positive full source moment '+str(j),full[0]>0)
        check('reported full half-width '+str(j),F(m['half_width'])==(full[1]-full[0])/2)
        check('reported width target '+str(j),F(m['half_width_goal'])==GOALS[j-1])
        check('goal flag '+str(j),m['goal_met']==((full[1]-full[0])/2<=GOALS[j-1]))
        A.append(full)
    U=[F(x) for x in old['moment_upper_n2']]
    V=[F(x) for x in old['moment_upper_n_ge3']]
    for j,(a,u) in enumerate(zip(A,U),1):
        check('new moments inside old analytic upper bound '+str(j),0<a[0]<=a[1]<=u)
    b=[parse_iv(x) for x in old['ground_coefficient_boxes']]
    h=[(a[0],a[1]+v) for a,v in zip(A,V)]
    K=[parse_poly(x) for x in old['K_polynomials_in_b1_to_b5_h1_to_h5']]
    D=parse_poly(old['D3_polynomial'])
    G=[e02.derivative(D,j) for j in range(5)]
    check('unchanged five collected gradients',[parse_poly(x) for x in old['G_polynomials']]==G)
    bv=[e02.var(j,10) for j in range(5)]
    hv=[e02.var(j+5,10) for j in range(5)]
    along=[e02.add(x,y) for x,y in zip(bv,hv)]
    expected=[]
    for g in G:
        p=e02.substitute(g,along)
        expected.append({e:a/F(sum(e[5:])+1) for e,a in p.items()})
    check('unchanged integrated common-path cofactor polynomials',K==expected)
    endpoint=e02.add(e02.substitute(D,along),e02.scale(e02.substitute(D,bv),-1))
    response=e02.add(*(e02.mul(x,y) for x,y in zip(hv,K)))
    check('exact cubic endpoint identity',endpoint==response)
    check('exchange sign mutation rejected',e02.add(response,e02.scale(e02.mul(hv[1],K[1]),-2))!=endpoint)
    ki=[e02.interval_value(k,b+h) for k in K]
    signs=[1,-1,1,-1,1]
    check('integrated gradient signs retained',all(x[0]>0 if s>0 else x[1]<0 for s,x in zip(signs,ki)))
    L2=(F(0),F(0))
    for a,k in zip(A,ki):L2=e02.iv_add(L2,e02.iv_mul(a,k))
    kap=F(old['constants']['source_slopes_lower'][1])
    norm_tail=(ki[0][0]+ki[1][0]/kap**2+ki[3][0]/kap**6,
               ki[0][1]+ki[2][1]/kap**4+ki[4][1]/kap**8)
    check('complete n>=3 normalized lower positive',norm_tail[0]>0)
    tail=(F(0),min(norm_tail[1]*V[0],F(old['final_bounds']['Lge3']['upper'])))
    delta_split=e02.iv_add(L2,tail)
    delta_endpoint=e02.interval_value(endpoint,b+h)
    delta=(max(delta_split[0],delta_endpoint[0]),min(delta_split[1],delta_endpoint[1]))
    check('split and collected endpoint bounds overlap',delta[0]<=delta[1])
    d0=e02.interval_value(D,b)
    check('unchanged positive ground determinant',d0==parse_iv(old['final_bounds']['D3_ground']) and d0[0]>0)
    ratio=e02.iv_mul(delta,(1/d0[1],1/d0[0]))
    # Same source moments, with the entire s-path enclosed: no sign inferred from integration alone.
    cpath=[(x[0],x[1]+y[1]) for x,y in zip(b,h)]
    gi=[e02.interval_value(g,cpath) for g in G]
    point=(F(0),F(0))
    for a,g in zip(A,gi):point=e02.iv_add(point,e02.iv_mul(a,g))
    def sign(iv):
        return 'strictly positive' if iv[0]>0 else 'strictly negative' if iv[1]<0 else 'undetermined'
    return {
        'arithmetic':'exact Fraction propagation of serialized Arb balls and frozen E02 polynomials',
        'ground_boxes':[e02.out_interval(x) for x in b],
        'total_excited_h_boxes':[e02.out_interval(x) for x in h],
        'integrated_K_boxes':[e02.out_interval(x) for x in ki],
        'n_ge3_normalized_response':e02.out_interval(norm_tail),
        'final_bounds':{'L2':e02.out_interval(L2),'Lge3':e02.out_interval(tail),
                        'Delta3_from_split':e02.out_interval(delta_split),
                        'Delta3_from_collected_endpoint':e02.out_interval(delta_endpoint),
                        'Delta3':e02.out_interval(delta),'D3_ground':e02.out_interval(d0),
                        'Delta3_over_D3_ground':e02.out_interval(ratio),
                        'pointwise_n2_all_s':e02.out_interval(point)},
        'strict_signs':{'L2':sign(L2),'Lge3':'strictly positive; zero lower endpoint is open',
                        'Delta3':sign(delta),'pointwise_n2_all_s':sign(point),
                        'groups':'reinforce' if L2[0]>0 else 'oppose' if L2[1]<0 else 'undetermined'},
        'all_width_goals_met':all(m['goal_met'] for m in chosen['moments']),
        'checks':checks,
    }


def main():
    global EVALUATIONS,ACQUISITION_START
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--repo',type=Path,required=True)
    group=ap.add_mutually_exclusive_group(required=True)
    group.add_argument('--output',type=Path)
    group.add_argument('--verify',type=Path)
    args=ap.parse_args()
    old,e02,hashes=load_inputs(args.repo)
    if args.verify:
        d=json.loads(args.verify.read_text())
        assert d['code_sha256']==hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
        assert d['input_sha256']==hashes
        replay=rational_replay(d,old,e02)
        assert replay==d['exact_propagation']
        print(json.dumps({'status':'serialized acquisition and exact common-path replay verified',
                          'checks':len(replay['checks']),'record_sha256':hashlib.sha256(args.verify.read_bytes()).hexdigest(),
                          'scope':'Trusts identified Arb integration and source-tail constant evaluations; no integration rerun'}))
        return
    if args.output.exists():raise SystemExit('Refusing to overwrite an acquisition record')
    import flint
    from flint import arb,acb,ctx
    ctx.prec=384
    ctx.threads=1
    d={'task':'MC11-E03','request_revision':'r1','date':'2026-11-04','timezone':'America/New_York',
       'prepared_for':'Edward Baker','llm_assistance':True,'actual_model':'gpt-6.1-sol','reasoning_effort':'ultra',
       'thread_id':'01a1a8e5-1cb3-74b3-80a9-e4b99f6f4fab','turn_id':'01a1a988-130d-7d12-a635-ee7f7a94ed96',
       'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'input_sha256':hashes,
       'python_version':platform.python_version(),'python_executable':sys.executable,
       'python_flint_version':flint.__version__,'FLINT_version':flint.__FLINT_VERSION__,
       'precision_bits':384,'tolerance_bits':320,
       'limits':{'acquisitions':1,'subdivision_refinements':1,'seconds':SECONDS,'callback_evaluations':MAX_EVALUATIONS,
                 'degree_per_call':128,'evaluations_per_call':5000,'depth_per_call':20,'use_heap':True},
       'source':'phi_(4pi)=exp(u-X)*(2X^2-3X), X=4pi*exp(4u); normalized u^(2j)/(2j)!; no extra 1/8',
       'domain':'[0,2] validated quadrature plus rigorous source tail to infinity',
       'passes':[],'failures':[],'status':'started'}
    ACQUISITION_START=time.perf_counter()
    signal.signal(signal.SIGALRM,alarm)
    signal.setitimer(signal.ITIMER_REAL,SECONDS)
    try:
        pi=arb.pi()
        E=4*pi
        exp8=arb(8).exp()
        XU=E*exp8
        rate=4*XU-9
        prefactor=2*E**2*(arb(18)-XU).exp()
        assert rate>0 and prefactor>0
        d['constants']={name:pack(v) for name,v in [('pi',pi),('E',E),('exp8',exp8),('XU',XU),('source_tail_rate',rate),('source_tail_prefactor',prefactor)]}
        tail_balls=[]
        for j in range(1,6):
            bound=prefactor/factorial(2*j)*sum(
                (arb(comb(2*j,k)*2**(2*j-k)*factorial(k))/rate**(k+1) for k in range(2*j+1)),arb(0))
            assert bound>0
            tail_balls.append(bound)
        for attempt in range(2):
            cover=BASE_COVER if attempt==0 else sorted(set(BASE_COVER+[(a+b)/2 for a,b in zip(BASE_COVER,BASE_COVER[1:])]))
            p={'attempt':attempt,'cover':[str(v) for v in cover],'moments':[],'complete':False}
            d['passes'].append(p)
            pass_start=time.perf_counter()
            finite=True
            tolerance=arb(2)**(-320)
            for j in range(1,6):
                m={'j':j,'segments':[]}
                p['moments'].append(m)
                total=acb(0)
                for index,(left,right) in enumerate(zip(cover,cover[1:])):
                    before=EVALUATIONS
                    denominator=factorial(2*j)
                    def integrand(z,analytic):
                        global EVALUATIONS
                        check_budget()
                        EVALUATIONS+=1
                        X=acb(E)*(4*z).exp()
                        return z**(2*j)*(z-X).exp()*(2*X**2-3*X)/denominator
                    val=acb.integral(integrand,arb(left.numerator)/left.denominator,
                                     arb(right.numerator)/right.denominator,
                                     rel_tol=tolerance,abs_tol=tolerance,deg_limit=128,
                                     eval_limit=5000,depth_limit=20,use_heap=True)
                    segment={'index':index,'callback_evaluations':EVALUATIONS-before}
                    m['segments'].append(segment)
                    if not val.is_finite():
                        finite=False
                        segment['failure']='nonfinite integral enclosure'
                        break
                    assert val.imag.contains(0),'integral excludes reality'
                    segment.update({'real':pack(val.real),'imag':pack(val.imag)})
                    total+=val
                    check_budget()
                if not finite:break
                m['compact_ball']=pack(total.real)
                m['tail_majorant_ball']=pack(tail_balls[j-1])
                compact=ball(m['compact_ball'])
                tail_payment=ceil_grid384(ball(m['tail_majorant_ball'])[1])
                full=(compact[0],compact[1]+tail_payment)
                half=(full[1]-full[0])/2
                m.update({'tail_upper_grid384':str(tail_payment),'full_box':e02.out_interval(full),
                          'half_width':str(half),'half_width_reading':e02.out_interval((half,half))['upper_reading'],
                          'half_width_goal':str(GOALS[j-1]),'goal_met':half<=GOALS[j-1]})
            p['complete']=finite and len(p['moments'])==5 and all('full_box' in m for m in p['moments'])
            p['elapsed_seconds']=time.perf_counter()-pass_start
            if p['complete'] and all(m['goal_met'] for m in p['moments']):
                d['status']='validated five source moments; all E03 width goals met'
                break
            p['refinement_reason']='nonfinite enclosure or specified half-width target unmet'
        if d['status']=='started':
            d['status']='inconclusive within fixed 384-bit acquisition/refinement contract'
    except (AssertionError,ArithmeticError,RuntimeError,ValueError) as exc:
        d['status']='capped' if isinstance(exc,CapExceeded) else 'failed'
        d['failures'].append({'type':type(exc).__name__,'message':str(exc)})
    finally:
        signal.setitimer(signal.ITIMER_REAL,0)
        d['acquisition_seconds']=time.perf_counter()-ACQUISITION_START
        d['total_callback_evaluations']=EVALUATIONS
    if any(p.get('complete') for p in d['passes']):
        try:
            start=time.perf_counter()
            d['exact_propagation']=rational_replay(d,old,e02)
            d['replay_seconds']=time.perf_counter()-start
        except (AssertionError,ArithmeticError,RuntimeError,ValueError) as exc:
            d['failures'].append({'phase':'exact replay','type':type(exc).__name__,'message':str(exc)})
            d['status']='enclosed acquisition; replay failed'
    with args.output.open('x') as f:json.dump(d,f,indent=2);f.write('\n')
    summary={'status':d['status'],'passes':len(d['passes']),'callbacks':EVALUATIONS,
             'seconds':d['acquisition_seconds'],'failures':d['failures']}
    if 'exact_propagation' in d:
        r=d['exact_propagation']
        summary.update({'strict_signs':r['strict_signs'],'checks':len(r['checks']),
                        'bounds':{k:{a:v for a,v in x.items() if 'reading' in a} for k,x in r['final_bounds'].items()},
                        'moments':[{'j':m['j'],'lower':m['full_box']['lower_reading'],
                                    'upper':m['full_box']['upper_reading'],'half_width':m['half_width_reading']}
                                   for m in [p for p in d['passes'] if p.get('complete')][-1]['moments']]})
    print(json.dumps(summary))


if __name__=='__main__':
    main()
