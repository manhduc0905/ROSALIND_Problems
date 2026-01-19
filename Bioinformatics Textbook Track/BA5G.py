#!/usr/bin/env/python
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
dp = np.zeros((n, m), dtype = int)
dp[:, 0] = np.arange(n)
dp[0, :] = np.arange(m)
dp[0][0] = 0
print(dp)
for i in range(1,n):
    for j in range(1,m):
        sub = dp[i-1][j-1] if (s1[i] == s2[j]) else dp[i-1][j-1] + 1
        delete = dp[i-1][j] + 1
        insert = dp[i][j-1] + 1
        dp[i][j] = min(sub, delete, insert)
print(dp)
f2.write(f"{dp[n-1][m-1]}")


        