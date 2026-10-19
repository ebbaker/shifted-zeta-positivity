#!/usr/bin/env python3
"""S02-T2: complete closed-cell frozen/full jets on B, with paid consumers.

Prepared for Edward Baker, 19 October 2026, with substantial LLM assistance.
Authoring gpt-6.1-sol, actual effort ultra. Internal research/verification.
Requires python-flint 0.9.0. Full tables are external regenerable archives.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import platform
import sys
import time

import flint
from flint import arb,acb,acb_series,ctx

INV=Path('papers/investigations-3/11_arithmetic_collision_rigidity')
LANE=INV/'symmetries/02_cutoff_reflection'
SCHEMA='s02-complete-frozen-jets-v1'


def A(x):return arb(x.numerator)/x.denominator if isinstance(x,F) else arb(x)
def out(x):return x.str(38,more=True)
def interval(a,b):
    a,b=A(a),A(b);return arb((a+b)/2,((b-a)/2).upper())
def check(c,msg):
    if not c:raise ArithmeticError(msg)
def digest(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def square(x):
    lo=(x.abs_lower()*x.abs_lower()).lower();hi=(x.abs_upper()*x.abs_upper()).upper()
    return arb((lo+hi)/2,((hi-lo)/2).upper())
def load(path,name):
    spec=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(spec);sys.modules[name]=m;spec.loader.exec_module(m);return m

def schur_residual_cover(eta,grid=8):
    """All real first three Schur coefficients; gamma remains in [-1,1]."""
    check(grid==8 and eta>=0,'fixed Schur parameter grid/allowance')
    rows=[]
    for ia in range(grid):
        a=interval(F(-1)+F(2)*ia/grid,F(-1)+F(2)*(ia+1)/grid);aa=square(a);d=1-aa
        for ib in range(grid):
            b=interval(F(-1)+F(2)*ib/grid,F(-1)+F(2)*(ib+1)/grid);bb=square(b)
            rows.append([eta*a,2*eta*d*b,8*eta*d*((1-bb)*interval(-1,1)-a*bb)])
    return rows


def q_sign_forms(jets,b,bp):
    q0,q1,q2=jets
    energy=square(q0)+square(q1+b*q0)
    laguerre=square(q1)-q0*q2-bp*square(q0)
    return energy,laguerre,laguerre-energy/100


def sign_tests(jets,b,bp,eta,cover=None):
    """Source-neutral actual acceptance path; all local residual costs paid."""
    check(eta>=0 and all(v.is_finite() for v in jets),'finite sign interface')
    boxes=[v+arb(0,(f*eta).upper()) for v,f in zip(jets,[1,2,8])]
    eb,lb,mb=q_sign_forms(boxes,b,bp)
    if eta==0:
        return {'box_energy':eb,'box_laguerre':lb,'box_excess':mb,
                'schur_laguerre_lower':lb.lower(),'schur_excess_lower':mb.lower()}
    cover=cover or schur_residual_cover(eta)
    L=None;M=None
    for errors in cover:
        _,lag,exc=q_sign_forms([v+e for v,e in zip(jets,errors)],b,bp)
        L=lag.lower() if L is None else min(L,lag.lower())
        M=exc.lower() if M is None else min(M,exc.lower())
    return {'box_energy':eb,'box_laguerre':lb,'box_excess':mb,
            'schur_laguerre_lower':L,'schur_excess_lower':M}


def first_jet_test(jets,omega,eta):
    check(omega.abs_lower()>0 and eta>=0,'first-jet interface needs nonzero phase derivative')
    W=acb(jets[0],-jets[1]/omega)
    error=(eta*max(arb(1),2/omega.abs_lower())).upper()
    # Real Schwarz-Pick necessary condition; division free for robustness.
    schur=(square(jets[0]).lower()+eta/2*jets[1].abs_lower()-eta*eta).lower()
    if eta==0:schur=W.abs_lower()
    return W,error,(W.abs_lower()-error).lower(),schur


class ClosedJetEvaluator:
    """B-only pointwise local jets; frozen centers must not be differentiated."""
    def __init__(self,repo,bits):
        self.repo=Path(repo);self.bits=bits
        check(bits in [192,256],'retained precision must be 192 or 256')
        ctx.prec=bits;ctx.cap=8
        self.oldpath=self.repo/LANE/'numerics/check_cutoff_reflection.py'
        self.old=load(self.oldpath,'s02_t2_original_'+str(bits))
        recpath=self.repo/LANE/'numerics/S02_MATCHED_CORRECTION_20261019.json'
        self.bound_record=json.loads(recpath.read_text());self.bound_sha=digest(recpath)
        check(self.bound_record['script_sha256']==digest(self.repo/LANE/'numerics/compare_correction_representations.py'),'matched bound script pin')
        for rel,pin in self.bound_record['source_sha256'].items():
            check(digest(self.repo/rel)==pin,'matched bound source pin '+rel)
        selected=[x for x in self.bound_record['runs'] if x['bits']==bits]
        check(len(selected)==1,'bound precision selection')
        bound=selected[0]['boxes'][0]
        check(bound['label']=='B' and bound['grid']==[4,24,8] and bound['radius']=='1/2' and bound['fixed_cutoff']==8,'bound domain contract')
        self.eta={'frozen':arb(bound['eta']['frozen']).upper(),'full':arb(bound['eta']['full_same_edge']).upper()}
        self.covers={k:schur_residual_cover(v) for k,v in self.eta.items()}
        self.pi=arb.pi();self.k=self.pi/8
        self.logGc=arb(7)/4*arb(1000).log()-125*self.pi

    def phase(self,x,t):
        s=(1-acb(0,1)*acb(x))/2;o=self.old;ii=acb(0,1)
        mp=lambda v:o.alpha(v)*(1+t*o.alphap(v)/2)
        mpp=lambda v:o.alphap(v)*(1+t*o.alphap(v)/2)+t*o.alpha(v)*o.alphapp(v)/2
        th=((o.mt(s,t)-o.mt(1-s,t))/(2*ii)).real
        w=(-(mp(s)+mp(1-s))/4).real
        wp=(ii*(mpp(s)-mpp(1-s))/8).real
        b=(-ii*(mp(s)-mp(1-s))/4).real
        bp=(-(mpp(s)+mpp(1-s))/8).real
        logA=((o.mt(s,t)+o.mt(1-s,t))/2).real
        return th,w,wp,b,bp,(self.logGc-logA).exp()

    def jets(self,x,t,recenter=None):
        o=self.old;ii=acb(0,1);th,w,wp,b,bp,chi=self.phase(x,t)
        if recenter is not None:
            thmid=self.phase(A(recenter),t)[0]
            # Mean-value integral at fixed real t; no frozen-family identity.
            th=thmid+w*(x-A(recenter))
        check(w<0,'phase orientation on B')
        ss=(1-ii*acb(x))/2;P=acb(1);Px=acb(0);Pxx=acb(0)
        for n in range(2,9):
            ell=arb(n).log();wn=(t*ell*ell/4-(ss+t*o.alpha(ss)/2)*ell).exp()
            coeff=ii*ell/2*(1+t*o.alphap(ss)/2)
            P+=wn;Px+=coeff*wn;Pxx+=(coeff*coeff+t*ell*o.alphapp(ss)/8)*wn
        ee=(ii*th).exp()
        g=[2*(ee*P).real,
           2*(ee*(ii*w*P+Px)).real,
           2*(ee*((ii*wp-w*w)*P+2*ii*w*Px+Pxx)).real]
        js,jp=o.J(x,t,8);q=-o.W_real(x,t)
        c=(q*js).real;u=(q*jp).real;h=self.k+b
        frozen=[g[0]-c,g[1]+h*c,g[2]-(h*h-bp)*c]
        # Coherent full analytic jets; full correction retains all profile jets.
        z=acb_series([acb(x),acb(1)],3)
        C=-o.W_real(z,t)*o.J(z,t,8)[0]
        full=[g[j]-math.factorial(j)*C[j].real for j in range(3)]
        for family in [frozen,full]:check(all(v.is_finite() for v in family),'nonfinite exact approximant image')
        return {'theta':th,'omega':w,'omega_x':wp,'b':b,'b_x':bp,'chi':chi,
                'frozen':frozen,'full':full,'u':u,'h':h}

    def enclose(self,t0,t1,x0,x1):
        t0,t1,x0,x1=map(F,(t0,t1,x0,x1))
        check(F(1,100)<=t0<=t1<=F(1,5) and F(999)<=x0<=x1<=F(1001),'closed evaluator outside B')
        t=interval(t0,t1);x=interval(x0,x1);xc=(x0+x1)/2
        data=self.jets(x,t,xc);center=self.jets(A(xc),t)
        half=A((x1-x0)/2);res={}
        for family in ['frozen','full']:
            f=data[family];fm=center[family];eta=self.eta[family];w=data['omega'];wp=data['omega_x'];b=data['b'];bp=data['b_x']
            W,eJ,direct,schur=first_jet_test(f,w,eta)
            Wm=acb(fm[0],-fm[1]/center['omega'])
            Rloc=f[0]+f[2]/(w*w)-wp*f[1]/(w*w*w)
            lip=(w.abs_upper()*(W.abs_upper()+Rloc.abs_upper())).upper()
            defect=arb(0)
            if family=='frozen':
                defect=(data['u'].abs_upper()*(1+(data['h']/w)**2).sqrt().abs_upper()).upper()
                lip=(lip+defect).upper()
            propagated=(Wm.abs_lower()-half*lip).lower()
            approximant=max(W.abs_lower(),propagated)
            paid=(approximant-eJ).lower()
            physical=[f[0],f[1]+b*f[0],f[2]+2*b*f[1]+(b*b+bp)*f[0]]
            pe=[eta,(eta*(2+b.abs_upper())).upper(),
                (eta*(8+4*b.abs_upper()+(b*b+bp).abs_upper())).upper()]
            ps=(pe[0]*pe[0]+pe[1]*pe[1]).sqrt().upper()
            physical_lower=(acb(physical[0],physical[1]).abs_lower()-ps).lower()
            tests=sign_tests(f,b,bp,eta,self.covers[family])
            res[family]={'Q_jet':f,'physical_jet_over_A':physical,
                         'Q_residual_errors':[eta,2*eta,8*eta],'physical_residual_errors':pe,
                         'whole_cell_Q_image_radii':[v.rad().upper() for v in f],
                         'phase_jet_error':eJ,'naive_phase_radius_lower':direct,
                         'approx_phase_radius_lower':approximant,'paid_phase_radius_lower':paid,
                         'physical_radius_lower':physical_lower,'joint_Schur_first_margin':schur,
                         'midpoint_Lipschitz_upper':lip,'diagonal_correction_payment':defect,
                         'diagonal_f0_derivative_defect':-data['u'] if family=='frozen' else arb(0),
                         'diagonal_f1_derivative_defect':data['h']*data['u'] if family=='frozen' else arb(0),
                         **tests}
        return data,res


def source_cell(hh,ev,data,t0,t1,x0,x1):
    v,budgets=ev.enclose(t0,t1,x0,x1);chi=data['chi'];b=data['b'];bp=data['b_x'];w=data['omega']
    q=[chi*v[0],chi*(v[1]-b*v[0]),chi*(v[2]-2*b*v[1]+(b*b-bp)*v[0])]
    radius=acb(q[0],-q[1]/w).abs_lower()
    L=square(v[1])-v[0]*v[2];E=square(v[0])+square(v[1]);M=L-E/100
    e0=chi.abs_upper()*budgets[0]['total'];e1=chi.abs_upper()*(budgets[1]['total']+b.abs_upper()*budgets[0]['total'])
    ephase=(e0*e0+(e1/w.abs_lower())**2).sqrt().upper()
    return {'physical_jet_over_Gc':v,'Q_complete_jet':q,'paid_phase_radius_lower':radius,
            'complete_phase_error_upper':ephase,'Gc_signed_excess':M,
            'signed_excess_over_A2':chi*chi*M,
            'complete_physical_errors_over_Gc':[row['total'] for row in budgets],
            'error_components_over_Gc':budgets}


def serialize(obj):
    if isinstance(obj,dict):return {k:serialize(v) for k,v in obj.items()}
    if isinstance(obj,list):return [serialize(v) for v in obj]
    if isinstance(obj,tuple):return [serialize(v) for v in obj]
    if isinstance(obj,(arb,acb)):return out(obj) if isinstance(obj,arb) else str(obj)
    if isinstance(obj,F):return str(obj)
    return obj


def canonical_line(data):return (json.dumps(serialize(data),sort_keys=True,separators=(',',':'))+'\n').encode()


def locate_archive(repo,relative):
    rel=Path(relative);check(not rel.is_absolute() and '..' not in rel.parts and rel.parts[0]=='output','invalid archive relative path')
    normal=Path(repo)/LANE/'numerics'/rel
    if normal.is_file():return normal
    root=os.environ.get('S02_JET_ARCHIVES')
    if root and (Path(root)/rel).is_file():return Path(root)/rel
    raise FileNotFoundError('Missing S02 jet archive '+str(rel)+'. Regenerate with evaluate_complete_frozen_jets.py; see S02 ARCHIVES.md or set S02_JET_ARCHIVES.')


def load_cell_archive(repo,receipt):
    """Fail closed before exposing any consumer rows; hashes identify data only."""
    p=locate_archive(repo,receipt['relative_path'])
    check(digest(p)==receipt['stored_sha256'],'stored archive hash mismatch')
    h=hashlib.sha256();lines=0
    with gzip.open(p,'rb') as f:
        header=json.loads(next(f));lines=1
        for line in f:h.update(canonical_line(json.loads(line)));lines+=1
    check(h.hexdigest()==receipt['canonical_jsonl_content_sha256'],'canonical archive hash mismatch')
    check(lines==receipt['cells']+1,'archive row count mismatch')
    with gzip.open(p,'rt') as f:
        header=json.loads(next(f));check(header['schema']==SCHEMA and header['kind']=='cell_archive','archive schema')
        check(header['bits']==receipt['bits'],'archive precision')
        check(digest(Path(repo)/LANE/'numerics/evaluate_complete_frozen_jets.py')==header['producer_sha256'],'archive evaluator pin')
        for rel,pin in header['source_sha256'].items():check(digest(Path(repo)/rel)==pin,'archive source pin '+rel)
        for index,line in enumerate(f):
            row=json.loads(line)
            check(row['cell']==[index//128,index%128],'archive cell order')
            yield row


def make_slab(it):
    return {'t_index':it,'methods':{m:{'cells':0,'firstjet_pass_cells':0,'physical_firstjet_pass_cells':0,
        'joint_firstjet_pass_cells':0,'box_L0_pass_cells':0,'box_excess_pass_cells':0,
        'Schur_L0_pass_cells':0,'Schur_excess_pass_cells':0,'minima':{},'maxima':{}}
        for m in ['frozen','full']},'source_minimum_radius':None,'source_minimum_signed_excess_Gc2':None,
        'source_maximum_phase_error':arb(0),'source_minimum_signed_excess_A2':None}


def update_slab(slab,methods,reference,x0,x1):
    for key,row in methods.items():
        agg=slab['methods'][key];agg['cells']+=1
        for count,value in [('firstjet_pass_cells',row['paid_phase_radius_lower']),
            ('physical_firstjet_pass_cells',row['physical_radius_lower']),
            ('joint_firstjet_pass_cells',row['joint_Schur_first_margin']),
            ('box_L0_pass_cells',row['box_laguerre'].lower()),('box_excess_pass_cells',row['box_excess'].lower()),
            ('Schur_L0_pass_cells',row['schur_laguerre_lower']),('Schur_excess_pass_cells',row['schur_excess_lower'])]:
            agg[count]+=int(value>0)
        for name in ['paid_phase_radius_lower','naive_phase_radius_lower','physical_radius_lower','joint_Schur_first_margin','schur_laguerre_lower','schur_excess_lower']:
            val=row[name].lower()
            if name not in agg['minima'] or val<agg['minima'][name]['bound']:
                agg['minima'][name]={'bound':val,'x':[str(x0),str(x1)]}
        for name in ['phase_jet_error','midpoint_Lipschitz_upper','diagonal_correction_payment']:
            agg['maxima'][name]=max(agg['maxima'].get(name,arb(0)),row[name].abs_upper())
    v=reference['paid_phase_radius_lower'];m=reference['Gc_signed_excess'].lower()
    slab['source_minimum_radius']=v if slab['source_minimum_radius'] is None else min(slab['source_minimum_radius'],v)
    slab['source_minimum_signed_excess_Gc2']=m if slab['source_minimum_signed_excess_Gc2'] is None else min(slab['source_minimum_signed_excess_Gc2'],m)
    slab['source_maximum_phase_error']=max(slab['source_maximum_phase_error'],reference['complete_phase_error_upper'])
    ma=reference['signed_excess_over_A2'].lower()
    slab['source_minimum_signed_excess_A2']=ma if slab['source_minimum_signed_excess_A2'] is None else min(slab['source_minimum_signed_excess_A2'],ma)


def exact_checks(e):
    o=e.old;checks=[];t=arb(21)/200
    for X in [arb(999),arb(1000),arb(1001)]:
        data=e.jets(X,t);z=acb_series([acb(X),acb(1)],3)
        full=o.series_approximation(acb(X),t,True)
        num=sum((o.mode(z,t,n) for n in range(1,9)),acb_series([0]))
        fr=(num-o.correction(acb(X),t,8)*(-e.k*(z-X)).exp())/o.normalizer(z,t)
        for j in range(3):
            check((data['frozen'][j]-math.factorial(j)*fr[j].real).contains(0),'frozen stable vs exact series')
            check((data['full'][j]-math.factorial(j)*full[j].real).contains(0),'full stable vs exact series')
        # Differentiate the diagonal jet family, with its varying coefficient.
        ss=(1-acb(0,1)*z)/2
        mp=lambda v:o.alpha(v)*(1+t*o.alphap(v)/2)
        bser=(-acb(0,1)*(mp(ss)-mp(1-ss))/4)
        cg=o.correction(z,t,8)/o.normalizer(z,t)
        G=num/o.normalizer(z,t)
        Fdiag=G-cg
        f1diag=G.derivative()+(e.k+bser)*cg
        check((Fdiag[1].real-(data['frozen'][1]-data['u'])).contains(0),'diagonal f0 correction')
        check((f1diag[1].real-(data['frozen'][2]+data['h']*data['u'])).contains(0),'diagonal f1 correction')
        checks.append({'x':out(X),'frozen_full_exact_series':True,'diagonal_derivative_defects_checked':True,
                       'frozen_point_arithmetic_and_input_rounding_radii':[out(v.rad().upper()) for v in data['frozen']],
                       'full_point_arithmetic_and_input_rounding_radii':[out(v.rad().upper()) for v in data['full']]})
    # Exact analytic disk event fixtures challenge the actual paid sign test.
    fixtures=[];eta=arb(1)/4
    for label,r in [('constant',[eta,arb(0),arb(0)]),('linear',[arb(0),2*eta,arb(0)]),
                    ('quadratic',[arb(0),arb(0),8*eta]),
                    ('Schur_extremal',[eta/arb(3).sqrt(),arb(0),8*eta*(1-arb(1)/3)])]:
        f=[-r[0],-r[1],2-r[2]]
        test=sign_tests(f,arb(0),arb(0),eta)
        _,_,margin,schur=first_jet_test(f,arb(1),eta)
        check(not(test['schur_excess_lower']>0) and not(margin>0) and not(schur>0),'event fixture passed strict acceptance')
        fixtures.append({'case':label,'Schur_excess_lower':out(test['schur_excess_lower']),
                         'firstjet_margin':out(margin),'rejected':True})
    try:e.enclose(F(1,100),F(1,5),F(999),F(1002))
    except ArithmeticError:outside=True
    else:raise ArithmeticError('outside B accepted')
    return {'series_checks':checks,'analytic_event_fixtures':fixtures,'outside_B_rejected':outside}


def run_precision(repo,bits,archive_dir,pins,model,effort):
    begin=time.monotonic();e=ClosedJetEvaluator(repo,bits);ctx.prec=bits
    hhpath=repo/INV/'numerics/high_height_consumer/high_height_consumer.py'
    hh=load(hhpath,'s02_t2_complete_source_'+str(bits))
    ev=hh.bounded(lambda:hh.WholeCellEvaluator(bits),60)
    meta=hh.provenance(repo,model,effort,bits);meta['date']='2026-10-19'
    setup=hh.setup_record(ev,meta)
    hh.validate_setup(setup,repo)
    rel=Path('output')/('S02_T2_B_'+str(bits)+'_20261019.jsonl.gz')
    target=archive_dir/rel;target.parent.mkdir(parents=True,exist_ok=True)
    canonical=hashlib.sha256();slabs=[]
    header={'schema':SCHEMA,'kind':'cell_archive','date':'2026-10-19','bits':bits,
        'domain':{'t':['1/100','1/5'],'x':[999,1001]},'cover':[32,128],
        'source_sha256':pins,'bound_record_sha256':e.bound_sha,
        'derivative_semantics':{'frozen':'Local z derivatives hold center X fixed; diagonal defects are supplied. Not a coherent S03 residual.',
                                'full':'Coherent analytic correction and exact z jets for S03 residual consumers.'},
        'reference_setup':setup,'producer_sha256':digest(__file__),
        'reference_setup_scope':{'inherited_consumer_limit_512':'Original adaptive HH consumer only; not an enclose() API limit.',
                                 'new_fixed_cover_calls':4096,'setup_budget_unchanged':True}}
    with target.open('wb') as raw:
        with gzip.GzipFile(filename='',mode='wb',fileobj=raw,mtime=0) as gz:
            line=canonical_line(header);gz.write(line)
            # Canonical mathematical-content identity excludes observational
            # acquisition timing in the header, includes every cell row.
            for it in range(32):
                ta=F(1,100)+F(19,100)*it/32;tb=F(1,100)+F(19,100)*(it+1)/32
                slab=make_slab(it);slab['t']=[str(ta),str(tb)]
                for ix in range(128):
                    xa=F(999)+F(2)*ix/128;xb=F(999)+F(2)*(ix+1)/128
                    data,methods=e.enclose(ta,tb,xa,xb)
                    reference=source_cell(hh,ev,data,ta,tb,xa,xb)
                    update_slab(slab,methods,reference,xa,xb)
                    row={'cell':[it,ix],'t':[str(ta),str(tb)],'x':[str(xa),str(xb)],
                         'phase_and_normalizer':{k:data[k] for k in ['theta','omega','omega_x','b','b_x','chi']},
                         'methods':methods,'source_reference':reference}
                    line=canonical_line(row);gz.write(line);canonical.update(line)
                slabs.append(slab)
    summary={}
    for method in ['frozen','full']:
        rows=[slab['methods'][method] for slab in slabs]
        minima={key:min(row['minima'][key]['bound'] for row in rows) for key in rows[0]['minima']}
        maxima={key:max(row['maxima'][key] for row in rows) for key in rows[0]['maxima']}
        counts={key:sum(row[key] for row in rows) for key in rows[0] if key.endswith('_cells') or key=='cells'}
        summary[method]={'minima':minima,'maxima':maxima,'counts':counts}
    ref={'minimum_phase_radius':min(slab['source_minimum_radius'] for slab in slabs),
         'minimum_signed_excess_Gc2':min(slab['source_minimum_signed_excess_Gc2'] for slab in slabs),
         'maximum_phase_error':max(slab['source_maximum_phase_error'] for slab in slabs),
         'minimum_signed_excess_A2':min(slab['source_minimum_signed_excess_A2'] for slab in slabs),
         'setup_seconds':ev.setup_seconds,'setup_callbacks':ev.callbacks,
         'consumer_cell_calls':ev.calls,'all_closed_cells_covered':True}
    check(ref['minimum_phase_radius']>0 and ref['minimum_signed_excess_Gc2']>0,'fresh complete-source regression failed')
    archive={'relative_path':str(rel),'bits':bits,'stored_bytes':target.stat().st_size,'stored_sha256':digest(target),
             'canonical_jsonl_content_sha256':canonical.hexdigest(),'cells':4096,
             'canonical_content_scope':'Sorted-key canonical cell rows in fixed time/space order; header timings excluded; every evaluated jet/error/consumer included.',
             'regeneration':'same script, frozen inputs and bits; timings may change stored hash while cell-content identity is independent of those observations'}
    # Check exact rational seams/coverage implied by the fixed loops.
    check(slabs[0]['t'][0]=='1/100' and slabs[-1]['t'][1]=='1/5' and
          all(a['t'][1]==b['t'][0] for a,b in zip(slabs,slabs[1:])),'time coverage')
    checks=exact_checks(e)
    return serialize({'bits':bits,'eta':e.eta,'methods':summary,'source_reference':ref,'slabs':slabs,
        'archive':archive,'checks':checks,'seconds_including_reference_acquisition':time.monotonic()-begin})


def main():
    p=argparse.ArgumentParser();p.add_argument('--repo',type=Path,required=True)
    p.add_argument('--output',type=Path,required=True);p.add_argument('--archive-dir',type=Path,required=True)
    p.add_argument('--bits',type=int,nargs='+',default=[192,256])
    p.add_argument('--execution-model',required=True);p.add_argument('--execution-effort',required=True)
    args=p.parse_args();repo=args.repo.resolve();start=time.monotonic()
    paths=[repo/LANE/'numerics/check_cutoff_reflection.py',repo/LANE/'numerics/compare_correction_representations.py',
        repo/LANE/'numerics/S02_MATCHED_CORRECTION_20261019.json',
        repo/LANE/'notes/02_MATCHED_FROZEN_AND_ANALYTIC_CORRECTIONS_20261019.md',
        repo/INV/'numerics/high_height_consumer/high_height_consumer.py',
        repo/INV/'symmetries/notes/03_S02_COMPLETE_JET_EVALUATION_CONTRACT_20261019.md',
        repo/INV/'symmetries/03_normalized_jet_rotation/numerics/check_normalized_rotation.py',
        repo/INV/'symmetries/03_normalized_jet_rotation/numerics/S03_ROTATION_192_20261018.json',
        repo/INV/'symmetries/03_normalized_jet_rotation/numerics/S03_CORRELATED_RESIDUAL_192_20261018.json']
    pins={str(path.relative_to(repo)):digest(path) for path in paths}
    runs=[]
    for bits in args.bits:
        run=run_precision(repo,bits,args.archive_dir,pins,args.execution_model,args.execution_effort);runs.append(run)
        print(json.dumps({'bits':bits,'frozen':run['methods']['frozen'],'source_reference':run['source_reference']}),flush=True)
    report={'schema':SCHEMA,'date':'2026-10-19','timezone':'America/New_York','prepared_for':'Edward Baker',
        'actual_model':args.execution_model,'actual_effort':args.execution_effort,
        'llm_assistance':'substantial; internal research and separate same-model audits',
        'python':platform.python_version(),'python_flint':flint.__version__,
        'script_sha256':digest(__file__),'source_sha256':pins,
        'domain':{'t':['1/100','1/5'],'x':[999,1001]},'closed_cover':[32,128],
        'Schur_parameter_cover':[8,8,'gamma in [-1,1]'],
        'normalization':'J=(Q,-Qx/omega); Laguerre/excess divided by A²; reference excess explicitly Gc².',
        'primary_metric':'complete paid phase-first-jet radius and residual allowance; no matched-cost objective',
        'runs':runs,'status':'complete evaluation; classify gate from paid comparisons, not old-box pass count',
        'C_activated':False,'new_coverage':False,'new_Newman_bound':False,'performance_claim':False,
        'remaining_interface':'Full analytic family for S03; frozen local disk jets carry diagonal derivative defects.',
        'seconds':time.monotonic()-start}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({'status':'complete','output':str(args.output),'bytes':args.output.stat().st_size,'seconds':report['seconds']}))

if __name__=='__main__':main()
