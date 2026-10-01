# Character channels: the winding phases are the Dirichlet family

26 September 2026. Prepared for Edward Baker by Claude (Anthropic). Model line: claude-fable-5-1 (Fable 5.1) per the runtime environment, session configured as claude-opus-5-5; the serving model may differ. Reasoning effort not exposed.

**Status: first session; one research note, one control program with records; nothing committed by the assistant.**

In the consolidated YM manuscript (`papers/susy-positivity/investigations/wilson-loewner/YM/`), winding a Mellin character packet $a$ times splits it into $a$ phase channels at the angles $2\pi j/a$; only the identity channel contributes to the prime terms of the Weil form for $\zeta$, and the other channels — carrying norm $(1-a^{-1})\|f\|^2$ — obstructed recentering and positivity. This investigation asks what those channels are.

**Answer** ([research note](notes/CHARACTER_CHANNELS_AND_THE_DIRICHLET_FAMILY_20260926.md)): in the Haar limit the winding operators and the phase multiplications satisfy the Bost–Connes relations, the limiting winding module is $L^2$ of the integral adeles $\mathbb{R}\times\hat{\mathbb{Z}}$ with a unitary Galois action of $\hat{\mathbb{Z}}^*$, and the $\chi$-isotypic combinations of the phase channels (Gauss sums) are the multiplicative twists whose winding limits are the prime terms of the explicit formula for $L(s,\chi)$: $\lim\langle M^\chi_R f, V_a M^\chi_R g\rangle = a^{-1/2}\overline{\chi(a)}\langle f,U_{\log a}g\rangle$. The norm the $\zeta$-realization discarded is the norm the nontrivial $L$-functions need; the natural target of the machinery is Weil positivity for the whole Dirichlet family, on which the profinite fiber forbidden by the manuscript's Theorem 6.1 is the natural coordinate. Two further exact statements: the interacting Yang–Mills state breaks the Galois symmetry down to complex conjugation and mixes $L$-function sectors of equal parity (proved, and confirmed numerically for the cubic characters mod 7); and the manuscript's two parities of archimedean insertion are the archimedean factors $\Gamma_{\mathbb R}(s)$, $\Gamma_{\mathbb R}(s+1)$ of even and odd characters, while the class-sector insertion itself diverges on character packets with an exactly computed finite part containing the conductor $-\log q$.

**What is not gained:** any positivity mechanism. The family form on the module is Weil's explicit formula reorganized, with assigned archimedean operators.

Contents:

- [notes/CHARACTER_CHANNELS_AND_THE_DIRICHLET_FAMILY_20260926.md](notes/CHARACTER_CHANNELS_AND_THE_DIRICHLET_FAMILY_20260926.md) — the research note (statements classified as proof / known / floating / heuristic; assessment; next steps).
- [numerics/](numerics/README.md) — `check_character_channels_family.py` (three parts: character limits in the class sector for Haar and an interacting marginal; the class-sector insertion on character packets; the family Weil form on the manuscript's probe against the zeros of $L(s,\chi)$ for six real primitive characters) with records.

Next steps, in the note's Section 7: a certifiable family version of the arithmetic-storage prime-weight rigidity (does window positivity pin the sign $\chi(2)$?), and the twisted-theta derivation of the character archimedean factor on the module.
