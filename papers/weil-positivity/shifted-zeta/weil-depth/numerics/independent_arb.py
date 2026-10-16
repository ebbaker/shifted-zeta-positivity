"""Independent reconstruction of the printed v0.1 Weil certificate.

No original numerical supplement or matrices were available for this review.
Only python-flint and the standard library enter certification. NumPy/mpmath
are not imported here. All comparisons that decide positivity use real balls.
"""
import argparse
from fractions import Fraction
from math import comb, factorial
import gzip
import hashlib
import json
from pathlib import Path
import time
import sys
import flint
from flint import arb, arb_mat, ctx


def ball(q):
    if isinstance(q, Fraction):
        return arb(q.numerator) / q.denominator
    return arb(q)


def profile(M):
    """Rational inversion of sinh(t)/t and direct multiplication."""
    sh = [Fraction(1, factorial(j+1)) if j % 2 == 0 else Fraction(0)
          for j in range(M+1)]
    inv = [Fraction(1)]
    for j in range(1, M+1):
        inv.append(-sum(sh[k]*inv[j-k] for k in range(1, j+1)))
    e = [Fraction(1, 2**j*factorial(j)) for j in range(M+1)]
    g = [sum(e[k]*inv[j-k] for k in range(j+1)) for j in range(M+1)]
    for j in range(1, M+1, 2):
        g[j] -= Fraction(4, 2**(j-1)*factorial(j-1))
    if g[:3] != [Fraction(1), Fraction(-7, 2), Fraction(-1, 24)]:
        raise ArithmeticError('Profile control failed')
    return g


def prime_base(n):
    for p in range(2, n+1):
        if n % p == 0:
            k = n
            while k % p == 0:
                k //= p
            return p if k == 1 else None


def active(n, L, log_endpoint):
    if log_endpoint is not None:
        return n < log_endpoint
    v = arb(n).log()
    if v < L:
        return True
    if v >= L:
        return False
    raise ArithmeticError('Unresolved arithmetic threshold')


def path_size(n, L, log_endpoint):
    q = 1
    while active(n**q, L, log_endpoint):
        q += 1
    return q


def delay_norm(n, L, log_endpoint):
    q = path_size(n, L, log_endpoint)
    return 2 * (arb.pi() / (q+1)).cos()


def bounds(L, N, M, g, indices, log_endpoint):
    eta = 256*(L/3)**(M+1)/((M+1)*(1-L/3))
    kl = sum(abs(ball(g[j]))*L**(j-1) for j in range(1, M+1))
    kl += arb(256)/3*(L/3)**M/(1-L/3)
    arithmetic = sum((arb(p).log()/arb(n).sqrt()*delay_norm(n,L,log_endpoint)
                      for n,p in indices), arb(0))   # arb(0) start: no active primes at L <= log 2
    a = sum(arb(1)/j for j in range(1,N+1)) - arb.const_euler() - (arb.pi()*L).log()
    a -= kl*L/(2*arb(N*(N+1)).sqrt()) + arithmetic
    c = (L/2).cosh()*((L/2).exp()*L**3/3+L**2/4)
    c += sum((arb(p).log()/arb(n).sqrt()*arb(n).log()**2
              *(arb(n).log()/2).cosh()*delay_norm(n,L,log_endpoint)/2
              for n,p in indices), arb(0))
    return {'eta':eta, 'K_L':kl, 'arithmetic_loss':arithmetic,
            'a':a, 'C_L':c}


def matrix(rows):
    return arb_mat(rows)


def sym(M):
    return (M+M.transpose())/2


def block(M, inds):
    return matrix([[M[i,j] for j in inds] for i in inds])


def gram(A, mom, B):
    H = matrix([[mom[i+j] for j in range(B.ncols())] for i in range(A.ncols())])
    return A*H*B.transpose()


def shift_rows(A, offset, sign=1):
    """Coefficients of A(offset + sign*u), enclosed by binomial expansion."""
    d=A.ncols()
    powers=[offset**j for j in range(d)]
    trans=matrix([[comb(k,j)*powers[k-j]*sign**j if j<=k else 0
                   for j in range(d)] for k in range(d)])
    return A*trans


def moments(kmax, a=0, b=1, logarithm=None):
    """Independent antiderivatives: integral_a^b u^k [1 or log(u)]."""
    a,b=ball(a),ball(b)
    vals=[]
    for k in range(kmax+1):
        s=k+1
        if logarithm is None:
            v=(b**s-a**s)/s
        elif logarithm=='log':
            def primitive(x):
                return arb(0) if x == 0 else x**s*(x.log()/s-arb(1)/(s*s))
            v=primitive(b)-primitive(a)
        else:
            raise ValueError(logarithm)
        vals.append(v)
    return vals


def model(L, N, M, g, indices, log_endpoint):
    d=N+M
    # A: normalized Legendre coefficients. B: regular polynomial in U_gamma.
    A=matrix([[ball((-1)**(n+k)*comb(n,k)*comb(n+k,k))*arb(2*n+1).sqrt()
               if k<=n else 0 for k in range(N)] for n in range(N)])
    ell=arb.const_euler()+(2*arb.pi()*L).log()
    h=[sum(arb(1)/j for j in range(1,k+1)) for k in range(N)]
    T=[[arb(0) for j in range(d)] for k in range(N)]
    lp=[L**j for j in range(M+1)]
    for k in range(N):
        T[k][k]=ell-h[k]
        beta=Fraction(1,k+1)
        for j in range(1,M+1):
            if j>1:
                beta*=Fraction(j-1,j+k)
            T[k][k+j]=ball(g[j]*beta)*lp[j]
    B=A*matrix(T)
    kmax=2*d
    m0=moments(kmax)
    ml=moments(kmax,logarithm='log')
    ml2=[arb(2)/(k+1)**3 for k in range(kmax+1)]
    mll=[]
    hh,hh2=arb(0),arb(0)
    for s in range(1,kmax+2):
        hh+=arb(1)/s
        hh2+=arb(1)/(s*s)
        mll.append(hh/(s*s)-(arb.pi()**2/6-hh2)/s)
    # U_gamma(u) = A(u) log(u) + B(u).
    Uhead=gram(A,ml,A)+gram(A,m0,B)
    F=gram(A,ml2,A)+gram(B,m0,B)
    mixed=gram(A,ml,B)
    F+=mixed+mixed.transpose()
    Ar=shift_rows(A,arb(1),-1)
    Br=shift_rows(B,arb(1),-1)
    C=gram(A,mll,Ar)+gram(B,m0,Br)
    mixed=gram(A,ml,Br)
    C+=mixed+mixed.transpose()
    delays=[]
    for n,p in indices:
        delta=arb(n).log()/L
        coef=2*arb(p).log()/arb(n).sqrt()
        D=shift_rows(A,-delta)*coef
        # Reflected delayed polynomial has support (0,1-delta).
        Dr=shift_rows(A,1-delta,-1)*coef
        delays.append((n,delta,D,Dr))
        m0t=moments(kmax,delta,1)
        mlt=moments(kmax,delta,1,'log')
        Uhead+=gram(A,m0t,D)
        mixed=gram(A,mlt,D)+gram(B,m0t,D)
        F+=mixed+mixed.transpose()
        m0r=moments(kmax,0,1-delta)
        mlr=moments(kmax,0,1-delta,'log')
        mixed=gram(A,mlr,Dr)+gram(B,m0r,Dr)
        C+=mixed+mixed.transpose()
    overlaps=[]
    for n,delta,D,Dr in delays:
        for n2,delta2,D2,Dr2 in delays:
            lower=delta if n>=n2 else delta2
            F+=gram(D,moments(2*N,lower,1),D2)
            if active(n*n2,L,log_endpoint):
                C+=gram(D,moments(2*N,delta,1-delta2),Dr2)
                overlaps.append([n,n2])
    q=-sym(Uhead)
    # These exact central operators commute with reflection. Require every
    # theoretically zero off-parity entry to enclose zero before omitting it.
    for i in range(N):
        for j in range(N):
            if (i+j)%2 and not q[i,j].contains(0):
                raise ArithmeticError('Central head reflection control failed')
    return q,sym(F),sym(C),overlaps


def ldl(M):
    n=M.nrows()
    ell=[[arb(0) for j in range(n)] for i in range(n)]
    piv=[]
    for i in range(n):
        di=M[i,i]-sum(ell[i][k]**2*piv[k] for k in range(i))
        if not di>0:
            return {'passed':False,'failed_index':i,'failed_pivot':str(di),
                    'pivots':piv}
        piv.append(di)
        for j in range(i+1,n):
            ell[j][i]=(M[j,i]-sum(ell[j][k]*ell[i][k]*piv[k]
                                  for k in range(i)))/di
    return {'passed':True,'pivots':piv}


def encode(x):
    return {'mid':[int(v) for v in x.mid().man_exp()],
            'rad':[int(v) for v in x.rad().man_exp()]}


def decode(x):
    return arb(tuple(x['mid']),tuple(x['rad']))


def main():
    p=argparse.ArgumentParser()
    group=p.add_mutually_exclusive_group()
    group.add_argument('--horizon',default=None)
    group.add_argument('--log-horizon',type=int)
    p.add_argument('--N',type=int,default=128)
    p.add_argument('--M',type=int,default=180)
    p.add_argument('--bits',type=int,default=1536)
    p.add_argument('--floor',default='1e-26')
    p.add_argument('--output',type=Path,required=True)
    p.add_argument('--bounds-only',action='store_true')
    args=p.parse_args()
    ctx.prec=args.bits
    L=arb(args.log_horizon).log() if args.log_horizon else arb(args.horizon or '9/5')
    if not (0<L<3 and args.N>=1 and args.M>=2):
        raise ValueError('Require 0<L<3, N>=1, M>=2')
    indices=[]
    n=2
    while active(n,L,args.log_horizon):
        base=prime_base(n)
        if base:
            indices.append((n,base))
        n+=1
    start=time.monotonic()
    g=profile(args.M)
    b=bounds(L,args.N,args.M,g,indices,args.log_horizon)
    m=arb(args.floor)
    a=b['a'].lower()
    eta=b['eta'].upper()
    eps=((abs(a-m)+40000)*eta+2*eta**2).upper()
    b['epsilon']=eps
    result={'parameters':{k:str(v) if isinstance(v,Path) else v for k,v in vars(args).items()},
            'environment':{'python':sys.version,'python_flint':flint.__version__,
                           'flint':getattr(flint,'__FLINT_VERSION__','unavailable')},
            'indices':indices,'bounds':{k:v.str(40) for k,v in b.items()}}
    print(json.dumps(result,indent=2),flush=True)
    args.output.mkdir(parents=True,exist_ok=True)
    if args.bounds_only:
        (args.output/'bounds.json').write_text(json.dumps(result,indent=2)+'\n')
        return
    if not a>m:
        raise ArithmeticError('Analytic tail does not exceed target floor')
    q,F,C,overlaps=model(L,args.N,args.M,g,indices,args.log_horizon)
    trace=sum(F[i,i] for i in range(args.N))
    if not trace<10000000:
        raise ArithmeticError('Required full Gram trace bound failed')
    result['gram_trace']=trace.str(40)
    result['overlaps']=overlaps
    print('Matrices assembled', time.monotonic()-start, 'seconds; trace',trace.str(20),flush=True)
    archive={'description':'Independent reconstruction; enclosures from the printed formulas',
             'parameters':result['parameters'], 'bounds':{k:encode(v) for k,v in b.items()},
             'matrices':{},'tests':{}}
    for name,X in [('q',q),('F',F),('C',C)]:
        archive['matrices'][name]=[[encode(X[i,j]) for j in range(args.N)]
                                   for i in range(args.N)]
        for i in range(args.N):
            for j in range(args.N):
                if not decode(archive['matrices'][name][i][j]).contains(X[i,j]):
                    raise ArithmeticError('Serialization containment failed')
    result['sectors']={}
    for r,label in [(1,'even'),(-1,'odd')]:
        ids=list(range(0 if r==1 else 1,args.N,2))
        qr,fr,cr=block(q,ids),block(F,ids),block(C,ids)
        E=(fr+r*cr)/2-qr*qr
        I=matrix([[int(i==j) for j in ids] for i in ids])
        S=sym((a-m)*(qr-m*I)-E-eps*I)
        test=ldl(S)
        result['sectors'][label]={k:v for k,v in test.items() if k!='pivots'}
        result['sectors'][label]['pivots']=[v.str(40) for v in test['pivots']]
        result['sectors'][label]['minimum_pivot_lower']=min(v.lower() for v in test['pivots']).str(40) if test['pivots'] else None
        archive['tests'][label]=[[encode(S[i,j]) for j in range(len(ids))] for i in range(len(ids))]
        print(label,result['sectors'][label]['passed'],result['sectors'][label]['minimum_pivot_lower'],flush=True)
    path=args.output/'independent_matrices.json.gz'
    with gzip.open(path,'wt') as f:
        json.dump(archive,f)
    result['matrix_sha256']=hashlib.sha256(path.read_bytes()).hexdigest()
    result['elapsed_seconds']=time.monotonic()-start
    (args.output/'certificate.json').write_text(json.dumps(result,indent=2)+'\n')
    if not all(x['passed'] for x in result['sectors'].values()):
        sys.exit(1)


if __name__=='__main__':
    main()
