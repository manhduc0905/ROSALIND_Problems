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
    
protein = f1.readline().strip()
spectrum = [aa_masses[x] for x in protein]
f2.write(' '.join(map(str,LinearSpectrum(spectrum))))



