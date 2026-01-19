#!/usr/bin/env/python
import os
import numpy as np
from Bio.Align import substitution_matrices
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path_in = os.path.join(script_dir, "input.INP")
file_path_out = os.path.join(script_dir, "output.OUT")
pam250 = substitution_matrices.load("PAM250")
f1 = open(file_path_in, "r")
f2 = open(file_path_out, "w")
indel_penalty = -5
seq1 = f1.readline().strip()
seq2 = f1.readline().strip()
n = len(seq1)
m = len(seq2)
seq1 = " " + seq1
seq2 = " " + seq2
dp = np.zeros((n+1, m + 1), dtype = int)
trace = np.zeros((n+1, m+ 1), dtype = int)
trace[:, 0] = 2 
trace[0, :] = 3
trace[0, 0] = 0
maxer = (-1, 0, 0)
for i in range(1,n+1):
    for j in range(1,m+1):
        score = pam250[seq1[i]][seq2[j]]
        trc = 0
        diag = dp[i-1][j-1] + score
        up   = dp[i-1][j]   + indel_penalty
        left = dp[i][j-1]   + indel_penalty
        best_val = 0
        best_dir = 0
        if diag > best_val:
            best_val = diag
            best_dir = 1
        if up > best_val:
            best_val = up
            best_dir = 2
        if left > best_val:
            best_val = left
            best_dir = 3
        dp[i][j] = best_val
        trace[i][j] = best_dir
max_score = np.max(dp)
max_idx = np.unravel_index(np.argmax(dp), dp.shape)
i, j = max_idx[0], max_idx[1]
print(max_score)
align1 = []
align2 = []
while dp[i][j] > 0:
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
f2.write(f"{int(max_score)}\n")
f2.write(''.join(map(str,align1)) + "\n")
f2.write(''.join(map(str,align2)) + "\n")
        