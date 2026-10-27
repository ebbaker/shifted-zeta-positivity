# Rodgers–Tao energy at an RH endpoint: review, sharp bound, and simplicity

26 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**, reasoning effort **max**. This is a research note with same-assistant checking, not independent specialist review or a priority claim.

**Result.** The recent Rodgers–Tao work gives a correct, useful finite-cluster exterior-force interface and a reproducible two-zero certificate. The current Book already supplies a high-height field atlas through time zero; that domain gap should not be reopened. The earlier RH-simplicity investigation also already contains the multiple-zero energy expansion, complete exterior forcing, bounded spectral tests and endpoint controls.

Combining those inputs gives the following precise answer to the proposed extension. With ordered-pair energy, an isolated multiplicity-\(m\) endpoint has
\[
 E_m(t)=\frac{m(m-1)}{8t}+O(1).
\]
The finite-cluster dissipation identity implies the sharp upper allowance
\[
 E_m(t)\le
 \frac{2K C_m}{1-e^{-2Kt}}
 =\frac{C_m}{t}+K C_m+O(t),
 \qquad C_m=\frac{m(m-1)}8,
\]
when the derivative of the complete exterior drift is bounded by \(K\). **Its leading coefficient is exactly the collision coefficient.** It therefore gives no contradiction. The explicit Riccati bound is the additional calculation in this review; the endpoint expansion is credited to BW10 Note12, and the stronger Hermite spectral lower bound to HDC brainstorm Note12.

A contradiction still needs an independently proved estimate for the unchanged theta source that is strictly below the multiplicity cost. Neither fixed-regulator physical bounds, forward heat regularization, nor the reviewed finite exterior estimate supplies that estimate. This conclusion is limited to those inputs and deductions; it does not rule out a more arithmetic Rodgers–Tao-inspired argument.

## 1. Interpretation, scope and prior work

I interpret “RH \(\Rightarrow\) simple zeros” as assuming **RH and a multiple zero**, and seeking a contradiction. A contradiction from **RH and all zeros simple** would instead point in the opposite direction. Section 3 explains why \(\Lambda=0\), even combined with the Rodgers–Tao theorem, does not itself contradict all-simple endpoint zeros.

The review includes the current [Book and its nine sections][book], the recent [Rodgers–Tao notes][rt-home], the surrounding [heat-flow application analysis][app-threshold], and selected earlier investigations listed below. It is not a fresh audit of every inherited proof or of all conversations in those investigations. Source snapshots, actual execution checks and review limits are recorded in the [assessment][assessment] and [input record][inputs].

This note follows the [result summaries][results] and [patterns to avoid][avoid], especially [target classification][a01], [control screening][a02], [scope of negative results][a07] and [coupled estimates][a12]. The established [collision-control register][controls] is used in Section 9.

| Earlier home | What is already established there | Consequence for this review |
| --- | --- | --- |
| [BW10 Note12 §3][bw12] | Full multiplicity-\(m\) Hermite expansion, exterior finite part, logarithmically divergent endpoint energy; fixed-reference subtraction does not remove it. | Do not present the \(1/t\) collision cost or its compatible finite part as new. |
| [BW10 Note19][bw19] | Complete root motion, mirror and infinite exterior contributions, finite-time gap inequalities. | Deflate the whole colliding cluster, not just a selected pair in an \(m>2\) event. |
| [BW10 Note05][bw05] | Under RH, arbitrarily theta-close normalized positive sources with endpoint doubles and real/simple positive-time zeros, but without ordinary Dirichlet-series arithmetic. | Positivity, closeness, completion and forward real-root behavior do not suffice for simplicity. |
| [BW10 research home][bw-home] | Reciprocal extraction, Gevrey approximation, multiplicity-sensitive norm costs, normalized heat profiles and repair costs. | Smoothing or an accurate approximation must retain the multiplicity cost; a generic norm bound cannot silently replace it by the simple-zero coefficient. These are inherited in-note results, not newly reaudited theorems here. |
| [BW09 heat-flow contour/energy program][bw09] | Completed bounded comparisons, with the larger energy route awaiting an independent arithmetic input and complete payments. | This review does not reactivate that campaign merely by renaming its endpoint obligation. |
| [Reciprocal Hodge energy][rhe], [Chern–Hopf integral estimates][chern], [late heat caps][caps] | Finite signed estimates and transport accounting; small late caps do not erase the other boundary contributions. | Charge/energy conservation needs the full boundary and tail statement. |
| [HDC Note06][hdc06] and [Note10][hdc10] | Pair-matrix spectrum and the bounded filter \(q\), with limits \(m-H_m\), plus finite-time multiplicity consumers. | There is already a bounded alternative to divergent raw energy. |
| [HDC brainstorm Note12][hermite] | Complete-cluster Hermite domination and \(q(t)\ge\sum(m-H_m)\) at every allowed positive time. | An opposing upper bound is missing; the lower bound is not. |
| [HDC Notes11,12][forest] and [Note12][transport] | Coefficient-only filtered-spectrum enclosure and complete-source backward transport without internal gap denominators. | These are the existing acquisition interfaces to try before inventing another simplicity criterion. |
| [HDC brainstorm Note23][conservation] | Precise limits of complex-field conservation laws, including infinite theta spatial mass at fixed regulator and surviving polynomial collision controls. | Global finite-energy conservation cannot be imported without its hypotheses. |

## 2. Review of the recent Rodgers–Tao work

### 2.1 The finite interface is useful and keeps the correct quantities

[RT Note02][rt2] uses the canonical convention
\[
 H_t=-H_{zz},\qquad H(0,z)=\tfrac18\xi((1+iz)/2).
 \tag{2.1}
\]
For a complete finite real cluster with simple roots \(a_i(t)\), it factors
\[
 H=UP,\qquad P=\prod_i(z-a_i),\qquad D=2U_z/U
\]
and retains the whole exterior unit. Its exact identities are
\[
 a_i'=f_i+D(a_i),\quad
 f_i=2\sum_{j\ne i}\frac1{a_i-a_j},
 \qquad
 E=\sum_{i\ne j}\frac1{(a_i-a_j)^2}=\frac14\sum_i f_i^2,
 \tag{2.2}
\]
\[
 E'=-Q+B,\qquad
 Q=\frac12\sum_{i\ne j}
       \left(\frac{f_i-f_j}{a_i-a_j}\right)^2,\qquad
 B=-2\sum_{i\ne j}
       \frac{D(a_i)-D(a_j)}{(a_i-a_j)^3}.
 \tag{2.3}
\]
The contour projection of \(H_z/H\) recovers \(U_z/U\). Consequently its source-to-drift bound includes all omitted roots and analytic unit terms, without matching the model roots to the true roots.

In particular, \(\sup_J|(D_H-D_F)'|\le\kappa\) implies
\[
 |B_H-B_F[a]|\le2\kappa E.
 \tag{2.4}
\]
The model term is evaluated on the **same actual configuration** \(a\). A separate model-root dynamics argument would have to pay the model's heat residual and any divisions by its root slopes. The analogous renormalized energy error is not \(2\kappa\widetilde E\); RT Note02 keeps its different signed reference expression.

These are sound distinctions. An absolute field approximation is not by itself a contour floor, and a contour floor enclosing several roots is not a simplicity assertion. Both matter in the endpoint application.

### 2.2 What the completed two-zero pilot actually shows

[RT Note03][rt3] and its [certificate][rt-cert] use
\[
 t\in[1/20000,1/10000],\quad
 \Gamma=\partial([26,46]+i[-2,2]),\quad J=[28,43].
\]
The degree-95 canonical Taylor model with six heat terms encloses the complete source; the contour count is two and both roots are certified real/simple throughout this slab. No global RH assumption is needed.

I reran the unmodified certificate. All stored fields agree exactly after excluding elapsed/setup seconds. The added wall uncertainty \(10^{-6}\) correctly causes rejection before a new certificate is written. The [replay record][replay] distinguishes the original script's authoring metadata from this review's model and effort.

| Complete payment on that fixed slab | Reproduced upper allowance |
| --- | ---: |
| Canonical source error, each declared jet | \(<6\cdot10^{-27}\) |
| Canonical and model contour floors | \(>4.94\cdot10^{-7}\) |
| Contour-based exterior-force integral | \(1.103614\cdot10^{-5}\) |
| Direct root-jet exterior-force integral | \(3.565471\cdot10^{-8}\) |
| Contour/direct allowance ratio | \(309.5283\) |
| Coupled/separate source-transfer allowance ratio | \(6.88721\) |

Thus the source error is already negligible for this example; the complete model-drift estimate dominates the contour budget. The paired source comparison is also weaker than separate drift control on this particular wide-gap geometry. Neither observation is a universal ranking of the methods. The raw energy increases slightly, consistently with the included compressive exterior term.

The recorded conclusion is appropriately a **methods pilot in an already covered region**, not new zero coverage or a threshold theorem. I found no substantive discrepancy in these checked identities and execution results. A broader audit of the shared theta oracle and all imported analytic results was not performed.

## 3. What changes when the assumption is RH

The primary [Rodgers–Tao paper, corrected v5][rt-paper] proves \(\Lambda\ge0\) by working under \(\Lambda<0\). Its argument has an all-real/simple interval before the zeta slice, time for relaxation, and an arithmetic spacing contradiction at time zero. The corrected boundary accounting matters; RT Note02 records the relevant distinctions and reference payments.

Under RH, \(\Lambda\le0\), so the theorem gives \(\Lambda=0\). Real/simple evolution is available for every \(t>0\), but \(t=0\) is now a boundary of that regime. This reverses the position of the desired endpoint relative to the relaxation interval. A forward upper estimate propagates control to later times. It does not upper-bound the earlier singular endpoint by later regular data.

Nor does \(\Lambda=0\) force an attained finite multiple zero. If all zeros at time zero are simple, then on any fixed compact region with a zero-free boundary, the finitely many endpoint zeros continue as simple real zeros for sufficiently small signed time. Yet for every negative time there must be some nonreal zero. These two statements are compatible: those nonreal zeros can escape every fixed compact set as \(t\uparrow0\). There is no uniform compactness assertion at the zero threshold.

The local splitting statement and complete root law used below are classical; see [Polymath, v2, Proposition 3.1][poly-paper]. Their content is already developed in BW10 Notes12 and19. They do not require a positive-time root collision under RH.

## 4. Sharp finite-cluster dissipation

This section extracts an elementary quantitative consequence of (2.2)–(2.3). It strengthens the generic forward bound \(E'\le2KE\); it does not improve the canonical two-zero certificate or the published Rodgers–Tao large-block theorem.

**Proposition.** Let \(m\ge2\) simple real roots form a complete cluster on \(0<t\le T\), in a real interval on which the complete drift obeys
\[
 \sup |\partial_zD(t,z)|\le K,\qquad K\ge0.
 \tag{4.1}
\]
Assume (2.2)–(2.3) there. Set \(C_m=m(m-1)/8\). Then
\[
 Q\ge\frac{E^2}{C_m},\qquad
 E'\le-\frac{E^2}{C_m}+2KE.
 \tag{4.2}
\]
For \(0<s<t\le T\), when \(K>0\),
\[
 \frac1{E(t)}\ge
 \frac{e^{-2K(t-s)}}{E(s)}
 +\frac{1-e^{-2K(t-s)}}{2KC_m}.
 \tag{4.3}
\]
If (4.1) holds down to time zero for the whole isolated cluster, then
\[
 \boxed{\ E(t)\le\frac{2KC_m}{1-e^{-2Kt}}\ }.
 \tag{4.4}
\]
At \(K=0\) these formulas mean
\[
 E(t)^{-1}\ge E(s)^{-1}+(t-s)/C_m,\qquad E(t)\le C_m/t.
 \tag{4.5}
\]

**Proof.** Put \(A_{ij}=(f_i-f_j)/(a_i-a_j)\) for \(i<j\), and \(M=m(m-1)/2\). The orientation cancels, and
\[
 \sum_{i<j}A_{ij}
 =\sum_i f_i\sum_{j\ne i}\frac1{a_i-a_j}
 =\tfrac12\sum_i f_i^2=2E.
\]
Since \(Q=\sum_{i<j}A_{ij}^2\), Cauchy–Schwarz gives
\(Q\ge4E^2/M=E^2/C_m\). The mean-value estimate in (4.1) gives \(|B|\le2KE\). This proves (4.2).

Writing \(y=1/E>0\) yields \(y'+2Ky\ge1/C_m\). Integration proves (4.3). Dropping its nonnegative initial term and taking \(s\downarrow0\) gives (4.4); no finite value \(E(0)\) was assumed. The \(K=0\) limit gives (4.5). □

**Sharpness.** The exact heat polynomial
\[
 P_m(t,z)=e^{-t\partial_z^2}z^m
 =(2t)^{m/2}\operatorname{He}_m(z/\sqrt{2t})
 \tag{4.6}
\]
has roots \(a_i=\sqrt{2t}\lambda_i\), where \(\operatorname{He}_m\) is the monic probabilists' Hermite polynomial. Here \(D=0\),
\[
 f_i=\frac{a_i}{2t},\qquad A_{ij}=\frac1{2t},\qquad
 E=C_m/t,\qquad Q=C_m/t^2.
 \tag{4.7}
\]
Every inequality in (4.2)–(4.5) is an equality. Thus the coefficient cannot be decreased for this class of complete finite root equations, even with zero exterior-force error.

For an isolated actual multiple endpoint, a fixed enclosing zero-free wall exists locally and Weierstrass preparation makes \(U\) analytic and nonvanishing through \(t=0\). Hence some finite local \(K\) exists. Making that \(K\) effective is an acquisition problem, but merely bounding it cannot change the coefficient of \(1/t\).

## 5. The endpoint expansion was already known, and matches exactly

Assume RH and an order-\(m\) zero at \(a>0\). Use the notation of [BW10 Note12 §3][bw12]:
\[
 g(z)=H(0,z)/(z-a)^m,\quad
 \ell=g'(a)/g(a),\quad
 S=-(\log|g|)''(a)
   =\sum_{r\ne a}\frac{m_r}{(a-r)^2}>0.
 \tag{5.1}
\]
The sum runs over all distinct real endpoint sites, with their multiplicities; it includes the mirror site. Locally \(D(0,a)=2\ell\), \(D_z(0,a)=-2S\).

With \(\tau=\sqrt{2t}\), that note proves
\[
 a_i(t)=a+\tau\lambda_i+\ell\tau^2
             -\tfrac S2\lambda_i\tau^3+O(\tau^4).
 \tag{5.2}
\]
Its **unordered** energy is \(M/(8t)+MS/4+O(t)\). Converting to the ordered convention in the recent RT work gives
\[
 \boxed{\ E_m(t)=\frac{C_m}{t}+2C_m S+O(t).\ }
 \tag{5.3}
\]
The integer-power remainder follows from the analyticity of the prepared polynomial coefficients and the meromorphic symmetric root expression; termwise root expansions alone would give a less precise remainder.

Comparison with (4.4) is completely consistent. On a shrinking local time/spatial neighborhood, the acquired derivative allowance can approach \(2S\), so its constant term \(K C_m\) approaches the same \(2C_mS\). The exterior compression does not supply an opposing sign.

For an exact double the equivalent gap formula is
\[
 (a_2-a_1)^2=8t-16S t^2+O(t^3).
 \tag{5.4}
\]
For \(m>2\), treating the other \(m-2\) descendants as a bounded exterior is invalid: their distances are also \(O(\sqrt t)\). Preparation of the whole cluster is essential.

There is an even stronger already available lower estimate. [HDC brainstorm Note12][hermite] compares the complete real-root dynamics with the free Hermite cluster:
\[
 a_{i+1}(t)-a_i(t)
 \le\sqrt{2t}(\lambda_{i+1}-\lambda_i).
 \tag{5.5}
\]
It uses every external root with its compressive sign. Summing consecutive gaps gives all-pair comparison, hence
\[
 \frac{C_m}{t}\le E_m(t)
 \le\frac{2KC_m}{1-e^{-2Kt}}
 \tag{5.6}
\]
on the local interval where (4.1) also holds. This is a compatible sandwich, not a contradiction.

### Discriminant accounting and the exact logarithmic cost

Let
\[
 \Delta(t)=\prod_{i<j}(a_j-a_i)^2,\qquad
 R_D(t)=2\sum_{i<j}\frac{D(a_i)-D(a_j)}{a_i-a_j}.
\]
Then (2.2) gives
\[
 (\log\Delta)'=4E+R_D,\qquad
 |R_D|\le m(m-1)K,
 \tag{5.7}
\]
and therefore
\[
 \int_\varepsilon^T E(t)\,dt
 =\tfrac14\log\frac{\Delta(T)}{\Delta(\varepsilon)}
       -\tfrac14\int_\varepsilon^T R_D(t)\,dt.
 \tag{5.8}
\]
This is the discriminant form of BW10 Note12's log-gap identity, with the ordered/unordered factor made explicit.

For one multiplicity-\(m\) site,
\[
 \Delta(t)=(2t)^M
   \prod_{i<j}(\lambda_j-\lambda_i)^2\,[1+O(t)],
 \qquad M=\binom m2.
 \tag{5.9}
\]
Thus \(\int_\varepsilon^T E=C_m\log(T/\varepsilon)+O(1)\). Fixed distinct reference gaps remove only bounded terms; the divergence survives the RT-type fixed-reference renormalization. Subtracting the universal collision term removes the divergence but also removes the proposed signal, leaving the compatible finite part (5.3).

For a fixed finite population containing whole endpoint sites \(a_\nu\), with multiplicities \(m_\nu\), cross-site terms stay bounded. Hence
\[
 \lim_{\varepsilon\downarrow0}
 \frac{\int_\varepsilon^T E(t)\,dt}{\log(T/\varepsilon)}
 =\sum_\nu\frac{m_\nu(m_\nu-1)}8.
 \tag{5.10}
\]
Four times this coefficient is \(\sum_\nu\binom{m_\nu}{2}\), the familiar local discriminant/charge count. It is another encoding of the existing signal.

A logarithmic coefficient strictly below \(1/4\) on every such covered window would exclude every multiple zero; the smallest nonzero contribution is a double. Likewise finite \(\int_0^T E\) is equivalent to simplicity on a fixed finite endpoint population. These are **final-strength reformulations under RH**, not independently proved bounds or intermediate evidence. They are recorded once to specify what the proposed contradiction would need.

## 6. What the current Book supplies, including work through zero

The inspected Book is the **B02 r2** synthesis described in its [README][book-readme]. Its current positive atlas incorporates the returns in Summary67. Earlier reviews of older manuscript states must not be treated as the current approximation baseline.

| Book input | Present scope relevant here | What it does not yet supply |
| --- | --- | --- |
| [Canonical and crossover chapters][book-crossover], retained-arithmetic [Ansatz Note26][ans26] | High-height field approximation on \(0\le t\le T_*\) for each fixed finite \(T_*\), retaining the arithmetic modes and the complete remainder. On \(4/L\le t\le1\), the normalized allowance is \(\epsilon_X=(1+\log X)^2X^{-3/4}\), with \(L^j\) spatial-jet and \(L^2\) time losses; the near-zero crossover covers \(0\le tL\le8\). | A lower first-jet margin, a discriminant lower bound, or a theta upper bound below (5.10). |
| [Negative chapter][book-negative] and recurrence companion | Strong negative endpoint hierarchy in its stated region, with order-dependent onset; signed crossover separately reaches microscopic times with a weaker allowance. | The strong negative estimate at every smaller time merely by taking its formula to zero. |
| [Positive hierarchy][book-positive] | Arbitrary fixed saddle order, high-height bounds for \(t\ge32\), compact overlaps and an eventual all-height onset depending on order. | A uniform near-zero collision exclusion from late-time simplicity. |
| [Physical chapter][book-physical] and [global construction][book-global] | Exact identities and regulated/smoothed approximation with source, residual and spatial joining terms retained; fixed-P4 switch consumer is included. | Uniform control after removing the physical regulator, or an identified equality between the physical covariance and RT inverse-gap energy. |
| [Effectivity chapter][book-effectivity] | Finite source construction and evaluation with declared order, height, precision and input restrictions. | An unproved favorable margin or an inexpensive joint endpoint/height limit. |
| Later [Note71][n71] and [Note72][n72] | Weak-filter puncture accounting and improved acquisition/evaluation cost on the specified late positive seam family; Note72 gives polynomial sufficient work in numerical height and requested bits with uninstantiated constants. | A time-zero multiplicity estimate. The central possible multiple-event region still has its fixed positive regulator; the outer simple-root pole estimate does not apply to an unregulated central double pole. |

[Note73][n73] further improves query cost to polynomial in binary height on certified pure-P exterior supports of that same late-time family. It retains the actual residual and weak-filter payments, and charges global construction separately. This is a scoped evaluation improvement, with no time-zero sign or multiplicity conclusion.

Here \(L=\log(X/(4\pi))\). The details are output- and domain-dependent; this table is a consumer review, not a replacement statement of the Book's theorems.

Three distinctions are decisive.

**Field accuracy versus collision-scale accuracy.** On a shrinking heat chart,
\[
 H(t,a+\sqrt{2t}\,w)
 =g(a)(2t)^{m/2}\{\operatorname{He}_m(w)+O(\sqrt t)\}.
 \tag{6.1}
\]
To transfer this normalized profile by an absolute approximation error \(\delta_0\), a sufficient requirement is
\(\delta_0=o(|g(a)|t^{m/2})\); for its first spatial derivative the corresponding requirement is
\(\delta_1=o(|g(a)|t^{(m-1)/2})\).
A fixed-height field error, even a very small one, cannot be treated as satisfying these conditions as \(t\downarrow0\). In carrier-normalized Book variables, divide both the errors and \(g(a)\) by the same carrier. Increasing height and decreasing time requires an explicitly uniform coupled estimate.

These conditions concern a shrinking normalized profile, not the existence of a fixed enclosing wall. Complete-cluster wall and coefficient methods can avoid individual gap denominators, as the earlier work demonstrates. They still need an informative upper value for the endpoint-sensitive observable.

**The physical observable is different.** The Book's covariance
\[
 \mathcal Q=K*(S_x^2-S_y^2)-(U_x^2-U_y^2)
\]
uses its declared smoothed variables and kernel. It is not \(Q\) in (2.3), nor \(E\), nor the pair-matrix filter below. Its regulator and mean terms cannot be dropped. In the small-positive regime the physical construction keeps a fixed positive regulator; its finiteness through a collision is consistent with (5.3). A uniform unregulated estimate and a proved bridge to the pair quantity would be additional mathematics.

**Conservation needs its actual hypotheses.** HDC brainstorm Note23 already identifies the obstruction to importing finite total-mass global identities for the whole transcendental theta field at fixed regulator. Local balances keep flux and late-cap faces; a finite polynomial heat collision can satisfy the corresponding admissible identities. Neither global conservation nor an asymptotically small selected cap pays the missing endpoint inequality.

## 7. Reuse the bounded spectral test

For a complete finite real population, the existing pair Laplacian and filter are
\[
 L_x=\sum_{i<j}\frac{(e_i-e_j)(e_i-e_j)^T}{(a_i-a_j)^2},
 \qquad
 q(t)=\operatorname{tr}\{4tL_x(I+4tL_x)^{-1}\}.
 \tag{7.1}
\]
Its trace before filtering is the ordered energy \(E\). If a site of multiplicity \(m\) is born at zero, the eigenvalues of \(tL_x\) in its limiting block are
\(0,1/4,\ldots,(m-1)/4\). Thus
\[
 q(0+)=\sum_\nu(m_\nu-H_{m_\nu}),\qquad
 H_m=\sum_{j=1}^m1/j.
 \tag{7.2}
\]
For complete endpoint clusters under the full real-root law, [Hermite domination][hermite] already proves the stronger statement
\[
 q(t)\ge\sum_\nu(m_\nu-H_{m_\nu})
 \tag{7.3}
\]
at each permitted positive time.

| Multiplicity | Ordered energy coefficient \(C_m\) | Discriminant time order | Filter cost \(m-H_m\) |
| ---: | ---: | ---: | ---: |
| 2 | \(1/4\) | 1 | \(1/2\) |
| 3 | \(3/4\) | 3 | \(7/6\) |
| 4 | \(3/2\) | 6 | \(23/12\) |

Accordingly an independently certified \(q(t)<1/2\) excludes any multiple site in a complete covered population. The existing bound on the number of labels belonging to nonsimple sites is \(M_{\rm ns}\le4q(t)\). An estimate \(q=o(N)\) for growing populations would therefore give density-one simplicity, but would allow isolated or zero-density multiple sites. These are different goals.

Two existing limitations must remain visible.

First, a late, nearly equally spaced population can have a large value of \(q\). At the established very-high-height positive-time onset, the dimensionless scale \(4t/\text{(mean gap)}^2\) is large, so the filter is near saturation per mode. Late regularity is not an early upper bound below \(1/2\).

Second, even simple endpoints have no universal time schedule derived just from simplicity. For
\[
 H_a(t,z)=z^2-a^2-2t,\qquad a>0,
\]
one has
\[
 q_a(t)=\frac{2t}{a^2+4t}.
 \tag{7.4}
\]
It tends to zero for each fixed \(a\), but tends to \(1/2\) along \(a^2=o(t)\). The fixed-population limit and a growing-height/small-time limit cannot be interchanged without additional control.

The [forest-polynomial theorem][forest] writes this scalar filter as a rational function of the complete prepared coefficients, and retains a coupled numerator/denominator residual. It has a genuinely gap-free double-collision neighborhood. It does **not** supply a nonvanishing denominator at every higher collision or a holomorphic extension through every complex coefficient approach. The [complete-source transport theorem][transport] gives a finite nilpotent coefficient propagator through internal events, provided its enclosing wall, source quotients and reference defect are paid. Both are relevant advances already in hand.

## 8. The concrete missing calculation

A useful continuation would combine the Book's retained-arithmetic approximation with those existing coefficient/filter interfaces. Its output must be a **complete upper number or bound**, not just smaller field error.

For a finite experiment, declare the complete population, common time, enclosing wall and endpoint coverage first. Use the unchanged canonical field to acquire the coefficient uncertainties and all exterior/source residuals. Then evaluate the correlated forest quotient with its actual denominator test, and compare the complete filter allowance against the existing direct first-jet certificate on the same data. A strict \(q<1/2\) with full coverage would be a finite exclusion; a cheaper or wider certificate would be an intermediate gain. A known-simple two-root box can test the implementation but is not new mathematical coverage.

For a theorem covering all zeros, the missing arithmetic estimate has to defeat the threshold at every relevant endpoint site, with a finite low-height core and the high-height quantifiers explicitly handled. An average in a height window can yield a proportion result without eliminating sparse multiple zeros. The logarithmic-energy statement (5.10) and the bounded test (7.3) are already final-strength consumers; repeating them is not progress toward their input.

The present review does **not** propose more late saddle terms as the immediate answer. The RT pilot's complete contour budget is dominated by model drift rather than source truncation, and the endpoint coefficient is already exact. Improving approximation is justified when a named complete consumer shows which error, margin or cost will improve. Equally, this is not a claim that the broader approximation program should stop.

## 9. Control screen and scope of the conclusion

This is an analytic screen against the existing controls, not a rerun of their numerical certificates.

| Control | Behavior under the calculation | Precise implication or failed premise |
| --- | --- | --- |
| Exact Hermite heat polynomial (4.6) | Attains the sharp Riccati bound and has the full multiple-endpoint signal. | Satisfies the finite root-equation hypotheses; fails the canonical theta source premise. It proves sharpness for the generic estimate. |
| RH-conditional theta-close normalized sources, BW10 Note05 | Have endpoint doubles despite real/simple positive-time evolution and arbitrarily close stated finite source/jet data. | Fail ordinary Dirichlet-series arithmetic. They rule out inference from those shared analytic data alone, not estimates using the unchanged coefficients. |
| Euler-factor family with \(c=1\) | Under RH its factor \(1+\cos(az)\) supplies endpoint double zeros, with the all-real threshold property. | Changes the arithmetic coefficients and conductor. The \(0<c<1\) family instead has nonreal factor zeros and fails endpoint RH; do not conflate them. |
| Weighted-square and finite-tail controls | Their certified local collisions do not create a complete all-real canonical interval. | The source-measurement audit shows these finite-tail families have nonreal zeros at every real time; they fail the all-real premise used for (5.5)/(7.3), as well as unchanged theta completion/reflection. |
| Reflected, smooth log-concave and positive-primitive controls | Screen arguments based only on reflection, positivity, primitive endpoints or shape. | Lack full theta arithmetic. Their local collision evidence must not be promoted to an unproved complete RH-like interval. |
| Finite-prime and finite-profile controls | Preserve their specified finite constraints while retaining events. | Fail the full unmodified arithmetic/profile premise; they do not establish a uniform canonical endpoint statement. |

The new generic inequality is **compatible with collisions** and is not intended to reject these controls. Any proposed strict arithmetic upper bound must distinguish the controls satisfying its analytic assumptions by a genuine additional premise and estimate. Merely saying “theta is special” would not supply that estimate.

The scoped conclusion is therefore: the reviewed finite RT dissipation, complete exterior control, Book field/regulated-physical bounds and forward relaxation do not, in their present forms, contradict an RH multiple endpoint. The already established spectral and coefficient machinery gives a concrete place to seek a stronger arithmetic input. No implication RH \(\Rightarrow\) simplicity, converse contradiction, new Newman bound, or new zero-exclusion region has been proved here.

## 10. Verification and provenance

The [exact algebra check][check-script] uses rational arithmetic to verify the finite force/energy identities on six configurations and the normalization of Hermite heat polynomials of multiplicity 2 through 8 at three rational times. It checks the discriminant power and polynomial differential equation without numerical root finding. Its [record][check-record] is a normalization check, not numerical evidence for simplicity.

The [separate assessment][assessment] records the RT replay, adversarial rejection, source inspection scope, and mathematical self-review. Third-party primary references reuse the parent reference catalog; see [reference notes][references]. No third-party PDF or generated manuscript snapshot was added. Other active investigations and their progress statuses were left unchanged.

[a01]: ../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[ans26]: ../../../01_heat_density_asymptotics/ansatz/notes/26_RETAINED_ARITHMETIC_MOVING_POSITIVE_BAND_20261026.md
[app-threshold]: ../../notes/02_RODGERS_TAO_POSITIVE_THRESHOLD_20261026.md
[assessment]: ../reviews/01_REVIEW_AND_ENDPOINT_CALCULATION_ASSESSMENT_20261026.md
[avoid]: ../../../../../avoid/README.md
[book]: ../../../01_heat_density_asymptotics/book/main.tex
[book-crossover]: ../../../01_heat_density_asymptotics/book/sections/03_crossover.tex
[book-effectivity]: ../../../01_heat_density_asymptotics/book/sections/07_effectivity.tex
[book-global]: ../../../01_heat_density_asymptotics/book/sections/06_global.tex
[book-negative]: ../../../01_heat_density_asymptotics/book/sections/02_negative.tex
[book-physical]: ../../../01_heat_density_asymptotics/book/sections/05_physical.tex
[book-positive]: ../../../01_heat_density_asymptotics/book/sections/04_positive.tex
[book-readme]: ../../../01_heat_density_asymptotics/book/README.md
[bw-home]: ../../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/README.md
[bw05]: ../../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/notes/05_CLOSE_POSITIVE_SOURCES_AND_NORMALIZED_DOUBLE_ZEROS_20261020.md
[bw09]: ../../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/09_expanding_contour_later_collision/research-overview/02_HEAT_FLOW_CONTOUR_AND_ENERGY_PROGRAM_20261020.md
[bw12]: ../../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/notes/12_FINITE_EVALUATION_AND_ENDPOINT_INVERSE_COSTS_20261020.md
[bw19]: ../../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/notes/19_COMPLETE_ROOT_MOTION_AND_FINITE_TIME_BOUNDS_20261021.md
[caps]: ../../../../investigations-4/11_late_heat_caps_and_charge_transport/README.md
[check-record]: ../numerics/ENDPOINT_ENERGY_EXACT_CHECKS_20261026.json
[check-script]: ../numerics/check_endpoint_energy.py
[chern]: ../../../../investigations-4/10_chern_hopf_integral_estimates/README.md
[conservation]: ../../../../investigations-4/12_height_dependent_heat_contours/brainstorm/notes/23_COMPLEX_FIELD_BOOK_AND_CONSERVATION_LAWS_20261024.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[forest]: ../../../../investigations-4/12_height_dependent_heat_contours/notes/11_FOREST_POLYNOMIAL_AND_GAP_FREE_FILTER_ENCLOSURE_20261023.md
[hdc06]: ../../../../investigations-4/12_height_dependent_heat_contours/notes/06_PAIR_MATRIX_SPECTRUM_AND_ENDPOINT_MULTIPLICITY_20261023.md
[hdc10]: ../../../../investigations-4/12_height_dependent_heat_contours/notes/10_EXACT_COLLISION_SPECTRUM_AND_GLOBAL_REDUCTION_20261023.md
[hermite]: ../../../../investigations-4/12_height_dependent_heat_contours/brainstorm/notes/12_HERMITE_CLUSTER_DOMINATION_AND_JOINT_CONSUMER_20261023.md
[inputs]: 01_REVIEW_INPUTS_20261026.json
[n71]: ../../../01_heat_density_asymptotics/notes/71_WEAK_FILTER_PUNCTURE_CONSUMER_20261026.md
[n72]: ../../../01_heat_density_asymptotics/notes/72_GRADED_WEAK_FILTER_AND_ACQUISITION_COST_20261026.md
[poly-paper]: https://arxiv.org/html/1904.12438v2
[references]: ../references/README.md
[replay]: ../numerics/RT_R2_REPLAY_20261026.json
[results]: ../../../../../result-summaries/README.md
[rhe]: ../../../../investigations-4/09_reciprocal_hodge_energy/README.md
[rt-cert]: ../../rodgers_tao/numerics/R2_CANONICAL_TWO_ROOT_CERTIFICATE_20261026.json
[rt-home]: ../../rodgers_tao/README.md
[rt-paper]: https://arxiv.org/html/1801.05914v5
[rt2]: ../../rodgers_tao/notes/02_CORRECTED_PROPAGATION_AND_CONTOUR_FORCE_TRANSFER_20261026.md
[rt3]: ../../rodgers_tao/notes/03_CANONICAL_TWO_ROOT_MARGINS_AND_FORCE_BUDGET_20261026.md
[transport]: ../../../../investigations-4/12_height_dependent_heat_contours/notes/12_COUPLED_COEFFICIENT_BACKWARD_TRANSPORT_20261023.md

[n73]: ../../../01_heat_density_asymptotics/notes/73_BINARY_HEIGHT_PURE_P_EXTERIOR_COST_20261026.md
