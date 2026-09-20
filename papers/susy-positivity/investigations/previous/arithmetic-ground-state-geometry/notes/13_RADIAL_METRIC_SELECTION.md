# Selection of the physical radial metric by its two endpoints

13 September 2026. The reflected pairing fixes the absolute topological normalization, and the separated-vacuum construction supplies the formerly missing massive endpoint. This note proves that the resulting endpoint problem has at most one positive metric. The proof is an elementary trace calculation followed by the maximum principle; it does not assume equal values of the remaining homogeneous-endpoint constant.

The statement is conditional on the inherited exact chiral metric equation in the specified polynomial-source frame. It does not independently rederive that equation from the supercharges. Under that identification, the globally defined physical Hodge metric supplies existence, and the argument below supplies uniqueness. The remaining constant is consequently selected by the theory, although its value and the associated Stokes matrices are not evaluated here.

## 1. The fixed equation and physically derived endpoint data

Retain the differential normalization
\[
f_c=\frac{A^2+B^2}{8}
+\frac{c}{16}(A^4+B^4+A^2B^2),
\qquad D_c=\bar\partial+df_c\wedge,
\qquad c\ne0.
\]
In the fixed holomorphic source frame
\[
E=(1,c(A^2+B^2),c^2A^2B^2)\,dA\wedge dB,
\]
put \(u=1/c\), \(\rho=|u|\), and
\[
C=\frac{R}{16},\qquad
R=\begin{pmatrix}
0&0&0\\
1&-1&0\\
0&1&-4/3
\end{pmatrix}.
\]
The exact equation assumed from the chiral Hodge identification is
\[
\partial_{\bar u}(g^{-1}\partial_u g)
=[C,g^{-1}C^\dagger g].
\tag{1}
\]
Here derivatives act on matrix coefficients, and \(C^\dagger\) is the ordinary conjugate transpose in this frame; the physical adjoint is \(g^{-1}C^\dagger g\). In particular the coefficient is \(1/16\), not \(1/8\). For a radial metric, (1) becomes
\[
(g^{-1}g')'+\rho^{-1}g^{-1}g'
=\frac1{64}[R,g^{-1}R^Tg],
\tag{2}
\]
where a prime denotes differentiation with respect to \(\rho\).

The physical metric is positive and radial by the unitary phase symmetry in [note 06](06_SHAPE_DEFORMATION_GEOMETRY.md). The source comparison at the homogeneous limit in [note 07](07_PHYSICAL_PAIRING_TEST.md), calibrated by the reflected pairing in [note 10](10_REFLECTED_BOUNDARY_PAIRING.md), gives
\[
g(\rho)=D_\rho\,[A(a_0)+o(1)]\,D_\rho,
\qquad \rho\downarrow0,
\tag{3}
\]
\[
D_\rho=\operatorname{diag}(\sqrt\rho,1,\rho^{-1/2}),
\qquad
A(a)=\operatorname{diag}(a,k,k^2/a),
\qquad
k=\frac{256\pi^2}{3},\quad a>0.
\]
The error in (3) is after the displayed two-sided rescaling. Neither unscaled off-diagonal decay nor derivative asymptotics are assumed.

The opposite endpoint in [note 12](12_MASSIVE_ENDPOINT.md) is
\[
g(\rho)=g_\infty+O(\rho^{-1/2}),
\qquad \rho\to\infty,
\tag{4}
\]
\[
g_\infty=4\pi^2
\begin{pmatrix}
128&-128&64/3\\
-128&448/3&-256/9\\
64/3&-256/9&256/27
\end{pmatrix}>0.
\]
Positivity follows also from its expression as the congruence of
\(4\pi^2\operatorname{diag}(16,64,48)\) by the invertible orbit-evaluation matrix. The convergence alone is enough below; its stated rate is not needed for uniqueness. The frame, all source factors and this massive normalization are held fixed throughout the comparison.

## 2. An explicit subharmonic trace identity

We first work locally with any two positive \(C^2\) Hermitian matrix solutions \(g_1,g_2\) of (1), for the same holomorphic Higgs matrix. The proof applies to a nonconstant holomorphic \(C(u)\) as well. Define
\[
F_{12}=\operatorname{tr}(g_1^{-1}g_2).
\]
This is a real, positive, frame-independent function. At an arbitrary point \(u_0\), a holomorphic change of frame can arrange
\[
g_1(u_0)=I,\qquad
\partial_u g_1(u_0)=0.
\tag{5}
\]
To see this, first use a constant frame transformation to set \(g_1(u_0)=I\); a holomorphic frame transformation with prescribed first derivative then cancels \(\partial_u g_1(u_0)\). Hermitian symmetry also gives \(\partial_{\bar u}g_1(u_0)=0\). A further constant unitary transformation preserves (5) and diagonalizes the other metric:
\[
g_2(u_0)=\Lambda=\operatorname{diag}(\lambda_1,\ldots,\lambda_r),
\qquad \lambda_i>0.
\]
All matrices in the following calculation are in that frame at \(u_0\). Write \(X=\partial_u g_2\), so \(\partial_{\bar u}g_2=X^\dagger\).

Expanding (1) before taking a trace gives, for either metric,
\[
\partial_{\bar u}\partial_u g_i
=(\partial_{\bar u}g_i)g_i^{-1}(\partial_u g_i)
+g_i Cg_i^{-1}C^\dagger g_i-C^\dagger g_i C.
\tag{6}
\]
At the chosen point,
\[
\partial_{\bar u}\partial_u g_1=[C,C^\dagger],
\qquad
\partial_{\bar u}\partial_u(g_1^{-1})=-[C,C^\dagger].
\]
The mixed product-rule terms vanish by (5). Therefore
\[
\begin{aligned}
\partial_{\bar u}\partial_u F_{12}
={}&\operatorname{tr}(X^\dagger\Lambda^{-1}X)\\
&+\operatorname{tr}\!\left(
\Lambda C\Lambda^{-1}C^\dagger\Lambda
-C^\dagger\Lambda C-[C,C^\dagger]\Lambda
\right).
\end{aligned}
\tag{7}
\]
The first term is the squared Hilbert-Schmidt norm of
\(\Lambda^{-1/2}X\). For the remaining terms, cyclicity of the trace gives
\[
\begin{aligned}
&\operatorname{tr}\!\left(
\Lambda C\Lambda^{-1}C^\dagger\Lambda
-C^\dagger\Lambda C-[C,C^\dagger]\Lambda
\right)\\
&\quad=
\operatorname{tr}(\Lambda^2 C\Lambda^{-1}C^\dagger)
-2\operatorname{tr}(\Lambda CC^\dagger)
+\operatorname{tr}(\Lambda C^\dagger C)\\
&\quad=\sum_{i,j}
\left(\frac{\lambda_i^2}{\lambda_j}-2\lambda_i+\lambda_j\right)
|C_{ij}|^2.
\end{aligned}
\]
Thus the sign required for the maximum principle follows directly from the sign of (1):
\[
\boxed{\quad
\partial_{\bar u}\partial_u F_{12}
=\|\Lambda^{-1/2}X\|_{\rm HS}^2
+\sum_{i,j}\frac{(\lambda_i-\lambda_j)^2}{\lambda_j}|C_{ij}|^2
\ge0.
\quad}
\tag{8}
\]
The frame used to evaluate the right-hand side is local to the point; the scalar inequality on the left is invariant. Since \(u_0\) was arbitrary, \(F_{12}\) is subharmonic. Exchanging the two metrics proves the same for \(F_{21}\).

Define their symmetric trace distance by
\[
d=F_{12}+F_{21}-2r.
\tag{9}
\]
The matrix \(g_1^{-1}g_2\) is similar to the positive Hermitian matrix
\(g_1^{-1/2}g_2g_1^{-1/2}\). If its positive eigenvalues are \(\mu_i\), then
\[
d=\sum_i(\mu_i+\mu_i^{-1}-2)\ge0,
\tag{10}
\]
and equality is equivalent to \(g_1=g_2\). By (8), \(d\) is subharmonic. This calculation is a direct version of the usual harmonic-metric comparison argument; no global uniqueness theorem for filtered Higgs bundles is being invoked.

## 3. The endpoint conditions force equality

Suppose \(g_1,g_2\) are positive radial solutions of (1), each obeying (3) with some constants \(a_1,a_2>0\), and both converging to the same \(g_\infty\) in (4). We do not require \(a_1=a_2\).

Write \(g_i=D_\rho(A(a_i)+\varepsilon_i)D_\rho\), with \(\varepsilon_i\to0\), near zero. Then
\[
g_1^{-1}g_2
=D_\rho^{-1}(A(a_1)+\varepsilon_1)^{-1}
(A(a_2)+\varepsilon_2)D_\rho.
\]
Similarity cancels the singular powers in its trace. The same applies with the indices reversed. In particular \(d\) is bounded near zero; more explicitly,
\[
d(\rho)\longrightarrow
2\left(\frac{a_2}{a_1}+\frac{a_1}{a_2}-2\right)<\infty.
\tag{11}
\]
At infinity, the common positive limit gives
\[
d(\rho)\longrightarrow0.
\tag{12}
\]

For completeness, apply the maximum principle on an annulus
\(\epsilon<|u|<R\). Let \(K\) bound \(d\) on all sufficiently small inner circles, and let \(\delta_R=\sup_{|u|=R}d\). The harmonic function
\[
\delta_R+(K-\delta_R)
\frac{\log(R/|u|)}{\log(R/\epsilon)}
\]
has values \(K\) and \(\delta_R\) on the two boundary circles. Since \(d\) is subharmonic, it is bounded above by this function. For a fixed interior point, first let \(\epsilon\downarrow0\), obtaining \(d(u)\le\delta_R\), and then let \(R\to\infty\). Equations (10) and (12) give \(d(u)=0\). Hence
\[
\boxed{\quad g_1=g_2\text{ on }\mathbb C^*.\quad}
\tag{13}
\]

The same proof works without radiality if the two endpoint conditions hold uniformly on parameter circles. Radiality also gives a shorter formulation: \(d(e^t)\) is convex in \(t=\log\rho\), is bounded as \(t\to-\infty\), and tends to zero as \(t\to+\infty\). A nonnegative convex function with those properties is identically zero. Neither version differentiates the endpoint expansions.

## 4. What supplies existence in this physical problem

For each \(c\ne0\), the polynomial differential already defines a positive Hilbert theory and its physical source metric, independently of solving (1). Its leading quartic gradient has cubic growth and no nonzero common zero; on a sufficiently small neighborhood of any fixed \(c_0\ne0\), the confinement estimates are uniform. The closed Hamiltonian forms have the common domain consisting of \(H^1\) forms with \(|(A,B)|^3\)-weighted coefficients in \(L^2\). Their coefficients depend smoothly on the real and imaginary parts of \(c\). The local form-operator inverse identity gives smooth norm-resolvent dependence after adding a fixed positive scalar.

The kernel dimension is nine throughout this neighborhood. A small spectral contour around zero therefore gives a smooth finite-rank physical projection. A common compact cutoff contains the nearby critical sets; the explicit comparison homotopy makes the specified polynomial-volume sources smooth \(L^2\) representatives. Applying the projection yields a smooth positive source metric. These local constructions agree on overlaps because the harmonic representative of each fixed cohomology class is unique. Thus the physical metric exists globally on \(\mathbb C^*\), although no uniform gap at a singular endpoint is required.

The analytic inputs are the strongly elliptic Hodge decomposition and comparison theorem in [Li–Wen, *On the L2-Hodge theory of Landau–Ginzburg models*](https://arxiv.org/html/1903.02713), together with the model's polynomial estimates. The chiral metric framework is developed in [Fan, *Schrödinger equations, deformation theory and tt*-geometry*](https://arxiv.org/abs/1107.1290). This note takes the identification of that physical metric with the exact equation (1), in the already specified holomorphic frame, as an explicit inherited hypothesis. Hodge existence alone is not a substitute for that identification.

Under this hypothesis, the physical metric supplies a solution of (1) with the independently derived endpoints (3)–(4), and (13) proves it is the only positive solution in this class. In particular the residual homogeneous constant \(a_0\) is not a free physical normalization or shooting choice. It is fixed implicitly by the global equation and the massive boundary normalization, with existence supplied by the original quantum mechanics.

No value of \(a_0\), higher asymptotic correction, Stokes matrix, or numerical solution is obtained here. The result establishes uniqueness of the physically normalized metric problem under the stated equation; it does not identify a polynomial exponential period with a physical cap or construct the complete Weil pairing. Exact algebra checks can verify the finite matrices and trace manipulations, but do not certify the analytical Hodge assumptions or the maximum-principle argument.
