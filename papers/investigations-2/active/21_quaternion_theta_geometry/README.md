# Quaternion theta geometry and RH criteria

14 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded model: **gpt-6.1-sol (Codex)**; reasoning effort: **ultra**.

**Investigation 21 is active at Edward Baker's request.** It develops the
quaternion first jet of the theta heat family as a possible source of a
signed current or boundary identity that excludes positive-time zero
collisions. The exact first-order equations and RH criterion map are the
starting point. A complete-source central norm bound and quantitative
imaginary-gluing stability estimate are now proved; the collision-excluding
signed estimate at unknown heights remains open.

This program was promoted from the quaternion branch of
[investigation 20](../20_constrained_operator_squares/README.md).
The [original quaternion note](../20_constrained_operator_squares/brainstorm/02_QUATERNION_JET_AND_HEAT_OPERATOR_20261014.md)
and [original handoff](../20_constrained_operator_squares/brainstorm/03_QUATERNION_CONTINUATION_20261014.md)
retain the proposal's provenance. New quaternion research belongs here.

## Start here

For the next session, read the [continuation note](notes/7_CONTINUATION_AND_NEXT_SIGNED_ESTIMATE_20261014.md),
which fixes the next bounded signed estimate and the recommended workflow.

1. [Self-contained manuscript](manuscript/quaternion_theta_geometry.tex)
   derives the scalar RH criteria and their quaternion translations, with
   complete proofs of the bounded theta estimates. Its
   [integration review](reviews/4_MANUSCRIPT_CONVENTION_AND_FOUNDATION_AUDIT_20261014.md)
   records the convention, foundation, and equation checks.
2. [Standard Fueter lift with independent time](notes/3_STANDARD_FUETER_LIFT_WITH_INDEPENDENT_TIME_20261014.md)
   fixes the adopted quaternion coordinates and proves regularity while
   keeping Newman time separate.
3. [RH criteria and quaternion setup](notes/1_RH_CRITERIA_AND_QUATERNION_SETUP_20261014.md)
   fixes the source, exact RH endpoints, stationary signs, bounded
   losses, and polynomial control.
4. [Initial research program](notes/2_INITIAL_RESEARCH_PROGRAM_20261014.md)
   specifies the first deliverable and the conditions for continuing.
5. [Cauchy Fueter boundary and current reformulations](notes/4_CAUCHY_FUETER_BOUNDARY_AND_CURRENT_REFORMULATIONS_20261014.md)
   gives conjugate-Fueter evolution, signed boundary moments, and a
   unified norm-time stationary target.
6. [Complete theta central estimate](notes/5_COMPLETE_THETA_CENTRAL_ESTIMATE_20261014.md)
   proves an analytic norm gap on \(0\le t\le1,|x|\le8\), with the
   entire source tail paid.
7. [Imaginary gluing stability](notes/6_IMAGINARY_GLUING_STABILITY_AND_HEIGHT_OBSTRUCTION_20261014.md)
   bounds physical jet errors from the full angular defect at one scale
   and identifies the remaining high-height compensation.
8. [Investigation 20's manuscript](../20_constrained_operator_squares/manuscript/constrained_operator_squares.tex)
   supplies the imported collision reduction, predecessor charts,
   locally bounded loss theorem, and existing operator obstructions.

## Objective and first target

Keep Newman time t as an independent real parameter, use
\(q=z_0+\mathbf jz_1\), and define the adopted theta field

\[
F(t,q)=H(t+\overline{z_1},z_0)
+\mathbf jH_z(t+\overline{z_1},z_0).
\]

It is standard left Fueter-regular for each real t. At real quaternion
argument q=x, it equals \(H(t,x)+\mathbf jH_x(t,x)\). The exact endpoint is

\[
\boxed{\mathrm{RH}\quad\Longleftrightarrow\quad
F(t,x)\ne0\quad\text{for every }t>0,\ x\in\mathbb R.}
\]

The physical norm is \(\mathcal E(t,x)=|F(t,x)|^2=H^2+H_x^2\).
The second complex coordinate is independent and acts as a heat-time
displacement inside H; it does not replace external time.

The initial construction target is a theta-specific identity controlling
both stationary Laguerre forms, or allowing a negative loss bounded by
\(K_j\mathcal E\) with \(K_j\) locally bounded through every candidate
collision. Each proposed estimate must state its domain and how it covers
the relevant predecessor curves.

The separate spectral alternative is
\(\mathcal C_0(0,z)\ge0\) for every complex z, where
\(\mathcal C_0=\tfrac12\partial_y^2|H(t,x+iy)|^2\).
The total quaternion norm cannot replace the scalar modulus in that criterion.

## First research deliverable

The [boundary and current note](notes/4_CAUCHY_FUETER_BOUNDARY_AND_CURRENT_REFORMULATIONS_20261014.md)
records exact general identities and their remaining signed target.
The [central bound](notes/5_COMPLETE_THETA_CENTRAL_ESTIMATE_20261014.md) and
[gluing defect estimate](notes/6_IMAGINARY_GLUING_STABILITY_AND_HEIGHT_OBSTRUCTION_20261014.md)
supply bounded source-specific results. The next deliverable must control
the full signed arithmetic cross terms on unknown-height predecessor domains.

Produce one short formula note giving either an exact theta-specific
current or boundary identity with its unresolved signed remainder, or a
precise obstruction for a declared operator class. State which criterion
the identity controls and which arithmetic source property it uses.
Retain the jet constraint, every oscillatory term, boundary contribution,
and approximation remainder. An operator factorization alone does not
establish the observation's sign.

## Connections and scope

- [20](../20_constrained_operator_squares/README.md) retains the general
  constrained operator method and quantum-energy application. This
  investigation focuses on the quaternion theta branch.
- [02](../02_angular_jacobi_gluing/README.md) supplies the full imaginary
  gluing information to investigate in a source-specific identity.
- [06](../06_paired_kernel_factorization/README.md) supplies the complete
  paired stationary kernels and their signed cross terms.
- [19](../19_euler_factor_controls/README.md) supplies arithmetic controls
  for checking the hypotheses of a proposed mechanism.

The polynomial heat control and the existing source controls test general
implications. A theorem restricted to genuine theta must identify the
additional property it needs. Passing a finite control screen does not
establish a global sign.

## Research records

Save derivations in `notes/`, tentative candidates in `brainstorm/`,
reproducible calculations and small records in `numerics/`, and assessments
in `reviews/`. Include the date, intended author, LLM assistance, recorded
model and effort. Numerical claims should be linked to their dedicated
notes and certificates.

Future investigation-specific chats belong in
[chat-histories](chat-histories/README.md). At the author's request, the
founding conversation now has its sole registration in this investigation;
its original identity, number 7, filename and first-capture provenance are
preserved in the [relocation record](CHAT_HISTORY_RELOCATION_20261014.json). Follow the repository's
[AGENTS.md](../../../../AGENTS.md),
[history guide](../../../../tools/CHAT_HISTORY.md), and
[large-file policy](../../../../LARGE_FILES.md).
Keep concise milestones in [DRAFT_HISTORY.md](DRAFT_HISTORY.md).
The manuscript was created at the author's explicit request. Keep it as
one stable source and record future milestones in the history; create no
manuscript snapshot folders.
