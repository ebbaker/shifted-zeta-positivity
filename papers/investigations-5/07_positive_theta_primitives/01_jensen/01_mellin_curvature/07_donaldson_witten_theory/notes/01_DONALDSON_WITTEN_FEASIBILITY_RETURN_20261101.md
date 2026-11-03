# Donaldson Witten assessment on the complex projective plane

1 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. **MC07-B01**, B — conceptual assessment; actual author/coordinator **gpt-6-astra / ultra**. Two read-only Astra/ultra source scouts examined disjoint primary-source questions; the coordinator selected and worked the candidate below. Separate MC07-E01 checking is requested, not presumed complete by this return.

**Outcome:** the full canonical theta source is recovered exactly from a normalized flux response inside the four-dimensional Donaldson–Witten u-plane integrand on \(\mathbb{CP}^2\). The selected complete protected surface correlator does **not** equal the theta coefficient generating function: its degree selection forces a zero where theta has a strictly positive coefficient. K3 supplies a genuine Donaldson realization of the Gaussian benchmark. These are useful physical dictionaries and a scoped matching obstruction; no new Mellin bound, Donaldson-invariant formula for RH or universal TQFT exclusion is obtained.

## 1 Candidate selection and the unchanged target

Two entry points were compared. The K3 projected Donaldson series is already a Gaussian on a homology ray, so it naturally describes the comparison model. The \(b_2^+=1\) u-plane construction retains an infinite flux lattice, making it a closer candidate for the complete theta source. **Select \(\mathbb{CP}^2\), gauge group SU(2), and its protected surface correlator.** No second four-manifold construction is worked after this choice.

The target remains
\[
\vartheta(\beta)=\sum_{n\in\mathbb Z}e^{-\pi\beta n^2},\qquad
\Phi(x)=e^x\left(\beta^2\partial_\beta^2+
 \frac32\beta\partial_\beta\right)\vartheta(\beta)
 \bigg|_{\beta=e^{4x}},\quad x\ge0,                                      \tag{1}
\]
\[
c_n=\frac1{(2n)!}\int_0^\infty x^{2n}\Phi(x)\,dx,\qquad
B_\theta(z)=\sum_{n\ge0}c_nz^{2n}=\frac18\xi((1+z)/2),\qquad
D_{r,k}=\det[c_{k+j-i}],\quad c_n=0\ (n<0).                              \tag{2}
\]
These are the complete source and inherited normalization in [Synthesis06](../../notes/06_PARALLEL_PHYSICAL_DIRECTIONS_SYNTHESIS_20261101.md). In particular \(c_0,c_1>0\). No zero hypothesis is used to obtain that positivity. At rank one a proposed coefficient dictionary must reproduce every \(c_n\), not just \(c_0\). The signed higher-rank determinant is not replaced by an absolute value or square.

## 2 The genuine four-dimensional dictionary

Use the following specified data, in the conventions of [Moore–Witten, hep-th/9709193v2][MW], Sections 1–3 and 9. This is the published low-energy physical representation with its coefficientwise regularization, not a new constructive definition of a quantum-field-theory measure.

| Item | Selected data |
| --- | --- |
| Manifold and metric data | \(X=\mathbb{CP}^2\), complex orientation, positive generator \(H\), \(H^2=1\); period point \(\omega=H\), a positive-scalar-curvature metric; \(b_1=0,b_2^+=1,b_2^-=0,\chi=3,\sigma=1\) |
| Gauge and topology | SU(2), equivalently the \(w_2(E)=0\) sector of the SO(3) description; sum over instanton numbers, with this bundle parity fixed |
| Geometric object | Anti-self-dual connection moduli spaces with the Donaldson point and surface classes, of degrees four and two |
| Theory and symmetry | Topologically twisted four-dimensional \(N=2\) Yang–Mills; gauge connection, adjoint scalar fields and twisted fermionic forms; scalar charge \(Q\) squares to a gauge transformation and is nilpotent on gauge-invariant observables |
| Protected observables | The point observable \(\mathcal O\) and descended surface observable \(I(H)\); \(Q I(H)=0\). The generating function is \(Z_D(p,t)=\langle e^{p\mathcal O+tI(H)}\rangle\), with the source's factorial convention |
| Low-energy variables | Coulomb coordinate \(U\), special coordinate \(a\), electromagnetic coupling \(\tau_{\rm em}=\xi+iy\), and \(J(\tau_{\rm em})=dU/da\) |
| Full integration | The modular region \(\mathcal M=\Gamma^0(4)\backslash\mathbb H\), including cusp limits and contact terms; \(\Gamma^0(4)\) has upper-right matrix entry divisible by four |

The standard Q/Donaldson interpretation is recorded in [Witten 1988][W88], Sections 2, 3 and 5. In this example the Seiberg–Witten contribution vanishes, so the full Donaldson generating function is the u-plane contribution. This does not remove its modular integral. Fix the stated period point and conventions; no assertion about arbitrary metric or chamber changes is needed.

The actual candidate for matching (2) is the **protected inserted correlator**
\[
\mathcal C_D(z)=-\frac23\,
 \partial_t Z_D(0,t)\big|_{t=z}
=-\frac23\left\langle I(H)e^{zI(H)}\right\rangle.                         \tag{3}
\]
The constant uses Moore–Witten's low-degree normalization, checked below. Compare it with \(B_\theta(z)/c_0\), allowing at most a nonzero overall constant and a nonzero linear source rescaling through zero. Arbitrary nonlinear substitutions, affine shifts away from zero, adjustable point-observable factors and target-coefficient insertions are outside this declared candidate.

## 3 Exact theta recovery from the flux response

Write \(\tau=\tau_{\rm em}\) in this section only. Specialize the flux factor \(\Psi\) in Moore–Witten (3.18). Here \(S=tH\), \(\lambda=nH\), \(\lambda_0=0\), \(\lambda_-=S_-=0\), and \(w_2(X)=H\bmod2\). Thus
\[
\Psi(\tau,t)
=\sum_{n\in\mathbb Z}(-1)^n
 \left(n+\frac{it}{4\pi y}J(\tau)\right)e^{-i\pi\bar\tau n^2}
=\frac{it}{4\pi y}J(\tau)\,\overline{\vartheta_4(\tau)}.                 \tag{4}
\]
The \(n\) term cancels by \(n\leftrightarrow-n\); all modes in the even term remain. Absolute convergence for \(y>0\) justifies that pairing and differentiation on compact subsets. The complex conjugation is essential. Here \(\vartheta_4(\tau)=\sum_n(-1)^n e^{i\pi\tau n^2}\).

Define the normalized response on the chosen electromagnetic-frame line
\[
\mathcal R(\beta)=\frac{4\pi\beta}{iJ(1+i\beta)}
 \partial_t\Psi(1+i\beta,0),\qquad\beta>0.                              \tag{5}
\]
The normalization is well-defined: Moore–Witten (4.6) gives
\(da/dU=\vartheta_2\vartheta_3/2\), whose product expansions in Appendix A are nonzero in \(\mathbb H\). Substitution into (4) gives directly
\[
\mathcal R(\beta)
=\sum_{n\in\mathbb Z}(-1)^{n+n^2}e^{-\pi\beta n^2}
=\sum_{n\in\mathbb Z}e^{-\pi\beta n^2}
=\vartheta(\beta).                                                       \tag{6}
\]
This uses the exact integer identity \(n+n^2\in2\mathbb Z\), not a truncation. Consequently
\[
\Phi(x)=e^x\left(\beta^2\mathcal R''(\beta)+
 \frac32\beta\mathcal R'(\beta)\right)_{\beta=e^{4x}}.                   \tag{7}
\]
The zero-flux term is removed by differentiation; both signs of every nonzero flux supply the correct multiplicity. Expanding (7) gives
\(e^x\sum_{n\ge1}(2\pi^2\beta^2n^4-3\pi\beta n^2)e^{-\pi\beta n^2}\), precisely (1). Differentiating the *normalized full expression* in (5) is required; differentiating only \(\Psi\) while freezing its \(\beta/J\) prefactor changes the source.

Equations (5)–(7) are a four-dimensional **flux-response representation** of the full source. They are not an equality with a Donaldson invariant. The coupling is fixed and a particular frame and line are chosen before the modular integration. Dividing out the special-coordinate factor is also part of this extraction. No protected observable that imposes this restriction on the full path integral has been constructed.

## 4 What the full invariant retains and why the match fails

For clarity, retain the full expression from Moore–Witten (3.20)–(3.21):
\[
Z_D(p,t)=\operatorname{Reg}\!\int_{\mathcal M}
 \frac{d\xi\,dy}{\sqrt y}\,\mu(\tau)
 e^{2pU+t^2\widehat T(\tau)}\Psi(\tau,t),                               \tag{8}
\]
\[
\widehat T=T+\frac{J^2}{8\pi y},\qquad
T=-\frac{E_2(\tau)J^2-8U}{24},\qquad
\mu(\tau)=-4\sqrt2,i(U^2-1)\frac{da}{dU}
 \left[\frac{((2i/\pi)dU/d\tau)^2}{U^2-1}\right]^{1/8}.                 \tag{9}
\]
The fractional-power branch is the source's electromagnetic-frame convention. It is not a positive scalar measure. \(\operatorname{Reg}\) means expansion to each fixed degree in \(p,t\), cusp cutoffs in the respective dual coordinates, integration in the real modular coordinate before removing the height cutoff, as in Section 3.2. An absolutely convergent unexpanded generating integral is not assumed.

After (4), at \(p=0\) write
\[
Z_D(0,t)=t\,\operatorname{Reg}\!\int_{\mathcal M}
 \frac{d\xi\,dy}{\sqrt y}\,\mu\frac{iJ}{4\pi y}
 \overline{\vartheta_4}\,e^{t^2\widehat T}.
\]
The protected insertion in (3) therefore differentiates to the full factor
\[
(1+2t^2\widehat T)e^{t^2\widehat T}.                                    \tag{10}
\]
Omitting the derivative of the contact exponential would compute a different object. Replacing this two-dimensional regularized integral by the line in (5) would also compute a different object.

The decisive obstruction does not require numerical integration. In the standard SU(2) instanton-number convention \(k=c_2\), the formal moduli dimension on \(\mathbb{CP}^2\) is \(8k-6\). Equivalently it is \(2\bmod8\); Witten (3.13) gives this index formula in his instanton notation. His symbol \(p_1\) should not be confused with the modern Pontryagin class of the adjoint bundle. With \(N\) surface insertions and \(m\) point insertions, degree matching is
\[
2N+4m=8k-6.
\]
For the declared \(p=0\) candidate, \(m=0\), so \(N\equiv1\pmod4\). Hence, as formal series,
\[
Z_D(0,t)=\sum_{j\ge0}A_jt^{4j+1},\qquad
\partial_tZ_D(0,t)=\sum_{j\ge0}(4j+1)A_jt^{4j}.                          \tag{11}
\]
The coefficient of \(z^2\) in (3) is zero. It remains zero after any allowed overall normalization and linear rescaling \(z\mapsto\alpha z\), \(\alpha\ne0\). In contrast,
\[
[z^2]\frac{B_\theta(z)}{c_0}=\frac{c_1}{c_0}>0.                         \tag{12}
\]
Thus the proposed protected-invariant match fails already for the rank-one coefficient sequence. This is a formal coefficient obstruction; no analyticity claim for \(Z_D\) is necessary. Contact corrections and the prescribed regularization respect the degree selection. We do not apply the \(b_2^+>1\) simple-type theorem to \(\mathbb{CP}^2\).

The normalization and a rank-two convention check are available from Moore–Witten (9.24). Their \(p=0\) coefficients begin
\[
Z_D(0,t)=-\frac32t+\frac{t^5}{5!}+\frac{3t^9}{9!}+\cdots,
\qquad
\mathcal C_D(z)=1-\frac{z^4}{36}-\frac{z^8}{20160}+\cdots.              \tag{13}
\]
Keep this published low-degree convention; do not assert that its linear term vanishes. If \(\mathcal C_D(z)=\sum_nd_nz^{2n}\), then
\(d_0=1,d_1=0,d_2=-1/36\) and
\(\det[d_{1+j-i}]_{i,j=0}^1=d_1^2-d_0d_2=1/36\).
A positive minor here does not repair the failed coefficient identity. For the source reconstructed by (7), the original checks are instead exactly
\(D_{1,k}=c_k\), \(D_{2,0}=c_0^2\), and \(D_{2,k}=c_k^2-c_{k-1}c_{k+1}\); these follow by retaining (1)–(2), not by transferring signs from (13).

The exclusion is for this manifold, bundle parity, point specialization, protected insertion and parameter matching. It does not cover nonzero or variable point sources, other insertions, other bundle classes, other manifolds, boundary/family theories, or independently justified integral transforms. Those alternatives have not been assessed here. Merely choosing a reparametrization to insert the desired coefficients would not supply independent geometric information.

## 5 The K3 comparison and the physical lesson

The short alternative screen has a positive outcome of its own. [Kronheimer–Mrowka][KM], Definition 1.4, (1.5) and K3 Example 1, give for the standard orientation and \(w=0\)
\[
\mathcal D_{K3}^0(h)
=D_{K3}^0\big((1+\mathfrak p/2)e^h\big)=e^{Q(h)/2},                     \tag{14}
\]
where \(\mathfrak p\) is the point generator. This is the projected Donaldson series, not \(D(e^h)\). For a Gaussian source \(Ce^{-a x^2}\), \(a>0\), direct Gaussian integration gives
\[
\frac{B_G(z)}{B_G(0)}=e^{z^2/(4a)}.
\]
Choose a real homology class \(S\) with \(Q(S)=1/(2a)\). Then (14) at \(h=zS\) equals this normalized comparator. Real scaling is allowed by polynomial extension of the invariants; integral homology with arbitrary prescribed norm is not being asserted. Its coefficient check is \(d_n=\lambda^n/n!\) and \(D_{2,k}=d_k^2/(k+1)\), \(\lambda=1/(4a)\).

This supplies a precise Donaldson interpretation of the existing Gaussian reference model. It establishes no inequality comparing two different four-manifold expressions, and no identification of the complete canonical source with the K3 series. The broader finite-basic-class structure theorem is background only; no general simple-type exclusion is needed for the selected CP2 assessment.

Unlike MC06, the selected complete observable (3) is Q-closed. Its failure is the coefficient match, not the loss of Q-closure. Conversely, the exact theta extraction (5) retains a coupling-dependent flux response before protection and integration have produced an invariant. Thus the four-dimensional work genuinely adds a different dictionary and a different obstruction to the circle result. A final RH equivalence through a protected Donaldson invariant remains unconstructed.

## 6 Controls and the complete Mellin question

| Control or check | Meaning for this candidate |
| --- | --- |
| Gaussian source | Has the exact K3 comparator realization (14); this supplies no canonical theta comparison |
| Weighted or finite square sources | Would change the uniform unshifted flux sum in (6); they do not satisfy this exact selected source dictionary. Their collision results are not tests of the full modular integral |
| Euler-factor, reflected and smooth-shape controls | No matching CP2 protected observable is established for these altered sources; their unknown response signs are not assigned here |
| Any nonzero positive source with finite first moments | Has \(c_1>0\); the coefficient-gap argument also stops the same protected-series identification. This obstruction is broader than theta but remains a restriction on the selected map |
| Rank one and rank two | (12) stops the invariant match; (13) checks factorials and determinant orientation only; (7) preserves the exact original coefficients and signed determinants |

Use the [result index][results], [control screen][controls] and [avoid index][avoid], especially [factor versus target][factor] and [scoped exclusions][scopes]. No control is claimed to have passed an unproved theta-specific inequality. A theta factor inside a physical expression and a complete protected observable have been kept separate throughout.

The Mellin consumer remains the full signed expression
\[
\mathcal C_3(s)=\operatorname{Var}_sT+
\frac{\operatorname{Cov}_s(h_3,(T-E_sT)^2)}{E_sh_3}
-\left(\frac{\operatorname{Cov}_s(h_3,T)}{E_sh_3}\right)^2.
\]
No term has acquired a bound from (4)–(14). The electromagnetic \(\tau\), source coordinate \(x\), surface parameter \(t\), and Mellin tilt \(s\) have different roles. All signed regions, including the negative source contribution in the original determinant observable, remain. There is no new interval of the Gaussian comparison, integrated neighboring-index inequality or coefficient positivity.

## 7 Disposition and separate checking

The bounded assessment is complete at the following scope: a complete-source four-dimensional flux-response identity, a proved coefficient mismatch for one genuine protected correlator, and a K3 interpretation of the Gaussian comparator. No numerical campaign, new model search or novelty claim is part of the return. The [source record][sources] and [small return record](../numerics/MC07_B01_RETURN_RECORD_20261101.json) identify primary passages, archived PDFs and fixed algebra checks.

**Next: [E] MC07-E01 — Sol.** Independently check the frozen return: the CP2 dictionary and index degree, all phases/conjugations and half-lattice choices in (4)–(7), \(J\)'s nonvanishing domain, the complete contact derivative and cusp prescription, factorials and the zero coefficient in (11)–(13), and the projected K3 normalization. Check the exact r=1/r=2 and control scopes. Replay only the fixed rational bookkeeping. Accept at the stated scope, correct, or identify a specific unresolved import; do not introduce a new theory or infer a Mellin inequality. After that check, integrate this additional direction into the overall J-B10 brainstorm. Do not automatically launch any unassessed alternative listed in Section 4.

[MW]: https://arxiv.org/pdf/hep-th/9709193v2
[KM]: https://people.math.harvard.edu/~kronheim/structhm.pdf
[W88]: https://www.ias.edu/sites/default/files/sns/%5B109%5DCommMathPhys117-1988.pdf
[sources]: ../../../../references/08_DONALDSON_WITTEN_ASSESSMENT_SOURCES_20261101.md
[results]: ../../../../../../../result-summaries/README.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../../avoid/README.md
[factor]: ../../../../../../../avoid/13_a_factor_is_not_the_target.md
[scopes]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
