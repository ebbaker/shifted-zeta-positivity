# Finite endpoint/count pilot: protocol fixed before execution

26 October 2026, America/New_York. Prepared for Edward Baker with substantial
LLM assistance, **gpt-6.1-sol (Codex), actual recorded effort ultra**.
Same HCB chat0001. **Pre-execution protocol; no values have yet been run.**

This bounded method comparison tests one exact member of Note03/Note04's
frozen family. It does not replace that family, prove a uniform theorem,
or claim a new zero-exclusion region. Under RH the selected height is
already in an all-real region. The purpose is to acquire actual endpoint
and count data for a declared finite case and compare the proposed
off-axis test with direct data from the same exact source.

## Fixed case, source and arithmetic

- The sole case is **m=16**, X=4π exp(16), L=16, τ_X=X^(-1/4),
  endpoints u=±4 and the unchanged rectangle Γ=[-4,4]+i[-2,2].
- Initial source is exactly H(0,z)=ξ((1+iz)/2)/8, including its complete
  gamma and zeta factors. Compute it with python-flint **0.9.0**, at
  **192 bits**. No truncated Dirichlet sum, zero database, sampled
  asymptotic error or uninstantiated F_N constant is an input.
- Normalize by the exact positive A_X of Note03, enclosed by Arb. This
  initial-source pilot does not certify the specified F_N error at m=16
  or supply its coefficient consumer.
- First and second logarithmic derivatives are computed analytically
  from the complete factors and zeta Taylor coefficients. All evaluation
  and rounding errors stay in outward Arb/Acb balls.

## Declared tests and comparator

1. Evaluate exact initial endpoint values and logarithmic jets. Enclose
   A_c=F'(c)/F(c) and Q_c=−(log F)''(c), where F=h_X(0,·).
   Under RH, Q_c is the full inverse-square zero sum.
2. For τ_X Q_c<1/2, use the complete-product/Gaussian bound
   |h_X(τ,c)/F(c)−exp(−τ A_c²)|
   ≤(1−2τ Q_c)^(-1/2)−1. Require its monotone upper error from 1
   at τ_X to be **<1/2**. Then the outward bound
   |F(c)|(1−error)>0 is uniform over the entire time interval.
   This is a conditional analytical certificate under RH; all tails
   occur in the displayed Gaussian moment, with no omitted truncation.
3. Evaluate D_c=F'/F(c+2i) at both safe upper corners and test
   P_c=−Im D_c≤**3/8**. This is the proposed off-axis gateway;
   failure is recorded, not repaired by choosing a different m or corner.
   The direct endpoint/jet test above is the same-source comparator and
   may succeed even if this stronger gateway fails.
4. Integrate F'/F continuously on the four declared rectangle edges,
   oriented counterclockwise. Each integral has absolute/relative
   tolerance **10^(-8)**, evaluation cap **4096**, depth cap **12**
   and degree cap **128**. These are rigorously enclosed integrals,
   not sampled winding increments. Require the resulting count ball
   divided by 2πi to isolate a single integer, have real radius <1/4,
   and contain zero in its imaginary component.
5. Reuse the upper-edge integral to compute the fourth-order Poisson
   count functional C_2. If the corner gateway passes, its analytical
   leakage allowance is 2/3−sqrt(3)/(2π); require its arithmetic radius
   to be **<10^(-4)** and the enlarged interval to isolate the same
   integer as the direct contour count. If the gateway fails, record
   C_2 only as a diagnostic and make no rounding claim from it.

## Stop rules and records

No precision retry, height sweep or adaptive choice of finite cases is
authorized by this protocol. Stop on nonfinite source data, an endpoint
ball containing zero, a failed direct time-margin inequality, a failed
continuous integral tolerance/integer isolation, or a **180-second total
execution cap**. A failed off-axis gateway ends only that gateway, while
the predeclared direct comparator/count can still report their result.
An interrupted/failed run must report the failed stage and keep earlier
verified data; it must not report a certificate for later stages.

Save a small script and JSON record in numerics, including the source
formula, environment, precision, complete balls, tolerances, statuses,
timings and source-code hash. Large logs/caches stay outside the tree.
Use one process and the fixed Arb context. An implementation repair may
fix an API/recording defect but must be named and must not change these
cases, tolerances, thresholds or scientific stop rules.

The derived transport and count-filter proofs will be recorded in the
associated research note and separately assessed before interpreting
the run. A successful finite case remains a method comparison, with
the uniform-in-m endpoint/count problem open.

## Post-stop witness plan (after the fixed source run)

The sole source run stopped when its first contour integral returned a
nonfinite enclosure under the fixed allowance. Its original record and
status remain unchanged. Completed endpoint/time and corner data survived.
No later integral/C_2 stage is reported as successful.

A separate verifier will make **zero new source evaluations**. It will
hash-check that retained record and source script, recheck the recorded
transport inequalities from outward printed balls, and accept only if
the two endpoint signs are opposite and the two-corner Poisson sum is
strictly below 2/5. Every interior root contributes at least 1/5 to that
sum, so under RH the count is at most one; the sign change supplies one.
This is a separately identified post hoc analytical consequence of
completed data, not completion or a retry of the stopped protocol.

For the uniform endpoint bounds it will test conservative constants
0.8144 and 0.2789. Given exact complete count one, the all-real exterior
factor's log-concavity and vertical modulus monotonicity then supply
the full canonical wall floor 0.2789/4 > 0.0697. The associated note
and internal review give these proofs and their RH dependence. The
uniform-in-m acquisition and F_N source conversion remain separate.
