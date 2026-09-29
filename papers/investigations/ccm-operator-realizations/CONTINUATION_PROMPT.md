# Continuation prompt: audit the infinite-support route

Prepared 26 September 2026 for Edward Baker with LLM assistance. Preparation model: GPT-6 (Codex); exact variant and reasoning-effort setting unavailable. Suggested model for execution: GPT-6 Astra, Extra high (`xhigh`). This suggestion does not describe the model that prepared this file.

Execution status: completed on 26 September 2026. Read the [audit and decision](notes/CCM_INFINITE_L_BOUNDED_AUDIT_20260926.md) and [review](reviews/INFINITE_L_BOUNDED_AUDIT_REVIEW_20260926.md) before initiating further work. The instructions below are preserved as the scope of the completed round.

## Task

Continue the investigation in `/Users/ebbaker/Documents/shifted-zeta-positivity/papers/investigations/ccm-operator-realizations` by conducting one bounded feasibility audit of the **L-to-infinity limit**. Produce actual mathematical analysis and a clear decision about the next research investment. Do not default to the previously proposed 4096-mode fixed-L Schur computation.

The central question is whether the mass–stiffness realization can yield estimates that survive growing support, or merely relocates the original CCM difficulties. A valid negative or unresolved outcome is acceptable. Do not manufacture a positive theorem to justify the program.

## Read first

Read `PROGRAM_OVERVIEW.md`, the current `README.md`, and the repository's `LARGE_FILES.md`. Then read these investigation files, prioritizing the indicated sections:

1. `notes/CCM_BOUNDARY_MECHANICS_AND_DETERMINANT_CONTROL_20260926.md`, Sections 2–3 and 6–7: hypotheses, normalization, determinant criterion, and free-tail scaling.
2. `notes/CCM_ENERGY_PORTS_AND_FIXED_SUPPORT_LIMIT_20260926.md`, Sections 5–8: trace-class mass, conditional fixed-support convergence, and relative-trace target.
3. `notes/CCM_ODD_TAIL_CERTIFICATE_AND_STRUCTURED_SCHUR_20260926.md`, Sections 3–7 and 9, together with `reviews/ODD_TAIL_AND_SCHUR_REVIEW_20260926.md`: exact scope of the tail bound and coupling estimates.
4. `numerics/README.md` and the relevant existing programs before proposing new computations.

Consult the earlier string and chiral notes if needed. Check any external theorem actually used against its primary source and record its hypotheses. In [CCM, Sections 7–8](https://arxiv.org/html/2511.22755v1#S7), distinguish convergence of the prolate-based candidate from the still-missing comparison with the Weil ground state.

## Known state that must remain explicit

L is support length, with \(X=e^L=\lambda^2\); N is Fourier cutoff. The latest rational tail certificate applies only at \(L=\log13\). It proves positivity of the odd high-frequency compression above mode 4096. It does not prove the complete continuum odd gap, even-sector simplicity, the Weil ground-energy sign, or an infinite-L limit.

The finite mechanical pair is
\[
\mathsf M=J^*(W_+-\varepsilon I)J,\qquad
\mathsf K=W_--\varepsilon I,
\]
with the full finite least energy \(\varepsilon\), the prescribed boundary gauge, and the stated finite CCM hypotheses. At fixed L the infinite integrated mass is trace class; determinant convergence remains conditional on a positive odd gap. All hypotheses and shifts must be retained.

A sufficient joint-limit target is a sequence \(L_j,N_j\to\infty\) satisfying those hypotheses, with
\[
\sup_j\tau_{L_j,N_j}<\infty,\qquad
\tau_{L,N}=\operatorname{tr}(\mathsf K^{-1}\mathsf M)
+\frac{L^2}{4\pi^2}\sum_{n>N}n^{-2},
\]
plus an independent arithmetic identification of the normalized spectral functions on a real interval. For the free tail to tend to one, \(L_j^2/N_j\to0\) is sufficient. These requirements alone do not bound the finite arithmetic block's approximation error. Uniformity over every pair \((L,N)\) is not required. A weaker strip-convergence route is admissible if its full criterion and normalization are stated.

## Work to perform

First make an L-dependence ledger. Include the prime/pole bound \(D_L\), inverse differentiation, the integrated mass trace, the unknown odd gap, the high-frequency split and leakage, the coupling coefficient bound, and the free tail. Separate an upper estimate that grows from a proof that the quantity being estimated grows. Do not extrapolate constants certified at log13 to general L.

Next examine **at most two concrete candidate estimates**. The preferred first candidate is a direct bound on the combined mass–stiffness trace, preserving cancellation between the two energy forms. Separate the low-energy contribution and its complement where useful. State any domain, inverse, basis-comparison, and ground-state assumptions. Simply rewriting the trace as a Hilbert–Schmidt norm is not a new estimate. Do not impose a uniform ordinary odd gap unless the argument really needs it.

For each candidate, give a precise inequality, its proposed range of L and N, the role it would play in convergence, and then prove what can be proved or locate the exact missing estimate. If a prolate comparison is used, specify its required norm, normalization, and error relative to the small spectral scales. Do not assume the principal missing CCM comparison under a new name.

Use at most one modest numerical sweep, and only if it can distinguish the proposed mechanisms. Choose support values and cutoffs for that purpose; test Fourier resolution and arithmetic precision separately. Generalize and validate the fixed-13 formulas before using them at other supports. Preserve existing source versions and historical records. Never use zeta-zero fitting as construction input, a difference of Ritz upper bounds as a continuum lower bound, or precision agreement as interval certification.

Finally address the identification step even if the estimates are inconclusive: explain exactly what additional arithmetic theorem would identify the limit with Xi, and whether the proposed route simplifies that obligation. A compact family of unspecified entire functions is not the intended result.

## Completion and decision

Complete this round after the ledger and up to two candidate estimates have been assessed. Save one of the following outcomes with its proper scope:

- A proved estimate with explicit L-dependence and a precise explanation of the part of the limit argument it advances.
- A rigorous obstruction to a specified estimate or mechanism; distinguish that obstruction from failure of the underlying CCM limit.
- An honest unresolved result recording the failed attempts, the exact remaining inequality, and the evidence needed to justify another round. Do not describe inability to prove something as a no-go theorem.

Recommend **continue**, **change approach**, or **suspend this route pending new input**, with reasons. Do not automatically expand into larger fixed-L computations, extra ports, a new geometric realization, or another indefinite continuation. A fixed-L certificate is justified only if you first explain its quantitative role in the growing-support argument.

Save the analysis under `notes/` and a sequential adversarial review under `reviews/`, both dated and with actual model/effort provenance. Label a same-model review honestly. Put any new code and small records in `numerics/`; follow the repository's large-file policy. Update `PROGRAM_OVERVIEW.md`, `README.md`, and the concise `DRAFT_HISTOR.md` only as the findings warrant. Preserve existing uncommitted work, avoid draft snapshots, and do not create a commit or release as part of this round.

The final response should state the decision, the strongest result, the principal remaining obstacle, and links to the saved artifacts. Separate mathematical proof, numerical evidence, and research judgment throughout.
