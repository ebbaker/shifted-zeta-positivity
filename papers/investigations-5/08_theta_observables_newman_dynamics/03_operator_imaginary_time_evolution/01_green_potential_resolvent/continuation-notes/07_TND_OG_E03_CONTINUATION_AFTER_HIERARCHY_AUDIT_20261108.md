# Next task: complete the signed-logarithm Green estimate

8 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. Actual model and reasoning effort
are not recorded in this chat's capture metadata.

**Default next task: [E] TND-OG-E03 r1 — recommended Sol6.1.** Prove the
complete finite-source, logarithmic-tail and prime-baseline acquisition
theorem in the existing fixed request. This note brings together the
manuscript milestone and the subsequent hierarchy audit. It prepares the
next session; **E03 remains ready and unactivated**.

| Next task | Type | Recommended model | Readiness and dependency | Expected output |
| --- | --- | --- | --- | --- |
| **TND-OG-E03 r1 — default** | E — execution | Sol6.1; field, route, constants and success test are fixed | Ready; [Request09](../research-progress/handoffs/09_TND_OG_E03_SIGNED_LOG_ACQUISITION_REQUEST_20261108.md), [inputs09](../research-progress/handoffs/09_TND_OG_E03_INPUTS_20261108.json) and B02 Note04 | Complete acquisition theorem with explicit vanishing error, proof-author check, return and continuation |
| B02 r2 — conditional only | B — conceptual clarification | Astra; only if a consequential fixed premise fails | Not triggered; requires an exact failed E03 clause | Resolve that failure without silently replacing the source or observable |

The [sole register](../research-progress/01_TND_OG_GREEN_RESOLVENT_RESEARCH_PROGRESS_20261107.md)
owns live status. The author chooses the actual model, effort and when to
continue. This is the current entry point after
[Continuation05](05_TND_OG_B02_RESULTS_AND_MODEL_CHANGE_20261108.md) and
[Continuation06](06_TND_OG_E04_MANUSCRIPT_AND_OUTSTANDING_TASKS_20261108.md);
Request09 r1 remains the authoritative mathematical contract.

## 1. Read in this order

1. Repository AGENTS.md, GPT_RESEARCH_MODEL_WORKFLOW.md, LARGE_FILES.md,
   REFERENCE_WORKFLOW.md and tools/CHAT_HISTORY.md. Read the
   [result index](../../../../../../result-summaries/README.md), especially
   [heat-flow cluster11](../../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md)
   and [controls12](../../../../../../result-summaries/12_collision_controls_and_screening.md),
   and the [patterns index](../../../../../../avoid/README.md), especially
   [target01](../../../../../../avoid/01_restating_the_target.md),
   [control02](../../../../../../avoid/02_shape_only_arguments_and_the_controls.md),
   [shared-premise05](../../../../../../avoid/05_same_model_reviews_and_shared_premises.md),
   [scope07](../../../../../../avoid/07_scoped_exclusions_read_as_universal.md)
   and [coupled payments12](../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md).
2. The sole register, Request09 and its input manifest. Verify actual
   input versions before beginning; preserve the frozen files.
3. [B02 Note04](../notes/04_TND_OG_B02_ONE_SIDED_BOUNDARY_LOG_ACQUISITION_20261108.md),
   especially (3)–(18), its
   [self-check02](../reviews/02_TND_OG_B02_BOUNDARY_LOG_SELF_CHECK_20261108.md)
   and [source-use04](../references/04_TND_OG_B02_SIGNED_LOG_SOURCE_USE_20261108.md).
   Follow Request09 to [OG Note02](../notes/02_TND_OG_E01_SHORT_MOLLIFIER_RESIDUAL_FLOOR_20261107.md)
   (22) for the literal source approximation and complete error.
   Carry the [E02 correction](../notes/03_TND_OG_E02_REAL_MIXED_TERM_AND_ACQUISITION_CLARIFICATIONS_20261107.md)
   wherever the older obstruction is discussed.
4. For current context, read [overview §7](../research-overview/01_TND_OG_GREEN_RESOLVENT_RESEARCH_OVERVIEW_20261107.md),
   [B03 Note05](../notes/05_TND_OG_B03_HDA_HIERARCHY_LOG_TRANSFER_20261108.md)
   and its [self-check04](../reviews/04_TND_OG_B03_HIERARCHY_TRANSFER_SELF_CHECK_20261108.md).
   The [manuscript](../manuscript/README.md) supplies a coherent background
   development; use the linked original proof sources for execution.

The inherited conditioning and short-mollifier obstructions retain E02's
accepted-with-additive-correction status. B02 and the new B03 composition
have proof-author checking only. No complete E03 assembly or favorable
canonical signed value has yet been acquired.

## 2. The precise result to prove

Keep Newman time zero and the canonical field
\[
 s=\frac{1-iz}{2},\qquad
 F(z)=\frac{s-1}{s}\zeta(s)=D_0(z)H_0(z),\qquad
 D_0(z)=\frac{16\pi^{s/2}}{s^2\Gamma(s/2)}.
\]
With \(K(u)=1/[16\cosh(\pi u/8)]\), retain the inherited identity
\[
 J_0^{\rm G}(X)
 =\int_{\mathbb R}K(x-X)\log|F(x)|\,dx-P(X)+G(X,1).
\]
The prime baseline \(P_Q\), its tail
\(\beta_Q=2Q^{-3/2}/3\), the compact envelope
\(\mathcal I_{X,R,\delta}\), the exact-log tail
\(\mathcal T(X,R)\), and the local-error sum
\(\mathcal E_{X,R}(\delta)\) are defined in Request09 (E1)–(E8).

Prove, with all constants and domains paid,
\[
 U_{R,Q,\delta}(X)
 =\mathcal I_{X,R,\delta}
   +\mathcal T(X,R)-P_Q(X)+\beta_Q+G(X,1),
\]
\[
 \boxed{
 0\le U_{R,Q,\delta}(X)-J_0^{\rm G}(X)
 \le\mathcal E_{X,R}(\delta)+2\mathcal T(X,R)+2\beta_Q.
 }
\]

This is an **acquisition theorem**: an accurate upper approximation to
the actual signed Green value. The separate inequality
\[
 \overline U<m(d,r),\qquad
 m(d,r)=\frac{\sin(\pi/8)d}{\cosh(\pi r/8)},
\]
is an unpaid value condition. Smaller approximation errors do not
establish it.

## 3. Execute the fixed proof in five steps

1. **Local logarithm and remote tail.** Audit Note04 on unit real
   intervals, including multiplicities, its safe anchor and its
   height-dependent exponent. Derive Request09 (E2)–(E3) for the
   complete exact logarithm. Preserve the height factor in joint limits.
2. **Compact envelope and source error.** Sum the local one-sided
   bounds with the actual kernel weights. Use the even reflected
   finite theta source with its arithmetic and radial errors,
   Request09 (E5)–(E6). Its gamma multiplier is a compact bound.
   Retain the signed logarithmic integral and include any additional
   field-evaluation error in delta.
3. **Prime baseline and final signs.** Check the integer prime cutoff,
   the single plus pole term, and the two factors of two in the
   completion inequality. Do not add a second correction for q(s).
4. **Finite choices and evaluation allowance.** For each prescribed
   X and h>0, choose R with T≤h/6, Q with beta≤h/6, delta with
   E≤h/3, then source cutoffs meeting the field allowance. Explain
   how a future directed evaluated upper value pays finite prime,
   G, field, integration and arithmetic errors. A prescribed sequence
   of heights or margins permits repeated finite choices; it is not
   a useful uniform cost bound or an all-center value theorem.
5. **Controls and scope.** Recheck Request09's named obstruction and
   collision controls using Note04's premise table. State the class
   of each exclusion and the canonical premise each control lacks.
   A generic defective field must retain its positive Green response;
   do not assign it the canonical prime baseline or anchor without
   those hypotheses.

No numerical experiment is needed for this analytical completion.

## 4. What the hierarchy audit changes

B03 identifies a useful alternative input. HDA's real time-zero
Riemann–Siegel completion has exact gamma normalization
\(\lvert D_0M\rvert=1\) on the real line. Its growing completion order
\(K_{\rm RS}=O(\log\log X)\), composed with B02, gives a local unit-interval
one-sided logarithmic error \(O((\log X)^{-2})\). This is the consequence
derived in Note05, with same-assistant checking only.

It uses real initial data directly, without extending the strong
negative-time recurrence through zero. The arithmetic population
still has O(sqrt X) modes; finite evaluation, coefficient costs and
a practical onset remain unpaid. The separate mean/fluctuation equation
does not provide a covariance sign or a closed canonical Green bound.

This connection is **context for E03, not a revision of its source
contract**. Request09 fixes the literal Fourier/theta approximation.
Complete that assembly using its specified input. An RS-based alternative
or comparison requires its own declared task and full error obligations;
it is not activated here. Keep the provider-independent logarithmic
steps identifiable for that later comparison.

## 5. Deliverables and stopping rule

Write one analytical proof note, one proof-author check in reviews, an
exact return in research-progress/handoffs, necessary source-use updates,
the sole register disposition and a continuation/model-change note.
Record actual metadata when available and preserve each imported input's
evidence level. Save conceptual session notes in brainstorm/notes.

One bounded correction cycle for constants, signs, ordinary domain
estimates or conservative allocations is allowed, recorded additively.
A failed local line estimate, indispensable new arithmetic smallness
hypothesis, or necessary source/observable change triggers **B02 r2**
at the exact failed clause. Stop that dependency and report it.
An unfavorable value is not such a failure: E03 promises accurate
acquisition, with no promise of favorable smallness.

Stop at the complete theorem, its precise failed clause, or exhaustion
of the one correction cycle. Work in the Green branch. Preserve parent
and sibling research, the current manuscript, frozen inputs and shared
result summaries. A later claim-level assessment can be specified after
completion; this note does not issue it or authorize further research.

## 6. Input integrity and conversation record

The preparation check on 8 November found **33 of the 34 E03 manifest
entries matching**. The sole difference is tools/CHAT_HISTORY.md:
20,937 bytes, SHA-256
62e4c8323ce51c9d2a74b690594f99f609ae201141ec85fa86b9ed3e3a623e83.
This is the same pre-existing shared-guide change recorded in the
[E04 build record](../numerics/01_TND_OG_E04_MANUSCRIPT_BUILD_20261108.json)
and [B03 return10](../research-progress/handoffs/10_TND_OG_B03_HIERARCHY_RELATIONSHIP_RETURN_20261108.json).
The mathematical inputs match. Recheck at execution; record any new
difference rather than rewriting the manifest or silently accepting it.

This session is branch chat0002, thread
01a1b9b7-8624-7e51-9f9b-ba8e5a87a938, titled
“Summarize Green resolvent research”. Its earlier public text and final
reply were successfully refreshed at the start of this turn.
Use the [history guide](../chat-histories/README.md) and current locked
recorder. A new conversation must use its own actual thread ID, title
and source. Preserve registration and provenance, and arrange the
exact-turn final capture under tools/CHAT_HISTORY.md.

## 7. Pasteable continuation prompt

> Work in /Users/ebbaker/Documents/shifted-zeta-positivity. Read AGENTS.md,
> GPT_RESEARCH_MODEL_WORKFLOW.md, LARGE_FILES.md, REFERENCE_WORKFLOW.md,
> tools/CHAT_HISTORY.md, and the result-summaries and avoid indexes.
> In papers/investigations-5/08_theta_observables_newman_dynamics/
> 03_operator_imaginary_time_evolution/01_green_potential_resolvent,
> read Continuation07, the sole progress register, frozen E03
> Request09/inputs09, B02 Note04 with its check and source-use record,
> and B03 Note05 with its check.
>
> Begin [E] TND-OG-E03 r1 — recommended Sol6.1, at my selected effort.
> Verify the inputs, recording the known chat-guide difference separately,
> and execute the fixed analytical signed-logarithm assembly. Prove the
> explicit compact-envelope, exact-log-tail and prime-baseline inequality,
> with finite parameter choices and honest evaluation allowances. Retain
> the literal Fourier/theta source specified in Request09; the new RS
> hierarchy is context, not authorization to replace that source.
>
> Preserve the distinction between vanishing acquisition error and a
> favorable canonical signed Green value. Allow only the request's one
> bounded correction cycle; report any consequential failure at its exact
> clause. Save the proof, check, return, brainstorm notes and continuation
> in the branch, maintain the sole register, and capture this actual chat
> through the locked recorder. Stop at the theorem or its precise failed
> dependency. Do not begin numerics, manuscript integration, sibling edits,
> or a new mechanism.
