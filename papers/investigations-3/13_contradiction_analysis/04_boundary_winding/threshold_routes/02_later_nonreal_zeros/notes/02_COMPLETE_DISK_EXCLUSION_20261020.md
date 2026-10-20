# Complete disk exclusion for the immediate forward double-event pair

20 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Authoring model **gpt-6-astra (Codex)**;
recorded parent-session reasoning effort **ultra**, inherited by this
research subagent.

**Status: proved in-note; [separate same-model internal review][review].**
No specialist review. This gives an
explicit event-dependent disk with no later nonreal zeros for a short
positive time interval. It is a scoped local obstruction to BW-02,
not the requested theta-specific later-witness implication. Read the
[result summaries][results] and [patterns to avoid][avoid], especially
[controls][controls] and [scope][scope]. The full common contract and
control record are in [BW-05 Note 02][main].

Let h=Hzz(T,a)!=0, sigma=r^2/4 and M3,M4,alpha,beta have the meanings
in the common note. Use complete derivative bounds on the *complex disk*
|z-a|<=r, for every T<=t<=T+sigma. Real-axis bounds alone do not supply
this statement. The common derivative remainder is

\[
 H(T+s,a+w)=h(w^2/2-s)+R_0,\qquad
 |R_0|\le M_3(|w|^3/6+s|w|)+M_4s^2/2.             \tag{1}
\]

For every 0<=s<=r^2/4, on the entire circle |w|=r,

\[
 |h(w^2/2-s)|\ge |h|(r^2/2-s)\ge |h|r^2/4,
\]

while (1) gives

\[
 |R_0|\le |h|r^2\left({5\alpha\over12}+{\beta\over32}\right).
                                                                    \tag{2}
\]

Consequently the strict condition

\[
 C(\alpha,\beta):={5\alpha\over12}+{\beta\over32}<1/4              \tag{3}
\]

gives, by the nonvanishing straight-line homotopy on the full circle
and the holomorphic argument principle, exactly two zeros counting
multiplicity in |z-a|<r. The comparison polynomial's roots have modulus
sqrt(2s)<=r/sqrt(2), so no root lies on that circle. This count includes
s=0, when the double event already accounts for both zeros.

For s>0, evaluate at w=0 using the sharper center part of (1):

\[
 |H(T+s,a)+hs|\le M_4s^2/2.
\]

Condition (3), with alpha,beta>=0, already implies beta<8, hence
M4s/(2|h|)<=beta/8<1. Therefore H(T+s,a)/h<0.
At w=+r and -r, the same strict boundary comparison gives
H(T+s,a+w)/h>0. The intermediate value theorem gives one real zero in
each of (-r,0) and (0,r). Since the total multiplicity in the complex
disk is two, these are the only zeros there and both are simple.

In particular the convenient common contract

\[
 \alpha\le1/16,\quad\beta\le1/4
\]

gives C<=13/384 and leaves the explicit full-contour margin

\[
 |H(T+s,a+w)|\ge (83/384)|h|r^2\quad(|w|=r).                    \tag{4}
\]

Every wholly off-real closed contour with its interior contained in
this disk consequently encloses zero zeros at these times. The result
does not prohibit nonreal zeros outside the disk: the mixed-zero
quartic in the common control record has exactly such zeros. No global
all-real threshold premise is used.

Under the common smallness contract, the roots have a quantitative
parabolic location as well. At either real root y, the common bound
|R0|<=|h|(alpha+beta/8)(s+y^2/2) gives, since
alpha+beta/8<=3/32,

\[
 {58\over35}s\le y^2\le {70\over29}s.                          \tag{5}
\]

Thus the later pair is separated from the center and stays within
explicit moving real corridors; no nonreal excursion can be hidden
between sampled heights. Equations (2)-(5) cover the whole relevant
circles or intervals, not just nodes.

The exact polynomial controls and all family distinctions are recorded
once in the [common note][main] and its [receipt][receipt]. This bounded
task is complete. A same-function theta arithmetic relation that forces
a nonreal zero beyond the certified neighborhood remains unproved.
The [initial route target][initial] is still open.

[main]: ../../05_later_laguerre_violation/notes/02_QUANTITATIVE_FORWARD_NEIGHBORHOOD_EXCLUSION_20261020.md
[receipt]: ../../05_later_laguerre_violation/numerics/FORWARD_NEIGHBORHOOD_CONTROLS_20261020.json
[initial]: 01_INITIAL_RESEARCH_NOTE_20261019.md
[results]: ../../../../../../../result-summaries/README.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../../avoid/README.md
[scope]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md

[review]: ../../05_later_laguerre_violation/reviews/01_FORWARD_NEIGHBORHOOD_REVIEW_20261020.md
