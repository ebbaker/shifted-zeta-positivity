# Sol continuation for J-E01 r1

1 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual authoring model **gpt-6-astra (Codex)**,
reasoning effort **max**. The executing assistant must record its own
actual model and effort.

**Next: [E] J-E01 — Sol.** Audit the selected coefficient-determinant
representation and test the proposed source signs at the origin and in
the tail. The mathematical request remains **r1 in
[Note01, Section 7][request]**. This continuation supplies a reading order
and execution checklist; it does not revise or enlarge that request.

| Task | Type | Recommended model and reason | Readiness at preparation | Expected output |
| --- | --- | --- | --- | --- |
| **J-E01 r1** | E — execution | Sol; the formulas, method and finite limits are specified | Ready; not started | One derivation/feasibility return, with exact algebra and any small execution record |
| J-B02 | B — brainstorm | Astra; the global sign mechanism remains unresolved | Depends on a supportive J-E01 return | A strategy for the remaining global source estimate |
| Return to J-B01 | B — brainstorm | Astra; a different mechanism would need selection | Only if the fixed mechanism fails or needs changing | A scoped failure and a revised choice |

The [Jensen progress register][progress] is the sole live status source.
Reread it before starting; preparation of this note leaves J-E01 unstarted.

## 1. Start here and retain the input versions

Work in
`/Users/ebbaker/Documents/shifted-zeta-positivity`, investigation
`papers/investigations-5/07_positive_theta_primitives/01_jensen`.

Read in this order:

1. Repository [AGENTS.md][agents], [model workflow][workflow],
   [large-file policy][large] and [chat-history workflow][chat].
2. The [live register][progress], then [Note01][decision], particularly
   Sections 1–5 and the frozen request in Section 7.
3. Shared [Note02 on differential closure][closure], especially the
   canonical state, derivative recurrence, moment normalization and
   boundary-preserving integration by parts.
4. Shared [Note03 on formulations][formulations], especially the
   distinction between source shape and coefficient signs. Use the
   [reference catalog][catalog] and Note01 Section 8 for the precise
   primary passages needed by the audit; preserve their inspection limits.
5. The [result index][results] and [avoid index][avoid], particularly
   [theta identities][theta], [controls][controls],
   [normalization][normalization], [joint estimates][joint],
   [scoped exclusions][scopes] and [unchecked imports][imports].

The request-bearing Note01 has SHA-256
`a2097d5952d1767781a6a0917f2acfd98b64d21f9a393755d62686863aae1717`.
Repository HEAD at preparation is
`c97b376dcbf81f05ea3a4f7d360da168af4a1345`; the research inputs include
uncommitted files. Note01 Section 7 records the earlier input hashes.
Its overview hash is explicitly **before a navigation update**, not a
requirement to restore that older overview. Record the actual input
versions. If a mathematical input or request changed, reconcile it before
dependent work; do not reset files or silently substitute another request.

## 2. Fixed objects and unresolved question

Use the complete canonical theta source at physical heat time zero, with
\[
b_n=\int_0^\infty u^{2n}\Phi(u)\,du,\qquad
c_n=\frac{b_n}{(2n)!},\qquad\gamma_n=n!c_n,
\qquad c_n=0\quad(n<0).
\]
The selected family is
\[
D_{r,k}=\det[c_{k+j-i}]_{i,j=0}^{r-1},\qquad r\ge1,\ k\ge0.
\]
Note01 derives the representation to audit:
\[
D_{r,k}=\frac{1}{\prod_{j=0}^{r-1}(2k+2j)!}
\int_{0<u_1<\cdots<u_r}
\Big(\prod_j u_j^{2k}\Big)
\prod_{a<b}(u_b^2-u_a^2)
\det[\Phi^{(2i)}(u_j)]_{{i=0,\ldots,r-1}\atop{j=1,\ldots,r}}
\,d\mathbf u.
\]
For the **order-three pilot**, define
\[
R=\frac{\Phi''}{\Phi},\qquad
T=\frac{\Phi^{(4)}}{\Phi},\qquad C=R'T''-T'R''.
\]
The proposed sufficient source conditions are \(R'>0\) and \(C\ge0\)
for \(u>0\): they make \(T\) a convex function of the increasing
coordinate \(R\). These signs are **not established for theta**.
J-E01 audits the implication and performs the two bounded feasibility
tests; a global proof is a later conceptual task. Order-three coefficient
positivity itself is already in the recorded classical baseline, so the
pilot's purpose is to assess this transfer mechanism.

## 3. Execute the four checks in r1

1. **Integral and endpoints.** Verify repeated integration by parts and
   determinant composition for all finite \(r,k\) in the stated domain.
   In
   \(\int_0^\infty u^{2m}\Phi^{(2i)}(u)/(2m)!\,du\), handle \(m<i\)
   through the endpoint \(-\Phi^{(2i-2m-1)}(0)=0\), not a negative
   factorial. Retain convergence and the ordered-chamber constant.
   Check \(D_{r,0}=c_0^r\).
2. **Classical normalization.** Reproduce Note01 (13) from the
   Csordas–Varga specialization \(f=1,\lambda=0\), including \(k=1\)
   and the moment factor \((2k-1)/(2k+1)\). Keep \(b,c,\gamma\)
   distinct. This is the required classical check, not a new estimate.
3. **Exact derivative algebra.** Audit the convex-graph lemma and
   the Jacobi reconstruction. Generate only \(Q_0,\ldots,Q_8\), as
   needed, and obtain complete signed expressions for \(R'\) and \(C\)
   with denominators known positive on the canonical orbit. Form the
   mixed expression before bounding its parts.
4. **Origin and tail.** For \(x=u^2\), use
   \(\widehat R(x)=R(\sqrt x)\), \(\widehat T(x)=T(\sqrt x)\), so
   \[
   R'=2u\widehat R',\qquad
   C=8u^3(\widehat R'\widehat T''-\widehat T'\widehat R'').
   \]
   Compute the leading regularized endpoint values/terms from the
   canonical initial data, using at most the eighth source derivative.
   Separately obtain the leading tail signs from the first theta summand
   with a justified differentiated remainder. Report positive, negative
   or unresolved outcomes for both required source signs at both ends.

## 4. Limits and stopping rules

Exact rational/polynomial algebra, Taylor expansions and equivalent
variables preserving the stated quantities are permitted. The sole
optional numerical acquisition is one outward-rounded enclosure of the
endpoint theta constant at 128 bits, with one refinement to 256 bits.
Record its source and tail error. The eighth-derivative limit remains in
force if an endpoint cancellation prevents a decision.

There is no evaluation grid, coefficient scan, sign test at \(r>3\),
new heat flow or replacement source in r1. Positive endpoint and tail
signs do not establish the intervening compact region. An asymptotic
tail sign is not an effective cutoff. Do not substitute weak consecutive
positivity for all-minors positivity or treat this finite-order pilot as
an RH criterion.

Complete unaffected checks if one condition fails. A precise failed
identity, required source sign or feasibility test is a valid bounded
return. Scope a failed source condition to this particular mechanism;
it does not invalidate the coefficient criterion or integrated
cancellation. Apply the control distinctions in Note01 Section 5:
a positive-time collision need not contradict time-zero order-three
positivity.

## 5. Save the return and hand back the decision

Mark J-E01 Active when execution begins. Save one dated return in
`01_jensen/notes/` using the next unused note number; place algebra code and
small records in `01_jensen/numerics/`, creating that folder with its first
artifact. Any separate assessment belongs in `01_jensen/reviews/`. Record
the actual model/effort, request r1, input/code hashes, formulas,
corrections, errors, failed or unresolved cases and evidence paths.

Update the owning register and relevant navigation after rereading them.
Preserve the frozen request and unrelated changes. No manuscript,
snapshot or new literature campaign is required.

- If the identity and bounded end tests support the mechanism, return
  the unresolved **global** source signs to **[B] J-B02 — Astra**.
- If a required source sign fails, the endpoint order is insufficient,
  or the representation/curvature mechanism needs changing, return the
  precise obstruction to **[B] J-B01 — Astra**.

Stop after the return. Neither outcome dispatches another task.

Use the authorized history tool at the start and end. A new Jensen-only
chat belongs in `01_jensen/chat-histories/` under its own actual identity;
an existing registration keeps its unique identity and location. This
chat is already registered there. Follow the bounded exact-turn capture
until trusted native-hook activation is verified.

## Pasteable Sol prompt

> Continue Investigation07 in
> /Users/ebbaker/Documents/shifted-zeta-positivity.
> Read AGENTS.md, GPT_RESEARCH_MODEL_WORKFLOW.md and
> papers/investigations-5/07_positive_theta_primitives/01_jensen/notes/02_CONTINUATION_FOR_SOL_J_E01_20261101.md.
> Reread the Jensen live register, then execute [E] J-E01, frozen request
> r1 in Note01 Section 7. Audit the real derivative-determinant formula
> with all endpoints and factorials, reproduce the classical order-two
> check, and perform only the specified origin/tail feasibility tests for
> R' and C. Preserve the canonical source, Q8 limit and finite arithmetic
> limits. Save the derivation and any code/record in the designated route
> folders, update the register, and return the named B decision. Stop at
> that boundary; do not start a global sign proof or broaden the scan.

[decision]: 01_J_B01_COEFFICIENT_REPRESENTATION_DECISION_20261101.md
[request]: 01_J_B01_COEFFICIENT_REPRESENTATION_DECISION_20261101.md#7-frozen-execution-request-j-e01-r1
[progress]: ../research-progress/01_JENSEN_RESEARCH_PROGRESS_20261101.md
[closure]: ../../notes/02_CNV_DETERMINANT_TRANSFER_AND_THETA_DIFFERENTIAL_CLOSURE_20261101.md
[formulations]: ../../notes/03_RH_FORMULATIONS_AND_RESEARCH_DIRECTION_20261101.md
[catalog]: ../../references/sources.json
[agents]: ../../../../../AGENTS.md
[workflow]: ../../../../../GPT_RESEARCH_MODEL_WORKFLOW.md
[large]: ../../../../../LARGE_FILES.md
[chat]: ../../../../../tools/CHAT_HISTORY.md
[results]: ../../../../../result-summaries/README.md
[theta]: ../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../avoid/README.md
[normalization]: ../../../../../avoid/08_normalization_and_constant_slips.md
[joint]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[scopes]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[imports]: ../../../../../avoid/16_unchecked_imports_and_novelty_claims.md
