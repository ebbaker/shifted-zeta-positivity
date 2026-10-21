# Internal review of arithmetic heat repair and exact completion

21 October 2026; continuation begun 20 October. Prepared for **Edward Baker**
with substantial LLM assistance. Actual recorded model **gpt-6-astra**,
reasoning effort **ultra**. Separate same-model checks; no specialist,
cross-model, formal, or priority validation. Checkpoint:
`6edecb68ae6e2e095e788f0901d39373851d6412`.

Reviewed [Note 18](../notes/18_ARITHMETIC_HEAT_TRANSFER_AND_EXACT_COMPLETION_20261021.md),
CT1–CT16 and FM1–FM15. The coordinator independently rederived the moment
projection, endpoint cutoff, exact pi example, fixed-shift Gaussian
estimate and Dirichlet-series contradiction. Separate same-model agents
checked the two arguments. The scope below is part of the conclusions.

## Arithmetic transfer

Finite coefficient heat multiplies the taper by exp(v u²/4); its inverse
preserves the fixed Gevrey class. CT5 retains the Leibniz terms rather
than equating coefficient heat with numerator heat. Its near-zero term
is −m u/2, so the first variation is nonzero even for a simple zero.
This is differentiation of an explicit fixed local profile, not of an
uncontrolled actual-N remainder.

The original profiles have moments integral(u^j p)=1_{j=0}, j<m.
Consequently their polynomial projection is the endpoint reproducing
kernel K_m. The distance to that affine space is exactly
||K_m−Pi_m h||². Solving the mth-order ODE with its initial jets gives
all required terminal jets from those moments. A flat cutoff in a
terminal layer of width eta has bounded mth derivative error on that
layer, and hence squared L² cost O(eta). Division by u^(m−1) at zero is
removable and preserves the Gevrey class. This proves sharpness in the
declared closure; positivity of the repairing taper is not required.

For m=2 the inverse Gram matrix is [[4,−6],[−6,12]], giving CT11.
At a=pi, h=2cos(pi u) has moment deficit (1,4/pi²). Substitution gives
the exact correction 4−48/pi²+192/pi⁴ and repaired cost
6−192/pi⁴>4. The closest repair need not minimize its own norm. The
example is obtained through fixed flat cutoffs with N sent to infinity
first; it does not import the false full-norm theorem for an unflattened
linear taper or assert uniformity as a base cutoff moves.

In CT15, the fixed multiplier sum is exactly one and the polynomial
length is floor(N/M) times M. The mixed error is a fixed finite sum of
the errors controlled by ST and CN, so actual tails are paid before
polarization and height exhaustion. For CT16 the baseline transfer
series is finite. Choose the finite zero set using that series, then
choose repairing tapers and fixed filters. The degree-independent
majorant includes both the baseline and every selected profile.
Summability permits the subsequent filter-degree limit. Thus CT16 is
an infimum of already-existing N→infinity constants over fixed finite
families, not a theorem about all arbitrary N-dependent polynomials.

Two wording corrections were applied: the stale reference to a removed
polynomial example was deleted, and the baseline profile was explicitly
included in the summable majorant. No substantive projection or ordered
tail correction was identified in these checks.

## Exact first-mode normalization

FM1 uses A only on x>=c>1, where it is positive and pole-free. Its
entire continuation and heat equation follow from a Gaussian majorant.
The complete xi convolution in FM3 is first verified on the real axis;
the identity theorem then gives complex s. Tonelli on the positive
Euler region, followed by compact absolute domination, justifies every
term of FM4. The complete left contribution is bounded by FM5, including
all negative real arguments. No Gaussian integral through poles of A
on the real axis is used.

The positive Gaussian tilt in FM7 has mean O(log sigma). FM8 is exact
integration by parts, including its positive boundary term at c.
The derivative tail is controlled before averaging g', so FM9 does
not differentiate an asymptotic error. Its exponent is −delta/2, hence
the n=2 mode has the factor sigma^(−t log 2/4). The entire n>=3 tail
is bounded by one fixed n=3 shift using FM10; no all-n uniform shift
expansion is needed. Gaussian-small normalization changes are negligible
relative to this n=2 term.

Conditional convergence of an ordinary Dirichlet series still bounds
its terms and forces absolute convergence farther right. Its first
two coefficients therefore give FM12. FM2 forces d1=1 and d2=0 but
leaves a remainder larger than O(3^(−sigma)), a contradiction.

For the actual horizontal contours, gamma reflection bounds A at
negative real infinity because the nonzero imaginary height keeps
the sine denominator away from zero. Deforming only Re z>=c crosses
no pole; the left ray and finite vertical segment give FM14. Eventual
nonvanishing on the positive real ray is enough for this argument.
No global zero-free property, critical-line norm theorem or uniform
moving-time estimate is assigned to these new normalizers.
FM15 explicitly requires the normalizer to solve the same heat equation;
the broader class of analytic Gaussian-small modifications inherits the
ordinary-series exclusion, but need not satisfy that quotient PDE.

## Bounded reread of the imported GC/ST estimates

A separate audit rederived the sensitive premises in
[Note 16](../notes/16_GEVREY_GLOBAL_APPROXIMATION_AND_RATE_20261020.md).
It found no concrete disputed inequality on this reread. This is not a
guarantee against a hidden gap, and it does not re-prove the later
multiplier construction or Burnol's lower bound.

The [Carneiro–Chandee–Milinovich RH bound](https://arxiv.org/pdf/1309.1526)
retains the coefficient 1/4 in S(t). Taking both one-sided endpoints
gives the closed-interval count used in GC11, including repeated zeros.
The reciprocal-anchor sign in GC13 is correct. GC16 is an absolutely
convergent difference of logarithmic derivatives; exterior zeros cost
O(U log log U), while every close root remains in the explicit cluster.
No inverse leading Laurent coefficient is bounded there.

Integration by parts of the full kernel exponential gives decay uniform
in H. Fourier inversion supplies the constant one with no missing
factor log N. The extra moment in ST12 has logarithm
(sigma−1)M log M+O_W(M+1), so it does not lose a second M log M.
The low-height remote tail dominates every fixed L^J t^J, the high-height
estimate retains L<(log t)^(1/b), and the real nearest-zero cell integral
is exactly 4. No separation assumption is introduced at that step.

[Bettin–Conrey–Farmer's Theorem 1](https://arxiv.org/pdf/1211.5191)
assumes RH plus an inverse-zeta-prime moment bound for its linear taper;
it does not externally validate this stronger flat-taper argument.
The present conclusion continues to depend on the internal GC/ST
derivation. Repeated same-model agreement is not independent evidence
for the original arithmetic hypotheses, and no simplicity conclusion
is obtained here.

Reviewed Note 18 source SHA-256: `4010a3ff8a007be98f831c161ae68ac2d50cdfc5faab37fcfc10c6655c82f84f`. This records the checked source identity, not mathematical validity.
