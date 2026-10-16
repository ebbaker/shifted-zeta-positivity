# Initial research program for stein and susy correlations

13 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: `gpt-6.1-sol`; reasoning effort: ultra.
Status: initialized, awaiting Claude review. No research run or new sign
certificate is reported by this note.

This project develops [brainstorm card 11](../../../brainstorm/LIFTED_THETA_SYMMETRY_SEARCH_CODEX_20261013.md#11-supersymmetric-identities-and-a-theta-stein-kernel).
Its question is whether an exact nonlinear partner of the complete theta
source carries a signed correlation absent from generic SUSY positivity.

## Actual state generator and observation

Use the complete even extension of
\[
\Phi(u)=\sum_{n\ge1}(2\pi^2n^4e^{9u}-3\pi n^2e^{5u})
e^{-\pi n^2e^{4u}},\qquad u\ge0.
\]
The unnormalized state is \(m_t=e^{tu^2}\Phi_e\), its generator is
\(\mathscr Gm=u^2m\), and the physical projection is
\[
\mathcal P_xm=\tfrac12\int_{\mathbb R}e^{ixu}m(u)du=H_t(x).
\]
Thus \(\partial_tH_t=-\partial_x^2H_t\). Set \(Z_t=H_t(0)>0\),
\(\rho_t=m_t/(2Z_t)\), \(C_t=H_t/Z_t\), and \(\mu_2=\mathbb E u^2\).
For \(g_t=\sqrt{\rho_t}\), the actual tangent is
\(\dot g_t=(u^2-\mu_2)g_t/2\). The positive Hamiltonian annihilating this
moving state is not its Newman-time generator.

## Established seed and precise objective

With \(W_t=-\log\rho_t\) and \(B_t=\partial_u+W_t'/2\), the
[existing SUSY scout](../../../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/03_susy_dirac_hodge/notes/1_MOVING_THETA_GROUND_STATE_WARD_RESIDUAL_AND_GAP_LIMIT_20261010.md)
gives \(B_t\dot g_t=ug_t\). The classical
[Stein identity, equations (5)–(6)](https://arxiv.org/html/1804.03926v3)
supplies the complementary source-exact insertion
\[
\tau_t(u)=\rho_t(u)^{-1}\int_u^\infty v\rho_t(v)dv,
\quad B_t^\dagger(\tau_tg_t)=ug_t.
\]
Evenness gives mean zero, an even positive \(\tau_t\), and vanishing endpoint
products. For \(T_t(x)=\mathbb E[\tau_t e^{ixu}]\), integration by parts
yields \(C_t'=-xT_t\). Complete theta decay pays its differentiated
integrals uniformly on compact time intervals.

The objective is a theta-specific source relation proving, for \(x>0\),
\[
C_tT_t'\ge0\quad(T_t=0),\qquad
T_t(2T_t'+xT_t'')\le0\quad(T_t+xT_t'=0).
\]
These are exactly the two physical stationary signs in the
[all-multiplicity criterion](../../../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/17_enlarged_state_transport/notes/5_STATIONARY_SIGN_CRITERION_AND_THETA_TARGETS_20261010.md).
They require complete predecessor neighborhoods, not a sign only at a
hypothetical collision. At \(x=0\), \(H_t(0)>0\) excludes a collision
directly.

## First bounded task checks and stopping condition

First derive a complete expression for \(\tau_t\rho_t\), including modular
or paired-source transformations and every boundary term. Choose one already
recorded genuine stationary cell and one smooth positive double-zero control.
Enclose \(T_t,T_t',T_t''\), their physical normalization, and the relevant
candidate bands. Compare the two signed products with a full interval error
payment. If time derivatives are used, include \(\partial_t\tau_t\).

Review the source identity and integration domain before running numerics.
Check parity, the factor two, Newman-time orientation, and both stationary
restrictions. Any promising estimate must distinguish theta from the control
and identify which source property supplies that distinction.

Continue after a new signed relation or a quantified source comparison pays
the conditional product. Stop this first task if it produces only positivity
of \(\tau_t\), a spectral gap, or a smaller bulk Gaussian-score discrepancy.
Those properties are shared by positive collision controls. The
[regular cohomological-quartet obstruction](../../../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/04_cohomological_localization/notes/1_EXACT_THETA_SUPERSPACE_AND_REGULAR_COMPLETION_OBSTRUCTION_20261010.md)
also remains in force: this insertion is not automatically a protected
localization observable. A different completion needs its own exact
source, domain and reduction proof.
