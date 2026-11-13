# RSCT-B01 r2: a signed three-height estimate and necessary background cancellation

11 November 2026, America/New_York. Prepared for **Edward Baker** with substantial OpenAI Codex LLM assistance, RSCT chat0001. Actual backend model and reasoning effort are unavailable in the recorded configuration. Type B; GPT-6 Astra/ultra was the recommendation, not verified provenance.

**Status: proved in-note from named inherited approximation inputs; same-assistant checking only.** The new quantitative output is an upper bound for a signed complete-field logarithmic difference, and the necessary noncentral contribution \(\le-1/36\) at a hypothetical all-real threshold event in the specified band. The isolated-event inference fails: an explicit positive-source threshold control satisfies the same scalar cap. No canonical collision is excluded, and no finite onset is instantiated.

This is the one supporting derivation for [Decision02](../brainstorm/notes/02_RSCT_B01_R2_SIGNED_HEIGHT_DECISION_20261111.md). [Note03](03_RSCT_B01_REFLECTED_POISSON_TEST_20261111.md) remains unchanged. Read the [result index](../../../../result-summaries/README.md), [heat-flow/RS cluster11](../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md), [controls12](../../../../result-summaries/12_collision_controls_and_screening.md), and [avoid index](../../../../avoid/README.md), especially [01](../../../../avoid/01_restating_the_target.md), [02](../../../../avoid/02_shape_only_arguments_and_the_controls.md), [07](../../../../avoid/07_scoped_exclusions_read_as_universal.md) and [12](../../../../avoid/12_term_by_term_matching_and_separate_bounds.md).

## 1. New choice, classification and domain

Keep the complete canonical theta source, \(H_0(z)=\xi((1+iz)/2)/8\), and \(\partial_T H=-H_{zz}\). The exact evolved reflected expression is [Note03 (1)–(2)](03_RSCT_B01_REFLECTED_POISSON_TEST_20261111.md), imported from [Polymath v2 §4 (35)–(39)](https://arxiv.org/html/1904.12438v2#S4). No source, clock or arithmetic coefficients are changed.

For a large real center a, select the intermediate family
\[
 L=\log(a/(4\pi)),\quad T=c/L,\quad 1/2\le c\le1,
 \qquad y\in\{4,6,8\}.                                      \tag{1}
\]
T is the same at all three points. Ultimately T may be an assumed positive threshold, but the arithmetic estimate below does not require all-realness. The all-real hypothesis enters only in §4. There is **no assertion** that every possible threshold event lies in (1). Bounded heights, c outside this interval, and the rest of the small-time domain remain uncovered.

The new observation is
\[
 W_T(a)=2\log|H_T(a+6i)|-\log|H_T(a+4i)|-\log|H_T(a+8i)|.       \tag{2}
\]
It cancels constant and linear-in-y carrier growth while keeping signed arithmetic information. This is a fixed-height acquisition estimate, not a renamed nonmultiplicity criterion. It is a different observation from Note03's pointwise Poisson mass; all-realness must justify its consumer separately. No differentiation of H is used, so no value remainder is differentiated to manufacture a derivative estimate. The only differentiated function below is an explicit nonvanishing carrier.

## 2. Complete reflected source payment at three heights

Reuse [GNP-RS E01 §§3–4, (E9)–(E19)](../../09_green_potentials_newman_flow/01_riemann_siegel_evolution/notes/03_GNP_RS_E01_UNIFORM_OUTER_BASELINE_PROOF_20261111.md), at its stated **proved in-note from inherited inputs; same-assistant** status. Its provider is [HDA Ansatz Note04, CS3/CS6](../../01_heat_density_asymptotics/ansatz/notes/04_COMPLEX_STRIP_REMAINDER_AND_BUFFERED_CROSSOVER_20261025.md), with [same-model Assessment03](../../01_heat_density_asymptotics/ansatz/reviews/03_COMPLEX_STRIP_AND_BUFFERED_CROSSOVER_ASSESSMENT_20261025.md). This is reuse, not a fresh validation of that theorem. The printed effective region of Polymath Theorem 1.3 is not silently enlarged to height eight.

Use exactly E01's carrier
\[
 C_-(T,z)=\frac{\pi^{1/4}}{32}z^{7/4}
 \exp\left[-\frac{\pi z}{8}+\frac{T}{16}(L(z)^2-\pi^2/4)
 -\frac{i z}{4}(L(z)-1)-\frac{i\pi T L(z)}{16}-\frac{7\pi i}{8}\right],
 \quad L(z)=\Log(z/(4\pi)),\quad V=H_T/C_- .                  \tag{3}
\]
The upper-half-plane branches are fixed as in that source. C_- is a nonzero elementary carrier, **not** the exact gamma factor and **not** an Euler product for H_T.

E01 states its outer comparison at y=4,8. Adding y=6 needs the following explicit check, rather than interpolating point values. CS6 already covers the whole fixed target strip with b=9 and its required enlarged buffers. For each y=4,6,8, E01's proof pays:

| Complete contribution after division by C_- | Payment, uniformly in (1) |
| --- | --- |
| Full reflected arithmetic population through the fixed chart cutoff | \(O(a^{(1-y)/4})\), hence \(O(a^{-3/4})\) or smaller |
| Retained RS correction with its true gamma factors | \(O(a^{-(y+1)/4})\) |
| Full buffered provider field error | \(O(a^{-3/4})\) |
| Removing the dominant quadratic heat weight | \(T D_2/4\), \(D_j=\sum_{n\ge2}n^{-5/2}(\log n)^j\) |
| Ordinary dominant Dirichlet tail | \((2/3)N^{-3/2}=O(a^{-3/4})\) |
| Replacing L(a+iy) by L in the shifted argument | \(D_1T|L(a+iy)-L|/4\) |

These are precisely the estimates E13–E17: all require only the displayed fixed range 4≤y≤8, not y being an endpoint. Replace E01's finite maximum B_pop over {4,8} by its maximum over {4,6,8}, and use that value in A_F and C_F. Call the resulting finite constant C_F^*. All other source constants, fractional-cutoff uniformity and onset gates remain inherited. A fixed N is used per chart; all compensating correction terms are retained at chart changes. Thus, for all sufficiently large a,
\[
 \left|V(a+iy)-\zeta\left(\frac{1+y}{2}+\frac c4-i\nu\right)\right|
 \le C_F^*/L,\qquad \nu=a/2+\pi T/8.                       \tag{4}
\]
In particular no fixed-mode limit replaces the growing reflected sum. This is an approximation to the **complete** field, not a substitution of the time-zero Euler product for H_T.

The ordinary series [DLMF 25.2.1](https://dlmf.nist.gov/25.2#E1) gives, on Re s≥5/2,
\( |\zeta(s)-1|\le7/(12\sqrt2)<1/2\).
With L>4C_F^*, (4) proves \(|V|>1/4\), so all three logarithms have the paid error
\[
 \left|\log|V(a+iy)|-\log\left|\zeta\left(\frac{1+y}{2}+\frac c4-i\nu\right)\right|\right|
 \le4C_F^*/L.                                             \tag{5}
\]
This floor is only at the three off-axis points. It assumes neither a real-axis arm floor nor simple zeros. Their logarithmic errors in (2) cost at most 16C_F^*/L.

The carrier is not dropped. Write u(y)=log|C_-(T,a+iy)| and g(z)=log C_-(T,z). Direct differentiation yields
\[
 g''(z)=-\frac7{4z^2}+\frac{T(1-L(z))}{8z^2}
        -\frac i{4z}+\frac{i\pi T}{16z^2},\qquad u''(y)=-\Re g''(a+iy).
\]
For L≥16, 4≤y≤8 and (1), enlarge the finite onset to ensure T|L(z)|≤2. Using |z|≥a and \(|\Re(-i/z)|=y/|z|^2\) gives \(|u''|\le5/a^2\). The second-difference integral with step two then gives
\[
 D_C:=2u(6)-u(4)-u(8),\qquad |D_C|\le20/a^2.               \tag{6}
\]
Thus both gamma-scale curvature and the full source remainder are paid. No spatial-derivative error of H is required by this finite-value observation.

## 3. Signed arithmetic formula and an explicit cap

The [Euler product, DLMF 25.2.11](https://dlmf.nist.gov/25.2#E11), is used only at Re s≥5/2. Expanding its absolutely convergent logarithm gives coefficients \(q_n=\Lambda_{\rm vM}(n)/\log n\in[0,1]\). Combining the three logarithms **before bounding them** gives
\[
 W_T(a)=-\sum_{n\ge2}q_n n^{-5/2-c/4}(1-n^{-1})^2
                  \cos(\nu\log n)+D_C+e,
 \qquad |e|\le16C_F^*/L.                                  \tag{7}
\]
The signed coefficient is 2n^{-1}−1−n^{-2}=−(1−n^{-1})². The same phase ν occurs at every height, including its heat correction. Equation (7) retains the complete signed series; it does not claim a favorable sign for the individual cosines.

After this cancellation, the elementary absolute envelope is small enough for a quantitative comparison. The function f(x)=x^{-5/2}(1−x^{-1})² decreases for x≥2, so
\[
 \sum_{n\ge2}q_n n^{-5/2-c/4}(1-n^{-1})^2
 \le f(2)+\int_2^\infty f(x)\,dx
 =\frac{389}{1680\sqrt2}<\frac16.                          \tag{8}
\]
For example, the integral is 71/(420√2) and f(2)=1/(16√2); the final strict comparison follows from \(2334^2<2\cdot1680^2\). No sampled zeta value or numerical experiment is involved. For an integer M≥2 the series tail is at most
\[
 \frac{M^{-3/2-c/4}}{3/2+c/4},                             \tag{9}
\]
by the same absolute convergence. A future finite evaluation would add this payment; no such evaluation is needed here.

The resulting full-field bound is
\[
 |W_T(a)|<\frac16+\frac{16C_F^*}{L}+\frac{20}{a^2}.
                                                                  \tag{10}
\]
In addition to inherited gates, require
\[
 \frac{16C_F^*}{L}+\frac{20}{a^2}\le\frac1{72},\qquad a^2\ge288.
                                                                  \tag{11}
\]
These hold uniformly for all sufficiently large a and c∈[1/2,1], but the inherited onset is **not numerically instantiated**. They imply W_T(a)<13/72. This is a new application of the inherited outer comparison, not a new full RS provider or zero-free region.

## 4. Exact all-real consumer and the 1/36 consequence

Now impose T=Λ>0 and all zeros of H_T real. The paired product of [Polymath v2, proof of Proposition 3.1 after (33)](https://arxiv.org/html/1904.12438v2#S3) gives, with all zeros r repeated by multiplicity,
\[
 W_T(a)=\sum_r K(a-r),\qquad
 K(d)=\frac12\log\frac{(d^2+36)^2}{(d^2+16)(d^2+64)}.       \tag{12}
\]
Constants in the product cancel because 2−1−1=0. Since K(d)=−4/d²+O(d^{-4}), the sum is absolutely convergent. The all-real assumption is what identifies each contribution with this real-distance kernel. It does **not** make that kernel nonnegative.

At a multiplicity-m event, m≥2, evenness gives m copies also at −a. With all copies at ±a removed, set
\[
 R_T(a)=\sum_{r\ne\pm a}K(a-r).
\]
The exact decomposition is
\[
 W_T(a)=m\,[K(0)+K(2a)]+R_T(a),\qquad K(0)=\log(9/8)>1/9. \tag{13}
\]
For d²≥64, writing the kernel as one logarithm shows \(|K(d)|\le8/d²\). Indeed its negative logarithmic increment has magnitude at most 8/d²≤1/8, and \(-\tfrac12\log(1-v)\le v\) for 0≤v≤1/2. Thus \(|K(2a)|\le2/a²\le1/144\) under (11). Consequently the reflected event contribution is strictly larger than
\[
 2(1/9-1/144)=15/72.
\]
Combining with W<13/72 proves the quantitative necessary constraint
\[
 \boxed{R_T(a)<-1/36}                                    \tag{14}
\]
at any assumed threshold event satisfying (1) and all onset gates. This handles arbitrary m≥2 without dividing by an arm or a real-axis derivative.

**Equation (14) is a required negative background, not an excluded background.** No lower bound for R_T(a) has been acquired. Although (10) lies below the isolated double contribution, (13) does not allow the rest of the zero population to be discarded.

## 5. Why cancellation of carrier growth loses positivity

The numerator minus denominator inside (12) is 8(34−d²). Hence
\[
 K(d)>0\ \text{for }|d|<\sqrt{34},\qquad
 K(d)<0\ \text{for }|d|>\sqrt{34},\qquad
 \int_{\mathbb R}K(d)\,dd=\pi(12-4-8)=0.                 \tag{15}
\]
The last identity follows by differentiating
\(\int\log[(d²+b²)/(d²+b_0²)]\,dd=2\pi(b-b_0)\)
with respect to b and fixing the constant at b=b0; differences are integrable.

More generally, for finitely many fixed positive heights b_j and real coefficients α_j, put
\[
 K_\alpha(d)=\tfrac12\sum_j\alpha_j\log(d²+b_j²).
\]
If \(\sum\alpha_j=0\), then Kα is integrable and
\(\int K_\alpha=\pi\sum\alpha_j b_j\).
If also \(\sum\alpha_j b_j=0\), cancelling the leading linear carrier, and Kα(0)>0, continuity and zero integral force Kα to be negative somewhere. Thus **finite fixed-height log combinations that exactly cancel the linear carrier and retain a positive central signal cannot have an everywhere nonnegative zero kernel**.

This is a scoped obstruction to a positivity-only inference for that class. It does not exclude signed background estimates, explicit zero deflation, height-dependent families with separately controlled costs, or retaining a nonzero bulk term. It is consistent with the prior [BW10 rational-resolution analysis](../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/notes/04_ZERO_DEFLATION_AND_RATIONAL_RESOLUTION_20261020.md): cancellation and resolution have different costs. No priority claim is made.

## 6. An exact threshold control passes the scalar cap

Reuse the [BW-01 positive three-atom control, §2](../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/01_local_double_winding/notes/04_EVENT_CONDITIONED_POSITIVE_SOURCE_OBSTRUCTION_20261020.md), with q=1/2 and spatial frequency \(\ell=2\pi/3>2\). For any T>0 define
\[
 G_T(t,z)=\frac49\left[\frac34+e^{\ell²(t-T)}\cos(\ell z)
                   +\frac12e^{4\ell²(t-T)}\cos(2\ell z)\right].     \tag{16}
\]
The half-line cosine source has positive masses \(\tfrac49(3/4,e^{-T\ell²},\tfrac12e^{-4T\ell²})\) at 0,ℓ,2ℓ. Its equation is the same physical backward heat equation. At t=T,
\(G_T(T,z)=\tfrac49(\cos(\ell z)+1/2)^2\).
The quadratic-in-cosine proof in BW-01 is independent of the choice of ℓ: every t>T has only simple real zeros, and every t<T has nonreal zeros, so its actual all-real threshold is T. The source’s original proof, not an assumed theta preservation theorem, is used here.

There are double events at \(a_j=1+3j\), j≥0. For any sufficiently large a_j choose T=c/log(a_j/(4π)) with the same c∈[1/2,1]. These controls therefore meet the tested time-height band on their actual collision domain. They are different frozen sources as T changes; no fixed source with varying threshold is asserted.

At these centers, elementary trigonometric factorization gives
\[
 \log|G_T(T,a_j+iy)|=\log(1/9)+2\ell y
      +\log(1-e^{-\ell y})+\log(1-e^{-3\ell y}).            \tag{17}
\]
The affine terms cancel in W. For f_b(y)=log(1−e^{-by}),
\(2f_b(6)-f_b(4)-f_b(8)\le-f_b(4)-f_b(8)\).
For b=ℓ,3ℓ, all four negative logarithms are <1/255 because \(e^{-4\ell}<e^{-8}<1/256\) and \(-\log(1-v)\le v/(1-v)\). Hence
\[
 W_{G_T}(a_j)<4/255<1/6<13/72.                            \tag{18}
\]
The same all-real event decomposition (13) then gives the negative background required by (14). **A bound on W below the isolated-event contribution does not by itself exclude a collision.** The control shares the scalar cap, positive source, heat equation and actual all-real threshold. It fails unchanged theta arithmetic, full gamma/profile growth and theta's eventual simplicity at its threshold (it has infinitely many simultaneous doubles). It need not satisfy the detailed canonical prime series (7), and that distinction is not hidden.

## 7. Full control screen and disposition

This is analytical screening of the [control catalog](../../../../result-summaries/12_collision_controls_and_screening.md), not certificate reruns.

| Family | What this test establishes; failed canonical premise |
| --- | --- |
| Atomic threshold control (16) | Actual high events in (1) pass the scalar cap and allow the negative background. Canonical coefficients/completion and eventual simplicity at threshold fail. |
| Exact finite-profile and continuous extensions | Finite observations and all-realness alone cannot justify discarding a signed background; no new scalar-cap evaluation for each extension is claimed. Full theta coefficients/profile fail. |
| Euler-factor and translated | The canonical comparison (4)/(7) changes with their extra factors. Unchanged arithmetic fails. Certified nonreal witnesses are not silently treated as all-real thresholds. |
| Weighted-square, finite-tail, finite-prime orbit | Full reflection and/or complete coefficients fail; many have no finite all-real time. Thus their local events do not supply the all-real product premise of (12). |
| Reflected super-Gaussian, smooth shape, positive primitive | Theta square-series arithmetic fails. Their recorded local collisions alone do not establish the global all-real premise; the present arithmetic cap is not assigned to them without proof. |
| RH-conditional endpoint | Conditional, time-zero scope remains. Ordinary Dirichlet arithmetic fails; no unconditional positive-threshold counterexample is inferred. |
| Variable readout / heat counter-kernels | Full cosine readout, unchanged source and/or physical generator fail. |
| Relaxed Green/profile populations | Exact integer canonical zero population and complete boundary-field identification fail. |

The cap (10) and necessary background (14) are quantitative intermediate statements; they are not RH-equivalent reformulations. The failed inference is specifically “all-realness makes the noncentral signed sum nonnegative.” Its failure is proved both by (15) and by an actual-threshold positive-source control satisfying the same scalar cap. No universal obstruction to signed arithmetic is asserted.

The inherited GNP-RS outer comparison retains ownership there; this note’s three-height combination and threshold consumer are the RSCT application. It neither reopens HCB-05’s stopped leading-pair norm comparisons nor acquires OA’s initial pair/factor/force inputs. [Decision02](../brainstorm/notes/02_RSCT_B01_R2_SIGNED_HEIGHT_DECISION_20261111.md) closes this bounded pass. Further work needs a new arithmetic estimate for the **event-conditioned noncentral signed background**, or a different acquisition/consumer pairing; no tractable E01 contract is supplied here.
