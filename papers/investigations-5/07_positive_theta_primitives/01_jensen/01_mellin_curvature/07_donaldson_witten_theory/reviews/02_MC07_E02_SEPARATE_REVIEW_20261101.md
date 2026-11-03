# MC07-E02 separate review: point insertions and the Vafa-Witten anomaly

Completed **2 November 2026**, America/New_York, for the **1 November 2026 request R1**; the output filename preserves the issued packet identity. Prepared for **Edward Baker** with substantial LLM assistance. **MC07-E02, E - fixed analytical checking**. Actual reviewer **gpt-6.1-sol / ultra**, verified from the reviewer's runtime turn metadata: thread 01a19a9f-230e-70e3-95b7-a46d0ad43408, turn 01a19a9f-231a-73c3-aa5c-7ced1796b3a4. The author/coordinator is gpt-6-astra / ultra. This is separate cross-model internal LLM checking with shared inputs, not independent specialist human review.

**Disposition: accept at the stated scope, without correction.** The point-insertion obstruction, SO(3) anomaly normalization, complete theta/source extraction, and entire Mellin-period identity with xi check. They provide no new signed Mellin inequality, comparison interval, protected local correlator equal to xi, or proof of RH.

## 1. Fixed inputs and primary checking

The [frozen return](../notes/02_POINT_INSERTIONS_AND_VAFA_WITTEN_ANOMALY_RETURN_20261101.md) has SHA-256 9c3a6c04021bf0506f6b0371d2aa2abfa7a721e6e66107578c9aa92b1ed89162. The [source note](../../../../references/09_VAFA_WITTEN_CONTINUATION_SOURCES_20261101.md) has SHA-256 a2084b99359c7e1a5fe41daaacaf6a52ac6939b7885941b43113d4945876a113. Both match R1. The [review record](../numerics/MC07_E02_REVIEW_RECORD_20261101.json) binds the request, inputs, primary PDFs, fixed rational checks and this review.

The archived primary PDFs were checked against their receipts; their primary URLs were also opened. Selected passages checked:

- [Moore-Witten, hep-th/9709193v2](https://arxiv.org/pdf/hep-th/9709193v2): (1.2)-(1.3), printed p.1; the CP2 SU(2), zero-w2 specialization and (9.23)-(9.24), especially printed p.64. The low-degree polynomials were inspected visually.
- [Dabholkar-Putrov-Witten, arXiv:2004.14387v3](https://arxiv.org/pdf/2004.14387v3): introduction, printed pp.2-5; (3.1), (3.3)-(3.7), pp.14-15; Section 3.3, pp.18-22; the boundary interpretation and (4.32)-(4.38), pp.31-33. Printed pp.14-15 and 33 were inspected visually for eta powers, barred variables and the sign caveat.
- [Vafa-Witten, hep-th/9408074v2](https://arxiv.org/pdf/hep-th/9408074v2): Section 2.5, printed p.34, and (4.23), (4.26), (4.30)-(4.32), pp.64-67; the latter pages were inspected visually. In the original notation, \(f_0=3\widehat h_0\), and the historical completed partition function is \(f_0/\eta^6\).

The [earlier return](../notes/01_DONALDSON_WITTEN_FEASIBILITY_RETURN_20261101.md), its [review](01_MC07_E01_SEPARATE_REVIEW_20261101.md), the [shared source/Mellin convention](../../notes/05_CONTINUATION_PARALLEL_PHYSICAL_DIRECTIONS_20261101.md) and [synthesis](../../notes/06_PARALLEL_PHYSICAL_DIRECTIONS_SYNTHESIS_20261101.md) were checked for inherited normalization and scope. This is selected-passage checking, not a full-paper or novelty review, or recertification of the inherited source-sign theorem.

## 2. Point-insertion coefficients and parity

Moore-Witten's Donaldson polynomials give ordinary coefficients; their exponential series divides a term with N surfaces and m points by \(N!m!\). The relevant generating terms are
\[
-\frac32t+\frac{t^5}{5!}-\frac{pt^3}{3!}
+\frac{3t^9}{9!}+\frac{15pt^7}{4\,7!}+\cdots.
\]
Applying \(-(2/3)\partial_t(1+\lambda\partial_p)\) at p=0 gives
\[
C_\lambda(z)=1+\frac{\lambda}{3}z^2-\frac{z^4}{36}
-\frac{\lambda}{288}z^6-\frac{z^8}{20160}+\cdots.
\]
The fixed standard-library rational check returned exactly \(1,1/3,-1/36,-1/288,-1/20160\), stripping lambda from its two coefficients, and
\[
\frac{-1/20160}{(-1/36)^2}=-\frac9{140}.
\]
After arbitrary nonzero complex rescaling alpha, the powers alpha^4 and alpha^8 cancel in this ratio. Thus \(a_4=-(9/140)a_2^2\) holds for every allowed complex lambda and alpha. Matching positive \(c_0,c_2,c_4\) would require \(a_2=c_2/c_0\), \(a_4=c_4/c_0\), a contradiction. An overall scalar gives the same impossible relation \(c_0c_4=-(9/140)c_2^2\).

For the family extension, N=2n+1 total surfaces gives
\[
2N+4m=8k-6\quad\Longleftrightarrow\quad n+m=2k-2.
\]
Odd point powers affect only odd n; n=0,2,4 are unchanged for every finite odd point polynomial. A nonzero identity coefficient can be normalized to one; with no identity term the constant coefficient is zero. This is a formal argument, needing no convergence of the unexpanded Donaldson series.

The wider positive-source premise is precise: positive mass on x>0, finite total mass and finite eighth moment give strictly positive finite \(c_0,c_2,c_4\). A mass only at zero does not meet it. The exclusion covers the declared CP2 sector, insertion family and through-zero linear dictionary. It does not cover even point powers, a nonzero point source, nonpolynomial insertions, other sectors/manifolds, or nonlinear/affine changes.

## 3. Completion, anomaly and physical conventions

DPW's selected SO(3), w2=0 formula is \(Z_0=3\eta^{-3}\widehat h_0\), with exactly the completion in return (4). The extra eta^-3 in the historical eta^-6 convention is the diagonal U(1) contribution described by DPW. The selected SO(3) global normalization must also be retained rather than silently substituted by the SU(2) partition function.

For an independent differentiation, put
\[
R_n(y)=\frac1{8\pi}\int_y^\infty v^{-3/2}e^{-4\pi n^2v}\,dv.
\]
Since \(\partial_{\bar\tau}y=i/2\) and \(q^{-n^2}\) is holomorphic,
\[
\partial_{\bar\tau}\bigl[R_n(y)q^{-n^2}\bigr]
=-\frac{i}{16\pi}y^{-3/2}e^{-4\pi n^2y}q^{-n^2}
=\frac1{16\pi i}y^{-3/2}\bar q^{n^2}.
\]
For n=0, \(R_0=1/(4\pi\sqrt y)\), and its derivative is nonzero. For nonzero n, the integral bound \(R_n(y)=O(n^{-2}e^{-4\pi n^2y})\), combined with \(|q^{-n^2}|=e^{2\pi n^2y}\), gives normal Gaussian convergence on compact upper-half-plane subsets; the needed derivatives have corresponding bounds. Multiplication by the holomorphic \(3\eta^{-3}\) proves (5), including sign and constant.

At \(\tau=i\beta/2\), \(\bar q=e^{-\pi\beta}\), so the entire prefactor in (6) cancels and \(\mathcal A(\beta)=\Theta(\beta)\) for every beta>0, with \(\beta=8\pi/g^2\). Eta has no upper-half-plane zero. All integer modes and the zero mode are included. The Wirtinger derivative is taken before restriction; differentiation along the imaginary-axis line would involve both Wirtinger derivatives.

The physical caveats are faithfully retained: zero-mode orientation leaves a sign choice, the four-dimensional calculation does not determine the absolute measure constant, and the two-dimensional trace determines the magnitude. The explicit completion fixes the adopted mathematical sign and normalization. Vafa-Witten's compactification caution prevents upgrading this to an ordinary compact-moduli Euler characteristic or constructive four-dimensional path-integral theorem.

Poisson reflection after theta extraction is also distinct from S-duality of one sector. Ordinary S sends beta to 4/beta on this line and mixes sectors; beta to 1/beta corresponds instead to \(\tau\mapsto-1/(4\tau)\).

## 4. Mellin identity, endpoints and the one-eighth normalization

For Re(s)>1, absolute Gaussian integration gives
\[
\frac12\int_0^\infty(\Theta(\beta)-1)\beta^{s/2-1}\,d\beta
=\pi^{-s/2}\Gamma(s/2)\zeta(s).
\]
Splitting at one and applying Poisson summation produces the elementary term \(1/(s-1)-1/s=1/[s(s-1)]\), plus one-half of the symmetric integral J(s) in return (8). Hence
\[
\mathcal X_{\rm VW}(s)=\frac12+\frac{s(s-1)}4J(s)=\xi(s).
\]
On compact s-sets, the integrand and its s-derivatives have integrable bounds because \(\Theta(\beta)-1=O(e^{-\pi\beta})\) at infinity. The prescribed period is entire, and its values at s=0,1 are 1/2. Its zeros are precisely the nontrivial zeta zeros with multiplicities. The full-zero-location assertion is therefore exactly RH; it is an equivalence, not an estimate or finite-zero check.

The inherited source constant can also be checked directly. Set \(f=\Theta-1\), \(L=\beta^2\partial_\beta^2+(3/2)\beta\partial_\beta\), and \(s=(1+z)/2\). Substitution beta=e^(4x) gives
\[
\int_0^\infty\Phi(x)\cosh(zx)\,dx
=\frac18\int_1^\infty Lf(\beta)
\bigl[\beta^{s/2}+\beta^{(1-s)/2}\bigr]\frac{d\beta}{\beta}.
\]
Two integrations by parts evaluate the last integral, before its factor 1/8, as
\[
-2\Theta'(1)-\frac12(\Theta(1)-1)+\frac{s(s-1)}4J(s).
\]
Poisson reflection differentiated at one gives \(\Theta'(1)=-\Theta(1)/4\), making the boundary constant exactly 1/2. This proves \(B_\theta(z)=\xi((1+z)/2)/8\). Complete-source rapid decay permits all z-derivatives and the cosh expansion, giving the stated factorial coefficients. There is no free normalization fit.

## 5. Complete signed source and curvature

Applying L to the full \(\Theta=1+2\sum_{n\ge1}e^{-\pi\beta n^2}\), then multiplying by beta^(1/4), yields exactly
\[
\Phi(x)=\sum_{n\ge1}(2\pi^2n^4e^{9x}-3\pi n^2e^{5x})
e^{-\pi n^2e^{4x}}.
\]
The zero mode vanishes at this step. Both signed differential contributions, the multiplicity from opposite nonzero fluxes, and every positive n remain. Differentiation must act on the full normalized response (6), including its varying prefactor. For x>=0 each complete summand is positive because \(2\pi n^2e^{4x}-3>0\); rapid decay supplies the moment premises. This does not remove h3's negative region.

For the inherited carrier, \(M_3=ZA_3\). Since h3 is sigma-independent and \(T=\partial_\sigma\log w_\sigma\),
\[
(\log Z)''=\operatorname{Var}_\sigma T,\quad
A_3'=\operatorname{Cov}_\sigma(h_3,T),\quad
A_3''=\operatorname{Cov}_\sigma(h_3,(T-E_\sigma T)^2).
\]
These identities give every term, sign and denominator in (12). Carrier positivity and A3>0 retain their inherited internal-review scope; this check does not recertify that theorem. The signed h3 has not become a probability density, square or absolute value. No comparison with kappa3, including the first slab [0,2], is newly covered.

## 6. Information limitation, controls and completion

Adding holomorphic F to Z0 leaves its bar-tau derivative and the subsequent normalized transforms unchanged. This concerns information lost by the derivative, not whether arbitrary additions are admissible physical partition functions. In particular the holomorphic class-number contribution is annihilated; no new counting-data bound reaches (12).

The [result index](../../../../../../../result-summaries/README.md), [theta cluster](../../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md), [control screen](../../../../../../../result-summaries/12_collision_controls_and_screening.md) and [avoid index](../../../../../../../avoid/README.md) apply, especially [shared-premise reviews](../../../../../../../avoid/05_same_model_reviews_and_shared_premises.md), [scoped exclusions](../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md), [normalization](../../../../../../../avoid/08_normalization_and_constant_slips.md), [unchecked imports](../../../../../../../avoid/16_unchecked_imports_and_novelty_claims.md) and [reformulation versus estimate](../../../../../../../avoid/01_restating_the_target.md).

Changed weights, square support or reconstructed sources fail this exact dictionary; positivity or reflection alone cannot restore it. These are premise failures, not exclusions of unspecified gauge realizations. The Gaussian remains a comparator without a cross-theory inequality. No control has passed a new comparison: none is claimed.

**Accepted without correction:** the scoped observable-family obstruction and (4)-(12), under the stated source conventions and inherited hypotheses. No unresolved import blocks this acceptance. One analytical pass and one finite exact-rational check complete E02. No grid, quadrature, new candidate, broadened source search or numerical campaign was undertaken. The frozen return, prior records and shared status files remain unchanged. Any MC07-B03 work remains a separately authorized B task.
