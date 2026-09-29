# CCM, resistance forms, and changing fractals

Date: 26 September 2026.

Model: GPT-6 (Codex). Exact model variant and reasoning-effort setting are not exposed in this session.

Status: initial research round, with proved model identities, a conditional CCM realization criterion, and explicit obstructions. The geometric model below is a control, not an arithmetic realization of CCM. No novelty claim is made. This investigation starts from the original finite mass–stiffness pair, independently of the subsequent inverse-string reconstruction in the neighboring investigation.

## 1. What changes if the fractal changes?

Allowing geometry to depend on support length is a substantive possibility. A fixed self-similar fractal with a bounded pure-power spectral counting law cannot supply the full zeta-zero counting law. A geometry with different behavior at different scales can escape that objection. We give an explicit compact resistance tree with finite mass, logarithmic frequency counting, and a trace-class inverse:
\[
N_*(T)=\frac{T}{\pi}\log T+O(T),\qquad
\operatorname{tr}\mathcal L_*^{-1}=\frac{\pi^2}{12},\qquad
\det(I-z^2\mathcal L_*^{-1})=\prod_{n\ge1}\cos(z/n).
\]
These statements coexist for one fixed operator. Its finite-branch geometries have compatible embeddings and a quantitative inverse-trace tail. The example therefore runs a positive control against an overbroad claim that compact fractal geometry necessarily has the wrong spectral growth. Its actual eigenvalues are elementary products, not zeta zeros.

Changing the apparent geometry as the probing frequency decreases is also meaningful, through coarse graining of a single system. Exact elimination produces a frequency-dependent boundary response; a constant mass–stiffness pair is generally only its low-frequency approximation. Selecting an unrelated fractal separately at each frequency would not specify one self-adjoint operator or its determinant.

The strongest prospective connection to CCM is a resistance form with arithmetic conductances and measure, with harmonic refinements as cutoffs grow. The missing task is to derive that form and its mass metric directly from the two CCM matrices. Positivity of those matrices alone does not do this.

## 2. Starting point and retained hypotheses

Let \(L=2\log\lambda>0\), retain Fourier modes \(|n|\le N\), and let \(W_{+,L,N}\), \(W_{-,L,N}\) be the even and odd Weil blocks, of dimensions \(N+1\) and \(N\). Assume the least eigenvalue \(\varepsilon_{L,N}\) of the full matrix is simple and even, with eigenvector \(g\) satisfying \(\ell(g)\ne0\). Normalize \(\ell(g)=1\). These are conditional inputs, consistent with [CCM, Theorem 5.10, p. 23](https://arxiv.org/pdf/2511.22755v1).

In the parity convention of the [boundary-mechanics note](../../ccm-operator-realizations/notes/CCM_BOUNDARY_MECHANICS_AND_DETERMINANT_CONTROL_20260926.md), put \(d_n=2\pi n/L\) and
\[
(Jq)_0=-\sqrt2\sum_{n=1}^Nq_n/d_n,\qquad (Jq)_n=q_n/d_n.
\]
Thus \(J\) is inverse differentiation into the even functions with zero endpoint value. The data to realize are
\[
\boxed{M_{L,N}=J^\dagger(W_+-\varepsilon I)J,\qquad
K_{L,N}=W_--\varepsilon I},\qquad Kq=\omega^2Mq.                 \tag{2.1}
\]
Both matrices are positive definite under the stated hypotheses: \(K>0\), while \(Jq\) cannot belong to the null line of \(W_+-\varepsilon I\) unless it is zero, because \(\ell Jq=0\) and \(\ell g=1\). Weighted self-adjointness of CCM identifies these frequencies with its finite quotient spectrum. We rechecked the finite derivation and the initial review; we did not infer the hypotheses from old numerical records.

Every proposed geometry built solely from (2.1) is invariant under \(W\mapsto W+cI\), \(\varepsilon\mapsto\varepsilon+c\). It cannot recover the sign of the original ground energy. The positive Laplacian ground state considered below is a different object from that Weil ground state.

### A direct arithmetic connection, before any inverse spectral construction

For a function \(f\) on the logarithmic interval, extend it by zero to \(\mathbb R\), and let \(U_a f(x)=f(x+a)\). The prime-power component in CCM uses delays and weights
\[
a=m\log p,\qquad c_a=(\log p)p^{-m/2},\qquad a\le L.
\]
Their coefficients come from [CCM, (3.16)–(3.18), p. 7](https://arxiv.org/pdf/2511.22755v1). In the symmetrized correlation convention \(q(f,f)(a)=2\operatorname{Re}\langle f,U_af\rangle\), the arithmetic contribution is \(-\sum_a c_a q(f,f)(a)\). Unitarity of translation gives the exact identity
\[
-\sum_a c_a q(f,f)(a)
=\sum_a c_a\|f-U_af\|_2^2-2\Big(\sum_a c_a\Big)\|f\|_2^2.    \tag{2.2}
\]
The first term is a positive jump energy with prescribed prime-power conductances; the second is a scalar energy offset. This explains a concrete possible connection to electrical networks. Equation (2.2) applies to the arithmetic part only. The pole and archimedean terms, the shift \(\varepsilon\), and the mass form \(J^\dagger T_+J\) must still be accounted for. No cancellation or Markov property of the full form is being asserted.

In the ordinary interval metric these are nonlocal jumps. They become edges only after specifying a different geometry. The orbit of translations by \(\log2\) and \(\log3\) is already dense in \(\mathbb R\); their irrational ratio follows from unique prime factorization. Thus a locally finite self-similar graph does not follow just by drawing one edge for each prime. A resistance metric, completion, and compatible finite approximants would need construction.

## 3. Three concrete candidates

| Candidate | Explicit connection to (2.1) | Advantage | Limitation and status |
|---|---|---|---|
| Standard Sierpinski-gasket resistance Laplacian | Graph energy and a vertex/continuum mass give exactly a generalized stiffness–mass eigenproblem. Harmonic extension uses a Schur complement. | Established local energy and exact refinement factor \(5/3\); an excellent control. | Its fixed spectral growth is incompatible with the full zeta-zero count. No arithmetic map has been found. |
| Non-self-similar resistance networks/trees, allowed to vary with \(L\) | Prescribed jump conductances suggest a network energy; a measure supplies the separate mass form. Both must satisfy the Gram identities in §6. | Flexible scale behavior, a resistance formula for the inverse trace, and genuine common refinements when constructed compatibly. | Strongest direction for further work. §5 supplies an explicit analytic control, not the CCM network. |
| Krein–Feller Laplacian with singular mass on an interval | Energy \(\int |u'|^2dx\), mass \(\int |u|^2d\mu\): a differential version of a positive mechanical pencil with a fractal mass distribution. | Established form construction; separates geometry from mass and permits nonuniform scaling. | No reason yet that the arithmetic pair has this local energy. Singular-support domains require harmonic representatives across gaps. Spectral exponent alone is insufficient for logarithmic asymptotics. |

The gasket energy and its counting law are stated in [Teplyaev, p. 21](https://arxiv.org/pdf/math/0505546v2). Resistance forms, their Markov axiom, and harmonic compatibility are established constructions in [Kigami, §§2 and 4](https://www-an.acs.i.kyoto-u.ac.jp/~kigami/ulcg.pdf). The interval form and dependence of spectral growth on the mass measure are treated in [Kesseböhmer–Niemann, §§1–2](https://arxiv.org/pdf/2106.08862v3). Their spectral-dimension convention is the exponent of Laplacian eigenvalue counting; the frequency exponent is twice that number.

### Precisely what the fixed-fractal obstruction says

Suppose a proposed positive Laplacian obeys, for some fixed \(\alpha>0\),
\[
0<cE^\alpha\le N_{\mathcal L}(E)\le CE^\alpha<\infty
\quad\text{for all sufficiently large }E.
\]
Its positive frequencies have count \(N_{\sqrt{\mathcal L}}(T)\asymp T^{2\alpha}\). No fixed exponent can make this asymptotic to \(T\log T/(2\pi)\): exponents below or above one give the wrong power, while exponent one has a bounded ratio to \(T\). Bounded log-periodic modulation does not remove this obstruction. For the standard gasket, \(2\alpha=\log9/\log5\).

The relevant target counts all nontrivial zeta-zero ordinates with multiplicity; the Riemann–von Mangoldt formula does not assume RH. Its leading terms are \(T\log(T/(2\pi))/(2\pi)-T/(2\pi)+O(\log T)\); see [Trudgian, Corollary 1, p. 2](https://arxiv.org/pdf/1208.5846v2). The obstruction concerns an asserted full limiting spectrum. It says nothing against finite approximations, selected boundary-visible spectra, moving geometries, or unbounded slowly varying corrections. In particular, merely having frequency spectral dimension one does **not** exclude \(T\log T\).

## 4. Resistance controls the inverse-frequency trace

Here is a useful precise gain from the resistance formulation. Assume a compact metrizable resistance space \((F,R)\) with a regular resistance form \((\mathcal E,\mathcal F)\), a finite full-support Borel measure \(\mu\), and an anchor \(o\) with \(\mu(\{o\})=0\). Impose a Dirichlet condition at \(o\). Assume the induced grounded form is densely defined and closed on \(H=L^2(F,\mu)\); these domain properties hold for the model in §5 and must be verified in any proposed arithmetic model.

The energy space is \(\mathscr E=\{u\in\mathcal F:u(o)=0\}\), with inner product \(\mathcal E(u,v)\). The positive self-adjoint operator is specified without any formal differential notation:
\[
\begin{split}
\operatorname{Dom}\mathcal L={}&\{u\in\mathscr E:\ \exists f\in H,
\ \mathcal E(u,v)=\langle f,v\rangle_\mu\ \forall v\in\mathscr E\},\\
\mathcal Lu={}&f.
\end{split}                                                        \tag{4.1}
\]
The complex form is obtained by complexifying the real resistance form. Boundary evaluation is meaningful in the resistance metric. The squared frequency ground value has the variational characterization
\[
\lambda_1=\omega_1^2=\inf_{u\ne0}\frac{\mathcal E(u,u)}{\|u\|_\mu^2}.
\]

**Proposition 1.** With these hypotheses,
\[
\boxed{\operatorname{tr}\mathcal L^{-1}=\tau:=\int_F R(x,o)\,d\mu(x)},
\qquad \omega_1^2\ge\tau^{-1},\qquad
|\det(I-z^2\mathcal L^{-1})|\le e^{\tau|z|^2}.                \tag{4.2}
\]
In particular \(\tau\le\mu(F)\operatorname{diam}_R(F)<\infty\).

Proof. The norm squared of evaluation at \(x\) in \(\mathscr E\) is \(R(x,o)\). This is the grounded Green-function identity; compare Kigami, Propositions 4.2–4.3, p. 11. For an energy-orthonormal basis \((e_j)\), Parseval and Tonelli give
\[
\sum_j\|e_j\|_\mu^2=\int_F\sum_j|e_j(x)|^2d\mu(x)=\int_FR(x,o)d\mu(x).
\]
Thus the inclusion \(I:\mathscr E\to H\) is Hilbert–Schmidt. The variational definition gives \(II^*=\mathcal L^{-1}\), hence the trace identity. Also \(\|u\|_\mu^2\le\tau\mathcal E(u,u)\), proving coercivity. The determinant bound follows by multiplying \(|1-z^2/\lambda_j|\le e^{|z|^2/\lambda_j}\). This is a proof under explicit form hypotheses, not an estimate already established for CCM.

With several grounded points, the diagonal is resistance to the grounded set, not automatically the distance to an arbitrarily chosen point. With a positive atom at a grounded vertex, its coordinate must be removed from the \(L^2\) state space. These qualifications prevent a hidden failure of dense definition.

## 5. A compact changing-scale tree: an explicit positive control

Fix \(0<a<1\). Glue the left endpoints of intervals \([0,r_n]\), \(n\ge1\), to a root \(o\), where
\[
r_n=n^{-a},\qquad m_n=n^{-(2-a)},\qquad
\rho_n=m_n/r_n=n^{2a-2}.
\]
Use path length as resistance distance, energy
\[
\mathcal E(u,u)=\sum_n\int_0^{r_n}|u_n'(s)|^2ds,
\qquad \|u\|_\mu^2=\sum_n\rho_n\int_0^{r_n}|u_n(s)|^2ds.     \tag{5.1}
\]
The geometry is compact: all sufficiently short arms fit into any prescribed ball about the root, and only finitely many longer arms remain. Its total mass is \(\sum m_n=\zeta(2-a)<\infty\), although its total resistance length \(\sum r_n\) is infinite. This is a compact infinitely branched resistance tree, not a standard finitely ramified self-similar gasket. The distinction is essential.

Its geometric dimensions also show why a single fractal dimension is not enough. In the resistance metric its Hausdorff dimension is one, since it is a countable union of intervals and a root, whereas its box dimension is \(1/a\). Indeed the number of radius-\(\delta\) balls needed is bounded above by a constant times \(\delta^{-1}\sum_{n\le\delta^{-1/a}}n^{-a}+\delta^{-1/a}\), and hence by \(C\delta^{-1/a}\). The tips of the arms of length at least \(2\delta\) give the matching lower bound. Varying \(a\) therefore changes a precise geometric scaling exponent while preserving the spectrum below.

Before grounding, the form domain consists of continuous functions with common root value, absolutely continuous \(H^1\) restrictions on each arm, and finite energy. Pointwise continuity at the accumulating root follows from
\(|u_n(s)-u(o)|^2\le r_n\mathcal E(u,u)\). Completing in energy modulo constants gives the resistance form; finite-arm piecewise-linear functions, with a common constant on the remaining arms, show regularity. The effective resistance equals path length, since the other dangling arms can be held constant in the variational problem. The Markov contraction decreases each edge energy.

Ground \(u(o)=0\) and impose the natural Neumann condition at each outer tip. Then
\[
(\mathcal L_*u)_n=-\rho_n^{-1}u_n'',\qquad
u_n(0)=0,\quad u_n'(r_n)=0.                                  \tag{5.2}
\]
Precisely, its domain consists of grounded finite-energy \(u\in H\) with \(u_n\in H^2(0,r_n)\), the stated tip conditions, and
\(\sum_n\rho_n^{-1}\int|u_n''|^2<\infty\). There is no Kirchhoff condition at the grounded root. These boundary conditions dynamically decouple the arms. This makes the model solvable and also limits its arithmetic relevance.

The normalized modes are
\[
u_{n,k}(s)=\sqrt{2/m_n}\sin((k+\tfrac12)\pi s/r_n),\quad
\boxed{\omega_{n,k}=\pi n(k+\tfrac12)},\qquad k=0,1,\ldots.   \tag{5.3}
\]
Normalization and eigenvalues follow directly from (5.1)–(5.2), using \(r_nm_n=n^{-2}\). Their direct-sum sine bases are complete. Below a finite frequency only finitely many pairs occur, so the resolvent is compact. The lowest squared frequency is \(\pi^2/4\), simple in this model. It provides no information about simplicity or sign of the CCM Weil ground state.

### Counting and determinant, with proofs

Let \(D(x)=\sum_{n\le x}\lfloor x/n\rfloor\). With \(x=2T/\pi\),
\[
N_*(T)=\#\{(n,k):n(2k+1)\le x\}=D(x)-D(x/2).                \tag{5.4}
\]
The hyperbola identity \(D(x)=2\sum_{j\le\sqrt{x}}\lfloor x/j\rfloor-\lfloor\sqrt{x}\rfloor^2\), together with the harmonic-sum asymptotic, gives \(D(x)=x\log x+(2\gamma-1)x+O(\sqrt x)\). Hence \(N_*(T)=(T/\pi)\log T+O(T)\). The related Dirichlet interval graph and divisor-counting mechanism are established in [Endres–Steiner, §2](https://www.uni-ulm.de/fileadmin/website_uni_ulm/nawi.inst.260/paper/09/tp09-1.pdf). Our mixed-boundary compact weighted version is derived here; no priority is claimed for it.

Independently of counting,
\[
\tau_* =\int R(s,o)d\mu(s)
=\sum_n\rho_n\int_0^{r_n}s\,ds
=\frac12\sum_{n\ge1}n^{-2}=\frac{\pi^2}{12}.                \tag{5.5}
\]
The reciprocal-square sum from (5.3) gives the same result. The classical cosine product on each arm then gives
\[
F_*(z)=\prod_{n\ge1}\cos(z/n),                              \tag{5.6}
\]
locally uniformly, because \(\sum n^{-2}<\infty\). This supplies a fully defined local-energy operator with the desired *order* of counting growth and controlled determinant, without using any zeta zero as input. It neither gives the actual zeta-zero locations nor derives their counting constant arithmetically.

Its spectral zeta function, in the convention \(\zeta_{\mathcal L}(s)=\sum\lambda_j^{-s}\), is
\[
\zeta_{\mathcal L_*}(s)=\pi^{-2s}(2^{2s}-1)\zeta(2s)^2,
\qquad\operatorname{Re}s>\tfrac12.                          \tag{5.7}
\]
Zeros of the continuation of (5.7) are not eigenvalues of \(\mathcal L_*\). Even a single ordinary interval has a spectral zeta function proportional to \(\zeta(2s)\). A Riemann-zeta factor in a fractal spectral zeta function therefore cannot substitute for a Hilbert–Pólya realization.

### Different geometries with increasing support

Retain the first \(B\) arms to obtain \(F^{(B)}\). Extend grounded functions by zero on the other arms. These embeddings preserve both forms exactly; on the full Hilbert direct sum, zero-extend the finite-arm inverse. The inverse difference is positive and
\[
\|\mathcal L_*^{-1}-(\mathcal L_*^{(B)})^{-1}\oplus0\|_1
=\frac12\sum_{n>B}n^{-2}\le\frac1{2B}.                     \tag{5.8}
\]
Thus \(F_*^{(B)}(z)=\prod_{n\le B}\cos(z/n)\) converges locally uniformly to (5.6). Here \(B\) counts arms; it is not the CCM Fourier cutoff \(N\). Each retained arm still has infinitely many modes. Finite-dimensional approximants can use nested piecewise-linear spaces on the retained arms. On an element of length \(h\), their stiffness and consistent mass are
\[
\frac1h\begin{pmatrix}1&-1\\-1&1\end{pmatrix},\qquad
\frac{\rho_nh}{6}\begin{pmatrix}2&1\\1&2\end{pmatrix}.
\]
Root degrees of freedom are removed; the tip condition is natural. Increasing both the arm and mesh cutoffs gives dense form spaces. No identification of these two geometric cutoffs with \((L,N)\) has been established.

One can now legitimately set \(B=B(L)\to\infty\), if an arithmetic construction prescribes that rule. For fixed \(B\), \(N_B(T)=T H_B/\pi+O(B)\), with \(H_B=\sum_{n\le B}1/n\); letting the number of active scales grow gives the logarithm. Fixed-geometry high-frequency asymptotics cannot be interchanged with this limit without estimates. Conversely, all spectra below \(T\) are already present when \(B\ge\lfloor2T/\pi\rfloor\). Fewer arms suffice as the probing window decreases, because this special model has decoupled arms.

Varying \(a\) changes resistance lengths and mass distributions while leaving (5.3) unchanged. This explicitly demonstrates underdetermination of geometry by spectral agreement. Arbitrary choices of \(a(L)\) add no arithmetic explanation. Grounding, scale compatibility, and the physical mass must be specified as well as a named fractal.

## 6. What would constitute a CCM realization?

For each fixed \(L\), suppose a grounded resistance system as in §4 exists, with finite-dimensional subspaces \(V_{L,N}\subset\mathscr E_L\) and bijective linear maps \(\Phi_{L,N}:\mathbb C^N\to V_{L,N}\) such that
\[
\mathcal E_L(\Phi q,\Phi r)=q^\dagger K_{L,N}r,\qquad
\langle\Phi q,\Phi r\rangle_{\mu_L}=q^\dagger M_{L,N}r.       \tag{6.1}
\]
This specifies the necessary map and both metrics; it is an existence requirement, not a map already constructed for CCM. A useful solution would derive \(\Phi\), conductances, and measure from the arithmetic input, such as (2.2), rather than fitting spectral values.

**Proposition 2 (conditional realization and convergence).** If (6.1) holds, the *Galerkin Laplacian* on \(V_{L,N}\) is unitarily equivalent, via \(\Phi\), to \(M_{L,N}^{-1}K_{L,N}\) in the \(M\) inner product. Thus it realizes exactly the finite squared positive CCM spectrum. It need not be the restriction of the full Laplacian to an invariant subspace.

For a common fixed-\(L\) energy space, let \(C_L=I_L^*I_L\), and let \(P_{L,N}\) be energy-orthogonal projection onto \(V_{L,N}\). The nonzero eigenvalues of \(C_{L,N}=P_{L,N}C_LP_{L,N}\) are \(\omega_j^{-2}\). If these subspaces are nested and energy dense, then
\[
\begin{split}
\tau_{L,N}^{\rm fin}&=\operatorname{tr}(K_{L,N}^{-1}M_{L,N})
=\operatorname{tr}C_{L,N}\uparrow\tau_L=\int R_L(x,o_L)d\mu_L(x),\\
\|C_L-C_{L,N}\|_1&\le2\sqrt{\tau_L}\sqrt{\tau_L-\tau_{L,N}^{\rm fin}}\longrightarrow0.  \tag{6.2}
\end{split}
\]
Consequently the finite normalized determinants converge locally uniformly to \(\det(I-z^2C_L)\).

Proof. Restrict the two forms to \(V\) to get precisely the pencil in (2.1). In energy coordinates the mass form represents \(C_{L,N}\), hence its eigenvalues are the reciprocal generalized eigenvalues. Nested orthogonal projections increase the trace and exhaust it. Writing \(J_N=I_LP_{L,N}\),
\(C_L-C_{L,N}=(I_L-J_N)^*I_L+J_N^*(I_L-J_N)\).
The Schatten inequality \(\|A^*B\|_1\le\|A\|_2\|B\|_2\) gives (6.2), since \(\|I_L-J_N\|_2^2=\tau_L-\operatorname{tr}C_{L,N}\). Continuity of the Fredholm determinant in trace norm completes the proof.

This conditional proposition is genuinely restrictive. A generic positive matrix is not a Markov energy in a prescribed vertex basis. A graph Laplacian there needs nonpositive off-diagonal entries and the appropriate row sums or grounding terms; the mass must also have a measure interpretation. Changing basis to match eigenvalues alone proves neither these properties nor compatibility at another cutoff. The monotonicity in (6.2) is itself a necessary test of a proposed nested exact realization, not a property assumed for the actual CCM cutoffs.

The signed finite CCM operator can be recovered by the usual chiral doubling of the positive square root. This is an operator equivalence only. The abstract doubled square root does not automatically give a local geometric Dirac operator, and we have not transported the spectral-triple algebra or verified its commutators. None of the three candidates has yet realized the full CCM spectral triple.

## 7. Lower frequencies: exact reduction versus a changing operator

For a fine graph separate retained boundary and interior variables. Assume, for this lemma, block-diagonal mass and positive interior stiffness:
\[
K=\begin{pmatrix}A&B\\B^\dagger&C\end{pmatrix},\quad
M=\begin{pmatrix}M_b&0\\0&M_i\end{pmatrix},\quad C>0,\ M_b>0,\ M_i\ge0.
\]
Static harmonic extension is \(Hq=(q,-C^{-1}B^\dagger q)\), giving
\[
K_{\rm eff}=A-BC^{-1}B^\dagger,\qquad
M_{\rm eff}=H^\dagger MH=M_b+BC^{-1}M_iC^{-1}B^\dagger.       \tag{7.1}
\]
This energy compatibility is the Schur-complement rule in Kigami, Proposition 2.6. At spectral parameter \(t=\omega^2\), the exact boundary pencil is instead
\[
S(t)=A-tM_b-B(C-tM_i)^{-1}B^\dagger.                        \tag{7.2}
\]
Let \(D=C^{-1/2}M_iC^{-1/2}\), \(\eta=\|D\|\). Whenever \(|t|\eta<1\), a convergent Neumann expansion proves
\[
S(t)=K_{\rm eff}-tM_{\rm eff}
-t^2BC^{-1/2}D^2(I-tD)^{-1}C^{-1/2}B^\dagger.              \tag{7.3}
\]
The remainder has norm at most
\[
\frac{|t|^2\|BC^{-1/2}\|^2\eta^2}{1-|t|\eta}.             \tag{7.4}
\]
Thus a coarser mass–stiffness model is controlled to order \(\omega^4\) below the first interior resonance. For coupled massive interiors it is generally not exact. If \(M_i=0\), all higher terms vanish; this is the required positive control. For non-block-diagonal mass one must retain its cross blocks as well; (7.2) cannot be reused unchanged.

There is also a determinant identity, where the inverse exists:
\[
\det(K-tM)=\det(C-tM_i)\det S(t).                           \tag{7.5}
\]
Keeping only the boundary response and forgetting the eliminated interior factor loses spectral data. This is particularly relevant if a new effective fractal is chosen for each frequency. A family of responses can represent one operator when derived by (7.2); arbitrary frequency-dependent geometry cannot be assumed to do so.

In diffusion terminology, if a model has walk exponent \(d_w\), the heuristic scale probed at Laplacian energy \(\omega^2\) is \(r\sim\omega^{-2/d_w}\). This scaling interpretation requires its own heat-kernel assumptions and is not used in any proof here. It motivates coarse graining at lower frequencies, rather than changing a fractal label without a map between state spaces.

## 8. Both CCM cutoffs and the untouched tail

Support growth \(L\) introduces additional delays \(m\log p\le L\), changes all free spacings, and changes the arithmetic forms. Fourier refinement \(N\) at fixed \(L\) is a different operation. Even if (6.1) were proved for every finite pair, convergence requires the common-space conditions and trace control in (6.2), followed by control of the \(L\)-dependent geometry. A bound on \(\tau_L\) gives normal-family control of the geometric determinants, but does not identify their limit with Xi. Different \(F_L\) must be compared using actual embeddings/resolvents; uniformly bounded traces alone do not imply convergence. For the full CCM determinant the free tail below must also be controlled.

In particular, the shifting ground energy already obstructs simply declaring Fourier-coordinate inclusions to preserve energy. For the standard odd-coordinate inclusion \(E:\mathbb C^N\to\mathbb C^{N'}\) at fixed \(L\), compression of the same Weil form and the explicit \(J\) give
\[
E^\dagger K_{L,N'}E=K_{L,N}+(\varepsilon_{L,N}-\varepsilon_{L,N'})I,
\]
\[
E^\dagger M_{L,N'}E=M_{L,N}+(\varepsilon_{L,N}-\varepsilon_{L,N'})J_N^\dagger J_N.
\]
Thus a compatible harmonic map generally has to differ from this inclusion. These are exact finite compression identities, not a proof that every geometric embedding fails. When the least eigenvalue stabilizes, the defects vanish; a diagonal Weil-form surrogate with a fixed isolated lowest even entry and larger added entries is a control for that possibility.

If a sequence of lowest frequencies genuinely tends to zero, its inverse trace is at least \(\omega_1^{-2}\) and therefore diverges. Consequently the proposed uniform trace criterion in the original frequency normalization cannot hold along that sequence. Rescaling frequencies changes the comparison target. Conversely, divergence of the trace alone need not imply that the lowest frequency tends to zero.

The finite geometric determinant would account only for the modified block. The full normalized CCM function is
\[
F_{L,N}(z)=\det(I-z^2K_{L,N}^{-1}M_{L,N})\,
U_{L,N}(z),\quad
U_{L,N}(z)=\prod_{n>N}\left(1-\frac{L^2z^2}{4\pi^2n^2}\right). \tag{8.1}
\]
Its inverse trace includes \(\frac{L^2}{4\pi^2}\sum_{n>N}n^{-2}\). At fixed \(L\), this tail disappears as \(N\to\infty\). If \(L^2/N\to c<\infty\), it instead converges locally uniformly to \(e^{-cz^2/(4\pi^2)}\): the first logarithmic term has that limit and higher terms are \(O(L^4/N^3)\). Merely moving the first untouched frequency to infinity is insufficient. No fractal reconstruction of the finite pair is entitled to erase this factor.

For fixed finite \((L,N)\), the eventual positive-frequency count of the full CCM operator is the free-circle linear count \(LT/(2\pi)+O(1)\). A different counting law for a joint limit therefore cannot be read off from that fixed-cutoff asymptotic, just as the finite-arm tree's fixed-\(B\) asymptotic does not determine (5.4).

## 9. Reproducible controls and review ledger

The [program](../numerics/check_resistance_models.py) and [compact record](../numerics/records/resistance_models_20260926.json) use no CCM eigenvalues or zeta zeros as inputs. All graph identities use exact rational arithmetic, and the counting controls use integers. Decimal diagnostics were recomputed at 32 and 64 digits: all 11 observables agree at 24 retained significant digits, with maximum absolute difference below \(6.4\times10^{-32}\). That sensitivity check concerns decimal presentation, not certification of an infinite-dimensional claim.

Checks and outcomes:

- Gasket levels 0, 1, 2 have 3, 6, 15 vertices. Renormalized conductances \((5/3)^m\) give exactly zero Schur-complement residual at both refinements.
- With one grounded vertex and unit total discrete mass on the others, the inverse traces are \(2/3\), \(77/150\), \(1196/2625\), all below maximum root resistance \(2/3\). These *varying discrete measures* are not the fixed continuum measure of Proposition 2, so their decreasing traces do not contradict (6.2).
- At the first refinement, uniform vertex masses \(1/6\) give effective mass with diagonal \(17/75\) and off-diagonal \(4/75\). At \(t=1/7\), the largest entry of the nonlinear remainder is exactly \(3001/50936550\ne0\); setting the interior masses to zero makes the remainder exactly zero.
- Parity-diagonal surrogates verify the Fourier-compression identities: a stable ground value gives zero defects, and lowering the even minimum by one gives stiffness defect one and mass defect three for the retained mode with \(d_1=1\). These are controls for the algebra, not computed Weil matrices.
- The divisor formula and direct odd-product enumeration agree for every integer \(1\le x\le500\). At \(x=10^6\), the full star has 7,331,585 modes below \(\pi x/2\), versus 2,371,953 on 64 arms. The ratio to \((x/2)\log x\) is about 1.06136; the proof of the asymptotic is (5.4), not this sample.

The [critical review](../reviews/RESISTANCE_REALIZATION_CRITICAL_REVIEW_20260926.md) checks hidden positivity, domains, circularity, counting conventions, and limits. The following status distinctions remain in force:

| Statement | Status |
|---|---|
| Prime contribution equals jump energy minus scalar offset, (2.2) | Proved algebraically from the finite-support correlation convention. |
| Grounded resistance trace formula and coercive estimate | Proved under the explicitly stated resistance/form hypotheses. |
| Compact weighted tree with logarithmic count, finite inverse trace, compatible arm cutoffs | Explicitly constructed and proved; an analytic control without CCM arithmetic. |
| Exact finite CCM realization by a resistance geometry | Conditional on both Gram identities (6.1); not constructed. |
| Fixed-support determinant convergence from a nested geometric realization | Conditional theorem, not established for the actual CCM cutoff family. |
| Simple-even Weil ground state, its original sign, Xi identification, full spectral triple | Unresolved here. |

## 10. One concrete next investigation

At fixed \(L=\log13\), use the prescribed prime-power jump terms (2.2) as the starting edge data and retain the archimedean and pole terms separately. Test whether the *full* two forms admit a single vertex interpretation with positive conductances, a positive mass measure, and harmonic maps between the \(N=4,8,16\) cutoffs. Require both Gram identities and the composition of the proposed maps; use (6.2)'s trace monotonicity as an early necessary diagnostic. If the proposed natural identification fails, record the first signed-energy, mass, or compatibility obstruction rather than repairing it by fitting eigenvalues.

This is a test of a specific arithmetic construction, not an unrestricted search over all isospectral fractals. Only after it survives should one ask for uniform resistance–mass bounds as \(L\) increases. The scale-dependent tree proves that this direction is analytically possible; it does not provide the missing arithmetic bridge.

## Sources and verification history

Primary sources consulted on 26 September 2026:

1. Connes–Consani–Moscovici, *Zeta Spectral Triples*, [arXiv:2511.22755v1](https://arxiv.org/abs/2511.22755v1). Printed PDF pp. 4, 6, 7 and 23 inspected for the correlation normalization, arithmetic signs and coefficients, and conditional theorem; finite mechanism checked against the founding note, first continuation, and initial review.
2. Jun Kigami, *Harmonic Analysis for Resistance Forms*, [author manuscript](https://www-an.acs.i.kyoto-u.ac.jp/~kigami/ulcg.pdf). Printed pp. 5 and 11 inspected for Schur compatibility and Green evaluation; resistance axioms checked in §2. The source uses nonpositive graph generators; this note uses positive stiffness matrices.
3. Alexander Teplyaev, *Spectral zeta functions of fractals and the complex dynamics of polynomials*, [arXiv:math/0505546v2](https://arxiv.org/abs/math/0505546v2). Printed p. 21 inspected for gasket energy and counting bounds. Fixed generator normalization does not affect the counting exponent.
4. Marc Kesseböhmer–Aljoscha Niemann, *Spectral dimensions of Kreĭn–Feller operators and Lq-spectra*, [arXiv:2106.08862v3](https://arxiv.org/abs/2106.08862v3). Printed p. 2 inspected for the form, counting convention, and dimensional bounds; used only for the candidate comparison.
5. Sebastian Endres–Frank Steiner, *A Simple Infinite Quantum Graph*, [author-hosted manuscript](https://www.uni-ulm.de/fileadmin/website_uni_ulm/nawi.inst.260/paper/09/tp09-1.pdf). Printed p. 2 inspected for product frequencies and divisor counting. Its unweighted Dirichlet model differs from the compact weighted mixed-boundary tree used here.
6. Timothy Trudgian, *An improved upper bound for the argument of the Riemann zeta-function on the critical line II*, [arXiv:1208.5846v2](https://arxiv.org/abs/1208.5846v2). Printed p. 2 inspected; only the classical asymptotic with logarithmic error is used.

Third-party PDFs and page renders were kept in temporary storage, outside the repository. Only source code, this research history, and a small JSON record are saved. No earlier notes or numerical records were overwritten.
