# Review of the local correlation and Jensen comparisons

20 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), reasoning effort ultra**,
verified from recorded metadata. Separate same-model internal checks of
[Note 07](../notes/07_LOCAL_CORRELATION_AND_JENSEN_MARGIN_COMPARISONS_20261020.md); no specialist review or priority claim.

**Disposition:** the stated local dominance and coalescence calculations
pass internal review. They are scoped comparisons, not simplicity of an
original theta zero. The acceptance gates in the [progress register](../research-progress/01_RH_TO_SIMPLICITY_PROGRESS_20261020.md)
remain unmet.

## 1. Localized correlation and arithmetic accounting

- The matched-kernel transform (L6) has the stated sign and normalization:
  Fourier transformation in `lambda` of `K(t-lambda)` gives
  `exp(-2 pi i v t) K_hat(v)`. Its support stays `[-Delta,Delta]` for
  arbitrary finite compactly supported nonnegative observation measure.
  The kernel is entire and `O((1+|Re z|)^(-2))` on each fixed horizontal
  strip, so the stated explicit formula is admissible. The two transforms
  at opposite prime frequencies combine to `2 Re h_hat`, giving exactly
  the coefficient `-1/pi` in (L7). Both complex pole terms are retained.
- The diagonal kernel uses `K^2`, whose transform is the convolution of
  two triangular transforms. Its support can reach `[-2Delta,2Delta]`;
  the squared prime horizon is correct. This is a potential payment for
  this direct exact formula, not a necessary cost for every method of
  bounding the diagonal. The text already makes that distinction.
- Compact observation support and the summable quadratic zero tail
  justify the uniform convergence and all full-zero expansions. The
  central identity is exact with arbitrary integer multiplicity:
  `E-2(L-1)=(m-1)(m-2)+2(m-1)b+E_other`. Each term is nonnegative for
  integer `m>=1`; no simplicity premise is smuggled into the subtraction.
- The independently certified `C` upper error and `D` lower error are
  added with the correct signs. The common-residual-ball comparison is
  Cauchy–Schwarz with the correct normalization `eps/sqrt(c)`. For
  maximal formal precision one may say the approximate observation
  `S_hat` is real-valued; otherwise insert a real part in its matched
  inner product. This is a presentation detail, not a gap for the stated
  real arithmetic computations.
- For the finite whole-line projection, `R>=K` is correct and strict away
  from the origin. The proof's derivative and `z>=3` estimates check.
  Thus (L12) follows without importing full-zero arithmetic into the
  projection. The explicit warning that `S>=S_I` cannot be reversed
  correctly retains the exterior-zero obligation.
- The paired-observation second derivative is
  `K''(a)/K(a)=-2 pi^2 Delta^2+(8/3)Delta^2` at
  `a=3/(2 Delta)`, below `K''(0)`. This correctly prevents extending
  `R>=K` to arbitrary compact windows.
- The rank-one PSD example gives `E=2-4r` for a central double, so a
  generic signed PSD form cannot inherit the nonnegative-cross-product
  multiplicity certificate. The scope is appropriately finite algebra,
  not an actual-zeta or positive-source counterexample.

The result is a same-information comparison. It neither supplies the
missing signed arithmetic bound nor rules out a separately strengthened
linear test, and the current scope statements preserve that distinction.


## 2. Exact theta coefficients and the limiting margin

- The coefficient normalization agrees with Investigation 22 Note 05.
  Its infinite-product/operator argument permits repeated limiting zeros
  and proves strict finite Jensen hyperbolicity under RH.
- The sharpened bounds (J3)–(J4) are valid coefficientwise: the positive
  coefficient remainder is at most `k^2(k-1)^2/(8d^2)`, including `k>d`. In (J8), product Taylor
  remainders for `k<=d` retain nonnegative factors on `[0,1]`; for `k>d`,
  the geometric comparison of the finite expansion costs less than
  `sqrt(e)<2`. The displayed complete-source moment norm therefore pays
  the remainder without truncating theta coefficients.
- Taking `J=floor(m/2)` gives error `O(d^(-(m+1)/2))` after local expansion,
  for odd as well as even multiplicity. The highest derivative terms
  give the stated probabilists' Hermite polynomial with normalization
  `c_m r^m d^(-m/2)`. Simple Hermite roots and Rouché give one root in
  each symmetric local disk; real coefficients force it real. The
  uniform error and nonzero Hermite derivatives sharpen its displacement
  to `O(d^-1)` in the original coordinate.
- The Laguerre constant is correct: even multiplicity gives
  `A_m=m He_m(0)^2`, odd multiplicity gives `A_m=He_m'(0)^2`.
  At `m=2`, (J10) reduces exactly to `r^2 f''(r)^2/(2d)`; (J3) supplies
  the sharper `O(d^-2)` remainder separately claimed in (J5).
- Primary sources checked directly: [Griffin–Ono–Rolen–Zagier,
  Theorems 1 and 3](https://arxiv.org/pdf/1902.07321) use fixed degree
  and increasing shift; [Griffin et al., Theorems 1.1 and
  2.1](https://arxiv.org/pdf/1910.01227) state `n>=c exp(d/2)` and
  `Delta(M)~1/sqrt(2M)` in the claimed normalization.
  [Csordas, Remark 4.8](https://arxiv.org/pdf/1309.0055) explicitly
  distinguishes strict all-real Laguerre positivity from nonnegativity
  and links the former to simple real zeros.

The note correctly treats the root-spacing and margin rates as behavior
compatible with a hypothetical multiple endpoint. It neither upgrades
finite strictness to limiting simplicity nor treats the coefficient-shift
theorems as estimates in the unshifted large-degree limit.

The sharper first-order remainder was independently checked by the
coordinating agent after the initial cross-review. If
`A=k(k-1)/(2d)`, the coefficient error lies between zero and `A^2/2`
for `k<=d`; for `k>d`, it is `A-1<=A^2/2`. Summing gives exactly
`B4(R)/(8d^2)` and differentiating its nonnegative coefficients gives
the displayed derivative bounds. The complete higher-order remainder
was unchanged. GORZ's coefficient normalization is eight times the note's;
this common factor changes neither roots nor normalized Turán ratios.
The follow-up paper uses the note's normalization directly.

## 3. Conditioning a finite zeta approximation

The companion arithmetic assessment obtained no signed-prime gain and
was not promoted to a new criterion. With a fixed analytic approximation
`zeta=A+E` near a hypothesized double zero `rho`, the event gives
`A(rho)=-E(rho)` and `A'(rho)=-E'(rho)`. Subtracting both jets produces
`zeta(rho+w)=A_c(rho+w)+E_c(rho+w)`, with
`|E_c|<=M2 |w|^2/2` and `|E_c'|<=M2 |w|` if a genuine local bound
`|E''|<=M2` is available. This removes a naive unavoidable `w^-2`
absolute-error claim. Relative logarithmic-derivative division still
needs a lower bound for `|zeta(rho+w)/w^2|`, which the assessment did not
obtain. No differentiated pointwise remainder or zero-free denominator
was assumed.

## 4. Verification scope

The checks cover arbitrary integer multiplicity, complete exterior-zero
sums, bandwidth and pole normalizations, all finite coefficient tails,
even and odd Hermite limits, and the difference between coefficient shift
and increasing unshifted degree. Nonnegative compact observation measures
are essential to the local dominance statement. Signed forms with
separately bounded cross terms remain outside it. The Jensen statement
uses the unchanged theta coefficients and describes the multiple-zero
hypothesis itself; it needs no new source control.

No numerical zero or sign scan was run. The prior 265-fixture algebra
replay is unchanged and does not certify these infinite analytical
statements. The useful changes are the explicit same-information
comparison and the `d^-1/2`, `d^(1-m)` rates, not a larger collection of
simplicity reformulations.
