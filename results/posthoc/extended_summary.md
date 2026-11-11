# ProofBangla — extended analysis (auto-generated)

* BangHallu test rows without any context: 510 of 1228 (41.5%)
  * M0 lexical: F1 with context 0.779 / without context 0.333
  * M1 released EN: F1 with context 0.575 / without context 0.333
  * M2 released EuroBERT-CN: F1 with context 0.491 / without context 0.390
  * M3 XLM-R seq (original, collapsed): F1 with context 0.486 / without context 0.432
  * M4 BanglaBERT-large (reference): F1 with context 0.921 / without context 0.705
  * M5 XLM-R MIL token detector: F1 with context 0.854 / without context 0.552
  * M4 8-bit, with question (seed 42): F1 with context 0.921 / without context 0.686
  * M4 8-bit, question dropped (seed 42): F1 with context 0.897 / without context 0.504
  * M4 answer-only (new): F1 with context 0.607 / without context 0.518
  * M4 question+answer, no context (new): F1 with context 0.704 / without context 0.700

## Grounding ablation (M4, 3 seeds)
* answeronly: Macro-F1 0.572 ± 0.004, AUROC 0.618
* nocontext: Macro-F1 0.703 ± 0.011, AUROC 0.807

## M3 diagnostic
* lr1e-5: best dev AUROC 0.532, test F1 0.522
* lr2e-5: best dev AUROC 0.542, test F1 0.545
* lr5e-5: best dev AUROC 0.517, test F1 0.490
* lr2e-5-norm: best dev AUROC 0.520, test F1 0.518

## Olikbochon (leak-filtered)
Model  N all  N clean        F1 all      F1 clean       CI clean  Δ (clean − all)  AUROC all  AUROC clean  BangHallu F1  Gap (clean − BangHallu)
   M0    299      269 0.658 ± 0.000 0.644 ± 0.000 [0.586, 0.702]           -0.014      0.629        0.605         0.653                   -0.009
   M1    299      269 0.542 ± 0.000 0.544 ± 0.000 [0.487, 0.603]            0.002      0.602        0.592         0.533                    0.011
   M2    299      269 0.561 ± 0.000 0.546 ± 0.000 [0.486, 0.602]           -0.015      0.598        0.582         0.508                    0.038
   M4    299      269 0.698 ± 0.032 0.684 ± 0.038 [0.636, 0.730]           -0.014      0.782        0.774         0.832                   -0.148

## Temperature scaling
              Model  Seed  T fitted  ECE before  ECE after  NLL before  NLL after  Brier before  Brier after  F1 before  F1 after  F1 @ fixed 0.5 (no tuning)  tau* (dev-tuned)
M4 BanglaBERT-large    42     2.466      0.1207     0.0846      0.5004     0.3654        0.1368       0.1151     0.8329    0.8329                      0.8230             0.175
M4 BanglaBERT-large  1337     2.831      0.1205     0.0886      0.5374     0.3565        0.1352       0.1107     0.8379    0.8379                      0.8371             0.575
M4 BanglaBERT-large  2026     2.319      0.1089     0.0820      0.4944     0.3672        0.1351       0.1160     0.8243    0.8243                      0.8290             0.792
       M5 XLM-R MIL    42     1.683      0.0639     0.0396      0.5095     0.4687        0.1651       0.1586     0.7353    0.7353                      0.7369             0.499
       M5 XLM-R MIL  1337     1.483      0.0553     0.0348      0.4923     0.4754        0.1650       0.1616     0.7210    0.7210                      0.7185             0.468
       M5 XLM-R MIL  2026     1.809      0.0950     0.0404      0.5337     0.4810        0.1744       0.1636     0.7326    0.7326                      0.7154             0.449

## Split overlap
                                             Measure            Value
                unique questions: train / dev / test 2924 / 619 / 614
                        test questions also in train         0 (0.0%)
                         dev questions also in train         0 (0.0%)
                          test questions also in dev         0 (0.0%)
                test rows whose question is in train         0 (0.0%)
test rows whose answer text (normalised) is in train         0 (0.0%)

## Failures
none