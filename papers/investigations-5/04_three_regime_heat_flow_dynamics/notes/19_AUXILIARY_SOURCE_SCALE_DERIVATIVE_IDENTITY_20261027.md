# Auxiliary source scale derivative identity

27 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort max**. Chat0006, thread `01a17e68-028c-7472-8317-c38eefa4c2f0`. The auxiliary exponential-parameter observation was proposed by Edward Baker in this conversation.

**Status: exact elementary identities checked by direct differentiation.** This records the proposed coupling of the two terms of the canonical theta source. It supplies no new source inequality or exclusion theorem. The [result index][results], particularly [theta identities][theta], and [avoid index][avoid], particularly [coupled estimates][coupled] and [target classification][classify], fix its research status.

## The parameter derivative

Choose a dimensionless parameter s with Re(s)>0 and recover the original exponential at s=1. Let

\[
B_n(s,u)=3\pi n^2e^{5u}\exp(-\pi s n^2e^{4u}),
\qquad B(s,u)=\sum_{n\ge1}B_n(s,u).
\]

Then

\[
\partial_s B_n=-3\pi^2 n^4e^{9u}\exp(-\pi s n^2e^{4u}).
\]

Consequently the positive first term is -(2/3) times the derivative of the positive magnitude of the second term. If the second term includes its minus sign, the proportionality factor is +2/3. The complete identity is

\[
\boxed{\Phi(u)=-\left[B(s,u)+\frac23\partial_s B(s,u)\right]_{s=1}.}
\tag{1}
\]

All prefactors are held fixed when differentiating in s. Other placements or normalizations of s change the proportionality constant and the recovery value.

## Passing through the heat integral

Define

\[
\mathcal B(t,z;s)=\int_0^\infty e^{tu^2}B(s,u)\cos(zu)\,du.
\]

Locally uniformly for Re(s)>0 and finite complex t,z, the theta Gaussian and its super-exponential decay in u dominate any fixed number of parameter derivatives. Differentiation therefore commutes with both the sum and this integral, giving

\[
\boxed{H(t,z)=-\left[1+\frac23\partial_s\right]
                  \mathcal B(t,z;s)\bigg|_{s=1}.}
\tag{2}
\]

This preserves the coupling between the two original source terms before any estimates are taken. Positivity of B as a source for real s>0 does not by itself sign its oscillatory cosine transform or the differential combination (2).

## Connection with dilation and the existing primitive

Directly,

\[
\partial_u B=5B+4s\partial_s B.
\]

Thus (1) also reads

\[
\Phi(u)=-\frac16(\partial_u+1)B(1,u).
\tag{3}
\]

Equivalently, define

\[
\Psi(s,u)=e^u\sum_{n\ge1}\exp(-\pi s n^2e^{4u}).
\]

Since B=-3 partial_s Psi,

\[
\Phi(u)=\left[2\partial_s^2\Psi+3\partial_s\Psi\right]_{s=1}.
\tag{4}
\]

For real s>0 the exact dilation relation is

\[
\Psi(s,u)=s^{-1/4}\Psi\left(1,u+\tfrac14\log s\right).
\]

It gives partial_u Psi=Psi+4s partial_s Psi and hence

\[
\Phi(u)=\frac18(\partial_u^2-1)\Psi(1,u).
\tag{5}
\]

Equation (5) is the identity already developed in [the positive theta primitive note][primitive]. That note also retains the lower-boundary term when transferring u derivatives through the half-line integral. Any change of variables using the dilation must similarly retain the moved integration endpoint. The s identity itself needs no integration by parts and adds no boundary term.

The useful analytical question is whether the coupled s dependence yields a new quantitative signed estimate for the physical field or its first jet. The identities above isolate an expression to study; they do not yet provide such an estimate or a control-separating premise. No new energy refinement, implementation, or task-status change follows from this observation alone.

[results]: ../../../../result-summaries/README.md
[theta]: ../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[avoid]: ../../../../avoid/README.md
[coupled]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[classify]: ../../../../avoid/01_restating_the_target.md
[primitive]: ../../../investigations-2/active/21_quaternion_theta_geometry/notes/05_theta_correlation_kernels/52_POSITIVE_THETA_PRIMITIVE_AND_DIFFERENTIAL_CLOSURE_20261015.md
