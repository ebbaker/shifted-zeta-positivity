# Internal review of the quantitative forward-neighborhood obstruction

20 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Reviewing model **gpt-6-astra (Codex)**,
actual effort **ultra**. The parent reviewed work produced by a separate
same-model agent; this is not independent specialist review.

**Assessment: the four scoped local conclusions are supported.** The
[common proof][main] gives a quantitative positive Laguerre margin for
every moving real point in a forward rectangle after an exact double
event. The [complex-disk proof][complex] counts precisely two real simple
zeros there. The [collision][collision] and [winding][winding] consumers
follow with the stated domain and time restrictions.

The parent checked the remainders directly. Expansion in time after
spatial Taylor division needs only complete third/fourth derivatives;
no unlisted fifth derivative is taken. Expanding Hx²-HHxx before paying
errors yields exactly the displayed K(α,β). At α<=1/16, β<=1/4,
K<=367/1024, giving the lower factor 657/1024. The complex full-circle
error is at most 13/384 of |h|r² against a leading margin 1/4, leaving
83/384. Real signs at the center and endpoints and the total complex
count prove the two roots are real and simple. Their squared-distance
interval [58s/35,70s/29] follows from the same pointwise remainder.

The source envelope includes cosh u, which is needed on a complex disk.
Real-axis moments alone are not used for the complex zero count.
The explicit radius depends on the unknown event curvature and source
moments; it is an analytic conditional radius, not a numerical theta
certificate. The winding-zero conclusion uses nonvanishing throughout
the entire enclosed Jordan domain, and not merely on its boundary.

The parent replayed the [exact checker][checker] successfully. It includes
both signs of the quadratic and genuine threshold quartic, a radius
where the sufficient scalar payment fails, and a mixed-zero quartic
with nonreal zeros outside the proved disk. It rejects h=0 and the
unseparated time cases. The [receipt][record] records only those finite
controls and exact constants; none is assigned theta source data.

The useful extension is from a same-point infinitesimal sign to a full
explicit neighborhood. Its scope remains generic local double-event
geometry. It does not produce the nonlocal arithmetic implication
requested by the later-witness routes, prove all-realness outside the
disk, cover an initial higher-order event, or give a uniform radius.
The four route targets remain open. This is consistent with [scope
discipline][scope] and [control screening][controls].

[main]: ../notes/02_QUANTITATIVE_FORWARD_NEIGHBORHOOD_EXCLUSION_20261020.md
[complex]: ../../02_later_nonreal_zeros/notes/02_COMPLETE_DISK_EXCLUSION_20261020.md
[collision]: ../../03_later_real_collisions/notes/02_FORWARD_COLLISION_EXCLUSION_20261020.md
[winding]: ../../04_later_negative_winding/notes/02_FORWARD_ZERO_WINDING_20261020.md
[checker]: ../numerics/check_forward_neighborhood_controls.py
[record]: ../numerics/FORWARD_NEIGHBORHOOD_CONTROLS_20261020.json
[scope]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
