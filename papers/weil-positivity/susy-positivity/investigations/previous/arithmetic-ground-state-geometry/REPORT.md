# Arithmetic ground-state geometry: constructions and the physical-pairing problem

The investigation has a closed positive source whose pairing equals the complete finite-interval Weil form **plus an explicit positive finite-rank error**. A joint gamma-and-prime response removes the error exactly on a high-mode subspace selected by a proved Neumann bound. The remaining low/high interaction is retained, and the unresolved sign becomes an explicit finite matrix comparison. This remains a positive completion, not a proof of full Weil positivity.

The [new review](notes/18_REVIEW_AND_NEUMANN_COMPARISON.md) found no invalidating error in the central constructions of notes 10–17 and reproduced all 39 earlier algebra checks. Their limitations remain material: the physical chiral-metric identification is conditional as stated; the quartic cap is an isometric label in the arithmetic source; the arithmetic gains are prescribed; and a compact error cannot be discarded.

[Note 19](notes/19_JOINT_RESPONSE_AND_FINITE_RANK_DEFECT.md) gives the new source, its domain and adjoint, a convergent expansion retaining mixed prime/gamma responses, and the finite-rank defect. It establishes compatibility within a fixed support envelope. Positivity of the remaining finite matrix and compatibility under arbitrary envelope enlargement are still open. The method is also available for non-arithmetic semibounded forms, so it is not by itself an arithmetic mechanism.

## Analytical sign continuation: note 20

[Note 20](notes/20_ARITHMETIC_SIGN_AND_BOUNDARY_RESPONSE.md) audits the live reduction, develops four distinct sign mechanisms and pursues the mixed-response route. The audit finds no invalidating domain or normalization gap under the stated hypotheses. It separates the arithmetic masses, contact, residues and prime-power data from the generic positive-source and Schur calculus. In particular, changing the positive reference shift leaves the remaining Schur matrix unchanged.

The new boundary theorem proves, for every positive support length,
\[
T_L=b(H_{\rm N})+\mathcal K_L,\qquad
\mathcal K_L\ge0\text{ bounded},\qquad
\|\mathcal K_L\|_{\rm ess}=\pi/2.
\]
The operator and form domains equal the corresponding Neumann logarithmic domains, and finite cosine sums are an operator core. Each mass contributes an explicit positive rank-two endpoint kernel. Their sum converges strongly but not in operator norm: every finite mass tail has norm at least \(\pi/2\). This is a rigorous obstruction to treating the boundary correction as a compact or norm-small remainder.

The narrower finite-input mechanism survives. The exact cosine columns have a tail of order \(a_J^{-1/2}\) at fixed input dimension. They give the gamma part of the complete mixed block
\[
B=Q\mathcal K_LP+QP_L^{\rm pole}P-QJ_L^{\rm off}P.
\]
A finite positive high-sector Galerkin response \(Y_K\), with full residual \(R_K=B-HY_K\), yields
\[
S_N\ge PW_LP-B^*Y_K-d_K^{-1}R_K^*R_K,
\quad d_K=b((K\pi/L)^2)-\beta_L>0.
\]
The proof retains the infinite inverse response via its residual. The note supplies mass and mode tail bounds and propagation of enclosure errors. The missing arithmetic lemma is a length-dependent trial rule making this lower matrix nonnegative, with every error included. No such all-length sign estimate is claimed.

The ordered-response alternative has an exact warning: at every finite truncation order, a rational positive-reference example has a positive truncated Schur matrix but a negative exact target. The omitted inverse tail lowers the true Schur matrix. The physical-gluing alternative needs an independently specified contraction satisfying an arithmetic intertwining identity; abstract existence of that contraction is exactly the unresolved ordering. The unit cap does not distinguish the negative control.

A fourth route exposes the prime discrepancy directly. With
\(E(r)=\sum_{p^m\le e^r}\log p-e^r+1\) and
\(h_f(r)=\operatorname{Re}\langle E_Lf,U_rE_Lf\rangle\),
\[
Q_L[f]=K_{\ge1}[E_Lf]+(4+w_0)\|f\|^2
-2\int_0^Le^{-r/2}h_f(r)\,dE(r).
\]
This is an exact cancellation of the lowest gamma response against the pole and smooth-density terms, valid on the full logarithmic domain. The derivative form is used only on the smooth core. Replacing the atomic prime measure by \(e^rdr\) while preserving all archimedean data gives a negative control at length two:
\[
Q_2^{\rm dens}[\cos(\pi x/2)]<-2979/6125.
\]
The bound controls the entire higher-mass tower and extends to a smooth compactly supported negative witness. Leading density alone therefore cannot supply the ordering. This obstruction does not exclude arguments using the actual signed prime discrepancy. Requiring its exact lower bound for every input is simply Weil positivity rewritten.

For arbitrary support, an independently proved Schur inequality at each length, or at a cofinal sequence of lengths, would suffice. Neither fixed dimension nor a uniform positive full-form gap nor compatible physical sources across all envelopes are required for that theorem. Constructing the compatible physical sources is a separate task. The preceding live manuscript is preserved in [a new dated snapshot](archive/drafts/20260913-before-sign-analysis/README.md); supported results are integrated in the current sections 10 and 14–15.

## Initial local-factor findings

| Result | What is established | What it does not establish |
|---|---|---|
| Four-supercharge cylinder theory | A positive self-adjoint Hamiltonian with an angular boson and form-valued fermions; one normalizable vacuum for nonzero cylinder parameter | The old scalar Morse state is not retained, and its gamma norm is not inherited. |
| Quadratic prime sector | Two complex fields give the physical metric \(|1-q|^{-2}\) in a specified holomorphic source frame | Its curvature is flat; the source normalization remains substantive. |
| Interacting quartic prime sector | Nine normalizable middle-degree vacua and a well-defined positive matrix metric | Fixed quartic coupling cannot retain the Euler identity period on any flat convergent cycle. |
| Interaction scaled with prime mass | Both the Euler pole in a period and its modulus-squared dependence in a physical metric survive, up to separate fixed constants | The mass is removable by a field dilation, so this alone creates no new chiral curvature. |
| Non-Abelian metric controls | Positive semisimple rank-two \(tt^*\) solutions can retain the real arithmetic norm with a changed complex extension | They do not supply the original arithmetic observable or a microscopic theory. |
| Ground-transform exclusions | Scalar reversible energies and scalar phase changes have the wrong full-kernel sign structure on explicit short intervals | Matrix/fermionic interference and nonlocal observables remain possible. |

All of these conclusions are analytical. The self-contained [integrated manuscript](manuscript.pdf) now includes both these initial findings and the results of notes 06–20 described below; the [coverage map](MANUSCRIPT_COVERAGE.md) locates them. The [draft archive](archive/drafts/README.md) preserves the previous and integrated PDF/TeX versions. The exact-algebra programs check displayed identities; they do not validate analytical proofs. The rational high-mode cutoff is an inequality certificate for the complementary sector only, not full arithmetic positivity.

## The positive enlarged theory

Replace the real Morse coordinate by a flat cylinder \(Y=y+i\theta\), with \(\theta\) periodic. On the ordinary positive Hilbert space of square-integrable differential forms, use
\[
\mathcal W_a(Y)=\tfrac12(e^Y-aY),\qquad h=\Re\mathcal W_a.
\]
The real function is harmonic when it is globally defined; for complex \(a\), its differential remains a globally defined real closed one-form despite an additive period. The two complex charges are
\[
Q_1=d+dh\wedge,
\qquad Q_2=d^c-d^ch\wedge.
\]
Their physical adjoints give four real charges with
\[
\{R_i,R_j\}=2\delta_{ij}H,\qquad H\ge0.
\]
The construction includes an actual additional bosonic coordinate and fermion degrees of freedom. It changes the original Hamiltonian and evades the earlier fixed-spectrum obstruction. The [construction note](notes/01_EXTENDED_THEORY_CONSTRUCTION.md) specifies the common core, cutoff argument for self-adjointness, Hamiltonian, action and vacuum equations.

The original scalar state \(e^{-h}\) is not normalizable on the cylinder: it grows in part of the angular direction. The physical vacuum is instead a one-form. The noncompact Morse theorem, followed by an explicit Fredholm continuation argument, establishes that there is exactly one such vacuum for nonzero \(a\). Its norm has not been evaluated in the arithmetic source frame. Moreover, this concrete real one-vacuum Hamiltonian has locally flat ordinary Berry connection. Extra periodic/flavor data or a different insertion are needed for nontrivial arithmetic geometry.[^morse]

The gamma function survives as the convergent holomorphic period
\[
\int_{\mathbb R}e^{-2\mathcal W_a(Y)}dY=\Gamma(a),\qquad \Re a>0.
\]
For complex parameters this real path is a convergent relative cycle, not generally a steepest-descent thimble. A holomorphic period and the positive Hermitian norm of the physical one-form vacuum are distinct quantities.

Add two complex fields \(U,V\), put \(M=1-q\), and take
\[
\mathcal W_{a,q}
=\frac12\left[e^Y-aY+\frac M2(U^2+V^2)\right].
\]
This is a four-supercharge theory on the cylinder times \(\mathbb C^2\). Its normalized real-cycle period is \(\Gamma(a)/(1-q)\). At \(a=z/2\), \(q=p^{-z}\), the specified \(\pi^{-z/2}\) source factor gives the complete gamma–one-prime local product.

There is also a physical metric statement. For one quadratic field, an explicit middle-degree Gaussian vacuum has squared norm \(2\pi/|M|\). In a normalized intrinsic holomorphic frame its metric is \(|M|^{-1}\); two fields give \(|M|^{-2}=|1-q|^{-2}\). This is an actual vacuum norm, not only a period. Its logarithmic curvature vanishes away from \(M=0\), and a holomorphic frame change can remove the scalar factor there. The chosen source frame is therefore part of the arithmetic data.

## A real interaction can preserve the Euler factor

Consider the interacting two-field potential
\[
F_{M,g}(U,V)
=\frac M2(U^2+V^2)
+\frac g4(U^4+V^4)+\frac g4U^2V^2.
\]
For \(g>0\), \(M\ne0\), it has nine isolated nondegenerate complex critical points. Its gradient grows cubically at infinity, while its Hessian grows quadratically. The strongly tame Kähler framework therefore supplies a nine-dimensional physical vacuum space concentrated in middle degree, with an ordinary positive metric.[^hodge]

This is a genuine interacting model, but keeping \(g\) fixed fails an exact arithmetic test. Every identity period \(I(M)\) on a flat rapid-decay cycle satisfies
\[
6g^2 I'''-7gM I''+(2M^2-7g)I'+2MI=0.
\]
The result follows from integration by parts and remains valid for arbitrary constant complex combinations of such cycles. Substituting the desired Euler period \(I=1/M\) gives
\[
-\frac{g(7M^2+36g)}{M^4},
\]
which cannot vanish on an open parameter region. This excludes more than the simplest real contour. Fixed quartic confinement removes the Gaussian Euler pole at \(M=0\).

There is, however, an exact interacting escape. Fix \(c>0\) and let the quartic coupling scale as \(g=cM^2\). Then
\[
F_M(U,V)=G_c(\sqrt M\,U,\sqrt M\,V),
\]
where
\[
G_c(A,B)=\tfrac12(A^2+B^2)+\tfrac c4(A^4+B^4+A^2B^2).
\]
On the correspondingly transported cycle,
\[
I(M)=\frac{C_c}{M}.
\]
The constant \(C_c\) is a finite positive reference integral. This equality is a change-of-variables identity; it does not fit a sequence of numerical values.

The physical metric can also be computed in its dependence on \(M\). Let \(\alpha_c\) be the harmonic representative of the identity holomorphic volume class at \(M=1\). Pullback by \(\phi_M(U,V)=\sqrt M(U,V)\) preserves middle-degree two-form \(L^2\) norms in four real dimensions. The identity-class representative at \(M\) is
\[
\alpha_M=M^{-1}\phi_M^*\alpha_c,
\qquad
\|\alpha_M\|^2=\frac{H_c}{|M|^2},\quad H_c=\|\alpha_c\|^2>0.
\]
A fixed reference normalization therefore gives the exact physical Euler metric \(|1-q|^{-2}\) in an interacting theory. The constants \(H_c\) and \(|C_c|^2\) have not been identified with one another. A single source rescaling cannot be claimed to normalize both independently.

The limitation is equally precise. The mass deformation satisfies
\[
\partial_M F_M
=\frac{U\partial_UF_M+V\partial_VF_M}{2M}.
\]
It is zero in the Jacobi ring, so its projected chiral operator vanishes. The model retains the Euler factor through field dilation and degeneration at \(M=0\), without generating a new chiral-curvature constraint along the prime mass. The [quartic period note](notes/05_QUARTIC_PERIOD_TEST.md) derives both the exclusion and this escape.

This directly answers the question about Gaussianity: non-Gaussian positive theories can carry the exact prime factor. What remains necessary is an interaction or boundary mechanism that changes the relevant geometry and pairing, rather than only changing the reference theory being dilated.

## Which apparent repairs are now excluded

Several additional results constrain how the physical models can be joined to the target.

**A simple gamma–prime mass coupling fails.** Replacing \(M\) by \(M+\lambda e^Y\) changes the period to
\[
\int_0^\infty\frac{t^{a-1}e^{-t}}{M+\lambda t}\,dt.
\]
It is strictly different from \(\Gamma(a)/M\) on the positive real parameter locus. In the full complex field space it also develops a noncompact critical quadric when the mass vanishes. This excludes the proposed isolated-vacuum control, rather than proving a general theorem about every coupled theory's quantum gap.

**Finite holomorphic vacuum enlargement is too restrictive.** For physical vacuum vectors holomorphic in one fixed ambient Hilbert space, the trace of their curvature is a nonnegative squared second fundamental form. Ordinary finite-rank chiral \(tt^*\) requires this trace to vanish. Consequently the vacuum subspace must be constant; finitely many such vectors cannot contain the full Morse coherent family. Physical vacua with nonholomorphic dependence outside their projected holomorphic bundle remain possible.

**Non-Abelian metric compatibility itself is possible.** An explicit positive semisimple rank-two \(tt^*\) solution can reproduce \(\Lambda_S(\sigma)\) on the real axis by changing its complex extension. This does not construct the original state family, observable \(X\), or transition amplitude. In fact many unrelated positive real-analytic norms admit the same local construction. The [matrix-metric note](notes/02_NONABELIAN_METRIC_TEST.md) separates these possibilities from the precise excluded extensions.

**Scalar ground transforms have the wrong signs.** The full continuous off-diagonal kernel is
\[
R(r)=2\cosh(r/2)-\frac{e^{-r/2}}{1-e^{-2r}}
=e^{-r/2}\frac{e^{3r}-e^r-1}{e^{2r}-1}.
\]
It becomes positive at separations larger than \(\log\rho\), where \(\rho^3-\rho-1=0\). Positive scalar reversible jump/diffusion energies have nonpositive cross terms between disjoint nonnegative inputs. Their ground transforms therefore cannot equal the full target on intervals longer than \(\log\rho\), with the stated pointwise source identification. For lengths above \(2\log\rho<\log2\), a triangle of signs also defeats any scalar phase gauge. These restrictions already occur before the first prime and leave matrix, fermionic and nonlocal mechanisms open.

The poles themselves admit a positive coherent edge square, but that square has a compulsory extra diagonal. Together with the arithmetic contact, removing it requires an infinite-dimensional constraint, not just two extra pole states. Writing a Schur complement that is positive only if the unknown Weil form is positive does not resolve this. The complete algebra is in [the ground-transform note](notes/03_GROUND_TRANSFORM_AND_CONTACT.md).

**Changing parameter type does not fix normalization by itself.** An explicit Abelian Bogomolny solution extends the old arithmetic Berry connection to a three-dimensional parameter half-space. It works for arbitrary suitable holomorphic functions, and a flat gauge change shifts the arithmetic contact while leaving curvature unchanged. This proves compatibility of a necessary equation, not a microscopic vector-multiplet realization. See [the vector-parameter note](notes/04_VECTOR_PARAMETER_GEOMETRY.md). The chiral/vector distinction is established in the supersymmetric Berry literature.[^berry]

## Continued calculation: the interacting shape has a three-state physical sector

Set
\[
s=A^2+B^2,\qquad t=A^2B^2,\qquad
f_c=G_c/4=s/8+c(A^4+B^4+A^2B^2)/16.
\]
The factor one quarter fixes the physical convention: the differential is \(D=\bar\partial+\partial f_c\wedge\). It follows from the four-charge construction with \(\mathcal W=G_c/2\); a variation of \(\mathcal W\) alone would give a Higgs matrix twice the canonical one.

The coordinate sign changes and exchange preserve the physical Hamiltonian. The identity holomorphic volume belongs to a three-dimensional symmetry sector with polynomial representatives \(1,s,t\). Its exact algebra is
\[
s^2=-s/c+t,\qquad st=-4t/(3c),\qquad t^2=4t/(9c^2).
\]
The canonical shape insertion is \(C_c=-s/(16c)\). It is nonzero and the identity is cyclic, so all three states are necessary to close under the interaction insertion. This is a symmetry block of the original nine-state theory, not a change in its vacuum count.

In the specified holomorphic source frame \(E=(1,cs,c^2t)dA\wedge dB\), put \(u=1/c\). The Higgs matrix becomes the constant
\[
C_u=\frac{R}{16},\qquad
R=\begin{pmatrix}0&0&0\\1&-1&0\\0&1&-4/3\end{pmatrix}.
\]
An exact fermion phase symmetry makes the physical metric in this frame radial in \(u\). Writing \(\rho=|u|\), its necessary \(tt^*\) equation is
\[
\bigl(g^{-1}g'\bigr)'+\rho^{-1}g^{-1}g'
=\frac1{64}[R,g^{-1}R^Tg].
\]
The source frame, residue pairing and physical reality condition are spelled out in [note 06](notes/06_SHAPE_DEFORMATION_GEOMETRY.md). They matter: the matrix equation and residue algebra alone admit a constant positive solution, so a nonzero shape insertion by itself does not prove that the physical metric is nonconstant.

There is now a physical way to exclude that constant control. At large positive \(c\), rescaling the fields by \(c^{1/4}\) leaves a fixed pure quartic plus a quadratic term of size \(c^{-1/2}\). The limiting critical point is degenerate but isolated. The non-Morse Hodge comparison theorem of Li–Wen applies, and direct uniform confining estimates and source-continuity arguments keep the nine-dimensional physical kernel and the chosen polynomial sources well defined through the collision.[^nonmorse]

The rotation symmetry of the pure quartic makes the limiting three-source Gram matrix diagonal. Consequently
\[
g(\rho)=D_\rho\,[\operatorname{diag}(a_0,a_2,a_4)+o(1)]\,D_\rho,
\qquad D_\rho=\operatorname{diag}(\sqrt\rho,1,\rho^{-1/2}),
\quad a_0,a_2,a_4>0,
\]
as \(\rho\downarrow0\). In particular the identity norm obeys \(H(c,c)\sim a_0/c\). These powers come from the physical theory and its fixed sources. No norm was fitted to an arbitrary solution of the matrix equation. At that stage the constants, the other endpoint and global selection remained undetermined. Notes 10–13 below calibrate the residue constant, derive the opposite limit and prove metric selection; they do not evaluate every metric entry. The formula remains a rescaled matrix limit and does not assert that all unscaled off-diagonal entries vanish.

## An exact obstruction to scalar preservation of both Euler factors

The physical identity norm \(H(c,\bar c)\) is radial in the complex shape parameter. In contrast, the real-cycle period
\[
C_{\rm per}(c)=\frac1{2\pi}\int_{\mathbb R^2}e^{-G_c}\,dA\,dB,
\qquad \Re c>0,
\]
is holomorphic, strictly decreasing on the positive real axis and tends to one as \(c\downarrow0\). These facts prove that
\[
\mathcal R(c,\bar c)=\frac{H(c,\bar c)}{|C_{\rm per}(c)|^2}
\]
cannot be constant on any complex-open region. If it were constant, radiality would force the holomorphic period locally, and then throughout the right half-plane, to be a monomial. Its finite nonzero limit at zero would force it to be constant, contradicting strict decrease. The proof does not require evaluation of the physical norm.

For a nonconstant holomorphic shape \(c(M)\), suppose a common scalar source adjustment \(r(M)\) preserved both \(A/M\) as the identity period and \(B/|M|^2\) as its physical metric, with fixed \(A\ne0\), \(B>0\). Cancelling the common source factor would make \(\mathcal R(c(M))=B/|A|^2\), contrary to the open mapping theorem and the preceding result. Thus this specific scalar repair fails. The conclusion assumes the identity source, transported real cycle, flat target metric and stated physical differential. It leaves physical state mixing, different boundary conditions or cycles, additional fields and a different full pairing open. It does not establish monotonicity of the ratio on the positive real axis.

[Note 07](notes/07_PHYSICAL_PAIRING_TEST.md) gives the physical symmetry and obstruction. [Note 09](notes/09_SHAPE_PERIOD_AND_NORMALIZATION.md) independently derives the exact shape-period equation
\[
48c^4C^{(3)}+(288c^3+28c^2)C''
 +(324c^2+56c+4)C'+(36c+7)C=0.
\]
Its local asymptotic coefficients are checked against independent Gaussian moments. This checks the period calculation; it does not replace the positive-Hilbert-space argument.

## Requirements identified before constructing the caps

A holomorphic period does not automatically define a covector on the physical Jacobi-state space. Once an actual physical boundary functional \(\ell(v)=pv\) on a positive state metric \(G\) is supplied, its Riesz representative gives the exact decomposition
\[
\|v\|^2=\frac{|\ell(v)|^2}{pG^{-1}p^\dagger}
+\|v_\perp\|^2.
\]
A period sees only one component of a state. Both the boundary normalization and the unseen orthogonal component must be controlled before its square can determine the full norm. Several physically constructed boundary functionals give a corresponding positive Gram-matrix formula. An arbitrary list of holomorphic periods does not yet supply those functionals.

There is also a stronger source-space requirement than simply increasing the number of vacua. For a fixed smooth compactly supported function \(\phi\), modulation gives
\[
f_N(x)=e^{iNx}\phi(x),\qquad
Q_L[f_N]=\|\phi\|_2^2\log N+O(1).
\]
The gamma kinetic multiplier produces this unbounded high-frequency growth; the other terms are bounded at fixed support. Any source of the form \(Af=\int f(x)b_x\,dx\), with \(\int\|b_x\|^2dx<\infty\), is bounded on \(L^2(I_L)\) and cannot reproduce it, even if the target Hilbert space is infinite dimensional. A complete construction therefore needs an unbounded or distributional source, an energy insertion, or a controlled singular boundary limit, with its domain specified.

[Note 08](notes/08_BOUNDARY_SOURCE_REQUIREMENTS.md) derives these requirements and a possible operator route. An independently self-adjoint bulk Hamiltonian and actual boundary coupling produce a positive resolvent Gram kernel. That construction applies to interacting Hamiltonians. Its positivity is automatic, but identifying its arithmetic source and singular limit, including the contact and poles, remains a research problem. Restricting the resolvent to finitely many vacua, or keeping every boundary source uniformly bounded, cannot supply the full target.

## New physical boundary construction and normalization

[Note 10](notes/10_REFLECTED_BOUNDARY_PAIRING.md) specifies a compact wavefunctional \(u_{p,f}=T_{\chi,f}(p\Omega)\) using an explicit Koszul–Dolbeault homotopy. The prepared state is \(h_f(p)=\lim_{t\to\infty}e^{-tH_f}u_{p,f}\). Exact polynomial classes prepare zero states, so the source descends to the physical Jacobi sector by construction. This is a cohomological cap, with an ordinary Euclidean Hilbert adjoint; no geometric brane or period interpretation is assumed.

The unitary fermion operation \(U=(-1)^{\deg_{\rm hol}}\) changes \(f\) to \(-f\). Hodge-star conjugation reflects the opposite-twist state back into the original Hilbert space. On middle-degree vacua the resulting \(\Theta=*\overline{U(\,\cdot\,)}\) is an antiunitary involution. Gluing gives
\[
\ell_p(q)=\langle\Theta h_f(p),h_f(q)\rangle
=\int h_f(q)\wedge h_{-f}(p)
=4\pi^2\operatorname{Res}_f(pq).
\]
The factor is fixed by an exact local Gaussian and compact-cutoff calculation in the raw Euclidean volume normalization, including its two-form sign.

Thus the three boundary covectors and their positive Gram matrix are
\[
P=4\pi^2\eta_E,\qquad
b_i=\Theta h_f(E_i),\qquad
\mathcal B=PG^{-1}P^\dagger=G^T>0.
\]
This is an actual preparation and gluing law. It characterizes the global Gram matrix without pretending to evaluate \(G(c,\bar c)\). In particular \(\|b_i\|^2=G_{ii}\). It also supplies a sharp example of the missing orthogonal component: \(\ell_1(1)=0\) despite \(H(c,\bar c)>0\), whereas the top-source cap has \(\ell_{c^2t}(1)=256\pi^2/3\).

The original raw period rule fails to descend even in the invariant sector. The zero Jacobi class \(A\partial_Af+B\partial_Bf\) has real-plane exponential integral \(C_{\rm per}/2\), by integration by parts. The physical caps therefore cannot be identified with that insertion rule merely by selecting polynomial representatives.

At the pure quartic, degree symmetry diagonalizes the source metric. With \(\lambda=256\pi^2/3\), the calibrated gluing now gives
\[
G_0=\operatorname{diag}(a_0,\lambda,\lambda^2/a_0).
\]
The middle-source norm is exactly evaluated; only \(a_0\) remains unevaluated. One consequence is a completely normalized interacting control: for
\[
f_M=\frac{M^2}{16}(U^4+V^4+U^2V^2),\qquad
\sigma_M=\frac{\sqrt3\,M}{16\pi}(U^2+V^2)\,dU\wedge dV,
\]
the cap prepares a state of norm squared \(|M|^{-2}\). This changes the original identity source and uses the isolated homogeneous quartic. It has a known normalization, but its mass class is still Jacobi-trivial and it is not the complete arithmetic form.

## The escaping vacua and physical metric selection

[Note 12](notes/12_MASSIVE_ENDPOINT.md) resolves the formerly open positive-real \(c\downarrow0\) limit. Rescaling gives nine fixed critical points for \(\rho f_1\), \(\rho=1/c\). Local holomorphic quadratic coordinates yield exact closed Gaussian representatives with the correct cohomology source normalization. Compact cutoff representatives give upper metric bounds; their exact opposite-twist pairings give matching lower bounds by Hilbert duality. This proves the endpoint without assuming an eigenvector-localization formula:
\[
G_{\rm orb}(c,c)=4\pi^2\operatorname{diag}(16,64,48)+O(c^{1/2}).
\]
In particular \(H(c,c)\to512\pi^2\). Setting \(c=0\) first gives the different single-Gaussian norm \(64\pi^2\). The eight escaping vacua retain seven additional Gaussian units in this fixed source; their contribution cannot be discarded.

The metric boundary data are now sufficient for uniqueness. [Note 13](notes/13_RADIAL_METRIC_SELECTION.md) derives
\[
\partial_{\bar u}\partial_u
\left[\operatorname{tr}(G_1^{-1}G_2)+
\operatorname{tr}(G_2^{-1}G_1)-6\right]\ge0
\]
for two positive solutions of the same \(tt^*\) equation. The calibrated strong endpoint makes this nonnegative trace distance bounded at zero, even if the proposed constants \(a_0\) differ. The common massive endpoint makes it tend to zero at infinity. The maximum principle forces the metrics to agree. No derivative endpoint expansion or numerical shooting is used.

The physical Hodge family supplies a globally defined metric for \(c\ne0\). Its identification with the unique equation solution uses the exact chiral \(tt^*\) framework already invoked in note 06; the comparison proof is independent of that framework. The residual constant is therefore fixed by the physical problem, although neither its value nor the Stokes matrices have been computed. This is metric selection, not an arithmetic observable identity.

## A closed source for the gamma kinetic term

[Note 11](notes/11_CLOSED_ARITHMETIC_SOURCE.md) turns the earlier source requirement into an explicit construction. For \(H=-\partial_x^2\), \(a_k=2k+1/2\), \(R_k=(a_k^2+H)^{-1}\), the positive local auxiliary energy prepares the residual source
\[
(\mathcal A F)_k=
\begin{pmatrix}
\sqrt{2/a_k}\,H R_kF\\
\sqrt{2a_k}\,\partial_xR_kF
\end{pmatrix},
\qquad
\|\mathcal A F\|^2=K[F].
\]
After zero extension, its maximal closed domain is
\[
\mathcal D_{\log,L}=
\left\{f\in L^2(I_L):
\int \log(2+|\tau|)\,|\widehat{E_Lf}(\tau)|^2\,d\tau<\infty\right\}.
\]
The note proves that compactly supported smooth functions are a core and derives the interval adjoint by distributional restriction. It distinguishes the form domain from the associated operator domain.

Truncating the tower gives operator norms squared exactly
\(\psi(N+1/4)-\psi(1/4)\sim\log N\). A heat regulator gives normalizable point-source vectors before its singular limit. Both converge to the same closed preparation exactly on the displayed domain, with strong-resolvent convergence for the induced operators.

Every other arithmetic term stays explicit:
\[
Q_L[f]=\|\mathcal A_Lf\|^2+\langle f,\mathcal R_L f\rangle,
\]
\[
\mathcal R_L=w_0I+2|c_L\rangle\langle c_L|-2|s_L\rangle\langle s_L|
-\sum_{m\log p<L}(\log p)p^{-m/2}(T_{m\log p}+T_{m\log p}^*),
\]
where \(c_L(x)=\cosh(x/2)\), \(s_L(x)=\sinh(x/2)\), and \(w_0=\psi(1/4)-\log\pi\). This is a closed semibounded realization of the full form, with its exact normalization and support compatibility. It is not a positive factorization of the signed remainder.

A further exclusion closes a possible finite-vacuum loophole: every densely defined closable map from \(L^2(I_L)\) into a finite-dimensional state space is bounded. Thus even a purported distributional preparation confined to finitely many vacua cannot realize the required logarithmic growth. Finite boundary channels coupled to infinitely many excited states remain possible.

## Exact pole gluing and its stability test

[Note 14](notes/14_POLE_BOUNDARY_GLUING.md) changes only the lowest massive field's endpoint condition. At \(a=1/2\), the attractive Robin operator
\[
A_{\rm R}=-\partial_x^2+\tfrac14,\qquad
u'(\pm L/2)=\pm\tfrac12u(\pm L/2)
\]
has the exact inverse
\[
A_{\rm R}^{-1}(x,y)=-e^{|x-y|/2}
=e^{-|x-y|/2}-2\cosh((x-y)/2).
\]
Consequently \(K_{0,L}+P_L=4I-A_{\rm R}^{-1}\): both pole signs are absorbed into one local boundary response.

The response is a saddle. Its auxiliary action has exactly one negative even mode for every \(L\). The reduced lowest pairing is strictly positive for \(L<4\), has kernel \(\operatorname{span}\{x\}\) at \(L=4\), and has one negative odd direction for \(L>4\). A specified spectral projection gives a positive source with an exact rank-one residual above that threshold. The projection is not yet a local physical constraint. Supersymmetric factorization requires an energy shift and changes infinitely many response coefficients. These are statements about the lowest gamma-plus-pole pairing, not a sign test for the complete Weil form.

[Note 15](notes/15_COHERENT_DELAY_DEFECT.md) obtains the signed poles inside an ordinary positive norm without that unstable auxiliary action. Tensor the gamma residual output with the physically normalized homogeneous cap \(\chi\), and in its lowest two-component mode inject
\[
\mathcal B_DF=-\frac{e^{D/2}}2
\begin{pmatrix}(U_D+U_{-D})F\\ (U_D-U_{-D})F\end{pmatrix}\otimes\chi,
\qquad D\ge L.
\]
The two output components cancel the double-delay terms in the defect's norm. Their cross term with the original massive field gives exactly \(2\cosh((x-y)/2)\) inside the interval. Hence
\[
\|\mathcal A_0f\|^2=K_L[f]+P_L[f]+e^D\|f\|^2,
\qquad
\mathcal A_0=(\mathcal A_\gamma\otimes\chi+\mathcal B_D)E_L.
\]
The positive contact \(e^D\) is optimal within this two-shift ansatz. More generally, preserving the continuous gamma and pole kernels with a finite alphabet of raw delays forces the additional contact to be nonnegative, even with square-summably many massive channels. The proof uses uniqueness of a convergent Laurent series between delay centers. It does not apply to filtered or resolvent source corrections.

## Conservative prime returns and their compulsory contact

[Note 16](notes/16_PRIME_RETURN_CHANNELS.md) specifies a nonnegative quantum-graph Laplacian with two external leads, a Neumann stub of length \(d/2\), and an explicit real orthogonal vertex coupler. One observed outgoing lead produces the coherent source
\[
\mathcal D_pF=
\sqrt{\frac{dq(1+q)}{1-q}}\,
(I-U_d)(I-qU_d)^{-1}F\otimes\chi,
\quad d=\log p,\quad q=p^{-1/2}.
\]
Its exact gluing is
\[
\mathcal D_p^*\mathcal D_p
=c_pI-d\sum_{m\ge1}q^m(U_d^m+U_d^{*m}),
\qquad c_p=\frac{2dq}{1-q}.
\]
Every prime repetition arises from one conservative return channel with infinitely many accessible continuum states. The input scale is prescribed explicitly; the quartic cap alone does not force the arithmetic factor \(d\).

A whole-line stationary prime Gram operator with exactly these off-diagonal coefficients is positive only if its scalar contact is at least \(\sum_p c_p\). The displayed channels attain this bound, which permits arbitrary coherent mixing of outputs. A single finite-support compression can have a smaller sharp contact; such support-dependent choices do not yield a compatible all-length source. The unrenormalized all-prime graph norm still diverges on every nonzero compactly supported input.

The graph's output norm and its scattering-phase derivative are separately computed. The Euler logarithmic derivative is a signed relative response with zero contact; it is not automatically the positive norm of the same graph output. Coherence realizes the exact returns but does not by itself remove their compulsory diagonal.

## A collective feedback source isolates the remaining operator

[Note 17](notes/17_COLLECTIVE_FEEDBACK_AND_COMPACT_DEFECT.md) changes the raw-delay hypothesis through a collective response. The already specified positive source \(\mathcal A_0\) gives
\[
T_0=\mathcal A_0^*\mathcal A_0=T_L+P_L+e^DI
\ge \bigl(e^D+L-2\sinh(L/2)\bigr)I>0.
\]
It has compact resolvent. A boundary field with positive Hessian \(T_0+\mu\), \(\mu\ge0\), responds to external input \(f\) by
\[
w_f=(T_0+\mu)^{-1}f.
\]
The ordinary positive readout is \(\mathcal A_0(f-\kappa w_f)\), coherently joined to the finitely many prime channels covering every prime active on \(I_L\). Choose the gain after deriving the response:
\[
2\kappa=e^D+\sum_{p\in\mathcal S}c_p-w_0.
\]
The closed source and its exact polarized pairing are
\[
\Gamma_Lf=
\mathcal A_0\bigl(I-\kappa(T_0+\mu)^{-1}\bigr)f
\oplus(\mathcal D_pE_Lf)_{p\in\mathcal S},
\]
\[
\boxed{\quad
\langle\Gamma_Lf,\Gamma_Lg\rangle
=Q_L(f,g)+\langle f,C_{\kappa,\mu}g\rangle,
\quad}
\]
\[
C_{\kappa,\mu}
=2\kappa\mu(T_0+\mu)^{-1}
+\kappa^2T_0(T_0+\mu)^{-2}>0.
\]
The common source domain is exactly \(\mathcal D_{\log,L}\); the note specifies the maximal adjoint and proves closure by bounded perturbation. The only inverse used is that of the independently positive reference \(T_0+\mu\), not the unknown target.

The residual is compact, of infinite rank, and nonzero on every nonzero input. Sending \(\mu\) to zero leaves \(\kappa^2T_0^{-1}\). For any fixed positive reference eigenvalue, its minimum over all \(\mu\ge0\) is strictly positive. Thus parameter tuning cannot finish this readout. Nor is the completed norm asserted to be compatible across supports: the interval response and selected prime set remain part of its data.

The coupling gains match arithmetic coefficients but are not derived as an arithmetic law of the bulk. The feedback identity is a general positive-completion mechanism. Treating its residual as zero, or subtracting it while retaining the claim of a physical norm, would undo the construction's exact accounting.

## A regularity restriction on further coherent repairs

Note 17 also excludes a Hilbert–Schmidt coherent correction \(B\) to the already unbounded gamma source. On an orthonormal family of exponential inputs supported in an interval shorter than \(\log2\), every prime overlap vanishes, the pole pairing is \(O(n^{-2})\), and the gamma energy is \(O(\log n)\). Matching the negative contact would require
\[
\|Bf_n\|^2\ge \frac{c}{\log(n+2)}
\]
for a positive constant \(c\), contradicting Hilbert–Schmidt summability. The same proof applies to the assembled pole-and-prime reference and extends to every finite Schatten class.

The collective correction \(-\kappa\mathcal A_0(T_0+\mu)^{-1}\) is compact but outside every such class. A variational comparison with Dirichlet auxiliary fields bounds the reference eigenvalues by \(O(\log n)\), proving its slow singular-value decay directly. Thus this feedback changes the regularity hypothesis in a controlled way, while still leaving the explicit residual above.

## Joint response and the finite-rank continuation

[Note 18](notes/18_REVIEW_AND_NEUMANN_COMPARISON.md) complements the previous Dirichlet upper bound by dropping the nonnegative exterior auxiliary energy. This proves
\[
b(H_{\rm N})\le T_L\le b(H_{\rm D}),\qquad
\lambda_n(T_L)=\log\frac{\pi n}{2L}-\psi(\tfrac14)+O_L(n^{-1}).
\]
The lower comparison and an explicit bound on the active prime chains select a finite Neumann cosine projection \(P_N\) whose complement \(Q_N\) has \(W_L|_{Q_NX}\ge\delta I>0\). At \(L=1\), elementary rational bounds prove that \(N=4,\delta=1/16\) works. This is a high-sector bound, not a new full-form positivity certificate.

Use the whole positive source \(A=\mathcal A_0\oplus\mathcal J_{\mathcal S}\), with
\[
T=A^*A=W_L+\alpha I,\qquad
\alpha=e^D+c_{\mathcal S}-w_0=2\kappa.
\]
With \(T_H=(A|_{Q_NX})^*(A|_{Q_NX})\), \(H=T_H-\alpha I\ge\delta I\) and \(B=Q_NTP_N\), repeated stable responses give the norm-convergent binomial factor
\[
R=I-\sum_{j\ge1}\frac{\binom{2j}{j}}{4^j(2j-1)}
       \alpha^jT_H^{-j},\qquad RT_HR=H.
\]
Its use is justified by the independently proved high-sector gap; positivity of the full target is not assumed. The response is genuinely joint: its ordered resolvent expansion retains all compressed prime/gamma words.

Let \(Z=(I-\Pi_H)A|_{P_NX}\) keep the original low-source component orthogonal to the range of \(A|_{Q_NX}\). The completed source is
\[
\Phi_Lf=A_HR(Q_Nf+H^{-1}BP_Nf)+ZP_Nf.
\]
It is closed on the same logarithmic domain and satisfies
\[
\boxed{\quad
\|\Phi_Lf\|^2=Q_L[f]+\langle P_Nf,D_NP_Nf\rangle,\qquad
D_N=\alpha I+B^*(H^{-1}-T_H^{-1})B>0.
\quad}
\]
The error has rank exactly \(N\). The coherent source correction remains compact but outside every finite Schatten class, so this does not contradict the previous regularity exclusion.

The finite Gram \(G=Z^*Z>0\) is independently supplied by the original positive source. The exact remaining condition is
\[
Q_L\ge0\quad\Longleftrightarrow\quad G-D_N\ge0.
\]
No sign of this difference is assumed. The new exact checker includes a positive rational reference with a negative target direction for which the same completion identity holds, making its limitation explicit.

## What should be investigated next

Pursue missing lemma B in [note 20](notes/20_ARITHMETIC_SIGN_AND_BOUNDARY_RESPONSE.md): derive an analytical trial response and a signed arithmetic estimate that covers the full mixed residual. The new boundary columns expose the gamma coupling, and the discrepancy identity identifies information lost in a smooth-density comparison. Either a successful intermediate estimate or a rigorous counterexample to a specified stronger claim would be useful. Further iteration of the already controlled high-sector square root is not the outstanding problem.

A finite-support enclosure must retain all active primes, mass and mode tails, unused outputs and numerical errors. Such an enclosure would not by itself prove all-support positivity. An analytical proof for each length would suffice without a single compatible physical source system. The cap geometry and conditional chiral equation remain separate from the unproved arithmetic ordering; see [CONTINUATION.md](CONTINUATION.md).

## Verification and sources

The ten retained programs use only Python's standard library and reproduce fifty-nine labelled exact checks. The newest ten test Green-kernel and cosine-column algebra, inverse-tail counterexamples, full mixed residuals, reference-shift cancellation and rational bounds for the smooth-density obstruction. The previous forty-nine records are unchanged. These checks do not certify the analytical domain, Hodge, endpoint or convergence arguments. Earlier passes recorded subtask cross-review of notes 10–17; the present continuation received single-agent internal review and exact algebra checks. No external specialist validation, full Weil positivity or RH result is claimed.

[^morse]: Xianzhe Dai and Junrong Yan, [Witten deformation for noncompact manifolds with bounded geometry](https://arxiv.org/abs/2005.04607), 2020. The note checks well tameness, then uses the Morse-inequality index at large deformation and a separate Fredholm continuation argument.
[^hodge]: Huijun Fan, [Schrödinger equations, deformation theory and \(tt^*\)-geometry](https://arxiv.org/abs/1107.1290), 2011. The strongly tame Kähler–Stein Hodge result supplies the middle-degree vacuum/Jacobi identification; the polynomial and dilation calculations are performed in this package.
[^berry]: Julian Sonner and David Tong, [Berry Phase and Supersymmetry](https://arxiv.org/abs/0810.1280), 2008/2009. The explicit comparison and compatibility constructions are derived in the notes.

[^nonmorse]: Si Li and Hao Wen, [On the L2-Hodge theory of Landau-Ginzburg models](https://arxiv.org/abs/1903.02713), *Advances in Mathematics* 396 (2022), 108165. Their Hodge decomposition and comparison theorem allow the isolated degenerate critical point. The uniform family estimates, source continuity and endpoint scaling here are deductions for the specified quartic.
