# Integrated RS development and averaged Green values

11 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. The actual model identifier and
reasoning effort are unavailable in this chat's recorded configurations
(child chat0004); no recommendation is used as provenance.

**Status: proved in-note from the named inherited inputs; same-assistant
self-check only.** The manuscript integration preserves its sources'
original statuses. The new consequence is an averaged-value theorem at
**c=1**, not a new arithmetic estimate at exceptional centers. The
[self-check](../reviews/10_GNP_RS_MANUSCRIPT_AND_MEAN_SELF_CHECK_20261111.md)
and [build/input record](../../numerics/02_GNP_RS_INTEGRATION_BUILD_RECORD_20261111.json)
record the scope and production checks. No numerical research was run.

Read the [result index](../../../../../result-summaries/README.md),
[heat-flow cluster11](../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md)
and [avoidance index](../../../../../avoid/README.md), particularly
[classification01](../../../../../avoid/01_restating_the_target.md),
[premises02](../../../../../avoid/02_shape_only_arguments_and_the_controls.md),
[scope07](../../../../../avoid/07_scoped_exclusions_read_as_universal.md),
[separate bounds12](../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md)
and [status19](../../../../../avoid/19_status_files_that_lag_the_findings.md).
The control screen uses [controls12](../../../../../result-summaries/12_collision_controls_and_screening.md).

## 1. Manuscript first: one development through E06

The user's request authorizes updating the current manuscript and
systematically deriving its relevant results. The existing parent
[live manuscript](../../manuscript/main.tex) was updated first with
Notes03,05,07,10,11,14,16–18. No manuscript snapshot or separate child
manuscript was created. Three successive sections now develop:

| Live section | Content and proof source |
| --- | --- |
| [Transition reduction](../../manuscript/sections/10a_transition_green.tex) | Harmonic carrier; complete fixed-buffer field input; uniform outer baseline with both reflected population and correction paid; true log exterior; one-sided regularization; shifted-zeta divisor and pole. Notes03,05,11. |
| [Coherent moments](../../manuscript/sections/10b_coherent_moments.tex) | Diagonal, all oscillatory pairs, cutoff endpoints, fixed-clock comparison and convolution edges; exact Jensen obstruction; prime exponential mean and 1/1000 phase-only failure; fixed-prefix transfer. Notes07,10,11. |
| [Euler references](../../manuscript/sections/10c_euler_references.tex) | Exact calibration; joint phase lemma uniform in the regulator; fixed-P residual mean, density and exceptional residuals; adaptive P=floor(L²) costs; fixed-P signed tangent failure. Notes14,17, with the further mean consequence below. |

The evidence section distinguishes inherited internal assessments,
proof-contributing assessors, and this same-assistant check. Numerics
remain in the supporting-evidence section. The final section now starts
with the unpaid exceptional-center value instead of asking for a
consumer already selected and studied. Original notes, issued requests,
reviews and historical builds are preserved.

Use (d\omega_X=K(x-X)dx) on (W_X) in the manuscript, avoiding the
parent's two-boundary probability measure (\mu_X). The outer allowance
is called (C_{\rm out}), avoiding the parent's earlier unit-log
(C_*). These are notation changes, not new normalizations. The strip,
carrier, full field, physical clock, c band and defect parameters are
unchanged. The classical ordinary-zeta series, derivative and Euler
product were checked against [DLMF §25.2](https://dlmf.nist.gov/25.2);
the existing canonical bibliography entry is reused. No new external
paper or full re-audit of the inherited HDA theorem is claimed.

## 2. The actual Green value converges in dyadic measure

Write (L_X=\log(X/(4\pi))), (J(X)=J_{1/L_X}(X)\ge0),
(q_X=\int_{W_X}K(x-X)dx\to1/2), and
(M(X)=\int_{W_X}K(x-X)|V_{1/L_X}(x)|^2dx).
Time stays fixed in each spatial integral; the height average samples
different times. E03 [Note07](07_GNP_RS_E03_COHERENT_JENSEN_OBSTRUCTION_20261111.md)
gives
\[
 T^{-1}\int_T^{2T}M(X)\,dX\longrightarrow\zeta(3/2).
 \tag{1}
\]
E05 [Note14](14_GNP_RS_E05_FINITE_EULER_RESIDUAL_20261111.md)
gives, with **fixed P** during the height limit,
\[
 T^{-1}\int_T^{2T}R_P(X,1)\,dX\longrightarrow
 \mu_P=\zeta(3/2)\prod_{p\le P}(1-p^{-3/2})-1,
 \qquad \mu_P\to0.
 \tag{2}
\]

Its density proof works at every fixed threshold (h>0), not only
(m_*). To make this extension explicit: choose fixed (\delta>0)
so (q_X\log b_\delta\le h/5), and then any sufficiently large
fixed P so the omitted prime-log subseries costs at most (h/5).
Set (r=\delta^2h/5). When (R_P\le r), its separate logarithmic
payment is at most (r/(2\delta^2)=h/10). The remaining errors are
eventually at most (h/5), for each such fixed P and δ. Thus

\[
 \limsup_{T\to\infty}T^{-1}|\{X\in[T,2T]:J(X)\ge h\}|
 \le \mu_P/r.
\]

Take arbitrarily large fixed P **after** the height limit. This proves
\[
 T^{-1}|\{X\in[T,2T]:J(X)\ge h\}|\longrightarrow0
 \quad\text{for each fixed }h>0.
 \tag{3}
\]
Neither the cutoff nor the threshold varies inside a limit justified
only for fixed values. There is no rate. This is an explicit consequence
of E05's proof, not an asserted extension to all c or a fixed-time slice.

## 3. Exponential integrability from the coherent moment

The exact quadratic allowance is an upper bound even though it cannot
pass the fixed defect margin at every center:
\[
 0\le J(X)\le\frac{q_X}{2}\log\frac{M(X)}{q_X}
       -P_{1,1/L_X}(X)+\epsilon_X,
 \quad \epsilon_X=T_X+C_{\rm out}/L_X\to0.
 \tag{4}
\]
The E03 rational proof gives (|P_{1,\lambda}|<23/100).
Eventually (q_X\ge1/4) and (\epsilon_X\le1/100). Exponentiating
(4) with exponent four yields
\[
 e^{4J(X)}\le e^{24/25}\left(\frac{M(X)}{q_X}\right)^{2q_X}
       \le e\,(1+4M(X)).
 \tag{5}
\]
Here (0<2q_X\le1) and (t^r\le1+t) for (t\ge0,0<r\le1).
For (t\le1), bound by one; for (t\ge1), bound by t. The moment
is positive, so its logarithm is defined. Also
\[
 \zeta(3/2)\le1+2^{-3/2}+\int_2^\infty u^{-3/2}du<3.
\]
By (1), its dyadic mean is at most three eventually. Consequently
\[
 \boxed{T^{-1}\int_T^{2T}e^{4J(X)}\,dX\le13e<39}
 \quad\text{for all sufficiently large }T.
 \tag{6}
\]
The constant 39 is convenient, not optimal; the onset remains finite
and unevaluated, inherited from the prior analytical estimates.
Equation (6) is a bound for the **actual** Green value in mean, not an
assertion that the failed quadratic allowance is pointwise small.

## 4. All finite power means and subcritical exponential means

Let (d_T(t)=T^{-1}|\{X\in[T,2T]:J(X)>t\}|). By (3), (d_T(t)\to0)
for every fixed (t>0). By (6) and Markov,
\[
 0\le d_T(t)\le\min(1,39e^{-4t}). \tag{7}
\]
Tonelli and (J\ge0) give, for (p>0),
\[
 T^{-1}\int_T^{2T}J(X)^p\,dX
       =p\int_0^\infty t^{p-1}d_T(t)\,dt.
\]
The bound (7) is integrable with this weight near zero and infinity.
Dominated convergence proves the first assertion below. For
(0<\alpha<4), the same argument applies to
\[
 T^{-1}\int_T^{2T}(e^{\alpha J(X)}-1)\,dX
       =\alpha\int_0^\infty e^{\alpha t}d_T(t)\,dt,
\]
since the majorant decays like (e^{-(4-\alpha)t}). We have proved
\[
 \boxed{\begin{aligned}
 T^{-1}\int_T^{2T}J_{1/L_X}(X)^p\,dX&\longrightarrow0
                    &&(p>0\text{ fixed}),\\
 T^{-1}\int_T^{2T}e^{\alpha J_{1/L_X}(X)}\,dX&\longrightarrow1
                    &&(0<\alpha<4\text{ fixed}).
 \end{aligned}} \tag{8}
\]

**The power-mean convergence does not supply an every-center estimate.**
Convergence at exponent four is not proved by (6): the layer-cake
majorant at that endpoint ceases to be integrable. No endpoint failure
for the theta field is asserted either. This conclusion is an averaged
analytical milestone under avoid01, not an RH-equivalent criterion.
It introduces no independent exceptional-center arithmetic input.

## 5. Collision controls and scope

This is an analytical premise screen at the actual witness domains,
not a rerun of the historical certificates. The generic positive-Green,
Jensen, Markov and layer-cake steps hold for any field meeting their
hypotheses. The canonical inputs (1)–(4) use the complete theta field
and the source-specific E03/E05 laws.

| Control family | Premise absent for the unchanged theta application |
| --- | --- |
| Euler-factor/translated sources | Unchanged canonical arithmetic arms, prime subtraction and completion. |
| Weighted squares, finite-prefix and finite-tail changes | Full unmodified square coefficients together with canonical reflection. |
| Finite-prime orbits | Full reflection and all source coefficients, despite agreement at selected primes. |
| Reflected super-Gaussian, smooth-shape and positive-primitive controls | Ordinary theta/zeta Dirichlet arithmetic in the complete field input. |
| Atomic, exact finite-profile and continuous extensions; heat counter-kernels | Full canonical profile, two-arm formula, correction and the exact coherent/residual laws. |
| RH-conditional normalized endpoint controls | Ordinary Dirichlet-series arithmetic; their conditional status is retained. |
| Fixed theta amplitude with variable readout | Literal cosine readout and physical Newman evolution. |
| Relaxed positive Green profiles | Identification with the exact integer zero measure and complete boundary field. |

Absence of these premises is not a proof that a control violates (8).
Mean convergence permits isolated collision witnesses. No control is
moved into our moving-time band, and no favorable pointwise exclusion
is claimed. Every negative theorem in the integrated manuscript retains
its class: quadratic allowance, phase-corrected diagnostic, fixed-P
separate residual payment or fixed-P tangent with constant-on-window
regulator. Adaptive P, spatial tangent variation and other nonlinear
signed estimates are outside those exclusions.

## 6. Outstanding work and continuation

The manuscript's final section gives the dependency order. The central
open task is still a complete every-center estimate of
(R_{\lfloor L_X^2\rfloor}(X,c)), or a genuinely nonlinear signed
value bound, on the original band and at the fixed defect margin.
Fixed-P means, power-mean convergence and the small normalized field
error do not supply it. No new applicable exceptional-center mechanism
was found in this consolidation and direct-corollary pass. The stop in
[Note18](18_GNP_RS_B05_E06_RETURN_AND_MODEL_CHANGE_20261111.md) remains
in force for the tested value-acquisition routes; this note supersedes
only its manuscript/averaged-results navigation, not its scientific stop.

Further independent tasks are: quantitative onsets; rate or all-c
extensions of the averaged results; the separate time-zero signed value;
and a source/claim audit beyond the present author's check. These are
not activated by being listed. No B06 or further proof request is issued.
If exceptional-center conceptual work is requested, the standing
recommendation remains **GPT-6 Astra, ultra**; **GPT-6.1 Sol, ultra**
is suitable for a fixed proof task after its new input and acceptance
test are specified. Recommendations do not identify this chat's model.

The current [sole register](../research-progress/01_GNP_RS_RESEARCH_PROGRESS_20261110.md)
owns this integration and corollary milestone as E07. The parent
time-zero, localized-correlation and collision-constraint tasks remain
separate. Chat0004 has its unique registration in this child's history
folder; current capture metadata and hashes belong to its registry.
