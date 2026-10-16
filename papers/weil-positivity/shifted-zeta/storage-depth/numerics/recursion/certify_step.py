"""Replay absolute positivity, then test old-energy and residual comparisons.

Every test uses the full old domain and unrestricted new complement.
Failure of a sufficient guarded test does not prove operator negativity.
"""
import argparse
import json
import time
from pathlib import Path
import mpmath as mp
from flint import ctx
from common import *
import archive
import tails

def brief(result):
    out={k:v for k,v in result.items() if k not in ['pivots','pivot_ball']}
    if 'pivots' in result:out['positive_pivot_count']=len(result['pivots'])
    return out

def run(args):
    assert __debug__
    start=time.monotonic();data,record,path=archive.load(args.record)
    ctx.prec=args.bits;mp.mp.dps=120
    unpack=lambda mat:AM([[c.unpack(x) for x in row] for row in mat])
    H=unpack(data['matrices']['head']);N=H.nrows()
    nn=data['modes'][-1];no=N-nn
    allgrams=[unpack(data['matrices'][f'gram_{i}']) for i in range(len(data['modes']))]
    Go=sum(allgrams[:-1],AM(N,N));Gn=allgrams[-1]
    eta=c.unpack(data['eta']);e=c.unpack(data['leakage_error'])
    beta=A(data['tail_bounds']['joint_tail_floor']).lower()
    floor=rat(record['requested_full_coercivity'])
    assert beta>floor>0
    E=c.sym(Go+Gn-H*H)
    absolute=ldl(c.sym((H-ident(N)*floor)*(beta-floor)-E-ident(N)*((beta-floor)*eta+e).upper()))
    print('Absolute replay',brief(absolute),flush=True)
    Ao=sub(H,range(no),range(no));F=sub(H,range(no,N),range(no,N));B=sub(H,range(no,N),range(no))
    if args.continuation:
        prior=json.loads(Path(args.continuation).read_text())
        assert prior['matrix_archive_sha256']==record['matrix_archive_sha256']
        strings=prior['continuation_rational_coefficients']
        J=AM([[rat(s) for s in row] for row in strings])
        assert J.nrows()==nn and J.ncols()==no
    else:
        J,strings=residual.rational_matrix(-F.solve(B),80)
    T=ident(N)
    for i in range(nn):
        for j in range(no):T[no+i,j]=J[i,j]
    To=sub(T,range(N),range(no))
    Ho=sub(H,range(no),range(N));Hn=sub(H,range(no,N),range(N))
    Eo=c.sym(Go-Ho.transpose()*Ho);En=c.sym(Gn-Hn.transpose()*Hn)
    MH=c.sym(T.transpose()*H*T)
    HJ=sub(MH,range(no),range(no))
    gamma=unpack(data['tail_bounds']['gamma_comparison'])
    rho=A(data['tail_bounds']['arithmetic']['norm_upper']).upper()
    gammaold=sub(gamma,range(gamma.nrows()-1),range(gamma.nrows()-1))
    betaA=tails.eigen_floor(gammaold-ident(gammaold.nrows())*rho)
    comparisons=[]
    for mu_text in args.mu:
        mu=rat(mu_text);assert 0<mu<1
        U=AM(To.tolist())
        for i in range(no):U[i,i]=1-mu
        bm=((1-mu)*betaA).lower()
        budget=(bm*eta*(frob2(To)+mu)+e*frob2(U)).upper()
        check=ldl(c.sym(bm*(HJ-mu*Ao)-U.transpose()*Eo*U-ident(no)*budget))
        comparisons.append({'mu':mu_text,'tail_floor':bm.str(45),'error_budget':budget.str(45),'check':brief(check)})
        print('Metric',mu_text,brief(check),flush=True)
        if check['positive']:break
    # A universally valid arithmetic cross estimate. If the old source
    # windows are disjoint, orthogonality improves sum(alpha) to sqrt(sum(alpha^2)).
    lengths=[LogPoint.read(x) for x in data['partition']]
    oldlength=sum(lengths[:-1],ZERO);L=oldlength+lengths[-1]
    f0=residual.row_floor(lengths[-1].value(),data['profile_degree'],c.profile(data['profile_degree']))
    assert f0>0
    windows=[]
    alpha=[]
    for n,p,_ in active_powers(L):
        lo=max(ZERO,oldlength-logn(n));hi=min(oldlength,L-logn(n))
        if lo<hi:windows.append((lo,hi));alpha.append(A(p).log()/A(n).sqrt())
    disjoint=all(not (max(a,c0)<min(b,d)) for i,(a,b) in enumerate(windows) for c0,d in windows[i+1:])
    ba=sum((x*x for x in alpha),A(0)).sqrt() if disjoint else sum(alpha,A(0))
    residuals=[]
    Eot=c.sym(T.transpose()*Eo*T);Ent=c.sym(T.transpose()*En*T)
    for theta_text in args.theta:
        theta=rat(theta_text);assert 0<theta<1
        lam=(1/theta).sqrt()
        gm=AM(gamma.tolist());k=gm.nrows()-1
        for i in range(k):gm[i,k]=gm[k,i]=gm[i,k]*lam
        bt=tails.eigen_floor(gm-ident(k+1)*(rho+(lam-1)*ba))
        attempt={'theta':theta_text,'tail_floor':bt.str(45)}
        if not bt>0:
            attempt['check']={'positive':False,'reason':'No positive modified complement floor'}
        else:
            Do=AM([[1 if i==j and i<no else lam if i==j else 0 for j in range(N)] for i in range(N)])
            Dn=AM([[lam if i==j and i<no else 1 if i==j else 0 for j in range(N)] for i in range(N)])
            enlarged=AM([[MH[i,j]*(lam if (i<no)!=(j<no) else 1) for j in range(N)] for i in range(N)])
            leakage=c.sym(Do*Eot*Do+Dn*Ent*Dn)
            budget=(bt*2*lam*eta*frob2(T)+e*(frob2(T*Do)+frob2(T*Dn))).upper()
            attempt['error_budget']=budget.str(45)
            attempt['check']=ldl(c.sym(bt*enlarged-leakage-ident(N)*budget))
        attempt['check']=brief(attempt['check'])
        residuals.append(attempt)
        print('Residual',theta_text,brief(attempt['check']),flush=True)
        if attempt['check']['positive']:break
    induction=None
    metric=next((x for x in comparisons if x['check']['positive']),None)
    relative=next((x for x in residuals if x['check']['positive']),None)
    carried=None
    if metric and relative:
        old_record=json.loads((HISTORY/'quarter-step-closure-20260910/closure_256_32.json').read_text())
        assert old_record['full_operator_certificate_pass']
        oldfloor=rat(old_record['requested_full_coercivity'])
        mu=rat(metric['mu']);theta=rat(relative['theta']);q=frob2(J).sqrt()
        tau=((q*q+4).sqrt()+q)/2
        carried=((1-theta.sqrt())*min((mu*oldfloor).lower(),f0)/tau**2).lower()
        assert carried>0
        induction={'mu':metric['mu'],'theta':relative['theta'],
                   'retained_old_fraction':((1-theta)*mu).lower().str(45),
                   'old_floor':old_record['requested_full_coercivity'],
                   'graph_norm_squared_upper':(tau*tau).upper().str(45),
                   'recursive_new_floor_lower':carried.str(45),
                   'old_certificate_sha256':legacy_io.file_hash(HISTORY/'quarter-step-closure-20260910/closure_256_32.json')}
    shifts=None
    available=floor if absolute['positive'] else carried
    if available is not None:
        gg=c.profile(data['profile_degree'])
        change=c.analytic(L.value(),gg,no,active_powers(L),None)['generator_change_constant'].upper()
        omega_text=args.shift;omega=rat(omega_text)
        if not change*omega**2<available/2:
            exponent=int(mp.floor(mp.log10(residual.ex.mid((available/(4*change)).sqrt()))))
            omega_text=f'1e{exponent}';omega=rat(omega_text)
        assert 0<omega<=rat('0.5') and change*omega**2<available/2
        shifts={'shift_upper':omega_text,'generator_change_constant_upper':change.str(45),
                'change_at_shift_upper':(change*omega**2).upper().str(45),
                'central_floor_lower':available.str(45),'pass':True}
    proposal_path=Path(args.proposal_output) if args.proposal_output else Path(args.output).with_suffix('.continuation.json')
    if args.continuation:proposal_path=Path(args.continuation)
    else:
        proposal={'scope':'Exact rational Galerkin continuation, zero on the omitted old modes.',
                  'modes':data['modes'],'decimal_digits':80,'continuation_rational_coefficients':strings,
                  'matrix_archive_sha256':record['matrix_archive_sha256']}
        proposal_path.write_text(json.dumps(proposal,separators=(',',':'))+'\n')
        assert proposal_path.stat().st_size<1048576
    out={'scope':'Full-domain three-interval sign replays and continuation comparisons in the working normalization.',
         'precision_bits':args.bits,'modes':data['modes'],'absolute_check':brief(absolute),
         'metric_comparisons':comparisons,'residual_comparisons':residuals,
         'continuation_record':proposal_path.name,'continuation_record_sha256':legacy_io.file_hash(proposal_path),
         'J_frobenius_squared_upper':frob2(J).str(45),
         'arithmetic_cross_disjoint_windows':disjoint,'arithmetic_cross_norm_upper':ba.upper().str(45),
         'full_new_slab_floor':f0.str(45),
         'induction_data':induction,
         'positive_shift_consequence':shifts,'matrix_archive_sha256':record['matrix_archive_sha256'],
         'matrices_content_sha256':record['matrices_content_sha256'],
         'build_record_sha256':legacy_io.file_hash(args.record),
         'source_sha256':source_hashes(),'seconds':time.monotonic()-start}
    Path(args.output).write_text(json.dumps(out,indent=2)+'\n')

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--record',required=True);p.add_argument('--output',required=True)
    p.add_argument('--bits',type=int,default=2048);p.add_argument('--continuation')
    p.add_argument('--proposal-output')
    p.add_argument('--mu',nargs='+',default=['1e-7','1e-8','1e-9'])
    p.add_argument('--theta',nargs='+',default=['0.9','0.95','0.99'])
    p.add_argument('--shift',default='1e-19')
    run(p.parse_args())
