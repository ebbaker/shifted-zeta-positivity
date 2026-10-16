# Character channels: native prime mixed pairings and the remaining source problem

25 September 2026, America/New_York.

Prepared for Edward Baker with substantial LLM assistance.

Model: GPT-6 (Codex). The deployed variant and reasoning effort are not exposed; neither is inferred.

Status: new analytical deductions and floating algebra controls, not independently reviewed. The fixed four-dimensional YM model is retained. No full Weil realization or RH proof is established.

Subsequent same-day [critical rederivation](../reviews/CHARACTER_CURRENT_AND_PRIME_DOMAIN_AUDIT_20260925.md): the displayed mixed-limit, weighted-adjoint, branching and prime-tail formulas survive, with the distributional domain clarified below. The phase at pi has the opposite finite current, so winding by two also fails the derivative intertwining. The infinite positive prime-difference form has domain only zero on the entire class space. The [archimedean continuation](ELECTRIC_PARITY_ARCHIMEDEAN_RESPONSE_AND_PHASE_OBSTRUCTION_20260925.md) now derives a complete signed mixed response, including its contact constant, but proves additional phase and source-occurrence obstructions; it supplies no positive Weil source.

## 1. What this continuation obtains

The character-weighted winding operations proposed in the [topology and observable assessment](TOPOLOGY_GEOMETRY_AND_CHARACTER_OBSERVABLE_OPTIONS_20260925.md) have a useful mixed pairing in the actual YM state. There is an independently specified family of finite character packets \(S_R f\) such that, for every fixed integer \(a\ge1\),
\[
\lim_{R\to\infty}\langle S_R f,V_a S_R g\rangle_\nu
 =a^{-1/2}\langle f,U_{\log a}g\rangle_{L^2(\mathbb R)}.
\tag{1}
\]
Combining this with the logarithmic derivative of the native operator Euler product gives precisely the prime-power coefficients in the Weil pairing. The factor \(a^{-1/2}\) is a consequence of the covering of integer representation labels and the packet normalization, rather than an assigned matrix coefficient.

The calculation also exposes its limitations. The packets converge weakly to zero and retain nonzero norm: they do not give a nonzero limiting source in the original physical Hilbert space. Positive squared differences involving \(V_a\) generate a divergent local term when summed over all prime powers. The archimedean term and its contact normalization have not been derived.

There are two further results. Rational phase components account exactly for winding's additional norm; in the Haar comparison their completion is \(L^2(\mathbb R\times\widehat{\mathbb Z})\). A current defined by the full YM electric operator and one Wilson scalar approaches arithmetic differentiation on the identity phase component, but grows without bound on several components produced by winding. These are concrete operator relations to investigate, not a demonstrated arithmetic source module inside YM.

## 2. Fixed state and the character metric

Retain pure \(SU(2)\), theta zero, the spatial \(6^3\) torus, open physical-time slices \(-2,-1,0,1,2\), and Wilson coupling \(\beta=8/5\). On the central spatial link manifold \(M\), the actual boundary state is
\[
d\nu=Z^{-1}\Omega^2\,dm,\qquad
\mathcal H=L^2_{\rm cov}(M,\nu;\operatorname{End}\mathbb C^2),
\quad
\langle A,B\rangle_\nu=\int\tfrac12\operatorname{tr}(A^\dagger B)\,d\nu .
\]
Here \(\Omega\) is the positive half-slab amplitude specified in §2 of the [winding-source note](NATIVE_WINDING_MELLIN_SOURCES_AND_ELECTRIC_PAIRING_20260925.md). It is smooth, strictly positive, and gauge invariant. Fix the same elementary spatial plaquette holonomy \(P\), whose \(\ell=4\) underlying links are distinct. Its actual marginal is \(\rho(g)\,dg\), where \(dg\) is normalized Haar measure and
\[
0<c_\rho\le \rho\le C_\rho<\infty.
\]
The marginal lemma in that note proves this without a sampling assumption. No explicit formula for the interacting \(\rho\) is assumed here.

Write
\[
\chi_n(\theta)=\frac{\sin(n\theta)}{\sin\theta},\quad n\ge1,
\qquad
t_k=\frac1\pi\int_0^\pi\rho(\theta)\cos(k\theta)\,d\theta.
\]
Thus \(\rho(\theta)=\sum_{k\in\mathbb Z}t_ke^{ik\theta}\); \(t_k\) is real, even and rapidly decreasing. The normalization is \(t_0-t_2=1\), not necessarily \(t_0=1\).

We identify scalar class functions with \(F(P)I\) in \(\mathcal H\). Product-to-sum gives the exact Gram matrix
\[
G_{nm}:=\langle\chi_n(P),\chi_m(P)\rangle_\nu
 =t_{n-m}-t_{n+m}.
\tag{2}
\]
Indeed Haar's radial measure is \((2/\pi)\sin^2\theta\,d\theta\). This is equivalent to the fusion-moment formula in the preceding assessment. For all finite coefficient sequences \(c\),
\[
c_\rho\sum|c_n|^2\le
\Big\|\sum c_n\chi_n(P)\Big\|_\nu^2
\le C_\rho\sum|c_n|^2.
\tag{3}
\]

Define the same observable operations as before:
\[
(V_aF)(g)=\chi_a(g)F(g^a),\qquad
V_a\chi_n=\chi_{an},\qquad V_aV_b=V_{ab}.
\tag{4}
\]
They are uniformly bounded, with \(\|V_a\|_\nu\le(C_\rho/c_\rho)^{1/2}\). No new spatial topology or physical field has been introduced.

### Actual adjoints

The map
\[
(WF)(\theta)=\sqrt2\sin\theta\,F(\theta)
\]
identifies the class space with odd functions in \(L^2(S^1,\rho(\theta)d\theta/(2\pi))\). Under it \(V_a\) becomes \(C_a A(\theta)=A(a\theta)\). Put
\[
(L_aB)(\theta)=\frac1a\sum_{j=0}^{a-1}
 B\!\left(\frac{\theta+2\pi j}{a}\right),\qquad
\rho_a=L_a\rho.
\]
A change of variables on the circle proves
\[
WV_a^{*\nu}W^{-1}=M_\rho^{-1}L_aM_\rho,\qquad
V_a^{*\nu}V_a=M_{\rho_a/\rho}.
\tag{5}
\]
Here the adjoint is on this closed class-function space; an extension to all of \(\mathcal H\) is not needed. Fourier expansion gives
\[
\rho_a(\theta)=\sum_{k\in\mathbb Z}t_{ak}e^{ik\theta}
 \longrightarrow t_0
\]
in every fixed \(C^r\) norm, faster than any inverse power of \(a\).

In the separate Haar control, \(V_a^*\chi_n=\chi_{n/a}\) when \(a\mid n\), and is zero otherwise. It follows on the character basis that
\[
V_a^*V_b=V_{b/d}V_{a/d}^*,\qquad d=\gcd(a,b).
\]
This last formula is a Haar adjoint identity; (5) is the formula in the interacting metric.

## 3. One packet law on every compactly supported input

Use \(\mathcal D=C_c^\infty(\mathbb R)\), \(\langle f,g\rangle=\int\overline f g\), and \(U_tg(x)=g(x-t)\). For \(R\in\mathbb R\), \(N=e^R\), and a fixed phase \(\alpha\in\mathbb R/(2\pi\mathbb Z)\), define
\[
S_R^\alpha f
 =\rho(\alpha)^{-1/2}
   \sum_{n\ge1}n^{-1/2}e^{i\alpha n}
        f(\log n-R)\,\chi_n(P)I,
\qquad S_R=S_R^0.
\tag{6}
\]
For each \(R\) and \(f\) this is a finite sum of smooth gauge-invariant observables. It is a continuous linear map from the usual smooth-test space into the physical boundary space. The same prescription applies to all supports; \(R\) moves the representation scale, not the model or state.

The half-density \(n^{-1/2}\) converts counting representation labels into logarithmic measure. The phase \(e^{i\alpha n}\) is a fixed operation on those labels. The positive normalizing factor uses the actual marginal at \(\alpha\); no zeta zeros, prime coefficients, or desired Weil moments enter (6). Unlike the earlier critical Mellin law, this prescription samples \(f\) itself, rather than \(\widehat f\). That is an explicit change of source ansatz.

**Theorem 1 (phase pairings).** For fixed \(f,g\in\mathcal D\) and fixed phases,
\[
\lim_{R\to\infty}\langle S_R^\alpha f,S_R^\beta g\rangle_\nu
 =
\begin{cases}
\langle f,g\rangle,&\alpha=\beta\pmod{2\pi},\\
0,&\alpha\ne\beta\pmod{2\pi}.
\end{cases}
\tag{7}
\]

**Proof.** Put \(c_n^f=n^{-1/2}f(\log(n/N))\). The logarithmic Riemann sum gives
\[
\sum_n\overline{c_n^f}c_n^g
 =\sum_n\frac1n\overline{f(\log(n/N))}g(\log(n/N))
 \longrightarrow \int\overline f g .
\]
The same limit holds if one coefficient index is shifted by a fixed integer \(k\). The supports lie between two positive constant multiples of \(N\), and all derivatives of the envelopes have the corresponding powers of \(N^{-1}\).

For the Toeplitz part \(t_{n-m}\) of (2), write \(m=n+k\). If the phases agree, its fixed-\(k\) coefficient tends to \(e^{i\alpha k}\langle f,g\rangle\). If they differ, summation by parts against \(e^{i(\beta-\alpha)n}\) makes that coefficient tend to zero. Cauchy–Schwarz and bounded coefficient \(\ell^2\) norms give a summable dominating bound \(\mathrm{const}\,|t_k|\). Summing over \(k\) therefore gives \(\rho(\alpha)\langle f,g\rangle\) in the equal-phase case.

The Hankel term \(t_{n+m}\) tends to zero: both indices are of order \(N\), so its absolute sum is \(O(N^{1-M})\) for every fixed decay exponent \(M\). Divide by \(\sqrt{\rho(\alpha)\rho(\beta)}\). This proves (7). \(\square\)

The proof also works for any finite set of inputs and phases simultaneously. It does not claim an operator-norm limit on \(L^2(\mathbb R)\); finite-\(R\) point sampling is not an \(L^2\)-bounded operation. For arbitrary phases and complex envelopes, finite-scale errors need not be \(O(N^{-2})\).

### Exact branching, before any limit

For every \(a\ge1\), put \(\beta_j=(\alpha+2\pi j)/a\) modulo \(2\pi\). Then
\[
V_a S_R^\alpha f
 =\frac1{\sqrt a}\sum_{j=0}^{a-1}
       \sqrt{\frac{\rho(\beta_j)}{\rho(\alpha)}}
       S_R^{\beta_j}(U_{\log a}f).
\tag{8}
\]
This is an exact equality of finite physical observables for every \(R\). To check it, use
\[
\frac1a\sum_{j=0}^{a-1}e^{2\pi ijn/a}=\mathbf1_{a\mid n}
\]
in the character coefficient on the right. When \(n=am\), that coefficient is
\(\rho(\alpha)^{-1/2}m^{-1/2}e^{i\alpha m}f(\log m-R)\), as on the left.

Theorem 1 and (8) prove (1): only the root \(\beta=0\) pairs with the identity component. Thus \(a^{-1/2}\) measures one component of an actual winding operation; the remaining components have not been thrown away.

More generally, for \(d=\gcd(a,b)\),
\[
\lim_{R\to\infty}\langle V_aS_R f,V_bS_R g\rangle_\nu
 =\frac{d\,\rho_d(0)}{\sqrt{ab}\,\rho(0)}
      \langle f,U_{\log(b/a)}g\rangle.
\tag{9}
\]
The common phases in the two root sets are \(2\pi j/d\). Summing their weights in (8), and using
\(\langle U_{\log a}f,U_{\log b}g\rangle
=\langle f,U_{\log(b/a)}g\rangle\), proves the formula. In particular,
\[
\lim_R\|V_aS_R f\|_\nu^2
 =\frac{\rho_a(0)}{\rho(0)}\|f\|_2^2.
\tag{10}
\]
This agrees with the actual norm defect (5).

## 4. A prime-power identity in mixed physical pairings

On the actual class space, uniform boundedness and (4) give the norm-convergent identities
\[
\mathcal Z_V(s)=\sum_{a\ge1}a^{-s}V_a
 =\prod_p(I-p^{-s}V_p)^{-1},\qquad
-\mathcal Z_V'(s)\mathcal Z_V(s)^{-1}
 =\sum_{a\ge2}\Lambda(a)a^{-s}V_a,
\quad\operatorname{Re}s>1.
\tag{11}
\]
Here \(\Lambda(p^k)=\log p\), and \(\Lambda(a)=0\) otherwise. Absolute convergence, unique factorization and the absolutely convergent Möbius inverse suffice; RH plays no role.

For a finite integer cutoff \(A\), take the operator polynomial
\[
\mathcal L_A=\sum_{2\le a\le A}\Lambda(a)V_a .
\]
Using (1) and its adjoint pairing gives
\[
\begin{aligned}
\lim_{R\to\infty}\big[
 \langle S_R f,\mathcal L_A S_R g\rangle_\nu
 +\langle\mathcal L_A S_R f,S_R g\rangle_\nu\big]
 =\sum_{2\le a\le A}\frac{\Lambda(a)}{\sqrt a}
 \big[\langle f,U_{\log a}g\rangle+
      \langle f,U_{-\log a}g\rangle\big].
\end{aligned}
\tag{12}
\]

The negative of the right side is exactly the prime part of \(Q(f,g)\). For fixed compact supports it stabilizes once \(\log A\) exceeds all their possible separations. One can also control the physical tail and define the infinite insertion as a distribution, as follows.

On the finite character span define
\[
\mathcal L F=\sum_{a\ge2}\Lambda(a)V_aF
\]
as a negative-Sobolev distribution. For a single character \(\chi_m(P)\), its Haar coefficients are \(\Lambda(a)\) at labels \(am\). By (17), the series converges in \(H^{-s}(M)\) for every \(s>1/2\), since
\(\sum_{a\ge2}a^{-2s}(\log a)^2<\infty\).
Finite linear combinations follow. Smooth multiplication by the actual state density defines its pairing with smooth physical test vectors, and equivalence of weighted Sobolev norms gives the same distributional well-definedness in that state. This is not admissibility as an OS Hilbert source or a Hilbert-valued insertion on this core. Explicitly,
\[
\langle\chi_n,\mathcal L\chi_m\rangle_\nu
 =\sum_{a\ge2}\Lambda(a)(t_{n-am}-t_{n+am})
\]
is absolutely convergent. This is not a Hilbert-valued operator on the character span: already \(\mathcal L\chi_1\) has non-square-summable coefficients.

For completeness, the tail estimate is particularly simple. Enclose the supports so that the nonzero packet indices satisfy
\(c_fN\le n\le C_fN\) and \(c_gN\le m\le C_gN\), with positive constants. Choose
\[
A_0>2\max(C_f/c_g,C_g/c_f,1).
\]
For \(a>A_0\), both Toeplitz index separations in the two mixed pairings are bounded below by a positive constant times \(aN\). The Hankel indices have the same bound. The coefficient \(\ell^1\) norms are \(O(\sqrt N)\). Consequently, for every fixed \(M_0>1\) and all large \(N\),
\[
|\langle S_R f,V_a S_R g\rangle_\nu|
 +|\langle V_a S_R f,S_R g\rangle_\nu|
 \le C_{f,g,\rho,M_0}N^{1-M_0}a^{-M_0}.
\]
Multiplication by \(\Lambda(a)\le\log a\) leaves a summable bound. The whole tail beyond \(A_0\) therefore vanishes as \(R\to\infty\), uniformly in an upper cutoff. The finite remaining terms converge by (12). This proves
\[
-\lim_{R\to\infty}
 \big[\langle S_R f,\mathcal L S_R g\rangle_\nu+
      \langle\mathcal L S_R f,S_R g\rangle_\nu\big]
 =Q_{\rm prime}(f,g)
\tag{13}
\]
for every pair of tests, with the brackets understood as distribution–smooth-vector pairings. It also proves the same limit for cutoffs \(A(R)\to\infty\), and the iterated limit obtained directly from (12).

This argument uses a distributional insertion and smoothness of the actual marginal. It does not assert an analytic continuation of (11) to \(s=0\), convergence in bounded operators, or a Hilbert norm for \(\mathcal L S_Rg\). At finite \(R\), interacting correlations need not vanish at large \(a\); their controlled decay suffices.

Equation (13) supplies genuine mixed matrix coefficients with the required arithmetic weights. However, it is a signed insertion pairing rather than the norm of a single source. The coefficient in (1) is also universal over smooth positive marginal densities, after the specified normalization. Its origin is the character and integer-covering algebra; it has not been shown to express special four-dimensional YM dynamics.

## 5. Rational phases and a profinite comparison

Admit all packets (6) with \(\alpha\in2\pi\mathbb Q/(2\pi\mathbb Z)\). This countable set contains zero and is closed under every root operation in (8). Theorem 1 defines the positive limiting completion
\[
\mathcal K_\infty=\bigoplus_{\alpha\in2\pi\mathbb Q/(2\pi\mathbb Z)}
                         L^2(\mathbb R).
\tag{14}
\]
On finite sums, the limiting \(V_a\) is exactly the weighted branching map (8). Distinct input phases have disjoint root sets, so
\[
\|\mathcal V_a\|^2\le C_\rho/c_\rho,\qquad
\mathcal V_a\mathcal V_b=\mathcal V_{ab}.
\]
The latter identity follows either from (8) twice or from cancellation of its intermediate density ratios. We explicitly admitted the individual phase-modulated packets; it is not asserted that applying only \(V_a\) to the identity component isolates every phase.

In the **Haar comparison** \(\rho=1\), finite cyclic Fourier transforms, followed by completion over all denominators, identify
\[
\ell^2(\mathbb Q/\mathbb Z)\cong L^2(\widehat{\mathbb Z},d\mu),
\qquad
\mathcal K_\infty^{\rm Haar}
 \cong L^2(\mathbb R\times\widehat{\mathbb Z},dx\,d\mu).
\]
Here \(\widehat{\mathbb Z}=\varprojlim_q\mathbb Z/q\mathbb Z\), with probability Haar measure. The branching formula becomes
\[
(\mathcal V_aF)(x,z)
 =\sqrt a\,\mathbf1_{a\widehat{\mathbb Z}}(z)
         F(x-\log a,z/a).
\tag{15}
\]
Multiplication by \(a\) is injective on \(\widehat{\mathbb Z}\), and its image has measure \(1/a\). Thus (15) is an isometry. On a rational character, the indicator is precisely the finite root-of-unity filter proving (8).

The extra arithmetic topology has therefore appeared as a limit of representation-label phases; spatial handles were not inserted by hand. For the actual state the density ratios in (8) must remain. This comparison is not a full adele class space, a trace formula, or an embedding of that new limiting Hilbert space as a physical source module.

## 6. Why this limit does not yet give a source in the fixed YM space

For any nonzero \(f\) and fixed phase,
\[
S_R^\alpha f\rightharpoonup0
\quad\hbox{in }\mathcal H,\qquad
\|S_R^\alpha f\|_\nu\longrightarrow\|f\|_2>0.
\tag{16}
\]
For a fixed character, (2) and rapid decay of \(t_k\) make the mixed pairing tend to zero. The characters are dense in the closed class subspace, and packet norms are bounded, proving weak convergence there. Orthogonal projection onto that subspace proves weak convergence against every vector of \(\mathcal H\). The norm limit follows from (7). No strongly convergent subsequence is possible.

The electric compactness criterion also fails for these raw packets. Let
\[
E_\nu=\sum_{\text{spatial links},\,j}D_j^{*\nu}D_j
\]
be the full weighted Friedrichs operator on the covariant space, with the generator normalization from the preceding winding note. Its Haar counterpart obeys
\[
E_0\chi_n(P)=\ell(n^2-1)\chi_n(P),\qquad \ell=4.
\tag{17}
\]
Weighted and Haar elliptic Sobolev norms on this fixed compact manifold are equivalent. Since the packet labels satisfy \(c_fN\le n\le C_fN\), (17) and (3) give, for every fixed \(r>0\),
\[
\|(1+E_\nu)^{r/2}S_R^\alpha f\|_\nu
 \asymp_{f,r,\nu}N^r .
\tag{18}
\]
For sufficiently large \(R\), both comparison constants are positive when \(f\ne0\). The state and the operators are fixed in this statement.

Thus the packets are not inside one of the fixed compact source balls required by the [finite-compatibility theorem](OFF_DIAGONAL_RIGIDITY_AND_COMPACT_SOURCE_EXISTENCE_20260924.md). The limiting construction (14) retains escaped norm in a new representation. An abstract isometric placement into the infinite-dimensional original Hilbert space would not prove occurrence of the required observable relations there.

Moreover, the bare limiting pairing is ordinary \(L^2\). It fails the target's logarithmic growth on pole-neutral modulations. Any proposal using these packets must add a justified insertion or source relation, as well as resolve occurrence.

## 7. A native electric current, with its precise limitation

There is a more informative physical operator than the electric energy alone. Put
\[
X(U)=\tfrac12\operatorname{tr}P=\cos\theta,\qquad
\mathcal A_\nu=\frac{i}{2\ell}[E_\nu,M_X]
\tag{19}
\]
initially on smooth covariant observables. On the product link manifold,
\[
\mathcal A_\nu
 =-i\big(Y\cdot\nabla+\tfrac12\operatorname{div}_\nu Y\big),
\qquad Y=\ell^{-1}\nabla X .
\tag{20}
\]
The smooth vector field \(Y\) is complete on compact \(M\). Its flow, with the square-root density Jacobian, gives a strongly continuous unitary group; (20) has the corresponding self-adjoint closure. Gauge invariance of \(X\), the metric and \(\nu\) preserves the covariant sector. This is a native nonperiodic transport candidate, not the physical transfer Hamiltonian.

It is essential here to use the **full** \(E_\nu\). In general it does not preserve functions of \(P\) alone. A marginal radial operator cannot silently replace it.

For the Haar comparison, multiplication by \(X=\chi_2/2\), character fusion and (17) give the exact formula
\[
\mathcal A_0\chi_n
 =\frac i2\big[(n+\tfrac12)\chi_{n+1}
                  -(n-\tfrac12)\chi_{n-1}\big],
\qquad \chi_0=0.
\tag{21}
\]
Thus its coefficient action is
\[
(\mathcal A_0c)_n
 =\frac i2\big[(n-\tfrac12)c_{n-1}
                    -(n+\tfrac12)c_{n+1}\big].
\]
For \(c_n=n^{-1/2}f(\log(n/N))\), Taylor expansion of this central difference gives
\[
\|\mathcal A_0S_R f-S_R(-if')\|_{\rm Haar}
 =O_f(N^{-2}).
\tag{22}
\]
In this formula the fixed scalar normalization \(\rho(0)^{-1/2}\) can be retained; it changes only the bound's constant. The half-density cancels the zeroth-order derivative contribution.

The actual state adds only a bounded multiplication term:
\[
E_\nu=E_0-2\nabla\log\Omega\cdot\nabla,\qquad
\mathcal A_\nu-\mathcal A_0
 =-\frac i\ell M_{\nabla\log\Omega\cdot\nabla X}.
\tag{23}
\]
For the distinct-link plaquette, \(|\nabla X|^2=\ell\sin^2\theta\). The fixed gradient of \(\log\Omega\) is bounded, and a two-step coefficient-difference estimate gives
\(\|\sin\theta\,S_R f\|_\nu=O_f(N^{-1})\).
This follows directly by multiplying \(\sum c_n\sin(n\theta)\) by \(\sin\theta\); its cosine coefficients are differences of neighboring \(c_n\)'s. Using (3), (22) and (23) proves the full physical estimate
\[
\boxed{\ \|\mathcal A_\nu S_R f-S_R(-if')\|_\nu=O_f(N^{-1})\ .\ }
\tag{24}
\]
The error constant uses the fixed state and a finite collection of smooth seminorms of \(f\).

For each fixed \(t\), Duhamel's formula and the same estimate on the compact family \(\{U_s f:|s|\le |t|\}\) also give
\[
\|e^{-it\mathcal A_\nu}S_R f-S_R U_t f\|_\nu\longrightarrow0.
\tag{25}
\]
This is a genuine arithmetic translation limit for these physical packets. It is not a limiting source in \(\mathcal H\), because of (16). The single-current norm tends to \(\|f'\|_2^2\), not to the Weil form; on high-frequency profiles it has quadratic rather than logarithmic growth.

There is a further compatibility obstruction. For a fixed phase \(\beta\),
\[
\mathcal A_\nu S_R^\beta f
 =N\sin\beta\,S_R^\beta(e^x f)+O_{\mathcal H,f,\beta}(1).
\tag{26}
\]
This follows from the leading coefficient in (21); the bounded drift in (23) cannot change it. Combining (26), (8) and (7) yields, for \(a\ge3\),
\[
\lim_{R\to\infty}N^{-2}\|\mathcal A_\nu V_aS_R f\|_\nu^2
 =\frac{a}{\rho(0)}
   \sum_{j=0}^{a-1}\rho(2\pi j/a)\sin^2(2\pi j/a)
   \int e^{2x}|f(x)|^2\,dx>0
\tag{27}
\]
when \(f\ne0\). For Haar the coefficient is \(a^2/2\). At \(a=2\) the leading term vanishes, since its roots are \(0,\pi\).

Consequently (24) does not supply one finite limiting current on the whole rational-phase space closed under winding. The subsequent audit also proves \(\mathcal A_\nu S_R^\pi f=S_R^\pi(+if')+O(N^{-1})\): the phase at pi has the opposite current, and \(\|\mathcal A_\nu V_2S_Rf-V_2S_R(-if')\|^2\to2\rho(\pi)\rho(0)^{-1}\|f'\|^2\). Thus the exceptional case a=2 is not an intertwining repair. Inserting a desired digamma function of a generator would also require a separate physical derivation and domain analysis; (24) or (25) alone supplies neither. A native generator remains optional for the bare source-existence objective.

## 8. Positivity exposes a divergent contact term

Consider the most direct positive-form assembly from the prime operations. Equations (1), (7) and (10) give
\[
\lim_R\|(I-V_a)S_R f\|_\nu^2
 =\left(1+\frac{\rho_a(0)}{\rho(0)}\right)\|f\|_2^2
   -\frac2{\sqrt a}\operatorname{Re}\langle f,U_{\log a}f\rangle.
\tag{28}
\]
Therefore the finite positive sum
\(\sum_{2\le a\le A}\Lambda(a)\|(I-V_a)S_R f\|_\nu^2\)
has, after \(R\to\infty\), exactly the desired negative prime correlations and the extra local coefficient
\[
C_A^\rho=\sum_{2\le a\le A}
 \Lambda(a)\left(1+\frac{\rho_a(0)}{\rho(0)}\right).
\tag{29}
\]
Since \(\rho_a(0)/\rho(0)\ge c_\rho/C_\rho\), \(C_A^\rho\to+\infty\); infinitely many primes already suffice. For fixed compact support the cross terms have stabilized while this contact term still diverges.

This finite sum is a positive form; no embedding of its auxiliary direct sum as one physical source is asserted. More fundamentally, subtracting \(C_A^\rho\|f\|^2\) removes the automatic positivity argument. Adding a positive archimedean sector does not by itself remove the divergence. A viable construction must derive a compatible source normalization, constraint, or subtraction with a proved positive limit.

The archimedean target on the pole-neutral domain
\(\mathcal D^0=(-\partial_x^2+1/4)\mathcal D\) is
\[
Q_\infty(f,g)=\frac1{2\pi}\int_{\mathbb R}
 \big[\operatorname{Re}\psi(1/4+i\tau/2)-\log\pi\big]
 \overline{\widehat f(\tau)}\widehat g(\tau)\,d\tau.
\]
Away from the diagonal its kernel is
\(-e^{-|x-y|/2}/(1-e^{-2|x-y|})\).
Equations (12)–(13) supply the prime shifts, but not this kernel, its logarithmic growth, or the local normalization. After pole removal the prime shifts give the required fourth derivatives of delta distributions from the previous note; the missing gamma part remains necessary.

## 9. What ordinary two-dimensional gluing does in the same limit

This section is a comparison theory with Haar character metric, not a change of the fixed state. For two-dimensional \(SU(2)\) YM, choose area units so the Casimir is \(n^2-1\). The cylinder, zero-area handle and pair-of-pants maps are
\[
P_t\chi_n=e^{-t(n^2-1)}\chi_n,\qquad
H\chi_n=n^{-2}\chi_n,\qquad
\mu(\chi_n\otimes\chi_m)=\delta_{nm}n^{-1}\chi_n.
\]
These are the character specialization of [Runkel–Szegedy, Proposition 5.7, (5.30)–(5.34)](https://doi.org/10.1007/s00220-020-03902-1); the cylinder also follows from (5.18). Gluing uses convolution, not the pointwise Wilson-character fusion in (21).

Here is our packet calculation from those formulas. Write \(S_R^{\rm H}\) for (6) with Haar normalization. For integer \(h\ge0\) and \(t\ge0\),
\[
\begin{aligned}
N^{2h}H^h S_R^{\rm H}g
 &=S_R^{\rm H}(e^{-2hx}g),\\
P_{t/N^2}S_R^{\rm H}g
 &=e^{t/N^2}S_R^{\rm H}(e^{-t e^{2x}}g).
\end{aligned}
\tag{30}
\]
Both equalities are exact at finite \(R\), by substituting \(n=Ne^x\) in each coefficient. Consequently their mixed pairing limits are
\[
\int\overline f(x)e^{-2hx}g(x)\,dx,\qquad
\int\overline f(x)e^{-t e^{2x}}g(x)\,dx,
\tag{31}
\]
respectively. At any fixed positive area, the cylinder kills these packets as \(R\to\infty\); any fixed positive number of handles does likewise before multiplication by \(N^{2h}\).

The handle logarithm \(\mathsf L=-\tfrac12\log H\) satisfies
\[
\mathsf L\chi_n=(\log n)\chi_n,\quad
\mathsf L V_a=V_a(\mathsf L+\log a),\quad
(\mathsf L-R)S_R^{\rm H}f=S_R^{\rm H}(xf).
\tag{32}
\]
Thus it is multiplication by the input coordinate in this limit, not its translation generator.

Ordinary cylinder and handle insertions, with these scalings, give local multipliers in the input coordinate. They do not provide the missing nonlocal gamma kernel or its modulation growth. This is a scoped calculation for these standard bordisms and scalings, not an exclusion of all two-dimensional YM observables, boundaries, or defects.

## 10. Verification and the next mathematical task

The [checker](../numerics/check_character_channels.py) and [small record](../numerics/records/character-channels-20260925.json) contain 57 floating controls. They check the weighted root-transfer adjoint against independent angular integration, the norm defect, exact branching, complex mixed limits including nontrivial greatest common divisors, phase orthogonality, positive differences, the two gluing multipliers, electric norm growth, the current approximation, and the divergence on winding-created phases.

The two densities are Haar and the prescribed smooth positive central probability density
\[
\rho_{\rm test}(\theta)=
 \frac{1+0.35\cos\theta+0.2\cos(2\theta)}{0.9}.
\]
They are algebra controls, not numerical samples of the interacting YM state. All 57 checks passed in the recorded environment. The largest absolute discrepancy in the finite exact controls was below \(2.2\times10^{-14}\). The largest final discrepancy in the asymptotic controls was below \(8.6\times10^{-6}\), with an acceptance tolerance \(2\times10^{-5}\).

Resolution matters: the equal-phase non-Haar mixed control required refinement to \(N=8192\), consistent with a possible \(N^{-1}\) error. The Haar current norm errors at \(N=32,128,512,2048\) were approximately \(0.01844,0.002127,0.00013725,0.0000085953\); the latter values show the predicted \(N^{-2}\) behavior. The record preserves these intermediate errors. The tolerance was not enlarged to hide a failed coarse-resolution comparison. These are floating diagnostics, not interval bounds or proofs of the infinite limits. The analytical arguments above supply the claims for the actual smooth positive marginal.

The next problem is now narrower: derive an archimedean response and a finite positive normalization from independently defined YM insertions or relations that remain compatible with the winding-created phase components. The full current (19), its exact weighted drift and the branching law (8) are concrete starting data. A functional calculus chosen solely to reproduce the digamma multiplier would not complete this derivation.

Separately, a successful source must occur in the original physical representation, or a new limiting physical model must be explicitly defined and justified. Equations (16)–(18) show why the present packets do not meet the existing compact occurrence theorem. The prime mixed identity is a useful partial advance; the positive global source and the complete mixed Weil identity remain open.
