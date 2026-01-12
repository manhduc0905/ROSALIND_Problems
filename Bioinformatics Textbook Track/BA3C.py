#!/usr/bin/env/python
import os
import numpy as np
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path_in = os.path.join(script_dir, "input.INP")
file_path_out = os.path.join(script_dir, "output.OUT")
f1 = open(file_path_in, "r")
f2 = open(file_path_out, "w")
graph = f1.read().strip().split('\n')
graph.sort()
prefix = {}
suffix = {}
print(graph)
for node in graph:
    pre = node[:-1]
    suf = node[1:]
    if (suf not in suffix): suffix[suf] = []
    if (pre not in prefix): prefix[pre] = []
    suffix[suf].append(node)
    prefix[pre].append(node)
for node in graph:
    if (node[1:] in prefix):
        f2.write(node + " -> " + prefix[node[1:]][0] + '\n')
