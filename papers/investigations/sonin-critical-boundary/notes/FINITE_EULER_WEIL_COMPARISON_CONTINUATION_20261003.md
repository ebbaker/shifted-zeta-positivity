# Continuation plan for finite Euler products and the Weil comparison

3 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); the exact serving variant and configured reasoning effort are not exposed and are not inferred.
Status: research handoff and proposed investigation, not a new proof or independent specialist review.
Repository baseline inspected: `5a431c1d7d8fc10cc3adeaa28d4f7a7818a1697e`; the working tree was clean before this note was added.

Investigate whether the complete arithmetic Weil form can be compared with an independently positive Sonin trace through finite Euler products and operator identities, without using sums over zeta zeros in the proposed proof. The first task is to audit the finite-product boundary identity and isolate a genuinely new inequality. Exact capture of the active prime sum does not establish the sign of the Sonin correction.

## Motivation and sufficient goals

The current [manuscript](../manuscript.tex), especially the boundary-resolvent representation and the arithmetic comparison, defines

\[
B_\sigma[F]=\operatorname{Tr}(C_F\Pi_\sigma C_F^*)
=\|C_F\Pi_\sigma\|_{\mathrm{HS}}^2\ge0,
\qquad
R_\sigma[f]=\operatorname{Tr}(f(D)(L_\sigma-\Pi_\sigma)f(D)^*)\ge0.
\]

Its critical-boundary results identify the majorant limit with the critical-zero measure. They do not identify the exact projection trace with the complete Weil form. In its conventions,

\[
B_\sigma[F]-Q[F]
=-R_\sigma[\widehat F]-Z_{\mathrm{off}}[F]+o_F(1).
\]

Vanishing of the return defect alone would recover the critical-zero contribution. It would not exclude off-line zeros. The present investigation instead seeks a direct arithmetic comparison, with positivity supplied independently by operators.

A sufficient goal is a positive trace family tending to \(Q[F]\) for every admissible fixed source. Equality is unnecessary: a lower bound

\[
Q[F]\ge B_j[F]-\varepsilon_j[F],\qquad
B_j[F]\ge0,\qquad \varepsilon_j[F]\to0
\]

would also suffice. The admissible class must allow arbitrarily large compact supports and complex sources. Pointwise convergence or comparison for each fixed source suffices; one uniform rate over the whole source class is not required. Weil's criterion supplies the eventual RH implication. It does not supply the operator inequality being sought.

Use pole-neutral sources

\[
F=(-\partial_x^2+1/4)h,\qquad h\in C_c^\infty(\mathbb R).
\]

Their transforms vanish at \(\pm i/2\). The earlier canonical audit proves that preparation covers the full pole-neutral class without enlarging support. It does not impose zero mean or additive parity. Any additional finite moment condition needs an explicit criterion justifying its use; a fixed support restriction cannot replace the all-support requirement.

## Existing research to read first

This plan refines an existing finite-place program rather than introducing finite-place transport as a new idea. Start with:

1. [Canonical comparison audit](../../../susy-positivity/investigations/wilson-loewner/arithmetic-storage/notes/SONIN_CANONICAL_COMPARISON_AUDIT_20260929.md), for the normalization, source class, exact inverse metric, and smoothing.
2. [Place addition and error control](../../../susy-positivity/investigations/wilson-loewner/arithmetic-storage/notes/SONIN_PLACE_ADDITION_AND_ERROR_CONTROL_20260929.md), especially the distinction between partial and complete arithmetic residuals and the obstruction to generic place monotonicity.
3. [Moving source tails and signed place addition](../../../susy-positivity/investigations/wilson-loewner/arithmetic-storage/notes/SONIN_DIRECT_PLACE_TAIL_CRITERIA_20260929.md), for what a growing-place limit would require.
4. [Earlier direct-limit continuation](../../../susy-positivity/investigations/wilson-loewner/arithmetic-storage/notes/SONIN_DIRECT_LIMIT_CONTINUATION_20260929.md), read as historical context; its then-open trace-finiteness question is addressed in the later manuscript.
5. [Manuscript review](../reviews/MANUSCRIPT_REVIEW_CLAUDE_20261001.md), for the assessed scope and remaining verification work.

Compare with Connes and Consani, [Weil positivity and trace formula, the archimedean place](https://alainconnes.org/wp-content/uploads/Selecta.pdf), particularly Theorem 4.6, Theorem 6.11, and Appendix C in the 2021 author version; their [quasi-inner framework](https://arxiv.org/abs/2008.10974); and Connes, Consani, and Moscovici, [semilocal transport](https://arxiv.org/abs/2310.18423v2), Sections 4.6–4.8. Check hypotheses and source conditions rather than importing a positivity conclusion from a restricted-support theorem.

## The arithmetic target without a zero sum

Use the manuscript's Fourier convention and inner products antilinear in the first variable. For a source of support diameter at most \(L\), set

\[
\kappa_F(u)=\int\overline{F(x)}F(x+u)\,dx,
\quad
\gamma_\infty(t)=\operatorname{Re}\psi(1/4+it/2)-\log\pi,
\quad
\Gamma[F]=\int\gamma_\infty(t)|\widehat F(t)|^2\frac{dt}{2\pi}.
\]

For prepared sources the complete target is

\[
Q[F]=\Gamma[F]-W_{1/2}[F],
\qquad
W_{1/2}[F]=\sum_{p,m\ge1}(\log p)p^{-m/2}
\{\kappa_F(m\log p)+\kappa_F(-m\log p)\}.
\]

Only shifts inside the correlation support contribute. Taking
\(S_L=\{p:p\le e^L\}\) safely includes every active prime. Equality at a support endpoint contributes zero for the compact smooth sources under consideration. All active powers of every included prime must be retained.

Consequently the partial prime expression \(W_{S_L,1/2}[F]\) equals the complete one exactly. This is an arithmetic support statement, not a statement that the trace or its correction stops changing when additional places are included.

## Finite Euler product and transported projection

For fixed finite \(S\) and \(\sigma>0\), define

\[
\zeta_S(s)=\prod_{p\in S}(1-p^{-s})^{-1},\qquad
v_{S,\sigma}(t)=v_\infty(t)
\frac{\zeta_S(\sigma+it)}{\zeta_S(\sigma-it)},
\quad
\mathcal F_{S,\sigma}=\mathcal Jv_{S,\sigma}(D),
\]

where \(v_\infty\) is the manuscript's gamma phase. The finite product is nonzero and pole-free on \(\operatorname{Re}s>0\), so this construction reaches \(\sigma=1/2\) without a zero-location assumption. It does not satisfy the full zeta functional equation that makes the global endpoint symbol equal to one.

To avoid confusing the transport with the frequency operator \(D=-i\partial_x\), call the transport \(\mathscr D_{S,\sigma}\). With
\((U_ah)(x)=h(x-a)\), its candidate formula is

\[
\mathscr D_{S,\sigma}=\prod_{p\in S}(I-p^{-\sigma}U_{\log p}),
\qquad
\mathcal F_{S,\sigma}
=\mathscr D_{S,\sigma}\mathcal F_\infty\mathscr D_{S,\sigma}^{-1}.
\]

For finite \(S\), each inverse has a norm-convergent causal geometric series. The bounds
\(\ell_{S,\sigma}=\prod_{p\in S}(1-p^{-\sigma})>0\) and
\(u_{S,\sigma}=\prod_{p\in S}(1+p^{-\sigma})\)
give bounded invertibility. They need not remain useful as \(S\) grows. Check the conjugation orientation directly against the symbol before using it.

Define \(T_{S,\sigma}=\chi\mathcal F_{S,\sigma}P\),
\(C_{S,\sigma}=\chi\mathcal F_{S,\sigma}\chi\), and the actual kernel projection \(\Pi_{S,\sigma}\). Reconcile it with the finite-place metric formula

\[
\Pi_{S,\sigma}
=\mathscr D_{S,\sigma}\Pi_\infty
M_{S,\sigma}^{-1}\Pi_\infty\mathscr D_{S,\sigma}^*,
\quad
M_{S,\sigma}
=\left.\Pi_\infty\mathscr D_{S,\sigma}^*\mathscr D_{S,\sigma}\Pi_\infty\right|_{\operatorname{Ran}\Pi_\infty}.
\]

Do not omit this inverse compressed metric. Define
\(B_{S,\sigma}[F]=\|C_F\Pi_{S,\sigma}\|_{\mathrm{HS}}^2\), and justify finiteness for the source class independently of arithmetic subtraction.

## First assignment for the next investigation

Audit the finite-product version of the boundary-resolvent proof at \(\sigma=1/2\). The proposed identity to establish is

\[
B_{S,1/2}[F]=\Gamma[F]-W_{S,1/2}[F]+K_{S,1/2}[F],
\]

with the correction represented independently by

\[
K_{S,\sigma}[F]
=2\operatorname{Re}\operatorname{Tr}_{\chi\mathcal H}
\bigl(C_{S,\sigma}(I_\chi-C_{S,\sigma}^2)^{-1}
T_{S,\sigma}X_{F,e}\bigr),
\quad
X_{F,e}=Pa_e(D)\chi,
\quad
a_e(t)=\tfrac12\bigl(|\widehat F(t)|^2+|\widehat F(-t)|^2\bigr).
\]

This note does not claim the adaptation has been proved. Verify bounded causal transport, a strict cutoff gap for fixed finite \(S\), the source-smoothed trace ideals, and all cyclicity steps. The finite Euler series should supply the prime bulk directly. Retain the finite spatial crossing strip and do not split unsmoothed operators into separately divergent traces.

For \(S\supseteq S_L\), the identity would imply

\[
Q[F]=B_{S,1/2}[F]-K_{S,1/2}[F].
\]

Reconcile this with the existing complete-residual formulas, including their signs and archimedean correction. Deriving the same scalar identity in a different notation is a consistency result, not a new positivity theorem.

The first session should end with either a verified finite-product identity and its precise hypotheses, or a specific obstruction. It should then state one narrow, independently formulated inequality to investigate next. Do not make proof of RH the first-session deliverable.

## Algebraic routes after the identity audit

A sufficient strong comparison is \(K_{S,1/2}[F]\le0\); the weaker bound \(K_{S,1/2}[F]\le B_{S,1/2}[F]\) suffices as well. Investigate a factorization, Schur complement, or signed covariance estimate using the actual Sonin kernel and the prepared source structure. The mixed trace is not nonnegative or nonpositive merely because other blocks are positive.

The prior place-addition note supplies an abstract finite-dimensional control with increments of either sign. Thus generic unitary translations, Gram positivity, and bounded invertible transport do not establish place monotonicity. Any new result must identify the additional Sonin-specific structure it uses. Check the empty-prime case against the known prolate correction and its extra source conditions before proposing induction in places.

As an alternative, use the arithmetic quadratic form directly. Keeping \(U_ah(x)=h(x-a)\),

\[
Q[F]=\langle F,\gamma_\infty(D)F\rangle
-\sum_{p,m}(\log p)p^{-m/2}
\langle F,(U_{m\log p}+U_{-m\log p})F\rangle.
\]

On sources supported in a specified interval the sum is finite. Seek positivity of this form on the pole-neutral subspace, or equivalently after \(F=(-\partial_x^2+1/4)h\). Treat the gamma multiplier and preparation through quadratic-form domains; do not silently replace them by bounded matrices. A sum-of-squares representation would be useful only if derived independently, rather than obtained by assuming the desired positivity.

## Decision criteria and outputs

Support-adapted finite sets may suffice for a direct inequality: proving it for each admissible source does not require one common infinite-place limit. If choosing a limiting route instead, specify the place sequence independently of the individual source and prove its convergence. Once the active arithmetic sum is captured, inactive additional primes can still change both the projection trace and correction, with compensating changes in their difference.

Numerics may falsify a proposed correction sign or identify a promising source sector. They cannot establish an all-support theorem from a finite sample. Retain both parity sectors and complex-source polarization, resolve the inverse metric, and enclose omitted tails when making certified claims. A positive correction would refute the strong bound \(K\le0\), not RH or necessarily the weaker comparison.

Save derivations in this investigation's `notes/`, numerical work in `numerics/`, and audits in `reviews/`, each with model and effort metadata. Follow [LARGE_FILES.md](../../../../LARGE_FILES.md); cite third-party papers rather than adding their PDFs. Record future notable commits in the concise draft history rather than creating manuscript snapshot folders.

## Platform and model recommendation

Use Codex with the local repository for the continuation. The task depends on cross-reading earlier proofs, retaining exact conventions, saving incremental derivations, and possibly running reproducible numerical checks. ChatGPT can be useful for a separate conceptual critique supplied with the relevant source passages; changing interfaces alone does not establish a mathematical capability advantage.

For the first proof audit and the search for a new signed inequality, prefer GPT-6 Astra at Extra high reasoning. This is a judgment about the task: it requires demanding mathematical analysis and detection of circular arguments. Official [model-selection guidance](https://learn.chatgpt.com/docs/model-selection) recommends Astra for demanding analysis and exacting requirements.

GPT-6.1 Sol at High or Extra high is a reasonable economical choice for bounded derivations, numerical implementation, and repository maintenance, with Astra used for the pivotal proof audit. Its [model documentation](https://developers.openai.com/api/docs/models/gpt-6.1-sol) describes near-Astra performance at lower cost and recommends comparing on the actual task. No task-specific benchmark establishes equivalent performance on this investigation, and cheaper tokens do not establish fewer total tokens to obtain a correct proof. Use the reasoning controls available in the chosen client rather than assuming API effort names map exactly to desktop settings.

## Suggested next-session instruction

Read this continuation note and its linked canonical and place-addition audits. First verify or obstruct the finite Euler product boundary identity at the critical exponent, retaining the actual inverse compressed metric and the independently defined correction. Reconcile it with the existing complete residual, then identify one Sonin-specific algebraic inequality that could imply positivity for the full pole-neutral source class. Keep derivations free of sums over zeta zeros except when stating the eventual Weil-criterion implication. Report reused results, new results, and unresolved claims separately. Save a concise derivation note and an adversarial proof audit before considering a manuscript change.
