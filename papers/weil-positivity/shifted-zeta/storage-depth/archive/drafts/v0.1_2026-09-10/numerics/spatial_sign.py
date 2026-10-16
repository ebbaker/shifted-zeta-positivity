"""Re-evaluate the absolute spatial Schur sign on the matrices supplied.

The replay entry point verifies file and content hashes before staging this
file. The sign below is decided by Arb, not by the recorded PASS boolean.
"""
import argparse
import hashlib
import json
from pathlib import Path
from flint import arb_mat as AM, arb as A, ctx
import close_complement as z

def run(archive, output):
    import gzip
    with gzip.open(archive, "rt") as stream:
        data = json.load(stream)
    for rel, digest in data["source_sha256"].items():
        assert hashlib.sha256((z.ROOT / rel).read_bytes()).hexdigest() == digest
    ctx.prec = data["precision_bits"]
    mats = {name: AM([[z.c.unpack(x) for x in row] for row in matrix])
            for name, matrix in data["matrices"].items()}
    H, G = mats["head"], mats["gram_old"] + mats["gram_new"]
    n = H.nrows()
    beta = A(data["tail_bounds"]["joint_tail_floor"]).lower()
    eta, error = z.c.unpack(data["eta"]), z.c.unpack(data["leakage_error"])
    m = z.c.rat("1e-33")
    assert beta > m > 0
    E = z.c.sym(G - H * H)
    budget = ((beta - m) * eta + error).upper()
    test = z.c.sym((beta - m) * (H - m * z.c.ident(n)) - E - budget * z.c.ident(n))
    result = z.c.ldl(test)
    Path(output).write_text(json.dumps({
        "scope": "Arithmetic replay of full spatial Schur test; analytic reductions inherited.",
        "requested_floor": "1e-33", "full_operator_certificate_pass": result["positive"],
        "schur_check": result, "budget": budget.str(40),
        "validator_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    }, indent=2) + "\n")
    assert result["positive"], "The supplied matrices failed the spatial sign test"
    print("Spatial Schur sign replay PASS: inserted floor 1e-33")

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--archive", required=True)
    p.add_argument("--output", required=True)
    a = p.parse_args()
    run(a.archive, a.output)
