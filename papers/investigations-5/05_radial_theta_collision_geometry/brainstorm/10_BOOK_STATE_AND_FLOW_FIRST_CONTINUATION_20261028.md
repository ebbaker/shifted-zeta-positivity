# Continuation: current book and flow-led choices

28 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), recorded effort xhigh**.
Chat0015, *Draft book rewrite change note*.

**Status: continuation and decision record, not a new flow result.**
Edward Baker's latest instruction is to **keep the book as it is for now,
continue the investigation, and let the flow equations dictate the
choices**. Do not resume changing the principal notation or geometry just
to shorten the initial integral. Develop materially different alternatives
in separate numbered notes, preserving the earlier versions.

This is the current handoff after
[Brainstorm09](09_GENERATING_THETA_AND_FLOW_CONTINUATION_20261028.md).
Its earlier instruction to hold all manuscript work is historical: the
book rewrite has now been requested and completed as a first draft.
The current instruction is to retain that draft while investigating flows.

## 1. Current artifacts and what has been settled

The [book source](../book/main.tex) is an 11-page initial draft. Its current
version is in commit `d1b2eff925103dc57595a71b9ae6676bd8f52ea0`
(*Book draft rewrite with new results*). The saved source still matches
[build record20](../numerics/20_BOOK_REWRITE_BUILD_RECORD_20261028.json):
SHA-256 `e577828b2015ec859cc46a96054d4c4cf4191ffc612ad96d423b7941dacd1a86`.
The build record and [assessment21](../reviews/21_BOOK_REWRITE_ASSESSMENT_20261028.md)
record successful local and desktop compilation, resolved references,
and inspection of all pages. These are same-assistant checks.

- **Main presentation:** the original \(H,V,G\) notation. Section 1
  starts with xi and a brief de Bruijn-Newman discussion, then derives
  the theta potential and the generator equations.
- **Companion representations:** Section 2 treats Mellin symmetry and
  entire continuation; Section 3 treats spherical means, inversion,
  preservation, and multiple-zero cancellation.
- **Additional presentation:** Section 4 retains the normalized
  three-dimensional notation \(F=16H(0,\cdot)\), with \(G_\Theta\)
  on the cylinder and \(\rho_\Theta\) in Euclidean volume. It is a
  separate presentation, not the replacement notation for the book.
- **Flow comparisons:** Section 5 contains cylinder heat, transported
  Newman flow, and the exact constant linear-combination benchmark.
  Section 6 states their control scope and remaining limitations.

The [original rewrite plan](../book/changes/02_REWRITE_20261028.md) was
restored. The later
[three-dimensional notation alternative](../book/changes/03_THREE_DIMENSIONAL_NOTATION_ALTERNATIVE_20261028.md)
was preserved byte-for-byte as a separate note, as requested, and also
included as the additional book section. Both remain available. The
alternative's earlier statements about pending implementation describe
the state when it was preserved; this continuation records the current state.

The [reading PDF](../../../../output/pdf/radial-theta-collision-geometry-book/theta-transform.pdf)
is generated and ignored by Git. No new manuscript snapshot is needed.
The separate conservative-flow manuscript in the investigation root has
not been replaced by this book.

## 2. The starting equations to carry forward

Retain the original normalization:
\[
\begin{gathered}
A(r)=\sum_{n\ge1}e^{-\pi n^2r^2},\qquad
\Theta(r)=1+2A(r)=r^{-1}\Theta(1/r),\\
r=e^{2u},\qquad
\Phi(u)=\frac14r^{5/2}\Delta_3\Theta(r),\qquad
\Delta_3=\partial_r^2+\frac2r\partial_r,\\
H(t,z)=\frac12\int_{\mathbb R}e^{tu^2}\Phi(u)e^{izu}\,du,
\qquad H_t=-H_{zz},\qquad
8H(0,z)=\xi\!\left(\frac{1+iz}{2}\right).
\end{gathered}
\tag{C1}
\]
The canonical source integral is entire in \(z\) for every real \(t\).
The basic Euclidean potential and observation are
\[
\boxed{
\begin{gathered}
V(r)=1+r^{-1}-\Theta(r)>0,\qquad
-\Delta_XV(|X|)=(\Delta_3\Theta)(|X|),\\
H(0,z)=\frac{1+z^2}{256\pi}\int_{\mathbb R^3}
V(|X|)|X|^{-5/2+iz/2}\,dX,
\qquad |\operatorname{Im}z|<1.
\end{gathered}
}
\tag{C2}
\]
Here \(V\) is smooth at the origin, \(V(0)=1\), and \(V(r)\sim1/r\)
at infinity. The central point sources have cancelled.

The generator and its cylinder form are
\[
\begin{gathered}
G(u)=\tfrac12e^uV(e^{2u})
=\cosh u-\tfrac12e^u\Theta(e^{2u}),\\
\mathcal C=\mathbb R\times\mathbb S^2,\qquad
d\mu=du\,\frac{d\omega}{4\pi},\qquad
\mathcal L=1-\partial_u^2-4\Delta_{\mathbb S^2},\\
\boxed{\mathcal LG=8\Phi,\qquad
16H(0,z)=(1+z^2)\int_{\mathcal C}G(u)e^{izu}\,d\mu.}
\end{gathered}
\tag{C3}
\]
The initial field is angularly constant; the integral has the same strip.
The square-root rescaling converts Kelvin inversion into reflection and
removes the first derivative from the logarithmic radial operator.

The current draft already accommodates a strip integral with entire
continuation. In particular,
\[
P(u)=e^{|u|}A(e^{2|u|}),\qquad
G=\tfrac12e^{-|u|}-P,\qquad
16H(0,z)=1-(1+z^2)\int_{\mathbb R}P(u)e^{izu}\,du.
\tag{C4}
\]
The last integral is entire, but \(P'\) jumps by \(-1\) at zero.
It gives \(H(0,\pm i)=1/16\). The vanishing prefactor in (C2)–(C3)
cannot be evaluated there while ignoring divergence of their integrals.

## 3. Geometry, coordinates, measure, and state are separate choices

The cylinder is optional. Ordinary Euclidean volume already gives the
short full-space identity (C2). The logarithmic variables simplify the
Fourier character, inversion symmetry, and conjugated differential
operator. They do not establish a preferred physical geometry.

The exact dictionary is
\[
\begin{gathered}
X=e^{2u}\omega,\qquad dX=8\pi r^3d\mu,\\
g_{\mathbb R^3}=4e^{4u}g_{\mathcal C},\qquad
g_{\mathcal C}=du^2+\tfrac14g_{\mathbb S^2},\qquad
dV_{\mathcal C}=\pi d\mu,\\
\Delta_X[r^{-1/2}f(u,\omega)]
=-\tfrac14r^{-5/2}\mathcal Lf.
\end{gathered}
\tag{C5}
\]
One may use logarithmic coordinates while retaining the Euclidean metric
and volume. Choosing the cylinder product metric is an additional step.
**Ordinary Euclidean heat and ordinary cylinder heat are different
evolutions.** A change of variables in one fixed evolution must carry its
coefficients, rescaling, volume, and boundary conditions along with it.

The evolved field must also be named. Heat on \(V\), on
\((\Delta_3\Theta)(|X|)\), on a weighted Euclidean density, and on
\(G\) are different proposals; the same word “heat” does not identify
the same law after rescaling.

The functional classes matter:

| Object | Initial class and endpoint behavior |
| --- | --- |
| \(V(|X|)\) | Smooth positive Euclidean potential; bounded at zero, \(1/r\) tail; not in \(L^1(dX)\). |
| \(V(r)r^{-5/2}\) | Integrable Euclidean density with a singularity at zero; not a smooth Euclidean Schwartz density. |
| \(G(u)\) | Smooth positive even function with exponential tails; Schwartz on the real line, but without exponential moments of every rate. |
| \(e^{tu^2}\Phi(u)\) | Canonical source with all exponential moments for every real \(t\); this is what supports the entire source integral. |

Thus a convenient smooth potential, an integrable density, and a
source with an entire Fourier integral should not be treated as the same
state space. Future existence and integration-by-parts arguments must
use the class of the field actually being evolved.

## 4. Decisions now fixed, and decisions still open

| Choice | Current disposition |
| --- | --- |
| Book layout and principal notation | Keep the draft as it stands; \(H,V,G\) lead, with the \(F\) alternative in Section 4. |
| Three-dimensional versus radial display | Retain full-space and cylinder integrals. Radial reductions remain useful for derivation and inversion. |
| Euclidean or cylinder geometry for an auxiliary flow | Open. Decide from the complete flow equations and estimates, not from the shortest initial display. |
| Initial analytic representation | The draft uses smooth \(V,G\) with a strip and the entire \(P\) companion. No replacement is requested. A later flow must justify its own domain. |
| Exact observation preservation versus a known nonvanishing multiplier | Still open. Including both possibilities in the draft did not approve a relaxation of the invariant. |
| What “preservation” quantifies over | Specify all real spectral values, all values in an analytic domain, or a fixed marked value/jet. These are different requirements. |
| Newman time versus an auxiliary or combined flow | Newman is the reference direction. It has not been selected as the only permitted evolution or replaced by a new one. |
| Angular dependence | Available in the state space; no mechanism creating it from exactly radial data has been selected. |
| Nonlinear or coupled-field mechanism | Open. No new candidate, canonical separating estimate, or collision exclusion is supplied by this handoff. |

Keep the source field independent of the spectral argument and the
observation kernel explicit in the present setup. If a new construction
changes that arrangement, state the change and its purpose in the new
note rather than importing it silently.

For integrable cylinder fields, exact preservation of every real pairing
in (C3) fixes the spherical mean by Fourier uniqueness. Radial fields
then cannot evolve nontrivially while keeping those pairings exactly
fixed. Angular freedom remains, but a unique rotation-equivariant
evolution from radial data stays radial. A proposed angular mechanism
must identify the extra field, asymmetric data, or changed hypothesis.

Conservation of total mass fixes only the zero-frequency observation.
Neither a single marked pairing nor mass conservation can be substituted
for preservation of the complete spectral family.

## 5. Exact flow benchmarks already available

### Cylinder heat: zero preservation through a known factor

For \(\partial_sG_s=\Delta_{\mathcal C}G_s\), \(s\ge0\), observation
with the same kernel gives
\[
\mathscr H_s(z)=e^{-sz^2}H(0,z).
\tag{C6}
\]
This preserves every zero and multiplicity, and permits exact recovery
of \(H\), but does not preserve the values of all observations. The
identity holds by the pairing in the strip and by continuation elsewhere.
It is a useful comparison if a known nonvanishing multiplier is allowed;
it is not the already selected auxiliary law.

### Newman flow transported to the generator

The canonical decaying inverse gives
\[
\begin{gathered}
G_t(u)=4\int_{\mathbb R}e^{-|u-v|}e^{tv^2}\Phi(v)\,dv,\\
\mathcal LG_t=8e^{tu^2}\Phi,
\qquad \partial_tG_t=\mathcal L^{-1}u^2\mathcal LG_t.
\end{gathered}
\tag{C7}
\]
This is on the source-defined analytic class, not an unrestricted
backward-heat well-posedness theorem. Multiplying \(G\) directly by
\(e^{tu^2}\) is not this evolution and destroys integrability at
positive \(t\).

### Constant linear combination: an exact rescaling benchmark

For constants \(\alpha,\beta\ge0\), the proposed combination induces
\[
\partial_\tau\mathscr H
=-\alpha\mathscr H_{zz}-\beta z^2\mathscr H.
\tag{C8}
\]
For \(\alpha\beta>0\), define
\[
\gamma=2\sqrt{\alpha\beta},\quad
c=\sec(\gamma\tau),\quad
T=\tfrac12\sqrt{\alpha/\beta}\tan(\gamma\tau),\quad
b=\tfrac12\sqrt{\beta/\alpha}\tan(\gamma\tau).
\]
The exact canonical observation is
\[
\boxed{\mathscr H(\tau,z)=\sqrt{c(\tau)}e^{-b(\tau)z^2}
H(T(\tau),c(\tau)z),\qquad
0\le\tau<\frac{\pi}{4\sqrt{\alpha\beta}}.}
\tag{C9}
\]
For \(\beta=0\) this becomes \(H(\alpha\tau,z)\); for
\(\alpha=0\) it becomes \(e^{-\beta\tau z^2}H(0,z)\).
The positive spectral rescaling and nonzero Gaussian factor carry the
same zeros and multiplicities. This specific benchmark adds no collision
exclusion. Nonlinear, variable-coefficient, or coupled-field proposals
are outside that conclusion. The observation solution also does not
assert global existence for arbitrary spatial data.

The separate observation generators satisfy
\[
[-\partial_z^2,-z^2]=4z\partial_z+2.
\tag{C10}
\]
A two-time construction therefore needs compatibility; one cannot impose
both as commuting evolutions without checking the resulting condition.

## 6. The next bounded continuation should compare actual flows

Start by comparing ordinary Euclidean heat on the **potential \(V\)**
with ordinary cylinder heat on the **generator \(G\)**. This is a
proposed baseline calculation, not an adoption of either law. Cylinder
heat already has (C6); the Euclidean candidate needs its own complete
observation calculation. Do not replace heat on \(V\) by heat on a
weighted density without identifying that as another candidate.

A useful next note should:

1. State the evolved field, spatial metric and measure, initial data,
   time domain, and boundary/decay class for each candidate.
2. Carry each fixed law through (C5), retaining all variable coefficients
   and field-rescaling terms. Distinguish this translation of one law
   from choosing a different Laplacian on the other space.
3. Differentiate the complete observation. Retain prefactors, source
   terms, and the origin/infinity boundary terms; establish the integral
   domain before using analytic continuation.
4. State exactly what the law preserves: values, a known multiplier,
   multiplicities, a spectral rescaling, or only selected moments. This
   computation should inform the invariant choice.
5. Compare the result with (C6)–(C9). If it is just another reparametrization
   of the same zeros, record that precisely. If it changes the proposed
   spatial diagnostic at a multiple zero, identify what additional
   canonical estimate would be required to use that change.

The desired return is the pair of explicit evolution/observation
identities and their valid domains, followed by a reasoned geometry and
invariant comparison. A new nonlinear mechanism or a numerical campaign
need not precede this comparison. Keep the current book unchanged during
that exploratory step; save the comparison as a new numbered note.

## 7. Controls, scope, and handoff practice

Consult the [result index](../../../../result-summaries/README.md),
especially [geometric realizations](../../../../result-summaries/16_hypercomplex_reductions_and_geometric_realizations.md)
and [collision controls](../../../../result-summaries/12_collision_controls_and_screening.md),
and the [pattern index](../../../../avoid/README.md), especially
[target classification](../../../../avoid/01_restating_the_target.md),
[shared control premises](../../../../avoid/02_shape_only_arguments_and_the_controls.md),
[coordinate re-realizations](../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md),
and [scoped exclusions](../../../../avoid/07_scoped_exclusions_read_as_universal.md).

The inherited analytical control comparison remains:

| Control | Premise not shared with the canonical application |
| --- | --- |
| Euler-factor threshold controls | Unchanged canonical theta source and conductor. |
| Weighted-square controls | Full source reflection and a global all-real heat time. |
| Reflected and positive-primitive controls | Canonical integer-square theta expansion. |
| Note01's positive Gaussian-polynomial control | Canonical integer-square expansion, completion, and double-exponential tails; only its stated local heat-time domain is available. |

The last control has an explicit double event and is transported by (C9)
where defined; see [Note01, Section 7](../notes/01_RADIAL_THETA_GEOMETRY_AND_COLLISION_MECHANISMS_20261027.md)
and the book's Section 6. Positivity, smoothness, the Green inverse,
and the constant linear benchmark do not separate it from theta.
No new numerical control run is claimed in this continuation.

This note records choices and existing exact identities. It does not
upgrade the earlier analytical status or assert a new estimate.
Detailed derivations remain in
[Brainstorm08](08_ZERO_TIME_RESCALINGS_AND_FLOW_BRAINSTORM_20261028.md)
and the book; the current reference provenance and build are linked above.

A new chat should register its own identity in this investigation's
`chat-histories/`, without reusing chat0015. An existing registered chat
should retain its unique identity and refresh it under
[the standing history workflow](../../../../tools/CHAT_HISTORY.md).
Preserve both change notes and use new numbered notes for substantial
alternative formulations. Later accepted book changes should be made in
place, with a concise entry in the investigation's draft history and no
new manuscript snapshot folder.
