# Review of the finite Euler continuation and next steps

3 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), as identified in the session instructions. Exact serving variant and configured reasoning effort were not exposed; neither is inferred. Three parallel same-model reviews covered the identity, residual estimates, and numerical implementation. This is an internal mathematical assessment, not independent specialist refereeing.

Reviewed repository state: `c943006b5003dad7ac48afc7689e7273f30c267a`, especially the changes since `2e84e2c` and the preceding continuation plan. The working tree was initially clean. The manuscript source SHA-256 is `f48309c50261d01b46023c6255c10ad8e784f8f92329c1357b91e11f9e293fc8`. This review changes no manuscript claims.

The latest work makes useful analytic and computational progress. The finite Euler identity and fixed-place obstruction passed the present checks, as did the analytic residual bounds. The remaining comparison still lacks a sign theorem. The highest-value continuation is a bounded attempt to certify the positive correction suggested by the fixed odd source. A one-sided lower bound for the transported Sonin trace may answer that question more cheaply than enclosing the entire boundary correction.

## Assessment of the contributions

| Contribution | Assessment | Limitation |
|---|---|---|
| Finite Euler boundary identity for every finite prime set and every positive exponent | Sound technical extension of the existing transport and boundary machinery, including the critical exponent | Establishes an identity, not a correction sign |
| Expanding-source obstruction at fixed finite places | Clearest new conceptual result in this continuation; excludes a broad class of strategies | Does not apply when the prime set changes to capture the growing support |
| Primal-dual residual and nuclear source-tail bounds | Valid framework for an eventual certificate; addresses previously uncontrolled complements | No complete numerical error budget has yet been evaluated |
| Full-output leakage Grams and first-prime diagnostic | Useful implementation progress and a concrete conjecture test | Positive finite approximations remain uncertified and sensitive to the trial space |
| Mean-functional rank-one proposal | Now connected to an explicit finite Euler boundary operator | Its shape and mixed-term lemma were already in the 29 September work; it remains unproved |

The [identity note](../notes/FINITE_EULER_BOUNDARY_IDENTITY_20261003.md), especially Sections 2–4, correctly retains the inverse compressed metric. Its causal transport has the right orientation and a bounded inverse for fixed finite places. The inherited archimedean gap gives a strict finite-place cutoff gap. Source smoothing establishes trace finiteness before arithmetic subtraction; no trace of unsmoothed critical one-prime C squared is needed. The multiplier symmetrization retains arbitrary complex sources. I found no material algebraic or trace-ideal defect in the added manuscript proposition, beginning at source line 722.

The [fixed-place obstruction](../manuscript.tex), beginning at source line 1787, is stronger than a failed numerical sign test. For each fixed finite S and positive sigma, the rescaled prepared sources have a strictly negative limiting partial arithmetic bulk. Therefore K exceeds B and is positive for sufficiently large support. The argument also works with zero mean. This rules out fixed-place all-support comparisons with that partial bulk. The dominated-convergence argument depends essentially on keeping S fixed; applying it to support-adapted prime sets would be invalid.

After active-prime capture, the identity is

\[
Q[F]=B_{S,1/2}[F]-K_{S,1/2}[F].
\]

Consequently the weak inequality K at most B is exactly the desired arithmetic positivity in these variables. Its reformulation alone supplies no new mechanism. The contribution is the independently specified correction and the tools available to study it.

These are statements about progress within the repository, not claims of first discovery in the literature. [Connes, Consani and Moscovici, Sections 4.6–4.8](https://arxiv.org/html/2310.18423v2#S4.SS6) already provide semilocal Sonin transport and a place-dependent Hilbert metric. [Connes and Consani, Theorem 6.11 and Appendix C](https://alainconnes.org/wp-content/uploads/Selecta.pdf) provide the short-support mean penalty and the restricted-test criterion. The former does not establish the proposed bound for increasing support and added primes. A theorem-by-theorem priority comparison remains appropriate before submission.

## Numerical evidence and its practical limits

The [diagnostic](../numerics/finite_euler_first_prime_DIAGNOSTIC_20261003.md) correctly distinguishes the full compressed square H from D squared. Their difference is the positive leakage Gram of the omitted output space. It also correctly distinguishes the two finite matrix orders, which need not commute although the continuum operators do.

Parallel reviewers independently replayed the small leakage check and the 128-cell graded-mesh first-prime run. The three Gram-entry checks agreed with quadrature within approximately 2.22e-16, and the full H check within 2.01e-14. The leakage trace was 0.3348778504. The 128-cell run reproduced the retained odd correction 0.016673290082474146 and finite denominator gap 9.540931205743335e-5. The replay used SciPy 1.17.1, versus 1.18.1 in the retained record. All four retained numerical JSON records bind to the current generating script hash, `7834887930053461425911fe04a079d7ed3317d47cf1957528e8bbb9af64a754`. These are floating-point consistency checks, not interval proofs. The 256- and 512-cell runs were inspected, not independently replayed in this review.

The stored odd correction falls from about 0.01667 at 128 cells to 0.00709 at 512 cells. At 512 cells the reversed-order value is about 0.00423. The full leakage norm is approximately 0.00647, compared with a finite denominator gap around 1.08e-5. This does not itself bound the scalar error, but it prevents treating leakage as negligible. The observations support investigating the source; they do not establish a positive continuum correction or a positive limiting value.

The [residual certificate](../notes/FINITE_EULER_BOUNDARY_RESIDUAL_CERTIFICATE_20261003.md) and [full leakage analysis](../notes/FINITE_EULER_RANK_ONE_ANALYSIS_20261003.md) passed checks of the primal-dual identity, nuclear Legendre tail, full-space Gram formulas, and truncation propagation. Their practical sharpness is untested. With the inherited certified gap,

\[
g=(17-12\sqrt2)57\cdot10^{-6}\approx1.67792334\cdot10^{-6},
\]

the residual coefficient 2/g is about 1.192 million, and the source nuclear-tail coefficient is about 1544. If either term alone were allowed an error of 0.001, equal primal and dual full residual norms would need to be below roughly 2.90e-5, or the nuclear source tail below roughly 6.48e-7, respectively. An actual total budget must allocate error among both terms and evaluation errors. These illustrative thresholds explain why successful finite matrix solves and tiny Euler tails do not settle the sign.

## Recommended first continuation

Use the exactly odd prepared source already specified, with b equal to 9/20,

\[
f_1=\frac{(-\partial_x^2+1/4)(x\phi(x))}
{\|(-\partial_x^2+1/4)(x\phi(x))\|_2},
\quad \phi(x)=\exp[-1/(1-(x/b)^2)]\,1_{|x|<b}.
\]

Its zero mean follows exactly from parity. The [earlier arithmetic certificate](../../../susy-positivity/investigations/wilson-loewner/arithmetic-storage/notes/SONIN_FINITE_MELLIN_DEFECT_20260929.md) already gives

\[
1.047808580\le Q[f_1]\le1.047808594.
\]

These inherited interval inputs should be verified through their generating records before a new certificate uses them. They were not regenerated with interval arithmetic here. A separate exploratory Fourier computation gave Q approximately 1.047808586958420, consistent with that interval.

For exact archimedean Sonin vectors w_j, set y_j equal to their finite-place transport. Define finite matrices

\[
G_{ij}=\langle y_i,y_j\rangle,\qquad
H_{ij}=\langle C_{f_1}y_i,C_{f_1}y_j\rangle.
\]

If the columns are independent, the finite-subspace trace is

\[
B^{[d]}=\operatorname{tr}(G^{-1}H)\le B_{\{2\},1/2}[f_1].
\]

This is the inherited actual-Sonin Galerkin lower bound, also valid with nonorthogonal columns; see the [actual projection enclosure note, equations (4)–(7)](../../../susy-positivity/investigations/wilson-loewner/arithmetic-storage/notes/SONIN_ACTUAL_PROJECTION_ENCLOSURES_20260929.md). A rigorous lower enclosure strictly greater than 1.047808594 would immediately prove K[f_1] positive and refute the proposed mean-only bound at this support. No upper bound for the omitted positive trace is needed for this one-sided conclusion.

This approach still requires certified actual kernel membership, a positive enclosed Gram matrix, full integrals for the retained source-smoothed vectors, and projection and arithmetic error bounds. A small cutoff residual does not establish actual membership. Exact columns can be defined by projecting seeds with the archimedean projection and enclosing that construction.

For prime 2 the compressed transport metric lies between approximately 0.0857864 and 2.914214, so its operator condition number is at most 33.9706. This is a useful advantage over the finite-place boundary inverse. Poorly chosen nonorthogonal coordinates can still make a finite Gram matrix ill-conditioned. The earlier two-vector trial space and first-moment bounds fall well short of the threshold; merely replaying them is not useful. The pilot should select projected seeds adapted to the dominant smoothed source response, then measure attainable lower bounds before investing in outward evaluation.

This is a proposed computational strategy based on existing identities, not a new sign result. If a lower bound does not exceed the threshold, the test is inconclusive. It does not validate the conjecture.

## Other useful continuation options

1. **Complete a boundary-residual enclosure.** Implement the existing full leakage, nuclear source tail, Euler truncation, primal-dual, and outward arithmetic estimates for the same odd source. Start with a table of estimated contributions to the error budget. Improve trial vectors, certify a sharper gap, or use source-specific energy estimates if the global inverse-gap bound dominates. Deliver one enclosing interval with auditable inputs. A positive interval refutes the mean-only conjecture; a negative interval settles only that source; an interval containing zero identifies a numerical limitation. This is the best option if developing reusable certificate machinery is the primary objective.

2. **Investigate the constrained sign directly.** If the numerical test leaves a viable analytic direction, target K at most zero on all pole-neutral, mean-zero sources for every support size. Exact preparation can be written as \(F=\partial_x(-\partial_x^2+1/4)h\) for compact smooth h. Proving that sign would already suffice for the restricted Weil criterion. The mixed-term estimate needed for a finite rank-one penalty is a stronger target and need not be a prerequisite. A concrete analytic project would derive the prepared source form for the actual prime-2 kernel, identify its local and translated singular terms, and determine whether a coercive part plus a controllable compact remainder exists. Such a decomposition must be proved; compactness of the boundary operator does not supply it.

3. **Consolidate the paper through specialist and priority review.** Review the finite Euler proposition, the fixed-place obstruction, and the earlier global critical-boundary results against the semilocal and Hardy/Hankel literature. Produce a precise table of inherited tools, new family-specific estimates, and unresolved comparisons. This has a clearer near-term publication payoff than extending exploratory grids. The detailed numerical certificate machinery can remain in the research notes until it proves a sign or another distinct result.

If the odd correction is certified positive, the mean-only hypothesis should be retired. The weaker comparison K at most B would remain open. A replacement using finitely many Mellin functionals would need a fixed permitted set of evaluation points, valid for unbounded support sizes, together with the requisite form estimates. A support-dependent collection of fitted eigenvectors or moment constraints is not automatically covered by the restricted criterion.

The present evidence favors the one-sided actual-Sonin trace pilot first, with the boundary-residual route as a parallel feasibility comparison. Further uncontrolled grid enlargement, an all-support fixed-prime induction, or declaring a positive finite correction to be a counterexample would not resolve the outstanding question.
