# Sonin residual: continuation after the CCM closeout

28 September 2026 (America/New_York). Prepared for Edward Baker with LLM assistance. Model: GPT-6 (Codex); the exact serving variant and configured reasoning effort are not exposed. This handoff incorporates separate same-model context and mathematical-scope checks; it is not independent human refereeing.

**Next target.** Audit the existing canonical semilocal Sonin comparison, then use it for one bounded first-prime mechanism test on a precisely stated pole-neutral source class. The objective is a one-sided estimate or an exact place-addition relation that could support positivity on arbitrarily large supports. Another certificate for the already studied finite Weil matrix is not the target.

**Status and authority.** The user has selected Sonin work and temporarily closed CCM. This supersedes earlier instructions to defer Sonin or ask which research option to pursue. Repository baseline: `305806625d1659466f2ba7ff3fed9d496c1a1bc2`, which commits the CCM closeout and the new meta-analysis update. Their references to round 9 as uncommitted describe an earlier working-tree state. This note prepares the next session; no Sonin trace calculation, new positivity interval, or residual sign theorem has been obtained in preparing it.

## 1. What to carry forward from the new assessment

Read the [CCM threshold-obstruction update](CCM_THRESHOLD_OBSTRUCTION_UPDATE_20260928.md), especially Sections 1 and 4–7, alongside Sections 2 and 7 of the [original program review](../reviews/PROGRAM_META_ANALYSIS_20260926.md).

CCM round 8 reduced the remaining question to exclusion of discrete subthreshold spectrum. Round 9 rejected a specific endpoint normalization: exact threshold modes are dense in the bare archimedean energy completion, so absolute relative estimates and bounded endpoint sandwiches fail there. The divergence is on the negative side of a signed comparison operator, while the required inequality is an upper bound. It neither produces a negative Weil vector nor proves a Sonin obstruction.

The transferable lessons are precise:

- State the Hilbert space, form domain, topology, sign and quantifiers of every estimate. A valid physical projection need not be continuous in a weaker energy completion.
- Preserve arithmetic cancellation. An absolute two-sided estimate can be much stronger than the one-sided inequality actually needed.
- Positivity of an independently constructed object is useful only with a proved comparison to the full arithmetic form.
- For the infinite limit, fixed-test convergence of positive approximants is sufficient. Whole-line operator-norm convergence and a uniform strictly positive gap are not requirements of the Weil criterion.

Keep CCM closed during this continuation. Its obstruction is a guide to choosing the Sonin estimate, not a substitute for analyzing it.

## 2. Reading order and recovered source

The relevant materials are:

1. The two meta-analysis references above: the common RH target, the scoped CCM failure, and the proposed Sonin sufficient conditions.
2. [Arithmetic bridge sweep, Sections 2–4 and 13](../../../susy-positivity/investigations/wilson-loewner/notes/ARITHMETIC_BRIDGE_SWEEP_AFTER_YM_20260924.md): the source-class refinement to pole-neutral tests, with a comparison rather than a presumed norm identity.
3. [Arithmetic-storage program and goals, Sections 5–6](../../../susy-positivity/investigations/wilson-loewner/arithmetic-storage/notes/ARITHMETIC_STORAGE_PROGRAM_AND_GOALS_20260924.md), the [post-closure continuation](../../../susy-positivity/investigations/wilson-loewner/arithmetic-storage/notes/RESEARCH_CONTINUATION_AFTER_FIRST_PRIME_CLOSURE_20260924.md), and the [first-prime closure and rigidity note, especially Table 2](../../../susy-positivity/investigations/wilson-loewner/arithmetic-storage/notes/FIRST_PRIME_JOIN_EQUIVALENCE_AND_PRIME_WEIGHT_RIGIDITY_20260924.md). The finite join is already closed internally; do not restart its certificate work.
4. The recovered 14 September **Canonical semilocal pairing and the localized Weil form**, described below. Read Sections 1–5 for the comparison and Sections 6–7 for the cutoff obstruction and validation limits.
5. The primary papers below, with their normalization, support and domain hypotheses retained.

The older comparison was located outside Git at:

`/Users/ebbaker/.codex/.chatgpt-projects/g-p-6a90684bbcb881918a5a1f5740bfbc65/output/semilocal-pairing-comparison-20260914/COMPARISON.md`

Its SHA-256 was checked against the existing provenance record:

`6c1d50c6b53e8f261efcb3d49e43dfa8e8affcb16e816964f054825487b3e12c`

This establishes the identity of the recovered source, not correctness of its claims. It contains a candidate comparison and finite-dimensional algebra checks, but **no evaluated actual Sonin trace**. Its main formulas are restated below so this handoff does not depend on that machine-local path. The next session should save a repository-local audited derivation; if the old file is unavailable, rederive from the cited constructions rather than silently treating the missing artifact as established evidence.

Primary references and limits:

- [Connes–Consani, *Weil positivity and Trace formula, the archimedean place*, v1](https://arxiv.org/html/2006.13771v1): check Theorem 7 and equations (83)–(84) for the proposed calibration. Theorem 1 requires support in `[2^(-1/2), 2^(1/2)]` and transform vanishings at `i/2` and `0`; it does not establish the desired comparison at log-support length 1. Appendix C, Proposition 1 permits prescribed finite Mellin zeros away from the nontrivial zeta zeros in the RH criterion.
- [Connes–Consani–Moscovici, *Zeta zeros and prolate wave operators*, v2](https://arxiv.org/html/2310.18423v2): Sections 4.6–4.8, equation (57) and Theorem 4.6 concern the finite-place maps and stability of Sonin spaces. The older comparison cites v1 Theorem 4.13. The transported metric depends on the places; stability is not isometry or residual positivity.
- [Connes–Consani, *Quasi-inner functions and local factors*](https://arxiv.org/abs/2008.10974): use only the stated operator-class results after checking their hypotheses. Compactness of an off-diagonal block supplies neither its sign nor a trace-class estimate.

## 3. Fix the full target before restricting the sources

Use `I_L=(-L/2,L/2)`, with `f,g` smooth and compactly supported there and zero extensions `F,G`. Inner products are antilinear in the first slot. Set

\[
\widehat F(t)=\int F(x)e^{-itx}\,dx,
\qquad (U_a h)(x)=h(x-a),\qquad
\kappa_{f,g}(a)=\int\overline{F(x)}G(x+a)\,dx.
\]

The reference arithmetic form is

\[
\begin{aligned}
Q_L(f,g)={}&\Gamma_L(f,g)+P_L^{\rm pole}(f,g)\\
&-\sum_{m\log p<L}(\log p)p^{-m/2}
\bigl(\kappa_{f,g}(m\log p)+\kappa_{f,g}(-m\log p)\bigr),
\end{aligned}
\tag{1}
\]

where

\[
\Gamma_L(f,g)=\int_{\mathbb R}
\left(\operatorname{Re}\psi(1/4+it/2)-\log\pi\right)
\overline{\widehat F(t)}\widehat G(t)\,\frac{dt}{2\pi},
\]
\[
P_L^{\rm pole}(f,g)=2\overline{c(f)}c(g)-2\overline{s(f)}s(g),
\quad c(f)=\int F(x)\cosh(x/2)\,dx,
\quad s(f)=\int F(x)\sinh(x/2)\,dx.
\]

The gamma multiplier includes the full scalar contact. No added normalization constant, dropped pole, or omitted active prime power is allowed. At the support boundary `m log p=L`, the correlation is zero for these interior compact tests; document any different endpoint convention used for an extension of the domain.

The preferred RH-directed source class is

\[
\mathcal D_L^0=\left\{f\in C_c^\infty(I_L):
\int e^{x/2}f(x)\,dx=\int e^{-x/2}f(x)\,dx=0\right\},
\tag{2}
\]

with same-support preparation

\[
f=(-\partial_x^2+1/4)h,\qquad h\in C_c^\infty(I_L).
\tag{3}
\]

These conditions eliminate both pole amplitudes. Audit the restricted-test criterion and its coordinate map `g(u)=u^(-1/2)f(log u)` before making an RH implication; the bridge sweep gives the intended application of Appendix C. Zero mean may also be imposed with the corresponding additional Mellin condition. Do not intersect this class with an extra parity restriction without separately proving sufficiency.

Evenness in the original real-place cosine model is different from parity in the additive variable `x=log u`. Retain both additive even and odd tests in exploratory diagnostics. The old Table 2 weak vectors are unrestricted inputs, not automatically elements of (2). Use a new constrained source family, or a controlled smooth approximation and moment correction, and recompute its scales.

## 4. Candidate Sonin comparison to audit

The spaces are different: the arithmetic inputs lie in `L^2(I_L)`, scaling acts on `H=L^2(R,dt)`, and `K=Ran Pi` is the archimedean Sonin space at **cutoff 1** in that representation. The support length `L` is not the Sonin cutoff, and `Pi` is not a finite cosine projection from a Weil certificate.

For the actual projection, use the positive-axis model `L^2(0,infinity;dx)`, the unitary cosine transform

\[
(\mathcal F_\infty h)(x)=2\int_0^\infty\cos(2\pi xy)h(y)\,dy,
\]

and `chi=1_(0,1)`, `R=I-chi`, `C_infinity=chi F_infinity chi`. The recovered equation (12) is

\[
\Pi=R-R\mathcal F_\infty\chi
(I-C_\infty^2)^{-1}\chi\mathcal F_\infty R,
\tag{4}
\]

conjugated to logarithmic coordinates by `h(x) -> e^(t/2)h(e^t)`. This is a bounded projection formula; its separate unsmoothed terms need not have finite traces.

For a finite set `S_f` of finite places, put

\[
D_S=\prod_{p\in S_f}(I-p^{-1/2}U_{\log p}),\quad
G_S=D_S^*D_S,\quad
A_S=(\Pi G_S\Pi)|_{\mathcal K}.
\]

The ordinary orthogonal projection onto `D_S K` and its isometric parametrization are

\[
\Pi_S=D_S\Pi A_S^{-1}\Pi D_S^*,\qquad
J_S=D_S\Pi A_S^{-1/2}:\mathcal K\longrightarrow\mathcal H.
\tag{5}
\]

Inverses are on `K`, extended by zero where surrounded by `Pi`. For fixed finite `S`, both `G_S` and `A_S` lie between `ell_S^2 I` and `u_S^2 I`, where

\[
\ell_S=\prod_{p\in S_f}(1-p^{-1/2}),\qquad
u_S=\prod_{p\in S_f}(1+p^{-1/2}).
\]

These are finite-set invertibility bounds, not uniform all-prime control. Do not omit the inverse compressed metric or commute `Pi` through a translation.

Let `C_F` be convolution by `F`, and `K_(f,g)=C_F^* C_G`. The proposed independently positive pairing is

\[
\mathcal B_S[f]=\|C_F\Pi_S\|_{\rm HS}^2
=\|C_FJ_S\|_{\rm HS}^2\ge0.
\tag{6}
\]

The recovered archimedean calibration and finite-place correction are

\[
\mathcal B_\infty(f,g)=\operatorname{Tr}_{\mathcal K}(\Pi K_{f,g}\Pi)
=\Gamma_L(f,g)+\mathcal E_\infty(f,g),
\qquad
\mathcal E_\infty(f,g)=\int\kappa_{f,g}(t)\epsilon(e^{|t|})\,dt,
\tag{7}
\]
\[
\mathcal B_S=\mathcal B_\infty+\Delta_S,\qquad
\Delta_S(f,g)=\operatorname{Tr}_{\mathcal K}
\left(A_S^{-1}\Pi G_S(I-\Pi)K_{f,g}\Pi\right).
\tag{8}
\]

Here `epsilon` is the archimedean prolate trace-error kernel in the recovered equations (14)–(15), to be calibrated against the primary trace formula, including its sign, normalization and convergence. Do not fit it numerically to force equality.

The inherited candidate identity is

\[
Q_L=\mathcal B_S+\mathcal R_{S,L},
\tag{9}
\]
\[
\begin{aligned}
\mathcal R_{S,L}(f,g)={}&P_L^{\rm pole}(f,g)-\mathcal E_\infty(f,g)-\Delta_S(f,g)\\
&-\sum_{m\log p<L}(\log p)p^{-m/2}
\bigl(\kappa_{f,g}(m\log p)+\kappa_{f,g}(-m\log p)\bigr).
\end{aligned}
\tag{10}
\]

Choose `S_f` to include all active primes. An inactive added place can change `B_S` and `Delta_S` even though it changes no term of (1); their changes must cancel in (9). This is a useful exact control. Equations (7)–(10) are the recovered comparison to audit, not a residual theorem certified by this handoff.

## 5. First gate: trace justification and the actual source class

The old note asserts that `K_(f,g) Pi` is trace class and uses it for cyclicity. Hilbert–Schmidt `C_F Pi` alone does not imply that stronger assertion. Audit what the published smoothing argument establishes. If the stronger assertion is unnecessary, replace it by a proof for the **compressed** products actually used, rather than treating a missing stronger estimate as an obstruction to the program.

A concrete factorization is available on the stated smooth core. Write `V_F=C_F Pi:K->H`, and suppose the calibration supplies Hilbert–Schmidt `V_F,V_G`. The smooth compact kernels define bounded convolution operators, and the bounded translation polynomial `G_S` commutes with `C_F^*`. Consequently,

\[
\Pi G_SK_{f,g}\Pi=V_F^*G_SV_G,
\qquad \Pi K_{f,g}\Pi=V_F^*V_G.
\]

Thus the compressed off-diagonal product has the trace-class factorization

\[
\Pi G_S(I-\Pi)K_{f,g}\Pi
=V_F^*G_SV_G-A_SV_F^*V_G.
\tag{11}
\]

Under these hypotheses, (11) justifies its trace and bounded-factor cyclicity without needing `K_(f,g) Pi` trace class. This elementary repair does not settle the primary calibration or residual sign. State the smooth-core hypotheses explicitly, then justify any extension in the intended form norm; continuity of a full form does not automatically extend every separate trace assertion.

The first deliverable is therefore an audited comparison with a clean domain statement: exact Fourier/Mellin convention, full contact and pole normalization, actual `Pi`, correct adjoints and metric inverse, trace existence, and the legitimate restricted-test RH implication. If that audit encounters a genuine gap, isolate or repair it before proceeding to computation.

## 6. Bounded first-prime test, only after that gate

Start at `L=1`, `S={infinity,2}`, with a small explicitly normalized family from (3). Do not begin by increasing `L` or matrix rank. With `a=log 2`, set

\[
Z=U_a+U_{-a},\quad
T=\tfrac12(\Pi Z\Pi)|_{\mathcal K},\quad \|T\|\le1,
\quad X(f,g)=\Pi Z(I-\Pi)K_{f,g}\Pi,
\quad \beta=2\sqrt2/3<1.
\]

Then `A_2=(3/2)(I-beta T)`. The recovered first-prime formula is

\[
\Delta_2(f,g)=-\frac{\sqrt2}{3}\sum_{n\ge0}\beta^n
\operatorname{Tr}_{\mathcal K}(T^nX(f,g)),
\tag{12}
\]
\[
|\Delta_2-\Delta_2^{(M)}|
\le\frac{\sqrt2}{3}\frac{\beta^{M+1}}{1-\beta}\|X(f,g)\|_1.
\tag{13}
\]

The factorization in Section 5, applied to `Z`, gives the crude smooth-core bound

\[
\|X(f,g)\|_1\le4\|V_F\|_{\rm HS}\|V_G\|_{\rm HS}
=4\sqrt{\mathcal B_\infty[f]\mathcal B_\infty[g]}.
\tag{14}
\]

This supplies a possible existence and truncation bound under the audited hypotheses; it is not a claim of sufficient numerical accuracy. The first numerical plan must also control approximation of the actual Sonin projection, the prolate kernel/error, the trace evaluation, and any source smoothing or moment correction. Give a total error budget at the scale of the chosen normalized inputs, not just the geometric-series tail.

On a diagonal pole-neutral test, report the separate contributions to

\[
Q_1[f]=\mathcal B_2[f]-\mathcal E_\infty[f]-\Delta_2[f]
-\frac{\log2}{\sqrt2}\bigl(\kappa_{f,f}(a)+\kappa_{f,f}(-a)\bigr),
\tag{15}
\]

with enclosures if making a sign claim. Cross-check against direct evaluation of (1), but do not define the computed residual solely by subtracting that answer from `B_2`: the point is to test the canonical arithmetic mechanism.

The unrestricted rigidity benchmarks are useful controls: Table 2 records a certified floor `9.15e-7` at `L=1` and `5.42e-8` at `L=log 3`, with different sensitive additive even and odd directions. With the same normalization, these remain valid lower bounds after restriction to (2), but they do not identify its constrained minimum or weak directions; determine the relevant constrained scales on the chosen family. Use the specified benchmark vectors if reproducing them; frequency labels alone do not identify the inputs. Add one near-`log 3` diagnostic only if the first test or audit makes its purpose clear. Success on a small family is diagnostic evidence, not an all-input inequality.

The internal return series (12) remains infinite. Its factors contain `Pi`, so the support rule that truncates the bare prime correlations does not truncate the returns. The positive `r_2^2 I` in `G_2` belongs to the transported metric; it is not an extra positive contact term in `Q_1`.

## 7. What would make this a route beyond finite support

The next structural question is a law for the **complete residual** under adjoining a place, with the compressed metric retained. The easy identity

\[
D_{S\cup\{p\}}=(I-p^{-1/2}U_{\log p})D_S
\]

is only its starting point. Compression and inversion do not turn it into a residual sign or monotonicity law. For primes 2 and 3 the metric already has mixed shifts `log 6` and `log(3/2)`; these are metric terms, not replacements for the arithmetic prime-power list. Increasing the support past `log 6` also crosses the Weil labels 3, 4 and 5; 6 itself is not a prime power and has no direct Weil summand. A place-addition analysis must account for powers of already included primes and all intervening arithmetic terms.

A useful structural result would provide at least one of the following, with explicit source and support quantifiers:

- `R_(S,L)[f]>=0`, a strong sufficient comparison.
- `R_(S,L)[f]>=-eta_(S,L) B_S[f]`, with `eta_(S,L)<=1`, on the required entire source class for an unbounded nested family of supports. No uniform strict margin below 1 is required; null directions must be included.
- Independently positive forms `P_j` for which, for every fixed admissible compact smooth `f`, eventually in their domains, `P_j[f]->Q[f]`; or `Q[f]>=P_j[f]-epsilon_j(f)` with `epsilon_j(f)->0`. Specify how finite places, support and projection resolution are chosen for that fixed test and prove the arithmetic limit.

The desired one-sided comparison is equivalent to the original sign question if merely rewritten as `R>=-B`. Progress requires additional usable structure: an exact signed identity, a controllable off-diagonal estimate, an induction stable under adjoining places, or a convergence theorem that does not assume Weil positivity. A changing finite-set metric with deteriorating constants is not by itself an infinite-limit argument.

## 8. Traps and decision rules

- **Compact is not Hilbert–Schmidt.** The recovered one-prime small-cutoff transform is compact but not Hilbert–Schmidt; its finite-return squared Hilbert–Schmidt norms grow linearly. Audit that calculation before relying on it, and do not copy an unsmoothed prolate square trace or subtract infinite traces. This does not invalidate the correctly smoothed pairing (6), and it is not the same operator as the finite-response boundary obstruction.
- **A model projection is not the test.** A fitted positive matrix, an oblique transported projection, or a finite cosine cutoff with no proved Sonin approximation cannot validate (9).
- **The sign matters.** Residual negativity alone does not imply `Q<0`; it may be compensated by `B`. Failure of a stronger proposed estimate refutes that estimate. In contrast, a genuinely validated `R<-B` on an admissible test, with exact (9), would give `Q<0`; it cannot be dismissed as merely failure of this decomposition. Audit normalization, domains and errors before interpreting any such result. This qualification corrects the overly broad stop wording in the earlier bridge sweep.
- **Do not assume the conclusion.** No square root defined by first assuming `Q>=0`, no unconditional sum of squares over supposedly real zero ordinates, and no use of RH to justify a source or projection approximation.
- **Do not demand unnecessary uniformity.** Avoid importing the failed CCM absolute endpoint estimate, or requiring a uniform positive gap, when a one-sided or fixed-test argument would suffice.

At the end of one bounded session, choose a concrete outcome: an audited identity and useful signed mechanism; a specific estimate with a justified next lemma; or a precisely scoped obstruction/domain gap. If the work yields only generic Gram positivity, another finite Weil certificate, or numerical cancellation without a controlled limit, document that limitation and stop that particular extension. Do not turn lack of progress in one estimate into an impossibility claim about the whole Sonin program.

## 9. Next-session outputs and opening instruction

Save incremental research in the existing [arithmetic-storage notes directory](../../../susy-positivity/investigations/wilson-loewner/arithmetic-storage/notes/), computations in its `numerics/`, and critical assessments in its `reviews/`. A folder migration, new manuscript, or new draft snapshot is unnecessary. Follow the root large-files policy; retain only small source/parameter/error records in Git. Include author/LLM provenance and the actual available model/effort metadata. Update the relevant overview when there is a result; no commit or push is requested by this handoff.

The first session should leave:

1. A repository-local audit of (7)–(10), including either the compressed-product proof (11) or a precise replacement, and a verified source-class statement.
2. If the audit passes and a credible total error budget is available, one bounded actual-Sonin first-prime diagnostic with reproducible small inputs and records. Otherwise, an exact account of the missing analytic estimate instead of an uncontrolled calculation.
3. A short critical review stating whether the evidence supports a one-sided bound or a place-addition law, what remains unproved for arbitrary supports, and the next single lemma worth attempting.

**Opening instruction for the new session:** Continue the Sonin residual program from this note. Keep CCM temporarily closed and preserve the completed first-prime Weil certificates. First audit the recovered canonical comparison on smooth compact inputs, including the compressed trace-class factorization, the archimedean calibration and the pole-neutral RH criterion. Then, only if the analytic and error-control gates pass, evaluate the actual Sonin residual on one stated pole-neutral first-prime source family at `L=1`. Seek a signed mechanism or a place-addition estimate with explicit relevance to fixed-test/infinite-support positivity. Save the audited derivation and a critical assessment even if the numerical stage is not justified. Do not substitute further finite-`L` certificates for that missing mechanism.
