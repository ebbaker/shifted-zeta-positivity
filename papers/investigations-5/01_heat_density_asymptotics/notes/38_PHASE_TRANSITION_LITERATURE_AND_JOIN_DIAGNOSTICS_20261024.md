# Phase-transition literature and joining diagnostics

24 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. **gpt-6-astra (Codex), actual effort xhigh**, verified from session metadata. Chat 0012, thread 01a170f9-948a-7083-9c79-2eeccb5ab856.

**Status: literature-informed assessment, a conditional scaling calculation and proposed tests.** No new theta criticality theorem, numerical execution, CFT identification, RG fixed point, global join or regulator change. This follows the author's suggestions about Landau order parameters and divergent correlation observables. See [Review 21](../reviews/21_NOTES35_37_PROJECT_AND_JOIN_ASSESSMENT_20261024.md).

Read the [result index](../../../../result-summaries/README.md), [heat-flow cluster](../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md), [control screen](../../../../result-summaries/12_collision_controls_and_screening.md), and [avoid index](../../../../avoid/README.md), particularly [unverified imports](../../../../avoid/16_unchecked_imports_and_novelty_claims.md). The objective remains an approximation with paid errors and equations.

## The join and the existing crossover

The negative Gaussian, finite-source central and positive gamma-saddle/outer models approximate one canonical heat field in different regions. Joining them requires compatible potential, density, current and actual covariance. A time blend has a known heat residual; a spatial cutoff generally breaks holomorphy (Note 34 CJ28). Different useful formulas are not by themselves different physical phases.

[Note 27 GO33](27_COMPACT_TIME_GAMMA_OUTER_DENSITY_20261024.md) states, for fixed |y|<h,
    
    R(t,X,y)/log X -> 0                    for t<=64,
    R(t,X,y)/log X -> k_h(y)/(4*pi)         for t>64,

as X tends to infinity. At finite X the regulated observable is smooth. This limiting jump is created by the chosen regulator switch, with no discontinuity in H. The number 64 is a definition point, not an intrinsic critical time.

[Note 28 JT22–JT33](28_JOINT_OUTER_REGULATOR_TRANSFER_AND_SWITCH_LAYER_20261024.md) already identifies

    b=log(epsilon_g/A_X),   d=max(b,0)/omega,
    R_layer=omega/(2*pi) [k_h(y-d)+k_h(y+d)].

These regularized-density layers are not claimed to be nonreal zeros. The center t_c satisfies b(t_c,X)=0. Its leading shift from 64 is 64/log X, whereas its time width is of order 1/(X log X). The exact implicit center is required at the much finer width.

For t=t_c-128*tau/(pi*X*log X), the existing law is

    R/log X=[k_h(y-tau_+)+k_h(y+tau_+)]/(8*pi)+O(1/log X).

The unnormalized error is O(1), not the finite-core small absolute error. It cannot simply be differentiated to obtain current/time/covariance control. Note 31 supplies stronger outer evolution comparisons from fields; this coarse layer does not supersede them.

## What the literature can contribute

See the [reference record](../references/PHASE_TRANSITION_METHODS_20261024.md) for exact reading scope and links.

- **Finite-size scaling:** Fisher–Barber distinguish a critical-location shift from its rounding width. This is the closest methodological analogy to Note 28. X is a height parameter, not an established thermodynamic size; no physical critical exponent is imported.
- **Landau/Landau–Ginzburg:** an order parameter and symmetry organize an effective free energy. A polynomial ansatz would need coefficients and stationary states derived from our canonical data or a specified effective model. Merely fitting a double well to changing profiles supplies no such derivation.
- **RG:** Wilson explains scaling through transformations and their fixed points. One fixed spatial convolution is not an RG flow. A scale transformation, observables and controlled discarded terms must be supplied.
- **Anomalous dimensions and CFT:** these become usable after demonstrating appropriate correlation scaling and, for CFT, the stronger symmetry structure. Holomorphy of H alone is not a CFT. Logarithms in a regulator-dependent crossover do not establish an anomalous dimension.
- **Uniform asymptotics:** the DLMF coalescing-saddle methods offer canonical transition approximations when saddles actually merge. Equality of regulator and carrier amplitudes does not establish that premise. Airy/Scorer or higher canonical integrals require the relevant degeneracy and contour hypotheses. Stokes switching and saddle coalescence are also distinct mechanisms.

## Order parameter, correlations and response

A diagnostic of the known crossover is

    m_X(t)=4*pi*R(t,X,0)/(k_h(0)*log X),  X>1.

Its fixed-time limits are 0 and 1 by GO33. This normalization is for interpretation only; the physical target remains unnormalized R. Its dependence on the chosen regulator prevents calling it an established intrinsic Landau order parameter.

The author's correlation criterion provides a stronger test. In standard continuous critical phenomena, connected correlations develop long-range power-law behavior, correlation length diverges, and an integrated correlation/response can diverge. A two-point function need not diverge at fixed nonzero separation. Tong Sections 2.2 and 3.2 give the correlation/response/scaling framework; Gibbs fluctuation-response identities are not automatically identities for deterministic filtering.

Here first choose an observable O and an averaging operation. A possible finite-window object is

    C_X(s;t)=<O(t,X+u)O(t,X+u+s)>_W
             -<O(t,X+u)>_W <O(t,X+u+s)>_W,

with W and its width declared. This is empirical spatial covariance, not an assumed stationary equilibrium ensemble. Its integral in s is an integrated correlation; calling it susceptibility requires a specified perturbation and a proved response relation. Known carrier/amplitude scales must be accounted for before growth is interpreted as critical. Shrinking regularization can amplify local peaks without creating long-range correlations.

The current Q is a signed difference of local filtered gradient variances. It is not this separated-point correlation, and cancellations can conceal growth of its individual terms. Neither large Q nor small Q alone diagnoses correlation-length divergence.

The useful checks are a declared limiting parameter, an order parameter, separation-dependent connected correlations, a defined response, and dependence on regulator/filter choice. Failure to find equilibrium structure would restrict imported physical theorems; it would not exclude interesting deterministic scaling.

## Conditional check of switch-dependent powers

For an analytical comparison only, suppose another flat switch obeys

    beta(t0+Delta) ~ B exp(-a/Delta^p),
    beta'/beta ~ a*p*Delta^(-p-1),    a,B,p>0,

with uniform derivative control. Assume the same leading carrier balance log A_X=-pi X/8+O(log^2 X), omega~log X/4, and that the other time derivatives in b are lower order on the layer. Then b=0 implies beta(t_c)~pi/(4X), whence

    Delta_c ~ (a/log X)^(1/p),
    b_t(t_c,X) ~ -pi*p/(8*a^(1/p)) * X*(log X)^(1+1/p),
    omega/|b_t| ~ 2*a^(1/p)/(pi*p*X*(log X)^(1/p)).

The present p=1,a=64 recovers 128/(pi X log X). This is a conditional balance calculation, not a new uniform theta theorem. Its derivative hypotheses are separate, not obtained by differentiating an uncontrolled asymptotic. It illustrates why switch-dependent logarithmic powers must be distinguished from intrinsic critical exponents. Existing physical q and records remain unchanged.

## Bounded next analytical deliverable

**Analysis — Sol:** make a short crossover/correlation specification from Notes 27–28 and 31 using the unchanged source/regulator. Identify the scaled fields needed beyond R, state the time/current/covariance estimates needed for the equations, and give one precise connected-correlation and response definition. Compare its leading behavior with the known carrier/regulator crossover before claiming a new critical effect. Do not differentiate JT33's error or assume CFT/exponents without their premises.

No numerical sweep or new model is needed for this specification. Stop with a precise unpaid estimate if the existing methods do not suffice. A resistant uniform differentiated-layer estimate or spatial-compatibility problem is an Astra task. Note 37's independent frozen-point certification remains a Sol task.

This proposal excludes no collision control: generic filtering and scaling ideas permit changed-source and polynomial controls. The canonical theta information would have to supply a distinguishing quantitative premise. No RH or simplicity conclusion follows.
