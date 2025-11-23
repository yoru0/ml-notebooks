# Directional Classification

Notebook project comparing SimpleRNN and LSTM models for predicting directional movement of Bitcoin 1‑minute bars.

## Contents
- `RNN_LSTM.ipynb`: end-to-end notebook (preprocessing, RNN/LSTM training, evaluation, plots, analysis).
- `btcusd_1-min_data.csv`: Kaggle Bitcoin Historical Data (1 minute bars) used locally.

## Dataset
- Source: https://www.kaggle.com/datasets/mczielinski/bitcoin-historical-data
- File used: `btcusd_1-min_data.csv` (must be present alongside the notebook).

## Running the notebook
1) Ensure Python with TensorFlow, scikit-learn, pandas, seaborn, matplotlib is available.
2) Place `btcusd_1-min_data.csv` in the repo root (already included here).
3) Open and run `RNN_LSTM.ipynb` top-to-bottom to reproduce preprocessing, training, and comparison plots.

## What the notebook covers
- Preprocessing: timestamp parsing, sorting, NA drop, MinMax scaling, directional label creation with lookback windows.
- Models: SimpleRNN and LSTM architectures with early stopping.
- Evaluation: validation curves, confusion matrices, test accuracy bar chart, and actual-vs-prediction comparison plot.
- Analysis: pros/cons of each model and brief conclusions based on observed metrics.
