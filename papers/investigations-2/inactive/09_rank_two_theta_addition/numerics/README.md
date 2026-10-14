# Rank-two theta addition numerics

13 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Current calculation model: `gpt-6-astra` (Codex), reasoning effort **ultra**,
inherited from the recorded parent session. These are internal checks,
not independent mathematical validation. The prior initialization used
`gpt-6.1-sol`, ultra; that provenance remains in its original note.

## Reproduction and scope

From the repository root:

```sh
python3 papers/investigations-2/inactive/09_rank_two_theta_addition/numerics/check_rank_two_to_paired.py \
  --record papers/investigations-2/inactive/09_rank_two_theta_addition/numerics/RANK_TWO_TO_PAIRED_RECORD_20261013.json
```

The [script](check_rank_two_to_paired.py) uses the Python standard library and
hash-checks the retained 60-digit outward Decimal implementation before import.
The [small record](RANK_TWO_TO_PAIRED_RECORD_20261013.json) contains its source
hash, imported hashes, parameters, exact-identity outcomes, diagnostic values,
all directed endpoints and every error payment. No external data are needed.
Follow [LARGE_FILES.md](../../../../../LARGE_FILES.md) for larger future outputs.

This implements the [complete two-coset reduction](../notes/1_COMPLETE_TWO_COSET_REDUCTION_20261013.md)
and the [06 factorization assessment](../../../active/06_paired_kernel_factorization/notes/1_FOLDED_PARITY_CUSP_AND_FACTORISATION_OBSTRUCTION_20261013.md).
Its two negative tests concern individual parity sectors; neither contradicts
positivity of the complete Fourier response or a physical stationary sign.

## Exact algebra and floating diagnostics

Exact rational polynomial assertions verify the unequal-scale quadratic form,
its determinant, the Poisson inverse matrix numerator, the source derivative
insertion `P(z)=16z²−24z`, the zero-axis annihilation and the `J0,J1` Fourier
multipliers including the Jacobian and `H=widehat(m)/2` normalizations.
The raw translated-source zero-frequency formulas are independently expanded
as exact polynomials. A finite integer lattice test verifies both cosets and
the mapped diamond bijection, including axes and boundary points.

Separately marked binary64 diagnostics compare finite source products in all
folding chambers, direct versus coupled-lattice `J0,J1` projections at
`s=.2,t=.025`, both unequal-scale Poisson cosets, and the differentiated
Poisson identity with its prefactor derivatives. These checks are calibration
only: their finite sums and quadrature windows have no certified tail payments.

## Outward folded-sector certificate

Write `A(u)=sum_{n even, n>0} phi_n(|u|)` and
`B(u)=sum_{n odd, n>0} phi_n(|u|)`. Their half-transforms are
`h_A(x)=integral_0^infinity cos(xu) A(u) du`, and similarly for `B`.
The same-parity coset response is

```text
C_j(x) = h_A^(j+1)(x)^2 - h_A^(j)(x) h_A^(j+2)(x)
       + h_B^(j+1)(x)^2 - h_B^(j)(x) h_B^(j+2)(x).
```

At `t=0,x=60` (the paired kernel's Fourier frequency is `120`), the complete
outward calculation gives the looser decimal enclosures

```text
-2.53642e-14 < C_0(60) < -2.50907e-14,
-1.08815e-16 < C_1(60) < -1.07228e-16.
```

There are 1,024 Simpson panels on `0<=u<=1`, retaining theta terms 1, 2 and 3.
For `z=pi n² exp(4u)`, put `phi_n=exp(u-z)(2z²−3z)`. The derivative
polynomials obey

```text
P_(k+1)(z) = (1−4z) P_k(z) + 4z P_k'(z).
```

For every source cell, directed polynomial evaluation bounds the first five
source jets. The fourth derivative of
`u^j cos(60u+j*pi/2) phi_n(u)` is bounded by the full multinomial Leibniz sum,
using `|sin|,|cos|<=1`. The Simpson error of a panel of width `h` is at most
`h^5 sup|f''''|/2880`. All these payments enter before any Laguerre sign test.
The smooth functions being integrated are restricted to `u>=0`; no quadrature
step differentiates through a folded cusp.

The omitted theta contribution, for each moment `j=0,1,2,3`, is bounded by

```text
2*pi²*4^4*exp(−16*pi) * j!
--------------------------------------------,
[1−(5/4)^4*exp(−9*pi)] * (64*pi−9)^(j+1)
```

because `exp(4u)>=1+4u`, the positive theta summands are bounded after dropping
their negative polynomial term, and the consecutive `n>=4` ratio is bounded
by `(5/4)^4 exp(−9*pi)`. The bound covers the entire omitted half-line integral
and is allocated safely to each parity sector.

For the remaining full-source `u>=U=1` tail use
`Phi(u)<=4*pi² exp(9u−pi exp(4u))`, derived by the geometric theta ratio
`16 exp(−3*pi)<1/2`. Concavity of the exponent bounds it by its tangent at `U`.
With `kappa=4*pi exp(4U)−9`, the `j`th absolute moment tail is bounded by

```text
4*pi² exp(9U−pi exp(4U))
  * sum_(ell=0)^j binomial(j,ell) U^(j−ell) ell! / kappa^(ell+1).
```

Pi and trigonometric values are independently enclosed by the imported
Taylor bounds; no binary floating-point value enters a certified sign.

## Outward raw-sector zero-frequency certificate

The raw, unfolded even-index source is instead
`A_raw(u)=Phi_e(u+a)/sqrt(2)`, `a=log(2)/2`; put `B_raw=Phi_e−A_raw`.
It is a different sector decomposition from the folded `A,B` above.
At `t=x=0`, its same-parity Fourier responses reduce exactly to

```text
C_0_raw = (2−sqrt(2)) H0 I2 − a² H0²/sqrt(2),
C_1_raw = (2−sqrt(2)) I2² − (1+sqrt(2)) a² H0 I2,
```

where `H0=integral_0^infinity Phi(u)du` and
`I2=integral_0^infinity u² Phi(u)du`.
Outward cell ranges, multiplied by their widths, enclose both moments on
`[0,1]`; the same complete theta and source tails are then added. Thus this
second certificate needs no quadrature remainder formula. It yields

```text
-3.12462e-4 < C_0_raw < -2.91420e-4,
-1.31661e-5 < C_1_raw < -1.21197e-5.
```

These bounded witnesses reject separate-coset positive-definiteness or
nonnegative autocorrelation assertions. They do not impose stationary
conditions on separate sectors, prove the complete kernels positive definite,
or establish an RH conclusion.
