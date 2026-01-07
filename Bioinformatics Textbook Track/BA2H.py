#!/usr/bin/env/python
from itertools import product
f1 = open("input.INP", "r")
f2 = open("output.OUT", "w")
pattern = f1.readline().strip()
sequences = f1.readline().strip().split()
k = len(pattern)
m = len(sequences[0])
n = len(sequences)
nu = ["A", "C", "T", "G"]
all_kmer = [''.join(p) for p in product(nu, repeat=k)]

def hamming(seq1, seq2):
    #print(seq1,seq2)
    cnt = 0
    for idx, base in enumerate(seq1):
        if (seq2[idx] != base):
            cnt +=1
    return cnt

def dist_cal(pattern):
    min1 = [float('inf') for _ in range(n)]
    for idx,seq in enumerate(sequences):
        for i in range(m - k + 1):
            min1[idx] = min(min1[idx],hamming(seq[i:i+k], pattern))
    return sum(min1)
f2.write(f"{dist_cal(pattern)}")