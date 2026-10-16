# Constrained operator squares and heat flow

14 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Initialization model: gpt-6-astra (Codex), reasoning effort **ultra**.
Continuation: gpt-6.1-sol (Codex), reasoning effort **ultra**, 14 October 2026.

**Status: active at the author's request.** This investigation develops
operator-square identities that retain the constraints, oscillatory terms,
normal ordering, and approximation residuals needed by their applications.
The initial source review and exact seed identities are complete as internal
derivations. The bounded continuation now gives a certified correlated
Hubbard trial bound, corrected smoothing machinery, local operator-class
obstructions for both stationary constraints, and three certified stationary
control boxes. A source-specific theta positivity certificate and a scalable
quantum cost advantage remain open.

The starting material is Edward B. Baker III's three unfinished notes from
2017 and 2018. Their unfinished state is preserved in the
[source review](reviews/THREE_SOURCE_NOTES_REVIEW_20261014.md).
The project has two explicit applications:

- **Theta:** derive a constrained square certificate for the physical
  stationary Laguerre forms, using full theta information and testing
  against the positive-time controls of investigation 19.
- **Quantum energy:** retain evolution residuals and terminal endpoints
  when replacing exact imaginary-time trajectories by approximations,
  so the resulting energy remains a genuine Rayleigh quotient or a
  certified upper bound.

The common operator method does not establish a transfer theorem between
these applications. Each has its own sign, domain, normalization and
success criterion.

## Start here

The [self-contained draft manuscript](manuscript/constrained_operator_squares.tex)
collects the theta heat setup, derivative indices and Laguerre forms, the
conditional collision route to RH, the operator and residual results, and
the formula-level bottlenecks and possible constructions. Numerical results
are referenced through their dedicated notes. See the
[integration review](reviews/MANUSCRIPT_INTEGRATION_REVIEW_20261014.md) for
its proof scope and successful native compilation.

1. [Initial research program](notes/INITIAL_RESEARCH_PROGRAM_20261014.md):
   first tasks, decision gates and possible paper endpoints.
2. [Dirac squares and stationary Laguerre energy](notes/DIRAC_SQUARES_AND_STATIONARY_LAGUERRE_ENERGY_20261014.md):
   the research note requested for this project, relocated from 06.
3. [Residual-corrected heat-trajectory identities](notes/RESIDUAL_CORRECTED_HEAT_TRAJECTORY_IDENTITIES_20261014.md):
   a finite-time theorem directly addressing the February 2018 notes'
   lost variational guarantee.
4. [Review of all three source notes](reviews/THREE_SOURCE_NOTES_REVIEW_20261014.md):
   valid seeds, corrections and application boundaries.

An elementary exact-arithmetic [checker](numerics/check_seed_identities.py)
and its [record](numerics/SEED_IDENTITY_CHECKS_20261014.json) check the seed
formulas on finite examples. They are not a theta certificate or a
many-body performance result.

## Bounded continuation results

The [research decision and audits](reviews/BOUNDED_PROGRAM_AND_DIRAC_CONTINUATION_REVIEW_20261014.md)
record the bounded first pass and the remaining constructive gate.

- [Hubbard heat residual benchmark](notes/HUBBARD_HEAT_RESIDUAL_BENCHMARK_20261014.md):
  a certified upper energy below the fixed-spin product Slater minimum;
  direct evaluation remains cheaper in the declared representation.
- [Gaussian translation defects and normal ordering](notes/GAUSSIAN_TRANSLATION_DEFECTS_AND_NORMAL_ORDERING_20261014.md):
  the corrected smoothing theorem, its equality case and 21 exact CAR checks.
- [Local multipliers and finite observations](notes/LOCAL_MULTIPLIER_AND_FINITE_OBSERVATION_OBSTRUCTIONS_20261014.md):
  full-core local stationary square completions fail for both derivative
  levels; finitely many declared source observations admit wrong-sign controls.
- [Stationary theta and Euler controls](notes/2_CERTIFIED_STATIONARY_THETA_AND_EULER_CONTROLS_20261014.md):
  local positive theta margins for both targets and an actual stationary
  Euler curve with a strictly negative positive-time margin.

The [complex Laguerre and vertical-path note](notes/COMPLEX_LAGUERRE_AND_VERTICAL_PATH_CRITERIA_20261014.md)
records exact whole-plane equivalents, their boundary Laguerre expressions,
and the unsigned forcing left by the forward-heat reformulation.

The next theta construction must use a nonlocal or restricted arithmetic
state with the complete imaginary gluing and its full signed remainder.
The local positive boxes are validation records, not a global factorization.

## Potential research leads

**14 October 2026 — Quaternion branch promoted.** At Edward Baker's
request, [investigation 21](../21_quaternion_theta_geometry/README.md)
is now the home for quaternion theta continuation. Its
[criteria note](../21_quaternion_theta_geometry/notes/1_RH_CRITERIA_AND_QUATERNION_SETUP_20261014.md)
and [initial program](../21_quaternion_theta_geometry/notes/2_INITIAL_RESEARCH_PROGRAM_20261014.md)
develop the branch from its original formulas here. Promotion: prepared
for Edward Baker with LLM assistance by `gpt-6.1-sol` (Codex), effort
**ultra**.

The [brainstorm folder](brainstorm/README.md) keeps brief notes on vertical
spectral paths and the quaternion derivative-state proposal, including
the exact rewritings and the additional arithmetic signs they would need.

## Relationship to the portfolio

[06](../06_paired_kernel_factorization/README.md) remains the destination
for complete paired-kernel signs; this project develops the constrained
operator method. [02](../02_angular_jacobi_gluing/README.md) supplies the
full-gluing hypothesis to investigate.
[19](../19_euler_factor_controls/README.md) supplies collision controls.
The earlier [SUSY scout](../../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/03_susy_dirac_hodge/notes/1_MOVING_THETA_GROUND_STATE_WARD_RESIDUAL_AND_GAP_LIMIT_20261010.md)
already shows why a positive source Hamiltonian alone does not generate
the physical Newman evolution.

Save derivations in notes, computations and small records in numerics,
and assessments in reviews. Maintain concise [milestones](DRAFT_HISTORY.md);
create no manuscript snapshots. A future manuscript should name Edward
Baker as author, or state that it is drafted for him, and acknowledge LLM
assistance. Follow the repository's large-file and chat-history policies.
The originating chat keeps its existing formal-replay identity; see
[chat histories](chat-histories/README.md).
