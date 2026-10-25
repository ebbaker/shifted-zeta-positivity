#!/usr/bin/env python3
"""HDA-17-AN03 positive cubic-Hermite source, explicit remainders, t64 pilot.
Prepared for Edward Baker with substantial LLM assistance, 2026-10-24,
gpt-6.1-sol (Codex), actual effort ultra. Floating diagnostic, not a
continuous observable/filter certificate. Requires NumPy and mpmath.
"""
import argparse,hashlib,json,math,os,platform,re,sys,time
from pathlib import Path
import numpy as np
import mpmath as mp
import hermite_source as hs
PI=math.pi
CATEGORIES=('interpolation','omitted_value_modes','omitted_derivative_modes','nodal_value_arithmetic_candidate','nodal_derivative_arithmetic_candidate','coefficient_construction_rounding')

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def lse(v):return float(np.logaddexp.reduce(np.asarray(v)))
def ideal_gauss_remainder(source,G,t=64.,Y=1.,zmax=math.sqrt(101)):
    """Absolute four-jet truncation bound for ideal positive Gauss rule.

    Source is cubic Bernstein with exact stored nonnegative coefficients.
    Taylor's exponential remainder plus degree2G-1 Gaussian exactness pays
    analytic truncation only; rounded source/rule/field arithmetic is unpaid.
    """
    a=source['nodes'][:-1];b=source['nodes'][1:];h=source['h'];c=(a+b)/2;d=h/2
    cap=np.max(source['coefficients'],axis=1);theta=(2*abs(t)*c+zmax)*d+abs(t)*d*d
    valid=cap>0;logs=[];vals=[];orders=[]
    for j in range(4):
        M=(2*G-1-j-3)//2;orders.append(M)
        terms=np.log(2*h[valid])+np.log(cap[valid])+j*np.log(b[valid])+t*c[valid]**2+Y*c[valid]+theta[valid]+(M+1)*np.log(theta[valid])-math.lgamma(M+2)
        z=lse(terms);logs.append(z/math.log(10));vals.append(math.exp(z))
    return dict(rule_nodes_per_cell=G,exponential_series_degree=orders,jet_bounds=vals,jet_bounds_log10=logs,t=t,Y=Y,zmax=zmax,scope='continuous source/filter buffer at stated t; ideal-Gauss truncation only',rounding='unpaid')

def fallback_ranges(source):
    ix=np.flatnonzero(source['fallback']);out=[]
    if not len(ix):return out
    lo=prev=int(ix[0]);u=source['nodes']
    for k in ix[1:]:
        k=int(k)
        if k!=prev+1:out.append(dict(first_cell=lo,last_cell=prev,u=[float(u[lo]),float(u[prev+1])])) ;lo=k
        prev=k
    out.append(dict(first_cell=lo,last_cell=prev,u=[float(u[lo]),float(u[prev+1])]))
    return out

def nodal_checks(source):
    mp.mp.dps=80;vmax=dmax=0.;worstvalue=worstslope=None
    for k,(u,v,d) in enumerate(zip(source['nodes'],source['values'],source['slopes'])):
        uu=mp.mpf(float(u));vv=mp.mpf(0);dd=mp.mpf(0)
        for n in range(1,5):
            A=mp.pi*n*n*mp.exp(4*uu);scale=mp.pi**(-mp.mpf(1)/4)*mp.mpf(n)**(-mp.mpf(1)/2)*mp.exp(-A)*A**(mp.mpf(5)/4)
            vv+=scale*(2*A-3);dd+=scale*(-15+30*A-8*A*A)
        vr=float(abs(mp.mpf(float(v))-vv)/mp.exp(float(source['log_value_candidate'][k])))
        dr=float(abs(mp.mpf(float(d))-dd)/mp.exp(float(source['log_slope_candidate'][k])))
        if vr>vmax:vmax=vr;worstvalue=[k,float(u)]
        if dr>dmax:dmax=dr;worstslope=[k,float(u)]
    return dict(value_candidate_max_ratio=vmax,slope_candidate_max_ratio=dmax,worst_value=worstvalue,worst_slope=worstslope,dps=80,status='finite checks of unproved nodal candidates')

def run(repo,output):
    started=time.perf_counter();num=repo/'papers/investigations-5/01_heat_density_asymptotics/numerics';sys.path.insert(0,str(num))
    import source_peak_diagnostic as local
    import source_accuracy_improvements as sa
    import weak_transfer_diagnostic as old
    import weak_coefficients as wk
    prior=json.loads((num/'SOURCE_PEAK_DIAGNOSTIC_20261024.json').read_text());cols=prior['row_columns']
    linear={ob['y']:{r['row']:r for r in [dict(zip(cols,v)) for v in ob['rows']]} for ob in prior['observations'] if ob['mesh']=='adaptive768'}
    nodes768,nodemeta=sa.adaptive_nodes(return_metadata=True)
    nodehash=hashlib.sha256(np.asarray(nodes768,dtype='<f8').tobytes()).hexdigest();assert nodehash==prior['adaptive_mesh']['nodes_sha256']
    meshes=[('uniform192',np.linspace(0,1.5,193)),('adaptive384',nodes768[::2]),('adaptive768',nodes768)]
    record=dict(request='HDA-17-AN03 r1',prepared_for='Edward Baker',model='gpt-6.1-sol',effort='ultra',date='2026-10-24 America/New_York',thread_id='01a170a3-5f6e-7aa2-9e33-bcae4835c782',status='floating source/observable diagnostic; arithmetic and continuous filter gates separate',environment=dict(python=sys.version,numpy=np.__version__,mpmath=mp.__version__,platform=platform.platform(),blas_threads=os.environ.get('OPENBLAS_NUM_THREADS')),source_cases=[],observations=[],cost_basis=dict(linear768_nodal_scalars=769,hermite384_nodal_scalars=770,linear768_unshared_cell_coefficients=1536,hermite384_stored_bernstein_coefficients=1536),adaptive768_nodes_sha256=nodehash,allocation=dict(source=.8,evaluator=.1,filter=.1))
    kernels={G:local.composite_rule(G,wk) for G in (8,12)}
    record['filter_geometry']={str(G):{k:local.jsonable(kr[k]) for k in ('edges','panels_per_direction','nodes_per_direction','field_nodes')} for G,kr in kernels.items()}
    allrows=[];work=0
    for mesh,nodes in meshes:
        source=hs.build_source(nodes);m=len(nodes)-1;case=dict(mesh=mesh,metadata=source['metadata'],nodes_sha256=hashlib.sha256(np.asarray(nodes,dtype='<f8').tobytes()).hexdigest(),coefficients_sha256=hashlib.sha256(np.asarray(source['coefficients'],dtype='<f8').tobytes()).hexdigest(),fallback_ranges=fallback_ranges(source),budgets=[])
        for weight in ('chord','gauss'):
            for G in (8,12):case['budgets'].append(hs.source_budget(source,order=G,weights=weight))
        best=case['budgets'][1];assert best['weight_method']=='chord' and best['weight_order']==12
        ds=np.array([r['total'] for r in best['rows']]);categories=np.array([[r[k] for r in best['rows']] for k in CATEGORIES]);tails=np.array([r['complete_tail_log10'] for r in best['rows']])
        eps={G:ideal_gauss_remainder(source,G) for G in (8,12)};case['evaluator_truncation']=eps;et=np.array(eps[12]['jet_bounds']);bars=ds+et
        case['nodal_candidate_checks']=nodal_checks(source);record['source_cases'].append(case)
        srules={G:hs.source_rule(source,G) for G in (8,12)}
        for y in (0.,.5):
            begin=time.perf_counter();values={}
            for G,kr in kernels.items():
                z=4-kr['x']+1j*(y-kr['y']);reg,_=old.regulator(64,z.real)
                g12=old.jets(64,z,srules[12]);work+=len(z)*m*12
                weak=old.values(g12,reg,kr);direct=local.direct_values(g12,reg,kr,old)
                co,variants,meta=local.local_coefficients(g12,bars,kr,reg,bars)
                values[G]=dict(weak=weak,direct=direct,co=co,variants=variants,meta=meta)
                if G==12:
                    g8=old.jets(64,z,srules[8]);work+=len(z)*m*8
                    weak8=old.values(g8,reg,kr);direct8=local.direct_values(g8,reg,kr,old)
            fine,coarse=values[12],values[8];rows=[]
            for n,co in fine['co'].items():
                if n=='DeltaQ':nn,al='DeltaQ',(0,0);ln=0
                else:nn,s=n.split(':');al=tuple(map(int,s.split(',')));ln=kernels[12]['L'][al]
                theta=old.target(nn,al,ln);sallow=float(co@ds);eallow=float(co@et)
                fc=float(abs(fine['weak'][n]-coarse['weak'][n]));pc=float(abs(co@bars-coarse['co'][n]@bars));wc=float(abs(fine['weak'][n]-weak8[n]))
                lt=[math.log10(c)+tails[j] for j,c in enumerate(co) if c>0]
                row=dict(row=n,target=theta,ABCD=co.tolist(),source_allowance=sallow,source_ratio=sallow/(.8*theta),source_categories=(categories@co).tolist(),source_tail_log10=float(np.logaddexp.reduce(np.array(lt)*math.log(10))/math.log(10)) if lt else None,evaluator_truncation_allowance=eallow,evaluator_truncation_ratio=eallow/(.1*theta),weak_evaluator_change=wc,weak_evaluator_ratio=wc/(.1*theta),weak_filter_change=fc,weak_filter_ratio=fc/(.1*theta),positive_filter_change=pc,positive_filter_ratio=pc/(.1*theta),weak_value12=old.cleanval(fine['weak'][n]),linear768_source_allowance=linear[y][n]['allowance'],linear768_weak_value12=linear[y][n]['weak_value12'])
                if n in fine['direct']:
                    de=float(abs(fine['direct'][n]-direct8[n]));df=float(abs(fine['direct'][n]-coarse['direct'][n]));dw=float(abs(fine['direct'][n]-fine['weak'][n]));row.update(direct_evaluator_change=de,direct_evaluator_ratio=de/(.1*theta),direct_filter_change=df,direct_filter_ratio=df/(.1*theta),direct_weak_disagreement=dw,direct_weak_ratio=dw/(.1*theta))
                rows.append(row);allrows.append(dict(mesh=mesh,t=64,x=4,y=y,**row))
            record['observations'].append(dict(mesh=mesh,cells=m,t=64,x=4,y=y,source_errors=ds.tolist(),evaluator_truncation_errors=et.tolist(),frozen_caps=bars.tolist(),rows=rows,metadata=fine['meta'],source_variants={kind:{n:float(co@ds) for n,co in variants.items()} for kind,variants in fine['variants'].items()},runtime_seconds=time.perf_counter()-begin))
            print('completed',mesh,y,'elapsed',round(time.perf_counter()-started,3),flush=True)
    metrics=('source_ratio','evaluator_truncation_ratio','weak_evaluator_ratio','direct_evaluator_ratio','weak_filter_ratio','direct_filter_ratio','positive_filter_ratio','direct_weak_ratio')
    record['maxima']={k:max((r for r in allrows if k in r),key=lambda r:r[k]) for k in metrics}
    record['mesh_maxima']={m:{k:max((r for r in allrows if r['mesh']==m and k in r),key=lambda r:r[k]) for k in metrics} for m,_ in meshes}
    packet=repo/'papers/investigations-5/01_heat_density_asymptotics/research-progress/handoffs/HDA-17-AN03.md'
    record['inputs']={n:dict(expected=h,actual=sha(repo/n),match=h==sha(repo/n)) for n,h in re.findall(r'\| `([^`]+)` \| `([0-9a-f]{64})` \|',packet.read_text())}
    record['script_hashes']={p.name:sha(p) for p in [Path(__file__),Path(hs.__file__),Path(__file__).with_name('check_hermite.py')]}
    record['controls']=json.loads(Path(__file__).with_name('HERMITE_CONTROLS.json').read_text())
    record['error_scope']=dict(positivity='exact algebraic for stored finite coefficients',interpolation='continuous remainder formula evaluated in floating arithmetic',source_ledger_arithmetic='unpaid',nodal_value_and_derivative='separate unproved candidate allowances, checked80digits',coefficient_construction='exact rational discrepancy to ideal polynomial of stored nodal floats; upper binary64 conversion',evaluator_truncation='explicit ideal-Gauss analytic bound at t64 over full source/filter buffer',evaluator_rounding='unpaid for both weak and direct routes',filter='all refinements diagnostics; continuous integration and arithmetic unpaid',continuous_D_time_acceptance=False,endpoint_join='unpaid')
    record['cost']=dict(source_node_field_point_interactions=work,coarse_filter_points=16384,fine_filter_points=36864,source_rules=[8,12],primary_source_rule=12)
    record['runtime_seconds']=time.perf_counter()-started;record['numerical_budget']=dict(cap_seconds=1800,main_run_seconds=record['runtime_seconds'],auxiliary_conservative_debit_seconds=10,total_debit_seconds=record['runtime_seconds']+10)
    columns=list(allrows[0]);optional=('direct_evaluator_change','direct_evaluator_ratio','direct_filter_change','direct_filter_ratio','direct_weak_disagreement','direct_weak_ratio')
    for k in optional:
        if k not in columns:columns.append(k)
    columns=[k for k in columns if k not in ('mesh','t','x','y')];record['row_columns']=columns;record['source_category_columns']=list(CATEGORIES)
    for ob in record['observations']:ob['rows']=[[r.get(k) for k in columns] for r in ob['rows']]
    output.write_text(json.dumps(local.jsonable(record),separators=(',',':'),allow_nan=False)+'\n');assert output.stat().st_size<1048576
    print('DONE',record['runtime_seconds'],output.stat().st_size,flush=True)
    print(json.dumps({m:{k:(r['row'],r['y'],r[k]) for k,r in table.items()} for m,table in record['mesh_maxima'].items()}),flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--repo',type=Path,required=True);p.add_argument('--output',type=Path,required=True);args=p.parse_args();run(args.repo,args.output)
