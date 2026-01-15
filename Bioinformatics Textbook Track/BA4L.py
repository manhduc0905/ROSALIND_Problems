#!/usr/bin/env/python
import os
import numpy as np
from Bio.Data import IUPACData
from collections import Counter
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

def LinearSpectrum(peptide):
    prefix_mass = [0]
    for aa in peptide:
        prefix_mass.append(prefix_mass[-1] + aa)
    
    spectrum = [0]
    for i in range(len(peptide)):
        for j in range(i + 1, len(peptide) + 1):
            spectrum.append(prefix_mass[j] - prefix_mass[i])
    return sorted(spectrum)
    
def score(peptide, spectrum, mode = "linear"):
    i = 0
    j = 0
    if (mode == "linear"):
        exp_spectrum = LinearSpectrum(peptide)
    if (len(exp_spectrum) == 0):
        return 0
    score = 0
    while (i < len(exp_spectrum) and j < len(spectrum)):
        if (exp_spectrum[i] == spectrum[j]):
            score += 1
            i += 1
            j += 1
        elif (exp_spectrum[i] > spectrum[j]):
            j+=1
        else:
            i+=1
    return score
def cut(N, leaderboard, spectrum):
    if len(leaderboard) <= N:
        return leaderboard
    
    new_ldb = []
    for peptide in leaderboard: 
        new_ldb.append((score(peptide, spectrum), peptide))
  
    new_ldb.sort(reverse=True)
    threshold_score = new_ldb[N-1][0]
    
    final_cut = []
    for s, p in new_ldb:
        if s >= threshold_score:
            final_cut.append(p)
        else:
            break
            
    return final_cut
protein = f1.readline().strip().split()
mp = {}
leaderboard = []
for prt in protein:
    cur = [aa_masses[x] for x in prt]
    leaderboard.append(cur)
    mp[tuple(cur)] = prt
theory_spectrum = list(map(int, f1.readline().strip().split()))
N = int(f1.readline().strip())
f2.write(' '.join([mp[tuple(x)] for x in cut(N, leaderboard, theory_spectrum)]))



