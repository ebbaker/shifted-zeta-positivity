# Internal verification pass on the first notes of 18 and 19

**Subsequent correction, 13 October 2026.** Prepared for Edward Baker with
LLM assistance by `gpt-6-astra` (Codex), effort **ultra**. This is the
historical internal verification record. Its numerical “Lambda collision
times” mean tracked branch times, with \(k=0\) denoted \(T_0\); no
global equality is certified. The formal expansion is for that branch.
The isolated-pair witness criterion remains valid, but the raw negative
margin tends to zero near collision. The [corrected 19 note](../../19_euler_factor_controls/notes/1_EXACT_FLOW_WITNESSES_AND_ASYMPTOTICS_20261013.md)
and [current allocation](../README.md) supersede broader readings of the
earlier verification summary below. Original evidence is retained.

13 October 2026. Prepared for Edward Baker with LLM assistance.
Model: Claude Opus 5.5 (configured identifier `claude-opus-5-5`; the serving
model may differ), Claude Cowork, reasoning effort **max**. The pass was run
by a separate Claude Opus 5.5 subagent that wrote its own mpmath code
(20–30 digits; scripts not retained). It is internal cross-checking, not
independent specialist validation.

**Scope.** [18, Note 1](../notes/1_CUSP_FORMULA_HECKE_AND_CONTROLS_20261013.md),
[19, Note 1](../../19_euler_factor_controls/notes/1_EXACT_FLOW_WITNESSES_AND_ASYMPTOTICS_20261013.md),
both program notes and the
[recommendation note](../../CLOSE_AND_MERGE_RECOMMENDATIONS_CLAUDE_20261013.md).

## Confirmed

| Claim | Result |
| --- | --- |
| Pair forms (1.2) of \(\mathscr L_0,\mathscr L_1\) | agree at \((0.05,10)\) to \(10^{-24}\) |
| Theorem 1 (cusp formula), four \((r,\kappa)\) including complex \(\kappa\) | relative error at most \(3\cdot10^{-25}\); proof steps and factor \(1/512\) checked |
| Annihilation of \(y^{\pm w},y^{\pm(1-w)}\) by \(\mathcal D(-\kappa,\partial_r)\) | exact |
| Theorem 2 at \((0.05,8)\), via Gauss–Hermite in \(V\) | \(\mathscr L_0\): \(1.7\cdot10^{-21}\); \(\mathscr L_1\): \(3.7\cdot10^{-20}\) |
| Theorem 3: \(\Phi_e\) as the even-index sub-sum, (4.1), (4.2) at \((0.1,6)\) | to \(10^{-28}\); \(E^*\) Hecke relation at 2 to \(3\cdot10^{-30}\) |
| Proposition 4(a) at two controls; the Dirichlet representation of \(\Phi_{c,p}\) | to \(10^{-22}\) and \(10^{-39}\) |
| 19, Propositions 1 and 2 | flow at complex \(x\) to \(10^{-29}\); witness argument valid (order 1, Laguerre–Pólya class for \(t\ge\Lambda\)) |
| \(\Lambda\) collision times \((101,\tfrac12)\), \((41,\tfrac12)\), and the \(k=1\) pair of \((2,\tfrac12)\) | 0.1297814765623, 0.2001166724596, 3.0688700: as tabulated |
| \(S_2\) and the first-order expansion | \(S_2=0.023104993115418970789\); expansion and sign confirmed |
| Platt–Trudgian \(\Lambda\le0.2\) | Corollary 2 of arXiv:2004.09765; Bull. LMS 53 (2021) 792–797 |

## Corrections made after the pass

1. **Error, now fixed.** 18 had said that the first Whittaker mode carries
   \(\mathscr L_0\) to within 20% for \(x\le60\). The pass found mode-1
   shares of 0.723 at \(x=54\) and 0.704 at \(x=56\); a rerun confirmed
   1.369 at \(x=46\) and 0.723 at \(x=54\). The note now says within 13%
   at the tested \(x\le42\), and the record includes \(x=46\) and \(x=54\).
2. 18, Theorem 3: \(\mathcal T\) is the transform of
   \(\sqrt2[\Phi_e\Phi_e+\Phi_o\Phi_o]\); the reason it holds at every
   Newman time is that (4.1) is a pointwise source identity (the
   Gaussian weight does not commute with translations; that is where the
   complex shifts come from).
3. 19: witnesses need not exist far below the collision. For
   \((p,c)=(2,0.05)\) at \(t=0\), \(\mathscr L_0>0\) on a fine grid of
   \((0,60]\) although an off-line zero exists. Statements now claim
   witnesses close to the collision and at the sampled times only.
4. 19: the tabulated \(\Lambda_{c,p}\) are collision times of the lowest
   pair. They are lower bounds; equality assumes every other pair
   collides earlier (checked for \(k=1,2\) only).
5. Both notes: "must use the Euler factor at every prime up to 41" was
   replaced by "must use some input that the control lacks", for example
   the Euler factor or direct low-height evaluation, which the existing
   proofs use.
6. Wording: "best published bound" became "best bound in the refereed
   literature"; the unrefereed \(\Lambda\le0.1787854\) claim is the one
   pinned in the Newman certificate audit. The recommendation note now
   marks the expansion as formal. Checker labels were renamed (E for
   exact, N for numerical) to avoid clashing with task labels A1–A4.
