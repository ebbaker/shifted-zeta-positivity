# TND-E01 r1: geometric Hamiltonian and complete spectral comparison

5 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance, **gpt-6.1-sol (Codex), actual recorded effort ultra**. Investigation08 chat0002, thread `01a1af0a-351c-78d2-8f3a-b1382a3d2e2f`. **E — execution**, request r1. The [activation record][inputs] freezes the issued request and exact working-tree input hashes; the [sole progress register][progress] owns status.

**Return: complete at the requested comparison scope, with proof-author checks.** The geometric kinetic operator is the spin connection Laplacian plus the fixed curvature term 2. Its continuous radial spectrum and complete angular spectrum differ explicitly from the scalar comparator. The existing response-to-source-to-scalar-field construction is exact, with supplied sampling and conjugation steps. It does not derive a local spinor-field-to-scalar-field map, identify source coordinate with physical position, or generate Newman time through the free Hamiltonian. Those are the specific adaptation choices returned to **TND-B01**. New claims await TND-E03; this note is not that assessment.

## 1. Evidence and conventions

We reuse MC11's accepted [operator derivations, Note05][mc-free], [fixed cylinder contract, Note06][mc-contract], [source/endpoint derivations, Note08][mc-source], [AR-E04 assessment][mc-review] and [manuscript Section 2][mc-main]. Investigation05's [companion source][book] supplies its scalar construction, with the evidence level of its [same-assistant assessment][book-review]. The [author clarification][clarification] fixes the Hamiltonian priority. No pending Note13-only preparation, measurement or normalized-wavefunction claim is needed here; MC11-OBS-E01 retains its separate status.

Use the Laplacian convention Δ with nonpositive spectrum, Hermitian Clifford matrices, and self-adjoint geometric D = −i slash∇ on the unit two-sphere. Its chirality Γ is parallel, Hermitian, Γ²=I and ΓD=−DΓ. Put A=D². Both signs are retained: D has eigenvalues ±n, n≥1, each with multiplicity 2n; P_n is the rank-4n projection for A=n².

The fixed physical cylinder coordinate is v:

\[
 C_v=\mathbb R_v\times S^2,\qquad g_C=dv^2+\tfrac14g_{S^2},\qquad
 \mathcal H_C=L^2(\mathbb R,dv;K),\quad K=L^2(S^2,\Sigma;d\Omega).
\tag{1}
\]

Metric volume is dv dΩ/4. The map ψ↦2ψ identifies the stated product-measure Hilbert space with the metric-volume space, without changing multiplicities. Separately, Investigation05 uses a scalar cylinder C_u with the same product metric and normalized measure dμ=du dΩ/(4π); its metric volume is πdμ. Multiplication by 1/√π maps its normalized scalar L² space isometrically to metric-volume L². Distinguishing these constant normalizations is sufficient; no source-dependent measure is introduced.

The symbols u (source/logarithmic coordinate), β (angular damping), λ (Newman parameter), k (real Fourier label) and τ (operator heat time) retain their different roles. We use R=e^{2u} for the auxiliary Euclidean radius in the scalar construction; the cylinder's sphere radius remains 1/2.

## 2. Product spin connection, curvature and Hamiltonian

In a local unit-sphere orthonormal frame e_a, the cylinder frame is E_0=∂_v and E_a=2e_a. The sphere scale is constant. The product connection therefore has no mixed radial/angular connection terms, and on pulled-back spinors

\[
 \nabla^C_{E_0}=\partial_v,\qquad
 \nabla^C_{E_a}=2\nabla^{S^2}_{e_a},\qquad
 (\nabla^C)^*\nabla^C=-\partial_v^2+4\nabla_{S^2}^*\nabla_{S^2}.
\tag{2}
\]

With the compatible tangential Clifford identification used by MC11,

\[
 \mathcal D_C=-i\Gamma\partial_v+2D,\qquad
 L_0=\mathcal D_C^2=-\partial_v^2+4D^2.
\tag{3}
\]

The cross term vanishes because Γ is v-independent and anticommutes with D. There is no radial 1/R spin-connection term on this product cylinder. Such terms arise in the different Euclidean polar metric and are not removed by silently changing coordinates.

For the geometric curvature identity, we checked Camporesi–Higuchi v1, equations (5.35)–(5.36), against the [primary text](https://arxiv.org/html/gr-qc/9505009). In its anti-Hermitian slash convention, changing to self-adjoint D gives D²=∇*∇+Scal/4. Unit S² has scalar curvature 2; the radius-1/2 sphere and its product cylinder have scalar curvature 8. Thus

\[
 D^2=\nabla_{S^2}^*\nabla_{S^2}+\tfrac12,
 \qquad
 \boxed{L_0=(\nabla^C)^*\nabla^C+2.}
\tag{4}
\]

This agrees directly with (2)–(3), so no extra curvature term is to be added to 4D². The inherited reference record and archived reading copy are indexed in [MC11's canonical catalog][mc-refs]; [the local reference guide][refs] records this additional passage check without duplicating that catalog.

A conventional positive kinetic Hamiltonian, with dimensionless coordinates (1) and physical length unit ℓ₀>0, is

\[
 H_{\rm kin}=\varepsilon L_0,\qquad
 \varepsilon=\frac{\hbar^2}{2m\ell_0^2},\quad m>0.
\tag{5}
\]

Its radial kinetic term is ε(−∂_v²); its angular term is 4εD². Equivalently its spin connection kinetic energy has the fixed geometric contribution 2ε from (4). Equation (5) declares the unit convention for a spinor kinetic theory; it supplies no new interaction or derivation that this must be the system's physical Hamiltonian.

The first-order factor is a different self-adjoint operator with both energy signs. A physical first-order interpretation would require its own energy unit and physical choice. The following operations are already distinguished by functional calculus:

| Object | Action and meaning |
| --- | --- |
| First-order factor | 𝒟_C, with spectrum of both signs; 𝒟_C⁻¹=𝒟_C L₀⁻¹ has a matrix/differential numerator |
| Kinetic unitary evolution | exp(−itH_kin/ℏ)=exp(−iεtL₀/ℏ), norm preserving on all of 𝓗_C and preserving its operator domains |
| Euclidean/proper-time evolution | exp(−τL₀), τ≥0, bounded with norm e^{−4τ}, smoothing for τ>0; τ is dimensionless in (1) |
| Resolvent/Green response | L₀⁻¹=∫₀∞exp(−τL₀)dτ, norm 1/4; a static inverse integrating all positive proper times |

Unitary evolution exp(−it𝒟_C) also exists mathematically. Neither it nor (5) equates physical time, proper time, angular damping or λ. There is no normalized full-cylinder Gibbs state: its positive heat trace density is constant along an infinite radial line.

## 3. Complete spinor and scalar spectral resolutions

Use the unitary full-line transform, componentwise in the angular Hilbert space,

\[
 \widehat\psi(k)=\frac1{\sqrt{2\pi}}\int_{\mathbb R}e^{-ikv}\psi(v)dv,
 \qquad
 \psi(v)=\frac1{\sqrt{2\pi}}\int_{\mathbb R}e^{ikv}\widehat\psi(k)dk.
\tag{6}
\]

The inverse and Plancherel equalities are understood in L², or pointwise on Schwartz functions. Take orthonormal χ⁺_{n,a} with Dχ⁺=nχ⁺ and χ⁻_{n,a}=Γχ⁺_{n,a}, 1≤a≤2n. On each pair,

\[
 D=n\sigma_z,\quad \Gamma=\sigma_x,\quad
 M_n(k)=\begin{pmatrix}2n&k\\k&-2n\end{pmatrix},\quad
 E_n(k)=\sqrt{k^2+4n^2},\quad
 \Pi_\pm(n,k)=\tfrac12\bigl(I\pm M_n(k)/E_n(k)\bigr).
\tag{7}
\]

Thus the full transform is the direct sum over all n,a of these two-component Fourier transforms; applying Π_± resolves 𝒟_C into ±E_n(k), each with 2n angular states at fixed k. L₀ has multiplier E_n(k)² on all 4n states. There is no discretization of k, and both propagation directions k∈ℝ are present.

Reuse exactly the accepted realizations:

\[
 \begin{split}
 \operatorname{Dom}\mathcal D_C
 &=\{\psi:\sum_{n\ge1}\int_{\mathbb R}(k^2+4n^2)
       \|P_n\widehat\psi(k)\|^2dk<\infty\},\\
 \operatorname{Dom}L_0
 &=\{\psi:\sum_{n\ge1}\int_{\mathbb R}(k^2+4n^2)^2
       \|P_n\widehat\psi(k)\|^2dk<\infty\}.
 \end{split}
\tag{8}
\]

The computational core is smooth compactly supported radial sections with finite angular support. More generally Dom L₀^p has weight (k²+4n²)^{2p} for each integer p≥0, by the same multiplication-operator calculus. The form domain has weight k²+4n². No additional boundary condition is selected.

For the scalar comparator on C_v, take spherical harmonics Y_{ℓm}, orthonormal in dΩ/(4π), with −Δ_{S²}Y_{ℓm}=ℓ(ℓ+1)Y_{ℓm}, ℓ≥0 and −ℓ≤m≤ℓ. In particular Y_{00}=1. Then

\[
 L_{\rm sc}=1-\partial_v^2-4\Delta_{S^2},\qquad
 b_\ell=2\ell+1,\qquad
 \widehat{(L_{\rm sc}g)}_{\ell m}(k)
 =(k^2+b_\ell^2)\widehat g_{\ell m}(k).
\tag{9}
\]

This defines a self-adjoint positive multiplication/direct-sum operator with

\[
 \operatorname{Dom}L_{\rm sc}
 =\{g:\sum_{\ell,m}\int_{\mathbb R}(k^2+b_\ell^2)^2
            |\widehat g_{\ell m}(k)|^2dk<\infty\}.
\tag{10}
\]

Here and in (8), membership in the underlying L² space is included. Self-adjointness follows because multiplication by a real measurable function on its maximal weighted domain is self-adjoint: the adjoint domain is forced to have that same weighted L² integrability by testing compact spectral sets. Finite harmonic truncations converge in graph norm. In each remaining channel the graph norm is equivalent to the H²(ℝ) norm; radial cutoffs and smooth approximation give the claimed compact-support core. This proves the scalar realization rather than borrowing a boundary extension. Powers have the analogous weight (k²+b_ℓ²)^{2p}.

| Operator | Channel dispersion | Angular multiplicity | Spectrum |
| --- | --- | --- | --- |
| 𝒟_C | ±√(k²+4n²), n≥1 | 2n per sign at each k | (−∞,−2]∪[2,∞) |
| L₀ | k²+4n², n≥1 | 4n | [4,∞) |
| L_sc | k²+(2ℓ+1)², ℓ≥0 | 2ℓ+1 | [1,∞) |

These radial spectra are absolutely continuous. Indeed each dispersion is a smooth monotone function of k on each open half-line; its threshold preimage has measure zero. Pushforwards of L² spectral densities are therefore absolutely continuous, including their integrable threshold singularities. Countable direct sums preserve this property. In particular plane waves and cosine waves are generalized modes, not normalizable states or a threshold ground state. The odd-square scalar and even-square spinor thresholds, multiplicities and bundles preclude identifying the operators by their displayed channels. No general assertion about every possible nonlocal comparison map is implied.

### Even cosine normalization and the first-order qualification

A unitary identification of the even full-line radial sector with L²(0,∞) is

\[
 (Eh)(v)=h(|v|)/\sqrt2,\qquad
 (\mathcal Ch)(k)=\sqrt{\frac2\pi}\int_0^\infty h(v)\cos(kv)dv,
 \quad k>0,\qquad \mathcal C^{-1}=\mathcal C.
\tag{11}
\]

Thus an even full-line f has a(k)=𝒞(√2 f|_{(0,∞)})(k)=√2 f̂(k), k>0, and

\[
 f(v)=\frac1{\sqrt\pi}\int_0^\infty a(k)\cos(kv)dk,\qquad
 \|f\|_{L^2(\mathbb R)}^2=\int_0^\infty|a(k)|^2dk.
\tag{12}
\]

The same formulas hold in each angular channel. Cosine multiplication by k²+4n² or k²+b_ℓ² gives the even sectors of the squared/scalar operators. **Plain radial evenness does not reduce 𝒟_C**, because ∂_v changes parity. Its full signed resolution is (6)–(7), not a scalar cosine diagonalization. A smooth even H² function has f′(0)=0 as a parity consequence. This introduces no physical wall and does not authorize replacing the retained full-line Green kernel with a Neumann image kernel at a boundary; that would double its boundary diagonal.

## 4. The complete Green response and the externally supplied source scan

For every n≥1, reuse the decaying full-line kernel and its spectral/proper-time normalization:

\[
 g_n(v,w)=\frac{e^{-2n|v-w|}}{4n},\qquad
 g_n(v,v)=\int_{\mathbb R}\frac{dk}{2\pi(k^2+4n^2)}
 =\int_0^\infty\frac{e^{-4n^2\tau}}{\sqrt{4\pi\tau}}d\tau
 =\frac1{4n}.
\tag{13}
\]

Its derivative has right-minus-left jump −1; it decays at ±∞. These conditions fix the inverse without a wall. The operator-valued kernel K₀(v,w)=∑_n g_n(v,w)P_n converges in operator norm, with discarded tail ≤1/[4(N+1)]. Its diagonal W=(4|D|)⁻¹ is bounded, but not trace class. For β>0,

\[
 Q_1(\beta)=\operatorname{Tr}_K(e^{-\beta A}K_0(v_0,v_0))
 =\sum_{n\ge1}4n\frac{e^{-\beta n^2}}{4n}
 =\sum_{n\ge1}e^{-\beta n^2}.
\tag{14}
\]

The fixed probe is v₀=0; translation invariance makes (14) independent of v₀. This trace accounts for every radial momentum through (13), not a k=0 projection. It is an angular trace of a radial diagonal, not an unregularized angular point-diagonal or unrestricted L² evaluation. Integrating that positive constant response over all v would diverge. Every fixed β derivative is justified on β≥ε>0 by ∑n^{2j}e^{−εn²}<∞; no β↓0 or j→∞ uniformity is inferred.

The subsequent steps are supplied source/readout rules:

\[
 \beta=\pi e^{4u}=\pi R^2,\quad R=e^{2u},\quad
 p(u)=e^uQ_1(\pi e^{4u}),\quad
 \Phi(u)=\tfrac18(\partial_u^2-1)p(u),\quad u\ge0,
\tag{15}
\]

\[
 \Phi(u)=e^u\sum_{n\ge1}
 [2(n^2x)^2-3n^2x]e^{-n^2x},\qquad x=\pi e^{4u}.
\tag{16}
\]

Equation (14) alone is independent of physical v; moving the radial probe cannot produce (15). In particular β(u), e^u and the second-order source readout have not been produced by the free Hamiltonian. Equations (15)–(16) are exact conditional on that explicitly prescribed scan.

The complete unit-weight theta identity, including its missing zero mode,

\[
 \Theta(R)=1+2Q_1(\pi R^2),\qquad \Theta(R)=R^{-1}\Theta(1/R),
\tag{17}
\]

extends Φ to a smooth positive even function on ℝ. This reuses the inherited Jacobi transformation and normalization; no new theta theorem is claimed. On u≥0 every summand is positive since n²x≥π>3/2. Odd derivatives at u=0 vanish only after using complete-source reflection; arbitrary filtering or reweighting cannot inherit that endpoint conclusion.

## 5. Scalar field, measures, endpoints and observation

Here u is the coordinate of the scalar auxiliary cylinder. Investigation05 constructs

\[
 A(R)=Q_1(\pi R^2),\quad
 V(R)=1+R^{-1}-\Theta(R)=R^{-1}-2A(R),\quad
 G(u)=\tfrac12e^u V(e^{2u}).
\tag{18}
\]

The scalar V is a generating potential, not a newly inserted interaction in L₀. For u≥0, G(u)=e^{−u}/2−p(u). The complete inversion extends it evenly and smoothly. In particular the two terms in the equivalent |u| expression have cancelling cusps at zero. On R>0,

\[
 \Phi(u)=\tfrac14R^{5/2}\Delta_3\Theta(R),\quad
 -\Delta_XV=\Delta_3\Theta,\quad
 G(u)\sim\tfrac12 e^{-|u|}.
\tag{19}
\]

The right side of the Poisson equation is the regular radial derivative extended smoothly at X=0. In the original expression the distributional central terms of 1/R and Θ cancel; one cannot discard the point source of 1/R separately. V is smooth at X=0 with V(0)=1, and decays like 1/R at infinity. There is no interface at R=1, corresponding to u=0.

The substitutions and measures are, without missing Jacobians,

\[
 X=R\omega=e^{2u}\omega,\quad dX=R^2dR\,d\Omega,
 \quad du=\frac{dR}{2R},\quad
 d\mu=\frac{du\,d\Omega}{4\pi}=\frac{dX}{8\pi R^3},
 \quad g_E=4e^{4u}g_C.
\tag{20}
\]

The scalar square-root conjugation is

\[
 \Delta_X[R^{-1/2}f(u,\omega)]
 =-\tfrac14R^{-5/2}L_{\rm sc}f,\qquad
 L_{\rm sc}=1-\partial_u^2-4\Delta_{S^2}.
\tag{21}
\]

For clarity, (21) is a differential conjugation, not a unitary equivalence between the displayed Euclidean and cylinder L² spaces: the conformal metric and measure factors remain (20). The scalar field G is constant on each sphere, so only ℓ=0 is excited. Write L=1−∂_u² for that channel. Its decaying full-line inverse kernel is e^{−|u−w|}/2. The full scalar comparator's arbitrary-ℓ kernel is e^{−b_ℓ|u−w|}/(2b_ℓ), fixed by the same jump and two-end decay argument.

For real λ define F_λ(u)=e^{λu²}Φ(u). Then the inherited generating family is

\[
 LG_\lambda=8F_\lambda,\qquad
 G_\lambda=8L^{-1}F_\lambda
 =4\int_{\mathbb R}e^{-|u-w|}F_\lambda(w)dw.
\tag{22}
\]

It is the unique solution decaying at both ends: no nonzero homogeneous combination of e^u and e^{−u} has that property. It is positive, even and smooth, with G_λ′(0)=0. No half-line source delta or boundary is substituted. In particular G₀ is exactly (18).

Let

\[
 H_\lambda(z)=\int_0^\infty F_\lambda(u)\cos(zu)du
 =\tfrac12\int_{\mathbb R}F_\lambda(u)e^{izu}du.
\tag{23}
\]

Its normalization remains H₀(z)=ξ((1+iz)/2)/8. The source integral is entire in z, whereas integration by parts in (22) initially gives only

\[
 \boxed{16H_\lambda(z)=(1+z^2)\int_{\mathbb R}G_\lambda(u)e^{izu}du,\quad
 |\operatorname{Im}z|<1.}
\tag{24}
\]

Angular integration in dμ is one, so (24) is also the scalar-cylinder integral in the companion. For real k, (6) gives the useful normalization cross-check

\[
 \widehat F_\lambda(k)=\sqrt{2/\pi}\,H_\lambda(k),\qquad
 \widehat G_\lambda(k)=\frac{8\sqrt{2/\pi}}{1+k^2}H_\lambda(k).
\tag{25}
\]

More precisely, splitting the convolution at w=u shows

\[
 G_\lambda(u)=4e^{-u}\int_{-\infty}^{u}e^wF_\lambda(w)dw
 +4e^u\int_u^\infty e^{-w}F_\lambda(w)dw,
\quad
 G_\lambda(u)\sim c_\lambda e^{-|u|},\quad
 c_\lambda=4\int_{\mathbb R}e^wF_\lambda(w)dw=8H_\lambda(i)>0.
\tag{26}
\]

The analogous derivative bounds below make all Green boundary terms vanish inside the strip. The positive coefficient in (26) means the raw G integral is not absolutely convergent on the boundary lines. Formula (24) can continue H through its source integral; it cannot be evaluated at z=±i by multiplying a divergent G integral by zero. At λ=0, c₀=1/2 and H₀(±i)=1/16, consistent with the inherited normalization.

The supplied construction (13)→(14)→(15)→(18)/(22) is an explicit scalar construction **from spinor spectral-response data**. It does not yet construct a local/covariant scalar field from an individual spinor field or state. No canonical scalar angular constant is a parallel spinor on the sphere: (4) on unit S² excludes a nonzero parallel spinor. Choosing an eigenspinor embedding would be an added encoding, with channel mass²4n² rather than the scalar radial mass²1.

## 6. Complete-source bounds at arbitrary finite order

These estimates extend accepted Note08 majorants to precisely the λ and Fourier derivatives used here. For x=πe^{4u}, u≥0, use its recurrence

\[
 T(P)=(1-4x)P+4xP',\qquad H_0(x)=2x^2-3x,\quad H_{j+1}=T(H_j),
\quad
 \Phi^{(j)}(u)=e^u\sum_{n\ge1}e^{-n^2x}H_j(n^2x).
\tag{27}
\]

Here deg H_j=j+2. For a polynomial P write A_P for the sum of the absolute coefficients, and put

\[
 C_d(N)=\sum_{n>N}n^{2d}e^{-\pi(n^2-1)},\quad
 B_j=A_{H_j}C_{j+2}(0)<\infty.
\tag{28}
\]

The accepted whole-tail estimate gives

\[
 \left|e^u\sum_{n>N}e^{-n^2x}H_j(n^2x)\right|
 \le A_{H_j}C_{j+2}(N)e^u x^{j+2}e^{-x},
 \quad C_d(N)\longrightarrow0.
\tag{29}
\]

It also bounds the sum of absolute values. Reflection supplies |Φ^{(j)}(u)|≤B_j e^{|u|}x^{j+2}e^{−x} on ℝ, now with x=πe^{4|u|}. This extension uses canonical smooth reflection, rather than reflecting a filtered source term by term.

For nonnegative integers r,d, M,b≥0 define

\[
 J_{r,d}(M,b)=\int_{\mathbb R}|u|^r
 e^{Mu^2+(b+1)|u|}x^d e^{-x}du<\infty.
\tag{30}
\]

For example, substitution x=πe^{4|u|} makes it twice

\[
 \frac1{4^{r+1}}\int_\pi^\infty
 [\log(x/\pi)]^r (x/\pi)^{(b+1)/4}
 x^{d-1}\exp\!\left(\frac M{16}\log^2(x/\pi)-x\right)dx.
\tag{31}
\]

The integrable exponential −x dominates the log-squared term and every indicated power. This proves an actual complete-tail payment, not just separate existence of finite derivatives.

For every p,q≥0, |λ|≤M and |Im z|≤b, differentiation of (23) is justified and

\[
 \partial_\lambda^p\partial_z^qH_\lambda(z)
 =\tfrac12\int_{\mathbb R}u^{2p}(iu)^qF_\lambda(u)e^{izu}du,
 \quad
 |\partial_\lambda^p\partial_z^qH_\lambda(z)|
 \le\tfrac12 B_0J_{2p+q,2}(M,b).
\tag{32}
\]

For the complete reflected source tail in (29), replace B₀ by A_{H₀}C₂(N), making the integrated absolute error tend to zero. Compact complex-z convergence and all interchanges claimed here follow. In fact domination on complex λ compacts also yields joint entire dependence, although only compact real λ intervals are required by r1.

For spatial derivatives use

\[
 \partial_u^j e^{\lambda u^2}=e^{\lambda u^2}R_j(\lambda,u),\quad
 R_0=1,\quad R_{j+1}=\partial_uR_j+2\lambda uR_j,
\quad
 R_j=j!\sum_{a=0}^{\lfloor j/2\rfloor}
 \frac{(2\lambda u)^{j-2a}\lambda^a}{a!(j-2a)!}.
\tag{33}
\]

Leibniz with (29) bounds every derivative of u^{2p}F_λ by

\[
 |\partial_u^q(u^{2p}F_\lambda)(u)|
 \le C_{p,q,M}(1+|u|)^{2p+q}e^{Mu^2+|u|}x^{q+2}e^{-x}.
\tag{34}
\]

An explicit finite choice for C is obtained by summing, over a+b+c=q and a≤2p, the multinomial q!/(a!b!c!), the falling factorial (2p)!/(2p−a)!, B_c and the absolute coefficient sum of R_b on |λ|≤M. This records the order dependence; no uniform bound as p or q grows is claimed. For differentiated complete angular tails use (29) in that finite sum on u>0, and use one-sided parity reflection on u<0. Reflected finite angular truncations need not be smooth at zero and may have distributional derivative terms there. Smoothness of the complete source at zero is inherited from the complete theta reflection identity, not inferred from those truncations. The global λ,z tail bound (32) involves no such spatial differentiation.

Thus F_λ and every polynomial insertion belong to Schwartz space, uniformly in its fixed seminorms on compact λ intervals. The inverse multiplier (1+k²)⁻¹ preserves Schwartz space, proving G_λ is Schwartz and belongs to Dom L^j for every finite j. Convolution in (22), including differentiated polynomial sources, also gives uniform weighted exponential decay with any weight e^{a|u|}, 0≤a<1, for all fixed λ/spatial derivatives; one can use e^{a|u|}≤e^{a|u-w|}e^{a|w|} and the integrability of e^{−(1−a)|u-w|}. Explicitly, the weighted supremum of |∂_λ^p∂_u^qG_λ| is at most 8/(1−a) times the weighted supremum of |∂_u^q(u^{2p}F_λ)|. For a compact substrip |Im z|≤b<1 choose b<a<1; the remaining exponential e^{−(a−b)|u|} pays integrability and all boundary limits. These are the strip bounds needed in (24), including its differentiated forms. An individual G_λ is exponentially tailed as in (26), not double-exponentially tailed.

At every endpoint, u^rΦ^{(j)} and u^rF_λ^{(j)} tend to zero at infinity; all odd derivatives of F_λ vanish at 0. On a half-line integration by parts this removes the appropriate odd source endpoints. For G_λ, all odd derivatives vanish at 0, and its exponential tails suffice only within the strip. No endpoint convention for a different source is imported.

## 7. Radial kinetic action versus Newman multiplication and transport

On source Schwartz functions let K_u=−∂_u² and X_u be multiplication by u. With (6), for every finite p,

\[
 \widehat{K_u^pf}(k)=k^{2p}\widehat f(k),\qquad
 \widehat{X_u^{2p}f}(k)=(-\partial_k^2)^p\widehat f(k).
\tag{35}
\]

These are different actions. If a field is explicitly encoded as f(v)χ_n, after supplying u=v, then

\[
 L_0^p[f\chi_n]
 =\sum_{j=0}^p\binom pj(4n^2)^{p-j}K_v^jf\,\chi_n,
\qquad n\ge1.
\tag{36}
\]

Its membership in every finite operator domain follows from f∈Schwartz and fixed n. Arbitrary complete angular superpositions require exactly the weighted summability in (8) and its powers. A fixed-shell encoding does not replace the complete angular response (14).

The actual source family obeys, at every finite p,

\[
 \partial_\lambda^p F_\lambda=X_u^{2p}F_\lambda,\qquad
 \partial_\lambda^pH_\lambda=(-\partial_z^2)^pH_\lambda.
\tag{37}
\]

On the common dense class Schwartz(ℝ), define the transported scalar generator B=L⁻¹X_u²L; it maps this class to itself. Equations (22), (32)–(34) justify every canonical application:

\[
 \partial_\lambda^pG_\lambda
 =8L^{-1}X_u^{2p}F_\lambda
 =B^pG_\lambda=L^{-1}X_u^{2p}LG_\lambda.
\tag{38}
\]

No powers are cancelled outside that invariant class. The product rule gives the useful nonlocal distinction

\[
 \boxed{Bf=u^2f+L^{-1}(4uf'+2f),}\qquad
 \widehat{B^pf}(k)=\frac{(-\partial_k^2)^p[(1+k^2)\widehat f(k)]}{1+k^2}.
\tag{39}
\]

Indeed L(u²f)=u²Lf−4uf′−2f, fixing the signs in (39). The p-fold spectral identity follows by telescoping the adjacent multipliers on Schwartz functions. For an arbitrary scalar channel ℓ the same comparison is available with L replaced by b_ℓ²−∂_u² and 1+k² replaced by b_ℓ²+k². Its inverse norm is b_ℓ⁻². The canonical G_λ excites ℓ=0 only; summing other scalar fields requires their declared weighted domains.

On the strip, define the inherited readout T(G)=(1+z²)∫G(u)e^{izu}du/16. Then

\[
 T(B^pG_\lambda)=(-\partial_z^2)^pH_\lambda.
\tag{40}
\]

Crucially the z derivatives act on the prefactor as well as the G integral. Replacing B by u² on G would omit those terms and is incorrect. In particular e^{δu²}G_λ is not integrable for δ>0, by (26); the exponential multiplier in Newman time acts on F_λ=LG_λ/8.

For comparison, if the source itself is explicitly encoded in shell n, free heat and kinetic unitary evolution multiply its real spectral amplitude respectively by e^{−τ(k²+4n²)} and e^{−iεt(k²+4n²)/ℏ}. They do not apply −∂_k². Ordinary scalar cylinder heat gives e^{−τk²}H on the radial observation, as already recorded in the companion. These Fourier identities are comparisons, not a newly selected physical flow.

Positive Newman increments act on the canonical sources for all finite real λ by the preceding double-exponential bounds. They do not define a bounded multiplier e^{δX_u²} on all L²(ℝ) for δ>0: unit vectors supported in [R,R+1] have image norm at least e^{δR²}. They also do not give a norm-preserving evolution on canonical F_λ, since d||F_λ||²/dλ=2∫u²|F_λ|²du>0. No self-adjointness of B in ordinary scalar L², global bounded positive-λ semigroup there, or global unitary Hamiltonian realization is asserted. This is a scoped comparison of the fixed operations, not an obstruction to controllers, enlarged systems or other physical constructions.

## 8. Inherited, newly derived and unresolved statements

| Statement | Evidence status in this return | Scope or remaining question |
| --- | --- | --- |
| Spinor cylinder, domains, Green diagonal, multiplicity cancellation | Inherited MC11 accepted operator/source results | Complete v∈ℝ, n≥1, both signs; angular trace only |
| Canonical source recurrence, tails and reflection | Inherited MC11 Note08 with AR-E04 assessment | Every finite order, constants depending on that order; full unit-weight source |
| Scalar V, G, conjugation, measure and source-defined Newman flow | Inherited companion identities with same-assistant checks | Exact canonical scalar family; not specialist acceptance |
| Product connection and curvature/unit dictionary | Derived here using inherited Dirac realization and checked primary curvature formula | L₀=∇*∇+2; conventional positive kinetic Hamiltonian εL₀ |
| Signed Dirac blocks, cosine normalization, scalar self-adjoint resolution | Derived here, proof-author and read-only same-model supporting checks | Complete continuous k; arbitrary n and ℓ; parity does not reduce first-order 𝒟_C |
| Compact-λ arbitrary finite derivative/complete-tail bounds; transported powers | Derived here from accepted source majorants | Equations (30)–(40); no order-uniform growth estimate or collision bound |
| Response data to scalar field | Explicit supplied construction, traced here | Contains external β(u), source readout and scalar inverse; not an intrinsic field intertwiner |
| Physical v=u, source/state preparation and physical meaning of λ | Unresolved; TND-B01 | Must specify the field, source/readout map and actual evolution; spectral relabeling alone is insufficient |
| Direct Newman realization versus useful auxiliary evolution | Not selected here; TND-B01 | At most the two plan avenues; a new interaction or physical law is conceptual work |

Classification under [avoid/01][a01]: **geometric/spectral representation and domain comparison**, not an RH-equivalent criterion, collision estimate or all-height gain. The [result index][results] and [patterns index][avoid] govern reuse, especially [coordinate re-realization][a03] and [scoped exclusions][a07]. No investigation closes and no manuscript milestone is declared; a new result-summary entry would await its required assessment.

The [collision-control screen][controls] remains essential. The geometry and generic Fourier/Green identities apply independently of theta. Positive weighted-square controls can retain inserted weighted angular responses and positive half-line sources, but fail the complete unit weights/full canonical reflection. Euler-factor controls retain smooth positive even source constructions and generic scalar Green/Fourier transport, but fail the unchanged integer-square arithmetic source. Reflected super-Gaussian and smooth shape/positive-primitive controls retain their applicable positivity/reflection/Green constructions but fail the exact canonical arithmetic expansion. Atomic controls admit Fourier observations, but not the smooth source-domain hypotheses used in (27)–(34). None is claimed to violate the generic representation identities or an unproved signed estimate. These premises identify which construction applies; they do not exclude a collision. See [avoid/02][a02].

## 9. Proof-author checks and continuation

One derivation pass and one local normalization/domain check were used. Two read-only Sol supporting agents checked, respectively, the geometry/spectral resolution and scalar source/transport dictionary; root alone wrote repository artifacts. They share the root model and imported premises. This is proof-author/same-model support, not TND-E03, independent specialist review, or completion of MC11-OBS-E01.

Checks retained in the final formulas: curvature 8/4=2 agrees with the unit-sphere connection split; the ±2n Dirac pair squares to k²+4n²; the scalar identity 1+4ℓ(ℓ+1)=(2ℓ+1)² holds at arbitrary ℓ; cosine Plancherel carries the √2 full/half-line conversion; the full-line jump gives 1/(4n) and no Neumann doubling; the source map gives H₀(±i)=1/16 and G₀ tail coefficient 1/2; (39) retains the product-rule signs and readout prefactor; (29)–(34) pay full angular/source tails at every finite order. No numerical acquisition, finite-mode fit or low-order determinant campaign was performed.

**Next: [B] TND-B01 — Astra.** Consume this proof-author return and compare the direct radial-spectral Newman avenue with one Hamiltonian-motivated auxiliary flow. The precise question is what physical field and source/readout map connect the fixed spinor cylinder to F_λ or G_λ, and what evolution law then produces the claimed observation. Freeze a single bounded E02 contract only when its generator, field space, domains, supplied theta inputs, parameter range, observation and completion test are fixed. A model switch is context transfer, not evidence upgrading. The [continuation/model-change note][continuation] gives routing and a pasteable prompt. No later task is activated by this return.

[inputs]: ../research-progress/handoffs/01_TND_E01_R1_INPUT_VERSIONS_20261105.json
[progress]: ../research-progress/01_THETA_OBSERVABLES_AND_NEWMAN_DYNAMICS_RESEARCH_PROGRESS_20261105.md
[continuation]: ../research-progress/handoffs/01_TND_E01_R1_RETURN_AND_MODEL_CONTINUATION_20261105.md
[mc-free]: ../../07_positive_theta_primitives/01_jensen/01_mellin_curvature/11_energy_filtered_theta_overlaps/notes/05_MC11_AR_E01_R1_ALL_INDEX_OPERATOR_AND_GREEN_DERIVATIONS_20261105.md
[mc-contract]: ../../07_positive_theta_primitives/01_jensen/01_mellin_curvature/11_energy_filtered_theta_overlaps/notes/06_MC11_BR01_R1_FROZEN_CYLINDER_MODEL_AND_ANALYTIC_CONTRACT_20261105.md
[mc-source]: ../../07_positive_theta_primitives/01_jensen/01_mellin_curvature/11_energy_filtered_theta_overlaps/notes/08_MC11_AR_E03_R1_SOURCE_MEMBERSHIP_AND_ENDPOINT_PAIRINGS_20261105.md
[mc-review]: ../../07_positive_theta_primitives/01_jensen/01_mellin_curvature/11_energy_filtered_theta_overlaps/reviews/05_MC11_AR_E04_R1_MODEL_SOURCE_AND_SCOPED_TRANSFER_ASSESSMENT_20261105.md
[mc-main]: ../../07_positive_theta_primitives/01_jensen/01_mellin_curvature/11_energy_filtered_theta_overlaps/manuscript/main.tex
[mc-refs]: ../../07_positive_theta_primitives/01_jensen/01_mellin_curvature/11_energy_filtered_theta_overlaps/references/README.md
[book]: ../../05_radial_theta_collision_geometry/book/main.tex
[book-review]: ../../05_radial_theta_collision_geometry/reviews/21_BOOK_REWRITE_ASSESSMENT_20261028.md
[clarification]: ../brainstorm/notes/02_DIRAC_CYLINDER_HAMILTONIAN_PRIORITY_20261105.md
[refs]: ../references/README.md
[results]: ../../../../result-summaries/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../avoid/README.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a02]: ../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a03]: ../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
