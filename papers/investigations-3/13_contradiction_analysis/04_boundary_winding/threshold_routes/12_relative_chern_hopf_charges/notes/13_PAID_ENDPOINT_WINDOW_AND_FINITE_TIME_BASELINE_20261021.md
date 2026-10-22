# Paid endpoint window and finite-time comparison baseline

21 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**, reasoning effort **ultra**, verified from the active parent turn metadata. Developed by a separate same-model agent and checked by another agent and the producing assistant; see [Review 12](../reviews/12_FINITE_TIME_SIGNED_RECONSTRUCTION_OPENING_REVIEW_20261021.md). **Status: proved in-note in the stated conditional parameterized scope; internal LLM review only.** No numerical theta domain, positive endpoint margin or specialist validation.

Read together with [Note 07][n07], [Note 11][n11], [Note 12][n12], the [manuscript source response][source], the [result index][results] and [collision controls][controls], and the [avoid index][avoid], especially [target classification][a01], [matched controls][a02], [scoped conclusions][a07] and [coupled estimates][a12]. This is an explicit applicability/cutoff estimate and matched-comparison screen, not another endpoint-positivity criterion.

## 1. An elementary complete-tail envelope

Use the exact normalization

    lambda_n=pi n^2,
    phi_n(u)=lambda_n exp(5u)(2lambda_n exp(4u)-3)exp(-lambda_n exp(4u)).

Write R_M=sum_(n>M) phi_n, beta=pi(M+1)^2 and

    theta_M=((M+2)/(M+1))^2 exp(-pi(2M+3)).

For Tbar>=0, Z>=0, beta>=9+Z and Tbar<=8 beta, every j>=0 satisfies

    integral_0^infty u^j R_M(u) exp(Tbar u^2) cosh(Zu) du
    <= b_(M,j):= (2 j!/3^(j+1)) beta^(1-j)exp(-beta)/(1-theta_M).       (1)

Proof: phi_n<=2lambda_n^2 exp(9u-lambda_n exp(4u)). Since exp(4u)>=1+4u+8u^2 and cosh(Zu)<=exp(Zu), the integrand is bounded by

    2lambda_n^2 exp(-lambda_n) u^j
       exp(-(4lambda_n-9-Z)u-(8lambda_n-Tbar)u^2)
    <=2lambda_n^2 exp(-lambda_n)u^j exp(-3lambda_n u).

Integration gives the first term in (1). Successive ratios of lambda_n^(1-j)exp(-lambda_n), for n>=M+1 and j>=0, are at most theta_M. Thus the displayed geometric series accounts for *all* omitted modes and the entire source ray. This bound does not depend on real center a, since real oscillation was discarded.

To avoid leaving complete derivative constants qualitative, take T0=R0=1. Valid upper bounds for the source moments B_j=integral Phi(u)u^j exp(u^2)cosh(u)du, j=2,3, are

    Bbar_j = 2 j! pi^2 exp(-pi)/(4pi-10)^(j+1)
       + (2 j!/3^(j+1))(4pi)^(1-j)exp(-4pi)
           /(1-(3/2)^2 exp(-5pi)).                               (2)

The n=1 term uses 4pi-10>0 directly; n>=2 uses (1). Bbar_j can replace B_j in every bound below. No floating-point evaluation is required for these inequalities.

## 2. A completely specified hypothetical-double family

Conditionally suppose H(0,a)=H_z(0,a)=0 and q=|H_zz(0,a)|/2>0 at a finite a>0. This covers either sign by evenness; a=0 is excluded by H(0,0)>0. Define

    R=min(1/2,a/2,q/Bbar_3), r=R/2,
    h=min(1/2,qR^2/(16sqrt(2)Bbar_2),R^2/128).

Note 07's proof, with the valid upper bounds (2), gives exactly two H roots inside each circle |z-a|=s, s=r,R, throughout |Re t|,|Im t|<=h, and

    |H(t,z)|>q s^2/2.

Let b_M=b_(M,0), using Tbar=1,Z=R in (1). Every M>=1 satisfies beta>=4pi>9+R and 1<=8beta. Choose **the least M>=1** with

    b_M <= q r^2/8 = qR^2/32.                                 (3)

Such an M exists because beta exp(-beta)/(1-theta_M) tends to zero. Set

    F_M(t,z)=integral S_M(u)exp(tu^2)cos(zu)du,
    E_M(t,z)=integral R_M(u)exp(tu^2)cos(zu)du.

On the entire closed spacetime product, |E_M|<=b_M. Rouche on both walls gives exactly two roots of F_M in each disk and no zero in their collar. In particular, the endpoint reference F=F_M(0,.) has both roots in |z-a|<r, including a possible reference double. An explicit outer floor and actual full-residual ratio are

    delta_M=qR^2/2-b_M >=15qR^2/32,
    sup_|z-a|=R |E_M(0,z)/F(z)| <= rho_M=b_M/delta_M <=1/15.       (4)

The inner head floor is at least 3q r^2/8. All theta modes and the full source ray are included in (1), so (4) is an actual E/F bound, not a ratio for a truncated numerical residual. Neither the root counts nor (4) assumes a positive internal gap. The additional R<=a/2 puts the complete reference cluster in Re z>0, for the canonical-kernel comparison below. No assertion is made that a theta double exists.

The dependence on height remains through the actual local q(a), the oscillations in F and E, and hence the cutoff (3). No uniform positive q, R or h is established. A lower certified q would suffice for conservative parameters; the event equalities themselves are conditional hypotheses, not numerically verified facts.

A wider, directly checkable domain uses the complete jets c0=H(0,a), c1=H_z(0,a), c2=H_zz(0,a)/2, q=|c2|>0. For 0<r<R<=1 and sqrt(2)h<=1 put

    d_s=q s^2-|c0|-s|c1|-Bbar_3 s^3/6-sqrt(2)h Bbar_2, s=r,R.

If d_r,d_R>0, both H counts follow by comparison with c2(z-a)^2. Any M with b_M<min(d_r,d_R) gives the corresponding head counts; delta=d_R-b_M and rho=b_M/delta<1 require additionally b_M<d_R/2. These inequalities contain the exact-double family above and can be checked on supplied complete source enclosures. **No new actual-theta numerical parameter domain is verified in this note.**

## 3. The complete direct Note 11 interval

For this fixed F and contour Gamma, let c be the reference two-root centroid. Retain Note 11's

    L(V)=-4 I[(z-c)V/F],
    B(V,W)=2 I[(z-c)VW/F^2]-I[V/F]I[W/F], Q(V)=B(V,V),
    C_L=4R(R+r)/delta_M,
    C_B=(2R(R+r)+R^2)/delta_M^2.

Define the actual canonical W=phi_M exp(-(beta-pi M^2)(exp(4u)-1)), the normalized tail mass m_M=R_M(0)/phi_M(0), and first-omitted mass A_M=((M+1)/M)^4 exp(-pi(2M+1)). The probability law lambda^can_M on [0,infinity] is fixed by

    lambda^can_M([u,infinity])=R_M(u)/(m_M W(u)),
    lambda^can_M({infinity})=A_M/m_M.

Its finite part is -(1/m_M)d(R_M/W), which is nonnegative by the manuscript's explicit Laplace-law theorem. These are the exact masses, not adjustable monotone envelopes. Let

    V_w(z)=integral_0^w W(u)cos(zu)du,
    N(w)=integral_0^w W(u)cosh(Ru)du,
    mu_M=m_M N(infinity).

For any declared integer J>=1 take equal N-coordinate cells (the last includes infinity), actual masses p_j=lambda^can_M(I_j), and midpoint representatives N(w_j)=(j-1/2)N(infinity)/J. Then

    Ehat=m_M sum_j p_j V_(w_j),
    epsilon_J=mu_M/(2J),
    Ecal_J=(C_L+2C_B mu_M)epsilon_J.                            (5)

Note 11 proves ||E-Ehat||_Gamma<=epsilon_J and the complete interval

    I_direct = [D_J-Ecal_J-C3(rho_M), D_J+Ecal_J+C3(rho_M)],
    D_J=Delta_F+L(Ehat)+Q(Ehat),                               (6)

where l2=-log(1-rho)-rho, l3=l2-rho^2/2 and

    C3(rho)=4R(R+r)l3+R^2(2rho l2+l2^2).

Everything in (6) is now an explicit function/integral of a,q,R,M,J and the unchanged canonical source. The formula supplies complete analytic endpoints, **not evaluated numerical endpoints or their sign**. Exact integrals/masses have zero acquisition error by definition. If implemented numerically, contour evaluations, actual masses, finite rays and all modes in the scalar mass must receive certified acquisition allowances. For a common residual perturbation bounded by eta, a safe extra response allowance is (C_L+2C_B mu_M)eta+C_B eta^2; independent errors in the evaluated D_J must also be added. A comparison cannot call an uncomputed integral exact acquisition or claim free computational accuracy.

For a fully elementary upper control on mu_M, put

    k=M+1, D0=2pi M^2-3,
    varrho_M=((k+1)/k)^4 exp(-pi(2k+1)),
    kappa_M=(1+3/D0)/(1-varrho_M).

The manuscript gives m_M/A_M<=kappa_M. Since R_M>=A_M W,

    mu_M <= kappa_M integral R_M cosh(Ru)du <= kappa_M b_M.       (7)

One can substitute this in (5); retaining the exact mu_M is sharper. The actual wall ratio remains (4), so it does not rely on unnecessarily replacing the true tail by the larger canonical envelope.

Under the hypothetical-double assumptions, any valid interval (6) contains zero, because Delta_H=0. This is a consistency control, not a proof that an additional theta-specific inequality could never yield a contradiction. Existing Note 11 already explains the head/tail cancellation that prevents interpreting a positive tail or a negative head event as the missing theta surplus.

For the covariance candidate, [Note 15](15_CANONICAL_COVARIANCE_SIGNED_ENCLOSURE_20261021.md), §5, declares a **second matched baseline**: the inherited exact cell-range method on common uniform x=e^-4w cells with a separate exact infinity atom. Its strict comparison retains this same grid and law in both methods. It does not assert fixed-J containment against (6), the equal-N grid, or optimized/adaptive partitions. Additional first and second cell moments and their acquisition errors are disclosed there.

## 4. A finite matching-time range and the equal-information screen

A concrete range requiring no large-time asymptotics is

    R^2/8 <= T <= R^2/4.                                      (8)

Since R<=1/2, 0<T<=1/16, and the complete source bound (1) with Tbar=1 applies. Its generic contour inflation obeys exp(R^2/(4T))<=e^2. Matching T need not be <=h: the Gaussian transfer evolves only the complete residual field; the two-root reference and response functionals stay at zero, and this operation does not continue root labels to T.

If the trial approximation is exactly

    P_T(y)=m_M sum_j p_j integral_0^(w_j) W(u)exp(Tu^2)cos(yu)du,

Gaussian reconstruction gives p0=Ehat for every T in (8). The omitted source density is the same fixed signed density for every T. Consequently the central D_J, the actual canonical law, wall ratio and cubic remainder are identical to (6). A proof that merely reconstructs the same law-cell bounds has **no strict interval improvement** to report. This is a candidate-specific outcome for the fixed canonical cell approximation, not a theorem against all finite-time methods.

A possible new comparison must make one of these distinctions explicit:

* A different T-dependent approximation changes the endpoint approximation p0. Give the competitive direct method that same reconstructed approximation and source information; do not attribute the approximation change itself to elapsed heat time.
* Smaller terminal numerical error or additional accurate moments are additional data. Charge them to both methods, or describe the comparison as an acquisition experiment with a measured cost contract.
* Gaussian/Hermite correlations, signed quadratic coupling, or contour-adapted response estimates may improve the old sup-norm payment. Such a gain needs an explicit strict inequality for the complete interval, with both endpoints reported. It may be a better estimator of endpoint information rather than a time-evolution gain.
* All finite real-line integration tails must be paid even though the canonical source is complete. For a bounded field residual |r_T|<=A_T, the contribution to Gaussian L2 energy outside |y-a|<=Y is <=A_T^2 erfc(Y/(2sqrt(T))). More accurate oscillatory tails are admissible if proved.

There is no reason to extend T toward infinity before such a strict paid comparison. The range (8) is an explicit pilot range, not a claim of optimality.

## 5. Candidate-specific collision audit and dispositions

The complete theta mode and mass formulas, especially (1), (3), and the canonical probabilities in (5), are the theta-specific data used here. The generic Rouche, discriminant-response, Gaussian transfer and source-error arguments hold for matching colliding controls with their own bounds. They make no favorable sign inference. The quadratic heat control has the compatible exact event and no theta source; for this control the literal canonical bound is unavailable. Euler-factor controls change the canonical arithmetic. Weighted-square and finite-prime controls lack the full normalized reflection/coefficient conjunction. Reflected super-Gaussian and smooth positive-primitive controls lack canonical square coefficients. Close normalized endpoint controls fail ordinary Dirichlet-series arithmetic. Their own positive source/jet bounds still pay the local window and their discriminant interval must contain zero on a domain containing their double. Saying a source lacks the exact theta formula is not evidence it violates the derived numerical inequality; no such discrimination has been proved here.

Cubic or higher births are outside the exactly-two-root hypothesis; q=0 makes this event prescription inapplicable. The work does not discharge the separate multiplicity task.

Task dispositions (recorded in the [progress register][progress]):

* FTSR-01: **proved conditional parameterized window and complete symbolic direct baseline; no evaluated actual-theta event domain**. The new concrete content is (1)--(4), which makes the canonical cutoff and wall ratio feasible at every hypothetical ordinary double. If the register's completion standard requires a verified numerical near-event theta parameter set, retain that implementation subtask as open.
* FTSR-02: the explicit bounded range (8) and evolved canonical cell approximation are admissible and fully source-integrable; the latter reconstructs the same direct approximation. Any genuinely new approximation remains a separate task.
* FTSR-04: the fixed canonical-cell exact-evolution comparison yields equality if the same source bounds are reused. No strict gain or sign established; this does not settle better signed/correlated estimators.
* FTSR-05: this candidate passes generic collision consistency and lists its canonical-data premises. No actual distinguishing sign is claimed.
* FTSR-06 and FTSR-07: remain gated, and the global height and higher-multiplicity obligations retain their original status.

[n07]: 07_QUANTITATIVE_ENDPOINT_WINDOWS_AND_HEIGHT_COVERAGE_20261021.md
[n11]: 11_CANONICAL_QUADRATIC_RESPONSE_AND_HEAD_TAIL_CANCELLATION_20261021.md
[n12]: 12_LARGE_TIME_INFORMATION_AND_ENDPOINT_RECONSTRUCTION_20261021.md
[source]: ../manuscript/source.tex
[progress]: ../research-progress/03_FINITE_TIME_SIGNED_RECONSTRUCTION_PROGRESS_20261021.md
[results]: ../../../../../../../result-summaries/README.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../../avoid/README.md
[a01]: ../../../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
