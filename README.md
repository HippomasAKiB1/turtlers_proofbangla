# Do Hallucination Detectors Read the Context? Transfer, Adaptation, and Grounding in Bengali Retrieval-Augmented Generation

Companion repository of the paper by Akib Hasan Pyil, Nazat E Rose Rhythm, Most. Sumaiya Habiba Nishat, S M Abdullah Shafi and Md. Ariful Islam (American International University-Bangladesh), submitted to ACM TALLIP. It holds the notebooks, frozen thresholds, per-example predictions, result tables, figures and error-analysis files behind every number in the paper.

## Abstract
Hallucination detectors for retrieval-augmented generation are developed mostly in English, and their behaviour on low-resource languages is unclear. Seven detectors are compared on the Bengali BangHallu benchmark on a single 8 GB GPU. Two released English and Chinese LettuceDetect checkpoints fall from 0.773 and 0.746 Macro-F1 on their native test sets to 0.533 and 0.508, below a lexical-overlap baseline (0.653), and stay low on rows with a context passage; their tokenizers split a Bengali word into about nine and eight subwords. BanglaBERT-large reaches 0.775 with 564 training examples and 0.832 with 5,627. An XLM-R sequence classifier did not train under five recipes, while the same backbone with a token-level multiple-instance head reaches 0.730. In a post hoc analysis of the 41.5% of test rows without context, the best detector (0.705) is indistinguishable from a question-and-answer-only model (+0.005, 95% confidence interval −0.019 to 0.031), whereas with context it reaches 0.921. Results on an external Bengali set (0.684 after leakage filtering) and a synthetic legal test (0.666 with gold evidence) are weaker. The study is empirical: a Bengali-pretrained encoder with a few hundred labelled examples is a workable starting point, and results should be reported separately for rows with and without evidence.

## Contributions
1. A controlled comparison of seven detectors (M0–M6) for Bengali under one protocol on a single 8 GB GPU, with seed-level variance, paired bootstrap intervals and Holm-corrected tests.
2. A tokenizer-fertility audit and a low-resource adaptation curve from zero to 5,627 Bengali examples, with a documented negative result on XLM-R sequence classification.
3. A post hoc grounding analysis that splits BangHallu test rows by context availability and ablates the input of the best detector.
4. An external evaluation on Olikbochon with a leakage filter, a legal-domain stress test with gold and retrieved evidence, calibration and cost measurements, and an error analysis whose rule-based tagger is validated against LLM-drafted, author-reviewed labels and then corrected.
5. Code, frozen thresholds and per-example predictions for every number in the paper.

## Repository map
| Path | Content |
|---|---|
| `notebooks/01_original_experiments.ipynb` | Original run: data loading, models M0–M6, evaluation, tables, figures (executed, with outputs) |
| `notebooks/02_posthoc_analysis.ipynb` | Post hoc analyses (executed). Reads the original outputs, writes only new files |
| `results/original_run/` | Original run: thresholds, leakage report, AURC, resources, run manifest with SHA-256 hashes, `tables/`, `figures/`. The run's `error_analysis_100_samples.csv` is not released because it contains dataset text |
| `results/posthoc/` | Post hoc tables, figures, thresholds, manifest |
| `predictions/` | 104 per-example prediction files `<stage>_<split>_<model>_seed<seed>.jsonl`: hashed id, gold label, scores; no dataset text |
| `annotation/` | 100 sampled BangHallu errors with LLM-drafted, author-reviewed labels; tagger categories (`key.csv`); `agreement.py`; corrected error shares (`table13c_*`) |
| `paper/` | Manuscript source (`main.tex`, `tables/`, `figures/`, `references.bib`) and `NUMBERS_TRACE.md` |
| `data/README.md` | Where to obtain each dataset (no data is included) |
| `docs/reproduce.md` | Reproduction steps with verification status |
| `scripts/` | `setup_workdir.sh` (builds the notebooks' working folder), `verify_outputs.py` (hash check) |

## Dataset access
No dataset is redistributed. BangHallu, BanglaGovRAG and BD Legal QA are on GitHub, Olikbochon is a Kaggle competition, and RAGTruth is on Hugging Face; links and placement are in `data/README.md`. What each source states about licensing is summarised in `data/README.md`; the data licences of BangHallu, Olikbochon and BanglaGovRAG are not settled, so check each source before use.

## Installation
Python 3.11 and a CUDA GPU for training (one 8 GB RTX 4060 was used).
```bash
pip install -r requirements.txt   # versions recorded by the original run; install torch 2.14.1 for your CUDA version
```

## What can be verified without a GPU
```bash
python scripts/verify_outputs.py   # SHA-256 of all predictions, tables and figures vs. the run manifest
python annotation/agreement.py     # agreement 47.0%, kappa 0.345, corrected error shares (Table 14)
```
Both need no dataset; `agreement.py` needs `numpy`, `pandas`, `scikit-learn`. Every table and figure is mapped to its source file in `paper/NUMBERS_TRACE.md`, and most metrics can be recomputed from `predictions/` with `results/original_run/thresholds.json`.

## How to reproduce
See `docs/reproduce.md`: `bash scripts/setup_workdir.sh`, place the data in `work/data/raw/`, then run both notebooks with `work/` as the working directory. The original notebook deletes and recomputes `predictions/F_olik_*.jsonl` (Stage 1.5), so never run it in the repository folders. Seeds 42, 1337, 2026. The GPU workflow has not been re-run for this release (Unverified).

## Results summary
Macro-F1 on the BangHallu test set (1,228 rows) unless stated; mean over three seeds for M3–M5.

| Finding | Value | Source |
|---|---|---|
| Released detectors, native → BangHallu | M1 0.773 → 0.533; M2 0.746 → 0.508; lexical baseline M0 0.653 | `results/original_run/tables/table2_native_source_evaluation.csv`, `table3_cross_lingual_transfer.csv` |
| Tokens per Bengali word | ModernBERT 9.18, EuroBERT 8.10, XLM-R 2.26, BanglaBERT 1.44 | `results/original_run/tables/table1_dataset_and_fertility_audit.csv` |
| BanglaBERT-large (M4) with 564 / 1,408 / 5,627 training examples | 0.775 / 0.785 / 0.832 | `results/original_run/tables/table4_low_resource_adaptation.csv` |
| XLM-R sequence head (M3), 100% data; XLM-R token head (M5) | 0.502; 0.730 | `table4_low_resource_adaptation.csv`; `results/posthoc/tables/table12b_context_split.csv` |
| **Post hoc:** rows with / without context | 718 / 510 (41.5% without) | `results/posthoc/extended_summary.md`, `results/posthoc/tables/table12b_context_split.csv` |
| **Post hoc:** M4 with / without context | 0.921 / 0.705 | `results/posthoc/tables/table12b_context_split.csv` |
| **Post hoc:** M4 minus question+answer-only model, rows without context | +0.005, 95% CI [−0.019, 0.031] | `results/posthoc/tables/table15_key_contrasts.csv` |
| **Post hoc:** Olikbochon M4, all 299 / leakage-filtered 269 rows | 0.698 / 0.684; gain over M0 on filtered rows +0.040, CI [−0.032, 0.109] | `results/posthoc/tables/table12a_olikbochon_leak_filtered.csv`, `table12a2_olikbochon_m4_vs_lexical.csv` |
| Synthetic legal test, M4 gold / retrieved evidence | 0.666 / 0.571 | `results/original_run/tables/table6_legal_domain_shift.csv` |
| **Post hoc:** M4 ECE before / after temperature scaling | 0.117 / 0.085 (F1 unchanged) | `results/posthoc/tables/table12c_temperature_scaling.csv` |
| Error-tagger agreement with reviewed labels | 47.0%, kappa 0.345 | output of `annotation/agreement.py` |

## Post hoc analyses
These analyses were added after the original run and are labelled post hoc in the paper and here: the context split, the M4 input ablation, the M3 diagnostic, the Olikbochon leakage filter and temperature scaling. Their outputs are in `results/posthoc/` and come from `notebooks/02_posthoc_analysis.ipynb`, which records in `results/posthoc/manifest_v2.json` that no original output was changed.

## Error-analysis labels and the superseded taxonomy
The 100 error labels in `annotation/` were drafted by an LLM (Claude) without access to the tagger's categories and then reviewed row by row by the authors, with the tagger's categories hidden; the authors accepted all 100 without changes. They were not annotated independently and there is no second annotator, so they validate the tagger's coarse behaviour, not a gold standard. Columns named `manual_*` in the CSVs hold these LLM-drafted, author-reviewed labels. The released annotation CSVs keep identifiers, labels and scores only; the question, context and answer text was removed (join on `id` with the dataset or with `predictions/`). `annotation/key.csv` holds the rule-based tagger's categories, which were hidden while labelling; it is not an answer key.
The original rule-based taxonomy in `results/original_run/tables/table8_error_taxonomy_breakdown.*` and `results/original_run/figures/fig6_pareto_efficiency_and_error_taxonomy.*` is unvalidated (agreement 47.0%, kappa 0.345) and superseded by the corrected shares in `annotation/table13c_buckets_for_paper.csv` and `annotation/table13c_calibrated_error_taxonomy.csv`.

## Limitations
One main Bengali benchmark and a 299-row external set; three seeds; the XLM-R sequence-head failure is unexplained; the legal negatives are synthetic perturbations; answer-level, not span-level, evaluation; the error labels are LLM-drafted and author-reviewed, not independently annotated, and validate only the tagger's coarse behaviour; dataset versions were not pinned by commit; model checkpoints are not released.

## Citation
See `CITATION.cff`. No DOI or publication record exists yet.

## Licence
Code: MIT (`LICENSE`), pending confirmation by the authors. The datasets are not included and keep their own terms (see `data/README.md`).
