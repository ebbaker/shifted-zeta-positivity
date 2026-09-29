# Energy-defined ports and a direct fixed-support determinant limit

Date: 26 September 2026. Continuation round 3.

Model: GPT-6 (Codex). Exact model variant and reasoning-effort setting are not exposed in this session.

Status: LLM-assisted working research, drafted for Edward Baker. Finite identities and the analytic deductions below are proved under their stated hypotheses. The arithmetic computations are exploratory multiprecision checks, not interval certificates. The accompanying [review](../reviews/ENERGY_PORTS_AND_FIXED_SUPPORT_REVIEW_20260926.md) is a same-agent check, not independent refereeing. No priority claim is made for inverse-string theory, Schatten estimates, or Galerkin convergence.

Predecessors: [boundary mechanics](CCM_BOUNDARY_MECHANICS_AND_DETERMINANT_CONTROL_20260926.md) and [strings, graph Dirac operators, and cutoff obstructions](CCM_STRINGS_GRAPH_DIRAC_AND_CUTOFF_OBSTRUCTIONS_20260926.md). Earlier notes, programs, and records are preserved.

## 1. Outcome and scope

The requested fixed-support port experiment has been extended to \(L=\log13\), \(N=8,12,16,24,32\), using four prescribed ports and the same normalization, first bead mass one. A fixed analytic odd profile improves the geometry at smaller cutoffs, but at \(N=32\) it and the original displacement port both put about 14 percent of the inverse trace beyond string coordinate \(10^6\). Applying inverse dynamics to the displacement profile makes this diagnostic worse. None of these finite observations proves or disproves uniform first-moment tightness.

There is a useful analytic alternative to establishing that particular geometric hypothesis. On the original odd Fourier space, the infinite integrated mass form
\[
B=J^*(W_+-\varepsilon_\infty)J
\tag{1}
\]
defines a positive trace-class operator at every fixed support length. This follows from the known logarithmic archimedean multiplier and the zero boundary values of \(Jf\); it does not require a lower bound on the odd-sector gap.

If, in addition, the limiting odd-sector gap satisfies
\[
\kappa_L:=\inf\sigma(W_-)-\varepsilon_\infty>0,
\tag{2}
\]
the inverse mechanical operators admit realizations on that same Fourier space converging in trace norm. Their normalized determinants, including the vanishing fixed-support free tail, consequently converge locally uniformly. This replaces the *string-measure* tightness condition for the purpose of determinant convergence at fixed \(L\). It does not prove (2), specify an arithmetic string limit, or identify the limiting function with Xi.

The numerical odd gaps fall from approximately \(3.91\times10^{-20}\) to \(6.71\times10^{-46}\) over this range. Finite positive gaps are not lower bounds on the continuum gap. The crude analytic estimate below can therefore be very weak, even if (2) eventually holds. The source's continuum simple-even hypothesis would imply (2), but remains unproved.

## 2. What the review confirms and changes

The previous finite transformations retain both energy metrics and correctly distinguish the removed Weil ground vector from the lowest mechanical mode. The string scale, cyclicity condition, ground-energy shift, and free Fourier tail are explicit. We found no error in those central claims. The geometric convergence proposition is a sufficient criterion, not a necessary condition for determinant convergence; that distinction motivates the new common-space construction.

Two cautions become concrete in this round:

1. A smooth displacement profile, or an additional inverse-energy smoothing, does not by itself control the first-moment tail of its reconstructed string.
2. Convergence of total string mass and of the first bead position is much weaker than first-moment tightness. Section 7 gives an exact two-bead counterexample with the same first-mass normalization.

These statements refine the proposed next steps without retracting the previous conditional theorem. They also do not alter the separate [fractal-Laplacian investigation](../../ccm-fractal-laplacians/README.md).

## 3. Port invariants that do not require reconstructing a string

Retain the finite positive mechanical pair \((M,K)\). If \(M=AA^*\), set
\[
H=A^{-1}KA^{-*},\qquad
\beta^2=b^*M^{-1}b,\qquad v=A^{-1}b/\beta.
\]
For a cyclic real port, let \(C=U^*HU\) be its Jacobi matrix, with \(Ue_1=v\), and put \(r=C^{-1}e_1\). Under the earlier convention \(h=r/r_1\), the first mass is one and
\[
x_1=r_1,
\qquad \mu([0,\infty))=\frac{\|r\|^2}{r_1^2}.
\]
Solving for the static response in the original coordinates gives the exact identities
\[
\boxed{x_1=\frac{b^*K^{-1}b}{b^*M^{-1}b}},\qquad
\boxed{\mu([0,\infty))=
\frac{(b^*M^{-1}b)(b^*K^{-1}MK^{-1}b)}{(b^*K^{-1}b)^2}}.
\tag{3}
\]
Indeed \(H^{-1}=A^*K^{-1}A\), so \(r_1=v^*H^{-1}v\) and \(\|r\|^2=v^*H^{-2}v\) give both formulas. Also
\[
1\le\mu([0,\infty))\le
\frac{\|H^{-1}\|}{x_1}\le
\frac{\operatorname{tr}(K^{-1}M)}{x_1}.
\tag{4}
\]
The lower bound follows from \(h_1=1\), and the upper bound from
\(\|r\|^2\le\|C^{-1}\|r_1\). These are identities and inequalities, not yet uniform estimates.

For a displacement-defined port \(b=Mf\), define
\[
a=f^*Mf,\quad p=(Mf)^*K^{-1}Mf,\quad
c=(K^{-1}Mf)^*M(K^{-1}Mf).
\]
Then \(x_1=p/a\) and the total mass is \(ac/p^2\). This formulation avoids inverting \(M\) to evaluate the port invariants, although the numerical string reconstruction still uses its Cholesky factorization.

## 4. Fixed-support experiment

The four ports are prescribed before observing their spectra:

| Name | Force vector in the original odd coordinates | Meaning |
|---|---|---|
| Force | \(e_1\) | Previous force-port baseline |
| Displacement | \(Me_1\) | Previous displacement-port baseline |
| Smooth displacement | \(Mf_N\), \((f_N)_n=2^{1-n}\) | Truncations of one fixed analytic odd profile |
| Inverse-energy displacement | \(MK^{-1}Me_1\) | Apply the inverse mechanical dynamics once to the original displacement |

For the smooth profile, the sine series is proportional to
\(\sin\theta/(1-\cos\theta+1/4)\), since
\(\sum_{n\ge1}2^{1-n}\sin(n\theta)=\sin\theta/(1-2(1/2)\cos\theta+(1/2)^2)\).
The common imaginary phase in the odd Fourier basis is immaterial. The fourth profile depends on the finite arithmetic pair; it is not a fixed continuum function assumed in advance. Neither uses zero data.

Each port is reconstructed with \(h_1=1\). Multiplying every mass by a cutoff-dependent factor would move the spatial tails and change the comparison, so no such rescaling is made.

The table records the fraction \(\int_{x>10^6}x\,d\mu/\int x\,d\mu\). These are fractions of inverse trace, not fractions of total string mass.

| \(N\) | Force | Displacement | Smooth displacement | Inverse-energy displacement |
|---:|---:|---:|---:|---:|
| 8 | 0.633101 | 0 | 0 | 0 |
| 12 | 0.752996 | 0 | 0 | 0 |
| 16 | 0.845890 | 0.0449941 | 0 | 0.0902135 |
| 24 | 0.927212 | 0.108105 | 0.0813203 | 0.167732 |
| 32 | 0.953224 | 0.138144 | 0.137510 | 0.198662 |

At the largest cutoff:

| Port | Total mass | Last bead position | Position containing 90% of inverse trace |
|---|---:|---:|---:|
| Force | 11.97493 | \(1.72362\times10^{40}\) | \(1.72362\times10^{40}\) |
| Displacement | 1.084165 | \(7.17216\times10^{13}\) | \(4.36057\times10^7\) |
| Smooth displacement | 1.179041 | \(3.06616\times10^{13}\) | \(1.80039\times10^7\) |
| Inverse-energy displacement | 1.013518 | \(1.96599\times10^{16}\) | \(5.32466\times10^9\) |

The finite inverse trace is common to every port:
\[
\operatorname{tr}(K_{32}^{-1}M_{32})
=0.01691867855571788098839021238282255\ldots.
\]
Adding the free tail gives \(0.02204587831302476837953081408775098\ldots\).
The total mass of the displacement string and its first position stabilize to many displayed digits, while its tail diagnostic and 90% quantile continue to move. Section 7 explains why those observations are compatible.

The whole five-cutoff, four-port experiment was run at both 120 and 160 decimal digits. All **1,177 numerical observables agree at all 45 saved significant digits**. Maximum scaled reconstruction residuals are \(7.76\times10^{-76}\) and \(1.11\times10^{-115}\), rounded upward. Checks include both energy congruences, Lanczos identities, (3), trace, determinant, boundary response, selected direct-correlation Weil entries, and comparison with the earlier implementation at \(N=8\). A noncyclic control is rejected instead of losing its invisible mode. None of this is an interval error bound, a uniform cyclicity proof, or evidence that the shared implementation cannot contain a common error.

See [the numerical guide](../numerics/README.md), [the generator](../numerics/check_energy_ports.py), and [the source-hash-checked comparison](../numerics/records/energy_port_precision_comparison_20260926.json). The records retain absolute tails at five radii as well as fractions and quantiles. Finite data at a fixed radius cannot decide the limit with \(R\to\infty\) and a supremum over all cutoffs.

## 5. The integrated mass is trace class at fixed support

Let \(I=[-L/2,L/2]\). Write \(W_L\) for the self-adjoint operator associated with the closed semibounded Weil form on \(L^2(I)\), and
\(\varepsilon_\infty=\inf\sigma(W_L)\). Use its even and odd restrictions \(W_+\), \(W_-\). The required source facts are closedness, semiboundedness, the Fourier form core, compact resolvent, and the decomposition into a logarithmic Fourier multiplier plus a bounded operator; these are in [CCM, Sections 3.1--3.2](https://arxiv.org/html/2511.22755v1#S3.SS1).

In the unitary Fourier convention, the archimedean multiplier is
\[
a(t)=2\theta'(t)=\operatorname{Re}\psi(1/4+it/2)-\log\pi.
\]
It is continuous on the real axis and grows as \(\log|t|+O(1)\). Choose a finite nonnegative constant \(a_0\) such that
\[
a(t)\le a_0+\log(1+t^2)\quad(t\in\mathbb R).
\tag{5}
\]
Existence follows from continuity on compact intervals and that asymptotic. No numerical value of \(a_0\) is certified here.

The prime and pole terms have absolute quadratic-form bound \(D_L\|u\|_2^2\), where one admissible constant is
\[
D_L=4\sinh(L/2)+2\sum_{p^j\le e^L}(\log p)p^{-j/2}.
\tag{6}
\]
For the pole term use Cauchy--Schwarz against \(e^{\pm x/2}\) on \(I\); each squared norm is \(2\sinh(L/2)\). For each prime term bound each translated correlation by \(\|u\|_2^2\). Thus this constant uses the entire bounded contribution, including either sign.

For \(u\in H^1_0(I)\), its zero extension is in \(H^1(\mathbb R)\). Plancherel and Jensen's inequality for the concave logarithm imply
\[
\int\log(1+t^2)|\widehat u(t)|^2\frac{dt}{2\pi}
\le\|u\|_2^2\log\left(1+\frac{\|u'\|_2^2}{\|u\|_2^2}\right).
\tag{7}
\]
The zero function is handled by continuity. In particular these functions belong to the Weil form domain. With \(A_L=a_0+D_L+|\varepsilon_\infty|\),
\[
0\le \|(W_+-\varepsilon_\infty)^{1/2}u\|_2^2
\le\|u\|_2^2\left[A_L+
\log\left(1+\frac{\|u'\|_2^2}{\|u\|_2^2}\right)\right]
\tag{8}
\]
for even \(u\in H^1_0(I)\).

Let \(e_n\) be the odd Fourier basis and \(d_n=2\pi n/L\). The same integration map as before satisfies
\[
Je_n=\frac{c_n-\sqrt2c_0}{d_n},\qquad
\|Je_n\|_2^2=\frac3{d_n^2},\qquad
\|(Je_n)'\|_2^2=1.
\]
Therefore
\[
\boxed{\operatorname{tr}B\le
\sum_{n\ge1}\frac3{d_n^2}
\left[A_L+\log(1+d_n^2/3)\right]<\infty.}
\tag{9}
\]
To justify the operator rather than merely the series, first define
\(Z=(W_+-\varepsilon_\infty)^{1/2}J\) on finite odd Fourier sums. Its column norm squares are summable by (8), so it extends to a Hilbert--Schmidt operator. For arbitrary odd \(f\), Fourier truncations converge under \(J\) in \(H^1_0(I)\), and (8) gives convergence in the shifted form norm. Closedness identifies this extension with the form composition. Hence \(B=Z^*Z\) is the positive trace-class operator in (1). No boundedness of \(W_+\) is being assumed.

If \(P_m\) projects onto the first \(m\) odd modes, (9) also gives
\[
t_m:=\operatorname{tr}((I-P_m)B)
\le\sum_{n>m}\frac3{d_n^2}[A_L+\log(1+d_n^2/3)]
=O_L\left(\frac{1+\log m}{m}\right).
\tag{10}
\]
This is a tail in the *original Fourier mass operator*. It is neither the reconstructed spatial first-moment tail nor yet the inverse-dynamics trace tail.

## 6. Conditional trace-norm convergence of inverse dynamics

Let \(\varepsilon_N\) be the least eigenvalue of the full finite Fourier compression, and put \(\delta_N=\varepsilon_N-\varepsilon_\infty\). The form-core property and min--max give \(\delta_N\downarrow0\). Extend every finite matrix by zero on the orthogonal complement of its odd Fourier space. With \(G=J^*J\), the finite mass satisfies the exact identity
\[
B_N:=\iota_N M_N\iota_N^*
=P_NBP_N-\delta_N P_NGP_N.
\tag{11}
\]
Here \(\iota_N\) is the coordinate inclusion and \(\operatorname{tr}G=L^2/8\). Thus
\[
\boxed{\|B_N-B\|_1
\le2\sqrt{(\operatorname{tr}B)t_N}+\delta_N L^2/8\longrightarrow0.}
\tag{12}
\]
For the compression estimate, expand \(B-P_NBP_N=(I-P_N)B+P_NB(I-P_N)\), factor each term through \(B^{1/2}\), and apply the Hilbert--Schmidt product inequality. The negative shift term in (11) has trace norm at most \(\delta_N\operatorname{tr}G\). This sign agrees with the earlier two-finite-cutoff compression identities: the finite ground energy is above the limiting one.

**Proposition.** Fix \(L\), assume (2), and retain the finite CCM hypotheses at all sufficiently large cutoffs being interpreted as CCM determinants. Then, with
\[
K_\infty=W_--\varepsilon_\infty,\quad R=K_\infty^{-1},\quad
R_N=\iota_NK_N^{-1}\iota_N^*,
\]
the positive operators on the common odd \(L^2\) space
\[
\mathcal C_N=R_N^{1/2}B_NR_N^{1/2},\qquad
\mathcal C=R^{1/2}BR^{1/2}
\tag{13}
\]
satisfy \(\|\mathcal C_N-\mathcal C\|_1\to0\). Consequently
\[
\operatorname{tr}(K_N^{-1}M_N)\longrightarrow\operatorname{tr}\mathcal C,
\qquad
\frac{\det(K_N-z^2M_N)}{\det K_N}
\longrightarrow\det(I-z^2\mathcal C)
\tag{14}
\]
locally uniformly in \(z\in\mathbb C\).

**Proof.** Odd Fourier sums are a core for the odd form: project the full core by the bounded parity projection, which preserves the form. Let \(\widetilde K_N\) be the Galerkin matrix of \(K_\infty\) on this space. Its lower bound is \(\kappa_L\), and
\(K_N=\widetilde K_N-\delta_NI\). For large \(N\), \(\delta_N<\kappa_L/2\); hence
\[
K_N\ge\kappa_L I/2,\qquad \|R_N\|\le2/\kappa_L.
\tag{15}
\]
The inverses of \(\widetilde K_N\), extended by zero, converge strongly to \(R\). One direct proof solves the coercive variational equation: its finite solution is the energy-orthogonal projection of the full solution onto the increasing form-core spaces. Energy convergence implies \(L^2\) convergence. The resolvent identity further gives
\[
\|\iota_N(K_N^{-1}-\widetilde K_N^{-1})\iota_N^*\|
\le\frac{\delta_N}{\kappa_L(\kappa_L-\delta_N)}\longrightarrow0.
\]
Thus \(R_N\to R\) strongly with a uniform bound. Polynomial approximation to the square-root function on a common bounded spectral interval gives \(R_N^{1/2}\to R^{1/2}\) strongly.

The contribution of \(B_N-B\) to the difference in (13) has trace norm at most \((2/\kappa_L)\|B_N-B\|_1\). For the remaining contribution set \(X_N=R_N^{1/2}B^{1/2}\) and \(X=R^{1/2}B^{1/2}\). Strong convergence and the Hilbert--Schmidt property of \(B^{1/2}\) imply \(\|X_N-X\|_2\to0\), by finite-rank approximation. Then
\[
\|X_NX_N^*-XX^*\|_1
\le(\|X_N\|_2+\|X\|_2)\|X_N-X\|_2\to0.
\]
This proves trace-norm convergence. On its finite Fourier range, \(\mathcal C_N\) is \(K_N^{-1/2}M_NK_N^{-1/2}\), so its nonzero eigenvalues are precisely \(\omega_{N,j}^{-2}\). Trace-norm convergence gives convergence of these positive eigenvalue lists in \(\ell^1\), and telescoping products gives locally uniform convergence of their determinants, as in the preceding note. This proves (14). \(\square\)

In particular, eventually
\[
\operatorname{tr}(K_N^{-1}M_N)
\le\frac{2}{\kappa_L}\operatorname{tr}B.
\tag{16}
\]
The finitely many smaller positive pencils cause no uniform-boundedness problem at a *fixed* \(L\), although their constants may be large. The new construction does not assert exact energy preservation by the original inclusions. It accounts for their defect through \(\delta_N\), so it does not contradict the earlier obstruction to exact nesting.

The full finite CCM function has the unchanged extra factor
\[
U_{L,N}(z)=\prod_{n>N}(1-z^2/d_n^2).
\]
At fixed \(L\), \(U_{L,N}\to1\) locally uniformly, so the full determinant has the same limit in (14). No statement uniform in \(L\) follows: both \(A_L\) and \(\kappa_L^{-1}\) can deteriorate. For joint limits the previously derived Gaussian factor when \(L^2/N\) has a positive finite limit remains necessary.

This proposition is an operator realization of a standard conditional approximation argument. Under a simple isolated even continuum ground state, convergence of its finite approximants is already central in [Connes--van Suijlekom, Theorem 5.11 and its proof](https://arxiv.org/html/2511.23257v1#S5). The contribution here is to make the trace-class mass factor and the common Fourier-space inverse operator explicit for this investigation, not to claim that the underlying simple-even difficulty has been removed.

### What this also gives for displacement ports

Suppose \(f_N=P_Nf\) for a fixed odd \(f\), and \(a=\langle f,Bf\rangle>0\). Equations (12)--(15) imply convergence of
\[
a_N=\langle f_N,B_Nf_N\rangle,\quad
p_N=\langle B_Nf_N,R_NB_Nf_N\rangle,\quad
c_N=\langle R_NB_Nf_N,B_NR_NB_Nf_N\rangle
\]
to their corresponding expressions with \(B,R,f\). In particular
\(p=\langle Bf,RBf\rangle>0\), since \(Bf\ne0\) and \(R\) is positive and injective. By (3), \(x_{1,N}\to p/a>0\) and total string mass tends to \(ac/p^2<\infty\), provided the ports are cyclic when a connected string is asserted. The same proof applies to norm-convergent moving profiles with positive limiting mass energy. It covers the inverse-energy profiles \(R_NB_Ne_1\) under these hypotheses whenever their limiting mass energy is positive.

Thus conditional total-mass control for displacement ports follows directly in Fourier coordinates. First-moment spatial tightness still does not follow.

## 7. A normalized counterexample to the remaining inference

For \(R>1\), consider the connected positive string
\[
\mu_R=\delta_1+\frac2R\delta_R,\quad
M_R=\operatorname{diag}(1,2/R),\quad
K_R=\begin{pmatrix}1+(R-1)^{-1}&-(R-1)^{-1}\\
-(R-1)^{-1}&(R-1)^{-1}\end{pmatrix}.
\tag{17}
\]
Its first mass and first position are both one. Its total mass converges to one, and \(\mu_R\) converges weakly against bounded continuous functions to \(\delta_1\). Nevertheless,
\[
\int x\,d\mu_R=3,\qquad
\int_{x>r}x\,d\mu_R=2\quad(R>r>1).
\]
The first moments are not uniformly tight. With \(t=z^2\), direct two-by-two determinants give
\[
P_R(t)=\frac{\det(K_R-tM_R)}{\det K_R}
=1-3t+2(1-1/R)t^2\longrightarrow(1-t)(1-2t),
\tag{18}
\]
whereas the weak limiting measure has determinant \(1-t\). At the first-bead force port,
\[
e_1^*(K_R-tM_R)^{-1}e_1
=\frac{1-2(1-1/R)t}{P_R(t)}.
\tag{19}
\]
Away from the limiting poles, this response tends to \(1/(1-t)\): the second spectral factor becomes invisible in the limiting boundary response. At finite \(R\) the off-diagonal spring is nonzero, so the first port is cyclic. Finite cyclicity does not ensure that all modes remain visible in a limiting response. Equation (19)'s limit is not asserted uniformly across the disappearing pole.

This example strengthens the earlier escaping single-mass control by respecting \(m_1=1\) and a stable positive \(x_1\). It is not an arithmetic CCM family and does not prove that its behavior occurs for the displacement port. It proves that stable mass and first-position data, even with determinant convergence, cannot replace the spatial-tail hypothesis. The [exact rational control](../numerics/check_energy_port_controls.py) verifies (17)--(19) at three values of \(R\); the algebra above proves the formulas for every \(R>1\).

## 8. Claim ledger and next steps

| Result | Status | Remaining condition |
|---|---|---|
| Port formulas (3), bounds (4) | Exact finite deductions | Cyclicity for a connected string |
| Four-port comparison through \(N=32\) | Two-precision evidence; 1,177 saved observables agree | Uniform arithmetic estimates and certified signs if required |
| \(B\) is trace class at fixed \(L\), with Fourier tail (10) | Proved from the stated established Weil-form facts | Effective constants needed for a numerical certificate |
| \(B_N\to B\) in trace norm | Proved, using Fourier-core ground-energy convergence | No additional odd-gap assumption for this statement |
| Inverse-dynamics and determinant convergence (14) | Proved conditional theorem at fixed \(L\) | Continuum odd gap (2), and the finite CCM hypotheses for the CCM interpretation |
| Total-mass convergence for energy-defined ports | Conditional corollary | Same gap, nonzero limiting mass energy, and cyclicity |
| First-moment tightness of the arithmetic strings | Not established or disproved | Quantitative spatial-tail or inverse-spectral visibility estimates |
| Xi identification, support-uniform bounds, original Weil positivity | Not established | Additional arithmetic input; the construction still loses the scalar energy offset |

The next useful task is to investigate the small odd-energy sector itself, rather than select another smoother port solely because its total mass is small. At \(L=\log13\), construct a low/high Fourier block enclosure for the odd Weil form, retaining the ground-energy shift and bounding the infinite high block analytically through the archimedean contribution. A Schur-complement lower bound could decide whether a positive continuum odd gap can actually be certified. Finite Ritz values alone cannot do that.

If the resulting inverse-gap constant is too large to give informative trace bounds, the next target is a *relative* estimate controlling \((W_+-\varepsilon_\infty)^{1/2}J(W_--\varepsilon_\infty)^{-1/2}\) in Hilbert--Schmidt norm, using cancellation between the two energy forms rather than a uniform ordinary \(L^2\) gap. This is the desired trace written as a factorization, not a proof of an estimate; it should be approached by separately estimating the small-energy sector and its complement.

For an arithmetic *string* limit, additionally study whether a limiting displacement port observes every nonzero limiting inverse mode. The counterexample explains why finite cyclicity and scalar response convergence are insufficient. An inverse-string continuity theorem would need its full hypotheses checked before turning that observation into a tightness conclusion.

Only after fixed-support control should one vary \(L\), retaining the free tail and seeking an independent arithmetic identification with Xi. Nothing here establishes RH.

## Source and provenance record

- Connes--Consani--Moscovici, [*Zeta Spectral Triples*, arXiv:2511.22755v1](https://arxiv.org/html/2511.22755v1): Sections 3.1--3.2 for the form input and Fourier multiplier; Theorem 5.10 for the conditional finite operator; Section 8 for the unresolved continuum hypotheses. HTML inspected 26 September 2026. The multiplier normalization was checked against (3.8)--(3.9) and (3.19), not just the asymptotic display.
- Connes--van Suijlekom, [*Quadratic Forms, Real Zeros and Echoes of the Spectral Action*, arXiv:2511.23257v1](https://arxiv.org/html/2511.23257v1): Theorem 5.11 and its variational approximation argument delimit the novelty and the role of the continuum gap. HTML inspected on the same date.
- All additional estimates, the port experiment, and the two-bead control are derived in this note and its linked code. No zeta-zero data are used in the new computation. No third-party PDFs, dense matrix archives, manuscript snapshots, or release artifacts are added.
