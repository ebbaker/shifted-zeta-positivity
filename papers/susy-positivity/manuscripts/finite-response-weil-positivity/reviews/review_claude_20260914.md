# Review of *Finite response matrices for Weil positivity* — final machine review before human review

Review date: 14 September 2026. Reviewer: Claude (Anthropic, model `claude-fable-5-1`), working in Cowork. This is an AI mathematical review with independent recomputation; it is not a human or external referee review and does not fill any line of `REVIEW_LOG.md`.

**Material reviewed.** `manuscript.tex` (M, 7 pages), `derivations.tex` (D, 17 pages), `preamble.tex`, `references.tex`, both PDFs, `README.md`, `EVALUATION.md`, `BUILD.md`, `VALIDATION.json`, `SOURCE_RECORD.json`, `REVIEW_LOG.md`, and everything in `reviews/`. Tied to repository HEAD `7bed51d` on branch `susy-positivity` (working tree clean) and to the SHA-256 values recorded in `VALIDATION.json`, which I re-hashed and found to match for all 19 listed files (in particular `manuscript.tex` `96a33211…`, `derivations.tex` `476c9e6a…`). Line numbers below refer to these `.tex` files. Both prior check scripts replay on these sources; their recorded outputs are reproduced up to floating-point noise below 1e-13.

## 1. Assessment

I stepped through every displayed formula, constant, inequality direction, domain statement and limiting argument in D and every claim in M. **I found no mathematical error.** The chain

Weil criterion (Suzuki normalization) → closed logarithmic form → explicit boundary correction → unconditional high-sector coercivity → Schur identity on the full form domain → RH ⇔ S_n ⪰ 0 for all n

is correct as written, and the unconditional pieces (Theorems 3.1 and 5.1, Corollary 5.2, the identities of Sections 8–13 of D) hold. The three qualifications of the Codex review of 13 September have been implemented faithfully; I checked the new text (certified cutoff, gamma bridge, projected source, parity split, compressed tail, variational identity, central-row formula) rather than the response's description of it.

Beyond re-deriving the algebra, I verified the two load-bearing identities against objects the paper does not use: the arithmetic normalization of Q_L against the **actual zeros of ζ** (agreement to 8e-23 for a compactly supported input at L = 3, while the individual terms are O(1)), and the boundary identity T_L = b(H_N) + K_L against an independent method-of-images kernel (agreement to 1e-14 at three lengths, with the boundary term carrying a third or more of the energy). I also assembled the full arithmetic operator in the cosine basis at L = 1 and L = 2 and computed the matrices S_1 and S_2 in floating point and in 50-digit arithmetic. Nothing in these computations contradicts the paper; several things they reveal should, in my view, be said in the paper before it goes to arXiv. They are listed in Section 3 as recommendations, not corrections.

**Recommendation.** Ready for the human review of the calculations. Before arXiv: adopt items 3.1–3.4 (wording and framing, no new mathematics), fix the placeholders in Section 5, and decide whether to add the length-one computation described in 3.3.

## 2. Independent verification performed

All scripts are new implementations in `reviews/check_claude_20260914/`; none imports or replays the paper's or the previous review's code. "Exact" means `Fraction` arithmetic; "mp" means mpmath at 25–50 digits; "fp" means double precision.

| # | What was checked | Method | Result |
|---|---|---|---|
| 1A | Suzuki's functional (D (2.1)) against Σ_ρ Φ_g(ρ) for F = e^{-x²/2}cos 30x | mp; 300 zeros, prime powers to 2·10⁶ | zero sum − formula = 5.8e-20 |
| 1B | **M's operator form Q_L[f] = t_L + w₀‖f‖² + 2\|⟨c,f⟩\|² − 2\|⟨s,f⟩\|² − primes** against Σ_ρ 2\|F̂(γ)\|² for f = sin⁴(πx/3) on (0,3) (12 active prime powers) | mp; 300 zeros, tail 6e-23 | pieces 2.478, −4.407, 2.648, 0, −0.719 sum to 1.3269558138e-8; zero sum 1.3269558138e-8; difference −8e-23. Also equals Suzuki's functional on g = F∗F̃ to 8e-24 |
| 2a | Kernel of K_L: image sum Σ_m[n(x+y+2mL)+n((2m+2)L−x−y)+n((2m+2)L±(x−y))] versus the direct mass sum of K_a in M (3.1) / D (5.1) | mp | 1.4e-20 |
| 2b | **T_L = b(H_N) + K_L** (Thm 3.1, D (5.3)): Fourier side (1/2π)∫b(τ²)\|F̂\|² versus Σ b_j\|⟨e_j,f⟩\|² + ⟨f,K_L f⟩ with the image kernel, f = sin⁴(πx/L) | mp + scipy dblquad | L = 1: 1.18897743 vs 0.71877 + 0.47020, diff 4e-14; L = 1.3: 3e-17; L = 2.5: 2e-16 |
| 2c | Column formula (3.3)/(6.1) and entries (3.4)/(6.2) against quadrature | mp | 3.4e-21 |
| 2d | Full-column tail M (3.2) / D (6.5): computed partial tails / bound | mp | max ratio 0.55 (< 1) |
| 2e | Shift entries D (6.6), pole coefficients c_j, s_j (D §6.3), ‖c‖², ‖s‖², ⟨c,s⟩ = 0 | mp | 3.5e-21, 7e-22, exact |
| 3i | Central-row formula r_h(q): equals max row sum for h < 40, six values of q; chain-matrix operator norm ≤ r_h | fp | exact; ratio ≤ 1 (= 1 at h = 2) |
| 3ii | Compression (1500 modes) of each prime term ≥ −(log p) r_h(p^{-1/2}); of R_L ≥ −β_L | fp, L = 1, 2 | all hold; p = 2 at L = 1 is sharp (−0.490129 both) |
| 3iii | Cutoff: N(1) = 4 (b₃ = 5.7772 < β₁ + 1/16 = 5.9670 < b₄ = 6.0651), N(2) = 131; H − Λ ⪰ 0 on compressions | fp | min eig(H−Λ) = 0.042 (L=1), 1.48 (L=2) |
| 3iv | Even/odd decoupling of W_L (hence of S_L) | fp | max mixed entry 2e-12 |
| 3v | Galerkin enclosures U_K, L_K of Thm 5.1 at L = 1 for K = 20…6000 | fp | monotone, nested, converge; see 3.3 |
| 4 | 50-digit spectrum of W_K and of S_1, S_2 | mp, K ≤ 200 | see 3.3 |
| 5 | Sections 12–13 rationals: 41611/7000, 64-term sum > 3007/500, margin 99/14000, 26/125, −2979/6125, 29/56, six-term e^{1.1} > 3, all auxiliary bounds; tail constants D (3.4), (6.3), (6.5) at J = 1, 5, 40; gamma series = Re ψ identity; w₀ closed form; contact integral = (ψ(½)−ψ(¼))/2; remainder-kernel bound of D §5.1 | exact / mp | all pass; τ²·[b(τ²) − (log τ − log 2 − ψ(¼))] → −1/24, confirming O(τ⁻²) |
| 6 | Mechanism of the smallest eigenvalues (Section 3.3 below) | fp + 300 zeros | see 3.3 |
| — | References: Suzuki 2606.09096v2 (title, author, v2 of 17 Aug 2026, §1.1 formula, criterion for C_c^∞), CCM 2511.22755 (Prop. 3.4 is the core/limit-of-smallest-eigenvalue statement; §4 explicit matrices; §5 truncations E_N and ε_N), DLMF 5.4.13/5.7.6/5.11.2, Kwaśnicki–Mucha 1707.02475, Yafaev 1210.5709 (Hankel kernel t⁻¹ = Carleman) | web | all as cited |
| — | PDFs: 7 and 17 pages, built from the current sources, no unresolved references | pdftotext | ok |

## 3. Recommendations before arXiv (no errors; framing and statement hygiene)

### 3.1 State the conjecture without the enclosure routine

**M lines 31–37 and 136–144; D §4.1 lines 254–308.** The conjecture is stated for "the matrix S_n defined in (4.1)", but S_n depends on the dimension N(n), and N(n) is produced by a search that depends on "deterministic rational enclosure routines" that the paper describes only schematically (D lines 281–299: "one can use Taylor series…", "fixing these routines… makes the search deterministic"). M is candid that "different admissible choices can change its matrices", but the effect is that Conjecture 1.1, as a mathematical statement, refers to an object that is not fully specified in the paper. Since Theorem 4.1 shows the sign of S_L is the same for **every** N with b_N > β_L + δ₀, the routine is not needed for the statement at all. I recommend:

> **Conjecture 1.1.** For every integer n ≥ 1 and every integer N with b_N > β_n + δ₀ (equivalently: for one such N), the matrix S_{n,N} = A − B\*H⁻¹B of (4.1) is positive semidefinite.

Then keep the certified search as a *remark on effectiveness* (it produces an explicit admissible N(n) without deciding an equality), and record that it is also legitimate to take the optional minimum N_min(n) or the explicit N = 4 at n = 1. This removes the dependence on an unstated implementation, keeps everything the paper proves, and is what a reader will want to quote. The same change simplifies the phrase "Its dimension is a prescribed integer N(n) selected by the terminating certification procedure" (M 32–33).

### 3.2 Say plainly how fast N(n) grows

**M lines 379–380** ("Present bounds may require very large dimensions as L increases") understates what the paper's own bound implies. Since β_L ≥ −w₀ + 2sinh(L/2) − L and the prime sum Σ_{p<e^L}(log p) r_h(p^{-1/2}) is of the same order e^{L/2}, while b_j = log(jπ/2L) − ψ(¼) + O(j⁻²), the certified dimension is N(n) = (2n/π)·exp(β_n + δ₀ + ψ(¼))·(1 + o(1)) with β_n of order e^{n/2}, i.e. **doubly exponential in n**. With the exact β_n of M (2.6):

| n | β_n | pole part 2sinh(n/2)−n | prime part | N(n) |
|---|---|---|---|---|
| 1 | 5.9045 | 0.042 | 0.490 | 4 |
| 2 | 8.7924 | 0.350 | 3.070 | 131 |
| 3 | 13.825 | 1.259 | 7.194 | 2.99·10⁴ |
| 4 | 22.637 | 3.254 | 14.01 | 2.68·10⁸ |
| 5 | 36.765 | 7.100 | 24.29 | 4.6·10¹⁴ |
| 6 | 62.019 | 14.04 | 42.61 | 5.1·10²⁵ |

One sentence and this table (or its first four rows) would make the "structural, not computational" character of the family explicit. It also motivates the parity-split even-sector bound β_L^{even} already recorded in D §6.4 and the rank-one treatment of −2ss\* noted below.

### 3.3 The matrices are nearly singular by design; say so, and (optionally) show S_1

This is the one substantive thing my computations add. Assembling W_L in the cosine basis (entries from D (6.2), (6.6), (6.7), with the digamma closed forms Σ_k 1/(a_k²+ω²) = Im ψ(¼+iω/2)/(2ω) and its ω-derivative for the rational mass sums) and computing S_L = A − B\*H_K⁻¹B with Galerkin dimension K:

* **L = 1, N = 4.** The eigenvalues of U_K are stable to six digits from K = 2000 on, the lower enclosure (residual Gram truncated at 6000 cosine rows) is below U_K by less than 3·10⁻⁶ at K = 4000, and the enclosure gap decays empirically like K^{-3/2} (4.9e-4 at K = 200, 1.4e-5 at K = 2000), versus the crude bound ‖B‖²(1+‖E‖/δ₀)²/d_K ≈ 80 of Theorem 5.1 (‖B‖ ≈ 0.63, ‖E‖ ≈ 1.76). The limit is
  S_1^{even} ≈ [[0.0081363, 0.0106320],[0.0106320, 0.0138958]], S_1^{odd} ≈ [[0.158804, 0.198410],[0.198410, 0.248392]],
  with eigenvalues **9.35·10⁻⁷** and 2.203·10⁻² (even block), 1.946·10⁻⁴ and 0.4070 (odd block); 50-digit compressions give 9.5·10⁻⁷ at K = 80, decreasing toward the double-precision value. So S_1 ≻ 0 numerically, but det S_1^{even} ≈ 2·10⁻⁸ against entries of size 10⁻².
* **L = 2, N = 131.** In 50-digit arithmetic the twelve smallest eigenvalues of the 200-mode compression of W_2 — and identically of S_2 = U_200 — are 6.5e-30, 1.6e-26, 2.5e-23, 2.5e-20, 1.6e-17, 6.4e-15, 1.6e-12, 2.6e-10, 4.2e-8, 4.4e-6, 2.1e-4, 8.3e-3: a super-exponential cascade, all positive, ten of them below double precision. (Compression eigenvalues are upper bounds for the true ones by min–max, so the true tail is at least this small.)

The mechanism is elementary and, I think, worth one remark in M §5 or §6: under the identity Q_L[f] = Σ_γ |F̂(γ)|² there are no zeros in |τ| < γ₁ = 14.13…, so functions supported on an interval of length L whose Fourier mass is concentrated in that window — of which there are about γ₁L/π ≈ 4.5 L, the prolate count — have Weil energy equal to the leaked mass outside the window, which decays super-exponentially with the mode index. I confirmed this directly: the eigenvector of the 9.35·10⁻⁷ eigenvalue at L = 1 has 99.987% of its Fourier mass in |τ| < γ₁, and its eigenvalue is reproduced by the zero sum (9.04·10⁻⁷ over 300 zeros plus a ≈3·10⁻⁸ endpoint-jump tail). At L = 2 there are ≈ 9–10 such directions, matching the cascade.

Consequences the paper should draw explicitly (they support, rather than weaken, its stated caution at M 316–317 and the tolerance form of Corollary 5.2):

1. Any certificate of S_n ⪰ 0 must have an enclosure gap below the smallest eigenvalue of S_n, which is ≈ 10⁻⁶ at n = 1 and at most ≈ 10⁻²⁹ at n = 2 (the compression value 6.5·10⁻³⁰ is an upper bound), and shrinks super-exponentially in n. The 2^{-m} tolerance of (5.3) is therefore informative only for m ≳ 20 at n = 1 and m ≳ 100 at n = 2. "Approximable entries" (M 234–236) is true but should not be read as "checkable".
2. The finite-mass scheme of D §10 is not the right tool even at n = 1: with K ≈ 10⁴ Galerkin modes needed to push the gap under 10⁻⁶, the O(J^{-1/2}) column tail η_{K,J} would require an astronomically large number of masses. The remedy is already in the paper implicitly: the kernel of K_L has the **elementary image representation** (verified to 10⁻²⁰) K_L(x,y) = Σ_{m≥0}[n(x+y+2mL) + n((2m+2)L−x−y) + n((2m+2)L+x−y) + n((2m+2)L−x+y)], n(t) = e^{-t/2}/(1−e^{-2t}), exponentially convergent in m, so every column W_L e_j is an elementary function and residual Grams need no mass tail. I recommend displaying this formula in D §5.1 (it is one line from the expansion of 1/(1−r_a²) already used there) and mentioning it in M after (3.4).
3. If Weil positivity on intervals of length 1 is not already covered by the explicit small-support results (Yoshida; Bombieri 2000; Connes–Consani's [2^{-1/2}, 2^{1/2}] range is length log 2 < 1 — this should be checked against the current literature), then a **rigorous** certificate that the two 2×2 blocks of S_1 are positive definite would be a genuine unconditional statement and the natural showcase for the paper. The numbers above say it is feasible with high-precision interval arithmetic, image-kernel columns, and parity-respecting Galerkin trials with K of order 10⁴. `EVALUATION.md` already suggests one worked enclosure; this is the concrete target.

### 3.4 Two wording points about "no finite collection suffices"

**D lines 568–570** ("It also shows that an arbitrary finite list of successful lengths cannot finish the proof") and **M 338–339** ("No finite collection of successful intervals or tolerances establishes (5.3)"). What the cofinal argument shows is that a finite list does not suffice *via this argument*; it does not prove that positivity on some fixed interval could not imply RH. That is exactly the localization question in the literature the paper cites: Yoshida proved unconditional positivity for sufficiently small support (so small fixed lengths certainly do not suffice), and — per Suzuki §1 — Yoshida's Theorem 2 identifies RH with the *non-degeneracy of the completion* of the localized form on a fixed interval, which is a fixed-interval statement of a finer kind. Rephrase as "does not by itself establish", and consider one sentence relating Conjecture 1.1 at fixed n to that refined localized criterion. (Not an error: the theorem statements are unaffected.)

### 3.5 Small expository gap in D §9

**D lines 701–707.** The proof that R_K → 0 in norm says "Since EY_K → EH⁻¹B in norm and the input space is finite dimensional, R_K → 0". One step is missing: R_K = (I−P_K)(B − EY_K) = (I−P_K)ΛH⁻¹B + (I−P_K)E(H⁻¹B − Y_K), and the first term tends to zero because ΛH⁻¹B is a bounded finite-rank operator (H⁻¹B has range in Dom H = Dom Λ) while I − P_K → 0 strongly. Add that sentence. Everything else in §9, including the inverse-order proof and the sign of the enclosure, is correct.

### 3.6 Minor items

* M 85–86: the remainder in b(τ²) = log|τ| − log 2 − ψ(¼) + O(τ⁻²) is −1/(24τ²) + O(τ⁻⁴); stating the constant is optional but costs nothing.
* M 127: "the even pole is nonnegative" is fine, but since −2ss\* is rank one, the odd-sector cutoff could be sharpened by a rank-one (Weinstein–Aronszajn) condition 2⟨s, Q(Λ′−δ₀)⁻¹Qs⟩ ≤ 1 instead of subtracting 2‖s‖² = 2sinh(L/2) − L from the diagonal; this removes the pole from β_L entirely. It does not change the double-exponential growth (the prime norm bound is also of order e^{L/2}), so this is optional.
* D 861: the phrase "by an integral tail" for 26/125 is correct; the sum itself is 0.16597, so there is slack.
* M 232 defines S_n := S_L|_{L=n}; Corollary 5.2 uses L_{n,K} without the corresponding sentence. One clause ("with L = n in (5.2)") would close the gap.

## 4. Section-by-section record for the human review

This list is meant to be read next to `REVIEW_LOG.md`. "Verified" means I re-derived the step by hand and, where a number or a formula was involved, recomputed it independently (Section 2). It is not a human sign-off.

* **D §2, M (2.1)–(2.4).** Verified: Suzuki's normalization (fetched and compared term by term, including e^{x/2}/(e^x−e^{-x}) = n_γ(x)); g(−r) = conj g(r); Re g = Re⟨F,U_rF⟩; K[F] = ∫₀^∞[2g(0)−g(r)−g(−r)]n_γ; the contact w₀ = −log 4π − γ − 2Σ(1/(2k+½) − 1/(2k+1)) = ψ(¼) − log π = −γ − π/2 − 3log 2 − log π = −5.37218; pole kernel 2cosh((x−y)/2) = 2cc\* − 2ss\*; prime coefficients (log p)p^{-m/2}, strict activity m log p < L. Cross-checked against the zeros (row 1B).
* **D §3, M 84–90.** Verified: partial fractions at z = ¼, t = √s/2 give (2/a_k)s/(a_k²+s); Plancherel/Tonelli bridge (3.2); one-mass minimizer û = a²F̂/(a²+τ²) and both output components; closed source and domain (3.3); dilation/mollification core proof (weights comparable for r ∈ [½,1]); compact embedding; scalar tail (3.4) with ∫_J^∞ 2(2x+½)⁻³dx = 1/(2a_J²).
* **D §4, M (2.5)–(2.8).** Verified: interval restriction lowers / zero extension raises the one-mass minimum; min–max eigenvalue bracket and λ_j = log(πj/2L) − ψ(¼) + O_L(1/j); chain decomposition, matrix q^{|i−j|}, σ_{i+1} − σ_i = q^i − q^{h−i}, central row, r_1 = 0, h = ⌈L/log p⌉ a.e.; ‖c‖², ‖s‖², ⟨c,s⟩ = 0; β_L; termination of the certified search (ε − 2^{1−r} > 0); effectiveness at integer n (e^n transcendental, so p^m < e^n is decidable); H ≥ Λ ≥ δ₀. Numerically: N(1) = 4, N(2) = 131.
* **D §5, M Thm 3.1.** Verified: both Green kernels, jump −1, zero Neumann derivative; the expansion 2a(R_N − R_f) = K_a term by term (the term r²e^{-a|x−y|} becomes r·v(x)u(y) for x ≤ y, which is what closes the symmetric form); coefficient eigenvalues 1/(1∓r); energy summand (2/a)I − 2aR so K_a enters with a plus sign; image bookkeeping n(x+y) + n(2L−x−y) + remainder ≤ 2[n(2L)+n(L)]/(1−e^{-L}) (numerically the remainder is ≤ 0.63 of that bound); n(t) − 1/(2t) → ¼; Schur test ∫₀^∞ y^{-1/2}/(x+y) dy = πx^{-1/2}; monotone strong limit; both domain equalities; operator core. Essential norm: the split at L/2, HS off-diagonal blocks, the logarithmic-window quotient ∫(1−|v|/log R)k(v)dv → ∫k = π with k(v) = 1/(2cosh(v/2)), dilation invariance of 1/(x+y), weak nullity; hence π/2 and ‖K_L − K^{(J)}‖ ≥ π/2.
* **D §6, M (3.3)–(3.4), 208–220.** Verified: ⟨u_a,e_j⟩, ⟨v_a,e_j⟩ = (−1)^j⟨u_a,e_j⟩, cancellation of 1−r² in (6.1), parity vanishing, the factor 2ν_iν_j and numerator 1−(−1)^j e^{-a_kL} in (6.2); compressed tail (6.3)–(6.4) with Σ_{k≥J}a_k⁻² ≤ a_J⁻² + 1/(2a_J) and Σν_j² = (2h−1)/L; full column tail (6.5) with ‖u_a‖ ≤ (2a)^{-1/2}, ‖K_ae_j‖ ≤ √2ν_j a^{-3/2}, Σ_{k≥J}a_k^{-3/2} ≤ a_J^{-3/2} + a_J^{-1/2}; shift entries (6.6) with phases +ω_jd and −ω_jd and the λ = 0 branch; J_j(σ), c_j, s_j with e^{∓L/4}; (6.7)–(6.8); reflection identities J V_d J = V_d\*, Jc = c, Js = −s, Je_j = (−1)^j e_j; β_L^{even}.
* **D §7, M Thm 4.1.** Verified: PX_L ⊂ Dom W_L so A, B are bounded; Dom H = Q Dom b(H_N) and Hh = QW_L h there; D_L = PX_L ⊕ QD_L because Q commutes with b(H_N)^{1/2}; cross term 2Re⟨h,Bp⟩; the square (7.1) with H^{1/2}H⁻¹ = H^{-1/2}; converse by h = −H⁻¹Bp; smooth negative input via the core; RH ⇒ core positivity ⇒ form-norm extension; converse by translation invariance (gamma multiplier, correlations, 2cosh((x−y)/2)) and zero extension; parity blocks of dimensions ⌈N/2⌉, ⌊N/2⌋.
* **D §8.** Verified: T ≥ I, G ≥ I by minimization, H⁻¹ − V = αVH⁻¹ ≥ 0 (functions of the same H), D ≥ αI, G − D = S_L, congruence criterion; Cp ⊥ A h via the T-form pairing, C\*C = G, contraction ⇔ D ⪯ G; the 2×2 control (H = 1, V = ½, G = 1, D = 3/2, S = −½, W + I > 0 with det 2).
* **D §9, M Thm 5.1.** Verified: residual expansion (9.1) with factors in order; sup-formula proof of H⁻¹ ≤ Λ⁻¹ with the form-domain inclusion; Galerkin identities Y_K\*HY_K = B\*Y_K = Y_K\*B, E_K R_K = 0; enclosures (9.2); ‖Y_K‖ ≤ δ₀⁻¹‖B‖, R_K = (I−P_K)(B − EY_K), gap ≤ ‖B‖²(1+‖E‖/δ₀)²/d_K, norm error ≤ gap for ordered Hermitian matrices, d_K = log K + O_L(1); the reversed-order counterexample (2^{-ℓ-2}). Numerically nested, monotone and convergent at L = 1. One sentence missing in the R_K → 0 argument (3.5).
* **D §10.** Verified: (10.1) from (9.1); V₀\*W_LV₀ ⪰ C_J by positivity of K_L − K^{(J)}; ‖Λ^{-1/2}(R−R̃)‖ ≤ η_{K,J}‖V₀‖/√δ₀ because V₀ maps into P_KX_L and ‖Λ^{-1/2}‖ ≤ δ₀^{-1/2}; ‖V₀‖² = 1 + ‖Y‖²; T_M of (10.3) ⪰ R̃\*Λ⁻¹R̃ by Parseval and monotone d_j; the perturbation inequality with cross term 2‖X‖ε; (10.4); availability argument. Practicality caveat in 3.3(2).
* **D §11, M Cor 5.2.** Verified both directions and the quantifier order; the ε-slack remark.
* **D §12, M (6.1).** Verified: prime Stieltjes form; 4∫cosh(r/2)h_f minus density 2∫e^{r/2}h_f leaves 2∫e^{-r/2}h_f = form of e^{-|x−y|/2}; the a₀ = ½ summand is 4I minus that kernel (2a₀R_{f,a₀} has kernel e^{-|x−y|/2}); hence (4 + w₀) and −2∫e^{-r/2}h_f dE; extension to D_L (h_f continuous, E of finite variation); integration by parts with vanishing boundary terms; Σ_{k≥1}2/a_k³ = 0.16597 ≤ 26/125; w₀ < −5 via γ > 29/56, e^{11/10} > 3 (six terms give 3.00126), log 2 > 2/3, log π > 1; ‖sin(πx/2)‖ = 1, ‖F′‖² = π²/4; −2979/6125 exact.
* **D §13, M 376–378.** Verified: only 2¹ active, h = 2, r₂ = q; β₁ < 41611/7000 exactly from the six rational bounds (each bound true; actual β₁ = 5.90450); the 64-term sum 6.0145140… > 3007/500; margin 99/14000; N = 4 admissible and in fact N_min(1) = 4 since b₃ = 5.7772 < 5.9670.
* **References and novelty framing.** All entries verified (Section 2). The comparison with CCM Prop. 3.4 is accurate: their proposition is the core statement plus "the lower bound of QW_λ is the limit of the smallest eigenvalue of the restriction to E_N", i.e. finite restrictions from above, whereas here the positive infinite sector is eliminated exactly and enclosed from both sides. I did not perform an originality search beyond this.

## 5. Presentation and metadata for an arXiv version

* `manuscript.tex` line 5 `\author{Draft for author review}` and `preamble.tex` line 10 `\fancyhead[R]{Human review draft}` are placeholders; the running head prints on every page of both PDFs.
* `derivations.tex` lines 3–4 (title "Detailed derivations for human review", author "Review record not yet completed") and the empty signature table of D §14 (lines 919–950) are internal; for an ancillary file, retitle ("Detailed derivations: companion to …") and either fill or drop the table.
* `references.tex` lines 17–20: the Investigation entry has no author; supply the author and, per `BUILD.md`, the version-specific DOI once minted. The manuscript cites commit `efb908a`, which is correct today.
* Disclosure (M 387–394, D "Preparation note"): the commit history shows ChatGPT as well as Codex, and this file adds a Claude review; arXiv's policy asks for an accurate account, so name the tools actually used and the human author's responsibility.
* M 42–50 and D §1 are fine as stated. Consider moving the sentence "No priority is claimed…" out of the abstract and into §1, where it already appears in substance.
* `README.md` and `EVALUATION.md` say "7 pages / 17 pages" — still true.

## 6. Comparison with the Codex review of 13 September

Items 1.1 (certified cutoff), 1.2 (gamma bridge), 1.3 (projected source and defect output), 3.1 (short enclosure proof), 3.2 (parity of the full response), 3.3 (compressed tail), 3.4 (variational identity) and 3.5 (central row) are all present in the current text and correct; I re-derived each rather than relying on `response_20260913.md`. The Codex review's assessment that the boundary identity and the treatment of the noncompact remainder are the strongest parts is one I share; the additional structure I would surface is the elementary image formula for K_L (3.3(2)), which makes that remainder fully explicit.

## 7. Limits of this review

I did not review the physical Investigation manuscript, did not carry out an originality search beyond the cited comparisons, and did not produce an interval-arithmetic certificate of anything. The floating-point and 50-digit spectra in 3.3 are diagnostics: compression eigenvalues bound the true ones from above only, and the double-precision values below 10⁻¹⁴ are noise (the mpmath values are not). The statement about what is and is not known unconditionally for support length 1 (3.3(3)) is a literature question I flag rather than settle. Nothing here proves Conjecture 1.1 for any n.

## 8. Files

* `reviews/review_claude_20260914.md` — this document.
* `reviews/check_claude_20260914/` — `chk1_explicit_formula.py` (rows 1A–1B), `chk2_boundary_identity.py` and `chk2b_boundary_identity.py` (rows 2a–2e), `chk3_operator_and_schur.py` (rows 3i–3v, cosine-basis assembly of W_L), `chk4_highprec_spectrum.py` (row 4), `chk5_rational_and_asymptotics.py` (row 5), `chk6_nearnull_mechanism.py` (row 6), `zeros_300.json` (cache of the first 300 ordinates, 20 digits), the `.out` transcripts and `.json` results, and `README.md` with run instructions. Python 3 with numpy, scipy, mpmath, sympy; total run time about 20 minutes, dominated by the zero-sum and high-precision checks. All files are well under 1 MB; nothing needed the `LARGE_FILES` archive.
