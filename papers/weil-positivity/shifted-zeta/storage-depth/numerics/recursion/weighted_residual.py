"""Interval-specific tail bounds for the full-domain residual certificate.

Positive rational weights distribute the analytic comparison matrix across
individual tails. Failed guarded tests propose new weights, never proof
premises. All successful tests use complete saved output Grams and Arb LDL.
"""
import argparse
import json
from pathlib import Path
import mpmath as mp
from flint import ctx
from common import *
import archive

def probe(mat):
    """Sign test plus a diagnostic failing-direction proposal."""
    n=mat.nrows();low=[[A(0) for _ in range(n)] for _ in range(n)];piv=[]
    for i in range(n):
        v=mat[i,i]
        for k in range(i):v-=low[i][k]*low[i][k]*piv[k]
        if not v.is_finite():return {'positive':False,'reason':'Non-finite pivot','failed_pivot':i},None
        if not v>0:
            x=[A(0) for _ in range(n)];x[i]=A(1)
            for j in range(i-1,-1,-1):x[j]=-sum((low[k][j]*x[k] for k in range(j+1,i+1)),A(0))
            scale=max(t.abs_upper() for t in x)
            x=AM([[rat(mp.nstr(residual.ex.mid(t/scale),60))] for t in x])
            return {'positive':False,'failed_pivot':i,'pivot':v.str(40)},x
        piv.append(v)
        for j in range(i+1,n):
            w=mat[j,i]
            for k in range(i):w-=low[j][k]*low[i][k]*piv[k]
            low[j][i]=w/v
    return {'positive':True,'positive_pivot_count':n,
            'minimum_pivot_lower':min(x.lower() for x in piv).str(40)},None

def run(args):
    assert __debug__
    data,build,path=archive.load(args.record);ctx.prec=args.bits;mp.mp.dps=90
    generating_sources=source_hashes()
    previous=json.loads(Path(args.comparison).read_text())
    assert previous['matrix_archive_sha256']==build['matrix_archive_sha256']
    assert previous['continuation_record_sha256']==legacy_io.file_hash(args.continuation)
    metric=next(x for x in previous['metric_comparisons'] if x['check']['positive'])
    proposal=json.loads(Path(args.continuation).read_text())
    assert proposal['matrix_archive_sha256']==build['matrix_archive_sha256']
    J=AM([[rat(s) for s in row] for row in proposal['continuation_rational_coefficients']])
    unpack=lambda mat:AM([[c.unpack(x) for x in row] for row in mat])
    H=unpack(data['matrices']['head']);N=H.nrows();nn=J.nrows();no=J.ncols()
    assert no+nn==N
    T=ident(N)
    for i in range(nn):
        for j in range(no):T[no+i,j]=J[i,j]
    MH=c.sym(T.transpose()*H*T)
    eta=c.unpack(data['eta']);err=c.unpack(data['leakage_error'])
    gamma=unpack(data['tail_bounds']['gamma_comparison'])
    rho=A(data['tail_bounds']['arithmetic']['norm_upper']).upper()
    ba=A(previous['arithmetic_cross_norm_upper']).upper()
    f0=A(previous['full_new_slab_floor']).lower();assert f0>0
    offsets=[0]
    for modes in data['modes']:offsets.append(offsets[-1]+modes)
    E=[]
    for i in range(len(data['modes'])):
        G=unpack(data['matrices'][f'gram_{i}'])
        row=sub(H,range(offsets[i],offsets[i+1]),range(N))
        E.append(c.sym(T.transpose()*(G-row.transpose()*row)*T))
    attempts=[];successful=None
    for theta_text in args.theta:
        theta=rat(theta_text);assert 0<theta<1;lam=(1/theta).sqrt()
        gm=AM(gamma.tolist());k=gm.nrows()-1
        for i in range(k):gm[i,k]=gm[k,i]=gm[i,k]*lam
        gm-=ident(k+1)*(rho+(lam-1)*ba)
        Do=AM([[1 if i==j and i<no else lam if i==j else 0 for j in range(N)] for i in range(N)])
        Dn=AM([[lam if i==j and i<no else 1 if i==j else 0 for j in range(N)] for i in range(N)])
        Ds=[Do]*k+[Dn]
        ES=[c.sym(d*e*d) for d,e in zip(Ds,E)]
        error_factors=[frob2(T*d) for d in Ds]
        enlarged=AM([[MH[i,j]*(lam if (i<no)!=(j<no) else 1) for j in range(N)] for i in range(N)])
        strings=list(args.weights)
        for trial in range(args.attempts):
            w=[rat(s) for s in strings];assert len(w)==k+1 and all(v>0 for v in w)
            beta=[(gm[i,i].lower()-sum(((-gm[i,j]).upper()*w[j]/w[i] for j in range(k+1) if j!=i),A(0))).lower() for i in range(k+1)]
            item={'theta':theta_text,'weights':strings,'tail_floors':[v.str(45) for v in beta]}
            if not all(v>0 for v in beta):
                item['check']={'positive':False,'reason':'Nonpositive weighted tail floor'}
                attempts.append(item);break
            budget=(2*lam*eta*frob2(T)+sum((err*f/b for f,b in zip(error_factors,beta)),A(0))).upper()
            test=c.sym(enlarged-sum((e/b for e,b in zip(ES,beta)),AM(N,N))-ident(N)*budget)
            check,x=probe(test);item.update({'error_budget_upper':budget.str(45),'check':check})
            attempts.append(item)
            print('theta',theta_text,'weights',strings,'tails',[v.str(10) for v in beta],check,flush=True)
            if check['positive']:successful=item;break
            if x is None:break
            r=[]
            for e in ES:
                value=residual.ex.mid((x.transpose()*e*x)[0,0])
                r.append(mp.sqrt(max(value,mp.mpf('1e-100'))))
            # A small regularizer prevents an almost absent residual
            # component from demanding a vanishing tail floor.
            scale=max(r);rhs=AM([[rat(mp.nstr(v+scale*mp.mpf('.02'),60))] for v in r])
            proposed=gm.solve(rhs)
            if not all(v>0 for v in proposed.entries()):break
            fresh=[residual.ex.mid(proposed[i,0]/proposed[0,0]) for i in range(k+1)]
            strings=['1']+[mp.nstr((mp.mpf(strings[i])+fresh[i])/2,16) for i in range(1,k+1)]
        if successful:break
    induction=None
    if successful:
        old_record=json.loads((HISTORY/'quarter-step-closure-20260910/closure_256_32.json').read_text())
        assert old_record['full_operator_certificate_pass']
        oldfloor=rat(old_record['requested_full_coercivity']);mu=rat(metric['mu'])
        theta=rat(successful['theta']);q=frob2(J).sqrt();tau=((q*q+4).sqrt()+q)/2
        carried=((1-theta.sqrt())*min((mu*oldfloor).lower(),f0)/(tau*tau)).lower()
        assert carried>0
        L=sum((LogPoint.read(x) for x in data['partition']),ZERO)
        change=c.analytic(L.value(),c.profile(data['profile_degree']),no,active_powers(L),None)['generator_change_constant'].upper()
        exponent=int(mp.floor(mp.log10(residual.ex.mid((carried/(4*change)).sqrt()))))
        shift=f'1e{exponent}';omega=rat(shift)
        assert change*omega*omega<carried/2
        induction={'mu':metric['mu'],'theta':successful['theta'],'old_floor':old_record['requested_full_coercivity'],
                   'retained_old_fraction':((1-theta)*mu).lower().str(45),
                   'graph_norm_squared_upper':(tau*tau).upper().str(45),
                   'recursive_new_floor_lower':carried.str(45),'safe_shift_upper':shift,
                   'generator_change_constant_upper':change.str(45),
                   'change_at_shift_upper':(change*omega*omega).upper().str(45),
                   'old_certificate_sha256':legacy_io.file_hash(HISTORY/'quarter-step-closure-20260910/closure_256_32.json')}
    out={'scope':'Full old-domain residual inequality via separate analytic tail floors, without assuming new-depth positivity.',
         'precision_bits':args.bits,'all_old_residual_certificate_pass':successful is not None,
         'attempts':attempts,'induction_data':induction,
         'matrix_archive_sha256':build['matrix_archive_sha256'],'matrices_content_sha256':build['matrices_content_sha256'],
         'comparison_record_sha256':legacy_io.file_hash(args.comparison),
         'continuation_record_sha256':legacy_io.file_hash(args.continuation),
         'source_sha256':generating_sources}
    assert source_hashes()==generating_sources
    Path(args.output).write_text(json.dumps(out,indent=2)+'\n')

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--record',required=True)
    p.add_argument('--comparison',required=True);p.add_argument('--continuation',required=True)
    p.add_argument('--output',required=True);p.add_argument('--bits',type=int,default=1024)
    p.add_argument('--theta',nargs='+',default=['0.99'])
    p.add_argument('--weights',nargs='+',default=['1','0.6','0.38'])
    p.add_argument('--attempts',type=int,default=10)
    run(p.parse_args())
