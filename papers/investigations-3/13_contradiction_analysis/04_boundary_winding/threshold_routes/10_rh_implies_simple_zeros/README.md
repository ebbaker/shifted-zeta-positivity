# RH implies simple zeros

20 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. **gpt-6-astra (Codex), reasoning effort ultra**,
verified from recorded turn metadata. Separate same-model internal review;
no specialist review.

**Route BW-10. Goal: prove that RH implies simplicity of every nontrivial
zero of the Riemann zeta function.** This is a substantive open conditional
target in the primary literature checked. The present work establishes
neither that implication nor priority for a new method.

Start with the [opening brainstorm](brainstorm/01_RH_IMPLIES_SIMPLICITY_20261020.md),
the [research program](research-overview/01_RH_TO_SIMPLICITY_PROGRAM_20261020.md)
and [progress register](research-progress/01_RH_TO_SIMPLICITY_PROGRESS_20261020.md).
The eleven-page [analytic consolidation draft](manuscript/main.tex)
([PDF](manuscript/main.pdf)) presents the principal estimates, the missing
arithmetic bound and their relation to BW09. The complete upper estimates
retain multiplicity costs; RH implies simplicity remains unproved.

21 October integration — **gpt-6-astra, actual effort max**: Sections 5–7
now include Notes 17–18's complete normalized heat limit, sharp arithmetic
repair, exact example, and fixed-time completion obstructions. The
[cap-motion and higher-dimensional-contour brainstorm](brainstorm/03_HEAT_ROOT_MOTION_AND_HIGHER_DIMENSIONAL_CONTOURS_20261021.md)
records the author's proposed directions and the selected-root length
comparison. No new simplicity or cap-surplus estimate is claimed.

The [heat-motion and signed-contour program](research-overview/02_HEAT_ROOT_MOTION_AND_SIGNED_CONTOURS_PROGRAM_20261021.md)
and [matching progress note](research-progress/02_HEAT_ROOT_MOTION_AND_SIGNED_CONTOURS_PROGRESS_20261021.md)
organize that continuation as HMC-00–07, with analytic completion
requirements and numerics reserved for supporting evidence.

21 October first analytic round — **gpt-6-astra, actual effort max**:
[Note 19](notes/19_COMPLETE_ROOT_MOTION_AND_FINITE_TIME_BOUNDS_20261021.md)
proves explicit complete-root tails, both velocity remainders, a finite
enclosure and a mirror-compression width bound.
[Note 20](notes/20_DIFFERENTIATED_SADDLE_AND_EVENTUAL_GAP_SHRINKAGE_20261021.md)
proves differentiated fixed-label asymptotics and eventual gap shrinkage,
with finite computable error conditions. The [review](reviews/19_ROOT_MOTION_AND_DIFFERENTIATED_SADDLE_REVIEW_20261021.md)
is a same-assistant self-review. These motion estimates remain compatible
with multiple endpoints; the arithmetic gap remains.

21 October moving-tube continuation — **gpt-6-astra, actual effort max**:
[Note 21](notes/21_MOVING_SIGNED_TUBES_AND_PHYSICAL_TRACE_20261021.md) completes signed transport and a paid
physical trace on bounded product tubes. Its exact planar reduction gives
`pi<=I_eta<=pi+g eta^2 D0/6` under RH, with no additional signed gain.
The [self-review](reviews/20_MOVING_TUBE_AND_TRACE_REVIEW_20261021.md) retains the compact-time
energy-floor dependence and the quadratic endpoint control. HMC-05's
separating theta estimate remains open.

21 October HMC-05 continuation — **gpt-6-astra, actual effort max**:
[Note 22](notes/22_HEAT_SCALE_SIGNED_TRACE_AND_UNIVERSAL_PROFILE_20261021.md) proves an explicit complete-source
heat-scale trace error of order `sqrt(t) log(1/t)`. At a hypothetical
double endpoint the tube observation tends to `pi(1+r^2)` for
`eta=r sqrt(2t)`; the all-multiplicity outer profile is also explicit.
Matching controls share these leading data, so this candidate does not
separate theta. [Self-review 21](reviews/21_HEAT_SCALE_TRACE_AND_CONTROL_REVIEW_20261021.md) records the
fixed-event scope and the local version for controls without an all-real
heat slice. HMC-05 remains open.

The [opening review](reviews/01_RH_TO_SIMPLICITY_OPENING_REVIEW_20261020.md)
checks the conditional logic, all-multiplicity cap baseline and controls.

The contradiction begins by assuming RH and a multiple real zero at heat
time zero. RH forbids every positive-time multiple zero, so an independently
forced later event would give a contradiction. For outer walls from an
\(m\)-fold event the ordinary cap decrease is \((m-1)\pi\); a strict surplus
must exceed that baseline.

The opening analysis transfers this accounting and identifies an exact
time-zero arithmetic control. A modified source can be all-real at zero,
multiple there, and simple at every later time. A successful proof must
use a quantitative consequence of the unchanged zeta arithmetic that this
control fails. **That estimate remains unproved.** The [research notes](notes/README.md) prove finite wall continuation under RH, identify exact arithmetic control responses, and quantify scoped failures of the tested estimators. Note 03 also rejects a finite Euler-polynomial control class by an explicit logarithmic coefficient witness. That rejection does not transfer to an original multiple zero. Note 04 quantifies the cost of subtracting certified neighboring zeros and proves a uniform bound on what the tested absolute-value derivative strategy can achieve. Note 05 constructs an RH-conditional positive-source control arbitrarily close to theta, preserving its leading tail and pole residue one while adding double zeros; ordinary Dirichlet-series arithmetic fails explicitly. Note 06 quantifies the resolution cost of a full-window second moment, the additive-one limit of universal phase positivity and the Möbius-energy cost of an event. None supplies an original theta simplicity exclusion. The [reviews](reviews/README.md) record these limits.

This track is distinct from [BW-09](../09_expanding_contour_later_collision/README.md),
whose manuscript supplies shared contour and Gaussian identities and whose
program studies hypothetical positive-threshold events. Neither track
changes the other's task statuses. The unconditional simplicity alternative
is retained in the brainstorm but is not the selected primary goal.

Further analysis belongs in `brainstorm/` or `notes/`, computations in
`numerics/`, and assessments in `reviews/`. The canonical manuscript is saved in `manuscript/`; no new numerical sign campaign was started. A frozen
[exact algebra replay](numerics/README.md) checks finite constants only.

[Chat history](chat-histories/README.md) preserves conversation 0003 at its
sole new home; the [relocation receipt](CHAT_HISTORY_RELOCATION_20261020.json)
records the authorized move. The number was preserved, not reset.
Conversation 0004 records the analytical continuations at the same home.
Conversation 0005 records the joint manuscript review and its discussion.
Conversation 0006 records the heat-motion, moving-tube and first HMC-05
analytic rounds.

Read the [result index](../../../../../../result-summaries/README.md),
[local heat-flow geometry](../../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md),
[collision controls](../../../../../../result-summaries/12_collision_controls_and_screening.md)
and [patterns to avoid](../../../../../../avoid/README.md).
[Threshold-route index](../README.md).
