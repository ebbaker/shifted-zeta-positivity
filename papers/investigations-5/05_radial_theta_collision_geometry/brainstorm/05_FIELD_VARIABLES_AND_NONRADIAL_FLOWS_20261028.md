# Field variables and nonradial conservative flows

28 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance, **gpt-6-astra (Codex), actual recorded reasoning effort max**, chat0013, **Review theta collision strategy**.

**B — conceptual discussion.** Edward Baker proposes keeping the usual radial initial field while allowing nonradial auxiliary dynamics, and asks for physical and geometric intuition about the variables before choosing more equations. This note explains the existing variables, why the current solution stays radial, and one simple conservative alternative. It does not replace the fixed feedback candidate or complete the separate B02 estimate task. The [live progress register](../research-progress/04_CONSERVATIVE_THETA_FLOW_RESEARCH_PROGRESS_20261028.md) retains those statuses.

The basic distinction is between the observation parameters (t,a) and the auxiliary position X. The first pair selects a number H(t,a). The second tells us where its signed contributions are placed in a three-dimensional representation. Auxiliary time s rearranges those contributions while leaving their total fixed.

| Symbol | Meaning | Geometric interpretation |
| --- | --- | --- |
| u>=0 | The original integration variable in the theta transform | Labels contributions before the three-dimensional realization |
| Phi(u) | The canonical positive theta source on the half-line | Gives the original weight of each contribution |
| t | Newman deformation parameter | Reweights the source by exp(t u^2); it changes H itself |
| a | Observation frequency | Sets the oscillations of cos(a u), hence the pattern of positive and negative contributions |
| X=(x,y,z) | Auxiliary spatial position | A point in the constructed three-dimensional representation |
| r=abs(X) | Radius in that auxiliary space | Initially linked to the original source variable by r=exp(2u) |
| s | Auxiliary evolution parameter | Moves or spreads a representation of the same H(t,a) |
| j_s(t,a;X) | Signed contribution per unit volume | A signed density, not a probability density |
| bold J_s | Spatial flux of the signed density | Describes how contributions cross surfaces as s increases |

The source formula is

\[
 H(t,a)=\int_0^\infty q_t(u)\cos(au)\,du,
 \qquad q_t(u)=e^{tu^2}\Phi(u).
\]

Increasing a makes the cosine oscillate more rapidly across u. Increasing t emphasizes larger u relative to smaller u; it need not increase H at a nonzero frequency, because the contributions have signs. The Newman equation is H_t=-H_aa. This differs from the auxiliary forward spatial heat equation: changing t changes the observed function, whereas changing s preserves the chosen observation.

The initial three-dimensional construction places each original contribution uniformly over a spherical shell. Since

\[
 r=e^{2u},\qquad 4\pi r^2\,dr=8\pi r^3\,du,
\]

the exact initial density is

\[
 j_0(t,a;X)=\mathbf1_{r\ge1}
       \frac{q_t(\tfrac12\log r)}{8\pi r^3}
       \cos\!\left(\frac a2\log r\right).
\]

Thus the contribution of a thin shell is exactly q_t(u)cos(au)du. The factor 1/(8pi r^3) divides by the shell's volume; it is not an additional theta weight. The empty initial ball arises because u starts at zero, which maps to r=1. It is not a reflecting boundary of the auxiliary flow.

One useful picture is a cloud with positive and negative signed density, represented by two colors. Its total signed amount is H(t,a). Every fixed (t,a) gives a different initial cloud. Moving s changes the cloud's shape while retaining its total. After redistribution, r remains a spatial radius, but log(r)/2 no longer identifies the original source label carried by the material arriving there. Diffusion mixes contributions from different starting shells, and can populate r<1.

The conservation equation is

\[
 \partial_sj_s+\nabla_X\cdot\mathbf J_s=0.
\]

For any fixed region Omega it says that the rate of change of the signed amount inside is minus the outward flux through its boundary. For the complete space, decay sufficient to remove the flux at infinity gives

\[
 \int_{\mathbb R^3}j_s(t,a;X)\,dX=H(t,a).
\]

Conservation does not require spherical symmetry. Nor does it require retaining each shell's contribution separately. The flux may carry contributions between both radii and angles.

The current heat choice is $\mathbf J=-\nabla_Xj$, hence $\partial_sj=\Delta_Xj$. It smooths spatial variation. The Cartesian Laplacian is $\partial_x^2+\partial_y^2+\partial_z^2$; it treats all directions equally.

The current radiality follows from **radial initial data, rotationally invariant dynamics, and uniqueness together**. For a rotation O, the field j_s(OX) solves the same heat equation with the same initial data. Uniqueness therefore identifies it with j_s(X). The radial feedback profile and the rotational scalar integrals used in its coefficient preserve the same argument. A uniquely solvable deterministic nonlinear equation that commutes with rotations also retains exact radial data. Nonlinearity alone does not create angular dependence; an instability can amplify a perturbation but does not supply one to exactly symmetric data.

The standard heat kernel, smoothing, and uniqueness inputs are in [Hunter, Section5.1](https://www.math.ucdavis.edu/~hunter/pdes/pde_notes.pdf), formulas(5.5)–(5.6), Theorems5.5 and5.12; the last applies to the L2 initial field by taking the Sobolev exponent to be zero. The rotation argument above is an elementary application. The [existing reference record](../references/10_PROJECTED_EVOLUTION_AND_ELLIPTIC_RESPONSE_20261027.md) retains the reading copy and scope.

For genuinely nonradial motion from the same initial field, a simple choice is

\[
 \boxed{\partial_sj+y\,\partial_xj=\varepsilon\Delta_Xj},
 \qquad\mathbf b=(y,0,0),\qquad\varepsilon>0.
\]

The velocity b slides different y-layers in the x direction at different speeds. This is shear. Its divergence is zero, and the flux is bold J=bj-epsilon grad j, so the complete signed integral is conserved. With t and a independent of these coefficients, the same propagator preserves the integrals of all admitted frequency derivatives and retains the Newman parameter identity. The initial source is unchanged.

For radial smooth data f(r), away from the raw unit-sphere jump, the initial evolution is

\[
 \left.\partial_sj\right|_{s=0}
 =\varepsilon\left(f''+\frac2r f'\right)
       -\frac{xy}{r}f'.
\]

The last term varies with angle, so this equation leaves the radial class. For the raw field the equation is understood mildly or distributionally at its jump. With diffusion omitted, the exact characteristic formula is

\[
 j_s(x,y,z)=f\!\left(\sqrt{(x-sy)^2+y^2+z^2}\right).
\]

Its spherical level surfaces become sheared ellipsoids, and the transformation has determinant one. Pure shear preserves every Lp norm for which the initial field is in Lp; changing this geometry alone is not a new scalar estimate. With diffusion present, transport creates spatial gradients and diffusion smooths them. For smooth decaying fields the exact energy identity is

\[
 \frac{d}{ds}\|j_s\|_2^2=-2\varepsilon\|\nabla j_s\|_2^2.
\]

These identities show the allowed freedom, not a theta separation result. Rigid rotation alone would leave the radial field unchanged: its velocity is tangent to spheres and divergence-free. Shear actually deforms the shells. Unequal diffusion coefficients, such as partial_x^2+2partial_y^2+3partial_z^2, give another simple choice that breaks rotational symmetry. A deterministic scalar flow with no asymmetric coefficient, auxiliary state, boundary condition or initial perturbation cannot choose a direction from exactly radial data under the uniqueness premise. One can also consider a family of orientations; rotating the entire shear construction gives an equivalent realization for the radial source.

The later feedback notation introduces a second distinction: **W is a two-component field on three-dimensional space; it is not a spatial velocity**. At a chosen observation p=(T,A),

\[
 U_s(X)=j_s^p(T,A;X),\qquad
 V_s(X)=\left.\partial_a j_s^p(T,a;X)\right|_{a=A},\qquad W=(U,V).
\]

Capital T and A simply select values of t and a. U is the contribution density; V is its sensitivity to changing observation frequency within the same propagator family. Moving the mark p itself changes the feedback path and is a different derivative. Their integrals are H(T,A) and H_a(T,A). A collision means **both total signed amounts vanish**. No particular spatial point is singled out by this condition, and neither field has to be identically zero. The physical event belongs to parameter space (t,a); the cloud in X displays a representation of its cancellations.

The energy E=integral(U^2+V^2) measures size without cancellation of signs. The gradient energy G=integral(abs(grad U)^2+abs(grad V)^2) measures spatial variation. The prescribed vector v is a spatial drift profile; in the current feedback the actual transport velocity is -alpha v, pointing inward. The scalar alpha=2G/D sets its compression strength to compensate the energy lost to diffusion, with D=integral(div v)abs(W)^2. These meanings should precede any proposal to optimize or replace the feedback.

For reference, adding the same unit shear to the prepared feedback pair gives

\[
 \partial_sW+y\partial_xW
   =\Delta W+\alpha\operatorname{div}(vW),
 \qquad\alpha=2G/D.
\]

On a smooth interval with the required decay, the divergence-free shear contributes zero to E', so E'=-2G+alpha D=0 still holds. Its additional contribution to G' is instead

\[
 -2\sum_{\ell=1}^2\int
       (\partial_xW_\ell)(\partial_yW_\ell)\,dX.
\]

This mixed-gradient term has no fixed sign. The existing collision-deadline proof cannot be transferred unchanged: shear alters the contraction estimate. Nonradial fields also have angular gradient energy,

\[
 G=\int_0^\infty\int_{S^2}
       \big(r^2|\partial_rW|^2+|\nabla_{S^2}W|^2\big)\,d\omega\,dr,
\]

so the manuscript's radial source-gradient formula would require the additional angular term and the changed commutator. These are conditional identities for the proposed equation, not a proved nonlinear lifespan or collision theorem.

The next conceptual decision, if this alternative is pursued, is which feature of the two signed clouds should become easier to estimate: their overlap, angular variation, gradient production, or a particular source-dependent signed interaction. This note does not choose an unexplained objective or authorize a numerical campaign. Making that geometric objective explicit should come before adding feedback terms. The manuscript is unchanged.

The [result index](../../../../result-summaries/README.md), [collision controls](../../../../result-summaries/12_collision_controls_and_screening.md), and [avoid index](../../../../avoid/README.md), especially [coordinate re-realizations](../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md) and [scoped exclusions](../../../../avoid/07_scoped_exclusions_read_as_universal.md), govern the interpretation. The exact Gaussian-polynomial collision control satisfies the shear conservation and energy identities on its moment domain; it fails the unchanged complete theta source, which those generic identities have not used to separate it. The applicable weighted-square, reflected, primitive and Euler-factor controls retain their respective failed full-coefficient, canonical-source or conductor premises from the control register. Atomic controls remain outside the stated smooth feedback class. None is excluded by introducing shear. The elementary calculations here have same-assistant checking only; no new collision exclusion, comparative gain, simulation or independent review is claimed.
