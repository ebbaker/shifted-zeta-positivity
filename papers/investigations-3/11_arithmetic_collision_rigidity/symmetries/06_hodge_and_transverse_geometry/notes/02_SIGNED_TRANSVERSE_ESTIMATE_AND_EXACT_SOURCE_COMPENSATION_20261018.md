# Signed transverse estimate and exact source compensation

18 October 2026, America/New_York. Prepared for Edward Baker with substantial
LLM assistance. Actual model **gpt-6.1-sol (Codex)**, reasoning effort
**ultra**, verified from this turn's metadata. Analytic proofs with
192/256-bit outward Arb constant checks and same-model internal review.
No specialist human review.

## Result and comparison contract

Let G1 be the complete base-p observation from [Note 01][opening], and put
K=−iG1. On the closed pilot rectangle
\(\mathcal B=[1/100,1/5]\times[999,1001]\), the new signed estimate is

\[
 \boxed{\frac{37}{100}<x^2K(t,x)<\frac38.}
 \tag{1}
\]

This positive auxiliary observation is too large for a small magnitude
payment by physical energy: fresh complete physical enclosures give

\[
 \boxed{K(t,x)^2>10^{310}E(t,x)\quad((t,x)\in\mathcal B).}
 \tag{2}
\]

An exact source correction removes the transverse reflection anomaly and
produces a convergent signed current. Its physical-energy estimate below
**uses the already established L0>E/100**. It is a paid transfer of that
input, not an independent proof of physical positivity or new coverage.
Finite endpoint corrections to the raw channel fail a polynomial physical
energy payment on an unbounded fixed-time half-line; complete source
compensation escapes that scoped obstruction.

The contract keeps the source, original heat weight, and all lower
endpoints. The primary numerical task was to determine the sign of K and
pay its comparison to E on the existing pilot. A four-derivative absolute
remainder failed; the one bounded repair used six derivatives. There is
no spectral cutoff or moving-cutoff approximation. Eight source modes
are retained, with the entire n>=9 tail bounded analytically on u>=0.
The displayed rational constants are outward roundings of the proved
enclosures, not a fitted asymptotic law.

Interpretation follows the [result summaries][summaries] and
[patterns to avoid][avoid], especially [controls][controls],
[theta bookkeeping][theta-summary], [reformulations][a1],
[certifying existing coverage][a11], [cancellation][a12], and
[scoped exclusions][a7]. Global noncollision remains the existing target.

## Real source and the signed boundary expansion

With q=e^(4u), D=partial_u, and
\(\phi_n=e^u(2v_n^2-3v_n)e^{-v_n}\), \(v_n=\pi n^2q\), define

\[
 g(u)=-i\partial_p\mathcal S(u,0)=\pi\sum_{n\ge1}n^2\phi_n(u),
 \qquad f_t(u)=e^{tu^2}g(u),\qquad
 K(t,x)=\int_0^\infty f_t(u)\cos(xu)\,du.
 \tag{3}
\]

Every fixed derivative of f_t decays doubly exponentially at +infinity,
uniformly on the stated time interval. Repeated integration by parts
therefore retains exactly

\[
 K=-\frac{f_t'(0)}{x^2}+\frac{f_t'''(0)}{x^4}
       -\frac{f_t^{(5)}(0)}{x^6}
       -\frac1{x^6}\int_0^\infty f_t^{(6)}(u)\cos(xu)\,du.
 \tag{4}
\]

No endpoint is discarded: all upper currents vanish by the complete
source decay; the three lower odd derivatives are displayed. In particular
f_t'(0)=g'(0),
\(f_t'''(0)=g'''(0)+6tg'(0)\), and
\(f_t^{(5)}(0)=g^{(5)}(0)+20tg'''(0)+60t^2g'(0)\).

The endpoint constants are evaluated from the complete mode series.
For a separate analytic check, theta reflection gives psi^(2j+1)(0)=−1/2
and yields

\[
 g'(0)=-\tfrac14\Phi''(0)-15\Phi(0)-\tfrac{15}4\psi(0)-\tfrac{15}8,
\]
\[
 g'''(0)=-\tfrac14\Phi^{(4)}(0)-45\Phi''(0)-510\Phi(0)
                         -\tfrac{375}4\psi(0)-\tfrac{375}8.
 \tag{5}
\]

The resulting enclosures include
\(-g'(0)=0.372268390680175755\ldots\) and
\(g'''(0)=-397.322648201412226\ldots\).
In contrast to the even physical source, this raw source has an
uncancelled odd endpoint.

## Explicit all-source remainder payment

Write \(\Phi^{(r)}=e^u\sum P_r(v_n)e^{-v_n}\), where

\[
 P_0(v)=2v^2-3v,\qquad
 P_{r+1}=4vP_r'+(1-4v)P_r.
 \tag{6}
\]

Then \(g^{(r)}=\pi e^u\sum n^2P_r(v_n)e^{-v_n}\).
Let h_j(u,t)=e^(−tu²)D^j e^(tu²). Its recurrence is
\(h_0=1, h_{j+1}=\partial_u h_j+2tu h_j\), with nonnegative
coefficients for t>=0. Hence

\[
 |f_t^{(r)}|\le e^{Tu^2}\pi e^u
 \sum_{k=0}^r\binom rk h_{r-k}(u,T)
 \sum_{n\ge1}n^2\sum_\ell |p_{k,\ell}|v_n^\ell e^{-v_n},
 \quad T=1/5.
 \tag{7}
\]

For lambda=pi*n², use
\(e^{4u}\ge1+4u+8u^2\) to bound the exponential in each monomial by

\[
 e^{-\lambda}\exp\{(4\ell+1-4\lambda)u-(8\lambda-T)u^2\}.
 \tag{8}
\]

Here 8lambda>T for every mode. For n=1 the Gaussian moments are paid
explicitly: with a=4ell+1−4lambda, b=8lambda−T>0,

\[
 I_0=\frac{\sqrt\pi}{2\sqrt b}e^{a^2/(4b)}
       \{1+\operatorname{erf}(a/(2\sqrt b))\},\quad
 I_1=\frac{1+aI_0}{2b},\quad
 I_{j+1}=\frac{jI_{j-1}+aI_j}{2b}.
 \tag{9}
\]

For n>=2 and ell<=8, B=4lambda−4ell−1>0. Dropping the remaining negative
quadratic in (8) gives the simpler moment j!/B^(j+1). The degree bound
ell<=8 covers every derivative through order six.

The entire omitted mode tail starts at m=9. Its successive numerator
ratio is bounded by

\[
 \rho_\ell=(1+1/m)^{2\ell+2}e^{-\pi(2m+1)}<1.
\]

Thus every endpoint tail monomial is bounded by
\(\pi |p_{r,\ell}|m^2(\pi m^2)^\ell e^{-\pi m^2}/(1-\rho_\ell)\).
For an integrated term u^j multiply this bound by j!/B_m^(j+1),
the corresponding heat coefficient, and the binomial coefficient in (7).
These positive bounds prove convergence and pay all omitted modes;
there is no quadrature or finite source-interval truncation in (7)–(9).

Both precision runs give the following conservative upper bounds:

| Quantity | Proved bound |
| --- | ---: |
| L1 norm of f_t^(4) | <577877 |
| L1 norm of f_t^(6) | <1783728354 |
| Magnitude of f_t'''(0) | <398 |
| Magnitude of f_t^(5)(0) | <100000 |
| Order-six integrated omitted-mode allowance | <1.28e−88 |

The four-derivative scaled remainder is about 0.580 and cannot establish
a positive sign. Equation (4) instead gives

\[
 |x^2K+g'(0)|
 \le\frac{|f_t'''(0)|}{999^2}
 +\frac{|f_t^{(5)}(0)|+\|f_t^{(6)}\|_1}{999^4}
 <0.00219.
 \tag{10}
\]

This proves (1) over every point of the closed pilot, rather than only
at sampled heights or times. The [192/256-bit records][numerics] preserve
the complete enclosures, tails and the failed first bound.

## The paid comparison with physical energy

The existing complete [physical contour evaluator][evaluator] was run
fresh at both precisions with its frozen source contour, retained modes
1 through 11 and first omitted mode 12, and all quadrature, source-tail, omitted-mode and
propagation payments. No earlier cached PASS flag supplies an input.
Its fixed normalization is

\[
 G_0=1000^{7/4}e^{-125\pi},\qquad H/G_0\text{ is evaluated},
 \quad G_0<5.047\,10^{-166}.
\]

A complete enclosure over the entire pilot gives
\(E<5.147\,10^{-332}\), while (1) gives
\(K>(37/100)/1001^2\). Their squared comparison proves (2);
the numerical lower quotient is greater than 2.64e318 in both runs.
All comparison quantities use the original physical normalization.

The dominant mismatch is the actual lower-endpoint term, not a failed
tail bound. Increasing arithmetic precision does not remove it. The
positive sign in (1) does not imply physical noncollision.

## Exact compensation and a signed physical current

Put P(D)=(D−1)(D−3)(D−5). Note 01 gives qg=−P(D)psi/32. The exact
factorization
\(P(D)=(D-9)(D^2-1)+24(D-1)\) gives the completed source

\[
 \boxed{C=qg+\tfrac34(D-1)\psi=\tfrac14(9-D)\Phi.}
 \tag{11}
\]

This uses a declared q weight in the transverse observation and a full
primitive correction. It does not identify the original G1 with a
same-point physical jet. The coefficient 3/4 is forced within the class
qg+c(D−1)psi by negative-cusp convergence: the two zero-mode coefficients
there are 3/4 and −c, multiplying e^(−u). This is a convergence completion,
not a positivity assumption. On the complete real line define

\[
 Z(t,x)=\frac12\int_{\mathbb R}e^{tu^2}C(u)e^{ixu}\,du
       =\frac{9H+i(xH-2tH_x)}4.
 \tag{12}
\]

The source combination C must be formed before this full-line integral:
the two terms on the left of (11) diverge separately at the negative cusp.
The observation is a complete cosine/sine pairing; it is not a doubled
half-line cosine of C. In the full-line integration by parts, Phi has
vanishing endpoints at both infinities. This pays the observation map
without suppressing a half-line boundary term.

An explicit norm comparison on the pilot is

\[
 \frac{81}{40083286400}E\le |Z|^2
       \le\frac{12526027}{200}E.
 \tag{13}
\]

For proof, expand
\(16|Z|^2=(81+x^2)H^2-4txHH_x+4t^2H_x^2\).
The associated matrix has trace (81+x²+4t²)/16 and determinant
81t²/64. Its largest eigenvalue is at most its trace; the least is at
least determinant/trace. Substituting the closed pilot bounds gives (13).

The cancellation-preserving signed current is

\[
 J=\operatorname{Im}(\overline Z Z_x)
   =\frac9{16}H^2+\frac{9t}8\mathcal L_0,
 \qquad J_c:=J-\frac9{16}H^2=\frac{9t}8\mathcal L_0.
 \tag{14}
\]

Fresh evaluation on a fixed four-by-sixteen closed cover rechecks the
**inherited** premise L0>E/100, with all physical errors paid. Combining
it with (14) proves the requested bounded signed transfer estimate

\[
 \boxed{J_c>\frac{9t}{800}E\ge\frac9{80000}E.}
 \tag{15}
\]

In particular J>9E/80000 and, using (13),
\(\partial_x\arg Z=J/|Z|^2>9/5010410800>1.79\,10^{-9}\).
The division is legitimate on the pilot because the physical input already
establishes E>0. The undivided current identity remains defined at collisions.
The lowest certified normalized excess for (15), after removing its
right-hand side, exceeds 1.0027e−6 on the fixed cover in both runs.

The constant in (15) is a genuine paid signed estimate for this completed
observation, but its entire sign input is the existing physical certificate.
Equation (14) also holds for heat-polynomial controls and can give negative
J. It does not create a new arithmetic inequality. No additional physical
region, smaller complete approximation error or evaluation-cost gain follows.

## Finite endpoint subtraction and collision controls

For the raw source the exact reflection anomaly is

\[
 g(-u)=\frac{e^{4u}}{32}(D^3+9D^2+23D+15)\psi(u)
             +\frac34e^{5u}.
 \tag{16}
\]

Thus g(−u)~3e^(5u)/4, while g(u) decays doubly exponentially. The identity
follows by writing g=−q^(−1)P(D)T0/64 and using evenness of T0. For fixed
t>=0, the odd part of f_t has infinitely many nonzero Taylor coefficients
at zero. Otherwise its real-analytic odd part would be a finite polynomial
on the real line, contradicting (16). Repeated integration by parts gives
the full inverse-even-power expansion of K. Subtracting any finite sum of
inverse even powers therefore leaves a first unmatched algebraic term.
Since H and H_x are Schwartz for fixed t, the remainder cannot obey
\(|R|^2\le P(x)E\) eventually on an unbounded half-line for any polynomial
P. This excludes fixed finite endpoint subtractions and magnitude payments.
It does not exclude high-order subtraction on a bounded pilot, a one-sided
lower bound, or the full source compensation (11).

The collision controls sharpen this distinction. For a finite positive
weighted-square source, at an event H_a=H_(a,x)=0,

\[
 K_a=\pi\sum_{n\ge2}(n^2-1)a_nH_n>0
\]

when some n>=2 coefficient is positive. The strict inequality uses the
already proved [positive arithmetic mode transforms][packets] for
0<=t<=1/2. The three- and four-square event controls have these properties.
Thus strict positivity of the raw auxiliary channel can coexist with a
physical collision. These controls fail full canonical theta coefficients
and reflection, while retaining the local transverse algebra.

The centered-current acceptance test in (15) is exactly 9t/8 times the
old strict Laguerre test. Fresh source-specific replay rejects the five
event boxes and the separate Euler negative-Laguerre witness at that
interface. This does not assert that the weaker uncentered-current sign
rejects the Euler witness. A direct polynomial witness gives J=−9/64 for
H=x²−2(t−1/2) at (t,x)=(1/4,0); a polynomial double event gives Z=J=0.
Generic current geometry therefore supplies no favorable sign by itself.

For a coupled source implementation, (11) must be used in each variable
before estimating. Expanding the completed product retains both cross
terms and both diagonal terms. The raw diagonal product K² is precisely
at the wrong scale in (2). The primitive lower edges and energy corner
from the original signed bridge remain part of any half-line product map.

## Decision

The raw signed estimate and its physical-scale mismatch are established.
The exact source completion gives a paid current estimate on the pilot,
conditional on its already certified physical margin. It closes the
observation-map and boundary bookkeeping for this compensation class; it
does not close the missing independent signed arithmetic estimate.

A further S06 step must control a recombined source remainder in (11),
or a coupled analogue, without importing the physical sign it is meant
to establish. Fixed-order endpoint subtraction and independent absolute
payments for the raw channel have now been screened out in their stated
classes. The unbounded real bridge and complex-exterior problem remain open.
See the [internal review][review] for scope and replay provenance.

[opening]: 01_TRANSVERSE_OBSERVATION_AND_FINITE_JET_OBSTRUCTIONS_20261018.md
[summaries]: ../../../../../../result-summaries/README.md
[avoid]: ../../../../../../avoid/README.md
[controls]: ../../../../../../result-summaries/12_collision_controls_and_screening.md
[theta-summary]: ../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[a1]: ../../../../../../avoid/01_restating_the_target.md
[a7]: ../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a11]: ../../../../../../avoid/11_certifying_the_known_and_tests_that_cannot_fail.md
[a12]: ../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[numerics]: ../numerics/README.md
[evaluator]: ../../../numerics/high_height_consumer/high_height_consumer.py
[packets]: ../../../notes/04_POSITIVE_ARITHMETIC_PACKETS_AND_MODULAR_CANCELLATION_CODEX_20261018.md
[review]: ../reviews/02_SIGNED_TRANSVERSE_ESTIMATE_INTERNAL_REVIEW_20261018.md
