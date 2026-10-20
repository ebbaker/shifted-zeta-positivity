# A paid forward rectangle contains no second real collision

20 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Authoring model **gpt-6-astra (Codex)**;
recorded parent-session reasoning effort **ultra**, inherited by this
research subagent.

**Status: proved consequence of [BW-05 Note 02][main]; [separate
same-model internal review][review].** No specialist review. This is a quantified local obstruction, not a new
theta-specific mechanism forcing a second event. See the [result
summaries][results], [controls][controls], and [patterns to avoid][avoid],
particularly [scope][scope].

Freeze the unchanged heat flow and exact double event with h=Hxx(T,a)!=0.
Suppose its complete M3,M4 derivative envelopes on the forward rectangle
give alpha=M3r/|h|<=1/16 and beta=M4r^2/|h|<=1/4. The common proof
establishes for 0<s<=r^2/4 and |y|<=r

\[
 H_x(T+s,a+y)^2-H(T+s,a+y)H_{xx}(T+s,a+y)
 \ge {657\over1024}h^2(s+y^2/2)>0.               \tag{1}
\]

If H=0 at one of these real points, (1) gives

\[
 |H_x|\ge {\sqrt{657}\over32}|h|\sqrt{s+y^2/2}
          \ge {\sqrt{657}\over32}|h|\sqrt{s}.      \tag{2}
\]

Every real zero there is simple. In particular no other event of any
multiplicity occurs in that forward rectangle. This conclusion needs
only real derivative envelopes; complete complex envelopes give in
addition the [exact two-zero count][complex] and the two real root
corridors. The theorem concerns an initial event of exact multiplicity
two; its exclusion of later higher multiplicity does not extend the
initial-event hypothesis to higher multiplicity.

For a proposed later witness region whose uncertainty lies entirely
in this rectangle and whose lower time separation is positive, an
existence proof must be incompatible with (1). An interval box that
merely contains zero in both component ranges does not establish a
counterexample. The lower bound in (2) tends to zero as s decreases
to zero, as required by the original double event; no uniform bound
through T is asserted.

The [own-source controls and exact receipt][main] show compatibility
with the genuine positive-threshold quartic and applicability even to
a mixed-zero quartic with nonreal zeros elsewhere. Thus the missing
premise for a future-event contradiction remains a signed consequence
of the unchanged complete theta arithmetic that forces a common zero
outside this local exclusion, or contradicts the original event.
The [route's global later-event target][initial] remains open.

[main]: ../../05_later_laguerre_violation/notes/02_QUANTITATIVE_FORWARD_NEIGHBORHOOD_EXCLUSION_20261020.md
[complex]: ../../02_later_nonreal_zeros/notes/02_COMPLETE_DISK_EXCLUSION_20261020.md
[initial]: 01_INITIAL_RESEARCH_NOTE_20261019.md
[results]: ../../../../../../../result-summaries/README.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../../avoid/README.md
[scope]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md

[review]: ../../05_later_laguerre_violation/reviews/01_FORWARD_NEIGHBORHOOD_REVIEW_20261020.md
