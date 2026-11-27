# Deep Learning

Collection of Jupyter notebooks that walk through fundamental deep learning workflows using TensorFlow and the Python data-science stack.

## Getting Started
1. Install [uv](https://docs.astral.sh/uv/). It provides Python 3.13 automatically.
2. Install the dependencies (from this folder):
   ```bash
   uv sync
   ```
3. Open a notebook in VS Code with the `.venv` kernel, or start Jupyter:
   ```bash
   uv run --with jupyterlab jupyter lab
   ```

Run each notebook from its own session folder, since data paths are relative.

## Contents

| Session | Notebook | Topic | Data |
|---|---|---|---|
| `01-neural-networks` | `bank-churn-neural-network.ipynb` | Feed-forward network for churn prediction | Downloaded (Kaggle) |
| `02-regression-and-classification` | `weather-humidity-regression.ipynb` | Regression on weather data | Downloaded (Kaggle) |
| `03-convolutional-neural-networks` | `rice-image-cnn.ipynb` | CNN image classification | Downloaded (Kaggle) |
| `05-recurrent-neural-networks` | `bahdanau-template.ipynb` | Sequence-to-sequence translation with Bahdanau attention | Downloaded (Tatoeba) |
| `06-transformers` | `vegetable-vision-transformer.ipynb` | Vision Transformer | Downloaded (Kaggle) |
| `07-unsupervised-learning` | `shoe-rbm.ipynb` | Restricted Boltzmann machine | Downloaded (Kaggle) |
| `08-autoencoders` | `shoe-vae.ipynb` | Variational autoencoder | Downloaded (Kaggle) |
| `09-generative-models` | `generative-adversarial-network.ipynb` | GAN | **Course data needed** |
| `11-reinforcement-learning` | `dqn.ipynb` | Deep Q-network | None (simulated environment) |
| `12-quiz` | `shoe-vae-v1.ipynb` | VAE quiz | Downloaded (Kaggle) |
| `13-final-exam` | `number1/`, `number2/` | Final exam notebooks | **Course data needed** |

Sessions `04` and `10` have no notebook in this repo. The session folders also hold lecture notes and exam papers as `.md` files.

## Datasets

Most notebooks download their own data the first time they run, so nothing is stored in the repo. Sources, download method and cache locations for each notebook are listed in the root [Datasets.md](../../Datasets.md).

### Needs course data

These notebooks cannot run until you supply the files yourself, because the course provided the data and there is no public source:

- `09-generative-models/generative-adversarial-network.ipynb` reads a `./dataset` folder of 32×32 images. The source is not documented, and the notebook has no saved outputs.
- `13-final-exam/number1/room-temperature-prediction.ipynb` and `13-final-exam/number2/vae-loss-analysis.ipynb` read course-supplied CSVs and PNGs from `./dataset`.

Put the files in a `dataset/` folder next to the notebook.

## Notes
- Some training loops run for many epochs; adjust the `epochs` argument if you are prototyping.
- TensorFlow has no GPU support on native Windows, so on Windows these notebooks train on CPU. Expect long runs for the larger models (`11-reinforcement-learning/dqn.ipynb` takes hours). Use WSL2 or Linux if you need a GPU.
