# VCD-E24 r1 — Directed quadrature error at a fixed coefficient cost

16 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex assistance. Recorded explicit dispatch **gpt-6.1-sol / ultra**.
Separate backend and lead-configuration attestation unavailable.

**Proved in-note under the stated quadrature-error and phase inputs.**
The exact local error comparison favors the next physical quadrature
at equal coefficient cost. At the smaller prefix, a directed enclosure
uses the positivity of the missing coefficient to restrict possible
zero locations and transfer counts on separated contours. The phase
identification and budget were taken as inputs from decision12 during
parallel work. The completed-source pins belong to the [return][return].
This is an intermediate estimate and consumer as classified in
[pattern01][a01]. See [decision13][decision], [result index][results],
[cluster18][cluster], [avoid index][avoid], [control catalog12][catalog]
and patterns [02][a02], [07][a07] and [12][a12].

## 1. Fixed source and inputs

Use the unchanged complete even theta density at heat time zero,
normalized to the probability measure \(d\mu=\Phi(u)\,du/Z\).
Write \(F(z)=\int e^{izu}\,d\mu(u)\). The links of its zero-diagonal
Jacobi matrix are \(\sqrt{\beta_j}>0\) between \(j-1\) and \(j\), with
\(\beta_0=0\). The \(N\)-site prefix is \(J_N\), for integers \(N\ge1\),
and \(G_N=e_0^{\mathsf T}e^{izJ_N}e_0\). The probability monic norm is
\(h_N^*=\prod_{j=1}^N\beta_j\), since it telescopes from \(h_0^*=1\).
The proved adjacent envelope and the polynomial-density exponential
moment come from [E01 §§1–3][e01]. In particular
\[
 B_j=\frac{\operatorname{arcosh}^2(2j+12)}{16},\qquad
 \beta_j+\beta_{j+1}\le B_j .
\]

Put \(d_N(z)=(-1)^N z^{2N}\) and \(L_N(z)=d_N(z)h_N^*/(2N)!\).
For the physical tail and zero modeled memory, the left side of the
exact E15 difference is \(F-G_N\). The input selected in [decision12][phase]
identifies this entire difference with \(L_N E_N\), where \(E_N(z)\)
is the even entire transform of the symmetric Hermite remainder law.
It has \(E_N(0)=1\) and
\[
 \sigma_N^2=-E_N''(0)
 =\frac{2(\beta_N+\beta_{N+1}+S_{2,N})}{(2N+1)(2N+2)},
 \qquad S_{2,N}=\operatorname{tr}J_N^2=2\sum_{j=1}^{N-1}\beta_j .
 \tag{1}
\]
The trace counts the two oriented length-two returns over each link,
and is zero when \(N=1\). For the quantitative conclusions use the
degree-only input
\[
 |E_N(z)-1|\le \epsilon_N(|z|,Y)=k_N(Y)|z|^2,
 \quad 0\le Y\le1,\quad |\Im z|\le Y,
 \qquad k_N(Y)=O\!\left(\frac{\log^2(N+1)}{N}\right)
 \tag{2}
\]
with a uniform constant on \(0\le Y\le1\). The explicit budget in
decision12 uses the upper fourth moment and exponential allowance.
[E15 §3][e15] and [decision12][phase]

## 2. Comparison with the next physical quadrature

The monomial-corrected model \(C_N=G_N+L_N\) uses exactly
\(\beta_1,\ldots,\beta_N\). The matrix for \(G_N\) uses the first
\(N-1\) links, and \(L_N\) requires \(\beta_N\). Likewise \(G_{N+1}\)
uses precisely the first \(N\) links. Each link \(\beta_j\) in a
finite quadrature first enters its derivative of order \(2j\). The
unique first walk to site \(j\) and back contributes
\((-1)^j\prod_{i=1}^j\beta_i\) to that derivative, and the other
walks in that order use only earlier links. This also checks that
the required links can be read in sequence from either model's germ,
with the last one read from \(L_N\) in the corrected model. For \(N=1\),
\(G_1=1\), the product over its links is empty, and both \(C_1\) and
\(G_2\) require only \(\beta_1\).

At \(z\ne0\), telescoping and the normalization give the exact ratio
\[
 \frac{L_{N+1}(z)}{L_N(z)}
   =-\frac{\beta_{N+1}z^2}{(2N+1)(2N+2)} .
 \tag{3}
\]
The ratio extends at zero as the displayed polynomial. The unacquired
link \(\beta_{N+1}\) is used to describe the actual next error. A bound
uses \(\beta_{N+1}\le B_N-\beta_N\le B_N\), which incurs no extra
coefficient acquisition. The following are allowances after division
by \(|L_N(z)|>0\).
\[
 \begin{aligned}
 \frac{|F(z)-G_{N+1}(z)|}{|L_N(z)|}
 &\le \frac{(B_N-\beta_N)|z|^2}{(2N+1)(2N+2)}
               (1+\epsilon_{N+1}(|z|,Y)),\\
 \frac{|F(z)-C_N(z)|}{|L_N(z)|}&\le \epsilon_N(|z|,Y).
 \end{aligned}
 \tag{4}
\]
On a common bounded-phase range, for example
\(|z|\le c\sqrt N/\log(N+1)\) with fixed \(c>0\), within the strip in
(2), \(\epsilon_N\) and \(\epsilon_{N+1}\) are uniformly bounded.
Using the larger degree-only \(B_N\) in the first allowance gives
order \(|z|^2\log^2(N+1)/N^2\). The explicit allowance (2) in the
second has order \(|z|^2\log^2(N+1)/N\). For this latter order, the
upper fourth moment used in (2) includes
\(12\overline S_{2,N}^{\,2}/[(2N+1)(2N+2)(2N+3)(2N+4)]\), where
\(\overline S_{2,N}=2(N-1)B_{N-2}\) for \(N\ge2\). This term has
order \(\log^4(N+1)/N^2\) and all terms are nonnegative. The
exponential allowance is at least one, so the displayed rate is
two-sided for this particular budget as \(N\to\infty\). The estimates
at zero hold for the respective unnormalized errors, which both
vanish there.

For the exact local comparison, evenness and (1) give
\(E_N(z)-1=-\sigma_N^2 z^2/2+O(z^4)\). The leading term is nonzero,
since the links are positive. Equation (3) and \(E_{N+1}(0)=1\)
then give, along any complex approach through nonzero \(z\),
\[
 \lim_{z\to0}\frac{F(z)-C_N(z)}{F(z)-G_{N+1}(z)}
   =\frac{\beta_N+\beta_{N+1}+2\sum_{j=1}^{N-1}\beta_j}
                {\beta_{N+1}}>1 .
 \tag{5}
\]
Both errors have order exactly \(2N+2\) at zero. The denominator
after factoring out this zero has a nonzero constant term. The
quotient therefore extends holomorphically near zero. Its modulus
is greater than one on a sufficiently small punctured disk for each
fixed \(N\). At \(N=1\) the limit is \(1+\beta_1/\beta_2\).
The strict actual ordering has this local scope. No ordering of
actual errors across the full strip follows from (4).

## 3. Directed uncertainty from the smaller prefix

Suppose only \(\beta_1,\ldots,\beta_{N-1}\) have been acquired. Define
the error amplitude \(\alpha_N\) and its computable upper bound \(A_N\)
by
\[
 \alpha_N=\frac{\prod_{j=1}^{N-1}\beta_j}{(2N)!}\,\beta_N,
 \qquad
 A_N=\frac{\prod_{j=1}^{N-1}\beta_j}{(2N)!}
                   (B_{N-1}-\beta_{N-1}) .
 \tag{6}
\]
These satisfy \(0<\alpha_N\le A_N\). At \(N=1\) the empty product
is one and \(A_1=B_0/2\). The upper bound uses only the known prefix
and the adjacent envelope. The amplitude is distinct from a Jacobi
link. At a fixed \(z\ne0\) in the strip set \(w=G_N(z)/d_N(z)\) and
\(\varepsilon=\epsilon_N(|z|,Y)\). Write \(D(a,r)\) for the closed
complex disk of center \(a\) and radius \(r\). In this notation
\[
 \frac{F(z)}{d_N(z)}=w+\alpha_N E_N(z),\qquad
 U^+=\bigcup_{0<a\le A_N}D(a,a\varepsilon),\qquad
 U=\bigcup_{0\le a\le A_N}D(a,a\varepsilon).
 \tag{7}
\]
A zero requires \(-w\in U^+\). Since \(a(1+\eta)\) with
\(|\eta|\le\varepsilon\) scales the \(A_N\)-disk by \(a/A_N\),
the set \(U\) is the convex hull of \(\{0\}\cup D(A_N,A_N\varepsilon)\).
Indeed, any convex combination of points in that disk and 0 is a
single scaling of a disk point, by convexity of the disk. The domain
\([0,A_N]\times D(0,\varepsilon)\) is compact, so \(U\) is closed.
The only point it can add to \(U^+\) is 0, which is already in
\(U^+\) if \(\varepsilon\ge1\).

The larger capsule \([0,A_N]+D(0,A_N\varepsilon)\) contains \(U\)
because the offset of a point in \(D(a,a\varepsilon)\) is at most
\(a\varepsilon\le A_N\varepsilon\). This proves the sufficient test
\[
 \operatorname{dist}(-w,[0,A_N])>A_N\varepsilon .                 \tag{8}
\]
The exact membership test for \(v=-w\) in \(U\) is
\[
 \min_{0\le a\le A_N}
 \{\,|v|^2-2a\Re v+(1-\varepsilon^2)a^2\,\}\le0 .               \tag{9}
\]
It comes from squaring \(|v-a|\le a\varepsilon\) with both sides
nonnegative. When \(\varepsilon<1\), the minimizer is
\(\Re v/(1-\varepsilon^2)\) limited to \([0,A_N]\). When
\(\varepsilon\ge1\), an endpoint minimizes the concave or affine
quadratic. In that case \(U=D(A_N,A_N\varepsilon)\), because this
disk already contains zero. For (8), equality only gives membership
in the larger capsule. For (9), equality gives membership in the
closed directed set and excludes no zero by the closed-set test.

When \(\varepsilon<1\), \(\Re E_N(z)\ge1-\varepsilon>0\).
Thus \(\Re w\ge0\) gives \(\Re(F/d_N)>0\), even when \(w=0\).
This pointwise test uses positivity of the actual amplitude and no
value of its upper bound. With \(\varepsilon=1\) this argument loses
strictness. More generally, for \(v\in U^+\) and \(\varepsilon<1\)
there is \(a>0\) with \(\Re v\ge a(1-\varepsilon)>0\). If
\(\theta=\arg v\) is chosen in \((-\pi/2,\pi/2)\), the distance
from \(a\) to the line through \(v\) and 0 is \(a|\sin\theta|\),
at most \(|v-a|\le a\varepsilon\). Hence any zero must satisfy
\[
 |\arg(-G_N(z)/d_N(z))|\le\arcsin\varepsilon,
 \qquad 0< |G_N(z)/d_N(z)|\le A_N(1+\varepsilon) .               \tag{10}
\]
The angular bound is attained for the abstract disk at
\(v=a\sqrt{1-\varepsilon^2}e^{\pm i\arcsin\varepsilon}\).
The radial bound is attained at \(A_N(1+\varepsilon)\). These
attainments concern the enclosure. When \(\varepsilon=0\), the
set \(U^+\) is the positive segment \((0,A_N]\). The angular
restriction has no asserted extension to \(\varepsilon>1\).

If the exact amplitude is known, the normalized error in (7) lies in
\(D(\alpha_N,\alpha_N\varepsilon)\), a subset of \(U^+\).
The strict disk test is \(|w+\alpha_N|>\alpha_N\varepsilon\),
equivalently \(|C_N|>|L_N|\varepsilon\). Equality alone does not
exclude cancellation. Using the exact amplitude amounts to the
same coefficient input as \(G_{N+1}\) by §2. A purely geometric
advantage of the corrected model over that next head would require
its own estimate. All divisions here use \(z\ne0\). At \(z=0\),
\(F(0)=G_N(0)=1\), which directly excludes a zero.

## 4. Conditional contour count

Let \(\Gamma\) be a positively oriented piecewise \(C^1\) simple
closed contour on the strip \(|\Im z|\le Y\le1\). The two functions
are entire, so they are holomorphic on a neighborhood of the contour
and its bounded interior. Suppose that for every \(z\in\Gamma\)
with \(z\ne0\), there is strict separation
\[
 \operatorname{dist}\big(-G_N(z)/d_N(z),U(z)\big)>0             \tag{11}
\]
from the **closed** set in (7). One may certify (11) by (8) or by
strict positivity of (9). Consider \(H_t=G_N+t(F-G_N)\) for
\(0\le t\le1\). At nonzero \(z\in\Gamma\), the normalized error
\(t\alpha_NE_N(z)\) belongs to \(U(z)\), including at \(t=0\).
Therefore \(H_t\) has no boundary zero. If the contour meets zero,
\(H_t(0)=1\) for every \(t\). Compactness and continuity give a
positive minimum of \(|H_t(z)|\) on \([0,1]\times\Gamma\).
By the argument principle, the zero count in the interior,
with multiplicity, is
\((2\pi i)^{-1}\int_\Gamma H_t'(z)/H_t(z)\,dz\).
The integral is continuous in \(t\) and integer valued. Thus
\(F\) and \(G_N\) have the same count. The argument allows
\(G_N\) to have interior nonreal zeros. It assigns no numerical
value to the model count. The same integral argument gives the
usual strict boundary comparison behind Rouché's theorem.
[Contour source passage][contour]

The positive-amplitude union \(U^+\) alone would miss the initial
homotopy endpoint when \(\varepsilon<1\). In particular the pointwise
half-plane test can pass when \(G_N=0\), at which point (11) fails.
If \(\varepsilon<1\) and \(\Re w\ge0\) with \(w\ne0\), then
\(-w\notin U\), since \(U\cap\{\Re v\le0\}=\{0\}\). Applying such
a test around a whole contour still requires verifying its conditions
at every boundary point. An exact-amplitude disk count for \(F\)
and \(C_N\) follows from the strict disk test on the whole contour
with \(F-C_N=L_N(E_N-1)\). It compares a different pair of models.

## 5. Control screen and missing canonical input

The shape assumption actually used for (7)–(11) is an error factor
in the disk of center 1, multiplied by a positive amplitude. The
exact Hermite law holds for other literal even probability transforms
with sufficient moments, at degrees with the requisite positive
norms. To inherit the paid quantitative bounds one also needs the
adjacent envelope and the degree-wise polynomial-density cosh
moment in E01. For each suitable positive square mixture, the same
score confinement gives the cosh moment by the E01 integration by
parts. This applies even at the weighted-square controls' recorded
heat times. It leaves their actual contours and finite-model counts
as separate questions. [E01 §5][e01] and [E07 §§2–4][e07]

| Catalog control | Premises and scope |
| --- | --- |
| Three- and four-square sources | Their even positive densities and tails give the exact law. Their score confinement gives the same cosh moment and coefficient envelope. They fail complete canonical coefficients and full smooth reflection. Those failures are outside (7)–(11). The catalog's separate finite-source theorem gives nonreal zeros even at time zero. |
| E07 finite canonical-score controls, and the finite-prime orbit sources screened there | The specified positive bounded square weights give the same law, cosh moment and envelope. Full canonical reflection and the unchanged complete coefficients fail. E07's nonreal-zero conclusion holds for its finite-mode perturbations with no fixed zero location. The orbit result supplies separate positive-time double events at escaping heights. Neither result supplies failure of a proposed canonical fixed-contour margin. |
| Euler-factor translates | The exact law applies to their even probability transforms with the requisite moments. The tested \(c=1/2,p=23\) case fails \(B_0\) at time zero. Other primes retain E01's untested envelope status. |
| Reflected super-Gaussian | Its tails allow the law. Its own score grows only polynomially and fails the E01 exponential confinement premise. Its degree-wise cosh and coefficient bounds remain untested here. |
| Smooth shape and positive-primitive sources | Their tails and positivity allow the law. They lack the exact square-summand score. E01's weaker confinement and degree-wise bounds remain untested across the catalog's allowed small damping. E10/E12 smooth compact perturbations likewise supply no inherited nonreal-zero claim. |
| Atomic and compact finite-profile controls | Finite-rank atoms allow the law only at degrees with positive monic norms. The inherited three-atom example fails the adjacent bound at its stated event. The atoms and compact extensions lack the strictly positive full-line density used in the score proof. No blanket coefficient-bound failure follows. |
| RH-conditional normalized endpoint controls | Their even positive densities and tail comparison allow the law in their stated RH-conditional scope. Ordinary Dirichlet arithmetic and the exact square-summand score fail. The degree-wise bounds remain untested. |
| Fixed-amplitude variable observation and BW-08 relaxed masses | Unchanged theta amplitude retains its coefficients, but the changed observation fails the literal cosine/Newman identity. The fractional-mass relaxation supplies no physical positive source with the required Fourier observation. |

What remains unpaid is canonical placement of the computed \(G_N/d_N\)
relative to \(U\) on contours covering the intended growing compact
regions. An off-real contour also needs a proved zero model count to
exclude zeros inside it. If a contour includes a real interval, a
confinement argument can instead match the transferred total count
with an independently justified count of real zeros.
The actual law and its degree-only allowance alone cannot give such
a global conclusion for their shared class. If a control has a
nonreal zero in a tested region, a valid boundary comparison there
would transfer that count to its model. Therefore the paired claim
of separation and zero model count must fail on a contour enclosing
that zero. No failure of every local margin is implied. The present
work verifies no theta contour or expanding-cover premise and gives
no unconditional zero confinement.

[return]: ../research-progress/handoffs/VCD-E24-r1-return.md
[phase]: ../brainstorm/notes/12_VCD_B06_ERROR_PHASE_CONSUMER_DECISION_20261116.md
[decision]: ../brainstorm/notes/13_VCD_B06_PREFIX_COST_AND_DIRECTED_ERROR_DECISION_20261116.md
[e01]: 01_VCD_E01_LOGARITHMIC_ENVELOPE_20261113.md
[e07]: 07_VCD_E07_FINITE_CANONICAL_SCORE_CONTROLS_20261116.md
[e15]: 13_VCD_E15_SHARED_MEMORY_EQUIVALENCE_20261116.md
[contour]: ../references/02_INDUCTION_SOURCE_PASSAGES_20261116.md
[results]: ../../../../result-summaries/README.md
[cluster]: ../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md
[catalog]: ../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../avoid/README.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a02]: ../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
