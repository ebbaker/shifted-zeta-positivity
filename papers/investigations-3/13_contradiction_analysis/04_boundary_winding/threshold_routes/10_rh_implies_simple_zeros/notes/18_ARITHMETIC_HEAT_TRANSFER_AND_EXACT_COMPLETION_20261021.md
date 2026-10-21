# Sharp arithmetic heat repair and exact completion obstructions

21 October 2026; continuation begun 20 October. Prepared for **Edward Baker**
with substantial LLM assistance. Actual recorded model **gpt-6-astra**,
reasoning effort **ultra**. Same-model internal derivation and review;
no specialist validation or novelty claim. Checkpoint:
`6edecb68ae6e2e095e788f0901d39373851d6412`.

This note strengthens two quantitative comparisons from
[Note 17](17_NORMALIZED_HEAT_GLOBAL_LIMIT_AND_ARITHMETIC_COSTS_20261020.md).
Under RH and the internally proved complete estimates of
[Note 16](16_GEVREY_GLOBAL_APPROXIMATION_AND_RATE_20261020.md), §§1–5 compute
the sharp first-order cost of transferring a normalized heat profile back
to the original zeta norm, over fixed finite filtered-Gevrey families.
Sections 6–10 prove unconditionally that exact first-mode heat
normalization, including the specified contour prescriptions, still has
no ordinary Dirichlet series at any fixed positive time. These are scoped
obstructions with explicit constants, not new exclusion criteria.

The [result index](../../../../../../../result-summaries/README.md),
[avoid index](../../../../../../../avoid/README.md),
[complete-payment rule](../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md)
and [gain-before-expansion rule](../../../../../../../avoid/20_volume_without_a_gain.md)
govern the comparison. The retained cost, rather than a reformulation of
the desired sign, is the new result. No original zero is excluded.

## 1. The finite heat operation is exact

Assume RH and fix a real normalized compact Gevrey extension W of
order 1<sigma<2, with w=W|[0,1], as in Note 16. Use the unchanged convention
\[
 V_{N,w}(s)=\sum_{n\le N}\mu(n)n^{-s}w(\log n/L),\qquad L=\log N.
\]
For fixed v>=0, finite differentiation gives exactly
\[
 \exp\!\left(\frac{v}{4L^2}\partial_s^2\right)V_{N,w}(s)
 =\sum_{n\le N}\mu(n)n^{-s}e^{v(\log n/L)^2/4}w(\log n/L)
 =V_{N,w_v}(s),\quad w_v(u)=e^{vu^2/4}w(u).
 \tag{CT1}
\]
There is no infinite Euler-series heat interchange here. The original
target remains zeta and the original weight remains (1/4+t^2)^(-1).
Multiplication by this entire factor preserves every fixed compact
Gevrey order 1<sigma<2, normalization w_v(0)=1, and flatness at 1.
The inverse factor does the same. Thus varying all permitted tapers
after this operation does not create a new class.

For each fixed v, Note 16's complete theorem applies literally:
\[
 \lim_N L\|1-\zeta V_{N,w_v}\|_{\mathcal H}^2
 =\sum_{\rho\ {\rm distinct}}\frac{\|q_{m_\rho,v,w}\|_2^2}{|\rho|^2},
 \quad q_{m,v,w}=-(e^{vu^2/4}f_m)^{(m)},\quad
 f_m=\frac{u^{m-1}w}{(m-1)!}.
 \tag{CT2}
\]
Here ||g||_H^2=(2pi)^(-1) int_R |g(1/2+it)|^2/(1/4+t^2) dt,
and ||.||_2 means L2(0,1). All ordinates, signs and multiplicities occur.

Write T_tau for Note 17's exact carrier-normalized target. Its profile
with the original taper is
\[
 h_{m,v,w}=-\sum_{k=0}^{\lfloor m/2\rfloor}
       \frac{m!}{k!(m-2k)!}(v/4)^k f_m^{(m-2k)}.
 \tag{CT3}
\]
It is different from q. The two complete scaled-tail theorems, followed
by the compact cross term (or polarization), give the actual limit
\[
 \lim_N L\|\zeta V_{N,w_v}-T_{v/L^2}V_{N,w}\|_{\mathcal H}^2
 =\sum_\rho\frac{\|q_{m_\rho,v,w}-h_{m_\rho,v,w}\|_2^2}{|\rho|^2}.
 \tag{CT4}
\]
The square of a difference is at most twice the two squared errors;
therefore the full height tail, not only finite-height polarization, is paid.

## 2. An explicit defect in the natural coefficient transfer

At one fixed zero order m, direct differentiation of the finite profile
formulas gives
\[
 \left.\partial_v(q_{m,v,w}-h_{m,v,w})\right|_{v=0}
 =-\tfrac14\{u^2f_m^{(m)}+2mu f_m^{(m-1)}\}.
 \tag{CT5}
\]
For m=1 the term involving f_m^(m-2) in CT3 is absent; CT5 still holds.
The lower-derivative terms cancel exactly, leaving the two displayed
Leibniz terms. Since f_m^(m-1)(0)=1 and f_m^(m) is bounded near 0, the
braces equal 2m u+O(u^2). Consequently this derivative is not zero for
any normalized fixed taper. In particular coefficient heat introduces
a transfer cost even at a simple zero, where numerator heat leaves
the first-order local profile unchanged.

## 3. The least possible arithmetic repair of a fixed heat profile

Let P_{m-1} be the polynomial subspace of degree less than m in L2(0,1),
Pi_m its orthogonal projection, and K_m its endpoint reproducing kernel:
int_0^1 K_m(u)P(u)du=P(0), ||K_m||_2^2=m^2. For any normalized arithmetic taper its
profile p satisfies
\[
 \int_0^1u^j p(u)du=\mathbf1_{j=0}\quad(0\le j<m),
 \quad\text{equivalently}\quad \Pi_m p=K_m.
 \tag{CT6}
\]
The same holds for complex fixed multiplier mixtures whose multipliers
sum to one, as in Note 16 AD. Therefore the squared distance of a
specified h=h_m,v,w to the full affine moment space is exactly
\[
 \delta_{m,v}(w)^2:=\|K_m-\Pi_m h\|_2^2,
 \qquad p_* =h+K_m-\Pi_m h.
 \tag{CT7}
\]
This is a correction cost, not the assertion ||p||>=m in new notation.
It identifies precisely the part of the numerator-heat profile that
no original arithmetic taper can retain.

The distance is sharp in the closure of the allowed real flat Gevrey
tapers. To verify that point, p_* is real Gevrey. Solve
\[
 f^{(m)}=-p_*,\quad f^{(j)}(0)=0\ (j<m-1),\quad f^{(m-1)}(0)=1.
 \tag{CT8}
\]
CT6 implies f^(j)(1)=0 for every j<m: integrate against (1-u)^k
for k=0,...,m-1. Multiply f by a fixed-order flat Gevrey cutoff which
equals one away from a terminal layer of width eta and vanishes near 1.
Because f^(j)(u)=O((1-u)^(m-j)) there for j<=m, the change in its mth
derivative is uniformly bounded and supported on that layer. Hence its
L2 norm tends to zero. The quotient (m-1)!f(u)/u^(m-1) is removable at
zero with value one and is Gevrey, as follows also from the integral
formula for CT8; use a compact negative-side cutoff for its extension.
The repaired profiles keep CT6 exactly. Orthogonality therefore gives
\[
 \|p_\eta-h\|_2^2
   =\delta_{m,v}(w)^2+\|p_\eta-p_*\|_2^2
   =\delta_{m,v}(w)^2+O(\eta).
 \tag{CT9}
\]
No positivity or monotonicity restriction on the taper is imposed.

The cost has a finite explicit matrix formula. Write
R=p_m,w-h_m,v,w and b_j=int u^j R(u)du, 0<=j<m, and let
G_m=(1/(i+j+1))_{0<=i,j<m} be the Hilbert Gram matrix. Then
\[
 \delta_{m,v}(w)^2=b^*G_m^{-1}b.
 \tag{CT10}
\]
For a double zero put I_j=int_0^1 u^j(uw(u))du, j=0,1. Since
R=(v/2)uw,
\[
 \boxed{\delta_{2,v}(w)^2
 =\frac{v^2}{4}(4I_0^2-12I_0I_1+12I_1^2).}
 \tag{CT11}
\]

There is also a simple uniform consequence at a specified profile:
\[
 \delta_{m,v}(w)^2\ge
        (m-\|h_{m,v,w}\|_2)_+^2.
 \tag{CT12}
\]
Thus any double numerator-heat profile of squared norm C<2 requires
correction greater than (2-sqrt(2))^2 at that location. Its contribution
to the actual scaled transfer norm is divided by |rho|^2; the conjugate
pair contributes twice this amount. This applies also to the nonmonotone
low-cost profiles of Note 16 HD.

## 4. An exact finite-separation example

At a=pi, v=2pi^2, take the order-two closure profile
\[
 f(u)=\frac{(1-u)\sin(\pi u)}\pi,\qquad
 w(u)=f(u)/u,\qquad h=-f''-\pi^2f=2\cos(\pi u).
\]
Its heat cost is ||h||_2^2=2. Its moment deficit is
b=(1,4/pi^2), since int h=0 and int u h=-4/pi^2. Thus
\[
 \delta^2=4-\frac{48}{\pi^2}+\frac{192}{\pi^4},\qquad
 p_*=2\cos(\pi u)+4-\frac{24}{\pi^2}
                +\left(-6+\frac{48}{\pi^2}\right)u,
\]
\[
 \|p_*\|_2^2=6-\frac{192}{\pi^4}>4.
 \tag{CT13}
\]
This is the sharp least-distance repair, which need not minimize the
repaired profile's own norm. The first expression is strictly larger
than the triangle lower allowance (2-sqrt(2))^2. It measures the full
two-moment mismatch, not just a norm mismatch.

The displayed w is understood through fixed flat Gevrey cutoffs of f
near 1: f(0)=0, f'(0)=1, f(1)=f'(1)=0, so both heat profiles and their
moment projections converge in L2. Take N to infinity for each fixed
cutoff before the cutoff width decreases. These are actual local norm
coefficients; a contribution at rho is divided by |rho|^2 and a conjugate
pair contributes twice. No full-height limit as this base cutoff moves
is asserted. For each fixed cutoff the complete result below applies.

## 5. Paying the complete repair and making its constant sharp

Let D_N be a fixed finite multiplier family from Note 16 AD:
\[
 D_N=\sum_{j=0}^J A_j(s)V_{\lfloor N/M\rfloor,w_j}(s),
 \quad \sum_j A_j\equiv1,
 \tag{CT14}
\]
with fixed finite Dirichlet multipliers supported through M and fixed
normalized Gevrey tapers. Its profile at rho is
q_rho=sum A_j(rho)p_mrho,wj. The mixed compact limits and the complete
ST/CN tails prove
\[
 \mathcal T(D;v,w):=\lim_N L
 \|\zeta D_N-T_{v/L^2}V_{N,w}\|_{\mathcal H}^2
 =\sum_\rho\frac{\|q_\rho-h_{m_\rho,v,w}\|_2^2}{|\rho|^2}.
 \tag{CT15}
\]
Indeed L/log floor(N/M) tends to one, each fixed multiplier is bounded
on the critical line, and the square of the mixed error is bounded by
a fixed finite sum of the already paid errors. No tail constant uniform
over growing filter complexity is presumed.

Within this declared family class the exact optimal transfer constant is
\[
 \boxed{\inf_D\mathcal T(D;v,w)
  =\Delta_v(w):=\sum_\rho
       \frac{\delta_{m_\rho,v}(w)^2}{|\rho|^2}<\infty .}
 \tag{CT16}
\]
For the lower bound, apply CT7 at every zero. For finiteness and the
upper bound, use the original w as baseline. Its complete transfer
constant B=sum ||p_m,w-h_m,v,w||^2/|rho|^2 is finite by ST/CN, and
each delta^2 is at most the corresponding baseline cost. Choose a
finite conjugate-symmetric set F leaving baseline tail below epsilon.
At each member select a fixed flat taper from CT9 with total excess
below epsilon. The bounded two-prime filters of AD assign these finitely
many tapers and converge pointwise to the baseline at every other zero.

Their complete profile majorant is
C_J(||h_m,v,w||^2+sum_{j=0}^J ||p_m,w_j||^2)/|rho|^2,
where j=0 explicitly includes the baseline w_0=w as well as every
selected taper. The baseline coefficient is 1-sum P and is bounded
by J+1 independently of filter degree. It is summable by ST/CN and independent of filter degree.
Dominated convergence therefore pays the whole filter limit. First N
tends to infinity for each fixed filter; then its degree increases.
The resulting cost is at most Delta+2epsilon. Let epsilon decrease.
Conjugate pairing of targets and filters gives real coefficients if
desired. This proves CT16 without an effective N threshold or a moving
taper assertion. Exact finite filters from Note 16 EF may be used in
place of the bounded peaks, with the same ordered tail payment.

## 6. Exact first-mode contribution and the conclusion

Put
\[
 A(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2),\qquad
 X_t(s)=8H_t(-2i(s-\tfrac12)),\qquad X_0=\xi=A\zeta.
\]
Fix **\(t>0\)** and **\(c>1\)**. Define the entire function
\[
 B_t^c(s)=\frac1{\sqrt{\pi t}}
           \int_c^\infty e^{-(x-s)^2/t}A(x)\,dx.
 \tag{FM1}
\]
It is the exact \(n=1\) contribution from the region where the original
Euler series converges absolutely. It is positive on the real axis,
solves \(\partial_tB_t^c=\tfrac14\partial_s^2B_t^c\), and tends to
\(A(\sigma)\) as \(t\downarrow0\) for fixed real \(\sigma>c\).

As real \(\sigma\to+\infty\),
\[
 \boxed{\quad
 \frac{X_t(\sigma)}{B_t^c(\sigma)}-1
 =2^{-\sigma}e^{t(\log2)^2/4}
       \left(\frac{\sigma}{2\pi}\right)^{-t\log2/4}
       \left[1+O_{t,c}\!\left(\frac{\log\sigma}{\sigma}\right)\right].
 \quad}
 \tag{FM2}
\]
This quotient has no representation by an ordinary Dirichlet series
converging in a right half-plane, even conditionally. The same conclusion
and asymptotic hold for either horizontal-contour heat regularization
of \(A\) defined in §9, or any specified analytic normalizer differing
from (FM1) by \(O(e^{-\kappa\sigma^2})\), \(\kappa>0\), on this real ray.
Only eventual nonvanishing on that ray is needed; no global zero-free
property of the normalizer is claimed.

## 7. A genuinely convergent mode decomposition

The complete theta Gaussian identity, proved in Note 17 (RN4), is
\[
 X_t(s)=\frac1{\sqrt{\pi t}}
              \int_{\mathbb R}e^{-(x-s)^2/t}\xi(x)\,dx.
 \tag{FM3}
\]
The source normalization is [Polymath15, equations
(1)–(4)](https://arxiv.org/html/1904.12438v2#S1). The Gaussian identity
uses the complete entire \(\xi\), so no completion pole has been crossed
in (FM3). On the real axis it is exactly (RN4) after a real translation.
Both sides are entire in \(s\), by Gaussian domination on compact sets,
so the identity theorem gives the displayed complex-\(s\) version.
Split this integral at \(c\), writing its left part as
\(Q_t^c(s)\). On \(x\ge c\), the positive absolutely convergent Euler
series and Gaussian domination justify summation under the integral.
Completing the square for each fixed \(n\) gives the exact identity
\[
 X_t(s)=Q_t^c(s)+\sum_{n\ge1}
 n^{-s}e^{t(\log n)^2/4}
 B_t^c\!\left(s-\frac t2\log n\right).
 \tag{FM4}
\]
The series in (FM4) converges absolutely and locally uniformly for every
complex \(s\): before completing the square it is bounded on each compact
set by an integrable Gaussian times \(A(x)\zeta(c)\). The displayed
coefficients depend on \(s\); (FM4) is not an ordinary Dirichlet series.

The entire left contribution is paid, including all negative real
arguments. Setting \(u=c-x\ge0\), for real \(\sigma\ge c\),
\[
 \begin{split}
 |Q_t^c(\sigma)|
 &\le\frac{e^{-(\sigma-c)^2/t}}{\sqrt{\pi t}}
 \int_0^\infty e^{-u^2/t}|\xi(c-u)|\,du\\
 &\ll_{t,c} e^{-(\sigma-c)^2/t}.
 \end{split}
 \tag{FM5}
\]
The omitted factor \(e^{-2(\sigma-c)u/t}\) is at most one. The remaining
integral is finite by the real functional equation and Stirling growth
\(|\xi(c-u)|\le\exp(O_c((u+1)\log(u+2)))\). Thus (FM5) does not
discard a left-side remainder or appeal to a formal heated Euler series.

## 8. A fixed-shift estimate pays the whole remaining Euler tail

Write \(g(x)=\log A(x)\) for real \(x>1\). The
[digamma and Stirling expansions](https://dlmf.nist.gov/5.11#E2), with the
[convergent trigamma series](https://dlmf.nist.gov/5.15#E1) for the derivative bound, give
\[
 g'(\sigma)=\tfrac12\log(\sigma/(2\pi))+O(\sigma^{-1}),
 \quad
 \sup_{|x-\sigma|\le(\log\sigma)^2}|g''(x)|=O(\sigma^{-1}).
 \tag{FM6}
\]
The same Gaussian localization used for (RN6)–(RN10), now with
\(A(x)\) only on \(x\ge c\), gives, with \(a=g'(\sigma)\),
\[
 B_t^c(\sigma)=A(\sigma)e^{ta^2/4}
          \left[1+O_{t,c}(\log^2\sigma/\sigma)\right],
 \qquad
 \mathbb E_{t,\sigma}|x-\sigma|=O_{t,c}(\log\sigma).
 \tag{FM7}
\]
Here the expectation has positive density proportional to
\(\mathbf1_{x\ge c}e^{-(x-\sigma)^2/t}A(x)\).
For clarity, use the cutoff \(|x-\sigma|\le(\log\sigma)^2\), Taylor
expand \(g\) as \(g(\sigma)+a(x-\sigma)+O((x-\sigma)^2/\sigma)\),
and tilt the Gaussian to mean \(ta/2\). Its second moment is
\(O_t(\log^2\sigma)\). The complementary integrals, also with a factor
\(|x-\sigma|\) or \(|g'(x)|\), are
\(O_{t,c}(A(\sigma)e^{-c_t\log^4\sigma})\): on \([c,\infty)\),
\(A(x)/A(\sigma)\le C_c\exp(C_c|x-\sigma|\log(\sigma+|x-\sigma|+2))\),
and \(|g'(x)|\ll_c\log(x+2)\). This supplies both estimates in (FM7)
and the derivative-tail payment needed next.

To get the sharper shift error, do not differentiate the error in (FM7).
Integration by parts gives exactly
\[
 (B_t^c)'(\sigma)=
 \frac{A(c)}{\sqrt{\pi t}}e^{-(\sigma-c)^2/t}
 +\frac1{\sqrt{\pi t}}\int_c^\infty
             e^{-(x-\sigma)^2/t}A'(x)\,dx.
 \tag{FM8}
\]
On the central interval, (FM6) bounds
\(|g'(x)-g'(\sigma)|\ll|x-\sigma|/\sigma\). Equations (FM7)–(FM8)
and their paid complementary tails prove
\[
 (\log B_t^c)'(\sigma)
   =\tfrac12\log(\sigma/(2\pi))
          +O_{t,c}(\log\sigma/\sigma).
\]
Hence for each fixed real \(\delta\),
\[
 \frac{B_t^c(\sigma-\delta)}{B_t^c(\sigma)}
 =\left(\frac{\sigma}{2\pi}\right)^{-\delta/2}
       \left[1+O_{t,c,\delta}(\log\sigma/\sigma)\right].
 \tag{FM9}
\]

For real \(x\ge c\),
\[
 0\le\zeta(x)-1-2^{-x}
   \le 3^c\zeta(c)\,3^{-x}.
 \tag{FM10}
\]
Thus the entire \(n\ge3\) contribution in (FM4), divided by
\(B_t^c(\sigma)\), is bounded by
\[
 3^c\zeta(c)\,3^{-\sigma}e^{t(\log3)^2/4}
       \frac{B_t^c(\sigma-\tfrac t2\log3)}{B_t^c(\sigma)}
 =O_{t,c}\!\left(3^{-\sigma}\sigma^{-t\log3/4}\right).
 \tag{FM11}
\]
Only the two fixed shifts in (FM9) have been used; there is no
unjustified all-\(n\) uniform asymptotic. The \(n=2\) term, (FM5),
(FM7) and (FM11) prove (FM2).

If an ordinary Dirichlet series \(\sum d_nn^{-s}\) converges at a real
point, boundedness of its terms gives absolute convergence farther
right, as in (RN12). Its first two terms therefore satisfy
\[
 D(\sigma)=d_1+d_2\,2^{-\sigma}+O(3^{-\sigma}).
 \tag{FM12}
\]
Equation (FM2) forces \(d_1=1\) and \(d_2=0\), since
\(2^\sigma(X_t/B_t^c-1)\to0\). But its nonzero positive main term is
not \(O(3^{-\sigma})\). This contradiction proves the claimed ordinary
Dirichlet-series exclusion, including conditional convergence.

## 9. Actual contour regularizations belong to the same excluded class

For any fixed real \(\eta\ne0\), define
\[
 B_{t,\eta}(s)=\frac1{\sqrt{\pi t}}
       \int_{\mathbb R+i\eta}e^{-(z-s)^2/t}A(z)\,dz,
 \tag{FM13}
\]
with left-to-right orientation. This is an absolutely convergent entire
heat solution. At positive real infinity use ordinary sectorial
Stirling. At negative real infinity use
[gamma reflection, DLMF 5.5.3](https://dlmf.nist.gov/5.5#E3):
\(|\sin(\pi(x+i\eta)/2)|\ge\sinh(\pi|\eta|/2)>0\), while
\(\Gamma(1-(x+i\eta)/2)\) lies in a right-half-plane Stirling sector.
Consequently \(|A(x+i\eta)|\le
\exp(O_\eta((|x|+1)\log(|x|+2)))\) on the full line, which the
Gaussian dominates locally uniformly in \(s\). Differentiation under
the integral proves its heat equation.

Deform only the part of the contour with \(\Re z\ge c\) to the real
ray \([c,\infty)\); that region contains no pole. The difference from
(FM1) consists of the left horizontal ray and the finite vertical
segment at \(c\). For real \(\sigma\ge c\), their Gaussian moduli
are bounded by the factor \(e^{-(\sigma-c)^2/t}\) times an integrable
function independent of \(\sigma\), exactly as in (FM5), with the
additional harmless factor \(e^{\eta^2/t}\). Thus
\[
 B_{t,\eta}(\sigma)-B_t^c(\sigma)
       =O_{t,c,\eta}(e^{-(\sigma-c)^2/t}).
 \tag{FM14}
\]
By (FM7), these functions are nonzero for all sufficiently large real
\(\sigma\), and (FM14) changes (FM2) only by a Gaussian-small term.
The upper and lower prescriptions, and their real symmetric average,
therefore all fail the ordinary Dirichlet-series test. Contours with
different nonzero heights of the same sign give the same function by
deformation within that half-plane; uniqueness across the poles is not
assumed. More generally the same argument applies to any analytic
normalizer \(\widetilde B\) satisfying
\(\widetilde B(\sigma)-B_t^c(\sigma)=O(e^{-\kappa\sigma^2})\)
for some fixed \(\kappa>0\). This is an explicit class, not a claim
about arbitrary regularizations.

## 10. Meaning for heat-to-arithmetic transfer

Exact removal of the first mode does remove Note 17's algebraic
\(\log^2\sigma/\sigma\) defect. It leaves a different, quantified
defect: the second mode has a power of \(\sigma\) multiplying its
\(2^{-\sigma}\) scale, incompatible with a constant Dirichlet coefficient.
For \(B=B_t^c\) or \(B=B_{t,\eta}\), numerator and denominator solve the
same heat equation. The completion drift is visible in their exact
quotient equation, wherever \(B\) is nonzero:
\[
 \partial_t(X_t/B)=\tfrac14\partial_s^2(X_t/B)
       +\tfrac12(B'/B)\partial_s(X_t/B).
 \tag{FM15}
\]
Here \(B'/B\sim\tfrac12\log(\sigma/(2\pi))\) for the positive normalizer
(FM1) on the right ray. Equation (FM15) is not asserted for an arbitrary
analytic normalizer in the larger Gaussian-small comparison class unless
it also satisfies that heat equation.

For comparison, retaining constant coefficients and applying positive
heat directly to each bare exponential would prescribe
\(e^{t\log^2n/4}n^{-s}\), whose terms fail to tend to zero at every
fixed \(s\). The convergent opposite-sign series
\(\sum e^{-t\log^2n/4}n^{-s}\) is entire for fixed \(t>0\) and
solves the opposite heat equation. Neither observation substitutes for
the complete, genuinely convergent calculation (FM4)–(FM11).

All limits above keep \(t>0\), the cutoff and the contour fixed. They
give no uniform estimate as \(t=t_N\to0\), no assertion that a contour
normalizer is zero-free on the critical line, and no new approximation
norm or lower bound. In particular Note 17's critical-line norm theorem
is **not** asserted for \(X_t/B_t^c\), for \(X_t/B_{t,\eta}\), or for the
symmetric contour prescription. Their cutoff and contour terms require
their own boundary analysis. Thus these natural exact first-mode replacements
do not supply the missing transfer of a normalized heat gain to the
original zeta norm; other completions or a different coherent transfer
remain outside this result.

## 11. Scope, controls, and the next action

CT16 concerns fixed filtered-Gevrey families with their proved profiles;
it is not asserted for every arbitrary coefficient sequence depending
on N. It measures transfer to the changed target times the original
approximant, not a new infimum for approximating 1. The original
polynomial-infimum coefficient remains K=sum m_rho^2/|rho|^2; no
multiplicity-independent upper bound is produced.

The endpoint moment projection is a Hilbert-space fact and also holds
in the isolated polynomial double-zero control. Its purpose is to
quantify a transfer obstruction, so passing that control is expected.
The actual all-zero equalities CT4/CT15 use the unchanged zeta and
Möbius convolution; the Euler c=1 control and the source-only/modified
arithmetic controls do not satisfy that premise. No control is claimed
to be rejected by a new signed arithmetic estimate.

The next action changes concretely: moving the heat onto finite
coefficients must retain the correction CT10, and the simplest positive
coefficient heat already has the nonzero first variation CT5. A sub-two heat profile
cannot be transferred to the original norm with vanishing first-order
error. A proposed alternative must supply an opposing original-arithmetic
estimate after this correction; reusing the numerator-heat decrease is
insufficient. No RH endpoint multiplicity is excluded.

The [collision-control screen](../../../../../../../result-summaries/12_collision_controls_and_screening.md)
does not turn either result into an event exclusion. The local projection
calculation accepts polynomial collision controls. The complete CT
transfer uses the original reciprocal coefficients; Euler-factor
controls change them, weighted-square controls change the theta
coefficients, and the reflected/positive-primitive controls change the
source. The FM calculation likewise assumes the original identity
xi=A zeta and its unit Euler coefficients; it does not assert that every
control has the same first two modes. No new signed premise separating
the original multiple-zero endpoint has been obtained.

For BW09, the Gaussian and exact-normalization obstruction is reusable
without RH. The CT full-norm transfer theorem assumes original-zeta RH,
so it cannot provide BW09's RH contradiction. The original simplicity
and strict cap-surplus steps remain open. The
[internal review](../reviews/18_ARITHMETIC_HEAT_TRANSFER_AND_COMPLETION_REVIEW_20261021.md)
also records a bounded reread of the imported GC/ST premises, which is
not external validation of their strong RH-only conclusion. The succinct
canonical manuscript remains at its previous consolidation checkpoint.
