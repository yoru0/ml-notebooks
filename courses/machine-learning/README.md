# Machine Learning

Introductory machine learning notebooks built with pandas, scikit-learn and TensorFlow. They go from exploring and cleaning a dataset to linear and logistic regression, a recommender system, and a text classification assignment.

## Contents

| Folder | Notebook | Topic |
|---|---|---|
| `01-eda-and-preprocessing` | `titanic-eda-and-preprocessing.ipynb` | Exploratory analysis and preprocessing on the Titanic data |
| `02-linear-regression` | `house-price-linear-regression.ipynb` | Linear regression on house prices |
| `03-logistic-regression` | `titanic-logistic-regression.ipynb` | Logistic regression on the Titanic data |
| `04-recommender-system` | `movielens-recommender-system.ipynb` | Recommender system on MovieLens 100K |
| `05-assignment` | `mental-health-text-classification.ipynb` | Classify mental-health related text |

## Getting Started

1. Install [uv](https://docs.astral.sh/uv/). It provides Python 3.13 automatically.
2. Install the dependencies for the whole course (from this folder):
   ```bash
   uv sync
   ```
3. Open a notebook in VS Code with the `.venv` kernel, or start Jupyter with `uv run --with jupyterlab jupyter lab`. Run each notebook from its own folder.

## Datasets

None of the datasets are stored in the repo. The notebooks download them the first time they run (Titanic and MovieLens from public URLs, House Prices and the mental health corpus through `kagglehub`), so the first run needs an internet connection. See [Datasets.md](../../Datasets.md) for the sources.

## Notes

- The notebooks use NLTK for the text assignment. They call `nltk.download(...)` for the corpora they need.
- Saved outputs in the notebooks come from the original runs. Re-running them can give slightly different numbers where a random split or sample is used.
