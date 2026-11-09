# Collision constraints: scientific overview

8 November 2026, America/New_York. Prepared for **Edward Baker** with substantial OpenAI Codex assistance. Actual recorded model and effort are unavailable, existing OC chat0006. Setup only; no new branch research or numerical execution is activated.

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

B01 compares at most two candidates:

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

Still undecided: event type, compact or asymptotic domain, normalization,
the source-dependent inequality, the actual margin to improve, and the
method for estimating it. These are B01 choices. Consequently no E01
execution packet or numerical campaign is ready.
