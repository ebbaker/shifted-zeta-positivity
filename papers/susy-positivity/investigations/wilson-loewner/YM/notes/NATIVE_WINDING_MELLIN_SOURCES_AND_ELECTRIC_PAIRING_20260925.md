# Native winding sources: an exact YM mixed pairing and its obstruction

25 September 2026, America/New_York.

Prepared for Edward Baker with substantial LLM assistance.

Model: GPT-6 (Codex). The deployed variant and reasoning effort are not exposed; neither is inferred.

Status: research deductions with explicit proofs and algebra controls; not independently reviewed. No arithmetic realization or RH proof is claimed.

## 1. Result and scope

This continuation constructs one global source law from the actual finite YM boundary state, repeated windings of one fixed Wilson holonomy, and the state's weighted electric Dirichlet operator. It derives the full mixed pairing, including the interacting weight. It then proves that this law cannot equal the Weil form: the source is locally bounded in the ordinary input \(L^2\) norm, whereas the target has logarithmic growth on fixed-support high-frequency probes.

The law admits an electric insertion which is not defined as a Hilbert vector before arithmetic smearing. Thus the calculation tests a generalized-source candidate beyond ordinary smearing of bounded loops. Its rejection follows from a new bound on the smeared insertion, not an assumption that all sources have bounded pointwise densities.

There is also a genuine, but limited, arithmetic structure. Winding operations give an operator Euler product and its prime-power logarithmic derivative on a continuous-function algebra. A twisted Poisson identity reduces to the completed zeta function at trivial holonomy. Neither identity supplies the YM inner product: the winding maps are unbounded in that Hilbert norm, and trivial-holonomy evaluation is not the state. These distinctions can be proved in the same fixed model.

The result is confined to the source law below. It does not exclude all YM insertions, all nonlinear loop families, an appropriately defined continuum source law, or the nonconstructive existence program. A separately specified native arithmetic translation generator remains optional. The separate causal shifted-transfer objective is unchanged.

The Weil form \(Q\) and its normalization are those in the [project outline](../PROJECT_OUTLINE.md), §2; its necessary high-frequency and off-diagonal behavior are stated explicitly below.

## 2. Fixed model, observables, and exact one-loop marginal

Fix pure \(SU(2)\) Wilson theory at theta zero on the spatial \(6^3\) torus and physical-time slices \(-2,-1,0,1,2\), with open time boundaries and coupling \(\beta=8/5\). This is the regulator already used in the [interacting experiment](FIRST_INTERACTING_SLAB_TEST_AND_CONTINUATION_20260924.md). It is fixed independently of arithmetic input support. No Monte Carlo approximation to its state is used here.

On the central spatial link manifold \(M\), use the actual boundary measure
\[
d\nu(U)=Z^{-1}\Omega(U)^2\,dm(U),\qquad
\Omega(U)=e^{-S_0(U)/2}\int e^{-S_+(U,X_+)}\,dX_+.
\tag{1}
\]
It is smooth, strictly positive, and gauge invariant. The reflected boundary Hilbert space is
\[
\mathcal H=L^2_{\mathrm{cov}}
 (M,\nu;\operatorname{End}\mathbb C^2),\qquad
\langle A,B\rangle=\int\tfrac12\operatorname{tr}(A^\dagger B)\,d\nu.
\tag{2}
\]
This retains the existing reference-color endomorphism sector, without adding dynamical matter. The [finite-slab note](FINITE_SLAB_REFLECTION_AND_DISCRETE_HIERARCHY_20260924.md) derives the reflected-pairing dictionary.

Let \(C\) be the positively oriented elementary plaquette in spatial directions 1 and 2, based at the origin of slice zero. Write \(P=P_C(U)\). Its four underlying links are distinct, and its matrix powers \(P^n\), \(n\in\mathbb Z\), are the same contour traversed repeatedly, with inverse orientation for negative \(n\).

**Marginal lemma.** There is a smooth strictly positive central density \(\rho\) on \(SU(2)\) such that the pushforward of \(\nu\) by \(P\) is \(\rho(g)\,dg\), with normalized Haar measure \(dg\). In particular
\[
0<c_\rho\le\rho\le C_\rho<\infty.
\tag{3}
\]

**Proof.** Fix the other links and choose one link appearing once in \(C\). The map from that link to the product \(P\) has the form \(U_\ell\mapsto A U_\ell^{\pm1}B\), a smooth Haar-preserving diffeomorphism. Change variables to \(P\) and integrate the smooth positive density over the remaining compact link manifold. Smoothness and strict positivity follow; gauge invariance at the base gives conjugation invariance. Compactness gives (3). This argument does not assume independent plaquettes or a heat-kernel model for the marginal. \(\square\)

Parameterize
\[
g=\cos\theta\,I+i\sin\theta\,\mathbf n\cdot\boldsymbol\sigma,
\qquad 0\le\theta\le\pi.
\]
The restriction \(\rho(\theta)\) extends to a smooth even \(2\pi\)-periodic function. Put \(d\lambda=d\theta/(2\pi)\) on the full circle and define
\[
\begin{aligned}
q(\theta)&=2\sin^2\theta\,\rho(\theta),\\
t_k&=\int e^{ik\theta}\rho(\theta)\,d\lambda,\\
w_k&=\int e^{ik\theta}q(\theta)\,d\lambda
 =\mathbb E_\nu[\tfrac12\operatorname{tr}P^k]\\
&=t_k-\tfrac12(t_{k+2}+t_{k-2}).
\end{aligned}
\tag{4}
\]
Both moment sequences are real, even, and rapidly decreasing. The density \(q\) integrates to one and vanishes quadratically at \(0\) and \(\pi\); \(\rho\) need not integrate to one against \(d\lambda\).

For finite Laurent sums, the exact OS mixed norm is
\[
\left\langle\sum_n a_nP^n,\sum_m b_mP^m\right\rangle
=\sum_{n,m}\overline{a_n}b_m w_{m-n}
=\int\overline{\sum_n a_ne^{in\theta}}
             \sum_m b_me^{im\theta}\,q(\theta)\,d\lambda.
\tag{5}
\]
The Haar case \(\rho=1\) is a separate algebra control, not a replacement of the fixed interacting state. In that control,
\[
t_k=\delta_{k0},\quad
w_k=\delta_{k0}-\tfrac12\delta_{|k|,2},\qquad
\left\|\sum_n a_nP^n\right\|_{\mathrm{Haar}}^2
=\tfrac12\sum_{k\in\mathbb Z}|a_{k+2}-a_k|^2.
\tag{6}
\]
The actual and Haar norms on this observable family are comparable by (3).

## 3. An independently defined global source law

Use \(\mathcal D=C_c^\infty(\mathbb R)\) and
\[
F(\tau)=\widehat f(\tau)=\int e^{-i\tau x}f(x)\,dx.
\]
The pole-neutral target domain is
\[
\mathcal D^0=\{f\in\mathcal D:\int e^{x/2}f(x)\,dx
 =\int e^{-x/2}f(x)\,dx=0\}
 =(-\partial_x^2+1/4)\mathcal D.
\]
The law below is defined on all of \(\mathcal D\), then restricted to this domain when testing the target.

For \(n\ne0\), set
\[
\lambda_n=\operatorname{sgn}(n)\log|n|,\qquad
a_f(n)=|n|^{-1/2}F(\lambda_n),\qquad a_f(0)=0.
\tag{7}
\]
The half-density \(n^{-1/2}\) is the natural critical choice for counting windings on logarithmic scale: its squared size converts counting measure approximately into \(d\log n\). This specifies an ansatz; it is not inferred from a desired positive arithmetic Gram matrix. The prescription uses no zeta zeros, selected eigenvalues, prime coefficients, or support-dependent choice of theory.

For \(0<r<1\), define the smooth covariant boundary function
\[
A_{f,r}(U)=\sum_{n\ne0}r^{|n|}a_f(n)P(U)^n.
\tag{8}
\]
Exponential damping makes the series converge with all link derivatives. The undamped \(A_f\) will be its limit in the relevant form norm.

Fix the bi-invariant metric on \(SU(2)\) for which \(i\sigma_1,i\sigma_2,i\sigma_3\) are orthonormal. This is the unit-radius \(S^3\) convention, with fundamental Casimir 3. For all central spatial links, let
\[
\begin{aligned}
\mathfrak e_\nu(A,B)&=\sum_{\ell,a}
 \langle D_{\ell,a}A,D_{\ell,a}B\rangle_{\mathcal H_{\mathrm{full}}},\\
E_\nu&=\sum_{\ell,a}D_{\ell,a}^{*}D_{\ell,a},\qquad
D_{\ell,a}^{*}=-D_{\ell,a}-2D_{\ell,a}\log\Omega.
\end{aligned}
\tag{9}
\]
Take the nonnegative Friedrichs operator and restrict to the reducing covariant subspace. The full sum is essential for gauge covariance. This is the weighted electric Dirichlet operator of the [source-control lemma](OFF_DIAGONAL_RIGIDITY_AND_COMPACT_SOURCE_EXISTENCE_20260924.md), with its normalization now explicit. It is not identified with the physical transfer Hamiltonian or an arithmetic translation generator.

The proposed source law is
\[
\boxed{\quad J_E f=E_\nu^{1/2}A_f
       =\lim_{r\uparrow1}E_\nu^{1/2}A_{f,r}.\quad}
\tag{10}
\]
Sections 4–5 prove existence, a global mixed identity, and continuity. Every approximant on the right is a smooth covariant vector: a square root of this elliptic operator preserves smooth vectors, by spectral calculus and elliptic regularity. The limit is admitted in the existing OS Hilbert completion; it is not asserted to be bounded pointwise or a finite loop polynomial.

The square root acts on the full boundary space. The subspace of functions of \(P\) alone need not reduce \(E_\nu\), and the output of (10) need not remain in that subspace. The one-loop marginal will determine the energy pairing by the full Dirichlet-form identity; no projected one-variable operator is substituted for \(E_\nu\).

This source has more content than abstract membership in a regularity class. It fixes \(I\), the particular \(P^n\), their coefficients, and the operator determined by \(\nu\). The unitary weight transport from the [review control](SOURCE_DOMAIN_AND_WEIGHT_TRANSPORT_REVIEW_CONTROLS_20260925.md) does not preserve this entire prescription: it multiplies the distinguished loop functions and conjugates the differential operator. No claim that the prescription is uniquely selected by YM is needed or made.

## 4. Exact mixed pairing in the interacting state

For a single group variable, the unit \(S^3\) metric is
\(d\theta^2+\sin^2\theta\,d\mathbf n^2\). Since
\[
g^n=\cos(n\theta)I+i\sin(n\theta)\mathbf n\cdot\boldsymbol\sigma,
\]
direct differentiation gives
\[
\sum_a\tfrac12\operatorname{tr}
 [(D_ag^n)^\dagger D_ag^m]
=nm\cos((m-n)\theta)
 +\frac{2\sin(n\theta)\sin(m\theta)}{\sin^2\theta}.
\tag{11}
\]
The first term is radial. The second uses
\(|\nabla_{S^2}\mathbf n|^2=2\), and its apparent endpoint singularities are removable for integer windings. Integrating against \((2/\pi)\rho(\theta)\sin^2\theta\,d\theta\) yields the one-link Gram matrix
\[
\boxed{\quad D_{nm}
 =nm\,w_{m-n}+2\bigl(t_{m-n}-t_{m+n}\bigr).\quad}
\tag{12}
\]
Here \(n,m\) may be negative or zero. In particular the row \(n=0\) vanishes.

For each of the four links of \(C\), varying that link varies \(P\) by a left or right group derivative with an orthonormal basis rotated by an adjoint action. Bi-invariance makes the sum of squared derivatives equal to (11). Links outside \(C\) contribute zero. Thus the contour length \(\ell(C)=4\) multiplies (12). This step uses distinct links, not an independence assertion about their distribution.

**Proposition 1 (source existence and exact mixed identity).** Formula (10) defines one continuous linear map \(J_E:\mathcal D\to\mathcal H\), with no support cutoff in its definition. For every \(f,g\in\mathcal D\),
\[
\boxed{\quad
\langle J_Ef,J_Eg\rangle_{\mathrm{OS}}
=\ell(C)\lim_{r\uparrow1}
 \sum_{n,m\ne0}r^{|n|+|m|}
 \overline{a_f(n)}a_g(m)
 \left[nm\,w_{m-n}+2(t_{m-n}-t_{m+n})\right].
\quad}
\tag{13}
\]
For \(r<1\) the sum converges absolutely. The common Abel limit is part of the formula. Separately summing undamped pieces of its radial term can destroy the cancellation which makes the form finite.

The state enters through its actual marginal \(\rho\), hence through \(w\) and \(t\). No factorization of Wilson expectations or phenomenological diffusion law has been used. Equation (13) is an independently derived YM mixed pairing. It is not an assertion that this pairing is the Weil form.

## 5. Domain proof and a global obstruction

### 5.1 Exact Haar electric identity

Extend every finite coefficient sequence by zero to \(\mathbb Z\), put \(c(k)=ka(k)\), and write \(\Delta_2c(k)=c(k+2)-c(k)\). Substitution of the Haar moments into (12) gives
\[
\mathfrak e_{\mathrm{Haar}}^{(1)}(A,A)
=\tfrac12\sum_k|\Delta_2c(k)|^2
 +\sum_k|a(k)-a(-k)|^2.
\tag{14}
\]
The superscript denotes one group variable, before the factor \(\ell(C)\). Polarization gives the mixed version. The radial term uses the same finite-difference identity as (6), now applied to \(c\). The angular contribution is
\(2\sum|a|^2-2\sum\overline{a(k)}a(-k)\), exactly the second squared norm.

Controls include
\[
D_{11}=3,\qquad D_{22}=6,\qquad D_{-1,1}=-3/2
\quad(\rho=1).
\tag{15}
\]
The negative mixed entry is compatible with positivity of the full Gram form.

### 5.2 Logarithmic sampling and finite-difference bounds

There is an absolute constant \(C\) such that, for \(F\in\mathcal S(\mathbb R)\),
\[
\sum_{n\ge1}\frac{|F(\log n)|^2+|F(-\log n)|^2}{n}
\le C\bigl(\|F\|_2^2+\|F'\|_2^2\bigr).
\tag{16}
\]
For example, partition the positive half-line into intervals
\([\log n,\log(n+1)]\), of length \(\delta_n\asymp1/n\). The fundamental theorem of calculus and Cauchy–Schwarz imply
\[
\delta_n|F(\log n)|^2
\le2\int_{\log n}^{\log(n+1)}|F|^2
 +2\delta_n^2\int_{\log n}^{\log(n+1)}|F'|^2.
\]
Sum, and repeat on the negative half-line. Thus \(a_f\in\ell^2\), and (5) defines its Hilbert limit.

For the positive branch \(c(n)=\sqrt n F(\log n)\), use the interpolant
\[
b_+(u)=\sqrt u F(\log u),\qquad
b_+'(u)=u^{-1/2}\bigl(F'(\log u)+\tfrac12F(\log u)\bigr).
\]
Consequently
\[
\begin{aligned}
\sum_{n\ge1}|c(n+2)-c(n)|^2
&\le4\int_1^\infty |b_+'(u)|^2\,du\\
&=4\int_0^\infty|F'(v)+\tfrac12F(v)|^2\,dv.
\end{aligned}
\tag{17}
\]
For the negative branch use \(b_-(u)=-\sqrt u F(-\log u)\), whose derivative is
\(u^{-1/2}[F'(-\log u)-F(-\log u)/2]\). The finitely many differences crossing zero are controlled by point evaluations of \(F\), hence by its \(H^1\) norm. The angular term of (14) is at most \(4\|a_f\|_{\ell^2}^2\). Equations (14)–(17) therefore give
\[
\mathfrak e_{\mathrm{Haar}}^{(1)}(A_f,A_f)
\le C\bigl(\|F\|_2^2+\|F'\|_2^2\bigr),
\tag{18}
\]
once the closure assertion below is justified.

### 5.3 Why the Abel limit really is in the form domain

Let \(a^r(k)=r^{|k|}a_f(k)\), \(c^r(k)=ka^r(k)\). Equation (16) gives \(a^r\to a_f\) in \(\ell^2\), so both the Hilbert norm and the angular term converge.

On the positive tail,
\[
\Delta_2c^r(k)
=r^k\Delta_2c(k)+(r^2-1)r^k c(k+2).
\tag{19}
\]
The first term converges to \(\Delta_2c\) in \(\ell^2\). The squared norm of the second is bounded, up to an absolute constant for \(r\) near one, by
\[
(1-r)^2\sum_{k\ge1}(k+2)r^{2k}|F(\log(k+2))|^2.
\tag{20}
\]
This tends to zero: split off a finite head; on the tail \(F(\log(k+2))\) is uniformly small, while
\((1-r)^2\sum(k+2)r^{2k}\) is uniformly bounded. The negative tail and the finite crossing terms behave identically. Thus the Abel approximants converge in the Haar form norm.

For any function of \(P\), the actual norm and energy are bounded above and below by the Haar versions using (3), with the factor \(\ell(C)\) for energy. Therefore the approximants are Cauchy in the actual closed form norm as well. Closedness proves \(A_f\in\operatorname{Dom}E_\nu^{1/2}\), (10), and (13). Polarization is legitimate after this strong convergence.

An abrupt cutoff in winding number is not a substitute for this argument. Its edge term involves \(|c(N)|^2=N|F(\log N)|^2\), which need not tend to zero. The Abel construction removes that spurious boundary energy.

### 5.4 Ordinary local \(L^2\) bound and failure of the target

By Plancherel with the declared Fourier convention,
\[
\|F\|_2^2+\|F'\|_2^2
=2\pi\int(1+x^2)|f(x)|^2\,dx.
\]
Combining this with (18) and the marginal comparison gives
\[
\boxed{\quad
\|J_Ef\|_{\mathrm{OS}}^2
\le C_*\ell(C)C_\rho\int(1+x^2)|f(x)|^2\,dx.
\quad}
\tag{21}
\]
In particular, for \(\operatorname{supp}f\subset[-R,R]\),
\[
\|J_Ef\|_{\mathrm{OS}}^2
\le C_*\ell(C)C_\rho(1+R^2)\|f\|_2^2.
\tag{22}
\]
This proves the continuity asserted in Proposition 1. The constant does not depend on the modulation frequency or on the Abel parameter; dependence on the fixed model and on an enclosing support interval is permitted.

**Theorem 2 (exclusion of the electric critical-winding law).** Neither \(J_E\) nor any constant scalar multiple of it realizes the Weil form on all pole-neutral tests \(\mathcal D^0\). The same conclusion holds for the identical prescription on any finite \(SU(2)\) Wilson slab with a smooth positive boundary state and a fixed simple contour whose underlying links are distinct.

**Proof.** Put \(T=-\partial_x^2+1/4\), choose nonzero \(h\in C_c^\infty\), and use the exact pole-neutral tests
\[
f_\lambda=\lambda^{-2}T(e^{i\lambda x}h).
\tag{23}
\]
Their support is fixed, \(\|f_\lambda\|_2\) is bounded, and the [audited target calculation](GLOBAL_SOURCE_AND_WARD_IDENTITY_AUDIT_20260924.md) gives
\[
Q[f_\lambda]=\|h\|_2^2\log\lambda+O_h(1),\qquad\lambda\to+\infty.
\tag{24}
\]
Equation (22) instead gives \(\|J_Ef_\lambda\|^2=O_h(1)\). A constant normalization cannot reconcile these asymptotics. All steps used only a fixed simple contour and smooth positive finite-state marginal, proving the stated extension. \(\square\)

This is an all-input obstruction to a specified law, not a numerical failure at a few supports. Allowing another fixed finite coupling or a longer distinct-link contour only changes finite constants. It does not remove this obstruction.

### 5.5 Why the insertion was a genuine domain question

Before smearing, the winding seed is formally
\[
\Xi_x(P)=\sum_{n\ge1}n^{-1/2}
 \bigl(n^{-ix}P^n+n^{ix}P^{-n}\bigr).
\tag{25}
\]
It exists in \(\mathcal H\), locally smoothly in \(x\): in (6) the coefficient differences are \(O_x(n^{-3/2})\), with powers of \(\log n\) after \(x\)-differentiation. Boundary terms vanish because the coefficients tend to zero. Comparison (3) transfers these assertions to the actual state.

However \(\Xi_x\) is outside the electric form domain. On its positive branch
\[
\Delta_2 c(n)
=2(\tfrac12-ix)n^{-1/2-ix}+O_x(n^{-3/2}),
\]
so its squared radial differences have a divergent harmonic sum. The necessary square-summability in (14) also holds for form-domain limits, by the Fourier description of the weak derivatives; here it fails. The actual form has the same domain on this family by (3).

Thus \(E_\nu^{1/2}\Xi_x\) is not an ordinary Hilbert-valued density. Applying the insertion only after smearing is essential. Equations (16)–(22) are what nevertheless make the generalized law locally \(L^2\)-bounded and exclude its arithmetic identification.

## 6. What the native arithmetic identities do and do not supply

### 6.1 Winding operations and the Euler product

The continuous functional-calculus algebra \(C^*(P)\) is faithfully \(C(S^1)\): full support of the marginal gives the whole circle as spectral support. Repeated traversal defines
\[
(\Psi_nF)(z)=F(z^n),\qquad
\Psi_m\Psi_n=\Psi_{mn},\qquad\|\Psi_n\|_{C\to C}=1.
\tag{26}
\]
For \(\operatorname{Re}s>1\), absolute operator-norm convergence and unique factorization give
\[
\begin{aligned}
\mathcal Z(s)&=\sum_{n\ge1}n^{-s}\Psi_n
 =\prod_p(I-p^{-s}\Psi_p)^{-1},\\
\mathcal Z(s)^{-1}&=\sum_{n\ge1}\mu(n)n^{-s}\Psi_n,\\
-\mathcal Z'(s)\mathcal Z(s)^{-1}
 &=\sum_{p,m\ge1}(\log p)p^{-ms}\Psi_{p^m}.
\end{aligned}
\tag{27}
\]
The prime coefficients in this algebraic identity are derived from winding composition. They were not assigned as desired positive moments. The identity holds in a Banach algebra of operators on continuous functions, on the indicated half-plane.

The actual Hilbert metric gives a sharp limitation. With \(q\) from (4),
\[
\|\Psi_nF\|_{L^2(q)}^2
=\int|F(u)|^2q_n(u)\,d\lambda(u),\qquad
q_n(u)=\frac1n\sum_{j=0}^{n-1}
 q\!\left(\frac{u+2\pi j}{n}\right).
\tag{28}
\]
For every \(n\ge2\), \(q(\pi)=0\) quadratically while \(q_n(\pi)>0\). The preimage \(\pi/n\) is interior and has positive \(q\). A smooth bump of width \(\epsilon\) at \(u=\pi\) therefore has input squared norm of order \(\epsilon^3\) and image squared norm of order \(\epsilon\). Hence \(\Psi_n\) has **no bounded extension** on the Hilbert closure of this winding algebra. A formal isometric use of these operations in the OS pairing is invalid.

This does not prohibit densely defined winding operations with their true domains. It does prohibit transporting (27) directly into a bounded Hilbert-operator identity or into its critical line without a new argument. Source definition (10) was proved by Abel/form convergence, not by assuming such a continuation of \(\mathcal Z(s)\).

On the constant line, \(\mathcal Z(s)I=\zeta(s)I\). This is a rank-one identity present for any such winding algebra. Conversely, if a continuous \(F\) obeys \(\mathcal Z(s)F=\zeta(s)F\) for every real \(s>1\), uniqueness of absolutely convergent Dirichlet series gives \(\Psi_nF=F\). Invariance under doubling makes \(F\) constant: its values on all dyadic roots of unity equal \(F(1)\), and those roots are dense.

Taking the YM expectation is different. The scalar winding series
\[
D_C(s)=\sum_{n\ge1}w_n n^{-s}
\tag{29}
\]
is entire, since \(w_n\) decreases faster than every power of \(n\). In the Haar control it is just \(-2^{-s-1}\). The YM state is not a multiplicative character of the winding-operator algebra; the scalar zeta Euler product does not follow by averaging (27).

### 6.2 The exact Poisson identity is holonomy-twisted

To test completion as well as prime coefficients, choose the even Schwartz function
\[
\phi(u)=u^2(2\pi u^2-3)e^{-\pi u^2}.
\tag{30}
\]
For Fourier transform \(\mathcal F_{2\pi}\phi(v)=\int e^{-2\pi iuv}\phi(u)\,du\), Gaussian differentiation gives \(\widehat\phi=\phi\) and \(\phi(0)=\int\phi=0\). Define an actual smooth loop observable
\[
\Theta_\phi(t,P)=\sum_{n\in\mathbb Z}\phi(nt)P^n,\qquad t>0.
\tag{31}
\]
At an eigenvalue \(e^{2\pi i\alpha}\) of \(P\), Poisson summation reads
\[
\sum_n\phi(nt)e^{2\pi in\alpha}
=t^{-1}\sum_{k\in\mathbb Z}\widehat\phi((k-\alpha)/t).
\tag{32}
\]
One can obtain (32) directly by taking the Fourier coefficients in \(\alpha\) of its right side. The dual lattice is shifted by the holonomy angle. It is not the unshifted winding observable at \(t^{-1}\) for a general YM configuration.

At \(P=I\) the twist disappears, and
\[
\begin{aligned}
M\phi(s)&=\int_0^\infty t^{s-1}\phi(t)\,dt
 =\frac{s(s-1)}{4\pi}\pi^{-s/2}\Gamma(s/2),\\
\int_0^\infty t^{s-1}\Theta_\phi(t,I)\,dt
 &=2M\phi(s)\zeta(s)\,I=\frac{\xi(s)}\pi I.
\end{aligned}
\tag{33}
\]
Termwise Mellin integration starts at \(\operatorname{Re}s>1\); the vanishing and self-duality of \(\phi\) give rapid decay of \(\Theta_\phi(t,I)\) at both ends, hence its entire continuation. The factors in (33) follow from elementary Gaussian integrals.

Evaluation at \(P=I\) is not the YM expectation and is not a continuous functional on its \(L^2\) completion. That holonomy has measure zero. The actual mixed pairing is instead
\[
\langle\Theta_\phi(t,P),\Theta_\psi(u,P)\rangle
=\sum_{n,m}\overline{\phi(nt)}\psi(mu)w_{m-n},
\tag{34}
\]
for Schwartz \(\phi,\psi\) and positive \(t,u\). Equations (32)–(34) locate the failure of a proposed shortcut: an untwisted scalar completion can be read at trivial holonomy, but the physical pairing integrates all holonomies with the actual state.

## 7. A precise necessary test for the next mixed identity

The preceding calculation should be compared with the existing [separated-support determination theorem](OFF_DIAGONAL_RIGIDITY_AND_COMPACT_SOURCE_EXISTENCE_20260924.md), rather than repairing normalization constants first.

Let a future continuous source law \(J:\mathcal D^0\to\mathcal H\) be given independently, and write its profile pairing
\[
\mathcal B_J(h,k)=\langle JTh,JTk\rangle,
\qquad T=-\partial_x^2+1/4.
\]
Its distribution kernel exists by continuity. If it agrees with \(Q(Th,Tk)\) whenever \(h,k\) have disjoint supports, then on the open set \(x\ne y\) that kernel is forced to be
\[
\begin{aligned}
&-\left(-\partial_r^2+\tfrac14\right)^2n_\Gamma(|r|)\\
&\quad-\sum_{p,m\ge1}(\log p)p^{-m/2}
\left(-\partial_r^2+\tfrac14\right)^2
 \bigl[\delta(r-m\log p)+\delta(r+m\log p)\bigr],
\qquad r=x-y,
\end{aligned}
\tag{35}
\]
where \(n_\Gamma(r)=e^{-r/2}/(1-e^{-2r})\). The sum is locally finite. This statement needs neither positivity nor a preassigned native translation generator.

**Derivation.** Away from the diagonal, the gamma difference form has kernel \(-n_\Gamma(|x-y|)\), while each prime pair has kernel \(-c[\delta(r-d)+\delta(r+d)]\). Apply \(T_xT_y\), integrating by parts. For kernels of \(r\), this is
\[
\left(-\partial_r^2+\tfrac14\right)^2
=\partial_r^4-\tfrac12\partial_r^2+\tfrac1{16}.
\tag{36}
\]
The pole term vanishes on \(T\mathcal D\), and contact terms stay on the diagonal. Tensor products of disjointly supported profiles determine distributions on every rectangle away from that diagonal, proving (35).

In particular, near every isolated separation \(d=m\log p>0\), the kernel contains a fourth derivative of a delta distribution with exact leading coefficient \(-(\log p)p^{-m/2}\). A source pairing with a smooth kernel everywhere off the diagonal cannot satisfy this identity. Local contact adjustments and the three calibration anchors cannot supply the missing separated singularities.

These signed singularities are not by themselves inconsistent with positivity. For a control unrelated to YM, the positive law
\[
J_df=\sqrt c\,(f-U_df)\quad\text{in }L^2(\mathbb R),\qquad
U_df(x)=f(x-d),
\]
has kernel \(2c\delta(r)-c\delta(r-d)-c\delta(r+d)\). Pulling back by \(T\) gives exactly the corresponding derivative signs. This control prescribes \(c,d\), so it is not an independent arithmetic realization; it only prevents a false inference that the sign of (35) alone contradicts a Hilbert-space norm.

The next candidate must therefore pass two concrete tests: logarithmic growth on (23), and a YM-derived mixed identity with the separated singularities (35). A log correction chosen solely to force the first asymptotic would leave the second question untouched. Potential enlargements include genuinely unbounded families of contour complexity or different state-defined insertions, but their source domains and pairings must be derived before they count as progress. Nothing here proves that such an enlargement works.

## 8. Verification, literature, and remaining gap

The [checker](../numerics/check_winding_electric_pairing.py) and [small record](../numerics/records/winding-electric-pairing-20260925.json) test (5), (12), and (14) against direct angular integration of the scalar and vector components of finite Laurent observables. There are 64 checks, including complex mixed pairs, negative windings, the constant null row, and the fundamental Casimir normalization. All passed; maximum scaled discrepancy was below \(1.6\times10^{-15}\) in the recorded environment.

The two densities are Haar and an explicitly prescribed smooth positive central polynomial control. They are not samples or estimates of the interacting state. Floating quadrature is an algebra diagnostic, not an interval certificate. The infinite-source limit and the target obstruction are analytical arguments in §5 and do not depend on the numerical tolerances.

Primary-source checks made for this continuation:

- Brzoska, Lenz, Negele and Thies, [*Diffusion of Wilson Loops*, arXiv:hep-th/0412003v2](https://arxiv.org/pdf/hep-th/0412003v2), p. 2, equations (7)–(10), gives the radial \(SU(2)\) Laplacian and eigenvalue normalization. Its introduction explicitly describes a phenomenological diffusion model. Only the group-geometric normalization is used here; its diffusion ansatz is not substituted for four-dimensional YM dynamics or for \(\rho\).
- [NIST DLMF §25.12(ii)](https://dlmf.nist.gov/25.12#ii), especially equation 25.12.10, identifies the ordinary polylogarithm series underlying a scalar eigenvalue of the winding seed. The proof here uses coefficient differences and does not import a boundary asymptotic or an analytic continuation without a domain argument.

The marginal lemma, exact interacting Gram formula, Abel-domain bound, winding-metric obstruction, and profile-kernel test are deductions in this note, not theorems attributed to those sources. Third-party papers are not stored in the repository. No novelty claim or independent validation is implied.

**Decision.** A genuine source prescription and its mixed pairing are now concrete for one generalized winding/electric family. That family is analytically rejected as an all-support Weil realization. Winding arithmetic and scalar zeta completion survive as algebraic controls, but do not provide the required physical metric. The remaining open problem is an independently defined source law whose actual YM pairing passes both (24) and (35), with a proved admissible global domain. The compact existence and three-constant determination theorems remain available if such source relations can be obtained.
