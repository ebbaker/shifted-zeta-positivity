# Review of the signed shrinking time collision continuation

9 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; the exact serving variant and
configured reasoning effort are not exposed and are not inferred.
This is a same-model internal review, not independent mathematical validation.

Reviewed artifact: [Heat Note 8](../newman_collisions/notes/8_SIGNED_SHRINKING_COLLISION_VECTOR_AND_PHASE_OBSTRUCTION_20261009.md).
It completes the bounded analytic attempt requested by the
[integration handoff](HEAT_MANUSCRIPT_INTEGRATION_REVIEW_20261009.md) through
precise obstructions to the proposed phase-independent and packetwise
mechanisms. The full genuine collision-exclusion inequality remains open.

## Results accepted within their stated scope

1. For \(x=4\pi e^{\kappa/t}\), \(\kappa\in[1,2]\), and
   \(0<t\le1/20\), the full symmetric-normalization disk majorant obeys
   \(\eta_N\le5e^{-\kappa(\kappa+4)/(16t)}\). Both errors are paid:
   \(|Q-F|\le\eta_N\) and \(|Q'-F'|\le(\kappa/t)\eta_N\).
   Reflection, every cutoff change, and Cauchy's derivative estimate are
   included. At fixed time the center cutoff belongs to an integer range
   of width at most one. An edge coefficient is exponentially small.
2. The exact scaled vector is
   \(\mathcal V=(F/2,2F'/L)=\sum w_nh_n\), with the actual logarithmic
   phases and the amplitude-drift term retained. Every genuine collision
   requires \(|\mathcal V|^2\le17\eta_N^2/4\). The full kernel keeps
   phase differences, phase sums, and both drift cross terms.
3. On the last block, the phase-independent derivative budget has size
   \(t e^{\kappa(4-\kappa)/(16t)}\), with an explicit positive integral
   constant. The derivative suppression is insufficient for a triangle
   argument treating that block as a small leading-term perturbation.
4. At \(x=4\pi M^2\), \(t=\kappa/(2\log M)\), the genuine terms
   \(M-1,M\) have packet energy \(O(w_M^2/M^2)\) and diagonal energy
   \((2\cos^2(\pi/8)+o(1))w_M^2\). Their adverse cross term nearly
   cancels the diagonal. A uniform positive packetwise comparison fails,
   including any fixed finite collection of bounded translated packets.
5. With the exact weights and local derivative data, independent phases
   can make the complete joint vector exactly zero for all sufficiently
   small times in this regime, retaining the leading term's actual phase.
   The constructive proof signs the tail and uses two perturbed circle
   groups in a fixed head of 256 terms. The constructed phases generally
   violate the genuine logarithmic correlations.

## Proof audit

The approximation audit checked the source's actual domain and constants
against [Polymath, Theorem 1.3, equations (20)--(24)](https://arxiv.org/html/1904.12438v2#S1.Thmtheorem3).
It checked the explicit ledger \(K_*<1.3\),
\(E_C\le1.01e^{-\mathfrak b/t}\), one cutoff payment at most
\(2.6e^{-\mathfrak b/t}\), and
\(E_{AB}\le.01e^{-\mathfrak b/t}\). Their sum is
\(4.706e^{-\mathfrak b/t}<5e^{-\mathfrak b/t}\).
The monotone integral comparison pays the large absolute coefficient
sum only in the error term, where the extra \(x^{-1}\) factor is present.
It is not used as a lower bound for the signed collision vector.

Separate internal audits checked the exact derivative signs, the asymmetric
sine-difference term in the kernel, the endpoint mass constants, the
carrier phase at \(4\pi M^2\), the adjacent phase difference, the weight
ratio and fixed-time frequencies, and the translated packet scope.
They also checked the decreasing weights, the signed tail discrepancy,
the head partition and all strict scalar margins in the ellipse proof.
The latter needs only a uniform sufficiently small time; no explicit
value for that time is claimed.

The audit added three clarifications: the kernel sum uses all ordered
pairs; translated-packet constants may depend on the fixed probe count;
and analytic phase offsets use conjugate multipliers on reflected terms
to preserve real symmetry. The cutoff lower bound is explicitly
\(m_-\ge22000\). No substantive mathematical correction was required.

## Reproducible finite checks

[check_signed_heat_collision_scout.py](../numerics/check_signed_heat_collision_scout.py)
prints the [small record](../numerics/signed_heat_collision_scout_record_20261009.json)
without writing files. It uses only Python's standard library and exact
fractions. Two fresh runs reproduced the record byte for byte.
Its **3,930 assertions** comprise 1,824 signed-kernel identities, 2,048
finite signing/partition invariants, 30 positive-log-series checks,
14 error/payment reserves, nine ellipse reserves, and five polynomial
exponent identities. The record binds the checker source by SHA-256.

These checks evaluate no heat function or genuine phase and enumerate no
large cutoff or zero grid. They validate finite identities and scalar
reserves; they do not prove the imported approximation theorem, the
uniform analytic limits, or the missing complete signed estimate.

## Remaining mathematical input

Writing \(D=\sum_nw_n^2|h_n|^2\), an estimate sufficient for this regime is

\[
2\sum_{n<m}w_nw_mh_n\cdot h_m>-D+17\eta_N^2/4
\]

for the complete actual phases, or an argument conditioned on both small
coordinates that contradicts their arithmetic correlations. The packet
obstruction does not rule out cancellation estimates between packets or
probes over longer ranges. The independent-phase theorem does not assert
an actual heat collision. Even a proof on \(\kappa\in[1,2]\) would leave
other scaling regimes and lower heights to control.

The stable manuscript is preserved. This continuation adds a research
note, this scoped review, a checker and its small record, and concise index
and history entries. No new snapshot, commit, global Newman improvement,
RH conclusion, or literature priority is asserted.
