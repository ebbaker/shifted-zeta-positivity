# B04 finite \(A,B\) comparison and a width-\(567/1000\) contract

13 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. Subagent dispatch recorded
**gpt-6.1-sol / ultra**. Backend configuration beyond the dispatch is
unavailable.

**Status.** Bounded analytical comparison. The finite-partition
allowance is proved below. Transferring it to a complete canonical
comparison on both domains is the [B04][packet] candidate for a fixed
execution. Follow [result-summaries][results] and [avoid][avoid], in
particular [heat-flow cluster11][r11], [collision controls12][r12],
[classification01][a01], [premises02][a02], [scope07][a07],
[separate bounds12][a12] and [imports16][a16]. This is a quantitative
advance in the finite-tail allowance under an unchanged field and clock.

## 1. Pair selection with the actual phase

Use [Note09][e02], [Note10][e03] and [Note12][e05]. Write
\(H_0(z)=\xi((1-iz)/2)/8\), \(\partial_tH_t=-\partial_z^2H_t\),
\(z=x+iy\), \(x>0\), \(L_x=\log(x/(4\pi))\), \(c=tL_x\), and
\(L(z)=\operatorname{Log}(z/(4\pi))\) on the right half-plane.
Keep the exact carrier and zeta argument
\(C_-(t,z)\), \(s_t(z)=(1-iz)/2+t L(z)/4-i\pi t/8\).
With \(N_x=\lfloor e^{L_x/2}\rfloor\), the dominant arm is
\(\sum_{n\le N_x}n^{-s_t(z)}e^{t(\log n)^2/4}\). Keep also the
full reflected arm with phase frequency
\(x/2+\pi t/8+t\Im L(z)/4\), the normalized corrected RS term,
and the entire provider remainder.

For either actual real frequency \(T\asymp x\), on arbitrary
subintervals \(I\subset[M,2M]\), the verified classical estimate is
\[
 \left|\sum_{n\in I} n^{\pm iT}\right|
    \ll x^kM^{l-k}+M/x .
\]
In [Montgomery–Vaughan][mv] use Definitions 16.1–16.2,
(16.55)–(16.58), with derivative parameter \(1\) and scale
\(T/(2\pi)>0\). The model phase is exactly \(T\log u/(2\pi)\),
so every relative derivative error is zero. Conjugation handles
the other sign. In the same author copy, Theorems 16.23 and 16.25
(printed pp. 37 and 41, PDF pp. 49 and 53) preserve exponent pairs
under
\[
 A(k,l)=\Bigl(\frac{k}{2k+2},\frac{k+l+1}{2k+2}\Bigr),
 \qquad B(k,l)=(l-1/2,k+1/2).
\]
Thus \(P=(1/6,2/3)=AB(0,1)\) and each pair below is verified.
Words act from right to left. These source passages were rechecked
in the author text via the web reader, using the existing
[source-use record][src]. No new PDF was downloaded. The theorem is
imported here for the logarithmic phase with \(M/x\) retained.
No log-ratio or mean-value estimate enters.

On real clipped dyadic blocks, Abel summation multiplies the estimate
by a fixed multiple of the starting weight. For the dominant amplitude
\(a_D(u)=u^{-\Re s_t(z)}e^{t(\log u)^2/4}\),
\(u\,a_D'(u)/a_D(u)=-\Re s_t(z)+t\log u/2\).
For the reflected amplitude
\(a_R(u)=u^{(y-1)/2}\exp(t[(\log u)^2-\Re L(z)\log u]/4)\),
the corresponding expression is
\((y-1)/2-t\Re L(z)/4+t\log u/2\).
Both are \(O_D(1)\) for \(0\le c\le D\), bounded \(y\), and
\(1\le u\le e^{L_x/2}\). This pays the weight supremum plus total
variation by \(O_D(a(M))\) within each clipped block.
There are \(O(1+L_x)\) blocks. The implied pair constants concern
only the fixed finite list.

## 2. Explicit five-piece proof

Put \(v=\log M/L_x\). For a pair \((k,l)\) write
\(g_{k,l}(v)=k/v+l-k-1+v/4\). At \(c=1\) the dominant
primary power of \(x/(4\pi)\) is bounded by
\[
 v[g_{k,l}(v)-\delta],\qquad \delta=(y-1/2)/2.
\]
The exact complex logarithm satisfies \(\Re L(z)\ge L_x\),
which can only improve the bound. Fix \(y_*=567/1000\)
and use real abscissae \(e^{vL_x}\) at the cuts below.
In each piece start its dyads at the left endpoint and clip at
the right. Intervals are open on the left and closed on the right.
The head ends at \(K_x=\lfloor e^{L_x/8}\rfloor\);
the selected blocks cover every integer \(K_x<n\le N_x\) once.

| \(v\) interval | Word at \(P\) | Pair | \(g\) at left | \(g\) at right |
| --- | --- | --- | --- | --- |
| \([1/8,4/25]\) | \(A^5\) | \((1/254,247/254)\) | \(1/32\) | \(841/25400\) |
| \([4/25,89/500]\) | \(A^5BA^2\) | \((11/1642,1573/1642)\) | \(5443/164200\) | \(4883141/146138000\) |
| \([89/500,11/50]\) | \(A^4BABA\) | \((1/102,385/408)\) | \(303221/9078000\) | \(1873/56100\) |
| \([11/50,9/20]\) | \(A^3BA^2BA\) | \((13/502,445/502)\) | \(18371/552200\) | \(5531/180720\) |
| \([9/20,1/2]\) | identity | \((1/6,2/3)\) | \(-37/2160\) | \(-1/24\) |

Each endpoint is at most \(q=669/20000\), and \(g''(v)=2k/v^3\ge0\).
For \(y\ge y_*\), \(\delta\ge67/2000=q+1/20000\).
Thus the primary power is at most \(-1/160000\).

At general \(c\), the change in that power is
\(-(c-1)(v-v^2)/4\), using the same real-log bound.
It improves the estimate uniformly for \(1\le c\le C\)
in the E05 transition region. On the curve at
\(t=1/L_X,\ |x-X|\le1\), use \(|c-1|\le10^{-5}\),
eventual once \(1/((X-1)L_X)\le10^{-5}\).
Its cost is at most \(1/1600000\). Both domains therefore
admit the power \(\kappa=1/200000\). The secondary term
\(M/x\) costs \(O(x^{-1/2})\) per block after weighting, since
\(a_D\le1\) and \(M\ll x^{1/2}\).

The precision of \(567/1000\) is supported by the finite table.
It is smaller than E03's exact \(A\)-chain allowance
\(2927/5152\) and the acquired common-time width \(4/7\).
For comparison, the [small exact replay][check] and [record][record] enumerate distinct
pairs of word length at most eight from \(P\), then intersects
the affine half-spaces for each candidate
\(k+(l-k-1)v\) to find its active intervals on \([1/8,1/2]\).
Minimizing \(g\) is equivalent to minimizing those lines at each
\(v>0\). Convexity on the active intervals reduces the outer
maximum to endpoint evaluations.

| Maximum word length | Envelope maximum | Width allowance |
| --- | --- | --- |
| 5 | \(351/10304\) | \(2927/5152\) |
| 6 | \(1663/49280\) | \(13983/24640\) |
| 7 | \(583/17360\) | \(4923/8680\) |
| 8 | \(406319/12161760\) | \(3446759/6080880\) |

Depth five leaves the old obstruction. Depths six and seven reduce
it but leave their best displayed allowance above \(567/1000\).
The length-eight maximum occurs at \(v=1040/5847\).
Convex combinations of these finite pairs cannot improve their
pointwise lower envelope since \(g\) is affine in \((k,l)\).
This finite-set comparison leaves other pairs and arbitrary-length
words outside its scope. Before the cap was fixed, exploratory exact-rational searches also
used depths 9–18. The depth-18 run reported the finite-set maximum
\(181561226381/5446973796992\) at \(1199424/6811987\), corresponding
to displayed width approximately \(0.56666499\). The fraction is
exact output and the decimal is rounded. These deeper results were
exploratory, are outside the replay, and furnish no input to the
five-piece contract. The contract and replay use only words through
length eight.

## 3. Full-field payment and fixed execution candidate

For \({y_*}\le y\le9/8\) and \(c\ge1-10^{-5}\),
\[
 \Re s_t(z)\ge(1+y)/2+c/4>1+1/32,\qquad
 (1+y)/2+7c/32>1+1/512 .
\]
Consequently the ordinary Euler-product reciprocal bound is 33.
For \(n\le K_x\), \(n^{-\Re s_t(z)}e^{t(\log n)^2/4}\le
n^{-1-1/512}\). The finite head's heat removal costs
\(A t\), \(A=\tfrac14\sum_{n\ge2} n^{-1-1/512}(\log n)^2\),
by \(e^u-1\le ue^u\). The ordinary zeta tail beyond \(K_x\)
costs \(32K_x^{-1/32}\ll x^{-1/256}\) as in E03. The
limiting fixed margin \(y_*-1/2\) pays this floor. At \(y=1/2\)
and \(c=1\), the uniform absolute-series margin tends to zero,
even though the exact complex-\(L\) correction can be positive.
A separate carrier and tail argument is needed there.

For the full reflected population use \(P\) on \(0\le v\le1/2\)
and \(|C_+/C_-|\ll x^{-y/2}\). Its primary power is at most
\(1/6-y/2+(y/2-c/4)v+cv^2/4\), convex in \(v\).
The endpoints at \(y=y_*,c=1-10^{-5}\) are both below \(-1/32\),
and both decrease with increasing \(y\) or \(c\) except the
\(c\)-independent left endpoint. The inverse derivative term,
using \(a_R(M)\le M^{1/16}\), costs at most
\(O(x^{-y/2}M^{17/16}/x)=O(x^{-1/2})\) per block.
This includes all reflected integers. Keep the inherited
normalized correction \(O_D(x^{-(1+y)/4})\) through every
fractional cutoff position. The remaining normalized HDA error
is \(O_D(x^{-3/4})(1+O(x^{-y/2}))\) from Note09 or the extended
positive provider in Note12, including the complete Gaussian
exterior. The ordinary zeta factor uses the exact \(s_t(z)\).

**Proposed E07 r1.** Freeze the full field, fixed chart/buffer data,
exact five cut intervals above, \(y_*=567/1000\) and
\(\kappa=1/200000\). Verify these payments with the inherited inputs
on both domains, preserving their distinct quantifiers.

- **Curve.** For \(t=1/L_X\) held fixed on \(|x-X|\le1\),
  \(y_*\le y\le9/8\), prove the exact field comparison against
  \(\zeta(s_t)\) with absolute error at most
  \(A/L_X+B(1+L_X)(X-1)^{-\kappa}\) after the Note09 gates and
  stated clock tolerance. Require 33 times this at most \(1/64\).
  Initial strip contraction and symmetry then give strict width
  \(y_*\) at the center for every sufficiently large \(X\).
- **Common time.** On \(1\le tL_x\le C,\ 0<t\le1/2,\ y_*\le y\le9/8\)
  inherit the order of constants from Note12. Prove the analogous
  bound \(At+B_D(1+L_x)x^{-\kappa}\), with \(D=C+1\) and
  \(C\ge\max(8,C_P)+1\) fixed before the provider constants.
  Pay \(At\le AC/L_x\). Choose an unevaluated finite \(L_*\) above
  the provider gates so \(33[AC/L_x+B_D(1+L_x)x^{-\kappa}]\le1/64\)
  for \(L_x\ge L_*\). With \(t_0=1/L_*\), the transition range
  controls all \(0<t\le t_0\) and \(x\ge4\pi e^{1/t}\) up to
  \(tL_x=C\). Beyond that point apply the same published all-real
  theorem as E05. Symmetry covers negative \(x\) and negative \(y\).
  The candidate is strict width \(y_*\) on the full spatial tail
  at each such single time. No uniform interval of untouched
  small heights follows as \(t\downarrow0\).

The relative-error threshold uses an independent carrier floor;
a geometric change using this same uniform error acquires no
additional arithmetic margin. Finite-height and intermediate
barriers and time zero remain separate.

## 4. Control premises

Apply [controls12][r12] to the unchanged canonical source and field.
Euler-factor and translated controls lose the full unit-coefficient
RS identification. Weighted-square, finite-tail and finite-prime
controls lack complete coefficients jointly with full reflection.
Reflected super-Gaussian and smooth/primitive controls lack the
theta arithmetic square expansion. Finite-profile and compact/atomic
sources do not identify the complete coefficients and field.
RH-conditional endpoint controls lack ordinary Dirichlet arithmetic.
Variable readouts lose the actual cosine/Newman equation. Relaxed
positive measures lack the exact integer divisor identification.
A freely changed phase also loses the exact logarithmic derivative
model. If the comparison carrier is nonzero at a control zero,
the relative error there is 1. The witness must lie in the claimed
domain for this check.

[packet]: ../research-progress/handoffs/GNP-BB-B04-r1.md
[e02]: 09_GNP_BB_E02_SIGNED_TAIL_WIDTH_20261113.md
[e03]: 10_GNP_BB_E03_ENVELOPE_ENDPOINT_AND_WIDTH_20261113.md
[e05]: 12_GNP_BB_E05_COMMON_TIME_TAIL_20261113.md
[check]: ../numerics/10_gnp_bb_b04_pair_search.py
[record]: ../numerics/10_GNP_BB_B04_PAIR_SEARCH_20261113.json
[mv]: https://personal.science.psu.edu/rcv4/571s25/montgomery-vaughanII.pdf
[src]: ../references/02_GNP_BB_SIGNED_TAIL_SOURCE_USE_20261113.md
[results]: ../../../../../result-summaries/README.md
[avoid]: ../../../../../avoid/README.md
[r11]: ../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md
[r12]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[a16]: ../../../../../avoid/16_unchecked_imports_and_novelty_claims.md
