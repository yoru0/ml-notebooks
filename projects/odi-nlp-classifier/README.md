## General
A notebook project that classifies whether a text is mental health related or not.
It compares several machine learning models, from a voting classifier to an LSTM, and saves the final voting classifier and its TF-IDF vectorizer as `.joblib` files.

## Files & Folders
- `model-selection.ipynb` -> the models tested, from voting classifier to LSTM
- `dataset/` -> the training data
- `voting_model.joblib`, `tfidf_vectorizer.joblib`, `model.joblib` -> the saved models

## How to use
### Clone repo
```
git clone https://github.com/yoru0/ml-notebooks.git
cd ml-notebooks/projects/odi-nlp-classifier
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
