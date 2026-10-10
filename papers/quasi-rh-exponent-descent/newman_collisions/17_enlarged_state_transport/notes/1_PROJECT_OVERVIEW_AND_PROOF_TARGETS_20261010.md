# Project 17: enlarged-state transport and heat-flow visibility

10 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6.1-sol (Codex), reasoning effort ultra, verified from the
recorded drafting-turn configuration. Derivations, computational checks,
and parallel reviews are internal LLM work, not independent mathematical
validation.

## The question

This project joins the full arithmetic state of program 09 with the
coherent phase-space state of program 13. Its purpose is to use their
simpler enlarged dynamics to prove that the genuine Riemann heat flow
cannot lose its value and slope simultaneously after reduction.

The scalar function is
\[
H_t(x)=\int_0^\infty e^{tu^2}\Phi(u)\cos(xu)\,du,
\qquad \partial_tH_t=-\partial_x^2H_t.
\]
Under the [parent collision reduction](../../newman_collision_reductions.tex),
which imports the de Bruijn--Newman threshold and effective large-height
facts needed to prevent escape to infinity, an RH counterexample would
produce a positive all-real threshold with a finite real multiple zero.
A direct exclusion of every positive-time joint zero of \(H_t,H_t'\)
is therefore a sufficient target under those inputs. The project initially
seeks a bounded theorem on a specified shrinking-time domain.

The existing threshold route studies a signed fourth-jet expression at
ordinary double zeros. Its complete Cauchy error payment can be large,
and higher multiplicities require further tests. The present project
prioritizes a first-jet visibility estimate. Such an estimate uses the
value and physical slope together, needs no all-real assumption, and
covers every multiplicity on its proved domain.

## Why retain the larger state?

Reduction conceals information. A positive bulk norm or energy can coexist
with cancellation of two scalar observations. The enlarged state keeps
the source preparation, transport between its components, and the signed
interference that the scalar readout compresses.

Program 09 realizes the finite arithmetic sum as a vector whose components
are the actual weighted phases at one physical height. Its bulk evolution
is diagonal and elementary. More information lies in its prescribed
divisor edges: multiplying an index by a prime has an exact weight and
phase transport factor. These edges, together with the anchored component
at index one, uniquely specify the genuine state. Constant twists obey
the same diagonal evolution but fail those same fixed edges. This gives
a concrete distinction between solving the bulk equation and preparing
the required arithmetic source.

Program 13 starts with the genuine positive wavefunction
\(\psi_t(u)=e^{tu^2/2}\sqrt{\Phi_e(u)}\). Its two-variable chord field is
\[
\mathcal A_t(k,\ell)=\int_{\mathbb R}e^{iku}
\psi_t(u+\ell/2)\psi_t(u-\ell/2)\,du.
\]
It obeys the simple equation
\[
\partial_t\mathcal A=(-\partial_k^2+\ell^2/4)\mathcal A,
\qquad \mathcal A_t(k,0)=2H_t(k).
\]
The scalar slice evolves autonomously. The transverse channels provide
additional overlaps whose restrictions must come from the prepared theta
state. In particular, transverse curvature is related exactly to the
oscillatory Fourier transform of the wavefunction's gradient energy.
This supplies a signed theta score observable which can be studied before
the final scalar cancellation.

Two further structures preserve arithmetic information during reduction.
The full angular theta field retains every Fourier coefficient and its
Jacobi gluing relation before taking a rotor trace. Its exact shifted
identity includes a boundary source. The stationary arithmetic transform
also becomes a reflection in logarithmic coordinates. Literal intervals
are paired with their reflected intervals, so the natural cutoff carries
an interior/exterior boundary coupling. These are possible ingredients
for an adjoint transport argument or a signed overlap estimate.

## What has been established

[Heat Note 25](../../notes/25_ENLARGED_STATE_TRANSPORT_CHORD_DYNAMICS_AND_THETA_GLUING_20261010.md)
establishes the divisor-edge and tangent identities, positive anchored
parent operator, exact chord and gradient-overlap equations, score-to-jet
dictionary, angular differential-shift identity, and reflection map. Its
companion exact checker validates finite algebra, including the anchored
Schur example and a positive-threshold control.

The main conditional certificate is already proved. Let the finite
physical observation be
\(Cq_R=(F/2,F'/(2L))\), where \(F\) approximates a nonvanishing
normalization of \(H_t\). An adjoint identity expresses the anchored
source covector through these two observations, divisor-edge equations,
the source phase condition, and a residual. If the full weighted residual
is bounded by \(R<1\), and the two observation multipliers have norm at
most \(Y\), then
\[
\|Cq_R\|_2\ge(1-R)/Y.
\]
The imported real-symmetric holomorphic error disk forces
\(\|Cq_R\|_2\le\eta/2\) at every genuine joint zero. Thus
\(R+\eta Y/2<1\) excludes that zero. A directional support version uses
the stronger correlated first-jet body.

The continuation in [Note 2](2_SHARP_ADJOINT_RESIDUALS_AND_RESTRICTED_PRIME_OBSTRUCTION_20261010.md)
constructs regular prime-division tree multipliers and proves that their
sharp pointwise residual is exactly the scalar observation defect.
It also proves that using only primes 2 and 3 cannot give a strict
residual gap for L at least 160 on the stated sector. A
[complete N=22066 cell](3_REGULAR_ADJOINT_CELL_CERTIFICATE_20261010.md)
now has a regular correlated certificate and paid margin greater than
0.5552583, conditional on the imported disk input. Its two global
coordinate hulls are inconclusive, although its forty subcells also
exclude by separate scalar tests. This is a bounded calibration.
Uniform multiplier bounds and a theta-specific signed correlation remain
open. Positive anchored energy supplies source coercivity; a uniform
observation estimate is still the missing theorem.
The [coordinate/IFT continuation](4_COORDINATE_INVARIANCE_AND_IMPLICIT_HEAT_FOLDS_20261010.md)
shows that ordinary collisions are regular folds in the time-height plane
and persist under small positive-density source perturbations. Passive
charts preserve the prescribed observation. A rescaled implicit chart
also proves a new conditional [two-sign criterion](5_STATIONARY_SIGN_CRITERION_AND_THETA_TARGETS_20261010.md):
on an open positive-time domain, the signs HH''<=0 when H'=0 and
H'H'''<=0 when H''=0 exclude every finite multiplicity. Their exact
theta overlap targets use D and D', and derivatives through order three.
The signs, predecessor coverage and genuine third-jet costs remain open;
fewer jets do not establish cheaper global estimates.
Purity and phase-space positivity also permit the bounded-time collision
control. Leading reflection preserves the existing threshold quadratic.
The four earlier finite zero atlases remain calibration data in
disconnected windows; their derivative tests already exclude joint zeros
on their surviving strips. The newer sparse pilots found no surviving
sampled joint candidate and do not certify interval coverage.

## The proposed proof milestones

1. **Construct one regular adjoint transport certificate.** Work on a
   closed physical cell with fixed cutoff. Use exact divisor telescoping
   and matched boundary channels to produce the multipliers and residual.
   Enclose their costs throughout the cell. An informative first success
   would resolve a cell where the existing separate value and derivative
   enclosures remain inconclusive.

   **Bounded calibration completed:** Note 3 gives such a cell for the
   separate global hulls. Note 2 proves that unrestricted pointwise
   optimization adds no information beyond the correlated first jet.
   The same recorded subcells pass scalar tests, so an arithmetic gain
   from the lift remains unproved.

2. **Control the multiplier growth on a shrinking family.** Seek uniform
   bounds \(R\le1-\delta\), \(Y\le C N^\alpha\), with
   \(\delta>0\) and \(\alpha<5/8\) on
   \(1\le\kappa=tL\le3/2\). Since
   \(\log N=\kappa/(2t)+o(1)\) and
   \(\eta\le5e^{-\kappa(\kappa+4)/(16t)}\), these bounds would make
   \(\eta Y\) tend uniformly to zero. Effective constants and a starting
   time would turn this implication into a theorem on the whole family.

3. **Estimate a complete theta gradient/score overlap.** Study the
   transverse curvature and score-square residual jointly. Their exact
   dictionary can feed either a complete first-jet current estimate or
   the density-strengthened threshold test. All quantities must come from
   the same physical state, with candidate conditions imposed only on the
   complete readout. The aim is a signed correlation, rather than separate
   absolute bounds reproducing the current error loss.

   **Precise alternative target:** Note 5 gives two signed correlations on
   the complete stationary sets of H and H'. If proved on a predecessor
   neighborhood with the printed physical-jet payments, they exclude all
   finite multiplicities without an all-real hypothesis. The rescaled IFT
   proof and 1,819 exact algebra assertions are complete; the theta signs
   and a genuine stationary-set cover are not.

4. **Use angular gluing when the source estimate needs more arithmetic
   data.** Preserve the genuine theta coefficients, modular partner, and
   endpoint source. First bound the growth and error cost of the fixed
   complex shift, which lies outside the existing small approximation
   disk. Then identify a boundary or angular identity that improves one
   of the first three milestones.

## Failure tests and later coverage

A proposed multiplier construction must stay regular when both observed
coordinates vanish. Dividing by those coordinates, or by their unknown
common-zero determinant, would presuppose visibility. Keeping only edges
for the primes 2 and 3 leaves disconnected source sectors; their costs
must remain explicit. Eliminating hidden coordinates is valid only after
their invertibility and source terms have been established.

A proposed overlap inequality must distinguish the actual theta
preparation from the pure-state positive-threshold control. A positive
gradient density has a signed Fourier transform. The finite
constant-coefficient transverse closure is already obstructed by the
exponential theta score. The angular PDE alone allows different Fourier
coefficients, and leading stationary coefficients require endpoint and
remainder payments before use in a full signed estimate.
Changing coordinates must transform the physical slope, heat coefficients
and observation covectors. A chart that straightens a fold does not remove
its collision. The stationary-sign route requires earlier critical-branch
coverage at every target boundary; a sign at the collision alone is
insufficient. Physical normalizer derivatives must be restored before
testing the stationary sets.

Computations should choose a lemma and test complete costs. Floating
samples and smaller isolated errors cannot decide a proof assertion;
outward enclosures are required. The shared checker verifies printed
finite identities and does not establish a huge-height sign, useful
multiplier bounds, or the imported analytical interface.

After a bounded mechanism succeeds, the program must bridge cutoff
boundaries and gaps, cover complementary time/height relations and compact
regions, and control the small-time limit. The threshold branch retains
its separate multiplicity hierarchy. A first-jet visibility theorem
already handles every multiplicity inside its domain. The initial
manuscript records exact structures and conditional implications. The
continuation supplies a strict, fully paid bound on a nonempty bounded
domain. It also supplies the conditional stationary-sign theorem and
complete theta targets. The next substantive milestone is a uniform
complete-source estimate on a growing family with the required multiplier
growth, or a proved theta stationary-set correlation with its full
predecessor coverage and error costs.

Continuation preparation record, 10 October 2026: GPT-6 (Codex), active
reasoning effort unavailable to this session and not inferred. The
new proofs, outward replay and parallel review are internal LLM checks.

Initial manuscript: [Enlarged-state transport and heat-flow visibility](../enlarged_state_transport_and_heat_flow.tex).
Historical context: [Heat Note 14](../../notes/14_DIMENSIONAL_REDUCTION_AND_SUPERSYMMETRIC_HEAT_PROGRAM_20261010.md),
[Note 23](../../notes/23_SIGNED_CANDIDATE_LOCALIZATION_AND_RESONANT_BOUNDARY_PROGRAM_20261010.md),
and [Note 24](../../notes/24_CURVATURE_CONES_SHARP_NULL_PAYMENTS_AND_LOCALIZED_POISSON_20261010.md).
