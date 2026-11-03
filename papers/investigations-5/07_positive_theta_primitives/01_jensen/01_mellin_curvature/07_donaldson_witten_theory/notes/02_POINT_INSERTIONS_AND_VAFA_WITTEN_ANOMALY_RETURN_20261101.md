# Continuation: point insertions and the Vafa–Witten anomaly

1 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. **MC07-B02**, B — bounded conceptual continuation; actual author/coordinator **gpt-6-astra / ultra**. Two read-only Astra/ultra assistants investigated disjoint questions: the point-insertion family and the published N=4 anomaly. The coordinator owns this return and shared files. Separate MC07-E02 checking is requested; this return does not presume its outcome.

**Outcome:** the previous failure was local to one protected correlator in one theory. A broader family in that same theory also fails, by an exact coefficient relation. A related N=4 theory succeeds at a different, useful task: its normalized holomorphic anomaly recovers the complete theta source and gives an exact RH reformulation as a Mellin period of that anomaly. No new Mellin comparison estimate is obtained. No claim of novelty or specialist review is made.

## 1 Scope and candidate decision

The author explicitly requested continuation if the earlier exclusion was local. It was: [Return01](01_DONALDSON_WITTEN_FEASIBILITY_RETURN_20261101.md) treated the p=0 surface correlator on CP2 in N=2 Donaldson–Witten theory, with a fixed bundle sector and through-zero linear parameter matching. It did not exclude topological field theories, other four-manifolds, or other observables. Its two minor review clarifications remain in [Review01](../reviews/01_MC07_E01_SEPARATE_REVIEW_20261101.md); the frozen return is not rewritten.

The [B02 launch](../numerics/MC07_B02_LAUNCH_RECORD_20261101.json) permits at most two extensions and one worked candidate. The short point-insertion screen below gives an exact obstruction. **Select the completed Vafa–Witten partition function on CP2 as the worked candidate.** This changes N=2 Donaldson theory to N=4 topological gauge theory; it does not claim to repair the failed Donaldson correlator.

| Following task | Type | Recommended model | Dependency | Output |
| --- | --- | --- | --- | --- |
| MC07-E02 | E — fixed separate checking | Sol / author-selected effort | This frozen return and request r1 | Check all normalizations, the family obstruction, full-source recovery, RH identity and limitations |
| MC07-B03, possible continuation | B — boundary-response mechanism | Astra; the missing issue is independent sign information | Acceptance of E02; not launched by this return | Assess one boundary Ward-identity route to the unchanged signed Mellin comparison, or isolate its surviving uncontrolled term |

Use the [result index][results], [theta cluster][thetaresults], [control screen][controls] and [avoid index][avoid], especially [reformulation versus estimate][reformulation], [scoped exclusions][scopes] and [factor versus target][factor].

## 2 What the point-insertion extension excludes

Keep the CP2 complex orientation, SU(2) sector, surface H and factorial convention of Return01. Let
\[
 Z_D(p,t)=\langle e^{p\mathcal O+tI(H)}\rangle,
 \qquad C_\lambda(z)=-\frac23\left.\partial_t(1+\lambda\partial_p)
 Z_D(p,t)\right|_{p=0,t=z}.
\]
[Moore–Witten][MW], (1.3) and (9.24), give, with the exponential factorials included,
\[
 C_\lambda(z)=1+\frac\lambda3z^2-\frac{z^4}{36}
 -\frac\lambda{288}z^6-\frac{z^8}{20160}+\cdots.                 \tag{1}
\]
Thus a nonzero point insertion removes the original missing z-squared coefficient. It does not solve the matching problem. For arbitrary complex lambda and nonzero complex alpha, write
\(a_n=[z^{2n}]C_\lambda(\alpha z)\). Then
\[
 a_2=-\frac{\alpha^4}{36},\qquad a_4=-\frac{\alpha^8}{20160},
 \qquad \boxed{a_4=-\frac9{140}a_2^2}.                         \tag{2}
\]
The complete theta target has coefficients c_n defined in Section 5, with c_0,c_2,c_4 strictly positive. Matching its normalized series would require a_2=c_2/c_0 and a_4=c_4/c_0, contradicting (2). This argument also rules out complex parameter choices. For unnormalized coefficients it says that matching would require
\(c_0c_4=-(9/140)c_2^2\). An overall multiplier is fixed by the constant term.

The same proof covers
\[
 -\frac23\langle I(H)[1+P_{\rm odd}(\mathcal O)]
                    e^{\alpha z I(H)}\rangle,                 \tag{3}
\]
where P_odd is any finite odd polynomial with arbitrary complex coefficients. To see this, a coefficient z^(2n) has N=2n+1 surface insertions and m point insertions. The index rule
\[
 2N+4m=8k-6\quad\Longrightarrow\quad n+m\text{ is even}
\]
shows that odd m changes only odd n. Hence a_0,a_2,a_4 in (3) retain their p=0 values, proving (2) for the entire family. A general nonzero constant multiplying the identity insertion can be normalized to one. With only odd point powers and zero constant, the constant Taylor coefficient vanishes and cannot match c_0.

This is an exclusion for a **family of observable dictionaries within one theory**. It does not cover higher even point powers, a fixed nonzero point source, nonpolynomial insertions, other bundles/manifolds, or affine/nonlinear parameter changes. None of those alternatives is asserted impossible or assessed here. For any nonnegative source measure with positive mass on x>0, finite total mass and finite eighth moment, c_0,c_2,c_4>0, so the same declared map also fails for that wider target class. This is a premise check, not an exclusion of those sources from physics.

## 3 Selected theory and exact anomaly normalization

Use the Vafa–Witten twist of four-dimensional N=4 SO(3) gauge theory on CP2, in magnetic sector w_2=0. Set
\[
 \tau=\tau_1+iy=\frac{\theta_{\rm YM}}{2\pi}+\frac{4\pi i}{g^2},
 \quad q=e^{2\pi i\tau},\quad \bar q=e^{-2\pi i\bar\tau}.
\]
The selected completed partition function is the explicit function in [Dabholkar–Putrov–Witten][DPW], printed pp.14–15, (3.1), (3.3)–(3.5):
\[
 Z_0=3\eta(\tau)^{-3}\widehat h_0,\quad
 \widehat h_0=\sum_{k\ge0}H(4k)q^k+
 2y^{-1/2}\sum_{n\in\mathbb Z}\mathcal B(4\pi n^2y)q^{-n^2},
 \quad \mathcal B(t)=\frac1{16\pi}\int_1^\infty u^{-3/2}e^{-ut}\,du.
                                                               \tag{4}
\]
Here H denotes the Hurwitz–Kronecker class numbers, H(0)=-1/12. The source's function called beta is renamed mathcal B to distinguish our positive coupling coordinate beta. The anomaly is
\[
 \partial_{\bar\tau}Z_0=
 \frac{3}{16\pi i\,y^{3/2}\eta(\tau)^3}
 \sum_{n\in\mathbb Z}\bar q^{n^2}.                            \tag{5}
\]
The eta power is **three** in this SO(3) normalization. The eta-six convention in [Vafa–Witten 1994][VW], (4.23)–(4.32), includes an additional diagonal U(1) factor; it is not interchangeable with (4). The [source record][sources] supplies archive receipts and passage scopes.

DPW interpret (5) as a boundary contribution at infinity on the noncompact Coulomb branch, and reproduce it in a two-dimensional sigma-model description. Their physical calculations leave an orientation sign unresolved, and the four-dimensional calculation does not derive the absolute measure normalization. We fix both through the explicit mathematical completion (4). This is not a rigorous construction of the four-dimensional path integral or an identification with an ordinary compact-moduli-space Euler characteristic.

Here is a direct check of the sign and constant, independent of the physical normalization argument. Substitute v=yu in the nth correction term of (4):
\[
 R_n(y):=2y^{-1/2}\mathcal B(4\pi n^2y)
       =\frac1{8\pi}\int_y^\infty v^{-3/2}e^{-4\pi n^2v}\,dv.
\]
Since \(\partial_{\bar\tau}y=i/2\) and q^(-n²) is holomorphic,
\[
 \partial_{\bar\tau}[R_n(y)q^{-n^2}]
 =\frac1{16\pi i}\,y^{-3/2}\bar q^{n^2}.
\]
This includes n=0, where R_0=1/(4 pi sqrt(y)). On compact subsets of the upper half-plane the series and its indicated derivatives converge uniformly by Gaussian bounds, justifying this differentiation. The holomorphic eta factor then gives (5).

## 4 Exact theta extraction and an RH reformulation

For every beta>0 define the normalized anomaly response
\[
 \mathcal A(\beta)=\frac{16\pi i}{3}\left(\frac\beta2\right)^{3/2}
 \eta(i\beta/2)^3
 \left.\partial_{\bar\tau}Z_0(\tau,\bar\tau)\right|_{\tau=i\beta/2}.
                                                               \tag{6}
\]
Take the Wirtinger derivative in (5) **before** restricting to the imaginary axis; it is not an ordinary derivative of Z_0(iy,-iy). Eta has no zero in the upper half-plane. Equations (5)–(6) give
\[
 \boxed{\mathcal A(\beta)=\sum_{n\in\mathbb Z}e^{-\pi\beta n^2}
 =\Theta(\beta)},\qquad \beta=\frac{8\pi}{g^2}
 \quad(\theta_{\rm YM}=0).                                    \tag{7}
\]
All positive, negative and zero fluxes of this sector are present. The half-integer sector is a different partition-function component, not a discarded term of Z_0. The normalization removes specified oscillator and zero-mode factors; the raw Z_0 itself is not Theta.

Define the completed anomaly Mellin period
\[
 \mathcal X_{\rm VW}(s)=\frac12+\frac{s(s-1)}4
 \int_1^\infty[\mathcal A(\beta)-1]
 \left[\beta^{s/2}+\beta^{(1-s)/2}\right]\frac{d\beta}{\beta}.
                                                               \tag{8}
\]
This is an explicitly prescribed nonlocal transform over gauge coupling, rather than a local protected correlator. Its identity with xi is proved as follows. For Re(s)>1, positive Gaussian integration and absolute convergence give
\[
 \frac12\int_0^\infty[\Theta(\beta)-1]\beta^{s/2-1}\,d\beta
 =\pi^{-s/2}\Gamma(s/2)\zeta(s)=:\Lambda(s).
\]
Split at beta=1 and use the Gaussian Poisson identity
\(\Theta(\beta)=\beta^{-1/2}\Theta(1/\beta)\). The elementary terms on (0,1) yield
\[
 \Lambda(s)=\frac1{s(s-1)}+
 \frac12\int_1^\infty[\Theta(\beta)-1]
 [\beta^{s/2}+\beta^{(1-s)/2}]\frac{d\beta}{\beta}.
\]
Multiplication by s(s-1)/2 and (7) prove
\[
 \mathcal X_{\rm VW}(s)=\xi(s),\qquad
 \xi(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s).            \tag{9}
\]
The integral in (8) converges locally uniformly for all complex s because Theta(beta)-1 decays exponentially at infinity. Thus (8) is entire and (9) extends by analytic continuation; its reflection s<->1-s is explicit. The zero-mode subtraction and additive one-half are essential. In particular the values at s=0,1 are one-half, not artificial zeros.

**RH is equivalent to every zero of the completed anomaly Mellin period (8) lying on Re(s)=1/2.** This is the promised physical reformulation, derived from a known anomaly and the classical theta Mellin identity. It is stated as an equivalence, not supported by finite zero checks or presented as progress toward a proof. No priority claim has been investigated.

Do not read the scalar reflection used here as S-duality of Z_0 alone. With tau=i beta/2, beta->1/beta means tau->-1/(4 tau), whereas ordinary S sends tau->-1/tau and mixes the two magnetic sectors. Our reflection step is Poisson summation after the exact extraction (7).

## 5 The complete signed observable is unchanged

Differentiate the **whole normalized response** (6), including its beta-dependent prefactor. Equation (7) yields
\[
 \Phi(x)=\left.\beta^{1/4}
 \left(\beta^2\partial_\beta^2+\frac32\beta\partial_\beta\right)
 \mathcal A(\beta)\right|_{\beta=e^{4x}}
 =\sum_{n\ge1}(2\pi^2n^4e^{9x}-3\pi n^2e^{5x})
 e^{-\pi n^2e^{4x}}.                                         \tag{10}
\]
The zero mode is removed by this differential operator, not prematurely omitted from (5). Both signed summands and every positive integer n remain. The resulting canonical coefficients and source generating function are
\[
 c_n=\frac1{(2n)!}\int_0^\infty x^{2n}\Phi(x)\,dx,\qquad
 B_\theta(z)=\sum_{n\ge0}c_nz^{2n}
 =\frac18\mathcal X_{\rm VW}((1+z)/2).                         \tag{11}
\]
The one-eighth normalization is the inherited exact source convention in Return01 and [Synthesis06](../../notes/06_PARALLEL_PHYSICAL_DIRECTIONS_SYNTHESIS_20261101.md), not a new fit. On x>=0 each summand of (10) is positive since 2 pi n² exp(4x)-3>0, hence c_0,c_2,c_4>0 as used above. Its rapid decay supplies all moments.

For the higher-rank observable retain
\[
 M_3(\sigma)=\int_{0<x_1<x_2<x_3}
 \prod_jx_j^{2\sigma}V(\mathbf x^2)
 \det[\Phi^{(2i)}(x_j)]_{i=0,1,2;\ j=1,2,3}\,d\mathbf x.
\]
Write R=Phi''/Phi,
\(w_\sigma=\prod_jx_j^{2\sigma}\Phi(x_j)V(\mathbf x^2)V(R(\mathbf x))\),
\(d\mu_\sigma=w_\sigma d\mathbf x/\int w_\sigma\),
\(T=2\sum_j\log x_j\), and
\[
 h_3=\frac{\det[\Phi^{(2i)}(x_j)/\Phi(x_j)]}{V(R(\mathbf x))},
 \quad A_3(\sigma)=E_\sigma h_3.
\]
The inherited positive carrier and A_3>0 have their existing internal-review scope. The insertion h_3 retains its negative region. Its complete curvature is
\[
 (\log M_3)''=\operatorname{Var}_\sigma T+
 \frac{\operatorname{Cov}_\sigma(h_3,(T-E_\sigma T)^2)}{A_3}
 -\left(\frac{\operatorname{Cov}_\sigma(h_3,T)}{A_3}\right)^2.     \tag{12}
\]
We use sigma here to distinguish the signed three-variable Mellin tilt from the zeta variable s in (8). The missing comparison remains (12)<=kappa_3(sigma), where
\(\kappa_3(\sigma)=\sum_{j=0}^2\sum_{\nu\ge0}(\sigma+j+1/2+\nu)^{-2}\), sigma>=0. Neither a pointwise interval nor an integrated neighboring-index comparison has been added. The first required interval [0,2] remains uncovered by this work. No signed determinant is replaced by a square, absolute value or ordinary positive-state variance.

## 6 What is gained and what still has to be supplied

The conceptual gain over B01 is that the source now comes from the anomaly of an explicitly completed four-dimensional partition function, rather than a theta factor before a u-plane integration. Equations (8)–(11) supply the full RH dictionary as a specified nonlocal response. They do not identify xi with the protected holomorphic partition function itself.

One exact limitation is visible without further computation. Adding a holomorphic function F(tau) to Z_0 leaves (5)–(11) unchanged. Such an addition need not be an allowed physical partition function or respect modularity; the statement concerns information retained by the derivative. In particular the holomorphic class-number contribution in (4) is annihilated. No new estimate from that counting data has been transmitted to (12). The possible new tool is the boundary-theory interpretation and its identities, not a sign inference from positive instanton counts.

| Control | Precise role in this assessment |
| --- | --- |
| Gaussian | Remains the K3 comparator of B01. It does not satisfy the exact CP2 anomaly dictionary (7), and no comparison between these theories has been derived. |
| Weighted/finite square controls | Change the unit weights or full infinite unshifted lattice in (7); square support alone is insufficient. No modified source is silently substituted. |
| Euler-factor controls | Change the complete reconstructed source. No realization with the unchanged (4)–(7) is provided. Positivity/evenness or a functional equation alone would not separate them. |
| Reflected, smooth-shape and primitive-compatible controls | May retain reflection, positivity or endpoints, but fail the full normalized unit-weight square expansion imposed by (7) and (10). No conclusion about their unspecified gauge realizations is asserted. |
| Positive-source coefficient test | The family obstruction (2) applies whenever c_0,c_2,c_4>0 under the moment hypotheses in Section 2, including the Gaussian. It is a check on that map, not a global obstruction to physical sources. |

These controls pass no newly claimed inequality: none is claimed. Exact source identification separates the selected construction from those controls but does not supply a quantitative margin. An RH-equivalent reformulation can still be useful for the author's independent physics objective.

## 7 Disposition and checking contract

MC07-B02 completes its bounded scope: one algebraic family screen and one worked anomaly candidate. There was no numerical scan, quadrature campaign, search over additional manifolds or altered-source test. The exact moment and Mellin arguments above are analytical, not floating evidence.

**Next: [E] MC07-E02 — Sol.** Follow the frozen request r1. Verify Moore–Witten factorials and the n+m parity argument; the negative coefficient relation even with complex rescaling; DPW's eta-three SO(3) completion, zero mode, Wirtinger derivative, sign and physics caveats; the beta/2 normalization; the entire Mellin continuation and boundary constants; the complete source operator, one-eighth convention, signed observable and control scopes. Accept, give a precise correction, or name an unresolved import. Do not alter the candidate or enlarge the investigation.

If accepted, the proposed **MC07-B03** asks whether one boundary Ward identity provides information about the full signed insertion beyond the exact theta identity. Compare at most two plausible identities, work one, and return either an independently justified contribution to (12) on a specified domain or the exact uncontrolled term. Merely rederiving (7) or restating the comparison is a scoped failure of that attempt. Any ensuing execution must receive its own fixed E contract. B03 is not executed here.

[MW]: https://arxiv.org/pdf/hep-th/9709193v2
[DPW]: https://arxiv.org/pdf/2004.14387v3
[VW]: https://arxiv.org/pdf/hep-th/9408074v2
[sources]: ../../../../references/09_VAFA_WITTEN_CONTINUATION_SOURCES_20261101.md
[results]: ../../../../../../../result-summaries/README.md
[thetaresults]: ../../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../../avoid/README.md
[reformulation]: ../../../../../../../avoid/01_restating_the_target.md
[scopes]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[factor]: ../../../../../../../avoid/13_a_factor_is_not_the_target.md
