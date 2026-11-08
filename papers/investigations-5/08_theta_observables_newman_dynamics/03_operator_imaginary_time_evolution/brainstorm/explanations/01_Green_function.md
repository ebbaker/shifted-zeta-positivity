**The Green potential is constructed directly from \(H_\lambda\), and your proposed localization of the Vandermonde statistics has a precise mathematical formulation.** The useful connection between them is that both can be expressed as observables of the complete zero configuration.

First, there is an unfortunate notation collision in the manuscript: **§6 and §18 both use \(J_\lambda\) for different objects.** Below I call the primitive transform \(\mathcal P_\lambda\) and the Green potential \(\mathcal J_\lambda\).

**The theta source, primitive, and \(H_\lambda\) form an exact chain.** With
\[
\vartheta(y)=\sum_{n\in\mathbb Z}e^{-\pi n^2y},
\]
the half-line primitive in (6.4) is
\[
p(u)=\frac{e^u}{2}\bigl[\vartheta(e^{4u})-1\bigr],
\qquad
\Phi(u)=\frac18\bigl(p''(u)-p(u)\bigr).
\]
Thus “primitive” here means a differential primitive of the theta source, rather than simply an antiderivative.

The Newman family is the cosine transform
\[
H_\lambda(z)=\int_0^\infty e^{\lambda u^2}\Phi(u)\cos(zu)\,du.
\tag{1.1, 2.2}
\]
The source coordinate \(u\), complex spatial coordinate \(z\), and Newman parameter \(\lambda\) are different variables. Differentiating this formula gives
\[
\partial_\lambda H_\lambda=-\partial_z^2H_\lambda.
\]
If your \(H(t,z)\) uses forward heat time, then \(H(t,z)=H_{\lambda_0-t}(z)\).

The primitive gives an alternative representation of exactly the same field. Define
\[
\mathcal P_\lambda(z)=\int_0^\infty p(u)e^{\lambda u^2}\cos(zu)\,du.
\]
Equation (6.6), with its essential endpoint contribution, becomes
\[
8H_\lambda(z)=
\frac12+(2\lambda-1-z^2)\mathcal P_\lambda(z)
+4\lambda z\mathcal P_\lambda'(z)
-4\lambda^2\mathcal P_\lambda''(z).
\]
In particular,
\[
8H_0(z)=\frac12-(1+z^2)\mathcal P_0(z).
\]

**The Green construction then acts on \(\log|H_\lambda|\), not directly on the theta source.** Its underlying identity is the distributional formula
\[
\boxed{\quad
\frac1{2\pi}\Delta_z\log|H_\lambda(z)|
=\sum_j m_j\delta_{z_j}.
\quad}
\]
Away from zeros, \(\log|H_\lambda|\) is harmonic. A zero of multiplicity \(m_j\) contributes a point source of strength \(m_j\).

This gives an electrostatic interpretation: \(\log|H_\lambda|\) is a potential, and the zeros are its charges. The Green function in §18 is the inverse-Laplacian kernel for the **spatial strip** \(0<\operatorname{Im}z<8\). It is not the heat kernel governing \(\lambda\).

At fixed \(\lambda\), equation (18.2) compares the harmonic extension of the boundary values with the actual interior value:
\[
\begin{aligned}
\mathcal J_\lambda(X)
={}&\int_{\mathbb R}K(x-X)
\bigl[\log|H_\lambda(x)|+\log|H_\lambda(x+8i)|\bigr]\,dx\\
&-\log|H_\lambda(X+4i)|.
\end{aligned}
\]
Green’s identity turns this discrepancy into
\[
\boxed{\quad
\mathcal J_\lambda(X)
=\sum_{y_j>0}G(X-x_j,y_j).
\quad}
\tag{18.3}
\]
The nonreal zeros inside the strip contribute positively; real zeros lie on its boundary and contribute no Green atom.

Consequently, the exact relationship is
\[
\vartheta
\;\longrightarrow\;p
\;\longrightarrow\;\Phi
\;\longrightarrow\;H_\lambda
\;\longrightarrow\;\log|H_\lambda|
\;\longrightarrow\;\mathcal J_\lambda.
\]
Either source representation of \(H_\lambda\) can be substituted into the Green formula. The logarithm makes this a nonlinear functional of the source: positivity of \(p\) or \(\Phi\) alone does not estimate it sharply. The prime-baseline formula (18.15) is another evaluation of this same functional, available specifically at \(\lambda=0\).

There is also a full-line source function called \(G_\lambda(u)\) in §2, obtained using \((1-\partial_u^2)^{-1}\). That is a different Green operator in the **source variable**, and should not be confused with the strip kernel \(G(X-x,y)\).

**Your interpretation of pair correlation is correct for the random-matrix ensemble, with one qualification.** For a unitary invariant Hermitian ensemble, the joint eigenvalue density has the form
\[
p_N(x_1,\ldots,x_N)
=\frac1{Z_N}
\left|\Delta(x_1,\ldots,x_N)\right|^2
\prod_{j=1}^N w_0(x_j),
\qquad
\Delta=\prod_{i<j}(x_j-x_i).
\]
Its two-point correlation is
\[
R_2(x,y)=N(N-1)
\int_{\mathbb R^{N-2}}
p_N(x,y,x_3,\ldots,x_N)\,dx_3\cdots dx_N.
\]
So we integrate out the other eigenvalues from the **full density**, including the squared Vandermonde and the confining weight—not from the Vandermonde alone. [dial.uclouvain.be](https://dial.uclouvain.be/pr/boreal/object/boreal%3A265974/datastream/PDF_02/view?utm_source=chatgpt.com)

Montgomery’s zeta statistic is instead a sum over a deterministic set of zeros, averaged over a growing height interval. His original paper assumes RH and identifies the connection with the random-matrix pair correlation
\[
1-\left(\frac{\sin\pi r}{\pi r}\right)^2.
\]
It does not derive a Vandermonde joint probability law for zeta zeros. Also, pair correlation need not be height independent: dependence only on separation arises in a translation-invariant, unfolded limiting description. [websites.umich.edu](https://websites.umich.edu/~hlm/paircor1.pdf?utm_source=chatgpt.com)

**Spatial weighting can be introduced before taking the two-point marginal—and can retain higher correlations.** For a compactly supported window \(w_{X,h}(x)=w((x-X)/h)\), consider
\[
\mathcal Z_{X,h}(\eta)
=
\frac1{Z_N}\int_{\mathbb R^N}
|\Delta(\mathbf x)|^2
\prod_{j=1}^N
w_0(x_j)\,[1+\eta w_{X,h}(x_j)]\,d\mathbf x.
\]
Equivalently,
\[
\mathcal Z_{X,h}(\eta)
=\mathbb E\prod_j[1+\eta w_{X,h}(x_j)].
\]
The factor is **one outside the window**, so it does not force the entire spectrum into that window. Expanding gives
\[
\mathcal Z_{X,h}(\eta)
=1+\eta\,\mathbb E\sum_jw_j
+\frac{\eta^2}{2}\mathbb E\sum_{j\ne k}w_jw_k+\cdots .
\]
This accesses weighted correlations of every order. Allowing arbitrary spatial test functions retains the full correlation hierarchy. For determinantal ensembles, these generating functionals have Fredholm-determinant representations; this is established machinery that closely matches your suggestion. [arxiv.org](https://arxiv.org/pdf/0911.1153?utm_source=chatgpt.com)

For our deterministic zeros, we can define the analogous observables without assuming a random-matrix law. Two formulations seem especially relevant:

- **A localized, marked pair statistic**
  \[
  S_{\lambda,X,h}[\Psi]
  =\sum_{j\ne k}w_{X,h}(x_j)w_{X,h}(x_k)
  \Psi(x_j-x_k,y_j,y_k).
  \]
  Retaining \(y_j,y_k\) matters. For example, a factor \((y_j-y_k)^2\) vanishes for pairs of real zeros but detects a conjugate nonreal pair. The unmarked version is closely related to the existing statistic (14.3).

- **A full configuration functional**
  \[
  \mathcal Z_\lambda[f]=\prod_j(1+f(z_j)),
  \]
  initially for compactly supported \(f\). Green weights fit naturally into it:
  \[
  \prod_{y_j>0}e^{-sG(X-x_j,y_j)}
  =e^{-s\mathcal J_\lambda(X)},
  \qquad s\ge0,
  \]
  with convergence supplied by §18’s zero-tail estimates.

There is a direct source interface for these proposals: the zero measure is \(\nu_\lambda=(2\pi)^{-1}\Delta\log|H_\lambda|\). A pair statistic is an integral against
\[
\nu_\lambda\otimes\nu_\lambda-\operatorname{diag}_*\nu_\lambda,
\]
where the subtraction removes self-pairs while retaining distinct multiplicity copies. This connects localized configuration statistics back to the theta-generated field without postulating a Vandermonde probability distribution.

**I would prioritize the Green method and investigate your suggestion with transverse marks retained.** A Vandermonde built only from ordinates also penalizes ordinary close real pairs and cannot distinguish a reflected off-line pair from a multiple critical-line zero. Green weights target the nonreal defect more specifically. The substantive question is whether a weighted configuration identity supplies a sharper source estimate than our current quadratic comparison; merely exponentiating \(\mathcal J\) supplies no new bound.

I retried chat-history capture and checked both registrations and transcript discovery. No matching transcript was available, and the app’s history-retrieval tools also failed, so I could not record this chat yet.