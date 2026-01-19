#!/usr/bin/env/python
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path_in = os.path.join(script_dir, "input.INP")
file_path_out = os.path.join(script_dir, "output.OUT")
f1 = open(file_path_in, "r")
f2 = open(file_path_out, "w")
money = int(f1.readline().strip())
val = list(map(int, f1.readline().strip().split(',')))
val.sort()
c_max = val[-1]
dp = [float('inf') for i in range(money+1)]
dp[0] = 0
for i in range(1,money+1):
    for coin in val:
        if (i < coin): break
        dp[i] = min(dp[i], dp[(i-coin)] + 1)
f2.write(f"{dp[money]}")

 
