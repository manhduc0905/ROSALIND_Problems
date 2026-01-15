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

def CycloSpectrum(peptide):
    n = len(peptide)
    dummy_string= peptide + peptide[:n-1]
    pre = [0]*len(dummy_string)
    pre[0] = aa_masses[dummy_string[0]]
    for i in range(1,len(dummy_string)):
        pre[i] = pre[i-1] + aa_masses[dummy_string[i]]
    spectrum = [0, pre[n-1]]
    for i in range(n):
        for k in range(n-1):
            before = 0 if i == 0 else pre[i-1]
            spectrum.append(pre[i+k] - before)
    spectrum.sort()
    return spectrum

prt = f1.readline().strip()
exp_spectrum = list(map(int,(f1.readline().strip().split())))
theory_spectrum = CycloSpectrum(prt)
i = 0
j = 0
score = 0
while (i < len(exp_spectrum) and j < len(theory_spectrum)):
    if (exp_spectrum[i] == theory_spectrum[j]):
        score += 1
        i += 1
        j += 1
    elif (exp_spectrum[i] > theory_spectrum[j]):
        j+=1
    else:
        i+=1
f2.write(f"{score}")