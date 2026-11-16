# Fixed-polynomial loss and the exponential score reference

16 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex assistance. Recorded tool dispatch **gpt-6.1-sol /
ultra**. Separate runtime configuration or backend attestation unavailable.
Fixed analytical task [VCD-E06 r2](../research-progress/handoffs/VCD-E06-r2.md).

**Status: proved in-note, internal analytical work.** This is an
intermediate score estimate. Its gain is a relative \(O(\log n/n)\)
error in the adjacent score identity, with an explicit constant.
Its scoped exclusion concerns fixed polynomial scores with a
negligible relative residual. See the
[result index](../../../../result-summaries/README.md),
[coefficient cluster](../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md),
[avoid index](../../../../avoid/README.md) and patterns
[01](../../../../avoid/01_restating_the_target.md),
[02](../../../../avoid/02_shape_only_arguments_and_the_controls.md) and
[07](../../../../avoid/07_scoped_exclusions_read_as_universal.md).
The choice of retained score information belongs to
[VCD-B02](../brainstorm/notes/04_VCD_B02_SCORE_INFORMATION_DECISION_20261116.md).

Keep the complete \(W_\lambda=e^{\lambda u^2}\Phi\), the physical
\(H_\lambda=\frac12\int W_\lambda(u)e^{izu}\,du\) and
\(F_\lambda=2H_\lambda/Z_\lambda\) for \(Z_\lambda=\int W_\lambda\).
All bounds below apply to \(0\le\lambda\le1/2\).
Write \(V_\lambda=-\log W_\lambda\), \(d\mu_\lambda=W_\lambda\,du/Z_\lambda\),
and use the normalized orthogonal basis \(q_j\) and its multiplication
matrix \(J\). The link \(a_n=\sqrt{\beta_n}\) joins \(n-1\) to \(n\).
We use [E05](05_VCD_E05_SOURCE_SCORE_RESIDUAL_20261116.md) for
\(a_n[V_\lambda'(J)]_{n,n-1}=n\) and the polynomial-vector domain.

## 1. A fixed polynomial carries a vanishing part of the score

For a fixed real odd polynomial \(p(u)=\sum_{k=0}^d p_k u^k\),
define the local edge majorant
\[
 A_{n,d}=\tfrac14\operatorname{arcosh}(2(n+d)+10),\qquad n\ge1 .
\]
The [envelope](01_VCD_E01_LOGARITHMIC_ENVELOPE_20261113.md)
\(\beta_{j-1}+\beta_j\le B_{j-1}\) makes \(a_j\le A_{n,d}\)
for \(1\le j\le n+d\). A nearest-neighbor walk of length \(k\le d\)
from \(n-1\) to \(n\) stays at or below site \(n+d\). There are at
most \(2^k\) choices and each product is at most \(A_{n,d}^k\).
Multiplying by \(a_n\le A_{n,d}\) proves
\[
 \left|a_n[p(J)]_{n,n-1}\right|
 \le A_{n,d}\sum_{k=0}^d |p_k|(2A_{n,d})^k .
 \tag{1}
\]
The zero polynomial can be included with \(d=0\). Since
\(\operatorname{arcosh}t\le\log(2t)\) for \(t\ge1\), the right side is
\(O_p(\log^{d+1}(n+2))\). By E05,
\[
 \begin{aligned}
 a_n\langle q_n,(V_\lambda'-p)q_{n-1}\rangle_{\mu_\lambda}
   &=n+O_p(\log^{d+1}(n+2)),\\
 \sup_{0\le\lambda\le1/2}
 \left|\frac{a_n}{n}\langle q_n,(V_\lambda'-p)q_{n-1}\rangle_{\mu_\lambda}
         -1\right|
   &\le \frac{A_{n,d}}n \sum_{k=0}^d |p_k|(2A_{n,d})^k
       \longrightarrow 0 .
 \end{aligned} \tag{2}
\]
In particular the signed residual carries asymptotically the entire
normalized score for each fixed \(p\). The conclusion applies to fixed
coefficients and degree. Degree-dependent polynomials require estimates
with their actual degree and coefficient sizes.

## 2. Exponential reference with an explicit bounded error

For \(u\ge0\) put \(\rho=\pi e^{4u}\), \(r_m=m^2\rho\),
\(s_m=e^u(2r_m^2-3r_m)e^{-r_m}\), and
\(w_m=s_m/\sum_{j\ge1}s_j\). The already justified differentiation
in [manuscript §§2 and 4](../manuscript/main.tex) gives
\[
 V_\lambda'(u)=-2\lambda u+
 \sum_{m\ge1}w_m\left(4r_m-9-\frac{12}{2r_m-3}\right).
\]
Separate \(4\rho\) from its positive weighted mean and use
\(4\rho-8\pi\sinh(4u)=4\pi e^{-4u}\). This gives the exact decomposition
\[
 V_\lambda'(u)=8\pi\sinh(4u)-2\lambda u+b(u), \tag{3}
\]
where, for \(u\ge0\),
\[
 b(u)=4\pi e^{-4u}-9-12\sum_{m\ge1}\frac{w_m}{2r_m-3}
       +4\rho\sum_{m\ge2}(m^2-1)w_m . \tag{4}
\]
The score and both reference terms are odd by reflection. They fix
\(b(0)=0\), so (4) also determines the odd extension at the origin.
The heat contribution in (3) accounts for all time dependence.

Since \(2\rho^2-3\rho\ge\rho^2\) and the first summand is positive,
\[
 0<w_m\le s_m/s_1\le 2m^4 e^{-(m^2-1)\rho}.
\]
For \(m\ge2\), the function \(t e^{-(m^2-1)t}\) decreases on \(t\ge\pi\).
Using \(\rho\ge\pi\) and \(\sum_m w_m=1\) in (4) proves
\[
 \|b\|_\infty\le C_b
  =9+\frac{12}{2\pi-3}+4\pi+
       8\pi\sum_{m\ge2}m^4(m^2-1)e^{-\pi(m^2-1)} . \tag{5}
\]
The series converges by Gaussian decay against a polynomial. It also
dominates the last sum in (4) uniformly in \(u\ge0\).
The rational sum is bounded by \(1/(2\rho-3)\). Consequently
the terms in (4) except \(-9\) tend to zero as \(u\to+\infty\);
for the last term this follows by termwise convergence under the
summable majorant. The tail limit on the positive side is \(-9\).

The theta tails put \(\sinh(4u)q_j\) in \(L^2(\mu_\lambda)\)
for every fixed \(j\), since the exponential growth of the multiplier
is dominated by \(e^{-\pi e^{4|u|}}\) in the density. The same domination
justifies insertion of the Taylor series under the matrix-element
integral, using \(e^{4|u|}|q_iq_j|\) as an integrable majorant.
The bounded \(b\) acts on the whole space with
\(\|b(J)\|\le\|b\|_\infty\). For the adjacent entries, (3) gives
\[
 8\pi a_n[\sinh(4J)]_{n,n-1}-2\lambda\beta_n
       =n-a_n[b(J)]_{n,n-1}.
\]
It follows that
\[
 \left|8\pi a_n[\sinh(4J)]_{n,n-1}-2\lambda\beta_n-n\right|
       \le C_b a_n
       \le \frac{C_b}{4}\operatorname{arcosh}(2n+10).
 \tag{6}
\]
This is absolute \(O(\log(n+2))\) and relative
\(O(\log(n+2)/n)\), uniformly in the time band. The absolute allowance
grows with \(n\), so its relative decay refers specifically to the
normalization by \(n\) in the score identity.

## 3. Exact boundary decomposition for the exponential reference

For fixed \(N\ge1\), put \(A=J_N\), \(e=e_{N-1}\),
\(P=|e\rangle\langle e|\), and \(D=J^{[N]}\), the tail supplied by
removing the link \(a_N\). For real \(t\) define
\[
 T_N(t)=\Pi_N e^{tJ}\Pi_N\big|_{\operatorname{ran}\Pi_N},\qquad
 K_N(t)=\langle e_N,e^{tD}e_N\rangle .
\]
These fixed entries are entire in \(t\) by the
[E04 fixed-vector audit, §§2 and 4](04_VCD_E04_TAIL_FOUNDATIONS_20261116.md).
Apply its real-height block equation to each initial retained
basis vector, which has zero initial tail. Continue that finite
equation to height \(x=-it\), including the oriented convolution.
The minus sign of the real-height memory and the two factors
\(-i\) from differentiation and integration yield the plus sign in
\[
 T_N'(t)=A T_N(t)+\beta_N\int_0^t K_N(t-s)P T_N(s)\,ds,\qquad
 T_N(0)=I_N .
\]
All terms use continued fixed-vector entries. Variation of constants
in the finite head gives
\[
 \Delta_N(t):=T_N(t)-e^{tA}
 =\beta_N\int_0^t ds\int_0^s dr\,
     e^{(t-s)A}P K_N(s-r)T_N(r). \tag{7}
\]
Both integrals are oriented for negative real \(t\). The only physical
link at the cut enters through its two crossings, \(\beta_N\). The
tail response \(K_N\) and the full projected \(T_N\) are retained
exactly inside (7). For example, \(K_N(t)=1+O(t^2)\) and
\(T_N(t)=I_N+tA+O(t^2)\) give the first two terms
\(\Delta_N(t)=\beta_N(t^2 P/2+t^3(AP+PA)/6)+O(t^4)\).
The cubic term agrees with the explicit paths in E05.

Now the linear term in (3) compresses exactly and the exponential
reference gives
\[
 C_N^V=4\pi\{\Delta_N(4)-\Delta_N(-4)\}
          +\Pi_N b(J)\Pi_N-b(A). \tag{8}
\]
The last term has operator norm at most \(2C_b\).
Alternating site signs conjugate \(\Delta_N(t)\) to \(\Delta_N(-t)\).
For \(t>0\), the convergent path expansion of \(\Delta_N(t)\) has
entrywise nonnegative terms from walks crossing the cut. Thus the
first term of (8) vanishes on equal-parity indices and is entrywise
nonnegative on opposite-parity indices. Its nonzero eigenvalues
occur in positive and negative pairs. The bounded \(b\)-correction
can contribute either entry sign within this estimate.

The paid part of (8) is the norm allowance on the bounded multiplier.
The exponential part still uses the full tail through \(K_N\) in (7).
Equation (6) constrains a neighboring matrix element of a real
exponential multiplier. The literal scalar \(F_\lambda(x)\) for
real height instead depends on the signed integral of
\(\cos(xu)\) against \(\mu_\lambda\). Neither (6) nor (8) estimates
the signed balance of that integral or a complex-height zero-free
margin. A separate transfer estimate would have to connect the
retained source-score information to that scalar.

## 4. Collision-control screen

The [collision catalog](../../../../result-summaries/12_collision_controls_and_screening.md)
and [E05 §5](05_VCD_E05_SOURCE_SCORE_RESIDUAL_20261116.md) supply the
source and observation premise comparisons. The validated three- and
four-square controls in manuscript §6 retain a positive first
summand and positive constant weights \(c_m\) on their finite mode
lists. For such a list, replacing \(s_m\) by \(c_m s_m\) in (4)
only inserts \(c_m/c_1\) in the upper bound on \(w_m\).
Thus their own scores have the same exponential reference in (3)
with a bounded odd \(b_c\), defined almost everywhere if the even
extension has a derivative jump at zero. They also retain the
coefficient envelope. For their coefficients and polynomials,
the own-score identity gives the actual canonical-score defect
\[
 \left|a_n^{c}
       \langle q_n^{c},V_\lambda' q_{n-1}^{c}\rangle_{\mu_\lambda^{c}}-n\right|
  = a_n^{c}
    \left|\langle q_n^{c}, (b-b_c)q_{n-1}^{c}\rangle_{\mu_\lambda^{c}}\right|
  \le (\|b\|_\infty+\|b_c\|_\infty)a_n^{c}.
\]
This is relative \(O(\log(n+2)/n)\) at their catalog collisions.
They fail complete equal canonical coefficients and full reflection.
The bound uses control-dependent constants and gives an asymptotic
defect. Simultaneous exact canonical finite score constraints and
the corresponding finite-information screen belong to VCD-E07.

The reflected super-Gaussian fails the bounded error in (3) because
its own score has polynomial growth. The Euler-factor, smooth shape
and positive-primitive controls lack the unchanged summand expansion.
Their quantitative tests against (6) are open here. Finite-prime
perturbations fail full reflection, and finite-source changes alter
the canonical source. Atomic sources lack the positive density and
compact triangular sources lack full-line positivity. The
RH-conditional endpoints alter ordinary Dirichlet arithmetic under
their stated RH hypothesis. A varied observation with fixed source
retains all score data while failing the literal Fourier readout.
The actual-profile relaxation lacks the complete source and
physical readout. These checks limit conclusions from the stated
score bound and shared premises. They leave growing-degree
source-sensitive constraints to be specified and proved.
