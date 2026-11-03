"""Fixed rational normalization bookkeeping for MC07; no acquired Donaldson data."""
from fractions import Fraction as Q
from math import factorial
import json
# Imported fixed p=0 Donaldson coefficients in MW (9.24); this check does not prove them.
normalization=Q(-2,3)
d0=normalization*Q(-3,2)
d1=Q(0)  # degree selection, proved analytically in the return
d2=normalization*Q(5,factorial(5))
d4=normalization*Q(27,factorial(9))
minor=d1*d1-d0*d2
assert (d0,d1,d2,d4,minor)==(Q(1),Q(0),Q(-1,36),Q(-1,20160),Q(1,36))
print(json.dumps({"scope":"fixed imported-coefficient factorial and 2x2 convention check", "d0":str(d0),"d1":str(d1),"d2":str(d2),"d4":str(d4),"D2_1":str(minor),"passed":True},indent=2))
