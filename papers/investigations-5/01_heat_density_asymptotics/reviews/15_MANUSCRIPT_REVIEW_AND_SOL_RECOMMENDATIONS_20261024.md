# Manuscript review and recommendations for the next Sol revision

24 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), actual effort max**,
verified from chat 0007's session metadata. Thread
`01a17067-eabc-7872-abc9-d9319b53bc41`.

**Disposition: retain the current working draft; make the correction and
additions below in a subsequent revision.** The existing manuscript
accurately limits its mathematical coverage to Note 30. Its omission of
Note 31 is intentional under the completed HDA-10-MI1 r1 specification,
not a failure of that production task. The most useful next addition is
Note 31's positive evolution and actual-covariance theorem. I found one
concrete notation inconsistency in the local-source bounds, and recommend
two improvements to self-contained exposition and navigation.

This is a **same-assistant analytical/editorial review**: the reviewer
also derived Notes 30--31. It is not a distinct-reviewer or specialist
audit, and does not fulfill HDA-20. I found no additional invalid displayed
identity or counterexample in this reading; that is not a correctness
certificate. No TeX, PDF, build record, numerical record, frozen handoff
or source proof was edited. The author will give Sol the implementation
request separately.

## 1. Exact version reviewed

- Source: the 14 TeX files under [manuscript/][manuscript], including
  `09_local_transfer.tex`, which is included by `08_finite_time.tex`.
- Reading copy: [54-page PDF][pdf], 710538 bytes, SHA-256
  `e8d0a288f15e3122c1acce461bcd95aef69a7743893044fcf9d06852a8d36f81`.
- All 14 source hashes agree with the [current build record][build].
  The successful build belongs to Sol's 24 October integration, documented
  in [Review 14][production]. I did not rebuild the unchanged manuscript.
- [Review input manifest][manifest] records the source, PDF, build,
  relevant notes/reviews and frozen prior handoff hashes. These identify
  the reviewed inputs; they do not validate the mathematics.
- Read all 14 TeX files and the current scope/provenance records. Re-read
  Note 31 and Review 13, and checked the source of the inner finite
  allowances in Note 16. The prior proof reviews remain shared inputs.
- Extracted the PDF text and visually inspected pages **1, 2, 10, 28,
  43, 47, 48, 51 and 54** at readable resolution. The sampled displays,
  tables, crosswalk and references are legible, without visible clipping
  or overlap. This turn did not repeat Review 14's all-page visual check.

The earlier [integration specification][old-spec] and [input manifest][old-inputs]
remain frozen as completed HDA-10-MI1 r1. A later revision should record
its own implementation scope and actual model/effort. Do not rewrite the
old request as though it had included Note 31.

## 2. Correction: disambiguate the local-source derivative constant

**Priority: required editorial correction.** In
[09_local_transfer.tex][local-source], lines **28, 44 and 58**, the
complete-source bound is still printed as `B_2`. The manuscript now calls
that source constant `B_2^Phi` in Lemma 3.1 / equation (3.1), whereas
Section 3.3 also defines a different, time-dependent composition budget
`B_m`, including `B_2`, in (3.22).

Replace these three source-bound occurrences by `B_2^{\Phi}`:

\[
B_2^{\Phi}h_s^2F_j/8,\qquad B_i\le B_2^{\Phi},\qquad
B_2^{\Phi}F_j/8.
\]

The local `B_i` remains the cell source bound. Do not globally replace
`B_2`: the composition budget and the centered moment `B_2(Y)` have
different legitimate meanings. This repairs a notation regression,
not the underlying interpolation estimate. The mismatch is visible
in Proposition 8.4 on PDF page 28 and its continuation on page 29.

## 3. Main addition: integrate Note 31 as an evolution theorem

**Priority: the principal recommended addition.** Introduce a new source
file, for example `13_positive_evolution.tex`, after
`12_full_gamma_saddle.tex` and before `14_scope_and_remaining_work.tex`.
Use a title such as **Positive evolution and actual covariance**.
The input is [Note 31][positive], with its [same-assistant assessment][positive-review].
This is a new revision beyond the original production scope.

### State the strength and derivative orders together

Retain the existing full saddle P_* and use its scales

\[
\mathcal L=\log(2+t+X),\quad N_*=1+X+t\mathcal L,\quad
e_*={t^{3/2}\over N_*^2},\quad
A_*=e_*\mathcal L^2,\quad d_*={t\over N_*^3}.
\]

Here `A_*` would collide with several amplitude symbols in the paper;
prefer a named error symbol such as `\mathfrak e_{\rm ev}` for
`e_* mathcal L^2`. Define the residual scale separately. A mere
statement that "all observables converge" would lose useful information.
Transcribe the PE6 table with its exact spatial derivative orders:

| Difference between H and P_* | Spatial order | Allowance |
| --- | --- | --- |
| U, W | <=4 | C e_* |
| R, averaged curvature C | <=2 | C e_* |
| J, actual Q, hence Delta Q | <=2 | C e_* mathcal L^2 |
| U_t, W_t, R_t, averaged C_t | <=2 | C e_* mathcal L^2 |
| Averaged forcing B and actual signed source S | <=2 | C e_* mathcal L^2 |

For all real x and t above one eventual T_*, the evolution allowance is
at most C t^-1/2. These are absolute errors on a fixed transverse strip
with a full buffer, fixed K and the unchanged q=epsilon_g^2. The model
equation corrections have the distinct allowance C d_*, at most
C/[t^2 log^3(2+t)]. Neither an error relative to every observable nor
numerically effective onset constants are asserted.

### Include the proof mechanisms, not just the table

The new section should contain the following dependency chain. Combining
short lemmas is fine, but none of these steps can be replaced by
differentiating the static big-O bound or by citing the small heat residual.

| Note 31 source | Manuscript content and reason |
| --- | --- |
| PE7--PE12 | Cauchy estimates on full disks of radius c/mathcal L, actual root displacement, bounded residues and analytic regular parts. Keep the residual correction in the model root velocity. |
| PE13--PE17 | Regulator-uniform regularized-pole comparison. Define V_m and Z_m through their smooth fractions at zeros; retain the e(1+abs(log e)) translation allowance and explain why no log(q) or positive regulator floor appears. |
| PE18--PE21 | Two regulator regimes, exact time coefficients and physical mass anchor. In the tail, the pole integral has an O(lambda) contribution, not only O(lambda^2). |
| PE22--PE27 | Direct time identities, weak current identity and differentiation of the exact weak density identity. Include every r_t and spatial/mixed regulator term, with the maximum kernel order four. |
| PE28--PE32 | Compare the actual signed gradient stress before taking absolute values; separately pay the difference of squared filtered gradients. This proves Q and Delta Q comparison without fitting a covariance. |
| PE33--PE39 | Exact residual-bearing current balance and potential/density equations, plus weak bounds on their residual corrections and the actual signed source. |
| PE40 | Differentiated inner overlap by comparison through H, preserving its coarser absolute rate and the sharper independent inner theorem. |
| PE41--PE44 | Separate compact-time outer theorem, including the flat-switch derivative estimate and the weaker time-error rate. |

In particular define, with D_P=|P|^2+q,

\[
Z_0={\mathcal E_*\overline P\over D_P},\qquad
\mathcal D_{\mathcal E_*}
={2q\Re((\mathcal E_*)_z\overline{P_z})\over\pi D_P^2}
-4\rho_P\Re {\mathcal E_*\overline P\over D_P}.
\]

The potential equation has `+2 Re(K*Z_0)`; the density equation has
`+(1/(2 pi)) Delta Re(K*Z_0)` as well as **both** curvature derivatives;
the current balance has `+K*D_E`. Keep the exact heat residual already
in equation (10.31). Its bound does not justify deleting these terms.
The weak form PE34 is needed to bound the correction without reciprocal
powers of a small regulator at individual peaks.

The compact-time theorem must state its own constants and threshold:
for each fixed T>=32, uniformly on [32,T] and X>=X_T, static errors
are O_T(X^-2), current/covariance errors O_T(log^2 X/X^2), time-dependent
errors O_T(log^2 X/X), and retained equation corrections O_T(X^-3),
with the derivative orders of PE6. Show

\[
|\beta'|\le C_T\beta\{1+\log_+^2(1/\beta)\},\qquad
\beta'=0\text{ where }\beta=0.
\]

Boundedness of beta' alone is insufficient: the physical time derivative
contains `-beta' x^2`. This is a substantive part of the extension across
64, not a routine compactness sentence.

### Update the surrounding scope only after the proof is present

| File | Revision action |
| --- | --- |
| `main.tex` | Include the new section; state positive all-height evolution at O(t^-1/2) and retain the unproved all-time assembly. Shorten the abstract by moving the full static joint formula to the theorem/roadmap. |
| `01_framework.tex` | Update source coverage to Note 31 and the opening result description; distinguish general exact heat identities from the later residual-bearing identities. |
| `07_explicit_clock.tex` | Link the differentiated overlap as well as static overlap; keep the inner O(L kappa^-7/6)=o(L/kappa) theorem and the absence of a clock potential/covariance assignment. |
| `08_finite_time.tex` | Update the final pointer from static-only exterior comparison to the now integrated evolution comparison; keep the finite-core and joining obligations. |
| `12_full_gamma_saddle.tex` | Keep its static theorem and residual proof intact. Replace its version-specific deferral paragraph with a pointer to the new section. The statement that static error alone cannot be differentiated remains true. |
| `14_scope_and_remaining_work.tex` | Add PE6, PE44 and differentiated-overlap rows, and make the remaining gap finite-core/joining, effective onsets and distinct review. Preserve fixed spatial filtering and all time/height quantifiers. |
| `05_appendices.tex` | Add Note 31's equation crosswalk and Review 13; revise current-version coverage and acknowledgment. Retain the distinction between analytical review and Sol production. |
| `06_references.tex`, reference catalog | Add Note 31 and the Cauchy derivative reference used in PE9; synchronize with the catalog. |
| Manuscript README and build record | Record the new implemented scope, current input/export hashes, actual production model/effort and checks. Retain the earlier integration as historical provenance. |

Search current narrative for `through Note 30`, `deferred`, `static
overlap` and `positive evolution` and assess each occurrence in context.
Do not mass-replace historical statements, Note 30's scope, or the frozen
HDA-10-MI1 files. HDA-18 remains Gated after this addition.

## 4. Make the inner finite transport bound self-contained

**Priority: recommended exposition improvement.** At
[07_explicit_clock.tex][inner-source], lines **159--167**, the manuscript
introduces `E_4=O(kappa^-9/4)` and refers to Note 16 AT3--AT4 for its
finite value. Equation (5.9) and the root-velocity allowance then use
the cancellation it controls. The reference is valid, but a reader
trying to evaluate the paper's finite allowance must leave the manuscript.

Add the existing finite expressions, preferably to Appendix A with a
short pointer from Section 5.3. This is consolidation of [Note 16][transport],
AT3--AT6, not new research. For clarity use e_mu here, not the local
refined-score symbol e without explanation:

\[
\bar v=A_2(0),\qquad
\nu_s={D_2(0)+D_0(0)\over Z_-}+\kappa e_\mu^2,
\]
\[
\begin{split}
E_4={}&\kappa^{-2}{D_4(0)+3D_0(0)\over Z_-}
+4e_\mu A_3(0)+6e_\mu^2A_2(0)+3e_\mu^4\\
&+3(\bar v+\kappa^{-1})\nu_s/\kappa.
\end{split}
\]

Also state the source-derived bounds
`|v'|<=2 mu B_3(0)+B_4(0)+v^2` and
`|m_3'|<=2 mu E_4+B_5(0)+4v B_3(0)`, with the existing positive
moment allowances and `L+e_mu`, `L-e_mu>0` replacements where needed.
This makes the finite root-velocity input reproducible on the page.
Retain the source gates; no numerical onset is supplied by adding formulas.

## 5. Put the model/domain guide near the beginning

**Priority: recommended reader-facing improvement.** The useful coverage
table is currently on pages 47--48, after the proofs. The reader has
already encountered a Gaussian, a mean clock, an explicit clock, a finite
source, a linear gamma pair and the full saddle. Add a compact guide
after the common protocol (or a short introduction pointer plus a table
there). It should distinguish the following objects:

| Model | Main use | Relation to the heat equation and covariance |
| --- | --- | --- |
| G_T | Negative endpoint | Exact heat field; actual Q_G computed from its potential |
| Explicit R_L,J_L | Sharper inner phase and transport | Exactly conservative observable pair; no assigned physical clock potential or actual covariance |
| H_f | Finite buffered core | Exact heat field; finite-source comparison and actual Q_f |
| P_lin | Explicit switch-layer and finite-phase analysis | Nonzero residual; historical restricted joint static range |
| P_* | Full-saddle positive endpoint and compact-time exterior | Nonzero residual; static comparison now, evolution after Note 31 is integrated |

Add theorem links and the corresponding domains rather than copying all
allowance formulas. A short notation key should distinguish L from
mathcal L, M=H(t,0) from M_0 and mathcal M, and inner alpha=mu'/mu from
gamma alpha=mathcal M'/mathcal M. The existing local explanations are
correct; a central key would reduce repeated backtracking. Rename the
dummy variable in `k(q)` to `k(v)` to avoid sharing q with epsilon_g^2.

Keep the detailed end coverage table as the complete contract, or move
it forward and leave only open work at the end. Avoid maintaining two
slightly different full rate tables. The title can remain: it does not
claim an all-time theorem. An optional later editing pass may move the
Vandermonde/pair-matrix material to an appendix, but this is not required
for the Note 31 revision. Do not reorder the linear gamma proof out of
the dependency path while the full saddle still invokes its collar lemma.

## 6. Mathematical distinctions to preserve

These are strengths of the current draft, not defects to be repaired:

- The negative covariance estimate uses a two-point covariance identity;
  separate squared-gradient bounds would lose a power of T.
- The full-saddle proof retains both arms, both connectors, the middle,
  all arithmetic modes and the mass anchor. The old `X>=exp(4t)`
  restriction is not imposed on P_*.
- The exact switch center belongs to P_lin. Replacing its amplitude by
  that of P_* requires a recentering estimate; it is not a notation edit.
- The regularized layers are not nonreal zeros. The positive density
  is not identified with adaptive potential curvature without C.
- Fixed compact-source and positive-cutoff obstructions retain their
  separate limiting procedures and restricted classes.
- The 192-cell trial remains failed, and production checks do not become
  mathematical or numerical evidence for the newer theorems.
- Same-time inner overlap does not give a finite-time join. The global
  regulator alone does not give an all-time approximation.

The Note 31 extension likewise must keep the actual signed Q, root-speed
residual correction, all weak regulator terms and the distinction between
absolute global and sharper inner transport errors. No new assertion of
earlier-time simplicity, RH, autonomous closure, interval certification,
time-averaged evolution or independent review belongs in this revision.

## 7. External source and production checks

I checked the cited primary sources at the specific uses relevant here:
the canonical convolution agrees with [Polymath, equation (35), version 2][polymath]
after a change of Gaussian integration variable; [DLMF 5.11][gamma]
supplies sectorial gamma expansions and complex remainder control;
[DLMF 25.2][zeta] supplies the ordinary Dirichlet series and the
Euler-summation formula used for the middle strip;
[DLMF 1.10(iv)--(v)][complex] contains the argument/Rouche and
maximum-modulus principles; [DLMF 24.8.3][bernoulli] is the Bernoulli
Fourier identity. [DLMF 1.9.31][cauchy] is the derivative input for
Note 31. This confirms these imports, not all research claims.
No new literature item or third-party PDF download was needed.

For Sol's later implementation:

1. Compare the live files with the input manifest and the current ledger.
   If the author has already revised them, reconcile the actual changes
   and record the new baseline; do not overwrite newer work using this
   review as an old snapshot.
2. Implement the notation correction, Note 31 proof/statement and scope
   updates. Add the finite E_4 input and early guide if adopting the
   recommended exposition changes. Keep mathematics traceable to the
   cited notes. An apparent proof discrepancy should be returned to Astra
   with the exact formula; do not silently weaken a theorem to typeset it.
3. Build with the maintained `manuscript/build.py`, exporting to the
   shared ignored `output/pdf/heat_density_asymptotics/` location. Check
   references, duplicate labels, unresolved markers, current local links
   and PDF metadata; visually inspect the new theorem tables, residual
   displays, crosswalk and page breaks. Retain source/export hashes and
   the actual production configuration in the build record.
4. Record the implementation in a new production assessment and concise
   DRAFT_HISTORY entry. Update the manuscript/overview/progress pointers
   without upgrading HDA-17, HDA-18 or HDA-20. No numerical campaign or
   new manuscript snapshot is part of this production recommendation.

Suggested instruction for the author to give Sol:

> Read Review 15 and its input manifest in
> `/Users/ebbaker/Documents/shifted-zeta-positivity/papers/investigations-5/01_heat_density_asymptotics/reviews/`.
> Implement the required B_2^Phi notation correction, integrate Note 31
> with the proof and residual terms specified in Section 3, and add the
> finite inner allowance and early model guide recommended in Sections
> 4--5. Preserve the completed HDA-10-MI1 history and all stated limits.
> Build and inspect the new PDF, record actual production provenance,
> and update the existing progress/history files. Return any analytical
> discrepancy to Astra; do not start numerical research or edit source
> notes to hide it.

The companion [continuation note][continuation] defines the next research
deliverable. **Next research task: Analytical — Astra**, derive the
finite-core accuracy and compatibility estimates consumed by HDA-17/HDA-18
joining. **Sol's next task is manuscript production** if the author
assigns the above revision; the numerical research queue remains empty.

[manuscript]: ../manuscript/README.md
[pdf]: ../../../../output/pdf/heat_density_asymptotics/heat_density_asymptotics.pdf
[build]: ../manuscript/BUILD_RECORD_20261024.json
[manifest]: 15_MANUSCRIPT_REVIEW_INPUTS_20261024.json
[production]: 14_MANUSCRIPT_INTEGRATION_PRODUCTION_REVIEW_20261024.md
[old-spec]: ../notes/MANUSCRIPT_INTEGRATION_FOR_SOL_20261024.md
[old-inputs]: ../notes/MANUSCRIPT_INTEGRATION_INPUTS_20261024.json
[local-source]: ../manuscript/09_local_transfer.tex
[inner-source]: ../manuscript/07_explicit_clock.tex
[positive]: ../notes/31_POSITIVE_ALL_HEIGHT_EVOLUTION_AND_COVARIANCE_20261024.md
[positive-review]: 13_POSITIVE_EVOLUTION_AND_COVARIANCE_SELF_REVIEW_20261024.md
[transport]: ../notes/16_ADAPTIVE_FORCING_AND_DIFFERENTIATED_CLOCK_20261024.md
[continuation]: ../notes/32_CONTINUATION_FINITE_CORE_AND_JOINING_20261024.md
[polymath]: https://arxiv.org/html/1904.12438v2#S4.E35
[gamma]: https://dlmf.nist.gov/5.11
[zeta]: https://dlmf.nist.gov/25.2
[complex]: https://dlmf.nist.gov/1.10
[bernoulli]: https://dlmf.nist.gov/24.8.E3
[cauchy]: https://dlmf.nist.gov/1.9.E31
