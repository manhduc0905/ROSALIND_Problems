#!/usr/bin/env/python
import os
import numpy as np
from Bio.Seq import translate, CodonTable, Seq
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path_in = os.path.join(script_dir, "input.INP")
file_path_out = os.path.join(script_dir, "output.OUT")
f1 = open(file_path_in, "r")
f2 = open(file_path_out, "w")

def revcomp(s):
    return s.translate(str.maketrans('ACTG','TGAC'))[::-1]

def protein_seq(seq):
    return Seq(seq).translate(table=1, stop_symbol = "")



dna_seq = f1.readline().strip()
peptide = f1.readline().strip()
k = len(peptide)
for i in range(len(dna_seq) - k*3 + 1):
    fwd_strand = dna_seq[i:i+k*3]
    rev_strand = revcomp(fwd_strand)
    #print(fwd_strand, rev_strand)
    if (protein_seq(fwd_strand) == peptide or protein_seq(rev_strand) == peptide):
        f2.write(fwd_strand + '\n')

    