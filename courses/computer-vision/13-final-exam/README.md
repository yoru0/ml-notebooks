# Computer Vision Final Exam

Computer vision mini-project for a final exam. It explores a full local-feature pipeline (Gaussian smoothing → Canny edges → Harris corners → descriptor extraction → matching → homography via RANSAC) in two notebook versions: a deliberately unstable baseline and a corrected, annotated pass.

## Setup
1) Install Python 3.10+ and pip.  
2) (Optional) Create a virtual environment: `py -m venv venv && .\\venv\\Scripts\\activate`.  
3) Install deps: `pip install -r requirements.txt`. If you do not already have a notebook runtime, add `pip install jupyter`.  
4) Add your own image pairs into `submission/data/`.

## Running the notebooks
- Open either notebook in Jupyter/VS Code. Start with `vision_engine_v1.ipynb` to see the unstable behavior, then compare against `vision_engine_v2.ipynb` to trace the fixes (notably the Gaussian kernel normalization and parameter tuning across the pipeline).  
- Update the image path constants at the top of each notebook if your filenames differ. Execution prints OpenCV/NumPy versions and visualizes each stage inline.

## Notes
- Outputs in `Output/` are sample results from the corrected pipeline; they are not used programmatically.  
- All code is CPU-only; no GPU dependencies are required.
