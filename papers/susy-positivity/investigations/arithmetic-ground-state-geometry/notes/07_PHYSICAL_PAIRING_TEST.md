# An exact physical metric test: shape dependence cannot be removed from both norm and period

13 September 2026. This note continues the saved manuscript with an analytic test of its interacting prime model. The result concerns a specified positive Hilbert problem, identity source and real-cycle period. It is not an exclusion of other sources, boundary constructions or the full arithmetic program.

## Result

The physical identity-state norm of the cross-coupled quartic model depends only on the modulus of its complex interaction parameter. Its real-cycle holomorphic period does not have this property. Consequently the ratio between that norm and the squared modulus of the period is nonconstant on every nonempty complex-open parameter region.

This gives a concrete obstruction beyond the fixed-coupling period test. A nonconstant holomorphic variation of the interaction shape cannot retain both the Euler period and the physical Euler metric by any common scalar renormalization of the identity source. The conclusion does not require calculating the physical metric or estimating it numerically.

## 1. The physical problem and the two quantities

On the complete flat target C squared, let

\[
G_c(A,B)=\frac12(A^2+B^2)
+\frac c4(A^4+B^4+A^2B^2),\qquad c\in\mathbb C\setminus\{0\}.
\]

The physical normalization is

\[
\mathcal W_c=G_c/2,\qquad f_c=\mathcal W_c/2=G_c/4,
\qquad D_c=\bar\partial+\partial f_c\wedge.
\]

The underlying Hilbert space is the ordinary positive space of square-integrable complex differential forms. In the real de Rham charge conventions of the construction,

\[
D_c=\frac{Q_1-iQ_2}{2},\qquad
\{D_c,D_c^\dagger\}=H_{\rm physical}/2.
\]

Thus the two descriptions have the same physical harmonic kernel and the same norm. No unproved change of the physical inner product is involved.

For every nonzero complex c, the leading homogeneous gradient has no nonzero complex zero. It grows cubically while the Hessian grows quadratically. Strong tameness therefore holds. The critical points are the origin, four axis points and four both-nonzero points; they are nondegenerate for every such c. The strongly tame Kähler–Stein Hodge theorem gives nine normalizable middle-degree harmonic representatives and their Jacobi-class identification. This is the analytic input from [Fan, *Schrödinger equations, deformation theory and tt*-geometry](https://arxiv.org/abs/1107.1290). The coefficient and Laplacian conventions agree with his twisted differential after setting f=G/4.

Let alpha_c be the harmonic representative of the identity holomorphic volume class

\[
\Omega=dA\wedge dB,
\qquad H(c,\bar c)=\|\alpha_c\|^2>0.
\]

The class is nonzero, since the constant polynomial is nonzero in the Jacobi ring. All source comparisons below retain this volume-coordinate normalization.

Separately, define the holomorphic real-cycle period

\[
C_{\rm per}(c)=\frac1{2\pi}\int_{\mathbb R^2}e^{-G_c(A,B)}\,dA\,dB,
\qquad \Re c>0.
\]

The factor 1/(2pi) is fixed. It is not derived from the physical norm. The period uses the weight exp(-G)=exp(-4f), whereas the physical differential uses f. We do not assume that this scalar integral is a canonical physical boundary covector or that it is the norm of a state. The distinction between physical vacuum metrics and holomorphic limiting brane amplitudes is also explicit in [Cecotti, Gaiotto and Vafa, *tt* Geometry in 3 and 4 Dimensions](https://arxiv.org/abs/1312.1008).

Where the period is nonzero, put

\[
R(c,\bar c)=\frac{H(c,\bar c)}{|C_{\rm per}(c)|^2}.
\]

A common source multiplier changes numerator and denominator by the same squared modulus and therefore leaves this ratio unchanged. Fixed convention-dependent constants do not affect the results below.

## 2. Exact radiality of the physical metric

Two unitary or conformal covariance statements determine its phase dependence without solving for alpha_c.

First write

\[
\phi_c(A,B)=(\sqrt c\,A,\sqrt c\,B),\qquad t=1/c.
\]

On a local square-root branch,

\[
f_c=\phi_c^*(t f_1),\qquad
\phi_c^*g_{\rm flat}=|c|g_{\rm flat},\qquad
\phi_c^*(dZ_1\wedge dZ_2)=c\,dA\wedge dB.
\]

Pullback intertwines the twisted differential. A constant metric rescaling g to a g multiplies its adjoint and Laplacian by a to the minus one, so changes no harmonic kernel. In real dimension four the squared L2 norm of a two-form is invariant under this constant conformal change. If beta_t is the harmonic representative of the identity volume class for t f_1 in the Z coordinates, naturality and uniqueness give

\[
\alpha_c=c^{-1}\phi_c^*\beta_{1/c},\qquad
H(c,\bar c)=|c|^{-2}\|\beta_{1/c}\|^2.
\tag{1}
\]

This is the same middle-degree conformal argument used for the mass-scaled Euler metric. It now isolates a genuine superpotential-strength parameter t, rather than removing the entire deformation by coordinate pullback.

Second, define a unitary operator on forms by their holomorphic degree:

\[
\mathsf U_\theta\big|_{\Omega^{p,q}}
=e^{ip\theta}\,\mathrm{id}.
\]

The operator bar-partial preserves p, while wedge multiplication by partial f increases p by one. Therefore, including the Hilbert adjoints,

\[
\mathsf U_\theta D_f\mathsf U_\theta^{-1}
=D_{e^{i\theta}f},\qquad
\mathsf U_\theta\{D_f,D_f^\dagger\}\mathsf U_\theta^{-1}
=\{D_{e^{i\theta}f},D_{e^{i\theta}f}^\dagger\}.
\tag{2}
\]

The identity volume form has holomorphic degree two. Consequently its fixed-source harmonic representative transforms as

\[
\beta_{e^{i\theta}t}
=e^{-2i\theta}\mathsf U_\theta\beta_t,
\qquad
\|\beta_{e^{i\theta}t}\|=\|\beta_t\|.
\tag{3}
\]

The compensating phase keeps the Jacobi volume class fixed; it has unit modulus. Equations (1)–(3) prove the exact statement

\[
\boxed{\quad H(c,\bar c)=H(|c|,|c|).\quad}
\tag{4}
\]

The norm is radial in the physical complex shape parameter. This is a consequence of the specified dynamics and source, rather than a choice made while solving the metric equations.

The same reasoning constrains the full three-dimensional symmetry sector. In the holomorphic polynomial-volume frame

\[
\bigl(1,\;c(A^2+B^2),\;c^2A^2B^2\bigr)\Omega,
\]

all three sources pull back from c-independent polynomials in Z with the same factor c to the minus one. They also all have holomorphic form degree two. The entire Hermitian matrix in this frame is therefore radial. This supplies a physical symmetry constraint for the reduced matrix tt* problem; it does not determine that matrix.

## 3. The period cannot be the squared norm up to a fixed factor

Holomorphy of C_per on Re c>0 follows by dominated differentiation on compact subsets. For real c>0 it is positive and strictly decreasing:

\[
C_{\rm per}'(c)
=-\frac1{8\pi}\int_{\mathbb R^2}
(A^4+B^4+A^2B^2)e^{-G_c}\,dA\,dB<0.
\tag{5}
\]

Also C_per(c) tends to one as c decreases to zero, by dominated convergence against the quadratic Gaussian.

**Proposition.** There is no nonempty complex-open region in Re c>0 on which

\[
H(c,\bar c)=K|C_{\rm per}(c)|^2
\]

for a constant K>0. Equivalently, R is constant on no such region.

**Proof.** Suppose the equality holds on a connected open patch. Its period is nonzero there because H is positive. By (4), its modulus is locally constant under angular variation. Hence

\[
\Im\left(c\frac{C_{\rm per}'(c)}{C_{\rm per}(c)}\right)=0.
\]

The expression in parentheses is a holomorphic function taking real values on an open set, so is a real constant k. Thus c C_per' minus k C_per vanishes on that patch and, by the identity theorem, on the whole right half-plane. On the positive real axis this gives C_per(r)=A r^k. Its finite nonzero limit one at r=0 forces k=0 and A=1. This contradicts (5). The argument does not require a global zero-free theorem for the period. QED.

There is a sharper explicit check near the Gaussian end. Gaussian moments give

\[
C_{\rm per}(c)=1-\frac74c+O(|c|^2),
\qquad \Re c\ge0,\quad |c|\to0.
\tag{6}
\]

Indeed E(A^4+B^4+A^2B^2)=3+3+1=7 under the normalized quadratic Gaussian. The quadratic remainder is uniformly dominated by its eighth-degree Gaussian moment when Re c is nonnegative, so (6) is a controlled local asymptotic statement, not a numerical expansion.

For fixed theta with |theta|<pi/2, the unknown physical metric cancels exactly between points of the same modulus. Thus

\[
\frac{R(re^{i\theta},re^{-i\theta})}{R(r,r)}
=\frac{|C_{\rm per}(r)|^2}{|C_{\rm per}(re^{i\theta})|^2}
=1-\frac72r(1-\cos\theta)+O(r^2).
\tag{7}
\]

For nonzero such theta and sufficiently small positive r, this ratio is strictly less than one. This directly exhibits a change in the source-normalization-invariant physical-to-period ratio without knowing H(r,r).

## 4. Consequence for a holomorphic shape repair of the Euler factor

Consider the enlarged prime family

\[
F_M(U,V)=G_{c(M)}(\sqrt M\,U,\sqrt M\,V),\qquad M\ne0,
\]

on a complex-open mass domain, with a nonconstant holomorphic shape c(M) taking values in Re c>0. Use the fixed identity volume source and the correspondingly transported real cycle. Pointwise conformal covariance gives

\[
\mathcal P(M)=\frac{C_{\rm per}(c(M))}{M},\qquad
g(M,\bar M)=\frac{H(c(M),\overline{c(M)})}{|M|^2}.
\]

Allow any common finite scalar source renormalization r(M). If it preserved both Euler dependences with fixed nonzero period constant A and norm constant B>0, it would have to satisfy

\[
r(M)C_{\rm per}(c(M))=A,
\qquad
|r(M)|^2H(c(M),\overline{c(M)})=B.
\]

Dividing gives R(c(M),overline{c(M)})=B/|A|^2. The open mapping theorem sends the nonconstant holomorphic c(M) to an open shape region. The proposition excludes a constant R there. Therefore

\[
\boxed{\text{No common scalar source renormalization preserves both
the identity Euler period and its physical Euler metric
along a nonconstant holomorphic shape variation.}}
\]

The scalar r need not be assumed holomorphic for the cancellation argument. Nonzero fixed period A already forces the relevant factors to be nonzero. The obstruction concerns preserving two specified local-factor identities; it does not assert that either identity is itself the full target of the arithmetic program.

## 5. Scope and the next physical question

This result is stronger than the fact that the real-cycle period changes with the interaction: even scalar source compensation cannot keep both specified quantities fixed on a holomorphic parameter region. It is also more limited than an obstruction to every interacting completion.

The hypotheses retain the identity class, the transported real-cycle period, the ordinary flat target metric, the stated physical differential and the use of a common scalar source. Mixing the three symmetry-sector source classes, changing the cycle or boundary problem, adding physical fields, changing the target geometry, or matching a different full pairing can evade these hypotheses. Such changes need a physical preparation and gluing law; a fitted parameter-dependent vector of periods is not supplied by the present construction.

Radiality by itself does **not** prove that R varies along the positive real c axis. Equation (7) compares complex shapes of equal modulus. The complex-open result is nevertheless sufficient for the holomorphic shape-repair corollary. A separate real-axis monotonicity theorem or explicit physical metric calculation has not been obtained here.

No semiclassical identification of H with a sum of inverse Hessian determinants is used. At c=0 eight classical critical points escape to infinity and the vacuum rank changes, so convergence to the single Gaussian physical metric cannot be assumed. Massive-vacuum asymptotics and residue reality may provide further information, but they are unnecessary for the exact obstruction proved above.

The useful next pairing calculation is therefore to specify a physical boundary/source map in the three-dimensional symmetry sector and determine its full positive Gram matrix or orthogonal residual. This would test whether state mixing contributes something beyond the scalar normalization excluded here. The identity period alone has no established physical boundary-vector interpretation at its chosen exponential scale.

## 6. A physical endpoint at large positive shape

There is also a controlled endpoint as c tends to positive infinity. This requires a theorem that permits a degenerate critical point: the Morse hypothesis in Fan's vacuum-counting theorem cannot simply be dropped. The comparison theorem of [Si Li and Hao Wen, *On the L2-Hodge theory of Landau-Ginzburg models*](https://arxiv.org/abs/1903.02713), together with the continuity argument below, supplies the needed justification.

Write q4(Z)=Z1^4+Z2^4+Z1^2 Z2^2 and s(Z)=Z1^2+Z2^2. Set

\[
\varphi_c(A,B)=(c^{1/4}A,c^{1/4}B),\qquad
\varepsilon=c^{-1/2},\qquad
\widetilde f_\varepsilon(Z)=\frac{q_4(Z)}{16}
+\frac{\varepsilon s(Z)}8.
\]

Then f_c=varphi_c^* tilde f_epsilon. The pure-quartic limit is tilde f_0=q4/16. Although its critical point is degenerate, it remains confining in the quantum Hilbert problem.

### The non-Morse Hodge input and its hypotheses

Li–Wen's strongly elliptic condition requires, for every delta>0 and integer k>=2,

\[
\delta|\nabla f|^k-|\nabla^k f|\longrightarrow+\infty
\quad\text{at infinity}.
\]

For epsilon in a bounded neighborhood of zero, the quartic gradient has no nonzero complex zero and gives the uniform estimates

\[
|\nabla\widetilde f_\varepsilon|\ge aR^3-bR,\qquad
|\nabla^k\widetilde f_\varepsilon|\le C_k(1+R^{4-k})
\quad(2\le k\le4).
\]

Derivatives of higher order vanish. These estimates verify the stronger ellipticity condition, uniformly outside a sufficiently large compact set. The flat target is complete with bounded geometry, and all critical points remain in a common compact set as epsilon tends to zero.

Their Theorem 2.34 identifies the compact-support, weighted smooth-L2 and ordinary smooth twisted-Dolbeault cohomologies under these hypotheses. Combined with their Hodge decomposition, it identifies the physical harmonic states with the smooth twisted cohomology without a Morse assumption. On C squared the latter is the holomorphic Koszul/Jacobi cohomology, concentrated in total form degree two. At epsilon=0 the two homogeneous cubic partial derivatives form a regular sequence with only the origin as common zero. Its Hilbert series is

\[
\frac{(1-z^3)^2}{(1-z)^2}=(1+z+z^2)^2,
\]

so its dimension is nine. For nonzero epsilon the nine simple critical points give the same dimension. Thus the physical kernel has dimension exactly nine throughout this family, including the degenerate endpoint. This conclusion uses the non-Morse comparison theorem; spectral continuity alone would only give an upper-semicontinuity statement and would not suffice.

### Continuity of the physical metric in fixed polynomial sources

The twisted Laplacians have common closed form domain

\[
\mathcal Q=\{u\in H^1\Omega^*(\mathbb C^2):R^3u\in L^2\},
\]

with equivalent form norms near epsilon=0. Indeed the scalar potential is comparable to R^6 at large radius, the Hessian is lower order, and the parameter-dependent difference of potentials is bounded by

\[
C\bigl(|\varepsilon|R^4+|\varepsilon|^2R^2+|\varepsilon|\bigr).
\]

It tends to zero in the relative form norm as epsilon tends to zero. Adding a fixed sufficiently large positive constant makes the forms uniformly coercive on Q. The inverse-operator identity for these bounded maps from Q to its dual then gives norm-resolvent continuity on L2. Each operator has compact resolvent, and the kernel has the constant dimension nine just proved. A spectral contour surrounding zero therefore gives a norm-continuous physical projector P_epsilon and a positive spectral gap uniform in a sufficiently small parameter neighborhood.

To ensure this comparison retains the chosen polynomial sources, choose a single compact-support cutoff rho equal to one near every critical point in the small parameter family. In the proof of Li–Wen's comparison theorem, the explicit operators are

\[
V_f=\frac{(df\wedge)^\dagger}{|df|^2},\qquad
T_{\rho,f}=\rho+(\bar\partial\rho)V_f
\bigl(1+[\bar\partial,V_f]\bigr)^{-1}.
\]

The inverse is a finite series by bidegree. All denominators occur away from the common critical neighborhood, where they are uniformly bounded on the relevant cutoff annulus. For any fixed polynomial-volume source p(Z) dZ1 wedge dZ2, the form

\[
u_{p,\varepsilon}=T_{\rho,\widetilde f_\varepsilon}
\bigl(p(Z)dZ_1\wedge dZ_2\bigr)
\]

is compactly supported, represents the same twisted cohomology class, and depends continuously on epsilon in L2. Its physical harmonic representative is P_epsilon u_{p,epsilon}. It therefore depends continuously on epsilon. This explicitly rules out silently changing the identity-source normalization while crossing the critical-point collision.

In the three-source frame (1,s,t) times Omega_Z, with t=Z1 squared Z2 squared, denote this continuous positive Gram matrix by g_tilde(epsilon). Then

\[
\widetilde g(\varepsilon)=g_0+o(1),\qquad g_0>0.
\tag{8}
\]

### The endpoint symmetry diagonalizes the reference Gram matrix

Let rho_theta act on the target by Z to exp(i theta) Z and let rho_theta^* be its unitary pullback on forms. Since tilde f_0 is homogeneous of degree four, the combined unitary

\[
\mathsf S_\theta=\mathsf U_{-4\theta}\rho_\theta^*
\]

commutes with D_tilde f0 and its adjoint. A homogeneous polynomial p of degree d times the holomorphic two-form has character

\[
\mathsf S_\theta(p\Omega_Z)
=e^{i(d-6)\theta}p\Omega_Z.
\]

The sources 1, s and t have distinct characters -6, -4 and -2. Their harmonic representatives have the same characters by uniqueness. Orthogonality of distinct unitary characters implies

\[
g_0=\operatorname{diag}(a_0,a_1,a_2),\qquad a_i>0.
\tag{9}
\]

The positivity is strict because all three Jacobi classes are nonzero at the pure-quartic point. In particular the degree-four class t spans the nonzero top-degree part of the above Jacobi Hilbert series.

### Endpoint powers in the original source frame

Under varphi_c, the three sources in the E frame transform as

\[
\begin{aligned}
\Omega_{A,B}&=c^{-1/2}\varphi_c^*\Omega_Z,\\
c(A^2+B^2)\Omega_{A,B}&=\varphi_c^*(s\Omega_Z),\\
c^2A^2B^2\Omega_{A,B}&=c^{1/2}\varphi_c^*(t\Omega_Z).
\end{aligned}
\]

Middle-degree norm invariance under this constant conformal dilation gives the exact matrix relation

\[
g_E(c)=D_c^\dagger\widetilde g(c^{-1/2})D_c,
\qquad D_c=\operatorname{diag}(c^{-1/2},1,c^{1/2}).
\tag{10}
\]

Consequently, as c tends to positive infinity,

\[
\boxed{\quad
g_E(c)=D_c^\dagger
\bigl[\operatorname{diag}(a_0,a_1,a_2)+o(1)\bigr]D_c,
\qquad H(c,c)=\frac{a_0+o(1)}c.\quad}
\tag{11}
\]

These are physical endpoint powers derived from the specified Hilbert dynamics and source classes. They are not parameters fitted to the tt* equations. In particular, a constant positive matrix in the fixed E frame cannot be the physical metric of this model: its identity entry would be constant, whereas (11) tends to zero. This excludes that algebraic flat control in the specified frame; it is not an exclusion of every conceivable flat connection after changing the physical source map.

For comparison, the same coordinate change in the real-cycle integral gives

\[
C_{\rm per}(c)=\frac{b_0+o(1)}{\sqrt c},\qquad
b_0=\frac1{2\pi}\int_{\mathbb R^2}e^{-q_4(Z)/4}\,dZ_1\,dZ_2>0.
\]

Hence

\[
R(c,c)\longrightarrow\frac{a_0}{b_0^2}\in(0,\infty).
\]

Neither this limit nor its derivation identifies a0 with b0 squared. The endpoint calculation does not supply the small-c asymptotics or an explicit value of any physical norm.

## Sources and status

- Huijun Fan, [*Schrödinger equations, deformation theory and tt*-geometry*](https://arxiv.org/abs/1107.1290). Used for the strongly tame physical Hodge/Jacobi framework. The phase conjugation, conformal scaling and ratio argument above are explicit deductions for this model.
- Sergio Cecotti, Davide Gaiotto and Cumrun Vafa, [*tt* Geometry in 3 and 4 Dimensions*](https://arxiv.org/abs/1312.1008). Used for the distinction between physical vacuum geometry and holomorphic brane limits, not as a norm identity for C_per.
- Si Li and Hao Wen, [*On the L2-Hodge theory of Landau-Ginzburg models*](https://arxiv.org/abs/1903.02713), published in *Advances in Mathematics* 396 (2022), 108165. Their non-Morse comparison theorem and Hodge decomposition justify the degenerate pure-quartic endpoint. Uniform polynomial estimates, spectral/source continuity and endpoint powers are checked explicitly above.

The model calculations, radiality result and simultaneous-preservation obstruction are new deductions in this investigation. They have been internally cross-checked, but have not undergone independent specialist review. No positivity claim for the complete Weil form is made.
