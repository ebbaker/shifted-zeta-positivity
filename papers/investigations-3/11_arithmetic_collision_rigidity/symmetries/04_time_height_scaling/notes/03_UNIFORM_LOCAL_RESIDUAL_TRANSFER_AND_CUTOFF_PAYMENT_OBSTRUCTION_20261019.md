# S04-T3: uniform local residual transfer and a cutoff-payment obstruction

19 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual recorded model **gpt-6.1-sol (Codex)**,
reasoning effort **ultra**. Separate same-model mathematical and prior-work
readers; internal LLM review, no independent specialist human review.

**Outcome:** proved in-note, using the inherited complete fixed-cutoff RS
disk theorem. The S03 endpoint method transfers to a precisely specified
family of local charts at every height in the S04 sector. The complete
local residual increment is `<46.679 exp(-b*/t)`. The stipulated method
of concatenating natural-cutoff charts with independent coefficientwise
transition disks assigns at least `.99 exp(1/(4t))` across the sector.
That payment diverges as time shrinks. This completes S04-T3's permitted
**uniform intermediate theorem and quantified failed-transfer branch**;
global calibrated arithmetic transfer and a positive physical anchor
margin remain open.

## Contract, information and prior results

This continuation follows the [overview][overview], [tracker][tracker],
[result summaries][results] and [patterns to avoid][avoid], particularly
[target reformulations][a01], [control premises][a02], [scoped negative
results][a07] and [preserving signed cancellation][a12]. Its primary metric
is the assigned complete error for a specified endpoint continuation rule,
including anchor uncertainty and every cutoff transition. It proposes no
new global nonvanishing criterion.

The [earlier manuscript][earlier], Proposition `sc:paiderror`, already
proves the uniform complete radius-1/L disk error, all fixed-order center
derivative payments and validity arbitrarily near a cutoff crossing.
Its `prop:absmass` already establishes growing absolute mass. [S04 Note
01][n01] supplies the phase-retaining first-jet model and exact transition
derivatives. [S03 Note 04][s03-4] supplies the real-Schwarz-Pick endpoint
argument; [Note 07][s03-7] supplies the exact primitive and its much sharper
fixed-pilot arithmetic estimate. The present output is explicit local
transport bookkeeping and a quantified failure of one concatenation rule,
not a new arithmetic cancellation theorem.

In particular, the S03 corrected residual
`Q-(G8-Chat8)/A`, its fixed B certificate `<0.000854`, RS8 profile Taylor
chart about `p0=-21/25` and finite tau tube are **not** transferred by
relabeling. We use the separately named residual below. Neither that
fixed-pilot allowance nor the stronger source-informed `<0.000266448`
is a comparator in this different domain and approximation norm.

## Uniform local chart theorem

Choose any center in
\[
 0<t\le1/20,\quad1\le\kappa\le2,\quad
 L=\kappa/t,\quad c=4\pi e^L,\quad
 N=\lfloor\sqrt{e^L+t/16}\rfloor,\quad R=1/L,
 \qquad b_*={\kappa(\kappa+4)\over16}.
\]
Freeze **t and N** on the whole analytic disk and define
\[
 r_c(t,z)=Q(t,z)-F_{t,N}(z),\qquad
 \eta_c=5e^{-b_*/t},\qquad |z-c|\le R.                    \tag{1}
\]
Here F is the exact finite scalar from Note 01, rather than its
leading-data replacement. The inherited theorem gives `|r_c|<=eta_c` on
that disk, including the correction for a possible change of the natural
cutoff. No floor-defined function is differentiated. Consider the closed
real chart `|y-c|<=R/2`. These small excursions may leave the center's
kappa interval; (1) holds on the original disk and does not require a new
center theorem at y.

Let `omega=theta_x=-Omega`, `C=4.001`, and
\[
 Z_g=e^{-i\theta}(g-i g_x/\omega),\qquad
 I_{r_c}(c,y)=i\{Z_{r_c}(y)-Z_{r_c}(c)\}.                 \tag{2}
\]
The exact S03 identity identifies (2) with the full signed filtered
integral, including every partial real prefix. It holds because r_c is
one analytic residual, without assuming an unforced heat equation.
Indeed, differentiating Z_r gives
`Z_r,x=-i exp(-i theta) omega [r+r_xx/omega^2-omega_x r_x/omega^3]`.

**Proposition 1.** Uniformly in this family of charts,
\[
 |Z_{r_c}(c)|\le C\eta_c,
 \qquad |Z_{r_c}(y)|\le {4C\over3}\eta_c,
 \qquad |I_{r_c}(c,y)|\le {7C\over3}\eta_c
                  <46.679e^{-b_*/t}.                    \tag{3}
\]

*Proof.* Note 01 (6) gives
`Omega(c)>=L(1-.005/c)/4`. [Note 02][n02] (13), on its larger already
justified real window, gives `|Omega_x|<.250003/c`. Consequently
\[
 {\Omega(y)\over L}\ge {1-.005/c\over4}
                -{.250003\over2L^2c}>{1\over4.001}.       \tag{4}
\]
The last inequality has a fixed positive reserve: substitute L=20 and
c=4*pi*exp(20) into its two decreasing losses. It is therefore uniform
without a height grid.

Set `s=(y-c)/R`, `u=r_c(y)/eta_c`. The residual is real on the real axis.
Real-symmetric Schwarz-Pick on the original disk yields
\[
 |u|\le1,\qquad
 |r_{c,x}(y)|\le {L\eta_c(1-u^2)\over1-s^2}.              \tag{5}
\]
For any K>=1, the convex polynomial
`v+K^2(1-v)^2`, `0<=v<=1`, is at most K^2. Thus (4)-(5) give
\[
 |Z_{r_c}(y)|\le {C\over1-s^2}\eta_c.
\]
At the center use s=0; at any other chart point use `|s|<=1/2`.
The triangle inequality in the exact primitive (2) proves (3). All
derivatives refer to the same frozen scalar. A paid second derivative is
unnecessary for this endpoint route. The zero residual case follows by
continuity. The Schwarz-Pick boundary case is a constant function. ∎

The maxima of these explicit allowances occur at kappa=1,t=1/20:

| Complete normalized quantity | Uniform coefficient times exp(-b*/t) | Opening upper allowance |
| --- | ---: | ---: |
| Anchor residual uncertainty | 20.005 | <0.038619 |
| Direct endpoint uncertainty | 80.02/3 | <0.051492 |
| Residual increment | 140.035/3 | <0.090111 |
| Approximate-anchor uncertainty plus increment | 200.05/3 | <0.128730 |

These are upper allowances derived from an inherited analytic theorem,
not measured errors. No value of H or signed sum is sampled here.

For physical return, with `a=partial_x log A`, (1),(5) also give
\[
 |\delta H|/A\le\eta_c,\qquad
 |\delta H_x|/A\le(4L/3+|a|)\eta_c.                      \tag{6}
\]
This includes the normalizer derivative. The first-jet coordinate
conversion is the same throughout the chart.

## Anchor error is not a positive anchor margin

The calibrated identity is
\[
 Z_Q(y)=Z_Q(c)+Z_F(y)-Z_F(c)-iI_{r_c}(c,y).               \tag{7}
\]
An independently enclosed Q anchor has its own uncertainty, paid once.
If only F(c) is available, (3) pays `C eta_c` to replace the anchor, so
the total normalized uncertainty is `(10C/3)eta_c`. The direct endpoint
payment is only `(4C/3)eta_c`. This same-envelope comparison gives no
consumer advantage to calibrated propagation. It asserts neither a
timing disadvantage nor optimality of the envelope method.

Equation (3) supplies no positive lower bound for `|Z_Q(c)|`, and a
positive anchor alone does not pay the approximant's intervening
variation. The Gaussian average and weighted energy of Note 02 permit
isolated collisions and cannot fill this gap at every selected anchor.
An event with Q=Q_x=0 can have r_c=0 if F=Q; zero approximation error by
itself has no exclusion content. The missing positive signed input stays
explicit rather than being called an additional established symmetry.

## Quantified failure of independent transition disks

Proposition 1 holds with a single fixed N on each local disk. A
continuation across the full sector at fixed t would cover
\[
 4\pi e^{1/t}\le x\le4\pi e^{2/t}.                       \tag{8}
\]
If the finite approximant is reset to its natural cutoff, its residual
and rotating primitive jump. For a crossing at
\[
 x_n=4\pi(n^2-t/16),\qquad L_n=\log(n^2-t/16),
\]
the exact entering mode is `g_n=2w_n cos(phi_n)`. At fixed t,n,
\[
 g_{n,x}=2w_n\{-tV\log n\cos\phi_n/4
       +[\Omega-(1+tU/2)\log n/2]\sin\phi_n\}.             \tag{9}
\]
Here U+iV=alpha' and V>0. Consider **exactly** the rule that envelopes
the value and derivative separately and adds their independent rotating
error disks at each transition. It assigns the valid radius
\[
 J_n=2w_n\sqrt{1+
 \left[{tV\log n/4+|\Omega-(1+tU/2)\log n/2|\over\Omega}\right]^2}
 \ \ge2w_n.                                               \tag{10}
\]
For the leading-data model, replace w_n by W_n, U by zero and V by 1/x_n.
That corresponding rule has the same lower bound with W_n. These are
**assigned envelope radii**, not lower bounds for actual mode jets.

**Proposition 2.** Either stipulated independent transition rule assigns
across (8) a total budget greater than `.99 exp(1/(4t))`.

*Proof.* Put B=exp(1/t) and retain only
\[
 \lceil B/2\rceil\le n\le\lfloor B\rfloor.                \tag{11}
\]
Every crossing lies in (8): its kappa lies below 2 and above
`2-2t log 2-t^2/(2B^2)>1.93>1`. There are at least B/2-1 indices.
The real-axis identity `alpha_r<=L_n/2` implies w_n>=W_n. Since
L_n<2 log n and log n<=1/t,
\[
 W_n(x_n)=\exp\{-\log n/2+t\log^2n/4-tL_n\log n/4\}
       \ge e^{-3/(4t)}.                                    \tag{12}
\]
Therefore the assigned sum is at least
\[
 2(B/2-1)e^{-3/(4t)}
   =(1-2e^{-1/t})e^{1/(4t)}>.99e^{1/(4t)}.                \tag{13}
\]
The sharper prefactor is >0.99999999 throughout t<=1/20. ∎

The lower assigned budget is already >148.413 at t=1/20 and diverges as
t decreases. All other independent errors can only increase that rule's
payment. The family of local errors decays, but this concatenation rule
does not retain that advantage across the growing number of cutoffs.
Moreover it would need anchor control and variation of the retained
signed approximant. Simply adding local increment radii would also lose
telescoping; (13) already rejects the declared rule before those costs.

This is a quantified failure of **independent coefficientwise
cutoff-transition payments for the uncorrected natural finite scalars**.
It is closely related to the inherited absolute-mass obstruction.
Actual jumps may cancel. A coherent corrected RS edge can cancel large
printed jumps. Signed summation of transition vectors, coherent edge
matching, a different fixed-cutoff organization and genuinely stronger
arithmetic residual estimates remain outside this exclusion. No lower
bound for the actual theta residual or its signed increment is proved.

## Complete ledger, checks and decision

The imported disk theorem pays the full theta RS representation,
reflection, normalization, all omitted terms and any cutoff adjustment
inside the original disk. Equations (4)-(5) pay movement and derivatives
through every closed real chart. Equations (3),(7) pay endpoint and anchor
uncertainty. No source quadrature, extra mode truncation, polynomial
approximation or differentiated floor is introduced. Transition payments
are explicit in (9)-(13); no finite-to-infinite extrapolation is made.

The [checker][checker] pins the actual analytic sources and evaluates
the monotone endpoint constants at 192/256 bits with outward Arb
arithmetic. Four scalar evaluations of (13) illustrate the analytic
formula; they are not height coverage. Fixtures include real Schur
extremals, a constant residual, an exact oscillator, an own-envelope
polynomial collision that rejects strict propagation, opposing transition
vectors, invalid contracts and missing/stale source identities.
[Separate same-model review and fresh replay][review].

Reproducibility caveat: an initial attempt to validate the whole historical
S04 opening record failed because its research-program guide hash is
stale. All its mathematical source hashes still match. That record was
left intact and is not claimed as a fresh successful replay. This new
analytic corollary imports the named theorem/notes under its own explicit
mathematical source pins; it consumes no historical point-jet output.

Fresh [source-specific acceptance controls][control] reject five event
boxes and the Euler negative-Laguerre witness in the unchanged signed
consumer. Theta's disk allowance is not assigned to altered sources.
Finite-prime and finite weighted-square controls lack unchanged complete
theta reflection/coefficient data; reflected, shape and primitive controls
lack the specific theta square expansion; Euler controls alter the level
and coefficients. Polynomial and counter-kernel controls share the
generic transport identity and lack the theta source contract. Positive
auxiliary observations do not supply the complete physical signed jet.
Analytic-only finite-prime/smooth constructions receive no invented event
box. These controls screen interpretation, not a new exclusion consumer.

**Decision:** S04-T3 is Complete for this intermediate theorem and scoped
failed-transfer deliverable. Stop independent transition-disk
concatenation across the sector. The next viable global branch needs a
coherent signed cutoff matching and an independently paid physical anchor
or signed core estimate. No new task ID or extension is activated. S04-T1
stays Conditional on choosing a second-derivative consumer. G4's global
calibrated transfer, the real bridge, the complex exterior and a new
Newman bound remain open. No manuscript snapshot is created.

[overview]: ../../research-overview/01_RESEARCH_OVERVIEW_GOALS_AND_TASKS_20261018.md
[tracker]: ../../research-progress/01_RESEARCH_TASK_TRACKER_20261018.md
[results]: ../../../../../../result-summaries/README.md
[avoid]: ../../../../../../avoid/README.md
[a01]: ../../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[earlier]: ../../../../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/newman_collision_reductions.tex
[n01]: 01_PHASE_RETAINING_FULL_CUTOFF_SCALING_20261018.md
[n02]: 02_GAUSSIAN_SIGNED_CORE_AND_COMPLETE_AVERAGED_VALUE_20261019.md
[s03-4]: ../../03_normalized_jet_rotation/notes/04_PHASE_AWARE_ANALYTIC_ALLOWANCE_AND_KERNEL_VARIATION_OBSTRUCTION_20261019.md
[s03-7]: ../../03_normalized_jet_rotation/notes/07_COMPLETE_ARITHMETIC_EDGE_AND_RESIDUAL_INCREMENT_20261019.md
[checker]: ../numerics/check_uniform_residual_transfer.py
[review]: ../reviews/03_UNIFORM_RESIDUAL_TRANSFER_INTERNAL_REVIEW_20261019.md
[control]: ../numerics/S04_T3_CONTROLS_20261019.json
