#!/usr/bin/env python3
"""CQ-E01: bounded exact controls, prepared for Edward Baker, 2026-11-18.

OpenAI Codex LLM assistance. Actual model/effort unavailable in the chat record.
No canonical source data are evaluated; all fractions below are exact.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import platform


def check_case(xs, exteriors, radius):
    x, ext, A = list(map(F, xs)), list(map(F, exteriors)), F(radius)
    n = len(x)
    c = sum(x) / n
    y = [v - c for v in x]
    rho = max(map(abs, y))
    assert rho < A and all(abs(z-c) > A for z in ext)
    p2, p3, p4 = [sum(v**k for v in y) for k in (2,3,4)]
    beta = F(2*n-3, n*(n-1))
    J = beta*p2*p2/4-p4/4
    grad = [-v**3+beta*p2*v+p3/n for v in y]
    assert sum(grad) == 0
    assert sum(g*v for g,v in zip(grad,y)) == 4*J
    q2 = sum(g*v*v for g,v in zip(grad,y))
    assert n == 4 and q2 == -p2*p3/6
    R = [sum(1/(v-z) for z in ext) for v in x]
    b = -sum(1/(c-z)**2 for z in ext)
    vel = [2*sum(1/(v-z) for j,z in enumerate(x) if j != i)+2*R[i]
           for i,v in enumerate(x)]
    cp = sum(vel)/n
    yp = [v-cp for v in vel]
    p2p = 2*sum(v*vp for v,vp in zip(y,yp))
    p4p = 4*sum(v**3*vp for v,vp in zip(y,yp))
    direct = beta*p2*p2p/2-p4p/4
    flux = 2*sum(g*r for g,r in zip(grad,R))
    assert direct == flux
    correction = flux-8*b*J
    # Independent evaluation from residues outside the counted block.
    contour = -2*sum(sum(g/(z-v) for g,v in zip(grad,x))-4*J/(z-c)**2
                     for z in ext)
    assert correction == contour
    # epsilon=1; every allowance is homogeneous in the common field error.
    separate = 2*A*sum(abs(g)/(A-abs(v)) for g,v in zip(grad,y))+8*abs(J)/A
    joint2 = 2/A*sum(abs(g)*v*v/(A-abs(v)) for g,v in zip(grad,y))
    joint3 = 2*abs(q2)/A**2 + 2/A**2*sum(abs(g)*abs(v)**3/(A-abs(v))
                                      for g,v in zip(grad,y))
    assert joint2 <= (rho/A)**2*separate
    if p3 == 0:
        assert joint3 <= (rho/A)**3*separate
    # Exact combined-kernel identity at three cleared rational test points.
    for Z in (A, -A, A+1):
        kernel = sum(g/(Z-v) for g,v in zip(grad,y))-4*J/Z**2
        reduced = sum(g*v*v/(Z-v) for g,v in zip(grad,y))/Z**2
        cubic = q2/Z**3 + sum(g*v**3/(Z-v) for g,v in zip(grad,y))/Z**3
        assert kernel == reduced == cubic
    return {"roots":list(map(str,x)), "exterior":list(map(str,ext)),
            "center":str(c), "radius":str(A), "root_radius":str(rho),
            "p2":str(p2), "p3":str(p3), "C4":str(J),
            "C4_derivative":str(direct), "affine_corrected_flux":str(correction),
            "exterior_residue_flux":str(contour), "q2":str(q2),
            "separate_source_allowance_per_epsilon":str(separate),
            "joint_quadratic_allowance_per_epsilon":str(joint2),
            "joint_quadratic_ratio":str(joint2/separate),
            "joint_cubic_plus_asymmetry_per_epsilon":str(joint3),
            "joint_cubic_plus_asymmetry_ratio":str(joint3/separate)}


def main():
    cases = [check_case([-2,-1,1,2],[-5,5],4),
             check_case([-3,-1,2,5],[-8,9],6)]
    assert cases[0]["joint_quadratic_ratio"] == "31/421"
    assert cases[0]["joint_cubic_plus_asymmetry_ratio"] == "43/1684"
    # At the shifted quartic event roots are (-b,-b,b,b), b=2, T=1/20.
    p2, p4 = F(16), F(64)
    C4 = F(5,48)*p2**2-p4/4
    assert C4 == F(32,3) and p2**2/6-4*C4 == 0
    script=Path(__file__).resolve()
    record={"date_local":"2026-11-18", "timezone":"America/New_York",
            "intended_author":"Edward Baker", "assistance":"OpenAI Codex LLM assistance",
            "recorded_model":None,"recorded_effort":None,
            "python":platform.python_version(),"arithmetic":"fractions.Fraction exact rationals",
            "scope":"Two fixed six-root examples and one quartic collision; allowance comparisons, not actual canonical errors or total widths.",
            "cases":cases,"collision_control":{"T":"1/20","b":"2","C4":str(C4),
                 "quadratic_discriminant_in_z_squared":"0","collision_retained":True},
            "script_sha256":hashlib.sha256(script.read_bytes()).hexdigest()}
    out=script.with_name('01_AFFINE_FLUX_EXACT_CHECKS_20261118.json')
    out.write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps({"status":"passed","record":str(out),
                      "symmetric_allowance_ratios":[cases[0]['joint_quadratic_ratio'],cases[0]['joint_cubic_plus_asymmetry_ratio']],
                      "asymmetric_p3":cases[1]['p3']}))


if __name__=='__main__':
    main()
