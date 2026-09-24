# The first-prime join is joined-window positivity, and the prime weight is rigid

24 September 2026. Prepared for Edward Baker with substantial LLM assistance.

**Model:** Claude (Anthropic). The session is configured as `claude-fable-5-1`; the
runtime environment reports the serving model as Claude Opus 5.5 (`claude-opus-5-5`).
The serving model may differ from either identifier. Reasoning effort: not exposed.
**Baseline:** commit `1bd1adf` (the arithmetic-storage opening package and first session).
**Status:** second arithmetic-storage session. It contains:

- elementary operator lemmas, with proofs;
- internal computer-assisted inequalities, produced with the **unchanged** weil-depth Arb builder;
- two structural propositions, proved at research-note level: one unconditional, one stated under RH;
- floating diagnostics from an independently written Galerkin model.

A same-assistant referee pass (a separate subagent, which also replayed the horizon-3/4
certificates) checked the lemmas and propositions; its corrections are incorporated.
Specialist review is outstanding. Nothing here is committed. The companion
[review](../reviews/review_claude_first_prime_session_20260924.md) audits the first session;
this note records the new results.

## 0. Summary

1. **The append hypothesis is joined-window positivity (Lemma A).** For coercive local
   forms, the central relative coupling satisfies κ₀ ≤ κ exactly when
   Q_{0,R} ⪰ (1 − κ)(Q_{0,L} ⊕ Q_{0,h}), R = L + h. In particular κ₀ ≤ 1 is equivalent to
   Q_{0,R} ⪰ 0. The first-prime task "κ₀ ≤ 0.999" is therefore a relative central inequality
   on (0, 3/4). When the joined form is positive, κ₀ is the cosine of the angle between the
   two segments in its geometry.
   Joined-window positivity also gives contraction of the joined transfer directly (Lemma C,
   a qualitative form of weil-depth's Proposition "central coercivity implies contraction").
   The energy-transfer lemma adds a quantitative Schur-complement margin, which plays no role
   at the next join.
2. **The first-prime append is closed (internal certificate).** The weil-depth pipeline at
   horizon 3/4 certifies Q_{0,3/4} ⪰ (123/250000)·I. Both of its implementations pass, with
   identical pivots, and the certified upper bound is 4.92324·10⁻⁴. With a norm bound on the
   mixed block, Lemma B gives κ₀ ≤ 0.99980037. The first session's certified constants then
   give a normalized cumulative coupling ≤ 0.99981859 < 1 at ω = 1/1000. Directly,
   ‖V_{ω,3/4}‖ ≤ exp(−ω/5000) for 0 < ω ≤ 1/50, with no append.
3. **No uniform margin for joins of fixed length (Proposition 1, unconditional).** For each
   fixed new length h, sup_L κ₀(L, h) ≥ 1. If RH fails, κ₀ ≥ 1 at a finite join. Under RH,
   κ₀(L, h) ↑ 1, because the Weil form is then the covariance of a deterministic process.
   Chains whose join lengths shrink are *not* excluded. A fixed relative margin is compatible
   with λ_min → 0 if h_k decreases roughly like e^{−L_k}: that is the infinitesimal-append,
   or canonical-system, regime.
4. **The first prime's weight is rigid.** Scale the prime-2 term by s, with s = 1 the
   arithmetic value. Positivity on (0, log 3) certifiably fails for s ≥ 1 + 3.16·10⁻⁶ and
   for s ≤ 1 − 8.18·10⁻⁵, and certifiably holds for |s − 1| ≤ 1.1·10⁻⁷. Table 2 gives the
   interval from 3/4 to log 3. Every translation-invariant perturbation with a bounded,
   continuous, sign-changing symbol destroys positivity at some finite window
   (Proposition 2, under RH; the referee pass sketches an unconditional version). The
   reason: under RH the spectral measure is atomic, so there is no absolutely continuous
   cushion.
5. **The archimedean threshold.** The prime-free form is certified positive at R = 0.74 and
   certified not positive at R = 0.745. The Galerkin estimate is R_A ≈ 0.743203, about 7%
   beyond log 2. Past R_A the prime is indispensable. At R = 0.85 the admissible weight
   interval is [−6.7%, +1.07%] around the arithmetic value.
6. **Consequence.** An append chain with joins of bounded-below length cannot carry a fixed
   margin, and any single append is joined-window positivity. The append method therefore
   supplies no continuation mechanism of its own. A mechanism must be exact in the
   arithmetic (at least against translation-invariant errors) and must control vanishing or
   shrinking margins. Section 5 re-scopes the program.

## 1. The append hypothesis is joined-window positivity

Notation follows the [first-prime analysis](FIRST_PRIME_CONTINUATION_ANALYSIS_20260924.md).
On the joined window (0, R), R = L + h, with the old input reflected,

  Q_{0,R} = [[A, −B*], [−B, C]],  A = Q_{0,L},  C = Q_{0,h},  B = H_0.

Here A and C are closed forms on the log-energy domains with compact resolvent, bounded
below by positive constants, and B is bounded.

Splitting a log-energy function at the join keeps both pieces in the form domains. The log
energy is equivalent to ‖f‖² + ∫₀¹ ‖f − S_u f‖² du/u. Cutting at a point adds at most a
multiple of ∫_{|y|<1} |f(y)|² log(1/|y|) dy near the cut, and this is controlled by the
logarithmic Hardy (Beckner) inequality. So the block form is Q_{0,R} on its whole form
domain.

**Lemma A.** For κ ≥ 0 the following are equivalent:
(i) |⟨v, Bf⟩| ≤ κ A[f]^{1/2} C[v]^{1/2} for all f, v in the form domains, that is
‖C^{−1/2} B A^{−1/2}‖ ≤ κ;
(ii) κA[f] + κC[v] − 2 Re⟨v, Bf⟩ ≥ 0 for all f, v.

*Proof.* (i) implies (ii) by AM–GM. Conversely, apply (ii) to (tf, e^{iθ}v/t), with θ
chosen so that ⟨e^{iθ}v, Bf⟩ = |⟨v, Bf⟩|. This gives κt²A[f] + κC[v]/t² ≥ 2|⟨v, Bf⟩|;
minimize over t > 0. □

**Corollaries.** (a) κ₀ ≤ 1 if and only if Q_{0,R} ⪰ 0.

(b) The pencil Q_{0,R} − μ(A ⊕ C) has spectrum {1 ± σ_i(K)} ∪ {1}, where
K = C^{−1/2}BA^{−1/2} is compact. Hence 1 − κ₀ = inf_x Q_{0,R}[x]/(A ⊕ C)[x], and κ₀ ≤ κ is
equivalent to Q_{0,R} ⪰ (1 − κ)(A ⊕ C). Consequently
λ_min(Q_{0,R}) ≥ (1 − κ₀) min(λ_min A, λ_min C).

(c) If Q_{0,R} ⪰ 0, then κ₀ is the cosine of the minimal angle between the old-segment and
new-segment subspaces in the Q_{0,R} inner product. Under RH, where Q_{0,R} is a covariance,
it is the first canonical correlation between the segments. κ₀(L, h) is nondecreasing in
both L and h.

The floating value κ₀ ≈ 0.996481 therefore says that the joined window's relative bottom is
about 0.00352.

**Lemma C.** Let 0 < ω ≤ 1/2, the range in which V is defined here. If Q_{s,R} ⪰ 0 for
0 ≤ s ≤ ω, then ‖V_{ω,R}‖ ≤ 1. This follows from the defect identity
⟨f, D_{ω,R} f⟩ = 2∫₀^ω Q_{s,R}[V_{s,R} f] ds, read as lim_{ε↓0} ∫_ε^ω on the smooth domain
as in the parent note. The quantitative version is [weil-depth, Proposition "Central
coercivity implies contraction"]: if Q_{0,R} ⪰ mI, then ‖V_{ω,R}‖ ≤ exp(−mω + C_R ω³/3).

By Corollary (b), the energy-transfer lemma's hypothesis κ_s < 1 for all s ≤ ω is the
statement Q_{s,R} ⪰ (1 − κ_s)(Q_{s,L} ⊕ Q_{s,h}) ⪰ 0. So contraction of the joined transfer
already follows from Lemma C, without the lemma. What the lemma adds is the normalized bound
‖F^{−1/2}YE^{−1/2}‖ ≤ κ, equivalently E − Y*F^{−1}Y ⪰ (1 − κ²)E. By Lemma A, the next
join's hypothesis is again joined-window positivity, so that margin does not enter it.

**Framing to annotate.** Two earlier documents describe an enlarged-window central
certificate as something other than the coupling task:

- the [operator-coupling certificate](../../../critical-path/notes/CUMULATIVE_OPERATOR_COUPLING_CERTIFICATE_20260920.md): "no enlarged-window central certificate is substituted for the coupling task";
- the [cross-program assessment](../../notes/CROSS_PROGRAM_PRIORITIES_AFTER_WZW_AND_N4SYM_REVIEWS_20260924.md): such a certificate "is a useful control, not a solution".

Both statements are defensible if "central certificate" means an *absolute* floor and
"solution" means a continuation mechanism. They should be annotated all the same: at zero
shift the coupling hypothesis *is* a joined-window central inequality, in relative form,
and the positive-shift part is O(ω²).

The relative form is quantitatively stronger than an absolute floor. At the critical-path
benchmark (R = 0.55, λ_min ≈ 0.0171, ‖H_0‖ ≤ 1.7532), Lemma B below gives only κ₀ ≤ 0.9903,
against the certified 0.951. The critical-path certificate therefore proved more than
coercivity. It is still a statement about the joined window only.

## 2. Closure of the first-prime append at (11/20, 1/5, 1/1000)

**Lemma B.** If Q_{0,R} ⪰ mI and ‖B‖ ≤ β, then κ₀ ≤ β/(β + m).

*Proof.* For f, v in the domains and t > 0, write the coercivity inequality at (tf, v/t):

  t²A[f] + C[v]/t² − 2 Re⟨v,Bf⟩ ≥ m(t²‖f‖² + ‖v‖²/t²) ≥ 2m‖f‖‖v‖ ≥ (2m/β)|⟨v,Bf⟩|.

Align the phase as before and minimize over t. The bound is optimal given only m and β. □

**Inputs.**

- *Mixed-block norm.* ‖H_0‖ ≤ π/2 + √((e^{11/20} − 1)(e^{1/5} − 1)) + (log 2)/√2 = 2.463845… < 2.464. The three terms come from the gamma corner (dominated by the Carleman kernel 1/(2(t+r))), the rank-one growing pole, and the prime partial isometry. The bound is enclosed in Arb.
- *Joined-window floor.* The weil-depth builder and Schur test, unchanged, are run at horizon 3/4 with N = 128, M = 180 and 1536 bits. The floor 123/250000 passes in both reflection sectors, with minimum pivots 0.0069543628… (even) and 0.4646600640… (odd). Weil-depth's separately written `independent_arb.py` passes the same floor with identical pivots. `enclose_certificate.py` gives the sector floors 4.92·10⁻⁴ (even) and 3.13·10⁻² (odd), and a certified upper bound 4.92324·10⁻⁴ for the bottom.

**Conclusions** (exact rationals in the record):

- κ₀ ≤ 2.464/(2.464 + 123/250000) = 0.99980036…;
- the normalized cumulative coupling is ‖F^{−1/2}YE^{−1/2}‖ ≤ (κ₀ + Δ/0.0812)/(1 − ℓ) = 0.99981858… < 1. This uses the first session's certified record values: the mixed shift perturbation Δ < 6.7285·10⁻⁷, relative local losses ℓ < 9.9386·10⁻⁶ from the floors 3/200 and 11/25, and √(0.015·0.44) > 0.0812;
- directly, C_{3/4} = 0.49468… < 1 and (123/250000) − (1/50)²/3 − 1/5000 = 119/750000 > 0, so ‖V_{ω,3/4}‖ ≤ exp(−ω/5000) for 0 < ω ≤ 1/50.

**Remarks.** (i) The handoff's intermediate target κ₀ ≤ 0.999 is not reached by this
absolute route. It would need λ_min(Q_{0,3/4}) ≥ 0.001·‖H_0‖/0.999, which is at least
1.57·10⁻³, because ‖H_0‖ ≥ π/2 from the corner. The bottom is about 4.923·10⁻⁴. The target
served only to make (4.4) below one, and that is now achieved.

(ii) Before this session, weil-depth's floor at log 3, 5.52·10⁻⁸, already implied
κ₀ ≤ 1 − 2.2·10⁻⁸ at this split, by compression and Lemma B. That suffices for (4.4) at
ω ≲ 3.5·10⁻⁵.

(iii) The first session's diagnostic recorded the joined-window bottom
(`complete_form_compression_minimum_eigenvalue`, 4.93·10⁻⁴ at 96 cosines) without
connecting it to the existing certificates.

## 3. Joins of fixed length cannot keep a uniform margin

Let R₀ = inf{R : λ_min(Q_{0,R}) ≤ 0}. Then R₀ ≥ log 7 by weil-depth, and R₀ = ∞ exactly
when Weil positivity holds on every window, that is under RH.

**Proposition 1.** Fix 0 < h < R₀. Over the L for which Q_{0,L} is coercive,
sup_L κ₀(L, h) ≥ 1.

*Proof.* Suppose first that R₀ < ∞. For L ∈ (R₀ − h, R₀), both local forms are coercive
and λ_min(Q_{0,L+h}) ≤ 0, since λ_min(Q_{0,R}) is nonincreasing in R. So 1 − κ₀ ≤ 0 by
Corollary (b).

Now suppose R₀ = ∞. Under RH the explicit formula gives Q_{0,R}[f] = Σ_γ m_γ|f̂(γ)|². Here
f̂(t) = ∫ f(x) e^{itx} dx, the sum runs over the distinct ordinates γ with multiplicities
m_γ, and the zero set is symmetric. A floating check at R = 3/4 agrees with the Galerkin
value to a relative 7·10⁻⁹ using ±300 zeros; weil-depth's
`review_claude/check_fourier_side.py` checks the same identity. The Q-completion of the
compactly supported log-energy functions embeds in the weighted ℓ² space of sequences
(f̂(γ)).

Suppose a vector (c_γ) in that space is orthogonal to every f supported in (−∞, 0]. Then the
tempered distribution F = Σ_γ m_γ c̄_γ e^{iγx} vanishes on (−∞, 0). It is tempered because
Σ m_γ(1 + |γ|)^{−2} < ∞. Convolving with φ ∈ C_c^∞(−1, 0) gives a uniformly convergent
almost-periodic series. Its coefficients are m_γ c̄_γ times the Fourier coefficient of φ at
∓γ, depending on convention, and the series vanishes on (−∞, −1). Its Bohr mean square is
zero, so every coefficient vanishes. Choosing φ with nonzero Fourier coefficient at each γ
gives c = 0.

The past is therefore dense: the process is deterministic, as it must be for an atomic
spectral measure. By translation invariance, for a fixed v₀ supported in the new segment,
the Q-distance from v₀ to the span of the old segment (0, L) tends to 0. Hence
κ₀(L, h) ≥ ‖P_old v₀‖/‖v₀‖ → 1; since κ₀ is nondecreasing in L and below one, κ₀ ↑ 1. □

**Scope.** Because κ₀(L, h) is also nondecreasing in h, Proposition 1 excludes a uniform
margin only for chains whose join lengths are bounded below. Chains with shrinking joins
are not excluded. Corollary (b) gives λ_min(Q_{0,L_k}) ≥ (1 − κ)^k λ_min(Q_{0,L_0}) along a
chain with κ₀ ≤ κ at each join and new-segment floors above the old ones. That is compatible
with a profile λ_min(R) ≈ exp(a − b e^R) as long as h_k ≲ |log(1 − κ)| e^{−L_k}/b, which
makes L_k grow like log k. This is the infinitesimal-append regime: a Schur or canonical-system
recursion. Proposition 1 does not rule it out, and Section 5 recommends it.

Proposition 1 is related to, but distinct from, the collapse λ_min(Q_{0,R}) → 0 seen in
weil-depth's seven-horizon profile and in the Landau–Widom discussion it cites (Zhu 2026,
arXiv:2608.24827, not read in this session).

## 4. The first-prime weight is rigid

### 4.1 Setting

For log 2 < R ≤ log 3 only the delay a = log 2 enters, and

  Q_R(s) = Q_R^A + s M_2,  M_2 = −((log 2)/√2)(S_a + S_a*),  s = 1 arithmetic.

The admissible set I(R) = {s : Q_R(s) ⪰ 0} is a closed interval, because Q_R(s) is affine
in s. It contains 1 for R ≤ log 7. Since 2a > R, ‖M_2‖ ≤ (log 2)/√2. So a floor m at s = 1
certifies [1 − m√2/log 2, 1 + m√2/log 2] ⊂ I(R). Outer bounds come from rational Ritz
vectors v of the N = 128 weil-depth head with ⟨v, Q_R(s) v⟩/⟨v, v⟩ + η < 0, where η is the
head's profile remainder. The head of Q_R^A is built by the same builder with its prime list
emptied.

### 4.2 Results

**Table 2.** Admissible prime-2 weight s, with N = 128 and 1536 bits (1792 bits and M = 220
at log 3). "Head interval" is floating. "Outer" lists trial weights certified not positive.
"Inner" is the certified half-width around s = 1, rounded down. At every sampled R the
upper edge is set by the even sector and the lower edge by the odd sector.

| R | λ_min at s = 1 (head) | certified floor | head interval for s | outer: not positive at | inner half-width |
|---|---:|---:|---|---|---:|
| 3/4 | 4.9232e−4 | 4.82e−4 * | [0.185188, 1.350900] | 1.358; 0.168 | 9.8e−4 |
| 4/5 | 1.8131e−4 | 1.77e−4 | [0.781447, 1.056266] | 1.0574; 0.777 | 3.6e−4 |
| 17/20 | 5.8527e−5 | 5.73e−5 | [0.933409, 1.010689] | 1.011; 0.932 | 1.1e−4 |
| 9/10 | 1.6158e−5 | 1.58e−5 | [0.980103, 1.002044] | 1.00209; 0.9797 | 3.2e−5 |
| 19/20 | 3.8622e−6 | 3.78e−6 | [0.994684, 1.000375] | 1.000383; 0.99457 | 7.7e−6 |
| 1 | 9.3385e−7 | 9.15e−7 | [0.998792, 1.0000743] | 1.0000758; 0.99876 | 1.8e−6 |
| 21/20 | 2.7153e−7 | 2.66e−7 | [0.9997235, 1.0000181] | 1.0000185; 0.999717 | 5.4e−7 |
| log 3 | 5.5369e−8 | 5.42e−8 | [0.99991986, 1.00000309] | 1.00000316; 0.9999182 | 1.1e−7 |

\* The automatic floor is 0.98 times the head minimum. The closure in §2 uses the enclosure
floor 4.92e−4, which gives an inner half-width of 1.0e−3.

In weight units c = s·(log 2)/√2, with c* = 0.49012907, positivity on (0, log 3) confines c
to the open interval (0.4900889, 0.4901307), rounded outward. The independent Galerkin
model at N = 64 reproduces every head interval; the margins 1 − s₋ and s₊ − 1 agree to
about three significant digits.

**The archimedean threshold.** With every delayed term removed, the prime-free form passes
the full weil-depth Schur test at R = 37/50, with floor 51/50000. At R = 149/200 it has a
certified negative direction in the odd sector, with Rayleigh bound ≤ −2.546·10⁻³. So
0.74 < R_A ≤ 0.745. The Galerkin estimate is R_A ≈ 0.743203, converging from above, and
R_A/log 2 ≈ 1.072.

The first session's witness at 3/4 lies just past R_A. Between log 2 and R_A the prime is
not needed, and s = 0 remains admissible. Past R_A the admissible interval moves off 0 and
contracts, and it is asymmetric:

- *1% errors.* At R = 0.85 it is [−6.7%, +1.07%] around s = 1. A +1% error in the weight fails near R ≈ 0.852, while a −1% error survives to about R ≈ 0.925.
- *Rate of contraction.* Between R = 0.9 and log 3 the upper margin s₊ − 1 falls by a factor of about 25 per 0.1 in R, somewhat faster than λ_min, which falls by about 17. The ratio (s₊ − 1)/λ_min decreases from about 127 to 56, because the ground state's M₂-expectation grows.

### 4.3 Why: the spectral measure is atomic

**Proposition 2 (under RH).** Let P be a translation-invariant form,
P[f] = ∫ |f̂(t)|² p(t) dt/2π, with p real, bounded and continuous. If Q_{0,R} + P ⪰ 0 on
every window, then p ≥ 0. Conversely, p ≥ 0 suffices.

*Proof.* By translation invariance, positivity on every window makes the Weil distribution
plus P positive-definite on C_c^∞(ℝ). By the Bochner–Schwartz theorem it is tempered, and
its Fourier transform μ + p dt/2π is a positive measure. Under RH, μ = Σ_γ m_γ δ_γ is atomic.
So p ≥ 0 off a countable closed set, and by continuity everywhere. □

**Remark.** The referee pass sketches why RH can be dropped. W + P tempered makes W tempered.
Then the Laplace transform of the causal part of W would be analytic in Re p > 0; it equals
2(ξ′/ξ)(1/2 + p) up to an entire function, and this forces RH. This is not written out here.

For a change δ in the weight of one delay log n, p(t) = −2δ cos(t log n) changes sign. So
every single prime-power weight is pinned exactly by positivity on all windows, with the
other terms fixed. Proposition 2 constrains only translation-invariant errors with bounded
symbol. It says nothing about errors of other shapes, for example boundary-localized ones.

Table 2 shows *where* the pinning of c₂ is detected. The perturbation −(s − 1)(log 2/√2)
(S_a + S_a*) has symbol −(s − 1)√2 log 2·cos(t log 2).

- For s > 1 it is negative near t = 0, in the widest zero-free band |t| < 14.13, where the even ground state lives.
- For s < 1 it is negative near t = π/log 2 ≈ 4.53, the odd sector's frequency.

The same atomicity gives Proposition 1's determinism.

A heuristic, not a claim. For perturbations whose negative part overlaps the ground-state
band, if λ_min(Q_{0,R}) behaves like exp(a − b e^R), a perturbation of size ε is detected by
R ≈ log((a + log 1/ε)/b). That is doubly logarithmic in 1/ε. Weil-depth's seven horizons
suggest b ≈ 11–12; Table 2 gives b ≈ 10 on [3/4, log 3].

## 5. Consequences for the arithmetic-storage program

**Direction A (the append chain) supplies no continuation mechanism of its own.** Each
append hypothesis is joined-window positivity (Lemma A). Joins of bounded-below length
cannot keep a uniform margin (Proposition 1). Weil-depth already certifies joined windows
through log 7 more directly, including the prime-power and mixed-overlap structure the
program note planned to test at log 3, log 4 and log 6. Further finite-append certificates
would reproduce those results in a less efficient decomposition.

The M = 128 obstruction of the first session is an artifact of that decomposition.
Splitting at the join creates endpoint energy that only the full gamma tail cancels against
the Carleman corner. The one version of the append idea that Proposition 1 leaves open is
the infinitesimal one, which is the canonical-system recursion.

**What a mechanism must satisfy.**

- It must be exact in the arithmetic, at least against translation-invariant errors (Proposition 2, Table 2).
- It must control margins that shrink with the window. They vanish for joins of fixed length.
- Storage with an absolutely continuous *positive* spectrum (dissipation) preserves positivity but changes the form. It does not realize the Weil form.

These conditions point to frameworks where the arithmetic is exact and a continuation step
is an identity:

- *Canonical systems / de Branges chains.* This is Suzuki's construction and the repository's [omega-string](../../../../../shifted-zeta/omega-string/README.md) inverse-spectral family. Heuristically, the Schur–Krein recursion is the exact version of an append: an infinitesimal append is a Schur step, and positivity on growing windows becomes local positivity of the Hamiltonian. The precise form of this correspondence for the Weil distribution, with its logarithmic diagonal, has not been checked here.
- *Semilocal Sonin spaces* (Direction B of the [program](ARITHMETIC_STORAGE_PROGRAM_AND_GOALS_20260924.md)). The local factor I − 2^{−1/2}U_a is exact there. The residual Δ₂ must be controlled to the λ_min scale near log 3, since there the relevant margin is about 5·10⁻⁸ absolutely.
- *Transmission.* This is standard de Branges–Lagarias structure, recorded for orientation. K_ω(p) = ξ(1/2 + p − ω)/ξ(1/2 + p + ω) is inner in Re p > 0 unconditionally for ω ≥ 1/2, and under RH for every ω > 0. Then the half-line transfer T_{K_ω} is an isometry, and D_{ω,L} = B*B with B = (I − P_L)T_{K_ω}P_L: the cumulative storage is the energy transmitted past the window. For ω > 1/2 define V_{ω,L} = P_L T_{K_ω} P_L; the small-ω case is the open one.

**Filter.** Every proposed mechanism, physical or operator-theoretic, should reproduce
Table 2 and its later analogues, for example the joint (c₂, c₃, c₄) region on (log 3, log 5].
This is in addition to the program's negative smooth-density control. For example, a
mechanism that gets the first prime's weight right only to within +1% fails positivity by
R ≈ 0.852. One that errs by −1% fails by about 0.925.

**Suggested next session (the author's choice):**

- (B1) re-derive the first-prime semilocal Sonin identity from Connes–Consani (arXiv:2006.13771) and the semilocal paper, since the 14 September derivation is outside the repository, and evaluate its residual on the weak directions of Table 2;
- (C1) compare the canonical-system Hamiltonian of the omega-string family at small ω with the prime impulses at log 2 and log 3. Ask whether an infinitesimal-append chain with a fixed relative margin (the regime left open in §3) exists, and whether Hamiltonian positivity has a local arithmetic explanation there;
- (D) close the arithmetic-storage folder and fold its surviving questions into those two programs.

## 6. Evidence ledger and reproduction

| Result | Kind | Source |
|---|---|---|
| Lemmas A, B; Corollaries (a)–(c); Proposition 1 (unconditional dichotomy) | Proof in this note (referee-checked, same assistant) | §1–§3 |
| Proposition 2; determinism step of Proposition 1 | Proof under RH (Bochner–Schwartz; almost-periodic uniqueness) | §3, §4.3 |
| Q_{0,3/4} ⪰ (123/250000)I; κ₀ ≤ 0.99980037; normalized coupling ≤ 0.99981859; ‖V_{ω,3/4}‖ ≤ e^{−ω/5000} | Internal computer-assisted (weil-depth builder and Schur test; exact rationals) | `certify_first_prime_join_from_central_floor.py`, record `first-prime-join-closure-20260924.json` |
| Same floor by the independent weil-depth implementation | Internal computer-assisted | `independent_arb.py --horizon 0.75` (replay command in the numerics guide) |
| Table 2: outer and inner bounds | Internal computer-assisted | `certify_prime_weight_window.py`, records `prime-weight-window-*-20260924.json` |
| 0.74 < R_A ≤ 0.745 | Internal computer-assisted | `certify_archimedean_threshold.py`, record `archimedean-threshold-20260924.json` |
| Head intervals, Galerkin cross-checks, R_A ≈ 0.743203, explicit-formula check | Floating diagnostics | `crosscheck_first_prime_galerkin.py`, record `first-prime-galerkin-crosscheck-20260924.json` |

All Arb runs used Python 3.11.15, python-flint 0.9.0 and FLINT 3.6.0 in the session's cloud
container. The weil-depth builder was imported, not modified; its source hash is recorded.
No ball archive was saved. Each rebuilds in 20–90 s, and the records carry the matrices'
content hashes, in line with [LARGE_FILES.md](../../../../../../LARGE_FILES.md). Commands are in
the [numerics guide](../numerics/README.md). Same-assistant replays, the referee pass and the
cross-checks do not replace specialist review. The three items a specialist should examine
are the weil-depth method, Lemma C's evolution-domain argument, and the propositions above.
