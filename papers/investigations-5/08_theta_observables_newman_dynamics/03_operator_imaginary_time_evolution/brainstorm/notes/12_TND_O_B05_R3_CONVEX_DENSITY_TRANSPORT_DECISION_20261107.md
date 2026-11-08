# B05 r3: convex broad-window transport and uniform off-axis density

6 November 2026 America/New_York (7 November UTC). Prepared for **Edward Baker** with substantial OpenAI Codex assistance. Lead tool-selected **gpt-6-astra, ultra**. This records configuration, not independently verified backend identity.

**Pre-dispatch revision:** request25 r1 was frozen but never dispatched. Preserve it as an unexecuted narrower target. The same broad-window mechanism now supports a stronger fixed consumer, so E11 r2 below replaces it before execution. Decision11's p=1 theorem remains a corollary. The root coordinator independently identified this convex-test extension; that is an internal same-premise contribution, not specialist review.

For the fixed broad a_T and cluster C_T of Decision11, take any even convex g in C²([-1,1]), g(0)=0, and put

    Q_{T,g}(lambda)=sum_j a_T(x_j(lambda)) g(y_j(lambda)).

The target general transport inequality is

    Q_{T,g}(lambda) <= Q_{T,g}(0)+Cχ ||g||∞ lambda log³T,           (C)

uniformT>=8,0<=lambda<=1/2, with Cχ independent of g,g',g''. This is a one-sided inequality: large nonnegative curvature in y is discarded, not estimated in absolute value. At each fixed T,g, compact-box regularity/finite-event assembly justifies integration; no constant depending on g's derivatives enters (C).

The exact kernel for f=a_T(x)g(y) is integral [a_T g'' e²−a_T'' g d²]/(d²+e²). Since g''>=0 and g>=0, the adverse local term costs ||a_T''|| ||g||∞ N(C_T)². The real exterior field remains O(log²T), so horizontal flux costs ||g||∞ log³T. Even convex g has g'(y) with the sign of y. The separated exterior conjugate calculation in Decision11 therefore makes the vertical Newman-time contribution nonpositive. Full paired tails and collision assembly remain required.

Fix one canonical density exponent c in(0,1), put a=c/2, and choose **one fixed b in(0,a)**. Apply(C) to

    g_T(y)=cosh(b logT y)−1.

Its complete canonical initial tail is bounded by C0 TlogT exp(−a v logT). Direct layer cake gives

    Q_{T,g_T}(0) <= C0 TlogT * b²/(a²−b²).

Also ||g_T||∞<=T^b and T^b log³T<=C_b TlogT forT>=8, since b<1. Thus Q_{T,g_T}(lambda)<=C_b TlogT uniformly in the full time interval. For b v logT>=1, cosh(bvlogT)−1 is bounded below by an absolute positive constant times exp(bvlogT); for smaller values the ordinary local count fills the gap. The required canonical conclusion is

    #{j:T<=x_j(lambda)<=2T, |y_j(lambda)|>v}
        <= C_b TlogT exp(−b v logT),                            (D)

simultaneously for everyT>=8,0<=lambda<=1/2,0<v<1, with multiplicities. Since c may be chosen in(2b,1), any fixed b in(0,1/2) is permitted, with constants depending on b and the chosen c. This is a quantitative propagated density bound, not a realness or simplicity theorem.

Two fixed corollaries belong to the same package: layer cake gives the full-family dyadic transverse mass O(T/logT), and combining(D) with the uniform local count exactly as in Note20 gives a local averaged bound C_b R A_b^p(2p)!/log^pT for all integerp>=1, 0<R<=1, **uniform also in lambda**. Pay the slightly enlarged center band by a bounded dyadic cover, with the same b and explicit constants. The one-pair allowance obstruction remains; do not mistake averaged exponential rarity for absence of isolated zeros.

No novelty claim is made. Root has discovered a recent unreviewed weighted-zero-moment preprint and is triaging its overlap separately; it is not a theorem premise. The proof is to rely on the checked Polymath and Maples–Rodgers inputs and the self-contained local kernel/assembly results. Attribution will be updated from the actual checked passages rather than inferred from an abstract.

One bounded E11 r2 theorem/consumer package and one correction pass. If a clause fails, retain the narrower paid result and name the exact failure. Do not add new kernels or numerical tests. [Result index](../../../../../../result-summaries/README.md), [controls](../../../../../../result-summaries/12_collision_controls_and_screening.md), [patterns](../../../../../../avoid/README.md), [classification](../../../../../../avoid/01_restating_the_target.md), and [scope rule](../../../../../../avoid/07_scoped_exclusions_read_as_universal.md) apply. Generic controls are not asserted to satisfy the imported canonical density input. The endpoint density and flux costs are now acquired for this mean-statistical consumer; single-event exclusion remains unpaid.
