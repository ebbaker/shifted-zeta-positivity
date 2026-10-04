# A finite signed Möbius target for Gaussian zero detection

4 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration. The exact serving variant and
configured reasoning effort are not exposed and are not inferred.
Parallel same-model analysis and cross-review are internal checks, not
independent specialist refereeing.

Status: proved arithmetic identities, effective removal of small divisors,
effective product and frequency tails, and a sufficient finite arithmetic
criterion for the saved zero detector. The remaining signed cancellation
inequality is unproved. No actual large prime computation, numerical zero
certificate, or new zero-free region is claimed. Mathematical priority
has not been established.

The next arithmetic investigation produces a more focused interface than
the continuous supremum in the
[explicit-constants note](EXPLICIT_CONSTANTS_AND_FINITE_WINDOW_20261004.md).
One can work directly with the Gaussian prime observable, remove all
Möbius divisors up to \(e^{15k}\) at an explicit small error, and retain
one finite signed sum with

\[
\boxed{d>e^{15k},\qquad dr\le e^{26k},\qquad r<e^{11k}.}
\tag{1}
\]

The exact continuum coefficient is retained. Each deleted range fits
the detector allowance without assuming Möbius cancellation. A separate
[height-uniform Vaughan comparison](HEIGHT_UNIFORM_VAUGHAN_REDUCTION_20261004.md)
also makes the original supremum route's derivative and cutoff costs
effective. These reductions locate the missing estimate; they do not
prove it.

## The full Gaussian observable and the spectral input

Fix \(b=3/4\), \(T=|t|\ge100\), and
\(g_k(v)=e^{-v^2/(4k)}/\sqrt{4\pi k}\).
Use \(\mu_G=20k\) for the Gaussian center, reserving \(\mu(d)\) for
the arithmetic Möbius function. Put

\[
W_{k,t}(x)=x^{-b-it}g_k(20k-\log x),\qquad x>0,
\]
\[
\mathcal I_{k,t}=\sum_{n\ge2}\Lambda(n)W_{k,t}(n),\qquad
\Phi_{k,t}(1)=\int_0^\infty W_{k,t}(x)\,dx
=e^{k(1-b-it)^2+20k(1-b-it)}.
\tag{2}
\]

The zero extension of \(W\) is a Schwartz function, flat at zero.
Every derivative is a polynomial in \(\log x\) times a fixed power of
\(x\) times the logarithmic Gaussian, so all endpoint terms vanish.
The sums and integral in (2) converge absolutely. The opening
[Gaussian identity](INITIAL_INVESTIGATION_20261004.md) gives

\[
\mathcal I_{k,t}-\Phi_{k,t}(1)
=-\mathcal Z_{k,t}+\mathcal R_{-1},\qquad
\mathcal Z_{k,t}=\sum_\rho m_\rho
 e^{k(\rho-b-it)^2+20k(\rho-b-it)}.
\tag{3}
\]

The contour is shifted only to the fixed line \(\Re s=-1\), retaining
its remainder; no divergent infinite trivial-zero Gaussian sum is used.

Let \(\mathcal Q(T)\) be the explicit closed radius-three zero-count
expression in the preceding note. Choose an integer

\[
N\ge\max(10,\lceil\mathcal Q(T)\rceil),\quad
\eta_N=(8e)^{-N},\quad k=4(N+1),4(N+2),\ldots,8N.
\tag{4}
\]

Then \(T+1<e^N\), and \(|\mathcal R_{-1}|<\eta_N/16\)
for every sample. If a zero has \(\beta_*\ge3/4\) and ordinate
\(t\), the proved power-sum argument forces
\(|\mathcal Z_{k,t}|\ge\eta_N/2\) at one of these samples.
No zero separation or simple-zero hypothesis is required.

## Effective removal of the small Möbius divisors

The elementary identity \(\Lambda=-(\mu\log)*1\) yields exactly

\[
\mathcal I_{k,t}=-\sum_{d\ge1}\mu(d)\log d
                           \sum_{r\ge1}W_{k,t}(dr).
\tag{5}
\]

Absolute convergence follows by grouping products and using
\(\sum_{d\mid n}\log d=\tau(n)\log n/2\); the Gaussian beats
every polynomial growth. All prime powers remain in (5).

Order-two Poisson summation gives, for every \(d>0\),

\[
\left|\sum_{r\ge1}W_{k,t}(dr)-\frac{\Phi_{k,t}(1)}d\right|
\le\frac d{12}\|W_{k,t}''\|_1.
\tag{6}
\]

With Fourier convention \(e^{-2\pi i\xi x}\), the coefficient is
exactly \(2\zeta(2)/(2\pi)^2=1/12\). There are no zero or negative
lattice samples because of the flat zero extension.

The derivative norm is exceptionally small. Write
\(q(y)=-b-it+(20k-y)/(2k)\). Then

\[
W''(x)=x^{-2}W(x)[q(\log x)^2-q(\log x)-1/(2k)].
\]

In its absolute integral, the positive measure
\(e^{-(b+1)y}g_k(20k-y)\,dy\) has total mass
\(e^{-511k/16}\). Under the normalized measure the real part of
\(q\) has mean one and variance \(a=1/(2k)\). Gaussian moments give

\[
\mathbb E|q^2-q-a|^2
=T^4+(1+2/k)T^2+1/(2k)+1/(2k^2)
\le(T^2+1)^2\quad(k\ge2).
\]

Cauchy--Schwarz therefore proves the fully effective bound

\[
\boxed{\|W_{k,t}''\|_1\le(T^2+1)e^{-511k/16}
                                  \le(T+1)^2e^{-511k/16}.}
\tag{7}
\]

Set \(D_k=e^{15k}\) and
\(L_{D_k}=\sum_{d\le D_k}\mu(d)\log d/d\).
Combining (5)--(7), with
\(\sum_{d\le D_k}d\log d\le D_k^2\log D_k\), gives

\[
\mathcal I_{k,t}-\Phi_{k,t}(1)
=-\sum_{d>D_k,r\ge1}\mu(d)\log d\,W_{k,t}(dr)
 -\Phi_{k,t}(1)(1+L_{D_k})+R_{\rm low},
\tag{8}
\]

\[
|R_{\rm low}|\le E_{\rm low}
:=\frac{5k}{4}(T+1)^2e^{-31k/16}.
\tag{9}
\]

The finite logarithmic continuum is subtracted with sign minus and
coefficient \(1+L_{D_k}\). Preparation does not justify deleting it,
and no infinite unweighted Möbius sum is inserted. Equation (9) uses
only \(|\mu(d)|\le1\); it is an unconditional saving for a specified
sector of the actual arithmetic identity.

## A finite product cap with every divisor coefficient paid for

Put \(B_k=e^{26k}\). The finite signed target is

\[
\boxed{\mathcal G_{k,t}:=
-\sum_{\substack{d>D_k,\ r\ge1\\dr\le B_k}}
      \mu(d)\log d\,(dr)^{-3/4-it}g_k(20k-\log(dr))
-\Phi_{k,t}(1)(1+L_{D_k}).}
\tag{10}
\]

Every retained product already exceeds \(D_k\), so no lower product
tail is discarded. Both the strict divisor cutoff and weak product cap
are literal. Equivalently the pair sum is

\[
-\sum_{1\le r\le\lfloor B_k/D_k\rfloor}
\sum_{D_k<d\le B_k/r}\mu(d)\log d\,W_{k,t}(dr).
\]

The innermost cap \(B_k/r\) must stay; replacing it by a rectangular
factor interval changes the target. The cofactor inequality is strictly
\(r<B_k/D_k=e^{11k}\) for every active pair.

Write \(a_D(n)=\sum_{d\mid n,d>D}\mu(d)\log d\). Its absolute
cumulative coefficients satisfy, for real \(x\ge1\),

\[
\sum_{n\le x}|a_D(n)|
\le\frac{\log x}{2}\sum_{n\le x}\tau(n)
\le\frac{x\log x(1+\log x)}2.
\tag{11}
\]

This is a divisor bound, rather than a prime-only tail estimate.
For \(x\ge B_k\), \(w(x)=|W_{k,t}(x)|\) decreases. Stieltjes
integration gives the exact strict upper-tail boundary term
\(-w(B_k)\sum_{n\le B_k}|a_D(n)|\), which can be dropped for an
upper bound, leaving the integral of (11) against \(-w'\).

At \(\log x=26k+u\), its exponential and derivative factors are

\[
e^{-5k/2-11u/4-u^2/(4k)},\qquad 15/4+u/(2k).
\]

Dropping only the final negative square and integrating the remaining
polynomial proves

\[
\sum_{n>B_k}|a_{D_k}(n)|\,|W_{k,t}(n)|
\le\frac{e^{-5k/2}}{4\sqrt{\pi k}}P(k)
\le250k^{3/2}e^{-5k/2}=:E_{\rm high},
\tag{12}
\]

where

\[
P(k)=\frac{10140}{11}k^2+\frac{12818}{121}k
                       +\frac{6756}{1331}+\frac{1472}{14641k}.
\]

Indeed \(P(k)\) is the integral of
\((26k+u)(1+26k+u)(15/4+u/(2k))e^{-11u/4}\) for \(u\ge0\).
All coefficients of \(P(k)/k^2\) are positive and its nonconstant
terms decrease. At \(k=8\),
\(P(8)/8^2=219062021/234256<1000\).
Thus (8)--(12) give

\[
\boxed{|(\mathcal I_{k,t}-\Phi_{k,t}(1))-\mathcal G_{k,t}|
                                      \le E_{\rm low}+E_{\rm high}.}
\tag{13}
\]

The omitted sector contains divisor coefficients and has been bounded
with their full cost. Small-divisor and product deletions cannot create
cancellation in the remaining signed sum.

## An optional finite relative-frequency form

For the exact cap in (10), define the finite Dirichlet polynomial

\[
H_k(s)=\sum_{\substack{d>D_k,\ r\ge1\\dr\le B_k}}
                                \mu(d)\log d\,(dr)^{-s},
\]

and the band-limited arithmetic functional

\[
\mathcal G_{k,t}^{[3]}=
-\frac1{2\pi}\int_{-3}^3 e^{-k\nu^2+i20k\nu}
               H_k(3/4+i(t+\nu))\,d\nu
-\Phi_{k,t}(1)(1+L_{D_k}).
\tag{14}
\]

The full Fourier integral reproduces (10). The coefficient bound (11)
and partial summation give

\[
\sum_{n\le B_k}|a_{D_k}(n)|n^{-3/4}
\le2B_k^{1/4}\log B_k(1+\log B_k).
\]

Since the absolute Fourier Gaussian mass outside \([-3,3]\) is at
most \(e^{-9k}/(6\pi k)\),

\[
|\mathcal G_{k,t}-\mathcal G_{k,t}^{[3]}|
\le\frac{26}{3\pi}(1+26k)e^{-5k/2}
\le80k e^{-5k/2}=:E_{\rm freq}\quad(k\ge8).
\tag{15}
\]

This pays the entire frequency tail. The compact integration band is
continuous; finitely many frequencies would require another enclosure.
The continuum term in (14) remains the full explicit coefficient in (10).

## One explicit sufficient arithmetic inequality

For every \(N\ge10\) and every sample in (4),

\[
E_{\rm low}<\eta_N/16,\qquad
E_{\rm high}<\eta_N/16,\qquad
E_{\rm freq}<\eta_N/16.
\tag{16}
\]

These are analytic all-sample bounds. For the first, use \(T+1<e^N\),
\(\log(8e)<31/10\), and monotonicity in \(k\). At the least sample,

\[
E_{\rm low}/\eta_N
\le5(N+1)e^{-53N/20-31/4}<1/16.
\]

This decreases in \(N\); the base \(N=10\) is
\(55e^{-137/4}<1/16\). For the other two use
\(k^{3/2}\le e^k\) and \(k\le e^k\), obtaining
\(250e^{-29N/10-6}\) and \(80e^{-29N/10-6}\), respectively.
Each is below \(1/16\) at \(N=10\) and decreases thereafter.

For a candidate box \(3/4\le\beta<1\),
\(|\gamma-t_0|\le\Delta\), all carriers must be covered, with
\(|t|\ge100\). Choose a single \(N\) satisfying (4) uniformly, using
\(T_{\max}=\max(|t_0-\Delta|,|t_0+\Delta|)\).
The entirely finite arithmetic hypothesis

\[
\boxed{|\mathcal G_{k,t}|\le\eta_N/4
\quad\text{for every covered carrier and every sample in (4)}}
\tag{17}
\]

would exclude the box: (3), (13), and the fixed-line bound give
\(|\mathcal Z_{k,t}|<7\eta_N/16<\eta_N/2\) for every sample,
contradicting the spectral detector at a hypothetical zero's own carrier.
Alternatively \(|\mathcal G_{k,t}^{[3]}|\le\eta_N/4\), together with
(15), gives the strict upper bound \(|\mathcal Z_{k,t}|<\eta_N/2\).
The strictness comes from each omitted-error allowance.

Thus the new arithmetic obligation is one signed finite Gaussian sum
per sample and carrier. A continuous supremum of the unfiltered prepared
scalar and its inverse norm are not required for this criterion.
Neither inequality follows from the reductions above. The complex
modulus is essential; the fixed real probe's one-sided Landau argument
cannot be applied to one arbitrarily selected real component.

The continuum is also quantitatively affordable while retained exactly:
\(|L_{D_k}|\le15k(1+15k)\), and

\[
|\Phi_{k,t}(1)(1+L_{D_k})|
\le(1+15k+225k^2)e^{-k(T^2-81/16)}<\eta_N/16.
\tag{18}
\]

This uses the Gaussian pole damping and a finite harmonic sum, rather
than an assumed saving in \(L_{D_k}\). Keeping the term in (10) and
(14) makes the underlying identity directly reviewable.

## The cutoff retains every forbidden zero residue

For each fixed cutoff \(D\), let
\(M_{\log,D}(s)=\sum_{d\le D}\mu(d)\log d\,d^{-s}\).
Initially for \(\Re s>1\), the infinite high-divisor coefficient series
is exactly

\[
\sum_{n\ge1}[-a_D(n)]n^{-s}
=-\frac{\zeta'}{\zeta}(s)+\zeta(s)M_{\log,D}(s).
\tag{19}
\]

The additional term is analytic at every nontrivial zero and vanishes
there. The residue remains minus the zero's multiplicity. At one the
residue is \(1+M_{\log,D}(1)=1+L_D\), matching (10).
This is a meromorphic identity with fixed \(D\), not evaluation of a
convergent Dirichlet series at a zero. The sample-dependent cutoff in
(10) is handled by its exact arithmetic identity separately for each
sample, rather than substituted into a Mellin transform over changing
physical scales.

Equation (19) supplies no contraction. Directly shifting its added
\(\zeta M_{\log,D}\) term would incur another contour cost. The proof
above instead uses the full \(\Lambda\) Gaussian identity and pays the
small-divisor lattice error explicitly.

## Feasibility and the next bounded investigation

At the illustrative magnitude \(T=3\cdot10^{12}\), the saved
outward count gives \(N=41\), so \(168\le k\le328\). The new ranges
have
\(2520\le\log D_k\le4920\),
\(4368\le\log B_k\le8528\), and cofactor ceilings with logarithms
between 1848 and 3608. The centers are \(\log X=20k\).
These are hypothetical detector costs, not suggested direct enumerations
or new zero exclusions.

Ordinary absolute PNT estimates still do not reach the needed cancellation.
For example [Johnston--Yang, Theorem 1.1](https://arxiv.org/html/2204.01980v2)
gives a relative error of the form
\(9.39(\log x)^{1.515}e^{-0.8274\sqrt{\log x}}\).
This is subpower in \(x\). Transferring such envelopes through an
absolute-value estimate does not supply the fixed power in the original
supremum gate or the exponentially small signed response in (17).
This comparison tests that method; it is not a lower bound for the
actual arithmetic observable or an impossibility theorem for cancellation.

The Type-II phase also factors exactly:

\[
e^{-it\log(dr)}=d^{-it}r^{-it},\qquad
\frac{e^{-it\log(d_1r)}}{e^{-it\log(d_2r)}}
=e^{-it\log(d_1/d_2)}.
\tag{20}
\]

Differencing in the divisor variable leaves a phase independent of the
cofactor. A generic mixed-phase estimate therefore does not gain a power
merely from the factor sizes. Any useful estimate must use Möbius signs
and the complete weighted interaction.

For a scale diagnostic only, the unsigned Gaussian density mass is
\(e^{81k/16}\). Supposing a relative divisor saving \(D_k^{-\alpha}\)
could be inserted into that envelope without extra height losses, beating
\(\eta_N\) at all samples would require asymptotically

\[
\alpha>\frac{81/16+\log(8e)/4}{15}.
\tag{21}
\]

This is a sufficient-input diagnostic, not a necessary barrier for the
true signed sum. Cofactor cancellation can change it. A global untwisted
Mertens power bound supplied as an assumption would itself impose a
strong zero-free statement; it must not be imported as routine arithmetic.

The next bounded task is to test one complete signed dyadic estimate for
(10) or (14), retaining every product cap and the continuum, and state
its actual divisor, cofactor, and carrier range. Before a large numerical
sweep, a short Poisson-saddle calculation may improve the coarse cutoff
\(D_k\), reducing that range. Any claimed saving should be checked against
(19), since the forbidden zero coefficient survives the exact deletion.

The [replay source and small record](../../../numerics/height_adapted_zero_detection/gaussian_localization/README.md)
check finite coefficient identities with formal prime logarithms and
synthetic complex rational weights, Gaussian moment arithmetic, the exact
tail polynomial, and outward budget calculations. They do not evaluate
the giant arithmetic target. The all-sample proofs are the analytic
arguments above. The [internal review](../../../reviews/height_adapted_zero_detection/gaussian_localization/ARITHMETIC_REDUCTION_REVIEW_20261004.md)
records the check scope and the remaining cancellation gap.
