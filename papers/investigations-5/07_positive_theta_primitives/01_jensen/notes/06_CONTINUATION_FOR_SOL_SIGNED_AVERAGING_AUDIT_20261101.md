# Continuation for the Sol signed averaging audit

1 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**,
reasoning effort **max**.

**Next: [E] J-E01 r2 — Sol.** Audit the conditional signed-averaging
argument and its two bounded theta feasibility tests. The complete frozen
request is [Note05, Section 7][request]. This note packages that request;
it does not widen it. The [Jensen register][progress] owns live status.

| Next task | Type | Recommended model and reason | Ready or dependency | Expected output |
| --- | --- | --- | --- | --- |
| **J-E01 r2** | E | Sol; formulas, proof audit, two limits and stopping rules are fixed | Ready, unstarted | Audited conditional transfer, Gaussian check, Q10 origin sign and differentiated tail sign |
| J-B02 | B | Astra; a global source estimate still requires a conceptual proof strategy | Only if r2 supports the mechanism | Resolve one named global estimate or issue a bounded E contract |
| Return to J-B01 | B | Astra; choose a different mechanism or stop if feasibility fails | Only on r2 failure or unresolved feasibility | Scoped decision preserving both r1 and r2 evidence |

## Read in this order

1. Root `AGENTS.md`, `GPT_RESEARCH_MODEL_WORKFLOW.md`, `LARGE_FILES.md`
   and `tools/CHAT_HISTORY.md`. Refresh this chat at its actual existing
   registration; a new chat receives its own identity in this route's
   `chat-histories/` folder. Do not copy another conversation's identity.
2. The [live register][progress] and [Note05][decision], particularly its
   conditional proof and frozen r2 request.
3. [Sol's r1 return][return] and [exact record][record]. Reuse the valid
   real integral and preserve the proved negative origin curvature.
4. Shared [Jacobi closure][closure] and [source records][sources]. The
   FKG statement is for finite distributive lattices; Note05 supplies
   the continuous limit. The divided-difference simplex has area 1/2.
5. The [result index][results] and [avoid index][avoid], particularly
   [controls][controls], [theta identities][theta],
   [joint estimates][joint], [scoped exclusions][scopes] and
   [unchecked imports][imports].

## Mathematical state to preserve

At physical heat time zero,
\[
R=\Phi''/\Phi,\quad T=\Phi^{(4)}/\Phi,\quad C=R'T''-T'R'',\quad
K=R'C'-3CR''.
\]
The original requirement \(C\ge0\) fails near zero. The new candidate
requires \(R'>0\) and \(K\ge0\) globally; **neither global requirement
is proved**. If \(T=g(R)\), then \(g'''=K/(R')^5\).

On \(0<u_1<u_2<u_3\), factor
\[
\Delta_3=\prod_i\Phi(u_i)\,V(R(\mathbf u))\,
 g[R(u_1),R(u_2),R(u_3)].
\]
Let \(h\) be the divided difference and
\[
w_k=\prod_i u_i^{2k}\Phi(u_i)\,V(\mathbf u^2)V(R(\mathbf u)),\quad
Z_k=\int w_k,\quad
A_k=\frac{(2k)!(2k+2)!(2k+4)!D_{3,k}}{Z_k}.
\]
Note05 derives positive association of this weight, conditional on
\(R'>0\). If \(g'''\ge0\), then \(h\) is increasing, and the index tilt
by \((u_1u_2u_3)^{2\ell}\) gives
\[
A_{k+\ell}\ge A_k\ge A_0=48c_0^3/Z_0>0.
\]
This permits \(h<0\) near the origin. Its prospective payoff is the
normalized index comparison; order-three coefficient positivity itself
is already known. No increasing-order or RH conclusion follows.

The regular endpoint variables are \(x=u^2\),
\(\widehat R(x)=R(\sqrt x)\), \(\widehat T(x)=T(\sqrt x)\),
\[
H=\widehat R'\widehat T''-\widehat T'\widehat R'',\qquad
J=\widehat R'H'-3H\widehat R'',\qquad K=32u^5J.
\]
Here primes are in \(x\). The old record proves
\(\widehat R'(0)>0\), \(H(0)<0\); **\(J(0)\) remains uncomputed**.
It requires the tenth source derivative. In the tail the leading
\(t^8\) terms of \(R'C'\) and \(3CR''\) cancel, where \(t=\pi e^{4u}\).
Keep the first nonzero remainder with differentiated theta error control.

## Bounded work and return

Follow Note05 Section 7 without replacing its hypotheses. Audit the
proof, reproduce the Gaussian equality \(A_k=1\), compute only through
Q10 at the origin and P7 in the tail, and report the two sign outcomes.
For the single endpoint constant, the optional enclosure limit is 128
bits with one refinement to 256 bits. No grid, compact certificate,
quadrature campaign, higher order or source/heat change is authorized.
An unresolved or failed estimate is a valid bounded return; increasing
the derivative cap or selecting another sufficient condition requires B.

Save the return in `01_jensen/notes/`, new code and records in
`01_jensen/numerics/`, and any assessment in `01_jensen/reviews/`. Preserve the
r1 note, program and record. Update the sole register and route indexes,
record actual model/effort and input/code hashes, and capture chat history
at the start and end. End by naming the applicable B task from the table.
Passing both limiting tests does not prove the intervening global signs.

## Model change prompt

Sol is recommended because the conceptual mechanism has been selected
and the audit is now fixed. Edward Baker chooses the actual model,
effort and chat. No model switch or dispatch has occurred; a cross-model
LLM check is not independent specialist review.

> Continue Investigation07's Jensen route in
> /Users/ebbaker/Documents/shifted-zeta-positivity. Read AGENTS.md, the
> model workflow, the sole Jensen progress register, and
> papers/investigations-5/07_positive_theta_primitives/01_jensen/notes/05_J_B01_SIGNED_AVERAGING_DECISION_20261101.md.
> Complete [E] J-E01 r2 exactly as frozen in Section 7. Audit the signed
> averaging and FKG argument, its Gaussian normalization and the index
> comparison. Reuse r1's integral and preserve its negative origin C.
> Compute the new regular origin J only through Q10 and the new K tail
> only through P7, keeping the leading cancellation and rigorous errors.
> Save the return and exact evidence, update the owning register and
> refresh this chat's own history. Stop at the declared boundary: if
> supported, return global R'>0 and K>=0 to [B] J-B02; if failed or
> unresolved, return the scoped obstruction to [B] J-B01. Do not begin
> a global scan, raise the caps or replace the mechanism.

[request]: 05_J_B01_SIGNED_AVERAGING_DECISION_20261101.md#7-frozen-execution-request-j-e01-r2
[decision]: 05_J_B01_SIGNED_AVERAGING_DECISION_20261101.md
[progress]: ../research-progress/01_JENSEN_RESEARCH_PROGRESS_20261101.md
[return]: 03_J_E01_R1_REPRESENTATION_AND_ENDPOINT_TAIL_RETURN_20261101.md
[record]: ../numerics/J_E01_R1_EXACT_RECORD_20261101.json
[closure]: ../../notes/02_CNV_DETERMINANT_TRANSFER_AND_THETA_DIFFERENTIAL_CLOSURE_20261101.md
[sources]: ../../references/05_SIGNED_AVERAGING_SOURCES_20261101.md
[results]: ../../../../../result-summaries/README.md
[theta]: ../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../avoid/README.md
[joint]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[scopes]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[imports]: ../../../../../avoid/16_unchecked_imports_and_novelty_claims.md
