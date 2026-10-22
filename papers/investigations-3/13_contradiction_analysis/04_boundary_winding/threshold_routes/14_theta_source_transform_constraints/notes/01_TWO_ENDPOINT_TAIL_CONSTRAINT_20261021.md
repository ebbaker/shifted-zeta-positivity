# Two reflection endpoints and a coupled theta-tail observation

21 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**,
reasoning effort **max**, verified from this chat's turn metadata.
Analytic derivation and 192-bit Arb constant verification; same-assistant
self-review, without independent specialist review.

**Result.** With the first theta coefficient fixed, the primitive endpoint
and the first source-reflection endpoint give a sharp upper bound
\(M<5.891258863\,10^{-11}\) on the normalized mass in modes \(n\ge3\).
The one-endpoint relaxation permits mass
\(R>1.718056625\,10^{-4}\): the reduction factor is **greater than
2,916,280**. The constraints also give an exact coupled convex enclosure
of \((H,H_z)\), and a complete uniform jet error below
\(3.570720\,10^{-12}\) on the complex domain specified below.

This improves a **relaxation's assigned allowance**, not a measured theta
error. For the actual unchanged coefficients, direct summation gives the
smaller mass \(R_2\); the new allowance is
\(1.000000001413121\ldots\) times that direct allowance. This chosen
comparison therefore supplies **no advantage over direct arithmetic**.
Finite-prime collision controls can obey both endpoints. No physical sign,
collision exclusion, boundary degree, or global simplicity result follows.

Read with the [result index][results], [arithmetic summary][arithmetic],
[control register][controls], and [avoid index][avoid], especially
[classification][a01], [matching controls][a02], [scope][a07], and
[complete signed estimates][a12]. Under that classification this is a
quantitative bounded approximation result, not an RH-equivalent criterion.
The [self-review][review] and [constant record][record] delimit its status.

## 1. The source object, observation, and inherited baseline

The source object is the complete covariant section expression, evaluated
in the prescribed frame along \((\tau,\zeta)=(ie^{4u},0)\):
\[
 \Phi(u)=\frac{y^{1/4}}{16\pi^2}
   (y^2\mathcal D^4\vartheta-3\pi^2\vartheta)(0,iy),
 \qquad y=e^{4u},\quad \mathcal D=\partial_\zeta+2\pi i s.
 \tag{1}
\]
The observation is the physical first jet
\[
 \mathcal G(t,z)=(H,H_z)(t,z),\qquad
 H(t,z)=\int_0^\infty e^{tu^2}\Phi(u)\cos(zu)\,du.       \tag{2}
\]
This is the vector used by [BW-12's relative charge][bw12] and the regular
metric in BW-11. We estimate its absolute Euclidean error; no division by
\(H\), \(H_z\), or their possibly vanishing norm is made.

The [earlier positive-tail note][cone] already constructs a convex hull
using the single primitive endpoint. Its finite pilot supplied no
theta-specific discrimination. The change here is to retain a second
exact linear relation **in that same coefficient measure**, giving an
explicit divided-difference hull. The extension to a complex observation
domain is derived below. This differs from S06's independent jet balls
and S07's whole-profile trace norm, but it is not a new ambient curvature
identity or a claim that arbitrary weighted series are theta sections.

## 2. Covariance, zero mode, and the two lower endpoints

At the zero section, repeated covariant differentiation gives
\[
 (\mathcal D^4\vartheta)|_0
 =\vartheta''''|_0+\frac{6\pi}{y}\vartheta''|_0
       +\frac{3\pi^2}{y^2}\vartheta|_0.
\]
Consequently the final term in (1) cancels the last displayed term,
including the \(n=0\) contribution. The complete result is
\[
 \Phi=\sum_{n\ge1}\phi_n,\quad
 \phi_n(u)=(2\lambda_n^2e^{9u}-3\lambda_ne^{5u})
                     e^{-\lambda_ne^{4u}},\quad \lambda_n=\pi n^2.
 \tag{3}
\]
In particular \(\phi_n>0\) for \(u\ge0\). The source identity and its
connection conventions are inherited from [Investigation 22, §8][gman].
One cannot replace \(\mathcal D^4\) by an ordinary fourth derivative in
(1); doing so changes (3).

Set
\[
 p_n=e^{u-\lambda_ne^{4u}},\quad d_n=4\lambda_n-1,\quad
 \beta_n=d_ne^{-\lambda_n},\quad 8\phi_n=p_n''-p_n.
 \tag{4}
\]
The full primitive \(\psi=\sum_{n\ge1}p_n\) satisfies
\(\psi'(0)=-1/2\). Full theta reflection gives \(\Phi'(0)=0\).
These follow from evenness of
\(e^u\vartheta(0,ie^{4u})=e^u+2\psi(u)\), using the classical
[theta modular inversion formula][dlmf] in the repository normalization.
Differentiating (3) gives
\[
 \gamma_n:=-\phi_n'(0)
 =(8\lambda_n^3-30\lambda_n^2+15\lambda_n)e^{-\lambda_n},
 \qquad \sum\beta_n=\tfrac12,\quad\sum\gamma_n=0.       \tag{5}
\]
Thus the new endpoint is also \(\psi'''(0)=\psi'(0)=-1/2\).
For \(n\ge2\), \(\gamma_n>0\). Write
\[
 r_n=\gamma_n/\beta_n
 =2\lambda_n^2-7\lambda_n+2+\frac2{4\lambda_n-1}.        \tag{6}
\]
For \(\lambda\ge12\),
\(r'(\lambda)=4\lambda-7-8/(4\lambda-1)^2>0\).
Hence \(r_n\) is strictly increasing for \(n\ge2\), and tends to infinity.

The covariant correction and the primitive lower endpoint are different
obligations; the first cancels a zero mode, while the second leaves the
nonzero \(\beta_n/8\) boundary contribution in the physical transform.

## 3. A sharp coefficient constraint and its exact coupled image

Consider nonnegative coefficient weights \(a_n\), with \(a_1=1\), obeying
the two exact moment constraints
\[
 \sum a_n\beta_n=\tfrac12,\qquad \sum a_n\gamma_n=0.     \tag{7}
\]
The positive sums over \(n\ge2\) are finite. This is a relaxation of the
canonical coefficients \(a_n=1\), not full theta automorphy. Define its
physical field by the normally convergent mode transforms. Arbitrary
members are not assumed to have all smooth source endpoints or a
holomorphic theta-bundle realization. For the actual theta source both
endpoints in (7) are ordinary differentiated source identities.

Put
\[
 R=\tfrac12-\beta_1,\quad B=-\gamma_1,\quad
 S=B-r_2R,\quad\Delta=r_3-r_2,\quad M=S/\Delta.
 \tag{8}
\]
For theta,
\[
 S=\sum_{n\ge3}\beta_n(r_n-r_2)>0.                    \tag{9}
\]
Writing \(w_n=a_n\beta_n\), every member of (7) satisfies
\[
 \sum_{n\ge2}w_n=R,\qquad
 \sum_{n\ge3}w_n(r_n-r_2)=S,\qquad
 \boxed{\sum_{n\ge3}w_n\le M.}                       \tag{10}
\]
This is the nonnegative moment inequality with the smallest possible
gap \(\Delta\). It is sharp when \(M\le R\): take \(w_3=M\),
\(w_2=R-M\), and all higher weights zero. Our interval check verifies
\(0<M<R\). This extremizer is a noncanonical source, not a claimed
collision witness. With only the first constraint, the sharp mass cap
is \(R\), attained by putting all the tail mass at mode 3.

Let
\[
 V_n(t,z)=\frac{(H_n,H_{n,z})(t,z)}{\beta_n},\quad
 Q_n(t,z)=\frac{V_n-V_2}{r_n-r_2}\quad(n\ge3),\quad
 A(t,z)=(H_1,H_{1,z})+R V_2.                          \tag{11}
\]
The exact observation identity is
\[
 \boxed{\mathcal G_a-A
       =S\sum_{n\ge3}q_nQ_n,\qquad
       q_n=\frac{w_n(r_n-r_2)}S\ge0,\quad\sum q_n=1.} \tag{12}
\]
Conversely any such probability vector gives admissible weights by
\(w_n=S q_n/(r_n-r_2)\) and \(w_2=R-\sum_{n\ge3}w_n\ge R-M\).
Thus the closure of the possible errors is exactly
\(S\overline{\operatorname{conv}}\{Q_n:n\ge3\}\), viewing
\(\mathbb C^2\) as a real vector space. The complete tail limit is
\(Q_n\to0\), and zero must be included in that closed hull.
It need not be attained by a finite source with \(S>0\).

This preserves the common weights of the value and derivative. Replacing
the hull by a rectangle below is an explicit relaxation for a cheap
comparison, not an assertion that its two coordinates vary independently.

## 4. Complete complex-domain transform payments

Before computing constants, fix
\[
 \mathcal B=\{(t,z)\in\mathbb C^2:
 |t|\le1/2,\ |\Re z|\le30,\ |\Im z|\le1\}.            \tag{13}
\]
Use \(T=1/2,Y=1,Z=31\), so \(|z|\le Z\). More generally the following
formulas hold for \(|t|\le T, |z|\le Z, |\Im z|\le Y\), provided
\(\lambda_n\ge T/8\) and \(D_n=d_n-Y>0\).
Since \(e^{4u}-1-4u\ge8u^2\),
\[
 \frac{p_n(u)}{\beta_n}e^{Tu^2+Yu}
 \le\frac{e^{-D_nu}}{d_n},\qquad
 \int_0^\infty\frac{p_n}{\beta_n}e^{Tu^2+Yu}u^kdu
 \le\frac{k!}{d_nD_n^{k+1}}.                         \tag{14}
\]
All upper integration boundaries vanish by double-exponential decay.
For \(F=e^{tu^2}\cos(zu)\), \(F(0)=1,F'(0)=0\); two integrations
by parts, with \(p_n'(0)=-\beta_n\), give exactly
\[
 \frac{H_n}{\beta_n}=\frac18+
 \frac18\int_0^\infty\frac{p_n}{\beta_n}e^{tu^2}
 [(2t+4t^2u^2-z^2-1)\cos(zu)-4tzu\sin(zu)]du.       \tag{15}
\]
Differentiation in \(z\) gives the integrand
\[
 -2z\cos(zu)-u(6t+4t^2u^2-z^2-1)\sin(zu)
                 -4tzu^2\cos(zu).                  \tag{16}
\]
Use \(|\cos(zu)|\le e^{Yu}\) and
\(|\sin(zu)|\le |z|u e^{Yu}\). Equations (14)–(16) prove
\[
 |V_{n,0}-1/8|\le A_n:=\frac18\left[
 \frac{1+2T+Z^2}{d_nD_n}
 +\frac{8(T^2+TZ^2)}{d_nD_n^3}\right],              \tag{17}
\]
\[
 |V_{n,1}|\le C_n:=\frac18\left[
 \frac{2Z}{d_nD_n}
 +\frac{2Z(1+10T+Z^2)}{d_nD_n^3}
 +\frac{96T^2Z}{d_nD_n^5}\right].                   \tag{18}
\]
These extend the [real-domain mode estimates][cone] without borrowing a
real trigonometric bound on a complex argument. Both decrease with n.
They prove the locally uniform limit \(V_n\to(1/8,0)\), hence the limit
in (12). They also give normal convergence for every field in (7): on
each compact domain discard finitely many small modes before applying
(14), then use \(\sum w_n<\infty\). No smooth trace hypothesis on a bulk
profile is needed; the restricted arithmetic modes themselves are the data.

Let \(c_0=A_2+A_3\), \(c_1=C_2+C_3\),
\(c=(c_0^2+c_1^2)^{1/2}\). Equations (10)–(18) give the complete bounds
\[
 |(\mathcal G_a-A)_j|\le M c_j,\qquad
 \|\mathcal G_a-A\|_2\le Mc.                        \tag{19}
\]
The retained transforms \(H_1,H_2\) in A include the whole interval
\([0,\infty)\). No source or mode tail is silently discarded. There is
no numerical quadrature in this comparison. If A is later approximated
with full component errors \(\epsilon_j\), the complete allowances are
\(\epsilon_j+Mc_j\), including whatever source cutoffs, quadrature and
domain propagation that acquisition uses.

Endpoint uncertainty must also be paid. If the two sums in (7) have
errors at most \(\epsilon_\beta,\epsilon_\gamma\), with \(a_1=1\)
still exact, then relative to the same nominal A the bound is
\[
 |(\mathcal G_a-A)_j|
 \le\epsilon_\beta v_j+
 \frac{S+\epsilon_\gamma+r_2\epsilon_\beta}{\Delta}c_j,
 \quad v_0=1/8+A_2,\quad v_1=C_2.                   \tag{20}
\]
Indeed the actual mass is \(R+\delta_\beta\), the actual reflection
moment is \(B+\delta_\gamma\), and its excess moment is
\(S+\delta_\gamma-r_2\delta_\beta\). Formula (20) prevents substituting
an approximate endpoint identity as though it were exact.

## 5. Frozen comparison: a large relaxation gain, no direct gain

The comparison uses domain (13), approximant A in (11), Euclidean norm,
and the same envelopes (17)–(18). Its intended gate is a strictly smaller
complete allowance than direct use of the unchanged theta coefficients;
an improvement over the less-informed one-endpoint class is reported
separately. Constants were computed only after fixing this contract.

For actual theta let
\[
 R_2=\sum_{n\ge3}\beta_n=R-\beta_2.
\]
Its error relative to the **same** A is
\(\sum_{n\ge3}\beta_n(V_n-V_2)\), so direct arithmetic gives
\(R_2c_j\) and \(R_2c\). Moreover
\[
 M-R_2=\sum_{n\ge4}\beta_n
     \frac{r_n-r_3}{r_3-r_2}>0.                      \tag{21}
\]
Therefore the direct comparator is strictly sharper. This ordering
survives every shared nonnegative acquisition payment \(\epsilon_j\).
An optimized direct method may do better still; this comparator suffices.

The [192-bit outward record][record] gives the following shortened values;
the checker compares balls rather than these displayed decimals.

| Quantity | Value or rigorous rounded bound |
| --- | --- |
| R, one-endpoint high-mode mass cap | 0.00017180566258547875025… |
| S, excess reflection moment | 6.9108594731574641… × 10^-8 |
| M, sharp two-endpoint high-mode mass cap | 5.89125886272107398… × 10^-11 |
| R/M | 2,916,280.9950965995… |
| Direct mass R2 | 5.89125885439601201… × 10^-11 |
| M/R2 | 1.0000000014131210619… |
| One-endpoint uniform vector allowance Rc | < 1.041323 × 10^-5 |
| Two-endpoint uniform vector allowance Mc | < 3.570720 × 10^-12 |
| Direct uniform vector allowance R2c | 3.5707193836205638… × 10^-12 |
| Two-endpoint value / derivative allowances | < 3.557128 × 10^-12 / < 3.112519 × 10^-13 |

The mass bound M is sharp for the relaxation. The observation bounds
\(Mc_j,Mc\) need not be sharp: their triangle and moment payments are
deliberate upper estimates. No actual-error lower bound is asserted.
No head acquisition or zero search was performed, since (21) already
fails the proposed direct-advantage gate. This is not a timing benchmark.

The numerical cross-check also pays the uncomputed coefficient tails.
For \(m=6\) and \(q_k=((m+1)/m)^k e^{-\pi(2m+1)}<1\),
\[
 \sum_{n\ge m}\beta_n\le\frac{4\pi m^2e^{-\pi m^2}}{1-q_2},\qquad
 \sum_{n\ge m}\gamma_n\le\frac{8\pi^3m^6e^{-\pi m^2}}{1-q_6}. \tag{22}
\]
The majorant term ratios decrease with n. The complete sums in (5), (9)
and R2 are cross-checked with modes 1–5 and (22), separately from their
endpoint-subtraction formulas. These checks verify the constants and
transcription; the analytic proof supplies the infinite-domain statements.

## 6. Collision controls and the scope of the result

The bound is an approximation theorem. It is not a strict acceptance rule
that ought to reject every colliding source. At a joint zero of a source
in (7), (19) merely forces \(\|A\|\le Mc\) at that point, if the point is
in the declared domain. It cannot supply a nonzero reference margin by
itself. The [finite-prime construction][finite-prime] explicitly permits
matching a fixed coefficient prefix and any finite list of source or
primitive endpoints while producing doubles at sufficiently high heights.
Taking those tests to include (7) shows that this constraint class itself
can contain colliding sources. Their event locations need not lie in (13).

| Control family | Application of this particular estimate |
| --- | --- |
| Polynomial heat germs, atomic threshold controls, q and q(T,a) kernels | No canonical integer-square mode representation with (7); generic heat behavior alone supplies neither the moment data nor the bound. |
| Euler-factor controls | Change the original mode/Euler data. The theta values R,B and the fixed first coefficient may not be imported into their estimates. No claim that their broad positivity fails. |
| Weighted-square controls | Share the positive-mode framework and some endpoints; a1=1 and both sums in (7) must be checked for each particular example. Finite endpoint matching alone is not a discriminator. |
| Finite-prime controls with the declared tests | **Can pass the exact present premises**, including a1=1 and both endpoints, while having a double event elsewhere. They inherit the local error bound, not exclusion. Full reflection is what they fail, and this estimate does not use it beyond the two endpoints. |
| Reflected super-Gaussian, smooth-shape and positive-primitive controls | Their preserved reflection/primitive properties do not supply the canonical square-mode representation. These separate preservation lists are not combined. |
| RH-conditional close-source endpoints | Ordinary Dirichlet-series arithmetic fails; they cannot be inserted as unchanged square-mode data. Their fixed-tolerance obstruction is consistent with this absolute, bounded-domain estimate. |
| Auxiliary smooth-density and two-channel controls | Do not supply the complete physical theta-mode observation with (7); their positive realizations are not a substitute for it. |

This is analytic premise screening, using the inherited witnesses and
their recorded review status; it is not a fresh numerical replay of those
event boxes. The new checker instead verifies the relevant endpoint
algebra and explicit distinct positive members of the relaxed class.

## 7. Decision and next research step

TST-01 is specified for this coupled observation, and TST-02 is complete
on (13), with exact source restriction, covariant correction, zero mode,
lower endpoint, uncertainty payments and full tails. TST-03 has a proved
quantitative **finite-endpoint** constraint, but its required arithmetic
discriminator remains open: the finite-prime controls pass these premises.
TST-04 has an analytic failed-advantage screen for (11), (17)–(19), not
an activated theta acquisition pilot. TST-05 remains gated on a useful
new physical input.

The divided-difference hull (12) is available as a robustness or source
uncertainty tool. Stop optimizing its rectangular envelope for superiority
over the same-information direct sum: (21) prevents that outcome. This
does not exclude another observation norm, a different acquisition cost
regime, or a bound using the complete coefficient/reflection relation.

The next substantive task is to identify a load-bearing use of the **full**
source relation in a signed observation, beyond any fixed list of
endpoints. Before computation, specify its receiving BW-11–13 observable,
its common direct comparator, and which finite-prime premise it actually
uses differently. One concrete candidate is an adjoint subtraction using
the full source reflection \(u\leftrightarrow-u\), with both cusps kept
together. Its first audit should test whether it only reproduces the
existing [complete reflected-contour evaluator][shifted], or supplies a
separately bounded signed remainder. That candidate is unexecuted.
More endpoint constraints may improve a finite error
budget; by themselves they do not evade this control screen. HMC-05
remains open and HMC-06 remains gated.

[results]: ../../../../../../../result-summaries/README.md
[arithmetic]: ../../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../../avoid/README.md
[a01]: ../../../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[gman]: ../../../../../../investigations-2/active/22_theta_manifold_geometry/manuscript/theta_manifold_geometry.tex
[cone]: ../../../../../../investigations-2/active/22_theta_manifold_geometry/notes/03_theta_bundles_and_connections/10_POSITIVE_TAIL_CONE_AND_FINITE_BOX_CERTIFICATE_20261015.md
[finite-prime]: ../../../../../11_arithmetic_collision_rigidity/notes/03_FINITE_PRIME_COMPATIBLE_COLLISION_CONTROLS_CODEX_20261018.md
[bw12]: ../../12_relative_chern_hopf_charges/notes/01_BOUNDED_THETA_CHARGE_AND_DIRECT_COMPARISON_20261021.md
[review]: ../reviews/01_TWO_ENDPOINT_TAIL_SELF_REVIEW_20261021.md
[record]: ../numerics/TWO_ENDPOINT_TAIL_CHECK_192_20261021.json
[dlmf]: https://dlmf.nist.gov/20.7.E32
[shifted]: ../../../../../11_arithmetic_collision_rigidity/notes/02_updated_research_plan/07_SHIFTED_EVALUATOR_AND_COMPLETE_ERROR_BUDGET_20261018.md
