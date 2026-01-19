#!/usr/bin/env/python
import os
import numpy as np
import Bio.Seq 
from Bio.Align import substitution_matrices
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path_in = os.path.join(script_dir, "input.INP")
file_path_out = os.path.join(script_dir, "output.OUT")
f1 = open(file_path_in, "r")
f2 = open(file_path_out, "w")
blosum62 = substitution_matrices.load("BLOSUM62")
indel_penalty = -5
seq1 = f1.readline().strip()
seq2 = f1.readline().strip()
n = len(seq1)
m = len(seq2)
seq1 = " " + seq1
seq2 = " " + seq2
dp = np.zeros((n+1, m + 1), dtype = int)
trace = np.zeros((n+1, m+ 1), dtype = int)
dp[:,0] = np.arange(n+1)*indel_penalty
dp[0,:] = np.arange(m+1)*indel_penalty
trace[:, 0] = 2 
trace[0, :] = 3
trace[0, 0] = 0
for i in range(1,n+1):
    for j in range(1,m+1):
        score = blosum62[seq1[i]][seq2[j]]
        trc = 0
        dp[i][j], trace[i][j] = max((dp[i-1][j-1] + score,1 ), (dp[i-1][j] + indel_penalty, 2), (dp[i][j-1] + indel_penalty, 3))
i, j = n, m
align1 = []
align2 = []
while i > 0 or j > 0:
    if (trace[i][j] == 1):
        align1.append(seq1[i])
        align2.append(seq2[j])
        i -=1
        j -=1
    elif (trace[i][j] == 3):
        align1.append("-")
        align2.append(seq2[j])
        j-=1
    else:
        align2.append("-")
        align1.append(seq1[i])
        i -=1
align1.reverse()
align2.reverse()
f2.write(f"{int(dp[n][m])}\n")
f2.write(''.join(map(str, align1)) + "\n")
f2.write(''.join(map(str, align2)) + "\n")
        