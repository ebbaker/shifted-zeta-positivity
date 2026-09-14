# Review of version 0.3 on finite-horizon-weil

Reviewed branch: `finite-horizon-weil`.

Reviewed head: [`6a876260e828c1b3e029811ca5c0b5e4dfc2b67a`](https://github.com/ebbaker/shifted-zeta-positivity/tree/6a876260e828c1b3e029811ca5c0b5e4dfc2b67a).

Comparison baseline: `aa40ff897179e818152823e9804f085cb8cff613`, reviewed previously. The intervening commits are `7fd3587` (v0.3 revision and reorganization) and `6a87626` (large-file separation).

Scope: manuscript, source changes, small saved records, references, and repository documentation. No numerical construction, certificate replay, eigensolver, enclosure sweep, or diagnostic numerical test was run. No removed matrix archive was recreated or restored. The numerical checks reported by the project are taken as the existing verification record. No repository files were edited.

## Assessment

The substantive revision is useful. It replaces deliberately conservative targets by two-sided enclosures, gives a seven-horizon profile, distinguishes the two reflection sectors, and makes the continuation proof considerably more explicit. The upper-bound argument is mathematically appropriate: a nonzero retained polynomial vector gives a Rayleigh upper bound once the profile error is added. Separation of the even upper bound from the odd lower bound establishes which sector contains the spectral infimum. The manuscript appropriately leaves simplicity of the ground state as a diagnostic rather than a certified theorem.

I found no new structural error in those finite-horizon arguments on this reading. However, I recommend correcting the table's directed rounding and narrowing the claims about asymptotic decay and a practical horizon ceiling before circulation. There is also a local error in the new Laplace-line lemma's proof and a small remaining packaging defect. None of these findings calls for another numerical rebuild.

## 1. Table 3 does not preserve its claimed directions of enclosure

**Concrete reporting error.** See [the table generator](https://github.com/ebbaker/shifted-zeta-positivity/blob/6a876260e828c1b3e029811ca5c0b5e4dfc2b67a/papers/weil-depth/numerics/make_tables.py#L80-L93) and [the generated table](https://github.com/ebbaker/shifted-zeta-positivity/blob/6a876260e828c1b3e029811ca5c0b5e4dfc2b67a/papers/weil-depth/manuscript/tables_certificate.tex#L1-L17).

The caption describes the displayed tail floor as an outward lower value and the displayed error as an outward upper value. But `plain()` rounds to nearest, while `sci()` defaults to rounding downward and is used for both the model error and the maximum matrix radius.

The saved records already demonstrate the problem without recomputation:

| Quantity at `log(7)` | Saved record | Display in Table 3 | Problem |
|---|---:|---:|---|
| Tail lower value | `0.60748624181467145668...` | `0.6075` | Display is larger, so it is not an outward lower value |
| Schur error | `3.73676416585199878669...e-37` | `3.73e-37` | Display is smaller, so it is not an outward upper value |
| Maximum matrix radius | `4.6679914633485587446...e-295` | `4.6e-295` | Display underreports the radius |

The stored values are in [enclosure.json](https://github.com/ebbaker/shifted-zeta-positivity/blob/6a876260e828c1b3e029811ca5c0b5e4dfc2b67a/papers/weil-depth/numerics/output/log7_N128/enclosure.json) and [central_certificate.json](https://github.com/ebbaker/shifted-zeta-positivity/blob/6a876260e828c1b3e029811ca5c0b5e4dfc2b67a/papers/weil-depth/numerics/output/log7_N128/central_certificate.json#L16-L17).

**Correction:** round lower endpoints downward and error/radius upper endpoints upward. At the displayed precision, safe replacements for this row are `0.6074`, `3.74e-37`, and `4.7e-295`. Alternatively, label every such column explicitly as an approximate summary and direct readers to the records for the actual certified endpoints.

The formatting functions also discard the radius of printed Arb strings before rounding. For reliable general use, obtain the required endpoint from the complete enclosure before formatting. The issue identified here is in presentation; the sign-test code uses the stored ball quantities rather than the shortened table entries.

## 2. The finite profile does not prove super-exponential decay

**Scope of the conclusion needs correction.** The [abstract](https://github.com/ebbaker/shifted-zeta-positivity/blob/6a876260e828c1b3e029811ca5c0b5e4dfc2b67a/papers/weil-depth/manuscript/finite_horizon_weil.tex#L59-L71), [introduction](https://github.com/ebbaker/shifted-zeta-positivity/blob/6a876260e828c1b3e029811ca5c0b5e4dfc2b67a/papers/weil-depth/manuscript/finite_horizon_weil.tex#L152-L162), and the discussion after the diagonal proposition describe the certified minimum or shift intervals as decaying super-exponentially with the horizon.

The seven enclosures establish very small spectral infima and an increasing observed logarithmic decay rate across the sampled horizons. They do not establish an asymptotic law as `L` tends to infinity. This distinction matters because positivity at unbounded horizons is precisely what remains open.

The cited preprint also distinguishes these logical statuses: Zhu labels the fitted Landau–Widom law as Conjecture 12.1 and the qualitative large-window upper bound as conditional on RH. Its empirical fit is not an unconditional asymptotic theorem that can be imported into the present result. See [Zhu v2, Sections 12–13](https://arxiv.org/html/2608.24827v2).

**Suggested abstract replacement:**

> At every certified horizon the spectral infimum lies in the even reflection sector. Across the sampled horizons, the two-sided enclosures exhibit a rapidly increasing logarithmic decay rate, consistent with the empirical Landau–Widom picture.

In the body, retain the stated finite-difference slopes as observations and explicitly say that no decay law at unbounded depth has been proved. Apply the same qualification to the shift intervals.

## 3. The estimated horizon near 2.7 is not a proved ceiling

**Separate resource projections from mathematical limitations.** The abstract says that the scalar tail bound cannot reach much beyond `2.7`, and [Section 7.2](https://github.com/ebbaker/shifted-zeta-positivity/blob/6a876260e828c1b3e029811ca5c0b5e4dfc2b67a/papers/weil-depth/manuscript/finite_horizon_weil.tex#L1142-L1167) concludes that the method stops around `log(13)`–`log(16)`.

The stated tail formula does not prove such a finite ceiling. At any fixed `0<L<3`, choose a valid finite profile degree `M`, so that `K_L` and the arithmetic sum are finite. Then

\[
a_{N,L}=H_N-\gamma-\log(\pi L)
-\frac{K_LL}{2\sqrt{N(N+1)}}-\Sigma_L
\longrightarrow+\infty\qquad(N\to\infty).
\]

This does not prove that the complete Schur test succeeds: the retained head, coupling, approximation error, and numerical cost still matter. It does show that the scalar tail floor alone has no hard obstruction at `L=2.7`.

The arithmetic loss explains severe growth of the dimension needed to maintain a chosen tail floor. It does not, without additional analysis, determine the computational limit on every machine or every implementation. Similarly, maintaining a tail floor near `0.6` does not establish that it suffices for an uncomputed horizon, where the required coupling bound may differ.

**Suggested replacement:**

> Extrapolating the present scalar-tail estimates suggests rapidly increasing computational cost beyond the certified range. Horizons near log(13)–log(16) may be demanding for the present implementation. These are resource projections, not impossibility bounds or predictions of successful certification.

The abstract should say that the paper estimates the increasing cost of extending the method. Retain `L<3` as the domain of the particular proved profile remainder. Also qualify the projected `10^{-34}` decay factor per additional unit of horizon as a local extrapolation.

## 4. Correct one denominator bound in the expanded Laplace-line proof

**Local analytic error with an immediate repair.** At [source lines 454–457](https://github.com/ebbaker/shifted-zeta-positivity/blob/6a876260e828c1b3e029811ca5c0b5e4dfc2b67a/papers/weil-depth/manuscript/finite_horizon_weil.tex#L454-L457), the proof asserts

\[
|p\pm\alpha|,\ |p\pm\beta|\ge\eta-\tfrac12.
\]

This is false for `p-beta`. For example, at `s=1/2`, `beta=1` and `tau=0`, its modulus is `eta-1`.

Only `p-alpha` and `p+beta` occur in the denominator of the displayed rational factor. Those do satisfy the needed positive lower bound. Replace the sentence by

> The denominator factors satisfy \(|p-\alpha|\ge\eta-\tfrac12\) and \(|p+\beta|\ge\eta+\tfrac12\), uniformly on the line.

If all four signs are to be mentioned, use the weaker valid common bound `eta-1>0`. The conclusion of the lemma survives this correction.

The expanded energy proof otherwise usefully states the weighted realization, positive-shift differentiability, causal restriction, smoothing, symmetric-form identity, and zero-shift limit. Its separate treatment of the endpoint `s=1/2` avoids using a singular imaginary-axis digamma representation there.

## 5. Finish the small-file documentation for the external archives

The intentional removal of the large matrix archives is not a defect. The repository retains the relevant source, parameter records, pivot records, and hashes. No restoration or reconstruction is needed for this review.

Two small packaging issues remain:

- The current [checksum manifest](https://github.com/ebbaker/shifted-zeta-positivity/blob/6a876260e828c1b3e029811ca5c0b5e4dfc2b67a/papers/weil-depth/SHA256SUMS.txt#L1-L19) still lists three unversioned macOS metadata files. All **70 present entries match their recorded hashes**; only those three entries are missing. Generate the release manifest from the intended tracked deliverables, excluding machine metadata. The earlier missing-log issue has been removed from the current manifest.
- The [README](https://github.com/ebbaker/shifted-zeta-positivity/blob/6a876260e828c1b3e029811ca5c0b5e4dfc2b67a/papers/weil-depth/README.md#L6-L22) directs readers to `numerics-archives/README.md`, but that small guide is itself absent from the checkout because the directory is excluded. Keep the guide in a tracked location, such as `ARCHIVES.md`, while leaving the data outside git. Document the exact expected layout, including `WEIL_ARCHIVES/output/log7_N128/central_matrices.json.gz`, and the method for obtaining the saved files if they are to be supplied to reviewers.

The wording that a rebuild on “any machine” reproduces the content hash should also be limited to the tested software environments and fixed parameters. A content hash is a useful identity check; it does not establish universal bit-for-bit portability across different Arb/FLINT versions or arithmetic implementations.

## Additional clarifications

**Classical comparison.** The new historical section should preserve the hypotheses of the cited classical results. Connes–Consani's printed Theorem 1 includes Fourier-vanishing conditions in addition to the support restriction; their introduction states the relevant vanishing conditions in its description of Yoshida's result as well. Cite those precise formulations, or explain the passage to the unrestricted full form including the pole term, before describing their theorem as the same positivity statement as the present `log(2)` row. This is a bibliographic precision issue, not an objection to the new row. See [Connes–Consani, introduction and Theorem 1](https://alainconnes.org/wp-content/uploads/Selecta.pdf).

**Comparison of lower bounds.** The inference from the `log(5)` row to a lower bound at total length `1.6` is valid by compression. The closeness of two lower bounds obtained by different methods is compatible evidence, but their agreement is not a numerical cross-check of the operators or implementations: lower bounds are not estimates with two-sided error bars, and the initial horizons differ. Use “consistent with the reported enclosure” rather than “cross-check between the programs.”

**Nested Schur paragraph.** The earlier exact/model distinction remains implicit in Appendix B. The printed blocks belong to `Q_0`, whereas the constructed Grams belong to `Q_tilde`; a future certificate using the nested test must carry profile and ball errors into the head, buffer, and all coupling products. One explicit sentence would close this exposition issue. The appendix is correctly excluded from the dependency chain of the current theorems.

**Editorial leftover.** Section 6 is still headed “Finite construction and the two certificates”; it now covers seven horizons. Rename it “Finite construction and the certificates.”

## Recommended disposition

Retain the seven-horizon two-sided theorem, the sector separation, the revised continuation constants, the expanded functional-analytic proof, and the separation of current files from historical drafts. Correct the bound formatting and local denominator statement; rephrase the growth and ceiling claims; finish the small-file archive documentation. These changes concern the interpretation and presentation of the existing work and do not require another numerical certification pass.

The review did not establish a new certificate or extend any shift interval. It assessed the changed arguments and their consistency with the committed records, respecting the instruction not to reproduce the large files or rerun the numerics.
