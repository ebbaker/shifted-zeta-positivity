# A quadratic heat-polynomial coefficient using the complete first jet

30 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6-astra**, reasoning effort **max**, Investigation05 **chat0046**, *Continue FCG-B03 R2 on C04*. This is the **FCG-B03 R3** conceptual return in the existing chat, following [Note15][intake] and the accepted [E02 R2 assessment][assessment]. [Progress06][progress] alone owns live status.

**Disposition.** Retain C04 and register **C04 R2**, a new coefficient formula within the same regional-noncollapse target. One mechanism was developed: a quadratic heat polynomial and its Bézout identity, with a remainder estimated after forming correlated complete-source Taylor coefficients. C01 is the sole comparator. The conditional regional energy theorem and the simple-zero/collision distinction are derived below. Positivity for the complete theta source on the fixed ball is **unproved and unevaluated**. A [bounded E01 R1/Sol packet][packet] fixes that test. No numerical acquisition or model dispatch occurs here.

This is a finite, sufficient source certificate, not an RH-equivalent definition, a new global exclusion, or an advantage over a direct first-jet consumer with the same information. The polynomial identity is generic caloric algebra; any theta distinction must enter through the actual signed theta jets and a paid remainder. This classification follows [avoid01][a01]. Earlier accepted results retain their exact scopes.

## 1. Fixed ball, source and physical evolution

Fix, before testing,
\[
 \tau=\frac14,\qquad a=\frac{882607}{20000}=44.13035,\qquad r=\frac1{64},
 \qquad
 B=\{(T,A):(T-\tau)^2+(A-a)^2\le r^2\}.
 \tag{1}
\]
Put \(t=T-\tau,\ x=A-a,\ T_+=17/64\). The containing rectangle
\(|t|,|x|\le r\) will pay every estimate on \(B\). The inherited three-positive-square control has its event at \(T=1/4\) and frequency in \((44.1303,44.1304)\), hence inside this ball. That control location, not a theta jet value or a nonvanishing assumption, selects (1). No theta zero or theta nonzero jet in this ball is asserted.

Keep the complete source and literal cosine
\[
 \Phi(u)=\sum_{n=1}^{\infty}
 (2\pi^2n^4e^{9u}-3\pi n^2e^{5u})e^{-\pi n^2e^{4u}}>0,\qquad
 H(T,A)=\int_0^\infty e^{Tu^2}\Phi(u)\cos(Au)\,du.
 \tag{2}
\]
Every finite polynomial moment with finite extra factors \(e^{Tu^2+Yu}\) is integrable. Thus \(H\) is entire jointly in its two parameters, derivatives can be taken under the complete source, and \(H_T=-H_{AA}\).

The physical vector field remains \(W_c=(U,U_A)\) on the full \(\mathbb R^3\), with
\[
 \partial_s W_c=\Delta_XW_c+c\,\operatorname{div}_X(vW_c),\qquad
 v(X)=X+\frac{X}{1+|X|^2}.
 \tag{3}
\]
Write \(u=\tfrac12\log|X|\),
\[
 \rho_T(X)=\mathbf1_{\{|X|\ge1\}}\frac{e^{Tu^2}\Phi(u)}{8\pi|X|^3},
 \quad
 W_c(0;p)=K_1*[\rho_T(\cos(Au),-u\sin(Au))],
 \quad K_1(X)=(4\pi)^{-3/2}e^{-|X|^2/4}.
 \tag{4}
\]
The same \(c\) is used for all \(p\in B\) and all \(s\ge0\); \(\int W_c=(H,H_A)=J\). Neither source combinations nor parameter averages replace the physical family.

## 2. Quadratic heat polynomial and an exact first-jet identity

Define real complete signed source jets at the single center:
\[
 h_j=\partial_A^jH(\tau,a)
 =\int_0^\infty u^j e^{\tau u^2}\Phi(u)
       \cos(au+j\pi/2)\,du,\qquad b=h_2.
 \tag{5}
\]
Let
\[
 P(t,x)=h_0+h_1x+b(x^2/2-t),\qquad P_A=h_1+bx,
 \quad P_T=-P_{AA},
 \tag{6}
\]
\[
 D_0=h_1^2-2bh_0,\qquad D(t)=D_0+2b^2t.
 \tag{7}
\]
A direct expansion gives the Bézout identity
\[
 P_A^2-2bP=D(t).
 \tag{8}
\]
Here “Bézout” means the displayed polynomial combination; no resultant criterion or outside nonvanishing theorem is assumed.

For \(R_0=H-P,\ R_1=H_A-P_A\), define the single scalar remainder
\[
 G(t,x)=-2bR_0+(h_1+bx)R_1,\qquad
 w(t,x)=(-2b,h_1+bx).
 \tag{9}
\]
Then, exactly,
\[
 w\cdot J=D(t)+G(t,x).
 \tag{10}
\]
Both physical jet components enter this identity. In particular \(D_0=h_1^2\) at a simple center zero \(h_0=0,h_1\ne0\). There is no division by \(H\), \(H_A\), or an unknown jet minimum.

## 3. An explicit complete-source remainder

### 3.1 Complex bounds used only for the remainder tail

Set \(R=2r=1/32\), and define the finite positive source integrals
\[
 {\cal M}_j(R)=\int_0^\infty u^j
     e^{(\tau+R)u^2+Ru}\Phi(u)\,du,\qquad j=3,4.
 \tag{11}
\]
For a radius \(z\le R\), write
\[
 e_0(z)=(z^3/6+z^2){\cal M}_3(R)+\tfrac12z^2{\cal M}_4(R),
 \qquad
 e_1(z)=(z+z^2/2){\cal M}_3(R).
 \tag{12}
\]
On the complex polydisk \(|t|,|x|\le R\),
\[
 |R_0|\le e_0(R),\qquad |R_1|\le e_1(R),\qquad
 |G|\le M_G:=2|b|e_0(R)+(|h_1|+R|b|)e_1(R).
 \tag{13}
\]
To verify the first bound, Taylor-expand in \(x\) through degree two at \(t=0\), expand in \(t\) through degree one at that \(x\), and use
\(H_T=-H_{AA}\). The three residual contributions are at most
\(R^3{\cal M}_3/6,\ R^2{\cal M}_3,\ R^2{\cal M}_4/2\).
For \(R_1\), first-order \(x\) expansion and the time increment give
\(R^2{\cal M}_3/2+R{\cal M}_3\). Complex straight-line Taylor integrals are valid because (2) is entire, and (11) bounds their absolute derivatives. The same argument gives (12) on any smaller polydisk without changing its paid moments.

### 3.2 Form signed coefficients before taking absolute values

For \(m,n\ge0\), let
\[
 f_{mn}=\frac{(-1)^m h_{2m+n}}{m!\,n!},\qquad
 q_{mn}=f_{mn}-p_{mn},
 \tag{14}
\]
where the only nonzero coefficients of \(P\) are
\[
 p_{00}=h_0,\quad p_{01}=h_1,\quad p_{02}=b/2,\quad p_{10}=-b.
 \tag{15}
\]
The complete Taylor coefficients of \(G\) are
\[
 g_{mn}=b(n-2)q_{mn}+h_1(n+1)q_{m,n+1}.
 \tag{16}
\]
Indeed multiplication of \(\partial_xR_0\) by \(x\) contributes
\(nq_{mn}\), including zero when \(n=0\). For orientation,
\[
 \begin{split}
 &g_{00}=g_{01}=0,\qquad g_{10}=-h_1h_3,\qquad
 g_{02}=h_1h_3/2,\\
 &g_{11}=bh_3-h_1h_4,\qquad
 g_{20}=-bh_4+h_1h_5/2,\qquad
 g_{03}=(bh_3+h_1h_4)/6 .
 \end{split}
 \tag{17}
\]
These products and cancellations are formed from the full signed \(h_j\). Replacing every \(h_j\) by a positive moment before (16) is a different, weaker allowance.

For a fixed integer \(N\ge1\), define
\[
 \Gamma_N=
 \sum_{1\le m+n\le N}|g_{mn}|r^{m+n}
       +M_G\frac{N+3}{2^N}.
 \tag{18}
\]
This is a finite, source-defined number: it needs only \(h_0,\ldots,h_{2N+1}\) and (11). Cauchy's coefficient bound on the radius-\(R\) bidisk gives
\(|g_{mn}|\le M_GR^{-m-n}\). There are \(k+1\) pairs of total degree \(k\), so
\[
 \sum_{k=N+1}^\infty(k+1)(r/R)^k=\frac{N+3}{2^N}.
 \tag{19}
\]
Consequently \(|G(t,x)|\le\Gamma_N\) on the entire real rectangle, hence on \(B\). This pays every Taylor degree and every parameter point. No spatial or source tail has been discarded.

The issue is not whether a truncation is exact. The finite signed coefficients and the positive analytic tail together bound the exact remainder.

## 4. Coefficient, positivity implication and all-time propagation

Define, before any sign is known,
\[
 d_{B,N}=|D_0|-2b^2r-\Gamma_N,\qquad
 {\cal N}=1+h_0^2+h_1^2+b^2,\qquad
 c_{B,N}=\frac{d_{B,N}}{{\cal N}}.
 \tag{20}
\]
All quantities are real and finite. In particular \(c_{B,N}\) is allowed to be zero or negative.

**Conditional theorem.** If \(d_{B,N}>0\), put
\[
 K_B=\sqrt{4b^2+(|h_1|+r|b|)^2},\qquad
 \mu_B=d_{B,N}/K_B.
 \tag{21}
\]
Then \(K_B>0\), and
\[
 |J(T,A)|\ge\mu_B>0\qquad ((T,A)\in B).
 \tag{22}
\]
To prove it, (10) gives \(|w\cdot J|\ge|D_0|-2b^2r-\Gamma_N=d_{B,N}\), while \(|w|\le K_B\). If \(K_B=0\), then \(b=h_1=0\), \(D_0=0\), and \(d_{B,N}\le0\), contradicting the premise.

The accepted scalar-carrier argument in [Note12, Section 4][r2] now applies with \(c=c_{B,N}\) and \(m=\mu_B\). Explicitly set
\[
 L=\int_0^\infty e^{T_+u^2}\Phi(u)(1+u)\,du,\qquad
 R_2=\int_0^\infty e^{T_+u^2+4u}\Phi(u)(1+u)\,du,
 \tag{23}
\]
\[
 \overline N=\max\{R_2+6L,\,3L/c_{B,N}\}.
 \tag{24}
\]
The common positive scalar carrier dominates \(|W_c|\), has mass \(L\), initial second moment \(R_2+6L\), and satisfies
\(N'(s)\le6L-2cN(s)\). For the spatial radius
\(R_X^2=2\overline N/\mu_B\), its full exterior mass is at most \(\mu_B/2\). Mass conservation and Cauchy–Schwarz on the interior ball yield
\[
 E_{c_{B,N}}(s;p)=\|W_{c_{B,N}}(s;p)\|_2^2
 \ge
 \delta_{B,N}:=\frac{3\mu_B^2}{16\pi}
      \left(\frac{\mu_B}{2\overline N}\right)^{3/2}>0
 \quad(p\in B,\ s\ge0).
 \tag{25}
\]
Thus \(S_B=0\). The spatial flow uses precisely the original drift and unit preparation. This implication needs no stationary convergence. Any positive fixed spatial coefficient could propagate the same proved mass floor; the flow does not manufacture the sign in (20).

## 5. Simple zeros, collisions and the actual controls

**Simple-zero capability.** For any positive cosine source with the required local moment domain and a simple center zero \(h_0=0,h_1\ne0\), and fixed finite \(N\), apply the same formulas on radius \(r\) with \(R=2r\). As \(r\downarrow0\), \(D_0=h_1^2>0\), the finite sum in (18) tends to zero, and \(M_G=O(r)\); hence \(\Gamma_N\to0\) and \(d_{B,N}>0\) for all sufficiently small \(r\). This proves that the mechanism is not automatically defeated by simple zeros. It neither assumes nor proves that the theta center of (1) is a simple zero, and it does not license shrinking the frozen diagnostic ball.

**Collision obstruction.** If \(J(p_*)=0\) anywhere in \(B\), (10) gives \(D(t_*)=-G(p_*)\). Therefore
\[
 |D_0|\le2b^2r+\Gamma_N,\qquad d_{B,N}\le0.
 \tag{26}
\]
This works for every multiplicity and boundary location in \(B\). It is an obstruction to this coefficient's positivity, not a separate proof of theta positivity.

**Sufficiency only.** A nonzero jet can have \(D_0=0\), for example a nonzero constant caloric function. The bound also pays an entire time interval and containing rectangle. Failure of (20) does not imply a collision or reject the general C04 target.

The [control register][controls] and [avoid02][a02] require source-specific allowances:

| Control | Shared premises and actual failed premise |
| --- | --- |
| Positive Gaussian-polynomial collision | Its own cosine transform solves the heat equation and has all needed local moments. At its event center \((1/4,2\sqrt6)\), \(h_0=h_1=0,\ b\ne0\). On the radius-\(1/64\) ball centered there, \(D_0=0\) and \(d_{B,N}<0\). It fails the positive source-margin premise. It does not have the complete unit-coefficient theta source. |
| Three-positive-square weighted source | Its certified event lies in (1). Applying (14)–(18) to that actual source, (26) forces \(d_{B,N}\le0\). Positivity of its source and the common heat/flow equations are shared; the theta arithmetic source and the proposed positive margin are not. This uses the inherited event, without replaying its isolating certificate. |
| Four-square weighted control | Its event at \(T=1/100,\ A\approx83.5324\) is outside (1). On an event-containing ball with its own moments, (26) forces nonpositivity despite its additional reflection and primitive endpoints. It fails the full unit-coefficient theta source. No failure on the present theta ball is inferred. |
| Euler-factor controls | They share positivity, an even cosine source, heat evolution and complete local moments, but change theta's arithmetic coefficients. On a ball containing an actual collision, (26) applies to their own source. Their certified negative-Laguerre witnesses do not, by themselves, imply a collision or a nonpositive \(d_{B,N}\) at the witness point; no such claim is made. |
| Reflected super-Gaussian and smooth/positive-primitive controls | Full reflection, Fourier–Gram positivity, strong shape constraints or primitive normalization can be shared while the complete theta square expansion fails. At their own admitted collisions, their full local moment budgets and (26) reject positivity. The additional shape/endpoint information alone does not prove (20). |
| Finite-source measurement and finite-prime-orbit controls | Finite measurements, coefficient prefixes or selected prime identities do not fix the complete jets and remainder in (18). Their altered full source/reflection data fail the theta premise; their own event-containing balls obey (26). High-gap existence does not place an event in (1). |
| BW-01 fixed-event and exact finite-profile controls | Finite positive measures and their stated continuous extensions have the needed local moments; their exact collisions force (26) on their own event balls. The complete theta source, full profile growth and eventual simplicity are not transferred to them. |
| RH-conditional normalized endpoint controls | Their time-zero doubles and preservation lists have their original conditional scope; ordinary Dirichlet-series arithmetic fails. Such an endpoint is outside (1). If the formula is applied on a moment-admissible ball containing their actual zero-time event, (26) again rejects positivity. |
| Observation-family polynomial controls | Their variable observation rule is not the fixed literal-cosine source in (2); the present derivative reconstruction and caloric certificate cannot be transferred on that premise alone. Any separately caloric realization must instead use its own full source and then obey (26). |

No theta tail constants are assigned to an altered source. An unverified moment domain remains inapplicable rather than numerically passed. The actual-three-profile positive-measure relaxation in the register is not itself a physical heat collision; no event is inferred from it. These are analytic screens, not newly executed control certificates.

## 6. Why independent absolute moments are not the selected estimate

The same paid information gives a simpler valid bound
\[
 \Gamma_{\rm sep}=2|b|e_0(r)+(|h_1|+r|b|)e_1(r).
 \tag{27}
\]
It throws away the cancellations in (16). Its limitation can be proved without evaluating theta. Hold \(\tau,r>0\) fixed, move only the real center \(a\), and keep the same definitions of the positive moments. The Riemann–Lebesgue lemma, applicable to the integrable complete source and its polynomial multiples, gives \(h_j\to0\) as \(a\to+\infty\). Eventually \(|h_0|\le e_0(r)\) and \(|h_1|\le e_1(r)\), so
\[
 |D_0|\le h_1^2+2|b||h_0|
       \le |h_1|e_1(r)+2|b|e_0(r)
       \le\Gamma_{\rm sep}.
 \tag{28}
\]
The coefficient with \(\Gamma_{\rm sep}\) is then nonpositive. This is a scoped obstruction to this fixed-radius independent absolute-moment allowance, not to (18), all correlated bounds, or every possible coefficient. Equation (28) is the bounded analytical falsification supporting the choice of (18). No high-frequency scan was run.

The selected bound also has limitations: absolute values of the already formed \(g_{mn}\) lose cancellations between monomials, and a fixed finite \(N\) still pays a positive Cauchy tail. It is not claimed to remain successful at arbitrarily large frequencies.

## 7. Same-information direct comparison and C01

At a parameter \(p\), a direct first-jet consumer given the same scalar constraint
\[
 |w\cdot(J-(P,P_A))|\le\Gamma_N
 \tag{29}
\]
can compute the distance from the origin to that strip. For \(w\ne0\) it is
\[
 \frac{(|D(t)|-\Gamma_N)_+}{|w|}.
 \tag{30}
\]
The uniform floor (21) is a conservative lower bound for (30) over the rectangle. Thus the C04 construction gives **no separation advantage over the exact direct consumer of the same correlated source information**. It provides a concrete way to acquire that information and transfer it to a common spatial coefficient.

For comparison, the independent component allowances
\(|R_0|\le e_0(r), |R_1|\le e_1(r)\) give the exact direct rectangle distance
\[
 \sqrt{(|P|-e_0(r))_+^2+(|P_A|-e_1(r))_+^2}.
 \tag{31}
\]
The row estimate using \(2|b|e_0(r)+|P_A|e_1(r)\) cannot exceed (31): every point in that rectangle satisfies the row constraint, so the strip is a larger feasible set. Any improvement from (18) over (27) is additional correlated source information, not a gain from the flow or a change of coordinates.

This respects the earlier [normalized-jet transport/direct comparison][direct] and its [complete-source cost comparison][cost]. Those sources already showed the importance of matching residual information, and recorded a paid first-jet box in a different regime. They neither evaluate (20) on (1) nor establish novelty of the present algebra. Their stopped transport configuration is not reopened.

For **C01**, the same input moments give
\[
 |H_{AA}(p)|\le B_2:=|b|+r({\cal M}_3(R)+{\cal M}_4(R)).
 \tag{32}
\]
Split the increment of \(H_{AA}\) into an \(A\) increment and a \(T\) increment, and use \(H_{TAA}=-H_{AAAA}\). If \(d_{B,N}>0\), then, for
\[
 E_J=H^2+H_A^2,\quad {\cal L}=H_A^2-HH_{AA},
 \qquad C=1+B_2/\mu_B,
 \tag{33}
\]
\[
 {\cal L}+CE_J\ge E_J\ge\mu_B^2.
 \tag{34}
\]
Indeed \({\cal L}\ge-B_2|J|\ge-(B_2/\mu_B)E_J\). With spatial \(c=1\), the accepted compact-uniform limits of \(U,U_A,U_{AA}\) give
\[
 D_1(s;p)+C E_1(s;p)\ \longrightarrow\
 Q(1)({\cal L}+CE_J)
 \tag{35}
\]
uniformly on \(B\), where \(Q(1)=\|p_1\|_2^2>0\).
Hence C01 is uniformly positive for all sufficiently large \(s\), for example above \(Q(1)\mu_B^2/2\). Unlike (25), this comparison imports stationary derivative convergence and gives no explicit start time here. Its theta information is exactly the same mass certificate and paid derivatives; no independent signed-curvature lemma has been obtained. C01 remains the comparator, not a second proposed mechanism.

## 8. Exact open theta statement and the bounded execution decision

The missing statement, with no implicit minimization or nonvanishing premise, is:
\[
 \boxed{\text{For the complete source (2), ball (1), and at least one }
 N\in\{8,16,32\},\
 |h_1^2-2h_2h_0|>2h_2^2/64+\Gamma_N.}
 \tag{36}
\]
This is a finite diagnostic question, not a theorem claimed here. The real source integrals and complex-polydisk remainder are explicit. There is now a tractable execution contract, so [the model workflow][workflow] routes acquisition to **FCG-E01 R1 / Sol** rather than implementing it during this Astra B turn.

The frozen packet fixes one center, one ball, degrees \(8,16,32\), source modes \(1,\ldots,8\) on \(0\le u\le1\), complete complementary tails from Appendix A, and two arithmetic precisions. Evaluate only enough center jets for the current degree. Stop after the first rigorously positive margin with confirmation, or after the last fixed degree/precision returns a rigorous nonpositive margin or unresolved enclosure. There is no center search, radius reduction, enlargement, contour optimization, or additional observable.

A positive return would certify this finite C04 instance and its direct first-jet consequence; it would not by itself show that the ball contains a theta simple zero. A nonpositive return would reject only this frozen sufficient allowance. A broad theta-specific source inequality and any coverage beyond this ball remain unresolved.

## Appendix A. Full mode and source tails for the fixed real-integral test

This appendix fixes a simple executable tail route; no integrals are evaluated in this note. Let \(\lambda_n=\pi n^2\). Each source term is positive and at most
\[
 2\lambda_n^2 e^{9u-\lambda_ne^{4u}},\qquad u\ge0.
 \tag{A1}
\]
For a moment factor \(u^j e^{Tu^2+Yu}\), use \(e^{4u}\ge1+4u+8u^2\). With \(m=M+1\), define
\[
 \beta_m=4\pi m^2-9-Y,\qquad
 q_m=\left(\frac{m+1}{m}\right)^4 e^{-\pi(2m+1)}.
 \tag{A2}
\]
If \(\beta_m>0,\ q_m<1,\ T\le8\pi m^2\), the omitted modes \(n\ge m\), on the entire half-line, contribute in absolute value at most
\[
 {\cal T}^{\rm mode}_j(T,Y;M)
 =\frac{2\pi^2m^4e^{-\pi m^2}}{1-q_m}
          \frac{j!}{\beta_m^{j+1}}.
 \tag{A3}
\]
The mode ratios \( ((n+1)/n)^4e^{-\pi(2n+1)}\) decrease with \(n\), so the geometric bound is valid. Real trigonometric factors have modulus at most one.

For each retained mode \(n\le M\), the tail from \(u\ge U>0\) is at most
\[
 {\cal T}^{\rm src}_{j,n}(T,Y;U)=
 \frac{2\lambda_n^2 U^j
  e^{TU^2+(9+Y)U-\lambda_ne^{4U}}}
 {4\lambda_ne^{4U}-(9+Y)-2TU-j/U},
 \tag{A4}
\]
provided the denominator is positive and \(16\lambda_ne^{4U}>2T\).
The logarithm of the integrand majorant has negative derivative at \(U\) and negative second derivative for \(u\ge U\); its tangent integrates to (A4).

Therefore the exact finite-mode integral on \([0,U]\), its outward quadrature error, (A3), and \(\sum_{n=1}^M\)(A4) enclose the complete source quantity. There is no overlap between the omitted-mode part and the retained-mode source exterior.

For the issued test, \(M=8,\ U=1,\ 0\le j\le65\), and the required pairs are
\[
 (T,Y)=(1/4,0)\quad\text{for }h_j;\qquad
 (9/32,1/32)\quad\text{for }{\cal M}_3,{\cal M}_4.
 \tag{A5}
\]
If a positive margin is certified, (23) additionally uses \(j=0,1\) at
\((T,Y)=(17/64,0),(17/64,4)\).
All inequalities in (A2)–(A4) must be checked with outward arithmetic in execution. The inequalities are comfortably admissible algebraically, but an implementation must not bypass its interval guards.

The existing [real/shifted source evaluator][evaluator] supplies a local implementation precedent. Its finite midpoint jets deliberately omit tails until its own consumer, and its hard-coded domain/mode rules differ. Do **not** import those midpoint values as the complete \(h_j\) in (14); append (A3)–(A4) to every jet first. This packet uses the real-source route, not an unreviewed contour shift.

## Provenance and continuation

This is same-assistant reasoning, with [a self-assessment][selfreview], and no independent/formal review. Equations (8), (16), (19), (25) and (26) were checked by explicit derivation; no numerical checker or theta evaluator was run. The accepted R2 carrier theorem is reused with its provenance intact. The actual controls were screened analytically; existing control certificates were not rerun.

The [continuation and model-change note][continuation] records the fixed Sol task, exact stop boundary, actual chat identity and later assessment route. No manuscript, result-summary or milestone entry is promoted. Follow the [result index][results], [avoid index][avoid], [separate-bound warning][a12], [scoped-negative rule][a07] and [noncircular-coefficient rule][a14].

[intake]: 15_CONTINUATION_FCG_B03_R3_AND_MODEL_HANDOFF_20261030.md
[assessment]: ../../reviews/fixed_coefficient_parameter_geometry/03_FCG_E02_R2_REGIONAL_COEFFICIENT_ASSESSMENT_20261030.md
[progress]: ../../research-progress/06_FIXED_COEFFICIENT_PARAMETER_GEOMETRY_RESEARCH_PROGRESS_20261030.md
[packet]: ../../research-progress/handoffs/fixed_coefficient_parameter_geometry/FCG-E01_R1_CORRELATED_JET_COEFFICIENT_20261030.md
[r2]: 12_REGIONAL_MOMENT_COEFFICIENT_AND_COMMON_FLOW_LIMITS_B03_R2_20261030.md
[selfreview]: ../../reviews/fixed_coefficient_parameter_geometry/04_QUADRATIC_HEAT_BEZOUT_B03_R3_SELF_ASSESSMENT_20261030.md
[continuation]: 17_CONTINUATION_FCG_E01_R1_JOINT_JET_COEFFICIENT_20261030.md
[direct]: ../../../../investigations-3/11_arithmetic_collision_rigidity/symmetries/03_normalized_jet_rotation/notes/01_SIGNED_TRANSPORT_AND_DIRECT_JET_COMPARISON_20261018.md
[cost]: ../../../../investigations-3/11_arithmetic_collision_rigidity/symmetries/03_normalized_jet_rotation/notes/12_MATCHED_COMPLETE_CONSUMER_AND_COST_COMPARISON_20261019.md
[evaluator]: ../../../../investigations-3/11_arithmetic_collision_rigidity/numerics/certify_shifted_theta_jet.py
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[workflow]: ../../../../../GPT_RESEARCH_MODEL_WORKFLOW.md
[results]: ../../../../../result-summaries/README.md
[avoid]: ../../../../../avoid/README.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[a14]: ../../../../../avoid/14_convenience_hypotheses_and_circular_definitions.md
