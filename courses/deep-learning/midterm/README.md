# Deep Learning Mid Exam

The repo bundles two notebook-based solutions: a regression model for indoor climate forecasting and a generative/classification pipeline for a CIFAR-style image subset.

## Environment setup
1) Create and activate a virtual environment (Python 3.10+ recommended):
```
py -m venv .venv
.\.venv\Scripts\activate
```
2) Install dependencies:
```
pip install -r requirements.txt
```
   If you do not already have Jupyter, add `pip install notebook` or use VS Code's built-in notebook support.

## Running the notebooks
- Problem 1 (room temperature regression): open `submission/number1/number1.ipynb` and run all cells. Data loads from `./data/room_climate-location_C-measurement14.csv` and `...15.csv` by default; the model forecasts the next-step temperature from current climate readings.
- Problem 2 (VAE + classifier): ensure `student_id` is set in `submission/number2/get_class_to_work.ipynb` (already set to use class `poppy`), then run `submission/number2/number2.ipynb` sequentially to train the VAE, generate images, construct the dataset, and train/evaluate the classifier variants.

All reported metrics and plots are captured in the respective notebooks and summarized in `Jawaban.pdf`.
