#!/usr/bin/env/python
import os
import numpy as np
from Bio.Seq import translate, CodonTable, Seq
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path_in = os.path.join(script_dir, "input.INP")
file_path_out = os.path.join(script_dir, "output.OUT")
f1 = open(file_path_in, "r")
f2 = open(file_path_out, "w")

class rna_class:
    def __init__(self, rna_seq):
        self.rna_seq = Seq(rna_seq)
    def protein_seq(self):
        return self.rna_seq.translate(table=1, stop_symbol = "")

rna_seq = rna_class(f1.readline().strip())
f2.write(str(rna_seq.protein_seq()))

    