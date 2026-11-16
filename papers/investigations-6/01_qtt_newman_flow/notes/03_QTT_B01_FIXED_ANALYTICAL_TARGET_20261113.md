# QTT-B01: fixed source, norm and derivation route

13 November 2026, America/New_York. Intended author **Edward Baker**;
substantial OpenAI Codex assistance. Recorded dispatch: **gpt-6-astra /
ultra**; independent backend model/effort metadata unavailable.
Status: **conceptual specification; the numerical sufficiency of the
proposed tuple is unproved pending QTT-E01**.

See [B01 decision](../brainstorm/notes/01_QTT_B01_OBSERVATION_NORM_DECISION_20261113.md),
[result index](../../../../result-summaries/README.md),
[avoid index](../../../../avoid/README.md),
[controls 12](../../../../result-summaries/12_collision_controls_and_screening.md)
and [approximation-versus-target classification](../../../../avoid/01_restating_the_target.md).
The unchanged source and reflection come from the
[inherited source chapter](../../../investigations-5/09_green_potentials_newman_flow/manuscript/sections/02_source.tex).

## Fixed representation

For u>=0 let r_n=pi*n^2*exp(4u) and
Phi(u)=exp(u) sum_(n>=1)(2r_n^2-3r_n)exp(-r_n).
Use its complete even reflection, W_lambda=exp(lambda*u^2)Phi and
H_lambda(z)=integral_0^infinity W_lambda(u)cos(zu)du. This is exactly the
full-line convention H=(1/2)integral W exp(izu)du; no mass normalization
is introduced. Put tau=1/2-lambda, so 0<=tau<=1/2.

Take U=2, h=2/2^L and u_j=(j+1/2)h, j=0,...,2^L-1. This is a
positive-half-line tensorization, explicitly replacing the symmetric-grid
encoding only. Binary ordering is coarse-to-fine,
u_b=h/2+sum_(k=1)^L h*2^(L-k)*b_k. The state is sqrt(h)W_lambda(u_b).
The source evolution remains -X^2. The cosine observation is the half-sum
of the two exponential product contractions, each with external factor
sqrt(h); their half-sum restores the cosine, not a second full-line factor.

Let p_d be the degree-d truncated Chebyshev expansion of W_(1/2) on
[0,2], with its exact complete-source coefficients. Let
q_m(tau,u)=sum_(j=0)^m(-tau*u^2)^j/j! and P_tau=p_d*q_m.
The inherited polynomial-translation construction gives QTT rank at most
d+2m+1. E01 may prove this directly; no imported optimal-rank claim is used.

## Bound to establish

The ellipse is u=1+(w+w^-1)/2, |w|=rho=5/4. Its real extent is
[-1/40,81/40] and its imaginary semiaxis is 9/40. Consequently
Re exp(4u)>0. Bound the complete series there by M_rho, with all constants
explicit. One elementary route uses t=pi*n^2 exp(4 Re u),
cos(4 Im u)>=1/2, t>=2n^2, and
(2t^2+3t)exp(-t/2)<=38 exp(-t/4). Prove any looser convenient
rational upper bound rather than evaluating an uncontrolled infinite sum.
The factor exp(u+u^2/2) is also bounded on the ellipse.

The contour/Laurent proof of the Chebyshev coefficient bound gives
epsilon_d <= 2 M_rho rho^(-d)/(rho-1). Derive that estimate in-note or
verify its exact normalization from a checked primary source. Put
M_0=sup_[0,2] W_(1/2), E_m=2^(m+1)/(m+1)!, and
delta=epsilon_d+(M_0+epsilon_d)E_m.
These are allowances, not measured errors.

For D={(lambda,z):0<=lambda<=1/2,40<=Re z<=80,|Im z|<=8}, define
S(x)=exp(pi*x/8)/(1+x)^(7/4), S_*=max_[40,80]S(x), and
T=integral_2^infinity exp(8u)W_(1/2)(u)du.
Let M_2 bound the second u derivative of W_lambda(u)cos(zu) on D x [0,2].
The target estimate is

    sup_D S(x)|H_lambda(z)-h sum_j P_tau(u_j)cos(z*u_j)|
      <= S_* [ T + (2 h^2/24) M_2 + 2 exp(16) delta ].

The midpoint term uses the complete integrand, followed by replacing its
node values with P_tau. This avoids paying a high-degree polynomial
derivative instead. The half-line normalization is explicit. Derive T
from the inherited source bound or directly by the positive series;
derive M_2 from that derivative envelope or Cauchy circles of radius
1/16 lying inside a domain with positive Re exp(4u).

The proposed tuple is (d,m,L)=(512,64,72), target <=10^-8. One correction
within (d<=640,m<=80,L<=80) is permitted if the first sufficient estimate
fails. Constants must be proved; numerical evaluation is not a certificate.

## Complete payments and comparison

The exact-coefficient mathematical construction has no arithmetic source
truncation, core rounding or implementation error. Those zeros describe
the theorem, not a completed executable algorithm. A computed version
must add a node-uniform source/core error e_node with contribution
2 exp(16)e_node, a finite-state Euclidean compression error e_TT with
contribution sqrt(2)exp(16)e_TT, and a complete scalar readout arithmetic
error e_out; multiply their sum by S_*. Explain whether errors were
already included in e_node before adding e_TT, so they are not double-counted.
An evolved approximate state also needs its accumulated residual from
the inherited contractive semigroup estimate. The polynomial heat error
already pays the specified q_m approximation; no additional time integrator
is part of this request.

Derive sufficient tolerances for each optional computed error by dividing
10^-8 by four and its actual transfer factor; do not claim those tolerances
were attained. All source coefficients remain exact in the base theorem.
No large tensor or dense grid is to be built.

The matched scalar baseline is integral_0^2 P_tau(u)cos(zu)du, retaining
the same tail. Its bound is S_*[T+2 exp(16)delta]. Thus the QTT version
does not improve this polynomial approximation allowance. State arithmetic
operation counts only for stated algorithms, with coefficient construction,
precision and stability unpaid unless actually derived. No speed result
or lower complexity bound follows from the rank theorem.
