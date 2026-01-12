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
n = len(seq)
graph = {}

for i in range(n - k + 1):
    read = seq[i:i+k]
    prefix = read[:-1]
    suffix = read[1:]
    if (prefix not in graph):
        graph[prefix] = []
    graph[prefix].append(suffix)
for x in graph:
    f2.write(x + " -> ")
    for idx,y in enumerate(graph[x]):
        if (idx == 0):
            f2.write(y)
        else:
            f2.write("," + y)
    f2.write("\n")





