# A reflected physical boundary pairing and its absolute normalization

13 September 2026. This note constructs boundary caps for the interacting polynomial quantum mechanics. The source, adjoint and positive Hilbert product are fixed first. Opposite-superpotential gluing then gives explicit covectors on the physical three-state sector. Their Riesz vectors are obtained by a physical antiunitary reflection, rather than by fitting a period vector to an unknown metric.

The resulting covector matrix is \(4\pi^2\eta_E\), with the raw volume sources of notes 06–09. Its positive boundary Gram matrix is \(g_E^T\). This characterizes a physical Gram matrix without evaluating all its entries. At the homogeneous quartic endpoint it does evaluate the middle-source norm exactly, and fixes the product of the two other norms. A normalized non-Gaussian Euler-metric control follows. These are finite-vacuum constructions; the complete Weil pairing remains open.

## 1. Hilbert space, physical adjoint and cap preparation

Write \(z_1=A,z_2=B\), \(\Omega=dz_1\wedge dz_2\), and retain
\[
f=f_c=\frac{A^2+B^2}{8}
+\frac{c}{16}(A^4+B^4+A^2B^2),\qquad c\ne0.
\]
Use the ordinary Euclidean metric \(dx_1^2+dy_1^2+dx_2^2+dy_2^2\), orientation \(dx_1\wedge dy_1\wedge dx_2\wedge dy_2\), and the first-antilinear inner product
\[
\langle\alpha,\beta\rangle
=\int_{\mathbb C^2}\overline\alpha\wedge *\beta.
\]
Thus \(\|dz_j\|^2=2\). There is no division by the finite symmetry group's order. The differential and its Hilbert adjoint are
\[
D_f=\bar\partial+df\wedge,\qquad
D_f^\dagger=\bar\partial^\dagger+(df\wedge)^\dagger.
\]
For example, on compactly supported smooth forms,
\[
D_f^\dagger
=2\sum_{j=1}^2\left(
-\iota_{\partial/\partial\bar z_j}\partial_{z_j}
+\overline{\partial_{z_j}f}\,\iota_{\partial/\partial z_j}\right).
\]
The positive closed Hamiltonian is \(H_f=2\{D_f,D_f^\dagger\}\). The confining estimates and Hodge comparison used in notes 06–07 apply to both \(f\) and \(-f\). They give a nine-dimensional harmonic space \(\mathscr V_f\), in total form degree two, identified with the Jacobi volume classes. All uses of the Hodge theorem below are within this strongly elliptic polynomial setting.

Here is an explicit boundary wavefunction for any polynomial insertion \(p\Omega\). Choose a smooth compact cutoff \(\chi=1\) on a neighborhood of all critical points. Away from those points put
\[
V_f=\frac{(df\wedge)^\dagger}{|df|^2},\qquad
N_f=[\bar\partial,V_f],\qquad
\mathcal R_f=V_f(1+N_f)^{-1}.
\]
The inverse is the finite bidegree series; \(N_f\) lowers holomorphic degree and raises antiholomorphic degree. The graded identity is \([D_f,\mathcal R_f]=1\) off the critical set. Consequently
\[
T_{\chi,f}=1-[D_f,(1-\chi)\mathcal R_f]
=\chi+(\bar\partial\chi)\wedge\mathcal R_f,
\qquad [D_f,T_{\chi,f}]=0.
\]
All appearances of the apparent singularity of \(\mathcal R_f\) are multiplied by functions supported away from the critical set. Define
\[
u_{p,f}=T_{\chi,f}(p\Omega),\qquad
S_{t,f}p=e^{-tH_f}u_{p,f},\qquad t\ge0.
\]
The cap \(u_{p,f}\) is smooth, compactly supported, \(D_f\)-closed, and specified without a harmonic metric or a period. Evolution through a Euclidean half-cylinder prepares
\[
h_f(p)=\lim_{t\to\infty}S_{t,f}p=P_fu_{p,f}.
\]
The convergence is in \(L^2\), and exponential for fixed \(f\), since zero is separated from the positive discrete spectrum. Gluing two such cylinders uses the already specified Hilbert adjoint:
\[
\langle S_{t,f}p,S_{s,f}q\rangle
=\langle u_{p,f},e^{-(t+s)H_f}u_{q,f}\rangle.
\]
This is a positive Gram pairing before taking any limit.

The cutoff construction is the explicit homotopy in [Li–Wen, *On the L2-Hodge theory of Landau–Ginzburg models*](https://arxiv.org/html/1903.02713), Section 2.6. Their comparison theorem and the polynomial estimates justify replacing compact representatives by harmonic ones. The cap/gluing specification and the calculations below are deductions for this particular model.

### Descent to physical Jacobi states is proved at the chain level

If \(p\Omega=df\wedge\gamma\) for a holomorphic polynomial one-form \(\gamma\), then
\[
u_{p,f}=D_f(T_{\chi,f}\gamma),\qquad P_fu_{p,f}=0.
\]
Thus \(h_f\) factors through the Jacobi quotient. Conversely the comparison theorem makes the induced map an isomorphism. Changing the cutoff changes the cap by a compactly supported exact form, so it does not change \(h_f(p)\). This proves the correspondence that a bare polynomial exponential integral does not supply.

Choose \(\chi\) invariant under the coordinate sign changes and interchange. The homotopy, evolution and projection then respect that symmetry. For
\[
E=(1,r,v)\Omega,\qquad r=c(A^2+B^2),\quad v=c^2A^2B^2,
\]
the construction lands exactly in the three-dimensional determinant-character sector. At finite cylinder length exact states can still be present; the infinite-cylinder limit selects its three physical vacua.

For comparison, descent actually fails for the raw exponential insertion rule, even within invariant polynomials. The polynomial
\[
z_c=A\partial_Af_c+B\partial_Bf_c
=\frac{s+cq_4}{4}
\]
is zero in the Jacobi quotient. Yet integration by parts on the convergent real plane gives
\[
\frac1{2\pi}\int_{\mathbb R^2}z_c e^{-G_c}\,dA\,dB
=\frac12 C_{\rm per}(c)>0\qquad(c>0).
\]
Indeed the integral of the divergence of \((A,B)e^{-G_c}\) vanishes and \(G_c=4f_c\). Choosing values only on a preferred polynomial basis would define an additional lift; it would not establish descent of this insertion rule. A different boundary cohomology or a derived lift to a twisted de Rham complex remains possible.

## 2. Opposite twist and the reflected physical bra

Let \(U\alpha^{p,q}=(-1)^p\alpha^{p,q}\). It is a unitary fermion operation satisfying
\[
UD_fU^{-1}=D_{-f},\qquad UH_fU^{-1}=H_{-f}.
\]
On a holomorphic two-form \(U=1\), so uniqueness of harmonic representatives gives
\[
h_{-f}(p)=Uh_f(p).
\]
Let \(K\alpha=\bar\alpha\), and put \(C=*K\). The twisted Hodge identities send \(C:\mathscr V_{-f}\to\mathscr V_f\) antiunitarily. On total degree two, \(C^2=1\) and \(CU=UC\). Hence
\[
\Theta=CU:\mathscr V_f\longrightarrow\mathscr V_f,
\qquad \Theta^2=1,
\]
is an independently specified antiunitary reflection. The Hodge identities are given explicitly in [Li–Wen, Section 2.3](https://arxiv.org/html/1903.02713#S2.SS3); here the degree and Euclidean orientation fix their signs.

Prepare the opposite-twist cap with the same polynomial \(p\), and reflect it at the gluing surface. Its physical ket is
\[
b_p=C h_{-f}(p)=\Theta h_f(p).
\]
Its bra is the ordinary Hilbert adjoint. The induced functional on an incoming source \(q\) is
\[
\boxed{\quad
\ell_p(q)=\langle b_p,h_f(q)\rangle
=\int_{\mathbb C^2}h_f(q)\wedge h_{-f}(p).
\quad}
\]
This expression is bilinear in the polynomial labels \(p,q\); \(b_p\) is antilinear in \(p\). It is not itself a positive quadratic form. Positivity belongs to the Gram matrix of the reflected kets and to ordinary Hilbert gluing.

The opposite signs are essential for descent. For a degree-\(k\) form \(a\), integration by parts gives
\[
\int D_fa\wedge b
=(-1)^{k+1}\int a\wedge D_{-f}b.
\]
The compact caps have no boundary terms; the harmonic and exact replacements have the decay supplied by the Hodge complex. The functional can therefore be evaluated using compact representatives in disjoint neighborhoods of the critical points. This is also why reflection can be implemented before the long-cylinder limit: exact changes to either closed cap do not change this bilinear amplitude. It supplies a concrete opposite-twist defect, rather than an asserted correspondence between a contour and a vacuum.

## 3. Absolute residue normalization from one local Gaussian

Fix the algebraic residue convention
\[
\operatorname{Res}_f(pq)
=\frac1{(2\pi i)^2}\int
\frac{pq\,dz_1\wedge dz_2}{f_{z_1}f_{z_2}}
=\sum_{df(a)=0}\frac{p(a)q(a)}{\det\operatorname{Hess}f(a)}
\]
when the critical points are simple. Localization of the compact pairing gives this residue times a universal constant. That constant must be computed in the physical measure.

For one coordinate and \(f=az^2/2\), \(a\ne0\), the exact raw-\(dz\) harmonic representatives for the two twists are
\[
\alpha_\pm=e^{-|a||z|^2}
\left(dz\mp\frac{\bar a}{|a|}d\bar z\right).
\]
They represent the class \(dz\), with no source rescaling. For example,
\[
\alpha_+-dz
=D_f\left[\frac{e^{-|a||z|^2}-1}{az}\right],
\]
whose bracket is smooth also at zero. Direct integration gives
\[
\|\alpha_\pm\|^2=\frac{2\pi}{|a|},\qquad
\int_{\mathbb C}\alpha_+\wedge\alpha_-=-\frac{2\pi i}{a}.
\]
One can obtain the second identity entirely from compact representatives: for a radial cutoff \(\rho=1\) near zero, use
\[
\rho\,dz+\frac{\bar\partial\rho}{az},\qquad
\rho\,dz-\frac{\bar\partial\rho}{az}.
\]
Their pairing is \(-2\pi i/a\). Thus neither normalization nor descent is being inferred from a Gaussian approximation.

In two coordinates, moving the middle degree-one factors past each other contributes a minus sign. The product Gaussian therefore gives
\[
-\left(-\frac{2\pi i}{a}\right)
\left(-\frac{2\pi i}{b}\right)
=\frac{4\pi^2}{ab}.
\]
Holomorphic Morse coordinates, cohomological localization, and the squared volume Jacobian give the same factor at each simple critical point of the quartic. It follows that
\[
\boxed{\quad \ell_p(q)=\nu\operatorname{Res}_f(pq),\qquad
\nu=4\pi^2.\quad}
\]
The nondegenerate cohomological pairing is the one in [Li–Wen, Section 2.7](https://arxiv.org/html/1903.02713#S2.SS7). The explicit local calculation here calibrates it against the \((2\pi i)^{-2}\) residue convention. At the isolated homogeneous critical point, the same calibration follows by continuity of compact representatives and the source metric, as proved for this family in notes 06–07.

The oscillator frame used earlier in note 01 contains an explicit factor \(1/(2i\sqrt{2\pi})\) per holomorphic coordinate. It is not the raw polynomial-volume frame used here. The different constants are consistent; no historical normalization is silently replaced.

## 4. Explicit covectors and their positive Gram matrix

Put \(\lambda=256\pi^2/3=\nu\,64/3\). In the ordered source frame \(E\), the physical boundary matrix is
\[
\boxed{
P=\nu\eta_E
=\lambda\begin{pmatrix}
0&0&1\\
0&1&-4/3\\
1&-4/3&4/9
\end{pmatrix}.}
\]
In particular
\[
\ell_1(q_0,q_1,q_2)=\lambda q_2,\qquad
\ell_r(q)=\lambda(q_1-4q_2/3),
\]
\[
\ell_v(q)=\lambda(q_0-4q_1/3+4q_2/9).
\]
These rows are derived from the caps and defect, not selected to reproduce the real-plane period. The normalization and all orbit multiplicities are fixed.

Let \(G_{ij}=\langle h_f(E_i),h_f(E_j)\rangle\). Reflection gives the exact Riesz vectors and their Gram matrix:
\[
b_i=\Theta h_f(E_i),\qquad
\|b_i\|^2=G_{ii},\qquad
\boxed{\quad\mathcal B_{ij}=\langle b_i,b_j\rangle
=G_{ji},\qquad \mathcal B=PG^{-1}P^\dagger=\bar G>0.\quad}
\]
All three caps form a basis of the physical block, since \(P\) is nonsingular. The matrix identity also proves the residue-reality relation with its formerly unspecified physical constant now calibrated. It does not evaluate \(G(c,\bar c)\) at general shape.

There is an explicit test of information invisible to a boundary amplitude:
\[
\ell_1(1)=0,\qquad \|h_f(1)\|^2=\|b_1\|^2=H(c,\bar c)>0.
\]
The identity source is entirely orthogonal to its reflected identity cap. By contrast, the top-source cap detects it: \(\ell_v(1)=\lambda\). Thus this physical identity cap cannot be the strictly positive real-plane identity period. This is a property of this specified cap, not an obstruction to different physical boundaries.

For any nonzero cap label \(p\), the now-physical normalization law is
\[
\|h_f(q)\|^2
=\frac{|\nu\operatorname{Res}_f(pq)|^2}{\|h_f(p)\|^2}
+\left\|h_f(q)-\frac{\ell_p(q)}{\|h_f(p)\|^2}\,b_p\right\|^2.
\]
The denominator is the norm of an independently prepared state, rather than an arbitrary scalar in a period comparison. It can still require solving the physical metric problem.

## 5. An exactly evaluated interacting norm at the homogeneous endpoint

Consider \(f_0=(Z^4+W^4+Z^2W^2)/16\), and let \(s_0=Z^2+W^2\), \(t_0=Z^2W^2\). The degree-rotation symmetry proved in notes 06–07 gives
\[
G_0=\operatorname{diag}(a_0,a_2,a_4)>0
\quad\text{in }(1,s_0,t_0)\Omega_Z.
\]
In that frame the calibrated boundary matrix is
\[
P_0=\lambda\begin{pmatrix}0&0&1\\0&1&0\\1&0&0\end{pmatrix}.
\]
Combining \(P_0G_0^{-1}P_0^\dagger=G_0\) with positivity gives
\[
\boxed{\quad a_2=\lambda=\frac{256\pi^2}{3},\qquad
a_0a_4=\lambda^2.\quad}
\]
In particular the middle cap is its own Riesz state, \(b_{s_0}=h_{f_0}(s_0)\), with the exactly evaluated norm \(\lambda\). The top cap is \(b_{t_0}=(\lambda/a_0)h_{f_0}(1)\). It saturates the identity-source calibration law, while the identity cap sees zero identity amplitude. One positive constant \(a_0\) remains unevaluated by this endpoint algebra.

Consequently the physical strong-interaction endpoint in the original frame is now
\[
G(\rho)=D_\rho
\left[\operatorname{diag}\left(a_0,\lambda,\lambda^2/a_0\right)+o(1)\right]D_\rho,
\qquad D_\rho=\operatorname{diag}(\sqrt\rho,1,\rho^{-1/2}).
\]
This retains the earlier rescaled-limit qualification: it supplies neither unscaled off-diagonal decay nor derivative asymptotics.

### A normalized homogeneous prime control

The evaluated middle norm gives a physical alternative to the original identity insertion. For \(M\ne0\), take the interacting homogeneous Hamiltonian with
\[
f_M(U,V)=\frac{M^2}{16}(U^4+V^4+U^2V^2)
\]
and specify the polynomial cap source
\[
\sigma_M=\frac{\sqrt3\,M}{16\pi}
(U^2+V^2)\,dU\wedge dV.
\]
This is a different, explicitly stated boundary/source control. It is strongly elliptic with an isolated length-nine critical scheme for every \(M\ne0\); a Morse critical point is not needed. Let \(\phi_M(U,V)=(\sqrt M U,\sqrt M V)\). The source identity is
\[
\sigma_M=\frac1{M\sqrt\lambda}\phi_M^*(s_0\Omega_Z).
\]
Middle-degree pullback preserves the \(L^2\) norm under this constant conformal dilation, and intertwines harmonic kernels. Hence its prepared physical state satisfies
\[
\boxed{\quad\|h_{f_M}(\sigma_M)\|^2=|M|^{-2}.\quad}
\]
For \(M=1-q\) this is an exactly normalized Euler metric in a non-Gaussian theory. Every coefficient of the source is known from the physical residue calibration; no unknown square root of an arithmetic operator enters. The bilinear self-gluing is \(M^{-2}\), while the positive norm is \(|M|^{-2}\). Neither is asserted to be the earlier exponential identity period. The mass insertion remains Jacobi-trivial by quartic homogeneity, so this control does not generate the missing arithmetic curvature or infinite source space.

## 6. Contribution and remaining identification

This construction supplies actual normalizable boundary states, their physical adjoints, explicit cohomological covectors, a positive three-by-three Gram characterization, and an evaluated interacting source norm. It resolves the existence and absolute normalization of one family of physical caps. It also makes the previously missing orthogonal component concrete: the reflected identity amplitude vanishes on the identity state.

It does not turn a polynomial exponential period into that covector, evaluate the full metric as a function of shape, or supply the signed poles, fixed contact and all prime returns in one norm. A finite number of these vacua cannot provide the closed unbounded source required by the Weil form. [Note 11](11_CLOSED_ARITHMETIC_SOURCE.md) constructs the positive gamma source on its full domain; [note 12](12_MASSIVE_ENDPOINT.md) derives the other metric endpoint without losing the escaping vacua. The arithmetic interaction or boundary law joining these ingredients is still required.

The cap homotopy, opposite-twist descent, normalization and reflection identities are analytical model statements. Exact finite-matrix replay can check their displayed algebra, but cannot certify the Hodge comparison, decay, endpoint continuity or full Weil positivity.

The new [boundary algebra program](../numerics/check_boundary_pairing.py) and its [retained record](../numerics/records/boundary-pairing.json) check the reflection signs, Gaussian cohomology coefficients, homogeneous residue-reality family and massive frame conversion with exact arithmetic. [Note 13](13_RADIAL_METRIC_SELECTION.md) supplies the subsequent uniqueness argument for the global radial metric, conditional on its inherited exact chiral equation.
