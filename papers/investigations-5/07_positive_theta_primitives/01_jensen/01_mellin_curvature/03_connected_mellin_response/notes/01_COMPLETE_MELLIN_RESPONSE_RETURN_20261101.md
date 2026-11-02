# MC03-B01: coalescing saddle and the complete signed trace response

1 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Contributor `/root/mc03_response`, actual recorded **gpt-6-astra (Codex), reasoning effort ultra**; child session `01a19a49-d2ca-7ab1-b502-4e2795ee4f33`, turn `01a19a49-d2e8-7940-8e28-d3ab8a4b9600`. This is an authoring return, pending separate checking, not independent specialist review.

**Disposition: bounded assessment complete; the global Mellin comparison remains open.** A fixed-box, large-Mellin-parameter calculation for the **complete signed theta determinant** has a nonzero three-particle Gaussian Vandermonde-squared limit, with an explicit normalization and trace susceptibility. An exact rescaling then reduces the desired tail estimate to two coarse signed-integral allowances. Those allowances have **not** been proved on the full chamber, and no effective theta tail threshold is claimed. The calculation provides a physical local model and a more concrete remaining obligation; it proves no new coefficient sign, global curvature bound, RH-equivalent physical theory, or RH result.

| Next task | Type / recommended model | Readiness | Bounded output |
| --- | --- | --- | --- |
| MC03-B02: full signed localization in the fixed saddle normalization of (9) | B — Astra; the mixed/off-saddle estimate is a consequential unresolved mechanism | Conceptually ready after separate review; no E numerical request issued | Prove the two allowances (12) for an explicit threshold, or exhibit the precise failed allowance. One localization attempt, fixed order three and fixed complete source; stop if a new observable or an unbounded numerical campaign is needed. |

The task compared two candidates: differentiating a relative determinant saddle expansion, and inserting the **centered Mellin score before estimating**. The latter is selected. It avoids needing to differentiate an unspecified big-O remainder; the first and second responses are kept as exact integrals from the outset. The finite algebra check below is restricted to Gaussian polynomial moments, not theta sampling.

Read with the [result index][results], especially [theta bookkeeping][theta] and [collision controls][controls], and the [avoid index][avoid], especially [reformulations][reformulation], [re-realizations][rerealization], [joint estimates][joint], [scopes][scopes] and [parallel ownership][parallel].

## 1. Fixed source and exact response

Keep physical heat time zero, the whole canonical series
\[
\Phi(u)=\sum_{n\ge1}(2\pi^2n^4e^{9u}-3\pi n^2e^{5u})e^{-\pi n^2e^{4u}},
\quad c_n=\frac1{(2n)!}\int_0^\infty u^{2n}\Phi(u)\,du,
\quad D_{r,k}=\det[c_{k+j-i}].
\]
Set \(c_n=0\) for negative integers. Ordinary coefficients \(c_n\), raw moments and exponential coefficients \(n!c_n\) remain distinct. On \(\Omega_3=\{0<u_1<u_2<u_3\}\), put
\[
f_s(\mathbf u)=\Bigl(\prod_j u_j^{2s}\Bigr)V(\mathbf u^2)
\det[\Phi^{(2i)}(u_j)]_{i=0,1,2;j=1,2,3},\qquad
M(s)=\int_{\Omega_3}f_s,\quad T=2\sum_j\log u_j. \tag{1}
\]
Equivalently \(f_s=w_sh_3\), with exactly the signed insertion of the packet; its negative origin region is retained everywhere in this return. The accepted order-three inputs give \(M(s)>0\) for real \(s\ge0\), at their recorded internal-review scope. Therefore
\[
\mathcal C_3(s)=\frac{\int T^2f_s}{M(s)}-
\left(\frac{\int Tf_s}{M(s)}\right)^2. \tag{2}
\]
This is a signed cross response, not a positive-state variance. Subtracting any real constant from \(T\) in (2) leaves it unchanged. A constant may depend on the *evaluation point* \(s\): (2) is an algebraic identity at each \(s\), not differentiation of a moving observable.

The exact 27-integral formula in [Note03][note03] remains an alternative evaluator of (1)–(2). No noninteger Toeplitz identity is asserted. At integers only,
\(M(k)=(2k)!(2k+2)!(2k+4)!D_{3,k}\).

## 2. Saddle scales and the determinant cancellation

For \(s>0\), define uniquely \(a=a(s)>0\), \(t=t(s)\), and \(\sigma=\sigma(s)>0\) by
\[
s=2\pi a e^{4a}=2at,\quad t=\pi e^{4a},\qquad
\sigma^2=\frac{a^2}{2s(1+4a)}. \tag{3}
\]
The scalar exponent \(F_s(u)=2s\log u-\pi e^{4u}\) has \(F_s'(a)=0\) and \(-F_s''(a)=\sigma^{-2}\). As \(s\to\infty\), \(a,t\to\infty\), while \(\sigma\to0\) and \(\sigma/a\to0\).

Write \(u_j=a+\sigma x_j\). Uniformly for fixed \(|x_j|\le L\), the **full source**, not a truncated source substituted into the observable, satisfies
\[
\Phi(a+\sigma x)=2e^a t^2 e^{-t}\,
\exp\{-\pi e^{4(a+\sigma x)}+t\}\,(1+o_L(1)). \tag{4}
\]
Here the omitted prefactor \(e^{9\sigma x}\), the first-mode factor \(1-3/(2\pi e^{4u})\), and the differentiated full theta remainder all tend uniformly to one or zero as appropriate. More transparently, combining the weight with the source gives
\[
\frac{u^{2s}\Phi(u)}{2e^at^2\exp(F_s(a))}
\longrightarrow e^{-x^2/2}. \tag{5}
\]
Taylor's remainder in \(F_s\) on this fixed box tends to zero: its cubic bound is \(O_L(\sigma)\); the amplitude error is \(O_L(\sigma+t^{-1})\). The full source-jet error is bounded by the differentiated theta sums in [J-E01 r2, Section 4][tail], rather than by differentiation of an unspecified asymptotic.

Let \(R=\Phi''/\Phi\), \(S=\Phi^{(4)}/\Phi=g(R)\). The same full-source tail gives
\[
R'(u)=128(\pi e^{4u})^2(1+o(1)),\qquad
\frac{d^2g}{dR^2}=\frac{R'S''-S'R''}{(R')^3}\longrightarrow2.
\]
Thus the divided-difference formula for \(h_3\) gives \(h_3\to1\), uniformly when all three nodes belong to the moving fixed box, including coincident limits. Consequently
\[
\begin{split}
V(\mathbf u^2)&=(2a\sigma)^3V(\mathbf x)(1+o_L(1)),\\
V(R(\mathbf u))&=(128t^2\sigma)^3V(\mathbf x)(1+o_L(1)).
\end{split} \tag{6}
\]
For the second line use the mean value integral for each pair difference, so no separation assumption on the \(x_j\) is needed. Equations (5)–(6), the full-source divided difference, and \(d\mathbf u=\sigma^3d\mathbf x\) fix the leading factor
\[
K(s)=(2e^at^2)^3e^{3F_s(a)}(256at^2)^3\sigma^9. \tag{7}
\]
The **power \(\sigma^9\)** comprises three powers from volume and six from the two Vandermondes. Replacing the moment matrix entries by their leading rank-one terms loses these six powers and gives a zero determinant. Equations (6)–(7) resolve that cancellation before any estimate is attempted.

Define the exact signed rescaled density on
\(\mathcal D_s=\{-a/\sigma<x_1<x_2<x_3\}\) by
\[
\rho_s(\mathbf x)=K(s)^{-1}\sigma^3
f_s(a+\sigma x_1,a+\sigma x_2,a+\sigma x_3).
\]
On every fixed ordered box \(\mathcal B_L=\{-L\le x_1\le x_2\le x_3\le L\}\), eventually contained in the closure of \(\mathcal D_s\),
\[
\rho_s(\mathbf x)\longrightarrow
\rho_G(\mathbf x):=e^{-\frac12\sum x_j^2}V(\mathbf x)^2. \tag{8}
\]
More strongly, the quotient by \(\rho_G\) extends through collision faces using the divided differences and tends uniformly to one on \(\mathcal B_L\). This is a **proved fixed-box local limit**. It is not convergence of the integral over the expanding domain \(\mathcal D_s\); no full-domain dominated-convergence claim is being made.

## 3. Gaussian normalization and exact signed susceptibility

Direct determinant composition with the first three Gaussian moments gives
\[
G:=\int_{x_1<x_2<x_3}\rho_G\,d\mathbf x
=(2\pi)^{3/2}\det\begin{pmatrix}1&0&1\\0&1&0\\1&0&3\end{pmatrix}
=2(2\pi)^{3/2}.
\]
The full orthant/permutation factor is \(3!\), not an additional factor in \(G\). Let \(\Lambda(s)=G K(s)>0\), and set
\[
Y_s(\mathbf x)=\frac{a}{2\sigma}(T-6\log a)
=\frac a\sigma\sum_j\log\left(1+\frac\sigma a x_j\right),
\qquad
I_p(s)=\frac1G\int_{\mathcal D_s}Y_s^p\rho_s\,d\mathbf x,
\quad p=0,1,2. \tag{9}
\]
These are **complete signed integrals**. In particular \(I_0=M/\Lambda>0\), and every negative source region is included. For all \(s>0\), exactly,
\[
\boxed{\mathcal C_3(s)=\frac{2}{s(1+4a)}
\left(\frac{I_2}{I_0}-\left(\frac{I_1}{I_0}\right)^2\right).} \tag{10}
\]
No derivatives of an asymptotic error occur. This is the selected response representation; it directly retains \(M,M',M''\), with the large deterministic center removed.

On fixed boxes, \(Y_s\to X:=x_1+x_2+x_3\) uniformly. Under the normalized Gaussian density \(\rho_G/G\), shifting all nodes by \(b\) preserves the Vandermonde and ordering and gives
\[
E_G e^{bX}=e^{3b^2/2},\qquad E_GX=0,\quad E_GX^2=3.
\]
Thus **if** the corresponding full-integral convergence were proved, (10) would give the previously heuristic scale \(6/[s(1+4a)]\). This return proves the fixed-box limit and its nonzero prefactor, but leaves that full-integral premise unpaid.

This density is the eigenvalue density of a three-by-three Gaussian Hermitian matrix, or the squared three-fermion oscillator Slater wavefunction. The normalization and moment identities needed here were derived above. For the terminology and chamber convention, the inspected primary exposition is [Terence Tao, 254A Notes 6, Section 1, equation (1)](https://terrytao.wordpress.com/2010/02/23/254a-notes-6-gaussian-ensembles/), 23 February 2010. No random-matrix universality theorem is imported. The local theory is positive while the original amplitude remains signed; it is neither an exact replacement of theta by GUE nor a newly established physical equivalence to RH.

## 4. A conditional tail comparison with coarse, explicit allowances

The following implication is proved algebraically and has no hidden derivative premise:
\[
\boxed{I_0(s)\ge\tfrac12,\quad I_2(s)\le6,
\quad s\ge S_0:=4\pi e^8
\quad\Longrightarrow\quad \mathcal C_3(s)\le\kappa_3(s).} \tag{11}
\]
Indeed the real square in (10) is nonnegative, so the hypotheses imply
\(\mathcal C_3\le24/[s(1+4a)]\). At \(s\ge S_0\), (3) gives \(a\ge2\) and \(s\ge20\). The decreasing-series integral bound gives
\[
\kappa_3(s)=\sum_{j=0}^2\sum_{n\ge0}(s+j+\tfrac12+n)^{-2}
\ge\sum_{j=0}^2(s+j+\tfrac12)^{-1}\ge\frac3{s+5/2}.
\]
Finally \(24/[s(1+4a)]\le24/(9s)\le3/(s+5/2)\), where the last inequality is exactly \(s\ge20\).

The constants \(1/2\) and 6 are **chosen sufficient budgets**, not measured theta values. The lemma is stronger than an exact reformulation of the curvature target: it separately requires a normalization floor and a signed centered-second-moment ceiling, and does not exploit the beneficial \(I_1^2\) term. Its proof does not acquire either hypothesis. \(S_0\) is the threshold of this **conditional lemma only**, not an effective threshold for the theta comparison.

To show precisely what remains, freeze \(L=12\), and split the same integrals into \(I_p=A_p+B_p\), with \(A_p\) over \(\mathcal B_{12}\) and \(B_p\) over \(\mathcal D_s\setminus\mathcal B_{12}\). One sufficient full-source payment is
\[
\boxed{A_0\ge\tfrac34,\quad A_2\le4,\qquad
B_0\ge-\tfrac14,\quad B_2\le2.} \tag{12}
\]
The first pair gives the local main term; the second explicitly retains the signed mixed/off-saddle region. Neither \(B_0\) nor \(B_2\) is replaced by zero, and no negative part of \(h_3\) is deleted.

For comparison, exact Gaussian scaling yields, for \(Q=\sum x_j^2\),
\[
E_GQ=9,\quad E_G(X^2Q)=33.
\]
These follow also from
\(G^{-1}\int e^{-\alpha Q/2+bX}V^2
=\alpha^{-9/2}e^{3b^2/(2\alpha)}\).
Since the complement of \(\mathcal B_{12}\) has \(Q>144\), its Gaussian mass is at most \(1/16\), and its \(X^2\)-moment at most \(11/48\). Hence the local limit (8) proves that the first pair in (12) holds **eventually**, but without an explicit threshold. It does not bound the second pair.

The exact surviving obligation is to obtain an explicit common \(S\ge S_0\) for all four inequalities (12), or directly for the two in (11). The noncompact region includes one or two nodes far from the saddle, the origin and its negative insertion, and the spatial tails with arbitrary relative node separations. A source tail estimate by itself does not bound these integrals relative to \(\Lambda\). This is where the selected argument stops.

## 5. Domain, controls and actual gain

**Endpoints and integrability.** Equation (2) holds for every \(s\ge0\), including the full \([0,2]\) slab, by the inherited complete-source integrability with two logarithmic insertions. Near zero one may use the undivided determinant in (1), whose source derivatives are bounded; \(u^{2s}|\log u|^p\) is integrable. At coincident nodes the undivided product is smooth and vanishes; (6) uses removable divided differences. At infinity each fixed source derivative has full double-exponential decay. Equations (3), (9) and (10) use \(s>0\) only; their degenerating coordinate scale at \(s=0\) does not remove the original endpoint. **No curvature inequality is proved on \([0,2]\), on any remaining compact interval, or on an effective unbounded theta tail.**

**Gaussian check.** The separate Gaussian source \(\Phi=e^{-bu^2}\), \(b>0\), has \(h_3=1\) and \(M_G(s)\) proportional to an exponential in \(s\) times \(\prod_{j=0}^2\Gamma(s+j+1/2)\). Thus \((\log M_G)''=\kappa_3\), agreeing with [the exact initial assessment][initial]. This Gaussian-source equality is distinct from the local GUE saddle density (8); neither is evidence that the theta inequality holds.

| Control / relaxation | What is and is not screened |
| --- | --- |
| Two-point association relaxation | Its \(Q_1=16705/576>28\) still defeats association-only reasoning. It has no canonical source jet, saddle relation (3), or derivative-determinant realization. Neither (8) nor (12) is inferred for it. |
| Euler-factor sources | Literal unchanged theta expansion and its differentiated reconstruction fail; their saddle/response allowances are untested. Their positive-time collisions do not contradict a time-zero order-three statement. |
| Weighted-square and finite-prime controls | Full canonical weights, and the relevant full-reflection assumptions, fail. A weighted source retaining a lowest square mode can still have a comparable *local* saddle limit; therefore that local limit alone does not distinguish theta or prove all-order signs. No claim that all such controls fail (12) is made. |
| Reflected super-Gaussian | The specific exponential-of-exponential theta tail used in (3)–(8) is absent. Generic moment-determinant and response identities remain applicable when integrable; quantitative allowances are untested. |
| Smooth shape / positive-primitive controls | They lack unchanged canonical reconstruction. Similar local saddle behavior can survive substantial source changes, so no automatic exclusion follows from (8). The complete normalized signed allowances, not the physical label, would need checking. |

The gain is **structural and local**: the determinant cancellation is resolved into the explicit \(\sigma^9\) prefactor, the complete response has the exact scaled form (10), and a broad sufficient tail budget is specified by (11)–(12). This is a nontrivial physical asymptotic reformulation of the pilot. It is not yet a quantitative advance proving any part of the global Mellin comparison. No arbitrary-order extension or RH equivalence is claimed; increasing particle number changes the needed signed-source and normalization inputs.

## 6. Support, versions and handoff

The [exact checker][check] expands the three-variable Vandermonde polynomial and uses rational Gaussian moments. Its frozen finite purpose is to verify the normalization 12 relative to three independent standard normals and the four values \(0,3,9,33\) for \(E_GX,E_GX^2,E_GQ,E_G(X^2Q)\). The [record][record] stores those values, the fixed Gaussian box allowances, the actual input and script hashes, and the run scope. It performs no theta coefficient acquisition, quadrature, grid, source derivative escalation or root calculation. These finite checks validate constants; the analytical claims and unpaid domains above are not certified by the script.

Inputs are the packet's [frozen launch record][launch], repository instructions and model workflow, the six-branch baseline, and these read versions. All listed launch-baseline inputs remained unchanged when checked; the local progress file alone was advanced under worker ownership.

| Input | SHA-256 |
| --- | --- |
| Initial assessment | `ee4280708b43d4d080fe98c128d58c0180f0ba0851b730bd859c2a899f84d9de` |
| Parent Note03 | `0d6167397219a4dd11dbb5650c5c3c5d31a8e17d7a22a6b81eba81af50fb091f` |
| Parent Note04 | `f4ff6338794cf359bf06ea6ec17867fd5aef44910de1796b3c26396f8fb5b720` |
| Continuation05 | `7cfa21664fe85e64749a7fc4e32c420300b8d91590f0dc62da35cf3816e677d7` |
| Local overview | `e3a0a0700b1dc26e95c548f32f3d29f966baefd5f7fc24018e8da585631d1997` |
| J-E01 r2 tail source | `202a37845f602efd56c8d11935cb8256c665edbaaae421b1b2fed14c186e97d2` |

**Next: [B] MC03-B02 — Astra.** Prove one full signed localization payment (12) with an explicit threshold, or return the failed payment. The current return is frozen for a different reviewer before that recommendation is acted on. Even a successful tail payment would leave an explicitly bounded compact interval, including \([0,2]\), unpaid; only then should an E/Sol certificate contract be designed. No numerical campaign is issued here.

[results]: ../../../../../../../result-summaries/README.md
[theta]: ../../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../../avoid/README.md
[reformulation]: ../../../../../../../avoid/01_restating_the_target.md
[rerealization]: ../../../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md
[joint]: ../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[scopes]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[parallel]: ../../../../../../../avoid/17_parallel_writers_and_broken_registries.md
[tail]: ../../../notes/07_J_E01_R2_SIGNED_AVERAGING_AND_Q10_P7_RETURN_20261101.md
[note03]: ../../notes/03_IDEAS_AND_POSSIBLE_ROUTES_20261101.md
[initial]: ../../notes/01_INITIAL_BRANCH_EVALUATION_20261101.md
[launch]: ../../numerics/PARALLEL_PHYSICAL_LAUNCH_RECORD_20261101.json
[check]: ../numerics/mc03_exact_gaussian_check.py
[record]: ../numerics/MC03_B01_EXACT_RECORD_20261101.json
