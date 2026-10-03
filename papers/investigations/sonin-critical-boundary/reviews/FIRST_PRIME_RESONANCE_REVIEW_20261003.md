# Independent internal review of the first-prime resonance obstruction

3 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), in a separate same-model subagent reading; exact serving
variant and configured effort are not exposed and are not inferred.
This is an internal mathematical review, not independent human specialist
refereeing or a priority assessment.

Reviewed the complete [translated-resonance note](../notes/FIRST_PRIME_TRANSLATED_RESONANCE_20261003.md),
including its quantitative profile bound, higher-return strong-convergence
argument, and infinite-positive-index corollary. The final reviewed note has
SHA-256 `27d39da6fad7487be62a9c20241f86217e2449df1bd942d331c4a3993fe8da2f`.
The final reading verified its explicit real-polarization and
complexification step after a clarification during the audit.

## Verdict and exact scope

The argument passes this audit. It proves eventual positivity of the actual
first-prime boundary correction on exactly prepared, mean-zero sources in
any window of length greater than `log p`, with the prime set fixed to
`{p}`. For `p=2` and `log 2<L<log 3`, this is the support-adapted prime set.
Thus it refutes the proposed mean-functional domination at `L=1`.

The finite-dimensional extension also checks: the correction has positive
subspaces of arbitrarily large finite dimension, even after restricting to
either additive parity. Consequently no finite family of linear moment
penalties can dominate this correction form on the full prepared source
class at that first-prime support window.

This is an asymptotic existence theorem. No explicit dyadic threshold `N`,
finite numerical witness, or sign for the previously prescribed single odd
bump is established. The construction gives `K>0`, not `K>B`; it leaves the
weaker comparison `K<=B`, Weil positivity, and RH undecided.

## 1. First-return normalization and its actual operator meaning

The coefficient `c_n c_m/2` in the cutoff kernel follows directly from
integrating the product of two cosines. In the crossing trace, the change
`y=exp(u)x` contributes `exp(u/2)` after multiplication by the physical
source factor `(xy)^(-1/2)`. The defining `2 Re` trace then gives equation
(3). These checks verify the sign and every factor of two.

Near `u=log p`, the infinite resonant family is exactly `n=m+1`, `m>=0`.
Its coefficient is `2(1-1/p)^2>0`. The pair `(n,m)=(0,-1)` is a single
continuous contribution and cannot change the singular profile. The
sum-frequency terms are also nonresonant.

The logarithmic majorant in equation (4) is sufficient to identify the
kernel integral with the operator trace. Away from the finitely many
resonant families, frequencies are bounded below by a constant times
`p^max(n,m)`, giving a summable majorant. Along each resonant family,
`|sinc z|<=min(1,1/|z|)` gives an integrable logarithm uniformly over finite
truncations. Meanwhile the truncated products converge in operator norm,
and multiplication by the fixed trace-class crossing operator gives trace
norm convergence. Thus the two limiting calculations agree. The proof does
not assign a pointwise value to the kernel on a resonant curve.

At zero, the crossing interval has length `O(u)`. It multiplies the
logarithmic diagonal singularity, yielding `e_1(u)=O(u(1+|log u|))` and
continuity with value zero. This distinguishes the self contribution from
the translated one.

## 2. Higher returns and exact source conditions

The Schatten estimate is valid:

\[
\|C_n\|_3^3\le \|C_n\|\,\|C_n\|_2^2\le4p^{-n/2}.
\]

Its cube root is summable in `n`. Hence `C` belongs to Schatten class 3,
`C^3` is trace class, and the bounded gap inverse makes
`R=C^3(I-C^2)^{-1}T` trace class. No Hilbert--Schmidt claim about `C` is
needed. Both proofs of the higher-return limit are sound: the continuous
trace-pairing kernel, and the more direct strong-convergence argument for
this particular packet family.

For the latter, the displayed Fourier transform of the paired source is
uniformly bounded and tends pointwise to zero. Dominated Plancherel gives
strong convergence of its source multiplier and crossing compression to
zero. Pairing a uniformly bounded strongly convergent family with the fixed
trace-class operator `R` makes the trace tend to zero.

The preparation `F=(-d^2/dx^2+1/4)H` makes both pole moments vanish exactly
by integration by parts. The assumption `integral g=0` additionally gives
exact zero mean for every finite width, including the lower-order
`epsilon^2 g/4` term. The autocorrelation therefore has exactly zero
integral, not just a small numerical value. The two-packet support condition
`log p+2b epsilon<L` is sufficient and becomes strict for all large `N`.

## 3. Lacunary limit and positive sign

Reindexing the dyadic series gives equation (8) with an
`O(epsilon^2 z^2)` remainder. The constant `N` cancels against the exact
zero correlation mass. Freezing the prefactor and crossing endpoints costs
`O(epsilon(1+N))`, which tends to zero along `epsilon=p^{-N}`.

The nonlinear argument of the profile is uniformly comparable to the
rescaled correlation coordinate. The bound
`C(1+|log|w||)` is integrable on its fixed compact support and justifies
dominated convergence. The proof correctly avoids differentiating the
lacunary profile or replacing its log-periodic part by an unproved
continuous error.

The Fourier-average identity in equation (12) has the right normalization
for the Fourier convention in use. Each paired sinc term is nonnegative.
The negative-index terms are summable because the Fourier transform
vanishes at zero; the positive-index terms are summable by Plancherel.
The additional absolute-pairing estimate stated in the note legitimizes
pairing the original profile series itself. Nonzero compact smooth `f`
gives strict positivity.

I independently recovered the limit coefficient
`4(1-1/p)^2 sqrt(p)` and the energy bracket in equation (16). The two
symmetric source cross-correlations account for the final factor of two.
For `p=2`, the limiting constant lies between

\[
\frac{1}{2\sqrt2}\int_{\mathbb R}\frac{|\widehat f(t)|^2}{|t|}\,dt
\quad\text{and}\quad
\frac{1}{\sqrt2}\int_{\mathbb R}\frac{|\widehat f(t)|^2}{|t|}\,dt.
\]

These are positive finite bounds on the limit, not on the finite-width
remainder. Normalizing the source multiplies its positive correction by a
positive scalar and preserves the obstruction, although the normalized
correction tends to zero.

## 4. Infinite positive index, parity, and finite-rank penalties

The strengthened corollary is valid. For clarity, begin with a real
finite-dimensional space `G` of compact profiles of fixed support and
zero mean. Polarizing the asymptotic formula on basis vectors and their
real sums gives entrywise convergence of the real symmetric correction
matrix. The limiting form is a positive constant times `S_p[-g'']`.
The map `g -> -g''` is injective on compactly supported smooth functions,
so this limiting form is positive definite on `G`. In finite dimension,
entrywise convergence is norm convergence. Its smallest eigenvalue remains
positive for all sufficiently large common `N`.

The packet map has the same dimension as `G`: its two components have
disjoint supports at sufficiently small width, and the preparation
operator has no nonzero compactly supported kernel. A single sufficiently
large `N` can therefore satisfy both the support/disjointness conditions
and positive definiteness on the entire finite-dimensional image.

Complexification introduces no extra sign obligation. For real sources
`u,v`, the even source multiplier satisfies

\[
a_{u+iv,e}=a_{u,e}+a_{v,e},\qquad
K[u+iv]=K[u]+K[v].
\]

Thus the real positive form extends to a positive Hermitian form on the
complexified space. One may alternatively extend the asymptotic formula
to complex profiles before using complex polarization; imaginary sums
should not be invoked solely on a theorem restricted in wording to real
profiles without this elementary extension.

Both parity claims check. An odd derivative of an even bump supplies odd
mean-zero profiles, while second derivatives supply even mean-zero
profiles. Each parity sector contains arbitrarily large finite-dimensional
profile spaces. Equal packets centered symmetrically preserve the parity,
as does preparation.

Finally, on a complex positive subspace of dimension `k+1`, any `k` complex
linear functionals have a nontrivial common kernel by rank-nullity. A
nonnegative quadratic penalty in their values vanishes on that kernel,
whereas the correction is strictly positive. This rules out finite-rank
domination. The argument does not require continuity of the functionals,
a bounded operator realization of the prepared form on ordinary `L2`, or
uniform constants as the support grows. It already applies at the single
first-prime support window under discussion.

## 5. What the proof has and has not decided

The translated-resonance result supersedes the proposed all-source
mean-only test as a viable sufficient target: that target is false. The
infinite-positive-index corollary also excludes repairing this particular
strong comparison with finitely many linear moment penalties.

It does not determine the sign of the correction for the earlier fixed
odd bump, whose trial calculations remain exploratory and below the
falsification threshold. It supplies no explicit smallest width or `N`
for a computable witness. A numerical witness would require quantitative
remainder bounds and outward arithmetic at a specified finite width.
The remaining weaker arithmetic comparison must accommodate these positive
corrections instead of attempting to remove them with finite-rank penalties.
