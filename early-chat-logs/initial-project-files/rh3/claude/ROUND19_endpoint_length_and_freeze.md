# ROUND 19 — Endpoint length collapse added, critical-member laws settled, numbering dispute arbitrated; paper at v5, ready for human review

**2026-08-28 (late night).** Response to the fifth referee pass (`Round19.md`), which found no
new flaw in the central chain Ψ_ω → q_ω → σ_ω → m_ω and declared further LLM auditing to have
sharply diminishing returns. Three items; the paper is **v5 (13 pp., compiles clean)** in
`claude/PAPER_omega_string.tex`. Next step per referee and per plan: human specialist review
(shortlist below, discussed with the user in-session).

## 1. The 3.4 vs 3.3 citation dispute — settled by compilation, citation UNCHANGED

The feedback insisted the critical-shift dichotomy is "Theorem 3.3" in the compiled concise
Paper 1 and that ROUND18's count was mistaken. Arbitrated by compiling a numbering skeleton
with the exact environment sequence of the current `claude/PAPER_psi_omega_concise.tex`
(amsart, remarks share the theorem counter): the `.aux` gives **thm:transition = 3.4**
(cor:margin 3.1, thm:threshold 3.2, the remark after it 3.3, cor:boundedCharacterization 3.5,
prop:sens 3.6). The feedback's count misses the numbered Remark 3.3. **[13, Thm 3.4] stands.**
**Resolution (user, same night): the reviewer had been given a different version of the
concise paper — both counts were right for their respective versions.** Policy going forward:
Paper 1 will see multiple revisions before submission (and publication order of the two papers
is undecided), so Paper 2's [13] citations are NOT chased through interim revisions; every
cite carries the theorem's name ("critical-shift dichotomy", "linear margin", etc.), and a
one-pass renumbering against the actually-submitted Paper 1 is a standing pre-submission
checklist item.

## 2. Critical-member bulk/UV laws (referee's refinement — verified and adopted)

For ω_c > 0 the referee is right that Theorems 1.3/1.4 extend to the critical member, and the
structural reason is clean: the closed form q_{ω_c}(−s) = (ξ′/ξ)(σ_c+√s)/√s is unchanged, and
(ξ′/ξ)(σ_c) > 0 still — an extremal pair contributes 0 to the paired Hadamard sum at real σ_c,
but its **mirror pair on Re s = 1−σ_c contributes 4ω_c/(4ω_c²+τ²) > 0** (the functional
equation forces mirrors; only at σ = ½ do pair and mirror coincide and the slope vanish). So
Kasahara's Thm 2 applies verbatim to the critical string: m_{ω_c}(x) ~ [(ξ′/ξ)(σ_c)]⁻²x at ∞
and ~ 4x/log²x at 0. Folded into Remark 6.1; Open Problem trimmed to what actually remains
(local structure at the embedded atoms; attained vs non-attained on the string side).

## 3. The endpoint length collapse (new Remark 6.3) — verified

Under RH, by oddness of ξ′/ξ about ½: q_ξ(−s) = (ξ′/ξ)(½+√s)/√s → (ξ′/ξ)′(½) = B(0) as s↓0,
so by Kreĭn–Kasahara ℓ = h(0) [Kas75, (9)]:

> **L_ω = ∞ for every ω > 0, while Kotani's limit string has finite length
> L_ξ = B(0) = Σ_γ γ⁻² = 0.0462099862…**

— the margin-scale constant of the companion paper ([13, Rem. 2.3]); equivalently
L_ξ = q_ξ(0⁻) = Σ_{τ>0} 2/τ² from Suzuki §9. Numerically verified this round:
q_ξ(−10⁻¹⁰) = 0.0462099862 (12-digit match to the central-difference (ξ′/ξ)′(½)); zero-sum
cross-check 0.0462126 (400 zeros + RvM tail, tail-limited). So the RH endpoint is **doubly
singular**: a.c. → pure point in spectral type, and infinite → finite length in geometry; in
the inextensible normalisation m_ξ ≡ ∞ on (B(0),∞), so Thm 1.6(iii) forces m_ω(x) → ∞ for
every x > B(0) — the (B(0)ω)⁻²-dense bulk is expelled past the finite length rather than
persisting. Added: Remark 6.3, a sentence in the intro after Theorem 1.6, the abstract clause,
and the upgraded physics-dictionary entry ("infinitely heavy bulk" now paired with the length
collapse). This also gives the margin constant B(0) a third role: margin curvature at ω = 0
(Paper 1), rate constant of the endpoint convergence (Thm 1.6(i) measurements), and now the
**length of Kotani's string**.

## 4. Acknowledgement softened

Adopted the referee's exact formulation: AI tools used extensively in exploration, numerical
verification, auditing, drafting; the author directed the research, reviewed arguments and
source checks, and takes responsibility. (Placeholder retained for final wording.)

## 5. Human-review shortlist and outreach status

**Outreach status (2026-08-28): the user has already sent the letter to Suzuki** (drafted in
PROGRESS §4b). If he responds, Paper 2 is the natural follow-up ("the inverse-spectral family
your §11 implicitly defines, computed"). Parallel options remain open pending his reply.

Shortlist, in natural order: **M. Suzuki** (Institute of Science Tokyo; contacted);
**S. Kotani** (Osaka, emeritus; the zeta string and its 4x/log²x law are his); one
canonical-systems/Kreĭn-string specialist for the Kasahara mechanics — **H. Woracek**
(TU Wien), **M. Langer** (Strathclyde), **R. Pruckner** (TU Wien), or **A. Kostenko** /
**G. Teschl** (Ljubljana/Vienna); **J. Lagarias** (Michigan; Herglotz positivity and de
Branges realisations of ζ); **J.-F. Burnol** (Lille; Kreĭn-string/scattering approaches to ζ,
Nyman–Beurling). Secondary/Weil-positivity side: E. Carneiro (ICTP), M. Milinovich
(Mississippi). **S. Gukov** (Caltech): not an inverse-spectral/analytic-NT specialist, but an
excellent router — the user knows him obliquely; mathematical physicist who will read the
physics dictionary natively, leads Caltech's mathematics+AI initiative (the AI-assisted
workflow is itself of interest), well positioned to forward the papers. Frame as "would you
or someone you'd point me to take a look", not a technical-refereeing request.

## State after v5 — the research program

All theorems and remarks in Paper 2 fully proved and sourced; both papers cross-consistent;
figure consistent; acknowledgements drafted. Remaining: author block (user); one-pass [13]
renumbering at submission (see §1); optional fig_string regeneration (numerics polish);
outreach responses. Open-problem pipeline for follow-on work: Dirichlet ω-strings and
conductor dependence; critical-member fine structure; effective endpoint rates; Gelfand–Levitan
high-resolution inversion; physics directions (scattering/AdS) only after human review.
