## General
A notebook project that classifies whether a text is mental health related or not.
It compares several machine learning models, from a voting classifier to an LSTM, and saves the final voting classifier and its TF-IDF vectorizer as `.joblib` files.

## Files & Folders
- `model-selection.ipynb` -> the models tested, from voting classifier to LSTM
- The training data (Mental Health Corpus from Kaggle) is downloaded by the notebook on first run
- The saved models (`voting_model.joblib`, `voting_model.pickle`, `tfidf_vectorizer.joblib`) are written to `~/.cache/ml-notebooks/mental-health-text-classification/`, not to the repo

## How to use
### Clone repo
```
git clone https://github.com/yoru0/ml-notebooks.git
cd ml-notebooks/projects/mental-health-text-classification
```

### Install and run
```
uv sync
```
Then open `model-selection.ipynb` in VS Code with the `.venv` kernel, or start Jupyter with `uv run --with jupyterlab jupyter lab`.

## Notes
- The saved `.joblib` models were trained with scikit-learn 1.6.1, which is why `pyproject.toml` pins that version. Loading them with a different scikit-learn version can fail or warn.
- Update - 22/5/2025 - Done?? Maybe...
- Update 2.0 - 26/5/2025 - Done???
- The Flask API and React frontend that used to live here were removed, so this project is the notebook and its saved models only.
