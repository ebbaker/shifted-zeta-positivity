# Angular multiplicity and the radial Green function

4 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance from **gpt-6-astra (Codex), reasoning effort xhigh**, recorded for this turn. Thread `01a1a9d4-3d44-7472-ae0f-54705423d86b`, MC11 history0002.

**Type B — continuation of MC11-BR01.** The author asks whether the angular weight is natural or imposed, why D is squared, and whether angular Dirac degrees of freedom can be combined with radial u degrees of freedom. He adds that a spherically symmetric potential should allow separation. The bounded conceptual question is whether radial separation supplies the proposed inverse-multiplicity factor, and what assumptions are needed. This note compares the product-cylinder and Euclidean radial geometries analytically, with no new numerics or E04 assessment. The new Green-function derivation has proof-author checking only.

## What the angular weight actually does

For the self-adjoint Dirac operator D on the unit two-sphere, the eigenvalues are ±n, n>=1, and each sign has 2n eigenvectors. Thus the squared eigenvalue n² has 4n eigenvectors when both signs are retained. The ordinary heat trace is
\[
\operatorname{Tr}e^{-tD^2}=\sum_{n\ge1}4n\,e^{-tn^2}.
\tag{1}
\]
The target Q(t)=sum exp(-tn²) counts each distinct squared energy once. Inserting
\[
W=(4|D|)^{-1}
\]
weights each state in the nth block by 1/(4n), so that
\[
\operatorname{Tr}(We^{-tD^2})
=\sum_{n\ge1}4n\frac1{4n}e^{-tn^2}=Q(t).
\tag{2}
\]
At n=1 there are four states with weight 1/4 each, at n=2 eight with weight 1/8 each, and at n=3 twelve with weight 1/12 each. This is averaging within a spectral block, not normalizing the entire partition function by one constant.

Within the class W=w(|D|), exact equality with Q(t) for every t>0 fixes 4n w(n)=1 for every n. The target coefficients therefore force this weight in that class. Rotational invariance by itself does not select it. It is a positive bounded operator, 0<W<=1/4, and hence can be a measurement effect, but no apparatus or dynamical principle was specified in Note05. It is not a density matrix: its ordinary trace diverges. As an angular operator it is nonlocal, since it is an inverse spectral function of D. Keeping only the positive Dirac branch changes the factor to 1/(2n), while the essential inverse-n dependence remains.

More general operators need only have total trace one on each n² block; equation (2) alone does not uniquely determine an arbitrary operator. The uniqueness statement is restricted to the scalar spectral-weight class just specified.

## Why the square appears

D is a first-order geometric differential operator. Its eigenvalues are linear in n and have both signs. Squaring gives n² and a nonnegative second-order operator. With the convention D=-i slash-nabla, the spinor Lichnerowicz formula reads
\[
D^2=\nabla^*\nabla+\frac{R}{4}
=\nabla^*\nabla+\frac12
\quad\text{on the unit }S^2.
\tag{3}
\]
Thus D² is the usual spinor Laplace-type kinetic/heat operator, including the curvature term. It is not an arbitrary nonlinear reassignment of eigenvalues. However, using pi D² as an angular Hamiltonian is a model choice. A relativistic massless positive-energy Dirac Hamiltonian would instead scale like |D|, giving energies proportional to n; fermionic statistics alone do not require the square. The angular geometric operator, a squared kinetic operator and the physical time-evolution Hamiltonian must remain distinguished.

The primary source for the spectrum, multiplicity and curvature formula is [Camporesi and Higuchi, section 3.1, (3.54), and (5.35)–(5.36)](https://arxiv.org/html/gr-qc/9505009). Its anti-Hermitian convention is converted as above. The [reference catalog](../../references/README.md) records the version, inspected passages and archived PDF.

## Separation and a natural source of the weight

Spherical symmetry does allow angular-mode decomposition. It leaves a family of radial equations indexed by angular quantum numbers; the effective radial equations retain those labels. For a first-order Dirac system, radial spinor components may remain coupled within a channel.

There is an exact elementary calculation in the product geometry already present in the [radial companion](../../../../../../../../papers/investigations-5/05_radial_theta_collision_geometry/book/main.tex):
\[
g_C=dv^2+\tfrac14g_{S^2},\qquad v\in\mathbb R.
\tag{4}
\]
Here v denotes the radial log-coordinate while a heat parameter t is kept independent. Let Gamma be the angular chirality operator, Gamma²=1 and Gamma D=-D Gamma. The self-adjoint product Dirac operator is
\[
\mathcal D_C=-i\Gamma\partial_v+2D,
\qquad
\mathcal L:=\mathcal D_C^2=-\partial_v^2+4D^2.
\tag{5}
\]
The cross terms cancel by anticommutation. In the n² angular sector, the radial operator is
\[
\mathcal L_n=-\partial_v^2+4n^2.
\]
Its decaying full-line Green kernel is
\[
G_n(v,w)=\frac{e^{-2n|v-w|}}{4n}.
\tag{6}
\]
Away from v=w this solves the homogeneous equation, and its first derivative has jump -1, so L_n G_n=delta(v-w). Equivalently the equal-point value is the radial-momentum integral
\[
G_n(v,v)=\int_{\mathbb R}\frac{dk}{2\pi}\frac1{k^2+4n^2}
=\frac1{4n}.
\tag{7}
\]
At equal radial points, the operator-valued Green kernel is therefore exactly
\[
\boxed{G_{\mathcal L}(v,v)=(4|D|)^{-1}=W.}
\tag{8}
\]
After angular heat damping, the trace is finite and gives
\[
\boxed{
\operatorname{Tr}_{\mathrm{spin}(S^2)}
\bigl[e^{-tD^2}G_{\mathcal L}(v,v)\bigr]
=\sum_{n\ge1}e^{-tn^2}=Q(t),\qquad t>0.
}
\tag{9}
\]
No finite full-space trace of L^(-1) is asserted; equation (9) is a radial-diagonal kernel followed by an angular trace. It is not the heat trace Tr(exp(-t L)). All factors follow from the stated metric, angular multiplicity and one-dimensional Green kernel. With unit-radius spheres instead, L=-partial_v²+D² and the diagonal is 1/(2n); an overall factor 1/2 then gives Q. The inverse-n dependence, rather than that overall scale, is the substantive cancellation.

This improves the interpretation of Note05's weight: it can arise from a local three-dimensional kinetic operator after the radial response has been eliminated. The original trace insertion was selected to match theta coefficients; equations (5)–(9) exhibit a geometric response observable that produces it. This does not imply that every spherical model or an ordinary thermal trace has that weight. Also, L^(-1) is the Green function of the squared operator. The fundamental propagator of a first-order fermionic Dirac action would involve D_C^(-1), with additional matrix/numerator structure. A physical readout of (9) remains an observable choice.

## Boundaries and a confining potential change the response

The exact calculation used the whole v line and V=0. On v>=0 the Dirichlet and Neumann Green diagonals for the same radial operator are respectively
\[
G_n^{\rm D}(v,v)=\frac{1-e^{-4nv}}{4n},\qquad
G_n^{\rm N}(v,v)=\frac{1+e^{-4nv}}{4n}.
\tag{10}
\]
Boundary-image terms survive multiplication by the angular degeneracy. The original MC11 space is a half-line, so its boundary cannot be silently replaced by the full-line prototype. Decomposing a full-line reflection-symmetric theory into both parities has its own justification; retaining only even source functions does not automatically retain the full-line kernel.

For the explicitly chosen second-order model
\[
\mathcal L_V=-\partial_v^2+4D^2+V(v),\qquad V\ge0,
\tag{11}
\]
angular separation still works, but the radial factor is now
\[
G_{n,V}(v,v)=\bigl(-\partial_v^2+4n^2+V(v)\bigr)^{-1}(v,v).
\]
The analogue of (9) has coefficients 4n G_(n,V)(v,v), which are not automatically one. A confining potential can be natural physically while changing the exact theta coefficients. Adding a potential to a first-order Dirac Hamiltonian requires its own radial equations; it is not automatically equivalent to adding V in (11).

Thus the author's separation observation is correct and useful. Separation exposes the n-dependent radial response that must be calculated; it does not remove that response from the source matching problem.

## Cylinder geometry versus Euclidean spheres of radius r

The logarithmic product metric in (4) has spheres of fixed metric radius 1/2. Under x=e^(2u) omega, the Euclidean metric is
\[
ds_{\rm E}^2=4e^{4u}\left(du^2+\tfrac14d\Omega^2\right).
\tag{12}
\]
It is conformally related to the product cylinder. If the two-sphere is required to have physical radius r=e^(2u) in ordinary Euclidean space, its angular Dirac operator scales as D/r. Its squared angular scale is n²/r², and spin-connection terms must be carried through the radial operator.

For example, after multiplying a Euclidean radial spinor by r to pass from r²dr to dr, a consistent local expression is
\[
\widetilde{\mathcal D}_{\rm E}=-i\Gamma\partial_r+r^{-1}D,
\qquad
\widetilde{\mathcal D}_{\rm E}^{\,2}
=-\partial_r^2+r^{-2}(D^2+i\Gamma D).
\tag{13}
\]
On the paired ±n angular space, i Gamma D is Hermitian with eigenvalues ±n. The centrifugal coefficients are therefore n(n±1), rather than merely n². This is a differential-expression comparison on r>0; a full operator statement needs an origin/exterior domain. It shows why a flat-space spinor calculation must not simply reuse the product-cylinder Green kernel.

At the level of a frozen-sphere weighted trace, a sphere of radius r yields Q(pi/r²)=A(1/r), while the original source uses A(r)=Q(pi r²). For the complete unit-weight theta source, Jacobi inversion gives
\[
A(r)=r^{-1}A(1/r)+\tfrac12(r^{-1}-1).
\tag{14}
\]
The extra constant and 1/r terms are harmonic away from the origin and drop out under the radial Laplacian used to form Phi. This offers a possible way to connect the two radius conventions using the existing source symmetry. It is only a trace-level identity here. Arbitrary filtered weights do not satisfy the same Jacobi identity, and equation (14) does not derive a coupled radial dynamics, boundary condition or determinant estimate.

## Relation to the actual source and the next question

Equation (9) recovers the generating sum Q(t). The original functions are then
\[
A(r)=Q(\pi r^2),\qquad
p(u)=e^uQ(\pi e^{4u}),\qquad
\Phi(u)=\tfrac18(p''-p).
\tag{15}
\]
The coordinate-dependent evaluation t=pi e^(4u) remains part of this observation map. The Green identity alone does not derive that evaluation from a physical time evolution, nor does it prepare all the f_i and g_j vectors. Encoding scalar source functions in an angular spinor space also requires a specified angular state or an appropriate mixed-state observation; there is no assumed angularly constant spinor replacing a scalar constant function.

These formulas are representation/response identities, not a new positivity mechanism. With a spectral multiplier a_n inserted into (9), the same cancellation produces weighted-square sources. Those controls retain the radial Green mechanism and fail the complete unit-weight source premise. Euler-modified and reflected/positive-primitive controls do not satisfy the literal fixed theta trace, but generic Hilbert/Fock or positive kinetic constructions remain available within their own domains. No control is claimed to fail a new signed estimate. See the [result index](../../../../../../../../result-summaries/README.md), [theta cluster](../../../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md), [collision controls](../../../../../../../../result-summaries/12_collision_controls_and_screening.md), [patterns index](../../../../../../../../avoid/README.md) and [re-realizations caution](../../../../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md).

The next conceptual task is to select what is to be physical: a theory on the product cylinder with a Green-function readout, or a Euclidean radial theory whose spin connection, boundary and potential must be included. The latter should begin with its separated radial operators and derive the observable, rather than choosing a potential solely to cancel a multiplicity.

| Next task | Type | Recommended model | Dependency | Expected output |
| --- | --- | --- | --- | --- |
| MC11-BR01 angular/radial model selection | B — conceptual | Astra; geometry and observable remain undecided | Author's continuation of this discussion | Choose product-cylinder Green response or Euclidean radial response; state the boundary, potential class and source map before a fixed execution request |
| Optional fixed-identity assessment of Note06 | E — analytical assessment | Sol | If the author wants this derivation checked first | Check (5)–(10), the spinor separation in (13), and the scope of (14)–(15), without choosing a new potential |

This narrows the present discussion toward the angular route without activating the earlier oscillator assessment or changing MC11 E04, B01 or E05. All new equations here retain proof-author status pending assessment.
