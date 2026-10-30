# E01 R3 return: primitive absolute-payment lower-cost witness

30 October 2026. Prepared for **Edward Baker** with substantial LLM assistance. Actual implementation/execution model **gpt-6.1-sol**, reasoning effort **ultra**, verified from local turn metadata. Internal LLM implementation; no independent specialist or formal review is claimed. Parent B03 R6; frozen E01 R3 only. The parent is the sole shared-status/history writer.

**Certified domination of the specified absolute-payment class.** Both precisions certify $L_{I,\mathrm{lower}}>M^{\mathrm{IBP}}_{G,\mathrm{upper}}$. The matched direct/C01 consumers retain the accepted R5 bound.

The fixed data are $(\tau,a,R)=(1/4,64,1/32)$ and $I=[1/32,1/4]$. At every uniform real Arb panel the complete signed $Q$ in B03 R6 (5) was formed before its absolute-value enclosure; it was multiplied by $\exp(u+u^2/4-\pi e^{4u})$ and the exact width. Arb encloses $\pi$. This is a real interval range integral with outward rounding, including its complete panel discretization enclosure; sampling and holomorphic quadrature through an absolute value were not used.

| Bits | Panels used | $J_I$ enclosure | $L_I$ enclosure | Accepted $M_G^{IBP}$ enclosure |
| --- | --- | --- | --- | --- |
| 256 | 256 | `[0.0058522387897879686474569009645840704547171679938119244893667845440 +/- 3.60e-4]` | `[9.5780815214780411021552696049803657694597831781645176081122270744e-15 +/- 5.89e-16]` | `[1.9065532420316421905044325905332296519686512055543086341079179388e-16 +/- 2.62e-17]` |
| 384 | 256 | `[0.0058522387897879686474569009645840704547171679938119244893667845440 +/- 3.60e-4]` | `[9.5780815214780411021552696049803657694597831781645176081122270766e-15 +/- 5.89e-16]` | `[1.9065532420331543119055864460382210313169364561830672767067594218e-16 +/- 2.62e-17]` |

All displayed decimals are summaries; the JSON preserves binary midpoints/radii for the complete saved inputs, decoded inputs, all panel contributions, final enclosures and consumer comparisons. Binary R2 $h_1,b,\mathcal U_3,\mathcal U_4$ were decoded at the matching precision. R2 stores row $M_G$ as text, so its full interval was reconstructed using Note26 (13) in the original arithmetic order. This reproduces the displayed common $M_G$ in every one of the twelve rule-C rows at each precision; each printed saved row encloses the reconstruction. No new jets were acquired.

At 256 bits, $L_I-M_G^{IBP}$ is `[9.3874261972748768831048263459270428042629180576090867447014352806e-15 +/- 6.15e-16]`; the strict endpoint gap is `[8.7730097299772570993892303297264320525954633789274076747055551536e-15 +/- 2.44e-81]` and $L_I/M_G^{IBP}$ is `[51.633975476026535034179687500000000000000000000000000000000000000 +/- 10.2]`. Panel arithmetic used 256 range evaluations in 0.008355 seconds.

At 384 bits, $L_I-M_G^{IBP}$ is `[9.3874261972747256709647109603765436663280895325462108804415511344e-15 +/- 6.15e-16]`; the strict endpoint gap is `[8.7730097301322022521028076332143220444237528889081215812395858023e-15 +/- 4.59e-80]` and $L_I/M_G^{IBP}$ is `[51.633975446224212646484375000000000000000000000000000000000000000 +/- 10.2]`. Panel arithmetic used 256 range evaluations in 0.003878 seconds.

The final $J_I$ and $L_I$ enclosures overlap across 256/384 bits; the baseline intervals also overlap. The fixed finite consumer cost differences below are lower bounds for $(L_{I,\mathrm{lower}}-M_{G,\mathrm{upper}}^{IBP})T_N(r/R)$. They are **margin-cost comparisons**, not newly acquired physical margins.

| $r$ | $N$ | 256-bit lower bound | 384-bit lower bound |
| --- | --- | --- | --- |
| 1/64 | 1 | `[1.7546019459954514198778460659452864105190926757854815349411110307e-14 +/- 1.96e-79]` | `[1.7546019460264404504205615266428644088847505777816243162479171605e-14 +/- 3.09e-79]` |
| 1/64 | 2 | `[1.0966262162471571374236537912158040065744329223659259593381943942e-14 +/- 3.04e-81]` | `[1.0966262162665252815128509541517902555529691111135151976549482253e-14 +/- 6.78e-80]` |
| 1/64 | 4 | `[3.8381917568650499809827882692553140230105152282807408576836803797e-15 +/- 1.06e-81]` | `[3.8381917569328384852949783395312658944353918888973031917923187885e-15 +/- 2.64e-80]` |
| 1/64 | 8 | `[3.7696526183496026598938099073043262725996131706328704852250432301e-16 +/- 3.86e-81]` | `[3.7696526184161806552004251548967790034633313194527084919388845244e-16 +/- 4.55e-81]` |
| 1/128 | 1 | `[2.4369471472159047498303417582573422368320731608131687985293208760e-15 +/- 6.72e-82]` | `[2.4369471472589450700285576758928672345621535802522559947887738340e-15 +/- 1.51e-80]` |
| 1/128 | 2 | `[7.9200782284516904369486107143363622697042377726427985952202928470e-16 +/- 2.18e-82]` | `[7.9200782285915714775928124466518185123269991358198319830635149605e-16 +/- 4.90e-81]` |
| 1/128 | 4 | `[7.2346868432972172260588270948264847655952171961640948706339213506e-17 +/- 2.31e-82]` | `[7.2346868434249931766472806003069496026063934413738849845291723196e-17 +/- 4.29e-82]` |
| 1/128 | 8 | `[4.6109229470027494656213741763902349451778728018315571749517179661e-19 +/- 3.69e-84]` | `[4.6109229470841856183401665010179983075821997673229941307648918978e-19 +/- 1.33e-85]` |
| 1/256 | 1 | `[4.9236279096811136782286496748464669682933723045000757358041380964e-16 +/- 6.82e-82]` | `[4.9236279097680726925066777533345684943194531519382314996752777462e-16 +/- 1.45e-81]` |
| 1/256 | 2 | `[8.1127959875427441288994795778720194363924884562785338828590911816e-17 +/- 2.07e-82]` | `[8.1127959876860288683348667526535503599581898526254950846922190136e-17 +/- 4.89e-82]` |
| 1/256 | 4 | `[1.8795809669414762798635647728906079513193804074352206732917075475e-18 +/- 4.36e-83]` | `[1.8795809669746726365215477929100359131368651059423291413888222930e-18 +/- 3.29e-83]` |
| 1/256 | 8 | `[7.5768900261653352033925950942060980959118373528286625524454508011e-22 +/- 1.18e-87]` | `[7.5768900262991550005126892542135577439542504611365239506839561458e-22 +/- 3.34e-87]` |

By B03 R6 (4)/(8), every bound paying the full joint primitive integrand by absolute value before source integration, with its stated finite-$U\ge1$ boundary/exterior or whole-line payment, costs more than the accepted IBP envelope at this center and outer radius. It cannot improve the same-radius, same-degree consumer margin or minimum passing degree. This invokes the issued proof; E02 R6 still owns its assessment.

Only the first positive primitive mode and $I$ enter this **lower** bound. Omitted primitive modes and the source complement contribute nonnegatively to B03 R6 (4), so no omitted-tail **upper** payment is needed for this witness. The saved $h_1$ remains the complete signed theta jet. This neither truncates the physical source nor encloses its complete primitive payment from above.

The result is restricted to the issued absolute-payment class, center, outer radius and unchanged matched consumers. Signed source-panel integration, cross-piece cancellation, other references and $U<1$ are outside that class. No global covering, physical collision, theta-zero exclusion, RH statement or new spatial floor follows.

Total arithmetic: 512 range evaluations, 0.012307 seconds; caps 3584 and 120 seconds. python-flint 0.9.0; FLINT 3.6.0. The record includes exact frozen-input and script hashes. All inputs were unchanged. Only this note, the permitted script and JSON were written.

Runnable evidence: [script](../../numerics/fixed_coefficient_parameter_geometry/execute_fcg_e01_r3.py), [JSON](../../numerics/fixed_coefficient_parameter_geometry/fcg_e01_r3_primitive_absolute_payment_20261030.json), [issued packet](../../research-progress/handoffs/fixed_coefficient_parameter_geometry/FCG-E01_R3_PRIMITIVE_ABSOLUTE_PAYMENT_20261030.md), [parent proof](B03_R6_PRIMITIVE_ABSOLUTE_PAYMENT_OBSTRUCTION_20261030.md). Interpretation follows the [result index](../../../../../result-summaries/README.md), [theta bookkeeping](../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md), [avoid index](../../../../../avoid/README.md), especially [separate absolute bounds](../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md) and [scoped exclusions](../../../../../avoid/07_scoped_exclusions_read_as_universal.md).
