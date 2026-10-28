# Continuation of radial integrand preservation and collision localization

27 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort max**. Investigation05 chat0007, **Explore collision-localizing deforms**, thread `01a18047-0177-7ad2-878f-19ed2eaa1a37`.

**Continuation update, chat0008, 27 October 2026:** Notes22–23 completed the bounded return to this handoff. The current handoff is [Note25](25_TOTAL_INTEGRAL_CONSERVATION_AND_DIRECTION_FREE_HEAT_FLOW_20261027.md): Edward Baker now requires preservation only of the entire observation integral and seeks simple direction-independent collision dynamics. The radial integrand may change. [Note24](24_EXPLICIT_THETA_FLOW_AND_COLLISION_MAGNIFICATION_SCOPE_20261027.md) explains the earlier projected flow and explicit theta input. The instructions below retain the historical chat0007 requirement and priority, now superseded at the general-program level.

**Original next step — LOC-02: derive and assess the complete signed identity on a finite angular tube around the collision-adapted curve.** The sole invariant is the complete one-dimensional radial integrand. Equations, fields and auxiliary dynamics may change. The purpose is to find a representation in which the cancellation at a hypothetical positive-time collision becomes easier to analyze.

The [rewritten overview][overview] defines the current program and the [progress register][progress] owns its task states. This note is the next-session handoff. [Note19][n19] retains the earlier Darboux continuation and subsequent priority amendment; its interior-node study is an optional supporting branch, not a prerequisite. This handoff records the current position and proposed work; it adds no mathematical result.

## Read in this order

1. Repository [AGENTS.md][agents] and [chat-history instructions][chatworkflow], then the [result index][results] and [patterns to avoid][avoid]. Consult the specific [collision controls][controls], [geometric realizations][realizations], [target classification][a01], [transported-identity caution][a03] and [scope rule][a07].
2. The current overview and progress register. LOC-01 supports the construction of admissible equations; LOC-02 is the immediate tube calculation; LOC-03 develops a projected Laplacian flow. LOC-04 is the later canonical estimate and LOC-05 its possible threshold application. These tasks remain open.
3. [Manuscript Sections 9–10][manuscript], [Note20][n20] and [Review12][review12] for the exact finite-parameter constructions and their verification scope.
4. [Brainstorm02][b02] for the two localization routes. [Brainstorm01][b01] preserves Edward Baker's original proposal, clarification of the invariant and the control-premise table. Use earlier source and Darboux notes when a calculation needs them.

## What can be used immediately

The following are established by direct calculation with same-assistant checking: the Laplacian projection identity, normalized angular concentration and transport flows, the full multiplicative operator and boundary map, explicit angular leakage and norm costs, and the collision-adapted first-moment identity. They are finite-parameter representation and localization results. No theta collision exclusion, complete signed tube comparison, global projected-flow construction or all-height estimate has been established.

Let \(P\) denote spherical averaging with \(d\nu=d\Omega/(4\pi)\). The radial density is

\[
\mathcal I(t,z;r)=\frac18r^{3/2}Q_t(r)
                         \cos\!\left(\frac z2\log r\right),
\qquad H(t,z)=\int_1^\infty\mathcal I(t,z;r)\,dr.
\]

The general invariant is \(P\mathcal J_s=\mathcal I\) at every radius. The source condition \(PF_{s,t}=Q_t\) is one sufficient realization, not the definition of every allowed deformation. In \(u\), use \(r=e^{2u}\), \(dr=2r\,du\), and density \(e^{tu^2}\Phi(u)\cos(zu)\). Radial symmetry, positivity of the deformed fields, an unchanged energy or spectrum, and Darboux form are not extra invariants.

The normalized flow is

\[
A_s=\frac{e^{sq}}{P(e^{sq})},\qquad
\partial_sA_s=(q-P(qA_s))A_s,\qquad A_0=1,
\qquad F_{s,t}=A_sQ_t.
\]

Here \(s\) is auxiliary time. For the current example, \(q\) is fixed independently of the running physical time and frequency. Freeze a candidate \(T>0\), \(a_*>0\) and scale \(b>0\), and put

\[
v(u)=(\cos(a_*u),-bu\sin(a_*u),0),\quad
m=|v|,\quad n=v/m,\quad q(r,\omega)=n(\log r/2)\cdot\omega.
\]

Then \(m>0\), and for \(s>0\), with \(\rho_T=e^{Tu^2}\Phi\),

\[
\int_0^\infty\rho_Tm\,P(\omega A_s)\,du
=(\coth s-1/s)(H(T,a_*),bH_z(T,a_*),0).
\]

Thus the first-jet cancellation is represented near \(\Gamma(u)=e^{2u}n(u)\). The physical event is unchanged. This does not remove its radial contributions or assert that a zero vector moment is impossible.

For the response, take \(\lambda=z^2/4>0\) on the positive real frequency axis and retain the selected solution from the manuscript:

\[
\psi=r^{-1/2}Y(\log r),\quad
L_\lambda=\Delta+\frac{\lambda+1/4}{r^2},\quad
L_\lambda\psi=Q_t.
\]

With \(\ell_s=\log A_s\) and \(\psi_s=A_s\psi\),

\[
L_{\lambda,s}=A_sL_\lambda A_s^{-1}
=\Delta-2\nabla\ell_s\cdot\nabla+
 \frac{\lambda+1/4}{r^2}+|\nabla\ell_s|^2-\Delta\ell_s,
\qquad L_{\lambda,s}\psi_s=A_sQ_t.
\]

The physical boundary operator is

\[
\mathcal R_sf=[(r\partial_r+1/2-r\partial_r\ell_s)f]_{r=1},
\qquad P\mathcal R_s\psi_s=B(t,\lambda)=-8H(t,2\sqrt\lambda),
\qquad P\mathcal R_s\partial_\lambda\psi_s=B_\lambda.
\]

Keep \(a_*\) fixed when differentiating the running spectral parameter. The observation follows from the selected response and transformed boundary map; an arbitrary homogeneous boundary problem cannot be substituted for it.

## The bounded LOC-02 calculation

1. **Specify the domain.** Use finite \(0\le s\le S\), \(b>0\), \(0<\delta<\pi\), and \(1<r_-<r_+<\infty\). Work near the fixed positive candidate frequency as needed for spectral differentiation. Define the angular tube

   \[
   \Omega_\delta=\{r_-<r<r_+,\ \omega\cdot n(\log r/2)>\cos\delta\}.
   \]

   Its width is angular; the physical width varies with radius. Keep the full selected response when restricting it to this domain.
2. **Derive the current and every boundary term.** Start from \(L_{\lambda,s}\psi_s=A_sQ_t\) and its spectral derivative. State the integration measure and the appropriate Green identity for that operator. Include drift and potential contributions, the lateral boundary with its radius-dependent normal, and both radial faces. Preserve cutoff derivative terms if cutoffs are introduced. The tube boundary does not acquire zero data merely because \(H=H_z=0\).
3. **Reconnect the tube to the physical observation.** Retain the complementary angular region and the intervals \(1\le r\le r_-\) and \(r\ge r_+\), either exactly or through justified estimates. The physical boundary is at \(r=1\); the artificial inner face at \(r_-\) does not replace it.
4. **Account for localization costs.** Note20 gives

   \[
   P(A_s\mathbf1_{q\le\cos\delta})
   \le\frac{e^{-s(1-\cos\delta)}}{1-e^{-2s}},\qquad
   P(A_s^2)=s\coth s.
   \]

   The leakage bound controls the specified angular mass, not every response or boundary term. Retain the \(n'(r)\), \(n''(r)\) terms in manuscript equation `eq:steeringcost`. No uniform inverse at \(s=\infty\) is available.
5. **Make the comparison.** Identify what is an exact pullback of the radial identity and what signed quantity might become easier to estimate. Compare using the same source information and complete error allowances. The full induced energy in \(A_s^{-2}d^3X\) already pulls back exactly; repeating that fact is not a new gain. Its scope does not rule out other signed local estimates.
6. **Screen and assess.** Check the exact Gaussian-polynomial collision from the manuscript during the derivation, then the relevant registered controls. A generic localized identity should remain compatible with their events. A claimed theta separation must identify the canonical premise actually used and prove its effect on the estimate.

**Completion test:** a full localized identity with a substantive comparison, a new controlled structural consequence, or a precise obstruction for the tested comparison. The cap formula or a restatement of \(H\) alone is insufficient. A scoped limitation is a useful return; it does not close all radial-integrand-preserving deformations. Save the derivation and assessment before selecting a larger family or numerical campaign.

## The complementary LOC-03 route

If the complete tube comparison only transports the known cancellation, record that conclusion at its tested scope and develop the bounded prototype from Brainstorm02. For fixed physical time on a spherical annulus, take

\[
F=Q_t+G,\qquad
\partial_sG=\varepsilon\Delta G-(I-P)[\chi_{\rm out}(Q_t+G)],
\qquad G_0=0,\quad G|_{\partial\Omega}=0,
\]

with smooth \(\chi_{\rm out}\ge0\) and \(\varepsilon>0\). For smooth solutions, \(PG=0\) persists and the stated energy

\[
\mathcal E(G)=\frac12\int_\Omega\chi_{\rm out}(Q_t+G)^2\,d^3X
 +\frac\varepsilon2\int_\Omega|\nabla G|^2\,d^3X
\]

satisfies \(d\mathcal E/ds=-\int_\Omega|\partial_sG|^2\,d^3X\). These remain conditional identities. Establish a precise solution class and well-posedness, regularity and boundary compatibility before claiming a completed evolution result. Address radial joins and the full response/observation map before extending it globally.

The present objective measures source localization. An objective tied to the collision equations requires the response variation and its adjoint; neither has been derived for this prototype. Positivity is not guaranteed or required by the user's invariant. LOC-03 is an early alternative, not evidence that the existing energy already controls collisions.

## Controls and scope to retain

The [existing premise table][b01] and [control register][controls] distinguish the Gaussian-polynomial, Euler-factor, weighted-square, finite-prime, reflected and positive-primitive examples. The generic constructions preserve their own marginals and collisions on their convergence domains. They lack the unchanged canonical theta marginal in the recorded ways, but that does not prove they fail an unconstructed inequality. Atomic examples require a measure or distribution formulation for PDE claims.

The first-moment identity covers multiplicity at least two; it does not classify higher jets. Bounds proved for one candidate frequency are not all-height bounds. Before LOC-05, read the [existing positive-threshold reduction][threshold] and check its uniform localization and multiplicity requirements. No positive-threshold contradiction has been acquired by this session.

## Save the return and preserve continuity

Write the next derivation in `notes/`, its assessment in `reviews/`, and only justified computations with small records in `numerics/`. Include date, author, actual model/effort and verification scope. Update the LOC progress entries without recounting old RDZ foundations as new completions. Use the [large-file policy][largefiles]; record actual manuscript milestones in `DRAFT_HISTORY.md` without snapshot folders.

The active source is [radial_deformations_and_zero_dynamics.tex][manuscript]. Its recorded 13-page build and checks are in [build record13][build]. This handoff leaves that source unchanged. When revising the open document, edit it in place and use the built-in LaTeX compilation check; keep its current editor open and follow the user's instruction against replacement documents or separate PDF builds. Inspect current working changes before editing; the program rewrite has pending local changes at handoff preparation.

This conversation has one canonical registration: **chat0007**, thread `01a18047-0177-7ad2-878f-19ed2eaa1a37`, in the investigation's [history registry][history]. A new session uses its own actual thread identity and title. Follow the standing recorder at the beginning and end of replies, preserving existing registrations and arranging the bounded exact-turn final capture when no trusted completion hook is verified. Do not hand-edit generated history JSON or prewrite a future answer into the archive.

[overview]: ../research-overview/03_RADIAL_DEFORMATION_AND_ZERO_DYNAMICS_RESEARCH_OVERVIEW_20261027.md
[progress]: ../research-progress/03_RADIAL_DEFORMATION_AND_ZERO_DYNAMICS_RESEARCH_PROGRESS_20261027.md
[n19]: 19_RADIAL_DEFORMATION_AND_ZERO_DYNAMICS_CONTINUATION_20261027.md
[n20]: 20_AUXILIARY_ANGULAR_FLOWS_AND_COLLISION_LOCALIZATION_20261027.md
[manuscript]: ../radial_deformations_and_zero_dynamics.tex
[review12]: ../reviews/12_RADIAL_INVARIANT_AND_ANGULAR_FLOW_SELF_ASSESSMENT_20261027.md
[b01]: ../brainstorm/01_RADIAL_INTEGRAND_PRESERVING_DEFORMATIONS_AND_COLLISION_LOCALIZATION_20261027.md
[b02]: ../brainstorm/02_AUXILIARY_FLOWS_FOR_COLLISION_LOCALIZATION_20261027.md
[build]: ../numerics/13_ANGULAR_FLOW_MANUSCRIPT_BUILD_RECORD_20261027.json
[history]: ../chat-histories/index.json
[threshold]: ../../02_heat_flow_rh_applications/notes/02_RODGERS_TAO_POSITIVE_THRESHOLD_20261026.md
[agents]: ../../../../AGENTS.md
[chatworkflow]: ../../../../tools/CHAT_HISTORY.md
[largefiles]: ../../../../LARGE_FILES.md
[results]: ../../../../result-summaries/README.md
[avoid]: ../../../../avoid/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[realizations]: ../../../../result-summaries/16_hypercomplex_reductions_and_geometric_realizations.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a03]: ../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
