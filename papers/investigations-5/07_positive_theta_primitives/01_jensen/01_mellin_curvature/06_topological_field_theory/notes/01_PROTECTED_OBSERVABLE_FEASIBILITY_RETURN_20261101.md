# MC06-B01: the theta source as an unprotected response of circle supersymmetric quantum mechanics

1 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Contributor /root/mc04_ward, actual recorded model **gpt-6-astra (Codex)**, reasoning effort **ultra**, verified in worker session 01a19a49-e72d-7902-8f13-adf50b8aa74f, current turn 01a19a4f-2ad8-7863-9b61-978dfd7e15fb. MC04's prior return is frozen and is not an input to this assessment. This is MC06-B01's one bounded B assessment; separate checking is pending.

**Result.** The complete canonical theta source is exactly a thermal differential response to the form-degree fugacity of de Rham supersymmetric quantum mechanics on a compact circle. This supplies an explicit geometric model and observable dictionary. The required insertion is not \(Q\)-closed, and its nonzero \(Q\)-commutator is exactly the heat-response term which a protected-index argument would erase. In the specified compact-circle model, replacing it by an admissible fixed even \(Q\)-closed insertion makes the reconstructed source zero, already failing the \(r=1\) match.

Thus the selected **protected-observable route fails within a proved scope**, while an exact **unprotected physical response formulation survives**. No Mellin bound, new determinant sign, Donaldson invariant, all-theory no-go statement, or novelty claim is made.

| Next task | Type and recommended model | Dependency | Fixed completion test |
| --- | --- | --- | --- |
| MC06-E01: check this return | E — Sol; finite spectral algebra, operator domains, normalization and scope | Frozen MC06-B01 return; different worker | Check (2)–(7), the \(r=1,r=2\) conventions, pairing theorem and its assumptions, endpoint/tail arguments, and precise failure of protection. Accept, correct or leave unresolved. No new theory or numerical campaign. |

## 1. Baseline and bounded choice

Use [packet05][packet], the [local overview][overview] and [sole local register][progress], with the original [launch manifest][launch]. Mathematical inputs are [Note04][physical], the [initial Mellin assessment][initial], [accepted sign review][signreview], [comparative review][comparative], [route note][routes], [parent overview][parent] and [inspected physics record][sources]. These are the launch versions; no new sibling result is used. The support record fixes the exact input versions and this return's hash.

One explicit candidate was selected: **compact-circle de Rham supersymmetric quantum mechanics with a form-degree fugacity**. No second construction, four-dimensional moduli guess, numerical test or hierarchy search was attempted. It has the actual integer-square spectrum before any target determinant is supplied, so the source match is more specific than inserting an arbitrary matrix into a Grassmann integral. The later antisymmetrization remains generic and is not counted as a new sign mechanism.

Classification: the source and multi-copy observable matches below are exact reformulations; the protected-insertion obstruction is proved in-note for the stated model and operator class. There is no quantitative estimate. The [result index][results] and [avoid index][avoid], particularly [physical-channel lessons][channels], [theta identities][theta], [controls][controls], [re-realizations][rereal], [target reformulations][target] and [scoped exclusions][scope], govern that distinction.

## 2. Exact model dictionary

| Required datum | Chosen construction |
| --- | --- |
| Geometry and dimension | Circle \(S^1=\mathbb R/(2\pi\mathbb Z)\) with metric \(dx^2\); a one-dimensional quantum-mechanical system, not a four-dimensional gauge theory. |
| Fields / state space | Position \(x\) on \(S^1\) and one complex fermionic mode. Exactly: \(\mathcal H=L^2(S^1;\Lambda^0\oplus\Lambda^1)\). Wedge multiplication by \(dx\) creates the fermion; contraction annihilates it. |
| Measure | \(L^2\) inner product using \(dx\); Fourier modes \(e^{inx}/\sqrt{2\pi}\) in each form degree. All observables below are defined by convergent operator traces. No continuum path-integral measure is assumed. |
| Differential and Hamiltonian | \(Q=\sqrt\pi\,d\), \(Q^\dagger=\sqrt\pi\,d^\dagger\), \(Q^2=0\), \(H=\{Q,Q^\dagger\}=\pi\Delta=-\pi\partial_x^2\) on both degrees. Periodic Sobolev domains, \(H^1\) for the first-order operators and \(H^2\) for \(H\), suffice. |
| Degrees | \(Q\) raises form degree by one; \(Q^\dagger\) lowers it. \(N\) counts form degree, with eigenvalues \(0,1\). \(N,H,y^N\) and all source insertions are even operators of degree zero. |
| Full spectrum | For every \(n\in\mathbb Z\), one degree-zero and one degree-one state have energy \(\lambda_n=\pi n^2\). All modes are retained. |
| Zero-mode subtraction | \(P_{\rm harm}\) projects onto the two harmonic states \(n=0\), one in each degree. \(P_{\rm exc}=1-P_{\rm harm}\). |
| Parameters | Thermal parameter \(\beta>0\), degree fugacity \(y\), source coordinate \(u\) with \(\beta=e^{4u}\), coefficient index \(k\), Mellin tilt \(s\), and physical heat time are distinct. The last stays zero. |

The finite Fourier subspaces are a common algebraic core. Heat factors make every fixed polynomial in \(H\) trace class for \(\beta>0\); the formulas can therefore be proved mode by mode and passed to the absolutely convergent sums. This avoids unproved cyclic trace manipulations with unbounded operators.

The underlying de Rham/SUSY viewpoint is classical, as in [Witten, *Supersymmetry and Morse Theory*](https://www.ias.edu/sites/default/files/sns/files/supersymmetry-and-morse-theory-1982.pdf), J. Differential Geom. 17 (1982), 661–692, DOI 10.4310/jdg/1214437492. Primary indexed passages on p.664 (index as a graded trace) and p.677 (cohomological zero modes and form-degree conjugation) were inspected. Direct PDF retrieval returned HTTP 403; no full-paper inspection or archived reading copy is claimed. The circle formulas and pairing argument below are proved directly, not imported as an unexamined localization theorem.

## 3. A protected zero with an unprotected, exact theta response

Let \(\operatorname{Str}B=\operatorname{Tr}((-1)^NB)\). The degree-fugacity trace after removing the harmonic states is exactly
\[
\mathscr Z_{\rm exc}(\beta,y)
=\operatorname{Str}\!\left[y^N P_{\rm exc}e^{-\beta H}\right]
=(1-y)\sum_{n\ne0}e^{-\pi\beta n^2}
=(1-y)(\vartheta(\beta)-1).                              \tag{1}
\]
It is a polynomial in \(y\), not a formal convergence assertion. At the supersymmetric value \(y=1\), the trace is identically zero, as are all its thermal derivatives. Its **degree-fugacity response** contains all the nonzero spectrum:
\[
\Theta_{\rm exc}(\beta):=
-\left.\partial_y\mathscr Z_{\rm exc}(\beta,y)\right|_{y=1}
=\operatorname{Str}[Oe^{-\beta H}]
=\vartheta(\beta)-1,\qquad O=-NP_{\rm exc}.                \tag{2}
\]
This is an insertion, not a normalized expectation: division by the protected zero \(\mathscr Z_{\rm exc}(\beta,1)\) is neither performed nor meaningful.

Apply the prescribed source reconstruction, with no omitted zero-mode or factorial terms:
\[
p(u)=\tfrac12e^u\Theta_{\rm exc}(e^{4u}),\qquad
\Phi(u)=\tfrac18(p''-p)
=e^u\left(\beta^2\partial_\beta^2+\tfrac32\beta\partial_\beta\right)
\Theta_{\rm exc}(\beta)\big|_{\beta=e^{4u}}.                \tag{3}
\]
Equivalently,
\[
\boxed{\Phi(u)=e^u\operatorname{Str}\!\left[
O\left(\beta^2H^2-\tfrac32\beta H\right)e^{-\beta H}\right]
_{\beta=e^{4u}}.}                                        \tag{4}
\]
Expanding the two states \(n,\,-n\), \(n\ge1\), yields exactly
\[
\Phi(u)=\sum_{n\ge1}
\left(2\pi^2n^4e^{9u}-3\pi n^2e^{5u}\right)
e^{-\pi n^2e^{4u}}.
\]
The sign and factor \(3/2\) in (3)–(4) are part of the match. This is the unchanged full source; no primitive-only or squared-amplitude surrogate is substituted.

This offers a useful precise interpretation: theta is the response **transverse to the protected point** of a supersymmetric circle theory. The model is supersymmetric, but this response is not a protected observable. The following calculation determines exactly why.

## 4. Where protection fails, with its surviving Ward term

Since \(NQ=Q\) and \(QN=0\) in this one-dimensional complex,
\[
[Q,N]=-Q,\qquad [Q,y^N]=(1-y)Q,\qquad
\boxed{[Q,O]=Q P_{\rm exc}=Q\ne0.}                       \tag{5}
\]
The fugacity insertion is \(Q\)-closed at \(y=1\), but differentiating in \(y\) leaves the \(Q\)-closed class. It is not a protected refinement by a charge commuting with the selected supercharge. No additional compensating symmetry has been constructed.

For the displayed \(O\) (or an even Fourier-block-preserving insertion with convergent operator products), graded cyclicity on finite Fourier sums and the heat-trace limit give
\[
\partial_\beta\operatorname{Str}(Oe^{-\beta H})
=-\operatorname{Str}(OH e^{-\beta H})
=\operatorname{Str}([Q,O]Q^\dagger e^{-\beta H}).          \tag{6}
\]
For the actual \(O\), this becomes the explicit nonzero term
\[
\boxed{\partial_\beta\Theta_{\rm exc}(\beta)
=\operatorname{Str}(QQ^\dagger e^{-\beta H})
=-2\sum_{n\ge1}\pi n^2e^{-\pi\beta n^2}<0.}              \tag{7}
\]
Thus a formal argument setting the \(Q\)-variation to zero deletes the very thermal response required to reconstruct theta. The failure is **observable closure**, not an anomaly, a noncompact target, a hidden boundary term, or a missing cancellation in a regulated trace. The circle is compact without boundary, and all sums are absolutely convergent. In the reconstructed insertion in (4), the energy polynomial commutes with \(Q\), but multiplication by it does not repair (5); its explicit \(\beta\) dependence must also be retained in any further variation.

### Scoped protected-insertion obstruction

Consider the following exact class: a fixed, even operator \(B\), independent of \(\beta\), preserving the \(H\) eigenspaces, commuting with \(Q\) on the Fourier core, and with absolutely convergent graded heat traces for \(\beta>0\). Bounded such operators suffice; polynomial energy growth is also allowed. On a positive-energy eigenspace, \(Q\) is an isomorphism from degree zero to degree one. The relation \([Q,B]=0\) makes the two restrictions conjugate, so their ordinary traces agree. Their contributions to \(\operatorname{Str}(Be^{-\beta H})\) cancel at **each** positive energy.

Consequently
\[
\operatorname{Str}(BP_{\rm exc}e^{-\beta H})=0,\qquad
\operatorname{Str}(Be^{-\beta H})
=\operatorname{Tr}_{\mathcal H^0_{\rm harm}}B
-\operatorname{Tr}_{\mathcal H^1_{\rm harm}}B,
\]
the latter independent of \(\beta\). Applying the same reconstruction (3) to either case gives zero: a constant trace contributes only a multiple of \(e^u\) to \(p\), annihilated by \(\partial_u^2-1\).

Therefore **no insertion in this fixed compact-circle \(Q\)-closed class can match the nonzero canonical \(\Phi\) through the stipulated reconstruction**. The actual insertion \(O\) lies outside the class precisely by (5), and gives the exact match (4). Allowing arbitrary explicit \(\beta\)-dependent scalar factors would no longer obtain information from protection and is not covered by this no-go statement. Different complexes, boundaries, equivariant supercharges, interacting theories, enlarged observables and four-dimensional moduli problems are also outside its scope.

This resolves the bounded feasibility gate: the selected protected observable fails, while its unprotected physical realization remains exact.

## 5. Coefficients, multi-copy observables and the first two orders

Define the linear response functional
\[
\mathcal L_n[\Theta]=\frac1{(2n)!}
\int_0^\infty u^{2n}e^u
\left(\beta^2\Theta''(\beta)+\tfrac32\beta\Theta'(\beta)\right)
_{\beta=e^{4u}}du,\qquad n\ge0,
\]
and \(\mathcal L_n=0\) for \(n<0\), as the prescribed coefficient convention. Equations (2)–(4) give \(c_n=\mathcal L_n[\Theta_{\rm exc}]\). For \(r\) independent copies of the same fixed circle model,
\[
D_{r,k}=\sum_{\sigma\in S_r}\operatorname{sgn}(\sigma)
\prod_{i=0}^{r-1}\mathcal L_{k+\sigma(i)-i}[\Theta_{\rm exc}]. \tag{8}
\]
Here \(\sigma\) permutes \(0,\ldots,r-1\). This is an explicitly antisymmetrized multi-copy response, generally nonlocal in the thermal parameter because each functional integrates \(u\). Every insertion has even degree zero. The determinant order is not a differential-form degree or the dimension of a moduli space. Equation (8) is an exact observable dictionary, not a claim that a new local \(2r\)-point field operator has been found.

At \(r=1\), \(D_{1,k}=c_k\), with the exact factorial \((2k)!\). In particular \(c_0>0\): for \(u\ge0\) each source summand is positive since \(\pi n^2e^{4u}>3/2\). The protected replacement gives all \(c_k=0\) and already fails this first check.

At \(r=2\), the convention is
\[
D_{2,k}=c_k^2-c_{k-1}c_{k+1},\qquad D_{2,0}=c_0^2
\quad(c_{-1}=0).
\]
The relative minus sign survives. It is not a squared norm obtained by pairing unrelated adjoint observables. The accepted \(R'>0\) supplies the existing \(D_{2,k}>0\), but no positivity is newly deduced from supersymmetry.

Since the source in (4) is literally the original \(\Phi\), all its derivative determinants, \(h_3\), its negative origin region, \(M_3=ZA\), and the complete signed curvature are unchanged. The \(s\) tilt is not generated by \(H\). No positive supersymmetric Hilbert space converts this signed Mellin response to an ordinary variance, and none of (1)–(8) bounds it by \(\kappa_3\).

## 6. Domains and controls

For every \(\beta>0\), fixed thermal derivatives are absolutely summable because \(\sum n^{2m}e^{-\pi\beta n^2}<\infty\). In the source range \(u\ge0\), \(\beta\ge1\), convergence is uniform on compact sets and all derivatives of fixed order are legitimate. At \(u=0\), the complete canonical source is smooth and even; the exact trace reconstruction retains its full reflection properties. At \(u\to\infty\), the differentiated sums have double-exponential decay. These facts pay the coefficient integrals and their fixed derivative versions.

The unchanged \(M_3\) has the already recorded integrability at origin, coincident nodes and spatial infinity, including fixed logarithmic insertions at \(s=0\). The present route introduces no new chamber quotient or removed domain. Nevertheless **the response inequality is unpaid on all \(s\ge0\)**: \([0,2]\), all other compact values and the unbounded Mellin tail. Thermal \(\beta\to\infty\), spatial \(u\to\infty\), and \(s\to\infty\) are not interchangeable.

| Control | Exact premise / tested scope |
| --- | --- |
| Gaussian | Fails the chosen unchanged circle-spectrum reconstruction. Its known curvature equality is only a normalization benchmark; this branch supplies no Gaussian-to-theta transfer. |
| Euler-factor sources | Modified source reconstruction fails the literal match (4). The abstract supersymmetric pairing obstruction is source-insensitive; it gives no new exclusion or sign for these controls. Their corresponding complete response remains untested here. |
| Weighted-square / finite-square sources | Fixed weights can be encoded by replacing \(O\) with \(-Nw(H)P_{\rm exc}\), but then the observable is changed and \([Q,O]=w(H)Q\) generally remains nonzero. The selected unchanged spectrum/weight condition fails. No full reflection or response bound is inferred. |
| Reflected super-Gaussian and positive-primitive / smooth-shape controls | Do not equal the stipulated full theta trace and reconstruction. A different physical realization is not ruled out. Generic Hilbert-space positivity and a supersymmetric doubling could also be available for other data; neither is the missing signed estimate. |
| Two-point association relaxation | Has no claimed circle-source realization. Its existing failure blocks an association-only conclusion; it is not a counterexample to the explicit spectral dictionary. |

Positive-time collision controls are not counterexamples to a time-zero finite-order theorem. The source match distinguishes the canonical input, but identification alone adds no quantitative allowance.

## 7. What survives as a physical reformulation

The selected theory is fully specified before the zeta coefficients are inserted: compact circle, de Rham supercharge, square spectrum, harmonic subtraction and degree fugacity. The complete theta source is the mixed thermal/degree response (3) of its protected zero. The \(D_{r,k}\) are the signed antisymmetrized multi-copy functionals (8). This is a concrete physical formulation worth retaining independently of a proof attempt; it identifies exactly which observable supersymmetry would have to control.

The limitation is equally concrete. Ordinary cohomological protection projects to harmonic data, whereas the desired response lives in the excited spectrum. Differentiating the fugacity at the protected point leaves the \(Q\)-closed sector, and (7) is the resulting nonvanishing Ward term. Any advanced localization argument must retain and estimate that term or supply a genuinely different protected construction with an exact match. Simply invoking the index erases the target.

This is not presented as a new theory in the literature, a newly proved RH equivalence, or a Mellin advance. Translating an existing all-order coefficient criterion through (8) leaves all its quantifiers and positivity obligations in place. The new bounded output here is the explicit response/protection distinction and the scoped failure of the selected protected class.

**Next: [E] MC06-E01 — Sol.** Check the frozen formulas, domains, matching and no-go scope. No further physical model, numerical campaign or claimed positivity consequence is issued by this return.

[packet]: ../../notes/05_CONTINUATION_PARALLEL_PHYSICAL_DIRECTIONS_20261101.md
[overview]: ../research-overview/01_TOPOLOGICAL_FIELD_THEORY_RESEARCH_OVERVIEW_20261101.md
[progress]: ../research-progress/01_TOPOLOGICAL_FIELD_THEORY_RESEARCH_PROGRESS_20261101.md
[launch]: ../../numerics/PARALLEL_PHYSICAL_LAUNCH_RECORD_20261101.json
[physical]: ../../notes/04_FERMIONIC_CORRELATORS_AND_PHYSICAL_INTERPRETATIONS_20261101.md
[initial]: ../../notes/01_INITIAL_BRANCH_EVALUATION_20261101.md
[signreview]: ../../../reviews/01_J_E03_GLOBAL_SIGN_AND_SIGNED_AVERAGING_ASSESSMENT_20261101.md
[comparative]: ../../../reviews/02_PARALLEL_BRANCH_EVALUATION_REVIEW_20261101.md
[routes]: ../../notes/03_IDEAS_AND_POSSIBLE_ROUTES_20261101.md
[parent]: ../../research-overview/01_MELLIN_CURVATURE_RESEARCH_OVERVIEW_20261101.md
[sources]: ../../../../references/06_PHYSICAL_INTERPRETATION_SOURCES_20261101.md
[results]: ../../../../../../../result-summaries/README.md
[channels]: ../../../../../../../result-summaries/06_physical_channels_wzw_ym_and_collar.md
[theta]: ../../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../../avoid/README.md
[target]: ../../../../../../../avoid/01_restating_the_target.md
[rereal]: ../../../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md
[scope]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
