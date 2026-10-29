# CTF-B02 R8: diffusion variance self-assessment

29 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra / actual recorded effort max**,
Investigation05 **chat0028**. This is checking by the proof's own assistant,
with no subagents, specialist review or formal verification. It is not the
next E08 assessment.

**Verdict: the bounded proof in [Note59][note] passes these internal checks.**
Its initial-data bound for B is finite on the closed old horizon
S_tar=L(g0); the explicit new guaranteed lifespan is strictly larger.
There is no claim that either horizon reaches a collision deadline.

| Obligation | Check and scope |
| --- | --- |
| Genuine positive gap | H2 equals N by whole-space Plancherel. The normalized gap nu0=N0/E0-g0² is the variance of spatial squared frequency. A nonzero L2 Fourier density cannot live on a single sphere. This uses no physical mass margin; zero-mass controls also pass. |
| Complete initial costs | The full theta source and Gaussian preparation give H0 through H3 finite. The vector L1 carrier M0+M2 and Gaussian factors 1,3/4,15/16,105/64 pay the optional S3 upper bound277/64. Numerical gap size and horizon have not been acquired. |
| Drift derivatives | The singleton/pair derivative expansion gives F0,...,F4=1,2,12,96,1056. Product and trace bounds give v constants6,20,168,1824 and d constants40,336,3648. These are whole-space Frobenius bounds. |
| H3 propagation | The spatial Leibniz expansion has exactly binomial multiplicities; all remainder orders are at most3. The integrated leading coefficient is d, not2d. Summing gives C3=6+12(46)+8(356)+2(3816)=11038. No order-four initial budget is consumed. |
| Noncircular persistence | h0 is strictly inside the old proved interval; its old bound gives B<=log2/C3. Thus the normalized total derivative energy is <=K=2S3 there. The complete N' formula gives abs(n')<=2K+220K², and abs(g')<=22K+(20/3)K². Consequently abs(nu')<=M=2K+264K²+(40/3)K³ and nu>=nu0/2 on [0,h]. |
| Restart and endpoint | The signed diffusion equation gives g'<=ag²+bg-2nu. On [0,h], y-g>=nu0 s. The cap h<=g0/(2nu0) keeps g1 positive. Restarting the old comparison gives L_new=h+L(g1)>L(g0); delta1(L(g0)-h)=nu0 h/yh=eta>0 proves the closed-horizon B bound. Bounded G justifies continuation before using that endpoint. |
| Complete downstream payment | Substituting B* into Note47 gives the finite weighted functional bound. The exact residual, full source/cutoff commutators, true second jet, combined sphere cancellation and inner ball remain. The separate inequalities are not added to double-count diffusion. |
| Matched information and controls | All admitted nonzero prepared radial fields share the mechanism. The theta low-mark direct margin already gives all finite horizons via Note29; this proof does not use it. No arithmetic separation, new physical domain, uniform restart gain or global iteration theorem is obtained. |

The finite [constant check][check] reproduces combinatorial constants and
checks three illustrative endpoint identities with exact fractions. These
examples are arithmetic sanity checks, not a proof of all parameters;
Note59's scalar algebra supplies that proof. No theta moment, flow,
quadrature or interval acquisition was performed.

The meaningful improvement is the complete finite bound at the old
comparison's singular endpoint, with initial variance and derivative costs
exposed. The large conservative C3 can make the guaranteed improvement
small. **A strict local restart is not a global continuation estimate.**
Repeated intervals could shrink to a finite sum; no lower total time has
been proved. This keeps the conclusion within [avoid07][scope] and
[avoid20][utility], and the controls within [cluster12][controls].

**Next: [E] CTF-E08 R8 — Sol**, the fixed proof/cost/scope assessment in
[the packet][packet]. Keep Note59 and this self-assessment frozen; any
correction goes in the assessment/return. Both manuscripts retain their
prior versions. Parent B02 remains partial, E03/B03 gated.

[note]: ../notes/59_DIFFUSION_VARIANCE_COMPRESSION_BOUND_B02_R8_20261029.md
[check]: ../numerics/25_DIFFUSION_VARIANCE_CONSTANT_CHECKS_20261029.json
[packet]: ../research-progress/handoffs/CTF-E08_DIFFUSION_VARIANCE_ASSESSMENT_REQUEST_R8_20261029.md
[scope]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[utility]: ../../../../avoid/20_volume_without_a_gain.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
