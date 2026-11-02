# J-B01 signed averaging decision and J-E01 r2 request

1 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**,
reasoning effort **max**.

**Decision:** retain the real coefficient integral and investigate
monotonicity of its **normalized signed average** as the coefficient index
increases. The conditional argument below permits the negative source
region proved in [J-E01 r1][return]. Its new source requirement is that
the curvature of the graph \(T=g(R)\) be increasing; it need not be
nonnegative. This requirement, and global \(R'>0\), are **unproved for
canonical theta**. This round supplies a mechanism and a bounded audit
request, with no new canonical coefficient range or novelty claim.

This completes the revised J-B01 decision requested by
[Continuation04][after-e01]. The [live register][progress] owns status.
The original [Note01][original], its r1 request and the exact obstruction
remain unchanged.

| Next task | Type | Recommended model and reason | Readiness | Expected output |
| --- | --- | --- | --- | --- |
| **J-E01 r2, Section 7** | E | Sol; audit a fixed averaging proof and two specified source limits | Ready, request issued | Proof audit, Gaussian normalization, exact origin and differentiated tail outcomes |
| J-B02 | B | Astra; decide how to prove the remaining global source inequalities | Gated by a supportive r2 return | One global proof route, bounded contract or scoped obstruction |
| Return to J-B01 | B | Astra; revise the mechanism if r2 rejects a required premise | Only on r2 failure or unresolved feasibility | Scoped decision; no automatic increase of derivative order |

Read with the [result index][results], [theta identities][theta] and
[controls][controls], and the [avoid index][avoid], especially
[reformulations][reformulations], [shape premises][shape],
[joint estimates][joint], [scoped exclusions][scopes] and
[unchecked imports][imports]. This is a fixed-order sufficient mechanism,
not an RH-equivalent criterion or an all-degree exclusion claim.

## 1. Preserve the obstruction and the normalization

Work at physical heat time zero with the complete even canonical source
\[
\Phi(u)=\sum_{n\ge1}(2\pi^2n^4e^{9u}-3\pi n^2e^{5u})
 e^{-\pi n^2e^{4u}},\qquad
b_n=\int_0^\infty u^{2n}\Phi(u)\,du,\quad
c_n=\frac{b_n}{(2n)!},\quad\gamma_n=n!c_n.
\]
Keep \(c_n=0\) for negative integer indices. Set
\[
R=\frac{\Phi''}{\Phi},\qquad T=\frac{\Phi^{(4)}}{\Phi},\qquad
C=R'T''-T'R'',\qquad D_{3,k}=\det[c_{k+j-i}]_{i,j=0}^2.
\]
Primes on \(R,T,C\) mean derivatives in \(u\). The verified identity is
\[
M_k:=F_kD_{3,k}
 =\int_\Omega\Big(\prod_{i=1}^3u_i^{2k}\Big)V(\mathbf u^2)
 \Delta_3(\mathbf u)\,d\mathbf u,
\quad F_k=(2k)!(2k+2)!(2k+4)!,
\tag{1}
\]
where \(\Omega=\{0<u_1<u_2<u_3\}\), \(V(\mathbf y)=\prod_{i<j}(y_j-y_i)\),
and \(\Delta_3=\det[\Phi^{(2i)}(u_j)]_{i=0,1,2;\,j=1,2,3}\).
Absolute convergence, the ordered-chamber constant, and all endpoints
were checked in r1. In particular
\[
D_{3,0}=c_0^3,\qquad M_0=0!\,2!\,4!\,c_0^3=48c_0^3>0.
\tag{2}
\]
The same return proves \(R'>0\) and \(C<0\) near zero, and both signs
positive eventually. Thus \(\Delta_3\) is negative for suitable three
small nodes. An everywhere nonnegative integrand is unavailable.
Constant row operations with positive determinant, positive column
scalings, or increasing changes of the source variable preserve that
local determinant sign. These elementary repairs cannot restore the
rejected pointwise sign mechanism. This observation says nothing about
more substantial integration identities or signed cancellation.

## 2. Compare two ways to use the signed integral

| Mechanism | Required estimate | Decision in this round |
| --- | --- | --- |
| Direct comparison of positive and negative parts of (1) | A bound on the complete negative region and a positive contribution that dominates it uniformly in the intended indices | Not selected. Origin and eventual-tail signs do not identify all mixed-node regions or pay the compact contribution. Fixed-order eventual positivity already belongs to the baseline. |
| Positive association after factoring a divided difference | Global \(R'>0\), and an increasing second derivative of \(g=T\circ R^{-1}\) | Selected for a bounded feasibility audit. It transfers the positive anchor (2) to larger indices while allowing local negative values. |

The first option remains available if new cancellation estimates emerge.
The second supplies an explicit comparison between indices. Its source
condition is still a substantive hypothesis to test.

## 3. Factor the determinant without discarding its sign

Temporarily assume \(R'(u)>0\) on \(u>0\), so the source curve is a graph
\(T(u)=g(R(u))\) on the interval \(I=R((0,\infty))\). Define
\[
h(\mathbf u)=g[R(u_1),R(u_2),R(u_3)],
\]
the second divided difference. Direct determinant algebra gives
\[
\Delta_3(\mathbf u)=\Big(\prod_i\Phi(u_i)\Big)V(R(\mathbf u))h(\mathbf u).
\tag{3}
\]
The positive averaging density is
\[
w_k(\mathbf u)=\Big(\prod_i u_i^{2k}\Phi(u_i)\Big)
 V(\mathbf u^2)V(R(\mathbf u)),\qquad
Z_k=\int_\Omega w_k\,d\mathbf u>0.
\tag{4}
\]
With \(d\mu_k=w_k\,d\mathbf u/Z_k\), the observable is
\[
A_k=\frac{F_kD_{3,k}}{Z_k}=\mathbb E_k h.
\tag{5}
\]
This is a signed expectation. Neither \(h\) nor \(\Delta_3\) is assumed
nonnegative.

The general argument requires a positive sufficiently smooth source
satisfying (1)–(2), \(R'>0\), and, for every integer \(k\ge0\),
\[
0<Z_k<\infty,\qquad \int_\Omega w_k|h|<\infty.
\tag{6}
\]
For canonical theta, these integrability conditions hold conditional on
\(R'>0\). At zero \(\Phi>0\) and \(R\) is finite. In the tail,
\(R=O(t^2)\), \(t=\pi e^{4u}\), whereas \(\Phi\) decays as a polynomial
in \(t\) times \(e^{u-t}\). Expanding the Vandermondes bounds \(Z_k\)
by convergent products. Also
\(w_k|h|=(\prod u_i^{2k})V(\mathbf u^2)|\Delta_3|\), whose absolute
integral was paid in r1. These arguments cover every fixed additional
index tilt, without giving estimates uniform in determinant order.

The Genocchi–Hermite formula gives
\[
h(\mathbf u)=\int_0^1\int_0^{1-s}
 g''\!\left((1-s-t)R(u_1)+sR(u_2)+tR(u_3)\right)\,dt\,ds.
\tag{7}
\]
The simplex has area \(1/2\). Thus \(g'''\ge0\) makes \(h\) increasing
in each source coordinate. Formula (7) is the order-two case of
[de Boor, (52), p. 64](https://ftp.cs.wisc.edu/Approx/dvdsurvey.pdf).
Increasing curvature permits negative curvature near the left endpoint.

## 4. Positive association supplies the index comparison

The ordered chamber is closed under coordinatewise minimum and maximum.
For any increasing scalar function \(f\), the pair factor
\(f(u_j)-f(u_i)\) has the multiplicative lattice inequality there.
In the only nontrivial case, write the transformed crossed endpoints as
\(a\le c<d\le b\). The meet/join product minus the original product is
\[
(d-a)(b-c)-(b-a)(d-c)=(c-a)(b-d)\ge0.
\]
For aligned endpoints the products agree. Apply this to each pair for
\(f(u)=u^2\) and \(f(u)=R(u)\). The single-coordinate factors in (4)
satisfy equality. Multiplication proves
\[
w_k(\mathbf u\wedge\mathbf v)w_k(\mathbf u\vee\mathbf v)
 \ge w_k(\mathbf u)w_k(\mathbf v).
\tag{8}
\]
No concavity of \(\Phi\) was needed for this step.

[FKG Proposition 1, p. 91](https://math.bme.hu/~balint/oktatas/perkolacio/percolation_papers/fortuin_kasteleyn_ginibre.pdf)
gives nonnegative covariance for increasing functions on finite
distributive lattices satisfying (8). For the continuous application,
take equally spaced finite grids of strictly ordered nodes in
\(\Omega\cap[\varepsilon,L]^3\). Each grid is a distributive sublattice
whose positive weights satisfy (8). Apply FKG and pass to Riemann
integrals. The divided difference extends continuously to coincident
nodes on this compact interval, so the functions are bounded. Then let
\(\varepsilon\downarrow0\), \(L\uparrow\infty\). Condition (6) and its
tilted versions justify convergence of all integrals. This proves the
needed covariance inequality for the possibly negative observable \(h\).

For an integer \(\ell\ge0\), the function
\(q_\ell(\mathbf u)=(u_1u_2u_3)^{2\ell}\) is increasing. Since
\(w_{k+\ell}=q_\ell w_k\),
\[
A_{k+\ell}-A_k
 =\frac{\operatorname{Cov}_{\mu_k}(h,q_\ell)}{\mathbb E_kq_\ell}\ge0.
\tag{9}
\]
Combining this with (2) proves the conditional implication
\[
\boxed{R'>0,\quad g'''\ge0\quad\Longrightarrow\quad
 A_{k+\ell}\ge A_k\ge A_0=\frac{48c_0^3}{Z_0}>0.}
\tag{10}
\]
In particular, under these hypotheses,
\[
D_{3,k}\ge\frac{48c_0^3}{F_k}\frac{Z_k}{Z_0}>0.
\tag{11}
\]
The positivity anchor is the triangular determinant. The bound retains
an unevaluated integral \(Z_k\); it is not a computed numerical
improvement. This derivation awaits the r2 audit, not an independent
specialist review.

**Normalization check.** For \(\Phi(u)=e^{-a u^2}\), \(a>0\),
\[
R=4a^2u^2-2a,\quad T=R^2-8aR-8a^2,\quad g''=2,\quad g'''=0.
\]
Thus \(h=1\), \(M_k=Z_k\), and \(A_k=1\) for every \(k\).
This checks the simplex constant and equality case; it is not theta
sign evidence.

## 5. The new source estimate and its endpoint form

Set
\[
K(u)=R'(u)C'(u)-3C(u)R''(u).
\]
Since \(g''=C/(R')^3\),
\[
g'''(R(u))=\frac{K(u)}{(R'(u))^5}.
\tag{12}
\]
The first unpaid **global** estimate is
\[
R'(u)>0,\qquad K(u)\ge0\qquad(0<u<\infty).
\tag{13}
\]
The old failure \(C<0\) does not contradict (13). The known positive
signs of \(R'\) and \(C\) in the tail do not establish it.

At the origin put \(x=u^2\), \(\widehat R(x)=R(\sqrt x)\),
\(\widehat T(x)=T(\sqrt x)\). Primes in the next display mean
\(x\)-derivatives:
\[
H=\widehat R'\widehat T''-\widehat T'\widehat R'',\quad
J=\widehat R'H'-3H\widehat R'',\quad
H'=\widehat R'\widehat T'''-\widehat T'\widehat R'''.
\]
Then
\[
C=8u^3H,\qquad K=32u^5J,\qquad
 g'''=\frac{J}{(\widehat R')^5}.
\tag{14}
\]
The r1 record proves \(\widehat R'(0)>0\), \(H(0)<0\).
The sign of \(J(0)\) has not been calculated. It requires the tenth
source derivative: \(\widehat T'''(0)\) contains \(\Phi^{(10)}(0)\).
The Q10 cap below is justified by (14); it does not authorize successive
higher derivative tests if this mechanism fails.

Reuse the exact Jacobi recurrence
\[
Q_0=U+\tfrac32(a^2-1),\quad Q_{j+1}=\mathcal DQ_j+\tfrac a4Q_j,
\quad \Phi^{(j)}=4^jB Q_j/8,
\]
on the canonical orbit
\(a(0)=\chi(0)=0\),
\(U(0)=z=\Gamma(1/4)^8/(64\pi^4)>47/10\), with
\(\mathcal D a=(U+a^2-1)/2\),
\(\mathcal D U=2U(a+\chi)\), \(\mathcal D\chi=a\chi-U\).
The full canonical reconstruction, including \(B\), remains fixed.
At interior points (12) uses source derivatives through order seven.

For the tail use \(t=\pi e^{4u}\) and
\[
P_0=2t^2-3t,\quad P_{j+1}=4tP_j'+(1-4t)P_j,\quad
\Phi^{(j)}=e^u\sum_{n\ge1}P_j(n^2t)e^{-n^2t}.
\tag{15}
\]
There is an essential cancellation: r1 gives
\(R'\sim128t^2\), \(R''\sim1024t^2\), \(C\sim2^{22}t^6\).
The resulting \(t^8\) terms of \(R'C'\) and \(3CR''\) agree.
The r2 calculation must keep the next nonzero term and a justified
differentiated remainder. Differentiating an unspecified big-O estimate
is not an acceptable tail proof. No sign for \(K\) is inferred here.

## 6. Payoff and the control screen

Order-three coefficient positivity is already inside Katkova's PF44
baseline, as normalized in [Note01, Section 4][original]. A successful
canonical application would test the structural comparison (9) and the
signed-transfer architecture with a known initial anchor. No novelty
claim or extension in determinant order is made. The difficult regime
of small index and growing order remains open.

The theorem is generic and conditional. Following [the control index][controls],
the analytical premise screen is:

| Control | Premise and scope |
| --- | --- |
| Euler-factor source | A positive even source can use (1); its altered source fails complete canonical reconstruction. Its signs in (13) are untested. |
| Weighted-square and finite-prime perturbations | Changed arithmetic weights fail canonical reconstruction. Without full evenness, the odd endpoint derivatives required by (1) must be checked and retained when nonzero. |
| Reflected super-Gaussian source | Evenness allows the boundary identity, but this is not the canonical orbit. Its collision alone implies no failure of (13). |
| Smooth shape and positive-primitive controls | Their shape or primitive signs do not imply (13); their changed source fails canonical identification. |
| Gaussian equality case | Satisfies the generic hypotheses and gives equality in (9), checking normalization. |

This screen does not rerun collision numerics. A fixed-order theorem may
accept a source with other nonreal zeros: its conclusion does not exclude
all collisions. The complete canonical source distinguishes the intended
application, but supplies no quantitative proof of (13).

## 7. Frozen execution request J-E01 r2

**Parent:** revised J-B01. **Type:** E. **Recommended model:** Sol;
the proof, source, expressions, domain and finite limits are fixed.
Issued 1 November 2026 for Edward Baker by **gpt-6-astra / max**.
The author chooses the actual executor and effort. This request is issued,
not executed or dispatched; r1 remains complete and unchanged.

**Inputs and versions.** Use this note, the [r1 return][return] and
[exact record][record], [Note01][original], shared [Jacobi closure][closure],
[primary-source records][sources05], and the [owning register][progress].
HEAD is `c97b376dcbf81f05ea3a4f7d360da168af4a1345`; inputs include
working-tree research files. Record this note's hash at execution.

| Preserved input | SHA-256 |
| --- | --- |
| Note01, original decision and r1 | `a2097d5952d1767781a6a0917f2acfd98b64d21f9a393755d62686863aae1717` |
| Note03, r1 return | `23ce0fa4b4b4553e5775b045724fe3e99676fa495dab22e578f942e6a2bb3875` |
| Note04, requested continuation | `76f7b2d849d33133caadc84d1820ef2ace658817ac928e3521ad59d78279d088` |
| Existing j_e01_audit.py | `5905598d1aba38d7e366df0b0fabf0b53a34f4ace21b4056a1a644e89d4f73e5` |
| J_E01_R1_EXACT_RECORD_20261101.json | `923b67d799a4c87af4efdabd7a23c4f02a428473886da0b23b9ace4f89ce41bb` |

**Fixed work in order.**

1. Audit (3)–(11): determinant orientation and simplex constant; the
   meet/join inequality; the finite-lattice FKG import and limiting
   steps; absolute integrability; the tilt/covariance identity and
   positive anchor. Reuse r1's coefficient integral, checking any issue
   needed for this application. Reproduce the Gaussian equality case.
   A correction preserving the same hypothesis and conclusion is
   permitted; a changed mechanism requires a B return.
2. Audit (12)–(14). Extend exact recurrence algebra only through
   \(Q_{10}\). Compute \(J(0)\) with complete mixed terms, give its
   numerator and positive denominator in \(z\), and decide its sign
   if the bounded methods below suffice. Preserve r1's signs of
   \(\widehat R'(0)\) and \(H(0)\). Report positive, negative, zero
   or unresolved; a zero value does not establish a neighborhood sign.
3. Extend the fixed first-summand tail calculation through the
   derivatives needed for \(K\), at most \(P_7\). Determine the first
   nonzero term after cancellation with a differentiated theta
   remainder bound. State whether (13) survives the eventual tail test.
   An asymptotic sign does not supply an effective cutoff.
4. Return the disposition and exactly which global estimates remain.
   Do not compute theta minors or \(Z_k\) just to recheck known
   order-three positivity.

**Finite limits and routine choices.** Exact polynomial algebra, rational
Taylor series and equivalent regular variables preserving (12)–(14) are
allowed. For the single constant \(z\), prefer a symbolic rational sign
proof; otherwise permit one outward-rounded enclosure at 128 bits and
one refinement at 256 bits, documenting acquisition and remainder. If
unavailable or inconclusive, return unresolved. No Q order above 10,
tail derivative above 7, source-coordinate grid, compact-region
certificate, quadrature campaign, higher determinant order, or heat/source
change belongs to r2. After a failed sign, complete only the remaining
bounded audit items; do not repair the hypothesis or expand the campaign.

**Outputs and acceptance.** Save a separate r2 return in `01_jensen/notes/`
and any new code and small exact record in `01_jensen/numerics/`. Preserve
r1's note, program and record; new code may reuse its routines without
modifying them. Record actual model/effort, input/code hashes, exact
versus enclosed signs, corrections and unproved premises. Completion is
a proof audit and two bounded feasibility outcomes, or a precise
obstruction making a remaining item unavailable. It does not require
the global inequalities (13).

**Routing and stop rule.** If the proof and both tests support the
mechanism, return (13) to **[B] J-B02 — Astra**. A failed required sign,
insufficient Q10 order or unresolved feasibility returns to
**[B] J-B01 — Astra** with the scope of failure. A failed \(K\) sign
rejects this sufficient monotone-curvature certificate; it does not
reject (9) under a weaker averaged premise or coefficient positivity.
No automatic next curvature derivative is authorized.

**Files allowed to change.** New r2 notes/code/record; the sole Jensen
register and route indexes; shared references for inspection/provenance;
this chat's uniquely registered history through the capture tool.
Preserve other writers' changes. Assessments belong in `01_jensen/reviews/`
and state their review relationship. Model change is not independent
review.

## 8. Source inspection and continuation

FKG Proposition 1 and de Boor (52) were read in primary PDF text and
visually inspected from archived copies. The [annotation][sources05],
catalog and receipts preserve their scope; third-party PDFs stay outside
Git. Sections 3–4 are our conditional application. Karlin–Rinott is a
background lead, not an imported theorem. No numerical research execution
occurred in this B round.

**Next: [E] J-E01 r2 — Sol.** The [model-change continuation][handoff]
gives the reading order and pasteable request. After the return,
brainstorm the global estimate only if this mechanism survives.

[original]: 01_J_B01_COEFFICIENT_REPRESENTATION_DECISION_20261101.md
[return]: 03_J_E01_R1_REPRESENTATION_AND_ENDPOINT_TAIL_RETURN_20261101.md
[after-e01]: 04_CONTINUATION_AFTER_J_E01_ORIGIN_OBSTRUCTION_20261101.md
[handoff]: 06_CONTINUATION_FOR_SOL_SIGNED_AVERAGING_AUDIT_20261101.md
[record]: ../numerics/J_E01_R1_EXACT_RECORD_20261101.json
[progress]: ../research-progress/01_JENSEN_RESEARCH_PROGRESS_20261101.md
[closure]: ../../notes/02_CNV_DETERMINANT_TRANSFER_AND_THETA_DIFFERENTIAL_CLOSURE_20261101.md
[sources05]: ../../references/05_SIGNED_AVERAGING_SOURCES_20261101.md
[results]: ../../../../../result-summaries/README.md
[theta]: ../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../avoid/README.md
[reformulations]: ../../../../../avoid/01_restating_the_target.md
[shape]: ../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[joint]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[scopes]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[imports]: ../../../../../avoid/16_unchecked_imports_and_novelty_claims.md
