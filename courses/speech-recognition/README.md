# Speech Recognition

Notebooks that go from handling audio files to feature extraction, classical models, a pretrained speech-to-text model, speech synthesis, and a small keyword-spotting CNN.

## Contents

| Folder | Notebook | Topic |
|---|---|---|
| `01-introduction` | `python-basics.ipynb`, `python_basics.py` | Python basics for the course |
| `02-audio-library/audio-manipulation` | `audio-manipulation.ipynb` | Read, write and augment audio with soundfile, wave, pydub and librosa |
| `03-mfcc` | `mfcc.ipynb` | MFCC feature extraction |
| `04-hmm-gmm` | `mfcc-and-gmm.ipynb` | MFCC features and a Gaussian mixture model |
| `05-wav2vec` | `wav2vec2-speech-to-text.ipynb` | Speech-to-text with Wav2Vec2 |
| `06-text-to-speech` | `speech-to-text-and-text-to-speech.ipynb` | Speech recognition and speech synthesis with gTTS (see its own README) |
| `07-keyword-spotting` | `keyword-spotting-*.ipynb`, `quiz-1` to `quiz-6` | CNN keyword spotting on Speech Commands |

The task description for the keyword-spotting exercise is `07-keyword-spotting/Keyword Spotting Exercise.md`.

## Getting Started

1. Install [uv](https://docs.astral.sh/uv/). It provides Python 3.13 automatically.
2. Install the dependencies for the whole course (from this folder):
   ```bash
   uv sync
   ```
3. Open a notebook in VS Code with the `.venv` kernel, or start Jupyter with `uv run --with jupyterlab jupyter lab`. Run each notebook from its own folder, since the small sample audio files (`sample.wav`, `sample_audio.wav`, `speech.wav`) are read by relative path.

## Datasets

- **Keyword spotting:** `keyword-spotting-review-2.ipynb` downloads Google Speech Commands v0.02 (about 2.3 GB) on first run and keeps only four keywords (`follow`, `learn`, `tree`, `visual`) in `~/.cache/ml-notebooks/speech-commands`. The other keyword-spotting notebooks read from that folder, so run `keyword-spotting-review-2.ipynb` first.
- **Everything else** uses the small sample audio files committed next to each notebook.

See [Datasets.md](../../Datasets.md) for the sources.

## Notes

- `pydub` needs `audioop-lts` on Python 3.13, which the environment already includes. Exporting formats other than WAV also needs [FFmpeg](https://ffmpeg.org/) on your `PATH`.
- `audio-manipulation.ipynb` writes its generated audio files to a temporary folder (`ml-notebooks/audio-manipulation` under your system temp directory), not into the repo.
- Hugging Face models used in `05-wav2vec` and `06-text-to-speech` download on first run.
