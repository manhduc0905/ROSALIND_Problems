#!/usr/bin/env/python
import os
import numpy as np
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path_in = os.path.join(script_dir, "input.INP")
file_path_out = os.path.join(script_dir, "output.OUT")
f1 = open(file_path_in, "r")
f2 = open(file_path_out, "w")
seq1 = f1.readline().strip()
seq2 = f1.readline().strip()
n = len(seq1)
m = len(seq2)
seq1 = " " + seq1
seq2 = " " + seq2
dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
trace = [["" for _ in range(m + 1)] for _ in range(n + 1)]
for i in range(n+1):
    dp[i][0] = 0
for j in range(m+1):
    dp[0][j] = 0
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if (seq1[i] == seq2[j]):
            dp[i][j] = dp[i-1][j-1] + 1
            trace[i][j] = "D"
        else:
            dp[i][j], trace[i][j] = max((dp[i-1][j], "U"), (dp[i][j-1], "L"))
trace = np.array(trace)
i = n
j = m
ans = ""
while i >= 0 and j >= 0:
    next = trace[i][j]
    if (trace[i][j] == "D"):
        ans = seq1[i] + ans
        i -=1
        j -=1
    elif (trace[i][j] == "L"):
        j -=1
    else:
        i -=1
f2.write(ans)


            

    