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

def int_mass(string):
    mass = 0
    for mol in string:
        mass += int(aa_masses[mol])
    return mass

nrps = f1.readline().strip()
mass_table = [0]
dummy_string = nrps + nrps[:len(nrps) -1] 
pre = [0]*len(dummy_string)
pre[0] = aa_masses[dummy_string[0]]
for i in range(1,len(dummy_string)):
    pre[i] = pre[i-1] + aa_masses[dummy_string[i]]
for i in range(len(nrps)):
    for k in range(len(nrps) - 1):
        before = 0 if i == 0 else pre[i-1]
        print(dummy_string[i:i+k+1])
        mass_table.append(pre[i+k] - before)
# for k in range(len(nrps) -1):
#     for i in range(len(dummy_string) - k):
#         mass_table.append(int_mass(dummy_string[i:i+k+1]))
mass_table.append(int_mass(nrps))
mass_table.sort()
f2.write(' '.join(map(str,mass_table)))

        
    