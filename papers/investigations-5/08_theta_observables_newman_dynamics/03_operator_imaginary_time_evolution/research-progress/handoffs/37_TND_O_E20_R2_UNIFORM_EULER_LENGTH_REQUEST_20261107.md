# E20 r2: uniform obstruction for growing finite Euler products

7 November 2026, America/New_York. Prepared for Edward Baker with substantial OpenAI Codex assistance. B04 r5 lead selected gpt-6-astra/ultra; r2 executor selected gpt-6.1-sol/ultra. Root configuration unavailable. These are dispatch records, not backend verification.

**ID:** TND-O-E20 r2. **Type E.** Parent: B04 r5, Decision17 §5.1. Prerequisite: completed E20 r1 Note28 and return36. This separately frozen revision extends the uniformity target; it does not alter the r1 request or evidence. It is the one focused height/polynomial-length clarification within the first of the same two mechanisms. No third mechanism or renewed approval.

## Fixed source, domain and statement

Retain exactly Note28's q(s)=(s−1)/s, F_Q, c_Q, probability strip measure, ε_Q, U0, k1 and λ=0. Fix 0<θ<17/33 and a fixed nonzero 0≤φ≤1 in C_c∞((1,2)). Write S=T/2. For each T choose any integer Q=Q(T)≥2 with primorial P_Q=∏_{p≤Q}p≤S^θ. Q is fixed throughout the center average X∈[T,2T]; do not select a different Q for each X.

Prove uniformly over all these Q that

 (1/T)∫_T^(2T) ε_Q(X)^2 dX ≥ c_(θ,φ) sqrt(log(T/2)) − C_(θ,φ),

for all sufficiently large T, with a displayed positive c_(θ,φ). Dependence of thresholds and O-constants must be θ,φ and explicitly chosen auxiliary ε only, never Q. Non-effective constants imported from the primary mean-square theorem must be identified honestly. This is a lower bound on the actual quadratic residual, not on J0, and not an existence assertion for nonreal zeros.

## Fixed proof route

1. Apply checked BCR v1 Theorem1 directly to the padded polynomial with a_n=μ(n)1_(n|P_Q), N=S^θ, |a_n|≤1. Do NOT substitute Q(T) into r1's O_Q(1) result. State the source's uniform coefficient convention.
2. Derive the exact factorization, where κ_Q=∏(1−1/p):

 Σ_{d,e|P_Q} μ(d)μ(e)/[d,e] {log[t(d,e)^2/(2πde)]+2γ}
 =κ_Q{log(t/(2π))+2γ+2Σ_{p≤Q} log p/(p−1)}.

Pay the positive sign of the added prime sum by the two mixed prime-divisibility terms. Dropping it gives a uniform lower main term.
3. Prove the elementary bound for any finite prime set of product L:

 κ≥e^(−2/log3)/(2 sqrt(max(3,log L))).

Use y=max(3,log L). The product over small primes is at least half the product of all odd factors 2j/(2j+1) up to y, at least 1/(2sqrt(y)) by induction. For primes>y, −log(1−1/p)≤2/p and their number≤logL/logy, giving total log loss≤2/log3. No PNT or numerical estimates.
4. Since logP_Q≤θlogS, for logS≥3/θ obtain κ_Q logS≥e^(−2/log3)sqrt(logS)/(2sqrtθ). Retain all uniform constants and the negative constant from log(u/(2π))+2γ after t=Su. The remainder divided by S is

 O_(θ,φ,ε)(S^(−17/20+ε+33θ/20)+S^(−2/3+ε)).

Choose explicitly 0<ε<min((17−33θ)/20,2/3). Record why the error is uniform in Q and decays.
5. Use Note28's exact nonnegative convolution and x=2t conversion, not a sharp-cutoff import. One permissible positive coefficient is

 c_(θ,φ)=k1 e^(−2/log3)(∫φ)/(4 U0² sqrtθ).

Prove this or a smaller explicit coefficient; any harmless conservative factor correction is permitted. State the endpoint trimming threshold from supp φ.

## Boundary and consumer

This rules out uniform all-center bounded quadratic residuals for the stated growing finite Euler products and length regime. It says nothing about every individual center, adaptive per-center Q, longer products, arbitrary mollifiers, defect-conditioned centers, shrinking-width replacements, or signed logarithmic cancellation. It does not prove RH or a collision. The Gaussian hierarchy remains available. Run relevant controls by reference to Note28/Decision17 with their exact failed premises; do not re-run finite experiments.

## Ownership, output and completion

Write only notes/29_TND_O_E20_R2_UNIFORM_EULER_LENGTH_OBSTRUCTION_20261107.md and research-progress/handoffs/37_TND_O_E20_R2_UNIFORM_EULER_LENGTH_RETURN_20261107.json. Preserve Note28 and return36 byte-identically. Include author, LLM acknowledgment, selected model/effort, version hashes, quantitative proof, uniform regime, all failure scope and a consumer assessment. Root owns all shared files and chat capture. No subagents, numerics, manuscript edits or commits. One bounded correction pass for constants, coefficient sign, length normalization or cutoff handling. If the primary theorem does not support uniformity, preserve the failed clause and return to B04; do not change multiplier class. E21 will audit r1/r2 and Decision17 mechanism2 together after this return.
