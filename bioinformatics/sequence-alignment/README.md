# Sequence Alignment Playground

Notebook experiments for basic bioinformatics tasks: loading FASTA/GenBank sequences, running pairwise alignments, translating to protein, and visualising sequence statistics.

## Repository Structure
- `main.ipynb` - main analysis notebook combining alignment, translation, and summary plots.
- `sequence.fasta` / `sequence.gb` - input nucleotide sequences in FASTA and GenBank formats.
- `requirements.txt` - Python dependencies required to execute the notebook.

## Setup
1. Install Python 3.10 or newer.
2. (Optional) create and activate a virtual environment.
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Notebook Highlights
- Imports sequences with Biopython and extracts selected regions for comparison.
- Performs local and global pairwise alignments to compare fragments.
- Computes mismatch counts (Hamming) and Levenshtein distance.
- Transcribes and translates sequences to explore mRNA and protein products.
- Calculates melting temperature, GC content, and molecular weight, with Matplotlib visualisations.
- Summarises nucleotide composition using simple bar charts.
