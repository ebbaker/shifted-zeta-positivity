# VCD-GT-E19 r1 — Proof return

17 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance. Recorded executor dispatch
**gpt-6.1-sol / ultra**. Independently exposed serving-model and
actual effort metadata were unavailable. Type E under B10 Decision18.

**Complete, proved in-note, pending separate E18 internal assessment.**
[Note38][proof] proves one packing bound and both downstream estimates
on the frozen domain. Eligible pairs have disjoint occurrences and
center separation at least \(3a/(4L)\), yielding packing cap
\(1+4TL/(3a)\). Negative individual interactions require
\(|\Im\rho|>2a/(3L)\). Counting their incidences and integrating the
complete canonical density tail gives
\(5B_b[31/9+8/(3ab)]TL e^{-2ba/3}\) as an upper bound for each
of the two counts with \(S_R<0\) or \(M<0\). Here \(0<b<1/2\)
is fixed. Absolute convergence and the far sign give the one-way
implication \(M<0\Rightarrow S_R<0\).

With \(\beta=(4/5)^4\), the padded visibility argument gives
\(16C_sTL/(\beta a^4h)\) for the count with \(\Xi\ge h\).
The matched count-only argument gives \(4C_0TL/(\beta a^2h)\).
Here \(C_s=11\pi(2B_b/b^2)/6\) and \(C_0=3\pi A\).
The pointwise count/strip bound \(O(L/a^2+1/L)\) already eliminates
fixed thresholds for \(a/\sqrt L\to\infty\). The polynomial
fixed-threshold comparison is stated for \(a=L^\eta\) with
\(0<\eta<1/2\). The signed count includes arbitrarily small negative
interactions and has the exponential comparison for \(0<\eta<1\).
Its upper allowance grows even at \(a=L\). The proof is slice-wise
and assumes the collar. Population fractions, time events, gap
signs, incoming values and costs need additional inputs.

One proof route and one correction pass. The pass specified the
length of the admissible incidence window, made the comparator an
explicit second inequality, and tied the full-interaction
strong-threshold implication to the pointwise \(M\ge S_R\).
The documentary replay checks that both Note34 fixed-slice fields
preserve the canonical dyadic second-moment and exponential-density
upper-bound forms with enlarged constants uniform in the control
parameter. For the density the added conjugate pair costs at most the
constant \(2e^{5\sqrt3 b/2}/(8\log8)\) added to \(B_b\), uniformly
in \(U\ge8\) and \(0<v<1\). The opposite signs persist at qualifying
doubles with \(a=2\). These slices supply neither a common physical
heat tube nor the unchanged theta source. The proof note and this
return are the two packet outputs. The next declared dependency is
the separate **[E] VCD-GT-E18** assessment.

| Identity | SHA-256 |
| --- | --- |
| [Frozen E19 r1][request] | 836772f122a86caee26a9998b65113cf6edd1ad9611e847383da1774c82b492b |
| B10 Decision18 | 0e88dcbf430414681687fc71b3d6e73b8113c7178b2921cb155d7a3c3af005fb |
| GT Note37 | 8b78a4fc25dc8e671238210a61ea359c764427cd72a12f48ae2a38e1723f923b |
| GT Note34 | d398589c8bae73dad530c8ffd9950fd778a0beabd0782b22a0efb7c37e06b2be |
| GT Source-use06 | 2484cb1535de12848598be67ac66db6bb4a5e1f16934d9741d2c6320b679f92e |
| TND-O Note21 | ee94e5c08ee793d927ca5afad7fbc86ddda559f39ec87623051e6f6d9ad4ee68 |
| TND-O Assessment07 | 1d5b4babf1ddffc0d9ec0ec0c6e2cb6d1aa5eb8cd203bb91b95e7df495d89c66 |
| [GT Note38][proof] | c1614650cb46dbc19062746d5e2115aa233a1b1d37bc991b6aaae9f42d0b1485 |

The packet and all six frozen input pins matched.

[request]: VCD-GT-E19-r1.md
[proof]: ../../notes/38_VCD_GT_E19_ISOLATED_PAIR_EXCEPTION_COUNT_20261117.md
