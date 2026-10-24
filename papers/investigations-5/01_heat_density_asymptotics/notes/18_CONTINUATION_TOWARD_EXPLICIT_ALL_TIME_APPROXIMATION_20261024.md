# Continuation toward an explicit approximation for all heat times

24 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), actual effort max**,
verified from this session's metadata.

**Start here in the next session.** This supersedes [Note 17][previous]
as the continuation entry point and carries forward the author's latest
clarification of the goal. The latest mathematical results are still in
[Note 16][transport]. Since that round, the [research overview][overview]
has been updated to make the all-time objective explicit. This handoff
adds no theorem, numerical result or completed research task.

The checkout is `/Users/ebbaker/Documents/shifted-zeta-positivity`; this
investigation is `papers/investigations-5/01_heat_density_asymptotics`.
Work there, rather than in the synced ChatGPT project sources.

## 1. The author's goal governs the next work

Find a **relatively simple explicit mathematical formula** for the
unnormalized averaged density, then improve both the formula and a proved
bound on its fluctuation/error against the true theta solution. Eventually
the construction must be defined for **every real heat time** and satisfy
the appropriate equations and correct boundary conditions. The error
theorem must cover the finite-time transition as well as both time limits.

The intended form is

\[
R_{\rm true}(t,\cdot)=R_{\rm app}(t,\cdot)+\mathcal E(t,\cdot),
\qquad \|\mathcal E(t,\cdot)\|_{X_t}\le B(t),\qquad t\in\mathbb R.
\]

Specify the spatial domains, norm, averaging and regulator. An informative
time-dependent bound is compatible with the goal: the physical density is
unnormalized and its positive-time mean grows. All-time validity does not
by itself establish uniformity over every height. Include any auxiliary
potential, current or covariance needed by the equations, and distinguish
model error from regulator bias against smoothed zero counts.

The endpoint formulas are starting approximations. A chosen mean profile
with a covariance defined afterward to force its equation is not yet a
validated approximation to the theta covariance. A truncated equation
needs a quantified residual and a stability estimate relating that
residual to actual solution error. Merely interpolating two endpoint
formulas does not establish the equations or the error bound.

## 2. Read in this order

1. Repository `AGENTS.md`, `LARGE_FILES.md`, `REFERENCE_WORKFLOW.md` and
   `tools/CHAT_HISTORY.md`. Read the [result index][results] and
   [avoid index][avoid], especially [heat geometry][geometry],
   [collision controls][controls], [target classification][classification],
   [evidence status][status-rule] and [scope][scope].
2. The [overview][overview] for the clarified objective and equation
   contracts, and the [progress register][progress] for the sole task ledger.
3. [Note 16][transport] and [Review 05][review] for the latest differentiated
   transport estimates and their limits.
4. [Note 12][positive] for complete-source concentration and the growing
   clock; [Note 14][variable] for variable-regulator corrections;
   [Note 11][negative] for negative time and the global heat-series fallback.
5. [Note 09][coarse] for finite-box source transfer, the Gaussian-envelope
   potential and kinematic covariance; [numerics][numerics] for the existing
   evaluators and records. The [manuscript guide][manuscript] describes the
   maintained 15-page fixed-epsilon draft. Notes 14 and 16 are later extensions.

This remains a quantitative approximation program under avoid/01, with
no RH or endpoint-simplicity conclusion as an acceptance target. Generic
heat/current identities also hold on collision controls. Retain the
source-specific premises and the controls' precise scope from Note 16,
Section 7; this handoff does not introduce a new exclusion argument.

## 3. Keep the target and equation conventions fixed

The unchanged canonical field is

\[
H(t,z)=\int_0^\infty e^{tu^2}\Phi(u)\cos(zu)\,du,
\qquad H_t=-H_{zz},\qquad
H(0,z)=\tfrac18\xi(\tfrac12+iz/2),\qquad z=x+iy.
\]

Here \(x\) is height. For \(q=\epsilon^2>0\), put

\[
D=|H|^2+q,\quad S=\log D,\quad r=\log q,\quad w=q/D,
\qquad
\rho=\frac{q|H_z|^2}{\pi D^2},\quad
j=\frac{qH_{zz}\overline{H_z}}{\pi D^2}.
\]

The current vector is \((\Re j,\Im j)\). The target is a positive
normalized average \(R=\mathcal F\rho\), without division by total mass.
The corresponding smoothed zero measure includes multiplicities.

For fixed filters, set \(U=\mathcal FS\),
\(Q=\mathcal F(S_x^2-S_y^2)-(U_x^2-U_y^2)\), and
\(\square=\partial_x^2-\partial_y^2\). Note 14 gives

\[
U_t=-\tfrac12(\square U+U_x^2-U_y^2+Q)+\mathcal F\mathcal B_\epsilon,
\qquad \Delta U=4\pi(R+\mathcal F C_\epsilon),
\]
\[
R_t+\operatorname{div}(\mathcal F\mathbf j)=\mathcal F\mathcal S_\epsilon,
\]

where

\[
\mathcal B_\epsilon
=w\{r_t+\tfrac12(r_{xx}-r_{yy}+r_x^2-r_y^2)\},\quad
C_\epsilon=\Delta S/(4\pi)-\rho,
\]
\[
\mathcal S_\epsilon=(1-2w)(r_t\rho+\nabla r\cdot\mathbf j).
\]

Use VE11 for the differentiated density equation, including both
derivatives of \(\mathcal F C_\epsilon\). Spatially varying epsilon
does not permit identifying positive density with potential curvature.
Moving filters additionally require VE13's commutators. These exact
identities do not themselves close the evolution.

The existing positive-time calculations use fixed compact spatial kernels
\(K(x,y)=k_\ell(x)k_h(y)\), where
\(k(s)=315(1-s^2)^4/256\) on \([-1,1]\), zero outside, and
\(k_a(s)=k(s/a)/a\). Typical diagnostics use \(\ell=10,h=0.75,Y=1\).
Preserve the full spatial buffers. A time average requires its full time
buffer and, for a causal problem, explicitly chosen history data.

## 4. Established starting formulas and their limits

**Negative time.** For \(t=-T\), \(\phi_0=\Phi(0)\), use

\[
G_T(z)=\frac{\phi_0\sqrt\pi}{2\sqrt T}e^{-z^2/(4T)},
\qquad R_-^{(0)}=\mathcal F\rho_\epsilon[G_T].
\]

Note 11, equations (4)--(5), gives the explicit elementary density and
its error constant: at fixed epsilon the error is \(O(T^{-3})\), uniformly
over all real heights and \(|y|\le A\sqrt T\), with filter buffers respected.
Note 14, VE19--VE21, instead chooses
\(\epsilon(-T)=\eta\phi_0\sqrt\pi/(2\sqrt T)\) and proves the explicit
scaled profile for \(T\rho\) with \(O(T^{-1})\) error. This can represent
regularization background in a zero-free region; the zero-measure target
needs its own regulator comparison.

**Positive time.** The explicit large saddle and curvature satisfy

\[
4\pi e^{4L}=2tL+9,\qquad \kappa=8tL-2t+36.
\]

Note 12 also expresses \(L\) through the Lambert W function. The simplest
existing coarse density is

\[
R_+^{(0)}(t,x,y)=\frac{L(t)}\pi k_h(y).
\]

On the buffered growing inner window \(X\asymp\kappa^{1/3}\), it has
the proved-in-note absolute error \(O(\kappa^{-1/2}+L^{-3})\) under
the stated gates and the explicit adaptive prescription

\[
M_0=2\pi^2e^{tL^2+9L-\pi e^{4L}}\sqrt{2\pi/\kappa},
\qquad \epsilon_+(t,x)=M_0\kappa^{-1}e^{-x^2/(2\kappa)}.
\]

This is an eventual positive-time prescription, not a regulator already
defined and validated for every real time. It also does not supply the
outer-height transition. The fixed-epsilon obstruction in Note 11 rules
out its specified all-height nonzero clock limit; it does not exclude
every adaptive regulator or all-time approximation.

For differentiated comparisons retain the finite moving clock. With
\(M=H(t,0)\), \(\mu=M^{-1}\int_0^\infty u e^{tu^2}\Phi(u)\,du\),
\(\alpha=\mu'/\mu\), and \(c_j=(j+1/2)\pi/\mu\), Note 16 uses

\[
R_c=k_h(y)\sum_jk_\ell(x-c_j),\qquad
J_c=-\alpha k_h(y)\sum_jc_jk_\ell(x-c_j).
\]

Only finitely many summands meet each compact filter. This reference
satisfies \(\partial_tR_c+\partial_xJ_c=0\), and its density time
derivative and current approximate the actual adaptive averages with
error \(O(L\kappa^{-7/6})=o(L/\kappa)\) on the growing inner window.
Its coefficients still use complete source moments; replacing them by
simple saddle formulas requires a paid coefficient-error estimate.

Note 16 additionally supplies \(O(\kappa^{-2})\) weak static regulator
bias, potential forcing \(O(L^2\kappa^{-2})\), and signed current-source
allowances \(O(\kappa^{-5/3}+L^2\kappa^{-2})\). The proof differentiates
the complete source and the exact weak-bias identity. Do not infer a
derivative estimate by differentiating an earlier asymptotic error bound.

Keep two specific restrictions: replacing \(\alpha\) by \(2/\kappa\)
is not justified at the claimed growing-window drift accuracy, and dropping
finite lattice phase is justified at that accuracy only on fixed height
ranges by AT27. The true differentiated covariance error remains open.

All these analytical claims are **proved in-note, with same-assistant
assessment only**. The [exact/allowance record][checks] and
[six-observation theta pilot][pilot] are distinct evidence. The latter is
floating quadrature, not interval certification, finite-epsilon peak
sampling or an evolved trajectory. Its continuum derivative discrepancy
reaches about 0.3143% of the mean derivative; several much smaller moving
clock discrepancies are at the refinement floor. Finite allowance gates
fail at some sampled times; no certified positive-time onset is known.

## 5. Recommended next bounded deliverable

**Produce one explicit candidate formula with a complete error ledger,
and identify how it can be connected through finite time.** Use the
existing endpoint formulas as the first members of an approximation
hierarchy. The author's clarification changes the emphasis of Note 17's
next-work recommendation: covariance and outer estimates should serve
the construction and validation of that formula.

1. Fix the comparison contract, including the proposed global regulator
   protocol and the required boundary/source data. The separate negative
   and positive prescriptions above have not yet been connected. Choose
   which parts of this first candidate will be proved on the existing
   domains and which are conjectural outside them.
2. Begin with the simple positive profile \(R_+^{(0)}\) and the controlled
   \(R_c\) reference. Seek a compact phase correction and explicit saddle
   coefficients. A short Fourier representation of the filtered lattice
   is one possible next calculation; it has not been derived or bounded
   in this round. Pay phase truncation, source-to-saddle coefficient error,
   root displacement and regulator bias separately, including the
   derivatives required by the equations.
3. Specify a finite-time bridge anchored to the canonical theta source.
   Source quadrature and Note 11's heat-series hierarchy can provide
   reference/error data, but a growing collection of xi derivatives is
   not yet the desired simple formula. Compare the candidate with actual
   theta data away from any fitting points and give analytic or certified
   error where possible. Do not hide an unevaluated copy of the full target
   inside the proposed simplification.
4. Audit the true covariance or use another justified source-based
   comparison to control the equation error. Retain negative-time
   derivative budgets, the positive outer-height transition, compatible
   potential boundary data, current flux and stability. A small residual
   alone is insufficient for the global closeness claim.

An all-time theorem must bridge overlapping domains, fix the harmonic
information and source normalization, and select the actual theta branch.
The two leading time limits alone do not select theta; the [opening note's
source perturbation control][opening] preserves them while changing intermediate
behavior. Do not assume the mixed-sign density equation is an ordinary
forward parabolic problem or prescribe incompatible endpoint data.

The next session should finish a concrete formula/error improvement or
state the precise failed estimate and its scope. Do not count another
formal reformulation as a quantitative gain. Independent review and
certified finite onset remain separate unfinished tasks. If using the
Polymath high-height literature, inspect the full theorem and hypotheses
first; its existing catalog entry was only metadata/abstract-checked.

HDA-02--06 remain partial and HDA-07--09 gated. HDA-10--12 are complete
only at their recorded bounded scopes. The clarified goal and this
continuation note do not change those statuses.

## 6. Files, provenance and the new session

Keep derivations in `notes/`, computations and small reproducible records
in `numerics/`, and assessments in `reviews/`. Preserve the maintained
manuscript until an expansion is requested; create no new snapshot folders.
Generated PDFs belong under the ignored root `output/pdf/` tree. Keep
milestone history concise and use Git commits/tags for future versions.
The working tree already contains substantial changes from earlier
research rounds; inspect and preserve them. No commit was made for this
handoff, and it requires no new manuscript build or numerical rerun.

The originating conversation is **0003 — Summarize heat-density research**,
thread **01a16fe8-5cab-7812-a4cc-e3a30ee34f56**, uniquely registered in
this investigation's [chat histories][histories]. Its archive contains the
author's clarification and approval history. Histories 0001 and 0002 are
separate conversations.

**A new session must use its own actual thread id, source transcript and
title. Do not reuse 0003's identity.** Discover any existing registration
first; otherwise register the new session in this investigation through
`tools/refresh_chat_history.py`. Preserve the tool-assigned number and
original provenance. Follow the history workflow at the beginning and end
of each reply. Until native hook activation is verified, arrange the
bounded exact-turn deferred capture as the final tool action, using that
session's actual turn id. Never prewrite an unsent final reply or hand-edit
a registered transcript. Synced `sources/` and generated `AGENTS.md`
remain read-only.

[previous]: 17_CONTINUATION_AFTER_ADAPTIVE_TRANSPORT_20261024.md
[overview]: ../research-overview/01_AVERAGED_DENSITY_RESEARCH_PROGRAM_20261024.md
[progress]: ../research-progress/01_AVERAGED_DENSITY_RESEARCH_PROGRESS_20261024.md
[transport]: 16_ADAPTIVE_FORCING_AND_DIFFERENTIATED_CLOCK_20261024.md
[review]: ../reviews/05_ADAPTIVE_TRANSPORT_SELF_REVIEW_20261024.md
[positive]: 12_GROWING_HEIGHT_STATIONARY_CLOCK_AND_VANDERMONDE_20261024.md
[variable]: 14_VARIABLE_EPSILON_EVOLUTION_AND_ASYMPTOTICS_20261024.md
[negative]: 11_TWO_TIME_LIMITS_ALL_HEIGHT_ERROR_20261024.md
[coarse]: 09_COMPLETE_SOURCE_MOMENT_TRANSFER_AND_WEAK_CURRENT_20261024.md
[opening]: 01_AVERAGED_DENSITY_AND_TWO_TIME_LIMITS_BRAINSTORM_20261024.md
[numerics]: ../numerics/README.md
[manuscript]: ../manuscript/README.md
[checks]: ../numerics/ADAPTIVE_TRANSPORT_CHECKS_20261024.json
[pilot]: ../numerics/ADAPTIVE_TRANSPORT_THETA_PILOT_20261024.json
[histories]: ../chat-histories/README.md
[results]: ../../../../result-summaries/README.md
[geometry]: ../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../avoid/README.md
[classification]: ../../../../avoid/01_restating_the_target.md
[status-rule]: ../../../../avoid/06_status_stronger_than_the_evidence.md
[scope]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
