"""Agreement between the rule-based error tagger and the LLM-drafted, author-reviewed labels (BangHallu, 100 errors with context).
The labels are in the column named manual_category (legacy name); they were drafted by an LLM and reviewed row by row by the authors.
Inputs (same folder): error_sample_100.csv, key.csv,
and ../results/posthoc/tables/table13_error_taxonomy_banghallu_only.csv (tagger counts per model).
Outputs: raw agreement, Cohen's kappa (10 categories and 5 buckets), per-category precision/recall, calibrated bucket shares with bootstrap CIs."""
import os, re, numpy as np, pandas as pd
from sklearn.metrics import cohen_kappa_score
here = os.path.dirname(os.path.abspath(__file__))  # works from any working directory and on Windows
lab = pd.read_csv(f'{here}/error_sample_100.csv', encoding='utf-8-sig')
key = pd.read_csv(f'{here}/key.csv', encoding='utf-8-sig')
cat = [c for c in lab.columns if c.startswith('manual_category')][0]
m = lab.merge(key[['sample_id', 'category']], on='sample_id').rename(columns={'category': 'auto', cat: 'man'})
m['auto'] = m.auto.astype(int); m['man'] = m.man.astype(int)
B = {1:'Factual detail',2:'Factual detail',10:'Factual detail',3:'Logical',5:'Logical',4:'Extrinsic content',6:'Surface / form',8:'Surface / form',9:'Surface / form',7:'Input processing'}
print(f"n={len(m)} agreement={(m.auto==m.man).mean():.1%} kappa={cohen_kappa_score(m.auto,m.man):.3f}")
ab, mb = m.auto.map(B), m.man.map(B)
print(f"buckets: agreement={(ab==mb).mean():.1%} kappa={cohen_kappa_score(ab,mb):.3f}")
for c in sorted(set(m.auto) | set(m.man)):
    na, nm, tp = (m.auto==c).sum(), (m.man==c).sum(), ((m.auto==c)&(m.man==c)).sum()
    print(f"category {c:2d}: tagger n={na:2d} manual n={nm:2d} precision={tp/na if na else float('nan'):.2f} recall={tp/nm if nm else float('nan'):.2f}")
# corrected bucket shares of with-context errors: post-stratification with the tagger-vs-reviewed-label confusion matrix
t13 = pd.read_csv(f'{here}/../results/posthoc/tables/table13_error_taxonomy_banghallu_only.csv')
models = ['M0', 'M1', 'M2', 'M4-100%', 'M5']; cnt = {}
for _, r in t13.iterrows():
    mm = re.match(r'^(\d+)\.', str(r['Category']))
    if mm and int(mm.group(1)) != 11: cnt[int(mm.group(1))] = {k: int(re.match(r'\s*(\d+)', str(r[k])).group(1)) for k in models}
cnt = pd.DataFrame(cnt).T; samp = {a: m.loc[m.auto==a, 'man'].values for a in sorted(m.auto.unique())}
def calib(s, counts):
    out = np.zeros(11)
    for a, n in counts.items():
        if n == 0: continue
        if a in s and len(s[a]): [out.__setitem__(c, out[c] + n*(s[a]==c).mean()) for c in range(1, 11)]
        else: out[a] += n
    return out
rng = np.random.default_rng(0)
for mod in models:
    c = cnt[mod]; tot = c.sum(); pt = calib(samp, c)
    bs = np.array([calib({a: rng.choice(v, len(v)) for a, v in samp.items()}, c) for _ in range(2000)])
    print(f"\n{mod} (with-context errors n={int(tot)})")
    for bk in ['Factual detail', 'Logical', 'Extrinsic content', 'Surface / form', 'Input processing']:
        idx = [k for k, v in B.items() if v == bk]; lo, hi = np.percentile(bs[:, idx].sum(1), [2.5, 97.5])
        print(f"  {bk:18s} {100*pt[idx].sum()/tot:4.0f}% [{100*lo/tot:.0f}, {100*hi/tot:.0f}]")
