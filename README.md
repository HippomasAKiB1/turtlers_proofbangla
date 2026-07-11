# SignLingua
### Zero-Shot Multilingual Gloss-Free Sign Language Translation using Raw Video and Large Language Models

> Breaking language barriers for the Deaf community through multimodal AI.

---

## 📖 Overview

**SignLingua** is a next-generation Sign Language Translation (SLT) system that translates continuous sign language videos directly into natural language sentences.

Unlike traditional SLT systems, SignLingua requires:

- ❌ No gloss annotations
- ❌ No pose/keypoint extraction
- ❌ No handcrafted linguistic supervision

Instead, it learns directly from **raw RGB videos** and leverages the reasoning ability of a **Frozen Large Language Model (LLM)** to generate fluent translations.

The long-term vision is to build a universal translator capable of understanding sign languages and producing translations in multiple spoken languages through simple prompting.

---

# ✨ Motivation

More than **70 million Deaf people** communicate primarily through sign language.

Current translation systems suffer from several limitations:

- Require expensive gloss annotations
- Depend on keypoint extraction pipelines
- Produce robotic translations using small text decoders
- Usually support only one output language

SignLingua aims to eliminate these limitations by combining modern computer vision with state-of-the-art language models.

---

# 🚀 Key Features

- Raw RGB video input
- Completely gloss-free training
- No MediaPipe or pose estimation required
- Frozen VideoMAE visual encoder
- Frozen Llama-3 8B language model
- Lightweight Q-Former bridge
- LoRA fine-tuning
- Contrastive semantic alignment
- Zero-shot multilingual translation
- Near real-time inference
- Interactive web interface

---

# 🧠 How It Works

```
               Raw Sign Video
                      │
                      ▼
        Frozen VideoMAE-v2 Encoder
                      │
          Spatio-temporal Features
                      │
                      ▼
             Q-Former Adapter
                      │
        Visual Language Embeddings
                      │
                      ▼
      Frozen Llama-3 8B Language Model
                      │
                      ▼
        Natural Language Translation
```

The visual encoder extracts semantic information from video frames.

Instead of training an entire language model, SignLingua learns a lightweight adapter that aligns visual features with the language model's embedding space.

The frozen LLM then generates fluent translations.

---

# 🌍 Zero-Shot Multilingual Translation

One unique capability of SignLingua is multilingual translation.

The model is trained only using:

```
German Sign Language
        ↓
German Text
```

At inference time, changing only the prompt enables translation into other languages.

Example:

```
Translate into German:
→ Morgen wird das Wetter sonnig sein.

Translate into English:
→ Tomorrow the weather will be sunny.

Translate into Turkish:
→ Yarın hava güneşli olacak.
```

No additional multilingual training is required.

---

# 🏗 Architecture

## Video Encoder

- VideoMAE-v2 Base
- Frozen during training
- Extracts spatio-temporal visual tokens

---

## Q-Former

A lightweight transformer that learns how to convert visual tokens into language embeddings.

Trainable.

---

## Language Model

- Llama-3 8B Instruct
- Frozen
- Generates fluent translations

LoRA adapters are used for efficient fine-tuning.

---

# 📚 Dataset

Current benchmark:

- RWTH-PHOENIX-Weather 2014T

Contains:

- Continuous German Sign Language videos
- German sentence translations

Future support:

- WLASL
- CSL
- BOBSL
- How2Sign

---

# 📈 Training Strategy

Only the following components are trained:

- Q-Former
- Projection Layer
- LoRA adapters

Frozen components:

- VideoMAE
- Llama-3

Loss function:

```
Total Loss

=
Language Modeling Loss
+
λ × Contrastive Alignment Loss
```

The contrastive objective aligns visual representations with semantic sentence embeddings.

---

# 💡 Novel Contributions

SignLingua introduces several novel ideas:

- Direct raw-video-to-text translation
- No gloss annotations
- No keypoint extraction
- Frozen LLM as decoder
- Contrastive visual-language alignment
- Zero-shot multilingual translation
- Real-time interactive demo

---

# 💻 Tech Stack

### Deep Learning

- PyTorch
- HuggingFace Transformers
- PEFT (LoRA)
- Accelerate

### Computer Vision

- VideoMAE-v2
- OpenCV

### NLP

- Llama-3 8B
- SentencePiece

### Deployment

- Gradio
- ONNX Runtime
- CUDA

---

# 📂 Project Structure

```
SignLingua/

├── data/
│   ├── raw/
│   ├── processed/
│   └── features/
│
├── models/
│   ├── videomae/
│   ├── qformer/
│   ├── lora/
│   └── projector/
│
├── training/
│   ├── train.py
│   ├── evaluate.py
│   └── losses.py
│
├── inference/
│   ├── translator.py
│   └── webcam.py
│
├── demo/
│   └── app.py
│
├── configs/
│
├── notebooks/
│
└── README.md
```

---

# ⚙ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/SignLingua.git

cd SignLingua
```

Create a virtual environment

```bash
python -m venv venv

source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🚀 Training

```bash
python training/train.py
```

---

# 🔍 Evaluation

```bash
python training/evaluate.py
```

---

# 🎥 Demo

Launch the interactive interface:

```bash
python demo/app.py
```

Features:

- Webcam recording
- Upload video
- Live translation
- Language selection
- Confidence visualization

---

# 📊 Evaluation Metrics

The model is evaluated using:

- BLEU-1
- BLEU-2
- BLEU-4
- ROUGE-L
- METEOR
- BERTScore

Human evaluation will also assess:

- Fluency
- Semantic correctness
- Readability

---

# 🔬 Future Work

- Support additional sign languages
- Real-time streaming translation
- Sign-to-sign translation
- Speech output generation
- Mobile deployment
- Edge AI optimization
- Larger multilingual datasets

---

# 🤝 Applications

- Deaf accessibility
- Education
- Public services
- Hospitals
- Customer support
- Video conferencing
- International communication

---

# 📜 Research Goal

SignLingua aims to bridge the gap between sign language users and spoken language communities through scalable multimodal artificial intelligence.

By eliminating gloss annotations and handcrafted preprocessing while leveraging the reasoning capabilities of Large Language Models, this project moves toward universal, multilingual sign language translation.

---

# 👨‍💻 Author

**Akib Hasan Pyil**

B.Sc. in Computer Science & Engineering

Major: Data Science & Artificial Intelligence

AIUB – American International University-Bangladesh

**Nazat E Rose Rhythm**

B.Sc. in Computer Science & Engineering

Major: Data Science & Artificial Intelligence

AIUB – American International University-Bangladesh

**Most. Sumiaya Habiba**

B.Sc. in Computer Science & Engineering

Major: Data Science & Artificial Intelligence

AIUB – American International University-Bangladesh

---

# 📄 License

This project is intended for academic research purposes.

