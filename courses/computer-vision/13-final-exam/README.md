# Computer Vision Final Exam

Computer vision mini-project for a final exam. It explores a full local-feature pipeline (Gaussian smoothing → Canny edges → Harris corners → descriptor extraction → matching → homography via RANSAC) in two notebook versions: a deliberately unstable baseline and a corrected, annotated pass.

## Setup
1) Install [uv](https://docs.astral.sh/uv/). It provides Python 3.12 automatically.
2) From the `courses/computer-vision` folder run `uv sync`. The final exam uses that shared environment.
3) Open the notebooks with the `.venv` kernel in VS Code, or start Jupyter with `uv run --with jupyterlab jupyter lab`.
4) Add your own image pairs into `submission/dataset/`.

## Running the notebooks
- Open either notebook in Jupyter/VS Code. Start with `vision-engine-v1.ipynb` to see the unstable behavior, then compare against `vision-engine-v2.ipynb` to trace the fixes (notably the Gaussian kernel normalization and parameter tuning across the pipeline).  
- Update the image path constants at the top of each notebook if your filenames differ. Execution prints OpenCV/NumPy versions and visualizes each stage inline.

## Notes
- Outputs in `Output/` are sample results from the corrected pipeline; they are not used programmatically.  
- All code is CPU-only; no GPU dependencies are required.
