# Analytic zero flux estimates for open heat contour boundaries

23 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**, reasoning effort **max**.

**Research objective:** replace a zero-free spatial wall, where it is an unnecessary restriction, by an analytically controlled boundary contribution. Determine whether this permits a useful larger backward width ε at high height and improves a completed multiplicity or cap estimate. The intended mathematical application remains RH implying simplicity, with **RH implying almost-all simplicity** the first global target compatible with a sublinear flux allowance.

**The work is driven by analytic goals. Numerics have a supporting role.** Proofs, complete-source inequalities and explicit error theorems define the milestones. Computations may check an identity, challenge a conjectured estimate, or clarify constants in an already specified theorem; a numerical result alone does not complete an analytic milestone. In particular, a height scan or a search for a larger numerically admissible ε is not the opening task.

This program remains in the brainstorm folder at the author's request. Its [progress register][progress] is the sole owner of the new **OBF** tasks. [Investigation 12's analytical program][hdc-program] and its HDC register retain their existing scope and task identities. The present program refines the open-boundary alternative discussed in [Brainstorm Note 04][flux-note]; it does not promote that finite derivation into an acquired theta estimate. The [continuation note][continuation] specifies the first research session.

Read the [result index][results] and [avoid index][avoid], particularly [local heat geometry][geometry], [collision controls][controls], [target classification][a01], [numerics before structure][a10], [coupled estimates][a12] and [scoped exclusions][a07]. No RH-equivalent restatement, generic transport identity or computational success is to be counted as a theta-specific upper bound.

## The field and the finite target

Retain the unchanged canonical source and normalization

\[
 H(\tau,z)=\int_0^\infty e^{\tau u^2}\Phi(u)\cos(zu)\,du,
 \qquad H_\tau=-H_{zz},\qquad
 8H(0,z)=\xi(1/2+iz/2).
\]

Here Φ is the complete canonical theta source used in the existing manuscript, including its full coefficients and tails. Positive surrogate sources, finite moment data and the reference field alone do not supply the desired arithmetic estimate.

For each height band declare an endpoint core, a buffer, a conjugation-invariant working region Ω_h, and a common earlier time −ε_h. Denote the endpoint population by N_h, counted with multiplicity. Geometry and ε_h must be specified from height and source information, rather than selected after inspecting unknown endpoint multiplicities. Distinguish the time width ε_h from a field regularization ρ and any cutoff η near the real axis. Introduce height-dependent graphs only after proving the common-time statement; their slopes and joins require additional terms.

The finite starting point from [Note 04][flux-note] is

\[
 N_{\rm nr}(0)=N_{\rm nr}(-\epsilon)
      +J_{\rm in}^{\rm nr}-J_{\rm out}^{\rm nr}-B_{\rm real},
 \qquad
 B_{\rm real}=\sum_{-\epsilon<t\le0}2\lfloor m(t,x)/2\rfloor.
 \tag{1}
\]

It assumes a real-type holomorphic heat solution, finite interior events and simple transverse boundary crossings, no spatial boundary zeros on the endpoint slices, and no multiple spatial boundary zero. Interior endpoint multiplicities are allowed. The upper endpoint event is included. Consequently, under endpoint reality,

\[
 M_h\le\tfrac32\bigl(N_{\rm nr}(-\epsilon_h)
                             +J_{\rm in}^{\rm nr}\bigr). \tag{2}
\]

The generic real-site version needs no RH; RH is used when interpreting it as a bound on all canonical endpoint multiplicities. It supplies neither a negative-time all-real interval nor positive spectral order for complex roots.

The first quantitative target is an independently bounded complete-source allowance

\[
 N_{\rm nr}(-\epsilon_h)\le A_h,\qquad
 J_{\rm in}^{\rm nr}\le\mathcal F_h+E_h,
 \qquad U_h=\tfrac32(A_h+\mathcal F_h+E_h). \tag{3}
\]

An upper bound on all inward crossings is acceptable as a conservative substitute, provided its size is useful. Signed *nonreal* flux can give a sharper consumer when its sign and errors are paid. Signed total-zero flux is insufficient: real exits can cancel nonreal entries. A bound on F alone does not control the earlier nonreal resource A.

## What open boundaries change

The physical first-jet cap requires |H|²+|H_z|²>0 on its boundary. A simple wall zero is already compatible with that condition. Its full side integral, complementary pieces and joins remain in

\[
 I_0=I_{-\epsilon}-S_\epsilon+Q_-,\qquad Q_-\ge0.
\]

A scalar crossing count cannot replace S_ε, and a multiple boundary event requires an event link or excision. The cap branch therefore needs an estimate of the full first-jet flux, not a new assertion that every spatial crossing is forbidden.

The [fixed-degree coefficient propagator][coefficient] does require a complete isolated population. Simple entries and exits admit one-sided multiplication or division of its prepared polynomial by the crossing factor. Developing a composition theorem with all transfer errors is a secondary task. A varying population cannot simply be inserted into the existing fixed-dimensional propagator, and one crossing does not automatically change the pair statistic q by at most one.

## Analytic work packages

| Task | Mathematical deliverable | Acceptance condition |
| --- | --- | --- |
| **OBF-01** | A precise finite transport theorem allowing simple spatial crossings, with the endpoint multiplicity consumer and a smooth-window extension if justified | A proof pays endpoint events, conjugation, multiplicities, crossings and any excisions; it reproduces the quadratic and cubic controls |
| **OBF-02** | A complete-field representation and analytic upper estimate for the required one-sided nonreal inflow, or a conservative inflow proxy | Its regularization, orientation, near-real contribution and source-error terms are explicit; the proof does not reintroduce the zero-free wall as an unproved hypothesis |
| **OBF-03** | A canonical-theta bound for that flux allowance on a prescribed negative-time band | An inequality with justified height, width, buffer and time dependence, complete source tails, and an identified arithmetic input; an exact representation alone does not pass |
| **OBF-04** | Independent analytic control of the earlier nonreal population, jointly with the flux error when useful | A bound on A_h, or a complete projected-pair upper bound near zero, with errors at the scale required by (3); a small boundary flux alone does not pass |
| **OBF-05** | A theorem choosing admissible ε_h and assembling the bands into a covered endpoint estimate | All population, overlap, omitted-label and graph-join costs are paid; the theorem states exactly whether it gives a finite improvement, density one, or an integer-scale exclusion |
| **OBF-06** | Optional transfer to the physical cap or piecewise coefficient method | A complete bound for that consumer, with its own boundary and conditioning requirements and an analytical comparison against the existing method |

Opening execution, 23 October 2026, for Edward Baker with substantial LLM assistance, **gpt-6.1-sol (Codex), actual effort xhigh**: [Note 07](../notes/07_NONREAL_WINDOW_TRANSPORT_AND_REGULARIZED_CURRENT_20261023.md) and its [same-assistant self-review](../reviews/02_NONREAL_WINDOW_AND_CURRENT_SELF_REVIEW_20261023.md) now prove OBF-01 at the stated finite scope and select the smooth current for OBF-02. The current/error representation, direct negative-time Taylor budget, and carrier terms are paid; a useful normalized theta small-value estimate is not. The [progress register][progress] records the precise partial status. OBF-02 and OBF-03 remain the main new flux questions. OBF-04 is a separate substantive obstacle already visible in the earlier program. OBF-06 should follow a specific useful estimate, rather than expand the opening session into several new formalisms.

## The first analytic investigation

First audit (1)–(2), then decide which observable can actually dominate the inflow. Two candidates deserve a short analytical comparison.

**A boundary current with one-sided orientation.** At a simple root, z'(t)=H_zz/H_z. Study the zero current through the space-time wall, using a signed area or coarea representation of the complete boundary field. Determine the orientation that counts inward motion, what positive part must be retained, and how the real-axis restriction changes the estimate. This is an attempt to bound an integrated contribution without dividing by a pointwise minimum of |H|. Small H_z near a collision, recrossings and simultaneous opposite crossings cannot be discarded.

**A smooth window with a defect-sensitive transport term.** Let 0≤ψ≤1 be compactly supported, equal to one on the endpoint core and varying only in its buffer. A candidate finite theorem uses

\[
 N_{\psi,\rm nr}(t)=\sum_{\Im z_j(t)\ne0}m_j\psi(z_j(t)),
 \qquad
 F^+_{\psi,\rm nr}=\int_{-\epsilon}^0
       \sum_{\Im z_j(t)\ne0}
       [\nabla\psi(z_j(t))\cdot z_j'(t)]_+\,dt,
\]

where complex velocities are identified with planar vectors and regular time segments are used. Establish the event terms and integrability before asserting a bound on M_core by 3/2 times N_ψ,nr(−ε)+F^+_ψ,nr. Even a successful proof would still need an independent source bound on these quantities. This is a proposed extension, not a completed theorem in this overview.

The [existing logarithmic regularization][regularization] gives stable transport of the *total* weighted divisor from u_ρ(H)=½log(|H|²+ρ²), with source error at most η_source‖Δψ‖₁/(4πρ). It does not by itself give F^+_ψ,nr. The next proof must explain how the regularized quantity controls the required positive current, how the field cutoff is removed, and what remains near the real axis. A thin omitted strip can contain the entire multiplicity witness.

Choose the candidate with the most explicit, least circular source inputs. The first new quantitative deliverable should be a finite analytic inequality with all constants and error terms exposed. If no useful inequality follows from the chosen information class, state that limited obstruction and identify the additional source information required. Do not replace the missing argument with a mesh refinement.

## The theta estimate and larger backward widths

The [corrected microscopic reference][reference] is relevant source information, but its acquired real-clock error is not automatically a negative-time or complex-time estimate. Prove any needed extension of the error against H, including the full source and heat defect. Analytic continuation of the reference formula alone is insufficient. The [positive-time height-boundary theorem][height] supplies a signed real net flux in its own large-height regime; it is a benchmark, not the negative-time nonreal-inflow bound needed here.

Keep the coupled field and derivative expressions intact before estimating. A bound obtained solely by replacing every denominator by a small uniform floor may recreate the old restriction. A deterministic average over a declared family of wall positions is a possible fallback, but a small average must be converted into admissible walls with proved endpoint coverage. It is not a license to discard troublesome roots.

The exact conservative resource on a fixed region,

\[
 R(a)=N_{\rm nr}(a)+J_{\rm in}^{\rm nr}(a,0),
\]

is nondecreasing as a moves farther backward: the added amount equals outward nonreal flux plus real births on the added interval. A larger ε therefore cannot improve this exact resource by itself. The analytical comparison must show that improved approximation or conditioning, after all flux and bias terms, gives a better completed upper bound or establishes a useful parameter range unavailable to the fixed-population proof. Record an enlarged admissible range separately from a sharper bound.

Do not guess a favorable power of height for ε_h from finite data. Derive the allowed range from the source and flux inequalities. A width rule selected after observing unknown endpoint separations would reintroduce the target through the hypotheses.

## Global assembly and the two simplicity goals

For disjoint endpoint cores covering all but r(T) labels, the proposed final consumer has the form

\[
 \frac{M(T)}{N(T)}\le
 \frac{r(T)}{N(T)}+
 \frac{3}{2N(T)}\sum_h(A_h+\mathcal F_h+E_h). \tag{4}
\]

This gives density one only after the numerator is proved o(N(T)). If working buffers overlap, bound the total resource over the bands; the same entering zero may be charged more than once. Bounds uniform in the number and widths of bands are essential. For every-zero simplicity, retain a separate finite criterion below the least possible nonzero integer defect and prove full coverage. An o(N) allowance leaves sparse exceptions possible.

The [earlier-time projected-pair consumer][earlier] provides one option for OBF-04: bound the near-zero mass for the real projections of all earlier roots, including nonreal conjugates. Normalize by the correct endpoint population when populations change. Positivity of a real pair Laplacian must not be transported into the negative-time complex population without proof.

## Controls, review and numerical support

The analytic proof must retain the exact quadratic H=z²−2t and cubic H=z³−6tz entry/collision examples in Note 04. They force the inflow term and the sharp factor 3/2. The drifting sine control separates net total transport from one-sided entry. These models fail the unchanged canonical theta source; they test the generic transport theorem rather than a theta-specific inequality.

For a proposed source estimate, apply the [full control register][controls] to its actual premises. Euler-factor perturbations change the source coefficients; weighted-square and finite-prime controls lack the recorded full arithmetic/reflection data; reflection-completed and positive-primitive controls alter the exact theta source; close normalized endpoint controls fail ordinary Dirichlet-series arithmetic. Generic flux identities exclude none of them. Do not grant a global all-real heat interval to a control that lacks one. A claim contradicted by a control must be narrowed or withdrawn before further computation.

Optional numerics must name the analytic statement they support and what outcome would falsify it. Appropriate examples are exact sign/factor checks, a sharp model for a constant, or interval evaluation of the explicitly derived error terms. More precision, a larger verified box or a favorable finite fit is not a replacement for OBF-03 through OBF-05. An open milestone is not a reason to launch a numerical campaign.

Save derivations in brainstorm `notes/`, assessments in `reviews/`, and only necessary supporting computation records in `numerics/`. Preserve the [large-file policy][large]. The originating chat remains [history 0002][chat]; a future chat gets its own identity under the [history workflow][history]. This program and its initial derivation have not received independent specialist review.

[progress]: ../research-progress/01_OPEN_BOUNDARY_FLUX_PROGRESS_20261023.md
[continuation]: ../notes/05_CONTINUATION_ANALYTIC_OPEN_BOUNDARY_FLUX_20261023.md
[flux-note]: ../notes/04_OPEN_BOUNDARIES_ZERO_FLUX_AND_BACKWARD_WIDTH_20261023.md
[hdc-program]: ../../research-overview/02_PAIR_SPECTRUM_CURVED_CONTOURS_AND_CONDITIONAL_SIMPLICITY_PROGRAM_20261023.md
[coefficient]: ../../notes/12_COUPLED_COEFFICIENT_BACKWARD_TRANSPORT_20261023.md
[earlier]: ../../notes/05_EARLIER_TIME_PAIR_COUNTS_AND_DENSITY_ONE_SIMPLICITY_20261023.md
[reference]: ../../notes/14_MICROSCOPIC_COMPLETE_REFERENCE_AND_HEAT_DEFECT_20261023.md
[regularization]: ../../../11_late_heat_caps_and_charge_transport/notes/08_LOW_VALUE_HODGE_COUNTS_AND_REGULARIZATION_20261022.md
[height]: ../../../notes/11_INITIAL_CAP_FUTURE_BIRTHS_AND_HEIGHT_BOUNDARIES_20261023.md
[results]: ../../../../../result-summaries/README.md
[avoid]: ../../../../../avoid/README.md
[geometry]: ../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a10]: ../../../../../avoid/10_numerics_ahead_of_the_question.md
[a12]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[large]: ../../../../../LARGE_FILES.md
[history]: ../../../../../tools/CHAT_HISTORY.md
[chat]: ../chat-histories/0002_2026-10-23T20-20-56Z_review-curved-contour-manuscript.json
