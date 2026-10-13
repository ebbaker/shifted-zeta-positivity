# Preprint v1.0 — deposit note (5 September 2026)

Converted `WORKING_DRAFT_first_slab_positivity` (3 Sept) into the preprint
`PAPER_first_slab_positivity_preprint_v1.tex` (24 pp., pdflatex, single file,
inline bibliography). Deliverables went to Teddy as a repo bundle
(README, CITATION.cff, .zenodo.json, LICENSE.md, VERIFICATION_STATUS.md,
.gitignore, PDF, .tex).

## Decisions taken with Teddy
- Author line: Edward Baker, NeoQuortex, teddy@neoquortex.com. **ORCID is a placeholder** (`0000-0000-0000-0000`) in the .tex title block and commented out in CITATION.cff — fill in before depositing.
- License: CC BY 4.0.
- Deposit scope: preprint only. Code / Investigation write-ups on request; later code release planned.
- Format: LaTeX + PDF (matches other PAPER_*.tex in the project).

## Substantive changes vs the working draft
1. **Item 0.3, corrected.** The certified Weyl–Schur margin *m* is the head clearance over κ²/d_tail; exact block-Schur gives Q ⪰ c·I with c = m − κ²m/(d(d−m)): c_even = 6.11594…e−4, c_odd = 5.26131…e−2. Theorem B now states c_* = 6.1159e−4; new Lemma 7.1 (block-Schur coercivity) + Remark 7.2. §8.6 uses c_*. The checklist/round-2 phrasing "Q ⪰ m·I" was slightly wrong (by ~4e−8).
2. **Item 0.4.** §1.1 and abstract now pinned to Suzuki [1]: Prop. 1.2 (ω₀>0: ζ≠0 for Re s>1/2+ω₀ ⟺ Θ_ω meromorphic inner for every ω>ω₀), Thm. 2.2 (inner ⟺ Hankel mapping property), Lemma 4.1 (inner ⟹ isometry). Single-shift "equivalence" removed.
3. **§9.3 rewritten.** Suzuki [1, Lemma 4.4] ("Let ω>1/2 and a>1") already proves ‖H_{ω,a}‖<1 for all finite sections via support Lemma 4.3 + compactness. Theorem A positioned as the complementary 0<ω≤1/2 result; ω=1/2 endpoint is new. (Statements from automated reading of the arXiv PDF — human confirm.)
4. **Item 0.6** inserted in Lemma 6.1 (a ≥ L/2 = 0.3466 > t₀ = 0.2812).
5. §12.1 + author-verification notice replaced by public **§13 Verification status** and Appendix C ledger row for ω>1/2. "Not for circulation" removed; LLM/computer-assisted disclosure kept on the title page.
6. §3.1 now quotes Suzuki's Mellin formula ∫g_ω x^s dx/x = γ(s−ω)/γ(s+ω), γ = Γ_∞ — this is the C1 normalization check (transfer and layer formula match [1] eq. (2.3), Prop. 2.1, Sect. 3.1).
7. Reference [1]: arXiv only (a RIMS journal ref could not be confirmed; abs page was rate-limited).

## Checks run today (script `verify_preprint_checks_20260905.py`, all pass)
Prop 4.2 proof steps (30+ digits, ω=0.3 and 1/2); endpoint lemma (delta mass → −π; f=1 agrees with Q₀+C_{1/2} to 7.5e−8, uncorrected off by 0.2402); full §6.3 chain incl. ∫|h| = 0.012293050401142319559; item 0.6; row-integral monotonicity in b; β*, d_tail, both Schur losses to 17 digits; block-Schur constants; Laplace of explicit impulse vs K (4e−11, quadrature-limited); Mellin of x^{-1/2}κ(−log x) vs Γ_∞ ratio. The discretised Volterra-identity check in the script is unreliable (kernel singularity on the anti-diagonal) — the identities were verified by hand instead.

## Still to do before/after deposit
- Fill ORCID; after Zenodo mints the DOI, uncomment `doi` in CITATION.cff and the badge in README.
- Items 0.1, 0.2, 0.5 (Inv 12 §4, §8.4; Inv 14 §7/§9) must be fixed before any code/write-up release.
- Parts A–D of the checklist remain open; C1 (human confirmation against Suzuki's PDF) is the highest-risk item.
- Local TeX note: compiled with OT1 Computer Modern (no lmodern/cm-super in the container); `\S` and `\thanks` avoided because they pull bitmap TS1 fonts there — harmless on a full TeX Live.
