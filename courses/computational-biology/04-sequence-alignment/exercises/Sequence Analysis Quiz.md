# Sequence Analysis Quiz

For the given DNA sequences:

- **Sequence A** is obtained from the FASTA file `NC_035298.fasta`.
- **Sequence B** is obtained from the FASTA file `MK312630.fasta`.

Please use **Biopython** to do the following operations.

## 1. Sequence Manipulation

a. Find and display the total length of Sequence A and B.
b. Find and display the index where the codon `GCT` first appears in Sequence A and B.
c. Take the first 13 nucleotides from Sequence A and the last 2 nucleotides from Sequence B, combine them, and reverse the result into a new sequence, **Sequence C**.

## 2. Sequence Analysis & Plotting

a. Determine and display the nucleotide base (A, C, G, T) frequency for Sequence A, B and C, with a chart using the `matplotlib` library.
b. Determine and display the GC and AT content percentage for Sequence A, B and C.
c. Determine and display the melting temperature for Sequence A, B and C (using the built-in Wallace method).
d. Determine and display the molecular weight for Sequence A, B and C.

## 3. DNA & mRNA Protein Synthesis

a. Transcribe and display DNA Sequence A, B and C into mRNA sequences.
b. Translate and display mRNA Sequence A, B and C into amino acid sequences.

## 4. Sequence Alignment & Similarities

a. Perform a **local** pairwise alignment between Sequence A and the sequence `TAACGCGTTAAGTATCCCG`, and display the alignment's score.
b. Perform a **local** pairwise alignment between Sequence B and the sequence `CTCTTGATACCAATAAAAT`, and display the alignment's score.
c. Find and display the Levenshtein distance between Sequence A and B.
