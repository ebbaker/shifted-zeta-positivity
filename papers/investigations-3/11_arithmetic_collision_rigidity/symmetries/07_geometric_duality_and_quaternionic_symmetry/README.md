# S07 Geometric duality and quaternionic symmetry

18 October 2026, America/New_York. Prepared for Edward Baker with substantial
LLM assistance. Actual authoring model **gpt-6.1-sol (Codex)**, reasoning
effort **ultra**, verified from the initializing turn metadata.
Open exploratory investigation. The first zero-form Green-identity round
is complete, with a scoped first-order trace obstruction and exact source
flux evaluation; an independent physical estimate remains open.

## Question and origin

Can Poincaré/relative duality, quaternionic J/K and twistor structures,
hyperholomorphic bundle identities, or related geometric symmetries make
the complete signed theta observation easier to estimate?

This direction was opened at Edward Baker's request following the
[geometric coverage review][coverage]. That review identified geometric
possibilities beyond bare Hodge star and computed the first J/K source
insertions. The [initial note][initial] consolidates those findings, their
proofs and limitations as the starting point for this investigation.
It includes the diagonal tensor-Hessian correction and the exact endpoint
of the resulting damped observation. These are inherited findings from
the opening review, not additional discoveries made by creating S07.

The [program guide][guide] supplies the common normalization, control
families, numerical gates and global scope. Read the repository
[result summaries][summaries] and [patterns to avoid][avoid], particularly
[controls][controls], [geometric realizations][geometry],
[generic lifts][a03], [scoped exclusions][a07] and [signed cancellations][a12].

## Opening investigation result

[Note 02](notes/02_ZERO_FORM_GREEN_IDENTITY_AND_PHYSICAL_TRACE_OBSTRUCTION_20261018.md) derives the polarized J-Green identity on the
fixed tube with all faces, a global physical dual test, and the canonical
source's zero integrated self-flux. It proves no generic first-order
bulk-energy bound controls the codimension-three physical path, even with
zero boundary current. The raw rough-Laplacian source also restores a
growing zero mode and fails ordinary positive-time half-line integration.

The [internal assessment](reviews/02_GREEN_IDENTITY_AND_TRACE_OBSTRUCTION_INTERNAL_REVIEW_20261018.md) accepts this scoped
obstruction. [Exact algebra and fresh inherited controls](numerics/README.md)
are recorded separately. These conclusions do not exclude estimates using
the canonical theta/PDE constraints, paid higher regularity, other form
degrees or a complete mixed boundary current. The next contract must add
one such ingredient; repeating the generic zero-form energy transfer is
not the next task. No new physical sign or region is claimed.
Prepared for Edward Baker with substantial LLM assistance, **gpt-6.1-sol,
actual effort ultra**, 18 October 2026; same-model internal review.

## Relation to the other directions

[S06][s06] retains the already developed base-p observation, finite
normalized-jet obstruction, complete source compensation, and coupled
two-source estimates. S07 studies the broader geometric actions and
duality frameworks, with a first focus on mixed quaternionic or
hyperholomorphic identities and their physical observations.

The prior S06 notes, review, checker and records remain at their existing
paths. Use them directly. A new name for an existing completed source,
relative Euler criterion, or unknown signed trace is not a new estimate.
[S05][s05] supplies the normalized source ladder; S01 and S03 are possible
consumers of an eventual improved arithmetic or first-jet estimate.

## Mathematical starting point

Keep the physical field and its scales fixed:

\[
 H(t,x)=\int_0^\infty e^{tu^2}\Phi(u)\cos(xu)\,du,
 \quad H_t=-H_{xx},\quad
 E=H^2+H_x^2,\quad\mathcal L_0=H_x^2-HH_{xx}.
\]

On the marked elliptic family M=ℍ×T², write τ=p+iq, z=r+τs and
q=e^(4u) on γ(u)=(p=r=s=0,q=e^(4u)). Use the existing semi-flat
metric, adapted theta line connection, arithmetic frame and complete
source extension. The [initial note][initial] states them explicitly.

For X=γ̇=4q∂q and IJ=K,

\[
 IX=-4q\partial_p,\qquad JX=-4q\partial_s,\qquad
 KX=4q^2\partial_r.
\]

Thus tangent J/K act in the elliptic fiber. They are not a quarter turn
in the spectral jet plane, a scalar action on the complex line fiber,
or a diffeomorphism preserving the full physical transform.

Available starting findings:

- Standard noncompact Poincaré duality pairs H²(M) with H_c²(M).
  Its fixed theta fiber degree is +1; no physical sign follows from it.
- Relative Euler/boundary winding already detects theta heat collisions
  with the all-multiplicity sign law from Investigation 22.
- The first J/K fiber insertions of the declared source vanish. The
  literal second J insertion restores a divergent zero mode. The second
  K insertion equals the S06 q-weighted base-p channel.
- The diagonal tensor Hessians add opposite corrections
  Φ′/(8q³); their exact half-line observation retains a lower endpoint.
- The ASD connection is hyperholomorphic in the curvature sense. The
  distinguished theta section is not simultaneously holomorphic for I
  and J. The complex line fiber has no automatic quaternionic structure.

These facts delimit particular constructions. Mixed derivatives,
coupled identities, relative boundary estimates and nonlocal constraints
are not excluded by the diagonal or finite-parity calculations.

## Read in this order

1. [Initial findings][initial] and [initial internal assessment][assessment].
2. [Coverage review][coverage] for the full geometric applicability table
   and primary literature checked during the opening review.
3. [Investigation 22 manuscript][manifold], especially Hodge pairings,
   hyperkähler metrics, the marked elliptic family and ASD connection.
4. [Adapted metric and physical restriction][metric], and S06
   [Note 01][transverse] and [Note 02][completion], for all connection,
   convergence, endpoint and compensation conventions.
5. [Spacetime topology][winding] and its [completed pilot review][pilot]
   before proposing a new relative Euler or winding mechanism.
6. [Checks and source records](numerics/README.md) before using the formulas
   in a computation. Finite algebra replay is not a sign certificate.

## Original bounded task (executed in Note 02)

Begin with **one polarized J-Dolbeault/Weitzenböck Green identity** for
the existing line connection on the fixed tube
\(\Omega=\{-1/4\le p\le1/4,\ 1\le q\le4\}\times T^2\).
State the exact operator and form degree, complete source section, dual
test, coordinate extensions and candidate physical consumer. Compute all
commutators and the complete source expression before restriction.

First decide whether the proposed channel survives parity and zero-mode
cancellation and has an ordinary convergent physical heat transform.
Retain each integration-by-parts endpoint. Determine whether the channel
returns a known S06 completion or a physical derivative, or leaves a
distinct signed remainder with a specified possible estimate.

Derive the full boundary flux on every p/q face and the observation map
before claiming coercivity. The dual test needs a genuine smooth bundle
extension agreeing with the prescribed physical covector; a constant
coefficient in one arithmetic frame is not automatically a global section
on the torus. State every coefficient-
bundle, type, primitive, support and operator-domain hypothesis being used.
No auxiliary norm is a lower bound for E without a separate comparison.
In particular Λ_JF=0 for the ASD curvature, so no favorable scalar
curvature term is assumed. Evaluate any curvature action in the chosen
form degree. Pay any regularity/derivative cost needed to restrict an
ambient estimate to the physical curve. The q=4 face and source tail
beyond u=log(4)/4 remain part of a complete physical comparison.

Only after this contract identifies an independently estimable term should
a bounded comparison use t∈[1/100,1/5], x∈[999,1001], with the same physical
normalization and complete error accounting as the program reference.
An alternative relative-winding comparison should reuse the existing
[25,45] pilot before selecting new coverage. Agreement on these pilots
validates a method; it is not new exclusion coverage.

## Decision rules and controls

Pass the opening research gate with an exact complete observation map
and a new, independently justified estimating consequence, or with a
proof/counterexample for a precisely stated transfer class. A subsequent
quantitative milestone requires a paid signed bound, smaller complete
error, measured matched cost gain, larger certified region or effective
onset, under the [program's gates][guide].

Stop the selected mechanism if it only returns the old unknown sign,
imports that sign into its assumptions, requires a divergent uncompleted
transform, drops a boundary or commutator, or depends on an unbounded
auxiliary-to-physical comparison. Repeatedly applying the same literal
J/K diagonal insertions is not the next task. A scoped stop does not
exclude every geometric continuation.

Use the [control map in the initial note][initial] and [summary 12][controls].
Generic geometric identities can hold for a colliding control. A claimed
strict physical bound must fail on a domain containing its event; a local
certificate need not fail on every collision-free control domain. Weighted
square sources share local heat/vertical differentiation, not full Jacobi
automorphy or canonical theta-bundle descent. Reflection alone does not
distinguish the reflected super-Gaussian control.

Global first-jet exclusion and all-degree Jensen-topology criteria retain
their recorded RH strength; reformulating them once is distinct from a
bounded estimating milestone. No new region or global sign estimate has
been established by this investigation's initialization.

## Organization and histories

| Folder | Purpose |
| --- | --- |
| [notes](notes/README.md) | Initial findings and subsequent exact maps, proofs and failed estimates |
| [numerics](numerics/README.md) | Small source/replay records and future investigation-specific code |
| [reviews](reviews/README.md) | Internal assessments with explicit verification limits |
| [chat-histories](chat-histories/README.md) | Future S07 registrations and links to inherited conversations |

Record actual model/effort, date, source identities, domains, all boundary
and derivative costs, the accepted hypotheses, controls and next decision.
Follow [LARGE_FILES.md][large]. Milestones go in the parent investigation's
[draft history][history]; create no manuscript snapshot folders.
The originating conversation retains its unique S06 registration; opening
this folder does not relocate or duplicate its history.

[initial]: notes/01_POINCARE_DUALITY_AND_QUATERNIONIC_SYMMETRY_INITIAL_FINDINGS_20261018.md
[assessment]: reviews/01_INITIAL_NOTE_AND_INVESTIGATION_SETUP_REVIEW_20261018.md
[guide]: ../../research-overview/03_SYMMETRY_RESEARCH_PROGRAM_AND_INVESTIGATION_GUIDE_20261018.md
[coverage]: ../06_hodge_and_transverse_geometry/reviews/03_GEOMETRIC_SYMMETRY_COVERAGE_POINCARE_AND_HYPERKAHLER_20261018.md
[s06]: ../06_hodge_and_transverse_geometry/README.md
[s05]: ../05_covariant_theta_jets/README.md
[summaries]: ../../../../../result-summaries/README.md
[avoid]: ../../../../../avoid/README.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[geometry]: ../../../../../result-summaries/16_hypercomplex_reductions_and_geometric_realizations.md
[a03]: ../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[manifold]: ../../../../investigations-2/active/22_theta_manifold_geometry/manuscript/theta_manifold_geometry.tex
[metric]: ../../../../investigations-2/active/22_theta_manifold_geometry/notes/03_theta_bundles_and_connections/02_ASD_METRIC_FREEDOM_AND_PHYSICAL_RESTRICTION_20261015.md
[transverse]: ../06_hodge_and_transverse_geometry/notes/01_TRANSVERSE_OBSERVATION_AND_FINITE_JET_OBSTRUCTIONS_20261018.md
[completion]: ../06_hodge_and_transverse_geometry/notes/02_SIGNED_TRANSVERSE_ESTIMATE_AND_EXACT_SOURCE_COMPENSATION_20261018.md
[winding]: ../../../../investigations-2/active/22_theta_manifold_geometry/notes/01_physical_jet_geometry/04_SPACETIME_INDEX_AND_MARKED_TOPOLOGY_20261015.md
[pilot]: ../../../../investigations-2/active/22_theta_manifold_geometry/reviews/18_SPACETIME_BOUNDARY_AND_GEOMETRIC_CONTINUATION_REVIEW_20261015.md
[large]: ../../../../../LARGE_FILES.md
[history]: ../../DRAFT_HISTORY.md
