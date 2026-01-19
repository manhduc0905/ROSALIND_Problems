#!/usr/bin/env python3
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

s1 = f1.readline().strip()
s2 = f1.readline().strip()
s1 = " " + s1
s2 = " " + s2
n = len(s1)
m = len(s2)
indel_ext = -1
indel_opening = -11
NEG_INF = -999999999
dp = np.zeros((n, m, 3), dtype = int)
trace = np.zeros((n, m, 3), dtype = int)
for j in range(1,m):
    dp[0,j,0] = NEG_INF
    dp[0,j,1] = indel_opening + (j-1)*indel_ext
    dp[0,j,2] = NEG_INF
    trace[0,j,1] = 1
for i in range(1,n):
    dp[i,0,0] = NEG_INF
    dp[i,0,1] = NEG_INF
    dp[i,0,2] = indel_opening + (i-1)*indel_ext
    trace[i,0,2] = 2
dp[0,0,0] = 0
for i in range(1,n):
    for j in range(1,m):
        score = blosum62[s1[i]][s2[j]]
        #Diag
        dp[i][j][0], trace[i][j][0] = max(
            (dp[i-1][j-1][0], 0),
            (dp[i-1][j-1][1], 1),
            (dp[i-1][j-1][2], 2)
        ) 
        #Left
        dp[i][j][1], trace[i][j][1] = max(
            (dp[i][j-1][0] + indel_opening, 0),
            (dp[i][j-1][1] + indel_ext, 1)
        )
        #Up
        dp[i][j][2], trace[i][j][2] = max(
            (dp[i-1][j][0] + indel_opening,0),
            (dp[i-1][j][2] + indel_ext,2)
        )
        dp[i][j][0] += score
current_state = np.argmax(dp[i, j, :])
max_score = np.max(dp[n-1, m-1, current_state])
i, j = n-1, m-1
align1 = []
align2 = []
while i > 0 and j > 0:
    if current_state == 0:  # M
        align1.append(s1[i])
        align2.append(s2[j])
        prev_state = trace[i, j, 0]
        i -= 1
        j -= 1
    elif current_state == 1:  
        align1.append("-")
        align2.append(s2[j])
        prev_state = trace[i, j, 1]
        j -= 1
    else:  
        align1.append(s1[i])
        align2.append("-")
        prev_state = trace[i, j, 2]
        i -= 1
    current_state = prev_state
align1.reverse()
align2.reverse()
f2.write(f"{int(max_score)}\n")
f2.write(''.join(map(str,align1)) + "\n")
f2.write(''.join(map(str,align2)) + "\n")


        