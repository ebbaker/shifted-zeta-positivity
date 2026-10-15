# Review of collision behavior and logarithmic losses

14 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded parent model **gpt-6-astra**, reasoning effort **ultra**, verified
from this turn's metadata. Separate internal analytic and computational
agents inherited this configuration. This is internal LLM review, not
external peer review or formal verification.

**Assessment: approved within the stated conditional scope.**
[Note 28](../notes/28_COLLISION_SCALES_AND_DELAYED_COMPARISONS_20261014.md)
explains the manuscript's finite-order stationary collision pole, refines
its finite part, and identifies the extra cancellation introduced by a
positive limiting delay. It also proves a sufficient criterion with
prescribed logarithmic energy losses. No theta inequality of that kind,
actual theta collision, or new finite or asymptotic sign coverage is claimed.

## Analytic checks

The time orientation agrees with H_t=-H_xx: nonreal conjugate roots approach
the real axis as time increases to the event, then split into simple real
roots. The double and cubic models have the stated physical energy and
stationary Laguerre forms. The cubic model correctly explains why the first
stationary set can be absent and the second test is indispensable.

The predecessor construction retains the actual moving stationary curve.
The finite part alpha=D/((r+1)A)-B^2/(2rA^2) follows from the heat Taylor
series and the exact derivative dW/ds=W_xx. The odd-case H/H_x coefficient,
its contribution to physical E, and the finite part of L_1/E are correct.
The extra term in the moving derivative of E on h_2=0 is retained.

For positive limiting delay and a nonzero earlier residual, the leading
split ratios have opposite order-s^(-r) poles. The exact recombination
preserves cancellation of every intermediate power. The stated diagnostic
minimum separate losses have the correct coefficient |g/k|/2. They are
explicitly not adopted as source-defined proof coefficients. The favorable
quartic control establishes a limitation of separate retained positivity
in the polynomial source class, not a theta counterexample.

Review corrected two ambiguities before installation: the odd-root
subtraction now explicitly gives chi-x_zero, and the complete residual
includes -2aW_x at every comparison time before current stationarity is
imposed. The earlier sample retains its drift. The shrinking-delay formulas
distinguish delta=rho*s+O(s^2) from convergence without a rate and do not
assert a nonzero leading term when its coefficient cancels.

## Logarithmic loss criterion

For fixed M>0 and finite q>=0, F_q(E)=E[1+log_+(M/E)]^q, extended by zero
at E=0, satisfies

\[
 \frac{-\mathcal L_j}{F_q(E)}
 \sim\frac{r}{s[2r\log(1/s)]^q}\longrightarrow\infty
\]

on any finite-order collision predecessor. Locally bounded K_j therefore
cannot satisfy L_j>=-K_j F_q(E) there. This proves the conditional exclusion;
the manuscript's separate finite collision criterion gives the RH implication
only when the required domain is covered. Theta nontriviality supplies finite
spatial multiplicity. The coefficients and nonlinear gauge must be prescribed
or independently proved, not defined by an observed quotient.

For q>0 this extends the original bounded-relative-loss condition and is
not an application of that condition with an unbounded effective coefficient.
The q>1 argument uses finite-order analyticity. The scalar smooth flat
countermodel is correctly differentiated and correctly distinguished from
an analytic heat family. The power-loss critical exponent and the comparison
F_q(E)=o(E^p) for fixed p<1 are correct.

## Exact checks and replay

The independent [checker](../numerics/check_collision_behavior.py) constructs
finite rational heat polynomials from raw spatial jets. It independently
solves two coefficients of the stationary branch and assembles physical
energy and Laguerre numerators before division. The
[receipt](../numerics/COLLISION_BEHAVIOR_CHECKS_20261014.json) records **1,072
named assertions**, including 60 generic jet cases, multiplicities 2 through
13, double/cubic controls, 30 delay comparisons, higher canceling poles, and
power-exponent arithmetic.

The parent reran the checker; its receipt is byte-identical to the independent
agent's receipt. Source SHA256:
`d54cd227f2be4a184e123105dec6f20fa798f5f85a96359d2c1304fb4efc5cd0`.
Receipt SHA256:
`4c918a39f1b261bef99536e4d51ffd017c97ca04e2adcbc74733e3661c3fd3e5`.

These finite checks do not prove analytic branch existence, the all-multiplicity
theorem, or the logarithmic limiting argument; those have explicit analytic
proofs. They do not evaluate the theta source. No manuscript revision,
quadrature run, commit, tag or new snapshot folder is part of this review.
