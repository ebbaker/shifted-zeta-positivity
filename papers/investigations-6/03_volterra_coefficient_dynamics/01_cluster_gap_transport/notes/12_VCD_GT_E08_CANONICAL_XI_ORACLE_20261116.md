# VCD-GT-E08 — Complete xi evaluation and signed-cost error bounds

16 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. Helper dispatched
**gpt-6.1-sol / ultra**. Lead settings and separate backend attestation of
the dispatch are unavailable. Proof-author checks are internal.

**Proved in-note** for the fixed evaluation domain; the contour and cost
bounds are conditional on the acquisition premises in §§4–5. This is a
finite quantitative evaluation contract under
[Decision04](../brainstorm/notes/04_VCD_GT_B04_CANONICAL_LEHMER_ACQUISITION_20261116.md).
It supports a local comparison of estimates from the same complete
source. See the [frozen E08 r1 request](../research-progress/handoffs/VCD-GT-E08-r1.md),
[result index](../../../../../result-summaries/README.md),
[controls12](../../../../../result-summaries/12_collision_controls_and_screening.md),
and the [avoid index](../../../../../avoid/README.md), especially
[classification01](../../../../../avoid/01_restating_the_target.md),
[control premises02](../../../../../avoid/02_shape_only_arguments_and_the_controls.md),
[scope07](../../../../../avoid/07_scoped_exclusions_read_as_universal.md),
[normalization08](../../../../../avoid/08_normalization_and_constant_slips.md)
and [source imports16](../../../../../avoid/16_unchecked_imports_and_novelty_claims.md).

## 1. Complete source and normalization

Use the parent [manuscript's complete source](../../manuscript/main.tex).
For \(u\ge0\), write \(r_m=\pi m^2 e^{4u}\),
\(\Phi(u)=e^u\sum_{m\ge1}(2r_m^2-3r_m)e^{-r_m}\), and extend \(\Phi\)
evenly. This is the literal theta source. Its physical field is
\[
 H_t(z)=\frac12\int_{\mathbb R}\Phi(u)e^{tu^2}e^{izu}\,du.
 \tag{1}
\]
The modulus of \(\Phi(u)\), with \(U=|u|\), is at most
\[
 2\pi^2 e^{9U}e^{-\pi e^{4U}}
       \sum_{m\ge1}m^4 e^{-\pi(m^2-1)}.
 \tag{2}
\]
In fact \(r_m\ge\pi\) and \(e^{4U}\ge1\), so each summand has the
indicated nonnegative envelope. This also gives local domination for
the derivatives in \(z,t\) of (1), and \(\partial_t H_t=-\partial_z^2 H_t\).

The time-zero factor follows directly from the theta primitive. With
\(\psi(v)=\sum_{m\ge1}e^{-\pi m^2 v}\) and \(p(u)=e^u\psi(e^{4u})\),
termwise differentiation gives \(\Phi=(p''-p)/8\). In the inherited
Jacobi inversion identity \(p(-u)-p(u)=\sinh u\), differentiation at
zero gives \(p'(0)=-1/2\). If \(I(z)=\int_0^\infty p(u)\cos(zu)\,du\),
two integrations by parts yield
\[
 8H_0(z)=\tfrac12-(1+z^2)I(z).
\]
The integrations are valid by the double-exponential decay of \(p,p'\),
obtained from their respective complete sums as in (2). For
\(\Re s>1\), termwise Mellin integration of \(\psi\), splitting at
one and applying Jacobi inversion below one, gives
\[
 \pi^{-s/2}\Gamma(s/2)\zeta(s)=
 \frac{1}{s(s-1)}
 +\int_1^\infty \psi(v)
   \bigl(v^{s/2-1}+v^{(1-s)/2-1}\bigr)\,dv .
\]
The last integral is entire in \(s\) and invariant under \(s\mapsto
1-s\). For \(s=(1+iz)/2\), substitution \(v=e^{4u}\) makes it \(8I(z)\),
and \(s(s-1)=-(1+z^2)/4\). Consequently
\[
 H_0(z)=\frac18\xi((1+iz)/2),\qquad
 \xi(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s),
 \qquad \xi(s)=\xi(1-s).
 \tag{3}
\]
This continuation agrees with the checked standard completion and
reflection equations. See the [reference addendum](../references/02_VCD_GT_XI_QUADRATURE_BOUND_SOURCES_20261116.md).

For \(q=\sqrt t\) and \(0\le t\le 1/10\), the modulus of the double
integrand in \(e^{-r^2}H_0(z+2iqr)\) on \(\mathbb R^2\), after (1)
is inserted, is
\[
 \tfrac12\Phi(u)e^{-\Im(z)u}\exp(-(r+qu)^2+tu^2).
\]
Tonelli and the Gaussian integral make its double integral finite by
(2), with the bound
\(\tfrac{\sqrt\pi}{2}\int_{\mathbb R}\Phi(u)e^{tu^2+|\Im z||u|}\,du\).
Thus Fubini gives the exact complete-field identity
\[
 H_t(z)=\frac1{\sqrt\pi}\int_{\mathbb R}e^{-r^2}
                       H_0(z+2i\sqrt t\,r)\,dr.
 \tag{4}
\]
Real zero height \(x\) corresponds to zeta ordinate \(x/2\).
At \(a=140101/10\), the high-height gamma factor in (3) has decay
\(e^{-\pi a/8}\), so set \(g=e^{\pi a/8}\) and \(G_t=gH_t\).
The constant positive factor \(g\) preserves all cluster coordinates.

## 2. A uniform strip majorant

Let \(f(r)=g e^{-r^2}H_0(z+2iqr)\). It is entire in \(r\). Fix
\(|z-a|\le2\), \(q=\sqrt t\), \(0\le t\le 1/10\), and
\(r=\nu+i\eta'\) with \(|\eta'|\le2\). Write \(U=|\nu|\),
\(s_0=(1+i(z+2iqr))/2\), and use (3) to select \(s\in\{s_0,1-s_0\}\)
with \(\sigma=\Re s\ge1/2\). Put \(\omega=s/2=X+iY\).
Directly,
\[
 \tfrac14\le X\le\tfrac34+\tfrac4{25}U,\qquad
 \left||Y|-\tfrac a4\right|\le\tfrac12+q,\qquad
 3501<|Y|<3504.
 \tag{5}
\]
Indeed \(|Y|=|\Re z/4-q\eta'/2|\) and
\(X=1/4+|\Im z/4+q\nu/2|\). As \(\sigma\ge1/2\), this gives
\[
 |\omega|\le3505+\tfrac4{25}U,\qquad
 |s-1|\le|s|\le7010+\tfrac8{25}U .
 \tag{6}
\]

For the gamma factor use the checked right-half-plane Laplace form of
Binet's formula. With the logarithm analytic there, it writes
\[
 \log\Gamma(\omega)
  =(\omega-\tfrac12)\log\omega-\omega+\tfrac12\log(2\pi)+R(\omega),
 \qquad
 R(\omega)=\int_0^\infty e^{-\omega v}
        \left(\frac1{e^v-1}-\frac1v+\tfrac12\right)\frac{dv}{v}.
\]
[DLMF equation 5.9.10_2](https://dlmf.nist.gov/5.9#E10_2).

For \(b=v/2>0\), the bracket is \((\coth b-1/b)/2\), between
zero and \(v/12\). For the lower bound, the coefficient of \(b^{2n+1}\)
in \(b\cosh b-\sinh b\) is \(2n/(2n+1)!\). For the upper bound,
the corresponding coefficient in \((1+b^2/3)\sinh b-b\cosh b\)
is \(2n(2n-2)/(3(2n+1)!)\) for \(n\ge1\) and zero for \(n=0\).
Both series are nonnegative on \(b>0\). The remainder satisfies
\(|R(\omega)|\le 1/(12X)\). Taking real parts in Binet and using
\[
 -Y\arg\omega=-\tfrac\pi2|Y|
             +|Y|\arctan(X/|Y|)\le-\tfrac\pi2|Y|+X
\]
gives the bound that retains the entire height exponential,
\[
 |\Gamma(\omega)|e^{\pi|Y|/2}
 \le \sqrt{2\pi}\,|\omega|^{X-1/2}e^{1/(12X)}.
 \tag{7}
\]
At \(Y=0\) the same bound follows directly from Binet.

Euler summation with \(N=1\) on \(\sigma>0,\ s\ne1\) gives
\(\zeta(s)=s/(s-1)-s\int_1^\infty \{v\}v^{-s-1}\,dv\).
On (5), \(|s-1|\ge|\Im s|>7002\), so \(|\zeta(s)|\le3|s|\).
[DLMF equation 25.2.8](https://dlmf.nist.gov/25.2#E8).

Now \(g e^{-\pi|Y|/2}\le e^{(\pi/2)(1/2+q)}<4\), and
\(|\pi^{-s/2}|\le1\), \(e^{1/(12X)}\le e^{1/3}<3/2\),
\(\sqrt{2\pi}<3\). Equations (3), (5)–(7) imply
\[
 |f(\nu+i\eta')|
 \le \frac{4\cdot3\cdot(3/2)\cdot3}{16}
 (7010+\tfrac8{25}U)^3
 (3505+\tfrac4{25}U)^{1/4+(4/25)U}e^{\eta'^2-U^2}.
\]
For explicit constants use \(\log(1+u)\le u\) for \(u\ge0\).
The prefactor at \(U=0\) is below \(27\cdot 7010^3<10^{13}\),
using \(3505^{1/4}<8\). The linear coefficient in the remaining
logarithm is at most
\[
 \tfrac4{25}\log(3505)+
 \frac{1}{4}\frac{4/25}{3505}
 +\frac{3(8/25)}{7010}<\tfrac{131}{100},
\]
and the added quadratic coefficient is \((4/25)^2/3505<1/10000\).
Here \(\log(3505)<409/50\) follows, for example, by the finite lower
bound \(\sum_{k=0}^{24}(409/50)^k/k!>3505\) on \(e^{409/50}\).
For the factor \(4\), use \(\pi<22/7\), \(q<8/25\),
\((\pi/2)(1/2+q)<4/3\) and \(e^{1/3}<7/5\). The last bound
follows by bounding the exponential series tail starting at order
two by \((1/18)/(1-1/9)\). Thus a uniform exact majorant is
\[
 \boxed{|f(\nu+i\eta')|\le C e^{\eta'^2-\alpha U^2+\beta U},\qquad
 C=10^{13},\quad \alpha=9999/10000,\quad \beta=131/100.}
 \tag{8}
\]
Integrating the real-line majorant in (4) also gives the uniform disk
bound
\[
 \sup_{\substack{|z-a|\le2\\0\le t\le1/10}}|G_t(z)|
 \le M_2=\frac{2C}{\sqrt\alpha}\exp(\beta^2/(4\alpha)).
\]
This can pay spatial Taylor tails through Cauchy's formula on
\(|z-a|=2\).

## 3. Infinite lattice and finite tails

For \(\widehat f(\omega)=\int_{\mathbb R}f(\nu)e^{-i\omega\nu}\,d\nu\),
shift to \(\Im r=-2\) for \(\omega>0\) and \(+2\) for \(\omega<0\).
The vertical sides tend to zero by (8). If \(M_\pm\) bound the \(L^1\)
integrals on the two lines, then
\[
 |\widehat f(\omega)|\le
 \begin{cases}
 M_-e^{-2\omega},&\omega>0,\\
 M_+e^{-2|\omega|},&\omega<0.
 \end{cases}
\]
The continuous periodized function \(h\sum_{k\in\mathbb Z}f(x+kh)\)
has Fourier coefficients \(\widehat f(2\pi n/h)\), as follows by
uniform summability from (8) and integration over one period.
These coefficients are absolutely summable by the shift estimate.
Evaluating their Fourier series at \(x=0\) and summing the two geometric
tails yields
\[
 \left|h\sum_{k\in\mathbb Z}f(kh)-\int_{\mathbb R}f(r)\,dr\right|
 \le \frac{M_++M_-}{e^{4\pi/h}-1},\qquad
 M_\pm=2C\sqrt{\pi/\alpha}\,\exp(4+\beta^2/(4\alpha)).
 \tag{9}
\]
The displayed \(M_\pm\) come from translating the half-line Gaussian
and bounding its integral by the whole Gaussian.

For both fixed steps \(h=1/3,1/4\) the endpoints \(\pm 12\) are
lattice nodes. On \(u\ge12\) the exponent \(-\alpha u^2+\beta u\)
decreases, so the sum of omitted lattice terms is at most
\(2C\int_{12}^\infty e^{-\alpha u^2+\beta u}\,du\) after multiplication
by \(h\). Bounding this concave exponent by its tangent at \(12\)
gives the explicit second term below. The full source evaluator
\[
 G^{[h]}_t(z)=\frac{h}{\sqrt\pi}\sum_{|kh|\le12} f(kh)
\]
has the uniform absolute error on the stated disk and time interval
\[
 \boxed{\quad
 |G_t-G^{[h]}_t|
 \le E_h=
 \frac{4C\,e^{4+\beta^2/(4\alpha)}}{\sqrt{\alpha}(e^{4\pi/h}-1)}
 +\frac{2C\,e^{-144\alpha+12\beta}}{\sqrt\pi(24\alpha-\beta)} .
 \quad}
 \tag{10}
\]
The formulas use exact constants; outward evaluation and finite-sum
arithmetic enclosures are separate. For scale, \(E_{1/3}\) is
approximately \(0.1423\), \(E_{1/4}\) approximately \(4.9611\cdot10^{-7}\),
and the shared second term approximately \(9.81\cdot10^{-45}\).
These are absolute allowances in the fixed gauge. A relative allowance
requires the modulus floor below.

## 4. Contour log and coordinate errors

At each time let \(\Gamma=\{|z-a|=\rho\}\) be counterclockwise,
\(w=z-a=\rho e^{i\theta}\), with \(\rho=9/10\), and let
\(\langle\,\cdot\,\rangle\) denote the normalized angular mean.
The acquisition premises are that \(G_t\) has count two within
\(\Gamma\) and is zero-free on a collar of \(\Gamma\). The argument
principle gives index zero for \(G_t/w^2\) on the collar. A holomorphic
log \(L=\log(G_t/w^2)\) exists on the annulus since its logarithmic
derivative has vanishing generator period. The angular lift is
periodic. For \(k\ge1\) the two offset power sums satisfy
\[
 p_k=\frac1{2\pi i}\oint_\Gamma w^k\frac{G_t'}{G_t}\,dz
     =-\frac{k}{2\pi i}\oint_\Gamma w^{k-1}L\,dz
     =-k\langle w^k L\rangle .
 \tag{11}
\]
The term \(2/w\) in the log derivative integrates to zero after
multiplication by \(w^k\). The formulas
\(c=a+p_1/2,\ D=p_2/2-p_1^2/4,\ Q=(z-c)^2-D\) now hold even
for a double zero, where the two offsets coincide. Reality under
conjugation of \(G_t\) makes \(c,D\) real.

Write \(A=G_t/Q\) and \(B=A'/A\), holomorphic through the cluster.
The regular pair drift \(K=(2\pi i)^{-1}\oint_\Gamma B/Q\,dz\)
is the divided difference of \(B\) at the two zeros, with derivative
at a double zero. Replacing \(B\) by \(G_t'/G_t\) adds the integral
of \(Q'/Q^2\), which is zero. Inserting \(G_t'/G_t=L'+2/w\)
adds the rational term \(2/(wQ)\), whose poles are all inside \(\Gamma\)
and whose integral vanishes by \(O(z^{-3})\) decay at infinity. Integration
by parts gives the derivative-free formula
\[
 K=\big\langle -w (1/Q)'L\big\rangle
   =\left\langle\frac{2w(z-c)L}{Q^2}\right\rangle .
 \tag{12}
\]
All exact means in (11)–(12) annihilate constants in \(L\). For the
last mean this follows by integrating \((1/Q)'\) around \(\Gamma\).

For a concrete source-to-log payment, let \(\widetilde G\) be a
holomorphic approximate field, for example the exact finite lattice
sum in (10). Suppose \(\sup_\Gamma|G_t-\widetilde G|\le\delta\)
and \(\inf_\Gamma|\widetilde G|\ge m>\delta\). When either field has
verified count two, Rouché transfers the count. Both admit periodic
collar logs and the branch for their difference can be chosen by the
series for \(\log(1+(G_t-\widetilde G)/\widetilde G)\).
It gives \(\ell=-\log(1-\delta/m)\) as a uniform log error. The ratio
extends to a collar where the series converges, by strictness and
compactness. Source discrepancy (10) can enter \(\delta\).
Nodewise arithmetic can be paid separately against the exact analytic
model values and their common branch.

More generally assume a log approximation \(\widetilde L\) on
\(\Gamma\) with \(\sup_\Gamma|L-\widetilde L|\le\ell\) after aligning
branches. Let \(q_j\) bound the angular integration and arithmetic
error of the approximate moment \(-j\langle w^j\widetilde L\rangle\).
Hence
\[
 |p_j-\widetilde p_j|\le j\rho^j\ell+q_j,\qquad
 e=\frac{\rho\ell+q_1}{2}\ \ge |c-\widetilde c|.
 \tag{13}
\]
If both computed and actual pair polynomials have roots in
\(|z-a|\le \rho-b\), \(b>0\), then
\[
 d=\rho^2\ell+q_2/2+2(\rho-b)e\ \ge |D-\widetilde D|.
 \tag{14}
\]
This uses
\(\left|(c-a)^2-(\widetilde c-a)^2\right|
 \le 2(\rho-b)|c-\widetilde c|\).
With only \(|c-a|\le\rho-b\) verified, replacing the factor
\(2(\rho-b)\) in (14) by \(2(\rho-b)+e\) suffices for the coordinate
bound. The buffer can be obtained separately by certifying count two
on a smaller concentric circle for the true field and enclosing the
roots of the computed pair polynomial. Independent coordinate
enclosures can also be used.

For (12) take a common buffer \(b\) for \(Q\) and
\(\widetilde Q=(z-\widetilde c)^2-\widetilde D\).
Let \(\Lambda\ge\sup_\Gamma|\widetilde L-L_*|\) for a constant
\(L_*\); center both logs by \(L_*\) when using this bound. Define
\(J=(4\rho-2b)e+d\). On \(\Gamma\), each polynomial has modulus at
least \(b^2\) and \(|\widetilde Q-Q|\le J\).
From the product of two reciprocal linear factors,
\(|(1/Q)'|\le2/b^3\). Moreover
\[
 \begin{aligned}
 |(1/Q)'-(1/\widetilde Q)'|
 &\le 2e/b^4+
        2|z-\widetilde c|\,|1/Q^2-1/\widetilde Q^2|\\
 &\le 2e/b^4+4(2\rho-b)J/b^6 .
 \end{aligned}
\]
The second line uses the product of the difference and the sum of
reciprocals. If \(q_K\) bounds quadrature and arithmetic for the
centered approximate log and its computed kernel, then
\[
 \boxed{\quad |K-\widetilde K|\le \kappa
  =2\rho\ell/b^3+
   \rho\Lambda\big(2e/b^4+4(2\rho-b)J/b^6\big)+q_K .\quad}
 \tag{15}
\]
This is the integration-by-parts mechanism of
[Note04 §§1–2](04_VCD_GT_E02_COMPLETE_COORDINATE_TRANSFER_20261116.md)
applied entirely to log values. The common buffer covers arbitrary
pair multiplicity. Taking the real part of an approximate moment or
drift preserves its additive error against a real true value.

Verified node bounds and floats for the sampled contour winding,
minimum modulus, or pair position describe a sampled diagnostic.
Certification over the contour needs enclosures on its arcs, a
consistent periodic log branch, and angular quadrature allowances.
For example, for an analytic \(2\pi\)-periodic angular integrand with
supremum bounds \(A_+,A_-\) on \(\Im\theta=\pm d_\theta\), the \(n\)-node
angular mean has error at most \((A_++A_-)/(e^{n d_\theta}-1)\).
Shifting the Fourier coefficient integrals and summing aliases proves
this by the same argument as (9); it needs an enclosed analyticity
strip and boundary bounds for the actual integrand used. A constant
log centering for finite-grid evaluation must be included in the
definition of that integrand and its allowances.

## 5. Signed primitive, time cost and exact control

With count two and the collar premise on the time interval, differentiating
the exact moment formula before its integration by parts gives
\[
 D'=-\frac1{2\pi i}\oint_\Gamma (z-c)\,\partial_tG_t/G_t\,dz
    =\frac1{2\pi i}\oint_\Gamma (z-c)\,G_t''/G_t\,dz.
\]
Here the local time derivative and contour interchange is justified
by the smooth entire field and boundary nonvanishing. In the factorization
\(G_t=QA\), the first term from \(Q''/Q\) contributes exactly two,
since \((z-c)Q''/Q=Q'/Q\). The middle term is
\(2(z-c)Q'B/Q=4B+4D B/Q\). The terms holomorphic in the closed disk
integrate to zero. Hence \(D'=2+4KD\) through both simple and double
zeros, as in [Note04 §3](04_VCD_GT_E02_COMPLETE_COORDINATE_TRANSFER_20261116.md).

For \(I=[u,v]=[0,1/10]\) put \(S(t)=4\int_t^v K(s)\,ds\) and
\(\mathcal B=2\int_u^v e^{S(t)}\,dt\). If (15) holds on the full
interval for a real measurable and integrable evaluator
\(\widetilde K(s)\) with integrable \(\kappa(s)\), and
\(\widehat S(t)\) approximates \(4\int_t^v\widetilde K(s)\,ds\)
within \(\eta_S(t)\), then set
\[
 \Delta(t)=4\int_t^v \kappa(s)\,ds+\eta_S(t).
\]
This yields
\[
 2\int_u^v e^{\widehat S(t)-\Delta(t)}dt
 \ \le\ \mathcal B\
 \le 2\int_u^v e^{\widehat S(t)+\Delta(t)}dt .
 \tag{16}
\]
For numerical use the error integrals need upper enclosures and the
outer integrals need rigorous lower and upper evaluations, including
the exponent and the outer time quadrature. Using \(|\widetilde K|\)
and the same \(\kappa\) encloses the absolute-cost comparator, by
\(\big||K|-|\widetilde K|\big|\le\kappa\). The signed evaluation
retains the signs of \(\widetilde K\) in the primitive. Time interpolation
and geometry over every time subinterval need payments in addition
to agreement at time nodes.

The identity and orientation are
\[
 e^{S(t)}D(t)=D(v)-2\int_t^v e^{S(s)}ds .
 \tag{17}
\]
An incoming lower gap bound strictly greater than an upper cost in
(16) gives strict positivity on the closed interval. Equality of the
two bounds gives nonnegative \(D(u)\) and strict positivity at \(t>u\),
by positivity of the cost integrand. Division by the positive
\(e^{S(u)}\) gives the transported left-endpoint bound. When the
numerator is positive, an upper bound for \(e^{S(u)}\) gives the
lower transported estimate; for a negative numerator an enclosed
positive lower bound for \(e^{S(u)}\) gives the lower estimate.
The direct comparator uses the same source evaluator and
(13)–(14) at \(u\).

For the exact quadratic control take
\(G_t=w^2-2(t-T)\) with \(T=1/20\) and the same \(\rho,u,v\).
The pair stays inside \(|w|\le\sqrt{1/10}<\rho\), including at
the double time. The periodic branch
\[
 L=\log(1-2(t-T)/w^2)
   =-\sum_{n\ge1}\frac{[2(t-T)]^n}{n w^{2n}}
\]
converges on a collar. It gives \(p_1=0,\ p_2=4(t-T)\) by mode
selection. Formula (12) has angular mean zero since \(c=a\) and the
product \(2w^2L/(w^2-2(t-T))^2\) has only strictly negative
powers of \(w\) in its convergent Laurent series there. Thus
\(D=2(t-T),\ K=0,\ e^{S(t)}=1\). Signed and absolute costs both
equal \(2(v-u)=1/5\), while \(D(v)=1/10\). The transported
difference at zero is \(-1/10\); starting at \(T\) instead gives
equality and \(D(T)=0\). The count and collar persist through this
event, with the strict incoming-cost premise failing exactly as (17)
requires.

## 6. Scope and control screen

The finite source estimate (10) depends on the exact normalized
xi source in (3). The Gaussian identity as a transform principle
applies to a changed source under the corresponding absolute
integrability condition, and the local logarithm and cost formulas
apply to any qualifying heat field. On a counted tube that spans a
nondegenerate double event at \(T\), the exact incoming gap equals the
tail cost starting at \(T\), by (17). The cost on a longer interval
starting before \(T\) is strictly larger than that incoming gap.
This identifies the failed strict success premise for that geometry.
The table records the separate source or domain distinctions in
[controls12](../../../../../result-summaries/12_collision_controls_and_screening.md)
and [Note04 §4](04_VCD_GT_E02_COMPLETE_COORDINATE_TRANSFER_20261116.md).

| Control | Premise for this evaluation or gap comparison |
| --- | --- |
| Exact quadratic and the earlier quartic heat control | The quadratic shares the counted buffered tube and exhausts its gap at \(T\). The quartic's small-gap test and favorable force sign coexist with its local double event. Polynomial fields lack the literal xi source. |
| Euler-factor translates | The extra factor changes the unchanged canonical Dirichlet coefficients and completion. Matching selected time-zero zeros gives no matching heated field. |
| Weighted-square and finite-source/finite-tail controls | The weighted squares fail the conjunction of full reflection and unit coefficients. Genuine finite source changes fail unchanged canonical coefficients. The cited finite-source class also lacks a finite all-real anchor, a condition unused here. |
| Reflected super-Gaussian, smooth shape and primitive-compatible controls | Canonical integer-square theta arithmetic is absent despite the stated shape, exact reflection or positive primitive conditions. |
| Finite-prime orbits and finite-score controls | Full canonical arithmetic/reflection is absent despite the selected-prime or finite-score equalities. Their recorded result grants no fixed event location for applying this particular circle. |
| Atomic and continuous finite-profile threshold controls | Full theta coefficients and full profile are absent despite matched probes; the threshold constructions have their own failures of eventual simplicity. |
| RH-conditional normalized endpoint control | Ordinary Dirichlet-series arithmetic changes and the control retains its RH premise. Its double at zero saturates the exact cost when a counted tube is available. |
| Variable observation kernel and actual-profile measure relaxation | The variable kernel fails the literal cosine/Newman equation. The relaxed measure fails to impose the complete integer zero divisor of a specified analytic field. |

This audit uses existing controls analytically and the explicit
quadratic calculation above. The earlier
[OA Lehmer decision](../../../../investigations-5/08_theta_observables_newman_dynamics/03_operator_imaginary_time_evolution/03_collision_constraints/notes/08_TND_OA_B03_LEHMER_DIRECTION_AND_ACQUISITION_STOP_20261109.md)
records the opposite direction of an upper exterior inverse-square
sum; (1)–(17) use the complete source and a local pair, with neither
exterior sums nor a global real-zero premise. The missing empirical
inputs for the named Lehmer circle are count, all-contour modulus
and buffer, the incoming gap, and the angular and time payments at
the scale required by the signed and direct comparators. Their
acquisition belongs to the fixed diagnostic and any subsequent
certification contract.
