# Flat quaternion Dirac operator and one lattice field for H

27 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort max**. Research chat **Continue higher-dimensional H-rep**, Investigation05 chat0003, thread 01a17f2b-8196-7683-ab85-434b4bd2ac20.

**Continuation update, 27 October 2026.** [Note13](13_RADIAL_LAPLACIAN_CONTINUATION_20261027.md) now supplies the next starting point: the standard radial Laplacian with the original theta sum. The dyadic/quaternionic construction below is retained as an exact comparison, but optimizing its arithmetic rule is no longer the immediate priority.

**Result and cost.** The standard flat quaternion Dirac operator, the actual spatial radius r=|X|=exp(2u), and a single Gaussian exponential field give an exact three-dimensional integral for the complete H(t,z). Both parameters occur inside the exponential. Genuine three-dimensional shell cancellation survives the observation. The price is a parity character and a dyadic hierarchy of cosets inside the cubic lattice. The kernel is not an ordinary unweighted heat kernel, and the construction does not establish a first-order Fueter equation in Newman time.

This extends the Jacobi shell identity and dyadic recovery already proved in [Note08][n08]. The changes are its quaternionic exponential form, assembly into one spatial field, and complete H observation with the flat Dirac operator. The shell theorem and dyadic decomposition are inherited; this is not a claim to a new theta identity. [Note09][n09] remains the whole-formula simplicity contract. The [result index][results], [hypercomplex summary][hypercomplex], and [avoid index][avoid] retain the prior status and the distinction between a representation and a collision mechanism.

## 1. The standard operator and the radial coordinate

Let X=x1 e1+x2 e2+x3 e3 be an imaginary quaternion, with

\[
e_i e_j+e_j e_i=-2\delta_{ij},\qquad
D_X=\sum_{i=1}^3e_i\partial_{x_i},\qquad D_X^2=-\Delta_X.
\tag{1}
\]

This is the standard Euclidean quaternion Dirac operator, with left multiplication. It is distinct from Note11's shifted scalar Laplacian on S^3. The flat convention is checked in Cerejeiras–Kähler–Kraußhar, Section 2.1; the four-dimensional Fueter convention is checked in Sudbery, equations (2.33)–(2.35). See [reference annotation07][refs].

Use the user's suggested paravector and the earlier radial coordinate:

\[
q=t+X,\qquad r=|X|\ge1,\qquad
\omega=X/r\in S^2,\qquad u=\tfrac12\log r.
\tag{2}
\]

In this note r really is the radius of the continuous three-dimensional integration variable. It also sets the damping of lattice sites. The angular phase below depends on omega, rather than being a plane wave in X. Thus pulling a flat torus heat field into these coordinates does not leave the same constant-coefficient heat equation in X.

For reference, the unchanged canonical normalization is

\[
A(r)=\sum_{n\ge1}e^{-\pi n^2r^2},\quad
\psi(u)=e^uA(e^{2u}),\quad
\Phi(u)=\tfrac18(\psi''-\psi)
        =\tfrac12r^{5/2}\Delta_3 A(r),
\tag{3}
\]
\[
H(t,z)=\int_0^\infty e^{tu^2}\Phi(u)\cos(zu)\,du.
\tag{4}
\]

Here Delta_3 in (3) is the ordinary radial Laplacian f''+2f'/r. A is used to verify the new field, not to define its summand.

## 2. A cubic lattice with a dyadic parity rule

Start with the additive lattice requested in the conversation,

\[
\Lambda=\mathbb Z e_1+\mathbb Z e_2+\mathbb Z e_3.
\]

For nonzero m in Lambda write uniquely

\[
m=2^{j(m)}v(m),\qquad j(m)\ge0,
\]

where the three integer coordinates of v are not all even. Thus j is the number of common factors of two in m's coordinates. Define

\[
\eta(m)=
\begin{cases}
(-1)^{v_3/2},&v_1\text{ odd and }v_2,v_3\text{ even},\\
0,&\text{otherwise}.
\end{cases}
\tag{5}
\]

The nonzero support is the disjoint union

\[
\mathcal L=\bigsqcup_{j\ge0}2^j\mathcal C,
\qquad \mathcal C=(1,0,0)+2\mathbb Z^3.
\tag{6}
\]

**Lattice scope:** Lambda is an additive rank-three lattice. Its weighted support L is a hierarchy of cosets, not itself an additive lattice or one periodic character of Lambda. This arithmetic choice must be counted when assessing simplicity.

The inherited Jacobi identity is

\[
\sum_{\substack{v\in\mathcal C\\|v|^2=N}}(-1)^{v_3/2}
=\begin{cases}2h\chi_4(h),&N=h^2,\ h\ge1\text{ odd},\\0,&\text{otherwise},\end{cases}
\quad \chi_4(h)=(-1)^{(h-1)/2}.
\tag{7}
\]

It follows from theta2 theta3 theta4=theta1' with nome exp(-4 pi r^2), using the conventions in Note08 and its DLMF annotation. In particular, this identity is supported by its infinite-series proof, not by the finite checks below.

## 3. A quaternionic exponential selects the square shells

For a nonzero imaginary quaternion v put R=|v| and I_v=v/R. Since v^2=-R^2,

\[
v^{-1}e^{I_v a}=\frac{\sin a}{R}-I_v\frac{\cos a}{R}.
\tag{8}
\]

Consequently a direct quaternionic lattice primitive is

\[
\boxed{\displaystyle
\mathcal Q_{t,z}(r)=\frac12\sum_{m\in\Lambda\setminus\{0\}}
\eta(m)v(m)^{-1}
\exp\!\left[
\pi r^2m^2+tu^2+
\left(\frac\pi2+\frac{zu}{|v(m)|}\right)v(m)
\right].}
\tag{9}
\]

Every exponent is a scalar plus a multiple of one imaginary quaternion, so its factors commute within that summand. Pairing v with -v cancels its vector part. For fixed j, grouping the scalar part by R and using (7) leaves

\[
e^{tu^2}\sum_{h\ge1\ {\rm odd}}
\chi_4(h)\sin(\pi h/2+zu)e^{-\pi r^2 4^j h^2}
=e^{tu^2}\cos(zu)\sum_{h\ge1\ {\rm odd}}e^{-\pi r^2 4^j h^2}.
\]

Every positive integer is uniquely 2^j h with h odd. Therefore

\[
\boxed{\mathcal Q_{t,z}(r)=e^{tu^2}A(r)\cos(zu).}
\tag{10}
\]

This meets the quaternionic-exponential summand goal directly. On its own it remains a radial primitive, not the requested three-dimensional observation. Simply integrating (9) against unused angles would add no structure. The next section supplies a field with actual angular dependence.

## 4. One angular Gaussian field and the complete spatial integral

Choose a fixed imaginary unit I, for example e1, and define on |X|>=1

\[
\boxed{\displaystyle
\mathcal K_{t,z}(X)=
\sum_{m\in\Lambda\setminus\{0\}}\eta(m)
\exp\!\left[
\pi r^2m^2+tu^2+
I\left(zu+\frac\pi2\langle v(m),\omega\rangle\right)
\right].}
\tag{11}
\]

This has one Gaussian exponential per weighted site, with no Phi or H inside it. The dot product is the Euclidean inner product of imaginary quaternions. The phase parameter z is a frequency conjugate to the logarithmic radius u. It does not depend on the lattice label. The sum has one field, rather than Note10's separate large-radius and reciprocal-radius Gaussian fields.

Let d sigma=d Omega/(4 pi) be probability measure on S^2 and Sc the quaternion scalar coefficient. Set K0=K_{0,0}. Pairing m and -m shows that K0 is scalar, though generally nonconstant in omega. The spherical exponential identity gives

\[
\int_{S^2}e^{I\pi\langle v,\omega\rangle/2}\,d\sigma
=\frac{\sin(\pi|v|/2)}{\pi|v|/2}.
\]

Using (7) at each dyadic scale yields

\[
\boxed{\displaystyle
\int_{S^2}\mathcal K_{t,z}(r\omega)\,d\sigma
=\frac4\pi e^{tu^2+Izu}A(r).}
\tag{12}
\]

This is genuine shell cancellation. At primitive squared radius 9, the two axial sites have signed count +2 and the eight nonaxial sites have count -8. Their total -6 is required for the correct coefficient. Keeping only the axial sites would give -1/3 in A instead of 1. The dyadic dilations preserve this contribution. This observation does not discard all transverse sites by a Fourier zero-mode projection.

The first complete formula uses exactly the user's operator:

\[
\boxed{\displaystyle
H(t,z)=-\frac1{64}\int_{|X|\ge1}r^{-1/2}
\operatorname{Sc}\!\left[e^{tu^2+Izu}D_X^2\mathcal K_{0,0}(X)\right]dX.}
\tag{13}
\]

To check its constant, spherical averaging commutes with the Euclidean Laplacian:

\[
\int_{S^2}\Delta_XK_0(r\omega)\,d\sigma
=\Delta_3\left(\frac4\pi A(r)\right).
\]

Substitute dX=4 pi r^2 dr d sigma, du=dr/(2r), and (3). The coefficient becomes (1/2)(pi/4)(1/2)/(4 pi)=1/64. The minus sign in (13) is D_X^2=-Delta_X. The angular Laplacian has zero sphere integral; it is included before averaging.

For a formula with both parameters already inside every summand and no derivatives on that summand, put

\[
B(t,z,u)=2t-1+(2tu+Iz)^2.
\tag{14}
\]

Then the complete observation is

\[
\boxed{\displaystyle
H(t,z)=\frac1{16}+\frac1{256}\int_{|X|\ge1}r^{-5/2}
\operatorname{Sc}\!\left[B(t,z,\tfrac12\log r)\mathcal K_{t,z}(X)\right]dX.}
\tag{15}
\]

Equivalently, in coordinates (u,omega),

\[
H(t,z)=\frac1{16}+\frac\pi{32}
\int_0^\infty\int_{S^2}e^u
\operatorname{Sc}[B(t,z,u)\mathcal K_{t,z}(e^{2u}\omega)]\,d\sigma\,du.
\tag{16}
\]

For the boundary calculation set g=exp(tu^2+Izu). It satisfies

\[
g''-g=[2t-1+(2tu+Iz)^2]g=Bg.
\]

At u=0, g=1, g'=Iz, and psi'(0)=-1/2. Two integrations by parts in (4) give

\[
\frac18\operatorname{Sc}\int_0^\infty g(\psi''-\psi)du
=\frac1{16}+\frac18\operatorname{Sc}\int_0^\infty(g''-g)\psi\,du.
\]

The endpoint term containing Iz psi(0) has zero scalar coefficient. Inserting (12) proves (16); changing measure proves (15). The additive constant and the polynomial B are retained completion costs.

## 5. Convergence and the roles of time and z

For real t,z, all preceding objects are ordinary quaternion-valued functions. For complex t,z, use H tensor C and extend Sc complex-linearly: Sc(a0+a1 e1+a2 e2+a3 e3)=a0. Do not replace this by the real part of a complex number; that would destroy holomorphy.

Since |v(m)|<=|m|, any fixed number of spatial derivatives of (11), on r>=1, introduces at most a polynomial in r, |m| and log r. On compact parameter sets, the remaining parameter factor is bounded by a constant times exp(T u^2+Z u). Moreover

\[
\sum_{m\ne0}e^{-\pi r^2|m|^2}
\le e^{-\pi r^2}\sum_{m\ne0}e^{-\pi(|m|^2-1)},\qquad r\ge1.
\tag{17}
\]

Polynomially weighted variants have the same integrable Gaussian domination after a harmless reduction of its exponent. Thus (9), (11), (13), and (15) converge absolutely, locally uniformly in t,z, and all used derivatives, shell groupings, integrals and parameter continuations are justified. The factor v^{-1} in (9) is bounded in norm by one. Entire continuation agrees with the original H on all finite complex t,z.

The field satisfies the physical parameter equation termwise:

\[
\partial_t\mathcal K_{t,z}=-\partial_z^2\mathcal K_{t,z},
\tag{18}
\]

because its t and z factors are exp(tu^2+Izu). This identity is not an ordinary diffusion equation in X. Writing q=t+X identifies a real coordinate with Newman time, but does not imply Fueter regularity

\[
(\partial_t+D_X)\mathcal K=0.
\]

Even the ordinary exponential exp(q) fails that equation: on the real axis, (partial_t+D_X)exp(q)=-2 exp(t). A simple monogenic plane wave exp(lambda t+I_k k dot X) instead requires lambda=|k| when I_k=k/|k|. That linear dispersion is different from the Newman factor u^2. These observations concern those explicit exponential ansatzes; they do not exclude other quaternionic constructions or observations.

The existing quaternionic investigation also kept Newman time independent in its [standard Fueter lift][fueter]. The present calculation does not replace that proven lift with an unproved first-order evolution. A parabolic Dirac system would require an enlarged algebra or spinor system; no such factorization is imported here.

## 6. Comparators and what became simpler

An even shorter full-cubic exponential with phase I(zu+2 pi(m2 a+m3 b)) has transverse torus average exp(tu^2+Izu)(Theta(r)-1). It completes Note06's marginal to H using the same polynomial B and boundary 1/16. However, it removes every m2 or m3 mode except zero. It therefore does not improve the explanatory issue identified in Note09.

A transverse magnetic-index idea was also considered. At the level actually needed for the observation, for any alpha(r)>0 and real gamma,

\[
\int_{[0,1]^2}\sum_{k,m,n\in\mathbb Z}
e^{-\pi r^2k^2-\alpha(r)(m^2+n^2)}
e^{I(2\pi(ma+nb)+\gamma mn)}\,da\,db=\Theta(r).
\tag{19}
\]

Fourier orthogonality proves this directly. It shows why a transverse phase or modified damping in this particular averaged family changes no observed data. No magnetic heat-kernel identification, spinor index theorem or operator normalization is required or claimed here. This test supplies no reason to replace the simpler projected Gaussian by a magnetic one.

The actual tradeoff in (11)–(16) is:

| Part | Improvement | Remaining cost |
| --- | --- | --- |
| Operator | Standard D_X, with D_X^2=-Delta_X | Only its square is used; no first-order advantage is proved |
| Continuous geometry | Actual X in the exterior of the unit ball, r=|X| | The angular phase depends on X/r, so this is not a flat spatial heat kernel |
| Summand | One Gaussian exponential, t and z included | Dyadic parity weight eta and primitive direction v(m) |
| Observation | One three-dimensional integral | B and 1/16, or two spatial derivatives |
| Surviving structure | Nonaxial shell contributions are essential | Signed cancellation, rather than a positive summand |
| Quaternion algebra | Inverse quaternion and exponential give (9) directly | The spatial kernel (11) lies in a fixed complex slice; noncommutativity has not improved recovery |

This is a cleaner assembly of one candidate, not a proof that the complete formula is intrinsically simpler than the original theta integral. The dyadic bookkeeping replaces the reciprocal-scale channel of Note10. No accuracy or speed improvement is claimed.

## 7. Checks and the next mathematical question

The [checker][checker] and [record][record] verify the quaternion anticommutators exactly, enumerate 900 scale/shell pairs through squared radius 225, and recover the weights of the first 15 squares by rational arithmetic. Separate floating diagnostics evaluate the literal quaternion exponential and both complete spatial formulas. Two angular/radial grids and five real or complex parameter pairs agree with the canonical integral to maximum absolute discrepancy 2.33e-14. These are normalization checks, not interval-certified quadrature or a proof of the infinite identities. [Review07][review] is a same-assistant assessment.

The next useful question is whether a standard geometric or quaternionic structure produces eta(m) and v(m) without prescribing the dyadic rule. A first-order identity whose observation supplies the completion would also improve the full formula. Merely replacing scalar notation by quaternion notation, or adding a transverse factor of index one, does not answer either question.

This is the seventh bounded RTC-03 representation return. Under [avoid01][classification], it is an exact representation, not a collision criterion or numerical milestone toward RH. It supplies no favorable sign, so the existing [collision controls][controls] are not rerun as if they certified this representation. Positive radial controls still lack the canonical theta arithmetic; weighted-square and Euler-factor controls alter it; forced-response controls still defeat a generic operator-positivity inference. The dyadic identity transfers the unchanged source but supplies no new exclusion estimate. [Avoid07][scope] governs the limited exponential and projection comparisons above, and [avoid16][imports] governs the selected literature use. Independent specialist review and the broader simplification task remain open.

[n08]: 08_GENUINE_THREE_DIMENSIONAL_LATTICE_SUMS_AND_THETA_RECOVERY_20261027.md
[n09]: 09_SIMPLER_HIGHER_DIMENSIONAL_H_REPRESENTATION_CONTINUATION_20261027.md
[refs]: ../references/07_FLAT_QUATERNION_DIRAC_REFERENCES_20261027.md
[checker]: ../numerics/10_check_flat_dirac_dyadic_lattice_20261027.py
[record]: ../numerics/10_FLAT_DIRAC_DYADIC_LATTICE_CHECKS_20261027.json
[review]: ../reviews/07_FLAT_DIRAC_DYADIC_LATTICE_SELF_REVIEW_20261027.md
[results]: ../../../../result-summaries/README.md
[hypercomplex]: ../../../../result-summaries/16_hypercomplex_reductions_and_geometric_realizations.md
[avoid]: ../../../../avoid/README.md
[classification]: ../../../../avoid/01_restating_the_target.md
[scope]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[imports]: ../../../../avoid/16_unchecked_imports_and_novelty_claims.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[fueter]: ../../../investigations-2/active/21_quaternion_theta_geometry/notes/3_STANDARD_FUETER_LIFT_WITH_INDEPENDENT_TIME_20261014.md
