# J-E01 r2: signed averaging audit and Q10/P7 feasibility return

1 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual recorded model **gpt-6.1-sol (Codex)**,
reasoning effort **ultra**.

**Complete bounded supportive return.** The conditional signed-averaging
argument passes, including the FKG limit, Gaussian equality and index
comparison. Exact Q10 algebra proves \(J(0)>0\), so the new \(K\) is
positive near zero. The P7 tail calculation gives
\(K\sim3\cdot2^{30}t^7>0\), \(t=\pi e^{4u}\), after the leading
cancellation. The global requirements \(R'>0\), \(K\ge0\) remain
unproved. **Next: [B] J-B02 — Astra**, for that global estimate.

| Frozen r2 item | Audited outcome |
| --- | --- |
| Determinant factorization, simplex normalization, lattice/FKG argument | Pass, with the stated integrability and monotonicity hypotheses |
| Gaussian equality | \(h=1\), \(A_k=1\) for every \(k\) |
| Origin, at most Q10 | \(J(0)>0\) by exact rational polynomial signs; \(K>0\) near zero |
| Tail, at most P7 | \(K=3\cdot2^{30}t^7+O(t^6)+O(t^{11}e^{-3t})>0\) eventually |
| Canonical application on the full half-line | Still conditional; no compact-region proof or effective cutoff |

## 1. Contract and provenance

This executes [Note05 Section 7, J-E01 r2][request] without changing its
hypotheses or conclusion. The request-bearing Note05 has SHA-256
`32f8289741bac117b45399855558b554e1f1430adc7169a8229bfd69448e3cf2`.
HEAD is `c97b376dcbf81f05ea3a4f7d360da168af4a1345`; the inputs include
working-tree research files. The [r1 return][r1] and its program/record
remain byte-identical to the versions frozen in Note05. In particular,
the negative origin sign of \(C\) is retained.

The [new program][code] reuses the hash-checked r1 rational-polynomial
routines without editing them. It generates only Q0–Q10 and P0–P7.
The [exact record][record] includes full signed polynomial coefficients,
the complete mixed numerator, input/code hashes and all exact checks.
It records all 16 coefficients of the translated endpoint numerator.
The actual overview hash before this return's navigation update is
`df12068bb9dbf0e715b5548ed32527ed13ddddf4e6d3772d44a8dbf671abd679`;
the Active register hash is
`0831f8792cf43aa361fca084cab9192f47fcb88394410fe073ec08480eae0194`.

No numerical theta acquisition, source grid, compact certificate,
quadrature, theta-minor computation or higher-order test was performed.
The preferred exact sign proof suffices, so neither optional precision
level was used. There were no corrections to the frozen argument and
no unresolved bounded item. Checks are same-session, same-model LLM
contributing checks with shared inputs, not independent specialist review.

Read with the [result index][results], especially [theta identities][theta]
and [controls][controls], and the [avoid index][avoid], especially
[joint estimates][joint], [normalization][normalization],
[scoped exclusions][scopes] and [unchecked imports][imports]. This is a
fixed-order conditional mechanism and a feasibility result, not evidence
for a complete RH-equivalent criterion or a new coefficient range.

## 2. Conditional averaging proof

Use Note05's unchanged notation
\(F_k=(2k)!(2k+2)!(2k+4)!\),
\(M_k=F_kD_{3,k}\), \(\Omega=\{0<u_1<u_2<u_3\}\).
Assume globally \(R'>0\), so \(T=g(R)\). Determinant orientation is
\[
\det[1;y_j;g(y_j)]_{j=1}^3
=V(\mathbf y)g[y_1,y_2,y_3].
\]
It gives exactly
\[
\Delta_3=\prod_i\Phi(u_i)V(R(\mathbf u))h(\mathbf u),\qquad
M_k=\int_\Omega w_kh,\quad A_k=M_k/Z_k,
\]
with \(h=g[R(u_1),R(u_2),R(u_3)]\) and the positive weight \(w_k\)
in Note05 (4). No absolute value is inserted into this factorization.

The Genocchi–Hermite formula, [de Boor (52), p.64][deboor], becomes
\[
h=\int_{s,t\ge0,\ s+t\le1}
g''((1-s-t)R(u_1)+sR(u_2)+tR(u_3))\,dt\,ds.
\tag{1}
\]
Its simplex has area \(1/2\). Thus \(g'''\ge0\), together with \(R'>0\),
makes \(h\) increasing in each source coordinate, even when it is
negative. The nested-simplex convention in the primary source and (1)
are related by a linear substitution of unit Jacobian.

For a pair of crossed transformed endpoints \(a\le c<d\le b\),
the pair-factor meet/join difference is
\[
(d-a)(b-c)-(b-a)(d-c)=(c-a)(b-d)\ge0.
\tag{2}
\]
Aligned pairs give equality. Apply (2) for each pair of coordinates,
first to \(f(u)=u^2\) and then to \(f(u)=R(u)\). Single-coordinate
source and power factors satisfy equality under meet/join. This proves
the multiplicative lattice inequality for \(w_k\); source concavity
does not enter this step.

The strictly ordered grid in \([\varepsilon,L]^3\) really is a
distributive sublattice of the product of three finite chains. For a
meet, choose the vector attaining the later coordinate; its earlier
coordinate bounds the meet's earlier coordinate strictly below the later
one. For a join, choose the vector attaining the earlier coordinate.
Thus both operations preserve strict order. Positive grid weights
satisfy precisely [FKG Proposition 1, p.91][fkg]. Increasing real
functions in that theorem may take negative values.

On each such compact set, \(g\) is smooth and its divided difference
extends continuously across coincident nodes. The weights, observables
and their products are bounded and Riemann integrable. FKG therefore
passes from equally spaced grids to compact integrals. For an integer
\(\ell\ge0\), use the increasing tilt
\(q_\ell=(u_1u_2u_3)^{2\ell}\), with \(w_{k+\ell}=q_\ell w_k\).
Pass next to \(\varepsilon\downarrow0,L\uparrow\infty\) in the
unnormalized inequality:
\[
Z_k M_{k+\ell}\ge Z_{k+\ell}M_k. \tag{3}
\]
The four required integrals are exactly \(Z_k,Z_{k+\ell},M_k,M_{k+\ell}\).
Their absolute convergence, not global boundedness or positivity of
\(h\), justifies this exhaustion.

For canonical theta conditional on \(R'>0\), \(R\) is regular at zero
and \(R=O(t^2)\) at infinity. Expanding the two Vandermondes in \(Z_k\)
gives products of polynomially weighted moments of \(\Phi\) and \(R\),
all convergent by the full theta decay. Also, exactly,
\[
w_k|h|=\Bigl(\prod_i u_i^{2k}\Bigr)V(\mathbf u^2)|\Delta_3|,
\]
whose integral was paid in r1. The same statements apply at \(k+\ell\).
Strict positivity of \(Z_k\) follows in the ordered interior.

Dividing (3) by \(Z_kZ_{k+\ell}>0\) verifies the covariance/tilt identity
and \(A_{k+\ell}\ge A_k\). The r1 boundary identity gives
\(M_0=0!2!4!c_0^3=48c_0^3>0\), so the full audited conclusion is
\[
\boxed{R'>0,\ K\ge0\ \Longrightarrow\
A_{k+\ell}\ge A_k\ge\frac{48c_0^3}{Z_0}>0,\qquad k,\ell\ge0,}
\tag{4}
\]
\[
D_{3,k}\ge\frac{48c_0^3Z_k}{F_kZ_0}>0.
\]
All indices here are finite integers. The condition \(K\ge0\) is used
through the chain rule below, not deduced from association.

**Gaussian equality.** For \(\Phi=e^{-au^2}\), \(a>0\),
\(R=4a^2u^2-2a\) and \(T=R^2-8aR-8a^2\). Thus \(g''=2\),
\(h=2\cdot(1/2)=1\), and \(M_k=Z_k\), \(A_k=1\) for every \(k\).
The exact program verifies the Gaussian polynomial relation and pair
identity (2). This is normalization and equality-case validation only.

Primary inspection was restricted to FKG printed pp.90–91, Proposition 1
and the support-sublattice discussion, and de Boor pp.63–64, especially
(52). The existing archived PDFs were visually checked by a contributing
same-model audit; hashes match the shared receipts. Their full proofs
were not audited. The continuous application above is our argument;
no background Karlin–Rinott theorem is imported.

## 3. New differential condition and regular origin

The differential identities in Note05 are correct:
\[
g''=C/(R')^3,\qquad g'''=K/(R')^5,\qquad K=R'C'-3CR''.
\]
With \(x=u^2\), write \(r=\widehat R'\), \(s=\widehat T'\) for this
display only. Then
\[
H=r\widehat T''-s\widehat R'',\quad
H'=r\widehat T'''-s\widehat R''',\quad
J=rH'-3H\widehat R'',\quad C=8u^3H,\quad K=32u^5J. \tag{5}
\]
The terms of order \(u^3\) in \(R'C'\) and \(3CR''\) cancel exactly.
Consequently \(g'''=J/(\widehat R')^5\) on the punctured half-line.

Retain \(p_j=4^jQ_j(0,z,0)\), \(z=U(0)\), \(e_j=p_j/p_0\),
\(p_0=z-3/2\), and all r1 jets. The only new even jet is
\[
\begin{aligned}
p_{10}={}&42943968z^6+793515312z^5+6355559664z^4\\
&-27710372640z^3-9760258112z^2-25420738320z+1125360240.
\end{aligned} \tag{6}
\]
The quotient-series recurrence from denominator times quotient equals
numerator, through degree three in \(x\), gives
\[
\begin{aligned}
\widehat R'''(0)&=(e_8-16e_2e_6-15e_4^2+120e_2^2e_4-90e_2^4)/120,\\
\widehat T'''(0)&=(e_{10}-15e_2e_8-16e_4e_6
+90e_2^2e_6+30e_2e_4^2-90e_2^3e_4)/120.
\end{aligned} \tag{7}
\]
The first two quotient derivatives agree with r1, including its coefficient
7 in \(12\widehat R''=e_6-7e_2e_4+6e_2^3\).

To specify the complete mixed numerator before cancellation, put
\[
\begin{aligned}
A&=e_4-e_2^2,& B&=e_6-e_2e_4,\\
D&=e_6-7e_2e_4+6e_2^3,& E&=e_8-6e_2e_6-e_4^2+6e_2^2e_4,\\
F&=120\widehat R'''(0),& G&=120\widehat T'''(0).
\end{aligned}
\]
Then \(J(0)=(A^2G-ABF-5ADE+5BD^2)/480\). Combining all terms in
the same variable \(z\) gives the exact result
\[
\boxed{J(0)=\frac{768\,\mathcal P(z)}{5(z-3/2)^6}}, \tag{8}
\]
where the complete numerator polynomial is specified by its coefficients
in ascending powers \(z^0,\ldots,z^{15}\):

```text
0, 5157219375, 197546060250, -400881899250,
-2617975845450, 1837905778800, -5088891988890,
1978703613270, 1297491608430, -950010914439,
237333481512, -35580583380, -1384014396,
1983548600, -458690000, 112500000
```

The sign proof needs no new enclosure of theta. The r1 analytic bound is
\[
z>\frac{6698045526361744}{1407422119140625}>47/10.
\]
After translating \(z=v+47/10\), all **16** coefficients of
\(\mathcal P(v+47/10)\) are strictly positive. They are retained exactly
in `origin.translated_M` of the record. Its constant term is
\(47814126725800678667031723599/62500000000\); its leading coefficient
is \(112500000\). The binomial translation and every coefficient sign
are verified by rational arithmetic in the program. This proves
\(\mathcal P(z)>0\), with the denominator in (8) positive.

Thus \(J(0)>0\), while r1's \(\widehat R'(0)>0,H(0)<0\) remain
unchanged. Analytic evenness and (5) give
\[
\boxed{K(u)=32J(0)u^5+O(u^7)>0}
\]
near zero, together with \(R'(u)>0\) there. No derivative above ten
was computed; analyticity supplies the remainder order without acquiring
an additional jet or an effective neighborhood radius.

For completeness, the record also contains an exact interior signed
numerator. With the r1 state numerators \(A_q=q_0q_3-q_1q_2\),
\(D_R\), \(N\) defined there, set
\(E_C=q_0\mathcal DN-3N\mathcal Dq_0\). Then
\[
K=\frac{4^{13}}{q_0^6}(A_qE_C-3ND_R).
\]
Its 579 signed state-polynomial terms are recorded before any bound;
\(q_0=8\Phi/B>0\) on the canonical orbit. This identity is not a
global sign proof.

## 4. Tail after the leading cancellation

Use exactly \(P_{j+1}=4tP_j'+(1-4t)P_j\) through \(P_7\).
For \(\phi_1=e^u(2t^2-3t)e^{-t}\), \(d=2t-3\), exact division gives
\[
R_1=16t^2-88t+33+24/d,
\quad T_1=256t^4-3840t^3+14944t^2-11632t-1983-7824/d.
\]
Using the exact rational derivatives \(D_u=4tD_t\),
\[
\begin{aligned}
R_1'&=128t^2-352t+O(t^{-1}),&R_1''&=1024t^2-1408t+O(t^{-1}),\\
C_1&=2^{22}t^6-39\cdot2^{20}t^5+O(t^4),&
C_1'&=24\cdot2^{22}t^6-780\cdot2^{20}t^5+O(t^4).
\end{aligned}
\]
The \(t^8\) terms in \(K_1\) cancel. The next coefficient is
\(-512(-39\cdot2^{20})-4224\cdot2^{22}=3\cdot2^{30}>0\).
The exact calculation retains the full rational expression
\[
K_1=\frac{3\cdot2^{26}t^5}{(2t-3)^7}\,p(t), \tag{9}
\]
\[
\begin{aligned}
p(t)={}&2048t^9-32768t^8+239232t^7-1034304t^6\\
&+2917728t^5-5589360t^4+7280280t^3\\
&-6180300t^2+3056130t-654885.
\end{aligned}
\]
It verifies the vanished degree-ten term before determining the leading
degree-nine numerator coefficient. Therefore
\(K_1=3\cdot2^{30}t^7+O(t^6)\).

The full-source error is separately differentiated through order seven.
If \(E_j=\Phi^{(j)}-\phi_1^{(j)}\),
\(M_j=\sum|\operatorname{coeff}P_j|\), and
\(B_j=\sum_{n\ge2}n^{2j+4}e^{-(n^2-4)}<\infty\), then
\[
|E_j|\le e^u M_jB_jt^{j+2}e^{-4t}\quad(t\ge1,\ 0\le j\le7). \tag{10}
\]
These same dominating sums justify the differentiated theta series.
For \(t\ge3\), \(\phi_1\ge e^ut^2e^{-t}\). For normalized jets
\(f_j=\Phi^{(j)}/\Phi\), this gives
\(f_j-f_{j,1}=O(t^je^{-3t})\).
Use the exact recurrence \(f_j'=f_{j+1}-f_1f_j\) to propagate errors:
\[
\begin{array}{lll}
\delta R'=O(t^3e^{-3t}),&\delta R''=O(t^4e^{-3t}),&\delta R'''=O(t^5e^{-3t}),\\
\delta T'=O(t^5e^{-3t}),&\delta T''=O(t^6e^{-3t}),&\delta T'''=O(t^7e^{-3t}).
\end{array}
\]
Crucially, \(C'=R'T'''-T'R'''\) exactly. Consequently
\(\delta C=O(t^8e^{-3t})\),
\(\delta C'=O(t^9e^{-3t})\),
\(\delta K=O(t^{11}e^{-3t})\). No unspecified big-O remainder was
differentiated. Combining (9)–(10) proves
\[
\boxed{K=3\cdot2^{30}t^7+O(t^6)+O(t^{11}e^{-3t})>0}
\]
eventually, alongside the inherited eventual \(R'>0\). There is no
effective cutoff or compact-interval conclusion.

## 5. Scope, controls and return

The analytical premise screen in Note05 Section 6 survives unchanged.
Euler-factor and altered arithmetic-square sources fail complete canonical
reconstruction; their new source signs are untested. Without full evenness,
weighted-square and finite-prime sources require their own retained
endpoint terms. Reflected super-Gaussian sources retain the generic even
boundary identity but are not canonical. Smooth shape/positive-primitive
data supply neither \(R'>0\) nor \(K\ge0\). The Gaussian satisfies the
generic hypotheses with equality. No numerical collision rerun or
uncomputed sign claim about a control is made. A fixed-order transfer may
accept colliding sources without contradicting its conclusion.

The conditional normalized index comparison (4) is the prospective
structural payoff. Canonical order-three positivity is already in the
recorded baseline. No new canonical coefficient range, increasing-order
argument or RH conclusion has been established. The preserved negative
origin \(C\) is compatible with the new condition; it is not repaired,
discarded or relabeled.

**J-E01 r2 is complete. Next: [B] J-B02 — Astra.** The remaining task is
to resolve the actual global pair \(R'(u)>0\), \(K(u)\ge0\) for
\(0<u<\infty\), by a proof, a usable bounded execution contract, or a
scoped obstruction. Both limiting tests pass, leaving the intervening
region unpaid. The [model-change continuation][continuation] specifies
that handoff. No global scan, new sufficient condition, or next derivative
test is started here.

[request]: 05_J_B01_SIGNED_AVERAGING_DECISION_20261101.md#7-frozen-execution-request-j-e01-r2
[r1]: 03_J_E01_R1_REPRESENTATION_AND_ENDPOINT_TAIL_RETURN_20261101.md
[code]: ../numerics/j_e01_r2_audit.py
[record]: ../numerics/J_E01_R2_EXACT_RECORD_20261101.json
[continuation]: 08_CONTINUATION_FOR_ASTRA_GLOBAL_SIGNED_AVERAGING_20261101.md
[fkg]: https://math.bme.hu/~balint/oktatas/perkolacio/percolation_papers/fortuin_kasteleyn_ginibre.pdf
[deboor]: https://ftp.cs.wisc.edu/Approx/dvdsurvey.pdf
[results]: ../../../../../result-summaries/README.md
[theta]: ../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../avoid/README.md
[joint]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[normalization]: ../../../../../avoid/08_normalization_and_constant_slips.md
[scopes]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[imports]: ../../../../../avoid/16_unchecked_imports_and_novelty_claims.md
