#!/usr/bin/env/python
f1 = open("input.INP", "r")
f2 = open("output.OUT", "w")
from scipy.spatial.distance import hamming
pattern = list(f1.readline().strip())
seq = list(f1.readline().strip())
n = len(seq)
m = len(pattern)
max_hamm = int(f1.readline().strip())
ans = []
for i in range(n - m + 1):
    hamm = hamming(seq[i:i + m], pattern)*m
    if (hamm <= max_hamm):
        ans.append(i)
f2.write(" ".join(map(str,ans)))
#f2.write(f"{int(hamming(seq1,seq2)*len(seq1))}")
#f2.write(hamming(seq1,seq2))