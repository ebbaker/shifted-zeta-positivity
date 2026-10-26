# Analysis continuation: three rounds for the recurrence hierarchy

26 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), recorded effort max**.
Ansatz chat0004, thread 01a1765a-5c4e-7dd1-9de8-d70dd1725e34.

**Continuation r1 — prepared, not executed. Next owner: Analysis — Sol.**
This note is designed for several successive rounds, in one chat or
across continuations. The [progress register][progress] owns live status.
Use its latest dispositions, not an earlier prompt's stale next item.
The mathematical common contract below is frozen for the three linked
r1 requests; append a revision before changing that contract.

## Read first

Read repository AGENTS.md, GPT_RESEARCH_MODEL_WORKFLOW.md,
LARGE_FILES.md, REFERENCE_WORKFLOW.md and tools/CHAT_HISTORY.md.
Then read the [overview][overview], [brainstorm][brainstorm], and
ansatz [Note16][note16] for the recurrence. Reuse [Note05][note05],
[Note06][note06], [Note10][note10] and [Note12][note12], with their
linked assessments, for the real initial-value heat identity,
classical RS remainder, all-mode estimates, complex buffers and tails.
The [input manifest][manifest] identifies the planning versions.
Recheck them at execution and record differences.

The original [AN07 request][oldpacket] is historical: the active first
round is now [HDA-R01-AN01 r1][packet1], with outputs in this branch.
Do not execute or register the same comparison twice.

## Common mathematical contract

Keep \(h(T,z)=H(-T,z)\), \(h_T=h_{zz}\), the full canonical theta
source and \(H(0,z)=\xi((1+iz)/2)/8\). Work on
\[
\Omega_X(r,b)=\{|\Re z-X|\le r,\ |\Im z|\le b\},
\qquad r,b>0,
\]
with an extra unit of analytic margin. The physical buffer choice is
\(r=\ell+2,\ b=1+h_{\rm av}+2\), where \(h_{\rm av}\) denotes the
parent's averaging height. Freeze the real center \(X\), all cutoffs,
window endpoints, gamma derivatives and coefficient data under spatial
and time differentiation. Use the reflected left chart only through
the canonical symmetry; \(|\Re z|\) is not a holomorphic coordinate.

Use Note16's \(U_{\epsilon,j}\), \(\mathcal Q_T\) and
\(\mathcal D_{\epsilon,r}\), including both arms and all
\(n\le N=\lfloor\sqrt{X/(4\pi)}\rfloor\). With \(L=\log(X/(4\pi))\),
take \(V=8\sqrt2 L\) for rounds 1–2; it is a fixed enlargement of the
existing slab window and its estimates must be checked. In round 3
use \(V_B=8\sqrt{\max(1,B)}L\).

Retain
\[
\mathcal I_{X,K}(T,z)=\frac1{\sqrt{4\pi T}}
\int_{X-V}^{X+V}e^{-(z-u)^2/(4T)}Q_{X,K}(u)\,du,
\]
where \(Q_{X,K}=S_{m(u)}-S_N+R_{m(u),K}\), with the classical real
RS coefficients through \(K\) and exact adjacent-cutoff transfer.
The real partitions are fixed in \(z,T\). Do not analytically
differentiate real RS coefficient functions or move the real-part
operation outside the complex-kernel integral.

Define \(F^{[p,K]}=\mathcal I_{X,K}+\sum_{\epsilon,j\le p}U_{\epsilon,j}\)
and \(E=h-F^{[p,K]}\). The requested norm is
\[
\|E\|^{(3,1)}_{X;\tau,B}
=\sup_{\substack{T\in[\tau,B]\\z\in\Omega_X(r,b)}}
\frac{\displaystyle\max_{0\le a\le3}|\partial_z^a E(T,z)|
      +|\partial_T E(T,z)|}{|G(z)|},
\]
where \(G(z)=[M((1+iz)/2)M((1-iz)/2)]^{1/2}\), positive at real \(X\).
State separate derivative constants if useful. Identify the actual
residual \((\partial_T-\partial_z^2)F\) and its first spatial derivative.
Both should vanish for the frozen construction; verify this rather than
using it as a substitute for the error comparison.

Pay canonical initial RS mismatch, the local weighted-order remainder,
the entire arithmetic population, true initial-data tails, artificial
polynomial/exponential tails, complex-kernel factors and all derivative
costs. Give sufficient height-onset conditions. Establish the first-time
bound from differentiated identities or kernels, never by differentiating
an already stated \(O(\cdot)\) allowance. Reconcile the curvature term
with the target-centered Note10 formula, whose differentiated residual
is different.

## Round 1 — first genuine finite-level comparison

Execute [HDA-R01-AN01 r1][packet1]. On \(1\le T\le2\), use \(p=2\),
\(K=4\). Validate the explicit \(U_1,U_2\) and derive a local
weighted-order remainder that survives heat integration and the full
mode sum. Try the prospective \(X^{-11/4}\) natural-scale rate, but
report the strongest rate actually proved.

Deliver one bounded comparison with its complete error table, or the
first precise estimate that the chosen method cannot pay. Save the
proof/attempt and an internal assessment before activating round 2.
The acceptance question is whether this grading gives controlled
accuracy, not whether its algebra can be repeated.

## Round 2 — arbitrary fixed order and matched completion

Execute [HDA-R02-AN01 r1][packet2] if round 1 supports the mechanism.
For each fixed \(p\ge1\), derive a finite combinatorial coefficient
description, a weighted Taylor remainder, a sufficient \(K(p)\), and
the actual exponent \(\sigma(p)\) in
\[
\|E^{[p,K(p)]}\|^{(3,1)}_{X;1,2}
\le C_{p,r,b}X^{-\sigma(p)}
\]
or its justified version with stated extra factors. Test \(K=2p\) and
\(\sigma(p)=p+3/4\) as candidates, not inherited facts. Retain explicit
majorants for order-dependent constants and sufficient onsets.

This is a theorem with \(p\) fixed before \(X\to\infty\). It is not an
infinite-series or growing-\(p\) theorem. If the generalization fails,
preserve the strongest finite-order result and identify which
order-dependent estimate failed. Do not bury that failure in a newly
named coefficient.

## Round 3 — compact time and endpoint dependence

Execute [HDA-R03-AN01 r1][packet3] using the accepted fixed-order
result. For declared \(0<\tau\le T\le B<\infty\), give a
parameterized error estimate and sufficient onset ledger. Track the
complex-kernel exponential, inverse-time factors, shifted moments,
all-mode damping and both tails explicitly.

If round 2 is unresolved but round 1 is sound, this request permits a
\(p=2\)-only compact-family theorem; label that fallback and leave
the general-order objective open. No uniformity as \(\tau\to0\),
\(B\to\infty\), or \(p\to\infty\) is asserted without a separate proof.
End with a short table of what is proved, which constants deteriorate,
and the first missing input for a joint limit or continuous-\(s\) estimate.

## Recording, stopping and subsequent choices

Each round has its own frozen request, return and disposition. After a
successful assessment, the next dependency-ready round can proceed
without another planning exercise within this continuation's scope.
A precise failure stops work that relies on it; routine repairs within
the same question are allowed and must be recorded. Escalate to Astra
only a specified resistant analytical bottleneck, with the attempted
estimate and evidence.

Use notes/02,03,04 for the respective mathematical returns, reviews/01,02,03
for internal assessments, and small nonnumerical provenance/work records
in numerics/. Include dates, actual models/efforts, input versions and
limits. Update the live register and each packet; retain original requests.
No numerical or machine-symbolic campaign, source change, manuscript
integration, positive-time extension or physical transfer is included.

The geometric and physical analogies remain in the overview and
brainstorm. After these three rounds, decide whether continuous
fluctuation strength, controlled order growth or a cancellation-preserving
grouping is a concrete next question. The prepared positive-time A08
task also remains available in the broader ansatz queue. Do not start
a fourth research direction automatically.

Read the [result index][results], [heat-flow cluster][heat],
[controls12][controls] and [avoid index][avoid], especially
[reformulations][a01], [shared premises][a02],
[scoped conclusions][a07] and [separate bounds][a12].
The control-premise screen is in the overview: these exact identities
are shared by suitable noncanonical sources, while the named controls
fail the complete canonical arithmetic/completion premise. No RH,
collision-exclusion or physical-transfer conclusion follows here.

The current chat remains uniquely registered as ansatz chat0004.
Refresh it at the start and end of replies, with bounded actual-final
capture, under the repository workflow. A genuinely new continuation
chat belongs in recurrence/chat-histories and keeps its own identity.

## Pasteable continuation

> Continue the recurrence investigation under its current overview and
> progress register. Execute HDA-R01-AN01 r1, then HDA-R02-AN01 r1 and
> HDA-R03-AN01 r1 in dependency order, following this continuation note.
> After each round save the mathematical return, an internal assessment
> and the updated disposition before proceeding. Keep all arithmetic
> modes, the bounded RS completion, full buffers and actual error costs.
> Treat proposed rates as targets, preserve failed estimates, and stop
> dependent work at a precise unpaid step. No manuscript or numerical
> campaign is included. Record actual model/effort and refresh chat history.

[progress]: ../research-progress/01_RECURRENCE_RESEARCH_PROGRESS_20261026.md
[overview]: ../research-overview/01_RECURRENCE_RESEARCH_OVERVIEW_20261026.md
[brainstorm]: ../brainstorm/01_RECURRENCE_AND_GENERALIZED_TRANSFORM_HIERARCHIES_20261026.md
[manifest]: 01_ANALYSIS_CONTINUATION_INPUTS_20261026.json
[note16]: ../../ansatz/notes/16_GAUSSIAN_FLUCTUATION_HIERARCHY_20261026.md
[note05]: ../../ansatz/notes/05_FIXED_NEGATIVE_TIME_REPRESENTATIONS_20261025.md
[note06]: ../../ansatz/notes/06_NEGATIVE_BRIDGE_AND_TIME_JOIN_20261025.md
[note10]: ../../ansatz/notes/10_FIRST_NEGATIVE_TIME_EVOLUTION_CORRECTION_20261025.md
[note12]: ../../ansatz/notes/12_COMPACT_NEGATIVE_TIME_FAMILY_20261025.md
[oldpacket]: ../../ansatz/research-progress/handoffs/HDA-A02-AN07.md
[packet1]: ../research-progress/handoffs/HDA-R01-AN01.md
[packet2]: ../research-progress/handoffs/HDA-R02-AN01.md
[packet3]: ../research-progress/handoffs/HDA-R03-AN01.md
[results]: ../../../../../result-summaries/README.md
[heat]: ../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../avoid/README.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
