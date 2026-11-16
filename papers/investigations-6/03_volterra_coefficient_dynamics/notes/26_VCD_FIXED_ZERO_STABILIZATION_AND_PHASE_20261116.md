# Fixed-zero stabilization and the role of phase

16 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance, chat0004. Actual model and
reasoning effort are unavailable in the recorded configuration. No
subagent or numerical research campaign was used.

**Status: analytical corollary derived and incorporated; same-assistant
checking only.** The author's suggestion to follow an older zero is made
precise in manuscript §10.3. This is a discussion-driven consequence of
the established convergence and signed error law, not execution of B07
or E25. No uniform growing-height zero-confinement result is claimed.

Read the [result index](../../../../result-summaries/README.md), especially
[cluster18](../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md),
and the [avoid index](../../../../avoid/README.md), especially
[01](../../../../avoid/01_restating_the_target.md),
[02](../../../../avoid/02_shape_only_arguments_and_the_controls.md),
[07](../../../../avoid/07_scoped_exclusions_read_as_universal.md) and
[13](../../../../avoid/13_a_factor_is_not_the_target.md).

## The fixed-zero result

The [manuscript](../manuscript/main.tex), Proposition 10.2, derives the
standard isolated-cluster consequence of compact convergence (5.5):
an isolated zero r of F of multiplicity m attracts exactly m zeros of
G_N, counted with multiplicity. Factoring F(z)=(z-r)^m A(z) on an
isolating disk gives the explicit localization (10.7). A simple real
zero has a unique, real, simple approximating zero r_N for all
sufficiently large N. A multiple zero supplies a cluster, not unique
labels for its constituents. On any fixed bounded region with zero-free
boundary, these clusters eventually account for all the readout zeros.

Corollary 10.3 combines that fact with F-G_N=L_N E_N and E_N(r)→1:

\[
r_N-r=\frac{L_N(r)}{F'(r)}(1+o(1)),\qquad
\frac{r_{N+1}-r}{r_N-r}
=-\frac{\beta_{N+1}r^2}{(2N+1)(2N+2)}(1+o(1)).
\]

Here L_N(r)=(-1)^N(β_1⋯β_N)r^{2N}/(2N)!. The coefficient envelope
makes the ratio O_r(log²(N+1)/N²). The displacements eventually alternate
sides and decrease at every degree; each parity subsequence approaches r
monotonically. Equation (10.8) also gives an upper bound with the explicit
error-factor allowance and the fixed limiting slope.

The proof uses the exact identity

\[
(r_N-r)\int_0^1G_N'(r+t(r_N-r))\,dt=L_N(r)E_N(r).
\]

The integral tends to F'(r) by Cauchy's derivative formula. This proves a
fixed-zero asymptotic and an eventual bound; it does not supply an effective
starting degree uniformly over increasing zero index. Simplicity and
reality belong to the specified limiting zero's hypotheses.

One can instead start from a finite approximant: isolate exactly one
G_N0 zero in a conjugation-symmetric disk and establish a strict boundary
comparison |F-G_N0|<|G_N0|. Rouché certifies one real simple F-zero there.
Lemma 10.1 supplies a sufficient slope/curvature test. The discussion
does not assert that this test is already certified for a growing family.

**Stabilization alone does not establish reality.** A nonreal limiting
zero also attracts a stable cluster, and a multiple real zero can be
approached by nonreal pairs. The RH-equivalent exhausting-strip objective
remains stated once, now in §10.4, without finite checks as support.

## Labels and the purpose of phase

An isolating disk gives a natural persistent label. Eigenvalues of J_N
are source-coordinate quadrature nodes; Fourier zeros are in the different
observation variable. Moreover G_2 is already a cosine with infinitely
many zeros: increasing N does not simply add one zero. The old/new
distinction is most useful as fixed compact geometry versus geometry in
expanding observation regions, without assuming chaotic motion.

The expanded §10.1 starts with the moving point (cos x, sin x). Zeros of
sin x are its horizontal-axis crossings; the continuous angle is x.
A positive angle derivative gives ordered crossings, and quantitative
angular-speed bounds can give spacing bounds. Formula (10.2) is the
general companion-function version. Christoffel–Darboux gives the needed
positive numerator for consecutive orthogonal polynomials in the source
coordinate. No corresponding Fourier-readout identity is established.
This derivative varies the observation coordinate at fixed degree; it
does not differentiate a zero with respect to N. Fixed-zero stability
uses local convergence directly and needs no phase comparison.

## Control screen and provenance

Applied [catalog12](../../../../result-summaries/12_collision_controls_and_screening.md)
using the explicit premise table in
[integration25](25_VCD_ANALYTICAL_READOUT_MANUSCRIPT_INTEGRATION_20261116.md#control-screen).
The standard cluster statement applies to any locally uniformly convergent
nonzero holomorphic limit, including nonreal-zero controls. The sharper
corollary applies whenever the signed error law, E_N(r)→1, coefficient
envelope and fixed real simple root hypotheses hold. Positive finite
weighted-square sources pass the shared analytical estimates and can
satisfy the corollary at individual real zeros while retaining nonreal
zeros elsewhere. They fail the unchanged complete source, not this local
lemma. Thus the local lemma is not an all-control rejection criterion.

For the other controls the existing named failures remain: tested Euler
translates fail the stated adjacent envelope; reflected super-Gaussians
fail the exponential score-confinement input; smooth shape and finite-data
controls fail complete canonical arithmetic; atoms and compact triangular
sources fail the positive full-line density premise (atomic quadrature
also degenerates after finite support); changed observations fail the
literal Fourier-readout premise; RH-conditional endpoints retain their RH
assumption; finite-profile relaxations do not identify the physical source.
Failure of an input to a quantitative bound is not a failure of generic
compact zero stability. E10's smooth finite-data freedom still has no
asserted nonreal-zero configuration. No control certificate was rerun.

Topping's author notes, §§9.8–9.9, Theorems 9.18 and 9.21, were rechecked
for the multiplicity count and Rouché comparison; the existing
[passage record02](../references/02_INDUCTION_SOURCE_PASSAGES_20261116.md)
and manuscript bibliography retain the source. The corollary is derived
from the manuscript's inputs, without a literature novelty claim.

[Assessment10](../reviews/10_VCD_FIXED_ZERO_COROLLARY_ASSESSMENT_20261116.md)
and [build12](../numerics/12_VCD_FIXED_ZERO_MANUSCRIPT_BUILD_20261116.json)
record the checks. The reading PDF remains in ignored root output;
intermediates remain outside the repository. Automatic chat refresh
reported a source/registry creation-time mismatch. The prior verified
archive, including the preceding final reply, was left intact; no history
JSON or identity metadata was edited to bypass the guard.
