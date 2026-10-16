# Exact shape-deformation algebra and the identity metric sector

13 September 2026. This calculation uses the canonical normalization of the manuscript: the physical superpotential is \(\mathcal W=G_c/2\), while the twisted Dolbeault differential is \(D=\bar\partial+\partial f_c\wedge\), with
\[
G_c(A,B)=\frac12(A^2+B^2)+\frac c4(A^4+B^4+A^2B^2),
\qquad f_c=G_c/4.
\]
Initially \(c>0\); the algebra and physical polynomial family extend to \(c\in\mathbb C^*\). The leading quartic remains strongly tame there. The real-plane holomorphic period has its directly convergent domain \(\Re c>0\); that smaller domain is not a restriction on the physical Hilbert problem.

The main reduction is exact: the identity volume belongs to a rank-three symmetry sector, its shape Higgs operator is explicit and nonzero, and its residue pairing has a fixed constant form after a holomorphic change of basis. The algebraic data alone do not determine the physical positive metric: they admit a flat positive control. The physical endpoint derived in section 7 excludes that control in the specified source frame and supplies one boundary of the remaining metric problem.

## 1. The Jacobi algebra and its cyclic invariant sector

The Jacobi algebra is
\[
\mathcal A_c=\frac{\mathbb C[A,B]}
 {\left(A(1+cA^2+\tfrac c2B^2),\ B(1+cB^2+\tfrac c2A^2)\right)}.
\]
The common factor \(1/4\) in the two derivatives of \(f_c\) does not change this ideal. It will matter for the residue pairing below.

There are nine simple points: the origin, four axis points with the nonzero coordinate squared \(-1/c\), and four points with \(A^2=B^2=-2/(3c)\). The algebra is consequently semisimple of dimension nine. An explicit vector-space basis is
\[
1,A,B,A^2,AB,B^2,A^2B,AB^2,A^2B^2.
\]
For example, the gradient relations reduce \(A^3,B^3\), and their products give
\[
A^3B=AB^3=-\frac{2}{3c}AB,
\qquad A^4=-\frac{A^2}{c}-\frac12A^2B^2,
\]
with the analogous formula for \(B^4\). Evaluation at the nine simple points, or the complete-intersection dimension, verifies that the spanning set is a basis.

Set \(s=A^2+B^2\) and \(t=A^2B^2\). Direct reduction gives
\[
\boxed{\quad
s^2=-s/c+t,\qquad st=-4t/(3c),\qquad t^2=4t/(9c^2).
\quad}
\]
Thus \(\operatorname{span}\{1,s,t\}\) is a closed three-dimensional subalgebra. Its spectrum consists of the values
\[
(s,t)=(0,0),\quad(-1/c,0),\quad(-4/(3c),4/(9c^2)).
\]

The canonical shape Higgs operator is multiplication by
\[
\boxed{\quad
C_c=[\partial_cf_c]
=\frac{[A^4+B^4+A^2B^2]}{16}
=-\frac{s}{16c}.
\quad}
\]
The last equality follows by summing \(A\partial_AG_c+B\partial_BG_c\) in the Jacobi ideal. In the ordered basis \((1,s,t)\), columns representing multiplication of basis vectors,
\[
C_c=
\begin{pmatrix}
0&0&0\\
-1/(16c)&1/(16c^2)&0\\
0&-1/(16c)&1/(12c^2)
\end{pmatrix}.
\]
Its eigenvalues are \(0,1/(16c^2),1/(12c^2)\). The identity is cyclic: its first two nontrivial powers under \(C_c\) span \(s,s^2\), and hence \(s,t\). No smaller invariant subspace can contain the identity for \(c\ne0\).

## 2. The volume character determines the physical sector

Let \(\mathsf G=(\mathbb Z_2)^2\rtimes S_2\), of order eight, act by the two coordinate sign changes and by exchange of \(A,B\). The potential and flat metric are invariant. The holomorphic volume
\[
\Omega=dA\wedge dB
\]
transforms by the determinant character \(\chi(g)=\det g\): each individual sign change and the exchange have character \(-1\). Accordingly,
\[
g^*(p\Omega)=\chi(g)(p\circ g)\Omega.
\]
The \(\chi\)-isotypic sector of \(\mathcal A_c\Omega\) is therefore precisely the invariant-polynomial subspace times \(\Omega\). The invariant polynomials take one independent value on each of the three critical-point orbits; their dimension is three and their representatives are \(1,s,t\).

The physical Hamiltonian, its vacuum projector, and the shape insertion commute with this fixed finite-group action. Thus the Hermitian metric and projected connection restrict to this sector. This is a physical block reduction, not a replacement of the full nine-vacuum theory by a three-vacuum theory. It also explains why using only even polynomials without checking the volume character would risk selecting the wrong representation.

There is no division of a physical norm or residue by eight in this reduction. The character projector already acts as the identity on these sources. One may normalize orbit sums differently, but must then transform both the source coordinates and pairings.

## 3. The residue pairing, including orbit multiplicities

Fix the conventional Grothendieck-residue normalization
\[
\eta(p\Omega,q\Omega)
=\frac1{(2\pi i)^2}\int
\frac{p(A,B)q(A,B)\,dA\wedge dB}
 {\partial_Af_c\,\partial_Bf_c}
=\sum_{v:\,df_c(v)=0}\frac{p(v)q(v)}{\det\operatorname{Hess}f_c(v)}.
\]
The cycle is the sum of the local residue tori with their standard complex orientations. This is a complex bilinear topological pairing, not a positive Hermitian norm.

Because \(f_c=G_c/4\), its Hessian determinant is \(1/16\) that of \(G_c\). The inverse determinants at the three types of point are
\[
16\quad\text{at the origin},\qquad
-16\quad\text{at each axis point},\qquad
12\quad\text{at each both-nonzero point}.
\]
The orbit weights are therefore \((16,-64,48)\). In the basis \((1,s,t)\),
\[
\boxed{
\eta(c)=
\begin{pmatrix}
0&0&64/(3c^2)\\
0&64/(3c^2)&-256/(9c^3)\\
64/(3c^2)&-256/(9c^3)&256/(27c^4)
\end{pmatrix}.}
\]
For instance, \(\eta(1,1)=16-64+48=0\), while
\(\eta(1,t)=48\cdot4/(9c^2)=64/(3c^2)\).
The determinant is \(-[64/(3c^2)]^3\ne0\). Vanishing self-residue of the identity does not imply a vanishing physical norm.

Use the holomorphic frame
\[
E=(1,r,v)\Omega,\qquad r=cs,\quad v=c^2t.
\]
Both the algebra relations and the residue matrix then become constant:
\[
r^2=-r+v,\qquad rv=-4v/3,\qquad v^2=4v/9,
\]
\[
\eta_E=
\begin{pmatrix}
0&0&64/3\\
0&64/3&-256/9\\
64/3&-256/9&256/27
\end{pmatrix},\qquad
C_c=-\frac{R}{16c^2},\qquad
R=\begin{pmatrix}0&0&0\\1&-1&0\\0&1&-4/3\end{pmatrix}.
\]
In particular \(\eta_E R=R^T\eta_E\), as required by invariance of the topological pairing under multiplication.

This is a holomorphic source frame, not a claim that the physical vacuum vectors are parameter independent. Its first vector is the original identity volume \(\Omega\). Its other vectors are the explicitly parameter-dependent insertions \(c(A^2+B^2)\Omega\) and \(c^2A^2B^2\Omega\). Their factors must be retained when differentiating sources or comparing physical pairings. The induced connection transforms with this holomorphic frame change; the multiplication matrices transform by conjugation.

The invariant orbit idempotents are
\[
e_0=1+r+\tfrac34v,\qquad
e_a=-r-3v,\qquad
e_b=\tfrac94v,
\qquad e_0+e_a+e_b=1.
\]
In this frame the residue is \(\operatorname{diag}(16,-64,48)\), and the Higgs matrix is diagonal. These are orbit sums of primitive idempotents; the multiplicities four have already been included.

## 4. The exact metric problem and an algebraic nonuniqueness control

Let \(g(c,\bar c)>0\) be the physical metric of this rank-three block in the frame \(E\). In the usual chiral \(tt^*\) normalization, its necessary equations are
\[
\partial_{\bar c}(g^{-1}\partial_cg)
=[C_c,g^{-1}C_c^*g],\qquad \partial_{\bar c}C_c=0.
\]
The physical reality structure additionally obeys the standard compatibility with the topological pairing; in a convention with this residue as \(\eta_E\), it reads
\[
(\eta_E^{-1}g)\overline{(\eta_E^{-1}g)}=I.
\]
A universal constant used to normalize the physical realization and its topological pairing must be carried consistently; the residue convention by itself is not a numerical evaluation of the Hilbert norm. The equation is the one developed in [Cecotti–Vafa](https://doi.org/10.1016/0550-3213(91)90021-O) and in the chiral-parameter Berry derivation of [Sonner–Tong](https://arxiv.org/abs/0810.1280). The strongly tame Hodge realization is supplied by [Fan](https://arxiv.org/abs/1107.1290).

Taking the trace gives \(\partial_c\partial_{\bar c}\log\det g=0\). With the displayed constant pairing and reality normalization, positivity fixes \(\det g=|\det\eta_E|\). This constrains the full block; it does not determine its identity component.

The parameter \(u=1/c\) makes the Higgs operator constant:
\[
C_u=C_c\frac{dc}{du}=R/16,
\qquad
\operatorname{spec}C_u=\{0,-1/16,-1/12\}.
\]
The critical values of \(f_c\) are correspondingly \(0,-u/16,-u/12\). This gives three distinct exponential scales for the associated flat-connection problem, but does not determine its Stokes or physical boundary data.

Indeed, in the orbit-idempotent frame the constant positive matrix
\[
g_{\mathrm{flat}}=\operatorname{diag}(16,64,48)
\]
has zero curvature, makes the diagonal Higgs operator normal, and satisfies the stated residue reality relation. It is an exact positive solution of these metric equations. Its identity-source norm is the constant \(128\) in this topological normalization. It has not been identified with the vacuum metric of the polynomial Hamiltonian. This provides a concrete warning: a nonzero semisimple chiral class does not force nonzero curvature or select the physical metric.

## 5. An additional physical symmetry reduces the problem to a radial matrix equation

The simultaneous physical analysis supplies a useful exact symmetry, which can also be checked directly. Dilation gives
\[
f_c(A,B)=c^{-1}f_1(\sqrt c\,A,\sqrt c\,B).
\]
All three sources in \(E\) become \(c^{-1}\) times the pullback of fixed polynomial volume classes for \(u f_1\), with \(u=1/c\). Middle-degree pullback is an \(L^2\) isometry under this constant conformal scaling, so
\[
g_E(c,\bar c)=|c|^{-2}\,g^{\mathrm{ref}}(u,\bar u).
\]
For the reference differential \(D_u=\bar\partial+u\partial f_1\wedge\), multiplication of a \((p,q)\)-form by \(e^{ip\theta}\) is unitary and conjugates \(D_u\) to \(D_{e^{i\theta}u}\). Each polynomial volume source has holomorphic degree two, so all three acquire the same source phase. Their Hermitian Gram matrix is invariant. Consequently the entire \(E\)-frame physical metric, not just its identity norm, depends only on \(|c|\).

Write it in the inverse parameter as \(G(\rho)\), \(\rho=|u|>0\). The ordinary metric equation reduces exactly to
\[
\boxed{
\frac{d}{d\rho}\left(G^{-1}\frac{dG}{d\rho}\right)
+\frac1\rho G^{-1}\frac{dG}{d\rho}
=\frac1{64}[R,G^{-1}R^TG].
}
\]
The coefficient follows from \(C_u=R/16\) and
\(\partial_{\bar u}(G^{-1}\partial_uG)=\tfrac14[(G^{-1}G')'+\rho^{-1}G^{-1}G']\). Positivity, the residue reality condition, and physically derived behavior at \(\rho\to0\) and \(\rho\to\infty\) must supplement this equation. The constant control above still solves it. Radial symmetry is thus an exact reduction, not a boundary condition or a uniqueness theorem.

## 6. What is fixed, and what remains to derive

The shape deformation is not the previous mass dilation: its chiral class is nonzero, the identity generates a rank-three block, and the mass-normalized Euler period is not protected against it. The algebra specifies multiplication, topological residues, critical-value separations, symmetry, and a radial matrix \(tt^*\) equation. It does not specify the physical Hermitian solution or identify it with a squared period.

The next analytic task is to derive the physical endpoint/Stokes conditions for this radial problem from the polynomial Hamiltonian, with its identity source fixed. The physically relevant scalar is \(g_{00}\), while the other block entries can be essential to its curvature equation; discarding them would return to an invalid scalar closure. A comparison with the identity period must keep its different normalization and insertion exponent. In particular, the period uses \(e^{-G_c}\), whereas the canonical Higgs operator above differentiates \(f_c=G_c/4\).

A possible subsequent escape is a physically selected source in the full rank-three block. For coordinates \(b(c)\) in the stated frame, its norm is \(b^*g_Eb\) and its holomorphic period is the corresponding linear combination of the three source periods. This adds mixing unavailable to a common scalar rescaling of the identity. A boundary condition, charge selection rule, or transport law must specify \(b\); choosing its three components from the desired arithmetic answer would not constitute a construction. Even a successful local-factor identity in this block would not supply the infinite-dimensional input space required by the full Weil form.

The calculations in Sections 1–4 are direct algebra. The radial Hilbert-space symmetry in Section 5 was obtained jointly with the companion physical-norm investigation. No positivity estimate, numerical fitting, metric boundary-condition uniqueness, or complete Weil pairing has been established here.

## 7. The pure-quartic endpoint supplies a physical boundary condition

The large-positive-\(c\) limit can be examined without assuming a semiclassical sum over separated vacua. Put
\[
Z=c^{1/4}A,\qquad W=c^{1/4}B,\qquad
\varepsilon=c^{-1/2},
\]
and define, now in the \((Z,W)\) coordinates,
\[
q_4=Z^4+W^4+Z^2W^2,\qquad s_0=Z^2+W^2,\qquad t_0=Z^2W^2,
\qquad
f_\varepsilon=\frac{q_4}{16}+\frac{\varepsilon s_0}{8}.
\]
The rescaled superpotential is exactly \(f_c=f_\varepsilon\circ\phi_c\). Its critical points collide at the origin when \(\varepsilon=0\); the limiting function is not Morse. Accordingly the Morse-only Hodge counting theorem cannot be applied at that endpoint.

### Why the harmonic source metric continues through the collision

The needed general result is the strongly elliptic comparison theorem of [Li–Wen, *On the L2-Hodge Theory of Landau–Ginzburg Models*](https://arxiv.org/abs/1903.02713), together with its \(L^2\) Hodge decomposition. Their Theorem 2.34 compares compactly supported, rapidly decreasing Sobolev, and smooth twisted complexes without requiring Morse critical points.

Here the assumptions can be verified uniformly for \(\varepsilon\) near zero. The leading cubic gradient has no zero on the complex unit sphere, so
\[
|\nabla f_\varepsilon|\ge aR^3-bR,
\qquad
|\nabla^k f_\varepsilon|=O(1+R^{4-k})\quad(2\le k\le4),
\]
with fixed constants on a bounded \(\varepsilon\) set; higher derivatives vanish. These estimates imply the strongly elliptic condition at every derivative order. The critical loci stay in a fixed compact set. The gradient ideal is a zero-dimensional complete intersection of length nine, including the homogeneous limit. On the Stein space \(\mathbb C^2\), its holomorphic Koszul complex therefore has only degree-two cohomology, represented by the same nine polynomial classes. The comparison and Hodge theorems identify this with the physical harmonic space. In particular, no extra zero modes are introduced at \(\varepsilon=0\).

Continuity of the specified sources requires more than this dimension count. The twisted Laplacians have a common confining leading term of degree six; the parameter-dependent terms have lower polynomial degree and are infinitesimally bounded as quadratic forms. They consequently form a norm-resolvent-continuous family. The discrete zero eigenspace has the constant rank just established, so its spectral projector \(P_\varepsilon\) is continuous. One may choose a fixed compact cutoff containing every critical point. The finite cutoff homotopy used in the comparison theorem turns each polynomial-volume source into a compactly supported representative depending continuously on \(\varepsilon\), because the gradient is uniformly nonzero on the cutoff annulus. Applying \(P_\varepsilon\) gives continuous harmonic representatives of the fixed sources.

It follows that their three-component metric satisfies
\[
g^{(\varepsilon)}\longrightarrow g^{(0)}>0
\quad\text{in the fixed source frame}\quad
(1,s_0,t_0)\,dZ\wedge dW.
\]
This establishes source continuity using the isolated-singularity theorem and the explicit uniform estimates; it is not an extrapolation of a Morse theorem through a degenerate point.

### The limiting metric is diagonal before the singular rescaling

Let \(T_\theta\) rotate both coordinates by \(e^{i\theta}\). Since \(f_0\) is homogeneous of degree four, \(T_\theta^*\) conjugates \(D_{f_0}\) to \(D_{e^{4i\theta}f_0}\). Combine this pullback with the unitary form-degree rotation from Section 5:
\[
\mathcal V_\theta=U_{-4\theta}T_\theta^*.
\]
It commutes with the physical twisted differential and its adjoint. On a degree-\(d\) polynomial volume source, its character is
\[
e^{i(d+2)\theta}e^{-8i\theta}=e^{i(d-6)\theta}.
\]
The sources \(1,s_0,t_0\) have the distinct charges \(-6,-4,-2\). Unitarity therefore forces
\[
g^{(0)}=\operatorname{diag}(a_0,a_2,a_4),\qquad a_0,a_2,a_4>0.
\]
These constants are physical harmonic norms, not values obtained from the residue computation.

Middle-degree conformal invariance and the source volume Jacobian give the exact relation
\[
g_E(c)=D_c^*g^{(\varepsilon)}D_c,
\qquad
D_c=\operatorname{diag}(c^{-1/2},1,c^{1/2}).
\]
Thus, with the inverse radial variable \(\rho=1/c\),
\[
\boxed{
G(\rho)=D_\rho
\bigl[\operatorname{diag}(a_0,a_2,a_4)+o(1)\bigr]D_\rho,
\qquad
D_\rho=\operatorname{diag}(\rho^{1/2},1,\rho^{-1/2}),
\quad\rho\downarrow0.
}
\]
In particular
\[
G_{00}(\rho)\sim a_0\rho,\qquad
G_{11}(\rho)\to a_2,\qquad
G_{22}(\rho)\sim a_4/\rho.
\]
Only the rescaled limiting matrix has been asserted diagonal. Small off-diagonal entries before multiplication by \(D_\rho\) need not remain small after this singular rescaling. No unproved derivative asymptotics are required for the three displayed limits.

The physical identity norm tends to zero, so the constant positive metric from Section 4 cannot be the metric selected by this polynomial Hamiltonian. The endpoint supplies a substantive boundary condition for the radial matrix equation. It does not yet supply its other endpoint data or prove uniqueness of the resulting solution.

### What the residue reality condition can fix at this endpoint

The pure-quartic residue on \((1,s_0,t_0)\Omega\) is
\[
\eta_0=\begin{pmatrix}0&0&a\\0&a&0\\a&0&0\end{pmatrix},
\qquad a=64/3.
\]
For example, at nonzero \(\varepsilon\) the same residue calculation gives \(\eta(1,t_0)=\eta(s_0,s_0)=a\), \(\eta(s_0,t_0)=-256\varepsilon/9\), and \(\eta(t_0,t_0)=256\varepsilon^2/27\); the homogeneous residue has the indicated limit.

If the physical topological pairing has been calibrated to exactly this residue normalization, its reality condition and diagonal \(g^{(0)}\) imply
\[
a_0a_4=a^2,\qquad a_2=a.
\]
This leaves one positive endpoint constant undetermined by that algebraic condition. If the physical pairing instead carries a universal factor \(\nu\), the corresponding statements are \(a_0a_4=|\nu|^2a^2\) and \(a_2=|\nu|a\). No value of \(\nu\), \(a_0\), or a period-to-norm proportionality is assumed or evaluated here.

The small exact matrix replay is [check_shape_jacobi.py](../numerics/check_shape_jacobi.py), with its retained [record](../numerics/records/shape-jacobi.json). It checks the finite algebra and the auxiliary control, not the Hodge comparison or the physical endpoint proof.
