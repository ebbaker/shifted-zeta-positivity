# Review of positive continuous controls in the reference theta norm ball

20 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Reviewing model **gpt-6-astra (Codex)**;
reasoning effort **ultra**, inherited from the parent configuration
and verified there from recorded metadata.

**Assessment: accept the scoped analytic strengthening in
[Note 03][note].** This is a **separate same-model internal mathematical
review**, not author self-review, cross-model review, independent
implementation or specialist review. It closes the positivity and
actual-threshold repair of the selected Gram relaxation. It does not
supply an opposing theta sign or activate BW2-04/05.

The reviewed note has SHA-256
`140302f158a4959c81b796c592cf003ed0ffdc51a656009d05f5f687e9f86fca`.
Its [input receipt][receipt] identifies the inherited files and
parent revision `06acae6a0aba05b8f44ea8609bd7c7986029d9d5`.
The review also consumed the finalized [Gram note][gram] and
[profile note][profile], their stated control sources,
[result summaries][results], [collision-control summary][controls]
and [patterns to avoid][avoid]. Hashes bind text versions and do not
prove mathematical validity.

## Mathematical verification

The convolution normalization is correct. The symmetric atomic
probability measure has Fourier transform
\((\cos(\lambda z)+q)^2/(1+q)^2\). The triangular probability
density on \([-2\kappa,2\kappa]\) has transform
\(\operatorname{sinc}^2(\kappa z)\). Convolution therefore gives
their product. Its half-line density is twice the even whole-line
density; after convolution there is no zero atom whose mass needs
separate treatment. The resulting density is continuous,
nonnegative, piecewise linear, bounded by \(1/\kappa\), and has the
stated common support. It is not asserted to be smooth at its knots.

The reference-theta change of measure is exact. The positive first
theta summand gives the uniform density floor on that compact
support. Consequently the squared ratio norm satisfies
\[
 1/N_U\le I_q\le1/(\kappa m_\theta).
\]
The upper inequality uses \(f_q^2\le f_q/\kappa\) and the complete
mass-one integral. The lower inequality is Cauchy--Schwarz on the
support. The stated scaling therefore produces bounded continuous
nonnegative multipliers with the exact reference norm \(M_0\).
Their independent own-source moment budget is correct. The argument
does not misidentify the reference Gram matrix as a Gram matrix
under the control's own measure.

The threshold proof extends legitimately from finite modes to a
compact continuous source. The threshold slice is an even entire
function of exponential type whose explicit real zeros give a
paired canonical product and a Laguerre--Pólya approximation.
The factors \(1\pm v\partial_z\) preserve that class. Bounded
spectral support gives locally uniform convergence of
\((1-s\partial_z^2/n)^n\) to the exact heat-weighted integral.
The limit is nonzero at zero and has only real zeros at every
later time. The exact double event creates nonreal roots immediately
before the designated time. Were any earlier slice all-real, its
even order-one product and the same forward preservation would
contradict those predecessors. Thus the designated positive time
really is the all-real threshold.

The event curvature has the correct positive factors and is nonzero
for \(q<1\). Logarithmic differentiation after deflation gives the
additive jet contribution
\[
 2\kappa^2\csc^2(\kappa a)-2/a^2>0
 \quad\text{when }\kappa a=1/2.
\]
Combined with the inherited atomic formula, it proves the stated
inverse-\((1-q^2)\) lower bound on \(S_2\). The resulting
\(Q_L=18h_2^2(S_2-L)>0\) holds for every fixed finite \(L\) after
the specified choice of \(q\). It is a statement about the actual
changed-source heat field. It does not identify the positive-cone
optimum with the signed spectral maximum of Note 02 or give a
uniform positive raw margin.

The strict mass defect is essential and correctly paid:
\[
 \langle w_q,1\rangle=c_q\le\sqrt{M_0N_U}<M_0.
\]
It is uniform over the family, so these controls fail every tighter
approximate mass anchor as stated. Exact theta mass together with
the same norm budget would force the singleton \(w=1\). No part of
the construction evades that equality case.

The finite-profile smoothing corollary preserves the relevant
observations by an explicit formula. Multiplication by the fixed
sinc-square factor preserves event normalization and adds its
known logarithmic derivative to every profile sample. It also adds
the positive deflated-jet term above. Thus the common exact profile
samples, genuine threshold and unbounded normalized jet persist
for complete continuous compact-source controls. A common small
scale preserves a fixed control mass and the reference norm
inequality; individual norm-equality scaling instead changes that
mass. These are distinct normalizations, and neither supplies the
theta mass anchor.

## Scope, novelty and acceptance

The earlier atomic source is not an \(L^2(\nu_\theta)\) multiplier.
Smoothing plus the proved density-ratio bound repairs that specific
missing premise. The construction also repairs positivity and a
genuine-threshold requirement missing from Note 02's abstract signed
witness. It therefore strengthens the obstruction to that estimator
class rather than merely adding another unrelated control.

The new controls still have changed coefficients, compact support,
bounded imaginary-axis profile and infinitely many threshold
events. Their mass differs from theta's by a stated uniform amount.
The continuous-source corollary does not merge these controls with
the polynomial profile family's eventual simplicity at the
threshold, nor with Euler-factor controls' full large-height floor.
The failed premise list remains necessary.

The proof uses complete analytic sources, not a theta truncation.
It has no numerical source acquisition, unbounded tail omission,
approximate event or physical exclusion margin. The exact
theta-reference floor only proves finite conditioning; it is not
presented as a measured numerical constant. No new numerical
certificate is needed or claimed.

Accept Note 03 as an additional **closed scoped attempt** within
BW2-01/02, with a linked BW2-03 continuous-source corollary.
No useful opposing theta estimate follows. A continuation must
retain quantitatively distinguishing coefficient-level or affine
information, or actual theta profile values that exclude the
constructed families. Positivity, continuity and genuine-threshold
conditions alone do not repair the particular reference norm
relaxation analyzed here.

[note]: ../notes/03_POSITIVE_MULTIPLIER_GRAM_EXTENSION_20261020.md
[receipt]: ../numerics/POSITIVE_MULTIPLIER_INPUTS_20261020.json
[gram]: ../notes/02_EVENT_CONDITIONED_THETA_GRAM_OBSTRUCTION_20261020.md
[profile]: ../../04_boundary_winding/threshold_routes/08_deflated_jet_hierarchy/notes/05_FINITE_PROFILE_CONDITIONING_OBSTRUCTIONS_20261020.md
[results]: ../../../../../result-summaries/README.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../avoid/README.md
