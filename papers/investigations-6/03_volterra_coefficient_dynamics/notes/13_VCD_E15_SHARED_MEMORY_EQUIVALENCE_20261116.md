# VCD-E15 r1 — Shared-memory midpoint equivalence and kernel error

16 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance. Recorded task dispatch **gpt-6.1-sol / ultra**.
Separate backend model and effort attestation unavailable.

**Complete, proved in-note.** All four input hashes in the [frozen
request][request] match. The [comparison in decision08][decision] is an
exact same-model identity. The signed error formula, its leading Taylor
coefficient, and the fixed-disk stability estimate concern two kernels
on one fixed prefix. This is an intermediate comparison in the
[coefficient cluster][cluster]. See the [result index][results],
[avoid index][avoid] and patterns [01][a01], [02][a02], [03][a03],
[07][a07] and [12][a12].

## 1. Entire finite evolution

Let \(N\ge1\), \(A=J_N\) be the real symmetric tridiagonal prefix on
sites \(0,\ldots,N-1\), and \(a_j=\sqrt{\beta_j}>0\) its adjacent
links for \(1\le j<N\). Set \(e=e_{N-1}\), \(P=ee^{\mathsf T}\) and
\(\beta=\beta_N>0\). For entire functions with compatible matrix sizes
use the ordered convolution
\[
 (U*V)(z)=\int_0^z U(z-w)V(w)\,dw
         =z\int_0^1 U((1-h)z)V(hz)\,dh.
\]
Integrals follow the oriented straight segment. The second expression
shows that the convolution is entire. For three factors a change of
variables gives \(z^2\) times the integral of
\(U(h_1z)V((1-h_1-h_3)z)W(h_3z)\) over
\(h_1,h_3\ge0,\ h_1+h_3\le1\), with area \(1/2\). Either parenthesization
gives this integral with the same factor order, so the convolution is
associative.

For an arbitrary scalar entire \(k\) consider
\[
 T_k'=iA T_k-\beta\,k*(P T_k),\qquad T_k(0)=I,\qquad
 y_k=T_k e_0,\qquad f_k=e_0^{\mathsf T}T_k e_0 .
\]
The equivalent integrated equation is \(T_k=I+C_k*T_k\), with
\(C_k(z)=iA-\beta P\int_0^z k(w)\,dw\). In fact \(C_k(0)=iA\)
and \(C_k'=-\beta P k\), so differentiating the integrated equation
recovers the differential equation and its initial value.
On \(|z|\le R\) put \(M_k=\sup_{|z|\le R}|k(z)|\) and
\(L_k=\|A\|+\beta M_k R\), where the matrix norm is induced by the
Euclidean norm. Then \(\|C_k(z)\|\le L_k\). Define
\(U_0=I\) and \(U_{m+1}=C_k*U_m\). Straight-segment integration
gives \(\|U_m(z)\|\le L_k^m |z|^m/m!\) by induction, hence
\(T_k=\sum_{m\ge0}U_m\) is locally uniformly convergent, solves
the integrated equation, and obeys \(\|T_k(z)\|\le e^{L_k|z|}\).
For the difference of any two entire solutions with the same
initial value, \(D=C_k*D\). Iterating gives
\(\|D(z)\|\le (\sup_{|w|\le R}\|D(w)\|)L_k^m|z|^m/m!\) for every
\(m\). Letting \(m\to\infty\) proves uniqueness on every disk.
The same proof for vectors gives \(y_k\) as the unique entire
solution of \(y_k'=iAy_k-\beta e(k*e^{\mathsf T}y_k)\) with
initial vector \(e_0\).

## 2. One kernel at two heights

Write \(y=y_k\), \(g=e^{\mathsf T}y\), and
\[
 I_k(t,s)=\int_0^t\!\int_0^s k(t+s-u-v)g(u)g(v)\,dv\,du,\qquad
 H_k(t,s)=y(t)^{\mathsf T}y(s)-\beta I_k(t,s).
\]
The substitutions \(u=ht,\ v=js,\ h,j\in[0,1]\) give an entire
function of \((t,s)\). The endpoint rule for complex integrals
applies because each integrand is entire in the integration
variable and in the parameters. The two interior derivatives
both bring down \(k'\), so
\[
 (\partial_t-\partial_s)I_k(t,s)
    =g(t)(k*g)(s)-(k*g)(t)g(s).
\]
For the head pairing the two \(iA\) terms cancel since
\((iA)^{\mathsf T}=iA\). The memory terms give
\[
 (\partial_t-\partial_s)\big(y(t)^{\mathsf T}y(s)\big)
    =\beta\{g(t)(k*g)(s)-(k*g)(t)g(s)\}.
\]
Consequently \((\partial_t-\partial_s)H_k=0\). For every fixed
\(w\in\mathbb C\), \(t\mapsto H_k(t,w-t)\) is constant.
Since \(I_k(w,0)=0\) and \(y(0)=e_0\), this proves
\[
                         H_k(t,s)=f_k(t+s).
\]
For the midpoint put \(\mathbf c_k(z)=y_k(z/2)\),
\(\gamma_k(z)=e^{\mathsf T}\mathbf c_k(z)\), and
\(R_k(z)=-\beta I_k(z/2,z/2)\). Changing the integration variables
gives the [E13 §4][e13] equations with kernel \(k\)
\[
 \begin{aligned}
 \mathbf c_k'(z)&=\frac{iA}{2}\mathbf c_k(z)
   -\frac{\beta}{4}e\int_0^z k((z-p)/2)\gamma_k(p)\,dp,\\
 R_k(z)&=-\frac{\beta}{4}\int_0^z\!\int_0^z
       k\big(z-(p+q)/2\big)\gamma_k(p)\gamma_k(q)\,dq\,dp .
 \end{aligned}
\]
The head uses kernel arguments on the segment out to \(z/2\).
The omitted term uses the segment out to \(z\). The midpoint scalar
\(\mathbf c_k^{\mathsf T}\mathbf c_k+R_k\) equals the direct
full-height scalar \(f_k\) for every choice of the shared kernel.

For \(k=0\) the memory and the double integral vanish and the
scalar is \(e_0^{\mathsf T}e^{izA}e_0\), the bare quadrature
in the physical prefix. A normalized physical tail has value
one at zero. The generic model allows kernels without a
positive-measure realization.

## 3. Exact signed transport

Let \(k,\ell\) be two entire kernels and \(\delta k=k-\ell\).
An entire matrix forcing \(G\) in the \(k\)-equation with zero
initial data has solution \(X=T_k*G\). Indeed
\[
 (T_k*G)'=G+T_k'*G=G+iA(T_k*G)-\beta k*\big(P(T_k*G)\big)
\]
by the endpoint rule and ordered associativity. The homogeneous
uniqueness argument gives uniqueness for this forcing. Subtracting
the two fundamental-matrix equations gives the \(k\)-equation for
\(T_k-T_\ell\) with forcing \(-\beta\,\delta k*(P T_\ell)\).
Applying the forcing formula and taking the \(e_0,e_0\) entry yields
\[
 \boxed{ f_k-f_\ell
      =-\beta\,(e_0^{\mathsf T}T_k e)*(\delta k)*(e^{\mathsf T}T_\ell e_0). }
 \tag{1}
\]
For the midpoint comparison the left-hand side equals
\[
 (\mathbf c_k+\mathbf c_\ell)^{\mathsf T}(\mathbf c_k-\mathbf c_\ell)
   +(R_k-R_\ell).
\]
Equation (1) preserves this combined signed difference before applying
absolute values. All operations use compact complex segments.

## 4. First discrepancy

For nonnegative integers \(p,r\), convolution of \(z^p/p!\) with
\(z^r/r!\) is \(z^{p+r+1}/(p+r+1)!\), by integration by parts on
the unit segment parameter. Thus for each \(m\ge0\) the derivatives
at zero satisfy
\[
 T_k^{(m+1)}(0)=iA T_k^{(m)}(0)
    -\beta P\!\!\sum_{\substack{r,s\ge0\\r+s=m-1}}
                    k^{(r)}(0)T_k^{(s)}(0),
\]
with an empty sum at \(m=0\). Induction in the recurrence shows
that \(T_k^{(m)}(0)\) is \((iA)^m\) plus a linear combination
of products in \(A,P\) with at most \(m-2\) factors of \(A\).
The memory part uses \(s\le m-1\) at derivative order \(m+1\).
The leading term arises by taking only \(iA\) at each step.
Since \(A\) moves at most one site at a time and \(P\) is
diagonal, both boundary transfers in (1) have vanishing
derivatives before order \(N-1\) and leading derivative
\(i^{N-1}\prod_{j=1}^{N-1}a_j\) in that order. The only path
of length \(N-1\) joining the endpoints is the monotone one.
At \(N=1\) the leading derivative is the initial entry \(1\).

If \(\delta k\) has first nonzero derivative of order \(q\),
two convolutions add two to the sum of the three leading orders.
Using the monomial convolution formula in (1) gives
\[
 f_k(z)-f_\ell(z)
  =(-1)^N\!\left(\prod_{j=1}^N\beta_j\right)
    \delta k^{(q)}(0)\,\frac{z^{2N+q}}{(2N+q)!}
   +O(z^{2N+q+1}).
 \tag{2}
\]
All links are positive, so the displayed term is nonzero.
If the derivatives of \(\delta k\) all vanish at zero, the two
entire kernels agree and their scalar responses coincide. If
both kernels are even with value one at zero, a finite \(q\)
is even and at least two. With \(k=k_N\) the physical tail
and \(\ell=0\), \(q=0\) and (2) gives the first excluded walk
coefficient in [E04 §1][e04]. As a separate endpoint check at
\(N=1,\ A=0,\ k=1,\ \ell=0\), the equation gives
\(f_k(z)=\cos(\sqrt\beta\,z)\) and \(f_\ell(z)=1\), with the
predicted coefficient \(-\beta/2\) of \(z^2\).

## 5. Fixed-disk stability

Let \(M=\max(\sup_{|z|\le R}|k(z)|,\sup_{|z|\le R}|\ell(z)|)\),
\(\epsilon=\sup_{|z|\le R}|\delta k(z)|\), and \(L=\|A\|+\beta MR\).
Section 1 gives \(\max(\|T_k(z)\|,\|T_\ell(z)\|)\le e^{L|z|}\)
on the disk. In the simplex formula for (1) the boundary
transfers are bounded by \(e^{L(h_1+h_3)|z|}\) and the middle
factor by \(\epsilon\). The area is \(1/2\) and \(h_1+h_3\le1\),
so
\[
                  |f_k(z)-f_\ell(z)|
                    \le \frac{\beta\epsilon |z|^2}{2}e^{L|z|}
                    \qquad (|z|\le R).
\]
This is an absolute estimate for a fixed prefix and disk, using
only the disk suprema and matrix norm. In the physical chain
[E04 §4][e04] gives \(\sup_{N\ge1}k_N(i b)=\infty\) at each
fixed real \(b\ne0\) and fixed heat time. Uniform moving-tail
control requires a different estimate.

## 6. Canonical input and control scope

For the exact theta tail \(k_N(z)=\langle e_N,e^{izJ^{[N]}}e_N\rangle\),
[E04][e04] supplies the entire tail kernel and the elimination
equations on each initial retained vector. Hence \(T_{k_N}\) is
the entire projected Fourier propagator and \(f_{k_N}=F_\lambda\).
Putting \(k=k_N\) in (1) reduces the exact E13 joint error to transport
of \(k_N-\ell\) on the fixed prefix. The exponential-parameter
matrix \(T_N(t)\) in [E06][e06] is \(T_{k_N}(-it)\), and its tail
kernel \(K_N(t)\) is \(k_N(-it)\). The exact canonical decomposition
remains \(V_\lambda'(u)=8\pi\sinh(4u)-2\lambda u+b(u)\), with
the exact bounded symbol \(b\) specified in E06 (4) and the
retained correction \(\Pi_N b(J)\Pi_N-b(A)\) in E06 (8).
The generic derivation uses only \(A,\beta,k,\ell\). Using the
canonical score to justify a quantitative kernel error on the
required segment or contour is still open. A zero transfer also
requires a modeled zero-free margin or quantitative contour
control, and an estimate across degrees or a justified terminal
condition for an induction.

The [catalog screen][catalog] applies through the [E13 comparisons][e13]
and the [detailed E07 table][e07screen]. The generic identity accepts
any common kernel on a finite symmetric head. The distinctions below
concern the extra premises a theta-specific application would need.

| Control | Premise comparison |
| --- | --- |
| Weighted three- and four-square sources | Keep the generic dynamics and the envelope. Complete equal square coefficients and full reflection fail. |
| Finite square-mode changes and finite-prime orbits | The complete source changes and full canonical reflection fails. Fixed finite measurements can survive. |
| Euler-factor translates | The canonical summand score and normalized first link change. The envelope failure cited in E13 is for \(c=1/2,p=23,\lambda=0\). |
| Reflected super-Gaussian | Exponential confinement and bounded comparison with the canonical score fail. |
| Smooth shape and positive-primitive controls | The theta square-summand formula fails. |
| Finite atoms and finite-profile controls | Atoms lack a positive full-line density. The compact triangular extensions fail strict positivity on the full line. |
| RH-conditional normalized endpoint controls | Ordinary Dirichlet arithmetic and the unchanged theta formula fail. Their zero conclusion retains the RH hypothesis. |
| Fixed amplitude with varied observation | The varied observation fails the literal Fourier/Newman readout. |
| Actual-profile positive-measure relaxation | The relaxed data lack the prescribed full-line physical source and Fourier field. |

The [E07 finite score controls][e07] use positive finite square-mode
changes and inherit the nonreal-zero result in that class, without
a prescribed zero location. The [E10 smooth compact multipliers][e10]
preserve the reflection jet and real tails while varying the next
canonical score defect in their stated class. They fail the constant
square-coefficient representation in the absolutely convergent class
checked in [E11][e11]. Their Fourier zero locations remain open.
Both classes can use their own exact kernels in the same-model identity.

Equality at each \(z\) limits the comparison to two readouts with the
same prefix, boundary link, and single entire scalar kernel shared
between head and omitted term. A new kernel can change the response
through (1). Distinct joint models fall outside the comparison.

[request]: ../research-progress/handoffs/VCD-E15-r1.md
[decision]: ../brainstorm/notes/08_VCD_B04_SHARED_MEMORY_COMPARISON_DECISION_20261116.md
[e04]: 04_VCD_E04_TAIL_FOUNDATIONS_20261116.md
[e06]: 06_VCD_E06_EXPONENTIAL_SCORE_RESIDUAL_20261116.md
[e07]: 07_VCD_E07_FINITE_CANONICAL_SCORE_CONTROLS_20261116.md
[e07screen]: 07_VCD_E07_FINITE_CANONICAL_SCORE_CONTROLS_20261116.md#3-catalog-screen
[e10]: 10_VCD_E10_SMOOTH_NEXT_DEFECT_FREEDOM_20261116.md
[e11]: ../reviews/05_VCD_E11_SMOOTH_DEFECT_ASSESSMENT_20261116.md
[e13]: 11_VCD_E13_MIDPOINT_AUDIT_20261116.md
[results]: ../../../../result-summaries/README.md
[cluster]: ../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md
[catalog]: ../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../avoid/README.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a02]: ../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a03]: ../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
