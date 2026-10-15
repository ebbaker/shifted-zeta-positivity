---
research_program: COORD
secondary_programs: [ALG, PR02, PR02-CORR]
status: integrated_and_auxiliary_positivity_pointwise_theta_bound_open
---

# Signed forms and a positive theta primitive

15 October 2026, America/New_York. Prepared for Edward Baker with substantial LLM assistance. Recorded coordinating model **gpt-6-astra**, reasoning effort **ultra**, verified from current-session metadata. This continues [Note 50](../04_octonionic_reductions/50_QUATERNION_FORMS_HODGE_PAIRING_AND_SOURCE_TARGET_20261015.md) and preserves [Note 49's pointwise target](49_OCTONIONIC_SIGNED_BOUND_ANALYTIC_CONTINUATION_20261015.md).

The author's 2014 documents were unpublished working notes, circulated to colleagues with mistakes and incompleteness acknowledged. Their role here is to suggest signed differential-form mechanisms. This continuation develops those ideas rather than treating the old documents as finalized claims.

**The theta-specific stationary bound remains open.** The continuation proves an exact disk completion, positive centered averages, and a strictly positive complete-theta auxiliary transform with an exact differential reconstruction. Two analytic controls identify why these results do not yet pay the physical energy near a candidate collision.

## Results and their limits

[Note 51](../04_octonionic_reductions/51_POLARIZED_HODGE_DISK_AND_CENTERED_SOURCE_BOUNDS_20261015.md) identifies the Hermitian signed density as
\[
\ell_f=|f'|^2-\Re(f\overline{f''})=\tfrac12\partial_y^2|f(x+iy)|^2.
\]
For \(g_R=(1-(z-x_0)^2/R^2)f\), it proves the sharp identity
\[
\int_{D_R}\ell_f+\frac1{2R}\int_{\partial D_R}|f|^2
=\tfrac12\int_{D_R}|g_R'|^2\ge0.
\]
The complete positive theta source also gives strictly positive averages of both branches against centered Gaussian weights, at every real heat time and imaginary displacement. The center must be the source's reflection origin. Translation introduces signed cosine factors, and the disk boundary norm is not the physical central energy. An exact positive atomic-source control shows that a fixed disk can have positive average while the central stationary loss has its adverse pole; detecting that pole requires \(R^2\) to shrink on the order of \(T-t\).

[Note 52](../05_theta_correlation_kernels/52_POSITIVE_THETA_PRIMITIVE_AND_DIFFERENTIAL_CLOSURE_20261015.md) defines the complete half-line primitive
\[
\psi(u)=e^u\sum_{n\ge1}e^{-\pi n^2e^{4u}},\qquad
J(t,x)=\int_0^\infty e^{tu^2}\psi(u)\cos(xu)\,du.
\]
It proves, for all real \(x\),
\[
J(t,x)>0\quad(0\le t\le1/2),
\]
and, for every real \(t\),
\[
8H=\tfrac12+(2t-x^2-1)J+4txJ_x-4t^2J_{xx}.
\]
The \(1/2\) is a proved modular boundary contribution. All indices and integration tails are retained. The positive auxiliary channel has algebraic spectral size, whereas the physical field has exponential decay. At time zero,
\[
J(0,x)=\frac1{2(1+x^2)}-\frac{8H(0,x)}{1+x^2},
\]
so the physical field appears as a small signed deviation from a positive rational profile. Positivity of \(J\) does not determine that deviation. The same note rules out any nonzero finite rational-coefficient linear jet identity for the complete theta field on an open spectral interval. It leaves stationary-only identities, transcendental coefficients, nonlocal formulas, and paid signed residuals available.

[Note 53](../05_theta_correlation_kernels/53_SOURCE_CONCAVITY_AND_POSITIVE_TIME_COLLISION_CONTROL_20261015.md) constructs a positive even source
\[
\phi_\delta(u)=e^{-u^2-\delta\cosh(4u)}
(1+u^2/5+u^4/50)
\]
for sufficiently small fixed \(\delta>0\). It has double-exponential decay, admits every heat time, and is strongly log-concave and decreasing around a positive-time collision; its logarithm in the squared source coordinate is strictly concave. Nevertheless, on a full stationary predecessor curve,
\[
\mathcal L_0/E=-1/(T_\delta-t)+O(1).
\]
The construction is analytic, with the exact undamped event at \(T_0=(8-\sqrt{10})/10\) and persistence proved by the implicit function theorem. It rules out deriving the desired bound from these source-shape properties alone. It is not a theta counterexample.

## Focus for the next analytic step

The target remains the complete signed circle current of Note 46, with full physical prefactors and full stationarity. Its useful sufficient form is
\[
\langle(1-\cos2\theta)\phi_j(\theta)\rangle\ge-C_jE,
\qquad j=0,1,
\]
with independently prescribed coefficients locally bounded through candidate events and a radius locally bounded away from zero. The equivalent sharper signed target, original staircase payments, and predecessor-covering domain conditions remain those of Notes 46 and 49.

The new primitive should be used only with the complete differential combination reconstructing \(H\), including its boundary constant. Separate bounds on \(J\), its derivatives, or the disk boundary norm lose the relevant cancellation. If the primitive route produces no estimate for that combined signed observation, its auxiliary positivity is not a reason to expand it further. A new certificate must identify extra theta arithmetic that excludes Note 53's control and, if exact on a spectral interval, must lie outside Note 52's finite rational closure class.

## Review and research state

[Review 31](../../reviews/31_SIGNED_FORMS_PRIMITIVE_AND_SOURCE_CONTROL_REVIEW_20261015.md) records the independent internal analytic cross-checks. No numerical pilot was run and no finite sample is used as proof. The manuscript, height-112 certificate, and outer threshold \(61/24\) are unchanged; no snapshot, commit, or tag was created.

This remains formal-replay history **16**, **Review octonionic signed-bound ideas**, thread `01a13e3b-8590-7352-8e09-ba07a7342c16`. Identity and prior messages are preserved. The live registry supplies current capture metadata. Native completion-hook activation has not been verified; the authorized bounded exact-turn capture remains in use.
