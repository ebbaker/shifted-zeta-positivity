# Reproducibility record for the fourth investigation

11 September 2026. This file retains executable source as Markdown text so
that the repository receives only background notes, as requested.

## Baseline and environment

- Branch: `susy-positivity`.
- Reviewed commit: `f92e775b44765a0f2e7fcfa69eb3bfb986ea46bb`.
- Python: `3.10.0`; NumPy: `1.25.1`.
- No zeta-zero data, optimized target matrix, or spectral square root was used.
- Imported rational helpers: the unchanged [round-3 checker](../../checks/round3/check_round3.py), which imports the unchanged [round-2 checker](../../checks/round2/check_round2.py).

Baseline SHA-256 values (historical; retained unchanged). The 12 September
reorganization updated navigation and build instructions only; current hashes
and fresh checks are separately recorded in [the attempt manifest](../../manifest.json)
and [the reorganization record](../../../../REORGANIZATION_20260912.md).
Paths in this baseline table are relative to the attempt directory.

Baseline SHA-256 values:

| File | SHA-256 |
|---|---|
| `checks/round2/check_round2.py` | `02e1a3dad1e61327113d081c34f8daee06183edb1861474700dd7df4e532ab45` |
| `checks/round3/check_round3.py` | `d8470c7876a8b10144bdbb496f1faa6b4fe7c03369d00f63e81ad7f63a86d2d7` |
| `manuscript.tex` | `18e42a1bce496d00372e8803317401269e319933ceb931d8cc1daac2b0be341b` |
| `manuscript.pdf` | `8785dd03fef158de67e4afa1f35144e3a81d12638db1e43d5bd7fb07f93a2e19` |

All 12 hashes listed in the baseline manifest matched during the review.
All three original programs were run from temporary copies preserving
`checks/round1`, `checks/round2`, and `checks/round3` relative structure.
Their complete runs passed. Their generated diagnostic files stayed in the
temporary replay directory. The original round-3 program correctly rejected
Python `-O`.

## New exact checks

The first Python block below is the complete new certificate program.
Save it as `susy_shift_review.py` in a temporary directory and pass the
positive-factorizations attempt directory as its sole argument. From this
progress-report directory, for example (set `replay_dir` to your temporary directory):

```sh
PYTHONDONTWRITEBYTECODE=1 python3 "$replay_dir/susy_shift_review.py" ../..
```

Use ordinary Python, not `-O`. The imported helpers contain assertions;
the new entry point explicitly rejects optimized mode. NumPy is required
by the existing helper module even when only its rational functions are used.
The certificate program writes no result files.

The analytic dependencies are the derivative and length-uniform reductions
in [the shifted odd note](SHIFTED_ODD_FACTOR_round4_20260911.md), and the
singular gap and polynomial witness in [the even note](EVEN_SECTOR_REDUCTION_round4_20260911.md).
The program checks the scalar bounds, not those analytic arguments.

| Exact check | Result |
|---|---:|
| Polynomial moment identities at four rational inputs, four powers each | 16 exact equalities passed |
| Shifted odd scalar cover | 1980 intervals plus endpoint tail passed |
| Proven shifted odd floor | `1/200` |
| Smallest cell | 1748, namely `[1748/2000,1749/2000]` |
| Smallest cell lower endpoint, approximate | `0.007595356689104375` |
| Endpoint-tail lower endpoint, approximate | `0.5256421302289268` |
| Even mean-zero gap lower endpoint, approximate | `0.11500531275311032 > 11/100` |
| Flattened even polynomial form | Upper endpoint `< -1/2500` |
| Flattened form enclosure, rounded outward | `[-0.008308003, -0.000495502]` |

The comparisons proving signs are exact rational comparisons. Decimal
summaries above are for reading. The new certificate uses the conservative
Euler-constant bounds from round 3; it does not silently replace them with
floating-point constants.

```python
from fractions import Fraction as F
import importlib.util
import sys
from math import comb
sys.dont_write_bytecode = True
from pathlib import Path
ROOT=Path(sys.argv[1]).resolve()
spec=importlib.util.spec_from_file_location('r3', ROOT/'checks/round3/check_round3.py')
r3=importlib.util.module_from_spec(spec);spec.loader.exec_module(r3)
I=r3.I

def certify():
    if not __debug__:
        raise RuntimeError('Optimized Python is not permitted')
    ell=F(7,20);C=F(17,16);D=F(31,480)
    require=r3.require
    # Exact split integrals independently check all four moment formulas.
    for ratio in [F(1,10),F(1,3),F(2,3),F(9,10)]:
        x=ell*ratio;z=ratio**2
        P=F(3,10)-z/6+z*z/25
        U=F(7,10)+F(3,5)*z-z*z/10+F(2,175)*z**3
        expected=[2*ell**2*P,F(52,75)*ell**3,ell**4*U,
                  8*ell**5*(F(13,75)*z+F(3,35))]
        for m in range(1,5):
            value=F(0)
            for lo,hi,left in [(F(0),x,True),(x,ell,False)]:
                for k in range(m+1):
                    plus=F(comb(m,k))*x**(m-k)
                    minus=plus*((-1)**k if left else (-1)**(m-k))
                    value+=(plus-minus)*((hi**(k+2)-lo**(k+2))/F(k+2)
                              -F(4,5)/ell**2*(hi**(k+4)-lo**(k+4))/F(k+4))
            require(value/x==expected[m-1],f'polynomial moment {m}, ratio {ratio}')
    require(((r3.exp_point(ell)+r3.exp_point(-ell))/2).hi<C, 'cosh(7/20)<17/16')
    half_cosh=(r3.exp_point(ell/2)+r3.exp_point(-ell/2))/2
    require(r3.power(half_cosh,2).hi<F(33,32),'cosh squared(7/40)<33/32')
    require(D*(1+C/2)<F(1,10),'quadratic derivative bound')
    require(C/3+C*C*ell*ell/24+C*C/4<F(13,20),'cubic derivative bound')
    ln2,pi,gamma,_=r3.constants()
    constant=-gamma-r3.log_interval(pi*F(7,10))
    def parts(z):
        den=1-F(4,5)*z
        P=F(3,10)-z/6+r3.power(z,2)/25
        Q=F(7,10)+F(3,5)*z-r3.power(z,2)/10+F(2,175)*r3.power(z,3)
        old=(F(7,5)-F(22,15)*z-2*D*ell**2*P-F(13,75)*ell**3*F(33,32))/den
        B=(-ell**2*P/2+F(91,150)*ell**3+ell**4*Q/30
           +F(13,10)*ell**5*(F(13,75)*z+F(3,35)))/den
        return old-I(0,max(F(0),B.hi))/4
    minimum=None;cell=None
    for k in range(1980):
        z=I(F(k,2000),F(k+1,2000))
        bound=constant-r3.log_interval(1-z)/2+parts(z)
        require(bound.lo>F(1,200),f'shifted odd potential cell {k}')
        if minimum is None or bound.lo<minimum:
            minimum=bound.lo;cell=k
    tail=constant+r3.log_point(100)/2+parts(I(F(99,100),1))
    require(tail.lo>F(1,200),'shifted odd endpoint tail')
    # A simpler even mean-zero bound, valid through total length 7/10.
    even_gap=F(3,2)+constant-D*F(7,10)**2/2
    require(even_gap.lo>F(11,100),'even mean-zero gap')
    flat=-gamma-r3.log_interval(pi*ln2)+F(31,30)+F(11,24)*ln2
    require(flat.hi<F(-1,2500),'flattened even model has a negative polynomial input')
    return {'shifted_odd_floor':'1/200','length_upper':'7/10','shift_range':'[0,1/2]',
            'exact_moment_checks':16,'cells':1980,'smallest_cell':cell,'smallest_cell_lower':float(minimum),
            'endpoint_tail_lower':float(tail.lo),'even_mean_zero_gap_lower':float(even_gap.lo),
            'flattened_even_rayleigh_interval':flat.display()}

if __name__=='__main__':
    print(certify())
```

## Separate floating-point identity diagnostics

The second block is an independent check of the shift correction, comparing
an original full-interval autocorrelation with the folded potential and
weighted-difference correction. It also rechecks the central identity using
the baseline program. Its input is the fixed complex odd polynomial
`phi(x) * (1 + 0.3i (x/ell)^2 + 0.2 (x/ell)^4)`.

Save this block as a separate temporary program and pass the same directory:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 "$replay_dir/susy_shift_diagnostics.py" ../..
```

The two quadrature orders are 96 and 192, at lengths `1/4`, `log(2)`,
and `7/10`, and shifts `1/4` and `1/2`. The moving cusp in the potential
integral is split explicitly. The triangle integral uses a change of
variables that keeps the difference coordinate separate.

The largest difference between the two shift-energy formulations, divided
by the input norm squared, was below `6e-17`. The largest central-identity
absolute error in these runs was below `1.1e-15` on the unnormalized input.
All sampled shifted conductances were positive. These are diagnostics;
positivity for the entire parameter range follows from the analytic proof
and rational cover, not these sampled values.

At `L=log(2), omega=1/2`, the shift energy divided by the input norm squared
was approximately `-0.00549687391794265`. At `L=7/10, omega=1/2`, it was
approximately `-0.00573045860887845`. In particular the shift correction
is not being assumed nonnegative.

The separate even polynomial calculation gives the true gamma value
approximately `0.005544682598649375` and the simplified value approximately
`-0.004406839079293734`. Only the latter sign has a new rational certificate
in this round. Its correlation is `1-5s^2+5s^3-s^5`, for `s=t/L` on `[0,1]`.

```python
import sys
sys.dont_write_bytecode=True
import importlib.util
from pathlib import Path
import math
import numpy as np
from numpy.polynomial.legendre import leggauss
ROOT=Path(sys.argv[1]).resolve()
spec=importlib.util.spec_from_file_location('r3',ROOT/'checks/round3/check_round3.py')
r3=importlib.util.module_from_spec(spec);spec.loader.exec_module(r3)

def diagnostic(L,om,n):
    ell=L/2;z,w=leggauss(n)
    x=ell*(z+1)/2;wx=ell*w/2
    phi=lambda q:q*(1-.8*(q/ell)**2)
    h=lambda q:1+.3j*(q/ell)**2+.2*(q/ell)**4
    f=lambda q:phi(q)*h(q)
    k=lambda t:2*np.sinh(om*t/2)**2*r3.kernel(t)
    # Original full-interval autocorrelation, independently of folding.
    t=L*(z+1)/2;wt=L*w/2
    v,wv=leggauss(16)
    xx=-t[:,None]/2+(L-t[:,None])*v/2
    corr=(L-t)/2*((np.conj(f(xx+t[:,None]))*f(xx))@wv)
    original=np.dot(wt,2*k(t)*corr.real)
    # Folded potential; split at the moving cusp y=x.
    delta=np.zeros_like(x)
    for lo,hi in [(np.zeros_like(x),x),(x,np.full_like(x,ell))]:
        y=lo[:,None]+(hi-lo)[:,None]*(z+1)/2
        wy=(hi-lo)[:,None]*w/2
        delta+=np.sum(wy*(k(abs(x[:,None]-y))-k(x[:,None]+y))*phi(y),axis=1)/phi(x)
    pot=np.dot(wx,2*delta*abs(f(x))**2)
    # Difference-square correction, integrated on a Duffy triangle.
    d=ell*(z+1)/2;wd=ell*w/2
    y=(ell-d[:,None])*(z+1)/2;wy=(ell-d[:,None])*w/2
    xx=y+d[:,None]
    dh=k(xx+y)-k(d[:,None])
    edge=np.dot(wd,np.sum(wy*dh*phi(xx)*phi(y)*2*abs(h(xx)-h(y))**2,axis=1))
    norm=2*np.dot(wx,abs(f(x))**2)
    conductance=np.cosh(om*(xx+y))*r3.kernel(xx+y)-np.cosh(om*d[:,None])*r3.kernel(d[:,None])
    err=abs(original-pot-edge)/norm
    if err>2e-10 or np.min(conductance)<=0:
        raise ArithmeticError('Shifted factor diagnostic failed')
    base=r3.odd_identity(L,n)
    return dict(L=L,omega=om,n=n,normalized_shift=float(original/norm),
                normalized_identity_error=float(err),
                base_identity_error=base['absolute_difference'],
                min_sampled_shifted_conductance=float(np.min(conductance)))

if __name__=='__main__':
    for L in [.25,math.log(2),.7]:
        for om in [.25,.5]:
            for n in [96,192]:
                print(diagnostic(L,om,n))
    # Separate even polynomial diagnostic; positivity is not certified here.
    z,w=leggauss(256);L=math.log(2);t=L*(z+1)/2;wt=L*w/2;s=t/L
    fx=np.sqrt(15/(8*L))*(1-z*z);wx=L*w/2
    pole=np.dot(wx,fx*np.cosh(L*z/4))
    q=r3.W0+np.dot(wt,2*r3.jump(t)*(5*s*s-5*s**3+s**5))+2*r3.tail(L)+2*pole*pole
    flat=-.5772156649015329-math.log(math.pi*L)+31/30+11/24*math.log(2)
    print(dict(even_polynomial_gamma_diagnostic=float(q),flattened_model=float(flat)))
```

## Interpretation and remaining checks

The exact computations prove their scalar inequalities conditional on the
written reductions. The floating-point checks test independently arranged
integrals and detect normalization, sign, and folding mistakes; they do
not establish continuum positivity. The even scalar Schur complement is
not evaluated by either program.

No new PDF or manuscript source is part of this investigation. Reproducing
these blocks in temporary files leaves the research deliverables in this
folder as Markdown only.
