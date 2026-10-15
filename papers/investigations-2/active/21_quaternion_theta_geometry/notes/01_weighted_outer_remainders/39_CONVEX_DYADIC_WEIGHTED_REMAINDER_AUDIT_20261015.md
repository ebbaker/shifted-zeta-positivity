---
research_program: PR01
secondary_programs: [PR03, COORD]
status: proved-bookkeeping-and-bounded-audit
---

# Convex dyadic summation and the bounded five-pair audit

15 October 2026, America/New_York. Prepared for Edward Baker with substantial LLM assistance. Recorded parent model **gpt-6-astra**, reasoning effort **ultra**, verified by the coordinating conversation. This is incremental research with internal LLM checking, not external refereeing or formal verification.

This continues [Note 32](../32_CLOSED_STRIP_EXTENSION_AND_MIDDLE_BLOCK_LEMMA_20261014.md), [Note 33](../33_RESEARCH_PRIORITIES_WEIGHTED_REMAINDERS_AND_SIGNED_CUSP_20261014.md), and [the continuation task](../00_research_coordination/37_OCTONIONIC_CORRELATION_INTEGRATION_AND_CONTINUATION_20261015.md). It uses exactly the five arithmetic inputs already audited in Note 32. No new exponent pair is imported or searched for.

The concrete improvement is a sharper summation of the existing block bounds:

\[
 \sum_{Y<n\le N_{\rm RS}}(\log n)^r
       e^{t\log^2 n/4}n^{-w_\pm(z)}
 =O_r\!\left(\ell^r e^{-\ell/20000}\right),
 \qquad Y=e^{\ell/5}.                                      \tag{1}
\]

Note 32 has an additional factor \(\ell\) on its right side. The improvement holds on exactly its existing shrinking discs and declared domain \(\theta\ge61/24\), \(0<t\le1/2\), at sufficiently large height. The stronger saved exponent \(m=76399/1273600000\) can replace \(1/20000\). The imported implied constants and starting height remain unevaluated. The overall analytic comparison still has its existing \(O(\Gamma/L)\) low-index error. There is **no new sign domain, finite bridge, or RH conclusion**.

## 1. Exact dyadic grid and the endpoint budget

Use all notation, hypotheses, and imported maximal-interval estimates of Note 32. In particular, \(\ell=\log(\Re z/(4\pi))\), \(\beta=\log M/\ell\), \(w=\sigma+i\tau\), and \(T=|\tau|\). The real observation is \(\theta=t\log(x/(4\pi))\); on the disc write \(\theta_u=t\ell\). Put

\[
 \theta_*=61/24,\qquad \rho=\eta=1/100000,
 \qquad \mu_*={21807\over254720000}.
\]

After the same increase in starting height as Note 32, we have
\(\theta_u\ge\theta_*-\rho\),
\(\sigma\ge1/2+\theta_u/4-\delta\), \(0\le\delta\le\rho\).
The exponent-pair estimate, the monotonicity of the actual heat weight, and exact Abel summation bound each block by

\[
 C_r\ell^r
 \exp\!\left\{\ell\left[
 F_{k,l}(\beta;\theta_u)+\delta\beta+\eta\right]\right\},
 \quad
 F_{k,l}(\beta;\theta)=
 k+(l-k-1/2)\beta-\frac\theta4\beta(1-\beta).                 \tag{2}
\]

Here one common \(C_r\) absorbs the largest of the five imported constants, the bounded conversion \(T/e^\ell\), and the fixed-order log-weight bound. It is independent of \(x,t\) on the stated domain, but it is not evaluated in this note. The statement that the geometric factor below is less than 1435 is **not** a claim that \(C_r\le1\).

Use the exact grid

\[
 M_q=Y2^q,\qquad
 \beta_q=1/5+q\log 2/\ell,
\]

retaining \(q\ge0\) for which \(M_q<N_{\rm RS}\). Its blocks are
\((M_q,\min(2M_q,N_{\rm RS})]\). Real, noninteger first endpoints cause no change: the imported estimate applies to every integer interval contained in \((M,2M]\), and the empty interval contributes zero. No endpoint is rounded or differentiated.

Assign a block according to its **left endpoint** \(\beta_q\), using the half-open versions of Note 32's five intervals (and closing the last endpoint):

\[
 [1/5,3/10],\quad[3/10,3/8],\quad[3/8,81/200],
 \quad[81/200,3/7],\quad[3/7,1/2].                         \tag{3}
\]

Use \(A^2P,AP,D,R,P\), respectively. A block may cross the right boundary of its assigned interval; the maximal-interval estimate is already valid on the entire block, so this costs nothing and does not omit any terms. The exact shortened final block is included.

For \(\beta\in[1/5,1/2]\), the disc/time displacement and real-part loss satisfy

\[
 F_{k,l}(\beta;\theta_u)+\delta\beta+\eta
 \le F_{k,l}(\beta;\theta_*)
          +\rho/16+\rho/2+\eta.                           \tag{4}
\]

Also \(\log N_{\rm RS}/\ell\le1/2+O(1/(u\ell))\). Thus there is at most one grid point above \(1/2\) at large height. Assign it to \(P\); the extra perturbation is at most \(\rho\), as in Note 32, uniformly even when \(\theta_u\le\ell/2\) grows. This isolated block is paid separately below. It is harmless to reserve this extra \(\rho\) for every block and use the common margin

\[
 m=\mu_*-\rho(1+1/2+1/16+1)
   ={76399\over1273600000}>{1\over20000}.                  \tag{5}
\]

## 2. Convexity pays the dyadic block count

Let \([a,b]\) be any interval in (3), \(\Delta=b-a\), and use its assigned pair. The exact quadratic identity is

\[
 F(\beta;\theta_*)=
 \frac{b-\beta}{\Delta}F(a;\theta_*)+
 \frac{\beta-a}{\Delta}F(b;\theta_*)
 -\frac{\theta_*}{4}(\beta-a)(b-\beta).                    \tag{6}
\]

Both endpoint values are at most \(-\mu_*\), by Note 32's rational table. For \(d(\beta)=\min(\beta-a,b-\beta)\),
\((\beta-a)(b-\beta)\ge\Delta d(\beta)/2\). Equations (4)–(6) therefore give

\[
 F(\beta;\theta_u)+\delta\beta+\eta
 \le -m-c_\Delta d(\beta),
 \qquad c_\Delta={\theta_*\Delta\over8}
              ={61\Delta\over192}.                       \tag{7}
\]

On each half of the interval, successive grid points have distances from the nearest endpoint differing by exactly \(h=\log2/\ell\). The first distance need not be zero; replacing it by zero only enlarges the positive majorant. Consequently

\[
 \sum_{\beta_q\in[a,b]}e^{-\ell c_\Delta d(\beta_q)}
 \le {2\over1-2^{-c_\Delta}}.                              \tag{8}
\]

One may assign a midpoint to either half; double-counting it in this upper bound is harmless. This proves the bound for shifted grids as well as grids landing exactly on an interval endpoint.

The five widths are

\[
 \Delta_i\in\{1/10,3/40,3/100,33/1400,1/14\}.
\]

Including the possible exceptional block above \(1/2\), the geometric summation factor is at most

\[
 G=1+2\sum_{i=1}^5{1\over1-2^{-c_{\Delta_i}}}.
\]

For \(v>0\), \((1-e^{-v})^{-1}\le1+v^{-1}\); also \(\log2>1/2\). Hence

\[
 G<11+4\sum_i{1\over c_{\Delta_i}}
   =11+{768\over61}\sum_i{1\over\Delta_i}
   ={962773\over671}<1435.                                \tag{9}
\]

The unsummed bound (2), (7)–(9), and the single exceptional block now give the explicit form

\[
 \left|\sum_{Y<n\le N_{\rm RS}}(\log n)^r
 e^{t\log^2 n/4}n^{-w}\right|
 \le {962773\over671}\,C_r\ell^r e^{-m\ell},               \tag{10}
\]

after increasing height as already allowed. This proves (1). The original block-count bound and (10) can also be minimized against one another; the geometric bound need not be the smaller one at moderate height.

The proof treats each of the two branches separately, so it preserves both branches and their full approximation errors. It does not posit cancellation between dyadic blocks or replace the heat weight by an unweighted sum. All the low-index, ordinary-zeta-tail, and imported approximation terms from Note 32 remain to be paid.

## 3. The exact bottleneck of these five limiting pairs

This finite audit clarifies the scope of the improvement. The lower envelope of the five affine functions
\(k+(l-k-1/2)\beta\) on \([1/5,1/2]\) uses the same pair order, with exact adjacent transition points

\[
 {1430\over4789},\quad {362\over957},\quad
 \beta_c={62831\over155153},\quad {3\over7}.                \tag{11}
\]

Endpoint comparison proves this lower-envelope assertion: pair differences are affine. For any one pair set

\[
 q_{k,l}(\beta)=
 {4\{k+(l-k-1/2)\beta\}\over\beta(1-\beta)}.
\]

Writing \(c=l-k-1/2\ge0\), the sign of \(q'\) is the sign of
\(c\beta^2+2k\beta-k\), whose derivative is positive for \(\beta>0\). Thus \(q\) has at most one interior turning point, a minimum; its maximum on each envelope interval is at an endpoint. Exact endpoint evaluation gives

\[
 \max_{1/5\le\beta\le1/2}\min_{(k,l)}q_{k,l}(\beta)
 =\theta_c={4911678521\over1933561194}
 \approx2.5402239847600088,                                \tag{12}
\]

attained where \(D\) meets \(R\), at \(\beta_c\). The crossover and its threshold were already recorded by Note 32’s checker; the present calculation places that value in the full bounded-envelope audit. This is a limiting threshold for these five blockwise majorants. Their required positive exponent losses preclude taking (12) as a proved closed-boundary sign theorem. No threshold change is claimed here.

At \(\theta=5/2\), the failure of these bounds occupies a full interval, not just \(\beta=2/5\). The \(A^2P\) quadratic has roots \(4/23,13/45\). The \(P\) quadratic has lower root

\[
 \beta_P={105-\sqrt{105}\over210}
         \approx0.45120499635.
\]

The \(AP,D,R\) quadratics have negative discriminants and positive leading coefficient, so they are positive everywhere. It follows that **all five** bounds have strictly positive weighted exponent throughout

\[
                13/45<\beta<\beta_P.                      \tag{13}
\]

At \(\beta=2/5\), the least of them is still \(9/3980>0\). Convex summation removes a block-count factor where a negative margin already exists; it does not remove this positive power. A direct weighted cancellation or a new source-specific estimate remains necessary to cross this obstruction using this framework. This is not an obstruction to the actual sum or to other arithmetic methods.

## 4. Effective-height meaning and validation

Equation (10) improves a sufficient error budget but does not evaluate \(C_r\), the disc starting conditions, the low-index constant, carrier differentiation errors, or the imported approximation constants. No verified effective \(X_*\) results.

For scale only, if the coefficient \(C_0\) in (10) were one and this were the sole error, making the right side at most \(1/8\) would be ensured by
\(\ell\ge20000\log(8\cdot962773/671)\), approximately 186965. Keeping \(m\) instead gives approximately 155839. These are illustrations of this conservative sufficient budget, not lower bounds on the true starting height and not validated jet thresholds. The corresponding heights remain far beyond the finite cover through 112. The next effective-height task is to evaluate the genuine constants or obtain a much stronger remainder, rather than commission a finite bridge from this illustration.

The [checker](../../numerics/check_convex_dyadic_weighted_remainder.py) and [receipt](../../numerics/CONVEX_DYADIC_WEIGHTED_REMAINDER_CHECKS_20261015.json) record **129 exact rational assertions**: endpoint margins, quadratic identities, perturbation arithmetic, geometric constant, lower-envelope coverage, limiting threshold, and the obstruction at five halves. They do not verify the imported arithmetic theorems, the analytic geometric-series proof, or any finite-height sign observation. The exact proof above supplies the interval and infinite-sum reasoning.

From the repository root:

    python3 papers/investigations-2/active/21_quaternion_theta_geometry/numerics/check_convex_dyadic_weighted_remainder.py --output /tmp/inv21-convex-dyadic-replay.json

The result is a PR01 bookkeeping improvement and a bounded audit. PR02-CORR remains the preferred investigation of a new signed source mechanism; the full stationary observations and small-energy collision target are unchanged.
