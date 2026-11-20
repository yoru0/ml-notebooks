# Computational Biology

Introductory bioinformatics notebooks built with Python and [Biopython](https://biopython.org/). They cover working with DNA sequences, composition analysis, protein synthesis and sequence alignment, and end with a small machine learning example on DNA k-mers.

## Contents

| Folder | Notebook | Topic |
|---|---|---|
| `01-sequence-analysis` | `sequence-basics.ipynb` | Create, slice, search and count sequences |
| `02-dna-composition-analysis` | `gc-content-and-melting-temperature.ipynb` | GC content, melting temperature, molecular weight |
| `03-protein-synthesis` | `transcription-and-translation.ipynb` | DNA to RNA to protein, codon table, 3D structure viewer |
| `04-sequence-alignment` | `fasta-genbank-alignment-exercise.ipynb` | 17-step exercise on FASTA and GenBank files |
| `04-sequence-alignment` | `sequence-analysis-quiz.ipynb` | Quiz on two NCBI sequences |
| `04-sequence-alignment` | `sequence-analysis-quiz-compact.ipynb` | Shorter version of the same quiz |
| `05-kmer-classification` | `kmer-sequence-classification.ipynb` | K-mer features and a logistic regression classifier |

The task descriptions for session 4 are in `04-sequence-alignment/exercises/`, and the sequence files are in `04-sequence-alignment/dataset/`. Useful AlphaFold links are in `03-protein-synthesis/AlphaFold Links.md`.

## Getting Started

1. Install [uv](https://docs.astral.sh/uv/).
2. Install the dependencies (from this folder):
   ```bash
   uv sync
   ```
3. Open any notebook in VS Code or Jupyter and select the `.venv` kernel. Run notebooks from their own folder, since the sequence files are read by relative path (`dataset/...`).

## Notes

- Pairwise alignment uses `Bio.Align.PairwiseAligner` with match = 1, mismatch = 0 and no gap penalty (the old `pairwise2` "xx" scoring). With free gaps there are millions of equally good alignments, so the notebooks print the score and only the first few.
- GC content uses `Bio.SeqUtils.gc_fraction`, which replaced the removed `GC` function.
- The k-mer notebook reads the two NCBI sequences from `04-sequence-alignment/dataset/`, so keep that folder where it is.
- The `.gitattributes` in the repository root keeps line endings as LF, so notebooks and sequence files look the same on every system.
