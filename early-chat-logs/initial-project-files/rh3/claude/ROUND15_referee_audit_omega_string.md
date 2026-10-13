# ROUND 15 — Referee audit of the ω-string note: Theorems A–E proved or pinned, two errata

**2026-08-28.** Response to external referee-style feedback (ChatGPT) on `NOTE_omega_string.md`
(feedback file `omega_string_referee_feedback.md`, uploaded this round). Overall verdict on the
feedback: high quality, adopted nearly wholesale. Its §8 instruction — *exact statement,
assumptions, proof, literature dependency, attempted counterexample, in priority order* — is
executed below for all six items. Two of its complaints are confirmed here by recomputation
(one direction typo, one 6th-digit numerical error, both now errata); one point (4.5)
under-credits the already-proved order-parameter theorem and is answered with a new theorem (E′)
that is *stronger* than the referee's suggested fallback. Scripts:
`~/work/round15/v1_identities.py`, `v2_thmE_kasahara.py` (session workspace).
**Same-day follow-up executed §8's steps 1–3: see the updated §8 at the end — the companion
paper is now drafted as `PAPER_omega_string.tex`.**

## 0. Triage of the referee's points

| pt | verdict | disposition |
|---|---|---|
| 4.1 "inverse problem solved" too strong | correct | note §2 reworded: discrete inverse problem solved to high precision; continuum convergence is separate and quadrature-dominated |
| 4.2 width = ω only under RH | correct | note §1 already conditions it; §3 and figure captions now do too (spec in §6) |
| 4.3 "same Weyl asymptotics as Hilbert–Pólya" | correct | replaced by "integrated spectral measure has the same leading Riemann–von Mangoldt growth as the zero-counting function" |
| 4.4 "localization transition" | correct | replaced by "a.c.-to-pure-point spectral transition"; "localization" demoted to explicit physics gloss |
| 4.5 "below ω_c the measure loses positivity" | correct that pointwise negativity of ρ_ω is unproven — a violating zero at height τ contributes −1/(β−σ) at u = τ against a background ≈ (1/2π)log(τ/2π), not automatically dominant | but the referee's suggested fallback is now a **theorem** (E′ below: non-real poles ⇒ Herglotz fails ⇒ no positive string), and the paper's thm:transition already gives the stronger Ψ_ω statement (two-sided exponential oscillation below ω_c) |
| 4.6 "all rigorous" | correct | note §3 re-tiered: theorem / standard-once-cited / numerics / interpretation (§7 below) |
| 4.7 UV direction inconsistency | **confirmed — erratum 1.** UV is y→∞ as the convention says; the analytic dual-curve ratio M/[4x/log²x] is 4607 at y = 10⁻⁶ and 1.39 / 1.093 / 1.008 at y = 10⁶ / 10⁹ / 10¹². The note's "ratio → 1.08 at y = 10⁻⁶" was wrong on both number and direction; corrected |
| — (found during audit) | **erratum 2** | ρ_∞(½) = 1874.7243, not 1874.7255. Closed form: (ξ′/ξ)(1) = γ/2 + 1 − ½log 4π = 0.02309570896612, slope⁻² = 1874.72427734. Feeds the control-corrected 0.9995–0.9996 comparisons at the 10⁻⁶ level only — verdicts unchanged |
| Thm E proposal (§3, §6.E) | adopted | the one genuinely new suggestion; proved in parts (i)–(ii) below, (iii) pinned |
| titles / framing (§9) | adopted | "The Shifted Zeta String: An Unconditional Inverse-Spectral Family and Its RH Endpoint" is now the paper's title |

---

## 1. Theorem A — the spectral measure identified (was: note §1, caveat 1; referee priority 1)

**Theorem A.** Fix ω ≥ ½, σ = ½+ω. For z ∈ ℂ∖[0,∞) take the branch √z with Im √z > 0 and set
w := −i√z (so Re w > 0, z = −w²). Define

> q_ω(z) := (ξ′/ξ)(σ+w)/w = i (ξ′/ξ)(σ−i√z)/√z.

Then: (i) q_ω is analytic on ℂ∖[0,∞), real and positive on (−∞,0);
(ii) q_ω belongs to the Stieltjes class N_S;
(iii) q_ω(z) = ∫₀^∞ dσ_ω(λ)/(λ−z) with **no** additive constant or linear term, and dσ_ω is
purely absolutely continuous:

> dσ_ω(λ) = ρ_ω(√λ)/√λ · dλ,  ρ_ω(u) = (1/π) Re(ξ′/ξ)(σ+iu)
>        = (1/π) Σ_ρ (σ−β)/((σ−β)²+(u−γ)²)  (all zeros ρ = β+iγ, absolutely convergent);

(iv) by Kreĭn's inverse theorem there is a unique string S[m_ω, L_ω] with principal Weyl
function q_ω; q_ω(−y) ↑ ∞ as y ↓ 0, so the string is non-regular at its right end (with
Theorem C, in fact m_ω(∞) = ∞, L_ω = ∞).

*Proof.*

**Lemma A.1 (paired Hadamard, no constant).** ξ′/ξ(s) = Σ_pairs [1/(s−ρ) + 1/(s−ρ̄)], the sum
over conjugate pairs, locally uniformly absolutely convergent off the zeros. Indeed
ξ′/ξ(s) = B + Σ_ρ[1/(s−ρ) + 1/ρ] with B = −Σ_ρ Re(1/ρ) (Davenport, *Multiplicative Number
Theory*, §12); grouping conjugates, Σ_pairs(1/ρ+1/ρ̄) = Σ_ρ Re(1/ρ) cancels B exactly. Each
paired term is 2(s−β)/((s−β)²+γ²) = O(|s|/γ²), and Σγ⁻² < ∞.

**Lemma A.2 (residue identity).** For a > 0, γ ∈ ℝ, z ∈ ℂ∖[0,∞), with w = −i√z as above:

> (1/w)[1/(a+w−iγ) + 1/(a+w+iγ)]
>  = (1/π) ∫_ℝ [a/(a²+(u−γ)²) + a/(a²+(u+γ)²)] / (u²−z) du.

*Proof of A.2.* Close the contour in the upper half u-plane. With a > 0 the Lorentzian poles
u = ±γ+ia lie in the **upper** half-plane, contributing 1/((±γ+ia)²−z); the pole u = √z (upper
root) contributes (i/√z)·a/(a²+(√z∓γ)²). Writing v = √z, both sides are rational in (a,γ,v);
clearing denominators reduces the identity to
(a²+v²+γ²)² − 4v²γ² = (γ²−a²−v²)² + 4a²γ² (both = (a²+v²)²+2γ²(a²−v²)+γ⁴) with matching
numerators −2(a²+v²−γ²). Checked by hand and numerically at four (a,γ,z) including near-cut
z = 100+i: agreement 10⁻³³–10⁻⁴⁴. ∎

**Positivity and convergence.** For ω ≥ ½, σ ≥ 1 and every zero has β < 1 ≤ σ (no zeros on
Re s = 1, Hadamard–de la Vallée Poussin), so a = σ−β > 0 strictly for every zero: each
Lorentzian is nonnegative and A.2 applies. Sum–integral interchange: |u²−z| ≥ c_z(1+u²) for
fixed z off the cut, and (Poisson semigroup)
∫_ℝ (1/π)·a/(a²+(u−γ)²) · du/(1+u²) = (1+a)/((1+a)²+γ²) = O(σ/γ²), summable.

Summing A.2 over pairs via A.1 gives q_ω(z) = ∫_ℝ ρ_ω(u)/(u²−z) du = ∫₀^∞ dσ_ω(λ)/(λ−z)
(substitute λ = u², use evenness of ρ_ω). Since ρ_ω ≥ 0: Im q_ω(z) = Im z · ∫ρ_ω/|u²−z|² > 0
on ℂ⁺, and q_ω(−y) = (ξ′/ξ)(σ+√y)/√y > 0 — hence (i), (ii). The constant in the Herglotz
representation is lim_{y→∞} q_ω(−y) = 0 (computed below, Theorem D), and there is no linear
term; the measure satisfies ∫dσ_ω/(1+λ) < ∞ (density ~ ρ_ω(0)/√λ at 0, ~ log λ · λ^{−3/2} at ∞).
Absolute continuity: q_ω extends continuously from ℂ⁺ to (0,∞) (ξ′/ξ is analytic on the closed
half-plane Re s ≥ σ > Θ; the ζ-pole at s = 1 is cancelled in ξ, ξ(1) = ½ ≠ 0), with
Im q_ω(λ+i0) = π ρ_ω(√λ)/√λ; Stieltjes–Perron inversion on compacts of (0,∞) gives the
a.c. identification. No atom at 0: q_ω(z) = O(|z|^{−1/2}) near 0, so lim ε·|q_ω(iε)| = 0. ∎

**Conditional extension.** For ω_c < ω < ½ (ω_c = Θ−½), every step holds verbatim: all
β ≤ Θ < σ, so a = σ−β > 0 still, with variable widths. Unconditionality holds exactly on
ω ≥ ½; on (ω_c, ½) the theorem is conditional on the zero-free half-plane, as it must be (E′).

**Failure mode — where positivity enters.** If a zero has β > σ, its Lorentzian pole
u = γ + i(σ−β) crosses into the **lower** half-plane and Lemma A.2 acquires a residue
correction: q_ω is then ∫ρ_ω/(u²−z)du **plus** explicit non-Herglotz pole terms. The boundary
formula for ρ_ω still holds, but q_ω is no longer the Stieltjes transform of its boundary
density. This localizes the failure exactly and is the mechanism behind Theorem E′.

---

## 2. Theorem B — screw representation and the margin identity (referee priorities 2–3)

**Theorem B.** For ω ≥ ½ (or ω > ω_c conditionally),

> Ψ_ω(t) = ∫_ℝ (1−cos ut)/u² · ρ_ω(u) du  (t ≥ 0),

absolutely convergent, with exactly the normalization shown (no stray π's or 2's).
**Corollary (margin = π × zero-energy DOS).** πρ_ω(0) = (ξ′/ξ)(½+ω): the linear margin slope
of the Ψ_ω paper equals π times the spectral density at u = 0 (density on the frequency line u;
in the energy variable λ = u² the density diverges as ρ_ω(0)/√λ — say "zero-energy DOS" only in
the u-normalization).

*Proof.* Both sides are continuous in t and polynomially bounded: (1−cos ut)/u² ≤ min(t²/2, 2/u²)
and ∫dµ_ω min(t², u⁻²) < ∞ since ∫_{|u|>1} ρ_ω(u)u⁻² du < ∞. So both Laplace transforms converge
on Im z > 0. The paper's identity gives ∫₀^∞ Ψ_ω(t)e^{izt}dt = −z⁻²(ξ′/ξ)(σ−iz). For the right
side, Fubini (justified by the min-bound against e^{−t Im z}) and the block

> ∫₀^∞ (1−cos ut) e^{izt} dt = −i u² / (z(z²−u²))  (Im z > 0; verified numerically to 10⁻²³)

give ∫₀^∞ RHS(t)e^{izt}dt = (i/z)∫_ℝ ρ_ω(u)/(u²−z²)du = (i/z)·q_ω(z²). For Im z > 0 the
principal upper root of z² is z itself, so q_ω(z²) = (ξ′/ξ)(σ−iz)/(−iz), and the transform is
−z⁻²(ξ′/ξ)(σ−iz) — identical. Uniqueness of Laplace transforms of continuous
polynomially-bounded functions gives the identity for all t ≥ 0. The corollary is then
definitional: ρ_ω(0) = (1/π)(ξ′/ξ)(σ), ξ′/ξ being real at real σ — the *content* is Theorem A's
statement that this same ρ_ω is the density of the string's spectral measure. ∎

Independent numerical anchor: note §1 check 5 (against Suzuki's arithmetic Ψ_{1/2}, reldiff
1.3·10⁻⁶ at t = 2). Normalization is thus fixed twice over: by the verified transform block and
by the arithmetic cross-check.

---

## 3. Theorem C — homogeneous IR bulk (referee priority 4)

**Theorem C.** For ω ≥ ½ (or ω > ω_c): the string mass function satisfies

> m_ω(x)/x → ρ_∞(ω) = [(ξ′/ξ)(½+ω)]⁻²  as x → ∞.

"ρ_∞ in string coordinates" means exactly this Cesàro/ratio limit of the Kreĭn mass function at
the non-regular end; at ω = ½: ρ_∞ = 1874.72427734 (erratum 2).

*Proof.* Exact small-y Weyl asymptotics from the closed form:
q_ω(−y)·√y = (ξ′/ξ)(σ+√y) → (ξ′/ξ)(σ) > 0 as y ↓ 0, with error O(√y). So q_ω(−y) is regularly
varying of index −½ at 0 with limit constant c = (ξ′/ξ)(σ). The Kreĭn–Kasahara correspondence
between the string's mass growth at its non-regular end and the Weyl function at 0 converts
q(−y) ~ c/√y (y↓0) into m(x) ~ c⁻²x (x→∞); the constant is exact, calibrated by the
homogeneous string itself (m = ρx has q(−y) = 1/√(ρy) exactly; index-1 mass growth is self-dual,
so no Γ-factor enters). ∎ — citation status: see updated §8.1. Status: **proved modulo the
internal theorem number in Kasahara 1975**.

Failure modes examined: (a) Tauberian converses need monotone m — automatic for a mass function;
(b) the approach of (ξ′/ξ)(σ+√y) to its limit is monotone-regular (O(√y)), no oscillation
obstruction; (c) orientation — y↓0 must pair with the non-regular end x→∞, consistent with
q(0⁻) = ∞ and L = ∞. Numerical anchor: the control-cancelled fits, fitted/predicted 0.9995,
0.9996, 0.9996 at ω = 0.5, 0.75, 1.0, ω-scaling exact to ~10⁻⁴ (note §2).

---

## 4. Theorem D — universal UV law (referee priority 5; erratum 1 corrected)

**Theorem D.** For every ω ≥ ½ (or ω > ω_c), unconditionally:

> m_ω(x) ~ 4x/(log x)²  as x → 0⁺,

the same law and constant as Kotani's RH-conditional zeta string.

*Proof.* Exact large-y asymptotics from the closed form:
(ξ′/ξ)(σ+√y) = ½ψ((σ+√y)/2) − ½log π + O(y^{−1/2}) = ¼ log y · (1+O(1/log y)), with
ζ′/ζ(σ+√y) = O(2^{−√y}) — **ω-independent at leading order and unconditional** (this is the
analytic face of "RvM density is ω-independent"). So q_ω(−y) ~ (¼ log y)/√y as y → ∞: regularly
varying of index −½ with slowly varying part ℓ(y) = ¼log y. Kasahara's theorem at the regular
end (x→0⁺, dual to y→∞) converts this into m(x) ~ 4x/(log x)²: on the dual curve
x(y) = q(−y), M(y) = 1/(y·q(−y)), substituting √y ~ log(1/x)/(2x) gives M ~ 4x/log²x. Constants
agree with Kotani's case because only the leading RvM growth enters. ∎ — same citation status
as Theorem C. Status: **proved modulo the internal theorem number in Kasahara 1975**.

**Corrected numerics (replaces the note's erroneous "ratio → 1.08 at y = 10⁻⁶").** The analytic
dual-curve ratio M(y)/[4x/log²x] at ω = ½:

| y | 1 | 10³ | 10⁶ | 10⁹ | 10¹² | 10¹⁵ |
|---|---|---|---|---|---|---|
| ratio | 374 | 4.26 | 1.388 | 1.093 | 1.008 | 0.974 |

→ 1 as y → ∞, non-monotonically (it crosses 1 near y ≈ 10¹²·⁵; the correction is
[(½log y − log(ξ′/ξ))/(½log y − log 2π)]², slowly varying, sign-changing). UV = y→∞ confirmed;
the convergence is log-slow, which is *why* no feasible string reconstruction can see this law
directly — it is an analytic statement, exactly as the note's own caveat said.

---

## 5. Theorems E and E′ — the RH endpoint (referee priority 6; its "most conceptually valuable" item)

**Theorem E′ (existence of the family ⟺ RH; unconditional).** Let ρ = β+iγ, γ > 0, be a zero
with β > σ = ½+ω. Then q_ω has the pole pair

> z_ρ = γ² − (β−σ)² ∓ 2iγ(β−σ)  (from ρ and ρ̄; both non-real),

in ℂ∖[0,∞); a Herglotz function is analytic off ℝ, so q_ω ∉ N_S and **no positive Kreĭn-string
realization exists**. Combined with Theorem A's conditional version:

> **RH ⟺ q_ω ∈ N_S for every ω > 0 ⟺ the ω-string family extends to the whole half-line ω > 0.**

This is the theorem-grade replacement for the note's "below ω_c the measure loses positivity":
what provably fails below ω_c is the Herglotz/passive-string property (via non-real poles);
whether the formal boundary density ρ_ω itself goes negative somewhere is open — and not needed.
(For the time-side statement the paper's thm:transition is stronger still: two-sided exponential
oscillation of Ψ_ω below ω_c.) Boundary case ω = ω_c: if the sup is attained by a zero on
Re s = σ exactly, q_ω acquires a boundary singularity on the cut — excluded from both statements;
remark only.

**Theorem E (RH endpoint).** (i) *Unconditional:* as ω ↓ 0, q_ω → q₀, q₀(z) = i(ξ′/ξ)(½−i√z)/√z,
locally uniformly on ℂ∖([0,∞) ∪ P), P the (possibly empty) pole set of q₀, with rate O(ω):
|q_ω − q₀| ≤ ω · sup|(ξ′/ξ)′| on the relevant compact (measured: 0.0462·ω at z = i, 0.0307·ω at
z = −1+2i, exactly linear over ω ∈ [0.01, 0.5]). Under RH, P ⊂ [0,∞) (poles sit at z = γ² *on*
the cut) and the convergence is locally uniform on all of ℂ∖[0,∞), where q₀ = q_ξ, Suzuki's
RH-conditional Weyl function.
(ii) *Under RH:* the spectral measures converge vaguely,

> σ_ω ⟹ 2 Σ_{γ>0} δ_{γ²}  (ω ↓ 0),

Kotani's pure-point zeta-string measure (masses 2, matching Suzuki §9). Proof: locally uniform
convergence of Herglotz/Stieltjes functions with vanishing linear terms is equivalent to vague
convergence of representing measures (Grommer–Hamburger); the limit measure is read off q_ξ
(Suzuki §9), or directly: each conjugate zero pair contributes Poisson kernels of width ω at ±γ
with unit mass each, → δ_γ + δ_{−γ}, pushforward mass 2 at λ = γ². Numerical check: against a
unit Gaussian f at γ₁, J(ω) = ∫ρ_ω f du = 0.635, 0.817, 0.900, 0.948, 0.979 at
ω = 0.5, 0.2, 0.1, 0.05, 0.02 → f(γ₁) = 1, deficit ≈ 1.0·ω. ✓
(iii) *Under RH, strings:* m_ω(x) → m_ξ(x) at every continuity point of m_ξ, by continuity of
the Kreĭn correspondence — now pinned to **[Kasahara 1975, Theorem 1]** (see §8.1). Status:
**standard consequence, citation pinned (secondhand)**.

Failure modes: without RH the endpoint is never reached — the family ceases to exist at ω_c > 0
(E′), so E(ii)–(iii) are genuinely RH-conditional, and conversely the *statement* "σ_ω converges
as ω↓0 to a positive measure" fails structurally below ω_c, making the endpoint behavior itself
an RH-equivalence at the level of the family. Vague convergence cannot see mass escaping to
λ = ∞ — both sides have infinite total mass; "local weak convergence" is the honest topology,
as the referee's own wording suggested.

---

## 6. Corrections applied to `NOTE_omega_string.md` (this round)

1. §2 header and body: "inverse spectral problem solved numerically" → discrete inverse problem
   solved to ≤10⁻¹¹⁷; continuum convergence separate, quadrature-dominated (referee 4.1).
2. §1 check 4: Hilbert–Pólya phrasing → "integrated spectral measure has the same leading
   Riemann–von Mangoldt growth as the zero-counting function" (4.3).
3. §3: "all rigorous" → tier structure; "localization transition" → "a.c.→pp spectral
   transition" with localization as explicit gloss (4.4, 4.6).
4. §3: "below ω_c the measure loses positivity — no string exists" → Herglotz failure via
   non-real poles (Theorem E′), density-negativity flagged open (4.5).
5. UV bullet: erratum 1 — corrected direction/values table (4.7).
6. Bulk bullet: erratum 2 — 1874.7255 → 1874.7243; slope closed form γ/2+1−½log 4π added.
7. Figure spec (referee §5): **executed** — see §8.3; captions as specified, string figure
   framed as numerical evidence, bulk density attributed to Theorem C with numerics as
   validation, not proof.

## 7. Claim tiers for the companion paper (the referee's four levels, instantiated)

- **Theorems (proved this round):** A (measure identification), B (+ margin = πρ_ω(0)),
  E′ (family-existence ⟺ RH), E(i) (Weyl convergence), E(ii) (vague convergence, modulo the
  standard Grommer–Hamburger step).
- **Standard consequence once cited (citations now pinned to the extent possible — §8.1):**
  C, D (Kasahara Tauberian), E(iii) (Kreĭn-correspondence continuity, [Kasahara 1975, Thm 1]).
- **Numerical evidence:** discrete inverse reconstruction (≤10⁻¹¹⁷ on the discretized measure);
  control-corrected absolute IR density (0.9995–0.9996); the UV–crossover–bulk profile shape;
  the ω-scaling of ρ_∞ to ~10⁻⁴.
- **Interpretation/conjecture:** zeros ↔ resonances of width ω (RH-conditioned wording); margin
  slope ↔ zero-energy DOS ↔ inverse-square bulk density (the boxed bridge — now theorem-backed
  via B and C); "localization"/"phase transition" as glosses only.

## 8. Next steps — status after the same-day follow-up session (2026-08-28 p.m.)

1. **Citations — pinned as far as fetchable sources allow.**
   - *Continuity of Kreĭn's correspondence* (Thm E(iii)): **[Kasahara 1975, Theorem 1]** —
     secondhand via Faggionato, EJP 17 (2012) (`\cite[Theorem 1]{K}` for the continuity theorem
     "based on Krein's correspondence"); corroborated by Kotani, Kyoto J. Math. 53 (2013)
     ("Later Kasahara established the continuity for the correspondence…", ref = Japan. J. Math.
     1 (1975), 67–84) and by Eckhardt–Kostenko–Teschl, J. reine angew. Math. 736 (2018) ("the
     proof of Y. Kasahara was based on the use of scaling and continuity properties of the Krein
     correspondence for strings").
   - *Tauberian theorem* (Thms C–D): cite Kasahara 1975 **without an internal number** (the free
     J-STAGE PDF, DOI 10.4099/math1924.1.67, is robots-blocked to automated retrieval; no
     fetchable secondary source displays the numbered statement) together with
     Kasahara–Watanabe, Kyoto J. Math. 50 (2010), 623–644 (*Asymptotic behavior of spectral
     measures of Kreĭn's and Kotani's strings* — the modern refined form, n.&s. conditions for
     σ(ξ) ~ const·ξ^α) and Kotani–Watanabe, LNM 923 (1982), 235–259.
   - *N_S ↔ string:* Kreĭn, Doklady Akad. Nauk SSSR 87 (1952), 881–884 (= Suzuki's [13], §9);
     *screw functions:* Kreĭn–Langer, IEOT 78 (2014), Thm 5.1 (= Suzuki's [16]). Also useful:
     Kasahara–Watanabe, Proc. Japan Acad. 85 (2009), 22–26 (the correspondence itself).
   - **USER ACTION:** download the free Kasahara 1975 PDF from J-STAGE by hand and confirm the
     internal theorem numbers before submission; the paper flags this in its "Status of the
     Tauberian citations" paragraph.
2. **Paper drafted:** `claude/PAPER_omega_string.tex` — "The shifted zeta string: an
   unconditional inverse-spectral family and its RH endpoint", 11 pp., compiles clean
   (pdflatex, no warnings). Structure: Theorems A→1.1, B→1.2, C→1.3, D→1.4, E′→1.5, E→1.6 with
   full proofs; numerics as evidence (§7); physics dictionary last (§8), tiered; open problems
   (§9: effective endpoint rate, Gelfand–Levitan high-resolution inversion, Dirichlet family,
   de Branges contact). Cites the margin paper as companion [13]; margin thm:transition is
   Thm 1.5 there. Needs: author block, acknowledgements, the fig_string regeneration (§8.3),
   and the §8.1 hand-check.
3. **Figures:** `fig_density.png` regenerated (two panels: ρ_{1/2} on [0,60] vs RvM mean;
   Lorentzian sharpening at γ₁ for ω = 0.5/0.25/0.1) with the referee-approved title/caption;
   embedded in the paper as Figure 1. The **string figure remains deferred** to the
   numerics-polish stage (requires re-running the peeling pipeline; the better route is the
   paper's Open Problem 2).
4. Numerical polish of the inverse-string machinery: unchanged — last, per the referee.

## Reproduction

`v1_identities.py`: Lemma A.2 at four (a,γ,z) — 3·10⁻³³, 2·10⁻³³, 1·10⁻³², 2·10⁻⁴⁴ (the last at
near-cut z = 100+i with refined quadrature); transform block to 3·10⁻²³; slope closed form vs
direct (agreement 6·10⁻⁹, limited by the s→1 regularization offset — the closed form is
authoritative). `v2_thmE_kasahara.py`: q_ω → q₀ linear-in-ω table at two z; J(ω) Gaussian test
at γ₁ (mp.zetazero); the corrected Kasahara dual-curve table (§4). `fig_density.py`: Figure 1
of the paper. All mpmath, dps 15–40.
