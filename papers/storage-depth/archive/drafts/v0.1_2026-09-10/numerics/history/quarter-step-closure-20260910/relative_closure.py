"""Certify the continuation-residual inequality on every old input.

Uses full-output spatial matrices, a finite graph congruence, and an enlarged
cross block. No full-operator coercivity result is assumed in this test.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
from flint import arb as A,arb_mat as AM,ctx
import close_complement as z
c=z.c

def frobenius2(mat):return sum((x.abs_upper()**2 for x in mat.entries()),A(0)).upper()

def run(args):
    archive_path=Path(args.archive)
    with gzip.open(archive_path,'rt') as f:data=json.load(f)
    ctx.prec=data['precision_bits']
    for rel,digest in data['source_sha256'].items():
        assert hashlib.sha256((z.ROOT/rel).read_bytes()).hexdigest()==digest,rel
    no,nn=data['old_modes'],data['new_modes'];n=no+nn
    mats={name:AM([[c.unpack(x) for x in row] for row in mat]) for name,mat in data['matrices'].items()}
    H,Go,Gn=mats['head'],mats['gram_old'],mats['gram_new']
    previous=z.ROOT/'quarter-step-20260910/residual_128_32.json'
    proposal=json.loads(previous.read_text())
    assert no>=128 and nn>=32
    J=AM(nn,no)
    for i,row in enumerate(proposal['continuation_rational_coefficients']):
        for j,value in enumerate(row):J[i,j]=c.rat(value)
    T=c.ident(n)
    for i in range(nn):
        for j in range(no):T[no+i,j]=J[i,j]
    Ho=AM([[H[i,j] for j in range(n)] for i in range(no)])
    Hn=AM([[H[i,j] for j in range(n)] for i in range(no,n)])
    Eo=c.sym(T.transpose()*(Go-Ho.transpose()*Ho)*T)
    En=c.sym(T.transpose()*(Gn-Hn.transpose()*Hn)*T)
    MH=c.sym(T.transpose()*H*T)
    eta=c.unpack(data['eta']);leak_error=c.unpack(data['leakage_error'])
    tail=data['tail_bounds']
    go=A(tail['old_gamma_tail']).lower();gn=A(tail['new_gamma_tail']).lower()
    bg=A(tail['gamma_cross_norm_upper']).upper();rho=A(tail['arithmetic_norm_upper']).upper()
    L=A(7).log()+(A(8).log()-A(7).log())/4
    ba=sum((A(p).log()**2/k for k,p,_ in c.prime_powers(L)),A(0)).sqrt()
    attempts=[]
    for theta_string in args.theta:
        theta=c.rat(theta_string);assert 0<theta<1
        lam=(1/theta).sqrt()
        beta=((go+gn-((go-gn)**2+4*(lam*bg)**2).sqrt())/2-rho-(lam-1)*ba).lower()
        attempt={'theta':theta_string,'modified_complement_floor':beta.str(40)}
        if beta<=0:
            attempt['positive']=False;attempt['reason']='No positive modified complement floor'
            attempts.append(attempt);continue
        Do=AM([[A(1) if i==j and i<no else lam if i==j else A(0) for j in range(n)] for i in range(n)])
        Dn=AM([[lam if i==j and i<no else A(1) if i==j else A(0) for j in range(n)] for i in range(n)])
        E=c.sym(Do*Eo*Do+Dn*En*Dn)
        enlarged=AM([[MH[i,j]*(lam if (i<no)!=(j<no) else 1) for j in range(n)] for i in range(n)])
        # Each separate old/new leakage Gram has error <= leak_error.
        eerr=leak_error*(frobenius2(T*Do)+frobenius2(T*Dn))
        # Scaling off-diagonal blocks has norm at most 2*lambda times
        # the unscaled error. Frobenius bounds are deliberately conservative.
        herr=2*lam*eta*frobenius2(T)
        budget=(beta*herr+eerr).upper()
        test=c.sym(beta*enlarged-E-c.ident(n)*budget)
        checked=c.ldl(test)
        attempt.update({'positive':checked['positive'],'final_error_budget_upper':budget.str(35),'schur_check':checked})
        attempts.append(attempt)
        print('theta',theta_string,'tail',beta.str(15),'check',{k:v for k,v in checked.items() if k not in ['pivots','pivot_ball']},flush=True)
        if checked['positive']:break
    passed=next((a for a in attempts if a['positive']),None)
    record={'scope':'Full old-input residual inequality for the original 128-to-32 continuation, extended by zero to the old orthogonal complement. Spatial Gram and analytic-complement certificate; no new-depth global coercivity certificate assumed.',
            'old_verification_modes':no,'new_verification_modes':nn,'old_continuation_modes':128,'new_continuation_modes':32,
            'all_old_relative_residual_certificate_pass':passed is not None,
            'theta_upper':passed['theta'] if passed else None,
            'inequality':'R* F^-1 R <= theta H_J, hence S >= (1-theta) H_J on the full old form domain' if passed else None,
            'attempts':attempts,'matrix_archive':archive_path.name,'matrix_archive_sha256':hashlib.sha256(archive_path.read_bytes()).hexdigest(),
            'continuation_record_sha256':hashlib.sha256(previous.read_bytes()).hexdigest(),
            'source_sha256':{str(p.relative_to(z.ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in [Path(__file__).resolve(),Path(z.__file__)]}}
    Path(args.output).write_text(json.dumps(record,indent=2)+'\n')
    print('ALL-OLD RELATIVE CERTIFICATE',record['all_old_relative_residual_certificate_pass'],'theta',record['theta_upper'],flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--archive',required=True);p.add_argument('--output',required=True)
    p.add_argument('--theta',nargs='+',default=['0.9','0.95','0.99'])
    run(p.parse_args())
