# Research overview: the unconditional positive-time hierarchy and regional bridges

26 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), actual effort max**,
verified from session metadata. Origin: recurrence **chat0007**, thread
01a178d3-5b84-7a81-9cbe-2210fd235c35.

**New focused program overview.** The author requests a large positive time
hierarchy studied independently of RH, followed by bridges across multiple
regions: first the regulator transition near 64, then intermediate positive
times and zero, and finally connection to the negative-time hierarchy.
The [new progress document][progress] is the sole live record for this
program and HDA-A04 execution. [Overview02][umbrella] retains the wider
all-time ansatz context; its older immediate priorities are superseded.
The opening document planned research. The execution updates now record
the first two corrections, arbitrary-fixed-order theorem and first
compact-positive high-height field bridge. Progress03 owns live status.

## 1. Objective and order

Develop a quantitatively controlled asymptotic hierarchy for the canonical
heat field as \(t\to+\infty\), understand what each level resolves and how
its error depends on time and spatial height, then construct a chain of
compatible approximations across the other time regions.

The order is:

1. **Understand large positive time well, without RH.** Establish the
   leading behavior, successive corrections, complete errors and the
   regimes of height in which the statements are uniform.
2. **Extend into the finite positive-time region and through the
   regulator switch near 64.** Match the field and the regulated
   observables with the fixed physical regulator and averaging rule.
3. **Cover intermediate and small positive times.** Retain the arithmetic
   information needed as large-t simplifications weaken.
4. **Pass through zero and connect to the negative-time hierarchy.**
   Use genuine overlap estimates, including all derivative and joining
   terms, to describe the transition between asymptotic organizations.

All four are goals of this program. The opening plan deferred bridges
until the large-time gate was paid. Notes17–19 now establish that gate
at arbitrary fixed order, and Note20 starts the compact-positive
high-height field bridge. The remaining regional and physical outputs
stay open; no all-time theorem is claimed.

## 2. An unconditional mathematical contract

Keep the exact source and normalization
\[
H(t,z)=\int_0^\infty e^{tu^2}\Phi(u)\cos(zu)\,du,\qquad
H_t=-H_{zz},\qquad H(0,z)=\xi((1+iz)/2)/8.
\]
The complete theta source, xi functional equation, ordinary Dirichlet
series on its convergence half-plane, and justified gamma/contour
estimates supply the information. **Do not assume RH, reality of every
zero at t=0, or a value of the de Bruijn--Newman threshold.** A zero
conclusion, if pursued later, must be derived independently from proved
canonical estimates. Approximating the field does not alone prove it.

For positive time the exact anchor is
\[
H(t,z)=\frac1{\sqrt{\pi t}}\int_{\mathbb R}
e^{-v^2/t}\frac{\xi(s+v)}8\,dv,\qquad s=(1+iz)/2.
\]
This is [Polymath v2 equation 35][poly], with no RH premise. It does not
extend any restricted approximation theorem by itself.

Fix observation strips and the required analytic and averaging buffers
before taking limits. Normalize approximation errors by a positive
carrier-amplitude envelope, not by H or a signed approximant that may
vanish. Later physical comparisons retain the same
\(q=\epsilon_g^2\), \(K=k_\ell k_h\), current, regulator terms and actual
signed covariance as the parent investigation. No convenient substitute
regulator, time average or mass normalization is introduced.

## 3. Established starting points and their limits

| Input | Existing result | Boundary to preserve |
| --- | --- | --- |
| [Parent Note30][n30], FS3--FS20 | Full implicit gamma-saddle field; envelope error \(C t^{3/2}/(1+X+t\log(2+t+X))^2\), for t>=32 and sufficiently large t+X. | Proved in-note; same-assistant review only. Onset/constants are not numerically instantiated. Higher-order accuracy is not established by this input. |
| [Parent Note31][n31] | Eventual large-t physical evolution/current/covariance comparison, uniformly over all real heights, with its stated \(O(t^{-1/2})\) allowances; separate compact-positive-time results. | Each derivative/observable retains its own rate, buffers and residual terms. No all-time assembly follows. |
| [Ansatz Note17][n17], AN01 r1 | First corrected full saddle; complete e4 budget, spatial0–3, direct first-time and exact residual, eventual all real heights. | Proved in-note from named inputs; same-model Assessment12 only. Symbolic sufficient onset; no new physical transfer or bridge. |
| [Ansatz Note18][n18], AN02 r1 | Second correction C4; complete e6 budget, finite constants, spatial0–3/time and exact residual, eventual all heights. | Proved in-note from named inputs; same-model Assessment13 only. Its earlier partial fixed-order status is superseded by Note19. |
| [Note19][n19], AN03 r1 | Arbitrary fixed J, indexed complete remainder and exact residual recurrence; spatial0–3/direct time. | Proved in-note from named inputs; same-model Assessment14. Fixed J before symbolic onset; no growing-order or convergence theorem. |
| [Note20][n20], AN04 r1 | Compact-positive arithmetic refinement, P4 X^-7 on[63,65], F1 extension and actual high-height overlap/time splice. | Proved in-note at high-height field scope; same-model Assessment15. Compact core and new physical/center consumers remain open. |
| [Parent Note28][n28] and [Note38][n38] | Regulator crossover near 64, its displaced center and finer rounding width; limitations of phase-transition analogies. | Regulator-dependent density behavior, not a singularity of H or a demonstrated saddle coalescence. |
| [Ansatz Note03][a03] | An earlier first corrected compact-positive carrier on [32,33]. | Different organization from the full implicit saddle. Note20 rechecks its chart on each fixed[32,T] and pays their field/one-arm comparison; physical consumers remain separate. |
| [Ansatz Note04][a04] and [Note06][a06] | Signed near-zero crossover and a paid weaker chartwise negative-time join. | Existing algebraic error, fixed chart cutoffs and actual residual remain; this is not the newer strong recurrence theorem through zero. |
| [Recurrence manuscript][recurrence] and [Note18][r18] | Negative-time hierarchy, controlled order growth, effective evaluation and uniform RS coefficient improvements. | The strongest stated outer-envelope theorem retains its negative-time slab. Its constants are not uniform toward zero merely by substitution. |

These are inherited results in their sources' status words, not new proofs
or independent validation in this program. The parent's finite
all-time/all-height evaluability results remain separate from a short
asymptotic description and its useful uniform error.

## 4. Organize the large-time hierarchy around the full saddle

Let
\[
\mathcal M(w)=\frac{w(w-1)}{16}\pi^{-w/2}\Gamma(w/2),\qquad
\alpha=(\log\mathcal M)'.
\]
For each of the two reflected arms, use the selected right-half-plane
branch
\[
p=w+\tfrac t2\alpha(p),\quad B=1-\tfrac t2\alpha'(p),\quad
\mathcal S_t(w)=\mathcal M(p)e^{-(p-w)^2/t}B^{-1/2}.
\]
The leading model is the sum of the two S arms. It already absorbs the
linear shift and quadratic curvature. Higher derivatives of log M supply
the remaining local fluctuations.

[Brainstorm03 P5--P9][discussion] gives a formal exponential-coefficient
recurrence, exact finite Gaussian moments, and the candidate first
correction
\[
C_2(t,w)=\frac{t^2\alpha'''(p)}{32B^2}
+\frac{5t^3(\alpha''(p))^2}{192B^3},\qquad
P_{*,2}=\sum_{w=s,1-s}\mathcal S_t(w)(1+C_2(t,w)).
\]
This candidate was validated in [Note17][n17] by the AN01 r1 execution.
Its complete field allowance is e4=t³/N⁵+t⁴/N⁶+t⁵/N⁷+t⁶/N⁸ after
explicit eventual arithmetic/contour absorption. The uniform field
rate is O(t^-2 log^-5 t), spatial order j<=3 has an additional log^j
loss, direct first-time is O(t^-2 log^-3 t), and the actual nonzero
residual is O(t^-3 log^-5 t). [Assessment12][r12] is same-model only. Standard simple-saddle expansions provide context
([DLMF 2.4(iv)][dlmf]); their general existence does not pay this source's
moving-parameter, contour or arithmetic errors.

The explicitly authorized AN02 continuation now closes one further fixed
order in [Note18][n18]: P4=sum S(1+C2+C4), with all five C4 monomials,
finite sectorial/Bell/Gaussian constants and complete e6=sum(k=1..6)
t^(k+3)/N^(k+6) allowance after eventual arithmetic/contour payment.
Uniform field is O(t^-3 log^-7 t), spatial j<=3 adds log^j, direct
first-time is O(t^-3 log^-5 t), and actual nonzero residual is
O(t^-4 log^-7 t). [Assessment13][r13] is same-model only. Onset remains
symbolic. This was the second worked order; the general theorem is now
proved in [Note19][n19]. For every fixed J>=0 it retains C0 through C2J,
with complete bJ=sum(k=1..2J+2)t^(J+1+k)/N^(2J+2+k) allowance,
indexed finite constants and exact residual -sum S Q C2J. Uniform
field is O_J(t^(-J-1)log^(-2J-3)t), spatial0–3 has log losses, direct
time adds log² and residual has an extra t^-1. A finite coefficient
identity proves the cancellation at every fixed order; no infinite
convergence or growing-order premise is used.

For each retained order distinguish:

- local saddle truncation, including justified parity cancellations;
- the full ordinary Dirichlet arithmetic, either retained or bounded;
- connectors, middle pieces, both infinite ends and other contour errors;
- buffered spatial derivatives, direct time derivatives and the actual
  nonzero heat residual of the moving-saddle model;
- growth of constants with order, before choosing any growing order.

The negative-time frozen models solve their heat equation exactly.
The moving-saddle truncations do not inherit that property.

## 5. Quantifiers and measurable gains at large time

Write
\[
X=|x|,\quad R=2+t+X,\quad \mathcal L=\log R,\quad
\mathcal N=1+X+t\mathcal L.
\]
The inherited coarse leading-field bound is \(O(t^{3/2}/\mathcal N^2)\),
hence \(O(1/(\sqrt t\log^2t))\) uniformly in real x on a fixed strip.
Note19's J=0 case now improves that bound by parity to
\(O(t^{-1}\log^{-3}t)\), with complete errors after its own onset.
The program distinguishes fixed x, all-x uniformity, and joint limits with
\[
X\ll t\log R,\qquad X\asymp t\log R,\qquad X\gg t\log R.
\]
These balances locate changes in useful asymptotic organization. They
are not by themselves physical phase transitions.

[AN01 r1][packet] now improves the **complete** field error with the
spatial0–3 and direct first-time bounds above on paid buffers. Note17
retains arithmetic and contour budgets before their explicit eventual
absorption. Reusing the old t>=32 arithmetic absorption at the new
X^-5 local scale would be unsupported; the sufficient larger onset is
specified symbolically, with no numerical or regulator64 conclusion.

Note19 states the attainable rate for every fixed finite order and its
parameter dependence, including these height regimes. An optional
order-growth study can now ask whether optimal truncation or stronger
than algebraic accuracy is justified. That study remains open;
convergence of the formal infinite series is not assumed.

As t decreases, omitted arithmetic can become the precision bottleneck.
Further gamma corrections must not be credited with an improvement
smaller than an unpaid arithmetic remainder. A later hierarchy may need
an independently chosen number of retained arithmetic modes.

## 6. Later bridges across the multiple regions

| Passage, in the intended order | What is already available | Required new bridge output |
| --- | --- | --- |
| Large t to bounded positive times reaching the neighborhood of64 | Note19 joint theorem and Note20 new compact proof; P4 pure X^-7 on[63,65], rechecked F1 chart and comparable envelopes | High-height overlap and optional time-splice defect are paid. A compact bounded-height core remains; no eventual onset was evaluated at64. |
| Across the regulated transition near 64 | Note28/31 baseline physical results; Note20 corrected field/arm inputs | Existing A03-AN01 r1 is next ready: exact named-center neighborhood/sensitivity and shifts. New physical/current/covariance and sharper layer consumers remain unpaid. |
| From that positive-time region toward small positive t | Parent t>=32 results, restricted published small-positive estimates, and prepared [A08-AN01][small] on [1/2,1] | A quantitatively covered chain through the remaining positive intervals, including the documented 1/2<t<32 gap in the desired buffered estimates. Each new slab must pay its complete arithmetic remainder. |
| Through t=0 into negative time | Signed \(\lvert t\rvert L\le8\) crossover, weaker negative join and prepared [R05-AN08][negative] approaching T=1/L | Compatible errors and derivatives on overlaps, full completion terms, and an explicit connection to the negative recurrence. The exact field is regular at zero; the representation and error scales change. |
| Assembled description on the covered union | The preceding separate models | A proved domain union, stated uncovered regions, and every cutoff/interface defect; no all-time claim from disconnected estimates. |

Near64 the existing regulator-defined center obeys
\[
t_c(X)-64=\frac{64}{\log X+c_0+O(1/\log X)},
\]
whereas the rounding width is \(O(1/(X\log X))\). The exact implicit
center is needed at that width. The fixed switch point 64 and this
density crossover belong to the chosen measurement protocol. H remains
smooth at finite height. A better saddle approximation may refine the
observable comparison without turning64 into an intrinsic zero threshold.

Near zero, arithmetic mode weights already suggest the joint variable
tL, with \(L=\log(X/(4\pi))\). This is motivation for retaining arithmetic,
not a universal critical value. The existing work window \(\lvert t\rvert
L\le8\) is a proved window under its own hypotheses, not a physical law.

Match models through the same exact H. On a genuine common domain,
compatible envelope bounds give a difference bound by the sum of errors.
Termwise equality of differently organized expansions is not required.
A time cutoff introduces its derivative times the model difference;
spatial cutoffs can break holomorphy and add further defects. Physical
transfer must retain regulator derivatives and actual covariance, not
replace them by products of averages.

## 7. Gates, scope and research discipline

The arbitrary-fixed-order gate is complete in Note19, with indexed
constants, full errors and a height-regime map. Note20 starts the next
stage with an actual compact-positive high-height field bridge through64.
The compact core and new physical-layer consumers remain open. Optional
optimal-order work is not required before the ready named-center task.
No t<32 slab, through-zero extension, refined physical layer or all-time
assembly is claimed as a new result.

This is an approximation program under [avoid01][a01], judged by
quantitative gains and newly covered domains. Read [results][results],
[heat-flow inputs][heat], [controls][controls] and [avoid][avoid],
especially [matching][matching], [scope][scope] and [review limits][review].
The control-premise screen is in [Brainstorm03 Section6][discussion]:
generic heat/recurrence/saddle structure excludes no collision control;
the application needs the unchanged complete canonical arithmetic and
source identity. No RH conclusion is inferred from shape properties.

**AN01–AN04 r1 CLOSED at their stated scopes**, same ansatz chat0005,
26 October2026, **gpt-6.1-sol, recorded effort ultra**; Notes17–20 and
same-model Assessments12–15. **LT-03 Complete at fixed order; LT-05 and
HDA-A04 Partial. Next owner: Analysis — Sol**, existing [A03-AN01 r1][center],
consume Note20 and finish exact named-center sensitivity/shifts. See
[whole-chat Summary21][summary] for the next prompt. No growing-order,
physical-tuple or through-zero execution has been performed. Numerical and machine-symbolic work stays
with Sol and requires a separate bounded question. Astra is reserved for a
specific resistant analytical mechanism, not the importance of the goal.
This planning document itself dispatches no chat, agent, model switch
or scheduled execution; the author explicitly authorized the fixed-order
theorem and starting regional work in ansatz chat0005. Preserve existing unique
chat registrations; the originating discussion stays in recurrence chat0007.

[n19]: ../notes/19_ARBITRARY_FIXED_POSITIVE_TIME_ORDER_20261026.md
[n20]: ../notes/20_COMPACT_POSITIVE_FIELD_BRIDGE_20261026.md
[summary]: ../notes/21_CHAT0005_RESEARCH_SUMMARY_AND_HANDOFF_20261026.md
[center]: ../research-progress/handoffs/HDA-A03-AN01.md
[n18]: ../notes/18_SECOND_CORRECTED_LARGE_POSITIVE_TIME_20261026.md
[r13]: ../reviews/13_SECOND_CORRECTED_LARGE_POSITIVE_TIME_ASSESSMENT_20261026.md
[n17]: ../notes/17_FIRST_CORRECTED_LARGE_POSITIVE_TIME_20261026.md
[r12]: ../reviews/12_FIRST_CORRECTED_LARGE_POSITIVE_TIME_ASSESSMENT_20261026.md
[progress]: ../research-progress/03_LARGE_POSITIVE_TIME_HIERARCHY_RESEARCH_PROGRESS_20261026.md
[umbrella]: 02_EVOLUTION_ASYMPTOTICS_RESEARCH_OVERVIEW_20261025.md
[packet]: ../research-progress/handoffs/HDA-A04-AN01.md
[small]: ../research-progress/handoffs/HDA-A08-AN01.md
[negative]: ../../recurrence/research-progress/handoffs/HDA-R05-AN08.md
[discussion]: ../../recurrence/brainstorm/03_POSITIVE_TIME_HIERARCHIES_AND_BRIDGES_20261026.md
[n30]: ../../notes/30_FULL_GAMMA_SADDLE_AND_INNER_OVERLAP_20261024.md
[n31]: ../../notes/31_POSITIVE_ALL_HEIGHT_EVOLUTION_AND_COVARIANCE_20261024.md
[n28]: ../../notes/28_JOINT_OUTER_REGULATOR_TRANSFER_AND_SWITCH_LAYER_20261024.md
[n38]: ../../notes/38_PHASE_TRANSITION_LITERATURE_AND_JOIN_DIAGNOSTICS_20261024.md
[a03]: ../notes/03_OUTER_CORRECTION_AND_SIGNED_REAL_BRIDGE_20261025.md
[a04]: ../notes/04_COMPLEX_STRIP_REMAINDER_AND_BUFFERED_CROSSOVER_20261025.md
[a06]: ../notes/06_NEGATIVE_BRIDGE_AND_TIME_JOIN_20261025.md
[recurrence]: ../../recurrence/manuscript/main.tex
[r18]: ../../recurrence/notes/18_UNIFORM_RS_BOUND_STRENGTHENING_20261026.md
[poly]: https://arxiv.org/html/1904.12438v2#S4
[dlmf]: https://dlmf.nist.gov/2.4#iv
[results]: ../../../../../result-summaries/README.md
[heat]: ../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../avoid/README.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[matching]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[scope]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[review]: ../../../../../avoid/05_same_model_reviews_and_shared_premises.md
