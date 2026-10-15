---
research_program: PR03
program_slug: 03_effective_bridge
status: proposed
---

# Effective heights and finite bridging target and validation

15 October 2026. Prepared for Edward Baker with substantial LLM assistance. Recorded model **gpt-6-astra**, reasoning effort **ultra**, verified from the current turn metadata.

[Workstream definition](README.md) · [Canonical source index](README.md)

Keep two distinct tasks: effective constants for an analytic starting height, and finite certified tests of proposed sign mechanisms. A bridge is complete only when a verified finite cover overlaps a proved analytic domain. The existing cover reaches |x|<=112 over 0<=t<=1/2; the sharper outer theorem has an unevaluated cutoff.

Before a large numerical sweep, determine whether an improved error budget gives a reachable starting height. The existing conservative saving exp(-L/20000) may lead to a very expensive threshold once constants and logarithmic factors are paid. This is a limitation of that bound, not a lower bound for the true threshold.

For a mechanism pilot, sample prescribed theta values including below two and isolate roots of h_1 and h_2 at t=theta/L(x). Root isolation along this curve uses d h_{j+1}/dx=h_{j+2}+theta h_{j+3}/(xL^2). Choose cutoff and precision from independent complete-source budgets. Retain interval failures as undecided unless a strict violation is proved.

A useful deliverable is either an evaluated analytic cutoff with a feasible bridge plan, or a small certified experiment that rules out or supports a precisely stated candidate mechanism. Neither task substitutes for all-height inner-cusp control.
