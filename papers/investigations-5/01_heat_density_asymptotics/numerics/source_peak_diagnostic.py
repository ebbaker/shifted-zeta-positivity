#!/usr/bin/env python3
"""AN02 bounded t64 source/filter diagnostic. No continuous certificate.
Prepared for Edward Baker with LLM assistance, 2026-10-24,
gpt-6.1-sol (Codex), actual effort ultra. Requires NumPy and mpmath.
Imports frozen AN01 code from --repo; no prior records are overwritten.
"""
import argparse, hashlib, json, math, os, platform, re, sys, time
from pathlib import Path
import numpy as np
from numpy.polynomial.legendre import leggauss
from numpy.polynomial import polynomial as pol
import mpmath as mp
import source_accuracy_improvements as sa
PI=math.pi

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def ind(n):return [(i,k-i) for k in range(n+1) for i in range(k+1)]
def name(n,a):return f'{n}:{a[0]},{a[1]}'
def jsonable(z):
    if isinstance(z,np.ndarray):return [jsonable(x) for x in z]
    if isinstance(z,(np.integer,np.floating)):return z.item()
    if isinstance(z,complex):return [z.real,z.imag]
    if isinstance(z,dict):return {k:jsonable(v) for k,v in z.items()}
    if isinstance(z,(list,tuple)):return [jsonable(x) for x in z]
    return z

def source_rule(nodes,order):
    v,w=leggauss(order);a=nodes[:-1];hh=np.diff(nodes);f=sa.phi(nodes)
    u=(a[:,None]+hh[:,None]*(v+1)/2).ravel()
    coeff=(f[:-1,None]*(1-v)/2+f[1:,None]*(1+v)/2).ravel()
    return u,(hh[:,None]*np.tile(w/2,(len(a),1))).ravel()*coeff

def composite_rule(order,wk):
    # Fixed geometry selected from kernel alone: all separable-derivative kinks
    # through order4 plus quarter points. No field-root/pilot search.
    edges=np.unique(np.concatenate([np.linspace(-1,1,9)]+[np.array(wk.kernel_roots(j)) for j in range(1,5)]))
    v,w=leggauss(order);nodes=[];weights=[]
    for a,b in zip(edges[:-1],edges[1:]):nodes.extend((a+b)/2+(b-a)*v/2);weights.extend((b-a)*w/2)
    v=np.array(nodes);w=np.array(weights);xx,yy=np.meshgrid(v,v,indexing='ij');ww=np.outer(w,w)
    pd=[pol.polyval(v,pol.polyder(wk.KPOLY,j)) for j in range(5)]
    kw={};L={}
    for i,j in ind(4):
        kw[(i,j)]=(ww*np.outer(pd[i]/2**i,pd[j]/.5**j)).ravel()
        L[(i,j)]=wk.kernel_l1_1d(i,2)*wk.kernel_l1_1d(j,.5)
    return dict(x=(2*xx).ravel(),y=(.5*yy).ravel(),signed_weights=kw,abs_weights={a:abs(v) for a,v in kw.items()},L=L,edges=edges,panels_per_direction=len(edges)-1,gauss_order_per_panel=order,nodes_per_direction=len(v),field_nodes=len(xx.ravel()))

def local_coefficients(g,bars,k,reg,full_errors):
    """Four positive source-jet columns with all nonlinear caps frozen.

    Source signed/product choice is fixed pointwise from the full error
    vector; each chosen coefficient map bounds every direction under caps.
    Physical regulator coefficients stay at source/filter integration points.
    """
    if any(np.any(np.asarray(reg[z])!=0) for z in ('rx','rxx','rtx','rtxx')):
        raise ValueError('Complete numerical local table is pre-switch only; adaptive source formulas are separate analytical inputs')
    q=reg['q'];rt=abs(reg['rt']);rx=abs(reg['rx']);e=np.sqrt(q);P=abs(g)+np.asarray(bars)
    m=np.maximum(abs(g[:,0])-bars[0],0);M=abs(g[:,0])+bars[0]
    clamp=lambda v:np.clip(v,m,M)
    va=clamp(e/math.sqrt(5));vb=clamp(e);vw=clamp(e/math.sqrt(3))
    A=q/(PI*(q+m*m)**2);A1=4*q*va/(PI*(q+va*va)**3)
    a=vb/(q+vb*vb);b=1/(q+m*m);w1=2*q*vw/(q+vw*vw)**2
    def vec(c0=0,c1=0,c2=0,c3=0):return np.column_stack([np.broadcast_to(z,(len(g),)) for z in (c0,c1,c2,c3)])
    R=vec(A1*P[:,1]**2,2*A*P[:,1])
    J=vec(A1*P[:,1]*P[:,2],A*P[:,2],A*P[:,1])
    E13=vec(A1*P[:,1]*P[:,3],A*P[:,3],0,A*P[:,1])
    W=vec(w1);rho=A*P[:,1]**2;jstar=A*P[:,1]*P[:,2]
    pstar=np.maximum(abs((m*m-q)/(m*m+q)),abs((M*M-q)/(M*M+q)))
    sourceold=rt[:,None]*(R+2*rho[:,None]*W)
    prod=pstar[:,None]*(rt[:,None]*R+rx[:,None]*J)+2*(rt*rho+rx*jstar)[:,None]*W
    As=lambda v:q*(v*v-q)/(PI*(q+v*v)**3)
    As1=lambda v:4*q*v*(2*q-v*v)/(PI*(q+v*v)**4)
    astar=np.maximum.reduce([abs(As(m)),abs(As(M)),abs(As(clamp(np.sqrt(2*q))))])
    crit=[np.sqrt(q*(17+sgn*math.sqrt(249))/10) for sgn in (-1,1)]
    as1star=np.maximum.reduce([abs(As1(m)),abs(As1(M))]+[abs(As1(clamp(v))) for v in crit])
    radial=vec(as1star*(rt*P[:,1]**2+rx*P[:,1]*P[:,2]),astar*(2*rt*P[:,1]+rx*P[:,2]),astar*rx*P[:,1])
    choose=(radial@full_errors<=prod@full_errors);src=np.where(choose[:,None],radial,prod)
    # Pointwise rho_t is unchanged by spatial q dependence at fixed x.
    Rt=2*E13+sourceold+4*((P[:,2]*a)[:,None]*R+rho[:,None]*vec(P[:,2]*b,0,a))
    Ut=2*vec(P[:,2]*b,0,a)+rt[:,None]*W
    Wt=rt[:,None]*W+2*vec(P[:,2]*b+P[:,2]*a*w1,0,a)
    d=vec(2*P[:,1]*b,2*a);G=2*P[:,1]*a
    cv=lambda al,f:k['abs_weights'][al]@f
    out={}
    env=dict(R=R,J=J,Rt=Rt,U=vec(2*a),Ut=Ut,W=W,Wt=Wt,B=rt[:,None]*W,source=src,C=vec(),Ct=vec())
    for n,v in env.items():
        for al in ind(4 if n in ('U','W') else 2):out[name(n,al)]=cv(al,v)
    for al in ind(2):
        EE=2*cv(al,G[:,None]*d)
        for be in ind(sum(al)):
            if be[0]<=al[0] and be[1]<=al[1]:
                ga=(al[0]-be[0],al[1]-be[1]);comb=math.comb(al[0],be[0])*math.comb(al[1],be[1])
                EE+=comb*(cv(be,d)*cv(ga,G)+cv(be,G)*cv(ga,d))
        out[name('Q',al)]=2*EE
    dk=abs(k['signed_weights'][(2,0)]+k['signed_weights'][(0,2)])
    cvd=lambda f:dk@f;zero=(0,0)
    out['DeltaQ']=2*(2*cvd(G[:,None]*d)+2*cv(zero,d)*cvd(G)+2*cv(zero,G)*cvd(d)+4*sum(cv(al,G)*cv(al,d) for al in [(1,0),(0,1)]))
    variants={n:{name('source',al):cv(al,v) for al in ind(2)} for n,v in [('old_product',sourceold),('product',prod),('signed',radial)]}
    return out,variants,dict(radial_selected_node_fraction=float(np.mean(choose)),minimum_field_over_regulator=float(np.min(abs(g[:,0])/e)))

def direct_values(g,reg,k,old):
    q=reg['q'];rt=reg['rt'];rx=reg['rx'];f,p,v,h=g.T;D=abs(f)**2+q;w=q/D;A=q/(PI*D*D)
    rho=A*abs(p)**2;j=A*v*np.conj(p)
    rhot=-2*A*(h*np.conj(p)).real+rt*(1-2*w)*rho+4*rho*(v*np.conj(f)/D).real
    source=(1-2*w)*(rt*rho+rx*j.real)
    sx=2*(p*np.conj(f)/D).real+rx*w;sy=-2*(p*np.conj(f)/D).imag
    cv=lambda al,x:np.sum(k['signed_weights'][al]*x)
    out={}
    for n,u in [('R',rho),('J',j),('Rt',rhot),('source',source)]:
        for al in ind(2):out[name(n,al)]=cv(al,u)
    # Actual covariance is formed after global primitive integrals.
    out['Q:0,0']=cv((0,0),sx*sx-sy*sy)-cv((0,0),sx)**2+cv((0,0),sy)**2
    dk=k['signed_weights'][(2,0)]+k['signed_weights'][(0,2)];val=np.sum(dk*(sx*sx-sy*sy))
    for u,sgn in [(sx,1),(sy,-1)]:val-=sgn*(2*cv((0,0),u)*np.sum(dk*u)+2*cv((1,0),u)**2+2*cv((0,1),u)**2)
    out['DeltaQ']=val
    return out

def run(repo,output):
    started=time.perf_counter();num=repo/'papers/investigations-5/01_heat_density_asymptotics/numerics';sys.path.insert(0,str(num))
    import weak_transfer_diagnostic as old
    import weak_coefficients as wk
    record=dict(request='HDA-17-AN02 r1',status='floating diagnostic; no continuous or rounding acceptance',prepared_for='Edward Baker',model='gpt-6.1-sol',effort='ultra',date='2026-10-24 America/New_York',thread_id='01a170a3-5f6e-7aa2-9e33-bcae4835c782',environment=dict(python=sys.version,numpy=np.__version__,mpmath=mp.__version__,platform=platform.platform(),blas_threads=os.environ.get('OPENBLAS_NUM_THREADS')),source_tables=[],observations=[],allocation=dict(source=.8,evaluator=.1,filter=.1))
    # Declare the switch-time gate before field execution. No t96 run unless
    # every t64 row source ratio<=1 and all integration indicators<=1.
    record['optional_t96_gate']='all t64 source/80% target<=1 and actual+positive filter indicators/10% target<=1; otherwise do not execute'
    for m in (192,384,768):
        for cap,weight in [('lc5','lc4'),('lc5','gauss'),('midpoint','chord'),('bernstein','chord'),('best','chord')]:
            for level in (8,12):record['source_tables'].append(sa.source_budget(m,cap=cap,weights=weight,order=level))
    anodes,ameta=sa.adaptive_nodes(return_metadata=True);record['adaptive_mesh']=ameta;record['adaptive_mesh']['nodes_sha256']=hashlib.sha256(np.asarray(anodes,dtype='<f8').tobytes()).hexdigest()
    abudget=sa.source_budget(anodes,cap='best',weights='chord',order=12);record['source_tables'].append(dict(mesh='adaptive768',**abudget))
    meshes=[('uniform192',np.linspace(0,1.5,193)),('uniform768',np.linspace(0,1.5,769)),('adaptive768',anodes)]
    kernels={8:composite_rule(8,wk),12:composite_rule(12,wk)}
    record['filter_geometry']={str(o):{v:jsonable(k[v]) for v in ('edges','panels_per_direction','gauss_order_per_panel','nodes_per_direction','field_nodes')} for o,k in kernels.items()}
    prior=json.loads((num/'WEAK_TRANSFER_DIAGNOSTIC_20261024_T64.json').read_text());priorcols=prior['row_columns']
    prior_values={}
    for ob in prior['observations']:
        for mm in ob['meshes']:
            prior_values[(ob['x'],ob['y'],mm['cells'])]={r['row']:r for r in [dict(zip(priorcols,v)) for v in mm['rows']]}
    allrows=[]
    for mesh,nodes in meshes:
        mbegin=time.perf_counter();m=len(nodes)-1
        best=sa.source_budget(nodes,cap='best',weights='chord',order=12)
        baseline=sa.source_budget(nodes,cap='lc5',weights='lc4',order=12)
        ds=np.array([r['total'] for r in best['rows']]);barsold=np.array([r['total'] for r in baseline['rows']])
        # Frozen before field evaluation; category columns of each table
        # are linear in the error vector within these declared caps.
        categories=np.array([[r[c] for r in best['rows']] for c in ('interpolation','omitted_modes','nodal_arithmetic_candidate')])
        tail_logs=np.array([r['complete_tail_log10'] for r in best['rows']])
        srules={o:source_rule(nodes,o) for o in (8,12)}
        for y in (0.,.5):
            obbegin=time.perf_counter();x=4.;computed={}
            for order,k in kernels.items():
                z=x-k['x']+1j*(y-k['y']);reg,_=old.regulator(64,z.real)
                gf=old.jets(64,z,srules[8]);values=old.values(gf,reg,k);direct=direct_values(gf,reg,k,old)
                coef,variants,meta=local_coefficients(gf,ds,k,reg,ds)
                frozen,_,_=local_coefficients(gf,barsold,k,reg,ds)
                baselinecoef,_,_=local_coefficients(gf,barsold,k,reg,barsold)
                computed[order]=dict(values=values,direct=direct,coef=coef,frozen=frozen,baseline=baselinecoef,variants=variants,meta=meta)
                if order==12:
                    gf12=old.jets(64,z,srules[12]);refined=old.values(gf12,reg,k)
            final=computed[12];coarse=computed[8];rows=[]
            if mesh=='adaptive768':
                tk=wk.kernel_data(64);zz=x-tk['x']+1j*(y-tk['y']);rr,_=old.regulator(64,zz.real);tv=old.values(old.jets(64,zz,srules[8]),rr,tk)
            else:
                pp=prior_values[(x,y,m)];tv={n:complex(*r['value64']) if isinstance(r['value64'],list) else r['value64'] for n,r in pp.items()}
            for n,co in final['coef'].items():
                if n=='DeltaQ':nn,al='DeltaQ',(0,0);ln=0
                else:nn,s=n.split(':');al=tuple(map(int,s.split(',')));ln=kernels[12]['L'][al]
                th=old.target(nn,al,ln);allow=float(co@ds);original=float(final['baseline'][n]@barsold);frozen=float(final['frozen'][n]@ds)
                af=abs(final['values'][n]-coarse['values'][n]);ef=abs(refined[n]-final['values'][n]);pf=abs(co@ds-coarse['coef'][n]@ds)
                tailterms=[math.log10(v)+tail_logs[j] for j,v in enumerate(co) if v>0]
                taillog=float(np.logaddexp.reduce(np.array(tailterms)*math.log(10))/math.log(10)) if tailterms else None
                row=dict(row=n,target=th,ABCD=co.tolist(),allowance=allow,source_ratio=allow/(.8*th),mapped_categories=(categories@co).tolist(),mapped_tail_log10=taillog,old_ledger_frozen_allowance=original,new_ledger_old_caps_allowance=frozen,actual_filter_change=float(af),actual_filter_ratio=float(af/(.1*th)),positive_filter_change=float(pf),positive_filter_ratio=float(pf/(.1*th)),evaluator_change=float(ef),evaluator_ratio=float(ef/(.1*th)),tensor64_composite12_disagreement=float(abs(final['values'][n]-tv[n])),weak_value12=old.cleanval(final['values'][n]))
                if n in final['direct']:
                    diff=abs(final['direct'][n]-final['values'][n]);row['direct_weak_disagreement']=float(diff);row['direct_weak_ratio']=float(diff/(.1*th));row['direct_filter_change']=float(abs(final['direct'][n]-coarse['direct'][n]));row['direct_filter_ratio']=row['direct_filter_change']/(.1*th)
                rows.append(row);allrows.append(dict(mesh=mesh,t=64,x=x,y=y,**row))
            obs=dict(mesh=mesh,cells=m,t=64,x=x,y=y,source_errors=ds.tolist(),old_source_errors=barsold.tolist(),source_ledger=best,rows=rows,source_variants={kind:{n:float(co@ds) for n,co in vals.items()} for kind,vals in final['variants'].items()},metadata=final['meta'],field_filter_runtime_seconds=time.perf_counter()-obbegin)
            record['observations'].append(obs)
            print('completed',mesh,y,'runtime',obs['field_filter_runtime_seconds'],'total',time.perf_counter()-started,flush=True)
        print('mesh_runtime',mesh,time.perf_counter()-mbegin,flush=True)
    metrics=('source_ratio','actual_filter_ratio','positive_filter_ratio','evaluator_ratio','direct_weak_ratio','direct_filter_ratio')
    record['maxima']={k:max((r for r in allrows if k in r),key=lambda r:r[k]) for k in metrics}
    record['mesh_maxima']={mesh:{k:max((r for r in allrows if r['mesh']==mesh and k in r),key=lambda r:r[k]) for k in metrics} for mesh,_ in meshes}
    record['evaluator_indicator_scope']='Weak observable evaluator8/12 only (jets0,2); direct four-jet evaluator quadrature and rounding unpaid'
    record['continuous_filter_remainder']='unpaid; composite refinements and direct/weak checks are diagnostics'
    record['cost']={'composite_panels_per_direction': 16, 'coarse_field_nodes': 16384, 'fine_field_nodes': 36864, 'tensor64_field_nodes': 4096, 'fine_to_tensor64_field_nodes_ratio': 9, 'distinct_rule_field_nodes_per_observation': 53248, 'field_evaluations_counted_with_repeated_source_rules_per_observation': 90112, 'main_source_node_field_point_interactions': 3001024512, 'note': 'Includes8-source coarse and fine plus12-source fine evaluations; adaptive tensor64 comparison adds two768*8*4096 interactions. Historical reused tensor values incur no new field cost.'}
    record['optional_t96_executed']=False
    assert max(r['source_ratio'] for r in allrows)>1 or max(r['actual_filter_ratio'] for r in allrows)>1
    # Check only nodal source arithmetic; later evaluator/filter remain distinct.
    mp.mp.dps=80;ratios=[]
    for mesh,nodes in meshes:
        f=sa.phi(nodes);rat=0.
        for u,val in zip(nodes,f):
            true=old.phi_mp(mp.mpf(float(u)));err=abs(mp.mpf(float(val))-true);sig=mp.mpf('1e-12')*abs(mp.mpf(float(val)))+mp.mpf('1e-300');rat=max(rat,float(err/sig))
        ratios.append(dict(mesh=mesh,observed_max_ratio=rat,status='sample candidate only'))
    record['nodal_candidate']=ratios
    record['runtime_seconds']=time.perf_counter()-started
    record['numerical_budget']=dict(cap_seconds=1800,measured_main_run_seconds=record['runtime_seconds'],auxiliary_controls_source_sanity_conservative_debit_seconds=10,total_conservative_debit_seconds=record['runtime_seconds']+10)
    record['source_control_record']=json.loads(Path(__file__).with_name('SOURCE_CONTROLS.json').read_text())
    packet=repo/'papers/investigations-5/01_heat_density_asymptotics/research-progress/handoffs/HDA-17-AN02.md'
    record['inputs']={n:dict(expected=h,actual=sha(repo/n),match=h==sha(repo/n)) for n,h in re.findall(r'\| `([^`]+)` \| `([0-9a-f]{64})` \|',packet.read_text())}
    record['scripts']={p.name:sha(p) for p in [Path(__file__),Path(sa.__file__),Path(__file__).with_name('check_source.py')]}
    # Compact row arrays; complete column map and all errors retained.
    columns=list(allrows[0])
    for c in ('direct_weak_disagreement','direct_weak_ratio','direct_filter_change','direct_filter_ratio'):
        if c not in columns:columns.append(c)
    columns=[c for c in columns if c not in ('mesh','t','x','y')];record['row_columns']=columns
    for ob in record['observations']:ob['rows']=[[r.get(c) for c in columns] for r in ob['rows']]
    output.write_text(json.dumps(jsonable(record),separators=(',',':'),allow_nan=False)+'\n');assert output.stat().st_size<1048576
    print('DONE',record['runtime_seconds'],output.stat().st_size,flush=True)
    print(json.dumps({k:{c:v.get(c) for c in ('mesh','y','row',k)} for k,v in record['maxima'].items()}),flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--repo',type=Path,required=True);p.add_argument('--output',type=Path,required=True);args=p.parse_args();run(args.repo,args.output)
