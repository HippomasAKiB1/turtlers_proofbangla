# Tagger vs LLM-drafted, author-reviewed labels — BangHallu error sample (n = 100, rows with context)

Labels: drafted by an LLM annotator (Claude) blind to the automatic labels, then reviewed row by row by the authors; all 100 labels were accepted without changes.

"Table 8" in this report is the original run's `results/original_run/tables/table8_error_taxonomy_breakdown.csv` (unvalidated). The corrected shares below are saved in `table13c_buckets_for_paper.csv` and appear as Table 14 in the paper. Columns named `manual_*` in the CSVs hold the LLM-drafted labels.

## Headline
| Measure | Value |
|---|---|
| Exact agreement, 10 categories | 47.0% |
| Cohen's kappa, 10 categories | 0.345 |
| Agreement / kappa, 5 macro-buckets | 54.0% / 0.340 |
| FN rows (hallucination missed), n=61 | 32.8% agree, kappa 0.105 |
| FP rows (faithful answer flagged), n=39 | 69.2% agree, kappa 0.312 |

Kappa is below the 0.6 bar, so the rule-based tagger is NOT validated. Table 8 must not be presented as a human-verified taxonomy as it stands.
Note: the sample was stratified by the tagger's category, so overall agreement and kappa depend on the sample mix; per-category precision below is the cleaner figure.

## Per-category quality of the tagger
| Category | tagger assigned (n) | precision | recall |
|---|---|---|---|
| 1 Numeric / date | 22 | 0.68 | 0.56 |
| 2 Entity substitution | 15 | 0.20 | 0.23 |
| 3 Negation | 0 | -- | 0.00 (6 true) |
| 4 Unsupported addition | 3 | 0.00 | 0.00 (13 true) |
| 5 Subtle contradiction | 23 | 0.09 | 0.22 |
| 6 Paraphrase (false alarm) | 31 | 0.81 | 0.89 |
| 8 Script mismatch | 3 | 0.67 | 1.00 |
| 9, 10 | 1, 2 | 0.00 | -- |

Main failure patterns (tagger -> reviewed label): 5 -> 1 (9 rows) and 5 -> 2 (8): the "subtle contradiction" label is a catch-all for numeric and entity errors; 1 -> 4 (7): faithful answers with a date not in the context; 6 -> 4 (5): correct answers not stated in the context; 5 -> 3 (3) and 2 -> 3 (3): negations are never detected.

## Calibrated Table 8 (with-context errors, tagger counts corrected with the tagger-vs-reviewed-label confusion matrix)
Share of each model's with-context errors, 95% bootstrap interval (2000 resamples within tagger strata):

| Bucket | M0 | M1 | M2 | M4-100% | M5 |
|---|---|---|---|---|---|
| Factual detail (number/date/entity/legal) | 52% [41,64] | 40% [32,48] | 45% [36,53] | 41% [26,52] | 39% [32,45] |
| Logical (negation/contradiction) | 13% [3,24] | 15% [9,21] | 18% [12,25] | 20% [10,34] | 11% [6,16] |
| Extrinsic content | 8% [4,12] | 13% [7,20] | 12% [7,19] | 10% [5,15] | 13% [7,20] |
| Surface / form (mostly false alarms) | 25% [20,32] | 31% [25,36] | 24% [19,28] | 28% [24,33] | 36% [29,42] |
| Input processing | 1% [0,3] | 1% [0,3] | 1% [0,3] | 1% [0,3] | 1% [0,4] |
| Errors on rows with context (n) | 158 | 303 | 351 | 53 | 102 |

The raw tagger said "Logical" was 61% of M0 errors and 29% of M5 errors; the calibrated figures are 13% and 11%. Rows WITHOUT context (own category, no taxonomy possible) are 62% / 46% / 42% / 74% / 69% of M0 / M1 / M2 / M4 / M5 errors.

## Caveats
* Calibration assumes the reviewed-label-vs-tagger confusion is the same for every model (the sample pools errors from all five).
* Strata with 1-3 sampled rows (tagger categories 4, 8, 9, 10) are tiny, so their intervals understate uncertainty. "Input processing" rests on a single row.
* Only rows with context are covered; the 100 rows were drawn from the 967 with-context errors.

## Suggested wording
"We validated the rule-based error tagger on 100 sampled BangHallu errors (rows with context). Labels were drafted by an LLM annotator blind to the tagger output and reviewed row by row by the authors. Agreement was 47% (Cohen's kappa 0.35), so we do not rely on the tagger's fine-grained categories; Table 8 reports macro-bucket shares corrected with the confusion matrix between tagger and reviewed labels, with bootstrap intervals."
