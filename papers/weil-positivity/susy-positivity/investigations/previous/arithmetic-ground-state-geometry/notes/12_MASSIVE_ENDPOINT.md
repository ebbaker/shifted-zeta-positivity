# The separated-vacuum endpoint with fixed polynomial sources

13 September 2026. This note derives the positive-real limit \(c\downarrow0\) of the interacting physical metric. It keeps all nine physical vacua and the raw holomorphic volume normalization of notes 06–09. A local construction of closed forms and a duality estimate suffice; no numerical shooting, unproved spectral localization formula, or continuity to the rank-one Gaussian problem is used.

The conclusion in the orbit-idempotent frame is
\[
\boxed{\quad
g_{\mathrm{orb}}(c,c)\longrightarrow
4\pi^2\operatorname{diag}(16,64,48)
\quad(c\downarrow0).
\quad}
\]
In particular the identity-volume norm tends to \(512\pi^2\). The raw identity-volume norm of the different theory obtained by setting \(c=0\) first is \(64\pi^2\). The escaping vacua account for the difference.

## 1. The parameter rescaling retains every source

The physical differential and Euclidean metric conventions are
\[
D_c=\bar\partial+\partial f_c\wedge,
\qquad
f_c(A,B)=\frac{A^2+B^2}{8}
 +\frac{c(A^4+B^4+A^2B^2)}{16},
\]
\[
ds^2=d(\Re A)^2+d(\Im A)^2+d(\Re B)^2+d(\Im B)^2.
\]
Thus \(\|dz\|^2=2\) and the measure is the ordinary real Lebesgue measure. Write \(\rho=1/c>0\), \(Z=\sqrt c\,A\), \(W=\sqrt c\,B\), and
\[
F(Z,W)=f_1(Z,W),\qquad
f_c=\phi_c^*(\rho F).
\]
The nine critical points of \(F\) stay fixed. In the reference coordinates put
\[
\Omega_Z=dZ\wedge dW,\qquad
S=Z^2+W^2,\qquad T=Z^2W^2.
\]
The original frame \(E=(1,cs,c^2t)\Omega_{A,B}\) becomes
\[
E=\rho\,\phi_c^*\bigl((1,S,T)\Omega_Z\bigr).
\]
Middle-degree pullback is an \(L^2\) isometry under this constant conformal dilation. Consequently
\[
g_E(c,c)=\rho^2 g_{\mathrm{ref}}(\rho),
\tag{1}
\]
where the reference sources are fixed polynomial volume classes for \(D_{\rho F}\).

The finite-dimensional harmonic/Jacobi identification used below follows from the Hodge decomposition and comparison theorem of [Li–Wen, *On the L2-Hodge theory of Landau-Ginzburg models*](https://arxiv.org/html/1903.02713), especially Theorem 2.34 and the Hodge statements in Section 2.3. Their assumptions hold here: the flat target is complete with bounded geometry, the critical set is finite, \(|\nabla F|\ge aR^3-bR\), and \(|\nabla^kF|=O(1+R^{4-k})\) for \(2\le k\le4\), with higher derivatives zero. These bounds verify strong ellipticity for each \(\rho>0\). The Jacobi quotient is the nine-dimensional semisimple algebra already computed in note 06. No uniform spectral-gap theorem as \(\rho\to\infty\) is required for the argument below.

## 2. The exact Gaussian representative includes its cohomology normalization

Consider one complex coordinate with \(f(z)=az^2/2\), \(a\ne0\). Set \(\kappa=\bar a/|a|\). Direct substitution into \(D_f\) and its Euclidean adjoint gives the harmonic one-form
\[
\gamma_a=e^{-|a||z|^2}(dz-\kappa\,d\bar z).
\tag{2}
\]
Its class is exactly \([dz]\) in the smooth twisted complex. Indeed the smooth function
\[
b_a=-\frac{1-e^{-|a||z|^2}}{az}
\]
extends across zero and satisfies
\[
D_fb_a=\gamma_a-dz.
\tag{3}
\]
The primitive in (3) is used in smooth cohomology; no assertion that \(dz\) or \(b_a\) is an \(L^2\) vector is needed. The comparison theorem identifies this smooth class with its harmonic representative.

The ordinary exterior norm is
\[
\|\gamma_a\|^2
=4\int_{\mathbb C}e^{-2|a||z|^2}\,dx\,dy
=\frac{2\pi}{|a|}.
\tag{4}
\]
For two independent coordinates, the wedge product of (2) represents the product volume class, and its squared norm is
\[
\frac{(2\pi)^2}{|a_1a_2|}.
\tag{5}
\]
This fixes a source factor that can be lost by normalizing a real one-form instead. For positive \(a\), (2) equals \(2i e^{-a|z|^2}dy\). The real form \(e^{-a|z|^2}dy\) therefore represents \(dz/(2i)\), rather than \(dz\).

For later use the opposite-twist Gaussian has the same norm and is
\[
\gamma_{-a}=e^{-|a||z|^2}(dz+\kappa\,d\bar z).
\]
With the complex orientation \(dx\wedge dy\),
\[
\int_{\mathbb C}\gamma_a\wedge\gamma_{-a}
=-\frac{2\pi i}{a}.
\tag{6}
\]
For two coordinates, reordering the two middle one-forms contributes one additional minus sign. Thus
\[
\int_{\mathbb C^2}
(\gamma_{a_1}\wedge\gamma_{a_2})
\wedge(\gamma_{-a_1}\wedge\gamma_{-a_2})
=\frac{4\pi^2}{a_1a_2}.
\tag{7}
\]

## 3. Local closed representatives at all nine critical points

Let \(v\) be a critical point of \(F\), with invertible complex symmetric Hessian \(H_v\). Choose a unitary matrix \(Q_v\) giving the Takagi diagonalization
\[
Q_v^T H_vQ_v=\operatorname{diag}(\sigma_{v1},\sigma_{v2}),
\qquad \sigma_{vj}>0.
\]
There are local holomorphic coordinates \(\zeta\) with
\[
(Z,W)=v+Q_v\zeta+O(|\zeta|^2),
\qquad
F=F(v)+\frac12\sum_{j=1}^2\sigma_{vj}\zeta_j^2.
\tag{8}
\]
One can obtain the needed version of the holomorphic Morse change directly. After the unitary linear change write the Taylor expansion as \(F-F(v)=w^T A(w)w/2\), where \(A\) is holomorphic and symmetric and \(A(0)=D=\operatorname{diag}(\sigma_{v1},\sigma_{v2})\). Near zero the convergent power series for \((D^{-1/2}A(w)D^{-1/2})^{1/2}\) is symmetric and has value \(I\). Taking
\[
\zeta=D^{-1/2}
 (D^{-1/2}A(w)D^{-1/2})^{1/2}D^{1/2}w
\]
gives (8), with derivative \(I\) in the \(w\) coordinates; the holomorphic inverse function theorem supplies its inverse.

Let \(e_v\) be the primitive Jacobi idempotent, whose value is one at \(v\) and zero at the other critical points. In the coordinates (8) its volume class has local coefficient
\[
k_v=\det Q_v.
\]
Indeed \(e_v(Z(\zeta))\det(\partial Z/\partial\zeta)\) has value \(k_v\) at zero, and its remaining Taylor terms are in the ideal \((\zeta_1,\zeta_2)\). Dividing those terms by the nonzero factors \(\rho\sigma_{vj}\) gives local holomorphic Koszul primitives. Therefore its local class is exactly \([k_v\,d\zeta_1\wedge d\zeta_2]\).

Take the product Gaussian (2) with \(a_j=\rho\sigma_{vj}\), multiply it by \(k_v\), and pull it to this neighborhood. Denote the resulting closed local form by \(a^+_{v,\rho}\). Its opposite-twist counterpart is \(a^-_{v,\rho}\). Equations (3) and (8) show that these have the prescribed local source class; the constant critical value does not enter either differential.

Choose disjoint coordinate neighborhoods and a smooth cutoff \(\chi_v\) supported in each, equal to one near its critical point. A closed compact representative is obtained by the following local contraction, which also makes the cutoff correction explicit. Away from the critical point put
\[
V=\frac{(\partial(\rho F)\wedge)^\dagger}
 {|\partial(\rho F)|^2},
\qquad
S=[\bar\partial,V],
\qquad
T_{\chi_v}=\chi_v+(\bar\partial\chi_v)V(1+S)^{-1}.
\tag{9}
\]
An auxiliary flat metric in the \(\zeta\) chart may be used in (9); it need not be the physical metric. The identities \([\partial(\rho F)\wedge,V]=1\) and the finite bidegree expansion of \((1+S)^{-1}\) verify that \(T_{\chi_v}\) takes closed forms to closed forms and preserves their local class. This is the cutoff homotopy used in Li–Wen's comparison proof. The result vanishes near the chart boundary, so its extension by zero is a globally smooth compactly supported closed form.

Write these representatives as \(u^\pm_{v,\rho}=T_{\chi_v}a^\pm_{v,\rho}\). They represent \([e_v\Omega_Z]\) for the two twists. On the cutoff annulus, \(V=O(\rho^{-1})\) and \(S=O(\rho^{-1})\); both are algebraic operators on forms. The Gaussian there is exponentially small. Consequently the cutoff correction has exponentially small norm up to fixed polynomial factors in \(\rho\).

The physical metric in (8) equals the Euclidean metric at zero and differs by \(O(|\zeta|)\). Rescaling \(\zeta=\rho^{-1/2}\xi\) in the Gaussian norm therefore proves
\[
N^\pm_{v,\rho}:=\|u^\pm_{v,\rho}\|^2
=\frac{4\pi^2}{\rho^2|\det H_v|}
 \bigl(1+O(\rho^{-1/2})\bigr).
\tag{10}
\]
Here \(|k_v|=1\) and \(\sigma_{v1}\sigma_{v2}=|\det H_v|\). The constants are uniform over the finite set of nine points. The two representatives can be chosen as images under the unitary degree operation \(U_\pi|_{(p,q)}=(-1)^p\), so their norms are equal, although equality is unnecessary for the estimate. Distinct \(v\) have disjoint supports and hence exactly zero mutual inner product before harmonic projection.

## 4. A duality estimate gives the matching lower bound

For closed rapidly decreasing or compact forms of opposite twist, the bilinear pairing
\[
K(\alpha,\beta)=\int_{\mathbb C^2}\alpha\wedge\beta
\tag{11}
\]
depends only on their twisted cohomology classes. Stokes' theorem verifies this: the two wedge terms involving \(\partial(\rho F)\) cancel. The extension to harmonic representatives is the Poincaré pairing of Li–Wen, Section 2.7. It obeys
\[
|K(\alpha,\beta)|\le\|\alpha\|\,\|\beta\|,
\tag{12}
\]
because the Hodge-star conjugation is an isometry.

For the primitive classes, (7), (8), and invariance under the compact cutoff homotopy give the exact pairing
\[
K(e_v\Omega_Z,e_w\Omega_Z)
=\delta_{vw}\,k_{v,\rho},
\qquad
k_{v,\rho}=\frac{4\pi^2}{\rho^2\det H_v}.
\tag{13}
\]
In this formula the first class uses \(+\rho F\) and the second \(-\rho F\). In deriving (13), the local holomorphic volume contributes \(k_v^2\), and
\[
\frac{k_v^2}{\sigma_{v1}\sigma_{v2}}=\frac1{\det H_v}.
\]
The integral can be evaluated in the quadratic chart with compact cutoffs; the cutoff homotopy then equates it to the full quadratic Gaussian integral. Thus (13) fixes the factor \(4\pi^2\) without making a norm-to-residue assumption.

Let \(G_\rho^+\) be the physical Gram matrix in the full nine-primitive source frame. Harmonic projection minimizes the norm in each \(L^2\) class. Projection of the disjoint representatives above gives
\[
G_\rho^+\le\operatorname{diag}(N^+_{v,\rho})
\tag{14}
\]
as Hermitian forms. For a coefficient vector \(z=(z_v)\), choose an opposite-twist source with coefficients
\[
w_v=\frac{\overline{z_v k_{v,\rho}}}{N^-_{v,\rho}}.
\]
Its squared physical norm is at most
\[
A=\sum_v\frac{|z_v|^2|k_{v,\rho}|^2}{N^-_{v,\rho}},
\]
by its disjoint compact representatives. Its pairing with the original source is exactly \(A\). Applying (12) gives \(A^2\le (z^\dagger G_\rho^+z)A\), and hence
\[
\operatorname{diag}\left(
 \frac{|k_{v,\rho}|^2}{N^-_{v,\rho}}\right)
\le G_\rho^+
\le\operatorname{diag}(N^+_{v,\rho}).
\tag{15}
\]
Both diagonal bounds have the same leading term by (10) and (13). Therefore
\[
\boxed{\quad
\rho^2G_\rho^+
=4\pi^2\operatorname{diag}\left(\frac1{|\det H_v|}\right)
 +O(\rho^{-1/2}).
\quad}
\tag{16}
\]
The error here is a finite-dimensional matrix estimate. It asserts no derivative expansion and no Stokes or uniqueness data. In particular the proof does not need to identify approximate local Gaussian eigenvectors with exact eigenvectors individually: the cohomology and duality bounds select the correct source amplitudes.

## 5. The orbit weights and the original frame

For \(F=f_1\), the critical-point data are

| Orbit | Cardinality | Critical coordinates | \(\det H_v\) | Sum of inverse absolute Hessians |
|---|---:|---|---:|---:|
| Origin | 1 | \((0,0)\) | \(1/16\) | \(16\) |
| Axis | 4 | One coordinate zero, the other squared \(-1\) | \(-1/16\) | \(64\) |
| Both nonzero | 4 | \(Z^2=W^2=-2/3\) | \(1/12\) | \(48\) |

The orbit idempotents in the original frame are
\[
e_0=1+r+\tfrac34v,\qquad
e_a=-r-3v,\qquad
e_b=\tfrac94v,
\qquad r=cs,\quad v=c^2t.
\]
They are sums of the primitive idempotents. Summing (16) over the orbits and applying (1) gives
\[
\boxed{
g_{\mathrm{orb}}(c,c)
=4\pi^2\operatorname{diag}(16,64,48)+O(c^{1/2}).
}
\tag{17}
\]
No division by the order-eight symmetry group occurs. The two multiplicities four are part of the physical source norms.

Evaluation of the original sources on the three orbits gives
\[
V=\begin{pmatrix}
1&0&0\\
1&-1&0\\
1&-4/3&4/9
\end{pmatrix},
\qquad
g_E=V^Tg_{\mathrm{orb}}V.
\]
Thus the full endpoint matrix is
\[
\boxed{
g_E(c,c)=4\pi^2
\begin{pmatrix}
128&-128&64/3\\
-128&448/3&-256/9\\
64/3&-256/9&256/27
\end{pmatrix}
+O(c^{1/2}).
}
\tag{18}
\]
The identity is the sum of all three orbit sources, so
\[
H(c,c)=512\pi^2+O(c^{1/2}).
\tag{19}
\]
For comparison, setting \(c=0\) first leaves \(f_0=(A^2+B^2)/8\), whose two Hessian eigenvalues are \(1/4\). Equation (5) gives \(\|[\Omega]\|_{c=0}^2=64\pi^2\). The origin contribution in (19) is precisely this value; the two escaping orbits contribute \(256\pi^2\) and \(192\pi^2\). A source normalization making the rank-one Gaussian identity norm one would make the limit in (19) equal to eight.

## 6. What is now fixed, and what remains open

Equation (13) also calibrates the raw physical topological pairing as \(\eta_{\mathrm{phys}}=4\pi^2\eta\) in the residue convention of note 06. Equivalently the universal modulus in its reality condition is \(|\nu|=4\pi^2\); the displayed opposite-twist orientation fixes \(\nu=+4\pi^2\). The reflected-boundary construction and its physical antiunitary are developed in note 10. This calibration comes from the specified exterior Hilbert norm and the exact cohomology normalization, rather than choosing a residue-normalized metric by convention.

At the pure-quartic endpoint, combining this calibration with the diagonal limiting metric already derived in notes 06–07 gives
\[
a_2=\frac{256\pi^2}{3},\qquad
a_0a_4=\left(\frac{256\pi^2}{3}\right)^2.
\]
The remaining positive constant \(a_0\), equivalently \(a_4\), has not been evaluated here. The massive limit (17) supplies the previously missing other endpoint, but two endpoint limits do not by themselves prove global existence or uniqueness of the radial matrix equation. The actual polynomial Hilbert model gives existence of its physical metric; uniqueness among abstract radial solutions, sharper corrections, and its Stokes data require further arguments. The immediately subsequent [note 13](13_RADIAL_METRIC_SELECTION.md) supplies the uniqueness argument under the inherited exact chiral equation, without evaluating the remaining constant or Stokes data.

This result also does not identify the real-cycle period with a physical boundary covector or with a norm. It determines a physically normalized metric endpoint for the fixed polynomial sources. Constructing the arithmetic preparation map and the full unbounded source domain remains separate work.

## Verification scope

The proof uses the cited strongly elliptic Hodge/comparison framework, direct Gaussian differential and cohomology identities, a local holomorphic quadratic coordinate construction, the explicit cutoff homotopy, and the Hilbert-space duality estimate (15). The Hessian weights and frame conversion are exact algebra. No additional semiclassical localization theorem is imported, and no numerical metric solution or positivity sampling is used.
