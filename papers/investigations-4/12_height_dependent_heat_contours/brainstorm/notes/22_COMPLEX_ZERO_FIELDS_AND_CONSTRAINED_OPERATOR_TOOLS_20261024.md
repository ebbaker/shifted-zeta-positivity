# Complex zero fields and the constrained-operator source tools

24 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance, **gpt-6-astra (Codex), actual recorded reasoning effort max**. Same-assistant derivation, source review and symbolic verification; no independent specialist review or priority claim.

## Status and purpose

The author proposes making a complex field primary, with **total normalization** \(\int|\psi|^2\,dA=1\), a density interpretation, and a gradient related to zero velocity. He also asks whether the growing concentration of zeros prevents normalization, whether a moving boundary remains necessary, and whether the three earlier operator manuscripts supply useful tools.

There is an exact realization of much of this proposal. A smooth complex amplitude has the manuscript's existing regularized zero density as its squared modulus. Its phase derivatives recover simple-zero velocity. It satisfies an exact Schrödinger-type equation coupled to a real potential; after rotation and rescaling this is the focusing Davey–Stewartson II differential system. A smoothed density-square observable detects multiplicity after its self-contribution is subtracted.

**Classification:** an exact change of variables and observable identity, useful for choosing a research formulation. This is neither a new arithmetic estimate nor progress on a simplicity proportion. The same identities hold for collision controls. The DS-II connection lies in established integrable-systems territory; the precise history of this particular formula has not been audited. The book, existing theorem statements and progress registers are unchanged.

Reading anchors: [established-result index](../../../../../result-summaries/README.md), especially [collision controls](../../../../../result-summaries/12_collision_controls_and_screening.md) and [local heat geometry](../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md); [patterns to avoid](../../../../../avoid/README.md), especially [restating the target](../../../../../avoid/01_restating_the_target.md), [shape-only arguments and controls](../../../../../avoid/02_shape_only_arguments_and_the_controls.md), and [unchecked imports/novelty](../../../../../avoid/16_unchecked_imports_and_novelty_claims.md).

## 1. Separate the field from a counting window

The older real \(\psi\) was a spatial test function selecting a counting region. The new complex \(\psi\) is a different mathematical object. Write the window as \(h\), the unnormalized complex amplitude as \(A_\epsilon\), and the normalized local state as \(\psi_\epsilon\). This avoids assigning both jobs to the same symbol.

Use the book's heat convention

\[
H_t=-H_{zz},\qquad z=x+iy,\qquad t\in\mathbb R,
\]

with \(H(t,\cdot)\) nonconstant and holomorphic and enough time regularity for the displayed derivatives. Spatial statements below are local unless global integrability is explicitly assumed. Fix a **constant** regulator \(\epsilon>0\), and set

\[
D=|H|^2+\epsilon^2,\qquad
\boxed{A_\epsilon=\frac{\epsilon}{\sqrt\pi}\frac{H_z}{D}.}
\tag{1}
\]

Then

\[
\mu_\epsilon=|A_\epsilon|^2
=\frac{\epsilon^2|H_z|^2}{\pi(|H|^2+\epsilon^2)^2}
=\frac1{4\pi}\Delta\log D.
\tag{2}
\]

This is exactly the density in [conserved_contours.tex](../../manuscript/conserved_contours.tex), equation `cc-scalar-current`, with its regulator \(\rho\) renamed \(\epsilon\). Equation (1) adds phase to that existing density, rather than proposing a new zero-counting measure.

At fixed positive \(\epsilon\), \(A_\epsilon\) is smooth at every zero of \(H\). It is nonzero at a simple zero and vanishes at a multiple zero. A multiple zero can therefore appear as a density ring surrounding a zero of the amplitude, not as a density maximum at its center. No singular wavefunction is required at the actual zeros.

Locally, as \(\epsilon\downarrow0\),

\[
\mu_\epsilon\,dA\ \rightharpoonup\
\sum_{H(a)=0}m_a\delta_a.
\tag{3}
\]

For the exact model \(H=c(z-a)^m\), direct radial integration gives

\[
\int_{|z-a|<R}\mu_\epsilon\,dA
=\frac{m|c|^2R^{2m}}{|c|^2R^{2m}+\epsilon^2}
\longrightarrow m.
\tag{4}
\]

For a general holomorphic function the same local mass follows from the local degree, or from (2) and the distributional limit of \(\log(|H|^2+\epsilon^2)\). This retains multiplicity. The limiting object in (3) is a measure; it is not the squared modulus of an ordinary limiting \(L^2\) function.

The regulator is measured in the **value of \(H\)**. Near a simple zero the spatial resolution is approximately \(\epsilon/|H_z(a)|\); near an order-\(m\) zero it is approximately \((\epsilon/|c|)^{1/m}\). A fixed regulator is not a fixed spatial resolution at increasing height. Replacing it by a space- or time-dependent regulator introduces additional derivative terms into the equations below.

## 2. The phase gradient gives zero velocity

At a simple zero \(a(t)\), differentiating \(H(t,a(t))=0\) gives

\[
\dot a=\frac{H_{zz}}{H_z}.
\tag{5}
\]

Where \(H_z\ne0\), choose a local phase \(\theta=\arg A_\epsilon=\arg H_z\). Holomorphicity gives

\[
\theta_x=\Im\frac{H_{zz}}{H_z},\qquad
\theta_y=\Re\frac{H_{zz}}{H_z}.
\]

Thus the real velocity vector is

\[
\boxed{\mathbf v=(\theta_y,\theta_x).}
\tag{6}
\]

The author's gradient suggestion is exact in this formulation, with the two derivatives exchanged. It is the phase gradient that determines transport; the gradient of the density alone does not determine a direction of motion.

Define the current everywhere by the smooth expression

\[
j_x=\Im(\overline A_\epsilon\,\partial_y A_\epsilon),\qquad
j_y=\Im(\overline A_\epsilon\,\partial_x A_\epsilon).
\tag{7}
\]

It agrees with

\[
j_x+ij_y
=\frac{\epsilon^2H_{zz}\overline{H_z}}{\pi D^2},\qquad
\mathbf j=\mu_\epsilon\mathbf v\quad(H_z\ne0),
\]

and satisfies

\[
\partial_t\mu_\epsilon+\nabla\cdot\mathbf j=0.
\tag{8}
\]

At a collision, individual zero velocities can diverge and a phase chart can fail, while the field and current remain smooth. This is the expected behavior of a regularized density/current representation, not a collision exclusion.

At an isolated order-\(m\) zero of \(H\), the local phase winding of \(A_\epsilon\) is \(m-1\). However, \(A_\epsilon\) also vanishes at critical points of \(H\) where \(H\ne0\). Phase winding alone is not a detector of zeros of \(H\); localization of the zero density, or the underlying analytic constraint, is also needed.

## 3. An exact field evolution

Set

\[
V_\epsilon=-2\partial_x\partial_y\log D\in\mathbb R.
\tag{9}
\]

Direct differentiation gives the exact coupled equations

\[
\boxed{\quad i\partial_t A_\epsilon
=-\partial_x\partial_y A_\epsilon+V_\epsilon A_\epsilon,
\qquad
\Delta V_\epsilon=-8\pi\partial_x\partial_y|A_\epsilon|^2.\quad}
\tag{10}
\]

For a short verification, put \(f=H\), \(p=H_z\), \(q=H_{zz}\). Then
\(D_x=p\bar f+f\bar p\), \(D_y=i(p\bar f-f\bar p)\),
\(D_t=-q\bar f-f\bar q\), and \(p_t=-H_{zzz}\). Inserting these into the first equation leaves zero. Equivalently,

\[
V_\epsilon
=4\Im\left(\frac{\bar H H_{zz}}D
-\left(\frac{\bar H H_z}D\right)^2\right),
\]

which makes its regularity at \(H_z=0\) and \(H=0\) explicit. The second equation follows by applying \(-2\partial_{xy}\) to (2). Taking the imaginary part of the first equation after multiplying by \(\bar A_\epsilon\) proves (8).

The kinetic operator is \(-\partial_{xy}\), not \(-\Delta\). It has symbol \(k_xk_y\) of both signs. Therefore a real potential and norm conservation do not provide a positive kinetic square or a lower energy bound of the kind needed in a positivity argument. Formal symmetry is also not a global selfadjointness theorem for an unbounded theta potential.

The pair (10) can be used as a field formulation once the potential's boundary/asymptotic data are supplied. Its elliptic equation alone determines \(V\) only up to a harmonic function. Moreover, a general solution of (10) need not arise from the canonical theta heat function through (1). Keeping the theta initial data and holomorphic/source compatibility is essential if this is used as a primary evolution.

### Identification with focusing Davey–Stewartson II

Let

\[
X=\frac{x+y}{\sqrt2},\quad Y=\frac{y-x}{\sqrt2},\quad t=2\tau,
\qquad q(\tau,X,Y)=2\sqrt\pi\,A_\epsilon(2\tau,x,y).
\]

Write \(V^\#(\tau,X,Y)=V_\epsilon(2\tau,x,y)\), and set
\(\Phi=V^\#-|q|^2\). Since
\(\partial_{xy}=\tfrac12(\partial_{XX}-\partial_{YY})\), (10) becomes

\[
i q_\tau+q_{XX}-q_{YY}-2(\Phi+|q|^2)q=0,
\qquad
\Delta\Phi+2\partial_{XX}|q|^2=0.
\tag{11}
\]

This matches equation (1) of [Klein–Stoilov, arXiv:1712.08814v1](https://arxiv.org/abs/1712.08814v1), page 1, in the checked convention. Only the differential-system identification is used; no finite-mass theorem or numerical blow-up conclusion is imported.

[Taimanov, arXiv:2111.07251v1](https://arxiv.org/abs/2111.07251v1), introduction and Section 4.1, supplies related prior art connecting two-dimensional Dirac operators, Moutard transformations, and holomorphic seeds satisfying \(f_t=i f_{zz}\). His equation (19) is a different explicit formula. It provides context, not a proof of (1) or a novelty claim about this construction. The [reference catalog](../../references/README.md) and [download receipt](../../references/REFERENCE_COMPLEX_ZERO_FIELD_RECEIPT_20261024.json) retain the checked scope and versioned reading copies.

## 4. Total normalization and the height problem

An equal-weight counting measure on infinitely many zeros has infinite total mass even at constant mean density. Increasing density with height makes a fixed observation scale more difficult, but it is not the fundamental obstruction to a global probability distribution. Unfolding to constant mean spacing does not make an infinite count finite.

This argument concerns the zero-counting measure. It does not by itself prove that the integral of (2) is infinite for the theta function at every fixed positive regulator. No global finite-norm result for that theta amplitude is established here. In particular, finite-\(L^2\) DS-II results cannot simply be applied.

A precise local version of the author's normalization is available. Take a fixed real, nonnegative \(h\in C_c^\infty(\mathbb C)\), with \(h=1\) on the desired finite height region, and define

\[
Z_\epsilon(t)=\int h^2|A_\epsilon|^2\,dA>0,\qquad
\boxed{\psi_\epsilon=\frac{hA_\epsilon}{\sqrt{Z_\epsilon(t)}}.}
\tag{12}
\]

Then \(\int|\psi_\epsilon|^2=1\). The probability density is \(|\psi_\epsilon|^2\); \(\psi_\epsilon\) is its complex amplitude. Retain \(Z_\epsilon\) alongside the normalized state so that absolute mass is available. Norm one alone cannot say how many zeros are represented. In a region where \(h>0\), the phase and velocity relation (6) are unchanged.

A fixed window eliminates any need to evolve a spatial wall, but it does not eliminate flux. Integration of (8) gives

\[
\dot Z_\epsilon=\int 2h\nabla h\cdot\mathbf j\,dA.
\tag{13}
\]

With \(\mathbf J=h^2\mathbf j/Z_\epsilon\), which is also the current computed from \(\psi_\epsilon\) by (7),

\[
\partial_t|\psi_\epsilon|^2+\nabla\cdot\mathbf J
=\frac{2h\nabla h\cdot\mathbf j}{Z_\epsilon}
-\frac{\dot Z_\epsilon}{Z_\epsilon}|\psi_\epsilon|^2.
\tag{14}
\]

The normalized state's equation is

\[
i\partial_t\psi_\epsilon
=-\partial_{xy}\psi_\epsilon+V_\epsilon\psi_\epsilon
+\frac{h_{xy}A_\epsilon+h_x(A_\epsilon)_y+h_y(A_\epsilon)_x}{\sqrt{Z_\epsilon}}
-i\frac{\dot Z_\epsilon}{2Z_\epsilon}\psi_\epsilon.
\tag{15}
\]

This form stays regular where \(h=0\). It explicitly retains localization and normalization corrections. Making the field primary means using (10), with (12) as the observation state; it does not require pretending the truncated state satisfies the unmodified global equation.

As a finite control, for any polynomial \(H\) of degree \(n\ge1\), the area formula for the proper map \(H:\mathbb C\to\mathbb C\) gives
\(\int_\mathbb C\mu_\epsilon\,dA=n\). Thus \(A_\epsilon/\sqrt n\) is globally normalized and remains so through collisions under degree-preserving polynomial heat flow. In particular \(H=z^2-2t\) gives a smooth globally normalized state with a double zero at \(t=0\). Normalizability and smooth evolution cannot exclude multiplicity.

## 5. The density-square tool gives a multiplicity observable

At a fixed time, take a **finite** selected divisor
\(\nu=\sum_a m_a\delta_a\), with distinct support points \(a\), and put \(N=\nu(\mathbb C)\). Let

\[
K_s(z)=\frac1{4\pi s}e^{-|z|^2/(4s)},\qquad
\nu_s=K_s*\nu,\qquad s>0.
\]

Using \(K_s*K_s=K_{2s}\), one obtains

\[
\boxed{
Q_s:=8\pi s\int\nu_s^2\,dA-N
=\sum_a m_a(m_a-1)
+\sum_{a\ne b}m_am_b e^{-|a-b|^2/(8s)}.
}
\tag{16}
\]

The second sum is over ordered pairs of distinct support points. Consequently

\[
\lim_{s\downarrow0}Q_s=\sum_a m_a(m_a-1).
\tag{17}
\]

The subtraction of \(N\) removes each individual zero's self-contribution, while retaining interactions between coincident zeros. This is the relevant analogue of normal ordering in the 2017 manuscript. It is an ordinary classical density identity here; no quantum field quantization is asserted.

For a probability density \(p_s=\nu_s/N\), the same observable is

\[
Q_s=8\pi sN^2\int p_s^2\,dA-N.
\]

If \(|\psi_s|^2=p_s\), it is a quartic observable of that amplitude. This \(\psi_s\) need not have the phase or exact evolution of (1); spatial smoothing and the value-plane regulator are distinct operations.

There is also a direct observable of the actual field (12):

\[
Q_{s,\epsilon}
=8\pi s\int\left[K_s*(Z_\epsilon|\psi_\epsilon|^2)\right]^2\,dA-Z_\epsilon.
\tag{18}
\]

Choose the finite cutoff with \(h=1\) near every selected zero and no zeros in its transition region at the time under consideration. First send \(\epsilon\downarrow0\) at fixed \(s\), and then \(s\downarrow0\); (18) tends to (17). For fixed \(s\), this follows from weak convergence of compactly supported finite measures and the continuous Gaussian pair kernel. A cutoff with fractional values at zeros instead gives weighted masses and does **not** give the integer multiplicity excess in (17). At fixed positive regulator, sending the spatial scale to zero first instead gives \(Q_{s,\epsilon}\to-Z_\epsilon\): the smooth density has no point masses. Thus (18) is not automatically nonnegative at finite regulator, and the order of limits is essential.

At finite scale the distinction is quantitative. One double zero contributes \(Q_s=2\) for every \(s\), whereas two distinct simple zeros separated by \(d>0\) contribute \(2e^{-d^2/(8s)}\), tending to zero only as the scale resolves the separation. In the heat control \(z^2-2t\), the value is \(2e^{-|t|/s}\). These limits are not uniform at a collision.

Equation (16) is an exact observable identity, not a newly proved upper bound. Applying it at increasing height requires control of close distinct pairs, regulator-to-divisor error, cutoff flux, and the relation between the two scales \(s\) and \(\epsilon\). A choice of field alone supplies none of those estimates.

## 6. What the three earlier manuscripts contribute

All three originals were read through as extracted text, and the relevant formulas were checked on rendered pages. The [14 October review](../../../../investigations-2/active/20_constrained_operator_squares/reviews/THREE_SOURCE_NOTES_REVIEW_20261014.md) and [residual-corrected trajectory note](../../../../investigations-2/active/20_constrained_operator_squares/notes/RESIDUAL_CORRECTED_HEAT_TRAJECTORY_IDENTITIES_20261014.md) were consulted alongside them. Their retained useful identities are distinct from their incomplete implementations.

| Source | Useful tool here | Restriction retained |
| --- | --- | --- |
| [Continuum_sigma.pdf](../../../../investigations-2/active/20_constrained_operator_squares/source_documents/Continuum_sigma.pdf), 22 November 2017, pages 3–4, equations (23)–(25) | Heat-semigroup factorization turns a pair kernel into a square of a smoothed density. This directly motivates (16), including the self-subtraction. | Heat smoothing is not multiplicative and cannot be one similarity transformation on the full multiplication algebra. The normal-order subtraction cannot be discarded. |
| [Heat_Quantum.pdf](../../../../investigations-2/active/20_constrained_operator_squares/source_documents/Heat_Quantum.pdf), 28 February 2018, page 3, equations (14)–(19), and page 5 | Treat state, normalization and evolution constraint separately. Heat-trajectory integrals can represent resolvent quadratic forms. | Requires a suitable positive operator/domain and endpoint decay. Approximate trajectories need residual and endpoint corrections; they do not retain variational bounds automatically. |
| [Dirac_operator_flow.pdf](../../../../investigations-2/active/20_constrained_operator_squares/source_documents/Dirac_operator_flow.pdf), 17 August 2018, pages 3, 4–8 and 12 | First-order matrix operators, spectral splitting and constrained squares suggest representations and observable design. The DS-II/Dirac literature makes this a concrete adjacent subject. | The proposed square's cross terms must reproduce the target operator. Number-changing terms and self-contractions cannot be silently removed. The mixed kinetic term in (10) is indefinite. |

For example, if an approximate field has residual
\(r=iA_t+A_{xy}-VA\), with real \(V\), its continuity equation has the exact defect

\[
\partial_t|A|^2+\nabla\cdot\mathbf j=2\Im(\bar A r).
\tag{19}
\]

An approximate mean-field relation has its own residual. This is the useful lesson of the 2018 trajectory work: retain the constraint error in the claimed observable, rather than treating normalization as a substitute for the equation.

## 7. Control screen and the remaining mathematical task

The exact identities (1)–(10) use only holomorphic heat evolution. Thus every analytic collision control listed in [Summary 12](../../../../../result-summaries/12_collision_controls_and_screening.md) passes them wherever its heat flow exists: Euler-factor, weighted-square, reflected super-Gaussian, smooth/positive-primitive, finite-prime, finite-profile, and RH-conditional close-source controls. Compact normalization (12) is also available for all of them. None fails a premise of this field construction. This is an analytic screen by the same general proof, not a newly run campaign of numerical witnesses.

The book's positive-source all-multiple example also passes. The polynomial \(z^2-2t\) gives the simplest fully explicit screen, including global norm one. At a collision these controls have positive limiting excess in (17); any claimed zero upper bound would fail there. No such bound is proved in this note.

What the controls lack is the unchanged complete theta source and its exact arithmetic data; the particular failed arithmetic/reflection/support premises differ by family and are recorded in Summary 12. Those distinctions are not used in the generic field identities. Adding the name “theta” to the field equation without a quantitative consequence would therefore not distinguish the controls.

The useful research question is now specific: **can the actual theta constraints give a bound on a multiplicity-sensitive field observable, with localization, resolution and approximation costs retained?** The density-square observable (18) supplies one explicit object to investigate. The DS-II formulation supplies an established set of evolution and operator tools to examine. Neither yet supplies the required theta-specific bound, a uniform high-height limit, or an exclusion of multiple zeros.

The moving contour can consequently be optional in the field formulation: it remains one way to select a transport region or measure flux. A fixed observation window is sufficient to define the normalized state, and its boundary terms are explicit in (13)–(15).

## Verification and saved evidence

- [Exact symbolic checker](../numerics/17_check_complex_zero_field.py) and [execution record](../numerics/17_COMPLEX_ZERO_FIELD_CHECKS_20261024.json): eight generic heat-jet identities reduce exactly to zero in SymPy 1.14.0; monomial mass checks for orders 1–6 and the separated/double-pair limits pass. The general proofs above, not a finite sample, establish their stated scope.
- [Source and file receipt](../numerics/17_COMPLEX_ZERO_FIELD_SOURCE_RECEIPT_20261024.json): input identities, source PDF hashes and saved checker/output hashes. Hashes establish file identity, not mathematical validity.
- [Primary-reference receipt](../../references/REFERENCE_COMPLEX_ZERO_FIELD_RECEIPT_20261024.json): versioned PDFs retained outside Git, with retrieval times, sizes and hashes.
- Continued in [brainstorm history 0009](../chat-histories/0009_2026-10-24T12-58-27Z_review-conserved-contour-results.json), preserving the author's normalization clarification and subsequent steering.

No manuscript edit, new draft snapshot, proof of RH, simplicity theorem, or commit was made by this continuation.
