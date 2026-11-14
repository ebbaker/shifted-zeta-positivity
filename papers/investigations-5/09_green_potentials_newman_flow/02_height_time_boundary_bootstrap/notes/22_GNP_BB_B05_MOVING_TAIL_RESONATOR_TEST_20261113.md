# B05: bounded-length resonators for the moving Poisson tail

13 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance, **gpt-6.1-sol / ultra** by
explicit tool selection. **Status: proved in-note, scoped estimating-class
result.** This is the bounded resonance test for [B05 r1][packet], using
the unchanged [Note15 target][green] described in [Note19][continuation].
It concerns an auxiliary arithmetic moment and the reach of a specified
positive-resonator argument. [Result index][results], [avoid index][avoid],
[heat-flow cluster11][r11], [controls12][controls], [classification01][a01],
[premises02][a02], [scope07][scope], [separate allowances12][a12].

## 1. Same moving tail and actual height

For \(X>4\pi\) write \(L_X=\log(X/(4\pi))\),
\(\tau_X=X/2+\pi/(8L_X)\), and
\[
 K_X=\lfloor e^{L_X/32}\rfloor,\qquad
 N_X=\lfloor e^{L_X/2}\rfloor,\qquad
 w_n(X)=n^{-65/64}e^{(\log n)^2/(4L_X)}.
\]
The Poisson moment to test is
\[
 Q(X)=\int_{\mathbb R}P(v)
 \left|\sum_{K_X<n\le N_X} w_n(X)
                e^{i(\tau_X+v/2)\log n}\right|^2\,dv,
 \qquad \int P=2/5,\quad P\ge0.
\]
with the unchanged bottom-edge strip kernel of Note15. The question
is whether \(Q(X)\le4/66^2\) eventually at every real \(X\).
The heat time is fixed inside this Poisson integral. Changing \(X\)
in an auxiliary average below follows precisely this physical clock.

The [HCB resonator][hcb] uses \(tL=2\), a different physical-jet norm
and a nonnegative fixed 25-mode weight. Its first-branch fixed small
integer resonances supply the actual projected surplus
\(12721/10800>7/6\). In the present moving tail, every fixed one
of those integers lies below \(K_X\) eventually. This does not
eliminate quadratic exact-ratio resonances: pairs can have fixed
ratio while both indices move to infinity. The following calculation
pays those surviving resonances as well as all nonresonant pairs.
[HCB internal review][hcbreview].

## 2. A uniform result over a growing resonator support

For a large dyadic height window \([U,2U]\) let
\[
 \mathcal B(X)=\left|\sum_{r\le R} a_r e^{i\tau_X\log r}\right|^2,
 \qquad \sum_{r\le R}|a_r|^2=1 .
\]
The coefficients can be complex, arbitrary and different for each
window. They are held fixed as \(X\) varies through that window.
The opposite phase sign generates the same class after conjugating
coefficients. The support consists of integers in \([1,R]\).
Write \(K=K_U\), \(N=N_{2U}\), \(J=\lfloor R\rfloor N\).
For any fixed \(\varepsilon>0\), with \(\alpha=57/64\),
\[
 \begin{aligned}
 \frac1U\int_U^{2U}\mathcal B(X)Q(X)\,dX
 &\ll_\varepsilon
 R^\varepsilon(1+\log R)
       \left(K^{-25/32}
        +\frac{N^{2-2\alpha}R\log(2J)}U\right),\\
 \frac1U\int_U^{2U}\mathcal B(X)\,dX
 &=1+O\bigl(R\log(2R)/U\bigr).
 \end{aligned}                                                    \tag{1}
\]
Thus for any fixed \(0<\delta<57/64\), the normalized
resonator-weighted average of the **actual** \(Q(X)\) tends to zero
uniformly for \(1\le R\le U^\delta\). This method cannot exhibit
a fixed positive lower bound for the supremum by proving such a
lower bound on its weighted average in this support class.

**Moving endpoints and nonstationary terms.** An integer \(n\)
is present exactly on \([4\pi n^2,4\pi n^{32})\cap[U,2U]\).
A term with both \(n,m\) is therefore active on a single intersection
interval. On it, \(\log n\le L_X/2\) implies
\[
 0<w_n(X)\le n^{-\alpha},\qquad
 \alpha=57/64,qquad
 |w_n'(X)|\le w_n(X)/(16X).
\]
The weights' endpoint sizes plus total variation, for products or
individual terms, obey the corresponding majorants. The phase
derivatives are exact along this auxiliary height average:
\[
 \tau_X'=\tfrac12-\frac{\pi}{8XL_X^2}\asymp1,qquad
 \tau_X''=O(U^{-2})\quad(U\le X\le 2U).
\]
If \(nr\ne ms\), integration by parts on the actual active
interval bounds the integral of this product term by a constant
times \((nm)^{-\alpha}/|\log(nr/(ms))|\), before the outside
coefficient \(a_r\overline{a_s}\). This pays both endpoints and
the clock-dependent variation. The independent factor
\(e^{iv\log(n/m)/2}\) is of modulus one for real \(v\).
We may bound all terms uniformly in \(v\) and then integrate
against the unchanged probability-mass factor \(2/5\). Every
cutoff and every off-diagonal term is included.

Set
\[
 b_j=\sum_{\substack{nr=j\\ K<n\le N,\ r\le R}}
               n^{-\alpha}|a_r|.
\]
Terms with \(nr=ms\) cost at most \(\sum_j b_j^2\) after
division by \(U\). The other terms cost at most
\[
 \frac C U\sum_{j\ne k}\frac{b_j b_k}{|\log(j/k)|}
       \le \frac{C'\log(2J)}U\sum_j j b_j^2 .
\]
For the last inequality use \(c_j=\sqrt j\,b_j\), the symmetric
matrix \(1/(\sqrt{jk}|\log(j/k)|)\) off its diagonal, and the
Schur weight \(p_j=j^{-1/2}\). The weighted row is
\(\sum_{k\ne j}1/(k|\log(j/k)|)\). For \(k<j\),
\(\log(j/k)\ge (j-k)/j\) bounds the summand by
\(j/[k(j-k)]=1/k+1/(j-k)\); for \(k>j\),
\(\log(k/j)\ge(k-j)/k\) bounds it by \(1/(k-j)\).
Thus the row is at most \(3(1+\log J)\). The simpler
\(|\log(j/k)|\ge |j-k|/J\) estimate would instead pay
\(J\log(2J)\sum_j b_j^2/U\) for these terms.
The same argument for the resonator square alone gives the
second line of (1), since its exact diagonal is one.

**Exact product coincidences.** The quadratic form
\(\sum_j b_j^2\) is indexed by \(r,s\le R\). Put
\(d=\gcd(r,s)\), \(r=dh\), \(s=dk\). The equation
\(nr=ms\) has \(n=kq,m=hq\); the two lower cutoffs give
\(q>K/\min(h,k)\). Dropping the upper cutoffs for this
positive majorant, its entry is at most
\[
 \begin{aligned}
 (hk)^{-\alpha}\sum_{q>K/\min(h,k)}q^{-2\alpha}
 &\ll (hk)^{-\alpha}(K/\min(h,k))^{1-2\alpha} \\
 &\le C K^{-25/32}(hk)^{-1/2}
  = C K^{-25/32}\frac{\gcd(r,s)}{\sqrt{rs}} .
 \end{aligned}
\]
The power bound remains true when \(K/\min(h,k)<1\), because
its right side before simplification then bounds the convergent
full sum. For the last inequality use
\(\min(h,k)\le\sqrt{hk}\). Thus every fixed-ratio resonance
has a decaying majorant, and the collective contribution can
be bounded using arithmetic of the ratios.

For completeness let \(A_{rs}=\gcd(r,s)/\sqrt{rs}\) and
\(p_r=r^{-1/2}\). Its weighted row sum satisfies
\[
 \sum_{s\le R} A_{rs}\frac{p_s}{p_r}
 =\sum_{s\le R}\frac{\gcd(r,s)}s
 \le\sum_{d\mid r}\sum_{\substack{s\le R\\d\mid s}}\frac d s
 \le d(r)(1+\log R),
\]
where \(d(r)\) is the number of positive divisors of \(r\).
For symmetric \(A\), apply
\(2|a_r a_s|\le |a_r|^2 p_s/p_r+|a_s|^2 p_r/p_s\)
and sum. The elementary bound \(d(r)\ll_\varepsilon r^\varepsilon\)
follows by choosing a fixed prime cutoff with \(p^\varepsilon\ge2\)
above it, using \(e+1\le 2^e\) there, and taking the product
of finite maxima \(\sup_{e\ge0}(e+1)p^{-\varepsilon e}\)
over the remaining primes. This proves
\(\sum_j b_j^2\ll_\varepsilon K^{-25/32}R^\varepsilon(1+\log R)\).

For the weighted product norm \(\sum_j j b_j^2\), with
\(r=dh,\ s=dk,\ n=kq,\ m=hq\) as before, the product is
\(j=d h k q\). Use the upper cutoffs \(q\le N/\max(h,k)\)
and drop the lower cutoffs for an upper bound. Each entry is
at most
\[
 d(hk)^{1-\alpha}\sum_{q\le N/\max(h,k)}q^{1-2\alpha}
 \ll_\alpha d N^{2-2\alpha},
\]
since \(1-2\alpha>-1\) and \(hk\le\max(h,k)^2\). The same
gcd Schur bound applies after using \(d\le R d/\sqrt{rs}\).
Thus
\(\sum_j j b_j^2\ll_\varepsilon
 N^{2-2\alpha}R^{1+\varepsilon}(1+\log R)\), which completes (1).

Since \(K\asymp U^{1/32}\) and \(N\ll U^{1/2}\), the two
exponents on the first line of (1) are bounded, up to
logarithms, by \(-25/1024+\delta\varepsilon\) and
\(-57/64+\delta(1+\varepsilon)\).
Both are negative with a sufficiently small fixed
\(\varepsilon>0\) for the stated \(\delta\).
The denominator tends to 1 since \(\delta<1\).
All bounds use the actual \(\tau_X\) and the actual moving
entry and exit endpoints. No phase choice or sample is involved.
The simpler \(J\)-based separation bound above gives the intermediate
range \(\delta<537/1024\).

## 3. Consequences and remaining scope

Taking \(R=1\) gives the ordinary dyadic mean
\[
 \frac1U\int_U^{2U}Q(X)\,dX\ll U^{-25/1024}.
\]
For each fixed \(h>0\), the proportion where \(Q(X)>h\) is therefore
\(O_h(U^{-25/1024})\). This is a statement about the exact Note15
moment with its fixed Poisson scale. It leaves open every-center
acquisition and possible exceptional spikes, including violation
of the raw \(4/66^2\) budget at some unbounded sequence of centers.

The near-diagonal part on its own also has a quantitative limit.
At any actual \(X\), for integer shifts \(1\le n-m\le B\), the
sum of absolute quadratic coefficients (with the conjugate partner)
is at most
\[
       (4/5)B\sum_{K_X<n\le N_X}w_n(X)^2
                 \ll B K_X^{-25/32}.
\]
Here \(|\widehat P|\le2/5\) and
\(2w_m w_n\le w_m^2+w_n^2\). A fixed number of neighboring
diagonals, or \(B=o(K_X^{25/32})\), cannot itself give a
nonzero constant contribution. Also every nontrivial pair with
\(n,m\le N_{2U}\) has \(|\log(n/m)|\gg U^{-1/2}\);
even its smallest such frequency has cumulative phase drift
of order at least \(U^{1/2}\) across a dyadic interval.
Constructive interference at an isolated height remains possible.
The previously computed \(X^{7/64}\) absolute allowance from a
large block does not quantify that interference.

**Decision within this comparison.** Stop using a fixed or growing
positive integer Dirichlet-polynomial weight in the declared class
to seek a constant lower obstruction by a whole dyadic weighted
average. The result includes the literal HCB finite resonator and
the growing-support extension above. It leaves longer supports,
shorter/adaptively centered averaging intervals, other test
weights, sparse supports modeled using ratio gaps and actual
large-value mechanisms open. The unresolved new input is control
of the complete signed quadratic at each physical center, or a
different witness estimate that beats the small weighted means.
There is no pointwise upper or lower obstruction to the raw
budget here. In particular the conditional Green consumer remains
at its recorded status.

## 4. Candidate after separately controlling the outer modes

The fixed-pair comparison for the same full Poisson moment
provides a supported extension to test in a frozen execution.
Let \(T_X^{\rm mid}\) retain only
\[
        \lfloor e^{3L_X/64}\rfloor<n\le\lfloor e^{5L_X/16}\rfloor.
\]
There is a uniform complement payment
\[
 \|T_X-T_X^{\rm mid}\|_{L^2(P(v)\,dv)}
     =O(X^{-1/8192}).
                                                               \tag{2}
\]
For the low complement \(K_X<n\le\lfloor e^{3L_X/64}\rfloor\),
\(w_n\le n^{-1-1/256}\). Its full absolute sum is
\(O(K_X^{-1/256})=O(X^{-1/8192})\), uniform in \(v\).
For the high complement and \(|v|\le\log X\), the exact frequency
\(\tau_X+v/2\) lies in \([X/3,2X/3]\) beyond a finite onset.
Using the arbitrary-subinterval logarithmic-phase theorem
from [Note14][pairs], the word \(AABABA\) on \((1/6,2/3)\)
gives \((1/24,27/32)\). The weighted power at
\(s=\log M/L_X\in[5/16,1/2]\) is
\(1/24-41s/192+s^2/4\), whose endpoint powers are
\(-1/1536,-1/384\). It is convex. The inverse-frequency term
costs \(O(X^{-1/2})\) per block. The fixed Abel variations and
clipped dyads of Note14 give high complement
\(O((1+L_X)X^{-1/1536})\) uniformly in this inner region.
Outside \(|v|\le\log X\), the full absolute mode bound is
\(O(X^{7/128})\) and the actual Poisson kernel decays as
\(O(e^{-(64\pi/5)|v|})\). Thus the exterior norm costs
\(O(X^{7/128-32\pi/5})\). Combining these gives the stated
complement budget. The split retains the actual frequency
and the total Poisson integration.

For \(T_X^{\rm mid}\), an index is active on
\([4\pi n^{16/5},4\pi n^{64/3})\) before intersection with
the dyadic window. The same argument as in (1) applies.
Here \(w_n\le n^{-15/16}\) on this band, the moving lower
cutoff is of order \(U^{3/64}\), and its upper cutoff
\(N_{\rm mid}\) is \(O(U^{5/16})\). The unweighted coincidence power
\((3/64)(2(15/16)-1)=21/512\) replaces \(25/1024\).
The weighted coincidence norm has upper-cutoff factor
\(N_{\rm mid}^{2-2(15/16)}=O(U^{5/128})\), so the off-diagonal
height factor in (1) is \(U^{-123/128}\) before \(R^{1+\varepsilon}\)
and logarithms. The intermediate \(J\)-based bound for this
localized band would give \(\delta<373/512\).
The prospective enlarged resonator class with the weighted estimate is
\[
        0<\delta<1-5/128=123/128 .
\]
For each such \(\delta\), the numerator in (1) for the middle
moment tends to zero uniformly in \(R\le U^\delta\).
To return to the original moment, take the triangle inequality
in the joint norm with measure
\(U^{-1}\mathcal B(X)dX\,P(v)dv\). By (2) the low and high
complement together cost at most
\(O(U^{-1/8192})(U^{-1}\int_U^{2U}\mathcal B(X)dX)^{1/2}\).
The mass is \(1+o(1)\) for every fixed \(\delta<1\).
This supplies the proposed transfer for the full moment, ready
for a fixed proof and check. The scope is still rates of decay
of whole dyadic weighted averages. The every-center upper bound
and a positive lower-bound witness remain open.

## 5. Source and collision-control scope

The upper bound on the weighted means uses the integer product
coincidences, exact common physical phase and stated positive
coefficient envelope. It is valid for finite sums with these
same properties and does not itself distinguish all theta fields
from positive-source controls. When interpreted as a statement about
the [Note15][green] theta acquisition, the Euler-factor and translated
controls fail unchanged ordinary coefficients, weighted-square and
finite-tail sources fail the full unit coefficient/reflection
conjunction, reflected and primitive-compatible sources fail
canonical square arithmetic, finite-prime controls fail full
reflection/coefficient agreement, and atomic or finite-profile
controls fail full source and profiles beyond matched measurements.
Normalized endpoint perturbations fail ordinary Dirichlet arithmetic,
variable readouts fail the actual cosine heat field, and freely
changed phases fail the common logarithmic physical phase.
The bound contains no zero or collision assertion about any
of these controls. [Control catalog][controls], [HCB screen][hcb].

[packet]: ../research-progress/handoffs/GNP-BB-B05-r1.md
[green]: 15_GNP_BB_B04_SIGNED_GREEN_ACQUISITION_20261113.md
[continuation]: 19_GNP_BB_CONTINUATION_AFTER_FIVE_PAIR_TRANSFER_20261113.md
[hcb]: ../../../03_heat_flow_collision_bounds/notes/14_SIGNED_LAG_RESONATOR_AND_ACTUAL_REMAINDER_20261028.md
[hcbreview]: ../../../03_heat_flow_collision_bounds/reviews/09_SIGNED_LAG_RESONATOR_INTERNAL_REVIEW_20261028.md
[results]: ../../../../../result-summaries/README.md
[avoid]: ../../../../../avoid/README.md
[r11]: ../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[scope]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[pairs]: 14_GNP_BB_B04_BROADER_PAIR_COMPARISON_20261113.md
