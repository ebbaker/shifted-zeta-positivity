# Hakimoglu-Brown's strip comparison against the height-p floor, and a table from the unconditional strip

17 October 2026. Prepared for Edward Baker with LLM assistance. Model:
Claude Opus 5.5 (configured identifier `claude-opus-5-5`), Claude Cowork,
reasoning effort max; the serving model may differ from the configured
identifier. This is the second note of Project 03's first phase. It carries
out item 6 of Section 9 of
[note 01](01_HEIGHT_P_TRANSPORT_AND_LEMMA_AP_CLAUDE_20261017.md), the
comparison with Hakimoglu-Brown's preprint, which became possible when
Edward added the preprint to the project on 17 October 2026.

**Revision (later on 17 October 2026, same model).** A literature check
made after filing found that three unrefereed 2026 preprints already start
a stepped comparison for the highest zero from the classical strip
\(M(0)\le1\), with stronger unconditional claims. They are listed in
Section 11. Summary items 3 and 6 and Sections 4.6, 9 and 10 were revised
accordingly; the mathematics, the table and the records are unchanged. The
note moved to `notes/round-1/` the same day.

Claim status is marked as in note 01: **proved**, **proof sketch**,
**conditional**, **numerical**, **planning** and **open**. A statement that
is the preprint's own is called "the paper's" and keeps the paper's status.
The two check programmes are
[`hakimoglu_brown_comparison_claude_20261017.py`](../../numerics/round-1/hakimoglu_brown_comparison_claude_20261017.py),
whose [record](../../numerics/round-1/HAKIMOGLU_BROWN_COMPARISON_CLAUDE_20261017.json)
has sections "record A" to "record E", and
[`unconditional_strip_table_claude_20261017.py`](../../numerics/round-1/unconditional_strip_table_claude_20261017.py),
whose [record](../../numerics/round-1/UNCONDITIONAL_STRIP_TABLE_CLAUDE_20261017.json)
is called "the certificate" below.

**Summary.**

1. *Source.* C. Hakimoglu-Brown, arXiv:2610.12803v1 (working draft of 7
   October 2026, 26 pages), read in full from the project copy. Project
   01's reading of it (its ledger H11), which note 01 relied on, is
   confirmed at every point note 01 used.
2. *Same main term, different remainder.* His floors for \(S\) at height
   \(p\) (Propositions 7, 8 and 11) and note 01's Theorem 4.6 have the same
   main term, \(\tfrac14L-\tfrac12\kappa(\tfrac{1+p}2+\tfrac t4L)\). His heat
   weight \(e^{t\log^2n/4}\) is the Gaussian average
   \(\mathbb E\,n^{-\tau N}\), and his point \(s_B=w+\tfrac t2\alpha(w)\) is
   the first iterate of note 01's saddle equation, with \(\alpha\) in
   Stirling form. He controls the remainder through Polymath's
   Riemann–Siegel coefficients on the band \(3\le\operatorname{Im}z\le6\)
   and a truncated, heat-weighted Dirichlet polynomial. Note 01 controls it
   through the exact Gaussian representation and Euler-product majorants,
   at any \(p>1\). At his height \(p=61/20\), note 01's floor (floating) is
   larger than his certified-form floor by \(0.005\) to \(0.017\): its
   remainder is \(1.7\) to \(4.4\) times smaller. A derivative bound
   obtained from note 01 by Cauchy's estimate (Corollary 2.1, proved) is
   smaller than his for \(t\le0.1\) and up to \(8\%\) larger after (record
   B).
3. *Main finding (conditional on the paper).* His derivative-kernel
   comparison (Lemma 10, Theorem 12) uses the seven-eighths hypothesis only
   through the initial strip \(M(0)\le q_0\), as his Section 1.1 says.
   Every zero of \(\xi\) satisfies the strip \(M(0)\le1\). Started from it,
   with his own Proposition 11 at \(p=61/20\), the comparison reaches
   \(q=1/25\) at \(t=16891/100000<1/5\), so
   \[
   \Lambda\ \le\ \tfrac{18891}{100000}=0.18891
   \]
   with no zero-free half-plane as input. The 34-row table is checked here.
   The chain, the Bernstein coefficients and the gates are checked in exact
   rational arithmetic, and the scalar bounds in directed-rounding decimal
   arithmetic. The same programme reproduces every certified margin of his
   Table 3.
   - The value is below the published \(0.2\) of Platt and Trudgian.
   - It is conditional on his unrefereed Lemma 2, Lemma 3, Proposition 11,
     Lemma 10 and Theorem 12, and on Polymath's published boundary
     computation.
   - It is neither a record nor a new idea. Gordon (\(0.1577\)), Raymond
     (\(0.1494\)) and Planat (\(0.1486\), under stated premises) start
     stepped comparisons from the same strip, and Gomila claims \(0.1788\)
     by Polymath's criterion. All four are unrefereed (Section 11). What
     this table adds is a short, fully checked instance whose numerical
     inputs are all published; its analytic inputs are the preprint's
     lemmas.
   - His warnings against extrapolating to \(\sigma=1\) (Remark 5, Section
     9) concern only his closed one-step formulas. Those formulas indeed do
     not reach \(q=1/25\) by \(t=1/5\) from \(q_0=1\), and neither does his
     Theorem 9 kernel (record C).
4. *What note 01's floor adds for zeta (planning).* Put note 01's floors
   and Corollary 2.1 in place of his Proposition 11. The same comparison
   then gives \(0.1867\) from \(q_0=1\) (at \(p=2.75\)) and \(0.1370\) from
   \(q_0=9/16\) (at \(p=2.5\)), against \(0.1889\) and \(0.1396\) (record D).
   The gain is small. Note 01's value for zeta is a second proof of the
   inputs that does not use Riemann–Siegel, once its evaluation is
   certified.
5. *Project 01's Target A (planning).* His Lemma 10 kernel with note 01's
   floors lowers the Target A planning values by \(5\%\) to \(13\%\). At
   \(q=10^8\) they fall from \(0.251/0.245\) to \(0.234/0.227\)
   (even/odd), and at \(q=10^{12}\) from \(0.187/0.184\) to
   \(0.165/0.161\) (record E). These remain conditional on H12, the
   comparison theorem and certification.
6. *Decisions (Section 9).* The table is a cross-check, not a priority
   result. A review of this round should start with note 01's Theorem 4.6
   and this note's Corollary 2.1, which also serve Project 01's family,
   where no comparable literature was found. The paper's Lemma 3 and
   Proposition 11 are the statements the table rests on. Note 01's
   certification, after that review, is the route to an independent proof
   of their output.

## 0. Source and coverage

The project copy `2610.12803v1.pdf` is arXiv:2610.12803v1 [math.NT], dated
8 October 2026 by arXiv and 7 October 2026 by the author, titled "A
conditional bound \(\Lambda\le0.13963\) for the de Bruijn–Newman constant".
All 26 pages were read: Sections 1–9, Tables 1–7, the acknowledgement
(ChatGPT assisted, not independently refereed) and the references. The
paper uses Polymath's normalization,
\(H_t(z)=\int_0^\infty e^{tu^2}\Phi(u)\cos(zu)\,du\),
\(H_0(z)=\tfrac18\xi(\tfrac12+\tfrac{iz}2)\), and the same
\(S(x,p,t)=-\operatorname{Im}(H_t'/H_t)(x+ip)\) as note 01. Its \(X\) is
\(60000083951.5\).

Its imported inputs, as it states them:

- Polymath's Section 8.4, claim (a): \(H_t(x+iy)\ne0\) for
  \(X\le x\le X+1\), \(\tfrac15\le y\le1\), \(0\le t\le\tfrac15\). The paper
  says its numerical certificate "has not been replayed here". A footnote
  corrects a time-interpolation term in Polymath's equation (91) and says
  the computation's code is unaffected.
- The finite RH verification Polymath used.
- Polymath's Propositions 6.1–6.2, its Proposition 3.1(ii) and its Theorem
  1.5(i).
- De Bruijn's strip theorem.

Gordon's and Gomila's preprints are cited, but not used.

## 1. Crosswalk

| Item | Hakimoglu-Brown | Note 01 or Project 01 | Relation |
| --- | --- | --- | --- |
| evaluation point | \(w=(1-iz)/2\) | \(w=\tfrac12(1+p)+\tfrac i2x\) | complex conjugates at \(z=x+ip\) |
| saddle | \(s_B=w+\tfrac t2\alpha(w)\), \(\alpha(s)=\tfrac1{2s}+\tfrac1{s-1}+\tfrac12\operatorname{Log}\tfrac s{2\pi}\) | \(s_*=w+\tfrac t2\alpha(s_*)\), \(\alpha=\Gamma_F'/\Gamma_F\) exact | first iterate; the two \(\alpha\) differ by \(\tfrac1{6s^2}+O(s^{-4})\) |
| heat weight | \(h_n=e^{t\log^2n/4}\) | \(\mathbb E\,n^{-\tau N}\), \(\tau^2=t/2\) | equal |
| heat gain | Lemma 6: \(\operatorname{Re}s_B\ge\tfrac{1+y}2+\tfrac t4L\); \(u=\sigma_p+5.57t^-\) | \(\sigma_*=\sigma_0+\tfrac t4\ell_*\) | the same shift (\(5.57<L/4\)) |
| floor | Propositions 7, 8, 11: \(\tfrac L4-\tfrac12\kappa(u)\) minus heat-weight and truncation errors | Theorem 4.6: \(\tfrac{\ell_*}4-\tfrac12\kappa(\sigma_*)-\tfrac E2\) | same main term |
| domain | \(x\ge6\cdot10^{10}\), \(3\le y\le6\) (Lemma 3), \(t\le\tfrac15\) | zeta \(x\ge40\); family every \(x\); any \(p>1\); \(t\le\tfrac12\) | note 01's is wider |
| \(\partial_pS\) | Proposition 11: \(G^*=\tfrac14K_2(u)\) plus errors (Cauchy on a disk of radius \(\tfrac1{20}\)) | Corollary 2.1 below: \(\tfrac14K_2(\sigma_*)\) plus a Cauchy estimate of \(E\) | same main term |
| finite region | Lemma 2: for \(t\le\tfrac15\), a zero with \(\lvert x\rvert\le X\) has \(\lvert\operatorname{Im}z\rvert<\tfrac15\) | none in note 01; Project 01, ledger H11 | used as it stands |
| comparison | Theorem 9, kernel \(K_h\ge(h/p)K_p\) for \(p^2\ge5q\) | Project 01, Proposition 3.3 (proved) | the same inequality |
| derivative kernel | Lemma 10 (polynomial (25)), Theorem 12 | not in the portfolio before | new to it |

## 2. A derivative bound from note 01

Theorem 12 needs an upper bound for \(\partial_pS\) as well as a floor for
\(S\). Note 01 gives one by Cauchy's estimate.

**Corollary 2.1 (proved).** Let \(r>0\). Suppose that at every point
\(w'\) of the closed disk \(\lvert w'-w\rvert\le r\) the hypotheses of note
01's Lemma 3.2 and Proposition 4.5 hold, with \(E(w')\) the bound of
Proposition 4.5. For the family this needs \(\operatorname{Re}w'>1\); for
zeta it needs \(\operatorname{Re}w'>1\) and \(\operatorname{Im}w'\ge20\).
Let \(a_*\ge\lvert\alpha'(s_*)\rvert\): \(a_*=\tfrac14\psi'(\tfrac{\sigma_*+\mathfrak a}2)\)
for the family and \(a_*=2/T\) for zeta (note 01, Lemma 4.2). Then
\[
\partial_pS(x,p,t)\ \le\ \frac{K_2(\sigma_*)+a_*}{4(1-\tau^2a_*)}+\frac1{4r}\max_{\lvert w'-w\rvert=r}E(w').
\]

*Proof.* On the disk, \(\mu\mapsto\tau^2\alpha(w'+\mu)\) maps a fixed
domain into itself with a contraction constant uniform in \(w'\). For the
family the domain is the half-plane \(\operatorname{Re}\mu\ge0\). For zeta
it is \(D_{x_+}\) of Lemma 3.2, with \(x_+\) the largest \(2\operatorname{Im}w'\)
on the disk; the images lie in \(D_{x'}\subseteq D_{x_+}\). The iterates
from \(\mu=0\) are holomorphic in \(w'\) and converge uniformly. So
\(s_*(w')\) is holomorphic, and implicit differentiation gives
\(s_*'=1/(1-\tau^2\alpha'(s_*))\).

The Gaussian average \(\mathcal G\) has no zero with
\(\operatorname{Re}w'>1\) (Lemma 3.1). Hence
\(\varepsilon(w')=(\mathcal G'/\mathcal G)(w')-(F'/F)(s_*(w'))\) is
holomorphic on the disk, and \(\lvert\varepsilon\rvert\le E\) there by
Proposition 4.5. Cauchy's estimate gives
\(\lvert\varepsilon'(w)\rvert\le\max\lvert\varepsilon\rvert/r\).

Since \(S=\tfrac12\operatorname{Re}(\mathcal G'/\mathcal G)(w)\) and
\(\partial w/\partial p=\tfrac12\),
\(\partial_pS=\tfrac14\operatorname{Re}\bigl[(F'/F)'(s_*)\,s_*'(w)+\varepsilon'(w)\bigr]\).
Finally
\(\lvert(F'/F)'(s)\rvert\le\lvert(\mathcal L'/\mathcal L)'(s)\rvert+\lvert\alpha'(s)\rvert\le K_2(\sigma)+a_*\),
by Lemma 4.1 with \(j=1\) and Lemma 4.2. \(\square\)

The disk condition matters for zeta at small heights. There the pole of
\(\alpha\) at \(s=1\) gives \(s_*\) branch points with
\(\operatorname{Re}w\) slightly above \(1\): about \(1.055\pm0.625i\) at
\(t=0.2\), as the subagent check of Section 10 found. Every use here is at
\(x\ge X\). In the records, the maximum over the circle is taken at its
leftmost point, \(p-2r\), and at the smallest \(\ell_*\). That rests on the
sampled monotonicity of note 01, so the evaluated bound is numerical.

## 3. The floors compared (numerical)

Record B evaluates both bounds at the paper's \(p=61/20\) and its \(X\)
(\(\ell_X=22.2866\)), on intervals \([t^-,t^+]\) of length \(1/200\).
The paper's bounds are its (31)–(32) with its own upper-bound inputs,
which reproduce its certified Table 3 entries (record A). Note 01's
bounds take the heat gain at \(t^-\) and \(E\) at \(t^+\), with \(r\) the
best of \(0.05,\dots,0.35\).

| \(t^-\) | main term | his \(C^*\) | note 01's \(C\) | his \(G^*\) | note 01's \(G\) | main term of \(G\) |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 5.2974 | 5.2903 | 5.2958 | 0.2340 | 0.2174 | 0.2094 |
| 0.05 | 5.3867 | 5.3603 | 5.3777 | 0.1738 | 0.1601 | 0.1217 |
| 0.10 | 5.4408 | 5.4193 | 5.4316 | 0.1121 | 0.1111 | 0.0771 |
| 0.15 | 5.4761 | 5.4607 | 5.4683 | 0.0735 | 0.0769 | 0.0517 |
| 0.195 | 5.4982 | 5.4869 | 5.4917 | 0.0520 | 0.0562 | 0.0374 |

The loss against the main term is \(0.007\)–\(0.026\) for the paper and
\(0.0016\)–\(0.0095\) for note 01. At \(p=301/100\), against his Table 2
(Proposition 8, steps of \(1/100\)), note 01's floor is larger by
\(0.012\) to \(0.025\).

These comparisons set a floating evaluation (note 01) against a certified
one (the paper's). Note 01's evaluation is not outward-rounded and rests on
sampled monotonicity. Its advantage is real only once certified.

## 4. Theorem 12 from the unconditional strip

**4.1 Where the half-plane enters.** The paper's Section 1.1 says the
hypothesis "fixes the initial value \(q_0=9/16\) of the strip comparison
in Theorem 12; the zero dynamics, the boundary input, the approximation on
\(3\le y\le6\), the kernel inequality, and all certificates are independent
of it". After Theorem 12 it calls the theorem "a general conversion
theorem … Any table satisfying the stated gates gives an explicit bound
\(t_n+q_n/2\)". Its Section 1.1 lists other half-planes only for
\(\sigma<1\). The proofs never use \(\sigma<1\), however, and \(\sigma=1\)
is the trivial strip.

The following was checked against the text (also by the subagent check):

- Lemma 2 uses the classical bound \(\lvert\operatorname{Im}z\rvert\le1\),
  not \(q_0\).
- Theorem 12's barrier argument needs \(Q_\varepsilon(0)>M(0)\), the
  classical strip theorem, Lemma 2, Polymath's Theorem 1.5(i) (Project 01,
  ledger H7) and backward Hermite splitting.
- Lemma 10 needs \(0<A_2<B\); its proof was rechecked here and holds for
  every \(A_2<B\).
- With \(q_0=1\): \(M(0)\le1\) because every zero of \(\xi\) has
  \(0<\operatorname{Re}s<1\); \(q_0<B=(61/20)^2=9.3025\); and the final time
  is below \(\tfrac15\).

**4.2 The table.** \(p=61/20\); \(t_i=i/200\); \(d_i=1/200\) for \(i<33\)
and \(d_{33}=391/100000\); \(q_{34}=1/25\). Each next height is the
following row's \(q_i\). The columns are \(10^6q_i\), \(10^4C_i\),
\(10^4G_i\), \(10^3\lambda_i\) and \(10^3\mu_i\).

| \(i\) | \(q\) | \(C\) | \(G\) | \(\lambda\) | \(\mu\) | \(i\) | \(q\) | \(C\) | \(G\) | \(\lambda\) | \(\mu\) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1000000 | 52902 | 2340 | 1474 | 481 | 17 | 356111 | 54036 | 1280 | 1804 | 1068 |
| 1 | 952036 | 52964 | 2322 | 1524 | 540 | 18 | 329670 | 54090 | 1225 | 1815 | 1096 |
| 2 | 904955 | 53031 | 2284 | 1574 | 609 | 19 | 304348 | 54143 | 1172 | 1824 | 1118 |
| 3 | 858867 | 53100 | 2234 | 1621 | 691 | 20 | 280116 | 54193 | 1122 | 1834 | 1139 |
| 4 | 813966 | 53172 | 2174 | 1644 | 738 | 21 | 256931 | 54242 | 1074 | 1844 | 1167 |
| 5 | 770525 | 53245 | 2107 | 1658 | 764 | 22 | 234774 | 54288 | 1028 | 1853 | 1188 |
| 6 | 728552 | 53318 | 2036 | 1671 | 788 | 23 | 213607 | 54334 | 985 | 1861 | 1208 |
| 7 | 688021 | 53390 | 1962 | 1684 | 815 | 24 | 193403 | 54377 | 944 | 1869 | 1227 |
| 8 | 648917 | 53462 | 1887 | 1698 | 841 | 25 | 174128 | 54419 | 905 | 1878 | 1255 |
| 9 | 611181 | 53533 | 1813 | 1710 | 865 | 26 | 155754 | 54459 | 867 | 1885 | 1273 |
| 10 | 574812 | 53602 | 1739 | 1723 | 892 | 27 | 138247 | 54498 | 832 | 1892 | 1291 |
| 11 | 539777 | 53670 | 1667 | 1735 | 916 | 28 | 121575 | 54536 | 798 | 1899 | 1308 |
| 12 | 506049 | 53736 | 1596 | 1748 | 944 | 29 | 105705 | 54572 | 766 | 1905 | 1325 |
| 13 | 473600 | 53800 | 1528 | 1759 | 967 | 30 | 90610 | 54606 | 736 | 1912 | 1341 |
| 14 | 442411 | 53862 | 1462 | 1771 | 995 | 31 | 76255 | 54640 | 707 | 1919 | 1367 |
| 15 | 412455 | 53922 | 1399 | 1782 | 1018 | 32 | 62616 | 54672 | 679 | 1925 | 1383 |
| 16 | 383698 | 53980 | 1338 | 1794 | 1046 | 33 | 49660 | 54703 | 653 | 1930 | 1397 |

How the rows were built (record C):

- The \(C_i\) and \(G_i\) are the paper's (31)–(32) with its upper-bound
  inputs on \([t_i,t_i+\tfrac1{200}]\), rounded down and up to \(10^{-4}\).
  They do not depend on \(q\). On rows 0–23 they coincide with the
  paper's certified Table 3 entries, except that \(G_6\) is \(10^{-4}\)
  larger here. The paper's row 23 covers \([0.115,0.11963]\); here row 23
  covers \([0.115,0.12]\) and is certified on that interval.
- \(\lambda_i\) and \(\mu_i\) maximize \(k_i\) of (33) over a sampled
  admissible region, reduced by \(0.005\) as the paper's rows are. They
  were then rounded and lowered until the exact Bernstein test passed.
- \(q_{i+1}\) is the barrier value rounded up.

**4.3 Checks (the certificate).**

- Exact rational arithmetic:
  - the chain;
  - every Bernstein coefficient of the compactified polynomial (34)–(35),
    eight subintervals, smallest \(1.4155\cdot10^{-3}\);
  - every \(k_i\), \(7.781\) to \(10.592\);
  - every gate, with \(E_{20}(k_id_i)\le e^{k_id_i}\), smallest margin
    \(1.079\cdot10^{-5}\);
  - the paper's two Section 8.2 inequalities, \(L/4>5.5716\) and
    \(N\ge69098\) for \(x\ge X\).
- Directed-rounding decimal arithmetic (32 digits; \(\exp\) and \(\ln\)
  moved one unit outward, other operations rounded toward the bound):
  \(C_i\le C^{\rm cert}\) and \(G_i\ge G^{\rm cert}\) on every row, with
  margins \(2.05\cdot10^{-6}\) and \(2.02\cdot10^{-6}\), and
  \(\varepsilon_0\le0.0191<\tfrac12\).
- Control: the same checks on the paper's Table 3 return its printed
  values exactly:
  - least Bernstein coefficient
    \(623287907570432169922330885087/479268282493202500000000000000000\) in
    row 21;
  - gate margin above \(2.78\cdot10^{-8}\);
  - scalar margins \(2.05\cdot10^{-6}\) and \(1.10\cdot10^{-6}\);
  - \(8.63<k_i<10.32\);
  - final time \(11963/100000\).

**4.4 Result.** *Conditional on the paper's Theorem 12, Lemma 10,
Proposition 11 (with its Lemma 3, Lemma 6, the normalizer bounds of its
Section 3 and its estimate (27)) and Lemma 2 (with Polymath's Section
8.4(a), the RH verification, Polymath's Proposition 3.1(ii) and de
Bruijn's theorem):*
\[
\Lambda\le t_{34}+\tfrac1{50}=\tfrac{16891}{100000}+\tfrac1{50}=\tfrac{18891}{100000}.
\]

Sensitivity (floating, record C): a step of \(1/400\) gives \(0.18850\), a
step of \(1/100\) gives \(0.18961\), and a polynomial margin of \(0.02\)
gives \(0.18982\). From \(q_0=1\) the Theorem 9 kernel does not reach
\(1/25\) by \(t=1/5\). The gain comes from Lemma 10.

**4.5 Thin places.**

- The scalar margins of about \(2\cdot10^{-6}\) are the paper's own. Rows
  0–22 reuse its values, so a correction to its constants would affect
  both tables alike.
- In row 0 the leading coefficient of the polynomial in \(D\),
  \(2-2\lambda_0+2\mu_0\), is \(0.014\). It is exact and positive.
- The smallest gate margin is \(1.08\cdot10^{-5}\).

**4.6 What this is not.**

- It is not a refereed result and not independent review.
- It is not a priority claim and not a record. Starting from the
  classical strip is already the approach of Gordon, Raymond and Planat,
  whose unrefereed claims are stronger (Section 11).
- The analytic content, above all the Riemann–Siegel estimates of
  Lemma 3 and the proof of Proposition 11, was read but not re-derived.

## 5. Planning with note 01's floors for zeta

Record D runs Theorems 9 and 12 with note 01's floors and Corollary 2.1 at
the paper's \(X\), inside Lemma 2's window \(t\le\tfrac15\), with steps of
\(1/200\). The values are \(\Lambda\) planning values; "–" means \(1/25\)
is not reached by \(t=\tfrac15\), or \(p^2<5q_0\) for Theorem 9.

| \(p\) | Thm 12, \(q_0=1\) | Thm 12, \(q_0=9/16\) | Thm 9, \(q_0=1\) | Thm 9, \(q_0=9/16\) |
| --- | --- | --- | --- | --- |
| 2.0 | 0.1953 | 0.1441 | – | 0.1491 |
| 2.25 | 0.1885 | 0.1382 | 0.2085 | 0.1524 |
| 2.5 | 0.1869 | **0.1370** | 0.2148 | 0.1561 |
| 2.75 | **0.1867** | 0.1374 | – | 0.1599 |
| 3.05 | 0.1882 | 0.1391 | – | 0.1643 |
| 3.5 | 0.1934 | 0.1424 | – | 0.1707 |

So note 01's floors improve the paper's own values (\(0.18891\) here and
its \(0.13963\)) by about \(0.002\)–\(0.003\). Heights below \(2.5\) do not
help, for two reasons. Lemma 10's polynomial leaves less room for
\(\lambda>1\) when \(B=p^2\) is small. And \(K_2\) grows as \(\sigma\)
approaches \(1\), which raises \(G\).

## 6. Project 01's Target A with the derivative kernel (planning)

Record E covers every primitive character of conductor \(q\), from
\(q_0=1\), with \(b\to0\). It uses note 01's family floors and Corollary
2.1. The reported value is the time at which the barrier reaches \(0\),
for the best \(p\) on a small grid.

| \(q\) | parity | Theorem 9 kernel | Theorem 12 kernel | change |
| --- | --- | --- | --- | --- |
| \(10^6\) | even | 0.3084 (\(p=2.5\)) | 0.2920 (\(p=4.0\)) | \(-5.3\%\) |
| \(10^6\) | odd | 0.2993 (2.5) | 0.2827 (3.5) | \(-5.5\%\) |
| \(10^8\) | even | 0.2511 (2.25) | 0.2344 (3.0) | \(-6.7\%\) |
| \(10^8\) | odd | 0.2448 (2.25) | 0.2268 (3.0) | \(-7.4\%\) |
| \(10^{12}\) | even | 0.1873 (2.25) | 0.1651 (2.5) | \(-11.9\%\) |
| \(10^{12}\) | odd | 0.1844 (2.25) | 0.1611 (2.5) | \(-12.6\%\) |

The Theorem 9 column agrees with note 01's record G to about \(0.001\).
The best \(p\) for the even character at \(q=10^6\) is at the edge of the
grid. These values remain conditional on H12, on a written comparison
theorem for the family (now with Lemma 10's kernel and the second exterior
input \(\partial_pS\le G\)) and on certification.

## 7. Consequences for note 01 and Project 01

- Item 6 of note 01's Section 9 is done here. Note 01's Section 7 asked
  "whether his comparison then improves, and how its finite region is
  closed". The finite region is closed by his Lemma 2 for \(t\le\tfrac15\),
  whatever \(q_0\). From the trivial strip, his own inputs give \(0.18891\)
  (Section 4), and note 01's floors move that by about \(0.002\) at the
  planning level (Section 5).
- Note 01's zeta rows used \(X=6\cdot10^{10}\). Its own Section 1 records
  the rounding; this note uses the paper's \(X=60000083951.5\).
- Project 01's planning values for Target A (its Section 4.6 and note 01's
  record G, both with the Theorem 9 kernel) are superseded at the planning
  level by Section 6. Its statement of Target A should allow Lemma 10's
  kernel, which adds \(\partial_pS\le G\) to the exterior input. Corollary
  2.1 supplies that from Theorem 4.6.

## 8. Premises, controls and patterns to avoid

The table is a statement about \(\zeta\) itself. It uses the Euler product
of \(\zeta\) inside Proposition 11, and zeta-specific published
computations, so the collision controls of
[summary 12](../../../../../result-summaries/12_collision_controls_and_screening.md)
are not in question. Four of the patterns in
[`avoid/`](../../../../../avoid/README.md), re-read for this note, apply:

- 06 and 16 (status and imports): the result is labelled conditional on
  the paper, and each imported statement is named with its location.
- 11 (certifying the known): \(0.18891\) is not forced by published
  results, whose best is \(0.2\).
- 05 (same-model checks): the subagent check of Section 10 is described as
  such.

## 9. Decisions and next bounded tasks

Recommendations to Edward, and to Codex as the auditor of this phase.

1. **Review order.** A review of round 1 should check note 01's
   Lemmas 3.1–3.3, Proposition 4.5 and Theorem 4.6, and this note's
   Corollary 2.1, before the table. Then it should check Section 4.1 (that
   \(q_0\) enters only at time zero) and replay the certificate. The table
   is only as good as the paper's Proposition 11 and Lemma 3, and its value
   is as a cross-check of the published-input route (Section 11).
2. **Note 01's certification, after that review.** Certify \(E\) and
   Corollary 2.1 with outward rounding. For zeta this means \(x\ge X\),
   \(p\in[2.5,3.05]\) and intervals \([t_i,t_i+\tfrac1{200}]\) with
   \(t_i\le0.17\). That would give a proof of the table's inputs that does
   not use Riemann–Siegel, and the planning value \(0.1867\). Stopping
   rule: wherever the certified floor falls below the paper's \(C_i\), keep
   the paper's row. The family certification for Project 01 matters more
   and uses the same machinery.
3. **Project 01.** Adopt Lemma 10 and Theorem 12 as the comparison for
   Target A, with exterior input the pair \((C_i,G_i)\) from note 01 and
   Corollary 2.1.
4. **Literature.** Done in Section 11. Planat's appendix on the paper's
   derivative comparison and Gomila's full text remain unread.
5. **Edward's decision:** whether to tell Hakimoglu-Brown about the table
   from \(q_0=1\). His paper cites Gordon, whose barrier already starts
   from the classical strip, so the point is a cross-check rather than a
   new idea.

## 10. Coverage, provenance and checks

**Read in full for this note:** the preprint (project copy) and the
`avoid/` index. Note 01, Project 01's note 01 and the result summaries were
read in this session for note 01.

**Records.**

- The comparison programme's record and the certificate regenerate byte
  for byte with Python 3.13.16 on x86_64 Linux; the replay on Edward's
  computer is reported in the [round-1 numerics README](../../numerics/round-1/README.md).
- Record A also reproduces:
  - the paper's one-step value (18), \(0.179727541426\);
  - its Table 2 gates (smallest \(1.2533\cdot10^{-7}\); the paper prints
    \(1.25\cdot10^{-7}\));
  - its Proposition 8 margins (smallest \(1.49\cdot10^{-6}\); the paper
    prints \(1.48\cdot10^{-6}\));
  - its Tables 6–7 entries, each printed value exceeding the recomputed one
    by \(0.03\) to \(0.97\) units of \(10^{-12}\).

**Subagent check.** A Claude subagent of this session, with its own code
(mpmath at 34 digits), did the following:

- read the paper with the Projects tool;
- confirmed that nothing in Lemmas 2, 3 and 10, Proposition 11 or Theorem
  12 uses the half-plane except through \(M(0)\le q_0\);
- recomputed every \(k_i\) and gate in exact rationals;
- certified the polynomial on all 34 rows by its own adaptive Bernstein
  scheme, with a different compactification;
- recomputed \(C^*\) and \(G^*\) on all rows, with the same smallest
  margins;
- re-ran the comparison from \(q_0=1\), reaching \(1/25\) at
  \(t\approx0.16865\);
- confirmed the crosswalk identities and the corollary's formulas.

It found the following, all corrected:

- Corollary 2.1 was first stated for all \(\operatorname{Re}w>1\), which
  fails for zeta at small heights.
- The dependency list in Section 4.4 was incomplete.
- "Unconditional" was the wrong word for the result.
- The certificate used Decimal powers, which Python documents only as
  "almost always" correctly rounded; they are now repeated directed
  multiplications.
- The paper's \(\sigma=1\) warnings concern only its closed formulas.

This check is the same model family as the author's and is not independent
review.

**Not done:**

- no re-derivation of the paper's Lemma 3 or Proposition 11;
- no replay of Polymath's boundary computation;
- no full reading of Gordon's, Raymond's, Planat's or Gomila's preprints
  (Section 11 says what was read);
- no certification of note 01's floors or of Corollary 2.1's evaluation;
- nothing was committed to git by this session.

## 11. Literature check (added later on 17 October 2026)

A second Claude subagent of this session searched the web and read what
it could fetch. Its quotations came through a summarizing fetch tool that
caps each excerpt. They were not checked against the full texts, so the
claims below are as the authors state them.

| Source | Claim and status | Relation to Section 4 |
| --- | --- | --- |
| S. Gordon, "A computer-assisted upper bound for the de Bruijn–Newman constant" (September 2026), [repository](https://github.com/stefangordon/dbn-upper-bound), [PDF](https://stefangordon.github.io/dbn-upper-bound/dbn-upper-bound.pdf) | \(\Lambda\le0.157656619\), no half-plane or RH hypothesis; "has not undergone external peer review"; uses Platt–Trudgian's verification to \(3\cdot10^{12}\) | zero dynamics of the highest zero, \(h'=-1/h-2\sum K_h\); a reference barrier with \(q_{\rm ref}(0)=(1000001/1000000)^2\), "the global strip gives strict entry at zero"; cites Polymath's Theorem 1.5(i). The same start, with its own analytic inputs and a far larger \(X\) |
| Raymond, "Correlated translated probes and the bound \(\Lambda<0.149396\)" (Zenodo, 21 September 2026), [record](https://zenodo.org/records/22867547) | \(\Lambda<0.149396\); "has not undergone external peer review" | "starts from the classical width-one zero strip at time zero"; 608 time cells |
| Planat, arXiv:2610.18214v1 (13 October 2026), [HTML](https://arxiv.org/html/2610.18214) | \(\Lambda\le0.148611789321711\) "under explicitly stated complete model-to-function source, localisation and global contact premises" | "a directed comparison beginning with the classical zero strip", using Raymond's source data; its Appendix A.1, on the paper's derivative comparison under the 7/8 hypothesis, could not be read |
| J. Gomila, [repository](https://github.com/judegomila/dbn-lambda-01787854-candidate-audit) and blog (August 2026) | \(\Lambda\le0.1787854\), "unconditional", "not yet been peer reviewed" | Polymath's Theorem 1.2 at \(X\approx6\cdot10^{12}\) with a barrier computation; no strip comparison; the PDF could not be parsed |
| Raymond, conditional (Zenodo, 10 October 2026) | \(\Lambda<0.116398\) assuming no zeros with \(\operatorname{Re}s>7/8\) | beats the paper's \(0.13963\) under the same hypothesis |

No later version of the paper was found, and nothing stating \(0.18891\)
or restarting the paper's Theorem 12 from \(q_0=1\) turned up.

**Imported inputs checked.**

- Platt's verification: D. Platt, Math. Comp. 86 (2017), 2449–2467,
  doi:10.1090/mcom/3198, isolates the zeros with imaginary part up to
  \(30{,}610{,}046{,}000\). That exceeds \((X+1)/2=30{,}000{,}041{,}976.25\)
  by about \(6\cdot10^8\).
- Polymath's Section 1 says the barrier region was replaced "with the
  larger and simpler region" \(X\le x\le X+1\), \(y_0\le y\le1\),
  \(0\le t\le t_0\), with \(t_0=0.2\), \(X=6\times10^{10}+83952-0.5\) and
  \(y_0=0.2\). This is the paper's (3). Polymath's Section 8.4 itself could
  not be fetched in full.
- Polymath's Theorem 1.5 holds for \(0<t\le\tfrac12\) with an absolute,
  non-explicit constant \(C\), as the barrier argument of Theorem 12 needs.

**Consequence.** Starting from the classical strip is not new. The
distinctive feature of Section 4 is that its numerical inputs are
published and independently verified computations (Polymath's barrier and
Platt's verification), with the paper's analytic lemmas on top, checked by
a 34-row certificate. The stronger claims rest on their authors' own
unrefereed computations. For Project 03 the zeta number is a cross-check.
The method of note 01 matters more for Project 01's Dirichlet family, for
which Project 01's search found no upper bound below \(\tfrac12\).
