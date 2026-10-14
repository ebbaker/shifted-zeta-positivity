# Initial program for quaternion theta geometry

14 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded model: **gpt-6.1-sol (Codex)**; reasoning effort: **ultra**.

The first task is to determine whether the constrained quaternion state
exposes a theta-specific signed identity beyond the exact rewriting.
Use the adopted [standard Fueter lift with independent time](3_STANDARD_FUETER_LIFT_WITH_INDEPENDENT_TIME_20261014.md),
\(F(t,q)=H(t+\overline{z_1},z_0)+\mathbf jH_z(t+\overline{z_1},z_0)\),
with \(q=z_0+\mathbf jz_1\). Its complex trace at \(z_1=0\) is
\(f(t,z)=H(t,z)+\mathbf jH_z(t,z)\). The
[criteria note](1_RH_CRITERIA_AND_QUATERNION_SETUP_20261014.md) fixes
the observation formulas and analytic assumptions. This program starts with the
real stationary observations; the whole-plane curvature route remains
a separately declared alternative.

## Bounded results and the remaining target

The [complete theta estimate](5_COMPLETE_THETA_CENTRAL_ESTIMATE_20261014.md)
now gives \(|F(t,x)|>1/120000\) for \(0\le t\le1,|x|\le8\),
and treats both stationary sets on \(|x|\le5\). The
[imaginary-gluing defect estimate](6_IMAGINARY_GLUING_STABILITY_AND_HEIGHT_OBSTRUCTION_20261014.md)
controls all four physical jets absolutely and yields a robust local
norm gap. Small nonzero defects can still permit remote collisions.
Full-source boundary substitution retains every n,m cross term;
separate index diagonals have wrong-sign algebraic tails.

## Primary construction target

Seek an exact current or boundary identity that controls both
\(\mathscr L_0\) on \(H_x=0\) and \(\mathscr L_1\) on \(H_{xx}=0\),
or yields
\(\mathscr L_j\ge-K_j|f|^2\) there with nonnegative \(K_j\) locally
bounded through every candidate joint zero. Fix the unnormalized source,
quaternion conventions, operator class, and an open real positive-time
domain before making a sign claim.

Use the complete theta preparation to identify the extra arithmetic
relation entering the identity. A proposed square must specify its
operator domain, adjoint, stationary constraint, and the observation it
actually controls. Retain all signed remainders, endpoints, and tails.
If no suitable identity exists for the chosen operator class, state and
prove that scoped obstruction.

## First deliverable

The [Cauchy Fueter note](4_CAUCHY_FUETER_BOUNDARY_AND_CURRENT_REFORMULATIONS_20261014.md)
now supplies a signed boundary quadratic form and a conserved current.
Its unified physical target is \(\partial_t|F(t,x)|^2\ge0\), or a
locally bounded negative loss, on \(H_xH_{xx}=0\). Continue with a
theta-specific estimate for one declared boundary or current domain.

Save one short derivation in `notes/`, with the following content:

1. The declared observation, domain, normalization, and operator class.
2. An exact candidate current or boundary identity, including its complete
   signed remainder, or a precise obstruction to that class.
3. The source-specific hypothesis used and the remaining estimate.
4. Its behavior on the polynomial control and applicable source controls.
5. How a successful estimate would cover both predecessor branches and
   imply the exact positive-time endpoint.

A formula that merely recovers an existing quaternion product should be
identified as a consistency check. The first research milestone requires
a new usable identity, estimate, or scoped obstruction.

## Validation conditions

| Condition | Evidence required |
| --- | --- |
| Jet compatibility | Preserve \(U_{z_0}=V\), standard left Fueter regularity, and external \(\partial_tF=-\partial_{z_0}^2F\). Distinguish the full lift from its trace f. |
| Signed observation | Identify the component or Hermitian curvature being controlled. A positive norm or integrated square alone is insufficient. |
| Collision coverage | Treat both derivative levels on predecessor neighborhoods. A bounded domain supplies only the exclusion it actually covers. |
| Regular loss | Prove \(K_0,K_1\) remain locally bounded through candidate \(f=0\); exclude uncontrolled division by the first jet. |
| Complete source | Retain full theta gluing and every oscillatory term, boundary contribution, and remainder. |
| Control separation | Explain the hypothesis that the polynomial or Euler controls lack, or show where a proposed general certificate fails on them. |
| Operator scope | Show how the construction falls outside, or satisfies the hypotheses of, the existing local multiplier and finite-observation obstructions. |

Passing a control screen is a necessary consistency check for a proposed
general implication, not proof of the theta sign. Numerical evidence
belongs in a dedicated note with its code, arithmetic, tails, domain,
and small certificate record.

## Spectral alternative

If a concrete identity points toward imaginary spectral displacement,
declare \(\mathcal C_0(0,z)\ge0\) throughout the spectral plane as the
target. Control \(|H|^2\), not the total norm \(|f|^2\).
The exact forward-heat reformulation leaves a forcing term without a
general sign; a maximum-principle argument must pay that term and its
boundary and growth assumptions. Forward preservation from t=0 does
not recover t=0 from a later real-rooted slice.

Read the [vertical-path formulas](../../20_constrained_operator_squares/notes/COMPLEX_LAGUERRE_AND_VERTICAL_PATH_CRITERIA_20261014.md)
before taking this alternative. Do not interchange a spectral curvature
claim with a real stationary sign without a proved implication and
matching domains.

## Required background

- [Original quaternion formulas](../../20_constrained_operator_squares/brainstorm/02_QUATERNION_JET_AND_HEAT_OPERATOR_20261014.md).
- [Collision and bounded-loss theorems](../../20_constrained_operator_squares/manuscript/constrained_operator_squares.tex).
- [Local multiplier and finite-observation obstructions](../../20_constrained_operator_squares/notes/LOCAL_MULTIPLIER_AND_FINITE_OBSERVATION_OBSTRUCTIONS_20261014.md).
- [Stationary theta and Euler controls](../../20_constrained_operator_squares/notes/2_CERTIFIED_STATIONARY_THETA_AND_EULER_CONTROLS_20261014.md).
- [Full-gluing construction gate](../../02_angular_jacobi_gluing/reviews/CONTINUATION_AND_BRAINSTORM_BRIEF_20261013.md).
- [Shared Euler-factor control program](../../19_euler_factor_controls/notes/INITIAL_RESEARCH_PROGRAM_20261013.md).

The quantum-energy application remains in investigation 20. No manuscript
is created by this setup. Save research assessments in `reviews/` and
record notable completed milestones in the concise root history.
