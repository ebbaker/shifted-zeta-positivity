# Shifted-zeta criteria, the \(\omega\)-string and defect depth

15 October 2026. Claude Fable 5.1 (`claude-fable-5-1`), Claude Cowork.

## Summary

**Paper 1, the margin.** \(\Psi_\omega(t)=(\xi'/\xi)(\tfrac12+\omega)\,t
+(\xi'/\xi)'(\tfrac12+\omega)+R_\omega(t)\) with
\(|R_\omega|\le A_*(\omega)e^{-(\omega-\vartheta)t}\) when
\(\vartheta\le\omega\); the slope is at least \((2+\gamma_0-\log4\pi)\omega\)
and the onset satisfies \(t_0\le0.0129\,\omega\). The critical-shift
dichotomy: \(\vartheta\le\omega\) gives \(\Psi_\omega=\)slope\(\cdot t+O(1)\),
\(\omega<\vartheta\) gives two-sided exponential oscillation, and
RH \(\iff\int\Psi^-<\infty\). Dirichlet \(L\)-functions are blind to real
(Siegel) zeros in this criterion.

**Paper 2, the \(\omega\)-string.** For \(\omega\ge\tfrac12\),
unconditionally, \(q_\omega\) is Stieltjes with an absolutely continuous
measure (Poisson-smoothed zeros); the margin identity
\((\xi'/\xi)(\tfrac12+\omega)=\pi\rho_\omega(0)\); bulk and UV laws;
RH \(\iff q_\omega\) is Stieltjes for all \(\omega>0\); degeneration onto
Kotani's string.

**Paper 3, defect depth.** Compactification and index theorems
(thm:compactification, thm:cfindex, rank-one and rank-two), the depth law
\(n_\varepsilon/\log(1/\varepsilon)\to1/(2g)\), and the envelope law
\(\eta t=2\log\tau+\log\log\tau+\log(S_\omega/\eta)+o(1)\) for how an
off-line zero becomes detectable.

## Status

"Proved in-paper" throughout, with no human review. Paper 1's phase
transition and Siegel-zero proofs are flagged for an independent check.
Paper 2's Theorems 1.3, 1.4 and 1.6(iii) rest on Kasahara, source-verified
against the original paper. Paper 3's high-height law is supported by
numerics only, and 17 `%% VERIFY` bibliography markers remain.

## Caveats

Paper 1's earlier "universal threshold u* ≈ 0.3748/ω" was withdrawn as
"vacuous as stated" (27 August; derivation record §4 and STATUS). These
papers give criteria and conditional endpoint descriptions; they do not
establish the positive family the program needs, and uniform detection of
every possible defect remains open (top-level README).

## Reusable for

The quantitative time-domain criterion and its margin constants; the
string family as the inverse-spectral object behind every later shifted
form; the defect envelope as a model for what a hypothetical off-line zero
would do to a finite certificate.

## Where

- [Program guide](../papers/shifted-zeta/README.md).
- Paper 1: [`psi_omega_concise.tex`](../papers/shifted-zeta/psi-omega-margin/psi_omega_concise.tex) (thm:asym, cor:margin, thm:threshold, thm:transition, cor:boundedCharacterization, thm:L1), [`psi_omega_margin.tex`](../papers/shifted-zeta/psi-omega-margin/psi_omega_margin.tex) (prop:siegel), [derivation and verification](../papers/shifted-zeta/psi-omega-margin/supplementary/DERIVATION_AND_VERIFICATION.md).
- Paper 2: [`omega_string.tex`](../papers/shifted-zeta/omega-string/omega_string.tex) §1.2; [STATUS](../papers/shifted-zeta/omega-string/STATUS.md).
- Paper 3: [`defect_depth.tex`](../papers/shifted-zeta/defect-depth/defect_depth.tex); [STATUS](../papers/shifted-zeta/defect-depth/STATUS.md).
- Cross-citation rule (cite statements by name, not number): [`papers/README.md`](../papers/README.md).
