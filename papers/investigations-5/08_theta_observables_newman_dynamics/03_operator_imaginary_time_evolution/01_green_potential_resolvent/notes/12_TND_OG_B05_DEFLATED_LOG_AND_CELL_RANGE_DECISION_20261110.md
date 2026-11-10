# B05: deflated logarithms, Green cell ranges and acquisition cost

10 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance. Actual model and reasoning effort are absent
from accessible chat0008 capture metadata; neither is inferred from the
Astra recommendation. **Status: proved in-note from named inherited
inputs, with proof-author checking only; canonical feasibility unpaid.**

## 1. Decision and classification

The bounded two-method comparison is complete:

1. **Independent divisor-cell upper ranges:** retain them for reuse of
   an existing census. For acquiring exclusion on the same rectangle,
   their strict Green pass implies that the identical occupied cells
   already prove direct exclusion. This is a precise information-class
   dominance result, not a theorem about every zero-based algorithm.
2. **Zero-aware signed logarithmic integration:** retain a conditional
   product-integration route. Equations (5), (8), (12) and (15) replace
   E06's small-value envelope and both midpoint terms. They still require
   certified root information and an affordable regular-factor floor.
   Those canonical data and a matched cold-cost advantage are unacquired.

No theta field, roots or signed value are evaluated here. The one selected
successor is **[E] TND-OG-E07 — GPT-6.1 Sol**, a bounded analytical audit
of these claims, ready but unactivated. It is not a field-run request.

Under [avoid01][a01], the gains are **conditional quantitative acquisition
bounds and a scoped comparison**, not an RH-equivalent criterion or new
exclusion coverage. Read the [result index][results], especially
[heat/Green cluster11][heat] and [controls12][controls], and the
[avoid index][avoid], especially [premise screening02][a02],
[scope07][a07] and [known-region cost11][a11]. [Source-use10][sources]
records the primary and sibling passages actually checked.

Keep time zero, the literal theta source, and [E03 Note06][e03]:
\[
 a=\pi/8,\quad K(t)=\frac1{16\cosh(at)},\quad
 F(x)=D_0(x)H_0(x),\quad
 J(X)=\int_{\mathbb R}K(x-X)\log|F(x)|\,dx-P(X)+G(X,1),
\]
\[
 G(t,y)=\operatorname{atanh}(\sin(ay)\operatorname{sech}(at)),
 \qquad m(d,r)=\sin(a)d\operatorname{sech}(ar).
 \tag{1}
\]
The favorable comparison with m remains the same unpaid value question.
E06's failure concerns its prescribed sufficient allowance: R=66,
Q=32 and delta=2^(-4533) lead to log2 count argument >5252.8622;
the kernel-only term already gives >27.8519. No optimal-cost lower
bound follows. We do not modify [Request18][e06] or its result.

## 2. Regular deflation: precisely which data are needed

Partition I=[X-R,X+R] into finitely many intervals I_v of lengths L_v.
On each interval choose a finite **certified multiset of actual H_0
zeros**, z_1,...,z_n, with multiplicities, and exact approximate nodes
w_j satisfying |z_j-w_j|<=rho_j. A cluster certificate may repeat one
approximate node for several roots; no internal separation is assumed.
The root certificate must justify existence, count and this multiset
matching. It cannot be inferred from small residuals at candidate nodes.

Write P_v(z)=product_j(z-z_j) and U_v=H_0/P_v, with removable values.
It is enough to remove a submultiset for which the regular factor has
the certified floor below. A full census of the target exclusion
rectangle is **not** required for this logarithmic identity. In practice
chosen near-line clusters need complete counts, and omitted line zeros
would prevent the factor floor from passing.

Deflate H_0, not F: the latter has a pole at z=-i. The known D_0
is nonzero and finite on the real line. This avoids silently extending
F's holomorphy across that pole. All derivative enclosures below hold
on a convex compact domain containing I_v, the actual/approximate nodes
and their interpolating segments, with a holomorphic neighborhood.

For a holomorphic f let
\[
 \mathscr D_{\boldsymbol z}f(x)=f[z_1,\ldots,z_n,x]
 =\int_{\Delta_n} f^{(n)}\!\left(t_xx+\sum_jt_jz_j\right)dt,
 \qquad t_x+\sum_jt_j=1.
 \tag{2}
\]
The simplex has volume 1/n!. This is the classical Genocchi–Hermite
formula; [de Boor §9, (52)][sources] is the primary attribution. At actual
roots, including repeated roots, the interpolating polynomial is zero,
so (2) equals U_v. The same formula at w_j applied to the literal finite
source Hhat defines Uhat_v. It subtracts the interpolation polynomial:
**it is not Hhat divided by a product of approximate roots.**

Here are the error constants, derived from the simplex weights. If
sup|H_0^(k)-Hhat^(k)|<=epsilon_k and
sup|Hhat^(k)|<=Mhat_k on that convex domain, then, for j=0,1,2,
\[
 \sup_{I_v}|U_v^{(j)}-\widehat U_v^{(j)}|
 \le e_{v,j}:=
 \frac{j!\,\epsilon_{n+j}}{(n+j)!}
 +\frac{j!\,Mhat_{n+j+1}}{(n+j+1)!}\sum_{k=1}^{n}\rho_k.
 \tag{3}
\]
Indeed differentiating x inserts t_x^j; its integral is j!/(n+j)!.
Moving one knot along its segment additionally inserts t_k, whose
weighted integral is j!/(n+j+1)!. First compare the two fields at
the actual knots, then move the model knots, and sum. This argument
uses complex line segments and absolute values, and remains valid at
coalescence. For n=0 the node term vanishes and the derivative error
is epsilon_j. For n=2 with exact knots the coefficients are 1/2,
1/6 and 1/12, as in [OA's second-order formula][oa].

This does not make derivative acquisition free. With
rho(u)=pi exp(4|u|), define
\[
 Q_{k,b}^{>V}=\int_{|u|>V}|u|^k e^{(b+1)|u|}\rho(u)^2e^{-\rho(u)}du,
 \quad Q_{k,b}=Q_{k,b}^{>0}.
\]
Using E03's unchanged reflected source, its C_2(N) and B_0,
\[
 \epsilon_k\le\tfrac12\{5C_2(N)Q_{k,b}+B_0Q_{k,b}^{>V}\}
                 +\epsilon_{k,\rm eval},\qquad |\Im z|\le b.
 \tag{4}
\]
Differentiate the half-Fourier integral: the multiplier is (iu)^k,
and |exp(izu)|<=exp(b|u|). Splitting the two omitted source parts
proves (4). The superexponential tail makes each displayed moment
finite. Bound Mhat_k by the corresponding finite absolute moment of
the actual reflected prefix; account separately for its evaluation.
Orders through n+3 suffice for all of (3), or n+2 when the knots are
exact. Large cluster order or a wide convex domain may be expensive.
E06's value-error payment does not pay these derivative errors.

The load-bearing condition is a **verified uniform**
\[
 |\widehat U_v(x)|\ge\mu_v>e_{v,0}\quad(x\in I_v),\qquad
 b_v=\frac{e_{v,0}}{\mu_v-e_{v,0}}.
 \tag{5}
\]
Then |log|U_v|-log|Uhat_v||<=b_v by the mean value theorem for log.
A point sample, root residual or generic source upper bound is not (5).
Let W_v=integral_(I_v) K(x-X)dx. The factor-error radius is
\[
 E_{\rm fac}=\sum_v W_v b_v,\qquad \sum_vW_v\le1/2.
 \tag{6}
\]
Both the root enclosures and (5) are currently unacquired for this route.

## 3. Integrated root-location error, including the axis

For any real interval of length L>0 and complex z,w with |z-w|<=rho,
rho>0, put
\[
 A(L,\rho)=4\rho\{1+\log(1+L/(2\rho))\}.
\]
Then
\[
 \int_I\big|\log|x-z|-\log|x-w|\big|dx\le A(L,\rho).
 \tag{7}
\]
For r=|x-z| and s=|x-w| the log difference is bounded by
log(1+rho/r)+log(1+rho/s), almost everywhere. Replace r,s by their
horizontal distances. Each even decreasing integrand has its largest
length-L integral on the interval centered at its singularity. That
integral is
2[(L/2)log(1+2rho/L)+rho log(1+L/(2rho))], at most
2rho[1+log(1+L/(2rho))]. This proves (7), including roots on the real
line and endpoints. Define A(L,0)=0 by continuity.

Consequently
\[
 E_{\rm roots}=\frac1{16}\sum_{v,j} A(L_v,\rho_{v,j})
 \tag{8}
\]
pays all root-location errors in the compact weighted integral. The
sum counts repeated factors, including repeated use in different patches.
At fixed L, this is O(rho log(1/rho)), with no reciprocal distance
from the axis. For a purely vertical change at fixed real part, the
stronger unweighted bound is pi times the change in |Im z|: differentiate
the log distance with respect to nonnegative height and integrate its
Poisson kernel over the whole real line. Thus the weighted bound is
pi | |Im z|-|Im w| |/16.

This is a modulus in **certified root-location data**. For the local
control H_eta(z)=z^2+eta, roots move by sqrt(eta), even though source
coefficients move by eta. Deflation has U=1 but cannot remove that
root-acquisition sensitivity. There is no contradiction with OG B01's
scoped square-root obstruction, nor a new Lipschitz source-to-Green claim.

## 4. Product integration replaces both F5 terms

Set
\[
 q_v(x)=\log|D_0(x)|+\log|\widehat U_v(x)|.
\]
Acquire H_v>=sup_(I_v)|q_v| and B_v>=sup_(I_v)|q_v''|. For example,
if V_{v,j}>=sup|Uhat_v^(j)|, then one sufficient bound is
\[
 B_v\ge \sup_{I_v}|(\log|D_0|)''|
             +V_{v,2}/\mu_v+(V_{v,1}/\mu_v)^2.
 \tag{9}
\]
This follows from the real part of Uhat''/Uhat-(Uhat'/Uhat)^2.
The known gamma multiplier and its numerical evaluation remain charged.
A constant rescaling may improve the representation, but its logarithm
must be retained in D_0 Uhat; it cannot erase actual conditioning.

Use a partition of each I_v of maximum panel width Delta, with all
patch boundaries included. Let K_h and q_h be the endpoint linear
interpolants of K(x-X) and q_v on each panel. Define the signed sum
\[
 Q_h=\sum_v\int_{I_v}K_h(x)
       \left(q_h(x)+\sum_j\log|x-w_{v,j}|\right)dx.
 \tag{10}
\]
The singular factors are integrated, never sampled at a zero. For
w=u+iv, t=x-u and b=|v|, their two needed primitives are
\[
 A_0(t,b)=\tfrac t2\log(t^2+b^2)-t+b\arctan(t/b),
\]
\[
 A_1(t,b)=\tfrac14\{(t^2+b^2)\log(t^2+b^2)-(t^2+b^2)\}.
 \tag{11}
\]
They integrate log sqrt(t^2+b^2) and t times that logarithm,
respectively. At b=0 use A_0=t log|t|-t and the continuous A_1;
0 log 0=0. The b arctan(t/b) term is replaced by zero in this case.
For a linear function of x use A_1+u A_0. Polynomial products
K_h q_h integrate exactly. Finite-precision evaluation of (11),
including endpoint cancellation and small b, still needs enclosures.

Let D_{v,j}=max_(x in I_v)|x-w_{v,j}| and
\[
 A_{v,j}=L_v\log^+D_{v,j}+2,\qquad
 S=\sum_v\left(L_v H_v+\sum_j A_{v,j}\right),
 \quad K_2=a^2/16<1/100.
\]
Here integral_I |log|x-w||<=A_{v,j}: the positive part is bounded
by L log^+D; the negative part is at most
integral_(-1)^1 -log|t|dt=2. Also |K''|<=K_2, directly from
(sech)''=sech(1-2 sech^2). Linear interpolation of any C^2 function
has uniform error at most its second-derivative bound times Delta^2/8.
Therefore
\[
 \boxed{E_{\rm quad}\le\Delta^2 C,\qquad
 C=\frac18\left(\sum_v W_vB_v+K_2S\right)
       \le\frac{B_*}{16}+\frac{a^2S}{128},\quad B_*=\max_vB_v.}
 \tag{12}
\]
To prove it, split K q_v-K_h q_h into K(q_v-q_h)+(K-K_h)q_h.
The first term integrates to at most Delta^2 W_vB_v/8.
The linear interpolant satisfies |q_h|<=H_v, paying the second term.
Apply the same kernel interpolation error to each integrable singular
factor. Add over the disjoint patches. The signed Q_h is retained;
only acquisition errors are bounded absolutely.

Equation (12) removes **both** E06 artifacts: there is no 1/delta
derivative term, and no first-order kernel term proportional to
|log delta|. It does not remove the actually acquired H_v, B_v or
source/root conditioning. For fixed paid constants the panel-width
cost is O(e_quad^(-1/2)). With p patches, subdividing each into
ceil(L_v/Delta) panels costs at most 2R/Delta+p panels. This is a
quadrature count, not total acquisition or operation count.

A concrete sufficient scalar box illustrates the kernel comparison.
At R=66, assume **p<=1024 patches, B_*<=2^20 and S<=2^19**.
Subdivide patch v into ceil(6000 L_v) equal panels. Their maximum
width is at most 1/6000 and their total number is at most
792000+p<=793024<10^6. Also C<65536+656<66200. Thus
\[
 E_{\rm quad}<66200/36000000<1/500<1/400<e_{\rm quad,E06}.
 \tag{13}
\]
The last comparison uses E06's directed radius >0.00277312.
These are **sufficient design thresholds, not measured theta bounds**.
The p allowance explicitly pays panel rounding at arbitrary patch
boundaries; a width condition alone would not establish a cap.
This arithmetic answers the kernel-only failure; it does not certify
that canonical deflation satisfies (5), (9), (13), or an affordable cost.

Node errors have an ordinary relative-factor payment, not 1/delta.
An absolute Uhat evaluation error eta<mu_v changes its logarithm by
at most eta/(mu_v-eta). Its product-interpolation weights are positive;
their sum is integral K_h, explicitly computable and <=R/8.
Kernel nodes, primitives, source moments, gamma, primes and arithmetic
must also be enclosed. None is paid by counting panels.

## 5. Complete signed acquisition ledger

Retain the **exact-log** tail T(X,R) and prime tail beta_Q of E03.
Suppose the evaluated central signed quantity Q_h-P_Q+G(X,1) has
center S_c and a certified radius e_num, including all finite numerical
errors not already in (6), (8), (12). Then
\[
 |J(X)-S_c|\le\mathcal R:=T+\beta_Q+E_{\rm fac}
                      +E_{\rm roots}+E_{\rm quad}+e_{\rm num}.
 \tag{14}
\]
In particular the new upper endpoint J_up=S_c+Rcal satisfies
\[
 \boxed{0\le J_{\rm up}-J(X)\le2\mathcal R.}
 \tag{15}
\]
This is a **two-sided** approximation followed by an upper endpoint.
The factor two cannot be copied from E03's one-sided local envelope
without adjustment. Requiring 2Rcal<=h gives an h-accurate upper;
J_up<m(d,r) is a separate, unevaluated value test. R=66 and Q=32
can reuse E06's T and beta payments, but its delta, source cutoffs and
node allowance do not automatically pay the new derivative/factor data.

## 6. Divisor-cell ranges: cusp, completeness and a full Green tail

Define Psi_X(x,y)=G(X-x,max(0,y)) for -1<=y<=1. For an occupied
rectangle C_i=[l_i,u_i] x [b_i,c_i] clipped to that strip, let n_i
be its certified number of zeros, including multiplicity. Let
dist_i=dist(X,[l_i,u_i]) and far_i=max(|X-l_i|,|X-u_i|). Then
\[
 L_i=G(far_i,(b_i)_+),\qquad U_i=G(dist_i,(c_i)_+),
 \qquad n_iL_i\le\sum_{z_j\in C_i}\Psi_X(z_j)\le n_iU_i.
 \tag{16}
\]
This follows from monotonicity in y and |X-x|. Singleton cells,
separation and exact reality are unnecessary. Do not discard the
positive height allowance of a cell straddling the axis.

For positive y the derivatives obey
\[
 0\le G_y(t,y)\le\tfrac12\operatorname{sech}(at),\qquad
 |G_t(t,y)|\le\tfrac15 y\operatorname{sech}(at).
 \tag{17}
\]
Use a<2/5, cos^2 a>21/25, sin(ay)<=ay in the differentiated
atanh expression: a/cos^2 a<1/2 and a^2/cos^2 a<1/5.
The positive-part map is 1-Lipschitz. Hence a safe per-label range
width is ((c_i)_+-(b_i)_+)/2+(c_i)_+(u_i-l_i)/5.
There is a derivative jump at y=0, but no loss of this Lipschitz
location bound. A smooth-test Newman-time theorem cannot be invoked
through that jump; root motion itself may have square-root time scale.

Completeness requires a zero-free enclosing boundary, exact total
counts and coverage of every retained strip zero, not just boxes around
numerically found roots. For integer X,R with all zeros in
|x-X|<R acquired, [Note10's source/count input][b06] gives
\[
 0\le J_{\rm tail}\le T_G(X,R)
 =32\sum_{n=R}^{\infty}(|X|+n+3)^2 e^{-3n/8}.
 \tag{18}
\]
There are two integer unit slabs per n, each with count
<=16(|X|+n+3)^2, and G(t,y)<=exp(-3|t|/8).
Writing q=exp(-3/8) and A=|X|+R+3 gives the closed expression
\[
 T_G=32q^R\left\{\frac{A^2}{1-q}
             +\frac{2Aq}{(1-q)^2}+\frac{q(1+q)}{(1-q)^3}\right\}.
 \tag{19}
\]
The integer alignment is a hypothesis; arbitrary shifted slabs need
an adjusted covering factor. This tail is exponential Green decay,
not OC's Gaussian tail. The complete upper is
J_cell=sum_i n_i U_i+T_G. It contains no extra prime, pole or
conjugate-pair term. Each upper zero is counted once; lower and real
zeros enter with zero exact contribution.

### Same-information dominance

Let D=[X-r,X+r] x [d,1], d>0, r<R, and assume the complete core
cover and certified cell counts above. **For the independent rectangular
range upper J_cell, J_cell<m(d,r) implies that every occupied C_i
is disjoint from D.**

Proof: if C_i meets D, its supremum U_i is at least G(r,d), and
G(r,d)>=sin(ad)sech(ar)>=d sin(a)sech(ar)=m(d,r).
Since n_i>=1 and every other term, including the tail, is nonnegative,
the strict test fails. Contraposition proves the assertion. Thus a direct
cell-intersection test can use the **identical acquired prefix** and
already conclude exclusion when this Green test succeeds. It need not
evaluate G or an infinite tail. This does not claim a measured wall-time
ordering of arbitrary implementations or compare correlated/divisor
constraints that go beyond independent cell maxima.

The inherited X=1500 census and bound <1/200 remain a useful warm-input
example at their original certification level. They do not supply the
X=30 root/factor data, a cold-cost comparison or new exclusion territory.

## 7. What the two methods actually cost

| Obligation | Deflated signed log | Independent Green cells | Matched direct exclusion |
| --- | --- | --- | --- |
| Canonical source | Literal source construction and derivative moments through local degree+3, with finite evaluation error | Source/derivative enclosures sufficient for certified contours and subdivision | Same source; pay only the jets/contours actually used on D |
| Root information | Certified selected cluster counts, multiplicities and radii; no assumed simple roots | Complete divisor cover of the full core, with multiplicities | May use exactly that cover and stop on cell disjointness, or acquire only D |
| Conditioning | Uniform mu_v>e_v,0, actual B_v/H_v, stable divided-difference evaluation | Contour modulus floors and conditioning needed to acquire counts/cells | Charge common contour/source setup equally; no Green tail needed |
| Finite integration | Product rule (10), singular primitives and all rounding; O(sum_v (1+n_v) N_v) panel operations for the displayed rule, apart from factor evaluation | Range values and sum; no singular log integration | Cell intersections/count zero; no log/Green sum |
| Infinite terms | E03 exact-log tail, finite prime sum and beta, one pole term | New exponential Green tail (19) | None outside the target when its completeness is paid |

A bound on (12) alone leaves C_source+C_roots+C_floor unpriced.
Write the full cost of the displayed log implementation as
\[
 C_{\log}=C_{\rm source}+C_{\rm roots}+C_{\rm floor}
           +C_{\rm factor\ eval}+C_{\rm product}+C_{\rm tail/prime}.
 \tag{20}
\]
No numeric values for these terms or the corresponding direct cost have
been acquired. Existence of a positive factor on a compact line implies
some positive minimum, not an affordable certified minimum. A generic
Harnack lower bound could simply move E06's severe conditioning here.

The decisive missing item is a **literal-source, completely charged
acquisition of (3)–(9)** on a declared patch cover, yielding (14) at the
requested accuracy and a credible cost comparison on the same D.
This is an acquisition/conditioning problem, not just renaming J<m.
A useful value remains separately required. If the proposed acquisition
already certifies D empty, record the Green computation as calibration
or a reusable observable; do not claim a new exclusion mechanism.

At X=30 the target is a known-region calibration, as previously sourced
in B04. No colder or higher target, provider replacement or parameter
sweep is authorized by this comparison. For an already-owned census,
its marginal reuse cost and its historical acquisition cost must both
be visible; charging the direct baseline for a census while giving it
free to Green is not a matched comparison.

## 8. Analytical collision controls and scope

The [controls12][controls]/[avoid02][a02] screen is analytical, not a new
numerical replay. The generic acquisition and dominance proofs can hold
for a colliding control with its own data; they do not distinguish theta.

| Control class | Canonical premise that cannot be transferred; scope of the new claims |
| --- | --- |
| Fixed/growing Euler factors | Unchanged conductor-one coefficients and prime baseline fail. Their own root shifts remain paid in (8); no uniform Lipschitz source claim follows. |
| Weighted squares and finite theta/zero-tail changes | Complete unchanged theta coefficients plus full normalized reflection are absent. Positive terms and finite endpoints do not pay (4) for theta. |
| Finite-prime orbits | Full source reflection is missing; selected arithmetic observations do not provide complete root matching or factor floors. |
| Reflected super-Gaussian and smooth positive/primitive sources | The complete integer-square arithmetic and xi/zeta identity are missing. Their generic deflation remains valid; no theta smallness is implied. |
| Fixed-event atoms and finite-profile families, including continuous extensions | Complete coefficients/profile and the stated eventual-simplicity hypotheses are absent. A real multiple root is allowed and has zero interior Green mass. |
| RH-conditional normalized endpoint perturbations | Ordinary Dirichlet-series arithmetic fails. Completion, functional equation and residue must not be listed as failed premises; those are preserved in that construction. |
| Variable readouts; three-profile positive-measure relaxation | Respectively the physical cosine/Newman equation, or integer divisor/full-source constraints, are absent. Counts in (16) cannot be fractional substitutes. |
| Counter-kernels q and q_(T,a); smooth-density replacement | They lack the canonical theta transform/anchor, or replace the discrete prime measure. Their own constants/baseline must be supplied. |
| Two-channel norm-factorization exclusion | Its architecture and support class differ from the signed log method; it is a scoped exclusion, not a universal field counterexample. |

A control with a positive-depth defect inside D cannot pass a correct
complete Green upper below m. For cell ranges, its occupied defect cell
already blocks the pass by the dominance proof. For signed acquisition,
its own valid upper remains at least its own positive Green value; a
failed exact-theta premise alone does not show which numerical allowance
would fail. An exactly real double zero has no interior mass, and a
positive-time event is not silently relocated to time zero. A finite
box missing a control's defects can legitimately pass.

## 9. Disposition

B05 selects no new field execution. It parks **cold acquisition of
independent Green cells for exclusion advantage**, at precisely the
information class proved above, and retains the conditional deflated-log
method with its explicit missing conditioning/cost data. There is no
obstruction asserted against all zero-based methods, signed estimates,
cluster methods or the unchanged theta source.

The useful next fixed task is the [E07 analytical assessment][audit],
with one bounded correction cycle. [Check10][check] is only the proof
author's internal checking. [Continuation14][next] gives model-change
guidance and conditional re-entry requirements. No manuscript milestone,
investigation closure, shared-summary promotion or numerical certificate
is claimed.

[results]: ../../../../../../result-summaries/README.md
[heat]: ../../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md
[controls]: ../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../avoid/README.md
[a01]: ../../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a11]: ../../../../../../avoid/11_certifying_the_known_and_tests_that_cannot_fail.md
[e03]: 06_TND_OG_E03_COMPLETE_SIGNED_LOG_ACQUISITION_20261108.md
[e06]: ../research-progress/handoffs/18_TND_OG_E06_SINGLE_TUPLE_FEASIBILITY_REQUEST_20261108.md
[b06]: 10_TND_OG_B06_SIBLING_RESULTS_AND_GREEN_CENSUS_TRANSFER_20261110.md
[oa]: ../../03_collision_constraints/manuscript/sections/02_deflation.tex
[sources]: ../references/10_TND_OG_B05_DEFLATION_AND_COST_SOURCE_USE_20261110.md
[audit]: ../research-progress/handoffs/23_TND_OG_E07_ANALYTICAL_ASSESSMENT_REQUEST_20261110.md
[check]: ../reviews/10_TND_OG_B05_PROOF_AUTHOR_CHECK_20261110.md
[next]: ../continuation-notes/14_TND_OG_B05_RESULTS_AND_MODEL_CHANGE_20261110.md
