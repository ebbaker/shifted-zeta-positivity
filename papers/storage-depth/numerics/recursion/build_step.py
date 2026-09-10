"""Append a second quarter slab, inheriting the certified first spatial head.

The default seed is hash-bound to v0.1. All generated matrix data must be
written to the caller's external archive directory.
"""
import argparse
import gzip
import json
import time
from pathlib import Path
from flint import ctx
from common import *
from spatial import Geometry
import tails

def run(args):
    assert __debug__
    start=time.monotonic();ctx.prec=args.bits
    generating_sources=source_hashes()
    verified=verify_legacy()
    rel='history/quarter-step-closure-20260910/closure_256_32.matrices.json.gz'
    seedpath=legacy_io.verify(rel)
    seed=legacy_io.read_data(seedpath)
    assert seed['profile_degree']==args.degree==320
    unpack=lambda mat:AM([[c.unpack(x) for x in row] for row in mat])
    oldhead=unpack(seed['matrices']['head'])
    oldgrams=[unpack(seed['matrices'][x]) for x in ['gram_old','gram_new']]
    seederr=c.unpack(seed['output_error'])
    seedtrace=sum((g[i,i] for g in oldgrams for i in range(oldhead.nrows())),A(0)).upper()
    seedrecord=next(r for r in legacy_io.catalog() if r['path']==rel)
    del seed
    h=(logn(8)-logn(7))/4
    geo=Geometry([logn(7),h,h],[256,32,args.new],args.degree)
    beta,tail=tails.bounds(geo,args.cells)
    print('Tail floor',beta.str(20),flush=True)
    ns=geo.modes;offsets=[0]
    for n in ns:offsets.append(offsets[-1]+n)
    N=offsets[-1];head=AM(N,N);setblock(head,oldhead,0,0)
    for source in range(3):
        block=geo.head_block(2,source)
        setblock(head,block,offsets[2],offsets[source])
        if source<2:
            reverse=geo.head_block(source,2)
            assert frob2(reverse-block.transpose()).sqrt()<A('1e-100')
            setblock(head,block.transpose(),offsets[source],offsets[2])
    head=c.sym(head)
    print('Head assembled; retaining the first 288 modes',flush=True)
    grams=[]
    for target in range(3):
        gram=AM(N,N)
        if target<2:setblock(gram,oldgrams[target],0,0)
        for left in range(3):
            for right in range(left,3):
                if target<2 and right<2:continue
                print('Gram output',target,'inputs',left,right,flush=True)
                block=geo.gram_block(target,left,right)
                assert all(x.is_finite() for x in block.entries()), ('Non-finite Gram block',target,left,right)
                print('Gram block finite; maximum radius',max(x.rad() for x in block.entries()).str(10),flush=True)
                setblock(gram,block,offsets[left],offsets[right])
                if left!=right:setblock(gram,block.transpose(),offsets[right],offsets[left])
        grams.append(c.sym(gram))
    eta=residual.eta(geo.L.value(),args.degree).upper()
    # Inherited old/old Gram blocks are compared with the exact truncated
    # model used for the new cross blocks. Each old output is a contraction
    # of the full seed output. Sum the two independent block error bounds.
    inherited_delta=(seederr+eta).upper()
    inherited_gram_error=2*(2*inherited_delta*seedtrace.sqrt()+inherited_delta**2)
    gram=sum(grams,AM(N,N))
    trace_upper=(sum((gram[i,i] for i in range(N)),A(0))+N*inherited_gram_error).upper()
    assert trace_upper>0 and trace_upper.is_finite()
    model_norm=trace_upper.sqrt()
    gram_error=(inherited_gram_error+2*eta*model_norm+eta**2).upper()
    leakage_error=(gram_error+2*eta*frob2(head).sqrt()+eta**2).upper()
    leakage=c.sym(gram-head*head)
    archive={'partition':[x.json() for x in geo.lengths],'modes':ns,'profile_degree':args.degree,
             'precision_bits':args.bits,'tail_bounds':tail,'eta':c.pack(eta),
             'gram_error':c.pack(gram_error),'leakage_error':c.pack(leakage_error),
             'matrices':{name:[[c.pack(x) for x in row] for row in mat.tolist()]
                         for name,mat in [('head',head)]+[(f'gram_{i}',g) for i,g in enumerate(grams)]},
             'seed_record':seedrecord,'source_sha256':generating_sources}
    out=Path(args.archive_dir);out.mkdir(parents=True,exist_ok=True)
    assert source_hashes()==generating_sources, 'Sources changed during matrix construction'
    path=out/'central_matrices.json.gz'
    with gzip.open(path,'wt') as stream:json.dump(archive,stream,separators=(',',':'))
    floor=rat(args.floor)
    result={'positive':False,'reason':'No positive analytic complement floor'}
    if beta>floor>0:
        budget=((beta-floor)*eta+leakage_error).upper()
        test=c.sym((head-ident(N)*floor)*(beta-floor)-leakage-ident(N)*budget)
        print('Checking all-input Schur guard',flush=True)
        result=ldl(test)
    record={'scope':'Second quarter step with inherited first-step spatial head; three interval complements.',
            'partition':archive['partition'],'modes':ns,'profile_degree':args.degree,'precision_bits':args.bits,
            'requested_full_coercivity':args.floor,'horizon':geo.L.value().str(45),
            'tail_bounds':tail,'eta_upper':eta.str(45),'gram_error_upper':gram_error.str(45),
            'leakage_error_upper':leakage_error.str(45),'all_input_certificate_pass':result['positive'],
            'schur_check':result,'matrix_archive':args.archive_relative,
            'matrix_archive_sha256':legacy_io.file_hash(path),
            'matrices_content_sha256':legacy_io.matrix_content_hash(archive),'bytes':path.stat().st_size,
            'seed_record':seedrecord,'verified_legacy_files':verified,'source_sha256':archive['source_sha256'],
            'seconds':time.monotonic()-start}
    Path(args.record).write_text(json.dumps(record,indent=2)+'\n')
    (out/'build_record.json').write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps({k:v for k,v in record.items() if k not in ['tail_bounds','schur_check','seed_record','source_sha256']},indent=2),flush=True)
    print('Schur check',{k:v for k,v in result.items() if k not in ['pivots','pivot_ball']},flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--bits',type=int,default=6144);p.add_argument('--degree',type=int,default=320)
    p.add_argument('--new',type=int,default=32);p.add_argument('--cells',type=int,default=512)
    p.add_argument('--floor',default='1e-36')
    p.add_argument('--archive-dir',required=True);p.add_argument('--archive-relative',default='output/second-quarter/central_matrices.json.gz')
    p.add_argument('--record',required=True)
    run(p.parse_args())
