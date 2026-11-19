# What the interaction estimate assumes and what dynamics add

19 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance. Actual recorded model and effort unavailable;
none is inferred. Status: **explanatory dependency audit of existing
results, same-assistant reading**. No new mathematical result, source
certificate, manuscript milestone or research-task disposition.

Edward asks whether the favorable-looking estimate d²M approximately 2
already requires precise gap information, and whether dynamics alone can
constrain the canonical zeros. His concern identifies the dependency
that should have led the earlier explanation: the canonical acquisition
of this estimate imports individual-zero localization, not merely
logarithmic counting density.

Read-first routing: [result index][results], [avoid index][avoid],
[Cluster18][cluster], [Controls12][controls],
[classification01][classification], [premises02][premises],
[scope07][scope] and [same-information12][same-information].
The representation, integration inequality and comparison below are
existing identities/theorems. No new global sign criterion is proposed.

## 1. Two lengths must not be conflated

Here g is the actual target gap, d is the local reference spacing from
the height-dependent clock, and D=g²/4. With delta=g/d and mu=d²M,
\[
 D'=2-\delta^2\mu,\qquad
 2DM=\frac{\delta^2\mu}{2}.
\]
Thus mu approximately 2 only implies D' approximately zero when delta
is also approximately one. A very small delta with mu of order one
instead gives D' approximately 2. The canonical readout in
[Discussion09][previous] demonstrates this distinction.
The statement d²M approximately 2 is not the stronger statement
g²M approximately 2 unless g/d is controlled.

## 2. The actual proof dependencies

[Printed §15][canonical] first imports the published canonical
localization theorem on a fixed slab I=[t0,t*] with t0>0.
At sufficiently high labels there is one real simple zero near each
nonuniform clock location q_n(t), uniformly on the slab. The error is
smaller than the clock spacing after increasing the height cutoff.
This is stronger information than an averaged counting asymptotic.

Put a=x_n, b=x_{n+1}, d=1/G_x(a,t), and L=log(X/(4pi)).
For actual neighbors within the specified local window, the proof obtains
\[
 \frac{x_{n+k}-a}{d}=k+e_k,\qquad
 |e_k|\le C E_R,\qquad e_0=0,\qquad
 E_R=LX^{-c_*t_0}+R^2/X.
\]
In particular, taking k=1 already gives
\[
 g=d(1+e_1).
\]
The individual gap is therefore bounded away from zero before the
interaction asymptotic is derived.

For each selected exterior index k not equal to 0 or 1,
\[
 \frac{d^2}{(x_{n+k}-a)(x_{n+k}-b)}
 =\frac1{(k+e_k)(k-1+e_k-e_1)}
 =\frac{1+O(E_R)}{k(k-1)}.
\]
The leading reference sum is the telescoping identity
\[
 \sum_{k\in\mathbb Z\setminus\{0,1\}}\frac1{k(k-1)}=2.
\]
The actual finite head differs from this reference by its localization
error and omitted reference tails. A separate height-dependent unit-count
estimate pays every actual exterior occurrence outside the window.
This produces, on the lemma's stated complete-real simple slices,
\[
 d^2M=2+O\!\left(E_R+\frac1{RL}\right).
\]
Negative heights and low zeros are included in that complete sum.
The later source-jet argument has a version not requiring the low
divisor to be real, with its own paid source inputs.

The logical direction is therefore
\[
 \text{canonical source localization}
 \ \Longrightarrow\ \text{individual separated geometry}
 \ \Longrightarrow\ \text{complete moment estimate}.
\]
It is not a derivation of individual separation from density alone.
The original analytic localization theorem genuinely establishes that
geometry; the downstream derivation is valid, but does not independently
extend its collision protection.

The opening of §15 says that these comparisons apply to the known
exterior “without extending its coverage.” Its joint-barrier subsection
also states that no cheaper acquisition or improved canonical onset is
demonstrated. These qualifications are material, not peripheral.

## 3. What the conditional dynamical theorem could provide

The general [joint comparison in §14][joint] does have a weaker input
interface than individual positions throughout the desired interval.
In backward physical time u it uses
\[
 V=1-2DM,\quad K=24D^2S_2+32D^3S_3,\qquad
 D_u=-2V,\quad V_u=(1-V^2-K)/D.
\]
A whole-time lower bound K>=1-eta², an initial upper bound V(0)<=v0,
and an initial lower bound D(0)>=d0 yield
\[
 D(u)\ge d_0-2vu,\qquad v\ge\max(v_0,\eta).
\]
The first-event proof excludes a collision on a duration Delta when
2v Delta<d0 and all stated regime/source requirements remain available
up to that event. It does not require high-precision root coordinates
at every subsequent time.

However, the current canonical acquisition gets its whole-time input
from the already separated clock geometry, including a lower bound
g>=(1-e)d throughout that regime. It demonstrates that the conditional
interface can recover the protection with those inputs. It does not
establish that the interface obtains those inputs more cheaply or
from genuinely weaker known canonical information.

There is also a quantitative issue after any small-defect estimate:
an absolute bound |D'|<=epsilon protects a known initial margin only
when epsilon Delta<D(initial). Since the density-scale D tends to
zero like log(X)^(-2), a bare assertion D'=o(1) does not automatically
pay a fixed duration. The manuscript keeps these rate requirements
explicit. This is an elementary integration observation, not a new
criterion or certificate.

## 4. Dynamics, source selection and information

The exact hierarchy reorganizes the evolution of one complete divisor.
It does not add independent source observations. Generic heat fields
satisfy these same local identities and can collide; for example,
H(t,z)=z²-2(t-T) has D=2(t-T), M=0, and D'=2 at its merger.
The source-specific restrictions that distinguish theta therefore
matter. A leading counting density does not specify the local
configuration, and fixed-order exterior regularity need not detect
an isolated closing target pair.

This does not imply that every dynamical approach is powerless.
Dynamics combined with other proved information can force new
constraints without computing every root. The
[Rodgers–Tao argument][rt] uses the hypothetical extension Lambda<0
to derive local equilibration incompatible with known zero statistics.
Its conclusion is the lower bound Lambda>=0; it does not supply the
upper-bound continuation sought here. This is an example of dynamics
and independent information doing substantive work, not a claim that
the argument can simply be reversed.

For the current investigation, there are three different achievements:
exact structure, controlled finite/source enclosures, and a new
restriction on previously unprotected canonical configurations.
The first two are established in their stated scopes. The
d²M asymptotic, acquired in the clock-controlled region, is not an
instance of the third. Earlier numerical error improvements likewise
retain their recorded local coverage and comparator.

The earlier preference for estimating the final observable concerns
efficient rigorous enclosure. It should not be read as a reason that
the hierarchy alone yields a new global zero constraint.
An advance in that direction would require a canonical estimate or
structural argument that remains effective in an unprotected regime,
without importing that regime's desired separation as its input.
No candidate meeting that requirement is proved in this discussion.

## 5. Direct comparison with Polymath

Follow-up, 19 November 2026, prepared for Edward Baker with OpenAI Codex
LLM assistance. The current chat registry records `gpt-6-astra`, reasoning
effort `max`; earlier unavailable configurations are not inferred.

Edward asks whether these methods improve on Polymath's results. For the
objective of additional collision protection or a better Newman upper
bound, **no improvement is demonstrated in the present manuscript**.
The positive-time high-height arguments import Polymath's localization
and remain inside its already protected exterior. Section 15 expressly
reports no numerical cutoff, estimate uniform down to time zero, new
compact gap law or improved bound on Lambda.

The exact hierarchy, controlled approximation results and refinements of
the project's earlier enclosure allowances are separate achievements.
They do not by themselves establish a stronger constraint on the zeros.
The enclosure gains have their stated internal comparators; they are not
a demonstrated improvement over Polymath's coverage or over an equally
informed direct method. This is an assessment of the manuscript's claims,
not a literature-wide novelty audit.

Even within the protected exterior, the matched direct clock comparison
matters: for a fixed positive time separation it pays roughly L² less
source error than the integrated squared half-gap estimate. At very short
times the integrated estimate can instead help because its allowance
vanishes with the time separation. This is a refinement of bounds in an
already controlled region, not new collision protection.

The useful unresolved question is whether the conditional dynamical
interface can acquire its inputs in a previously unprotected regime, or
with a demonstrated advantage over direct propagation using the same
information. Neither has been established here. The earlier explanation
gave the favorable moment asymptotic too much weight relative to this
dependency. This clarification changes no scientific task status.

## 6. How a better error estimate could give more protection

Second follow-up, 19 November 2026. Prepared for Edward Baker with OpenAI
Codex assistance; the chat registry records `gpt-6-astra`, effort `max`.
Edward proposes that improving the near-cancellation could eventually
give stronger control. This is a credible possibility. The earlier
no-improvement assessment concerns achieved coverage, not the potential
of the method. Under [classification01][classification], the following
is explanatory bookkeeping from existing laws and comparisons, not a
new criterion or an acquired canonical estimate. An actual finite
extension would be a quantitative milestone judged by its complete
margin and newly covered interval.

Keep the height-dependent reference d distinct from the actual gap g.
Put e_g=g/d-1 and e_M=d²M-2. The exact drift defect is
\[
 \mathcal E=2-g^2M
 =-4e_g-2e_g^2-(1+e_g)^2e_M.
\]
Thus a small e_M alone does not control the drift, and approximate
cancellation does not establish its sign. No uniform-chain model or
time-independent reference spacing is assumed in this identity.

In backward physical time u=t*-t the actual squared half-gap obeys
\[
 D_u=-\mathcal E.
\]
If a proved nonnegative envelope satisfies E(u)<=epsilon(u) up to a
first event, then
\[
 D(u)\ge d_0-\int_0^u\epsilon(s)\,ds,
 \qquad D(0)\ge d_0>0.
\]
Consequently an integrated allowance strictly below d0 prevents a
collision through the proposed duration, provided the contour/regime
and other exits are controlled. An upper bound on the shrinking part
suffices; requiring monotone widening would be unnecessarily strong.
This is the integrated pair law, not a new independent source bound.

For near-clock initial gaps, L=log(X/(4pi)) and D(0) is of order L^-2.
A uniform drift allowance epsilon therefore needs epsilon*Delta<D(0).
An o(L^-2) allowance pays any fixed available duration eventually.
Section 15 already obtains an O(L^-3) allowance through its joint-time
comparison, and a still sharper source-jet estimate. This demonstrates
the error-to-duration mechanism inside the established positive-time
domain. It does not extend the domain of the inputs.

The missing estimate must control the response over time. Section 14
uses V=E/2 and K=24D²S2+32D³S3, with
\[
 V_u=(1-V^2-K)/D.
\]
Its independently acquired lower K bound can keep an initially small
defect small. For the stated fixed-duration comparison, sufficient rates
are V(0)_+=o(L^-2) and (1-K)_+=o(L^-4) uniformly; the square root in
the forcing barrier explains the different powers. In contrast, the
particular initial-M Riccati envelope still has an O(g²) allowance even
with exact initial data. That limitation does not apply to all
time-dependent estimates.

There are two plausible kinds of gain: sharper explicit bounds could
lower a finite cutoff or extend a compact interval; a source estimate
remaining effective as time decreases could extend the analytical
domain. The present localization error contains X^(-c*t0), and the
source onset is exponential in 1/t0. At t0=0 the former ceases to decay.
Improving a prefactor at fixed positive t0 does not remove that loss of
uniformity. No uniform limit or new cutoff is asserted here.

The [compact source section][compact] already supplies a noncircular
way to attempt a finite extension. A cleared contour counting two roots
may survive their merger. One can estimate the complete interaction or
forcing for trial coordinates with D between a positive stopping value
and an independently established upper bound, then prove that the
actual trajectory cannot reach that stopping value. What remains is a
useful canonical estimate on a proposed extended domain, with all source,
time, exterior and contour errors included. Any gain should be compared
with direct enclosure from the same information. This discussion does
not activate a source campaign or claim such an extended estimate.

## 7. Polymath as the starting configuration for backward continuation

Third follow-up, 19 November 2026, for Edward Baker with OpenAI Codex
assistance; recorded chat configuration `gpt-6-astra`, effort `max`.
The author's interpretation is correct: the published high-height
separation can provide initial data for a backward continuation argument.
This clarifies the existing proposal; it establishes no extension.

For 0<t<=1/2, [Polymath Theorem 1.5][polymath] uses a sufficiently large
absolute constant C and a height threshold x>=exp(C/t). Its corresponding
index threshold must also be paid. After adjusting the constant and
retaining spatial buffers, the disjoint small disks around the clock
locations give real simple zeros and a lower gap bound on the scale
1/log x. The proof of part (i), after equation (104), gives the stronger
displacement O(x^(-ct)/log x), not just the weaker O(x^(-ct)) in the
theorem statement. No numerical C or sharp onset is extracted here.

For a pair remaining near a large reference height X, the sufficient
boundary can be pictured as t=C/log X. Start at t* inside the protected
region with an acquired positive D(t*). The useful extension would reach
a time t1 below that sufficient boundary. The zeros move, so a rigorous
implementation follows their labels and pays a spatial buffer; it does
not identify a fixed X with an exactly stationary root.

Using the nonnegative shrinking-error envelope from §6, the existing
integration bound in physical time reads
\[
 D(t_1)\ge D(t_*)-\int_{t_1}^{t_*}\epsilon(s)\,ds>0.
\]
The envelope and other continuation conditions must remain justified
throughout the proposed earlier interval, or up to its first event.
The lower initial gap is the starting margin; it does not itself supply
the subsequent complete interaction bound. Reapplying only the imported
localization inside x>=exp(C/t) supplies no crossing of its boundary.
A finite crossing with the complete error budget paid would be a new
local continuation result. A global Newman improvement additionally
requires coverage of every relevant pair/height and the interfaces.
The classification and analytical control screen in §§6 and 8 apply.

## 8. Scope and controls

The [Discussion06 analytical premise screen][screen] is retained.
Quadratic/quartic controls satisfy the generic local heat identities
while failing literal theta identification. Euler-factor controls
change the full source and lower-order count data, even when retaining
leading logarithmic density. Finite-source and finite-prime
perturbations retain only their documented finite data; they do not
supply the unchanged canonical source or its full localization theorem.
Static divisor surgery supplies neither a canonical path nor a
whole-time forcing bound.

The [full Discussion06 table][screen] also retains the atomic and
finite-profile controls (full theta/profile identity fails), the
RH-conditional endpoint construction (ordinary Dirichlet arithmetic
fails, and RH is a premise), and changed-kernel controls (the physical
Newman readout fails). For any eligible actual colliding pair, the exact
law gives integral E = D(0) by its first merger. A nonnegative upper
envelope therefore cannot satisfy the strict integrated margin on that
interval. At a regular isolated merger with bounded exterior moments,
E tends to 2 and K tends to zero. These are analytic screens of the
budget, not new numerical replays or evidence for an unproved global
criterion. The explicit quadratic control has E=2, K=0 and
D(u)=D(0)-2u, so the strict bound stops exactly before its collision.

These controls distinguish a valid general identity from an acquired
canonical margin. No new replay of their certificates is claimed, and
the limitation of the current acquisition is not an impossibility
theorem for alternative source estimates or dynamical methods.

[previous]: 09_VCD_GT_CM_HEIGHT_DENSITY_AND_GAP_FLUCTUATIONS_20261119.md
[results]: ../../../../../../../result-summaries/README.md
[avoid]: ../../../../../../../avoid/README.md
[cluster]: ../../../../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[classification]: ../../../../../../../avoid/01_restating_the_target.md
[premises]: ../../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[scope]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[same-information]: ../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[canonical]: ../../manuscript/sections/13_canonical_time.tex
[joint]: ../../manuscript/sections/12_joint_time.tex
[compact]: ../../manuscript/sections/15_compact_acquisition.tex
[rt]: https://arxiv.org/html/1801.05914v5
[polymath]: https://arxiv.org/html/1904.12438v2
[screen]: 06_VCD_GT_CM_RESEARCH_POSITION_AND_PATHS_DISCUSSION_20261118.md
