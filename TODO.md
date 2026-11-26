# TODO

## Decisions needed

- [ ] `projects/stock-forecasting`: the notebook downloads data up to today, so results drift on every run (R² was 0.963 on data through 2025-06-18, 0.917 now). Pin `end` to 2025-06-18 if you want stable numbers.
- [ ] Which `.wav` files are course-supplied and may stay committed: `courses/speech-recognition/02-audio-library/audio-manipulation/sample.wav`, `03-mfcc/sample_audio.wav`, `04-hmm-gmm/sample_audio.wav`, `05-wav2vec/speech.wav`. Everything else should be downloaded by its notebook and listed in `Datasets.md`.
- [ ] Five NLP menu notebooks need keyboard input and cannot run unattended (see the NLP README). Leave them, or add a non-interactive path.
- [ ] `projects/dog-breed-classification`: delete or rewrite `test.py` and `baseline_cnn.py` (unrunnable Kaggle scratch scripts), and decide whether to keep the tracked `results/eda/*.csv`.

## Not re-run yet

- [ ] `projects/skin-cancer-classification`: needs a CUDA build of torch (about 1 hour on CPU). Old outputs are kept and include stale Colab text.
- [ ] `projects/dog-breed-classification` (3 notebooks): needs a Kaggle login for `kagglehub.competition_download`. Path edits are untested.
- [ ] Courses not yet cleaned: computer-vision (`.py` scripts), deep-learning, speech-recognition.
- [ ] No saved outputs: `courses/deep-learning/09-generative-models/generative-adversarial-network.ipynb`, `courses/speech-recognition/01-introduction/python-basics.ipynb`, `courses/speech-recognition/06-text-to-speech/speech-to-text-and-text-to-speech.ipynb`. Run them where possible. Leave the GAN notebook as it is, with a README note, if it won't finish.

## Housekeeping

- [ ] Empty untracked `assets/` folders (for example `courses/natural-language-processing/06-quiz/assets`).
- [ ] Delete the leftover clone `../ml-notebooks-rewrite` and, once happy with the rewritten history, the backup `../ml-notebooks-backup.git`.
- [ ] On machines where Python rejects site certificates (`CERTIFICATE_VERIFY_FAILED`), set `SSL_CERT_FILE` to the environment's certifi bundle before running notebooks that download over HTTPS.
