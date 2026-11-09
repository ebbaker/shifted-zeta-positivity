# Collision constraints: scientific overview

9 November 2026, America/New_York. Prepared for **Edward Baker** with substantial OpenAI Codex assistance, OA chat0002. Actual model identifier and reasoning effort are unavailable in the chat registry. The inherited geometry below remains the baseline; the first-cycle result and its limits are recorded at the end.

## Question and boundaries

Can the unchanged complete theta source yield an inequality that
constrains a specified collision, its time, or the exterior influence
on a nearby pair? A first result may concern a declared compact
time/height region or a quantitative height-dependent bound. It need
not prove global realness. A restatement of no collisions is not an
intermediate result.

This branch owns **alternatives selected for a collision consequence**.
OC owns generalized marked marginals even without an immediate collision
application. OG owns the existing Green/resolvent program. The three
branches may exchange a proved estimate, but none is a prerequisite
merely because their representations involve the same H.

The [result index](../../../../../../result-summaries/README.md), especially
[geometry13](../../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md),
[theta14](../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md)
and [controls12](../../../../../../result-summaries/12_collision_controls_and_screening.md),
and [avoid index](../../../../../../avoid/README.md), especially
[classification01](../../../../../../avoid/01_restating_the_target.md),
[control02](../../../../../../avoid/02_shape_only_arguments_and_the_controls.md),
[coordinate03](../../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md),
[scope07](../../../../../../avoid/07_scoped_exclusions_read_as_universal.md)
and [volume20](../../../../../../avoid/20_volume_without_a_gain.md), govern
the distinction between an identity, a paid error and an effective bound.

## Fixed source and collision geometry

Use the canonical \(\Phi\), with all integer-square coefficients retained,
\[
H_\lambda(z)=\int_0^\infty e^{\lambda u^2}\Phi(u)\cos(zu)\,du,\qquad
\partial_\lambda H_\lambda=-H_{\lambda,zz}.
\]
The half-line primitive satisfies
\(p(u)=e^u\sum_{n\ge1}e^{-\pi n^2e^{4u}}\), \(p''-p=8\Phi\).
Its transform \(\mathcal P_\lambda\) obeys
\[
8H_\lambda=\tfrac12+(2\lambda-1-z^2)\mathcal P_\lambda
+4\lambda z\mathcal P_\lambda'-4\lambda^2\mathcal P_\lambda''.
\]
These are inherited identities, not positivity estimates; see
[parent Note11 §§3–4](../../notes/11_TND_O_B02_CRITICAL_COEFFICIENTS_THETA_AND_RODGERS_TAO_20261106.md).

For forward imaginary time write \(h(\tau,z)=H_{\lambda_0-\tau}(z)\),
so \(h_\tau=h_{zz}\). A generic real double event has
\(h=h_z=0\), \(a=h_{zz}\ne0\). Near it, a real pair disappears into
a conjugate pair as tau increases. Higher multiplicities are separate
cases; B01 may select the generic pair and must state that restriction.

Two useful coordinates already exist. Along \(h_z(\tau,x_c(\tau))=0\),
\[
v(\tau)=h(\tau,x_c(\tau)),\qquad
v'=h_{zz},\quad x_c'=-h_{zzz}/h_{zz}.
\]
For a local isolated pair, factor
\(h=(z-r_-)(z-r_+)F\), with F nonzero on a suitable neighborhood.
With \(\delta=r_+-r_-\), \(q=\delta^2\), and
\[
B(\tau)=\int_0^1(\log F)_{zz}(\tau,r_-+t\delta)\,dt ,
\]
the inherited exact law on the real simple-pair side is
\[
q'=-8-4qB.
\]
The integrating-factor form shows the actual consumer:
\[
q(\tau)=e^{-4\int_0^\tau B}
 \left[q(0)-8\int_0^\tau e^{4\int_0^s B}\,ds\right].
\]
The bracket needs a positive lower bound on the interval in question.
A source-dependent bound for B, an initial gap and a valid isolated-pair
domain are therefore substantive inputs. Writing this formula supplies
none of them. The reference time 0 here is a chosen tau origin, not
necessarily Newman time zero.

[Parent Note07 §§3–4](../../notes/07_TND_O_B02_COLLISION_ANATOMY_20261106.md)
derives the critical-value and gap laws; they have proof-author checks.
[Parent Note11 §4](../../notes/11_TND_O_B02_CRITICAL_COEFFICIENTS_THETA_AND_RODGERS_TAO_20261106.md)
already links exterior jets to contours and records an unfavorable
finite contour-versus-direct budget. This is a baseline to improve,
not a new contour idea to rediscover. Event-conditioned real-zero
product inequalities there retain their extra hypotheses.

## Candidates, comparator and unresolved choices

The first B01 cycle compared the following two candidates:

1. **Event-conditioned source or primitive jets.** Choose a ratio or
   signed combination whose bound has a specified effect on a critical
   value or collision neighborhood. Determine whether complete
   arithmetic supplies information beyond source positivity, endpoint
   matching and the already studied conditional real-zero bounds.
2. **Localized gap and exterior-force control.** Seek a complete
   source estimate on B, or a controlled time-integrated substitute,
   that changes a declared gap-lifetime or exclusion bound. Pay
   deflation, boundary nonvanishing, exterior/tail and time errors.
   Reuse the direct comparator and prior contour result.

For either candidate the existing
[Green potential](../../notes/25_TND_O_B03_R5_COMPLETE_GREEN_STRIP_POTENTIAL_20261107.md)
is a comparator for a nonreal defect, with margin
\(m(d,r)=d\sin(\pi/8)/\cosh(\pi r/8)\).
[OG acquisition](../../01_green_potential_resolvent/notes/06_TND_OG_E03_COMPLETE_SIGNED_LOG_ACQUISITION_20261108.md)
pays approximation but not the favorable upper value; its
[resolution analysis](../../01_green_potential_resolvent/notes/09_TND_OG_B04_GREEN_MASS_RESOLUTION_AND_VALUE_DECISION_20261108.md)
limits broad averaging. A real double event itself has zero upper-half-plane
Green mass, so an event-to-defect/time bridge must be stated when using it.

The [OC friction note](../../02_localized_zero_correlations/notes/14_TND_OC_B08_ARITHMETIC_MARGINAL_COLLISION_FRICTION_20261108.md)
explains why a fixed smooth marginal estimate need not bound a singular
interaction and records the premise-level collision-control screen.
No theorem forbids using stronger marginals here if they later pay a
specific consumer. No inherited asymptotic or density estimate is treated
as a pointwise collision exclusion.

The setup choices were resolved in part by the 9 November B01 cycle:
nondegenerate local double events, a parameterized compact positive-Newman-time
box, and the finite real-pair lifetime consumer. The selected acquisition
uses classical divided differences of the complete source to remove the
actual pair before evaluating its regular factor. [Note02](../notes/02_TND_OA_B01_REGULAR_DEFLATION_AND_FORCE_TRANSFER_20261109.md)
derives complete source-tail errors, conditioned signed force transfer,
and explicit midpoint/upper-gap confinement before the survival argument.
It is **proved in-note** and accepted under its fixed premises by the
separate-chat [E01 assessment](../reviews/03_TND_OA_E01_R1_REGULAR_DEFLATION_ASSESSMENT_20261109.md).

The derivative transfer uses coupled information from the complete
source. B02 selected one candidate box from the existing RT/HDC pair;
the E01 model's full-box denominator, signed force and strict margins
remain unacquired.

The comparison now includes a regular direct divided-difference evaluator.
Small root slopes alone do not show a contour advantage. Conversely,
the uniform real parameter-box floor may fail where a contour method is
usable. No method dominates on the information acquired so far.

## B02 finite pilot decision

On 9 November, [Note06](../notes/06_TND_OA_B02_CANONICAL_PILOT_AND_REDUNDANT_GAP_GATE_20261109.md)
screened one canonical box for Newman times \([1/20000,1/10000]\).
The strongest inherited complete-source comparison already proves
survival of that population on a larger interval. The new elementary
screen \(Q_-Q_+>32D^2\Delta\) also shows, conditionally on E01's floor
and confinement data, that the unsigned bound \(B\le K\) suffices for
its gap margin. On the selected box the signed average therefore would
not change the survival verdict. Existing jets expose a conditioning
loss for the particular uniform-ratio midpoint allowance.

These implications are **proved in-note, with proof-author self-check
only**. The resulting [decision](../brainstorm/notes/02_TND_OA_B02_PILOT_NO_RUN_DECISION_20261109.md)
is not to run that pilot for the proposed consumer. It does not prove
the candidate's center curvature or full factor floor fails, and it
does not exclude other geometries or estimators. This is a finite design
diagnostic under [known-region11](../../../../../../avoid/11_certifying_the_known_and_tests_that_cannot_fail.md)
and [scope07](../../../../../../avoid/07_scoped_exclusions_read_as_universal.md).

B03 subsequently screened one replacement candidate and used its one
focused clarification, as recorded below.

## B03 source-readiness and bound-direction return

9 November: [Note08](../notes/08_TND_OA_B03_LEHMER_DIRECTION_AND_ACQUISITION_STOP_20261109.md)
records the first Lehmer pair as a candidate for positive-time survival
ending at zero. The inspected records do not provide its actual positive
starting tuple or a quantitative gap in the direct comparison. Under the
additional real-exterior product premise, the endpoint sum obeys
\(G+2B=qS\ge0\). An upper \(G\) therefore gives a lower \(B\), whereas
E01 survival uses an upper \(B\). An exact polynomial heat control passes
the small-gap diagnostic and retains negative force but still collides.

The algebra and control are **proved in-note** and accepted at their
stated scope in the [E02 assessment](../reviews/06_TND_OA_E02_R1_LEHMER_SCREEN_ASSESSMENT_20261109.md). The diagnostic
limits this use of the exterior sum under the real-product premise.
The control-premise audit remains tied to
[controls12](../../../../../../result-summaries/12_collision_controls_and_screening.md)
and [scope07](../../../../../../avoid/07_scoped_exclusions_read_as_universal.md).

[Decision03](../brainstorm/notes/03_TND_OA_B03_PARK_FINITE_PAIR_ACQUISITION_20261109.md)
parks the present finite-pair acquisition cycle.
[Continuation11](../notes/11_TND_OA_AFTER_E02_CONTINUATION_AND_MODEL_CHANGE_20261109.md) names the evidence needed to reopen it.
