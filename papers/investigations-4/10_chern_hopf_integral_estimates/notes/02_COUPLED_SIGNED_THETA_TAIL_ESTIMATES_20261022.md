# Coupled signed theta-tail estimates and their actual finite comparison

22 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual recorded authoring **gpt-6.1-sol
(Codex), effort ultra**. Delegated same-model checks are internal LLM
checks, not independent specialist review.

**Status: proved in-note; one regular canonical critical point and complete
signed intervals interval-certified.** Coupling stationarity with the value
gives strictly smaller intervals than specified same-moment Taylor bounds.
An additional direct signed tail integral is much sharper in the actual
pilot. This is a useful moment-interface refinement, not the missing
global signed theta estimate or an advantage intrinsic to topological mass.

## 1. Classification and the target that remains unpaid

Read the [result index][results] and [avoid index][avoid], especially
[collision controls][controls], [heat geometry][geometry], [arithmetic
bookkeeping][arithmetic], [target classification][a01], [control
premises][a02], [scope][a07], [known-forced checks][a11] and [joint
cancellation][a12]. The inherited [critical-wall note][wall] defines
the signed consumer

\[
 \sigma(C_2-kC_0)=|V|(q-k),\qquad S_1=0,\quad V=C_0,
 \quad \sigma=\operatorname{sign}V.
\]

The estimates below refine finite acquisition of that consumer. They are
not RH-equivalent reformulations and make no exclusion claim. Their
milestone is the **complete interval width and endpoint gain**, not the
number of moments, digits or sampled critical points. All head and tail
terms belong to the same unchanged source.

There is also a known-forced sign screen. Put

\[
 F=C_2C_4+S_3^2=(H_{zzz})^2-H_{zz}H_{zzzz}.
\]

Whenever the declared all-real regime supplies the inherited
Laguerre–Pólya property, this is the first Laguerre expression for
\(H_{zz}\), hence \(F\ge0\) on the real line. For completeness, real-root
polynomials satisfy \((p')^2-pp''\ge0\) by the logarithmic-derivative
sum; apply this to their second derivatives, then pass to the locally
uniform limit and its derivatives. Merely acquiring this sign in that
regime would not improve the research target. The magnitude or a useful
signed residual still needs additional information. Positive sources
without that all-real premise need not have \(F\ge0\): §6 retains an
ordinary-double control with \(F=-9/25\).

## 2. Exact source split and a one-equation improvement

Keep the canonical source, with its full reflection identity,

\[
 \Phi(u)=\sum_{n\ge1}
  (2\pi^2n^4e^{9u}-3\pi n^2e^{5u})e^{-\pi n^2e^{4u}},
 \quad d\mu_t=e^{tu^2}\Phi(u)\,du.
\]

For \(u\ge0\) every summand is positive. Split into the exact first \(m\)
modes and their complete positive tail \(R_m\); set

\[
 h_j=\int_0^\infty u^j e^{tu^2}\Phi_{\le m}(u)
  \begin{cases}\cos(xu),&j\text{ even},\\\sin(xu),&j\text{ odd},\end{cases}du,
 \qquad M_j=\int_0^\infty u^j e^{tu^2}R_m(u)\,du.
\]

Only \(h_0,h_1,h_2\) are needed below. No reflection identity is assigned
to the head or tail separately. The exact head plus tail is the full
canonical source throughout.

For \(x\ne0\), stationarity gives

\[
 C_2-kV=h_2-\frac{h_1}{x}-kV+
 \int\left[u^2\cos(xu)-\frac u x\sin(xu)\right]d\mu_{R,t}.
 \tag{1}
\]

For every real \(v\), with the continuous value at zero,

\[
 0\le\cos v-\frac{\sin v}{v}+\frac{v^2}{3}
       \le\frac{v^4}{30}.
 \tag{2}
\]

Indeed, for \(v\ge0\),
\(\cos v-\sin v/v=-v^{-1}\int_0^v s\sin s\,ds\), and
\(0\le s-\sin s\le s^3/6\). Evenness completes the proof.
Consequently, writing

\[
 A_1=h_2-h_1/x-kV-x^2M_4/3,\qquad E_1=x^4M_6/30,
\]

we have the **one-sided coupled enclosure**

\[
                    C_2-kV\in[A_1,A_1+E_1].                 \tag{3}
\]

This improves more than the separate tail bound \(\pm M_2\). The same
moments give the stronger uncoupled cosine-Taylor interval

\[
 I_4=h_2-kV+
 [M_2-x^2M_4/2,\ M_2-x^2M_4/2+x^4M_6/24].                 \tag{4}
\]

Equation (3) is strictly inside (4) for \(x\ne0\) and a nonzero positive
tail. To see both endpoint gains, use

\[
 0< S_{1,R}/x-M_2+x^2M_4/6 <x^4M_6/120.
\]

The strict inequalities follow from the global sine remainder and the
positive tail on \(u>0\). The exact-data width ratio is \(4/5\).
Against the coarser \(\pm M_2\), sufficient strict-containment conditions
are \(x^2M_4<4M_2\) and \(x^2M_6<12M_4\); the endpoint gains are at least
\(2M_2-x^2M_4/2\) and \(x^2M_4/2-x^4M_6/24\).

## 3. Simultaneous value and stationarity: a sharper signed enclosure

Use **both** \(C_0=V\) and \(S_1=0\), still with the same exact head/tail.
Define

\[
 g(v)=(v^2-8)\cos v-5v\sin v+8.
\]

The global one-sided inequality is

\[
             v^6/90-v^8/1680\le g(v)\le v^6/90.             \tag{5}
\]

Here \(g(0)=g'(0)=0\) and
\(g''(v)=v\int_0^v r\sin r\,dr\). Integrating twice gives, for \(v\ge0\),

\[
 g(v)=\int_0^v \frac{r(v-r)^2(v+2r)}6\sin r\,dr.
\]

The weight is nonnegative. Substituting
\(r-r^3/6\le\sin r\le r\) proves (5), including its constants;
evenness covers negative \(v\).

Set

\[
 A_2=h_2+\frac8{x^2}(V-h_0-M_0)-\frac{5h_1}{x}-kV
                    +\frac{x^4M_6}{90},\qquad
 E_2=\frac{x^6M_8}{1680}.
\]

Then the complete exact-data statement is

\[
                  \boxed{C_2-kV\in[A_2-E_2,A_2].}          \tag{6}
\]

The counterpart using the **same moments** and cosine alone is

\[
 I_6=h_2-kV+[P_M-x^6M_8/720,\ P_M],\quad
 P_M=M_2-x^2M_4/2+x^4M_6/24.                              \tag{7}
\]

The exact-data width ratio of (6) to (7) is \(3/7\). There is also strict
containment, not just a narrower unrelated interval. Put
\(P(v)=v^2-v^4/2+v^6/24\) and
\(a(v)=8(\cos v-1)+5v\sin v+v^6/90\). Direct integration gives

\[
 P(v)-a(v)=\int_0^v
 \frac{(1-\cos s)(v-s)^4(17v+8s)}{120}\,ds.
\]

For \(v>0\), \(0<P-a<v^8/1260\), by
\(0\le1-\cos s\le s^2/2\) and strictness on a set of positive measure.
After integrating against the tail and dividing by \(x^2\), this gives
both strict endpoint gains of (6) inside (7).

Multiplication by \(\sigma=-1\) reverses the interval; for \(\sigma=1\)
it preserves it. No sign is discarded. The identities hold for any real
\(k\); the common \(-kV\) does not affect exact containment.

## 4. Complete acquisition and endpoint costs

If stationarity is only enclosed as \(S_1=s\), the exact right-hand side
of (3) gains \(s/x\), and that of (6) gains \(5s/x\). Enclose these
terms; do not silently set a measured residual to zero. For the second
estimate, a sufficient input-error allowance at a fixed nonzero \(x\) is

\[
 e_2+\frac{5e_1}{|x|}+\left|\frac8{x^2}-k\right|e_V
 +\frac8{x^2}(e_0+e_{M_0})
 +\frac{x^4}{90}e_{M_6}+\frac{x^6}{1680}e_{M_8}
 +\frac{5e_s}{|x|}.                                     \tag{8}
\]

Here \(e_0,e_1,e_2\) describe head acquisitions, \(e_V\) the shared full
value, and \(e_s\) any separate stationarity residual error. If \(V\) and
the residual are already supplied as balls, their errors must not be
counted again. For a critical-point bracket of radius \(\omega\), use
head variations \(D_1\omega,D_2\omega,D_3\omega\), enclose every rational
coefficient over the bracket, and retain all moment/source errors.
At an exact critical point, full-value variation is at most
\(D_2\omega^2/2\). The implementation uses conservative common complete
moment bounds and outward ball arithmetic for these payments.

These formulas do **not** remove the inherited endpoint cost. If
\(k\sim1/t\), the coefficient of the value error in (8) is still of
order \(1/t\). Preserving an \(O(t)\) amplitude residual still requires
the sufficient value accuracy \(e_V=O(t^2)\). A fixed-cutoff absolute tail
error also does not vanish with \(t\); an endpoint calculation needs a
uniform vanishing allowance or an adaptively increasing cutoff.
Neither the unit logarithmic term nor the square-trace subtraction
\(2r_0/t\) from [Note 06][wall] has been improved.

## 5. Actual canonical finite certificate and the stronger comparator

The [script][script] and [small receipt][receipt] use python-flint 0.9.0,
320-bit Arb/Acb arithmetic, the first three modes as head, modes 4–7 for
tail acquisition on \([0,1]\), and **all** omitted modes and exterior rays.
At \(t=0\), they certify a unique regular real critical point in

\[
 x\in31.171417179658684689191458471044708211406421697860907074476119403575
                    \ \pm10^{-60}.
\]

Existence uses opposite signs of \(S_1\) at the two endpoints; uniqueness
uses \(C_2<0\) on the whole bracket. The critical value lies near
\(-0.00010019534412093423\), so \(\sigma=-1\). No known-zero table or
global RH assumption is used in the certificate.

For \(k=1\), after **all** source, quadrature, wall and rounding errors:

| Enclosure of the same amplitude | Complete interval width |
| --- | ---: |
| Separate tail \(\pm M_2\) | \(3.62491\times10^{-25}\) |
| Cosine Taylor (4), same \(M_2,M_4,M_6\) | \(1.23573\times10^{-27}\) |
| Stationarity-coupled (3) | \(9.88586\times10^{-28}\) |
| Cosine Taylor (7), through \(M_8\) | \(4.44602\times10^{-29}\) |
| Value-and-stationarity coupled (6) | \(1.90544\times10^{-29}\) |
| Additional direct signed tail integral | \(1.26549\times10^{-61}\) |

Both coupled intervals have **strict complete endpoint containment** in
their displayed cosine comparators. The exact ratios \(4/5\) and \(3/7\)
acquire tiny positive error allowances; the receipt records their full
balls rather than asserting those fractions for rounded inputs.
The signed result from (6) is near \(-8.616554377992413\times10^{-5}\).
That sign at this regular point is a finite acquisition, not a new global
theta sign theorem.

The source majorants are explicit. For omitted \(n\ge N\), set
\(\lambda=\pi N^2\), \(b=4\lambda-9\),
\(q=((N+1)/N)^4e^{-\pi(2N+1)}<1\). Concavity gives the complete bound

\[
 \sum_{n\ge N}\int_0^\infty u^j\phi_n(u)\,du
 \le\frac{2\lambda^2e^{-\lambda}j!}{b^{j+1}(1-q)}.
\]

For retained rays \(u\ge1\), use
\(u^j\le e^{j(u-1)}\) and the tangent with positive slope magnitude
\(4\lambda_ne^4-9-j\). The negative source term is retained in every
core acquisition; dropping it is used only in positive error majorants.

**Comparator cost and decision.** Ten scalar integrals acquire the
shared head/value/root and five tail moments; one additional scalar signed
tail integral supplies the last row. Timings in the receipt describe this
small local run and do not establish asymptotic cost. An equally informed
direct method can use (1) or (6) itself. In this pilot it can also directly
integrate the signed tail, gaining more than thirty orders of magnitude
in width. **Stop this finite tail-moment refinement as a candidate for a
win over the acquired direct signed integral.** Keep it as a proved
coupled acquisition interface. This scoped decision does not exclude
other locations, costs, localized mass estimates or arithmetic constraints.

## 6. Collision screens and the remaining research question

The [receipt][receipt] runs a positive atomic ordinary-double control:
at its event the heat-weighted masses at \(u=0,1,2\) are
\(9/10,1,1/10\), and \(x=\pi\). Thus
\(C_0=S_1=S_3=0\), \(C_2=-3/5\), \(C_4=3/5\).
An event at \(T=1/4\) is obtained by multiplying the original masses by
\(e^{-Tu^2}\). Both (3) and (6) contain its actual amplitude; they retain
the collision. It fails the unchanged canonical source and the all-real
premise used for the Laguerre sign screen.

The [cluster-12 screens][controls] are applied analytically, not by
recomputing their published witnesses:

| Family | Universal coupled inequalities | Premise of the actual-theta numerical receipt it fails |
| --- | --- | --- |
| Euler-factor | Pass for its positive source | Unchanged complete theta source and its measured moments |
| Weighted-square | Pass | Unchanged coefficients and full reflection |
| Reflected super-Gaussian | Pass | Canonical integer-square expansion |
| Smooth shape / positive primitive | Pass | Canonical arithmetic expansion |
| Finite-prime orbit | Pass | Full reflection and unchanged coefficients |
| Fixed-event / finite-profile | Pass | Unchanged source and complete profile |
| RH-conditional normalized endpoint | Pass | Unchanged source and ordinary Dirichlet arithmetic |

The inequalities are valid for these controls precisely because they use
positivity and the two matching equations. The particular canonical
numbers are source-specific, but no new property is identified that all
collision controls fail. Therefore this milestone does not upgrade home
02's new-source-constraint task, CHB-05's complete phase/flux acquisition,
ICW's strict signed budget, or any inherited exclusion gate.

The next useful brainstorming question is **what identity or inequality
for the unchanged theta arithmetic controls the complete conditional
quadratic \(C_2C_4+S_3^2\), or a named signed residual, under both
\(C_0=S_1=0\), uniformly as height grows?** It must improve a complete
consumer beyond direct source acquisition, preserve the full remainder,
and not import an unproved pointwise zero separation through a normalized
curvature bound. Fixed finite-prime or finite-prefix identities alone are
already screened by [cluster 12][controls]. Another absolute tail envelope
or a proof of the known Laguerre sign does not pay this step. This is an
open research question, not a proposed new criterion or an established
arithmetic estimate.

[results]: ../../../../result-summaries/README.md
[avoid]: ../../../../avoid/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[geometry]: ../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[arithmetic]: ../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a02]: ../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a11]: ../../../../avoid/11_certifying_the_known_and_tests_that_cannot_fail.md
[a12]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[wall]: ../../notes/06_CRITICAL_WALL_TRACES_AND_SIGNED_ENDPOINT_BUDGET_20261022.md
[script]: ../numerics/certify_coupled_signed_tail.py
[receipt]: ../numerics/COUPLED_SIGNED_TAIL_CERTIFICATE_20261022.json
