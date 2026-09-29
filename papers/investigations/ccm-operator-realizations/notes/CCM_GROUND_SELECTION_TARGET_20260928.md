# CCM continuation: from a small residual to ground-state selection

Date: 28 September 2026. Continuation round 6.

Drafted for Edward Baker with LLM assistance. Model: GPT-6 (Codex); the exact serving variant and reasoning-effort setting are not exposed to the lead reviewer. Parallel analytic and numerical readings were used; these are same-model checks, not independent mathematical refereeing.

## 1. Outcome

The latest target was the arithmetic comparison between the actual Weil ground state and the concentrated prolate candidate, following the [round-5 audit](CCM_INFINITE_L_BOUNDED_AUDIT_20260926.md). This continuation establishes a useful distinction:

**Producing an arithmetic approximate null vector is possible unconditionally. Proving that the bottom eigenspace has a substantial component in that vector is the unresolved step.**

The analytic Xi kernel and every translate are annihilated by the whole-line Weil distribution, without RH. Truncating them gives extremely small residuals. There are arbitrarily many such near-zero directions; even positive approximate null vectors can have second moments tending to infinity. Thus neither an absolute residual estimate nor positivity of the candidate resolves the ground-state or concentration problem.

A weaker sufficient target for **RH itself** follows: prove that the actual even ground space does not become as nearly orthogonal to the truncated Xi kernel as its residual becomes small. This requires much less than convergence of the whole ground profile, and needs neither a simple ground eigenvalue nor the finite CCM boundary condition. It remains a substantial arithmetic estimate, not a proof of RH. The stronger objective of identifying the CCM determinant limit still requires concentration and normalization control.

Detailed proofs are in the [boundary-residual note](CCM_XI_ANNIHILATOR_AND_BOUNDARY_RESIDUAL_20260928.md) and the [ground-selection note](CCM_NEAR_NULL_CLUSTER_AND_GROUND_SELECTION_20260928.md). The [review](../reviews/CCM_GROUND_SELECTION_REVIEW_20260928.md) records the scope and checks. Sonin residuals are outside this continuation.

## 2. The unshifted arithmetic operator is essential

Use \(b=L/2\), \(I_b=[-b,b]\), and the closed localized Weil operator \(W_b\) already used in the investigation. Let \(W_b^+\) denote its even restriction, \(\varepsilon_b^+=\min\sigma(W_b^+)\), and \(E_b\) the orthogonal projection onto that bottom eigenspace. Compact resolvent and a lower bound hold at each fixed b; no bound uniform in b is assumed.

Throughout this note, ground energies are the **original unshifted** Weil energies. Replacing \(W_b\) by \(W_b-\varepsilon_b I\) would erase the sign information used below. The positive mass–stiffness realization is therefore not the premise of the overlap argument.

The logarithmic Xi kernel is
\[
k(x)=e^{x/2}\sum_{n\ge1}h(ne^x),\qquad
h(u)=\frac\pi2u^2(2\pi u^2-3)e^{-\pi u^2}.
\]
It is even, strictly positive, smooth, and decreases faster than every exponential at both ends. Its Fourier transform is a fixed nonzero scalar multiple of \(\Xi\); the scalar cancels in every normalized expression here. This construction is the arithmetic reference profile, not a zero-list interpolation. The link to the prolate candidate is the already-recorded approximation in round 5. See [CCM, Section 7](https://arxiv.org/html/2511.22755v1#S7).

Define
\[
f_b=\mathbf1_{I_b}k,\qquad v_b=f_b/\|f_b\|_2,\qquad
r_b=\|W_b^+v_b\|_2,\qquad \alpha_b=\|E_bv_b\|_2.
\tag{1}
\]
The cutoff f_b lies in the localized operator domain despite its jumps at the endpoints: its zero extension has Fourier decay \(O(1/|t|)\), which is sufficient for the squared logarithmic multiplier weight. Smooth cutoffs provide an alternative when using whole-line weighted-space estimates.

## 3. What the new analytic calculation supplies

For a nontrivial zero \(\rho\), put \(z_\rho=(\rho-1/2)/i\), with no assumption that it is real. The explicit formula evaluates the Weil form through transforms at \(z_\rho\) and its conjugate. Since \(\widehat k(z_\rho)=0\),
\[
Q(k,h)=0
\tag{2}
\]
for the admissible test functions used here. Translation multiplies \(\widehat k\) by an exponential and preserves these zeros. Equation (2) is an unconditional annihilator identity; it is not a positivity statement.

Writing \(t_b=(1-\mathbf1_{I_b})k\), one obtains
\[
W_bf_b=-\mathbf1_{I_b}(w*t_b),\qquad
Q(f_b,f_b)=Q(t_b,t_b),
\tag{3}
\]
where w is the full Weil distribution. The full distribution on the right includes all prime powers; it cannot be replaced by the compact-support prime list when estimating the exterior tail.

The boundary-residual note proves, with constants independent of b for \(b\ge1\),
\[
\|W_b f_b\|_2\le C(1+b)^{3/2}e^{-b}k(b)
\le C'(1+b)^{3/2}e^{7b/2}e^{-\pi e^{2b}},
\tag{4}
\]
and the stronger quadratic estimate
\[
|Q(f_b,f_b)|\le C(1+b)e^{-2b}k(b)^2
\le C'(1+b)e^{7b}e^{-2\pi e^{2b}}.
\tag{5}
\]
The estimates use the gamma kernel, the pole term, and an elementary bound \(\Lambda(n)\le\log n\); no prime-number theorem, RH, or zero computation is input. Retaining the separation of translated boundary tails improves the estimate over a triangle bound on all prime terms. In terms of L, the residual bound is \(O((1+L)^{3/2}e^{7L/4}e^{-\pi e^L})\). Since \(\|f_b\|_2\to\|k\|_2>0\), the normalized residual r_b obeys the same rate.

Equation (5) is an absolute upper estimate. It does not give the sign of the Rayleigh quotient, and a tiny Rayleigh quotient is not a lower bound on the bottom eigenvalue.

## 4. Why a residual is insufficient, even for the actual arithmetic form

For fixed \(a\ge0\), the even profile
\[
g_a(x)=\tfrac12\{k(x-a)+k(x+a)\}
\]
is positive and is also an annihilator. Its normalized transform and half second moment are
\[
\frac{\widehat g_a(z)}{\widehat g_a(0)}
=\cos(az)\frac{\Xi(z)}{\Xi(0)},\qquad
\tau(g_a)=\tau(k)+\frac{a^2}{2}.
\tag{6}
\]
Thus the null equation does not select Xi as the normalized transform. These profiles are not asserted to be finite CCM ground states or to generate positive mechanical pairs.

Smoothly truncating any fixed number m of linearly independent g_a's gives an m-dimensional trial space on which the **norm of the restriction \(W_b:S_b\to L^2(I_b)\)** tends to zero. By spectral projection, W_b has at least m even eigenvalues near zero for sufficiently large b. The statement is unconditional and permits other, negative eigenvalues below that cluster. If RH holds, the first m even eigenvalues all tend to zero; in particular, a positive even ground gap uniform in b is not a viable objective.

Allow the shifts to grow, for example \(a_b=b/2\), and cut off smoothly near \(\pm b\). The residual still tends to zero faster than every ordinary exponential, while
\[
\tau(\chi_b g_{a_b})=\tau(k)+b^2/8+o(1)
=\tau(k)+L^2/32+o(1).
\tag{7}
\]
This is a concentration obstruction **inside the actual arithmetic approximate-null family**, strengthening the earlier nonarithmetic sinc example. Evenness, pointwise positivity, and a vanishing arithmetic residual do not bound the second moment. Ground selection or another localization principle is needed.

## 5. A weaker, precise sufficient target for RH

The spectral theorem immediately gives
\[
|\varepsilon_b^+|\,\alpha_b
=\|E_bW_b^+v_b\|_2\le r_b.
\tag{8}
\]
It is important that E_b is the projection onto the **bottom** eigenspace. Projection onto an arbitrary cluster near zero would make the overlap large automatically and would not imply RH.

**Overlap criterion.** If there is a cofinal sequence \(b_j\to\infty\) with \(\alpha_{b_j}>0\) and
\[
\boxed{r_{b_j}/\alpha_{b_j}\longrightarrow0,}
\tag{9}
\]
then RH holds.

Indeed, (8) gives \(\varepsilon_{b_j}^+\to0\). The even bottom energies are nonincreasing as the interval grows, since zero extension includes the smaller form domain in the larger one. Therefore every fixed-support even form is nonnegative. Alternatively, if an off-axis zero existed, the explicit-formula construction in the ground-selection note supplies a compactly supported even negative test. It would force \(\varepsilon_b^+\le-\delta\) for all sufficiently large b, contradicting (8)–(9). This latter proof spells out why even tests suffice.

Concrete sufficient lower bounds, using (4), include any fixed positive lower bound on \(\alpha_b\), any bound \(\alpha_b\ge e^{-C b^p}\) for fixed C,p, or even
\[
\alpha_b\ge e^{-c e^{2b}}\quad\text{for a fixed }0<c<\pi
\tag{10}
\]
along a cofinal sequence. None of these lower bounds has been established. Under failure of RH the opposite estimate follows: for some \(\delta>0\), \(\alpha_b\le r_b/\delta\) eventually. The unknown alternative is therefore an extraordinarily strong asymptotic orthogonality of the actual bottom space to a known positive arithmetic profile.

This criterion avoids the simple-even and boundary-functional assumptions of the finite CCM determinant construction, and needs no proof that \(u_b\to k/\|k\|_2\). It does **not** show that RH implies (9), identify a determinant limit, bound the signed ground-state second moment, or prove that the ground eigenfunction is pointwise positive. Those are separate questions.

Finite Fourier analogues must control consistency with the infinite Fourier operator. A small finite matrix residual cannot be substituted for r_b in (8). A cofinal sequence of dimensions by itself does not provide the required error estimate.

## 6. A bounded diagnostic of the previous comparison gate

The experiment uses the L2-normalized restriction of k and then projects it onto the finite Fourier space. It deliberately does **not** call that proxy the finite prolate candidate q_L. It checks the proposed comparison mechanism without assuming the conjectured prolate–ground relation.

The finite matrices are built from the prime/gamma/pole formula, with the support parameter generalized from X=13. For X=5,13,29 the builder is checked at N=3 against the defining-form quadrature. The important N=32 cases are repeated at 90 and 130 decimal digits. These are multiprecision diagnostics, not interval certificates or infinite-tail bounds.

For the even matrix A, normalized proxy \(\widehat v\), and its first two levels \(\lambda_1<\lambda_2\), write \(\rho=\langle\widehat v,A\widehat v\rangle\). The numerical residual here is \(r_{\rm num}=\|(A-\rho)\widehat v\|\), centered at the Rayleigh quotient; it is distinct from the uncentered continuum residual r_b in (1). The earlier gate requires \(\lambda_2-\rho>0\).

| X, N | Proxy–ground overlap | L2 distance | Proxy Rayleigh quotient | Second even level | Ground half second moment |
|---|---:|---:|---:|---:|---:|
| 13, 32 | 0.9998865 | 0.0150644 | 7.86e-29 | 1.01e-42 | 0.0220459 |
| 13, 64 | 0.9997465 | 0.0225145 | 6.06e-29 | 2.59e-51 | 0.0215400 |
| 29, 32 | 0.9994395 | 0.0334808 | 1.59e-35 | 2.60e-61 | 0.0255912 |

The Xi reference moment is about 0.0231049931. All tested gate signs are negative. At X=13,N=32, only about \(1.11\times10^{-13}\) of the proxy's squared norm is outside the first four even eigenvectors, yet that complement supplies essentially all its squared centered residual. The first excited mode supplies almost all the angular error. Consequently the full residual norm and the error in selecting the first mode measure different effects.

Increasing N from 32 to 64 at X=13 worsens the proxy distance and changes the moment. The data do not establish cutoff convergence or disprove the asymptotic prolate comparison. Their purpose is narrower: they show that the raw residual/second-level gate is not practically discriminating in these examples, even when the proxy is resolved to extremely high L2 accuracy.

See the [diagnostic record](../reviews/CCM_XI_GROUND_DIAGNOSTIC_20260928.md) and [numerical guide](../numerics/README.md) for exact fields, normalization checks, precision comparisons, and provenance.

## 7. The next comparison should resolve the low cluster

A constructive route is to use a space S_b generated by suitably truncated arithmetic annihilators or by the low prolate arithmetic profiles, rather than treating the entire even complement as one block. For a finite Hermitian compression, write
\[
A=\begin{pmatrix}H&C^*\\ C&D\end{pmatrix}_{S_b\oplus S_b^\perp}.
\]
If \(D-E\) is invertible, the eigenvalue equation is equivalent to
\[
[H-C^*(D-E)^{-1}C]p=Ep,\qquad
q=-(D-E)^{-1}Cp.
\tag{11}
\]
The analytic task is to control this effective low-dimensional problem on the scale of its own level splittings. Absolute errors that are tiny on the scale of one can still be huge on that scale. A lower bound on D must also exclude lower states outside S_b; presuming that S_b contains the bottom eigenspace would be circular.

For smooth arithmetic annihilators g_i, put \(f_i=\chi_bg_i\) and \(t_i=(1-\chi_b)g_i\). Their exact trial matrix is
\[
Q(f_i,f_j)=Q(t_i,t_j),\qquad G_{ij}=\langle f_i,f_j\rangle.
\tag{12}
\]
This gives a concrete boundary-tail problem in which to search for a relative asymptotic expansion. It retains prime and archimedean cancellation. It does not justify discarding the correction \(C^*(D-E)^{-1}C\), infer positivity from small entries, or imply that a fixed number of basis elements captures all near-zero directions. The cluster dimension may need to grow with b.

Two useful outcomes would be genuinely stronger than more fixed-L calculations:

1. **For RH:** derive a lower bound for the bottom-space overlap in (9), perhaps from a quantitative localization or sign argument for the actual arithmetic eigenfunction. Candidate positivity alone is insufficient, and the signed Weil kernel does not automatically supply a positivity-preserving semigroup.
2. **For CCM determinant convergence:** prove that the effective ground direction selects the centered profile, with the weighted normalization and moment control from round 5. This is stronger than (9), but directly serves the original spectral-limit program.

The prolate picture remains a plausible source of the needed structure. Its useful new content would be a comparison of the actual form and boundary corrections, with errors relative to the cluster splitting. The already-known approximation of h_lambda by h does not provide that comparison.

## 8. Stopping rule and present status

Do not enlarge a Fourier cutoff merely to obtain a smaller displayed energy or residual. Any next calculation should test a specific term in (11)–(12), a proposed uniform overlap inequality, or a proved bound on its omitted complement. Track actual low-space orientation, normalization, and support dependence.

This continuation supplies unconditional residual estimates, an arithmetic concentration counterexample, a near-zero cluster argument, and a weaker sufficient overlap criterion. It supplies **no overlap lower bound for the true ground state**, no general simple-even theorem, no infinite-support positivity proof, and no Xi determinant limit. The new conclusion is that the arithmetic ground-selection problem can be posed more precisely and with a substantially weaker sufficient target for RH, while the original profile-comparison target remains open.
