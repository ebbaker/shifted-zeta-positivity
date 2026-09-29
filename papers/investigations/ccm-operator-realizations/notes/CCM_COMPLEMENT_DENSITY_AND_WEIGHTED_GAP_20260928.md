# Complementary-space obstruction, a derivative form core, and the weighted Xi transform

28 September 2026. Prepared for Edward Baker with LLM assistance. Model: GPT-6 (Codex); exact serving variant and configured effort are not exposed to this agent. Analytic working derivation, not formal verification or independent human refereeing. No numerical sweep was used for this analytic derivation. The repository LARGE_FILES policy was read; this small note contains no derived numerical archive.

## 1. Inputs and notation

Write `I_b=[−b,b]`, and let `A_b=W^+_{2b}` be the original, **unshifted** even Weil operator on this interval, defined by its closed form. It has compact resolvent and is bounded below for each fixed b. Its bottom is `ε_b`. The argument concerns this continuum operator, not an inadequately resolved Fourier matrix.

Inputs established in the preceding working notes are:

* The real, even, strictly positive Xi kernel k and each fixed translate or derivative are unconditional annihilators of the full Weil form Q. This is a distributional/weighted-test-space statement; no bounded whole-line L2 operator is presumed.
* Compact cutoffs of any fixed finite independent family of these profiles have all-input operator residual tending to zero superexponentially as b increases. Their Gram matrices converge to nonsingular whole-line Gram matrices. Their form entries equal pairings of the omitted tails.
* RH is equivalent to positivity of every compact even test. More explicitly, an off-axis Xi zero produces a compact smooth even negative witness. Consequently `ε_b` is nonincreasing, tends to zero under RH, and is at most a fixed negative number for all sufficiently large b if RH fails.

See [the preceding selection note](CCM_NEAR_NULL_CLUSTER_AND_GROUND_SELECTION_20260928.md), Sections 2–6, for the weighted-space and negative-witness arguments; see [the hard-truncation residual note](CCM_XI_ANNIHILATOR_AND_BOUNDARY_RESIDUAL_20260928.md), Sections 3–5, for the stronger hard-cutoff estimate. The underlying explicit formula and finite operator realization are in [CCM, Sections 3 and 5](https://arxiv.org/html/2511.22755v1#S3). The deductions below do not assume RH.

**Normalization correction.** Here k uses the literal theta coefficient in the preceding residual note,

\[
k(x)=e^{x/2}\sum_{n\ge1}h(ne^x),\qquad
h(u)=\frac\pi2u^2(2\pi u^2-3)e^{-\pi u^2}.
\]

Its Fourier transform is `Xi/4`, not Xi. Direct Gaussian integration gives

\[
\int_0^\infty h(u)u^{s-1}du
=\frac{s(s-1)}8\pi^{-s/2}\Gamma(s/2).
\]

Mellin summation, initially for `Re s>1`, gives `ξ(s)/4`; analytic continuation and the functional equation give the Fourier identity. Thus `∫k=Xi(0)/4` and `M=∫k cosh(x/2)dx=ξ(1)/4=1/8`. Annihilation, Rayleigh quotients and normalized-profile statements in the preceding notes are unaffected by this scalar correction. Section 5 keeps M visible and then substitutes its value.

## 2. Removing a near-null trial space leaves the negative spectrum intact

This is a bounded-perturbation statement, not a formal invocation of a Schur complement.

**Proposition 1.** Let A be a self-adjoint, bounded-below operator with compact resolvent on a Hilbert space. Let `S⊂Dom A` be finite dimensional, P its orthogonal projection, and `P⊥=1−P`. Define D to be the self-adjoint operator associated with the restriction of the closed form of A to `S⊥`. Put

\[
r=\|AP\|=\sup_{s\in S,\ \|s\|=1}\|As\|.
\]

Then

\[
\boxed{\ \|A-(0_S\oplus D)\|\le 2r\ },                 \tag{1}
\]

where the difference is a bounded finite-rank operator and the two unbounded operators have the same domain. In particular, for nonzero S,

\[
\boxed{\ \left|\inf\sigma(A)-\min\{0,\inf\sigma(D)\}\right|\le2r\ }. \tag{2}
\]

**Proof.** Since `S⊂Dom A`, P preserves `Dom A` and AP is bounded. In the orthogonal decomposition `S⊕S⊥`,

\[
A=\begin{pmatrix}H&C^*\\C&D\end{pmatrix},\qquad
H=PAP,\quad C=P^\perp AP.
\]

The lower-right domain is `Dom A∩S⊥`: the finite-rank off-diagonal terms are bounded, so subtracting them reduces A to a self-adjoint block diagonal operator; equivalently this identifies the operator represented by the restricted form. The difference in (1) is `AP+PA P⊥`. Its summands have norm at most r, since `PA P⊥=(P⊥AP)^*`. The variational principle gives (2). The same bounded-perturbation estimate applies to all ordered eigenvalues, counting the zero block with its finite multiplicity. ∎

There is also a direct negative-test estimate. If `f∈Dom A` and `g=P⊥f`, then

\[
\big|Q(g,g)-Q(f,f)\big|\le3r\|f\|^2.                  \tag{3}
\]

Expand `Q(f−Pf)` and use `|⟨f,APf⟩|≤r||f||||Pf||` and `|⟨Pf,APf⟩|≤r||Pf||²`. Thus if `Q(f,f)≤−δ||f||²` and `3r≤δ/2`, the nonzero g lies in the complement and has Rayleigh quotient at most `−δ/2`.

**Application.** Suppose the arithmetic trial spaces `S_b` satisfy `r_b=||A_b|S_b||→0`. They may have increasing rank if this all-input bound is proved uniformly. If RH fails, the same compact even negative witness can be used at every sufficiently large b. Equation (3) proves

\[
\inf\sigma(D_b)\le-\delta/2
\quad\text{eventually}.                               \tag{4}
\]

So removing a space made exclusively of sufficiently accurate near-null modes cannot remove an actual negative ground branch. This remains true even when the rank grows. No assertion of uniform residual control as rank grows is supplied merely by fixed-rank tail estimates.

For fixed independent whole-line annihilators there is an equivalent limiting explanation: subtract the whole-line L2 projection of f onto their span. The form value stays exactly `Q(f,f)`, because every subtracted profile lies in the radical. After compact cutoff and the small correction needed for exact finite-window orthogonality, a strictly negative test remains in the complement. Equation (3) is stronger and avoids tracking those coefficients.

One may weaken a proposed positive complement gap to the following precisely sufficient condition:

\[
r_{b_j}\longrightarrow0,\qquad
D_{b_j}\ge-\eta_j I,\qquad \eta_j\longrightarrow0
\quad (b_j\to\infty).                                 \tag{5}
\]

Equation (2) gives `ε_bj≥−η_j−2r_bj`; an explicit near-null vector gives `limsup ε_bj≤0`. Hence (5) implies RH. Conversely RH makes every D_b nonnegative. Thus for any prescribed family with `r_b→0`, proving a vanishing lower floor for its complement along a cofinal sequence is already an RH-equivalent task. It is a valid target, but positivity of the small arithmetic trial matrix does not make that target easier by itself.

## 3. Any fixed-rank complement still has arbitrarily many near-zero modes

**Proposition 2.** Fix integers m≥0 and j≥1. Let `S_b⊂Dom A_b` be any spaces of rank at most m. They need not consist of annihilators and their orientation may vary with b. Let D_b be their form compressions. Then for sufficiently large b, D_b has at least j eigenvalues in

\[
[-2\epsilon_{m+j}(b),\ 2\epsilon_{m+j}(b)],\qquad
\epsilon_{m+j}(b)\to0,                                \tag{6}
\]

where the rate is the fixed-family superexponential residual rate from the preceding selection note.

**Proof.** Choose m+j fixed independent even translates or derivatives of k and their smooth compact cutoffs. Their span T_b has dimension m+j and satisfies `||A_b t||≤ε_(m+j)(b)||t||`. Dimension counting gives `dim(T_b∩S_b⊥)≥j`. For every t in this intersection, t belongs to `Dom D_b` and `D_b t=P_b⊥A_b t`, so its D_b residual is at most the same bound. If the spectral projection of D_b onto the interval in (6) had rank less than j, some nonzero vector of the intersection would lie in its orthogonal complement, contradicting the spectral theorem. ∎

Under RH, D_b is nonnegative, and each of its fixed-index eigenvalues tends to zero. Therefore **no fixed-rank arithmetic trial space can have a complement with a uniform positive gap**. Without RH, (6) is still a near-zero cluster statement; a negative branch may sit below it. It would be incorrect to replace this statement by a claim that the j-th ordered eigenvalue tends to zero without first excluding negative branches.

These results do not rule out a gap measured relative to an even smaller trial energy or residual. They do rule out treating the remainder after two or any other fixed number of profiles as a uniformly coercive positive high-energy space.

## 4. At fixed support, all even derivatives are a form core

This establishes the missing second limit rigorously. Use **hard restrictions** here:

\[
S_{m,b}=\operatorname{span}\{1_{I_b}k,1_{I_b}k'',\ldots,
1_{I_b}k^{(2m-2)}\}.
\]

The form-domain statement does not automatically hold for a smooth cutoff that vanishes on a nonempty outer strip: all such trial functions miss that strip.

Let

\[
\mathcal V_b=\left\{f\in L^2(\mathbb R):
\operatorname{supp}f\subset I_b,\quad
\int_{\mathbb R}(1+\log(2+|t|))|\widehat f(t)|^2dt<\infty\right\}.
\tag{7}
\]

The even Weil form domain is `V_b^+`. Its shifted form norm is equivalent to (7): the gamma symbol differs from `log(2+|t|)` by a bounded function, while the finitely many local prime shifts and the local pole term are bounded on L2. Hard restrictions of smooth functions lie in V_b, because their Fourier transforms are O(1/|t|).

First, `C_c∞((−b,b))` is dense in V_b. Inward dilation `f_r(x)=f(x/r)`, r↑1, is strongly continuous in the logarithmic Fourier norm and has support in `[−rb,rb]`. Strong continuity follows first for Schwartz functions, then by density and the uniformly bounded ratio of the weights at t and rt for r near 1. Convolution with a smooth approximate identity of radius less than `(1−r)b` then gives compact smooth approximants and converges in the same norm. Even approximants preserve parity.

**Proposition 3.** For each fixed b>0, the union of S_m,b is dense in `V_b^+` in form norm.

**Proof.** Let ℓ be a continuous linear functional on `V_b^+` which annihilates every `1_I k^(2j)`. For a smooth function φ near I_b define the even compact-support distribution

\[
T(\phi)=\ell\!\left(1_{I_b}\,\frac{\phi(x)+\phi(-x)}2\right).
\]

This is a distribution because the map `φ↦1_I φ` is continuous from C1(I) into V_b: its L1 norm and total variation bound its Fourier transform by `C min(1,1/|t|)`. It is supported in I_b. Consider

\[
F(a)=T\big(k(\cdot-a)\big).
\]

The theta series for k is holomorphic in the connected strip `|Im a|<π/4`, locally uniformly with all derivatives on the compact x support of T; hence F is holomorphic there. All even derivatives of F at 0 vanish by the hypothesis on ℓ, and all odd derivatives vanish by parity. Therefore F vanishes on the strip and in particular on the real axis. Fourier transformation of the tempered convolution gives `hat T(t) Xi(t)=0` (up to the harmless normalization of k). The Fourier transform of the compact-support distribution T is entire. Xi is nonzero on a real interval, so `hat T` vanishes there and then identically. Thus T=0. In particular ℓ vanishes on even compact smooth functions; their established form density implies ℓ=0. Hahn–Banach proves the claim. ∎

Let `ρ_m(b)=inf_{0≠f∈S_m,b} Q(f,f)/||f||²`. Proposition 3 and min–max give

\[
\lim_{m\to\infty}\rho_m(b)=\epsilon_b
\quad\text{for every fixed }b.                         \tag{8}
\]

For each fixed m, the exact omitted-tail identity and convergence of the Gram matrix give

\[
\lim_{b\to\infty}\rho_m(b)=0                           \tag{9}
\]

unconditionally. Independence follows because the Fourier transforms are Xi times distinct even monomials; restriction does not create a dependence, by analyticity. The tail form convergence can be obtained with hard-cutoff BV estimates, as in the residual note, or by comparing hard and smooth cutoffs whose difference remains in the superexponentially small outer tails. Fixed higher derivatives contribute only fixed polynomial factors to those bounds.

Thus the two iterated limits are

\[
\lim_{m\to\infty}\lim_{b\to\infty}\rho_m(b)=0,
\qquad
\lim_{b\to\infty}\lim_{m\to\infty}\rho_m(b)
=\lim_{b\to\infty}\epsilon_b.                          \tag{10}
\]

The second limit is zero under RH and is strictly negative or −∞ if RH fails. This is a genuine limit-order trap. Excellent fixed-rank asymptotics, including unconditional Xi selection in a small trial matrix, cannot justify interchanging these limits.

The parallel [boundary note, Section 7](CCM_DERIVATIVE_BOUNDARY_SELECTION_20260928.md) proves more: every fixed derivative rank has an eventually positive-definite form, using an adapted Vandermonde jet basis and a positive limiting polynomial moment matrix. Combining that separately checked result with Proposition 3 gives an exact conditional consequence. If RH fails, the least rank `m_−(b)` for which `ρ_m(b)<0` is finite for every sufficiently large b, yet `m_−(b)→∞` as b grows. Thus negativity, if present, escapes every fixed derivative rank. This does not prescribe the growth rate of the rank needed to see it.

An all-rank version also clarifies the obstruction: at a fixed b, if `||A_b|S_m,b||` stayed bounded by a common r for every m, form density would force A_b to extend to a bounded operator of norm at most r. The logarithmic archimedean operator is unbounded. Therefore the all-input residual constants necessarily deteriorate with rank at fixed b. A simultaneous m,b theorem must quantify that deterioration rather than extrapolate fixed-rank estimates.

## 5. The positive-k transform gives an exact signed-jump obstruction

This offers a concrete alternate formulation of the missing inequality. It does not supply that inequality.

Away from the origin the Weil convolution distribution has gamma kernel `−H(|s|)`, where

\[
H(s)=\frac{e^{-s/2}}{1-e^{-2s}},\quad s>0,
\]

prime atoms `−q_n(δ_(log n)+δ_(−log n))`, with `q_n=Λ(n)/sqrt n`, and pole kernel `2cosh(s/2)`. Contact terms at zero disappear when multiplied by a squared difference.

For a smooth compact u, apply the annihilation `Q(k,k|u|²)=0` and symmetrize. It gives

\[
Q(ku,ku)=-\frac12\iint \mathcal W(x-y)k(x)k(y)
|u(x)-u(y)|^2\,dx\,dy.                                \tag{11}
\]

Distributional regularization at the diagonal is legitimate because the squared difference vanishes quadratically; alternatively truncate the gamma kernel away from the diagonal and pass to the limit. Define the positive energies

\[
\mathcal E_\Gamma(u)=\frac12\iint H(|x-y|)k(x)k(y)
|u(x)-u(y)|^2\,dx\,dy,
\]

\[
\mathcal E_p(u)=\sum_{n\ge2}q_n\int k(x)k(x+\log n)
|u(x+\log n)-u(x)|^2\,dx,
\quad\mathcal E=\mathcal E_\Gamma+\mathcal E_p.
\tag{12}
\]

Every integral and sum is finite for compact smooth u, using the superexponential kernel tails. Put

\[
d\mu=k(x)\cosh(x/2)\,dx,\quad
d\nu=k(x)\sinh(x/2)\,dx,\quad
M=\mu(\mathbb R)>0,\quad
\bar u=M^{-1}\int u\,d\mu.
\]

Using `cosh((x−y)/2)=cosh(x/2)cosh(y/2)−sinh(x/2)sinh(y/2)` and `ν(R)=0`, (11) becomes

\[
\boxed{\ Q(ku,ku)=\mathcal E(u)
-2M\int|u-\bar u|^2d\mu
-2\left|\int u\,d\nu\right|^2\ }.                     \tag{13}
\]

For even u the last term vanishes. Since k is strictly positive, multiplication by k maps even compact smooth functions bijectively to themselves. The compact-even criterion therefore gives the exact equivalent target

\[
\boxed{\quad\mathrm{RH}\iff
\mathcal E(u)\ge2M\int|u-\bar u|^2d\mu
\quad\text{for every even compact smooth }u.\quad}     \tag{14}
\]

Thus the gamma and prime parts become positive jump energies, but the poles become a nontrivial variance subtraction. Positivity of k and positivity of the jump conductances do not prove the sharp weighted Poincaré inequality (14). This identifies exactly what a ground-state-transform argument still owes.

The sharp threshold is itself infinitely degenerate. Define, for j≥1,

\[
u_j(x)=\frac{k^{(2j)}(x)}{k(x)}-4^{-j}.                 \tag{15}
\]

Integration by parts gives `∫k^(2j)(x)cosh(x/2)dx=4^−j M`, so every u_j has μ-mean zero. These are independent and belong to L2(μ). They also have finite energy (12): their ratios and first derivatives grow at most exponentially for each fixed j, while k decays superexponentially. For the prime sum, the exponential-weighted overlap estimate bounds the cross terms by any prescribed power of n^−1; for the gamma term, smoothness handles the diagonal and the same tails handle infinity. Smooth compact cutoffs converge in L2(μ) and energy, justifying all following pairings.

Polarize (13), take a compact even v, and use the radical property of `k u_j=k^(2j)−4^−j k`. It follows that

\[
\mathcal E(u_j,v)=2M\langle u_j,v\rangle_{L^2(\mu)}.    \tag{16}
\]

One can define the positive jump operator by closing (12) on even L2(μ), initially on smooth compact functions; the preceding approximation puts constants and the u_j in that closure. Equation (16) makes each u_j an eigenfunction at 2M. Constants give the eigenvalue zero. Thus the positive jump operator has an explicit infinite-dimensional eigenspace at the threshold 2M, unconditionally. The unresolved question is whether its mean-zero even sector has spectrum **below** that threshold. This is exactly (14), hence RH; it is not settled by exhibiting the threshold eigenfunctions.

For this literal theta normalization, the threshold is `2M=1/4`. Consistently rescaling k changes this numerical spectral value and the reference measure, while leaving (14) invariant.

For completeness, closability here is elementary. The continuous jump measure and every prime-shift jump measure give zero mass to pairs having either coordinate in a μ-null set. An L2(μ)-convergent sequence has an almost-everywhere-convergent subsequence, hence its differences converge almost everywhere for the summed jump measure. Fatou's lemma proves closedness of the maximal finite-energy form and closability of its smooth compact restriction. For smooth cutoffs of u_j, the prime-energy error is bounded by exponential-weighted overlaps of `k|tail(u_j)|²` with k, tending to zero and summable over n. Away from the gamma diagonal dominated convergence applies; near the diagonal weighted derivative tails bound the squared difference and tend to zero. The same argument, simpler, puts constants in the core closure. These facts justify the operator eigenfunction interpretation of (16).

## 6. Every finite-prime truncation of the positive jump form has gap zero

For a fixed finite P define

\[
\mathcal E_{\le P}=\mathcal E_\Gamma+
\sum_{2\le n\le P}q_n\int k(x)k(x+\log n)
|u(x+\log n)-u(x)|^2dx.
\]

**Proposition 4.** For every fixed finite P, its even mean-zero spectral gap is zero. Equivalently,

\[
\inf_{\substack{u\in C_c^\infty\ \mathrm{even}\\
\int|u-\bar u|^2d\mu>0}}
\frac{\mathcal E_{\le P}(u)}{\int|u-\bar u|^2d\mu}=0.
\tag{17}
\]

**Proof.** Fix nonzero `φ∈C_c∞((0,1))`. Set `A_R=πe^(2R)` and `d_R=1/A_R`, and take the even pair

\[
u_R(x)=a_R\{\phi(A_R(x-R))+\phi(A_R(-x-R))\},
\qquad\|u_R\|_{L^2(\mu)}=1.
\]

The theta asymptotic and logarithmic derivative give `k(R+s)≍k(R)` and `cosh((R+s)/2)≍e^(R/2)` uniformly for `|s|≤2d_R`. Consequently `a_R² k(R)e^(R/2)/A_R≍1`. The μ-measure p_R of the two supports tends to zero. Cauchy–Schwarz gives `|∫u_R dμ|²≤p_R`, so the variance denominator is `1−O(p_R)→1`.

Split the gamma integral into jump lengths below d_R, between d_R and 1, and at least 1. For the first part use `|u_R(x)−u_R(y)|≤C a_R A_R|x−y|` and `H(s)≤C/s`. It is at most `C a_R² k(R)²/A_R`, hence `O(k(R)e^(−R/2))` after normalization.

For the middle part, symmetry and `|u(x)−u(y)|²≤2|u(x)|²+2|u(y)|²` reduce the integral to x on the supports. For `d_R≤|s|≤1`, `k(x+s)≤k(R−1)` for large R. This contributes at most `C e^(−R/2)k(R−1)log A_R` after normalization.

For the last part, `H(s)≤C e^(−s/2)` for s≥1, and on either support

\[
\int_{|x-y|\ge1}H(|x-y|)k(y)dy
\le C e^{-R/2}\int e^{|y|/2}k(y)dy.
\]

Dividing the remaining `k(x)|u_R(x)|²` integral by its reference density `k(x)cosh(x/2)` gives another `O(e^(−R/2))`. Therefore

\[
\mathcal E_\Gamma(u_R)\le C e^{-R}
+C e^{-R/2}(1+\log A_R)k(R-1).                         \tag{18}
\]

For a fixed prime shift s=log n, the same squared-difference inequality gives

\[
\mathcal E_n(u_R)\le2q_n\int k(x)|u_R(x)|^2
[k(x-s)+k(x+s)]dx.
\]

For all n≤P and sufficiently large R, the bracket is at most `2k(R−log P−1)`, since k is decreasing on the far tail. Hence

\[
\sum_{n\le P}\mathcal E_n(u_R)
\le C_P e^{-R/2}k(R-\log P-1).                         \tag{19}
\]

The right sides tend to zero and are eventually `O_P(e^(−R))`. Subtracting the weighted mean preserves the jump energies and gives mean-zero vectors in the closed form domain. This proves (17). ∎

Thus even the entire gamma jump form, combined with any finite collection of the positive prime jumps, has optimal even Poincaré constant zero. It cannot establish the positive threshold 1/4. Monotone convergence of the prime sum for each fixed test does not supply uniform convergence over the moving normalized tests determining the spectral gap.

There is no conflict with finite-window truncation of the original Weil prime autocorrelations. In the positive-k transform u is zero outside its compact support but k is not. Formula (12) includes interior-to-exterior squared differences for arbitrarily large prime powers. Their diagonal contributions enter the exact cancellation `W*k=0`. Deleting those jumps does not reproduce the original finite-window form.

## 7. What remains a useful research target

The complementary space is not innocuous: for fixed rank it retains arbitrarily many near-zero modes; if RH fails, every space with uniformly vanishing all-input residual leaves a negative witness in the complement. Fixed-rank positive trial forms and excellent profile asymptotics can therefore hold unconditionally while missing the true ground.

A sufficient route must add information of one of the following kinds:

1. A uniform joint rank/support theorem that controls the complete derivative form core and its tail, with constants valid at the needed spectral scale. Equations (8)–(10) show why fixed-rank asymptotics are inadequate. The all-input residual need not remain small after enough directions are included; indeed a complete fixed-support basis cannot consist uniformly of near-null directions.
2. A complement lower floor tending to zero, as in (5), proved using an ingredient beyond the annihilator identities. This is weaker than a positive gap and exactly sufficient, but the negative-witness argument shows its RH strength.
3. A proof of the sharp weighted jump inequality (14), or a structural reason excluding spectrum below its explicitly known infinitely degenerate threshold. This is a precise alternative arithmetic operator target; the signed pole contribution prevents an automatic positivity argument. Proposition 4 requires control of the infinite prime family that prevents mass escaping to infinity: fixed finite-prime lower bounds cannot work.

These statements do not establish a simultaneous growing-rank selection theorem, a positive complement estimate, or RH. They explain why low-dimensional boundary cancellation, even if it selects Xi unconditionally, cannot supply those missing statements by itself.
