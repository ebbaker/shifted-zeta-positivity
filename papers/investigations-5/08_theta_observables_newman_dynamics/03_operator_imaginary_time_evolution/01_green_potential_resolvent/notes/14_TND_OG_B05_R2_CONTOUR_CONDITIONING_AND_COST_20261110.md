# B05 r2: acquire the regular factor from certified local contours

10 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance. Actual model and effort are not recorded in
chat0009's accessible source metadata; neither is inferred. **Status:
proved in-note, proof-author checked only; canonical acquisition untested.**

## 1. Decision and project status

B05 r2 selects one concrete acquisition design: literal-source Taylor
polynomials, complete local disk counts, certified small cluster disks,
and boundary-modulus bounds. The boundary data give a quantitative
regular-factor floor by the maximum principle applied to its reciprocal.
A logarithmic oscillation bound then pays curvature without the coarse
ratio-squared allowance in Note12 (9). Polynomial divided differences
can be precomputed without dividing by root separations.

The resulting **conditional** full-cover design uses 264 patches and
67584 integration panels, with each of factor, root, quadrature and
finite numerical error below or equal to 1/2000. The conditions are
explicit gates, not measured theta bounds. There is no field run here.
The selected next task is **[E] TND-OG-E08 — GPT-6.1 Sol**, a bounded
three-patch acquisition pilot and a same-source direct comparator, in
[Request26][request]. It does not execute the full-cover design.

Classification under [avoid01][a01]: conditional quantitative acquisition
and a cost experiment specification, not a new RH-equivalent criterion.
Read the [result index][results], [heat/Green cluster11][heat],
[controls12][controls] and [avoid index][avoid], especially
[premise screening02][a02], [scope07][a07] and [matched cost11][a11].

The high-level state is:

* **OG:** E03/E05 give finite signed-log acquisition; E06's specified
  uniform-midpoint allowance failed; E07 accepted B05 r1's conditional
  deflation and cell comparison. The source-acquired favorable signed
  value and affordable full-cover conditioning are still open.
* **Finite reuse:** [Note10][siblings] derives
  \(0\le J_0^{\rm G}(1500)<291/65536+2^{-157}<1/200\) from OC's complete
  census at its inherited winding-certification scope. That census
  already contains stronger local exclusion information.
* **OC/OA:** Note10 records OC's finite Gaussian pair enclosure and
  OA's pair law \(q'=-8-4qB\). A smooth pair statistic does not control
  the nonsmooth Green boundary test; a deflated pair law still requires
  a factor floor and an upper force envelope on the whole time interval.
  Those are not supplied by the present time-zero design.

Keep the unchanged physical source and [Note06][e03] normalization:
\[
 s(z)=(1-iz)/2,\quad H_0(z)=\xi(s(z))/8,\quad
 F=D_0H_0,\quad D_0=16\pi^{s/2}/[s^2\Gamma(s/2)],
\]
\[
 J(X)=\int_{\mathbb R}\frac{\log|F(x)|}{16\cosh(a(x-X))}\,dx
       -P(X)+G(X,1),\quad a=\pi/8,
\]
\[
 G(t,y)=\operatorname{atanh}(\sin(ay)\operatorname{sech}(at)),\qquad
 m(d,r)=d\sin(a)\operatorname{sech}(ar).                         \tag{1}
\]
The inherited identity also equals the nonnegative sum
\(J(X)=\sum_{\Im z_j>0}G(X-\Re z_j,\Im z_j)\), with multiplicity.
Its existing consumer J(X)<m(d,r) excludes the rectangle
[X-r,X+r]+i[d,1]. This is the old target, not a new result of r2.
The fixed target remains \(X=30,R=66,Q=32,d=1/2,r=1\), with
\(D=[29,31]+i[1/2,1]\) and \(h=m(1/2,1)/4\). This is calibration
inside the known region. Neither small acquisition error nor a small
panel count supplies the separate inequality \(J_{\rm up}<m\).

## 2. A declared cover and complete root certificates

Partition [-36,96] into the 264 intervals
\[
 I_v=[-36+v/2,-36+(v+1)/2],\quad c_v=-143/4+v/2,
 \quad 0\le v<264.                                           \tag{2}
\]
Each half-length is \(\ell=1/4\). For each patch test outer radii
\(A\in\{1/2,3/4,1\}\), in that order, and put \(s=A-1/8\).
Acquire an exact rational-coefficient polynomial p approximating H0
on the **whole closed disk** \(|z-c_v|\le A\), with derivative errors
\(\epsilon_k\), k=0,...,7, as in section 5. The polynomial is a
paid evaluation of the literal source, not a zeta/RS replacement.

Certify the following, allowing refusal when a boundary or cap fails:

1. The outer circle has \(m_p\le|p|\le M_p\) with
   \(m_p>\epsilon_0\), and a certified winding count n, \(0\le n\le4\).
2. For n>0, disjoint closed cluster disks \(|z-w_j|\le\rho_j\)
   lie strictly inside \(|z-c_v|<s\), have certified positive integer
   counts \(m_j\) summing to n, and satisfy
   \(\min_{\partial B_j}|p|>\epsilon_0\). The centers are exact dyadic
   complex numbers and \(\rho_j\le2^{-24}\).

Rouché transfers each count from p to H0. Completeness follows from
the outer count equalling the sum of the disjoint inner counts. All
disk zeros, including multiplicities, are thus in the inner disks;
there is no uncounted annular zero. Repeat w_j and rho_j exactly m_j
times in the list of n knots. This gives an actual-root multiset
matching without resolving internal cluster separation or asserting
that m_j is the multiplicity of a single root. A real-centered disk
of count one can establish reality by conjugation; it is not assumed.

The certificates can use interval enclosures of p on circular arcs.
Each accepted arc image lies in a convex ball avoiding zero, so the
image path is homotopic to its endpoint chord without crossing zero.
A consistent argument lift or certified polygon winding determines the
integer count. Include endpoint rounding and certify the unique integer;
unverified principal-argument sums are insufficient. Translate p to a
cluster center before evaluation if cancellation makes the original
basis ineffective. Candidate roots only propose disks; counts certify them.

The method needs a complete census **inside each chosen disk**, not a
census of the whole strip. Zeros outside that disk remain in its regular
factor. Their effects are included in the boundary data and the maximum
principle; they have not been dropped from the logarithmic identity.

## 3. An acquired floor, including repeated roots

Let z_1,...,z_n be the certified actual roots in the outer disk, repeated
with multiplicity, and put
\[
 U(z)=H_0(z)/\prod_{j=1}^n(z-z_j),\quad
 m=m_p-\epsilon_0>0,\quad M=M_p+\epsilon_0.
\]
All singularities of U are removable and U is zero-free on the closed
disk. On its boundary, \(A-s\le|z-z_j|\le A+s\). The maximum principle
for U and 1/U therefore gives, throughout the disk,
\[
 \boxed{\mu_0:=\frac{m}{(A+s)^n}\le |U(z)|
                 \le\frac{M}{(A-s)^n}=:V_0.}                 \tag{3}
\]
For n=0 the products are one. The root counts, strict boundary floor
and positive gap A-s are load-bearing. Merely evaluating a symbolic
product or declaring U nonvanishing does not acquire (3).

Let \(\widetilde U(z)=p[w_1,\ldots,w_n,z]\). Note12 (3), valid for
any holomorphic approximant with the stated derivative errors, gives
on the whole disk
\[
 e_j=\frac{j!\epsilon_{n+j}}{(n+j)!}
      +\frac{j!M_{p,n+j+1}}{(n+j+1)!}\sum_{k=1}^n\rho_k,
 \quad j=0,1,2,                                             \tag{4}
\]
where \(M_{p,k}\ge\sup_{|z-c_v|\le A}|p^{(k)}(z)|\).
The disk is convex and contains all actual and approximate knots,
so the same simplex proof works for complex evaluation points.
The highest order needed is n+3<=7. For
\(p(c_v+\zeta)=\sum_{k=0}^{64}a_k\zeta^k\), one acquired bound is
\(M_{p,j}\le\sum_{k=j}^{64}(k)_j|a_k|A^{k-j}\), with directed rounding.
This uses the acquired local coefficients rather than discarding their
cancellation in a global absolute-source moment.

Require the relative gate \(e_0\le\mu_0/1024\). Then
\[
 \mu:=\mu_0-e_0\le|\widetilde U|\le V_0+e_0=:V,
 \qquad
 E_{\rm fac}\le\frac12\frac{e_0/\mu_0}{1-2e_0/\mu_0}
              \le\frac1{2044}<\frac1{2000}.                 \tag{5}
\]
For different patches apply the bound separately and use
\(\sum_v\int_{I_v}K\le1/2\). We retain Note12's conservative
\(e_0/(\mu-e_0)\) logarithmic payment rather than changing its ledger.
The explicit unpaid relative inequality is
\[
 \frac{\epsilon_n}{n!}
 +\frac{M_{p,n+1}}{(n+1)!}\sum\rho_k
 \le\frac{m_p-\epsilon_0}{1024(A+s)^n}.                       \tag{6}
\]
This is now a check on recorded contours, coefficients and root radii.
No assertion that theta satisfies it within the proposed budget is made.

## 4. Curvature from logarithmic oscillation

Suppose a zero-free holomorphic g on a disk of radius A has
\(\mu\le|g|\le V\). A holomorphic logarithm exists in the disk.
On a circle of radius t about a point x, subtract
\((\log\mu+\log V)/2\) from its real part. Its absolute value is at
most \(\frac12\log(V/\mu)\). If the logarithm's local power-series
coefficient of degree k is b_k, Fourier extraction gives, for k>=1,
\[
 b_kt^k=\frac1\pi\int_0^{2\pi}\log|g(x+te^{i\theta})|
                     e^{-ik\theta}\,d\theta,
 \qquad |b_k|\le\frac{\log(V/\mu)}{t^k}.
\]
Taking k=2 and t increasing to A-|x-c_v| proves
\[
 |(\log|g|)''(x)|\le
 \frac{2\log(V/\mu)}{(A-\ell)^2}\quad(x\in I_v).             \tag{7}
\]
Use g=tilde U and write \(\lambda_v=\log(V/\mu)\). This bound
uses a zero-free complex disk; a floor on the real interval alone
does not justify (7).

The known multiplier has a useful fully explicit curvature payment:
\[
 (\log|D_0|)''=\Re\left[-\frac1{2s^2}
                           +\frac1{16}\psi'(s/2)\right],
 \qquad |(\log|D_0|)''|\le 2+20/16=13/4.                    \tag{8}
\]
Indeed |s|>=1/2 and Re(s/2)=1/4 on the real line. The trigamma
series gives \(\sum_{j\ge0}|j+s/2|^{-2}\le16+4=20\), bounding
the j>=1 sum by the integral from zero. [Source-use11][sources]
records the primary passages; the constants above are derived here.

Thus Note12's regular q_v=log|D0|+log|tilde U| can use
\[
 B_v=13/4+\frac{2\lambda_v}{(A-1/4)^2}.                     \tag{9}
\]
A computable absolute bound is
\(H_v=H_{D,v}+\max\{|\log\mu|,|\log V|\}\).
If the two endpoint log|D0| values are enclosed, their maximum absolute
value plus 13/128 is a valid H_D,v by linear interpolation and (8).
Logarithmic gamma evaluation and all rounding still cost operations.

For the full design require \(\lambda_v\le32\) and \(H_v\le256\)
on all patches. These are **unmeasured sufficient gates**. Since
A-1/4>=1/4, B_*<=4109/4. Since every approximate knot is within
s<=7/8, its distance from I_v is at most 9/8. Therefore the S of
Note12 (12) satisfies
\[
 S\le132\cdot256+(264\cdot4)(2+\tfrac12\log(9/8))
   \le35970,
\]
\[
 C\le B_*/16+a^2S/128<4109/64+35970/800
   =34933/320<110.                                         \tag{10}
\]
Use exactly 256 panels per patch, width \(\Delta=1/512\). Then
\[
 \boxed{N_{\rm pan}=67584,\qquad E_{\rm quad}<110/512^2
                                           <1/2000.}        \tag{11}
\]
There are at most 1056 root labels across patches, with repeated use
charged again. Note12 (8), L=1/2 and rho<=2^-24, gives
\[
 E_{\rm roots}\le264\,2^{-24}
       [1+\log(1+2^{22})]
 <\frac{99}{262144}<1/2000,                                \tag{12}
\]
using log(1+2^22)<23. This pays roots on the line and repeated roots.

## 5. Pay the literal-source polynomial, including its derivatives

Fix **N_src=8, V_src=2, degree L=64** for the proposed pilot. These are
chosen design parameters, not successful theta measurements. On u>=0 set
\[
 \Phi_N(u)=e^u\sum_{n=1}^N[2(n^2\pi e^{4u})^2-3n^2\pi e^{4u}]
                                         e^{-n^2\pi e^{4u}}.
\]
By the unchanged reflected convention,
\(\widehat H(z)=\int_0^2\Phi_8(u)\cos(zu)du\).
For real c obtain 65 coefficient enclosures from
\[
 \alpha_j(c)=\frac1{j!}\int_0^2\Phi_8(u)u^j
                          \cos(cu+j\pi/2)du,
 \quad |a_j-\alpha_j|\le\delta_j,\quad 0\le j\le64.           \tag{13}
\]
Choose exact dyadic real a_j. Include their rounding in delta_j.
Let Qbar and Qbar(2) be Note06 (15)'s explicit upper majorants and
B0bar=5 C2bar(0). For k<=7 and b<=2,
\(u^ke^{(b+1)u}\le e^{9u}\): for k>0 the maximum of
\(u^ke^{-(8-b)u}\) is \([k/(e(8-b))]^k<1\).
Consequently the complete omitted-source derivative radius is bounded by
\[
 E_{\rm src}=\tfrac12[5\overline C_2(8)\,\overline Q
                       +\overline B_0\,\overline Q(2)].     \tag{14}
\]
The same majorant pays every derivative through order seven. No original
theta tail is replaced by a finite source, and no derivative at the
reflection join u=0 is assumed to match.

Put \(M_{65,A}^{\rm fin}=\int_0^2\Phi_8(u)u^{65}e^{Au}du\).
For A<=3/2 one sufficient scalar bound is
\(M_{65,A}^{\rm fin}\le2^{65}\overline B_0\overline Q/2\).
Taylor's integral remainder applied to the entire cosine gives
\[
 \epsilon_k\le E_{\rm src}
 +\sum_{j=k}^{64}(j)_k\delta_j A^{j-k}
 +\frac{2^{65}\overline B_0\overline Q}{2}
              \frac{A^{65-k}}{(65-k)!},\quad 0\le k\le7.     \tag{15}
\]
All quantities in (14)-(15) need directed enclosures. This is the
explicit derivative-error input to (4); increasing precision cannot
remove the fixed source or Taylor remainder.

A fixed validated coefficient integrator is available without importing
a new physical provider. For the integrand f_j in (13), on a real source
panel [u0-h,u0+h] integrate its midpoint Taylor polynomial of degree 15:
\[
 2\sum_{l=0}^7\frac{f_j^{(2l)}(u_0)h^{2l+1}}{(2l+1)!},\qquad
 |\text{remainder}|\le\frac{2h^{17}}{17!}
                         \sup_{\rm panel}|f_j^{(16)}|.       \tag{16}
\]
Finite interval differentiation of the displayed positive-half-line
source supplies the derivative bound, including at the one-sided
endpoint zero. Sum all remainders and arithmetic radii. Poor enclosures
may force subdivision or fail the work cap; an integrator label is not
an error payment. The sixteenth derivatives in (16) refer to the u-integration
algorithm; the physical z-derivative interface still ends at order seven.

For exact p, form its divided-difference polynomial by repeatedly
replacing r(z) with [r(z)-r(w)]/(z-w). Synthetic division computes
each quotient's coefficients using additions and multiplications only.
After n steps it is p[w1,...,wn,z], also when knots coincide. It is
**not** p(z)/product(z-wj). Setup costs O(nL) scalar operations and
each factor value costs O(L-n) by Horner. Ball arithmetic must still
enclose coefficient-growth and cancellation errors; no numerical
stability theorem is asserted merely from the absence of small divisors.

## 6. Complete signed error and finite evaluation obligations

Use Note12's signed product integration, including its singular-log
primitives and exact b=0 limits. Polynomial source errors are already
in (15) and (4); do not charge them twice. Charge subsequent deflation,
Horner, logarithm, gamma, kernel, primitive, prime and rounding errors
to \(e_{\rm num}\le1/2000\). For example:

| Numerical part | Sufficient allocation |
| --- | --- |
| Factor endpoint evaluation and logarithm | Radius <=1/10000; an absolute factor evaluation error <=2^-17 mu gives weighted log error <1/10000 because integral K_h<=R/8=33/4. Include log rounding separately within the allocation. |
| log abs(D0) endpoints | Total weighted radius <=1/10000. A uniform log radius <=2^-17 is sufficient for this part. |
| Kernel nodes | Total radius <=1/10000. With the exact regular/singular L1 bound S<=35970, a uniform kernel error <=2^-29 suffices; also include products with node uncertainty. |
| Singular primitives | Accumulated interval radius <=1/10000, including small imaginary parts and endpoint cancellation. |
| Prime sum, pole term and remaining arithmetic | Combined radius <=1/10000. Include all cross-error and summation terms here or explicitly in another row; no unallocated error is permitted. |

These are allocation tests, not promised working precision. The complete
radius and upper endpoint remain
\[
 \mathcal R=T+\beta_Q+E_{\rm fac}+E_{\rm roots}+E_{\rm quad}+e_{\rm num},
 \quad J_{\rm up}=S_c+\mathcal R,\quad
 0\le J_{\rm up}-J\le2\mathcal R.                            \tag{17}
\]
E06's recorded R=66,Q=32 bounds have T,beta<=h/12 and h>1/64.
Thus a full passing cover and evaluation give
\(2\mathcal R\le h/3+1/250<h\). This deliberately leaves slack.
The factor two, prime remainder and one plus pole term are retained.
No S_c or J_up has been acquired in B05 r2.
Using E06's saved directed tail endpoints and the sharper individual
allowances (5), (11), (12), [Record08][record] checks the conditional
comparison \(J_{\rm up}-J<17/1000<h\) by exact rational arithmetic.
This bounds acquisition error; it is not an upper bound of 17/1000 on J.

## 7. Price acquisition and give direct exclusion identical information

Use a cost vector, not an invented wall-time prediction. Let P be working
precision, Q_v the number of source panels, A_v^test the number of tested
contour arcs (including rejected tests), I_v root-candidate/isolation
work, and L=64. With order-16 jets, direct finite series arithmetic gives
O(Q_v (N_src+L+1)17^2) ball operations for the coefficient integrator,
plus its elementary-function calls. Record those calls, peak precision,
retries and actual runtime in any execution. Bounds for source moments
and derivatives must be charged even if cached across centers.

For the full specified log implementation the cost has all of these terms:
\[
 \begin{split}
 C_{\log}={}&C_{\rm source\ setup}
 +\sum_v[C_{\rm coeff}(Q_v,P)+C_{\rm isolate}(I_v,P)
          +C_{\rm contour}(A_v^{test}L,P)+C_{\rm gates}(L,P)]\\
 &+C_{\rm deflate}(\sum_v n_vL,P)
  +C_{\rm Horner}(\sum_v(N_v+1)(L-n_v+1),P)\\
 &+C_{\rm gamma/kernel/log}+C_{\rm primitives/product}
  +C_{\rm exact\ tail/prime/pole/rounding}.                   \tag{18}
 \end{split}
\]
In particular there are 17160 coefficient integrals before sharing, at
most 67848 factor endpoint evaluations, 67585 distinct global gamma and
kernel nodes before reuse, and at most 271392 root/node pairs for each
of the two primitives. Contour and isolation work is not determined by
67584 panels. Precision-dependent operation costs and failed attempts
cannot be omitted from a claimed measured saving.

The matched direct target is the same D and the same H0 provider.
Give it every acquired polynomial, error enclosure and root certificate
at the same cost. Where their certified disks cover D and the retained
root disks avoid D, direct exclusion is already proved. If that union
does not cover D, do not claim a complete direct conclusion from it.

For a concrete **cold comparator**, use one additional polynomial
centered at real c=30, evaluated on radius A=3/2; this disk contains D.
Use the identical N_src,V_src,L, coefficient algorithm and precision
tiers. Certify \(|p_{30}|>\epsilon_0\) on the four sides of D and
winding zero. Rouché then gives no H0 zero in the closed D, with its
boundary explicitly nonzero. This requires 65 coefficient integrals,
contour tests and rounding, but no tiny root disks, factor evaluation,
Green quadrature or external Green tail. The different geometric domain
is priced explicitly; it is not given a cheaper uncharged zeta provider.

For a warm comparator charge shared acquisition once to both consumers
and compare only the extra work. If direct exclusion has already passed,
any later Green scalar is observable calibration/reuse. The 264 versus
one center count is not a wall-time theorem: source precision and
contour conditioning may differ, and neither has been measured here.
Note12's dominance theorem for **independent rectangular maxima** is
unchanged; it does not by itself dispose of this signed-log design.

## 8. Analytical collision and failure controls

The mandatory [controls12][controls] screen is run analytically, as in
[avoid02][a02]. No new collision numerics is claimed. The new complex
analysis estimates are generic and can pass for colliding sources with
their own acquired data. They do not distinguish theta by themselves.

| Control family | Canonical premise absent or changed |
| --- | --- |
| Fixed/growing Euler-factor controls | The unchanged conductor-one source coefficients and prime baseline. Their own local polynomial acquisition can still be valid. |
| Weighted squares; finite theta/zero-tail changes | The conjunction of complete unchanged theta coefficients and full normalized reflection. Finite endpoint matches do not pay (14). |
| Finite-prime orbit controls | Full reflection; selected arithmetic measurements are not the complete source integral. |
| Reflected super-Gaussian; smooth shape/positive primitive | Complete integer-square theta arithmetic and xi/zeta identity. Positivity or reflection does not establish a canonical boundary modulus. |
| Fixed-event atoms and finite-profile families, including continuous extensions | Complete theta coefficients/profile growth; the stated eventual-simplicity premise in the families where it fails. A real multiple root is permitted by the present local theorem. |
| RH-conditional normalized endpoint perturbations | Ordinary Dirichlet-series arithmetic. Their preserved completion, functional equation and residue are not listed as failures. |
| Variable observation kernels; three-profile positive-measure relaxation | Respectively the full physical cosine/Newman equation, or integer-divisor/full-source realizability. |
| Older q and q_(T,a) kernels; smooth prime-density replacement | Literal theta transform/anchor, or the discrete prime measure and its baseline. |
| Two-channel norm-factorization exclusion | Different specified support and factorization architecture; no universal obstruction to this signed method follows. |

Three local failure tests make the additional hypotheses substantive:

* **Omitted root:** H(z)=z(z-1/4), outer disk |z|<=1, but remove only
  z=0. A positive boundary modulus does not make H/z zero-free. Its
  missing root invalidates count completeness and (3).
* **Boundary root:** H(z)=z-1 on |z|<=1 has zero minimum modulus;
  the strict contour gate must reject it, regardless of numerical samples.
* **Collision:** H_eta(z)=z^2+eta has U=1 after both roots are removed,
  but its roots move on the sqrt(eta) scale. Its factor floor may pass;
  root acquisition and the Green value still pay that motion. A real
  double has zero interior Green mass and is not excluded by this method.

If a control has a positive-depth zero inside D, a correct complete
upper cannot pass below m. Which acquired value or error gate fails
must be determined from that control's actual data, not inferred merely
by naming its absent theta identity. Its event time is not moved to zero.

## 9. Completion, limits and next decision

B05 r2 completes the **design** requested after E07: it replaces an
unspecified regular minimum by (3), makes curvature depend on the
acquired logarithmic oscillation, pays local polynomial derivative
errors, and exposes all cost terms. This is not a canonical certificate,
a measured speedup, a favorable signed value or a universal exclusion of
other methods. No manuscript milestone or investigation closure occurs.

The first unmeasured questions are whether the specified polynomial
errors are below the selected contour margins, whether complete tiny
cluster counts and (6) pass, and whether lambda<=32 and H<=256 hold
within a useful acquisition budget. Testing all 264 patches before
learning those costs is not justified by the panel arithmetic alone.

[E08 Request26][request] therefore fixes three existing-cover centers
113/4,121/4,383/4, plus the c=30 direct comparator. It first checks the
new analytic interface and then measures only these acquisitions, with
finite precision, contour and source-panel limits. A pass is local pilot
feasibility; it neither validates the remaining 261 patches nor estimates
a total runtime by multiplying three observations. A hard failed bound
or unresolved cap is a useful return. Full integration requires a later
explicit contract after this result. [Continuation16][next] supplies the
model-change prompt; the [sole register][progress] owns live status.

[results]: ../../../../../../result-summaries/README.md
[heat]: ../../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md
[controls]: ../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../avoid/README.md
[a01]: ../../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a11]: ../../../../../../avoid/11_certifying_the_known_and_tests_that_cannot_fail.md
[e03]: 06_TND_OG_E03_COMPLETE_SIGNED_LOG_ACQUISITION_20261108.md
[siblings]: 10_TND_OG_B06_SIBLING_RESULTS_AND_GREEN_CENSUS_TRANSFER_20261110.md
[sources]: ../references/11_TND_OG_B05_R2_CONTOUR_AND_POLYNOMIAL_SOURCE_USE_20261110.md
[record]: ../numerics/08_TND_OG_B05_R2_EXACT_DESIGN_RECORD_20261110.json
[request]: ../research-progress/handoffs/26_TND_OG_E08_LITERAL_SOURCE_ACQUISITION_PILOT_REQUEST_20261110.md
[next]: ../continuation-notes/16_TND_OG_B05_R2_RESULTS_AND_MODEL_CHANGE_20261110.md
[progress]: ../research-progress/01_TND_OG_GREEN_RESOLVENT_RESEARCH_PROGRESS_20261107.md
