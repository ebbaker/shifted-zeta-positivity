# Finite canonical-score measurements and positive square-source controls

16 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex assistance. Recorded task dispatch **gpt-6.1-sol /
ultra**. Separate backend model and effort attestation unavailable.

**Status: proved in-note, internal analytical work.** This is an
information-sufficiency obstruction in the positive square-source class
specified below. It combines a finite linear measurement construction
with the inherited finite-source zero theorem and quantifies the error
of the unchanged theta score for every degree. The
[frozen request](../research-progress/handoffs/VCD-E07-r1.md) implements
[B02](../brainstorm/notes/04_VCD_B02_SCORE_INFORMATION_DECISION_20261116.md).
The [result index][results], [control catalog][catalog],
[avoid index][avoid], and patterns [01][a01], [02][a02] and [07][a07]
govern the scope. The earlier [finite-source audit][finite] and
[finite-prime control][orbit] supply the precedents for the zero theorem
and finite linear measurement constraints.

## 1. Finite information at time zero

Use the [manuscript][ms] source
\[
 \rho=\pi e^{4u},\qquad r_m=m^2\rho,\qquad
 s_m(u)=e^u(2r_m^2-3r_m)e^{-r_m},\qquad
 \Phi(u)=\sum_{m\ge1}s_m(u)\quad(u\ge0),
\]
with smooth even extension for \(\Phi\). For any positive even source
\(w\), let \(Z_{w,\lambda}=\int_{\mathbb R}e^{\lambda u^2}w(u)\,du\),
\(d\mu_{w,\lambda}=e^{\lambda u^2}w(u)\,du/Z_{w,\lambda}\), and let
\(q_{w,j}\) be the probability-orthonormal polynomials with positive leading
coefficients at the specified time. Write \(a_{w,n}\) for the Jacobi link
joining sites \(n-1\) and \(n\). Use the **same** test symbol
\(V_{\theta,\lambda}'=-(\log\Phi)'-2\lambda u\) in both score matrices:
\[
 S^\theta_{w,ij}(\lambda)
 =\int V_{\theta,\lambda}'(u)q_{w,i}(u)q_{w,j}(u)\,d\mu_{w,\lambda}(u).
\]
Thus \(S^\theta_{\Phi}\) is the canonical score matrix of [E05][e05].

**Claim.** Fix a finite coefficient head through \(a_{\Phi,L}(0)\), any
finite set of score indices \((i,j)\) at \(\lambda=0\), and any finite
source smoothness order \(K\ge0\). There is a strictly positive source
\(\Psi=\Phi+\epsilon f\), with \(f\ne0\) a finite real combination of
\(s_m\) for \(m\ge2\) on the positive half-line and reflected evenly.
It has the following properties.

- The mass, chosen head and selected entries of \(S^\theta(0)\) agree
  exactly with theta. Any additional finite real linear observations
  defined on the span of the chosen modes can also be preserved.
- The first mode remains unchanged. All square coefficients are
  positive and only finitely many differ from 1. The reflected source
  is at least \(C^K\) and has the same modewise confinement and Jacobi
  envelope as theta throughout \(0\le\lambda\le1/2\).
- The own and canonical scores differ by an arbitrarily small bounded
  function. Equation (4) gives the resulting uniform relative adjacent
  defect on the physical time band.
- For every real \(\lambda\), the literal half-line cosine transform
  of \(e^{\lambda u^2}\Psi\) has finitely many real and infinitely many
  nonreal zeros. The source eventually fails the smooth reflection
  of the canonical source at a finite odd derivative order.

Choose \(D\) at least \(L\) and at least every selected row and column
index. For the unknown finite combination \(f=\sum c_m s_m\), impose
\[
 \int_{\mathbb R}u^{2k}f(u)\,du=0\quad(0\le k\le D),\qquad
 \int_{\mathbb R}V_{\theta,0}'(u)q_{\Phi,i}(u)q_{\Phi,j}(u) f(u)\,du=0
 \quad((i,j)\text{ selected}).                                    \tag{1}
\]
The polynomials in (1) are evaluated at time zero. Add
\(f^{(j)}(0+)=0\) for every odd \(j\le K\), and set the change of each
additional linear observation to zero. The score integrals converge
absolutely since \(|V_{\theta,0}'(u)|\le C\pi e^{4|u|}\), as in E05,
and each mode has double-exponential decay. Parity makes some score
rows automatic. No rank assumption is needed.

Choose more modes with \(m\ge2\) than the number of real equations.
All chosen modes can lie above any prescribed square-mode cutoff.
A homogeneous nullspace vector \((c_m)\ne0\) gives \(f\ne0\): if
\(m_*\) is its least nonzero index, then \(f(u)/s_{m_*}(u)\to c_{m_*}\)
as \(u\to+\infty\), since every other ratio in the finite sum tends
to zero exponentially in \(\rho\). Fix this direction and take any
nonzero \(\epsilon\) with \(|\epsilon|\max_m|c_m|<1/2\). Then
\(\Psi=\sum b_m s_m\) on the half-line, where \(b_m=1+\epsilon c_m\)
on the selected modes and \(b_m=1\) elsewhere. Each summand is positive,
\(b_1=1\), and \(\Phi/2\le\Psi\le3\Phi/2\).

Evenness and (1) give equality of all moments through degree \(2D\),
including mass. The Gram matrices of monomials through degree \(D\)
therefore agree. Positive definiteness and the positive leading
coefficient convention fix the orthonormal polynomials through \(D\),
and the monic norms fix the links through \(a_D(0)\). Mass equality
keeps the probability normalization in the score rows. Substitution
of the common polynomials and common mass in (1) proves
\(S^\theta_{\Psi,ij}(0)=S^\theta_{\Phi,ij}(0)\) for all selected
\((i,j)\). In particular, taking all entries on sites \(0,\ldots,N-1\)
and the corresponding head keeps the full finite E05 correction
\(\Pi_N V_{\theta,0}'(J)\Pi_N - V_{\theta,0}'(J_N)\) equal, with the
canonical symbol in both terms.

For the reflection endpoint, analytically continue the **finite**
half-line expression for \(f\) along the real axis. It equals
\(e^u A(e^{4u})\), where
\(A(x)=\sum_m c_m(2\pi^2m^4x^2-3\pi m^2x)e^{-\pi m^2x}\)
is entire and nonzero by the mode independence argument. If all odd
endpoint derivatives vanished, this analytic continuation would be
even. At negative infinity it instead has the nonzero leading term
\(d e^{(1+4k)u}\) for the first Taylor term \(d x^k\) of \(A\) at zero.
At positive infinity it decays doubly exponentially. Hence there is a
least nonzero odd derivative of finite order \(j_* > K\). The even
extension is \(C^{j_*-1}\) and fails to be \(C^{j_*}\) at zero. Its
strict positivity and piecewise smoothness still give local absolute
continuity. The [finite-source proposition, §3][finite] has the same
mode normalization and applies to this nonzero finite change of theta.
It uses the surviving odd endpoint after every common heat tilt for
algebraic real-axis decay. Since the entire field has order one and
infinite type, the remaining zeros include infinitely many nonreal
zeros at each fixed real heat time. This conclusion uses the inherited
zero theorem only for its finite-change class.

## 2. A bounded score difference and relative adjacent defects

On \(u\ge0\), write \(g=f/\Phi\). The first mode lower bound and the
manuscript derivative estimates give
\[
 \Phi\ge e^u\rho^2e^{-\rho},\qquad
 |\Phi'/\Phi|\le C\rho,\qquad
 |f^{(j)}(u)|\le C_f e^u\rho^{2+j}e^{-m_*^2\rho}\quad(j=0,1).
\]
They imply \(g\) and \(g'\) are bounded on the half-line, with
\(|g'|\le C_f'\rho e^{-(m_*^2-1)\rho}\). The even extension of \(g\) is
locally absolutely continuous. With
\(V_{\Psi,\lambda}=-\log(e^{\lambda u^2}\Psi)\), the own score and
canonical score differ almost everywhere by
\[
 V_{\Psi,\lambda}'-V_{\theta,\lambda}'
 =-\frac{\epsilon g'}{1+\epsilon g},\qquad
 \Delta:=\|V_{\Psi,\lambda}'-V_{\theta,\lambda}'\|_\infty
 \le 2|\epsilon|\,\|g'\|_\infty.                                \tag{2}
\]
The common heat tilt cancels for every real \(\lambda\). The same bound
holds for any prescribed positive tolerance by reducing \(|\epsilon|\)
along the fixed nonzero direction. Since the score difference is a
bounded multiplication operator on \(L^2(\mu_{\Psi,\lambda})\), its
matrix entries in the \(\Psi\)-basis are each at most \(\Delta\) in
absolute value. This is a same-basis comparison of the two symbols.

Each positive constant \(b_m\) cancels in the individual log derivative
of \(b_ms_m\). Differentiated tail convergence for the bounded sequence
\((b_m)\) justifies the positive weighted mean of those derivatives.
Thus the [manuscript's confinement inequality and general envelope][ms]
apply to \(e^{\lambda u^2}\Psi\): the own score obeys
\(u V_{\Psi,\lambda}'(u)\ge\cosh(4u)-11\) almost everywhere, and
\[
 a_{\Psi,n}^2+a_{\Psi,n+1}^2\le B_n,
 \qquad B_n=\frac{\operatorname{arcosh}^2(2n+12)}{16},
 \qquad 0\le\lambda\le1/2 .                                    \tag{3}
\]
The required tail limits and integrability follow from the same mode
bounds. Local absolute continuity allows integration by parts across
the origin, with no jump term. The [own-score identity][e05] therefore
gives \(n=a_{\Psi,n}\int V_{\Psi,\lambda}' q_{\Psi,n}q_{\Psi,n-1}\,
 d\mu_{\Psi,\lambda}\) for every \(n\ge1\). Using the canonical symbol
with the control's links and polynomials gives
\[
 \frac{|a_{\Psi,n}S^\theta_{\Psi,n,n-1}(\lambda)-n|}{n}
 \le\frac{a_{\Psi,n}\Delta}{n}
 \le \frac{\Delta\operatorname{arcosh}(2n+10)}{4n}
 =O\!\left(\Delta\frac{\log(n+2)}{n}\right).                       \tag{4}
\]
The first inequality uses Cauchy–Schwarz for the two normalized
polynomials and the second uses \(B_{n-1}\). The estimate is uniform in
the physical time band. Exact equalities of the chosen entries and head
were imposed at time zero.

## 3. Catalog screen

Test the finite-data implication from strict positive even weights with
local absolute continuity and the requisite tails, the literal Fourier
observation, the envelope (3), exact finite mass/head/score data, and an
arbitrarily small bound of the form (2)–(4). Source reflection beyond a
fixed finite derivative order is an additional premise. A bare collision
in another family only tests this implication if the requisite premises
are met and the collision contradicts the proposed conclusion.

| Catalog family | Pass, fail or untested for the stated premises |
| --- | --- |
| Euler-factor translates | Positive, smooth, even, and literal Fourier heat flow. For \(a=\tfrac12\log p\) and \(c>0\), mass becomes \((1+c)Z_{\Phi,0}\) and the normalized second moment increases by \(ca^2/(1+c)\). Mass scaling cannot repair the first link. The checked \(c=1/2,p=23\) case also fails \(B_0\) at time zero. The dominant \(\Phi(u-a)\) tail gives own-score leading term \(4\pi e^{-4a}e^{4u}\), which fails the bounded score comparison. Finite score entries were not separately tested. [Earlier VCD screen][screen] |
| Three- and four-square finite sources | Pass positivity, local absolute continuity, literal observation and (3). Since the first coefficient is positive, their own score differs from theta by a bounded amount, by the same first-mode comparison at infinity. Arbitrarily small score tolerance and exact selected mass/head/score matches are untested for the certified examples. Full smooth reflection fails. [Manuscript §6][ms] |
| Reflected super-Gaussian | Passes smooth positivity and literal observation. The quartic translates give a polynomially bounded own score, so a bounded difference from the exponential canonical score and exponential confinement both fail. The coefficient envelope and exact head/rows are untested. [Catalog][catalog] |
| Smooth shape and positive-primitive controls | Pass smooth positivity and literal observation. Their own score is \(4\delta\sinh(4u)+O(u)\) by differentiating the damping factor, the Gaussian and the polynomial. Thus the sufficiently small damping constructions with \(\delta<2\pi\) fail a bounded score difference against theta's leading \(4\pi e^{4u}\). Coefficient envelope and exact head/rows are untested. [Shape Note 53 §3, (8)][shape], [primitive Note 56 §3, (12)–(13)][primitive] |
| Finite-source audit | Strictly positive bounded square-coefficient changes with the first mode retained pass (3) and the bounded score comparison. The audit alone gives the zero theorem and small measurement errors. The construction in §1 selects a member satisfying the full stated finite equality premises and (2)–(4), with the inherited nonreal-zero conclusion. Zero-tail examples are covered by the finite-source zero theorem on their own terms. [Finite-source audit][finite] |
| Finite-prime orbit controls | The orbit theorem allows the exact mass, moment and score rows in (1) among its finite measurements. It preserves the first mode and positivity. In the differentiated mode bound for \(j=0,1\), after factoring out \(e^u\rho^{2+j}e^{-m_*^2\rho}\), the bounded orbit coefficients are dominated by a constant times the summable \(m^{4+2j}e^{-\pi(m^2-m_*^2)}\). Thus (2)–(4) also hold and the orbit collision sequence has arbitrarily small score difference. The known witness is a double event at fixed positive time, at heights tending to infinity. Full smooth reflection fails. The inherited finite-source zero theorem above is used only for the finite-support change. [Orbit note, finite prime relaxation (1)–(4) and statement of the obstruction][orbit] |
| BW-01 fixed-event atoms and finite-profile threshold controls, including compact triangular extensions | Atoms fail the positive full-line density premise. The continuous compact extensions still fail strict full-line positivity, so the global own-score comparison does not apply. Calibrated profile values are separate observations from (1). [Catalog][catalog] |
| RH-conditional normalized endpoint control | Passes smooth positivity and literal observation. The exact Fourier mass fails because the spectral multiplier at \(x=0\) is \(a^4/(b^2c^2)=1+2e/(b^2c^2)>1\), using \(a^2=A-e\) and \((A+1-e)^2=(b^2+1)(c^2+1)\). Its normalization is at the completion endpoints. The relative source bound is known. The score tolerance and coefficient envelope are untested here. The constructed physical-time zeros are all real under RH, with an exact endpoint double. [Endpoint Note 05 §3, (9)–(12), (15)–(16) and §4][endpoint] |
| Fixed amplitude with variable observation | The unchanged source passes all coefficient and score tests. The variable kernel fails the literal cosine/Newman observation. [Catalog][catalog] |
| BW-08 actual-profile relaxation | Feasible fractional masses in a relaxed positive-measure problem do not give a full-line positive heat source with the literal Fourier observation and the retained score matrices. [Catalog][catalog] |

## 4. Remaining information

The fixed finite global implication fails in the stated relaxation even
with arbitrarily small relative all-degree defects of the specific form
(4). The controls fail complete square-source reflection at a finite odd
order despite satisfying any prescribed finite list of matching rows and
endpoint derivatives. The direction and its first uncancelled derivative
depend on that list. Matching all time-zero moments and mass would fix
the entire cosine transform, since its Taylor series consists of those
moments, and Fourier uniqueness would then fix the source.

There is no fixed zero location in this construction. For any bounded
real heat interval and bounded imaginary part of \(z\), the transform
difference is at most \(|\epsilon|\) times the finite integral of
\(|f(u)|e^{T u^2+Y u}\), with \(T\) an upper heat bound and
\(Y\ge|\operatorname{Im}z|\). On any compact set where the canonical
field has a positive lower modulus, this leaves it zero-free for
sufficiently small \(|\epsilon|\). A growing-degree induction for compact
shrinking-strip confinement may use an independent residual restriction,
full reflection, or a quantitative margin that changes with its retained
degree. Those premises have not been tested by (1)–(4). B03 owns the
decision about which new signed source information could pay an update.

[results]: ../../../../result-summaries/README.md
[catalog]: ../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../avoid/README.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a02]: ../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[ms]: ../manuscript/main.tex
[e05]: 05_VCD_E05_SOURCE_SCORE_RESIDUAL_20261116.md
[screen]: 02_VCD_ANALYTICAL_MANUSCRIPT_INTEGRATION_20261114.md
[finite]: ../../../investigations-3/07_source_measurement_audit/notes/round-2/01_REVIEW_RECONCILIATION_AND_ENDPOINT_NONREALITY_CODEX_20261017.md
[orbit]: ../../../investigations-3/11_arithmetic_collision_rigidity/notes/03_FINITE_PRIME_COMPATIBLE_COLLISION_CONTROLS_CODEX_20261018.md
[shape]: ../../../investigations-2/active/21_quaternion_theta_geometry/notes/05_theta_correlation_kernels/53_SOURCE_CONCAVITY_AND_POSITIVE_TIME_COLLISION_CONTROL_20261015.md
[primitive]: ../../../investigations-2/active/21_quaternion_theta_geometry/notes/05_theta_correlation_kernels/56_POSITIVE_PRIMITIVE_COLLISION_CONTROL_20261015.md
[endpoint]: ../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/notes/05_CLOSE_POSITIVE_SOURCES_AND_NORMALIZED_DOUBLE_ZEROS_20261020.md
