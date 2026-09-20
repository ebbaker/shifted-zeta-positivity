# Operator formulation of the gamma tower and the full Weil target

Date: 13 September 2026.

This note records and expands the operator perspective discussed after the
manuscript's research-program bridge was added. Its purpose is to make the
entire response operator the object of study, with a particular input function
appearing only when an energy or matrix element is evaluated. It supplies an
explicit spectral comparison problem for further work. It does not establish
the missing comparison or a positive realization of the full Weil form.

## 1. What is already incorporated, and what this note adds

The [background](../../../../background.pdf), particularly “The shifted transfer
and its generator” and its bulk–boundary discussion, already explains the
operator shift-energy balance, minimizing extension maps, positive response
operators, and Schur complements. The
[current manuscript](../../manuscript.pdf) already gives the finite-block Schur
complement, the relative Hilbert complex, and exact response formulas valid for
arbitrary admitted inputs. Those formulas are not extrapolations from selected
numerical test functions.

What is not yet assembled there as one account is the following chain:

| Object | Operator formulation | Status |
| --- | --- | --- |
| Gamma kinetic energy | Functional calculus of the positive whole-line Laplacian | Existing construction, rewritten below |
| Auxiliary-field elimination | Schur complement or harmonic projection | Existing mechanism, made explicit below |
| Full arithmetic target | A self-adjoint finite-interval operator, including poles and prime delays | Consequence of the background's closed form |
| Positive loop model | The gamma function of a modified positive derivative operator | Equivalent operator description of the manuscript's formula |
| Remaining sign question | Domination of the residual and pole correction by that positive response | Exact reformulation; unresolved |
| Normalized comparison | A compact self-adjoint operator whose spectral upper bound must be at most one | Additional formulation and justification in this note |

The final two items suggest an operator-centered investigation. They do not
remove the universal quantifier over states: an operator inequality is precisely
a statement about all states in its form domain. They remove the need to select
and solve for one boundary profile at a time.

No background equation numbers are used below. The definitions needed for the
formulation are reproduced explicitly.

## 2. Spaces, domains, and the meaning of an energy operator

Fix an interval length \(L>0\), and write

\[
I_L=(-L/2,L/2),\qquad
\mathcal H_L=L^2(I_L),\qquad
\mathcal H=L^2(\mathbb R).
\]

Inner products are conjugate-linear in the first variable. Let
\(E_L:\mathcal H_L\to\mathcal H\) be zero extension; its adjoint is
restriction. On the whole line use

\[
D=-i\partial_x,\qquad \operatorname{Dom}D=H^1(\mathbb R),
\qquad A=D^2=-\partial_x^2,\qquad
\operatorname{Dom}A=H^2(\mathbb R).
\]

Both are self-adjoint, and \(A\geq0\). The Fourier convention is
\(\widehat F(\tau)=\int_{\mathbb R}F(x)e^{-i\tau x}\,dx\).
The finite-interval energy domain is

\[
\mathcal D_{\log,L}=
\left\{f\in\mathcal H_L:
\int_{\mathbb R}\log(2+|\tau|)
|\widehat{E_Lf}(\tau)|^2\,d\tau<\infty\right\}.
\]

An unbounded energy operator and its form have different domains. For the
self-adjoint operator \(\mathsf W_L\) defined below,
\(Q_{0,L}(g,f)=\langle g,\mathsf W_Lf\rangle\) is valid when
\(f\in\operatorname{Dom}\mathsf W_L\) and
\(g\in\mathcal D_{\log,L}\). Its quadratic form is defined on the larger
space \(\mathcal D_{\log,L}\). Every unbounded compression, sandwich, and
inequality below is interpreted through the associated forms unless an
operator-domain statement is made explicitly.

Thus “without explicit boundary data” means retaining the space and the
injection \(E_L\), while leaving a particular vector \(f\) implicit. It
does not mean removing the domain, changing the exterior condition, or choosing
an arbitrary self-adjoint interval Laplacian. In particular, compression of
\(B(A)\) is generally different from applying \(B\) to a Dirichlet interval
Laplacian. The whole-line auxiliary fields and their exterior tails remain part
of the model.

## 3. The gamma kinetic operator and its positive channels

Define

\[
B(s)=\operatorname{Re}\psi\!\left(\tfrac14+
\tfrac{i\sqrt{s}}2\right)-\psi(\tfrac14),
\qquad a_k=2k+\tfrac12.
\]

The digamma partial-fraction identity gives

\[
B(s)=\sum_{k=0}^{\infty}\frac2{a_k}\frac{s}{a_k^2+s},
\qquad s\geq0.
\]

This follows by taking real parts in the standard digamma series and
subtracting its value at \(1/4\); see [NIST DLMF, “Series
Expansions”](https://dlmf.nist.gov/5.7). Functional calculus therefore gives

\[
\boxed{\mathsf K=B(A)
=\sum_{k=0}^{\infty}\frac2{a_k}A(a_k^2+A)^{-1}\geq0.}
\]

The partial sums are bounded positive operators, increasing in form order.
Their limit is the closed, generally unbounded form of \(B(A)\); there is
no assertion of convergence in bounded-operator norm. Its multiplier grows
like \(\log|\tau|\), so its form domain is the stated logarithmic Fourier
space. On the interval,

\[
\mathsf K_L=E_L^*B(A)E_L
\]

denotes the operator associated with the compressed closed form. More
precisely it is \((B(A)^{1/2}E_L)^*(B(A)^{1/2}E_L)\).

For one mass \(a>0\), set

\[
R_a=(I+a^{-2}A)^{-1}=a^2(a^2+A)^{-1}.
\]

This is the equilibrium response operator, a bounded positive contraction.
The joint channel energy is represented by the positive block form

\[
\mathbb H_a=\frac2a
\begin{pmatrix}
I&-I\\
-I&I+a^{-2}A
\end{pmatrix},
\qquad \text{form domain }L^2(\mathbb R)\oplus H^1(\mathbb R).
\]

Its value on \((F,u)\) is
\((2/a)(\|F-u\|^2+a^{-2}\|u'\|^2)\). Eliminating the second component
gives the Schur complement

\[
\boxed{\mathsf K_a=\frac2a(I-R_a)
=\frac2a A(a^2+A)^{-1}\geq0.}
\]

The minimizing map is \(F\mapsto R_aF\), valid for all \(F\in L^2\)
at once. Summing these responses gives \(\mathsf K\). This is the
operator content of the first success: a specified positive system produces
exactly the required gamma kinetic operator. The contact constant, poles, and
prime terms have not been included in this success.

### The same response in the relative SUSY complex

Let

\[
D_au=(u,a^{-1}u'),\qquad JF=(F,0),
\qquad \Pi_a=P_{\ker D_a^*}.
\]

Here \(D_a:H^1\subset L^2\to L^2\oplus L^2\) is closed and has closed
range. The orthogonal projection \(\Pi_a\) is bounded. The prepared
response map and its energy operator are

\[
\Gamma_a=\sqrt{2/a}\,\Pi_aJ,
\qquad \Gamma_a^*\Gamma_a=\frac2aJ^*\Pi_aJ=\mathsf K_a.
\]

The quotient-norm, Schur-complement, and resolvent descriptions thus produce
the same operator. In the tower, one first forms each \(\Gamma_{a_k}\)
and then takes their direct sum on the finite-energy domain. The unprepared
source \((\sqrt{2/a_k}JF)_k\) has infinite norm for every nonzero \(F\),
because \(\sum_k2/a_k\) diverges. Writing an operator formula does not
permit projecting that nonexistent ambient Hilbert vector.

The auxiliary SUSY Hamiltonian is
\(\operatorname{diag}(D_a^*D_a,D_aD_a^*)\). A prepared harmonic vector
has zero energy under this auxiliary Hamiltonian and may have nonzero ordinary
norm. The latter norm is the gamma response. The effective energy operator
\(\mathsf K_a\) should therefore be distinguished from the auxiliary SUSY
Hamiltonian; neither construction alone supplies a canonical physical dynamics.

## 4. The full finite-interval Weil operator

Let \(U_d=e^{-idD}\), so \((U_dF)(x)=F(x-d)\), and let

\[
T_d=E_L^*U_dE_L.
\]

Whole-line translations are unitary. Their interval compressions are
contractions and include the loss of overlap at the endpoints. They are zero
for \(d\geq L\). Define the bounded scalar maps

\[
\mathcal C_Lf=\int_{I_L}f(x)\cosh(x/2)\,dx,
\qquad
\mathcal S_Lf=\int_{I_L}f(x)\sinh(x/2)\,dx,
\]

and the rank-at-most-two pole operator

\[
\mathsf P_L=2\mathcal C_L^*\mathcal C_L-
2\mathcal S_L^*\mathcal S_L.
\]

With \(\ell_p=\log p\), \(r_p=p^{-1/2}\), and
\(w_0=\psi(1/4)-\log\pi<0\), the target is

\[
\boxed{
\mathsf W_L=\mathsf K_L+w_0I+\mathsf P_L
-\sum_{\substack{p\ {\rm prime},\ m\geq1\\m\ell_p<L}}
\ell_pr_p^m(T_{m\ell_p}+T_{m\ell_p}^*).
}
\]

At each fixed \(L\), the sum is finite and everything after
\(\mathsf K_L\) is a bounded self-adjoint perturbation. Consequently
\(\mathsf W_L\) exists, is self-adjoint and semibounded, and has form
domain \(\mathcal D_{\log,L}\), without an RH assumption. This is a
realization of the given arithmetic form as an operator, not yet its positive
factorization. The external operator framework and the localized Weil criterion
are described in [Suzuki, “Weil's quadratic form via the screw
function”](https://arxiv.org/html/2606.09096v2).

The program can now be stated as

\[
\boxed{\mathrm{RH}\quad\Longleftrightarrow\quad
\mathsf W_L\geq0\ \text{for every }L>0
\quad\Longleftrightarrow\quad
\inf\sigma(\mathsf W_L)\geq0\ \text{for every }L>0.}
\]

An unbounded sequence of lengths suffices. No positive gap uniform in \(L\)
is required. These eigenvalues are energy levels of the localized Weil
operator; they have not been identified with zeta-zero ordinates.

## 5. The loop response as functional calculus

Choose a finite prime set \(\mathcal P\) containing every prime active at
the chosen interval length. The manuscript defines the bounded return operator

\[
\mathcal A_{\mathcal P}
=\sum_{p\in\mathcal P}\ell_p
\sum_{m\geq1}r_p^mU_{m\ell_p},
\qquad
M_t=\exp[t(cI-2\mathcal A_{\mathcal P})].
\]

Each return series converges in operator norm. At fixed finite prime set,
\(M_t\) and its inverse are bounded and preserve all ordinary Sobolev
spaces. They commute with \(D\). Write its Fourier multiplier as
\(m_t(\tau)=e^{tg(\tau)}\), where

\[
v(\tau)=\operatorname{Re}g(\tau)
=c-2\sum_{p\in\mathcal P}\ell_p
\sum_{m\geq1}r_p^m\cos(m\ell_p\tau).
\]

Define the closed derivative map \(M_tD\) on \(H^1\), and its positive
energy operator

\[
A_t=(M_tD)^*(M_tD)\geq0.
\]

Its multiplier is \(\tau^2e^{2tv(\tau)}\), and its operator domain is
\(H^2\). The exact positive loop response is

\[
\boxed{\mathsf Z_{t,L}=E_L^*B(A_t)E_L\geq0.}
\]

This follows by replacing \(A\) with \(A_t\) in every channel Schur
complement. It describes the entire minimizing response, rather than an
approximation obtained from a few inputs.

Define the residual multiplier and its compression by

\[
\rho_t(\tau)=B(\tau^2e^{2tv(\tau)})-B(\tau^2)-tv(\tau),
\qquad
\mathsf R_{t,L}=E_L^*\rho_t(D)E_L.
\]

For fixed cutoff, \(\rho_t\) is bounded, real, even, and
\(O(|\tau|^{-2})\). Its continuous inverse Fourier kernel gives a
Hilbert–Schmidt, hence compact, self-adjoint operator on the interval. The
manuscript's exact arithmetic identity at \(t=1\), \(c=w_0\) is

\[
\boxed{\mathsf W_L=\mathsf Z_{1,L}+\mathsf P_L-\mathsf R_{1,L}.}
\]

The unresolved positivity question is therefore precisely

\[
\boxed{\mathsf R_{1,L}-\mathsf P_L\leq\mathsf Z_{1,L}.}
\]

An operator comparison proving this inequality would establish positivity at
that length. A positive bulk model whose Schur complement equals
\(\mathsf W_L\) would additionally give the desired constructive
realization. Either would be substantive progress; equality of the existing
positive loop response with the full target has not been proved.

## 6. A normalized compact spectral problem

The unbounded positive term can be used as a reference energy. Fix
\(\alpha>0\), and define

\[
H_{\alpha,L}=\mathsf Z_{1,L}+\alpha I,
\qquad
\mathsf C_{\alpha,L}=
H_{\alpha,L}^{-1/2}
(\alpha I+\mathsf R_{1,L}-\mathsf P_L)
H_{\alpha,L}^{-1/2}.
\]

Since \(H_{\alpha,L}\geq\alpha I\), its inverse square root is bounded
and maps \(\mathcal H_L\) onto the form domain. The normalized correction
\(\mathsf C_{\alpha,L}\) is bounded and self-adjoint. Direct substitution
gives the exact form identity

\[
\mathsf W_L=
H_{\alpha,L}^{1/2}(I-\mathsf C_{\alpha,L})
H_{\alpha,L}^{1/2}.
\]

Surjectivity of the inverse-square-root map onto the form domain proves

\[
\boxed{
\mathsf W_L\geq0
\quad\Longleftrightarrow\quad
I-\mathsf C_{\alpha,L}\geq0
\quad\Longleftrightarrow\quad
\sup\sigma(\mathsf C_{\alpha,L})\leq1.
}
\]

This is a congruence, not a unitary equivalence; the two operators need not
have equal numerical eigenvalues. The added \(\alpha\) cancels in the
identity. It changes the normalization of the comparison, not the arithmetic
target or the truth of the sign condition. Only the spectral upper bound is
needed. Requiring \(\|\mathsf C_{\alpha,L}\|\leq1\) would also control
large negative eigenvalues and is a stronger condition.

### Why the normalized operator is compact

At fixed cutoff, \(v\) is bounded, and
\(B(\tau^2e^{2v(\tau)})-B(\tau^2)\) is bounded. The form norm of
\(H_{\alpha,L}\) is therefore equivalent to the logarithmic Fourier norm
on \(\mathcal D_{\log,L}\). A bounded set in this norm has uniformly
small Fourier tails: beyond frequency \(R\), its squared \(L^2\) mass
is bounded by a constant divided by \(\log(2+R)\).

All zero extensions have support in the same bounded interval. Splitting
Fourier space into \(|\tau|\leq R\) and its tail also gives uniform
continuity under translations: on the first part use
\(|e^{ih\tau}-1|\leq |h|R\), and on the tail use the preceding bound.
The \(L^2\) compactness criterion then proves that the form-domain embedding
into \(\mathcal H_L\) is compact. Thus
\(H_{\alpha,L}^{-1/2}\), and hence \(\mathsf C_{\alpha,L}\), is
compact. The same argument gives compact resolvent for \(\mathsf W_L\),
so its spectral lower bound is a lowest eigenvalue.

The sign problem has now been converted into the spectral upper bound of an
explicit compact operator. Compactness alone does not establish that bound.

### An exact even–odd decomposition

Reflection \((\mathcal Jf)(x)=f(-x)\) commutes with the target, the loop
response, the residual, and the normalized correction. Their multipliers or
symmetrized delay kernels are even. Although the causal amplitude \(M_t\)
need not commute with reflection, its derivative energy \(A_t\) does.
Consequently the normalized comparison splits into its even and odd sectors,
and its spectral upper bound is the larger of the two sector bounds.

The pole correction simplifies as well: on even functions it is
\(2\mathcal C_L^*\mathcal C_L\), and on odd functions it is
\(-2\mathcal S_L^*\mathcal S_L\). Thus there is one pole amplitude in
each sector, with opposite signs. This decomposition covers the entire complex
input space and is an exact operator reduction, not a choice of a few trial
profiles. Both sector bounds together establish positivity of the full operator.

### What a rigorous finite computation would need

Let \(\Pi_N\) be finite-rank orthogonal projections converging strongly to
the identity. Compactness implies

\[
\varepsilon_N=
\|\mathsf C_{\alpha,L}-\Pi_N\mathsf C_{\alpha,L}\Pi_N\|
\longrightarrow0.
\]

If \(\lambda_N\) is the largest eigenvalue of the compression on
\(\operatorname{ran}\Pi_N\), then

\[
\sup\sigma(\mathsf C_{\alpha,L})
\leq\max\{\lambda_N,0\}+\varepsilon_N.
\]

The zero accounts for the orthogonal complement when the finite matrix is
extended by zero. A certified matrix bound and a certified remainder bound
could therefore prove positivity at a fixed length. A finite matrix with all
eigenvalues below one, without control of \(\varepsilon_N\), does not.
If the true spectral upper bound is exactly one, this elementary error-bound
strategy may need a separate treatment of the equality modes.

No such certified computation or remainder estimate is supplied by this note.
This is a precise alternative to collecting individual positive test-function
values, and a possible next calculation. A finite collection of verified
lengths would still leave the arbitrary-length requirement open.

## 7. Existing repairs and obstructions in operator language

The manuscript's structural obstructions retain their force under this
reformulation. The following statements keep their original model scopes.

| Proposed repair | Operator interpretation | What the manuscript establishes |
| --- | --- | --- |
| A fixed rational scalar one-delay filter | Implement the required entire repetition sequence with a restricted transfer function | The all-repetition identity fails in that class; matching a finite subset is a different question |
| Finitely many extra boundary amplitudes | Add a finite-rank Hermitian operator to the response | The one-prime residual has infinite rank, so a net finite-rank correction cannot give exact matching |
| More relaxation variables with the old energy still accessible | The new minimized response is at most the old response in form order | Analytic high-frequency packets show that the target requires increases on a subspace surviving any finite set of amplitude constraints |
| An independent positive addition | Require \(\mathsf W_L-\mathsf Z_{1,L}\geq0\) | The reported negative bump diagnostic is not a certified sign theorem; this proposed exclusion remains numerical at that scope |
| Finitely many independent convex compliance splits, or the specified derivative penalty | Modify channel Schur complements within those stated families | The next singular coefficient survives for the finite convex splits; the fixed positive derivative penalty restores an unmatched leading cusp |

Infinite rank obstructs *exact finite-rank replacement*, not approximation or
operator domination. Similarly, a nonzero residual obstructs equality of a
particular model response with the target, but does not by itself obstruct
positivity of \(\mathsf W_L\). Analytic test-function families are legitimate
proofs of failure of an operator inequality; their role differs from numerical
sampling.

### The leading-cusp cancellation as an operator modification

For the manuscript's one-prime model at \(t=1\), put

\[
Q_M=(M_1^*M_1)^{-1},\qquad
X_\delta=(1-\delta)Q_M+\delta I,\qquad 0<\delta<1.
\]

These are positive bounded invertible Fourier multipliers commuting with
\(A\). The old and replacement channel responses are

\[
\mathsf T_a(Q_M)=\frac2a A(A+a^2Q_M)^{-1},\qquad
\mathsf T_a(X_\delta)=\frac2a A(A+a^2X_\delta)^{-1}.
\]

The second formula comes from eliminating the manuscript's positive splitting
field. It is not prescribed by subtracting an error after minimization. The
new whole-line positive tower response is

\[
\widetilde{\mathsf Z}
=B(A_1)-\mathsf T_a(Q_M)+\mathsf T_a(X_\delta).
\]

Positivity follows because one positive channel was replaced by another; the
displayed subtraction simply removes the old channel from the sum. Compress
this response to the interval as before. If \(q(\tau)=e^{-2v(\tau)}\),
the leading residual coefficient becomes

\[
\left(-\frac1{24}+2a\delta\right)
\frac{q(\tau)-1}{\tau^2}.
\]

At \(a=1/2\), \(\delta=1/24\), it vanishes at every phase. The residual
then has an \(O(|\tau|^{-4})\) Fourier tail, rather than the original
\(O(|\tau|^{-2})\) tail. The corrected residual operator has a smoother
kernel but remains infinite rank; the manuscript proves a surviving
third-derivative jump.

This is useful for an operator investigation because it changes the full
high-frequency response in a controlled way and may permit sharper estimates
of approximation remainders. Any improved rate or usable constant still needs
proof. Kernel smoothness does not imply a smaller residual operator norm or a
better normalized spectral bound. Indeed, in the stated one-prime arithmetic
model \(q>1\), the split stiffens the channel; the existing numerical bump
discrepancy becomes larger even though the leading cusp disappears.

## 8. Connection with the shifted generator and contraction defect

The static formulation uses \(\mathsf W_L=\mathsf W_{0,L}\). The
background also provides a shift-dependent family. Let

\[
\xi(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s),
\qquad F(p)=\xi(1/2+p),\qquad
K_\omega(p)=\frac{F(p-\omega)}{F(p+\omega)}.
\]

The causal finite-interval transfer \(V_{\omega,L}\) is defined from this
symbol on a right-half-plane Laplace line. Its generator has symbol

\[
a_\omega(p)=\frac{F'(p-\omega)}{F(p-\omega)}
+\frac{F'(p+\omega)}{F(p+\omega)},
\qquad
\partial_\omega V_{\omega,L}=-G_{\omega,L}V_{\omega,L}.
\]

The closed symmetric generator form is represented by

\[
\mathsf W_{\omega,L}=\tfrac12(G_{\omega,L}+G_{\omega,L}^*)
\]

in form sense. It includes the gamma, pole, contact, and prime contributions.
For the contraction defect,

\[
D_{\omega,L}=I-V_{\omega,L}^*V_{\omega,L},\qquad
\partial_\omega D_{\omega,L}
=2V_{\omega,L}^*\mathsf W_{\omega,L}V_{\omega,L}.
\]

At positive shift the pulled-back form specifies the bounded derivative
operator. At zero shift the background proves the right-derivative identity on
smooth compactly supported inputs; no derivative in bounded-operator norm is
asserted. In this sense the central Weil form is the initial rate of change of
the contraction defect, while the defect records the accumulated change.

If one independently constructs a loss-channel operator \(Y_{\omega,L}\)
with

\[
V_{\omega,L}^*V_{\omega,L}
+Y_{\omega,L}^*Y_{\omega,L}=I,
\]

then \(D_{\omega,L}=Y_{\omega,L}^*Y_{\omega,L}\geq0\) follows from
norm conservation. This is a possible operator mechanism for contraction, not
a conservation law established by the present model. Defining \(Y\) as the
square root of a defect already assumed positive would not prove contraction.

The shift \(\omega\) is an auxiliary parameter, not an established physical
time. It is also distinct from the loop coupling \(t\): the manuscript's
\(M_t\) modifies an auxiliary derivative operator, whereas
\(V_{\omega,L}\) evolves the input using the full arithmetic generator.
The two operators cannot be identified from their exponential notation.

## 9. What must remain when explicit inputs are suppressed

**The finite-length family remains essential.** For \(L<L'\), zero
extension from \(I_L\) into \(I_{L'}\) preserves the target form. This is
an exact compatibility of the arithmetic targets. It does not automatically
give compatible bare bulk models, response factors, or estimates as the prime
cutoff changes. Additional inactive primes can change the nonlinear loop
response and its compensating residual even though their direct compressed
delays vanish. Bounds on the finite-prime operators above are not uniform over
all prime sets.

**A single factor on ordinary whole-line \(L^2\) is a different demand.**
The related [positive-factorizations manuscript](../../../positive-factorizations/manuscript.pdf)
contains the “No closable factor on ordinary whole-line \(L^2\)” obstruction.
Its mechanism is relevant here. If such a factor realized the full Weil form
on every compactly supported smooth input, positivity would first imply RH.
The form would then be the sum of squared Fourier evaluations at zero
ordinates, with their multiplicities. A sequence

\[
f_N(x)=N^{-1}e^{i\gamma_0x}\phi(x/N),\qquad
\widehat\phi(0)=1,
\]

converges to zero in ordinary \(L^2\), while its Fourier samples converge
in the weighted sequence space to the nonzero atom at \(\gamma_0\).
Rapid Fourier decay and the zero-counting bound justify that convergence.
The factor's images would be Cauchy with nonzero limiting norm, contradicting
closability. The increasing supports explain why this does not contradict
finite-interval operators or the positive gamma tower. Other input topologies
are a separate possibility. Thus moving to operator language should retain the
finite-interval family used here, rather than silently impose an incompatible
ordinary whole-line realization of the full form.

**The model must determine the response before matching.** For a suitably
defined positive block operator

\[
\mathbb H_L=
\begin{pmatrix}
H_{bb}&H_{bi}\\H_{ib}&H_{ii}
\end{pmatrix}\geq0,
\]

with an invertible interior block and justified block domains, the effective
operator is

\[
\mathsf S_L=H_{bb}-H_{bi}H_{ii}^{-1}H_{ib}.
\]

This is literal block algebra for bounded blocks with
\(H_{ii}\geq\beta I>0\). For continuous fields, an appropriate closed
form and solvability argument must justify the expression; the gamma channels
above provide such an example. Positivity of the whole block gives
\(\mathsf S_L\geq0\). Positivity of \(H_{ii}\) alone does not.
The constructive target is \(\mathsf S_L=\mathsf W_L\) on the full form
domain, derived from independently specified fields and couplings.

## 10. A concrete next investigation

Two related directions now have precise outputs.

1. **Spectral comparison of the existing response.** Work at a fixed first-prime
   length, construct or estimate \(\mathsf C_{\alpha,L}\), and seek an
   analytic upper bound or a finite compression with a certified remainder.
   Treat the poles and the entire residual together. The meaningful output is
   a proved spectral bound, a certified violating mode, or a clearly identified
   estimate that remains missing. The normalized comparison is algebraically
   equivalent to Weil positivity and may be just as difficult; its purpose is
   to expose available operator tools.
2. **A new coupled positive block system.** Follow the manuscript's suggestion
   of a coupled two-mass/history model or a modified field-valued source map.
   Specify its positive energy and domains, compute its Schur complement as an
   operator, and compare its exact kernel with \(\mathsf W_L\). Check all
   active singular terms before estimating the regular remainder. In the
   manuscript's diagonal compliance class, the first two cancellation
   conditions already require some relative softening alongside net
   stiffening; a family that only stiffens cannot meet both.

The first route aims directly at an operator inequality. The second aims at an
independent positive realization. Neither requires beginning with a special
input profile. Both require all-domain validity, followed by control over an
unbounded set of interval lengths before the full research-program objective
is reached.

## Source and status record

- The formulas for the gamma tower, finite-prime loop response, exact residual,
  splitting field, and scoped obstructions are taken from the current
  [manuscript source](../../manuscript.tex) and reorganized here.
- The arithmetic normalization, logarithmic domain, and shift-energy identities
  agree with the current [background source](../../../../background_section.tex).
- The normalized compact comparison and its finite-compression error inequality
  are derived in this note. They are proposed tools, not a completed estimate.
- The external mathematical references used above are NIST DLMF and Suzuki's
  operator treatment. Local links identify the investigation's source material.
- This note adds exposition and deductions from the displayed operators. It
  changes no manuscript theorem, PDF, numerical program, or diagnostic record,
  and reports no new positivity interval or RH proof.
