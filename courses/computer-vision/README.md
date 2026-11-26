# Computer Vision

Hands-on computer vision mini-projects built with Python and OpenCV. Each folder contains a self-contained script that walks through a particular concept.

## Getting Started

1. Install [uv](https://docs.astral.sh/uv/). It provides Python 3.13 automatically.
2. Install the dependencies (from this folder):
   ```bash
   uv sync
   ```
3. Run any script from inside its own lesson folder, for example:
   ```bash
   cd 04-edge-detection
   uv run python canny_edge_detection.py
   ```

## Contents

| Folder | File | Topic |
|---|---|---|
| `01-introduction` | `introduction.py` | Load, show, edit and save an image |
| `02-image-descriptions` | `histogram_equalization.py` | Grayscale histograms and histogram equalization |
| `03-image-processing` | `thresholding_and_blur_filters.py` | Thresholding and blur filters |
| `04-edge-detection` | `canny_edge_detection.py` | Sobel, Laplacian and Canny edges |
| `05-feature-detection` | `fast_vs_orb_keypoints.py`, `harris_corner_subpixel.py` | FAST vs ORB keypoints, Harris corners with sub-pixel refinement |
| `06-image-matching` | `akaze_flann_image_matching.py`, `PoVeKamon.md` | AKAZE features with FLANN matching, and the task description |
| `07-quiz-i` | `compare_preprocessing_matching.py`, `match_objects_akaze.py`, `Quiz Help.md` | Quiz I: object matching with different preprocessing |
| `09-image-retrieval` | `color_histogram_retrieval.py` | Image retrieval by colour histogram (needs an image library that is not in the repo) |
| `10-object-detection` | `lbph_face_recognition.py` | Haar cascade face detection with LBPH recognition |
| `11-face-recognition` | `lbph_face_recognition_menu.py`, `QuizPrep.md` | Menu-driven LBPH face recognition |
| `12-quiz-ii` | `lbph_face_recognition_menu.py` | Quiz II: the face recognition menu, using the dataset from `11-face-recognition` |
| `13-final-exam` | `submission/vision-engine-v1.ipynb`, `submission/vision-engine-v2.ipynb` | Local-feature pipeline, baseline and corrected versions |

The course has no session 08. `dataset/odi.jpg` is the sample image used by sessions 01 to 05.

## Notes

- Scripts that call `cv2.imshow` (01, 02, 10, 11, 12) or `plt.show` open a window, so they need a display. The menu scripts in `11-face-recognition` and `12-quiz-ii` also wait for keyboard input.
- Generated files go to `~/.cache/ml-notebooks/computer-vision/`, not the repo: the trained `lbph_model.xml` of each menu script, and `modified_odi.jpg` from `01-introduction`.
- The `haarcascade_frontalface_default.xml` files are OpenCV's public pretrained face detector, kept next to the scripts that load it.