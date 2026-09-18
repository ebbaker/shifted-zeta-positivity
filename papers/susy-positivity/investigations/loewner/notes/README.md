# Research notes

The [manuscript](../manuscript.pdf) (working draft 0.1, 17 September 2026)
consolidates the notes below into a self-contained report; the notes remain the
incremental record and carry details the manuscript summarizes. The
investigation's founding document is the
[Wilson-lines note of 17 September](../../wilson-lines/notes/LOEWNER_AND_THE_MARKOV_DECOMPOSITION_20260917.md),
inherited whole and not copied here: Section 4 of that note (the decomposition
$K_\omega=R_\omega\widetilde K_\omega$ with $\widetilde K_\omega$ completely
monotone) is the object, and its Section 6 was the first plan.

| Note | Status | Read it for |
|---|---|---|
| [MARKOV_PART_AND_REALIZATIONS_20260917.md](MARKOV_PART_AND_REALIZATIONS_20260917.md) | Opening note; current | The archimedean factor is Bessel additivity: $K^\Gamma_\omega\propto\mathbb E\,U^{p/2}$ with $U=Z_a/(Z_a+Z_{2\omega})\sim\mathrm{Beta}(\frac a2,\omega)$ for squared Bessel processes of dimensions $a=\frac12-\omega$ and $2\omega$, summing to $b=\frac12+\omega$ (Prop. 1.1). A Loewner chain cannot produce the prime comb in either variable identification --- far-field transport is a pure delay and translation invariance forces it everywhere (Prop. 2.1); the comb is the Hecke/Bost--Connes operator $\sum_n\widetilde c_n\mu_n$. The pole factor is **forced** by unimodularity (Prop. 3.1), which **withdraws** the inherited note's expectation that a realization would fail "at two numbers". Cleaner decomposition $K_\omega=B_b\widehat K_\omega$, one Blaschke factor at the pole of $\zeta$ times a completely monotone $\widehat K_\omega$, so $k_\omega=\widehat k_\omega-2\,\mathrm{EMA}_b[\widehat k_\omega]$ with $\widehat k_\omega\geq0$ (Prop. 3.2). At $\omega=\frac12$ the Markov part is exactly the Eisenstein scattering matrix of the modular surface and the comb weights are $\varphi(n)/n$. Ranked plan headed by registering the elementary assembly and measuring the contraction margin. Written by Claude Fable 5.1. |
| [CONTRACTION_MARGIN_FIRST_RUN_20260917.md](CONTRACTION_MARGIN_FIRST_RUN_20260917.md) | Current; plan item 1, first half done | The elementary assembly validated end to end at $L=\log3$: $V_{\omega,L}$ built in the sine basis from $k_\omega$ alone is a strict contraction with $\lambda_{\min}(D_{\omega,L})/2\omega\to m_L^{(N)}$ (agreement $0.1\%$ at $\omega=0.01$), so the transfer side and the form side agree at first order. The exact compressed defect expands as $2\omega Q_{0,L}-\omega^2(2Q_{0,L}^2+[Q_{0,L},A_{0,L}])+O(\omega^3)$ and the commutator vanishes on the minimizer, so the only first-order correction is $-\omega m_L^2$ (Prop. 2.1); the positive excess of the Galerkin computation is the sine-tail energy of $A_{0,L}f_N$, removed by a nested defect (Prop. 2.2, checked). Closed form for the first-order mass beyond the horizon from $\xi'/\xi$ alone, matching the assembled masses to five digits (Prop. 2.3). Numerical lessons (local coordinates for the spike, tanh--sinh step, the edge-atom sliver) and what remains of plan item 1. Written by Claude Fable 5.1. |

Reading order: the inherited Wilson-lines note first (its Section 4), then the
opening note, then the contraction-margin note. Claims conditional on the Riemann hypothesis are labelled where
they occur; proposals and readings are labelled as such.

See the [investigation index](../README.md).
