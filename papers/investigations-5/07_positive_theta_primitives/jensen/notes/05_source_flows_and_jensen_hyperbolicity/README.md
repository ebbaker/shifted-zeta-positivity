# Source flows and Jensen hyperbolicity

1 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**, reasoning effort **xhigh**. Organization task J-E04.

This direction changes the source and therefore the coefficients. It asks whether the induced Jensen-polynomial evolution can preserve real-rootedness along a justified path to the canonical theta target.

**Research task: J-B08, B — Astra.** Choosing a reflection-compatible source generator and a root-preservation mechanism is conceptual work. The [sole progress register](../../research-progress/01_JENSEN_RESEARCH_PROGRESS_20261101.md) owns status.

## Target and distinction from conservative integrand flows

For an evolving source \(\Phi_s\), define
\[
c_n(s)=\frac1{(2n)!}\int_0^\infty u^{2n}\Phi_s(u)\,du,
\qquad J_s^{d,n}(X)=\sum_{j=0}^d\binom dj(n+j)!c_{n+j}(s)X^j.
\]
A useful path needs a known hyperbolic starting family, a proved evolution in the direction leading to theta, and a justified endpoint or limiting passage. Source positivity and positive averaging alone do not preserve polynomial real-rootedness.

For illustration only, if an actual induced equation were
\[
\partial_sP_s=-a(s,X)P_s''+b(s,X)P_s'+c(s,X)P_s,
\]
its simple real roots would satisfy
\[
\dot x_i=2a(s,x_i)\sum_{j\ne i}\frac1{x_i-x_j}-b(s,x_i).
\]
Local repulsion when a>0 is not a global preservation theorem. Degree, leading coefficient, multiple roots, full parameter coverage and convergence still need proof. No such theta path is presently constructed.

## First bounded question

Select at most one source-flow candidate preserving the full evenness and endpoint compatibility needed by the chosen representation. Derive the induced moment or Jensen evolution far enough to identify a concrete root-preservation theorem or the mixed quantities preventing closure. Keep fixed small shift, especially n=0 with increasing d, in the scope statement.

**Completion:** a specified candidate and exact missing root estimate, a usable proof route, or a scoped obstruction. No automatic flow or root-sampling campaign follows. Do not equate k=0 triangular Toeplitz positivity with n=0 Jensen hyperbolicity.

## Existing obstruction and reading

- [Note14, Section 6](../14_HIGHER_ORDER_SIGNED_AVERAGING_AND_RADIAL_FLOW_FEASIBILITY_20261101.md) gives the direct Jensen integral, the positive-averaging counterexample and the local root formula.
- [Investigation05 chat0053](../../../../05_radial_theta_collision_geometry/notes/CHAT0053_SOURCE_TRANSPORT_UNBOUNDED_STRIP_OBSTRUCTION_20261031.md) rules out its precise raw radial transport with fixed logarithmic cosine, including the endpoint-recentered variant, as an all-real intermediate family. It does not rule out every source flow.
- The odd logarithmic velocity proposed at the end of that note preserves evenness but has no proved hyperbolicity advantage. Retain that status if it is selected.
- [Conservative negative-mass flows](../03_conservative_negative_mass_flows/README.md) preserve the target integral instead; the two directions require different transfer arguments.

## Organization

Save new derivations in this folder. Put computations and small records in the matching `jensen/numerics/05_source_flows_and_jensen_hyperbolicity/` subfolder and assessments in `jensen/reviews/05_source_flows_and_jensen_hyperbolicity/` when first needed. Keep one canonical source for reusable results and link applications. Existing numbered notes and this chat’s registration keep their current locations.

[Ideas index](../../../ideas/README.md) · [Common assessment](../14_HIGHER_ORDER_SIGNED_AVERAGING_AND_RADIAL_FLOW_FEASIBILITY_20261101.md) · [Live register](../../research-progress/01_JENSEN_RESEARCH_PROGRESS_20261101.md)
