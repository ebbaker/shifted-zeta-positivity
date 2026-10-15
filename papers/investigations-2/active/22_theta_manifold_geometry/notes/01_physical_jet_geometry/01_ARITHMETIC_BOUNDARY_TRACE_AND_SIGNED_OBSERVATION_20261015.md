# Arithmetic boundary traces and signed physical observation

15 October 2026, America/New_York. Prepared for Edward Baker with substantial LLM assistance. Coordinating model **gpt-6-astra**, reasoning effort **ultra**. This note proves elementary sequence and finite-dimensional statements, derives conditional consequences for physical endpoint reconstruction, and proposes a geometric research target. No theta signed-core inequality or collision exclusion is established.

The [adjoint recurrence experiment](../03_theta_bundles_and_connections/08_ADJOINT_RECURRENCE_ENDPOINT_EXPERIMENT_20261015.md) identifies a lower-boundary obstruction in the attempted arithmetic reconstruction. Here that obstruction is combined with the [manuscript's physical jet geometry](../../manuscript/theta_manifold_geometry.tex), the [complete-start cutoff requirement](../03_theta_bundles_and_connections/07_PARITY_STRIP_CUTOFF_AND_FULL_STARTING_FACTOR_20261015.md), and the [exponential-average criterion](../02_signed_turning_control/04_EXPONENTIAL_AVERAGE_AND_SHRINKING_CHORD_TARGETS_20261015.md).

## 1. A one-dimensional boundary obstruction

Let \(\mathscr S_+\) denote real rapidly decreasing sequences on \(n\ge1\), and \(\mathscr S_0\) those on \(n\ge0\). Thus every seminorm \(\sup_n(1+n)^k|r_n|\) is finite. Define

\[
(\Delta J)_n=J_{n-1}-2J_n+J_{n+1},\qquad
\mathscr N=\{J\in\mathscr S_0:J_0=J_1\}.
\]

**Boundary-trace proposition.** The map \(\Delta:\mathscr N\to\mathscr S_+\) is injective, and

\[
\operatorname{range}(\Delta|_{\mathscr N})
=\left\{r\in\mathscr S_+:\sum_{n\ge1}r_n=0\right\}.
\tag{1}
\]

Consequently its algebraic cokernel is one-dimensional, detected by total sum.

**Proof.** Telescoping and rapid decrease give

\[
\sum_{n\ge1}\Delta J_n=J_0-J_1.
\]

Conversely, for any \(r\in\mathscr S_+\), the current

\[
J_n=\sum_{m>n}(m-n)r_m
\tag{2}
\]

is rapidly decreasing, satisfies \(\Delta J=r\), and has
\(J_0-J_1=\sum r_n\). Rapid decrease follows by bounding the tail with an arbitrarily high weighted seminorm of \(r\). A homogeneous solution of \(\Delta J=0\) is affine in \(n\); the only rapidly decreasing such solution is zero. This proves all assertions. \(\square\)

For the complete primitive endpoint sequence

\[
\beta_n=(4\pi n^2-1)e^{-\pi n^2},\qquad
\sum_{n\ge1}\beta_n=\tfrac12,
\]

the class of \(\beta\) spans this cokernel. Every \(r\) has a unique decomposition

\[
r=\Delta J+\eta\beta,\qquad J\in\mathscr N,
\qquad \eta=2\sum_{n\ge1}r_n.
\tag{3}
\]

Choosing \(\eta\) by this formula uses the unknown physical residual itself. A useful arithmetic construction must supply its boundary cancellation or estimate independently. The complete endpoint value \(1/2\) must not replace a finite partial sum without its tail.

These statements concern rapidly decreasing sequences. Parameter-dependent applications require locally uniform weighted bounds for the claimed uniform estimates and exchanges. Formula (1) explains why unrestricted recurrence inversion merely relocates the physical residual to a lower boundary; it does not improve that residual.

## 2. The physical observation quotient

Let \(V\) be a finite-dimensional real inner-product space representing a **homogeneous linear relaxation** of arithmetic and stationarity constraints. Let

\[
\mathsf J:V\longrightarrow\mathbb R^2,
\qquad \ell:V\longrightarrow\mathbb R
\]

be respectively its physical first-jet observation and endpoint functional.

**Quotient-norm proposition.** A finite constant \(C\) satisfying

\[
|\ell(c)|\le C\|\mathsf Jc\|\quad(c\in V)
\tag{4}
\]

exists exactly when \(\ker\mathsf J\subseteq\ker\ell\). In orthonormal coordinates its least value is

\[
C_{\min}=\|\ell\mathsf J^\dagger\|,
\tag{5}
\]

where \(\mathsf J^\dagger\) is the Moore–Penrose inverse.

**Proof.** Necessity follows by testing kernel vectors. Under kernel inclusion, \(b(\mathsf Jc)=\ell(c)\) defines a well-defined covector on \(\operatorname{im}\mathsf J\). Its operator norm is the least constant in (4). The row \(\ell\mathsf J^\dagger\) represents this covector and vanishes on the orthogonal complement of the image. \(\square\)

Thus the endpoint must descend to the quotient \(V/\ker\mathsf J\), measured with the physical observation norm. For affine normalization constraints, the direction space and the retained basepoint contribution require separate treatment; (4) alone is not an affine criterion. Nor does this proposition assert that actual theta coefficients range over every vector in a chosen relaxation.

Pointwise descent is weaker than local boundedness through degeneration. Consider

\[
\mathsf J(\tau)=\operatorname{diag}(1,\tau^2),
\qquad \ell(\tau)=(0,\tau).
\]

Kernel inclusion holds for every \(\tau\), including zero, but
\(C_{\min}=|\tau|^{-1}\) for \(\tau\ne0\). This analytic matrix example is not a theta heat field. It shows that a successful rank test needs a subsequent singular-value or vanishing-order estimate. Computing a pseudoinverse does not establish the required boundedness.

## 3. Reconstruction coefficients at a hypothetical collision

Return to the complete physical field. Write

\[
F=(H,H_x),\qquad \rho=\|F\|=\sqrt E,
\qquad W=h_j,\qquad S=h_{j+1},\quad j=0,1.
\]

Suppose an endpoint observation \(V\) has a reconstruction

\[
V=AH+BH_x+CS+R,\qquad |R|\le\varepsilon.
\tag{6}
\]

On full stationarity \(S=0\) with \(\rho>0\), Cauchy–Schwarz gives the necessary pointwise bound

\[
\boxed{\|(A,B)\|\ge
\frac{(|V|-\varepsilon)_+}{\rho}.}
\tag{7}
\]

At a multiplicity \(2r+j\) event, the manuscript proves that its full stationary predecessor has \(\rho(T-s,\chi(s))\sim c s^r\), with \(c>0\). For every sufficiently small fixed positive \(\delta\), the complete endpoint limit \(W(T,a+\delta)\) is nonzero. Choosing a sufficiently accurate fixed endpoint cutoff preserves that nonzero limit. If the fixed residual allowance in (6) is smaller than half its magnitude, (7) forces coefficient growth at least a positive constant times \(s^{-r}\).

An independently proved bounded reconstruction would therefore exclude the event. Formula (7) diagnoses why division-based reconstructions cannot establish that conclusion by themselves. The order of choices matters: fix the spatial length and a sufficiently accurate cutoff before taking the collision limit.

This obstruction survives bounded nonsingular changes of physical first-jet frame. If \(F'=GF\), with \(G\) and \(G^{-1}\) locally bounded, the physical norms and corresponding dual coefficient norms remain comparable. A singular frame can hide the displayed growth only by transferring it to the comparison with physical energy. This concerns changes of first-jet frame; it does not rule out every auxiliary geometric method.

## 4. Orientation and radial order are both needed

For \(\rho>0\), put \(\theta=F/\rho\). Let \(e_j\) be the coordinate vector selecting \(H\) or \(H_x\), so \(W/\rho=e_j\cdot\theta\). For fixed \(\delta>0\), set \(\alpha=e^{-\delta}\) and

\[
A=W^2-\alpha WV.
\]

Then

\[
\frac{A}{E}=(e_j\cdot\theta)^2
-\alpha\frac{(e_j\cdot\theta)V}{\rho}.
\tag{8}
\]

Since \(0\le(e_j\cdot\theta)^2\le1\), existence of a locally bounded nonnegative \(K\) with \(A\ge-KE\) is equivalent to local boundedness of

\[
\boxed{\frac{[(e_j\cdot\theta)V]_+}{\rho}
=\frac{[WV]_+}{E}.}
\tag{9}
\]

This signed condition can demand substantially less than absolute endpoint reconstruction. A large endpoint opposite in sign to \(W\) is harmless. On branch zero, full stationarity gives \(E=W^2\), making the distinction explicit.

At a covered collision, \(\theta\to\operatorname{sgn}(a_0)e_j\), while a sufficiently close fixed complete endpoint has sign \(a_0\). Thus (9) has a positive pairing divided by a vanishing radius. More generally, even a pairing tending to zero must vanish at least as rapidly as \(\rho\) on its positive side. The example in section 2 shows why limiting direction or pointwise kernel inclusion does not settle this radial order.

The manuscript already explains that curvature squares lose the physical sign and that the marked real Gauss map retains orientation. The additional distinction here is between oriented direction and **relative radial order**, together with an exact quotient norm for the stronger reconstruction problem. Equation (9) is an equivalent target, not an independent sign theorem.

## 5. A geometric question for the arithmetic current

Suppose the recurrence experiment produces, with all endpoints retained,

\[
V=AH+BH_x+CS+B_{\partial}+R,
\qquad B_{\partial}=J_0-J_1+\eta/2,
\qquad |R|\le\varepsilon.
\tag{10}
\]

Upper-cutoff corrections must be included in \(B_{\partial}\) or in the justified error. Instead of forcing the boundary trace to be small absolutely, seek the source-prescribed estimate

\[
\boxed{\frac{W}{\rho}B_{\partial}
\le C_0\rho+\varepsilon_0}
\qquad(S=0,\ \rho>0).
\tag{11}
\]

For locally bounded \(A,B,C_0\), multiplication by \(\rho\), (10), and \(|W|\le\rho\) give

\[
WV\le(|A|+|B|+C_0)E
+(\varepsilon+\varepsilon_0)\sqrt E.
\tag{12}
\]

This supplies the mixed-error chord target when the error tends to zero with the prescribed cutoff and spatial-scale conditions. Large boundary traces paired oppositely to the normalized starting jet need no absolute payment. Both stationary branches, complete starting factors, and the declared neighborhood coverage remain necessary.

The proposed geometric task is therefore to prove an **oriented estimate for the complete arithmetic boundary trace**, with the correct radial order. The recurrence identifies the boundary class; the physical jet determines its signed observation. Their interaction, rather than an additional metric or calibration, is the possible source of a new result.

Earlier complete-source identities already retained divergence terms and lower endpoints, and the manuscript already retained physical orientation. The genuinely additional tools here are the exact sequence-space cokernel, the sharp finite-dimensional quotient norm and its degeneration test, and the weaker signed boundary target (11). They clarify what a successful arithmetic mechanism must control. None supplies that mechanism: a further change of representation without an independently proved trace estimate remains a reformulation.
