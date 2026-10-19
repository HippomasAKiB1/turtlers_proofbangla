# ProofBangla: Cross-Lingual Transfer and Domain-Shift Robustness of Hallucination Detection for Bengali Retrieval-Augmented Generation



**Detailed Research Proposal and Experimental Specification**

*Prepared for thesis planning, implementation, and agent-to-agent handoff*

| Item | Decision |
| --- | --- |
| **Research type** | Empirical NLP / trustworthy AI / RAG evaluation

 |
| **Primary language** | Bengali (Bangla), including Banglish/code-switched inputs where available

 |
| **Primary domain** | General RAG hallucination detection, with Bangladesh legal RAG as domain-shift evaluation

 |
| **Primary task** | Hallucination detection; span-level where gold spans exist, answer-level where Bengali benchmark labels are answer-level

 |
| **Core contribution** | Controlled study of English-to-Bengali transfer, multilingual transfer, low-resource Bengali adaptation, and legal-domain robustness

 |
| **Prototype** | ProofBangla: evidence-grounded Bengali RAG with hallucination-risk highlighting

 |
| **Compute** | RTX 5070 Ti 16 GB available to teammate; RTX 4060 8 GB also available; VRAM is not a project constraint

 |
| **Hard execution constraint** | Complete experimental thesis within approximately one week

 |
| **Data constraint** | Use existing datasets only; no new human annotation; no large custom dataset creation

 |

> **Important scope correction:** An earlier version proposed a newly human-annotated Bengali legal span dataset, OCR robustness experiments, and translating RAGTruth into Bengali. Those components are removed from the final one-week plan. The present proposal is intentionally built around existing released datasets and reproducible experiments.
> 
> 

---

## 1. Executive Summary



This thesis studies whether hallucination detectors developed primarily on English RAG data can reliably transfer to Bengali and whether Bengali-specific adaptation improves robustness. The central research problem is not simply whether Bengali language models hallucinate. Bengali hallucination detection already exists at the answer level. The research problem is whether a detector trained for evidence-grounded hallucination detection in one language and domain remains reliable when moved to Bengali, and what happens when the target environment becomes a specialized legal RAG system.

The methodology deliberately separates three questions that are often conflated: (1) cross-lingual transfer, (2) in-language adaptation, and (3) domain shift into Bangladeshi legal RAG. The primary source-domain resource is RAGTruth, which contains RAG responses with token/span-level hallucination annotations. LettuceDetect provides an existing lightweight token-level detector and English/multilingual checkpoints. For Bengali answer-level evaluation, BangHallu provides 4,480 Bengali question pairs / 8,960 answers with human-checked hallucination labels and fixed splits. Olikbochon provides an additional Bengali hallucination evaluation setting. For legal-domain evaluation, BanglaGovRAG provides a frozen benchmark of 100 question-passage pairs with gold evidence spans and 50 out-of-corpus refusal probes.

The thesis will not claim that BangHallu or BanglaGovRAG is a span-level Bengali hallucination benchmark. Instead, it uses each dataset for the task it actually supports. RAGTruth is the controlled span-level source benchmark; BangHallu and Olikbochon are Bengali hallucination classification/generalization benchmarks; BanglaGovRAG is a legal grounding and domain-shift benchmark. This distinction is central to methodological correctness.

---

## 2. Problem Statement



Retrieval-Augmented Generation (RAG) reduces reliance on a model's parametric memory by supplying retrieved evidence, but retrieved evidence does not guarantee a faithful answer. A model may introduce unsupported facts, alter numbers, invent legal references, or combine evidence incorrectly. Hallucination detectors attempt to identify these unsupported claims after generation.

Most fine-grained RAG hallucination work has been developed and evaluated in English or a limited set of other languages. LettuceDetect, for example, performs token-level detection from question, context, and answer, and its released multilingual models cover seven languages: English, German, French, Spanish, Italian, Polish, and Chinese. Bengali is not among those released multilingual model languages. The system can emit exact hallucinated spans and confidence scores.

At the same time, Bengali hallucination evaluation is active. BangHallu is an existing Bengali corpus for hallucination detection, while Olikbochon is a Bengali hallucination detection challenge. These resources make a Bengali evaluation study possible without constructing a new human-annotated corpus.

The remaining scientifically useful question is therefore transfer and robustness: how much performance is lost when a detector crosses languages, how much Bengali supervision recovers, whether multilingual pretraining helps, and whether the resulting detector remains useful when moved into a Bangladesh-specific legal RAG setting.

---

## 3. Research Gap and Novelty Positioning



### 3.1 What is already established



* Bengali hallucination detection exists at the answer/classification level, including BangHallu and Olikbochon.


* Fine-grained RAG hallucination detection is established internationally; LettuceDetect performs token/span-level detection.


* Cross-lingual hallucination-detector transfer and low-resource effects are already recognized research problems.


* Bangladesh-specific legal QA resources now exist, including a 2,165-record bilingual legal QA dataset and the BanglaGovRAG benchmark.



### 3.2 Defensible gap



The thesis should not claim to be the first Bengali hallucination detector, the first cross-lingual hallucination study, or the inventor of a new detector architecture. The defensible contribution is a controlled empirical study of how existing fine-grained RAG hallucination detectors transfer to Bengali, how much Bengali-specific supervision recovers performance, and whether the resulting detector remains robust under Bangladesh-specific legal domain shift.

### 3.3 Claims to avoid



* First Bengali hallucination detector.


* First study showing cross-lingual transfer fails.


* First token-level hallucination detector in the world.


* A novel hallucination-detection architecture.


* A universal Bengali RAG hallucination benchmark.


* Human-verified Bengali legal span annotations, because the final one-week plan does not create them.



### 3.4 Claims that are defensible



* A controlled comparison of English-only, multilingual, and Bengali-adapted hallucination detection for Bengali RAG.


* A low-resource adaptation curve showing how much Bengali supervision is needed to improve transfer.


* Cross-dataset evaluation across Bengali hallucination resources to test robustness beyond a single benchmark.


* A domain-shift evaluation of hallucination/grounding behavior in Bangladesh legal RAG using an existing legal benchmark.


* A reproducible prototype demonstrating how the detector can be integrated into a Bengali evidence-grounded RAG system.



---

## 4. Research Objectives



1. Measure zero-shot transfer of an English RAG hallucination detector to Bengali.


2. Measure whether multilingual pretraining improves transfer to Bengali.


3. Quantify the benefit of Bengali-specific adaptation under low-resource conditions.


4. Test whether Bengali-adapted detection generalizes to an independent Bengali hallucination benchmark.


5. Evaluate behavior under Bangladesh legal-domain shift without pretending that the legal benchmark supplies human hallucination-span labels.


6. Separate retrieval/evidence availability problems from answer-level hallucination detection wherever the available benchmark permits.


7. Build a lightweight ProofBangla prototype that visualizes evidence and hallucination risk.


8. Produce fully reproducible notebooks, configurations, seeds, metrics, and experiment manifests.



---

## 5. Research Questions and Hypotheses



| ID | Research question | Hypothesis / expected observation |
| --- | --- | --- |
| **RQ1** | How effectively does an English-trained RAG hallucination detector transfer to Bengali?

 | Performance will degrade relative to its source-domain performance; the size of the degradation is itself a result.

 |
| **RQ2** | Does multilingual pretraining improve Bengali transfer compared with English-only training?

 | The multilingual model should transfer better than an English-only detector, but Bengali-specific weaknesses may remain.

 |
| **RQ3** | How much Bengali supervision is needed to recover performance?

 | A small fraction of Bengali training data should produce a measurable improvement, with diminishing returns as supervision increases.

 |
| **RQ4** | Does Bengali adaptation generalize across Bengali datasets?

 | A model tuned on one Bengali benchmark should improve on a held-out or external Bengali distribution, but gains may not transfer perfectly.

 |
| **RQ5** | Does the detector remain reliable under Bangladesh legal-domain shift?

 | General Bengali performance will not fully predict legal-domain performance; legal terminology, section references, and evidence structure can expose additional failure modes.

 |
| **RQ6** | What is the accuracy-efficiency trade-off between an encoder detector and an optional small LLM verifier (or weakly supervised MIL token detector)?

 | The encoder should be substantially faster and cheaper at inference, while potentially providing competitive detection performance.

 |

---

## 6. Dataset and Resource Specification



### 6.1 RAGTruth: source-domain span-level benchmark



RAGTruth is the primary source-domain resource because it provides RAG-generated responses and fine-grained hallucination annotations. It is used to reproduce/verify source-domain detector behavior and to train or reuse a span-level detector. It is not assumed to be Bengali.

* **Role:** Source-domain training and span-level validation.


* **Labels:** Token/span-level hallucination annotations.


* **Primary output:** Token/span precision, recall, and F1.


* **Methodological rule:** Keep its original train/test separation intact.



### 6.2 LettuceDetect: detector baseline and implementation reference



LettuceDetect is a lightweight token-level RAG hallucination detector. It takes question, context, and answer as input and predicts hallucination probabilities for answer tokens, which can be converted into spans. Its public repository provides English ModernBERT models and multilingual EuroBERT models for seven languages. Bengali is not among those released training languages. Therefore, Bengali results must be described as transfer/adaptation experiments, not as use of a Bengali-trained LettuceDetect checkpoint. The detector should first be sanity-checked on RAGTruth before any cross-lingual inference.

### 6.3 BangHallu: Bengali answer-level benchmark



BangHallu is an existing Bengali question-answer hallucination corpus containing 4,480 question pairs and 8,960 answers. Each question has a correct and a hallucinated answer; the project reports human checking and Cohen's kappa of 0.865. The repository also provides fixed train/dev/test splits and an evaluation ladder.

* **Role:** Bengali supervised adaptation and answer-level evaluation.


* **Critical limitation:** Do not call it a span-level hallucination dataset.


* **Protocol:** Use its fixed splits and follow its leakage safeguards. Check the repository's data licensing/redistribution notice before redistributing raw data.



### 6.4 Olikbochon: independent Bengali evaluation



Olikbochon is an official Bengali hallucination detection challenge. It is useful as an external Bengali evaluation environment. Its competition rules emphasize reproducible open-weight inference and code-compliant execution.

* **Role:** External Bengali generalization test.


* **Critical limitation:** Do not treat it as a span-level benchmark unless the exact released data explicitly contains span labels.



### 6.5 BanglaGovRAG: Bangladesh legal/domain-shift benchmark



BanglaGovRAG provides a frozen benchmark of 100 question-passage pairs: 40 Bengali, 32 code-switched, and 28 English, covering seven question types. It provides gold evidence spans and source URLs, plus 50 out-of-corpus refusal probes with annotator judgments. Its repository also contains retrieval, generation, judging, agreement, and statistical evaluation code. Its gold evidence spans must not be relabeled as hallucinated-answer spans. The benchmark is therefore used for legal grounding, retrieval/domain-shift analysis, and refusal behavior, with separate gold-evidence and retrieved-evidence conditions.

* **Role:** Legal grounding/domain-shift evaluation.


* **Critical limitation:** Gold spans are evidence/retrieval annotations, not automatically hallucinated-answer spans.


* **Protocol:** Use the benchmark to test evidence retrieval, groundedness, refusal behavior, and detector behavior where outputs permit.



### 6.6 Bangladesh Legal QA dataset: complementary legal resource



A separate 2026 Bangladesh Legal QA release contains 2,165 context-grounded bilingual QA records, with 1,211 Bangla and 954 English examples, covering six Acts and three schedules. The associated study explicitly separates retrieval/scoring/model effects. This resource can be used for legal-domain adaptation, retrieval testing, or controlled legal QA experiments if its exact record schema is useful.

| Resource | Language | Label type | Primary role | Do not claim |
| --- | --- | --- | --- | --- |
| **RAGTruth** | English

 | Token/span hallucination

 | Source-domain training + span evaluation

 | Bengali benchmark

 |
| **LettuceDetect** | English + 7 multilingual languages

 | Token/span prediction

 | Existing detector/checkpoints

 | Bengali pretrained checkpoint

 |
| **BangHallu** | Bengali

 | Answer-level hallucination

 | Bengali adaptation + evaluation

 | Span-level ground truth

 |
| **Olikbochon** | Bengali

 | Hallucination challenge labels

 | External Bengali evaluation

 | Span-level labels unless verified

 |
| **BanglaGovRAG** | BN / code-switched / EN

 | Gold evidence spans + refusal judgments

 | Legal grounding/domain shift

 | Hallucination-span benchmark

 |
| **BD Legal QA** | Bangla + English

 | Context-grounded QA

 | Legal adaptation/retrieval control

 | Hallucination annotations

 |

---

## 7. Final Experimental Design



The study follows a controlled progression. Each stage answers one research question and prevents language transfer, Bengali adaptation, and legal domain shift from being mixed into one uncontrolled comparison.

### Experiment A: Dataset and schema audit



Before model training, inspect every candidate dataset and record: available fields, context availability, label granularity, official splits, language distribution, license, duplicate structure, and which metrics the labels actually support. Create a nullable unified schema without inventing missing fields. If a dataset has no context, it must not be presented as a RAG hallucination benchmark.

* **Required unified JSONL audit fields:** `id`, `dataset`, `split`, `question`, `context`, `answer`, `label_answer`, `label_spans`, `evidence_spans`, `source_url`, and `metadata`. Missing fields remain `null`. This audit is a hard gate for the rest of the project.


* **Tokenizer fertility and truncation audit:** For every model (`ModernBERT`, `EuroBERT`, `XLM-R-base`, `BanglaBERT-large`), compute and report: tokens per word, maximum sequence length, percentage of examples truncated, and percentage of answer tokens truncated.


* **Context-only truncation rule (Critical for 512-token encoders):** Because `BanglaBERT-large` and `XLM-R-base` have a hard maximum length of 512 tokens, preprocessing must allocate token budget to `[CLS] question [SEP]` and `[SEP] answer [SEP]` first, truncating only the `context` tokens to fit within `max_seq_length` so that `answer` tokens are never silently truncated.

### Experiment B: Source-domain sanity check



Run the released LettuceDetect checkpoint on RAGTruth and verify token-level and span-level evaluation against the dataset's available ground truth. Record checkpoint, tokenizer, maximum sequence length, threshold, library versions, and seed. This confirms the implementation before Bengali transfer is attempted.

### Experiment C: English-to-Bengali transfer



Use the English LettuceDetect checkpoint as a zero-shot transfer baseline only when the target example contains the required question/context/answer fields. Do not force context-free Bengali datasets into a RAG formulation. When Bengali labels are answer-level, aggregate token probabilities to one answer score instead of pretending span ground truth exists.

* **Primary pooling rule:** $S_{\text{answer}} = \max_i p_i$ over answer tokens. Select the decision threshold only on the Bengali development split, then freeze it for test evaluation. Report top-$k$ mean pooling ($k=3,5$) only as a secondary sensitivity analysis if time permits.



### Experiment D: Multilingual transfer



Run the released multilingual EuroBERT/LettuceDetect checkpoint under the same schema and pooling protocol. Bengali is outside its released seven-language training coverage, so the comparison tests out-of-language transfer rather than claiming Bengali support. Compare English-only and multilingual transfer under identical preprocessing, truncation rules, thresholds, and evaluation splits. Attribute differences cautiously to multilingual pretraining rather than claiming universal multilingual superiority.

### Experiment E: Bengali adaptation



Train `xlm-roberta-base` and `csebuetnlp/banglabert_large` as answer-level sequence classifiers on BangHallu. The primary input is `[CLS] question [SEP] context [SEP] answer [SEP]` when context exists; for context-free Bengali hallucination datasets, use `[CLS] question [SEP] answer [SEP]` and explicitly label the task as general hallucination classification rather than RAG hallucination detection.

* **`BanglaBERT-large` normalization:** Apply the official `normalizer` pipeline (`buetnlpnormalizer`) before tokenization for `BanglaBERT-large`. `XLM-R-base` serves as the multilingual comparison model.


* **Low-resource supervision curve:** Train on 0%, 10%, 25%, and 100% of the official BangHallu training split (if compute is abundant, optionally add 5% and 50%). For each fraction, sample deterministically from the official training split (keeping paired correct/hallucinated variants together), keep development/test sets untouched, and select the threshold/checkpoint using development performance only.



| Training fraction | Purpose |
| --- | --- |
| **0%** | Zero-shot / no Bengali supervision baseline

 |
| **10%** | Low-resource adaptation

 |
| **25%** | Moderate adaptation

 |
| **100%** | Full available supervision

 |

### Experiment F: Independent Bengali generalization



Freeze the best Bengali-adapted checkpoint selected on BangHallu development data and evaluate on Olikbochon or another independent Bengali evaluation resource. Do not tune on its test labels. Report the generalization gap and error categories. If Olikbochon lacks the context fields required by LettuceDetect, use it only for answer-level Bengali generalization and do not report its score as span-level RAG hallucination detection.

### Experiment G: Bangladesh legal domain shift



Use BanglaGovRAG (and optionally the Bangladesh Legal QA dataset) as a legal grounding/domain-shift benchmark. Evaluate two conditions where feasible: (1) gold evidence supplied, isolating generation/detector behavior from retrieval failure; and (2) retrieved evidence, measuring the full pipeline.

* Keep retrieval quality, answer groundedness, refusal behavior, and detector behavior as separate outcomes. Gold evidence spans are evidence annotations, not hallucinated-answer spans.


* Report retrieval failures separately from detector failures. If the correct passage was never retrieved, the detector should not be blamed for the resulting unsupported answer; if correct evidence was supplied and unsupported content remains, that is a meaningful grounding/detection failure.


* If a controlled detector classification stress test is added, create synthetic legal perturbations (e.g., negative context pairing or rule-based section/number swaps) only as a secondary experiment. Label them explicitly as synthetic and never present them as human-ground-truth legal hallucination annotations.



### Experiment H: Prototype validation



Use the final frozen detector inside ProofBangla only after the research experiments are frozen. The prototype demonstrates the practical workflow (`question -> retriever -> evidence -> generator -> detector -> highlighted answer`) but does not create a new evaluation set or change the thesis metrics.

---

## 8. Model Matrix



| ID | System | Training / setup | Question answered |
| --- | --- | --- | --- |
| **M0** | Lexical evidence baseline

 | No training; evidence-answer overlap / containment

 | How far can simple lexical evidence checks go?

 |
| **M1** | English LettuceDetect

 | Released English checkpoint (`ModernBERT`)

 | How much performance survives English-to-Bengali transfer?

 |
| **M2** | Multilingual LettuceDetect

 | Released multilingual `EuroBERT` checkpoint

 | Does multilingual pretraining improve transfer?

 |
| **M3** | `XLM-R-base` classifier

 | Sequence classification on BangHallu (0/10/25/100%)

 | What does multilingual in-language supervision achieve?

 |
| **M4** | `BanglaBERT-large` classifier

 | Sequence classification on BangHallu (0/10/25/100%)

 | How much Bengali-specific supervision is needed, and does a Bengali-oriented encoder help?

 |
| **M5** | Optional MIL token detector

 | Answer-level BangHallu labels used as weak supervision via max-pooled token loss

 | Can answer-level supervision be converted into fine-grained localization without new annotation?

 |
| **M6** | Optional Small LLM verifier

 | Frozen 3B-class open-weight model + zero-shot prompt

 | How does a generative LLM verifier compare with an encoder on accuracy vs. latency?

 |

*Note:* **M5** and **M6** are strictly optional. If time becomes tight, drop M6 and M5 before dropping the low-resource curve, external evaluation, or legal-domain analysis. The core thesis is about transfer and adaptation (M0–M4), not about winning against a large LLM.

---

## 9. Data Leakage and Reproducibility Protocol



* Use official fixed train/dev/test splits whenever a dataset provides them.


* Never select checkpoints or thresholds using the final test set.


* Keep every question-answer pair and its paired correct/hallucinated variants in the same split.


* Check exact and near-duplicate questions across train/dev/test.


* Record dataset version, commit hash, file hash, model revision, tokenizer revision, and preprocessing configuration.


* Save raw predictions (JSONL/Parquet), not only final metrics.


* Run at least three seeds (`42, 1337, 2026`) for the final trainable model when time permits; if the one-week budget prevents this on intermediate fractions, explicitly report the limitation.


* Use deterministic preprocessing and fixed random seeds.


* Keep an experiment manifest so another agent can reproduce every reported table from saved prediction files.



---

## 10. Evaluation Metrics



| Metric | Use |
| --- | --- |
| **Macro-F1** | Primary answer-level metric for Bengali hallucination classification.

 |
| **Precision / Recall** | Identify false-positive control versus missed hallucinations.

 |
| **AUROC / AUPRC** | Threshold-independent and imbalance-aware diagnostics where scores are available.

 |
| **Token F1** | Primary fine-grained metric on RAGTruth.

 |
| **Span F1** | Hallucination localization metric only where gold hallucination spans exist.

 |
| **Answer score pooling** | Primary: $\max_i p_i$ answer-token probability; secondary: top-$k$ mean for $k=3,5$ if time permits.

 |
| **Calibration / ECE** | Tests whether detector confidence corresponds to actual correctness.

 |
| **Coverage / risk-coverage** | Measures practical selective detection and threshold behavior.

 |
| **Latency / memory** | Measures deployment cost of the detector (ms/example, peak VRAM MB).

 |

> **Rule:** Do not use token accuracy as the headline metric. Supported tokens usually dominate the sequence, so a trivial classifier can obtain deceptively high token accuracy.
> 
> 

---

## 11. Statistical Analysis



* Report mean $\pm$ standard deviation across seeds for trainable models.


* Use paired bootstrap confidence intervals (1,000 resamples) for the final metrics.


* Use paired tests when the same examples are scored by two detectors.


* Use McNemar's test for paired binary classification comparisons where appropriate.


* For multiple pairwise comparisons, apply Holm-Bonferroni correction.


* Report effect sizes and confidence intervals, not only $p$-values.


* Do not run significance tests repeatedly until a favorable result appears.



---

## 12. Ablation Plan



| Ablation | Variants | Purpose |
| --- | --- | --- |
| **Language supervision** | 0 / 10 / 25 / 100%

 | Measure the low-resource effect.

 |
| **Model family** | English / multilingual / XLM-R / BanglaBERT

 | Separate transfer from in-language encoder choice.

 |
| **Pooling** | $\max$ / top-$k$ mean ($3,5$)

 | Test whether answer aggregation changes Bengali classification results.

 |
| **Tokenizer / truncation** | Model-specific audit

 | Measure Bengali tokenization and truncation effects rather than assuming them.

 |
| **Evidence condition** | Gold evidence / retrieved evidence

 | Separate detector behavior from retrieval failure in legal RAG.

 |
| **Domain** | General Bengali / legal Bengali

 | Measure domain shift.

 |

Do not run every ablation if it threatens the one-week deadline. The must-have ablations are the Bengali supervision curve and English-versus-multilingual transfer. Legal and input/evidence ablations are second priority.

---

## 13. Error Analysis



Sample 50–100 errors from the held-out evaluation data and categorize them. The categories must be defined before looking at results:

1. Numerical mismatch or fabricated number.


2. Wrong legal section / act / clause.


3. Entity substitution.


4. Unsupported causal or explanatory statement.


5. Correct fact expressed with an unsupported modifier.


6. Code-switching or transliteration mismatch.


7. Evidence retrieval failure.


8. Detector false positive on a supported claim.


9. Detector false negative on an unsupported claim.


10. Ambiguous or insufficient evidence.



*(Note: For rapid annotation on Day 5, these 10 fine-grained tags can also be grouped into 5 macro-buckets: Numerical/Section error, Entity error, Unsupported claim/modifier, Code-switching/Retrieval artifact, and Detector False Positive/Negative.)*

---

## 14. ProofBangla Prototype



The prototype is a demonstration layer for the research, not the primary scientific contribution. Cap implementation at approximately three focused hours on Day 6.

```text
Question -> Retriever -> Legal / general evidence -> Frozen small generator -> Generated answer -> Hallucination detector -> Token/span/answer risk scores -> Highlighted answer + evidence panel

```

### 14.1 User experience



* User enters a Bengali or Banglish question.


* System retrieves evidence.


* A small open-weight generator creates an answer.


* Detector scores answer tokens/spans (or sentence/answer risk).


* UI highlights high-risk unsupported text.


* Evidence panel displays the source passage.


* System displays a caution/abstention message when confidence is low.



### 14.2 Suggested implementation



Streamlit is the default one-week choice. The prototype must use frozen retrieval/generation/detector components and must not introduce a new manually labeled evaluation set.

| Component | Recommended choice |
| --- | --- |
| **Backend / UI** | Streamlit single-app (or FastAPI + Streamlit if decoupled)

 |
| **Retrieval** | BM25 + multilingual embedding retrieval; use existing legal corpus

 |
| **Vector store** | FAISS or Chroma

 |
| **Generator** | Small quantized open-weight model, inference only

 |
| **Detector** | LettuceDetect or fine-tuned `BanglaBERT-large` / `XLM-R-base`<br> |
| **Storage** | Simple JSON/SQLite

 |

---

## 15. Compute and Hardware Plan



| Task | Recommended hardware | Notes |
| --- | --- | --- |
| **Encoder fine-tuning** | RTX 5070 Ti 16 GB

 | Primary training machine (`BanglaBERT-large`, `XLM-R-base`).

 |
| **Secondary training/inference** | RTX 4060 8 GB

 | Useful for parallel zero-shot transfer runs and evaluation scripts.

 |
| **Small LLM inference** | RTX 5070 Ti 16 GB

 | Use 4-bit quantization if needed for RAG generation or optional M6.

 |
| **Data preprocessing** | CPU

 | Tokenization, normalization, filtering, deduplication.

 |
| **Retrieval** | CPU/GPU

 | BM25 on CPU; dense embeddings on GPU.

 |

---

## 16. One-Week Execution Plan



| Day | Primary objective | Concrete deliverable | Stop condition |
| --- | --- | --- | --- |
| **Day 1** | Dataset/schema + tokenizer audit

 | Load candidate datasets; write unified JSONL schema; verify licenses/splits/context/labels; run tokenizer fertility & truncation audit; freeze manifest.

 | Any dataset failing schema/licensing/metric support is removed from the critical path.

 |
| **Day 2** | Source-domain + transfer

 | RAGTruth/LettuceDetect sanity check; English and multilingual transfer with fixed pooling protocol.

 | Do not spend the day tuning zero-shot transfer.

 |
| **Day 3** | Bengali adaptation

 | BangHallu preprocessing; `XLM-R-base` and `BanglaBERT-large` runs at 0/10/25/100%.

 | If training is slow, reduce seeds on intermediate fractions; do not create data.

 |
| **Day 4** | Independent Bengali + legal setup

 | Olikbochon evaluation; BanglaGovRAG gold/retrieved evidence conditions; legal schema integration.

 | Legal data is used only for supported grounding/domain-shift analyses.

 |
| **Day 5** | Core analysis

 | Threshold selection audit, calibration, bootstrap CIs, paired comparisons, error categories, transfer/domain tables.

 | Freeze models and thresholds after analysis setup.

 |
| **Day 6** | ProofBangla prototype

 | Minimal Streamlit demo: `question -> evidence -> answer -> detector -> highlighted risk`.

 | Hard cap of about 3 hours; stop before prototype work threatens results.

 |
| **Day 7** | Reproducibility + thesis results

 | Final notebooks, machine-readable predictions, tables, figures, limitations, methods/results narrative.

 | No new experiments unless a critical implementation bug invalidates a result.

 |

---

## 17. Priority System for the One-Week Deadline



If time runs short, items must be dropped in this exact order:

1. Drop custom frontend polish (use standard Streamlit).


2. Drop optional M6 (Small LLM verifier) and M5 (MIL token detector).


3. Drop secondary ablations (e.g., top-$k$ pooling variants).


4. Reduce the low-resource curve to `0% / 10% / 100%`.


5. **Keep** English vs. multilingual transfer (Experiments B, C, D).


6. **Keep** Bengali adaptation (Experiment E).


7. **Keep** independent Bengali evaluation (Experiment F).


8. **Keep** legal domain-shift analysis if the existing benchmark loads cleanly (Experiment G).


9. **Keep** leakage audit, confidence intervals, and reproducibility artifacts.



---

## 18. Expected Results and Interpretation Rules



| Observed result | Interpretation |
| --- | --- |
| **Multilingual > English transfer** | Evidence that multilingual pretraining improves cross-lingual transfer.

 |
| **Bengali adaptation > multilingual** | Evidence that in-language supervision adds value.

 |
| **Small-data adaptation closes most of the gap** | Evidence of efficient low-resource adaptation.

 |
| **Full-data adaptation barely beats 10%** | Diminishing returns; useful practical finding.

 |
| **Bengali adaptation wins on BangHallu but loses on Olikbochon** | Likely dataset/domain overfitting; investigate error types.

 |
| **Legal performance drops despite Bengali gains** | Evidence of domain shift.

 |
| **Legal performance improves without legal training** | Evidence that the learned detector transfers better than expected.

 |
| **Optional LLM verifier wins accuracy but is much slower** | Accuracy-efficiency trade-off rather than simple winner/loser.

 |
| **No meaningful adaptation gain** | Valid negative result; investigate label/task mismatch, domain shift, or model capacity.

 |

---

## 19. Threats to Validity and Limitations



* Bengali hallucination benchmarks are not necessarily RAG-specific or span-level. Results must be reported at the correct label granularity, and context-free datasets must be described as general hallucination classification rather than RAG hallucination detection.


* BanglaGovRAG is small (100 question-passage pairs) and should be treated as a legal stress test, not a universal legal benchmark. Its evidence spans cannot be treated as hallucinated-answer spans without additional ground truth.


* LettuceDetect's released multilingual checkpoints do not include Bengali, so Bengali transfer is genuinely out-of-language for those checkpoints. Tokenization and truncation behavior must be measured rather than assumed.


* Standard Bengali encoders (`BanglaBERT-large`, `XLM-R-base`) have a 512-token context limit, requiring context-only truncation on long passages.
* Synthetic legal perturbations can be useful for controlled stress testing but contain artifacts and must remain secondary to natural benchmark evaluation.


* A legal-domain benchmark may reflect retrieval quality as much as hallucination detection quality; gold-evidence and retrieved-evidence conditions must be separated.


* One-week experimentation limits the number of seeds, model families, and robustness tests that can be run.


* The prototype is not a legal advice system and must include a clear disclaimer; the thesis evaluates AI reliability and grounding behavior, not legal correctness for real users.



---

## 20. Reproducibility Package



The final repository must follow this exact directory structure:

```text
proofbangla/
├── README.md
├── limitations.md
├── configs/
│   ├── datasets.yaml
│   ├── models.yaml
│   └── experiments.yaml
├── data/
│   ├── raw/
│   ├── unified/
│   └── README.md
├── notebooks/
│   ├── 01_dataset_audit.ipynb
│   ├── 02_source_domain.ipynb
│   ├── 03_transfer.ipynb
│   ├── 04_bengali_adaptation.ipynb
│   ├── 05_external_eval.ipynb
│   ├── 06_legal_shift.ipynb
│   └── 07_final_analysis.ipynb
├── src/
│   ├── preprocessing/
│   ├── models/
│   ├── evaluation/
│   ├── statistics/
│   └── prototype/
├── predictions/
├── results/
├── figures/
├── tables/
└── app/

```

---

## 21. Agent Handoff Specification (Hard Constraints for Coding Agent)



Any coding/research agent generating the experiment notebooks must obey these exact rules and never silently alter them:

| Rule | Instruction |
| --- | --- |
| **Research goal** | Study cross-lingual transfer, Bengali adaptation, and legal-domain robustness of hallucination detection.

 |
| **Time & Data** | 7-day execution. Existing datasets only; no new human annotation and no large custom dataset creation.

 |
| **Schema audit (`01_dataset_audit.ipynb`)** | Before training, convert all datasets into the unified JSONL format (`id, dataset, split, question, context, answer, label_answer, label_spans, evidence_spans, source_url, metadata`) and output `results/schema_audit.json`.

 |
| **Tokenizer & Truncation audit** | Compute tokens/word, max length, % examples truncated, and % answer tokens truncated for all models. Enforce **context-only truncation** so `answer` tokens are never cut off at the 512-token limit.

 |
| **Span vs. Answer labels** | Use span-level metrics only on RAGTruth (or where gold hallucination spans exist). BangHallu/Olikbochon are answer-level unless the exact schema proves otherwise.

 |
| **RAG claim** | If `context` is null/absent in a dataset, format input as `[CLS] question [SEP] answer [SEP]` and log the task as `general_hallucination_classification`, not `rag_hallucination_detection`.

 |
| **Pooling rule** | For token-level models (LettuceDetect) evaluated on answer-level labels, compute $S_{\text{answer}} = \max_i p_i$ over answer tokens. Tune the binary threshold on `dev` only and freeze on `test`.

 |
| **Models** | Use `ModernBERT` (English LettuceDetect), `EuroBERT` (Multilingual LettuceDetect), `xlm-roberta-base`, and `csebuetnlp/banglabert_large` (with `buetnlpnormalizer` applied).

 |
| **Legal conditions** | BanglaGovRAG gold spans are evidence spans, not hallucinated-answer spans. Evaluate gold-evidence and retrieved-evidence conditions separately. Label any synthetic legal perturbations explicitly as secondary stress tests.

 |
| **Statistics** | Save raw predictions per example to `predictions/<exp_id>_<model>_<seed>.jsonl`. Compute paired bootstrap 95% CIs, McNemar's test, and Holm-Bonferroni correction in `07_final_analysis.ipynb`.

 |

---

## 22. Final Research Contribution



The thesis tells one coherent story:

```text
English RAG hallucination detector
            ↓
   cross-lingual transfer
            ↓
         Bengali
            ↓
  low-resource adaptation
            ↓
independent Bengali evaluation
            ↓
     legal domain shift
            ↓
   ProofBangla prototype

```

The central contribution is not a new neural architecture. It is the controlled empirical evidence showing how hallucination detection changes across language and domain boundaries, how much Bengali supervision is required, and whether the resulting detector remains useful in a Bangladesh legal RAG environment.

---

## 23. References and Verification Sources



* **LettuceDetect repository:** `[https://github.com/KRLabsOrg/LettuceDetect](https://github.com/KRLabsOrg/LettuceDetect)` (or mirror `[https://github.com/stelin41/LettuceDetect](https://github.com/stelin41/LettuceDetect)`) — Existing token-level RAG hallucination detector; RAGTruth-based; English ModernBERT and multilingual EuroBERT checkpoints; seven multilingual languages.


* **BangHallu / Bhibranti repository:** `[https://github.com/mayer-doa-coder/Bhibranti](https://github.com/mayer-doa-coder/Bhibranti)` — Bengali hallucination corpus with 4,480 question pairs / 8,960 answers, fixed splits, annotation/agreement documentation.


* **BanglaGovRAG repository:** `[https://github.com/shoumya-chy/banglagovrag](https://github.com/shoumya-chy/banglagovrag)` — Frozen legal/admin benchmark: 100 question-passage pairs, gold evidence spans, code-switched subset, refusal probes, evaluation harness.


* **Bangladesh Legal QA dataset:** `[https://huggingface.co/datasets/momahadi/bangladesh-legal-qa-dataset](https://huggingface.co/datasets/momahadi/bangladesh-legal-qa-dataset)` — 2,165 context-grounded bilingual legal QA records; six Acts and three schedules.


* **Bangladesh Legal QA code & paper artifacts:** `[https://github.com/m-mahadi/bangladesh-legal-qa](https://github.com/m-mahadi/bangladesh-legal-qa)` — Frozen protocol, statutory corpus, QA records, benchmark runs, and analysis code emphasizing separation of scoring, retrieval, and model/context-use effects (verify exact citation/DOI directly from the repository `CITATION.cff` or `README.md`).


* **Olikbochon Kaggle rules:** `[https://www.kaggle.com/competitions/bengali-hallucination/rules](https://www.kaggle.com/competitions/bengali-hallucination/rules)` — Official Bengali hallucination detection challenge rules and reproducibility constraints.



---

## 24. Verification Notes for Future Agents



Before any model training begins, the coding agent must execute `01_dataset_audit.ipynb` to run the dataset schema audit and tokenizer audit. The schema audit must record available fields, label granularity, train/dev/test split, license, language distribution, context availability, and whether the labels support the intended metric. The tokenizer audit must record tokens per word, maximum sequence length, example truncation rate, and answer-token truncation rate (verifying 0% answer truncation after context-only truncation is applied). If a dataset fails the audit, it must be removed from the critical path rather than forcing the research question to fit the dataset.