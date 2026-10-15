#!/usr/bin/env python3
"""Exact endpoint, branch-cover, and preassigned half-time comparison audit.

Prepared for Edward Baker, 2026-10-14, with substantial LLM assistance.
Recorded parent model: gpt-6.1-sol, reasoning effort ultra.
Uses standard-library Fraction arithmetic; source quadrature/tail lemmas
remain trusted numerical inputs. No sampled sign decides a conclusion.
"""
import argparse
from collections import Counter
from fractions import Fraction as Q
from hashlib import sha256
import json
from pathlib import Path
import platform

import check_proportional_gaussian_source_filter_pilot as f
from audit_theta_centered_residual_record import negative_exponential_lower


def digest(path):
    return sha256(Path(path).read_bytes()).hexdigest()


class Audit:
    def __init__(self):
        self.counts=Counter()
    def check(self, group, message, condition):
        self.counts[group]+=1
        if not condition:
            raise ValueError(message)


def common_space_independent_times(current, earlier, eta, dt):
    """Range Ccurrent-.5Cearlier, retaining their common spatial variable.

    The two time displacements vary independently through the complete
    paid original slabs. Differences of constant-time spatial coefficients
    are formed before the shared eta is ranged. This is an overcover of
    the earlier-time triangle, not a nonlinear-delay Taylor substitution.
    """
    ep=[f.power(eta,m) for m in range(f.LX)]
    tp=[f.power(dt,p) for p in range(f.LT)]
    answer=f.ZERO
    for m in range(f.LX):
        coefficient=f.sub(current[0][m],f.scale(earlier[0][m],Q(1,2)))
        for p in range(1,f.LT):
            coefficient=f.add(coefficient,f.sub(f.mul(current[p][m],tp[p]),
                f.scale(f.mul(earlier[p][m],tp[p]),Q(1,2))))
        answer=f.add(answer,f.mul(coefficient,ep[m]))
    return answer


def analyze_record(path, source_dir, audit):
    check=audit.check
    r=json.loads(path.read_text())
    check('metadata','historical schema',r['schema']=='inv21_phase_centered_complete_source_pilot_v1')
    check('metadata','current run attribution',r['recorded_model']=='gpt-6.1-sol' and r['recorded_effort']=='ultra')
    check('metadata','transparent historical attribution',r['historical_driver_hardcoded_attribution']=={'recorded_model':'gpt-6-astra','recorded_effort':'ultra'})
    check('source_binding','historical driver hash',digest(source_dir/'certify_phase_centered_residual.py')==r['script_sha256'])
    check('source_binding','contour source hash',digest(source_dir/r['imported_source_name'])==r['imported_source_sha256'])
    check('source_binding','execution wrapper hash',digest(source_dir/r['execution_wrapper_name'])==r['execution_wrapper_sha256'])
    xl,xr=map(Q,r['domain']['x'])
    check('protocol','one of both fixed new bands',(xl,xr) in ((Q(104),Q(108)),(Q(108),Q(112))))
    check('protocol','full fixed time domain',r['domain']['t']==['0','1/2'])
    check('protocol','fixed old cone unchanged',Q(r['B_squared_claim'])==Q(1,9))
    check('protocol','fixed grid and precision',r['width']=='1' and r['time_slabs']==8 and r['runtime']['bits']==192)
    check('protocol','fixed complete-source numerical parameters',r['N']==8 and Q(r['U'])==Q(3,2) and r['space_order']==12 and r['time_order']==8)
    declared=r['execution_wrapper_protocol']
    check('protocol','protocol not fitted and declaration sequence transparent',
          declared['each_band_declared_before_its_first_evaluation'] is True
          and declared['joint_blind_predeclaration'] is False
          and len(declared['declaration_sequence'])==3
          and declared['filter_adjusted_after_observation'] is False)
    expected={((str(x),str(x+1)),(str(Q(k,16)),str(Q(k+1,16)))) for x in range(int(xl),int(xr)) for k in range(8)}
    keys=[(tuple(c['x']),tuple(c['t'])) for c in r['cells']]
    check('coverage','exact unique closed-cell Cartesian cover',len(keys)==r['cell_count']==len(set(keys))==32 and set(keys)==expected)
    lookup=dict(zip(keys,r['cells']))
    observations=Counter(); cone_failures=[]; physical_floor=Q(1,10**17)
    for i,row in enumerate(r['cells']):
        Z=list(map(f.iv,row['whole_cell_jets']));C=list(map(f.iv,row['whole_cell_C']))
        E=f.iv(row['energy_lower']);C2=f.iv(row['C2_upper']);mu=f.iv(row['Lambda']);slack=f.iv(row['residual_cone_margin'])
        check('shape',f'cell{i}: four jets, two residuals, order28 centers',len(Z)==4 and len(C)==2 and len(row['center_jets'])==29)
        check('shape',f'cell{i}: complete four-jet payments',len(row['jet_space_payments'])==len(row['jet_time_payments'])==4)
        distance=lambda v: v[0] if v[0]>0 else -v[1] if v[1]<0 else Q(0)
        check('norm',f'cell{i}: exact positive energy floor',0<E[0]==E[1]<=distance(Z[0])**2+distance(Z[1])**2)
        check('cone',f'cell{i}: residual square upper',C2[0]==C2[1] and C2[0]>=sum(max(abs(v[0]),abs(v[1]))**2 for v in C))
        exact_slack=E[0]/9-C2[0]
        check('cone',f'cell{i}: recorded cone slack encloses exact endpoint result',slack[0]<=exact_slack<=slack[1])
        expected_cone=bool(exact_slack>0 and mu[0]>=Q(2,5))
        check('cone',f'cell{i}: unchanged cone flag',row['residual_inequality_pass'] is expected_cone)
        if not expected_cone:
            cone_failures.append({'x':row['x'],'t':row['t'],'norm_ok':True})
        check('metadata',f'cell{i}: norm and centering flags',row['norm_positive'] is True and row['mu_at_least_two_fifths'] is True and mu[0]>=Q(2,5))
        xc=sum(map(Q,row['x']))/2
        certified_physical=E[0]*negative_exponential_lower(Q(22,7)*xc/4)
        check('norm',f'cell{i}: independent rational physical norm greater than1e-17',certified_physical>physical_floor**2)
        normalized=E[0]*negative_exponential_lower(Q(22,7)/8)
        check('norm',f'cell{i}: independent rational normalized energy greater than3000',normalized>3000)
        for j in (0,1):
            excluded=Z[j+1][0]>0 or Z[j+1][1]<0
            signed=f.add(f.mul(mu,f.power(Z[j],2)),f.mul(Z[j],C[j]))
            expected_class='stationarity_excluded' if excluded else 'stationary_sign_certified_by_centered_identity'
            check('stationarity',f'cell{i},j{j}: stationary implication',excluded or signed[0]>0)
            check('stationarity',f'cell{i},j{j}: recorded class',row['stationary_classification'][j]==expected_class)
            if not excluded:
                check('stationarity',f'cell{i},j{j}: recorded full-sign margin',f.iv(row['stationary_signed_form_enclosures'][j])[0]>0)
                check('branch_creation',f'cell{i},j{j}: next derivative cannot vanish',Z[j+2][0]>0 or Z[j+2][1]<0)
            observations[f'j{j}:{expected_class}']+=1
        for key in ('jet_space_payments','jet_time_payments','C_space_payments','C_time_payments'):
            check('payments',f'cell{i}: nonnegative {key}',all(f.iv(z)[0]>=0 for z in row[key]))
    check('metadata','cone failures preserved exactly',r['failed_cells']==cone_failures)
    check('metadata','historical incomplete cone status preserved',r['status']==('INCOMPLETE' if cone_failures else 'PASS'))
    check('metadata','separate signs and norm pass',r['stationary_sign_status']==r['norm_status']=='PASS' and r['all_stationary_observations_resolved'] is True)
    for key in ('complete_unscaled_index_payments','complete_unscaled_integration_payments','complete_unscaled_moment_majorants'):
        check('payments',f'complete positive {key}',len(r[key])==30 and all(f.iv(v)[0]>0 for v in r[key]))
    a=f.iv(r['a']);mu=f.add(f.power(a,2),(Q(1,16),Q(1,16)));eta=f.sym(Q(1,2));dt=f.sym(Q(1,32));branches=[]
    candidate_windows=[]
    # Identify every possible current branch from paid enclosures. The filter
    # and constants were fixed before this identification and never change.
    for k in range(8):
      tkey=(str(Q(k,16)),str(Q(k+1,16)))
      for j in (0,1):
        candidates=[lookup[((str(x),str(x+1)),tkey)] for x in range(int(xl),int(xr))
                    if lookup[((str(x),str(x+1)),tkey)]['stationary_classification'][j]!='stationarity_excluded']
        check('branch_cover',f'slab{k},j{j}: at most one candidate cell in this fixed band',len(candidates)<=1)
        if not candidates:
            continue
        row=candidates[0];Z=list(map(f.iv,row['whole_cell_jets']));zcur=list(map(f.iv,row['center_jets']))
        left=f.endpoint(row,zcur,j+1,-1);right=f.endpoint(row,zcur,j+1,1)
        increasing=Z[j+2][0]>0 and left[1]<0 and right[0]>0
        decreasing=Z[j+2][1]<0 and left[0]>0 and right[1]<0
        check('branch_cover',f'slab{k},j{j}: genuine unique regular current branch at every time',increasing or decreasing)
        candidate_windows.append({'j':j,'slab':k,'x':row['x'],'t':row['t']})
        prior=lookup[(tuple(row['x']),(str(Q(k//2,16)),str(Q(k//2+1,16))))]
        earlier=tuple(Q(t)/2 for t in row['t']);pc=sum(map(Q,prior['t']))/2;tc=sum(map(Q,row['t']))/2;offset=tc/2-pc
        check('affine_transport',f'slab{k}: exact earlier-center offset',offset==Q(-1 if k%2==0 else 1,64))
        displacement=f.add(f.scale(dt,Q(1,2)),(offset,offset))
        check('affine_transport',f'slab{k}: paid prior-cell containment',displacement==(earlier[0]-pc,earlier[1]-pc) and max(map(abs,displacement))<=Q(1,32))
        check('affine_transport',f'slab{k}: common physical normalization',prior['x']==row['x'] and prior['normalization']==row['normalization']=='e^(pi*xc/8), constant across cell')
        zprior=list(map(f.iv,prior['center_jets']));Ccur=f.cjets(zcur,a,mu);Cprior=f.cjets(zprior,a,mu)
        Tcur=f.tensor(Ccur,j);Tprior=f.tensor(Cprior,j,Q(1,2),offset)
        curpay=f.cpayment(row,j,a,mu);priorpay=f.cpayment(prior,j,a,mu)
        G=f.add(f.evaluate(Tprior,eta,dt),f.sym(priorpay))
        Rsource=f.add(f.evaluate(f.combine(Tcur,Tprior,1),eta,dt),f.sym(curpay+priorpay))
        Bsource=f.add(f.evaluate(f.combine(Tcur,Tprior,Q(1,2)),eta,dt),f.sym(curpay+priorpay/2))
        Cstat=f.sub(f.neg(Z[j+2]),f.mul(mu,Z[j]))
        R=f.intersect(Rsource,f.sub(Cstat,G));B=f.intersect(Bsource,f.sub(Cstat,f.scale(G,Q(1,2))))
        P=f.mul(Z[j],G);hR=f.mul(Z[j],R);absorption=f.mul(Z[j],B)
        check('delay_signs',f'slab{k},j{j}: prescribed P>0',P[0]>0)
        check('delay_signs',f'slab{k},j{j}: prescribed Q>0',absorption[0]>0)
        # Separate protocol declared before evaluation: overcover the entire
        # earlier-time triangle 0<=s<=t by paid prior slabs0,...,k. This keeps
        # all original source and parameter errors. It does not transport a
        # nonlinear delay or assume that an earlier point is stationary.
        prior_enclosures=[];correlated_absorption_factors=[]
        for earlier_k in range(k+1):
            paid=lookup[(tuple(row['x']),(str(Q(earlier_k,16)),str(Q(earlier_k+1,16))))]
            paid_center=f.cjets(list(map(f.iv,paid['center_jets'])),a,mu)
            paid_tensor=f.tensor(paid_center,j);paid_payment=f.cpayment(paid,j,a,mu)
            paid_C=f.add(f.evaluate(paid_tensor,eta,dt),f.sym(paid_payment))
            prior_enclosures.append(paid_C)
            correlated_source=f.add(common_space_independent_times(Tcur,paid_tensor,eta,dt),
                                    f.sym(curpay+paid_payment/2))
            correlated_absorption_factors.append(f.intersect(correlated_source,
                f.sub(Cstat,f.scale(paid_C,Q(1,2)))))
        past_hull=(min(v[0] for v in prior_enclosures),max(v[1] for v in prior_enclosures))
        universal_P=f.mul(Z[j],past_hull)
        universal_Q=f.mul(Z[j],f.sub(Cstat,f.scale(past_hull,Q(1,2))))
        universal_verdict=('CERTIFIED_PASS' if universal_P[0]>0 and universal_Q[0]>0
            else 'CERTIFIED_FAIL' if universal_P[1]<0 or universal_Q[1]<0 else 'UNDECIDED')
        correlated_factor_hull=(min(v[0] for v in correlated_absorption_factors),
                                max(v[1] for v in correlated_absorption_factors))
        correlated_Q=f.mul(Z[j],correlated_factor_hull)
        check('universal_delay_signs',f'slab{k},j{j}: all earlier times retained sign',universal_P[0]>0)
        check('universal_delay_signs',f'slab{k},j{j}: all earlier times absorption',correlated_Q[0]>0)
        branches.append({'j':j,'slab':k,'role':'development' if k%2==0 else 'holdout',
            'x':row['x'],'t':row['t'],'earlier_t':list(map(str,earlier)),
            'prior_original_slab':k//2,'prior_original_t':prior['t'],'affine_offset':str(offset),
            'normalization':row['normalization'],
            'current_left_stationary_derivative':f.encode(left),
            'current_right_stationary_derivative':f.encode(right),
            'current_monotonic_derivative':f.encode(Z[j+2]),'current_hj':f.encode(Z[j]),
            'stationary_full_C_fixed_mu':f.encode(Cstat),'whole_cell_G':f.encode(G),
            'whole_cell_R_source':f.encode(Rsource),'whole_cell_absorption_source':f.encode(Bsource),
            'stationary_R':f.encode(R),'stationary_absorption_factor':f.encode(B),
            'h_G':f.encode(P),'h_R':f.encode(hR),'h_R_plus_lambda_h_G':f.encode(absorption),
            'current_C_payment':str(curpay),'prior_C_payment':str(priorpay),
            'favorable_verdict':f.verdict(P),'residual_verdict':f.verdict(hR),
            'absorption_verdict':f.verdict(absorption),'fixed_K_zero_criterion_passed':True,
            'universal_earlier_time_test':{
                'earlier_time_overcover':['0',str(Q(k+1,16))],
                'prior_paid_slabs':list(range(k+1)),
                'complete_Cj_earlier_time_hull':f.encode(past_hull),
                'current_hj_times_earlier_Cj':f.encode(universal_P),
                'current_hj_times_Ccur_minus_half_earlier_Cj':f.encode(universal_Q),
                'favorable_verdict':f.verdict(universal_P),
                'absorption_verdict':f.verdict(universal_Q),
                'criterion_verdict':universal_verdict,
                'display_only':{'P':[float(z) for z in universal_P],
                                'Q':[float(z) for z in universal_Q]},
                'common_space_refinement':{
                    'independent_time_displacements':['-1/32','1/32'],
                    'common_spatial_displacement':['-1/2','1/2'],
                    'all_original_paid_remainders_retained':True,
                    'absorption_factor_hull':f.encode(correlated_factor_hull),
                    'h_j_times_absorption':f.encode(correlated_Q),
                    'criterion_verdict':'CERTIFIED_PASS',
                    'display_only':{'Q':[float(z) for z in correlated_Q]}}},
            'display_only':{name:[float(v[0]),float(v[1])] for name,v in
                            [('hG',P),('hR',hR),('absorption',absorption)]}})
    return {'input_record_name':path.name,'input_record_sha256':digest(path),
        'domain':r['domain'],'cell_count':len(r['cells']),
        'historical_uniform_cone_status':r['status'],'cone_failed_cell_count':len(cone_failures),
        'all_stationary_signs_certified':True,'norm_positive_everywhere':True,
        'stationary_classification_counts':dict(sorted(observations.items())),
        'all_possible_branches_covered':True,'branch_creation_excluded_in_candidate_cells':True,
        'closed_candidate_branch_cover':candidate_windows,'delay_row_count':len(branches),
        'delay_rows':branches,
        'universal_earlier_time_summary':dict(Counter(
            row['universal_earlier_time_test']['criterion_verdict'] for row in branches)),
        'universal_earlier_time_common_space_summary':dict(Counter(
            row['universal_earlier_time_test']['common_space_refinement']['criterion_verdict'] for row in branches)),
        'minimum_universal_product_lower_endpoints':{
            'P':str(min(Q(row['universal_earlier_time_test']['current_hj_times_earlier_Cj'][0]) for row in branches)),
            'Q':str(min(Q(row['universal_earlier_time_test']['common_space_refinement']['h_j_times_absorption'][0]) for row in branches))},
        'minimum_normalized_product_lower_endpoints':{
            key:str(min(Q(row[field][0]) for row in branches)) for key,field in
            [('P','h_G'),('Q','h_R_plus_lambda_h_G')]},
        'core_reported_physical_norm_lower':r['physical_norm_lower'],
        'core_reported_normalized_energy_lower':r['normalized_energy_lower'],
        'independently_audited_rational_norm_floor':'1/100000000000000000',
        'independently_audited_normalized_energy_floor':'3000',
        'a':f.encode(a),'fixed_delay_mu':f.encode(mu)}


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--record',type=Path,action='append',required=True)
    ap.add_argument('--source-dir',type=Path,default=Path(__file__).resolve().parent)
    ap.add_argument('--output',type=Path,required=True)
    args=ap.parse_args();audit=Audit()
    result={'schema':'inv21_fixed_cusp_band_extension_exact_audit_v1',
        'date':'2026-10-14','prepared_for':'Edward Baker','llm_assistance':'Substantial',
        'recorded_model':'gpt-6.1-sol','recorded_effort':'ultra',
        'python':platform.python_version(),'status':'FAIL',
        'audit_name':Path(__file__).name,'audit_sha256':digest(__file__),
        'source_bindings':{name:digest(args.source_dir/name) for name in
            ('certify_fixed_cusp_band_extension.py','certify_phase_centered_residual.py',
             'check_shifted_contour_payments.py','check_proportional_gaussian_source_filter_pilot.py',
             'audit_theta_centered_residual_record.py')},
        'arithmetic':'Exact fractions.Fraction endpoint operations; float fields are display only.',
        'delay_protocol':{'delta':'t/2','lambda':'1/2','a':'pi/16','b':'1/4','K0':0,'K1':0,
            'development_slabs':[0,2,4,6],'holdout_slabs':[1,3,5,7],
            'changed_after_observing_results':False},
        'additional_universal_earlier_time_protocol':{
            'declared_before_evaluation':True,
            'earlier_time':'any s in [0,t]',
            'enclosure':'hull of the complete paid fixed-centering Cj over prior original slabs0,...,k for current slabk',
            'lambda':'1/2','a':'pi/16','b':'1/4','K0':0,'K1':0,
            'changed_after_observing_results':False,
            'independent_verdict_from_half_time_test':True,
            'enclosure_refinement':
                'After coarse hull left8cases undecided, retain common spatial eta in Ccurrent-.5Cearlier, with independent time displacements and every original paid source remainder. This changes only enclosure arithmetic, not the prescribed filter or constants.'},
        'scope':'Only supplied finite closed rectangles and all their genuine current stationary branches. The original uniform1/9 cone failures remain failures of that enclosure.',
        'limitations':[
            'Complete-source quadrature and contour/index/integration-tail lemmas are trusted inputs; this is not formal verification of Arb or the analytic lemmas.',
            'The exact auditor recomputes endpoint signs and finite Taylor transport; it does not recompute source quadrature.',
            'Delayed fields are evaluated at t/2 at the current stationary spatial point. Earlier stationarity is never imposed.',
            'Closed-cell stationarity implications cover any possible branch creation; strict next-derivative signs and endpoint signs exclude creation in the actual candidate cells.',
            'No arbitrary-height, collision-cusp, or Riemann-Hypothesis conclusion is supplied.']}
    try:
        audit.check('source_binding','actual imported exact transport helper matches bound source',
            digest(Path(f.__file__))==digest(args.source_dir/'check_proportional_gaussian_source_filter_pilot.py'))
        # The imported function is decorated with functools.lru_cache;
        # inspect the underlying function's actual defining source.
        audit.check('source_binding','actual imported exponential helper matches bound source',
            digest(Path(negative_exponential_lower.__wrapped__.__code__.co_filename))==digest(args.source_dir/'audit_theta_centered_residual_record.py'))
        domains=[tuple(json.loads(p.read_text())['domain']['x']) for p in args.record]
        audit.check('coverage','no duplicated input band',len(set(domains))==len(domains))
        result['bands']=[analyze_record(path,args.source_dir,audit) for path in args.record]
        result['total_cells']=sum(v['cell_count'] for v in result['bands'])
        result['total_stationary_observations']=2*result['total_cells']
        result['delay_row_count']=sum(v['delay_row_count'] for v in result['bands'])
        result['status']='PASS'
    except Exception as exc:
        result['error']={'type':type(exc).__name__,'message':str(exc)}
    result['checks_by_group']=dict(sorted(audit.counts.items()))
    result['checks_total']=sum(audit.counts.values())
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in result if k not in ('bands','source_bindings','limitations')},indent=2))
    return 0 if result['status']=='PASS' else 1


if __name__=='__main__':
    raise SystemExit(main())
