# Bargmann Fock observation geometry

Initial scout, 10 October 2026. Model: GPT-6 (Codex). Exact serving variant
and configured reasoning effort are unavailable. The review is an internal
LLM check, not independent mathematical validation.

The question is whether the genuine theta state's Fock coefficients obey
a restriction that makes its value and slope observable together.

- Enlarged state: the genuine entire function \(f_t(z)=H_t(z)\) in the fixed
  Gaussian holomorphic Hilbert space \(\mathcal F_a\), \(a>0\).
- Generator: \(-\partial_z^2\), on the genuine theta orbit and its finite
  parameter derivatives; this is not the number operator.
- Reduction: real-axis evaluation, followed by the manuscript's nonvanishing
  normalizer. The value and slope are bounded functionals at each fixed \(x\).
- Arithmetic data: the full even theta kernel from the stable manuscript,
  including its factors of two; \(H_0=\xi(1/2+iz/2)/8\).
- Domain: all positive widths and real times on compact intervals; theta
  super-exponential decay pays every norm and differentiation used here.
- Intended implication: a lower bound for the angle to the joint observation
  kernel, or an opposite signed threshold-jet inequality.

[Scout note](notes/1_THETA_FOCK_NORM_PAID_TAIL_AND_OBSERVATION_KERNEL_20261010.md)
proves an exact theta double-integral norm, a width-based coefficient tail,
and the observed projection identity. It establishes a scoped obstruction:
positive even theta-type moment signs and a positive two-kernel Gram matrix
cannot by themselves imply joint nonvanishing. No new collision exclusion,
theta-specific angle estimate, or global coverage is established.

See [numerical record](numerics/README.md) and
[internal review](reviews/1_SCOUT_INTERNAL_REVIEW_20261010.md).
