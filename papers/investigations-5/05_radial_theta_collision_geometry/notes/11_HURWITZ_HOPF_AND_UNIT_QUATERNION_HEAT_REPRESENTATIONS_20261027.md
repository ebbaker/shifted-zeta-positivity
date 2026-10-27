# Hurwitz lattices, the Hopf map and unit-quaternion heat representations

27 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort max**. Conversation: **Continue higher-dimensional H-rep**, Investigation05 chat0003, thread `01a17f2b-8196-7683-ab85-434b4bd2ac20`.

**Status: exact constructions and scoped comparisons proved in-note, using the classical Hurwitz norm count; same-assistant checking and self-review.** Three distinct quaternionic choices are evaluated. The ordinary Hurwitz Epstein series gives an exact zero-preserving representation at t=0 in a declared strip. A Hopf-map lattice with an explicit Möbius correction recovers the full H at every finite complex time. The unit-quaternion sphere supplies the simplest local differential operator found in this return and reduces completion to a first-order scale observation. None yet improves on [Note10](10_COMPLETE_THREE_DIMENSIONAL_GAUSSIAN_OBSERVATION_20261027.md) in simultaneously supplying an additive rank-three lattice and a genuinely three-dimensional complete observation.

This responds to Edward Baker's suggestion to consider quaternionic lattices. The earlier [hypercomplex summary](../../../../result-summaries/16_hypercomplex_reductions_and_geometric_realizations.md) is useful context: its Fueter lifts, signed Hodge pairings and physical metrics start from H and its derivatives. Here the order, Hopf map or sphere operator is specified before H. Their defining data contain no physical zeros.

The [result index](../../../../result-summaries/README.md), [avoid index](../../../../avoid/README.md), [coordinate-lift warning](../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md), [factor warning](../../../../avoid/13_a_factor_is_not_the_target.md), [scoped-exclusion rule](../../../../avoid/07_scoped_exclusions_read_as_universal.md), and [controls](../../../../result-summaries/12_collision_controls_and_screening.md) apply. These are representation results under Note09's objective, not new RH criteria or collision inequalities. No literature-priority claim is made.

## 1. The ordinary Hurwitz lattice: a useful t=0 result with visible costs

Use the Hurwitz order

\[
 \mathcal O=\mathbb Z^4\ \cup\ (\mathbb Z+\tfrac12)^4\subset\mathbb H,
 \qquad N(q)=q\bar q=a^2+b^2+c^2+d^2.
\tag{1}
\]

For n>=1 its norm shell has

\[
 r_{\mathcal O}(n)=24\sigma_{\rm odd}(n),
 \qquad \sigma_{\rm odd}(n)=\sum_{d\mid n,\ d\ {m odd}}d.
\tag{2}
\]

The classical count is recorded in Asada et al., Section 2, Lemma 1; the checked passage, published metadata and external PDF receipt are in [reference06](../references/06_QUATERNION_LATTICES_AND_COMPLETE_OBSERVATION_20261027.md). Only that count is imported from the paper.

The normalized lattice Epstein series, absolutely convergent for Re(w)>2, is

\[
 \mathcal Q(w)=\frac1{24}\sum_{q\in\mathcal O\setminus\{0\}}N(q)^{-w}
 =\sum_{n\ge1}\sigma_{\rm odd}(n)n^{-w}
 =(1-2^{1-w})\zeta(w)\zeta(w-1).
\tag{3}
\]

The last equality follows directly by writing n=dk, d odd and interchanging the two absolutely convergent series. It also specifies the meromorphic continuation.

In the inherited normalization, w=(1+iz)/2 and H(0,z)=xi(w)/8. Hence

\[
 \boxed{H(0,z)=
 \frac{w(w-1)\Gamma(w/2)}
 {16\pi^{w/2}(1-2^{1-w})\zeta(w-1)}\,\mathcal Q(w).}
\tag{4}
\]

On 0<Re(w)<1, equivalently |Im(z)|<1, the displayed prefactor is holomorphic and nonzero. In fact |2^(1-w)|>1, and zeta(w-1) is nonzero in -1<Re(w-1)<0 by the functional equation and the Euler product on the reflected half-plane. Gamma has no zeros or poles here and w(w-1) is nonzero. Thus (4) preserves zeros and multiplicities throughout that strip. This includes the physical real z axis, but is not a claim about every complex zero of the unnormalized quaternionic Epstein function.

The raw series in (3) does not converge on the physical line Re(w)=1/2. The extra zeta factor and gamma completion have not disappeared. Nor does replacing the ordinary theta heat trace by

\[
 \frac1{24}\sum_{q\ne0}e^{-\pi r^2N(q)}
 =\sum_{n\ge1}\sigma_{\rm odd}(n)e^{-\pi r^2n}
\tag{5}
\]

give A(r): the exponential rates are n, rather than n², and the shell coefficients differ. Already norm 2 contributes e^(-2 pi r²). This rejects direct equality with this unweighted Gaussian trace, not signed quaternionic projections, other kernels, or all quaternionic constructions. Applying Newman heat evolution to the product in (4) would also differentiate its prefactor; retaining it unchanged is incorrect.

## 2. A genuinely quaternionic way to obtain the square exponents

Fix the imaginary unit i and form the quadratic Hopf map

\[
 h(q)=q i\bar q\in\operatorname{Im}\mathbb H,
\]
\[
 h(a+bi+cj+dk)=
 (a^2+b^2-c^2-d^2,\ 2(bc+ad),\ 2(bd-ac)).
\tag{6}
\]

For every Hurwitz quaternion,

\[
 h(q)\in\mathbb Z^3,\qquad |h(q)|=N(q).
\tag{7}
\]

For integer coordinates, integrality is immediate. For half-integer coordinates write twice each coordinate as an odd integer. The first numerator in (6) is divisible by four, and twice each of the other two integer numerators is also divisible by four. Norm multiplicativity gives |h(q)|²=N(q)². This is actual use of quaternion multiplication, rather than a relabeling of Euclidean vectors.

Consequently the Gaussian on the Hopf image is

\[
 B(r)=\frac1{24}\sum_{q\ne0}e^{-\pi r^2|h(q)|^2}
 =\sum_{n\ge1}\sigma_{\rm odd}(n)e^{-\pi r^2n^2}
 =\sum_{d\ge1\ {m odd}}d A(dr).
\tag{8}
\]

The norm-square exponent is now correct. The exact remaining operation is to remove the divisor multiplicity. Odd-divisor Möbius inversion gives

\[
 \boxed{A(r)=\sum_{d\ge1\ {m odd}}\mu(d)d B(dr)
 =\frac1{24}\sum_{d\ge1\ {m odd}}\mu(d)d
        \sum_{q\ne0}e^{-\pi r^2d^2N(q)^2}.}
\tag{9}
\]

Indeed, the coefficient of exp(-pi r² n²) is

\[
 \sum_{d\mid n,\ d\ {\rm odd}}\mu(d)d\,\sigma_{\rm odd}(n/d)=1.
\tag{10}
\]

This is the Dirichlet-convolution identity (mu times the odd identity function) * (odd identity function) = delta, followed by convolution with the constant-one function. Absolute convergence can be checked before using cancellation: replacing mu by its absolute value makes the coefficient at most n tau(n)²<=n³. Thus (9) is absolutely convergent for every r>0 and decays uniformly like a Gaussian for r>=1.

Let W be the explicit second-order observation from Note10, equation (5). Equations (9) and the canonical boundary reconstruction give the complete formula

\[
 \boxed{H(t,z)=\frac1{16}+\frac1{192}
 \sum_{d\ge1\ {\rm odd}}\mu(d)d\sum_{q\in\mathcal O\setminus\{0\}}
 \int_0^\infty e^u W_{t,z}(u)
       e^{-\pi e^{4u}d^2N(q)^2}\,du.}
\tag{11}
\]

It converges absolutely and locally uniformly for all complex t,z, with every fixed parameter derivative. The n³ majorant above, followed by the double-exponential scale decay, proves the needed interchanges. Thus this quaternionic lattice construction does have actual nonzero Newman-time dependence; it is not merely a t=0 dictionary.

### What the Hopf construction costs

The Gaussian is ordinary in the three-dimensional vector h(q), but quartic in the four lattice coordinates of q. The Hopf image is an arithmetic subset of Z³, with repeated fibers, not a full additive rank-three lattice. The odd d sum and its signed Möbius weight are additional data. Combining them into weights on image points is possible, but does not make the weights local or remove their arithmetic definition.

The signs are substantive. At output length 3, the norm-3 Hopf images are the 24 signed/permuted vectors of shape (1,2,2), each with four preimages. They contribute total weight 4 after division by 24. The d=3 images of the 24 units contribute total weight -3 on the six axial vectors of length 3. The combined shell weight is 1. A positive contribution from each image point is not preserved by (9).

There is also a conventional operator interpretation. On the flat four-torus whose Fourier frequencies are O, put P=-Delta/(4 pi²), so P has eigenvalues N(q). Then

\[
 B(r)=\frac1{24}\{\operatorname{Tr}(e^{-\pi r^2P^2})-1\}.
\tag{12}
\]

This is a fourth-order heat operator with its zero mode removed, followed by the arithmetic scale inverse (9). Positivity of its spectral trace does not assert a positivity-preserving spatial kernel. Unfolding the trace and the u integral gives five continuous dimensions, not three. Formula (11) is a valid alternative, but currently more elaborate than Note10 for the requested combined dimension/simplicity goal.

## 3. The unit-quaternion sphere: a simpler local operator

A different choice is the round unit sphere

\[
 S^3=\{q\in\mathbb H:N(q)=1\},\qquad L=1-\Delta_{S^3}.
\tag{13}
\]

Use the radius-one round metric, Delta with nonpositive eigenvalues, and normalized Haar volume dmu (total mass one). Degree-ell spherical harmonics have eigenvalue ell(ell+2) for -Delta and multiplicity (ell+1)². For completeness: the Euclidean polar Laplacian in dimension four applied to r^ell Y gives Delta_S3 Y=-ell(ell+2)Y. Homogeneous harmonic polynomials have dimension binomial(ell+3,3)-binomial(ell+1,3)=(ell+1)². Harmonic decomposition of polynomials and density of their restrictions give the complete spectrum. Thus L has eigenvalue n² with multiplicity n², n=ell+1>=1.

Define the ordinary shifted heat trace

\[
 Z(s)=\operatorname{Tr}(e^{-\pi sL})
     =\sum_{n\ge1}n^2e^{-\pi s n^2},\qquad s>0.
\tag{14}
\]

The primitive is exactly its Green-weighted trace:

\[
 \boxed{A(r)=\operatorname{Tr}(L^{-1}e^{-\pi r^2L}).}
\tag{15}
\]

The inverse is the inverse of one fixed local elliptic operator, rather than a fitted arithmetic shell denominator. The eigenvalue shift +1 is essential; it turns n²-1 into n². No identification with the conformal Laplacian or an unshifted Dirac square is being made.

More usefully, the **complete source**, not just its primitive, is

\[
 \boxed{\Phi(u)=-\frac\pi2(\partial_u+1)
      \{e^{5u}Z(e^{4u})\}.}
\tag{16}
\]

Direct differentiation of (14) proves (16): each mode gives
(2 pi² n^4 e^(9u)-3 pi n² e^(5u)) exp(-pi n²e^(4u)). The n² multiplicity is geometric, and only one remaining scale derivative is required. Equivalently, with s=e^(4u),

\[
 \Phi(u)=-2\pi s^{3/4}\frac d{ds}\{s^{3/2}Z(s)\}.
\tag{17}
\]

This makes the source a derivative of a dimensionally normalized, shifted round-sphere heat trace.

Integrating (16) by parts just once gives

\[
 \boxed{H(t,z)=\frac\pi2Z(1)+\frac\pi2\int_0^\infty
 e^{5u+tu^2}Z(e^{4u})
 \left[(2tu-1)\cos(zu)-z\sin(zu)\right]du.}
\tag{18}
\]

This has an ordinary second-order local heat operator, no Möbius inversion, no Green inverse in the final H formula, and a first-order rather than second-order observation. It is the cleanest **operator representation** found in this return. It is valid for all finite complex t,z; the same double-exponential majorant applies. The contact pi Z(1)/2 is essential. Commuting (partial_u-1) with (partial_t+partial_z²) on exp(tu²)cos(zu) proves the correct Newman equation. The auxiliary heat parameter s=e^(4u) remains distinct from t.

### An explicit quaternionic Green kernel

Write q=cos(theta)+omega sin(theta), 0<theta<pi, with omega an imaginary unit. The character chi_n(theta)=sin(n theta)/sin(theta) has L-eigenvalue n². The normalized central heat kernel is

\[
 p_s(q)=\sum_{n\ge1}n e^{-\pi sn^2}\chi_n(\theta),
 \qquad p_s(1)=Z(s).
\tag{19}
\]

Here normalization refers to Haar volume; the shifted kernel has total mass exp(-pi s), not one.

The Green kernel is elementary:

\[
 \boxed{G(q)=\frac{\pi-\theta}{2\sin\theta}.}
\tag{20}
\]

The radial Laplacian is f''+2 cot(theta) f'. For f=g/sin(theta), (1-Delta)f=-g''/sin(theta); hence LG=0 away from the identity. Near theta=0, G~pi/(2 theta), the correct unit delta normalization for total-volume-one measure, since ordinary S³ volume is 2 pi². At theta=pi the apparent singularity is removable and G=1/2.

Alternatively, the L² character expansion G=sum chi_n/n follows from sum sin(n theta)/n=(pi-theta)/2, by Abel summation of -log(1-r exp(i theta)). Character orthogonality under normalized Haar measure gives

\[
 \int_{S^3}G(q)p_{r^2}(q)d\mu(q)
       =\sum_{n\ge1}e^{-\pi r^2n^2}=A(r).
\tag{21}
\]

Thus the primitive has an honest three-dimensional Green/heat observation on unit quaternions, without a scalar density manufactured from Phi.

### Dimension and lattice qualification

The sphere spectrum can be indexed by integer triples (n,a,b) with n>=1 and 0<=a,b<n. This is a spectral lattice cone with n² states per n, not a full additive lattice in R³. In (18) the trace already contains the three-dimensional sphere. If it is expanded as an integral of the heat-kernel diagonal and combined with du, the total is four-dimensional. In (21), likewise, adding the scale integral for H makes four dimensions. The diagonal trace is homogeneous on the sphere; simply renaming u as an angular coordinate would not produce a genuine three-dimensional coupled observation. These are real costs, despite the simpler operator and one-derivative completion.

## 4. Comparison, controls and continuation

| Construction | What is exact | Remaining cost for the requested full representation |
| --- | --- | --- |
| Note10 coset Gaussian pair | Full H; rank-three additive coset; three-dimensional scale-and-sphere integral | Two channels, parity sign, elementary correction, second-order observation and boundary |
| Ordinary Hurwitz Epstein series | t=0 H and its zeros/multiplicities on |Im z|<1 | Meromorphic continuation, extra zeta/gamma factor, no simple unchanged-factor time flow |
| Hurwitz Hopf/Möbius construction | Square exponents from quaternion multiplication; full H for all complex t,z | Quartic lattice kernel, signed infinite arithmetic scale inverse, four lattice coordinates; no three-dimensional complete observation |
| Round unit-quaternion heat operator | Full H from the standard local operator 1-Delta; first-order observation | Spectral cone instead of additive full lattice; trace plus scale has four continuous dimensions |

The Hopf formula answers a precise part of the quaternionic suggestion: multiplication produces the correct square exponents naturally. The round-sphere formula answers a different part: curvature and spectral multiplicity give a simple local source operator. These gains should be retained without claiming that every representational requirement is now optimized.

The existing quaternionic positivity and Hodge theorems do not change the signed observation in (11) or (18). Euler-factor controls fail unchanged canonical arithmetic/conductor; weighted-square controls fail the exact canonical multiplicities/full reflection; reflected smooth and positive-primitive controls fail the unchanged square arithmetic. Their generic positivity properties still invalidate a sign argument based only on a positive trace, Green kernel, or norm. No new collision premise or separating bound is acquired, so their event computations are not rerun.

The [shared checker](../numerics/09_check_complete_lattice_and_quaternions_20261027.py) verifies Hurwitz counts, Hopf integrality/norms and Möbius shell inversion through norm 32 by integer arithmetic. It checks the degree/multiplicity shift through ell=39, and compares (18) with the canonical H integral at five real/complex parameter pairs on two grids. The largest fine-grid absolute discrepancy for (18) is below 7.6e-16. These diagnostics are floating, not interval certificates; they do not validate an RH statement. Infinite proofs and imported inputs are given above. The [self-review](../reviews/06_COMPLETE_OBSERVATION_AND_QUATERNION_SELF_REVIEW_20261027.md) is same-assistant and not independent specialist review.

The next bounded question is whether a natural quaternionic projector or geometric quotient can remove the specific sigma_odd multiplicity in (8), or whether the sphere Green/heat formula can combine its scale and group observation without spectator dimensions. Any candidate should be written in full and compared with Note10 and (18) before pursuing zeros. Generic Fueter lifting, taking quaternion norms, or restating physical positivity does not answer that question.
