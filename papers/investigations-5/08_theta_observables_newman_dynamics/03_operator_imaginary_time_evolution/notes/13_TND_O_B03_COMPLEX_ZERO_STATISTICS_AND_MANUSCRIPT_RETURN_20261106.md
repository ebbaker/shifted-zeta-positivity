# Coefficients, complex-zero statistics and the positive-threshold question

6 November 2026, America/New_York. Prepared for **Edward Baker** with substantial
LLM assistance, actual **gpt-6-astra / max**, branch chat0004. TND-O-E04
manuscript integration and TND-O-B03 conceptual research return. One focused
source/analytical pass with local corrections and production checks; no
separate mathematical assessment or numerical campaign.

**Status: analytical manuscript extension complete; B03 literature and
finite-identity reconnaissance returned. No contradiction to Lambda>0 is
proved.** The requested sequence was followed: integrate previous results,
then investigate nonreal-zero statistics, then incorporate those findings.
The [manuscript](../manuscript/README.md) contains the full derivations.
[Request12](../research-progress/handoffs/12_TND_O_E04_B03_MANUSCRIPT_AND_COMPLEX_STATISTICS_20261106_REQUEST.md)
and its input manifest fix the scope;
[source receipt07](../references/07_TND_O_B03_COMPLEX_ZERO_STATISTICS_SOURCE_USE_20261106.md)
records the primary passages actually inspected.

## 1. The coefficient development

The terminology is **collision**; “double zero” describes multiplicity.
Equations (5.4) and (5.5) retain their numbers. The critical curve is
h_x(tau,x_c(tau))=0, not a zero trajectory. The manuscript separates
amplitude a=h_xx from beta=b/a and gamma=c/a-b^2/a^2. Along the curve,
A'=h_xxxx-h_xxx^2/A and (log|A|)'=gamma. For v=h and r_c=-v/A,
r_c'=-1-r_c A'/A.

With local factor H=P U, ell=U'/U and kappa=(U'/U)' at the event,
equation (5.17) gives

\[
\beta=3\ell,\qquad c/a=6(\kappa+\ell^2),\qquad
\gamma=6\kappa-3\ell^2,\qquad B_*=\kappa.
\]

The even Laguerre–Pólya benchmark is conditional on the all-real product
hypothesis. Its reflected partner implies gamma<0, but the admitted
smooth collision control has gamma<-16. That stronger sign is proved
by elementary integral bounds without quadrature or an assertion that
the control is globally in the Laguerre–Pólya class.

Section6 derives complete signed theta moments and the heat-weighted
half-line primitive identity, including the endpoint 1/2 in 8H_lambda.
It gives a contour formula for U'/U and explicit boundary-error allowances,
reusing existing finite-cluster contour work. Boundary floor, cluster
count and actual source errors remain necessary for a quantitative estimate.

Section7 adds moving-boundary identities. Local mass M satisfies M'=-2T
and T/M=-1/2(log M)'. Both M and kinetic form T vanish at the event;
only their quotient diverges. In gap coordinates,
M~a^2 delta^5/120, T~a^2 delta^3/12, and delta^2 T/M tends to10.
The endpoint term in T' is retained. Epsilon is remaining imaginary time.

Section11 distinguishes pair deflation from Rodgers–Tao renormalization:
the latter retains the inverse-square collision pole. Neither is the
Hilbert-space field energy. E01/E02's supplied-source scope and Q1/Q2
remain unchanged.

## 2. What the literature supplies without RH

Write a zeta zero rho=sigma+it. Its corresponding H_0 zero is
z=2t+i(1-2sigma). Off-line zeros are **nonreal** H_0 zeros; pure imaginary
H_lambda zeros are impossible by positivity of the cosh integral.

| Statistic | Retained information | Established scope |
| --- | --- | --- |
| Ordinate-only Montgomery sum F_v | Differences t-t' | Defined without RH; original restricted-frequency theorem assumes RH |
| Analytic complex-difference sum F_c | Complete rho-rho' with complex weight | BGST unconditional restricted-frequency asymptotic |
| Marked pair measure and planar structure factor | Longitudinal differences and both transverse coordinates | Finite definitions and positivity; no arbitrary-mark sine-kernel theorem |

Baluyot–Goldston–Suriajaya–Turnage-Butterbaugh's Theorem1 applies to F_c,
not the unchanged F_v. Proposition12.2 derives a finite Gram-integral
identity using reflection rho -> 1-conjugate(rho). The article already
proves positivity by a Cauchy-kernel integral and is credited. Positive
total sum does not make its pair terms positive or force zeros onto the
line. Rudnick–Sarnak's earlier Theorem1.1 also uses complex zero coordinates
in analytic smoothed tests; restricted Fourier support must be retained.

Goldston–Lee–Schettler–Suriajaya v4 prove that their **ordinate PCC**,
without an added RH premise, implies density one of simple critical-line
zeros. This remains conditional on PCC; it is neither RH nor a consequence
of the unconditional BGST theorem. Their horizontal-multiplicity formulation
gives the elementary mechanism in Proposition12.3: for total multiplicity
m_t at ordinate t and D=sum_t m_t(m_t-1), N_off<=D and
N_simple,critical>=N-D.

Rodgers–Tao's final contradiction does not assume full PCC. Their Section9
uses an established positive proportion of small gaps, through
Conrey–Ghosh–Goldston–Gonek–Heath-Brown, against the almost regular gaps
their all-real dynamics would force at time0 under Lambda<0.

## 3. Finite exceptions and positive Newman time

Proposition12.4 is a directly proved sensitivity statement for the two
specified sums. Suppose locally finite multisets in 0<sigma<1 have local
ordinate counts O(log(2+t)) and differ by finitely many fixed zeros, all
changed zeros satisfying eta<=sigma<=1-eta. With common normalizer
B_T=T log(T)/(2pi), uniformly on 0<=alpha<=1,

\[
|\Delta F_v|=O((T\log T)^{-1}),\qquad
|\Delta F_c|=O(T^{-\eta}/\log T).
\]

The summable inverse-square ordinate kernel controls each fixed exception;
the complex exponential costs at most T^(1-eta). This constructs no
alternative zeta function.

**The two specified leading correlation asymptotics are insensitive to
finitely many fixed zero changes on 0<=alpha<=1.** This is not a statement
about all statistics, all frequencies, or sharper remainder estimates.

Ki–Kim–Lee's Theorems1.3–1.4 imply that, at each **fixed** lambda>0, all
but finitely many H_lambda zeros are real and simple, with high positive
real gaps asymptotic to4pi/log x. Their Xi_mu(t)=8H_(4mu)(2t).
No uniform tail threshold as lambda decreases to0 is supplied.

If Lambda>0, choose0<lambda<Lambda: a finite nonreal exceptional set
coexists with that regular real tail. A sufficiently high-window marked
statistic then has no transverse marks. Positive-time regular spacing
therefore supplies no contradiction. Relating it to time0 requires
uniform control in a joint time-height limit, beyond compact convergence.

For a finite isolated simple cluster, with g=U'/U and prime denoting
increasing Newman time, Proposition12.6 gives

\[
\frac{d}{d\lambda}\sum_j y_j^2
=-4\sum_{j<k}\frac{(y_j-y_k)^2}{|z_j-z_k|^2}
 +4\sum_j y_j\Im g(z_j).
\]

For a conjugate pair, (y^2)'=-2+4y Im g(x+iy). Near a real event,
Im g(x+iy)=y g_x(x)+O(y^3), linking the correction to kappa.
The identity is local and uses no infinite principal-value sum.
For a complete polynomial cluster g=0, transverse contraction does not
prevent the reverse collision. Complex inverse-square interactions are
not positive: a conjugate pair contributes -1/(4y^2). An absolute-square
replacement requires its own evolution argument.

## 4. Controls and continuation

These are identities, literature inputs and a scoped sensitivity theorem;
no RH-equivalent certificate is validated by sampling. The exact smooth
control retains positivity, heat flow, regularity and negative curvature
but fails **the literal canonical theta arithmetic formula**. It is not
asserted to satisfy the zeta correlation or KKL tail theorems. The polynomial
model tests only the finite dynamics. These boundaries follow
[control summary12](../../../../../result-summaries/12_collision_controls_and_screening.md)
and [pattern02](../../../../../avoid/02_shape_only_arguments_and_the_controls.md).

The missing scientific step is a canonical estimate sensitive to an
exceptional cluster, including its exterior term, or an amplification
theorem carrying one exception into a statistic covered by an arithmetic
estimate. Section14 separates this from coefficient acquisition, joint
time-height/multiplicity/endpoint coverage and supporting numerics.

[Production Review03](../reviews/03_TND_O_E04_B03_ANALYTICAL_AND_PRODUCTION_CHECK_20261106.md)
is a same-author check. [Continuation14](14_TND_O_E04_B03_CONTINUATION_AND_MODEL_CHANGE_20261106.md)
recommends a bounded E05/Sol assessment before further B/Astra target choice.
No successor is automatically activated. Use the
[result index](../../../../../result-summaries/README.md),
[local geometry13](../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md),
[patterns index](../../../../../avoid/README.md) and
[scope pattern07](../../../../../avoid/07_scoped_exclusions_read_as_universal.md).
No universal statistical no-go theorem or advantage over equally informed
scalar source analysis is asserted.
