# CCM operators as strings and graph Dirac operators: locality and cutoff obstructions

Date: 26 September 2026. Continuation round 2.

Model: GPT-6 (Codex). The exact variant and reasoning-effort setting are not exposed in this session.

Status: LLM-assisted working research. The finite transformations and estimates below are proved algebraically, conditional on the explicitly stated CCM hypotheses. The limiting proposition is conditional. Numerical observations are multiprecision checks, not interval certificates. The accompanying [critical review](../reviews/STRING_REALIZATION_CRITICAL_REVIEW_20260926.md) is a same-agent review, not independent refereeing. No novelty claim is made for Jacobi/string theory, graph Dirac operators, or Green-kernel trace formulas.

Predecessors: [boundary mechanics and determinant control](CCM_BOUNDARY_MECHANICS_AND_DETERMINANT_CONTROL_20260926.md), [founding note](CCM_SPECTRAL_OPERATORS_AND_CHIRAL_REALIZATION_20260926.md), and [initial derivation review](../reviews/INITIAL_DERIVATION_CHECK_20260926.md). Those records and their programs are preserved unchanged.

## 1. Outcome

A finite positive CCM mechanical pencil can be converted into a string of positive point masses and positive nearest-neighbor springs. For a cyclic forcing vector it is one connected string; without cyclicity, a direct sum of strings realizes the whole pencil. The associated weighted incidence operator gives an explicit graph Dirac operator unitarily equivalent to the finite CCM quotient, including its metric, not merely an agreement of eigenvalues.

The useful invariant is
\[
\boxed{\operatorname{tr}(K^{-1}M)
 =\sum_i m_i x_i
 =\operatorname{tr}\mathcal C_\mu},\qquad
\mu=\sum_i m_i\delta_{x_i},
\quad
\mathcal C_\mu=\int |1_{(0,x)}\rangle\langle1_{(0,x)}|\,d\mu(x).
\tag{1}
\]
Here \(x_i\) is distance from the fixed end in the reconstructed string, **not** the logarithmic arithmetic coordinate. The last operator acts on the common strain space \(L^2(0,\infty;ds)\). Its nonzero eigenvalues are \(\omega_j^{-2}\). This supplies a concrete geometric sufficient condition for determinant convergence: convergence of the mass distributions together with control of their first-moment tails.

The obstruction is equally important. Locality has been purchased by a global, cutoff-dependent coordinate change. The original Fourier inclusions change both energy forms by explicit ground-energy corrections, and the reconstructed strings need not extend one another. The computations show severe dependence on the choice of forcing vector and substantial trace mass far from the fixed end. None of the needed tightness estimates is established for the CCM family.

A second, narrower obstruction rules out a tempting shortcut: mixed signs in the CCM rank-one residues prevent realizing that same rational perturbation by one passive boundary coupling to the unchanged free Fourier bath. This does not rule out the reconstructed string, whose uncoupled coordinates are different.

## 2. Sources and the three candidates

Primary sources consulted, with printed equations checked against PDF pages:

- Connes, Consani, Moscovici, [*Zeta Spectral Triples*, arXiv:2511.22755v1](https://arxiv.org/pdf/2511.22755v1): p. 7, (3.14)--(3.18), for the distribution; pp. 15--16, (5.1)--(5.3), for the finite matrix; p. 23, Theorem 5.10, for the conditional quotient operator and determinant. Their unmodified high Fourier modes remain part of the operator. This note uses their finite theorem, not their numerical convergence as a theorem.
- A. Mikhaylov and V. Mikhaylov, [*Inverse problems for finite Jacobi matrices and Krein--Stieltjes strings*, arXiv:2505.06143v1](https://arxiv.org/pdf/2505.06143v1): Section 3, pp. 12--13, (3.2)--(3.4), exhibits diagonal point masses and nearest-neighbor inverse-length couplings. Their evolution uses a negative stiffness matrix; below the stiffness is positive and \(M_s\ddot u+K_su=0\). The isolated slope-jump display for \(l_M\) on p. 13 has a plus sign, inconsistent with its preceding integral definition and smooth negative-Laplacian convention on p. 12. We derive the sign from the energy in (11)--(12). Our free right end also differs from a string fixed at both ends.
- J. Eckhardt, [*Two inverse spectral problems for a class of singular Krein strings*, arXiv:1203.2271v2](https://arxiv.org/pdf/1203.2271v2): p. 8, proof of Theorem 2.4, gives the Dirichlet--Neumann inverse kernel \(\min(x,s)-a\), its first-mass-moment trace, and the associated product. Our finite version and common-strain-space comparison are derived below; an inverse theorem for a singular string is not being silently applied to the CCM cutoffs.
- J. Eckhardt and A. Kostenko, [*The Classical Moment Problem and Generalized Indefinite Strings*, arXiv:1707.08394](https://arxiv.org/pdf/1707.08394): Section 4.1, p. 11, (4.3) and Theorem 4.1, states the correspondence between Herglotz functions and trace-normalized canonical systems. Its positivity assumption concerns the Weyl function, not the unshifted Weil form.

| Candidate | Explicit connection | What it can realize | Assessment |
|---|---|---|---|
| Positive point-mass string, with its graph Hodge--Dirac operator | Congruence of \((M,K)\) to diagonal mass and a tridiagonal spring energy, constructed in Sections 4--5 | Full finite pencil and finite quotient operator; a selected forcing response as well | Selected: explicit local dynamics, variational principle, and (1). Arithmetic locality and compatible cutoff limits remain open. |
| Passive boundary oscillator coupled to the original free Fourier bath | The CCM squared matrix is diagonal minus rank one; compare its secular function with a Schur complement | The same rational perturbation, if its residues have the required sign | Mixed residue signs obstruct this particular model. General boundary-coupled operators with different bulk data are not excluded. |
| Canonical system determined by the mechanical Weyl function | \(m(z)=z\,b^\dagger(K-z^2M)^{-1}b\) is Herglotz | Boundary spectral measure, and all finite frequencies if \(b\) is cyclic | An established inverse-spectral existence route, but its coefficients are less direct than the string's and depend on the port. It supplies no missing arithmetic estimate by itself. |

For the last row, diagonalize the positive pencil to write
\[
m(z)=\sum_j c_j\frac{z}{\omega_j^2-z^2}
=\frac12\sum_jc_j\left(\frac1{\omega_j-z}+\frac1{-\omega_j-z}\right),
\qquad c_j\ge0.
\]
Each term has nonnegative imaginary part in the upper half-plane. Invisible modes have \(c_j=0\); a scalar Weyl function then loses them. The canonical-system correspondence is established literature; choosing this particular CCM port and identifying its Hamiltonian arithmetically would be our proposal. No zeta zeros are prescribed as spectral input to any candidate.

## 3. Finite hypotheses and arithmetic input

Use \(X=\lambda^2>1\), \(L=\log X\), and Fourier cutoff \(N\ge1\). Work in the parity basis of the preceding note. The even and odd spaces have dimensions \(N+1\) and \(N\). The required assumptions are:

1. \(W=W_{L,N}\) is the real symmetric restricted Weil matrix, commuting with reflection and satisfying the CCM divided-difference identity.
2. Its least eigenvalue \(\varepsilon=\varepsilon_{L,N}\) is simple and its eigenvector \(g\) is even. Thus \(T_+=W_+-\varepsilon I\) has kernel \(\mathbb Cg\) and \(T_-=W_--\varepsilon I>0\).
3. The endpoint functional \(\ell\) is nonzero on \(g\); normalize \(\ell g=1\). In the CCM matrix class this is part of the finite mechanism, and it is retained explicitly here.

Set \(d_n=2\pi n/L\), \(R=(0\ \operatorname{diag}(d_n))\), and
\[
J_{0n}=-\frac{\sqrt2}{d_n},\quad J_{nn}=\frac1{d_n},\quad
RJ=I,\quad \ell J=0,
\qquad M=J^\dagger T_+J,\quad K=T_-.
\tag{2}
\]
Indices in \(J\) are \(0\le i\le N\), \(1\le n\le N\); unlisted entries vanish. \(M>0\) because a zero-energy \(Jq\) would belong both to \(\mathbb Cg\) and \(\ker\ell\). Thus \(Kq=\omega^2Mq\) has strictly positive squared frequencies.

Arithmetic enters through \(W\), before any reconstruction. In logarithmic coordinates its prime contribution to the correlation functional is
\[
-\sum_{p^a\le e^L}(\log p)p^{-a/2}\,F(a\log p),
\tag{3}
\]
in addition to the pole and regularized archimedean terms. For the Fourier matrix, \(F\) is the symmetrized correlation of two zero-extended basis functions. The numerical builder includes the archimedean integral beyond the support through its analytic endpoint term. In particular its regularized constant is
\(\tfrac12[\log(4\pi)+\gamma+\log\tanh(L/2)]F(0)\), with the archimedean contribution subtracted. This sign and factor were checked against (3.15), including extension by zero.

The maps \(J,R\) are geometric. All subsequent string coefficients are determined by \(W\), the shift \(\varepsilon\), and the stated port choice. No formula below makes an individual spring correspond to an individual prime. Increasing \(L\) changes the basis, the support, and the set of prime powers in (3); increasing \(N\) at fixed \(L\) changes only the Fourier compression and the chosen ground energy.

The boundary-coordinate quotient is
\[
\mathscr D=\begin{pmatrix}0&M^{-1}K\\I&0\end{pmatrix},\qquad
\|(y,v)\|^2=y^\dagger My+v^\dagger Kv,
\qquad (y,v)\longmapsto[Jy+v].
\tag{4}
\]
Rechecking the weighted adjoint relation gives \(MQ=K\) for
\(Q=R(I-g\ell)R^\dagger\), which verifies (4) without assuming that \(J\) is an isometry.

## 4. Constructing a positive string without fitting its spectrum

Let \(M=AA^\dagger\) be its Cholesky factorization and define
\[
H=A^{-1}KA^{-\dagger}>0.
\]
Choose a nonzero real force \(b\) in the original mechanical coordinates. Our main numerical choice is \(b=e_1\), the first odd Fourier coordinate; a second diagnostic uses \(b=Me_1\), corresponding after whitening to an initial displacement in that coordinate. Put
\(v_1=A^{-1}b/\beta\), \(\beta=\|A^{-1}b\|\).

**Additional one-string hypothesis.** The vectors \(v_1,Hv_1,\ldots,H^{N-1}v_1\) span \(\mathbb R^N\). This cyclicity does not follow just from the simple-even ground state of \(W\). In particular, a positive squared pencil can still have repeated eigenvalues. The code checks nonbreakdown of the multiprecision Lanczos procedure; this is numerical evidence only.

Under cyclicity, orthonormalizing these Krylov vectors, with alternating signs, gives an orthogonal \(U\) such that
\[
C=U^\dagger HU=
\begin{pmatrix}
a_1&-b_1&0&\cdots\\
-b_1&a_2&-b_2&\cdots\\
0&-b_2&a_3&\cdots\\
\vdots&\vdots&\vdots&\ddots
\end{pmatrix}>0,\qquad b_i>0.
\tag{5}
\]
The scalars \(b_i\) in (5) are Jacobi off-diagonal coefficients, distinct from the force vector \(b\). No eigenspectrum is fitted or supplied.

Solve \(r=C^{-1}e_1\), and set \(h=r/r_1\), so \(h_1=1\). Every component of \(r\) is positive: explicitly,
\[
r_i=\frac{(b_1\cdots b_{i-1})\det C_{i+1:N,i+1:N}}{\det C}>0,
\tag{6}
\]
with empty products and determinants equal to one. Define
\[
m_i=h_i^2,\qquad k_1=1/r_1,\qquad
k_{i+1}=b_i h_i h_{i+1},\qquad
\Delta x_i=k_i^{-1},\quad x_i=\sum_{j\le i}\Delta x_j.
\tag{7}
\]
All masses, springs, and lengths are positive. Let \(D_h=\operatorname{diag}(h_i)\), and let \(B\) be the anchored incidence matrix:
\((Bu)_1=u_1\), \((Bu)_i=u_i-u_{i-1}\) for \(i>1\). Then
\[
M_s=D_h^2,\qquad K_s=B^\dagger\operatorname{diag}(k_i)B
=D_hCD_h.
\tag{8}
\]
To check the diagonal entries, use \(Ch=e_1/r_1\). For an interior row it says \(a_ih_i=b_{i-1}h_{i-1}+b_ih_{i+1}\); the first row supplies \(k_1\), and the last has no spring beyond the last bead.

The explicit configuration map is
\[
q=Su,\qquad S=A^{-\dagger}UD_h,
\qquad S^\dagger MS=M_s,\quad S^\dagger KS=K_s.
\tag{9}
\]
This is an exact congruence of both energies. It also preserves the chosen port:
\[
S^\dagger b=\beta e_1,\qquad
b^\dagger(K-tM)^{-1}b
=\beta^2 e_1^\dagger(K_s-tM_s)^{-1}e_1.
\tag{10}
\]
The normalization \(h_1=1\) fixes the first bead mass to one. Multiplying \(h\) by \(c>0\), and multiplying the right side of its defining equation by \(c\), instead multiplies every mass and spring by \(c^2\), divides every length by \(c^2\), and leaves all frequencies and \(\sum m_ix_i\) unchanged. Comparisons of geometric coefficients require a fixed convention.

If cyclicity fails, the completed Krylov space is invariant under symmetric \(H\); its orthogonal complement is invariant too. Restart there with a nonzero vector and repeat. Each irreducible block yields (7)--(9), including one-bead blocks. The result is a disjoint union of strings with the full finite spectrum and multiplicities. The original port only observes its first block. A single connected scalar string cannot represent repeated eigenvalues: the three-term recurrence makes each eigenspace at most one-dimensional.

## 5. State spaces, boundary conditions, and the graph Dirac map

The string Hilbert space is
\[
\mathcal H_s=L^2(\mu)=\mathbb C^N,
\quad \langle u,v\rangle_\mu=\sum_i m_i\overline{u_i}v_i,
\quad \mu=\sum_i m_i\delta_{x_i}.
\]
Its operator \(L_s=M_s^{-1}K_s\) has domain all of \(\mathbb C^N\). It is self-adjoint in this inner product. The mechanical phase space is \(\mathbb R^N\times\mathbb R^N\), with conserved energy
\[
E_s(u,\dot u)=\frac12\sum_i m_i|\dot u_i|^2
 +\frac12\sum_i k_i|u_i-u_{i-1}|^2,
\qquad u_0=0.
\tag{11}
\]

For a differential interpretation, choose any massless terminal interval \((x_N,R_s)\), \(R_s>x_N\), interpolate affinely between the beads, impose \(u(0)=0\) and \(u'(R_s)=0\), and continue constantly after \(x_N\). The distributional eigenproblem is
\[
-u''=t\,u\,\mu,\qquad
u'(x_i+)-u'(x_i-)=-t m_i u(x_i).
\tag{12}
\]
These conditions give precisely \(K_su=tM_su\). The affine interpolation is the energy-minimizing representative of the values at the beads. Thus the energy is \(\int|u'|^2ds\); the terminal interval adds no energy and no degree of freedom. This formulation avoids ambiguous endpoint atoms or an unstated boundary condition at the last mass.

For a differential geometer, the first-order operator is a discrete Hodge--Dirac operator on nodes and edges. In ordinary orthonormal coordinates set
\[
d_s=\operatorname{diag}(\sqrt{k_i})BD_h^{-1},\qquad
D_s=\begin{pmatrix}0&d_s^\dagger\\d_s&0\end{pmatrix}
\quad\hbox{on }\mathbb C^N\oplus\mathbb C^N.
\tag{13}
\]
Its domain is the whole finite space. It is self-adjoint and odd for the node/edge grading, with \(d_s^\dagger d_s=C\). Anchoring the first node removes the constant cochain and makes \(d_s\) invertible; there is no finite zero mode.

The required unitary map from (4), rather than an unspecified isospectrality, is
\[
\mathcal U(y,v)=
\big(U^\dagger A^\dagger y,\ d_sU^\dagger A^\dagger v\big).
\tag{14}
\]
Using \(AUCU^\dagger A^\dagger=K\), one obtains
\(\|\mathcal U(y,v)\|^2=y^\dagger My+v^\dagger Kv\), and direct multiplication gives
\(\mathcal U\mathscr D=D_s\mathcal U\).

Adjoining the unchanged Fourier tail yields a unitary realization of the **full spectral operator at this fixed pair \((L,N)\)**. The tail domain is
\[
\{(a_n)_{|n|>N}:\sum_{|n|>N}d_n^2|a_n|^2<\infty\},
\quad (a_n)\mapsto(d_na_n).
\]
This is not a realization of the full spectral triple: no algebra action or commutator condition has been transported or identified geometrically. In particular multiplication on the original circle does not automatically descend to its quotient by \(g\).

## 6. What locality buys: variational and trace identities

The lowest *mechanical* squared frequency has the local Rayleigh principle
\[
\omega_1^2=\min_{u\ne0}
\frac{\sum_i k_i|u_i-u_{i-1}|^2}{\sum_i m_i|u_i|^2}.
\tag{15}
\]
Since \(u_i=\sum_{j\le i}(u_j-u_{j-1})\), Cauchy--Schwarz gives
\[
|u_i|^2\le x_i\sum_j k_j|u_j-u_{j-1}|^2,
\quad
K_s\succeq\frac{M_s}{\sum_i m_ix_i},\quad
\omega_1^2\ge\frac1{\sum_i m_ix_i}.
\tag{16}
\]
The exact inverse is even more useful:
\[
(K_s^{-1})_{ij}=\min(x_i,x_j).
\tag{17}
\]
Proof: \(B^{-1}\) sums increments; hence
\(K_s^{-1}=B^{-1}\operatorname{diag}(\Delta x_i)B^{-\dagger}\). Taking its mass-weighted trace proves (1). All entries of \(K_s^{-1}M_s\) are strictly positive; its Perron eigenvector is the simple lowest mechanical mode and can be chosen strictly positive on the beads. This is a property of the reconstructed dynamics. It does not prove simplicity, parity, or sign of the original Weil ground energy: that ground vector has already been quotiented out.

For an ambient energy space independent of the number of beads, put \(v_x=1_{(0,x)}\) in \(\mathcal E=L^2(0,\infty;ds)\), and define
\[
Z_\mu:\mathbb C^N\longrightarrow\mathcal E,
\qquad Z_\mu a=\sum_i\sqrt{m_i}a_i v_{x_i}.
\]
Then
\[
Z_\mu^\dagger Z_\mu=M_s^{1/2}K_s^{-1}M_s^{1/2},
\quad Z_\mu Z_\mu^\dagger=\mathcal C_\mu,
\quad \|Z_\mu\|_{HS}^2=\sum_i m_ix_i.
\tag{18}
\]
The first matrix is unitarily equivalent to the inverse of the mass-normalized string operator. Its nonzero spectrum equals that of \(\mathcal C_\mu\), so
\[
\boxed{P_{L,N}(z):=\frac{\det(K-z^2M)}{\det K}
=\det_{\mathcal E}(I-z^2\mathcal C_{\mu_{L,N}}).}
\tag{19}
\]
This is a Fredholm determinant of a positive finite-rank operator on a common space, not a claim that the finite CCM Hilbert spaces already embed compatibly. For multiple strings, use a direct sum of strain spaces and sum the mass moments.

## 7. A conditional geometric convergence criterion

**Proposition.** Choose connected string realizations with a specified port and length/mass normalization along a sequence \((L_j,N_j)\). Suppose their finite positive measures \(\mu_j\) converge weakly on \([0,\infty)\) to a finite positive measure \(\mu\), their total masses are uniformly bounded, and
\[
\lim_{R\to\infty}\sup_j\int_{(R,\infty)}x\,d\mu_j(x)=0.
\tag{20}
\]
Then \(\int x\,d\mu<\infty\), \(\mathcal C_{\mu_j}\to\mathcal C_\mu\) in trace norm, their traces converge, and \(P_{L_j,N_j}\) converges locally uniformly to \(\det(I-z^2\mathcal C_\mu)\). In particular a common bounded support together with weak convergence suffices. An atom at zero contributes zero to \(\mathcal C_\mu\).

Here weak convergence means against bounded continuous functions. The explicit mass bound is included to emphasize its role, although it also follows from this notion of weak convergence for finite measures. This proposition supplies a sufficient condition; it has **not** been verified for the CCM strings.

**Proof.** For \(x,y\ge0\), the rank-one trace norm inequality gives
\[
\big\||v_x\rangle\langle v_x|-|v_y\rangle\langle v_y|\big\|_1
\le(\sqrt{x}+\sqrt{y})\sqrt{|x-y|}.
\tag{21}
\]
The map into trace-class operators is norm-continuous on every compact interval and vanishes at zero. Approximate it there uniformly by a finite sum of continuous scalar functions times fixed rank-one operators. Weak convergence and the mass bound give convergence of these integrals in trace norm. Use a continuous spatial cutoff, then (20) and
\(\||v_x\rangle\langle v_x|\|_1=x\) to remove the cutoff. The same truncation argument gives the finite first moment of \(\mu\) and convergence of traces.

For completeness, determinant convergence does not require an unproved change of domains. For positive trace-class operators converging in trace norm, the positive eigenvalues converge coordinatewise and their sums converge. Thus the eigenvalue lists converge in \(\ell^1\): truncate at a fixed index, then bound both tails by their convergent sums. Telescoping the finite products and using \(|1-z^2a|\le e^{|z|^2a}\) proves uniform convergence on each disk, then the same estimate removes the infinite product tails. This proves the determinant assertion. \(\square\)

A quantitative special case makes the geometric content clear. For equal total mass \(m\), measures supported in \([0,R]\), and any coupling \(\pi\) of them,
\[
\|\mathcal C_\mu-\mathcal C_\nu\|_1
\le2\sqrt R\,\sqrt{m\int|x-y|\,d\pi(x,y)}.
\tag{22}
\]
Integrate (21) and apply Cauchy--Schwarz. It controls inverse dynamics by movement of the reconstructed mass, without requiring atom positions to coincide exactly.

Both restrictions matter. Positive mechanics alone gives no uniform trace bound: a one-bead system with \(M=r\), \(K=1\) has trace \(r\), arbitrarily large. Weak convergence on an unbounded interval is insufficient even when the traces stay bounded: \(\mu_j=j^{-1}\delta_j\) converges weakly to zero and has mass at most one, but \(\operatorname{tr}\mathcal C_{\mu_j}=1\) and its determinant is always \(1-z^2\). Its first moment escapes to infinity and violates (20). These are explicit controls for the scope of the proposition.

There is also no identification with \(\Xi\) in this proposition. It produces the determinant of whatever limiting mass distribution the arithmetic construction actually supplies.

## 8. The two cutoffs, moving energy, and the free tail

At fixed \(L\), let \(P:E_n\to E_N\), \(n<N\), be the coordinate inclusion (and use the analogous parity inclusions). Fourier compression gives \(P^\dagger W_NP=W_n\). Set
\(\delta=\varepsilon_{L,n}-\varepsilon_{L,N}\ge0\), by the ordinary min--max principle for \(W\). Since the columns of \(J_n\) are the corresponding columns of \(J_N\),
\[
\boxed{P_-^\dagger K_NP_-=K_n+\delta I,\qquad
P_-^\dagger M_NP_-=M_n+\delta J_n^\dagger J_n.}
\tag{23}
\]
Thus the natural Fourier inclusion is not an isometry for either shifted energy when \(\delta>0\). This is an exact obstruction to interpreting these particular inclusions as Galerkin restrictions of one fixed pencil. It does not exclude a different embedding or a convergent renormalization.

For a fixed nonzero old vector \(q\), set \(m=q^\dagger M_nq\), \(j=\|J_nq\|^2\), \(c=\|q\|^2\), and \(\rho=q^\dagger K_nq/m\). Its restricted new Rayleigh quotient obeys
\[
\rho_N(q)-\rho
=\frac{\delta(c-\rho j)}{m+\delta j}.
\tag{24}
\]
It moves toward the geometric quotient \(c/j\). There is no universal sign, and a tiny \(\delta\) need not be negligible relative to a very small \(m\). Ordinary interlacing or monotone-extension arguments for a single fixed string therefore need an additional justification. Nor does the abstract embedding of (18) imply that the ranges of successive \(Z_\mu\)'s are nested.

At variable support, even (23) is unavailable without identifying the different intervals and bases; \(L\), \(X=e^L\), and the arithmetic coefficients all change. The physical string length \(x_N\) is a different quantity from \(L\).

The normalized **full** spectral function retains the free tail:
\[
F_{L,N}(z)=P_{L,N}(z)\prod_{n>N}\left(1-\frac{L^2z^2}{4\pi^2n^2}\right),
\quad
\tau_{L,N}=\int x\,d\mu_{L,N}(x)
 +\frac{L^2}{4\pi^2}\sum_{n>N}n^{-2}.
\tag{25}
\]
In particular \(|F_{L,N}(z)|\le e^{\tau_{L,N}|z|^2}\). At fixed \(L\) the tail tends to one. If \(N\to\infty\), \(L\to\infty\), and \(L^2/N\to\alpha<\infty\), its limit is
\[
\exp[-\alpha z^2/(4\pi^2)].
\tag{26}
\]
Indeed the quadratic logarithmic coefficient converges as stated and the fourth-order remainder is \(O_R(L^4/N^3)\to0\) on each fixed disk. The first free tail frequency tends to infinity under this hypothesis. Combining the proposition with this scaling gives the full limit
\(\det(I-z^2\mathcal C_\mu)e^{-\alpha z^2/(4\pi^2)}\), not an automatic \(\Xi\) limit. If \(L^2/N\) is unbounded, the free tail alone precludes a uniform bound on \(\tau\). A nonvanishing Gaussian preserves zeros while changing the determinant's Taylor data.

Finally \(W\mapsto W+cI\), \(\varepsilon\mapsto\varepsilon+c\) leaves (2), the entire reconstruction, and all these estimates unchanged. None fixes the original sign of \(\varepsilon\).

## 9. Why the original Fourier bath need not be passive

In boundary coordinates,
\[
Q=M^{-1}K=\operatorname{diag}(d_n^2)-u v^\dagger,
\quad u_n=d_ng_n,\quad v_n=\sqrt{2/L}\,d_n,
\tag{27}
\]
where \(g_n\), \(n\ge1\), are even-basis coordinates with \(\ell g=1\). The determinant lemma gives
\[
\frac{\det(Q-tI)}{\prod_n(d_n^2-t)}
=1-\sum_n\frac{r_n}{d_n^2-t},\qquad
r_n=\sqrt{2/L}\,d_n^2g_n.
\tag{28}
\]
A real self-adjoint rank-one update of this fixed free bath has the form
\(\operatorname{diag}(d_n^2)+\sigma aa^\dagger\); its corresponding coefficients in (28) all have one sign. The same sign constraint on the bath residues holds when eliminating positive-metric bath coordinates coupled through a single port of an additional oscillator: its Schur complement is
\(\kappa-tm-\sum_n|a_n|^2/(d_n^2-t)\). A constant or linear term cannot repair mixed residues at the fixed poles.

**Finite obstruction.** If two nonzero \(r_n\)'s have opposite signs, neither of these passive, fixed-bath secular realizations produces (28). Equivalently, a positive diagonal metric cannot symmetrize (27): off-diagonal symmetry would require
\(w_i u_i/v_i=w_j u_j/v_j\) for all \(i\ne j\), impossible with mixed signs and \(w_i>0\).

Another easy diagnostic is interlacing. For a positive self-adjoint rank-one update, the smallest squared eigenvalue is at most \(d_2^2\) when \(N\ge2\): restrict the Rayleigh quotient to the nonzero intersection of \(\operatorname{span}(e_1,e_2)\) with \(a^\perp\). A negative update has smallest eigenvalue at most \(d_1^2\). Therefore \(\omega_1>d_2\) excludes both signs. This argument is a finite min--max proof, not an appeal to numerical folklore.

The scope is deliberately narrow. CCM's positive metric is dense, and (27) is not self-adjoint in the ordinary Fourier metric. Coupled boundary systems with more variables, a changed bulk operator, or a changed metric can evade this obstruction. The positive string of Section 4 is one such changed-coordinate realization.

An exact nonarithmetic control shows this distinction without floating point:
\[
M_0=\begin{pmatrix}41&60\\60&89\end{pmatrix},\quad
K_0=\begin{pmatrix}481&680\\680&976\end{pmatrix},\quad
M_0^{-1}K_0=\begin{pmatrix}41&40\\-20&-16\end{pmatrix}
=\operatorname{diag}(1,4)-\binom{-40}{20}(1\ \ 1).
\]
The positive leading minors and determinants \(\det M_0=49\), \(\det K_0=7056\) prove positivity; the squared frequencies are 9 and 16. The residues have opposite signs and the first squared frequency exceeds the second free pole. Thus positive mechanical energy and the fixed-bath obstruction coexist. This example is not claimed to be an arithmetic Weil matrix.

## 10. Reproducible numerical checks

[The new program](../numerics/check_string_realization.py) imports the preserved Weil-distribution builder, recomputes \(W\), and constructs both port choices. It never evaluates zeta zeros. It checks both congruences, the graph Dirac intertwiner and metric, the Green kernel, the trace identity, the port response, the determinant in strain coordinates, (23)--(24), and the rank-one formula. Synthetic controls include a genuinely passive interlacing update, an arbitrarily soft positive oscillator, and the escaping-mass example above.

The runs use \(X=2,5,13\), with \(N=4,8\) and a fixed-support sequence \(X=13\), \(N=8,12,16\). They recompute the complete sequence at 120 and 160 decimal digits. Each \(X\) is assembled at its largest required cutoff and compressed for the smaller cases, exactly matching the identity under test. No parameter is selected to fit a zeta zero.

The [120-digit record](../numerics/records/string_realization_120_20260926.json), [160-digit record](../numerics/records/string_realization_160_20260926.json), and [hash-checked comparison](../numerics/records/string_precision_comparison_20260926.json) retain the results. All 504 numerical observables agree at all 45 saved significant digits. The maximum scaled reconstruction residuals are below \(8.85\times10^{-92}\) and \(2.20\times10^{-130}\), respectively. The following geometric observations are not convergence theorems:

- At \(X=2,N=4\), the residues in (28) all have the same sign; this is a useful control against an overbroad obstruction.
- At \(X=5,N=8\) and every tested \(X=13\) cutoff, residues have mixed signs and \(\omega_1>d_2\). The passive fixed-bath shortcut fails both diagnostics.
- With the force port and first bead mass one, string lengths for \(X=13\), \(N=8,12,16\) are approximately \(9.15\times10^{12}\), \(2.08\times10^{20}\), \(6.72\times10^{25}\). The fractions of the inverse-square trace beyond string coordinate \(10^6\) are approximately 0.633, 0.753, 0.846. These cutoffs do not demonstrate the required tightness.
- Replacing the port by \(Me_1\) changes those lengths to approximately 119.5, 16898, and \(1.99\times10^6\), while preserving the full spectrum and trace. This shows why string length alone is not a spectral invariant or an arithmetic explanation. Rescaling all lengths also cannot change \(\sum m_ix_i\).
- The first Jacobi diagonal at fixed \(X=13\) increases by factors about 2.73 and 2.06 across those two cutoff steps. These particular normalized Jacobi matrices are not successive principal truncations of one Jacobi matrix. Finite observations do not prove that their coefficients cannot converge after another choice or normalization.

All these are observations from finite, ill-conditioned matrices. The original simple-even hypothesis and cyclicity were observed at the tested precision, not certified or proved for arbitrary cutoffs.

## 11. Claim ledger and next investigation

| Claim | Exact status | Missing input |
|---|---|---|
| Positive strings and graph Dirac realize the finite CCM operator | Proved under finite CCM assumptions; one connected string additionally needs a cyclic port, otherwise use a direct sum | Uniform CCM simple-even hypothesis; a preferred arithmetic port |
| Trace equals the first string mass moment; coercivity (16); determinant (19) | Proved finite identities/inequality | A bound on that moment from arithmetic, uniform along the intended two-cutoff sequence |
| Weak mass convergence with (20) controls the determinant | Proved conditional proposition on a common strain space | Verify its mass and tail assumptions for a normalized CCM family, then identify the resulting determinant arithmetically |
| Natural Fourier inclusions are not fixed-energy embeddings when \(\delta>0\) | Exact identity (23) and its consequence | A different compatible embedding or quantitative control of the defect |
| Mixed residues obstruct one passive coupling to the fixed Fourier bath | Proved finite obstruction; mixed signs observed numerically | A theorem on those signs if a uniform obstruction is wanted |
| Original Weil positivity, a continuum spectral triple, or convergence to \(\Xi\) | Not established | Absolute ground energy, domains/algebra, and arithmetic identification respectively |

**Concrete next investigation.** Work first at fixed \(L=\log13\), before varying support. Compare port choices generated directly by the arithmetic energy (starting with \(b=Me_1\) and a fixed smooth odd profile), fixing the length/mass scaling before comparison. Derive or disprove a bound on
\(\int_{x>R}x\,d\mu_{L,N}(x)\) uniform in \(N\), alongside a total-mass bound. The low-cost preliminary diagnostic is to increase precision and \(N\) while recording this tail, not just the first frequency. A successful bound would verify a genuinely new hypothesis of Section 7; failure would identify which port or embedding needs to change. Support growth and the free tail in (25) would remain a separate subsequent problem.
