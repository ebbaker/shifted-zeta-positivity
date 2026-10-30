# Fixed-degree tail and quadratic-time limits of C04 R2

30 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6-astra**, reasoning effort **max**, Investigation05 **chat0048**, *Continue FCG-B03 research*. **FCG-B03 R4**, following [Note16][n16] and [Note21][n21]. [Progress06][progress] alone owns live status.

**Decision.** Retain C04 R2's accepted finite certificate, but stop its **fixed-radius, bounded-degree, unchanged absolute-Cauchy-tail continuation to arbitrarily large frequencies**. The exact coefficient necessarily becomes nonpositive for the complete theta source in that class. A second, independent calculation shows that the quadratic time penalty can fail on a smooth positive source with no zeros, at every degree. These are proved-in-note limitations of this particular sufficient certificate, not collisions, a rejection of regional noncollapse, or an RH result. No new theta region is evaluated or proposed for numerical testing.

This pass considered two continuation designs: shrinking onto a simple zero, and carrying the existing correlated coefficient to other frequencies with its fixed budgets. The first alone does not isolate a joint-information gain; the second has the obstruction below. The resulting fixed task is [E02 R4/Sol assessment][packet], not another pilot. [Self-assessment07][self] is by the proof author only.

## 1. Exact object and the useful comparison

Keep the full source
\[
 \Phi(u)=\sum_{n\ge1}(2\pi^2n^4e^{9u}-3\pi n^2e^{5u})
                 e^{-\pi n^2e^{4u}},\qquad
 H(T,A)=\int_0^\infty e^{Tu^2}\Phi(u)\cos(Au)\,du.
 \tag{1}
\]
Fix \(0<r<\tau\), put \(R=2r\), and vary only the real center frequency \(a>0\). Each region remains the radius-\(r\) ball about \((\tau,a)\), estimated on its containing rectangle. Write \(h_j=\partial_A^jH(\tau,a)\), \(b=h_2\). Use exactly Note16's \(P,q_{mn},g_{mn}\) and
\[
 D_0=h_1^2-2bh_0,\quad
 F_N=\sum_{1\le m+n\le N}|g_{mn}|r^{m+n},\quad
 \kappa_N=\frac{N+3}{2^N},
\]
\[
 \Gamma_N=F_N+\kappa_N M_G,\qquad
 d_N=|D_0|-2b^2r-\Gamma_N,\qquad
 c_N=\frac{d_N}{1+h_0^2+h_1^2+b^2}.
 \tag{2}
\]
These are exact quantities, not interval lower bounds. In particular, a proof that \(d_N\le0\) cannot be repaired by arithmetic precision.

The physical evolution stays
\[
 \partial_sW_c=\Delta_XW_c+c\operatorname{div}_X(vW_c),\qquad
 v=X+\frac{X}{1+|X|^2},\quad X\in\mathbb R^3,
 \tag{3}
\]
with Note16's complete radial source, literal cosine, two physical components and unit Gaussian preparation. A positive mass floor still has the accepted all-time carrier consequence, including \(6L\) and the entire spatial exterior. Nothing here changes that implication or the accepted ball at \((1/4,882607/20000)\).

At an actual simple center zero, \(h_0=0,h_1\ne0\), Note16 already proves \(d_N>0\) for sufficiently small \(r\) at fixed \(N\). But its **same information** also gives
\[
 |H_A(\tau+t,a+x)|\ge |h_1|-r|b|-e_1(r)>0
 \quad (|t|,|x|\le r)
 \tag{4}
\]
for all sufficiently small \(r\): \(e_1(r)=(r+r^2/2){\cal M}_3(2r)\to0\). Thus merely shrinking around a known simple zero demonstrates passage through an \(H\)-zero, but does not demonstrate an advantage over a direct scalar **derivative** bound. This statement is only about sufficiently small neighborhoods; it does not say that every larger joint-jet certificate reduces to one component.

The exact direct consumer of Note16's correlated strip continues to give the same separation as the coefficient. A useful comparison must identify the source information improved or acquisition cost reduced; the spatial flow supplies neither automatically. The earlier [S03 direct comparison][direct] and [complete cost comparison][cost] already establish related, carefully scoped limitations. Their stopped transport configuration is not reopened here.

## 2. The finite-degree correlated tail itself forces failure

For this fixed \(\tau,r\), the positive complete-source moments
\[
 {\cal M}_j(R)=\int_0^\infty u^j e^{(\tau+R)u^2+Ru}\Phi(u)\,du
 \quad(j=3,4)
\]
are finite and strictly positive, independent of \(a\). Set
\[
 E_0=(R^3/6+R^2){\cal M}_3(R)+(R^2/2){\cal M}_4(R),\qquad
 E_1=(R+R^2/2){\cal M}_3(R).
 \tag{5}
\]
These are \(e_0(R),e_1(R)\), not the smaller-radius component bounds. Define
\[
 Z=2|b|E_0+|h_1|E_1,\quad
 M_G=Z+R|b|E_1,\quad
 \nu(a)=\max\{|h_0|/E_0,\ |h_1|/E_1\}.
 \tag{6}
\]
All denominators are proved positive source integrals; none is a jet minimum.

**Exact rejection test.** If \(\nu(a)\le\kappa_N\), then \(d_N\le0\). Indeed
\[
 |D_0|\le h_1^2+2|b||h_0|\le \nu Z,
\]
and consequently
\[
 \boxed{d_N\le (\nu-\kappa_N)Z
       -\kappa_NR|b|E_1-2b^2r-F_N.}
 \tag{7}
\]
Every term after the first is nonpositive. If \(Z=0\), then \(b=h_1=0\), the row and all \(g_{mn}\) vanish, and \(d_N=0\) directly. Otherwise \(\nu<\kappa_N\) gives strict negativity. No estimate of the finite correlated coefficients is needed for this obstruction; keeping their cancellations cannot remove the positive Cauchy tail already present in (2).

The complete signed jets \(h_0,h_1\) tend to zero as \(a\to\infty\). The following constructive estimate proves this here and supplies a source-defined cutoff, so no asymptotic theta formula is imported. Let
\[
 f(u)=e^{\tau u^2}\Phi(u),\qquad
 V_0=\int_0^\infty|f'(u)|\,du,\qquad
 V_1=\int_0^\infty|(uf(u))'|\,du.
 \tag{8}
\]
Both are finite. To check the complete-source payment, put \(\lambda_n=\pi n^2\). Termwise differentiation gives
\[
 \Phi_n'=(30\lambda_n^2e^{9u}-15\lambda_ne^{5u}
                    -8\lambda_n^3e^{13u})e^{-\lambda_ne^{4u}}.
 \tag{9}
\]
The sum of the three positive absolute terms is an integrable majorant after multiplication by any fixed polynomial and \(e^{\tau u^2}\). Summability follows from the same double-exponential domination used for (1), now with at most \(n^6\). Thus
\[
 |f'|\le e^{\tau u^2}(2\tau u\Phi+\sum_n|\Phi_n'|),\qquad
 |(uf)'|\le f+u|f'|
\]
are integrable, and the required boundary terms vanish. Integration by parts gives exactly
\[
 h_0=-\frac1a\int_0^\infty f'\sin(au)\,du,\qquad
 h_1=-\frac1a\int_0^\infty(uf)'\cos(au)\,du.
 \tag{10}
\]
There is no \(u=0\) contribution: the first formula has \(\sin0=0\), the second has \(uf(0)=0\). Hence, with
\[
 C_{\tau,r}=\max\{V_0/E_0,V_1/E_1\},
 \qquad \nu(a)\le C_{\tau,r}/a,
 \tag{11}
\]
every \(1\le N\le N_{\max}\) fails once
\[
 \boxed{a\ge A_*:=\max\{r,C_{\tau,r}/\kappa_{N_{\max}}\}.}
 \tag{12}
\]
Here \(\kappa_N\) decreases strictly with \(N\). This is an explicit finite source-defined cutoff, not a numerically evaluated height. For the old allowed list \(\{8,16,32\}\), its smallest tail factor is exactly \(35/2^{32}\). Equation (12) applies to that list at the old fixed \(\tau,r\), but does not place its cutoff near the successful old pilot.

The conclusion is for **the actual complete theta source** and **the unchanged allowance (2), at fixed positive radius and any fixed finite degree cap**. It does not exclude growing degree, shrinking radius, a different analytic envelope, other reference functions, or other C04 coefficients. Positive source rescaling does not cause the result: \(V_i,E_i,h_i\) all scale together and \(\nu,C_{\tau,r}\) are unchanged.

When \(\nu>0\), positivity necessarily requires
\[
 \kappa_N<\nu,\qquad
 N\log2-\log(N+3)>\log(1/\nu).
 \tag{13}
\]
The latter is only a necessary degree payment. Paying it need not overcome \(F_N\), the time penalty, or a small discriminant. No theta decay rate beyond (10) or measured degree-cost advantage is claimed.

## 3. A separate obstruction unaffected by degree

Even removing \(\Gamma_N\) completely leaves the necessary condition
\[
 |D_0|>2b^2r. \tag{14}
\]
For \(b\ne0\), failure says that the quadratic reference's discriminant vanishes at a time \(t_*=-D_0/(2b^2)\) in \([-r,r]\). It says nothing by itself about an actual zero of \(H\); the reference's corresponding spatial critical point may also lie outside the rectangle.

A concrete smooth positive source separates this loss from actual collision geometry. Take
\[
 \Phi_{\rm G}(u)=e^{-\beta u^2},\quad q=\beta-\tau>2r,
 \quad y=\frac{a^2}{2q}.
\]
Its local moment domain includes the entire complex bidisk used above. At every real \(T<\beta\), its cosine transform is
\[
 H_{\rm G}(T,A)=\frac{\sqrt\pi}{2\sqrt{\beta-T}}
               \exp\{-A^2/[4(\beta-T)]\}>0.
 \tag{15}
\]
This follows either from the Gaussian integral or the integration-by-parts equation \(H_A=-A H/[2(\beta-T)]\) with its value at \(A=0\). At the center,
\[
 h_1=-\frac{a}{2q}h_0,\quad b=\frac{y-1}{2q}h_0,\quad
 D_0=\frac{2-y}{2q}h_0^2,
\]
so
\[
 |D_0|-2b^2r
 =\frac{h_0^2}{2q^2}\{q|2-y|-r(y-1)^2\}<0
 \quad\hbox{if }y\ge1+q/r.
 \tag{16}
\]
For that condition, \(y>2\) and
\(r(y-1)^2\ge q(y-1)>q(y-2)\), proving strictness even at the stated endpoint. Thus **every degree fails**, even with a hypothetical zero remainder, on these Gaussian balls. This is a counterexample to adequacy of the quadratic time allowance for all positive smooth noncolliding sources. It is not a theta example or a proof that (14) fails eventually for theta.

The same exact Gaussian information gives the direct positive transform (15) and
\[
 H_A^2-HH_{AA}=H^2/[2(\beta-T)]>0. \tag{17}
\]
Thus C01's source curvature is positive there even when C04 R2 fails. The usual eventual spatial C01 transfer would use its accepted compact-uniform derivative limit and the Gaussian's finite moments; this observation neither changes the physical theta source nor transfers a Gaussian constant to theta. The same-information comparison is already decisive at the source level (17).

## 4. What a replacement estimate would have to improve

This is an interface for later B work, not a new theta sign claim. If explicit complete-source bounds \(U_3(a;R),U_4(a;R)\) on the **signed complex derivatives** throughout the same bidisk are proved, Note16's Taylor argument permits replacing \({\cal M}_3,{\cal M}_4\) by them. Form \(\widetilde E_0,\widetilde E_1,\widetilde M_G\) by (5)–(6), leaving the exact finite \(g_{mn}\) unchanged. The new sufficient estimate would be
\[
 \kappa_N\widetilde M_G
 < |D_0|-2b^2r-F_N. \tag{18}
\]
When the right side is positive, its ratio to the new paid tail is a defined comparison. It is not assumed positive. A frequency-sensitive bound could remove the specific domination in (7); upper derivative bounds alone still do not supply a positive discriminant or fix (14). Merely naming the unknown supremum is not an acquired estimate. No such new complete-theta envelope is established here. Using one would define a new allowance and coefficient revision, not retroactively alter the accepted C04 R2 definition.

This identifies why increasing precision or retaining more low-order cancellations alone is inadequate under a fixed cap. A later B03 pass can discover an oscillatory source envelope, alter the reference's time dependence, or choose another mechanism; neither a completed envelope nor a positive sign is required as its intake. Any resulting fixed numerical comparison must be issued separately with one region, identical direct/C01 information and a finite stop rule. No extra pilot is justified by the present proofs.

## 5. Collision controls, scope and disposition

The [control register][controls] and Note16's source-specific screen are retained. The following are analytic checks; no isolating certificate was rerun.

| Control class | Shared information and failed premise |
| --- | --- |
| Gaussian-polynomial and three-/four-square actual collisions | Heat equation and local moments are shared. At each source's event in its own ball, Note16's exact row identity forces \(d_N\le0\). These fail the positive-margin premise and the full unit-coefficient theta source; their events are not placed in any new theta region. |
| Euler-factor controls | Their own complete source and moments may be used. A genuine included collision defeats the margin; a negative-Laguerre witness alone does not establish \(d_N\le0\) there. They change theta's arithmetic coefficients. |
| Reflected, smooth-shape and positive-primitive controls | Shape/endpoint/reflection facts do not pay the signed derivative envelope in (18). Their complete theta square expansion fails; on moment-admissible actual event balls the existing collision obstruction applies. |
| Finite-source, finite-prime and exact finite-profile controls | Their preserved measurements do not identify the full theta jets or remainder. Full coefficients/reflection or profile growth fail as specified in the register. Atomic sources need not satisfy (8)–(10); the high-frequency theorem is not assigned to them. Their own included collisions still defeat any valid margin. |
| RH-conditional endpoint and variable-observation controls | Keep the original conditional and endpoint scopes. Ordinary theta arithmetic fails for the former; the literal cosine/heat premise fails for the latter. No event location or derivative reconstruction is silently transferred. |
| Actual-theta three-profile relaxation | It is not itself a physical collision; no rejection of a physical ball is inferred from it. |
| Pure Gaussian (15), a noncolliding adequacy check | It has positive smooth source, heat evolution and all required local moments; it fails the theta arithmetic source and theta tail profile. Its failure of this sufficient coefficient is (16), while its true transform and C01 curvature remain positive. |

No positive source-margin statement has been proposed for all these classes. The new theta rejection theorem uses decay of its genuine signed Fourier jets; it is not a theorem that high-frequency collisions exist. The Gaussian calculation shows why rejection cannot be read that way.

**Bounded return:** two exact failure mechanisms and the simple-zero comparison are derived, with a constructive complete-source cutoff for the first. C04 R2's finite accepted result remains valid. Its unchanged fixed-radius, finite-degree-cap continuation is stopped; C04's broader source-coefficient target remains open. C01 remains the sole candidate comparator, without a new theta curvature inequality. No source quadrature, root search, scan, numerical code, new region certificate, manuscript, result-summary or milestone promotion is made.

The [continuation/model note][next] and [fixed E02 R4 packet][packet] give the next assessment. This is same-assistant derivation and self-checking, with no delegation, independent implementation, specialist or formal review. Follow the [result index][results], [avoid index][avoid], [classification][a01], [scope][a07], [separate-bound warning][a12] and [noncircular-constant rule][a14].

[n16]: 16_QUADRATIC_HEAT_BEZOUT_COEFFICIENT_B03_R3_20261030.md
[n21]: 21_CONTINUATION_AFTER_FCG_E02_R3_AND_MODEL_HANDOFF_20261030.md
[progress]: ../../research-progress/06_FIXED_COEFFICIENT_PARAMETER_GEOMETRY_RESEARCH_PROGRESS_20261030.md
[self]: ../../reviews/fixed_coefficient_parameter_geometry/07_FIXED_DEGREE_AND_TIME_LIMITS_B03_R4_SELF_ASSESSMENT_20261030.md
[packet]: ../../research-progress/handoffs/fixed_coefficient_parameter_geometry/FCG-E02_R4_COEFFICIENT_LIMITS_ASSESSMENT_20261030.md
[next]: 23_CONTINUATION_AFTER_B03_R4_AND_MODEL_HANDOFF_20261030.md
[direct]: ../../../../investigations-3/11_arithmetic_collision_rigidity/symmetries/03_normalized_jet_rotation/notes/01_SIGNED_TRANSPORT_AND_DIRECT_JET_COMPARISON_20261018.md
[cost]: ../../../../investigations-3/11_arithmetic_collision_rigidity/symmetries/03_normalized_jet_rotation/notes/12_MATCHED_COMPLETE_CONSUMER_AND_COST_COMPARISON_20261019.md
[results]: ../../../../../result-summaries/README.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../avoid/README.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[a14]: ../../../../../avoid/14_convenience_hypotheses_and_circular_definitions.md
