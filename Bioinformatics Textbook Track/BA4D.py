#!/usr/bin/env/python
import os
import numpy as np
from Bio.Data import IUPACData
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path_in = os.path.join(script_dir, "input.INP")
file_path_out = os.path.join(script_dir, "output.OUT")
aa_masses = """G 57
A 71
S 87
P 97
V 99
T 101
C 103
I 113
L 113
N 114
D 115
K 128
Q 128
E 129
M 131
H 137
F 147
R 156
Y 163
W 186"""
aa_masses = [x.split(' ') for x in aa_masses.split('\n')]
aa_masses = {x[0]:int(x[1]) for x in aa_masses}
f1 = open(file_path_in, "r")
f2 = open(file_path_out, "w")
value_list = np.unique(list(aa_masses.values()))
n = int(f1.readline().strip())
dp = [0 for _ in range(n + 1)]
dp[0] = 1
for i in range(n+1):
    for val in value_list:
        if (val > i):
            break
        dp[i] += dp[i-val]
f2.write(f"{dp[n]}")



