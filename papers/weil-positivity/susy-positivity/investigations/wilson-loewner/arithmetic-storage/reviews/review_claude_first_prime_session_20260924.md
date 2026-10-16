# Review of the arithmetic-storage opening package and first-prime session

24 September 2026. Review prepared for Edward Baker with substantial LLM assistance.

**Model:** Claude (Anthropic). The session is configured as `claude-fable-5-1`; the
runtime environment reports the serving model as Claude Opus 5.5 (`claude-opus-5-5`).
The serving model may differ from either identifier. Reasoning effort: not exposed.

**Scope:** commit `1bd1adf` ("Initial work on the arithmetic-storage program"), prepared
by GPT-6 (Codex). The review covered:

- the opening [program note](../notes/ARITHMETIC_STORAGE_PROGRAM_AND_GOALS_20260924.md), the [first-prime analysis](../notes/FIRST_PRIME_CONTINUATION_ANALYSIS_20260924.md) and its [handoff](../notes/RESEARCH_CONTINUATION_AFTER_FIRST_PRIME_INPUTS_20260924.md);
- the three programs and four records under `numerics/`;
- the inherited [operator-coupling certificate](../../../critical-path/notes/CUMULATIVE_OPERATOR_COUPLING_CERTIFICATE_20260920.md) and the [cross-program assessment](../../notes/CROSS_PROGRAM_PRIORITIES_AFTER_WZW_AND_N4SYM_REVIEWS_20260924.md).

**Status:** a same-family LLM audit. It includes replays, an independently written
floating model, Arb runs of the repository's own weil-depth pipeline, and new elementary
lemmas. A separate subagent refereed the new lemmas and replayed the horizon-3/4
certificates; its corrections are incorporated in the note. It is not specialist review. The new mathematics is in the companion
[research note](../notes/FIRST_PRIME_JOIN_EQUIVALENCE_AND_PRIME_WEIGHT_RIGIDITY_20260924.md).

## 1. Verdict

The first session is careful and, as far as I can check, correct. Every certified
inequality replays at 40 and 60 digits with identical results. An independently written
Galerkin model reproduces every stated number to the precision given. I found no
arithmetic or sign error in the derivations.

The session's *target*, however, does not test what it was meant to test, and the next
bounded task was already answerable with existing repository tools.

- **The append hypothesis is joined-window positivity.** By an elementary Schur-complement
  lemma (Lemma A of the note), κ₀ ≤ κ is equivalent to Q_{0,R} ⪰ (1 − κ)(Q_{0,L} ⊕ Q_{0,h}).
  So "κ₀ ≤ 0.999 at (11/20, 1/5)" is a relative Weil-positivity inequality on (0, 3/4). No
  arithmetic delay is "crossed" by the method beyond what positivity on the joined window
  already says.
- **Contraction follows directly.** Contraction of the joined transfer follows from
  joined-window central positivity through the defect identity (weil-depth's Proposition
  "central coercivity implies contraction"), without the energy-transfer lemma.
- **The task is closed in about 20 seconds of computation.** The weil-depth builder and
  Schur test, unchanged, certify Q_{0,3/4} ⪰ (123/250000)I; weil-depth's independent
  implementation agrees. With a five-line norm lemma this gives κ₀ ≤ 0.99980, a normalized
  cumulative coupling ≤ 0.99982 < 1 at ω = 10⁻³, and directly ‖V_{ω,3/4}‖ ≤ e^{−ω/5000} for
  ω ≤ 1/50. Even weil-depth's existing log 3 floor already implied κ₀ < 1 − 2.2·10⁻⁸ at this
  split.
- **Joins of fixed length cannot carry a fixed margin.** For every h, sup_L κ₀(L, h) ≥ 1,
  unconditionally (Proposition 1 of the note). Chains with shrinking joins remain possible
  in principle; that infinitesimal limit is the canonical-system (Schur) recursion, not the
  finite-append certificates of the session.

The genuinely informative output of the session is its certified negative gamma/pole
witness at R = 3/4. This session sharpens it into a certified threshold 0.74 < R_A ≤ 0.745
and a rigidity table for the first prime's weight.

**Recommendation:** stop producing finite-append certificates, keep the existing ones as
records, and re-scope the program as in §6.

## 2. Replay

Replayed in the cloud container with Python 3.11.15, NumPy 2.4.4 and the committed sources.

| Program | Result |
|---|---|
| `certify_first_prime_inputs.py` (40 digits) | PASS. The `checks` section is byte-identical to the committed record; only the recorded Python version differs. |
| same, `--digits 60` | PASS; identical `checks`. |
| `diagnose_first_prime_coupling.py` | PASS. Every quotient agrees with the committed record within 1.5·10⁻¹⁴ (NumPy version differences). |
| `check_first_prime_records.py` | PASS: 15 nested interval pairs, 8 floating controls, conditional implication 413875000/414281559 < 49951/50000. |

The two 40-digit record hashes differ (`3caf68b7…` committed, `45a157e5…` replayed) only
because the Python version string is embedded in the record.

## 3. Independent recomputation

The recomputation is new code (`crosscheck_first_prime_galerkin.py`). It uses orthonormal
Legendre bases on one window or on the split (0, L) + (L, R). The gamma form is integrated
in the translation variable against the kernel 2e^{−u/2}/(1 − e^{−2u}), with exact
polynomial correlations; the poles enter as 2 f̂(i/2) f̂(−i/2), and the primes as exact
partial translations. This is independent of the session's cosine/exponential-series
formulas and of weil-depth's moment method. All values are floating.

| Quantity | Session | Independent value |
|---|---|---|
| λ_min Q_{0,11/20} (certified floor 0.015) | 0.0171474 at 96 cosines | 0.0171288 at N = 80 |
| λ_min Q_{0,1/5} (floor 0.44) | 0.457147 | 0.457084 |
| ψ witness: Q^A, prime, Q | (−0.001003, −0.000754); +0.02210390116; (0.021101, 0.021350) | −0.000962346; +0.0221039012; 0.0211415548 |
| (f, v) witness: complete, M = 128 proxy | (0.004951, 0.006525); (−0.004133, −0.003380) | 0.00533346; −0.00403806 |
| κ₀ complete / archimedean / prime | 0.99647753 / 1.06569 / 0.63607 at 96 cosines | 0.9964810 / 1.066200 / 0.636337 at 48 Legendre modes per window |
| λ_min of the joined form | 4.931·10⁻⁴ (recorded, not discussed) | 4.9239·10⁻⁴; weil-depth encloses [4.92, 4.92324]·10⁻⁴ |

Normalization checks: my λ_min at log 2 (1.329311·10⁻³) and at log 3 (5.5436·10⁻⁸) fall
inside weil-depth's enclosures. At R = 3/4 the form of a smooth test function equals
Σ_ρ |f̂(γ_ρ)|² over ±300 zeros to a relative 7·10⁻⁹.

## 4. Audit of the derivations

Each of the following was checked by hand, and the numbers were recomputed.

- *Generator.* The symbol is 2(ξ'/ξ)(1/2 + p) = w₀ + [ψ(1/4 + p/2) − ψ(1/4)] + 2/(p + 1/2) + 2/(p − 1/2) − Σ 2Λ(n)n^{−1/2−p}, with w₀ = ψ(1/4) − log π = −5.37218…. The n = 0 gamma term cancels the decaying pole; the kernels match (2.2) of the certificate note and §2 of the analysis. The pole form satisfies 2⟨c,f⟩² − 2⟨s,f⟩² = 2⟨e^{x/2},f⟩⟨e^{−x/2},f⟩.
- *Shift.* The shifted generator is (log H)'(p − s) + (log H)'(p + s). No constant shifts, and G_s − G_0 has causal kernel −2H_0^A(u)(cosh su − 1) on prime-free windows. This confirms (4.1). Bound (4.3) is correct, including the Carleman majorant and the prime term c_p(cosh(sa) − 1).
- *Defect floors.* (4.2) follows from ‖V_s f‖² ≤ e^{−2s(m−δ)}‖f‖² and Z* = JZJ.
- *Constants in (4.4).* sqrt(0.015·0.44) > 0.0812, the relative losses are below 10⁻⁵ and 3·10⁻⁸, and the implication is correct.
- *Operator facts.* (2.1) is correct: finitely many constraints on an infinite-dimensional active segment. It is elementary.
- *First-prime transfer.* The expansion V = T + c₂S_aT with c₂ = (2^ω − 2^{−ω})/√2 on log 2 < L < log 3 is correct. Compressions of causal products factor, and c₂'(0) = √2 log 2 reproduces the prime term −((log 2)/√2)(S_a + S_a*).
- *Witness logic.* §5 and §6 are correct. The endpoint-strip inequality ‖g‖² − Re⟨g, S_u g⟩ ≤ u‖g‖²_∞ + (u²/2)‖g′‖² holds exactly as (1/2)∫₀^u g² + (1/2)∫_{ℓ−u}^ℓ g² + (1/2)∫(Δ_u g)². The omitted-tail bound (6.3) follows.
- *Code.* The certificate code implements the stated formulas: rates 2n + 1/2; features sqrt(2a²(1 ∓ e^{−aℓ})); pole coefficients sinh(ℓ/4)/(1/4 + k²) and cosh(ℓ/4)/(1/4 + k²); the prime overlap on (a − L, h) with phases ±k_j a; and the reflection r = L − y. Assertions guard every sign decision, and `python -O` is refused.

## 5. The main issue in detail

**What the session set out to test.** The program note (§4) and the analysis (§8) present
the first-prime append as a test of "whether the parent continuation method can survive a
genuine arithmetic delay". By Lemma A, the method's hypothesis at that join *is* Weil
positivity on the joined window, with a relative margin. Nothing about the prime is tested
beyond positivity of Q_{0,3/4}.

That positivity was already certified in the repository. Weil-depth's floor at log 3,
5.52·10⁻⁸, holds for every shorter horizon by compression. The coercive joined form then
gives the joined transfer's contraction directly.

**Why the 0.999 target looked hard.** The margin was being spent in the block
decomposition. Splitting at the join creates large artificial endpoint energies in Q_L[f]
and Q_h[v] (jumps of the zero-extended pieces). The Carleman corner of H cancels them.
That is why the archimedean relative norm exceeds one (1.066) while the joined form is
positive, and why the M = 128 tower, which discards part of that endpoint energy, fails.
Working directly on the joined window, as weil-depth does, avoids the problem.

**Statements to annotate.** Two earlier documents describe an enlarged-window central
certificate as something other than the coupling task:

- the critical-path certificate ("no enlarged-window central certificate is substituted");
- the cross-program assessment ("a useful control, not a solution").

Both are defensible if "central certificate" means an absolute floor and "solution" means a
continuation mechanism. Still, at zero shift the coupling hypothesis *is* a joined-window
central inequality in relative form, and the positive-shift remainder is O(ω²). I suggest a
one-line annotation in each rather than a rewrite.

To be fair to the earlier work, the relative form is quantitatively stronger than an
absolute floor. At the critical-path benchmark (R = 0.55), Lemma B with λ_min ≈ 0.0171
gives only κ₀ ≤ 0.9903, while the critical-path certificate proved 0.951. It remains a
statement about one joined window.

**What the energy-transfer lemma does add.** It gives a quantitative Schur-complement
margin, E − Y*F^{−1}Y ⪰ (1 − κ²)E. The lemma is correct and useful as a statement about the
defect's structure. It is not an iteration mechanism, because the next join again requires
joined-window positivity. Proposition 1 of the note shows further that no fixed per-join
margin can be carried along a chain whose join lengths are bounded below.

## 6. The negative results, and re-scoping

- **Gamma/pole witness at 3/4.** Meaningful: the prime is needed at this length. The
  threshold is now bracketed, 0.74 < R_A ≤ 0.745 (certified). The archimedean form alone
  stays positive about 7% past log 2, so the prime does not arrive "just in time". Past
  R_A its weight is quickly pinned, asymmetrically:
  - at R = 0.85 the admissible interval is [−6.7%, +1.07%];
  - at log 3 it is [−8·10⁻⁵, +3·10⁻⁶] (certified outer bounds).

  Under RH, every single-weight change fails at some finite window (note, §4).
- **M = 128 proxy failure.** Correct, but informative only about that lower-bound
  technique (§5 above).
- **Lesson drawn in the analysis (§8)** ("discarding positive gamma energy can erase the
  cancellation needed at a prime threshold"). It is accurate, but it concerns the block
  decomposition. The structural lesson is stronger: positivity at the first prime is exact
  arithmetic cancellation, with margins that vanish as the window grows.

Re-scoping, following the note (§5):

- Stop the finite-append chain. Do not extend it to log 3, log 4 or log 6; weil-depth already covers those joined windows directly. The infinitesimal version (fixed relative margin with joins shrinking like e^{−L}), which Proposition 1 leaves open, belongs to the canonical-system comparison.
- Adopt the first-prime weight window as a mandatory quantitative filter for any proposed mechanism, alongside the smooth-density control.
- Give the next session to one exact-arithmetic framework: the semilocal Sonin residual, re-derived from primary sources because the 14 September derivation is outside the repository, or the canonical-system comparison. Alternatively, fold the folder into those programs.

## 7. Smaller points

1. The handoff's target κ₀ ≤ 0.999 is stronger than (4.4) needs. With the session's
   constants the requirement is κ₀ < 1 − 1.82·10⁻⁵ (loss 9.94·10⁻⁶ plus 6.73·10⁻⁷/0.0812).
2. The analysis never mentions that its own diagnostic computed the joined-window bottom,
   about 4.93·10⁻⁴. That number, with Lemma B, closes the task.
3. The program note (§7) plans tests at log 3, log 4 and log 6 "in their actual order".
   Weil-depth already certifies those joined windows, including the mixed overlaps (2, 3)
   and (3, 2) at 9/5 and log 7.
4. The Sonin formulas in the program note rest on a machine-specific file outside the
   repository (`/Users/ebbaker/.codex/…`). Any Direction B work must start by re-deriving
   them; the cross-program assessment already says so.
5. Record keeping is good: model lines, source hashes, nested precision records, and
   explicit non-claims. The only gap is that the root `CHANGELOG.md` has no entry for
   commit `1bd1adf`; this session adds one covering both.

## 8. Evidence for this review

The replays and the independent model are recorded under
`numerics/records/first-prime-galerkin-crosscheck-20260924.json`. The closure, the
rigidity table and the threshold have their own records, listed in the note's §6. The weil-depth
builder was imported unchanged; no ball archive was saved (LARGE_FILES policy); each run
rebuilds in 20–90 s. The same assistant produced the review, the new lemmas and the
checks. A specialist should look in particular at Lemma A's domain statement (splitting
log-energy functions at the join), at Proposition 1's determinism step, and at the
weil-depth tail estimate on which all the Arb results rest.
