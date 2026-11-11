# Data
No dataset is redistributed in this repository. Download each dataset from its source and check its terms before use.

| Dataset | Used for | Source |
|---|---|---|
| BangHallu (Bhibranti) | Main Bengali benchmark | https://github.com/mayer-doa-coder/Bhibranti (files `data/splits/{train,dev,test}.jsonl`) |
| Olikbochon | External Bengali evaluation (299 labelled rows) | Kaggle competition `bengali-hallucination` (accepting the competition rules is required) |
| BanglaGovRAG | Legal domain shift | https://github.com/shoumya-chy/banglagovrag (`benchmark/benchmark_v1.1.csv`) |
| BD Legal QA | Legal domain shift | https://github.com/m-mahadi/bangladesh-legal-qa |
| RAGTruth (English; Chinese translation) | Source domain of the released detectors | See the RAGTruth and LettuceDetect papers |

**Licences** (checked on 2026-11-11 from each source; not legal advice, re-check before reuse):

| Dataset | What the source states |
|---|---|
| BangHallu (Bhibranti) | The repository's MIT licence covers code only. Its README states the data text derives from Bengali Wikipedia (CC BY-SA 4.0) and from BCS/school question banks whose redistribution terms are unconfirmed (see the repository's `data/SOURCES.md`). Data licence: not settled. |
| Olikbochon | No licence found. It was a private Kaggle competition (IUT CSE Fest 2026); the competition rules are only accessible on Kaggle after joining. Data licence: unknown. |
| BanglaGovRAG | No licence file and no licence statement in the repository. Data licence: unknown (no licence granted by default). |
| BD Legal QA | `LICENSE.md`: the release team's original contributions under CC BY 4.0; quoted Bangladesh statutory text is excluded from the grant. |
| RAGTruth | The ParticleMedia/RAGTruth repository is under MIT. The Chinese translation used for M2: source and licence not recorded. |

This repository redistributes none of their text. It does release hashed example ids and the datasets' gold labels inside `predictions/`.

**Versions:** downloaded in October 2026. Commit hashes were not recorded, and BD Legal QA has been updated since. Row counts per split, and a SHA-256 of each dataset as the notebook built it, are under `datasets` in `results/original_run/experiment_manifest.json`. RAGTruth is loaded from Hugging Face using the candidate ids in the notebook's `HF_CANDIDATES`; which id was used is not recorded in the outputs.

**Placement:** the notebooks run in `work/` (see `docs/reproduce.md`) and read raw data from `work/data/raw/<key>/`, with `<key>` one of `banghallu`, `olikbochon`, `banglagovrag`, `bdlegalqa`, `ragtruth`. When the folder is empty, the original notebook tries to `git clone` the GitHub-hosted datasets and to download Olikbochon with the Kaggle API (needs Kaggle credentials). It writes a unified copy to `work/data/unified/`.

**What the released files contain:** `predictions/*.jsonl` hold a hashed example `id`, the dataset's `gold_label` and the model outputs (`pred_prob`, `pred_label`, `token_probs`, `latency_ms`). They contain no dataset text.
