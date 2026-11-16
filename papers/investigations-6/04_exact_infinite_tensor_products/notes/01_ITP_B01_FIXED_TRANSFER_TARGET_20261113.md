# ITP-B01: fixed weighted refinement and readout target

13 November 2026, America/New_York. Intended author **Edward Baker**;
substantial Codex LLM assistance. Recorded dispatch **gpt-6-astra / ultra**;
independent backend metadata unavailable. Status: **specification and proof
route; constants and theorem await ITP-E01 execution**.

The [decision](../brainstorm/notes/01_ITP_B01_EXACT_CELL_PHASE_DECISION_20261113.md)
contains the option comparison and control screen. Read the
[result index](../../../../result-summaries/README.md),
[avoid index](../../../../avoid/README.md),
[controls 12](../../../../result-summaries/12_collision_controls_and_screening.md)
and [scoped conclusions](../../../../avoid/07_scoped_exclusions_read_as_universal.md).

## Objects, topology and product ordering

Keep the complete source from the
[GNP source chapter](../../../investigations-5/09_green_potentials_newman_flow/manuscript/sections/02_source.tex):
W_lambda=e^(lambda*u^2)Phi, H_lambda=(1/2)integral_R W_lambda exp(izu)du,
0<=lambda<=1/2 and tau=1/2-lambda. Imaginary-time source evolution is
partial_tau W=-u^2 W. No probability normalization is introduced.

Partition R into integer unit slabs, then refine each slab in coarse-to-fine
binary order. At level L the common cells are I_j=[jh,(j+1)h), h=2^-L.
P_h f is the cell mean. On each slab let f_0 be the slab mean and
R_k=(P_(2^-k)f)/(P_(2^-(k-1))f), so f_0 product_(k<=L)R_k=P_h f.
Positivity justifies the local ratios; they act on growing prefixes.
No global lower floor or global operator-norm product is asserted.

The topology selected here is uniform-in-lambda convergence in
||g||_(1,8)=integral_R exp(8|u|)|g(u)|du for the prepared amplitudes.
The consumer is uniform absolute field error over x in R and |y|<=8.
Neither gamma-normalized error nor error relative to H is controlled.

For exact masses m_j=integral_(I_j)W_lambda and centers c_j=(j+1/2)h,

    A_L(lambda,z) = (1/2) integral_R P_h W_lambda(u) exp(izu)du
       = (1/2) sinc(z*h/2) sum_(j in Z) m_j exp(iz*c_j).

Use sinc(w)=sin(w)/w with sinc(0)=1. On each cell this factor is the
conditional expectation of all unresolved binary phase factors; it does
not approximate the phase by its value at a point. The infinite phase
product itself has only inherited bounded-height norm convergence. The
claimed all-height statement is instead for its integrated readout after
source approximation; keep these different quantifiers explicit.

## Elementary proof route and target constants

Prove, for an absolutely continuous f on a length-h cell I,

    integral_I |f-mean_I f| <= (h/2) integral_I |f'|.

A double-integral proof gives the kernel 2t(h-t)/h for the derivative,
whose maximum is h/2. Then use max_I exp(8|u|)/min_I exp(8|u|)<=exp(8h)
to obtain

    ||W_lambda-P_h W_lambda||_(1,8)
       <= (h exp(8h)/2) ||W'_lambda||_(1,8).

The Fourier factor 1/2 gives the target readout constant h exp(8h)/4.
The scalar baseline integrating the same P_h W gives this identical bound.

For explicit theta domination put rho=pi exp(4u), u>=0. The inherited
polynomial recurrence gives P_0=2r^2-3r and
P_1=-8r^3+30r^2-15r, with coefficient sums 5 and 53. Put
C_d(0)=sum_(n>=1)n^(2d)exp(-pi(n^2-1)), B_0=5C_2(0), B_1=53C_3(0).
Use

    |W'_lambda(u)| <= exp(u^2/2+u)
                        [B_1 rho^3 + u B_0 rho^2] exp(-rho).

The proposed simple constants follow from C_2(0)<=C_3(0)<2,
u^2/2+9u<=rho/2 and u<=rho/4. These are elementary inequalities to
verify, not imported numerical measurements. Substituting rho gives

    V_8 <= 8 B_1+2 B_0 < 868.

For the exponential inequality, pi>=3 and exp(4u)>=1+4u+8u^2 reduce
it to a positive quadratic. Bound the C_3 tail by an explicit geometric
series; do not leave its value as an unexplained decimal. The integral
of rho^2 exp(-rho/2) on [0,infinity) is 16.

For integer U>=1 and h dividing U, retain only cells in [-U,U]. Their
readout A_(L,U) has total error at most

    h exp(8h) V_8/4 + T_8(U),
    T_8(U)=(1/2)integral_(|u|>U) exp(8|u|)W_(1/2)(u)du.

One valid proof splits the true integral at U and uses the local cell
bound inside; it does not need a separate outside P_h tail. Derive
T_8(U)<= (B_0/2)(rho_U+2)exp(-rho_U/2), rho_U=pi exp(4U).
First quantitative test: U=2,L=30, V_8<=868 and a complete allowance
<=10^-6. Permit one correction only, with U<=3,L<=34, if a routine
constant correction makes the first tuple fail. No grid or masses are
numerically constructed.

## Scope of time and arithmetic payments

Each m_j(lambda) is an exact complete-source integral. Recomputing or
defining these masses at each lambda gives the exact orbit projected at
that time. Do not assert that P_h commutes with multiplication by u^2,
or that the level-L state solves the exact source ODE. No finite closed
time integrator or simple local coefficient law is supplied.

There is no source truncation or numerical arithmetic in the theorem.
For a future finite computed version with errors delta m_j, use the
exact cell-readout bound

    |delta A_(L,U)(x+iy)|
      <= (1/2) exp(4h) sum_j exp(8|c_j|)|delta m_j| + e_readout,

uniformly in x and |y|<=8, since |sinc(z*h/2)|<=exp(4h).
Here e_readout is a separately established absolute contraction error,
not an assumed precision guarantee. The mass errors must include actual
source, integration and core/compression errors before use. Give a
sufficient budget for these quantities; do not claim it was attained.
No division by the small signed field is permitted, and no Green-log
anchor or deflation condition is acquired by this result.

## Scoped point-phase comparison

The one comparison architecture is
B_L(lambda,x)=(1/2)sum_j m_j(lambda)exp(ix*c_j), omitting sinc.
At x_k=2*pi*k/h its value is (-1)^k Z_lambda/2, with
Z_lambda=integral_R W_lambda>0. For each fixed lambda, integrability
implies H_lambda(x_k)->0. Derive

    sup_(x in R)|H_lambda(x)-B_L(lambda,x)| >= Z_lambda/2

for every fixed L. This is a lower bound on this specified point-phase
architecture's actual uniform error, not merely its upper allowance.
It concerns neither exact cell integration nor general tensor networks,
adaptive grids, increasing-height windows or normalized relative error.
