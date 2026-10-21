# Joint review of the contour and simplicity investigations

21 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**,
reasoning effort **max**, verified from this chat's turn metadata.
This is a same-model internal assessment for discussion, not specialist
validation. Research checkout: `8cc883d2e022710975ab71a0da8591a5ad963d39`.

The two investigations have produced useful contour identities, quantitative
approximation and heat estimates, and explicit limitations on several
proposed transfers. They have not proved RH, RH implies simplicity, or a
later theta collision. The strongest claimed approximation theorem deserves
assessment as a mathematical result in its own right, separately from its
ability to prove simplicity.

This review follows the [result index][results], especially the
[local geometry summary][geometry] and [collision controls][controls], and
the [avoid index][avoid]. The relevant distinctions are
[a reformulation versus a quantitative gain][a01],
[the premises actually shared by controls][a02], and
[a scoped obstruction versus a universal exclusion][a07].

## How the two questions differ

[BW09's manuscript][bw09] begins with a hypothetical attained ordinary
event at a positive all-real threshold. It asks whether the original theta
source forces another event later. A later event would contradict
all-realness above that threshold. Coverage remains separate: BW09 has
not established that every hypothetical positive threshold supplies the
assumed finite-height ordinary event.

[BW10's manuscript][bw10] instead assumes RH and a multiple zero of the
original zeta function. The event is already at a specified heat time,
zero, and at a finite height by the contradiction hypothesis. This removes
the threshold-attainment issue and makes the original zeta and Möbius
arithmetic available. It also retains every finite multiplicity, rather
than treating all events as double.

Under RH, the heat flow is all-real for nonnegative times and simple at
every strictly positive time. A multiple zero at a positive time would
have nonreal predecessors at slightly earlier positive times. This
argument permits multiplicity at time zero; nonreal predecessors at
negative time are consistent with the hypothesis. Thus positive-time
simplicity does not itself settle the endpoint.

## What the contour work accomplished

For the physical jet \(J=H+iH_x\), a simple root wall has exactly zero
tangential phase change. Between simple root endpoints, with \(N\)
interior simple roots, the cap decrease is exactly
\[
M_{\rm cap}=(N+1)\pi.
\]
For an ordinary born pair the initial baseline is \(\pi\), so a complete
strict lower bound above \(\pi\) would force additional events. For the
outer walls of an order-\(m\) birth, the baseline is \((m-1)\pi\).
The local index is \(-\lfloor m/2\rfloor\), with the original event
and any apex connector accounted for separately.

The cap-at-infinity analysis makes two potentially misleading pictures
precise. The quadratic's ordinary half-turn concentrates at its endpoints.
For the complete theta source at large positive time,
\[
H(t,z/L_t)/H(t,0)\longrightarrow\cos z,
\qquad L_t\sim\tfrac14\log t,
\]
and the physical jet's phase concentrates near an interior extremum.
These changes in location preserve the ordinary phase total. Positive
rescaling of the derivative channel can redistribute the concentration
without changing the degree.

This is useful analytical progress: it prevents pointwise vanishing of
a phase density, or a disappearing amplitude, from being mistaken for
vanishing total winding. It also shows why a nonvanishing approximation
to an adjacent cosine lobe cannot supply extra winding. The new
[phase-surplus register][psc] correctly leaves the event-conditioned
strict estimate unexecuted.

The bounded numerical work has a narrower role. It excluded small stated
event boxes, found that the selected Gaussian estimator failed to prove
its requested negative sign, and proved one selected localized average
positive. Those results do not cover all hypothetical threshold events.

## The strongest approximation claim

Let \(L=\log N\), let \(V_{N,w}\) be the original Möbius polynomial
with one fixed normalized compact Gevrey taper of order \(1<\sigma<2\),
and use the manuscript's weighted critical-line error \(E\).
[Note 16][n16] records, **proved in-note under RH**, the complete limit
\[
L E(V_{N,w})\longrightarrow
\sum_{\rho\ {\rm distinct}}\frac{C_{m_\rho}(w)}{|\rho|^2}.
\]
Its important analytic step is a bound on the actual scaled height tail,
uniform in \(N\), rather than summability of limiting local profiles alone.
The proof keeps entire nearby zero clusters and uses the coherent ratio
\(\zeta(s)/\zeta(s+(H+iv)/L)\), avoiding separate reciprocal-derivative
estimates at individual zeros. The nearest-zero distance is integrated
over its actual cells, without a minimum-spacing hypothesis.

The finite Dirichlet filters in §§13–14 then permit different tapers at
different fixed zero locations. Their complete remaining profile tails
are controlled independently of filter degree. With the stated order of
choices and limits, the note obtains
\[
\lim_{N\to\infty}L d_N^2=K,
\qquad K=\sum_{\rho\ {\rm distinct}}\frac{m_\rho^2}{|\rho|^2}.
\]
This conclusion concerns the infimum over all admissible Dirichlet
polynomials, whose choices can depend on zeros and multiplicities. It
does not give an effective threshold in \(N\), an asymptotic for the
original linear Möbius taper, or uniformity for moving filters.

This is a substantial claim, not merely a restatement of simplicity.
[Burnol's lower bound](https://arxiv.org/pdf/math/0103058) supplies the
multiplicity-squared lower constant. The primary
[Bettin–Conrey–Farmer paper](https://arxiv.org/pdf/1211.5191), pp. 1–2,
states the corresponding expected asymptotic and proves its result under
RH plus an inverse-derivative moment hypothesis. The present notes claim
to obtain the infimum asymptotic from RH alone by a different fixed-taper
construction. That comparison makes Note 16's complete-tail theorem a
priority for specialist review; the cited literature does not validate
that internal theorem. No exhaustive priority determination was attempted.

The separate filter-resolution result is also concrete. Exact isolation
of two critical-line points separated by \(\Delta\), with a Dirichlet
polynomial bounded by one on that line, requires
\(\log M\ge\pi/|\Delta|\), and the explicit construction is within
\(\log2\) of this for small gaps. This prices that isolation task;
it is not a lower bound on every approximation strategy.

## What the energy calculations reveal

Write
\[
Z=\sum_{\rho\ {\rm distinct}}\frac{m_\rho}{|\rho|^2}
 =2+\gamma_E-\log(4\pi),\qquad
K-Z=\sum_{\rho\ {\rm distinct}}
 \frac{m_\rho(m_\rho-1)}{|\rho|^2}.
\]
All sums include both ordinate signs. A double conjugate pair contributes
\(4/(\gamma^2+1/4)\) to the excess. The approximation upper constant
retains exactly the squared-multiplicity cost that its lower bound detects.
There is no contradictory upper constant \(Z\).

[Note 15][n15] gives a second, independently interpretable measurement.
For the completed ratio energy at a multiple endpoint, the local
coefficient is
\[
c_m=m\left(1-\binom{2m}{m}/4^m\right).
\]
Its global proof uses a positive harmonic majorant with a known complete
mass, so the passage from local profiles to all zeros does not discard
mass at infinity. On the heat scale \(t=v\epsilon^2\), the complete
profile coefficient \(\mathcal A_{1/2}(v)\) satisfies
\[
\lim_{v\to\infty}v\bigl(\mathcal A_{1/2}(v)-Z/2\bigr)
 =(K-Z)/4.
\]
The limits are ordered: first \(\epsilon\to0\) at fixed \(v\),
then \(v\to\infty\). This links two ways of measuring multiplicity.
It provides no opposing bound or permission to interchange those limits.

The distinction between geometric measurements and arithmetic exclusions
is central. Establishing \(K=Z\) would settle simplicity under RH,
but renaming that condition would be an equivalent target. A different
idea can bypass these particular quantities; it need not continue this
optimization problem.

## What the latest notes add beyond the manuscript

The canonical BW10 manuscript intentionally stops before
[Notes 17][n17] and [18][n18]. Their additional conclusions matter for
the discussion:

| Result | Consequence and scope |
| --- | --- |
| Note 16 §16: positive heat time makes the original global norm infinite for every nonzero finite Dirichlet polynomial, for fixed \(0<t\le1/2\) | A compact heat calculation cannot be promoted to that unchanged global norm. The sharp logarithmic Gaussian weight threshold is \(t/8\), including equality, for the stated weight. |
| Note 17: an explicit carrier normalization restores a complete moving-heat profile limit under RH | The theorem keeps a fixed taper and bounded \(v=tL^2\). The changed target lacks ordinary Dirichlet-series structure and has an essential singularity at one; the original approximation lower bound is not automatically available. |
| Note 18 §§1–5: sharp arithmetic repair in the declared fixed finite filtered-Gevrey class | Original arithmetic profiles have fixed polynomial moments. Projecting a heat profile back into that affine moment space has an explicit cost, and the complete infimum of these transfer constants is identified. |
| Note 18 §§6–10: exact first-mode normalization also fails the ordinary-series test | Its second mode has a nonconstant power of the real argument multiplying \(2^{-s}\). The proof covers the specified first-mode and contour normalizers at fixed positive time, not every normalization or every moving-time transfer. |

For a double zero, the admissible original profile \(p\) obeys
\(\int p=1\), \(\int up=0\), and hence \(\|p\|_2^2\ge4\).
If \(h\) is a heat profile, Note 18 gives the least repair cost
\[
\delta^2=\|\mathcal K_2-\Pi_2 h\|_2^2,
\]
where \(\Pi_2\) projects onto linear polynomials and
\(\mathcal K_2(u)=4-6u\). In its explicit example,
\(h=2\cos(\pi u)\) has squared norm two, but the closest arithmetic
repair has squared norm
\(6-192/\pi^4\approx4.02893\); its squared distance from \(h\)
is about \(1.10765\). The apparent reduction in the heat problem
therefore does not supply a reduction below four in the original problem.

The approximation heat cost and ratio energy must also stay distinct.
The former's optimized double profile is nonmonotone in finite separation
and can fall below two; the latter's Hermite profile decreases toward
the separated simple-zero value. Transferring monotonicity between these
different functionals is unsupported.

## Controls and what remains open to a different idea

The exact positive atomic family \(1+e^t\cos x\) is all-real at time
zero, multiple there, and simple at every later time. It preserves the
generic heat and phase mechanisms but lacks the theta arithmetic. The
endpoint Euler-factor control preserves more arithmetic structure but
changes the zeta coefficients and conductor-one completion. Note 05's
closer positive sources preserve the displayed completion, residue one
and leading theta tail while adding double zeros, but fail ordinary
Dirichlet-series arithmetic. These are different controls; their
preservation lists cannot be combined into one object.

The remaining catalogue has equally specific limits. Weighted-square
and finite-prime controls fail full reflection and do not supply an
all-real slice merely from their local events. Reflected and
positive-primitive controls lack the unchanged theta square expansion.
The two-event quartic detects extra winding but its first event is not
its all-real threshold. No new estimator is proposed here, so these
are premise checks, not a new numerical control campaign.

The tested absolute-prime estimates, common-taper tradeoffs and heat
normalizations establish obstructions in their declared classes. They
do not establish that every signed arithmetic estimate, deformation,
or rigidity argument must fail. A proposed alternative should identify
which actual restriction it changes before inheriting a stop decision.

Two observations are especially relevant for a fresh discussion. First,
local separation immediately after an event and eventual compression of
fixed-index roots toward zero are compatible without a finite later
collision; the latter asymptotic also requires identification of the
selected walls. Second, a hypothetical multiple zero at arbitrary height
has an arbitrarily small weighted contribution to \(K-Z\). A universal
all-zero conclusion cannot be inferred from a fixed numerical tolerance
in that weighted sum.

The useful opening question for a different idea is therefore which
property of the unchanged zeta function constrains the admissibility of
the multiple endpoint, rather than merely assigning it a different
geometric or norm cost. This is a way to compare proposals, not a claim
that the present arithmetic formulation is the only possible route.

## Review depth and verification

Both canonical manuscript sources were read in full. The focused proof
assessment covered Note 15's mass exhaustion and crossover, Note 16's
convolution, cluster estimates, compact and scaled global limits, and
finite filters, together with the normalized-heat and repair arguments
in Notes 17–18. Earlier work was assessed through selected source notes,
the progress registers, and the recorded reviews; this was not a
line-by-line audit of every historical document.

No concrete fatal gap was identified in the inspected central estimates.
Their status remains proved in-note with same-model internal review.
The strong RH-only approximation conclusion has not acquired external
validation through this reread. Specialist scrutiny should concentrate
on Note 16's uniform complete-tail theorem, upon which several later
claims depend, before further branches rely on it.

The existing exact-rational replay was rerun: all 265 fixtures passed,
the returned mathematical fields matched the saved record, and the
script hash matched. These fixtures concern finite heat/Gaussian and
Euler-control algebra. They do not verify the analytic tail theorem.
The stored Lean check covers an abstract inner-product implication;
its analytic hypotheses and zeta transfer are outside that formalization.

The manuscript and research statuses were not changed by this discussion
review. The associated conversation is uniquely registered as
[history 0005][history] in this investigation's chat-histories folder.

[bw09]: ../../09_expanding_contour_later_collision/manuscript/main.tex
[bw10]: ../manuscript/main.tex
[psc]: ../../09_expanding_contour_later_collision/research-progress/03_ANALYTICAL_PHASE_SURPLUS_PROGRESS_20261020.md
[n15]: ../notes/15_COMPLETED_RATIO_ENERGY_AND_MULTIPLICITY_20261020.md
[n16]: ../notes/16_GEVREY_GLOBAL_APPROXIMATION_AND_RATE_20261020.md
[n17]: ../notes/17_NORMALIZED_HEAT_GLOBAL_LIMIT_AND_ARITHMETIC_COSTS_20261020.md
[n18]: ../notes/18_ARITHMETIC_HEAT_TRANSFER_AND_EXACT_COMPLETION_20261021.md
[results]: ../../../../../../../result-summaries/README.md
[geometry]: ../../../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../../avoid/README.md
[a01]: ../../../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[history]: ../chat-histories/0005_2026-10-21T04-09-04Z_review-threshold-route-manuscripts.json
