#!/usr/bin/env/python
import os
import numpy as np
from Bio.Data import IUPACData
from collections import Counter
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path_in = os.path.join(script_dir, "input.INP")
file_path_out = os.path.join(script_dir, "output.OUT")
f1 = open(file_path_in, "r")
f2 = open(file_path_out, "w")
spectrum = list(map(int,(f1.readline().strip().split())))
spectrum.sort()
n = len(spectrum)
a = []
for i in range(n):
    for j in range(i):
        if (spectrum[i] == spectrum[j]):
            break
        a.append(spectrum[i] - spectrum[j])
a = Counter(a)
for key, val in a.items():
    for i in range(val):
        f2.write(f"{key} ")
