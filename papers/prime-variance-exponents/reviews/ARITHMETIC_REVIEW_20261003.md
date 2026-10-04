# Arithmetic transfer and generic-model review

3 October 2026; final-text pass completed 4 October 2026 (America/New_York).
Internal LLM proof review for the new manuscript.
Model: GPT-6 (Codex), inherited configuration; the exact serving variant
and configured reasoning effort are not exposed and are not inferred.
This is an internal check, not independent specialist refereeing.

## Sources checked

Read the [continuation note](../notes/MANUSCRIPT_CONTINUATION_20261003.md)
and all four [subpower program notes](../../investigations/sonin-critical-boundary/notes/subpower-milestones/README.md).
Also checked the elementary Chebyshev proof in selective-loss note 05 and
the previous first-investigation review. This record concerns the
arithmetic reduction and generic obstruction; it does not certify a new
actual-prime saving or independently regenerate the outward zero data.

## Short intervals

The exact constants and complete support bands are correct. The inverse
set of t for an atom n in the centered interval is
[n-h/2,n+h/2), up to measure-zero endpoints. Finite Fubini therefore gives
the symmetric average of w((n+u)/x). The density term vanishes exactly
because the integral of w is zero, including real X and h.

The symmetric Taylor average differs from w(n/x) by at most
h²||w''||∞/(24x²). The zero extension is C², so this also holds at the
support boundaries. The difference vanishes outside
[Ax-h/2,Bx+h/2]; all these atoms are included when bounding their total
weight by ψ(Bx+h/2). Elementary binomial coefficients give
ψ(2n)-ψ(n) ≤ 2n log 2; dyadic summation and rounding give
ψ(T) ≤ 4(log 2)T. Because h ≤ AX ≤ Ax,
Bx+h/2 ≤ (B+A/2)x. Thus the stated C_app is valid and
the squared L² approximation error is at most C_app²h⁴/(2X).

Cauchy–Schwarz gives Q_h ≤ (3/2)X²S(X,h)/h². Combining this with
|a+b|² ≤ 2|a|²+2|b|² proves the factor 3 and the stated error term
C_app²h⁴/X. The reverse triangle inequality gives the stated norm error.
At h=X^(3/4), the support condition h≤AX holds for all sufficiently
large X, and the norm error is O(X). This proves equivalence of the
admissible exponents 2+δ for δ≥0, without equating leading constants.

The covariance integral on [AX,2BX]² retains all t,u coordinates used
by w(t/x)w(u/x); its Gram positivity does not make its individual cross
terms positive. The atom band is larger only in the separate averaging
error estimate, not in this t,u integration domain.

For h=X^τ, the proposed raw bound gives exactly
O(X^(3-κ)L(X)+X^(4τ-1)). Every
δ>max(0,1-κ,4τ-3) follows. The strict inequality is sufficient but
occasionally stronger than necessary: if 4τ-3 dominates strictly over
1-κ, that frontier endpoint also follows. An unbounded subpower L
prevents asserting an endpoint controlled by the first term. The
manuscript can safely use the simpler strict formulation. At τ=3/4,
κ≥1 implies every positive δ and hence RH, while κ=1 and unbounded L
does not directly give the δ=0 bound.

## Generic finite-prefix model

The construction is valid with N=max(N₀,8). For
M(x)=x+η Re(x^(β+iγ)/(β+iγ)), 1-η≤M'(x)≤1+η<2.
Set F(x)=S_N+M(x)-M(N). Starting from S_N=F(N), choose c_n=log n
when S_(n-1)<F(n) and c_n=0 otherwise. If d_n=F(n)-F(n-1),
then 0<d_n<2. In the insertion case the new excess belongs to
(log n-2,log n), and is positive since n≥9; without insertion it
lies in [0,log(n-1)]. This proves 0≤S_n-F(n)≤log n. Passing to
real x costs at most 2 in F, so ψ̃(x)=M(x)+O(log x), with a fixed
prefix-dependent offset absorbed in that error.

An economical response proof works directly with Ṽ. Put α=δ/2 and
β=1/2+α. Full-support Stieltjes integration gives

Ṽ(x)=η Re[G(-α-iγ)x^(β+iγ)]+O(log x),

because ∫w=0 and
∫w(u)u^(β+iγ-1)du=G(1/2-β-iγ). The tracking-error contribution is
O(log x) after integration by parts; w vanishes at both endpoints.
The coefficient is nonzero by the probe's noncancellation lemma.

With λ=2+δ and ℓ=log 2, the leading normalized shell factor is
Q(θ)=∫₀^ℓ e^(λt)cos²(θ+γt)dt. Its minimum is

½{(e^(λℓ)-1)/λ - |(e^((λ+2iγ)ℓ)-1)/(λ+2iγ)|}>0.

The strict inequality follows because e^(2iγt) is not constant almost
everywhere on an interval when γ≠0. The cross and squared errors are
O(X^(3/2+δ/2)log X+X(log X)²), both smaller than X^(2+δ).
The resulting two-sided variance bound holds for every sufficiently
large real X.

For the diagonal, define Ã₂(t)=Σ_(log n≤t)c_n²/n. Only after t≥log N
may the exact identity
Ã₂(t)=∫_(2−)^(e^t)(log u/u)dψ̃(u)+C_N
use a single fixed prefix correction C_N. Partial summation gives
Ã₂(t)=t²/2+C+o(1): the endpoint error is
O(t e^(-(1-β)t)) and the error integral converges because β<1.
Defining D̃(Y)=∫₀^YΣ c_n²g(y-log n)²/n dy, finite interchange gives
D̃(Y)=∫g(v)²Ã₂(Y-v)dv. Since log 2>a, no lower packet cap is lost.
The normalization and evenness of g² give D̃(Y)=Y²/2+O(1).

The model preserves PNT, the fixed probe identities, the diagonal scale
and any finite coefficient prefix. It does not preserve actual
prime-power support or assert an Euler product. Its obstruction applies
only to a rule based on these retained generic controls. The β=1
endpoint is unnecessary and invalid for the stated PNT and diagonal
remainder argument.

## Fresh pass on the manuscript

On 4 October 2026, read the actual text of Sections 4–6 and Appendices
A–B of [manuscript.tex](../manuscript.tex), including their dependencies
on the stated transform convention. No substantive arithmetic correction
was needed. In particular:

- The baseline uses the full supremum on [AX,2BX] and squares the PNT
  envelope with the correct constants and asymptotic interpretation.
- The finite theorem retains the linear sixth-power tail, both signs of
  zero ordinates, the unrestricted-y response envelope, and exact full
  shell integration. All three continuous ranges follow by monotonicity.
- The covariance identity, expanded atom band, real X/h quantifiers,
  approximation constant, exponent table, and frontier qualifications
  agree with the independent derivation above.
- The finite-prefix model has the correct plus-transform amplitude
  G(-α-iγ), uniform positive phase minimum, smaller error terms, and
  correctly qualified exact diagonal identity. Its scope is explicitly
  generic and does not claim an actual-prime obstruction.

The Saffari–Vaughan reduction was additionally checked against the
[primary paper](https://aif.centre-mersenne.org/item/10.5802/aif.649.pdf),
Section 6. Its proof establishes the relative ψ estimate before passing
to θ. The manuscript's averaging argument applies directly to ψ; its
factor 12 is a safe upper bound. With density exponent 12/5 and margin
1/12, the relative lower threshold is U^(-3/4), while the required band
starts at a constant times X^(-1/4). The three shifted dyadic intervals
cover the complete t-band. The resulting saving remains subpower.

Reopened the [Platt–Trudgian theorem](https://arxiv.org/pdf/2004.09765):
its exact verified height is 3,000,175,332,800, so the manuscript's phrase
“exceeding H” is justified at H=3×10^12. Also checked the displayed
[Hasanalizade–Shen–Wong Corollary 1.2](https://arxiv.org/pdf/2107.06506)
against the primary text: its constants and range T≥e match Appendix A.

Using a fresh elementary Python calculation with exact fractions,
independently reconstructed the polynomial g₀ and verified its stated
norm, sixth-derivative squared norm, endpoint-atom mass, and integer
upper majorant. Independently checked the three exact rational budget
fractions and all five source hashes printed in Appendix A. All passed.
This did not regenerate the outward zero enclosures; those remain
identified imported input records.

The pass caught three missing closing equation environments, after the
probe, response, and finite-theorem displays. These were communicated to
the drafting agent and their repair was verified in the source. Two
minor precision edits were recommended: explicitly require real γ≠0
in the model proposition, and show the dependence on the fixed ceiling C
in the height-law comparison constant. Neither changes a proof or a
claimed conclusion. Compilation and the complete central-theorem review
are recorded by the other manuscript checks.

The reviewed source after the equation-environment repair had SHA-256
`1f3161ebd74681128b6e4e560aa50cb2c27d00fd5ac501c6f78a03ae355232d8`.
Subsequent source hashes may differ after the two precision edits or
layout repairs; this identifies the actual text used for this pass.
