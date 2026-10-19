# S01 opening result: pair the nonstationary endpoints before estimating

18 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. **GPT-6.1 Sol (`gpt-6.1-sol`), actual reasoning
effort ultra**, verified from the parent turn metadata. Derivation and
parallel adversarial checks are internal same-model review; no independent
specialist review is claimed.

**Result.** A signed endpoint in the existing complete shifted arithmetic
remainder can be combined across the reflected contours and across source
monomials before taking its absolute value. This gives a smaller bound for
the same omitted-mode remainder, including its first and second spectral
derivatives on a fixed complex neighborhood. On the inherited height-1000
rectangle, it also strictly reduces the complete added approximation error
of the same retained polynomial. It does not give a sign or a lower bound
for the retained field, new collision-free coverage, or a Newman bound.

The [program guide][guide] and [S01 contract][s01] define this bounded first
task. The [result-summary index][summaries] and [avoid index][avoid] govern
classification: see [theta bookkeeping][theta-summary], [controls][controls],
[target reformulations][target], [scoped negative results][scope], and
[preserving cancellations][cancel]. This is an approximation-error milestone,
not a reformulation or proof of global noncollision.

## 1. Declared comparison and relation to prior work

Use the complete theta source and heat normalization

\[
 H(t,z)=\int_0^\infty e^{tu^2}\Phi(u)\cos(zu)\,du,
 \qquad H_t=-H_{zz}.
\]

The [complete-contour theorem][shifted] already shifts the full even source
before truncating its integer-square series. The [nonstationary theorem][effective]
already integrates each omitted monomial by parts and pays its endpoint
and remaining integral separately. Those results, the full endpoint
cancellation, and coefficient rigidity are inherited; they are not earned
again here. The new step is to retain the signed *paired endpoint* of that
integration by parts. The remaining integral still receives the inherited
absolute payment.

The primary objective is a **strict decrease of the complete added error**
for physical value and first derivative, with second derivative also paid.
No speed objective or larger exclusion region is claimed. Freeze the exact
parameters of the [existing evaluator][evaluator]:

\[
 \begin{gathered}
 1/100\le t\le1/5,\quad 999\le\Re z\le1001,\quad|\Im z|\le1,\\
 d=\pi/8-4\log(1000)/1000,\quad m=12,\quad U=2.
 \end{gathered} \tag{1}
\]

Retain modes 1 through 11. For a complete numerical comparison, retain the
same source cutoff, midpoint `(21/200,1000)`, spatial degree 24, time degree
12, all 51 midpoint jets and all quadrature and propagation rules. The
normalization is the fixed positive constant

\[
 G_c=\mathcal G_0(1000)=1000^{7/4}e^{-125\pi}.
\]

Every reported normalized component is `physical derivative / G_c`.
The constant is never differentiated and is not a lower bound for the
field. We also inspected the already declared constant-distance contour
with parameter 33; it is not the primary comparison because (1) matches the
existing complete evaluator exactly. No parameter or height scan was run.

## 2. Exact complete pair and boundary terms

Put `w_t(v)=exp(tv^2) Phi(v)`, `lambda_n=pi n^2`, and

\[
 \phi_n(v)=2\lambda_n^2e^{9v-\lambda_ne^{4v}}
                  -3\lambda_ne^{5v-\lambda_ne^{4v}}.
\]

Full source reflection gives, for complex z,

\[
 H(t,z)=\frac{e^{-dz}}2\int_0^\infty
 \{w_t(u+id)e^{izu}+w_t(u-id)e^{-izu}\}\,du. \tag{2}
\]

Let `Htilde_{m,d}` replace Phi in (2) by `sum_{n<m} phi_n`, and set
`R=H-Htilde_{m,d}`. This keeps the spectral phase, physical heat weight,
and both shifted contributions. The complete reflection is used before
truncation; no evenness is asserted for the finite source or Htilde.

For completeness, an analytic half-line source w with sufficient contour
decay obeys the more general identity

\[
 \int_0^\infty w(u)\cos(zu)\,du
 =P_d[w](z)+\frac i2\int_0^d
        [w(iv)-w(-iv)]e^{-zv}\,dv, \tag{3}
\]

where `P_d[w]` is the paired right side of (2). The two remote vertical
boundaries vanish by the double-exponential decay for the complete theta
source; its remaining vertical segment in (3) vanishes by analytic
reflection. Individual modes and finite-prime perturbations generally
retain that segment. Differentiating it j times inserts `(-v)^j`.
These facts are essential to the source-specific scope of (2).

No further boundary is dropped in the calculation below. Its source
infinity boundary vanishes, while its source-zero boundary is the signed
term that improves the estimate.

## 3. Paired-endpoint theorem

Let `0<d<pi/8`, `0<=t<=T`, `z=x+iy`, `x>=0`, `|y|<=Y`, and put

\[
 \begin{gathered}
 c=\cos4d,\qquad s_d=\sin4d,\qquad
 B=4c\lambda_m-9-Y,\\
 p_n=4s_d\lambda_n-x-2td,\qquad
 Q_j=\sum_{k=0}^j\binom jk\frac{d^{j-k}k!}{B^k}.
 \end{gathered}
\]

Assume `B>0`, `8c lambda_m>=T`, and `p_m>0`. Define the absolutely
convergent sums

\[
 \begin{aligned}
 A_n&=2\lambda_n^2+3\lambda_n,\\
 C_n&=2\lambda_n^2\sin(9d-s_d\lambda_n)
             -3\lambda_n\sin(5d-s_d\lambda_n),\\
 \mathfrak A(t,x)&=\sum_{n\ge m}\frac{A_ne^{-c\lambda_n}}{p_n},\qquad
 \mathfrak C(t,x)=\sum_{n\ge m}\frac{C_ne^{-c\lambda_n}}{p_n}.
 \end{aligned}
\]

For every fixed integer `j>=0`,

\[
 \boxed{
 |\partial_z^jR(t,z)|\le e^{-dx-td^2}
 \{d^j|\mathfrak C|+(2Q_j-d^j)\mathfrak A\}.}
 \tag{4}
\]

The matched unpaired estimate, retaining the same monomial denominators
and heat damping, is

\[
 |\partial_z^jR|\le e^{-dx-td^2}2Q_j\mathfrak A. \tag{5}
\]

Thus the certified saving from pairing itself is
`exp(-dx-td^2) d^j (Afrak-|Cfrak|)`. Heat damping and retaining individual
denominators are not credited as pairing gains. The manuscript's existing
`2 S Q_j / P` bound follows by additionally replacing all denominators by
the smallest one and dropping heat damping.

**Proof.** Separate the two monomials with `r=9,5`, carrying coefficients
`2 lambda_n^2,-3 lambda_n`. After taking the jth spectral derivative
directly in (2), factor out `exp(-dz-td^2)`. The two half-integrands are

\[
 \frac12\{g_+(u)q_+(u)e^{i\theta(u)}
                    +g_-(u)q_-(u)e^{-i\theta(u)}\},
\]

where

\[
 \begin{aligned}
 g_\pm(u)&=\exp\{tu^2+(r\mp y)u-c\lambda_ne^{4u}\},\\
 q_\pm(u)&=(-d\pm iu)^j,\\
 \theta(u)&=rd-s_d\lambda_ne^{4u}+(x+2td)u,\\
 p(u)&=-\theta'(u)=4s_d\lambda_ne^{4u}-x-2td.
 \end{aligned}
\]

The assumptions give `p>0`, `p'>0`, `g'<=0`, `(log g)''<=0` and
`g(u)<=g(0) exp(-Bu)` for each half. The derivatives of the phase
exponentials are `-ip exp(i theta)` and `+ip exp(-i theta)`.
Integration by parts therefore gives the exact paired endpoint

\[
 (-d)^j\frac{e^{-c\lambda_n}\sin(rd-s_d\lambda_n)}{p_n}. \tag{6}
\]

Both endpoint amplitudes and both derivative factors agree at zero.
Consequently (6) holds off the real axis as well; it does not use an
invalid off-axis conjugation or real-part replacement.

For either remaining integral,

\[
 \left|\left(\frac{gq}{p}\right)'\right|
 \le-\left(\frac{g(u+d)^j}{p}\right)'
             +\frac{2jg(u+d)^{j-1}}p.
\]

The remote boundary is zero. Integration and the exponential amplitude
majorant bound this remainder by

\[
 \frac{e^{-c\lambda_n}}{p_n}
 \left[d^j+2j\int_0^\infty(u+d)^{j-1}e^{-Bu}\,du\right]
 =\frac{e^{-c\lambda_n}}{p_n}(2Q_j-d^j).
\]

For j=0 the integral containing j is absent. Sum the endpoints (6) with
their original monomial signs and mode weights, then take one absolute
value. Bound the remainders by A_n. The original factor 1/2 pays for the
two halves exactly. This proves (4). The source-strip majorants already
proved in the manuscript justify the sums, differentiations and limits.

The denominators p_n appear only in a pointwise estimate **after** spectral
differentiation. Differentiating (6) alone would leave additional terms
unpaid; no such differentiation is used here.

As a non-numerical check, with `a=2 lambda_n^2`, `b=3 lambda_n`,

\[
 |C_n|\le\sqrt{a^2+b^2-2ab\cos4d}<a+b.
\]

This gives a strict endpoint saving in the named nonstationary
representation. It does not imply a uniform factor bounded away from one
for every parameter choice, nor a lower bound for R or H.

## 4. Infinite summation and uniform analytic-neighborhood estimate

To enclose (4) on (1), use interval denominators for the signed endpoint
sum and the minimum denominators for the positive remainder mass. Sum
the signed endpoints for `12<=n<24`. For n>=M=24 put

\[
 p_n^*=4\pi s_dn^2-1001-2Td,\qquad
 \rho_M=\left(\frac{M+1}{M}\right)^2e^{-c\pi(2M+1)}.
\]

The positive tail of Afrak, and the absolute tail of Cfrak, are at most

\[
 \frac{A_Me^{-c\lambda_M}}{p_M^*(1-\rho_M)}. \tag{7}
\]

Indeed `A_n/p_n^*=(2 pi^2 n^2+3 pi)/(4 pi s_d-(1001+2Td)/n^2)`;
the denominator increases and the numerator's successive ratio is bounded
by `((n+1)/n)^2`. This proves (7) for the full infinite series.

Outward Arb/Acb arithmetic checks (1), its phase gap, and (7) at 192 and
256 bits. With Y=1, `B>189.59` and `p_m>797.37`. The interval endpoint
enclosure obeys

\[
 |\mathfrak C|\le\frac{29}{125}\,\overline{\mathfrak A}, \tag{8}
\]

where Abar is the common uniform positive-mass upper bound. The raw
ratio of the endpoint upper bound to Abar is below 0.231014. We round it
up to 29/125 before the comparison; independent finite-precision endpoint
upper bounds need not be identical numbers. Using this same rational
allowance makes the compared tail expressions enclosures of the same
scalar formulas at both precisions.

The [small record][record] preserves every finite endpoint, infinite tail,
normalization factor, admissibility bound and derivative comparison.
The table gives approximate new/old ratios using the **stronger matched
unpaired bound (5)**, including the common heat damping:

| Derivative order | Y=0 | Y=1 |
| --- | ---: | ---: |
| 0 | 0.616000 | 0.616000 |
| 1 | 0.621441 | 0.621469 |
| 2 | 0.626879 | 0.626936 |

These enclose physical derivatives, not derivatives of a varying contour
rule or varying cutoff. The fixed parameters also apply at any natural
Riemann–Siegel cutoff crossing inside the domain; that jumping cutoff is
not part of this representation. The domain here is not a new coverage
claim for a separate transition experiment.

## 5. Complete-error comparison

The [checker][code] freshly constructs the existing evaluator at 192 bits.
It retains its exact midpoint polynomial, quadrature radii, subsequent
outward image arithmetic, retained-source tail and whole-box Taylor
payment. Only the omitted-mode bound is replaced. The comparison is
uniform on the entire closed real rectangle in (1), not just at its
center. Its two sides enclose the same physical derivatives in the same
fixed normalization.

| Order | Existing complete added error / G_c | New complete added error / G_c | New/old |
| --- | ---: | ---: | ---: |
| 0 | 4.620515e-12 | 3.934535e-12 | 0.851536 |
| 1 | 3.469201e-12 | 3.218759e-12 | 0.927810 |
| 2 | 3.055846e-12 | 2.964413e-12 | 0.970080 |

Displayed bounds are rounded upward; ratios are rounded upward to the
shown digits. The mode payments change respectively from about
`(1.78241e-12,6.60052e-13,2.44476e-13)` to
`(1.09643e-12,4.09609e-13,1.53043e-13)`. The common whole-box Taylor
payment is about `2.16484e-12`; quadrature with internal rounding costs
about `6.44e-13` to `6.74e-13` per component. Source tails are below
`1.2e-435`. The exact interval values, including each separate payment,
are in the record. The shared polynomial image enclosure contains its
subsequent arithmetic rounding; the added error is not the radius of that
whole-cell image.

The complex neighborhood has the complete analytic mode-error bounds
in Section 4. The numerical complete-polynomial comparison in this table
is on the real rectangle; a new complex wall evaluation is not claimed.

An independent fresh complete comparison at 256 bits is stored in the
[replay record][replay]. It repeats quadrature rather than accepting a
saved PASS label. Each precision has its own unchanged common costs on
the two compared sides. No between-precision timing or error equality
is asserted.

This satisfies the declared strict complete-error gate. It is a bounded
improvement in the inherited evaluator, with no claim of a factor-two
performance milestone or improved all-height asymptotic exponent.

## 6. Controls, scope and next decision

The checker verifies (3) through two spectral derivatives for the explicit
non-even analytic source `w(u)=exp(-u)`, at `d=1/4` and `z=2+i/2`.
Here

\[
 P_d[w](z)=\frac{e^{-dz}(\cos d+z\sin d)}{1+z^2},\qquad
 B_d(z)=\int_0^d\sin v\,e^{-zv}\,dv.
\]

The full identity is enclosed; dropping the vertical term is rejected.
Five inadmissible parameter choices are rejected separately: zero shift,
the source-strip edge, a stationary omitted mode, excessive spectral
height, and excessive imaginary width. These are interface and domain
checks, not evidence for the analytic theorem by themselves.

The [fresh source-specific control replay][control-record] rejects all five
surrounding event boxes at both strict first-jet and signed-margin
interfaces, and separately rejects the Euler negative-Laguerre witness.
It retains their own source errors; theta tail constants are never
substituted for control constants. These replays check the downstream
acceptance interface, not the new theorem's proof.

| Family | Premise absent from this theta application |
| --- | --- |
| Finite-prime and finite weighted-square sources | Complete normalized analytic reflection; their vertical term must be retained |
| Reflected super-Gaussian and smooth positive-primitive controls | The unchanged normalized theta integer-square expansion and the coefficients used in (4) |
| Euler-factor controls | The unchanged level-one coefficients and source decomposition; the witness is not a double-event box |
| Generic heat counter-kernels and polynomial events | The exact theta source and its evaluated remainder constants |
| Smooth-density and two-channel controls | A justified comparison to the complete signed physical observation |

The finite-prime events have no effective supplied height and the smooth
primitive construction has no certified damping/event box here. Their
screens remain analytic premise checks. Generic reflected sources can
share endpoint pairing; that identity alone cannot exclude their events.
Full reflection plus square-coefficient rigidity selects theta in its
stated coefficient class, but supplies no quantitative signed lower bound.

**Next decision:** carry (4) and the endpoint summation into S02/S03 as a
smaller fixed-contour error payment. Recompute complete errors on any new
domain rather than reusing the 29/125 allowance. For an estimate of the
retained oscillatory sum, a new correlation or stationary-phase argument
is still needed: the low modes with `n^2<x/(4pi)` fail the phase-gap
premise of this tail theorem. Do not expand a height scan on the strength
of the present gain. The existing real gap
`1001<|x|<exp(2000), 1/100<=t<=1/5` remains open, as does the missing
complex exterior for the conditional global consumer.

[guide]: ../../../research-overview/03_SYMMETRY_RESEARCH_PROGRAM_AND_INVESTIGATION_GUIDE_20261018.md
[s01]: ../README.md
[summaries]: ../../../../../../result-summaries/README.md
[avoid]: ../../../../../../avoid/README.md
[theta-summary]: ../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[controls]: ../../../../../../result-summaries/12_collision_controls_and_screening.md
[target]: ../../../../../../avoid/01_restating_the_target.md
[scope]: ../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[cancel]: ../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[shifted]: ../../../manuscript/positive_arithmetic_packets/sections/07_shifted_approximation.tex
[effective]: ../../../manuscript/positive_arithmetic_packets/sections/08_effective_tails.tex
[evaluator]: ../../../numerics/high_height_consumer/high_height_consumer.py
[code]: ../numerics/check_paired_modular_tail.py
[record]: ../numerics/PAIRED_MODULAR_TAIL_20261018.json
[replay]: ../numerics/PAIRED_MODULAR_TAIL_REPLAY_256_20261018.json
[control-record]: ../numerics/S01_MODULAR_CONTROLS_20261018.json
