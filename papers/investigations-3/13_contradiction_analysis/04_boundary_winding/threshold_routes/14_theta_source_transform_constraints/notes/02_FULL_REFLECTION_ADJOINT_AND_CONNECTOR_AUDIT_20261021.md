# Full reflection adjoints, finite-source connectors and the direct comparator

21 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**,
reasoning effort **max**. Analytic audit and bounded numerical regression;
assessment is by the authoring assistant only, with no independent
specialist review or priority claim.

## 1. Decision and frozen question

This executes the next step selected after [Note 01][n01]: apply the full
source reflection before estimating the coupled physical first jet
\(J=(H,H_z)\), and determine whether its adjoint subtraction supplies an
estimate beyond the existing reflected-contour evaluator.

The answer is scoped and negative for the tested operation. Reflection
projects the exponential kernel onto its cosine part. In the declared
pointwise source-error norm, that projection is already the optimal direct
reflection-aware bound; its allowance ratio to that comparator is exactly
one. Contour shifting of the complete source gives the already available
paired evaluator. A finite theta prefix instead has an explicit vertical
connector, proved below for complex heat time and spectral coordinate.
Discarding that connector changes the physical value and derivative.

This is a boundary-term and same-information audit, not a new theta
nonvanishing criterion. The retained signed arithmetic estimate remains
open. The following distinctions are essential:

- The complete shifted formula, its mode-tail bound and the cancellation
  warning are inherited from [the arithmetic manuscript, Section 7][shifted].
- The explicit reflection-defect connector is also already present in
  [S01, Section 2][s01-note], including its derivative factor. It is
  rederived here with complex-time payments. The optimality statement
  for the specified relaxed error class supplies the scoped comparison;
  no novelty claim is made.
- [S01][s01] already improves a **paired nonstationary tail** by estimating
  its signed endpoints before taking absolute values. The present audit
  neither supersedes that result nor rules out other signed estimates.

The [result index][results], [theta/arithmetic cluster][arithmetic],
[collision controls][controls] and [avoid index][avoid] govern this
continuation. In particular, apply [target classification][a01],
[matching premises][a02], [coordinate rewrites][a03], [scoped stops][a07]
and [complete signed comparisons][a12]. The intended recipient is the
physical first-jet observation in BW-11–13, not a positive norm on the
elliptic source family.

**Comparison fixed before the diagnostic.** Use the unchanged source,
the same value/derivative pair, the same contour and retained modes,
and the same complete tail and acquisition payments. An adjoint operation
passes only if it supplies an independently bounded residual or reduces
the complete error/cost relative to the reflection-aware direct evaluator.
The diagnostic fixes \(d=\pi/16\), \(|t|\le1/2\),
\(\Re z\ge0\), \(|\Im z|\le1\); it checks connector identities and
a matching collision control. It is not a theta sign or coverage pilot.

## 2. Source and two contour formulas

Retain the exact source convention of Note 01, including the covariant
lower-order correction and the cancellation of the zero lattice mode:
\[
 \lambda_n=\pi n^2,\qquad
 \phi_n(v)=(2\lambda_n^2e^{9v}-3\lambda_ne^{5v})
                  e^{-\lambda_ne^{4v}},\qquad
 \Phi(v)=\sum_{n\ge1}\phi_n(v).
 \tag{1}
\]
The complete source is holomorphic and even in
\(|\Im v|<\pi/8\). Normal convergence holds on every compact subset
of that strip, since \(\Re(e^{4v})>0\). Theta inversion first proves
reflection on the real axis, then the identity theorem extends it to
the strip. This is the [inherited modular identity][shifted]; the
underlying theta transformation is [DLMF 20.7.32][dlmf].

For any source \(A\) holomorphic on a neighborhood of the two closed
right half-strips of height \(d<\pi/8\), with enough decay to remove
their remote vertical sides, set
\[
 H_A(t,z)=\int_0^\infty e^{tu^2}A(u)\cos(zu)\,du,
 \tag{2}
\]
\[
 P_{A,d}(t,z)=\frac12\int_0^\infty
 \left[e^{t(u+id)^2}A(u+id)e^{iz(u+id)}
       +e^{t(u-id)^2}A(u-id)e^{-iz(u-id)}\right]du.
 \tag{3}
\]
The finite sums \(A=\Phi_N=\sum_{n\le N}\phi_n\), and the complete
\(A=\Phi\), satisfy the hypotheses locally uniformly in all complex
\((t,z)\). For example, on either positive half-strip,
\[
 |\phi_n(u+i\eta)|\le(2\lambda_n^2+3\lambda_n)
       e^{9u-\cos(4d)\lambda_ne^{4u}},\quad |\eta|\le d.
 \tag{4}
\]
Polynomial jet factors and the heat and spectral weights are dominated
by this superexponential decay on compact parameter sets.

**Connector identity.** Write \(D_A(v)=A(v)-A(-v)\). Then
\[
 \boxed{H_A=P_{A,d}+C_{A,d}},\qquad
 C_{A,d}(t,z)=\frac12\int_0^{id}e^{tv^2+izv}D_A(v)\,dv
 =\frac i2\int_0^d e^{-ts^2-zs}D_A(is)\,ds.
 \tag{5}
\]
To prove it, shift the positive-exponential half-line upwards and the
negative-exponential half-line downwards. The first vertical contribution
is \(\int_0^{id}e^{tv^2}A(v)e^{izv}dv\); the second is
\(\int_0^{-id}e^{tv^2}A(v)e^{-izv}dv\). In the second set \(v=-w\),
giving the negative of the first integral with \(A(v)\) replaced by
\(A(-v)\). Their half-sum is (5). This proof uses no conjugacy
assumption and therefore also covers complex \(t,z\).

For every fixed nonnegative integer \(j\), differentiation at **fixed
\(d\)** gives
\[
 C_{A,d}^{(j)}(t,z)=\frac i2\int_0^d(-s)^j
             e^{-ts^2-zs}D_A(is)\,ds.
 \tag{6}
\]
The finite segment and (4) justify all derivatives. Choosing a contour
as a function of height for evaluation does not license differentiating
that choice in this formula.

For \(A=\Phi\), \(D_A=0\), so \(H=P_{\Phi,d}\) exactly. This
is the existing complete shifted evaluator. For a finite prefix,
\(D_{\Phi_N}\) is generally nonzero. With
\(P_N=P_{\Phi_N,d}\), \(C_N=C_{\Phi_N,d}\), and
\(P_{>N}=P_{\Phi-\Phi_N,d}\), the two correct residuals are
\[
 \boxed{H-P_N=P_{>N}},\qquad
 \boxed{H-H_{\Phi_N}=P_{>N}-C_N}.
 \tag{7}
\]
Indeed \(C_{\Phi-\Phi_N}=-C_N\). A shifted finite approximation
\(P_N\) is legitimate, but it is a different approximation from the
ordinary half-line finite sum \(H_{\Phi_N}\).

Even extension \(\Phi_N(|u|)\) has the latter cosine transform, but
does not give a holomorphic reflected finite source. It generally has
a cusp at zero. Conversely, the analytic negative-\(u\) continuation
of each \(\phi_n\) behaves as \(-3\lambda_ne^{5u}\) as
\(u\to-\infty\); for real \(t>0\), its full-line heat integral
does not converge. The complete reflection cancels that problem before
the full-line shift. Neither finite interpretation permits silently
removing the connector.

## 3. A paid connector and its large-height behavior

For \(|t|\le T\), \(x=\Re z\ge0\), (6) gives
\[
 |C_{A,d}^{(j)}|\le\frac{e^{Td^2}}2
       \int_0^d s^j e^{-xs}|D_A(is)|\,ds.
 \tag{8}
\]
If \(|D_A(is)|\le2Ls\) on the segment, then
\[
 |C_{A,d}^{(j)}|
 \le L e^{Td^2}\int_0^d s^{j+1}e^{-xs}ds
 \le L e^{Td^2}\frac{(j+1)!}{x^{j+2}}\quad(x>0).
 \tag{9}
\]
At \(x=0\) the integral is \(d^{j+2}/(j+2)\). One admissible
\(L\) is \(\sup_{|s|\le d}|A'(is)|\); alternatively one can
evaluate the signed finite-segment integral, as in Section 7.

For the canonical prefix let \(a_N=\Phi_N'(0)\). The endpoint
notation of Note 01 gives
\[
 \gamma_n=-\phi_n'(0)
 =(8\lambda_n^3-30\lambda_n^2+15\lambda_n)e^{-\lambda_n},
 \qquad a_N=\sum_{n>N}\gamma_n>0\quad(N\ge1).
 \tag{10}
\]
Here \(\sum\gamma_n=0\) by complete reflection and
\(\gamma_n>0\) for \(n\ge2\). Thus
\(D_{\Phi_N}(is)=2ia_Ns+O(s^3)\). At fixed \(t,d,N\), Laplace
expansion at \(s=0\) in (6) yields, for real \(x\to+\infty\),
\[
 C_N^{(j)}(t,x)=(-1)^{j+1}\frac{(j+1)!a_N}{x^{j+2}}
                  +O(x^{-j-4}).
 \tag{11}
\]
For completeness, expand \(e^{-ts^2}D_{\Phi_N}(is)\) to its
linear term on a fixed small segment. The remainder is bounded by a
constant times \(s^3\); its Laplace integral is \(O(x^{-j-4})\).
The remaining segment and the finite-upper-limit correction are
exponentially small. This proves (11) without an asymptotic sum exchange.

Consequently the finite-prefix connector is generally **algebraic** in
height, even though the complete shifted mode tail carries \(e^{-dx}\).
This is consistent with the established [endpoint cancellation][modular],
not a new obstruction for the complete theta transform. The signs in
(11) are eventual signs; the two-mode diagnostic at height 30 need not
have reached that regime.

## 4. What a reflection adjoint can improve in the declared norm

This section fixes a deliberately explicit information class. Let
\(t,x\in\mathbb R\), and suppose a real source error \(r\) is
known only to be measurable, even and bounded by a nonnegative even
envelope \(\rho\), with
\(\int_0^\infty\rho(u)e^{tu^2}(1+u)du<\infty\).
Analyticity, source positivity, lattice coefficients and additional
moments are **not** encoded in this relaxed class.

Its first-jet error body is
\[
 K=\left\{\int_0^\infty r(u)e^{tu^2}
                  (\cos xu,-u\sin xu)du:\ |r|\le\rho,\ r\text{ even}\right\}
 \subset\mathbb R^2.
 \tag{12}
\]
For a real covector \(\ell=(\ell_0,\ell_1)\), write the even
function
\[
 F_\ell(u)=e^{tu^2}(\ell_0\cos xu-\ell_1u\sin xu).
 \tag{13}
\]
The original whole-line exponential kernel in this direction has even
part \(F_\ell/2\). Its other part is odd. A reflection adjoint
subtraction adds an odd kernel, the image of \((I-R)^*\), where
\(Rf(u)=f(-u)\). For any integrable odd \(b\), including complex
\(b\), pair \(u\) and \(-u\) and use the triangle inequality:
\[
 \begin{aligned}
 \int_{\mathbb R}\rho|F_\ell/2+b|du
 &=\int_0^\infty\rho
      (|F_\ell/2+b|+|F_\ell/2-b|)du\\
 &\ge\int_0^\infty\rho|F_\ell|du.
 \end{aligned}
 \tag{14}
\]
Equality is attained at \(b=0\). The last integral is also the exact
support function of (12):
\[
 \boxed{h_K(\ell)=\int_0^\infty\rho(u)|F_\ell(u)|du.}
 \tag{15}
\]
It is attained by the even error \(r=\rho\,\operatorname{sign}F_\ell\).
This admissible extremizer is typically not analytic, which is exactly
why (15) is asserted only for the stated relaxation.

Thus reflection adjoint optimization and the best direct cosine estimate
have **identical** directional allowances. When an allowance is nonzero,
their ratio is 1; zero allowances coincide as well. This is an analytic
comparison on the whole declared class, not evidence from a grid.

The statement retains coupling between the value and derivative. The
body \(K\) is compact, convex and symmetric (the image of the bounded
\(L^\infty\) ball under two integrable observations). For a known
approximate jet \(v\), its exact lower radius in this model is
\[
 \operatorname{dist}(0,v+K)
 =\max_{\|\ell\|_2\le1}\{\ell\cdot v-h_K(\ell)\}.
 \tag{16}
\]
Projection onto a closed convex set, or elementary separation, proves
the dual formula; \(\ell=0\) makes its right side nonnegative.
Replacing \(K\) with independent Cartesian intervals can lose
information. That loss does not give the adjoint an advantage over a
direct method using the **same coupled body**.

The conclusion does not extend to arbitrary analytic residual classes,
other norms, nonlocal arithmetic constraints, nonlinear observations or
different acquisition costs. In particular, contour shifting can improve
an envelope by using analyticity; (14) does not forbid that. What the
present candidate supplies after shifting is precisely (3), already
available to the direct comparator. Reflection alone contributes no
further residual estimate.

## 5. Complete mode-tail payment on the complex-time domain

To make the shifted comparison explicit, put \(m=N+1\),
\(c_d=\cos(4d)>0\), and assume
\[
 b=4c_d\pi m^2-9-Y>0,\quad 8c_d\pi m^2\ge T,\quad
 q=\left(\frac{m+1}{m}\right)^4e^{-c_d\pi(2m+1)}<1.
 \tag{17}
\]
Define
\[
 S=\frac{(2\pi^2m^4+3\pi m^2)e^{-c_d\pi m^2}}{1-q},\qquad
 K_j^{\mathbb C}=e^{Td^2}S\sum_{k=0}^j
                {j\choose k}\frac{d^{j-k}k!}{b^{k+1}}.
 \tag{18}
\]
Then, for all \(|t|\le T\), \(\Re z=x\ge0\), \(|\Im z|\le Y\),
\[
 \boxed{|\partial_z^j(H-P_N)(t,z)|\le e^{-dx}K_j^{\mathbb C}.}
 \tag{19}
\]
This is the existing absolute shifted-tail proof with the explicit
complex-time payment. Indeed
\(|e^{t(u\pm id)^2}|\le e^{T(u^2+d^2)}\), the spectral factor
is at most \(e^{-dx+Yu}\), and a derivative costs \((u+d)^j\).
The inequality \(e^{4u}\ge1+4u+8u^2\) bounds the remaining
integrand by its mode constant times \((u+d)^je^{-bu}\).
Successive mode constants have ratio at most \(q\); the complete
sum and integral give (18). No unbounded source or mode tail is dropped.

For real \(0\le t\le T\), the extra factor \(e^{Td^2}\) can be
omitted as in the inherited theorem. The manuscript's
[nonstationary estimate][nonstationary] and S01's paired endpoint
estimate are stronger comparators in their respective domains. Equation
(19) is a transparent complete allowance, not a claim to improve them.

At \(m=5,d=\pi/16,T=1/2,Y=1\), the 192-bit receipt encloses
\[
 K_0^{\mathbb C}=4.593802477333131\ldots\,10^{-23},\qquad
 K_1^{\mathbb C}=9.236451632981766\ldots\,10^{-24}.
 \tag{20}
\]
These constants include all modes \(n\ge5\) and the entire positive
source rays. They exclude retained-integral quadrature and rounding
payments. They are error allowances, not physical jet margins.

## 6. Collision controls: full reflection still passes a double event

The decisive matching example is the existing
[reflected super-Gaussian control][reflected]. With \(T_*=1/4\), set
\[
 g(u)=e^{-u^4}+\tfrac12e^{-(u-4)^4}+\tfrac12e^{-(u+4)^4},
 \qquad \Phi_*(u)=c e^{-T_*u^2}g(u),\quad c>0.
 \tag{21}
\]
This source is positive, even and entire, and decays on every fixed
horizontal strip rapidly enough for (3)–(6) at every bounded heat time.
At \(T_*\), translation in the whole-line Fourier transform gives
\[
 H_*(T_*,x)=cF(x)(1+\cos4x),\qquad
 F(x)=\int_0^\infty e^{-u^4}\cos(xu)du.
 \tag{22}
\]
For \(M_k=\int_0^\infty u^ke^{-u^4}du\), integration by parts
and Cauchy–Schwarz give \(M_4=M_0/4\), \(M_2\le M_0/2\).
Hence \(F(x)\ge M_0(1-x^2/4)>0\) for \(|x|<2\). In particular,
\[
 H_*(T_*,\pi/4)=H_{*,z}(T_*,\pi/4)=0,\qquad
 H_{*,zz}(T_*,\pi/4)=16cF(\pi/4)>0.
 \tag{23}
\]
The complete connector vanishes for this source too. The same reflected
contour and odd-adjoint cancellation therefore coexist with a genuine
nondegenerate collision. Choosing the positive normalization in the
source note also preserves its stated primitive endpoints; the fresh
diagnostic uses \(c=1\), which leaves multiplicity unchanged.

| Control class | Reflection/adjoint screen | Premise missing from a canonical theta estimate |
| --- | --- | --- |
| Reflected super-Gaussian | Passes evenness, analytic strip shifting and vanishing connector; (23) is an exact collision. | Unchanged integer-square coefficients and theta mode-tail constants. |
| Euler-factor translated-source controls | Positive symmetric real translations preserve evenness and the analytic-strip decay needed for (3); the reflection connector vanishes. | Original level-one coefficients/conductor; theta numerical envelopes cannot be copied unchanged. |
| Weighted-square and finite-prime orbit controls | Can match selected endpoints; generally fail complete analytic reflection, so (5) retains a defect. | Full normalized reflection and unchanged complete coefficients. |
| Smooth shape / positive-primitive controls | Their stated real reflection passes the real-axis adjoint identity. No unproved complex-strip continuation is assumed here. | Canonical square expansion; any extra analytic hypotheses must be checked separately. |
| Polynomial, atomic and compact-profile controls | Useful for other jet/profile screens, but do not provide the holomorphic source with these strip tails. | The analytic source and arithmetic hypotheses used in (1), (4), (19). |

The finite-prime preservation theorem is in [the arithmetic control
note][finite-prime]. The family distinctions and their inherited review
statuses are in [the control register][controls]. No combined preservation
list is attributed to a single control. An upper error bound is not
required to fail on a collision; a proposed positive lower bound on a
domain containing that collision would have to use additional premises.

Full reflection **together with** normalized integer-square arithmetic
does determine the theta coefficients under the existing rigidity
hypotheses. That source identification is already known and does not
itself give a signed transformed estimate. This audit does not claim
that a collision control meets that conjunction.

## 7. Bounded diagnostic and all exterior tails

The [checker][checker] and [192-bit receipt][receipt] use Python 3.10.0,
python-flint 0.9.0 and its [Arb complex integration interface][flint]. All
callbacks are entire; no complex conjugation is used inside integration.
Absolute/relative requests are \(10^{-32},10^{-29}\), with finite-result
and radius guards. The source cutoff is \(U=1\). The fixed cases are
\[
 (N,t,z)=(1,1/10,30),\qquad
 (2,1/10+i/20,30+i/2).
 \tag{24}
\]
Each of \(H_{\Phi_N}^{(j)},P_N^{(j)},C_N^{(j)}\), \(j=0,1\),
is acquired independently. To cover \(u\ge U\) for each retained
mode, the checker integrates the tangent exponential majorant. On the
real ray its value at \(U\), divided by the positive decay slope, is
\[
 E^{\rm real}_{n,j}=
 \frac{2\lambda_n^2U^j
 e^{TU^2+(9+Y)U-\lambda_ne^{4U}}}
 {4\lambda_ne^{4U}-2TU-9-Y-j/U}.
 \tag{25}
\]
Here positivity of \(\phi_n(u)\) for \(u\ge0\) gives
\(\phi_n(u)\le2\lambda_n^2e^{9u-\lambda_ne^{4u}}\).
For the paired rays the corresponding bound is
\[
 E^{\rm pair}_{n,j}=
 \frac{(2\lambda_n^2+3\lambda_n)(U+d)^j
 e^{T(U^2+d^2)+(9+Y)U-c_d\lambda_ne^{4U}-dx}}
 {4c_d\lambda_ne^{4U}-2TU-9-Y-j/(U+d)}.
 \tag{26}
\]
The code checks the positive slopes and
\(16c_d\lambda_ne^{4U}>2T\) (and its real version), making the
log-majorants concave and their tangents valid on the full exterior.
It sums (25)–(26) over every retained mode and enlarges the quadrature
balls. The connector is a complete finite-segment integral. There are
no additional modes in the finite-source identities being tested.

Representative enclosed connector values are:

| Case | \(C_N\) | \(\partial_z C_N\) |
| --- | --- | --- |
| One mode, real parameters | \(-1.3866920095491027604\times10^{-5}\) | \(+3.0291896975624521060\times10^{-8}\) |
| Two modes, complex parameters | \(8.8966670152420817102\times10^{-11}-9.3559630391578081652\times10^{-12}i\) | \(-1.8303624323172220851\times10^{-11}+1.7864247170586605669\times10^{-12}i\) |

All four identity residual balls contain zero with modulus upper bound
below \(10^{-25}\); each connector and each difference
\(H_{\Phi_N}^{(j)}-P_N^{(j)}\) excludes zero. The saved receipt gives
the full enclosures, including rounding, rather than treating these
displayed centers as exact values.

For the reflected control, integrate its paired rays to \(V=8\), at
\(x=\pi/4\) and \(c=1\). For a translated quartic with
\(a\in\{0,4,-4\}\), \(u\ge V\) gives
\(\Re(u-a\pm id)^4\ge(u-a)^4/2\), because the checked inequality
\(6d^2/(V-4)^2<1/2\) suffices. Thus a full exterior allowance is
\[
 E_j^*=\frac{2e^{-dx}(V+d)^j e^{-(V-4)^4/2}}
                 {2(V-4)^3-j/(V+d)},\quad j=0,1,2.
 \tag{27}
\]
The same decreasing tangent argument proves it. The final value and
first derivative balls contain zero, and the second derivative encloses
\(13.0469417294339317307841204705\) with real radius below
\(7.4\times10^{-30}\), strictly positive. Equation (22), **not** an
interval containing zero, proves the exact collision.

The complete-mode constants (20) are separately checked. They are not
inserted as fictitious theta tails for the control. No runtime advantage,
theta nonvanishing region or adaptive stopping boundary is measured.

## 8. Disposition and the next research gate

Stop the **reflection-only odd-adjoint improvement** in the norm of
Section 4: its complete directional comparison is equality. Retain (5)–(7)
as a reusable safeguard when comparing finite theta sums with complete
shifted approximants. Retain the complex-time extension (19) where that
domain is needed. Neither result supplies a new sign for the retained
theta core or advances HMC-05; HMC-06 remains gated.

The next bounded action is to specify a residual that uses the canonical
lattice relation **in the retained signed arithmetic sum**, rather than
only its even reflection. Its acceptance contract must name the residual,
the receiving jet/charge/period, and the changed coupled information. The
first comparison must include S01's already paired endpoint bound and
the unchanged direct retained evaluator. The [covariant-jet program][s05]
already supplies a normalized infinite ladder and warns against separate
divergent zero-mode transforms or an assumed finite closure; repeating
those identities is not a new candidate.

No such improved retained-core inequality is asserted here. If the next
derivation again gives only source rigidity, parity projection or an
identity for the existing evaluator, record that outcome before starting
a numerical theta pilot. Other analytic norms and genuinely coupled
arithmetic estimates remain open.

[n01]: 01_TWO_ENDPOINT_TAIL_CONSTRAINT_20261021.md
[checker]: ../numerics/check_reflection_adjoint.py
[receipt]: ../numerics/REFLECTION_ADJOINT_CHECK_192_20261021.json
[results]: ../../../../../../../result-summaries/README.md
[arithmetic]: ../../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../../avoid/README.md
[a01]: ../../../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a03]: ../../../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md
[a07]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[shifted]: ../../../../../11_arithmetic_collision_rigidity/manuscript/positive_arithmetic_packets/sections/07_shifted_approximation.tex
[modular]: ../../../../../11_arithmetic_collision_rigidity/manuscript/positive_arithmetic_packets/sections/04_modular_collisions.tex
[nonstationary]: ../../../../../11_arithmetic_collision_rigidity/manuscript/positive_arithmetic_packets/sections/08_effective_tails.tex
[s01]: ../../../../../11_arithmetic_collision_rigidity/symmetries/01_modular_self_duality/README.md
[s01-note]: ../../../../../11_arithmetic_collision_rigidity/symmetries/01_modular_self_duality/notes/01_PAIRED_ENDPOINT_REMAINDER_AND_BOUNDED_COMPARISON_20261018.md
[s05]: ../../../../../11_arithmetic_collision_rigidity/symmetries/05_covariant_theta_jets/README.md
[finite-prime]: ../../../../../11_arithmetic_collision_rigidity/notes/03_FINITE_PRIME_COMPATIBLE_COLLISION_CONTROLS_CODEX_20261018.md
[reflected]: ../../../../../../investigations-2/active/22_theta_manifold_geometry/notes/05_control_families/04_REFLECTION_POSITIVE_SOURCE_COLLISION_AND_MIXED_SECTORS_20261015.md
[dlmf]: https://dlmf.nist.gov/20.7.E32
[flint]: https://python-flint.readthedocs.io/en/latest/acb.html#flint.acb.integral
