#!/usr/bin/env/python
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path_in = os.path.join(script_dir, "input.INP")
file_path_out = os.path.join(script_dir, "output.OUT")
f1 = open(file_path_in, "r")
f2 = open(file_path_out, "w")
n,m = map(int, f1.readline().strip().split())
score = [[[0 for _ in range(2)] for _ in range(m+1)] for _ in range(n+1)]

def inbound(node):
    x = node[0]
    y = node[1]
    if (x <= n and y <= m): return True
    return False

for i in range(n):
    line = list(map(int, f1.readline().strip().split()))
    for idx, base in enumerate(line):
        score[i][idx][0] = base

middle = f1.readline()

for i in range(n+1):
    line = list(map(int, f1.readline().strip().split()))
    for idx, base in enumerate(line):
        score[i][idx][1] = base

start = (0,0)
dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
dir = [(0,1), (1,0)]
queue = [start]

for i in range(n+1):
    for j in range(m+1):
        up = dp[i-1][j] + score[i-1][j][0] if i > 0 else 0
        down = dp[i][j-1] + score[i][j-1][1] if j > 0 else 0
        dp[i][j] = max(up, down)
f2.write(f"{dp[n][m]}")
            
            