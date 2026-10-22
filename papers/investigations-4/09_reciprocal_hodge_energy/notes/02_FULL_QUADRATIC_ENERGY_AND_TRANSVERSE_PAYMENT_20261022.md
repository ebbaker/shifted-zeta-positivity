# Full quadratic energy and the transverse period

22 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual recorded model **gpt-6.1-sol (Codex)**,
reasoning effort **ultra**, verified from the active root turn metadata.

**Status: exact calibration proved in-note; scoped boundary compression
fails.** The inherited logarithmic degeneration is not a new simplicity
criterion or nodal-coefficient result. The additional calculation keeps
the two physical boundaries, the cut pair and coherent primitive constants
in one explicit full-energy evaluation. See the [finite contract][contract],
[program][program], [result index][results], [avoid index][avoid],
[controls][controls] and [internal review][review].

## 1. Exact cover and complete energy interval

Let \(H_a(z)=z^2-a^2\), \(0<a<R\), on \(|z|<R\). Set
\[
 z=a\cosh u,\quad w=a\sinh u,\quad u=s+i\theta\pmod{2\pi i}.
\]
This parametrizes the cover itself, with \(\omega=dz/w=du\), including
the regular branch points \(u=0,i\pi\). Since
\(|\cosh(s+i\theta)|^2=\sinh^2s+\cos^2\theta\), its domain is
\[
 -U(\theta)<s<U(\theta),\quad
 U(\theta)=\operatorname{arsinh}\sqrt{(R/a)^2-\cos^2\theta}.
                                                               \tag{1}
\]
The full two-sheet energy is therefore
\[
 \mathcal E_a=2\int_0^{2\pi}U(\theta)d\theta,\qquad
 4\pi\operatorname{arcosh}(R/a)\le\mathcal E_a
                  \le4\pi\operatorname{arsinh}(R/a).             \tag{2}
\]
Indeed \((i/2)du\wedge d\bar u=ds\,d\theta\).
Both bounding endpoints are \(4\pi\log(2R/a)+O(a^2/R^2)\).
For the heat control \(a^2=2\tau\), the energy diverges as
\(2\pi\log(1/\tau)+O(1)\) for fixed \(R\).

## 2. Every cut and physical boundary contribution

Cut at \(\theta=0\), use \(0\le\theta\le2\pi\), and set \(F=u\).
The global shift \(F=u+U_0\) normalizes the bottom left corner to zero
as in the finite contract; it leaves both the total and the grouped cut
and physical-boundary integrals unchanged.
Let \(U_0=U(0)=\operatorname{arcosh}(R/a)\).
The positive boundary orientation runs along the bottom from
\(-U_0\) to \(U_0\), up the right side, along the top in reverse,
and down the left side. The core period is \(q=2\pi i\), while the
bottom transverse integral is \(p=2U_0\).
Across the identified cut, \(J=F_{\rm bottom}-F_{\rm top}=-2\pi i\).
Consequently
\[
 \int_{\rm bottom+top}F\bar\omega=-4\pi iU_0,
 \qquad E_{\rm cuts}=2\pi U_0.                               \tag{3}
\]
The physical right side is \(u=U(\theta)+i\theta\), traversed upward;
the left side is \(u=-U(\theta)+i\theta\), traversed downward. Thus
\[
 \int_{\partial X}F\bar\omega
  =2i\int_0^{2\pi}(\theta U'-U)d\theta
  =4\pi iU_0-4i\int_0^{2\pi}U d\theta,
\]
\[
 E_{\rm physical}=\mathcal E_a-2\pi U_0,
 \qquad E_{\rm cuts}+E_{\rm physical}=\mathcal E_a.            \tag{4}
\]
Both terms in this coherent normalization grow logarithmically. Keeping
only the cut term would miss half the leading energy. Resetting the
primitive separately on the two physical components loses their relative
constant \(2U_0\); that lost connector is unbounded.

## 3. The comparison that fails

Fix \(R\), let \(0<a\le R/2\), and take \(a\downarrow0\).
On \(|z|=R\), \(|H_a|\ge3R^2/4\), and every prescribed finite
collection of spatial derivatives of the labeled boundary form is bounded
uniformly. The source polynomial, its derivative bounds and its outer jet
are regular. The core period \(q=2\pi i\) is exactly constant.
Even the separately rebased boundary primitives
\[
 F_\pm(\theta)-F_\pm(0)=\pm(U(\theta)-U_0)+i\theta
\]
stay bounded, because
\(0\le U-U_0\le\operatorname{arsinh}(R/a)-\operatorname{arcosh}(R/a)\).
Nevertheless (2) diverges. There is no finite upper energy bound depending
only on these fixed common upper-budget inequalities and the fixed core
period. These are not observations of exact attained norm values, which
could themselves encode the shrinking parameter.
The relative period \(p=2U_0\) is not bounded by them.

This is a failure of that **compressed information class**. Exact boundary
values determine the polynomial and permit recovery of \(a\); arbitrary
methods using all boundary information are outside this negative result.
Absolute field errors that admit arbitrarily small positive \(a\) likewise
admit arbitrarily large finite energy, even though each admitted fiber
has simple branch points. An error ball admitting a double has no finite
uniform upper reciprocal-energy bound.

For this explicit control, direct reciprocal integration under the same
paid map \(z=a\cosh u\) gives exactly (1)–(2), and the complete boundary
calculation (3)–(4) gives that same integral. It supplies no stricter
analytic interval than the equally informed direct method. No computation
or cost measurement for theta, and no universal cost comparison, follows.
The small [floating diagnostic][diag] checks signs and the two boundary
payments; the mathematical evidence is the calculation above.

## 4. Matched controls and the remaining source gate

| Control | Premise it fails and what the energy identity still does |
| --- | --- |
| Quadratic and neighboring-root quartic | They lack unchanged theta arithmetic. The quadratic already satisfies every premise of the compressed local boundary proposal and disproves its uniform upper bound; a small chart of the quartic has the same ordinary-double divergence. |
| Euler-factor source | It changes canonical arithmetic. Generic source positivity, regular covers and the complete Stokes identity still hold on its regular finite charts. |
| Weighted-square and finite-prime controls | They lack the complete normalized reflection conjunction and unchanged full coefficient sequence. Finite square support or a finite prime list cannot substitute for those conjunctions. |
| Reflected and positive-primitive controls | They lack unchanged canonical square coefficients; their strong reflection/primitive properties are distinct preservation lists. The energy identity does not reject their collisions. |
| Finite Jensen approximants with a limiting double | Strict finite hyperbolicity lacks the required uniform limiting nondegeneration. This is a separate compact-model gate, not a physical theta estimate. |

The proofs (1)–(4) do not invoke any arithmetic premise that excludes these
controls. Therefore failure of literal theta identities by a control does
not make these generic energy formulas a discriminator.

The declared first comparison is closed for bounded core-period/exterior-norm
compression. A new theta candidate must pay a joint relative-period and
physical-boundary estimate, or establish a complete acquisition benefit.
RHE-02 remains open for that input. Uniform endpoint bounds, all heights,
higher multiplicities and any RH coverage bridge remain unproved.

[contract]: 01_FINITE_COVER_CONTRACT_AND_ENERGY_ENCLOSURE_20261022.md
[program]: ../research-overview/01_RECIPROCAL_HODGE_ENERGY_PROGRAM_20261022.md
[results]: ../../../../result-summaries/README.md
[avoid]: ../../../../avoid/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[review]: ../reviews/01_CONTRACT_AND_QUADRATIC_PILOT_REVIEW_20261022.md
[diag]: ../numerics/01_quadratic_cut_diagnostic_20261022.py
