#!/usr/bin/env/python
import os
import numpy as np
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path_in = os.path.join(script_dir, "input.INP")
file_path_out = os.path.join(script_dir, "output.OUT")
f1 = open(file_path_in, "r")
f2 = open(file_path_out, "w")
seqs = f1.read().strip().split('\n')
big_seq = ""
for idx, seq in enumerate(seqs):
    if (idx != len(seqs) - 1):
        big_seq += seq[0]
    else:
        big_seq += seq
f2.write(big_seq)