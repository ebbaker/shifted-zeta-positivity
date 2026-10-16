# A complete candidate-current atlas and thirteen simple heat-zero branches

10 October 2026. Prepared with substantial LLM assistance. The parent
session recording verifies model GPT-6.1-sol (Codex), configured reasoning
effort ultra; the delegated work inherits that configuration. Derivation,
interval replay and agent cross-reading are internal checks, not independent
mathematical review.

This continues [Note 3](3_COMPLETE_CURRENT_AND_PAID_SIMPLE_ZERO_RECTANGLE_20261010.md)
over a height interval eighty times wider and through the exact time
endpoint \(t=1/20\). The new finite theorem covers the **entire closed
rectangle**, preserves all 22,066 genuine cutoff terms, and proves exactly
thirteen simple genuine heat zeros at each allowed time. Value-away strips
are removed first; every surviving strip has a strictly paid complete
current and a strictly paid physical derivative. These are bounds on actual
signed arithmetic data with full holomorphic payment.

Put
\[
 M=N=22066,\qquad x_0=4\pi M^2,\qquad
 t_0=(2\log M)^{-1},
\]
\[
 \mathcal A=\{(t,x):t_0\le t\le1/20,\quad x_0\le x\le x_0+8\}.
\tag{1}
\]
Here \(t_0\approx0.04999103540096768\), so the time width is about
\(8.9645990\cdot10^{-6}\). The theorem is
\[
 \inf_{\mathcal A}\left\|(Q_t,Q_t'/L)\right\|>0.03728,
 \qquad H_t=A_tQ_t,
\tag{2}
\]
and, for every \(t\in[t_0,1/20]\), exactly thirteen zeros of
\(H_t\) occur in \([x_0,x_0+8]\), all simple. Thus \(H_t,H_t'\)
have no joint zero anywhere in (1). Each zero is trapped in its own fixed
disjoint height band and gives a smooth zero branch, with local continuation
through the endpoint times. No continuation farther outside the certified
domain is asserted.

## 1. Exact domain, constant cutoff and full payment

The time and height in (1) are exact expressions. Decimal intervals for
\(t_0\) and \(x_0\) are only outer arithmetic hulls. In particular the
lower endpoint of a rounded time hull lies microscopically below exact
\(t_0\); the sector assertion concerns (1), not that additional hull.
Since \(t_0(2\log M)=1\), monotonicity proves
\[
 1\le\kappa=t\log(x/(4\pi))<1.000180<2
\tag{3}
\]
on the exact domain. The interval calculation independently proves
\[
 M^2+0.0031244<\frac{x}{4\pi}+\frac t{16}
                 <M^2+0.639745<(M+1)^2.
\tag{4}
\]
Consequently the natural integer cutoff is always precisely \(M\).
The choice of nonnegative height offsets is deliberate: negative offsets
at time \(t_0\) would violate \(\kappa\ge1\), and sufficiently negative
offsets would also change the natural cutoff. Neither change is silently
inserted into this certificate.

The full complex-disk interface from Heat Notes
[8](../../notes/8_SIGNED_SHRINKING_COLLISION_VECTOR_AND_PHASE_OBSTRUCTION_20261009.md)
and [13](../../notes/13_RECENT_HEAT_RESULTS_AND_PATHS_FORWARD_20261009.md)
gives
\[
 |Q_t-F_{t,M}|\le\eta,\qquad |Q_t'-F_{t,M}'|\le L\eta,
 \quad \eta\le5e^{-tL^2/16-L/4},\quad L=\log(x/(4\pi)).
\tag{5}
\]
On the real axis \(F=2\Re S\), \(F'=2\Re S'\), with
\(S=\sum_{n=1}^{M}q_n\). Off-axis the approximant is the symmetric
reflected analytic sum from those notes. The payment includes the true
normalizer, reflection, natural-cutoff changes within the local disk and
Cauchy's derivative payment. The new checker uses this already established
analytic interface; it does not reprove the imported approximation theorem.
The resulting uniform outward payments satisfy
\[
 \eta<0.009642,\qquad L\eta<0.192864.
\tag{6}
\]

## 2. One signed coherent polynomial covers the whole interval

Let \(q_n^0=q_n(t_0,x_0)\),
\(\delta_n=\log(M/n)\), \(\omega_n=\delta_n/2\), and define
\[
 G(h)=\sum_{n=1}^{M}q_n^0e^{-i\omega_nh},\qquad
 g_j=G^{(j)}(4)
       =\sum_{n=1}^{M}(-i\omega_n)^jq_n^0e^{-4i\omega_n},
       \quad0\le j\le63.
\tag{7}
\]
The genuine principal-branch carrier and every weight remain in these
signed sums. There is no adjustable common phase. The comparison \(G\)
is a finite coherent transport, paid against the physical sum below; it is
not assigned a Newman heat equation.

With
\[
 P(h)=\sum_{j=0}^{63}g_j(h-4)^j/j!,\qquad
 M_{64}=\sum_{n=1}^{M}|q_n^0|\omega_n^{64},
\]
the real Taylor integral remainder yields throughout \(0\le h\le8\)
\[
 |G(h)-P(h)|\le\frac{M_{64}4^{64}}{64!}<1.480\cdot10^{-6},
\]
\[
 |G'(h)-P'(h)|\le\frac{M_{64}4^{63}}{63!}<2.3678\cdot10^{-5}.
\tag{8}
\]
Every real phase exponential has modulus one, so this remainder has no
exponential growth factor. The certificate stores all 64 signed complex
jets and the complete absolute moment; it does not discard a small-index
or complementary block.

Each adaptive cell uses the exact algebraic shift of the same polynomial
to its own midpoint, followed by interval Horner evaluation in the small
local displacement. This retains the coherent cancellations already
computed in (7); direct interval evaluation in a large displacement would
lose them. Sixty-three rational polynomial-shift controls check this
translation routine. The Taylor remainders in (8) remain global bounds and
are added after the exact shift.

All complement and block interference is present because the checker sums
every term before forming the current
\[
 \mathcal J=-\Im(S'\overline S)=u'v-uv',\qquad S=u+iv.
\tag{9}
\]
Expanding this complete product recovers the block, complement and cross
current of Note 3. The signed real observations \(u,u'\) also retain the
actual common carrier, and hence reflected phase information. No complex
norm or diagonal-only estimate replaces these real observations.

## 3. Physical spatial and time motion remain paid

Use the physical data of Note 3, \(\alpha=\alpha_r+i\alpha_i\),
\(\alpha'=U+iV\),
\(c=(1+tU/2)/2\),
\(\Omega=\{\alpha_r(1+tU/2)-\alpha_i tV/2\}/2\). At fixed
time and cutoff,
\[
 \gamma_n=q_n'/q_n=-tV\log n/4-i(\Omega-c\log n),
\]
\[
 r_n=\gamma_n+i\omega_n
 =-t_0V\log n/4-i\{\Omega-c\log M+(c-1/2)\delta_n\}.
\tag{10}
\]
On the complete spatial hull \(x_0\le x\le x_0+8\), the checker
bounds \(|r_n|\) by a componentwise complex absolute bound \(R_n\).
The exact scalar transport identity then gives
\[
 q_n(t_0,x_0+h)=q_n^0e^{-i\omega_nh}
                  \exp\!\left(\int_0^h r_n(x_0+y)\,dy\right),
\]
\[
 \epsilon_{x,0}=\sum |q_n^0|(e^{8R_n}-1),\qquad
 \epsilon_{x,1}=\sum |q_n^0|
       \{\omega_n(e^{8R_n}-1)+R_ne^{8R_n}\}.
\tag{11}
\]
These bound \(|S(t_0,x_0+h)-G(h)|\) and its physical spatial
derivative error, respectively. In particular amplitude drift and carrier
curvature have both been paid.

At fixed physical \(x,N\),
\[
 \chi_n=q_{n,t}/q_n=\log^2n/4-\alpha_r\log n/2
                  +i\alpha_i(\alpha_r-\log n)/2,
\]
\[
 \gamma_{n,t}=-V\log n/4
              -i\{U(\alpha_r-\log n)-\alpha_iV\}/4,
\]
\[
 S_t=\sum q_n\chi_n,\qquad
 S_{xt}=\sum q_n(\gamma_{n,t}+\gamma_n\chi_n).
\tag{12}
\]
The imaginary part of \(\chi_n\) retains the genuine common time phase.
These are not derivatives along the curve \(tL=1\). Summing complete
outward bounds on (12) gives budgets \(B_{t,0},B_{t,1}\) on the whole
rectangle. With \(\Delta t=1/20-t_0\), the complex component enclosures
of the physical \(S,S'\) use
\[
 E_0=M_{64}4^{64}/64!+\epsilon_{x,0}+\Delta t B_{t,0},
\]
\[
 E_1=M_{64}4^{63}/63!+\epsilon_{x,1}+\Delta t B_{t,1}.
\tag{13}
\]
The following deliberately wider bounds are replay assertions or directly
enclosed quantities.

| Complete transport budget | Outward bound |
|---|---:|
| Maximum spatial residual \(R_n\) | \(<3.490\cdot10^{-10}\) |
| Spatial value transport \(\epsilon_{x,0}\) | \(<2.598\cdot10^{-7}\) |
| Spatial derivative transport \(\epsilon_{x,1}\) | \(<3.306\cdot10^{-7}\) |
| Fixed-height time budget \(B_{t,0}\) | \(<2201\) |
| Fixed-height mixed budget \(B_{t,1}\) | \(<2194\) |
| Total complex value error \(E_0\) | \(<0.019732\) |
| Total complex physical derivative error \(E_1\) | \(<0.019684\) |

For the genuine real observations, (5) adds another \(\eta\) to
\(2E_0\) and another \(L\eta\) to \(2E_1\). Every endpoint sign and
derivative sign below includes both layers of payment.

## 4. An adaptive paid candidate atlas is complete coverage

A genuine joint zero necessarily obeys both rectangular tolerances
\[
 |u|\le\eta/2,\qquad |u'|\le L\eta/2,
\tag{14}
\]
and the complete-current consequence
\[
 |\mathcal J|\le\frac\eta2(L|v|+|v'|).
\tag{15}
\]
The checker starts with the closed height interval \([0,8]\), always
covering the full exact closed time interval. It bisects a height cell only
when neither acceptance rule has been proved. It accepts a cell by one of
two explicitly recorded rules:

1. **Value pruning:** the entire physical \(u\) enclosure has distance
   from zero greater than the outward value tolerance \(\eta/2\).
2. **Paid candidate current and derivative:** the physical \(u'\)
   enclosure has distance greater than \(L\eta/2\), and the entire
   complete \(\mathcal J\) enclosure reverses (15), including its full
   invisible-quadrature support payment.

Thus every cell whose value enclosure could contain a genuine zero must
pass *both* derivative and current tests. No cell is accepted solely by a
midpoint sign or an unverified favorable phase. The resulting atlas has
46 closed strips: 29 value-pruned strips and 17 strips retained by the
value screen, of total height width \(2.25\). Cell widths are \(1/8\)
or \(1/4\). Exact Decimal dyadic adjacency, both boundary endpoints and
total width eight are checked. Their union is the whole closed rectangle
(1), including every shared cell boundary and \(t=1/20\).

The minimum complete-current gap on the 17 retained strips is
\[
 \inf\left\{|\mathcal J|-\frac\eta2(L|v|+|v'|)\right\}
       >0.11934.
\tag{16}
\]
This is a bounded candidate-conditioned signed estimate: a point not
removed by the necessary value screen lies in a strip that violates the
paid current candidate condition. Several value-pruned strip current
enclosures straddle zero; the atlas does not claim current positivity
throughout the rectangle.

The checker also reports the lower bound
\[
 (2|u|/\eta)^2+2|u'|/(L\eta)
\tag{17}
\]
on every strip. The strengthened necessary upper bound one at a joint
zero follows from the holomorphic error correlation in
[Heat Note 18](../../notes/18_CORRELATED_HOLOMORPHIC_PAYMENTS_AND_CANDIDATE_COVERAGE_20261010.md).
This is an additional audit quantity. The coverage proof and the finite
theorem already follow from (14)–(16), without relying on that refinement.

For a value-pruned strip, \(|Q_t|\ge2\operatorname{dist}(u,0)-\eta\).
For a retained strip,
\(|Q_t'|/L\ge2\operatorname{dist}(u',0)/L-\eta\), bounded using the
largest enclosed \(L\). Taking the smallest positive component margin
over all 46 cells proves (2).

## 5. Exact counting and simple branches

Merge adjacent retained strips into connected bands. There are thirteen
such disjoint bands. The checker independently evaluates both endpoints
at every allowed time, adds the full value payment, and checks opposite
strict signs. It also verifies one strict sign of the fully paid
\(Q_t'\) throughout each band. The intermediate-value theorem and strict
monotonicity give exactly one genuine zero there at every time. The
value-pruned complement contains no zero, so the total count is exactly
thirteen, not merely thirteen detected crossings.

| Height offset band \(x-x_0\) | Sign of \(Q_t'\) throughout |
|---|---|
| \([0.25,0.375]\) | positive |
| \([0.875,1]\) | negative |
| \([1.5,1.625]\) | positive |
| \([2,2.25]\) | negative |
| \([2.625,2.875]\) | positive |
| \([3.25,3.375]\) | negative |
| \([3.75,3.875]\) | positive |
| \([4.375,4.5]\) | negative |
| \([5,5.125]\) | positive |
| \([5.625,5.75]\) | negative |
| \([6.125,6.5]\) | positive |
| \([7,7.125]\) | negative |
| \([7.5,7.75]\) | positive |

Every band has \(|Q_t'|>3.08\). The complete numerical intervals for
the two endpoint values and the derivative are stored in the certificate.
Because \(A_t>0\) on the real axis, normalized and genuine zeros agree;
at a zero \(H_t'=A_tQ_t'\ne0\). Smoothness and the implicit-function
theorem, together with uniqueness and trapping inside each fixed band,
give the thirteen branches across the certified time interval.

## 6. Replay and the remaining arithmetic obligation

The new standard-library source is
[check_candidate_current_atlas.py](../numerics/check_candidate_current_atlas.py).
It hash-checks the unchanged Note 3 source before import; the latter also
checks the unchanged Note 2 interval source. It inherits the 60-digit
directed Decimal arithmetic, enclosed pi, exact principal carrier, Taylor
trigonometry and the directed-multiplication integer-power override. No
ordinary binary float enters a proof assertion.

The retained
[certificate](../numerics/CANDIDATE_CURRENT_ATLAS_CERTIFICATE_20261010.json)
stores the coherent jets, complete motion budgets, full payments, every
closed leaf and all thirteen endpoint/monotonicity checks. Its size is
about 122 KB, below the repository's small-record convention. The
[build record](../numerics/CANDIDATE_CURRENT_ATLAS_BUILD_RECORD_20261010.json)
binds the new source, both preserved dependencies and the certificate.
Hashes establish identity; the arithmetic decides the signs.
[Review 4](../reviews/4_CANDIDATE_CURRENT_ATLAS_INTERNAL_REVIEW_20261010.md)
records internal analytic and replay checks.

The certificate expands a finite geometric neighborhood; it supplies no
estimate uniform in \(M\), no sign across untested cutoff cells, no
shrinking-time theorem and no RH conclusion. The next arithmetic task is
to retain a paid complete candidate margin across a specified family of
cutoff cells, with the sector edge and cutoff jumps explicitly controlled,
or to extract the uniform signed information needed by the complete
threshold-jet inequality. Repeating finite atlases can test such a proposed
mechanism; it does not establish its uniform bound.
