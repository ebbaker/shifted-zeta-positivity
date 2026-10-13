# Handoff — C1/C2 verification, session state at 10 Sept 2026

Read this first, then `claude/PROTOCOL_C1_C2_verification_20260906.md`.
This note records what happened in the working session that produced that
protocol, and amends one part of it.

---

## 1. Where C1 stands

**Part 1 (derivable without Suzuki): complete.**

- The master factorization is confirmed:
  `Θ_ω(z) = ξ(s−ω)/ξ(s+ω) = [Γ_∞(s−ω)/Γ_∞(s+ω)] · [ζ(s−ω)/ζ(s+ω)]`
  with `s = ½ − iz`, following from `ξ = Γ_∞ζ` alone. Done by hand.
- The Dirichlet identity `Σ c_ω(n) n^{−w} = ζ(w−ω)/ζ(w+ω)` with
  `c_ω(n) = n^ω Σ_{d|n} μ(d) d^{−2ω}` is confirmed, via
  `c_ω = (μ·Id^{−ω}) * Id^{ω}`.
- Domain of absolute convergence: `Re s > 1 + |Re ω|`; for `ω` real in
  `(0, ½]`, `Re s > 1 + ω`.

**One error was made and corrected during this step**, and it is worth
recording because of what kind of error it was. In the first hand derivation
the two weights were attached to the wrong factors — `n^{ω}` to the Möbius
sum and `n^{−ω}` to the all-ones sum — which computes `ζ(s+ω)/ζ(s−ω)` and
yields `c_{−ω}(n)` rather than `c_ω(n)`. Confirmed numerically: at `s = 3`,
summed to `n = 4000`, the swapped coefficient reproduces the reciprocal ratio
to ~1e−9, and `c_swapped(n, ω) = c_paper(n, −ω)` exactly.

That is an **ω sign flip** — precisely the class of error C1 exists to
detect, since a sign or factor slip in the normalization chain would move the
`log 2` threshold while leaving every downstream computation internally
consistent. The blind derivation caught it. The domain conclusion is
unaffected by the swap (both assignments give the same two convergence
conditions).

**Parts 2, 3 and 4: not started.** N1–N4 (the four items needing the Suzuki
PDF), the blind threshold re-derivation, and P1–P3.

## 2. Where C2 stands

Not started. Targets, search strings, venues and the MathOverflow draft are
in the protocol, Part 5 and the Appendix.

## 3. Amendment to the protocol's independence rule

Part 0 of the protocol states the independence rule too broadly ("don't let
this document or any model tell you what Suzuki's paper says"). The rule that
actually matters distinguishes:

- **Regenerable claims** — anything you can derive and verify yourself. Being
  told these first costs little, because your check does not depend on the
  teller. All of Part 1 is in this category.
- **Testimony** — claims about what is printed in [1]. You cannot regenerate
  these; you can only look. Once told what to expect, looking is
  contaminated. N1–N4 and the P-items are in this category, and nothing in
  this project has been told to the author about them.

Read Part 0 as governing the testimony tier only.

### Consequences for two specific items

- **Part 1.3** (record beliefs before comparing) was pre-empted during the
  session and is spent. Low cost — it covered regenerable items only.
- **The domain of [1, Prop. 2.1]** was named as `Im z > ½ + ω` during the
  session before the author derived it, so that check is no longer blind.
  The author judged it recoverable (the source had only been skimmed) and is
  re-deriving from scratch. Standing safeguard: **if what is printed in [1]
  does not match the derived domain, the mismatch is the finding** — do not
  resolve it by assuming a miscounted shift.
- **Still completely clean:** the domain of validity of the Mellin formula in
  [1, §3.1]. Nothing has been said about it in any session. Derive the
  convergence half-plane for `∫ g_ω(x) x^s dx/x` from N1's support claim,
  write it down, then compare against both [1] and §3.1 of the preprint.
  This is the unspoiled domain fingerprint.

## 4. Context not recorded elsewhere

- The paper's **certificate is load-bearing**, not corroborating: S14 and S18
  are status `computer`, and Theorem B — hence Theorem A — rests on interval
  arithmetic with no analytical proof behind it. Statements with paper proofs
  plus numerical confirmation (Prop. 4.2, the §6.3 constants, the Laplace
  transform check) are a separate category, and S08/S05/S21 are a third:
  numerics standing in for a proof that is not written, with S21 having
  neither.
- Per the blueprint's own assessment, the **certificate stack is the more
  formalizable half** (Flyspeck pattern: stored interval matrices plus a
  verified LDLᵀ checker), while the §8 chain S21–S26 is out of reach because
  Mathlib lacks uniform Stirling on vertical lines, the digamma integral
  representation, and distributional limits.
- **Distribution plan:** Zenodo + version DOI for priority; no arXiv; Lean
  Zulip as the most promising route, with a narrow ask (are two or three
  `good-first-check` statements cleanly stated, and does Mathlib have the
  pieces) rather than a request to formalize; MathOverflow for the C2
  originality question; friends first, escalate only if it survives them.
  S19 (Lemma 7.1) is the identified afternoon-sized Lean target.
- **Highest-value single action remains an email to Suzuki**, which would
  settle C1, P1–P3 and C2 Target A at once.

## 5. Open checklist

- [ ] N1 support of `g_ω` — transcribe from [1]
- [ ] N2 form of `h_ω`, [1, eq. (2.3)] — transcribe verbatim
- [ ] N3 Hankel kernel and measure, [1, eq. (2.5)]
- [ ] N4 compression window, [1, eq. (2.6)]; re-derive `L = 2 log a`
- [ ] Part 3 blind re-derivation of the layer formula and the `log 2` threshold
- [ ] Mellin-domain fingerprint from [1, §3.1] (clean check — do before reading §3.1 of the preprint)
- [ ] P1–P3 citation checks
- [ ] C2 Target A (off-center kernel identity) and Target B (energy identity, incl. systems-theory literature)
- [ ] Post the MathOverflow question
- [ ] Record results in `verification/first-slab/` and update §13
