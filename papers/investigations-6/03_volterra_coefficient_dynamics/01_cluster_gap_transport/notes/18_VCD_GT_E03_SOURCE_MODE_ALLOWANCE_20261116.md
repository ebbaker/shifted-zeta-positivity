# VCD-GT-E03 r4 A — Laurent source modes and the one-mode allowance

16 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance, chat0003. Helper dispatch
**gpt-6.1-sol / ultra** from the frozen request. Separate backend
attestation and the lead's actual model and effort are unavailable.

**Proved in-note under the stated local hypotheses.** The Laurent
expansion is an exact evaluation of the existing \(K\). The selected
one-mode upper allowance fails its finite quantitative test on the
already certified Lehmer tube, even with the exact signed coefficient.
The two-sign example is an analytic heat-field premise test. Internal
proof-author checking only. See [Decision06][decision], the
[frozen request][request], [result index][results], [controls12][controls],
and the [avoid index][avoid], especially [01][classification], [02][premises],
[07][scope] and [12][bounds].

## 1. Which modes carry the drift

Fix \(t\) and put \(w=z-a\). Assume \(G_t(a+w)\) is holomorphic on a
neighborhood of the closed radius-\(R\) disk. It has exactly two zeros
counted with multiplicity, their offsets \(u_1,u_2\) satisfy
\(|u_j|\le r<R\), and the radius-\(R\) circle has a zero-free collar.
Use
\[
 Q(w)=(w-u_1)(w-u_2),\qquad A(w)=G_t(a+w)/Q(w),\qquad
 K=\frac1{2\pi i}\oint_{|w|=R}\frac{A'(w)/A(w)}{Q(w)}\,dw .
\]
The quotient extends holomorphically through the pair, and \(A\) is
zero-free on a slightly larger disk by compactness and the collar.
The log \(g=\log A\) exists on this disk by integrating \(A'/A\).
On the annulus where \(r<|w|\) in the disk, the standard power series
for \(\log(1-u_j/w)\) are single-valued and converge absolutely. Their
sum with \(g\) is a log of \(G_t(a+w)/w^2\). Equivalently, the
argument principle gives zero winding for that ratio on the collar
because the zero count is two and \(w^2\) has index two.

Write \(L(t,w)\) for a holomorphic collar log of the ratio, with any
fixed real centering subtracted. Its expansion on the common annulus
satisfies
\[
 L(t,w)=g(w)+C(t)-\sum_{m\ge1}\frac{u_1^m+u_2^m}{m w^m}.
 \tag{1}
\]
A different log branch adds a spatial constant on the connected
annulus. Centering adds another constant, and the sign normalization
of Note14 also changes only a constant if used. Thus the positive
Laurent coefficients
\[
 a_n(t)=\frac1{2\pi i}\oint_{|w|=R}L(t,w)w^{-n-1}\,dw,\qquad n\ge1,
\]
are the Taylor coefficients of \(g\) at the origin. The negative
modes record the pair power sums. For a field real under conjugation,
\(A\) is real under conjugation, so \(A'/A\) is also. Its Taylor
coefficients show \(a_n\in\mathbb R\) for \(n\ge1\). Similarly all
the symmetric polynomials \(h_j\) below are real.

Expand \(1/Q\) by multiplying the two geometric series on the circle.
Termwise integration with \(g'\), by absolute uniform convergence on
that circle, gives
\[
 \frac1{Q(w)}=\sum_{j\ge0}h_j w^{-j-2},\qquad
 h_j=\sum_{\ell=0}^j u_1^\ell u_2^{j-\ell},\qquad
 \boxed{K=\sum_{n\ge2}n a_n h_{n-2}} .
 \tag{2}
\]
The term integral selects \(n=j+2\). The log branch and centering
leave every coefficient used in (2) unchanged. The expression is
symmetric in the two offsets at each time, with \(h_j=(j+1)u_1^j\)
at a double. It uses the multiplicity-counted divisor and the
external collar, so it needs neither persistent root labels nor an
inverse internal gap.

For the unchanged complete xi heat convolution \(G_t=e^{\pi a/8}H_t\),
the normalizations of [Note12 §§1, 4][note12] and the actual log
construction of [Note14 §3][note14] apply. [Note15][note15] supplies
count, collar, real symmetry and the uniform bounds on \(I=[0,1/10]\)
at \(a=140101/10\). Formula (2) uses the actual field and gives the
same drift as the full contour formula used there.

## 2. Exact failure of the selected allowance

With \(\max_{|w|=R}|L(t,w)|\le B\), the coefficient integral gives
\(|a_n|\le B/R^n\). Since \(|h_j|\le (j+1)r^j\), taking the first term
of (2) exactly yields the valid upper bound
\[
 K\le U_2=2a_2+T,\qquad
 T=\frac{B}{R^2}\sum_{n\ge3}n(n-1)(r/R)^{n-2}.
 \tag{3}
\]
The remainder bounded by \(T\) is the signed sum of all terms with
\(n\ge3\). For the frozen values \(r=3/4,\ R=21/20,\ B=1737/1000\),
\[
 q=r/R=5/7,\qquad \frac{B}{R^2}=\frac{386}{245},\qquad
 \sum_{n\ge3}n(n-1)q^{n-2}=\frac{2}{(1-q)^3}-2=\frac{335}{4}.
\]
The sum follows by differentiating the convergent geometric series
twice and removing the \(n=2\) term. Consequently
\[
 T=\frac{12931}{98},\qquad
 U_2\ge -\frac{772}{245}+\frac{12931}{98}
     =\frac{63111}{490}>0.
 \tag{4}
\]
Equivalently, success at the target \(U_2\le-59/100\) at even one
time would require \(a_2\le-649441/9800\). This conflicts with
\(a_2\ge-386/245=-15440/9800\).

This rules out passing the chosen bound (3) with these \(r,R,B\).
The lower bound in (4) applies to the formula \(U_2\) for every
Cauchy-compatible \(a_2\). The actual remainder can be far smaller
than \(T\), and the actual \(K\le-59/100\) already follows from the
accepted full kernel certificate in [Note15][note15]. If the exact
\(a_2\) were retained in a different proof of that target, the
unpaid estimate would be
\[
 \sum_{n\ge3} n a_n h_{n-2}\le -59/100-2a_2
 \quad\text{uniformly on } I.
\]
It calls for a sharper bound on the joint signed tail or a different
quantitative estimate of the same drift. The all-mode identity
contains that tail exactly and by itself gives no sign estimate.
Every acquired coefficient or field value is available to the direct
contour method on the same domain.

## 3. Opposite signs with common unsigned local bounds

In local physical time \(\tau\), set
\[
 s=1+4\kappa\tau,\quad b=\kappa/s,\quad D=2\tau s,\quad
 P=s^{-5/2}e^{bw^2},\qquad F_\kappa(\tau,w)=P(w^2-D).
\]
For \(s>0\), this is entire in \(w\), real under conjugation and
real-analytic in \(\tau\). With \(Q=w^2-D\), direct differentiation
gives
\[
 \frac{P_\tau}{P}=-10b-4b^2w^2,\qquad
 \frac{P_w}{P}=2bw,\qquad
 \frac{P_{ww}}P=2b+4b^2w^2,\qquad
 D'=2+16\kappa\tau=2+8bD .
\]
Hence \((\partial_\tau F_\kappa+\partial_w^2 F_\kappa)/P
=-8bQ-D'+8bw^2+2=0\). The deflated logarithmic derivative is
\(2bw\). Formula (2), or the contour integral of \(2bw/Q\),
gives \(K=2b=2\kappa/s\), including at the double. The pair has center
zero in \(w\) and squared half-separation \(D\).

Take \(0<|\kappa|\le1/20\), \(u=-1/20\le\tau\le v=1/20\).
Then \(99/100\le s\le101/100\), \(|D|\le101/1000\), and both
zeros are inside \(|w|<7/10\). They are counted twice at \(\tau=0\).
On the common collar \(7/10<|w|<11/10\) containing both \(r\) and
\(R\), a periodic log with real centering zero is
\[
 \mathcal L=-\tfrac52\log s+bw^2+\log(1-D/w^2).
\]
There \(|\log s|\le1/99\) by integrating \(1/s\), and
\(|D/w^2|\le101/490<1/4\). The log series then gives the same bound
for both signs of \(\kappa\),
\[
 |\mathcal L|\le \frac{5}{198}+\frac{121}{1980}+\frac13
              =\frac{277}{660}<\frac12<B.
\]
In particular \(F_\kappa/w^2=e^{\mathcal L}\) has real part at least
\(e^{-1/2}\cos(1/2)\ge7/16\) and modulus less than \(2\) on the
collar. Also \(|K|\le10/99\) for both signs, while \(\operatorname{sgn}K
=\operatorname{sgn}\kappa\). The shared count, collar and unsigned
bounds therefore allow opposite drift signs in this analytic
heat-field class.

For the cost comparison of [Note12 §5][cost], the positive weight is
\(W(\tau)=e^{4\int_\tau^vK}=[s(v)/s(\tau)]^2\). Since \(s\) is affine,
\(2\int_u^v W=2(v-u)s(v)/s(u)\), giving
\[
 D(v)-2\int_u^vW=2u\,\frac{s(v)^2}{s(u)}
               =-\frac{s(v)^2}{10s(u)}<0.
\]
Starting at the double \(\tau=0\) gives equality. This supplies the
failed strict passage premise even for \(\kappa<0\). The tube here is
in local time centered at the double. It can be shifted to
\([0,1/10]\) by \(\tau=t-1/20\) without changing the heat equation.
The example is scoped to analytic heat fields, with no positive
Fourier source or canonical arithmetic assumed. Its symmetry is about
the chosen center \(a\). At \(\tau=0\), its values at \(z=a\) and
\(z=-a\) are zero and \(4a^2 e^{4\kappa a^2}\), respectively, so the
shifted field lacks global evenness in \(z\) for \(a\ne0\).

## 4. Control premises

The contour algebra applies to any qualifying analytic field with
the counted buffered pair. The cost identity additionally needs the
physical heat equation and a persistent counted collar in time. On
any qualifying interval starting at a double, \(D(T)=0\) forces
equality in the exact incoming-cost test. Extending the interval to
start before \(T\) makes the exact cost strictly larger. The existing
controls below are screened using [controls12][controls],
[Note12 §6][screen12] and [Note14 §6][screen14].

| Control | Shared input and failed premise |
| --- | --- |
| Exact quadratic and local quartic heat fields | The quadratic shares the counted buffered collar, equation and log and has only negative powers apart from its log constant, so \(K=0\). Its strict cost fails across its double. The quartic shares local heat calculus and has the recorded double despite a favorable force sign. These polynomial fields lack the complete xi source. |
| Euler-factor translates | Positivity, reflection and, in the \(0<c<1\) family, the time-zero real zero set are shared. The extra factor changes the completed field and its Dirichlet coefficients. Its reflected comb uses noninteger nodes as well. |
| Three- and four-weighted-square sources | Positive integer-square support and their respective finite endpoint identities survive. Full source reflection with the canonical unit sequence fails. Their recorded local events do not supply an all-real threshold. |
| Reflected super-Gaussian | Full reflection, positivity and the odd primitive data survive. Its source lacks canonical integer-square support and coefficients. |
| Smooth strongly log-concave and normalized positive-primitive controls | The respective shape, primitive and endpoint data survive as recorded. The literal theta square expansion is absent. |
| Reflection rigidity and four-family comparison | In the rigidity class, unit coefficients follow from full reflection and the normalized endpoint for polynomially weighted integer-square combs. The three- and four-square examples fail full reflection, while the reflected and Euler-factor examples fail integer-square support. The full conjunction supplies no distinct control within the rigidity class. |
| Finite-source measurement audit | Finite head or measurement data can survive a finite change. The changed normalized theta tail or finite zero-tail source fails source equality. The finite-source classes in the audit lack a finite all-real anchor, which this local test does not require. |
| Finite-prime orbit controls | The fixed prime conditions, coefficient prefix, measurements and primitive normalization can survive. Full source reflection fails. The distinct high-gap constructions do not supply an event at the frozen location. |
| BW-01 fixed-event positive source | Complete moment bounds and two selected imaginary-axis floors are shared in the stated class. The three-atom source lacks unchanged theta coefficients, full profile and eventual threshold simplicity, with its event fixed at \(a=20\). |
| Exact finite-profile threshold controls | Prescribed finite probes, event height, normalization and common moment bounds can survive. The atomic and continuous compact-source versions fail unchanged theta arithmetic, full profile growth and eventual threshold simplicity as recorded. |
| BW-10 RH-conditional normalized endpoint control | The normalized completion, functional equation and pole residue survive in the conditional construction. Ordinary Dirichlet-series arithmetic changes, the result retains its RH premise, and the added doubles escape to infinity. |
| Fixed theta amplitude with varied observation kernel | The theta amplitude, raw compatibility and prescribed finite cosine prefix can survive. The kernel fails the full cosine oscillator/Newman equation, so the observed field does not instantiate the literal physical gap law here. |
| BW-08 actual-theta three-profile relaxation | Three actual observations are retained. Fractional masses do not give the complete integer zero divisor of a specified analytic heat field and do not supply a physical counted pair. |
| Canonical-score refinement | A fixed finite score list, coefficient head and envelope can survive. The nonzero finite-tail change fails unchanged canonical source, and the construction supplies no fixed zero location. |

Except for the explicit local models just analyzed, the quantitative
mode inequalities and the exact count and collar on this particular
Lehmer tube remain untested for the controls. A finite certificate can
pass a collision-free box of a changed source. The arithmetic bounds
here concern the frozen allowance and the analytic control class. The
unchanged canonical field, sharper joint estimates, and other
geometries retain their separate proof requirements.

[decision]: ../brainstorm/notes/06_VCD_GT_B06_SOURCE_MODE_AND_MATCHED_ENVELOPE_20261116.md
[request]: ../research-progress/handoffs/VCD-GT-E03-r4.md
[results]: ../../../../../result-summaries/README.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../avoid/README.md
[classification]: ../../../../../avoid/01_restating_the_target.md
[premises]: ../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[scope]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[bounds]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[note12]: 12_VCD_GT_E08_CANONICAL_XI_ORACLE_20261116.md
[note14]: 14_VCD_GT_E09_TENSOR_CERTIFICATE_BOUNDS_20261116.md#3-count-collar-and-centered-log
[note15]: 15_VCD_GT_E04_CERTIFIED_SIGNED_GAP_20261116.md
[cost]: 12_VCD_GT_E08_CANONICAL_XI_ORACLE_20261116.md#5-signed-primitive-time-cost-and-exact-control
[screen12]: 12_VCD_GT_E08_CANONICAL_XI_ORACLE_20261116.md#6-scope-and-control-screen
[screen14]: 14_VCD_GT_E09_TENSOR_CERTIFICATE_BOUNDS_20261116.md#6-control-premises-and-scope
