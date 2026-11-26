# Natural Language Processing

Notebooks that cover the standard NLP pipeline in Python: tokenization, stemming and lemmatization, part-of-speech tagging, TF-IDF with cosine similarity, Naive Bayes, and a larger comparison of text classifiers.

## Contents

| Folder | Notebook | Topic |
|---|---|---|
| `01-natural-language-toolkit` | `tokenization.ipynb` | Tokenization with NLTK |
| `02-stemming-and-lemmatization` | `stemming-and-lemmatization.ipynb` | Stemming, lemmatization, WordNet synonyms and antonyms |
| `03-pos-tagging` | `pos-tagging.ipynb`, `pos-tagging-menu-exercise.ipynb` | Part-of-speech tagging and a menu-driven exercise |
| `04-tf-idf-and-cosine-similarity` | `tf-idf-and-cosine-similarity.ipynb` | TF-IDF vectors and cosine similarity |
| `05-naive-bayes` | `imdb-naive-bayes.ipynb` | Naive Bayes sentiment classifier on IMDB reviews |
| `06-quiz` | `quiz-answer-1` to `quiz-answer-4`, `movie-review-practice.ipynb` | Quiz answers: movie sentiment, TF-IDF recommendation, preprocessing, Word2Vec |
| `07-assignment-mental-health` | `mental-health-model-comparison.ipynb`, `single-model/` | Comparison of text classifiers on the mental health corpus |
| `08-airline-tweet-practice` | `Airline Tweet Sentiment Practice.md` | Practice task description (airline tweet sentiment) |

The task descriptions are in Markdown next to the notebooks: `06-quiz/Quiz Description.md`, `06-quiz/Quiz Description 2.md` and `08-airline-tweet-practice/Airline Tweet Sentiment Practice.md`. The assignment write-ups are in `07-assignment-mental-health/`.

## Getting Started

1. Install [uv](https://docs.astral.sh/uv/). It provides Python 3.13 automatically.
2. Install the dependencies for the whole course (from this folder):
   ```bash
   uv sync
   ```
   This also installs the spaCy model `en_core_web_sm`.
3. Open a notebook in VS Code with the `.venv` kernel, or start Jupyter with `uv run --with jupyterlab jupyter lab`. Run each notebook from its own folder.

## Datasets

Nothing is stored in the repo. The notebooks download what they need on first run through `kagglehub` (IMDB reviews, the mental health corpus, and the Rotten Tomatoes data for the quiz notebooks), so the first run needs an internet connection. See [Datasets.md](../../Datasets.md) for the sources.

## Notes

- NLTK corpora (`punkt`, `stopwords`, `wordnet`, the POS tagger) are fetched with `nltk.download(...)` inside the notebooks.
- The `06-quiz` notebooks build their movie data from the Kaggle Rotten Tomatoes dataset, which is the closest public match to the original quiz files. Saved outputs in those notebooks come from the earlier data, so numbers will differ when you re-run them. `quiz-answer-3-preprocessing.ipynb` already fails on a fresh run because a cell calls `predict_review` before a model exists.
- Five notebooks are interactive menu exercises that wait for keyboard input (`input()`), so they cannot run top to bottom unattended: `02-stemming-and-lemmatization/stemming-and-lemmatization.ipynb`, `03-pos-tagging/pos-tagging-menu-exercise.ipynb`, `06-quiz/movie-review-practice.ipynb`, `06-quiz/quiz-answer-2-tfidf.ipynb` and `06-quiz/quiz-answer-3-preprocessing.ipynb`. Run them cell by cell and type at the prompts. Their saved outputs come from earlier interactive runs.
- The notebooks save trained models (`model.pickle`, `*.joblib`) next to themselves. Git ignores these files, so they are recreated when you run the notebooks.
