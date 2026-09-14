# Review of the two new passes and a quantitative high-mode bound

13 September 2026. This review concerns commits `5287dad` and `e45acb1`,
especially notes 10–17. The checkout was clean when the review began.
All eight existing programs reproduced their saved records: 39 labelled
algebra checks, 58 hashed package files and 157 checked local links.
These are reproduction results, not analytical proof certification.

The central norm identity survives this review. It is a **positive
completion**, with an essential positive error. The continuation in
[note 19](19_JOINT_RESPONSE_AND_FINITE_RANK_DEFECT.md) replaces that
infinite-rank error by an explicit finite-rank one, using a joint
response and a proved high-mode bound. The finite matrix left behind
still contains the unresolved positivity question.

## 1. Evaluation of the new work

| Claim reviewed | Assessment and qualification |
|---|---|
| Compact Koszul–Dolbeault caps and opposite-twist reflection, note 10 | The chain homotopy, Gaussian source normalization and degree-two reflection signs are consistent. Li–Wen's comparison theorem and opposite-twist pairing support the stated route under the model's strong ellipticity estimates. The evaluated norm is that of the specified middle source; it does not evaluate the original identity period as a norm. |
| All-nine-vacuum endpoint, note 12 | The local representatives have the right source factors. The upper projection bound and lower duality bound have matching leading terms. Keeping the four axis and four mixed vacua explains the factor eight compared with setting the quartic coupling to zero first. |
| Metric uniqueness, note 13 | The trace identity has the correct nonnegative sign, and the annulus argument needs only the rescaled endpoint limits. Applying it to the physical metric remains conditional on the stated exact chiral equation in that frame. Hodge existence alone does not prove that identification. |
| Closed gamma source, note 11 | The bounded-component closure argument, support contraction followed by mollification, and interval restriction of the distributional adjoint are consistent. Form and operator domains are properly distinguished. |
| Robin and remote-delay pole laws, notes 14–15 | The attractive Green kernel, auxiliary negative mode, reduced threshold at length four and remote-delay contact agree with direct calculations. Auxiliary stability and positivity of the reduced arithmetic form are distinct assertions. |
| Prime graph, note 16 | The unitary coupler and complementary output powers give the displayed contact and every prime repetition. The stationary contact lower bound follows from the Fourier multiplier at zero; it has the stated whole-line scope. |
| Collective feedback, note 17 | Expanding the readout gives exactly the displayed error, including its self-pairing. Its positivity, compactness, nonzero massless limit and exclusion of finite Schatten-class corrections follow under the specified domains. |

No invalidating algebraic or domain error was found in these central
arguments. This is an internal mathematical review, not an independent
specialist validation or a verification of every theorem used in the
earlier manuscript.

Three qualifications should remain prominent. First, compactness is not
a bound saying the error is small on the potentially dangerous modes.
For fixed parameters the error remains nonzero on each reference
eigenvector. Second, the unit quartic cap is an isometric tensor label
in notes 15–17: suppressing that label leaves the same source Gram
identities. Those identities have not yet made the supersymmetric
interaction select arithmetic positivity. Third, the gain and prime
parameters are prescribed to match coefficients; the positive response
does not derive their arithmetic normalization.

The primary inputs checked during this review were [Li–Wen, Theorem
2.34 and Section 2.7](https://arxiv.org/html/1903.02713), [Fan's chiral
Hodge framework](https://arxiv.org/abs/1107.1290), and the [Weil-form
context in Suzuki](https://arxiv.org/abs/2606.09096v2). Li–Wen supplies
the comparison and duality framework. Fan's framework does not remove
note 13's explicitly retained model-identification hypothesis.

## 2. Add the missing Neumann half of the gamma comparison

Use \(X=L^2(I_L)\), zero extension \(E_L\), and the gamma operator

\[
T_L=(\mathcal A_\gamma E_L)^*(\mathcal A_\gamma E_L),
\qquad
b(s)=\sum_{k\ge0}\frac{2}{a_k}\frac{s}{a_k^2+s},
\quad a_k=2k+\tfrac12.
\tag{1}
\]

Let \(H_{\rm N}\) and \(H_{\rm D}\) be the ordinary Neumann and
Dirichlet Laplacians on the interval. Their auxiliary form domains
are \(H^1(I_L)\) and \(H_0^1(I_L)\), respectively. For one mass, put

\[
e_a(f,v)=\frac2a\left(\|f-v\|^2+a^{-2}\|v'\|^2\right).
\tag{2}
\]

Restriction of a whole-line auxiliary field to the interval drops a
nonnegative exterior energy. Conversely a Dirichlet auxiliary field
extended by zero is an admissible whole-line field. Minimizing gives

\[
\inf_{H^1(I_L)}e_a(f,v)
\ \le\ \inf_{H^1(\mathbb R)}e_a(E_Lf,u)
\ \le\ \inf_{H_0^1(I_L)}e_a(f,v).
\tag{3}
\]

The exterior term is included in the middle expression. Eliminating
the three fields by their positive resolvents identifies the outer
operators as \((2/a)H_{\rm N,D}(a^2+H_{\rm N,D})^{-1}\).
Summing finite towers and then increasing the tower proves the form
comparison

\[
\boxed{\qquad b\(H_{\rm N}\)\le T_L\le b\(H_{\rm D}\).\qquad}
\tag{4}
\]

For clarity, the domain inclusion is

\[
\operatorname{Dom}b\(H_{\rm D}\)^{1/2}
\subset\mathcal D_{\log,L}
\subset\operatorname{Dom}b\(H_{\rm N}\)^{1/2}.
\tag{5}
\]

No identification of an auxiliary Neumann or Dirichlet field with the
actual gamma boundary condition is made. Inequality (4) compares
energies of three different preparations. It extends the Dirichlet
upper comparison already proved in note 17.

## 3. Consequences for eigenvalues and the old feedback error

Index eigenvalues increasingly, starting at one. Min–max applied to
(4) yields

\[
b(((n-1)\pi/L)^2)\le\lambda_n\(T_L\)
\le b((n\pi/L)^2).
\tag{6}
\]

The lower comparison uses its larger form domain; the upper bound can
also be obtained directly on the first \(n\) Dirichlet eigenfunctions.
Using the digamma asymptotic already established in note 11 gives

\[
\boxed{\quad
\lambda_n\(T_L\)=\log\frac{\pi n}{2L}-\psi(\tfrac14)
+O_L(n^{-1}).
\quad}
\tag{7}
\]

Thus no separate Weyl theorem for a compressed logarithmic operator is
needed here. The [digamma asymptotic](https://dlmf.nist.gov/5.11.E2)
identifies \(b(s)\); the spectral sandwich is a direct variational
deduction.

For the old reference \(T_0=T_L+P_L+e^D I\), the pole operator has
rank two. Finite-rank eigenvalue interlacing in (6) therefore gives

\[
\lambda_n(T_0)=\log\frac{\pi n}{2L}-\psi(\tfrac14)+e^D
+O_{L,D}(n^{-1}).
\tag{8}
\]

In particular, writing \(s_n\) for singular values in decreasing
order, note 17's correction and error satisfy the sharper limits

\[
\sqrt{\log n}\,s_n(\mathcal F_{\kappa,\mu})\longrightarrow\kappa,
\qquad
\log n\,s_n(C_{\kappa,\mu})\longrightarrow\kappa^2+2\kappa\mu.
\tag{9}
\]

The scalar eigenvalue functions are decreasing eventually; sorting
changes at most finitely many initial positions. These limits confirm
the previous exclusion of every finite Schatten class and quantify
the slow decay. They do not control the sign of the Weil form.

## 4. An explicit finite-dimensional place for every unresolved sign

Let \(P_L^{\rm pole}=2|c_L\rangle\langle c_L|-2|s_L\rangle
\langle s_L|\). Distinguish this pole operator from the mode
projection \(P_N\) below. Write the full target operator as

\[
W_L=T_L+w_0 I+P_L^{\rm pole}-J_L^{\rm off},
\qquad
J_L^{\rm off}=
\sum_{m\log p<L}(\log p)p^{-m/2}(T_{m\log p}+T_{m\log p}^*).
\tag{10}
\]

One immediately usable bound is

\[
\beta_L^{\rm crude}=-w_0+2\sinh(L/2)-L
+2\sum_{m\log p<L}(\log p)p^{-m/2},
\qquad W_L\ge b\(H_{\rm N}\)-\beta_L^{\rm crude}I.
\tag{11}
\]

A sharper elementary alternative uses note 16's finite prime chains.
For each active prime put \(d=\log p\), \(q=p^{-1/2}\),

\[
n_p=\lceil L/d\rceil,\qquad
r_n(q)=\max_{1\le i\le n}
\left(\sum_{j=1}^{i-1}q^j+\sum_{j=1}^{n-i}q^j\right).
\tag{12}
\]

The nonnegative off-diagonal matrix \(d(R_n(q)-I)\) is bounded above
by \(d r_n(q)I\), using its maximum absolute row sum. Smaller fibers
cannot increase that bound. Consequently

\[
\boxed{\quad
W_L\ge b\(H_{\rm N}\)-\beta_L I,\qquad
\beta_L=-w_0+2\sinh(L/2)-L+\sum_{\log p<L}(\log p)r_{n_p}(p^{-1/2}).
\quad}
\tag{13}
\]

Using the exact chain maximum eigenvalue instead is permitted if it
is proved or enclosed; no such computation is required for (13).

Let \(e_0=L^{-1/2}\),

\[
e_j(x)=\sqrt{2/L}\cos\bigl(j\pi(x+L/2)/L\bigr),\quad j\ge1,
\qquad P_N=\sum_{j=0}^{N-1}|e_j\rangle\langle e_j|,
\quad Q_N=I-P_N.
\tag{14}
\]

Choose any \(N\ge1\) and \(\delta>0\) for which

\[
b((N\pi/L)^2)\ge\beta_L+\delta.
\tag{15}
\]

Such an \(N\) exists for each fixed \(L\), by \(b(s)\to\infty\).
Then the restriction of the target form to \(Q_N X\) is independently
coercive:

\[
Q_NW_LQ_N\ge\delta Q_N.
\tag{16}
\]

This is a statement about the restricted closed form. It does not
bound mixed low/high terms by zero or prove positivity on all inputs.
Those mixed terms are retained in note 19.

The chosen cosine vectors belong to the **operator** domain of \(T_L\).
Integration by parts gives \(\widehat{E_Le_j}(\tau)=O_j((1+|\tau|)^{-1})\).
Since \(b(\tau^2)=O(\log(2+|\tau|))\), their whole-line images under
\(b(-\partial_x^2)\) are in \(L^2\). Note 11's maximal interval
domain therefore includes them. This also shows that the finite mode
projection preserves the form domain and that its off-diagonal
coupling to \(W_L\) is bounded and finite rank.

## 5. A fully rational worked cutoff, not a positivity certificate

At \(L=1\), only the first return of prime two is active. The prime
chain bound is \(\log2/\sqrt2<1/2\), and

\[
\beta_1<\frac{58}{100}+\frac{11}{7}+\frac{21}{10}
+\frac{23}{20}+\frac{43}{1000}+\frac12.
\tag{17}
\]

Here \(\gamma_E<58/100\), \(\pi<22/7\), \(\log2<7/10\),
\(\log\pi<23/20\), and \(2\sinh(1/2)-1<43/1000\).
These bounds can be checked with elementary rational series:

- \(\log2=2\sum_{j\ge0}3^{-(2j+1)}/(2j+1)\) gives
  \(6931/10000<\log2<7/10\); then
  \(\gamma_E<H_{256}-8(6931/10000)<58/100\).
- The alternating integral series for \(4\int_0^1(1+x^2)^{-1}dx\)
  gives \(\pi>3\), and
  \(22/7-\pi=\int_0^1x^4(1-x)^4/(1+x^2)\,dx>0\).
- A finite exponential series gives \(e^{23/20}>22/7\).
  The positive series for \(\sinh(1/2)\), with a geometric tail
  bound, gives the last bound in (17).

Because \((4\pi)^2>144\), positivity of the gamma summands gives

\[
b((4\pi)^2)>
\sum_{k=0}^{63}\frac{2}{a_k}\frac{144}{a_k^2+144}
>\text{the right side of (17)}+\frac1{16}.
\tag{18}
\]

The last inequality is tested with exact fractions in the
[joint-response program](../numerics/check_joint_response.py).
Thus \(N=4,\delta=1/16\) is a proved choice at \(L=1\), with no
floating-point positivity sampling. The four unresolved modes still
couple to the high sector. This is an example of a cutoff usable in
the new source construction, **not a new certified interval for full
Weil positivity**.

The next note uses (16) to derive a stable joint response, preserves
all mixed terms and unused outputs, and gives a positive completion
whose error is supported entirely in these finitely many chosen modes.
