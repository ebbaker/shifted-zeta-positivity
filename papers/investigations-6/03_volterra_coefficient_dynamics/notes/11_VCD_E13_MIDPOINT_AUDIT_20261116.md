# VCD-E13 r1 — Midpoint foundation audit

16 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance. Recorded task dispatch **gpt-6.1-sol / ultra**.
Separate runtime model and effort attestation unavailable.

**Complete, proved in-note.** The five groups in [plan §15][plan] are
checked against the [frozen request][request] and [input manifest][manifest].
All eleven input hashes match. The midpoint formulas are exact
representations, and the compact convergence statements concern
approximation. This audit uses the [author's insertion and bra convention][discussion],
[overview §4.1][overview], and the domains accepted for [E04][e04]
in [E09][e09]. The [result index][results], [coefficient cluster][cluster],
[avoid index][avoid], and patterns [01][a01], [02][a02], [03][a03]
and [07][a07] govern the classification and screen.

Fix \(\lambda\in[0,1/2]\), with \(\lambda=0\) the zero objective. Keep
the complete canonical \(W_\lambda=e^{\lambda u^2}\Phi\),
\(Z_\lambda=\int_{\mathbb R}W_\lambda(u)\,du\),
\(d\mu_\lambda=W_\lambda\,du/Z_\lambda\), and
\[
 F_\lambda(z)=\int_{\mathbb R}e^{izu}\,d\mu_\lambda(u)
             =2H_\lambda(z)/Z_\lambda .
\]
The unitary spectral representation \(U\) sends \(e_n\) to the real
\(\mu_\lambda\)-orthonormal polynomial \(q_n\), with \(q_0=1\).
It sends \(J=J(\lambda)\) to multiplication by \(u\). Write
\(a_n^2=\beta_n\) for the link between \(n-1\) and \(n\).
The projection \(\Pi_N\) retains sites \(0,\ldots,N-1\) for \(N\ge1\).
The finite compression is \(J_N\), and \(Q_N=I-\Pi_N\).

## 1. Bilinear identity, bra sign and normalization

The Hermitian convention is \(\langle v,w\rangle=v^*w\). For real \(t\)
the bra of \(e^{itJ}e_0\) is \(e_0^*e^{-itJ}\).
For any \(z\in\mathbb C\) let
\[
 c(z)=e^{izJ/2}e_0,\qquad
 c_n(z)=\langle e_n,c(z)\rangle=\int q_n(u)e^{izu/2}\,d\mu_\lambda(u).
\]
In the spectral representation the orbit is the \(L^2(\mu_\lambda)\)
vector \(e^{izu/2}\). This multiplier is square integrable on the fixed
input \(1\) at every \(z\), as in [E04 §4][e04]. If \(C\) is
coordinatewise conjugation in the polynomial basis, then
\(Uc(z)=\exp(izu/2)\) gives \(Cc(z)=c(-\bar z)\), since \(U\) intertwines
the two conjugations. In particular the bra of \(c(z)\) is
\(e_0^*e^{-i\bar zJ/2}\) on the domain of that operator, with bounded
extension as a functional given by \(c(z)^*\).

For \(v,w\in\ell^2\) write
\(B(v,w)=\langle Cv,w\rangle=\sum_n v_nw_n\).
The pairing is continuous by Cauchy–Schwarz and equals
\(\int (Uv)(Uw)\,d\mu_\lambda\). Therefore
\[
 F_\lambda(z)=B(c(z),c(z))
             =\langle c(-\bar z),c(z)\rangle
             =\sum_{n\ge0} c_n(z)^2 .
\]
All products in this argument are pairings of square-integrable vectors.
For real \(x\) the Hermitian expression uses the state at \(-x/2\) in
its first slot and the state at \(x/2\) in its second slot. The pairing
of \(c(x)\) with itself in the Hermitian norm is \(1\).

Evenness gives \(q_n(-u)=(-1)^nq_n(u)\), so
\(c_n(-z)=(-1)^n c_n(z)\). On the real axis \(c_n(x)\) is real for even
\(n\) by the cosine integral and purely imaginary for odd \(n\) by the
sine integral. Equivalently \(c_n(x)=i^n b_n(x)\) for real \(b_n(x)\),
and \(F_\lambda(x)=\sum_n(-1)^n b_n(x)^2\) with
\(\sum_n b_n(x)^2=1\). At \(z=0\) the orbit is \(e_0\), giving
\(F_\lambda(0)=1\).

## 2. Entire head and tail on the fixed orbit

For \(z=x+iy\), the spectral norm gives
\[
 \|c(z)\|^2=\int e^{-yu}\,d\mu_\lambda(u)=F_\lambda(iy)
            =\int\cosh(yu)\,d\mu_\lambda(u).
\]
Set \(\mathbf c_N=\Pi_Nc\), \(d_N=Q_Nc\),
\(S_N=\sum_{n<N}c_n^2\), \(R_N=\sum_{n\ge N}c_n^2\). The sum of
absolute values of the terms defining \(R_N\) is exactly
\(\|d_N(z)\|^2\). The norm-holomorphic orbit of E04 has compact image on
each compact \(K\subset\mathbb C\). Since \(\|Q_N\|\le1\) and
\(Q_Nv\to0\) for every \(v\in\ell^2\), taking a finite norm net for
that image proves
\[
 \sup_{z\in K}|R_N(z)|
 \le\sup_{z\in K}\sum_{n\ge N}|c_n(z)|^2
 =\sup_{z\in K}\|d_N(z)\|^2\longrightarrow0 .
\]
Thus the squares converge absolutely and locally uniformly, and
\(S_N\) and \(R_N=F_\lambda-S_N\) are even entire functions.

The fixed-disk tail convergence also holds uniformly in the allowed
time band. Indeed, \(Q_NJ^p e_0=0\) for \(p<N\) by finite propagation.
The E04 bound with its time-independent constant \(C_*\) gives
\(\|J^p e_0\|\le[2C_*\log(p+2)]^p\) for \(p\ge1\).
On \(|z|\le\rho\), the projected vector norm is bounded by the tail
from \(p=N\) onward of the convergent midpoint Taylor majorant
\(\sum_{p\ge1} [\rho C_*\log(p+2)]^p/p!\).
The estimate concerns the fixed input \(e_0\) and a fixed disk. For
the moving tail origin \(e_N\), E04 instead proves
\(\sup_{N\ge1}k_N(ib)=\infty\) at every fixed \(\lambda\) and every
real \(b\ne0\), where \(k_N(w)=\langle e_N,e^{iwJ^{[N]}}e_N\rangle\).

## 3. Finite-head baseline and excursions

Put \(\mathbf c_N^0(z)=e^{izJ_N/2}e_0\) on the finite head. In the
model with these amplitudes and zero omitted term, \(J_N^{\mathsf T}=J_N\)
gives for every complex \(z\)
\[
 (\mathbf c_N^0(z))^{\mathsf T}\mathbf c_N^0(z)
  =e_0^{\mathsf T}e^{izJ_N/2}e^{izJ_N/2}e_0
  =F_{\lambda,N}(z).
\]
This is precisely E04's Gaussian quadrature. Its convergence on fixed
complex disks is the inherited quadrature result.

The exact retained vector includes walks leaving the finite block.
For instance \(c_0(z)=F_\lambda(z/2)\). Its first Taylor derivative
that differs from the finite-head amplitude at site zero is
\[
 \left.(c_0-(\mathbf c_N^0)_0)^{(2N)}\right|_{z=0}
 =(-1)^N2^{-2N}\prod_{j=1}^N\beta_j .
\]
It comes from the shortest excluded return walk
\(0\to1\to\cdots\to N\to\cdots\to0\), using the outside link \(a_N\).
Thus the exact midpoint head already requires information beyond
\(J_N\). It is a finite sum of entire amplitudes, with \(S_1(z)=F_\lambda(z/2)^2\)
as one example.

## 4. Joint error and common boundary memory

For proposed retained amplitudes \(\widetilde{\mathbf c}_N\) and a
proposed scalar omitted contribution \(\widetilde R_N\), put
\(G_N=\widetilde{\mathbf c}_N^{\mathsf T}\widetilde{\mathbf c}_N+\widetilde R_N\).
The exact difference is
\[
 F_\lambda-G_N
    =(\mathbf c_N+\widetilde{\mathbf c}_N)^{\mathsf T}
       (\mathbf c_N-\widetilde{\mathbf c}_N)+(R_N-\widetilde R_N).
\]
With \(E_c=\|\mathbf c_N-\widetilde{\mathbf c}_N\|\) and
\(E_R=|R_N-\widetilde R_N|\), this gives
\[
 |F_\lambda-G_N|\le (2\sqrt{F_\lambda(iy)}+E_c)E_c+E_R .
\]
The norm factor is bounded on fixed compact sets. In the whole
time band the bound follows from
\(\mu_\lambda(du)\le W_{1/2}(u)\,du/Z_0\), as in [E04 §5][e04].
If both errors tend uniformly to zero on each fixed compact set,
this estimate delivers local uniform convergence. A zero argument
would still need quantitative control of the signed cancellation
or a lower modulus on the relevant region with enough separation
from the joint error. Separate absolute budgets contain no
information about how the two scalar errors cancel or reinforce.
See [avoid 12][a12].

Write \(A=J_N\), \(D=J^{[N]}\), and \(e=e_{N-1}\).
In E04's height \(w\), before midpoint rescaling, put
\(y_N(w)=\Pi_Ne^{iwJ}e_0\) and \(v_N(w)=Q_Ne^{iwJ}e_0\).
The equations with \(y_N(0)=e_0,\ v_N(0)=0\) are
\[
 \begin{aligned}
 y_N'(w)&=iAy_N(w)-\beta_N e\int_0^w k_N(w-t)(y_N(t))_{N-1}\,dt,\\
 v_N(w)&=ia_N\int_0^w e^{i(w-t)D}e_N(y_N(t))_{N-1}\,dt .
 \end{aligned}
\]
For complex heights the integrals run on oriented straight segments.
The tail integral extends as an entire Hilbert-space-valued function
by the E04 normally convergent vector series on \(e_N\), the scalar
entire boundary component, and the substitution \(t=\theta w\).
Agreement on the real axis then extends it to the entire tail
orbit, as can also be checked componentwise.

At \(w=z/2\), \(\mathbf c_N(z)=y_N(z/2)\) and
\(d_N(z)=v_N(z/2)\). Use \(t=s/2\) in both integrals and the
chain-rule factor \(1/2\) in \(\mathbf c_N'(z)\). With
\(f_N(s)=(\mathbf c_N(s))_{N-1}\), the rescaled equations are
\[
 \begin{aligned}
 \mathbf c_N'(z)
   &=\frac{i}{2}A\mathbf c_N(z)
          -\frac{\beta_N}{4}e\int_0^z k_N((z-s)/2) f_N(s)\,ds,\\
 d_N(z)
   &=\frac{ia_N}{2}\int_0^z e^{i(z-s)D/2}e_N f_N(s)\,ds .
 \end{aligned}                                                    \tag{1}
\]
Variation of constants in the finite head gives the retained
correction relative to the bare midpoint baseline:
\[
 \mathbf c_N(z)-\mathbf c_N^0(z)=
 -\frac{\beta_N}{4}\int_0^z ds\int_0^s dr\,
   e^{i(z-s)A/2}e\, k_N((s-r)/2)f_N(r).
\]
The omitted term \(R_N(z)=B(d_N(z),d_N(z))\) has a scalar form using
the same \(k_N\). In the tail, complex conjugation commutes with \(D\)
on its domain, by reality and the finite-sequence core of E04 §2.
It consequently intertwines the spectral multipliers with their
conjugates. On the fixed orbit issued from \(e_N\), the bilinear
pairing of the two tail vectors in (1) is
\[
 B(e^{i(z-s)D/2}e_N,e^{i(z-t)D/2}e_N)
       =k_N\bigl(z-(s+t)/2\bigr).
\]
This equality uses the spectral measure at \(e_N\) and multiplication
of the two scalar exponentials inside that integral. The integrals
in (1) are continuous along compact segments. Bilinear continuity
therefore gives
\[
 R_N(z)=-\frac{\beta_N}{4}\int_0^z\!\int_0^z
       k_N\bigl(z-(s+t)/2\bigr) f_N(s)f_N(t)\,dt\,ds .              \tag{2}
\]
For a point \(z\), the retained memory uses kernel arguments on
the segment from \(0\) to \(z/2\). The omitted square uses arguments
on the segment from \(0\) to \(z\). The link \(a_N\) and the same
boundary response occur in both terms. A scalar kernel model
used through (1)–(2) would consequently need coverage for the
full segment, including control of the resulting head response.

As an exact factor check, take a two-site chain with link \(a>0\)
and cut at \(N=1\). Then \(A=D=0\), \(k_1=1\),
\(c_0(z)=\cos(az/2)\), and \(d_1(z)=i\sin(az/2)e_1\).
Equation (1) differentiates the cosine and recovers the sine
with its factor \(i\), and (2) gives \(R_1=-\sin^2(az/2)\).
The complete square sum is \(\cos(az)\) and the one-site baseline
is \(1\).

The source interface comes from [E05][e05]–[E06][e06]. E05 gives
\(a_n[V_\lambda'(J)]_{n,n-1}=n\) and the score compression at the
cut. In E06 notation,
\(T_N(t)e_0=\mathbf c_N(-2it)\) and \(K_N(t)=k_N(-it)\).
The score compression uses the full retained matrix at real
exponential parameters \(t=\pm4\), or \(z=\mp8i\) in midpoint
notation. The bounded-symbol correction remains
\(\Pi_N b(J)\Pi_N-b(A)\), with norm at most \(2C_b\), for the
E06 decomposition \(V_\lambda'(u)=8\pi\sinh(4u)-2\lambda u+b(u)\).
Those constraints cover selected exponential information. A
quantitative transfer to the Fourier heights and the joint signed
error in (1)–(2) remains open.

## 5. Degree increments and control scope

The projections give \(S_{N+1}-S_N=c_N^2\) and
\(R_N-R_{N+1}=c_N^2\), where \(c_N\) here is the scalar amplitude
at entering site \(N\). Each increment uses that full-chain
amplitude. Recursion for the responses in E04 expresses the
shallower kernel using a deeper kernel and a boundary link.
For predictive induction the additional information must enter
through a quantitative canonical restriction on those inputs and
their resulting boundary response, an independently justified
starting or limiting condition, and a Fourier estimate sensitive
to the signed cancellation.

The bilinear identity, convergence on fixed compacts, and finite
baseline apply to even sources with the exponential moments
used above and their corresponding Jacobi representation. The
boundary identities use the fixed tail vector domains. The
weighted-square examples, E07 and E10 have the exponential
moments and coefficient envelope needed for the same domains.
The source and readout comparison follows the
[collision catalog][catalog], the inherited [overview screen][screen]
and [E07's detailed screen][e07screen].

| Control | Premise comparison |
| --- | --- |
| Positive three- and four-square sources | The envelope and the generic identities survive at the validated collisions. Complete equal square coefficients and full reflection fail. |
| Finite-source changes and finite-prime orbits | They change the complete source. The orbit controls fail full canonical reflection, while fixed finite measurements and bounded score tolerance can survive. |
| Euler-factor translates | The canonical summand score changes. The checked \(c=1/2,p=23,\lambda=0\) example fails the coefficient envelope. |
| Reflected super-Gaussian | Exponential confinement fails. The stated source still has the moments for the midpoint identity. |
| Smooth shape and positive-primitive sources | The theta square-summand formula fails. Compact convergence from exponential moments still applies. |
| Finite atoms and finite-profile threshold examples | The atomic examples have finite-chain analogues and lack a positive full-line density. Compact triangular extensions also fail global strict positivity. |
| RH-conditional normalized endpoint examples | Ordinary Dirichlet arithmetic and the unchanged theta formula fail. Their existing conclusions have the stated RH hypothesis. |
| Fixed amplitude with varied readout | The source identities survive. The varied observation fails the literal Fourier/Newman readout. |
| Actual-profile positive-measure relaxation | The relaxation lacks the specified full-line source and physical Fourier field. |

[E07][e07], within the positive finite square-mode change class, keeps
fixed finite canonical-score/head measurements and arbitrarily
small bounded score difference, yet has nonreal zeros by the
inherited theorem for that class. The failed full reflection,
the time-zero scope of the exact finite matches and the absence
of a prescribed zero location are part of the [E09][e09] assessment.
[E10][e10], within its smooth compact-multiplier class, keeps the
reflection jet, real tails, specified time-zero head and lower
defects, and the envelope, while allowing either sign of the next
canonical score defect. Its constant square-mode representation
fails in the absolutely convergent class checked by [E11][e11].
The smooth control's Fourier zero locations are open. A future
candidate must identify which new quantitative premise excludes
the relevant control and prove it in the canonical case. Failure
of the source formula alone gives no test of an unspecified
derived inequality.

The exact all-degree score equations identify the source under
[E08's][e08] hypotheses. The existing unspecified shrinking-strip
criterion for convergent approximants at \(\lambda=0\) has the
RH-equivalent status established in [E04 §5][e04]. The present
audit verifies the midpoint approximation and its two errors.
A predictive update and a signed Fourier implication remain
B04's open tasks.

[request]: ../research-progress/handoffs/VCD-E13-r1.md
[manifest]: ../numerics/07_VCD_MIDPOINT_SESSION_INPUTS_20261116.json
[plan]: ../research-plan/02_VCD_TAIL_CLOSURE_INDUCTION_RESEARCH_PLAN_20261116.md#15-vcd-e13--midpoint-identity-approximation-ledger-and-baseline
[discussion]: ../brainstorm/notes/03_VCD_INDUCTION_TRUNCATION_AND_ZERO_CONTROL_20261116.md#endpoint-insertion-versus-truncating-the-dynamics
[overview]: ../research-overview/02_VCD_TAIL_CLOSURE_INDUCTION_RESEARCH_OVERVIEW_20261116.md#41-midpoint-mode-truncation-and-a-joint-closure
[screen]: ../research-overview/02_VCD_TAIL_CLOSURE_INDUCTION_RESEARCH_OVERVIEW_20261116.md#7-control-screen-and-the-scope-of-possible-failures
[e04]: 04_VCD_E04_TAIL_FOUNDATIONS_20261116.md
[e05]: 05_VCD_E05_SOURCE_SCORE_RESIDUAL_20261116.md
[e06]: 06_VCD_E06_EXPONENTIAL_SCORE_RESIDUAL_20261116.md
[e07]: 07_VCD_E07_FINITE_CANONICAL_SCORE_CONTROLS_20261116.md
[e07screen]: 07_VCD_E07_FINITE_CANONICAL_SCORE_CONTROLS_20261116.md#3-catalog-screen
[e08]: 08_VCD_E08_FULL_SCORE_RIGIDITY_20261116.md
[e09]: ../reviews/04_VCD_E09_TAIL_SCORE_ASSESSMENT_20261116.md
[e10]: 10_VCD_E10_SMOOTH_NEXT_DEFECT_FREEDOM_20261116.md
[e11]: ../reviews/05_VCD_E11_SMOOTH_DEFECT_ASSESSMENT_20261116.md
[results]: ../../../../result-summaries/README.md
[cluster]: ../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md
[catalog]: ../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../avoid/README.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a02]: ../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a03]: ../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
