# Round 3: reflection supplies an odd-sector factor; the first prime stabilizes

11 September 2026. Continuation on `susy-positivity` from `4de517e`.
Working research, with AI-assisted derivation and checking; no independent
specialist review or novelty claim. The full proofs are in manuscript v0.2,
“Reflection folding and an explicit odd-sector completion” and its certificate
appendix. The checker is [check_round3.py](checks/round3/check_round3.py).

## The questions this round decided

The previous rounds left two concrete milestones: complete the prime-free
form with coherent amplitudes, and understand the first-prime diagonal
accounting. This round asked whether reflection, an existing symmetry of the
arithmetic form, supplies a useful mixing rule; and whether the proposed
independent prime-edge square leaves a positive remainder.

The answers are partial success and a definite failure, respectively. There
is now an explicit complete factor for the central **odd** gamma sector
through the prime-free slab. The even sector is still open in this
construction. The independent-edge remainder is negative on a simple
polynomial input within the first-prime interval.

## An explicit factor on the odd subspace

Write the original interval as `(-ell,ell)`, with `ell=L/2`. Fold an input of
parity `epsilon` by setting `g(x)=sqrt(2) f(x)` on `(0,ell)`. The off-diagonal
kernel becomes

$$R(|x-y|)+\epsilon R(x+y).$$

The function `R` is strictly increasing. Consequently the odd sector has a
positive difference conductance

$$h_-(x,y)=R(x+y)-R(|x-y|)>0.$$

Use the explicit positive cubic

$$\phi_L(x)=x\left(1-\frac{4x^2}{5\ell^2}\right).$$

With `v_L=(Q_gamma^- phi_L)/phi_L`, expanding the weighted difference square
gives the exact identity

$$
Q^\gamma_{0,L}[f]
=\frac12\iint h_-(x,y)\phi_L(x)\phi_L(y)
 \left|\frac{g(x)}{\phi_L(x)}-\frac{g(y)}{\phi_L(y)}\right|^2 dx\,dy
 +\int v_L(x)|g(x)|^2dx.
$$

The proof computes `v_L` directly, including the normalization, endpoint
logarithms, and negative odd pole term. It bounds the derivative of the
regular kernel `r(t)=j(t)-1/(2t)` by `31/480` for `t<=7/10`. This reduces
positivity to an explicit scalar function of `z=x^2/ell^2`. Exact rational
interval arithmetic proves that function exceeds `1/100` on **every**
`0<=z<1`: 1980 rational cells cover `[0,.99]`, and an analytic logarithm
bound handles `[.99,1)`. The smallest cell lower bound is about `0.0176841`.

Thus

$$Q^\gamma_{0,L}[f]\geq\frac1{100}\|f\|^2
\quad\text{for odd }f,\qquad 0<L\leq7/10.$$

Closing this factor from the odd smooth core gives the full logarithmic
form domain and a graded supercharge by the manuscript's block lemma.
For `L<=log(2)` this is a factor of the full central Weil form on odd inputs.
For `log(2)<L<=.7` it is a statement about the gamma form only.

The cubic was selected by testing simple positive odd polynomials and then
proved to work; it is not a canonical arithmetic object or a fitted
spectral square root. The constant and linear trial weights in the folded
coordinate did not give a positive pointwise potential at `L=log(2)`.
Reflection supplies a concrete coherent operation: the odd projection mixes
`f(x)` with `f(-x)` before another difference is squared. As a map on the
original inputs it can involve four amplitudes, so this construction is
outside the two-point class excluded in round 2.

The even folded kernel is positive on an open set whenever
`L>2*t0`, approximately `.5624`. Therefore a positive scalar conductance
with the same folding cannot cover the even sector at `L=log(2)`.
This is a restriction on that construction, not on even-sector positivity.

## The first prime is an essential stabilizer on an explicit input

Take `L=1` and the unit input `f(x)=sqrt(12)*x` on `(-1/2,1/2)`.
Only the `n=2` arithmetic delay is active. The checker proves:

| Quantity on this input | Certified enclosure, rounded outward |
|---|---:|
| Gamma form | `[-0.137027, -0.128850]` |
| First-prime contribution | `[0.405231, 0.405232]` |
| Full form | `[0.268205, 0.276382]` |
| Gamma minus the independent-edge diagonal debit | `[-0.598903, -0.590726]` |

These signs follow from an exact mass expansion of the polynomial
correlation, with integral bounds on inverse-power tails and a geometric
bound on exponential tails. They use no zeta-zero data. They are signs on
this input, not a new certificate of positivity on all inputs at `L=1`.

This makes the earlier diagonal-accounting objection concrete. The prime
raises a negative odd gamma direction above zero. A model that requires the
gamma contribution to remain an independently positive additive subsystem
throughout the first-prime interval cannot work. The previously proposed
remainder after taking out the prime-edge square actually fails.

## The exact first-prime coupling after folding

For `log(2)<L<=log(3)`, set `a=log(2)` and `c=a/sqrt(2)`. On the folded
half interval the first prime is the reflection `x -> a-x` restricted to the
cap `J=(a-ell,ell)`. Let `Pi_+` and `Pi_-` project onto the symmetric and
antisymmetric functions on this cap. Then

$$Q_p[f]=-\epsilon c\bigl(\|\Pi_+g\|^2-\|\Pi_-g\|^2\bigr).$$

For odd inputs it adds `c` to the symmetric cap channel and subtracts `c`
from the antisymmetric channel. Even inputs have the opposite signs.
The independent-edge square is `2c ||Pi_{-epsilon} g||^2`; its remainder
subtracts `c ||1_J g||^2` from gamma. This explains why that allocation
loses positivity. There is an exact coupling rule, but one channel remains
negative and must be controlled jointly with gamma.

## Verification and scope

- The odd potential inequality and the three linear-input signs have exact
  rational certificates, conditional on the written analytic reductions.
- Independent autocorrelation and folded-factor quadratures agree on a
  complex odd polynomial at `L=.25, log(2), .7`, with 128 and 256 nodes.
  The endpoint logarithm is integrated with explicit polynomial moments.
  The largest absolute discrepancy is below `6e-16` on the unnormalized
  test inputs. This is an identity diagnostic, not the positivity proof.
- A discrete full-interval translation is compared to the folded reflection
  on complex inputs of both parities. Both positive and negative odd cap
  channels are tested as controls.
- The original round-1 and round-2 checkers were replayed in temporary
  directories; their historical recorded outputs were preserved.
- The checker rejects Python `-O`, because its imported rational helpers
  contain assertions.
- No large data, target matrices, spectral square roots, or zero archives
  enter the new proof. No depth-extension campaign was undertaken.
- Independent proof review, continuum domain review, and priority review
  remain outstanding. The existing finite-depth results are stronger as
  positivity ranges; the contribution here is an explicit factor on one
  symmetry sector and a design constraint on the first-prime model.

## Literature check and the next mathematical target

A targeted primary-source search identified the existing setting, without
establishing priority for the explicit cubic bound. Suzuki's
[Weil's quadratic form via the screw function, v2](https://arxiv.org/abs/2606.09096v2)
provides an operator framework for earlier Weil-form results; its August
revision still needs a detailed comparison with this manuscript. Connes and
Consani's [archimedean trace-formula paper](https://arxiv.org/abs/2006.13771)
uses the Sonin-space compression and controls the difference from the Weil
distribution. These abstract-level checks are orientation only: this round
has not verified or imported a new theorem from either paper. The project
notes already record an earlier odd-sector experiment and a retracted
Dirichlet-form novelty claim. That history remains relevant.

The next construction target is the **even central prime-free sector**, with
its positive pole amplitude retained coherently. It must match the full
normalization and pass the folded off-diagonal test; a direct repetition of
the odd ground transform cannot do so. Once an even model exists, the
cap-reflection formula provides a concrete first-prime test: both cap
channels must be accounted for without demanding positivity of gamma alone
or of the failed independent-edge remainder. A shift-uniform version of the
odd construction is also still open here.
