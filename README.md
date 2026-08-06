# Research Proposal

## Bengali-MMRAG: Multimodal Retrieval-Augmented Generation for Complex Bangla Form Comprehension

---

### 1. Executive Summary

| Aspect | Description |
| :--- | :--- |
| **Proposed Title** | Bengali-MMRAG: Multimodal Retrieval-Augmented Generation for Complex Bangla Form Comprehension |
| **Research Domain** | Natural Language Processing, Computer Vision, Multimodal AI, Low-Resource Languages |
| **Core Problem** | Visually-rich Bengali documents (government forms, official records) cannot be effectively understood by current RAG systems due to lack of multimodal benchmarks, brittle OCR, and scarce annotated data for low-resource languages |
| **Proposed Solution** | A novel Multimodal RAG framework that combines layout-aware visual encoding, cross-lingual retrieval, and Bengali-specific generation for document question answering, evaluated on the BaFCo benchmark |
| **Primary Dataset** | **BaFCo** – A Document Understanding Benchmark for Complex Bangla Form Comprehension (ECCV 2026) |
| **Key Novelty** | First Bengali-specific Multimodal RAG system evaluated on BaFCo; first systematic comparison of retrieval strategies (text-only, visual-only, hybrid) for Bengali visually-rich documents; novel layout-aware fusion mechanism |
| **Feasibility** | 6-8 months; leverages existing tools (Gemma 4 Vision, LangChain, ChromaDB, FastAPI); builds directly on your Borno, Utopia, and LangLens projects |
| **Publication Potential** | ACL/EMNLP/NAACL (NLP), ECCV/CVPR (Vision), or LREC/COLING (Low-resource languages) |

---

### 2. Introduction & Motivation

Retrieval-Augmented Generation (RAG) has emerged as a powerful paradigm for grounding Large Language Models (LLMs) in external knowledge, enabling accurate and verifiable question answering. However, the vast majority of RAG research has focused on high-resource languages like English, leaving low-resource languages—spoken by billions of people—behind.

Simultaneously, visually-rich documents (VRDs)—such as scanned forms, reports, and handwritten notes—present a unique challenge for RAG systems. Traditional approaches that rely on Optical Character Recognition (OCR) for text extraction are brittle, losing critical layout and structural information. Recent work on Visual Document RAG (ViDoRAG, EMNLP 2025; VDocRAG, CVPR 2025) has demonstrated the value of preserving visual modalities. ViDoRAG employs a Gaussian Mixture Model (GMM)-based hybrid strategy to effectively handle multi-modal retrieval, while VDocRAG directly understands varied documents in a unified image format to prevent information loss from OCR parsing.

**The research gap is clear:** These systems are overwhelmingly designed for English or high-resource languages. There exists no systematic study of Multimodal RAG for visually-rich documents in Bengali, a language spoken by over 230 million people worldwide.

To address this gap, I propose **Bengali-MMRAG**, the first Multimodal RAG framework specifically designed for visually-rich Bengali documents, evaluated on the **BaFCo** benchmark—a curated dataset of 200 complex multi-page Bangladeshi government forms across 316 pages and 15 domains, with manual annotations for Document Layout Analysis (DLA) and Key Information Extraction (KIE).

---

### 3. Literature Review

#### 3.1 Multimodal Retrieval-Augmented Generation

Multimodal RAG has emerged as a major research direction:

- **ViDoRAG** (EMNLP 2025): Visual Document Retrieval-Augmented Generation via Dynamic Iterative Reasoning Agents. Uses a Gaussian Mixture Model (GMM)-based hybrid strategy for multi-modal retrieval.

- **VDocRAG** (CVPR 2025): Retrieval-Augmented Generation over Visually-Rich Documents. Directly understands documents in a unified image format to prevent information loss from OCR parsing.

However, these systems are exclusively designed for English documents and evaluated on English benchmarks.

#### 3.2 RAG for Low-Resource Languages

Recent work has begun exploring RAG for low-resource settings:

- **TraSe** (ACL Anthology): Enhances RAG for Bangla using translative prompting, achieving 34% with automatic retrieval and 63% with Human-in-the-Loop retrieval.

- **Enhancing Bangla Language Model Through Translation-Free Hybrid RAG**: Utilizes a dataset of 177K+ articles from Bangla Wikipedia with parallel retrieval (Dense and BM25) followed by RRF fusion.

- **Bangla-RAG-Pipeline**: A lightweight multilingual RAG pipeline for Bangla + English questions over Bangla PDFs using OCR-based text extraction, Bangla-BERT embeddings, and FAISS vector search.

- **LR-MMQA** (NeurIPS 2025): Introduces a benchmark for multimodal multilingual retrieval and reasoning in low-resource languages like Tamil and Yoruba, revealing "significant weaknesses in cross-lingual retrieval, multi-hop reasoning, and answer synthesis".

**Critically, none of these studies focus on Bengali visually-rich documents or multimodal document QA.**

#### 3.3 Bengali Document Understanding

Recent advances in Bengali document analysis include:

- **BaFCo** (ECCV 2026): A Document Understanding Benchmark for Complex Bangla Form Comprehension. Curates 200 complex multi-page government forms across 316 pages and 15 domains, with 16,382 layout entities across 26 entity types and 1,926 key-value pairs for KIE. Evaluates the latest MLLMs from ChatGPT, Gemini, Claude, Qwen, and Kimi series using zero-shot and chain-of-thought prompts.

- **Khondo**: A multimodal benchmark for document packet splitting on Bangladeshi government forms, comprising 1,950 bilingual document packets across 14 administrative domains. It is bilingual (Bangla-English) and vision-native, where models operate directly on page images.

- **NCTB-QA**: A large-scale Bangla educational question answering dataset comprising 87,805 question-answer pairs extracted from 50 textbooks published by Bangladesh's National Curriculum and Textbook Board.

- **BaDLAD**: A large multi-domain Bengali Document Layout Analysis dataset with 33,695 human-annotated document samples from six domains.

While these works provide foundational tools, **none integrate these capabilities into a RAG framework for document question answering.**

#### 3.4 Research Gap Summary

| Gap | Evidence |
| :--- | :--- |
| No Bengali-specific Multimodal RAG | All VRD-RAG systems (ViDoRAG, VDocRAG) are English-only |
| No benchmark for Bengali multimodal document QA with RAG | BaFCo provides DLA/KIE annotations but no RAG evaluation |
| No systematic comparison of retrieval strategies for Bengali VRDs | Text-only vs. visual-only vs. hybrid retrieval unexplored |
| No evaluation of RAG for Bengali visually-rich documents | Existing Bengali RAG systems are text-only (PDFs, Wikipedia) |

---

### 4. Problem Statement & Research Questions

**Primary Research Question:**

*How can a Multimodal Retrieval-Augmented Generation system be designed to effectively answer questions over visually-rich Bengali documents, as represented by the BaFCo benchmark?*

**Sub-Questions:**

1. **RQ1**: What is the optimal retrieval strategy for Bengali VRDs—text-based (OCR), visual-based (image embeddings), or hybrid (both)?

2. **RQ2**: How can layout information from BaFCo's DLA annotations be effectively encoded and integrated into the retrieval and generation pipeline?

3. **RQ3**: How does Multimodal RAG performance on Bengali VRDs compare to text-only RAG baselines and zero-shot MLLM performance reported in the BaFCo paper?

4. **RQ4**: Can a lightweight, CPU-friendly Multimodal RAG system achieve competitive performance on Bengali document QA without requiring large-scale GPU infrastructure?

---

### 5. Proposed Methodology

#### 5.1 Dataset: BaFCo

**BaFCo** (A Document Understanding Benchmark for Complex Bangla Form Comprehension) is the primary dataset for this research:

- **200 complex multi-page government forms** across 316 pages
- **15 domains** (agriculture, education, banking, land management, etc.)
- **16,382 layout entities** across a fine-grained 26-entity schema
- **1,926 key-value pairs** across 156 forms for Key Information Extraction (KIE)
- **Bilingual annotations** (Bangla + English)
- **Code repository**: [github.com/mausulazad/BaFCo](https://github.com/mausulazad/BaFCo)
- **License**: CC-BY-NC-4.0 (research use allowed)

**Why BaFCo is perfect for this thesis:**

- It directly addresses "visually-rich Bengali documents" (government forms)
- The KIE annotations can be repurposed for **question-answering** (keys = questions, values = answers)
- The DLA annotations provide layout information for layout-aware retrieval
- It's fresh (ECCV 2026) and highly cited
- The BaFCo paper already evaluated ChatGPT, Gemini, Claude, Qwen, and Kimi on zero-shot and chain-of-thought prompts—providing strong baselines for comparison

**Secondary Datasets (Optional for Generalizability):**

- **NCTB-QA**: 87,805 Bangla QA pairs from textbooks—for demonstrating generalizability beyond forms
- **Khondo**: 1,950 bilingual document packets—for document splitting experiments

#### 5.2 System Architecture: Bengali-MMRAG

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         BENGALI-MMRAG FRAMEWORK                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌──────────────────┐    ┌──────────────────────────────────────────────┐  │
│  │   Document        │    │           RETRIEVAL PIPELINE                 │  │
│  │   Ingestion       │    │  ┌─────────────┐   ┌──────────────┐        │  │
│  │                   │    │  │  Text-Only  │   │  Visual-Only │        │  │
│  │  ┌──────────┐    │    │  │  Retrieval  │   │  Retrieval   │        │  │
│  │  │  OCR     │────┼────┼──▶│ (SBERT/     │   │  (CLIP/      │        │  │
│  │  │(Tesseract)│    │    │  │  BanglaBERT)│   │   DINOv2)    │        │  │
│  │  └──────────┘    │    │  └─────┬───────┘   └──────┬───────┘        │  │
│  │  ┌──────────┐    │    │        │                  │                 │  │
│  │  │  Layout  │    │    │        └────────┬─────────┘                 │  │
│  │  │ Analysis │────┼────┼─────────────────┼───────────────────────────┤  │
│  │  │(BaFCo DLA)│   │    │                 │                           │  │
│  │  └──────────┘    │    │  ┌──────────────▼───────────────┐          │  │
│  │  ┌──────────┐    │    │  │     Hybrid Retrieval         │          │  │
│  │  │  Visual  │    │    │  │  (Multi-vector + Re-ranking) │          │  │
│  │  │ Encoding │────┼────┼──▶│     + Layout-Aware Fusion   │          │  │
│  │  │ (CLIP)   │    │    │  └──────────────┬───────────────┘          │  │
│  │  └──────────┘    │    └─────────────────┼──────────────────────────┘  │
│  └──────────────────┘                      │                             │
│                              ┌──────────────▼──────────────────────────┐  │
│                              │          GENERATION PIPELINE            │  │
│                              │  ┌─────────────────────────────────┐   │  │
│                              │  │  Context Assembly +             │   │  │
│                              │  │  Bengali-Aware Prompt           │   │  │
│                              │  │  Engineering                    │   │  │
│                              │  └──────────────┬──────────────────┘   │  │
│                              │  ┌──────────────▼──────────────────┐   │  │
│                              │  │  LLM Generation                 │   │  │
│                              │  │  (Gemini / Claude / GPT)       │   │  │
│                              │  └──────────────┬──────────────────┘   │  │
│                              │  ┌──────────────▼──────────────────┐   │  │
│                              │  │  Verification &                │   │  │
│                              │  │  Hallucination Reduction       │   │  │
│                              │  └─────────────────────────────────┘   │  │
│                              └──────────────────────────────────────┘  │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

**Key Components:**

1. **Document Preprocessing Module:**
   - OCR for text extraction (Tesseract or specialized Bengali OCR)
   - Layout analysis using BaFCo's DLA annotations (bounding boxes, entity types, relationships)
   - Visual encoding using CLIP or DINOv2 for document image embeddings
   - Unified document representation combining text + layout + visual features

2. **Dual-Encoder Retrieval Module:**
   - **Text Encoder**: SBERT or BanglaBERT for Bengali text embeddings
   - **Visual Encoder**: CLIP or DINOv2 for document image embeddings
   - **Hybrid Retrieval**: Multi-vector retrieval with re-ranking
   - **Novel contribution**: Layout-aware retrieval that weights text blocks by their spatial relationships and entity types

3. **Fusion Module:**
   - Early fusion (concatenate text + visual embeddings)
   - Late fusion (retrieve from both, combine results)
   - **Novel contribution**: Layout-aware fusion that incorporates BaFCo's DLA annotations

4. **Generation Module:**
   - Context assembly with retrieved text and visual summaries
   - Bengali-aware prompt engineering (handling mixed Bangla/English text)
   - LLM generation (Gemini, Claude, or fine-tuned Bengali model)
   - Verification layer for hallucination reduction (inspired by your BartaVerify optimization approach)

#### 5.3 Implementation Stack

| Component | Tool/Framework | Rationale |
| :--- | :--- | :--- |
| **Backend** | Python, FastAPI | Your existing expertise |
| **ML Frameworks** | PyTorch, Transformers | Your existing expertise |
| **Vision Models** | CLIP, DINOv2 | State-of-the-art visual encoders |
| **Vector DB** | ChromaDB, FAISS | Your experience from Utopia |
| **LLM** | Gemini API, Claude API | BaFCo evaluated these models |
| **Orchestration** | LangChain | Your experience from Utopia |
| **Deployment** | Docker, Nginx | Your experience from TournAI |

#### 5.4 Experiments

| Experiment | Description | Evaluation Metric |
| :--- | :--- | :--- |
| **E1: Retrieval Strategy** | Compare text-only vs. visual-only vs. hybrid retrieval | Recall@k, MRR |
| **E2: Fusion Strategy** | Compare early vs. late vs. layout-aware fusion | EM, F1, BLEU |
| **E3: LLM Selection** | Compare Gemini, Claude, GPT (same as BaFCo paper) | Accuracy, Hallucination Rate |
| **E4: Baselines** | Compare against BaFCo's zero-shot MLLM results and text-only RAG | EM, F1 |

**Baselines:**
1. Text-only RAG (OCR text only) — standard RAG
2. Visual-only RAG (image embeddings only)
3. Zero-shot MLLMs (from BaFCo paper)
4. Vanilla LLM (no retrieval)

#### 5.5 Evaluation Metrics

**Quantitative Metrics:**
- Exact Match (EM)
- F1 Score
- BLEU / ROUGE
- Retrieval Recall@k, MRR
- Hallucination Rate (automated + human evaluation)

**Qualitative Analysis:**
- Error analysis by document type (forms types from BaFCo's 15 domains)
- Layout sensitivity analysis (using BaFCo's DLA annotations)

---

### 6. Novelty & Contribution

#### 6.1 Novelty Arguments

| Aspect | Why It's Novel | Evidence from Literature |
| :--- | :--- | :--- |
| **Bengali-Specific Multimodal RAG** | No existing RAG system is designed for Bengali VRDs | All VRD-RAG systems (ViDoRAG, VDocRAG) focus on English |
| **First Multimodal RAG on BaFCo** | BaFCo is a DLA/KIE benchmark, not a RAG benchmark | BaFCo paper evaluates MLLMs only |
| **Layout-Aware Retrieval Fusion** | Novel method for weighting text blocks by spatial relationships using BaFCo's DLA annotations | Current multimodal RAG systems use simple concatenation or late fusion |
| **Systematic Comparison of Retrieval Strategies** | First comparison of text-only, visual-only, and hybrid for Bengali VRDs | Existing Bengali RAG systems are text-only |
| **Lightweight, CPU-Friendly Design** | Building on your BartaVerify optimization (~4ms CPU inference) | Your existing expertise in model optimization |

#### 6.2 Expected Contributions

1. **Framework**: Open-source Bengali-MMRAG implementation
2. **Findings**: First empirical insights into what retrieval and fusion strategies work for Bengali VRDs
3. **Comparison**: Direct comparison against BaFCo's zero-shot MLLM results
4. **Guidelines**: Best practices for building RAG systems for low-resource languages

#### 6.3 Positioning Against Related Work

| Paper | Language | Document Type | RAG | Bengali Focus | Multimodal |
| :--- | :--- | :--- | :--- | :--- | :--- |
| ViDoRAG (2025) | English | VRDs | ✓ | ✗ | ✓ |
| VDocRAG (2025) | English | VRDs | ✓ | ✗ | ✓ |
| TraSe (ACL) | Bangla | Text | ✓ | ✓ | ✗ |
| Bangla-RAG-Pipeline | Bangla+English | PDF (Text) | ✓ | ✓ | ✗ |
| Hybrid Bangla RAG | Bangla | Wikipedia | ✓ | ✓ | ✗ |
| BaFCo (ECCV 2026) | Bengali | VRDs | ✗ | ✓ | ✓ |
| **Bengali-MMRAG (Proposed)** | **Bengali** | **VRDs** | **✓** | **✓** | **✓** |

---

### 7. Feasibility Assessment

#### 7.1 Resource Requirements

| Resource | Requirement | Availability |
| :--- | :--- | :--- |
| **Computing** | GPU (for vision models) | Google Colab Pro / University lab |
| **Data** | BaFCo dataset (publicly available) | Hugging Face |
| **APIs** | Gemini/Claude access | Free tier + university credits |
| **Time** | 6-8 months | Thesis timeline |
| **Supervision** | ML/NLP faculty | Available |
| **Code** | Existing projects (Borno, Utopia, LangLens) | Your GitHub repositories |

#### 7.2 Risk Mitigation

| Risk | Mitigation |
| :--- | :--- |
| **OCR accuracy issues** | Use specialized Bengali OCR + visual fallback (VDocRAG approach) |
| **Computational constraints** | Use smaller models for prototyping, APIs for generation |
| **Time constraints** | Prioritize core experiments (E1-E3), defer ablation studies |
| **Dataset access** | BaFCo is publicly available on Hugging Face |

#### 7.3 Timeline

| Phase | Months | Activities | Deliverables |
| :--- | :--- | :--- | :--- |
| **Phase 1** | 1 | Download and analyze BaFCo dataset; literature review | Understanding of data schema, DLA/KIE annotations |
| **Phase 2** | 1-2 | Convert KIE annotations to QA format; design architecture | QA pairs from BaFCo; architecture specification |
| **Phase 3** | 2-3 | Implement Bengali-MMRAG system | Working system with text + visual retrieval |
| **Phase 4** | 1-2 | Run experiments on BaFCo | Results comparing retrieval strategies |
| **Phase 5** | 1 | Write thesis + prepare publication | Thesis draft; paper submission |

---

### 8. Connection to Your Background

| Your Experience | Connection to Thesis |
| :--- | :--- |
| **Borno (বর্ণ)**: Whiteboard to Study Guide with Gemma 4 Vision | Direct foundation: OCR, multimodal understanding, mixed Bangla/English text extraction, PDF generation |
| **Utopia**: RAG-powered AI Companion with LangChain, ChromaDB | Core RAG infrastructure: retrieval, vector databases, generation pipeline |
| **BartaVerify**: Bangla Fake News Detector (~4ms inference, sub-1.3MB) | Bengali NLP expertise, model optimization, CPU-friendly inference |
| **LangLens**: 97% accuracy language detection across 33+ languages | Multilingual data processing, model evaluation, FastAPI deployment |
| **TournAI**: Full-stack with FastAPI, Celery, Redis, Docker, Nginx | Production deployment, system architecture, async processing |
| **Joblume AI**: AI-powered resume builder with OpenRouter | LLM API integration, prompt engineering |
| **AIUB Computer Club**: Research leadership, 15-member team | Research collaboration, publication experience |

---

### 9. Publication Plan

#### 9.1 Target Venues

| Venue | Type | Alignment | Timeline |
| :--- | :--- | :--- | :--- |
| **ACL/EMNLP/NAACL** | Top-tier NLP | RAG, multilingual NLP, low-resource languages | Submit by Jan 2027 |
| **ECCV/CVPR** | Top-tier Vision | Document understanding, layout analysis | Submit by Mar 2027 |
| **LREC/COLING** | Reputable NLP/LR | Low-resource languages, datasets | Submit by Jun 2027 |
| **ACM Transactions on Asian Language Processing** | Journal | Bengali NLP | Submit by Sep 2027 |

#### 9.2 Expected Papers

| Paper | Content | Target |
| :--- | :--- | :--- |
| **Paper 1** | Bengali-MMRAG: Framework & Experiments on BaFCo | ACL / EMNLP |
| **Paper 2** | Systematic Comparison of Retrieval Strategies for Low-Resource VRDs | ECCV / CVPR (workshop) |

---

### 10. Conclusion

This thesis proposes **Bengali-MMRAG**, the first systematic study of Multimodal Retrieval-Augmented Generation for visually-rich Bengali documents, evaluated on the **BaFCo** benchmark. By leveraging BaFCo's DLA and KIE annotations, designing a novel layout-aware retrieval architecture, and conducting the first empirical comparison of retrieval strategies for Bengali VRDs, this work addresses a critical research gap at the intersection of low-resource NLP, multimodal AI, and document understanding.

The proposed work is **novel** (no existing work applies RAG to BaFCo or studies Bengali VRDs with Multimodal RAG), **feasible** (6-8 months, leverages existing tools and publicly available datasets), and **publishable** (targets top-tier NLP/CV venues). It directly builds on your experience with Borno, Utopia, LangLens, and Bengali NLP, positioning you as a researcher at the frontier of inclusive AI for low-resource languages.

---

### 11. References

1. BaFCo: A Document Understanding Benchmark for Complex Bangla Form Comprehension. ECCV 2026.
2. ViDoRAG: Visual Document Retrieval-Augmented Generation via Dynamic Iterative Reasoning Agents. EMNLP 2025.
3. VDocRAG: Retrieval-Augmented Generation over Visually-Rich Documents. CVPR 2025.
4. TraSe: Enhancing RAG for Bangla using Translative Prompting. ACL Anthology.
5. NCTB-QA: A Large-Scale Bangla Educational Question Answering Dataset.
6. Khondo: A Multimodal Benchmark for Document Packet Splitting of Bangla Forms.
7. BaDLAD: A Large Multi-Domain Bengali Document Layout Analysis Dataset.
8. Bangla-RAG-Pipeline: Lightweight Multilingual RAG for Bangla PDFs.
9. Enhancing Bangla Language Model Through Translation-Free Hybrid RAG.
10. LR-MMQA: Low-Resource Multimodal Question Answering Benchmark. NeurIPS 2025.

---

### 12. Dataset Access

| Dataset | Access Link | License |
| :--- | :--- | :--- |
| **BaFCo** | [huggingface.co/datasets/Mausul/bafco](https://huggingface.co/datasets/Mausul/bafco) | CC-BY-NC-4.0 |
| **Khondo** | [huggingface.co/datasets/Mausul/khondo](https://huggingface.co/datasets/Mausul/khondo) | Research use |
| **NCTB-QA** | [huggingface.co/datasets/eyasir2047/NCTB-QA](https://huggingface.co/datasets/eyasir2047/NCTB-QA) | CC BY-NC 4.0 |
| **BaDLAD** | [github.com/bengaliai/badlad](https://github.com/bengaliai/badlad) | Research use |

---

*This research proposal is designed to be the centerpiece of a compelling Erasmus Mundus application, demonstrating that you are not just a skilled engineer, but a budding researcher with a vision for the future of inclusive, multilingual AI.*
