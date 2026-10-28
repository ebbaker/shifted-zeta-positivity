# CTF-E02 request R1: quantify the conservative feedback payment gap

28 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort
max**, Investigation05 chat0009 **Continue conservative theta flow**.

**Type: E — execution. Recommended model: Sol. Revision: R1. Optional.**
The [live register][progress] owns status. The default substantive next
task is **[B] CTF-B02 — Astra**. This packet fixes a small scalar audit;
it does not choose an actual execution model or effort, authorize a PDE
experiment, or make its completion a prerequisite for B02.

## Question and known disposition

How large is the gap between the generic guaranteed existence time and
the paid collision deadline, and which of the energy-observation and
absolute-moment payments dominates it on the existing eleven examples?
Report the already acquired direct H/H_a information alongside it.

[Note28][note] equation(22) already proves that the ratio of these two
times is less than 1/100 for every admissible source in this comparison.
No computation is needed to decide whether these particular payments
exclude a collision: **they cannot**. E02 measures the extent and source
of this loss, if that quantitative calibration is useful to B02. Do not
present the known inequality as the research result or use a test of it
as evidence for theta noncollision. A large loss points to a weak
assigned bound, not an actual short lifespan or a failed flow theorem.

## Frozen inputs and provenance

Read the complete proof and [assessment16][review]. Verify these SHA-256
values before calculation:

| Input | SHA-256 |
| --- | --- |
| Note28 | `519dda1bdb4418b0cc7cea0f0fa2c403e3542196c7de1ade29cfda169649879c` |
| [E01 record16][record] | `a7c742bfc3bb0a4e2841c57fb0d9b1ff4560c6a157552cbad3ef6124d35361d3` |
| [Note25][n25], source normalization | `321d557080ef06abb3e8a70f85872f1e10980881a91fc47806d54ab9b050e11b` |

Hashes identify inputs, not mathematical correctness. If a source changed,
identify the difference and issue a revised request if it changes the
contract. Do not silently recompute with a new normalization. Reuse
record16's `raw_samples`, `quantities`, error categories, exact control
references and provenance. Its 30/50-digit runs are floating diagnostics,
not numerical enclosures.

The candidate is exactly Note28 equations(2)–(5): full space R3, unit
preparatory heat, unit diffusivity and jet weight,
v=X+X/(1+|X|^2), alpha=2G/D, and a fixed mark p=(T,A) with a separate
running spectral parameter. W0 is the pre-smoothed density/actual-jet
pair. Preserve the mark and derivative distinction. No flow coefficient
or spatial profile is to be tuned in E02.

## Fixed scalar formulas

Use C_(m,k)=integral exp(2mu) rho_t(u) u^k du for m=0,2 and k=0,1,
and only F_(4,k) from the existing heat data. All C values are positive
majorants; they are not frequency-dependent absolute moments.

\[
C=C_{0,0}+C_{0,1},\qquad
\overline P=\sqrt{C_{0,0}C_{2,0}}+
\sqrt{C_{0,1}C_{2,1}}+\frac4{\sqrt\pi}C,
\]
\[
\overline G=\frac34(8\pi)^{-3/2}C^2,\qquad
\underline E=\frac{(24\pi)^{3/2}}{(16\pi)^3}
                  (F_{4,0}^2+F_{4,1}^2),
\]
\[
\underline S_{\rm local}=\frac1{20}
  \log\!\left(1+\frac{3\underline E}{\overline G}\right),\quad
\overline S_* =\frac{60}{7(5\pi^2)^{2/5}}
  \frac{\overline P^{4/5}}{\underline E^{2/5}}.
\]

The exact inequalities behind these formulas are P0<=Pbar,
G(0)<=Gbar, E0>=Eunder. Existence is guaranteed for
s<S_local_lower, with a strict endpoint convention. The collision
deadline is conditional on (H,H_a)=(0,0). It is not an upper bound on
lifespan at an arbitrary noncolliding point.

Check the factors by the K3*K1=K4 identity and the Gaussian gradient
and first-moment formulas in Note28; do not add a PDE discretization to
check identities already proved analytically.

For resolved positive Eunder, report gamma=S_local_lower/S_star_upper
and its reciprocal Q. Also report
eta=(F4,0^2+F4,1^2)/C^2 and p=Pbar/C. The overall source scale cancels.
Use the expression for gamma in Note28 equation(22) as an implementation
cross-check. To separate the two payment losses, compare Q to its formal
reference value at eta=1 and p=1+4/sqrt(pi); the eta loss factor is

\[
L_\eta=\eta^{-2/5}
\frac{\log(1+3\sqrt3/2)}{\log(1+(3\sqrt3/2)\eta)},\qquad
L_p=\left(\frac{p}{1+4/\sqrt\pi}\right)^{4/5}.
\]

These factors describe the assigned comparison, not measured errors or
an optimality bound. Do not infer an actual flow profile from them.

## Cases, error accounting and limits

Use exactly the eleven E01 source/time/frequency points:

| Source | Physical time | Frequencies |
| --- | --- | --- |
| Complete theta | 0 and 1/4 | 0, 2sqrt(6), 28, 30 |
| Gaussian-polynomial control | T_c=1/4 | 2sqrt(6)-1/4, 2sqrt(6), 2sqrt(6)+1/4 |

Evaluate the displayed algebra at 30 and 50 decimal digits from the saved
values at those precisions. No new integral evaluation, precision level,
theta-index cutoff, physical case, auxiliary time or refinement is
permitted. A zero or unresolved energy payment remains unresolved.

For a separate diagnostic-adjusted version, use the recorded total
acquisition allowance epsilon_q for each quantity q. Replace every
positive C by C+epsilon_C, and each absolute F entering the lower energy
by max(abs(F)-epsilon_F,0). Propagate those values monotonically into
Pbar, Gbar, Eunder, the two times and gamma. Keep nominal and adjusted
versions distinct. Preserve the theta-index, u-tail, quadrature and
precision-difference categories supplied by E01; no rigorous roundoff
bound was acquired there. Algebraic propagation of those allowances
does not upgrade them to interval certification. Additional scalar
roundoff is monitored only by the declared precision comparison.

Copy the direct H/H_a observations and their allowances from the same
record; their role is a matched existing-information comparator. Preserve
H_*=H_{*,a}=0 exactly at the control event a=2sqrt(6), rather than
substituting quadrature residuals. The theta a=0 derivative vanishes
by symmetry but H>0. Neither the exact control event nor this symmetry
example is a newly discovered zero.

Cap scalar processing at **60 seconds** with time checks between cases.
Count **zero new integrand evaluations**. Report measured processing
time, without claiming that reuse makes the original acquisition free.
There is no optimization, PDE run, zero search, new source scan or larger
height domain. Failure of a hash, unavailable input or unresolved energy
payment is a bounded result, not permission to expand this request.

## Return and stop rule

Save reproducible code and a small JSON record in `numerics/`, and a short
return note or assessment in the established folders. Include the actual
model/effort, date, R1, source/code hashes and software versions. Report
all eleven nominal and diagnostic-adjusted rows at both precisions,
unresolved ratios, eta/p loss decomposition, direct comparator, and
actual processing cost. Keep unfavorable or extremely weak payments.

The substantive disposition is which payment dominates, how the theta
and control cases differ quantitatively, and whether this optional audit
helps specify a sharper bound. It does not test the truth of equation(22)
or the reformulation in equation(18). If the computed ratio violates the
proved structural bound beyond its declared diagnostic uncertainty,
first resolve the implementation or input issue; do not call it a
collision exclusion.

Completion means the finite question has a documented answer or precise
input/budget limitation. Stop then. **Next: [B] CTF-B02 — Astra** for an
independent canonical gradient/response bound. A changed flow, parameter
jet or observable is a **B01 revision**; an unresolved canonical estimate
belongs in **B02**, not a larger E02 calculation. Issue E03 only when B02
has specified an inequality requiring finite rigorous inputs.

Permitted writes are the new code/record, return note/assessment, an
appended return link here, the live progress entry and necessary
navigation. Keep this request frozen. Do not edit the manuscript, E01
acquisition data or the proof source as part of this scalar audit.
Follow [LARGE_FILES.md](../../../../../LARGE_FILES.md). No numerical
execution or values for these new payments are asserted by this packet.

[progress]: ../04_CONSERVATIVE_THETA_FLOW_RESEARCH_PROGRESS_20261028.md
[note]: ../../notes/28_ENERGY_NORMALIZED_CONSERVATIVE_COLLISION_MAGNIFIER_20261028.md
[review]: ../../reviews/16_CONSERVATIVE_FEEDBACK_MAGNIFIER_B01_ASSESSMENT_20261028.md
[record]: ../../numerics/16_CONSERVATIVE_HEAT_BASELINE_MEASUREMENTS_20261028.json
[n25]: ../../notes/25_TOTAL_INTEGRAL_CONSERVATION_AND_DIRECTION_FREE_HEAT_FLOW_20261027.md
