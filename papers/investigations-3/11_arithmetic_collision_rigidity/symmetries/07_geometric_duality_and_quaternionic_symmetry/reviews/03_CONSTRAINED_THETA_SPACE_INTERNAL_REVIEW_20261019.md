# Internal review: constrained theta space and residual contract

19 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Reviewing model **gpt-6.1-sol (Codex)**,
reasoning effort **ultra**, in a separate delegated same-model reading.
This is an internal mathematical review, not independent specialist human
review. The reviewer read S07 Notes 01/02, the T1 planning contract and
the complete new Note 03, and replayed its exact checker separately.

## Disposition

**Pass after two corrections incorporated before installation.** S07-T1
may be marked Complete as an admissible-space and observation contract;
S07-T2 may become Ready for the single selected N=2 bounded comparison.
Neither the note nor this review supplies a useful evaluated residual
constant, a physical lower bound, an arithmetic advantage or new coverage.
T3 remains Waiting and T4 Deferred. The repository's result and avoidance
guidance still governs any stronger claim.

The review caught an evenness mismatch: the first draft restricted every
profile to be even while claiming inclusion of all five jet levels. The
final class allows general profiles and therefore includes the odd levels
as well. It also caught an unjustified norm-domination phrase. X pays
additional mixed/profile regularity, but need not dominate the entire
ambient covariant H1 norm: the latter contains a y-squared moment in its
p derivative. The final text describes X as a different paid norm and
does not assert that domination. Neither correction changes inequality
(17), its constant or the selected physical residual.

## Geometry, fiber algebra and source

The frame conventions are consistent. A coefficient F in the original
holomorphic frame becomes h^(1/2)F in the unitary frame. Z in (2) is
isometric for fiber measure dr ds; the source profile therefore contains
the factor exp(pi p-squared q). Its p derivative in (18) retains this
factor's contribution. Reindexing at s+1 gives exactly the unitary
multiplier in (13). This justifies the global smooth profile cutoff and
also exposes the seam in a cutoff depending only on the integer index.
No modular descent is asserted.

The Gaussian raising recurrence, Gaussian Gram matrix, adjoint convention
A-star=-B and lowering relation BA^j theta=-j(pi/q)A^(j-1)theta agree.
The positive diagonal entries in (4) establish independence. The
fixed-fiber kernel-B^5 characterization follows by induction from the
one-dimensional holomorphic kernel and the nonzero lowering constants;
it is not a base-derivative closure assertion. The normalized source
uses levels 0 and 4 with the coefficients in (6). Its squared norm is
33/(256 sqrt(2)) times exp(2 pi p-squared q). The nonholomorphy coefficient
in (7) follows directly by lowering A^4; it is nonzero.

The kernel (8)-(9) is the finite-dimensional evaluation kernel in an
orthonormal basis. Its base metric factor cancels as claimed. A useful
uniform numerical supremum is expressly left unpaid. Equation (11)
correctly distinguishes coefficient p derivatives from covariant p
derivatives and shows the possible level-six component. No invariant
five-level base connection has been smuggled into the contract.

## Sampling constant, trace and residual class

The constants in (10) and (17) are safe. On a centered unit interval,
the fundamental theorem gives |f(n)|^2 <= 2 integral(|f|^2+|f_y|^2).
The comparison 1+n^2 <= 2(1+y^2), together with
sum_n(1+n^2)^(-1) <= 1+pi < 5, yields the stated factor 20 for Y.
The Hilbert-valued center trace on an interval of length 1/2 admits the
weaker printed constants 4 and 1. Applying it in the weighted profile
Hilbert space and then integrating dq/(4q) proves (17). No q trace or q
derivative is required for this integrated observation; a pointwise q
estimate would be another matter. The Cauchy payment in (21) follows
with exactly the physical measure shown.

The Gaussian envelope class with general profiles contains the whole
five-level class, the source, the stated smooth cutoff approximation,
the whole residual and both projections. Derivatives needed in X are
explicitly retained in (18), including the cutoff annulus. It is a
non-tautological domain: neither its definition nor its norm calls the
unknown complete-source point evaluation. Constants for the actual
envelope, cutoff and Gaussian-tail integrals remain T2 work.

The outside-V4 argument is sound. The residual profile vanishes on an
open plateau and is nonzero farther out; a finite polynomial times this
Gaussian cannot do so. The isometry makes this a fiber-space statement,
not just a formal profile observation. Its actual level-zero coefficient
is strictly positive: on the nonzero tail, pi q y-squared > 3/2,
a_q > 0, b_0 > 0 and 1-chi_N >= 0. Thus this particular residual has
both low and high components; this is stronger than the generic
multiplier fixture in the checker. Its low projection is not discarded
or conflated with the whole residual. The note correctly
refrains from assigning arbitrary spectral S02/S03 residuals to this
ambient class without a proved lift.

## Jacobi and holomorphy defects

Equation (19) was checked independently in its stated nonisometric
profile convention. In the original holomorphic frame its coefficient
is F=exp(pi q s-squared) Z_p[a]. At fixed z, the real base derivatives
are D_p=partial_p-s partial_r and
D_q=partial_q+(ps/q)partial_r-(s/q)partial_s. Substitution into
4 pi i partial_tau|_z-partial_z^2 combines the apparent n,s terms into
y=n+s and gives every coefficient of the printed profile operator.
The bare Gaussian is annihilated, while the covariant fourth source
retains its actual inhomogeneity. The vertical B expression and both
cutoff commutators in (20) follow by the product rule, including both
annular derivative orders and their signs. The equations must not be
reused without conjugation in the isometric f convention.

The class pays only the derivatives used in its observation bound.
It does not pretend to pay B^5, every Jacobi residual or an arbitrary
Green estimate in advance. The rigid homogeneous parent theta line is
distinguished from the broader source/error class as required.

## Controls and limits of completion

The old compact r-bump family is excluded exactly by Gaussian Fourier
decay, hence r analyticity. With unrestricted envelope constants this is
not a uniform anti-concentration theorem. The final note says so and
locates the actual bound in X. Alternative physical source functions can
already be lifted using a variable ground-level coefficient; V4 or the
Gaussian class alone therefore cannot distinguish collision controls.
The written premise screen and the upper-bound scope are appropriate.

The source-control record was inspected. Its five event rejections and
separate Euler signed witness are replay results for the unchanged
physical consumer, not validation of a new acceptance rule. This
mathematical review did not independently rerun that interval consumer.
No event box is claimed for the analytic existence controls. The note
retains the q>4 physical payment, all four faces if Green is later used,
normalization and approximation payments, and the requirement for a
matched direct comparison before any benefit claim.

## Verification receipt

The reviewer freshly ran the supplied standard-library checker with
assertions enabled. It passed and produced
`S07_T1_MATHEMATICAL_REVIEW_REPLAY_20261019.json`. This replay checks the
finite Hermite/Gram/source algebra, transitions, connection and Jacobi
fixtures, and rational budget constants. Its exact finite checks do not
replace the analytic convergence, sampling, trace and cutoff arguments
reviewed above. Hashes identify checked files and are not proof steps.

Source: [Note 03](../notes/03_CONSTRAINED_THETA_JET_SPACE_AND_RESIDUAL_CONTRACT_20261019.md).
Code: [exact checker](../numerics/check_theta_section_space.py).
Primary record: [section-space record](../numerics/S07_T1_SECTION_SPACE_20261019.json).
Controls: [source-control replay](../numerics/S07_T1_SOURCE_CONTROLS_20261019.json).

No remaining mathematical correction was identified in the corrected
draft. A true but losing T2 estimate would close its bounded feasibility
attempt; it would not invalidate this admissibility theorem or activate
the dependent physical task.
