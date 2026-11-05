# MC11-E03 r1 — first-excited acquisition and three-orbital return

4 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6.1-sol (Codex), effort ultra**; MC11 chat0001, thread 01a1a8e5-1cb3-74b3-80a9-e4b99f6f4fab, turn 01a1a988-130d-7d12-a635-ee7f7a94ed96.

**E03 r1 complete: all five width goals met on the first 384-bit acquisition, with no subdivision refinement.** The validated input and exact common-path replay give \(L_2>0\), \(L_{\ge3}>0\), and \(\Delta_3>0\). The two spectral groups reinforce. The first excited level accounts for more than 99.99997573% of the gain. **E04 assessment remains pending.**

[Acquisition and replay record][record] · [Code and saved-data verifier][code] · [Sole progress register][progress] · [E04/model-change handoff][handoff]

## 1. Fixed task and numerical inputs

The [E02 return][e02note] isolated uncertainty in the five source moments
\[
A_j=a_j(4\pi)=\int_0^\infty
\frac{u^{2j}}{(2j)!}\,e^{u-X}(2X^2-3X)\,du,\qquad
X=4\pi e^{4u},\qquad j=1,\ldots,5.
\]
Only those moments were acquired. The source, physical heat time zero, full half-line, canonical unit-weight endpoint and common path \(w_1=1,w_{n\ge2}=s\in[0,1]\) are unchanged. The response is the real **unnormalized** \(D_3(s)\), with source orbitals and endpoint cancellation as accepted in E01.

The calculation still uses
\[
b_j=a_j(\pi),\quad H_j=\sum_{n\ge3}a_j(\pi n^2),\quad
h_j=A_j+H_j,\quad c_j(s)=b_j+s h_j.
\]
The compact reference \(c_j^*\), full-half-line ground moments \(b_j\), and newly acquired first-excited source moments \(A_j\) remain distinct. In E01 Note01 the letter \(A_j\) locally denoted a compact primitive integral; no data are relabeled between those definitions.

All consumed E02 and inherited input/code hashes matched. Key versions are:

| Input | SHA-256 |
| --- | --- |
| E02 exact spectral-split record | 2e33a57d09ae986343c3735fbad97c3a49c26a909b2f2b11f5b964c07de86d20 |
| E02 calculation | 4d0eff7733071967fe8af896889b75000522aefb5210501725ff8760166cb0da |
| E02/E03 continuation packet | f9f35d523e9f46372faf2b8203ed19c9e4bd5369370003f06dffab06bf757bc9 |
| Original validated RGD acquisition code | b4863a6840cd4d68b10fe993f3f4cdc5e66dd8b3d44903445b306a50c8879db4 |

The new record binds these, all inherited E02 inputs, the new code hash, actual software versions and every acquired segment. Its SHA-256 is **cbe82f4e927c1fdd25dd6a579e5c027cbee69217b8bcb5dc4e07f185ca5ac0d7**. Hashes identify versions; the interval arithmetic supplies the sign evidence.

## 2. Validated acquisition on the fixed compact cover

The existing python-flint/FLINT integration framework was adapted from primitive moments to the actual source moments. Its entire callback is
\[
z\longmapsto\frac{z^{2j}}{(2j)!}\exp(z-X)(2X^2-3X),
\qquad X=(4\pi)e^{4z}.
\]
There is **no additional \(1/8\)**: that factor has already been incorporated in the displayed source density. Integer powers, polynomials and exponentials make the callback entire, so ignoring the callback's analytic flag is appropriate. The \(\pi\) enclosure and all nested-exponential rounding remain inside Arb/Acb arithmetic.

The fixed settings were Python 3.12.14, python-flint 0.9.0, FLINT 3.6.0, 384 bits, one arithmetic thread, relative and absolute tolerance \(2^{-320}\), degree limit 128, 5,000 evaluations per integration call, depth limit 20, heap enabled. The compact cover was
\[
[0,1/8],\ [1/8,1/4],\ [1/4,1/2],\ [1/2,1],\ [1,2].
\]
Thus five moments required 25 segment integrals. The callback count was **1,991**, and recorded acquisition time **0.022567542 seconds**, below the declared 180-second and 200,000-callback caps. One acquisition completed; the optional single midpoint subdivision refinement was not used. No precision change, other moment, energy group or determinant order was acquired.

Each segment was finite and its imaginary enclosure contained zero. The record retains real and imaginary dyadic balls and callback counts. The exact verifier checks that their real interval sum is contained in the saved compact-total ball. Display strings are rounded reading aids; neither those strings nor the requested tolerance replace the serialized radii.

## 3. Full \(n=2\) spatial exterior

The new integral needs a **source** tail, rather than reuse of a primitive tail with missing endpoint terms. For \(E=4\pi\), \(U=2\), \(X_U=Ee^{4U}\) and \(\lambda=4X_U-9>0\), positivity gives
\[
0<\phi_E(u)\le2E^2e^{9u-Ee^{4u}}.
\]
Writing \(u=U+v\) and using \(e^{4v}\ge1+4v\) yields
\[
\begin{aligned}
0<R_j&:=\int_U^\infty\frac{u^{2j}}{(2j)!}\phi_E(u)\,du\\
&\le
\frac{2E^2e^{9U-X_U}}{(2j)!}
\sum_{k=0}^{2j}\binom{2j}{k}
\frac{U^{2j-k}k!}{\lambda^{k+1}}=:B_j^{(2)}.
\end{aligned}
\]
The factor follows by dropping the negative \(-3X\) source term, retaining \(2X^2\), then integrating the polynomial times \(e^{-\lambda v}\). No truncated Green identity is invoked and no \(1/8\) belongs in this tail formula.

Arb encloses the positive expression \(B_j^{(2)}\) at 384 bits. Its readings run from about \(7.0441\times10^{-16264}\) at \(j=1\) to \(9.9391\times10^{-16268}\) at \(j=5\). The record retains the original dyadic balls, including their nonzero radii. For safe exact post-processing, every upper tail endpoint is rounded **upward** to the \(2^{-384}\) grid, giving the same payment \(2^{-384}\) in these five cases. The verifier checks containment before any propagation.

If the compact ball has exact endpoints \([\ell_j,u_j]\), the full source moment is enclosed by
\[
A_j\in[\ell_j,u_j+\overline B_j^{(2)}],
\]
where \(\overline B_j^{(2)}\) is that upward payment. The actual tail lies in \([0,\overline B_j^{(2)}]\). A positive lower endpoint of the **bound-expression ball** is not used as a lower bound on the actual tail.

The separate complete \(n\ge3\) Green majorant from E02 is retained unchanged. The new \(n=2\) source exterior does not replace, duplicate or omit that energy-group allowance.

## 4. Acquired full-half-line moments

The values below are approximate readings; the record contains exact interval endpoints. The half-widths include the compact enclosure and the upward spatial-tail payment and are rounded upward in this table.

| \(j\) | Approximate \(a_j(4\pi)\) | Full interval half-width less than | Requested half-width at most |
| --- | --- | --- | --- |
| 1 | \(8.212077023544616\times10^{-9}\) | \(6.346\times10^{-105}\) | \(8.8483\times10^{-15}\) |
| 2 | \(2.413814655797370\times10^{-12}\) | \(5.557\times10^{-106}\) | \(3.6456\times10^{-18}\) |
| 3 | \(5.736209739808966\times10^{-16}\) | \(3.044\times10^{-97}\) | \(1.5020\times10^{-21}\) |
| 4 | \(1.139624904152950\times10^{-19}\) | \(3.849\times10^{-99}\) | \(6.1887\times10^{-25}\) |
| 5 | \(1.938540412985706\times10^{-23}\) | \(3.029\times10^{-101}\) | \(2.5498\times10^{-28}\) |

Every full lower endpoint is positive and every goal is met. All five new boxes lie within E02's pre-existing analytical upper bounds. The chosen precision was fixed by the contract, not selected after observing a sign.

## 5. Replay along the same common filter path

The code loads E02's frozen polynomial record and reconstructs its five collected gradients and exact integrated \(K_j\) polynomials. It verifies equality with those frozen polynomials, then substitutes
\[
A_j\in\text{new acquired box},\qquad
H_j\in[0,V_j^{\rm E02}],\qquad
h_j=A_j+H_j
\]
throughout. The ground boxes, including their full-half-line exterior, are unchanged.

The exact formal identity
\[
\sum_{j=1}^5h_jK_j=D_3(b+h)-D_3(b)
\]
passes again. Reversing the signed \(h_2K_2\) contribution breaks it. The collected cubic endpoint interval overlaps the split-response interval, and their intersection is retained for \(\Delta_3\). This does not restore the groups in a different order.

The \(n\ge3\) contribution uses E02's slope-ratio bound and its complete infinite energy majorant, with the refined common \(K_j\) boxes. Its strict positivity is retained. The zero endpoint in its stored numerical interval is open by the analytical positivity argument, not a claim of zero contribution.

Conservative outward decimal bounds are:

| Quantity | Returned rigorous bound | Disposition |
| --- | --- | --- |
| \(L_2\) | \(2.22665020868\times10^{-33}<L_2<2.22665020869\times10^{-33}\) | Strictly positive |
| \(L_{\ge3}\) | \(0<L_{\ge3}<5.402\times10^{-40}\) | Strictly positive |
| \(\Delta_3\) | \(2.22665020\times10^{-33}<\Delta_3<2.22665075\times10^{-33}\) | Strictly positive |
| \(D_3(0)\) | \(1.66142398817\times10^{-28}<D_3(0)<1.66142398818\times10^{-28}\) | Strictly positive |
| \(\Delta_3/D_3(0)\) | \(1.34020588635\times10^{-5}<\Delta_3/D_3(0)<1.34020621148\times10^{-5}\) | Fractional increase |

The fractional comparison is licensed by the strict ground determinant lower bound. Its size is approximately 0.001340206 percent of the first-mode overlap. The uncertainty of this final net interval is now governed by the unmeasured higher group, not the acquired first-excited quadrature widths.

There is also a genuine whole-path sign check for the first excited level: enclosing \(G_j(c(s))\) for all \(0\le s\le1\), then combining the fixed acquired \(A_j\), gives
\[
2.2266193\times10^{-33}
<\chi_3(4\pi;s)<
2.2266811\times10^{-33},\qquad 0\le s\le1.
\]
This is not inferred from \(L_2>0\). With E02's whole-path \(n\ge3\) result, **every excited box level raises the three-orbital overlap throughout this filter path**, within the unchanged canonical source premises. At two orbitals E01 established the opposite direction.

The complete higher group satisfies
\[
0<\frac{L_{\ge3}}{\Delta_3}<2.427\times10^{-7},
\qquad
\frac{L_2}{\Delta_3}>0.9999997573.
\]
For example, the conservative upper tail and lower net bounds in the table already give the first inequality. This answers which spectral group accounts for the change at order three: the first excited level contributes more than 99.99997573% of the gain, and all higher levels reinforce it with the stated small allowance.

## 6. Saved-record verification and review status

The 113,111-byte record preserves the 25 segment enclosures, tail balls, upward payments, width comparisons, software/configuration metadata, input/code hashes, exact propagated intervals and **121 checks**. Standard-library verification of that serialized record reproduced the exact propagation and passed all checks without calling the integrator. The recorded exact replay time during acquisition was 0.022712625 seconds.

To verify from the repository root using ordinary Python:

    python3 papers/investigations-5/07_positive_theta_primitives/01_jensen/01_mellin_curvature/11_energy_filtered_theta_overlaps/numerics/mc11_e03_r1_first_excited_acquisition.py --repo . --verify papers/investigations-5/07_positive_theta_primitives/01_jensen/01_mellin_curvature/11_energy_filtered_theta_overlaps/numerics/MC11_E03_R1_FIRST_EXCITED_ACQUISITION_20261104.json

Acquisition is reproducible with the same script's output mode under Python with python-flint installed, using a fresh output path. The actual interpreter and versions are in the record. A new run must not overwrite the saved acquisition. Verification checks serialization, covers and propagation; it trusts the identified Arb quadrature and constant enclosures and does not formally verify FLINT.

The coordinator implemented/acquired the enclosures. One read-only Sol/ultra contributor checked the entire callback, source-tail proof and normalization. These are same-model author checks with inherited source premises. **This return has not received E04 assessment or independent specialist review.** The new numerical signs must be assessed under that existing task before B01 interprets transfer to other orders.

## 7. Scope and continuation

This is a fixed-order signed comparison using acquired first-excited moments and bounded spectral contributions, not a new positivity range or RH-equivalent criterion. The [result index][results] and [theta cluster][theta] locate inherited results; [avoid/01][a01], [joint estimates][a12] and [review provenance][a05] delimit the gain and evidence status.

The [collision screen][controls] still applies. Reweighted square spectra change the coefficient/cofactor payments and the preparations; the acquired canonical \(A_j\) and unchanged \(b,h\) path cannot be imported unchanged. Euler-factor sources do not retain this trace, and reflected/positive-primitive controls do not supply the unit-square source and its quantitative bounds. No uncomputed inequality failure for a control is asserted. A positive-time collision is not contradicted by this time-zero finite-order increase.

No growing-order, neighboring-shift, normalized-wedge or Mellin-curvature conclusion follows. The strengthened pointwise claim is scoped to this physical path and these two orders; see [scope warning][a07].

**Next: [E] MC11-E04 — Sol**, one-pass assessment of the finished E02/E03 return, with at most one local correction. The [handoff][handoff] and [frozen review input list][versions] specify the obligations. B01 remains after E04, unless assessment identifies a substantive structural premise change.

[record]: ../numerics/MC11_E03_R1_FIRST_EXCITED_ACQUISITION_20261104.json
[code]: ../numerics/mc11_e03_r1_first_excited_acquisition.py
[progress]: ../research-progress/01_ENERGY_FILTERED_THETA_OVERLAPS_RESEARCH_PROGRESS_20261104.md
[e02note]: 02_MC11_E02_R1_COMMON_PATH_SPECTRAL_SPLIT_20261104.md
[handoff]: ../research-progress/handoffs/03_MC11_E03_RETURN_AND_E04_MODEL_CONTINUATION_20261104.md
[versions]: ../research-progress/handoffs/03_MC11_E04_R1_INPUT_VERSIONS_20261104.json
[results]: ../../../../../../../result-summaries/README.md
[theta]: ../../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[avoid]: ../../../../../../../avoid/README.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[a01]: ../../../../../../../avoid/01_restating_the_target.md
[a05]: ../../../../../../../avoid/05_same_model_reviews_and_shared_premises.md
[a07]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
