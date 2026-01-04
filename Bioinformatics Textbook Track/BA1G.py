#!/usr/bin/env/python
f1 = open("input.INP", "r")
f2 = open("output.OUT", "w")
from scipy.spatial.distance import hamming
seq1 = list(f1.readline().strip())
seq2 = list(f1.readline().strip())
f2.write(f"{int(hamming(seq1,seq2)*len(seq1))}")
#f2.write(hamming(seq1,seq2))