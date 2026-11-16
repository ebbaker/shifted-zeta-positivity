# TN6-B02 — A finite complete-source coefficient acquisition

14 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. Explicit worker dispatch:
**gpt-6-astra / ultra**; backend identity and actual runtime effort are
not independently exposed. **B decision complete; acquisition unperformed.**

| Successor | Type/model | Dependency | Output |
| --- | --- | --- | --- |
| TN6-E02 r1 | E — GPT-6.1 Sol / Ultra | Ready after frozen packet/input checks | Sixteen Jacobi couplings, complete mass, uniform mathematical error allowance and nine certified readouts, or the precise failed budget |
| TN6-E03 | E — GPT-6.1 Sol / Ultra | E02 return; root freezes assessment inputs | One bounded internal assessment; no expanded experiment |

Read [the result index](../../../../result-summaries/README.md),
[avoid index](../../../../avoid/README.md), [tensor bounds 18](../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md)
and [controls 12](../../../../result-summaries/12_collision_controls_and_screening.md).
This is an acquisition decision for an intermediate approximation milestone,
not an RH-equivalent criterion: [avoid 01](../../../../avoid/01_restating_the_target.md).
The number to change is the count of actually enclosed theta couplings
from zero to sixteen, with a complete error at most 10^-8 on the stated
benchmark. [Avoid 03](../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md),
[10](../../../../avoid/10_numerics_ahead_of_the_question.md) and
[20](../../../../avoid/20_volume_without_a_gain.md) rule out another
representation or enlarged scan as a substitute. The sole parent register
records activation before this decision and owns future status.

## Decision and comparison

| Acquisition approach | Benefit | Unpaid or conditioning cost | Decision |
| --- | --- | --- | --- |
| Even moments and parity Gram LDL | Seventeen positive scalar integrals give all norms through degree 16; finite ball arithmetic passes every integration error into the coefficients | Monomial cancellation can destroy relative norm accuracy; positive interval pivots and measured norm loss must be obtained | **Selected** at N=16, with fixed precision ceilings |
| Orthogonalization against an enclosed source measure | Can reduce repeated moment cancellation using a better basis | Requires verified quadrature errors for computed polynomials, or a moment model plus basis changes; neither removes enclosure dependency automatically | Not implemented in this round; a later alternative if the selected route fails |
| Acquire Gaussian nodes/weights directly | Natural scalar evaluation, equivalent to the principal chain | Requires a certified nonlinear node/weight or polynomial-root solve and mass consistency; it does not supply recurrence coefficients for free | No separate acquisition; the chain already is the Gaussian rule |

Select **N=16**, real **|x|<=8**, **0<=tau<=1/2**, lambda=1/2-tau,
absolute error **10^-8 H_(1/2)(0)**. This modest low-height acquisition
benchmark measures conditioning and full cost; it makes no growing-height
or near-zero claim. The actual normalized degree-16 monic norm, rather
than the conservative sufficient-depth formula, pays the chain remainder.
No depth search is permitted. Numerical values are required at the nine
pairs tau in {0,1/4,1/2}, x in {0,4,8}. The uniform theorem concerns the
exact function of the acquired rational matrix; machine rounding is
certified at those nine pairs only.

The matched baseline is direct Acb integration of the **same complete
source**, at the same nine pairs, with the same physical normalization,
source cutoff and rigorous tail payment. This finite real-height benchmark
does not need a Riemann–Siegel implementation. It compares end-to-end
coefficient acquisition plus readouts with complete direct integrals;
separate setup and marginal evaluation costs are recorded. Gaussian
quadrature with the same exact coefficients is identical to the chain,
so relabeling it is no speed comparison. A successful enclosure need not
beat the baseline. One small runtime result is not a complexity law.

## Complete input acquisition and error route

Use the [unchanged source chapter](../../../investigations-5/09_green_potentials_newman_flow/manuscript/sections/02_source.tex):
W_*(u)=exp(u^2/2+u) sum_(m>=1) (2r_m^2-3r_m)exp(-r_m),
r_m=pi m^2 exp(4u), on u>=0, with its **complete** even reflection.
Let m_j=int_R u^j W_*(u)du, m_0=Z_*. Odd moments are exactly zero.
Acquire m_0,m_2,...,m_32 using the first M=8 terms on [0,U], U=2;
restore all omitted arithmetic and spatial mass by the following bounds.
The finite prefix is only an integrand, never a replacement source.

Put a=9^4 exp(-81pi), q=(10/9)^4 exp(-19pi), R=pi exp(8).
For 0<=k<=16, a full-line bound for omitted arithmetic inside [0,U] is

    A_k = 4 pi^2 U^(2k+1) exp(U^2/2+9U) a/(1-q).

Indeed 0<2r^2-3r<2r^2, exp(-pi m^2 exp(4u))<=exp(-pi m^2),
and successive m^4 exp(-pi m^2) ratios for m>=9 are <=q<1.
This deliberately simple allowance is conservative, but fixed before
execution. The complete spatial tail for every such moment is bounded by

    B = 10 (R+2) exp(-R/2).

To check it, the [ITP complete-source proof](../../04_exact_infinite_tensor_products/notes/02_ITP_E01_EXACT_CELL_PHASE_TRANSFER_20261113.md)
gives Phi(u)<10 exp(u)rho^2 exp(-rho), rho=pi exp(4u).
For u>=2, u^(2k)<=u^32 and
32 log u+u^2/2+9u <= u^2/2+41u <=16u^3 <=rho/2.
The middle inequality follows from 16u^2-u/2-41>0 and increasing there;
the last follows from pi>3 and the cubic exponential term. Substitute
du=d rho/(4rho), and include both half-lines. Thus
m_(2k) belongs to twice the retained integral plus [0,A_k+B].
For any direct scalar sample, the omitted absolute field is at most
(A_0+B)/2 since |cos(xu)|<=1 and W_lambda<=W_*.
All constants must be evaluated outward; requested accuracy is not an
achieved radius. [API source record](../../references/01_BALL_INTEGRATION_SOURCES_20261114.md)
records what was inspected and its implementation/version limitations.

Separate the Hankel Gram matrix (m_(i+j))_(0<=i,j<=16) by parity.
The even block has monomials 1,u^2,...,u^16 and the odd block
u,u^3,...,u^15. Interval LDL without pivoting produces the raw monic
norms h_0,...,h_16 as its pivots, interlaced by degree. Exact parity
orthogonality justifies this identification. Every enclosing pivot must
have positive lower endpoint. Then beta_n=h_n/h_(n-1), a_n=sqrt(beta_n)
for n=1,...,16. J_16 uses a_1,...,a_15; a_16 is the omitted edge and
h_16/h_0 pays its remainder. Record each norm-to-diagonal ratio
h_n/m_(2n), interval relative radius, and a certified infinity-norm
condition bound on each diagonally scaled parity Gram block when the
bounded solve succeeds. Report failure of that optional condition bound
honestly; positive pivot/coefficient certificates remain the primary test.

Let Jhat be the exact rational midpoint matrix and delta the maximum
row sum of its edge error radii, so ||J_16-Jhat||_2<=delta. The Gaussian
representation in [JCH R2](../../02_jacobi_chain_height_flow/notes/02_JCH_E01_R1_FINITE_CHAIN_READOUT_20261113.md)
and Duhamel's unitary identity give, for real symmetric A,B,

    ||exp(-tau A^2)cos(xA)-exp(-tau B^2)cos(xB)||
      <= ||A-B|| E|x+sqrt(2tau)G| <=9 ||A-B||

on this domain. The last constant uses |x|<=8 and
E|sqrt(2tau)G|=sqrt(4tau/pi)<1. This avoids treating A^2-B^2 as a
new source of uncertainty. Let Zhat be the rational midpoint of Z_* and
eta_Z=radius(Z_*)/lower(Z_*). The exact nominal physical scalar
Chat=(Zhat/2)<e0,exp(-tau Jhat^2+i x Jhat)e0> satisfies

    |H-Chat|/(Z_*/2) <= Q + 9 delta + eta_Z,
    Q = upper(h_16/h_0) S_16(1/2,8).

S_16 is the nonnegative rational sum in the acquired JCH theorem.
Contractivity bounds the mass-error factor by one. The finite exponential
uses **Jhat squared**, never the compressed infinite square. A certified
physical numerical radius r at a sample adds 2r/lower(Z_*). Source/tail
errors already enter the moment and coefficient balls; do not add them
a second time to the chain ledger. The direct baseline pays its own
integration and tail radius.

## Actual collision-control screen

This checks the current acquisition/readout premises, not an unperformed
control computation; see [avoid 02](../../../../avoid/02_shape_only_arguments_and_the_controls.md).

| Witness | Premise or allowance and consequence |
| --- | --- |
| Three atoms F_lambda=2+2 exp(lambda-T)cos x | At T=1/4,x=pi, inside this domain, the exact three-site output and error are zero at a double collision. Infinite-support positivity through degree16 fails (Gram terminates), and the theta integrand/tails are inapplicable. Generic finite-chain accuracy demonstrably does not imply noncollision. |
| Euler-factor sources | Finite translated complete sources keep generic moment/quadrature and matrix-perturbation premises. The **literal unshifted** summand integral and A_k,B payment above fail to describe them. The earlier p=23 envelope failure is at lambda=0, not a fixed-base failure claimed here. No transfer of the theta numeric certificate is asserted. |
| Positive three-/four-square sources | Positive density, even moments, Gram acquisition and the JCH remainder can hold at their known events. Complete canonical coefficients/full reflection fail; our arithmetic-tail equality is then for the wrong source. Their events at about44.13/83.53 are outside this benchmark; no within-box rejection is required. |
| Reflected quartic, smooth shape and positive-primitive sources | Their complete moments and generic acquisition/readout permit approximation at collisions (quartic event at tau=1/4,x=pi/4 is in this domain). They fail the specified integer-square expansion and its numerical tail constants. Small-damping qualification is retained. No failure of the generic matrix estimate follows. |
| Finite-prime orbit sources | Modified coefficients/full-reflection premise fails; generic moment bounds can hold. Events are in sufficiently high gaps and need not be in this box. Fixed finite observations cannot replace complete-source identity. |
| Atomic and continuous finite-profile thresholds | Atomic rank termination prevents positive pivots to degree16 when support is too small. Triangular continuous extensions can have positive finite Gram matrices; the theta profile and specified source/tails still fail. |
| RH-conditional endpoint controls | Their construction remains conditional and ordinary Dirichlet arithmetic fails. Generic moment and readout estimates can apply; the present literal theta integration input does not describe the perturbation. Escaping event heights need not lie here. |
| Unchanged amplitude, altered kernel | Coefficients and their acquisition can be identical. The full cosine/Newman observation premise fails, so the readout allowance does not cover that output. |
| Actual-profile positive-measure relaxation | It is not an integer zero configuration or a supplied theta Fourier source, and cannot be an input to this acquisition contract. |

A negative return applies only to this N=16 moment/LDL method, frozen
source and error/work limits: [avoid 07](../../../../avoid/07_scoped_exclusions_read_as_universal.md).
Same-source checking and a different dispatched model are not independent
specialist review: [avoid 05](../../../../avoid/05_same_model_reviews_and_shared_premises.md).
[One writer](../../../../avoid/17_parallel_writers_and_broken_registries.md)
owns each shared file. The [frozen E02 request](../../research-progress/handoffs/TN6-E02-r1.md)
is the sole numerical contract; no numerical campaign, manuscript or
coefficient certificate is claimed by this B decision.

A bounded read-only internal analytical check by an inherited-setting
subagent found no defect in A_k, B, parity LDL or the normalized transfer;
it requested explicit restriction of delta to the fifteen internal edges
and exact symmetric zero-diagonal midpoints. Both are stated in E02 r1.
No numerical computation or independent specialist review occurred.
