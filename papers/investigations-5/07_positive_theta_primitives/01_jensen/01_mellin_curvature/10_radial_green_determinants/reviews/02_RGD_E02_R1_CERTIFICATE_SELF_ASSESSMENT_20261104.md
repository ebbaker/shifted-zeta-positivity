# RGD-E02 r1 — certificate self-assessment

4 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance; actual **gpt-6.1-sol (Codex), effort ultra**,
chat0003, turn `01a1a789-4831-75e3-ac1d-91bbab495d0d`.

**Disposition: E02 author checks pass.** The [return][note] is supported
by the frozen [Packet04][packet], [code][code] and [certificate][record].
The two certified lower allowances exceed 7e-23 and 1e-74 at k=1,4.
This file is **same-assistant/same-model self-assessment** of the proof
and implementation, with fresh read-only same-model contributing route,
code and saved-record checks. It is not the separate E04 r2 assessment,
independent specialist review, or a formal proof of FLINT.

## Checks performed

| Obligation | Author-check finding |
| --- | --- |
| Fixed task and source | Packet04 was frozen before any E02 integration. Exactly k=1,4, moments 0,...,7, U=2, exact b=1/16, complete canonical source and original E+B are retained. |
| Exact algebra | Copied pure polynomial helpers regenerate E03's exact hashes, eight-term/factorization check, independent permutation identities, 111/881 Taylor monomials, all degrees through six and k=4 b-independence. |
| Analytic callback | Integer powers and exponential composition are entire for all values of pi in the certified real pi ball. Ignoring the callback flag is justified by that proof, not sampled behavior. The factor 1/(8*(2j)!) is inside each integral. |
| Domain and acquisition | All 40 integrations cover the five exact rational intervals for all eight moments. Finite complex balls are summed outward; real integrals are justified analytically, with zero-containing imaginary balls required as consistency checks. |
| Tails and rounding | Arb computes every E, positive nonzero B, and E+B. Exact-Fraction post-run checks confirm that saved E+B contains the sum of the saved E/B boxes. Every denominator is certified positive. No tiny tail or compact acquisition error is discarded. |
| Joint propagation | Each collected Taylor coefficient is evaluated on X before abs_upper. Positive upper tail endpoints and outward sums give a residual upper bound U; q_lower-U then gives a valid lower allowance. No neighboring determinant product is bounded separately. |
| Exact serialization | Dyadic midpoint/radius pairs carry the values. Decimal display radii can be dominated by formatting, including for exact endpoints, and are not used for decisions. |
| Rational verification | The standard-library verifier passed: code/six input hashes, cover sums, dyadic endpoint signs, work counts and exact Fraction propagation. Its upward 2^-384 tail grid includes B. Both weaker rational witnesses are verified true. |
| Finite limits | One 384-bit pass; all 40 segment calls complete, maximum 239 callbacks per call, total 4,546. Full acquisition/propagation 0.713642541 s; saved-record verification 0.749134416 s. No 512-bit pass, cap, failed case, rerun or post-start fix. |
| Consequence and scope | Q3,k>=L_(k,2)>lambda_k at k=1,4. D4>lambda/D2 uses inherited D2>0. No new numerical D2 bound, positivity range, uniform-index/order theorem, Mellin/Gaussian estimate or RH conclusion follows. |

Two pre-run implementation-review corrections were applied before code
hashing/acquisition: a finite imaginary ball excluding zero now fails
rather than invoking a precision refinement, and the saved-record verifier
uses the residual upper endpoint and explicitly checks moment/segment
coverage. Neither changed a mathematical formula or required a packet
revision. No defect was found after the acquisition began.

## Artifact identity and trust boundary

Certificate SHA-256:
`6db6276d65ea11706286cffa0aef899d1097f8e4bac76cbdd70f0ef40d692298`.
Code SHA-256:
`b4863a6840cd4d68b10fe993f3f4cdc5e66dd8b3d44903445b306a50c8879db4`.
Packet04 SHA-256:
`18bf3cfd702a38123bdf22b79f6a0e568b262fac1a4881330443afc95fbf3dd1`.
All six acquisition input hashes match current files. The certificate is
65,610 bytes. No prior artifact, inherited code or parent/sibling register
was changed.

Trust includes the accepted Note01 analytical E/B theorem and scalar
normalization, exact sparse polynomial operations, and the identified
python-flint 0.9.0 / FLINT 3.6.0 enclosure implementation. The standard-
library check is an independent arithmetic propagation from saved balls;
it does not independently acquire the integrals or prove pi/exp/library
correctness. The imported API and serialization contracts were checked
against [python-flint integration][acb] and [Arb endpoint documentation][arb].
The detailed primary-source inspection is in the [reference guide][refs].

Read the [result index][results], [theta cluster][theta], [control screen][controls]
and [avoid index][avoid], especially [shared review][shared],
[joint estimates][joint] and [status][status]. The same claim-specific
control screen as E04 r1 applies: altered square weights/series and
non-square reflected primitives do not inherit the canonical quantitative
inputs. No uncalculated control failure or positive-time inference is
claimed. The existing finite-order baseline is preserved.

**Next: [E] RGD-E04 r2 — Sol**, separately assess the saved certificate
under [Packet05][next]. E02 completes at this boundary. B03 is still gated;
no additional acquisition or scan is authorized by this self-assessment.

[note]: ../notes/03_RGD_E02_R1_RIGOROUS_TWO_CASE_BOUND_RETURN_20261104.md
[packet]: ../research-progress/handoffs/04_RGD_E02_R1_RIGOROUS_TWO_CASE_ACQUISITION_20261104.md
[code]: ../numerics/rgd_e02_two_case_certificate.py
[record]: ../numerics/RGD_E02_R1_TWO_CASE_CERTIFICATE_20261104.json
[next]: ../research-progress/handoffs/05_RGD_E04_R2_AND_MODEL_CHANGE_AFTER_E02_20261104.md
[refs]: ../references/README.md
[acb]: https://python-flint.readthedocs.io/en/latest/acb.html#flint.acb.integral
[arb]: https://python-flint.readthedocs.io/en/latest/arb.html
[results]: ../../../../../../../result-summaries/README.md
[theta]: ../../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../../avoid/README.md
[shared]: ../../../../../../../avoid/05_same_model_reviews_and_shared_premises.md
[joint]: ../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[status]: ../../../../../../../avoid/06_status_stronger_than_the_evidence.md
