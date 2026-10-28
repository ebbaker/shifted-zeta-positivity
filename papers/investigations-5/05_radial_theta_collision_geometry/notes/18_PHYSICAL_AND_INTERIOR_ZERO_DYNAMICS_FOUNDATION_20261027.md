# Physical zeros and interior zeros under radial deformation

27 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort max**. Investigation05 chat0006, **Review radial collision progress**.

**Status: elementary local corollaries proved here, with same-assistant checking.** These formulas consolidate the initial deformation into the [working manuscript][manuscript]. They distinguish the zero sets that the new [RDZ program][overview] will study. No bulk zero-count monotonicity, multiple-node classification, or physical collision exclusion is established.

Use [Note17][n17]'s x=log r, lambda=a^2/4>0, w=kappa tanh(kappa x), c=lambda+kappa^2, U=Y'-wY, h=g'-wg, and B=Y'(0)=-8H(t,a). The source g=g_t and response Y do not depend on kappa. Work on compact time, positive-lambda and finite-kappa sets, with the complete selected tails. Three zero sets are different: physical frequency zeros of H; interior spatial zeros of U at fixed t,lambda; and characteristic zeros of a separately specified homogeneous operator. The current forced response does not identify the third with H.

## Physical zero motion is unchanged

Since U(t,0;lambda)=B(t,lambda) for every kappa, the physical zero set and its multiplicities are fixed under auxiliary deformation. At a simple real positive zero, differentiating H(t,a(t))=0 and using H_t=-H_aa gives

\[
\frac{da}{dt}=\frac{H_{aa}}{H_a}.
\]

The chain rule in a=2sqrt(lambda) gives

\[
B_t=-\lambda B_{\lambda\lambda}-\tfrac12B_\lambda,
\qquad
\frac{d\lambda}{dt}=\lambda\frac{B_{\lambda\lambda}}{B_\lambda}+\tfrac12.
\]

The second formula is valid only where B_lambda is nonzero. It is not a rule for continuation through a collision. It gives the same physical velocity in every realization.

## Interior simple zeros can move

At fixed t,lambda, direct differentiation and w'+w^2=kappa^2 yield

\[
U_x=g-cY-wU,\qquad U_\kappa=-(\partial_\kappa w)Y.
\]

For a simple interior zero x(kappa)>0, the implicit-function theorem therefore gives

\[
\boxed{\frac{dx}{d\kappa}
=\frac{(\partial_\kappa w)(x)Y(t,x;\lambda)}
 {g_t(x)-(\lambda+\kappa^2)Y(t,x;\lambda)}}.
\]

The denominator is U_x at the zero and is assumed nonzero. This formula has no general sign conclusion. Interior degeneracies U=U_x=0, endpoint crossings, and limits x->infinity require separate analysis. In particular, an interior double node differentiates in x, whereas a physical multiple zero is U(t,0;lambda)=U_lambda(t,0;lambda)=0. They must not be identified.

## A regular parameter at the undeformed endpoint

The family is even in kappa. At kappa=0 its first kappa derivative vanishes, so that coordinate can conceal nontrivial first variation. On compact x sets, put mu=kappa^2 and use

\[
w=\mu x-\mu^2x^3/3+O(\mu^3),\qquad
\left.\partial_\mu U\right|_{\mu=0}=-xY.
\]

The mu version of the simple-node velocity replaces partial_kappa w by partial_mu w and c by lambda+mu. At mu=0 its numerator is xY. This expansion is local on bounded x sets; it is not a uniform tail approximation.

## Control and verification scope

For Note17's Gaussian-polynomial event at lambda=6,

\[
U_{\kappa,*}=[-8x^3-4w(x)(x^2+1)]e^{-x^2}<0\quad(x>0),
\]

while U(0)=U_lambda(0)=0 for every kappa. Thus absence of interior U zeros does not by itself exclude a multiple physical boundary zero. The control lacks theta's full arithmetic and canonical tails. The generic smooth-source formulas transport the other registered controls on their actual convergence domains; no numerical certificate was rerun, and atomic sources require distributional treatment.

The formulas were checked by direct differentiation, the implicit-function theorem with its nonzero derivative hypothesis, and the Taylor series for tanh. The [manuscript assessment][review] records their scope. They are starting identities for RDZ-02/03, not completion of the proposed nodal-bifurcation study. The [result index][results], [avoid index][avoid], [collision controls][controls] and [scope rule][scope] apply.

[manuscript]: ../radial_deformations_and_zero_dynamics.tex
[overview]: ../research-overview/03_RADIAL_DEFORMATION_AND_ZERO_DYNAMICS_RESEARCH_OVERVIEW_20261027.md
[n17]: 17_RADIAL_DARBOUX_SYSTEMS_PRESERVING_PHYSICAL_OBSERVATION_20261027.md
[review]: ../reviews/11_INITIAL_DEFORMATION_MANUSCRIPT_AND_PROGRAM_ASSESSMENT_20261027.md
[results]: ../../../../result-summaries/README.md
[avoid]: ../../../../avoid/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[scope]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
