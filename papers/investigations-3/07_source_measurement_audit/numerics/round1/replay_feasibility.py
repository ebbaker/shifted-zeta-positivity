#!/usr/bin/env python3
"""Bounded independent finite coefficient feasibility and Euclidean solves.

Prepared for Edward Baker, 16 October 2026 America/New_York.
LLM assistance: gpt-6.1-sol (Codex), reasoning effort ultra.
This is an independent floating calculation, not a formal review or a certificate.
No import from the earlier Claude scripts. Scope: 32 frozen cases only.

Read EVALUATION_DPS{80,120}.json, write own output JSON. Small dense SVD for
Euclidean equality solves; all active sets for positive Euclidean projection;
2D convex hull separation for explicit strictly separating witnesses. Stored
witnesses are intended for subsequent outward rounded sign checks.
"""
import argparse
import hashlib
import itertools
import json
import time
from pathlib import Path
import mpmath as mp


def dot(a,b):
    return mp.fsum(x*y for x,y in zip(a,b))


def norm(v):
    return mp.sqrt(dot(v,v))


def take_columns(A,F):
    return mp.matrix([[A[i,j] for j in F] for i in range(A.rows)])


def min_norm(A,b):
    """Row-scaled SVD; return floating equality candidate and dual multiplier.

    Never discard a positive computed singular value by a rank threshold.
    A large residual is called inconsistent only in the low-column cases
    with a separately recorded nonzero augmented minor.
    """
    m,k=A.rows,A.cols
    if k==0:
        return {'x':mp.matrix(0,1),'resid':b.copy(),'resid_norm':norm(b),
                'lambda':mp.matrix(m,1),'singular_values':[]}
    scales=[norm([A[i,j] for j in range(k)]) for i in range(m)]
    scales=[s if s else mp.mpf(1) for s in scales]
    S=mp.matrix([[A[i,j]/scales[i] for j in range(k)] for i in range(m)])
    c=mp.matrix([b[i]/scales[i] for i in range(m)])
    U,s,V=mp.svd_r(S)
    x=mp.matrix(k,1)
    lam=mp.matrix(m,1)
    for j in range(len(s)):
        if not s[j]:
            continue
        ucb=dot([U[i,j] for i in range(m)],c)
        for l in range(k):
            x[l]+=V[j,l]*ucb/s[j]
        for i in range(m):
            lam[i]-=U[i,j]*ucb/(s[j]*s[j]*scales[i])
    residual=A*x-b
    return {'x':x,'resid':residual,'resid_norm':norm(residual),
            'scaled_resid_norm':norm([residual[i]/scales[i] for i in range(m)]),
            'lambda':lam,'singular_values':list(s),'row_scales':scales}


def augmented_minor(P,q):
    """For k<3, nonzero minor proves affine equality inconsistency.

    Normalization changes columns by positive beta and target by positive M.
    Thus original feasibility iff columns [p_x,p_y,1] span [q_x,q_y,1].
    """
    k=len(P)
    rows=[[p[0] for p in P]+[q[0]],
          [p[1] for p in P]+[q[1]], [mp.mpf(1)]*(k+1)]
    if k==1:
        vals=[]
        for ri in itertools.combinations(range(3),2):
            v=mp.det(mp.matrix([[rows[i][j] for j in range(2)] for i in ri]))
            vals.append((abs(v),ri,v))
        _,ri,v=max(vals)
        return {'size':2,'row_indices':list(ri),'column_labels':['free_node','target'],
                'value':v,'formula':'det augmented normalized point columns; target is last column'}
    if k==2:
        return {'size':3,'row_indices':[0,1,2],
                'column_labels':['free_node_1','free_node_2','target'],
                'value':mp.det(mp.matrix(rows)),
                'formula':'det[[B0_n/beta_n],[B1_n/beta_n],[1]], with target rjet/M last'}
    return None


def strict_separator(P,q):
    """Find nearest hull vertex/edge and a strict normalized Farkas witness.

    If d=q-p*, all hull points have d.(p-p*)<=0. The midpoint offset
    c=d.p*+||d||^2/2 yields y=(-d_x,-d_y,c), y.(p,1)>0 and y.(q,1)<0.
    Enumerating every pair includes all actual hull edges and is tiny here.
    """
    candidates=[]
    for i,p in enumerate(P):
        candidates.append((list(p),[i],[mp.mpf(1)]))
    for i,j in itertools.combinations(range(len(P)),2):
        v=[P[j][a]-P[i][a] for a in range(2)]
        vv=dot(v,v)
        if not vv:
            continue
        alpha=dot([q[a]-P[i][a] for a in range(2)],v)/vv
        alpha=max(mp.mpf(0),min(mp.mpf(1),alpha))
        candidates.append(([P[i][a]+alpha*v[a] for a in range(2)],
                           [i,j],[1-alpha,alpha]))
    # Numerical finding only. Stored signs will be separately certified.
    eps=mp.power(10,-mp.mp.dps//2)
    valid=[]
    for pstar,ids,coeffs in candidates:
        d=[q[a]-pstar[a] for a in range(2)]
        d2=dot(d,d)
        if d2<eps*eps:
            continue
        supporting=max(dot(d,[p[a]-pstar[a] for a in range(2)]) for p in P)
        if supporting>eps*max(mp.mpf(1),d2):
            continue
        y=[-d[0],-d[1],dot(d,pstar)+d2/2]
        yn=max(abs(v) for v in y)
        y=[v/yn for v in y]
        columns=[dot(y,[p[0],p[1],1]) for p in P]
        target=dot(y,[q[0],q[1],1])
        if min(columns)>0 and target<0:
            valid.append((d2,{'normalized_point_multiplier':y,
                 'column_values':columns,'target_value':target,
                 'minimum_column_margin':min(columns),'target_margin':-target,
                 'nearest_hull_point':pstar,'contact_free_indices':ids,
                 'contact_convex_weights':coeffs,'distance_to_hull':mp.sqrt(d2),
                 'definition':'p_n=(B0_n/beta_n,B1_n/beta_n); q=rjet/M; y.(p_n,1)>0 and y.(q,1)<0'}))
    return min(valid,key=lambda z:z[0])[1] if valid else None


def build_case(case,beta,N,tail,anchor):
    B=mp.matrix([[mp.mpf(v) for v in row[:N]] for row in case['B']])
    h=mp.matrix([mp.mpf(v) for v in case['h']])
    bta=beta[:N]
    tailbeta=mp.mpf('0.5')-mp.fsum(bta)
    tailjet=[h[i]-mp.fsum(B[i,j] for j in range(N)) if tail=='theta' else mp.mpf(0)
             for i in range(2)]
    free=list(range(1 if anchor else 0,N))
    E=mp.matrix([[B[i,j] for j in free] for i in range(2)]+
                [[bta[j] for j in free]])
    r=mp.matrix([-tailjet[0]-(B[0,0] if anchor else 0),
                 -tailjet[1]-(B[1,0] if anchor else 0),
                 mp.mpf('0.5')-(tailbeta if tail=='theta' else 0)-(bta[0] if anchor else 0)])
    rdelta=r-E*mp.matrix([1]*len(free))
    return B,h,tailbeta,tailjet,free,E,r,rdelta


def solve_case(case,beta,N,tail,anchor):
    B,h,tailbeta,tailjet,free,E,r,rdelta=build_case(case,beta,N,tail,anchor)
    k=len(free)
    P=[[B[0,j]/beta[j],B[1,j]/beta[j]] for j in free]
    M=r[2]
    q=[r[0]/M,r[1]/M]
    eq=min_norm(E,rdelta)
    d=[mp.mpf(0)]*N
    for j,v in zip(free,eq['x']):
        d[j]=v
    a=[1+v for v in d]
    eps=mp.power(10,-mp.mp.dps//2)
    minor=augmented_minor(P,q)
    inconsistent=minor is not None and abs(minor['value'])>eps
    eq_record={'status':'floating_inconsistent_with_augmented_minor' if inconsistent else 'floating_equality_candidate',
               'delta_first_N':d,'a_first_N':a,'first_N_raw_l2_distance':norm(d),
               'full_raw_l2_distance': 'infinity (zero tail)' if tail=='zero' else norm(d),
               'beta_weighted_l1_at_euclidean_solution_first_N':mp.fsum(beta[j]*abs(d[j]) for j in range(N)),
               'full_beta_weighted_l1_at_euclidean_solution':mp.fsum(beta[j]*abs(d[j]) for j in range(N))+(tailbeta if tail=='zero' else 0),
               'weighted_metric_label':'value at Euclidean equality minimizer; not separately optimized',
               'raw_equality_residual':list(eq['resid']),
               'row_scaled_equality_residual_norm':eq['scaled_resid_norm'],
               'row_scaled_positive_singular_values':eq['singular_values'],
               'normalization_residual':dot(beta[:N],a)+(tailbeta if tail=='theta' else 0)-mp.mpf('0.5'),
               'minimum_a':min(a),'augmented_minor':minor}
    if inconsistent:
        # Least squares data are diagnostics only, not a genuine collision distance.
        eq_record['first_N_raw_l2_distance']=None
        eq_record['full_raw_l2_distance']='infinity (infeasible equalities)'
        eq_record['candidate_label']='least squares diagnostics, not an equality solution'
        eq_record['beta_weighted_l1_at_euclidean_solution_first_N']=None
        eq_record['full_beta_weighted_l1_at_euclidean_solution']=None
        eq_record['weighted_metric_label']='not applicable: equalities inconsistent'
    positive=[]
    for active_count in range(k+1):
        for Z_tuple in itertools.combinations(range(k),active_count):
            Z=set(Z_tuple)
            F=[j for j in range(k) if j not in Z]
            if not F:
                continue
            EF=take_columns(E,F)
            # a_Z=0, objective projection is a_F=1+delta_F.
            bF=r-EF*mp.matrix([1]*len(F))
            sol=min_norm(EF,bF)
            if sol['scaled_resid_norm']>eps:
                continue
            af=[1+v for v in sol['x']]
            if min(af)<-eps:
                continue
            aa=[mp.mpf(0)]*k
            for j,v in zip(F,af):
                aa[j]=v
            obj=mp.fsum((v-1)**2 for v in aa)
            lam=sol['lambda']
            mu=[aa[j]-1+mp.fsum(E[i,j]*lam[i] for i in range(3)) for j in range(k)]
            # For full-row-rank faces lambda is determined and this directly tests KKT.
            kkt_sign=(min([mu[j] for j in Z] or [mp.inf])>=-eps)
            kkt_free=max([abs(mu[j]) for j in F] or [0])
            positive.append((obj,aa,F,sorted(Z),lam,mu,sol,kkt_sign,kkt_free))
    sep=None
    if not positive:
        sep=strict_separator(P,q)
        positive_record={'status':'floating_infeasible_with_strict_separator' if sep else 'unresolved_no_candidate_or_separator',
                         'strict_farkas_separator':sep,'active_sets_enumerated':2**k}
    else:
        obj,aa,F,Z,lam,mu,sol,kkt_sign,kkt_free=min(positive,key=lambda z:z[0])
        a_full=[mp.mpf(1) if anchor and j==0 else mp.mpf(0) for j in range(N)]
        for j,v in zip(free,aa):
            a_full[j]=v
        dd=[v-1 for v in a_full]
        positive_record={'status':'floating_positive_euclidean_optimum_candidate' if kkt_sign else 'floating_positive_candidate_kkt_unresolved',
            'a_first_N':a_full,'delta_first_N':dd,'active_zero_nodes':[free[j]+1 for j in Z],
            'positive_free_nodes':[free[j]+1 for j in F],
            'first_N_raw_l2_distance':mp.sqrt(obj),
            'full_raw_l2_distance':'infinity (zero tail)' if tail=='zero' else mp.sqrt(obj),
            'full_beta_weighted_l1_at_positive_euclidean_solution':mp.fsum(beta[j]*abs(dd[j]) for j in range(N))+(tailbeta if tail=='zero' else 0),
            'weighted_metric_label':'value at positive Euclidean optimum; not separately optimized',
            'raw_equality_residual':list(E*mp.matrix(aa)-r),
            'normalization_residual':dot(beta[:N],a_full)+(tailbeta if tail=='theta' else 0)-mp.mpf('0.5'),
            'kkt_raw_equality_multiplier':list(lam),
            'kkt_nonnegative_multiplier_free_index_order':mu,
            'kkt_active_multiplier_margin':min([mu[j] for j in Z] or [mp.inf]),
            'kkt_free_stationarity_residual_max':kkt_free,
            'kkt_signs_hold_numerically':kkt_sign,
            'active_sets_enumerated':2**k,'feasible_faces_found':len(positive)}
    return {'point_id':case['id'],'t':case['t'],'x':case['x'],'N':N,'tail':tail,'anchor_a1':anchor,
            'free_nodes':[j+1 for j in free],'tail_beta':tailbeta,'tail_jet':tailjet,
            'normalized_mass_M':M,'normalized_target_q':q,
            'equality':eq_record,'positive':positive_record}


def strings(obj):
    if isinstance(obj,mp.mpf):
        return mp.nstr(obj,mp.mp.dps-8)
    if isinstance(obj,dict):
        return {k:strings(v) for k,v in obj.items()}
    if isinstance(obj,(tuple,list)):
        return [strings(v) for v in obj]
    return obj


def run(input_path,output_path):
    start=time.monotonic()
    data=json.loads(Path(input_path).read_text())
    mp.mp.dps=data['dps']
    beta=[mp.mpf(v) for v in data['beta']]
    results=[]
    wanted={'t025_x44_1303','t0_x60'}
    for case in data['cases']:
        if case['id'] not in wanted:
            continue
        for N,tail,anchor in itertools.product((2,3,4,6),('theta','zero'),(False,True)):
            results.append(solve_case(case,beta,N,tail,anchor))
    assert len(results)==32,len(results)
    out={'schema':'source_measurement_feasibility_v1','dps':data['dps'],
         'status':'independent floating replay, certification separate',
         'prepared_for':'Edward Baker','model':'gpt-6.1-sol (Codex)','effort':'ultra',
         'scope':'two fixed points; N=2,3,4,6; theta/zero tail; anchor off/on',
         'algorithm':'row-scaled mpmath SVD; all nonnegative active faces; strict 2D convex hull Farkas witnesses',
         'error_propagation':'floating candidates and witnesses only; root will propagate outward rounded evaluation bounds',
         'input':str(input_path),'input_sha256':hashlib.sha256(Path(input_path).read_bytes()).hexdigest(),'runtime_seconds':time.monotonic()-start,'cases':results}
    Path(output_path).write_text(json.dumps(strings(out),indent=2)+'\n')
    print(json.dumps({'output':str(output_path),'dps':data['dps'],'runtime_seconds':out['runtime_seconds'],
       'positive_status_counts':{s:sum(r['positive']['status']==s for r in results) for s in sorted({r['positive']['status'] for r in results})}}))


if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('input')
    p.add_argument('output')
    args=p.parse_args()
    run(args.input,args.output)
