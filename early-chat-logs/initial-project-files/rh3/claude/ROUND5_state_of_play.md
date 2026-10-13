# Round 5: state of play

**2026-08-25.** Short orientation note. Read this first on returning; the detail is in the three
notes written today plus rounds 1–4.

## What is actually finished

- **The certified detector and its paper** (`PAPER_rh_detector.tex`). Unchanged and unaffected by
  anything today. Remaining work is engineering: interval arithmetic, `|S(u,χ)|` constants.
- **The pencil corollary** — `Λ(p) = inf{t : spec(X+tY) ⊂ ℝ}`. Modest, correct, provenance settled
  (the identity is Wilson's; the De Bruijn–Newman reading is the contribution).
- **The margin map and the edge law** (round 4) — mechanism found, reduced to one classical-analysis
  derivation via GORZ coefficient asymptotics. **This is the only item on the critical path.**

## What today added

Nothing positive. Today produced four corrections to claims made in the course of it, one small
theorem weaker than first advertised, and one provisional numerical fact. The map of what does not
work is better; there is no new result.

- **Prop. 3.1** (`NOTE_existence_loophole.md` §3) — true, but it is a general fact about
  semialgebraic descriptions, not a circularity blade.
- **`Σ|β_n| ≈ 2.114`** (`NOTE_n4_reformulation.md` §3.2) — the Dorigoni–Treilis sum over zeta zeros
  converges absolutely, which nobody states. **Provisional**: it depends on a residue formula
  transcribed from seminar slides, not from the printed paper. Verify before use.

## What is closed, and why

| route | closed by |
|---|---|
| ADHM / instanton size dictionary | circular; lossy; the deformation bounds sizes away from zero (rounds 1–2) |
| Undeformed YM, non-self-dual solutions, Vafa–Witten, 2D YM | round 2 §3 |
| Existence reframing *as an obstruction question* | no shape obstruction (Hermite 1856), no type obstruction (`NOTE_existence_loophole.md`) |
| N=4 SYM as a *lever* on the zeros | ξ cancels in the spectral decomposition; contour at the strip edge; Sarnak's ceiling is PNT (`NOTE_n4_sym_seam.md`) |

**The structural reason all of them fail** (`NOTE_existence_loophole.md` §6): geometry is a
*product-side* supplier — zeros, spacings, log-gas structure. The arithmetic lives on the
*coefficient* side, in the moments of `Φ`. Transport between the sides is cheap (measured: `~d/4.7`
decimals) but the geometry has nothing to carry across.

**And the sharpest version, for the physics routes specifically**: in a modular function the Fourier
modes are graded by instanton number, and the `ξ` factors appear **only in the constant term**. The
classical solutions are in the nonzero modes; the arithmetic is in the zero mode. They are
complementary sectors of the same object.

## Open, but not on the path

`NOTE_n4_sym_seam.md` §7 Column B: the ABJM/mirror-curve Laguerre–Pólya family (its `Λ_DN` is
undefined and nobody has called it Lee–Yang); Kenyon–Okounkov–Sheffield Harnack/dimer; MTV/Karp plus
the unwritten Nekrasov–Shatashvili translation; the N=4 reformulation itself
(`NOTE_n4_reformulation.md`). Each is real; none reaches RH. Two could be written up on their own
terms by someone who wants to.

## Method note

Six claims this session were asserted at a strength the evidence did not support: three caught by an
adversarial referee, two by the user, one by a control I ran before drawing the conclusion. The
standing corrective, which worked the one time it was applied: **for every claim of the form "X
cannot happen," run the control that would show X happening in a case where it does.** Second rule,
learned from the N=4 detour: **verify object type before building — lexical co-occurrence in a
literature search is not structural relatedness.** Third: **for hep-th material, read the printed
PDF; never build on a paraphrase of a display equation.**
