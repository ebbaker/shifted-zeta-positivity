# Forest polynomial and gap-free filtered-spectrum enclosure

23 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual model **gpt-6-astra (Codex)**, reasoning effort **ultra**. Contributing same-model agents independently checked the cubic and Hermite controls and the higher-collision limitation; no independent specialist review or priority claim.

**Status: proved finite coefficient-to-filter error theorem, with an explicit denominator test and a genuine gap-free neighborhood of a double collision.** The inverse-square matrix can be eliminated from the acquisition step: an integer polynomial in the complete prepared coefficients supplies the scalar trace of its rational spectral filter wherever the original matrix and inverse are defined. The same quotient extends through certain double collisions. It does not extend holomorphically through every higher collision, and its denominator can be very small at a heat birth. No canonical theta coefficient accuracy or useful early upper bound is acquired.

This follows the [moving-wall and coefficient theorem](08_CURVED_CONTOUR_TRANSPORT_AND_HEIGHT_GRAPH_20261023.md), [complete source-force estimate](07_COMPLETE_SOURCE_FORCE_AND_FILTER_RESIDUAL_20261023.md), and [spectral consumer](06_PAIR_MATRIX_SPECTRUM_AND_ENDPOINT_MULTIPLICITY_20261023.md). Use the [result index](../../../../result-summaries/README.md), [collision controls](../../../../result-summaries/12_collision_controls_and_screening.md), [avoid index](../../../../avoid/README.md), [coupled-estimate rule](../../../../avoid/12_term_by_term_matching_and_separate_bounds.md), [classification rule](../../../../avoid/01_restating_the_target.md) and [scope rule](../../../../avoid/07_scoped_exclusions_read_as_universal.md). This is a quantitative finite error interface, not another simplicity criterion presented as a theta estimate.

## 1. Complete population and the forest identity

Let P(z)=product_{i=1}^N(z-z_i)=z^N+c_1z^(N-1)+...+c_N be the monic polynomial of a complete finite population acquired by a zero-free spatial wall. No reality or RH assumption is needed for the polynomial statements. Initially suppose the roots are distinct, put M=N(N-1)/2, and define

\[
 \Delta=\prod_{i<j}(z_i-z_j)^2,\qquad
 L=\sum_{i<j}(z_i-z_j)^{-2}v_{ij}v_{ij}^T,
 \quad v_{ij}=e_i-e_j.
\]

For a complex parameter a set

\[
 D(z,a)=\Delta\det(I+aL),\qquad G(z,a)=a\partial_aD(z,a).
 \tag{1}
\]

Let F range over all undirected forests on the labeled vertices {1,...,N}, including the empty forest. Let f=|E(F)| and let
m(F)=product_{C in components(F)}|C|. Then

\[
 \boxed{D(z,a)=\sum_F m(F)a^{|E(F)|}
       \prod_{\{i,j\}\notin E(F)}(z_i-z_j)^2.}
 \tag{2}
\]

In particular every edge occurs at most once in a forest; multiplying by one discriminant clears all the inverse-square denominators in the determinant. This assertion concerns the determinant, not individual entries of an inverse matrix.

**Proof of the coefficient.** Orient the complete graph arbitrarily and let B be its incidence matrix, with columns v_ij. Expanding det(I+aBWB^T) by principal minors and Cauchy–Binet gives a sum over edge sets S with coefficient det(B_S^TB_S) product_{e in S}w_e. A set containing a cycle has dependent columns and contributes zero. For a forest, the incidence Gram determinant is the product of its component sizes: Cauchy–Binet sums squared incidence minors, each surviving minor deletes exactly one row per tree component and has determinant ±1. There are product_C |C| such deletions. Substituting w_ij=(z_i-z_j)^(-2) proves (2). All matrix operations use transpose, not complex conjugation; the identity is algebraic for complex roots.

The right side of (2) is an ordinary polynomial, valid also at colliding roots. Relabeling vertices permutes its forest terms, so it is symmetric in z. The fundamental theorem of symmetric polynomials over the integers yields a unique polynomial

\[
 \mathcal D_N(c_1,\ldots,c_N;a)\in\mathbb Z[c_1,\ldots,c_N,a]
 \quad\hbox{equal to }D(z,a).
 \tag{3}
\]

This reduction is constructive. Expand (2), eliminate the lexicographically largest symmetric monomial with an appropriate product of elementary symmetric functions, and iterate; replace e_j by (-1)^j c_j. The leading-monomial procedure uses integer subtraction and terminates. Each monomial c^beta a^k has weighted degree sum_j j beta_j+2k=2M, and k≤N-1. Translation invariance can be used to center the polynomial before this calculation.

Define \(\mathcal G_N=a\partial_a\mathcal D_N\). On the original domain

\[
 \Delta\ne0,\qquad \mathcal D_N\ne0,
\]

Jacobi's determinant derivative gives

\[
 \boxed{q_a=\operatorname{Tr}\{aL(I+aL)^{-1}\}
       =\frac{\mathcal G_N}{\mathcal D_N}.}
 \tag{4}
\]

Here a is differentiated with the roots, coefficients and time fixed. At a=0 and distinct roots the formula gives q_0=0. Wherever D is nonzero but Delta=0, the quotient defines an analytic continuation of the scalar observable; the original inverse-square matrix itself is undefined there. This distinction will matter below.

## 2. An explicit coefficient-only perturbation theorem

Suppose a complete-population wall theorem has supplied coefficient disks

\[
 |c_j-c_{*,j}|\le\epsilon_j,\quad 1\le j\le N.
 \tag{5}
\]

For example, Note 08, equations (3.2)–(3.4), obtains these from the strict relative wall bound |H/H_*-1|≤eta<1, with no internal gap or root disks. Fix a and expand the already evaluated polynomials

\[
 \mathcal D_N(c;a)=\sum_\beta d_\beta(a)c^\beta,
 \qquad \mathcal G_N(c;a)=\sum_\beta g_\beta(a)c^\beta.
\]

Evaluate coefficients at the chosen a before taking absolute values; this preserves any cancellation between different powers of a. For a polynomial V(c)=sum_beta v_beta c^beta define

\[
 \mathfrak E[V]=\sum_\beta |v_\beta|
 \left\{\prod_j(|c_{*,j}|+\epsilon_j)^{\beta_j}
              -\prod_j|c_{*,j}|^{\beta_j}\right\}.
 \tag{6}
\]

The convention x^0=1 includes x=0. Expanding each monomial at c=c_*+delta c proves
|V(c)-V(c_*)|≤mathfrak E[V]. No eigenvalue separation, root matching, actual discriminant floor or matrix norm estimate enters this bound.

Put

\[
 D_*=\mathcal D_N(c_*;a),\quad G_*=\mathcal G_N(c_*;a),
 \quad E_D=\mathfrak E[\mathcal D_N],\quad E_G=\mathfrak E[\mathcal G_N].
\]

If

\[
 \boxed{|D_*|>E_D,}
 \tag{7}
\]

then every coefficient vector in (5) has |D|≥|D_*|-E_D>0. The quotient q^flat=G/D is analytic throughout that coefficient polydisk, and

\[
 |q^\flat-q_*|\le
 \frac{E_G+|q_*|E_D}{|D_*|-E_D},\qquad q_*=G_*/D_*.
 \tag{8}
\]

For vectors with Delta≠0 this is an enclosure of the original q_a; for vectors with Delta=0 it encloses only its stated scalar continuation. Test (7) does not imply that the roots are simple.

A better estimate retains the numerator/denominator correlation. Form the **complete residual polynomial**

\[
 \mathcal K(c)=\mathcal G_N(c;a)-q_*\mathcal D_N(c;a),
 \qquad \mathcal K(c_*)=0,
\]

and compute E_K=mathfrak E[mathcal K] after combining like monomials. Then

\[
 \boxed{|q^\flat-q_*|\le\frac{E_K}{|D_*|-E_D}.}
 \tag{9}
\]

Indeed q^flat-q_*=K(c)/D(c). Coefficientwise triangle inequalities give E_K≤E_G+|q_*|E_D, so this bound never worsens (8). Any of E_D, E_G and E_K may be replaced by a sharper proved uniform polynomial-error allowance. A rigorous correlated uncertainty set can replace the coefficient disks and improve the allowances further. No positivity of a or reality of the roots is used in this theorem.

The constants are explicit finite polynomial expressions once N is declared. Forest enumeration and symmetric reduction can be expensive at growing N; neither efficiency nor a uniform large-rank estimate is claimed. Exact symbolic coefficients or rigorously enclosed polynomial coefficients are required for a certificate. A floating polynomial construction alone would not certify (7).

## 3. Scaling and a matched direct comparison

For a fixed center c_0 and nonzero scale r, write z_i=c_0+r y_i and a_hat=a/r². Then

\[
 \Delta_z=r^{2M}\Delta_y,\qquad
 \mathcal D_z(c;a)=r^{2M}\mathcal D_y(\widehat c;a_{\rm hat}),
 \qquad G_z=r^{2M}G_y.
 \tag{10}
\]

The quotient and relative error test are unchanged. Centering and scaling may improve coefficient arithmetic, but rescaling both the signal and error does not independently improve a denominator margin. If r is chosen as a function of time, it is held fixed in the partial derivative with respect to a in (1).

Equations (6)–(9) give a direct route from the same wall information to q. They can succeed where a root-disk/smallest-singular-value approach cannot even state uniform root separation, as the double example below shows. This is a finite information and conditioning gain, not a new theta upper bound. An equally informed direct coefficient computation receives exactly the same improvement; a curved time detour has no automatic advantage. Its value would have to come from smaller complete wall errors or a better correlated polynomial residual on the chosen path.

At a fixed common-time real slice where all actual roots are distinct and a≥0, q is real and the complex enclosure may be turned into a real upper bound. Only after independently supplying the canonical real-root and endpoint-coverage hypotheses may such an upper bound feed the simplicity consumer. The theorem does not supply endpoint reality, completeness from partial root samples, or the required small numerical value of q.

## 4. Quadratic formula and a neighborhood with no gap floor

For P=z²+bz+c let delta=b²-4c. The forest identity gives

\[
 D=\delta+2a,\qquad G=2a,\qquad q^\flat=\frac{2a}{\delta+2a}.
 \tag{11}
\]

Given |b-b_*|≤epsilon_b and |c-c_*|≤epsilon_c, the explicit allowance

\[
 E_\delta=2|b_*|\epsilon_b+\epsilon_b^2+4\epsilon_c
\]

is also E_D; the numerator has no coefficient error. If |delta_*+2a|>E_delta, the coupled error is at most

\[
 |q^\flat-q_*|\le
 \frac{|q_*|E_\delta}{|\delta_*+2a|-E_\delta}.
 \tag{12}
\]

Take a>0, the double reference P_*=z², and the coefficient family P=z²+c with |c|≤a/8. Then

\[
 |D|\ge3a/2,\qquad q_*=1,\qquad |q^\flat-1|\le1/3.
 \tag{13}
\]

This polydisk includes c=0 and arbitrarily small nonzero discriminants, so no positive internal gap floor or pair of disjoint single-root disks can hold uniformly on it. Nevertheless the scalar filter has the explicit stable enclosure (13). At c=0 this is the analytic scalar continuation, not an evaluation of an undefined L. This example establishes the claimed finite error-theorem gain, while its value near one is of no use for an all-simple threshold q<1/2.

These are bounds for the scalar trace q only. They do not bound the norm of the full resolvent for a nonnormal complex L: the equilateral cubic in Section 5 has q=0 and det(I+aL)=1 while its nonzero nilpotent matrix and resolvent can grow as its roots coalesce.

The separate resolvent obligation has not disappeared. For the simple-endpoint heat polynomial H(tau,z)=z²-1-2tau with a=4tau,

\[
 D=4+16\tau,\qquad q=\frac{2\tau}{1+4\tau}.
\]

Its denominator vanishes at tau=-1/4 while the discriminant is 2. Test (7) detects the same obstruction that a matrix resolvent test detects, now directly in coefficients.

## 5. Cubic formula, simultaneous doubles and higher-collision limits

For P=z³+bz²+cz+d put

\[
 B=b^2-3c,\qquad
 \Delta=b^2c^2-4c^3-4b^3d-27d^2+18bcd.
\]

The elementary identities for the three squared gaps give sum gap²=2B and sum of products of two squared gaps=B². Hence

\[
 \boxed{D=\Delta+2aB^2+6a^2B,\qquad
 G=2aB^2+12a^2B.}
 \tag{14}
\]

For explicit acquisition, obtain E_Delta by applying (6) to the displayed discriminant and let
E_B=2|b_*|epsilon_b+epsilon_b²+3epsilon_c. Then valid alternative error allowances for D and K are

\[
 E_D^{\rm alt}:=E_\Delta+2|a|E_B(2|B_*|+E_B)+6|a|^2E_B,
\]
\[
 E_K^{\rm alt}:=|q_*|E_\Delta
 +2|a||1-q_*|E_B(2|B_*|+E_B)
 +6|a|^2|2-q_*|E_B.
 \tag{15}
\]

One may take the minimum with the directly computed majorants (6). Neither representation is universally sharper: combining the coefficient residual retains common coefficients, whereas the B-based bounds can retain cancellation at B_*=0.

**Triples retain a zero denominator.** At an exact triple root B=Delta=0, so D=0 for every a. More generally, if any m≥3 roots coincide, every nonzero term of (2) would have to include all edges of the complete graph on those m vertices, which contains a cycle. No forest does so; D vanishes. Clearing poles therefore does not by itself produce a nonzero denominator at a higher collision.

Nor is that higher zero automatically removable in a full complex coefficient neighborhood. Fix a≠0 and approach the centered triple P=z³ in two ways. Along P=z³+pz with real p<0, (14) gives q→2. Along P=z³-r³ with r≠0, B=0, Delta=-27r^6, and q=0 identically. The latter roots form an equilateral complex configuration. Thus the two-variable rational function has no continuous, hence no holomorphic, coefficient-space extension at the triple. A directional limit along a real heat birth can still exist and must be stated with that restriction.

**Restricted real cubic cone.** An independently established real-rootedness premise allows a different reduction through a triple. After centering the cubic, its discriminant satisfies

\[
 B\ge0,\qquad 0\le\Delta\le\frac4{27}B^3.
\]

For B>0 divide (14) by B. With fixed a>0 and kappa=B/a, this yields

\[
 \boxed{\frac{2\kappa+12}{4\kappa^2/27+2\kappa+6}
 \le q^\flat\le\frac{2\kappa+12}{2\kappa+6}.}
 \tag{15a}
\]

The reduced denominator Delta/B+2aB+6a² is at least 6a². Both ends tend to 2 as B decreases to zero. Thus the quotient has a continuous extension with value 2 at the triple **within the real-rooted coefficient cone**, despite its failure to extend to a complex coefficient neighborhood. For example, 0≤B≤a/10 implies

\[
 \frac{8235}{4186}\le q^\flat\le2,
 \tag{15b}
\]

including the triple only in that continuous sense. The lower bounding function in (15a) is decreasing for kappa≥0, so insertion of 1/10 proves the constant. Real-rootedness and a>0 are additional premises here; these inequalities cannot be imported into a complex-time contour. They bound the retained collision mass rather than excluding it.

**Separated simultaneous doubles can be covered.** If the roots are real, a>0, and all multiplicities are at most two, choose the forest consisting of every within-double edge and no other edge. It is a matching; its complement contains only nonzero squared gaps. Its contribution to (2) is strictly positive. All other forest terms are nonnegative, so D>0. Together with the preceding forest-cycle argument, this proves D>0 for a real root multiset and fixed a>0 if and only if every multiplicity is at most two. The quotient is therefore analytic in a sufficiently small complex coefficient neighborhood of every such configuration, even though Delta=0 at a double-collision center.

For an explicit four-root check with double sites at -b and b, b≠0 real, set d_0=2b. Mandatory within-double edges and the four possible extra cross edges give exactly

\[
 D=4a^2d_0^8+16a^3d_0^6
   =4a^2d_0^8(1+4a/d_0^2),
\]
\[
 q^\flat=2+\frac{4a/d_0^2}{1+4a/d_0^2}.
 \tag{16}
\]

For a>0 the denominator is positive. Two saturated internal modes and one finite collective mode remain. This is a polynomial snapshot identity, not a claim that a product of independently evolved double factors solves the heat equation.

## 6. Heat-birth normalization and the unavoidable error scale

For the genuine monic m-root heat polynomial

\[
 P_m(t,z)=e^{-t\partial_z^2}z^m,
 \qquad z_j(t)=\sqrt{2t}\,h_{m,j},\quad t>0,
\]

the h's are the zeros of the probabilists' monic Hermite polynomial. Put J=m(m-1)/2 and C_m=product_{j=1}^m j^j. Its discriminant and exact forest polynomial are

\[
 \Delta_m=(2t)^J C_m,
\]
\[
 \boxed{D_m(t,a)=(2t)^J C_m
       \prod_{k=1}^{m-1}\left(1+\frac{ak}{4t}\right).}
 \tag{17}
\]

The Hermite discriminant follows from He_m'=m He_(m-1) and the monic recurrence: successive resultants differ by (-1)^(m-1)(m-1)^(m-1), giving C_m after the discriminant sign. The determinant factor in (17) uses the inherited spectrum lambda_k(L)=k/(4t). Therefore at the program's a=4t,

\[
 D_m(t,4t)=(2t)^J C_m\,m!,\qquad
 q_{4t}=\sum_{k=1}^{m-1}\frac{k}{k+1}=m-H_m.
 \tag{18}
\]

Here G is computed by first differentiating at fixed t and then setting a=4t; it is not the total time derivative of D_m(t,4t).

In particular the double has D=8t+2a and q_(4t)=1/2. The triple has

\[
 D=108t(a+2t)(a+4t),\qquad
 D(t,4t)=5184t^3,\qquad q_{4t}=7/6.
 \tag{19}
\]

The raw denominator tends to zero at order t^J even though q has a finite collision signature. Thus an uncorrelated absolute allowance must be smaller than that scale to pass (7); more precisely E_D<|D_*| and the coupled residual E_K must be small relative to the same denominator to give a small quotient error. Polynomialization does not remove this precision cost.

A declared single-cluster blowup gives a regular alternative. Set y=(z-z_0)/sqrt(2t), a_hat=a/(2t), and let c_hat be the coefficients of the monic scaled polynomial. Formula (10) becomes

\[
 D=(2t)^J\widehat D(\widehat c;a_{\rm hat}).
\]

For an actual analytic m-fold heat birth, c_hat tends to the Hermite coefficient vector, and a=4t gives a_hat=2. At that reference
\(\widehat D=C_m m!>0\). The coefficient theorem in Section 2 therefore gives a genuine finite error neighborhood in these scaled coefficients, free of internal root gaps. However the physical coefficient errors must be correspondingly scaled: after the declared translation, the jth coefficient error is divided by (2t)^(j/2). A source theorem providing those scaled errors is still required. The event location/type and the scaling cannot be presumed from unknown endpoint multiplicities in an attempted simplicity proof. If the source-to-coefficient acquisition uses a reference wall |z-z_0|=R sqrt(2t) whose normalized Hermite polynomial is bounded away from zero there, the unnormalized reference field has size comparable to t^(m/2), provided its analytic unit has a nonzero finite limit. A fixed small relative wall error therefore requires an absolute error at most a fixed small multiple of t^(m/2); a vanishing relative error requires o(t^(m/2)). This cost is part of the source acquisition, not supplied by normalization.

The coefficient precision can be tested exactly. For the perturbed centered cubic snapshots

\[
 P(t,z)=z^3-6tz+\eta t^{3/2},\qquad a=4t,
\]

formula (14) gives

\[
 q=\frac{6048}{5184-27\eta^2}.
 \tag{19a}
\]

For real eta with |eta|<sqrt(32), these snapshots have three distinct real roots; at equality they have a double and the displayed value is the scalar continuation. A fixed nonzero eta changes q from 7/6 by a fixed nonvanishing amount as t decreases to zero, even though the absolute constant-coefficient error is O(t^(3/2)). This is a coefficient-error example, not a claim that the time-dependent perturbed snapshots solve the heat equation. In depressed cubic coordinates, error o(t) in the linear coefficient and o(t^(3/2)) in the constant coefficient is a sufficient condition for vanishing normalized shape error; an uncentered formulation must also pay its translation error. The example does not exclude a correlated error class on which the quotient is more stable.

For several separated endpoint clusters of multiplicities m_l, let J_total=sum_l m_l(m_l-1)/2. Along their real heat births, cross-cluster factors tend to nonzero constants, and

\[
 \Delta\sim C t^{J_{\rm total}},\qquad
 D(t,4t)\sim C t^{J_{\rm total}}\prod_l m_l!,\qquad
 q_{4t}\longrightarrow\sum_l(m_l-H_{m_l}),
 \tag{20}
\]

where C>0 includes the limiting cross separations and Hermite discriminants. Hence two simultaneous doubles with a=4t have a denominator of order t², despite the fixed-a continuation in (16). A full-cluster or otherwise justified deflation must retain this scale. Equation (20) is a directional statement for declared separated clusters; it does not provide an arbitrary coefficient-space extension at higher collisions.

## 7. Controls, application status and fair comparison

The quadratic, cubic and Hermite computations verify the determinant coefficient, the filter numerator and the a=4t normalization. The supporting [exact-rational replay](../numerics/05_check_forest_filter_20261023.py) and [small result record](../numerics/05_FOREST_FILTER_CHECKS_20261023.json) check forest identities and these sharp controls; they do not certify theta data. The [separate same-model review](../reviews/09_FOREST_FILTER_AND_COLLISION_CONDITIONING_REVIEW_20261023.md) assesses collision continuation and conditioning. The equilateral cubic disproves a universal higher-collision removability claim. The simultaneous-double calculation shows that this limitation does not invalidate the gap-free double-neighborhood theorem. These controls preserve the hypotheses of the specific algebraic assertions being tested.

All registered holomorphic heat controls obey (2)–(9) on their actual complete finite populations and admissible denominator domains. A claimed source-based bound below the endpoint collision threshold must still fail on a matching collision population. Weighted-square, reflected and positive-primitive controls are not assigned an unproved complete all-real heat interval. The unchanged theta source is not selected by the forest identity alone.

The concrete gain over Note 08's root-disk route is the following: complete coefficient enclosures plus the explicit polynomial test (7) can enclose the scalar filter uniformly over a neighborhood containing double collisions, where a positive internal separation floor is impossible. The complete residual (9) preserves numerator/denominator correlation. This is compatible with the extra resolvent pole in Section 4 and the higher-collision obstruction in Section 5.

What remains unpaid is a useful canonical coefficient/error package at a source-prescribed time and population, with |D_*|-E_D and E_K adequate for an upper filter threshold. The same data benefit a direct wall-to-coefficient computation; no generic advantage of a curved path is claimed. Growing-rank polynomial conditioning, complete source tails, endpoint coverage, and any theta simplicity conclusion remain open.
