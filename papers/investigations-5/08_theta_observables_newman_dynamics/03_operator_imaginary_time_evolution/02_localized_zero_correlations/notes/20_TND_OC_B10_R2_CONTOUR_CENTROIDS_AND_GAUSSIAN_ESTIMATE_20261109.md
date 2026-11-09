# B10 r2: contour counts and centroids for the Gaussian pair projection

9 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex assistance, OC chat0009. Recorded current thread
settings `gpt-6-astra / max`; per-turn backend configuration
is unavailable in the public-history adapter. Root is the sole writer;
no delegation or model change.

**Disposition: B10 r2 complete at analytical design/conditional-contract
scope.** One source mechanism was selected and tested. The conditional
error theorem and explicit theta tail below are **proved in-note,
proof-author checked**, with exact-rational constant checks. No canonical
count, contour certificate, centroid or pair value has been computed.
[Execution E13 r1][request] is ready for a bounded Sol pass.

Read the [result index][results] and [avoid index][avoid], especially
[theta14][theta], [geometry13][geometry], [controls12][controls],
[classification01][a01], [premises02][a02], [scope07][a07] and
[numerical purpose11][a11]. Classification: a quantitative finite
acquisition contract, not an RH-equivalent criterion or asymptotic
correlation claim. Its acceptance target is the declared projected
canonical value, not another verification of known low-height realness.

## 1. The additional source information and its limits

The added input is **an exact contour count and a certified first complex
power sum for every occupied small cell**, together with a complete outer
count. For a cell C with geometric center \(a_C\), set
\[
 Z(z)=\zeta(1/2-iz/2),\qquad
 n_C=\frac1{2\pi i}\oint_{\partial C}\frac{Z'}Z\,dz,\quad
 q_C=\frac1{2\pi i}\oint_{\partial C}(z-a_C)\frac{Z'}Z\,dz .
 \tag{1}
\]
On the zero-free boundary these give
\[
 n_C=\#\{j:z_j\in C\},\qquad
 q_C=\sum_{z_j\in C}(z_j-a_C),\qquad
 c_C=a_C+q_C/n_C\quad(n_C>0).                         \tag{2}
\]
Counts include multiplicity. The residue of \(Z'/Z\) at a zero of
multiplicity m is m; multiplying by \(z-a_C\) proves the second formula.
This reuses the classical argument principle, not a new identity about
zeta. [B07][b07] already uses complete contour counting. The new
acquisition design uses **cluster centroids and their first-order
cancellation**, without requiring each cell to contain a single simple
real zero or resolving its internal zeros.

Use the complete-source identity \(H_0(z)=\xi(1/2-iz/2)/8\).
In the rectangle below, the completion factors are holomorphic and
nonzero, and Z has no pole or trivial zero. Thus (1) computes the actual
theta divisor's counts and first moments. The extra logarithmic
derivative of a nonvanishing completion factor has zero integrals
against 1 and \(z-a_C\). [Source-use14][sources] records the primary
argument-principle and series-evaluation inputs.

This is a **finite source evaluator**. It obtains stronger local
information from the exact canonical function and then contracts it.
It is not a new prime asymptotic, a closed stochastic law, or a prediction
of unknown zero configurations without inspecting the source. It is
distinct from the old mixed-moment/Laplace reformulations because its
inputs have a specified acquisition algorithm and finite success/failure
gates. No claim of literature novelty or measured runtime saving is made.

## 2. Preserve the r1 observable exactly

Freeze \(T=1000,\ell=1,h=1,\epsilon=1/4\), the same uniform center law
and the single blurred, separately marked projection \(P_T\) of
[Note19 (4)][n19]. The equality \(\ell=1\) follows from
\(\log1000<12<4\pi\). Define for arbitrary complex z=x+iy and w=x'+iy'
the smooth real kernel
\[
 \begin{split}
 K(z,w)&=\frac{c_G}{T}\int_T^{2T}
 e^{-(x-X)^2/2}e^{-(x'-X)^2/2}
 e^{-4(x-x')^2/9}b_+(y)b_-(y')\,dX,\\
 c_G&=32\sqrt2/51<1,\qquad
 b_\pm(y)=e^{-(8/17)(y\mp1/2)^2}.
 \end{split}                                                   \tag{3}
\]
On the canonical divisor it includes exactly the original height weights
and blur, because all imaginary marks lie in \((-1,1)\), where
\(\kappa_0=1\). Extending the formula smoothly outside that strip is only
for evaluating certified approximating centroids; no approximant strip
theorem or new point-process law is inferred.

Set \(m=(x+x')/2,d=x-x'\). The exact center integral is
\[
 K(z,w)=c_G I_T(m)e^{-25d^2/36}b_+(y)b_-(y'),\quad
 I_T(m)=\frac{\sqrt\pi}{2T}
 [\operatorname{erf}(2T-m)-\operatorname{erf}(T-m)].      \tag{4}
\]
Therefore \(P_T=\sum_{j\ne k}K(z_j,z_k)\).
The finite center edges, full observation plane, observation blur, both
imaginary-mark tests and all distinct multiplicity labels are unchanged.
No frequency cutoff, unblurring or center quadrature is used in (4).

For the scalar \(D(z)=K(z,z)\),
\[
 D(x+iy)=c_G I_T(x)e^{-4/17}e^{-16y^2/17}.              \tag{5}
\]
This is the exact weighted self term, not a square of just one mark
factor. The projected target is still distinct from a full \(Q^2\)
profile.

## 3. An explicit canonical tail, with no unmeasured count constant

The complete positive theta source from [Note02 §4][n02] has
\[
 \Phi(u)=e^u\sum_{l\ge1}(2l^4r_u^2-3l^2r_u)e^{-l^2r_u},
 \qquad r_u=\pi e^{4u},\quad u\ge0 .
\]
Its inherited majorant gives
\(\Phi(u)\le5C_2(0)e^u r_u^2e^{-r_u}<10e^u r_u^2e^{-r_u}\):
the geometric bound
\(C_2(0)\le(1-16e^{-3\pi})^{-1}<2\) follows already from
\(3\pi>9\) and \(e>2\).

Let \(\mathcal M=\int_0^\infty e^{u^2}\Phi(u)\,du\).
Since \(u^2\le r_u/12\), substitution \(v=r_u\) yields
\[
 \mathcal M
 \le\frac{10}{4\pi^{1/4}}\int_\pi^\infty v^{5/4}e^{-11v/12}\,dv
 <5(12/11)^3<7.                                      \tag{6}
\]
Here \(e^{2u}\ge2u\) and \(\pi>3\) prove the first inequality in the
exponent; \(v^{5/4}\le v^2\) for \(v\ge\pi\), followed by extending
the \(v^2\) integral to zero, proves the last bound.
This is only a source majorant, not a change of observation time.

On \(0\le u\le1/10\), \(3<r_u<8\), and the first source term is
at least \(9e^{-8}>9/3^8\); every other term is positive. Thus
\[
 H_0(0)>1/7290>10^{-4},\qquad \log(\mathcal M/H_0(0))<20.       \tag{7}
\]
The elementary bounds \(e^{2/5}<2\), \(\pi<4\), and \(e<3\)
suffice. The ratio is less than \(70000<2^{20}<e^{20}\).

For \(|z|\le2r\), Young's inequality and positivity give
\(|H_0(z)|\le e^{r^2}\mathcal M\). Jensen at zero therefore bounds the
number \(N_{\rm disk}(r)\) of all zero labels in \(|z|\le r\) by
\[
 N_{\rm disk}(r)\log2\le r^2+20,\quad
 N_{\rm disk}(r)\le2r^2+40.                            \tag{8}
\]
Boundary zeros are handled by a larger-radius limit. Since the canonical
divisor is in \(|\Im z|<1\), each real unit slab starting at q contains
at most
\[
 16(|q|+2)^2                                             \tag{9}
\]
labels: it lies in the disk of radius \(|q|+2\), and (8) is even smaller.
This deliberately coarse *global* bound is sufficient for a Gaussian
tail and requires no numerical value for Note18's A.

Let
\[
 \mathcal R=\{988<\Re z<2012,\ |\Im z|<3/2\}.
\]
For \(X\in[1000,2000]\), every omitted label has \(|x_j-X|\ge12\).
Two unit slabs per shell and (9) give omitted height weight at most
\[
 b=32\sum_{n=12}^\infty(2003+n)^2e^{-n^2/2}<2^{-44}.   \tag{10}
\]
For the stated strict bound write \(n=12+j\), use
\(e^{-n^2/2}\le2^{-72}2^{-12j}\), and
\((2015+j)^2\le2015^2(1+j)^2\).
With \(q=2^{-12}\), \(\sum(1+j)^2q^j=(1+q)/(1-q)^3<2\);
also \(2015<2^{11}\). These give (10) using rational arithmetic.

If the complete count in \(\mathcal R\) is \(N\le1024\), then the
retained weight is at most N. At least one factor of each omitted
ordered pair comes from (10), so
\[
 0\le P_T-P_T^{\mathcal R}
 \le2c_G(N+b)b<2^{-32}.                              \tag{11}
\]
No labels at negative heights or beyond the finite slab were silently
discarded. The count cap is an execution gate, not an observed count.

## 4. Centroids change the transport allowance from first to second order

All derivatives here are real two-coordinate derivatives. The following
global bounds for (3) and (5) suffice:
\[
 \|\nabla_zK\|,\|\nabla_wK\|\le9/T,\quad
 \|D_z^2K\|_{\rm op},\|D_w^2K\|_{\rm op}\le18/T,\quad
 \|\nabla D\|\le4/T,\quad \|D^2D\|_{\rm op}\le10/T.     \tag{12}
\]
For clarity \(D^2D\) denotes the Hessian of the scalar function D.

Here is a direct check. Put \(w(s)=e^{-s^2/2}\) and
\(g(d)=e^{-4d^2/9}\). Each of \(w,g,b_\pm\) and their first and
second derivatives has absolute value at most 1. In differentiating
with respect to z, leave the other height weight unbounded by 1 and
integrate it: \(\int_{\mathbb R}w(x'-X)dX=\sqrt{2\pi}<3\).
The gradient components of K are at most \(6/T,3/T\) and its Hessian
entries \(12/T,6/T,3/T\) in xx,xy,yy. The maximum absolute row sum
gives \(18/T\); the w-variable calculation is identical.
For D, use
\[
 |I_T|\le2/T,\quad |I_T'|\le2/T,\quad |I_T''|\le8/T
\]
by integration over the full line, and
\(|(e^{-16y^2/17})'|\le1,\ |(e^{-16y^2/17})''|\le2\).
The corresponding Hessian entries are at most \(8/T,2/T,4/T\).
This proves all of (12), including the finite center edges.

Partition the retained divisor into disjoint convex cells C, each of
diameter at most \(r=2^{-12}\), with counts \(n_C\) and exact centroids
\(c_C\) from (2). Convexity gives \(c_C\in C\). Put
\[
 S_2=\sum_C\sum_{z_j\in C}|z_j-c_C|^2\le Nr^2.
\]
For any real \(C^2\) test F, Taylor expansion and
\(\sum_{j\in C}(z_j-c_C)=0\) give
\[
 \left|\sum_{j\in C}F(z_j)-n_CF(c_C)\right|
 \le\frac12\sup_C\|D^2F\|_{\rm op}
                  \sum_{j\in C}|z_j-c_C|^2.          \tag{13}
\]
The complex first moment cancels **both** real components of the linear
term. It is the unweighted centroid; all window and mark weights remain
inside F.

Apply (13) successively to the two variables of the *raw* all-label
double sum. Each application costs at most \(9NS_2/T\). Apply it to
the self term D at cost \(5S_2/T\). Consequently, for
\[
 P_{\rm bar}=\sum_{C,E}n_Cn_EK(c_C,c_E)-\sum_Cn_CD(c_C),
\]
\[
 |P_T^{\mathcal R}-P_{\rm bar}|
 \le\frac{18N+5}{T}S_2
 \le\frac{18N^2+5N}{T}r^2.                           \tag{14}
\]
Within a cell the coefficient is \(n_C(n_C-1)\), even though distinct
zeros have been deliberately collapsed. Its error is paid by (14);
no artificial multiple zero is asserted to be a canonical one.

If exact dyadic approximations \(\widehat c_C\) obey
\(|\widehat c_C-c_C|\le\sigma=2^{-24}\), the gradient bounds give
\[
 |P_{\rm bar}-\widehat P|
 \le\frac{18N^2+4N}{T}\sigma,\quad
 \widehat P=\sum_{C,E}n_Cn_EK(\widehat c_C,\widehat c_E)
                         -\sum_Cn_CD(\widehat c_C).  \tag{15}
\]
This bound uses the same centers in each pair through K, not independent
center averages. The self term is subtracted with n_C, not n_C squared.

For comparison, the elementary count-only/representative-location
allowance on this **same projection** is
\((18N^2+4N)r/T\), equal to \(4609/1000\) at the frozen caps.
The added first moments replace that first-order uncertainty by
(14)–(15). This is a gain in an error allowance from stronger certified
input; it is not a lower bound on actual count-only error or proof that
centroid acquisition costs less than another algorithm.

## 5. A paid conditional \(P_{1000}\) estimate

Combine (11), (14), (15). Under the count, cell and centroid gates,
\[
 |P_{1000}-\widehat P|
 \le \frac{36(1024)^2+9(1024)}{1000\,2^{24}}+2^{-32}
 <\frac1{400}.                                       \tag{16}
\]
If a certified evaluation of the finite erf/exponential sum
\(\widehat P\) has radius at most \(1/400\), then adding (16) gives
\[
 \boxed{\text{a canonical enclosure for }P_{1000}
                     \text{ of radius }<1/200<1/100.}         \tag{17}
\]
[The exact-rational replay][check] verifies these constant comparisons;
its [record][record] is not a theta certificate.

| Cost | Payment |
| --- | --- |
| Omitted labels on the complete divisor | \(<2^{-32}\), via the explicit complete-theta Jensen bound |
| Cluster replacement | \((18N^2+5N)r^2/T\) |
| Contour first-moment/centroid enclosure | \((18N^2+4N)\sigma/T\), after certified \(\sigma\le2^{-24}\) |
| Complete source | Exact zeta access through the full theta identity; every ball includes the library remainder and rounding |
| Final finite sum | Certified radius \(\le1/400\) |
| Observation blur, center edges, frequency | Exact in (3)–(4); no such truncation or unsmoothing is performed |

This reallocates r1's error ledger using a different acquisition proof,
without changing its observable. It can evaluate the contracted canonical
quantity directly; it does not acquire the entire mixed-log array or a
uniform-in-frequency version of Note19 (14).

The interior log singularity error has not been assumed small or dropped:
no approximation to \(\log|H_0|\) inside a cell is made. Instead the
contours must have paid nonvanishing and interval moment integrals.
Arbitrarily small interior gaps and multiple zeros are allowed. Tiny
values **on the proposed contours** can cause the finite algorithm to
fail; the proof contains no guaranteed contour floor. A truncated theta
implementation would need both arithmetic/radial tails, derivative
remainders and a justified ratio error; it is not a free substitute for
the frozen exact-zeta access route.

## 6. Executable acquisition, before changing models

[Request27][request] freezes one E13 pilot. Use source ball arithmetic
to count the whole fixed rectangle, then recursively subdivide it,
discarding only cells whose complete count is zero. Subdivide occupied
cells until their diameter is at most \(2^{-12}\); counts need not be
one. Try at most the three declared dyadic cut fractions if a cut cannot
be certified free of zeros. Require all child counts to sum to the
parent count and all occupied leaf counts to sum to the outer N.

For each occupied leaf compute the **centered** integral \(q_C\) in (1).
A specified validated midpoint rule suffices: on a segment of length L,
with midpoint z_m and
\(G_C(z)=(z-a_C)Z'(z)/Z(z)\),
\[
 \left|\int_{\text{segment}}G_C(z)\,dz
       -(z_1-z_0)G_C(z_m)\right|
 \le \frac{L^3}{24}\sup_{\text{segment}}|G_C''(z)|.     \tag{18}
\]
This follows from the real interval midpoint remainder applied to the
straight-line parameter; the complex magnitude bound follows from its
integral remainder. Enclose Z and its first three derivatives on the
entire segment using a complex-ball power series through cubic order.
Formal division supplies the second derivative of G_C only after its
denominator enclosure excludes zero. Sum certified segment balls and
(18), divide by \(2\pi i n_C\), and include rounding to the exact dyadic
\(\widehat c_C\). Refine until the **Euclidean** centroid error is at
most \(2^{-24}\). The same source segment certificates support B07's
branch-safe winding count. Endpoint-only nonvanishing is insufficient.

The packet fixes precision, subdivision and evaluation caps, a
30-minute acquisition/evaluation wall-clock ceiling, replayable records
and one bounded repair. These are ceilings, not measured costs.
The inspected default python3 lacks python-flint; E13 includes runtime
preflight and isolated setup, or an explicit environment failure.
No canonical function was evaluated in r2.

## 7. Controls, status and the next task

The analytical screen uses [controls12][controls]; no original collision
certificate was rerun.

| Control class | Canonical premise absent; effect on the mechanism |
| --- | --- |
| Euler-factor | Unmodified complete theta/zeta identity fails. Its own contour counts and centroid transport can still be valid; a collision is not rejected. |
| Weighted-square / finite-tail / finite-prime orbit | Full normalized reflection or complete unit-coefficient identity fails. The canonical strip and numerical source majorants cannot be assigned to those controls without proof. |
| Reflected super-Gaussian / smooth positive shape / positive primitive | Complete arithmetic theta expansion fails. Classical residues and Taylor cancellation survive on paid finite contours. |
| Atomic / finite-profile threshold | Complete theta growth/profile fails. Snapshot cluster counting does not require eventual simplicity. |
| RH-conditional theta-close endpoint | Ordinary Dirichlet-series arithmetic fails; multiple labels remain admissible. |
| Variable observation kernel | Physical cosine/Newman equation fails. That equation is not used by the snapshot centroid lemma, so the lemma need not distinguish the control. |
| Fractional-profile relaxation | Integer-divisor realizability fails; it supplies no integer winding count for the proposed factorial census. |

For \(F(z)=(z-a)^m\), a surrounding contour has count m and centered
moment \(m(a-a_C)\). The estimator retains \(m(m-1)\).
For \(F(z)=(z-a)^2-\delta^2\), a cell enclosing both zeros has centroid
a for real or imaginary \(\delta\). Taylor's quadratic allowance covers
both configurations. These exact local controls show that the mechanism
does not infer simplicity, realness or collision exclusion. They do not
satisfy the canonical source identity and are not theta examples.

**Next: [E] TND-OC-E13 r1 — GPT-6.1 Sol.** Check the fixed proof and run
one certified cluster-count/centroid pilot. Return an enclosure satisfying
(17), or the exact failed gate with observed work. A success is a finite
canonical projected value; a failure is scoped to the declared method,
domain and caps. Need for a new source access method, observable, larger
budget or analytical repair beyond the fixed allowance returns to B10 r3.

[Self-check16][review] is proof-author checking, not independent acceptance.
No E13 execution, manuscript milestone, investigation closure or root
summary promotion occurs here. E09 remains the separate optional
compact-window evaluator. [Continuation23][cont] records the model handoff.

[results]: ../../../../../../result-summaries/README.md
[avoid]: ../../../../../../avoid/README.md
[theta]: ../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[geometry]: ../../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[controls]: ../../../../../../result-summaries/12_collision_controls_and_screening.md
[a01]: ../../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a11]: ../../../../../../avoid/11_certifying_the_known_and_tests_that_cannot_fail.md
[n19]: 19_TND_OC_B10_R1_GAUSSIAN_CONTRACTION_AND_MISSING_ESTIMATE_20261109.md
[n02]: 02_TND_OC_LOCAL_LOG_TRANSFER_20261107.md
[b07]: 13_TND_OC_B07_COMPLETE_DIVISOR_AND_GAUSSIAN_EVALUATOR_20261108.md
[sources]: ../references/14_TND_OC_B10_R2_CONTOUR_MOMENT_SOURCE_USE_20261109.md
[check]: ../numerics/check_b10_r2_cluster_constants.py
[record]: ../numerics/16_TND_OC_B10_R2_EXACT_CONSTANTS_20261109.json
[request]: ../research-progress/handoffs/27_TND_OC_E13_R1_CONTOUR_CENTROID_EVALUATOR_REQUEST_20261109.md
[review]: ../reviews/16_TND_OC_B10_R2_CONTOUR_CENTROID_SELF_CHECK_20261109.md
[cont]: ../continuation-notes/23_TND_OC_AFTER_B10_R2_CLUSTER_MOMENTS_AND_MODEL_CHANGE_20261109.md

