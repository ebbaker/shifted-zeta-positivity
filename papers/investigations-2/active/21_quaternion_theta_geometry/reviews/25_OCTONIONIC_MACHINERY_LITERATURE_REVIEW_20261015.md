---
research_program: COORD
secondary_programs: [PR01, PR02, PR03]
status: internal_literature_review
---

# Octonionic simplifications and the theta collision problem

15 October 2026, America/New_York. Prepared for Edward Baker with substantial LLM assistance. Recorded model **gpt-6-astra**, reasoning effort **ultra**, verified from this turn's metadata. Three parallel LLM investigations supported the algebra, analysis, and arithmetic review. The deductions and checks below are internal research assessments, not external refereeing or proof-assistant verification.

## Assessment

The present octonionic construction can be simplified materially, but the reviewed literature does not supply the missing theta-specific stationary sign estimate. The most useful immediate changes are an alternative reflected monogenic lift and an explicit reduction of the physical associators to planar bilinear forms. The most promising analytic follow-up is a complete-source correlation-kernel formulation, connected directly to the established literature on Laguerre inequalities and Fourier transforms.

Exceptional theta series, triality, and octonionic reproducing kernels are substantial theories. Their available positivity statements concern different observations or require additional hypotheses. Applying them here requires an explicit identity or inequality for the physical first-jet energy. A shared eight-dimensional setting or a positive norm is insufficient.

This assessment leaves the manuscript, research overview, and notes organization unchanged. It proposes no new sign region or RH conclusion.

## Baseline and scope

The reviewed manuscript is [quaternion_theta_geometry.tex](../manuscript/quaternion_theta_geometry.tex), SHA-256 `7316eded0017b8da9f2641c6cc9207f26883fb5b87f3f11f4a7b5b178c831376`. The program context is the [research overview](../research-overview/RESEARCH_OVERVIEW_20261015.md) and [continuation note 34](../notes/00_research_coordination/34_MANUSCRIPT_PROGRAMS_AND_CONTINUATION_20261015.md), together with [octonionic note 15](../notes/15_OCTONIONIC_LIFT_AND_ASSOCIATOR_SIGN_TARGET_20261014.md) and [review 10](10_OCTONIONIC_LIFT_AND_ASSOCIATOR_INTERNAL_REVIEW_20261014.md).

Write

\[
h_j=\partial_x^jH,\qquad E=h_0^2+h_1^2,\qquad
\mathcal L_j=h_{j+1}^2-h_jh_{j+2},\qquad S_j=\{h_{j+1}=0\}.
\]

The open task is a source-derived lower bound \(\mathcal L_j\ge-K_jE\) on both full stationary sets, with coefficients locally bounded through every covered positive-time candidate collision. The manuscript's logarithmic-loss and all-cutoff transfers give alternative sufficient formulations. They do not remove this obligation. The established outer domain begins at \(t\log(|x|/(4\pi))\ge61/24\), at an unevaluated height, and the finite certificate reaches \(|x|\le112\).

The review covers octonion algebra and calibrated geometry; monogenic, slice, and partial-slice function theories; integral operators and reproducing kernels; integral octonions and exceptional theta series; and the scalar correlation literature needed to assess their relevance. Current primary records were checked through 15 October 2026. The recent papers below are identified as preprints where appropriate. This is a targeted literature review, not a claim that every paper mentioning octonions and zeta has been exhausted.

## Exact simplifications

### A reflected monogenic lift

The manuscript uses

\[
\mathcal O_m(t,q,r)=
\left(G_m(t,q)-\tfrac12G_{m+3}(t,q)\bar r,\ G_{m+2}(t,q)\right),
\]

where \(D_qG_m=0\), \(\partial_tG_m=-G_{m+2}\), and \(\partial_{x_0}G_m=G_{m+1}\). Its correction preserves the same quaternion argument in the two components and gives genuine dependence on the added coordinates.

If only monogenicity, the physical trace, and the external heat/jet identities are required, a simpler alternative is

\[
\boxed{\widetilde{\mathcal O}_m(t,q,r)
       =\bigl(G_m(t,q),\ G_{m+2}(t,\bar q)\bigr).}
\]

It is independent of \(r\). In the manuscript's pair convention, this gives

\[
\mathcal D_8\widetilde{\mathcal O}_m
=\left(D_qG_m(t,q),\ \bar D_q[G_{m+2}(t,\bar q)]\right)=0,
\]

because quaternion conjugation reverses all three imaginary coordinate derivatives, so
\(\bar D_q[B(\bar q)]=(D_qB)(\bar q)\).
Reflection commutes with \(\partial_{x_0}\) and the external time derivative. Consequently

\[
\partial_{x_0}\widetilde{\mathcal O}_m=\widetilde{\mathcal O}_{m+1},
\qquad \partial_t\widetilde{\mathcal O}_m=-\widetilde{\mathcal O}_{m+2},
\qquad
\widetilde{\mathcal O}_m(t,x,0)=(G_m(t,x),G_{m+2}(t,x)).
\]

For \(m=0\), field values require derivatives only through \(h_3\), eliminating the original correction's \(h_4\). Differentiation still generates higher jets; this is not a finite closed heat system. Away from the physical slice the second component has reflected spectral and complex-time arguments, so this does not replace the original lift when common off-slice arguments or dependence on all eight coordinates is required. It is a new elementary deduction for the present manuscript, independently checked by the algebra and analysis investigations, rather than a theorem imported from a source.

### A planar dictionary for every physical associator

Put \(v_j=(h_j,h_{j+1})\). Then

\[
E=|v_0|^2,\qquad
\mathcal L_j=-\det(v_j,v_{j+1}),\qquad
\tfrac12E_t=-v_0\cdot v_2.
\]

All physical \(G_m\) lie in the single complex plane \(\mathbb R+\mathbf j\mathbb R\). The full octonionic trace lies in the associative quaternion subalgebra generated by \(\mathbf j\) and \(\ell\). The nonzero associators in the manuscript arise from the fixed transverse twists, not from nonassociative multiplication of the untwisted physical jets.

For \(a=A+\mathbf jB\), \(b=C+\mathbf jD\), and \(\mathbf u=\ell\mathbf j\), the manuscript's identities read

\[
[a\mathbf i,b\mathbf i,\ell]=-2\mathbf u\det((A,B),(C,D)),
\qquad
[a\mathbf i,b\mathbf k,\ell]=2\mathbf u (A,B)\cdot(C,D).
\]

Thus the signed observation is one real coefficient on a fixed oriented ray. Computing that coefficient directly simplifies proofs and interval propagation without losing any cross terms. Merely replacing it by the associator norm changes a signed determinant into its absolute value.

The classical Harvey–Lawson identity for imaginary octonions,

\[
\varphi(a,b,c)^2+\tfrac14|[a,b,c]|^2=|a\wedge b\wedge c|^2,
\]

reduces for these twisted triples to the ordinary planar Gram identity. The calibration term is zero, since the relevant product lies in \(\mathbb H\) and is orthogonal to \(\ell\). It supplies a squared magnitude, not the required orientation. This specialization follows from the primary [Harvey–Lawson paper, Theorem 1.6](https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/6313-11511_2006_Article_BF02392726.pdf); [Karigiannis, Corollary 3.52](https://arxiv.org/abs/1909.09717) provides a modern account.

### A single observation for the existing full-amplitude cutoffs

Let \(v_2^{(N)}=(h_2^{(N)},h_3^{(N)})\) use precisely the manuscript's staircase cutoff, and define

\[
B_N=-v_0\cdot v_2^{(N)}=-h_0h_2^{(N)}-h_1h_3^{(N)}.
\]

On \(S_0\), \(B_N=J_{0,N}\). On \(S_1\),

\[
B_N-J_{1,N}=-h_0h_2^{(N)}=h_0(h_2-h_2^{(N)}).
\]

Consequently the discrepancy is at most \(\sqrt E\,|h_2-h_2^{(N)}|\), with the complete source-tail bound available. More generally, on \(S_0\cup S_1\),

\[
\left|B_N-\tfrac12E_t\right|
\le \sqrt E\,|v_2-v_2^{(N)}|.
\]

Its octonionic expression is simply
\(-[F\mathbf i,G_2^{(N)}\mathbf k,\ell]/2=\mathbf uB_N\).
This unifies notation and preserves the vanishing at \(E=0\), while giving exactly the square-root-energy tail scale used by the existing Young-inequality transfer. It adds no new signed estimate. All stationary sets remain those of the full source.

The separate \(J_{j,N}\) observations can still give sharper certificates: on \(S_1\), the combined observation pays an extra \(h_2\) tail that the separate product avoids. The common notation is therefore optional, not a proposed strengthening of PR02. The underlying paired kernels have at most three features, \(1,y,y^2\), before source weighting. Shared moments can be computed without constructing a large pair matrix; this factorization is already implicit in the jet formulation. It does not make the quadratic form positive:

\[
\mathcal L_j=h_{j+1}^2+\tfrac14(h_j-h_{j+2})^2
                          -\tfrac14(h_j+h_{j+2})^2.
\]

Its unrestricted inertia is \((2,1)\), and an invertible change of coordinates cannot remove the negative direction.

### Ambient logarithmic positivity can be computed exactly

The special quaternionic lift is the holomorphic vector \(v=(H,H_z)\) in the two complex variables \((z,\tau)\). Away from its common zero set, \(\log\widehat E\), where \(\widehat E=|H|^2+|H_z|^2\), is plurisubharmonic. Direct differentiation gives on the physical slice

\[
\boxed{\Delta_q\log\widehat E
=\frac{4\{\mathcal L_0^2+(h_0h_3-h_1h_2)^2\}}{E^2}.}
\]

This shows exactly why ambient elliptic positivity does not control the heat derivative: the orientation has been squared away. The formula is valid only where \(E>0\). It must not be used to assume the absence of a common zero.

Nor is logarithmic subharmonicity a generic octonionic monogenic principle. The eight-dimensional Cauchy kernel has magnitude \(|p|^{-7}\); away from zero, \(\Delta_8\log|p|^{-7}=-42/|p|^2<0\). The stronger property above comes from the holomorphic two-component structure of this particular lift.

## The most promising analytic reduction

### One complete theta correlation family

Extend \(w_t(u)=e^{tu^2}\Phi(u)\) evenly to the real line. The manuscript normalization is

\[
2H(t,x)=\int_{\mathbb R}w_t(u)e^{ixu}\,du.
\]

For \(m=0,1,2\), define

\[
K_m(t,s)=\int_{\mathbb R}r^{2m}w_t(s+r)w_t(s-r)\,dr.
\]

The complete source is positive, even, and rapidly decreasing, and all polynomially weighted integrals below converge absolutely on bounded time intervals. Direct polarization and \(u=s+r,v=s-r\) give

\[
\boxed{\mathcal L_0(t,x)=\int_{\mathbb R}K_1(t,s)\cos(2xs)\,ds,}
\]
\[
\boxed{\mathcal L_1(t,x)=\int_{\mathbb R}
 [K_2(t,s)-s^2K_1(t,s)]\cos(2xs)\,ds.}
\]

For the first formula, if \(F=2H\), symmetrization yields
\(F'^2-FF''=\frac12\iint(u-v)^2w_t(u)w_t(v)e^{ix(u+v)}du,dv\).
The change of variables has Jacobian two and \((u-v)^2=4r^2\); division by four proves the displayed normalization. For the second formula, the symmetrized multiplier for \(F''^2-F'F'''\) is \(-uv(u-v)^2/2\). Since \(uv=s^2-r^2\), the second formula follows with the stated sign.

The heat deformation has an exact expression:

\[
K_m(t,s)=e^{2ts^2}\int_{\mathbb R}r^{2m}e^{2tr^2}
             \Phi(s+r)\Phi(s-r)\,dr,
\qquad \partial_tK_1=2s^2K_1+2K_2.
\]

Consequently

\[
\boxed{(\partial_t+\partial_x^2)\mathcal L_0=2\mathcal L_1.}
\]

The last identity also follows immediately by differentiating the scalar jets and using backward heat. It relates the two observations but does not allow the second stationary set to be discarded.

This is the associated-kernel construction of [Csordas, Theorem 3.7](https://arxiv.org/pdf/1309.0055), specialized with the manuscript's normalization and supplemented by the derivative observation. The Wronskian/correlation framework of [Dimitrov–Xu](https://arxiv.org/pdf/1606.05011) places it in a broader established theory. These are classical mechanisms applied here, not claims of a new general correlation theorem. The formulas were derived directly, so importing the identities does not require assuming the log-concavity hypotheses of particular theorems in that literature for the deformed source.

The simplification is useful because both paired sectors, all source indices, and their cross interactions are present in one real correlation family. Before truncation there are no staircase-entry terms. Truncating the source or the correlation variables still requires complete tail and boundary payments; the coordinate change does not cancel those obligations.

### The precise remaining positivity problem

Although \(K_1(t,s)>0\), its Fourier transform need not be nonnegative. A pointwise positive function and a positive-definite kernel are different objects. Likewise \(K_2-s^2K_1\) has no automatic pointwise sign. Csordas's positive-definiteness conditions are substantive hypotheses, not consequences of source positivity.

The relevant weaker targets remain

\[
\int K_1(t,s)\cos(2xs)\,ds\ge-\kappa_0E\quad\text{on }S_0,
\]
\[
\int [K_2(t,s)-s^2K_1(t,s)]\cos(2xs)\,ds\ge-\kappa_1E
\quad\text{on }S_1.
\]

Here \(\kappa_0,\kappa_1\) are loss coefficients, distinct from the correlation kernels. They must be prescribed from the source and locally bounded through candidate collisions. A positive-definite decomposition with a paid signed remainder would suffice, but demanding positive definiteness everywhere is stronger than the present program requires. The manuscript's positive-source collision controls remain a decisive test of any proposed generic argument.

The energy itself has a compatible exact representation. With

\[
B(t,s)=\tfrac12\{(1-s^2)K_0(t,s)+K_1(t,s)\},
\qquad E(t,x)=\int_{\mathbb R}B(t,s)\cos(2xs)\,ds,
\]

the target is the nonnegativity of the transform of
\(A_j(t,s)+\kappa_j(t,x)B(t,s)\) on \(S_j\), where
\(A_0=K_1\) and \(A_1=K_2-s^2K_1\). Since \(\kappa_j\) may depend on \(x\), this is generally not a single global positive-definite-kernel problem. This formulation keeps the physical energy and avoids division by it.

The preferred hybrid cutoff can also be preserved exactly. Set \(d_n=\frac12\log n\), \(V_N=\frac12\log N\), and

\[
\psi_{a,N}(t,y)=e^{t(y+ia)^2}
\sum_{y+d_n\le V_N}\phi_n(y+ia)\quad(y\ge0),
\]

with value zero elsewhere. Then define

\[
\mathscr C_{j,N}^{a}(t,s)=
-\int_{s-V_N}^{s}[i(s+r)]^j[-a+i(s-r)]^{j+2}
  w_t(s+r)\psi_{a,N}(t,s-r)\,dr.
\]

Direct multiplication of the full-line formula for \(h_j\) and the original retained shifted formula gives

\[
J_{j,N}=e^{-ax}\Re\int_{\mathbb R}
\mathscr C_{j,N}^{a}(t,s)e^{2ixs}\,ds.
\]

This is the same full-amplitude cutoff in new coordinates. Its staircase and discontinuities remain inside \(\psi_{a,N}\), and the original complete tail bound still applies. A new estimate in this representation must retain them.

The first worthwhile research task is to use the exact theta/Poisson identity inside this correlation family and determine whether it yields a complete signed remainder at the physical energy scale. The two theta arguments are \(e^{4(s+r)}\) and \(e^{4(s-r)}\); their product is \(e^{8s}\). They are reciprocal only on \(s=0\). Thus modular inversion does not automatically turn the full two-variable product into a diagonal positive expression. Moreover the factor \(e^{tu^2}\) becomes \(\exp\{t(\log y)^2/16\}\) under \(y=e^{4u}\): it preserves inversion symmetry but is not a fixed modular weight. A transformed identity must carry this factor explicitly.

More precisely, after using the theta identity to establish evenness of \(\Phi\), inversion of one factor exchanges \(s\) and \(r\), up to signs. This pair symmetry holds for arbitrary even kernels and therefore cannot by itself distinguish the theta source from the collision controls. Extra arithmetic identities, beyond that reflection, are needed.

## How the broader octonionic literature applies

### Algebra, triality, and calibrated geometry

[Baez, The octonions](https://arxiv.org/abs/math/0105155) supplies the Cayley–Dickson convention, alternativity, quaternionic subalgebras, and triality. These explain why the physical trace has fewer algebraic degrees of freedom than an arbitrary octonion. Moufang identities can safely shorten selected products, but do not impose a sign on the scalar determinant.

Triality preserves the relevant norm/trilinear structures. The collision observation, however, singles out the first pair \((h_0,h_1)\), and the stationary sets single out two derivative coordinates. A transformation that mixes this pair with \((h_2,h_3)\) must transport the projection and stationary constraints as well. If it does, it preserves the same problem; if it does not, it changes the collision detector. In particular \(|\mathcal O|^2=E+h_2^2+h_3^2\) is already positive at an ordinary double collision.

The Harvey–Lawson and Karigiannis calibration identities give useful consistency checks and coordinate-free descriptions, but their specialization above yields no additional theta relation. A calibrated-submanifold argument would also need an actual map whose tangent planes satisfy the calibration hypotheses; the fixed octonionic target space does not establish those hypotheses.

### Monogenic and slice analysis

[Kauhanen–Orelma, Cauchy–Riemann operators in octonionic analysis](https://arxiv.org/abs/1701.08698) is directly relevant to checking operator conventions and their Clifford realization. It supports keeping multiplication order explicit. An associative real-matrix representation of left multiplication is useful for implementation: the imaginary-unit operators satisfy Clifford anticommutation because alternativity cancels the symmetric associator terms. This construction is explicit in [Baez, Section 2.3](https://math.ucr.edu/home/baez/octonions/node6.html). Matrix composition is not a multiplicative embedding of the octonion algebra.

[Colombo–Kraußhar–Sabadini, Octonionic monogenic and slice monogenic Hardy and Bergman spaces](https://arxiv.org/abs/2311.07691) develops reproducing spaces using an appropriate real part of a weighted para-linear inner product. These can provide bounded-domain norm and evaluation estimates. Their Hilbert-space positivity does not provide a lower bound for \(-\langle F,F_{xx}\rangle\) at the physical energy scale.

[Kraußhar–Ferreira–Vieira–Rodrigues, The Teodorescu and the Π-operator in octonionic analysis and some applications](https://doi.org/10.1016/j.geomphys.2024.105328) develops Borel–Pompeiu/Teodorescu formulas and Bergman projections with the required associator compensation. This is potentially useful for a future approximate monogenic field with a known defect. The current lifts are already exactly monogenic, so replacing them by an integral reconstruction adds boundary and kernel bookkeeping without a known gain in the signed theta estimate.

[Xu–Sabadini, Generalized partial-slice monogenic functions: the octonionic case](https://arxiv.org/abs/2503.12409v4), published in Transactions of the AMS 379 (2026), 3257–3291, unifies several regularity settings and proves representation and integral formulas. This is a useful current reference. Its identity and maximum-modulus theorems do not turn nonzero ambient fields into a nonvanishing distinguished two-component trace. Slice and Dirac monogenicity must not be interchanged without checking the defining equations.

### Exceptional arithmetic and modular sign constructions

The connection between integral octonions and the \(E_8\) lattice is real, but the lattice theta series counts eight-dimensional norms. The manuscript source is a differentiated one-dimensional Jacobi theta function. Replacing it with an \(E_8\) theta series changes the arithmetic coefficients and the function under investigation. Tensor powers also lose direct equivalence with the first-jet collision observation.

For example, in the standard lattice normalization,
\(\Theta_{E_8}(\tau)=E_4(\tau)=1+240\sum_{n\ge1}\sigma_3(n)e^{2\pi in\tau}\).
Its Mellin transform is

\[
\int_0^\infty(\Theta_{E_8}(iy)-1)y^{s-1}\,dy
=240(2\pi)^{-s}\Gamma(s)\zeta(s)\zeta(s-3),\qquad\Re s>4.
\]

This follows by termwise integration and the divisor-sum identity. The extra zeta factor and different center make the mismatch explicit. [Elkies–Gross](https://msp.org/pjm/1997/181-3/pjm-v181-n3-p06-s.pdf) supplies the integral-octonion lattice background.

There are genuine exceptional-to-classical modular bridges. In particular [Yi Shan, The global exceptional theta correspondence for F4 × PGL2, version 2](https://arxiv.org/abs/2501.19101v2), revised **12 October 2026**, constructs exceptional theta series on the classical modular group and proves nonvanishing of the stated global lifts. Its Theorem B concerns cuspidal eigenforms in \(S_{2n+12}(\Gamma_0(N))\), \(n\ge0\), in the trivial-character PGL2 setting; Theorem E states that the reverse theta-series construction spans \(S_{2n+12}(\mathrm{SL}_2(\mathbb Z))\) for \(n>0\). This rules out dismissing exceptional theory as disconnected from classical modular forms. It does not yet identify the current heat-deformed theta correlation as one of those forms or carry its stationary energy-relative observation through a lift.

For a useful exceptional route, first exhibit an explicit transform or restriction reproducing the actual \(H\), its four jets, or the complete correlation kernels, with the heat deformation and projections preserved. Next show that a known arithmetic identity yields a signed estimate after that restriction. Without this bridge, positive Fourier coefficients or a positive Jordan-algebra norm concern another quantity.

The sign-construction methods behind [Viazovska's eight-dimensional sphere-packing theorem](https://arxiv.org/abs/1603.04246) are a more concrete source of ideas: modular transformations can be used to construct functions with prescribed Fourier signs. The useful lesson is to identify a specific modular expression and prove its transformed sign. The dimension eight and the \(E_8\) connection do not by themselves transfer the theorem to the present problem.

[Romik's proof of Viazovska's modular form inequalities](https://www.math.ucdavis.edu/~romik/data/uploads/papers/ineq.pdf) is especially useful for studying how to preserve the combined modular expression before estimating its parts. It remains a methodological precedent until the current source expression has been identified and its deformation accounted for.

Two recent preprints by Seewoo Lee, [Inequalities involving polynomials and quasimodular forms](https://arxiv.org/abs/2602.10536) and [Positive quasimodular forms and the sign uncertainty principle](https://arxiv.org/abs/2608.15415v2), give additional concrete modular inequality methods. They merit a bounded applicability check if a transformed theta correlation can be placed in their classes. The required identification has not been established here; their Fourier-eigenfunction sign conditions are not the current stationary collision condition.

### A useful scalar comparison with de Branges theory

On intervals where \(G_j\ne0\), identifying \(\mathbf j\) with the complex unit gives

\[
\partial_x\arg(h_j+i h_{j+1})
=-\frac{\mathcal L_j}{h_j^2+h_{j+1}^2}.
\]

The associator orientation therefore also has a familiar phase/Wronskian interpretation. This can improve exposition and diagnostics. It does not justify dividing by the denominator at a collision or treating a Hermite–Biehler hypothesis as already proved.

The warning is concrete: [Conrey–Li](https://arxiv.org/pdf/math/9812166) give counterexamples to particular proposed de Branges shift-positivity conditions for spaces associated with zeta and Dirichlet L-functions. Their result concerns those specific conditions, not all de Branges approaches. A new kernel-positivity route here must state its exact observation and establish its own source hypothesis.

## Recommended priorities

| Candidate | Immediate value | Missing step | Recommendation |
| --- | --- | --- | --- |
| Reflected octonionic lift | Removes the auxiliary correction when the physical trace is the goal | Decide whether common off-slice arguments are needed | Retain as a proved alternative; short finite project |
| Planar associator dictionary and combined cutoff | Shorter algebra and common tail bookkeeping | No new sign estimate | Use in exposition and future certificates |
| Complete theta correlation kernels | Puts both signs in one source family and connects to established Fourier theory | A theta-specific signed estimate with complete payments | Highest-priority new analytic follow-up within PR02 |
| Modular sign constructions | Offers explicit transform-based inequality techniques | Identify the deformed kernel in an applicable class | Bounded literature-to-identity test |
| Hardy/Bergman/Teodorescu estimates | Useful if a concrete boundary or defect estimate is needed | Convert norm control to the required signed relative observation | Supporting tool, not a separate principal program |
| Exceptional theta lifts and triality | Genuine arithmetic structure and exact symmetry | An observation-preserving bridge to this source | Exploratory until the bridge is written explicitly |

If adopted, a short **Octonionic reductions** folder could contain the reflected lift, planar dictionary, and exact checks. A **Theta correlation kernels** folder would have a distinct analytic target and could serve as a focused branch of PR02. The broader overview should continue to identify source-specific stationary control as the principal route. No new folder is warranted solely for another equivalent representation.

A useful first deliverable for the correlation project is an exact transformed identity plus an all-cutoff lower-bound target that survives near \(E=0\). Any numerical pilot should use predetermined stationary observations, retain all source interactions, freeze its coefficient rule, and validate on fresh cells. A favorable plot or a positive correlation density is not the required theorem.

## Additional primary references and applicability

The linked discussion above covers the main references. The following additional works complete the principal branches checked in this review.

| Primary reference | Relevance and limitation |
| --- | --- |
| Schray and Manogue, *Octonionic representations of Clifford algebras and triality*, Foundations of Physics 26 (1996), 17–70. [Author text](https://arxiv.org/abs/hep-th/9407179) | Careful octonionic Clifford and triality framework. Useful for validating representation changes; it supplies no theta sign estimate. |
| Kauhanen and Orelma, *On the Structure of Octonion Regular Functions*, Advances in Applied Clifford Algebras 29 (2019), article 77. [Publisher](https://doi.org/10.1007/s00006-019-0983-y) | Proposition 3.5 and Section 4 distinguish left regular, bi-regular, and Riesz-type classes. This prevents unjustified transfers of stronger regularity properties to the current lift. |
| Li and Peng, *The Cauchy integral formulas on the octonions*, Bulletin of the Belgian Mathematical Society 9 (2002), 47–64. [Publisher](https://doi.org/10.36045/bbms/1102715140) | Foundational formulas with nonassociativity accounted for. Moving factors through a boundary kernel without the required brackets can change the formula. |
| Constales and Kraußhar, *Octonionic Kerzman–Stein Operators* (2021). [Author preprint](https://arxiv.org/abs/2012.11925) | Hardy-space boundary projection methods and real-inner-product adjoints. Potentially useful for a concrete boundary reconstruction; not presently simpler than the manuscript's scalar contour estimates. |
| Gentili and Struppa, *Regular Functions on the Space of Cayley Numbers*, Rocky Mountain Journal of Mathematics 40 (2010), 225–241. [Author repository](https://digitalcommons.chapman.edu/scs_articles/15/) | Octonionic slice regularity and zero structure. Its function class differs from the manuscript's Dirac-monogenic class. |
| Ghiloni, *Slice Fueter-Regular Functions*, Journal of Geometric Analysis 31 (2021), 11988–12033. [Publisher](https://doi.org/10.1007/s12220-021-00709-x) | Quaternionic-slice regularity, Vekua equations, and integral formulas. The required slice condition is additional, and a maximum-modulus result is not a lower bound for the physical first pair. |
| Colombo, Sabadini, and Sommen, *The Fueter mapping theorem in integral form and the F-functional calculus*, Mathematical Methods in the Applied Sciences 33 (2010), 2050–2066. [Publisher](https://doi.org/10.1002/mma.1315) | Integral transfer from slice data to monogenic functions in Clifford analysis. Such differential transforms change the physical observation and can annihilate low-degree collision controls; trace reconstruction is essential. |
| Feehan, *A Kato–Yau inequality for harmonic spinors and decay estimate for eigenspinors*, Journal of Geometric Analysis 11 (2001), 469–489. [Author preprint](https://arxiv.org/abs/math/9903021) | Refined norm-gradient bounds. These concern ambient spatial derivatives, not the sign of the external heat derivative. |
| Borrelli and Wu, *On the Nodal Set of Solutions to Dirac Equations*, Journal of Geometric Analysis 36 (2026), article 195. [Publisher](https://doi.org/10.1007/s12220-026-02443-8) | Frequency and nodal-set dimension results describe possible zeros rather than exclude intersections with the physical slice. A double collision is not even a zero of the full four-jet octonionic field. |
| Elkies and Gross, *Embeddings into the Integral Octonions*, Pacific Journal of Mathematics 181, special issue (1997), 147–161. [Publisher PDF](https://msp.org/pjm/1997/181-3/pjm-v181-n3-p06-s.pdf) | Sections 1–2 connect the Coxeter order with E8 and count embeddings using theta series. Genuine arithmetic structure, but different source coefficients and observations. |
| Kim, *Exceptional modular form of weight 4 on an exceptional domain contained in C27*, Revista Matemática Iberoamericana 9 (1993), 139–200. [Publisher](https://ems.press/journals/rmi/articles/5274) | A singular modular form on the exceptional domain of Hermitian octonionic matrices. Its arithmetic Fourier and Mellin structure does not directly realize the present heat family. |
| Pollack, *Exceptional theta functions and arithmeticity of modular forms on G2*, arXiv:2211.05280. [Author text](https://mathweb.ucsd.edu/~apollack/exceptional_theta_functions.pdf) | Theorems 1.0.1 and 1.1.1 give arithmeticity and explicit theta expansions. Algebraic coefficients and rank restrictions are not signed physical product bounds. |
| Pollack, *Exceptional Siegel–Weil theorems for compact Spin8*, arXiv:2308.09100 (2023). [Author record](https://arxiv.org/abs/2308.09100) | Exceptional theta lifts and Eisenstein identities supply a real triality-related summation mechanism. A bridge identifying the current source inside it is still needed. |
| Lee, *Algebraic proof of modular form inequalities for optimal sphere packings*, arXiv:2406.14659. [Author record](https://arxiv.org/abs/2406.14659) | A complementary algebraic approach to modular inequalities, relevant if a concrete transformed correlation lands in its modular class. |

For bibliographic clarity, the manuscript's Kauhanen–Orelma preprint appeared as *Cauchy–Riemann Operators in Octonionic Analysis*, Advances in Applied Clifford Algebras 28 (2018), article 1, DOI [10.1007/s00006-018-0826-2](https://doi.org/10.1007/s00006-018-0826-2). The Csordas reference used here is arXiv:1309.0055v2 (2014). Dimitrov–Xu appeared in Transactions of the AMS 372 (2019), 4107–4125. Baez appeared in Bulletin of the AMS 39 (2002), 145–205, and Harvey–Lawson in Acta Mathematica 148 (1982), 47–157. These publication details can be incorporated into the manuscript bibliography if the corresponding discussion is adopted.

## Validation and provenance

The reflected-lift proof and its off-slice limitation were checked independently by two LLM investigations. The retained [exact checker](../numerics/check_octonion_reflected_lift.py) and [execution record](../numerics/OCTONION_REFLECTED_LIFT_CHECKS_20261015.json) contain **325 passing assertions** over sparse integer polynomials: heat-polynomial inputs of degrees 0 through 12, lift levels 0 through 3, full operator/trace/heat checks, and bilinear/cutoff identities. They use no sampling. The general proof is the chain rule, not the finite test family.

The correlation constants and signs were derived from the full-line Fourier normalization above; for the control \(w(u)=e^{-u^2}\), they give \(\mathcal L_0=\pi e^{-x^2/2}/8\), agreeing with direct differentiation of \(H=\sqrt\pi e^{-x^2/4}/2\). Independent LLM review of this assembled assessment checked the correlation, energy, hybrid-cutoff, and logarithmic-energy formulas and found no blocking mathematical issue. The primary session reran the exact checker and reproduced its full record. These checks concern the new reductions, not the validity of every imported literature theorem or a new theta sign certificate.

This chat is registered as history **13**, **Review octonionic simplifications**, in the formal replay lane. The history registry remains authoritative for current capture counts and hashes. The overview, continuation note, manuscript, and historical notes were used as references and have not been rewritten by this review.
