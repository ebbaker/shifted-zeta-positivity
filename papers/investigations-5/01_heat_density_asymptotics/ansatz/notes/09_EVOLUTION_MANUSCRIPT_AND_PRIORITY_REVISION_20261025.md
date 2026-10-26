# Evolution-first manuscript integration and priority revision

25 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), recorded effort max**.
Ansatz chat0002, thread `01a17600-b15f-7f52-8713-31fa13599341`.

**Status:** manuscript synthesis and research-plan revision, with exact
algebraic identities. No new asymptotic estimate, propagated-error theorem,
physical-transfer result or independent mathematical assessment. The
[input manifest](09_EVOLUTION_REWRITE_INPUTS_20261025.json) records source
identities. This note records the author's requested rewrite; it does not
execute the next analytical packet.

## Author's direction and implementation

The author asks to prioritize understanding and bounding the asymptotic
estimates for all times, especially large height, through the evolution
equations acting on ansatze and their errors. The t=64 regulator behavior
remains important supporting work.

The maintained [manuscript](../manuscript/main.tex) has been rewritten
around that objective. The title, abstract, opening discussion, negative-
and positive-time interpretation, coverage map and continuation priorities
now follow the error-evolution approach. The previous bounded theorem
statements remain attached to their original sources and domains. The
new [Overview02](../research-overview/02_EVOLUTION_ASYMPTOTICS_RESEARCH_OVERVIEW_20261025.md)
and [Progress02](../research-progress/02_EVOLUTION_ASYMPTOTICS_RESEARCH_PROGRESS_20261025.md)
are authoritative for current planning; the earlier pair has a dated
supersession notice and remains historical.

The rewrite adds no accepted asymptotic bound. It makes the next missing
estimates and their relation to the evolution equations explicit.

## Mathematical integration

| Manuscript component | Source and status | What remains to prove |
| --- | --- | --- |
| Error equation and original-time correction hierarchy | H_t=-H_zz and product rule; Note08 EV1/EV6 with explicit time-sign conversion. Exact identities. | Initial comparison and a solution-error estimate in the claimed norm. |
| Negative-time Duhamel formula | Note08 EV2--3; inspected Stanford handout Section2.7. Standard whole-line identity under declared function-class assumptions. | Carrier-relative stability, tails, complex buffers and chart localization. |
| Amplitude and unwrapped phase equations | Note08 EV4--6. Exact for nonvanishing complex arms. | A controlled expansion with canonical initial matching, including all modes and the RS correction. |
| Negative-time damped arithmetic sum | Note08 EV7--9, algebraic rewriting of Notes03--05. | No validity-domain enlargement, dominance claim or error improvement follows from the rewriting. |
| Observable residual forcing | Parent Note31 PE33--39 and Note34 CJ25--26; Note08 EV10--12. Exact holomorphic-model identities. | New uniform transfer estimates for the ansatze; nonholomorphic spatial joins also need Note42 defects. |
| Bounded estimates | Notes03--06 and Assessments02--05. Proved in-note from named inputs, same-model internal assessment only. | Wider domains, sharper short formulas, physical transfer, useful cost and independent review. |

One elementary identity is displayed more explicitly than in Note08.
For T=-t, e_T-e_xx=-d, a positive smooth real-line weight A and v=e/A,
the product rule gives

\[
v_T-v_{xx}-2(A_x/A)v_x+((A_T-A_{xx})/A)v=-d/A.
\]

It exposes the drift and zeroth-order terms a weighted stability proof
must control. It is not a weighted contraction estimate, and no global
positive extension of a chart envelope is presumed. Spatial localization
adds -2 chi' e_x-chi''e. The manuscript states the function-class and
time-direction limits of the unweighted Duhamel estimate.

For the negative-time modal rewriting, exp(T lambda_n²) with
lambda_n=-pi/8+i k_n gives exp(pi²T/64) exp(-T k_n²)
exp(-i pi T k_n/4). The manuscript distinguishes fixed-mode absolute
damping on T log²X from relative fixed-mode weighting on T logX, and
retains the growing near-cutoff population. A component-weight bound is
not a leading asymptotic or lower bound for the signed canonical field.

For observables, q and K are physical and unchanged. The residual
forcing Xi_F=2 Re(conj(F) r_F)/(abs(F)²+q) is kept in the potential
equation and its Laplacian in the density equation; the current defect
also uses (r_F)_z. The actual covariance is not defined from a desired
evolution law. When q depends only on time, its spatial curvature is
zero but its time forcing remains. The identity does not pay the
regulator denominators or near-zero transfer constants.

## Priorities and ownership

HDA-A02-AN03 r1 is now the primary next bounded packet, **Analysis — Sol**,
prepared and not dispatched. It seeks one explicit correction and a
named o(|G|X^-3/4) field/jet/time allowance on 1<=T<=2, with the actual
residual and an honest outer-scale conversion. Its frozen scope is
unchanged. A02 remains Partial.

The new A08 ledger entry assigns the already documented compact-positive
gap 1/2<t<32 and uniform positive-time joins. A04/A05 retain joint
positive/negative limits as primary field-asymptotic tasks. A06 owns
physical transfer and assembly. A03-AN01 remains a prepared packet on
63<=t<=65, now deferred supporting; no regulator result is withdrawn or
promoted. Gaussian-polynomial and optional Lambert-W simplifications
remain secondary. All three all-time meanings are explicit in Overview02.

Historical frozen requests and returns are preserved. Live navigation
and dated priority notices are updated without silently changing their
mathematical contracts. Parent HDA-17 Partial, HDA-18 Gated and HDA-20
unfulfilled remain unchanged. No new chat, dispatch, numerical campaign,
model change, commit or snapshot folder is part of this rewrite.

## Verification, limits and continuation

[Assessment06](../reviews/06_EVOLUTION_MANUSCRIPT_REWRITE_ASSESSMENT_20261025.md)
records editorial/mathematical consistency checks at synthesis scope.
The [build record](../manuscript/BUILD_RECORD_20261025_EVOLUTION_REWRITE.json)
records compilation and rendered-page inspection. Neither is independent
validation of Notes03--06. The
[history verification](../chat-histories/VERIFICATION_20261025_EVOLUTION_REWRITE.json)
checks both unique ansatz registrations against their current public
sources, with stored and canonical hashes and original identity intact.
It is a pre-final snapshot; the exact-turn follow-up captures the real
final reply after completion.

This is an approximation program, not an RH criterion. Read the
[result index](../../../../../result-summaries/README.md),
[cluster11](../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md)
and [controls12](../../../../../result-summaries/12_collision_controls_and_screening.md),
and the [avoid index](../../../../../avoid/README.md), especially
[shared premises02](../../../../../avoid/02_shape_only_arguments_and_the_controls.md),
[scoped exclusions07](../../../../../avoid/07_scoped_exclusions_read_as_universal.md),
[separate bounds12](../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md)
and [status discipline19](../../../../../avoid/19_status_files_that_lag_the_findings.md).
Overview02 and the manuscript retain explicit control screening: the
heat identities exclude none, and the canonical arithmetic input is a
premise difference rather than a noncollision argument.

Next: **Analysis — Sol**, [HDA-A02-AN03 r1](../research-progress/handoffs/HDA-A02-AN03.md).
Use the pasteable bounded prompt in Progress02; no automatic execution.
