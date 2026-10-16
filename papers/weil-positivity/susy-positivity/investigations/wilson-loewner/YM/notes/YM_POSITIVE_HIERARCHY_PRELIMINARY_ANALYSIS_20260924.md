# A positive state space for the YM Loewner hierarchy: memory, projection error and the reflection boundary

24 September 2026. Prepared for Edward Baker with substantial LLM assistance.

**Model:** GPT-6 (Codex; developer-provided identity).  
**Reasoning effort:** not exposed; not inferred.  
**Baseline:** repository commit `488c782b639728a5dfd9685139b81e09cbb1cd40`, with the uncommitted [updated path assessment](../../notes/UPDATED_PATH_ASSESSMENT_REFLECTION_AND_HIERARCHIES_20260924.md) from this conversation.  
**Status:** preliminary analytical work and finite diagnostics. The Hilbert-space statements below are proved under explicit regulated hypotheses. The numerical examples use prescribed smooth backgrounds, not a sampled YM measure. No continuum four-dimensional construction, interacting N4SYM reflection theorem, or arithmetic realization is claimed. No independent specialist review has occurred.

The [research plan](YM_REFLECTION_AND_HIERARCHY_RESEARCH_PLAN_20260924.md) gives the next experiments and their success criteria.

## 1. What the preliminary analysis establishes

There is a concrete way to continue the physical hierarchy without assuming finite closure. For pure gauge transport, the entire matrix-valued Wilson loop is a unit vector in a positive space of field-dependent observables. Projecting this vector onto its scalar expectation gives an exact memory equation. Projecting onto a finite, moving family gives a norm-preserving approximation with an explicit residual bound.

For the first family, consisting of the identity and the transported curvature moment J, the residual separates into two nonnegative quantities:

- variation of J orthogonal to the retained family, which includes the covariant-derivative and transverse content;
- the part of J squared orthogonal to that family, which measures curvature fluctuations beyond the retained moments.

These terms are retained in an error estimate. No field equation sets them to zero. In a finite SU(2) background ensemble, the resulting bound on the Wilson expectation is small enough to resolve its departure from one.

There is also a limitation that must be made explicit: a positive configuration-space norm does not automatically descend to an Osterwalder–Schrader (OS) quotient. Section 7 gives an exact finite counterexample. The proposed physical bridge is therefore a **spatial time-slice construction using a positive lattice transfer matrix**, with the reference color fiber specified. It is not arbitrary multiplication in a half-space OS algebra.

This is useful progress on a regulated hierarchy, not a solution for the original N=4 scalar-coupled loop. Pure YM changes two important hypotheses: its ordinary holonomy is unitary, and Wilson lattice YM at theta zero has a positive measure. The N4SYM calculation did not have this combination for its chosen observable.

## 2. The observable and the three levels of rigor

Keep the gauge group SU(N), coupling, action and state fixed. Let a specified Loewner driver generate a planar trace, completed by a straight return chord. Use the notation of the [parent YM derivation](../../notes/GENUINE_LOEWNER_TRACE_YM_HIERARCHY_20260921.md):

\[
Q_t=R_t(1)^{-1}U_t,\qquad
J_t=\int_0^1 r\,\widehat F_{12,t}(r)\,dr,
\qquad k_t=q_1\dot q_2-q_2\dot q_1.
\]

For a smooth Hermitian gauge connection,

\[
\dot Q_t=i k_tJ_tQ_t,\qquad J_t^*=J_t,\qquad
\operatorname{tr}J_t=0,\qquad Q_t^*Q_t=I.                 \tag{2.1}
\]

The completed contour is based at a fixed point. The curvature moment and Q transform by conjugation in that basepoint fiber. Traces of their paired products are gauge invariant.

Three settings must remain distinct:

| Setting | What is available here |
|---|---|
| Finite Wilson lattice, theta zero, spatial polygonal loops | Positive measure and unitary loop matrices; exact discrete shape evolution and finite Gram identities |
| A positive regulated measure with smooth connections and controlled J | Continuous identity (2.1), exact projection memory and the residual theorems below |
| Unflowed continuum 4D YM or the scalar-coupled N4SYM loop | Additional construction, domain and renormalization obligations; no automatic extension |

The continuous memory proposition is initially stated with bounded multiplication generators and integrable operator norms on a finite capacity interval. This is enough for a rigorous time-ordered propagator and its compressed generator. An unbounded extension requires a common domain and a proof that the compressed generator defines the required evolution; self-adjointness of the full operator does not by itself settle the compression.

A finite lattice does not provide the differentiable continuum tip equation by itself. The exact lattice construction is discrete, as described in Section 7. Taking a smooth-contour limit or choosing a smooth gauge-covariant interpolation is a further step. Likewise, four-dimensional gradient flow supplies smooth probes under the parent's assumptions but need not preserve half-space support for an OS argument.

## 3. Positive configuration space and exact storage

Let mu be the normalized, fixed positive regulated measure. Equip matrix-valued observables with

\[
\langle X,Y\rangle_\mu
=\mathbb E_\mu\frac1N\operatorname{tr}(X^*Y),\qquad
\mathcal H_\mu=L^2(\mu;\operatorname{End}\mathbb C^N),
\qquad e(A)=I.
\]

The inner product is conjugate-linear in its first slot, and \(\|e\|=1\). Where a gauge-covariant subspace is imposed, multiplication below preserves it. Define the skew-adjoint multiplication generator

\[
\mathsf A_tX=i k_tJ_tX.
\]

For bounded regulated coefficients, it generates a unitary propagator \(\mathsf U(t,s)\). Equation (2.1) states that \(\Psi_t=Q_t=\mathsf U(t,0)e\). The Wilson expectation is

\[
W(t)=\langle e,\Psi_t\rangle_\mu.
\]

With \(P=|e\rangle\langle e|\), \(P_\perp=I-P\), and \(z_t=P_\perp\Psi_t\), orthogonality gives the exact identity

\[
\boxed{|W(t)|^2+\|z_t\|_\mu^2=1.}                     \tag{3.1}
\]

The second term is the squared distance from Q to its scalar mean times the identity. It includes color-matrix variation as well as configuration fluctuations. It is not merely the variance of the normalized scalar trace.

The elementary inequality \(|W|\leq1\) is familiar; it is not the novelty of this analysis. Its useful role is to identify the positive state space in which the hierarchy can be projected and its error measured.

Nor is \(\|z_t\|^2\) necessarily increasing. A two-state unitary rotation has \(W=\cos t\), storage \(\sin^2t\), and perfect return of the stored amplitude. Thus the storage identity does not justify pointwise dissipation, a Markov approximation, or contraction from every intermediate shape to every later shape. It also concerns one prepared state, not an arbitrary waveform input.

For the SU(N) curvature moment, \(\langle e,\mathsf A_te\rangle=0\). Set

\[
v_t=\mathsf A_te=i k_tJ_t.
\]

The exact projected equations are

\[
\dot W=-\langle v_t,z_t\rangle,\qquad
\dot z_t=v_tW+P_\perp\mathsf A_tP_\perp z_t.            \tag{3.2}
\]

The unresolved observables live in z. They have not been assumed small.

## 4. Exact nonstationary memory with a positive Gram kernel

Let \(\mathsf R(t,s)\) be the unitary propagator of the compressed skew-adjoint generator on the complement. Since \(z_0=0\),

\[
z_t=\int_0^t\mathsf R(t,s)v_sW(s)\,ds,
\]

and hence

\[
\boxed{\dot W(t)=-\int_0^t\Gamma(t,s)W(s)\,ds,\qquad
\Gamma(t,s)=\langle v_t,\mathsf R(t,s)v_s\rangle.}       \tag{4.1}
\]

Extend the expression to both time orders by the unitary propagator. With \(w_t=\mathsf R(t,0)^*v_t\),

\[
\Gamma(t,s)=\langle w_t,w_s\rangle,\qquad
\sum_{ij}\bar c_i\Gamma(t_i,t_j)c_j\geq0.               \tag{4.2}
\]

Thus the full two-time kernel is positive definite. Individual values need not be positive, and multiplying the kernel by a causal step function does not make it a self-adjoint positive operator. The retained state has the explicit norm

\[
\|z_T\|^2=\left\|\int_0^T w_sW(s)\,ds\right\|^2.
\]

The construction is a time-dependent projection argument of the type introduced in [Mori's projection formalism](https://doi.org/10.1143/PTP.33.423). We derive the particular nonstationary formula here from (3.2); a stationary thermal fluctuation-dissipation theorem is not being imported into Loewner capacity.

Equation (4.1) is exact under its hypotheses and defines its kernel independently of W through the microscopic generator and complementary propagator. It avoids the circular replacement of an unknown derivative by W'/W. Nevertheless, evaluating R can be as difficult as the original hierarchy. This representation organizes the missing information; the finite-family residual in the next section is what makes the proposal testable.

For \(g(t)=\mathbb E\operatorname{tr}J_t^2/N\), one immediate bound is

\[
|\Gamma(t,s)|\leq |k_tk_s|\sqrt{g(t)g(s)}.              \tag{4.3}
\]

No convolution structure follows: changing the contour changes J. Causality here means dependence on previous values of the shape parameter. It does not mean a Lorentzian response to a laboratory source.

## 5. A moving observable family with an analytical error estimate

### 5.1 General finite family

Choose differentiable, linearly independent observables \(b_0(t)=e,b_1(t),\ldots,b_{m-1}(t)\), in the common domain. Let B be the map taking coefficients to their linear combination, and set

\[
G=B^*B,\qquad M=B^*\mathsf A B,\qquad C=B^*\dot B.
\]

The Galerkin condition is \(B^*(\dot\Psi_m-\mathsf A\Psi_m)=0\), with \(\Psi_m=Bc\), giving

\[
\boxed{G\dot c=(M-C)c.}                               \tag{5.1}
\]

Since \(M^*=-M\) and \(\dot G=C+C^*\), differentiation proves

\[
\frac{d}{dt}(c^*Gc)=0.                                \tag{5.2}
\]

The moving-basis connection C is essential. Omitting it can generate apparent norm growth even when the full dynamics is unitary. A singular Gram matrix must be reduced by its null space; it must not be made invertible by an unreported regularization that changes the norm.

Define \(D=\dot B-\mathsf A B\), \(\Pi_m=BG^{-1}B^*\). The residual is

\[
r_m=\dot\Psi_m-\mathsf A\Psi_m=(I-\Pi_m)Dc,
\]

and

\[
\|r_m\|^2=c^*\left(D^*D-D^*BG^{-1}B^*D\right)c.        \tag{5.3}
\]

The matrix in parentheses is a nonnegative Gram Schur complement. All its entries are specified expectation values of the retained observables and their actual derivatives. No lower-moment closure is assumed.

If the initial state is represented exactly, variation of constants and unitarity give

\[
\boxed{\|\Psi_t-\Psi_m(t)\|\leq\int_0^t\|r_m(s)\|\,ds.} \tag{5.4}
\]

This is an analytical inequality; evaluating its right side by ordinary floating quadrature is only a diagnostic until those evaluations are enclosed. Initial approximation error adds its norm to the bound.

### 5.2 A stronger bound for the Wilson expectation

Because e belongs to the family at every time, \(\langle e,r_m(s)\rangle=0\). In the Duhamel expression for the scalar error, subtract e from \(\mathsf U(t,s)^*e\). The backward propagator satisfies

\[
\|(\mathsf U(t,s)^*-I)e\|
\leq\int_s^t\|\mathsf A_ve\|\,dv
=\int_s^t|k_v|\sqrt{g(v)}\,dv.
\]

Consequently, with \(W_m=\langle e,\Psi_m\rangle\),

\[
\boxed{|W(t)-W_m(t)|
\leq\int_0^t\left(\int_s^t |k_v|\sqrt{g(v)}\,dv\right)
\|r_m(s)\|\,ds.}                                     \tag{5.5}
\]

One may take the smaller of (5.4) and (5.5). This refinement matters: an error bound on the whole matrix state can exceed the small Wilson shape effect, while the projected bound can resolve it.

### 5.3 Explicit two-observable system

Take \(b_0=e\), \(b_1=J_t/\sqrt{g(t)}\), with g positive on the interval. Define

\[
\mu_3=\mathbb E\frac{\operatorname{tr}J^3}{N},\qquad
\mu_4=\mathbb E\frac{\operatorname{tr}J^4}{N},\qquad
d=\mathbb E\frac{\operatorname{tr}\dot J^2}{N}.
\]

The basis is orthonormal. Its connection vanishes within this two-dimensional family: J and its derivative are Hermitian and traceless, and \(\langle J,\dot J\rangle=\dot g/2\) is real. Writing \(\Psi_2=xe+yJ/\sqrt g\), (5.1) becomes

\[
\boxed{\frac{d}{dt}\binom{x}{y}
=i k\begin{pmatrix}0&\sqrt g\\\sqrt g&\mu_3/g\end{pmatrix}
\binom{x}{y},\qquad (x(0),y(0))=(1,0).}                \tag{5.6}
\]

It preserves \(|x|^2+|y|^2=1\). It is an approximation, not an exact two-moment closure.

The two orthogonal Hermitian residuals are

\[
R_D=\dot J-\frac{\dot g}{2g}J,
\qquad
R_C=J^2-ge-\frac{\mu_3}{g}J.                          \tag{5.7}
\]

Both are orthogonal to e and J. The inner product of two Hermitian matrix observables is real, so the real cross term between \(R_D\) and \(-ikR_C\) vanishes. This proves

\[
\boxed{\|r_2\|^2
=\frac{|y|^2}{g}\left[
d-\frac{\dot g^2}{4g}
k^2\left(\mu_4-g^2-\frac{\mu_3^2}{g}\right)\right].}  \tag{5.8}
\]

Each bracketed contribution is nonnegative. The derivative of the parent J is

\[
\dot J=\dot q^\mu\mathcal D_\mu+i k\mathcal R,
\]

with the full ordered commutator term \(\mathcal R\) and covariant derivatives of curvature defined in the parent note. Thus d retains the derivative sector, including the transverse terms exposed when one tries to use field equations. The fourth moment retains the curvature-product sector. No Gaussian rule, planar approximation, or large-N factorization has been used.

For SU(2), every traceless Hermitian two-by-two J has zero trace of J cubed, configuration by configuration. Thus \(\mu_3=0\) and

\[
x(t)=\cos\theta(t),\quad y(t)=i\sin\theta(t),\quad
\theta(t)=\int_0^t k_s\sqrt{g(s)}\,ds.                 \tag{5.9}
\]

Although J squared is scalar on each SU(2) configuration, its coefficient fluctuates across configurations. Therefore \(\mu_4-g^2\) generally remains nonzero. Replacing it by zero would discard actual ensemble information.

The new computational target is explicit: determine g, its derivative, d and the cubic/fourth moments, then evaluate (5.8) and (5.5). These are curvature-insertion observables on the specified chord. They remain interacting quantities, but they do not require inserting the unknown completed loop Q into every higher equation.

### 5.4 Short capacity and the existing coefficient

For the linear driver u(t)=at, the parent derivation gives

\[
k_t=-\frac{2a}{3}\sqrt t+O(t^{3/2}),\qquad
J_t=F_{12}(0)/2+O(\sqrt t).
\]

Assume the requisite regulated moments and derivative bounds, with
\(C=\mathbb E\operatorname{tr}F_{12}(0)^2/N>0\). Then \(g=C/4+O(\sqrt t)\), and in the SU(2) two-mode approximation

\[
\theta=-\frac{2a\sqrt C}{9}t^{3/2}+O(t^2),\qquad
W_2=1-\frac{2a^2C}{81}t^3+O(t^{7/2}).                  \tag{5.10}
\]

If \(\|R_D\|=O(t^{-1/2})\) and \(\|R_C\|=O(1)\), then \(|y|=O(t^{3/2})\), so \(\|r_2\|=O(t)\). Equation (5.5) yields \(|W-W_2|=O(t^{7/2})\), whereas the whole-state bound only gives O(t squared). The projection estimate therefore reproduces the order needed to resolve the previously derived leading Wilson response. It does not compute C or establish regulator-uniform bounds.

### 5.5 Sufficient moment bounds and their cost

The assumptions can be tied to the parent's smooth-field controls. Let K0 bound the operator norm of curvature and K1 the directional covariant derivative of curvature on the swept neighborhood. Unitary chord transport gives

\[
\|J\|_{\rm op}\leq K_0/2,\qquad
\|\mathcal D_{\dot q}\|_{\rm op}\leq |\dot q|K_1/3,
\qquad \|\mathcal R\|_{\rm op}\leq K_0^2/4.
\]

For the last inequality use \(\|J(r)\|\leq K_0r^2/2\), the commutator bound and \(\int_0^1r^3dr=1/4\). Consequently

\[
g\leq\tfrac14\mathbb E K_0^2,\qquad
\mu_4\leq\tfrac1{16}\mathbb E K_0^4,\qquad
d\leq\mathbb E\left(|\dot q|K_1/3+|k|K_0^2/4\right)^2. \tag{5.11}
\]

Finite \(\mathbb E K_1^2\) and \(\mathbb E K_0^4\), uniformly on a fixed regulated neighborhood, are therefore sufficient for these residual estimates. They imply the short-time orders used above when g has a positive limiting value. They are stronger than the moments used in the parent's scalar short-loop remainder. This is a real cost of controlling the state hierarchy: stronger derivative/fourth-moment bounds are required, and no uniformity as the ultraviolet regulator is removed has been established. The coarse bounds in (5.11) may be much less informative numerically than directly measuring the orthogonal residuals.

## 6. Preliminary diagnostics

The [checker](../numerics/check_positive_hierarchy.py) is self-contained apart from NumPy. Its [small record](../numerics/records/positive-hierarchy-preliminary-20260924.json) contains 64 passing controls:

- finite OS null-space and nonmonotone-storage counterexamples;
- generic SU(3) residual identities, including the nonzero cubic-moment term;
- moving Gram-metric conservation and failure when the connection is omitted;
- a nonautonomous four-state memory reconstruction and positive two-time Gram kernel;
- actual linear-driver geometry, noncommuting SU(2) prefix/chord transports and the two-observable residual bounds in a finite positive background ensemble.

For the last group, the three constant non-Abelian connections have probabilities 0.2, 0.3 and 0.5. These are chosen controls, not draws from YM. The full Wilson loop is computed by integrating the original connection along the growing trace and closing by the chord. The approximation is computed from separately evaluated transported curvature moments. Derivatives and quadratures are floating approximations.

| Driver slope a | Capacity t | Direct W | Two-mode W | Observed scalar error | Evaluated bound (5.5) |
|---:|---:|---:|---:|---:|---:|
| 0 | 0.4225 | 1 | 1 | numerical roundoff | 0 |
| 0.8 | 0.2025 | 0.9999601393 | 0.9999593917 | 7.48e-7 | 6.15e-6 |
| 0.8 | 0.4225 | 0.9996561469 | 0.9996420564 | 1.41e-5 | 8.00e-5 |
| -0.8 | 0.4225 | 0.9996537456 | 0.9996406862 | 1.31e-5 | 7.69e-5 |

For the positive-slope longer trace, the whole-state error bound is about 0.00707 and would obscure the scalar shape effect. The refined bound is about 0.000080, below the observed departure from one of about 0.000344. This is evidence that the residual can be informative in a noncommuting model. It is not evidence that the same bound will be small in the YM vacuum. The chosen ensemble is not reflection/parity invariant, so the small difference between positive and negative driver slopes does not test vacuum parity symmetry.

The unitarity/storage discrepancies are at most about 1.3e-12 in these runs. Doubling the step count passes the stated refinement checks. None of the floating upper bounds is an interval certificate; their analytical justification is (5.5), conditional on accurate evaluation and the hypotheses above.

## 7. Reflection positivity: an obstruction and a concrete repair to the setup

### 7.1 Why configuration unitarity is insufficient

Take two independent signs \(\sigma_+,\sigma_-\in\{-1,1\}\), with reflection exchanging them. For functions of the positive sign alone,

\[
\langle\Theta f\,g\rangle=\overline{\mathbb Ef}\,\mathbb Eg.
\]

This is reflection positive. The function \(f(\sigma_+)=\sigma_+\) has zero OS norm. Multiplication by \(U(\sigma_+)=i\sigma_+\) is unitary in configuration L2, but \(Uf=i\) has OS norm one. Thus even pointwise unitary multiplication need not preserve the OS null space and need not define an operator on the reconstructed physical space.

This elementary counterexample blocks an automatic identification of Section 3 with the parent's half-space reflection proposal. It is a test of that inference, not a counterexample to YM reflection positivity.

### 7.2 Put the contour on a spatial boundary slice

Choose Euclidean time perpendicular to the plane of the growing trace. All contours then lie on one spatial slice. Start with finite-volume Wilson lattice gauge theory at theta zero and a positive transfer-matrix construction. The existence of physical positivity and a positive transfer matrix in the standard lattice setting is established by [Lüscher](https://doi.org/10.1007/BF01614090) and [Osterwalder–Seiler](https://doi.org/10.1016/0003-4916(78)90039-8). Those results do not provide the differentiable Loewner interpolation or the continuum estimates proposed here.

Let \(\Omega(U)\) be a normalized gauge-invariant vacuum wavefunction on spatial links in the transfer-matrix realization. Define the slice measure \(d\nu=|\Omega|^2dU\). The map

\[
\mathcal I:X(U)\longmapsto\Omega(U)X(U)
\]

is an isometry from \(L^2(\nu;\operatorname{End}\mathbb C^N)\) into the boundary wavefunction space, with the trace-normalized color norm. A based spatial loop acts by left multiplication by Q(U), which is unitary in this space. This is a boundary operator acting on wavefunctions, not multiplication by an arbitrary positive-time history functional.

The basepoint color cannot be suppressed. Use the covariant sector

\[
\Psi(U^g)=g(b)\Psi(U)g(b)^{-1},
\]

equivalently a specified nondynamical reference fiber \(\mathbb C^N\otimes\overline{\mathbb C^N}\) at b. The initial \(\Omega I\) is its singlet; multiplying by Q can populate other components of the combined gauge-field/reference state while respecting the total gauge constraint. Tracing the vacuum matrix element returns the original closed-loop expectation. This is an explicit probe-sector enlargement, not additional dynamical matter in the YM action.

There is a simple positivity check for such a sector: if a positive kinematic transfer operator T acts on spatial-link wavefunctions, tensor it with the identity on the reference fiber and impose the gauge constraint with the orthogonal group-averaging projector \(P_G\). Then

\[
\langle\psi,P_G(T\otimes I)P_G\psi\rangle\geq0.
\]

Gauge covariance of the standard transfer construction supplies the invariant-sector interpretation. The detailed reflected network, color convention and any reference-source energy subtraction should be written out before identifying it with a particular OS correlator. The algebra above gives a definite finite-lattice candidate; this note does not claim that the earlier matter-endpoint construction or its renormalization has thereby been validated.

If only the scalar physical sector is retained, multiplication by tr(Q)/N is bounded by one but is generally not unitary. Discarding the reference/color channels would therefore discard part of the storage in (3.1).

### 7.3 Exact discrete shape evolution before smooth interpolation

For a sequence of based lattice approximations to the trace/chord contours, let \(Q_n(U)\) denote the actual loop products. The incremental multiplication

\[
\mathsf U_nX=Q_{n+1}Q_n^*X
\]

is unitary and sends \(Q_n\) to \(Q_{n+1}\). No logarithm of a plaquette or choice of a fractional link power is needed. Split \(\mathsf U_n\) into blocks relative to e and its orthogonal complement:

\[
x_{n+1}=a_nx_n+b_nz_n,\qquad
z_{n+1}=c_nx_n+d_nz_n.
\]

Eliminating z retains products of the d blocks and all previous inputs x. Resetting z after each step would create a different evolution. This exact discrete construction is the safe initial lattice task; the continuous curvature formulas are comparison targets for its smooth limit. Ordinary four-dimensional flow should not be used to claim boundary locality. Smearing that depends only on spatial links stays in the boundary algebra, although its observable and interpolation properties still need to be specified.

## 8. Which N4SYM limitations this can address

| Limitation found in N4SYM | What this proposal changes | What it does not establish |
|---|---|---|
| First two equations do not close | Keeps the complement as memory and measures finite-family leakage by a Gram residual | Efficient closure or small leakage in the interacting vacuum |
| Transverse derivative and ordered-pair terms survive field equations | Includes them in d and the fourth-moment residual; can promote their orthogonal components to new basis elements | Their vanishing or a bound from W alone |
| Scalar-coupled transport is not an ordinary unitary holonomy | Starts with ordinary pure-YM gauge transport, whose skew generator is explicit | A repair of the same N4 scalar-coupled observable |
| Extra scalar, Yukawa and fermion-current insertions | They are absent in the chosen pure-YM theory; gauge derivatives remain | A theorem deleting them in N4SYM |
| No controlled positive norm for the hierarchy | Supplies a configuration norm, an error theorem and a specific spatial transfer-matrix route | Automatic OS descent for arbitrary half-space observables |
| Cusp, tip and regulator dependence | Keeps a finite regulator, retains the moving-basis connection and states the smooth-limit obligations | Uniform continuum bounds or positivity-preserving cusp subtraction |
| Shape evolution was not a physical response channel | Makes the shape-state preparation and observation explicit | A Lorentzian input/output law or arbitrary-input passivity |
| No arithmetic delays or complete Weil-form identity | No new solution here | Any arithmetic realization or RH implication |

The reason to continue is therefore specific: nonclosure can be replaced by a controlled approximation problem, and in pure YM its first residual has a computable positive formula. The strongest open question is whether that formula remains useful under the interacting measure and regulator refinement. If it does not, the present Hilbert representation remains correct but may offer little practical compression.

## 9. Statement ledger and immediate handoff

| Statement | Evidence and scope |
|---|---|
| Configuration storage identity | Exact algebra for positive mu and unitary pure-gauge loop |
| Memory equation and Gram kernel | Proof for bounded regulated generators; unbounded extension not supplied |
| Moving-family norm conservation and residual/error bounds | Proof under the differentiability/domain and nonsingular-Gram hypotheses |
| Two-observable residual formula | Exact algebra; SU(2) and generic SU(3) finite checks |
| Short-time recovery of the parent coefficient | Conditional asymptotic deduction under regulated moment bounds |
| OS null-space counterexample | Exact finite construction |
| Boundary time-slice proposal | Explicit isometry and probe-sector positivity argument; detailed lattice/network implementation pending |
| 64 passing diagnostics | Finite matrices and selected smooth backgrounds; no YM sampling |
| Small errors in the interacting vacuum or a continuum limit | Open |
| Extension to the original N4SYM loop or arithmetic target | Open; no new matching evidence |

The immediate next task is the finite-lattice boundary construction and its first Gram/residual measurements, following the [detailed plan](YM_REFLECTION_AND_HIERARCHY_RESEARCH_PLAN_20260924.md). The decisive observable is the residual bound relative to the measured Wilson shape effect. Adding more formal equations is useful only insofar as it identifies the next state needed to reduce that error.

The cited lattice positivity and Mori precedents were checked through primary publisher records and abstracts. Their complete technical proofs were not independently audited in this session. The projection identities and finite counterexample above are derived explicitly in this note; the proposed reference-sector network and continuum extension remain separate tasks.
