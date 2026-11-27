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
| `courses/speech-recognition/07-keyword-spotting` | Google Speech Commands v0.02, keywords `follow`, `learn`, `tree`, `visual` (**~2.3 GB download**, only these 4 words are kept) | [TensorFlow: speech_commands_v0.02](http://download.tensorflow.org/data/speech_commands_v0.02.tar.gz) | notebook cell (`keyword-spotting-review-2.ipynb`) | `~/.cache/ml-notebooks/speech-commands/<word>/` |
| `projects/emotion-recognition` | RAVDESS Audio Speech Actors 01–24 (~200 MB) | [Zenodo record 1188976](https://zenodo.org/records/1188976) | notebook cell | `~/.cache/ml-notebooks/` |
| `projects/bitcoin-direction-rnn-lstm` | Bitcoin Historical Data (1-minute bars) | [Kaggle: mczielinski/bitcoin-historical-data](https://www.kaggle.com/datasets/mczielinski/bitcoin-historical-data) | `kagglehub` | kagglehub cache |
| `projects/stock-forecasting` | BTC-USD prices | [Yahoo Finance](https://finance.yahoo.com/) | `yfinance` | not saved |
| `projects/skin-cancer-classification` | Skin cancer ISIC, 9 classes (2,357 images, ~826 MB) | [Kaggle: nodoubttome/skin-cancer9-classesisic](https://www.kaggle.com/datasets/nodoubttome/skin-cancer9-classesisic) | `kagglehub` | kagglehub cache, re-split copy in `~/.cache/ml-notebooks/skin-cancer` |
| `courses/computational-biology/04-sequence-alignment`, `05-kmer-classification` | NCBI nucleotide records NC_035298.1 and MK312630.1 | [NCBI Nucleotide](https://www.ncbi.nlm.nih.gov/nuccore/) | `Bio.Entrez.efetch` | not saved |
| `courses/computational-biology/04-sequence-alignment/fasta-genbank-alignment-exercise.ipynb`, `projects/sequence-alignment` | NCBI records M99367.1 (FASTA) and BI431008 (GenBank) | [NCBI Nucleotide](https://www.ncbi.nlm.nih.gov/nuccore/) | `Bio.Entrez.efetch` | not saved |
| `courses/machine-learning/05-assignment`, `courses/natural-language-processing/07-assignment-mental-health`, `projects/mental-health-text-classification` | Mental Health Corpus (27,977 posts, `text` + `label`) | [Kaggle: reihanenamdari/mental-health-corpus](https://www.kaggle.com/datasets/reihanenamdari/mental-health-corpus) | `kagglehub` | kagglehub cache |
| `courses/computer-vision/06-image-matching`, `07-quiz-i` | Pokemon Images Dataset (8 images of 819, plus 3 rotated and enlarged targets built from them) | [Kaggle: kvpratama/pokemon-images-dataset](https://www.kaggle.com/datasets/kvpratama/pokemon-images-dataset) | `kagglehub` | kagglehub cache, subset in `~/.cache/ml-notebooks/computer-vision/<session>/` |
| `courses/computer-vision/10-object-detection`, `11-face-recognition`, `12-quiz-ii` | Labeled Faces in the Wild (3–4 people, 10–12 training photos each) | [Kaggle: jessicali9530/lfw-dataset](https://www.kaggle.com/datasets/jessicali9530/lfw-dataset) | `kagglehub` | kagglehub cache, train/test split in `~/.cache/ml-notebooks/computer-vision/<session>/dataset/` |
| `courses/natural-language-processing/06-quiz` | Rotten Tomatoes movies and critic reviews | [Kaggle: andrezaza/clapper-massive-rotten-tomatoes-movies-and-reviews](https://www.kaggle.com/datasets/andrezaza/clapper-massive-rotten-tomatoes-movies-and-reviews) | `kagglehub` | kagglehub cache |
| `courses/deep-learning/05-recurrent-neural-networks` | Tatoeba English–German sentence pairs (the 64,000 shortest) | [manythings.org/anki](https://www.manythings.org/anki/) (from [Tatoeba](https://tatoeba.org/), CC BY 2.0 FR) | notebook cell (`urllib`) | not saved |

Notes:
- The vegetable subset is built by taking `0001.jpg`–`0500.jpg` of each class from the Kaggle `train` split. This matches the file names of the copy that used to be committed, but it was not compared byte for byte.
- Both Titanic notebooks used to read the file from a private Google Drive folder. They now read the public CSV directly, so they no longer need `google.colab`.
- The Drive links in the emotion-recognition notebook were replaced with the official Zenodo archive.

## Needs a Kaggle login

**Dog Breed Identification** (`projects/dog-breed-classification`) is a Kaggle *competition*, so the download needs a Kaggle account and an API token.

1. Open <https://www.kaggle.com/competitions/dog-breed-identification> and click **Join Competition** to accept the rules.
2. Create an API token in your Kaggle account settings and save it as `~/.kaggle/kaggle.json`.
3. Run the notebooks. They call `kagglehub.competition_download("dog-breed-identification")`, which caches the files outside the repo. The processed splits go to `~/.cache/ml-notebooks/dog-breed-processed`.

This download has not been run end to end.

## Course files without a notebook

These files used to be committed but no notebook in the repo reads them. Public copies:

- `courses/deep-learning/04-word-embeddings`: [Kaggle: sbhatti/financial-sentiment-analysis](https://www.kaggle.com/datasets/sbhatti/financial-sentiment-analysis) (`data.csv`, 5,842 rows). The old committed file was identical.
- `courses/natural-language-processing/08-airline-tweet-practice`: [Kaggle: crowdflower/twitter-airline-sentiment](https://www.kaggle.com/datasets/crowdflower/twitter-airline-sentiment) (`Tweets.csv`, use the `airline_sentiment` and `text` columns). The old committed file was a subset of it.

```python
import kagglehub
path = kagglehub.dataset_download("sbhatti/financial-sentiment-analysis")
```

## Notes on the replaced files

- `movie_sentiment.csv` and `movie_rating.csv` (NLP 06-quiz) were replaced by the Rotten Tomatoes dataset above, which is the closest public match: about 91% of the old `movie_sentiment.csv` rows appear in it. The old `movie_rating.csv` was IMDb user reviews with the film's IMDb rating. No public copy was found, so the quiz notebooks now build `Title`, `Rating` (audience score ÷ 10) and `Review` from Rotten Tomatoes. Results differ from the old outputs.
- The skin cancer notebook used a Google Drive zip of 3,780 images (train/test/val). The Kaggle copy has 2,357 images in Train/Test only, so the notebook pools them and splits again 70/20/10. Results will differ from the old outputs.
- `dictionary.csv` (deep-learning/05) was an older Tatoeba snapshot (99.7% of its pairs are still in the current file). The notebook now uses the 64,000 shortest current pairs.

## Not covered (kept in the repo or unknown source)

- The room-climate CSVs (`courses/deep-learning/13-final-exam`): supplied with the exam, not in the repo.
- Computer-vision images that are still committed: `courses/computer-vision/dataset/odi.jpg` (sample image for sessions 01 to 05) and `13-final-exam/submission/dataset/` (six photos of a toy car, taken for the exam). Both are personal photos with no public source. These are the only data files left in the repo.
- The old computer-vision images (celebrity face photos, TV-show stills and Pokemon pictures) were removed from the repo because they were third-party material. The scripts now use the public datasets above, so accuracy and match results differ from the old outputs.
