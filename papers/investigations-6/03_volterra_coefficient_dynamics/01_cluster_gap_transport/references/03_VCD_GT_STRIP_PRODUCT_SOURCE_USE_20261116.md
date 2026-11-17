# Canonical zero strip and exterior product source passages

16 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance for the revised VCD-GT-B06 pass. The helper
dispatch selected **gpt-6.1-sol / ultra**. Separate backend attestation
and actual lead settings are unavailable. Scope is the selected passages
and the normalization and product checks below.
[Reference workflow][workflow] · [Result index][results] · [Avoid index][avoid]

## 1. Checked passages and physical normalization

| Source and passage inspected online | Input used here |
| --- | --- |
| [D. H. J. Polymath, arXiv:1904.12438v2 (4 August 2019), §1 (1)–(4)][poly-intro] | The same \(H_0(z)=\xi((1+iz)/2)/8\), \(\Phi\) and heat multiplier \(\exp(tu^2)\) as [Note12 §1][note12]. Thus no time, ordinate or heat-equation rescaling is needed. |
| [Polymath §3, Theorem 3.2 and the opening of the proof of Proposition 3.3, pp. 14–15][poly-strip] | De Bruijn's theorem contracts the upper strip from \(y_0>0\) at \(t_0\) to \(\sqrt{\max(y_0^2-2(t-t_0),0)}\) for \(t>t_0\). The same passage applies it starting from the canonical \(\xi\) strip \(0\le\Re s\le 1\). Conjugation gives the lower half. |
| [Charles M. Newman, *Fourier Transforms with Only Real Zeros* (1976), Theorem 1, p. 246][newman] | Restates de Bruijn's Theorem 13 for real even integrable \(f\) with \(\lvert f(u)\rvert=O(\exp(-\lvert u\rvert^\gamma))\) for some \(\gamma>2\), multiplying \(f(u)\) by \(\exp(\delta u^2)\) for \(\delta>0\). Its width has the factor \(2\delta\). This generic theorem can be used in the branch's \(u,z\) variables directly. Newman's separate \(\Xi\) notation on p. 245 uses \(s=1/2+iz\). |
| [Polymath §3 opening and Proposition 3.1(i) proof, pp. 12–14][poly-product] | Uses the canonical field's order one, evenness and \(H_t(0)>0\) to obtain the Hadamard product with opposite zeros paired and the local uniform convergence needed for logarithmic differentiation. The product applies even when zeros are nonreal or repeated. |

The canonical records own available archived reading-copy provenance.
The online institutional PDF of [de Bruijn (1950), Theorem 13][debruijn]
returned HTTP 403, so the theorem was checked in the two restatements
above. The online passages were read on 16 November 2026. No new local
reading copy was taken.
[Polymath catalog][poly-catalog] · [Auxiliary-flow catalog, ZP03/ZP04][aux-catalog]

For the branch's whole-line convention \(f(u)=\Phi(u)/2\), the
double-exponential envelope [Note12 (2)][note12] supplies integrability
and the decay hypothesis. Since
\(\Re((1+iz)/2)=(1-\Im z)/2\), the classical strip gives
\(\lvert\Im z\rvert\le1\) at \(t=0\). Applying the theorem with
\(\delta=t\) gives the unconditional bound
\[
 \boxed{\ \lvert\Im\rho(t)\rvert\le b(t)=\sqrt{1-2t},
       \qquad 0\le t\le1/10,\quad H_t(\rho(t))=0.\ }
\]
The notation \(\rho(t)\) means any zero on that slice, with no assumption
of continuous labels. In this interval the width is positive. An
all-real exterior zero population is a separate, unpaid premise.
[Polymath §3][poly-strip] · [OA decision08][oa]

## 2. Order and the absolutely convergent exterior gap term

The order bound also follows from the complete theta envelope in
[Note12 (2)][note12]. Write \(R=|z|\). For \(0\le t\le1/10\) and \(u\ge0\),
absorb \(9u+u^2/10\) into \(C+(\pi/2)e^{4u}\). In the remaining
exponent, retain \(-(\pi/4)e^{4u}\) as an integrable factor and use
\[
 \sup_{u\ge0}\bigl(Ru-(\pi/4)e^{4u}\bigr)
 \le (R/4)\log_+(R/\pi),
\]
where \(\log_+x=\max(\log x,0)\) for \(x>0\), with the right side
defined as zero at \(R=0\). Hence \(\log M_t(R)=O(R\log(2+R))\) as
\(R\to\infty\), uniformly on the slab. The positivity of each summand
of \(\Phi(u)\) for \(u\ge0\) gives \(H_t(0)\ge H_0(0)>0\).
Jensen's formula then gives \(N_t(R)=O(R\log(2+R))\), counting
multiplicities, and a dyadic sum gives
\(\sum_{|\rho|>R}|\rho|^{-2}=O(\log(2+R)/R)\) uniformly as \(R\to\infty\).
This big-O argument supplies convergence with no evaluated tail constant.
Standard Hadamard factorization gives genus-one factors
\((1-z/\rho)e^{z/\rho}\) and a prefactor \(e^{\alpha+\beta z}\).
Opposite pairs can be grouped, as in the inspected Polymath proof.
[Polymath Proposition 3.1(i) proof][poly-product]

On a paid count-two tube let \(Q(z)=(z-z_1)(z-z_2)\),
\(A(z)=H_t(z)/Q(z)\), and \(B=A'/A\). Deflation subtracts the two
root poles, including their full multiplicities at a double.
The constants \(1/\rho\) in the logarithmic derivative and the
constant \(\beta\) cancel in the divided difference. Thus the
[local \(K\) of Note04][note04] is
\[
 K=\frac{B(z_1)-B(z_2)}{z_1-z_2}
 =-\sum_{\rho\ {\rm exterior}}\frac{1}{(z_1-\rho)(z_2-\rho)} .
\]
At \(z_1=z_2\) the left side is \(B'(z_1)\) and the summand has
denominator \((z_1-\rho)^2\). The compact pair region and a paid
collar give separation from all remaining poles. The inverse-square
tail gives absolute convergence, locally uniform in pair coordinates
away from those poles, and permits grouping exterior zeros with
their complex conjugates. The identity needs neither global reality
nor persistent labeling. A radius beyond the certified collar, when
used to sign the combined contributions, requires its own full-slab
zero exclusion. A strictly favorable upper drift requires sufficient
lower positive contribution after all remaining terms are accounted
for. The strip and product alone supply neither datum.
[Note12 §§4–6][note12] · [Existing tube certificate][note15]

The [OA decision08 §2][oa] proves in its all-real exterior class
that an **upper** inverse-square sum only gives a **lower** bound
on the exterior force. The canonical strip provides bounds on imaginary
parts, so using it for an upper \(K\) still requires a separate sign
and magnitude argument. The generic contraction theorem applies to
changed kernels that meet its own Fourier, decay and initial-strip
hypotheses. The Euler-factor controls perturb the canonical
completion and may have a different initial strip. The weighted-square,
finite-source, reflected, primitive-compatible, finite-data, threshold
and changed-observation tests keep the failed or untested canonical
premises in [Note12 §6][note12] and [controls12][controls].
No new zero or annulus enclosure was acquired here.

[workflow]: ../../../../../REFERENCE_WORKFLOW.md
[results]: ../../../../../result-summaries/README.md
[avoid]: ../../../../../avoid/README.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[note04]: ../notes/04_VCD_GT_E02_COMPLETE_COORDINATE_TRANSFER_20261116.md
[note12]: ../notes/12_VCD_GT_E08_CANONICAL_XI_ORACLE_20261116.md
[note15]: ../notes/15_VCD_GT_E04_CERTIFIED_SIGNED_GAP_20261116.md
[poly-intro]: https://arxiv.org/pdf/1904.12438v2#page=1
[poly-strip]: https://arxiv.org/pdf/1904.12438v2#page=14
[poly-product]: https://arxiv.org/pdf/1904.12438v2#page=12
[newman]: https://sites.math.northwestern.edu/~auffing/papers/Newman.pdf#page=3
[debruijn]: https://doi.org/10.1215/S0012-7094-50-01720-0
[poly-catalog]: ../../../../investigations-5/02_heat_flow_rh_applications/references/sources.json
[aux-catalog]: ../../../../investigations-5/06_auxiliary_collision_flows/references/sources.json
[oa]: ../../../../investigations-5/08_theta_observables_newman_dynamics/03_operator_imaginary_time_evolution/03_collision_constraints/notes/08_TND_OA_B03_LEHMER_DIRECTION_AND_ACQUISITION_STOP_20261109.md
