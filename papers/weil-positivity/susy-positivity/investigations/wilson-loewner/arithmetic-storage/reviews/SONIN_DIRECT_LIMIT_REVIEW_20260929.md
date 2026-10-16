# Internal crosscheck of the direct positive-limit investigation

29 September 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); exact serving variant and configured reasoning effort
are not exposed and are not inferred. This is a separate same-model
mathematical crosscheck, not independent human or specialist refereeing.
No numerical calculation or new numerical certificate is part of this review.

## Verdict and reviewed scope

The [main program note](../notes/SONIN_DIRECT_POSITIVE_LIMIT_PROGRAM_20260929.md),
[topology note](../notes/SONIN_POSITIVE_LIMIT_TOPOLOGY_20260929.md),
[regularized-family note](../notes/SONIN_REGULARIZED_POSITIVE_FAMILY_20260929.md),
and [moving-tail note](../notes/SONIN_DIRECT_PLACE_TAIL_CRITERIA_20260929.md)
pass this internal mathematical and scope check. No required mathematical
correction was found. This review checks the displayed operator arguments
and their stated consequences; it is not an exhaustive literature or novelty
review. In particular, it does not certify an arithmetic limit or RH.

## Regularization and the critical endpoint

For fixed sigma>1, absolute convergence of the prime coefficients gives
operator-norm convergence of the transports and their inverses. The stated
uniform compressed-metric gap, inverse-square-root estimate, and
Hilbert–Schmidt convergence of the smoothed isometries follow. The resulting
positive trace operators converge in trace norm. These claims are justified
only within the stated absolute-convergence region.

The phase signs are consistent with the stated Fourier convention:

\[
\mathcal F_\sigma
=\frac{L_\infty(1/2-it)}{L_\infty(1/2+it)}
 \frac{\zeta(\sigma-it)}{\zeta(\sigma+it)}J.
\]

This is a unitary involution almost everywhere. At sigma=1/2 the functional
equation cancels its multiplier, without a zero-location assumption.
Consequently the endpoint involution is logarithmic reflection and the
endpoint positive-half-line intersection is zero. Strong convergence of
the involutions implies strong convergence of the intersection projections
to zero: if Q_sigma=F_sigma R_+ F_sigma, then
0<=P_sigma<=R_+ Q_sigma R_+ and the upper bound tends strongly to zero.

The notes correctly do **not** infer vanishing smoothed traces from this
strong collapse. For 1/2<sigma<=1 they also do not inherit trace finiteness,
bounded inverse transport, or convergence from finite-prime Euler products.
The finite-rank forms ||C_F P_sigma E_N||_HS^2 are always finite and positive,
but tend to zero at fixed N. A nonzero limit must use unbounded rank through
a justified joint prescription or order of limits. None is established here.

## Moving-tail increment estimates

The finite-place involution F_S=D_S F_infinity D_S^{-1} is unitary and
reverses translations. Causal invertibility preserves the positive
half-line in both directions, so the transported Sonin projection satisfies
both cutoff constraints and commutes with F_S.

For real F, W=P_S C_F^* C_F P_S commutes with that involution. The two cutoff
constraints independently control the two translated terms in
T=P_S(U_a+U_{-a})P_S/2, proving

\[
\operatorname{Tr}(T^2W)\le\operatorname{Tr}(E_aW)=B\,i_S(a).
\]

The output overlap estimate uses the actual source-smoothed output support
[-b,infinity), and thus the stated cutoff a-b is correct. Splitting the
compressed resolvent once gives the stated sign and remainder:

\[
\delta_p^S/B=-\beta c_{S,p}+e_{S,p},\qquad
|e_{S,p}|\le\frac{\beta^2}{1-\beta}
\bigl(\sqrt{i_S(\log p)}+i_S(\log p)\bigr).
\]

In particular, ||T V^*||_HS^2=Tr(T^2W); the other remainder is controlled by
the positive operator (I-beta T)^{-1}T^2. No unproved commutation of T and W
is needed. The absolute summability criterion and the signed multiplicative
criterion both follow. The latter uses convergence of the normalized
increment series and its squared series before passing to logarithms.

These estimates are uniform algebraic statements for finite S. Their
required diagonal tail or signed-covariance hypotheses along the growing
prime family remain unproved. Fixed-S trace-class tails give neither a
uniform rate nor prime summability. The notes preserve that distinction.

## Topology and arithmetic scope

The fixed-compression obstruction is correctly scoped to ordinary bounded
compressions on the whole logarithmic L2 space, with every prepared compact
source admitted. Absolute continuity of the frequency measure, its
polynomial growth obtained by closed graph and modulation, and uniqueness
by polarization and a compact approximate identity justify the contradiction
with the atomic measure forced by an assumed global identity with Q. The
argument first derives RH from that assumed identity; it does not assume RH
to define the proposed approximants. Its relation to the existing
no-closable-factor result is expressly acknowledged.

The rank-one concentration example correctly shows why a zero strong
projection limit can coexist with a nonzero smoothed trace limit. Thus
ordinary state-space trace compactness is an unsuitable mandatory endpoint
condition. The proposed frequency-measure convergence and source-weighted
frequency tails are sufficient conditions, still to be proved for an
arithmetic family. The separate moving spatial cutoffs in the place-tail
criterion do not impose uniform capture at one fixed spatial cutoff.

Finally, all notes distinguish convergence of positive forms from identifying
their limit with the complete arithmetic form. The raw prime-cutoff family
and the analytically continued phase family are separate candidates; no
theorem equates their limiting procedures. Dense-class positivity of Q can
extend by Q's fixed-support continuity, whereas extending convergence of the
approximants requires additional control. Finite test computations prove
neither assertion. The main note's revised priority and its remaining open
obligations accurately reflect the results checked here.
