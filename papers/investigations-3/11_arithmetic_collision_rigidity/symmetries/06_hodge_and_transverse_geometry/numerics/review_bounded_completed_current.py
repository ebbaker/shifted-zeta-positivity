#!/usr/bin/env python3
"""Separate same-model S06-T2 exact-record and replay review.

19 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Actual model gpt-6.1-sol (Codex), effort ultra. No specialist human review.
This reviews producer records; it is not an alternative physical quadrature.
"""
import argparse
import copy
from fractions import Fraction as F
import hashlib
import importlib.util
import json
import math
from pathlib import Path

EXPECTED_PRODUCER='650adaabcc1f9c42191e1d5e19e8c0200817cd6d2b476ed1ffe421555effe692'
EXPECTED_CONTRACT='9c2c36808de7167cb29c64b8ac8bba023ec126c6b17f97b5af656cdb1de5d73e'
EXPECTED_BASE='e96feb2b4c3e84de3025713b486fb8cf99fdd810f61366b79a0da188eb12535f'
BASE=Path('papers/investigations-3/11_arithmetic_collision_rigidity/numerics/high_height_consumer/high_height_consumer.py')

def digest(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def canonical(d):return hashlib.sha256(json.dumps(d,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def check(c,msg):
    if not c:raise ArithmeticError(msg)
def dy(v):
    check(set(v)=={'mantissa','exponent'},'dyadic keyset')
    check(isinstance(v['mantissa'],str)and isinstance(v['exponent'],int),'dyadic types')
    e=v['exponent'];m=int(v['mantissa']);check(abs(e)<100000,'dyadic exponent bound')
    return F(m)*(F(2)**e)
def ep(v):return dy(v['dyadic'])
def iv(v):
    m=dy(v['midpoint']);r=dy(v['radius']);check(r>=0,'negative radius')
    return m-r,m+r
def add(a,b):return a[0]+b[0],a[1]+b[1]
def mul(a,b):
    z=[x*y for x in a for y in b];return min(z),max(z)
def neg(a):return -a[1],-a[0]
def subset(a,b):return b[0]<=a[0]<=a[1]<=b[1]
def normmax(a):return max(abs(a[0]),abs(a[1]))
def dist(a):return max(a[0],-a[1],F(0))
def numeric(d):
    if isinstance(d,dict):return {k:numeric(v)for k,v in d.items()if k not in {'seconds','jet_seconds','consumer_seconds','total_seconds'}}
    if isinstance(d,list):return[numeric(v)for v in d]
    return d

def validate(r,repo,producer,contract):
    check(r['schema']=='s06-t2-bounded-completed-current-v1'and r['status']=='pass','record schema/status')
    bits=r['actual_precision_bits'];check(bits in (192,256),'precision')
    check(bool(r['actual_model'].strip())and bool(r['actual_effort'].strip()),'model metadata')
    check(r['producer_sha256']==digest(producer)==EXPECTED_PRODUCER,'producer pin')
    check(r['base_sha256']==digest(repo/BASE)==EXPECTED_BASE,'base pin')
    check(r['contract_sha256']==digest(contract)==EXPECTED_CONTRACT,'contract pin')
    check(r['contract_file']==contract.name,'contract filename')
    spec=importlib.util.spec_from_file_location('s06_review_base',repo/BASE)
    base=importlib.util.module_from_spec(spec);spec.loader.exec_module(base)
    check(r['source_pins']==base.source_pins(repo),'complete current source pin set')
    settings=r['settings'];s=settings['frozen'];pre=settings['predeclared']
    check(settings['domain']=={'t':['1/100','1/5'],'x':['999','1001']},'domain')
    check(settings['midpoint']==['21/200','1000'],'midpoint')
    check(settings['normalization']=='fixed Gc=1000^(7/4)exp(-125*pi); never differentiated','normalizer')
    check(s=={'d':'pi/8-4*log(1000)/1000','U':2,'first_omitted_mode':12,'retained_modes':[1,11],'spatial_degree':24,'time_degree':12,'midpoint_orders':[0,51],'common_moment_order':53},'frozen parameters')
    check(pre['bits']==bits and pre['refinement']is False and pre['consumer_calls']==64,'execution contract')
    check(pre['setup_seconds_limit']==60 and pre['setup_callback_limit']==2000000 and pre['per_integral_eval_limit']==200000 and pre['depth_limit']==30,'bounded work')
    check(pre['midpoint_abs_tol_norm']=='1e-13'and pre['midpoint_rel_tol']=='1e-30','quadrature tolerances')
    setup=r['setup'];coeff=setup['midpoint_jets']
    check(len(coeff)==52 and [v['j']for v in coeff]==list(range(52)),'52 ordered midpoint coefficients')
    check(len(setup['uniform_mode_tails'])==len(setup['uniform_source_tails'])==4,'four physical tails')
    check(len(setup['all_order_mode_tails'])==len(setup['all_order_source_tails'])==54,'all-order tails through53')
    check(setup['callbacks']<=2000000 and setup['seconds']<=60,'observed bounded setup')
    check(len(setup['jet_callbacks'])==len(setup['jet_seconds'])==52,'quadrature cost ledger')
    check(all(dy(c['quadrature_radius'])>=0 for c in coeff),'nonnegative quadrature radii')
    for c in coeff:dy(c['midpoint'])
    check(ep(setup['common_moment'])>0,'positive independent moment')
    check(F(0)<=ep(setup['whole_box_taylor'])<F(1,10**9),'whole-box Taylor subbudget')
    for key in ('uniform_mode_tails','uniform_source_tails','all_order_mode_tails','all_order_source_tails'):
        check(all(ep(v)>=0 for v in setup[key]),'nonnegative tail')
    times=[F(1,100)+F(19*k,400)for k in range(5)];xs=[F(999)+F(k,8)for k in range(17)]
    cover=settings['cell_cover']
    check(cover=={'time_cuts':[str(t)for t in times],'x_cuts':[str(x)for x in xs],'closed':True,'cells':64},'declared exact cover')
    cells=r['cells'];check(len(cells)==64,'64 complete cells')
    check([v['index']for v in cells]==[[ti,xi]for ti in range(4)for xi in range(16)],'ordered complete cover')
    signed=0;strict=0;minsC=[];minsD=[];failed=[];maxerror=F(0)
    for row in cells:
        ti,xi=row['index'];t0,t1=times[ti:ti+2];x0,x1=xs[xi:xi+2]
        check(list(map(F,row['t']))==[t0,t1]and list(map(F,row['x']))==[x0,x1],'closed cell geometry')
        check(len(row['jets'])==len(row['budgets'])==4,'four complete physical jets')
        jets=list(map(iv,row['jets']));beta=iv(row['beta']);aa=iv(row['coefficient_a']);bb=iv(row['coefficient_b']);rr=iv(row['residual'])
        nominal_beta=(2*t0*x0/(165+4*t1+x1*x1),2*t1*x1/(165+4*t0+x0*x0))
        check(subset(nominal_beta,beta),'outward beta')
        check(subset(add(neg(jets[2]),mul(beta,jets[3])),aa),'outward coefficient a')
        check(subset(add(jets[1],neg(mul(beta,jets[2]))),bb),'outward coefficient b')
        check(subset(add(mul(jets[0],aa),mul(jets[1],bb)),rr),'outward complete current interval')
        rlo=ep(row['residual_lower']);M=ep(row['denominator_upper'])
        check(rlo<=rr[0]and M>=0 and M*M>=normmax(aa)**2+normmax(bb)**2,'outward residual/denominator endpoints')
        radii=[ep(v)for v in row['distances_to_zero']]
        check(all(F(0)<=radii[j]<=dist(jets[j])for j in (0,1)),'firstjet distances conservative')
        dball=iv(row['direct_radius']);cball=iv(row['current_radius']);direct2=sum(d*d for d in radii)
        check(dball[0]>=0 and dball[0]**2<=direct2<=dball[1]**2,'direct radius sqrt enclosure')
        positive=rr[0]>0
        check(row['independently_signed']==positive,'current sign decision')
        if positive:
            signed+=1;check(M>0 and subset((rlo/M,rlo/M),cball),'current extracted radius')
            check(cball[1]<F(69,125)*dball[0]and row['strict_current_below_direct']is True,'strict percell current/direct ratio below0.552')
            strict+=1
        else:
            failed.append(row['index']);check(cball==(F(0),F(0))and row['strict_current_below_direct']is None,'failed current remains failure')
        check(row['no_gain']is True,'percell no-gain status')
        es=[];ms=[]
        R=max(abs(x0-1000),abs(x1-1000));delta=max(abs(t0-F(21,200)),abs(t1-F(21,200)))
        for j,budget in enumerate(row['budgets']):
            values={k:ep(budget[k])for k in ('quadrature','taylor','mode','source','total')}
            check(all(v>=0 for v in values.values()),'nonnegative error ledger')
            check(values['total']>=sum(values[k]for k in ('quadrature','taylor','mode','source')),'complete source error sum')
            check(values['total']<F(1,10**8),'component error target')
            check(values['total']<[F(5171,10**15),F(4020,10**15),F(3607,10**15),F(3363,10**15)][j],'reported component-error ceiling')
            exactQ=sum((R**l*delta**k*dy(coeff[j+l+2*k]['quadrature_radius'])/math.factorial(l)/math.factorial(k)for l in range(25)for k in range(13)),F(0))
            check(values['quadrature']>=exactQ,'full quadrature-radius propagation including order51')
            check(values['mode']==ep(setup['uniform_mode_tails'][j])and values['source']==ep(setup['uniform_source_tails'][j]),'own derivative-order tails')
            image=iv(budget['polynomial_image']);e=values['total']
            check(subset((image[0]-e,image[1]+e),jets[j]),'complete jet contains image plus paid error')
            es.append(e);ms.append(image);maxerror=max(maxerror,e)
        def B(i,j):return normmax(ms[i])*es[j]+normmax(ms[j])*es[i]+es[i]*es[j]
        exactEr=B(1,1)+B(0,2)+normmax(beta)*(B(1,2)+B(0,3))
        check(ep(row['residual_added_approximation_error_upper'])>=exactEr,'complete quadratic current-error ledger')
        check(ep(row['residual_added_approximation_error_upper'])<F(2906,10**15),'reported residual-error ceiling')
        minsC.append(cball[0]);minsD.append(dball[0])
    summary=r['summary']
    check(summary['cells']==summary['consumer_calls']==64 and summary['coverage_verified']is True,'summary cover')
    check(summary['independently_signed_cells']==signed and summary['failed_current_cells']==64-signed,'summary signs')
    check(summary['strictly_smaller_current_radius_cells']==strict and summary['all_cells_no_current_radius_gain']is True,'summary no gain')
    check(ep(summary['minimum_current_radius'])<=min(minsC),'current minimum conservatively rounded')
    check(F(0)<ep(summary['minimum_direct_radius'])<=min(minsD),'direct minimum conservatively rounded')
    check(ep(summary['maximum_added_component_error_norm'])==maxerror,'maximum complete error')
    check(summary['midpoint_quadratures']==52 and summary['additional_h3_midpoint_quadratures_vs_old_setup']==1,'additional h3 work charged')
    return {'bits':bits,'signed_cells':signed,'failed_cells':failed,'strict_current_loss_cells':strict,'current_uniform_radius':str(min(minsC)),'direct_uniform_radius_lower_decimal':summary['minimum_direct_radius']['value'],'exact_record_arithmetic':'64 cells x four jet payments checked with Fraction; current/Cauchy/direct and quadratic-error interval containment checked with Fraction'}

def adversarial(r,repo,producer,contract):
    fixtures=[]
    def challenge(label,change):
        altered=copy.deepcopy(r);change(altered)
        try:validate(altered,repo,producer,contract)
        except (ArithmeticError,KeyError,ValueError,TypeError,IndexError):fixtures.append(label)
        else:raise ArithmeticError('invalid fixture accepted: '+label)
    challenge('unsupported precision',lambda d:d.update(actual_precision_bits=160))
    challenge('blank model',lambda d:d.update(actual_model=''))
    challenge('stale producer',lambda d:d.update(producer_sha256='0'*64))
    challenge('stale base',lambda d:d.update(base_sha256='0'*64))
    challenge('stale contract',lambda d:d.update(contract_sha256='0'*64))
    challenge('empty source pins',lambda d:d.update(source_pins={}))
    challenge('missing source pin',lambda d:d['source_pins'].pop(next(iter(d['source_pins']))))
    challenge('changed domain',lambda d:d['settings']['domain'].update(x=['999','1002']))
    challenge('changed frozen shift',lambda d:d['settings']['frozen'].update(d='0'))
    challenge('changed source cutoff',lambda d:d['settings']['frozen'].update(first_omitted_mode=11))
    challenge('missing h3 coefficient',lambda d:d['setup']['midpoint_jets'].pop())
    challenge('duplicate coefficient order',lambda d:d['setup']['midpoint_jets'][1].update(j=0))
    challenge('negative quadrature radius',lambda d:d['setup']['midpoint_jets'][0]['quadrature_radius'].update(mantissa='-1'))
    challenge('missing h3 tail',lambda d:d['setup']['uniform_source_tails'].pop())
    challenge('missing order53 majorant tail',lambda d:d['setup']['all_order_mode_tails'].pop())
    challenge('missing closed cell',lambda d:d['cells'].pop())
    challenge('gapped closed geometry',lambda d:d['cells'][0].update(x=['999','1000']))
    challenge('negative complete jet radius',lambda d:d['cells'][0]['jets'][0]['radius'].update(mantissa='-1'))
    challenge('missing fourth jet',lambda d:d['cells'][0]['jets'].pop())
    challenge('false current sign',lambda d:d['cells'][0].update(independently_signed=False))
    challenge('negative component payment',lambda d:d['cells'][0]['budgets'][0]['total']['dyadic'].update(mantissa='-1'))
    challenge('removed derivative-order tail',lambda d:d['cells'][0]['budgets'][3]['source']['dyadic'].update(mantissa='0'))
    return fixtures

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--repo',type=Path,required=True);p.add_argument('--producer',type=Path,required=True);p.add_argument('--contract',type=Path,required=True);p.add_argument('--record-dir',type=Path,required=True);p.add_argument('--replay-dir',type=Path,required=True);p.add_argument('--note',type=Path,required=True);p.add_argument('--controls',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    rows=[];records=[]
    for bits in (192,256):
        stored=a.record_dir/f'S06_T2_BOUNDED_CURRENT_{bits}_20261019.json';replay=a.replay_dir/f'S06_T2_REVIEW_REPLAY_{bits}_20261019.json'
        r=json.loads(stored.read_text());fresh=json.loads(replay.read_text())
        check(numeric(r)==numeric(fresh),'fresh replay differs mathematically')
        result=validate(r,a.repo,a.producer,a.contract)
        result.update(stored_sha256=digest(stored),stored_canonical_sha256=canonical(r),fresh_replay_sha256=digest(replay),numeric_canonical_sha256=canonical(numeric(r)),separate_full_replay_numeric_identity=True)
        rows.append(result);records.append(r)
    guards=adversarial(records[0],a.repo,a.producer,a.contract)
    controls=json.loads(a.controls.read_text());check(controls['status']=='pass'and controls['producer_sha256']==digest(a.producer),'reviewed producer controls identity')
    result={'status':'pass','date':'2026-10-19','prepared_for':'Edward Baker','actual_model':'gpt-6.1-sol (Codex)','actual_effort':'ultra','llm_assistance':'substantial; separate same-model internal review; no human specialist review','reviewer_script_sha256':digest(__file__),'producer_sha256':digest(a.producer),'contract_sha256':digest(a.contract),'reviewed_note_sha256':digest(a.note),'controls_stored_sha256':digest(a.controls),'actual_api_guard_rejections':len(controls['actual_producer_invalid_input_rejections']),'fresh_event_controls':len(controls['actual_source_event_rejection']),'fresh_source_event_controls':sum(c['fresh_own_source_event_certificate']for c in controls['actual_source_event_rejection']),'control_scope':controls['scope'],'replays':rows,'reviewer_record_guard_rejections':guards,'guard_scope':'adversarial corruption of stored records is rejected by this reviewer validator; this is not a claim that the producer loads external source caches','fresh_source_quadrature_replays':2}
    a.output.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'status':'pass','full_replays':2,'record_guard_rejections':len(guards),'output':str(a.output)}))
if __name__=='__main__':main()
