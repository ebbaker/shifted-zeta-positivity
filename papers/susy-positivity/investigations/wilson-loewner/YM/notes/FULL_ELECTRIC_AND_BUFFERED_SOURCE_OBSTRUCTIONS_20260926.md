# Full electric point sources and buffered physical preparation

26 September 2026. Drafted for Edward Baker with substantial LLM assistance. Model exposed: GPT-6 (Codex); exact deployed variant and reasoning effort unavailable, not inferred. These are model-assisted proofs with a separate self-audit, not independent specialist verification.

This continuation tests exactly two mechanisms in the original four-dimensional SU(2) slab and its actual state: Sobolev-regularized point sources for the **full** electric wave, and distributional observables prepared through the strict half-slab integral. Both give well-defined positive physical pairings. Neither gives the Weil pairing. The second exclusion does not require a native arithmetic generator. No continuum limit, change of state, or two-dimensional comparison is used.

## 1. Fixed data and the two questions

Keep the spatial $6^3$ torus, times $-2,\ldots,2$, open outer boundaries, Wilson coupling $8/5$, and theta angle zero. There are $L=648$ spatial links and $V=216$ spatial vertices. Thus $M=\mathrm{SU}(2)^L$ has dimension $D=1944$. With the manuscript's notation,

\[
\mathcal H=L^2_{\rm cov}(M,\nu;\operatorname{End}\mathbb C^2),\qquad
d\nu=Z^{-1}\Omega^2dm=w\,dm,\qquad
\Omega=e^{-S_0/2}h,
\]
\[
h(U)=\int e^{-S_+(U,X)}dX,\qquad
E=\sum_{\ell,j}D_{\ell,j}^{*\nu}D_{\ell,j}\ge0.
\tag{1}
\]

The fiber norm is $\operatorname{tr}(B^*B)/2$. All measures in the finite integrals are normalized Haar. Smoothness, positivity and upper/lower bounds for $h,w$ follow from compactness and the finite Wilson action. The Friedrichs electric operator has compact resolvent and reduces the covariant, scalar and traceless subspaces. Its form, not an individual colored derivative, is gauge invariant.

The target and conventions are exactly those in manuscript Section 1: $T=-\partial_x^2+1/4$, $\mathcal D^0=T C_c^\infty(\mathbb R)$, $\widehat f(\tau)=\int e^{-i\tau x}f(x)dx$, $U_tf(x)=f(x-t)$, and the complete signed prime/digamma form $Q$. In particular

\[
m_+(\tau)=\log(|\tau|/(2\pi))+O(|\tau|^{-2}),\qquad
m_+(0)=-\gamma_E-\pi/2-3\log2-\log\pi.
\tag{2}
\]

The preceding [compact-return note](COMPACT_RETURN_AND_PHYSICAL_TRANSLATION_SOURCES_20260925.md) did **not** establish a compact return for the full many-link electric operator. We do not assume one now. The new tests use spectral growth and physical preparation bounds instead.

## 2. Candidate A: electric waves from a sharp boundary configuration

### 2.1 Physical definition and domain

Choose an irreducible boundary connection $q$ independently of arithmetic. Its gauge stabilizer is the common center. Such connections exist: after a spanning-tree gauge choice, two noncommuting loop holonomies have common centralizer $\{\pm I\}$. The gauge group has dimension $3V=648$, so the principal quotient has local dimension

\[
d=3L-3V=1296.
\tag{3}
\]

Near $q$, scalar and traceless covariant functions are sections of bundles of ranks one and three. The center acts trivially on both. The quotient density is smooth and positive there; write it $a_\nu(y)dy$. The reduced electric operator is locally elliptic with scalar positive quadratic principal symbol $p_2(y,\eta)$. Singular gauge orbits elsewhere do not turn this regular point into a boundary point.

Let $E_0,E_1$ be the restrictions to these two actual orthogonal sectors. Put $\omega_{jn}=\sqrt{1+\lambda_{jn}}$ and choose actual orthonormal electric eigenvectors $e_{jn}$. Choose nonzero fiber vectors $\xi_j$ at $q$, and define

\[
b_{jn}=\langle e_{jn}(q),\xi_j\rangle_{\rm fib},\qquad
J_sf=\sum_{j=0}^1\sum_n
\omega_{jn}^{-s}b_{jn}\widehat f(\epsilon_j\omega_{jn})e_{jn},
\quad \epsilon_0=1,\ \epsilon_1=-1.
\tag{4}
\]

This is the spectral meaning of an electric Sobolev power applied to the gauge-covariant point distribution, followed by wave smearing. Point preparation fixes a boundary configuration; the Sobolev power controls its electric regularity. Both choices have a meaning before a Weil form is mentioned. All real $s$ are allowed. The opposite signs use existing reference-color sectors and add no Hilbert-space copy. They are a candidate two-sided **electric wave** action, not physical time translations or an independently derived arithmetic identification.

Point evaluation is a finite-order distribution. Consequently its spectral mass grows at most polynomially. The rapid decrease of $\widehat f$ makes (4) converge in the actual Hilbert norm for every compact smooth $f$, uniformly on bounded sets with fixed support. It defines a continuous source on all such tests, hence on $\mathcal D^0$. No separate undefined operation on a distribution is needed: (4) is the combined multiplier definition. Finite spectral cutoffs converge strongly, including all mixed pairings.

The exact, state-dependent pairing is

\[
B_s(f,g)=\sum_{j,n}\omega_{jn}^{-2s}|b_{jn}|^2
\overline{\widehat f(\epsilon_j\omega_{jn})}
\widehat g(\epsilon_j\omega_{jn}).
\tag{5}
\]

It is positive without a subtraction. Eigenvalues, eigenfunctions, and their point evaluations are those of (1) in the interacting measure. The corresponding unitary group has generator $\sqrt{1+E_0}\oplus(-\sqrt{1+E_1})$, and $JU_t=e^{-itG}J$. No winding operators, phase projections, or rational-phase identifications are used. Thus there are no discarded winding branches. This construction does not assert an intertwining law with the manuscript's $V_a$.

### 2.2 The relevant local spectral law

At the chosen regular point, the local Weyl law gives

\[
N_j(R):=\sum_{\omega_{jn}\le R}|b_{jn}|^2
=C_jR^d+o(R^d),\qquad C_j>0,
\tag{6}
\]
\[
C_j=\frac{\|\xi_j\|_{\rm fib}^2}{(2\pi)^d a_\nu(q)}
\int_{p_2(q,\eta)<1}d\eta.
\tag{7}
\]

Formula (7) uses a local orthonormal fiber frame and the indicated coordinate density, so its expression is coordinate invariant. In particular the physical weight is retained. Multiplication by $\sqrt w$ conjugates the full weighted electric operator to the Haar Laplacian plus a bounded smooth potential. This leaves its principal symbol unchanged but changes point normalization. Locally on the principal quotient, the same statement is an elliptic bundle operator with scalar leading symbol; the short-time heat kernel has leading coefficient proportional to the fiber identity. Its positive spectral measure yields (6). Equivalently one may apply the fixed-isotypic local Weyl law after removing the ineffective central gauge action. See [Ramacher, Theorem 4.3 and the discussion of principal orbits](https://arxiv.org/abs/1512.02193), and [Hörmander's local spectral-function theorem](https://doi.org/10.1007/BF02391913). We use only the leading local power, not a uniform estimate near singular orbits or an assertion that the whole quotient is smooth.

### 2.3 Direct mismatch with the required logarithm

Take a nonzero real $h_0\in C_c^\infty(\mathbb R)$ and put

\[
h_R(x)=R^{1/2}h_0(Rx),\qquad f_R=R^{-2}Th_R.
\tag{8}
\]

These are globally pole neutral. Their supports shrink, so the diagonal prime sum is exactly zero for large $R$. The Fourier formula

\[
\widehat f_R(\tau)=R^{-5/2}(\tau^2+1/4)\widehat h_0(\tau/R)
\tag{9}
\]

and (2), splitting $|\tau/R|<R^{-1}$ from its complement, rederive

\[
Q[f_R]=\|h_0''\|_2^2\log R+
\frac1{2\pi}\int u^4\log(|u|/(2\pi))|\widehat h_0(u)|^2du+o(1).
\tag{10}
\]

The $u^4\log|u|$ term is integrable; the low-frequency piece and the lower powers of $R^{-1}$ vanish. This checks the earlier shrinking-test claim needed here, including the $2\pi$ contact convention.

Set $p=d-2s$. For $p>0$, (6) and Stieltjes rescaling in (5) give

\[
B_s[f_R]\sim d(C_0+C_1)R^{p-1}
\int_0^\infty u^{p+3}|\widehat h_0(u)|^2du.
\tag{11}
\]

For completeness, the weighted spectral measure has cumulative mass
$\int_1^R\omega^{-2s}dN_j(\omega)\sim dC_jR^p/p$.
After division by $R^p$ its dilation converges to
$dC_ju^{p-1}du$. Uniform polynomial mass bounds and Schwartz decay control the large-$u$ tail. Near zero the leading test factor is $u^4$; the $1/(4R^2)$ correction in $(u^2+1/(4R^2))^2$ tends to zero under the same weighted bounds. This proves (11), not merely an unsmoothed density heuristic.

If $p=0$, weighted mass is $O(\log R)$; splitting at $R$ and summing dyadic high-frequency tails gives $B_s[f_R]=O(R^{-1}\log R)$. If $p<0$, the total weighted mass is finite and $\sup_\tau|\widehat f_R(\tau)|=O(R^{-1/2})$, so $B_s[f_R]=O(R^{-1})$.

It follows that no real $s$ gives (10): for $p>1$ the growth is a strictly positive power, for $p=1$ it tends to a positive constant, and for $p<1$ it tends to zero. Allowing different Sobolev powers in the two orthogonal channels does not help; their positive contributions cannot cancel. Fixed rescaling of electric time changes constants, not these alternatives. Finite powers of arithmetic differentiation are covered by the same change of spectral order.

This is a proved exclusion of the specified full-electric point-source family. It is not a full-electric spectral exclusion. Sources with other singular supports, singular-orbit preparations, nonclassical spectral weights (including logarithmic factors), or nonlocal source relations are not covered. Inserting a logarithmic factor to fit (10) would still need an independent physical prescription and all of the mixed arithmetic identities. The failure already occurs before prime matching.

The pairing (5) fixes its contact distribution by its actual convergent smearing; it has no free subtraction constant. Even adding a fixed $c\langle f,g\rangle_2$ cannot repair (11), since $\|f_R\|_2$ stays bounded. No positivity claim is made for subtracting a divergent contact term. These sources avoid the earlier ordinary-input-norm exclusion whenever their norm diverges on the bounded-$L^2$ family (8); the new obstruction is precisely what tests them beyond that exclusion.

## 3. A many-direction local test for physical preparation

This elementary lemma supplies the second mechanism's obstruction. It uses no zero spectrum, RH, generator covariance, or prime-number asymptotics.

**Lemma (uniform short-interval test spaces).** Fix an open bounded interval $I$ of length less than $\log2$. For every sufficiently large integer $N$ there is an $N$-dimensional space $F_N\subset\mathcal D^0$ supported in $I$, with a parametrization $c\mapsto f_{N,c}$, such that

\[
c_1\|c\|_{\ell^2}\le\|f_{N,c}\|_2\le c_2\|c\|_{\ell^2},\qquad
Q[f_{N,c}]\ge c_3\log N\,\|c\|_{\ell^2}^2,
\tag{12}
\]
\[
\|f_{N,c}\|_{C^m}\le C_mN^{m+1/2}\|c\|_{\ell^2},\qquad
\|f_{N,c}\|_{H^s(\mathbb R)}\le C_sN^s\|c\|_{\ell^2}\quad(s\ge0).
\tag{13}
\]

**Proof.** Place $N$ disjoint translates of $h_R$ from (8) in a fixed compact subinterval of $I$, taking $R=aN$ for a sufficiently large fixed $a$. Let $H_c$ be their linear combination and $f_{N,c}=R^{-2}TH_c$. Disjointness gives

\[
\|f_{N,c}\|_2^2=
\left(\|h_0''\|_2^2+\frac{\|h_0'\|_2^2}{2R^2}
+\frac{\|h_0\|_2^2}{16R^4}\right)\|c\|^2,
\qquad \|H_c\|_2=\|h_0\|_2\|c\|.
\tag{14}
\]

Every prime mixed term within this space vanishes by the length of $I$. If $P_{\le\epsilon R}$ is the usual Fourier cutoff, then

\[
\|P_{\le\epsilon R}f_{N,c}\|_2
\le(\epsilon^2+1/(4R^2))\|H_c\|_2.
\tag{15}
\]

Choose fixed small $\epsilon>0$ so this is at most half of $\|f_{N,c}\|_2$ for large $R$. The multiplier $m_+$ is bounded below globally and is at least $\log R-C_\epsilon$ on the complementary Fourier region. At least three quarters of the squared norm is in that region. This proves (12). Derivative scaling and disjoint support prove the integer Sobolev and $C^m$ estimates; Sobolev interpolation proves (13) for real $s$. All constants are independent of $c,N$. In particular, cancellation between the different translates was explicitly controlled in (15). $\square$

## 4. Candidate B: distributional strict-half-slab observables

### 4.1 Independently defined source relation and reflected pairing

Keep the reflection plane fixed. Let $X=X_+$ be precisely the strict half-slab variables integrated in (1), and let $\mathcal A f$ be a matrix-valued covariant distribution in those variables, with **no dependence on the central spatial links $U$**. On every compact arithmetic support interval assume

\[
\mathcal A:\mathcal D^0(I)\longrightarrow H^{-s}(X)
\quad\hbox{is continuous and linear for some finite }s=s_I.
\tag{16}
\]

The Sobolev space uses any fixed smooth product metric on the finite compact link manifold $X$. This is the ordinary finite-order distribution condition, not ordinary $L^1$ or $L^2$ boundedness in the arithmetic input. In particular a jointly distributional observable kernel on $I\times X$ has (16): its local finite-order estimate, followed by Sobolev embedding for its $X$ test function, gives $\|\mathcal Af\|_{H^{-s}}\le C_I\|f\|_{C^m}$ for a finite $m$. Gauge covariance may be imposed by averaging. Examples include observables at positive lattice time, parallel transported to the reference color if required, together with finite-order insertions and distributional arithmetic smearings. The scope excludes explicit central-link source dependence.

The physical boundary descent fixes the source; it is not a fit to $Q$:

\[
I_f(U)=\langle\mathcal Af,e^{-S_+(U,\cdot)}\rangle_X,\qquad
Jf(U)=K_\nu\mathcal Af(U):=h(U)^{-1}I_f(U).
\tag{17}
\]

For smooth insertions this is exactly the half-slab integral divided by the prepared boundary amplitude. Distributional pairing extends it because its kernel is smooth. Its actual reflected mixed pairing is

\[
B_{\mathcal A}(f,g)=\frac1Z\int_M e^{-S_0(U)}
\frac12\operatorname{tr}\big(I_f(U)^*I_g(U)\big)dm(U).
\tag{18}
\]

This depends on the full interacting action and on the specified observable relation $\mathcal A$. There is no arithmetic generator assumption, no marginal compensation, and no arithmetic measure definition. Positivity is the norm square (18). Smooth gauge-compatible regularization of $\mathcal Af$ converges in $H^{-s}(X)$ and, by (19) below, strongly in the physical representation; (18) is the resulting positive completed pairing. Neither a divergent subtraction nor a retained norm on weakly vanishing packets is involved.

### 4.2 Smoothing is a proved consequence of the finite physical integral

For every finite $s,r\ge0$,

\[
K_\nu:H^{-s}(X)\longrightarrow\mathcal K_r
=\operatorname{Dom}(1+E)^{r/2}
\quad\hbox{is bounded}.
\tag{19}
\]

Indeed all $U$ derivatives of $e^{-S_+(U,X)}/h(U)$ are smooth in $X$, with uniformly bounded $H^s(X)$ norms on compact $M$. Distributional duality bounds all output derivatives by $\|\mathcal Af\|_{H^{-s}}$. Elliptic Sobolev equivalence transfers these bounds to $\mathcal K_r$. Crucially the same finite arithmetic order $m$ from (16) bounds every output order, although the constants depend on $r$:

\[
\|Jf\|_{\mathcal K_r}\le C_{I,r}\|f\|_{C^m}
\quad\hbox{for all }r>0.
\tag{20}
\]

This is stronger than merely requiring each individual source vector to be smooth, or allowing a different input order $m_r$ for every output order. It follows here from the independently specified half-slab source relation.

### 4.3 Rank and regularity obstruction

An elementary conservative count suffices:

\[
\operatorname{rank}\mathbf1_{[0,L_0]}(E)\le C(1+L_0)^{D/2},\qquad D=1944.
\tag{21}
\]

To check it without a smooth-global-quotient assumption, compare the weighted Rayleigh quotient with the Haar one using the positive upper/lower bounds on $w$. On one link, eigenvalues are $n^2-1$ with multiplicity $n^2$, $n\ge1$. The product count is bounded by the product of $\sum_{n\le\sqrt{C L_0+1}}n^2$, times the four-dimensional matrix fiber. Restricting to the covariant subspace can only reduce the count. This gives (21). The exponent is deliberately the ambient one, not a claimed optimal physical Weyl exponent.

**Theorem (no fixed smoothing preparation).** No continuous linear source satisfying (20) for a single finite $m$ can have $\langle Jf,Jg\rangle_\nu=Q(f,g)$ on $\mathcal D^0$. Consequently the distributional half-slab source (16)–(17) cannot realize the target.

**Proof.** Use $F_N$ from (12) and choose $L_N\asymp N^{2/D}$ with the rank in (21) less than $N$. There is $\|c_N\|=1$ with $P_{L_N}Jf_{N,c_N}=0$. Exact pairing and (12) would give

\[
\sqrt{c_3\log N}\le\|Jf_{N,c_N}\|
\le (1+L_N)^{-r/2}\|Jf_{N,c_N}\|_{\mathcal K_r}
\le C_rN^{m+1/2-r/D}.
\tag{22}
\]

Choose $r>D(m+1/2)$. The right side tends to zero, a contradiction. The selected $c_N$ may depend on $J$; all estimates are uniform over that selection. $\square$

The same proof excludes a fixed electric heat preparation $J=e^{-\beta E}\mathcal A$ for $\beta>0$ and any continuous Hilbert-valued input distribution $\mathcal A$. It has the independent meaning of fixed electric diffusion, not physical Euclidean time identification. The sharper bound is $C N^{m+1/2}\exp(-c\beta N^{2/D})$. This is one instance of the same smoothing mechanism, not a third source proposal.

No winding module is used in this proof. Any finite winding operations on strict-half variables that preserve (16) are included, with their full resulting observables. A winding or source relation explicitly involving central links lies outside (17); none of its phases has been removed by the argument.

### 4.4 Consequence for compact-source occurrence

For any exact source whose vectors lie in $\mathcal K_r$, the rank argument also gives the necessary preparation cost

\[
\sup_{\|c\|=1}\|Jf_{N,c}\|_{\mathcal K_r}
\ge c_rN^{r/D}\sqrt{\log N}.
\tag{23}
\]

Thus a bound $\|Jf\|_{\mathcal K_r}\le C\|f\|_{H^s(\mathbb R)}$ on one short interval requires $s>r/D$; the logarithm excludes the critical equality too. A $C^m$ input bound requires $m+1/2>r/D$ by this estimate. These are necessary conditions, not sufficient preparation laws. The original compact-occurrence theorem uses one fixed $r$ and allows an appropriate finite test seminorm; it is not invalidated. However one cannot verify its finite feasibility by a common finite-order strict-half insertion passed through the smoothing kernel (17). Such feasibility would contradict (22).

## 5. Established scope and the remaining opening

The strongest new result is the generator-free exclusion of all sources obtained by the actual strict-half-slab integral from finite-order distributional observable families independent of central spatial links. Its assumptions are finite compact link geometry, smooth strictly positive finite-slab state, the source relation (16)–(17), and exact Weil pairing. It uses no continuum assumption, mass gap, RH, or arithmetic spectrum. Candidate A independently rules out regular-point electric waves with arbitrary fixed Sobolev power, using the local Weyl law. Both are genuine positive source constructions with the wrong pairing, not a negative Gram-matrix search.

What remains includes central-slice-dependent distributional sources outside the point/Sobolev class, nonclassical full-electric source weights with a physical prescription, and preparation limits whose smoothing or finite-order bounds lose uniformity while their vectors converge strongly. For continuum proposals, finite-lattice smoothing constants, link dimension, and preparation norms need not be uniform; this note does not pass its exclusion to that limit. OS positivity, existence and a mass gap do not by themselves supply the missing arithmetic identity or those ultraviolet estimates. A new construction must still recover the complete mixed pairing, all prime shifts and the fixed archimedean contact, in the actual positive representation.

No earlier proved identity is retracted. The new qualification is sharper than the prior ordinary-input-norm obstruction: distributional finite-lattice sources remain possible in general, but a common finite-order source family passed through the specified fixed smoothing readout is excluded. The full many-link electric operator itself is still not excluded as an arithmetic action for every possible seed. The numerical tail cleanup from 25 September is unchanged; no zero-list data or numerical envelope enters either proof.

See the [self-audit](../reviews/FULL_ELECTRIC_AND_BUFFERED_SOURCE_AUDIT_20260926.md) and the maintained manuscript's new section on full electric sources and physical preparation.
