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
def expand(peptides):
    new_set = []
    for x in peptides:
        for y in value_list:
            new_set.append(x + [y])
    return new_set

def consistent(peptide, spectrum):
    n = len(peptide)
    if (n == 1):
        if peptide[0] not in spectrum:
            return False
        else:
            return True
    if (sum(peptide) not in spectrum):
        return False
    
    for k in range(n-1):
        for i in range(n - k + 1):
            if (sum(peptide[i:i+k+1]) not in spectrum):
                return False
    return True

def CycloSpectrum(peptide):
    n = len(peptide)
    spectrum = [0, sum(peptide)]
    dummy = peptide + peptide[:n-1]
    for i in range(n):
        for k in range(n-1):
            #print(k)
            spectrum.append(sum(dummy[i:i+k+1]))
    spectrum.sort()
    return spectrum

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
    else:
        exp_spectrum = CycloSpectrum(peptide)
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


def Leaderboard_CycloPeptideSequencing(N, spectrum):
    leaderboard = [[]]
    lead_peptide = []
    while leaderboard:
        leaderboard = expand(leaderboard)
        new_leaderboard = []
        for peptide in leaderboard:
            if (sum(peptide) == spectrum[-1]):
                if (score(peptide, spectrum, "cyclo") > score(lead_peptide, spectrum, "cyclo")):
                    lead_peptide = peptide
            elif (sum(peptide) <= spectrum[-1]):
                new_leaderboard.append(peptide)
        new_leaderboard = cut(N, new_leaderboard, spectrum)
        leaderboard = new_leaderboard
    return lead_peptide 

def SpectralConv(M, spectrum):
    n = len(spectrum)
    a = []
    for i in range(n):
        for j in range(i):
            if (spectrum[i] == spectrum[j]):
                break
            subtract = spectrum[i] - spectrum[j]
            if (subtract >= 57 and subtract <= 200):
                a.append(subtract)
    counts = Counter(a)
    sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    res = []
    if len(sorted_counts) <= M:
        return [x[0] for x in sorted_counts]
    
    threshold_count = sorted_counts[M-1][1]
    final_masses = []
    for mass, count in sorted_counts:
        if count >= threshold_count:
            final_masses.append(mass)
        else:
            break
            
    return final_masses
    

M = int(f1.readline().strip())
N = int(f1.readline().strip())
spectrum = list(map(int,(f1.readline().strip().split())))
spectrum.sort()
value_list = SpectralConv(M,spectrum)
print(value_list)
final_set = Leaderboard_CycloPeptideSequencing(N, spectrum)
f2.write('-'.join(map(str, final_set)) + " ")


