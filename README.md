# ML Notebooks

![Python 3.13](https://img.shields.io/badge/python-3.13-blue)
![uv](https://img.shields.io/badge/environments-uv-de5fe9)
![Jupyter](https://img.shields.io/badge/notebooks-Jupyter-f37626)

Machine learning coursework and standalone projects, written as Jupyter notebooks. Every course and every project is self-contained: its own folder, its own README and its own [uv](https://docs.astral.sh/uv/) environment.

## Table of contents

- [Quick start](#quick-start)
- [Repository layout](#repository-layout)
- [Courses](#courses)
- [Projects](#projects)
- [Datasets](#datasets)
- [Conventions](#conventions)
- [Troubleshooting](#troubleshooting)

## Quick start

**Prerequisites:** [uv](https://docs.astral.sh/uv/getting-started/installation/) and Git. uv downloads the right Python version for you, so you don't need to install Python yourself. Some notebooks also need [FFmpeg](https://ffmpeg.org/) on your `PATH` (audio) or a GPU (training).

```bash
git clone https://github.com/yoru0/ml-notebooks.git
cd ml-notebooks/courses/deep-learning   # any course or project folder
uv sync                                 # creates .venv and installs the pinned dependencies
uv run --with jupyterlab jupyter lab    # or open a notebook in VS Code with the .venv kernel
```

Notes:

- Run each notebook from its own folder. Files such as `dataset/...` and sample audio are read by relative path.
- Environments are not shared between courses, because TensorFlow, PyTorch and library pins conflict. Run `uv sync` once in each folder you want to use.
- All environments use Python 3.13, except `projects/gesture-recognition` (3.12), which needs `mediapipe.solutions`.
- The first run of a notebook downloads its data and models, so it needs an internet connection.

## Repository layout

```text
ml-notebooks/
├── courses/
│   └── <course>/
│       ├── pyproject.toml, uv.lock    environment for the whole course
│       ├── README.md                  contents, setup and notes
│       └── 01-<topic>/                one folder per session
├── projects/
│   └── <project>/                     same structure as a course
├── Datasets.md                        where every dataset comes from
├── CLAUDE.md                          repository conventions
└── README.md
```

## Courses

| Course                                                             | What it covers                                                                  |
| ------------------------------------------------------------------ | ------------------------------------------------------------------------------- |
| [Computational Biology](courses/computational-biology)             | DNA and protein sequences with Biopython, alignment, k-mer classification       |
| [Computer Vision](courses/computer-vision)                         | Image processing, feature detection and matching, face recognition              |
| [Deep Learning](courses/deep-learning)                             | Neural networks, CNNs, transformers, autoencoders, GANs, reinforcement learning |
| [Machine Learning](courses/machine-learning)                       | EDA, regression, recommender systems, text classification                       |
| [Natural Language Processing](courses/natural-language-processing) | Tokenization, POS tagging, TF-IDF, Naive Bayes, text classifiers                |
| [Speech Recognition](courses/speech-recognition)                   | Audio processing, MFCC, Wav2Vec2, text-to-speech, keyword spotting              |

## Projects

| Project                                                                         | What it does                                                  |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| [bitcoin-direction-rnn-lstm](projects/bitcoin-direction-rnn-lstm)               | SimpleRNN vs LSTM for Bitcoin price direction                 |
| [dog-breed-classification](projects/dog-breed-classification)                   | Dog breed identification with PyTorch (Kaggle competition)    |
| [emotion-recognition](projects/emotion-recognition)                             | Emotion classification from speech (RAVDESS)                  |
| [gesture-recognition](projects/gesture-recognition)                             | Webcam hand gesture recognizer with MediaPipe                 |
| [mental-health-text-classification](projects/mental-health-text-classification) | Mental health text classifier                                 |
| [sequence-alignment](projects/sequence-alignment)                               | Pairwise alignment of nucleotide sequences                    |
| [skin-cancer-classification](projects/skin-cancer-classification)               | Skin lesion classification with an EfficientNet + Swin hybrid |
| [stock-forecasting](projects/stock-forecasting)                                 | LSTM price forecasting for stocks and crypto                  |
