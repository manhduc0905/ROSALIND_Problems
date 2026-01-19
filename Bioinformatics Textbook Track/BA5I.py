#!/usr/bin/env python3
import os
import numpy as np
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path_in = os.path.join(script_dir, "input.INP")
file_path_out = os.path.join(script_dir, "output.OUT")
f1 = open(file_path_in, "r")
f2 = open(file_path_out, "w")

s1 = f1.readline().strip()
s2 = f1.readline().strip()
s1 = " " + s1
s2 = " " + s2
n = len(s1)
m = len(s2)
d = -2
dp = np.zeros((n, m), dtype = int)
trace = np.zeros((n, m), dtype = int)
#dp[0, 1:] = d * np.arange(1, m)
#dp[1:, 0] = d * np.arange(1, n)
dp[0][0] = 0
trace[1:, 0] = 2
for i in range(1,n):
    for j in range(1,m):
        diag = (dp[i-1][j-1] + 1, 3) if (s1[i] == s2[j]) else (dp[i-1][j-1] + d,3)
        left = (dp[i][j-1] +d, 1)
        up = (dp[i-1][j] + d, 2)
        dp[i][j], trace[i][j] = max(diag, left, up)
max_score = np.max(dp[n-1, :])
i, j = n-1, np.argmax(dp[n-1, :])
align1 = []
align2 = []
while i > 0 and j > 0:
    if (trace[i][j] == 3):
        align1.append(s1[i])
        align2.append(s2[j])
        i -=1
        j -=1
    elif (trace[i][j] == 1):
        align1.append("-")
        align2.append(s2[j])
        j-=1
    else:
        align2.append("-")
        align1.append(s1[i])
        i -=1
align1.reverse()
align2.reverse()
f2.write(f"{int(max_score)}\n")
f2.write(''.join(map(str,align1)) + "\n")
f2.write(''.join(map(str,align2)) + "\n")


        