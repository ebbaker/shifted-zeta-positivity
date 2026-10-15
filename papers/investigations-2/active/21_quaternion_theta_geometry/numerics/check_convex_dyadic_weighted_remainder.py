#!/usr/bin/env python3
"""Exact finite audit of Note 39's dyadic arithmetic, not an analytic proof.

Prepared for Edward Baker, 15 October 2026, with substantial LLM assistance.
Recorded parent model: gpt-6-astra; reasoning effort: ultra.
Run from repository root, or pass --repo-root explicitly.
"""
import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path

p = argparse.ArgumentParser()
p.add_argument('--repo-root', type=Path, default=Path.cwd())
p.add_argument('--output', type=Path, required=True)
a = p.parse_args()
checks = []
def check(label, ok):
    if not ok:
        raise AssertionError(label)
    checks.append(label)

def f(pair, beta, theta):
    k,l = pair
    return k+(l-k-Q(1,2))*beta-theta*beta*(1-beta)/4

def threshold(pair, beta):
    k,l=pair
    return 4*(k+(l-k-Q(1,2))*beta)/(beta*(1-beta))

names=['A2P','AP','D','R','P']
pairs=[(Q(13,414),Q(359,414)),(Q(13,194),Q(76,97)),(Q(18,199),Q(593,796)),(Q(4742,38463),Q(35731,51284)),(Q(13,84),Q(55,84))]
ends=[Q(1,5),Q(3,10),Q(3,8),Q(81,200),Q(3,7),Q(1,2)]
theta=Q(61,24); rho=eta=Q(1,100000)
mu=Q(21807,254720000)
margin=mu-rho*(1+Q(1,2)+Q(1,16)+1)
check('surviving margin',margin==Q(76399,1273600000))
check('strict saved power',margin>Q(1,20000))
for i,(name,pair) in enumerate(zip(names,pairs)):
    left,right=ends[i:i+2]
    check(name+' ordered interval',left<right)
    check(name+' left endpoint margin',f(pair,left,theta)<=-mu)
    check(name+' right endpoint margin',f(pair,right,theta)<=-mu)
    check(name+' nonnegative linear coefficient',pair[1]-pair[0]-Q(1,2)>=0)
    # For a quadratic, this identity of coefficients proves the chord formula.
    # Expand at three distinct points, sufficient for polynomial degree <= 2.
    for label,beta in [('left',left),('middle',(left+right)/2),('right',right)]:
        chord=((right-beta)*f(pair,left,theta)+(beta-left)*f(pair,right,theta))/(right-left)
        check(name+' exact quadratic chord '+label,f(pair,beta,theta)==chord-theta*(beta-left)*(right-beta)/4)
    width=right-left
    check(name+' curvature distance factor',theta*width/8==Q(61,192)*width)

widths=[b-a for a,b in zip(ends,ends[1:])]
cs=[theta*d/8 for d in widths]
G=11+4*sum((1/c for c in cs),Q())
check('geometric rational constant',G==Q(962773,671))
check('geometric constant below 1435',G<1435)
check('first dyadic endpoint',ends[0]==Q(1,5))
check('last dyadic endpoint',ends[-1]==Q(1,2))

crossings=[]
for i in range(4):
    k,l=pairs[i]; K,L=pairs[i+1]
    b=(K-k)/((l-k)-(L-K))
    crossings.append(b)
    check(names[i]+' adjacent pair equality',f(pairs[i],b,theta)==f(pairs[i+1],b,theta))
opt_ends=[Q(1,5),*crossings,Q(1,2)]
check('exact crossing list',crossings==[Q(1430,4789),Q(362,957),Q(62831,155153),Q(3,7)])
for i,pair in enumerate(pairs):
    left,right=opt_ends[i:i+2]
    check(names[i]+' envelope interval ordered',left<right)
    for endpoint_label,beta in [('left',left),('right',right)]:
        for j,other in enumerate(pairs):
            check(names[i]+' lower envelope '+endpoint_label+' vs '+names[j],f(pair,beta,theta)<=f(other,beta,theta))
        check(names[i]+' critical theta endpoint '+endpoint_label,threshold(pair,beta)<=Q(4911678521,1933561194))
critical=threshold(pairs[2],crossings[2])
check('critical theta identity',critical==Q(4911678521,1933561194))
check('critical theta above five halves',critical>Q(5,2))
check('critical theta below current theorem',critical<Q(61,24))
for name,pair in zip(names,pairs):
    k,l=pair
    c=l-k-Q(1,2)-Q(5,8)
    disc=c*c-Q(5,2)*k
    if name in ['AP','D','R']:
        check(name+' negative discriminant proves positive quadratic',disc<0)
check('A2P first zero at five halves',f(pairs[0],Q(4,23),Q(5,2))==0)
check('A2P second zero at five halves',f(pairs[0],Q(13,45),Q(5,2))==0)
check('P polynomial constant',168*pairs[-1][0]==26)
check('P polynomial linear',168*(pairs[-1][1]-pairs[-1][0]-Q(1,2)-Q(5,8))==-105)
check('P polynomial quadratic',168*Q(5,8)==105)
check('P root discriminant',105**2-4*105*26==105)
check('five halves gap at beta two fifths',f(pairs[2],Q(2,5),Q(5,2))==Q(9,3980))
source=a.repo_root/'papers/investigations-2/active/21_quaternion_theta_geometry/notes/32_CLOSED_STRIP_EXTENSION_AND_MIDDLE_BLOCK_LEMMA_20261014.md'
record={
 'description':'Exact arithmetic supporting convex dyadic summation and the bounded five-pair audit; not verification of imported analytic theorems or any new sign domain.',
 'date':'2026-10-15',
 'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'prepared_for':'Edward Baker',
 'llm_assistance':{'recorded_parent_model':'gpt-6-astra','reasoning_effort':'ultra'},
 'source':{'path':str(source.relative_to(a.repo_root)),'sha256':hashlib.sha256(source.read_bytes()).hexdigest()},
 'checks_passed':len(checks),'checks':checks,
 'values':{'margin':str(margin),'geometric_factor_rational_bound':str(G),'critical_beta':str(crossings[2]),'five_pair_limiting_theta':str(critical)},
 'limitations':['No external exponent-pair theorem is reverified.','No imported implied constant or effective starting height is evaluated.','No new sign domain, finite certificate, or RH conclusion is established.']
}
a.output.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'checks_passed':len(checks),'output':str(a.output),'values':record['values']}))
