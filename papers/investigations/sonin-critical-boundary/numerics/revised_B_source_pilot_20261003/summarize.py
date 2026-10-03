#!/usr/bin/env python3
"""Summarize small records; no derived matrices are loaded or persisted."""
import hashlib,json
from pathlib import Path
p=Path(__file__).parent
rows=[]
for path in sorted(p.glob('*_c*.json')):
 d=json.loads(path.read_text())
 rows.append({'file':path.name,'source_dim':d['source_dim'],'mean_zero':d['mean_zero_exact_by_preparation'],'trial_cells':d['trial_cells'],'B_min':d['B_eigenvalues'][0],'Q_min':d['Q_eigenvalues'][0],'K_d_max':d['K_d_eigenvalues'][-1],'revised_margin_min':d['B_minus_K_d_positive_part_eigenvalues'][0],'generalized_K_d_max':d['generalized_K_d_over_B_eigenvalues'][-1],'relative_positive_part_max':d['relative_positive_part_max'],'opposite_parity_B_max':d['opposite_parity_B_max'],'record_sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
res={'status':'EXPLORATORY_FLOATING_NO_CERTIFICATION','scope':'Finite smooth L1 source spaces; exact support diameter0.9. All reported positive parts are finite matrix positive parts.','results':rows}
(p/'SUMMARY.json').write_text(json.dumps(res,indent=2)+'\n');print(json.dumps(res,indent=2))
