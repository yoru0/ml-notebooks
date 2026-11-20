# Assignment Exercise

1. Read the sequence from the file `sequence.fasta` and store it in a variable `seq_a`.
2. Read the sequence from the file `sequence.gb` and store it in a variable `seq_b`.
3. Take the last 40 nucleotides from `seq_a` and reverse the order. Then store it in a variable `seq_c`.
4. Take the first 50 nucleotides from `seq_b` and store it in a variable `seq_d`.
5. Find the best local alignment score for `seq_c` and `seq_d` using default alignment scores.
6. Find the best global alignment score for `seq_c` and `seq_d` using default alignment scores.
7. Determine the Hamming distance score for `seq_c` and `seq_d`.
8. Determine the Levenshtein distance score for `seq_c` and `seq_d`.
9. Find the mRNA sequence for `seq_c` and store it in a variable `mrna_c`.
10. Find the mRNA sequence for `seq_a` and store it in a variable `mrna_a`.
11. Combine the mRNA sequences `mrna_c` and `mrna_a` and store the result in a variable `mrna_z` (`mrna_c` first, then followed by `mrna_a`).
12. Find the protein sequence for `mrna_z`.
13. Find the DNA sequence for `mrna_z` and store it in a variable `seq_z`.
14. Find the melting temperature of `seq_a` and `seq_b` using the GC method and plot it.
15. Determine the GC content of `seq_a` and `seq_b` and plot it.
16. Determine the molecular weight of `seq_a` and `seq_b` and plot it.
17. Find the nucleotide base frequency (the frequency of the nucleotides G, C, A and T) of `seq_z` and plot it.
