# Sequence Alignment Playground

Notebook experiments for basic bioinformatics tasks: loading FASTA/GenBank sequences, running pairwise alignments, translating to protein, and visualising sequence statistics.

## Repository Structure
- `main.ipynb` - main analysis notebook combining alignment, translation, and summary plots.
- `sequence.fasta` / `sequence.gb` - input nucleotide sequences in FASTA and GenBank formats.
- `pyproject.toml` / `uv.lock` - Python dependencies, managed with uv.

## Setup
1. Install [uv](https://docs.astral.sh/uv/). It provides Python 3.12 automatically.
2. Install the dependencies:
   ```bash
   uv sync
   ```
3. Open `main.ipynb` with the `.venv` kernel in VS Code, or start Jupyter with `uv run --with jupyterlab jupyter lab`.

## Notebook Highlights
- Imports sequences with Biopython and extracts selected regions for comparison.
- Performs local and global pairwise alignments to compare fragments.
- Computes mismatch counts (Hamming) and Levenshtein distance.
- Transcribes and translates sequences to explore mRNA and protein products.
- Calculates melting temperature, GC content, and molecular weight, with Matplotlib visualisations.
- Summarises nucleotide composition using simple bar charts.
