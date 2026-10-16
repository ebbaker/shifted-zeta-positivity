# Scoped review: localized target and amplitude-profile compatibility

8 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Reviewer: a separate GPT-6 (Codex) agent from the author of the localized
endpoint certificate. Exact serving variant and configured reasoning effort
are not exposed and are not inferred.

## Verdict

The exact endpoint certificate in `check_localized_target.py` is algebraically
correct, covers the stated parameter rectangle, and is compatible with the
full-amplitude reduction in `AMPLITUDE_PROFILE_REDUCTION_20261008.md`.
The proposed boundary `17499/20000` remains conditional on a NEW count gain
on the residual nearly saturated class, in addition to the already imported
external moment, detector, reflection, and seven-eighths inputs. This review
does not establish that new estimate and does not independently validate the
external deep proofs or Lean formalization.

## Independent reconstruction

Using the source's general endpoint exponent rather than the checker's
`Eplain` formula, I reconstructed

\[
E=h(R^*+1/2+\delta)-1-b(7/12+\delta/2)
 +\ell(q-1-\delta/2),
\]
\[
R^*=1-\delta+
\frac{(5/6-\delta)\delta P_x}{2J},\quad
J=(5/6-\delta)D_x+\delta P_x,\quad x=q/\delta.
\]

At `ell=1/6+1/5000`, `b=1/8`, the geometry is
`h=508/625`, `sigma=17499/20000`, and `low=3749/20000`.
With `y=1/2-x`, `P_x=p_y/9` and `J=j_y/108`, multiplication gives

\[
N=10368J(-E)
=-96j_yE_{\rm plain}
 -576h(5/6-\delta)\delta p_y.
\]

This is exactly the polynomial used by the checker. As an independent
arithmetic check, I evaluated the direct source expression and the sparse
polynomial at a tensor set of three distinct rational delta values and four
distinct rational y values. Every value agreed. Both expressions after
multiplication have degree at most two in delta and at most three in y, so
these 12 exact nodes also determine the polynomial identity; this is not an
extremum estimate from a grid.

On `1/50<=delta<=3/4`, `0<=y<=1/2`, the denominator `J` is strictly
positive: `5/6-delta>=1/12`, while both `D_x` and `P_x` are positive.
Thus checking `N-10368*margin*J>0` is the correct sign for `E<-margin`.
Replacing the row exponent by `R^*-eta` subtracts exactly `h*eta` from E,
so the improved polynomial is correctly
`N+10368*(h*eta-margin)*J`.

## Continuous certificate and cover

The binomial change from each rectangle to the unit square is correct.
For degree `(n,m)`, the conversion of a monomial coefficient `q[i,j]` to
the Bernstein coefficient `(k,l)` uses
`C(k,i)/C(n,i) * C(l,j)/C(m,j)`, summed over `i<=k,j<=l`.
Bernstein basis functions are nonnegative and sum to one, so a positive
minimum coefficient gives the required lower bound throughout the box.
Each recursive bisection exactly covers its parent.

The four starting rectangles cover the full active rectangle:

- `delta in [1/50,9/25]`, all y;
- `delta in [21/50,3/4]`, all y;
- `delta in [9/25,21/50]`, `y in [1/100,1/2]`;
- the remaining hard box, with the new row-count hypothesis.

The common boundaries overlap harmlessly. The seven terminal rectangles
have strictly positive rational Bernstein coefficients, as reported. I reran
the exact script and reproduced the retained JSON exactly. The floor bin
is handled separately, so the absence of `delta<1/50` from this cover is
intentional.

The remaining low-geometry and elementary margins are consistent with the
previously reviewed geometry family. In particular, `ell<1/5` and
`f(d)=-d+(5ell-1+d)_+/8` has maximum zero at the checked endpoints and
kink. The principal, floor, middle, and small-row margins exceed `1/100000`.
The frequency allowance `zeta=1/1600000` retains
`ell/(h+zeta)>1/5` and costs less than one quarter of this endpoint margin
under the previously established slope bound of two. The lower Euler
contour domain remains valid since `sigma>87/100`.

## Profile compatibility

A full profile needs the supply threshold `1/5`, slightly stronger than
the old `7/37`. The checker proves the stronger threshold. The refined
crossing has `r>=3/5`, so the inverse second width has a fixed margin
`2r-1>=1/5`; the first width is supplied by the fixed capacity decrement.
For mathematical comparisons away from the crossing, extending G constantly
beyond its available length is legitimate. The actual selected-side
capacities are below the available length.

On the hard box, the retuning ratio has exact lower bound `31/52`.
A fixed-cutoff short-branch improvement at least `1/5000` therefore gives
complete-count improvement at least `31/260000`, after reducing t. The
spare amount above the desired `1/10000` is `1/52000`. All preliminary
count-level losses can be chosen smaller than that fixed amount. Retuning
is essential: keeping t at its old optimum leaves the long inverse branch
unchanged and does not yield a full-count saving.

Accordingly the proposed additional theorem need only concern profiles with
`H_G(t0)<1/5000` inside the hard box. The weighted saturation statements in
the profile note follow directly from Markov's inequality for the deficits:
mean deficit is `delta*y<=21/5000`, at most one fifth of the length can be
below 90 percent of maximal amplitude, and zero-amplitude slots occupy at
most one fiftieth. The fully saturated profile has exactly zero profile gain
and remains in the unresolved class.

## Additional audit: joint-witness payoff and normalization

Section 8 of `JOINT_WITNESS_REDUCTION_20261008.md` passes this scoped audit.
The new mixed arithmetic estimate remains unproved. The audit concerns its
conditional implication, not the existence of the asserted saving.

The mixed moment exponent `1+delta*m-eta_mix`, divided by the simultaneous
witness spike `delta*(r+m)` and selected prime spike `2G_I`, gives
`1-delta*r-2G_I-eta_mix`. With `G_I>=q*z` and ideal capacity
`z=(1-r)/2`, this is exactly `A_I(r)-eta_mix`. The baseline exponent is
consistent with the source's marked inverse moment and its pointwise bound
`|S_m|^2<=U^(delta*m+epsilon)` for `m<=1/2`. Whole-slot/capacity losses and
rowwise-height losses must still be budgeted; no moment with arbitrary extra
coefficients is being imported.

The inverse/plain crossing displacement is `-eta_mix/(delta*D)`, the short
envelope improvement is `(B/D)*eta_mix`, and the subsequent detector cutoff
displacement is `-B*eta_mix/J`. The resulting full-envelope factor `F=aB/J`
has the stated exact derivative numerators:

- delta derivative: `-(5/6)B^2(1-x)`;
- x derivative: `a[(10/9)a+delta*B^2]`.

Both denominators are `J^2>0`. Thus the uniform minimum is exactly
`1091200/2012413`. A mixed saving `1/5000` implies full gain
`5456/50310325`, leaving `169987/20124130000` above the required `1/10000`.
That spare exponent is approximately `0.000008446924165`; for example a
cumulative count-level loss below `1/250000` fits strictly within it.

Independent positive interval arithmetic reproduces
`t_new in (1.10602459656,1.14832472132)` and the conservative crossing range
`r_new in (0.70130991158,0.73517021282)`. Hence the proposed inverse-length
band `[0.70,0.74]` covers the crossing with fixed margins. Within that band,
`t_new-r>0.36602459`, so the plain-length range `[0.36,0.50]` covers every
nontrivial short witness after sufficiently small support losses. It also
justifies removal of the inverse base cutoff from its fixed annulus for
sufficiently large U. Cases `m>=1/2` retain their unweighted plain count.

The stated outside-band margins are valid and equal, using the coarser
rational endpoints, to `7/12500` on the plain/left side and `13/25000` on
the inverse/right side. Both exceed `1/2000`. The latter correctly subtracts
`eta_mix` because the old inverse estimate outside the band has no mixed
saving. These margins cover all short witnesses; the original long branch
is used at the new cutoff. No assumption of a gain on both marginal branches
is made.

The independent standard-library checker `check_joint_witness_payoff.py`
verifies the derivative identities with rational sparse polynomials, the
rational interval bounds and outside-band margins, and the crossing and
normalization identities. Its small retained output is
`joint_witness_payoff_check.json`. It uses no floating-point optimization;
decimals in the output are displays of exact fractions. The scope excludes
the rest of the coefficient and cross-cutoff analysis beyond the specific
moment-to-count normalization requested for this review.

Related derivations: [localized target](../notes/LOCALIZED_JOINT_WITNESS_TARGET_20261008.md),
[profile reduction](../notes/AMPLITUDE_PROFILE_REDUCTION_20261008.md), and
[joint witness](../notes/JOINT_WITNESS_REDUCTION_20261008.md).
Exact checks and their scope are indexed in the [numerical guide](../numerics/README.md).
