#!/usr/bin/env python3
"""AN03 r2: directional gradient caps on the same Hermite768 observations.
Prepared for Edward Baker with LLM assistance, 2026-10-24,
gpt-6.1-sol, actual effort ultra. Floating positive convolutions only.
The r1 numerical record is read and preserved, never overwritten.
"""
import argparse,hashlib,json,math,os,platform,re,sys,time
from pathlib import Path
import numpy as np

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def ind(n):return [(i,k-i) for k in range(n+1) for i in range(k+1)]

def cov_columns(g,bars,reg,k,directional=True):
    q=reg['q'];f=g[:,0];p=g[:,1];D=abs(f)**2+q
    m=np.maximum(abs(f)-bars[0],0);M=abs(f)+bars[0]
    v=np.clip(np.sqrt(q),m,M);a=v/(q+v*v);b=1/(q+m*m);P1=abs(p)+bars[1]
    dc=np.column_stack([2*P1*b,2*a,np.zeros(len(g)),np.zeros(len(g))])
    universal=2*P1*a
    if directional:
        gradx=2*(p*np.conj(f)/D).real;grady=-2*(p*np.conj(f)/D).imag
        err=dc@bars
        Gx=np.minimum(universal,abs(gradx)+err);Gy=np.minimum(universal,abs(grady)+err)
    else:Gx=Gy=universal
    # At t64 the x,y gradient-error columns coincide; aggregate Gx+Gy
    # only after retaining the two valid separate component caps.
    G=Gx+Gy;cv=lambda al,z:k['abs_weights'][al]@z
    rows={}
    for al in ind(2):
        cc=2*cv(al,G[:,None]*dc)
        for be in ind(sum(al)):
            if be[0]<=al[0] and be[1]<=al[1]:
                ga=(al[0]-be[0],al[1]-be[1]);comb=math.comb(al[0],be[0])*math.comb(al[1],be[1]);cc+=comb*(cv(be,dc)*cv(ga,G)+cv(be,G)*cv(ga,dc))
        rows[f'Q:{al[0]},{al[1]}']=cc
    dk=abs(k['signed_weights'][(2,0)]+k['signed_weights'][(0,2)]);dd=lambda z:dk@z
    rows['DeltaQ']=2*dd(G[:,None]*dc)+2*cv((0,0),dc)*dd(G)+2*cv((0,0),G)*dd(dc)+4*sum(cv(al,G)*cv(al,dc) for al in ((1,0),(0,1)))
    return rows,dict(directionally_reduced_fraction_x=float(np.mean(Gx<universal)),directionally_reduced_fraction_y=float(np.mean(Gy<universal)),cap_scope='common cap for both H and ideal-Gauss model within fixed bars; arithmetic/integration unpaid')

def run(repo,output):
    start=time.perf_counter();num=repo/'papers/investigations-5/01_heat_density_asymptotics/numerics';sys.path.insert(0,str(num))
    import hermite_source as hs
    import source_peak_diagnostic as local
    import source_accuracy_improvements as sa
    import weak_transfer_diagnostic as old
    import weak_coefficients as wk
    path=num/'POSITIVE_HERMITE_DIAGNOSTIC_20261024.json';r1=json.loads(path.read_text());cols=r1['row_columns']
    for n,h in r1['script_hashes'].items():assert sha(num/n)==h,n
    nodes=sa.adaptive_nodes();source=hs.build_source(nodes);case=next(c for c in r1['source_cases'] if c['mesh']=='adaptive768');assert hashlib.sha256(np.asarray(source['coefficients'],dtype='<f8').tobytes()).hexdigest()==case['coefficients_sha256']
    cats=r1['source_category_columns'];best=case['budgets'][1];category=np.array([[r[n] for r in best['rows']] for n in cats]);tails=[r['complete_tail_log10'] for r in best['rows']]
    srule=hs.source_rule(source,12);kernels={G:local.composite_rule(G,wk) for G in (8,12)};allrows=[];observations=[]
    for y in (0.,.5):
        ob=next(o for o in r1['observations'] if o['mesh']=='adaptive768' and o['y']==y)
        ds=np.array(ob['source_errors']);eps=np.array(ob['evaluator_truncation_errors']);bars=np.array(ob['frozen_caps']);computed={}
        inherited={r['row']:r for r in [dict(zip(cols,v)) for v in ob['rows']]}
        for G,k in kernels.items():
            z=4-k['x']+1j*(y-k['y']);reg,_=old.regulator(64,z.real);g=old.jets(64,z,srule)
            co,meta=cov_columns(g,bars,reg,k)
            if G==12:
                universal,_=cov_columns(g,bars,reg,k,False)
                for n,v in universal.items():assert np.allclose(v,inherited[n]['ABCD'],rtol=5e-13,atol=1e-18),(y,n,'r1 replay mismatch')
            computed[G]=(co,meta)
        fine,coarse=computed[12][0],computed[8][0];updated=[]
        for n,co in fine.items():
            row=dict(inherited[n]);theta=row['target'];oldallow=row['source_allowance'];row['ABCD']=co.tolist();row['r1_source_allowance']=oldallow;row['source_allowance']=float(co@ds);row['source_ratio']=float(co@ds)/(.8*theta);row['source_categories']=(category@co).tolist();row['evaluator_truncation_allowance']=float(co@eps);row['evaluator_truncation_ratio']=float(co@eps)/(.1*theta)
            vals=[math.log10(c)+tails[j] for j,c in enumerate(co) if c>0];row['source_tail_log10']=float(np.logaddexp.reduce(np.array(vals)*math.log(10))/math.log(10)) if vals else None
            row['positive_filter_change']=float(abs(co@bars-coarse[n]@bars));row['positive_filter_ratio']=row['positive_filter_change']/(.1*theta);updated.append(row);inherited[n]=row
        for row in inherited.values():allrows.append(dict(y=y,**row))
        observations.append(dict(mesh='adaptive768',t=64,x=4,y=y,updated_covariance_rows=updated,all_other_rows_inherited=True,metadata=computed[12][1]))
        print('completed directional',y,'elapsed',time.perf_counter()-start,flush=True)
    metrics=('source_ratio','evaluator_truncation_ratio','weak_evaluator_ratio','direct_evaluator_ratio','weak_filter_ratio','direct_filter_ratio','positive_filter_ratio','direct_weak_ratio')
    result=dict(request='HDA-17-AN03 r2',prepared_for='Edward Baker',model='gpt-6.1-sol',effort='ultra',date='2026-10-24 America/New_York',thread_id='01a170a3-5f6e-7aa2-9e33-bcae4835c782',status='sampled allowance comparison only; no continuous core or rounding/filter acceptance',inherited_r1_record=dict(file=path.name,sha256=sha(path)),source_and_observable_values_unchanged=True,observations=observations,maxima_over_all91_rows={k:max((r for r in allrows if r.get(k) is not None),key=lambda r:r[k]) for k in metrics},source_category_columns=cats,evidence_scope='two t64 observation centers; common directional gradient caps only; all transcendental/nodal/budget/evaluator rounding and continuous filter errors remain unpaid',runtime_seconds=time.perf_counter()-start,script_sha256=sha(__file__),environment=dict(python=sys.version,numpy=np.__version__,platform=platform.platform(),blas_threads=os.environ.get('OPENBLAS_NUM_THREADS')))
    result['total_AN03_conservative_numeric_debit_seconds']=r1['numerical_budget']['total_debit_seconds']+result['runtime_seconds']+5
    output.write_text(json.dumps(local.jsonable(result),separators=(',',':'),allow_nan=False)+'\n');assert output.stat().st_size<1048576
    print('DONE',result['runtime_seconds'],output.stat().st_size,{k:r[k] for k,r in result['maxima_over_all91_rows'].items()},flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--repo',type=Path,required=True);p.add_argument('--output',type=Path,required=True);args=p.parse_args();run(args.repo,args.output)
