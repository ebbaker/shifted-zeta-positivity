# CTF-E07 R2: fixed radial compact-coefficient request

**Issued 29 October 2026; preserve this request unchanged.** Prepared for
Edward Baker with substantial LLM assistance, **gpt-6.1-sol / ultra**,
Investigation05 chat0021. Parent: CTF-B02 R4, complete bounded result in
Note42; E08 integration complete in Review23.

**Type E; recommended model Sol.** The remaining calculation is ordinary
scalar/cutoff calculus for one previously defined coefficient. The author
requested a Sol continuation after manuscript integration. The actual
executing model and effort must be recorded by the executor. The sole
Progress05 register owns live status; this request is ready, not executed.

## Frozen quantities and question

Keep the complete theta source, prepared radial class on
P=[0,1/2] x [1,6], original conservative feedback, actual fixed-mark jets,
nonzero residual, exact source-operator cutoff and omega=(1+r^2)^(-2).
The only quantity to acquire is Note40's exact
\[
 B_1=\sup_X\omega\,|b\cdot\nabla v-v\cdot\nabla b|,
 \quad b=\eta(r)\log r\,X,\quad v=\lambda(r)X,
 \quad\lambda(r)=1+(1+r^2)^{-1}.
\]
Here eta=h(4r-2), with h=0 for t<=0, h=1 for t>=1, and
h(t)=exp(-1/t)/(exp(-1/t)+exp(-1/(1-t))) in 0<t<1.

**Target:** one explicit proved b_star<455/24 with B1<=b_star over all
space. No optimal or near-optimal value is requested. Then prove
\[
 \kappa_1-\kappa_{1,\rm rad}
 \ge455/24-b_{\rm star}>0,
 \quad\kappa_{1,\rm rad}=265/24+B_1+B_0,
\]
using the exact max identity in manuscript (7.25). For the same actual B,
the radial compact upper allowance for F+E0 is smaller than the old
compact allowance by the factor exp[-(kappa1-kappa1,rad) B]. Explain the
strict gain for B>0 and its bound from b_star. This does not control B
through a collision deadline.

## Fixed route, finite scope, and acceptance

Differentiate only the stated radial vector fields. For r>0 their
coefficient reduces exactly to
\[
 B_1=\sup_{r\ge0}\frac{r}{(1+r^2)^2}
 \left|\eta(r)\{r\lambda'(r)\log r-\lambda(r)\}
       -\lambda(r)r\eta'(r)\log r\right|,
\]
with smooth zero continuation at the origin. Retain the eta' term.
Pay three fixed domains: r<=1/2 (zero), 1/2<r<3/4 (t=4r-2 and
eta'=4h'(t)), and r>=3/4 (eta=1, eta'=0). Splitting the last at r=1
is a permitted routine choice. Derive one conservative bound on h' from
its displayed formula and use elementary logarithmic/rational bounds to
pay the compact annulus and whole tail. No source integration is involved.

Acceptance requires a written all-radius proof with an explicit b_star,
the strict compact comparison, and the unchanged domain/control limits.
One finite analytical proof is the whole task: no optimization, adaptive
search, coefficient campaign, floating sample, interval computation or
PDE simulation. Ordinary algebraic simplifications and conservative
inequalities within these fixed domains are permitted. If the proposed
payments do not reach the threshold, return the exact unresolved bound
and domain to B02; do not switch method/target or alter eta, omega, the
functional, source or PDE. No second coefficient is included.

B1 is a fixed drift/cutoff budget independent of T,a and the theta
logarithmic derivative. The full source still enters the other unchanged
budgets/data. The exact colliding control remains admitted with both
terms of its same-theta-operator preparation residual. Preserve sphere
cancellation, actual jets and inner-ball accounting. No new exclusion,
first-jet information or acquisition-cost advantage follows.

## Return and permitted changes

Save one new analytical return in notes/ (next available number), with
actual model/effort, input hashes, b_star and proof or exact failed
payment, comparison and scope. Update only the corresponding Progress05
row and minimal navigation. Do not alter this issued R2 request, R1,
Notes39–43, Review23 or manuscript in this execution. No code/numerics
record is required for an analytical proof. Recommend E08 for a completed
result, or B02 with the precise failed premise; do not execute a new
scientific task automatically.

## Frozen input identities

Hashes identify the request inputs, not their mathematical validity.

| Input | SHA-256 |
| --- | --- |
| `notes/31_CANONICAL_SOURCE_RELATION_AND_PREPARATORY_COMMUTATOR_20261028.md` | `9d2a9832f3a128d3bb2c3fc37eb7ab83547f2f9d35c16c82847ef7994795b8ec` |
| `notes/40_WEIGHTED_RESIDUAL_CLOSURE_E07_R1_RETURN_20261029.md` | `abbb999e364006ea3558869a29d39a648922c85f0df71e09fa23dd1c0b90440e` |
| `notes/42_RADIAL_DRIFT_PRODUCTION_IMPROVEMENT_B02_R4_20261029.md` | `895a3f9524bb871d66f6ceae840e55f013f2a012df934abb78499dd73261634c` |
| `notes/43_RADIAL_DRIFT_INTEGRATION_SOL_CONTINUATION_20261029.md` | `e2e0bf9f529cd255885e444ea350095e323074372711cd4d14e407cc1e569706` |
| `reviews/23_RADIAL_DRIFT_IMPROVEMENT_E08_INTEGRATION_20261029.md` | `44c40831c6eb9103dba4d793e029a934ca02c42fdd5ef378b47bf451a69ba8a0` |
| `radial_deformations_and_zero_dynamics.tex` | `394ce86b6a5ab432015f1b4b3ed86bed3896070618fbe84afc196e44fb7bd238` |
