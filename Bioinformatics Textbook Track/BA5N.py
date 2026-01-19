#!/usr/bin/env python3
import os
import numpy as np
from collections import deque
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path_in = os.path.join(script_dir, "input.INP")
file_path_out = os.path.join(script_dir, "output.OUT")
f1 = open(file_path_in, "r")
f2 = open(file_path_out, "w")

graphs = [x.split('\n') for x in f1.read().strip().split('\n\n')]

def topo_sort(mp, nodes, in_deg):
    queue = deque()
    ans = []
    for node in nodes:
        if (in_deg[node] == 0):
            queue.append(node)
    while queue:
        top = queue.popleft()
        ans.append(top)
        for x in mp[top]:
            in_deg[x] -= 1
            if (in_deg[x] == 0):
                queue.append(x)
    return ', '.join(map(str, ans))

for graph in graphs:
    mp = {}
    in_deg = {}
    nodes = set()
    for line in graph:
        u, neighbor = line.split(' -> ')
        u = int(u)
        neighbor = list(map(int,neighbor.split(',')))
        if u not in nodes: 
            mp[u] = []
            in_deg[u] = 0
            nodes.add(u)
        for v in neighbor:
            if v not in nodes: 
                mp[v] = []
                in_deg[v] = 0
            if v not in mp[u]:
                mp[u].append(v)
                in_deg[v] += 1
            nodes.add(v)
    ans = topo_sort(mp, nodes, in_deg)
    if (ans):
        f2.write(f"{ans}\n")
    else:
        f2.write("-1\n")