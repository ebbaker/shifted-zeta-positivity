# Cross-model review of the first Newman certificate audit session

12 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Reviewer: Claude Opus 5.5 (configured model `claude-opus-5-5`, Cowork
session; reasoning effort: max). Reviewed: notes 1–2, the numerics folder
and the README changes written earlier the same day by Claude Fable 5.1
(`claude-fable-5-1`), committed as `610a653`. This is a second-model
internal review. It is not independent specialist validation, and the two
sessions used the same tools and may share blind spots.

Pinned package throughout: `judegomila/dbn-lambda-01787854-candidate-audit`
at `a74738deb6d5e0f76887cb36901da08b68dca705`.

## Verdict

The two notes are accurate. Every numerical claim I re-executed
reproduced. The transcription of the published criterion and error bounds
is correct. The benchmark decision (stop the corrected-interface campaign
for this certificate class) is sound. I found no error that changes a
conclusion. The items in §3 are refinements:

- one sharpness claim needed its reason;
- the lemma behind the side observation has a two-line proof and is
  stronger than the note says, so half of the work it lists (the window
  freeze) is unnecessary;
- the package's external referee report makes a context claim that note 2
  §5 contradicts, and the notes did not say so;
- reasoning effort is not recorded.

Note 3, written in this session, completes two of the ledger's four
remaining audit items: an independent certified replay of the weakest
rows, and an independent re-verification of the Dini gate.

## 1. What was re-executed

| Item | How | Result |
| --- | --- | --- |
| Pin and seal | fresh fetch of `a74738de…`; `sha256sum -c SHA256SUMS` | 443/443 OK |
| Polymath Theorem 1.2 | arXiv:1904.12438v2, read through WebFetch (the extracted text reaches §7) | the ranges in (i)–(iii) and the conclusion `Λ ≤ t0 + y0²/2` agree with ledger §3 |
| Theorem 1.3, (20)–(24) | same | agree, including `t/(2x²)` in (21), the single denominator `x − 6.66` under both terms in (23), and `10.44`, `x − 12` in (24) |
| Proposition 6.6(vi) | same | `e_C` and `e_{C,0}` agree with `check_newman_error_budget.py`, so `e_C/e_{C,0} = s/(1+s)` exactly as stated in ledger §4 |
| Error-budget record | re-ran `check_newman_error_budget.py` (Python 3.13.16) | byte-identical JSON |
| Weakest row | re-ran `replay_triangle_row.py --N 690988` on Teddy's machine (aarch64, numpy 2.2.6) | `7.913667465e-7` against the recorded `7.913667453e-7` (float noise); sharp weight `0.07700` |
| Stored corpus | parsed all 15 certificate shards | 3,149,013 contiguous rows `690988…3840000`; 23 first-of-run rows; each leg's minimum is its first row; agrees with `PROOF_NOTE.md` (4.8) |
| Barrier transcript | parsed `barrier_target_closed.log` independently | 883 prisms, all `PASS`; 14,493,508 mesh evaluations; minimum margin `0.5198499` (prism 882); minimum `|f|` `1.5432` (prism 883); allowance/margin `0.066–0.240 %` |
| Tail transcript | `logs/tail_arb_256.log` | `D < 0.999721`, `M_max < 1.608290`, flow `1.73533e-4`, error `1.16716e-8`, as in ledger §3 |
| "Frozen sawtooth" | producer source header | confirmed: within a run the weight freezes γ at `g(max(n/d_min, N_start)) ≥ g(N)`; at a run's first row the weight is the exact Triangle summand and the value is exact up to a proven Taylor remainder |
| Sensitivities | recorded runs | `∂L/∂(y²) = 9.528`, `∂L/∂t = 19.058` |

The certified replay in note 3 removes the main computational caveat of
note 2 §2. `L_{690988}` lies in `[7.9136674559412e-7, 7.9136674559419e-7]`,
and the 12-decimal floor reproduces the stored value exactly.

## 2. Confirmations worth recording

1. **The uniform-lane argument (ledger §4) is right.** A lane that bounds
   `|f_t|` by a triangle inequality uniformly over a window can use the
   Riemann–Siegel `C` term only through `sup_window |C_t/B_t|`. The
   corrected interface is a pointwise statement, so it has nothing to offer
   this lane. The barrier could use it, but there the allowance is 0.07 %
   of the margin.
2. **The published row is optimal for its lane.** The sensitivity ratio
   `19.058/9.528 = 2.0002` is the first-order condition for minimizing
   `t0 + y0²/2` along the lane's boundary, since `∂Λ/∂t : ∂Λ/∂(y²) = 1 : 1/2`.
   The "almost neutral" trade in note 2 §3 is exactly this condition. It
   shows the parameters were tuned against this lane, which supports the
   note's reading that the lane, not the error term, is the binding
   constraint.
3. **The decision follows from the stop test.** The decision in note 2 §6
   is the README's stop test applied as written.

## 3. Corrections and refinements

1. **Ledger §4, "sharp up to the factor 1 + s".** This is true but not
   explained. Polymath's dropped term is built from
   `C_0(p) = (e^{πi(p²/2+3/8)} − i√2 cos(πp/2)) / (2 cos πp)`, where
   `p = 1 − 2(a − N)` and `a = √(T'/2π)`, `T' = x/2 + πt/8`. The bound
   `e_{C,0}` uses `|C_0(p)| ≤ 1/2`. Since `|C_0(±1)| = 1/2` at both ends of
   a window (and `|C_0(0)| ≈ 0.31` in the middle), the supremum over a
   window is attained near its ends. That supremum is what a uniform lane
   pays.
2. **Note 2 §3.** `1/2 − 9.528/19.058 = 0.00005`, not `0.0001`.
   Immaterial.
3. **The side observation's lemma (note 2 §5; project README).**
   1. *Proof.* Put `T_γ(w) = w + γ w̄`. A term `b z + γ a z̄`, with
      `z = n^{−s}` and real `a`, `b`, equals `T_γ(u)` with
      `|u| ≤ U_r(b,a) := (|b − r²a| + r|a − b|)/(1 − r²)`, where
      `r = |γ| < 1`. Since `S = T_γ(1 + Σ u_n)` and
      `|T_γ(w)| ≥ (1 − r)|w|`, it follows that
      `|S| ≥ (1 − r)(1 − Σ U_r(b_n,a_n) n^{−σ})`.
   2. *Weight.* `(1 − r)U_r(b,a)` equals the producer's sharp weight
      `max(|b − ra|, ((1−r)/(1+r))|b + ra|)`. This was checked on
      2·10⁶ random triples (largest relative discrepancy `4e-16`) and by
      cases.
   3. *Mollified sums.* Mollification keeps this form:
      `E f = Σ B n^{−s*} + γ(E/Ē) Σ A n^{−s̄*}`, with `|γ E/Ē| = |γ|`,
      and `B`, `A` real. This holds up to the `κ`-correction, which is
      handled as in the plain lane.
   4. *Monotonicity.* `U_r(b,a)` is nondecreasing in `r` for all real
      `a`, `b` (four sign cases). So the bound holds with any `g ≥ |γ|`
      in place of `|γ|` whenever it is nonnegative. Numerically: 5·10⁵
      monotonicity tests, and 2,745 random instances of the full lemma
      with `|γ| < g` and adversarial phase search, all without violation.

   **Consequence.** The sharp lane's window freeze needs nothing beyond
   the plain lane's, because the frozen `g_N` bounds `|γ(x)|`. Only the
   `y`-transfer must be re-proved, since `A_{N,n}` depends on `y`. Note 2
   §5 lists both. Note 3 §5 records the numbers at the certified row.
4. **Context the notes did not flag.** The package's external AI referee
   report (`EXTERNAL_REFEREE_REPORT_2026-07-28.md`, "Related" section)
   quotes a companion analysis. It says `0.1787854` "sits ≈2×10⁻⁷ from the
   certifiability wall at height 3×10¹²" and that "the only Λ-moving lever
   is more verified height".
   - Within the plain-Triangle lane it is consistent with note 2 §3, which
     puts the row within about `3·10⁻⁸` of its boundary in `Λ`.
   - For the method as a whole, note 2 §5 contradicts it. The published
     improved inequality, which the producer already implements, moves the
     lane's boundary by about `0.004–0.006` in `Λ` at the same height.

   The package's proof does not rely on the claim, so this is a correction
   to its framing, not to its theorem.
5. **Reasoning effort.** It is not recorded in notes 1–2 or in the
   numerics README, although the portfolio README asks for it.
6. **`DRAFT_HISTOR.md`.** The project README's Records section and the
   portfolio README both say `DRAFT_HISTOR.md`; the project instructions
   name the file `DRAFT_HISTORY.md`. The typo is inherited from the setup.
   This session corrects it in the project README only.
7. **Location of the improved inequality.** Ledger §1 locates it in
   Polymath "Section 8.5". The extracted text available to me ends in §7,
   so that location is unverified. The inequality itself is proved in
   item 3 above.
8. **Note 2 §6 on the cost of a rigorous replay.** It calls a rigorous
   replay of `L_{690988}` a computation over a "1.6·10⁹-term sum". Only
   about `1.1·10⁷` integers `n ≤ DN` have an active divisor, and they
   can be enumerated directly as `n = gcd(n,D)·k` with `k ≤ N`. The
   certified replay in note 3 therefore runs in about 100 s in standard
   Python.

## 4. The ledger's remaining obligations after this session

| Obligation (ledger §6) | Status |
| --- | --- |
| 1. Dini `y`-transfer and window freeze | **Window freeze:** checked by hand, correct. **Dini:** reduction checked line by line. The gate was re-verified independently with acceptance threshold 3/4 on the package's domain; in the `{2,3}` leg, `h ≤ 0` holds everywhere. The package's reported worst ratio `0.99999860767` is an artifact of its bisection stopping rule; the ratio at that leaf is about `0.12`. See note 3 §4. |
| 2. Lemma 8.4 majorants and prism gate | Open. This needs Polymath §8, which the WebFetch extraction does not reach. Margins are 400× the approximation allowance, but the majorants themselves carry the mesh argument. |
| 3. Tail-lemma gates | Open. |
| 4. Rigorous replay of the first-row floor | Done. Note 3 §3 gives an independent standard-library certificate for `N = 690988` and 31 further stored rows. |

Two further obligations should be added, because the package itself lists
them for referees:

- the proof-to-code map of `verify_prop410_arb.c`, which carries the
  uniform `E_max`;
- the two prose imports, namely `B_t ≠ 0` on the barrier box and the
  `t → 0` extension of Theorem 1.3 and Lemma 8.4.

## 5. Recommendation

The notes can stand as written, with items 3.1–3.8 recorded here. Further
audit work on the finite lane would mostly re-confirm results, because both
of its delicate links now have independent checks. The barrier majorants
are the largest unaudited piece of the package. Auditing them requires the
Polymath PDF in the session, kept outside the repository. Whether to pursue
the sharp lane (note 2 §6) remains Teddy's decision. Item 3.3 above makes
that lane cheaper than the note estimated: one new `y`-transfer gate, not
two lemmas.
