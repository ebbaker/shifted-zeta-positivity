# E20 r1: paid quadratic Green comparison and fixed-Euler obstruction

7 November 2026, America/New_York. Prepared for Edward Baker with substantial OpenAI Codex assistance. Conceptual route selected by gpt-6-astra/ultra in B04 r5; executor to be explicitly selected gpt-6.1-sol/ultra. Root configuration unavailable. Tool selections are not independent backend verification.

**ID:** TND-O-E20 r1, parent TND-O-B04 r5. **Type E.** The fixed mathematical route is ready. This request is frozen before dispatch; exact source hashes are in inputs36. Root owns the sole Register02, Overview02, manuscript and indexes. Executor owns only Note28 and return36. The author has already received the high-level baseline and a second check-in describing the quadratic comparison, missing residual smallness, and compact-source/remote-tail issue. No new approval is required.

## Domain and normalization

Time λ=0 only. Integer Q≥2, x,X real. Set s(z)=1/2−iz/2, a=π/8, K(x)=1/(16 cosh(ax)), q(s)=(s−1)/s, M_Q(s)=∏_{p≤Q}(1−p^(−s)), F_Q(z)=q(s(z))ζ(s(z))M_Q(s(z)), c_Q(X)=F_Q(X+4i). Cancellation at s=1 is analytic. All M factors are zero-free on Re s≥1/2. Use the complete probability measure μ_X on y=0 and y=8, with density K(x−X) on each line. Reuse exact J0 and its pole-corrected prime representation from Note25/Decision15; do not assign an Euler product at λ≠0.

## Fixed theorem package

1. Prove c0≤|c_Q(X)|≤U0 uniformly in X,Q, c0=(3/5)ζ(5)/ζ(5/2), U0=ζ(5/2). Justify complete complex harmonic mean ∫F_Q dμ_X=c_Q and harmonic invariance of the Green log functional when replacing H0 by F_Q. Real-boundary log singularities and the removable zeta pole must be paid.
2. Define ε_Q(X)^2=∫|F_Q/c_Q−1|²dμ_X. Prove ε²=∫|F_Q/c_Q|²dμ_X−1 and J0(X)≤(1/2)log(1+ε²). A zero y≥d>0, |x−X|≤r forces m=sin(a)d/cosh(ar), so ε²<exp(2m)−1 suffices for excluding that class. Classify this as a paid comparison only: no unconditional small residual is presumed.
3. Pay complete-source approximation on a finite central interval only. Here F_Q=16π^(s/2)M_Q(s)H0(z)/(s²Γ(s/2)). For |x−X|≤R and y∈{0,8}, use the explicit supremum B_Q(X,R) of this factor and the complete source error δ_H(N,U;8)≤[5C2(N)J_{0,2}(0,8)+B0 J_{0,2}^{>U}(0,8)]/2. Derive the formula directly from the inherited source majorant if its notation differs. The error is B_Qδ_H/c0 in the probability L² norm. Do not insert a uniform absolute H error on the full gamma-renormalized boundary.
4. Let C_Q=∏_{p≤Q}(1+p^(−1/2)), B=2+|X|. Prove |F_Q(x)|≤C_Q(2+|x|) and |F_Q(x+8i)|≤ζ(9/2), using fractional-part continuation and the rough Euler product. One allowed tail target is

 τ_Q(X,R)=exp(−aR)/(2a) × { (C_Q²/c0²)[(B+R)²+2(B+R)/a+2/a²]+ζ(9/2)²/c0²+2 }.

Verify or conservatively repair its numerical factors. If εhat_R is the compact residual norm from the finite-source field with exact c_Q, prove ε≤εhat_R+B_Qδ_H/c0+sqrt(τ_Q). Give an explicit absolute-tail prescription for c_Q from its safe Euler logarithm (integer cutoff, finite Q exact), and, if approximating c_Q, propagate that denominator error with a positive lower margin. Show a valid order of limits for fixed or varying X,Q,d,r: choose R for tail, then N,U for compact source, then center precision. The theorem must be useful for arbitrarily large X/index; no assertion of inexpensive computation or residual smallness.
5. Fixed-Q obstruction, using only the checked BCR v1 Theorem 1: expand M_Q as a finite polynomial over divisors of the primorial and verify κ_Q=Σ a_d a_e/[d,e]=∏_{p≤Q}(1−1/p)>0. For any fixed nonzero 0≤φ≤1 supported strictly inside (1,2), establish a lower bound of the form

 (1/T)∫_T^{2T} ε_Q(X)^2 dX ≥ [k1 κ_Q/U0²](∫φ) log T + O_{Q,φ}(1),
 k1=∫_{−1}^1K(u)du=(1/π)atan(sinh(π/8)).

Verify the x=2t scaling, center-endpoint trimming and complete convolution. A smaller explicit positive coefficient is permitted if needed. This is failure of uniform all-center smallness for each fixed finite Q, not failure at every center or a theorem for Q=Q(T). Track actual primorial length and permissible zero-padding; do not promote fixed-Q asymptotics to growing Q. No RH, no numerical tests.

## Controls, limits and consumer

Use result-summaries12 and avoid01/02/07. The Jensen comparison is general analytic information; finite canonical Euler arithmetic enters the fixed-Q moment calculation. State exactly which premises the positive-source Euler controls, weighted-square/reflected/smooth controls fail. Naming the literal theta source does not supply the missing residual estimate. State that small d, exceptional centers, finite-height coverage, growing Q, and nonzero Newman time remain outside the proved exclusion. Gaussian and other metrics remain available.

## Outputs, completion and bounded repair

Write only notes/28_TND_O_E20_PAID_QUADRATIC_GREEN_COMPARISON_20261107.md and research-progress/handoffs/36_TND_O_E20_PAID_QUADRATIC_COMPARISON_RETURN_20261107.json. Include Edward Baker, LLM assistance, actual selected model/effort, source versions, theorem/proof, precise failure class, and the consumer’s remaining dependency. One bounded repair is permitted for normalization, conservative tail constants, denominator handling, and the smooth moment cutoff. A changed multiplier class, scientific mechanism or joint-Q target returns to B04 before work. No manuscript, register, bibliography, chat-history, numerical campaign, commit or push. Return once this package or an exact failed clause is complete; E21 will audit the actual returned claims separately. No novelty or specialist-independence claim.
