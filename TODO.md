# TODO

## Decisions needed

- [ ] `projects/stock-forecasting`: the notebook downloads data up to today, so results drift on every run (R² was 0.963 on data through 2025-06-18, 0.917 now). Pin `end` to 2025-06-18 if you want stable numbers.
- [ ] Which `.wav` files are course-supplied and may stay committed: `courses/speech-recognition/02-audio-library/audio-manipulation/sample.wav`, `03-mfcc/sample_audio.wav`, `04-hmm-gmm/sample_audio.wav`, `05-wav2vec/speech.wav`. Everything else should be downloaded by its notebook and listed in `Datasets.md`.
- [ ] Five NLP menu notebooks need keyboard input and cannot run unattended (see the NLP README). Leave them, or add a non-interactive path.
- [ ] `projects/dog-breed-classification`: delete or rewrite `test.py` and `baseline_cnn.py` (unrunnable Kaggle scratch scripts), and decide whether to keep the tracked `results/eda/*.csv`.
- [ ] Delete or rename: the empty `courses/speech-recognition/02-audio-library/audio-manipulation/scratch.ipynb`, the generic `a.png`, `f.png` and `s.png` in `courses/computer-vision/13-final-exam/output/`, and `Computer Vision Mid Exam Report.md` in the final-exam folder (looks misfiled).
- [ ] `courses/computer-vision`: `haarcascade_frontalface_default.xml` is tracked three times (sessions 10, 11, 12), and `12-quiz-ii/lbph_face_recognition_menu.py` is nearly a copy of the one in session 11.

## Missing data (cannot run until you supply it)

- [ ] `courses/computer-vision/09-image-retrieval`: needs `assets/assets/image_library/` and `assets/assets/test_image/Geography.jpg`.
- [ ] `courses/deep-learning/09-generative-models/generative-adversarial-network.ipynb`: reads `./dataset` (32×32 images) with no documented source. No saved outputs.
- [ ] `courses/deep-learning/13-final-exam/number1/room-temperature-prediction.ipynb` and `number2/vae-loss-analysis.ipynb`: read course-supplied CSVs and PNGs from `./dataset`. Add the sources to `Datasets.md` once known.
- [ ] `courses/speech-recognition/07-keyword-spotting/quiz_1.py` reads a `dataset/` folder that does not exist.

## Not re-run yet

- [ ] `projects/skin-cancer-classification`: needs a CUDA build of torch (about 1 hour on CPU). Old outputs are kept and include stale Colab text.
- [ ] `projects/dog-breed-classification` (3 notebooks): needs a Kaggle login for `kagglehub.competition_download`. Path edits are untested.
- [ ] `courses/deep-learning/11-reinforcement-learning/dqn.ipynb`: source fixed, but it would take hours on CPU (about 0.5 s per update). The old outputs, including two interrupted-run errors, are kept.
- [ ] `courses/speech-recognition/01-introduction/python-basics.ipynb`: first cell calls `input()`, so it cannot run unattended and has no saved outputs.
- [ ] TensorFlow has no GPU support on native Windows, so deep-learning notebooks run on CPU. Mention this in `courses/deep-learning/README.md`.

## Docs to improve

- [ ] `courses/deep-learning/README.md`: add a contents table, dataset sources, and a note that `09` and `13-final-exam` need course data. Several session folders have no README.
- [ ] `courses/computer-vision/07-quiz-i/README.md` and `12-quiz-ii/README.md` are one-line fragments.
- [ ] `projects/dog-breed-classification/README.md` is a single heading.

## Housekeeping

- [ ] Empty untracked `assets/` folders (for example `courses/natural-language-processing/06-quiz/assets`).
- [ ] Delete the leftover clone `../ml-notebooks-rewrite` and, once happy with the rewritten history, the backup `../ml-notebooks-backup.git`.
- [ ] On machines where Python rejects site certificates (`CERTIFICATE_VERIFY_FAILED`), set `SSL_CERT_FILE` to the environment's certifi bundle before running notebooks that download over HTTPS.
