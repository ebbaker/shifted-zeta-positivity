# Audit of character packets, weighted adjoints, currents, and prime domains

25 September 2026, America/New_York. Prepared for Edward Baker with substantial LLM assistance.

Model exposed: GPT-6 (Codex). Exact deployed variant and reasoning effort: unavailable; not inferred.
Baseline: `12a39447c8ef41cfbf9ca1db60e73f78d5ef8c49`. The working tree was clean when this audit began.

Status: rederivation with proofs, not independent human verification. No RH or positive Weil-source theorem. The [character note](../notes/CHARACTER_CHANNEL_LIMITS_AND_PRIME_MIXED_PAIRINGS_20260925.md) is the object of this audit, not an assumed theorem. The [new continuation](../notes/ELECTRIC_PARITY_ARCHIMEDEAN_RESPONSE_AND_PHASE_OBSTRUCTION_20260925.md) uses only the conclusions below.

## 1. Verdict and scope corrections

The displayed weighted-adjoint, branching, fixed-prime mixed-limit, distributional prime-tail, and identity-phase current formulas survive rederivation. No numerical counterexample to these formulas was found, and none is asserted. There are two material qualifications to carry forward:

1. Negative-Sobolev membership of the prime insertion is **distributional well-definedness**, not admissibility as an OS Hilbert source or as a Hilbert-valued operator on the character core. The phrase “same admissibility” in the earlier note has been replaced accordingly. No Hilbert adjoint of the infinite insertion is supplied by that argument.
2. The exceptional phase at pi has the **opposite** limiting current. Thus even winding by two, whose leading divergent current term vanishes, does not intertwine the identity-phase derivative. Equation (A7) below fills this substantive gap in the phase analysis. Treating that exception as a common finite arithmetic current would be false.

There is also a stronger obstruction than the earlier packet calculation: the unrenormalized infinite positive prime-difference form has domain **only zero on the entire closed one-plaquette class space**, not merely divergent values on the selected packets. This is proved in §6.

## 2. Metric and actual adjoints

All statements use the same four-dimensional SU(2) Wilson slab: spatial `6^3`, time slices -2 through 2, beta=8/5, theta angle zero, and boundary measure `dnu=Z^{-1} Omega^2 dm`. The four-link plaquette has smooth positive central marginal rho(g) dg. This follows by changing one of its distinct link variables to the plaquette product and integrating the remaining compact variables. In particular rho and its reciprocal are smooth and bounded. No explicit interacting density is assumed.

For characters chi_n(theta)=sin(n theta)/sin(theta), normalized Haar integration gives

\[
G_{nm}=t_{n-m}-t_{n+m},\qquad
t_k=\pi^{-1}\int_0^\pi\rho(\theta)\cos(k\theta)\,d\theta.
\tag{A1}
\]

The even periodic extension is smooth, so t_k decreases faster than any power. The norm is comparable to the coefficient l2 norm. In particular t_0-t_2=1; setting t_0=1 would generally be wrong.

The unitary map W F=sqrt(2) sin(theta) F identifies this space with the odd subspace of L2(S1,rho dtheta/(2pi)). Here V_a becomes C_a A(theta)=A(a theta). Splitting the circle into a equal arcs gives, for arbitrary odd smooth A,B,

\[
\langle A,C_aB\rangle_\rho
=\langle\rho^{-1}L_a(\rho A),B\rangle_\rho,
\quad L_a h(\theta)=a^{-1}\sum_{j=0}^{a-1}h((\theta+2\pi j)/a).
\]

Thus

\[
WV_a^{*\nu}W^{-1}=\rho^{-1}L_a\rho,\qquad
WV_a^{*\nu}V_aW^{-1}=M_{\rho_a/\rho},\quad\rho_a=L_a\rho.
\tag{A2}
\]

Evenness of rho and oddness of A ensure that the transfer remains odd. These are adjoints on the closed class space, not unrestricted operations on every boundary observable. The Haar divisibility formula for V_a^* cannot be substituted for (A2). The uniform norm bound sqrt(C_rho/c_rho) and composition V_a V_b=V_ab do hold in the actual metric.

## 3. Phases and the mixed limit

Write N=exp R and c_n^f=n^{-1/2} f(log(n/N)). For fixed compact supports, n lies in [cN,CN]. Riemann sums give sum conjugate(c_n^f)c_n^g -> <f,g>. Fixed integer shifts of n have the same limit. In the Toeplitz term of (A1), the shifted phase factor is exp(i alpha k) for equal phases; summation over k gives rho(alpha). For unequal phases, summation by parts in n gives zero, dominated by a constant times |t_k|. The Hankel contribution is O(N^{1-M}) for every M. Consequently

\[
\langle S_R^\alpha f,S_R^\beta g\rangle_\nu
\longrightarrow\mathbf1_{\alpha=\beta\ (2\pi)}\langle f,g\rangle.
\tag{A3}
\]

This also applies to alpha and -alpha: their common angular concentration does not remove their opposite oscillatory carriers. They are distinct components except at 0 and pi.

For beta_j=(alpha+2pi j)/a, the coefficient filter sum_j exp(i beta_j n) is zero unless a divides n, when it equals a exp(i alpha n/a). It proves the **finite-R** identity

\[
V_aS_R^\alpha f={1\over\sqrt a}\sum_{j=0}^{a-1}
\sqrt{\rho(\beta_j)/\rho(\alpha)}\,
S_R^{\beta_j}U_{\log a}f.
\tag{A4}
\]

Using (A3), only beta_0=0 pairs with the identity phase. Hence the claimed coefficient is exactly a^{-1/2}, without a Haar replacement. Intersecting the two root sets for a,b gives d=gcd(a,b) roots and the coefficient d rho_d(0)/(sqrt(ab) rho(0)) of the earlier note. Fixed phases are essential; the proof is not uniform when distinct phases approach each other as R varies. Nor is point sampling a bounded map from input L2 at finite R.

## 4. Infinite insertion: what its domain actually is

On the finite character span define L=sum_{a>=2} Lambda(a) V_a. With the full Haar electric Laplacian E_0 chi_n=4(n^2-1)chi_n,

\[
\|\mathcal L\chi_m\|_{H^{-s}}^2
=\sum_{a\ge2}\Lambda(a)^2(1+4((am)^2-1))^{-s}<\infty
\quad(s>1/2).
\tag{A5}
\]

This uses orthogonality before changing the weight. Smooth multiplication by the full boundary density defines the actual distribution pairing and preserves these Sobolev spaces. For any smooth class function with rapidly decreasing character coefficients b_n, the coefficient of chi_k is sum_{n|k,n<k} Lambda(k/n)b_n, of size at most log(k) sum_n |b_n|. Dominated convergence in H^{-s}, s>1/2, therefore also defines L continuously on the smooth class space. This is an extension of the earlier core statement, not an extension to all Hilbert vectors.

Already L chi_1 is not L2, since its coefficients Lambda(a) are not square summable. More generally no nonzero finite character combination has an L2 image: take its smallest nonzero label m, and primes p larger than all its labels. The coefficient at mp is b_m log p; a different fixed label can divide mp only by dividing m, which contradicts minimality if its coefficient is nonzero. Norm equivalence transfers the conclusion to nu. In particular the displayed distribution is not a densely defined Hilbert operator **with this core as domain**. No conclusion about other possible domains is intended.

For the actual finite packets, their coefficient l1 norms are O(sqrt N). If a>A_0>2 max(C_f/c_g,C_g/c_f,1), all indices n-am, an-m, n+am, an+m in the two pairings have absolute size at least c aN. Equation (A1) yields

\[
|\langle S_R f,V_aS_Rg\rangle|+
|\langle V_aS_Rf,S_Rg\rangle|
\le C_M N^{1-M}a^{-M}.
\tag{A6}
\]

For any M>1 this is summable after multiplication by Lambda(a)<=log a. It justifies the infinite distributional mixed limit and any cofinal cutoff A(R)->infinity for these **raw** packets. The finitely many remaining terms use (A3)-(A4). This is not analytic continuation of the Euler product from Re(s)>1 to zero. The second bracket is the conjugate distribution pairing; writing it as an infinite Hilbert adjoint would be unjustified.

## 5. Full electric current, including the phase at pi

For X=cos theta, ell=4, use the full E_nu and A_nu=i[E_nu,X]/(2ell). Integration by parts gives

\[
A_\nu=-i(Y+\tfrac12\operatorname{div}_\nu Y),\quad
Y=\ell^{-1}\nabla X,\quad
A_\nu-A_0=-i\ell^{-1}\nabla\log\Omega\cdot\nabla X.
\]

The last term is bounded, but generally leaves the class space. The smooth complete flow of Y with its density Jacobian gives the self-adjoint closure on the covariant space. There is no replacement of this operator by a marginal radial operator.

Fusion with X and E_0 chi_n=ell(n^2-1)chi_n give the coefficient action

\[
(A_0c)_n={i\over2}[(n-\tfrac12)c_{n-1}-(n+\tfrac12)c_{n+1}].
\]

For c_n=e^{i beta n}n^{-1/2}f(log(n/N)), Taylor expansion gives leading term n sin(beta)c_n and next term -i cos(beta)n^{-1/2}exp(i beta n)f'. At beta=0 or pi, the next remainder is O(N^{-2}) in the Haar norm. Also ||sin(theta) S_R^beta f||=O(N^{-1}) at these two phases. Since |nabla X|=sqrt(ell)|sin theta|, the actual drift contributes O(N^{-1}). Therefore

\[
\begin{split}
A_\nu S_R^0 f&=S_R^0(-if')+O(N^{-1}),\\
A_\nu S_R^\pi f&=S_R^\pi(+if')+O(N^{-1}),\\
\lim_R\|A_\nu V_2S_Rf-V_2S_R(-if')\|_\nu^2
&=2\rho(\pi)\rho(0)^{-1}\|f'\|_2^2.
\end{split}
\tag{A7}
\]

The last equality uses (A4), so it is a statement in the actual state. At other fixed phases the leading n sin(beta) term survives. Orthogonality of the finitely many roots proves the earlier positive N^2 coefficient for a>=3. Bounded drift cannot cancel it. The identity-phase unitary limit follows by Duhamel on the compact family of translated tests; it supplies no uniform assertion over all phases.

## 6. A zero-domain theorem for the positive prime sum

**Theorem.** On the closed one-plaquette class space, the extended nonnegative form

\[
\mathfrak d(F)=\sum_{a\ge2}\Lambda(a)\|(I-V_a)F\|_\nu^2
\]

is finite only when F=0.

**Proof.** First V_a F converges weakly to zero as a->infinity. This holds against character tests for character inputs by (A1); density and the uniform operator bound extend it to arbitrary inputs and tests. By (A2) and uniform convergence rho_a->t_0,

\[
\|V_aF\|_\nu^2\longrightarrow t_0\|F\|_{\rm Haar}^2.
\]

Thus ||(I-V_a)F||_nu^2 tends to ||F||_nu^2+t_0||F||_Haar^2, strictly positive for F nonzero. The sum of Lambda(a) diverges (even powers of 2 suffice). This proves the claim. Square-summability of an auxiliary direct sum cannot evade the same calculation. \(\square\)

This is a scoped obstruction for these coefficients and operations in this source sector. Pole-neutral input constraints do not change it for any nonzero output F. A separate, independently defined renormalized form is not excluded, but must prove its own positivity and domain. Subtracting sum Lambda(a)(I+V_a^*V_a) leaves a signed form and discards the preceding positive construction.

## 7. Occurrence and verification

The packet weak limit is zero, its norm tends to ||f||, and its weighted elliptic H^r norm is comparable to N^r for nonzero f. Haar spectral localization proves the latter, followed by equivalence of Sobolev norms for the fixed smooth weight. The compact-source theorem's uniform balls therefore fail even for a single nonzero fixed test. Weak compactness does not repair this failure.

The original 57 floating checks were rerun unchanged and all passed (largest recorded asymptotic error 8.5953e-6). They use Haar and a prescribed trigonometric density, **not** the interacting Wilson marginal. The proofs above use only the actual marginal lemma and full weighted electric calculus. The new [control script](../numerics/check_archimedean_response.py) separately tests the pi-phase sign, logarithmic response, parity, and phase divergence; neither set of controls proves a limit or supplies an occurrence theorem.
