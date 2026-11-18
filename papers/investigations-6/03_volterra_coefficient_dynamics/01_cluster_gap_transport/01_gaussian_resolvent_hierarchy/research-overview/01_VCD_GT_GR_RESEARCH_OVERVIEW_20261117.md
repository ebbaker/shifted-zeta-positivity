# Gaussian scale decomposition and integer/resolvent evolution

17 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance. Setup chat0007, thread
01a1eb96-c257-77a3-96be-ee1cb0279757, turn
01a1ec37-585e-79d2-ab6b-ae0f872b508e. Actual lead model and effort are
unavailable. Intended research effort: **ultra**; recommended conceptual
lead: **Astra**; expressly authorized bounded helpers: **GPT-6.1 Sol/ultra**.
Recommendations and dispatch settings are separate from actual metadata.

## Question and scope

Can a joint description of the complete exterior interaction by distance
scales and interaction moments yield an improved one-sided forcing bound
or integrated backward-transport allowance for a selected pair?

The author chose both descriptions in the setup request following
[Discussion22](../../brainstorm/notes/22_VCD_GT_AUTHOR_SCALE_HIERARCHY_DISCUSSION_20261117.md).
The task is to develop them together and identify a useful quantitative
comparison. Gaussian partition identities and new hierarchy equations
are preparatory work; their existence alone is not a signed estimate.

Read the [result index](../../../../../../result-summaries/README.md), especially
[cluster18](../../../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md)
and [controls12](../../../../../../result-summaries/12_collision_controls_and_screening.md),
and the [avoid index](../../../../../../avoid/README.md), particularly
[classification01](../../../../../../avoid/01_restating_the_target.md),
[premises02](../../../../../../avoid/02_shape_only_arguments_and_the_controls.md),
[representations03](../../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md),
[scope07](../../../../../../avoid/07_scoped_exclusions_read_as_universal.md) and
[joint bounds12](../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md).
Use the [plan](../research-plan/01_VCD_GT_GR_RESEARCH_PLAN_20261117.md)
and [sole register](../research-progress/01_VCD_GT_GR_RESEARCH_PROGRESS_20261117.md).
The overview is not a second status register.

## Fixed objects and domains

Use the unchanged complete canonical theta field in physical Newman time,
\(\partial_tH=-H_{zz}\), initially \(0\le t\le1/2\). A separately established
conjugation-invariant count-two tube contains the two target occurrences,
with multiplicities, and excludes every exterior occurrence by a collar.
Set
\[
c=(z_++z_-)/2,\quad D=((z_+-z_-)/2)^2,\quad
w_j=\rho_j-c,\quad a_j=w_j^2-D,\quad M=-K=\sum_j a_j^{-1}.
\]
The sum counts the complete exterior divisor. Its conjugate sum is real.
Both signs of \(D\) and \(D=0\) remain in the domain. The goal allows real
multiple zeros at time zero; it must not assume positivity of an unknown
earlier gap, simple exterior roots, or an internal slope lower bound.

For the initial growing-height comparison use the inherited Section 17
domain: \(T\ge64\), \(L=\log T\), \(\ell=L^{-1}\),
\(c(t)\in[T,2T]\), \(|D|\le d\ell^2\),
\(\max(2,4\sqrt d)\le a\le L\), and exterior collar
\(|w_j|\ge a\ell\). The selected occurrences are within \(a\ell/4\).
Fix \(a,d\) when comparing height rates. Let
\[
\sigma=(t-t_0)/\ell^2,\quad \delta=D/\ell^2,\quad
m=\ell^2M,\quad \mu_j=\ell^2/a_j.
\]
The fixed band supplies uniformity; \(\ell\) is not differentiated in time.
A new domain or moving scale must be stated and its derivative terms paid.
The letter \(R\) denotes a spatial Gaussian length, not scaled time.

## Accepted consumer and baseline

The [shared manuscript](../../../manuscript/main.tex),
[pair transport §12](../../../manuscript/sections/gap_transport.tex)
(12.4), (12.9), and
[interaction dynamics §17](../../../manuscript/sections/interaction_dynamics.tex)
(17.1), (17.5), gives
\[
D'=2-4MD,\qquad
M'=2M^2-12S_2-16DS_3,\qquad S_p=\sum_j a_j^{-p},
\]
\[
m_\sigma=2m^2-\mathcal F,\qquad
\mathcal F=12\ell^4S_2+16\delta\ell^6S_3
=\ell^4(12S_2+16DS_3).
\]
For \(W(t,v)=\exp[-4\int_t^vM]\),
\[
W(t,v)D(t)=D(v)-2\int_t^vW(s,v)\,ds.
\]
An exact nonnegative margin gives \(D(t)\ge0\), and equality permits a
double. A strict conservative lower/upper-bound separation is sufficient
for \(D(t)>0\), not necessary for exact positivity. The undivided
Volterra identity and collision-anchored version are in
[Note44 §1](../../notes/44_VCD_GT_SCALE_AND_MOMENT_HIERARCHY_DISCUSSION_20261117.md#1-notation-and-edge-inclusive-transport).
The incoming anchor and existence/duration of the tube remain independent
obligations. An improvement for \(\mathcal F\) must have the useful
**upper-bound** direction, or supply a justified joint/integrated alternative.

| Inherited input | Status and use | Remaining limitation |
| --- | --- | --- |
| [Note41](../../notes/41_VCD_GT_E21_EXACT_INTERACTION_RICCATI_BOUND_20261117.md), [Synthesis42](../../notes/42_VCD_GT_B11_FIXED_COLLAR_SYNTHESIS_20261117.md), [Assessment19](../../reviews/19_VCD_GT_E22_FIXED_COLLAR_ASSESSMENT_20261117.md) | Proved and internally accepted within the independently paid tube: exact \(M\) law, \(|\mathcal F|\le C_FL\), interior negative allowance \(O(\sqrt L)\) after a fixed positive elapsed scaled time, multiplier \(O(L)e^{O(s\sqrt L)}\) | No every-pair positivity, tube acquisition or incoming gap |
| [Synthesis35](../../notes/35_VCD_GT_B07_B08_SYNTHESIS_AND_CONTINUATION_20261117.md) | Accepted far-tail asymptotic and fixed-slice exact-count/opposite-sign examples | Favorable normalized far contribution tends to zero at the selected cutoff; countermodels are not canonical common-time flows |
| [Synthesis39](../../notes/39_VCD_GT_B09_B10_SOURCE_ESTIMATE_SYNTHESIS_20261117.md), [Note40](../../notes/40_VCD_GT_E20_FIXED_COLLAR_TIME_OCCUPATION_20261117.md) | Accepted transverse mean, eligible-pair count and occupation improvements | An ordinary-center mean or growing occupation allowance does not exclude a particular pair |
| [Note44](../../notes/44_VCD_GT_SCALE_AND_MOMENT_HIERARCHY_DISCUSSION_20261117.md), [Record25](../../numerics/25_VCD_GT_HIERARCHY_DISCUSSION_CHECKS_20261117.json) | Preliminary exact scale decompositions and finite-polynomial next-moment calculation; same-assistant checks only | No assessed complete-theta extension or new canonical estimate |
| [Fixed tube Synthesis32](../../notes/32_VCD_GT_EXTERIOR_MASS_SYNTHESIS_AND_CONTINUATION_20261116.md) | Internally accepted local \(M>0.5937558081007126288\); target \(D>0\) already supplied | Validation input if useful; more precision is not new reality coverage |

Statuses are inherited through the named assessments. This setup performs
no new mathematical assessment, source computation or specialist review.

## Gaussian scale component

One preliminary radial choice is
\[
M_R=\sum_j\frac{\chi_R(w_j)}{a_j},\qquad
\chi_R(w)=e^{-|w|^2/R^2}.
\]
For increasing \(R_0<\cdots<R_n\), retain the complete telescope
\[
M=M_{R_0}+\sum_{k=1}^n(M_{R_k}-M_{R_{k-1}})+(M-M_{R_n}).
\]
The nonnegative weights sum to one, while the weighted interactions remain
signed. Note44 gives the corresponding continuum logarithmic-scale
density. The original author Gaussian \(e^{-\alpha w^2}\) is holomorphic
but has modulus \(e^{-\alpha x^2+\alpha y^2}\). A fixed-strip finite split
can be valid while its small-length endpoint grows. The radial Gaussian
is bounded and positive but nonholomorphic, requiring a justified weak
or integrated treatment of exterior mergers.

B01 must decide a precise joint formulation, comparing at most these two
initial Gaussian implementations per pass. It may use radial scales for
estimates and a holomorphic resolvent for dynamics. It must not assume a
smooth radial time law at all multiple events. Retain the derivative of
the moving center and transport across scales. A time-varying \(R\) needs
its own derivative contribution.

The starting physical analogy is Edward B. Baker III's 2017 continuum
sigma note, equations (5)–(11), pp.1–2, and its corrected scope in the
[reference guide](../references/README.md). Its real Coulomb
semigroup interpretation does not itself give positivity of this complex
zero interaction.

## Integer and resolvent component

A branch-free local generator is
\[
\mathcal R(\eta,t)=\sum_j(a_j-\eta)^{-1}
=\sum_{n=0}^{\infty}\eta^nS_{n+1}(t),
\quad |\eta|<\inf_j|a_j|.
\]
Thus \(S_2=\mathcal R_\eta(0)\), \(S_3=\mathcal R_{\eta\eta}(0)/2\).
The auxiliary \(\eta\) is a spectral probe, not a physical change to \(D\).

The preliminary finite-polynomial identity is
\[
S_2'=8MS_2-32S_3+4DS_2^2-40DS_4+4T_2^2,\qquad
T_2=\sum_j w_j a_j^{-2}.
\]
Its generic polynomial examples have equal full denominator multisets but
different \(S_2'\). This diagnoses information lost by using only squared
displacements in that class. It neither rules out a richer state nor a
canonical relation. The first complete-theta extension needs the finite
product/contour limiting derivative argument; it is not inherited as proved.

Use integer moments and spatial companions first. Continuous/complex
\(p\) may be introduced by a later recorded B decision if it has a concrete
consumer. Fixed-slice absolute convergence for \(\Re p>1/2\), branch choices
near negative denominators and the sector \(\Re a_j>0\) in the gamma
integral are separate issues. An infinite positive-ray transform may not
silently remove the adverse near terms. The [checked DLMF passage](../../references/02_VCD_GT_XI_QUADRATURE_BOUND_SOURCES_20261116.md#gamma-transform-passage-17-november-2026-chat0007)
has only its stated sector.

## Joint estimate and success criteria

Preserve correlations between \(D\), Gaussian pieces, spatial moments and
resolvent derivatives before estimating. In particular, \(M^2\) contains
all cross-scale products. Separate positivity of every band is not a
requirement, and independent absolute allowances are only comparators
unless justified as sufficiently sharp.

A selected quantitative contract must state:
- the exact observation, domain and source information beyond the existing
  counts and broad moments, or the demonstrable gain obtained by consuming
  those same inputs jointly;
- the complete signed inequality and useful direction, with all constants,
  height/collar/time dependencies and initial-layer terms;
- a matched baseline with identical geometry and data;
- the effect on the current forcing, integrated adverse interaction or
  backward cost, and any remaining anchor/tube obligations;
- the premise screen and the exact class of a possible failure.

A useful intermediate gain can be an improved height rate, constant,
valid domain or integrated cost. A height-independent forcing cap alone
still allows an order-one negative Riccati barrier; it is not a completed
reality proof. A finite diagnostic is not a uniform bound. Structural
identities may be necessary technical steps, but accumulation of them is
not the scientific objective.

## Controls and evidence discipline

Apply [controls12](../../../../../../result-summaries/12_collision_controls_and_screening.md)
and the existing [Note44 §7 screen](../../notes/44_VCD_GT_SCALE_AND_MOMENT_HIERARCHY_DISCUSSION_20261117.md#7-controls-scope-and-the-next-quantitative-question)
to the premise of each selected estimate. That inherited screen is
documentary plus its recorded polynomial checks; setup reruns none.
The quadratic and even quartic obey the generic decompositions and can
collide. The quartic fails the full incoming budget; neither polynomial
has canonical growing counts. Exact-count opposite-sign slice examples
pass the aggregate allowances without providing a canonical heat tube.
Other controls retain their named arithmetic, strip/order, observation,
multiplicity or untested-premise qualifications from the source screen.

A new inequality must identify the relevant failed quantitative premise,
not merely call the source theta. Negative conclusions name their class.
Higher clusters, a changed source or physical flow, unbounded numerical
searches, and sibling research are outside the initial branch scope.
They need an explicit author scope decision. Parent shared-manuscript
editing is not authorized by a child proof task.

## Ownership and execution

The [sole register](../research-progress/01_VCD_GT_GR_RESEARCH_PROGRESS_20261117.md)
owns VCD-GT-GR statuses. Scientific inputs stay at their existing parent
locations. One lead writes the shared register, synthesis and chat history;
helpers receive disjoint files or read-only tasks. B01/E01 lead into
specified E02/E03, assessment, and a quantitative B02/E06/E07 cycle.
The lead then makes the next justified in-scope decision and continues.
The [plan](../research-plan/01_VCD_GT_GR_RESEARCH_PLAN_20261117.md)
sets per-packet limits and escalation, while the continuation authorizes
a sustained session when invoked.
