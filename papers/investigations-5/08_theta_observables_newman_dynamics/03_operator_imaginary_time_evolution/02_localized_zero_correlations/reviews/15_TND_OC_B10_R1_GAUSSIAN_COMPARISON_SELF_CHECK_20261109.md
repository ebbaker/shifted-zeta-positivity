# B10 r1 Gaussian comparison: proof-author self-check

9 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex assistance, OC chat0009. Recorded current thread
settings: `gpt-6-astra / max`; per-turn backend configuration
unavailable in the public-history adapter. Same assistant as the proof;
no independent, different-model or specialist assessment.

**Disposition:** [Note19](../notes/19_TND_OC_B10_R1_GAUSSIAN_CONTRACTION_AND_MISSING_ESTIMATE_20261109.md) is retained at
**proved in-note, proof-author checked** for its elementary identities,
conditional error bounds and scoped lower bound. B10 r1 is complete at
the missing-input/decision boundary. No canonical joint value or gain
over the paid B06-style baseline was established.

| Check | Finding |
| --- | --- |
| Same full observable | Note19 (1)–(3) use the Gaussian height window, fixed B06 blur and Q². Compact-window constants are not silently reused on its enlarged support. Each connected estimate pays a second product of first intensities. |
| Observation convolution | The difference variance is 1/8 and each mark variance 1/16. The factors give \(c_G=32\sqrt2/51\), gap exponent \(4/(9\ell^2)\), and mark exponent \(8/17\). The unfolding Jacobian cancels in each observation integral. |
| Projection and center edges | The projection integrates over the whole observation plane. Note19 explicitly distinguishes this from data on Q². Its center integral is the finite erf difference, including both edges; midpoint dependence remains. |
| Label self term | The diagonal is \(W^2b_+b_-\), with \(\chi_R^2\) after truncation, not \(W^2b_+^2\). The two shifted mark squares give \(e^{-4/17-16y^2/(17\ell^2)}\). Multiplicity m retains m(m−1). |
| Common-center Fourier identity | The normalized density \(\rho_\ell\) has integral one and transforms to the required horizontal Gaussian. Conjugation gives a raw modulus square but does not change the self term or factorize the center mean. |
| Tails | Weight telescoping gives \(2c_GBb_R\). Frequency truncation gives \(c_GB^2\operatorname{erfc}(3\ell K/4)\) because the self term stays outside the truncated integral. The geometric bound uses \(j^2\ge j\) for integers j≥0. |
| Source and numerical errors | Every log-product error is estimated after integration, with bounds on exact contracted amplitudes. Source error is \(c_G(2Bd+d^2+e)\). The four \(1/400\) slots total \(1/100\); their satisfaction is not claimed. Arithmetic/radial approximations and the enlarged-domain anchor/log transfer remain explicit future costs. |
| Blur interpretation | The exact convolved test defines the target, so no blur error is discarded. If changed to the unsmoothed test, the displayed \(B^2/8\) allowance follows from a four-coordinate Laplacian bound of 4. It is not asserted small. |
| Small-value lower bound | On \(t\le1/(4M)\), the M positive remainder terms from M+1 through 2M sum to at least 1/8. Their disk area is \(\pi a^2(4M)^{-1/m}\). The resulting lower bound is for positive absolute errors in the local monomial class; no signed contracted or canonical lower bound follows. |
| Evidence and routing | The BGST statement is used only for an interface comparison. Generic Gaussian identities pass the controls. No new E packet is issued; conditional B10 r2 requires a named added source input. E09 is a separate optional compact-window evaluator. |

The single focused clarification was the local small-value-rate question.
There were two candidate routes, one analytical pass, no numerical
campaign, no manuscript change and no new root-summary claim. The
identities are useful bookkeeping but do not satisfy the canonical
acquisition gate. An external or separately commissioned assessment is
still absent.

See [controls12](../../../../../../result-summaries/12_collision_controls_and_screening.md),
[status06](../../../../../../avoid/06_status_stronger_than_the_evidence.md)
and [scope07](../../../../../../avoid/07_scoped_exclusions_read_as_universal.md).

