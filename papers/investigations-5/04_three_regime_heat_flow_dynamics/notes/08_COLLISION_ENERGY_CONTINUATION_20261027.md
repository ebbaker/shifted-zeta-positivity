# Continuation for the collision energy research program

27 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort max**.
Origin: **Review three-regime heat-flow status**, chat0003, thread
`01a17da8-4a84-7df3-b309-ec18e0535f1e`.

## Assignment for the next session

Continue the approved analytical program in
[the collision energy overview][overview] and [the CE progress register][progress].
Keep \(t_c,b,a\) general and retain arbitrary finite multiplicity \(m\).
Develop the exact source formula, a useful shifted-source hierarchy, its
transfer to energy, and the first actual canonical coefficient estimate.
Pursue multiple compatible goals in one session before proposing a new
brainstorm. The requested return is research with complete parameter
dependence, not another plan or an early numerical choice.

The first package comprises CE-01 through CE-05, with CE-07's limit audit
running throughout and CE-08's assessment at the end. Advance CE-06 if an
acquired strict margin permits it. A task can yield a precise scoped
failure; do not treat the expected absence of a pre-existing canonical
energy bound as a reason to stop before performing the specified work.
The progress register defines deliverables and dependencies, so there is
no need to reconfirm the direction before routine analytical choices.

## Read first and preserve ownership

Read repository `AGENTS.md`, `tools/CHAT_HISTORY.md`, [the result index][results]
and [avoid index][avoid]. The essential mathematical entry points are:

1. [The new overview][overview] and [CE register][progress], including the
   distinct quantifiers for a fixed event, every positive slab and uniform
   control at zero.
2. [Note07][note], especially its shifted source, normalized error, energy
   coefficient and Section 9 clarification; [its assessment][assessment].
3. [The positive-threshold analysis][threshold], Sections 3 and 5, for the
   inherited finite-event reduction and the fixed-slab target.
4. [Complete coefficient transport][coeff], for the full source operator,
   exterior forcing and wall costs. Then [fixed-order recurrence][fixed]
   and [moving lower endpoint][moving] for the actual hierarchy domains.

Use the [control register][controls], [universal-profile limitation][profile]
and [coupled-estimate warning][a12] when an estimate is proposed. Consult
[the buffered response][response] only as needed for the specified alternate
consumer; do not take over chat0002's existing task.

The [parent register][trd] owns TRD-00 through TRD-08. This session works
under CE-01 through CE-08 and may supply evidence to TRD-07/08 later.
Chat0001's Dobner work and chat0002's response continuation remain with
their current owners. A new chat must use its own actual thread identity
and unique registration in this investigation's `chat-histories/`;
chat0003 above is provenance, not a registration to reuse. Follow the
standing beginning/end capture workflow.

## Mathematical starting point

The exact field is
\[
H(t,z)=\int_0^\infty e^{tu^2}\Phi(u)\cos(zu)\,du,
\qquad H_t=-H_{zz}.
\]
At a hypothetical threshold \(t_c=\Lambda>0\), let \(a\) have exact
multiplicity \(m\ge2\), with \(c=\partial_z^mH(t_c,a)/m!\ne0\). Work with
\[
F_r(s,w)=\frac{H(t_c+r^2s,a+rw)}{cr^m}.
\]
Its leading profile is the universal heat polynomial
\(e^{-s\partial_w^2}w^m\). The local Gaussian amplification is bounded
on fixed scaled sets, but the shrinking amplitude, derivatives, tails and
source information remain part of the error budget.

The shifted source is \(e^{t_cu^2}\Phi(u)\). Calling the relative time
negative does not restore the old negative-time theorem. Its lower time
onset, fixed physical buffers and high-height domain cannot be ignored.
A local Taylor expansion built from the assumed event reproduces that
event; it does not supply the independent upper estimate.

For unordered pairs in the collision cluster,
\[
E_{\rm cl}(t_c+u)=\frac{\kappa_m}{u}+O(u^{-1/2}),\qquad
\kappa_m=\frac{m(m-1)}{16},
\]
so an annulus \([r^2,4r^2]\) contributes
\(\kappa_m\log4+O(r)\). The double and triple coefficients are \(1/8\)
and \(3/8\). These are inherited facts to normalize against, not results
to rediscover as the main deliverable.

The missing independent upper estimate has the form
\[
\int_\epsilon^{u_0}E_W(t_c+u)\,du
\le (A_N+\eta_N)\log(u_0/\epsilon)+C_N,
\qquad A_N+\eta_N<\kappa_m.
\]
The bounded term cannot depend on an assumed minimum gap or on \(\epsilon\).
The multiplicity-independent bound below \(1/8\) is sufficient but stronger
than necessary. No numerical values of \(A_N\) or \(\eta_N\) have been
acquired in this program.

## Work sequence and branch decisions

**First establish the source interface.** Carry out CE-01 with a fixed
isolating contour. Use the complete prepared polynomial and source
operator, then derive the scaled discriminant/energy relation with every
exterior term. Identify a specific canonical source expression whose bound
could affect the energy coefficient. Label imported algebra separately
from a new estimate. This should specify the exact derivative and error
requirements for the next tasks.

**Build only the hierarchy the consumer needs.** Develop the first useful
finite-order CE-02 bound and the corresponding CE-03 transfer on
\(1\le s\le4\). Keep source tails and amplitude normalization. Determine
whether the ordinary negative-time recurrence can be adapted on a proved
domain or whether a direct shifted canonical integral is the better
starting point. A failure of one inherited representation is a reason to
test the other specified representation, not to fix the parameters or
start a numerical campaign.

**Test arithmetic discrimination early.** Carry out a first CE-04 estimate
while the interface and first transfer are available. Preserve the signed
coupling that could distinguish theta from colliding controls. If the
bound gives exactly the universal coefficient, identify the step at which
all distinguishing information was discarded. Test a coupled treatment
of that explicit term. Do not generate further hierarchy orders merely
to approximate the same compatible collision more accurately.

**Use the alternate consumer only for a defined reason.** If energy
transfer loses essential information or cannot be paid with the acquired
source data, test Note07's scaled pre-event transverse moment using those
same data. Its limit is \(2m(m-1)\), and any source upper bound must beat
that signal independently. Pay regulator bias and all moving-test terms.
A concrete improvement or scoped failure is required; simply switching
observables does not resolve the arithmetic obligation.

**Assemble the complete budget and continue through its consequences.**
For CE-05, separate summable \(O(r^\alpha)\) terms from persistent errors
per annulus. Convert a persistent error \(e_N\) to logarithmic coefficient
\(e_N/\log4\). Give actual dependence on order and the event parameters.
If a strict margin is acquired, continue to CE-06's coverage argument.
Otherwise finish the CE-07 dependency audit and CE-08 assessment using
the exact obstruction, rather than reporting only that a bound is missing.

## Keep the zero endpoint within the analysis

Do not specialize \(b\) just to simplify constants. For each proposed
estimate record whether it is valid at an arbitrary fixed positive event,
on each positive slab, or uniformly in a joint limit. Track height,
\(|c|^{-1}\), multiplicity, wall radius, order and regulator separately.
The exterior height onset \(\exp(C/b)\) is not the Gaussian loss eliminated
by local rescaling.

A proof for every fixed \(t_c>0\) may have constants depending on that
candidate and still exclude all positive thresholds. Likewise, a theorem
for every \(b>0\), or a proved sequence of upper bounds tending to zero,
would suffice. Bounded constants at \(b=0\) are a stronger goal, not an
automatic prerequisite. Fix parameters before taking \(r\downarrow0\)
unless a joint theorem justifies another order. A few successful positive
slabs do not prove the arbitrarily-small-time statement.

## When a new brainstorm is warranted

Continue routine work across the listed goals without asking for a new
choice after each lemma. A new brainstorm becomes appropriate when an
explicit calculation or matching control shows that the specified source
information cannot produce the needed coefficient, when both the energy
and specified transverse consumer leave the same demonstrated obstruction,
or when the next step requires a materially different hypothesis or
research direction. Save that evidence and complete any independent
remaining tasks first.

A zero-free boundary, exact event multiplicity and consequences of local
analyticity may be established conditionally on the event. An assumed
positive endpoint discriminant, favorable unknown margin or uniform
physical gap would assume the conclusion. Use [target classification][a01],
[control screening][a02] and [scope discipline][a07] to distinguish a
conditional interface from an acquired source estimate or exclusion.

## Required return and archival record

Save the derivations in the next available numbered note or notes in this
investigation, with source links, actual model/effort and complete parameter
domains. Save an assessment under `reviews/`, update the CE register's exact
status and evidence, and add navigation links as needed. Preserve unrelated
parent entries and unique chat histories. Do not reserve future filenames
without checking the current directory.

The research return should identify the exact new bound or scoped failure,
its baseline, whether the logarithmic coefficient or only the bounded
remainder improved, the applicable controls, the supported time/height
range and the next executable calculation. Link a concise continuation
if work remains. State honestly what was independently checked. Keep
large derived data outside Git and use commit/tag references for future
manuscript milestones rather than snapshot folders.

[overview]: ../research-overview/02_COLLISION_ENERGY_RESEARCH_OVERVIEW_20261027.md
[progress]: ../research-progress/02_COLLISION_ENERGY_RESEARCH_PROGRESS_20261027.md
[trd]: ../research-progress/01_THREE_REGIME_DYNAMICS_RESEARCH_PROGRESS_20261026.md
[note]: 07_COLLISION_SCALE_RESOLUTION_AND_PROOF_MECHANISMS_20261027.md
[assessment]: ../reviews/04_COLLISION_SCALE_MECHANISMS_SELF_ASSESSMENT_20261027.md
[threshold]: ../../02_heat_flow_rh_applications/notes/02_RODGERS_TAO_POSITIVE_THRESHOLD_20261026.md
[coeff]: ../../../investigations-4/12_height_dependent_heat_contours/notes/12_COUPLED_COEFFICIENT_BACKWARD_TRANSPORT_20261023.md
[fixed]: ../../01_heat_density_asymptotics/recurrence/notes/03_FIXED_ORDER_FLUCTUATION_HIERARCHY_20261026.md
[moving]: ../../01_heat_density_asymptotics/recurrence/notes/20_MOVING_LOWER_ENDPOINT_20261026.md
[response]: 01_BUFFERED_RESPONSE_AND_RESOLUTION_20261026.md
[profile]: ../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/notes/22_HEAT_SCALE_SIGNED_TRACE_AND_UNIVERSAL_PROFILE_20261021.md
[results]: ../../../../result-summaries/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../avoid/README.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a02]: ../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
