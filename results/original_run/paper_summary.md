# ProofBangla — results summary

*Numbering below follows the order in the experiment brief; align the RQ labels with your proposal if they differ.*

## RQ1 — Zero-shot cross-lingual transfer drop
Artifacts: `table2_native_source_evaluation`, `table3_cross_lingual_transfer`, `fig1_tokenizer_fertility_and_transfer_drop` (panel B).
- M1 released English LettuceDetect (ModernBERT): RAGTruth EN Macro-F1 0.773 → BangHallu 0.533 (Δ -0.240)
- M2 released EuroBERT-210M LettuceDetect (Chinese RAGTruth fine-tune): RAGTruth-CN (translated Chinese) Macro-F1 0.746 → BangHallu 0.508 (Δ -0.237)
- Lexical baseline M0 Macro-F1: 0.653

## RQ2 — Tokenizer fertility and truncation
Artifacts: `table1_dataset_and_fertility_audit`, `fig1_…` (panel A).
- ModernBERT: tokens/word EN 1.279 vs BN 9.182; BN answer-token truncation naive 0.000% → context-only 0.000%
- EuroBERT: tokens/word EN 1.241 vs BN 8.098; BN answer-token truncation naive 0.000% → context-only 0.000%
- XLM-R-base: tokens/word EN 1.398 vs BN 2.260; BN answer-token truncation naive 0.000% → context-only 0.000%
- BanglaBERT-large: tokens/word EN 2.139 vs BN 1.437; BN answer-token truncation naive 0.000% → context-only 0.000%
- ModernBERT @512: tokens/word EN 1.279 vs BN 9.182; BN answer-token truncation naive 2.059% → context-only 0.000%
- EuroBERT @512: tokens/word EN 1.241 vs BN 8.098; BN answer-token truncation naive 0.829% → context-only 0.000%

## RQ3 — Low-resource Bengali adaptation
Artifacts: `table4_low_resource_adaptation`, `fig2_low_resource_adaptation_curve`, `table7` (M4-10% vs M4-100%).
- M3 @ 0%: Macro-F1 0.503 ± 0.019
- M3 @ 10%: Macro-F1 0.506 ± 0.027
- M3 @ 25%: Macro-F1 0.561 ± 0.053
- M3 @ 100%: Macro-F1 0.502 ± 0.054
- M4 @ 0%: Macro-F1 0.501 ± 0.020
- M4 @ 10%: Macro-F1 0.775 ± 0.027
- M4 @ 25%: Macro-F1 0.785 ± 0.010
- M4 @ 100%: Macro-F1 0.832 ± 0.007

## RQ4 — External generalization, ablations, calibration, selective prediction
Artifacts: `table5_…` (Olikbochon gap, pooling, query conditioning), `table7_statistical_significance_matrix`, `fig3_calibration_reliability_diagrams`, `fig4_risk_coverage_curves`.
- M0: BangHallu 0.653 ± 0.000 → Olikbochon 0.658 ± 0.000
- M1: BangHallu 0.533 ± 0.000 → Olikbochon 0.542 ± 0.000
- M2: BangHallu 0.508 ± 0.000 → Olikbochon 0.561 ± 0.000
- M3: BangHallu 0.502 ± 0.054 → Olikbochon 0.496 ± 0.057
- M4: BangHallu 0.832 ± 0.007 → Olikbochon 0.698 ± 0.032

## RQ5 — Legal domain shift
Artifacts: `table6_legal_domain_shift`, `fig5_legal_domain_shift_analysis`. Negatives in the legal sets are synthetic perturbations unless the source dataset provides native labels (flagged in the table).
- Retrieval (All, n=1607): R@1 0.228, R@5 0.409, MRR 0.318
- Retrieval (BN, n=971): R@1 0.185, R@5 0.341, MRR 0.266
- Retrieval (CS, n=1): R@1 1.000, R@5 1.000, MRR 1.000
- Retrieval (EN, n=635): R@1 0.291, R@5 0.512, MRR 0.397

## RQ6 — Efficiency and error taxonomy
Artifacts: `table5_…` (accuracy vs efficiency), `table8_error_taxonomy_breakdown`, `fig6_pareto_efficiency_and_error_taxonomy`, `results/error_analysis_100_samples.csv`.
- M0: Macro-F1 0.653, latency 0.087 ms/ex, peak VRAM 8.125 MB (n=1228)
- M1: Macro-F1 0.533, latency 12.093 ms/ex, peak VRAM 587.880 MB (n=1228)
- M2: Macro-F1 0.508, latency 7.102 ms/ex, peak VRAM 674.521 MB (n=1228)
- M3: Macro-F1 0.502, latency 1.428 ms/ex, peak VRAM 652.979 MB (n=1228)
- M4: Macro-F1 0.832, latency 8.752 ms/ex, peak VRAM 784.401 MB (n=1228)
- M5: Macro-F1 0.730, latency 4.129 ms/ex, peak VRAM 575.198 MB (n=1228)
- M6: Macro-F1 0.705, latency 106.448 ms/ex, peak VRAM 2902.250 MB (n=600)

## Generated files
- Tables: table1_dataset_and_fertility_audit, table2_native_source_evaluation, table3_cross_lingual_transfer, table4_low_resource_adaptation, table5_external_generalization_and_ablations, table6_legal_domain_shift, table7_statistical_significance_matrix, table8_error_taxonomy_breakdown
- Figures: fig1_tokenizer_fertility_and_transfer_drop, fig1a_tokenizer_fertility_preview, fig2_low_resource_adaptation_curve, fig3_calibration_reliability_diagrams, fig4_risk_coverage_curves, fig5_legal_domain_shift_analysis, fig6_pareto_efficiency_and_error_taxonomy, fig6a_pareto_preview
- Manifest: `results/experiment_manifest.json`