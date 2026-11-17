# Emotion Recognition

This repository contains a Jupyter notebook that trains a convolutional neural network to classify emotions in speech using the Ryerson Audio-Visual Database of Emotional Speech and Song (RAVDESS).

## Features
- Automated download and extraction of the RAVDESS speech corpus via `gdown`.
- Exploratory data analysis covering actor coverage, duplicate detection, emotion distribution, audio duration, and sample-rate checks.
- Audio feature engineering with MFCC, chroma, and Mel-spectrogram statistics plus augmentation through additive noise and temporal shifts.
- 1D CNN built with TensorFlow/Keras (Conv1D, pooling, dropout, L1/L2 regularisation) trained for 100 epochs and evaluated with confusion matrices and sample predictions.
- Utility helpers to save/reload artefacts and audition predictions directly in the notebook.

## Dataset
The workflow expects the RAVDESS Audio Speech Actor archive (`Audio_Speech_Actors_01-24.zip`). The first section of the notebook uses `gdown` to fetch the zip and extracts it to `speech_dataset/`. If the automated download is blocked, download the archive manually from [the official RAVDESS release](https://zenodo.org/record/1188976/files/Audio_Speech_Actors_01-24.zip) and place it in the project root before rerunning the extraction cell.

## Getting Started
### Prerequisites
- Python 3.10 or newer
- `pip`
- (Recommended) a virtual environment tool such as `venv`, `conda`, or `pipenv`

### Installation
1. Clone the repository.
2. Create and activate your virtual environment.
3. Install dependencies: `pip install -r requirements.txt`

## Running the Notebook
1. Launch JupyterLab/Notebook or open `main.ipynb` in VS Code.
2. Execute the cells sequentially. The notebook will download the dataset, perform EDA, extract features, split the data, train the CNN (batch size 64, 100 epochs), and plot training history alongside the confusion matrix.
3. The final "Uji Coba" section provides `predict_sample` examples that play audio clips and display the model’s predictions.
4. Use the "Save & Load Model" section if you want to persist trained weights or reuse them in later sessions.

## Repository Structure
- `main.ipynb` – complete pipeline covering data ingestion, EDA, preprocessing, model training, evaluation, saving/loading, and sample inference.
- `requirements.txt` – Python dependencies needed to run the notebook.

## Notes
- CPU training can take a while; enable a GPU-backed TensorFlow install if available.
- Intermediate artefacts (`X.npy`, `y.npy`, trained weights) are created only when the corresponding cells are run.

## Acknowledgements
- Built with TensorFlow/Keras, Librosa, Scikit-learn, and the broader Python data-science ecosystem.
