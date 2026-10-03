# First-prime boundary diagnostic: a positive odd signal without a sign certificate

3 October 2026. Prepared for Edward Baker with substantial GPT-6 (Codex)
assistance. The exact serving variant and configured reasoning effort are
not exposed and are not inferred. This is exploratory floating-point work,
not independently refereed mathematics or a computer-assisted sign proof.

The new calculation evaluates the **actual finite-place boundary kernel**
at exponent one half and source length below one. It neither subtracts an
arithmetic form to manufacture the correction nor replaces the finite Euler
factor by the global endpoint symbol. The computation retains an inverse
matrix but has not enclosed its infinite-dimensional error.

**Finding.** A fixed exactly mean-zero odd prepared source gives a positive
finite approximation in every retained first-prime run. The result changes
materially with the spatial mesh, inclusion of the full compressed square,
and finite matrix order. Consequently it is a falsification *probe* for the
rank-one candidate, not a falsification. This sensitivity is a reason to
prioritize full residual bounds instead of another uncontrolled rank sweep.
The candidate, weaker support-adapted comparison, and RH remain undecided.

## Sources and exact versus sampled conditions

Let b=9/20, phi(x)=exp(-1/(1-(x/b)^2)) on |x|<b, extended by zero.
Use A=-d²/dx²+1/4 and divide each source by its own L² norm:

1. F0=A phi (even, nonzero mean);
2. F1=A(x phi) (odd, exactly zero mean);
3. F2=A((x²-c)phi), where c=(integral x² phi)/(integral phi)
   (even, intended exactly zero mean).

All exact source definitions are smooth, compactly supported in (-1/2,1/2),
and pole neutral. Their source support has diameter 0.9, so their correlations
vanish for shifts of magnitude at least 0.9 and the active prime set is {2}.
The odd mean-zero condition follows identically from parity
and does not rely on a sampled integral. The even coefficient is evaluated
as c≈0.032018011343419146; its floating evaluation is **not** an enclosure
of the exact ratio. The source preparation, correlations, and L²
normalizations are sampled in the program, rather than certified.

The three-by-three source matrix retains same-parity polarization. Real
opposite-parity cross terms vanish by the even-multiplier symmetry; their
small reported values provide a numerical check. For these fixed real
sources the real symmetric matrix extends sesquilinearly to complex
coefficients. Nothing here treats the whole smooth source space as finite.

## Actual operator and the finite approximation

In positive-axis coordinates, C acts on (0,1), T crosses from (1,infinity),
and the actual first-prime involution has the norm-convergent expansion

    F2 = (1/2) sum[n>=0] 2^(-n/2) U_(-n log 2) F_infinity
         - 2^(-1/2) U_(log 2) F_infinity.

Here U_a denotes normalized dilation, u -> exp(-a/2) f(exp(-a)u),
the physical-coordinate version of logarithmic translation.

Its formal kernel is sum[n>=0] cos(2*pi*2^n*x*y)-cos(pi*x*y).
This is used only after integration, not as a convergent pointwise series.
Keeping n=0,...,M-1 has operator tail at most
(1+1/sqrt(2))*2^(-M/2). At M=64 this is about 3.975e-10.
This analytic bound is recorded but **has not been propagated through the
inverse or made into an outward trace enclosure**.

Take normalized indicator functions of cells with endpoints x_i=(i/N)^q.
Write E for their synthesis isometry, D=E* C E, H=E* C² E, and B=E* T X E.
The independent crossing kernel is

    X(u,z) = kappa(log(u/z))/sqrt(u*z),  u>1, 0<z<1.

It vanishes unless 1<u<exp(0.9) and exp(-0.9)<z<1. The program integrates
C's cell matrix using sine-integral corner differences. It integrates the
y-cell first for TX and then uses an exactly integrated linear interpolant
of the remaining smooth u function. This evaluates highly oscillatory
dyadic sine terms without sampling them on the source mesh.

For H the program integrates each product of sine primitives over the
**whole** output interval (0,1). The identity used is

    integral[0,1] sin(a*x) sin(b*x)/x² dx
      = (J(a+b)-J(a-b))/2,
    J(v)=v*Si(v)+cos(v)-1.

The full derivation and an independent small-case check are in the
[rank-one analysis](../notes/FINITE_EULER_RANK_ONE_ANALYSIS_20261003.md).
H-D² is the off-grid leakage Gram; it must not be deleted when forming the
Galerkin denominator. All H and D entries here use the same finite dyadic
partial sum and floating arithmetic.

The primary finite scalar is

    k_N = 2 Re Tr[D (I-H)^(-1) B].

It corresponds to the finite center in the
[boundary residual certificate](../notes/FINITE_EULER_BOUNDARY_RESIDUAL_CERTIFICATE_20261003.md)
with the output/source columns also projected to the selected step space.
It is **not** a proved lower or upper bound for K. That certificate requires
full source, primal, dual, dyadic, and rounding error estimates not supplied
by this script.

The record also reports 2 Re Tr[(I-H)^(-1)D B] as
`K_reversed_finite_order`. C commutes with I-C² in the continuum, but D
and H need not commute. These different finite centers must not silently
be interchanged. An earlier exploratory order was corrected during the
internal audit; both final values are retained to expose sensitivity.

## Retained results

All numbers in the tables are floating approximations, not intervals.
The primary q=4 graded-mesh runs use M=64, source grid 16384, crossing
interpolation 4096, and 6-point z quadrature.

| N | Primary odd k_N | Reversed-order odd | Even mean-zero k_N | Smallest eigenvalue of I-H |
|---:|---:|---:|---:|---:|
| 128 | 0.0166732901 | 0.0103791513 | -0.1283421962 | 9.54093e-5 |
| 256 | 0.0164848026 | 0.0118239339 | -0.1446008392 | 2.78158e-5 |
| 512 | 0.0070874592 | 0.0042301385 | -0.1725812878 | 1.08460e-5 |

At N=512, ||H-D²|| is about 0.00646511. This is not small relative to
the displayed inverse gap. Finite values alone do not establish that the
infinite correction is positive, negative, or zero.

A second N=128 run doubles source and u resolution and changes z quadrature
from 6 to 8. Its primary odd value is 0.0166731192, a change of about
1.71e-7. This empirical sensitivity is much smaller than the spatial and
finite-order effects. It is not a rigorous error bound.

For contrast, squaring the compressed D on a uniform mesh gives the
following *different* approximation, 2 Tr[D(I-D²)^(-1)B]:

| N | Odd approximation |
|---:|---:|
| 128 | 0.0393428908 |
| 512 | 0.0318216875 |
| 1024 | 0.0281765321 |

These use M=48 (tail bound about 1.018e-7). They illustrate why a positive
compressed-matrix sign cannot be promoted to a continuum assertion.

The same implementation with the archimedean kernel 2 cos(2*pi*x*y)
provides a convention control. With the full square and a uniform mesh:

| N | Even F0 approximation | Odd F1 approximation |
|---:|---:|---:|
| 512 | -0.1084810245 | -0.1404903382 |
| 1024 | -0.1096063030 | -0.1412073577 |

These approach the existing independently interval-enclosed values near
-0.10999 and -0.14145 in the
[scalar trace summary](../../../susy-positivity/investigations/wilson-loewner/arithmetic-storage/numerics/records/sonin_scalar_summary.json).
This checks normalization and sign empirically. It does not transfer that
older certificate to the first-prime calculation.

## Reproduction and stopping point

The [program](finite_euler_first_prime_boundary.py) uses Python with NumPy
and SciPy. Retained records were run with Python 3.12, NumPy 2.5.3 and
SciPy 1.18.1; exact runtime details, source definitions, calculation
parameters, model disclosure, and the generating program hash are in each
small JSON record. No grid arrays are saved. The runtime/scope metadata was
appended to the raw numerical output without changing its generating script.

From this directory, using a Python environment with those dependencies:

```sh
OPENBLAS_NUM_THREADS=1 python3 -B finite_euler_first_prime_boundary.py --cells 128 256 512 --ugrid 4096 --terms 64 --full-square --mesh-power 4 --output finite_euler_first_prime_graded4.json
OPENBLAS_NUM_THREADS=1 python3 -B finite_euler_first_prime_boundary.py --cells 128 --ugrid 8192 --source-grid 32768 --zquad 8 --terms 64 --full-square --mesh-power 4 --output finite_euler_first_prime_source_refinement.json
OPENBLAS_NUM_THREADS=1 python3 -B finite_euler_first_prime_boundary.py --cells 128 512 1024 --ugrid 2048 --terms 48 --output finite_euler_first_prime_compressed.json
OPENBLAS_NUM_THREADS=1 python3 -B finite_euler_first_prime_boundary.py --cells 512 1024 --ugrid 4096 --archimedean --full-square --output finite_euler_first_prime_archimedean_control.json
```

The fixed grid sweep stops here. The next useful step is an outward full
residual enclosure using the whole-output Gram and source nuclear tail in
the linked analysis notes, against a specifically chosen smooth odd source.
If its final error bar crosses zero, the sign remains unresolved. Source
sampling, dyadic tails, floating arithmetic, and all output/source
complements must be included before the mean-zero candidate can be rejected.
