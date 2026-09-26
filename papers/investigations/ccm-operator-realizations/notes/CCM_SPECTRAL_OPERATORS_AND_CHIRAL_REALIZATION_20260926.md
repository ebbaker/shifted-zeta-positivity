# CCM spectral operators: metric transport and a finite chiral realization

Date: 26 September 2026.

Model: GPT-6 (Codex). Exact model variant and reasoning-effort setting are not exposed in this session.

Status: LLM-assisted expository note and elementary algebraic deductions. This is not an RH proof or a claim of a new spectral construction. The purpose is to explain the operators and make a possible search for another realization precise.

## Literature input and conventions

The circle underlying the earlier Connes–Consani construction has length
\(L=2\log\lambda\), with \(\lambda>1\). In centered logarithmic coordinates
\(x=\log u\), its momentum operator is
\[
D_0=-i\partial_x,\qquad
\operatorname{Dom}D_0=H^1_{\mathrm{per}}([-L/2,L/2]).
\]
The starting algebra is \(C^\infty(\mathbb R/L\mathbb Z)\), represented by multiplication on \(L^2\). See [Connes–Consani, Section 4](https://arxiv.org/html/2106.01715#S4).

For the 2025 CCM construction, let \(E_N\) contain Fourier modes \(|n|\le N\), and let \(W\) represent the restricted Weil form on this space. Assume its least eigenvalue \(\varepsilon\) is simple, with even eigenvector \(g\). Put
\[
T=W-\varepsilon I,\qquad
\ell_N(f)=(P_Nf)(L/2),\qquad \ell_N(g)=1,
\]
\[
A=D_0-(D_0g)\ell_N.
\]
CCM establish self-adjointness on
\[
\mathcal H_{\lambda,N}
=\big(E_N/\mathbb Cg,\langle\cdot,T\cdot\rangle\big)
\oplus E_N^\perp.
\]
The second summand retains its ordinary norm and free circle operator. Their determinant formula is
\[
\det_{\rm reg}(A-z)=-i e^{-izL/2}\widehat g(z),\qquad
\widehat g(z)=\int_{-L/2}^{L/2}g(x)e^{-izx}\,dx.
\]
Here the determinant refers to the induced quotient operator together with the free tail, not to the unreduced matrix containing the forced null vector. See [CCM, Theorem 5.10](https://arxiv.org/html/2511.22755v1).

The matrix mechanism behind this construction gives
\[
A^\dagger T=TA,\qquad
\Gamma T=T\Gamma,\qquad
\Gamma A=-A\Gamma,\qquad (\Gamma f)(x)=f(-x).
\]
These follow from the divided-difference commutator, the even ground vector, and the even boundary functional; see [Connes–van Suijlekom, Section 5](https://arxiv.org/html/2511.23257v1#S5).

The deductions below use these identities; they do not assume positivity of the unshifted Weil form.

## 1. An ordinary Hermitian matrix representing the quotient

Use the original \(L^2\) inner product to define
\[
H_0=g^\perp\cap E_N,\qquad
P=I-\frac{|g\rangle\langle g|}{\langle g,g\rangle}.
\]
Every quotient class has a unique representative in \(H_0\). Since \(Ag=0\), the quotient operator is represented there by
\[
K=PA|_{H_0}.
\]
Writing \(G=T|_{H_0}\), simplicity of the least eigenvalue gives \(G>0\). The weighted adjoint relation becomes
\[
K^\dagger G=GK.
\]
Consequently
\[
B=G^{1/2}KG^{-1/2}
\]
is Hermitian in the ordinary inner product:
\[
B^\dagger
=G^{-1/2}K^\dagger G^{1/2}
=G^{1/2}KG^{-1/2}=B.
\]

This is an exact finite-dimensional realization. More intrinsically, the map
\([f]\mapsto T^{1/2}f\) is unitary from the quotient with its \(T\)-metric to \(H_0\) with its ordinary metric. No zeta-zero locations enter this construction.

It is essential to form the quotient first. The expression \(T^{-1/2}\) on all of \(E_N\) is undefined, and \(A\) need not preserve the ordinary orthogonal complement of \(g\). The compression \(K\) accounts for both issues.

## 2. Chiral Dirac form and a supersymmetric Hamiltonian

Since \(g\) is even, \(P\) commutes with reflection. Thus \(H_0\) splits into even and odd subspaces, each of dimension \(N\). The operator \(K\) anticommutes with reflection, while \(G^{1/2}\) commutes with it. The same anticommutation therefore holds for \(B\).

In parity-adapted orthonormal coordinates,
\[
\Gamma=\begin{pmatrix}I_N&0\\0&-I_N\end{pmatrix},\qquad
B=\begin{pmatrix}0&C^\dagger\\C&0\end{pmatrix},
\]
for an \(N\times N\) matrix \(C\). Hence
\[
B^2=\begin{pmatrix}C^\dagger C&0\\0&CC^\dagger\end{pmatrix}\ge0.
\]

This supplies a finite chiral Dirac operator and its usual supersymmetric Hamiltonian. The positive eigenvalues of \(B\) are the nonzero singular values of \(C\), counted with multiplicity; negative eigenvalues are their negatives. Zero singular values yield zero modes in both parity sectors.

The statement concerns the finite modified sector. Adjoining the unmodified Fourier tail recovers the full spectral operator. Nothing in this algebraic construction implies that \(C\) is local, differential, sparse, or compatible with a geometric limit as \(\lambda,N\) increase. Such additional structure would be the actual research target.

This is also an operator equivalence. Equivalence of full spectral triples additionally requires an algebra representation and its intertwining. The original multiplication action cannot simply be declared to act on \(E_N/\mathbb Cg\): generally it neither preserves \(E_N\) nor preserves the null line. Any full geometric realization must handle that representation explicitly.

## 3. The absolute ground energy has been removed

For any real constant \(c\), replacing \(W\) by \(W+cI\) replaces its least eigenvalue by \(\varepsilon+c\). It leaves
\[
T=(W+cI)-(\varepsilon+c)I=W-\varepsilon I
\]
unchanged. The eigenvector, rank-one modification, quotient metric, \(B\), and \(C\) are consequently unchanged.

Therefore this realization cannot determine the sign of \(\varepsilon\) by self-adjointness or by positivity of \(B^2\) alone. A positivity proof for the original Weil form would need additional information fixing the absolute energy offset. The operators \(W\) and \(B^2\) should not be identified.

## 4. Exact small example

This example illustrates the algebra; it is not a computed Weil matrix. Use dimensionless frequencies and put
\[
T=\begin{pmatrix}3&-1&-1\\-1&1&-1\\-1&-1&3\end{pmatrix},\quad
D=\operatorname{diag}(-1,0,1),\quad
g=\tfrac14(1,2,1)^t,\quad \ell(f)=f_{-1}+f_0+f_1.
\]
Then \(Tg=0\), \(\ell(g)=1\), and \(A=D-(Dg)\ell\) satisfies \(A^tT=TA\) and reflection anticommutation.

Choose the ordinary orthogonal representatives
\(e=(1,-1,1)^t\), \(o=(-1,0,1)^t\). In these unnormalized coordinates,
\[
G=\begin{pmatrix}9&0\\0&8\end{pmatrix},\qquad
K=\begin{pmatrix}0&2/3\\3/4&0\end{pmatrix}.
\]
Flattening this coordinate metric gives
\[
B=\begin{pmatrix}0&1/\sqrt2\\1/\sqrt2&0\end{pmatrix},\qquad
B^2=\tfrac12 I_2.
\]
But \(W=T-2I\) has eigenvalues \(-2,1,2\). It has exactly the same shifted metric and Dirac realization, despite its negative least eigenvalue.

Verification: the null-vector, weighted-adjoint, reflection, quotient-metric, quotient-operator, and square identities were checked using exact rational arithmetic; the displayed square-root normalization follows directly. This check does not test a numerical approximation to zeta.

## 5. What a different realization should deliver

A useful realization would add a mechanism that survives increasing cutoffs. Three concrete targets are:

1. An independently described energy space realizing \(G\), with compatible embeddings as the cutoffs grow.
2. A local or otherwise tractable operator producing the same finite quotient dynamics and explaining the simple-even ground state.
3. Estimates strong enough to identify the normalized entire spectral functions with \(\Xi\) in a limit.

Finite metric transport alone supplies no uniform bound. If \(\varepsilon_1\) is the next eigenvalue of \(W\),
\[
\|G^{-1/2}\|=(\varepsilon_1-\varepsilon)^{-1/2}.
\]
A shrinking gap can make this representation difficult to control. This is a possible source of difficulty, not a proof that the transformed operators must diverge; cancellations could matter.

For the limiting argument, local uniform convergence on the open strip \(|\operatorname{Im}z|<1/2\), with nonzero limit \(\Xi(z)\) up to a known nonvanishing factor, is a sufficient target. It covers the transformed nontrivial zeros. Hurwitz applied to each half-strip would then exclude nonreal zeros. Agreement at selected real frequencies or operator convergence without the necessary entire-function control does not establish this target.

The prolate comparison already provides a concrete differential-operator route. The two outstanding requirements described in [Connes's survey, Section 6.6](https://arxiv.org/html/2602.04022v1#S6.SS6) are a simple even ground state for the Weil operator and sufficient approximation of that ground state by the prolate-based candidate. The candidate's Fourier-transform convergence is developed separately in Section 6.5. A change of realization should be assessed against these particular requirements.

Project continuity: [the 24 September bridge sweep, Route E](../../../susy-positivity/investigations/wilson-loewner/notes/ARITHMETIC_BRIDGE_SWEEP_AFTER_YM_20260924.md) already records the quotient metric, the lost energy offset, and the entire-function convergence requirement. The additional purpose of this note is to make the ordinary Hermitian and chiral forms explicit.
