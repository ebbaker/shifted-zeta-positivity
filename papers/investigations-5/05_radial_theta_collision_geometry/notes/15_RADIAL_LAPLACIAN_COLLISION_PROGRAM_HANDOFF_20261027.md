# Continuation of the radial Laplacian collision program

27 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort max**. Investigation05 chat0004, **Explore 3D Laplacian collision rules**.

**Start here for the new program.** Edward Baker requested a new research overview and progress file, gave them priority over the previous program, required analytic results with numerics only in support, and asked that the documents be created as new files. Relevant material from the previous program may be reused. The earlier files remain intact, so their historical next-session instructions do not override this handoff.

Read the new [overview][overview] for the full program and the new [progress register][progress] for actual task states. [CURRENT_RESEARCH_PROGRAM.md][current] is the new root entry point. The first task is a bounded analytic comparison joining RLC-01 to RLC-02. A broad numerical search, a new higher-dimensional lattice, and another rewrite of the existing Wronskian are not the default continuation.

## The research objective

Use the standard three-dimensional radial Laplacian, its canonical theta flux, and complete boundary equations to obtain analytic restrictions on simultaneous H=H_a=0. Preserve the original integer-square theta source and the full physical observation. A useful first return may be a quantitative source-balance restriction or a precise failure of an estimate, rather than a global collision theorem.

The program has seven parts. RLC-01 supplies analytic flux and transfer bounds. RLC-02 uses them to constrain the joint cancellation. RLC-03 supplies local energy estimates only when their full interface costs help a specified consumer. RLC-04 seeks a different source-dependent restriction under the event boundary conditions. RLC-05 waits for a concrete homogeneous characteristic candidate. RLC-06 transfers actual results to the correct multiplicities and parameter ranges. RLC-07 supplies controls, verification, references and provenance throughout. RLC-04 does not require the shell route to succeed first.

## Reading order

1. Read repository AGENTS.md, [the chat workflow][history-workflow], [result summaries][results] and [patterns to avoid][avoid]. Use the [collision controls][controls], [target-classification rule][a01], [coupled-estimate guidance][a12] and [scoped-conclusion guidance][a07] when framing the next claim.
2. Read the new overview and progress register. They take priority over the older RTC scheduling instructions. Do not import old task completions into the new RLC count.
3. Read [Note14][n14], the immediate flux and energy foundation. Consult [Note13][n13] for the fixed radial representation and [Note01][n01], Sections 2–7, for normalization, the evolved potential, forced equation and explicit control.
4. Read [Note05][n05] before proposing a source-dependent weight, scalar Wronskian conjugation or finite theta closure. Read [Note04][n04] before using a deformation or global index argument.
5. The earlier [chat0002 discussion][chat2] explains how the radial system differs from the subsequent lattice constructions. The [reference guide][references] points to the already checked primary passages. Notes06–12 are optional comparison material unless a concrete new task needs them.

## Exact working formulas

Keep r=e^(2u), x=log r=2u, a real, lambda=a^2/4 and

\[
\Theta(r)=1+2\sum_{n\ge1}e^{-\pi n^2r^2},\quad
Q=\Delta_3\Theta,\quad
Q_t=e^{t\log^2r/4}Q,\quad H_t=-H_{aa}.
\]

The potential and flux are fixed by

\[
M_t=16H(t,i),\quad
\mathcal T_t(r)=M_t+\int_r^\infty(s^2/r-s)Q_t(s)\,ds,
\quad S_t(r)=-r^2\mathcal T_t'(r).
\]

Thus S_t'= -r^2Q_t, S_t(0+)=M_t, S_t(infinity)=0 and 2S_t(1)=T_t(1). The whole-space equation retains -4 pi M_t delta_0. Newman time multiplies Q; it does not turn this Poisson problem into radial diffusion.

The practical simplification is

\[
S_0(r)=4\pi r^3\sum_{n\ge1}n^2e^{-\pi n^2r^2},\quad
S_t(r)=w_t(r)S_0(r)+\frac t2\int_r^\infty
\frac{\log s}{s}w_t(s)S_0(s)\,ds,
\quad w_t=e^{t\log^2r/4}.
\tag{1}
\]

Both terms are nonnegative on r>=1, t>=0; the first is strictly positive and the correction is zero at t=0. With k_a=r^(-1/2)cos((a/2)log r),

\[
8(H,H_a)=\int_1^\infty r^2Q_t(k_a,\partial_a k_a)\,dr,
\]

\[
8H=S_t(1)+\int_1^\infty S_tk_a'\,dr,\qquad
8H_a=\int_1^\infty S_t\partial_a k_a'\,dr.
\tag{2}
\]

For any flux approximation, subtract (2) before majorizing. The first component includes the difference at r=1, and both integrals share the same residual. The full exterior formula already incorporates inversion; do not double it by adding another interior observation.

## First bounded analytic task

**Task.** Develop one complete canonical flux-to-two-observation estimate and compare it with the direct u formulation on the same domain. Start from (1)-(2); their elementary rederivation does not constitute the new return.

1. **Declare the statement.** Choose symbolic compact ranges such as 0<=t<=T_+ and 0<a_-<=a<=a_+. State whether the intended output is a uniform observation bound, a source-balance restriction at a candidate collision, a strict exclusion on a domain, or a comparison obstruction. Do not select a numerical rectangle by sampling first.
2. **Acquire the needed canonical bounds analytically.** Derive bounds for S_t, shell differences S_t(R)-S_t(U) and the outer weighted tails needed by both kernels in (2). Keep the complete positive time correction, the full theta sum and all differentiation justifications. A finite prefix is usable only together with its actual remainder.
3. **Choose one coupled estimate.** For example, use exact shell charges q_j=S_t(R_j)-S_t(R_(j+1)) with the joint kernel (k_a,partial_a k_a). Derive a signed projection or other analytic bound using actual theta information. The generic convex-hull enclosure by itself is already in Note14. Preserve correlations from shared endpoint fluxes; pay derivatives of moving cuts if used.
4. **Compare before optimizing.** Express the same proof in the original u variable, or otherwise identify the best matched direct comparator with identical source information and tail allowances. Determine where the radial formulation changes an actual constant, cancellation estimate, source requirement or evaluation cost. If it does not, state the exact equality or dominance and stop that variant.
5. **Screen the mechanism.** Check the explicit Gaussian-polynomial event from Note01 and the relevant families in the collision-control register. If the method uses only positive radial charge and Kelvin symmetry, it must remain compatible with those colliding sources. Name the exact canonical premise used by any separating estimate, and prove its effect rather than just noting that a control is not theta.
6. **Return and assess.** Save one focused proof note and a concise assessment. State the gain or scoped failure, domain, supporting inputs and remaining condition. Only then decide whether an exact-algebra check or a finite interval enclosure would resolve a stated remaining uncertainty.

A satisfactory result can be analytic without numerical evaluation. If a specific constant remains, show its formula and its role before computing. More sampling or precision cannot compensate for an incomplete signed inequality. Do not silently replace an unsuccessful estimate with a broader claim that all radial approaches fail.

## Alternative routes and known stopping points

For RLC-03, the logarithmic mode has inverse-square coefficient (1+a^2)/4. The radial energy reduces to integral (|v'|^2-a^2|v|^2/4) dx, so positivity on arbitrary annuli is unavailable. A Dirichlet interval of width L gives pi^2/L^2-a^2/4, but the actual response needs cutoffs or traces. Include their complete costs before claiming a benefit.

For RLC-04, keep the selected responses

\[
Y_{xx}+\lambda Y=g_t,\quad
Z_{xx}+\lambda Z=-Y,\quad
g_t=4e^{tx^2/4}\Phi(x/2),\quad Z=Y_\lambda.
\]

At a multiple event, Y_x(0)=Z_x(0)=0 and integral Y^2 + integral g_t Z=0. This is an exact cancellation identity, not an independent sign. The next candidate must supply an additional theta-specific relation or complete signed estimate. Note05 already excludes the tested scalar modular multiplier as an unconditional pointwise-sign mechanism on its stated regime; this does not exclude every event-conditioned current.

For RLC-05, H is currently a source coefficient, not a characteristic determinant. Begin only with a definite operator/domain/boundary proposal and an exact physical map. For RLC-06, distinguish all-multiplicity exclusion of H=H_a=0 from an argument restricted to nondegenerate double events. Keep bounded regions, positive-threshold applications and t=0 simplicity separate. No current program result covers the missing global ranges.

## Records and chat history

Save derivations in notes/, assessments in reviews/, and supporting computations and small records in numerics/. Include Edward Baker, LLM assistance, date, actual recorded model and effort. Follow the [large-file policy][large-files] and [reference workflow][reference-workflow]. This planning reset creates no manuscript snapshot and is not a manuscript milestone.

This conversation has one canonical registration: **chat0004**, thread `01a17fce-4841-7672-b275-325823e098f4`, [archive][chat4], [registry][history-index]. The original creation time and filename are retained. The preceding answer was captured by its bounded exact-turn follow-up; the setup verification record records the later integrity check. A new continuation chat must register its own actual identity in this investigation, not reuse chat0004's id or number.

For continuation in this same chat, run the standing refresh at the beginning of the reply. Before finishing, refresh completed public text and arrange the bounded capture with the **actual current turn id**, as documented in tools/CHAT_HISTORY.md. The deferred call is the final tool action, followed promptly by the real final response. Never insert a planned response into an archive or reuse the prior turn id. Native completion-hook activation has not been verified in this session; keep the documented bounded follow-up workflow until it is.

The [setup verification record][verification] distinguishes verified archived text from the not-yet-sent final response of its own turn. Later capture times, counts and hashes belong to the registry. Preserve the existing registrations of the founding Investigation04 chat and Investigation05 chats0001–0003.

[overview]: ../research-overview/02_RADIAL_LAPLACIAN_COLLISION_RESEARCH_OVERVIEW_20261027.md
[progress]: ../research-progress/02_RADIAL_LAPLACIAN_COLLISION_RESEARCH_PROGRESS_20261027.md
[current]: ../CURRENT_RESEARCH_PROGRAM.md
[n01]: 01_RADIAL_THETA_GEOMETRY_AND_COLLISION_MECHANISMS_20261027.md
[n03]: 03_CIRCLE_HEAT_LIFT_AND_BOUNDARY_TRANSFER_OBSTRUCTION_20261027.md
[n04]: 04_GAUSSIAN_SOURCE_DEFORMATION_AND_COLLISION_INDEX_TRANSPORT_20261027.md
[n05]: 05_MODULAR_WRONSKIAN_WEIGHT_AND_CANONICAL_SIGN_OBSTRUCTION_20261027.md
[n13]: 13_RADIAL_LAPLACIAN_CONTINUATION_20261027.md
[n14]: 14_RADIAL_FLUX_AND_COLLISION_RESTRICTIONS_BRAINSTORM_20261027.md
[chat2]: ../chat-histories/0002_2026-10-27T19-50-22Z_review-radial-theta-collision-work.json
[chat4]: ../chat-histories/0004_2026-10-27T23-59-47Z_explore-3d-laplacian-collision-rules.json
[history-index]: ../chat-histories/index.json
[references]: ../references/README.md
[verification]: ../reviews/08_RADIAL_PROGRAM_SETUP_AND_HISTORY_VERIFICATION_20261027.md
[results]: ../../../../result-summaries/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../avoid/README.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[history-workflow]: ../../../../tools/CHAT_HISTORY.md
[large-files]: ../../../../LARGE_FILES.md
[reference-workflow]: ../../../../REFERENCE_WORKFLOW.md
