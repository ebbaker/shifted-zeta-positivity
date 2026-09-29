# New-session continuation: the CCM threshold index target

Prepared 28 September 2026 for Edward Baker with LLM assistance. Preparation model: GPT-6 (Codex); exact serving variant and configured reasoning effort are not exposed. **Status: executed in round 9 on 28 September 2026.** This file preserves the original scope. Results and the revised decision are in [the threshold energy analysis](CCM_THRESHOLD_ENERGY_OBSTRUCTION_20260928.md) and [sequential review](../reviews/CCM_THRESHOLD_ENERGY_REVIEW_20260928.md). The bounded endpoint-energy mechanism is obstructed; the one-sided sharp inequality remains open.

## Task and scope

Continue the CCM investigation in `/Users/ebbaker/Documents/shifted-zeta-positivity/papers/investigations/ccm-operator-realizations` with a bounded analytic investigation of the **one-negative-direction target at the weighted spectral threshold**. The immediate purpose is to find and test an estimate that remains useful as the spectral depth tends to zero. Another fixed-depth reformulation or finite-L calculation is not enough.

The sharp statement is RH-equivalent. A complete proof is not an assumed outcome of this session. A useful partial theorem, a rigorous obstruction to a specified mechanism, or a precise unresolved estimate with a justified next decision is an acceptable completed result. Keep Sonin residuals deferred. Do not restart the completed finite-support certificate, string-port experiments, or round-5 audit.

The committed baseline containing round 8 is `8eaabbf5ab409422827013b6bc83ad0c1bbb92bc` ("Broad project overview and work on CCM analysis"). Inspect the actual current checkout before editing; this identifier is a provenance reference, not an instruction to reset or discard later work. The handoff and overview refresh were prepared after that commit.

## Read first, in this order

1. [Program overview](../PROGRAM_OVERVIEW.md) and the repository [large-file policy](../../../../LARGE_FILES.md).
2. [Round-8 synthesis](CCM_WEIGHTED_TAIL_AND_DISCRETE_OBSTRUCTION_20260928.md), especially Sections 3–6: exact weighted operator, controlled arithmetic tail, and compact counting target.
3. [Weighted operator proof](CCM_WEIGHTED_OPERATOR_SPECTRAL_REDUCTION_20260928.md), Sections 2–7: closed domain, local and relative compactness, essential edge, localization, and signed Birman–Schwinger count.
4. [Round-8 critical review](../reviews/CCM_WEIGHTED_TAIL_REVIEW_20260928.md).
5. [Round-7 complement and weighted-gap note](CCM_COMPLEMENT_DENSITY_AND_WEIGHTED_GAP_20260928.md), Sections 2–6, for the negative-complement obstruction, limit order, exact weighted identity, and finite-prime zero-gap theorem.

Consult the [prime-return proof](CCM_PRIME_RETURN_AND_EXTERIOR_COERCIVITY_20260928.md) if an aggregate prime-rate estimate is needed. The [bounded rate diagnostic](../reviews/CCM_PRIME_RETURN_DIAGNOSTIC_20260928.md) is supporting evidence, not an eigenvalue-count certificate. Read the older ground-selection and determinant notes only when a proposed argument actually uses their results. Check any external theorem newly invoked against a primary source, including its domains and hypotheses.

The inherited results are analytic working proofs checked by parallel agents of the same model family, not independently refereed theorems. Audit the inputs needed by the chosen mechanism; if a material gap appears, repair or delimit it before building on it.

## Exact starting object

Use the literal positive even theta kernel

\[
k(x)=e^{x/2}\sum_{n\ge1}\frac\pi2(ne^x)^2
\bigl(2\pi(ne^x)^2-3\bigr)e^{-\pi(ne^x)^2},
\qquad \widehat k=\Xi/4.
\]

Set

\[
m(x)=k(x)\cosh(x/2),\quad d\mu=m(x)dx,
\quad M=\mu(\mathbb R)=\tfrac18,\quad s=2M=\tfrac14.
\]

J denotes the closed positive gamma-plus-full-prime jump operator on the **even** space \(L^2(\mu)^+\). It is not the inverse-differentiation map denoted J in the older mechanical notes. With \(Uu=\sqrt m\,u\) and \(a=\sqrt{k/\cosh(x/2)}\), round 8 establishes the closed-form identity

\[
H:=UJU^{-1}=sI+A_0-K,
\qquad A_0=M_a(g(D)+6)M_a,
\]
\[
g(t)=\Re\psi(1/4+it/2)-\log\pi>-6,
\qquad K=6M_{a^2}+P_a,
\]
\[
P_a=\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
M_a(T_{\log n}+T_{-\log n})M_a,
\quad T_\ell v(x)=v(x+\ell).
\tag{1}
\]

A_0 is defined by its nonnegative form, with domain

\[
\mathcal V=\{v\in L^2(dx)^+:av\in H_{\log}\},
\quad \|w\|_{H_{\log}}^2
=\int(1+\log(2+|t|))|\widehat w(t)|^2dt.
\tag{2}
\]

Compact smooth even functions are a core. K is bounded and self-adjoint, and relatively form compact with respect to A_0. K is generally signed and is not claimed compact on ordinary L2.

The known normalized zero mode is

\[
v_0=\sqrt m/\sqrt M,\qquad Hv_0=0.
\]

The inherited conclusions are

\[
H\ge0,\quad \ker H=\operatorname{span}\{v_0\},
\quad \inf\sigma_{\mathrm{ess}}(H)=s.
\tag{3}
\]

Spectrum in (0,s), if present, is discrete and may accumulate only at s. There is an unspecified positive gap above zero. The known threshold eigenfunctions are

\[
u_j=k^{(2j)}/k-4^{-j},\quad Ju_j=s u_j,\quad j\ge1.
\tag{4}
\]

Their closed span is infinite dimensional. It has not been shown to exhaust the threshold eigenspace or the even mean-zero space.

## Target, with the quantifiers retained

The desired one-negative-direction statement is

\[
\langle v,(A_0-K)v\rangle\ge0
\quad\text{for every }v\in\mathcal V\cap v_0^\perp.
\tag{5}
\]

Pairings involving A_0 in (5) mean its closed quadratic form. Since \((A_0-K)v_0=-s v_0\), (5) says that H−s has negative index exactly one. Equivalently, in form sense,

\[
K\le A_0+s|v_0\rangle\langle v_0|.
\tag{6}
\]

These are target inequalities, **not established estimates**. They are equivalent to no spectrum of J in (0,s), hence to RH through the compact even Weil criterion. They do not imply the additional ground-profile and determinant-convergence statements required by the original CCM program without further work.

For a fixed spectral energy \(0<E<s\), let \(\delta=s-E\) and

\[
\mathcal T_E=(A_0+\delta I)^{-1/2}
K(A_0+\delta I)^{-1/2}.
\tag{7}
\]

E is an energy, not the support parameter lambda>1 of CCM. This compact self-adjoint operator satisfies the signed inertia identity

\[
N(H<E)=n(\mathcal T_E>1).
\]

The equivalent target is

\[
\boxed{\ n(\mathcal T_E>1)=1
\quad\text{for every }0<E<1/4.\ }
\tag{8}
\]

Counts are strict and include multiplicity. The known zero mode guarantees one count for E>0; it is generally **not** an eigenvector of T_E. A fixed-depth certificate, or finitely many E values, leaves the endpoint issue unresolved.

## Estimates already available

For each fixed \(0<c<\pi/2\), a finite C gives \(a(x)\le C e^{-c e^{2|x|}}\). In particular,

\[
\|P_a-P_{a,\le P}\|
\le2C^2\sum_{n>P}\frac{\log n}{\sqrt n}e^{-2cn}.
\tag{9}
\]

Round 8 also supplies explicit exterior and localization errors d_R,e_R tending to zero superexponentially. A normalized eigenfunction u with eigenvalue at most s−delta obeys

\[
\|1_{|x|\ge R+1}u\|_\mu^2
\le\frac{e_R}{\delta-d_R},\qquad d_R<\delta.
\tag{10}
\]

For a bounded approximation K_N to K,

\[
\|\mathcal T_E-(A_0+\delta I)^{-1/2}K_N(A_0+\delta I)^{-1/2}\|
\le\|K-K_N\|/\delta.
\tag{11}
\]

There is no assumption that K_N is finite rank. Finite-rank approximation is guaranteed for T_E; no such ordinary operator-norm approximation of K is supplied here.

These inputs make fixed-depth analysis possible. They do not supply a sharp bound on the second count in (8), an inverse for A_0 at delta=0, or a compact endpoint operator T_s.

## Work to perform

**First select one concrete mechanism for (5) or (8).** Prefer a form comparison or factorization retaining the signed prime translations, or a rigorously defined reduction that removes the known mode and treats the threshold eigenspace before taking delta to zero. State the exact missing inequality, its domain, and its endpoint quantifier before computing. Merely deriving (5)–(8) again is not the task.

Handle the known mode on the H side, where v_0 is an exact reducing eigenvector, or derive the correct congruence/Schur removal on the Birman–Schwinger side. Do not apply naive orthogonal deflation by v_0 to T_E. If using the known threshold span, distinguish that closed span from the complete eigenspace; do not assume its completeness or a positive gap on its complement.

Make a short endpoint error ledger: prime cutoff, spatial restriction, frequency resolution, coupling/deflation, and any projection onto threshold modes. For every term record its dependence on delta and which cancellations it preserves. Explain whether proposed choices P(delta), R(delta), and a frequency cutoff actually control an inertia count, rather than just converge for each fixed test. Do not assume positive-operator monotonicity of T_E from its signed K; justify whatever comparison is used.

Develop this mechanism until it yields a useful estimate or an identifiable obstruction. If a second mechanism offers a genuinely different way to address that obstruction, examine at most one alternative. Do not expand into an open-ended list of equivalent formulations.

Use no new numerical sweep by default. One bounded diagnostic is appropriate only after specifying which analytic alternatives it distinguishes and how spatial, frequency, prime-tail, and precision errors will be separated. Never use a finite Ritz calculation as a continuum lower bound, zero fitting as construction input, or multiprecision agreement as interval certification.

## Traps that must remain visible

- The essential lower edge s excludes an essential subthreshold branch, not discrete eigenvalues just below s; the whole essential spectrum has not been identified.
- Infinite exact threshold multiplicity does not justify a finite-dimensional separation estimate or a uniform inverse at the endpoint.
- Fixed-support density of derivative restrictions does not establish whole-line weighted completeness. Fixed-rank positivity as support grows holds even if RH fails.
- Individual weighted shifts are generally noncompact on L2; relative compactness uses the logarithmic form domain.
- Truncating P_a while retaining the exact full diagonal in (1) is norm controlled. Truncating positive prime jump energies deletes their long-jump diagonal as well and has gap zero.
- Localizing eigenfunctions at each fixed delta does not give one bounded region controlling all possible shallow modes as delta tends to zero.
- The Xi/4 normalization and mass 1/8 must stay consistent. The sharp gap is an RH-equivalent target, not an available comparison input.

## Deliverables and completion rule

Save a dated analysis in `notes/` and a sequential adversarial review in `reviews/`, with actual model/effort provenance and an explicit LLM acknowledgement. Label same-model review honestly. Use the session's actual date. Put any new programs and small records in `numerics/`; retain no dense matrices or third-party PDFs and follow LARGE_FILES.md. Preserve existing files and uncommitted work. The ChatGPT mirror's `sources/` files are read-only.

Finish this bounded round with one of: a proved estimate advancing the endpoint problem; a rigorous obstruction to the chosen mechanism; or an unresolved result identifying the exact missing inequality and what new input would make further work worthwhile. A fixed-depth theorem can be useful, but label it as such and state the remaining endpoint obligation. Do not claim a general impossibility result merely because a sufficient estimate fails.

Update the overview, README, and concise `DRAFT_HISTOR.md` only as findings warrant. No manuscript snapshot is needed. Do not commit, push, create another chat, or switch to Sonin residuals as part of these instructions. Conclude with a decision to continue, change approach, or suspend this particular route pending specified input, and link the saved findings.
