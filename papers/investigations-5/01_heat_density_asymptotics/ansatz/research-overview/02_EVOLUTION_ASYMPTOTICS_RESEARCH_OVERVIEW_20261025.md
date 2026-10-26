# Research overview: evolution-driven large-height asymptotics across time

25 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), recorded effort max**.
Ansatz chat0002, thread `01a17600-b15f-7f52-8713-31fa13599341`.

**Current overview.** This replaces Overview01 as the branch's planning
document at the author's request. [Overview01](01_HIGH_HEIGHT_ANSATZ_RESEARCH_OVERVIEW_20261025.md)
remains a historical record. The corresponding
[Progress02](../research-progress/02_EVOLUTION_ASYMPTOTICS_RESEARCH_PROGRESS_20261025.md)
is the sole live ansatz ledger. The [maintained manuscript](../manuscript/main.tex)
has been rewritten to follow this perspective.

## Objective and priority

Understand and rigorously bound the large-height asymptotics of the
canonical heat field for **all real times**, using the evolution
equations to derive corrections and track their errors. A short formula
is desirable; the proof and error estimate may be complicated. Different
regimes may require different formulas.

The primary success measure is a quantitative improvement or a newly
covered domain for the field and its required derivatives. Residual
cancellation, an exact PDE representation, or a qualitative description
of the modes becomes useful when accompanied by the canonical initial
comparison and a controlled solution error. Understanding the regulator
transition near t=64 remains important, but its fine analysis follows
this primary asymptotic-estimate work.

Three meanings of all times must be covered separately:

1. Every fixed real t, as X tends to infinity, with the t-dependence of
   constants and the height onset specified.
2. Uniformity on prescribed compact time intervals, including through
   zero, with full spatial buffers and estimates on overlaps.
3. Joint time-height limits t=t(X), including unbounded positive and
   negative times, with explicit scaling regions and matching.

No common onset for the entire real time axis is assumed. Substituting a
moving time into a fixed-time error is not a uniform theorem. The next
bounded packet concerns 1<=T=-t<=2; the research objective is wider.

## What the last round established

[Note07](../notes/07_CHAT0001_RESEARCH_SUMMARY_20261025.md) summarizes all
four completed packets in ansatz chat0001. Their status remains **proved
in-note from named classical inputs, same-model internal assessment
only**, with constants/onsets not numerically instantiated.

| Source | Accepted bounded output | Boundary to retain |
| --- | --- | --- |
| [Note03](../notes/03_OUTER_CORRECTION_AND_SIGNED_REAL_BRIDGE_20261025.md) | First corrected outer carrier on 32<=t<=33; buffered spatial jets through three and direct first time error. | Higher positive-time coverage and physical transfer do not follow automatically. |
| [Note04](../notes/04_COMPLEX_STRIP_REMAINDER_AND_BUFFERED_CROSSOVER_20261025.md) | Fixed-cutoff complex RS remainder and signed buffered crossover on \(\lvert t\rvert L\le8\). | Cutoffs are frozen on charts; no differentiation of a moving floor. |
| [Note05](../notes/05_FIXED_NEGATIVE_TIME_REPRESENTATIONS_20261025.md) | On 1<=T<=2, a short natural-gamma-scale formula and a distinct finite representation at outer-carrier precision. | Short natural-scale accuracy does not imply outer-scale accuracy; the latter representation retains growing orders and a bounded correction integral. |
| [Note06](../notes/06_NEGATIVE_BRIDGE_AND_TIME_JOIN_20261025.md) | Extension to 4/L<=T<=2 and a paid chartwise time join on [-2,0]. | The near-zero residual remains; physical spatial assembly and transfer are separate. |

Here L=log(X/(4pi)). In the crossover the relative allowance is
X^-3/4 exp(t_- L²/16), at most C X^-1/4 on the declared window.
For the short negative-time formula the field/jet/time allowance is
C |G| X^-3/4. The finite growing-order model attains
C E_o exp(-L²/4), and its heat residual is exactly zero on a frozen
chart. The joined [-2,0] allowance is C E_o X^-1/4 with the stated
logarithmic factors for derivatives. These statements preserve the
source domains and do not claim an all-time asymptotic theorem.

The parent [summary62](../../notes/62_CHAT0021_RESEARCH_SUMMARY_20261025.md)
and [progress register](../../research-progress/01_AVERAGED_DENSITY_RESEARCH_PROGRESS_20261024.md)
remain authoritative for the wider program. Notes54--55 supply a finite
analytical all-time/all-height construction on its declared strip;
Notes58--61 supply source compression, evaluation/filter budgets and
polynomial additional-accuracy-bit cost at fixed descriptor/query box.
Useful uniform height cost and the independent full-chain audit remain
open. The new asymptotic program should use this machinery where it
helps, without equating finite evaluability with a short asymptotic law.
Parent HDA-17 Partial, HDA-18 Gated and HDA-20 unfulfilled are unchanged.

## Evolution framework and mathematical contract

Keep the complete canonical source, H_t=-H_zz and
H(0,z)=xi((1+iz)/2)/8. Zeta height is X/2. Retain physical
q=epsilon_g², fixed K=k_ell k_h, actual signed covariance, and all
regulator and joining terms. The target physical strip is |y|<=1;
proofs also pay the full averaging, collar and analytic buffers.

For a spatially holomorphic F, set r_F=F_t+F_zz and E=H-F. Exactly,

\[
(\partial_t+\partial_{zz})E=-r_F.
\]

For T=-t this is forward heat evolution with forcing. The Duhamel
formula separates initial mismatch from integrated defect. Whole-line
absolute supremum contraction does not establish the much stronger
outer-carrier-relative estimate on a chart. A propagation proof must
pay function classes, tails, localization commutators, complex-strip
losses and the coefficients introduced by carrier normalization.
Increasing positive t requires the canonical analytic source or a
controlled contour argument, not an arbitrary-data backward-heat bound.

For a nonzero negative-time arm f=a exp(i theta), the exact heat equations
read a_T=a_xx-a theta_x² and theta_T=theta_xx+2(a_x/a)theta_x.
For f=f0(1+c), its residual divided by f0 is

\[
c_T-c_{xx}-2p c_x+r_0(1+c),\quad
p=(f_0)_x/f_0,\quad r_0=((f_0)_T-(f_0)_{xx})/f_0.
\]

These equations suggest controlled correction hierarchies. Match their
initial data to the canonical gamma/RS expansion and keep all modes and
the cutoff correction. The full signed field has zeros, so use positive
carrier envelopes and named complex arms rather than dividing by H.
[Note08](../notes/08_EVOLUTION_RESIDUAL_AND_NEGATIVE_TIME_MODES_20261025.md)
contains the exact identities and source map; [Note09](../notes/09_EVOLUTION_MANUSCRIPT_AND_PRIORITY_REVISION_20261025.md)
records their manuscript integration. Neither supplies a new improved
asymptotic theorem.

The short negative-time formula has mode damping exp(-T k_n²) and phase
drift -pi T k_n/4, where k_n=log(sqrt(X/(4pi))/n)/2. Fixed-mode damping
changes on T log²X; relative fixed-mode weights change on T logX.
At fixed T the weakly damped band still contains a growing population
near the cutoff. Component damping is not a dominance statement for
the signed total. This is the main interpretive opportunity at
intermediate negative times, and also the main cancellation obligation.

## Prioritized research program

| Priority | Workstream | Required quantitative outcome |
| --- | --- | --- |
| **1: large-height field estimates for all times** | HDA-A02: evolution corrections at negative time, then arbitrary compact negative intervals. | Improve an explicit field/jet/time allowance; state the remaining outer-scale loss and pay joins. |
| **1: same objective** | HDA-A08: compact positive-time coverage, especially the gap 1/2<t<32 and matching to the crossover and parent outer range. | A buffered canonical field comparison uniform on declared intervals, with direct time error and residual. Published small-positive and parent t>=32 inputs keep their separate hypotheses. |
| **1: same objective** | HDA-A04 and HDA-A05: joint positive and negative time-height limits. | Scaling regions, uniform remainders and proved overlaps; match the negative Gaussian endpoint without confusing absolute and relative error. |
| **2: physical meaning and assembly** | HDA-A06: transfer on completed domains, then full region assembly. | U,W,R,J,Q and the rest of the parent tuple, actual covariance, residual forcing, regulator derivatives and spatial/time joining defects. |
| **3: retained supporting work** | HDA-A03: the fine transition near t=64. | Named one-arm comparison and center shifts at the true rounding scale, then direct dynamic observable bounds. The existing packet is preserved. |
| **4: supporting simplification** | HDA-A07 and the optional part of A04. | Gaussian-polynomial core, Lambert-W replacement and useful cost only when they preserve paid errors or give a declared improvement. |

Priority 1 includes joint limits; it is not exhausted by a single
negative-time experiment. Physical transfer can be developed as soon
as a domain's input estimates are ready. The regulator transition is
retained as a concrete accuracy test, without displacing the missing
all-time asymptotic bounds.

## Immediate bounded next step

**Analysis — Sol**, [HDA-A02-AN03 r1](../research-progress/handoffs/HDA-A02-AN03.md),
is the primary next packet, prepared and not dispatched. The author's
new priority changes its queue position; its frozen mathematical
request is unchanged.

On 1<=T<=2 and the full fixed complex buffers, derive one explicit
evolution correction to the existing short F_N and prove a named
o(|G|X^-3/4) error for the field, spatial derivatives through three and
first time derivative. |G|X^-5/4 with specified logarithms is a work
target, not a promised rate. Supply the actual residual, canonical
initial matching, full mode-population bounds and separate natural/
outer-scale comparison. Stop at a precise failed estimate if the
focused attempt cannot establish a gain. A formally smaller residual
or an unevaluated Duhamel correction alone does not close the packet.

> Continue HDA-A02-AN03 r1 under Overview02 and Progress02. Derive one
> explicit negative-time evolution correction on 1<=T<=2 and prove an
> improved natural-scale field/jet/time error, with its actual residual
> and honest outer-scale conversion. Retain all arithmetic modes and
> canonical initial corrections; stop at the first precise unpaid estimate.

The task is analytical only. Routine derivations, constants and branch
bookkeeping are delegated to Sol within the packet. No automatic chat
creation, agent dispatch, model change or numerical campaign is implied.

## Evidence discipline and controls

Read the [result index](../../../../../result-summaries/README.md),
especially [heat-flow cluster11](../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md)
and [collision controls12](../../../../../result-summaries/12_collision_controls_and_screening.md),
and the [avoid index](../../../../../avoid/README.md). Relevant patterns
are [quantitative gain01](../../../../../avoid/01_restating_the_target.md),
[shared premises02](../../../../../avoid/02_shape_only_arguments_and_the_controls.md),
[same-model review05](../../../../../avoid/05_same_model_reviews_and_shared_premises.md),
[scoped exclusions07](../../../../../avoid/07_scoped_exclusions_read_as_universal.md),
[normalization08](../../../../../avoid/08_normalization_and_constant_slips.md),
[separate bounds12](../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md),
[checked imports16](../../../../../avoid/16_unchecked_imports_and_novelty_claims.md)
and [current statuses19](../../../../../avoid/19_status_files_that_lag_the_findings.md).

Classification: an approximation program, not an RH-equivalent criterion.
The heat and modulation equations also hold for collision controls and
exclude none. Euler-factor controls fail the unchanged full Dirichlet
coefficients; finite-prime matching is insufficient. Weighted-square and
theta-cutoff controls fail the canonical completion/RS expansion.
Reflected, smooth-shape, positive-primitive, counter-kernel and fixed-event
controls lack that same complete gamma/arithmetic identity. These premise
differences are not noncollision conclusions. A failed bound excludes
only its specified method or allowance, not every resummation.

Sources and manuscripts remain maintained in place. Save new mathematics
and input identities in notes/, assessments in reviews/, small work
records in numerics/, and milestones in DRAFT_HISTORY.md. The unique
[chat histories](../chat-histories/README.md) preserve their original
numbers and provenance; historical planning files are not live ledgers.
