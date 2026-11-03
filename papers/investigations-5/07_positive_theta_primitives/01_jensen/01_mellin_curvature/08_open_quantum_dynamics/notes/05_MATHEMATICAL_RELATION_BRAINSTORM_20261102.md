# MC08-B03: background and candidate mathematical relations

2 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance; actual **gpt-6-astra (Codex), effort xhigh**, chat `01a19e4c-7083-7282-92f6-f6cbeb970065`, turn `01a19f05-6b05-78c0-ad65-4a519c810b08`. This is an author-requested discussion primer. **No mechanism is selected, no new estimate is proved and no execution campaign is issued.** The task remains at conceptual discussion. E04's check of B02 is separately pending.

| Continuation | Type | Recommended model | State | Output |
| --- | --- | --- | --- | --- |
| MC08-B03, discuss and select a mathematical relation | B | Astra: the independent premise and proof mechanism remain open | Current author-requested discussion | One selected premise with a consumer and controls, or a precisely scoped failed idea |
| MC08-E04 r1, check B02 | E | Sol: the analytical checks are frozen | Separate Ready/unstarted task, not executed by this discussion | Accept/correct the narrow intermediate-cone stop |

Read with the [result index][results], [theta/physical cluster][theta-results], [control inventory][controls], [avoid index][avoid], [target-reformulation rule][target], [joint-estimate lesson][joint] and [scope rule][scope]. These candidate descriptions are research questions, not evidence for RH or newly established comparison principles.

## 1. The mathematical and physical objects

The fixed source Phi comes from the complete integer-square theta spectrum. Its coefficients are
\[
c_n=\frac1{(2n)!}\int_0^\infty u^{2n}\Phi(u)\,du>0,
\qquad F(w)=\sum_{n\ge0}c_nw^n,
\]
with c_n=0 for n<0. Under the established normalization, nonnegativity of every finite ordered coefficient minor is equivalent to RH. This full-family formulation is a reformulation, not a new criterion. Rectangular determinants
\[
D_{r,k}=\det[c_{k+j-i}]_{i,j=0}^{r-1}
\]
are the present pilot, not a substitute for all arbitrary minors and all particle numbers. The classical multiple-positivity bridge is recorded in [MC02](../../02_fermionic_correlators/notes/01_THETA_ORBITAL_COMPARISON_RETURN_20261101.md) and [Katkova v1, Definition 2, ASWE and Theorem C](https://arxiv.org/html/math/0505174v1).

The elementary two-particle example is D_{2,1}=c_1^2-c_0c_2. Positive individual coefficients do not sign their difference. In the fermionic picture the terms are alternative assignments of identical particles to output modes, with an exchange minus sign. They are mathematical paths in mode index, not a claim about spatial paths of a laboratory particle.

MC08's no-count transfer K_v=F(vS)/F(v) represents the corresponding signed amplitudes. For r particles displaced together by k,
\[
A_{r,k}(v)=\frac{v^{rk}}{F(v)^r}D_{r,k}.
\]
E01/E02 give a time-dependent quadratic Hamiltonian plus linear loss on 0<=v<=1/25, a count instrument, a fixed-mode ideal collision approximation, and a separately justified compatible vacuum-Fock extension. A controlled reference arm measures the sign. The conventional distinction between conditional no-jump evolution and the complete master equation is explained in [Castin–Dalibard–Mølmer v1, Sections 1–2](https://arxiv.org/html/0805.4002v1).

The project-specific construction is in [Return03](03_FERMIONIC_LINDBLAD_REALIZATION_20261102.md); E03 accepted its stated scope in separate same-model internal review. It remains neither specialist validation nor a positivity theorem. Signal survival p_J and flag survival q_0=(1+p_J)/2 are distinct, and the signed expectation is A=q_0 E[X|no count]. The original phase, full F(v), parity and particle-number conventions remain fixed.

## 2. The concrete comparison and its meaning

For r=3, abbreviate A_k=A_{3,k}. Accepted order-three results give D_{3,k}>0 for every integer k>=0. At k=0 the determinant is c_0^3. Thus for k>=1 and 0<v<=1/25 the denominator in
\[
\eta_k=\frac{A_{k-1}A_{k+1}}{A_k^2}
=\frac{D_{3,k-1}D_{3,k+1}}{D_{3,k}^2}
\tag{1}
\]
is positive. The proposed stronger quantitative pilot is
\[
\eta_k\le\frac{k}{k+3}.
\tag{2}
\]
It asks that the middle amplitude dominate the geometric mean of its two neighbors by a specified factor. For k=1 the allowance is 1/4, not merely 1. No numerical lower floor for D_{3,k} is supplied here.

Desnanot–Jacobi gives
\[
D_{4,k}D_{2,k}=D_{3,k}^2-D_{3,k-1}D_{3,k+1}.
\]
Since D_{2,k}>0, (2) would imply
\[
D_{4,k}\ge\frac{3}{k+3}\frac{D_{3,k}^2}{D_{2,k}}>0.
\tag{3}
\]
The proposed gain is a quantitative margin and a reusable mechanism. This fixed-order pilot sits within known finite-order positivity; it is not a new RH proof merely to recover an order-four sign. Extending it to every finite r would still require separate full-quantifier work. See [the original budget](../../notes/01_INITIAL_BRANCH_EVALUATION_20261101.md).

The Gaussian comparator F_G(w)=c_0 exp(aw), a>0, has
\[
D^G_{3,k}=\frac{2c_0^3 a^{3k}}{k!(k+1)!(k+2)!},\qquad
\eta^G_k=\frac{k}{k+3}.
\]
Taking a=c_1/c_0 fixes a convenient positive reference without changing theta. Define e_k=D_{3,k}/D^G_{3,k}>0. Then (2) is exactly e_k^2>=e_{k-1}e_{k+1}. This Gaussian-normalized discrete log-concavity is an explanatory restatement of the target, not an independently justified mechanism.

## 3. What the present blocker actually is

Complete positivity controls density matrices and probabilities. It does not determine the sign of a coherent overlap. The polynomial F_*=1+w+2w^2 passes the established loss admissibility and signed readout while producing -v^2/F_*(v)^2 in a two-particle endpoint amplitude. It lacks the canonical theta source but shares the generic physical structure. A successful relation therefore needs additional source information or a proved property that this control fails.

[B02](04_SIGNED_COMPARISON_DECISION_20261102.md) rejects one stronger mechanism: the unchanged generator cannot preserve the fixed nonnegative occupation cone on every intermediate interval. Longer hops have both signs depending on occupied spectators; demanding all of them nonnegative would force Gaussian F. Its proof-author check is complete, separate E04 verification pending. It does not reject positivity of the actual prepared endpoint amplitudes, paired-path cancellation or a different comparison method.

B02 also proves d eta_k/dv=0. The activity factors cancel exactly in (1), as do the survival terms when the signed observation is reconstructed. A constant quantity can still obey a structural bound. What fails is the hope that variation of this activity, or survival alone, improves the unknown coefficient ratio. A new parameter or relation must carry additional information, not identify v with source heat or Mellin tilt.

There is an exact integral version of the blocker. The existing positive three-particle carrier mu_s and signed insertion h give M(s)=Z(s) E_s h>0, with T=2 sum log u_j. The established identity is
\[
(\log M)''(s)=\operatorname{Var}_s(T)
+\frac{\operatorname{Cov}_s(h,(T-E_sT)^2)}{E_sh}
-\left(\frac{\operatorname{Cov}_s(h,T)}{E_sh}\right)^2.
\tag{4}
\]
Here h can be negative. The scalar M(s) is positive but its integral is not a positive h-weighted probability measure. Bounding the carrier variance alone leaves the mixed centered-square covariance unpaid. The last square has a favorable minus sign; bounding the three terms separately can lose useful cancellation.

The Gaussian benchmark is kappa_3(s)=sum_{j=0}^2 sum_{n>=0}(s+j+1/2+n)^(-2). A joint bound of (4) by kappa_3(s) for s>=0 would give (2) by triangular integration over [k-1,k+1], with the existing factorial budget. That pointwise statement is stronger than the integrated target and might fail even if (2) holds. The first case needs the entire [0,2] slab, not a selected point. None of these bounds is acquired here. Integer k, real s, source heat and activity v remain distinct.

## 4. Three discussion routes and their actual obligations

### A. A joint endpoint exchange comparison

Keep the complete quantity
\[
W_k=\frac{k}{k+3}A_k^2-A_{k-1}A_{k+1}.
\tag{5}
\]
This is exactly the pilot target in undivided form. A promising *kind* of new relation would rewrite W_k using the actual theta source as a positive quadratic contribution plus a signed correction with a paid lower bound, or pair complete competing terms so that their joint total is nonnegative. Merely naming W_k, or defining an auxiliary quantity as its square root, adds no information.

Its measurement interpretation is elementary: let Z_j be the signed flag outcome X on no count and 0 on a count. E Z_j=A_j. Independent repetitions give E(Z_k Z'_k)=A_k^2 and E(Z_{k-1}Z_{k+1})=A_{k-1}A_{k+1}. Thus (5) compares two products of signed outcomes, preserving success factors automatically. It is not a positive measurement operator for arbitrary sources; measurement accessibility supplies no inequality. No two-copy entangling protocol or simulation is required for this identity.

The research obligation is an **independently derived theta relation** for the joint expression. The source's complete square spectrum and inversion identity are candidate inputs. Generic CAR, Wick algebra, loss dynamics or ordinary Cauchy–Schwarz alone are already insufficient. A noncircular positive decomposition would have to be built from source data without assuming the determinant margin it is meant to prove.

### B. An integrated bound for the signed insertion and source response

Use (4), or the existing inserted Ward identity, to keep the mixed response together. The hope is that the complete theta source ties the carrier's spread to the insertion's variation strongly enough to pay the Gaussian comparison after integration. This would provide an analytical route for the same endpoint comparison in A, rather than a mathematically independent target.

This is not a recommendation to derive another generic Ward identity. [MC04](../../04_biorthogonal_ensembles/notes/01_INSERTED_ENSEMBLE_IDENTITY_RETURN_20261101.md) already has one, including Xh, and proved failure of its specified pointwise finite-polynomial closure. A genuinely new move would bound its complete integrated mixed residual, or find another source-derived relation that pays it. The negative origin insertion, coincident-node cancellations and every spatial tail must remain. [MC03](../../03_connected_mellin_response/notes/01_COMPLETE_MELLIN_RESPONSE_RETURN_20261101.md) also leaves its full-domain signed moment payments open; its fixed-box Gaussian limit is not their substitute.

### C. Comparison along an auxiliary Gaussian-to-theta source path

One could seek a separately specified source family indexed by lambda, with a Gaussian initial endpoint and the original theta final endpoint. If all relevant D_{3,j}(lambda) stayed positive, a sufficient monotonicity relation would be
\[
\partial_\lambda\{\log D_{3,k-1}(\lambda)+\log D_{3,k+1}(\lambda)-2\log D_{3,k}(\lambda)\}\le0.
\tag{6}
\]
It would transport Gaussian equality into the desired bound. This is a conjectural proof architecture; (6) is not proved and no particular path is selected or authorized for execution here. It would need its own endpoint matching, source differentiability, all-path denominator positivity and complete tail estimates. A generic interpolation need not preserve the necessary positivity.

This cannot be the present v evolution, for which the left side is identically zero and there is no independently known Gaussian starting source. Nor can one assume the source-heat hierarchy closes from a finite coefficient prefix: [MC05](../../05_schur_toda_structure/notes/01_THETA_SCHUR_CONSTRAINT_RETURN_20261101.md) exposes the missing higher-coefficient response. A path chosen by assuming the target signs would be circular.

## 5. Source information and controls before selecting a route

The complete theta trace satisfies vartheta(t)=t^(-1/2)vartheta(1/t), t>0, with vartheta(t)=sum_{n in Z}exp(-pi n^2 t). This is [DLMF 20.7.32](https://dlmf.nist.gov/20.7.E32) at z=0, tau=it. It relates large and small scales while retaining exact unit weights on integer squares. It is an available identity, **not** an inequality for (5). Its use must yield a quantitative statement about the signed observable.

| Control | Required distinction in the discussion routes |
| --- | --- |
| Gaussian | Normalization/equality comparator; not canonical theta. A and B must match its constants; C must justify connecting to it. |
| Negative polynomial | Shares the loss construction, but fails canonical source reconstruction and has the explicit negative endpoint amplitude. Defeats generic physical-positivity arguments. It is not by itself a counterexample satisfying all strict order-three premises of (2). |
| Euler-factor | Alters the canonical coefficient/source data while preserving some positivity and symmetry. Its actual finite-order ratio and new candidate bound are not assigned. |
| Weighted-square / finite-prime | Alters unit weights and can fail full reflection. Square support and finitely many matching moments/endpoints alone do not supply the proposed comparison. |
| Reflected / smooth positive-primitive | Can preserve reflection, strong decay and auxiliary positivity while failing the complete arithmetic square expansion. Symmetry or shape alone is not enough to assert the desired bound. |
| Two-point association relaxation | Shows that monotone h, a positive carrier and positive association alone do not pay the original factorial budget. It does not realize the full canonical derivative-orbital structure. |

No family is excluded simply by declaring it noncanonical. A proposed derived inequality must be tested against its own premises. A positive-time collision is not evidence about an uncomputed time-zero finite-order minor.

## 6. Discussion recommendation, evidence and model changes

Begin by discussing A as the **joint target to organize**, with B as a possible way of deriving a source-dependent relation for it. This keeps the physical interference interpretation while exposing exactly where arithmetic/source information must enter. C is a distinct, more demanding architecture because it creates an entire path of new hypotheses. This is a discussion preference, not a feasibility finding or selected mechanism.

The useful next choice is whether to seek a direct integrated endpoint identity/pairing, or to invest in a new auxiliary source path. Do not label generic equations or an equivalent log-concavity reformulation as a result. A future execution task needs one explicit identity/inequality, its positive denominators, finite scope or analytic domain, controls, complete errors/tails and stop rule. None is issued here.

Checks in this turn are exact elementary algebra: cancellation of the v prefactor, the condensation consequence (3), Gaussian normalization of e_k, and products of the signed flag outcomes. The carrier/curvature and Ward statements are reused from the cited notes with their existing review limits. There is no new independent review, numerical program, quadrature, source interpolation, simulation or sampled sign claim. No manuscript milestone is declared.

Primary-passage reinspection on 2 November 2026: Katkova v1 Definition 2/ASWE/Theorem C (full-family scope); Castin–Dalibard–Mølmer v1 Sections 1–2, especially (4) and the no-jump normalization (conditional versus averaged evolution); DLMF 20.7.32 (theta inversion). These are already cataloged sources; earlier PDF provenance is preserved, and no full-paper audit is claimed.

**Next: [B] MC08-B03 — Astra**, continue the author discussion and choose one independent relation to investigate before issuing execution. E04/Sol remains separately Ready and unstarted. On a model change, read this note, the sole progress register and B02's narrow scope clarification. Record actual new model/effort; preserve the complete source and measurement, and this chat's unique MC08 history **0003**. A new public chat gets its own registration. No model switch, chat creation, delegation or computation is launched by this note.

[results]: ../../../../../../../result-summaries/README.md
[theta-results]: ../../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../../avoid/README.md
[target]: ../../../../../../../avoid/01_restating_the_target.md
[joint]: ../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[scope]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
