# Canonical anchors, finite root products, and isolated-event amplitude floors

22 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Recorded model **gpt-6.1-sol (Codex), reasoning effort ultra**, verified by the parent research turn. **Status: proved in-note in the declared finite-root or isolated-event classes; separate same-model proof audits pass.** These are quantitative lower bounds in declared finite root or isolated-event classes. No zero separation, isolation distance, or all-height theorem is acquired here.

Read the [result index][results], [collision controls][controls], and [avoid index][avoid], particularly patterns 01, 02, 07, 08 and 12. This continues [RHE Notes 09][rhe09]--[11][rhe11] beyond upper moments: a positive canonical value anchor fixes the otherwise missing amplitude normalization, while an explicit root-distance payment remains. The [BW10 complete root/tail note][bw19] supplies the exact paired product, Jensen count and complete inverse-square tail. The [home 10 signed-tail pilot][signedtail] is a different finite moment interface and is not restarted.

## 1. Declared real-root slice and a complete positive anchor

Let \(0\le t\le T\) and assume the canonical slice \(H(t,\cdot)\) has only real zeros. Under RH this applies at time zero and all later times; positive-time simplicity is already an imported classical fact. For an ordinary multiple endpoint under RH the relevant hypothetical slice is time zero, not a newly alleged positive-time double. The fixed-slice derivations also apply at a separately supplied all-real threshold slice.

Write its positive zeros, with multiplicities, as \(r_j>0\). Canonical source positivity gives \(H(t,0)>0\), so zero is not a root. Evenness and order at most one give the paired product from [BW10 Note 19, RM5][bw19]:

\[
H(t,z)=H(t,0)\prod_j(1-z^2/r_j^2).
\tag{1}
\]

For any \(y\ge0\), \(H(t,iy)>0\). A complete explicit lower bound is

\[
H(t,iy)\ge L_y:=4h_*\frac{\sinh(y/4)}y,
\qquad
h_*:=\frac{\pi(2\pi-3)}4e^{-\pi e},
\qquad L_0=h_*.
\tag{2}
\]

Indeed on \(0\le u\le1/4\), the exact first positive theta summand satisfies
\(\Phi_1(u)\ge\pi(2\pi-3)e^{-\pi e}\), while \(e^{tu^2}\ge1\). Integrate this lower bound against \(\cosh(yu)\). All other modes and the complementary half-line are positive, hence dropping them is valid for this lower estimate. An acquired complete value anchor can replace \(L_y\); no oscillatory real-axis evaluation is required.

## 2. A full-product lower with a paid infinite tail

Fix \(A>0\), \(R>\max(2,A)\), and \(|x|\le A\). Split the complete paired product at positive root cutoff \(R\):

\[
P_R(x)=\prod_{0<r_j\le R}\frac{r_j^2-x^2}{r_j^2+y^2},
\qquad
H(t,x)=H(t,iy)P_R(x)T_R(x).
\tag{3}
\]

Let \(\mathcal B_T(R)\) be the explicit complete tail from RM4,
\(\sum_{|r|>R}r^{-2}\le\mathcal B_T(R)=2C_T(\log R+2)/R\), with \(C_T\) exactly as defined in RM1. Since each omitted paired factor is positive,

\[
\boxed{\quad
1\ge T_R(x)\ge e^{-K},
\quad K=\frac{(A^2+y^2)\mathcal B_T(R)}{2(1-A^2/R^2)}.
\quad} \tag{4}
\]

For a single omitted positive root put
\(u=(x^2+y^2)/(r_j^2+y^2)\in[0,1)\). The inequality
\(\log(1-u)\ge-u/(1-u)\) gives
\(\log[(r_j^2-x^2)/(r_j^2+y^2)]\ge-(A^2+y^2)/[(1-A^2/R^2)r_j^2]\).
Sum over positive roots and use half of RM4, which counts both signs. This proves (4), including its factor two. All omitted roots and their multiplicities are paid.

Thus, including a zero by removable continuation,

\[
 |H(t,x)|\ge L_y e^{-K}|P_R(x)|. \tag{5}
\]

This is not an interior field floor on a set containing zeros; its finite product explicitly vanishes at them.

## 3. A finite positive-time Laguerre floor

Suppose the head roots are simple, as they are at positive time under RH. Let \(\mathcal R_R=\{\pm r_j:0<r_j\le R\}\), with \(N=|\mathcal R_R|\). Define the removable polynomial

\[
D_R(x)=\sum_{r\in\mathcal R_R}
             \left[\frac{P_R(x)}{x-r}\right]^2.
\]

The all-real product gives
\(Q=H'^2-HH''=H^2\sum_{r\in\mathbb R:H(r)=0}(x-r)^{-2}\) off the roots. Discard only positive tail summands and apply (4)--(5). Continuity through each root then proves

\[
\boxed{\quad
Q(t,x)\ge L_y^2e^{-2K}D_R(x)\qquad(|x|\le A).
\quad} \tag{6}
\]

If the finite head is nonempty and simple, \(D_R>0\) on every real compact interval: away from roots each summand is positive; at a root the corresponding removable term is nonzero. A rigorous finite polynomial minimum, with root/acquisition errors propagated, supplies an explicit \(q_*\) for [RHE Note 11][rhe11]. This replaces an oscillatory direct Q acquisition by finite root data and a positive canonical anchor, but does not make the root data or minimum free.

For an adjacent cap \([a,b]\subseteq[-A,A]\) with both endpoints in the head, an explicit closed lower exposes the separation cost. Write
\(P_R(x)=\kappa\prod_{r\in\mathcal R_R}(x-r)\), where
\(|\kappa|=\prod_{0<r_j\le R}(r_j^2+y^2)^{-1}\). Then

\[
\boxed{\quad
\min_{[a,b]}D_R\ge
 \frac{\kappa^2}{2^{2(N-1)}}
 \min_{s\in\{a,b\}}\prod_{r\in\mathcal R_R\setminus\{s\}}|s-r|^2.
\quad} \tag{7}
\]

To prove it, choose a nearest head root to x; by adjacency it is a or b. For every other r, nearest-root choice and the triangle inequality give \(|x-r|\ge|s-r|/2\). Retain that summand in \(D_R\). The product in (7) includes \((b-a)^2\): it explicitly pays the necessary loss when the pair coalesces. Higher near-collisions elsewhere require their own distances as well. A sharper acquired minimum of \(D_R\) may substantially improve this deliberately coarse closed bound.

## 4. Event-curvature lower without individual head-root acquisition

Here the new hypothesis is an **explicit isolated-event class**. Assume a slice as in Section 1 has an exact ordinary double at \(a\in(0,A]\). Delete the two copies of a; assume every other real zero, including the two mirror copies at -a, is at distance at least \(\rho>0\) from a. This isolation is neither proved by RH nor supplied by an upper moment. It must be independently paid or kept conditional.

Choose \(R>\max(2,A)\), and let \(n_R\) be any explicit upper on the full zero count in \(|z|\le R\), for example the integer floor of RM3's sharper bound

\[
 N_t(R)\le\frac{A_T+(R/2)\log R}{\log2}.
\]

Here \(A_T\) is RM1's growth constant, not the event-height A. Set

\[
 K_R=\max\{0,\lfloor n_R/2\rfloor-2\},
 \quad \theta=\min\{1,\rho^2/R^2\},
 \quad K_0=\frac{A^2\mathcal B_T(R)}{2(1-A^2/R^2)}.
\]

There are four counted roots at \(\pm a\), each double; therefore any actual event in this class has \(n_R\ge4\). Factor the two copies of the positive root a out of (3), with y=0. Taking the coefficient at a gives exactly

\[
\frac{|H_{zz}(t,a)|}{2}
 =\frac{4H(t,0)}{a^2}
 \prod_{\substack{0<r_j\le R\\r_j\ne a\text{ (two deleted copies)}}}
       \left|\frac{r_j^2-a^2}{r_j^2}\right|
 \ T_R(a).
\tag{8}
\]

For every remaining positive head root both \(|a-r_j|\) and \(|a+r_j|\) are at least \(\rho\), by the stated full-root isolation. Each absolute factor in (8) is therefore at least \(\rho^2/R^2\), hence at least \(\theta\). The number of remaining positive factors, with multiplicities, is at most \(K_R\). Use \(0<\theta\le1\), (2), (4), and \(a\le A\) to obtain

\[
\boxed{\quad
|H_{zz}(t,a)|\ge h_{2,*}:=
 \frac{8h_*}{A^2}e^{-K_0}\theta^{K_R}>0.
\quad} \tag{9}
\]

Thus canonical normalization, a complete Jensen/tail budget, bounded event height and **declared isolation** give an explicit curvature lower. No individual finite head root and no assumed lower for Hzz enters (9). The price \(\theta^{K_R}\) makes the weakness for high counts or small isolation visible; the bound is not claimed practically sharp.

The stronger pointwise imaginary-anchor variant of (8)--(9) is

\[
|H_{zz}(t,a)|\ge
 \frac{8a^2L_y}{(a^2+y^2)^2}
 e^{-K(A,y,R)}
 \min\{1,\rho^2/(R^2+y^2)\}^{K_R}. \tag{10}
\]

An event-height interval can be propagated through the displayed rational factor. The y=0 bound (9) already supplies a complete uniform constant for the isolated bounded-height class. This is not a source-only lower over all possible events: removing the isolation premise removes the proof.

## 5. Uniform positive-time floors on the born cap of that class

Let \(\alpha_*=h_{2,*}/2\). With complete moments
\(M_j=M_{j,1}(T+1)\), define

\[
 r_* =\min\{1,\alpha_*/(4M_3)\},
\]
\[
 \sigma_* =\min\left\{
 \frac35,\frac{3\alpha_*r_*^2}{8M_2},
 \frac{\alpha_*r_*}{4M_3},\frac{\alpha_*}{4M_4}\right\}.
\tag{11}
\]

These are uniform choices for the [manuscript's complete-source ordinary-event chart][chart], since its actual coefficient \(A_e=H_{zz}(t,a)/2\) obeys \(|A_e|\ge\alpha_*\). At every \(0<\tau\le\sigma_*\), the two born roots are real and simple in the fixed disk. Put \(G(x)=\operatorname{sign}(A_e)H(t+\tau,a+x)\), let k be its unique critical point in that pair, and write \(v=-G(k)>0\). The chart gives

\[
 G''\ge c:=3|A_e|/2,
 \qquad 3|A_e|\tau/2\le v\le5|A_e|\tau/2.
\]

For any point of the root-to-root cap put \(u=G(x)-G(k)\in[0,v]\). Integrating \(d(G'^2)/dG=2G''\) on either side of k gives \(G'^2\ge2cu\). Consequently,

\[
 Q=G'^2-GG''\ge2cu+c(v-u)\ge cv,
\]

and hence the explicitly paid physical Laguerre floor is

\[
\boxed{\quad Q(t+\tau,x)\ge\frac94\alpha_*^2\tau
       \qquad\text{on the complete born cap}.\quad} \tag{12}
\]

Furthermore \(v\le c\) because \(\tau\le3/5\). Therefore
\(E=G^2+G'^2\ge(v-u)^2+2cu\ge v^2\), and

\[
\boxed{\quad |H(t+\tau,k)|\ge\frac32\alpha_*\tau,
\qquad E(t+\tau,x)\ge\frac94\alpha_*^2\tau^2.
\quad} \tag{13}
\]

The critical value and the physical jet now have quantitative lower bounds in this declared class. Substitution into Note 11 legitimately pays its previously missing denominator, with the necessary inverse-time scale \(q_*^{-1}=O(1/\tau)\). It does not remove that scale, contradict the compatible Hermite profile, or supply a signed phase surplus. All constants deteriorate with the stated isolation/count/height inputs; no endpoint-uniform positive E is claimed.

## 6. An unconditional finite-chart Harnack alternative

The real-root product is not essential if the declared isolation applies to complex roots as well. This alternative uses higher complete moments and is available **without RH**. Let the canonical slice have an exact real double at \(a\in(0,A]\), where \(A<R\) and \(R\ge2\). Let \(r_1,\ldots,r_N\) list **all complex zeros in the closed disk** \(|z|\le R\), with multiplicities. Boundary zeros are included; alternatively take zero-free radii and limits. Define

\[
 P_N(z)=\prod_{j=1}^N(z-r_j),\qquad V_N(z)=H(t,z)/P_N(z).
\]

Then \(V_N\) is zero-free in the open disk, including its removable values at the listed roots. The confluent divided-difference simplex formula gives

\[
 |V_N(z)|\le \mathcal M_N:=\frac{M_{N,R}(T)}{N!}
 \quad(|z|\le R),\qquad
 |V_N(0)|\ge h_*/R^N. \tag{14}
\]

For the first bound, \(V_N(z)=H[r_1,\ldots,r_N,z]\) is the integral of \(H^{(N)}\) over the N-simplex of volume \(1/N!\); every affine evaluation point lies in the same convex disk. Repeated roots are handled by the confluent limit. The second bound uses the **complete nonzero canonical anchor** \(H(t,0)\ge h_*\) and \(\prod|r_j|\le R^N\). In particular no listed root equals zero. Both inputs in (14) are source-controlled; neither assumes an interior H floor.

Put

\[
 \gamma=\frac{R+A}{R-A},\qquad
 \vartheta_N=\min\left\{1,\frac{h_*}{R^N\mathcal M_N}\right\},
 \qquad \nu_N=\mathcal M_N\vartheta_N^{\gamma}>0.
\]

The nonnegative harmonic function
\(\log(\mathcal M_N/|V_N|)\) obeys the disk Harnack inequality. Hence

\[
 \boxed{|V_N(z)|\ge\nu_N\qquad(|z|\le A).} \tag{15}
\]

For an actual admissible N the untruncated ratio defining \(\vartheta_N\) is already at most one by (14); the minimum makes the formula conservative for integer candidates N that do not occur. Harnack is applied to the **proved zero-free deflated unit**, not to H across its roots.

Now declare that every other complex root in \(|z|\le R\), after deleting the two copies at a, is at least \(\rho>0\) from a. Factoring at the double yields

\[
 \boxed{|H_{zz}(t,a)|
 =2|V_N(a)|\prod_{r_j\ne a\text{ (two deleted copies)}}|a-r_j|
 \ge2\nu_N\rho^{N-2}.} \tag{16}
\]

If only Jensen's source-controlled upper \(N\le n_R\) is used, a fully explicit lower is

\[
 \boxed{h_{2,\mathrm H}:=
 2\min_{2\le n\le n_R}\nu_n\rho^{n-2}>0.} \tag{17}
\]

The finite minimum is conservative; canonical evenness at a positive real double actually requires at least four counted roots. The isolation remains a declared or independently acquired **complex-root** condition. No individual root location or exact attained count is required for (17). The upper count, high derivative moments and all their source tails must still be honestly paid if numerical constants are acquired.

Equations (11)--(13) apply with \(\alpha_*\) replaced by \(h_{2,\mathrm H}/2\), now without an all-real premise for the original slice. Thus an explicitly isolated bounded-height real ordinary event has quantitative born-cap critical-value, Laguerre and physical-jet floors from the unchanged canonical source alone **within that isolation class**. No sign contradiction follows: every such ordinary event has the compatible local birth, and the same necessary \(\tau\) and \(\tau^2\) losses remain. The larger of this valid lower floor and the real-product lower floor may be used when both sets of premises hold; a matched direct estimator may use all the same information.

The [amplitude-propagation note](13_CRITICAL_AMPLITUDE_AND_PROPAGATED_LAGUERRE_FLOORS_20261022.md) strengthens the full-cap floor and carries it forward when the later slices satisfy its LP hypotheses. The [canonical bulk-mass note](14_CANONICAL_BULK_MASS_LOWER_BOUND_20261022.md) supplies a different lower, requiring no physical jet floor. [Review 07](../reviews/07_CANONICAL_AMPLITUDE_AND_BULK_LOWER_REVIEW_20261022.md) checks these distinctions.

## 7. Scope, controls and the exact residual obstacle

Equations (6)--(7) give a positive-time floor from **finite root data plus a complete canonical anchor and tail**, while (9)--(13) give a uniform curvature and born-cap amplitude floor from a **bounded isolated-event class**. Equations (14)--(17) give an unconditional complex-isolation alternative using a complete count and higher moments. These are explicit lower inequalities, not existence arguments or a tail-moment refinement of the stopped home-10 pilot. Neither dataset has been newly acquired here.

The new use of the unchanged source is its fixed positive normalization and effective growth/tail constants. The product and nearest-root arguments themselves are generic all-real entire-function arguments. Close normalized endpoint controls retain compatible multiple zeros; their own constants and isolations produce compatible bounds, not rejection. Quadratic/Hermite models check the local \(\tau\) and \(\tau^2\) powers. Euler-factor, weighted-square, finite-prime, reflected, primitive and finite-profile controls keep their distinct missing canonical premises from [cluster 12][controls]. No control receives an invented all-real slice.

The remaining root-distance payment is explicit. RM6 contains the nearby exterior interaction; RM7 pays only distant roots, and RM13 is a gap **upper**, not a lower. Those results alone do not provide the finite separations needed in (7) or the isolation \(\rho\) in (9). A separately proved dynamical or arithmetic separation estimate could supply them; this note does not rule that possibility out. Without such information the lower constants may collapse, correctly admitting a multiple endpoint. There is no all-height simplicity, RH, or later-collision conclusion.

[rhe09]: 09_SIGNED_LAGUERRE_TRANSFER_AND_COUNT_BOUND_20261022.md
[rhe11]: 11_WEIGHTED_TRACE_PAYMENT_AND_ENDPOINT_OBSTRUCTION_20261022.md
[chart]: ../manuscript/reciprocal_hodge_energy/sections/06_heat_chart.tex
[bw19]: ../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/notes/19_COMPLETE_ROOT_MOTION_AND_FINITE_TIME_BOUNDS_20261021.md
[signedtail]: ../../10_chern_hopf_integral_estimates/notes/02_COUPLED_SIGNED_THETA_TAIL_ESTIMATES_20261022.md
[results]: ../../../../result-summaries/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../avoid/README.md
