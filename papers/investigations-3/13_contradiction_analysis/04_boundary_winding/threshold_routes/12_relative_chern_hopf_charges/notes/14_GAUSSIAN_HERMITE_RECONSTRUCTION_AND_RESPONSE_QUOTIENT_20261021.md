# Finite Gaussian projection, exact response compression, and a scoped no-gain result

21 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual session configuration **gpt-6-astra, reasoning effort ultra**, verified by the coordinating agent from the current turn metadata. This note was developed by a separate same-model agent and checked by another agent and the producing assistant; it has not received specialist review. See [Review 12](../reviews/12_FINITE_TIME_SIGNED_RECONSTRUCTION_OPENING_REVIEW_20261021.md).

**Status.** The statements below are elementary proved-in-note identities and bounds for the complete canonical residual, conditional on the explicitly declared two-root reference geometry. Gaussian Hermite projection reconstructs an endpoint Taylor polynomial exactly. Its usual orthogonality-based remainder bound has no intrinsic finite-time improvement over the corresponding endpoint information. The signed linear-plus-quadratic response also admits exact compression to at most four endpoint measurements, with an error bound that retains their mixed quadratic interaction. No positive complete theta margin, matched finite-time improvement, or global exclusion is claimed.

Read with [Note 11](11_CANONICAL_QUADRATIC_RESPONSE_AND_HEAD_TAIL_CANCELLATION_20261021.md), [Note 12](12_LARGE_TIME_INFORMATION_AND_ENDPOINT_RECONSTRUCTION_20261021.md), the [FTSR program](../research-overview/03_FINITE_TIME_SIGNED_RECONSTRUCTION_PROGRAM_20261021.md), and the source normalization in [the manuscript](../manuscript/source.tex). The [result index](../../../../../../../result-summaries/README.md), [collision-control register](../../../../../../../result-summaries/12_collision_controls_and_screening.md), and [avoid index](../../../../../../../avoid/README.md) apply. Particularly relevant are [target classification](../../../../../../../avoid/01_restating_the_target.md), [matching controls](../../../../../../../avoid/02_shape_only_arguments_and_the_controls.md), [scoped exclusions](../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md), and [coupled estimates](../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md).

## 1. Complete source and fixed endpoint geometry

Fix M>=1 and use the unchanged canonical modes

\[
 \phi_n(u)=\lambda_ne^{5u}(2\lambda_ne^{4u}-3)e^{-\lambda_ne^{4u}},
 \quad \lambda_n=\pi n^2,
\]
\[
 F(z)=\int_0^\infty\sum_{n\le M}\phi_n(u)\cos(zu)du,
 \quad E_0(z)=\int_0^\infty R_M(u)\cos(zu)du,
 \quad R_M=\sum_{n>M}\phi_n.
\]

The statements also hold for any real signed source with the corresponding complete moments, but the displayed tail bounds below use these exact theta coefficients. Suppose F has precisely two zeros counting multiplicity in Gamma={|z-a|=R}, both in |z-a|<r<R, a real, with |F|>=delta on Gamma. Their centroid is c. No positive internal separation is assumed. Retain Note 11's

\[
 L(V)=-4\mathcal I[(z-c)V/F],\qquad
 B(V,W)=2\mathcal I[(z-c)VW/F^2]-\mathcal I[V/F]\mathcal I[W/F],
\]
\[
 S(E)=L(E)+B(E,E),\qquad
 C_L=4R(R+r)/\delta,\quad
 C_B=(2R(R+r)+R^2)/\delta^2.
\]

For every finite T>0 set

\[
 E_T(y)=\int_0^\infty R_M(u)e^{Tu^2}\cos(yu)du,
 \quad d\gamma_{T,a}(y)=K_T(a,y)dy,
 \quad K_T(z,y)=\frac{e^{-(z-y)^2/(4T)}}{\sqrt{4\pi T}}.
\]

All complete heat-weighted moments are finite. In particular E_T and every fixed real derivative are bounded, E_T belongs to L2(gamma), and E_0(z)=integral K_T(z,y)E_T(y)dy. The full source rays and full real line are included in these assertions.

## 2. Gaussian Hermite projection is exactly endpoint Taylor truncation

Let He_n denote the probabilists' Hermite polynomial, characterized by

\[
 e^{sx-s^2/2}=\sum_{n\ge0}\operatorname{He}_n(x)s^n/n!,
 \qquad h_n(y)=\frac{\operatorname{He}_n((y-a)/\sqrt{2T})}{\sqrt{n!}}.
\]

This normalization agrees with [NIST DLMF 18.12.16](https://dlmf.nist.gov/18.12.E16); the Gaussian orthogonality conventions are in [DLMF §18.3](https://dlmf.nist.gov/18.3). The h_n form an orthonormal basis in L2(gamma). Its coefficient is

\[
 c_n(T)=\langle E_T,h_n\rangle_\gamma
       =\frac{(2T)^{n/2}}{\sqrt{n!}}E_0^{(n)}(a).                 \tag{1}
\]

Proof: integration by parts against the Gaussian n times gives the coefficient as (2T)^(n/2)/sqrt(n!) times the Gaussian convolution of E_T^(n). The bounded complete moments justify each boundary term and interchange, and this convolution is E_0^(n). Equivalently insert the cosine source and evaluate its Gaussian Fourier transform.

For P_{T,N}=sum_{n=0}^N c_n h_n, Gaussian convolution yields

\[
 p_N(z)=\int K_T(z,y)P_{T,N}(y)dy
       =\sum_{n=0}^N E_0^{(n)}(a)\frac{(z-a)^n}{n!}.             \tag{2}
\]

Indeed, the generating function shows integral K_T(z,y)h_n(y)dy=(z-a)^n/((2T)^(n/2)sqrt(n!)). Thus this finite-dimensional positive-time approximation, although T-dependent before convolution, produces the same polynomial at every matching time.

The exact residual energy is

\[
 \eta_{T,N}^2
 =\|E_T-P_{T,N}\|_\gamma^2
 =\sum_{n>N}\frac{(2T)^n}{n!}|E_0^{(n)}(a)|^2.                 \tag{3}
\]

Parseval is legitimate because E_T is bounded. In particular the entire positive series in (3) is finite for every finite T, including arbitrarily large finite T. The canonical source decay is stronger than needed for this fact. Termwise monotonicity makes eta nondecreasing in T; no differentiation of the series is needed for that conclusion.

For possible direct acquisition of (3), the complete energy also equals

\[
 \|E_T\|_\gamma^2=\frac12\int_0^\infty\!\int_0^\infty
 R_M(u)R_M(v)
 \{e^{2Tuv}\cos(a(u-v))+e^{-2Tuv}\cos(a(u+v))\}\,du\,dv.       \tag{4}
\]

The mixed source kernel is retained. Fubini follows from 2uv<=u²+v² and the complete heat-weighted source mass. Subtract sum_{n=0}^N c_n² only with correctly directed numerical errors; a rounded negative residual energy is not admissible.

## 3. Sharp orthogonality payment and its precise comparison scope

The Gaussian kernel ratio has Hermite expansion

\[
 \frac{K_T(z,y)}{K_T(a,y)}
 =\sum_{n\ge0}\frac{(z-a)^n}{(2T)^{n/2}\sqrt{n!}}h_n(y).
\]

Since E_T-P_{T,N} is orthogonal to h_0,...,h_N,

\[
 \|E_0-p_N\|_\Gamma\le\beta_{T,N}:=
 \eta_{T,N}\left[\sum_{n>N}\frac{(R^2/(2T))^n}{n!}\right]^{1/2}. \tag{5}
\]

This removes the first N+1 terms from Note 12's full exponential kernel norm. It is a real improvement to that *unprojected fallback allowance*, but does not yet constitute a matched improvement over the direct endpoint method.

Two comparisons must be distinguished.

1. **Same weighted tail-energy information.** Suppose one knows the first N+1 endpoint derivatives and a bound for sum_{n>N}(2T)^n|E_0^(n)(a)|²/n!. At time zero, apply Cauchy–Schwarz directly to the Taylor remainder. This gives exactly (5). Thus the finite-time Hermite bound is already an endpoint bound using identical information. It has no additional time-transport gain.

2. **Complete derivative information.** If the actual complete derivative sequence is available, define

\[
 A_N(R)=\sum_{n>N}|E_0^{(n)}(a)|R^n/n!.
\]

Then

\[
 \|E_0-p_N\|_\Gamma\le A_N(R)\le\beta_{T,N}\qquad(T>0).        \tag{6}
\]

The second inequality is precisely Cauchy–Schwarz on the two sequences with squares appearing in (3) and (5). A full derivative sequence is stronger information than finitely many measured jets; (6) must not be reported as a cost-free practical replacement when those derivatives have not been acquired. A convergent enclosure for A_N is possible by acquiring finitely more derivatives and bounding the rest by complete source moments, but its cost belongs in the comparison. A coarse source-moment upper bound for A_N may exceed beta even though the exact A_N does not.

The exact signed response error also has no T dependence:

\[
 S(E_0)-S(p_N)=L(e_N)+2B(p_N,e_N)+B(e_N,e_N),\quad e_N=E_0-p_N. \tag{7}
\]

For example its safe symmetric payment is

\[
 |S(E_0)-S(p_N)|\le(C_L+2C_B\|p_N\|_\Gamma)\beta_{T,N}
                         +C_B\beta_{T,N}^2.                 \tag{8}
\]

Replacing beta by a valid smaller endpoint remainder bound only decreases this payment. More substantially, expansion of (7) in the endpoint Taylor coefficients retains every mixed term and is itself exactly independent of T. This closes the *complete Gaussian Hermite projection plus Gaussian Cauchy–Schwarz payment* route as a source of an intrinsic time gain. It does not close a route that obtains new source-specific signed information or uses a genuinely different approximation/error model.

As a normalization check, E_T=e^(Tu²)cos(uy) gives (1) with E_0^(n)(a)=u^n cos(au+n pi/2), and summing its coefficient squares recovers one half of {e^(2Tu²)+e^(-2Tu²)cos(2au)}. This is the one-atom transfer control, not a theta collision control.

## 4. Exact rank-four compression of the coupled response

Let alpha_1,alpha_2 be the two zeros of F inside Gamma, with multiplicity, and put

\[
 P(z)=(z-\alpha_1)(z-\alpha_2),\qquad q(z)=P(z)^2.
\]

Then F=UP with U holomorphic and nonzero on the closed disk. Define the polynomial projection

\[
 (\Pi V)(z)=\frac1{2\pi i}\oint_\Gamma
  \frac{V(\zeta)}{q(\zeta)}
  \frac{q(\zeta)-q(z)}{\zeta-z}\,d\zeta.                      \tag{9}
\]

The divided difference is a polynomial of degree at most three in z, including when z=zeta. Cauchy's formula gives, in the disk,

\[
 V(z)-\Pi V(z)=q(z)\frac1{2\pi i}\oint_\Gamma
                   \frac{V(\zeta)}{q(\zeta)(\zeta-z)}d\zeta. \tag{10}
\]

Consequently V-Pi V is divisible by P². If e=P²g is any holomorphic error, e/F=Pg/U and Ve/F²=Vg/U² are holomorphic. All their contour integrals vanish, so

\[
 L(e)=0,\qquad B(V,e)=0,\qquad S(V)=S(\Pi V).                 \tag{11}
\]

This includes a coincident pair. It is not an interpolation formula containing inverse internal root separation.

An explicit external-gap bound is

\[
 \|\Pi V\|_{|z-a|\le R}
 \le D_{r,R}\|V\|_\Gamma,\qquad
 D_{r,R}=\frac{4R(R+r)^3}{(R-r)^4}.                            \tag{12}
\]

Proof: every factor of q on Gamma has modulus at least R-r. The telescoping product identity bounds its divided difference by 4(R+r)^3 for z on the closed disk. The contour length supplies R. This bound pays only the external clearance. It may be large as r approaches R, and it is not a uniform all-height condition estimate.

For simple distinct reference roots, Pi E records E and E' at each root. For a reference double F=U(z)(z-b)², the degree-three quotient records E through its third derivative, but the response itself ignores that last derivative. Setting h=E/U, residues give

\[
 S(E)=-4h(b)+h'(b)^2+2h(b)h''(b).                            \tag{13}
\]

Thus degree-two Gaussian Hermite projection centered at b captures this *quadratic response* exactly, for every T, since it matches E's first three jets. This does not make the cubic remainder in the full discriminant expansion vanish. Nor does it prove any sign in (13).

## 5. A coupled signed finite-dimensional error bound

Use the real centered basis 1,(z-a),(z-a)²,(z-a)³ and write Pi E=sum d_j(z-a)^j. Real symmetry makes d real. Define

\[
 l_j=L((z-a)^j),\qquad M_{jk}=B((z-a)^j,(z-a)^k).
\]

Then M is real symmetric, and

\[
 S(E)=l^\top d+d^\top M d.                                   \tag{14}
\]

For an approximation d_hat, the *complete coupled error* is

\[
 S(E)-S(d_{\rm hat})=(l+2Md_{\rm hat})^\top e+e^\top M e,
 \qquad e=d-d_{\rm hat}.                                    \tag{15}
\]

Suppose a proved acquisition/reconstruction contract gives e=D x, ||x||<=eta, with a fixed real matrix D. Rectangular coefficient boxes can always be enclosed in such an ellipsoid; retaining their actual correlations can give a smaller one. Put

\[
 A=D^\top M D,\qquad b=D^\top(l+2Md_{\rm hat}).
\]

For any lambda>max(0,-lambda_min(A)) and kappa>max(0,lambda_max(A)), completion of squares proves

\[
 r_-(\lambda)=-\lambda\eta^2-\tfrac14 b^\top(A+\lambda I)^{-1}b,
\]
\[
 r_+(\kappa)=\kappa\eta^2+\tfrac14 b^\top(\kappa I-A)^{-1}b,
\]
\[
 \boxed{r_-(\lambda)\le S(E)-S(d_{\rm hat})\le r_+(\kappa).}   \tag{16}
\]

For the lower bound, write x^TAx+b^Tx=x^T(A+lambda I)x+b^Tx-lambda||x||², complete the first square, and use ||x||²<=eta². Apply the same argument to -A,-b for the upper bound. Optimizing the two scalar parameters is optional; each admissible parameter gives a rigorous bound. This derivation does not assume the desired endpoint sign and does not replace the mixed term by its separate modulus. Formula (16) is a signed quadratic error estimator, not a completed theta improvement.

For clarity, one way to generate D from a full-field error contract is explicit. Let k_j(y) be the coefficient of (z-a)^j in Pi[K_T(.,y)], and phi_j(y)=k_j(y)/K_T(a,y). Then

\[
 d_j=\int E_T(y)\phi_j(y)d\gamma(y).
\]

The kernels phi_j have finite Gaussian second moments by (9), compactness of Gamma, and the complete Gaussian kernel-ratio norm. If r_T is a terminal-field error with ||r_T||_gamma<=eta and G_{jk}=integral phi_j phi_k dgamma, its coefficient error has e=G^(1/2)x for some ||x||<=eta. To see this, the adjoint of x↦sum x_j phi_j has Gram matrix G; diagonalize G and apply Bessel's inequality. Zero eigenvalues force the corresponding measurement error to vanish. Thus D=G^(1/2) is admissible without assuming invertibility. This construction retains all real-line tails in the norm; a compact-window norm alone is not sufficient.

These four positive-time weighted measurements are exactly the corresponding endpoint quotient measurements. Evaluating (16) directly at the endpoint with the same coefficient uncertainty gives the identical interval. A gain requires a better quantified data contract, rather than the mere existence of this representation.

## 6. Explicit complete theta source payments

Here is an elementary majorant which makes every omitted mode and source ray explicit. For K>=1 let

\[
 \beta_K=\pi(K+1)^2,\quad
 q_K=\left(\frac{K+2}{K+1}\right)^4e^{-\pi(2K+3)},\quad
 A_K=\frac{2\pi^2(K+1)^4}{1-q_K}.
\]

The ratio of successive terms n^4 e^(-pi n² e^(4u)), n>=K+1, is at most q_K, uniformly for u>=0. Since phi_n(u)<=2 pi² n^4 e^(9u)e^(-pi n²e^(4u)),

\[
 0<R_K(u)\le A_K e^{9u-\beta_K e^{4u}}.                       \tag{17}
\]

No asymptotic replacement of the source was made. The complete lower-order term in phi_n remains in every retained mode; dropping it here is only an upper bound for the omitted positive tail.

For integer j>=0, T>=0, B>=0, and U>0, set

\[
 \kappa_{j,K}=4\beta_K e^{4U}-2TU-(9+B)-j/U.
\]

If 16 beta_K e^(4U)>=2T and kappa_{j,K}>0, concavity of

\[
 h(u)=Tu^2+(9+B)u+j\log u-\beta_K e^{4u}
\]

on u>=U gives the explicit ray bound

\[
 \int_U^\infty u^jR_K(u)e^{Tu^2+Bu}du
 \le \frac{A_K U^j e^{TU^2+(9+B)U-\beta_K e^{4U}}}
               {\kappa_{j,K}}.                             \tag{18}
\]

Indeed h''(u)=2T-j/u²-16 beta_K e^(4u)<=0, and h'(U)=-kappa. Thus h(u)<=h(U)-kappa(u-U). These sufficient cutoff conditions can always be met for finite T,B,j. B=R pays cosine growth on the endpoint contour; B=0 pays real jets and terminal real-field moments.

For acquisition using modes M<n<=K and 0<=u<=U, the omitted endpoint derivative has absolute error at most

\[
 \theta_j(K,U)=\int_0^U u^jR_K(u)du+
                       \int_U^\infty u^jR_M(u)du.            \tag{19}
\]

The first integral is at most A_K e^(-beta_K) U^(j+1)/(j+1), because 9u-beta_K e^(4u) decreases on u>=0 for K>=1. The second is bounded by (18) with T=B=0 and K replaced by M. An actual integrator can improve the compact contribution, but cannot omit it. Heat-weighted and contour-weighted analogues follow by inserting the displayed weights in (19) and applying (17)-(18); their compact integrals remain finite and explicit.

Coefficient errors |delta E_0^(j)(a)|<=theta_j become |delta c_j|<=(2T)^(j/2)theta_j/sqrt(j!), or a contour polynomial error <=sum_{j<=N}theta_j R^j/j!. They enter (15) or (8) through the same approximated residual, never through independently adjusted linear and quadratic data.

For a finite remainder estimate based on a finite number of exact endpoint derivatives, the unseen Taylor tail beyond degree J is bounded by

\[
 \sum_{n>J}|E_0^{(n)}(a)|R^n/n!
 \le \int_0^\infty R_M(u)
       \left(e^{Ru}-\sum_{n=0}^{J}(Ru)^n/n!\right)du.          \tag{20}
\]

This uses |cos(au+n pi/2)|<=1 and preserves all source rays. It proves convergence of finite derivative enclosures to A_N when their acquisition errors are controlled, while also showing exactly where an absolute source envelope can lose oscillatory cancellation.

## 7. Explicit real-line tail payments

The analytic identities above integrate the entire real line; no spatial truncation is implicit. If terminal-field data are acquired only for |y-a|<=Y, write L=Y/sqrt(2T), and let X be standard normal. For h_n as above,

\[
 \left|\int_{|y-a|>Y}E_T(y)h_n(y)d\gamma\right|
 \le M_T\,\tau_n(L),\quad
 M_T=\int_0^\infty R_M(u)e^{Tu^2}du,
\]
\[
 \tau_n(L)=\frac1{\sqrt{n!}}
  \int_{|x|>L}|\operatorname{He}_n(x)|
                      \frac{e^{-x^2/2}}{\sqrt{2\pi}}dx.       \tag{21}
\]

M_T is paid by the complete source bound. A finite elementary upper for tau_n follows from

\[
 \operatorname{He}_n(x)=n!\sum_{j=0}^{\lfloor n/2\rfloor}
 \frac{(-1)^j x^{n-2j}}{2^j j!(n-2j)!},
\]

and the absolute Gaussian moments

\[
 \mathbb E[|X|^m1_{|X|>L}]
 =\frac{2^{m/2}}{\sqrt\pi}
      \Gamma((m+1)/2,L^2/2).                                \tag{22}
\]

For a fixed terminal polynomial P_{T,N}=sum c_n h_n, a safe omitted contribution to eta² is

\[
 \int_{|y-a|>Y}|E_T-P_{T,N}|^2d\gamma
 \le 2M_T^2\operatorname{erfc}(L/\sqrt2)
       +2\int_{|X|>L}|P_{T,N}(a+\sqrt{2T}X)|^2d\gamma_1(X).   \tag{23}
\]

The last integral is a finite polynomial Gaussian tail computable by (22), or by an outward-rounded upper bound for its absolute coefficient expansion. This is conservative but complete. Using (3) or (4) instead avoids spatial truncation altogether and transfers the acquisition obligation to complete source moments. It is not legitimate to drop the tail because the Gaussian is small while E_T's normalization has not been paid.

## 8. Full discriminant interval, control screen, and research status

With the actual wall ratio rho=sup_Gamma|E_0/F|<1 and Note 11's cubic allowance C_3(rho), any rigorously acquired center S(d_hat) and (16) give

\[
 \Delta_H\in\Delta_F+S(d_{\rm hat})+[r_-,r_+]
                                      +[-C_3(\rho),C_3(\rho)]. \tag{24}
\]

Reference-data uncertainty (F, its quotient P, l, M, the centroid, and Delta_F), numerical acquisition uncertainty, and any wall-ratio uncertainty must additionally be included. Equations (12), (17)-(23) identify finite bounds without inverse internal separation; they do not acquire those reference data automatically. The same rho and cubic payment must be retained in a matched direct-versus-finite-time comparison.

The Hermite and quotient identities are generic and remain valid for collision controls with their admissible complete source moments. They do not exclude a collision. The exact canonical source tail payments use the unchanged pi n² nodes and coefficients: Euler-factor controls alter arithmetic; weighted-square and finite-prime controls lack the full normalized reflection conjunction; reflected/positive-primitive controls lack the canonical square coefficients; the close normalized endpoint controls fail ordinary Dirichlet-series arithmetic. No claim here needs those controls to fail a generic Gaussian identity. A claimed future positive bound would still have to identify a quantitative source premise it uses on a domain containing the control event.

A reference double is explicitly retained in (13); its signed jet expression may have either sign, and the original head-tail cancellation from Note 11 remains in force. Exact finite-rank response compression does not remove that cancellation. This is a quantitative approximation/conditioning result and a scoped closure of one norm-based finite-time candidate, not a reformulated criterion counted as endpoint progress.

**Progress accounting.** FTSR-02: a complete finite-T candidate and its tail contract have been analyzed. FTSR-03: the coupled finite-dimensional signed error enclosure (16) is proved, but an actual-theta comparative gain remains unproved. FTSR-04: no strict improvement established; the specific full Hermite projection plus norm payment has the scoped no-gain conclusion (5)-(8). FTSR-05: generic and canonical-premise controls screened as above. FTSR-06 and FTSR-07 retain their gates. The conditional parameterized window, actual wall ratio and explicit bounded matching-time range are paid by [Note 13](13_PAID_ENDPOINT_WINDOW_AND_FINITE_TIME_BASELINE_20261021.md). No particular numerical near-event theta domain is certified. The [exact control script](../numerics/ftsr_exact_controls.py) and [receipt](../numerics/FTSR_EXACT_CONTROLS_20261021.json) check finite polynomial transfers and rational-unit quotient responses; they do not substitute for these proofs.
