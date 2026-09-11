"""Analytic complement estimates for an arbitrary finite spatial partition."""
import math
from common import *

def arithmetic(L,cells=512,iterations=500):
    length=L.value();active=active_powers(L)
    edges=[]
    for n,p,_ in active:
        delta=A(n).log()*cells/length
        for signed in [-delta,delta]:
            k=math.floor(float(signed.mid()))
            # A grid-aligned delay is allowed, but only if exact log geometry
            # establishes alignment before the Arb floor check.
            exact=any(logn(n)==L*Fraction(abs(j),cells) for j in [k,k+1])
            if exact:
                k=next(j for j in [k,k+1] if logn(n)==L*Fraction(abs(j),cells))
                offsets=[k]
            else:
                assert k<signed<k+1
                offsets=[k,k+1]
            edges.append((A(p).log()/A(n).sqrt(),offsets))
    neighbors=[[(float(alpha.mid()),[i+k for k in offsets if 0<=i+k<cells])
                for alpha,offsets in edges] for i in range(cells)]
    weights=[1.]*cells
    for _ in range(iterations):
        tw=[sum(alpha*max((weights[j] for j in js),default=0.) for alpha,js in row) for row in neighbors]
        scale=max(tw)+3
        weights=[(x+3*y)/scale for x,y in zip(tw,weights)]
    strings=[format(x,'.16g') for x in weights];w=[rat(s) for s in strings]
    assert all(x>0 for x in w)
    ratios=[]
    for i in range(cells):
        row=A(0)
        for alpha,offsets in edges:
            vals=[w[i+k] for k in offsets if 0<=i+k<cells]
            if vals:row+=alpha*max(x.upper() for x in vals)
        ratios.append((row/w[i]).upper())
    rho=max(ratios)
    return rho,{'cells':cells,'iterations':iterations,'norm_upper':rho.str(45),
                'active_prime_powers':[x[0] for x in active],'weights':strings}

def eigen_floor(mat):
    """Positive lower bound by finite Arb LDL; zero means uncertified."""
    lo=A(0);hi=min(mat[i,i].upper() for i in range(mat.nrows()))
    if not ldl(mat)['positive']:return A(0)
    for _ in range(80):
        mid=(lo+hi)/2
        if ldl(mat-ident(mat.nrows())*mid)['positive']:lo=mid
        else:hi=mid
    return lo.lower()

def comparison(geometry):
    lengths=[x.value() for x in geometry.lengths]
    g=geometry.g;M=geometry.degree;L=geometry.L.value()
    deriv=sum(((j-1)*abs(rat(g[j]))*L**(j-2) for j in range(2,M+1)),A(0))
    ratio=L/3
    deriv+=A(256)/9*ratio**(M-1)*(M/(1-ratio)+ratio/(1-ratio)**2)
    n=len(lengths);mat=AM(n,n);cross={}
    for i,(length,modes) in enumerate(zip(lengths,geometry.modes)):
        mat[i,i]=c.analytic(length,g,modes,[],None)['tail_floor'].lower()
    for i in range(n):
        for j in range(i+1,n):
            li,lj=lengths[i],lengths[j]
            ni,nj=geometry.modes[i],geometry.modes[j]
            primitive=min((li/A(ni*(ni+1)).sqrt()).upper(),(lj/A(nj*(nj+1)).sqrt()).upper())
            smooth=(deriv*primitive*(li*lj).sqrt()/4).upper()
            if j==i+1:singular=A.pi()/2
            else:
                gap=(geometry.starts[j]-geometry.starts[i+1]).value()
                hs=(((gap+li)*(gap+lj)/(gap*(gap+li+lj))).log().sqrt()/2).upper()
                singular=min((A.pi()/2).upper(),hs)
            bound=(singular+smooth).upper()
            mat[i,j]=mat[j,i]=-bound
            cross[f'{i},{j}']={'singular_upper':singular.upper().str(40),'smooth_upper':smooth.str(40)}
    return mat,cross

def bounds(geometry,cells=512):
    rho,record=arithmetic(geometry.L,cells)
    gamma,cross=comparison(geometry)
    beta=eigen_floor(gamma-ident(gamma.nrows())*rho)
    return beta,{'arithmetic':record,'gamma_comparison':[[c.pack(x) for x in row] for row in gamma.tolist()],
                 'gamma_cross':cross,'joint_tail_floor':beta.str(45)}
