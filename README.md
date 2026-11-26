# ML Notebooks

![Python 3.13](https://img.shields.io/badge/python-3.13-blue)
![uv](https://img.shields.io/badge/environments-uv-de5fe9)
![Jupyter](https://img.shields.io/badge/notebooks-Jupyter-f37626)

My machine learning coursework and personal projects. Each course and project has its own folder, README and [uv](https://docs.astral.sh/uv/) environment.

## Quick start

Install [uv](https://docs.astral.sh/uv/getting-started/installation/). It will install Python 3.13 for you.

```bash
git clone https://github.com/yoru0/ml-notebooks.git
cd ml-notebooks/courses/deep-learning   # any course or project folder
uv sync
uv run --with jupyterlab jupyter lab
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

## License

[MIT](LICENSE) for the code and notebooks written here. Datasets, course material and third-party files keep their original terms.
