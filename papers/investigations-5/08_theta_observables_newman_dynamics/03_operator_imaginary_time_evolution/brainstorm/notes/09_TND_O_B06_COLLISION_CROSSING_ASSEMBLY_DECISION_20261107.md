# B06 r1: cross collisions by a uniform moment bound

6 November 2026, America/New_York (7 November UTC). Prepared for **Edward Baker** with substantial OpenAI Codex assistance. Lead tool-selected configuration: **gpt-6-astra, ultra**; no independent backend verification.

**Decision:** if E10 proves the stated derivative bound on simple intervals, extend the same local moment across all multiple-root times by continuity and finite-event assembly. This is one extension architecture, not an assumption of globally simple zeros. Its contract will be frozen after the actual E10 result. No uniform lower bound on root gaps or on distances between events is required.

## Fixed intended theorem

For a fixed nonnegative chi in C_c^2([-1,1]), X>=10 and 0<R<=1, the complete multiplicity-counted canonical moment

    Q_{X,R}(lambda)=sum_j chi((Re z_j(lambda)-X)/R)(Im z_j(lambda))^2

is to be Lipschitz on [0,1/2], with constant C_chi R^{-2}log^2(2+X), uniformly for the full stated X,R family. Its derivative agrees almost everywhere with the E08 paired interaction identity; its distributional derivative has no atom at a collision. This is fixed derivative order, unbounded height and full zero-index control. It makes no assertion of infinite derivative-order regularity.

The proof route is: root-multiset continuity on compact boxes; local Hermite splitting from the heat equation at every multiple zero; finite many collision times in each fixed compact space/time box; E10's uniform derivative bound on the complementary intervals; continuity at their endpoints. The qualitative number and separation of collision events may depend on X,R. They do not enter the Lipschitz constant when integrating the same derivative bound across finitely many intervals. A claimed uniform radius in the Hermite normal form is unnecessary and would be unjustified by the imported local theorem.

## Local kink formula to check in the same package

For a single multiplicity-m cluster at z0=x0+i y0 at lambda0, let f(x,y)=a(x)y^2 and q(lambda) be the sum of f over that local cluster. The heat normal form uses the probabilists' Hermite roots h_k,

    z_k(lambda0+tau)=z0+sqrt(2 tau) h_k+O(tau),
    sum h_k=0,  sum h_k^2=m(m-1).

The analytic centroid supplies one common first-derivative term on both sides. The candidate jump is

    q'_+(lambda0)-q'_-(lambda0)
      =m(m-1) Delta f(z0)
      =m(m-1)[a''(x0)y0^2+2a(x0)].

The two one-sided derivatives and the sum over simultaneous clusters must be justified. At a real event, the gradient of f is zero and this reduces to q'_-=−2m(m−1)a(x0), q'_+=0. In reverse heat time a double event has slope +4a, agreeing with the polynomial pair. The constants in the O(tau) root expansion are local and not asserted uniform; the eventual Lipschitz constant comes from E10 instead.

## Consumer and scope

The output would be a collision-stable canonical moment calculus, with its actual width loss, and an exact local kink law. The sign and magnitude of the spatial flux still require canonical information beyond coarse counts. A local production law shared by polynomial or smooth-source collision controls is not an exclusion. E12 must return this boundary explicitly; B05 may conclude that a collision-time consumer is not ready because no independently small endpoint/flux bound has been acquired.

[Polymath arXiv:1904.12438v2](https://arxiv.org/html/1904.12438v2), Proposition 3.1(ii), supplies the local Hermite expansion with event-dependent constants; the present assembly must not promote those constants into unproved uniformity. The source is complete and the zero set has multiplicities. The time-zero endpoint is included by canonical local analyticity and the E10 endpoint passage, not by assuming RH.

Mandatory context: [result index](../../../../../../result-summaries/README.md), [local geometry](../../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md), [controls](../../../../../../result-summaries/12_collision_controls_and_screening.md), [patterns index](../../../../../../avoid/README.md), [scope discipline](../../../../../../avoid/07_scoped_exclusions_read_as_universal.md), [B03 decision07](07_TND_O_B03_R4_LOCALIZED_TRANSVERSE_DECISION_20261107.md), and [B04 decision08](08_TND_O_B04_SAFE_LINE_CANONICAL_ESTIMATE_DECISION_20261107.md).
