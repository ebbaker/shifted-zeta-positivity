"""Independent identities and failure controls for the review revision.

Run with python-flint, mpmath and NumPy installed. Quadrature and random
matrix checks are diagnostics; only Arb sign tests certify the operator.
"""
import json
from fractions import Fraction
from pathlib import Path
import subprocess
import sys
import tempfile
import gzip
import shutil
from math import comb
import numpy as np
import mpmath as mp
from flint import arb as A, arb_mat as AM, ctx
import certify_arb as c

def require(value, message):
    if not value:
        raise ArithmeticError(message)

def main():
    ctx.prec=384
    mp.mp.dps=80
    moment_count=0
    maxerr=mp.mpf(0)
    delta=mp.mpf('0.3')
    for k in [0,1,2,7,11]:
        for kind,weight,lo,hi in [
            ('plain',lambda u:1,0,1),('log',mp.log,0,1),
            ('log2',lambda u:mp.log(u)**2,0,1),
            ('log1',lambda u:mp.log(1-u),0,1),
            ('loglog',lambda u:mp.log(u)*mp.log(1-u),0,1),
            ('tail',lambda u:1,delta,1),('tail_log',mp.log,delta,1),
            ('tail_log1',lambda u:mp.log(1-u),delta,1),
            ('window',lambda u:1,delta,mp.mpf('0.7'))]:
            val=c.moment(1,k+1,kind,A('0.3'),A('0.7'))[0,k]
            diagnostic=mp.mpf(val.mid().str(90,radius=False))
            integral=mp.quad(lambda u:u**k*weight(u),[lo,(lo+hi)/2,hi])
            err=abs(diagnostic-integral)
            maxerr=max(maxerr,err)
            require(err<mp.mpf('1e-70'),'Moment quadrature: '+kind)
            moment_count+=1
    # Differentiate the arithmetic coefficients directly and compare with
    # the divisor-convolution form of the printed logarithmic generator.
    def primes(n):
        return [p for p in range(2,n+1) if n%p==0 and all(p%d for d in range(2,p))]
    def coeff(n,w,derivative=False):
        if n==1:return A(0 if derivative else 1)
        ps=primes(n);fac=[1-(-2*w*A(p).log()).exp() for p in ps]
        pref=((w-A('1/2'))*A(n).log()).exp()
        prod=lambda v:__import__('functools').reduce(lambda a,b:a*b,v,A(1))
        result=prod(fac)
        if derivative:
            result=A(n).log()*result+sum(2*A(p).log()*(-2*w*A(p).log()).exp()
                *prod(fac[:i]+fac[i+1:]) for i,p in enumerate(ps))
        return pref*result
    euler_count=0
    for w in [A(0),A('1/10'),A('1/2')]:
        for n in range(2,19):
            rhs=A(0)
            for d in range(2,n+1):
                if n%d:continue
                pp=primes(d)
                if len(pp)==1:
                    rhs+=2*A(pp[0]).log()/A(d).sqrt()*(w*A(d).log()).cosh()*coeff(n//d,w)
            require((coeff(n,w,True)-rhs).contains(0),'Euler derivative')
            euler_count+=1
    # Arbitrary tail combinations, rather than one-mode tests.
    fractional=[]
    for nu in [mp.mpf('0.2'),mp.mpf('0.5'),mp.mpf('0.8')]:
        L=mp.mpf('1.8');N=3
        coeffs=[mp.mpf(1),mp.mpf('-0.7'),mp.mpf('0.2'),mp.mpf('0.9')]
        # Integrate the terminating Legendre monomials directly. This avoids
        # a hypergeometric implementation's endpoint convergence heuristics.
        terms=[sum(v*mp.sqrt((2*n+1)/L)*(-1)**(n+k)*comb(n,k)*comb(n+k,k)
                   for n,v in enumerate(coeffs,N) if n>=k)
               *mp.factorial(k)/(mp.gamma(k+1+nu)*L**k)
               for k in range(N+len(coeffs))]
        def output(x):
            return x**nu*mp.polyval(list(reversed(terms)),x)
        observed=mp.quad(lambda x:output(x)**2,[0,L/2,L])
        upper=(L/2)**(2*nu)*mp.gamma(N+1-nu)/mp.gamma(N+1+nu)*sum(x*x for x in coeffs)
        require(observed<upper,'Fractional tail combination')
        fractional.append(str(observed/upper))
    # Finite Toeplitz control for exact central parity leakage.
    rng=np.random.default_rng(8675309);dim=18;head=8
    delays=rng.normal(size=dim)
    U=np.array([[delays[i-j] if i>=j else 0 for j in range(dim)] for i in range(dim)])
    R=np.eye(dim)[::-1];Q=-(U+U.T)/2
    plus=np.array([(np.eye(dim)[:,i]+np.eye(dim)[:,dim-1-i])/np.sqrt(2) for i in range(head//2)]).T
    minus=np.array([(np.eye(dim)[:,i]-np.eye(dim)[:,dim-1-i])/np.sqrt(2) for i in range(head//2)]).T
    P=np.column_stack([plus,minus]);projector=P@P.T
    for parity,B in [(1,plus),(-1,minus)]:
        q=B.T@Q@B;F=B.T@U.T@U@B;C=B.T@U.T@R@U@B
        leakage=B.T@Q@(np.eye(dim)-projector)@Q@B
        require(np.linalg.norm((F+parity*C)/2-q@q-leakage)<1e-11,'Parity identity')
    # Positive and negative signs must both be detected by the ball LDL.
    require(c.ldl(AM([[2,1],[1,2]]))['positive'],'Positive LDL control')
    require(not c.ldl(AM([[1,2],[2,1]]))['positive'],'Indefinite LDL control')
    require(not c.ldl(AM([[1,0],[0,0]]))['positive'],'Singular LDL control')
    require(c.chain_norm(2,A(4).log(),4).overlaps(A(1)),'Endpoint chain log4')
    require(c.chain_norm(2,A(8).log(),8).overlaps(A(2).sqrt()),'Endpoint chain log8')
    require([n for n,p,k in c.prime_powers(A(7).log(),7)]==[2,3,4,5],'Endpoint prime exclusion')
    require([n for n,p,k in c.prime_powers(A('1.95'))]==[2,3,4,5,7],'Prime activation control')
    root=Path(__file__).resolve().parent
    failed=subprocess.run([sys.executable,'-O',str(root/'certify_arb.py'),'--help'],capture_output=True)
    require(failed.returncode!=0 and b'assertions' in failed.stderr,'Optimized mode rejection')
    # A stale/forged PASS record must never produce a continuation claim.
    with tempfile.TemporaryDirectory() as t:
        folder=Path(t)
        src=root/'output/log7_N128'
        shutil.copyfile(src/'central_matrices.json.gz',folder/'central_matrices.json.gz')
        cert=json.loads((src/'central_certificate.json').read_text())
        cert['matrix_archive_sha256']='0'*64
        (folder/'central_certificate.json').write_text(json.dumps(cert))
        stale=subprocess.run([sys.executable,str(root/'analyze_certificate.py'),str(folder)],capture_output=True)
        require(stale.returncode!=0 and b'hash does not match' in stale.stderr,'Stale certificate rejection')
    negative=subprocess.run([sys.executable,str(root/'analyze_certificate.py'),str(root/'output/log7_N128'),'--shift=-3e-18'],capture_output=True)
    require(negative.returncode!=0 and b'requested shift/decay' in negative.stderr,'Negative shift rejection')
    # Exact scalar counterexample to a margin-only storage update.
    eps=Fraction(1,4);c2=Fraction(1,2)
    require(eps-c2<0 and 1-c2>0,'Storage orientation counterexample')
    result={'status':'PASS','moment_quadratures':moment_count,'max_moment_absolute_difference':str(maxerr),
            'arithmetic_derivative_identities':euler_count,'fractional_tail_combination_ratios':fractional,
            'controls':['parity leakage','positive/indefinite/singular LDL','logarithmic thresholds',
                        'Python -O rejection','stale certificate rejection','negative shift rejection',
                        'storage orientation counterexample'],
            'scope':'Identity diagnostics and failure controls; not substitutes for the analytic proof or Arb full-operator certificates'}
    (root/'review/review_checks.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
