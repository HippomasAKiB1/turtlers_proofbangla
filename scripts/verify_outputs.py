"""Check the released outputs against the SHA-256 hashes recorded by the original run.

results/original_run/experiment_manifest.json stores a hash for every prediction file, table and figure
written by notebooks/01_original_experiments.ipynb. This script recomputes them. It needs only the Python
standard library and does not read any dataset. Run from the repository root:

    python scripts/verify_outputs.py
"""
import hashlib, json, sys
from pathlib import Path

root = Path(__file__).resolve().parent.parent
manifest = json.loads((root / "results/original_run/experiment_manifest.json").read_text(encoding="utf-8"))
sections = {"predictions": root / "predictions",
            "tables": root / "results/original_run/tables",
            "figures": root / "results/original_run/figures"}
failed = 0
for sec, folder in sections.items():
    ok, bad = 0, []
    for name, rec in manifest[sec].items():
        expected = rec["sha256"] if isinstance(rec, dict) else rec
        path = folder / name
        if not path.is_file():
            bad.append(f"missing {name}")
        elif hashlib.sha256(path.read_bytes()).hexdigest() != expected:
            bad.append(f"hash differs {name}")
        else:
            ok += 1
    failed += len(bad)
    print(f"{sec}: {ok}/{len(manifest[sec])} match")
    for b in bad:
        print("   ", b)
sys.exit(1 if failed else 0)
