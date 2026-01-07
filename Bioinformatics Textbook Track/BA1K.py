#!/usr/bin/env/python
from itertools import product
f1 = open("input.INP", "r")
f2 = open("output.OUT", "w")
seq = f1.readline().strip()
k = int(f1.readline().strip())
nu = ["A", "C", "G", "T"]
patterns = [''.join(p) for p in product(nu, repeat=k)]
freq = {x:0 for x in patterns}
for i in range(len(seq) - k + 1):
    freq[seq[i:i+k]] += 1
f2.write(" ".join(map(str, freq.values())))