# Continuation after the auxiliary flow literature survey

28 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), recorded effort max**.
Founding conversation: Investigation05 chat0017, *Assess auxiliary flow strategy*.

**Status: historical discussion handoff before planning.** For current
task routing, use the [research plan](../research-overview/01_AUXILIARY_COLLISION_FLOWS_RESEARCH_OVERVIEW_20261028.md#research-plan-for-an-independent-theta-estimate)
and [Progress01](../research-progress/01_AUXILIARY_COLLISION_FLOWS_RESEARCH_PROGRESS_20261028.md).
The preplanning discussion below is retained in its original scope.

The author has opened
Investigation06 to explore auxiliary evolutions and natural modifications
of the de Bruijn–Newman equation that might improve collision signals or
their analysis. The [initial overview][overview] supplies the background;
the new [forty-reference survey][survey] supplies related frameworks and
their hypotheses. **Further brainstorming comes before a research plan.**
No preferred flow, task sequence, progress register or numerical campaign
has been selected.

This note synthesizes the complete survey and the existing overview. It
does not independently audit all forty papers or add a mathematical
result. The survey was prepared by **gpt-6.1-sol, recorded effort ultra**,
with selected primary-source checks and explicitly stated access limits;
its same-model parallel searches do not constitute independent review.

## 1 Where the discussion stands

The useful idea inherited from Investigation05 is the freedom to design
an auxiliary evolution and its observable together. Geometry remains
available, but neither dimension three nor the earlier conservative
feedback equation is prescribed.

[Note28][n28] constructs a finite-time collision magnifier. Its global
regularity condition reformulates noncollision. [Note29][n29] obtains
regularity from an already available first-jet margin, without acquiring
that margin. These facts motivate a different flow whose response might
be easier to control; they do not rule out auxiliary-flow research.

The present distinction is between a useful diagnostic and an independent
constraint on the canonical source. A diagnostic can work on generic
colliding examples. An exclusion additionally needs information that
those examples fail. A large response alone is not a demonstrated gain
in attainable precision or an exclusion estimate.

## 2 Reading route

Read the [overview][overview], then the survey's opening **Connections
that change how the overview can be read** and **Collision-control
interpretation** sections. The following entry groups provide the closest
connections; this is a reading guide, not a research schedule.

| Discussion topic | Survey entries | Why they matter |
| --- | --- | --- |
| Universal exponential tilts | [ZP05][zp05], with original attribution in ZP01–ZP04 | Distinguish preservation for a whole source class from a canonical-source response |
| Local and finite-shift operators | ZP07–ZP09, [ZP10][zp10], [ZP11][zp11], ZP12 | Operator symbols, analytic domains and strip contraction; an operator and its exponential are separate claims |
| Controlled interaction motion | [LY10][ly10], supported by LY03–LY06 and LY08 | A substantive auxiliary-parameter precedent with essential ferromagnetic hypotheses |
| Zero dynamics and collision observables | [DY01][dy01], DY02–DY03, [DY09][dy09], DY10 | Localized interaction information, higher jets, analytic squared gaps and the difference between sensitivity and precision |
| The cosine flow and parabolic orientation | [AX06][ax06]–AX07, AX04–AX05 | Exact translation kernel; one-sided probability interpretation; forward versus backward heat |

[Note38][n38] contains the local calculations and exact Gaussian control.
[Note37][n37] preserves the broader motivation for returning to geometry.
The [reference catalog][catalog], [bibliography][bib] and
[PDF receipts][pdfs] retain versions and the actual scope of inspection.

## 3 Mathematical setup to retain

Use the complete canonical source and repository normalization
\[
H(t,z)=\int_0^\infty\Phi(u)e^{tu^2}\cos(zu)\,du,
\qquad H_t=-H_{zz},\qquad
H(0,z)=\tfrac18\xi\!\left(\tfrac{1+iz}{2}\right).
\]
The source-defined auxiliary family is
\[
F(t,s,z)=\int_0^\infty\Phi(u)e^{tu^2+s q(u)}\cos(zu)\,du,
\qquad F(t,0,z)=H(t,z).
\tag{1}
\]
For bounded real even q, it is entire in t,s,z for the theta source.
The new parameter s is distinct from Newman time t. At a nondegenerate
real double event, \(H(T,a)=H_z(T,a)=0\) and \(A=H_{zz}(T,a)\ne0\), define
\[
R_q(t,z)=F_s(t,0,z).
\]
The analytic squared gap of the two nearby zeros satisfies
\[
D(t,s)=8(t-T)-8\frac{R_q(T,a)}A s
+O\bigl((|t-T|+|s|)^2\bigr),
\tag{2}
\]
and the nearby curve of double events has T'(0)=R_q(T,a)/A.
This is the local nondegenerate setting; it is not a uniform height,
higher-multiplicity or threshold theorem.

The choices q=1 and q=u^2 give amplitude and Newman-time changes.
The quartic choice gives F_s=F_{zzzz}; theta's tail admits it for all
complex parameters, but a positive quartic tilt diverges on the
Gaussian-tail control for s>0. Also, the quadratic heat model has zero
fourth derivative at its double event. These are scoped limitations of
that candidate and control domain.

The constant/linear drift distinction in Note38 has been corrected:
bF_z translates the argument, while bzF_z dilates it with a time change.
Do not copy the earlier mislabeled dilation formula. Regular terms
proportional to F or F_z vanish at a double event; their possible global
effects remain a separate question.

## 4 What the survey adds

### Universal preservation is a restrictive objective

The survey derives from Pólya's universal-factor criterion, as stated in
ZP05, a precise restriction: if q is even entire and real on the real
axis, and exp(sq) is an admissible universal source multiplier at a fixed
nonzero real s, then
\[
q(u)=q(0)+cu^2,\qquad sc\ge0.
\]
The reason is that its rotated zero-free even Laguerre–Pólya function
must have only the Gaussian factor. Requiring both signs of s leaves
amplitude changes alone.

This concerns **universal zero-preserving exponential multipliers in the
stated class**. It does not dispose of source-specific estimates,
diagnostic deformations, nonexponential operators, or coupled systems.
In particular, the cosine tilt remains an explicit diagnostic candidate
even though it is not a universal preserver. The finite-difference and
strip-preserver theorems have their own operator and domain hypotheses;
the cosine in ZP10 is an operator symbol, not the bounded source weight
in equation(1).

### The cosine flow has a classical exact representation

For q_a(u)=cos(au), fix the mark a>0 independently of s and z. The
inherited response and the survey's Bessel expansion are
\[
F_s=\tfrac12\{F(t,s,z+a)+F(t,s,z-a)\},
\]
\[
R_{q_a}(t,a)=P_a(t)
=\int_0^\infty\Phi(u)e^{tu^2}\cos^2(au)\,du
=\tfrac12\{H(t,0)+H(t,2a)\}>0,
\tag{3}
\]
\[
F(t,s,z)=\sum_{n\in\mathbb Z}I_n(s)H(t,z+na).
\tag{4}
\]
Here I_n is the modified Bessel function. The canonical source provides
the domination needed to interchange the series and integral. For real
\(s\ge0\), the normalized flow is the exact probability average
\[
e^{-s}F(t,s,z)
=\mathbb E\,H(t,z+a(N_+-N_-)),\qquad
N_+,N_-\ \text{independent Poisson}(s/2).
\tag{5}
\]
Its generator is (T_a+T_{-a})/2-I, where T_a f(z)=f(z+a).
For real t it is a contraction in the real-line sup norm. The probability
interpretation requires \(s\ge0\); it does not extend as positive weights to
negative s. The unnormalized field retains its e^s amplitude factor.

Equation(4) makes the evaluation tradeoff explicit: translated original
observations and the series tail must be paid. It supplies a benchmark,
not a speedup theorem. Equation(3) gives a nonzero unfolding direction
at a marked double event, but ordinary Newman time already gives
square-root splitting. The ratio P_a/A and propagated errors still matter.

The survey also shows that this averaging can create collisions. In its
full-line atomic normalization, take mass 1-p at zero and p/2 at each
of \(\pm1\), with \(1/2<p<1\). Then
\[
H_\rho(z)=1-p+p\cos z,\qquad
F_\rho(s,z)=(1-p)e^s+pe^{-s}\cos z
\]
under \(q(u)=\cos(\pi u)\). Initially all zeros are real and simple. At
\(s_c=\tfrac12\log(p/(1-p))\), \(z=\pi\) is double, and for \(s>s_c\)
the zeros are nonreal. This control passes the bounded-tilt and strict
response conditions; it lacks continuity, the theta tail and canonical
arithmetic. It is not a claim about the theta trajectory.

### Coupled interactions provide a substantive precedent

Hou–Jiang–Newman, [LY10][ly10], studies zero motion under a changing
ferromagnetic interaction. In its stated connected finite-spin setting,
distinct zero trajectories are disjoint; the Curie–Weiss specialization
gives strict motion of principal zeros. This is a close example of an
auxiliary parameter with mathematically controlled zero behavior.

Its component measures and interactions are essential. Treating the theta
density itself as a single spin already known to have the Lee–Yang
property would assume the sought zero geometry. A useful connection would
need a justified representation using independently admissible inputs.
LY02 and LY08 provide approximation and closure precedents, but such
limits can have multiple zeros; they do not supply a simplicity margin.
LY06's auxiliary-field nonvanishing domains likewise come from an existing
Lee–Yang theorem, not from positivity alone.

### Established diagnostics clarify what a gain would mean

DY09 continues analytic sums, squared differences and partial
discriminants of coalescing eigenvalues. This is a direct precedent for
equation(2), with fresh theta-specific error and omitted-zero estimates
still needed. DY10 distinguishes enhanced branch sensitivity from
attainable measurement precision in its particular sensor model; it is
not a universal obstruction to deterministic numerical improvement.

DY01 and DY02 explain why surrounding-zero interactions and complete
localized energy terms matter. Their estimates belong to the original
flow; a changed generator does not inherit them automatically. DY03's
higher-jet Lehmer tests retain both their RH premise and conditioning
near a vanishing first derivative.

## 5 Qualifications that must travel to the next session

The survey flags Cardon's **corrected arXiv:1401.0237v3, 20 October
2026** in ZP11. Use its recorded hypotheses and corrections; do not revive
the withdrawn conjectures from the uncorrected published text. Historical
entries read only through metadata or later statements retain that
inspection status. The forty references are not forty audited proofs.

Polynomial operator preservation, preservation by exp(sL), and continuity
on the relevant entire-function space are different assertions. Positivity
of a density, positive semidefiniteness and total positivity are also
different hypotheses. AX04–AX05 concern scalar forward parabolic time
r=-t, with their interval/boundary conditions; they do not automatically
apply to fourth-order, nonlocal or coupled equations or to a global count
of infinitely many theta zeros.

Keep the survey's [collision-control screen][survey] and the repository
[control register][controls] in view. Euler-factor controls change the
canonical factors; weighted-square and finite-prime controls fail complete
coefficients or reflection; reflected and positive-primitive controls lack
canonical square arithmetic. Their admitted positive continuous sources
share the bounded response calculation. These failed canonical premises
are not themselves a separating estimate. Atomic strict positivity
requires its explicit support condition. No new numerical control run or
theta exclusion is claimed by this handoff.

The [result index][results] and [avoid index][avoid] apply, particularly
[heat-flow results][heat], [target reformulations][a01],
[shared control premises][a02], [coordinate realizations][a03],
[scoped exclusions][a07] and [unchecked imports][a16].

## 6 Resume with discussion rather than a selected program

The open choices concern the desired benefit: clearer collision
diagnostics, controlled motion under a deformation, or an independently
estimated quantity that could constrain the physical slice. Local terms,
finite shifts and coupled interactions remain possibilities. The cosine
family is a concrete comparison example, not an automatically chosen
research direction.

The next conversation can explore which structure in these precedents
could connect to the complete theta source, and which observable that
connection would make easier to control. The survey's restrictions should
help make the alternatives precise without becoming broad impossibility
claims. Do not turn the bibliography into task IDs, a numerical grid or a
research plan before the author requests that step.

## 7 Suggested prompt for the next session

> Continue Investigation06, auxiliary flows for collision analysis, from
> `papers/investigations-5/06_auxiliary_collision_flows/notes/01_CONTINUATION_AFTER_LITERATURE_SURVEY_20261028.md`
> in `/Users/ebbaker/Documents/shifted-zeta-positivity`. Read the linked
> overview and literature survey. We are still brainstorming natural
> modifications of the de Bruijn–Newman flow and auxiliary evolutions that
> could enhance or help control collision signals; do not create a research
> plan or progress register yet. Explain what the survey adds to this idea,
> especially universal-factor restrictions, the cosine flow's exact
> translation representation, and controlled Lee–Yang interaction motion.
> Keep diagnostic improvement distinct from collision exclusion and retain
> the original physical slice, source hypotheses and error costs. Treat the
> cosine example as a benchmark rather than a chosen program, and discuss
> other local or coupled mechanisms without committing to dimension three.
> Preserve the cited results' scopes and save new brainstorming in this
> investigation with the actual model and effort recorded.

## 8 Files and conversation identity

The actual survey directory is **lit-survey/**. Links and the reference
catalog have been aligned with that path; the underscore in the PDF
manifest's filename is intentional. The survey text and its source
inspection records remain the basis for this synthesis.

The founding chat remains uniquely registered as Investigation05
chat0017. The literature-survey chat is Investigation06 chat0001. See the
[history guide][history]; do not duplicate or renumber either archive.
A genuinely new session should register its actual identity here through
the repository history workflow. Future derivations belong in notes/,
brainstorming in brainstorm/, numerics in numerics/ and assessments in
reviews/. No manuscript, research plan or progress register is created
by this continuation.

[overview]: ../research-overview/01_AUXILIARY_COLLISION_FLOWS_RESEARCH_OVERVIEW_20261028.md
[survey]: ../lit-survey/01_AUXILIARY_COLLISION_FLOWS_ANNOTATED_LITERATURE_SURVEY_20261028.md
[catalog]: ../references/sources.json
[bib]: ../references/sources.bib
[pdfs]: ../references/lit_survey_pdf_manifest_20261028.json
[history]: ../chat-histories/README.md
[n28]: ../../05_radial_theta_collision_geometry/notes/28_ENERGY_NORMALIZED_CONSERVATIVE_COLLISION_MAGNIFIER_20261028.md
[n29]: ../../05_radial_theta_collision_geometry/notes/29_POSITIVE_CARRIER_COMPARISON_AND_QUANTITATIVE_REGULARITY_20261028.md
[n37]: ../../05_radial_theta_collision_geometry/notes/37_GEOMETRY_DISCUSSION_AND_RETURN_CONTINUATION_20261028.md
[n38]: ../../05_radial_theta_collision_geometry/notes/38_AUXILIARY_SOURCE_FLOWS_AND_COLLISION_RESPONSE_20261028.md
[zp05]: ../lit-survey/01_AUXILIARY_COLLISION_FLOWS_ANNOTATED_LITERATURE_SURVEY_20261028.md#zp05
[zp10]: ../lit-survey/01_AUXILIARY_COLLISION_FLOWS_ANNOTATED_LITERATURE_SURVEY_20261028.md#zp10
[zp11]: ../lit-survey/01_AUXILIARY_COLLISION_FLOWS_ANNOTATED_LITERATURE_SURVEY_20261028.md#zp11
[ly10]: ../lit-survey/01_AUXILIARY_COLLISION_FLOWS_ANNOTATED_LITERATURE_SURVEY_20261028.md#ly10
[dy01]: ../lit-survey/01_AUXILIARY_COLLISION_FLOWS_ANNOTATED_LITERATURE_SURVEY_20261028.md#dy01
[dy09]: ../lit-survey/01_AUXILIARY_COLLISION_FLOWS_ANNOTATED_LITERATURE_SURVEY_20261028.md#dy09
[ax06]: ../lit-survey/01_AUXILIARY_COLLISION_FLOWS_ANNOTATED_LITERATURE_SURVEY_20261028.md#ax06
[results]: ../../../../result-summaries/README.md
[heat]: ../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../avoid/README.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a02]: ../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a03]: ../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a16]: ../../../../avoid/16_unchecked_imports_and_novelty_claims.md
