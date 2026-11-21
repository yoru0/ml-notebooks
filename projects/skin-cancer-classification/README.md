# Skin Cancer Classification

A notebook that classifies nine types of skin lesion from ISIC dermoscopy images with a hybrid model: an EfficientNet-B0 and a Swin-Tiny transformer (both from `timm`) whose features are combined, plus Grad-CAM heatmaps to see what the model looks at.

## Files

- `skin-cancer-hybrid-efficientnet-swin.ipynb`: image loading with `tf.keras`, the PyTorch hybrid model (EfficientNet and Swin features concatenated into a classifier head), training (10 epochs), a classification report and Grad-CAM.
- `pyproject.toml` and `uv.lock`: the Python environment, managed with uv.

## Getting Started

1. Install [uv](https://docs.astral.sh/uv/). It provides Python 3.13 automatically.
2. Install the dependencies:
   ```bash
   uv sync
   ```
3. Open the notebook in VS Code with the `.venv` kernel, or start Jupyter with `uv run --with jupyterlab jupyter lab`.

A GPU is strongly recommended for training. The environment contains both PyTorch and TensorFlow, so the install is large.

## Dataset

The notebook downloads [Skin cancer ISIC, 9 classes](https://www.kaggle.com/datasets/nodoubttome/skin-cancer9-classesisic) (2,357 images, about 826 MB) through `kagglehub` on first run. The Kaggle copy only has Train and Test folders, so the notebook pools both and splits them again 70/20/10 into train, validation and test folders in `~/.cache/ml-notebooks/skin-cancer`. Nothing is written into the repo. See [Datasets.md](../../Datasets.md).

## Notes

- The saved outputs in the notebook come from an earlier, larger copy of the data (3,780 images). Results will differ when you re-run it.
- One cell uses `google.colab.files` to download the trained weights, so that cell only works in Google Colab.
