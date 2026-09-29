# CCM prime jumps: the prescribed resistance construction fails

Date: 26 September 2026.

Model: GPT-6 (Codex). Exact deployed variant and configured reasoning-effort level are not exposed in this session; neither is inferred from the task's difficulty.

Status: continuation of the [resistance-form investigation](CCM_RESISTANCE_FORMS_AND_CHANGING_FRACTALS_20260926.md), with one analytic obstruction, finite arithmetic computations, and a same-agent critical review. No priority claim is made. These results neither prove RH nor exclude all possible resistance realizations of the CCM pair.

## 1. Outcome of the proposed next experiment

The initial note proposed testing prime-power edges against **both** CCM forms at fixed support length \(L=\log 13\), with Fourier cutoffs \(N=4,8,16\). That experiment has now been performed for a specified, spectrum-independent logarithmic-coordinate interpretation.

It fails in three separate ways:

1. With nodal values obtained by evaluating the odd Fourier field on nested dyadic nodes, the uniquely required stiffness has positive off-diagonal entries and negative grounding row sums. It is not the trace energy of a positive-conductance grounded graph on those vertices.
2. The required nodal mass has negative entries. It cannot be the Gram matrix of nonnegative harmonic coordinate functions against a positive measure. More intrinsically, the actual CCM mass fails a pointwise sine-product identity satisfied by **every** measure in the unchanged logarithmic sine representation.
3. Algebraic energy-minimizing extensions between these nodal spaces preserve neither prescribed coarse form and do not compose. Their coefficients also violate the maximum principle for positive resistance networks.

The inverse-frequency traces increase, and the finite inverse spectra pass the necessary compression-interlacing tests. Thus neither of these basis-independent diagnostics supplies an obstruction for this sample. Passing them is insufficient to establish a geometric embedding.

There is also an analytic explanation, independent of the numerical cutoffs: prime jumps crossing the reflection midpoint give **positive** cross energy between disjoint, nonnegative functions on the folded half interval. An explicit example remains positive after including the pole and archimedean contributions, for every scalar ground shift. Consequently the full odd Weil form, in these pointwise half-interval coordinates, is not a scalar Markov energy.

The earlier compact tree and conditional resistance-trace theorems survive review. The direct arithmetic bridge proposed for testing does not.

## 2. Fixed arithmetic data and the geometric map being tested

Write \(t\in[0,L]\), \(d_n=2\pi n/L\), and use real odd functions
\[
\phi_n(t)=\sqrt{2/L}\sin(d_nt),\qquad
\Phi_Nq=\sum_{n=1}^N q_n\phi_n(t).
\]
These differ by a common unit-modulus factor from the imaginary odd basis of the founding mechanical derivation, so its real Gram matrices are unchanged. Reflection is \(t\mapsto L-t\), and the half interval is \([0,L/2]\).

The input pair remains
\[
K_N=W_{-,N}-\varepsilon_N I,\qquad
M_N=J_N^T(W_{+,N}-\varepsilon_N I)J_N,
\]
\[
(J_Nq)_0=-\sqrt2\sum_{n=1}^Nq_n/d_n,\qquad
(J_Nq)_n=q_n/d_n.
\]
The simple-even minimum and nonzero ground boundary value are checked numerically for each case, not assumed proved for all cutoffs. At \(N=16\), the observed parity gap is approximately \(8.61\times10^{-32}\) and the least mass eigenvalue approximately \(9.92\times10^{-37}\). Ordinary machine precision would be inadequate.

For the vertices, take the first \(N\) base-two radical inverses \(v_j\): reverse the binary digits of \(j\), and divide by \(2^{\text{number of digits}}\). Thus
\[
(v_1,v_2,v_3,v_4,v_5,\ldots)
=(1/2,1/4,3/4,1/8,5/8,\ldots),\qquad t_j=Lv_j/2.
\]
The vertex sets are genuinely nested at \(4,8,16\). They are fixed before constructing any Weil matrix. The set with \(N=2^k\) consists of the interior dyadic grid of denominator \(2^k\), plus the next inserted point; it is not claimed to be a uniform finite-difference grid.

Let \(B_{N,jn}=\phi_n(t_j)\), so nodal values are \(u=B_Nq\). The matrices forced by both Gram identities are
\[
K_N^{\mathrm v}=B_N^{-T}K_NB_N^{-1},\qquad
M_N^{\mathrm v}=B_N^{-T}M_NB_N^{-1}.                 \tag{2.1}
\]
They are unique for this invertible map. Invertibility follows from
\(\sin(n\theta)=\sin\theta\,U_{n-1}(\cos\theta)\): evaluation at distinct points of \((0,\pi)\) gives a polynomial Vandermonde matrix times nonzero diagonal factors. The computed Frobenius condition products \(\|B_N\|_F\|B_N^{-1}\|_F\) are approximately \(5.26,10.85,22.13\).

Testing (2.1) as a **graph trace energy with harmonic vertex lifts** is stricter than asking for arbitrary Galerkin subspaces of an unknown resistance system. Positive off-diagonals can occur in a sign-changing Galerkin basis. The finite sign test is not used to exclude that broader possibility.

## 3. The prime, pole, and archimedean terms remain separate

The signed decomposition used is
\[
W=W^{\rm pole}+W^{\rm arch}+W^{\rm prime},\qquad
W^{\rm prime}=-\sum_{p^m\le13}(\log p)p^{-m/2}q(\log p^m).
\]
The normalization and signs follow from [CCM, equations (3.13)–(3.18) and (4.2)–(4.3)](https://arxiv.org/html/2511.22755v1). The full matrix is rebuilt with the preserved neighboring Weil-quadrature program. The prime part is evaluated directly from its finite sum; the pole part uses its closed rank-two formula; the signed archimedean part is the remainder. The endpoint term \(p^m=13\) has zero correlation but is retained in the jump-energy offset.

For \(C=\sum_{p^m\le13}(\log p)p^{-m/2}\),
\[
G^{\rm prime}=W^{\rm prime}+2CI\succeq0,
\]
because, on zero-extended full-line functions,
\[
\langle f,G^{\rm prime}f\rangle
=\sum_{p^m\le13}(\log p)p^{-m/2}\|f-U_{\log p^m}f\|_2^2.
\]
This positive-semidefinite control passes. It does **not** make its compression to odd fields a Markov form on the half interval. Section 6 proves the distinction explicitly.

The records keep the separate contributions to the largest positive nodal stiffness entry and to the sine-mass defect. For example, at \(N=8\), the stiffness witness at vertex pair \((3,6)\) is approximately
\[
0.25006975\quad\text{(prime)}
-0.01356876\quad\text{(pole)}
-0.05001537\quad\text{(archimedean)}
+9.95\times10^{-25}\quad\text{(shift)}
=0.18648561.
\]
At the largest-entry witnesses for \(N=4\) and \(N=16\), the positive contribution instead comes from the archimedean nodal matrix. No claim is made that every finite nodal sign defect is caused by one prime edge; Fourier interpolation itself affects individual entries.

## 4. Finite stiffness and mass obstructions

For a grounded graph with nonnegative conductances, stiffness in vertex values satisfies
\[
K_{ij}^{\mathrm v}=-c_{ij}\le0\quad(i\ne j),\qquad
\sum_jK_{ij}^{\mathrm v}=c_{i,o}\ge0.
\]
These conditions also hold for its harmonic trace after interior vertices are eliminated. The positive-stiffness convention is opposite to the generator convention in [Kigami, Definitions 2.1–2.2 and Proposition 2.6](https://www-an.acs.i.kyoto-u.ac.jp/~kigami/ulcg.pdf).

For a positive mass measure supported just at the retained vertices, \(M^{\mathrm v}\) must be diagonal. Allowing mass in a larger resistance space weakens this to a necessary entrywise sign condition for harmonic coordinates:
\[
M_{ij}^{\mathrm v}=\int h_i h_j\,d\mu\ge0,
\]
because the grounded harmonic coordinate functions \(h_i\) are nonnegative by the maximum principle. All three cases violate even this weaker condition.

| \(N\) | Largest off-diagonal \(K_N^{\mathrm v}\) | Smallest row sum of \(K_N^{\mathrm v}\) | Smallest off-diagonal \(M_N^{\mathrm v}\) | \(\operatorname{tr}(K_N^{-1}M_N)\) |
|---:|---:|---:|---:|---:|
| 4 | \(0.00252180384\) | \(-0.0104531657\) | \(-0.0000725069464\) | \(0.008234664362\) |
| 8 | \(0.186485613\) | \(-0.275299895\) | \(-0.00140873009\) | \(0.011479982567\) |
| 16 | \(0.499656232\) | \(-0.361116243\) | \(-0.000773251405\) | \(0.014390758152\) |

These are multiprecision diagnostics, not certified interval bounds. They are well separated from numerical residuals and agree between the independent precision runs.

### A mass test that does not depend on the dyadic vertices

If the unchanged sine field had any measure representation
\[
M_{ij}=\int\phi_i(t)\phi_j(t)\,d\mu(t),
\]
then the pointwise identity
\[
\phi_2^2=\phi_1^2+\phi_1\phi_3
\]
would force
\[
\boxed{D(M):=M_{22}-M_{11}-M_{13}=0.}                       \tag{4.1}
\]
The requirement holds for singular and atomic measures, indeed even for signed measures whenever the integrals exist. Changing the underlying metric, restricting to a fractal support, changing coordinates, or multiplying every basis function by the same scalar field preserves this product identity. Thus none of those changes alone can fix a nonzero defect while retaining these pointwise functions.

The computed defects are
\[
\begin{array}{c|c}
N&D(M_N)\\\hline
4&-2.8491024897733315774\times10^{-7}\\
8&-2.8491025368197846922\times10^{-7}\\
16&-2.8491025368197850653\times10^{-7}.
\end{array}
\]
The defect is about \(2.178\%\) of the largest absolute matrix entry appearing in (4.1), not a tiny relative perturbation of those entries. Its separate arithmetic contributions substantially cancel, which is another reason to use multiprecision.

Its cutoff dependence has an exact explanation. With \(d_1=2\pi/L\),
\[
D(J_N^TJ_N)=-\frac{35}{12d_1^2},\qquad
D(M_N)=D_0+\frac{35\varepsilon_N}{12d_1^2},\quad N\ge3,      \tag{4.2}
\]
where \(D_0\) uses only the same unshifted even modes \(0,1,2,3\). Rayleigh–Ritz gives \(\varepsilon_{N'}\le\varepsilon_N\), hence \(D(M_{N'})\le D(M_N)\). Therefore a future interval certificate for the single sign \(D(M_4)<0\) would exclude this measure interpretation for every higher cutoff for which the pair is formed. The current finite records do not claim to be that certificate.

Equation (4.1) concerns the field \(\Phi_Nq\). A different map, for example using the even integrated field \(J_Nq\), has different product identities and is not ruled out by (4.1).

## 5. Refinement and its positive controls

For each pair \(n<m\), order the fine vertices so the first \(n\) are the retained ones, as above, and partition
\[
K_m^{\mathrm v}=\begin{pmatrix}A&B\\B^T&C\end{pmatrix}.
\]
Since the matrix is positive definite, its algebraic minimizer is well-defined:
\[
H_{n,m}=\begin{pmatrix}I\\-C^{-1}B^T\end{pmatrix}.
\]
It is the unique static extension minimizing this specified fine energy for the fixed boundary values, even though that energy is not a resistance-network trace.

The required compatibility identities are
\[
H_{n,m}^TK_m^{\mathrm v}H_{n,m}=K_n^{\mathrm v},\qquad
H_{n,m}^TM_m^{\mathrm v}H_{n,m}=M_n^{\mathrm v},\qquad
H_{8,16}H_{4,8}=H_{4,16}.                                  \tag{5.1}
\]
Define a relative defect by \(\|A-B\|_F/\max(\|A\|_F,\|B\|_F)\). The stiffness/mass defects are respectively

| Refinement | Stiffness defect | Mass defect | Smallest extension coefficient |
|---|---:|---:|---:|
| \(4\to8\) | 0.999917435 | 0.999988189 | \(-54.3087\) |
| \(8\to16\) | 0.999901653 | 0.999987624 | \(-21.6134\) |
| \(4\to16\) | 0.999999999985 | 0.999999999999 | \(-4704.20\) |

The composition defect is approximately \(0.989938331\). These are failures of exact compatibility, not approximation rates. Negative and greater-than-one coefficients also violate the grounded harmonic maximum principle.

Several controls prevent confusing this failure with a broken implementation:

- A positive grounded three-edge path, using the **same** harmonic-extension routine, preserves both its energy and a pulled-back positive mass through successive reductions, with composable maps.
- An arbitrary positive atomic sine mass satisfies (4.1) to the working precision.
- The full-line prime jump Gram matrix is positive.
- Both original Fourier-compression identities hold, with defects exactly explained by \(\varepsilon_n-\varepsilon_m\). These identities are checked separately from the failed nodal Schur identities.
- Necessary interlacing of inverse squared frequencies passes: if \(\mu_1\ge\cdots\ge\mu_N\) are the eigenvalues of \(K_N^{-1/2}M_NK_N^{-1/2}\), then \(\mu_i^{(m)}\ge\mu_i^{(n)}\ge\mu_{i+m-n}^{(m)}\) in all three comparisons. Passing this finite spectral test does not construct arithmetic maps.

The monotone trace values in §4 therefore must be reported as a **passing necessary test**, alongside the failed prescribed construction. They do not justify the common-space assumptions of the preceding note's convergence theorem.

## 6. Analytic obstruction: odd folding loses the Markov property

This section is an independent proof, not an extrapolation of the nodal matrix signs.

For a real function \(f\) on \((0,L/2)\), define its odd lift
\[
(Of)(t)=\begin{cases}f(t),&0<t<L/2,\\-f(L-t),&L/2<t<L,\end{cases}
\]
and extend by zero outside \([0,L]\). On compactly supported piecewise-linear functions, the Weil form is finite. For any real scalar \(s\), set
\[
\mathcal E_s(f,g)=QW(Of,Og)-s\langle Of,Og\rangle_{L^2(0,L)}.
\]
This is the continuum pointwise interpretation of the shifted odd stiffness; it does not presuppose a global ground-state theorem.

**Proposition.** At \(L=\log13\), no scalar shift \(s\) makes \(\mathcal E_s\) a Markov form on the half interval. In particular it cannot be a grounded scalar resistance form in these coordinates.

**Proof.** A real Markov form satisfies \(\mathcal E(f,g)\le0\) for disjoint nonnegative functions in its domain: apply the absolute-value contraction to \(f-g\), whose absolute value is \(f+g\).

Let \(a=\log2\), \(h=1/100\),
\[
t_0=(L-a)/2-1/10,\qquad s_0=(L-a)/2+1/10,
\]
and \(\psi(y)=(1-|y|)_+\). Take
\[
f(t)=\psi((t-t_0)/h),\qquad g(t)=\psi((t-s_0)/h).
\]
Their supports lie strictly inside the half interval and are disjoint. The odd lifts also have disjoint supports, so the scalar shift contributes zero for every \(s\).

The direct distances between the half-interval supports lie in \([0.18,0.22]\), below the smallest prime delay. The reflected distances lie in \([a-0.02,a+0.02]\), containing only the delay \(a=\log2\). That jump couples a positive copy of one tent to a negative reflected copy of the other. Its contribution is
\[
\mathcal E^{\rm prime}(f,g)
=2\frac{\log2}{\sqrt2}\int f(t)g(L-a-t)\,dt
=\frac{4\log2}{3\sqrt2}h.                                 \tag{6.1}
\]
The remaining smooth off-diagonal kernel, directly from the pole and archimedean distributions, is
\[
A(r)=2\cosh(r/2)-\frac{e^{r/2}}{2\sinh r},\quad r>0.
\]
Regularization terms at zero and the archimedean tail are multiples of \(\langle Of,Og\rangle=0\), so none were omitted in writing
\[
\mathcal E^{\rm smooth}(f,g)
=2\iint f(t)g(u)\{A(|t-u|)-A(L-t-u)\}\,dt\,du.             \tag{6.2}
\]
All distances in this integral belong to \([0.18,0.72]\). On that interval,
\[
|A(r)|\le 2\cosh(0.36)+\frac{e^{0.36}}{2\sinh(0.18)}<8.
\]
For elementary rational bounds, use \(e^{0.36}<3/2\), \(2\cosh(0.36)<3\), and \(2\sinh(0.18)>9/25\), giving \(3+25/6<8\). The exponential inequality follows, for example, by bounding the Taylor tail with \(n!\ge2\cdot3^{n-2}\) for \(n\ge2\). Since each tent integrates to \(h\),
\[
|\mathcal E^{\rm smooth}(f,g)|<32h^2.
\]
Finally \(\log2>2/3\) (the first term of its positive \(2\operatorname{arctanh}(1/3)\) series) and \(1/\sqrt2>2/3\). Hence
\[
\boxed{\mathcal E_s(f,g)>
\frac{16}{27}h-32h^2=\frac{46}{16875}>0}                   \tag{6.3}
\]
for every scalar \(s\). This contradicts the disjoint-support sign required by the Markov property. The tents are continuous, piecewise linear, vanish near the interval endpoints and midpoint, and have finite archimedean energy; alternatively they can be approximated by smooth tents without changing the strict sign. ∎

As a numerical cross-check only, direct two-dimensional quadrature gives
\[
\mathcal E^{\rm prime}(f,g)\simeq0.00653505428979031,\quad
\mathcal E^{\rm smooth}(f,g)\simeq-0.000383026901382184,
\]
\[
\mathcal E_s(f,g)\simeq0.00615202738840813.
\]
The proof uses the rational lower bound, not these decimal values.

A crossing positive jump on the unfolded interval becomes a term of the form \(c|u(t)+u(v)|^2\) on the odd half interval. Such a term is a positive quadratic energy but is not an ordinary resistance edge \(c|u(t)-u(v)|^2\). Restricting a Markov form to a symmetry sector need not preserve the Markov property, because the pointwise contractions do not preserve oddness.

This also obstructs the prime-only jump energy in these folded coordinates: adding its scalar offset changes no disjoint cross term. A two-sheet or sign-valued connection description can encode that prime mechanism, but does not by itself realize the full Weil stiffness or its mass.

## 7. Verification and review of the preceding round

The preceding exact resistance-controls program was replayed and reproduced its entire saved JSON record, including its code hash and diagnostics. The compact weighted-star construction, its \(T\log T\) counting law, inverse trace, cosine determinant, and branch-tail estimate remain valid under the stated grounded boundary condition. Its arms are dynamically decoupled; it is still only a control example.

The conditional common-space trace-norm argument also survives review. It requires one energy space and one positive measure with genuine compatible maps. The current computations show why those assumptions cannot simply be filled in by the direct prime-jump proposal. The analytic jump identity in the earlier note is correct; the missing step was preservation of the Markov property after the parity reduction and identification of the separate mass.

New reproducible files:

- [Numerical program](../numerics/check_prime_jump_geometry.py), rebuilding the full Weil matrix at each precision and compressing the same matrix for the smaller cutoffs.
- [80-digit record](../numerics/records/prime_jump_geometry_80_20260926.json) and [120-digit record](../numerics/records/prime_jump_geometry_120_20260926.json).
- [Hash-bound precision comparison](../numerics/records/prime_jump_precision_comparison_20260926.json), produced by [the comparison program](../numerics/compare_prime_jump_precision.py).
- [Critical review](../reviews/PRIME_JUMP_GEOMETRY_CRITICAL_REVIEW_20260926.md).

All 153 saved numerical observables agree across the two runs at the 45-significant-digit serialization used by the generator, and pass the comparison's relative \(10^{-25}\) threshold. All 119 discrete observables also match. This comparison concerns saved values, not equality of unrounded internal arithmetic. The maximum algebraic/control residuals are below \(7.4\times10^{-58}\) and \(4.7\times10^{-98}\), respectively. Neither run is an interval certificate. No zeta zeros are evaluated or used as fitting data.

## 8. What remains worth testing

The next investigation should change the prescribed map explicitly, rather than changing the name or dimension of a fractal while retaining the rejected pointwise interpretation.

A bounded first alternative is to use the even integrated field \(\Psi_Nq=J_Nq\). With \(\theta=2\pi t/L\), its basis functions are proportional to \((\cos(n\theta)-1)/n\). Before constructing any graph, test the necessary measure identity
\[
M_{22}-\frac34M_{13}-M_{12}+\frac14M_{11}=0,                \tag{8.1}
\]
which follows from the pointwise product relation for these functions. If this alternative also fails, the arithmetic Hilbert metric must be transported by a genuinely different map, or the intended mass must be allowed to be nonlocal. Equation (8.1) is a proposed next test, not a result of the saved current experiment.

For the prime energy alone, an unfolded two-sheet description retains positive edges and explains the signs in the odd sector. Extending that description must retain the pole and archimedean terms, identify the actual mass, and prove compatible maps. The resistance identity \(\operatorname{tr}\mathcal L^{-1}=\int R\,d\mu\) cannot be applied to a signed sector or a nonlocal mass without an additional theorem.

The simple-even hypothesis at general cutoffs, the sign of the original Weil ground energy, fixed-support arithmetic convergence, growing-support control, Xi identification, and a full spectral-triple realization remain open. The untouched CCM Fourier-tail determinant remains part of the problem; none of the current finite trace tests removes it.

Primary-source formulas were checked against the linked CCM article and Kigami manuscript during this continuation. Only new notes, source programs, and compact records are saved. Earlier research and the neighboring investigation are preserved; no draft snapshot, third-party PDF, large matrix archive, or Git commit is created by this continuation.
