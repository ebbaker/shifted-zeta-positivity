# Canonical source score and its finite-boundary residual

16 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex assistance. Recorded tool dispatch **gpt-6.1-sol /
ultra**. Separate runtime configuration or backend attestation unavailable.
Fixed analytical task [VCD-E05 r1](../research-progress/handoffs/VCD-E05-r1.md).

**Status: proved in-note, internal analytical work.** This is a
source-consistency identity and residual accounting for a possible
coefficient induction. Its finite walks and weighted integrals identify
the inputs a quantitative update would need. The
[result index](../../../../result-summaries/README.md),
[coefficient cluster](../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md),
[avoid index](../../../../avoid/README.md), and
patterns [01](../../../../avoid/01_restating_the_target.md),
[02](../../../../avoid/02_shape_only_arguments_and_the_controls.md) and
[07](../../../../avoid/07_scoped_exclusions_read_as_universal.md) govern its
use as infrastructure. The frozen route is [plan §6](../research-plan/02_VCD_TAIL_CLOSURE_INDUCTION_RESEARCH_PLAN_20261116.md)
and [brainstorm §§2, 7](../brainstorm/notes/03_VCD_INDUCTION_TRUNCATION_AND_ZERO_CONTROL_20261116.md).

## 1. Canonical score, normalization and operator domain

Fix any real \(\lambda\in[0,1/2]\). Retain \(W_\lambda=e^{\lambda u^2}\Phi\),
\(H_\lambda(z)=\tfrac12\int_{\mathbb R}W_\lambda(u)e^{izu}\,du\),
\(Z_\lambda=\int W_\lambda\,du\), \(d\mu_\lambda=W_\lambda\,du/Z_\lambda\),
and \(F_\lambda=2H_\lambda/Z_\lambda\). Set \(V_\lambda=-\log W_\lambda\).
Use the monic \(P_j\), squared norms \(h_j=\int P_j^2W_\lambda\,du\),
and \(q_j=\sqrt{Z_\lambda/h_j}\,P_j\). Then \(a_n^2=\beta_n=h_n/h_{n-1}\)
for \(n\ge1\), and \(a_0=\beta_0=0\). The Jacobi link \(a_n\)
joins sites \(n-1\) and \(n\).

For \(u\ge0\), use \(\rho=\pi e^{4u}\), \(r_m=m^2\rho\) and
\(s_m=e^u(2r_m^2-3r_m)e^{-r_m}\) from the
[manuscript, §§2 and 4](../manuscript/main.tex). Its checked source
derivative gives
\[
 V_\lambda'(u)
 =-2\lambda u+\sum_{m\ge1}\frac{s_m(u)}{\Phi(u)}
       \left(4r_m-9-\frac{12}{2r_m-3}\right).
\]
The smooth even extension of \(\Phi\) is positive on \(\mathbb R\),
so \(V_\lambda'\) is smooth and odd, with value zero at the origin.
The first summand supplies the lower bound
\(\Phi(u)\ge s_1(u)\ge e^u\rho^2e^{-\rho}\) since \(\rho\ge\pi>3\).
With \(\rho=\pi e^{4|u|}\) on the full line, the inherited upper bounds
\(\Phi\le C_0 e^{|u|}\rho^2e^{-\rho}\) and
\(|\Phi'|\le C_1 e^{|u|}\rho^3e^{-\rho}\) give
\[
 |V_\lambda'(u)|\le C_1\rho+|u|.
\]
For each \(j\), \(|q_j(u)|^2\le C_{j,\lambda}(1+|u|)^{2j}\).
Consequently \(\int|V_\lambda'q_j|^2\,d\mu_\lambda<\infty\).
Indeed the integrand is bounded by a constant times
\[
 (1+|u|)^{2j}(C_1\rho+|u|)^2
 e^{u^2/2+|u|}\rho^2e^{-\rho},
\]
which is integrable. The same estimates give integrable products with
\(W_\lambda'\) and vanishing polynomial boundary terms with \(W_\lambda\).

Use the multiplication realization justified in manuscript §3. For a
real measurable symbol \(f\), \(f(J)\) acts as multiplication by \(f(u)\)
on the vectors for which this product belongs to \(L^2(\mu_\lambda)\).
The bound above puts every finite linear combination of \(q_j\) in the
domain of \(V_\lambda'(J)\), and also in that of \(r(J)\) for
\(r=V_\lambda'-p\) with \(p\) any fixed polynomial. The finite compression
\(\Pi_N f(J)\Pi_N\) used below is restricted to
\(\operatorname{ran}\Pi_N=\operatorname{span}\{e_0,\ldots,e_{N-1}\}\).
For the continuous symbols used here, \(f(J_N)\) is defined by the
finite spectral calculus for \(J_N=\Pi_N J\Pi_N\) on that space.

Integrating \((P_nP_{n-1}W_\lambda)'\) over both ends of \(\mathbb R\)
yields, for \(n\ge1\),
\[
 \int V_\lambda'P_nP_{n-1}W_\lambda\,du
   =\int(P_n'P_{n-1}+P_nP_{n-1}')W_\lambda\,du
   = n h_{n-1}.
\]
Here \(P_n'-nP_{n-1}\) has degree less than \(n-1\), and \(P_{n-1}'\)
has degree less than \(n\). The probability normalization divides the
last expression by \(\sqrt{h_nh_{n-1}}\). Thus
\[
  [V_\lambda'(J)]_{n,n-1}
   =\langle q_n,V_\lambda'q_{n-1}\rangle_{\mu_\lambda}
   =n/a_n,\qquad a_n[V_\lambda'(J)]_{n,n-1}=n. \tag{1}
\]
The same integration by parts gives the real matrix identity
\[
 [V_\lambda'(J)]_{ij}
   =\langle q_i',q_j\rangle_{\mu_\lambda}
       +\langle q_i,q_j'\rangle_{\mu_\lambda}. \tag{2}
\]
For retained \(i,j<N\), expand the polynomial derivatives in the
orthonormal basis to compute (2). The recurrence starting at \(q_0=1\)
determines the required polynomials from \(a_1,\ldots,a_{N-1}\).
In particular the exact retained score compression is computable from
that prefix.

## 2. Arbitrary odd polynomial and paths through the cut

Take any fixed real odd polynomial
\(p(u)=\sum_{\ell=0}^d c_\ell u^{2\ell+1}\), with the zero polynomial
covered by zero coefficients. Put \(r=V_\lambda'-p\), still odd.
On the indicated vectors the exact adjacent relation is
\[
 n=a_n[p(J)]_{n,n-1}
       +a_n\langle q_n,rq_{n-1}\rangle_{\mu_\lambda}. \tag{3}
\]
The term \((J^k)_{ij}\) is the sum over \(k\)-step nearest-neighbor
walks from \(j\) to \(i\) on the nonnegative sites. Each walk contributes
the product of its traversed links. A walk visiting a highest site \(b\)
spends at least \(2b-i-j\) steps reaching it and returning to its endpoint.
The corresponding lower-site bound is \(i+j-2b\) for a lowest site \(b\).
Taking \(k=2\ell+1\), the walks from \(n-1\) to \(n\) use links only
between indices \(\max(1,n-\ell)\) and \(n+\ell\).
Thus the polynomial part of (3), given the prefix through \(a_{N-1}\),
can use omitted links \(a_N,\ldots,a_{n+d}\) if \(n+d\ge N\).

For every \(N\ge1\), linearity on the domains in §1 gives
\[
 \begin{aligned}
 C_N^V&=\Pi_NV_\lambda'(J)\Pi_N-V_\lambda'(J_N)\\
      &=\underbrace{\Pi_Np(J)\Pi_N-p(J_N)}_{D_N^p}
            +\underbrace{\Pi_Nr(J)\Pi_N-r(J_N)}_{D_N^r}.
 \end{aligned} \tag{4}
\]
In \(D_N^p\), all walks staying in \(0,\ldots,N-1\) cancel.
A remaining walk from \(j\) to \(i\) visits site \(N\), traverses \(a_N\)
at least twice, and requires \(k\ge 2N-i-j\). For \(d=0\) or \(N=1\)
the polynomial correction vanishes. Otherwise each potentially
nonzero entry has opposite-parity endpoints \(i,j<N\) and
\(i+j\ge2N-(2d+1)\). Both endpoints then lie among the last
\(\min(N,2d)\) retained sites. Since opposite parity gives
\(i+j\le2N-3\), any contributing walk stays at or below site \(N+d-1\).
The only omitted links used in \(D_N^p\) are therefore among
\(a_N,\ldots,a_{N+d-1}\).

Let \(\mu_{\lambda,N}\) denote the spectral probability measure of
\((J_N,e_0)\). For \(j<N\), \(q_j(J_N)e_0=e_j\) follows by induction
from the recurrence. Consequently the residual block is the signed
quadrature discrepancy
\[
 (D_N^r)_{ij}=
 \int r(u)q_i(u)q_j(u)\,[d\mu_\lambda(u)-d\mu_{\lambda,N}(u)],
       \qquad 0\le i,j<N. \tag{5}
\]
Using \(\mu_{\lambda,N}\) costs only the retained prefix, including the
evaluation of \(r\) at its finite nodes. Formula (2) also determines
\(C_N^V\) from the exact prefix and the values of \(V_\lambda'\) at
those nodes. Hence for retained endpoints the **signed** difference
in (5) can also be recovered algebraically as \(C_N^V-D_N^p\) if the
finite list of cross-cut links is supplied. This equality gives
consistency with a candidate tail when accompanied by a separately
justified restriction on the residual.

For a positive measurable \(\omega\), put
\(d\nu_i^\eta=q_i^2d\eta\) for \(\eta=\mu_\lambda\) or \(\mu_{\lambda,N}\)
and \(i<N\) in the latter case. Both choices give probability measures
because \(q_i\) is normalized in the full space and \(q_i(J_N)e_0=e_i\)
in the finite case. Weighted Cauchy–Schwarz gives
\[
 \left|\int r q_i q_j\,d\eta\right|
 \le
 \left(\int\omega\,d\nu_i^\eta\right)^{1/2}
 \left(\int\frac{|r|^2}{\omega}\,d\nu_j^\eta\right)^{1/2}. \tag{6}
\]
Exchanging \(i,j\) gives the other assignment of the factors.
The unweighted case \(\omega=1\) is finite by §1. Applying (6) to (5)
uses two separate upper bounds and drops any full/discrete cancellation.
It also drops the sign of each individual integral. Each walk weight
is nonnegative before multiplication by the coefficients \(c_\ell\),
which can have either sign. The finite matrices for all three
corrections in (4) are real symmetric and change sign upon conjugation
by \(e_i\mapsto(-1)^i e_i\). Their nonzero eigenvalues come in
opposite-sign pairs, even when \(D_N^p\) has nonnegative entries.

## 3. Exact linear and cubic algebraic controls

Use separate model weights at a fixed time.

- **Linear score.** For \(V'(u)=b u\) with \(b>0\), take a Gaussian
  of variance \(\sigma^2=1/b\). With \(p=V'\), the residual is zero,
  \([p(J)]_{n,n-1}=ba_n\), and (1) gives \(\beta_n=n/b=n\sigma^2\).
  On the retained sites \(D_N^p=0\) for all \(N\), since one step
  cannot leave the retained chain and return.
- **Cubic score.** For \(e^{-u^4+t u^2}\), take \(p=V'=4u^3-2tu\).
  The length-three paths from \(n-1\) to \(n\) have weights
  \(a_n\beta_{n-1}\), \(a_n\beta_n\) and \(a_n\beta_{n+1}\).
  The first is absent at \(n=1\), represented by \(\beta_0=0\).
  Therefore
  \[
    n=4\beta_n(\beta_{n-1}+\beta_n+\beta_{n+1})-2t\beta_n.
  \]
  This agrees with Van Assche, §3, equation (3.1), as recorded in the
  [checked passages](../references/02_INDUCTION_SOURCE_PASSAGES_20261116.md).
  For \(N\ge2\), the length-three excursion
  \(N-2\to N-1\to N\to N-1\) and its reverse give the full boundary
  correction
  \[
    C_N^V=4a_{N-1}\beta_N
       (|e_{N-1}\rangle\langle e_{N-2}|
        +|e_{N-2}\rangle\langle e_{N-1}|).
  \]
  For \(N=1\) it vanishes. More generally the cubic coefficient of
  \(p=cu^3+bu\) is \(c\) in place of \(4\) in this boundary formula.
  The two nonzero eigenvalues when \(c\ne0\) and \(N\ge2\) are
  \(\pm |c|a_{N-1}\beta_N\). The theta residual is separately retained
  in (4) for either polynomial choice.

## 4. Residual ledger

The inherited confinement \(uV_\lambda'\ge\cosh(4u)-11\) and the
diagonal integration-by-parts identity give
\(\int\cosh(4u)\,d\nu_i^{\mu_\lambda}\le2i+12\).
They also give the inherited
\(\beta_i+\beta_{i+1}\le B_i=\operatorname{arcosh}^2(2i+12)/16\).
These bounds control the first full-measure factor in (6) for
\(\omega=\cosh(4u)\), the sizes of each link in the finite walk lists,
and the monic norm product used in quadrature. The theta tail bound
in §1 also ensures that \(|r|/\cosh(4u)\) is bounded for fixed \(p\).
This gives a coarse positive allowance for the second full-measure
factor in terms of the same confinement moment, with a constant
depending on the chosen polynomial. Formula (6) at finite \(N\) uses
exactly computable weighted sums for both factors.

| Quantity | Finite data or estimate available | Outstanding information for an update |
| --- | --- | --- |
| Adjacent polynomial term in (3) | Paths with links from \(\max(1,n-d)\) to \(n+d\). Inherited \(B\) bounds their sizes. | Actual values of the links beyond a retained prefix. |
| Adjacent signed integral in (3) | Exact value by subtraction if \(a_n\) and all its polynomial links are supplied. | An independent bound or relation on \(\int r q_n q_{n-1}d\mu_\lambda\) to constrain unsupplied links. |
| Quadratic factors in (6) | Fixed-degree integrability and a confinement-based magnitude allowance. Discrete factors use the retained nodes. | Quantitative control of \(\int (|r|^2/\omega)q_j^2d\mu_\lambda\) at the accuracy required by an update, or a signed estimate that avoids independent absolute bounds. |
| Boundary block in (4)–(5) | \(C_N^V\) and the finite-node part from exact retained data. \(D_N^p\) and then the signed \(D_N^r\) use at most the indicated \(d\) additional links. | A restriction on (5) that holds independently of the unsupplied links and controls an update. Separate Cauchy bounds supply magnitudes and omit the signed full/discrete cancellation. |
| Tail or Fourier consequence | The source identity fixes a multiplication-score matrix. | A relation with controlled error between this residual and the omitted-tail response or a zero-sensitive Fourier margin. |

Thus evaluation and integrability are paid at fixed degree. The
unpaid estimates concern predictive use of the signed integrals or
their weighted magnitudes. Finite algebraic recovery using already
supplied coefficients cannot serve as the independent residual bound
in that use of (3) or (4).

## 5. Control screen

The relevant comparison is between the **own-score** identity and the
identity with the unchanged canonical \(V_\lambda'\). Regular sources
with the same integration-by-parts hypotheses satisfy (1)–(2) for
their own scores. The algebra in (3)–(6) is also generic. The
[collision catalog](../../../../result-summaries/12_collision_controls_and_screening.md)
and the [existing VCD screen](02_VCD_ANALYTICAL_MANUSCRIPT_INTEGRATION_20261114.md)
give the following premise checks for this decomposition.

| Control | Premise check |
| --- | --- |
| Positive three- and four-square sources | Pass the inherited envelope at their validated collisions and satisfy the own-score identity. The even locally absolutely continuous extension allows integration by parts with matching endpoint values at zero. Their full reflection and complete canonical equal coefficients fail. |
| Euler-factor translates | The canonical summand-score formula fails. The envelope additionally fails for the checked \(c=1/2,p=23,\lambda=0\) case. |
| Reflected super-Gaussian | The exponential confinement inequality fails at large source coordinate. Its own-score identity and polynomial tails for the score permit the domain calculation. |
| Smooth shape and positive-primitive controls | The canonical square-summand score fails. Satisfaction of the weaker confinement bound remains untested here. |
| Nonzero finite-source changes and finite-prime orbit perturbations | Change the complete canonical source, with full reflection absent in the finite-prime controls. Positive square carriers can retain own-score identities and confinement. |
| Fixed-event atoms, finite-profile atoms and their compact triangular extensions | Atomic cases lack a positive full-line density, and the triangular extensions lack global strict positivity. |
| RH-conditional normalized endpoint sources | Ordinary Dirichlet arithmetic and the unchanged canonical source fail. The construction retains its RH hypothesis. |
| Fixed amplitude with varying observation | All source identities survive. The altered kernel fails the literal Fourier/Newman observation. |
| Actual-profile positive-measure relaxation | Lacks the full physical source and observation to which the score identity applies. |

The weighted-square controls show directly that the generic score
identity plus the inherited envelope permit positive-time collisions.
This limits the use of those shared premises. Testing a specific
theta residual inequality would require its own quantified premise.
