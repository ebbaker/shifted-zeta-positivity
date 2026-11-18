# VCD-GT-CM-E16 r1 — Common-time finite-divisor approximation

18 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance. Actual model/effort unavailable; B05 helper
settings inherited. Type **E**, recommended **Sol**: the approximation,
proof mechanism, domain and acceptance test are fixed below.

**Frozen, ready contract; not executed in the B05 discussion.**
[B05 Note15](../../notes/15_VCD_GT_CM_B05_BBGKY_TRUNCATION_RECONSIDERATION_20261118.md)
selects a finite-divisor realization, distinct from a moment-order cutoff.
The sole register owns live status. A new numerical campaign is not needed.

## Inputs and target

Read root GPT_RESEARCH_MODEL_WORKFLOW.md, LARGE_FILES.md, result/avoid
indexes, controls12, and CM Note09/manuscript Section 1 plus Note15.
Verify the seven [frozen input identities](VCD-GT-CM-E16-inputs-r1.json)
before execution; their paths are repository-relative.
Preserve H_t=-H_zz, complete canonical initial source, a fixed height T,
fixed ell, a fixed independently paid tube I=[t0,t1], both D signs,
multiplicities and independent gap anchors. Do not alter existing proofs.

At t0 define P_N by truncating H(t0,0)'s opposite-paired canonical product
at modulus N, keeping all ties, conjugates and occurrences. Evolve the
same polynomial from t0 throughout I by exp(−(t−t0)partial_z²).
N is a divisor cutoff, not the number P of retained S/T moment orders.

Prove a quantitative compact-space/common-time approximation, with errors
for spatial derivatives through order three, followed by the transferred
count-two coordinates and each fixed S_n,T_n. The intended field error is
`C_j E_N`, where E_N is the omitted opposite-pair inverse-square sum,
`E_N=O(log N/N)`, and C_j is explicit in the fixed input constants.
If this rate requires a bounded local correction, retain the actual proved
rate and explain the loss; do not claim it from qualitative convergence.

## Fixed proof route

1. Prove an N-independent initial envelope
   `G(r)=C exp(C(1+r)log(2+r))` using the complete unit count, strip,
   finite near-zero factors and H(t0,0). List exactly which initial
   divisor information and constants must be supplied; theoretical exact
   canonical data are not a certificate that those data have been acquired.
2. Bound the initial product remainder by
   `G(|z|)(exp(|z|² E_N)−1)`. Keep the convention of one representative
   per opposite pair consistent with the complete count and tail bound.
3. Derive the Gaussian imaginary-shift formula for the polynomial and for
   H from its unchanged source. For tau in [0,t1−t0], prove domination
   uniformly on |z|≤R. One explicit route uses E_N≤eta with
   `eta=1/(16(1+t1−t0))` and
   `exp(r² E_N)−1≤E_N r² exp(eta r²)`.
   The finite Gaussian integral of `r²G(r)exp(eta r²)`, with
   `r=R+sqrt(2(t1−t0))|X|`, gives a proposed constant. Prove its finiteness
   and an explicit bound from the envelope; do not merely invoke dominated
   convergence to claim a rate. A near/far Gaussian split is an allowed
   bounded repair, with both cutoffs and tails paid.
4. Use Cauchy estimates on an enlarged disk for spatial jets. Cover the
   independent canonical tube by finitely many cleared contour charts.
   Quantify the field-error threshold for Rouché, then c_N,D_N from
   contour moments, and the perturbed rational kernels for fixed S_n,T_n.
   Include target and exterior mergers. No global strip for evolved P_N
   or tracking of individual root labels is needed or to be assumed.
5. Transfer errors to m,F, log W and the inhomogeneous cost, including
   the physical ell² factor. Compare with direct residues given exactly
   the same finite divisor and errors. No stronger sign, cost advantage,
   uniform-height claim or tube/anchor acquisition follows automatically.
6. State the finite-dimensional closure meaning via polynomial coefficients
   (and, if useful, finite-divisor recurrences). It is not a theorem that
   a prescribed short moment head determines the canonical omitted tail.
   Count the required finite initial data and state how supplied data
   errors enter; no computation of canonical zeros is part of this packet.

## Boundaries and return

One analytical proof pass and at most two local repairs of constants,
domination or contour transfers. A changed source, evolution sign,
finite approximation, limit regime or required new mathematical premise
returns to B05 before dependent work. No arbitrary-sequence well-posedness,
statistical projection, short memory, positive moment matrix or all-real
exterior is an input. No simultaneous N/T/order limit is inferred.

Save the proof in notes, a compact input/error record in numerics if needed,
and an execution return here. Arrange a bounded nonauthor internal assessment
before promoting the theorem into the established-results summary; register
that assessment when its proof inputs exist. Completion is a fully paid
fixed-height approximation theorem, or a precise failed step within this
fixed method. It is not an improved canonical signed bound or RH claim.
