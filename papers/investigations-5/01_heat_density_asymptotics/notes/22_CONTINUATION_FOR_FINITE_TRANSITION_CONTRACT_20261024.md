# Continuation: analytical estimates extending to infinite height

24 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), actual effort max**,
verified from the current session metadata.

**Latest new-session handoff:** [Note 24](24_CONTINUATION_FOR_GPT_ASTRA_INFINITE_HEIGHT_ANALYSIS_20261024.md) consolidates the current
Astra analytical starting point and manual Sol handoff rules. This note
retains the earlier handoff and its amendments for provenance.

## GPT model ownership and manual handoffs

Further author decision, 24 October 2026; gpt-6-astra, actual effort max:
Within GPT research, **GPT-6 Astra owns analytical formulas and proofs;
GPT-6.1 Sol owns all
numerical implementation and execution.** Edward Baker keeps the chats
going and carries requests between them. The
[shared workflow](../../../../GPT_RESEARCH_MODEL_WORKFLOW.md) gives the
bounded request, numerical return and analytical assessment template.
It introduces no automatic chat coordination or model switching.

Start with the current assignment in the [progress register][progress].
Astra develops the analytical argument and issues a packet only for a
specific computation it needs. Sol returns the result, error accounting,
reproduction record and any analytical questions; Astra records what this
permits the proof or formula to claim. Preserve each chat's actual model,
effort and unique history registration. Earlier Astra numerical work keeps
its historical attribution; the division applies moving forward.

## Current amendment — the author's infinite-height priority

24 October 2026; **gpt-6-astra, actual effort max**. The author asks that
analytical results extending to infinite height take priority, and that
numerics support analytical goals. This supersedes the bounded-bridge-first
schedule in the original handoff below. The existing [overview][overview]
and [sole progress register][progress] have been revised in place.
This is a priority decision, with no new analytical result or status upgrade.

Here height means real x in z=x+iy, with the transverse strip and full
filter buffer stated. Distinguish an all-real-x bound at each time from a
window growing as time tends to infinity; also distinguish fixed-time
height asymptotics from joint time/height limits.

1. **HDA-19 first:** derive positive outer-height field and observable
   estimates on an unbounded domain, with useful error and a controlled
   overlap with the existing inner clock. Start by stating the time/height
   regimes and tracking the regulator in the nonlinear comparison.
   Note 20's regulator loses a global positive floor after spatial
   dependence turns on; absolute field error alone does not pay that
   comparison through the existing floor-dependent estimate. This is an
   open estimate, not an impossibility claim for other methods.
2. **HDA-16:** extend the all-height negative Gaussian density estimates
   to current, time derivative and actual potential/covariance quantities;
   complete the positive evolution comparison with inner and outer bounds.
   Preserve the regulator corrections, full buffers and differentiated
   source estimates. Do not infer derivative error from a static bound.
3. **HDA-17 supports those analytical goals:** use finite-transition
   estimates or finite certification when a named global theorem needs
   them. HDA-18 assembles both time and height coverage, paying overlaps
   and joins. A bounded-height all-time theorem is a possible subresult,
   not a prerequisite for beginning outer-height work.

Useful existing inputs must not be overlooked: [Note 11](11_TWO_TIME_LIMITS_ALL_HEIGHT_ERROR_20261024.md)
already gives a negative all-height Gaussian estimate and a positive
all-height analytic hierarchy at fixed regulator; [Note 14][adaptive]
gives the adaptive negative profile. Notes 20 and
[23](23_FINITE_TRANSITION_CONTRACT_AND_LOCAL_BOUNDS_20261024.md) give
absolute jet allowances for every real x on compact time slabs and a
bounded transverse strip. For slabs ending at t<=64 the regulator has a
uniform floor, so global nonlinear bounds are also available, though
their constants can be poor. The Note 23 rectangle is a diagnostic domain,
not a limitation of those source lemmas. The positive inner clock still
has the growing-window scope in Note 19. None of this supplies the missing
adaptive outer-height theorem.

Before numerical work, name the analytic estimate it advances, the
question and possible decision, the finite regime and budget, and the
stopping rule. Appropriate uses are a bounded test of an estimate,
evaluation of explicit constants, verification of a derived identity,
or certification of a finite input with analytical control of the rest.
Do not infer infinite-height uniformity from larger samples. Stop when
the question is answered, a declared gate fails, or numerical uncertainty
is below the dominant analytical allowance. A new run requires a remaining
analytic need. The failed 192-cell trial is preserved; refining it is no
longer the default next task. See the [numerical policy](../numerics/README.md)
and [avoid 10](../../../../avoid/10_numerics_ahead_of_the_question.md).

Read the [result index][results], [heat-flow cluster][geometry],
[collision controls][controls] and [avoid index][avoid]. Keep the original
physical normalization and distinguish regularized density error from
regulator-to-zero-measure error. The original proofs and self-review
scopes remain unchanged. Under [avoid 20](../../../../avoid/20_volume_without_a_gain.md),
this amendment updates the existing handoff; no additional manuscript or
research note is created solely for a schedule change.

## Original handoff — historical execution order, superseded above

All sections below preserve the earlier handoff and its then-current task
states. Follow the current amendment above and the sole progress register
for execution; HDA-15 has since been completed at the Note 23 scope.

**Original status: continuation and task handoff; no new analytical result.**
Begin with **HDA-15**, the transition contract and sharper source/nonlinear
comparison bounds. The [existing overview][overview] and [sole progress
register][progress] were revised in place because the objective is unchanged.
The primary route is now direct comparison with the canonical theta source;
an autonomous density closure is an alternative with its own stability
requirements. The first all-time milestone is on a fixed height window,
followed by the extension toward the author's all-height objective.

This was the handoff after Notes 19--21 and the earlier program revision.
[Note 18][goal] retains the author's explicit all-time approximation goal;
its earlier next-step recommendations should be read through the revised
overview and HDA-15--20. Existing results and historical task statuses have
not been upgraded by these planning changes.

### Read first

Work in `/Users/ebbaker/Documents/shifted-zeta-positivity`, under
`papers/investigations-5/01_heat_density_asymptotics`.

1. Read the repository [instructions][instructions], [large-file policy][large]
   and [chat-history workflow][history-workflow]. Then read the
   [result index][results], specifically the [heat-flow cluster][geometry]
   and [collision controls][controls], and the [avoid index][avoid].
2. Read the revised [overview][overview], especially Sections 3--6, and
   the current state, alignment decision and task table in [progress][progress].
3. Read [Note 20][bridge], especially FB8--FB13, as the immediate
   mathematical starting point. Read [Note 19][clock] for the explicit
   positive endpoint and its exact phase and finite gates.
4. Read the [manuscript guide][manuscript], [integration note][integration]
   and [latest self-review][review7]. Consult [Notes 14][adaptive]
   and [16][transport] for the exact adaptive equations and differentiated
   source estimates when needed.

Under [avoid 01][classification], this is a quantitative approximation
program. Progress means a new useful bound, a paid approximation or a
precisely scoped failure. It is not an RH or simplicity criterion.

### Author decisions and the comparison target

The author wants a simple explicit approximation valid across real heat
time, respecting the equations and compatible boundary data, with errors
improved progressively. Preserve the absolute scale of

\[
\rho_{\epsilon_g}(t,z)=
\frac{\epsilon_g(t,x)^2|H_z(t,z)|^2}
{\pi\bigl(|H(t,z)|^2+\epsilon_g(t,x)^2\bigr)^2},
\qquad H_t=-H_{zz},\qquad z=x+iy.
\]

The immediate target is its spatial average \(R=K*\rho_{\epsilon_g}\),
with fixed positive widths and the full convolution buffer. Start with
spatial averaging only; time averaging and moving widths remain allowed
extensions after their extra data and commutators are paid. Do not replace
the physical density by a probability-normalized profile. The exact
adaptive equations are P3a--P5a in the overview; keep both derivatives of
the curvature correction and the adaptive current source.

The author has already authorized incorporating results into the maintained
manuscript and rewriting its background or other sections as useful.
Lead with analytical results, mention numerics briefly as backup, and
refer to notes for numerical detail. No renewed approval is needed for
routine research or manuscript integration within this scope.

### Results available at this handoff

The analytical results below are **proved in the cited notes/manuscript
at their stated scopes, with same-assistant review only**. Numerical checks
are separate supporting evidence. There is no certified finite onset or
completed all-time approximation.

| Input | What is available | Limit relevant to continuation |
| --- | --- | --- |
| [Notes 11][negative] and [14][adaptive] | Negative-time Gaussian density estimates, including the adaptive \(T\rho\) profile with \(O(T^{-1})\) scaled error on the stated scaled strip and all real scaled heights | HDA-16 must supply the negative current/time and adaptive covariance/boundary budgets required by the chosen full-system contract. |
| [Notes 16][transport] and [19][clock] | Explicit positive saddle clock with five periodic-polynomial density terms, six current terms and exact phase; density error \(O(\kappa^{-1/2})\), current/time error \(O(L\kappa^{-7/6})\) | These are eventual estimates on the buffered \(X\asymp\kappa^{1/3}\) window under the explicit source/collar gates. Actual clock potential, covariance and its Laplacian still need comparison bounds. |
| [Note 20][bridge] | One smooth global regulator and a finite source field with exact heat evolution; finite-slab bounds for jets, density, current, time derivative, potential, actual covariance and its Laplacian | No selected mesh with informative uniform error across the full transition, no certified endpoint overlap, and no all-time joining theorem. |
| [Note 21][integration] and the [manuscript][main] | One maintained analytical manuscript incorporating the above, with a sharper mean-input term in the existing determinant allowance | Its 25-page build and link/visual checks are production checks. The determinant improvement does not improve the dominant root-location order or complete the research gates. |

In Note 19, the complete-source score proves
\(|\mu-L|=O(\kappa^{-1})\) and
\(|\alpha-2/\kappa|=O(\kappa^{-3/2})\). These bounds pay the saddle
substitution that was not justified at the earlier accuracy. Retain finite
phase in differentiated estimates; the smooth mean profile alone does not
inherit the clock's current/time error. Use the finite allowances and gates
SC15--SC18 when seeking an actual onset, not only their asymptotic orders.

### Immediate task HDA-15

**Deliver a declared finite-transition contract and a justified improvement
to its error allowances, or identify precisely why the proposed improvement
does not help.** Do this before a large numerical campaign.

1. **Specify the contract.** Choose a fixed observation rectangle
   \(|x|\le X_0, |y|\le Y_0\), its full kernel buffer, fixed kernel widths,
   a trial compact time slab \([a,b]\), and the parameter \(\eta\) in
   Note 20's common regulator FB2. Declare norms and componentwise
   tolerances or nonvanishing reference scales for \(R,J,R_t,U,Q,\Delta Q\)
   and the constraints, derivatives and boundary traces required by the
   stated theorem. Use absolute errors where quantities can vanish.
   Concrete numerical choices are still open; choose and justify them
   before judging observed discrepancies.
2. **Improve the source allowance where it loses the most.** The starting
   field is
   \[
   H_f(t,z)=\int_0^{U_s}e^{tu^2}f(u)\cos(zu)\,du,
   \]
   where \(f\) is the nonnegative piecewise-linear interpolant of finitely
   many truncated theta-source values. Note 20 evaluates this as a finite
   error-function expression. Here \(U_s\) denotes that note's source
   cutoff \(U\), to distinguish it from the averaged potential.
   Its original jet budget is
   \[
   \delta_j=(B_2h_s^2/8+\tau_N)F_j(s,Y,U_s)+T_j,
   \qquad j=0,1,2,3,\quad s=\max(b,0),
   \]
   with \(F_j=\int_0^{U_s}u^je^{su^2+Yu}\,du\), full transverse buffer
   \(Y\), complete-source derivative bound \(B_2\), source mesh width
   \(h_s\), theta-mode error \(\tau_N\) and tail allowance \(T_j\).
   Seek source-weighted or cellwise interpolation estimates in place of
   the single global bound. Retain every theta-mode, tail and nodal
   arithmetic term; refining the mesh cannot remove those other errors.
3. **Improve nonlinear transfer without changing the target.** Compare
   the original FB10--FB13 allowances with amplitude-aware bounds for
   the same field, regulator, domain and observables. Preserve the physical
   scale; if an internal normalization depends on time or position, pay its
   derivatives in any transformed equation. The comparison must remain
   meaningful at zeros and multiple events. Control the actual covariance
   computed from the approximate field, rather than define a missing
   covariance from the desired equation.
4. **Use a small diagnostic only to locate the cost.** Report the separate
   source, nonlinear, arithmetic and filter contributions, together with
   representation size. Check the error-function evaluation near removable
   singularities and in its required argument range. Note 20's small
   primitive check is not a production evaluator. Floating observations
   may guide refinement; any numerical input to a theorem needs a uniform
   enclosure over the entire slab and buffer, including gaps between samples.
5. **Record the actual outcome.** Give the new proof and its quantitative
   gain over FB8--FB13, or a scoped failed estimate with the dominant term
   and regime. Save derivations in the next unused research-note number,
   diagnostics in `numerics/`, assessment in `reviews/`, and update the
   existing progress register. Integrate genuine new analytical results
   into the maintained manuscript with brief numerical support.

HDA-15 does not by itself complete the finite bridge. HDA-17 requires an
explicit choice of slab, cutoff, mode count and source mesh whose complete
errors meet the declared tolerances uniformly, with its cost stated.

### Subsequent tasks and completion gates

| Task | Status at handoff | Next obligation |
| --- | --- | --- |
| HDA-15 | Ready, not started | The contract and sharper allowances above. |
| HDA-16 | Ready, not started | Negative Gaussian current/time bounds; positive clock potential and actual covariance/Laplacian bounds; required adaptive negative covariance and endpoint boundary traces. Derive derivative errors directly. |
| HDA-17 | Gated by contract and useful bounds | One informative finite transition representation with complete uniform error and explicit cost. |
| HDA-18 | Gated by endpoint and transition budgets | Thresholds valid over whole time tails, two nonempty overlap intervals, full time coverage and paid joining/constraint errors on the fixed height window. |
| HDA-19 | Ready, later priority, not started | Positive outer-height extension with quantitative spatial matching. The order is a priority choice, not an impossibility claim. |
| HDA-20 | Ready for existing proofs, not started | A distinct-reviewer audit with provenance and shared inputs recorded; distinguish another same-model review from specialist review. |

HDA-16 and review of existing proofs can advance before HDA-17 finishes.
The [progress register][progress] remains the authority for all task
statuses, including earlier HDA-00--14.

Endpoint thresholds must control whole tails. The regulator's switch
points 64 and 128 are definitions, not certified clock-onset times.
Overlap needs each approximation's own error against the same theta field.
A triangle inequality bounds value mismatch; it does not pay the derivative
terms from a time-dependent join. Blending two exact heat fields creates
\(\chi'(t)(H_2-H_1)\). Direct source comparison can prove closeness without
first solving an autonomous density PDE; a residual-only route still
needs a stability argument.

The failure of a **fixed compact-source** field at positive infinite time
is scoped to that class. It does not rule out growing source cutoffs or
endpoint matching. Regulator-to-zero-measure bias is also a separate
obligation: it is needed for a zero-count interpretation, but is not a
prerequisite for a theorem expressly about the regularized density.

Keep the [collision-control screen][controls] from Notes 19--20. Atomic
and polynomial controls lack the smooth canonical-source premises.
Euler-factor controls change the source and score; weighted-square and
finite-prime controls change the canonical weights/full reflection;
reflected and positive-primitive controls lack the canonical square
expansion. They cannot inherit unchanged theta majorants. Generic smooth
field-stability estimates remain compatible with colliding controls, and
a simple-root collar fails at a covered collision. None of these
approximation results excludes an earlier theta collision. Apply the
[status][status-rule] and [scoped-exclusion][scope] rules to every extension.

### Files and new-chat provenance

The maintained source is [manuscript/main.tex][main]. Its current local
reading copy is [the shared-output PDF][pdf]; build instructions and the
small build record are in the [manuscript guide][manuscript]. Keep derived
PDFs in the ignored root `output/pdf/` tree and create no new manuscript
snapshot folders. Use the existing [milestone history][draft-history] for
substantive manuscript milestones. This handoff requires no new build or
numerical rerun and does not create a new research program or progress file.
The working tree contains substantial earlier uncommitted work; inspect
and preserve it. No commit was made for this handoff.

This conversation is **0004 — Continue heat density asymptotics**, thread
`01a17005-c3ef-7a22-80de-17bf918be4e9`, with its unique [registered
history][this-history]. The author asked for this continuation note so
that research can continue in a new chat.

**The new chat must use its own actual thread id, transcript and title.**
Discover any existing registration before registering it in this
investigation's [chat-histories][histories]; do not reuse 0004's identity
or manually assign its successor number. Use `tools/refresh_chat_history.py`
at the beginning and end of each reply. Until trusted completion-hook
activation is verified, arrange the bounded exact-turn deferred capture
as the final tool action, using the new chat's actual turn id, and then
send the real final response. Never prewrite unsent text or hand-edit a
registered transcript. Synced `sources/` and generated `AGENTS.md` remain
read-only.

[overview]: ../research-overview/01_AVERAGED_DENSITY_RESEARCH_PROGRAM_20261024.md
[progress]: ../research-progress/01_AVERAGED_DENSITY_RESEARCH_PROGRESS_20261024.md
[goal]: 18_CONTINUATION_TOWARD_EXPLICIT_ALL_TIME_APPROXIMATION_20261024.md
[clock]: 19_EXPLICIT_SADDLE_CLOCK_AND_EXACT_PHASE_20261024.md
[bridge]: 20_GLOBAL_REGULATOR_AND_FINITE_SOURCE_BRIDGE_20261024.md
[integration]: 21_ANALYTICAL_MANUSCRIPT_INTEGRATION_20261024.md
[negative]: 11_TWO_TIME_LIMITS_ALL_HEIGHT_ERROR_20261024.md
[adaptive]: 14_VARIABLE_EPSILON_EVOLUTION_AND_ASYMPTOTICS_20261024.md
[transport]: 16_ADAPTIVE_FORCING_AND_DIFFERENTIATED_CLOCK_20261024.md
[manuscript]: ../manuscript/README.md
[main]: ../manuscript/main.tex
[review7]: ../reviews/07_ANALYTICAL_MANUSCRIPT_INTEGRATION_SELF_REVIEW_20261024.md
[pdf]: ../../../../output/pdf/heat_density_asymptotics/heat_density_asymptotics.pdf
[draft-history]: ../DRAFT_HISTORY.md
[histories]: ../chat-histories/README.md
[this-history]: ../chat-histories/0004_2026-10-24T22-26-28Z_continue-heat-density-asymptotics.json
[instructions]: ../../../../AGENTS.md
[large]: ../../../../LARGE_FILES.md
[history-workflow]: ../../../../tools/CHAT_HISTORY.md
[results]: ../../../../result-summaries/README.md
[geometry]: ../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../avoid/README.md
[classification]: ../../../../avoid/01_restating_the_target.md
[status-rule]: ../../../../avoid/06_status_stronger_than_the_evidence.md
[scope]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
