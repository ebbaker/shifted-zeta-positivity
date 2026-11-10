# Next session on the joint primitive lattice estimate

Session begun 9 November 2026, America/New_York. Prepared for **Edward Baker**
with substantial OpenAI Codex LLM assistance, direct chat0007, thread
`01a1c389-3fe9-7930-8223-c935cc1920e1`. Actual backend model and reasoning
effort are unavailable in accessible capture metadata. This continuation
was requested by the author after the primitive/lattice derivation.

**Default next task: [B] TND-D-B03 — joint primitive/lattice estimate,
GPT-6 Astra.** The new input is a proved exact representation, with
proof-author checking; the conceptual choice is how to use its complete
arithmetic cancellation to obtain a useful signed estimate. The manuscript
now develops the formula in Section 9, Theorem 9.2. This is a focused
continuation of B03, not a restart of the completed r3 survey.

| Next task | Type | Recommended model | Readiness or dependency | Expected output |
| --- | --- | --- | --- | --- |
| B03 primitive/lattice continuation | B: select and test one joint arithmetic reorganization | **GPT-6 Astra**, following the existing B03 routing; plan r3 records Astra/ultra | Ready for the author's next session from Brainstorm06 and manuscript Section 9; finite scope below | One source-specific lemma/proof strategy and useful signed consequence, or a precise remaining gap |
| E09, followed by E10 | E: fixed proof/calculation, then separate assessment | **GPT-6.1 Sol**, under the existing project workflow | Unissued until B03 fixes a contract satisfying plan r3 section 6 | Bounded proof/error return and scope-conscious assessment |

These are recommendations, not model changes, dispatched workers or an
automatic research schedule. [Progress01][progress] is the sole live
register. E11 is the author's separate manuscript/continuation production
task; it does not supply a signed estimate or activate E09/E10.

## Read these sources first

1. [Brainstorm06][primitive], especially equations (7), (7a), (8)–(13),
   and [manuscript Section 9][section]. The manuscript uses lower-case x
   for the Gaussian center to distinguish it from the position operator;
   the research notes use X.
2. [Note09][gaussian] section 1 for the complete resolving error and
   section 3 for the precisely scoped failure of discarding positive
   contributions. Its old result does not exclude the present method.
3. The [result index][results], particularly [theta arithmetic14][theta]
   and [collision controls12][controls], and the [avoid index][avoid],
   particularly [target classification01][a01], [premise screening02][a02],
   [scoped exclusions07][a07], [joint estimates12][a12] and
   [utility20][a20]. Use the linked sources rather than expanding their
   summaries into another survey.
4. [Plan r3][plan] section 6 for the E09/E10 gate and the
   [B/E workflow][workflow] for model routing. The old exhausted r3 pass
   remains historical; the author supplied the new primitive method.

The original radial identities are in Investigation05 [Note01][radial]
section 2 and [Note73][ibp] sections 1–4. They are already located and
used; no new search for the scalar primitive is needed.

## The exact starting object

Keep the canonical source and normalization
\[
 H_\lambda(k)=\int_0^\infty e^{\lambda u^2}\Phi(u)\cos(ku)\,du,
 \quad F_\lambda=e^{\lambda u^2}\Phi,
 \quad h_*=H_{1/2}(0).
\]
For a normalized Gaussian w_v of variance v and center X,
\[
 A_0=\int_{\mathbb R}w_v(k-X)[(H_\lambda')^2-H_\lambda H_\lambda'']\,dk.
\]
Set
\[
 A(r)=\sum_{n\ge1}e^{-\pi n^2r^2},\quad
 \psi(u)=e^u A(e^{2u}),\quad D_u=\partial_u^2-1.
\]
Then D_u psi=8 Phi and psi'(0)=-1/2. With
\[
 g(s)=e^{-vs^2/2}\cos(Xs),\qquad
 T(p,q)=\frac{e^{\lambda(p^2+q^2)}}4
 [(p-q)^2g(p+q)+(p+q)^2g(p-q)],
\]
the complete formula is
\[
 \boxed{A_0=\frac1{64}\iint_{[0,\infty)^2}
 \psi(p)\psi(q)D_pD_qT(p,q)\,dp\,dq
 -\frac1{16}H_{\lambda-v/2}''(X).}
\]
Its lattice weight is
\[
 \psi(p)\psi(q)=e^{p+q}\sum_{m,n\ge1}
 e^{-\pi(m^2e^{4p}+n^2e^{4q})}.
\]
The square-index polynomial factors have been removed exactly. The
geometry is radial in three dimensions per source, while the arithmetic
lattice here has rank two. There is no mean replacement or new
normalization. Complete tails pay the derivative transfers.

The boundary is a main part of the signed problem. Near a hypothetical
double event with a=H''(lambda*,k*) != 0, its contribution tends to -a/16,
although the complete A0 tends to zero. It cannot be discarded or assumed
to lie at the smaller resolving scale.

## One bounded next pass

Choose **one joint theta-product or modular reorganization of this full
formula**, using the separated test and fourth-order operator in
Brainstorm06 equation (8). The product identity
\[
 A(r)A(s)=\tfrac14[\Theta(r)\Theta(s)-\Theta(r)-\Theta(s)+1]
\]
and inversion \(\Theta(r)=r^{-1}\Theta(1/r)\) are available. Preserve
the axis subtractions, sphere terms, transformed domain and test
derivatives. The separate terms in the bracket need not be integrable
against the growing test; prove any regrouping before interchanging it
with integration. The a=p+q, b=p-q domain is a >= |b|, not a product.

Use one conceptual/analytical pass and one local clarification or check,
with at most one E09 successor contract. No broad numerical campaign,
new physical construction or further manuscript expansion is part of
this next B03 pass. A routine algebra repair stays inside the pass; a
different mechanism requires an explicit scope revision.

The inherited initial comparison is hypothetical nondegenerate events
\[
 \lambda_*\in[1/8,3/8],\quad k_*\in[1/2,100],\quad
 0<\epsilon\le1/16,\quad
 (\lambda,X,v)=(\lambda_*-\epsilon,k_*,\epsilon).
\]
It is neither a certified event-free box nor a claim that theta has an
event. Write b=|H''(lambda*,k*)|. [Note09][gaussian] gives
\[
 A_0=-\tfrac12b^2\epsilon+\mathcal E,
 \qquad |\mathcal E|\le E_1(b,I_3(3/8),I_4(3/8),\epsilon).
\]
Use its complete explicit equation (3), not only big-O notation. At each
fixed event, E1 <= b² epsilon/4 gives a negative resolving margin. No
uniform curvature floor or event-independent epsilon is available.
The exact primitive identities themselves hold beyond this initial box;
an enlarged estimating target must be stated explicitly.

Before declaring an estimating gain, name the independent arithmetic
premise, the signed quantity controlled, the parameter range, all tails
and derivative/boundary errors, and the consequence compared with direct
analysis using the same information. Primitive positivity and endpoint
normalization are shared by colliding controls. Brainstorm06 section 5
records the full premise screen; failure of the literal theta identity
does not by itself prove failure of a proposed inequality.

If the chosen reorganization gives only another exact formula, preserve
it at that scope and identify the remaining cancellation estimate. Do not
interpret this as either a collision exclusion or a universal failure of
lattice methods. A fixed E09 contract is issued only after plan r3's gate
is satisfied. The present continuation issues none.

## Model change and a pasteable starting request

On a model change, record the new actual model/effort only if the runtime
or source transcript supplies them. Keep chat0007's real provenance and
the existing histories intact; register a genuinely new chat under its
actual identity in this investigation, following [CHAT_HISTORY][capture].
Read the current register before changing live status. Preserve the
assessed count results, the earlier r3 stop, Brainstorm06's proof-author
level and E11's production-only status.

> Continue TND-D-B03 from brainstorm Note07 and manuscript Section 9.
> Follow the root AGENTS.md, result-summaries/README.md, avoid/README.md
> and the sole direct-branch progress register. In one bounded conceptual
> pass, test one joint theta-product/modular reorganization of the complete
> two-primitive A0 formula, retaining the boundary curvature term and all
> tails. Seek a source-specific signed estimate with a declared useful
> consequence against the same-information direct baseline. Use the exact
> controls and resolving error; do not restart the scalar primitive
> derivation or infer a sign from primitive positivity. Return one fixed
> E09 contract if justified, or the precise remaining gap. Save conceptual
> notes in brainstorm/notes, update progress, and capture the actual chat.

[primitive]: 06_TND_D_TWO_SOURCE_PRIMITIVE_IBP_AND_LATTICE_20261109.md
[section]: ../../manuscript/sections/09_primitive_lattice.tex
[gaussian]: ../../notes/09_TND_D_B03_GAUSSIAN_INTERFACE_AND_SIGNED_KERNEL_SCREEN_20261109.md
[progress]: ../../research-progress/01_DIRECT_NEWMAN_REALIZATION_RESEARCH_PROGRESS_20261105.md
[plan]: ../../research-plan/03_DIRECT_NEWMAN_REALIZATION_RESEARCH_PLAN_R3_20261109.md
[radial]: ../../../../05_radial_theta_collision_geometry/notes/01_RADIAL_THETA_GEOMETRY_AND_COLLISION_MECHANISMS_20261027.md
[ibp]: ../../../../05_radial_theta_collision_geometry/notes/73_BOOK_INTEGRATION_BY_PARTS_AND_FEEDBACK_PAIRINGS_20261029.md
[workflow]: ../../../../../../GPT_RESEARCH_MODEL_WORKFLOW.md
[results]: ../../../../../../result-summaries/README.md
[theta]: ../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[controls]: ../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../avoid/README.md
[a01]: ../../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[a20]: ../../../../../../avoid/20_volume_without_a_gain.md
[capture]: ../../../../../../tools/CHAT_HISTORY.md
