# Where every number in the paper comes from
Paths are relative to the repository root. `results/original_run/` = outputs of `notebooks/01_original_experiments.ipynb`; `results/posthoc/` = outputs of `notebooks/02_posthoc_analysis.ipynb` (post hoc). Table and figure numbers follow the order of the floats in `paper/main.tex`.

| Paper item | Source file(s) | Notes |
|---|---|---|
| Table 1 (datasets), fertility and truncation numbers (Sec. 5.2) | results/original_run/tables/table1_dataset_and_fertility_audit.csv | Sections "Dataset statistics" and "Tokenizer fertility audit" |
| Leakage counts (151 / 275 / 507; 9 / 30) | results/original_run/leakage_report.json; Stage 1.5 log of the original notebook; results/posthoc/olikbochon_leaked_ids.json | 6,134 -> 5,627 training rows |
| Table 4, Fig. 2 | results/original_run/tables/table3_cross_lingual_transfer.csv; native F1: results/original_run/tables/table2_native_source_evaluation.csv | |
| Table 6, Fig. 3 | results/original_run/tables/table4_low_resource_adaptation.csv | M5 row: F1 from results/posthoc/tables/table12b_context_split.csv; AUROC 0.837 = mean of per-seed test AUROC (0.8437, 0.8332, 0.8328) recomputed from predictions/E_test_M5_seed*.jsonl |
| Table 5 | results/original_run/tables/table7_statistical_significance_matrix.csv | Vote-F1 columns (0.5083, 0.5335, 0.8428, 0.5365, 0.8029); M3 vote-F1 0.5365 is printed as 0.537 in Table 5 and the text; recomputed from predictions/E_test_* and C_test_* with results/original_run/thresholds.json, majority vote of three seeds |
| Table 7, Fig. 4 | results/posthoc/tables/table11_m3_diagnostic.csv; results/posthoc/figures/figX1_training_dynamics_xlmr_vs_banglabert.pdf | M5 and M4 curves come from `train_log.json` in checkpoints/M5_mil_seed42 and checkpoints/M4-100pct_seed42 (checkpoints are not released; per-epoch logs of the original runs are also stored under `training_logs` in results/original_run/experiment_manifest.json) |
| Table 8, Fig. 5 left, Sec. 5.4 text | results/posthoc/tables/table12b_context_split.csv; results/posthoc/tables/table12b2_transfer_drop_decomposition.csv; results/posthoc/tables/table13b_error_rate_by_context.csv | 718 / 510 rows: printed by the state-loader cell of the post hoc notebook |
| Table 9, Fig. 5 right, contrasts (+0.217, +0.005, +0.066, +0.153) | results/posthoc/tables/table10_grounding_ablation.csv; results/posthoc/tables/table15_key_contrasts.csv | |
| Table 10 | results/posthoc/tables/table12a_olikbochon_leak_filtered.csv; results/posthoc/tables/table12a2_olikbochon_m4_vs_lexical.csv | |
| Table 11, Fig. 6, Sec. 5.6 text | results/original_run/tables/table6_legal_domain_shift.csv | Detection rows with Language = All; perturbation recalls from the "Synthetic perturbation" section; retrieval and refusal rows from their sections; theta = 0.844 in the refusal-probe row |
| Table 12, Sec. 5.7 | results/posthoc/tables/table12c_temperature_scaling.csv (means over seeds); results/original_run/aurc.json | AURC: confidence = distance of the seed-averaged probability from the mean threshold |
| Table 13 | results/original_run/tables/table5_external_generalization_and_ablations.csv (accuracy and efficiency section); results/original_run/resources.json | M0 runs on CPU |
| Table 14, Sec. 5.8 | annotation/agreement.py (run it); annotation/table13c_buckets_for_paper.csv; results/posthoc/tables/table13_error_taxonomy_banghallu_only.csv | Labels (LLM-drafted, author-reviewed): annotation/error_sample_100.csv; tagger categories: annotation/key.csv |
| Split overlap (Sec. 3.2) | results/posthoc/tables/table14_split_overlap.csv | |
| Pooling robustness (<= 0.009) | results/original_run/tables/table5_external_generalization_and_ablations.csv (pooling section) | |
| Tables 2, 3, 15; Fig. 1; Algorithm 1 | — | Descriptive only (detectors, design, implementation settings, study flow); every value repeats a setting stated in Sections 3–4 and contains no result |
