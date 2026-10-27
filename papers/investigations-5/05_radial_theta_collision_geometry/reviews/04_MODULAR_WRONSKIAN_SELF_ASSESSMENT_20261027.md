# Modular Wronskian self assessment

27 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort max**. Same assistant as the derivation; this is not independent mathematical review.

## Decision

[Note05][note] completes the second bounded RTC-03 test. The selected multiplier has an exact canonical nonlinear description, but its complete integrated current is the original boundary residual. On the unchanged canonical source, the actual integrand takes both signs for all sufficiently large positive lambda, uniformly for 0<=t<=1/2. Stop the proposed automatic sign and everywhere-positive-integrand argument. Retain broader signed comparisons and different coupled currents as open questions.

## Mathematical checks

| Item | Assessment |
| --- | --- |
| Source and frequency normalization | x=2u, s=exp(2x), lambda=a^2/4 and B=-8H are unchanged. The factor g=exp(tx^2/4+x/2)K(Dell+ell^2+ell) agrees with Note03's complete source. |
| Nonlinear input | The scaled alpha, beta, eta system follows from Proposition1, equation(8), of the versioned primary source and E2=12 eta_Weierstrass/pi^2. The source-coordinate generator is not physical heat. Canonical initial data and Jacobi's algebraic relation are retained. |
| Weight and boundaries | w=4alpha beta/(alpha+beta)^2, (log w)'=2(alpha-beta), w(0)=1, w'(0)=0. The full integrand is -(wW)'; the infinity boundary vanishes only with the selected source tails. A finite cutoff retains its boundary term. |
| Conjugated response | U=sqrt(w)Y still has source sqrt(w)g. Its first derivative and potential corrections are present. The natural Green factor 1/w recovers the original forcing integral. No bounded operator similarity is claimed as w tends to zero. |
| Source derivatives | Exact polynomial differentiation gives P0, P2 and P4 in Note05(10), with odd derivatives one and three zero. Heat multiplication contributes tP0/2 to order two and 3tP2+3t^2P0/4 to order four. |
| Rational bounds | The arctangent and exponential remainders, full theta tail, and v in (47/10,49/10) are explicit. Monotonic endpoint polynomial bounds yield the discriminant upper bound -5936/5 after division by K_*^2 for the entire t interval. These are sufficient bounds, not optimized or measured constants. |
| Frequency asymptotics | Four integrations of the resolvent identity suffice. Differentiating the remainder uses an integrable first source moment and the displayed lambda derivative bound. The expansions for Y, Z and their x derivatives hold uniformly on any fixed source-coordinate compact set and the declared t slab. |
| Actual sign change | At x=0 the leading coefficient is uniformly negative. Its full integral is zero because it is a complete derivative with both endpoints zero. The common delta0, X and positive point margin follow from compactness and uniform tails; a uniform large-lambda remainder then transfers both signs to the actual integrand. There is no numerical onset claim. |
| Control | The exact Gaussian control has W=8x exp(-2x^2), and the weighted integrand is its negative weighted derivative. Its integral stays zero with this same modular weight. The control lacks the actual theta source relation. |

The [standalone checker][checker] and [record][record] pass. They verify identities as polynomials and the source enclosure using rational arithmetic. The convergence, uniform asymptotic remainder, imported identities and sign-change proof are analytical arguments; the checker does not certify them by sampling. No physical theta values or events are sampled.

## Scope and continuation

The global integral equality is not a proof that every estimate using the weight is useless. The canonical sign-change proposition rules out an unconditional one-sign integrand on the stated slab and all positive frequencies; it does not rule out signed cancellation, a restricted physical domain, a different current, or a bound using additional event conditions. It supplies no collision exclusion at any multiplicity and does not settle the positive threshold or time-zero simplicity questions.

The declared construction meets its stopping rule. No RTC-04 characteristic problem or RTC-06 numerical consumer has emerged. A next return must specify the independent signed information it intends to acquire, rather than enlarging the same multiplier family without a consumer. Independent review remains outstanding. No manuscript milestone or investigation closeout is declared.

[note]: ../notes/05_MODULAR_WRONSKIAN_WEIGHT_AND_CANONICAL_SIGN_OBSTRUCTION_20261027.md
[checker]: ../numerics/04_check_modular_wronskian_20261027.py
[record]: ../numerics/04_MODULAR_WRONSKIAN_CHECKS_20261027.json
