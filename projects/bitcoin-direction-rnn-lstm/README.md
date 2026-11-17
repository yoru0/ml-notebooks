# Bitcoin Direction Prediction: RNN vs LSTM

Notebook project comparing SimpleRNN and LSTM models for predicting directional movement of Bitcoin 1‑minute bars.

## Contents
- `RNN_LSTM.ipynb`: end-to-end notebook (preprocessing, RNN/LSTM training, evaluation, plots, analysis).

## Dataset
- Source: https://www.kaggle.com/datasets/mczielinski/bitcoin-historical-data (Bitcoin Historical Data, 1-minute bars).
- File used: `btcusd_1-min_data.csv`. It is not included in this repo: download it from Kaggle and place it next to the notebook.

## Running the notebook
1) Ensure Python with TensorFlow, scikit-learn, pandas, seaborn, matplotlib is available.
2) Download `btcusd_1-min_data.csv` from Kaggle (see Dataset) and place it next to the notebook.
3) Open and run `RNN_LSTM.ipynb` top-to-bottom to reproduce preprocessing, training, and comparison plots.

## What the notebook covers
- Preprocessing: timestamp parsing, sorting, NA drop, MinMax scaling, directional label creation with lookback windows.
- Models: SimpleRNN and LSTM architectures with early stopping.
- Evaluation: validation curves, confusion matrices, test accuracy bar chart, and actual-vs-prediction comparison plot.
- Analysis: pros/cons of each model and brief conclusions based on observed metrics.
