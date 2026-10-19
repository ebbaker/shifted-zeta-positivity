#!/usr/bin/env python3
"""Separate S05-T2 review of full records, exact ledgers and invalid inputs.

19 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Actual review model gpt-6.1-sol, effort ultra. Same-model internal review.
Run the full producer separately at 192/256 bits first, then pass its original
and fresh-replay directories here. No new quadratures or repository writes.
"""
import argparse
from collections import Counter
import copy
from fractions import Fraction as F
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import types
from flint import arb,ctx


def check(c,m):
    if not c: raise AssertionError(m)

def digest(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def canonical(v): return hashlib.sha256(json.dumps(v,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def numeric(v):
    if isinstance(v,dict):
        return {k:numeric(x) for k,x in v.items() if 'seconds' not in k and k!='path_at_execution'}
    if isinstance(v,list):return [numeric(x) for x in v]
    return v

def exact(d):
    m,e=int(d['mantissa']),int(d['exponent'])
    return F(m*2**e) if e>=0 else F(m,2**(-e))

def endpoints(row):
    mid,rad=exact(row['midpoint_dyadic']),exact(row['radius_upper_dyadic'])
    check(rad>=0,'negative serialized ball radius')
    return mid-rad,mid+rad

def load(path,name):
    spec=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m


def exact_ledgers(report):
    acquisitions=report['acquisitions']; checked=0
    coefficient_sets={method:data['coefficients'] for method,data in acquisitions.items()}
    for name,receipt in report['hybrid_receipts'].items():
        choices=receipt['alternatives'];selected=[]
        for j,row in enumerate(receipt['selection']):
            check(row['j']==j,'hybrid order')
            best=min(choices,key=lambda method:exact(acquisitions[method]['coefficients'][j]['quadrature_radius_upper_dyadic']))
            source=acquisitions[best]['coefficients'][j]
            check(row['method']==best,'hybrid did not use its declared exact radius minimum/tie rule')
            for key in ('midpoint_dyadic','quadrature_radius_upper_dyadic'):
                check(row[key]==source[key],'hybrid midpoint/radius tuple mix')
            selected.append(row)
        check(len(selected)==51,'hybrid incomplete')
        check(receipt['selection_counts']==dict(Counter(x['method'] for x in selected)),'hybrid selection counts')
        check(receipt['charged_all_selected_complete_setups_callbacks']==sum(acquisitions[x]['setup_callbacks'] for x in choices),'hybrid did not charge every acquisition')
        coefficient_sets[name]=selected
    for method,result in report['results'].items():
        radii=[exact(row['quadrature_radius_upper_dyadic']) for row in coefficient_sets[method]]
        for j,row in enumerate(result['whole_box_complete_error_ledger']):
            check(row['j']==j,'ledger derivative order')
            q_exact=sum((F(19,200)**k*radii[j+ell+2*k]/(math.factorial(ell)*math.factorial(k)) for ell in range(25) for k in range(13)),F(0))
            components={key:exact(value) for key,value in row['components_dyadic'].items()}
            check(components['quadrature']>=q_exact,'whole-box quadrature allowance underpays exact rational weighted sum')
            check(components['total']>=sum((components[key] for key in ('quadrature','taylor','mode','source')),F(0)),'complete sum underpayment')
            common=report['common_data']
            check(components['taylor']==exact(common['whole_box_taylor']),'changed common Taylor payment')
            check(components['mode']==exact(common['uniform_tails'][0][j]),'changed common mode payment')
            check(components['source']==exact(common['uniform_tails'][1][j]),'changed common source payment')
            il,ih=endpoints(row['polynomial_image_with_outward_rounding']);jl,jh=endpoints(row['complete_physical_jet_enclosure'])
            check(jl<=il-components['total'] and jh>=ih+components['total'],'physical output drops image rounding or added error')
            checked+=1
    return {'exact_rational_whole_box_ledgers':checked,'all_hybrid_whole_tuples_verified':True,'outward_polynomial_image_plus_complete_allowance_paid':True}


def mutation_guards(m,report,repo,producer,contract,work):
    rows=[]
    def reject(name,func,fragment=None):
        try:func()
        except (ArithmeticError,KeyError,ValueError) as e:
            if fragment is not None:check(fragment in str(e),(name,str(e)))
            rows.append({'case':name,'rejected':True,'message':str(e)})
        else:raise AssertionError(name+' unexpectedly passed')
    reject('precision128',lambda:m.validate_metadata(128,'gpt-6.1-sol','ultra'),'192/256')
    reject('empty_model',lambda:m.validate_metadata(192,' ','ultra'),'model metadata')
    reject('empty_effort',lambda:m.validate_metadata(192,'gpt-6.1-sol',''),'effort metadata')
    for label,pins in [('missing_expected_pin',{k:v for i,(k,v) in enumerate(report['source_sha256'].items()) if i}),('empty_expected_pins',{}),('stale_expected_pin',{**report['source_sha256'],next(iter(report['source_sha256'])):'0'*64})]:
        p=work/(label+'.json');p.write_text(json.dumps(pins));reject(label,lambda p=p:m.prepare_inputs(repo,p))
    reject('missing_contract',lambda:m.run(repo,192,'gpt-6.1-sol','ultra',work,work/'ABSENT_CONTRACT.md'),'contract required')
    p=work/'MODIFIED_CONTRACT.md';p.write_text(contract.read_text()+'\nMutation fixture only.\n')
    expected=work/'EXPECTED_REPORT.json';expected.write_text(json.dumps(report))
    reject('changed_contract',lambda:m.run(repo,192,'gpt-6.1-sol','ultra',work,p,expected),'contract hash changed')
    ctx.prec=192;d=arb.pi()/8-4*arb(1000).log()/1000
    coeff=report['acquisitions']['expanded']['coefficients'];common=report['common_data']
    ev=types.SimpleNamespace(bits=192,tlo=F(1,100),thi=F(1,5),tc=F(21,200),xlo=F(999),xhi=F(1001),xc=F(1000),U=arb(2),m=12,L=24,K=12,J=2,maxmid=50,maxrem=52,pi=arb.pi(),d=d,c=(4*d).cos(),sin4d=(4*d).sin(),norm=arb(1000)**(arb(9)/4),lams=[arb.pi()*n*n for n in range(1,12)],values=[m.undyadic(z['midpoint_dyadic']) for z in coeff],radii=[m.undyadic(z['quadrature_radius_upper_dyadic']) for z in coeff],majorant=m.undyadic(common['majorant']),full_H_moment=m.undyadic(common['full_H_moment']),whole_box_taylor=m.undyadic(common['whole_box_taylor']),uniform_tails=[[m.undyadic(x) for x in group]for group in common['uniform_tails']],high_order_tails=[[m.undyadic(x)for x in group]for group in common['high_order_tails']])
    m.validate_frozen(ev);m.validate_coefficients(ev,coeff);check(m.common_data(ev)==common,'valid common-data fixture fails')
    for attr,val in [('xhi',F(1002)),('d',d+arb(1)/100),('U',arb(3)),('m',11),('L',23),('K',11),('J',1),('maxmid',49),('maxrem',51),('norm',ev.norm*2),('lams',ev.lams[:-1])]:
        changed=copy.copy(ev);setattr(changed,attr,val);reject('changed_'+attr,lambda v=changed:m.validate_frozen(v))
    reject('missing_coefficient',lambda:m.validate_coefficients(ev,coeff[:-1]),'51 ordered')
    bad=copy.deepcopy(coeff);bad[2]['j']=3;reject('misordered_coefficient',lambda:m.validate_coefficients(ev,bad),'order changed')
    for label,v in [('negative_radius',arb(-1)),('nonfinite_radius',arb('nan'))]:
        changed=copy.copy(ev);changed.radii=list(ev.radii);changed.radii[0]=v;reject(label,lambda v=changed:m.validate_coefficients(v,coeff),'radius')
    changed=copy.copy(ev);changed.values=list(ev.values);changed.values[0]+=1;reject('midpoint_radius_tuple_mismatch',lambda:m.validate_coefficients(changed,coeff),'tuple differs')
    for attr in ('majorant','full_H_moment','whole_box_taylor'):
        changed=copy.copy(ev);setattr(changed,attr,getattr(ev,attr)*2);reject('changed_common_'+attr,lambda v=changed:m.check(m.common_data(v)==common,'common payment mutation rejected'))
    for attr in ('uniform_tails','high_order_tails'):
        for group in (0,1):
            changed=copy.copy(ev);v=[list(z)for z in getattr(ev,attr)];v[group][0]*=2;setattr(changed,attr,v);reject('changed_common_'+attr+'_'+str(group),lambda v=changed:m.check(m.common_data(v)==common,'common payment mutation rejected'))
        changed=copy.copy(ev);setattr(changed,attr,getattr(ev,attr)[:-1]);reject('missing_common_'+attr,lambda v=changed:m.check(m.common_data(v)==common,'common payment mutation rejected'))
    ledger=json.loads((repo/m.S01/'numerics/S01_COMPLETE_CONSUMER_20261019.json').read_text());cover=m.frozen_cover(ledger,192)
    reject('missing_cover_cell',lambda:m.validate_cover(cover[:-1]))
    bad=copy.deepcopy(cover);bad[0]['x'][0]='9991/10';reject('cover_endpoint_gap',lambda:m.validate_cover(bad))
    return rows


def main():
    p=argparse.ArgumentParser()
    for arg in ('repo','producer','comparison-contract','reports-dir','replay-dir','work-dir','output'):
        p.add_argument('--'+arg,type=Path,required=True)
    p.add_argument('--execution-model',required=True);p.add_argument('--execution-effort',required=True)
    a=p.parse_args();a.work_dir.mkdir(parents=True,exist_ok=True)
    check(a.execution_model.strip() and a.execution_effort.strip(),'review metadata required')
    m=load(a.producer,'s05_t2_independent_review_producer');reports=[];outcomes=[]
    for bits in (192,256):
        path=a.reports_dir/f'S05_T2_COMPLETE_SHIFTED_SOURCE_{bits}_20261019.json';fresh=a.replay_dir/path.name
        r=json.loads(path.read_text());rr=json.loads(fresh.read_text())
        check(r['script_sha256']==rr['script_sha256']==digest(a.producer),'producer fingerprint mismatch')
        check(r['comparison_contract_input']['sha256']==rr['comparison_contract_input']['sha256']==digest(a.comparison_contract),'contract fingerprint mismatch')
        check(numeric(r)==numeric(rr),'fresh numerical replay mismatch after excluding elapsed times and execution path')
        ctx.prec=bits;m.verify_pins(a.repo.resolve(),r['source_sha256'])
        proof=exact_ledgers(r)
        outcomes.append({'precision_bits':bits,'original_stored_sha256':digest(path),'fresh_stored_sha256':digest(fresh),'numerical_content_sha256':canonical(numeric(r)),'fresh_numeric_identity':True,**proof,'hybrid_selection_counts':{name:row['selection_counts'] for name,row in r['hybrid_receipts'].items()},'factoring_marginal_comparisons':r['strongest_same_caller_comparisons'],'physical_checks':{name:{'fixed_calls':row['fixed_40_cell_consumer']['calls'],'fixed_closed_coverage_verified':row['fixed_40_cell_consumer']['closed_coverage_verified'],'fixed_raw_minimum':row['fixed_40_cell_consumer']['minimum_signed_excess_norm2'],'adaptive_calls':row['adaptive_consumer']['summary']['total_consumer_calls'],'adaptive_reported_minimum':row['adaptive_consumer']['summary']['minimum_signed_excess_norm2']} for name,row in r['results'].items()}});reports.append(r)
    ctx.prec=256;m.validate_precision_replays(reports)
    guards=mutation_guards(m,reports[0],a.repo.resolve(),a.producer,a.comparison_contract,a.work_dir)
    result={'schema':'s05-t2-independent-review-v1','date':'2026-10-19','prepared_for':'Edward Baker','actual_model':a.execution_model,'actual_effort':a.execution_effort,'review_provenance':'Separate same-model internal review; no independent model or specialist review','review_script_sha256':digest(__file__),'producer_script_sha256':digest(a.producer),'comparison_contract_sha256':digest(a.comparison_contract),'source_sha256':reports[0]['source_sha256'],'identity_scope':'Matching hashes establish recorded data identity in this tested environment; inequalities are checked by exact rational or outward arithmetic, not by the hash.','replay_outcomes':outcomes,'precision_replay_real_and_imaginary_overlap':True,'guards':guards,'invalid_input_rejections':len(guards),'guard_scope':'Importable producer validation and common-payment equality gates; no new quadratures in this helper','status':'pass'}
    a.output.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'status':'pass','output':str(a.output),'guard_rejections':len(guards),'both_precisions_exact_numeric_replay':True,'review_script_sha256':result['review_script_sha256']}))

if __name__=='__main__':main()
