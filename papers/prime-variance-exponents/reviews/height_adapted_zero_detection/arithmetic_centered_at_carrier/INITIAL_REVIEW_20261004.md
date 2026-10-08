# Review of the carrier centered arithmetic program

4 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration. The exact serving variant and
configured reasoning effort are not exposed and are not inferred.
This is parallel same-model internal analysis and cross-review, not
independent specialist refereeing or formal verification.

The arithmetic recommendation in the
[prioritized assessment](../../../notes/height_adapted_zero_detection/PRIORITIZED_ASSESSMENT_20261004.md)
is sound. No fatal error was found in its carrier factorization, multiplier,
or conditional cutoff calculations. Its resource warnings correctly
separate optional deletions from necessary detector costs. The main
qualification is that later Gaussian notes already complete parts of the
recommended work. The new investigation should build on those results.

## Assessment findings

| Issue | Review conclusion | Consequence for the new folder |
| --- | --- | --- |
| Carrier factorization in equations 6 and 7 | The shell carrier phases cancel and the normalized amplitude coefficients are uniformly bounded. Physical lattice derivatives still grow with height. | Use centered amplitude norms for the spectral tail and the saved physical Vaughan error for the comparison. |
| Existing arithmetic work | The height-uniform Vaughan note already gives effective full-\(\Lambda\) comparison and feasible cutoffs. The direct Gaussian note already gives a different finite centered-frequency target. | Complete the cofactor spectrum for the original scalar and explain its distinction from the Gaussian criterion. |
| Prime-only spectral source | The earlier finite cross-spectrum uses \(\theta-x\) and prime coefficients. | Replace it by \(\psi-x\) and full \(\Lambda\); do not inherit an unaffordable prime-power deletion. |
| Zeta pole | Removability alone does not prove a uniform bound near the displaced pole. | Prove centered decay for \(B_t'\) as well as \(B_t\), and retain \(W_t(0)=c_tK(1-it)\). |
| Density frequency shift | After centering, its denominator is \(t+\nu\). | Use translated Plancherel, rather than the invalid shortcut \(2/|\nu|\). |
| Complex scalar | Both arithmetic factors have the same carrier twist and the prefactor is \(e^{it\log H}\). | Keep the full complex product and both halves of the integral. There is no inherited real one-sided criterion. |
| Density cancellation | Its remainder depends on the physical seventh derivative. | Extend the exact cancellation with an effective \(T^7H^{-8}\) budget. |

The common-sector deduction, the stated finite-cluster use of the
Turan–Nazarov inequality, the polynomial remote-tail bookkeeping, and
the integer Hardy-dictionary projection calculation were also checked
at the level of their displayed algebra and stated hypotheses. Those
checks found no reason to reverse the recommended program ordering.
They are not a proof of the full inverse Gaussian construction or an
independent audit of every inherited transform theorem.

The cited Turan–Nazarov version was checked against the printed
[Bownik–Speegle PDF, Theorem 2.1](https://pages.uoregon.edu/mbownik/papers/51.pdf).
The source supports the interval-location loss in the assessment; its
absolute constant is not evaluated there. The assessment correctly
charges non-cluster zeros separately.

The quoted classical comparison inputs were checked against
[Bellotti–Trudgian–Yang, version 1, Theorem 1 and the introduction](https://arxiv.org/html/2603.21490v1)
and the
[Platt–Trudgian abstract](https://arxiv.org/abs/2004.09765).
Their stated constants and the verified \(3\cdot10^{12}\) benchmark
agree with the assessment. This was a source check, not a claim that
those inputs are the latest possible results. No stronger thesis input
or external novelty claim was adopted.

## Opening reduction findings

The [opening note](../../../notes/height_adapted_zero_detection/arithmetic_centered_at_carrier/INITIAL_REDUCTION_20261004.md)
now supplies the exact full-\(\Lambda\) correlation and complete
spectral-tail bound. Parallel calculations separately checked the
physical density calculation, centered Mellin inversion, and translated
mean-square estimate.

The continuum coefficient is \(D_t'(1)=c_tK(1-it)/q\). Its cancellation
has an explicit negative-sign remainder, rather than an assumed
negligible density. Product differentiation of the primitive divided by
\(u\) gives \(\|D^8f_t\|_{\rm TV}<2^{75}T^7\). With the exact
order-eight Poisson constant this gives
\(|R_t|<2^{54}T^7H^{-8}\), hence \(|R_t|<2^{-32}r\) at the
saved cutoff. No extra cutoff restriction is needed.

The pole proof uses the preparation zero and uniform seventh-order
Fourier decay of the logarithmically weighted amplitude. The continued
value is the original continuum moment. Arithmetic endpoints are dealt
with by physical support before truncating the integral, so no terminal
atom cancellation is assumed for a finite frequency interval.

The spectral tail uses coefficient-phase-insensitive finite-polynomial
mean squares and the full-line norm of the density transform. It pays
for both frequency signs and for any omitted neighborhood of the
displaced pole. Its constant is independent of height; its displayed
logarithmic height factor remains. The constant has not yet been
numerically evaluated.

## Verification status and limits

The [numerical guide](../../../numerics/height_adapted_zero_detection/arithmetic_centered_at_carrier/README.md)
and retained record identify the exact finite arithmetic checks,
rational density budgets, and floating phase controls. Deliberately
changing a cutoff, dropping prime powers, omitting the carrier prefactor,
or conjugating a factor must fail those controls.

The replay passed 1,792 exact Vaughan coefficient identities, 76 complex
weighted cofactor comparisons, 76 exact density comparisons, nine rational
budget checks, and 21 floating phase samples. All five negative controls
changed the corresponding diagnostic. An additional read-only review of
the opening note found no blocking equation error; its guard-count
hypothesis and spectral-constant wording were clarified before delivery.

These are synthetic diagnostics of identities and conventions. They do
not certify the actual prepared-kernel variation norms, Mellin inversion,
the analytic tail, or any central arithmetic saving. The note contains
the analytical all-parameter argument; the checker is not a proof
assistant. No zero-free result follows without the open signed central
estimate and the existing detector's full coverage hypotheses.

The appropriate next task is a usable numerical bound for the spectral
constant, followed by one signed estimate on complete dyadic blocks.
No manuscript, historical snapshot, commit, or unrelated staged change
was altered for this investigation.
