#!/usr/bin/env/python
import os
import numpy as np
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path_in = os.path.join(script_dir, "input.INP")
file_path_out = os.path.join(script_dir, "output.OUT")
f1 = open(file_path_in, "r")
f2 = open(file_path_out, "w")

k = int(f1.readline().strip())
seq = f1.readline().strip()
k_mer = [seq[i:i+k] for i in range(len(seq) - k + 1)]
k_mer.sort()
f2.write('\n'.join(map(str, k_mer)))
