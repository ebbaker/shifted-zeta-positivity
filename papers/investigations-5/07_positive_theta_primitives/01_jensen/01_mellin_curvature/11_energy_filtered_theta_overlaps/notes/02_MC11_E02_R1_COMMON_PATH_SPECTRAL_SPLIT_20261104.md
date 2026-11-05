# MC11-E02 r1 — the common-path three-orbital spectral split

4 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6.1-sol (Codex), effort ultra**; MC11 chat0001, thread 01a1a8e5-1cb3-74b3-80a9-e4b99f6f4fab, turn 01a1a8f3-323b-7ca1-aa36-acb844ed67ff.

**E02 r1 complete as a bounded return; E04 assessment remains pending.** Every level \(n\ge3\) raises the unnormalized three-orbital overlap at every filter setting. The entire higher-level contribution is positive and at most \(5.402\times10^{-40}\). The existing bounds leave both the \(n=2\) contribution and net change undecided. The deficit is localized to the five first-excited source moments, and the conditional E03 acquisition gate is demonstrated below. This is a precise limit of the specified enclosures, not a vanishing or negative canonical overlap.

[Exact record][record] · [Reproducible calculation][code] · [Live register][progress] · [Continuation/model change][handoff]

## 1. Fixed question and input versions

The [E01 assessment][e01] supplies accepted source, endpoint and moment-payment premises. Use the unchanged full half-line, canonical energies \(E_n=\pi n^2\), common filter path \(w_1=1,w_{n\ge2}=s\in[0,1]\), and real unnormalized \(D_3(s)\). Put
\[
A_j=a_j(4\pi),\quad H_j=\sum_{n\ge3}a_j(\pi n^2),\quad
h_j=A_j+H_j,\quad b_j=a_j(\pi),\quad c_j(s)=b_j+s h_j.
\]
Here \(A_j\) denotes a source moment of the first excited level. E01 Note01 used the letter \(A_j\) for a compact primitive integral; that notation is local to that note and must not be imported into these formulas. The compact Green reference is always written \(c_j^*\).

The two contributions are defined along this same path:
\[
L_2=\sum_{j=1}^5 A_jK_j,\qquad
L_{\ge3}=\sum_{j=1}^5 H_jK_j,\qquad
K_j=\int_0^1G_j(c(s))\,ds,\qquad
\Delta_3=L_2+L_{\ge3}=D_3(1)-D_3(0).
\]
There is no sequential restoration of the two groups.

All five E01 frozen input hashes match the request. The E02 record also binds the E01 assessment, exact record and continuation packet, and the original RGD acquisition used solely to read its saved \(\pi\) enclosure. That acquisition's SHA-256 matches the value already bound in RGD r2:
6db6276d65ea11706286cffa0aef899d1097f8e4bac76cbdd70f0ef40d692298.
No input version was substituted, and no integration was repeated.

## 2. Collect first, then integrate the five weights

Permutation expansion gives
\[
D_3=c_3^3-2c_2c_3c_4+c_1c_4^2+c_2^2c_5-c_1c_3c_5.
\]
The five collected moment gradients, including all cofactors for repeated entries, are
\[
\begin{aligned}
G_1&=c_4^2-c_3c_5,&
G_2&=2c_2c_5-2c_3c_4,\\
G_3&=3c_3^2-2c_2c_4-c_1c_5,&
G_4&=2c_1c_4-2c_2c_3,\\
G_5&=c_2^2-c_1c_3.
\end{aligned}
\]
Define the exact integrated product
\[
B_{ij}=b_ib_j+\frac{b_ih_j+h_ib_j}{2}+\frac{h_ih_j}{3}.
\]
Then
\[
\begin{aligned}
K_1&=B_{44}-B_{35},&
K_2&=2B_{25}-2B_{34},\\
K_3&=3B_{33}-2B_{24}-B_{15},&
K_4&=2B_{14}-2B_{23},\\
K_5&=B_{22}-B_{13}.
\end{aligned}
\]
The same \(b,h\) appear in every expression. In the checker, formal substitution \(c=b+s h\) precedes exact integration of each power of \(s\); all constant, linear and quadratic terms remain.

The formal polynomial identity
\[
\boxed{\sum_{j=1}^5h_jK_j=D_3(b+h)-D_3(b)}
\]
passes against a separate permutation expansion of the cubic endpoint difference. Flipping the signed contribution \(h_2K_2\) breaks that identity. This is an algebraic author check; E04 must assess the full return independently of the saved PASS flags.

## 3. Existing-data bounds and the complete infinite tail

The ground source moments use the saved compact coefficient boxes and the nonzero spatial exterior. If \(R_j=x_j-A_j^{\rm compact}\in[0,B_j(2)]\) is the omitted first-mode primitive exterior, then
\[
b_j=c_j^*+R_{j-1}-R_j,\quad
b_j\in[\underline c_j^*-\overline B_j,\,
        \overline c_j^*+\overline B_{j-1}].
\]
The checker rounds each saved positive spatial-tail upper bound upward to the \(2^{-384}\) grid before propagating it. The original compact integration uncertainty is already in \(c_j^*\). The spatial exterior is paid once; no Green transfer is applied to a truncated source.

For a single level, let \(Q_j(E)=\frac18\int_0^\infty m_jp_E\). Green transfer gives \(a_j(E)=Q_{j-1}(E)-Q_j(E)>0\). With \(\lambda_2=16\pi-1\), the existing exponential tangent bound yields
\[
0<A_j\le U_j:=\frac{e^{-4\pi}}{8\lambda_2^{2j-1}}.
\]
For \(n\ge3\), use \(n^2\ge9+7(n-3)\). Summing the geometric majorant and setting \(\lambda_3=36\pi-1\) gives
\[
0<H_j\le V_j:=
\frac{e^{-9\pi}}{8(1-e^{-7\pi})\lambda_3^{2j-1}}.
\]
This includes every level \(n\ge3\) and all spatial \(u\ge0\); no unrecorded energy cutoff or discarded spatial tail occurs. The inequality \(a_j\le Q_{j-1}\), using positivity, is slightly sharper than bounding the two primitive terms by their sum.

The only additional constant evaluation is exact rational arithmetic. The saved \(\pi\) ball is enlarged to a \(2^{-128}\) grid. For positive \(x\in\{4\pi,7\pi,9\pi\}\), the checker encloses \(e^x\) by its sum through degree 128 plus the geometric remainder
\[
0<e^x-\sum_{k=0}^{128}\frac{x^k}{k!}
\le\frac{x^{129}}{129!}\frac1{1-x/130}.
\]
It evaluates endpoint bounds, inverts, and rounds \(e^{-x}\) outward to a \(2^{-192}\) grid. All later arithmetic is exact Fraction arithmetic. These are constant evaluations, not quadrature, a new moment acquisition, or floating inputs.

## 4. Integrated weights and the one regrouping

The outward coefficient intervals have signs \(+,-,+,-,+\), both for the pointwise \(G_j(c(s))\) over the entire path and for the integrated \(K_j\). Rounded outward decimal bounds for the latter are:

| \(j\) | Lower \(K_j\) | Upper \(K_j\) |
| --- | --- | --- |
| 1 | \(8.99348\times10^{-25}\) | \(8.99352\times10^{-25}\) |
| 2 | \(-2.89646\times10^{-21}\) | \(-2.89644\times10^{-21}\) |
| 3 | \(3.52810\times10^{-18}\) | \(3.52814\times10^{-18}\) |
| 4 | \(-1.73653\times10^{-15}\) | \(-1.73649\times10^{-15}\) |
| 5 | \(3.46680\times10^{-13}\) | \(3.46692\times10^{-13}\) |

The first interval calculation uses independent positive moment boxes \(0<A_j\le U_j\), \(0<H_j\le V_j\). It leaves both response intervals containing zero. Those initial intervals are retained in the record.

The one permitted regrouping divides each response by its own lowest group moment and retains the correlations supplied by the logarithmic slope. For
\[
F(E)=4E-9-\frac{12}{2E-3},\qquad
\kappa_2=F(4\pi)>40,\quad \kappa_3=F(9\pi)>100,
\]
the E01 normalized-moment recursion gives
\[
0<\frac{A_j}{A_1}\le\kappa_2^{-2j+2},\qquad
0<\frac{H_j}{H_1}\le\kappa_3^{-2j+2}.
\]
The group inequality follows by applying the single-level recursion to every level and summing. Monotonicity of \(F\) justifies the common \(\kappa_3\).

For either integrated weight vector \(K\), the normalized lower/upper bounds are
\[
\underline K_1+\frac{\underline K_2}{\kappa_N^2}
                 +\frac{\underline K_4}{\kappa_N^6}
\ \le\ \frac{L_N}{\text{lowest group moment}}\ \le\
\overline K_1+\frac{\overline K_3}{\kappa_N^4}
                +\frac{\overline K_5}{\kappa_N^8}.
\]
The checker uses lower bounds on \(\kappa_N\) with the correct sign orientations. Intersecting the resulting intervals with the initial valid bounds is bookkeeping, not an additional regrouping.

For the higher group this lower bound exceeds \(6.29517\times10^{-25}\). Applying exactly the same argument to the whole-path \(G_j\) boxes gives
\[
\frac{\chi_3(E_n;s)}{a_1(E_n)}>6.29515\times10^{-25}>0,
\qquad n\ge3,\quad 0\le s\le1.
\]
Thus the pointwise sign is proved on the stated domain, rather than inferred from the sign of an integrated contribution or an asymptotic limit. For \(n=2\), the retained normalized interval still spans approximately
\[
-1.22794\times10^{-24}<L_2/A_1<2.22803\times10^{-24}.
\]
In particular, the lower-bound contribution from the negative \(K_2A_2\) term can outweigh the positive \(K_1A_1\) term; the present boxes do not resolve their cancellation with \(K_3A_3\) and the smaller terms.

## 5. Returned bounds and what they decide

The exact rational endpoints are in the record. The following simpler bounds round outward:

| Quantity | Rigorous conservative bound | Sign disposition |
| --- | --- | --- |
| \(L_2\) | \([-1.087\times10^{-32},\,1.335\times10^{-32}]\) | Undetermined |
| \(L_{\ge3}\) | \(0<L_{\ge3}<5.402\times10^{-40}\) | Strictly positive |
| \(\Delta_3\) | \([-1.087\times10^{-32},\,1.335\times10^{-32}]\) | Undetermined |
| \(D_3(0)\) | \(1.66142398817\times10^{-28}<D_3(0)<1.66142398818\times10^{-28}\) | Strictly positive |
| \(\Delta_3/D_3(0)\) | \([-6.540\times10^{-5},\,8.033\times10^{-5}]\) | Signed interval containing zero |

The ground determinant bound is a new exact propagation of the existing ground moment boxes, including the full-half-line spatial exterior. It licenses the last fractional interval; no fractional effect is stated without this denominator floor.

The higher-level group is at least seven orders of magnitude below the present first-excited uncertainty width. The two groups' reinforcing or opposing relationship remains **undetermined**, because the first group sign is unresolved. Strict positivity of the tail does not settle the net sign.

## 6. Why E03 is justified, and specified useful widths

The unresolved numerical inputs are \(A_1,\ldots,A_5\). The ground boxes are narrow, the common-path cofactor uncertainty is quantified, and the complete higher group has a paid upper bound. No new structural premise is needed to propagate sharper \(A_j\) boxes.

A concrete sufficient E03 target is an absolute **half-width** at most \(U_j/10^6\). The following slightly smaller decimal targets are valid:

| \(j\) | Requested absolute half-width at most |
| --- | --- |
| 1 | \(8.8483\times10^{-15}\) |
| 2 | \(3.6456\times10^{-18}\) |
| 3 | \(1.5020\times10^{-21}\) |
| 4 | \(6.1887\times10^{-25}\) |
| 5 | \(2.5498\times10^{-28}\) |

Full interval widths are twice these numbers. The saved exact target is \(U_j/10^6\), so the decimal requests are conservative acquisition goals.

To make the usefulness test explicit, write \(k_j\) and \(r_j^K\) for the midpoint and radius of the current \(K_j\) boxes. For acquired moment midpoints \(\mu_j\in[0,U_j]\) and half-widths \(\delta_j\le U_j/10^6\),
\[
\left|L_2-\sum_j k_j\mu_j\right|
\le\sum_j\max|K_j|\,\delta_j+\sum_jU_jr_j^K.
\]
The moment-radius payment is \(<2.4980\times10^{-38}\); the current cofactor-radius payment is \(<5.7997\times10^{-38}\). Including the full positive tail, a conservative symmetric net-sign test is
\[
\left|\sum_j k_j\mu_j\right|>8.352\times10^{-38}.
\]
The sign of that midpoint expression then decides the sign of the net change. Recomputing \(K\) with refined \(h=A+H\) may improve this sufficient test, but is not needed for its validity.

The record also supplies two retained-uncertainty-set witnesses, one positive and one negative, satisfying the current moment upper bounds and slope recursions. Boxes at these target widths enclose net responses near \(+3.902\times10^{-33}\) and \(-3.615\times10^{-33}\), respectively, and both exclude zero even with current cofactor and tail payments. These are **not measured or claimed realizable source moments**. They demonstrate that input narrowing can decide this calculation without changing its observable or inventing a new source estimate; they do not predict the actual sign. An acquisition returning a near-zero interval remains an admissible inconclusive result.

Thus E03's conditional gate is met. **No E03 acquisition was performed here.** Its existing 384-bit, five-integral, one-refinement contract remains unchanged. An E03 return, including an interval containing zero, must go to E04 before B01 interprets it.

## 7. Provenance, scope, and continuation

One exact/outward calculation and one regrouping were used, with 36 checks, zero integrand evaluations and zero new moments. The recorded execution time was 0.127425333 seconds. The code/record remain below 1 MiB. Reproduction from the repository root, using a fresh output file:

    python3 papers/investigations-5/07_positive_theta_primitives/01_jensen/01_mellin_curvature/11_energy_filtered_theta_overlaps/numerics/mc11_e02_r1_spectral_split.py --repo . --output /tmp/MC11_E02_R1_REPLAY_fresh.json

The coordinator wrote the calculation, and one read-only Sol/ultra contributor supplied the algebra/tail derivation. This is same-model internal author checking with shared inherited enclosures; **E04 has not assessed this return**. A model change does not supply specialist independence.

This is a fixed-order quantitative estimate, not a new RH-equivalent criterion or positivity range. Read the [result index][results], [theta cluster][theta], [avoid index][avoid], [reformulation warning][a01] and [joint-estimate warning][a12]. The [collision screen][controls] and [shape warning][a02] delimit the premises: reweighted square sources do not inherit the ground/cofactor payment; Euler-factor changes do not retain this trace; reflected and positive-primitive controls do not supply the literal canonical square sum. Some sources satisfying the same numerical premises could share the result; no uncomputed control-margin failure is asserted. Positive-time collisions do not contradict this time-zero fixed-order bound.

The inconclusive intervals exclude only a sign conclusion from the specified bounds, not a sign of the true canonical response or the possibility of sharper estimates; see [scope warning][a07]. Growing order, neighboring shifts and transfer to Mellin curvature remain open.

**Next: [E] MC11-E03 — Sol**, the conditional five-moment first-excited acquisition and replay, under the [continuation/model-change packet][handoff].

[record]: ../numerics/MC11_E02_R1_SPECTRAL_SPLIT_20261104.json
[code]: ../numerics/mc11_e02_r1_spectral_split.py
[progress]: ../research-progress/01_ENERGY_FILTERED_THETA_OVERLAPS_RESEARCH_PROGRESS_20261104.md
[e01]: ../reviews/01_MC11_E01_R1_STARTING_RESULTS_ASSESSMENT_20261104.md
[handoff]: ../research-progress/handoffs/02_MC11_E02_RETURN_AND_E03_MODEL_CONTINUATION_20261104.md
[results]: ../../../../../../../result-summaries/README.md
[theta]: ../../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[avoid]: ../../../../../../../avoid/README.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[a01]: ../../../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
