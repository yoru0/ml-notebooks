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

## Notes
- Some training loops run for many epochs; adjust the `epochs` argument if you are prototyping.
