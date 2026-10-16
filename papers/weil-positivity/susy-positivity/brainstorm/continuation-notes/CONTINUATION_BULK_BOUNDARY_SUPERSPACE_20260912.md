# Continuation: Weil positivity, bulk–boundary realizations, and superspace

Prepared 12 September 2026 for continuation in a new chat.

## Where the discussion stands

The background now presents the common goals and mathematical framework of the SUSY positivity research program. The existing manuscript is the positive-factorizations attempt, one approach within that program. The user wants the general mathematical construction explained before examples, with every function, parameter, and map introduced explicitly.

The most recent discussion clarified that the proposed bulk for the **full Weil form** remains to be constructed. “Bulk” means additional degrees of freedom introduced into a model; it does not mean everything outside the input interval. It can be a geometric extension, an auxiliary-field system, or potentially a system formulated on superspace.

The user then asked: “It could also be a superspace right?” The answer was yes, as a possible further construction, with a distinction between a superspace description and the positive Hilbert-space energy needed for the positivity argument. The user requested this continuation file to carry that discussion into a new chat.

**Status:** the general bulk–boundary explanation has already been expanded in the background TeX and compiled PDF. The latest superspace discussion is recorded here; it has **not** yet been inserted into those files. No particular superspace action or full arithmetic bulk completion has been constructed.

## Files to read

Start with the [program README](README.md). All local links below resolve within the repository.

The current standalone background files are:

- [background_section.tex](background_section.tex): the authoritative substantive program background section.
- [background.tex](background.tex): the standalone wrapper, packages, and bibliography. It inputs the section; it is not a redundant alternative version.
- [background.pdf](background.pdf): the standalone program background. Its earlier preview had nine pages; fresh build and layout results are recorded in [the reorganization record](REORGANIZATION_20260912.md).

Related files:

- [Research program overview](PROGRAM_OVERVIEW.md): the high-level overview, already updated earlier in the conversation.
- [Positive-factorizations manuscript](attempts/positive-factorizations/manuscript.tex): its mathematical content is unchanged by the program reorganization; its repository references have been repaired. Read its discussion of supersymmetric extensions, positive component spaces, and the gamma kinetic tower.
- [Weil-depth manuscript](../shifted-zeta/weil-depth/manuscript/finite_horizon_weil.tex): the direct project source for the diagonal contraction proposition cited in the background.

The repository has undergone user-directed reorganization. Read current files before editing, preserve unrelated changes, and do not assume old folder locations. Files under the separate ChatGPT project mirror's sources/ directory are read-only reference material.

## The proposed superspace interpretation

A possible geometric bulk could have ordinary coordinates \(x,y\), together with anticommuting Grassmann coordinates \(\theta,\bar\theta\). Schematically, its fields could be packaged into a superfield

\[
\mathcal U(x,y,\theta,\bar\theta)
=u(x,y)+\theta\chi(x,y)+\bar\theta\widetilde\chi(x,y)
+\theta\bar\theta\,b(x,y).
\]

This is an illustrative component expansion, not a specified supermultiplet or action. The number and type of odd coordinates, reality conditions, transformation laws, and supersymmetry algebra would have to be chosen for an actual model. Adding Grassmann coordinates alone does not establish a supersymmetry of its dynamics.

The original input \(f\) could be identified with a distinguished bosonic component on the ordinary boundary:

\[
(\operatorname{Tr}\mathcal U)(x)=u(x,0)=f(x).
\]

This notation includes both restriction to \(y=0\) and selection of a component. A boundary superfield retaining its odd-coordinate dependence is a different object. Other components need their own boundary conditions; these must be compatible with whatever supersymmetry the model is intended to preserve.

The RH criterion requires every admissible test input \(f\). A construction restricted to special supersymmetric boundary profiles would therefore not, by itself, cover that criterion.

For a half-plane bulk, the ordinary boundary is the whole \(x\)-line, and one can prescribe the zero extension \(\widetilde f\) there. The interval is then the support of the nonzero prescribed data, not the entire geometric boundary. For a strip \(I_L\times(0,\infty)\), the interval is a lower boundary segment and the side conditions must also be supplied.

The extra odd directions are algebraic directions, not ordinary spatial directions in which one takes a distance to the interval. A formulation using only an interval with odd directions also does not automatically make that interval a geometric boundary of a larger ordinary space.

### How positivity would be interpreted

The background's expression

\[
\inf_{\operatorname{Tr}U=f}\mathcal E[U]
\]

is a minimization of real, nonnegative energies. Grassmann-valued quantities do not have the ordinary ordering required for that minimization. A superspace proposal therefore needs a precise translation into a component-energy or positive Hilbert-space formulation before this variational statement can be used.

In the Hilbert-space formulation, fermionic states can have ordinary positive norms. For a densely defined closed factor \(A:\mathcal H_{\mathrm B}\to\mathcal H_{\mathrm F}\), one has the graded construction

\[
\mathscr D=
\begin{pmatrix}0&A^*\\ A&0\end{pmatrix},
\qquad
\mathscr D^2=
\begin{pmatrix}A^*A&0\\0&AA^*\end{pmatrix}\geq0,
\]

on the appropriate domains. The labels “bosonic” and “fermionic” indicate the grading; they do not assign a negative Hilbert norm to the fermionic sector.

This is the kind of operator structure already used in the positive-factorizations attempt. A superspace model would be an additional description or construction whose relation to that structure must be demonstrated. Berezin integration and supertraces do not themselves supply a positive energy or prove positivity of the desired boundary observable.

The research target remains an exact identification of the resulting boundary energy with the full Weil form. Supersymmetry could help constrain the couplings and factorization, but a nonnegative supersymmetric Hamiltonian alone does not establish the arithmetic identity.

References consulted:

- [David Tong, superspace and superfields](https://www.damtp.cam.ac.uk/user/tong/susy/susy3.pdf): commuting and anticommuting coordinates and component descriptions.
- [David Tong, Supersymmetric Quantum Mechanics](https://www.damtp.cam.ac.uk/user/tong/susy/susyqm.pdf), especially §1.1: the supercharge algebra and positivity of the Hamiltonian.

## The general bulk–boundary mechanism already in the background

Fix \(\omega,L\) and a boundary input \(f\). The current section distinguishes:

| Object | Meaning |
| --- | --- |
| \(\operatorname{Tr}U=f\) | Extract the prescribed boundary data from a bulk configuration. |
| \(\mathcal P f=U_{\min}\) | Extend the input into the bulk by solving the constrained minimization problem. |
| \(\mathcal C U\) | Extract bulk energy amplitudes, with \(\mathcal E[U]=\|\mathcal C U\|^2\). |
| \(Af=\mathcal C\mathcal P f\) | The factor obtained after solving for the minimizing field. |
| \(\mathsf S=A^*A\) | The boundary response operator when the closed-form and operator-domain hypotheses hold. |

The trace map is not a matrix trace. In a geometric model it can restrict a field to an edge; in an auxiliary-channel model \(U=(f,u_0,u_1,\ldots)\), it is simply projection onto the distinguished component \(f\).

One has \(\operatorname{Tr}\mathcal P=I\) on allowed boundary inputs. In general \(\mathcal P\operatorname{Tr}\) replaces a field by its equilibrium extension rather than returning the original field.

If \(e\) is the sesquilinear form of the bulk energy, the minimizing extension satisfies

\[
\operatorname{Tr}(\mathcal P f)=f,
\qquad
e(h,\mathcal P f)=0
\quad(h\in\ker\operatorname{Tr}).
\]

These are the boundary condition and the weak interior equilibrium equation. They imply

\[
\mathcal E[\mathcal P f+h]
=\mathcal E[\mathcal P f]+\mathcal E[h].
\]

The section states sufficient hypotheses for existence, uniqueness, and linearity; positivity alone does not guarantee attainment of the infimum.

It also derives the finite block calculation

\[
u_{\min}=-H_{\mathrm{ii}}^{-1}H_{\mathrm{ib}}f,
\qquad
\mathsf S=H_{\mathrm{bb}}
-H_{\mathrm{bi}}H_{\mathrm{ii}}^{-1}H_{\mathrm{ib}},
\]

assuming the full block matrix is nonnegative and the interior block is positive definite. This is the Schur complement. It explains how local bulk couplings can give a nonlocal boundary operator after elimination.

For geometric systems, a corresponding response can be a Dirichlet-to-Neumann map. The trace reads the boundary value; the response reads the normal flux after solving the bulk equation. The background now cites [Kwaśnicki and Mucha](https://arxiv.org/abs/1707.02475) for positive extension realizations and their variational formulation.

Equation 1.14 is explicitly a matching **target**:

\[
Q_{\omega,L}[f]\stackrel{\mathrm{target}}{=}
\mathcal E^{\mathrm{eff}}_{\omega,L}[f]
:=\inf_{\operatorname{Tr}U=f}\mathcal E_{\omega,L}[U].
\]

The bulk system is independently specified first; its reduced energy must then be computed and proved equal to the arithmetic form.

## What bulk is already concrete

For the gamma kinetic contribution, the positive-factorizations attempt has an established explicit positive auxiliary-field construction within the stated kinetic scope. With \(a_k=2k+\tfrac12\),

\[
\mathcal E^{\mathrm{kin}}[\widetilde f,(u_k)]
=\sum_{k\geq0}\frac2{a_k}
\int_{\mathbb R}
\left(|\widetilde f-u_k|^2+a_k^{-2}|u_k'|^2\right)\,dx.
\]

The fields \(u_k\) vary on the whole line while \(f\) is fixed. Their equilibrium equations and minimizing Fourier transforms are

\[
(1-a_k^{-2}\partial_x^2)u_k=\widetilde f,
\qquad
\widehat u_k(\tau)=
\frac{a_k^2}{a_k^2+\tau^2}\widehat f(\tau).
\]

The minimum gives the gamma kinetic form \(K[\widetilde f]\), and the background explicitly identifies its trace, minimizing extension, and amplitude map. Cutting off the auxiliary fields at the input endpoints changes the problem.

This construction does not yet reproduce the full Weil form. The additional normalization, pole terms, and prime delays still need a common positive realization.

## Earlier mathematical clarifications to preserve

The input interval is \(I_L=(-L/2,L/2)\). The direct classical criterion is

\[
\mathrm{RH}\iff Q_{0,L}[f]\geq0
\quad\text{for every }L>0,\quad
f\in C_c^\infty(I_L).
\]

Complex-valued test functions are allowed. Positivity means nonnegativity; a uniform strictly positive margin is not required. The form-domain extension and the full arithmetic expression are given in the TeX.

The zero in \(Q_{0,L}\) fixes the zeta shift at \(\omega=0\). Requiring \(Q_{\omega,L}\geq0\) for every positive shift and every length is not this RH criterion. The shift is an auxiliary parameter, not automatically a geometric bulk coordinate.

For the transfer \(V_{\omega,L}\) and causal generator \(G_{\omega,L}\), equation 1.7 starts with a fixed test input:

\[
\frac{d}{d\omega}(V_{\omega,L}f)
=-G_{\omega,L}V_{\omega,L}f,
\qquad
\frac{d}{d\omega}\|V_{\omega,L}f\|_{L^2(I_L)}^2
=-2Q_{\omega,L}[V_{\omega,L}f].
\]

The norm is the ordinary unweighted \(L^2\) norm in \(x\). The brackets in \(Q[Vf]\) denote evaluation of a quadratic functional, whereas \(GV\) is composition of linear operators.

The background then makes \(f\) implicit in the operator evolution and derives the operator energy balance. With \(D_{\omega,L}=I-V_{\omega,L}^*V_{\omega,L}\),

\[
\partial_\omega V_{\omega,L}=-G_{\omega,L}V_{\omega,L},
\qquad
\partial_\omega D_{\omega,L}
=V_{\omega,L}^*(G_{\omega,L}^*+G_{\omega,L})V_{\omega,L}.
\]

The second right-hand side is specified in the form sense, with the bounded product-rule expression provided at positive shift. At zero, derivatives are interpreted on the test core and the initial limit is strong; no operator-norm derivative at zero is asserted.

The cumulative identity is

\[
\langle f,D_{\omega,L}f\rangle
=2\int_0^\omega Q_{s,L}[V_{s,L}f]\,ds,
\qquad
Q_{0,L}[f]
=\lim_{\omega\downarrow0}
\frac{\langle f,D_{\omega,L}f\rangle}{2\omega}.
\]

Proposition 1.1 states a sufficient contraction route: an unbounded sequence \(L_j\to\infty\) and positive shifts \(\omega_j\downarrow0\) with \(\|V_{\omega_j,L_j}\|\leq1\) imply RH. Its direct project source is the **Weil-depth manuscript**, subsequently used in storage-depth; do not attribute that precise proposition to Suzuki. The background includes its proof and citation.

Equation 1.12 is the central factorization target \(Q_{0,L}[f]=\|A_{0,L}f\|^2\); equation 1.13 displays a shifted factorization on a specified parameter region. The positive-factorizations attempt does not establish either a full central factorization at arbitrary lengths or the unbounded contraction sequence.

## Build and validation

From this program directory, run `latexmk -pdf -interaction=nonstopmode -halt-on-error background.tex`. Build the attempt from `attempts/positive-factorizations/` with the same command applied to `manuscript.tex`. See the [attempt README](attempts/positive-factorizations/README.md) for replay commands that preserve historical diagnostics. The [reorganization record](REORGANIZATION_20260912.md) distinguishes the fresh verification from historical records.

## How to continue

The next chat should use the current background as its starting point and develop the superspace possibility without treating it as an established completion. A useful opening message is:

> Read this continuation note and the linked background section. Continue our discussion of a possible superspace bulk: explain how its superfields, boundary component, supersymmetry, and positive component or Hilbert-space energy would fit the existing variational construction. Keep the concrete gamma tower distinct from a proposed completion of the full Weil form.

The user's notation preference is to show an equation acting on \(f\) first, then derive its operator version and explain that \(f\) has become implicit. Avoid introducing several new variables without a direct correspondence. Keep the general mechanism ahead of examples, and distinguish established identities, sufficient conditions, and proposed constructions.
