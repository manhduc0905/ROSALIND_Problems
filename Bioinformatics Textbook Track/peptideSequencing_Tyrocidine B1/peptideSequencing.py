#!/usr/bin/env/python
import os
import numpy as np
from Bio.Data import IUPACData
from collections import Counter
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path_in = os.path.join(script_dir, "data.txt")
file_path_out = os.path.join(script_dir, "sequence.txt")
f1 = open(file_path_in, "r")
f2 = open(file_path_out, "w")
EPSILON = 0.5
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
        theoretical_spectrum = LinearSpectrum(peptide)
    else:
        theoretical_spectrum = CycloSpectrum(peptide)
    if (len(theoretical_spectrum) == 0):
        return 0
    score = 0
    while (i < len(theoretical_spectrum) and j < len(spectrum)):
        diff = theoretical_spectrum[i] - spectrum[j]
        #print(diff)
        if (abs(diff) <= EPSILON):
            score += 1
            i += 1
            j += 1
        elif (diff < -EPSILON):
            i+=1
        else:
            j+=1
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
            #print(s, p)
        else:
            break
    
    return final_cut


def Leaderboard_CycloPeptideSequencing(N, spectrum):
    leaderboard = [[]]
    lead_peptide = []
    parent_mass = spectrum[-1]
    while leaderboard:
        leaderboard = expand(leaderboard)
        new_leaderboard = []
        for peptide in leaderboard:
            current_mass = sum(peptide)
            if (abs(parent_mass - current_mass) <= (2*EPSILON)):
                if (len(peptide) == 10):
                    if (score(peptide, spectrum, "cyclo") > score(lead_peptide, spectrum, "cyclo")):
                        lead_peptide = peptide
            elif (len(peptide) <= 10 and current_mass < parent_mass + EPSILON):
                new_leaderboard.append(peptide)
        new_leaderboard = cut(N, new_leaderboard, spectrum)
        leaderboard = new_leaderboard
        #print(leaderboard)
    return lead_peptide 

def SpectralConv(M, spectrum):
    n = len(spectrum)
    diff = []
    for i in range(n):
        for j in range(i):
            if (spectrum[i] == spectrum[j]):
                break
            subtract = spectrum[i] - spectrum[j]
            if (subtract >= 57 and subtract <= 200):
                diff.append(subtract)
    binned_diffs = [int(round(x)) for x in diff]
    counts = Counter(binned_diffs).most_common()
    
    return [mass for mass, count in counts[:M]]
    

M = 20
N = 2500
spectrum = list(map(float,(f1.readline().strip().split())))
spectrum.sort()
value_list = SpectralConv(M,spectrum)
print(value_list)
final_set = Leaderboard_CycloPeptideSequencing(N, spectrum)
f2.write('-'.join(map(str, final_set)) + " ")


