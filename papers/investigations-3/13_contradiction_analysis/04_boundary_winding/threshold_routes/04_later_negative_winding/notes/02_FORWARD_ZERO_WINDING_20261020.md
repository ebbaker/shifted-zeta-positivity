# Zero winding on a quantitative forward neighborhood

20 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Authoring model **gpt-6-astra (Codex)**;
recorded parent-session reasoning effort **ultra**, inherited by this
research subagent.

**Status: proved consequence of [BW-05 Note 02][main]; [separate
same-model internal review][review].** No specialist review. This closes the local immediate-future attempt
within an explicit paid neighborhood, not the full later negative-
winding route. See the [result summaries][results], [controls][controls],
and [patterns to avoid][avoid], especially [scope][scope].

At an exact ordinary double event (T,a), let h=Hxx(T,a)!=0 and choose
r>0 with complete real derivative envelopes satisfying
M3r/|h|<=1/16 and M4r^2/|h|<=1/4. The common theorem proves

\[
 \mathcal L(T+s,a+y)\ge {657\over1024}h^2(s+y^2/2)>0
 \quad(0<s\le r^2/4,\ |y|\le r).                  \tag{1}
\]

Let D be any bounded Jordan domain with closure contained in this
forward rectangle. Compactness gives inf_Dbar(t-T)>0. If the physical
jet J=(H,Hx) vanished anywhere in the closure, L would vanish there,
contrary to (1). Thus J is nonzero *throughout the entire closed domain*.
The map J/|J| from the boundary to the circle extends continuously to
the Jordan disk. Its degree is therefore zero:

\[
 \boxed{W(D)=0.}                                             \tag{2}
\]

No index sum is needed, and no unproved sign of a partial face integral
is used. With physical orientation dt wedge dx, (2) is zero; reversing
orientation also gives zero. Constant multiplication by a nonzero real
number multiplies both jet components and preserves it.

This proof provides a complete neighborhood statement instead of
sampling its boundary. Consequently corners and wall locations are
immaterial as long as the entire closed Jordan region is contained
in the proved rectangle. A domain that touches (T,a), has unvalidated
time separation, or extends beyond the rectangle is not covered.
Boundary nonvanishing alone would not imply (2); the interior extension
is the essential extra conclusion here.

All polynomial and source-family controls are screened in the
[common note and receipt][main]. Their shared local heat geometry
explains why this theorem supplies no theta-only contradiction.
The missing step remains an arithmetic implication forcing a later
physical region of negative winding beyond this certified local
exclusion. The [initial route target][initial] remains open.

[main]: ../../05_later_laguerre_violation/notes/02_QUANTITATIVE_FORWARD_NEIGHBORHOOD_EXCLUSION_20261020.md
[initial]: 01_INITIAL_RESEARCH_NOTE_20261019.md
[results]: ../../../../../../../result-summaries/README.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../../avoid/README.md
[scope]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md

[review]: ../../05_later_laguerre_violation/reviews/01_FORWARD_NEIGHBORHOOD_REVIEW_20261020.md
