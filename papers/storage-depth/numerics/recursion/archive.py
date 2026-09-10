"""Fail-closed, dual-hash lookup for current spatial matrix records."""
import os
import json
from pathlib import Path
from common import PAPER,legacy_io,verify_legacy,source_hashes

def load(record_path):
    record=json.loads(Path(record_path).read_text())
    rel=Path(record['matrix_archive'])
    if rel.is_absolute() or '..' in rel.parts:raise ValueError('Unsafe archive path')
    path=PAPER/'numerics'/rel
    if not path.is_file():
        root=os.environ.get('STORAGE_DEPTH_ARCHIVES')
        if root:path=Path(root).expanduser()/rel
    if not path.is_file():
        raise FileNotFoundError(f'Missing {rel}. Set STORAGE_DEPTH_ARCHIVES or regenerate using ARCHIVES.md.')
    if path.stat().st_size!=record['bytes']:raise ValueError('Archive size mismatch')
    if legacy_io.file_hash(path)!=record['matrix_archive_sha256']:raise ValueError('Archive file hash mismatch')
    data=legacy_io.read_data(path)
    if legacy_io.matrix_content_hash(data)!=record['matrices_content_sha256']:raise ValueError('Matrix content hash mismatch')
    for name,digest in data['source_sha256'].items():
        if source_hashes().get(name)!=digest:raise ValueError(f'Builder source mismatch: {name}')
    verify_legacy()
    return data,record,path
