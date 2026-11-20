# AGC continuation estimates: separate contributing-agent assessment

19 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance. Requested reviewing-helper dispatch:
**gpt-6.1-sol / ultra**. Actual serving-backend model and effort were not
independently attested to this helper. This is internal LLM review by a
different contributing agent, with inherited/shared source premises; it
is not specialist human review or an attested cross-model assessment.

**Final assessment status:** E10's two analytical modules, E13's log-disk
refinement, and their mathematical integration in manuscript Section 8
are **accepted within their stated hypotheses and scope**. No blocking
mathematical finding remains. E12's implementation, numerical record and
certification are excluded from this final acceptance: the lead assigned
their nonauthor assessment and sole replay to a separate helper's
**Review04**. One full analytical assessment and one correction round
were completed.

The [assessment request](../research-progress/handoffs/AGC-E13-r1-review-request.md),
[B01](../brainstorm/notes/02_AGC_B01_FIXED_CELL_COMPARISON_20261119.md),
[B02](../brainstorm/notes/03_AGC_B02_LOG_DISK_REFINEMENT_20261119.md), and
[fixed-pilot addendum](../brainstorm/notes/04_AGC_B01_FIXED_PILOT_ADDENDUM_20261119.md)
define the scope. Read with the
[result index](../../../../result-summaries/README.md),
[pattern index](../../../../avoid/README.md),
[Controls12](../../../../result-summaries/12_collision_controls_and_screening.md),
and patterns [01](../../../../avoid/01_restating_the_target.md),
[02](../../../../avoid/02_shape_only_arguments_and_the_controls.md),
[07](../../../../avoid/07_scoped_exclusions_read_as_universal.md),
[08](../../../../avoid/08_normalization_and_constant_slips.md), and
[12](../../../../avoid/12_term_by_term_matching_and_separate_bounds.md).

## Ownership and limits

The assessor did not author E10 notes04–05, B02, E13 note08, or the E12
module. **The assessor did author source note06. That note is
excluded from this assessment's nonauthor-review claim.** The lead's
separate [source check](03_AGC_SOURCE_ALLOWANCE_LEAD_CHECK_20261119.md)
owns its review and primary-import verification.
References to that source allowance below check consumer compatibility,
not independently validate the allowance. No assessed file is edited by
this review.

The analytical claims concern finite conditional transfer and estimator
refinement. They are not an RH-equivalent criterion or a canonical
positive-gap result. The fixed numerical cell lies within earlier
coverage and cannot supply new canonical coverage by passing its checks.

## E10 contour module

Source: [Note 04](../notes/04_AGC_E10_CONTOUR_ENDPOINT_20261119.md).
**Accepted**, within its written hypotheses and status.

1. With \(\langle f\rangle=(2\pi i)^{-1}\oint_\Gamma f\,dz\),
   integration by parts gives
   \(\Delta A_1=-I_0\),
   \(\Delta A_2=-2(I_1+c_PI_0)\). Substitution into
   \(D=A_2/2-c^2\) gives exactly
   \(\Delta c=-I_0/2\) and
   \(\Delta D=-I_1-I_0^2/4\). The square is a complex square, not an
   absolute square. Multiplicities are retained by the argument principle.
2. On the fixed radius-\(r\) circle, the Cauchy–Schwarz estimate is
   \(|I_1|\le r\sqrt{r^2+|X-c_P|^2}\,\lambda\), with
   \(\lambda=-\log(1-q)\). The full allowance and center error have
   the correct \(r\), \(1/2\), and \(1/4\) factors. Convexity of
   the disk gives \(|X-c_P|<r\) from count two, with no real-zero
   assumption. Conjugation symmetry makes the discriminant real;
   positive discriminant then distinguishes a real pair from a nonreal
   conjugate pair.
3. Backward time gives \(P_u=P_{zz}-R\), \(H_u=H_{zz}\), so
   \(\ell_u=Q+R/P\) and
   \((c_P)_u=\langle R/P-P_{zz}/P\rangle/2\).
   Differentiating both the moving center and \(I_0^2/4\) gives
   \((D_H-D_P)_u=-K\). All three terms of \(K\), including the
   center and reference defect, are present. The endpoint functional and
   the complete signed integral are equal for the same admissible path.
4. A nonvanishing holomorphic multiplicative factor changes the collar
   logarithm by a holomorphic function plus a branch constant. Both
   moments annihilate that change. This statement is valid even for a
   spatially nonconstant factor; the isolated quotient \(Q\) need not
   vanish. Its time version correctly imposes the unchanged heat law,
   which makes the full defect-compatible contour integral vanish.
5. A strict \(q<1\), reference count two, cleared contour and the
   analytic/time regularity are explicit. The logarithm is required only
   on a collar, not through interior zeros. The final lower bound is
   required on every time slice. No inequality between two separately
   relaxed allowances is inferred from equality of exact functionals.

Two display typos were reported to the lead during the correction round:
the branch-constant formula contained stray inline dollar delimiters,
and the control text had a malformed \(D_P(U)\). The lead corrected
them; the underlying identities and conclusions do not change.

## E10 bounded-heat module

Source: [Note 05](../notes/05_AGC_E10_BOUNDED_HEAT_20261119.md).
**Accepted**, within its written classical-solution hypotheses.

The diffusion coefficient is one in the physical variable. Green's
identity has boundary contribution
\([K E_\xi-K_\xi E]_{x_-}^{x_+}\), giving the positive left kernel
\(\partial_\xi K|_{x_-}\) and positive right kernel
\(-\partial_\xi K|_{x_+}\). Both lateral data are retained. The
adjoint identity is correctly bilinear, with no inserted complex
conjugation. Fixing \(y\) leaves an ordinary real horizontal heat
problem, so there is no omitted boundary integral at \(y=\pm h\).

The constant solution checks the exact mass identity
\(S+Q_-+Q_+=1\). Half-line comparison bounds each \(Q_\pm\) by its
erfc function, and the sum is even and convex in \(x-X\), so the
circle bound at \(x=X\pm r\) is correct. The bound does not invoke an
unacquired whole-line extension or outside tail amplitude. Initial and
lateral corner compatibility and the \(u=0\) mass convention are paid.

The positive-kernel allowance retains full initial, lateral and forcing
data. Its scalar reduction correctly combines the initial and lateral
terms as \(\varepsilon_0+(M_b-\varepsilon_0)(1-S)\).
Replacing \(1-S\) by its upper bound requires
\(M_b\ge\varepsilon_0\); the note explicitly avoids the invalid sign
substitution when that condition fails. Its Cauchy fallback for
\(E_{zz}\) has the correct coefficient \(2/d^2\) and explicitly
requires a paid larger analytic disk. It does not claim to preserve the
joint numerator's cancellation after separate derivative bounds.

The claimed initial-local-norm-only failure is confined to the stated
classical homogeneous heat class. The entire exponential family has the
required small initial rectangle norm and unbounded later interior norm;
its growing boundary datum is precisely what the representation pays.
This does not refute bounded-domain propagation with acquired boundaries.

## E13 centered logarithm and coupled coefficient bound

Source: [Note 08](../notes/08_AGC_E13_LOG_DISK_ALLOWANCE_20261119.md).
**Accepted**, as an analytical refinement of the specified complete
allowance at the same information, with no canonical data acquisition.

The normalization \(v=(1+w)/\sqrt{1-q^2}\) sends the value disk to
the disk with center \(\cosh\eta\), radius \(\sinh\eta\), where
\(\eta=\operatorname{atanh}q\). Its inequality
\(|v|^2+1\le2\cosh\eta\Re v\) is equivalent under
\(\xi=(v-1)/(v+1)\) to
\(|\xi|\le\tanh(\eta/2)\). The convergent odd series for
\(2\operatorname{atanh}\xi\) agrees with the principal logarithm
because the entire disk lies in the right half-plane. This proves
\(|\log(1+w)-\kappa|\le\eta\), with
\(\kappa=\log(1-q^2)/2\), including the separate \(q=0\) case.
The two real endpoints are distance \(2\eta\) apart, so the asserted
optimal containing radius is correct. The note does not mistake this
containing disk for the actual logarithm image.

Subtracting the constant \(\kappa\) preserves both contour moments.
Bessel's inequality gives the joint negative-mode constraint
\(|a_1|^2+|a_2|^2\le\eta^2\), without assuming the other modes
vanish. The Fourier signs and radius factors then give exactly

\[
\Delta D=-r^2a_2+(c_P-X)r a_1-r^2a_1^2/4.
\]

The complex square and fixed-contour offset are both retained. On the
abstract two-coefficient ball, maximizing the complete modulus gives

\[
F(\eta,d)=\max_{0\le x\le\eta}
 \{\sqrt{\eta^2-x^2}+dx+x^2/4\},\qquad d=|c_P-X|/r.
\]

The phase choice in the note aligns all three terms, so this is the
exact maximum of that relaxation. Its maximizers are not asserted to
be realizable by an admissible logarithm or theta source. Substitution
\(y=\sqrt{\eta^2-x^2}\) yields \(F(\eta,0)=\eta\) for
\(0\le\eta\le2\), and \(1+\eta^2/4\) for \(\eta\ge2\).
The general Cauchy bound and the concave-quadratic bound
\(F\le\eta+\eta d^2/(2-\eta)\) are correct, the latter used only
when \(0<\eta<2\). The zero and endpoint cases are explicit.
Complex or uncertain centers are handled by a paid upper bound for
\(d\); there is no moving contour or assumed canonical centered pair.

The strict comparison uses the stronger E10 old allowance
\(r^2[\sqrt{1+d^2}\lambda+\lambda^2/4]\), not merely the weaker
\((1+d)\lambda\) version in B02. Since
\(0<\eta<\lambda=-\log(1-q)\) for \(q>0\),
\(r^2F\le r^2[\sqrt{1+d^2}\eta+\eta^2/4]\) is strictly smaller
for every finite \(d\). An identical additional nonnegative error on
both sides preserves that strict comparison; it does not supply the
additional error or any missing positive margin.

At \(q=1/2,d=0\), the complete new allowance is
\(r^2\log3/2\). The exact positive-series estimates
\(\log2>69/100\) and \(\operatorname{atanh}(1/2)<11/20\), together
with
\((17/25)(69/100+(69/100)^2/4)=550137/1000000>11/20\), prove the
claimed factor below \(17/25\), hence more than 32 percent saved.
This checks a symbolic allowance comparison, not a theta certificate.

The all-time, count, branch, source-error and conjugation gates are
explicit. The same zero-error quadratic still merges, and the expanded
Controls12 screen remains valid for this generic improvement. Neither
the exact coefficient-ball optimum nor the smaller numerical constant
distinguishes theta from a colliding source.

## Manuscript integration check

The lead additionally requested a compatibility read of
[Section 8](../manuscript/sections/08_local_estimates.tex). Its heat
signs, lateral terms, source/reference choice, fixed-circle offset,
complete nonlinear square and comparison scope agree with the accepted
notes. Source note06 itself remains excluded from this nonauthor review.

The correction request identified two LaTeX transcription errors
(missing backslashes before an \(\texttt{end\{align\}}\) and
\(\texttt{quad}\)), and requested that the optimality wording apply
only to \(F\), not its looser Cauchy/parabolic upper bounds. A short
phase-attainment argument and the rational constant comparison make
those quantitative claims self-contained. The lead's corrections were
re-read and pass: both transcription errors are fixed, optimality is
restricted to \(F\), the phase argument is present, and the inserted
positive-series rational proof is valid. The analytical integration is
accepted. Any subsequently appended numerical pilot table and its
certification claims require the separate numerical Review04.

## Numerical assessment delegated to Review04

After the analytical review, the lead directed that a separate nonauthor
helper assess E12's script, final record and numerical manuscript table,
including the sole replay. This review therefore makes **no acceptance
claim** for its reported numerical margins or certification. Review04
owns checks of full source/alias/arithmetic payments, time/arc coverage,
annular logarithm branch, scale, interval method, hashes and replay.
The analytical estimator comparison proved above is independent of the
numerical pilot's eventual assessment. The same-information comparator
and earlier-coverage qualifications remain mandatory for that pilot.

## Comparator and collision screen already checked for E10

The same-information comparator receives the same source, reference,
anchor, boundary data, forcing, correlations and propagated enclosures.
It may evaluate endpoint moments or intersect every valid bound. Exact
functional equality therefore rules out a representation-only advantage
on an identical admissible path set; it says nothing about superiority
over a weaker raw data envelope or the cost of acquiring correlated data.
No new such superiority has been acquired by E10.

The translated quadratic with \(H=P\) gives \(E=R=0\), a cleared
count-two contour, and a discriminant reaching zero. This checks that
both modules preserve a merger and fail their strict final-gap premise
there. The analytical screen covers Euler-factor, weighted-square,
reflected super-Gaussian, smooth/positive-primitive, finite-source,
finite-prime, fixed-event/profile and RH-conditional endpoint controls.
At any applicable isolated double event a valid final allowance cannot
give \(D_P-B>0\), since \(D_H=0\) forces \(D_P\le B\).
Source-specific theta identification fails for the modified controls,
but that does not imply every relaxed numerical inequality fails on
every box. The absence of an all-real time for the documented finite
source class is preserved. RH-conditional escaping doubles are not
treated as unconditional fixed-compact counterexamples.

Changed-observation-kernel controls fail the physical cosine/Newman
equation, so their complete prepared residual must be included. Reflection
rigidity is a classification statement, not another collision witness;
fractional divisors fail integer count two, and static divisor surgery
does not supply the common source heat path. A failure of an order-one
product hypothesis in a control is not used as a premise of these local
contour or bounded-heat identities, which need no such global product.

The accepted E10 results are finite identities and conditional complete
bounds. Their controls reject an unpaid collision exclusion, not the
unchanged theta source or every possible source-specific arithmetic
estimate.

## Final disposition and correction record

Accept E10 notes04–05, E13 note08, and the analytical Section 8 integration.
The correction round resolved presentation errors and sharpened the
manuscript's optimality wording and self-contained finite-factor proof;
it did not change the accepted mathematical conclusions. Exact full
transport and direct endpoint readouts remain equal on an identical
admissible path set. E13 strictly improves the specified complete
allowance at the same \(q\), geometry and reference information; it is
shared by both readouts. No source-specific \(q\), canonical positive
margin, new zero coverage, or numerical certificate is acquired by this
analytical acceptance. Source note06 is owned by the separate lead
check; numerical E12 is owned by Review04.
