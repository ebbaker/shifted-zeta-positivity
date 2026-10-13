# Smooth-weight source argument scope review

13 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited session configuration; exact serving variant
and reasoning effort are not exposed and are not inferred.

This is a separate same-family reading of
`5_SMOOTH_WEIGHT_UNIFORMITY_SOURCE_PASS_20261013.md` and the cited pinned
Lean contracts. No Lean build, VM command or repository change was made.
It is not external independent validation of the source theorems or a
checked Lean application.

**Assessment:** no concrete mathematical defect was found in the conditional
paper-level derivation. The argument preserves the required derivative-order
quantifiers and quadratic dependence on the weight seminorm. U1's arithmetic
dictionary and the uncompiled conversion/partition/transport applications
remain explicit obligations.

- **Fourier tail and order.** Integration by parts with `m=J+2` changes the
  weighted large-frequency integrand to a constant times `|v|^-2`, whose
  integral over `|v|>1` is two. The small-frequency interval has length two.
  Both yield the stated `2^(J+1)` bound. Compact support removes boundary
  terms. The Stirling-number formula for derivatives of `V(exp u)` bounds
  the required norms by `M_(J+2)(V)` on the fixed log annulus. The alternative
  source `J+p` route has a coefficient linear in its source-bound parameter;
  it correctly leaves the ordinary-to-Schwartz comparison uncompiled and
  does not assert `p=2`.
- **Partition and derivative costs.** A bump positive on `[3/4,3/2]` has
  dyadic dilates covering the positive axis. Its locally finite sum is
  positive and invariant under doubling, so division constructs the stated
  partition. A nonzero summand on `[a,b]` requires
  `a/2<=2^j<=2b`; thus the restriction is finite and fixed with the interval.
  Leibniz and dilation give `M_k(V_j)<=B_(psi,k) max(1,lambda_j)^k M_k(W)`
  without raising the derivative order. Empty support gives the zero-weight
  case directly.
- **Scale transport.** The read polynomial is `D^(-1/2)` times the ideal
  sum at zero twists. Substituting `W_j(x)=V_j(x/lambda_j)` leaves that sum
  unchanged at column length `lambda_j D`, producing exactly `sqrt(lambda_j)`
  in the polynomial and `lambda_j` in its energy. Compactly supported
  summands justify finite linearity. The row characters and original row
  bound are unchanged.
- **Capacity and finite energy sum.** With `c0=c/2`, the displayed threshold
  implies `lambda_j^(1+c0)<=D^(c-c0)`, hence
  `(lambda_j D)^(1+c0)<=D^(1+c)<=H`. The positive margin is essential.
  `max(1,lambda_j D)<=max(1,lambda_j) max(1,D)` preserves all positive
  rescaled lengths. Finite Cauchy–Schwarz contributes the required factor
  `N`; combined with the derivative and raw-moment costs, it gives the
  displayed `N sum_j lambda_j max(1,lambda_j)^(kappa+2k)` constant.
- **Bounded scales.** The source polynomial estimate and row cardinality
  estimate yield `128^3 max(1,b)^2 M_k(W)^2 H D`. Replacing `D` by `D0`
  and using `(H max(1,D))^kappa>=1` for `H>=1,kappa>0` produces the claimed
  uniform bound for every `0<D<D0`, including short scales. There is no
  unaccounted negative power of `D`.
- **Quantifiers and O5 specialization.** The one reference cutoff and
  positive parameters are fixed before selecting `J`; the cited reference
  theorem selects `J` before `RowData`. Thus `k` precedes interval, data and
  weight. Partition/dilation/threshold costs depend on the fixed interval,
  while the final constant is uniform over its weights and homogeneous of
  degree two in `M_k(W)`. Taking `c=theta`,
  `kappa=epsilon/(2+theta)` and `H=D^(1+theta)` gives normalized exponent
  `1+theta+epsilon`; multiplying by `D` gives the O5 exponent
  `2+theta+epsilon`, conditional on U1. Element-row multiplicity is retained.

This supports the proposed source route, not closure of U2 as a compiled
application. The remaining ordinary-derivative conversion, smooth partition,
scale identity and assembly must still be instantiated and checked. Terminal
zero-free replay does not supply those application checks.

For the separate operational documentation refresh, the actual initial
attempt's `--baseline-name` label is `pre-math-replay-20261013`; the Multipass
snapshot reference is `rh-replay.pre-math-replay-20261013`. Those identify the
same intended baseline at different interfaces and should be distinguished
in the example command. The parent agent is correcting that label.
