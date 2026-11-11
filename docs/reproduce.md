# Reproducing the results

Each workflow is labelled with its verification status at release preparation (2026-11-11):
**Verified** = run end to end and outputs matched; **Partially verified** = some steps run; **Unverified** = not run.

## Without a GPU and without the datasets
| Step | Command | Status |
|---|---|---|
| Install | `pip install numpy pandas scikit-learn` is enough for this section (`verify_outputs.py` needs only the standard library); the full pinned set is in `requirements.txt` | Pinned install unverified; the scripts below were run with Python 3.14, numpy 2.4.6, pandas 2.3.3, scikit-learn 1.9.0 |
| Integrity of released outputs | `python scripts/verify_outputs.py` recomputes the SHA-256 of all 104 prediction files, 16 tables and 16 figures and compares them with `results/original_run/experiment_manifest.json` | Verified (all match) |
| Error-tagger agreement and corrected shares | `python annotation/agreement.py` prints agreement 47.0%, Cohen's kappa 0.345 (bucket level 54.0%, 0.340) and the corrected bucket shares in `annotation/table13c_buckets_for_paper.csv` | Verified (output equals the CSV and Table 14) |
| Paper numbers | `paper/NUMBERS_TRACE.md` maps each table, figure and number to a file | Partially verified: 50+ numbers spot-checked against the files, no mismatch; vote F1 (Table 5) and M5 AUROC (Table 6) recomputed from `predictions/` and matched |

## Re-running the notebooks (CUDA GPU)
Status: **Unverified.** The notebooks were not re-run for this release.

1. Run `bash scripts/setup_workdir.sh` from the repository (Linux, macOS, WSL or Git Bash on Windows). It creates `work/` with the layout the notebooks expect: `data/raw/`, `predictions/`, `results/` (JSON files), `tables/`, `figures/`, `checkpoints/`, `cache/`, `results2/`. Status: Verified (layout built and checked in a scratch copy).
2. Put the datasets in `work/data/raw/<key>/` as described in `data/README.md`.
3. Start Jupyter with `work/` as the working directory and run `notebooks/01_original_experiments.ipynb`. Training needs a CUDA GPU (one 8 GB RTX 4060 was used); runs resume from `checkpoints/`.
4. Run `notebooks/02_posthoc_analysis.ipynb` from the same folder. It reads the original outputs in `results/` and `predictions/` and writes only to `results2/`.

**Warning.** Stage 1.5 of the original notebook deletes `predictions/F_olik_*.jsonl` and recomputes them. Always run inside `work/`, never in the repository folders, so the released files stay unchanged. `scripts/verify_outputs.py` checks the repository copies, not `work/`.

Run settings: seeds 42, 1337, 2026; Python 3.11.17; torch 2.14.1 + CUDA 12.6; Windows; one RTX 4060 (8 GB). Package versions: `requirements.txt`.
