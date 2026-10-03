# Bounded extension preflight: signed frequency compression

3 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); serving variant and reasoning effort are not exposed.
This preflight was written before running the new outward certificate.
Predicted values below are floating diagnostics, not certified inequalities.

## All-window obligation and chosen test

The target remains Q>=0 on the same three-moment smooth complex source class
for an unbounded sequence of nested support windows. No finite set of
certificates proves that statement, and no common positive L2 gap is required.
This experiment fixes L=6/5. Only the prime powers 2 and 3 are active.
For converting to a Sonin comparison throughout 1<=L<=6/5, keep S={2,3}.
The previous length-one certificate is an immutable baseline and has been
replayed once; its numerical record and generator bindings match.

The raw positive-part operator loses useful positive energy before source
compression. At lambda=1, T=164, its largest floating eigenvalue is about
1.01720, whereas signed compression gives about 0.997081. This is a failure
of the sufficient majorant. More precision would not fix it.
One additional bounded parameter choice, lambda=1/2 and T=100, gives a
smaller signed problem with a predicted gap about 0.00244838. No other
window or unbounded parameter search is included in this session.

## Signed alternative

Let f(y)=sqrt(L)F(Ly) on (-1/2,1/2), and let P_E remove exactly
1, exp(Ly/2), exp(-Ly/2). With v_t=P_E exp(iLty), put

    r(t)=lambda-gamma(t)+sum_active c_a cos(at),
    A=(L/pi) integral_0^T r(t) Re|v_t><v_t| dt.

If gamma(T)>lambda+sum c_a, monotonicity gives q(t)>=lambda for t>=T,
and Q>=lambda I-A. Keeping signed r retains every positive-frequency
contribution in the band. It does not use a prime-density error theorem
or solve the exponential cutoff barrier.

The signed integrand is smooth. With Wabs=integral_0^T |r|, set

    V1=gamma(T)-gamma(0)+T sum c_a a,
    V2=15 sqrt(3)/2+T sum c_a a^2,
    R2=V2+(2L/sqrt(3))V1+L^2(1/sqrt(20)+1/6)Wabs.

The midpoint operator error is at most L h^2 R2/(8 pi). The independent
all-mode Legendre error is at most 2L delta_M Wabs/pi. Wabs itself is
enclosed from midpoint absolute mass with the first-variation allowance
h V1/2. These constants have a separate same-model analytic audit.
The [scaling audit](../reviews/ALL_WINDOW_SCALING_AUDIT_20261003.md) gives
the formulas and proof, including the full analytic moment projection.

## Resource and error budget

Chosen parameters: lambda=1/2, T=100, M=100, N=30000, precision 192.
There are two real 50-by-50 blocks and 3,000,000 plane-coordinate
special-function evaluations; batched matrix multiplication uses panels
of 128. Matrices are transient and no large arrays are saved. The replay
of the length-one implementation took about 8 seconds, but its lower rank
and arguments make linear runtime extrapolation unreliable. Allow up to
10 minutes for the first run and up to 10 minutes for a 256-bit audit replay.
Stop and diagnose if either exceeds its allowance; do not enlarge the
experiment silently. Hard CLI guards bound L<=6/5, T<=200, M<=192,
N<=80000, and precision<=384; these are ceilings, not an authorized sweep.

| Item | Predicted value / chosen cap |
|---|---:|
| gamma(100)-1/2-C_L | 0.0184626 |
| largest signed matrix eigenvalue | 0.49755162 |
| outward matrix cap to test | 249/500 = 0.498 |
| midpoint operator error | about 0.000320564 |
| complete Legendre tail error | about 9.2e-9 |
| chosen total error allowance | 1/2000 = 0.0005 |
| resulting all-source Q gap if checks pass | 3/2000 = 0.0015 |
| fixed-{2,3} correction norm coefficient at L=6/5 | about 3457.34493 |
| rational correction cap to test | 3458 |

The matrix cap and error allowance leave distinct positive margins. Arb
LDL, the frequency cutoff, tail ratio, and all scalar error/correction
tests must pass outward before accepting the certificate. Float eigenvalues
make only this cost decision. The resulting retained fraction would be
(3/2000)/(3458+3/2000)=3/6916003.

## What the test can support

On the same source space, the capped lambda=1/2 bound is negative in its
worst even and odd directions. The signed band recovers about 0.21161 and
0.14522 units of positive energy respectively, leaving positive lower
values in those directions. The pilot will record both the actual-Q
diagnostic and this discarded-energy comparison separately from proof.

A pass would support retaining signed frequency energy before compression,
and demonstrate a comparison through the first new-prime threshold. It
would not establish signed prime-density cancellation with useful large-L
constants. The remaining sufficient theorem is an all-window bound
lambda_max(A_L)+error_L<=lambda_L for unbounded L, or a quantitative
relative-energy complement and mixed-block bound guaranteeing H_L<=I.
The existing absolute-amplitude cutoff still grows doubly exponentially
on the prime-number-theorem scale. A continuation algorithm also needs a
proof that accepted window increments cannot accumulate at finite L.
