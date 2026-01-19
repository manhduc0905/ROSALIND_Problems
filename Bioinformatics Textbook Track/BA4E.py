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
spectrum = list(map(int,(f1.readline().strip().split())))
value_list =list(x for x in aa_masses.values() if x in spectrum)
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

def CycloPeptideSequencing(spectrum):
    peptides = [[]]
    final_peptides = set()
    while peptides:
        peptides = expand(peptides)
        new_peptides = []
        for peptide in peptides:
            if (sum(peptide) == spectrum[-1] and tuple(peptide) not in final_peptides):
                #print(CycloSpectrum(peptide), peptide)
                if (CycloSpectrum(peptide) == spectrum):
                    final_peptides.add(tuple(peptide))
            elif consistent(peptide, spectrum):
                new_peptides.append(peptide)
        peptides = new_peptides
    return final_peptides

final_set = CycloPeptideSequencing(spectrum)
print(final_set)
for x in final_set:
    f2.write('-'.join(map(str, x)) + " ")


