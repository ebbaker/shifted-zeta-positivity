# Round 1 continuation: field growth and necessary degeneration of quartic networks

> Update, 17 October 2026: the [cross-model review](../../reviews/01_ROUND_ONE_CROSS_MODEL_REVIEW_CLAUDE_20261017.md) found no mathematical error in the scoped round-one claims. The [round-two reconciliation](../round-2/README.md) supersedes the weak-convergence limitation and the unbounded-base-time exception. The original derivation below is retained as the reviewed record; scope corrections and classical attributions are in round two. Recorded updater: gpt-6.1-sol (Codex), effort ultra, with substantial LLM assistance for Edward Baker.


17 October 2026. Prepared for **Edward Baker** with substantial LLM assistance. Recorded model: **gpt-6.1-sol (Codex)**; reasoning effort: **ultra**. Same-model authoring checks are not formal round review. The user has explicitly requested this continuation and an unreviewed draft manuscript before the round review.

This continues [Notes 01–02](README.md) under the [result index](../../../../../result-summaries/README.md) and [avoid index](../../../../../avoid/README.md), especially [collision controls](../../../../../result-summaries/12_collision_controls_and_screening.md), [target classification](../../../../../avoid/01_restating_the_target.md) and [scoped exclusions](../../../../../avoid/07_scoped_exclusions_read_as_universal.md). It is a scoped negative result about actual source approximation, not an RH-equivalent target reformulation. It supplies a necessary constraint on growing quartic networks that is stronger than the observation that a fixed model has the wrong tail. It makes no assertion about all Ising scaling limits.

## 1. Readout-normalized quartic networks

Let a finite zero-field network have density proportional to

\[
\exp\{-\sum_{j=1}^{d}\alpha_jx_j^4-\sum_j\beta_jx_j^2
       +\sum_{i<j}K_{ij}x_ix_j\},
\qquad \alpha_j>0,\quad K_{ij}\ge0,
\]

and readout \(S=\sum_jb_jx_j\), where \(b_j>0\). Write
\(M(h)=\mathbb E\exp(hS)\), with the initial normalizer fixed.
For comparison with individual seeds set

\[
Y_j=b_jx_j,\qquad
a_j=\alpha_j/b_j^4,\qquad c_j=\beta_j/b_j^2,
\qquad L_{ij}=K_{ij}/(b_ib_j)\ge0.
\tag{1}
\]

In these variables \(S=\sum_jY_j\), the site density is
\(e^{-a_jY_j^4-c_jY_j^2}\), and the pair interaction is
\(L_{ij}Y_iY_j\). This normalization matters: an apparent vanishing
amplitude can exactly compensate a changing quartic coefficient.

Let

\[
m_{a,c}(h)=
\frac{\int_{\mathbb R}e^{-ay^4-cy^2+hy}\,dy}
     {\int_{\mathbb R}e^{-ay^4-cy^2}\,dy}.
\tag{2}
\]

**Proposition (ferromagnetic comparison).** For every \(h\ge0\),

\[
\boxed{\quad M(h)\ge\prod_{j=1}^{d}m_{a_j,c_j}(h)
                 \ge m_{a_k,c_k}(h)\quad\text{for every }k.\quad}
\tag{3}
\]

The statement holds independently of the number and size of other
couplings. It compares normalized transforms; simply dropping positive
couplings from an unnormalized partition function would not prove it.

### Proof of (3), including the needed covariance inequality

For an even product a-priori measure with quartic tails and nonnegative
pair couplings and fields, the GKS covariance inequality is

\[
\operatorname{Cov}(Y_A,Y_B)\ge0
\tag{4}
\]

for any two finite spin monomials, with repeated indices allowed. Here
is a direct proof in precisely the class needed. Take two copies
\(y,z\), put \(u=(y+z)/2\), \(v=(y-z)/2\), and multiply the covariance
by twice the squared partition function. Its numerator becomes the
integral of
\((y_A-z_A)(y_B-z_B)\) against the doubled Gibbs density.
Each difference is a polynomial in \(u,v\) with nonnegative coefficients,
because expansion keeps exactly the terms with an odd number of \(v\)'s.
The doubled interaction and field are

\[
2\sum_{i<j}L_{ij}(u_iu_j+v_iv_j)+2\sum_jh_ju_j,
\qquad L_{ij},h_j\ge0.
\]

Their exponential has nonnegative power-series coefficients. The doubled
single-site measure is invariant under \(u_j\mapsto-u_j\) and independently
under \(v_j\mapsto-v_j\): these operations use the original evenness and
exchange the two copies. Thus each integrated monomial vanishes if any
local exponent is odd, and is nonnegative otherwise. Quartic tails
justify absolute integration of the series, including polynomial factors.
This proves (4) directly without an unverified import.

For fixed couplings let \(\langle\cdot\rangle_h\) denote the measure with
the common field \(h\ge0\). Equation (4) gives

\[
\frac{d}{dh}\langle Y_iY_j\rangle_h
   =\sum_k\operatorname{Cov}_h(Y_iY_j,Y_k)\ge0.
\]

Therefore

\[
\partial_{L_{ij}}\log M(h)
 =\langle Y_iY_j\rangle_h-\langle Y_iY_j\rangle_0\ge0.
\]

Increasing the couplings from zero to their specified values proves the
first inequality in (3). Evenness gives \(m_{a,c}(h)=\mathbb E\cosh(hY)\ge1\),
which proves the second. This is the usual GKS mechanism, here written
out so that its exact class and normalizer are explicit. Simon–Griffiths,
*The (phi^4)_2 field theory as a classical Ising model*, CMP 33 (1973),
145–164, pp. 145–146, discusses the classical GKS provenance and arbitrary
even single-spin laws; Theorem 1 and pp. 151–152 supply the quartic Ising
approximation and Lee–Yang theorem already used in Note 02.

## 2. A uniform obstruction requiring only one retained site

**Lemma (monotonicity of the normalized single-site transform).**
For real \(h\ge0\), \(m_{a,c}(h)\) is nonincreasing in each of \(a>0\)
and \(c\in\mathbb R\). Indeed, under the zero-field site law,

\[
\partial_a m_{a,c}(h)=-\operatorname{Cov}(\cosh(hY),Y^4)\le0,
\quad
\partial_c m_{a,c}(h)=-\operatorname{Cov}(\cosh(hY),Y^2)\le0.
\tag{5}
\]

The covariance signs here need no spin inequality: both functions are
increasing functions of \(Y^2\), so the elementary independent-copy
identity for a covariance gives the signs.

Fix constants \(A>0\) and \(B\ge0\). If the network contains even one
site with \(a_k\le A\) and \(c_k\le B\), then (3)–(5) imply

\[
M(h)\ge m_{A,B}(h)\qquad(h\ge0).
\tag{6}
\]

No lower bound on \(a_k\), no lower bound on \(c_k\), and no bound on the
other sites, total dimension, or couplings is required.

The normalized theta Laplace transform in the repository convention is

\[
M_\theta(h)=\frac{H_0(-ih)}{I_0(0)}
           =\frac{\xi((1+h)/2)}{\xi(1/2)}.
\tag{7}
\]

Using the xi definition and Stirling's formula gives, as \(h\to+\infty\),

\[
\log M_\theta(h)
 =\frac h4\log h-\frac h4(1+\log(4\pi))
   +\frac74\log h+O(1).
\tag{8}
\]

The factor \(h/4\), and the \(4\pi\) inside the logarithm, follow from
the repository's \(H_0(z)=\xi(1/2+iz/2)/8\), not the alternative
normalization \(\Xi(z)=\xi(1/2+iz)\). The primary formula sources are
[DLMF 25.4.4](https://dlmf.nist.gov/25.4.E4) and
[DLMF 5.11.1](https://dlmf.nist.gov/5.11.E1), both inspected on 17 October
2026. The bound \(\zeta(s)=1+O(2^{-s})\) for real \(s\to+\infty\)
follows immediately from its defining Dirichlet series and the integral
bound on its positive tail.

The elementary quartic saddle computation gives

\[
\log m_{A,B}(h)
 =\frac{3}{4^{4/3}}A^{-1/3}h^{4/3}+O(h^{2/3}+\log h).
\tag{9}
\]

Only the lower bound in (9) is needed. An explicit one, valid for \(h\ge1\),
is obtained by integrating over \([u,u+1/h]\), where
\(u=(h/(4A))^{1/3}\):

\[
\begin{split}
\log m_{A,B}(h)&\ge F_{A,B}(h),\\
F_{A,B}(h)&=hu-A(u+h^{-1})^4-B(u+h^{-1})^2-\log h\\
&\hspace{15mm}-\log\!\left(\frac{\Gamma(1/4)}{2A^{1/4}}\right).
\end{split}
\tag{10}
\]

The denominator in (2) is at most
\(\int e^{-Ay^4}dy=\Gamma(1/4)/(2A^{1/4})\), since \(B\ge0\).
The leading term of (10) is the positive \(h^{4/3}\) term in (9),
and its next largest loss is \(O(h^{2/3})\).

**Theorem (persistent diffuse quartic-site obstruction).** Let \(M_n\)
be normalized readout Laplace transforms of any sequence of finite
ferromagnetic quartic networks; dimensions and couplings may vary without
bounds. If \(M_n(h)\to M_\theta(h)\) for every real \(h\ge0\), then,
for every \(A>0,B\ge0\), eventually no site satisfies both

\[
\alpha_{n,j}/b_{n,j}^4\le A,
\qquad \beta_{n,j}/b_{n,j}^2\le B.
\tag{11}
\]

Equivalently, every fixed lower-left parameter rectangle is eventually
empty after normalizing to the readout variables. In particular a single
unchanging nontrivial quartic block cannot be retained while other
ferromagnetic blocks are appended to achieve theta approximation.

A useful equivalent-site scaling gives the especially simple necessary
condition requested for the manuscript. Put
\(\ell_j=b_j\alpha_j^{-1/4}\) and
\(r_j=\beta_j\alpha_j^{-1/2}\), so the normalized site has density
\(e^{-x^4-r_jx^2}\) and readout \(\ell_jx\). For every fixed real
\(R\),

\[
\boxed{\quad
\max_{j:r_{n,j}\le R}\ell_{n,j}\longrightarrow0,
\quad\text{with the empty maximum defined as zero}.\quad}
\tag{11a}
\]

Otherwise some site has \(r\le R,\ell\ge\varepsilon>0\), and (3),
monotonicity in the quadratic parameter, and monotonicity of an even
Laplace transform on the positive real axis give
\(M_n(h)\ge m_{1,R}(\varepsilon h)\). This again contradicts (8)–(9)
at one sufficiently large fixed field. One can replace \(R\) by
\(\max(R,0)\) in the reference law if a nonnegative parameter is desired.
Condition (11a) follows from (11):
\(a=\ell^{-4}\le\varepsilon^{-4}\) and
\(c=r/\ell^2\le\max(R,0)/\varepsilon^2\).
The rectangle formulation (11) can exclude additional degenerations
where \(r\to+\infty\) and \(\ell\to+\infty\) together.

**Proof.** If a subsequence retained a site satisfying (11), (6) would
give \(M_n(h)\ge m_{A,B}(h)\) along it. Equations (8)–(10) show that some
fixed finite \(h_*\) has
\(m_{A,B}(h_*)>M_\theta(h_*)\). This contradicts convergence at \(h_*\).

This also gives an explicit error witness whenever a chosen \(h_*\ge1\)
satisfies \(F_{A,B}(h_*)>\log M_\theta(h_*)\): every network retaining
such a site obeys

\[
|M(h_*)-M_\theta(h_*)|
 \ge e^{F_{A,B}(h_*)}-M_\theta(h_*)>0.
\tag{12}
\]

No numerical value of \(h_*\) is claimed here. Formula (10) makes a
chosen parameter budget finitely testable using rigorous gamma/xi
evaluation. The result excludes complex-compact Fourier convergence,
which implies Laplace convergence at \(z=-ih_*\). It does not by itself
exclude weak convergence without the uniform integrability needed to
pass these real exponential observables to the limit.

## 3. Independent pure-quartic blocks: no approximation even with unbounded count

Let \(X\) have normalized density proportional to \(e^{-x^4}\), and let
\(m(h)=\mathbb E e^{hX}\). Consider arbitrary finite triangular arrays
\[
M_n(h)=e^{\sigma_n^2h^2/2}\prod_{j=1}^{d_n}m(b_{n,j}h),
\qquad \sigma_n^2\ge0,\quad b_{n,j}\ge0.
\tag{13}
\]
An empty-row maximum is defined to be zero. These include independent scaled quartic blocks, arbitrary changing block
counts, and an independent centered Gaussian component. Each is a known
stable construction; quadratic tilts of the individual quartic laws and
inter-block interactions are not included in (13).

**Theorem.** The transforms (13) cannot converge to \(M_\theta\) uniformly
on every compact subset of the complex field plane.

**Proof.** If some subsequence has \(\max_jb_{n,j}\ge\varepsilon>0\),
evenness gives \(M_n(h)\ge m(\varepsilon h)\) for every real \(h\ge0\).
Equations (8)–(10) contradict convergence at a sufficiently large fixed
field. Thus \(\max_jb_{n,j}\to0\). Complex-compact convergence gives
convergence of derivatives at zero, hence bounded variances. With
\(v=\mathbb EX^2>0\),
\[
\sigma_n^2+v\sum_jb_{n,j}^2=M_n''(0)\le C.
\]
For fixed real \(h\), analyticity at zero gives
\(\log m(bh)=vb^2h^2/2+O_h(b^4)\). The summed error tends to zero because
\(\sum_jb_{n,j}^4\le(\max_jb_{n,j}^2)\sum_jb_{n,j}^2\to0\).
Derivative convergence supplies \(M_n''(0)\to v_\theta>0\),
so the limit must satisfy \(M_\theta(h)=e^{v_\theta h^2/2}\). This contradicts
theta's \(O(h\log h)\) field growth. The proof is entirely analytic.

Alternatively, independence gives
\(\kappa_4(M_n)=\kappa_4(X)\sum_jb_{n,j}^4\to0\), contrary to the
inherited strict theta fourth-cumulant sign. This is a convenient
certificate-based check, not a premise needed by the analytic proof.

**Weak-convergence corollary.** The same independent class cannot even
converge weakly to theta's normalized source. Indeed integration by parts
and strict Cauchy give \(\kappa_4(X)<0\), so
\(\mathbb E S_n^4\le3(\operatorname{Var}S_n)^2\). For positive variances, Paley–Zygmund yields
\(\mathbb P\{S_n^2>\operatorname{Var}(S_n)/2\}\ge1/12\), and tightness
forces bounded variances. Quartic field growth also gives the global
bound \(m(h)\le e^{Ch^2}\), because \(\log m(h)/h^2\) extends continuously
at zero and tends to zero at infinity. The variance bound gives a common
sub-Gaussian bound for all transforms, hence uniform integrability of
fixed exponential observables. Weak convergence would give real Laplace
convergence and, by normality, complex-compact convergence, already
excluded above. This weak upgrade is specific to the independent class;
it has not been proved for the interacting-network theorem.

The moment enclosure is in the [canonical spin scout](../../../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/15_lee_yang/notes/1_THETA_MOMENT_ENCLOSURE_AND_FERROMAGNETIC_SPIN_SCREEN_20261010.md)
and its linked record; no new moment calculation is required, and the main proof does not use the enclosure. This
stronger class exclusion is independent of the pure-potential finite
source test in Note 02. Convolution of quartic seeds need not remain a
single quartic potential, but (13) still cannot approximate theta.

## 4. Exact leading field growth for any fixed network

For a fixed network with positive \(b_j\),

\[
\log M(h)=C h^{4/3}+O(h^{2/3}+\log h),\qquad
C=\frac{3}{4^{4/3}}\sum_jb_j^{4/3}\alpha_j^{-1/3}>0.
\tag{14}
\]

To see the leading constant, put \(x_j=h^{1/3}y_j\). The quartic and
field part divided by \(h^{4/3}\) is
\(\sum_j(b_jy_j-\alpha_jy_j^4)\), whose unique maximum is \(C\).
Its maximizer is \(y_j=(b_j/(4\alpha_j))^{1/3}\). Every quadratic
interaction enters only with coefficient \(h^{-2/3}\) after this division.
For a completely elementary error bound, sandwich the quadratic form by
\(\pm L\sum_jx_j^2\). The lower bound integrates the box
\(x_j\in[h^{1/3}y_j,h^{1/3}y_j+h^{-1}]\). For the upper bound use
\(Lx^2\le(\varepsilon\alpha_j/2)x^4+L^2/(2\varepsilon\alpha_j)\),
reserve \((\varepsilon\alpha_j/2)x^4\) for integrability, maximize the
remaining quartic-field polynomial, and take \(\varepsilon=h^{-2/3}\).
The resulting exponential losses are \(O(h^{2/3})\) and polynomial
integrals contribute \(O(\log h)\). The fixed normalizer contributes only
a constant. All constants here depend on the fixed network; (14) alone
cannot be passed uniformly through a changing network sequence.

Thus no fixed finite coupled-quartic law equals theta, even though it is
stable, heat compatible, and outside Note 02's nonnegative-potential cone.
The persistent-site theorem is what extends this observation to growing
networks in a nontrivial, carefully stated way.

## 5. What remains open and how the controls apply

To evade (11), a putative approximating sequence must change every
retained diffuse quartic site's effective parameters: for example,
readout weights can tend to zero, quartic stiffness can diverge, or the
site can tend to a sharply concentrated two-well/discrete-spin seed.
The theorem supplies a necessary escape, not a construction or an
exclusion of those escapes. It does not exclude general initially
interacting Ising limits. In particular, the theorem must not be extended to arbitrary Ising scaling limits: [Camia–Garban–Newman](https://arxiv.org/abs/1307.3926) give critical planar magnetization limits with a different tail exponent. No planar approximation to theta is asserted here.

The actual theta field is tested by the comparison of the exact Laplace
growth rates. This theorem is an obstruction within a specified
construction class and does not claim a generic real-zero criterion.
For any putative stable approximation to the collision controls in
result-summary 12, the failed premise remains complex-compact convergence
on a slice where that control has a nonreal zero: time zero for the
Euler-factor controls and a positive pre-collision slice for weighted-square,
reflected, and smooth/positive-primitive controls. Hurwitz excludes that
convergence; none of those controls is assigned an uncomputed quartic
parameter representation.

**Pre-review research consequence.** Keep the broad interacting direction
open, but replace “append more quartic blocks while retaining a fixed diffuse seed”
by the sharper necessary condition (11). The only surviving quartic-network
approximation regime is one in which no diffuse site persists at fixed
readout scale. A uniformly bounded parameter box with a nonvanishing
readout site is therefore closed by a written analytic obstruction,
without a moment-fit campaign. All claims await the formal round review.

The requested [working manuscript](../../manuscript/constructive_stable_models.tex) integrates these results with the bounded certificates from Notes 01–02. It is explicitly unreviewed; its creation at the user’s request is not an accepted manuscript milestone.

## 6. Exact local clarification and reproducibility

For independent pure-quartic \(X,Y\), the source of \(X+Y/4\) has
\[
0.97<[s^4](-\log\rho(s))<0.99,\qquad
-0.25<[s^6](-\log\rho(s))<-0.11.
\]
The [exact rational checker](../../numerics/round-1/certify_unequal_quartic_convolution.py)
and [record](../../numerics/round-1/UNEQUAL_QUARTIC_CONVOLUTION_CERTIFICATE.json)
verify these bounds by enumerating the Taylor expansion through degree
six and using \(1/12<m^2<1/4\),
\(m=\Gamma(3/4)/\Gamma(1/4)\). The fixed contract is \(\delta=1/4\),
three coefficients, exact Fraction arithmetic, no quadrature, no parameter
grid and no refinement; it followed an analytic derivation and scout.
Thus even independence of continuous quartic blocks does not force the
nonnegative-potential cone from Note 02. The new global theorem excludes
this independent approximation route anyway. No theta fit is asserted.

The manuscript gives the formulas, finite coefficient calculation,
field-growth arguments and scope of the remaining interacting regime.
