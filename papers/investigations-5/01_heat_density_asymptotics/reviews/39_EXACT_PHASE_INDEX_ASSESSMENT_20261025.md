# Exact phase-index construction: internal assessment

25 October 2026. Prepared for **Edward Baker** with substantial LLM
assistance, **gpt-6.1-sol, actual recorded effort ultra**, chat0021.
Same-model internal analytical assessment of
[Note60](../notes/60_EXACT_PHASE_INDEX_BY_DYADIC_ONSET_SELECTION_20261025.md),
including parallel same-model branch, arithmetic/cost and contract checks.
This is not independent specialist review or HDA-20 completion.

## Finding and scope

The inspected construction closes Note59 EV21 **with the author's
explicitly authorized existing onset freedom**. It preserves the literal
ceiling at its selected onset. It does not solve equality for a previously
prescribed arbitrary dyadic onset, select a replacement upper integer,
or instantiate any research data in this turn.

No blocking error was found in the inspected phase expansion,
four-onset lemma, rational winner test or finite selector cost. The
result depends on the inherited Note45 saddle branch and Note54 full
onset/join ledger; those complete chains have not been independently
reviewed here.

## Checks of the new analytical steps

1. **Actual saddle and logarithm.** The expansion is for
   p=w+32alpha(p), with the full M and determinant B. Stirling is used
   at Re p>2. Its identity agrees with EV11 by analytic continuation
   from p>2, fixing the phase lift. The comparison point q=ix/2 is used
   only in analytic Taylor/log estimates. EF3 is not applied at w or q.

2. **Phase coefficients.** The exact completion
   alpha0 v-v^2/64=16alpha0^2-(v-32alpha0)^2/64 pays the saddle shift.
   The imaginary contributions are x(L-1)/4, pi/8, 3pi/4 and4pi L.
   Thus the constant is7pi/8 and the logarithmic correction is4pi L.
   The displayed modulus remainder pays Taylor, log p, rational,
   log-Gamma and determinant terms separately; 2^16(1+log x)^2/x
   is a safe upper bound.

3. **Quantitative separation.** The coefficient vector(-4,8,-5,1)
   annihilates the 2^j and j2^j terms and constants, and sends j to1.
   The normalized combination therefore equals4 log 2 plus error
   <1/100 for K>=2048. Elementary 2/3<log 2<7/10 makes its
   integer distance >19/100. The coefficient absolute sum18 yields
   one individual distance >19/1800>1/100. This is a four-candidate
   statement, not a claim that every candidate is noninteger.

4. **Absolute precision and rational decision.** The elementary
   provider precision P=ell+ceil(log_2(ell+1))+20 pays the factor
   2^ell ell in the leading phase. The normalized center error is
   <2^-19. Radius1/1000 intervals enclose the true phase. At least one
   interval lies strictly in(n-1+1/200,n-1/200), and both tests are
   finite rational comparisons. Exact rational ties mean rejection;
   the four-onset lemma ensures a different acceptance if needed.
   No equality oracle, indefinite precision refinement or test of
   “the first exact noninteger phase” is hidden in winner selection.

5. **Elementary provider cost.** Fixed-length Machin and atanh sums
   supply pi, log 2 and log pi. Rounding the Machin rational to a
   dyadic before the log pi series keeps its ratio numerator and
   denominator at O(P) bits. Explicit factorial/base common
   denominators give O(P^2) operand bits. Note60's inflated
   2^100(P_*+1)^10 bit and2^20(P_*+1)^3 storage bounds safely cover
   the four finite sums, rounding, rational division and comparisons.
   This is a bound in K, not in log K, and not a full tuple cost.

6. **Onset and downstream order.** K includes C_b^+=(1+c_b)C_b,
   target delta=theta/64 and the pre-switch bridge maximum in Note54 D,
   as well as all exterior gates. Each candidate exponent is larger
   than this sufficient threshold; the inherited monotone inequalities
   remain true. The winner is selected before X0,R_c,L,sigma, source
   tolerance or coefficients. The original n=ceil(Q) and exact phase
   inverse then define the original family member. No source from a
   rejected candidate is reused at the winner.

The principal issue found during analysis was contractual: the
four-onset route cannot recover a previously fixed exponent. This was
made explicit to the author, who replied **“Use existing onset freedom.”**
The note records the bounded scope throughout. The final proof also
avoids an invalid extension of EF3 and pays absolute rather than merely
relative phase precision. These issues are resolved in the written
construction rather than deferred as unproved assumptions.

## What remains and status

The discrete step can be appended to Notes54,58,59's finite provider
and construction recipes. No new analytic equality payment is required
for this free-onset selector. The cost of constructing a sufficient K,
the phase inverse, source and evaluated complete tuple is separately
accounted for by those notes; Note60's polynomial selector cost is not
a polynomial complete-runtime theorem.

The next analytical question is a useful carrier-aware working-error
and continuous-integration estimate improving Note59 EV14--EV20's
coarse inverse-q dependence. Efficient gamma and flat-profile providers
are additional performance tasks. No universal lower bound or
impossibility follows from the current scheme's expense.

**HDA-17 Partial, HDA-18 Gated, HDA-20 unfulfilled** remain. The generic
phase selector can also apply to colliding controls with the same gamma
model; it is no sign or collision certificate. Note60 names the full-source
premises of its IC23 application and the controls that lack them.

Zero numerical, exact-rational or machine-symbolic research executions.
No evaluated phase, source coefficient, field/gamma sample or interval
campaign; all reasoning and operation bounds were on paper. Housekeeping
hash/link/size checks and authorized chat capture carry no mathematical
validation. Manuscript/DRAFT_HISTORY unchanged; no snapshot or commit.
Next owner **Analysis — Sol**; distinct HDA-20 assignment remains with
Edward Baker.
