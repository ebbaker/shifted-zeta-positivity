# Fixed compression and normalization: comparison of two different flows

30 October 2026, America/New_York. Prepared for Edward Baker with substantial LLM assistance. Actual recorded model **gpt-6-astra**, recorded reasoning effort **xhigh**. Investigation05 chat0042, *Clarify signed cross-production questions*.

**Status: elementary fixed-coefficient comparison derived here from the repository's common-kernel, gradient, and Fourier estimates; same-assistant derivation only. No independent review, theta-specific exclusion, changed live task, or numerical experiment.** The author's proposal is to consider a finite coefficient fixed throughout the auxiliary flow. This note separates freezing the PDE coefficient from maintaining the original energy constraint.

Follow the [result index](../../../../result-summaries/README.md), [flow cluster](../../../../result-summaries/16_hypercomplex_reductions_and_geometric_realizations.md), [control register](../../../../result-summaries/12_collision_controls_and_screening.md), and [avoid index](../../../../avoid/README.md), particularly [target reformulation](../../../../avoid/01_restating_the_target.md), [scope](../../../../avoid/07_scoped_exclusions_read_as_universal.md), and [circular inputs](../../../../avoid/14_convenience_hypotheses_and_circular_definitions.md).

## 1. Exact change of problem

Fix c>0 and keep the original drift

    v(X)=X+X/(1+|X|^2),  d=div v in [3,6],
    Dv >= kappa I,  kappa=7/8.

Let W_c solve

    partial_s W_c = Delta W_c + c div(v W_c),  W_c(0)=W0.

The scalar transition kernel for the bounded coefficient path alpha(s)=c is positive and conservative on every finite interval, as in [Note28](28_ENERGY_NORMALIZED_CONSERVATIVE_COLLISION_MAGNIFIER_20261028.md). The globally Lipschitz drift yields a global linear evolution for the prepared smooth data. Its signed vector mass m=int W_c is conserved. However,

    E_c'=-2G_c+c D_c,

and E_c is generally not constant. Setting c=2G_c(0)/D_c(0) only sets the initial derivative to zero. To preserve energy for all times one would additionally need 2G_c(s)/D_c(s)=c for every s. The original normalized-flow blow-up theorem uses E(s)=E0 and does not carry over after that condition is removed.

The immediate bound E_c'<=6c E_c rules out finite-time L2 blow-up. The next section gives a stronger whole-time statement, including decay at zero mass.

## 2. Fixed-coefficient convergence without a physical mass floor

Let

    mathcal V(X)=(|X|^2+log(1+|X|^2))/2,
    p_c(X)=exp(-c mathcal V(X))/Z(c),
    Z(c)=int exp(-c mathcal V).

Then int p_c=1 and grad p_c+c v p_c=0. The smooth radial stationary formula is already proved in [Note90, Section 5](90_CARRIER_FEEDBACK_DEFECT_AND_STATIONARY_CANDIDATE_R13_20261029.md).

Set f(s)=W_c(s)-m p_c, componentwise. It solves the fixed linear equation and has zero vector mass. Assume the prepared data have finite L1, H1 and first absolute moment, as in the inherited theta and Gaussian-control class. These properties hold for f(0); p_c has Gaussian decay. If f(0)=0 the conclusion is immediate. Otherwise put

    ell=||f(0)||_1>0,  P=int |X| |f(0,X)| dX,
    E=||f||_2^2,  G=||grad f||_2^2,  N=||Delta f||_2^2.

Positivity/conservation give ||f(s)||_1<=ell. The elementary Fourier/Nash inequality used in Notes67/76 gives

    G >= c_N E^(5/3) ell^(-4/3),
    c_N=(3/5)(6 pi^2)^(2/3).

Thus

    E' <= -2 c_N E^(5/3) ell^(-4/3) + 6c E,
    E <= Ebar := max{E(0), (3c/c_N)^(3/2) ell^2}.

Use the general drift bounds from Note28, rather than a new radial estimate:

    G' <= -2N+10c G+30c E,
    G^2 <= N E.

Consequently

    G' <= -2G^2/Ebar+10c G+30c Ebar,
    G <= Gbar := max{G(0), Ebar r_c},
    r_c=(5c+sqrt(25c^2+60c))/2.

All constants are finite for each fixed finite c. No physical vector-mass lower bound is used.

The synchronous contraction argument of Note28, with B(s)=cs, and int f=0 give

    |hat f(s,xi)| <= |xi| P exp(-kappa c s).

Splitting Plancherel at any R>0 gives

    E(s) <= P^2 exp(-2 kappa c s) R^5/(10 pi^2) + Gbar/R^2.

Choose R=exp(2 kappa c s/7). Since 4 kappa/7=1/2, this proves

    ||W_c(s)-m p_c||_2^2
    <= [P^2/(10 pi^2)+Gbar] exp(-c s/2).

The exponent and constants are sufficient, not optimal. The finite-interval integrations and Fourier bounds use the inherited smooth weighted prepared class. Taking arbitrary finite intervals yields the stated whole-time estimate.

In particular, at m=0 the fixed-coefficient solution tends to zero in L2, instead of blowing up. This is a scoped negative answer to transferring the original normalized-flow divergence to the frozen equation. It is not a theorem against all uses of fixed-coefficient comparison.

## 3. The stationary energy-matching interpretation

For every c>0 the stationary projection is m p_c. Its squared norm is

    ||m p_c||_2^2=mu^2 Z(2c)/Z(c)^2,  mu=|m|.

Thus matching the original positive energy requires

    mu^2 Z(2c)/Z(c)^2=E0.

Note90 proves Z(2c)/Z(c)^2 is continuous, strictly increasing from zero to infinity. For mu>0 there is a unique finite matching c_star. For mu=0 there is no such c, because every stationary projection is zero. Note90's bracket reads

    pi(E0/mu^2)^(2/3) <= c_star <= 8pi(E0/mu^2)^(2/3).

This matches the previously identified candidate lambda_star; [Note98](98_RADIAL_LOG_SLOPE_ATTRACTION_B02_R15_20261029.md) subsequently proves attraction of the actual normalized orbit under the accepted positive-mass inputs. Matching a stationary energy does not assert constant energy along the transient frozen-coefficient orbit or alpha(s)=c_star from the beginning.

Classification: existence of this compatible nonzero stationary state is equivalent to mu>0 in the stated class, so it is a reformulation, not independent evidence for noncollision. A new source argument could still prove a useful independent nondecay or overlap estimate, but none is supplied by merely choosing c.

## 4. Controls and the exact failed premise

The prepared weighted-square source at its certified high-frequency event is an admitted zero-mass case in [R16, Section 5](101_MASS_FREE_FEEDBACK_DEFECT_AND_SLOPE_CLOSURE_TEST_R16_20261029.md). It has the regularity and moment premises needed above, so its frozen-coefficient flow is globally regular and decays. The Gaussian-polynomial collision control also belongs to the prepared finite-moment class used in Note28 and has the same conclusion.

These controls do not fail the premise 'a finite fixed-coefficient flow exists and is regular'; it holds for them. They fail 'this fixed-coefficient solution retains a positive constant energy', by the decay just derived. Therefore fixed-coefficient existence/regularity is not a collision discriminator. Other registered families fall under the comparison only when their prepared-class hypotheses are established; no new event, common mark, tail identity, or class extension is asserted. No source-specific separating premise is proposed, so no claim is made that coefficient choice screens the broader control register.

## 5. Relation to the DMC analogy

The exact ground-state eigenvalue of a fixed quantum Hamiltonian is fixed; the reference/trial energy used for population control in practical DMC is commonly updated ([QMCPACK documentation](https://qmcpack.readthedocs.io/en/v4.4.0/methods.html)). An additive scalar energy shift moves eigenvalues without changing eigenfunctions. In the frozen conservative operator L_c=Delta+c div(v dot), changing c changes the stationary spatial profile, while the stationary eigenvalue is zero for every c. The coefficient of that stationary profile remains the conserved vector mass m. This explains why changing c cannot restore a stationary component whose mass is zero.

Three distinct targets must stay separate: prescribing c in a new linear equation; proving the original alpha(s) stays below a finite c; and proving the original alpha(s) is identically c. The second is the existing sufficient bound sought; the third is stronger and is not implied by a stationary candidate or its eventual attraction.
