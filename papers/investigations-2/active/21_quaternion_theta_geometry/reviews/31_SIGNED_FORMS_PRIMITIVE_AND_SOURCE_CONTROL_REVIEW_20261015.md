# Review of the signed form and theta primitive continuation

15 October 2026, America/New_York. Prepared for Edward Baker with substantial LLM assistance. Recorded coordinating model **gpt-6-astra**, reasoning effort **ultra**, verified from session metadata. Three independently prompted internal agents derived separate components and cross-reviewed another component. The coordinator also checked the main formulas directly. All used the inherited model and effort. This is internal LLM review, not external peer review or formal verification.

The review covers [Note 51](../notes/04_octonionic_reductions/51_POLARIZED_HODGE_DISK_AND_CENTERED_SOURCE_BOUNDS_20261015.md), [Note 52](../notes/05_theta_correlation_kernels/52_POSITIVE_THETA_PRIMITIVE_AND_DIFFERENTIAL_CLOSURE_20261015.md), and [Note 53](../notes/05_theta_correlation_kernels/53_SOURCE_CONCAVITY_AND_POSITIVE_TIME_COLLISION_CONTROL_20261015.md), integrated in [Note 54](../notes/00_research_coordination/54_SIGNED_FORMS_AND_POSITIVE_THETA_PRIMITIVE_CONTINUATION_20261015.md). Their scope is integrated positivity, an auxiliary theta identity, and applicability controls. The stationary physical-energy estimate remains unproved.

## Disk and centered weighted bounds

The complex-normal identity \(\ell_f=\frac12\partial_y^2|f|^2\) has the correct sign. Expanding in the scaled disk coordinate verifies the Dirichlet completion, including the boundary coefficient \(1/(2R)\). The triangular even-polynomial sequence has the exact ratio \(-2N/(2N+3)\), establishing sharpness in the general holomorphic class even under center stationarity. This does not establish theta sharpness or a physical-energy boundary allowance.

The full-frequency Hermitian product has prefactor \(1/2\) with density \(\rho=w/2\); folding the four quadrants gives the prefactor \(1/4\) in the half-line formula. The odd-branch subtraction is controlled by monotonicity of the nonnegative Fourier transform of the weight. Strict positivity holds on an open region near equal positive frequencies. The complete source moments and integrability of the weight justify every interchange for compact heat/displacement sets. Translation introduces both stated cosine factors and breaks the comparison.

The cosine-source control solves the exact backward heat equation. Its full stationary ratio, the disk mean \(I_1(2kR)/(kR)\), and the critical-radius expansion \(R^2=2(T-t)+O((T-t)^2)\) all check. It is explicitly a positive atomic-source control, not the smooth theta source. Note 53 supplies a separate smooth control.

## Positive theta primitive and closure obstruction

The complete modular-even primitive satisfies \(P=e^u+2\psi\), \(\Phi=(P''-P)/16=(\psi''-\psi)/8\), and \(\psi'(0)=-1/2\). Integration by parts gives every sign and factor in the reconstructed field, including the indispensable constant \(1/2\). The growing modular-even primitive cannot replace the decaying half-line primitive inside a positive-time integral.

For \(0\le t\le1/2\), the source-term estimate \(f_n''/f_n\ge9q_n^2-16q_n>0\) is valid for all \(u\ge0\), \(n\ge1\). The formula with \(1-\cos(xu)\) proves strict positivity of \(J\) for all nonzero real \(x\), while \(x=0\) follows directly. This is consistent with [Csordas, Theorem 3.4](https://arxiv.org/pdf/1309.0055): the even primitive has a cusp, unlike the smooth original theta source.

The first two endpoint terms give \(J=1/(2x^2)-(1+6t)/(2x^4)+O_T(x^{-6})\). The uniformly bounded fifth endpoint derivative and integrable sixth derivative pay the remainder. The contrast with exponential physical-jet decay excludes uniform or polynomial-in-height separate norm budgets; it does not exclude coefficients merely locally bounded at finite height.

The derivative asymptotic \(w_t^{(m)}/w_t\sim(-4\pi)^m e^{4mu}\) follows from the complete first-index asymptotic at each fixed differentiation order. A highest-derivative polynomial coefficient cannot cancel against lower derivatives. The invertible Fourier correspondence \(x\mapsto i\partial_u\), \(\partial_x\mapsto iu\) therefore proves the stated finite rational-jet obstruction after denominators are cleared. It concerns identities on open spectral intervals, not arbitrary identities on a stationary set or signed inequalities.

One wording correction was made during cross-review: the conjugated operator \(-4t^2\partial_x^2-1\) has lower spectral edge \(-1\), and its quadratic form takes both signs. It does have a lower bound; it lacks the nonnegative sign needed here.

## Smooth collision control and literature scope

Independent expansion verifies the Gaussian-polynomial transform, its discriminant, \(T_0=(8-\sqrt{10})/10\), \(x_c^2=4+7\sqrt{10}/5\), and the positive second derivative at the double zero. The two-equation parameter Jacobian has determinant \(-h_2^2\), so the collision persists for all sufficiently small positive damping. Gaussian domination near the undamped event supplies the needed parameter convergence; the optional one-sided \(C^1\) extension is legitimate and does not use a divergent negative-damping integral.

The series for \(\cosh(4\sqrt v)\) gives \(C'(v)\ge8\), \(C''(v)>0\). Together with the explicit \((\log Q)''\), it proves both strict square-variable log-concavity and uniform ordinary strong log-concavity in the declared time range. Double-exponential decay pays all heat and spectral derivatives. Once a positive damping is fixed, the entire stationary-predecessor argument uses that same complete source. The ratio \(-1/(T-t)+O(1)\) follows from the heat equation on the genuine stationary curve.

The primary [Csordas paper](https://arxiv.org/pdf/1309.0055) was checked for Definition 1.2, Theorems 3.5 and 4.2(b), Remark 2.1, and Example 3.12. These justify the stated distinction between admissible/log-concave kernels and positive-definite kernels; they do not supply the missing Fourier sign. No literature novelty claim is made for the control or the elementary methods.

## Disposition

The analytic claims above passed the internal checks. No numerical pilot, new finite certificate, or unbounded theta sign theorem is asserted. No manuscript changes are part of this continuation. The author's clarification that the 2014 documents were unpublished and knowingly incomplete is recorded in Review 30 and Note 54. Their exploratory ideas, rather than publication claims, motivated this work.
