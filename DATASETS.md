# Datasets

Datasets from Kaggle or other open sources are **not stored in this repo**. The notebooks fetch them the first time you run them, using a short cell just above the cell that loads the data. Kaggle datasets go through [`kagglehub`](https://github.com/Kaggle/kagglehub) (Kaggle's official library) and are cached once in `~/.cache/kagglehub`, outside the repo and shared across notebooks.

Public Kaggle datasets need no API key. The exceptions are Kaggle *competitions* such as Dog Breed. See [Needs a Kaggle login](#needs-a-kaggle-login).

## Downloaded automatically

| Where | Dataset | Source | Download | Saved to |
|---|---|---|---|---|
| `courses/deep-learning/01-neural-networks` | Bank Customer Churn Prediction | [Kaggle: gauravtopre/bank-customer-churn-dataset](https://www.kaggle.com/datasets/gauravtopre/bank-customer-churn-dataset) | `kagglehub` | kagglehub cache |
| `courses/deep-learning/02-regression-and-classification` | Szeged weather 2006–2016 | [Kaggle: budincsevity/szeged-weather](https://www.kaggle.com/datasets/budincsevity/szeged-weather) | `kagglehub` | kagglehub cache |
| `courses/deep-learning/03-convolutional-neural-networks` | Rice Image Dataset (75k images, ~230 MB) | [Kaggle: muratkokludataset/rice-image-dataset](https://www.kaggle.com/datasets/muratkokludataset/rice-image-dataset) | `kagglehub` | kagglehub cache |
| `courses/deep-learning/06-transformers` | 4 vegetable classes (Tomato, Cucumber, Carrot, Broccoli), first 500 training images each | [Kaggle: misrakahmed/vegetable-image-dataset](https://www.kaggle.com/datasets/misrakahmed/vegetable-image-dataset) | `kagglehub` | kagglehub cache |
| `courses/deep-learning/07-unsupervised-learning`, `08-autoencoders`, `12-quiz` | Shoe vs Sandal vs Boot (15k images) | [Kaggle: hasibalmuzdadid/shoe-vs-sandal-vs-boot-dataset-15k-images](https://www.kaggle.com/datasets/hasibalmuzdadid/shoe-vs-sandal-vs-boot-dataset-15k-images) | `kagglehub` | kagglehub cache |
| `courses/machine-learning/01-eda-and-preprocessing`, `03-logistic-regression` | Titanic (`train.csv` equivalent, 891 rows) | [datasciencedojo/datasets](https://github.com/datasciencedojo/datasets) (GitHub mirror of the Kaggle Titanic data) | `pd.read_csv(<url>)` | not saved |
| `courses/machine-learning/02-linear-regression` | House Prices (`train.csv`) | [Kaggle: lespin/house-prices-dataset](https://www.kaggle.com/datasets/lespin/house-prices-dataset) (mirror of the competition files) | `kagglehub` | kagglehub cache |
| `courses/machine-learning/04-recommender-system` | MovieLens 100K | [GroupLens](https://grouplens.org/datasets/movielens/100k/) | `pd.read_csv(<url>)` | not saved |
| `courses/natural-language-processing/05-naive-bayes` | IMDB Dataset of 50K Movie Reviews | [Kaggle: lakshmi25npathi/imdb-dataset-of-50k-movie-reviews](https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews) | `kagglehub` | kagglehub cache |
| `courses/speech-recognition/07-keyword-spotting` | Google Speech Commands v0.02, keywords `follow`, `learn`, `tree`, `visual` (**~2.3 GB download**, only these 4 words are kept) | [TensorFlow: speech_commands_v0.02](http://download.tensorflow.org/data/speech_commands_v0.02.tar.gz) | notebook cell (`keyword-spotting-review-2.ipynb`) | `dataset/<word>/` |
| `projects/emotion-recognition` | RAVDESS Audio Speech Actors 01–24 (~200 MB) | [Zenodo record 1188976](https://zenodo.org/records/1188976) | notebook cell | `Audio_Speech_Actors_01-24.zip`, `speech_dataset/` |
| `projects/bitcoin-direction-rnn-lstm` | Bitcoin Historical Data (1-minute bars) | [Kaggle: mczielinski/bitcoin-historical-data](https://www.kaggle.com/datasets/mczielinski/bitcoin-historical-data) | `kagglehub` | kagglehub cache |
| `projects/stock-forecasting` | BTC-USD prices | [Yahoo Finance](https://finance.yahoo.com/) | `yfinance` | not saved |

Notes:
- The vegetable subset is built by taking `0001.jpg`–`0500.jpg` of each class from the Kaggle `train` split. This matches the file names of the copy that used to be committed, but it was not compared byte for byte.
- Both Titanic notebooks used to read the file from a private Google Drive folder. They now read the public CSV directly, so they no longer need `google.colab`.
- The Drive links in the emotion-recognition notebook were replaced with the official Zenodo archive.

## Needs a Kaggle login

**Dog Breed Identification** (`projects/dog-breed-classification`) is a Kaggle *competition*, so the download needs a Kaggle account and an API token.

1. Open <https://www.kaggle.com/competitions/dog-breed-identification> and click **Join Competition** to accept the rules.
2. Create an API token in your Kaggle account settings and save it as `~/.kaggle/kaggle.json`.
3. From `projects/dog-breed-classification`, run:

   ```bash
   uv run --with kaggle kaggle competitions download -c dog-breed-identification -p data/dog-breed-identification
   unzip data/dog-breed-identification/dog-breed-identification.zip -d data/dog-breed-identification
   ```

The notebooks expect `data/dog-breed-identification/{train/, test/, labels.csv}`. This download has not been run end to end.

## Not covered (source unknown)

These still point at the copy that is in the repo, or at a Google Drive link. I could not confirm their original source, so they were not changed:

- Mental health text classification (`machine-learning/05`, `natural-language-processing/assignment-3`, `projects/odi-nlp-classifier`): Google Drive link.
- Skin cancer ISIC (`projects/skin-cancer-classification`): Google Drive link.
- `movie_sentiment.csv`, `movie_rating.csv`, `Tweets.csv` (NLP quizzes), `dictionary.csv` (deep-learning/05), the room-climate CSVs (deep-learning/13), and the computer-vision images (`dataset/` folders in 06, 10, 11, 13).
- `projects/sequence-alignment/sequence.fasta` and `sequence.gb`: small, so they are kept in the repo.
