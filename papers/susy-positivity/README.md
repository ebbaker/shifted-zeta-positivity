# SUSY positivity research program

This program seeks an independently defined positive structure whose pairing
is the full central Weil quadratic form on every smooth compactly supported
input, at arbitrary support length. The shifted transfer family supplies a
related contraction route. **The all-length sign problem remains open; no RH
proof is claimed.**

## Start here

- [Critical path](investigations/critical-path/README.md): reviewed adaptive-EMA work and an all-input original-transfer anchor at L=1/2, omega=0.001. A finite arithmetic relaxation tower with exact endpoint response closes the pilot’s omitted-input gap; cumulative depth coupling is next.
- [Wilson–Loewner](investigations/wilson-loewner/README.md): working manuscript pair 0.4: an 18-page [program exposition](investigations/wilson-loewner/manuscript.pdf), 33-page [supplementary information](investigations/wilson-loewner/supplementary-information.pdf), preserved drafts, and the [shift-flow, cumulative-storage and critical-path note](investigations/wilson-loewner/notes/SHIFT_FLOW_CUMULATIVE_STORAGE_AND_CRITICAL_PATH_20260919.md).
- [Wilson lines](investigations/wilson-lines/README.md), [Loewner](investigations/loewner/README.md), and [fractional dimension](investigations/fractional-dimension/README.md): the other retained investigations, with their existing conclusions and qualifications.
- [Previous investigations](investigations/previous/README.md): five complete packages outside the current research focus. This grouping does not mean disproved, completed, or scientifically obsolete.
- [Mathematical background](background.pdf) and [program overview](PROGRAM_OVERVIEW.md): shared normalization, domains, goals, and the original research framework.
- [Boundary corrections and finite responses](manuscripts/finite-response-weil-positivity/README.md): a separate technical note. Submission remains deferred pending further work, human mathematical review, and novelty reassessment.

## Folder map

```text
susy-positivity/
  README.md
  PROGRAM_OVERVIEW.md
  background.tex                 # standalone wrapper and bibliography
  background_section.tex         # authoritative substantive background
  background.pdf                 # compiled reading copy
  brainstorm/                    # proposals, surveys, continuation context
    ASSESSMENT.md                # latest research-direction assessment
    candidate-bulk-theories/
    continuation-notes/
    theory-landscape-20260913/
  investigations/                # current research focus
    critical-path/               # adaptive smoothing and cumulative continuation
    wilson-loewner/
    wilson-lines/
    loewner/
    fractional-dimension/
    previous/                    # grouping by focus, not scientific status
      arithmetic-ground-state-geometry/
      inverse-bulk-realization/
      positive-factorizations/
      source-selection-rules/
      topological-susy-bulk/
  manuscripts/                   # separate manuscripts drawn from the research
    finite-response-weil-positivity/
  archive/                       # historical reorganization record and path guide
  validation/                    # structure checker and historical relocation checks
```

The [brainstorm index](brainstorm/README.md) explains the dated proposals and
later reassessment. The [manuscript index](manuscripts/README.md) distinguishes
standalone notes from manuscripts retained within investigations.

## Investigation scope and status

The [Wilson-Loewner opening note](investigations/wilson-loewner/notes/OPENING_NOTE_20260919.md)
records a 19 September qualification to the earlier Loewner closure: the
tested bare-map and radial-kernel identifications do not exclude a
field-dependent Wilson observable on a Loewner-generated contour. The
dated parent conclusions below retain their historical context.

| Investigation | Scope and status |
|---|---|
| [Critical path](investigations/critical-path/README.md) | Reviewed EMA audit plus an all-input original-transfer certificate: Q(0,1/2) >= I/40 and D(0.001,1/2) >= 0.000049998 I. A finite prescribed EMA tower, exact endpoint response, and rational interval bounds cover the entire input complement; 40/60-digit certificates and a separate causal-response check pass. This closes the pilot’s designated gap, not a new depth horizon. Normalized cumulative depth coupling and all-depth continuation remain open; historical controls and v0.4 manuscripts are preserved. |
| [Wilson-Loewner](investigations/wilson-loewner/README.md) · [exposition](investigations/wilson-loewner/manuscript.pdf) · [supplement](investigations/wilson-loewner/supplementary-information.pdf) · [drafts](investigations/wilson-loewner/drafts/README.md) · [notes](investigations/wilson-loewner/notes/README.md) | Working manuscript pair 0.4: an 18-page exposition and 33-page technical companion. Main Section 5 and SI S10–S11 add the full fixed-window response comparison, scoped regularity and compactness obstructions, and the auxiliary localization product. The earlier variation, endpoint, reflection and continuation tools remain available. The physical realization, positive norm identity and all-depth bounds remain open. Versions 0.1–0.3 are preserved; 299 finite diagnostics and both-document build records accompany the pair. No independent review. |
| [Wilson lines](investigations/wilson-lines/README.md) · [PDF](investigations/wilson-lines/manuscript.pdf) · [drafts](investigations/wilson-lines/drafts/README.md) | Working manuscript 0.8 (47 pages), *Deformation flows for the shifted Weil family: the transfer as an all-pass filter*. Opened 17 September 2026 from a proposal that the shifted family is the deformation flow of a Wilson line. The transfer symbol is unimodular on the critical line, exactly and unconditionally, so the transfer is an all-pass filter; its phase derivative is the archimedean symbol, which explains the density identity; its phase jumps are resonances at the zeros, so the Weil form is a total resonant response; under RH it is inner and the contraction defect is the flux through the leading endpoint; and a filter that changes only phase is abelian, so the non-Abelian Stokes mechanism has nothing to act on along the shift. The contraction region is then settled: it is monotone in the length with supremum one or infinity, so contraction at every length is equivalent to the absence of zeros at distance more than the shift --- a graded criterion, with no critical path and only a disproof reading. What remains is the endpoint direction, where the algebra is triangular and flat. The form's exact symmetry group turns out to be the residual conformal group of a ray with one end pinned, so conformal symmetry is aligned with the target rather than in tension with it. No source is constructed and no positivity is proved. |
| [Loewner](investigations/loewner/README.md) · [manuscript](investigations/loewner/manuscript.pdf) · [notes](investigations/loewner/notes/README.md) | Working manuscript 0.3 (33 pages). Opened 17 September 2026 from the Wilson-lines investigation and worked on through 18 September, around a factorization of the shifted transfer: $K_\omega=B_b\widehat K_\omega$ with $B_b=\frac{p-b}{p+b}$ one first-order all-pass section at the pole of $\zeta$ ($b=\frac12+\omega$) and $\widehat K_\omega$ completely monotone, so the transfer kernel is an explicit positive measure --- a Beta-distributed archimedean delay (squared-Bessel additivity in dimensions $\frac12\mp\omega$) convolved with a multiplicative comb $\widetilde c_n=n^{\omega-\frac12}\prod_{p\mid n}(1-p^{-2\omega})$ at the integer ratios, with one further exponential smoothing --- minus twice its exponential moving average. The compressed transfer is thereby assembled exactly from elementary functions and the integers $n<e^L$. The comb is a Hecke/Bost--Connes semigroup structure and not a Loewner one; the correction is forced by the functional equation; at $\omega=\frac12$ the positive part is the Eisenstein scattering matrix of the modular surface. Written in each atom's own coordinate the kernel is $\tau^{\omega-1}$ times a function holomorphic on $\lvert \tau\rvert<\pi$, so the spike belongs in a Gauss--Jacobi quadrature weight and the whole assembly runs in double precision; it is validated at $L=\log3,\log5,\log7$ --- a strict contraction at each, whose defect reproduces the Weil-form margin in the same basis to $0.5\%$, $1.2\%$ and $1.8\%$ at $\omega=0.01$ over margins from $6\times10^{-8}$ to $2\times10^{-22}$, with the deviation linear in $\omega$ and identified as the Galerkin truncation term --- against a phase-matched lattice surrogate that misses by factors $1.07$, $2.19$, $0.76$ at the same three horizons. Also: the second-order defect $2\omega Q-\omega^2(2Q^2+[Q,A])$; a zero-free closed form for the first-order tail; an exact $\Gamma$-ratio Laplace transform for one atom; and the cumulative Cayley coordinate $P=\frac2\omega\mathrm{Re}(I-V)(I+V)^{-1}$, in which contraction is positivity and which is *even* in $\omega$ because $K_{-\omega}=1/K_\omega$. And the archimedean factor turns out to be, exactly, the horocycle integral $\int_{\mathbb R^{2\omega}}\lvert t+i\rvert^{-(p+b)}dt$ in dimension $2\omega$, whose delay is the log-modulus along the horocycle and whose kernel prefactor is the area of $S^{2\omega-1}$: **the shift is half a dimension**, and $2\omega$ is an integer at exactly one point of the family, $\omega=\frac12$, where the horocycle is the cusp of the modular surface and contraction is unconditional. That quantization is why no radial Loewner chain produces the archimedean Beta law --- three independent proofs --- and with the comb and the correction already excluded, the Loewner proposal that opened the investigation closes. Manuscript *The Markov part of the shifted Weil transfer*, working draft 0.3 (33 pages), with a pedagogical introduction, and two registered check programmes of 53 and 43 cases replayed with it. **Closed 18 September**: the proposal it was opened to test is answered in the negative on all three factors. Its durable output is the decomposition with its dictionary and the registered assembly of $V_{\omega,L}$, which computes the norm, the defect and the Cayley coordinate at any horizon from elementary functions and the integers below $e^L$; work continuing this program should use that instrument rather than rebuild it. The forward direction continues in [fractional dimension](investigations/fractional-dimension/README.md). No source is constructed and no positivity is proved. |
| [Fractional dimension](investigations/fractional-dimension/README.md) · [opening note](investigations/fractional-dimension/notes/OPENING_NOTE_20260918.md) · [notes](investigations/fractional-dimension/notes/README.md) · [past the wall](investigations/fractional-dimension/notes/PAST_THE_WALL_20260918.md) · [the trade is not it](investigations/fractional-dimension/notes/THE_TRADE_IS_NOT_IT_20260918.md) · [manuscript](investigations/fractional-dimension/manuscript.pdf) | Opened 18 September 2026 from the Loewner investigation, around one question: the shifted transfer's Markov part is $\Lambda(2s-d)/\Lambda(2s)$ with $d=2\omega$ and $2s=p+b$, and **every one of its factors is $d$-dimensional as a formula** --- the archimedean part is the Riesz integral $\int_{\mathbb R^{d}}\lvert t+i\rvert^{-(p+b)}dt$, the comb's weights are the Jordan totient $J_d(n)/n^{(d+1)/2}$, which at integer $d$ counts the primitive vectors in $(\mathbb Z/n\mathbb Z)^d$, and the Blaschke factor sits at the pole $2s=d+1$ of the volume term. At $d=1$ this is the Eisenstein scattering matrix of the modular surface, and $d=1$ is the only integer the family's range $(0,1]$ contains. Is $d$ a dimension, or a parameter? If a dimension, the family is a deformation of the modular surface in the dimension of its cusp; if only a parameter, the right output is a clean statement of which property fails to continue. The dictionary is now closed on a single object. The dimension is $2\omega$ and not $\omega$: $\tau=\log\lvert t+i\rvert$ is a *Busemann* function on the horocycle rather than a distance, and $\tau\sim r^2/2$ is a square, so the two local exponents $r^{2\omega-1}$ and $\tau^{\omega-1}$ are the same measure and the normalized limits differ by exactly $2^{1-\omega}$; in the true half-distance the measure is the radial measure of complex hyperbolic space of complex dimension $\omega$, real dimension $2\omega$ (Jacobi parameters $(\omega-1,0)$, $\rho=\omega>0$, the only reading accounting for every factor of the kernel), and the comb, having no radial coordinate at all, fixes $d=2\omega$ independently. And the Blaschke factor is a volume term: $\operatorname{Res}_{p=b}\widetilde K_\omega=\lvert S^{d}\rvert/2\zeta(d+1)$, the sphere of $\mathbb R^{d+1}$ times the primitive density in $\mathbb Z^{d+1}$ --- the volume term of a **lattice of rank $d+1$** whose cusp integrates over a $d$-dimensional horocycle, giving $6/\pi=2/\mathrm{vol}$ at $d=1$. So all three entries name one object, and the question sharpens: a dimension can be continued, but a **rank is a cardinality**. That question is now answered, and the answer is a lattice at every integer and no point set in between. For a covolume-one $L\subset\mathbb R^{m}$ the primitive Epstein zeta $E^{*}_L(s)=\sum_{v\ \mathrm{prim}}\lvert v\rvert^{-2s}$ satisfies $\xi(2s)E^{*}_L(s)=\xi(m-2s)E^{*}_{L^{*}}(m/2-s)$, so its reflection ratio is independent of the lattice and is an invariant of the **rank alone** --- and under the dictionary that ratio is exactly the Markov part, so for **every** integer $d\ge1$, not just $d=1$, the transfer is the scattering matrix of the space of unimodular lattices of rank $d+1$, with $p\mapsto-p$ the Epstein functional equation $s\mapsto m/2-s$ (which is why it is all-pass on $\Re p=0$). The family's cap $\omega\le\frac12$ is then a rank cap: a second pole of the numerator sits at $p=\omega-\frac12$, inside the closed left half-plane iff $m\le2$, and in the lattice variable it is $\zeta$'s own pole --- so the family occupies the **first gap** $m\in(1,2]$ of the rank sequence, with the modular surface at its right endpoint. Inside the gap the lattice does not exist: the point count's unique interpolation is the $q$-coefficients of $\theta^{m}$, polynomial in $m$, and $r_{d+1}(3)=\frac43(d^{3}-d)$ is strictly negative for **every** $d\in(0,1)$, vanishing only at the endpoints, so $\theta(it)^{d+1}$ is not completely monotone anywhere strictly inside. What continues is the whole of the cusp data --- $J_d>0$, $1/\zeta(d+1)\in(0,1)$, the horocycle integral, the unimodularity --- and what fails is the interior: at fractional $d$ there is a **scattering matrix without a space**. Crossing the wall then settles what the range is worth. The decomposition survives it: $R_\omega=B_b\cdot\frac{p+a}{p-a}$ at every $\omega$, and $\frac{p+a}{p-a}=B_c$ with $c=\omega-\frac12$ is a genuine Blaschke factor exactly when $\omega\ge\frac12$, so $R_\omega=B_bB_c$ is **inner** past the wall and a ratio $B_b/B_a$ with a right-half-plane pole inside the range; and $\widehat K_\omega$ stays completely monotone at every $\omega>0$, by two groupings of the Gamma factors that are exchanged at $\omega=\frac12$ --- past it, $\widehat K^\Gamma_\omega=\pi^\omega\frac{\Gamma(z+c)}{\Gamma(z+\omega)}\frac{\Gamma(z+1)}{\Gamma(z+c+1)}$ with $z=\frac{p+a}2$, two Gamma ratios of parameter gap $\frac12$ and $c$. The two cancelled poles have different origins, $p=b$ the comb's and $p=c$ the **archimedean** factor's, so past the wall the correction removes one pole from each half; and the inherited assembly needed no second factor at all, only a removable $0/0$ at $\omega=1$. **But past the wall the criterion is empty:** for every $\omega\ge\frac12$ no zero has $\lvert\Re\rho-\frac12\rvert>\omega$, so by the parent's dichotomy every $V_{\omega,L}$ is a contraction *unconditionally* --- on the Euler product alone for $\omega>\frac12$, with the classical zero-free region needed only at the boundary point $\omega=\frac12$. The criterion has arithmetic content on exactly $\omega\in(0,\frac12)$, where it is the zero-free strip of half-width $\omega$ --- which is $d\in(0,1)$, which is the same open gap on which $r_{d+1}(3)<0$: **the criterion has content precisely where the lattice does not exist**. And the endpoints read the other way round from how they were first described: the Euler product is the criterion's *value* at rank two, and RH is its *derivative* at rank one, where $E^{*}_{\mathbb Z}\equiv2$, $\widetilde K_0=1$, $V_0=I$ and the first-order law gives the localized Weil form. Finally, the two positivity statements turn out not to be one statement. The point count fails on $(2,3)$ as well as on $(1,2)$ while the criterion has content only on $(1,2)$, and at $m=3$ the point count is completely monotone and the rational factor is not --- so no equivalence can hold, and the coincidence of intervals is the first gap and nothing more, forced by both of the criterion's endpoints sitting at the two smallest ranks. The point count's failure is **Lagrange's four-square theorem seen through a binomial series**: on the gap $(k,k+1)$, $\operatorname{sign}\binom mj=(-1)^{\max(0,j-k-1)}$, so $r_m(n)>0$ for free when $n\le k+1$ and the first forced negative coefficient sits at the least integer needing $k+2$ **positive** squares --- $2$, $3$, $7$, and none at all once $k\ge3$, since $s(n)\le4$ always. The transfer, by contrast, has exactly one positivity threshold in $m$ and it is at $m=2$; its only other feature at an integer, the archimedean exponent vanishing at $m=3$, is a regularity threshold and points the wrong way. **What explains the split is where the rank sits:** in the transfer it is an *exponent* --- $(2\sinh\tau)^{\omega-1}$, $(1-e^{-t})^{\beta-\alpha-1}$, $p^{-d}$ --- where positivity is a local inequality at one $\tau$ or one prime that continuation cannot break; in the point count it is a *binomial index*, where it can. So the transfer's positivity was never inherited from a lattice and the lattice's failure leaves no trace in it. **The investigation's question is answered: $d$ is a parameter.** Manuscript *A scattering matrix without a space*, working draft 0.1 (21 pages), the consolidated report of the investigation, with six registered check programmes of 1522 cases replayed with it; $\zeta$ is evaluated at real arguments only, and not at all in the last one. |

### Previous investigations

These packages are outside the current research focus. The grouping makes no
claim about completion, disproof, or obsolescence.

| Investigation | Scope and status |
|---|---|
| [Inverse bulk realization](investigations/previous/inverse-bulk-realization/README.md) · [PDF](investigations/previous/inverse-bulk-realization/manuscript.pdf) · [drafts](investigations/previous/inverse-bulk-realization/drafts/README.md) | Working manuscript 0.6 (42 pages): self-contained Weil normalization, sphere-sector pairings, a dressed Schur realization of the positive prime reference at one fixed quantization parameter, and magnetic-domain and mixed-return restrictions. Earlier gamma, gauge and rational-feedback tests are retained. The joint contact/pole match and all-support realization remain open. |
| [Source selection rules](investigations/previous/source-selection-rules/README.md) · [PDF](investigations/previous/source-selection-rules/manuscript.pdf) · [drafts](investigations/previous/source-selection-rules/drafts/README.md) | Working manuscript 0.1, *A jump-process presentation of the localized Weil form*. A spin-off from inverse bulk realization that asks what the localized Weil form is rather than building a source: the archimedean symbol identified with the smooth zero density, the target presented as a single Lévy jump form whose atoms are the primes, the Perron--Frobenius structure and the rank-two pole term that breaks it, a necessary condition with a disproof test that found no violation, and nine selection rules. No source is constructed and no positivity is proved. |
| [Positive factorizations](investigations/previous/positive-factorizations/README.md) · [PDF](investigations/previous/positive-factorizations/manuscript.pdf) · [status](investigations/previous/positive-factorizations/STATUS.md) | Manuscript v0.2: short-window factors, gamma kinetic tower, restricted odd-sector factors, scoped obstructions, and a certified first-prime stabilization example. Separate round-4 reports extend the odd factor across shifts and isolate the remaining even scalar. A complete even factor, joint prime construction, and arbitrary-length mechanism remain open. |
| [Topological SUSY bulk](investigations/previous/topological-susy-bulk/README.md) · [PDF](investigations/previous/topological-susy-bulk/manuscript.pdf) · [status](investigations/previous/topological-susy-bulk/STATUS.md) | Manuscript through 12 September: positive relative gamma complex, arithmetic loop responses, and correction obstructions. Separate 13 September notes construct a physical Fock realization and superspace boundary action and study finite-block restrictions. The full arithmetic norm remains open. |
| [Arithmetic ground-state geometry](investigations/previous/arithmetic-ground-state-geometry/README.md) · [PDF](investigations/previous/arithmetic-ground-state-geometry/manuscript.pdf) · [status](investigations/previous/arithmetic-ground-state-geometry/STATUS.md) | Integrated manuscript through note 20: interacting local factors, physical caps, closed gamma source, pole gluing, prime returns, and a positive source equal to the full Weil form plus an explicit finite-rank positive error. The remaining finite response matrix is not proved positive. Includes the noncompact gamma boundary correction and residual estimates; an all-support physical source law remains open. |

The positive gamma kinetic construction is established within its stated
scope. Later constructions retain the normalization, poles, and primes in an
explicit signed remainder or finite-rank error; positivity of the auxiliary
source does not remove that error. Local results retain their support, shift,
and input restrictions. Internal checks do not replace specialist proof review.

## Standalone manuscript

[Boundary corrections and finite responses for the localized Weil form](manuscripts/finite-response-weil-positivity/README.md)
contains a [condensed note](manuscripts/finite-response-weil-positivity/manuscript.pdf),
[detailed derivations](manuscripts/finite-response-weil-positivity/derivations.pdf),
and its own review, build, provenance, and dated draft records. It develops
boundary corrections, truncation bounds, and finite-response enclosures from
the ground-state investigation. Its matrix conjecture remains unproved; the
numerical example is not a positivity certificate or demonstrated computational
advantage. See the [current evaluation](manuscripts/finite-response-weil-positivity/EVALUATION.md)
for the deferred publication status.

This folder moved from `papers/finite-response-weil-positivity/` to
`papers/susy-positivity/manuscripts/finite-response-weil-positivity/`.
The [review navigation guide](manuscripts/finite-response-weil-positivity/reviews/README.md)
maps preserved reviews to the drafts they assessed. Their old paths and line
numbers are historical references, not links to the current revision.

## Working conventions

Keep shared background at the program root. New approaches belong in
`investigations/<descriptive-name>/`, with a README stating their mechanism,
scope, status, and relation to the shared framework. Keep their working
manuscripts, notes, checks, and histories together. A separate manuscript
belongs in `manuscripts/<descriptive-name>/`, with an explicit source record,
review status, build instructions, and dated drafts. Exploratory proposals
and comparative assessments belong in `brainstorm/`.

Keep earlier complete packages under `investigations/previous/` when they leave
the current focus; retain their scientific status and scope. The original
Loewner proposal retains its qualified closure despite remaining at the top level.
Update this index when adding an investigation or manuscript. Distinguish
proved results, diagnostics, and proposals. Link to the shared background;
retain historical validation and snapshots under their original dates, and
refresh current file inventories explicitly after edits. The
[archive guide](archive/README.md) maps earlier layouts without rewriting
historical evidence. Follow the repository [large-file policy](../../LARGE_FILES.md).

## Build and verification

Run the structure check from this directory:

```sh
python3 validation/check_structure.py
python3 investigations/previous/arithmetic-ground-state-geometry/validation/check_package.py --replay
python3 investigations/previous/topological-susy-bulk/validation/check_package.py
```

The first checks current navigation, TeX dependencies, and selected current
file records while distinguishing historical links. The investigation checks
verify their complete package manifests; the ground-state replay also
reproduces 59 labelled exact-algebra checks. None is an analytical proof checker.

Build the shared background with a standard TeX distribution:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error background.tex
```

Use each package's build or replay guide for its outputs:

- [Positive factorizations](investigations/previous/positive-factorizations/README.md): manuscript build and replay that preserves historical diagnostics.
- [Topological SUSY bulk](investigations/previous/topological-susy-bulk/README.md): isolated build and numerical replay.
- [Arithmetic ground-state geometry](investigations/previous/arithmetic-ground-state-geometry/BUILD.md): integrated manuscript build and package refresh procedure.
- [Finite-response note](manuscripts/finite-response-weil-positivity/BUILD.md): both document builds and review checks.
- [Candidate bulk theories](brainstorm/candidate-bulk-theories/REPRODUCE.md): model diagnostics and earlier certificate replay.

The [12 September verification record](validation/reorganization-20260912/VERIFICATION.json)
describes that reorganization, not a fresh build of later revisions.

The [20 September relocation record](archive/REORGANIZATION_20260920.md)
provides the five-folder map, preservation fingerprints, and validation results.
