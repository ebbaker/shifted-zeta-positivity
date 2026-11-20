# E03 r1 — signed gap correction on a counted chart

19 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance. Explicit helper dispatch **gpt-6.2-sol /
ultra**. Independent serving-model and effort metadata are unavailable.
**Proved in-note under the stated chart and input hypotheses.** This
is the conditioned local estimate selected by
[B02](../brainstorm/notes/03_AGC_JH_B02_SIGNED_GAP_REMAINDER_20261119.md)
and bounded by the [E03 r1 request](../research-progress/handoffs/AGC_JH_E03_REQUEST_R1_20261119.md).
Classification and scope follow the [result index](../../../../../result-summaries/README.md),
[patterns index](../../../../../avoid/README.md),
[avoid01](../../../../../avoid/01_restating_the_target.md) and
[avoid07](../../../../../avoid/07_scoped_exclusions_read_as_universal.md).

## 1. The signed first variation and complete remainder

Use the B01 fixed circle \(\Gamma:|z-a|=r\), positively oriented, with
\(a\) real. On the closed disk and a neighborhood let \(Y=G_{N,t}\),
\(N\ge2\), and \(Z=F_t\) or \(G_{N+2,t}\). The physical field is the
unchanged normalized complete theta field with its cosine observation.
Assume both fields are conjugation-symmetric and each has two zeros
counted with multiplicities in the disk, with both pairs in
\(|z-a|\le r-b\) for a common \(0<b\le r\). Use a cleared collar and
\(q=(Z-Y)/Y\) with \(\sup|q|\le\eta<1\) there. The power series
\(\ell=\log(1+q)\) then gives a single-valued holomorphic collar
logarithm. Let \(q_0\) be a supplied continuous contour function with
\(\sup_\Gamma|q-q_0|\le e\). Write
\[
 \langle f\rangle=\frac{1}{2\pi i}\oint_\Gamma f(z)\,dz,\qquad
 B_Y=Y_z/Y,\qquad
 c_Y=\tfrac12\langle z B_Y\rangle,\qquad
 D_Y=\tfrac12\langle z^2 B_Y\rangle-c_Y^2 .
\]
These moments give the mean of the two roots and their squared
half-difference, including at a double. Put \(w=z-c_Y\) and denote
the changes from \(Y\) to \(Z\) by \(\Delta c,\Delta D\).

Since \(B_Z-B_Y=\ell_z\), integration by parts of the single-valued
logarithm around the closed curve yields
\[
 \Delta c=-\tfrac12\langle\ell\rangle,\qquad
 \Delta D=-\langle w\ell\rangle-\tfrac14\langle\ell\rangle^2 .
 \tag{1}
\]
In particular the linear part in \(q\) at zero is
\(-\langle wq\rangle\). Retain its supplied approximation
\(J=-\langle wq_0\rangle\). For the exact remainder
\(\mathcal R=\Delta D-J\), the identity and its bound are
\[
 \begin{aligned}
 \mathcal R&=-\langle w(\ell-q_0)\rangle-\tfrac14\langle\ell\rangle^2,\\
 |\mathcal R|&\le
 r(2r-b)\bigl[e-\log(1-\eta)-\eta\bigr]
       +\frac{r^2}{4}\bigl[-\log(1-\eta)\bigr]^2
       =:\mathcal A .
 \end{aligned}
 \tag{2}
\]
Indeed \(|c_Y-a|\le r-b\) gives \(\sup_\Gamma|w|\le 2r-b\).
The integral norm contributes \(r\). For \(k\ge2\) the absolute
Taylor terms of \(\ell-q\) sum to at most
\(\sum_{k\ge2}\eta^k/k=-\log(1-\eta)-\eta\). The series from \(k=1\)
bounds \(|\ell|\) by \(-\log(1-\eta)\). This pays the entire log
nonlinearity and the square of the center change. For \(0\le\eta\le1/4\),
\[
 -\log(1-\eta)-\eta\le \frac{\eta^2}{2(1-\eta)}
            \le \tfrac23\eta^2,\qquad
 -\log(1-\eta)\le\frac{\eta}{1-\eta}\le\tfrac43\eta .
\]
Consequently
\[
 |\mathcal R|
   \le r(2r-b)e+
      \left(\frac{16r^2}{9}-\frac{2rb}{3}\right)\eta^2 .
 \tag{3}
\]

Complex conjugation preserves \(c_Y,c_Z,D_Y,D_Z\) and the \(\ell\)
moments by reflection of the circle and reversal of orientation.
The supplied functions below have the same conjugation symmetry, so
\(J,\mathcal R\) are real. For a general supplied \(q_0\), (2) holds
in complex modulus and the reflected average
\((q_0(z)+\overline{q_0(\bar z)})/2\) makes \(J\) real while preserving
the error bound. No inverse internal gap occurs in (1)–(3). If
\(D_Y+J-\mathcal A>0\), then \(D_Z>0\) and the two counted roots
are distinct and real. Applying this implication to a time interval
requires the lower margin there at every required time.

An independently justified outer count of two for \(Y\) transfers
by Rouché when \(|Z-Y|<|Y|\) on \(\Gamma\). To acquire the buffer by
Rouché, choose \(0<b<r\), certify a count of two for \(Y\) strictly
inside \(|z-a|=r-b\), and check \(|Z-Y|<|Y|\) separately on that inner
circle. Its count and the outer count put both pairs inside the
smaller disk. Outer count equality alone gives no prescribed buffer.
A lower floor for \(|Y|\) on the chosen collar and the matching
numerator bound are one way to acquire \(\eta\).

## 2. Source-phase and finite-increment inputs

Suppress \(t\) and put \(L_j=(-1)^j h_j^* z^{2j}/(2j)!\) with
\(h_j^*=\prod_{k=1}^j\beta_k\). The unchanged source has
\(F-G_j=L_j E_j\). The inherited explicit bound is
\(|E_j-1|\le\epsilon_j(|z|,y_*)\) for \(|\Im z|\le y_*\le1\) and
\(t\in[0,1/2]\), where
\(\epsilon_j(R,y_*)=R^2\sqrt{2\mathcal A_j(y_*)\mathcal Q_j}/2\)
uses the explicit source and node envelopes in the cited phase
theorem. The exact factorization is entire. The quantitative
specializations using this bound require the relevant collar to be
inside the strip. The envelopes for \(\epsilon_j\) use \(j\) and the
proved theta bounds. \(\mathcal A_j,\mathcal Q_j\) here are the phase
theorem's constants. [VCD error law](../../../03_volterra_coefficient_dynamics/manuscript/sections/error_law.tex),
[VCD phase theorem](../../../03_volterra_coefficient_dynamics/manuscript/sections/phase.tex),
[VCD physical-time extension](../../../03_volterra_coefficient_dynamics/manuscript/sections/gap_transport.tex).

- For \(Z=F\), retain \(q_0=L_N/G_N\). Take \(e\) at least the
  supremum of \(|L_N|\epsilon_N/|G_N|\) on \(\Gamma\), and bound
  \(\eta\) by the collar supremum of \(|L_N|(1+\epsilon_N)/|G_N|\).
  The leading correction needs links through \(\beta_N\), including
  the first omitted edge of \(G_N\).
- For \(Z=G_{N+2}\), the exact source-error identity is
  \[
   G_{N+2}-G_N=L_NE_N-L_{N+2}E_{N+2}.
  \]
  With \(q_0=(L_N-L_{N+2})/G_N\), take \(e\) at least the supremum on
  \(\Gamma\) of
  \[
   \frac{|L_N|\epsilon_N+|L_{N+2}|\epsilon_{N+2}}{|G_N|}.
  \]
  One sufficient allowance for \(\eta\) is the collar supremum of
  \(|q_0|\) plus the corresponding collar bound for the phase errors.
  This retains the leading subtraction before taking its absolute
  value and pays both source phases. The leading difference needs
  links through \(\beta_{N+2}\). These termwise phase payments assume
  only the displayed envelopes. The full-source \(E_j\) involve the
  unchanged source law and remain unknown as functions under those
  envelope inputs.
- For the same finite update a second admissible choice is
  \(q_0=(G_{N+2}-G_N)/G_N\) exactly, so \(e=0\). In E02 (3)–(4),
  \[
   G_{N+2}-G_N=h_N^*\frac{1}{2\pi i}
      \oint_{\Sigma}\frac{\xi e^{iz\xi}}{P_N(\xi)P_{N+2}(\xi)}\,d\xi
      =L_N\left(\chi_{\rm cross}+
                \frac{z}{2N+1}\chi_{\rm cross}'\right).
  \]
  Here \(P_j\) are the monic Jacobi characteristic polynomials,
  \(\Sigma\) surrounds the finite source spectra and
  \(\chi_{\rm cross}\) is the characteristic transform of their
  combined list with uniform simplex weights, retaining repetitions.
  This formula and the exact readout difference both need only links
  through \(\beta_{N+1}\) at each slice. The collar floor and \(\eta\)
  still need acquisition. The exact finite increment is data from
  two finite readouts and supplies no exact value for \(F-G_N\).
  To evaluate the time defects explicitly, the \(N\)-site head
  needs \(\beta_N\) and the \(N+2\)-site head needs \(\beta_{N+2}\).
  [E02 degree and time interface](03_AGC_JH_DEGREE_TIME_INTERFACE_20261119.md).

## 3. Complete weighted forcing on every subinterval

For the fixed common chart on a compact time interval \(I\), the time
regularity and full exterior trace \(M_Y=S_{1,Y}\) are as in E01.
Writing \(Q_Y=(z-c_Y)^2-D_Y\) and \(A_Y=Y/Q_Y\), the formula
\(M_Y=-\langle (A_Y'/A_Y)/Q_Y\rangle\) extends through a double. Put
\(f_Y=R_Y/Y\), \(R_Y=(\partial_t+\partial_z^2+\beta_1)Y\), and
\(r_Y=-\langle(z-c_Y) f_Y\rangle\), with analogous definitions for
\(Z\). For the normalized physical \(F_t\) its \(R_F=0\). For
\(G_{j,t}\) the actual moving-head defect is
\(R_j=\beta_j\beta_{j-1}\partial_{\beta_{j-1}}G_{j,t}\).
[E01 forced integer hierarchy](02_AGC_JH_FORCED_INTEGER_HIERARCHY_20261119.md).

On the collar the shared scalar normalization cancels in E02 (11):
\[
 \ell_t=-\ell_{zz}-2B_Y\ell_z-(\ell_z)^2+f_Z-f_Y .
 \tag{4}
\]
Differentiation of (1) gives its gap combination
\[
 \partial_t\Delta D=-\langle(z-c_Z)\ell_t\rangle+
                  \Delta c\langle Y_t/Y\rangle ,
\]
using \(\partial_t c_Y=-\langle Y_t/Y\rangle/2\).
This is the difference of the two differentiated argument-principle
moments. Equivalently, using \(\bar c=(c_Y+c_Z)/2\),
(1) gives \(\Delta D=-\langle(z-\bar c)\ell\rangle\). Its time
derivative is the raw combined difference in E02 (14).
The pair laws \(\partial_t D_i=2-4M_iD_i+r_i\) for
\(i=Y,Z\) give the equivalent form
\[
 \partial_t\Delta D +4M_Y\Delta D
       =\mathcal P,\qquad
 \mathcal P=-4(M_Z-M_Y)D_Z+r_Z-r_Y .
 \tag{5}
\]
The same subtraction gives \(4M_Z\Delta D\) on the left if the right
uses \(-4(M_Z-M_Y)D_Y+r_Z-r_Y\).
In (5) use the real, positive weight
\(W(s,v)=\exp(-4\int_s^v M_Y(t)\,dt)\). For every \(u\le v\) in \(I\),
\[
 \begin{aligned}
 \int_u^v W(s,v)\mathcal P(s)\,ds
   &=\Delta D(v)-W(u,v)\Delta D(u),\\
 \left|\int_u^v W(s,v)\mathcal P(s)\,ds
            -\bigl[J(v)-W(u,v)J(u)\bigr]\right|
   &\le \mathcal A(v)+W(u,v)\mathcal A(u) .
 \end{aligned}
 \tag{6}
\]
The first line is E02 (15) and E01 (9), in the orientation of (5).
It follows by differentiating \(W(s,v)\Delta D(s)\) in
\(s\). The bound uses (2) at the two endpoints. Thus each partial
interval can use its own endpoint corrections and paid error.
Formula (6) needs no time derivative of \(q_0\). If
\(|W(u,v)-\widehat W|\le\omega\) with \(\widehat W\ge0\), replacing
the endpoint approximation by \(J(v)-\widehat W J(u)\) gives a
radius \(\mathcal A(v)+(\widehat W+\omega)\mathcal A(u)+\omega|J(u)|\)
for the same exact weighted aggregate. The complete
\(M\) in E01, including the \(12S_2+16DS_3\) contribution in its
differential law, has undergone no truncation in (5). Formula (6)
controls the weighted aggregate. Individual drift and heat defect
integrands would require their own information.

The same-information direct comparator evaluates the argument-principle
moments on the same fixed circle. With identical counts, floors,
\(q_0,e,\eta\) and weight data it can use (1)–(3), and subtract the same
two endpoint gaps to obtain (6). With the exact finite readouts it can
also use their full logarithm. Keeping the first variation provides a
quadratic-in-\(\eta\) allowance plus the paid source error. The comparator
has all the same source information and can compute the same enclosure.
No computational advantage is established by this comparison.
[Joint-payment pattern](../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md).

## 4. Exact nonvacuity and the collision controls

On the toy chart \(a=0,r=1,b=1/2\), put
\(Y=z^2\), \(Z=(z-k)^2-h\), \(k=1/128\), \(h=\pm1/64\).
Both pairs obey the buffer. For \(3/4<|z|<5/4\),
\(q=q_0=-2k/z+(k^2-h)/z^2\) satisfies
\(|q|\le 449/9216<1/20\). Residues give \(D_Y=0,\ D_Z=h,\
\Delta c=k,\ J=h-k^2\), so the exact error is \(k^2\). At
\(\eta=1/20,e=0\), (3) gives \(13/3600\), smaller than
\(|J|\) for either sign. The example distinguishes positive and
negative gaps within the stated allowance, right from a double
reference. It is an exact polynomial check outside the Jacobi data.

The [collision controls](../../../../../result-summaries/12_collision_controls_and_screening.md)
and the [branch source screen](../research-overview/01_AGC_JH_RESEARCH_OVERVIEW_20261119.md)
test the premises of any stronger interpretation, as in
[avoid02](../../../../../avoid/02_shape_only_arguments_and_the_controls.md).
For any control with an exact double in a valid count-two chart, its
two-root \(D_Z=0\) at that event forces \(D_Y+J-\mathcal A\le0\).
The lower bound is negative when the counted pair is nonreal.
This event-domain check applies wherever the controls satisfy the
stated chart inputs.

| Control from the source screen | Premise absent from a canonical application |
| --- | --- |
| Euler-factor and Dirichlet-arithmetic perturbations | Unchanged ordinary Dirichlet coefficients and hence the literal complete theta source. Their shared positivity and heat law are compatible with the generic estimate. |
| Weighted-square and finite-source or finite-score variants | Unchanged complete square weights and full reflection, or the full canonical sequence in the finite-score setting. A fixed compact nonreal-zero location is not supplied by finite-score matching. |
| Reflected super-Gaussian | The unchanged arithmetic square expansion. Its reflection and Fourier–Gram positivity are compatible with a double. |
| Smooth shape and positive-primitive controls | The exact theta square expansion, despite the shared shape and primitive information. |
| Finite-prime orbit controls | Full canonical reflection and unchanged square coefficients, despite finite-prime agreement. |
| Atomic threshold, finite-profile controls and their compact continuous extensions | The full theta profile and growth, unchanged coefficients and eventual simplicity at the threshold. Selected profiles and moments do not supply these premises. |
| Variable observation kernel at fixed theta amplitude | The literal cosine observation and its full oscillator/Newman equation. |
| Three-profile positive-measure relaxation | A realizable exterior integer zero divisor, which the full trace interpretation assumes through actual counted fields. |

The canonical sign of \(J\), any positive seed satisfying
\(D_Y+J>\mathcal A\), and the chart, count, floor and accumulation data
for induction remain open inputs. The exact finite update establishes
a local two-readout comparison. An all-degree limit estimate requires
further control. Evidence here consists of the proof and the exact
polynomial check, pending internal assessment.

