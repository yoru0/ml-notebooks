# Recommender System

Notebook-based implementation of a user-user collaborative filtering recommender using the MovieLens 100K dataset.

## Overview
- Downloads MovieLens metadata and ratings directly from GroupLens.
- Builds a user-item utility matrix and computes cosine similarity between users.
- Generates top-N movie recommendations by predicting ratings from similar users.
- Includes exploratory analysis of rating distributions and dataset dimensions.

## Requirements
Install [uv](https://docs.astral.sh/uv/) (it provides Python 3.12), then install the dependencies from this folder:
```bash
uv sync
```

## Data Sources
- Movie metadata: https://files.grouplens.org/datasets/movielens/ml-100k/u.item
- Ratings data: https://files.grouplens.org/datasets/movielens/ml-100k/u.data
