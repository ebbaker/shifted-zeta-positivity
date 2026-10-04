# One-sided continuation of the prepared-probe growth criterion

3 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); exact serving variant and reasoning effort not exposed.
This is a same-model research derivation, not independent specialist refereeing.
No literature priority is claimed for the Landau argument or oscillation method.

## Results and scope

The proposed global bound can be weakened further. For the exact prepared
polynomial probe in `SINGLE_PROBE_GROWTH_THEOREM_20261003.md`, **either an
upper or a lower eventual subexponential envelope alone implies RH**.
Likewise, weighted integrability of only the positive part or only the
negative part suffices. Neither envelope is established here.

There is also a quantitative strengthening of the obstruction: every
hypothetical off-critical zero forces exponential excursions of both
signs, with an explicit residue lower bound at the zero's exact exponent.
The argument does not need a rightmost zero or a spectral gap.

A positive continuous prime-counting model demonstrates precisely why
positivity of the counting measure, the prepared polynomial kernel, and
a prime number theorem with an error exponent above one-half cannot,
by themselves, supply the missing estimate.

## 1. Notation and real-axis regularity

Keep the existing normalized probe, its autocorrelation `phi`, support
radius `ell=1/2`, and bilateral transform `Phi`. Put

    M(r) = sum_(n>=2) Lambda(n)n^(-1/2) phi(log n-r),
    A(s) = -Phi(s) zeta'(1/2+s)/zeta(1/2+s).

The earlier note proves:

    M(r) = O((1+r)e^(r/2)),
    L M(s) = A(s)  for Re s>1/2,
    Phi(s) != 0  if Re s>0 and s != 1/2.

The zero of `Phi` at `s=1/2` has order two, so the apparent pole of `A`
there is removable. Moreover, **A is holomorphic in a neighborhood of
every real s>=0**. For `1/2+s>1` this follows from the Euler product.
For `0<1/2+s<1`, the alternating eta series is positive, while
`1-2^(1-(1/2+s))` is negative, so zeta is strictly negative and nonzero.
For completeness, the alternating eta series is positive because its
sum lies between `1-2^(-v)>0` and `1` when `v>0`.
At `s=0`, zeta is nonzero and `Phi` has a double zero. This regularity
is a local real-axis statement, not a zero-free right half-plane claim.

## 2. Positive Laplace transforms cannot continue across their real abscissa

**Lemma (Landau boundary lemma).** Let `f>=0` be locally integrable on
`[0,infinity)`, and suppose its Laplace transform converges at at least
one real point. Define

    sigma_c = inf{sigma : integral_0^infinity e^(-sigma r)f(r)dr<infinity}.

If `sigma_c` is finite, the Laplace transform has no holomorphic
continuation to a neighborhood of the real point `sigma_c`.

**Proof.** Suppose such a continuation exists in a disc
`|s-sigma_c|<R`. Set `b=sigma_c+R/4`. Its Taylor series about `b`
converges at `b-R/2`, since the disc centered at `b` of radius `3R/4`
is contained in the continuation disc. Differentiation under the
integral, justified by a smaller convergent exponential weight, gives

    (-1)^n F^(n)(b) = integral r^n e^(-br)f(r)dr >= 0.

Consequently the Taylor expansion and Tonelli's theorem imply

    F(b-R/2)
      = sum_(n>=0) (R/2)^n/n! integral r^n e^(-br)f(r)dr
      = integral e^(-(b-R/2)r)f(r)dr < infinity.

But `b-R/2=sigma_c-R/4`, contradicting the definition of `sigma_c`.
The same proof applies to a nonnegative tail; truncating a locally
integrable function on a compact interval adds an entire transform. QED.

This is the standard positivity mechanism in Landau's theorem.
A modern research-paper treatment of the Laplace version is Lemma 5.4
of J.-S. Giet, P. Vallois, and S. Wantz-Mézières, *The logistic S.D.E.*, 
Theory of Stochastic Processes 20(36), no. 1 (2015), 28–62:
https://www.mathnet.ru/eng/thsp95 . The proof above is included so the
application does not rely on importing that theorem's probability setup.
For context on the classical Dirichlet-series version, see B. Maurizi,
*Extending Landau's Theorem on Dirichlet Series with Non-Negative
Coefficients*, arXiv:1009.0228, https://arxiv.org/abs/1009.0228 .

## 3. One fixed exponent, one sign

**Proposition.** Let `a>=0`. If for some `K>=0` and `R>=0` either

    M(r) <= K e^(a r)  for all r>=R,                    (3.1+)

or

    M(r) >= -K e^(a r) for all r>=R,                    (3.1-)

then

    integral_0^infinity e^(-sigma r)|M(r)|dr<infinity
                  for every sigma>a.                  (3.2)

In particular zeta has no zero with `Re rho>1/2+a`.

**Proof.** In the upper-bound case put

    f(r) = 1_[R,infinity)(r) [K e^(a r)-M(r)] >=0.

It has Laplace abscissa at most `max(a,1/2)`, possibly minus infinity. In the
initial convergence half-plane,

    F(s) = K e^(-(s-a)R)/(s-a) - A(s)
                + integral_0^R e^(-sr)M(r)dr.            (3.3)

If its abscissa `sigma_c` exceeded `a`, the right side would be
holomorphic in a neighborhood of the real `sigma_c`, by section 1.
The meromorphic identity theorem extends the initial equality throughout
the convergence half-plane, supplying the continuation needed in the Landau lemma. The lemma rules out `sigma_c>a`. (If the abscissa
is minus infinity, the conclusion is immediate.) Thus `f` is integrable
with every exponential weight of exponent `sigma>a`. Since

    |M(r)| <= K e^(a r)+f(r)  for r>=R,

(3.2) follows, and compact intervals cause no difficulty. The lower-bound
case uses `f=1_[R,infinity)(K e^(a r)+M(r))` and the same argument.
The earlier transform/noncancellation theorem then excludes zeros in
`Re rho>1/2+a`. QED.

One may replace `K e^(a r)` by `K(1+r)^k e^(a r)` (fixed nonnegative
integer k): its tail Laplace transform is holomorphic near every real
`s>a`, so the same proof works. A continuous nonnegative majorant `B`
with a Laplace transform holomorphic on `Re s>a` also works.

**Corollary.** Each of the following is equivalent to RH and to the
all-window positivity conclusion in the existing manuscript:

* For every `epsilon>0`, `M(r)<=C_epsilon e^(epsilon r)` eventually.
* For every `epsilon>0`, `M(r)>=-C_epsilon e^(epsilon r)` eventually.

The envelope constants and start points may depend on epsilon. Either
one of these conditions alone suffices; they need not be assumed jointly.
Conversely RH supplies the already established two-sided boundedness.

## 4. Only one signed part need be integrable

Write `M_+=max(M,0)` and `M_-=max(-M,0)`.

**Proposition.** For any fixed `a>=0`, if

    integral e^(-sigma r) M_+(r)dr<infinity for every sigma>a,  (4.1+)

then the same holds for `M_-`, and hence for `|M|`. The reverse-sign
statement holds as well.

**Proof.** Let `P(s)=L M_+(s)`, holomorphic on `Re s>a`, and let
`N(s)=L M_-(s)` in its initial half-plane. There

    N(s) = P(s)-A(s).

If the nonnegative function `M_-` had Laplace abscissa `b>a`, the right
side would continue `N` holomorphically near real `b`, contrary to the
Landau lemma. Thus that abscissa is at most `a`. Reverse the signs for
the other assertion. QED.

In particular each of the two separate assertions

    for every epsilon>0, integral e^(-epsilon r) M_+(r)dr<infinity,
    for every epsilon>0, integral e^(-epsilon r) M_-(r)dr<infinity

is equivalent to RH. A weighted `L^2` condition on just one signed part
also suffices, by Cauchy–Schwarz followed by this proposition.

## 5. Both signs must reveal an off-critical zero

**Proposition (explicit two-sided oscillation obstruction).** Suppose
`rho=1/2+alpha+i gamma` is a zeta zero of multiplicity `m`, with
`alpha>0`. Then

    limsup_(r->infinity) e^(-alpha r) M(r)
                           >= m |Phi(alpha+i gamma)| > 0,
    liminf_(r->infinity) e^(-alpha r) M(r)
                           <= -m |Phi(alpha+i gamma)| < 0.       (5.1)

These are extended-real limsup/liminf assertions.

**Proof.** Put `s0=alpha+i gamma`, with residue
`Res_(s=s0) A(s) = -m Phi(s0)`. There are no real nontrivial zeros, so
`gamma!=0`. Suppose the first inequality fails. Choose a positive `K`
strictly between the limsup and `m|Phi(s0)|`; if the limsup is negative,
any sufficiently small positive `K` works. Then `M(r)<=K e^(alpha r)`
for all sufficiently large `r`. Section 3 shows that the nonnegative
tail `f=K e^(alpha r)-M(r)` has a Laplace transform in `Re s>alpha`,
given there by (3.3). Positivity gives

    |F(sigma+i gamma)| <= F(sigma)  for sigma>alpha.

Multiply by `sigma-alpha` and let `sigma` decrease to `alpha`.
The real expression tends to `K`, because `A` is regular at real
`alpha` and the compact correction is entire. On the complex ray the
majorant and compact correction stay regular, whereas the residue of
`-A` gives a limit of magnitude `m|Phi(s0)|`. Hence
`m|Phi(s0)|<=K`, a contradiction. Apply the same proof to `-M` for the
second inequality. QED.

The proof is also valid for `alpha=0` whenever `Phi(i gamma)!=0`.
For an off-critical zero noncancellation was already proved, so no
additional proviso is needed in (5.1).

Consequently, for every `0<=b<alpha`,

    limsup e^(-b r) M(r)=+infinity,
    liminf e^(-b r) M(r)=-infinity,

and both weighted integrals of `M_+` and `M_-` diverge with any positive
weight exponent strictly below `alpha`. The latter assertion follows
from section 4 and the pole at `s0`, not merely from pointwise excursions
(which alone would not control excursion widths).

## 6. Direct arithmetic route: exactly where cancellation is needed

Let `psi(x)=sum_(n<=x)Lambda(n)` and `E(x)=psi(x)-x`. For `r>ell`, the
whole support lies in `x>1`, and the zero `Phi(1/2)=0` removes the main
term exactly:

    M(r) = integral x^(-1/2) phi(log x-r) dE(x)
         = -integral E(x) x^(-3/2)
                    [phi'(log x-r)-phi(log x-r)/2] dx.     (6.1)

There are no endpoint terms: `phi` is compactly supported and vanishes
at the endpoints. If `|E(x)|<=B x^theta`, equation (6.1) gives

    |M(r)| <= B e^((theta-1/2)r)
                  integral_-ell^ell e^((theta-1/2)u)
                                 |phi'(u)-phi(u)/2|du.     (6.2)

Thus this direct route reaches subexponential growth only once the
prime-counting remainder reaches the square-root exponent with an
arbitrarily small loss. Applying an absolute bound to (6.1) cannot use
the signs of the oscillatory kernel to improve the exponent.

A one-sided estimate on `E` does not directly yield a one-sided estimate
on `M`: the coefficient `phi'-phi/2` changes sign. Indeed its weighted
integral is

    integral e^(u/2)[phi'(u)-phi(u)/2]du = -Phi(1/2)=0,

and it is nonzero, so it cannot have just one sign.

## 7. Positive model showing the limitation is real

Fix `0<alpha<1/2`, `gamma!=0`, and `0<delta<1`. Define a positive
continuous counting measure on `[1,infinity)` by

    d psi_model(x) = [1+delta x^(alpha-1/2) cos(gamma log x)] dx.

Its density is at least `1-delta>0`, and

    psi_model(x) = x-1
        + delta Re[(x^(1/2+alpha+i gamma)-1)/(1/2+alpha+i gamma)],

so `psi_model(x)=x+O(x^(1/2+alpha))`. The same normalized polynomial
probe gives, for every `r>ell`, the exact identity

    M_model(r)
       = integral x^(-1/2) phi(log x-r) d psi_model(x)
       = delta e^(alpha r) Re[e^(i gamma r) Phi(alpha+i gamma)].

Here the main term is `e^(r/2)Phi(1/2)=0`, while the final coefficient
is nonzero by the probe's proved zero-location property. Therefore

    limsup e^(-alpha r) M_model(r)=delta |Phi(alpha+i gamma)|,
    liminf e^(-alpha r) M_model(r)=-delta |Phi(alpha+i gamma)|.

This is not a model of the Euler product or a claim about actual primes.
It proves only, but rigorously, that **positivity of the counting measure,
its leading PNT density, the compact polynomial preparation, and even
any fixed remainder exponent above one-half are jointly insufficient**
to yield the desired one-sided or two-sided subexponential estimate.
An argument must exploit additional arithmetic information about the
actual von Mangoldt weights.

## 8. Unconditional reduction to primes alone

Write

    M(r)=P(r)+sum_(k>=2) P_k(r),
    P(r)=sum_p (log p)/sqrt(p) phi(log p-r),
    P_k(r)=sum_p (log p)/p^(k/2) phi(k log p-r).

**Proposition.** The prime-power correction satisfies

    sum_(k>=2) P_k(r)=o(1)  as r->infinity.                 (8.1)

Hence all boundedness, one-sided subexponential envelope, and weighted
one-sided integrability criteria stated above are unchanged when `M`
is replaced by the sum `P` over primes alone. The exact off-critical
oscillation lower bounds (5.1) are also unchanged.

**Proof.** Put `theta(x)=sum_(p<=x)log p`. The unconditional prime number
theorem gives `theta(x)=x+o(x)`; its weaker consequence
`theta(x)<=C x` suffices for all powers at least three. For squares,

    P_2(r)=integral x^(-1)phi(2 log x-r)d theta(x).

Once the support lies in `x>1`, the `d x` main term equals

    integral x^(-1)phi(2 log x-r)dx=(1/2)integral phi(u)du=0,

since `integral phi=Phi(0)=0`. Write `R_theta(x)=theta(x)-x`. Integration
by parts gives

    |P_2(r)| <= (1/2) sup_(x in I_r)|R_theta(x)|/x
                              integral |2phi'(u)-phi(u)|du=o(1),

where `I_r=[exp((r-ell)/2),exp((r+ell)/2)]`. The supremum tends to zero
because the lower endpoint tends to infinity.

For `k>=3`, a contributing prime satisfies
`k log p in [r-ell,r+ell]`. Thus

    |P_k(r)| <= ||phi||_infinity exp(-(r-ell)/2)
                                   theta(exp((r+ell)/k))
             <= C ||phi||_infinity exp(5ell/6) exp(-r/6).

Only `k<=(r+ell)/log 2` can contribute. Summing gives

    sum_(k>=3)|P_k(r)|=O((1+r)e^(-r/6)).

Together with the square estimate this proves (8.1). The correction is
also bounded on compact intervals, so it is bounded globally. Adding
or subtracting a bounded function preserves every criterion claimed
above. For the one-sided integral statements use
`|u_+-v_+|<=|u-v|` and the corresponding inequality for negative parts.
QED.

This removes prime powers as a source of global growth. The square
contribution disappears because of the zero ordinary moment; the main
prime density disappears because of the exponential moment at `1/2`.
The remaining cancellation problem lies entirely in the actual primes.
The classical PNT input is summarized in NIST DLMF §25.16:
https://dlmf.nist.gov/25.16 .

## 9. Exact outstanding step

It now suffices to establish, arithmetically and for one sign, either

    for every epsilon>0,
    sum_(n>=2) Lambda(n)n^(-1/2)phi(log n-r)
                                      <= C_epsilon e^(epsilon r)
                                      for all sufficiently large r,

or its lower-bound analogue, or the corresponding weighted one-sided
integrability condition. None has been proved here. Analytic continuation
of `A` along the positive real axis cannot by itself substitute for the
missing envelope: signed Laplace transforms may continue across their
abscissas, as the explicit positive counting model above illustrates.
The Landau step only becomes available after one has controlled a signed
part or constructed a nonnegative tail with a controlled majorant.
