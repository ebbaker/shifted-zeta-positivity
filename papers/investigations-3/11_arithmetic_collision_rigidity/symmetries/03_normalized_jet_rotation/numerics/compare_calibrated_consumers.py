#!/usr/bin/env python3
"""S03-T3 fixed-box calibrated first-jet, scalar and direct-source comparison.

Prepared for Edward Baker, 19 October 2026, with substantial LLM assistance.
Actual authoring model gpt-6.1-sol, reasoning effort ultra. Internal evidence.
Requires python-flint 0.9.0. Regenerable source setup stays external.
"""
from __future__ import annotations
import argparse, hashlib, importlib.util, json, platform, time
from fractions import Fraction as F
from pathlib import Path
import flint
from flint import arb, acb, ctx

INV=Path('papers/investigations-3/11_arithmetic_collision_rigidity')
LANE=INV/'symmetries/03_normalized_jet_rotation'
S02=INV/'symmetries/02_cutoff_reflection/numerics'
HH=INV/'numerics/high_height_consumer/high_height_consumer.py'

def A(v): return arb(v.numerator)/v.denominator if isinstance(v,F) else arb(v)
def check(ok,msg):
    if not ok: raise ArithmeticError(msg)
def out(v): return v.str(38,more=True)
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def box(a,b):
    a,b=A(a),A(b)
    return arb((a+b)/2,((b-a)/2).upper())
def poly(cs,x):
    value=cs[-1]
    for c in reversed(cs[:-1]): value=value*x+c
    return value
def load(p,name):
    s=importlib.util.spec_from_file_location(name,p)
    m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
def dyadic(row): return arb((int(row['mantissa']),int(row['exponent'])))
def canonical_setup(data):
    # Omit observed acquisition times/callbacks, retain all mathematical fields
    # including exact binary jets/tails, source pins and fixed parameters.
    def clean(value):
        if isinstance(value,dict):
            return {k:clean(v) for k,v in value.items()
                    if k not in ['seconds','callbacks','jet_seconds','jet_callbacks']}
        if isinstance(value,list): return [clean(v) for v in value]
        return value
    keys=['schema','kind','status','bits','actual_precision_bits','source_sha256',
          'source_pins','normalization','domain','frozen_parameters','predeclared',
          'source_contract','cache_contract','setup']
    value={k:clean(data[k]) for k in keys}
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':')).encode()).hexdigest()

def export_anchors(repo,setup_path,output,model,effort):
    old_path=repo/LANE/'numerics/S03_CORRELATED_RESIDUAL_192_20261018.json'
    old=json.loads(old_path.read_text());setup=json.loads(setup_path.read_text())
    check(old['script_sha256']==sha(repo/LANE/'numerics/check_correlated_residual.py'),
          'retained correlated producer pin')
    check(sha(setup_path)==old['source_pins']['complete_setup']['sha256'],
          'first anchor export requires the retained exact source setup; use saved export for later regenerated inputs')
    hh=load(repo/HH,'t3_export_hh');hh.validate_setup(setup,repo)
    inherited=old['source_pins']
    check(inherited['complete_setup_analytic_pins']==setup['source_pins'],
          'retained analytic setup pins')
    for key in ['complete_source_code','arithmetic_source_code','opening_S03_192_record']:
        pin=inherited[key];check(sha(repo/pin['path'])==pin['sha256'],'retained '+key)
    check(sha(repo/S02/'S02_CUTOFF_REFLECTION_192_20261018.json')==
          inherited['arithmetic_source_code']['retained_record_sha256'],'retained S02 original record')
    opening=json.loads((repo/inherited['opening_S03_192_record']['path']).read_text())
    check(opening['script_sha256']==sha(repo/LANE/'numerics/check_normalized_rotation.py')==
          inherited['opening_S03_192_record']['script_sha256'],'retained opening producer')
    check(old['closed_cover']['time_cells']==32 and old['closed_cover']['space_cells']==128,
          'retained cover')
    paths=[LANE/'numerics/check_correlated_residual.py',
           LANE/'numerics/S03_CORRELATED_RESIDUAL_192_20261018.json',
           LANE/'numerics/check_phase_residual_allowance.py',
           LANE/'numerics/S03_PHASE_ANALYTIC_ALLOWANCE_20261019.json',
           S02/'evaluate_complete_frozen_jets.py',S02/'check_cutoff_reflection.py',
           S02/'S02_MATCHED_CORRECTION_20261019.json',HH,
           S02/'S02_CUTOFF_REFLECTION_192_20261018.json',
           LANE/'numerics/check_normalized_rotation.py',
           LANE/'numerics/S03_ROTATION_192_20261018.json']
    phases=json.loads((repo/paths[3]).read_text())
    check(phases['script_sha256']==sha(repo/paths[2]),'phase allowance producer pin')
    for rel,pin in phases['source_sha256'].items(): check(sha(repo/rel)==pin,'phase source pin '+rel)
    nominal=old['calibrated_oscillator']['nominal_physical_anchor_time_coefficients']
    check(nominal['time_center']=='21/200' and nominal['anchor_x']=='999', 'anchor center')
    check(len(nominal['physical_delta_over_Gstar'])==13 and len(nominal['physical_delta_x_over_Gstar'])==13,
          '26 exact dyadic anchor coefficients')
    result={'schema':'s03-t3-anchor-export-v1','date':'2026-10-19','prepared_for':'Edward Baker',
      'actual_model':model,'actual_effort':effort,'llm_assistance':'substantial; same-model internal work',
      'source_sha256':{str(v):sha(repo/v) for v in paths},
      'source_setup':{'original_stored_sha256':sha(setup_path),
          'mathematical_setup_sha256':canonical_setup(setup),'precision_bits':192,
          'observational_fields_excluded':'setup and jet seconds/callback counts; all mathematical fields retained',
          'original_acquisition_seconds':setup['setup']['seconds'],
          'original_acquisition_callbacks':setup['setup']['callbacks'],
          'regeneration':'Run high_height_consumer.py at192 bits externally; the source and mathematical setup hashes must match. Timings may differ.'},
      'historical_residual_preparation':{'observed_consumer_seconds':old['seconds'],
          'source_setup_is_additional':True,'shared_model':old['shared_model'],
          'arithmetic_polydisk':old['arithmetic_polydisk'],
          'prefix_cover':old['closed_cover'],
          'scope':'Historical descriptive observation, not a matched benchmark. Calibration needs the source setup PLUS recombined mixed coefficients, polydisk majorant, residual prefix and anchor export.'},
      'domain':{'t':['1/100','1/5'],'x':[999,1001],'anchor':999,'cover':[32,128]},
      'nominal_physical_anchor_time_coefficients':nominal,
      'inherited_physical_error_ledger':old['physical_error_ledger'],
      'analytic_only_complete_increment_upper':phases['runs'][0]['allowance']['combined'],
      'historical_comparison':old['comparison'],
      'slabs':[{'t':v['t'],
         'nominal_anchor_uncertainty_upper':v['nominal_oscillator_anchor_uncertainty_upper'],
         'complete_correlated_increment_upper':v['correlated_signed_prefix_integral_upper'],
         'uncalibrated_residual_anchor_radius_upper':v['anchor_residual_jet_radius_upper'],
         'uncalibrated_residual_slab_radius_upper':v['full_box_residual_jet_radius_upper']}
          for v in old['slabs']]}
    for it,row in enumerate(result['slabs']):
        check(row['t']==[str(F(1,100)+F(19,100)*it/32),str(F(1,100)+F(19,100)*(it+1)/32)],'slab partition')
    output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'exported_anchor_coefficients':26,'output':str(output),
                      'source_math_sha256':result['source_setup']['mathematical_setup_sha256']}))

def paid_radius(nominal_lower,error):
    check(nominal_lower.is_finite() and error.is_finite() and error>=0,'invalid paid radius inputs')
    return (nominal_lower-error).lower()
def scalar_radius(anchor_lower,increment_upper,anchor_error,residual_increment):
    check(increment_upper>=0 and anchor_error>=0 and residual_increment>=0,'invalid scalar payments')
    return paid_radius((anchor_lower-increment_upper).lower(),(anchor_error+residual_increment).upper())
def propagate_radius(Wcell,Wmid,Wprimecell,halfwidth):
    check(halfwidth>=0,'negative cell halfwidth')
    return max(Wcell.abs_lower(),(Wmid.abs_lower()-halfwidth*Wprimecell.abs_upper()).lower())
def Wprime(jet,w,wp): return acb(jet[1],-jet[2]/w+jet[1]*wp/(w*w))
def Q_from_physical(v,data):
    b,bp,C=data['b'],data['b_x'],data['chi']
    return [C*v[0],C*(v[1]-b*v[0]),C*(v[2]-2*b*v[1]+(b*b-bp)*v[0])]
def jet_vector(jet,w): return acb(jet[0],-jet[1]/w)

def run(repo,contract,setup_path,bits):
    begin=time.monotonic();ctx.prec=bits
    check(contract['domain']=={'t':['1/100','1/5'],'x':[999,1001],
                              'anchor':999,'cover':[32,128]},'fixed B/anchor/cover contract')
    for rel,pin in contract['source_sha256'].items(): check(sha(repo/rel)==pin,'anchor dependency pin '+rel)
    old=json.loads((repo/LANE/'numerics/S03_CORRELATED_RESIDUAL_192_20261018.json').read_text())
    phase_record=json.loads((repo/LANE/'numerics/S03_PHASE_ANALYTIC_ALLOWANCE_20261019.json').read_text())
    check(contract['analytic_only_complete_increment_upper']==phase_record['runs'][0]['allowance']['combined'],
          'retained analytic-only increment altered')
    check(contract['nominal_physical_anchor_time_coefficients']==
          old['calibrated_oscillator']['nominal_physical_anchor_time_coefficients'],
          'exported nominal anchors altered')
    check(contract['inherited_physical_error_ledger']==old['physical_error_ledger'],
          'inherited complete error ledger altered')
    check(len(contract['slabs'])==32,'anchor slab count')
    for a,b in zip(contract['slabs'],old['slabs']):
        expected={'t':b['t'],'nominal_anchor_uncertainty_upper':b['nominal_oscillator_anchor_uncertainty_upper'],
          'complete_correlated_increment_upper':b['correlated_signed_prefix_integral_upper'],
          'uncalibrated_residual_anchor_radius_upper':b['anchor_residual_jet_radius_upper'],
          'uncalibrated_residual_slab_radius_upper':b['full_box_residual_jet_radius_upper']}
        check(a==expected,'retained slab allowance altered')
    setup=json.loads(setup_path.read_text());hh=load(repo/HH,'t3_hh_'+str(bits));hh.validate_setup(setup,repo)
    check(canonical_setup(setup)==contract['source_setup']['mathematical_setup_sha256'],
          'source mathematical setup mismatch; rebuild exact declared source data or re-prove changed calibration')
    source=hh.load_setup(setup);ctx.prec=bits
    module=load(repo/S02/'evaluate_complete_frozen_jets.py','t3_full_'+str(bits))
    e=module.ClosedJetEvaluator(repo,bits);ctx.prec=bits
    anchor=contract['nominal_physical_anchor_time_coefficients']
    p0=[dyadic(v) for v in anchor['physical_delta_over_Gstar']]
    p1=[dyadic(v) for v in anchor['physical_delta_x_over_Gstar']]
    analytic_increment=A(contract['analytic_only_complete_increment_upper']).upper()
    ii=acb(0,1);tc=A(F(21,200));slabs=[]
    counts={'full_jet_evaluations':0,'source_cell_evaluations':0,'source_midpoint_evaluations':0,
            'stable_primitive_evaluations':0,'complete_source_quadratures_this_consumer':0,'cells':0}
    def full(x,t,recenter=None):
        counts['full_jet_evaluations']+=1
        return e.jets(x,t,recenter)
    def cal_W(data,theta_a,Wa): return (ii*(data['theta']-theta_a)).exp()*Wa
    def zminus2(x,t,data):
        # Same complete coherent full formula as the inherited stable primitive.
        counts['stable_primitive_evaluations']+=1
        s=(1-ii*acb(x))/2;P=acb(1);Px=acb(0);o=e.old
        for n in range(2,9):
            ell=A(n).log();pn=(t*ell*ell/4-(s+t*o.alpha(s)/2)*ell).exp()
            lam=ii*ell/2*(1+t*o.alphap(s)/2);P+=pn;Px+=lam*pn
        from flint import acb_series
        z=acb_series([acb(x),acb(1)],3)
        C=-o.W_real(z,t)*o.J(z,t,8)[0]
        phase=(-ii*data['theta']).exp();w=data['omega']
        return 2*(P-1)-ii/w*(Px+phase**2*Px.conjugate())-phase*(C[0]-ii*C[1]/w)
    for it in range(32):
        ta=F(1,100)+F(19,100)*it/32;tb=F(1,100)+F(19,100)*(it+1)/32
        t=box(ta,tb);data_a=full(A(999),t);w_a=data_a['omega'];th_a=data_a['theta']
        a0=data_a['chi']*poly(p0,t-tc)
        a1=data_a['chi']*(poly(p1,t-tc)-data_a['b']*poly(p0,t-tc))
        Wga=acb(a0,-a1/w_a);Wfa=jet_vector(data_a['full'],w_a)
        Za=zminus2(A(999),t,data_a)
        row=contract['slabs'][it]
        epsa=A(row['nominal_anchor_uncertainty_upper']).upper()
        B=A(row['complete_correlated_increment_upper']).upper();ecal=(epsa+B).upper()
        er_a=A(row['uncalibrated_residual_anchor_radius_upper']).upper()
        er_slab=A(row['uncalibrated_residual_slab_radius_upper']).upper()
        ea_an=(e.eta['full']*max(A(1),(2/w_a.abs_lower()).upper())).upper()
        minima={k:A(100) for k in ['analytic_direct','calibrated_direct','source_direct_raw',
             'source_direct_propagated','source_direct_best','uncalibrated_source_direct']}
        locations={};maxI=A(0);source_error=A(0);max_physical_matrix=A(0)
        for ix in range(128):
            xa=F(999)+F(2)*ix/128;xb=F(999)+F(2)*(ix+1)/128;xm=(xa+xb)/2
            x=box(xa,xb);half=A((xb-xa)/2)
            d=full(x,t,xm);m=full(A(xm),t)
            w,wp=d['omega'],d['omega_x'];wm=m['omega']
            Wf=jet_vector(d['full'],w);Wfm=jet_vector(m['full'],wm)
            Wg=cal_W(d,th_a,Wga);Wgm=cal_W(m,th_a,Wga)
            Wc=Wf+Wg;Wcm=Wfm+Wgm
            Pf=Wprime(d['full'],w,wp)
            Pc=Pf+ii*w*Wg
            rf=propagate_radius(Wf,Wfm,Pf,half)
            rc=propagate_radius(Wc,Wcm,Pc,half)
            Rf=d['full'][0]+d['full'][2]/(w*w)-wp*d['full'][1]/(w**3)
            # Retain the established generic derivative bound as well as the
            # directly differentiated vector: either interval evaluation may win.
            lf=(w.abs_upper()*(Wf.abs_upper()+Rf.abs_upper())).upper()
            lc=(w.abs_upper()*(Wc.abs_upper()+Rf.abs_upper())).upper()
            rf=max(rf,(Wfm.abs_lower()-half*lf).lower())
            rc=max(rc,(Wcm.abs_lower()-half*lc).lower())
            ean=(e.eta['full']*max(A(1),(2/w.abs_lower()).upper())).upper()
            raw,budgets=source.enclose(ta,tb,xa,xb);counts['source_cell_evaluations']+=1
            mid,_=source.enclose(ta,tb,xm,xm);counts['source_midpoint_evaluations']+=1
            q=Q_from_physical(raw,d);qm=Q_from_physical(mid,m)
            Ws=jet_vector(q,w);Wsm=jet_vector(qm,wm);Ps=Wprime(q,w,wp)
            rsraw=Ws.abs_lower();rsprop=(Wsm.abs_lower()-half*Ps.abs_upper()).lower()
            Rs=q[0]+q[2]/(w*w)-wp*q[1]/(w**3)
            ls=(w.abs_upper()*(Ws.abs_upper()+Rs.abs_upper())).upper()
            rsprop=max(rsprop,(Wsm.abs_lower()-half*ls).lower())
            rs=max(rsraw,rsprop)
            # Source enclose() already includes every source error in raw/mid.
            e0=d['chi'].abs_upper()*budgets[0]['total']
            e1=d['chi'].abs_upper()*(budgets[1]['total']+d['b'].abs_upper()*budgets[0]['total'])
            source_error=max(source_error,(e0*e0+(e1/w.abs_lower())**2).sqrt().upper())
            values={'analytic_direct':paid_radius(rf,ean),
               'calibrated_direct':paid_radius(rc,ecal),
               'source_direct_raw':rsraw,'source_direct_propagated':rsprop,'source_direct_best':rs,
               'uncalibrated_source_direct':paid_radius(rf,er_slab)}
            for key,val in values.items():
                if val<minima[key]: minima[key]=val;locations[key]=[str(xa),str(xb)]
            # Preserve the complete signed primitive; Ig=0 for calibration.
            zz=zminus2(x,t,d);zzm=zminus2(A(xm),t,m)
            Iz=min((zz-Za).abs_upper(),((zzm-Za).abs_upper()+half*abs(w*Rf).upper()).upper())
            maxI=max(maxI,Iz)
            matrix=(1+d['b']*d['b']+w*w).sqrt().upper()
            max_physical_matrix=max(max_physical_matrix,matrix)
            counts['cells']+=1
        cal_anchor=(Wfa+Wga).abs_lower();f_anchor=Wfa.abs_lower()
        scalar={'analytic_only':scalar_radius(f_anchor,maxI,ea_an,analytic_increment),
          'source_uncalibrated':scalar_radius(f_anchor,maxI,er_a,B),
          'source_calibrated':scalar_radius(cal_anchor,maxI,epsa,B)}
        slabs.append({'t_index':it,'t':[str(ta),str(tb)],
          'direct_radii':{k:out(v) for k,v in minima.items()},'minimum_locations':locations,
          'scalar_radii':{k:out(v) for k,v in scalar.items()},
          'calibrated_anchor_nominal_radius_lower':out(cal_anchor),
          'full_approximation_anchor_nominal_radius_lower':out(f_anchor),
          'complete_approximation_increment_upper':out(maxI),
          'calibration_error_ledger':{'anchor_uncertainty_upper':out(epsa),'correlated_increment_upper':out(B),
             'complete_phase_jet_error_upper':out(ecal),'physical_firstjet_error_divided_by_A_upper':out(max_physical_matrix*ecal)},
          'source_complete_phase_error_diagnostic_upper':out(source_error),
          'analytic_anchor_error_upper':out(ea_an)})
    direct={k:out(min(A(row['direct_radii'][k]).lower() for row in slabs)) for k in slabs[0]['direct_radii']}
    scalar={k:out(min(A(row['scalar_radii'][k]).lower() for row in slabs)) for k in slabs[0]['scalar_radii']}
    # Classification compares reported uniform certificates, not exact infima.
    return {'bits':bits,'same_source_setup_precision_bits':setup['bits'],
       'direct_complete_phase_radius_lower':direct,'scalar_complete_phase_radius_lower':scalar,
       'maximum_calibrated_phase_jet_error_upper':out(max(A(v['calibration_error_ledger']['complete_phase_jet_error_upper']).upper() for v in slabs)),
       'maximum_source_phase_error_diagnostic_upper':out(max(A(v['source_complete_phase_error_diagnostic_upper']).upper() for v in slabs)),
       'work':counts,'slabs':slabs,'consumer_seconds':time.monotonic()-begin}

def main():
    p=argparse.ArgumentParser();p.add_argument('--repo',type=Path,required=True)
    p.add_argument('--setup',type=Path,required=True);p.add_argument('--output',type=Path,required=True)
    p.add_argument('--anchors',type=Path);p.add_argument('--export-anchors',action='store_true')
    p.add_argument('--bits',type=int,nargs='+',default=[192,256])
    p.add_argument('--execution-model',required=True);p.add_argument('--execution-effort',required=True)
    args=p.parse_args();repo=args.repo.resolve()
    if args.export_anchors:
        export_anchors(repo,args.setup,args.output,args.execution_model,args.execution_effort);return
    check(args.anchors is not None,'supply the retained --anchors export')
    contract=json.loads(args.anchors.read_text())
    check(contract['schema']=='s03-t3-anchor-export-v1','anchor schema')
    runs=[run(repo,contract,args.setup,bits) for bits in args.bits]
    result={'schema':'s03-t3-calibrated-consumers-v1','date':'2026-10-19','prepared_for':'Edward Baker',
      'actual_model':args.execution_model,'actual_effort':args.execution_effort,
      'llm_assistance':'substantial; same-model research and separate internal review',
      'python':platform.python_version(),'python_flint':flint.__version__,
      'script_sha256':sha(__file__),'anchor_export_sha256':sha(args.anchors),
      'source_setup_stored_sha256':sha(args.setup),
      'source_setup_mathematical_sha256':contract['source_setup']['mathematical_setup_sha256'],
      'source_sha256':contract['source_sha256'],'domain':contract['domain'],
      'primary_metric':'Complete paid phase-scaled first-jet radius, matched closed cover and source data',
      'source_acquisition':contract['source_setup'],
      'historical_residual_preparation':contract['historical_residual_preparation'],
      'cost_scope':'Descriptive work/times only; source setup acquired once for all source-informed routes; historical residual majorant/coefficient/prefix setup and anchor construction required for calibration. No matched-cost claim.',
      'scope':'Real-only first jets on B. No calibrated second-jet or complex-disk residual bound, new coverage or Newman bound.',
      'runs':runs}
    text=json.dumps(result,indent=2)+'\n';check(len(text.encode())<1048576,'small-record size policy')
    args.output.write_text(text)
    print(json.dumps({'output':str(args.output),'runs':[{'bits':r['bits'],
        'direct':r['direct_complete_phase_radius_lower'],'scalar':r['scalar_complete_phase_radius_lower']} for r in runs]}))

if __name__=='__main__':main()
