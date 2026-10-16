# Direct positive approximation of the arithmetic form

29 September 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); exact serving variant and configured reasoning effort
are not exposed and are not inferred. This is an internally checked research
continuation, not independent specialist review. No new numerical certificate
or manuscript is claimed.

## Objective and change of priority

Construct a specified family of independently positive forms P_j such that

\[
P_j[F]\ge0,\qquad P_j[F]\longrightarrow Q[F]
\]

for every fixed compact smooth pole-neutral source F. The sources range over
arbitrarily large supports. Positivity must follow from the construction;
arithmetic identification of the limit is a separate theorem. Neither a
finite-stage domination inequality nor monotonicity is required.

The odd-source mean-zero domination test is no longer a prerequisite.
It tests a stronger comparison that a successful convergent family need not
satisfy. The earlier source, projection, scalar, and moment certificates remain
available for calibration of a stated asymptotic mechanism. Further moment
calculations require a demonstrated role in that mechanism.

The same-support preparation is F=P0 h, P0=-d^2/dx^2+1/4, h compact smooth.
It is exactly onto the pole-neutral class, as proved in the
[canonical audit](SONIN_CANONICAL_COMPARISON_AUDIT_20260929.md). A common
source-independent approximation family is sought; parameters must not be
chosen by fitting each source to its already-known arithmetic answer.

## The first candidate and its exact identification problem

Let S_R contain the real place and primes at most R. With the actual
orthogonal projection Pi_R onto D_R K, where

\[
D_R=\prod_{p\le R}(I-p^{-1/2}U_{\log p}),
\]

the existing positive family is

\[
P_R[F]=\mathcal B_{S_R}[F]=\|C_F\Pi_R\|_{\rm HS}^2.
\]

The inverse compressed metric is part of Pi_R and cannot be omitted.
For a fixed pole-neutral source, the full prime-power sum W[F] has only
finitely many nonzero terms, and the audited comparison reads

\[
P_R[F]-Q[F]=\mathcal E_\infty[F]+\Delta_{S_R}[F]+\mathcal W[F].
\]

Thus the required limit is

\[
\Delta_{S_R}[F]\longrightarrow
-\mathcal E_\infty[F]-\mathcal W[F].
\tag{1}
\]

This is an exact target, not a derived convergence theorem. Adding inactive
places can still change P_R. Their cumulative geometric effect must be
controlled and identified; summability to an unknown limit would not prove
(1). An increasing numerical trial space at fixed R only resolves P_R and
does not perform this arithmetic limit.

## Analytic results from the first direct limit investigation

### Positive frequency measures and a restriction on the final realization

For each fixed projection P for which all the smoothed traces are finite,
there is a positive frequency measure

\[
\nu_P(J)=\operatorname{Tr}(P E_JP),\qquad
\|C_FP\|_{\rm HS}^2=\int|\widehat F(t)|^2\,d\nu_P(t),
\]

where E_J is frequency restriction. This measure is locally finite and
absolutely continuous with respect to Lebesgue measure. Closed graph and
modulation arguments show polynomial growth when all prepared compact
sources are admitted.

A fixed bounded compression on ordinary logarithmic L2 cannot realize Q
on every pole-neutral source at all supports. Assuming such an identity
first implies RH by the restricted criterion; the explicit formula would
then identify the measure with the nonzero atomic zero-counting measure.
Polarization on prepared sources makes that identification unique, contradicting
absolute continuity. The proof is in the
[topology note](SONIN_POSITIVE_LIMIT_TOPOLOGY_20260929.md), and is a scoped
version of the program's existing no-closable-factor obstruction. It is not
an obstruction to limits of positive forms.

A simple model shows the permitted behavior: rank-one projections onto
frequency packets of shrinking width tend strongly to zero, while their
smoothed traces tend to |Fhat(gamma)|^2. Spectral concentration can carry
a nonzero limit even when the state-space projection limit is zero.
Consequently the program must not demand convergence to a single fixed
ordinary L2 compression, or uniform state-space trace compactness that would
force that outcome.

A useful sufficient route instead is convergence of positive frequency
measures on compact frequency sets together with tail control weighted by
|Fhat|^2 for each fixed source. The limit must be identified from the arithmetic
expression. It must not be defined using an assumed real-zero spectrum.

### A regularized infinite-place family

For fixed sigma>1, replace the prime coefficient by p^(-sigma). The products

\[
D_{R,\sigma}=\prod_{p\le R}(I-p^{-\sigma}U_{\log p})
\]

and their inverses converge in operator norm to bounded invertible operators.
The compressed metrics retain a positive lower bound, and the source-smoothed
isometric factors converge in Hilbert–Schmidt norm. This constructs an
unconditional positive infinite-place form B_sigma for every sigma>1.
It is a controlled baseline, not the arithmetic endpoint: no identity with
Q follows, and the fixed-compression obstruction precludes a global equality
at a fixed sigma in this regime.

### A phase continuation with a singular endpoint

The regularized construction has a bounded phase formulation. Let R_+ be
restriction to positive logarithmic position, J logarithmic reflection, and

\[
m_\infty(t)=\frac{L_\infty(1/2-it)}{L_\infty(1/2+it)}.
\]

Define a unitary involution on the Fourier side, almost everywhere, by

\[
\mathscr F_\sigma
=m_\infty(t)\frac{\zeta(\sigma-it)}{\zeta(\sigma+it)}J,
\qquad
\Pi_\sigma=\operatorname{proj}
\bigl(\operatorname{Ran}R_+\cap\mathscr F_\sigma\operatorname{Ran}R_+\bigr).
\tag{2}
\]

Isolated zeros or poles affect only null sets in this multiplier definition.
No half-plane innerness or zero-free claim is used. For sigma>1 this projection
agrees with the regularized transported Sonin projection. For 1/2<sigma<=1,
(2) is a definition; bounded inverse-Euler transport is not inherited from
the sigma>1 proof. The later
[frequency-tail theorem](SONIN_PHASE_FREQUENCY_TAILS_20260929.md) separately
proves full source-smoothed trace finiteness for every sigma>1/2.

The functional equation cancels the phase at sigma=1/2, giving
F_(1/2)=J. Hence the endpoint intersection is zero. Moreover F_sigma tends
strongly to J and Pi_sigma tends strongly to zero as sigma decreases to 1/2.
This result does not decide the smoothed trace limit. It identifies the
critical limit as singular and excludes interchanging it with a continuous
fixed-state trace realization. The detailed construction and proof are in the
[regularization note](SONIN_REGULARIZED_POSITIVE_FAMILY_20260929.md).

The phase path is a separate candidate from R->infinity at the physical
coefficient p^(-1/2). No theorem equates those limiting procedures.

### Finite-rank positive forms and the now-established full traces

Fix source-independent finite-rank orthogonal projections E_N increasing
strongly to the identity. The forms

\[
P_{\sigma,N}[F]=\|C_F\Pi_\sigma E_N\|_{\rm HS}^2\ge0
\tag{3}
\]

are finite for every compact smooth F. Their N->infinity limit is B_sigma
for every sigma>1/2, now known to be finite by the separate frequency-tail
theorem. They remain useful as approximants, but are no longer necessary
merely to define finite forms.

For each fixed N, P_(sigma,N)[F] tends to zero as sigma decreases to 1/2,
because Pi_sigma E_N tends to zero in Hilbert–Schmidt norm. A nonzero
arithmetic limit therefore requires a coupled growth N=N(sigma)->infinity.
Existence of a schedule with the correct limit has not been established.
This is a concrete family to study, not a successful arithmetic approximation.

### A conditional convergence mechanism for the raw place sequence

The [place-tail analysis](SONIN_DIRECT_PLACE_TAIL_CRITERIA_20260929.md)
bounds the exact signed prime increment using source-weighted spatial tails
at a moving cutoff log p. It supplies both an absolute sufficient condition
and a less restrictive condition retaining cancellation of the signed leading
terms. Those hypotheses are not proved uniformly along the growing-place
Sonin family. The result explains which new estimate could establish
convergence of the raw positive family; it does not identify its limit with Q.
A moving spatial cutoff is compatible with spectral concentration and must
not be replaced by uniform tightness at a fixed spatial cutoff.

## Next work and decision points

The [phase boundary derivation](SONIN_PHASE_BOUNDARY_TRACE_20260929.md)
now supplies the requested representation for sigma>1, including the
independently represented correction, its archimedean calibration, and a
controlled return expansion. The subsequent
[critical-limit synthesis](SONIN_CRITICAL_LIMIT_STATUS_20260929.md)
closes full source-trace finiteness, uniform weighted tails, and arithmetic
crossing bookkeeping. The actual projection can still lose critical-line
mass through its return operator. An exact rational model shows that local
phase factorization and a positive prelimit gap do not rule out total loss.

1. Determine a global property of the actual zeta phase that controls its
   return mass near cutoff spectral value 1, or shows a nonzero defect.
   Return mass away from 1 and the other boundary terms now vanish in the
   critical limit. The remaining step must distinguish approximate kernel
   vectors from the exact intersection; local phase information is insufficient.
2. Prove an arithmetic comparison with an error tending to zero on each fixed
   prepared source. One sufficient formulation is convergence, as distributions
   on compact correlation tests, of the independently constructed kernels to
   the fully prepared gamma/contact-minus-prime distribution. Preserve the
   exact normalization and all active prime powers. This is the decisive open
   lemma, not a consequence of convergence to an unidentified positive measure.
3. Phase-family tails are proved. Any needed parameter schedule for (3)
   must resolve the remaining exact-kernel loss; fixed N still gives zero.
   Fixed Abel parameters instead recover the critical-line zero measure,
   which omits the signed off-line pairing. For the raw place family,
   investigate its still-unproved moving-tail or signed-sum conditions.
4. Use numerics only to discriminate a stated concentration, tail, or
   discrepancy mechanism. The two existing sources are calibration probes.
   Resolve their finite-stage residual signs only if the chosen asymptotic
   argument actually requires that information.

An analytic result on a dense prepared-source class, including linear
combinations, would already imply positivity of Q on all sources by its
known fixed-support continuity. To prove convergence of the positive forms
on every source from dense-class convergence, additional equicontinuity
would suffice. These are different obligations; finitely many source tests
establish neither.

If the raw family converges to the wrong object, revise the family or the
geometric cutoff rather than demand that its finite remainders become
nonnegative. The regularized phase family now has finite smoothed traces
and weighted tail control. If its exact projection loses the needed mass,
retain those results and assess another positive construction. This would
not close the general positive-approximation program.

## Current assessment

The direct program now has a precise arithmetic-limit target, a controlled
regularized positive baseline, a well-defined finite positive phase family,
and a restriction identifying why the critical limit cannot be an ordinary
continuous trace of a fixed final projection. These are analytic advances
in the construction and choice of topology. They do not prove the needed
arithmetic limit, an all-source sign theorem, or RH. See the
[internal review](../reviews/SONIN_DIRECT_LIMIT_REVIEW_20260929.md).

The immediate priority is arithmetic identification of a concentrating
positive family. CCM remains temporarily closed. Existing numerical records
are preserved; this stage adds analysis and the revised plan, not a new
numerical certificate, manuscript snapshot, commit, or push.
