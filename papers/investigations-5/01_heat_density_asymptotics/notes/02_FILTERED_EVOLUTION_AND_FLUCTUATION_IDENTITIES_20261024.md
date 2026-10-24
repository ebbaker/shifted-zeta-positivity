# Exact filtered evolution and the fluctuation term

24 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), recorded effort max**,
verified from this turn's metadata.

**Status:** elementary identities derived below, with an exact substitution
control; same-assistant calculation only. No theta closure, error estimate,
or independent review is supplied.

This supplies the equation contract for the
[research program](../research-overview/01_AVERAGED_DENSITY_RESEARCH_PROGRAM_20261024.md).
It continues the [opening brainstorm](01_AVERAGED_DENSITY_AND_TWO_TIME_LIMITS_BRAINSTORM_20261024.md)
and the [book](../../../investigations-4/12_height_dependent_heat_contours/manuscript/book.tex),
especially eq:potentialidentities, eq:lapdensity and eq:continuity.
The [result index](../../../../result-summaries/README.md), particularly
[heat geometry](../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md),
and [avoid index](../../../../avoid/README.md), particularly
[target classification](../../../../avoid/01_restating_the_target.md) and
[discarded terms](../../../../avoid/12_term_by_term_matching_and_separate_bounds.md),
apply. This is an exact equation inventory, not a quantitative approximation
milestone by itself.

## 1. The smoothed density and an auxiliary real potential

Fix \(\epsilon>0\), write \(z=x+iy\), and let \(\mathcal F\) be a fixed
translation-invariant space-time average with a real nonnegative kernel
of total weight one and compact support. Spatial-only and time-only
averages are included. Assume the full averaging buffer lies in the
domain of the smooth fields. Put

\[
S=\log(|H|^2+\epsilon^2),\qquad
U=\mathcal F S,\qquad
R=\mathcal F\rho_\epsilon,\qquad
\rho_\epsilon=\frac1{4\pi}\Delta S.
\]

Thus \(R\), not \(|\mathcal F A|^2\), is the unnormalized smoothed density,
and
\[
\Delta U=4\pi R. \tag{1}
\]
The source lift fixes the harmonic and additive data of \(U\).
Solving (1) alone on a finite domain does not fix them.

From the book's equation for \(S_t\),
\[
S_t=-\frac12(S_{xx}-S_{yy})
    -\frac12(S_x^2-S_y^2). \tag{2}
\]
Define the exact local gradient covariances
\[
T_{ij}=\mathcal F(S_iS_j)-U_iU_j,\qquad i,j\in\{x,y\},
\qquad Q=T_{xx}-T_{yy}. \tag{3}
\]
They are central moments over the averaging window at its observation
point. The matrix \(T\) is positive semidefinite, but its difference
\(Q\) need not be positive.

Commuting the fixed average with derivatives in (2) gives
\[
\boxed{
U_t=-\frac12(U_{xx}-U_{yy})
    -\frac12(U_x^2-U_y^2)-\frac12Q.
} \tag{4}
\]
Applying \(\Delta/(4\pi)\) yields the corresponding density equation:
\[
\boxed{
R_t=-\frac12(R_{xx}-R_{yy})
    -\frac1{8\pi}\Delta(U_x^2-U_y^2+Q),
\qquad \Delta U=4\pi R.
} \tag{5}
\]

Equations (4)–(5) are exact filtered identities. They are not yet closed:
the research task is to approximate \(Q\) and retain the source/boundary
information for \(U\). The mixed-sign spatial operator is inherited
from the actual equation; it is not an ordinary forward diffusion.
There is no justification here for setting \(Q=0\), declaring it small,
or assigning it a favorable sign.

## 2. How density fluctuations enter

Two useful diagnostics are
\[
\delta\rho=\rho_\epsilon-R,\qquad
V_\rho=\mathcal F(\rho_\epsilon^2)-R^2\ge0. \tag{6}
\]
The pointwise residual \(\delta\rho\) and the local variance \(V_\rho\)
are different objects. Let \(s=S-U\). Then exactly
\[
\Delta s=4\pi\delta\rho. \tag{7}
\]
Recovering \(\nabla s\) from density fluctuations also requires the
unresolved harmonic boundary data. Their effect is part of the closure.

A smoothing convolution is generally not a projection:
\(\mathcal F^2\ne\mathcal F\). One must therefore retain
\[
\begin{split}
T_{ij}={}&\mathcal F(U_iU_j)-U_iU_j\\
&+\mathcal F(U_i s_j+s_i U_j)+\mathcal F(s_i s_j).
\end{split} \tag{8}
\]
In particular, \(\mathcal F s\) is not assumed to vanish. Equation (8)
keeps resolved-window variation, cross correlations and fluctuation
correlations. A closure based on local density fluctuations must
approximate the contributions needed for \(Q\), rather than append an
unrelated noise term to the density equation.

Candidate inputs include \(V_\rho\), spatial density correlations,
gradient covariances, and the mean potential. Time averaging can require
history-dependent correlations. Whether a simpler local instantaneous
closure suffices is a question to test against the complete theta field.
For (5), the relevant error is in \(\Delta(Q-Q_{\rm model})\), or in its
corresponding weak norm, not just in the pointwise value of \(Q\).

## 3. The current supplies a second exact consistency check

For the book's smooth current,
\[
j=\frac{\epsilon^2H_{zz}\overline{H_z}}
        {\pi(|H|^2+\epsilon^2)^2},\qquad J=\mathcal F j,
\]
one has
\[
R_t+2\Re(\partial_zJ)=0. \tag{9}
\]
If a reduced current \(J_{\rm model}\) is used, the exact missing flux is
\[
\Gamma=J-J_{\rm model},\qquad
R_t+2\Re(\partial_zJ_{\rm model})
=-2\Re(\partial_z\Gamma). \tag{10}
\]
This is another way to retain fluctuation effects. The scalar-potential
and current descriptions must describe the same density evolution.
Defining an effective velocity as \(J/R\) merely repackages the unknown
current; it does not close (9). Keep the undivided smooth current where
the amplitude or its derivatives vanish.

The fixed-window mass balance remains
\[
\frac{d}{dt}\int_\Omega R\,dA
=-\int_{\partial\Omega}{\boldsymbol J}\cdot n\,ds.
\]
An approximate fluctuation term must respect this balance with its
boundary contribution. There is no added physical mass source.

## 4. An exact control: density variance alone misses a correction

Take the noncanonical even heat field
\(H(t,z)=e^{-t}\cosh z\), with \(\epsilon=1\).
At \(t=0,z=0\), average the two points \(x=\pm\log2,y=0\)
with weights \(1/2\). This fixed positive two-point filter is an algebraic
control for the identities, not the proposed final smooth kernel.

At both sample points \(H=5/4\), \(H_z=\pm3/4\), and
\[
\rho_\epsilon=\frac{144}{1681\pi},\quad
S_x=\pm\frac{30}{41},\quad S_y=0,\quad
S_{xx}-S_{yy}=\frac{3200}{1681},\quad
S_t=-\frac{50}{41}.
\]
Consequently
\[
V_\rho=0,\quad U_x=U_y=0,\quad
Q=\frac{900}{1681}.
\]
Equation (4) gives
\[
-\frac12\left(\frac{3200}{1681}+\frac{900}{1681}\right)
=-\frac{50}{41},
\]
exactly. Dropping \(Q\) gives \(-1600/1681\), an error of
\(450/1681\). A closure that automatically sets this correction to zero
whenever \(V_\rho=0\) fails this control. This does not exclude
closures using fuller density, gradient, correlation or boundary data.
The control fails the unchanged canonical theta-source premise.

The remaining [collision-control screen](01_AVERAGED_DENSITY_AND_TWO_TIME_LIMITS_BRAINSTORM_20261024.md#7-what-to-measure-and-what-to-screen)
still applies: all those fields obey their generic filtered identities.
No new certificate replay or collision exclusion is claimed.

## 5. What remains to be established

The research must determine the asymptotics of \(R\), its needed
derivatives and \(Q\); choose and validate a closure; specify compatible
boundary/source data; and quantify the resulting solution error.
If averaging widths or \(\epsilon\) vary, derivative commutators or
regulator terms must first be added to (1)–(10).
The [progress register](../research-progress/01_AVERAGED_DENSITY_RESEARCH_PROGRESS_20261024.md)
tracks these outstanding tasks.
