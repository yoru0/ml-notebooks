# Computational Biology

Introductory bioinformatics notebooks built with Python and [Biopython](https://biopython.org/). They cover working with DNA sequences, composition analysis, protein synthesis and sequence alignment.

## Contents

| Folder | Notebook | Topic |
|---|---|---|
| `01-sequence-analysis` | `sequence-basics.ipynb` | Create, slice, search and count sequences |
| `02-dna-composition-analysis` | `gc-content-and-melting-temperature.ipynb` | GC content, melting temperature, molecular weight |
| `03-protein-synthesis` | `transcription-and-translation.ipynb` | DNA to RNA to protein, codon table, 3D structure viewer |
| `04-sequence-alignment` | `fasta-genbank-alignment-exercise.ipynb` | 17-step exercise on FASTA and GenBank files |
| `04-sequence-alignment` | `sequence-analysis-quiz.ipynb` | Quiz on two NCBI sequences |
| `04-sequence-alignment` | `sequence-analysis-quiz-compact.ipynb` | Shorter version of the same quiz |

The task descriptions for session 4 are in `04-sequence-alignment/soal/`.

## Getting Started

1. Install [uv](https://docs.astral.sh/uv/).
2. Install the dependencies (from this folder):
   ```bash
   uv sync
   ```
3. Open any notebook in VS Code or Jupyter and select the `.venv` kernel. Run notebooks from their own folder, since they read the sequence files next to them.

## Notes

- Pairwise alignment uses `Bio.Align.PairwiseAligner` with match = 1, mismatch = 0 and no gap penalty (the old `pairwise2` "xx" scoring). With free gaps there are millions of equally good alignments, so the notebooks print the score and only the first few.
- GC content uses `Bio.SeqUtils.gc_fraction`, which replaced the removed `GC` function.
