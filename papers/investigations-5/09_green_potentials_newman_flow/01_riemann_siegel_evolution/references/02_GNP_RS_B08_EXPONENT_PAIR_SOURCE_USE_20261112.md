# B08 exponent-pair corroboration: source-use record

**B10 addition, 12 November 2026:** the later addendum below newly imports
Theorem 4; earlier statements about non-use describe their original passes.

12 November 2026, America/New_York. Prepared for Edward Baker with substantial
OpenAI Codex assistance. Actual model and effort are unavailable; no helper
configuration is inferred. Status: selected-passage verification only.

**Jean Bourgain and Nigel Watt, *Decoupling for perturbed cones and mean
square of \(|\zeta(\frac12+it)|\)*, arXiv:1505.04161v1, submitted
15 May 2015.** [Pinned abstract](https://arxiv.org/abs/1505.04161v1),
[pinned PDF](https://arxiv.org/pdf/1505.04161v1). Retrieved 12 November 2026.

Checked printed pages 54–55 (PDF pages 54–55), conditions (13.31)–(13.32),
Lemma 13.3 and its equation (13.37). For the phase
\(T\log((m+h)/(m-h))\), the proof uses
\(BAAB(0,1)=(2/7,4/7)\) when \(h/M\) is sufficiently small, retaining
the bound \((hT)^{2/7}+M^2/(hT)\). Its lemma assumes
\(1\le M\le\sqrt{2T}\), \(M/2\le M_1\le M\), and its stated shift
restriction. These conditions are not removed here.

This corroborates [Note25](../notes/25_GNP_RS_B08_EXPONENT_PAIR_LOCALIZATION_20261112.md)'s
choice of exponent pair. It is not a literal transfer to the asymmetric
phase \(\log(1+h/m)\): that application uses the separately checked
[Robert semimonomial record](01_GNP_RS_B07_DISCRETE_DERIVATIVE_SOURCE_USE_20261112.md).
The paper's decoupling arguments and main zeta mean-square theorems are not
imported; no full-paper reading or later-version inspection is claimed.

The [manifest](02_GNP_RS_B08_REFERENCE_DOWNLOADS_20261112.json) records the
external v1 PDF's URL, path, size and SHA-256. The hash identifies bytes,
not mathematical validity. Citation key: `BourgainWattPerturbedCones2015v1`.


## B09 source-use addendum: Theorem 2 parameter gates

12 November 2026, America/New_York. Prepared for Edward Baker with
substantial OpenAI Codex assistance. Actual model and effort are unavailable;
no helper configuration is inferred. Status: selected-passage verification
and a scoped failed direct import; no new estimate is imported.

The same primary source, [Bourgain–Watt, arXiv:1505.04161v1,
§6, printed pages 14–15](https://arxiv.org/pdf/1505.04161v1), was checked
against both the local PDF text and rendered page images. This uses the
already archived PDF identified by the
[existing download manifest](02_GNP_RS_B08_REFERENCE_DOWNLOADS_20261112.json):
542,327 bytes, SHA-256
`968e5bc1dca05f367fb144b1e616e331962da5ee6b8674e02ad91a0edc44cffa`.
The local bytes were rehashed and matched. This addendum extends the reading
scope recorded above; it does not alter the original B08 record or claim a
full-paper reading.

Theorem 2 fixes real constants \(\epsilon>0\) and
\(C_2,\ldots,C_6\ge2\), and an **integer constant \(\nu\ge6\)**, with
\[
q_\nu=\frac{2(13\nu-12)}{6\nu-5}.
\]
This source parameter \(\nu\) is unrelated to the physical frequency
\(\nu_U\) in the RS notes. The theorem takes \(F\in C^5([1/3,3];\mathbb R)\),
bounded BV functions \(g,G\) on \([1/2,1]\), large positive \(M,T\), and
\(H\ge1\), for
\[
S=\sum_{H/2<h\le H}g(h/H)
  \sum_{M/2<m\le M}G(m/M)
  e\!\left(TF((m+h)/M)-TF((m-h)/M)\right).
\]
Its derivative hypotheses are (6.1)–(6.3): fixed upper bounds for orders
2–5, fixed positive lower bounds for orders 2–4, and a fixed positive
lower bound for \(|F''F^{(4)}-3(F''')^2|\). The constants \(B_5,B_4>0\)
in the following formulas are small constants constructed from
\(C_2,\ldots,C_6\).

Part (A) requires all three conditions (6.4)–(6.6), including exactly
\[
H\le B_5 M
T^{-\frac{149\nu-400}{16(29\nu-75)}}
(\log T)^{\frac{969\nu}{2240(29\nu-75)}}.
\tag{BW 6.6}
\]
The other two conditions are conditional lower bounds on \(H\):
\(H\ge M^{-9}T^4(\log T)^{171/140}\) if
\(M\le T^{7/16}(\log T)^{57/448}\), and
\(H\ge M^{11}T^{-6}(\log T)^{171/140}\) if
\(M\ge T^{9/16}(\log T)^{-57/448}\).
At \(M\asymp\sqrt T\), their antecedents are eventually false; they are
not being silently removed in other regimes.

Part (B) requires (6.10), \(M\le C_6T^{1/2}\), and exactly
\[
H\le B_4\min\left\{
\left(
\frac{M^{155\nu-480}(\log T)^{(969/140)\nu}}
     {T^{46\nu-160}}
\right)^{\frac1{189\nu-480}},
\left(\frac{M^3}{T}\right)^{\frac{5\nu-12}{13\nu-36}}
\right\}.
\tag{BW 6.11}
\]
No conclusion of Part (A) or (B) is used when its hypotheses fail.

For the proposed B09 direct import, grant for this parameter test that the
phase and weights could be transferred to the source form. The largest RS
block has \(T\asymp U\), \(M\asymp N\asymp\sqrt U\), and effective dyadic
shift scale \(H\asymp N/\ell\). Write
\[
a_\nu=\frac{149\nu-400}{16(29\nu-75)}.
\]
For real \(\nu\ge6\),
\(a_\nu'=425/[16(29\nu-75)^2]>0\), so its smallest allowed value is
\(a_6=247/792\). Thus (6.6) gives, at best in power of \(T\),
\[
H\ll T^{149/792}
 (\log T)^{969\nu/[2240(29\nu-75)]}.
\]
In (6.11), the first entry simplifies at \(M\asymp\sqrt T\) to
\[
T^{1/6}(\log T)^{969\nu/[140(189\nu-480)]},
\]
since \(((155\nu-480)/2-(46\nu-160))/(189\nu-480)=1/6\).
The second entry is
\(T^{(5\nu-12)/[2(13\nu-36)]}\), whose exponent exceeds \(1/6\)
for every allowed \(\nu\); the first entry alone already supplies the
necessary power restriction.

At the current B08 boundary \(\ell=U^{17/72}\), the effective shift scale
is \(H\asymp U^{19/72}\). Its excess exponents over the two necessary
source caps are respectively
\[
\frac{19}{72}-\frac{149}{792}=\boxed{\frac5{66}},
\qquad
\frac{19}{72}-\frac16=\boxed{\frac7{72}}.
\]
For each fixed allowed \(\nu\), the displayed logarithmic factors and
fixed constants cannot absorb either positive power gap. At
\(\ell=U^{17/72-\kappa}\), \(\kappa\ge0\), each gap increases by
\(\kappa\); at \(\ell=U^{17/72+\rho}\), each decreases by \(\rho\).
The exclusion therefore concerns a direct improvement at or below the
B08 boundary, not every interval allowed by B08.

Here \(H\) is the location scale of the source's shifts
\(H/2<h\le H\), not the length of a short subinterval of those shifts.
It cannot be replaced by a subdivision length without rechecking the
phase and amplitude hypotheses. The actual RS weight is also coupled in
\(h,m\) through its Fourier factor, whereas the displayed theorem has
separated \(g(h/H)G(m/M)\); converting that weight, the asymmetric
log-ratio phase, and the exact cutoffs would require additional work.
The numerical gate failure above holds even after granting those
transfers. Shifts of size a sufficiently small fixed multiple of
\(N/\ell\) have Fourier argument in a fixed neighborhood of zero, so
Fourier decay alone does not remove the missing scale.

This is only a failed direct application of the **printed Theorem 2** in
this parameter regime. The authors explicitly say in Remark (i), printed
page 15, that (6.6) and (6.11) impose upper bounds stronger than their method
requires, and that an additional case was omitted. No obstruction to all
Bourgain–Watt refinements, to joint cancellation, or to the canonical RS
sum is asserted. The established B08 result remains unchanged.

## B10 source-use addendum: cumulative theorem and internal parameters

12 November 2026, America/New_York. Prepared for Edward Baker with
substantial Codex assistance; actual model/effort unavailable, chat0007.
The existing v1 PDF was rehashed and matched the original manifest.
Printed pages 1, 15 and 20 were visually inspected; pages 16 and 30–33
were additionally inspected in extracted text. This is selected-passage
reading, not a full proof audit or a claim about later versions.

[Theorem 4, page 1](https://arxiv.org/pdf/1505.04161v1) gives the
cumulative critical-line mean-square error E(T)=Oε(T^(1515/4816+ε)).
[Note29](../notes/29_GNP_RS_B10_SIGNED_MELLIN_MEAN_ESTIMATE_20261112.md)
uses ε=151/144480 to retain θ=19/60, then proves the exact-cutoff
Mellin transfer. The local error is retained, not erased by subtraction.
Theorem 2's shift gates are not imposed on this separate import.

Section 7, (7.3), (7.5), independently force TH²/M³≪1 in the
unchanged internal setup. At M≈sqrt T and H≈M/ell, this fails below
the quarter-power window. Adding the omitted spacing case alone does
not remove these premises. This scopes a setup failure, not the method.

## B10 pre-integration audit, 12 November 2026

For Edward Baker with substantial Codex assistance, chat0008. Actual model
and effort are unavailable. Rechecked Theorem 4 in the pinned v1 PDF and
the (7.3), (7.5) constraints. The **left** inequality in (7.3) bounds
N(R−1)² above, and R≥2 converts this to the required upper bound on NR².
See [Note31](../notes/31_GNP_RS_B10_PREINTEGRATION_PROOF_AUDIT_20261112.md).
The journal article is *International Mathematics Research Notices*
2018(17), 5219–5296. [Publisher record](https://academic.oup.com/imrn/article/2018/17/5219/3059060)
The checked theorem numbering refers to v1. The separate follow-up
[arXiv:1709.04340](https://arxiv.org/abs/1709.04340) is marked withdrawn.
