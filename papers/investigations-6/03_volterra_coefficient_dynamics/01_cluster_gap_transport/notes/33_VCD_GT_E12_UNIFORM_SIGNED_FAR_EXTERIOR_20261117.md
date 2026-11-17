# VCD-GT-E12 r1 — Uniform signed far exterior

17 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex assistance. Tool-selected executor dispatch **gpt-6.1-sol /
ultra**. Separate serving-model and actual reasoning-effort metadata were
unavailable to the executor. All four frozen input SHA-256 hashes matched.
[Request][request] · [Decision15][decision] · [Source-use05][source]

**Proved in-note**, conditional on the independently paid count-two
geometry for the unchanged canonical field. This is a quantitative
intermediate estimate in the classification of [Avoid01][classification].
Its output is a centered far-tail main term with a uniform error. The
signed near sum and a strict incoming gap margin remain open inputs for
new tubes. [Result summaries][results] · [Controls12][controls] ·
[Avoid index][avoid] · [Premises02][premises] · [Scope07][scope]

## 1. Pair and full divisor

Use \(H_0(z)=\xi((1+iz)/2)/8\) and \(\partial_tH_t=-\partial_z^2H_t\)
for \(0\le t\le1/2\). The unchanged field is real under conjugation and
even. Use the inherited order-at-most-one product and \(|\Im\rho|\le1\)
for every zero \(\rho\), counted with multiplicity. The order proof
applies with the same double-exponential majorant and heat weight
bounded by \(e^{u^2/2}\) on this slab. This majorant supplies locally
uniform convergence \(H_t\to H_0\) as \(t\downarrow0\) by dominated
convergence on compact \(z\)-sets. On the imaginary axis the canonical
integral weights the positive source by \(e^{tu^2}\cosh(u\Im z)>0\),
so \(H_t\) has no zero there. [Note21 §1][product] · [Source-use05][source]

Let \(z_1,z_2\) be a counted isolated pair on a conjugation-invariant
contour with a paid collar. Set \(c=(z_1+z_2)/2\) and
\(D=(z_1-z_2)^2/4\), both real. Assume \(c\ge16\pi\), \(|D|\le1\)
and \(3\le R\le c/2\). The absolutely convergent deflated product gives
\[
 M=-K=\sum_{\rho\ {\rm exterior}}
       \frac{1}{(z_1-\rho)(z_2-\rho)}.
\]
Here exterior excludes the two target occurrences. The formula uses
the divided difference of the deflated logarithmic derivative, with
its derivative limit at \(D=0\). The collar separates the remaining poles.
Absolute convergence permits conjugate grouping. For \(\rho=c+x+iy\)
the real part after grouping is
\[
 q(x,y,D)=\frac{x^2-y^2-D}{(x^2-y^2-D)^2+4x^2y^2}.
\]
A real zero contributes one copy of \(q\) per occurrence. A conjugate
pair contributes two copies. Thus with sums over occurrences,
\[
 S_R=\sum_{\rho\ {\rm exterior},\,|x|\le R}q(x,y,D),\qquad
 T_R=M-S_R=\sum_{|x|>R}q(x,y,D).
\]
The strict far cutoff already omits the target because
\(|\Re z_j-c|\le1\) by \((z_j-c)^2=D\).
Both cutoff lines belong to the signed near sum.

## 2. Uniform counting, including time zero

Let \(\mu_t=\sum_{\Re\rho>0}\delta_{\Re\rho}\), over the full canonical
multiset, and \(N_t(X)=\mu_t((0,X])\). Write
\[
 g(X,t)=\frac{X}{4\pi}\log\frac{X}{4\pi}-\frac{X}{4\pi}
       +\frac{11}{8}+\frac{t}{16}\log\frac{X}{4\pi},
 \qquad F_t(X)=N_t(X)-g(X,t).
\]
For \(X\ge4\pi,\ 0<t\le1/2\) use the checked Polymath v2
Theorem 1.5(iv) bound \(\lvert F_t(X)\rvert\le C_0\log(2+X)\)
in the right-continuous convention of Source-use05. The input counts
complex zeros with multiplicity, has an absolute constant, and holds
on this range without a time-dependent large-height onset. The same
part supplies the unit upper count. [Source-use05][source]

To include \(t=0\), fix \(X>4\pi\). Choose \(\varepsilon\downarrow0\)
with \(X-\varepsilon>4\pi\) such that both lines at \(X\pm\varepsilon\)
avoid the real coordinates of the zeros of \(H_0\). Only finitely many
coordinates are excluded in the bounded region. Use rectangles with
left side \(\Re z=0\), right side \(\Re z=X\pm\varepsilon\), and
horizontal sides \(\Im z=\pm2\). By §1 and the chosen sides their
boundaries are zero-free for \(H_0\). Compact convergence and Rouché's
theorem give \(N_t(X\pm\varepsilon)=N_0(X\pm\varepsilon)\) for all
sufficiently small positive \(t\) at each fixed \(\varepsilon\).
The strip makes the rectangular counts the complete cumulative
counts at these endpoints. Sending \(t\downarrow0\) first gives
\[
 g(X-\varepsilon,0)-C_0\log(2+X-\varepsilon)
 \le N_0(X-\varepsilon)\le N_0(X)\le N_0(X+\varepsilon)
 \le g(X+\varepsilon,0)+C_0\log(2+X+\varepsilon).
\]
Sending \(\varepsilon\downarrow0\) in the outer bounds pays the full
possible atom at \(X\), including all occurrences sharing that real
coordinate. At \(X=4\pi\) the upper bound follows by approaching from
above and the lower bound follows from \(N_0(4\pi)\ge0\) with an
absolute enlargement of \(C_0\). The contour agreement may require
different small times for different endpoints. The resulting bound
has an absolute discrepancy constant on the closed slab.

For \(X>4\pi\) the left limit \(F_t(X-)\) obeys the same bound.
In particular \(J_t(X):=\mu_t\{X\}=F_t(X)-F_t(X-)\ll\log(2+X)\).
At \(X=4\pi\), the total atom is bounded by \(N_t(4\pi)\ll1\).
Subtracting counts as \(\mu_t([U,U+1])=N_t(U+1)-N_t(U-)\)
and bounding the \(g\)-increment gives the closed unit-window bound
\(\mu_t([U,U+1])\ll\log(2+U)\) for \(U>4\pi\). For
\(0\le U\le4\pi\) use \(N_t(4\pi+1)\ll1\).
Also \(N_t(U)\ll U\log(2+U)\) for \(U\ge4\pi\).
Evenness reflects the positive-height divisor to negative heights
with multiplicities preserved. The compact argument extends the
cumulative discrepancy. The earlier unit-count extension and
inverse-square shell method appear in [TND-O Note18 §§1, 3][predecessor].

## 3. Conjugate expansion and full remainder

For \(|x|>R\), put \(h=y^2+D\). Then \(|h|\le2\),
\(x^2-h\ge(7/9)x^2\), and direct subtraction gives
\[
 q(x,y,D)-x^{-2}
  =\frac{(D-3y^2)x^2-h^2}{x^2\{(x^2-h)^2+4x^2y^2\}}
  =O(|x|^{-4}).
\]
The numerator is \(O(x^2)\) and the denominator is bounded below
by a fixed positive multiple of \(x^6\). This uses the real part
after grouping, with the odd imaginary term canceled. The same
\(x^2-h>0\) proves positivity of every far weight.

Write \(G=\log(2+c)\), \(u=\Re\rho\), \(\alpha=c/2\) and
\(\beta=3c/2\). In the central band \([\alpha,\beta]\), cover
each side of \(R+j<|u-c|\le R+j+1\), \(j\ge0\), by a closed
unit window if it meets the band. For nonempty shells the starts
are between \(\alpha-1\) and \(\beta\), so the count per shell
is \(O(G)\). The central sum of \(|u-c|^{-4}\) outside the
cutoff is \(O(G\sum_{j\ge0}(R+j)^{-4})=O(G/R^3)\).

For \(p\in\{2,4\}\), the low positive region \(0<u<\alpha\)
contributes \(O(G/c^{p-1})\) to \(\sum |u-c|^{-p}\) by
\(|u-c|\ge c/2\) and \(N_t(\alpha)\ll cG\).
For \(u>\beta\) one has \(u-c\ge u/3\). The dyadic interval
\(2^j\beta<u\le2^{j+1}\beta\) has count \(O(2^jc(G+j))\), so
summing the weighted bounds gives \(O(G/c^{p-1})\) since \(p>1\).
For \(u=-s<0\) the weight is \((c+s)^{-p}\).
Reflection and \(N_t(c)\ll cG\) pay \(O(G/c^{p-1})\) for
\(0<s\le c\), and the dyadic intervals in \(s>c\) with base
\(c\) give the same bound. This includes the reflected target
and every other negative-height occurrence. All these remote
regions are outside the cutoff. Section 1 excludes \(u=0\).

The central and remote estimates at \(p=4\) give a full
fourth-order remainder \(O(G/R^3)\), using \(R\le c/2\).
The remote estimates at \(p=2\) then give
\[
 T_R=\int_{[\alpha,\beta]\cap\{|u-c|>R\}}\frac{d\mu_t(u)}{(u-c)^2}
       +O(G/R^3+G/c). \tag{1}
\]
All exterior complex roots are included, with their vertical
offsets covered by the uniform kernel remainder.

## 4. Stieltjes payments and the centered main term

For \(R<c/2\), put \(a=c-R,\ b=c+R\) and
\(f(u)=(u-c)^{-2}\). The two domains in (1) are
\([\alpha,a)\) and \((b,\beta]\). The atom at \(a\) is dropped
when changing from \([\alpha,a]\) to \([\alpha,a)\), and the
atom at \(b\) is dropped when changing from \([b,\beta]\) to
\((b,\beta]\). Their inverse-square payments \(R^{-2}J_t(a)\)
and \(R^{-2}J_t(b)\) are each \(O(G/R^2)\).
The half-open formulas incorporate these payments exactly:
\[
\begin{aligned}
 \int_{[\alpha,a)} f\,dF_t
   &=f(a)F_t(a-)-f(\alpha)F_t(\alpha-)
     -\int_\alpha^a f'(u)F_t(u)\,du,\\
 \int_{(b,\beta]} f\,dF_t
   &=f(\beta)F_t(\beta)-f(b)F_t(b)
     -\int_b^\beta f'(u)F_t(u)\,du .
\end{aligned}
\tag{2}
\]
Here \(dF_t=d\mu_t-\partial_u g(u,t)\,du\) on the band.
The one-sided values also keep the atoms at \(\alpha,\beta\)
in (1). All displayed discrepancy values are \(O(G)\).
Each endpoint value of \(f\) is at most \(R^{-2}\), and the
variation of \(f\) on each side is at most \(R^{-2}\) by
monotonicity. Thus (2) costs \(O(G/R^2)\). At \(R=c/2\)
both central intervals are empty and contribute zero. Their
endpoints then coincide with the cutoff lines and belong to
\(S_R\), so the strict remote ranges in §3 also give the
correct count at this endpoint.

On the central band the smooth density satisfies, uniformly in \(t\),
\[
 \partial_u g(u,t)=\frac{1}{4\pi}\log\frac{u}{4\pi}+\frac{t}{16u}
  =\frac{L}{4\pi}+O\!\left(\frac{|u-c|+1}{c}\right),
 \qquad L=\log\frac{c}{4\pi}.
\]
Replacing the density by \(L/(4\pi)\) costs
\[
 O\!\left(\frac1c\int_R^{c/2}\frac{s+1}{s^2}\,ds\right)
 =O\!\left(\frac{\log(c/(2R))+1/R}{c}\right)=O(G/c).
\]
Integrating the constant density on both sides yields
\[
 \frac{2L}{4\pi}\int_R^{c/2}\frac{ds}{s^2}
 =\frac{L}{2\pi R}-\frac{L}{\pi c}.
\]
The subtracted term is \(O(G/c)\). Both density integrals are
zero in the empty central band case. Equations (1)–(2) prove
\[
 \boxed{\displaystyle
 \left|M-S_R-\frac{\log(c/(4\pi))}{2\pi R}\right|
 \le C\left(\frac{\log(2+c)}{R^2}+\frac{\log(2+c)}{R^3}
                   +\frac{\log(2+c)}{c}\right).}
 \tag{3}
\]
The constant is absolute and can depend on the published count
constant. The proof leaves its numerical value unevaluated.

## 5. Scaling and matched direct comparison

At a fixed sufficiently large physical \(R\), (3) gives
\(T_R\asymp L/R\) as \(c\to\infty\), uniformly on the slab.
Indeed, the error divided by \(L/R\) is at most
\(C(G/L)(R^{-1}+R^{-2}+R/c)\). Choose fixed \(R\) to make
the first two terms sufficiently small, then let \(c\) grow.
This uses \(G=L+O(1)\) and the main-term coefficient \(1/(2\pi)\).

For \(L\ge9\), \(R=\sqrt L\) is admissible since \(c/2=2\pi e^L\).
The errors in (3) are \(O(1)\), \(O(L^{-1/2})\), and
\(O(Le^{-L})\), respectively. Thus uniformly on the closed slab,
\[
 T_{\sqrt L}=\frac{\sqrt L}{2\pi}+O(1),\qquad
 \ell^2 T_{\sqrt L}
   =\frac{1}{2\pi L^{3/2}}+O(L^{-2}),\qquad \ell=1/L.
\]
The scale \(\ell\) is frozen at the evaluation height. Positive far
mass becomes small in this normalized interaction. Nearby terms
retain their signs and can have small denominators. As occurrences
cross the moving sharp cutoff, \(S_R\) and \(T_R\) can jump by equal
and opposite weights.
The total mass on the cutoff lines at a fixed slice is \(O(G/R^2)\)
by the atom estimate and \(|q|\ll R^{-2}\) there, using the same
kernel inequality at \(|x|=R\ge3\). The two sums always recombine
to the original regular \(M\) on a paid tube.

The inherited physical-time law is \(D'=2-4MD\).
The existing integrating-factor allowance for a backward passage
from \(v\) to \(u\) compares \(D(v)\) to
\(2\int_u^v\exp(-4\int_t^vM(s)\,ds)\,dt\).
Equation (3) pays only the far part of its exponent. A separate
signed near estimate and the strict incoming allowance remain due
for a new gap conclusion. The estimate leaves finite certified
onset open. [Decision15][decision] · [Note21 §§3–4][product]

The equally informed direct comparison receives the same complete
field, physical-time law, order and strip, uniform cumulative and
unit counts, counted pair and collar, values or enclosures of \(c,D\),
signed near-sum formula with the same cutoff, and the full estimate
(3) with its endpoint conventions. Any independently acquired near
data or incoming values also go to that comparator. These inputs
give the same possible enclosure of \(M\) through direct deflation
and the same scalar gap law. Near enclosure acquisition and runtime
comparison remain outside the estimate.

## 6. Documentary control replay

The transfer test uses the explicit order, strip and density
premises and keeps the incoming margin independent. Passing the count
leaves the signed near field to pay. These verdicts concern the
documented classes with their stated assumptions.
[Decision15][decision] · [Controls12][controls] ·
[Note21 §6][product] · [Premises02][premises] · [Scope07][scope]

| Control | Verdict for the premises used here |
| --- | --- |
| Quadratic and even quartic | They can share the order and strip on the stated slabs. Their finite divisor fails the growing cumulative main term. The even quartic of Note21 already witnesses failure of the strict incoming allowance even with positive exterior mass. |
| Nonzero quadratic-exponential factor and reflected super-Gaussian | The former has order two in the stated examples. The latter has imaginary-axis growth \(\log H_t(iy)\gg y^{4/3}\) from its positive \(e^{-u^4}\) component. Each fails the product's order-at-most-one premise as used here. |
| Three- and four-weighted-square, finite theta/zero-tail changes including finite-score changes, and bounded positive finite-prime orbits | In the documented endpoint-defective classes, the first nonzero odd endpoint survives the even heat weight. The resulting nonzero algebraic leading term in each fixed horizontal strip leaves finitely many zeros there, while the growth argument supplies infinitely many zeros in total. The global finite-strip premise fails in these classes. |
| Euler-factor translates | For the factor \(1+\gamma\cos(az)\), \(a=\tfrac12\log p>0\), the documented \(0<\gamma<1\) factors fail width one when \(\operatorname{arccosh}(1/\gamma)/a>1\), and otherwise can pass. At \(t=0\) every nonconstant factor adds \(aX/\pi+O(1)\) positive-height occurrences, two per period \(2\pi/a\) with multiplicity, even at common product roots. The endpoint-inclusive canonical \(O(\log(2+X))\) discrepancy fails. The endpoint suffices to test the uniform hypothesis. [Euler-factor source][euler] |
| Damped smooth-shape and positive-primitive controls | Their double-exponential damping supplies the order bound. Strip and exact cumulative discrepancy are untested here. Positive shape, primitive data and changed source do not decide the count inequality. |
| Reflection rigidity and four-family comparison | In the stated polynomially weighted square-comb class, full reflection and the normalized endpoint force the unchanged theta weights. The four-family comparison takes the foregoing order, strip and count verdicts family by family. |
| BW-01 finite-atom and compact-source finite-profile controls | Exponential type and Jensen's bound give \(O(X)\) zeros of \(|z|\le X+1\), with multiplicity. Under the strip premise this would bound their positive-height counts by \(O(X)\), contrary to the canonical main term. |
| RH-conditional normalized endpoint mergers | Under the control's RH premise, order and strip can survive. The exact cumulative discrepancy is untested here. A qualifying interval starting at an added double has zero strict incoming margin. |
| Varied observation kernels and fractional-profile relaxation | The varied kernels lack the literal cosine/Newman field equation. The fractional measures do not furnish the multiplicity-counted divisor of a specified analytic heat field. Neither supplies the hypotheses of the canonical count/product argument. |

The scope of (3) is the complete canonical field and the conditional
count-two application above. The replay concerns transfer of its
estimate, with collisions and incoming gap signs outside that scope.

[request]: ../research-progress/handoffs/VCD-GT-E12-r1.md
[decision]: ../brainstorm/notes/15_VCD_GT_B07_NEAR_FAR_COUNT_DECISION_20261117.md
[source]: ../references/05_VCD_GT_UNIFORM_COUNT_SOURCE_USE_20261117.md
[product]: 21_VCD_GT_E03_JOINT_CONJUGATE_SOURCE_ESTIMATE_20261116.md
[predecessor]: ../../../../investigations-5/08_theta_observables_newman_dynamics/03_operator_imaginary_time_evolution/notes/18_TND_O_E10_CANONICAL_MODULUS_AND_SHARPNESS_20261107.md
[euler]: ../../../../investigations-2/active/19_euler_factor_controls/manuscript/euler_factor_controls.tex
[results]: ../../../../../result-summaries/README.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../avoid/README.md
[classification]: ../../../../../avoid/01_restating_the_target.md
[premises]: ../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[scope]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
