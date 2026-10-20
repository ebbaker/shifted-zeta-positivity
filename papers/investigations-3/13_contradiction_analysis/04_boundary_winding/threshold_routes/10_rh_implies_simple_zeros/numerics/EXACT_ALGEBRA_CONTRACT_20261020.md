# Exact algebra replay contract

20 October 2026. Prepared for Edward Baker with substantial LLM assistance;
**gpt-6-astra, effort ultra**, recorded session configuration.

Frozen before execution. The standard-library rational replay checks only:

1. The finite heat-polynomial Gaussian calculation for monomials of
   degrees 2–12 at a zero-time event, against the Hermite coefficients.
2. The event jets of the even real-rooted polynomial `(x^2-a^2)^2` for
   `a=1,2,3`, at `x=a`, and the double-event lower bound at
   `s=a^2/16,a^2/8,a^2/4`.
3. The finite Euler-control Fejér sum against
   `2(1+{N}(1-{N})/N^2)` for the predeclared positive rationals
   `N=j/k`, `1<=j<=35`, `1<=k<=7`, including integer endpoints.

All arithmetic is exact rational arithmetic. These checks detect finite
coefficient/normalization mistakes; they prove neither the infinite-source
identities nor the optimized asymptotic, and certify no theta zero or
height interval. Those claims require the analytical proofs in Notes 01–02.
No sign is selected by a numerical search.
