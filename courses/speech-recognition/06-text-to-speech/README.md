# Text to Speech

Notebook demonstrating speech-to-text inference with Wav2Vec2 and text-to-speech synthesis using gTTS.

## Contents
- speech-to-text-and-text-to-speech.ipynb - end-to-end workflow for automatic speech recognition and speech synthesis.

## Getting Started
1. Install [uv](https://docs.astral.sh/uv/). It provides Python 3.13 automatically.
2. Install the dependencies for the whole course (from `courses/speech-recognition`):
   ```bash
   uv sync
   ```
3. Open `speech-to-text-and-text-to-speech.ipynb` with the `.venv` kernel in VS Code, or start Jupyter with `uv run --with jupyterlab jupyter lab`.

## Usage
### Speech to Text
- By default the notebook transcribes `../05-wav2vec/speech.wav`. To transcribe your own file, change `audio_path` in the notebook (it is resampled to 16 kHz).
- The generated `english.mp3` is written to `~/.cache/ml-notebooks/speech-recognition/text-to-speech/`, not to the repo.
- Run the "Speech To Text" section to load the Wav2Vec2 model, tokenize the waveform, and decode the predicted transcript.

### Text to Speech
- Update the example text string and execute the "Text To Speech" cells to synthesise audio with gTTS.
- The resulting MP3 file is written to the working directory (default `english.mp3`).

## Notes
- Hugging Face models download on first run; ensure internet connectivity for the initial execution.
- gTTS makes requests to Google services, so network access is required when generating speech.
- For GPU acceleration, install a CUDA-enabled build of PyTorch and move tensors to the GPU in the notebook.
