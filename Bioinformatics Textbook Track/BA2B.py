#!/usr/bin/env/python
from itertools import product
f1 = open("input.INP", "r")
f2 = open("output.OUT", "w")
k = int(f1.readline().strip())
sequences = [s for s in f1.read().split() if s]
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
    
def median_string():
    dist = float('inf')
    med = ""
    for kmer in all_kmer:
        d = dist_cal(kmer)
        if (dist > d):
            dist = d
            med = kmer
    return med

f2.write(median_string())







#table = {y:[0 for x in range(m)] for y in nu}
#print(table)
# for col in range(m):
#     for row in range(n):
#         table[sequences[row][col]][col] += 1
# consensus_seq = []
# for row in range(m):
#     cur = ["N", -1]
#     for x in nu:
#         if (cur[1] < table[x][row]):
#             cur = [x, table[x][row]]
#     consensus_seq.append(cur[0])


