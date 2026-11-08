# TND-OG-E01 r1: short-mollifier normalized residual floor

7 November 2026, America/New_York. Prepared for **Edward Baker** with substantial OpenAI Codex assistance. Request author: **gpt-6-astra / max**, branch chat0001. **Type E; recommended gpt-6.1-sol / ultra.** The route and success test are fixed; execution model/effort must be recorded when work actually starts. This is a frozen request, not an execution return.

Parent: [B01 decision](../../brainstorm/notes/01_TND_OG_B01_RESOLVENT_CONDITIONING_DECISION_20261107.md). Status owner: [sole register](../01_TND_OG_GREEN_RESOLVENT_RESEARCH_PROGRESS_20261107.md). Exact input versions: [inputs02](02_TND_OG_E01_INPUTS_20261107.json). Primary inspection/reading-copy provenance: [source-use01](../../references/01_TND_OG_B01_SOURCE_USE_20261107.md).

## 1. Fixed objects and proposed theorem

Use the **literal complete canonical H₀=ξ(s)/8** only at Newman λ=0, with s(z)=1/2−iz/2. No Euler product at another time. Set a=π/8, K(u)=1/(16 cosh(au)); μ_X has density K(x−X) on each of y=0,8 and total mass one.

Fix **0<θ<1/2**, T→∞, S=T/2, and N≤S^θ (integer). For each T allow an arbitrary complex polynomial

\[
A_T(s)=\sum_{n\le N}a_n n^{-s},\qquad a_1=1,\quad |a_n|\le1.
\tag{E1}
\]

Freeze this one polynomial for all x and all centers in

\[
L_T=a^{-1}\log T,\qquad I_T=[T-L_T,2T+L_T],\quad |I_T|=T+2L_T.
\tag{E2}
\]

Let q(s)=(s−1)/s, F_A(z)=q(s(z))ζ(s(z))A_T(s(z)), c_A(X)=F_A(X+4i), and

\[
\epsilon_A(X)^2=\int|F_A/c_A(X)-1|^2d\mu_X,
\quad V_A(X)=\int|F_A|^2d\mu_X-|c_A(X)|^2.
\tag{E3}
\]

Prove, or return the precise failed clause in, the uniform target

\[
\liminf_{T\to\infty}\inf_{A_T\ {m satisfying}\ (E1)}
\frac1{|I_T|}\int_{I_T}\epsilon_A(X)^2dX
\ge\frac1{12\zeta(5/2)^4}.
\tag{E4}
\]

In particular seek the weaker finite conclusion ≥1/(24ζ(5/2)^4) for all sufficiently large T, with onset depending on θ and the imported theorem's common coefficient bounds, **not** on the individual polynomial. Do not invent a numerical onset.

## 2. Fixed proof route and mandatory checks

1. **Analytic normalization.** Reuse parent Note28's fractional-part continuation to cancel the zeta pole. Prove F_A is holomorphic on the strip, of polynomial horizontal growth, with complex harmonic mean ∫F_A dμ_X=c_A(X). Show

   \[
   c_*:=\frac35\frac{\zeta(5)}{\zeta(5/2)}[2-\zeta(5/2)]
   \le|c_A(X)|\le U:=\zeta(5/2)^2.
   \tag{E5}
   \]

   Use |A(5/2−it)|≥2−ζ(5/2)≥1/3. Establish V_A=|c_A|²ε_A²≥0 and ε_A²≥V_A/U². Center dependence is retained throughout; replacing c_A(X) by 1 is forbidden.

2. **Green consumer with multiplier zeros.** The quotient F_A/H₀ is D₀(z)A_T(s(z)), D₀=16π^(s/2)/(s²Γ(s/2)). D₀ is zero-free on this strip but A need not be. Prove logarithmic boundary integrability and

   \[
   0\le J_0^{\rm G}\le J[F_A]
   =J_0^{\rm G}+J[A_T\circ s]
   \le\tfrac12\log(1+\epsilon_A^2),\quad J[A_T\circ s]\ge0.
   \tag{E6}
   \]

   A permitted route for the multiplier is the bounded subharmonic function (1/2)log(|A|²+δ²), followed by monotone convergence as δ↓0, using the safe-center floor and bounded upper values. This pays boundary zeros without pretending A is zero-free. Alternatively use a complete Green formula with all multiplier zeros and tails. Do not double-count the zeta pole: the separate prime representation retains its plus G(X,1), while F_A has already cancelled the pole.

3. **Primary moment and coefficient uniformity.** Use only Radziwiłł, arXiv:1207.6583**v3**, §1 Proposition B (Soundararajan), at fixed θ<1/2, with its coefficient condition; inspect §7, (13)–(16), Lemmas 9–14 as needed to justify uniformity for the common |a_n|≤1 class. The imported lower bound concerns |1−ζA|², not |ζA|² and not ε_A². Prove the needed first mean S⁻¹∫_S^(2S)ζ(1/2+it)A(1/2+it)dt=1+o(1), uniformly. A permitted elementary proof shifts the finite rectangle to Re s=2; bound horizontal edges by fractional-part continuation with cutoff of order S and |A|≤2√N. No pole lies inside the rectangle at heights [S,2S]. This should give edge error O(S^((1+θ)/2)log S) and an absolutely convergent right-line Dirichlet mean. Retain complex coefficients: the negative-t boundary uses conjugated coefficients, still in (E1). Conclude the critical square mean ≥1+1/θ+o(1).

4. **Uniform safe-line mean.** Write ζ(s)A_T(s)=Σb_n n^(−s), |b_n|≤τ(n). On Re s=5/2, prove the long-interval mean square is at most Στ(n)²n^(−5)+o(1), uniformly in A_T. Absolute off-diagonal summation is sufficient: |log(n/m)|≥(n−m)/n for n>m, and τ(n)≤2√n. The resulting sums are bounded by constants times Σ_m H_m/m³. The factor |q|≤1 only improves the upper bound for |c_A|². Use the deliberately crude

   \[
   \sum_{n\ge1}\tau(n)^2n^{-5}
   \le1+4\sum_{n\ge2}n^{-4}\le17/12.
   \tag{E7}
   \]

   Normalization is by the actual interval length. Bounded c_A pays the O(log T) padding without a new mean theorem.

5. **Complete convolution and x=2t.** Integrate V_A over I_T. Drop only the nonnegative top-boundary square; retain the negative center square. For each x∈[T,2T], all centers |X−x|≤L_T lie in I_T, so its lower-boundary center mass is at least ∫_(−L_T)^(L_T)K→1/2. Tonelli applies to the complete nonnegative square. Use |q(1/2−ix/2)|=1, x=2t and S=T/2 exactly. Combining steps 3–4 gives a variance lower allowance (1+1/θ)/2−17/12>1/12 and then (E4). Do not claim the same result for an unpadded interval or center-adaptive A.

6. **Exact-source and tail ledger.** The proof uses exact H₀ and does not need a numerical source approximation. Still state how E6 remains a paid complete-source certificate: adapt Note28 §§3–6 with C_A=Σ_(n≤N)|a_n|n^(−1/2)≤2√N, center floor c_*, and upper-line bound |F_A(x+8i)|≤ζ(9/2)². Compact D_A errors, both remote tails, safe-center acquisition and denominator propagation must be displayed or explicitly derived from those substitutions; A's possible zeros must not be divided out. The order remains boundary radius first, complete arithmetic/radial cutoffs next, then safe-center precision. It is finite acquisition per tuple, not uniform useful cost, residual smallness or a finite run. No growing derivative order is used.

## 3. Completion, scope and stop

Success is a written proof of the stated uniform floor and its correctly scoped consumer consequence, with exact theorem/normalization/error payments. The result would obstruct a uniformly small **sufficient quadratic residual** for (E1) on (E2), in particular the vanishing thresholds e^(2m(d,r))−1 as d↓0. It must not be presented as a lower bound on J, failure at every center, nonreal-zero existence, or failure of Green methods generally.

Excluded from this request: θ≥1/2 (including the gap to 17/33), longer mollifiers, adaptive A(X), optimizing coefficients, unpadded intervals, nonzero Newman times, a numerical onset, new kernels, or a manuscript. Every control comparison names the absent canonical premise, following Note01 §5 and controls12. The exact canonical source is used in the application; the new fixed-prime family is only a methodological screen.

One bounded repair of constants or an elementary intermediate bound is permitted. If primary uniformity, the normalized variance transfer or the multiplier/source accounting cannot be paid within this route, stop with that precise clause and return it to **B01 r2** before changing mechanism or coefficient/interval class. A conditional transfer alone must be labelled conditional.

Write `notes/02_TND_OG_E01_SHORT_MOLLIFIER_RESIDUAL_FLOOR_<DATE>.md` and an exact return under `research-progress/handoffs/`; update the sole TND-OG register and concise continuation. Do not alter frozen requests, parent sources, shared registers or sibling work. E02 follows only an actual E01 return and a frozen claim-level assessment; it should also assess Note01 §§1–5. Keep one writer per artifact. No subagent or model switch is automatically authorized by this packet; the author chooses execution. Record actual model/effort, preserve unique chat-history registration, and follow the repository's bounded final-capture workflow.
