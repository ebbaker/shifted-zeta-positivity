"""Rebuild the second step from a freshly regenerated first-step catalog (v0.3 variant using build_step_seed.py).

The explicit catalog binds the new gzip bytes without altering the immutable
v0.1 catalog. Matrix hashes and the seed's generating sources are verified
before the standard builder is called.
"""
import argparse
import os
from pathlib import Path
from common import *
import build_step_seed as build_step

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--seed-catalog',type=Path,required=True)
    p.add_argument('--seed-archives',type=Path,required=True)
    p.add_argument('--bits',type=int,default=6144);p.add_argument('--degree',type=int,default=320)
    p.add_argument('--new',type=int,default=32);p.add_argument('--cells',type=int,default=512)
    p.add_argument('--floor',default='1e-36');p.add_argument('--archive-dir',required=True)
    p.add_argument('--archive-relative',default='output/second-quarter/central_matrices.json.gz')
    p.add_argument('--record',required=True)
    p.add_argument('--seed-relative',default='history/quarter-step-closure-20260910/closure_256_32.matrices.json.gz')
    args=p.parse_args()
    verify_legacy()
    legacy_io.CATALOG=args.seed_catalog.resolve()
    os.environ['STORAGE_DEPTH_ARCHIVES']=str(args.seed_archives.resolve())
    rel=args.seed_relative
    path=legacy_io.verify(rel)
    seed=legacy_io.read_data(path)
    for name,digest in seed['source_sha256'].items():
        if legacy_io.file_hash(HISTORY/name)!=digest:
            raise ValueError(f'Rebuilt seed source mismatch: {name}')
    del seed
    build_step.run(args)
