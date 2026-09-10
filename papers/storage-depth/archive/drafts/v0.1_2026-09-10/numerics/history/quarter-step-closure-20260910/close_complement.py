"""Spatial head/complement certificate for the central quarter-step.

The head is piecewise polynomial. The complement has separate old/new
orthogonality conditions. Its analytic floor uses a joint arithmetic Schur
weight, local gamma tail floors, and the bounded gamma cross operator.
Complete output Grams retain the coupling to both infinite complements.
"""
import argparse
from fractions import Fraction
import gzip
import hashlib
import json
import math
from pathlib import Path
import sys
import time
from types import SimpleNamespace
from flint import arb as A, arb_mat as AM, arb_poly as P, ctx

ROOT=Path(__file__).resolve().parent.parent
sys.path.insert(0,str(ROOT/'quarter-step-20260910'))
import central_residual as r
import shifted_moments as sm
import arithmetic_bound as arith
c=r.c

def blockmat(aa,ba,bb):
    n,m=aa.nrows(),bb.nrows()
    return AM([[aa[i,j] if i<n and j<n else ba[i-n,j] if i>=n and j<n else ba[j-n,i] if i<n else bb[i-n,j-n]
                for j in range(n+m)] for i in range(n+m)])

def bstar_gamma(nn,a,h,M,g):
    ratio=h/a
    phis=[r.ex.legendre(i,A(0),A(1),A(1)) for i in range(nn)]
    z=P([-1/ratio,1/ratio])
    cont=[p(z) for p in phis]
    div=[]
    for i,phi in enumerate(phis):
        hz=P([sum((phi[k]/(k-j) for k in range(j+1,i+1)),A(0)) for j in range(i)])
        div.append(hz(z))
    moments=AM(nn,M)
    for i in range(nn):
        value=Fraction(math.factorial(i)**2,math.factorial(2*i+1))
        for k in range(i,M):
            if k>i:value*=Fraction(k*k,(k-i)*(k+i+1))
            moments[i,k]=A(2*i+1).sqrt()*c.rat(value)
    H=AM(M,M)
    for k in range(M):
        for j in range(M-k):
            H[k,j]=-c.rat(g[j+k+1])*math.comb(j+k,j)*a**j*h**k/2
    smooth=[p(P([1,-1])) for p in r.rows((a*h).sqrt()*moments*H)]
    poly=[smooth[i]-div[i]*(1/(2*ratio.sqrt())) for i in range(nn)]
    right=[p*(1/(2*ratio.sqrt())) for p in cont]
    outer=[-p for p in right]
    return r.matrix(poly),r.matrix(right),r.matrix(outer)

class OldOutput:
    def __init__(self,no,nn,a,h,M,g):
        self.no,self.nn,self.a,self.h=no,nn,a,h
        self.ap,self.al=r.gamma_output(no,a,M,g)
        self.bp,self.br,self.bo=bstar_gamma(nn,a,h,M,g)
        self.maxmom=2*(no+nn+M)+1
        self.ext=sm.exterior(self.maxmom,1+h/a)
        self.cache={}
        self.log1square=[]
        hn,hn2=A(0),A(0)
        for k in range(self.maxmom):
            hn+=A(1)/(k+1);hn2+=A(1)/(k+1)**2
            self.log1square.append((hn*hn+hn2)/(k+1))
        self.at=[];self.bt=[]
        for n,p,_ in c.prime_powers(a,7):
            d=A(n).log()/a;alpha=-A(p).log()/A(n).sqrt()
            self.at.append(((0,Fraction(n)),(0,Fraction(7)),r.matrix([alpha*r.ex.legendre(i,-d,A(1),A(1)) for i in range(no)])))
            self.at.append(((0,Fraction(1)),(0,Fraction(7,n)),r.matrix([alpha*r.ex.legendre(i,d,A(1),A(1)) for i in range(no)])))
        for n,p,_ in c.prime_powers(a+h,8):
            d=A(0) if n==7 else (A(n).log()-a)/h
            alpha=-A(p).log()/A(n).sqrt()*(a/h).sqrt()
            self.bt.append(((0,Fraction(7,n)),(1,Fraction(7,n)),r.matrix([alpha*r.ex.legendre(i,d,a/h,A(1)) for i in range(nn)])))

    def pos(self,key):
        hs,q=key
        return (hs*self.h+c.rat(q).log())/self.a

    def less(self,x,y):
        if x==y:return False
        xx,yy=self.pos(x),self.pos(y)
        assert xx<yy or yy<xx
        return xx<yy

    def intersection(self,a,b,c0,d):
        lo=c0 if self.less(a,c0) else a
        hi=b if self.less(b,d) else d
        return (lo,hi) if self.less(lo,hi) else None

    def moment(self,n,m,kind,lo=(0,Fraction(1)),hi=(0,Fraction(7))):
        key=(kind,lo,hi)
        if key not in self.cache:
            ll,hh=self.pos(lo),self.pos(hi)
            if lo==(0,Fraction(1)):ll=A(0)
            if hi==(0,Fraction(7)):hh=A(1)
            if kind=='plain':v=sm.plain(self.maxmom,ll,hh)
            elif kind=='left':v=sm.left(self.maxmom,ll,hh)
            elif kind=='right':v=sm.minus(self.maxmom,A(1),ll,hh)
            elif kind=='outer':v=sm.minus(self.maxmom,1+self.h/self.a,ll,hh)
            else:raise ValueError(kind)
            self.cache[key]=v
        return sm.hankel(self.cache[key],n,m)

    def inner(self,x,y,kind='plain',window=None):
        args=window if window else ()
        return x*self.moment(x.ncols(),y.ncols(),kind,*args)*y.transpose()

    def special(self,x,y,kind):
        if kind=='right2':vals=self.log1square
        elif kind in self.ext:vals=self.ext[kind]
        elif kind=='leftright':return x*c.moment(x.ncols(),y.ncols(),'loglog')*y.transpose()
        else:raise ValueError(kind)
        return x*sm.hankel(vals,x.ncols(),y.ncols())*y.transpose()

    def build(self):
        ap,al,bp,br,bo=self.ap,self.al,self.bp,self.br,self.bo
        # Gamma/gamma pieces. Both endpoint-log coefficients of A are al.
        cross=self.inner(ap,bp)+self.inner(al,bp,'left')+self.inner(al,bp,'right')
        cross+=self.inner(ap,br,'right')+self.special(al,br,'leftright')+self.special(al,br,'right2')
        cross+=self.inner(ap,bo,'outer')+self.special(al,bo,'left_outer')+self.special(al,bo,'right_outer')
        bb=self.inner(bp,bp)+self.special(br,br,'right2')+self.special(bo,bo,'outer2')
        q=self.inner(bp,br,'right')+self.inner(bp,bo,'outer')+self.special(br,bo,'right_outer')
        bb+=q+q.transpose()
        print('Exterior-log gamma Grams built',flush=True)
        for lo,hi,at in self.at:
            cross+=self.inner(at,bp,window=(lo,hi))+self.inner(at,br,'right',(lo,hi))+self.inner(at,bo,'outer',(lo,hi))
        for lo,hi,bt in self.bt:
            cross+=self.inner(ap,bt,window=(lo,hi))+self.inner(al,bt,'left',(lo,hi))+self.inner(al,bt,'right',(lo,hi))
            z=self.inner(bp,bt,window=(lo,hi))+self.inner(br,bt,'right',(lo,hi))+self.inner(bo,bt,'outer',(lo,hi))
            bb+=z+z.transpose()
            for alo,ahi,at in self.at:
                window=self.intersection(lo,hi,alo,ahi)
                if window:cross+=self.inner(at,bt,window=window)
        # The five translated source windows are disjoint.
        for i,(lo,hi,_) in enumerate(self.bt):
            for j,(lo2,hi2,_) in enumerate(self.bt):
                if i<j:assert self.intersection(lo,hi,lo2,hi2) is None
        alpha2=sum((A(p).log()**2/n for n,p,_ in c.prime_powers(self.a+self.h,8)),A(0))
        bb+=c.ident(self.nn)*alpha2
        return cross,c.sym(bb)

def tail_floor(a,h,no,nn,M,g,rho):
    def gamma_floor(L,N):
        b=c.analytic(L,g,N,[],None)
        return b['tail_floor']
    L=a+h
    deriv=sum(((j-1)*abs(c.rat(g[j]))*L**(j-2) for j in range(2,M+1)),A(0))
    ratio=L/3
    deriv+=A(256)/9*ratio**(M-1)*(M/(1-ratio)+ratio/(1-ratio)**2)
    smooth_cross=deriv*a*(a*h).sqrt()/(4*A(no*(no+1)).sqrt())
    cross=A.pi()/2+smooth_cross
    old,new=gamma_floor(a,no),gamma_floor(h,nn)
    beta=(old+new-((old-new)**2+4*cross**2).sqrt())/2-rho
    return beta.lower(),{'old_gamma_tail':old.str(35),'new_gamma_tail':new.str(35),'gamma_cross_norm_upper':cross.upper().str(35),'smooth_cross_norm_upper':smooth_cross.upper().str(35),'arithmetic_norm_upper':rho.str(35),'joint_tail_floor':beta.lower().str(35)}

def run(args):
    if not __debug__:raise RuntimeError('Assertions must remain enabled')
    start=time.monotonic();ctx.prec=args.bits
    a=A(7).log();h=(A(8).log()-a)/4;L=a+h
    no,nn,M=args.old,args.new,args.degree
    g=c.profile(M)
    # Rebuild the weighted arithmetic bound, including all ball checks.
    arithmetic=arith.build(args.cells)
    ctx.prec=args.bits
    rho=A(arithmetic['norm_upper']).upper()
    beta,tail=tail_floor(a,h,no,nn,M,g,rho)
    print('Analytic spatial complement',json.dumps(tail),flush=True)
    assert beta>0
    out=Path(args.output);out.parent.mkdir(parents=True,exist_ok=True)
    cache=out.parent/f'old_{no}_{M}_{args.bits}.json.gz'
    if cache.exists():
        with gzip.open(cache,'rt') as f:data=json.load(f)
        assert data['builder_source_sha256']==hashlib.sha256(Path(c.__file__).read_bytes()).hexdigest()
        print('Loaded old-depth output matrices',flush=True)
    else:
        data=c.build(SimpleNamespace(N=no,M=M,horizon=None,log_horizon=7))
        with gzip.open(cache,'wt') as f:json.dump(data,f)
    mats={name:AM([[c.unpack(x) for x in row] for row in mat]) for name,mat in data['matrices'].items()}
    Ao=mats['Q'];oldgram=mats['E_central']+Ao*Ao
    F=r.cg.gamma_head(nn,h,M,g);B,*_=r.cg.cross(no,nn,a,h,M,g)
    head=blockmat(Ao,B,F)
    print('Spatial head assembled; building old output cross Gram',flush=True)
    oldout=OldOutput(no,nn,a,h,M,g)
    cross,bb=oldout.build()
    gramold=blockmat(oldgram,cross.transpose(),bb)
    print('Old-interval full output Gram complete',flush=True)
    bp,bl,be=r.cross_output(no,a,h,M,g,args.log_degree)
    fp,fl=r.gamma_output(nn,h,M,g)
    k=max(bp.ncols(),fp.ncols());kl=max(bl.ncols(),fl.ncols())
    poly=AM(r.pad(bp,k).tolist()+r.pad(fp,k).tolist())
    left=AM(r.pad(bl,kl).tolist()+r.pad(fl,kl).tolist())
    right=AM(AM(no,nn).tolist()+fl.tolist())
    gramnew=r.gram(poly,left,right)
    gram=c.sym(gramold+gramnew)
    eta=r.eta(L,M)
    # cross_output includes eta(L,M) plus its log-series approximation;
    # adding eta again is a safe budget for the full model operator.
    error=(eta+be).upper()
    headnorm=sum((head[i,j]**2 for i in range(no+nn) for j in range(no+nn)),A(0)).sqrt()
    outnorm=sum((gram[i,i] for i in range(no+nn)),A(0)).sqrt()
    leakage=gram-head*head
    leakage_error=2*error*outnorm+error**2+2*eta*headnorm+eta**2
    archive_path=out.with_suffix('.matrices.json.gz')
    archive={'old_modes':no,'new_modes':nn,'profile_degree':M,'log_series_degree':args.log_degree,'precision_bits':args.bits,
             'tail_bounds':tail,'eta':c.pack(eta),'output_error':c.pack(error),'leakage_error':c.pack(leakage_error),
             'matrices':{name:[[c.pack(mat[i,j]) for j in range(no+nn)] for i in range(no+nn)] for name,mat in [('head',head),('gram_old',gramold),('gram_new',gramnew)]},
             'source_sha256':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in [Path(__file__).resolve(),Path(sm.__file__),Path(arith.__file__),Path(r.__file__),Path(c.__file__),Path(r.cg.__file__),Path(r.ex.__file__)]}}
    with gzip.open(archive_path,'wt') as f:json.dump(archive,f)
    m=c.rat(args.floor)
    assert beta>m>0
    budget=(beta-m)*eta+leakage_error
    test=c.sym((head-c.ident(no+nn)*m)*(beta-m)-leakage-c.ident(no+nn)*budget.upper())
    result=c.ldl(test)
    lifted=None
    if result['positive'] and no==128 and nn==32:
        # Extend the previously certified continuation by zero on the old
        # orthogonal complement. This yields a strict all-old residual factor.
        previous=ROOT/'quarter-step-20260910/residual_128_32.json'
        proposal=json.loads(previous.read_text())
        J=AM([[c.rat(s) for s in row] for row in proposal['continuation_rational_coefficients']])
        T=AM(c.ident(no).tolist()+J.tolist())
        rg=T.transpose()*gramnew*T
        j2=sum((J[i,j]**2 for i in range(nn) for j in range(no)),A(0))
        rn=sum((rg[i,i] for i in range(no)),A(0)).sqrt()+error*(1+j2).sqrt()
        smooth=c.analytic(L,g,no,c.prime_powers(L),None)['smooth_variation']
        b=A.pi()/2+smooth*(a*h).sqrt()/2+sum((A(p).log()**2/n for n,p,_ in c.prime_powers(L)),A(0)).sqrt()
        f0=r.row_floor(h,M,g)
        penalty=(rn**2+b*b)/f0
        epsilon=(m/(m+penalty)).lower()
        assert epsilon>0
        lifted={'scope':'All old inputs, with J equal to the earlier 128-to-32 continuation on the head and zero on its orthogonal complement.',
                'head_residual_norm_upper':rn.upper().str(35),'full_residual_penalty_norm_upper':penalty.upper().str(35),
                'relative_candidate_slack_lower':epsilon.str(40),'inequality':'R* F^-1 R <= (1-epsilon) H_J; S >= epsilon H_J',
                'continuation_record_sha256':hashlib.sha256(previous.read_bytes()).hexdigest()}
    record={'scope':'Full central operator at the quarter-step via a spatial head and the joint old/new complement; no new-depth global polynomial certificate used.',
            'old_modes':no,'new_modes':nn,'profile_degree':M,'log_series_degree':args.log_degree,'precision_bits':args.bits,
            'requested_full_coercivity':args.floor,'tail_bounds':tail,'full_output_operator_error_upper':error.str(35),
            'leakage_error_upper':leakage_error.upper().str(35),'final_schur_error_upper':budget.upper().str(35),
            'full_output_norm_upper':outnorm.upper().str(35),'full_operator_certificate_pass':result['positive'],
            'matrix_archive':archive_path.name,'matrix_archive_sha256':hashlib.sha256(archive_path.read_bytes()).hexdigest(),
            'full_old_residual_corollary':lifted,
            'schur_check':result,'arithmetic_weight':arithmetic,'seconds':time.monotonic()-start,
            'source_sha256':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in [Path(__file__).resolve(),Path(sm.__file__),Path(arith.__file__),Path(r.__file__),Path(c.__file__),Path(r.cg.__file__),Path(r.ex.__file__)]}}
    out.write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps({k:v for k,v in record.items() if k not in ['arithmetic_weight','source_sha256','schur_check']},indent=2),flush=True)
    print('Schur check', {k:v for k,v in result.items() if k not in ['pivots','pivot_ball']},flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--old',type=int,default=128);p.add_argument('--new',type=int,default=32)
    p.add_argument('--degree',type=int,default=320);p.add_argument('--log-degree',type=int,default=100)
    p.add_argument('--bits',type=int,default=6144);p.add_argument('--cells',type=int,default=512)
    p.add_argument('--floor',default='1e-33');p.add_argument('--output',required=True)
    run(p.parse_args())
