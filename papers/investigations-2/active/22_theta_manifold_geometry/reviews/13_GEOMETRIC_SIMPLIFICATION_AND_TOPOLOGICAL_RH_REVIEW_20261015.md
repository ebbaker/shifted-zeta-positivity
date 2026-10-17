# Geometric simplification and topological formulations of RH

> **17 October 2026 — history routing update.** Historical formal-replay routing below is superseded. Chats [22](../chat-histories/0022_2026-10-15T18-10-39Z_review-theta-manifold-geometry.json) now use this investigation's [local registry](../chat-histories/index.json), as recorded in the [relocation receipt](../CHAT_HISTORY_RELOCATION_20261017.json). Original identities, provenance and public messages are preserved. All future Investigation 22 chats belong in this local history folder.

15 October 2026, America/New_York. Prepared for Edward Baker with substantial LLM assistance. Recorded coordinating model **gpt-6-astra**, reasoning effort **ultra**, verified from the current turn metadata. Three independent LLM subtasks reviewed the geometric argument, Investigation 21, and topological/literature alternatives. This is internal review, not external refereeing or formal verification.

## Assessment of the current manuscript

The [manuscript](../manuscript/theta_manifold_geometry.tex) and [continuation note 11](../notes/00_research_coordination/11_SCALAR_MANUSCRIPT_AND_POSITIVE_TAIL_CONTINUATION_20261015.md) correctly distinguish proved geometric reductions from the missing theta-specific estimate. The strongest current simplification is the classification of the complete backward stationary locus as one analytic curve with a principal physical-jet factor. The checked scalar signed quotient and prescribed-cone arguments retain the necessary uniformity through an event. No new defect was found in those arguments.

The remaining target

\[
WB_\partial\le CW^2+\varepsilon|W|
\]

is an analytic arithmetic estimate. Changing the ambient special-holonomy language does not estimate its invariant trace. The completed positive-tail pilot establishes a finite box and a useful tail-orientation lemma, but the same sign holds for arbitrary positive tails with the same first mode. Its stopping decision is justified: it supplies no new theta-specific discriminator or demonstrated computational advantage.

This review did not modify the manuscript or recompile its 49-page PDF. Its assessment is a targeted derivation and research-direction review, not a fresh reproduction of all prior numerical receipts. Existing working-tree manuscript changes were preserved.

## A compact surface reformulation is available

The [compact surface note](../notes/01_physical_jet_geometry/05_JENSEN_HYPERELLIPTIC_TOPOLOGY_20261015.md) proves a precise answer to the manifold question. Define

\[
f(z)=\xi(1/2+\sqrt z)=\sum_{k\ge0}\gamma_k z^k/k!,
\qquad J_d(X)=\sum_{k=0}^d\binom dk\gamma_kX^k,
\]

with \(f\) understood through its entire power series. The coefficients are explicit positive moments of the same complete theta source. Let \(C_g\) be the smooth projective normalization over \(\mathbb R\) of

\[
y^2=J_{2g+1}(x).
\]

Then

\[
\boxed{\mathrm{RH}\iff b_0(C_g(\mathbb R))=g+1
\quad\hbox{for every }g\ge1.}
\]

The object is a compact surface with its conjugation involution. The fixed circles, rather than the abstract unmarked surface, distinguish real from nonreal branching. The specified count also forces the expected genus \(g\), so repeated polynomial roots are not silently excluded by definition. Saying only that every normalization is an M-curve relative to its actual genus would be too weak: normalization can erase complex square factors.

The forward proof needs strict Jensen hyperbolicity even if RH allows multiple zeta zeros. A finite-factor argument supplies it: select \(d\) negative-zero factors from the genus-zero Hadamard product for \(f\), apply their operators \(1+a_iD\) last to the real-rooted polynomial supplied by the remaining product, and use the elementary multiplicity-drop/interlacing lemma. No assumption that zeta zeros are simple is made. The reverse proof uses normalization, the odd-degree real-component formula, and locally uniform Jensen convergence. Two independent mathematical reviews checked these points.

This is a rigorous synthesis of classical results. The relevant Jensen framework is explicit in [O'Sullivan](https://fsw01.bcc.cuny.edu/cormac.osullivan/Research/xi-revised.pdf) and [Griffin, Ono, Rolen and Zagier](https://arxiv.org/abs/1902.07321); the topology belongs to classical real algebraic geometry, including [Gross and Harris](https://www.numdam.org/item/10.24033/asens.1401.pdf). The exact compact-family formulation was not located in a bounded search, but that is not evidence of originality. A publishable novelty claim requires a broader comparison and a contribution beyond the composition of these ingredients.

## A simpler criterion inside the existing heat-flow program

The [spacetime note](../notes/01_physical_jet_geometry/04_SPACETIME_INDEX_AND_MARKED_TOPOLOGY_20261015.md) proves that every order-\(m\) event has local first-jet index

\[
\operatorname{ind}(H,H_x)=-\lfloor m/2\rfloor
\]

with orientation \(dt\wedge dx\). Therefore a nonzero boundary jet has

\[
\operatorname{wind}_{\partial D}(H+iH_x)
=-\sum_{\text{interior events}}\lfloor m/2\rfloor.
\]

Every contribution has the same sign. A zero-winding boundary certificate excludes all interior collisions, using one spacetime first jet for both even and odd multiplicities. The temporal phase component detects the cubic control that the first spatial Laguerre sign misses. Investigation 21 contributes the exact global normalization, Hermite splitting, positive imaginary-axis values, strip bounds, and time-uniform confinement needed to turn compact winding tests into an RH-equivalent exhaustion. The stabilized winding also equals the upper-right-quadrant nonreal-zero count at the initial time.

The degree mechanism is already explicit in [Angenent, §3](https://people.math.wisc.edu/~angenent/preprints/extatic.pdf). Its useful research contribution here is the concrete theta boundary target and possible certification method. A bound on a one-dimensional boundary can avoid a two-dimensional interior energy floor. A boundary approximation with a strict nonzero homotopy margin determines the integer winding; the sign law then rules out hidden cancelling collisions.

## Geometry that does and does not retain the obstruction

The four-dimensional jet surface is a curve times a flat complex line. At an order-\(m\) zero its transverse primitive curve has embedded link \(T(m,m+1)\), while its abstract local topology is still a disk. The physical metric has cone angle \(2\pi m\), but cone angle is metric information. The complex projective Gauss map extends across the event after cancelling its common factor. These constructions therefore require an embedding, a metric, or a marked real section to detect the obstruction.

Moving the circle phase into an unrestricted \(S^3\) or \(S^7\) destroys its fundamental-group obstruction. The theta line bundle's fixed degree, an auxiliary ASD connection, and the existing calibrated inclusions do not recover it. Investigation 21's positive-source and endpoint controls continue to be essential tests against any claimed arithmetic sign mechanism.

## Recommended next work and publication threshold

There are two distinct useful directions.

1. **Compact real surfaces.** Develop the exact Jensen-surface equivalence as a short, carefully attributed mathematical note, followed by a deeper novelty review. The natural next substantive question is whether the theta moment structure gives a useful geometric constraint on this family beyond classical polynomial hyperbolicity. The reciprocal polynomials \(R_d(X)=X^dJ_d(1/X)=f(D)X^d\) satisfy \(R_d'=dR_{d-1}\); this is an explicit hierarchy to study, but it does not automatically give holomorphic maps between the curves or prove their maximality.
2. **Boundary winding certificates.** Run one bounded theta pilot on a box where neither \(H\) nor \(H_x\) has fixed sign. Certify every boundary segment, compute winding by a polygonal homotopy, retain the complete theta tails, and compare work with the current stationary/interior approach. A real advantage or a new arithmetic boundary estimate would make the reformulation more than a change of vocabulary.

A new nontrivial reformulation can be publishable without proving RH. Here there is an exact compact-surface equivalence to assess, but publication readiness is not established. General winding, ordinary cusp links, and generic compactification should not be presented as newly discovered principles. The strongest next deliverable would combine a correct attributed equivalence with a new structural or quantitative theorem that uses it.

## Verification and provenance

The exact [checker](../numerics/check_spacetime_topology.py) passes **1,573 assertions across 60 rectangles**, covering multiplicities 2 through 16, symmetric and asymmetric heat germs, and both overall signs. It uses rational polynomial arithmetic and Sturm root isolation to compute oriented ray crossings independently of the half-zero-count formula. It verifies that additional asymmetric roots lie outside the local box. A separate-process replay has identical mathematical content after removing only the capture timestamp. These checks concern polynomial controls, not a new theta sign domain, compact-curve numerical certification, or RH.

The [verification manifest](../numerics/TOPOLOGICAL_REFORMULATION_REVIEW_20261015.json) records the reviewed inputs, notes, checker, receipt and replay comparison. Formal replay identity **22**, thread `01a140c2-517a-7b73-8684-502f71e31500`, is retained in the [canonical history](../chat-histories/0022_2026-10-15T18-10-39Z_review-theta-manifold-geometry.json). No manuscript snapshot, commit or tag was created.
